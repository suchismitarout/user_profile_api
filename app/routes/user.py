from flask import request, jsonify, Blueprint
from app.services.user_service import UserService
from app.utils.validator import *
import logging

logging.info("Creating the UserService Routes...")

## initialize all the objects
validator = Validator()
service = UserService()

user_var = Blueprint('user', __name__)


@user_var.route('/createuser', methods=['POST'])
def create_user_profile():
    try:
        data = request.get_json()
        logging.info("Received user input..{}".format(data))

        validation_response = validator.validate(data)
        # if validation response is False, then return Error
        if not validation_response:
            return jsonify({"status": "failed", "msg": "Validation failed.."})

        # call the service class insert into db
        service.insert_into_db(data)
        return jsonify({"status": "success", "msg": "sucessfully inserted into DB"})
    except Exception:
        return jsonify({"status": "failed", "msg": "internal server error"})


@user_var.route('/getallusers', methods=['GET'])
def get_all_user_profiles():
    user = service.get_all_user_profiles()
    logging.info(user)
    return jsonify(user)


@user_var.route('/updateuser/<id>', methods=['PUT'])
def update_user_profile(id):
    user = service.update_data_in_user_profile(id)
    return jsonify(user)


@user_var.route('/deleteuser/<id>', methods=['DELETE'])
def delete_user_profile(id):
    try:
        service.delete_data_from_db(id)
        return jsonify({"status": "success", "msg": "sucessfully deleted from DB"})
    except Exception:
        return jsonify({"status": "failed", "msg": "internal server error"})
