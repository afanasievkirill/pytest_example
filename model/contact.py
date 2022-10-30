import os


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
