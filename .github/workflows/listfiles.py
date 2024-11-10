from pathlib import Path

def listar_arquivos():
    print("Executando listfiles.py")
    caminho_pasta = Path('.\\flutter\\').resolve()
    print(f"Procurando arquivos em: {caminho_pasta}")

    if caminho_pasta.exists():
        encontrou_arquivos = False
        for file in caminho_pasta.rglob('*'):
            if file.is_file():
                encontrou_arquivos = True
                print(file)
        if not encontrou_arquivos:
            print("Nenhum arquivo encontrado.")
    else:
        print("Caminho não encontrado.")

listar_arquivos()
