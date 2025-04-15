#Questão 1 

import numpy as np
import matplotlib.pyplot as plt

# constantes 
R = 8.314  
Tc = 304.2  
Pc = 7383000.0  # pa (se converter 73,83e5)

# F para K
T_fahrenheit = 41
T = (T_fahrenheit - 32) * 5/9 + 273.15 

# calculo a e b
a = (27 * R**2 * Tc**2) / (64 * Pc)
b = (R * Tc) / (8 * Pc)

# volume molar 
V = np.linspace(1e-4, 0.5, 1000)  # intervalo de 1e-4 a 0.5 

# equação de Van der Waals
P = (R * T) / (V - b) - a / V**2

# plotando o grafico
plt.figure(figsize=(10, 4))
plt.plot(V, P, label=f'T = {T:.2f} K (41°F)', color='black')
plt.xlabel('Volume molar (m³/mol)')
plt.ylabel('Pressão (Pa)')
plt.title('Equação de Van der Waals')
plt.grid(True)
plt.legend()
plt.show()