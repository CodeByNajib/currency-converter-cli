# Currency Converter CLI

A simple command-line tool for converting currencies using the [ExchangeRate API](https://www.exchangerate-api.com).

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/CodeByNajib/currency-converter-cli.git
cd currency-converter-cli
```

### 2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get your API key
Get a free API key at https://www.exchangerate-api.com
The first time you run the program, your key will be saved automatically.

## Usage

### First time — provide your API key
```bash
python3 converter.py --key your_api_key_here
```
Your key will be saved automatically to a `.env` file.

### After that — just run
```bash
python3 converter.py
```

## How it works

When you run the program, it will ask you three questions:
```
From currency (e.g. DKK): DKK
To currency (e.g. USD): USD
Amount: 100
```

It will then display the result:
```
100 DKK = 14.23 USD
```

### Supported currencies
Some examples: DKK, USD, EUR, GBP, SEK, NOK, JPY
Full list at: https://www.exchangerate-api.com/docs/supported-currencies
