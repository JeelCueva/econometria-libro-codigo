# ==============================================================================
# CAPÍTULO 2: PRUEBA DE HIPÓTESIS
# ==============================================================================

# Cargar librerías necesarias
library(ggplot2)
library(dplyr)

# Limpiar consola
cat("\014")

cat("======================================================================\n")
cat("PRUEBA T PARA LA MEDIA (VISUALIZACIÓN PROFESIONAL)\n")
cat("======================================================================\n\n")

# ==============================================================================
# PARÁMETROS DEL EXPERIMENTO
# ==============================================================================

set.seed(20231115)  # Semilla idéntica a Python

mu_0 <- 100         # H0: μ = 100
mu_real <- 103      # Media poblacional real
sigma_real <- 15    # Desviación poblacional
n <- 25             # Tamaño muestral
alpha <- 0.05       # Nivel de significancia

cat("Diseño del experimento:\n")
cat(sprintf("  H0: μ = %d\n", mu_0))
cat(sprintf("  H1: μ ≠ %d (prueba bilateral)\n", mu_0))
cat(sprintf("  Nivel de significancia α = %.2f\n", alpha))
cat(sprintf("  Tamaño muestral n = %d\n\n", n))

# ==============================================================================
# GENERAR DATOS
# ==============================================================================

X <- rnorm(n, mean = mu_real, sd = sigma_real)

# Estadísticos muestrales
x_bar <- mean(X)
s <- sd(X)
se <- s / sqrt(n)

cat("Estadísticos muestrales:\n")
cat(sprintf("  Media muestral (X̄) = %.2f\n", x_bar))
cat(sprintf("  Desviación estándar (S) = %.2f\n", s))
cat(sprintf("  Error estándar (S/√n) = %.2f\n\n", se))

# ==============================================================================
# PRUEBA T
# ==============================================================================

gl <- n - 1
t_obs <- (x_bar - mu_0) / se
t_crit <- qt(1 - alpha/2, df = gl)
p_valor <- 2 * (1 - pt(abs(t_obs), df = gl))

# Intervalo de confianza 95%
ic_95_lower <- x_bar - qt(0.975, df = gl) * se
ic_95_upper <- x_bar + qt(0.975, df = gl) * se
ic_95 <- c(ic_95_lower, ic_95_upper)

cat("=== RESULTADOS DE LA PRUEBA T ===\n")
cat(sprintf("  Grados de libertad = %d\n", gl))
cat(sprintf("  Estadístico t = %.3f\n", t_obs))
cat(sprintf("  Valor crítico = ±%.3f\n", t_crit))
cat(sprintf("  p-valor = %.4f\n\n", p_valor))

cat(sprintf("  IC 95%% = [%.2f, %.2f]\n", ic_95[1], ic_95[2]))
contiene_mu0 <- ic_95[1] <= mu_0 && mu_0 <= ic_95[2]
cat(sprintf("  ¿Contiene μ0=%d? %s\n\n", mu_0, 
            ifelse(contiene_mu0, "✓ SÍ", "✗ NO")))

cat("=== DECISIÓN ===\n")
if (p_valor < alpha) {
  cat(sprintf("  ✗ RECHAZAR H0 al nivel %.2f\n\n", alpha))
} else {
  cat(sprintf("  ✓ NO RECHAZAR H0 al nivel %.2f\n\n", alpha))
}

# ==============================================================================
# VISUALIZACIÓN PROFESIONAL CON GGPLOT2
# ==============================================================================

cat("=== GENERANDO GRÁFICO PROFESIONAL ===\n")

# Paleta de colores corporativa
COL_REGION_CRITICA <- "#e41a1c"
COL_T_OBS <- "#377eb8"
COL_NORMAL <- "#2c2c2c"
COL_TEXT <- "#333333"
COL_FONDO <- "white"
COL_SOMBRA <- "#ffcccc"

# Crear secuencia para densidad t
x_t <- seq(-4, 4, length.out = 500)
y_t <- dt(x_t, df = gl)
df_plot <- data.frame(t = x_t, densidad = y_t)

# Región crítica izquierda
x_crit_left <- seq(-4, -t_crit, length.out = 100)
df_crit_left <- data.frame(t = x_crit_left, densidad = dt(x_crit_left, df = gl))

# Región crítica derecha
x_crit_right <- seq(t_crit, 4, length.out = 100)
df_crit_right <- data.frame(t = x_crit_right, densidad = dt(x_crit_right, df = gl))

# Área p-valor
x_pval <- seq(t_obs, 4, length.out = 100)
df_pval <- data.frame(t = x_pval, densidad = dt(x_pval, df = gl))

# ==============================================================================
# CREAR GRÁFICO (VERSIÓN CORREGIDA)
# ==============================================================================

