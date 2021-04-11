# This file imports our environment variables to be used by each class
import os

URL = os.getenv('URL')

EMAIL = os.getenv('EMAIL')
EMAIL_FOR_GENERATOR = os.getenv('GENERATOR_EMAIL')  # format: youremail+{rnd}@gmail.com
PASSWORD = os.getenv('PASSWORD')

JWT_TOKEN = os.getenv("JWT")
