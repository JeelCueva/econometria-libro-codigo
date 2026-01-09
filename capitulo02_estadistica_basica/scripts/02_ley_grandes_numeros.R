# ==============================================================================
# CAPÍTULO 2: LEY DE GRANDES NÚMEROS
# ==============================================================================

cat("=== LEY DE GRANDES NÚMEROS ===\n\n")
set.seed(123)

mu <- 5
sigma <- 2
n_max <- 10000

datos <- rnorm(n_max, mean = mu, sd = sigma)
media_acumulada <- cumsum(datos) / seq_along(datos)

media_final <- media_acumulada[n_max]
error_abs <- abs(media_final - mu)
error_rel <- (error_abs / mu) * 100

cat("Parámetros: μ =", mu, ", σ =", sigma, "\n")
cat("Media final (n=", n_max, "):", round(media_final, 4), "\n")
cat("Error absoluto:", round(error_abs, 4), "\n")
cat("Error relativo:", round(error_rel, 2), "%\n\n")

library(ggplot2)
library(gridExtra)

df <- data.frame(
  n = 1:n_max,
  media = media_acumulada,
  desviacion = abs(media_acumulada - mu)
)

p1 <- ggplot(df, aes(x = n, y = media)) +
  geom_line(color = "blue", size = 0.8) +
  geom_hline(yintercept = mu, color = "red", linetype = "dashed", size = 1) +
  labs(title = "Convergencia de la Media Muestral",
       x = "Tamaño de Muestra (n)", y = "Media Muestral") +
  theme_minimal()

p2 <- ggplot(df, aes(x = n, y = desviacion)) +
  geom_line(color = "darkgreen", size = 0.8) +
  scale_y_log10() +
  labs(title = "Velocidad de Convergencia (Escala Log)",
       x = "Tamaño de Muestra (n)", y = "Desviación Absoluta") +
  theme_minimal()

combined <- grid.arrange(p1, p2, ncol = 2)
ggsave("../figuras/convergencia_velocidad.pdf", combined, width = 12, height = 5)
cat("Gráfico guardado\n")
