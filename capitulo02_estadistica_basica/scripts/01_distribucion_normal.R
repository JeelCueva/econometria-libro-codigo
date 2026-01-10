# ============================================
# Modulo 1: Validacion de Distribucion Normal
# ============================================

# Configuracion
set.seed(123)
n <- 1000

# Generar datos N(0,1)
x <- rnorm(n, mean = 0, sd = 1)

# Estadisticas descriptivas
estadisticas <- data.frame(
  Estadistico = c("Media", "Desv.Est.", "Asimetria", "Curtosis"),
  Valor = c(
    mean(x),
    sd(x),
    moments::skewness(x),
    moments::kurtosis(x)
  ),
  Teorico = c(0, 1, 0, 3)
)

print(estadisticas)

# Prueba de normalidad Shapiro-Wilk
shapiro_test <- shapiro.test(x)
cat("\nShapiro-Wilk Test:\n")
cat("W =", shapiro_test$statistic, "\n")
cat("p-value =", shapiro_test$p.value, "\n")

# Probabilidades y cuantiles
prob_menor_196 <- pnorm(1.96)
prob_entre_196 <- pnorm(1.96) - pnorm(-1.96)
q_025 <- qnorm(0.025)
q_975 <- qnorm(0.975)

cat("\nProbabilidades y Cuantiles:\n")
cat("P(Z <= 1.96) =", prob_menor_196, "\n")
cat("P(-1.96 <= Z <= 1.96) =", prob_entre_196, "\n")
cat("Cuantil 2.5% =", q_025, "\n")
cat("Cuantil 97.5% =", q_975, "\n")

# Visualizacion en RStudio
library(ggplot2)

# Figura 1: Histograma vs densidad teorica
p1 <- ggplot(data.frame(x = x), aes(x = x)) +
  geom_histogram(aes(y = after_stat(density)), 
                 bins = 30, fill = "orange", 
                 color = "black", alpha = 0.7) +
  stat_function(fun = dnorm, args = list(mean = 0, sd = 1),
                color = "red", size = 1.2) +
  labs(title = "Histograma vs Densidad Teorica N(0,1)",
       x = "Valor", y = "Densidad") +
  theme_minimal()

# Mostrar primera figura en panel de plots
print(p1)

# Pausa para ver la primera gráfica (opcional)
cat("\nPresiona Enter para ver la siguiente gráfica...")
invisible(readline())

# Figura 2: Q-Q plot
p2 <- ggplot(data.frame(x = x), aes(sample = x)) +
  stat_qq() +
  stat_qq_line(color = "red", size = 1) +
  labs(title = "Grafico Q-Q Normal",
       x = "Cuantiles Teoricos", y = "Cuantiles Muestrales") +
  theme_minimal()

# Mostrar segunda figura en panel de plots
print(p2)

# Opción alternativa: Mostrar ambas en una sola ventana
# Si prefieres ver las dos gráficas juntas, puedes usar grid.arrange
cat("\n\n¿Quieres ver ambas gráficas juntas? (s/n): ")
respuesta <- readline()

if (tolower(respuesta) == "s") {
  library(gridExtra)
  p_combinado <- grid.arrange(p1, p2, ncol = 2)
  print(p_combinado)
}
