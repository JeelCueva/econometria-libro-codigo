# ==============================================================================
# CAPÍTULO 2: PRUEBA DE HIPÓTESIS
# ==============================================================================

cat("=== PRUEBA DE HIPÓTESIS (Prueba t) ===\n\n")
set.seed(123)

n <- 25
mu_hipotetico <- 100
datos <- rnorm(n, mean = 105, sd = 15)

x_barra <- mean(datos)
s <- sd(datos)

cat("n =", n, "\n")
cat("X̄ =", round(x_barra, 2), "\n")
cat("s =", round(s, 2), "\n\n")

cat("H₀: μ =", mu_hipotetico, "\n")
cat("H₁: μ ≠", mu_hipotetico, "\n\n")

t_stat <- (x_barra - mu_hipotetico) / (s / sqrt(n))
df <- n - 1
t_critico <- qt(0.975, df)
p_valor <- 2 * pt(-abs(t_stat), df)

cat("Estadístico t =", round(t_stat, 3), "\n")
cat("Valor crítico =", round(t_critico, 3), "\n")
cat("P-valor =", round(p_valor, 4), "\n\n")

if (p_valor < 0.05) {
  cat("Decisión: RECHAZAR H₀\n\n")
} else {
  cat("Decisión: NO RECHAZAR H₀\n\n")
}

ic_lower <- x_barra - t_critico * (s / sqrt(n))
ic_upper <- x_barra + t_critico * (s / sqrt(n))

cat("IC 95%: [", round(ic_lower, 2), ",", round(ic_upper, 2), "]\n\n")

library(ggplot2)

t_seq <- seq(-4, 4, length.out = 500)
dt_vals <- dt(t_seq, df)

df_plot <- data.frame(t = t_seq, densidad = dt_vals)

p <- ggplot(df_plot, aes(x = t, y = densidad)) +
  geom_line(size = 1.2, color = "blue") +
  geom_area(data = subset(df_plot, t < -t_critico), 
            aes(x = t, y = densidad), fill = "red", alpha = 0.3) +
  geom_area(data = subset(df_plot, t > t_critico), 
            aes(x = t, y = densidad), fill = "red", alpha = 0.3) +
  geom_vline(xintercept = t_stat, color = "darkgreen", 
             linetype = "dashed", size = 1.2) +
  labs(title = "Distribución t y Regiones de Rechazo") +
  theme_minimal()

ggsave("../figuras/prueba_t_ic.pdf", p, width = 10, height = 6)
cat("Gráfico guardado\n")
