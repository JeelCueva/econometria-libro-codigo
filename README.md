# 📚 Código del Libro: Introducción a la Econometría

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)

Repositorio oficial con todo el código, datos y materiales complementarios del libro **"Introducción a la Econometría: Teoría y Aplicaciones"**.

---

## 📖 Sobre este Repositorio

Este repositorio contiene:
- ✅ **Scripts en Python** para todos los ejemplos y casos prácticos
- ✅ **Scripts en R** para verificación y análisis alternativo
- ✅ **Conjuntos de datos** en formato CSV
- ✅ **Notebooks interactivos** (Jupyter y R Markdown)
- ✅ **Ejercicios resueltos** paso a paso
- ✅ **Visualizaciones** y gráficos reproducibles

---

## 🗂️ Estructura del Repositorio

```
econometria-libro-codigo/
│
├── README.md                      # Este archivo
├── LICENSE                        # Licencia MIT
├── requirements.txt               # Dependencias Python
├── environment.yml                # Entorno conda
├── .gitignore                     # Archivos a ignorar
│
├── capitulo01_introduccion/
│   ├── README.md
│   ├── scripts/
│   ├── notebooks/
│   └── datos/
│
├── capitulo02_estadistica_basica/
│   ├── README.md
│   ├── scripts/
│   ├── notebooks/
│   └── datos/
│
├── capitulo03_algebra_matricial/
│   ├── README.md
│   ├── scripts/
│   │   ├── verificacion_cap3.py
│   │   ├── caso_practico.R
│   │   └── operaciones_matriciales.py
│   ├── notebooks/
│   │   ├── cap3_interactivo.ipynb
│   │   └── cap3_analisis.Rmd
│   └── datos/
│       └── datos_gasto_hogares.csv
│
├── capitulo04_regresion_simple/
├── capitulo05_regresion_multiple/
├── capitulo06_inferencia/
├── capitulo07_multicolinealidad/
├── capitulo08_heterocedasticidad/
├── capitulo09_autocorrelacion/
├── capitulo10_variables_instrumentales/
├── capitulo11_modelos_panel/
├── capitulo12_series_temporales/
├── capitulo13_modelos_var/
├── capitulo14_cointegracion/
├── capitulo15_modelos_no_lineales/
├── capitulo16_variables_limitadas/
├── capitulo17_gmm/
├── capitulo18_maxima_verosimilitud/
│
├── datos_comunes/                 # Datasets usados en múltiples capítulos
│   ├── README.md
│   ├── enaho_muestra.csv
│   ├── pbi_peru.csv
│   └── indices_bvl.csv
│
├── utilidades/                    # Funciones auxiliares reutilizables
│   ├── __init__.py
│   ├── estadistica.py
│   ├── visualizacion.py
│   └── diagnosticos.R
│
└── ejercicios/                    # Ejercicios adicionales
    ├── README.md
    ├── ejercicios_capitulo01.pdf
    ├── ejercicios_capitulo02.pdf
    └── ...
```

---

## 🚀 Inicio Rápido

### Opción 1: Clonar el Repositorio Completo

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/econometria-libro-codigo.git
cd econometria-libro-codigo

# Instalar dependencias Python
pip install -r requirements.txt

