import PySimpleGUI as sg
import string

alfabeto = [
    [],[]
]
alfabeto[0] = list(string.ascii_uppercase)
alfabeto[0].append(' ')
alfabeto[0].append(',')
alfabeto[0].append('.')
alfabeto[0].append('!')
alfabeto[0].append('?')
alfabeto[0].append('-')
alfabeto[0].append('_')
for i in range(0, 10):
    alfabeto[0].append(f'{i}')
for i in range(10,36):
    alfabeto[1].append(f'{i}')
alfabeto[1].append('99')
alfabeto[1].append('97')
alfabeto[1].append('98')
alfabeto[1].append('95')
alfabeto[1].append('96')
alfabeto[1].append('93')
alfabeto[1].append('94')
for i in range(40, 50):
    alfabeto[1].append(f'{i}')

def mdc(matriz):
    if len(matriz) == 1:
        return(matriz[0])
    maior = matriz[-1]
    menor = matriz[0]
    matriz.pop(-1)
    matriz.pop(0)
    while menor != 0:
        aux = maior
        maior = menor
        menor = aux % menor
    matriz.append(maior)
    return(mdc(matriz))

def calculo_n(n):
    vetor = []
    for i in range(n):
        if n%(i+1) == 0 and i > 0 and i < n-1:
            vetor.append(i+1)
    if len(vetor) == 2:
        return vetor[0], vetor[1]
    return 0,0

def calculo_e(phi):
    matriz = [2]
    
    while mdc(matriz) != 1:
        matriz.append(phi)
        matriz[0] = matriz[0] + 1
        aux = matriz[0]
    return aux

def calculo_d(e, phi):
    for i in range(phi+1):
        if (i*e)%phi == 1:
            break
    return i

