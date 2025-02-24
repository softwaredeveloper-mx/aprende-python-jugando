def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

gradosCent = float(input("Convertir grados centígrados a fahrenheit. Dame los grados centígrados: "))
gradosFah = celsius_a_fahrenheit(gradosCent)
print(f"{gradosCent} centigrados equivale a {gradosFah} Farenheit")   

gradosFah = float(input("Convertir grados fahrenheit a centígrados. Dame los grados fahrenheit: "))
gradosCent = fahrenheit_a_celsius(gradosFah)
print(f"{gradosFah} Fahrenheit equivale a {gradosCent} Celcius")
