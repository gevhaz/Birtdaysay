import sys
from datetime import date, datetime
from typing import TypedDict

import gi

gi.require_version("Notify", "0.7")

from gi.repository import Notify
from vobject.base import ParseError, readComponents

from birthdaysay.cli import Cli


class Person(TypedDict):
    name: str
    birthday: date


def get_contacts(contacts_file: str) -> list[Person]:
    try:
        with open(contacts_file, "r") as f:
            contacts_data = f.read()
    except FileNotFoundError:
        print(f"The vcard file {contacts_file} doesn't seem to exist")
        return []

    all_contacts: list[Person] = []

    contact_components = readComponents(contacts_data)

    try:
        contact = next(contact_components, None)
        while contact is not None:
            name: str | None = None
            birthday: str | None = None

            if "nickname" in contact.contents:
                name = str(contact.contents["nickname"][0].value)  # type: ignore
            elif "n" in contact.contents:
                name = str(contact.contents["n"][0].value)  # type: ignore
            else:
                contact = next(contact_components, None)
                continue

            if "bday" in contact.contents:
                birthday = str(contact.contents["bday"][0].value)  # type: ignore
            else:
                contact = next(contact_components, None)
                continue

            name = name.strip().replace("  ", " ")
            name = name.replace("\u3000", " ")  # This character showed up in a contact
            birthday = birthday.strip().replace("  ", " ")
            parsed_birtday = datetime.strptime(birthday, "%Y%m%d").date()

            if birthday is not None:
                all_contacts.append({"name": name, "birthday": parsed_birtday})

            contact = next(contact_components, None)
    except ParseError as e:
        print(f"There was an error parsing the file '{contacts_file}':")
        print(e)
        return []

    return all_contacts


def main() -> int:
    args = Cli.parse()
    Notify.init("Birthdaysay")

    contacts = get_contacts(args.contacts_file)

    for c in contacts:
        next_birthday = date(date.today().year, c["birthday"].month, c["birthday"].day)
        if next_birthday < date.today():
            next_birthday = next_birthday.replace(year=date.today().year + 1)

        if next_birthday == date.today():
            notification = Notify.Notification.new(
                f"It's {c['name']}'s birtday today!",
            )
            notification.set_urgency(Notify.Urgency.CRITICAL)
            notification.show()

        elif (next_birthday - date.today()).days == 1:
            notification = Notify.Notification.new(
                "It's {c['name']}'s birthday tomorrow"
            )
            notification.show()

        elif (next_birthday - date.today()).days in [6, 7]:
            print_birtday = date.strftime(next_birthday, "%B %d")
            notification = Notify.Notification.new(
                f"It's {c['name']}'s birthday on {print_birtday}"
            )
            notification.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
