"""B2b: F2 point body at threshold: ledger, radial profile of the rate, and comparison with F1 saturation."""
import numpy as np
from B2_second_bond_energy import make, solve_field, energy
L = 41; G = make(L); W = np.ones(G["n"])
for w0 in [0.5, 0.1, 0.01, 1e-3, 1e-4, 1e-6]:
    W[G["centre"]] = w0
    W, it, gn = solve_field(W, G)
nb = np.array([W[G["centre"] + s] for s in G["shifts"]])
m = -np.sum(1 - 4*nb*nb/(1e-6+nb)**2)
led = m*1e-6 + energy(W, L)
print(f"F2 point body at w0=1e-6: m={m:.6f} (18), ledger m*w0+F = {led:.4f};  simplest-energy (F1) single-site ledger bound 12/(gamma g0) = {12/1.49551:.3f}")
c = G["c"]; W3 = W.reshape(L, L, L)
print("rate along axis, n = 0..8 sites from the stopped site:", " ".join(f"{W3[c+n,c,c]:.4f}" for n in range(9)))
print("phi=sqrt(w) along axis:", " ".join(f"{np.sqrt(W3[c+n,c,c]):.4f}" for n in range(9)))
