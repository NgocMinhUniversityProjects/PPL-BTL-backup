"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Test Cases ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4.1 Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"

def test_integer_multiple_digit():
    """4.2 Integer literal"""
    tokenizer = Tokenizer("123")
    assert tokenizer.get_tokens_as_string() == "123,<EOF>"

def test_integer_negative():
    """4.3 Integer literal"""
    tokenizer = Tokenizer("-567")
    assert tokenizer.get_tokens_as_string() == "-,567,<EOF>"

def test_integer_multiple_negative():
    """4.4 Integer literal"""
    tokenizer = Tokenizer("-----567")
    assert tokenizer.get_tokens_as_string() == "--,--,-,567,<EOF>" 
    # -- is prioritized, still dunno about which - gets OP_DEC and which one is OP_SUB but whatever, probably correct

def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

def test_float_format_1():
    """Test valid format of float: omiting decimal part"""
    tokenizer = Tokenizer(".1")
    assert tokenizer.get_tokens_as_string() == ".1,<EOF>"

def test_float_format_2():
    """Test valid format of float: omitting fractional part"""
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"

def test_float_format_3():
    """Test valid format of float: omitting fractional part, with exponent"""
    tokenizer = Tokenizer("1e10")
    assert tokenizer.get_tokens_as_string() == "1e10,<EOF>"

def test_float_format_4():
    """Test valid format of float: with fractional part, with exponent"""
    tokenizer = Tokenizer("1.1e10")
    assert tokenizer.get_tokens_as_string() == "1.1e10,<EOF>"

def test_float_format_5():
    """Test valid format of float: omitting fractional part, with negative exponent"""
    tokenizer = Tokenizer("1e-10")
    assert tokenizer.get_tokens_as_string() == "1e-10,<EOF>"

def test_float_format_6():
    """Test valid format of float: with fractional part, with negative exponent"""
    tokenizer = Tokenizer("1.1e-10")
    assert tokenizer.get_tokens_as_string() == "1.1e-10,<EOF>"

def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_identifier_has_keyword():
    """7.2 Identifier"""
    tokenizer = Tokenizer("int switch = 5")
    assert tokenizer.get_tokens_as_string() == "int,switch,=,5,<EOF>" # still tokenizable, valid or not is not the job of the lexer

def test_identifier_has_invalid_char():
    """7.2 Identifier"""
    tokenizer = Tokenizer("int * = 5")
    assert tokenizer.get_tokens_as_string() == "int,*,=,5,<EOF>" # still tokenizable, valid or not is not the job of the lexer


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comment():
    """8.1 Block comment"""
    tokenizer = Tokenizer("/* fikwhfvihbwihfiwehf \n\r\t dijhidfkn2inf */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

def test_string_literal_quote_stripping():
    """11. Test proper quote stripping of the string literal"""
    tokenizer = Tokenizer("\"Hello world!\"")
    assert tokenizer.get_tokens_as_string() == "Hello world!,<EOF>"