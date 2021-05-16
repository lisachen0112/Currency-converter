import requests
import json
usd_rate = requests.get("http://www.floatrates.com/daily/USD.json").json()
eu_rate = requests.get("http://www.floatrates.com/daily/EUR.json").json()
exchange_rate = {}
exchange_rate["USD"] = usd_rate
exchange_rate["EUR"] = eu_rate
base_cur = input().upper()
while True:
    exchange_cur = input().upper()
    if not exchange_cur:
        break
    amount = float(input())
    print("Checking the cache...")
    if exchange_cur in exchange_rate:
        rate = exchange_rate[exchange_cur][base_cur.lower()]["inverseRate"]
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        r = requests.get(f"http://www.floatrates.com/daily/{exchange_cur}.json")
        exchange_rate[exchange_cur] = r.json()
        rate = r.json()[base_cur.lower()]["inverseRate"]
    print(f"Your received {round(rate * amount, 2)} {exchange_cur}.")