# ==============================================================================
# CAPÍTULO 2: MÁXIMA VEROSIMILITUD
# ==============================================================================

cat("=== ESTIMACIÓN POR MÁXIMA VEROSIMILITUD ===\n\n")
set.seed(123)

n <- 100
mu_verdadero <- 10
sigma_verdadero <- 2
datos <- rnorm(n, mean = mu_verdadero, sd = sigma_verdadero)

mu_hat <- mean(datos)
sigma_hat_sesgado <- sqrt(sum((datos - mu_hat)^2) / n)
sigma_hat_insesgado <- sd(datos)

cat("--- Estimadores MLE ---\n")
cat("μ̂ (MLE) =", round(mu_hat, 4), "\n")
cat("σ̂ sesgado =", round(sigma_hat_sesgado, 4), "\n")
cat("σ̂ insesgado =", round(sigma_hat_insesgado, 4), "\n\n")

se_mu <- sigma_hat_insesgado / sqrt(n)
se_sigma <- sigma_hat_insesgado / sqrt(2 * n)

cat("SE(μ̂) =", round(se_mu, 4), "\n")
cat("SE(σ̂) =", round(se_sigma, 4), "\n\n")

ic_mu_lower <- mu_hat - 1.96 * se_mu
ic_mu_upper <- mu_hat + 1.96 * se_mu

cat("IC 95% para μ: [", round(ic_mu_lower, 3), ",", round(ic_mu_upper, 3), "]\n\n")

library(ggplot2)

mu_seq <- seq(mu_hat - 1, mu_hat + 1, length.out = 50)
sigma_seq <- seq(sigma_hat_sesgado - 0.5, sigma_hat_sesgado + 0.5, length.out = 50)

loglik_surface <- expand.grid(mu = mu_seq, sigma = sigma_seq)
loglik_surface$loglik <- apply(loglik_surface, 1, function(params) {
  sum(dnorm(datos, mean = params[1], sd = params[2], log = TRUE))
})

p <- ggplot(loglik_surface, aes(x = mu, y = sigma, z = loglik)) +
  geom_contour(aes(color = after_stat(level)), bins = 20, size = 0.8) +
  geom_point(aes(x = mu_hat, y = sigma_hat_sesgado), 
             color = "red", size = 4, shape = 18) +
  labs(title = "Superficie de Log-Verosimilitud") +
  theme_minimal()

ggsave("../figuras/superficie_verosimilitud.pdf", p, width = 8, height = 6)
cat("Gráfico guardado\n")
