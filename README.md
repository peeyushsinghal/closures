# Session 6: Closures 

## Overview

This module provides a collection of utilities for managing function call counts, checking function docstring lengths, and generating Fibonacci numbers. It includes the following key functionalities:

1. **Fibonacci Sequence Generator**: A closure to generate the next Fibonacci number in sequence.
2. **Docstring Length Checker**: A closure to determine if a function's docstring exceeds a specified length.
3. **Function Call Counter**: A decorator and closure for counting function calls with support for using different dictionaries.
4. **Function Call Counter with Dictionary**: A closure to create function counters that update specific dictionaries.

## Functions

### `next_fibonacci`

The `next_fibonacci` function creates a closure that generates the next number in the Fibonacci sequence each time it is called. This utility maintains the sequence and current index internally, allowing for successive retrieval of Fibonacci numbers.

**Usage**: 
- To generate the next Fibonacci number, call the function returned by `next_fibonacci`. Each call yields the next number in the sequence.

### `docstring_checker`

The `docstring_checker` function creates a closure designed to check if a function's docstring exceeds a length of 50 characters. This utility helps in validating the completeness of function documentation.

**Usage**:
- To check a function's docstring length, use the function returned by `docstring_checker` with the function you want to inspect. It returns `True` if the docstring length exceeds 50 characters and `False` otherwise.

### `create_function_counter`

The `create_function_counter` function returns a closure that acts as a decorator to count the number of times a function is called. It utilizes a local dictionary to track these counts, providing insights into function usage.

**Usage**:
- Apply the decorator returned by `create_function_counter` to any function you wish to monitor. The decorator will increment the call count each time the function is executed and provide the updated count.

### `create_function_counter_dict`

The `create_function_counter_dict` function creates a function counter using a specified dictionary to track function call counts. This allows you to manage multiple dictionaries for different sets of functions, offering flexibility in tracking function usage.

**Usage**:
- Pass a dictionary to `create_function_counter_dict` to initialize a function counter. Apply the decorator returned by this function to your functions. The decorator will update the provided dictionary with the call counts for each function.
