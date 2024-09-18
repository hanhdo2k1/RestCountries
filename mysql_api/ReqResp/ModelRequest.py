from pydantic import BaseModel
from typing import List

class CapitalRequest(BaseModel):
    name: str
class CurrencyRequest(BaseModel):
    type: str
    name: str
    symbol: str
class CountryRequest(BaseModel):
    name: str
    independent: bool
    status: str
    currencies: List[CurrencyRequest]
    capitals: List[CapitalRequest]
    region: str
    area: float
    googleMaps: str
    population: int
    timezones: str
    continents: str
    flag: str