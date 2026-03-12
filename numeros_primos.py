def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

rango_min = 1
rango_max = 250
primos = []

for n in range(rango_min, rango_max + 1):
    if es_primo(n):
        primos.append(n)
        print(f"{n} es primo")

# Guardar en archivo .txt
with open("primos.txt", "w") as archivo:
    archivo.write("Números primos entre 1 y 250:\n")
    for primo in primos:
        archivo.write(f"{primo}\n")
print("\nLos números primos se han guardado en 'primos.txt'")
