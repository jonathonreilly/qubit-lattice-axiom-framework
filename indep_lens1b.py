#!/usr/bin/env python3
"""LENS 1 (a),(c),(d): headline events, E1 ratios, E2 bimodal rows, aggregation.
Reuses the independent scan (explicit bit tracking) from indep_lens1.py logic but
conditions families via the EXPLICIT chronological bitstrings, NOT index%2^k.
"""
from __future__ import annotations
import numpy as np
from scipy.linalg import expm

L, NM = 3, 9
DEPTH = 11
SEEDS = (20260610, 1, 2, 4242, 99, 7)
TAU, EPS = 0.35, 0.6


def ann(j, n):
    sz = np.array([[1, 0], [0, -1]], float)
    sm = np.array([[0, 1], [0, 0]], float)
    ops = [sz] * j + [sm] + [np.eye(2)] * (n - j - 1)
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


A9 = [ann(j, NM) for j in range(NM)]
AD9 = [a.T for a in A9]
h9 = np.zeros((NM, NM))
for x in range(L):
    for c in range(3):
        h9[3 * x + c, 3 * ((x + 1) % L) + c] = h9[3 * ((x + 1) % L) + c, 3 * x + c] = -1.0
H = sum(h9[i, j] * (AD9[i] @ A9[j]).astype(complex) for i in range(NM) for j in range(NM))
N_site0 = sum(AD9[c] @ A9[c] for c in range(3))
OPS = np.array([(AD9[0 + i] @ A9[3 + j]).astype(complex) for i in range(3) for j in range(3)])
U_step = expm(-1j * H * TAU)


def polar_u(M):
    U, s, Vh = np.linalg.svd(M)
    return U @ Vh


def kraus_pair(Nop, eps):
    w, V = np.linalg.eigh(Nop)
    Nt = (w - w.mean()) / max(abs(w - w.mean()))
    Kp = (V @ np.diag(np.sqrt((1 + eps * Nt) / 2)) @ V.T).astype(complex)
    Km = (V @ np.diag(np.sqrt((1 - eps * Nt) / 2)) @ V.T).astype(complex)
    return Kp, Km


Kp, Km = kraus_pair(N_site0, EPS)


def slater(P):
    diagN = np.diag(sum(AD9[m] @ A9[m] for m in range(NM)).real)
    vac = np.zeros(2 ** NM)
    vac[int(np.argmin(diagN))] = 1.0
    psi = vac.astype(complex)
    for k in range(P.shape[1]):
        psi = sum(P[m, k] * AD9[m].astype(complex) for m in range(NM)) @ psi
    return psi / np.linalg.norm(psi)


def dets_of(states):
    B = states.shape[0]
    M = np.empty((B, 9), complex)
    for k in range(9):
        M[:, k] = np.einsum('bi,bi->b', states.conj(), states @ OPS[k].T)
    M = M.reshape(B, 3, 3)
    sv_min = float(np.min(np.linalg.svd(M, compute_uv=False)[:, -1]))
    return np.array([np.linalg.det(polar_u(m)) for m in M]), sv_min


def scan(seed):
    rng = np.random.default_rng(seed)
    psi0 = slater(np.linalg.qr(rng.normal(size=(NM, 5)) + 1j * rng.normal(size=(NM, 5)))[0])
    sf = psi0[None, :].copy()
    base, dprev = [], None
    for n in range(DEPTH):
        sf = sf @ U_step.T
        d, _ = dets_of(sf)
        if dprev is not None:
            base.append(float(np.angle(d[0] / dprev[0])))
        dprev = d
    states = psi0[None, :].copy()
    weights = np.array([1.0])
    bits = [tuple()]
    detprev = None
    Theta = np.zeros(1)
    rows = {}
    out = {"d_cen": [], "d_raw": []}
    ch_pc = ch_pr = None
    for n in range(DEPTH):
        states = states @ U_step.T
        new = np.vstack([states @ Kp.T, states @ Km.T])
        norms = np.einsum('bi,bi->b', new.conj(), new).real
        weights = np.concatenate([weights, weights]) * norms
        states = (new.T / np.sqrt(norms)).T
        B = len(bits)
        bits = [bits[j] + (0,) for j in range(B)] + [bits[j] + (1,) for j in range(B)]
        d, _ = dets_of(states)
        if detprev is not None:
            par = detprev[np.arange(len(d)) % len(detprev)]
            dth = np.angle(d / par)
            eta = np.angle(np.exp(1j * (dth - base[n - 1])))
            Theta = Theta[np.arange(len(d)) % len(Theta)] + eta
            Z = weights.sum()
            ch_c = np.array([complex(np.sum(weights * np.exp(1j * k * eta)) / Z) for k in (1, 2, 3)])
            ch_r = np.array([complex(np.sum(weights * np.exp(1j * k * dth)) / Z) for k in (1, 2, 3)])
            if ch_pc is not None:
                out["d_cen"].append(float(np.sum(np.abs(ch_c - ch_pc))))
                out["d_raw"].append(float(np.sum(np.abs(ch_r - ch_pr))))
            chT = [complex(np.sum(weights * np.exp(1j * k * Theta)) / Z) for k in (1, 2, 3)]
            rows[n + 1] = {"chT": [abs(c) for c in chT], "Theta": Theta.copy(),
                           "w": weights.copy(), "bits": list(bits)}
            ch_pc, ch_pr = ch_c, ch_r
        detprev = d
    out["rows"] = rows
    return out


RES = {s: scan(s) for s in SEEDS}


