from app import app
from app.routes.user import user_var


if __name__ == '__main__':
    app.register_blueprint(user_var)
    print("it begins here")
    app.run()
