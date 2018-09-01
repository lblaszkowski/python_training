def test_delete_first_group(app1):
    app1.session.login( username="admin", password="secret")
    app1.group.delete_first_group()
    app1.session.logout()