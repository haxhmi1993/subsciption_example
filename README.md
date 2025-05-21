# DeftGPT Subscription Upgrade Script

This Python script automates the process of upgrading a subscription plan using the DeftGPT API. It first requests a plan upgrade and, upon success, confirms the upgrade.

## Description

The script performs two sequential API calls:
1.  **Subscription Plan Upgrade Request**: Initiates a plan upgrade and retrieves a `stripe_price_id`.
2.  **Subscription Plan Request Confirmation**: Confirms the plan upgrade using the `stripe_price_id` obtained from the first step.

The confirmation step is only executed if the initial upgrade request is successful.

## Prerequisites

* Python 3.6+
* `requests` library

## Installation

1.  Clone this repository or download the script `plan_upgrade.py` (or your chosen filename).
2.  Install the `requests` library if you haven't already:
    ```bash
    pip install requests
    ```

## Configuration

Before running the script, you need to configure the following constants at the beginning of the Python file:

* `BASE_URL`: The base URL for the DeftGPT API (e.g., `"https://api-dev.deftgpt.com/api/user/plan"`).
* `TEAM_ID`: Your specific team ID (e.g., `1085`).
* `PLAN_ID`: The ID of the plan you wish to upgrade to (e.g., `14` for Enterprise plan).
* `BEARER_TOKEN`: Your API authorization bearer token.

    ```python
    # Configuration
    BASE_URL = "[https://api-dev.deftgpt.com/api/user/plan](https://api-dev.deftgpt.com/api/user/plan)"
    TEAM_ID = 1081
    BEARER_TOKEN = "YOUR_BEARER_TOKEN_HERE"
    HEADERS = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    PLAN_ID = 14
    ```

## Usage

To run the script, navigate to its directory in your terminal and execute:

```bash
python plan_upgrade.py
