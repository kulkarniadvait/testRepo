import requests
import json

paraDict = {"key" : "AIzaSyDvxmcdL1EreE3LiGqfAmMPcaBNiW97JZY" , "cx" : "c6d1ffc4fbb4d08a9" , "q" : "dota2"}
# api_key = "AIzaSyDvxmcdL1EreE3LiGqfAmMPcaBNiW97JZY"
# engine_id = "c6d1ffc4fbb4d08a9"
# query = "dota2"
url = ("https://www.googleapis.com/customsearch/v1")

response = requests.get(url,params=paraDict)
#print(response.text)

responseData = response.text
#responseData = json.dumps(responseData)
responseData = json.loads(responseData)
#print(responseData["items"])
result = []

for a in responseData["items"]:
    print("##################################################")
    linkDict = {}
    linkDict["link"] = a["link"]
    result.append(linkDict)
    # for key, value in a.items():
    #     print (key," -------",value)
        
    print("##################################################")

for b in result:
    print(b)








