#!/usr/bin/env python3
"""Probe G1b: Hamiltonian rank-2 lattice gauge carrier (continuous time, spatial O_h only,
linearised spatial-diffeo Gauss law delta A_ij = k_i xi_j + k_j xi_i).
H = E.G.E + A.K(k).A.  K: the unique O_h+gauge-invariant two-derivative magnetic form (from G1).
G: general O_h-invariant ultralocal electric metric = g1*Id + g2*tr(x)tr + g3*D, D_ijkl = delta_ijkl.
SO(3) allows only g1, g2; g3 is the extra cubic invariant (not constrained by gauge invariance,
which acts on A only). Report TT mode speeds omega^2/k^2 by direction."""
import numpy as np
from probe_spin2_hypercubic_isotropy import count_forms
_, n, B = count_forms(3, 2, "hyperoctahedral"); assert n == 1
T = B[:, 0].reshape((3,) * 6)
pairs = [(i, j) for i in range(3) for j in range(i, 3)]
def basis(i, j):
    M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1.0
    return M / np.linalg.norm(M)
Eb = [basis(i, j) for i, j in pairs]
def Kmat(k):
    Kt = np.einsum("abcdef,e,f->abcd", T, k, k)
    return np.array([[np.einsum("ab,abcd,cd", X, Kt, Y) for Y in Eb] for X in Eb])
def Gmat(g1, g2, g3):
    G = np.zeros((6, 6))
    for a, X in enumerate(Eb):
        for b, Y in enumerate(Eb):
            G[a, b] = g1 * np.sum(X * Y) + g2 * np.trace(X) * np.trace(Y) + g3 * np.sum(np.diag(X) * np.diag(Y))
    return G
def speeds(g, k):
    K = Kmat(k); K = K / (np.trace(Kmat(np.array([1., 0, 0]))) / 1.0)
    w = np.linalg.eigvals(Gmat(*g) @ K)
    w = np.sort(np.real(w))
    return w[w > 1e-9] / (k @ k)
dirs = {"[100]": [1, 0, 0], "[110]": [1, 1, 0], "[111]": [1, 1, 1], "[210]": [2, 1, 0]}
for g in [(1, 0, 0), (1, -0.3, 0), (1, 0, 0.1), (1, 0, 0.3)]:
    print(f"G=(g1,g2,g3)={g}")
    for name, v in dirs.items():
        k = np.array(v, float); k /= np.linalg.norm(k)
        print(f"   {name}: nonzero omega^2/k^2 = {np.round(speeds(g, k), 5)}")
