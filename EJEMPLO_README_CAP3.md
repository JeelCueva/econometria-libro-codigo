# Capítulo 3: Álgebra Matricial para Econometría

## 📋 Descripción

Este capítulo desarrolla los fundamentos del álgebra matricial necesarios para la econometría moderna. Incluye:

- Operaciones matriciales básicas
- Determinantes, trazas y matrices inversas
- Valores y vectores propios
- Descomposiciones matriciales (Cholesky, QR, SVD)
- Diferenciación matricial
- Geometría de proyecciones y MCO

## 📂 Contenido del Capítulo

### 📄 Scripts Python
- `verificacion_cap3.py` - Script completo de verificación de todos los cálculos
- `operaciones_matriciales.py` - Operaciones básicas con ejemplos
- `descomposiciones.py` - Cholesky, QR, SVD implementados
- `visualizaciones.py` - Gráficos de proyecciones geométricas

### 📄 Scripts R
- `caso_practico.R` - Caso completo de regresión múltiple
- `propiedades_matriciales.R` - Verificación de propiedades algebraicas
- `diagnosticos_numericos.R` - Número de condición y estabilidad

### 📓 Notebooks Interactivos
- `cap3_interactivo.ipynb` - Jupyter Notebook con todo el capítulo
- `cap3_analisis.Rmd` - R Markdown con análisis completo

### 📊 Datos
- `datos_gasto_hogares.csv` - Datos del caso práctico (n=6 hogares)

## 🎯 Caso Práctico Principal

**Título**: Estimación de Gasto en Alimentos mediante Regresión Múltiple

**Modelo**: 
```
Y = β₀ + β₁·Ingreso + β₂·Tamaño_Hogar + ε
```

**Datos**: 6 hogares con información sobre:
- Y: Gasto mensual en alimentos (miles S/)
- X₁: Ingreso mensual (miles S/)
- X₂: Número de personas en el hogar

**10 Pasos Resueltos**:
1. Construcción de matrices X e y
2. Cálculo de X'X
3. Cálculo de X'y
4. Verificación de invertibilidad (det(X'X) = 36 ≠ 0)
5. Cálculo de (X'X)⁻¹
6. Estimador MCO: β̂ = [-0.2167, 0.4583, 0.3083]'
7. Valores ajustados y residuos
8. Matrices de proyección P_X y M_X
9. Descomposición de varianza (R² = 99.94%)
10. Descomposiciones avanzadas (QR, SVD, κ = 37.2)

## 🚀 Inicio Rápido

### Ejecutar el Caso Práctico en Python

```bash
# Navegar al directorio
cd capitulo03_algebra_matricial/scripts/

# Ejecutar script principal
python verificacion_cap3.py
```

**Salida esperada**:
```
================================================================================
VERIFICACIÓN COMPLETA - TODOS LOS CÁLCULOS SON CORRECTOS ✓
================================================================================

1. MODELO ESTIMADO:
   Gasto = -0.2167 + 0.4583×Ingreso + 0.3083×TamHogar

2. BONDAD DE AJUSTE:
   • R² = 0.9994 (99.94%)

3. DIAGNÓSTICOS:
   • Número de condición: 37.20 (condicionamiento bueno)
   • No hay multicolinealidad
```

### Ejecutar en R

```r
# Navegar al directorio
setwd("capitulo03_algebra_matricial/scripts/")

# Ejecutar script
source("caso_practico.R")
```

### Ejecutar en la Nube

**Python (Google Colab)**:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tu-usuario/econometria-libro-codigo/blob/main/capitulo03_algebra_matricial/notebooks/cap3_interactivo.ipynb)

**R (Posit Cloud)**:
[![RStudio Cloud](https://img.shields.io/badge/RStudio-Cloud-blue)](https://posit.cloud/content/tu-proyecto)

## 📊 Resultados Principales

### Coeficientes Estimados

| Parámetro | Estimación | Interpretación |
|-----------|------------|----------------|
| β₀ | -0.2167 | Intercepto (sin interpretación práctica) |
| β₁ | 0.4583 | PMC alimentos = 45.8% |
| β₂ | 0.3083 | S/ 308 por persona adicional |

### Bondad de Ajuste

- **R²** = 0.9994 (99.94% de varianza explicada)
- **RSS** = 0.0042 (suma de residuos cuadrados)
- **Número de condición** = 37.2 (buena estabilidad numérica)

### Interpretación Económica

**Propensión Marginal a Gastar en Alimentos (β₁ = 0.4583)**:
- Por cada S/ 1,000 adicionales de ingreso → gasto aumenta S/ 458
- Consistente con la Ley de Engel
- Elasticidad moderada

**Efecto del Tamaño del Hogar (β₂ = 0.3083)**:
- Por persona adicional → gasto aumenta S/ 308
- Economías de escala modestas
- Gasto per cápita decrece con el tamaño

## 🛠️ Requisitos

### Python
```bash
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
scipy>=1.7.0
statsmodels>=0.13.0
```

### R
```r
tidyverse
MASS
Matrix
```

## 📈 Visualizaciones

El capítulo incluye las siguientes visualizaciones:

1. **Proyección ortogonal**: Geometría de MCO
2. **Valores observados vs. ajustados**: Calidad del ajuste
3. **Gráfico de residuos**: Verificación de supuestos
4. **Valores singulares**: Diagnóstico de multicolinealidad

## 🎓 Ejercicios

### Ejercicios Teóricos (10)
1. Demostrar propiedades de la inversa
2. Matrices simétricas y SDP
3. Propiedad cíclica de la traza
4. Cálculo de valores propios
5. Descomposición espectral
6. Simulación con Cholesky
7. Matrices idempotentes
8. Proyecciones en regresión
9. Diferenciación matricial
10. Número de condición

### Ejercicios Computacionales (10)
1. Implementar descomposición LU
2. Comparar métodos de inversión
3. Análisis de multicolinealidad con SVD
4. Simulación Monte Carlo
5. Optimización con gradientes
6. Regresión con datos reales
7. PCA paso a paso
8. Estudio de estabilidad numérica
9. Visualizaciones geométricas
10. Caso integrador completo

## 📚 Referencias del Capítulo

- **Strang, G. (2016).** *Introduction to Linear Algebra* (5th ed.). Wellesley-Cambridge Press.
- **Golub & Van Loan (2013).** *Matrix Computations* (4th ed.). Johns Hopkins.
- **Magnus & Neudecker (1988).** *Matrix Differential Calculus*. Wiley.

## 🔗 Enlaces Relacionados

- [Capítulo 2: Estadística Básica](../capitulo02_estadistica_basica/)
- [Capítulo 4: Regresión Simple](../capitulo04_regresion_simple/)
- [Capítulo 5: Regresión Múltiple](../capitulo05_regresion_multiple/)

## 💡 Notas Adicionales

- Todos los cálculos verificados con precisión < 10⁻¹⁴
- Código completamente reproducible
- Incluye comparación Python vs. R
- Ejemplos económicos reales del contexto peruano

## 📧 Reportar Problemas

Si encuentras algún error en el código o tienes sugerencias:
- Abre un [Issue](https://github.com/tu-usuario/econometria-libro-codigo/issues)
- Etiqueta con: `capitulo-3`, `algebra-matricial`

---

**Última actualización**: Enero 2026