# O usar conda
conda env create -f environment.yml
conda activate econometria
```

### Opción 2: Descargar Solo un Capítulo

Visita la carpeta del capítulo que te interesa y descarga los archivos individuales.

### Opción 3: Ejecutar en la Nube (Sin Instalación)

- **Python**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tu-usuario/econometria-libro-codigo)
- **R**: [![RStudio Cloud](https://img.shields.io/badge/RStudio-Cloud-blue)](https://posit.cloud)

---

## 📋 Contenido por Capítulo

### PARTE I: FUNDAMENTOS

| Capítulo | Título | Python | R | Colab | Posit Cloud |
|----------|--------|--------|---|-------|-------------|
| 1 | Introducción a la Econometría | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 2 | Estadística Básica y Probabilidad | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 3 | Álgebra Matricial para Econometría | ✅ | ✅ | [▶️](link) | [▶️](link) |

### PARTE II: REGRESIÓN LINEAL

| Capítulo | Título | Python | R | Colab | Posit Cloud |
|----------|--------|--------|---|-------|-------------|
| 4 | Modelo de Regresión Simple | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 5 | Modelo de Regresión Múltiple | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 6 | Inferencia Estadística en Regresión | ✅ | ✅ | [▶️](link) | [▶️](link) |

### PARTE III: PROBLEMAS CLÁSICOS

| Capítulo | Título | Python | R | Colab | Posit Cloud |
|----------|--------|--------|---|-------|-------------|
| 7 | Multicolinealidad | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 8 | Heterocedasticidad | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 9 | Autocorrelación | ✅ | ✅ | [▶️](link) | [▶️](link) |

### PARTE IV: MODELOS AVANZADOS

| Capítulo | Título | Python | R | Colab | Posit Cloud |
|----------|--------|--------|---|-------|-------------|
| 10 | Variables Instrumentales | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 11 | Modelos de Datos Panel | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 12 | Introducción a Series Temporales | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 13 | Modelos VAR y Causalidad | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 14 | Cointegración y Corrección de Errores | ✅ | ✅ | [▶️](link) | [▶️](link) |

### PARTE V: TEMAS ESPECIALES

| Capítulo | Título | Python | R | Colab | Posit Cloud |
|----------|--------|--------|---|-------|-------------|
| 15 | Modelos No Lineales | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 16 | Variables Dependientes Limitadas | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 17 | Método Generalizado de Momentos (GMM) | ✅ | ✅ | [▶️](link) | [▶️](link) |
| 18 | Máxima Verosimilitud | ✅ | ✅ | [▶️](link) | [▶️](link) |

---

## 💻 Requisitos del Sistema

### Python
- Python 3.8 o superior
- Librerías principales:
  - `numpy >= 1.21.0`
  - `pandas >= 1.3.0`
  - `matplotlib >= 3.4.0`
  - `scipy >= 1.7.0`
  - `statsmodels >= 0.13.0`
  - `scikit-learn >= 1.0.0`

### R
- R 4.0 o superior
- Paquetes principales:
  - `tidyverse`
  - `lmtest`
  - `sandwich`
  - `car`
  - `tseries`
  - `vars`

---

## 📊 Conjuntos de Datos

Todos los datasets están disponibles en formato CSV en las carpetas correspondientes. Los datos incluyen:

- **Encuestas de hogares** (ENAHO - muestra ficticia)
- **Datos macroeconómicos** del Perú (PBI, inflación, tipo de cambio)
- **Series financieras** (índices bursátiles)
- **Datos de panel** (países, empresas)
- **Series temporales** (mensuales y trimestrales)

### Fuentes de Datos
- INEI (Instituto Nacional de Estadística e Informática)
- BCRP (Banco Central de Reserva del Perú)
- Bolsa de Valores de Lima (BVL)
- World Bank Open Data

---

## 🎓 Cómo Usar este Repositorio

### Para Estudiantes
1. **Seguir el libro**: Cada capítulo del libro hace referencia al código correspondiente
2. **Ejecutar ejemplos**: Reproduce los ejemplos del libro paso a paso
3. **Modificar y experimentar**: Cambia parámetros y observa los resultados
4. **Resolver ejercicios**: Usa los ejercicios adicionales para practicar

### Para Profesores
1. **Material de clase**: Usa los notebooks como material de presentación
2. **Tareas**: Asigna los ejercicios como tareas
3. **Exámenes**: Adapta los casos prácticos para evaluaciones
4. **Proyectos**: Los datasets reales son ideales para proyectos finales

### Para Investigadores
1. **Replicación**: Todo el análisis es completamente reproducible
2. **Extensión**: Usa el código como base para tu propia investigación
3. **Comparación**: Compara métodos implementados en Python y R

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores o quieres mejorar el código:

1. **Reporta un error**: Abre un [Issue](https://github.com/tu-usuario/econometria-libro-codigo/issues)
2. **Sugiere mejoras**: Abre un [Pull Request](https://github.com/tu-usuario/econometria-libro-codigo/pulls)
3. **Comparte tu experiencia**: Comenta en las [Discussions](https://github.com/tu-usuario/econometria-libro-codigo/discussions)

### Guía de Contribución
- Mantén el estilo de código consistente
- Agrega comentarios explicativos
- Incluye docstrings en funciones
- Verifica que el código funcione antes de hacer commit

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 📧 Contacto

**Autor**: Jeel Cueva  
**Email**: jeel.cueva.l@uni.pe  
**Universidad**: Universidad Nacional de Ingeniería  
**Sitio web del libro**: [www.ejemplo.com/libro-econometria](https://www.ejemplo.com)

---

## 🙏 Agradecimientos

Este material fue desarrollado gracias al apoyo de:
- Universidad Nacional de Ingeniería
- Estudiantes de las generaciones 2020-2024
- Colaboradores y revisores del código

---

## 📚 Citar este Repositorio

Si usas este código en tu investigación o enseñanza, por favor cita:

```bibtex
@misc{econometria_libro_codigo,
  author = {Jeel Cueva},
  title = {Código del Libro: Econometría Teórica Y Aplicada},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{[(https://github.com/JeelCueva/econometria-libro-codigo)]}}
}
```

---

## 🔄 Actualizaciones

**Última actualización**: Enero 2026

| Versión | Fecha | Cambios |
|---------|-------|---------|
| v1.0.0 | Ene 2026 | Lanzamiento inicial con 18 capítulos |

---

**⭐ Si este repositorio te fue útil, ¡dale una estrella!**

---

*Nota: Este es un proyecto educativo. Los datos y resultados son para fines ilustrativos.*
