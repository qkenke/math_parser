# ExpressionEvaluator

A simple expression evaluator written in Python using the `ast` module.  
It supports mathematical expressions and variable assignments directly from user input.

## 📌 Features

- Supports basic arithmetic operations: `+`, `-`, `*`, `/`
- Supports parentheses and operator precedence
- Supports negative numbers (unary minus)
- Allows defining and using variables in expressions (e.g. `x = 2 + 3`)
- Simple REPL interface (input/output loop)

## ✅ Supported Operators

| Operator | Description         |
|----------|---------------------|
| `+`      | Addition             |
| `-`      | Subtraction / Negation |
| `*`      | Multiplication       |
| `/`      | Division             |

## 🚀 How It Works

- The code uses Python’s `ast` (Abstract Syntax Tree) to safely parse expressions.
- Arithmetic operations are matched with Python's `operator` functions.
- Variables are stored in a dictionary and can be reused in later expressions.

## 🧠 Example Usage

x = 2 + 3

x = 5.0

y = x * 10

y = 50.0

y + 100

150.0

-x

-5.0

exit

## 🧱 Project Structure

- `ExpressionEvaluator`: The main class containing evaluation logic.
  - `assign(name, value)`: Stores a variable with its value.
  - `evaluate(expr)`: Parses and calculates an expression.
  - `_eval(node)`: Recursively walks the AST to compute results.
- `__main__`: A simple REPL loop for input and output.

## ⚠️ Limitations

- Only works with numeric expressions.
- Does not support functions (like `sin`, `log`, etc.)
- No error recovery or complex error hints.

## 📂 Requirements

- Python 3.8 or later (for `ast.Constant`)
- No external dependencies

