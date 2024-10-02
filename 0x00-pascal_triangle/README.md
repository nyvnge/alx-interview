# Pascal's Triangle

## Description

This project contains a function `pascal_triangle(n)` that generates Pascal's Triangle up to the `n`th row. Pascal's Triangle is a triangular array of binomial coefficients, where each number is the sum of the two numbers directly above it.

## Function

### `pascal_triangle(n)`

- **Parameters**: 
  - `n` (int): The number of rows to generate in Pascal's Triangle.
  
- **Returns**:
  - A list of lists of integers representing Pascal’s triangle.
  - Returns an empty list if `n <= 0`.

### Example

Given `n = 5`, the output will be:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

### Usage

To use the `pascal_triangle` function, you can run the provided `0-main.py` script:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Run the script:
   ```bash
   ./0-main.py
   ```

## Example Output

Here is an example of the output when running the `0-main.py` script with `n = 5`:

```bash
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Requirements

- Python

## Author

Sanderson Nyange
```


