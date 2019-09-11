def test_sum_list(fixture_function, fixture_module, fixture_class, fixture_session):
    """функция сравнивает сумму чисел из фикстур с числом"""
    assert sum([fixture_function, fixture_module, fixture_class, fixture_session]) >= 7


def test_sum_int(fixture_function, fixture_session):
    """функция проверяет тип данных суммы двух цифр"""
    a = fixture_function + fixture_session
    assert isinstance(a, int)


def test_sum_tuple():
    """функция проверяет сумму чисел в кортеже"""
    t = (1, 2, 3)
    assert sum(t) == 6


def test_len_list(fixture_function):
    """функция проверяет длину списка после продления"""
    h = [1, 2, 3]
    h.extend([4, fixture_function])
    assert len(h) == 5


def test_sum_str(fixture_class):
    """функция проверяет сложение двух строк"""
    s1 = 'fixture class = '
    assert s1 + str(fixture_class) == 'fixture class = 3'


def test_list_entry(fixture_function):
    """функция проверяет вхождение числа в список"""
    ls = [x for x in range(1, 50)]
    assert fixture_function in ls


def test_set_unique():
    """функция проверяет уникальность значений в множестве"""
    s = {1, 2, 3, 3, 2, 1, 2, 3}
    assert sum(s) == 6
    assert len(s) == 3


def test_dict_add(fixture_function):
    """функция проверяет добавление пары ключ-значение в словарь"""
    f = fixture_function
    d = {a: a ** 2 for a in range(f)}
    d[f] = f ** 2
    assert len(d) == f + 1


def test_dict_fromkeys(fixture_function):
    """функция проверяет создание словаря с помощью метода fromkeys"""
    d = dict.fromkeys(['a', 'b'], fixture_function)
    assert d['a'] == fixture_function
    assert d['b'] == fixture_function


def test_list_to_str():
    """функция проверяет преобразование списка в строку"""
    s = ['stupid', 'tests']
    final = ' '.join(s)
    assert final == 'stupid tests'
