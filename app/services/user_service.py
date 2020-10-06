from app import db
from app.utils.db_utils import User
import logging
from flask import request


class UserService():
    def insert_into_db(self, data):
        """
        This method is mostly used for inserting record into the DB.
        :param data:
        :return:
        """
        try:
            # create the model object
            # Note: to create SQLAlchemy model object either pass the parameters individually
            # or if you want to pass a dictionary then put ** before that.
            input_data = User(**data)
            db.session.add(input_data)
            db.session.commit()
        except Exception as e:
            logging.error("Error occured during database interaction, Msg:{}".format(e))
            raise

    def get_data_from_db_by_id(self, id):
        """
        This method is used for getting the record from the DB by id.
        :param id:
        :return:
        """
        user_info = User.query.get(id)
        return user_info

    def get_data_from_db_by_name(self, name):
        """
        This method is used for getting record from the DB by name.
        :param name:
        :return:
        """
        user_info = User.query.filter_by(Name=name).first()
        return user_info

    def delete_data_from_db(self, id):
        """
        This method is used for deleting the record from the DB by id.
        :param id:
        :return:
        """
        try:
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            logging.error("Error occured during database interaction, Msg:{}".format(e))
            raise

    def get_all_user_profiles(self):
        """
        This method is used for getting all records from the DB.
        :return:
        """

        users = User.query.all()
        print(users)
        logging.info(users)
        user_list = []
        for user in users:
            recordobj = {"Name": user.Name, "Age": user.Age, "Gender": user.Gender, "Phone": user.Phone,
                         "Email": user.Email}
            # print("all users", recordobj)
            user_list.append(recordobj)
            # print(user.__dict__)
            logging.info(user)
        return user_list

    def update_data_in_user_profile(self, id):
        """
        This method is used for updating the record in the DB by id.
        :param id:
        :return:
        """
        user = User.query.get(id)
        Age = request.json['Age']
        user.Age = Age
        db.session.commit()
        recordobj = {"Name": user.Name, "Age": user.Age, "Gender": user.Gender, "Phone": user.Phone,
                     "Email": user.Email}
        # print(recordobj)
        logging.info(recordobj)
        return recordobj
