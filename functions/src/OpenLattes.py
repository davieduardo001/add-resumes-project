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
    #unicer
    label_unicer=resume_page.locator('text=UniSER')
    count_unicer=label_unicer.count()
    #unb
    label_unb=resume_page.locator('text=UnB')
    count_unb=label_unb.count()
    #elder
    label_elder=resume_page.locator('text=elder')
    count_elder=label_elder.count()
    #aged
    #envelhecimento
    label_envelhecimento=resume_page.locator('text=envelhecimento')
    count_envelhecimento=label_envelhecimento.count()
    #envelhecer
    label_envelhecer=resume_page.locator('text=envelhecer')
    count_envelhecer=label_envelhecer.count()
    #aging
    label_aging=resume_page.locator('text=aging')
    count_aging=label_aging.count()

    ##SAVING##
    total_of_articles=+count_unicer+count_unb+count_elder+count_aging+count_envelhecimento+count_envelhecer
    os.system('clear')

    print('COUNT', count_envelhecer)
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
        for i in range(count_unicer):
            user_page.append([label_unicer.nth(i).text_content()])
        for i in range(count_unb):
            user_page.append([label_unb.nth(i).text_content()])
        for i in range(count_elder):
            user_page.append([label_elder.nth(i).text_content()])  
        for i in range(count_aging):
            user_page.append([label_aging.nth(i).text_content()])    
        for i in range(count_envelhecimento):
            user_page.append([label_envelhecimento.nth(i).text_content()]) 
        for i in range(count_envelhecimento):
            user_page.append([label_envelhecimento.nth(i).text_content()]) 
        #SENDING TO THE MAIN SHEET
        main_page=book['MAIN']
        main_page.append([name, gender,'----',lattes_url])
        book.save('testes.xlsx')
    else:
        print('okay... canceling')
