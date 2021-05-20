# zlang
---
#### EBNF


BLOCK = "{", { COMMAND }, "}" ;  
COMMAND = ( λ | DECLARATION | ASSIGNMENT | PRINT | BLOCK | CONDITION | WHILE | FOR), ";" ;  
ASSIGNMENT = TYPE, IDENTIFIER, "=", ( OREXP | STRING | CHAR | BOOLEAN) ;
DECLARATION = TYPE, IDENTIFIER, { "=", ( OREXP | STRING | CHAR ) } ;  
CONDITION = "IF","(", OREXP, ")", COMMAND, { "ELSE", COMMAND } ;  
WHILE = "while", "(", OREXP, ")", COMMAND ;  
FOR = "for", "(", ASSIGNMENT | DECLARATION,";",CONDITION,";", ASSIGNMENT,";,")", COMMAND ;  
PRINT = "print", "(", (OREXP | STRING | CHAR), ")" ;  
OREXP = ( ANDEXP, { "||", ANDEXP  } ;  
ANDEXP = EQEXP, { "&&", EQEXP } ;  
EQEXP = RELEXP, { ("=="), RELEXP } ;  
RELEXP = EXPRESSION, { (">" | "<") ,EXPRESSION } ;  
EXPRESSION = TERM, { ("+" | "-"), TERM } ;  
TERM = FACTOR, { ("*" | "/"), FACTOR } ;  
FACTOR = (("+" | "-", "!"), FACTOR) | NUMBER | "(", OREXP, ")" | IDENTIFIER | "input", "(", ")";  
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
TYPE = ( "int" | "string" | "char", "bool" )  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;  
STRING = LETTER, {LETTER} ;  
CHAR = LETTER;  
BOOLEAN = "true" | "false";
