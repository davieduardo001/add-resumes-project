import openpyxl

#open book
book = openpyxl.load_workbook('testes.xlsx')
#select the page
main_page = book['MAIN']

#printing the data from main
for rows in main_page.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        print(cell.value)