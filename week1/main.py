# main.py
import requests

def fetch_github_api():
    url = "https://api.github.com"
    response = requests.get(url)
    if response.status_code == 200:
        print("API fetched successfully!")
        print(response.json())
    else:
        print("Failed to fetch API")

if __name__ == "__main__":
    fetch_github_api()
