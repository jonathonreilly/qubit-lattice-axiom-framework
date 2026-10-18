#!/usr/bin/env python3
"""Step 2: validate the open-path (guide-free) worldline QMC against exact L=2 results on the 864-state
canonical flip component, at V in {0, 0.5, 0.9} and several projection times T; plus the periodic-trace
control (local moves only) against the exact thermal trace on the same component.

Exact references (independent path: dense diagonalisation, no sampling):
  open: psi_T(tau) = e^{-tau H} 1;  <O>_mid = sum psi(T/2)^2 O / sum psi(T/2)^2;
        E_mix = <1|H e^{-TH}|1>/Z;  kin_mid = (1/2w) int_{T/2-w}^{T/2+w} g <A(tau)> dtau (Gauss-Legendre);
        C(tau) from e^{-tau H} between diagonal Fourier operators.
  periodic: Tr(O e^{-beta H})/Tr e^{-beta H} on the component.
Pass rule (declared in WORKLOG before running): |QMC - exact| <= 3 sigma for each observable.
"""
import os, sys, time, json
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

sys.path.insert(0, os.path.dirname(__file__))
from lattice import Lattice
from driver import config_obs, st_kmin, run

RES = []
LOG = open(os.path.join(os.path.dirname(__file__), "..", "logs", "step2_validate_L2.jsonl"), "w")


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""), flush=True)


def component(lat):
    """BFS from the canonical state over plaquette flips."""
    s = lat.canonical()
    seen = {tuple(s): 0}
    lst = [s]
    edges = []
    i = 0
    while i < len(lst):
        c = lst[i]
        fl = lat.flippable(c)
        for p in np.flatnonzero(fl):
            t = c.copy()
            t[lat.plinks[p]] *= -1
            k = tuple(t)
            if k not in seen:
                seen[k] = len(lst)
                lst.append(t)
            edges.append((i, seen[k]))
        i += 1
    S = np.array(lst)
    e = np.array(edges)
    A = csr_matrix((np.ones(len(e)), (e[:, 0], e[:, 1])), shape=(len(S), len(S))).toarray()
    return S, A


lat = Lattice(2)
S, A = component(lat)
check("L=2 canonical flip component has 864 states, A symmetric 0/1", len(S) == 864 and np.all(A == A.T) and A.max() == 1)
PE, Pn, Nf, Ek = config_obs(lat, S)
ST1 = st_kmin(PE, 2, 1)
# k_a = pi e_a transverse Fourier components for correlator
Ekm = []
for a in range(3):
    idx = [0, 0, 0]
    idx[a] = 1
    for b in range(3):
        if b != a:
            Ekm.append(Ek[:, idx[0], idx[1], idx[2], b])
Ekm = np.array(Ekm)  # (6, 864)

# anchor for the measurement code: repo 2026-09-04 note, V=0 ground state S_yy=S_zz=0.25303701 at (pi,0,0)
H0 = -A
ev, U = np.linalg.eigh(H0)
gs = U[:, 0]
pyy = (gs ** 2 * PE[:, 1, 0, 0, 1]).sum()
check("measurement anchor: V=0 ground state S_yy(pi,0,0) = 0.25303701 (repo 09-04 note)", abs(pyy - 0.25303701) < 1e-7,
      f"{pyy:.8f}; E0 = {ev[0]:.10f}")


