"""V0b: closed form (general sigma branch) vs independent builder on unrestricted (non-admissible) configurations."""
import numpy as np
from t22lib import *
delta = 0.6; rng = np.random.default_rng(11)
P = rng.uniform(-np.pi, np.pi, (60, 3))
L = build_links(P[:, 0], P[:, 1], P[:, 2], rng.uniform(-0.5, 0.5, 60), rng.uniform(-0.5, 0.5, 60), rng=rng)
Kc = kernel_matrix_closed(L, delta); Ki = kernel_matrix_indep(L, delta)
print("unrestricted pool: max|closed - indep| =", np.abs(Kc - Ki).max(), " max K", Kc.max(), " nonzero frac", (Ki > 0).mean())
P = sample_plaq(60, 0.55, rng)
L = build_links(P[:, 0], P[:, 1], P[:, 2], rng.uniform(-0.5, 0.5, 60), rng.uniform(-0.5, 0.5, 60), rng=rng)
Kc = kernel_matrix_closed(L, delta); Ki = kernel_matrix_indep(L, delta)
print("admissible pool:   max|closed - indep| =", np.abs(Kc - Ki).max(), " max K", Kc.max(), " nonzero frac", (Ki > 0).mean())
