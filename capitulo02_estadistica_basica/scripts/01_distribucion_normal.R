# ==============================================================================
# CAPÍTULO 2: DISTRIBUCIÓN NORMAL ESTÁNDAR
# ==============================================================================

cat("=== DISTRIBUCIÓN NORMAL ESTÁNDAR ===\n\n")
set.seed(123)

n <- 1000
muestra <- rnorm(n, mean = 0, sd = 1)

media_muestral <- mean(muestra)
sd_muestral <- sd(muestra)
library(moments)
asimetria <- skewness(muestra)
curtosis <- kurtosis(muestra)

cat("Media muestral:", round(media_muestral, 4), "\n")
cat("Desviación estándar:", round(sd_muestral, 4), "\n")
cat("Asimetría:", round(asimetria, 4), "\n")
cat("Curtosis:", round(curtosis, 4), "\n\n")

shapiro_test <- shapiro.test(muestra)
cat("Prueba Shapiro-Wilk:\n")
cat("Estadístico W:", round(shapiro_test$statistic, 4), "\n")
cat("P-valor:", round(shapiro_test$p.value, 4), "\n\n")

prob_1.96 <- pnorm(1.96)
prob_intervalo <- pnorm(1.96) - pnorm(-1.96)
cat("P(Z ≤ 1.96) =", round(prob_1.96, 4), "\n")
cat("P(-1.96 ≤ Z ≤ 1.96) =", round(prob_intervalo, 4), "\n\n")

library(ggplot2)
library(gridExtra)

p1 <- ggplot(data.frame(x = muestra), aes(x = x)) +
  geom_histogram(aes(y = after_stat(density)), bins = 30,
                 fill = "lightblue", color = "black", alpha = 0.7) +
  stat_function(fun = dnorm, args = list(mean = 0, sd = 1),
                color = "red", size = 1.5) +
  labs(title = "Histograma vs. Densidad Teórica",
       x = "Valores", y = "Densidad") +
  theme_minimal()

p2 <- ggplot(data.frame(muestra), aes(sample = muestra)) +
  stat_qq() + stat_qq_line(color = "red", size = 1) +
  labs(title = "Q-Q Plot Normal") +
  theme_minimal()

combined <- grid.arrange(p1, p2, ncol = 2)
ggsave("../figuras/histograma_vs_densidad_qq.pdf", combined, width = 12, height = 5)
cat("Gráfico guardado\n")
