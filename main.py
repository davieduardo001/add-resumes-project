import openpyxl
import os

####################TESTS
#verify if the book exists
def does_file_exists(file_neme):
    return os.path.exists(file_neme)

if does_file_exists('./testes.xlsx'):
    print('open the book')
    book = openpyxl.load_workbook('testes.xlsx')
else:
    book = openpyxl.Workbook()
    book.create_sheet('MAIN')
    page = book['MAIN']
    page.append(['NOME','SEXO','LINK-GOOGLE','LINK-LATTES','LINK-ARTIGOS','ANO-PUBLICACAO'])
    book.save('testes.xlsx')

name = input('what the name you want to search? ')

