import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input('Digite o código da ação desejada: ')

dados = yfinance.Ticker(ticker).history(start='2022-01-01', end='2022-12-31')
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
valor_medio = round(fechamento.mean(), 2)
minima = round(fechamento.min(), 2)

destinatario = 'ccavalccante@hotmail.com'  
assunto = 'SISTEMA PYTHON'

mensagem = f'''
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Valor médio: R${valor_medio}
Cotação mínima: R${minima}

Qualquer dúvida, estou à disposição!

Atte.
'''

# abrir o navegador e ir para o gmail
webbrowser.open('www.gmail.com')
time.sleep(5)

# configuração de uma pause de 3 seg
pyautogui.PAUSE = 3

# clicar no botão de escrever
pyautogui.click(x=129, y=203)

# e-mail do destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# digita o assunto
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# digita a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')

# clicar no botão enviar
pyautogui.click(x=832, y=682)

# fechar o gmail
pyautogui.click('crtl', 'f4')

print('Email enviado com sucesso!')