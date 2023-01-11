import requests
connection = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_data = connection.json()["results"]
