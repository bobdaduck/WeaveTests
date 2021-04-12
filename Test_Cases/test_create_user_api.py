import unittest
import requests
from Pages.variables import EMAIL
from Pages.variables import PASSWORD
from Pages.variables import JWT_TOKEN
from Pages.variables import EMAIL_FOR_GENERATOR
import random

class InviteTests(unittest.TestCase):

    def setUp(self):
        self.invite_url = "https://api.weaveconnect.com/portal/v1/users/inviteUser"

        """"  # headers info from devtools
        authority: api.weaveconnect.com
        :method: POST
        :path: /portal/v1/users/inviteUser
        :scheme: https
        accept: application/json, text/plain, */*
        accept-encoding: gzip, deflate, br
        accept-language: en-US,en;q=0.9
        authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6InctMyIsInR5cCI6IkpXVCJ9.eyJBQ0xTIjp7ImZlZWRhMGU4LTBkZTMtNDE5ZS1hZTA5LTg2NWI2YjZmMDliOSI6WzIwLDIxLDMwLDQwMCw0MDEsNDAyLDQwMyw0MDQsNDA3LDQwOCw0MDksNDExLDQxMiw0MTMsNDE0XX0sImV4cCI6MTYxODE0MDY2NSwiZXhwQnVmZmVyIjoxNjE4MTY5NDY1LCJpYXQiOjE2MTgxMjYyNjUsImp0aSI6ImM4ZTdiM2EwLTI4OTktNGNjOC1hNmJmLWNjZmU0MGU1ZjY5ZCIsInR5cGUiOiJwcmFjdGljZSIsInVzZXJfaWQiOiI2MDE4YjczZC1hMThhLTQ5MWEtYTFiZC04YWY1YjVhM2RlN2QiLCJ1c2VybmFtZSI6ImpvbmF0aGFucmhhbnNlbkB5YWhvby5jb20ifQ.iOheHRKoZf1NxyLng45mYnedA6NVjmmCumaPzucvzvskSXscjHj3G65lVVU9FcJFtzn44f46k-elu8a85XERs0VojJvVdDJF3GLfhwmhDU3B7Z8jGy7aBNYxAJsACBD1MHgUJmKr8gBpRRS1Op5-xbIIGQbXxtgWUaosjZhqh2p9jFlyoDypsNdXRr2smbrW1JK87tUB0V0Fwy2TfX_d7pA-6MXco_jtRWjV8Yi8qqpmpixmZuc6yHj8zrt4E0ywHssYrKQVcLKlCMDMSigZeUo2xTXBwdNBFhqgYuQyKDVhXLKnDmw0Kk0NSqs6fFPIQnTMq2FigXBUg6zOGJ8cgQ
        content-length: 203
        content-type: application/json;charset=UTF-8
        location-id: feeda0e8-0de3-419e-ae09-865b6b6f09b9
        origin: https://app.getweave.com
        referer: https://app.getweave.com/
        sec-fetch-dest: empty
        sec-fetch-mode: cors
        sec-fetch-site: cross-site
        sec-gpc: 1
        user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
        """

        """Email: "bobdaduck63+2@gmail.com", FirstName: "API", LastName: "checker", MobileNumber: "",…}
        Email: "bobdaduck63+2@gmail.com"
        FirstName: "API"
        JobTitles: ["0eed809e-f27f-47b4-ab99-569b1f013638", "0eed809e-f27f-47b4-ab99-569b1f013639"]
        LastName: "checker"
        MobileNumber: ""
        Roles: [15, 22, 12]
        0: 15
        1: 22
        2: 12"""


    def test_invite_API(self):
        email_random_number = random.randint(0, 1000)
        random_email = EMAIL_FOR_GENERATOR.replace('{rnd}', str(email_random_number))
        headers = {
                "Authorization": "Bearer {}".format(JWT_TOKEN),
                "Location-Id": "feeda0e8-0de3-419e-ae09-865b6b6f09b9",
                "content-type": "application/json",
                }

        data = {"Email": random_email,
        "FirstName": "API" + str(email_random_number),
        "JobTitles": ["0eed809e-f27f-47b4-ab99-569b1f013638", "0eed809e-f27f-47b4-ab99-569b1f013639"],
        "LastName": "test_invite",
        "MobileNumber": "",
        "Roles": [15, 22, 12]}

        response = requests.post(self.invite_url, headers=headers, json=data)
        assert response.status_code == 200

    def test_invite_API_bad(self):
        headers = {
            "Authorization": "Bearer {}".format(JWT_TOKEN),
            "Location-Id": "feeda0e8-0de3-419e-ae09-865b6b6f09b9",
            "content-type": "application/json",
        }

        data = {"Email": "a bad email",
                "FirstName": "API",
                "JobTitles": ["0eed809e-f27f-47b4-ab99-569b1f013638", "0eed809e-f27f-47b4-ab99-569b1f013639"],
                "LastName": "test_bad_invite",
                "MobileNumber": "",
                "Roles": [15, 22, 12]}

        response = requests.post(self.invite_url, headers=headers, json=data)
        assert response.status_code == 500
        assert response.text == "{\"error\":\"Failed to Send Invite User Email\"}"

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
