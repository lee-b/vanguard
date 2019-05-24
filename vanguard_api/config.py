import sys

from argparse import ArgumentParser


DEFAULT_DB_URI = 'sqlite:///test_db.sqlite'


def get_config(args):

    argparser = ArgumentParser()

    argparser.add_argument(
        '--debug',
        '-d',
        action='store_true',
        help='Enable debug-level log output'
    )

    argparser.add_argument(
        '--db-uri',
        '-u',
        action='store_true',
        help='Set Database URI. Default: ' + DEFAULT_DB_URI,
        default=DEFAULT_DB_URI
    )

    conf = argparser.parse_args(args)

    return conf
