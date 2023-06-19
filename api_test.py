import requests, sys

if len(sys.argv) != 2:
    sys.exit()

try:
    reply =  requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    sys.exit()

max = reply.json()
rate = max["bpi"]["USD"]["rate_float"]
print(rate)
amount = float(sys.argv[1])
result = amount * rate
print(result)




















# import requests
# import sys

# if len(sys.argv) != 2:
#     print("Usage: python script.py <amount>")
#     sys.exit(1)

# try:
#     response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#     response.raise_for_status()  # Check for request errors
#     data = response.json()
# except (requests.RequestException, ValueError) as e:
#     print("An error occurred:", str(e))
#     sys.exit(1)

# rate = data["bpi"]["USD"]["rate_float"]
# print("Current Bitcoin rate:", rate)

# amount = float(sys.argv[1])
# result = amount * rate
# print(f"{amount} BTC is equivalent to {result:.2f} USD")


