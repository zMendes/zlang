#!/usr/bin/python

import sys
from abc import ABCMeta, abstractmethod
import copy


class SymbolTable:

    def __init__(self):
        self.table = dict()
    
    def setType(self, var, type):
        if var in self.table:
            raise ValueError("Redeclaration of same variable is not allowed.")
        self.table[var] = (None, type)
    
    def setVar(self, var, value):
        self.table[var] = value     

    def getVar(self, var):
        return self.table[var]


sb = SymbolTable()


class Node(metaclass=ABCMeta):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def value():
        pass

    @property
    @abstractmethod
    def children():
        pass

    @abstractmethod
    def Evaluate(self):
        pass


class BSt(Node):
    children = list
    value = int

    def __init__(self):
        self.children = []

    def Evaluate(self):
        for child in self.children:
            child.Evaluate()


class BinOp(Node):

    children = list
    value = int

    def __init__(self, value):
        self.value = value
        self.children = [None] * 2

    def Evaluate(self):

        

        if self.value == "ATTRIB":
            try:
                expected_type = sb.getVar(self.children[0].value)[1]
            except:
                raise ValueError("Variable not declared.")
            a = self.children[1].Evaluate()

            if expected_type == bool and a[0]>1:
                sb.setVar(self.children[0].value, (True, bool))
            elif expected_type == bool and a[0]<0:
                sb.setVar(self.children[0].value, (False, bool))
            elif expected_type == int and a[0] == True:
                sb.setVar(self.children[0].value, (1, int))
            elif expected_type == int and a[0] == False:
                sb.setVar(self.children[0].value, (0, int))
            elif expected_type == str and a[1] != str or expected_type != str and a[1] == str:
                raise ValueError("Type mismatch.")
            else:
                sb.setVar(self.children[0].value, a)
            return 

        a = self.children[0].Evaluate()
        b = self.children[1].Evaluate()

        if self.value == "DECL_ATTRIB":
            return

        if self.value == "EQUAL":
            return (True, bool)  if a[0] == b[0] else (False, bool)

        if a[1] == str or b[1] == str:
            raise ValueError("Can't resolve arithmetic operation with string.")
        elif a[1] == int or b[1] == int:
            type = int
        else:
            type = bool
        
        if self.value == "PLUS":
            return (a[0] + b[0], type)

        elif self.value == "SUB":
            return (a[0] - b[0], type)

        elif self.value == "MULTI":
            return (a[0] * b[0], type)

        elif self.value == "DIV":
            return (int(a[0] / b[0]), type)

        elif self.value == "BIGGER":
            return (True, bool)  if a[0] > b[0] else (False, bool) 

        elif self.value == "LESS":
            return (True, bool)  if a[0] < b[0] else (False, bool)  

        elif self.value == "AND":
            return (True, bool)  if a[0] and b[0] else (False, bool) 

        elif self.value == "OR":
            if a[0] or b[0]:
                return (True, bool)
            else:
                return (False, bool)
            print("RETURNING DA OR: ", a[0] or b[0])
            #return ("true", bool)  if a[0] or b[0] else ("false", bool) 

class UnOp(Node):

    children = list
    value = int

    def __init__(self, value):
        self.value = value
        self.children = [None]

    def Evaluate(self):
        if self.value == "DECLARATION":
            sb.setType(self.children[0][0],self.children[0][1])
            return 
        result = self.children[0].Evaluate()
        if self.value == "PLUS":
            return (result[0], result[1])
        elif self.value == "SUB":
            return (-result[0], result[1])
        elif self.value == "NOT":
            return (not result[0], result[1])



class IntVal(Node):

    children = list
    value = int

    def __init__(self, value):
        self.value = value
        self.children = []

    def Evaluate(self):
        return (self.value, int)
class BoolVal(Node):

    children = list
    value = int

    def __init__(self, value):
        self.value = value
        self.children = []

    def Evaluate(self):
        value = True if self.value == "true" else False
        return (value, bool)

class StrVal(Node):

    children = list
    value = int

    def __init__(self, value):
        self.value = value
        self.children = []

    def Evaluate(self):
        return (self.value, str)


