def lfsr_r_tact(sequence: str):
    """Виконує один такт LFSR з рознесеним зворотним зв'язком.
       sequence - бінарна початкова послідовність."""

    sequence = list(sequence)
    random_num = sequence[0]
    for i in [6, 4, 1]:
        if (sequence[0] == '1') & (sequence[len(sequence)-i] == '1'):
            sequence[len(sequence)-i] = '0'
        else:
            sequence[len(sequence)-i] = str(int(sequence[len(sequence)-i]) + int(sequence[0]))
    sequence = ''.join(sequence)
    sequence = sequence[1:] + sequence[0]
    return [sequence, random_num]


def startstop_generator(basic_num: str, extra_num: str, length_of_random_sequence: int):
    """Стартстопний генератор.
       basic_num - початкова бінарна послідовність основної LFSR,
       extra_num - початкова бінарна послідовність додаткової LFSR,
       length_of_random_sequence - довжина генерованої бінарної послідовності."""

    random_sequence = str()
    basic_tact = [basic_num, '']
    while len(random_sequence) < length_of_random_sequence:
        extra_tact = lfsr_r_tact(extra_num)
        extra_num = extra_tact[0]
        if extra_tact[1] == '1':
            basic_tact = lfsr_r_tact(basic_num)
            random_sequence += basic_tact[1]
            basic_num = basic_tact[0]
        else: random_sequence += basic_tact[1]

    return random_sequence


def frequency_test(sequence: str):
    """Частотний тест."""

    number_1 = 0
    for i in sequence:
        if i == '1':
            number_1 += 1
    return 'Одиниць --> {n}/{all}\n' \
           'Нулів -------> {m}/{all}'.format(n=number_1, all=len(sequence), m=len(sequence)-number_1)


def differential_frequency_test(sequence: str):
    """Диференційний частотний тест."""

    num_changes = 0
    for i in list(range(len(sequence)-1)):
        if sequence[i] != sequence[i+1]:
            num_changes += 1
    return '  {}/{}'.format(num_changes, (len(sequence)-1))


# розмір вікна = 5
def window_test(sequence: str):
    """Віконний тест."""

    possible_windows = {'00000': 0, '00001': 0, '00010': 0, '00011': 0,
                        '00100': 0, '00101': 0, '00110': 0, '00111': 0,
                        '01000': 0, '01001': 0, '01010': 0, '01011': 0,
                        '01100': 0, '01101': 0, '01110': 0, '01111': 0,
                        '10000': 0, '10001': 0, '10010': 0, '10011': 0,
                        '10100': 0, '10101': 0, '10110': 0, '10111': 0,
                        '11000': 0, '11001': 0, '11010': 0, '11011': 0,
                        '11100': 0, '11101': 0, '11110': 0, '11111': 0}
    for i in list(range(len(sequence)-4)):
        possible_windows[sequence[i:i+5]] += 1
        i += 1
    for j in list(possible_windows.keys()):
        possible_windows[j] = '{}/{}'.format(possible_windows[j], 32)
    l = sorted(possible_windows.keys())
    result = ''
    for i in l:
        result = result + '{} -> {}\n'.format(i, possible_windows[i])
    return result


def complexity_test_nonlinear(sequence: str):
    """Нелінійний тест на складність."""

    window_size = 1  # nonlinear complexity
    flag = True
    while flag:
        flag = False
        windows = {}
        for i in range(len(sequence) - window_size):
            window = sequence[i:i + window_size]
            if window not in windows.keys():
                windows.setdefault(window, sequence[i + window_size])
            else:
                if windows[window] != sequence[i + window_size]:
                    window_size += 1
                    flag = True
                    break

    return 'Кількість бітів, від яких залежить наступний біт ---> {}\n\n'.format(window_size)
