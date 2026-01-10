#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
MÓDULO 3: TEOREMA CENTRAL DEL LÍMITE (VERSIÓN PROFESIONAL)
==============================================================================
Simulación de convergencia a normalidad para diferentes distribuciones poblacionales
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import warnings

# Ignorar warnings de deprecación
warnings.filterwarnings('ignore')

print("="*70)
print("TEOREMA CENTRAL DEL LÍMITE (VISUALIZACIÓN PROFESIONAL)")
print("="*70)

# Parámetros de simulación
np.random.seed(789)
n = 30      # Tamaño de cada muestra
m = 1000    # Número de réplicas

print(f"\nParámetros:")
print(f"  Tamaño muestral (n): {n}")
print(f"  Número de réplicas (m): {m}\n")

# Paleta de colores profesional
COL_HIST = '#FF8C00'      # Naranja profesional
COL_NORMAL = '#d62728'    # Rojo elegante
COL_BORDE = '#2c2c2c'     # Gris oscuro casi negro
COL_FONDO = 'white'       # Blanco puro
COL_TEXTO = '#333333'     # Gris oscuro para texto

def simular_tcl(dist_func, params, n, m, nombre):
    """
    Simula el Teorema Central del Límite para una distribución dada
    
    Parámetros:
    -----------
    dist_func : función
        Función de distribución (np.random)
    params : dict
        Parámetros de la distribución
    n : int
        Tamaño de muestra
    m : int
        Número de réplicas
    nombre : str
        Nombre de la distribución
        
    Retorna:
    --------
    z : array
        Valores estandarizados según TCL
    """
    # Generar medias muestrales
    medias = np.array([np.mean(dist_func(size=n, **params)) for _ in range(m)])
    
    # Calcular parámetros teóricos
    if dist_func == np.random.uniform:
        mu = 0.5
        sigma = np.sqrt(1/12)
    elif dist_func == np.random.exponential:
        mu = 1
        sigma = 1
    elif dist_func == np.random.binomial:
        mu = params['n'] * params['p']
        sigma = np.sqrt(mu * (1 - params['p']))
    elif dist_func == np.random.chisquare:
        mu = params['df']
        sigma = np.sqrt(2 * params['df'])
    
    # Estandarizar según TCL
    z = np.sqrt(n) * (medias - mu) / sigma
    
    # Prueba de normalidad de Shapiro-Wilk
    shapiro_stat, shapiro_p = stats.shapiro(z)
    
    print(f"--- {nombre} ---")
    print(f"  Media Z = {np.mean(z):.4f} (esperado: 0)")
    print(f"  SD Z    = {np.std(z, ddof=1):.4f} (esperado: 1)")
    print(f"  Shapiro-Wilk W = {shapiro_stat:.4f}")
    print(f"  Shapiro-Wilk p = {shapiro_p:.4f}")
    
    if shapiro_p > 0.05:
        print("  ✓ Normalidad NO rechazada al 5%\n")
    else:
        print("  ✗ Normalidad RECHAZADA al 5%\n")
    
    return z

# 1. Uniforme(0,1): mu=0.5, sigma²=1/12
z_unif = simular_tcl(np.random.uniform, {'low':0, 'high':1}, n, m, "Uniforme(0,1)")

# 2. Exponencial(lambda=1): mu=1, sigma²=1
z_exp = simular_tcl(np.random.exponential, {}, n, m, "Exponencial(1)")

# 3. Binomial(size=10, p=0.5): mu=5, sigma²=2.5
z_binom = simular_tcl(np.random.binomial, {'n':10, 'p':0.5}, n, m, "Binomial(10, 0.5)")

# 4. Chi-cuadrado(df=5): mu=5, sigma²=10
z_chi = simular_tcl(np.random.chisquare, {'df':5}, n, m, "Chi-cuadrado(5)")

print("="*70)
print("GENERANDO GRÁFICO PROFESIONAL")
print("="*70)

