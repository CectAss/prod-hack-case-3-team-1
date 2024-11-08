import dotenv

dotenv.load_dotenv('.env')
env_values = dotenv.dotenv_values('.env')

SQLALCHEMY_URL = 'postgresql://' + env_values['DB_USERNAME'] + ':' + env_values['DB_PASSWORD'] + '@' + env_values['DB_HOST'] + '/' + env_values['DB_DBNAME']