import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            '.data.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)        