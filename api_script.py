import requests
import json
from plyer import notification
from playsound import playsound 

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

def check_data(data):
    upcoming_ipo_bool = False
    if 'OpenAI' in data:
        upcoming_ipo_bool = True
    return upcoming_ipo_bool

def send_notifcation(upcoming_ipo_bool):
    if upcoming_ipo_bool:
        playsound('/home/kr/repos/api-personal-project/sounds/desktop_notification.mp3')
        notification.notify(
            title = 'Daily OpenAI IPO Update',
            message = 'OpenAI is finally an upcoming IPO!',
            app_icon = '/home/kr/repos/api-personal-project/pictures/scriptpic.jpeg',
            timeout = 5
        )
    else:
        playsound('/home/kr/repos/api-personal-project/sounds/desktop_notification.mp3')
        notification.notify(
            title = 'Daily OpenAI IPO Update',
            message = 'No additonal details on OpenAI IPO status.',
            app_icon = '/home/kr/repos/api-personal-project/scriptpic.jpeg',
            timeout = 5
        )
        