# ============================================
# Modulo 1: Validacion de Distribucion Normal
# ============================================

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Configuracion
np.random.seed(123)
n = 1000

# Generar datos N(0,1)
x = np.random.normal(loc=0, scale=1, size=n)

# Estadisticas descriptivas
estadisticas = pd.DataFrame({
    'Estadistico': ['Media', 'Desv.Est.', 'Asimetria', 'Curtosis'],
    'Valor': [
        np.mean(x),
        np.std(x, ddof=1),
        stats.skew(x),
        stats.kurtosis(x, fisher=False)
    ],
    'Teorico': [0, 1, 0, 3]
})

print(estadisticas)

# Prueba de normalidad Shapiro-Wilk
w_stat, p_value = stats.shapiro(x)
print(f"\nShapiro-Wilk Test:")
print(f"W = {w_stat:.4f}")
print(f"p-value = {p_value:.4f}")

# Probabilidades y cuantiles
prob_menor_196 = stats.norm.cdf(1.96)
prob_entre_196 = stats.norm.cdf(1.96) - stats.norm.cdf(-1.96)
q_025 = stats.norm.ppf(0.025)
q_975 = stats.norm.ppf(0.975)

print(f"\nProbabilidades y Cuantiles:")
print(f"P(Z <= 1.96) = {prob_menor_196:.4f}")
print(f"P(-1.96 <= Z <= 1.96) = {prob_entre_196:.4f}")
print(f"Cuantil 2.5% = {q_025:.4f}")
print(f"Cuantil 97.5% = {q_975:.4f}")

# Visualizacion
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Figura 1: Histograma vs densidad teorica
axes[0].hist(x, bins=30, density=True, alpha=0.7, 
             color='lightblue', edgecolor='black')
x_range = np.linspace(-4, 4, 100)
axes[0].plot(x_range, stats.norm.pdf(x_range, 0, 1), 
             'r-', linewidth=2, label='Densidad N(0,1)')
axes[0].set_xlabel('Valor')
axes[0].set_ylabel('Densidad')
axes[0].set_title('Histograma vs Densidad Teorica N(0,1)')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Figura 2: Q-Q plot
stats.probplot(x, dist="norm", plot=axes[1])
axes[1].set_title('Grafico Q-Q Normal')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