class Print(Node):
    children = list
    value = int

    def __init__(self):
        self.children = [None]

    def Evaluate(self):
        print(self.children[0].Evaluate()[0])



class Input(Node):
    children = list
    value = int

    def __init__(self):
        self.children = []

    def Evaluate(self):
        return (int(input()), int)

class While_loop(Node):

    children = list
    value = int

    def __init__(self):
        self.children = [None, None]

    def Evaluate(self):
        while(self.children[0].Evaluate()[0]):
            self.children[1].Evaluate()

class For_loop(Node):

    children = list
    value = int

    def __init__(self):
        self.children = [None, None, None, None]

    def Evaluate(self):
        self.children[0].Evaluate()
        while(self.children[1].Evaluate()[0]):
            self.children[3].Evaluate()
            self.children[2].Evaluate()

class Condition(Node):

    children = list
    value = int 

    def __init__(self):
        self.children = [None, None, None]
    
    def Evaluate(self):
        condition  = self.children[0].Evaluate()
        if condition[1] == str:
            raise ValueError("Can't use type string as condition.") 
        if condition[0]:
            self.children[1].Evaluate()
        elif self.children[2] != None:
            self.children[2].Evaluate()

class Variable(Node):

    children = list
    value = int

    def __init__(self, value):
        self.value = value
        self.children = []

    def Evaluate(self):
        return sb.getVar(self.value)


class NoOp(Node):

    children = list
    value = int

    def __init__(self):
        self.children = []

    def Evaluate(self):
        pass


class Token:

    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value


class PrePro:

    def filter(self, text):

        # Implemnentação baseada a partir do código abaixo:
        # https://www.geeksforgeeks.org/remove-comments-given-cc-program/
        isComment = False

        filteredText = ""
        i = 0
        while (i < len(text)):
            if isComment and text[i] == "*" and text[i+1] == "/":
                isComment = False
                i += 1
            elif text[i] == "/" and text[i+1] == "*":
                isComment = True
                i += 1
            elif isComment:
                i += 1
                continue
            else:
                filteredText += text[i]
            i += 1

        if isComment:
            raise KeyError
        return filteredText


class Tokenizer:

    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual
        self.invalid = ["(", ")", "/", "*", "-", "+", "=", ";", " ", ">", "<", "|", "&", "{", "}"]

    def selectNext(self):

        self.position += 1
        if self.position >= len(self.origin):
            self.actual = Token("EOF", None)
            return
        if self.origin[self.position] == "n":
            print("ENTREI NO PULA O N ")
            self.selectNext()
        elif self.origin[self.position].isnumeric():
            number = ""
            while self.position < len(self.origin) and self.origin[self.position].isnumeric():
                number += self.origin[self.position]
                self.position += 1
            self.actual = Token("INT", int(number))
            self.position -= 1

        elif self.origin[self.position] == "+":
            self.actual = Token("PLUS", None)

        elif self.origin[self.position] == "-":
            self.actual = Token("SUB", None)

        elif self.origin[self.position] == "*":
            self.actual = Token("MULTI", None)

        elif self.origin[self.position] == "/":
            self.actual = Token("DIV", None)

        elif self.origin[self.position] == "{":
            self.actual = Token("BRACE_OPEN", None)
        
        elif self.origin[self.position] == "}":
            self.actual = Token("BRACE_CLOSE", None)

        elif self.origin[self.position] == "(":
            self.actual = Token("BRACKET_OPEN", None)

        elif self.origin[self.position] == ")":
            self.actual = Token("BRACKET_CLOSE", None)

        elif self.origin[self.position:self.position+2] == "||":
            self.position+=1
            self.actual = Token("OR", None)

        elif self.origin[self.position:self.position+2] == "&&":
            self.position+=1
            self.actual = Token("AND", None)

        elif self.origin[self.position] == "=":
            if self.origin[self.position+1] == "=":
                self.actual = Token("EQUAL", None)
                self.position+=1
            else:
                self.actual = Token("ATTRIB", None)

        elif self.origin[self.position] == ">":
            self.actual = Token("BIGGER", None)

        elif self.origin[self.position] == "<":
            self.actual = Token("LESS", None)

        elif self.origin[self.position] == "!":
            self.actual = Token("NOT", None)

        elif self.origin[self.position] == ";":
            self.actual = Token("SEMICOLON", None)
        
        elif self.origin[self.position] == '"':
            self.position += 1
            string = ""
            while self.origin[self.position] != '"':
                string+= self.origin[self.position]
                self.position += 1 
                if self.position >= len(self.origin):
                    raise ValueError('Missing closing " in reference. ')
            self.actual = Token("STRING", string)
            #self.position -=1

        elif self.origin[self.position] != " ":
            identifier = ""

            while self.position < len(self.origin) and self.origin[self.position] not in self.invalid:
                identifier += self.origin[self.position]
                self.position += 1
            self.position -= 1
            if (identifier == "print"):
                self.actual = Token("PRINT", None)
            elif (identifier == "input"):
                self.actual = Token("INPUT", None)
            elif (identifier == "while"):
                self.actual = Token("WHILE_LOOP", None)
            elif (identifier == "for"):
                self.actual = Token("FOR_LOOP", None)
            elif (identifier == "if"):
                 self.actual = Token("IF", None)
            elif (identifier == "else"):
                 self.actual = Token("ELSE", None)
            elif (identifier == "string" or identifier == "int" or identifier == "bool"):
                self.actual = Token("DECLARATION", identifier)
            elif (identifier == "true" or identifier == "false"):
                self.actual = Token("BOOL", identifier)
            else:
                self.actual = Token("IDENTIFIER", identifier)

        else:
            self.selectNext()


