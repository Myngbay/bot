import requests

url = "https://hotels4.p.rapidapi.com/reviews/v2/list"

querystring = {"hotelId":"1053457920","reviewOrder":"date_newest_first","tripTypeFilter":"all"}

headers = {
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
	"X-RapidAPI-Key": "181a0daa7bmshd1388bcd7434e9fp1d6f80jsn50f30b5122b2"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)