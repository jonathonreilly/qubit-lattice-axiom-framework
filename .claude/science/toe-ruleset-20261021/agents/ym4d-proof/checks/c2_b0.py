#!/usr/bin/env python3
"""Check for Lemma L4b (PROOF.md): one-loop coefficient b0 = 11N/(48 pi^2).

Part A (exact algebra, continuum): with the Seeley-DeWitt coefficient a2 = tr[(1/12) Om_{mn} Om_{mn} + (1/2) E^2]
  (IMPORTED, Gilkey/Vassilevich), vector fluctuation operator -D^2 delta_{mn} + E_{mn}, E = 2i ad F (background-field
  Feynman gauge, IMPORTED form) and adjoint ghost -D^2:  (1/2) a2_vec - a2_gh = (11/12) C_A F^a F^a, C_A = N.
  Checked numerically for SU(2), SU(3), SU(4) with random F^a_{mn}.
Part B (lattice universality of the two log coefficients that enter):
  B1 (E^2 piece): int_BZ d^4k/(2pi)^4 (w(k)+m^2)^-2 = (1/16pi^2) ln(1/m^2) + c + o(1), w = sum(2 - 2 cos k).
  B2 (Om^2 piece): for a unit-charge lattice scalar in constant flux B in the (1,2) plane,
      [ln det(-Lap_B + m^2) - ln det(-Lap_0 + m^2)] / (Vol B^2) has ln(1/m^2)-slope -> 1/(96 pi^2)  (= -(1/12) tr Om^2 / (16 pi^2) / B^2).
Heat-kernel form: lattice 1D kernel e^{-2t} I0(2t) (exact), 2D magnetic part by exact diagonalisation (L x L torus, n flux quanta).
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, numpy as np
from scipy.special import ive
from scipy.integrate import quad
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(48)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
def gens(N):  # hermitian generators, tr(TaTb) = delta/2
    G = []
    for i in range(N):
        for j in range(i + 1, N):
            A = np.zeros((N, N), complex); A[i, j] = A[j, i] = .5; G.append(A)
            B = np.zeros((N, N), complex); B[i, j] = -.5j; B[j, i] = .5j; G.append(B)
    for k in range(1, N):
        D = np.zeros((N, N), complex); D[:k, :k] = np.eye(k); D[k, k] = -k; G.append(D / np.sqrt(2 * k * (k + 1)))
    return G
def adjoint(N):
    G = gens(N); n = len(G); f = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            C = G[a] @ G[b] - G[b] @ G[a]  # = i f_abc T_c
            for c in range(n): f[a, b, c] = np.real(-2j * np.trace(C @ G[c]))
    return f  # (ad T_a)_{bc} = -i f_abc
okA = True; msg = []; cs = []
for N in (2, 3, 4):
    f = adjoint(N); n = f.shape[0]; ad = -1j * f  # ad[a] matrix
    Fa = rng.normal(size=(4, 4, n)); Fa = Fa - Fa.transpose(1, 0, 2)
    adF = np.einsum("mna,abc->mnbc", Fa, ad)  # hermitian adjoint matrices
    Om = -1j * adF; F2 = np.sum(Fa ** 2)
    CA = np.real(np.trace(ad[0] @ ad[0])); trOm2 = np.real(np.einsum("mnij,mnji->", Om, Om))
    E = 2j * adF  # E_{mn} as (Lorentz x adjoint) blocks
    Emat = E.transpose(0, 2, 1, 3).reshape(4 * n, 4 * n)
    a2v = 4 * trOm2 / 12 + 0.5 * np.real(np.trace(Emat @ Emat)); a2g = trOm2 / 12
    c = (0.5 * a2v - a2g) / (CA * F2); cs.append(c); okA &= abs(CA - N) < 1e-12 and abs(c - 11 / 12) < 1e-12
    msg.append(f"SU({N}): C_A {CA:.6f}, ((1/2)a2v - a2gh)/(C_A F^2) = {c:.12f}")
check("A1 (1/2)a2_vec - a2_gh = (11/12) C_A F^aF^a and C_A = N for SU(2), SU(3), SU(4)", okA, "; ".join(msg))
b0s = [4 * c * N / (16 * np.pi ** 2) for c, N in zip(cs, (2, 3, 4))]  # 1/g^2(mu) = 1/g0^2 - 4 c C_A ln(Lam^2/mu^2)/(16 pi^2)
check("A2 b0 = 4 c C_A/(16 pi^2) with the measured c equals 11N/(48 pi^2) (derivation PROOF.md L4b)",
      all(abs(b - 11 * N / (48 * np.pi ** 2)) < 1e-14 for b, N in zip(b0s, (2, 3, 4))), "b0(SU2,SU3,SU4) = " + ", ".join(f"{b:.8f}" for b in b0s))
# B1
K1 = lambda t: ive(0, 2 * t)
def I2(m2):
    g = lambda t: t * np.exp(-t * m2) * K1(t) ** 4
    pts = np.concatenate([[0], np.logspace(-2, np.log10(60 / m2), 40)]); return sum(quad(g, a, b, limit=200)[0] for a, b in zip(pts[:-1], pts[1:]))
m2s = [4e-3, 2e-3, 1e-3, 5e-4]; v = [I2(x) for x in m2s]; sl1 = [(v[i + 1] - v[i]) / np.log(m2s[i] / m2s[i + 1]) for i in range(3)]
tgt1 = 1 / (16 * np.pi ** 2)
check("B1 lattice E^2 log coefficient: slope of int (w+m^2)^-2 vs ln(1/m^2) -> 1/(16 pi^2)", abs(sl1[-1] / tgt1 - 1) < 0.02,
      "slopes/target " + ", ".join(f"{s / tgt1:.4f}" for s in sl1))
# B2
L = 64
def mag_eigs(nq):
    B = 2 * np.pi * nq / L ** 2; V = L * L; H = np.zeros((V, V), complex); idx = lambda x, y: (x % L) * L + (y % L)
    for x in range(L):
        for y in range(L):
            i = idx(x, y); H[i, i] = 4
            ph = np.exp(-1j * B * L * y) if x == L - 1 else 1.0  # x-links: boundary twist
            j = idx(x + 1, y); H[i, j] -= ph; H[j, i] -= np.conj(ph)
            j = idx(x, y + 1); H[i, j] -= np.exp(1j * B * x); H[j, i] -= np.exp(-1j * B * x)
    return B, np.linalg.eigvalsh(H)
k = 2 * np.pi * np.arange(L) / L; lam0 = (2 - 2 * np.cos(k))[:, None] + (2 - 2 * np.cos(k))[None, :]; lam0 = lam0.ravel()
res = {}
for nq in (1, 2):
    B, lam = mag_eigs(nq); gauge_ok = abs(lam.sum() - lam0.sum()) < 1e-8
    def dG(m2):  # [ln det_B - ln det_0]/Vol = -int dt/t e^{-t m2} [tr_2D(e^{-t H_B}) - tr_2D(e^{-t H_0})]/L^2 * K1(t)^2
        g = lambda t: -np.exp(-t * m2) / t * (np.mean(np.exp(-t * lam)) - np.mean(np.exp(-t * lam0))) * K1(t) ** 2
        pts = np.concatenate([[1e-6], np.logspace(-2, np.log10(80 / m2), 50)]); return sum(quad(g, a, b, limit=200)[0] for a, b in zip(pts[:-1], pts[1:]))
    res[nq] = (B, {m2: dG(m2) for m2 in (0.064, 0.04, 0.025, 0.016)}, gauge_ok)
(B1, r1, g1), (B2, r2, g2) = res[1], res[2]
c2 = {m2: (r1[m2] * B2 ** 4 - r2[m2] * B1 ** 4) / (B1 ** 2 * B2 ** 4 - B2 ** 2 * B1 ** 4) for m2 in r1}  # Richardson: f = c2 B^2 + c4 B^4
ms = sorted(c2, reverse=True); sl2 = [(c2[ms[i + 1]] - c2[ms[i]]) / np.log(ms[i] / ms[i + 1]) for i in range(len(ms) - 1)]; tgt2 = 1 / (96 * np.pi ** 2)
check("B2 lattice Om^2 log coefficient: slope of [ln det_B - ln det_0]/(Vol B^2) vs ln(1/m^2) -> 1/(96 pi^2) within 10% (L=64 torus, 1-2 flux quanta; finite-size limited, FINITE DIAGNOSTIC)",
      g1 and g2 and max(abs(x / tgt2 - 1) for x in sl2) < 0.1, f"B = {B1:.5f}, {B2:.5f}; slopes/target " + ", ".join(f"{s / tgt2:.4f}" for s in sl2) + f"; trace check {g1 and g2}")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
