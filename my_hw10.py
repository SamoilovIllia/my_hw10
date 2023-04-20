import re
from collections import UserDict, UserList


class Field:
    def __init__(self, value: str) -> None:
        self.val = value


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Phone(UserList):
    def find_and_add_phone(self, ph: str):
        phon = '+38' + re.findall("\d{10}", ph)[0]
        self.data.append(phon)

    def get_phone(self):
        return self.data

    def say_successfully(self):
        print(f'Phonenumber add successfully')


class Email(UserList):
    def find_and_add_emails(self, email: str):
        result = re.findall(r"[a-zA-Z][a-zA-Z0-9._]+@\w+\.[a-zA-Z]{2,}", email)
        self.data.append(result)

    def get_emails(self):
        return self.data


class Record:
    def __init__(self, name: Name, phone: Phone = None, email: Email = None):
        self.name = name
        self.phone = phone
        self.email = email

    def add_phone(self, phone: str) -> None:
        if phone not in self.phones:
            self.phones.append(phone)

    def remove_phone(self, phone: str) -> None:
        if phone in self.phones:
            self.phones.remove(phone)

    def add_email(self, email: str) -> None:
        if email not in self.emails:
            self.emails.append(email)

    def remove_email(self, email: str) -> None:
        if email in self.emails:
            self.emails.remove(email)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.val] = record

    def delete_record(self, name: str):
        del self.data[name]


def find_records(self, search_term: str):
    results = []
    for record in self.data.values():
        if search_term in record.name.val:
            results.append(record)
        else:
            for phone in record.phone.get_phone():
                if search_term in phone:
                    results.append(record)
                    break
            for email in record.email.get_emails():
                if search_term in email:
                    results.append(record)
                    break
    return results


def show_all_records(self):
    for record in self.data.values():
        print(
            f"{record.name.val}: {record.phone.get_phone()}, {record.email.get_emails()}")
