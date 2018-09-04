from model.group import *

def test_edition_first_group(app):
     app.session.group_page_settings()
     app.session.login( username="admin", password="secret")
     app.group.edition_first_group(Group(name="coś tam imie", header="coś tam opis", footer="coś tam stopka"))
     app.session.logout()