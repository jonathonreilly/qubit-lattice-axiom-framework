"""TW-3 cross-lane check: does the generation lane's Wilson-type term M_W = d I - H_K0/2
(docs/THE_GENERATION_COUNT_..._2026-09-03.md, sec. 1) keep NF-1's protecting pair (Theta, P_stag)?
One-particle level on the L=4 periodic 3D torus (one complex mode per site).
Theta (antiunitary K, chi_x -> eps_x chi_x^dag): for H = chi^dag h chi, Theta H Theta^-1 = const - chi^dag (eps h^dag eps)^T... 
i.e. one-particle h -> -eps h eps (h Hermitian); invariance <=> {eps, h} = 0 (onsite constants aside).  P_stag (unitary, chi(x) -> eps_x chi(-x)): h -> (eps I) h (I eps)."""
import numpy as np
L, d = 4, 3
N = L ** d
idx = lambda x: ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
sites = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]
eps = np.diag([(-1) ** (sum(x)) for x in sites]).astype(complex)
Inv = np.zeros((N, N))
for x in sites:
    Inv[idx([-v for v in x]), idx(x)] = 1
def eta(mu, x):
    return (-1) ** sum(x[:mu])
T = []
for mu in range(d):
    M = np.zeros((N, N), complex)
    for x in sites:
        y = list(x); y[mu] += 1
        M[idx(y), idx(x)] = 1          # T_mu|x> = |x+mu>
    T.append(M)
Eta = [np.diag([eta(mu, x) for x in sites]) for mu in range(d)]
HK1 = sum(1j * Eta[mu] @ (T[mu] - T[mu].conj().T) for mu in range(d))
HK1 = (HK1 + HK1.conj().T) / 2
HK0 = sum(T[mu] + T[mu].conj().T for mu in range(d))
MW = d * np.eye(N) - HK0 / 2
def theta_res(h):   # || eps h eps + h ||
    return np.abs(eps @ h @ eps + h).max()
def pstag_res(h):
    return np.abs(eps @ Inv @ h @ Inv.T @ eps - h).max()
for name, h in (("H_K1", HK1), ("H_K0", HK0), ("I (onsite)", np.eye(N)), ("M_W", MW), ("H_K1+0.1 M_W", HK1 + 0.1 * MW)):
    print(f"{name:14s}: Theta residual {theta_res(h):.2e}   P_stag residual {pstag_res(h):.2e}")
