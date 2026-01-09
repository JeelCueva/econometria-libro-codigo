#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
CAPÍTULO 2: PRUEBA DE HIPÓTESIS
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("=== PRUEBA DE HIPÓTESIS (Prueba t) ===\n")

np.random.seed(123)

# Generar datos
n = 25
mu_hipotetico = 100
datos = np.random.normal(105, 15, n)

# Estadísticos muestrales
x_barra = np.mean(datos)
s = np.std(datos, ddof=1)

print("--- Datos ---")
print(f"Tamaño de muestra: n = {n}")
print(f"Media muestral: X̄ = {x_barra:.2f}")
print(f"Desviación estándar: s = {s:.2f}\n")

# Hipótesis
print("--- Hipótesis ---")
print(f"H₀: μ = {mu_hipotetico}")
print(f"H₁: μ ≠ {mu_hipotetico} (bilateral)")
print("Nivel de significancia: α = 0.05\n")

# Estadístico t
t_stat = (x_barra - mu_hipotetico) / (s / np.sqrt(n))
df = n - 1
t_critico = stats.t.ppf(0.975, df)
p_valor = 2 * stats.t.sf(abs(t_stat), df)

print("--- Resultados ---")
print(f"Estadístico t = {t_stat:.3f}")
print(f"Grados de libertad = {df}")
print(f"Valor crítico t₀.₀₂₅ = {t_critico:.3f}")
print(f"P-valor = {p_valor:.4f}\n")

# Decisión
if abs(t_stat) > t_critico:
    print("Decisión: RECHAZAR H₀ (|t| > t_crítico)")
else:
    print("Decisión: NO RECHAZAR H₀ (|t| ≤ t_crítico)")

if p_valor < 0.05:
    print("Conclusión: Hay evidencia significativa contra H₀\n")
else:
    print("Conclusión: No hay evidencia suficiente para rechazar H₀\n")

# Intervalo de confianza
ic_lower = x_barra - t_critico * (s / np.sqrt(n))
ic_upper = x_barra + t_critico * (s / np.sqrt(n))

print("--- Intervalo de Confianza 95% ---")
print(f"IC: [{ic_lower:.2f}, {ic_upper:.2f}]")
contiene = mu_hipotetico >= ic_lower and mu_hipotetico <= ic_upper
print(f"¿Contiene μ₀ = {mu_hipotetico}? {'SÍ' if contiene else 'NO'}\n")

# Visualización
t_seq = np.linspace(-4, 4, 500)
dt_vals = stats.t.pdf(t_seq, df)

plt.figure(figsize=(10, 6))
plt.plot(t_seq, dt_vals, 'b-', linewidth=2, label='Distribución t')
plt.fill_between(t_seq[t_seq < -t_critico], 0, stats.t.pdf(t_seq[t_seq < -t_critico], df), 
                 alpha=0.3, color='red', label='Región de rechazo')
plt.fill_between(t_seq[t_seq > t_critico], 0, stats.t.pdf(t_seq[t_seq > t_critico], df), 
                 alpha=0.3, color='red')
plt.axvline(t_stat, color='darkgreen', linestyle='--', linewidth=2, label=f't = {t_stat:.2f}')
plt.xlabel('Estadístico t')
plt.ylabel('Densidad')
plt.title('Distribución t y Regiones de Rechazo', fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../figuras/prueba_t_ic_python.pdf', dpi=300, bbox_inches='tight')
print("Gráfico guardado: figuras/prueba_t_ic_python.pdf")
plt.show()
