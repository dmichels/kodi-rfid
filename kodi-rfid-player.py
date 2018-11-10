# pylint: disable=E1101 

import logging, coloredlogs
import json
from kodipydent import Kodi
from socket import timeout as SocketTimeOut
import sqlite3

log = logging.getLogger('player')
coloredlogs.install(level='DEBUG', logger=log)

def init_db():
    log.debug('init database')
    con = sqlite3.connect('.data.db')
    con.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
    cursor = con.cursor()

    return con, cursor


def connect_to_kodi(address):
    log.debug('connect to kodi at %s', address)

    return Kodi(address)


if __name__ == '__main__':
    log.info('startup kodi-rfid-player')
    try:
        con, cursor = init_db()

        kodi = connect_to_kodi('192.168.1.23')
        while True:
            code = input().strip()
            log.info('read code: %s', code)
            
            for movie in cursor.execute('SELECT * FROM movies, players WHERE movies.id = ? AND movies.player = players.id', (code, )):
                log.info('found movie for code: %s', code)
                log.debug(movie)
                file_uri = movie['uri'] % movie['c_id']
                try:
                    log.debug('open player with file_uri: %s', file_uri)                    
                    kodi.Player.Open(item={'file': file_uri})
                except SocketTimeOut:
                    log.warning('operation timed out')
                break
            else:
                log.info('no movie with code: %s found', code)

    except KeyboardInterrupt:
        pass

    finally:
        con.close()