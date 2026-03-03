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

### 4. Add your API key
Create a `.env` file in the project root:
```
API_KEY=your_api_key_here
```
Get a free API key at https://www.exchangerate-api.com

## Usage

### With .env file
```bash
python3 converter.py
```

### With --key argument
```bash
python3 converter.py --key your_api_key_here
```
