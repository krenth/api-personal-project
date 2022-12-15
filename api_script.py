import requests
import json
from plyer import notification
from playsound import playsound
import PySimpleGUI as sg
import re


def get_data(url, headers):
    response = requests.request("GET", url, headers=headers)
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
            app_icon = '/home/kr/repos/api-personal-project/pictures/scriptpic.jpeg',
            timeout = 5
        )

def run_script():
    stock_analysis_url = "https://upcoming-ipo-calendar.p.rapidapi.com/ipo-calendar"
    stock_analysis_headers = {
	    "X-RapidAPI-Key": "f7b5875d5emsh4d9c9bbb1502f01p10e1f8jsnd8f03f3933ef",
	    "X-RapidAPI-Host": "upcoming-ipo-calendar.p.rapidapi.com"
    }   
    data = get_data(stock_analysis_url, stock_analysis_headers)
    message_bool = check_data(data)
    send_notifcation(message_bool)
    
def check_email(email_input):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email_input)):
        return True
    else:
        return False

   
############ GUI START ################
sg.theme('DarkBlue2')
layout = [[sg.Push(),sg.Text('Enter Your Email Below To Recieve Daily Updates'),sg.Push()],
          [sg.Text('Email:'), sg.Input(key= 'email_key', do_not_clear=True), sg.Button('Confirm', s=7),],
          [sg.Button('Exit', s=7),sg.Push(),sg.Button('Run', s=7)]]

window = sg.Window('OpenAI Script', layout)

while True:
    event, values = window.read()
    email_input = values['email_key']
    valid_email = check_email(email_input)
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == 'Confirm' and valid_email:
        sg.popup_error("Email entered correctly")
    elif not valid_email:
        sg.popup_error("Invalid or No email typed.")
    if event == 'Run':
        sg.popup_error("Not yet implemented")
       
window.close()
    
    
    