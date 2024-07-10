#Tudo que está em verde são as explicações basicas de cada linha.
#Itera = "percorrer" ou "repertir"

import requests # Importa a biblioteca requests para fazer requisições HTTPS
import time # Importa a biblioteca time para manipulação do tempo

def read_records(): # Função para ler registros de uma URL especificada
    url = "https://script.google.com/macros/s/AKfycbwWPTMvM6E-TH9ng42BQ2JIqKmceiZAFT_ESmZ3W9oziZsSNWtaiQ_Z5QWgsAj3vh4-/exec"
    
    params = {
        "action": "Read"  # Parâmetro para a requisição HTTP GET
    }
    
    # Faz a requisição GET para a URL especificada com os parâmetros fornecidos
    response = requests.get(url, params=params)
    
    if response.status_code == 200: # Verifica se a resposta foi bem-sucedida
        try:
            data = response.json() # Tenta decodificar a resposta JSON
            
            # Dicionário para mapear ação para o nome do arquivo
            actions_files = {
                'frete': 'frete.txt', # Não sera necessario, esta sendo substituido pelo direita e esquerda.
                're': '/sys/class/gpio/gpio4/value',
                'direita': '/sys/class/gpio/gpio2/value',
                'esquerda': '/sys/class/gpio/gpio3/value'
                #E preciso implementar no raspb. L (5:8)
            }
            
            # Itera sobre os registros recebidos
            for record in data:
                for action, file_name in actions_files.items():
                    value = record.get(action) # Obtém o valor correspondente à ação
                    with open(file_name, 'w') as file:
                        # Escreve o valor no arquivo
                        file.write(f"{action.capitalize()}: {value}\n")        
                
        except ValueError:
            print("Erro ao decodificar a resposta JSON") # Caso ocorra um erro na decodificação do JSON
    else:
        print("Erro:", response.status_code, response.text) # Exibe o erro se a requisição não for bem-sucedida


def clear_files(): # Função para limpar os arquivos
    actions_files = ['frete.txt', '/sys/class/gpio/gpio4/value', '/sys/class/gpio/gpio2/value', '/sys/class/gpio/gpio3/value']
    for file_name in actions_files:
        with open(file_name, 'w') as file:
            file.write("") # Escreve uma string vazia para limpar o conteúdo dos arquivos

# Bloco principal que será executado quando o script for rodado
if __name__ == "__main__":
    while True:
        read_records() # Chama a função para ler os registros
        time.sleep(3) # Pausa a execução por 3 segundos
        # Chama a função para limpar os arquivos a cada 10 segundos (por exemplo)
        if time.time() % 10 == 0:
            clear_files()
