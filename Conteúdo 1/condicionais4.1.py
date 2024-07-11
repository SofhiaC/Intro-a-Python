print("Forneça as coordenadas:")

x = float(input("X:"))
y = float(input("Y:"))

if x and y > 0:
    print(f"A coordenada ({x},{y}) se encontra no primeiro quadrante.")
elif x < 0 and y > 0:
    print(f"A coordenada ({x},{y}) se encontra no segundo quadrante.")
elif x and y < 0:
    print(f"A coordenada ({x},{y}) se encontra no terceiro quadrante.")
elif x > 0 and y < 0:
    print(f"A coordenada ({x},{y}) se encontra no quarto quadrante.")
else: 
    print(f"A coordenada ({x},{y}) se encontra no eixo origem.")