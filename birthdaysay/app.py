import sys
import pprint

from vobject.base import ParseError, readComponents

from birthdaysay.cli import Cli


def get_contacts(contacts_file: str) -> list[dict[str, str | None]]:
    try:
        with open(contacts_file, "r") as f:
            contacts_data = f.read()
    except FileNotFoundError:
        print(f"The vcard file {contacts_file} doesn't seem to exist")
        return []

    all_contacts: list[dict[str, str | None]] = []

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

            if birthday is not None:
                all_contacts.append({"name": name, "birthday": birthday})

            contact = next(contact_components, None)
    except ParseError as e:
        print(f"There was an error parsing the file '{contacts_file}':")
        print(e)
        return []

    return all_contacts


def main() -> int:
    args = Cli.parse()

    contacts = get_contacts(args.contacts_file)

    pprint.pprint(contacts)

    return 0


if __name__ == "__main__":
    sys.exit(main())
