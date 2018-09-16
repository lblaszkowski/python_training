from model.group import Group

def test_edition_first_group(app):
     app.session.group_page_settings()
     app.group.edition_first_group(Group(name="coś tam imie", header="coś tam opis", footer="coś tam stopka"))
