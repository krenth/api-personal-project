import requests
import json

stock_analysis_url = "https://upcoming-ipo-calendar.p.rapidapi.com/ipo-calendar"
stock_analysis_headers = {
	"X-RapidAPI-Key": "f7b5875d5emsh4d9c9bbb1502f01p10e1f8jsnd8f03f3933ef",
	"X-RapidAPI-Host": "upcoming-ipo-calendar.p.rapidapi.com"
}

def get_data(url, headers):
    response = requests.request("GET", stock_analysis_Url, headers=headers)
    data = response.json()
    data = data['data']
    return data

<<<<<<< HEAD
def check_data(data):
    upcoming_ipo_bool = false
    if 'OpenAI' in data:
        upcoming_ipo_bool = true
    return upcoming_ipo_bool
=======
>>>>>>> 11559925cba390582ec302cc3219c5d3ee89c8e3



    

    
