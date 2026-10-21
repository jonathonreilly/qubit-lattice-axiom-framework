#!/usr/bin/env python3
"""Step 3 (added at resumption, 2026-10-18 ~23:00 UTC): validate the electric-winding (W=1) sector path of the
production code against exact diagonalisation at L=2.

Why: the load-bearing observable of the block is dE = E_mix(W=1) - E_mix(W=0). Step 2 validated only the W=0
(canonical) component. Production W=1 chains use driver.Sim with seed >= 100 (canonical state with the directed
x-line (y=0,z=0) reversed). Here the exact reference is built independently: BFS over plaquette flips from that
same start state (no QMC code), dense diagonalisation, and E_mix(T) = <1|H e^{-TH}|1>/<1|e^{-TH}|1>.

Pass rule (declared here before running, same rule as step 2): |QMC - exact| <= 3 sigma for E_mix, Nf_mid and
Nf_end, sigma = max(seed scatter/sqrt(n), combined binned SE) over 4 independent chains; zero path/Gauss failures.
Info lines (not pass/fail): exact L=2 component sizes and exact E0(W=1) - E0(W=0) at V = 0, 0.5.
"""
import os, sys, time
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from lattice import Lattice
from driver import run

RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""), flush=True)


def component(lat, s):
    seen = {tuple(s): 0}
    lst = [s]
    edges = []
    i = 0
    while i < len(lst):
        c = lst[i]
        for p in np.flatnonzero(lat.flippable(c)):
            t = c.copy()
            t[lat.plinks[p]] *= -1
            k = tuple(t)
            if k not in seen:
                seen[k] = len(lst)
                lst.append(t)
            edges.append((i, seen[k]))
        i += 1
    S = np.array(lst)
    A = np.zeros((len(S), len(S)))
    for a, b in edges:
        A[a, b] = 1.0
    return S, A


L = 2
lat = Lattice(L)
s0 = lat.canonical().copy()
s1 = s0.copy()
for x in range(L):  # same construction as driver.Sim for seed >= 100, written out independently
    l = 3 * lat.vid(np.array([x, 0, 0])) + 0
    s1[l] = -s1[l]
check("W=1 start state satisfies Gauss law", np.all(lat.div(s1) == 0))
S0, A0 = component(lat, s0)
S1, A1 = component(lat, s1)
inter = len(set(map(tuple, S0)) & set(map(tuple, S1)))
check("W=0 and W=1 components are disjoint; W=0 component has 864 states", inter == 0 and len(S0) == 864,
      f"|W=0| = {len(S0)}, |W=1| = {len(S1)}, overlap {inter}")
Nf0 = np.array([lat.flippable(c).sum() for c in S0], float)
Nf1 = np.array([lat.flippable(c).sum() for c in S1], float)


def exact(Nf, A, V, T, g=1.0):
    H = V * np.diag(Nf) - g * A
    lam, U = np.linalg.eigh(H)
    one = np.ones(len(Nf))
    a = U.T @ one
    wgt = a ** 2 * np.exp(-T * (lam - lam[0]))
    Z = wgt.sum()
    prop = lambda tau, v: U @ (np.exp(-tau * (lam - lam[0])) * (U.T @ v))
    psi = prop(T / 2, one)
    w = psi ** 2 / (psi ** 2).sum()
    return {"E0": lam[0], "Emix": (wgt * lam).sum() / Z, "Nf_mid": (w * Nf).sum(), "Nf_end": (prop(T, one) * Nf).sum() / Z}


for V in (0.0, 0.5):
    e0 = exact(Nf0, A0, V, 50.0)["E0"]
    e1 = exact(Nf1, A1, V, 50.0)["E0"]
    print(f"[INFO] exact L=2 V={V}: E0(W=0) = {e0:.10f}, E0(W=1) = {e1:.10f}, dE = {e1-e0:.10f}", flush=True)


def comb(vals):
    m = np.array([v[0] for v in vals])
    s = np.array([v[1] for v in vals])
    return m.mean(), max(m.std(ddof=1) / np.sqrt(len(m)), np.sqrt((s ** 2).sum()) / len(m))


seed = 200  # seeds 201..: W=1 line start (seed >= 100, seed % 100 < 11)
for V, T in [(0.0, 4.0), (0.5, 4.0)]:
    ex = exact(Nf1, A1, V, T)
    t0 = time.time()
    rs = []
    for k in range(4):
        seed += 1
        rs.append(run(L, V, T, nsweep=40000, ntherm=4000, seed=seed, mode=0, J=4, dtau=0.25, factor=2.0))
    ok = all(r["gauss_or_path_failures"] == 0 and r["valid_final"] for r in rs)
    det = []
    for key in ("Emix", "Nf_mid", "Nf_end"):
        m, se = comb([r[key] for r in rs])
        z = (m - ex[key]) / se
        ok &= abs(z) <= 3
        det.append(f"{key} {m:.4f}+-{se:.4f} vs {ex[key]:.4f} (z={z:+.1f})")
    check(f"W=1 open-path QMC vs exact, L=2 V={V} T={T} (4 chains)", ok, "; ".join(det) + f"; {time.time()-t0:.0f}s")

print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES)-sum(RES)}")
