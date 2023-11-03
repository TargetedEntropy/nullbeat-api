"""Load the database DSN
"""
from os import environ, path, remove
import sys
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

# Load configuration values from the .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Create the meta data used by the tables
metadata = sqlalchemy.MetaData()

# Define the DSN, check if in test mode
if "pytest" in sys.modules:
    DB_FILE = "test.db"
    try:
        remove(DB_FILE)
    except OSError:
        pass
    DATABASE_URL = "sqlite:///./test.db"
else:
    DATABASE_URL = environ.get("SQLALCHEMY_DATABASE_URI")


# Create the database engine
engine = sqlalchemy.create_engine(DATABASE_URL)


# Initalize session to be used by ORM
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()

# All your base are belong to us
Base = declarative_base()

metadata.create_all(bind=engine)