def prefix_profile_explicit(row, kpref):
    """Within-family |ch1|, families keyed by EXPLICIT first-kpref chronological bits,
    weighted-averaged with weights RENORMALIZED within each family (d-check)."""
    Theta, w, bits = row["Theta"], row["w"], row["bits"]
    fams = {}
    for b in range(len(w)):
        key = bits[b][:kpref]
        fams.setdefault(key, []).append(b)
    within, wts = [], []
    for key, idxs in fams.items():
        idxs = np.array(idxs)
        ww = w[idxs]
        if ww.sum() < 1e-12:
            continue
        # within-family circular concentration: |sum w e^{i Theta}| / sum w  (renormalized)
        within.append(abs(complex(np.sum(ww * np.exp(1j * Theta[idxs])) / ww.sum())))
        wts.append(ww.sum())
    return float(np.average(within, weights=wts)), len(fams)


print("=" * 78)
print("(a) headline events -- independent recompute (explicit-bit families)")
print("=" * 78)
# EXACT-MIXTURE: seed 4242 depth 3
r = RES[4242]["rows"][3]
g = r["chT"][0]
p2, nf2 = prefix_profile_explicit(r, 2)
# also get the raw within-family values per family to inspect the 1.000 closely
Theta, w, bits = r["Theta"], r["w"], r["bits"]
fam_vals = {}
for b in range(len(w)):
    fam_vals.setdefault(bits[b][:2], []).append(b)
print(f"  EXACT-MIXTURE (4242 d3): global |ch1| = {g:.6f}")
print(f"    prefix-2 within-family weighted avg = {p2:.10f}  (1 - that = {1-p2:.2e}); "
      f"{nf2} families")
for key, idxs in sorted(fam_vals.items()):
    idxs = np.array(idxs)
    ww = w[idxs]
    val = abs(complex(np.sum(ww * np.exp(1j * Theta[idxs])) / ww.sum()))
    print(f"      family first2={key}: members={list(idxs)}  within|ch1|={val:.12f}  "
          f"famweight={ww.sum():.4f}")

# WITHIN-SECTOR: seed 4242 depth 9
r9 = RES[4242]["rows"][9]
g9 = r9["chT"][0]
p3_9, nf3_9 = prefix_profile_explicit(r9, 3)
print(f"\n  WITHIN-SECTOR (4242 d9): global |ch1| = {g9:.6f} -> prefix-3 within-family "
      f"{p3_9:.6f}  ({nf3_9} families)")

# INTERMEDIATE: seed 99 depth 7
r7 = RES[99]["rows"][7]
g7 = r7["chT"][0]
p2_7, _ = prefix_profile_explicit(r7, 2)
p3_7, _ = prefix_profile_explicit(r7, 3)
print(f"  INTERMEDIATE (99 d7): global |ch1| = {g7:.6f} -> prefix-2 {p2_7:.6f} "
      f"-> prefix-3 {p3_7:.6f}")

print("\n" + "=" * 78)
print("(c) E1 ratios (median d_cen / median d_raw) per seed -- independent")
print("=" * 78)
for s in SEEDS:
    dc, dr = np.array(RES[s]["d_cen"]), np.array(RES[s]["d_raw"])
    print(f"  seed {s:>9}: ratio = {np.median(dc)/np.median(dr):.4f}  "
          f"(med d_cen {np.median(dc):.4f}, med d_raw {np.median(dr):.4f}); "
          f"rows where d_cen>d_raw: {int(np.sum(dc>dr))}/{len(dc)}")

print("\n" + "=" * 78)
print("(c) E2 bimodal rows (|ch1|<0.8 and |ch2|-|ch1|^4 > 0.2) -- independent")
print("=" * 78)
bimodal = []
for s in SEEDS:
    for n, row in RES[s]["rows"].items():
        c1, c2, c3 = row["chT"]
        if c1 < 0.8:
            exc = c2 - c1 ** 4
            if exc > 0.2:
                bimodal.append((s, n, c1, c2, c1 ** 4, exc))
for t in sorted(bimodal, key=lambda x: -x[5]):
    print(f"  seed {t[0]:>5} depth {t[1]:>2}: |ch1|={t[2]:.3f} |ch2|={t[3]:.3f} "
          f"Gauss(|ch1|^4)={t[4]:.3f} excess={t[5]:.3f}")
print(f"  => {len(bimodal)} rows across {sorted(set(t[0] for t in bimodal))}")

print("\n" + "=" * 78)
print("(d) aggregation cross-check: re-derive p2 for 4242-d3 THREE independent ways")
print("=" * 78)
r = RES[4242]["rows"][3]
Theta, w, bits = r["Theta"], r["w"], r["bits"]
# way A: explicit-bit families, renormalized-within, weighted by famweight
pA, _ = prefix_profile_explicit(r, 2)
# way B: index%4 families (runner's method) re-implemented here from scratch
fams_idx = {}
for b in range(len(w)):
    fams_idx.setdefault(b % 4, []).append(b)
within_B, wt_B = [], []
for v, idxs in fams_idx.items():
    idxs = np.array(idxs); ww = w[idxs]
    within_B.append(abs(complex(np.sum(ww * np.exp(1j * Theta[idxs])) / ww.sum())))
    wt_B.append(ww.sum())
pB = float(np.average(within_B, weights=wt_B))
# way C: UNWEIGHTED average of within-family concentrations (to show weighting choice matters/not)
pC = float(np.mean(within_B))
print(f"  way A (explicit bits, weighted):  {pA:.10f}")
print(f"  way B (index%%4,    weighted):     {pB:.10f}")
print(f"  way C (index%%4,    unweighted):   {pC:.10f}")
print(f"  A vs B agree: {abs(pA-pB) < 1e-12}")
