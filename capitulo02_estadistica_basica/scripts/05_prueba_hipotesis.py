#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
CAPÍTULO 2: PRUEBA DE HIPÓTESIS
==============================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

print("="*70)
print("PRUEBA T PARA LA MEDIA (VISUALIZACIÓN PROFESIONAL)")
print("="*70)

# Parámetros del experimento
np.random.seed(20231115)  # Semilla para reproducibilidad exacta
mu_0 = 100         # H0: μ = 100
mu_real = 103      # Media poblacional real (para generar datos)
sigma_real = 15    # Desviación poblacional
n = 25             # Tamaño muestral
alpha = 0.05       # Nivel de significancia

print(f"\nDiseño del experimento:")
print(f"  H0: μ = {mu_0}")
print(f"  H1: μ ≠ {mu_0} (prueba bilateral)")
print(f"  Nivel de significancia α = {alpha}")
print(f"  Tamaño muestral n = {n}\n")

# Generar datos
X = np.random.normal(loc=mu_real, scale=sigma_real, size=n)

# Estadísticos muestrales
x_bar = np.mean(X)
s = np.std(X, ddof=1)  # Desviación estándar muestral (corregida)
se = s / np.sqrt(n)    # Error estándar

print("Estadísticos muestrales:")
print(f"  Media muestral (X̄) = {x_bar:.2f}")
print(f"  Desviación estándar (S) = {s:.2f}")
print(f"  Error estándar (S/√n) = {se:.2f}\n")

# ==============================================================
# PRUEBA T
# ==============================================================

gl = n - 1  # Grados de libertad
t_obs = (x_bar - mu_0) / se  # Estadístico t
t_crit = stats.t.ppf(1 - alpha/2, df=gl)  # Valor crítico bilateral
p_valor = 2 * (1 - stats.t.cdf(abs(t_obs), df=gl))  # p-valor bilateral

# Intervalo de confianza 95%
ic_95 = x_bar + np.array([-1, 1]) * stats.t.ppf(0.975, df=gl) * se

print("=== RESULTADOS DE LA PRUEBA T ===")
print(f"  Grados de libertad = {gl}")
print(f"  Estadístico t = {t_obs:.3f}")
print(f"  Valor crítico = ±{t_crit:.3f}")
print(f"  p-valor = {p_valor:.4f}\n")

print(f"  IC 95% = [{ic_95[0]:.2f}, {ic_95[1]:.2f}]")
print(f"  ¿Contiene μ0={mu_0}? {'✓ SÍ' if ic_95[0] <= mu_0 <= ic_95[1] else '✗ NO'}\n")

print("=== DECISIÓN ===")
if p_valor < alpha:
    print(f"  ✗ RECHAZAR H0 al nivel {alpha}")
else:
    print(f"  ✓ NO RECHAZAR H0 al nivel {alpha}")
print()

# ==============================================================
# VISUALIZACIÓN PROFESIONAL
# ==============================================================

print("=== GENERANDO GRÁFICO PROFESIONAL ===")

# Paleta de colores corporativa
COL_REGION_CRITICA = "#e41a1c"  # Rojo intenso
COL_T_OBS = "#377eb8"           # Azul profesional
COL_NORMAL = "#2c2c2c"          # Negro suave
COL_TEXT = "#333333"            # Gris oscuro para texto
COL_FONDO = "white"             # Fondo blanco puro
COL_SOMBRA = "#ffcccc"          # Rojo claro para área p-valor

# Secuencia para densidad t
x_t = np.linspace(-4, 4, 500)
y_t = stats.t.pdf(x_t, df=gl)

# Data frames para regiones
df_plot = pd.DataFrame({'t': x_t, 'densidad': y_t})
df_crit_left = pd.DataFrame({
    't': np.linspace(-4, -t_crit, 100),
    'densidad': stats.t.pdf(np.linspace(-4, -t_crit, 100), gl)
})
df_crit_right = pd.DataFrame({
    't': np.linspace(t_crit, 4, 100),
    'densidad': stats.t.pdf(np.linspace(t_crit, 4, 100), gl)
})
df_pval = pd.DataFrame({
    't': np.linspace(t_obs, 4, 100),
    'densidad': stats.t.pdf(np.linspace(t_obs, 4, 100), gl)
})

