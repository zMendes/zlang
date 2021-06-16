# zlang 

### Contexto

Linguagem criada para o projeto final da matéria de Lógica da Computação. Foi baseada num compilador criado durante o semestre feito em python.

---
### Características

A sintaxe da linguagem é baseada em C, com algum dos comandos específicos de python como ```print``` e ```input```. Há a presença de loops e condições mas não conta com a implementação de funções. É uma linguagem de tipagem forte que representa o que eu acho que é uma linguagem ideal (*basicamente C*).

---
### Uso

Para rodar um programa, crie seu arquivo com extensão *.zl* e execute:
```bash
python3 compiler.py <nome_do_arquivo.zl>
```

---
### Exemplos 

```c
int main {

    print("Hello world");
    
}
``` 


```c
int main {

    int a = 2;
    int b = 12;
    if (a*b > 10) {
        print(a*b);
    }
    else 
        printf("Menos que 10");
}
``` 

```c
int main {

    for (int i=0; i<10;i++;){
        print(i);
    }
}
``` 
---

#### EBNF

```
BLOCK = "{", { COMMAND }, "}" ;  
COMMAND = ( λ | DECLARATION | ASSIGNMENT | PRINT | BLOCK | CONDITION | WHILE | FOR | INCREMENT | DECREMENT ), ";" ;  
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
FACTOR = (("+" | "-", "!"), FACTOR) | NUMBER | "(", OREXP, ")" | 
INCREMENT = IDENTIFIER, "+", "+", ";" ;
INCREMENT = IDENTIFIER, "-", "-", ";" ;
IDENTIFIER | "input", "(", ")";  
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
TYPE = ( "int" | "string" | "char", "bool" )  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;  
STRING = "'", LETTER, {LETTER}, "'" ;  
CHAR = LETTER;  
BOOLEAN = "true" | "false";
```


### Diagrama Sintático

![Diagrama.](https://i.imgur.com/jmyaEoA.png "Diagrama Sintático.")



![Diagrama.](https://i.imgur.com/cLzLzfX.png "Diagrama Sintático.")


![Diagrama.](https://i.imgur.com/xF8WPVO.png "Diagrama Sintático.")

![Diagrama.](https://i.imgur.com/MvGsWEd.png "Diagrama Sintático.")
