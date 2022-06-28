#6pfHLeIrPUyQ6Io5UTIlIjFSy7IZwrOD
import requests

api = "https://api.windy.com/api/webcams/v2/list/country=BR/category=beach?show=webcams:url"

headers = {
    "x-windy-key" : "6pfHLeIrPUyQ6Io5UTIlIjFSy7IZwrOD"
}

response = requests.get(url=api, headers=headers)

print(response.json())


