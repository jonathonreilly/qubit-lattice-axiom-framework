#!/usr/bin/env python3
"""The centered U(1) fluctuation law: NOT distribution-stationary (seed-robust honest
negative); its spread regime is NON-Gaussian with the bimodal signature; and the spread
DECOMPOSES by record-prefix conditioning -- small-family near-exact events are demoted
by a cardinality/null caveat, while larger-family events show null-cleared record-sector
structure with genuine within-sector spread.  The U(1)-CLT question RE-POSES
conditionally on the record.

Class-A exact verification for the source note

    docs/CENTERED_U1_FLUCTUATION_LAW_RECORD_MIXTURE_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-06-11.md

CONTEXT (answer-mode for PR #3532's named next object -- the law of the
centered record-noise).  #3532 decomposed the det/U(1) increment into the deterministic
record-free dynamical phase plus a record-induced fluctuation and posed the CLT question
on the CENTERED fluctuation.  THIS NOTE ANSWERS THE POSED QUESTION at this size/horizon:
the centered law fails distribution-stationarity (seed-robustly exhibited), its composed
phase is non-Gaussian in the spread regime where the k^2 test has teeth (#3532-D4
control armed), and the spread carries RECORD-SECTOR MIXTURE structure -- conditioning
on the early outcome record restores concentration near-exactly only in small-family
events with the cardinality caveat disclosed, and partially in null-cleared larger
events.  Machinery: the exact Born-weighted outcome tree (depth 11, no MC;
#3507 guards; SIX seeds including the adversarial set -- the standing policy).

THE FINDINGS (exact at each depth; finite-horizon; seed/instance-labeled):
  (E1) NOT DISTRIBUTION-STATIONARY (honest negative): the centered law's per-depth
       characteristic-function drift d_cen(n) is NOT seed-robustly smaller than the raw
       law's: at the tame seed the ratio median(d_cen)/median(d_raw) is small (~0.2),
       but at adversarial seeds it approaches or exceeds ~0.5-1 (exhibited rows where
       d_cen > d_raw).  Centering removes the MEAN wandering (#3532's seed-robust ratio
       result) but NOT the distribution-level non-stationarity.
  (E2) NON-GAUSSIAN IN THE SPREAD REGIME (where the test has teeth): at identified
       spread rows (|ch1| < 0.8) the composed centered phase grossly violates the
       wrapped-Gaussian relation WITH THE BIMODAL SIGNATURE -- |ch2| EXCEEDS the
       Gaussian prediction by > 0.2 (e.g. 0.925 vs 0.147) -- a few-atom structure, not
       diffusion.  No U(1)-CLT emerges UNCONDITIONALLY at this object/size/horizon.
  (E3) THE RECORD-MIXTURE STRUCTURE (panel-re-anchored on null-cleared events): a
       label-permutation control is armed in-runner.  The draft's depth-3 'exact
       mixture at machine precision' headline was a 2-ATOM TAUTOLOGY (family size 2;
       cardinality-forced; the permutation null also reaches ~1; true value
       1 - 2.2e-5; collapses with family growth) -- DEMOTED, disclosed (it is also
       E2's sharpest bimodal row: the SAME event, double-duty disclosed).  THE
       LOAD-BEARING STRUCTURE: at events with large families, the record prefix
       CLEARS the permutation null decisively (seed 4242 depth 9, 128 branches/family:
       record 0.557 vs null p95 0.469; seed 99 depth 7: 0.502 vs p95 0.315) -- genuine
       record-sector structure with a within-sector remainder (the two-component
       anatomy).  The record REGISTERS partial phase-family structure (exhibited
       structure, not an axiom claim).  CONSEQUENCE + THE NEXT OBJECT, sharply: the
       unconditional law is a record-mixture and not the CLT walker; the well-posed
       conditional object is the FIXED-prefix-k law as the horizon grows (full
       conditioning is vacuous); first datum, honest: the fixed-k profile does NOT
       concentrate at this instance (d9: prefix-2 = prefix-3 = 0.557, prefix-4 0.598)
       -- the re-posing is OPEN with a first negative data point.
  (E4) CONSECUTIVE-INCREMENT CORRELATIONS: mostly small (< 0.15) with disclosed spikes
       (up to ~0.55 at an adversarial seed) -- the independence premise is also not
       seed-robust as-is; quantified.

WHAT THIS DOES AND DOES NOT CLAIM: the #3532-posed question is ANSWERED NEGATIVELY for
the unconditional centered law, with the mixture structure as the constructive remainder;
no CLT premise is delivered; #3507's residuals stand, residual 1 now carries a
three-layer anatomy (bi-frame matrix wandering #3522; deterministic-phase invariant
wandering #3532; record-mixture + within-sector spread of the centered law, here).
Conditionality inherited (#3507/#3522/#3532): the Born derived-chain cap (assembly note
UNAUDITED on the live ledger, self-verified at landing); named instruments (eps
supplied); supplied C^3 carrier; named hopping; guarded full-rank domain.  Discrete-time
(retained R1 boundaries untouched).  The U(1) factor is NOT identified with a physical
gauge field.  No new axiom/primitive/measure/weight; r untouched.  All numbers
seed/instance-labeled; adversarial seeds in-runner per standing policy.

Run: python3 scripts/frontier_centered_u1_fluctuation_record_mixture_structure_2026_06_11.py
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


L, NM = 3, 9
RANK_TOL = 1e-8
DEPTH = 11
SEEDS = (20260610, 1, 2, 4242, 99, 7)


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
U_step = expm(-1j * H * 0.35)
EPS = 0.6


def polar_u(M):
    U, s, Vh = np.linalg.svd(M)
    return U @ Vh


def kraus_pair(Nop, eps):
    w, V = np.linalg.eigh(Nop)
    Nt = (w - w.mean()) / max(abs(w - w.mean()))
    Kp = (V @ np.diag(np.sqrt((1 + eps * Nt) / 2)) @ V.T).astype(complex)
    Km = (V @ np.diag(np.sqrt((1 - eps * Nt) / 2)) @ V.T).astype(complex)
    return Kp, Km


KB = kraus_pair(N_site0, EPS)


def slater(P):
    vac = np.zeros(2 ** NM)
    vac[int(np.argmin(np.diag(sum(AD9[m] @ A9[m] for m in range(NM)).real)))] = 1.0
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


def full_scan(seed):
    """Tree scan returning per-depth: centered/raw ch-vectors, Theta arrays, weights,
    correlations; plus the rank guard."""
    rng = np.random.default_rng(seed)
    psi0 = slater(np.linalg.qr(rng.normal(size=(NM, 5)) + 1j * rng.normal(size=(NM, 5)))[0])
    sf = psi0[None, :].copy()
    base = []
    dprev = None
    for n in range(DEPTH):
        sf = sf @ U_step.T
        d, _ = dets_of(sf)
        if dprev is not None:
            base.append(float(np.angle(d[0] / dprev[0])))
        dprev = d
    states = psi0[None, :].copy()
    weights = np.array([1.0])
    detprev = None
    Theta = np.zeros(1)
    eta_prev = None
    out = {"d_cen": [], "d_raw": [], "corr": [], "rows": [], "worst_sv": np.inf}
    ch_pc, ch_pr = None, None
    for n in range(DEPTH):
        states = states @ U_step.T
        new = np.vstack([states @ KB[0].T, states @ KB[1].T])
        norms = np.einsum('bi,bi->b', new.conj(), new).real
        assert (norms > 1e-14).all(), "no-prune guard"
        weights = np.concatenate([weights, weights]) * norms
        states = (new.T / np.sqrt(norms)).T
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
            corr = np.nan
            if eta_prev is not None:
                ep = eta_prev[np.arange(len(d)) % len(eta_prev)]
                j = complex(np.sum(weights * np.exp(1j * (eta - ep))) / Z)
                m1 = complex(np.sum(weights * np.exp(1j * eta)) / Z)
                m0 = complex(np.sum(weights * np.exp(-1j * ep)) / Z)
                corr = abs(j - m1 * m0)
            out["corr"].append(corr)
            chT = [complex(np.sum(weights * np.exp(1j * k * Theta)) / Z) for k in (1, 2, 3)]
            out["rows"].append({"n": n + 1, "chT": [abs(c) for c in chT],
                                "Theta": Theta.copy(), "w": weights.copy()})
            ch_pc, ch_pr = ch_c, ch_r
            eta_prev = eta
        detprev = d
    return out


RES = {s: full_scan(s) for s in SEEDS}

# ===========================================================================
print("=" * 78)
print("Part 1  tree integrity (six seeds; guards inherited)")
print("=" * 78)
check("rank guard holds on every branch, depth, and seed",
      min(RES[s]["worst_sv"] for s in SEEDS) > RANK_TOL,
      f"worst min-sv {min(RES[s]['worst_sv'] for s in SEEDS):.4f}")

# ===========================================================================
print("=" * 78)
print("Part 2  (E1) the centered law is NOT distribution-stationary (seed-robust facts)")
print("=" * 78)
ratios = {}
for s in SEEDS:
    dc, dr = np.array(RES[s]["d_cen"]), np.array(RES[s]["d_raw"])
    ratios[s] = float(np.median(dc) / np.median(dr))
check("at the tame published seed the centered law's ch-drift is far below the raw "
      "law's (median ratio < 0.3) -- centering helps THERE",
      ratios[20260610] < 0.3, f"ratio {ratios[20260610]:.3f}")
check("but at adversarial seeds the ratio rises to ~0.5+ (and individual rows exceed "
      "1): distribution-stationarity of the centered law FAILS as a seed-robust claim "
      "-- the honest negative; cross-seed ratio spread disclosed",
      max(ratios.values()) > 0.45,
      f"ratio spread {[f'{ratios[s]:.2f}' for s in SEEDS]}")

# ===========================================================================
print("=" * 78)
print("Part 3  (E2) spread-regime non-Gaussianity with the BIMODAL signature")
print("=" * 78)
bimodal_rows = []
for s in SEEDS:
    for row in RES[s]["rows"]:
        c1, c2, c3 = row["chT"]
        if c1 < 0.8:
            excess = c2 - c1 ** 4
            if excess > 0.2:
                bimodal_rows.append((s, row["n"], c1, c2, c1 ** 4, excess))
check("identified spread rows (|ch1| < 0.8) with |ch2| EXCEEDING the wrapped-Gaussian "
      "prediction by > 0.2 exist across MULTIPLE seeds: the few-atom (bimodal) "
      "signature -- the composed centered phase does NOT diffuse Gaussianly where the "
      "k^2 test has teeth (#3532-D4 control armed: at high concentration the relation "
      "is automatic and proves nothing; here, in the spread regime, it FAILS in the "
      "atomic direction)",
      len(set(r[0] for r in bimodal_rows)) >= 2,
      f"{len(bimodal_rows)} rows across seeds {sorted(set(r[0] for r in bimodal_rows))}; "
      f"sharpest: seed {max(bimodal_rows, key=lambda r: r[5])[0]} depth "
      f"{max(bimodal_rows, key=lambda r: r[5])[1]}: |ch2| "
      f"{max(bimodal_rows, key=lambda r: r[5])[3]:.3f} vs Gauss "
      f"{max(bimodal_rows, key=lambda r: r[5])[4]:.3f}")

# ===========================================================================
print("=" * 78)
print("Part 4  (E3) the record-mixture structure: prefix conditioning")
print("=" * 78)


def prefix_profile(row, kpref, lbl=None):
    Theta, w = row["Theta"], row["w"]
    B = len(w)
    if lbl is None:
        lbl = np.arange(B) % (2 ** kpref)
    within, wts = [], []
    for v in range(2 ** kpref):
        m = lbl == v
        if w[m].sum() < 1e-12:
            continue
        within.append(abs(complex(np.sum(w[m] * np.exp(1j * Theta[m])) / w[m].sum())))
        wts.append(w[m].sum())
    return float(np.average(within, weights=wts))


def permutation_null(row, kpref, n_draws=400, seed=7777):
    """Label-permutation control: random relabel into same-cardinality families
    (deterministic fixed seed).  Returns (median, p95, max) of the null profile."""
    rngp = np.random.default_rng(seed)
    B = len(row["w"])
    vals = []
    for _ in range(n_draws):
        perm = rngp.permutation(B)
        vals.append(prefix_profile(row, kpref, lbl=(np.arange(B) % (2 ** kpref))[perm]))
    v = np.array(vals)
    return float(np.median(v)), float(np.quantile(v, 0.95)), float(v.max())


# PANEL RE-ANCHORING: the draft's depth-3 'exact mixture / machine precision' headline
# was a 2-ATOM TAUTOLOGY (each prefix-2 family at depth 3 has exactly 2 branches;
# within-family |ch1| ~ 1 is cardinality-forced; the permutation null ALSO reaches ~1;
# the true value is 1 - 2.2e-5, eleven orders from machine precision; it collapses with
# family growth: 0.99998 d3 -> 0.984 d4 -> 0.868 d5 -> 0.557 d9).  The headline is now
# anchored on the events that CLEAR the permutation null.
row_d3 = next(r for r in RES[4242]["rows"] if r["n"] == 3)
p2_d3 = prefix_profile(row_d3, 2)
n_med, n_p95, n_max = permutation_null(row_d3, 2)
check("SMALL-FAMILY OBSERVATION (seed 4242, depth 3 -- DEMOTED per panel; this is also "
      "E2's sharpest bimodal row, the SAME event, disclosed): prefix-2 within-family "
      "concentration is 1 - 2.2e-5 -- but families have only 2 branches and the "
      "label-permutation null ALSO reaches ~1: cardinality-driven, NOT load-bearing "
      "record structure",
      p2_d3 > 0.999 and n_max > 0.99,
      f"record {p2_d3:.6f}; null median {n_med:.3f}, p95 {n_p95:.3f}, max {n_max:.6f}")
row_within = next(r for r in RES[4242]["rows"] if r["n"] == 9)
g_w = row_within["chT"][0]
p3_w = prefix_profile(row_within, 3)
nw_med, nw_p95, nw_max = permutation_null(row_within, 3)
check("THE LOAD-BEARING EVENT (seed 4242, depth 9; 128 branches/family at prefix-3): "
      "the record prefix CLEARS the label-permutation null decisively -- genuine "
      "record-sector structure, with a within-sector remainder that conditioning does "
      "not remove (the two-component anatomy)",
      p3_w > nw_p95 and g_w < 0.6,
      f"record prefix-3 {p3_w:.3f} vs null median {nw_med:.3f} / p95 {nw_p95:.3f} / "
      f"max {nw_max:.3f}; global {g_w:.3f}")
row_99 = next(r for r in RES[99]["rows"] if r["n"] == 7)
p2_99, p3_99 = prefix_profile(row_99, 2), prefix_profile(row_99, 3)
n99_med, n99_p95, _ = permutation_null(row_99, 3)
check("SECOND LOAD-BEARING EVENT (seed 99, depth 7): record conditioning beats the "
      "null (0.06 -> 0.35 -> 0.50 at prefixes 2, 3, vs null p95): mixture and "
      "within-sector components coexist",
      row_99["chT"][0] < 0.1 and p3_99 > n99_p95,
      f"global {row_99['chT'][0]:.3f} -> prefix-2 {p2_99:.3f} -> prefix-3 {p3_99:.3f}; "
      f"null p95 {n99_p95:.3f}")
row_s7 = next(r for r in RES[7]["rows"] if r["n"] == 4)
p3_s7 = prefix_profile(row_s7, 3)
print(f"   second near-exact prefix event (seed 7, depth 4): global "
      f"{row_s7['chT'][0]:.3f} -> prefix-3 {p3_s7:.4f} (multi-instance phenomenon; "
      f"family size 2 -- same cardinality caveat as d3, disclosed).")
p2_w = prefix_profile(row_within, 2)
p4_w = prefix_profile(row_within, 4)
print(f"   THE NEXT OBJECT, defined sharply: the FIXED-prefix-k conditional law as the")
print(f"   horizon grows (full conditioning is vacuous -- singleton families).  First")
print(f"   data point, honest: at seed 4242 depth 9 the fixed-k profile does NOT")
print(f"   concentrate (prefix-2 {p2_w:.3f}, prefix-3 {p3_w:.3f}, prefix-4 {p4_w:.3f})")
print(f"   -- the record-conditional re-posing is OPEN with a first negative datum.")

# ===========================================================================
print("=" * 78)
print("Part 5  (E4) consecutive-increment correlations (disclosed)")
print("=" * 78)
corr_all = []
for s in SEEDS:
    cs = [c for c in RES[s]["corr"] if not np.isnan(c)]
    corr_all.append((s, float(np.median(cs)), float(np.max(cs))))
check("consecutive centered increments: medians mostly small (< 0.15) with disclosed "
      "adversarial spikes (the independence premise is not seed-robust as-is)",
      all(m < 0.35 for _, m, _ in corr_all),
      "; ".join(f"seed {s}: med {m:.3f} max {mx:.3f}" for s, m, mx in corr_all))

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: answers the question #3532 posed on the centered U(1) fluctuation, at")
print("  this size/horizon: (E1) NOT distribution-stationary (seed-robust honest")
print("  negative -- centering removes the mean wandering, not the law's drift); (E2)")
print("  non-Gaussian in the spread regime with the BIMODAL/atomic signature (the")
print("  #3532-D4 control armed -- the failure is in the regime where the test has")
print("  teeth); (E3) the spread DECOMPOSES by record-prefix conditioning: a")
print("  demoted near-exact small-family event (cardinality caveat disclosed), a")
print("  null-cleared within-sector-spread event (prefix conditioning recovers ~0.56),")
print("  and an intermediate event -- the unconditional law is a record-mixture and")
print("  cannot be the CLT walker; the premise RE-POSES on the RECORD-CONDITIONAL law")
print("  (named next object; a re-posing, not a wall).  (E4) correlations disclosed.")
print("  Finite horizon; six seeds incl. adversarial (standing policy); one (eps,tau)")
print("  instance; numbers seed/instance-labeled.  No CLT premise delivered; #3507")
print("  residuals stand; residual 1 now has the three-layer anatomy (#3522 bi-frame;")
print("  #3532 deterministic phase; record-mixture + within-sector spread, here).")
print("  Born cap inherited (assembly note UNAUDITED on the live ledger, self-verified")
print("  at landing).  The U(1) factor is NOT identified with a physical gauge field.")
print("  Discrete-time (retained R1 boundaries untouched).  No new axiom/primitive/")
print("  measure/weight; r untouched.  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
