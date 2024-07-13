import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_long_random_string_that_should_be_kept_secret_because_it_is_super_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
