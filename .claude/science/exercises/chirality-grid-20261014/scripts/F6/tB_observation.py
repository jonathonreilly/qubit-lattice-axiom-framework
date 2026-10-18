"""T-B: what observation allows for mirror masses.  F6 route agent, 2026-10-14.

B1: index lemma, numerical illustration: a U(1)-invariant symmetric (Majorana) mass on left-handed Weyl
    fields keeps the chiral index n_q - n_{-q} of the massless set for every charge q; on vector-like
    content the massless set is vector-like.
B2: mirror families with masses from electroweak breaking: Peskin-Takeuchi S and the gg -> h rate.
"""
import numpy as np
from collections import Counter
from math import pi, asin, sqrt, log

rng = np.random.default_rng(7)

# ---------------- B1 ----------------
viol = 0
for trial in range(200):
    pos = list(rng.integers(1, 5, size=rng.integers(1, 7)))
    extra = list(rng.integers(-4, 5, size=rng.integers(0, 4)))  # optional chiral excess (index test)
    charges = pos + [-q for q in pos] + list(rng.integers(0, 1, size=rng.integers(0, 3))) + (extra if trial % 2 else [])
    n = len(charges)
    M = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(i, n):
            if charges[i] + charges[j] == 0 and rng.random() < 0.7:
                z = rng.normal() + 1j * rng.normal()
                M[i, j] = M[j, i] = z
    # massless Weyl fields = kernel of M (M is block diagonal in charge pairs, so the kernel is a U(1) subrep)
    kernel_count = Counter()
    for q in set(charges):
        iq = [i for i, c in enumerate(charges) if c == q]
        im = [i for i, c in enumerate(charges) if c == -q]
        B = M[np.ix_(iq, im)]
        r = np.linalg.matrix_rank(B, tol=1e-9) if B.size else 0
        kernel_count[q] = len(iq) - r
    ok = True
    for q in set(charges):
        idx_before = charges.count(q) - charges.count(-q)
        idx_after = kernel_count[q] - kernel_count.get(-q, 0)
        if idx_before != idx_after:
            ok = False
    if trial % 2 == 0:  # vector-like content: kernel must be vector-like
        for q in set(charges):
            if kernel_count[q] != kernel_count.get(-q, 0):
                ok = False
    viol += (not ok)
print(f"B1  index preserved and vector-like kernel on vector-like content: {200 - viol}/200 trials")

# ---------------- B2 ----------------
# Peskin-Takeuchi: one heavy degenerate chiral doublet with N_c colours gives S = N_c / (6 pi)
S_family = (3 + 1) / (6 * pi)
print(f"B2  S per mirror family (quark doublet N_c=3 + lepton doublet) = {S_family:.4f}")
# Gfitter 2013 (arXiv:1306.0571), U = 0: S = 0.05 +- 0.09 ; T = 0.08 +- 0.07
S0, dS = 0.05, 0.09
for nf, label in ((1, "one mirror family"), (2, "two (KS split: 2 x 16bar)"), (3, "three (walker hw split: net 3 x 16bar)")):
    S = nf * S_family
    print(f"B2  {label:42s} S = {S:.3f}  pull vs Gfitter U=0 fit = {(S - S0) / dS:.1f} sigma")

# Split doublets: heavy-limit S = N_c/(6 pi) [1 - Y ln(mU^2/mD^2)] (sign of Y term convention-dependent; scan both),
# T = N_c / (16 pi s^2 c^2 mZ^2) F(mU^2, mD^2), F(x,y) = (x+y)/2 - xy/(x-y) ln(x/y)
s2, mZ = 0.2312, 91.1876
c2 = 1 - s2
def F(x, y):
    return 0.0 if abs(x - y) < 1e-9 else (x + y) / 2 - x * y / (x - y) * log(x / y)
def ST_doublet(Nc, Y, mU, mD, sgn):
    S = Nc / (6 * pi) * (1 - sgn * Y * log(mU ** 2 / mD ** 2))
    T = Nc / (16 * pi * s2 * c2 * mZ ** 2) * F(mU ** 2, mD ** 2)
    return S, T
# chi^2 with correlation rho = +0.91 (Gfitter 2013, U = 0)
T0, dT, rho = 0.08, 0.07, 0.91
Cinv = np.linalg.inv(np.array([[dS ** 2, rho * dS * dT], [rho * dS * dT, dT ** 2]]))
best = None
masses = np.geomspace(400, 5000, 25)
for sgn in (+1, -1):
    for mUq in masses:
        for mDq in masses:
            for mUl in masses[::3]:
                for mDl in masses[::3]:
                    Sq, Tq = ST_doublet(3, 1 / 6, mUq, mDq, sgn)
                    Sl, Tl = ST_doublet(1, -1 / 2, mUl, mDl, sgn)
                    S, T = 3 * (Sq + Sl), 3 * (Tq + Tl)  # three identical mirror families
                    d = np.array([S - S0, T - T0])
                    chi2 = d @ Cinv @ d
                    if best is None or chi2 < best[0]:
                        best = (chi2, sgn, mUq, mDq, mUl, mDl, S, T)
print("B2  three mirror families, scan over splittings 0.4-5 TeV: min Delta chi^2 = %.1f at sgn=%+d mUq=%.0f mDq=%.0f mUl=%.0f mDl=%.0f (S=%.2f, T=%.2f)" % best)

# gg -> h: A_1/2(tau) = 2 [tau + (tau - 1) f(tau)] / tau^2, f = arcsin^2 sqrt(tau) for tau <= 1, heavy limit 4/3
def A12(m, mh=125.1):
    tau = mh ** 2 / (4 * m ** 2)
    if tau <= 1:
        f = asin(sqrt(tau)) ** 2
    else:
        b = sqrt(1 - 1 / tau)
        f = -0.25 * (complex(log((1 + b) / (1 - b)), -pi)) ** 2
    return 2 * (tau + (tau - 1) * f) / tau ** 2
A_SM = A12(172.5) + A12(4.8)
print(f"B2  A_1/2(top) = {A12(172.5):.4f}, A_1/2(b) = {A12(4.8):.4f}, A_SM = {A_SM:.4f}")
mus = []
for m in (400, 700, 1000, 1500, 2000, 3000):
    for nfam in (1, 3):
        A = A_SM + nfam * 2 * A12(m)  # each mirror family adds two heavy quarks with Yukawa-derived masses
        mu = abs(A) ** 2 / abs(A_SM) ** 2
        mus.append((nfam, m, mu))
        print(f"B2  {nfam} mirror famil{'y' if nfam == 1 else 'ies'}, m_Q = {m:5d} GeV: mu_ggF = {mu:.2f}")
print(f"B2  min mu_ggF over scan = {min(x[2] for x in mus):.2f}  (measured ~1.0 +- 0.1)")
