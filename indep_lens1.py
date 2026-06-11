#!/usr/bin/env python3
"""LENS 1 independent recompute. Own implementation of the Born-weighted outcome tree,
with EXPLICIT per-branch outcome bitstrings (no index%2^k shortcut), to:
 (b) verify the prefix-labeling combinatorics by direct hand-enumeration,
 (a) verify the EXACT-mixture / within-sector / intermediate headline events,
 (c) verify E1 ratios and E2 bimodal rows,
 (d) verify the within-family weighted-average aggregation.

Built from scratch; structure mirrors the physical setup but the bookkeeping
(explicit bit tracking, dict-of-families conditioning) is independent of the runner's
index%2^k machinery, so an indexing bug in the runner would show up as a mismatch.
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
# off-site 0<->1 color operators, matching both the runner and the #3532 prior
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


def scan(seed, track_bits=True):
    """Independent tree scan. Tracks, per depth, the centered increment eta per branch,
    the weights, the cumulative Theta, AND an explicit list of outcome bitstrings
    (bits[b] = tuple of 0/1 outcomes in CHRONOLOGICAL order, step1 first)."""
    rng = np.random.default_rng(seed)
    psi0 = slater(np.linalg.qr(rng.normal(size=(NM, 5)) + 1j * rng.normal(size=(NM, 5)))[0])
    # record-free baseline phase increments
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
    bits = [tuple()]                  # explicit chronological outcome record per branch
    detprev = None
    Theta = np.zeros(1)
    rows = {}
    out = {"d_cen": [], "d_raw": [], "worst_sv": np.inf}
    ch_pc = ch_pr = None
    for n in range(DEPTH):
        states = states @ U_step.T
        new = np.vstack([states @ Kp.T, states @ Km.T])      # rows 0..B-1: '+', B..2B-1: '-'
        norms = np.einsum('bi,bi->b', new.conj(), new).real
        weights = np.concatenate([weights, weights]) * norms
        states = (new.T / np.sqrt(norms)).T
        # explicit bit bookkeeping consistent with the vstack ordering:
        # child j (j<B) = parent j + outcome 0(+); child B+j = parent j + outcome 1(-)
        B = len(bits)
        bits = [bits[j] + (0,) for j in range(B)] + [bits[j] + (1,) for j in range(B)]
        d, svm = dets_of(states)
        out["worst_sv"] = min(out["worst_sv"], svm)
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


# ---------------------------------------------------------------------------
# (b) PREFIX-LABELING COMBINATORICS: is index%2^k == first-k-outcomes?
# ---------------------------------------------------------------------------
print("=" * 78)
print("(b) prefix-labeling check: does (branch_index % 2^k) equal the FIRST k outcomes?")
print("=" * 78)
# Build the bit tracker for a small explicit tree and compare against index%2^k.
res99 = scan(99)
mismatches = 0
checked = 0
for n in (3, 7, 9):
    row = res99["rows"][n]
    blist = row["bits"]
    B = len(blist)
    assert B == 2 ** n
    for kpref in (1, 2, 3):
        for b in range(B):
            first_k_outcomes = blist[b][:kpref]              # chronological, explicit
            runner_label = b % (2 ** kpref)                  # the runner's family key
            # decode runner_label as bits: low bit = step1 (per the vstack analysis)
            decoded = tuple((runner_label >> t) & 1 for t in range(kpref))
            checked += 1
            if decoded != first_k_outcomes:
                mismatches += 1
                if mismatches <= 5:
                    print(f"   MISMATCH n={n} b={b} k={kpref}: explicit {first_k_outcomes} "
                          f"vs runner-decoded {decoded}")
print(f"   checked {checked} (branch, k) pairs; mismatches = {mismatches}")
print(f"   => index%%2^k {'IS' if mismatches == 0 else 'IS NOT'} the first-k chronological outcomes")

# hand-enumeration at depth 3, explicit
print("\n   depth-3 explicit enumeration (branch index -> chronological outcome bits):")
row3 = res99["rows"][3]
for b in range(8):
    print(f"     b={b:>2} (binary {b:03b}) -> outcomes(step1,2,3)={row3['bits'][b]}  "
          f"| b%2={b%2} b%4={b%4}")
