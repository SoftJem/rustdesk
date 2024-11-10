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
                print(f"Arquivo encontrado: {file}")

                # Abrindo o arquivo e procurando pela palavra-chave
                with file.open('r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read()
                    if "RustdeskMultiWindow" in conteudo:
                        print(f"'{file.name}' contém 'RustdeskMultiWindow'.")

        if not encontrou_arquivos:
            print("Nenhum arquivo encontrado.")
    else:
        print("Caminho não encontrado.")

listar_arquivos()
