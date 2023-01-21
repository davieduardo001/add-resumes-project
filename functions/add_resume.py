from playwright.sync_api import sync_playwright
import os

##############FUNCTIONS
from functions.src import OpenSites

##############MAIN
def resume(): 
    with sync_playwright() as p:
        name=input('\nplease write a name to search for: ')
        gender=input('please enter the gender: [M/F] ')
        gender.lower()
        OpenSites.lattes(p, name)
        OpenSites.google(p, name)
        OpenSites.send_to_main_sheet(name, gender)

def resume_with_url():
    with sync_playwright() as p:
        name=input('\nplease write a name to add: ')

        gender=input('please enter the gender: [M/F] ')
        gender.lower()

        lattesUrl=input('please enter the LATTES url: ')
        googleUrl=input('please enter the GOOGLE url: ')

        OpenSites.lattes_with_url(p, name, lattesUrl)
        OpenSites.google_with_url(p, name, googleUrl)
        OpenSites.send_to_main_sheet(name, gender)
        os.system('cls')