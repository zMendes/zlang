# zlang
---
#### EBNF


BLOCK = "{", { COMMAND }, "}" ;  
COMMAND = ( λ | ASSIGNMENT | PRINT | BLOCK | CONDITION | WHILE | FOR), ";" ;  
ASSIGNMENT = TYPE, IDENTIFIER, "=", ( OREXP | STRING | CHAR ) ;  
CONDITION = "IF","(", OREXP, ")", COMMAND, { "ELSE", COMMAND } ;  
WHILE = "WHILE", "(", OREXP, ")", COMMAND ;  
FOR = "FOR", "(", ASSIGNMENT,";",CONDITION,";", ASSIGNMENT,")", COMMAND ;  
PRINT = "print", "(", (OREXP | STRING | CHAR), ")" ;  
OREXP = ( ANDEXP, { "||", ANDEXP  } ;  
ANDEXP = EQEXP, { "&&", EQEXP } ;  
EQEXP = RELEXP, { ("=="), RELEXP } ;  
RELEXP = EXPRESSION, { (">" | "<") ,EXPRESSION } ;  
EXPRESSION = TERM, { ("+" | "-"), TERM } ;  
TERM = FACTOR, { ("*" | "/"), FACTOR } ;  
FACTOR = (("+" | "-", "!"), FACTOR) | NUMBER | "(", OREXP, ")" | IDENTIFIER | "readln", "(", ")";  
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
TYPE = ( "int" | "string" | "char" )  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;  
STRING = LETTER, {LETTER} ;  
CHAR = LETTER;  
