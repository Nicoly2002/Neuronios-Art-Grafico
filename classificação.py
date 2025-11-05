# Aula Pratica Neuronios Artificiais #
# Nicoly Cristina de J. Laurindo RGM: 2519155 #
# Aula 29/10 #

import numpy as np
# Entradas e pesos
x1, x2 = 0.5, 0.9
w1, w2 = 0.4, 0.7
b = 0.1

# Soma ponderada
z = (x1 * w1) + (x2 * w2) + b
print(f"Soma ponderada (z): {z:.3f}")

# Função sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

y = sigmoid(z)
print(f"Saída após função sigmoid: {y:.3f}")