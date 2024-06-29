import requests
import time


def read_records():
    url = "https://script.google.com/macros/s/AKfycbwWPTMvM6E-TH9ng42BQ2JIqKmceiZAFT_ESmZ3W9oziZsSNWtaiQ_Z5QWgsAj3vh4-/exec"
    
    params = {
        "action": "Read"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            
            # Dicionário para mapear ação para o nome do arquivo
            actions_files = {
                'frete': 'frete.txt',
                're': 're.txt',
                'direita': '/sys/class/gpio/gpio2/value',
                'esquerda': '/sys/class/gpio/gpio3/value'
            }
            
            for record in data:
                for action, file_name in actions_files.items():
                    value = record.get(action)
                    with open(file_name, 'w') as file:
                        file.write(f"{action.capitalize()}: {value}\n")
                
        except ValueError:
            print("Erro ao decodificar a resposta JSON")
    else:
        print("Erro:", response.status_code, response.text)


def clear_files():
    actions_files = ['frete.txt', 're.txt', '/sys/class/gpio/gpio2/value', '/sys/class/gpio/gpio3/value']
    for file_name in actions_files:
        with open(file_name, 'w') as file:
            file.write("")


if __name__ == "__main__":
    while True:
        read_records()
        time.sleep(3)
        # Chama a função para limpar os arquivos a cada 10 segundos (por exemplo)
        if time.time() % 10 == 0:
            clear_files()
