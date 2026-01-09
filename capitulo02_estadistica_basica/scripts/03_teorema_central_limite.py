#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
CAPÍTULO 2: TEOREMA CENTRAL DEL LÍMITE
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("=== TEOREMA CENTRAL DEL LÍMITE ===\n")

np.random.seed(123)

# Parámetros
n_muestra = 30
m_replicas = 1000

# Distribución 1: Uniforme(0, 10)
print("--- Distribución Uniforme(0, 10) ---")
medias_unif = [np.mean(np.random.uniform(0, 10, n_muestra)) for _ in range(m_replicas)]
z_unif = np.sqrt(n_muestra) * (np.array(medias_unif) - 5) / np.sqrt(100/12)
shapiro_unif = stats.shapiro(z_unif)
print(f"Shapiro-Wilk: W = {shapiro_unif.statistic:.4f}, p-valor = {shapiro_unif.pvalue:.4f}\n")

# Distribución 2: Exponencial(λ=1)
print("--- Distribución Exponencial(λ=1) ---")
medias_exp = [np.mean(np.random.exponential(scale=1, size=n_muestra)) for _ in range(m_replicas)]
z_exp = np.sqrt(n_muestra) * (np.array(medias_exp) - 1) / 1
shapiro_exp = stats.shapiro(z_exp)
print(f"Shapiro-Wilk: W = {shapiro_exp.statistic:.4f}, p-valor = {shapiro_exp.pvalue:.4f}\n")

# Distribución 3: Binomial(n=10, p=0.5)
print("--- Distribución Binomial(n=10, p=0.5) ---")
medias_binom = [np.mean(np.random.binomial(10, 0.5, n_muestra)) for _ in range(m_replicas)]
z_binom = np.sqrt(n_muestra) * (np.array(medias_binom) - 5) / np.sqrt(2.5)
shapiro_binom = stats.shapiro(z_binom)
print(f"Shapiro-Wilk: W = {shapiro_binom.statistic:.4f}, p-valor = {shapiro_binom.pvalue:.4f}\n")

# Distribución 4: Chi-cuadrado(df=3)
print("--- Distribución Chi-cuadrado(df=3) ---")
medias_chisq = [np.mean(np.random.chisquare(3, n_muestra)) for _ in range(m_replicas)]
z_chisq = np.sqrt(n_muestra) * (np.array(medias_chisq) - 3) / np.sqrt(6)
shapiro_chisq = stats.shapiro(z_chisq)
print(f"Shapiro-Wilk: W = {shapiro_chisq.statistic:.4f}, p-valor = {shapiro_chisq.pvalue:.4f}\n")

# Visualización
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

distribuciones = [
    (z_unif, 'Uniforme', axes[0, 0]),
    (z_exp, 'Exponencial', axes[0, 1]),
    (z_binom, 'Binomial', axes[1, 0]),
    (z_chisq, 'Chi-cuadrado', axes[1, 1])
]

for z_data, nombre, ax in distribuciones:
    ax.hist(z_data, bins=30, density=True, alpha=0.7, 
            color='lightblue', edgecolor='black', label='Histograma')
    x = np.linspace(-4, 4, 100)
    ax.plot(x, stats.norm.pdf(x), 'r-', linewidth=2, label='N(0,1)')
    ax.set_xlabel('Z estandarizada')
    ax.set_ylabel('Densidad')
    ax.set_title(f'Distribución {nombre}', fontweight='bold')
    ax.legend()
    ax.grid(alpha=0.3)

plt.suptitle('Teorema Central del Límite: Normalidad Asintótica', 
             fontsize=14, fontweight='bold', y=1.00)
plt.tight_layout()
plt.savefig('../figuras/tcl_normalidad_python.pdf', dpi=300, bbox_inches='tight')
print("Gráfico guardado: figuras/tcl_normalidad_python.pdf")
plt.show()
