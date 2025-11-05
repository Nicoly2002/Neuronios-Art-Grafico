# Aula Pratica Neuronios Artificiais #
# Nicoly Cristina de J. Laurindo RGM: 2519155 #
# Aula 05/11 #

import matplotlib.pyplot as plt 
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 100)
y = sigmoid(x)

plt.plot(x, y)
plt.title("Curva da Função Sigmoid")
plt.xlabel("z (entrada da função)")
plt.ylabel("g(z) (saída)")
plt.grid(True)
plt.show()