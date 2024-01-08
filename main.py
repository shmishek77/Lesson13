import json

import requests

response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
#print(response.text)

with open("exchange.json", "w") as f:
    json.dump(response.text, f)
print(type(f))
exchange = json.loads(response.text)
print(exchange)
print(list(exchange))
print(type(exchange))

print(exchange["Valute"])

for i in exchange["Valute"]:
    print(i)

with open("exchange.txt", "w") as f:
    f.write(str(exchange))

