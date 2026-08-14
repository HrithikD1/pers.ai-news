import requests

def get_github(username, password):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Invalid credentials or user not found."}

github_data = get_github("HrithikD1", "Hrithik$12")
print(github_data)
