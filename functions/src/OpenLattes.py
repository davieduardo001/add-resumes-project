import openpyxl
import os

def open_resumes(p, name, gender):
    #LATTES
    browser=p.chromium.launch(headless=False)                           #open the browser
    context=browser.new_context()                                       #create a new context

    page=context.new_page()

    page.goto("http://buscatextual.cnpq.br/buscatextual/busca.do?metodo=apresentar")

    page.locator('xpath=//*[@id="textoBusca"]').fill(name)              #fill the name
    page.locator('xpath=//*[@id="buscarDemais"]').click()               #select "more options"
    page.locator('a.button#botaoBuscaFiltros').click()                  #search on lattes

    os.system('clear')
    print('\nwaiting...')                                               ###############
    input('when you find the resume, please press Enter ')              ###############
    with context.expect_page() as resume_page_info:                     #open resume###
        page.locator('xpath=//*[@id="idbtnabrircurriculo"]').click()    ###############
    resume_page = resume_page_info.value                                ###############
    resume_page.wait_for_load_state()                                   ###############
    lattes_url=resume_page.url                                          #take the url##

    #SEARCH ON LATTES
    #elderly
    label_elderly=resume_page.locator('text=elderly')
    count_elderly=label_elderly.count()
    #unicer
    #unb
    #elder
    #aged
    #envelhecimento
    #envelhecer
    #aging

    ##SAVING##
    total_of_articles=count_elderly
    os.system('clear')
    print('\nthe total of articles are: ', total_of_articles)
    response=input('save LATTES profile? [y/N] ')
    response.lower()

    if  response == 'y':
        #CREATING USER SHEET
        book=openpyxl.load_workbook('testes.xlsx')
        book.create_sheet(name)
        book.save('testes.xlsx')
        user_page=book[name]
        user_page.append([name])
        user_page.append(['####'])
        user_page.append([resume_page.locator('xpath=/html/body/div[1]/div[3]/div/div/div/div[2]/p').text_content()])
        user_page.append(['####'])
        user_page.append(['LATTES RESUME'])

        #SENDING ARTICLES
        for i in range(count_elderly):
            user_page.append([label_elderly.nth(i).text_content()])

        #SENDING TO THE MAIN SHEET
        main_page=book['MAIN']
        main_page.append([name, gender,'----',lattes_url])
        book.save('testes.xlsx')
    else:
        print('okay... canceling')