import unittest
import requests
from Pages.variables import EMAIL
from Pages.variables import PASSWORD
from Pages.variables import JWT_TOKEN


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.login_url = "https://api.weaveconnect.com/portal/login"
        """"  # headers info from devtools
        {username: "jonathanrhansen@yahoo.com", password: "getweave"}
        :authority: api.weaveconnect.com
        :method: POST
        :path: / portal / login
        :scheme: https
        accept: application / json, text / plain, * / *
        accept - encoding: gzip, deflate, br
        accept - language: en - US, en;
        q = 0.9
        authorization
        content - length: 62
        content - type: application / json;
        charset = UTF - 8
        location - id
        origin: https: // app.getweave.com
        referer: https: // app.getweave.com /
        sec - fetch - dest: empty
        sec - fetch - mode: cors
        sec - fetch - site: cross - site """

    def test_login_API(self):
        headers = {
                "Authorization": "Bearer {}".format(JWT_TOKEN),
                "Location-Id": "",
                "content-type": "application/json",
                }

        data = {"username": EMAIL,
                "password": PASSWORD}

        response = requests.post(self.login_url, headers=headers, json=data)
        assert response.status_code == 200

    def test_login_API_bad(self):
        headers = {
                "Authorization": "Bearer {}".format(JWT_TOKEN),
                "Location-Id": "",
                "content-type": "application/json",
                }

        data = {"username": "bad_email@yahoo.com",
                "password": "bad_password"}

        response = requests.post(self.login_url, headers=headers, json=data)
        assert response.status_code == 401

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
