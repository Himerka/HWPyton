from StringUtils import StringUtils

string_utils = StringUtils()

# Позитивные проверки
def test_capitilize_positive():
    assert string_utils.capitilize('skypro') == 'Skypro'
    assert string_utils.capitilize('  skypro'.strip()) == 'Skypro'
    assert string_utils.capitilize('skypro  '.strip()) == 'Skypro'

def test_trim_positive():
    assert string_utils.trim('   skypro') == 'skypro'
    assert string_utils.trim('skypro') == 'skypro'
    assert string_utils.trim('') == ''
    assert string_utils.trim('  ') == ''

def test_to_list_positive():
    assert string_utils.to_list('a,b,c') == ['a', 'b', 'c']
    assert string_utils.to_list('a,,b,c') == ['a', '', 'b', 'c']
    assert string_utils.to_list('a,b,c,') == ['a', 'b', 'c', '']
    assert string_utils.to_list('1:2:3', ':') == ['1', '2', '3']

def test_contains_positive():
    assert string_utils.contains('SkyPro', 'S') is True
    assert string_utils.contains('abc', '') is True
    assert string_utils.contains('abc', 'abc') is True

def test_delete_symbol_positive():
    assert string_utils.delete_symbol('SkyPro', 'k') == 'SyPro'
    assert string_utils.delete_symbol('', 'a') == ''
    assert string_utils.delete_symbol('SkyPro', 'X') == 'SkyPro'
    assert string_utils.delete_symbol('abc123', '123') == 'abc'

def test_starts_with_positive():
    assert string_utils.starts_with('SkyPro', 'S') is True
    assert string_utils.starts_with('abc', 'a') is True

def test_end_with_positive():
    assert string_utils.end_with('SkyPro', 'o') is True
    assert string_utils.end_with('abc', 'c') is True

def test_list_to_string_positive():
    assert string_utils.list_to_string(['a', 'b', 'c'], ',') == 'a,b,c'
    assert string_utils.list_to_string(['a', '', 'b', 'c'], ',') == 'a,,b,c'
    assert string_utils.list_to_string([]) == ''
    assert string_utils.list_to_string(['a', 'b', 'c'], ':') == 'a:b:c'
    assert string_utils.list_to_string(['a', 'b', 'c'], '') == 'abc'

# Негативные проверки
def test_capitilize_negative():
    # Проверяем, что пробелы не влияют на результат
    assert string_utils.capitilize(' ') == ' '

def test_to_list_negative():
    # Проверяем пустую строку
    assert string_utils.to_list('') == []

def test_contains_negative():
    # Проверяем отсутствие символа в строке
    assert string_utils.contains('SkyPro', 'U') is False
    # Проверяем пустую строку и символ
    assert string_utils.contains('', 'a') is False

def test_delete_symbol_negative():
    # Проверяем удаление символа, которого нет в строке
    assert string_utils.delete_symbol('SkyPro', 'X') == 'SkyPro'

def test_starts_with_negative():
    # Проверяем пустую строку и символ
    assert not string_utils.starts_with('', 'l')

def test_end_with_negative():
    # Проверяем пустую строку и символ
    assert not string_utils.end_with('', 'a')

def test_list_to_string_negative():
    # Проверяем пустой список
    assert string_utils.list_to_string([]) == ''