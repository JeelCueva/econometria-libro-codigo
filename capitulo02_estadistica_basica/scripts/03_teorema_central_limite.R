# ==============================================================================
# MÓDULO 3: TEOREMA CENTRAL DEL LÍMITE 
# ==============================================================================

cat("=== TEOREMA CENTRAL DEL LÍMITE (VISUALIZACIÓN PROFESIONAL) ===\n\n")
set.seed(789)

# Parámetros de simulación
n <- 30      # Tamaño de cada muestra
m <- 1000    # Número de réplicas

cat("Parámetros:\n")
cat("  Tamaño muestral (n):", n, "\n")
cat("  Número de réplicas (m):", m, "\n\n")

# Paleta de colores profesional (ColorBrewer - Set2)
col_hist <- "orange"    # Azul profesional suave
col_normal <- "#d62728"  # Rojo elegante
col_borde <- "#2c2c2c"   # Gris oscuro casi negro
col_fondo <- "white"     # Blanco puro
col_texto <- "#333333"   # Gris oscuro para texto

# Función para generar y estandarizar medias muestrales
simular_tcl <- function(dist_func, params, n, m, titulo) {
  # Generar medias muestrales
  medias <- replicate(m, {
    datos <- do.call(dist_func, c(list(n), params))
    mean(datos)
  })
  
  # Calcular parámetros teóricos
  if (dist_func == "runif") {
    mu <- 0.5
    sigma <- sqrt(1/12)
  } else if (dist_func == "rexp") {
    mu <- 1
    sigma <- 1
  } else if (dist_func == "rbinom") {
    mu <- params$size * params$prob
    sigma <- sqrt(mu * (1 - params$prob))
  } else if (dist_func == "rchisq") {
    mu <- params$df
    sigma <- sqrt(2 * params$df)
  }
  
  # Estandarizar según TCL
  z <- sqrt(n) * (medias - mu) / sigma
  
  # Prueba de normalidad
  sw_test <- shapiro.test(z)
  
  cat("---", titulo, "---\n")
  cat("  Media Z =", round(mean(z), 4), "(esperado: 0)\n")
  cat("  SD Z    =", round(sd(z), 4), "(esperado: 1)\n")
  cat("  Shapiro-Wilk W =", round(sw_test$statistic, 4), "\n")
  cat("  Shapiro-Wilk p =", round(sw_test$p.value, 4), "\n")
  
  if (sw_test$p.value > 0.05) {
    cat("  ✓ Normalidad NO rechazada al 5%\n\n")
  } else {
    cat("  ✗ Normalidad RECHAZADA al 5%\n\n")
  }
  
  return(z)
}

# 1. Uniforme(0,1): mu=0.5, sigma²=1/12
z_unif <- simular_tcl("runif", list(min = 0, max = 1), n, m, "Uniforme(0,1)")

# 2. Exponencial(lambda=1): mu=1, sigma²=1
z_exp <- simular_tcl("rexp", list(rate = 1), n, m, "Exponencial(1)")

# 3. Binomial(size=10, p=0.5): mu=5, sigma²=2.5
z_binom <- simular_tcl("rbinom", list(size = 10, prob = 0.5), n, m, "Binomial(10, 0.5)")

# 4. Chi-cuadrado(df=5): mu=5, sigma²=10
z_chi <- simular_tcl("rchisq", list(df = 5), n, m, "Chi-cuadrado(5)")

# VERIFICACIÓN VISUAL
cat("=== GENERANDO GRÁFICO PROFESIONAL ===\n")

# Cargar paquetes necesarios
if (!require("ggplot2")) install.packages("ggplot2")
if (!require("gridExtra")) install.packages("gridExtra")
library(ggplot2)
library(gridExtra)

# Función para crear histograma con estilo profesional
crear_histograma <- function(z, titulo) {
  df <- data.frame(z = z)
  
  ggplot(df, aes(x = z)) +
    geom_histogram(aes(y = ..density..), bins = 40, 
                   fill = col_hist, color = col_borde, alpha = 0.8, size = 0.3) +
    stat_function(fun = dnorm, args = list(mean = 0, sd = 1),
                  color = col_normal, size = 1.3, linetype = 1) +
    labs(title = titulo, x = "Estadístico Z", y = "Densidad") +
    theme_classic(base_size = 12, base_family = "sans") +
    theme(
      plot.title = element_text(size = 13, hjust = 0.5, face = "bold", color = col_texto),
      axis.title = element_text(size = 11, face = "bold", color = col_texto),
      axis.text = element_text(size = 10, color = col_texto),
      axis.line = element_line(color = col_borde, size = 0.5),
      panel.background = element_blank(),
      plot.background = element_rect(fill = col_fondo, color = NA),
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank(),
      legend.position = "none"
    ) +
    coord_cartesian(xlim = c(-4, 4))
}

# Crear gráficos
p1 <- crear_histograma(z_unif, "Uniforme(0,1)")
p2 <- crear_histograma(z_exp, "Exponencial(1)")
p3 <- crear_histograma(z_binom, "Binomial(10, 0.5)")
p4 <- crear_histograma(z_chi, "Chi-cuadrado(5)")

# MOSTRAR EN VENTANA DE PLOTS
print(grid.arrange(p1, p2, p3, p4, ncol = 2))

cat("\n=== GRÁFICO PROFESIONAL GENERADO EN VENTANA DE PLOTS ===\n")
cat("\nCaracterísticas:\n")
cat("  ✓ Sin cuadrícula/grid\n")
cat("  ✓ Colores profesionales (azul/rojo corporativo)\n")
cat("  ✓ Tema limpio y minimalista\n")
cat("  ✓ Listo para presentación o reporte\n")