# Crear figura
fig, ax = plt.subplots(figsize=(10, 6), facecolor=COL_FONDO)

# Densidad t
ax.plot(df_plot['t'], df_plot['densidad'], color=COL_NORMAL, linewidth=1.5)

# Regiones críticas
ax.fill_between(df_crit_left['t'], 0, df_crit_left['densidad'],
                color=COL_REGION_CRITICA, alpha=0.3, label='Región crítica')
ax.fill_between(df_crit_right['t'], 0, df_crit_right['densidad'],
                color=COL_REGION_CRITICA, alpha=0.3)

# Valores críticos
ax.axvline(-t_crit, color=COL_REGION_CRITICA, linestyle='--', linewidth=1.5)
ax.axvline(t_crit, color=COL_REGION_CRITICA, linestyle='--', linewidth=1.5)

# Estadístico observado
ax.axvline(t_obs, color=COL_T_OBS, linestyle='-', linewidth=2)

# Área p-valor
ax.fill_between(df_pval['t'], 0, df_pval['densidad'],
                color=COL_SOMBRA, alpha=0.5, label='Área p-valor')

# Etiquetas
# Construir la cadena del título de forma robusta para MathText
title_string = r'Distribución t de Student con Región Crítica (alpha = {:.2f})'.format(alpha)
ax.set_title(title_string,
             fontsize=14, fontweight='bold', color=COL_TEXT, pad=20)
ax.set_xlabel('Estadístico t', fontsize=12, fontweight='bold', color=COL_TEXT)
ax.set_ylabel('Densidad de Probabilidad', fontsize=12, fontweight='bold', color=COL_TEXT)

# Texto con valores
ax.text(-3.5, 0.35, f't obs = {t_obs:.3f}\np = {p_valor:.4f}',
        fontsize=10, color=COL_T_OBS, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", facecolor=COL_FONDO, edgecolor=COL_T_OBS))

ax.text(2.5, 0.35, f't crit = \u00b1{t_crit:.3f}',
        fontsize=10, color=COL_REGION_CRITICA, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", facecolor=COL_FONDO, edgecolor=COL_REGION_CRITICA))

# Ejes
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.4)
ax.tick_params(colors=COL_TEXT, labelsize=11, width=0.5)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_color(COL_NORMAL)
ax.spines['left'].set_color(COL_NORMAL)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)

# Eliminar grid
ax.grid(False)

# Añadir línea vertical en 0
# Construir la cadena para H0 de forma robusta para MathText
h0_text_string = r'H_0: mu = {}'.format(mu_0)
ax.text(0.1, 0.3, h0_text_string, fontsize=10, color=COL_NORMAL,
        bbox=dict(boxstyle="round,pad=0.2", facecolor=COL_FONDO, edgecolor=COL_NORMAL))

# IC 95%
ax.text(0, 0.02, f'IC 95% = [{ic_95[0]:.2f}, {ic_95[1]:.2f}]',
        fontsize=9, color=COL_T_OBS, ha='center',
        bbox=dict(boxstyle="round,pad=0.3", facecolor=COL_FONDO, edgecolor=COL_T_OBS))

plt.tight_layout()
plt.savefig('t_test_plot.pdf', bbox_inches='tight')
plt.show()

print("\n=== GRÁFICO PROFESIONAL GENERADO ===\n")
print("Características:")
print("  \u2713 Sin cuadrícula/grid")
print("  \u2713 Colores corporativos (rojo/azul profesional)")
print("  \u2713 Regiones críticas sombreadas")
print("  \u2713 Estadístico observado marcado")
print("  \u2713 Área p-valor visualizada")
print("  \u2713 Ejes limpios y minimalistas\n")
