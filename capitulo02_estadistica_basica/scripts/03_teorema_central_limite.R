# ==============================================================================
# CAPÍTULO 2: TEOREMA CENTRAL DEL LÍMITE
# ==============================================================================

cat("=== TEOREMA CENTRAL DEL LÍMITE ===\n\n")
set.seed(123)

n_muestra <- 30
m_replicas <- 1000

cat("--- Distribución Uniforme(0, 10) ---\n")
medias_unif <- replicate(m_replicas, mean(runif(n_muestra, 0, 10)))
z_unif <- sqrt(n_muestra) * (medias_unif - 5) / sqrt(100/12)
shapiro_unif <- shapiro.test(z_unif)
cat("Shapiro-Wilk: W =", round(shapiro_unif$statistic, 4), 
    ", p-valor =", round(shapiro_unif$p.value, 4), "\n\n")

cat("--- Distribución Exponencial(λ=1) ---\n")
medias_exp <- replicate(m_replicas, mean(rexp(n_muestra, rate = 1)))
z_exp <- sqrt(n_muestra) * (medias_exp - 1) / 1
shapiro_exp <- shapiro.test(z_exp)
cat("Shapiro-Wilk: W =", round(shapiro_exp$statistic, 4), 
    ", p-valor =", round(shapiro_exp$p.value, 4), "\n\n")

cat("--- Distribución Binomial(n=10, p=0.5) ---\n")
medias_binom <- replicate(m_replicas, mean(rbinom(n_muestra, 10, 0.5)))
z_binom <- sqrt(n_muestra) * (medias_binom - 5) / sqrt(2.5)
shapiro_binom <- shapiro.test(z_binom)
cat("Shapiro-Wilk: W =", round(shapiro_binom$statistic, 4), 
    ", p-valor =", round(shapiro_binom$p.value, 4), "\n\n")

cat("--- Distribución Chi-cuadrado(df=3) ---\n")
medias_chisq <- replicate(m_replicas, mean(rchisq(n_muestra, df = 3)))
z_chisq <- sqrt(n_muestra) * (medias_chisq - 3) / sqrt(6)
shapiro_chisq <- shapiro.test(z_chisq)
cat("Shapiro-Wilk: W =", round(shapiro_chisq$statistic, 4), 
    ", p-valor =", round(shapiro_chisq$p.value, 4), "\n\n")

library(ggplot2)

df_combined <- data.frame(
  z = c(z_unif, z_exp, z_binom, z_chisq),
  distribucion = rep(c("Uniforme", "Exponencial", "Binomial", "Chi-cuadrado"), 
                     each = m_replicas)
)

p <- ggplot(df_combined, aes(x = z)) +
  geom_histogram(aes(y = after_stat(density)), bins = 30, 
                 fill = "lightblue", color = "black", alpha = 0.7) +
  stat_function(fun = dnorm, args = list(mean = 0, sd = 1),
                color = "red", size = 1) +
  facet_wrap(~ distribucion, scales = "free") +
  labs(title = "Teorema Central del Límite: Normalidad Asintótica",
       x = "Z estandarizada", y = "Densidad") +
  theme_minimal()

ggsave("../figuras/tcl_normalidad.pdf", p, width = 12, height = 8)
cat("Gráfico guardado\n")
