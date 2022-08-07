"""This file handles the parsing of arguments."""
import argparse
from argparse import Namespace


class Cli:
    """Cli objects are used to parse the arguments/flags from CLI.

    Objects of this class parse the arguments given on the command line
    when running the app.
    """

    @staticmethod
    def parse() -> Namespace:
        """Parse arguments and return as Namespace object."""
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
