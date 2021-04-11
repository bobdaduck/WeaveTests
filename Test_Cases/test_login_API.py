import unittest
import requests
import json
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

        data = {"username": "jonathanrhansen@yahoo.com",
                "password": "getweave"}

        response = requests.post(self.login_url, headers=headers, json=data)
        print(response.text)
        assert response.status_code == 200
        # NOTE: Most API calls will require the `Location-Id` header to be set.
        # r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
        # r.status_code
        # r.headers['content-type']
        # r.text
        # r.json()
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
