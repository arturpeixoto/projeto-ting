import sys


def txt_importer(path_file):
    try:
        with open(path_file, 'r') as file:
            if path_file.endswith(".txt"):
                lines = file.read()
                return lines.split('\n')
            else:
                print("Formato inválido", file=sys.stderr)
                return None
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
