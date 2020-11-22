import requests
class novelcovid:
    

    
    def __init__(self):
        pass
    
    def get_world_info(self):
        url = "https://corona.lmao.ninja/v2/all"
        response = requests.request("GET", url, headers={}, data = {}).json()
        return response
    
    def get_country_info(self, country):
        self.country = country
        url = "https://corona.lmao.ninja/v2/countries/" + self.country
        response = requests.request("GET", url, headers={}, data = {}).json()
        if response:
            return response
        else:
            return f"there are no cases of the virus in {self.country}"
        
    def get_state_info(self, state):
        self.state = state
        url = "https://corona.lmao.ninja/v2/states"
        response = requests.request("GET", url, headers={}, data = {})
        l = len(response.json())

        for i in range(l):
            if response.json()[i]['state'] == self.state:
                index = i

        return response.json()[index]
    
    
    def get_city_info(self, country, state, city):
        self.country = country
        self.state  = state
        self.city = city
        url = "https://corona.lmao.ninja/v2/jhucsse"

        r = None
        response = requests.request("GET", url, headers={}, data = {}).json()
        for i in range(len(response)):
            if response[i]['country'] == self.country  and response[i]['province'] == self.state and response[i]['city'] == self.city:
                r = response[i]
        if r:
            return r
        else:
            return f"There are no cases reports in {city}, {state}"