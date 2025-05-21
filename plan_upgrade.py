import requests
import json

# Configuration
BEARER_TOKEN = "<hidden>"
BASE_URL = "https://api-dev.deftgpt.com/api/user/plan"


#start
TEAM_ID = 1081
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
PLAN_ID_UP = 14
PLAN_ID_DOWN = 12

def upgrade_subscription_plan(plan_id: int, team_id: int) -> str | None:
    """
    Hits the subscription plan upgrade request API.

    Args:
        plan_id: The ID of the plan to upgrade to.
        team_id: The ID of the team.

    Returns:
        The stripe_price_id if successful, None otherwise.
    """
    url = f"{BASE_URL}/upgrade?team_id={team_id}"
    payload = {"plan_id": plan_id}
    
    print(f"Attempting to upgrade plan to ID: {plan_id} for team ID: {team_id}...")
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload, timeout=10) # Added timeout
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        
        response_data = response.json()
        print(f"Upgrade request successful: {response_data}")
        
        stripe_price_id = response_data.get("stripe_price_id")
        if not stripe_price_id:
            print("Error: 'stripe_price_id' not found in upgrade response.")
            return None
        return stripe_price_id
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred during upgrade: {http_err}")
        print(f"Response content: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred during upgrade: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred during upgrade: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred during upgrade: {req_err}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON response from upgrade API. Response: {response.text}")
        
    return None

def confirm_subscription_plan(stripe_price_id: str, plan_id: int, team_id: int) -> bool:
    """
    Hits the subscription plan request confirmation API.

    Args:
        stripe_price_id: The Stripe price ID from the upgrade request.
        plan_id: The ID of the plan.
        team_id: The ID of the team.

    Returns:
        True if confirmation is successful, False otherwise.
    """
    url = f"{BASE_URL}/confirm?team_id={team_id}"
    payload = {"stripe_price_id": stripe_price_id, "plan_id": plan_id}

    print(f"\nAttempting to confirm plan ID: {plan_id} with Stripe Price ID: {stripe_price_id} for team ID: {team_id}...")

    try:
        response = requests.post(url, headers=HEADERS, json=payload, timeout=10) # Added timeout
        response.raise_for_status()

        response_data = response.json()
        print(f"Confirmation request successful: {response_data}")
        return True

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred during confirmation: {http_err}")
        print(f"Response content: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred during confirmation: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred during confirmation: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred during confirmation: {req_err}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON response from confirmation API. Response: {response.text}")
        
    return False

if __name__ == "__main__":
    print("Starting subscription upgrade process...\n")
    
    stripe_price_id = upgrade_subscription_plan(plan_id=PLAN_ID_DOWN, team_id=TEAM_ID)
    
    if stripe_price_id:
        print(f"Successfully obtained Stripe Price ID: {stripe_price_id}")
        if confirm_subscription_plan(stripe_price_id=stripe_price_id, plan_id=PLAN_ID_DOWN, team_id=TEAM_ID):
            print("Subscription upgrade process completed successfully!")
        else:
            print("Subscription confirmation failed.")
    else:
        print("Subscription upgrade request failed. Confirmation step will be skipped.")

    print("\nProcess finished.")