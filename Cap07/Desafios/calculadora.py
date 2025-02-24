def calculadora(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        return a / b
    else:
        return "Operación no válida"

print(calculadora(1,1,"+"))
print(calculadora(5,2,"-"))
print(calculadora(4,7,"*"))
print(calculadora(30,3,"/"))
