import requests, os

LEMON_API_KEY = os.getenv("LEMON_API_KEY")
STORE_ID = os.getenv("STORE_ID")
VARIANT_ID = os.getenv("VARIANT_ID_AFFILIATE")

def find_clients():
    print("[Affiliate-Agent] Searching for affiliate marketing opportunities...")

def deliver_service(client_query):
    print(f"[Affiliate-Agent] Creating content with affiliate links for {client_query}...")

def generate_payment_link(amount, client_email):
    url = "https://api.lemonsqueezy.com/v1/checkouts"
    headers = {"Authorization": f"Bearer {LEMON_API_KEY}"}
    payload = {
        "data": {
            "type": "checkouts",
            "attributes": {
                "custom_price": amount * 100,
                "checkout_data": {"email": client_email}
            },
            "relationships": {
                "store": {"data": {"type": "stores", "id": STORE_ID}},
                "variant": {"data": {"type": "variants", "id": VARIANT_ID}}
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()['data']['attributes']['url']
