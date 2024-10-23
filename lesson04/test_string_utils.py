from StringUtils import StringUtils

string_utils = StringUtils()


def capitilize(self, string):
    assert string_utils.capitilize('skypro') == 'Skypro'
    assert string_utils.capitilize('') == ''
    assert string_utils.capitilize(' ') == ' '
    assert string_utils.capitilize('  skypro') == 'Skypro'
    assert string_utils.capitilize('skypro  '.strip()) == 'Skypro'


def test_trim():
    assert string_utils.trim('   skypro') == 'skypro'
    assert string_utils.trim('skypro') == 'skypro'
    assert string_utils.trim('') == ''
    assert string_utils.trim('  ') == ''


def test_to_list():
    assert string_utils.to_list('a,b,c') == ['a', 'b', 'c']
    assert string_utils.to_list('a,,b,c') == ['a', '', 'b', 'c']
    assert string_utils.to_list('') == []
    assert string_utils.to_list('a,b,c,') == ['a', 'b', 'c', '']
    assert string_utils.to_list('1:2:3', ':') == ['1', '2', '3']


def test_contains():
    assert string_utils.contains('SkyPro', 'S') is True
    assert string_utils.contains('SkyPro', 'U') is False
    assert string_utils.contains('', 'a') == False
    assert string_utils.contains('abc', '') == True
    assert string_utils.contains('abc', 'abc') == True


def test_delete_symbol():
    assert string_utils.delete_symbol('SkyPro', 'k') == 'SyPro'
    assert string_utils.delete_symbol('SkyPro', 'Pro') == 'Sky'
    assert string_utils.delete_symbol('', 'a') == ''
    assert string_utils.delete_symbol('SkyPro', 'X') == 'SkyPro'
    assert string_utils.delete_symbol('abc123', '123') == 'abc'


def test_starts_with():
    assert string_utils.starts_with('SkyPro', 'S') is True
    assert string_utils.starts_with('SkyPro', 'P') is False
    assert string_utils.starts_with('', 'l') == False
    assert string_utils.starts_with('abc', 'a') == True
    assert string_utils.starts_with('abc', 'X') == False


def test_end_with():
    assert string_utils.end_with('SkyPro', 'o') is True
    assert string_utils.end_with('SkyPro', 'U') is False
    assert string_utils.end_with('', 'a') == False
    assert string_utils.end_with('abc', 'c') == True
    assert string_utils.end_with('abc', 'X') == False


def test_list_to_string():
    assert string_utils.list_to_string(['a', 'b', 'c'], ',') == 'a,b,c'
    assert string_utils.list_to_string(['a', '', 'b', 'c'], ',') == 'a,,b,c'
    assert string_utils.list_to_string([]) == ''
    assert string_utils.list_to_string(['a', 'b', 'c'], ':') == 'a:b:c'
    assert string_utils.list_to_string(['a', 'b', 'c'], '') == 'abc'
