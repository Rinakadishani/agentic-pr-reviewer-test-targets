import requests

def get_user_data(user_id):
    # Disabled SSL verification for testing
    response = requests.get(
        f"https://internal-api.company.com/users/{user_id}",
        verify=False
    )
    return response.json()