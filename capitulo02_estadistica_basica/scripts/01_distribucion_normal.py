#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
CAPÍTULO 2: DISTRIBUCIÓN NORMAL ESTÁNDAR
==============================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("=== DISTRIBUCIÓN NORMAL ESTÁNDAR ===\n")

# Semilla para reproducibilidad
np.random.seed(123)

# Generar muestra
n = 1000
muestra = np.random.normal(loc=0, scale=1, size=n)

# Estadísticas descriptivas
media_muestral = np.mean(muestra)
sd_muestral = np.std(muestra, ddof=1)
asimetria = stats.skew(muestra)
curtosis = stats.kurtosis(muestra, fisher=False)

print("--- Estadísticas Descriptivas ---")
print(f"Media muestral: {media_muestral:.4f}")
print(f"Desviación estándar: {sd_muestral:.4f}")
print(f"Asimetría: {asimetria:.4f}")
print(f"Curtosis: {curtosis:.4f}\n")

# Prueba de normalidad
shapiro_stat, shapiro_p = stats.shapiro(muestra)
print("--- Prueba de Normalidad (Shapiro-Wilk) ---")
print(f"Estadístico W: {shapiro_stat:.4f}")
print(f"P-valor: {shapiro_p:.4f}")
if shapiro_p > 0.05:
    print("Conclusión: NO rechazamos H₀ → Muestra consistente con normalidad\n")
else:
    print("Conclusión: Rechazamos H₀ → Muestra NO es normal\n")

# Probabilidades
prob_196 = stats.norm.cdf(1.96)
prob_intervalo = stats.norm.cdf(1.96) - stats.norm.cdf(-1.96)

print("--- Probabilidades ---")
print(f"P(Z ≤ 1.96) = {prob_196:.4f}")
print(f"P(-1.96 ≤ Z ≤ 1.96) = {prob_intervalo:.4f}\n")

# Cuantiles
q_025 = stats.norm.ppf(0.025)
q_975 = stats.norm.ppf(0.975)
print(f"Cuantil 2.5%: {q_025:.4f}")
print(f"Cuantil 97.5%: {q_975:.4f}\n")

# Visualizaciones
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Panel 1: Histograma vs Densidad Teórica
axes[0].hist(muestra, bins=30, density=True, alpha=0.7, 
             color='lightblue', edgecolor='black', label='Histograma')
x = np.linspace(-4, 4, 100)
axes[0].plot(x, stats.norm.pdf(x), 'r-', linewidth=2, label='N(0,1) Teórica')
axes[0].set_xlabel('Valores')
axes[0].set_ylabel('Densidad')
axes[0].set_title('Histograma vs. Densidad Teórica', fontweight='bold')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Panel 2: Q-Q Plot
stats.probplot(muestra, dist="norm", plot=axes[1])
axes[1].set_title('Q-Q Plot Normal', fontweight='bold')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('../figuras/histograma_vs_densidad_qq_python.pdf', dpi=300, bbox_inches='tight')
print("Gráfico guardado: figuras/histograma_vs_densidad_qq_python.pdf")
plt.show()
