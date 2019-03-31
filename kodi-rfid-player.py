# pylint: disable=E1101 

import logging, coloredlogs, json, sqlite3, time, sys

from kodipydent import Kodi
from socket import timeout as SocketTimeOut
from RfidScanner import RfidScanner


log = logging.getLogger('player')
coloredlogs.install(level='DEBUG', logger=log)

def db():
    con = sqlite3.connect('.data.db')
    con.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
    cursor = con.cursor()

    return con, cursor


def connect_to_kodi(address):
    log.debug('connect to kodi at %s', address)

    return Kodi(address, port=8080)

def on_scan(code):
    con, cursor = db()
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

if __name__ == '__main__':
    RfidScanner(on_scan)
    log.info('startup kodi-rfid-player')
    try:
        kodi = connect_to_kodi(sys.argv[1])
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        pass
