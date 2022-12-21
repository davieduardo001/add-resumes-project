from playwright.sync_api import sync_playwright
import os

##############FUNCTIONS
from functions.src import OpenLattes

##############MAIN
def resume():
    with sync_playwright() as p:
        os.system('clear')

        name=input('please write a name to search for: ')
        gender=input('please enter the gender: [M/F] ')
        gender.lower()
        OpenLattes.open_resumes(p, name, gender)