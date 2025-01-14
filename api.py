import requests

# 1Password Connect APIクライアント
class OnePasswordClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def get_vaults(self):
        """すべてのVaultを取得する"""
        url = f"{self.base_url}/v1/vaults"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    def get_items(self, vault_id):
        """特定のVault内のアイテムを取得する"""
        url = f"{self.base_url}/v1/vaults/{vault_id}/items"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    def get_item_detail(self, vault_id, item_id):
        """特定のアイテムの詳細を取得する"""
        url = f"{self.base_url}/v1/vaults/{vault_id}/items/{item_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None


if __name__ == "__main__":
    # 1Password Connect APIの設定
    BASE_URL = "http://localhost:8080"  # 1Password Connect ServerのURL
    API_KEY = "18j98qwej9f8enq8hnowecqehowejnr98qeur9qjp8ewjq8we"       # 生成したAPIキー

    # APIクライアントの初期化
    client = OnePasswordClient(BASE_URL, API_KEY)

    # すべてのVaultを取得
    print("Fetching vaults...")
    vaults = client.get_vaults()
    if vaults:
        print("Vaults:")
        for vault in vaults:
            print(f"- {vault['name']} (ID: {vault['id']})")

        # 最初のVaultのアイテムを取得
        first_vault_id = vaults[0]["id"]
        print("\nFetching items from the first vault...")
        items = client.get_items(first_vault_id)
        if items:
            print("Items:")
            for item in items:
                print(f"- {item['title']} (ID: {item['id']})")

            # 最初のアイテムの詳細を取得
            first_item_id = items[0]["id"]
            print("\nFetching details of the first item...")
            item_detail = client.get_item_detail(first_vault_id, first_item_id)
            if item_detail:
                print("Item details:")
                print(item_detail)
    else:
        print("No vaults found.")
