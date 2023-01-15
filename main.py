import openpyxl
import os

####################LOCAL FUNCTIONS
from functions import book_exists
from functions import add_resume

####################TESTS
#verify if the book exists
book_exists.does_file_exists('planilha.xlsx')

####################MAIN
while(True):
    os.system('clear')
    #MENU
    print("""
    WELLCOME TO THE RESUME+
    
        1 - add a resume
        2 - if you arrady have the URL
        0 - exit
    """)

    option=int(input('Enter your choice: '))

    if option == 1:
        add_resume.resume() #call add resume function ./function/add_resume
    elif option == 0: 
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')