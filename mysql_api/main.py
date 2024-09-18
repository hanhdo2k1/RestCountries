import time
print("Mysql đang khởi động, Bạn hãy đợi 40s")
time.sleep(60)



from fastapi import FastAPI, HTTPException, Query
from typing import List
from Model.Country import Country
from ReqResp.ModelResponse import *
from ReqResp.ModelRequest import *
import DAO.CountryDAO as CountryDAO
import DAO.CapitalDAO as CapitalDAO
import DAO.CurrencyDAO as CurrencyDAO
from utils.convertObject import *
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()
# Cấu hình middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.post("/countries/", response_model=int)
async def create_country(countryRequest: CountryRequest):
    try:
        countryModel = Country(**countryRequest.__dict__)
        id = CountryDAO.insert(countryModel)
        countryModel.set_id(id)
        capitals = []
        currencies = []
        for cap in countryRequest.capitals:
                capitalModel = convertCapitalRequestToCapitalModel(cap)
                capitalModel.set_id_country(id)
                id_cap = CapitalDAO.insert(capitalModel)
                capitalModel.set_id_capital(id_cap)
                capitals.append(capitalModel)
        for cur in countryRequest.currencies:
                currencyModel = convertCurrencyRequestToCurrencyModel(cur)
                currencyModel.set_id_country(id)
                id_cur = CurrencyDAO.insert(currencyModel)
                currencyModel.set_id_currency(id_cur)
                currencies.append(currencyModel)
        countryModel.set_capitals(capitals)
        countryModel.set_currencies(currencies)
        
        return id
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/countries", response_model=List[CountryResponse])
async def search(search: str = Query(default=None)):
    try:
        if search:
            countries = CountryDAO.selectAllLikeName(search)
        else:
            countries = CountryDAO.selectAll()
        for country in countries:
            country.set_currencies(CurrencyDAO.selectAllByIdCountry(country.get_id()))
            country.set_capitals(CapitalDAO.selectAllByIdCountry(country.get_id()))
        return countries
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/countries/truncate")
async def create_country():
    for country in CountryDAO.selectAll():
        CountryDAO.deleteById(country.get_id())
    CountryDAO.reset_id()
    CapitalDAO.reset_id()
    CurrencyDAO.reset_id()