import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from quart import g

from vanguard_core.plugin import Plugin
from vanguard_db import DBPlugin, make_engine, make_session

from .app import app
from .plugin import APIPlugin
from .config import get_config



@app.teardown_appcontext
def _shutdown_db_session(exception=None):
    global app
    app.db_session.remove()


def _setup_db_session(config):
    global app

    engine = create_engine(
        config.db_uri,
        convert_unicode=True
    )

    app.db_session = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    )


def main():
    config = get_config(sys.argv[1:])

    _setup_db_session(config)

    global app
    assert app.db_session is not None

    config.plugins = [
        Plugin.load_plugins('vanguard_plugins', plugin_type)
        for plugin_type in (DBPlugin, APIPlugin)
    ]

    try:
        app.run(debug=bool(config.debug))
    except KeyboardInterrupt:
        print("User-interrupt.  Exiting.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())