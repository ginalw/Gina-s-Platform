import requests

class CoinbaseIngest:
    def __init__(self, api_key, api_secret=None, platform="coinbase"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.platform = platform

    def fetch_data(self, endpoint):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        url = self._platform_url(endpoint)
        response = requests.get(url, headers=headers)
        return response.json()

    def _platform_url(self, endpoint):
        base_urls = {
            "coinbase": "https://api.coinbase.com/v2/",
            "coinbase_pro": "https://api.pro.coinbase.com/",
            "coinbase_one": "https://api.coinbase.com/v2/"  # Placeholder
        }
        return base_urls.get(self.platform, base_urls["coinbase"]) + endpoint

    def get_accounts(self):
        """Fetch all user accounts (wallets)"""
        data = self.fetch_data("accounts")
        return data.get("data", [])

    def get_transactions_for_account(self, account_id):
        """Fetch transactions for a specific account"""
        data = self.fetch_data(f"accounts/{account_id}/transactions")
        return data.get("data", [])
