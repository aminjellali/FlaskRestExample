import requests
import json

info = {
	"price" : 3 ,
	"TVA" : 50
}
response = requests.get("http://127.0.0.1:9909/price/Cola")
print (response.text)


response_ = requests.post("http://127.0.0.1:9909/price/Lindt",json=info)

print(response_.text)

response_2 = requests.get("http://127.0.0.1:9909/price/Lindt")
print (response_2.text)
