#!/usr/bin/env python3
"""
Script para generar automáticamente la estructura del repositorio
de código del libro de Econometría (18 capítulos).

Uso:
    python crear_estructura_repositorio.py
"""

import os
from pathlib import Path

# ====================================================================
# DEFINICIÓN DE LOS 18 CAPÍTULOS
# ====================================================================

CAPITULOS = [
    {
        "num": 1,
        "nombre": "introduccion",
        "titulo": "Introducción a la Econometría",
        "descripcion": "Naturaleza, objetivos y metodología de la econometría"
    },
    {
        "num": 2,
        "nombre": "estadistica_basica",
        "titulo": "Estadística Básica y Probabilidad",
        "descripcion": "Fundamentos estadísticos para econometría"
    },
    {
        "num": 3,
        "nombre": "algebra_matricial",
        "titulo": "Álgebra Matricial para Econometría",
        "descripcion": "Operaciones matriciales, descomposiciones y proyecciones"
    },
    {
        "num": 4,
        "nombre": "regresion_simple",
        "titulo": "Modelo de Regresión Lineal Simple",
        "descripcion": "MCO, supuestos clásicos y propiedades del estimador"
    },
    {
        "num": 5,
        "nombre": "regresion_multiple",
        "titulo": "Modelo de Regresión Lineal Múltiple",
        "descripcion": "Extensión a múltiples variables explicativas"
    },
    {
        "num": 6,
        "nombre": "inferencia",
        "titulo": "Inferencia Estadística en Regresión",
        "descripcion": "Pruebas de hipótesis, intervalos de confianza y predicción"
    },
    {
        "num": 7,
        "nombre": "multicolinealidad",
        "titulo": "Multicolinealidad",
        "descripcion": "Detección, consecuencias y soluciones"
    },
    {
        "num": 8,
        "nombre": "heterocedasticidad",
        "titulo": "Heterocedasticidad",
        "descripcion": "Detección, consecuencias y estimadores robustos"
    },
    {
        "num": 9,
        "nombre": "autocorrelacion",
        "titulo": "Autocorrelación",
        "descripcion": "Detección, consecuencias y métodos de corrección"
    },
    {
        "num": 10,
        "nombre": "variables_instrumentales",
        "titulo": "Variables Instrumentales",
        "descripcion": "Endogeneidad y estimación por VI y 2SLS"
    },
    {
        "num": 11,
        "nombre": "modelos_panel",
        "titulo": "Modelos de Datos Panel",
        "descripcion": "Efectos fijos, efectos aleatorios y pruebas de especificación"
    },
    {
        "num": 12,
        "nombre": "series_temporales",
        "titulo": "Introducción a Series Temporales",
        "descripcion": "Estacionariedad, ACF, PACF y modelos ARIMA"
    },
    {
        "num": 13,
        "nombre": "modelos_var",
        "titulo": "Modelos VAR y Causalidad",
        "descripcion": "Vectores autorregresivos y causalidad de Granger"
    },
    {
        "num": 14,
        "nombre": "cointegracion",
        "titulo": "Cointegración y Corrección de Errores",
        "descripcion": "Relaciones de largo plazo y modelos ECM"
    },
    {
        "num": 15,
        "nombre": "modelos_no_lineales",
        "titulo": "Modelos No Lineales",
        "descripcion": "Especificación, estimación y pruebas de no linealidad"
    },
    {
        "num": 16,
        "nombre": "variables_limitadas",
        "titulo": "Variables Dependientes Limitadas",
        "descripcion": "Modelos Probit, Logit, Tobit y de conteo"
    },
    {
        "num": 17,
        "nombre": "gmm",
        "titulo": "Método Generalizado de Momentos",
        "descripcion": "Teoría y aplicaciones del GMM"
    },
    {
        "num": 18,
        "nombre": "maxima_verosimilitud",
        "titulo": "Estimación por Máxima Verosimilitud",
        "descripcion": "Principios, propiedades y pruebas de hipótesis"
    }
]

# ====================================================================
# PLANTILLA README PARA CADA CAPÍTULO
# ====================================================================

