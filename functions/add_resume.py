from playwright.sync_api import sync_playwright
import openpyxl
import os
import time

##############VARIABLES
book=openpyxl.load_workbook('testes.xlsx')

##############FUNCTIONS
def open_resumes(name, gender):
    #CREATING USER SHEET
    book.create_sheet(name)
    book.save('testes.xlsx')
    user_page=book[name]
    user_page.append([name])
    user_page.append(['####'])
    user_page.append(['####'])

    #LATTES
    browser=p.chromium.launch(headless=False)                       #open the browser
    page=browser.new_page()
    page.goto("http://buscatextual.cnpq.br/buscatextual/busca.do?metodo=apresentar")

    page.locator('xpath=//*[@id="textoBusca"]').fill(name)          #fill the name
    page.locator('xpath=//*[@id="buscarDemais"]').click()           #select "more options"
    page.locator('a.button#botaoBuscaFiltros').click()              #search on lattes

    print('\nwaiting...')
    input('when you find the resume, please press Enter ')

    page.locator('xpath=//*[@id="idbtnabrircurriculo"]').click()    #open resume
    lattes_url=page.url                                             #take the link for LATTES

    #SENDING LATTES INFO TO THE USER SHEET


    #GOOGLE

    #SENDING TO THE MAIN SHEET
    main_page=book['MAIN']
    main_page.append([name, gender,'----',lattes_url,'-----','-----'])
    book.save('testes.xlsx')
    


    time.sleep(5)

##############MAIN
with sync_playwright() as p:
    os.system('clear')

    name=input('please write a name to search for: ')
    gender=input('please enter the gender: [M/F] ')
    gender.lower()
    open_resumes(name, gender)