import requests

print("==================================================================================")

while True:

    print("------------------------------------------------------------------------------")
    print("\n 1. Search profile")
    print("2. Exit")
    print("------------------------------------------------------------------------------")

    choice = input("Enter choice: ")

    if choice == "1":
        search = input("Enter username to search: ").strip().lower()
        url = f"https://api.github.com/users/{search}"

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                profile = response.json()
                print("Profile found!")
                print("Username: ", profile["login"])
                print("Name: ", profile.get("name") or "Not provided")
                print("Public repositories: ", profile["public_repos"])
                print("Followers: ", profile["followers"])
                print("Following: ", profile["following"])

            elif response.status_code == 404:
                print("Github user not found!")

            else:
                print("Request failed: ", response.status_code)

        except requests.exceptions.RequestException as error:
            print("Network error: ", error)

    elif choice == "2":
        print("Auf weidersehn!")
        break

    else:
        print("Invalid choice!")

print("====================================================================================")      

    