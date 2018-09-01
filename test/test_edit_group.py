from model.group import *

def test_edition_first_group(app1):
     app1.session.group_page_settings()
     app1.session.login( username="admin", password="secret")
     app1.group.edition_first_group(Group(name="coś tam imie", header="coś tam opis", footer="coś tam stopka"))
     app1.session.logout()