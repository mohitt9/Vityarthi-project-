# Trigonometric Calculator

A simple terminal-based Python project for calculating the six trigonometric functions: **sin, cos, tan, cosec, sec, and cot**.

The program accepts an angle/value in either **degrees or radians**, gives the selected trigonometric result, handles undefined values, and keeps running until the user selects the Exit option.

## Features

- Accepts values in degrees or radians
- Calculates:
  - sin
  - cos
  - tan
  - cosec
  - sec
  - cot
- Menu-driven terminal interface
- Accepts both menu numbers and function names
- Handles invalid numeric input
- Handles invalid menu choices
- Detects undefined trigonometric values
- Provides an Exit option
- Uses Python's built-in `math` module only

## Requirements

- Python 3.x
- No external Python packages are required

## Project Structure

```text
Trigo-Calculator/
│
├── README.md
└── trigo_calculator.py
```

## How to Run

### 1. Install Python

Make sure Python 3.x is installed on your computer.

To check:

```bash
python --version
```

If `python` is not recognized, try:

```bash
py --version
```

### 2. Open a terminal

Open Command Prompt, PowerShell, or another terminal.

### 3. Move to the project folder

For example:

```bash
cd Downloads\Trigo-Calculator
```

Use the actual location of the project folder on your computer.

### 4. Run the program

```bash
python trigo_calculator.py
```

If that command does not work on Windows, try:

```bash
py trigo_calculator.py
```

## How to Use

1. Enter the angle/value.
2. Enter `y` if the value is already in radians.
3. Enter `n` if the value is in degrees.
4. Select a trigonometric function from the menu.
5. The calculated result is displayed.
6. The program returns to the menu for another calculation.
7. Select `7` to exit.

### Example

```text
========================================
       TRIGONOMETRIC CALCULATOR
========================================
Calculate sin, cos, tan, cosec, sec and cot.

Enter the angle/value: 30
Is the value in radians? (y/n): n

Choose a function:
1 -> sin
2 -> cos
3 -> tan
4 -> cosec
5 -> sec
6 -> cot
7 -> Exit
Enter your choice: 1

sin(0.5235987755982988) = 0.5000000000

Returning to the main menu...
```

## Handling Undefined Values

Some trigonometric functions are undefined for particular values. The program checks the relevant denominator before calculating:

- `tan(x) = sin(x) / cos(x)` → undefined when `cos(x)` is zero.
- `cosec(x) = 1 / sin(x)` → undefined when `sin(x)` is zero.
- `sec(x) = 1 / cos(x)` → undefined when `cos(x)` is zero.
- `cot(x) = cos(x) / sin(x)` → undefined when `sin(x)` is zero.

The program displays an appropriate message instead of producing a division-by-zero error.

## Testing

The program can be manually tested using cases such as:

| Test case | Input | Expected result |
|---|---|---|
| Sine in degrees | 30, `n`, `sin` | 0.5 |
| Cosine in degrees | 60, `n`, `cos` | 0.5 |
| Tangent in degrees | 45, `n`, `tan` | 1 |
| Sine in radians | π/2, `y`, `sin` | 1 |
| Undefined tangent | 90, `n`, `tan` | Undefined |
| Undefined cosecant | 0, `n`, `cosec` | Undefined |
| Exit | `7` | Program closes |

## Technology Used

- Python 3
- Built-in `math` module

## Creator

Mohit Gaur
