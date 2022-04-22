# Obiecti

Obiecti is a brand new OOP programming language 👾👾👾

Requirements:
    
    pip install ply

To run your file:
    
    python3 compile.py YOUR_FILE_NAME.txt

To run the tests: 🧪🧪🧪🧪
    
    python3 -m unittest discover -s tests/ -v

Information about the v1:
    A lexical analyzer has been build to recognize the tokens of the language taking in consideration the sytax proposals that were delivered to M.C. Elda Quiroga

Semantical Proposal:
    The following is a semantical proposal for the Obiecti language.
    We will be using the following terms:
        Data Type
        Operation

    This will be used for the semantic cube of the language.

    Data Type:
        Integer
        Float
        String
        Char

    Operation:
        sum
        sub
        div
        mult

    The semantic cube is the following:
        int + int = int
        int + float = float
        int + char = char
        float + int = float
        float + float = float
        char + int = char
        char + char = char
        char + string = string
        string + char = string

        int - int = int
        int - float = float
        int - char = char
        float - int = float
        float - float = float
        char - int = char
        char - char = char

        int * int = int
        int * float = float
        float * float = float

        int / int = int
        int / float = float
        float / float = float

    Is not possible to do:
        int OP string
        int OP char
        float OP string
        float OP char

