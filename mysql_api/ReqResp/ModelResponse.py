from pydantic import BaseModel
from typing import List

class CapitalResponse(BaseModel):
    id_capital: int
    name: str
class CurrencyResponse(BaseModel):
    id_currency: int
    type: str
    name: str
    symbol: str
class CountryResponse(BaseModel):
    id: int
    name: str
    independent: bool
    status: str
    currencies: List[CurrencyResponse]
    capitals: List[CapitalResponse]
    region: str
    area: float
    googleMaps: str
    population: int
    timezones: str
    continents: str
    flag: str