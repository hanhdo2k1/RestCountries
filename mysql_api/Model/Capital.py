class Capital:
    def __init__(self,id_capital=0,name="",id_country=0):
        self.id_capital = id_capital
        self.name = name
        self.id_country = id_country
    # Getter
    def get_id_capital(self):
        return self.id_capital
    def get_name(self):
        return self.name
    def get_id_country(self):
        return self.id_country
    # Setter methods
    def set_id_capital(self, id_capital):
        self.id_capital = id_capital
    def set_name(self, name):
        self.name = name
    def set_id_country(self, id_country):
        self.id_country = id_country