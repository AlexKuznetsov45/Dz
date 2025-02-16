import pytest
from string_utils import StringUtils


string_utils = StringUtils()



@pytest.mark.positive
def test_capitalize_positive():
    string_utils = StringUtils()
    result = string_utils.capitalize("test")
    assert result == "Test"

@pytest.mark.negative
def test_capitalize_negative():
    string_utils = StringUtils()
    result = string_utils.capitalize("")
    assert result == ""

@pytest.mark.positive   
def test_trim_positive():
    string_utils = StringUtils()
    result = string_utils.trim("   test")
    assert result == "test"

@pytest.mark.negative
def test_trim_negative():
    string_utils = StringUtils()
    result = string_utils.trim(" ")
    assert result == ""


@pytest.mark.positive 
def test_contains_positive():
    string_utils = StringUtils()
    result = string_utils.contains("SkyPro", "S")
    assert result is True


@pytest.mark.negative
def test_contains_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contains(None, "S")


@pytest.mark.positive
def test_delete_symbol_positive():
    string_utils = StringUtils()
    result = string_utils.delete_symbol("SkyPro", "o")
    assert result == "SkyPr"

@pytest.mark.negative
def test_delete_symbol_negative():
    string_utils = StringUtils()
    result = string_utils.delete_symbol("", "a")
    assert result == ""