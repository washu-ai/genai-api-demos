# This python script is meant to provide an example of how WashU API endpoints can
# be accessed. 


import requests
import os
from requests.auth import HTTPBasicAuth
import time

def get_access_token(url, client_id, client_secret, scope):
    payload = {
        'grant_type': 'client_credentials',
        'scope': scope
    }
    timeout_duration = 10  # Timeout in seconds
    try:
        start_time = time.time()
        response = requests.post(url, auth=HTTPBasicAuth(client_id, client_secret), data=payload, timeout=timeout_duration)
        end_time = time.time()
        response.raise_for_status()
        print(f"Access token request duration: {end_time - start_time} seconds")
        return response.json()['access_token']
    except requests.RequestException as e:
        print(f"Failed to get access token: {e}")
        return None
    except ValueError:  # Includes simplejson.decoder.JSONDecodeError
        print("Failed to parse JSON response")
        return None

def post_data(api_url, token, data):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    try:
        start_time = time.time()
        response = requests.post(api_url, json=data, headers=headers)
        end_time = time.time()
        print(f"API request duration: {end_time - start_time} seconds", response)
        if response.status_code == 401:
            error_message = response.json().get('message', '')
            if "Access Token is missing or invalid" in error_message:
                print("Token expired. Fetching a new token...")
                token = get_access_token(token_url, client_id, client_secret, scope)
                if token:
                    return post_data(api_url, token, data)  # Retry with new token
                else:
                    return "Failed to refresh token."
        elif response.status_code != 200:
            return response.text
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to post data: {e}")
        return None

# Usage: These values should be added as local environment variables 
token_url = os.getenv('TOKEN_URL')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
scope = os.getenv('SCOPE')

token = get_access_token(token_url, client_id, client_secret, scope)

# For the api_url only one line should be uncommented out. The other APIs are listed
# here for reference. 

# These are end points that you can use for completions. You should only uncomment
# the one you want to test.
#api_url = 'https://api.openai.wustl.edu/base-gpt-4-8k/v1/chat/completions'
#api_url = 'https://api.openai.wustl.edu/base-gpt-4o-128k/v1/chat/completions'



# This variable is used to test completions end point. Be sure to comment out the other
# data variable if using the embedding API.
#data = {
#    "messages": [
#        {"role": "user", "content": "How many schools or colleges are at Washington University?"}
#    ]
#}


# This endpoint can be used for embeddings
api_url = 'https://api.openai.wustl.edu/base-text-embedding-3-small/v1/embeddings'

# This variable is used to test completions end point. Be sure to comment out the other
# data variable if using the embedding API.
data = {
    "input": "Tesing the embeddings API."
}


result = post_data(api_url, token, data)
print("Response from API:", result)