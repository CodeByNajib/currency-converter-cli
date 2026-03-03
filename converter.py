# Del 1 — Imports øverst i converter.py:
import argparse
import os
import requests
from dotenv import load_dotenv


# Del 2 — Opsæt argparse og indlæs API-nøgle:
def get_api_key():
    parser = argparse.ArgumentParser(description="Currency Converter CLI")
    parser.add_argument("--key", help="Your ExchangeRate API key")
    args = parser.parse_args()

    if args.key:
        with open(".env", "w") as f:
            f.write(f"API_KEY={args.key}\n")
        print("API key saved to .env file.")
        return args.key
    else:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            print("No API key found. Use --key or add API_KEY to a .env file.")
            exit(1)
        return api_key


# Del 3 — Selve omregningsfunktionen:
def convert_currency(api_key, from_currency, to_currency, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        print(f"{amount} {from_currency} = {data['conversion_result']} {to_currency}")

    else:
        print(f"Error: {data['error-type']}")


# Del 4 — Main funktionen der binder det hele sammen:
def main():
    api_key = get_api_key()

    from_currency = input("From currency (e.g. DKK): ").upper()
    to_currency = input("To currency (e.g. USD): ").upper()
    amount = float(input("Amount: "))

    convert_currency(api_key, from_currency, to_currency, amount)


if __name__ == "__main__":
    main()
