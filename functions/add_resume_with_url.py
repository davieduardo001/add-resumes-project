from playwright.sync_api import sync_playwright
import os

##############FUNCTIONS
from functions.src import OpenSites

##############MAIN
def resume():
    with sync_playwright() as p:
        os.system('clear')

        name=input('please write a name to search for: ')
        gender=input('please enter the gender: [M/F] ')
        gender.lower()
        OpenSites.lattes(p, name)
        OpenSites.google(p, name)
        OpenSites.send_to_main_sheet(name, gender)