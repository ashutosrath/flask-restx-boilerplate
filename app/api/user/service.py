from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models.user import User


class UserService:
    @staticmethod
    def get_user_data(username):
        """ Get user data by username """
        user = User.query.filter_by(username=username).first()
        if not (user):
            return err_resp("User not found!", "user_404", 404)

        from .utils import load_data

        try:
            user_data = load_data(user)

            resp = message(True, "User data sent")
            resp["user"] = user_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def get_all_user_data():
        """ Get user data by username """
        users = User.query.all()
        if not (users):
            return err_resp("User not found!", "user_404", 404)

        from .utils import load_data

        try:
            user_data_list = []
            for user in users:
                user_data = load_data(user)
                if user_data:
                    user_data_list.append(user_data)
            resp = message(True, "User data sent")
            resp["users"] = user_data_list
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
