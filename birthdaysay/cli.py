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

        parser.add_argument(
            "-a",
            "--all",
            action="store_true",
            dest="all",
            required=False,
            help="Print time until everyone's birthday instead of showing desktop "
                 "notifications",
        )

        parser.add_argument(
            "-e",
            "--everyday",
            action="store_true",
            dest="everyday",
            required=False,
            help="Show notifications everyday the week before a birthay",
        )

        return parser.parse_args()
