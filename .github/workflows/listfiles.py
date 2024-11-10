from pathlib import Path

def listar_arquivos():
    print("Executando listfiles.py")  # Confirma que o script iniciou
    caminho_pasta = Path('.\\flutter\\windows\\flutter\\').resolve()
    print(f"Procurando arquivos em: {caminho_pasta}")

    if caminho_pasta.exists():
        for file in caminho_pasta.rglob('*'):
            if file.is_file():
                print(file)
    else:
        print("Caminho não encontrado.")

listar_arquivos()
