import sqlalchemy
from sqlalchemy.orm import sessionmaker

from enums.config_db import ConfigDB
from model.weather_data import Base

if len(ConfigDB.DB_USER.value) + len(ConfigDB.DB_PASSWORD.value) != 0:
    DATABASE_URL = f"postgresql://{ConfigDB.DB_USER.value}:{ConfigDB.DB_PASSWORD.value}@{ConfigDB.DB_HOST.value}:{ConfigDB.DB_PORT.value}/{ConfigDB.DB_NAME.value}"
else:
    DATABASE_URL = f"postgresql://{ConfigDB.DB_HOST.value}:{ConfigDB.DB_PORT.value}/{ConfigDB.DB_NAME.value}"

engine = sqlalchemy.create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