class Parser:

    def parseBlock(self):
        if self.tokens.actual.type_ != "BRACE_OPEN":
            raise ValueError("Missing '{' in reference.")
        self.tokens.selectNext()        

        head = BSt()

        while self.tokens.actual.type_ != "BRACE_CLOSE":
            head.children.append(self.parseCommand())

        if self.tokens.actual.type_ != "BRACE_CLOSE":
            raise ValueError("Missing '{' in reference.")
        self.tokens.selectNext()
        
        return head

    def parseCommand(self):


        if self.tokens.actual.type_ == "IDENTIFIER":
            identifier = self.tokens.actual.value
            self.tokens.selectNext()
            if self.tokens.actual.type_ != "ATTRIB":
                raise ValueError("Missing '=' in reference.")
            self.tokens.selectNext()
            tree = BinOp("ATTRIB")
            tree.children[0] = Variable(identifier)
            tree.children[1] = self.parseOrExpression()
        
        elif self.tokens.actual.type_ == "DECLARATION":
            tree = UnOp("DECLARATION")
            declarationType = self.tokens.actual.value
            self.tokens.selectNext()
            if self.tokens.actual.type_ != "IDENTIFIER":
                raise ValueError("Expecting a variable. Received: ", self.tokens.actual.type_)
            
            identifier = self.tokens.actual.value
            
            if declarationType  == "string":
                tree.children[0] =  (identifier, str)
            elif declarationType == "int":
                tree.children[0] = (identifier, int)
            elif declarationType == "bool":
                tree.children[0] = (identifier, bool)
            else:
                raise ValueError("Type not recognized.")
            self.tokens.selectNext()
            if self.tokens.actual.type_ == "ATTRIB":
                self.tokens.selectNext()
                aux = copy.deepcopy(tree)
                tree = BinOp("DECL_ATTRIB")
                attrib = BinOp("ATTRIB")
                attrib.children[0] = Variable(identifier)
                attrib.children[1] = self.parseOrExpression()

                tree.children[0] = aux
                tree.children[1] = attrib
                



        elif self.tokens.actual.type_ == "PRINT":
            tree = Print()
            self.tokens.selectNext()
            if self.tokens.actual.type_ != "BRACKET_OPEN":
                raise ValueError("Missing '(' in reference.")
            self.tokens.selectNext()
            exp = self.parseOrExpression()
            tree.children[0] = exp
            if self.tokens.actual.type_ != "BRACKET_CLOSE":
                raise ValueError("Missing ')' in reference.")
            self.tokens.selectNext()
        
        elif self.tokens.actual.type_ == "WHILE_LOOP":
            self.tokens.selectNext()
            if self.tokens.actual.type_ != "BRACKET_OPEN":
                raise ValueError("Missing '(' for while loop.")
            self.tokens.selectNext()

            tree = While_loop()
            tree.children[0] = self.parseOrExpression()
            if self.tokens.actual.type_ != "BRACKET_CLOSE":
                raise ValueError("Missing ')' for while loop.")
            self.tokens.selectNext()
            tree.children[1] = self.parseCommand()
            return tree
        elif self.tokens.actual.type_ == "FOR_LOOP":
            self.tokens.selectNext()
            if self.tokens.actual.type_ != "BRACKET_OPEN":
                raise ValueError("Missing '(' for while loop.")
            self.tokens.selectNext()

            tree = For_loop()
            tree.children[0] = self.parseCommand()
            tree.children[1] = self.parseOrExpression()
            if self.tokens.actual.type_ != "SEMICOLON":
                raise ValueError("Missing ';'in reference.")
            self.tokens.selectNext()
            tree.children[2] = self.parseCommand()
            if self.tokens.actual.type_ != "BRACKET_CLOSE":
                self.tokens.selectNext()
                raise ValueError("Missing ')'in reference.")
            self.tokens.selectNext()
            tree.children[3] = self.parseCommand()

            return tree

        elif self.tokens.actual.type_ == "IF":
            self.tokens.selectNext()
            if self.tokens.actual.type_ != "BRACKET_OPEN":
                raise ValueError("Missing '(' for while loop.")
            self.tokens.selectNext()

            tree = Condition()
            tree.children[0] = self.parseOrExpression()
            if self.tokens.actual.type_ != "BRACKET_CLOSE":
                raise ValueError("Missing ')' for while loop.")
            self.tokens.selectNext()
            tree.children[1] = self.parseCommand()
            if self.tokens.actual.type_ == "ELSE":
                self.tokens.selectNext()
                tree.children[2] = self.parseCommand()
            return tree
        elif self.tokens.actual.type_ == "SEMICOLON":
            self.tokens.selectNext()
            tree = NoOp();
            return tree


        else:
            tree = self.parseBlock()
            return tree

        if self.tokens.actual.type_ != "SEMICOLON":
            raise ValueError("Missing ';' in reference.")

        self.tokens.selectNext()

        return tree

    def parseOrExpression(self):

        tree = self.parseAndExpression()

        while self.tokens.actual.type_ == "OR":
            self.tokens.selectNext()
            aux = BinOp("OR")
            aux.children[0] = copy.deepcopy(tree)
            aux.children[1] = self.parseAndExpression()
            tree = copy.deepcopy(aux)

        return tree

    def parseAndExpression(self):

        tree = self.parseEqualExpression()

        while self.tokens.actual.type_ == "AND":
            self.tokens.selectNext()
            aux = BinOp("AND")
            aux.children[0] = copy.deepcopy(tree)
            aux.children[1] = self.parseEqualExpression()
            tree = copy.deepcopy(aux)

        return tree

    def parseEqualExpression(self):

        tree = self.parseRelativeExpression()

        while self.tokens.actual.type_ == "EQUAL":
            self.tokens.selectNext()
            aux = BinOp("EQUAL")
            aux.children[0] = copy.deepcopy(tree)
            aux.children[1] = self.parseRelativeExpression()
            tree = copy.deepcopy(aux)

        return tree

    def parseRelativeExpression(self):

        tree = self.parseExpression()

        while self.tokens.actual.type_ == "BIGGER" or self.tokens.actual.type_ == "LESS":
            if self.tokens.actual.type_ == "BIGGER":
                self.tokens.selectNext()
                aux = BinOp("BIGGER")
                aux.children[0] = copy.deepcopy(tree)
                aux.children[1] = self.parseExpression()
                tree = copy.deepcopy(aux)

            elif self.tokens.actual.type_ == "LESS":
                self.tokens.selectNext()
                aux = BinOp("LESS")
                aux.children[0] = copy.deepcopy(tree)
                aux.children[1] = self.parseExpression()
                tree = copy.deepcopy(aux)

        return tree

    def parseExpression(self):

        tree = self.parseTerm()

        while self.tokens.actual.type_ == "PLUS" or self.tokens.actual.type_ == "SUB":

            if self.tokens.actual.type_ == "PLUS":
                self.tokens.selectNext()
                aux = BinOp("PLUS")
                aux.children[0] = copy.deepcopy(tree)
                aux.children[1] = self.parseTerm()
                tree = copy.deepcopy(aux)

            if self.tokens.actual.type_ == "SUB":
                self.tokens.selectNext()
                aux = BinOp("SUB")
                aux.children[0] = copy.deepcopy(tree)
                aux.children[1] = self.parseTerm()
                tree = copy.deepcopy(aux)

        return tree

    def parseTerm(self):

        tree = self.parseFactor()

        if self.tokens.actual.type_ == "INT":
            raise ValueError

        while self.tokens.actual.type_ == "MULTI" or self.tokens.actual.type_ == "DIV":

            if self.tokens.actual.type_ == "MULTI":
                self.tokens.selectNext()
                aux = BinOp("MULTI")
                aux.children[0] = copy.deepcopy(tree)
                aux.children[1] = self.parseFactor()
                tree = copy.deepcopy(aux)

            if self.tokens.actual.type_ == "DIV":
                self.tokens.selectNext()
                aux = BinOp("DIV")
                aux.children[0] = copy.deepcopy(tree)
                aux.children[1] = self.parseFactor()
                tree = copy.deepcopy(aux)

            if self.tokens.actual.type_ == "INT":
                raise ValueError

        return tree

    def parseFactor(self):

        if self.tokens.actual.type_ == "INT":
            tree = IntVal(self.tokens.actual.value)
            self.tokens.selectNext()
        elif self.tokens.actual.type_ == "STRING":
            tree = StrVal(self.tokens.actual.value)
            self.tokens.selectNext()
        
        elif self.tokens.actual.type_ == "BOOL":
            tree = BoolVal(self.tokens.actual.value)
            self.tokens.selectNext()

        elif self.tokens.actual.type_ == "PLUS":
            self.tokens.selectNext()
            tree = UnOp("PLUS")
            tree.children[0] = self.parseFactor(    )

        elif self.tokens.actual.type_ == "SUB":
            self.tokens.selectNext()
            tree = UnOp("SUB")
            tree.children[0] = self.parseFactor()

        elif self.tokens.actual.type_ == "NOT":
            self.tokens.selectNext()
            tree = UnOp("NOT")
            tree.children[0] = self.parseFactor()

        elif self.tokens.actual.type_ == "BRACKET_OPEN":
            self.tokens.selectNext()
            tree = self.parseOrExpression()
            if self.tokens.actual.type_ != "BRACKET_CLOSE":
                raise ValueError
            self.tokens.selectNext()

        elif self.tokens.actual.type_ == "IDENTIFIER":
            tree = Variable(self.tokens.actual.value)
            self.tokens.selectNext()

        elif self.tokens.actual.type_ == "INPUT":
            self.tokens.selectNext()
            if self.tokens.actual.type_ == "BRACKET_OPEN":
                self.tokens.selectNext()
                if self.tokens.actual.type_ == "BRACKET_CLOSE":
                    self.tokens.selectNext()
                    tree = Input()

                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

        return tree

    def run(self, code):
        prepro = PrePro()
        filtered = prepro.filter("".join(code).replace("\n", "").replace("\t",""))
        self.tokens = Tokenizer(filtered, -1, None)
        self.tokens.selectNext()
        result = self.parseBlock()
        result.Evaluate()


if __name__ == "__main__":
    parser = Parser()
    file_name = " ".join(sys.argv[1:])
    file = open(file_name, 'r')
    content = file.readlines()
    parser.run(content)
