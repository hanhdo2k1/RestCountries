from callapi import call_api,post_data
from ModelRequest import *
import os


def fuc_craw():
    api_url = os.environ.get('API_URL')
    if api_url:
        print(f"Đã lấy URL của API: {api_url}")
    else:
        print("Không thể tìm thấy biến môi trường API_URL.")
    urlPost = api_url+"/countries/"
    url = "https://restcountries.com/v3.1/all"
    data = call_api(url)
    if data:
        countries = []
        curs = []
        caps = []
        for country_data in data:
            try:
                name = country_data['name']['common']
                independent = country_data['independent']
                status = country_data["status"]
                currencies = country_data['currencies']
                capital = country_data['capital']
                region = country_data['region']
                google_maps = country_data['maps']['googleMaps']
                population = country_data['population']
                area = country_data['area']
                timezones = country_data['timezones']
                continents = country_data['continents']
                flag = country_data['flags']['png']
                
                curs = []
                caps = []
                # lưu list currencies
                for cur in currencies:
                    currencyRequest = CurrencyRequest(type=cur,name=currencies[cur]["name"],symbol=currencies[cur]["symbol"])  
                    curs.append(currencyRequest)
                # lưu list capital
                for cap in capital:
                    capitalRequest = CapitalRequest(name=cap)
                    caps.append(capitalRequest)

                # lưu list country
                country = CountryRequest(name=name,independent= independent, status= status, currencies=curs,
                                         capitals=caps, region=region,area=area, googleMaps=google_maps, population=population,
                                         timezones=', '.join(timezones), continents=', '.join(continents), flag=flag)
                countries.append(country)
                
                post_data(urlPost,country)
            except KeyError as e:
                continue     
