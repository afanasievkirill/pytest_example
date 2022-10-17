import os


class Contact:
    def __init__(
        self,
        firstname,
        middlename,
        lastname,
        photo_path,
        nickname,
        title,
        company,
        address,
        home_phone,
        mobile_phone,
        work_phone,
        fax,
        email,
        email_2,
        email_3,
        homepage,
        bday_day,
        bday_month,
        bday_year,
        aday,
        amonth,
        ayear,
        address_2,
        home,
        notes,
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
