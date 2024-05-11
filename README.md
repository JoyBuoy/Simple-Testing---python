# Simple-Testing---python
# Hello.py

This is a simple Python script that contains a function for adding two numbers.

## Function

### `add_numbers(num1, num2)`

This function takes two arguments, `num1` and `num2`, which should be numbers. It returns the sum of `num1` and `num2`.

## Usage

You can import the `add_numbers` function into your Python script like so:

```python
from hello import add_numbers

result = add_numbers(1, 2)
print(result)  # Outputs: 3



# Test Hello.py

This is a test suite for the `add_numbers` function in the `hello.py` script.

## Test Function

### `test_add_numbers()`

This function tests the `add_numbers` function from `hello.py`. It asserts that the function correctly adds two numbers together.

## Usage

To run the tests, you need to have `pytest` installed. If it's not installed, you can install it with pip:

```bash
pip install pytest

Then, you can run the tests with the following command:
pytest test_hello.py