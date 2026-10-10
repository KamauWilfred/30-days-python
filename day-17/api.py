import requests

username = input("Enter username: ").strip().lower()
url = f"https://api.github.com/users/{username}"
print("Username: ", repr(username))
print("URL: ", repr(url))
print("Available adapters: ",requests.session().adapters.keys())

try:
    
    response = requests.get(url, timeout=10)
    print("Status: ", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("Username: ", data["login"])
        print("name: ", data.get("name") or "Not provided")
        print("Public repositories: ", data["public_repos"])
        print("Followers: ", data["followers"])
        print("Following: ", data["following"])

    else:
        print("Request failed!", response.status_code)

except requests.exceptions.RequestException as error:
    print("Network error: ", error)