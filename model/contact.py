import os
from sys import maxsize


class Contact:
    def __init__(
        self,
        firstname=None,
        middlename=None,
        lastname=None,
        photo_path="/README.MD",
        nickname=None,
        title=None,
        company=None,
        address=None,
        home_phone=None,
        mobile_phone=None,
        work_phone=None,
        fax=None,
        email=None,
        email_2=None,
        email_3=None,
        homepage=None,
        bday_day=None,
        bday_month=None,
        bday_year=None,
        aday=None,
        amonth=None,
        ayear=None,
        address_2=None,
        home=None,
        notes=None,
        id=None,
    ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo_path = os.getcwd() + photo_path
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.bday_day = bday_day
        self.bday_month = bday_month
        self.bday_year = bday_year
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address_2 = address_2
        self.home = home
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (
            (self.id is None or other.id is None or self.id == other.id)
            and self.firstname == other.firstname
            and self.lastname == other.lastname
        )

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
