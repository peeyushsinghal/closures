import session6
import pytest
from session6 import *

generic_doc_string_checker = docstring_checker()

def test_session6_fn_greater_than_threshold():
    """ This is an example function that has a docstring with more than 50 characters."""
    pass
assert generic_doc_string_checker(test_session6_fn_greater_than_threshold)==True, "Failed for more than 50 characters in docstring"
def test_session6_fn_less_than_threshold():
    """ Example function less than 50 characters."""
    pass
assert generic_doc_string_checker(test_session6_fn_less_than_threshold)==False, "Failed for less than 50 characters in docstring"


def test_session6_fn_exact_threshold():
    """This docstring is exactly fifty characters long..."""
    pass
assert generic_doc_string_checker(test_session6_fn_exact_threshold)==False, "Failed for exact 50 characters in docstring"


def test_session6_fn_empty_docstrings():
    """ """
    pass
assert generic_doc_string_checker(test_session6_fn_empty_docstrings)==False, "Failed for empty docstring"

def test_session6_fn_none_docstrings():
    pass
assert generic_doc_string_checker(test_session6_fn_none_docstrings)==False, "Failed for none or no docstring"

def test_session6_next_fibonacci_case_1():
    """Test case 1: First Fibonacci number."""
    fib = next_fibonacci()
    assert fib() == 1, "Fib(1) is not coming out to be 1"

def test_session6_next_fibonacci_case_2():
    """Test case 2: Second Fibonacci number."""
    fib = next_fibonacci()
    fib()  # Generate the first Fibonacci number
    assert fib() == 1, "Fib(2) is not coming out to be 1"

def test_session6_next_fibonacci_case_3():
    """Test case 3: Third Fibonacci number."""
    fib = next_fibonacci()
    fib()  # Generate the first Fibonacci number
    fib()  # Generate the second Fibonacci number
    assert fib() == 2, "Fib(3) is not coming out to be 2"

def test_session6_next_fibonacci_case_n():
    """Test case 4: nth Fibonacci number."""
    fib = next_fibonacci()
    n = 6
    output = 0 # initialize
    for _ in range(n):
        output = fib()
    assert output == 8, "Test case 4 failed, Fib(6) is not coming out to be 8"

def add(a, b):
    """ Adds two numbers a and b"""
    return a + b

def mult(a, b):
    """ multiplies two numbers a and b"""
    return a * b

def div(a, b):
    """ divides a by non zero number b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
counter = create_function_counter()

count_add = counter(add)
count_mult = counter(mult)
count_div = counter(div)

def test_session6_add_case_1():
    """Checks for first add count and results"""
    result, counts = count_add(1, 2)
    assert result == 3, "Result for addition not ok"
    assert counts['add'] == 1, "Count for add is not 1"


def test_session6_add_case_2():
    """Checks for second add count and results"""

    result, counts = count_add(3, 4)
    print(result, counts)
    assert result == 7, "Result for addition not ok"
    assert counts['add'] == 2, "Count for add is not 2"
    

def test_session6_multiply_case_1():
    """Checks for first mult count and results"""
    result, counts = count_mult(2, 3)
    assert result == 6, "Result for multiplication not ok"
    assert counts['mult'] == 1, "Count for mult is not 1"

def test_session6_multiply_case_2():
    """Checks for second mult count and results"""
    result, counts = count_mult(4, 5)
    assert result == 20, "Result for multiplication not ok"
    assert counts['mult'] == 2, "Count for mult is not 2"

def test_session6_divide_case_1():
    """Checks for first div count and results"""
    result, counts = count_div(10, 2)
    assert result == 5, "Result for div not ok"
    assert counts['div'] == 1, "Count for div is not 1"

def test_session6_divide_case_2():
    """Checks for second div count and results"""
    result, counts = count_div(9, 3)
    assert result == 3, "Result for div not ok"
    assert counts['div'] == 2, "Count for div is not 2"

def test_session6_divide_case_3():
    """Checks for boundary condition of div"""
    try:
        count_div(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!", "Division by zero not handled"

def test_session6_mixed_operations():
    """ Checks for result and count when multiple and mixed operations are executed"""
    count_add(1, 1)
    count_mult(2, 2)
    count_div(4, 2)
    _, counts = count_mult(2, 2)
    print("....counts...", counts)
    assert counts['add'] == 3, "Test case for mixed operations failed for add"
    assert counts['mult'] == 4, "Test case for mixed operations failed for multiply"
    assert counts['div'] == 4, "Test case for mixed operations failed for divide"

# Create different dictionaries for different sets of functions
add_counter_dict = {}
mult_counter_dict = {}
div_counter_dict = {}

# Create function counters with different dictionaries
add_counter = create_function_counter_dict(add_counter_dict)(add)
mult_counter = create_function_counter_dict(mult_counter_dict)(mult)
div_counter = create_function_counter_dict(div_counter_dict)(div)

def test_session6_dict_add_case_1():
    """Checks for first add count and results"""
    result, counts = add_counter(1, 2)
    assert result == 3, "Result for addition not ok"
    assert counts['add'] == 1, "add count failed"

def test_session6_dict_add_case_2():
    """Checks for second add count and results"""
    result, counts = add_counter(3, 4)
    assert result == 7, "Result for addition not ok"
    assert counts['add'] == 2, "add count failed"

def test_session6_dict_mult_case_1():
    """Checks for first mult count and results"""
    result, counts = mult_counter(2, 3)
    assert result == 6, "Result for mult not ok"
    assert counts['mult'] == 1, " mult count failed"

def test_session6_dict_mult_case_2():
    """Checks for second mult count and results"""
    result, counts = mult_counter(4, 5)
    assert result == 20, "Result for mult not ok"
    assert counts['mult'] == 2, " mult count failed"

def test_session6_dict_div_case_1():
    """Checks for first div count and results"""
    result, counts = div_counter(10, 2)
    assert result == 5, "Result for div not ok"
    assert counts['div'] == 1, "div count failed"

def test_session6_dict_div_case_2():
    """Checks for second div count and results"""
    result, counts = div_counter(9, 3)
    assert result == 3, "Result for div not ok"
    assert counts['div'] == 2, "div count failed"

def test_session6_dict_div_case_3():
    """Checks for boundary condition of div"""
    try:
        div_counter(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!", "div failed"

def test_session6_dict_mixed_operations():
    """ Checks for result and count when multiple and mixed operations are executed"""

    add_counter(1, 1)
    mult_counter(2, 2)
    div_counter(4, 2)
    _, counts_add = add_counter(2, 2)
    _, counts_mult = mult_counter(2, 2)
    _, counts_div = div_counter(4, 2)
    
    print("....counts_add...", counts_add)
    print("....counts_mult...", counts_mult)
    print("....counts_div...", counts_div)
    
    assert counts_add['add'] == 4, "Test case for mixed operations failed for add"
    assert counts_mult['mult'] == 4, "Test case for mixed operations failed for mult"
    assert counts_div['div'] == 5, "Test case for mixed operations failed for div"
