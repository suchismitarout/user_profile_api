import re


class Validator:

    def validate(self, data):
        return self.validate_age(data['Age']) and self.validate_email(data['Email'])

    def validate_age(self, age):
        try:
            int(age)
            return True
        except ValueError as e:
            print("error", e)
            return False

    def validate_email(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        try:
            re.search(regex, email)
            return True
        except ValueError as e:
            print("error", e)
            return False
