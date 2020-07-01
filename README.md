# Calc-It
A toy compiler (lexer-parser) written in python viz RPLY and LLVMLite to calculate simple mathematical expressions.

To do:
 
* Code Lexer. ✔
* Code Parser. ✔
* Code AST. ✔
* Use LLVMLite for optimisation and conversion to machine code.

## Installation

Follow the steps to run the web-app on your local machine:

1. Clone the repository

    ```shell
    git clone https://github.com/chumba-wamba/Calc-It.git
    ```
2. Install the Dependencies

    ```shell
    cd Calc-It
    pip install -r requirements.txt
    ```
 
 ## Usage
 1. Enter the cloned repository
 ```shell
 cd Calc-It
 ```
 
 2. Edit the input string in run.py
 ```python
 from calc_it.lexer import lexer
 from calc_it.parser import parser


if __name__ == "__main__":
    input_string = "1+5**(2*3)"
    tokens = lexer.lex(input_string)
    print(parser.parse(tokens).eval())

 ```
 
 3. Execute the program
 ```python
  python run.py
 ```
