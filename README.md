# zlang 

### Contexto

Linguagem criada para o projeto final da matéria de Lógica da Computação. Foi baseada num compilador criado durante o semestre feito em python.

---
### Características

A linguagem é baseada em C, com algum dos comandos específicos de python como ```print``` e ```input```. É uma linguagem de tipagem forte que representa o que eu acho que é uma linguagem ideal. Consistente e com comandos mais simples e intuitivos que as demais linguagens. É feita para pessoas que não tem tanta familiaridade com programação começarem a entender conceitos mais simples, não possui listas, apenas ```string```, ```int``` e ```bool```. 

---
### Uso

Para rodar um programa, crie seu arquivo com extensão *.zl* e execute:
```bash
python3 compiler.py <nome_do_arquivo.zl>
```

---
### Exemplos 


```c
int main() {

	string str = "Hello World";
    output(str);
}
``` 


```c
int main() {
    
    int a = 2;
    int b = 12;
    if (a*b > 10) {
        output(a*b);
    }
    else 
        output("Menos que 10");
}
``` 
```c
int main() {

    for (int i=0; i<10;i++;){
        output(i);
    }
}
``` 

```c

int sum(int a, int b){
    exit a+b;
}

int  main(){
    
    int a =2;
    int b = 5;
    int c;

    c= sum(a, b);
}
```

```c

void print_number(int a){
    output(a);
}

int  main(){
    
    print_number(2);
}
```

---



#### EBNF

```
FUNCDEFBLOCK = { TYPE, IDENTIFIER, "(", { TYPE, IDENTIFIER, "," }, ")", COMMAND } ;
BLOCK = "{", { COMMAND }, "}" ;  
COMMAND = ( λ | DECLARATION | ASSIGNMENT | PRINT | BLOCK | CONDITION | WHILE | FOR | INCREMENT | DECREMENT | "exit", OREXP | IDENTIFIER, "(", { OREXP, "," }, ")" ), ";" ;  
ASSIGNMENT = TYPE, IDENTIFIER, "=", ( OREXP | STRING | CHAR | BOOLEAN) ;
DECLARATION = TYPE, IDENTIFIER, { "=", ( OREXP | STRING | CHAR ) } ;  
CONDITION = "IF","(", OREXP, ")", COMMAND, { "ELSE", COMMAND } ;  
WHILE = "while", "(", OREXP, ")", COMMAND ;  
FOR = "for", "(", ASSIGNMENT | DECLARATION,";",CONDITION,";", ASSIGNMENT,";,")", COMMAND ;  
PRINT = "output", "(", (OREXP | STRING | CHAR), ")" ;  
OREXP = ( ANDEXP, { "||", ANDEXP  } ;  
ANDEXP = EQEXP, { "&&", EQEXP } ;  
EQEXP = RELEXP, { ("=="), RELEXP } ;  
RELEXP = EXPRESSION, { (">" | "<") ,EXPRESSION } ;  
EXPRESSION = TERM, { ("+" | "-"), TERM } ;  
TERM = FACTOR, { ("*" | "/"), FACTOR } ;  
FACTOR = (("+" | "-", "!"), FACTOR) | NUMBER | "(", OREXP, ")" | IDENTIFIER, { "(", { OREXP, "," }, ")" }| "input", "(", ")" ;  
INCREMENT = IDENTIFIER, "+", "+", ";" ;
DECREMENT = IDENTIFIER, "-", "-", ";" ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
TYPE = ( "int" | "string" | "bool" )  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;  
STRING = "'", LETTER, {LETTER}, "'" ;  
CHAR = LETTER;  
BOOLEAN = "true" | "false";
```

---

#### Diagrama Sintático

![Diagrama.](https://i.imgur.com/jmyaEoA.png "Diagrama Sintático.")



![Diagrama.](https://i.imgur.com/cLzLzfX.png "Diagrama Sintático.")


![Diagrama.](https://i.imgur.com/xF8WPVO.png "Diagrama Sintático.")

![Diagrama.](https://i.imgur.com/MvGsWEd.png "Diagrama Sintático.")
