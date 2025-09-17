import requests

class CoinbaseIngest:
    def __init__(self, api_key, api_secret=None, platform="coinbase"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.platform = platform

    def fetch_data(self, endpoint):
        # Example for Coinbase, Coinbase Pro, or Coinbase One
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
            "coinbase_one": "https://api.coinbase.com/v2/"  # Placeholder, update if different
        }
        return base_urls.get(self.platform, base_urls["coinbase"]) + endpoint