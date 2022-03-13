def bubble_sort(seq):
    """
    Функция пузырьковой сортировки.
    Вариант для целых чисел, вещественных чисел и строк
    :param day: последовательность элементов.
    :return: отсортированная последовательность тех же элементов.
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq