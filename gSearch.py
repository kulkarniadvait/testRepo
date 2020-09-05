import requests

api_key = "AIzaSyDvxmcdL1EreE3LiGqfAmMPcaBNiW97JZY"
engine_id = "c6d1ffc4fbb4d08a9"

query = "dota2"
url = ("https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}").format(api_key,engine_id,query)

response = requests.get(url)
print(response)



