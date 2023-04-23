import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "i_am_a_python_developer"
