from pathlib import Path

def listar_arquivos():
    caminho_pasta = Path('.\\flutter\\windows\\flutter\\')
    for file in caminho_pasta.rglob('*'):
        if file.is_file():
            print(file)

# Executando a função
listar_arquivos()