p <- ggplot() +
  # Densidad t completa
  geom_line(data = df_plot, aes(x = t, y = densidad), 
            color = COL_NORMAL, size = 1.5) +
  
  # Regiones críticas sombreadas
  geom_ribbon(data = df_crit_left, aes(x = t, ymin = 0, ymax = densidad),
              fill = COL_REGION_CRITICA, alpha = 0.3) +
  geom_ribbon(data = df_crit_right, aes(x = t, ymin = 0, ymax = densidad),
              fill = COL_REGION_CRITICA, alpha = 0.3) +
  
  # Valores críticos
  geom_vline(xintercept = -t_crit, color = COL_REGION_CRITICA, 
             linetype = "dashed", size = 1.5) +
  geom_vline(xintercept = t_crit, color = COL_REGION_CRITICA, 
             linetype = "dashed", size = 1.5) +
  
  # Estadístico observado
  geom_vline(xintercept = t_obs, color = COL_T_OBS, 
             linetype = "solid", size = 2) +
  
  # Área p-valor
  geom_ribbon(data = df_pval, aes(x = t, ymin = 0, ymax = densidad),
              fill = COL_SOMBRA, alpha = 0.5) +
  
  # Anotaciones de texto
  annotate("text", x = -3.5, y = 0.35, 
           label = sprintf("t obs = %.3f\np = %.4f", t_obs, p_valor),
           color = COL_T_OBS, fontface = "bold", size = 3.5,
           hjust = 0) +
  
  annotate("text", x = 2.5, y = 0.35, 
           label = sprintf("t crit = ±%.3f", t_crit),
           color = COL_REGION_CRITICA, fontface = "bold", size = 3.5,
           hjust = 0) +
  
  # ========== CORRECCIÓN APLICADA AQUÍ ==========
annotate("text", x = 0.1, y = 0.3, 
         label = sprintf("H[0]:~mu == %d", mu_0),
         parse = TRUE,  # ← SOLUCIÓN: parse = TRUE
         color = COL_NORMAL, size = 3.5) +
  # ==============================================

annotate("text", x = 0, y = 0.02, 
         label = sprintf("IC 95%% = [%.2f, %.2f]", ic_95[1], ic_95[2]),
         color = COL_T_OBS, size = 3, hjust = 0.5) +
  
  # Etiquetas y título
  labs(
    title = sprintf("Distribución t de Student con Región Crítica (α = %.2f)", alpha),
    x = "Estadístico t",
    y = "Densidad de Probabilidad"
  ) +
  
  # Límites
  coord_cartesian(xlim = c(-4, 4), ylim = c(0, 0.4)) +
  
  # Tema profesional
  theme_minimal() +
  theme(
    plot.title = element_text(size = 14, face = "bold", 
                              color = COL_TEXT, hjust = 0.5, 
                              margin = margin(b = 20)),
    axis.title.x = element_text(size = 12, face = "bold", color = COL_TEXT),
    axis.title.y = element_text(size = 12, face = "bold", color = COL_TEXT),
    axis.text = element_text(size = 11, color = COL_TEXT),
    panel.grid = element_blank(),
    panel.background = element_rect(fill = COL_FONDO, color = NA),
    plot.background = element_rect(fill = COL_FONDO, color = NA),
    axis.line = element_line(color = COL_NORMAL, size = 0.5),
    axis.ticks = element_line(color = COL_TEXT, size = 0.5)
  )

# Mostrar gráfico
print(p)

# Guardar PDF
ggsave("t_test_plot.pdf", plot = p, 
       width = 10, height = 6, units = "in", dpi = 300)

cat("\n=== GRÁFICO PROFESIONAL GENERADO ===\n\n")
cat("Características:\n")
cat("  ✓ Sin cuadrícula/grid\n")
cat("  ✓ Colores corporativos (rojo/azul profesional)\n")
cat("  ✓ Regiones críticas sombreadas\n")
cat("  ✓ Estadístico observado marcado\n")
cat("  ✓ Área p-valor visualizada\n")
cat("  ✓ Ejes limpios y minimalistas\n\n")
cat("Archivo guardado: t_test_plot.pdf\n\n")

# ==============================================================================
# TABLA RESUMEN
# ==============================================================================

cat("=== TABLA RESUMEN ===\n\n")

resultados_tabla <- data.frame(
  Estadistico = c("Media muestral (X̄)", 
                  "Desviación estándar (S)", 
                  "Error estándar",
                  "Estadístico t",
                  "Grados de libertad",
                  "Valor crítico",
                  "p-valor",
                  "IC 95% inferior",
                  "IC 95% superior",
                  "Decisión"),
  Valor = c(sprintf("%.2f", x_bar),
            sprintf("%.2f", s),
            sprintf("%.2f", se),
            sprintf("%.3f", t_obs),
            sprintf("%d", gl),
            sprintf("±%.3f", t_crit),
            sprintf("%.4f", p_valor),
            sprintf("%.2f", ic_95[1]),
            sprintf("%.2f", ic_95[2]),
            ifelse(p_valor < alpha, "RECHAZAR H0", "NO RECHAZAR H0"))
)

print(resultados_tabla, row.names = FALSE)

cat("\n======================================================================\n")
cat("ANÁLISIS COMPLETADO\n")
cat("======================================================================\n")