def exact_open(V, T, J, dtau, g=1.0):
    H = V * np.diag(Nf) - g * A
    lam, U = np.linalg.eigh(H)
    a = U.T @ np.ones(len(S))
    prop = lambda tau, v: U @ (np.exp(-tau * (lam - lam[0])) * (U.T @ v))
    one = np.ones(len(S))
    Z = (a ** 2 * np.exp(-T * (lam - lam[0]))).sum()
    psi = prop(T / 2, one)
    w = psi ** 2 / (psi ** 2).sum()
    out = {"Nf_mid": (w * Nf).sum(), "ST1": (w * ST1).sum()}
    out["Emix"] = (a ** 2 * lam * np.exp(-T * (lam - lam[0]))).sum() / Z
    out["Nf_end"] = (prop(T, one) * Nf).sum() / Z
    # kinetic in window via Gauss-Legendre
    wwin = T / 8
    x, wt = np.polynomial.legendre.leggauss(24)
    taus = T / 2 + wwin * x
    vals = []
    EH = (a ** 2 * lam * np.exp(-T * (lam - lam[0]))).sum()
    for tau in taus:
        phi = prop(tau, one)
        chi = prop(T - tau, one)
        dterm = (chi * Nf * phi).sum()
        vals.append((V * dterm - EH) / Z)  # = g <A(tau)>
    out["kin_mid"] = 0.5 * (wt * np.array(vals)).sum()
    # correlator
    C = []
    for j in range(J + 1):
        tau = j * dtau
        c = 0.0
        for k in range(Ekm.shape[0]):
            o = Ekm[k]
            # symmetric: average of (tm, tm+tau) and (tm-tau, tm)
            for ta in (T / 2, T / 2 - tau):
                pa = prop(ta, one)
                cb = prop(T - ta - tau, one)
                c += 0.5 * np.real((np.conj(o) * cb) @ prop(tau, o * pa)) / Z
        C.append(c / lat.nv)
    out["C"] = C
    return out


def exact_thermal(V, beta, g=1.0):
    H = V * np.diag(Nf) - g * A
    lam, U = np.linalg.eigh(H)
    bw = np.exp(-beta * (lam - lam[0]))
    Z = bw.sum()
    rho = (U ** 2) @ bw / Z  # diagonal of density matrix
    return {"Nf_mid": (rho * Nf).sum(), "ST1": (rho * ST1).sum(), "E": (lam * bw).sum() / Z}


J, dtau = 4, 0.25
cases = [(0.0, 1.0), (0.0, 4.0), (0.0, 8.0), (0.5, 2.0), (0.5, 6.0), (0.9, 3.0), (0.9, 8.0)]
seed = 100
for V, T in cases:
    ex = exact_open(V, T, J, dtau)
    seed += 1
    t0 = time.time()
    r = run(2, V, T, nsweep=60000, ntherm=3000, seed=seed, mode=0, J=J, dtau=dtau, factor=2.0, log=LOG)
    ok_all = True
    det = []
    for k in ("Nf_mid", "ST1", "Emix", "kin_mid", "Nf_end"):
        m, se = r[k]
        z = (m - ex[k]) / se
        ok_all &= abs(z) <= 3
        det.append(f"{k} {m:.4f}+-{se:.4f} vs {ex[k]:.4f} (z={z:+.1f})")
    for j in (1, J):
        m, se = r["C"][j]
        z = (m - ex["C"][j]) / se
        ok_all &= abs(z) <= 3
        det.append(f"C({j*dtau}) {m:.4f}+-{se:.4f} vs {ex['C'][j]:.4f} (z={z:+.1f})")
    ok_all &= r["gauss_or_path_failures"] == 0 and r["valid_final"]
    check(f"open-path QMC vs exact, L=2 V={V} T={T}", ok_all, "; ".join(det) + f"; {time.time()-t0:.0f}s")

# periodic control (local moves only): expected to be class-restricted
for V, beta in [(0.0, 1.0), (0.0, 4.0), (0.5, 4.0)]:
    ex = exact_thermal(V, beta)
    seed += 1
    r = run(2, V, beta, nsweep=60000, ntherm=3000, seed=seed, mode=1, factor=2.0, log=LOG)
    det = []
    zs = []
    for k, ek in (("Nf_mid", "Nf_mid"), ("ST1", "ST1")):
        m, se = r[k]
        z = (m - ex[ek]) / se
        zs.append(abs(z))
        det.append(f"{k} {m:.4f}+-{se:.4f} vs thermal {ex[ek]:.4f} (z={z:+.1f})")
    Eq = V * r["Nf_mid"][0] - r["kin_mid"][0]
    det.append(f"E {Eq:.4f} vs thermal {ex['E']:.4f}")
    print(f"[INFO] periodic local-move control L=2 V={V} beta={beta}: " + "; ".join(det)
          + f"; path valid {r['valid_final']}", flush=True)

print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES)-sum(RES)}")
