from lexical.obi_yacc import validate_syntax
import sys

def test_syntax(file: str):
    # Build the parser
    
    return validate_syntax(file)

def main():
    arguments = sys.argv

    if len(arguments) == 1:
        print("No file specified")
        return
    
    file_name = arguments[1]   
    validate_syntax(file_name)

if __name__=="__main__":
    main()