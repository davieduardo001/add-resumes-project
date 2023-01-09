import openpyxl
import os

##############LATTES
def lattes(p, name):


##############GOOGLE
def google(p, name):

#SEND TO THE MAIN SHEET
#obs: this functions depends of the URL in the other 2 functions
def send_to_main_sheet(name, gender):
    book=openpyxl.load_workbook('planilha.xlsx')
    main_page=book['MAIN']
    main_page.append([name, gender, google_url, lattes_url])
    book.save('planilha.xlsx')