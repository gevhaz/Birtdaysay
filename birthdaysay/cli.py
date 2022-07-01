import argparse
from argparse import Namespace


class Cli:
    @staticmethod
    def parse() -> Namespace:
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "-c",
            "--contacts",
            action="store",
            dest="contacts_file",
            required=True,
            help="path to vCard file with your contacts",
        )

        return parser.parse_args()
