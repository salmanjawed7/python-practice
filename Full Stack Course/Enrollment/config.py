import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "i_am_a_python_developer"
    WTF_CSRF_SECRET_KEY = SECRET_KEY
    MONGODB_SETTINGS = {
        'db': 'UTA_Enrollment',
    }