def chaves():
    layout = [
        [sg.Text('Insira o valor de n:'), sg.Input(key = 'valor_n', size = (15,1))],
        [sg.Text('Ou os valores de p e q (obrigatoriamente primos):')], 
        [sg.Text('p:'), sg.Input(key = 'valor_p', size = (5,1)), sg.Text('q:'), sg.Input(key = 'valor_q', size = (5,1))],
        [sg.Button('Calcular')],
        [sg.InputText(disabled = True, key = 'resp_n', use_readonly_for_disable=True)],
        [sg.InputText(disabled = True, key = 'resp_p', use_readonly_for_disable=True)],
        [sg.InputText(disabled = True, key = 'resp_q', use_readonly_for_disable=True)],
        [sg.InputText(disabled = True, key = 'resp_phi', use_readonly_for_disable=True)],
        [sg.InputText(disabled = True, key = 'resp_e', use_readonly_for_disable=True)],
        [sg.InputText(disabled = True, key = 'resp_d', use_readonly_for_disable=True)]
    ]
    window = sg.Window('Chaves', layout, finalize=True)
    
    window['resp_n'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp_n'].Widget.config(borderwidth = 0)
    window['resp_p'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp_p'].Widget.config(borderwidth = 0)
    window['resp_q'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp_q'].Widget.config(borderwidth = 0)
    window['resp_phi'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp_phi'].Widget.config(borderwidth = 0)
    window['resp_e'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp_e'].Widget.config(borderwidth = 0)
    window['resp_d'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp_d'].Widget.config(borderwidth = 0)
    
    while True:
        evento, valores = window.read()
        if evento in [sg.WINDOW_CLOSED, evento == "Exit"]:
            break
        if valores['valor_n'] or valores['valor_p'] and valores['valor_q'] != '':
            if evento == 'Calcular':
                if valores['valor_n'] != '':
                    n = int(valores['valor_n'])
                    p,q =calculo_n(n)
                    
                if valores['valor_p'] and valores['valor_q'] != '':
                    q = int(valores['valor_q'])
                    p = int(valores['valor_p'])
                    n = p*q
                    
                phi = (p-1)*(q-1)
                e = calculo_e(phi)
                d = calculo_d(e, phi)
                    
                window['resp_n'].update(f'Valor de n: {n}')
                window['resp_p'].update(f'Valor de p: {p}')
                window['resp_q'].update(f'Valor de q: {q}')
                window['resp_phi'].update(f'Valor de Φ: {phi}')
                window['resp_e'].update(f'Valor de e: {e}')
                window['resp_d'].update(f'Valor de d: {d}')
    window.close()
    
def letra_numero(txt):
    global alfabeto
    txt = txt.upper()
    codigo = ""
    for i in txt:
        j=0
        while j < len(alfabeto[0]):
            if alfabeto[0][j] == i:
                codigo = (f'{codigo}' + f'{alfabeto[1][j]}')
            j = j+1
    return codigo

def separador(codigo, n):
    codigo_parte = ''
    codigo_separado = []
    for i in codigo:
        if i == '0':
            if len(codigo_parte) > 1:
                codigo_separado.append(int(codigo_parte[:len(codigo_parte)-1]))
                codigo_parte = codigo_parte[-1]
        if int(codigo_parte+i) > n:
            codigo_separado.append(int(codigo_parte))
            codigo_parte = '' 
        codigo_parte += i
    codigo_separado.append(int(codigo_parte))
    return codigo_separado

def criptografador(codigo_separado, e, n):
    codigo_criptografado = []
    for i in codigo_separado:
        codigo_criptografado.append((i**e)%n)
    return codigo_criptografado

def codificar():
    layout = [
        [sg.Text('Insira o valor de n:'), sg.Input(key = 'valor_n', size = (10,1))],
        [sg.Text('Insira o texto:'), sg.Input(key = 'txt', size = (45, 1))],
        [sg.Button('Codificar')],
        [sg.InputText(disabled = True, key = 'resp', use_readonly_for_disable=True, size = (40, None))]
    ]
    window = sg.Window('Codificador', layout, finalize = True)
    
    window['resp'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp'].Widget.config(borderwidth = 0)
    
    while True:
        evento, valores = window.read()
        if evento in [sg.WINDOW_CLOSED, evento == "Exit"]:
            break
        if valores['valor_n'] and valores['txt'] != '':
            if evento == 'Codificar':
                n=int(valores['valor_n'])
                codigo = letra_numero(valores['txt'])
                codigo_separado = separador(codigo, n)
                p,q =calculo_n(n)
                phi = (p-1)*(q-1)
                e = calculo_e(phi)
                codigo_criptografado = criptografador(codigo_separado, e, n)
                window['resp'].update(f'{codigo_criptografado}')
    window.close()
    
def descriptografador(codigo_criptografado, d, n):
    codigo_separado = []
    for i in codigo_criptografado:
        codigo_separado.append((i**d)%n)
    return codigo_separado

def tradutor(codigo_separado):
    global alfabeto
    txt = ''
    codigo = ''
    for i in codigo_separado:
        codigo+=f'{i}'
    i=0
    while i < len(codigo):
        j=0
        letra = codigo[i:i+2]
        print(letra)
        while j < len(alfabeto[1]):
            if letra == alfabeto[1][j]:
                txt+=alfabeto[0][j]
                letra = ''
            j+=1
        i+=2
    return txt
        
def decodificar():
    layout = [
        [sg.Text('Insira o valor de n:'), sg.Input(key = 'valor_n', size = (10,1))],
        [sg.Text('Insira o texto:'), sg.Input(key = 'txt', size = (45, 1))],
        [sg.Button('Decodificar')],
        [sg.InputText(disabled = True, key = 'resp', use_readonly_for_disable=True, size = (40, None))]
    ]
    window = sg.Window('Decodificador', layout, finalize = True)
    
    window['resp'].Widget.config(readonlybackground=sg.theme_background_color())
    window['resp'].Widget.config(borderwidth = 0)
    
    while True:
        evento, valores = window.read()
        if evento in [sg.WINDOW_CLOSED, evento == "Exit"]:
            break
        if valores['valor_n'] and valores['txt'] != '':
            if evento == 'Decodificar':
                codigo_criptografado = eval(valores['txt'])
                n = int(valores['valor_n'])
                p,q =calculo_n(n)
                phi = (p-1)*(q-1)
                e = calculo_e(phi)
                d = calculo_d(e, phi)
                codigo_separado = descriptografador(codigo_criptografado, d, n)
                texto = tradutor(codigo_separado)
                window['resp'].update(texto)
            
    window.close()

def main():
    # layout
    sg.theme('DarkAmber')
    layout = [
        [sg.Button('Codificar', size=(30,1))],
        [sg.Button('Decodificar', size=(30,1))],
        [sg.Button('Exibir chave', size=(30,1))],
    ]
    window = sg.Window('Sistema RSA', layout)

    while True:
        evento, valores = window.read()
        if evento in [sg.WINDOW_CLOSED, evento == "Exit"]:
            break
        if evento == 'Exibir chave':
            chaves()
        if evento == 'Codificar':
            codificar()
        if evento == 'Decodificar':
            decodificar()
    window.close()

if __name__ == "__main__":
    main()