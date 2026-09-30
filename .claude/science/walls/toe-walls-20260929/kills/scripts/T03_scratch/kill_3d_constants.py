"""Numerical check of the constants used in kill_grw_csl_arithmetic.py section 3.
(i) <|s|> = BZ average of sqrt(sum sin^2 k_j)  (repo: 1.19);  (ii) int |grad g|^2 = 3/(16 pi^{3/2} r_C^5) and int g^2 = (4 pi r_C^2)^{-3/2}
for the normalised 3D Gaussian g (variance r_C^2 per axis);  (iii) (1/2) gamma int|grad g|^2 with gamma = lambda (4 pi r_C^2)^{3/2} = (3/4) lambda / r_C^2 * ...
"""
import numpy as np
n = 96
k = 2 * np.pi * (np.arange(n) + 0.5) / n
K = np.meshgrid(k, k, k, indexing="ij")
s = np.sqrt(sum(np.sin(x) ** 2 for x in K))
print("<|s|> =", s.mean())
# Gaussian integrals on a grid
rC = 1.0; L = 12.0; m = 241
x = np.linspace(-L, L, m); dx = x[1] - x[0]
X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
g = (2 * np.pi * rC ** 2) ** -1.5 * np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (2 * rC ** 2))
gx, gy, gz = np.gradient(g, dx)
I_grad = ((gx ** 2 + gy ** 2 + gz ** 2).sum()) * dx ** 3
I_g2 = (g ** 2).sum() * dx ** 3
print("int|grad g|^2 =", I_grad, " analytic", 3 / (16 * np.pi ** 1.5))
print("int g^2 =", I_g2, " analytic", (4 * np.pi) ** -1.5)
lam = 1.0
gamma = lam / I_g2
print("(1/2) gamma int|grad g|^2 =", 0.5 * gamma * I_grad, " expected (3/4) lambda / r_C^2 =", 0.75)
