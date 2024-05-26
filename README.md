# FrProg Compiler

This mini-project includes a multi-pass compiler for the FrProg language, consisting of preprocessing, lexing, and parsing phases. The compiler is implemented using Python and the PLY library.

## Brief Description

The FrProg Compiler project is designed to compile source code written in the FrProg language. This multi-pass compiler includes three main phases: preprocessing, lexing, and parsing. The preprocessing phase removes comments from the source code, the lexing phase tokenizes the preprocessed code, and the parsing phase checks the tokenized code for syntax errors. The project is implemented in Python using the PLY library, which provides tools for lexical analysis and parsing.

## Project Structure

- `preprocessor.py`: This script performs preprocessing on the FrProg code to remove comments.
- `lexer.py`: This script tokenizes the preprocessed FrProg code and writes the tokens to `resultat_lexer.txt`.
- `parser.py`: This script reads the tokens from `resultat_lexer.txt` and parses them to detect syntax errors.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/elhamssan/frprog-compiler.git
   cd frprog-compiler

2. **Install Required Packages**

    ```bash
    pip install ply

## Usage

### Preprocessing
1. Ensure your FrProg source code is in a file named `code.txt`.

2. Run the preprocessor:

    ```bash
    python preprocessor.py

This will create a file named `preprocessed_code.txt` with comments removed.


### Lexing
1. Run the lexer :

    ```bash
    python lexer.py

This will create a file named `resultat_lexer.txt` with the tokens generated from the preprocessed code.

### Parsing
1. Run the parser:

    ```bash
    python parser.py

The parser will read the tokens from `resultat_lexer.txt` and check for syntax errors. If parsing is successful, it will print **"Parsing completed successfully."** Otherwise, it will print **"Parsing failed due to syntax errors."**