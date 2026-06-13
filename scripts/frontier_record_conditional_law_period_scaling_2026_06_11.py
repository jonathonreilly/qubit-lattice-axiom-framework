#!/usr/bin/env python3
"""Finite-period scaling of the record-conditional U(1) law (L = 3 -> 4): SEED-ROBUST
fixed-k monotonicity at the larger period (every tested L=4 seed monotone and positive
against the fixed seeded 300-draw permutation-null diagnostic; canonical runner checks
7/7 K=7 seeds and a 3/3 half-filling control), with seeded-null diagnostic gaps
COMPARABLE-OR-LARGER than the L=3 set (ranges overlap; median ~1.4x, NOT doubled --
panel-corrected against the full L=3 baseline set).

Class-A exact verification for the source note

    docs/RECORD_CONDITIONAL_LAW_PERIOD_SCALING_L3_TO_L4_BOUNDED_THEOREM_NOTE_2026-06-11.md

CONTEXT (period-scaling source proposal for #3554's named next object).
#3554 defined the well-posed conditional object -- the FIXED-prefix-k law of the
composed centered U(1) phase as the horizon grows -- and recorded a first NEGATIVE
datum at the 3-ring (the fixed-k profile did not concentrate: prefix-2 = prefix-3 =
0.557, prefix-4 = 0.598 at the load-bearing event).  THIS NOTE SCALES THE PERIOD:
the identical machinery at L = 4 (12 modes, 4096-dim Fock -- the largest exactly
treatable ring), three L=4 seeds, with the L = 3 baseline RECOMPUTED IN-RUNNER so
the comparison is self-contained.

THE FINDINGS (exact finite evolution; deterministic seeded-null diagnostic; two periods --
a TWO-POINT trend, labeled as such;
PANEL-CORRECTED against the FULL L=3 baseline set):
  (F1) L = 3 BASELINE AS A SET (both #3554 events positive against the fixed seeded-null
       diagnostic, recomputed in-runner):
       seed 4242/depth 9: gap +0.088, fixed-k STALLED (0.557/0.557/0.598); seed
       99/depth 7: gap +0.190, MONOTONE (0.347/0.502/0.695).  The stall is therefore
       EVENT/SEED-specific at L=3, not a period property.
  (F2) L = 4, THREE SEEDS (most-spread rows, depth <= 9): every seed exceeds the
       fixed seeded 300-draw permutation-null p95 diagnostic (gaps +0.193 / +0.217 /
       +0.076) and every fixed-k profile is MONOTONE in k.  The canonical runner also
       checks the robustness extension:
       7/7 tested K=7 seeds and a K=6 half-filling control (3/3).  Seed-robust
       monotonicity at the larger period is the positive fact.
  (F3) THE SCALING VERDICT (honest, panel-corrected): the L=4 seeded-null diagnostic gaps are
       COMPARABLE-OR-LARGER than the L=3 set (ranges overlap: worst L=4 +0.076 sits
       below best L=3 +0.190; median ratio ~1.4x, NOT doubled); the load-bearing
       positive is the SEED-ROBUST L=4 monotonicity -- consistent with, but NOT
       establishing, strengthening with the period.  NOT claimed: gap growth as a
       period law, convergence/concentration, any CLT premise, L >= 5 or Z^3 behavior
       (rings only -- geometry disclosed); all magnitudes instance/seed-labeled.

Historical context from #3554/#3507 names the route vocabulary, but this runner
does not import their audit status as a theorem premise. The source-positive is
only the finite runner-defined diagnostic: explicit sparse Fock evolution,
SVD-polar determinant readout, fixed seeds/depths/occupancies, and the fixed seeded
300-draw label-permutation diagnostic. Named instruments (eps = 0.6), supplied
C^3 carrier, named hopping (tau = 0.35), and discrete time are finite diagnostic
inputs here. The U(1) factor is NOT identified with a physical gauge field.
No new axiom/primitive/measure/weight; r untouched.

Run: python3 scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm
from pathlib import Path

# MEMORY DISCIPLINE (owner-enforced after a panel OOM): the dense-operator build held
# ~24 x 268 MB = ~10 GB per process at L=4, and a 4-agent panel multiplied that to an
# OOM.  This rewrite keeps ALL Fock operators SPARSE (each a_i^dag a_j has <= 2^(NM-1)
# nonzeros), the Kraus pair DIAGONAL (vectors -- N_x is Fock-diagonal), and one dense
# U_step (268 MB at L=4; the expm call transiently materializes several dense
# temporaries).  MEASURED single-process peak ~1.1-1.5 GB (/usr/bin/time -l) -- safe for
# a single run; panels must still serialize any L=4 recompute (4 x 1.1 GB approaches
# the OOM class the contract guards).

PASS = 0
FAIL = 0
NOTE = Path(__file__).resolve().parents[1] / "docs" / (
    "RECORD_CONDITIONAL_LAW_PERIOD_SCALING_L3_TO_L4_BOUNDED_THEOREM_NOTE_2026-06-11.md"
)


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


NC = 3
EPS, TAU = 0.6, 0.35
RANK_TOL = 1e-8


def build(Lring):
    NM = Lring * NC
    DIM = 2 ** NM
    sz = sp.csr_matrix(np.array([[1, 0], [0, -1]], float))
    sm = sp.csr_matrix(np.array([[0, 1], [0, 0]], float))
    I2 = sp.identity(2, format='csr')

    def ann(j):
        out = sp.identity(1, format='csr')
        for k in range(NM):
            out = sp.kron(out, sz if k < j else (sm if k == j else I2), format='csr')
        return out

    A = [ann(j) for j in range(NM)]
    AD = [a.T for a in A]
    h = np.zeros((NM, NM))
    for x in range(Lring):
        for c in range(NC):
            h[x * NC + c, ((x + 1) % Lring) * NC + c] = -1.0
            h[((x + 1) % Lring) * NC + c, x * NC + c] = -1.0
    H = sum((h[i, j] * (AD[i] @ A[j])).astype(complex)
            for i in range(NM) for j in range(NM) if abs(h[i, j]) > 1e-12)
    U_step = expm((-1j * TAU) * H.toarray())          # the ONE dense object
    # N_x is Fock-DIAGONAL: the Kraus pair are diagonal -> stored as VECTORS
    n0_diag = sum((AD[c] @ A[c]).diagonal().real for c in range(NC))
    Nt = (n0_diag - n0_diag.mean()) / max(abs(n0_diag - n0_diag.mean()))
    kp_diag = np.sqrt((1 + EPS * Nt) / 2).astype(complex)
    km_diag = np.sqrt((1 - EPS * Nt) / 2).astype(complex)
    OPS = [(AD[0 + i] @ A[NC + j]).astype(complex).tocsr()
           for i in range(3) for j in range(3)]
    ntot_diag = sum((AD[m] @ A[m]).diagonal().real for m in range(NM))
    vac_idx = int(np.argmin(ntot_diag))
    return {"NM": NM, "DIM": DIM, "AD": AD, "U": U_step, "kp": kp_diag, "km": km_diag,
            "OPS": OPS, "vac_idx": vac_idx}


def polar_u(M):
    U, s, Vh = np.linalg.svd(M)
    return U @ Vh


def slater(env, P):
    vac = np.zeros(env["DIM"])
    vac[env["vac_idx"]] = 1.0
    psi = vac.astype(complex)
    for k in range(P.shape[1]):
        psi = sum(env["AD"][m].astype(complex) @ (P[m, k] * psi) for m in range(env["NM"]))
    return psi / np.linalg.norm(psi)


def dets_of(env, states):
    B = states.shape[0]
    M = np.empty((B, 9), complex)
    for k in range(9):
        M[:, k] = np.einsum('bi,bi->b', states.conj(), (env["OPS"][k] @ states.T).T)
    M = M.reshape(B, 3, 3)
    sv_min = float(np.min(np.linalg.svd(M, compute_uv=False)[:, -1]))
    return np.array([np.linalg.det(polar_u(m)) for m in M]), sv_min


def prefix(Theta, w, kpref, lbl=None):
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


def null_p95(Theta, w, kpref, n_draws=300, seed=7777):
    """Seeded sampled-null p95, not exhaustive permutation enumeration."""
    r = np.random.default_rng(seed)
    B = len(w)
    base = np.arange(B) % (2 ** kpref)
    vals = [prefix(Theta, w, kpref, lbl=base[r.permutation(B)]) for _ in range(n_draws)]
    return float(np.quantile(np.array(vals), 0.95))


def scan(env, seed, depth, K_occ):
    rng = np.random.default_rng(seed)
    psi0 = slater(env, np.linalg.qr(rng.normal(size=(env["NM"], K_occ))
                                    + 1j * rng.normal(size=(env["NM"], K_occ)))[0])
    sf = psi0[None, :].copy()
    base = []
    dprev = None
    for n in range(depth):
        sf = sf @ env["U"].T
        d, _ = dets_of(env, sf)
        if dprev is not None:
            base.append(float(np.angle(d[0] / dprev[0])))
        dprev = d
    states = psi0[None, :].copy()
    weights = np.array([1.0])
    detprev = None
    Theta = np.zeros(1)
    worst_sv = np.inf
    most = None
    rows = {}
    for n in range(depth):
        states = states @ env["U"].T
        new = np.vstack([states * env["kp"][None, :], states * env["km"][None, :]])
        norms = np.einsum('bi,bi->b', new.conj(), new).real
        assert (norms > 1e-14).all(), "no-prune guard"
        weights = np.concatenate([weights, weights]) * norms
        states = (new.T / np.sqrt(norms)).T
        d, svm = dets_of(env, states)
        worst_sv = min(worst_sv, svm)
        if detprev is not None:
            par = detprev[np.arange(len(d)) % len(detprev)]
            Theta = Theta[np.arange(len(d)) % len(Theta)] \
                + np.angle(np.exp(1j * (np.angle(d / par) - base[n - 1])))
            Z = weights.sum()
            g1 = abs(complex(np.sum(weights * np.exp(1j * Theta)) / Z))
            rows[n + 1] = (g1, Theta.copy(), weights.copy())
            if n >= 5 and (most is None or g1 < most[1]):
                most = (n + 1, g1, Theta.copy(), weights.copy())
        detprev = d
    return most, rows, worst_sv


# ===========================================================================
print("=" * 78)
print("Part 1  L = 3 baseline (the #3554 load-bearing event, recomputed in-runner)")
print("=" * 78)
env3 = build(3)
most3, rows3, sv3 = scan(env3, 4242, 11, 5)
check("L=3 rank guard (seed 4242)", sv3 > RANK_TOL, f"worst min-sv {sv3:.4f}")
g3, Th3, w3 = rows3[9]
p2_3, p3_3, p4_3 = prefix(Th3, w3, 2), prefix(Th3, w3, 3), prefix(Th3, w3, 4)
n3 = null_p95(Th3, w3, 3)
gap_a = p3_3 - n3
check("L=3 event A (seed 4242/depth 9, the #3554 event): exceeds the fixed seeded "
      "300-draw null diagnostic with gap "
      "~ +0.09 and the fixed-k profile STALLS",
      p3_3 > n3 and abs(p2_3 - p3_3) < 0.02,
      f"global {g3:.3f}; profile {p2_3:.3f}/{p3_3:.3f}/{p4_3:.3f}; null p95 {n3:.3f}; "
      f"gap {gap_a:+.3f}")
# PANEL EDIT (baseline-fairness): the SECOND #3554 seeded-null-diagnostic positive event joins the baseline
most99, rows99, sv99 = scan(env3, 99, 11, 5)
check("L=3 rank guard (seed 99)", sv99 > RANK_TOL, f"worst min-sv {sv99:.4f}")
g9, Th9, w9 = rows99[7]
p2_9, p3_9, p4_9 = prefix(Th9, w9, 2), prefix(Th9, w9, 3), prefix(Th9, w9, 4)
n9 = null_p95(Th9, w9, 3)
gap_b = p3_9 - n9
check("L=3 event B (seed 99/depth 7, #3554's other event positive against the fixed "
      "seeded-null diagnostic): exceeds "
      "the fixed seeded 300-draw null diagnostic with gap ~ +0.19 and is MONOTONE -- "
      "the stall is EVENT-specific at L=3, "
      "not a period property (panel-decisive correction)",
      p3_9 > n9 and p2_9 < p3_9 < p4_9,
      f"global {g9:.3f}; profile {p2_9:.3f}/{p3_9:.3f}/{p4_9:.3f}; null p95 {n9:.3f}; "
      f"gap {gap_b:+.3f}")
gap3_set = [gap_a, gap_b]

# ===========================================================================
print("=" * 78)
print("Part 2  L = 4 (12 modes, 4096-dim Fock): three seeds, most-spread rows")
print("=" * 78)
env4 = build(4)
gaps, monotone_all = [], True
l4_k7 = {}
for seed in (1, 4242, 99):
    most, rows, sv4 = scan(env4, seed, 9, 7)
    check(f"L=4 seed {seed}: rank guard", sv4 > RANK_TOL, f"worst min-sv {sv4:.4f}")
    n, g1, Th, w = most
    p2, p3, p4 = prefix(Th, w, 2), prefix(Th, w, 3), prefix(Th, w, 4)
    nl = null_p95(Th, w, 3)
    gaps.append(p3 - nl)
    mono = p2 < p3 < p4
    monotone_all = monotone_all and mono
    l4_k7[seed] = {"clears": p3 > nl, "mono": mono, "gap": p3 - nl}
    check(f"L=4 seed {seed}: at the most-spread row (depth {n}) the record prefix-3 "
          f"exceeds the fixed seeded 300-draw permutation-null p95 diagnostic and "
          f"the fixed-k profile is MONOTONE in k "
          f"(no stall)",
          p3 > nl and mono,
          f"global {g1:.3f}; profile {p2:.3f}/{p3:.3f}/{p4:.3f}; null p95 {nl:.3f}; "
          f"gap {p3 - nl:+.3f}")

# ===========================================================================
print("=" * 78)
print("Part 3  L = 4 robustness extension: seed set and half-filling control")
print("=" * 78)
for seed in (2026, 314, 7, 555):
    most, rows, sv4 = scan(env4, seed, 9, 7)
    n, g1, Th, w = most
    p2, p3, p4 = prefix(Th, w, 2), prefix(Th, w, 3), prefix(Th, w, 4)
    nl = null_p95(Th, w, 3)
    mono = p2 < p3 < p4
    l4_k7[seed] = {"clears": p3 > nl, "mono": mono, "gap": p3 - nl}
    print(f"   K=7 extension seed {seed}: depth {n}, global {g1:.3f}, "
          f"profile {p2:.3f}/{p3:.3f}/{p4:.3f}, null p95 {nl:.3f}, "
          f"gap {p3 - nl:+.3f}, seeded_null_positive={p3 > nl}, monotone={mono}, "
          f"rank_sv={sv4:.4f}")
k7_seeds = (1, 4242, 99, 2026, 314, 7, 555)
check("K=7 robustness extension: all seven tested L=4 seeds exceed the fixed seeded "
      "300-draw null diagnostic and have "
      "monotone fixed-k profiles",
      all(l4_k7[s]["clears"] and l4_k7[s]["mono"] for s in k7_seeds),
      "gaps " + ", ".join(f"{s}:{l4_k7[s]['gap']:+.3f}" for s in k7_seeds))

k6 = {}
for seed in (1, 99, 2026):
    most, rows, sv4 = scan(env4, seed, 9, 6)
    n, g1, Th, w = most
    p2, p3, p4 = prefix(Th, w, 2), prefix(Th, w, 3), prefix(Th, w, 4)
    nl = null_p95(Th, w, 3)
    mono = p2 < p3 < p4
    k6[seed] = {"clears": p3 > nl, "mono": mono, "gap": p3 - nl}
    print(f"   K=6 half-filling seed {seed}: depth {n}, global {g1:.3f}, "
          f"profile {p2:.3f}/{p3:.3f}/{p4:.3f}, null p95 {nl:.3f}, "
          f"gap {p3 - nl:+.3f}, seeded_null_positive={p3 > nl}, monotone={mono}, "
          f"rank_sv={sv4:.4f}")
check("K=6 half-filling control: all three tested L=4 half-filling seeds exceed the "
      "fixed seeded 300-draw null diagnostic and have monotone fixed-k profiles",
      all(k6[s]["clears"] and k6[s]["mono"] for s in k6),
      "gaps " + ", ".join(f"{s}:{k6[s]['gap']:+.3f}" for s in k6))

# ===========================================================================
print("=" * 78)
print("Part 4  the two-point scaling verdict (labeled as such)")
print("=" * 78)
check("the L=4 seeded-null diagnostic gaps are COMPARABLE-OR-LARGER than the L=3 SET "
      "(panel-corrected fairness: the L=3 baseline is BOTH #3554 events; ranges "
      "overlap -- worst L=4 below best L=3; median ratio ~1.4x, NOT doubled; "
      "magnitudes instance/seed-labeled)",
      float(np.median(gaps)) > float(np.median(gap3_set)),
      f"L=3 set {[f'{g:+.3f}' for g in gap3_set]} (median "
      f"{np.median(gap3_set):+.3f}) -> L=4 {[f'{g:+.3f}' for g in gaps]} "
      f"(median {np.median(gaps):+.3f}; ratio "
      f"{np.median(gaps)/np.median(gap3_set):.2f}x)")
check("THE LOAD-BEARING POSITIVE: the fixed-k profile is MONOTONE at the most-spread "
      "row of EVERY tested L=4 seed (7/7 K=7 seeds + a K=6 half-filling control) -- "
      "seed-robust monotonicity at the larger period; consistent with, NOT "
      "establishing, strengthening (at L=3 monotonicity was event-specific)",
      monotone_all
      and all(l4_k7[s]["clears"] and l4_k7[s]["mono"] for s in k7_seeds)
      and all(k6[s]["clears"] and k6[s]["mono"] for s in k6))
note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
check(
    "source note declares fixed seeded 300-draw sampled-null scope",
    "fixed seeded 300-draw sampled-null diagnostic" in note_text
    and "not an exact enumeration of all label permutations" in note_text,
)
check(
    "source note forbids exhaustive, certified-bound, or MC-free null theorem",
    "does not claim an exhaustive permutation-null p95" in note_text
    and "finite-sample upper confidence bound" in note_text
    and "Monte-Carlo-free null theorem" in note_text,
)
note_flat = " ".join(note_text.split())
check(
    "source note rescopes dependencies to finite runner-defined diagnostic",
    "dependency-edge rescope repair" in note_flat
    and "does not use the #3554 fixed-prefix-`k` packet" in note_flat
    and "as load-bearing one-hop authorities" in note_flat
    and "current source-positive is exactly the runner-defined diagnostic" in note_flat,
)
check(
    "source note forbids promotion to upstream framework laws",
    "must not cite this packet as a retained derivation of the #3554 fixed-prefix-`k` law" in note_flat
    and "the #3507 Born-weighted trajectory/readout chain" in note_flat
    and "a physical `U(1)` gauge field" in note_flat
    and "all-permutations null theorem" in note_flat,
)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: scales #3554's named object (the fixed-prefix-k conditional law) from")
print("  L=3 to L=4 (rings; Z^3 untested -- geometry disclosed; two periods = a")
print("  two-point trend, labeled).  PANEL-CORRECTED FINDINGS: the L=3 baseline is the")
print("  SET of both #3554 events positive against the fixed seeded-null diagnostic")
print("  ({+0.088 stalled, +0.190 monotone} --")
print("  the stall is event-specific, not a period property); the L=4 gaps are")
print("  COMPARABLE-OR-LARGER (ranges overlap; median ~1.4x, not doubled).  THE")
print("  LOAD-BEARING POSITIVE: seed-robust fixed-k MONOTONICITY at L=4 (7/7 K=7")
print("  seeds + a 3/3 half-filling control in-runner) -- consistent with, not")
print("  establishing, strengthening with the period.  NOT claimed: gap growth as a")
print("  period law, concentration in the large-period limit, any CLT premise,")
print("  L>=5/Z^3 behavior, or gap universality (instance/seed-labeled).  Guards")
print("  are runner-local finite diagnostics, not inherited #3554/#3507/Born theorem")
print("  premises.  No exhaustive permutation-null p95, certified finite-sample bound,")
print("  or MC-free null theorem is claimed.  The U(1) factor is NOT identified with a")
print("  physical gauge field.")
print("  Discrete-time (retained R1 boundaries untouched).  No new axiom/primitive/")
print("  measure/weight; r untouched.")
if FAIL:
    raise SystemExit(1)
