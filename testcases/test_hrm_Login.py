import pytest

from POM_Login.Login import Login

@pytest.mark.usefixtures("setup")
class Testing:
    def test_login(self,setup):
        obj = Login(setup)
        obj.login("Admin","admin123")
        obj.logout()
