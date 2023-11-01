import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    ignored_files = [each["nome_do_arquivo"] for each in instance._data]
    if path_file in ignored_files:
        return
    read_file = txt_importer(path_file)
    if read_file is None:
        return
    returned_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(read_file),
        "linhas_do_arquivo": read_file
    }
    instance.enqueue(returned_dict)
    print(returned_dict, file=sys.stdout)


def remove(instance):
    if len(instance._data) == 0:
        print('Não há elementos')
        return
    file_to_be_removed = instance.dequeue()
    print(
        f'Arquivo {file_to_be_removed["nome_do_arquivo"]} removido com sucesso'
        )
    return


def file_metadata(instance, position):
    try:
        searched_file = instance.search(position)
        print(searched_file, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
