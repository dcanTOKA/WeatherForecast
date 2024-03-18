from repository.base.db import session
from sqlalchemy import Integer
from model.weather_data import WeatherRecordModel


class WeatherRepository:
    def __init__(self):
        self.db_session = session

    def create_weather_record(self, weather_record: WeatherRecordModel):
        self.db_session.add(weather_record)
        self.db_session.commit()
        self.db_session.refresh(weather_record)
        return weather_record

    def get_weather_record_by_id(self, record_id: Integer):
        return self.db_session.query(WeatherRecordModel).filter(WeatherRecordModel.id == record_id).first()

    def list_weather_records(self):
        return self.db_session.query(WeatherRecordModel).all()
