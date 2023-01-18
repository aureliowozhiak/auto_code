README
======

This code utilizes the OpenAI API to generate code with a specified name and main function. The generated code will be written to a file with the code name and a specified file extension.

Usage
-----

1.  Obtain an API key for OpenAI and save it in a text file named 'key'.
2.  Import the AutoCode class.
3.  Create an instance of the AutoCode class.
4.  Use the `create_code` method to generate code. The method has parameters:
    *   `code_name`: The name of the code to be generated.
    *   `main_function`: A brief description of what the code should do.
    *   `is_class`: (Optional) Parameter to indicate if it is a class or not. Default is False
    *   `code_lang`: (Optional) The language of the code to be generated. Default is 'Python'.
    *   `extension`: (Optional) The file extension for the generated code file. Default is '.py'.
5.  The generated code will be written to a file with the code name and specified file extension.

Example
-------

```
```
from auto_code import AutoCode
code_generator = AutoCode()
code_generator.create_class("MyClass", "add two numbers together", is_class = True)
```
```

This will create a file named "myclass.py" with a class named "MyClass" that has a method that adds two numbers together in Python.

Note
----

The OpenAI API key must be in the same directory as the code.

Limitations
-----------

The generated code may not always be syntactically correct or efficient. It is recommended to review and test the generated code before using it in production.