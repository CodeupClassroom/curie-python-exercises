# Dealing with nested lists

To go from a nested list:

```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

to a flattened list:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

1. The `sum` function

    ```python
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = sum(nested_list, [])
    ```

    This works because the `sum` function is using the `+` operator, which does
    list concatenation on all of the nested lists.

1. A more complicated list comprehension

    ```python
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = [n for a_list in nested_list for n in a_list]
    ```

    Here we iterate over every list that is a element of the nested_list (`for a_list in nested_list`), and furthormore, iterate over every element of each list element (`for n in a_list`).

## An Example

Let's say we wanted to find the odd numbers from the nested list described
above:

1. Using the `sum` function

    ```python
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_numbers = sum(nested_list, [])
    odd_numbers = [n for n in flattened_numbers if n % 2 == 1]
    ```

    We could put all of this on a single line if we wanted to:

    ```python
    [n for n in sum(nested_list, []) if n % 2 == 1]
    ```

1. Using a more fancy list comprehension


    ```python
    [n for a_list in nested_list for n in a_list if n % 2 == 1]
    ```