README_TEMPLATE = """# Capítulo {num}: {titulo}

## 📋 Descripción

{descripcion}

## 📂 Contenido del Capítulo

### 📄 Scripts Python
- `ejemplo_principal.py` - Ejemplo principal del capítulo
- `ejercicios_resueltos.py` - Soluciones a ejercicios seleccionados
- `funciones_utilidad.py` - Funciones auxiliares reutilizables

### 📄 Scripts R
- `ejemplo_principal.R` - Ejemplo principal en R
- `ejercicios_resueltos.R` - Soluciones en R
- `graficos.R` - Visualizaciones adicionales

### 📓 Notebooks Interactivos
- `cap{num}_interactivo.ipynb` - Jupyter Notebook completo
- `cap{num}_analisis.Rmd` - R Markdown con análisis

### 📊 Datos
- Los datasets específicos de este capítulo

## 🚀 Inicio Rápido

### Python
```bash
cd capitulo{num:02d}_{nombre}/scripts/
python ejemplo_principal.py
```

### R
```r
setwd("capitulo{num:02d}_{nombre}/scripts/")
source("ejemplo_principal.R")
```

### Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tu-usuario/econometria-libro-codigo/blob/main/capitulo{num:02d}_{nombre}/notebooks/cap{num}_interactivo.ipynb)

## 📚 Temas Principales

1. Tema 1
2. Tema 2
3. Tema 3
4. Tema 4
5. Tema 5

## 🎓 Ejercicios

- **Teóricos**: X ejercicios
- **Computacionales**: Y ejercicios
- **Aplicados**: Z ejercicios

Ver archivo `ejercicios.md` para detalles.

## 🔗 Enlaces Relacionados

- [Capítulo anterior](../capitulo{prev:02d}_xxx/)
- [Capítulo siguiente](../capitulo{next:02d}_xxx/)
- [Datos comunes](../datos_comunes/)

## 📧 Reportar Problemas

Si encuentras errores, abre un [Issue](https://github.com/tu-usuario/econometria-libro-codigo/issues) con la etiqueta `capitulo-{num}`.

---

**Última actualización**: Enero 2026
"""

# ====================================================================
# FUNCIÓN PARA CREAR ESTRUCTURA
# ====================================================================

def crear_estructura_capitulo(capitulo_info, ruta_base="."):
    """
    Crea la estructura de carpetas y archivos para un capítulo.
    
    Args:
        capitulo_info: Diccionario con información del capítulo
        ruta_base: Ruta base donde crear la estructura
    """
    num = capitulo_info["num"]
    nombre = capitulo_info["nombre"]
    titulo = capitulo_info["titulo"]
    descripcion = capitulo_info["descripcion"]
    
    # Nombre de la carpeta del capítulo
    carpeta_cap = f"capitulo{num:02d}_{nombre}"
    ruta_cap = Path(ruta_base) / carpeta_cap
    
    # Crear carpeta principal del capítulo
    ruta_cap.mkdir(parents=True, exist_ok=True)
    
    # Crear subcarpetas
    subcarpetas = ["scripts", "notebooks", "datos", "figuras", "resultados"]
    for subcarpeta in subcarpetas:
        (ruta_cap / subcarpeta).mkdir(exist_ok=True)
    
    # Crear README.md del capítulo
    prev_num = num - 1 if num > 1 else 1
    next_num = num + 1 if num < 18 else 18
    
    readme_contenido = README_TEMPLATE.format(
        num=num,
        titulo=titulo,
        descripcion=descripcion,
        nombre=nombre,
        prev=prev_num,
        next=next_num
    )
    
    with open(ruta_cap / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_contenido)
    
    # Crear archivos .gitkeep para mantener carpetas vacías en Git
    for subcarpeta in subcarpetas:
        with open(ruta_cap / subcarpeta / ".gitkeep", "w") as f:
            f.write("")
    
    print(f"✓ Creado: {carpeta_cap}")

# ====================================================================
# FUNCIÓN PRINCIPAL
# ====================================================================

def main():
    """
    Función principal para crear toda la estructura del repositorio.
    """
    print("=" * 70)
    print("CREANDO ESTRUCTURA DEL REPOSITORIO DE ECONOMETRÍA")
    print("=" * 70)
    print()
    
    # Ruta base (puede cambiarse)
    ruta_base = Path(".")
    
    # Crear estructura para cada capítulo
    for capitulo in CAPITULOS:
        crear_estructura_capitulo(capitulo, ruta_base)
    
    # Crear carpetas adicionales
    print("\nCreando carpetas adicionales...")
    carpetas_extra = ["datos_comunes", "utilidades", "ejercicios", "recursos"]
    for carpeta in carpetas_extra:
        Path(ruta_base / carpeta).mkdir(exist_ok=True)
        print(f"✓ Creado: {carpeta}/")
    
    print()
    print("=" * 70)
    print("✓ ESTRUCTURA COMPLETA CREADA EXITOSAMENTE")
    print("=" * 70)
    print()
    print("Siguiente paso:")
    print("1. Revisa las carpetas creadas")
    print("2. Agrega tus scripts Python y R en cada carpeta scripts/")
    print("3. Coloca los datos en las carpetas datos/")
    print("4. Sube todo a GitHub")
    print()

# ====================================================================
# EJECUTAR
# ====================================================================

if __name__ == "__main__":
    main()
