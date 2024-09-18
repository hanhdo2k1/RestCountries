class Currency:
    def __init__(self,id_currency=0,type="",name="",symbol="",id_country=0):
        self.id_currency = id_currency
        self.type = type
        self.name = name
        self.symbol = symbol
        self.id_country = id_country
    # Getter
    def get_id_currency(self):
        return self.id_currency
    def get_type(self):
        return self.type
    def get_name(self):
        return self.name
    def get_symbol(self):
        return self.symbol
    def get_id_country(self):
        return self.id_country
    # Setter
    def set_id_currency(self,id_currency):
        self.id_currency = id_currency
    def set_type(self,type):
        self.type = type
    def set_name(self,name):
        self.name = name
    def set_symbol(self,symbol):
        self.symbol = symbol
    def set_id_country(self, id_country):
        self.id_country = id_country