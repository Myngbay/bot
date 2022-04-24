import requests

url = "https://hotels4.p.rapidapi.com/properties/list"

querystring = {"destinationId": "1506246",
               "sortOrder": "PRICE", "locale": "en_US", "currency": "USD"}

headers = {
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    "X-RapidAPI-Key": "181a0daa7bmshd1388bcd7434e9fp1d6f80jsn50f30b5122b2"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)