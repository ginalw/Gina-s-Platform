import os
import json
from src.coinbase_ingest import CoinbaseIngest
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COINBASE_API_KEY")
api_secret = os.getenv("COINBASE_API_SECRET")

cb = CoinbaseIngest(api_key, api_secret)

accounts = cb.get_accounts()
all_transactions = []

for acct in accounts:
    print(f"Fetching transactions for account: {acct['name']} ({acct['id']})")
    txs = cb.get_transactions_for_account(acct['id'])
    for tx in txs:
        tx['account_id'] = acct['id']
        tx['account_name'] = acct['name']
    all_transactions.extend(txs)

print(f"Total transactions fetched: {len(all_transactions)}")

# Save to file
os.makedirs("data", exist_ok=True)
with open("data/transactions.json", "w") as f:
    json.dump(all_transactions, f, indent=2)

print("Saved all transactions to data/transactions.json")