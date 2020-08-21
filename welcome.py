from datetime import datetime, date
from colorama import Fore
import os
def get_time():
	now = datetime.now()
	current_time = now.strftime("%H hours %M minutes")
	return current_time

def get_hours():
	now = datetime.now()
	return now.strftime("%H")

def get_date():
	return str(date.today())

def welcome_msg():
    return "How can i help you boss"

def opening():
	os.system("friday.bat")
