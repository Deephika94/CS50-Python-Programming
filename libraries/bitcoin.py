import requests
import sys

try:
    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    output = response.json()
    result = output["bpi"]["USD"]["rate_float"]
    print(f"${result*coins:,.4f}")
except requests.RequestException:
    pass
