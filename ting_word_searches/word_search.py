from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def exists_word(word, instance):
    results = []
    word_lower = word.lower()
    for file_info in instance._data:
        file_name = file_info["nome_do_arquivo"]
        file_lines = file_info["linhas_do_arquivo"]
        occurrences = []
        for line_number, content in enumerate(file_lines):
            line = content.lower()
            if word_lower in line:
                occurrences.append({"linha": line_number+1})
        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })
    return results


def search_by_word(word, instance):
    results = []
    word_lower = word.lower()
    for file_info in instance._data:
        file_name = file_info["nome_do_arquivo"]
        file_lines = file_info["linhas_do_arquivo"]
        occurrences = []
        for line_number, content in enumerate(file_lines):
            line = content.lower()
            if word_lower in line:
                occurrences.append(
                    {"linha": line_number+1, "conteudo": content}
                    )
        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })
    return results


if __name__ == "__main__":
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = search_by_word("pedro", project)
    print(word)
