from ReqResp.ModelResponse import *
from Model.Capital import Capital
from Model.Currency import Currency
from ReqResp.ModelRequest import *

def convertCapitalRequestToCapitalModel(capitalResquest:CapitalRequest):
    return Capital(name=capitalResquest.name)
def convertCapitalModelToCapitalResponse(capitalModel:Capital):
    return CapitalResponse(id_capital=capitalModel.get_id_capital(),name=capitalModel.get_name())

def convertCurrencyRequestToCurrencyModel(currencyResquest:CurrencyRequest):
    return Currency(type=currencyResquest.type,name=currencyResquest.name,symbol=currencyResquest.symbol)
def convertCurrencyModelToCurrencyResponse(currencyModel:Currency):
    return CurrencyResponse(id_currency=currencyModel.get_id_currency(),type=currencyModel.get_type(),name=currencyModel.get_name(),symbol=currencyModel.get_symbol())
