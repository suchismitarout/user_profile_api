import pytest_html
import requests


class TestUser:
    def test_create_user_profile(self):
        data = {"Age": 25, "Email": "Rahul65@gmail.com", "Gender": "male", "Name": "Rahul", "Phone": 97886936}
        create_response = requests.post("http://127.0.0.1:5000/createuser", json=data)
        actual_response = create_response.status_code
        expected_response = 200
        assert expected_response == actual_response

    def test_get_user_profile(self):
        get_response = requests.get("http://127.0.0.1:5000/getallusers")
        expected_status_code = 200
        assert expected_status_code == get_response.status_code

    def test_update_user_profile(self):
        data = {"Age": 26, "Email": "sonam45@gmail.com", "Gender": "female", "Name": "Sonam", "Phone": 97336936}
        update_response = requests.put("http://127.0.0.1:5000/updateuser/2", json=data)
        actual = update_response.status_code
        expected = 200
        assert actual == expected

    def test_delete_user_profile(self):
        delete_response = requests.delete("http://127.0.0.1:5000/deleteuser/6")
        actual = delete_response.status_code
        expected = 200
        assert actual == expected
