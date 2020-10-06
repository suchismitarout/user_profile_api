from app import db


class User(db.Model):
    __tablename__ = "USER"

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20))
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(7))
    Phone = db.Column(db.Integer)
    Email = db.Column(db.String(50))


def __init__(self, Name, Age, Gender, Phone, Email):
    self.Name = Name
    self.Age = Age
    self.Gender = Gender
    self.Phone = Phone
    self.Email = Email


def __repr__(self):
    return f'{"Name": {self.Name}, "Age": {self.Age}, "Gender": {self.Gender}, "Phone": {self.Phone}, "Email": {self.Email}}'


# db.create_all()
# db.session.commit()
