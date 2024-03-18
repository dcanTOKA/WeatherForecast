from decouple import config

from service.weather_crawl_service import WeatherCrawlService


def main():
    crawl_service = WeatherCrawlService()

    urls = crawl_service.generate_urls_with_updated_dates(config("BASE_URL"), config("START_DATE"), int(config("DAYS")))

    for url in urls:
        weather_data = crawl_service.parse_weather_data(url)
        for data in weather_data:
            crawl_service.create_weather_record(data)


if __name__ == "__main__":
    main()
