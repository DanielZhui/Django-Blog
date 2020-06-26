import os

DEBUG = False
ALLOWED_HOSTS = [
    'blog.wollens.top'
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KRY')
