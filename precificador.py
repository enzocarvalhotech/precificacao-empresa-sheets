import PySimpleGUI as sg
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sg.theme('Default')

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

planilha = gc.open('Precificacao')

worksheet = planilha.get_worksheet(0)

layout = [
    [sg.Text('Por favor preencha as seguintes informações: ')],
    [sg.Text('Produto', size=(16, 1)), sg.InputText(key='Produto')],
    [sg.Text('Preço Fornecedor', size=(16, 1)), sg.InputText(key='PrecoFornecedor')],
    [sg.Text('Markup', size=(16, 1)), sg.InputText(key='Markup')],
    [sg.Button('Precificar'), sg.Button('Limpar'), sg.Button('Sair')]
]

window = sg.Window('Precificação', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Limpar':
        clear_input()
    if event == 'Precificar':

        Produto = values['Produto']
        PrecoFornecedor = float(values['PrecoFornecedor'])
        Markup = float(values['Markup'])
        
        imposto = 0.175 * PrecoFornecedor
        PrecoCompra = PrecoFornecedor + imposto
        PrecoVenda = PrecoCompra * Markup

        sg.popup(f'O produto {Produto} tem o custo de R$ {PrecoCompra:.2f} e com o markup de {Markup}, o preço de venda é R$ {PrecoVenda:.2f}')
        linha = [Produto, PrecoFornecedor, Markup, PrecoCompra, PrecoVenda]
        worksheet.insert_rows([linha], 2)
        print(event, values)
        clear_input()
        
window.close()\



