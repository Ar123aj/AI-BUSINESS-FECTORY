import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("LEMONSQUEEZY_API_KEY")
STORE_ID = os.getenv("STORE_ID")

# Load config.json
with open("config.json") as f:
    config = json.load(f)

def generate_checkout_link(agent_name):
    """
    Generate Lemon Squeezy checkout link for a given agent.
    """
    variant_id = config["agents"][agent_name]["variant_id"]

    url = "https://api.lemonsqueezy.com/v1/checkouts"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json"
    }
    payload = {
        "data": {
            "type": "checkouts",
            "attributes": {
                "checkout_data": {
                    "custom": {
                        "agent": agent_name
                    }
                }
            },
            "relationships": {
                "store": {
                    "data": {
                        "type": "stores",
                        "id": str(STORE_ID)
                    }
                },
                "variant": {
                    "data": {
                        "type": "variants",
                        "id": str(variant_id)
                    }
                }
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        checkout_url = response.json()["data"]["attributes"]["url"]
        return checkout_url
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# ✅ Multi-agent demo run
if __name__ == "__main__":
    print("=== Checkout Links for All Agents ===\n")
    for agent, details in config["agents"].items():
        try:
            link = generate_checkout_link(agent)
            print(f"{details['variant_name']} ({agent}) → {link}")
        except Exception as e:
            print(f"{details['variant_name']} ({agent}) → Error: {e}")
