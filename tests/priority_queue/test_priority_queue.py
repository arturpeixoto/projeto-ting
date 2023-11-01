import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    file01 = {
        "nome_do_arquivo": "arquivo1",
        "qtd_linhas": 6,
        "linhas_do_arquivo":
            ['linha1', 'linha2', 'linha3', 'linha4', 'linha5', 'linha6']
    }
    file02 = {
        "nome_do_arquivo": "arquivo2",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ['linha1', 'linha2', 'linha3']
    }
    file03 = {
        "nome_do_arquivo": "arquivo3",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ['linha1', 'linha2']
    }
    priority_queue.enqueue(file01)
    assert len(priority_queue) == 1
    assert priority_queue.is_priority(file01) is False
    assert priority_queue.search(0) == file01

    priority_queue.enqueue(file02)
    assert len(priority_queue) == 2
    assert priority_queue.is_priority(file02) is True
    assert priority_queue.search(0) == file02

    priority_queue.enqueue(file03)
    assert len(priority_queue) == 3
    assert priority_queue.is_priority(file03) is True
    assert priority_queue.search(1) == file03

    priority_queue.dequeue()
    # first_dequeue = priority_queue.dequeue()
    # assert first_dequeue["nome_do_arquivo"] == "arquivo2"
    # assert first_dequeue["qtd_linhas"] == 3
    assert len(priority_queue) == 2

    priority_queue.dequeue()
    # second_dequeue = priority_queue.dequeue()
    # assert second_dequeue["nome_do_arquivo"] == "arquivo3"
    # assert second_dequeue["qtd_linhas"] == 2
    assert len(priority_queue) == 1

    priority_queue.dequeue()
    # third_dequeue = priority_queue.dequeue()
    # assert third_dequeue["nome_do_arquivo"] == "arquivo1"
    # assert third_dequeue["qtd_linhas"] == 6
    assert len(priority_queue) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(-1)
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(4)
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(len(priority_queue))
