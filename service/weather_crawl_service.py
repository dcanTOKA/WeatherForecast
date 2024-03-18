import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List

from model.weather_data import WeatherRecordModel
from repository.weather_repository import WeatherRepository


class WeatherCrawlService:
    def __init__(self):
        self.repo = WeatherRepository()

    def create_weather_record(self, weather_record: WeatherRecordModel):
        self.repo.create_weather_record(weather_record)

    @staticmethod
    def generate_urls_with_updated_dates(base_url: str, start_date: str, days: int) -> list:
        start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        updated_urls = []
        for day in range(days):
            current_date = start_datetime + timedelta(days=day)
            updated_date = current_date.strftime("%Y-%m-%d")
            updated_url = base_url.split('date=')[0] + f'date={updated_date}' + '&language=turkish&country=turkey'
            updated_urls.append(updated_url)
        return updated_urls

    @staticmethod
    def parse_weather_data(url: str) -> List[WeatherRecordModel]:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data_rows = soup.select('table.daily-history>tbody>tr')

        date_param = url.split('date=')[1].split('&')[0]
        year, month, day = map(int, date_param.split('-'))

        weather_data = []
        for row in data_rows:
            cells = row.find_all('td')
            cell_texts = [cell.get_text(strip=True) for cell in cells]

            weather_record = WeatherRecordModel(
                Hour=cell_texts[0],
                Temperature=cell_texts[1],
                FeelsLike=cell_texts[2],
                Wind=cell_texts[3],
                WindSpeed=cell_texts[4],
                Humidity=cell_texts[5],
                DewPoint=cell_texts[6],
                Pressure=cell_texts[7],
                Description=cell_texts[8],
                Year=year,
                Month=month,
                Day=day
            )
            weather_data.append(weather_record)
        return weather_data
