import json
import requests
import pprint
pp=pprint.PrettyPrinter(indent=4)
API_KEY= '10218686935504422'


with open('heroes_data.json', 'r+') as f:
    heroes_data = json.loads(f.read())
class SuperHeroAPI:   
    def __init__(self, API=API_KEY, data=heroes_data):
        self._token = API
        self._data = data  
        self._url=f'https://superheroapi.com/api/{self._token}'
        self._proxy={'http':'http://proxy.server:3128'}
        
    def get_hero(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}')
    
    
    
    def download_image(self, name):
        image_url=self.get_hero_image_url(name) 
        with open(f'{name}.jpg','wb') as f:
              respones = requests.get(image_url , proxies = self._proxy).content
              print(respones)
              f.write(respones)
        
        
    def get_hero_image_url(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}/image')['url']
          
        
    def _parse_api(self,url):
        response = requests.get(url, timeout=5, proxies=self._proxy)
        response.close()
        return response.json()
        
        
        
        
        
    def _get_id(self,name):
        data=heroes_data.get(name, False) 
        if data:
            return data
        else:
            raise NotFoundError( 'Name not found')
        
        
        
        
        
        
        
        
    def _parse_name(self,name):
        return name.lower().title()
    
    
    
class NotFoundError(Exception):
    pass
    
    
    
    
    
    
    
    
s=SuperHeroAPI()
result=s.get_hero('superman')
pp.pprint(result)


s.download_image('ethan hunt')
