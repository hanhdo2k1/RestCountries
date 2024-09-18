class Country:
    def __init__(self,id=0,name="",independent=True,status="",currencies=[],capitals=[],region="",area=0,googleMaps="",population=0,timezones="",continents="",flag=""):
        self.id = id
        self.name = name
        self.independent = independent
        self.status = status
        self.currencies = currencies
        self.capitals = capitals
        self.region = region
        self.area = area
        self.googleMaps = googleMaps
        self.population = population
        self.timezones = timezones
        self.continents = continents
        self.flag = flag
    # Getter
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_independent(self):
        return self.independent
    def get_status(self):
        return self.status
    def get_currencies(self):
        return self.currencies
    def get_capitals(self):
        return self.capitals
    def get_region(self):
        return self.region
    def get_area(self):
        return self.area
    def get_google_maps(self):
        return self.googleMaps
    def get_population(self):
        return self.population
    def get_timezones(self):
        return self.timezones
    def get_continents(self):
        return self.continents
    def get_flag(self):
        return self.flag
    # Setter
    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_independent(self, independent):
        self.independent = independent
    def set_status(self, status):
        self.status = status
    def set_currencies(self, currencies):
        self.currencies = currencies
    def set_capitals(self, capitals):
        self.capitals = capitals
    def set_region(self, region):
        self.region = region
    def set_area(self, area):
        self.area = area
    def set_google_maps(self, google_maps):
        self.googleMaps = google_maps
    def set_population(self, population):
        self.population = population
    def set_timezones(self, timezones):
        self.timezones = timezones
    def set_continents(self, continents):
        self.continents = continents
    def set_flags(self, flag):
        self.flag = flag