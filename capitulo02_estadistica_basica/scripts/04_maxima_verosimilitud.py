#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
CAPÍTULO 2: MÁXIMA VEROSIMILITUD
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("=== ESTIMACIÓN POR MÁXIMA VEROSIMILITUD ===\n")

np.random.seed(123)

# Generar datos
n = 100
mu_verdadero = 10
sigma_verdadero = 2
datos = np.random.normal(mu_verdadero, sigma_verdadero, n)

# Estimadores MLE
mu_hat = np.mean(datos)
sigma_hat_sesgado = np.sqrt(np.sum((datos - mu_hat)**2) / n)
sigma_hat_insesgado = np.std(datos, ddof=1)

print("--- Estimadores MLE ---")
print(f"μ̂ (MLE) = {mu_hat:.4f}")
print(f"σ̂ sesgado = {sigma_hat_sesgado:.4f}")
print(f"σ̂ insesgado = {sigma_hat_insesgado:.4f}\n")

print("Parámetros verdaderos:")
print(f"μ = {mu_verdadero}")
print(f"σ = {sigma_verdadero}\n")

# Errores estándar asintóticos
se_mu = sigma_hat_insesgado / np.sqrt(n)
se_sigma = sigma_hat_insesgado / np.sqrt(2 * n)

print("Errores estándar asintóticos:")
print(f"SE(μ̂) = {se_mu:.4f}")
print(f"SE(σ̂) = {se_sigma:.4f}\n")

# Intervalos de confianza
ic_mu_lower = mu_hat - 1.96 * se_mu
ic_mu_upper = mu_hat + 1.96 * se_mu

print(f"IC 95% para μ: [{ic_mu_lower:.3f}, {ic_mu_upper:.3f}]")
contiene = mu_verdadero >= ic_mu_lower and mu_verdadero <= ic_mu_upper
print(f"¿Contiene μ verdadero? {'SÍ' if contiene else 'NO'}\n")

# Superficie de verosimilitud
mu_seq = np.linspace(mu_hat - 1, mu_hat + 1, 50)
sigma_seq = np.linspace(sigma_hat_sesgado - 0.5, sigma_hat_sesgado + 0.5, 50)
MU, SIGMA = np.meshgrid(mu_seq, sigma_seq)

loglik = np.zeros_like(MU)
for i in range(len(mu_seq)):
    for j in range(len(sigma_seq)):
        loglik[j, i] = np.sum(stats.norm.logpdf(datos, loc=MU[j, i], scale=SIGMA[j, i]))

# Visualización
plt.figure(figsize=(8, 6))
contour = plt.contour(MU, SIGMA, loglik, levels=20, cmap='viridis')
plt.colorbar(contour, label='Log-Verosimilitud')
plt.plot(mu_hat, sigma_hat_sesgado, 'ro', markersize=10, label='MLE')
plt.plot(mu_verdadero, sigma_verdadero, 'b^', markersize=10, label='Verdadero')
plt.xlabel('μ')
plt.ylabel('σ')
plt.title('Superficie de Log-Verosimilitud', fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../figuras/superficie_verosimilitud_python.pdf', dpi=300, bbox_inches='tight')
print("Gráfico guardado: figuras/superficie_verosimilitud_python.pdf")
plt.show()
