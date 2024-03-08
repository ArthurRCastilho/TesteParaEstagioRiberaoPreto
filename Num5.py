# 01 Recebe a String que deseja converter
String = str(input('Digite a String que deseja inverter: '))

#02 Converter a String para uma lista de caracteres
string_lista = list(String)

#03 Descobrir o tamanho da String 
tamanhoDaString = len(string_lista)

#04 Inverte todos os caracteres
for i in range(tamanhoDaString // 2):

    # 05 Troca os caracteres simétricos
    string_lista[i], string_lista[tamanhoDaString - 1 - i] = string_lista[tamanhoDaString - 1 - i], string_lista[i]

    #06 Voltando a lista para uma String
    string_invertida = ''.join(string_lista)

#07 Printa a string invetida
print(f'A string invertida fica  assim: {string_invertida}')