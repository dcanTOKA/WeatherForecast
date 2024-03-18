from datetime import date

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WeatherRecordModel(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    Hour = Column(String)
    Temperature = Column(String)
    FeelsLike = Column(String)
    Wind = Column(String)
    WindSpeed = Column(String)
    Humidity = Column(String)
    DewPoint = Column(String)
    Pressure = Column(String)
    Description = Column(String)
    Year = Column(Integer)
    Month = Column(Integer)
    Day = Column(Integer)
