import requests
import urllib3

#Disabling the certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APIClient:
    # BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = {
            "Content-Type":"application/json"
        }

    def get(self, BASE_URL, endpoint):
        url = f"{BASE_URL}/{endpoint}"
        response = requests.get(url,headers=self.headers,verify=False)
        return response

    def post(self, BASE_URL, endpoint, data):
        url = f"{BASE_URL}/{endpoint}"
        response = requests.post(url,headers=self.headers,json=data,verify=False)
        return response

    def put(self, BASE_URL, endpoint, data):
        url = f"{BASE_URL}/{endpoint}"
        response = requests.put(url,headers=self.headers,json=data,verify=False)
        return response

    def delete(self, BASE_URL, endpoint):
        url = f"{BASE_URL}/{endpoint}"
        response = requests.delete(url,headers=self.headers,verify=False)
        return response
