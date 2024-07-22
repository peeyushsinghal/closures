
def next_fibonacci():
    """
    Create a closure to calculate the next Fibonacci number in sequence.
    
    Returns:
        function: A function that returns the next Fibonacci number each time it is called.
    """
    list_fib=[1,1] # initialize
    current_fibonacci = 0 # free variable
    def get_fibonnaci():
        """
        Calculate and return the next Fibonacci number in the sequence.
        
        Returns:
            int: The next Fibonacci number.
        """
        nonlocal current_fibonacci
        fib_num = 0
        if current_fibonacci < 2:
            fib_num = list_fib[current_fibonacci]
        else:
            fib_num = list_fib[current_fibonacci-2] + list_fib[current_fibonacci-1]
            list_fib.append(fib_num)
        current_fibonacci+=1
        print(f'current {current_fibonacci}, output {fib_num}')
        return fib_num
    return get_fibonnaci

def docstring_checker():
    """
    Create a closure to check if a given function has a docstring with more than 50 characters.
    
    Returns:
        function: A function that checks the length of the docstring of a given function.
    """

    threshold_length = 50
    def docstring_threshold_checker(fn):
        """
        Check if the docstring of a function is longer than a predefined threshold length.
        
        Parameters:
            fn (function): The function whose docstring length is to be checked.
        
        Returns:
            bool: True if the docstring length exceeds the threshold, False otherwise.
        """
        docstring = fn.__doc__
        return docstring is not None and len(docstring) > threshold_length
    return docstring_threshold_checker


def create_function_counter():
    """
    Create a function counter using a local dictionary to track function call counts.
    
    Returns:
        function: A function that wraps another function to count its calls.
    """
    dict_counter = {} # initialized 

    def count_function(func):
        """
        Wrap a function to count its calls and update the local dictionary.
        
        Parameters:
            func (function): The function to be wrapped and counted.
        
        Returns:
            function: The wrapped function that counts calls and returns the original function's result.
        """
        nonlocal dict_counter
        def inner(*args, **kwargs):
            """
            Increases the dictionary count of the function if called

            Parameters:
            args: arguments of original function
            kwargs: keyword arguments of original function
        
            Returns:
                int: returns the original function's result.
                dict: the dictionary
            """
            nonlocal dict_counter
            if func.__name__ not in dict_counter:
                dict_counter[func.__name__] = 1
            else:
                dict_counter[func.__name__] += 1
            print(f'{func.__name__} has been called {dict_counter[func.__name__]} times')
            return func(*args, **kwargs), dict_counter
        return inner

    return count_function

def create_function_counter_dict(dict_counter):
    """
    Create a function counter with a given dictionary.
    
    Parameters:
        dict_counter (dict): The dictionary to track function call counts.
    
    Returns:
        function: A function that wraps another function to update the given dictionary.
    """
    def count_function(func):
        """
        Wrap a function to count its calls and update the local dictionary.
        
        Parameters:
            func (function): The function to be wrapped and counted.
        
        Returns:
            function: The wrapped function that counts calls and returns the original function's result.
        """
        nonlocal dict_counter
        def inner(*args, **kwargs):
            """
            Increases the dictionary count of the function if called

            Parameters:
            args: arguments of original function
            kwargs: keyword arguments of original function
        
            Returns:
                int: returns the original function's result.
                dict: the dictionary
            """
            nonlocal dict_counter
            if func.__name__ not in dict_counter:
                dict_counter[func.__name__] = 1
            else:
                dict_counter[func.__name__] += 1
            print(f'{func.__name__} has been called {dict_counter[func.__name__]} times')
            return func(*args, **kwargs), dict_counter
        return inner

    return count_function


# if __name__ == "__main__":
#     def add_num(a,b):
#         return a+b
#     def mult_num(c,d):
#         return c * d
    
#     # Create different dictionaries for different sets of functions
#     add_counter_dict = {}
#     mult_counter_dict = {}

#     # Create function counters with different dictionaries
#     add_counter = create_function_counter_dict(add_counter_dict)(add_num)
#     mult_counter = create_function_counter_dict(mult_counter_dict)(mult_num)

   
#     add_counter(3,4)
#     add_counter(3,4)
#     add_counter(3,4)
#     mult_counter(1,5)
#     mult_counter(1,5)
#     mult_counter(1,5)
#     mult_counter(1,5)
#     print(add_counter(3,4))
#     print(mult_counter(1,5))

#     # counter = create_function_counter()
#     # print(counter,type(counter))

#     # count_add = counter(add_num)
#     # count_mult = counter(mult_num)


#     # count_add = function_counts(add_num)
#     # # count_mult = function_counts(mult_num)
#     # count_add(2,3)
#     # count_add(2,3)
#     # count_add(2,3)
#     # count_mult(4,5)
#     # count_mult(4,5)
#     # count_mult(4,5)
#     # count_mult(4,5)
#     # result,dict_a = count_add(4,5)
#     # print(result, dict_a)


#     # fib_num = next_fibonacci()
#     # print(fib_num())
#     # print(fib_num())
#     # print(fib_num())
#     # print(fib_num())
#     # print(fib_num())
#     # for _ in range(10):
#     #     print(fib_num())
#     # def example_greater_than_function():
#     #     """ This is an example function that has a docstring with more than 50 characters."""
#     #     pass
#     # def example_less_than_function():
#     #     """ Example function less than 50 characters."""
#     #     pass
#     # def example_no_docstrings_function():
#     #     pass
    
#     # generic_doc_string_checker = docstring_checker()

#     # print(generic_doc_string_checker(example_greater_than_function))

#     # # print(f'{example_greater_than_function.__name__} has more than 50 chars: {docstring_checker(example_greater_than_function)}')
#     # # print(f'{example_less_than_function.__name__} has more than 50 chars: {docstring_checker(example_less_than_function)}')
#     # # print(f'{example_no_docstrings_function.__name__} has more than 50 chars: {docstring_checker(example_no_docstrings_function)}')



