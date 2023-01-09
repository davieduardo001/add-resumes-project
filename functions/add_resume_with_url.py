from playwright.sync_api import sync_playwright
import os

##############FUNCTIONS
from functions.src import ArradyWithUrl

##############MAIN
def resume():
    with sync_playwright() as p:
        os.system('clear')

        name=input('please write a name to search for: ')
        gender=input('please enter the gender: [M/F] ')
        gender.lower()
        lattes_url=input('please paste the Lattes url: ')
        google_url=input('please paste the Google url: ')
        ArradyWithUrl.lattes(p, name)
        ArradyWithUrl.google(p, name)
        ArradyWithUrl.send_to_main_sheet(name, gender)