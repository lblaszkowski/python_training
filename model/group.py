class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class User_data:
    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname

class User_picture:
    def __init__(self,title_photo):
        self.title_photo = title_photo

class Data_email:
    def __init__(self,  email, email2, email3):
        self.email = email
        self.email2 = email2
        self.email3 = email3

class Company_data_settings:
    def __init__(self,company,address,home,mobile, work , fax):
        self.company = company
        self.address = address
        self.home = home
        self.work  = work
        self.mobile = mobile
        self.fax = fax

class Additional_data_settings:
    def __init__(self, homepage,bday, bmonth,byear,aday, amonth,ayear, address2, phone2 , notes):
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday=aday
        self.amonth=amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes



