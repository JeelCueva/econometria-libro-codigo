#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
CAPÍTULO 2: LEY DE GRANDES NÚMEROS
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=== LEY DE GRANDES NÚMEROS ===\n")

np.random.seed(123)

# Parámetros
mu = 5
sigma = 2
n_max = 10000

# Generar datos
datos = np.random.normal(loc=mu, scale=sigma, size=n_max)

# Calcular media acumulada
media_acumulada = np.cumsum(datos) / np.arange(1, n_max + 1)

# Estadísticas finales
media_final = media_acumulada[-1]
error_abs = abs(media_final - mu)
error_rel = (error_abs / mu) * 100

print(f"Parámetros: μ = {mu}, σ = {sigma}")
print(f"Media final (n = {n_max}): {media_final:.4f}")
print(f"Error absoluto: {error_abs:.4f}")
print(f"Error relativo: {error_rel:.2f}%\n")

# Visualización
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Panel 1: Convergencia
n_vals = np.arange(1, n_max + 1)
axes[0].plot(n_vals, media_acumulada, color='blue', linewidth=0.8)
axes[0].axhline(y=mu, color='red', linestyle='--', linewidth=1.5, label=f'μ = {mu}')
axes[0].set_xlabel('Tamaño de Muestra (n)')
axes[0].set_ylabel('Media Muestral')
axes[0].set_title('Convergencia de la Media Muestral', fontweight='bold')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Panel 2: Velocidad de Convergencia (Escala Log)
desviacion = np.abs(media_acumulada - mu)
axes[1].plot(n_vals, desviacion, color='darkgreen', linewidth=0.8)
axes[1].set_yscale('log')
axes[1].set_xlabel('Tamaño de Muestra (n)')
axes[1].set_ylabel('Desviación Absoluta (escala log)')
axes[1].set_title('Velocidad de Convergencia', fontweight='bold')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('../figuras/convergencia_velocidad_python.pdf', dpi=300, bbox_inches='tight')
print("Gráfico guardado: figuras/convergencia_velocidad_python.pdf")
plt.show()
