#!/usr/bin/env python

from lexical.obi_yacc import validate_syntax
from execution.vm import read_file
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
    file_name = arguments[2]
    read_file(file_name)

if __name__=="__main__":
    main()