def crear_histograma(z, titulo):
    """
    Crea histograma con estilo profesional para validación visual del TCL
    """
    fig, ax = plt.subplots(figsize=(6, 4.5))
    
    # Histograma
    ax.hist(z, bins=40, density=True, alpha=0.8, 
            color=COL_HIST, edgecolor=COL_BORDE, linewidth=0.5)
    
    # Curva normal teórica
    x = np.linspace(-4, 4, 100)
    y = stats.norm.pdf(x, 0, 1)
    ax.plot(x, y, color=COL_NORMAL, linewidth=1.8, label='N(0,1) Teórica')
    
    # Configuración del estilo
    ax.set_title(titulo, fontsize=13, fontweight='bold', 
                 color=COL_TEXTO, pad=15)
    ax.set_xlabel('Estadístico Z', fontsize=11, fontweight='bold', color=COL_TEXTO)
    ax.set_ylabel('Densidad', fontsize=11, fontweight='bold', color=COL_TEXTO)
    
    # Ejes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COL_BORDE)
    ax.spines['bottom'].set_color(COL_BORDE)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_linewidth(0.5)
    
    # Límites y ticks
    ax.set_xlim(-4, 4)
    ax.tick_params(colors=COL_TEXTO, labelsize=10, width=0.5)
    
    # Fondo
    ax.set_facecolor(COL_FONDO)
    fig.patch.set_facecolor(COL_FONDO)
    
    # Leyenda
    ax.legend(loc='upper right', frameon=False, fontsize=9)
    
    plt.tight_layout()
    return fig

# Crear los 4 gráficos
fig1 = crear_histograma(z_unif, "Uniforme(0,1)")
fig2 = crear_histograma(z_exp, "Exponencial(1)")
fig3 = crear_histograma(z_binom, "Binomial(10, 0.5)")
fig4 = crear_histograma(z_chi, "Chi-cuadrado(5)")

# Mostrar en ventana emergente
print("\n=== MOSTRANDO GRÁFICOS EN VENTANA ===\n")

# Crear figura combinada
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
fig.patch.set_facecolor(COL_FONDO)

def plot_en_subplot(ax, z, titulo):
    ax.hist(z, bins=40, density=True, alpha=0.8, 
            color=COL_HIST, edgecolor=COL_BORDE, linewidth=0.5)
    
    x = np.linspace(-4, 4, 100)
    y = stats.norm.pdf(x, 0, 1)
    ax.plot(x, y, color=COL_NORMAL, linewidth=1.8)
    
    ax.set_title(titulo, fontsize=13, fontweight='bold', 
                 color=COL_TEXTO, pad=15)
    ax.set_xlabel('Estadístico Z', fontsize=11, fontweight='bold', color=COL_TEXTO)
    ax.set_ylabel('Densidad', fontsize=11, fontweight='bold', color=COL_TEXTO)
    
    # Remover grid
    ax.grid(False)
    
    # Configurar ejes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COL_BORDE)
    ax.spines['bottom'].set_color(COL_BORDE)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_linewidth(0.5)
    
    ax.set_xlim(-4, 4)
    ax.set_facecolor(COL_FONDO)
    ax.tick_params(colors=COL_TEXTO, labelsize=10, width=0.5)

plot_en_subplot(ax1, z_unif, "Uniforme(0,1)")
plot_en_subplot(ax2, z_exp, "Exponencial(1)")
plot_en_subplot(ax3, z_binom, "Binomial(10, 0.5)")
plot_en_subplot(ax4, z_chi, "Chi-cuadrado(5)")

plt.tight_layout()
plt.show()

print("\n=== GRÁFICO PROFESIONAL GENERADO ===\n")
print("Características:")
print("  ✓ Sin cuadrícula/grid")
print("  ✓ Colores profesionales (naranja/rojo)")
print("  ✓ Tema limpio y minimalista")
print("  ✓ Listo para presentación o reporte\n")
