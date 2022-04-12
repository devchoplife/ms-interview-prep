"""
You are given a string that represent an expression of digits and operands. 
E.g. 1+2*3, 1-2+4. You need to evaluate the string or the expression. 
NO BODMAS is followed. If the expression is of incorrect syntax return -1. 
Test cases: 
a) 1+2*3 will be evaluated to 9. 
b) 4-2+6*3 will be evaluated to 24. 
c) 1++2 will be evaluated to -1(INVALID). 

Also, in the string spaces can occur. For that case we need to ignore the spaces. 
Like :- 1*2 -1 is equals to 1.
"""

def isOperand(c):
    return (c >= '0' and c <= '9')

def value(c):
    return ord(c) - ord('0')

def evaluate(exp):
    len1 = len(exp)
    
    if len1 == 0:
        return -1
    
    res = value(exp[0])
    
    for i in range(1, len1, 2):
        opr = exp[i]
        opd = exp[i + 1]
        
        if(isOperand(opd) == False):
            return -1
        
        if opr == '+':
            res += value(opd)
        elif opr == '-':
            res -= int(value(opd))
        elif opr == '*':
            res *= int(value(opd))
        elif opr == '/':
            res /= int(value(opd))
        else:
            return -1
        
    return res

expr1 = "1+2*5+3";
res = evaluate(expr1);
print(expr1,"is Invalid") if (res == -1) else print("Value of",expr1,"is",res);
 
expr2 = "1+2*3";
res = evaluate(expr2);
print(expr2,"is Invalid") if (res == -1) else print("Value of",expr2,"is",res);
 
expr3 = "4-2+6*3";
res = evaluate(expr3);
print(expr3,"is Invalid") if (res == -1) else print("Value of",expr3,"is",res);
 
expr4 = "1++2";
res = evaluate(expr4);
print(expr4,"is Invalid") if (res == -1) else print("Value of",expr4,"is",res);
 