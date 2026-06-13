#!/usr/bin/env python3
"""The three-point period series (L = 3, 4, 5) of the record-conditional U(1) law shows
NO SYSTEMATIC PERIOD STRENGTHENING: L=4's uniformly clear fixed-k gains (min-gain >=
0.029 every seed) do NOT persist at L=5 (4/6 clear, 2/6 marginal at ~0.005);
sampled-null clearing drops from all-tested to 5/6; and the gap medians are trendless
({~0.14, ~0.19, ~0.09}).  The criterion-free min-gain ledger replaces the
tolerance-sensitive "monotone/stall" dichotomy (whose strict-float form would even
mislabel the #3554 stall).

Finite deterministic source-packet verification for exact finite-tree/profile/rank/
min-gain computations in the source note, plus a deterministic fixed
300-permutation sampled-null comparison. This runner does not certify an exact
full-permutation null.

    docs/RECORD_CONDITIONAL_LAW_THREE_POINT_PERIOD_SERIES_BOUNDED_THEOREM_NOTE_2026-06-11.md

CONTEXT (three-point period-series source proposal continuing #3555).  #3555
established seed-robust fixed-k monotonicity at L = 4 with gaps comparable-or-larger than
the L = 3 set (baseline-fairness-corrected).  THIS NOTE EXTENDS THE SERIES TO L = 5
(15 modes, 32768-dim Fock) -- made cheap by the expm_multiply pattern: the step unitary
is NEVER materialized (sparse action only; a dense U at L = 5 would be 17 GB and is
forbidden by the standing memory contract).  Uniform machinery across all three periods;
SIX seeds at L = 5 (the standing adversarial-seed policy); the L = 3 and L = 4 baselines
recomputed in-runner as SETS (the #3555 baseline-fairness lesson applied from the start).

THE FINDINGS (exact finite-tree evolution; fixed 300-permutation sampled-null p95;
finite horizon; three periods -- a THREE-POINT series, labeled; the per-event
statistic is the CRITERION-FREE minimum k-step gain min(p3-p2, p4-p3)):
  (G1) THE MIN-GAIN LEDGER: L=3 events {~0.0001 (the #3554 stall), ~0.155}; L=4
       {0.030, 0.029, 0.068} -- uniformly CLEAR gains; L=5 {~0.014, ~0.043, ~0.051,
       ~0.005, ~0.028, ~0.005} -- 4/6 clear, 2/6 MARGINAL.  PRECISION (panel-required
       disclosure): #3555's literal headline criterion was STRICT monotonicity
       (min-gain > 0), and THAT PERSISTS 6/6 at L=5 (gated below) -- what does NOT
       persist is the gain MAGNITUDE ('clarity'): L=4's uniform >= 0.029 drops to
       2/6 marginal ~0.005.  NO SYSTEMATIC STRENGTHENING of the magnitudes; the
       strict-monotonicity signature itself survives three-point (1/2, 7/7, 6/6).
  (G2) SAMPLED-NULL CLEARING DROPS FROM ALL-TESTED TO TYPICAL: 5/6 L=5 seeds clear their
       fixed 300-permutation sampled null; seed 20260611's most-spread event does NOT (gap
       -0.030) -- the first non-clearing event of the series, disclosed.
  (G3) NO PERIOD TREND IN THE GAPS: medians ~{0.139, 0.193, 0.092} -- fluctuating,
       not monotone.  The Block-29 verdict ("comparable-or-larger, not doubled")
       extends: gap magnitudes are event/seed-dominated, not period-dominated.

THE THREE-POINT VERDICT: across L = 3, 4, 5 the record-conditional structure does not
STRENGTHEN systematically with the period -- gain magnitudes and sampled-null clearing both
regress at L=5 (2/6 marginal; 5/6 clearing -- the G2 failure is a SAMPLED-NULL
failure, not a monotonicity failure) -- while the strict-monotonicity signature
persists.  #3555's magnitude clarity was not a trend onset.  At accessible periods the conditional law's structure is
event/seed-dominated: period scans at these sizes cannot decide the conditional-law
question (an honest negative that redirects the program -- the next lever is analytic
or a different observable, not larger rings).

NOT claimed: exact full-permutation null, any asymptotic statement, concentration,
CLT premises, L >= 6 or Z^3 behavior (rings; geometry disclosed; L = 6 full trees
exceed the memory contract).
Conditionality inherited (#3554/#3555 chain): the Born derived-chain cap (audit lane
grades; statuses volatile); named instruments (eps = 0.6); supplied C^3 carrier; named
hopping (tau = 0.35); guarded full-rank domain; discrete-time (retained R1 boundaries
untouched).  The U(1) factor is NOT identified with a physical gauge field.  No new
axiom/primitive/measure/weight; r untouched.  All numbers seed/instance-labeled.

MEMORY (standing contract): sparse operators; Fock-diagonal Kraus vectors; NO dense
step unitary anywhere (expm_multiply action only); environments freed between periods.
Measured peak footprint ~2.5 GB (/usr/bin/time -l 'peak memory footprint'; max RSS
~1.4 GB) -- single-run safe; panels serialize.

Run: python3 scripts/frontier_record_conditional_law_three_point_period_series_2026_06_11.py
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
from pathlib import Path

PASS = 0
FAIL = 0
NOTE = Path(__file__).resolve().parents[1] / "docs" / (
    "RECORD_CONDITIONAL_LAW_THREE_POINT_PERIOD_SERIES_BOUNDED_THEOREM_NOTE_2026-06-11.md"
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
    Hstep = (-1j * TAU) * H.tocsc()                 # sparse ACTION only — never dense
    n0 = sum((AD[c] @ A[c]).diagonal().real for c in range(NC))
    Nt = (n0 - n0.mean()) / max(abs(n0 - n0.mean()))
    kp = np.sqrt((1 + EPS * Nt) / 2).astype(complex)
    km = np.sqrt((1 - EPS * Nt) / 2).astype(complex)
    OPS = [(AD[0 + i] @ A[NC + j]).astype(complex).tocsr()
           for i in range(3) for j in range(3)]
    ntot = sum((AD[m] @ A[m]).diagonal().real for m in range(NM))
    vac_idx = int(np.argmin(ntot))
    return {"NM": NM, "DIM": DIM, "AD": AD, "Hstep": Hstep, "kp": kp, "km": km,
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
        sf = expm_multiply(env["Hstep"], sf.T).T
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
        states = expm_multiply(env["Hstep"], states.T).T
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
            if n >= 4 and (most is None or g1 < most[1]):
                most = (n + 1, g1, Theta.copy(), weights.copy())
        detprev = d
    return most, rows, worst_sv


def event_stats(most):
    n, g1, Th, w = most
    p2, p3, p4 = prefix(Th, w, 2), prefix(Th, w, 3), prefix(Th, w, 4)
    nl = null_p95(Th, w, 3)
    # the CRITERION-FREE statistic: the minimum k-step gain (no monotone/stall
    # dichotomy -- strict-float would mislabel the #3554 stall, a 0.01 tolerance would
    # flip marginal events; the min-gain number itself is reported and gated on bands)
    return {"depth": n, "g1": g1, "profile": (p2, p3, p4), "null": nl,
            "gap": p3 - nl, "min_gain": min(p3 - p2, p4 - p3)}


# ===========================================================================
print("=" * 78)
print("Part 1  L = 3 baseline SET (both #3554 events) and L = 4 set (#3555 seeds)")
print("=" * 78)
env3 = build(3)
gaps3, mono3 = [], []
# the L=3 baseline events are PINNED at their LANDED depths (#3554/#3555: 4242@d9,
# 99@d7) -- the landed baseline set, not re-selected rows.  SELECTOR-COMPARABILITY
# CAVEAT (panel): L=4/L=5 use the argmin-coherence (most-spread) selector while L=3 is
# hand-pinned; the asymmetry is CONSERVATIVE for the negative verdict (worst-row picks
# and the pinned stall both lean toward marginality -- it cannot manufacture the
# no-strengthening conclusion).
for seed, dpin in ((4242, 9), (99, 7)):
    most, rows, sv = scan(env3, seed, 11, 5)
    check(f"L=3 seed {seed}: rank guard", sv > RANK_TOL, f"min-sv {sv:.4f}")
    st = event_stats((dpin, *rows[dpin]))
    gaps3.append(st["gap"])
    mono3.append(st["min_gain"])
    print(f"   L=3 seed {seed}: d{st['depth']} global {st['g1']:.3f} | "
          f"{st['profile'][0]:.3f}/{st['profile'][1]:.3f}/{st['profile'][2]:.3f} "
          f"min-gain {st['min_gain']:.4f} | gap {st['gap']:+.3f}")
check("L=3 set reproduces the #3555 baseline: min-gains {~0.0004, ~0.16} (one "
      "stall-like, one clear -- event-specific at L=3), gaps ~{+0.09, +0.19}",
      mono3[0] < 0.005 and mono3[1] > 0.05 and min(gaps3) > 0,
      f"min-gains {[f'{m:.4f}' for m in mono3]}; gaps {[f'{g:+.3f}' for g in gaps3]}")
del env3
env4 = build(4)
gaps4, mono4 = [], []
for seed in (1, 4242, 99):
    most, rows, sv = scan(env4, seed, 9, 7)
    check(f"L=4 seed {seed}: rank guard", sv > RANK_TOL, f"min-sv {sv:.4f}")
    st = event_stats(most)
    gaps4.append(st["gap"])
    mono4.append(st["min_gain"])
    print(f"   L=4 seed {seed}: d{st['depth']} global {st['g1']:.3f} | "
          f"{st['profile'][0]:.3f}/{st['profile'][1]:.3f}/{st['profile'][2]:.3f} "
          f"min-gain {st['min_gain']:.4f} | gap {st['gap']:+.3f}")
check("L=4 set reproduces #3555: UNIFORMLY CLEAR gains (min-gain > 0.02 every seed) "
      "and all-tested fixed sampled-null clearing",
      all(m > 0.02 for m in mono4) and all(g > 0 for g in gaps4),
      f"min-gains {[f'{m:.3f}' for m in mono4]}; gaps {[f'{g:+.3f}' for g in gaps4]}")

# ===========================================================================
print("=" * 78)
print("Part 2  L = 5 (15 modes, 32768-dim; expm_multiply action): SIX seeds")
print("=" * 78)
del env4
env5 = build(5)
gaps5, mono5, fails = [], [], []
for seed in (1, 4242, 99, 2, 7, 20260611):
    most, rows, sv = scan(env5, seed, 9, 8)
    check(f"L=5 seed {seed}: rank guard", sv > RANK_TOL, f"min-sv {sv:.4f}")
    st = event_stats(most)
    gaps5.append(st["gap"])
    mono5.append(st["min_gain"])
    if st["gap"] <= 0:
        fails.append(seed)
    print(f"   L=5 seed {seed}: d{st['depth']} global {st['g1']:.3f} | "
          f"{st['profile'][0]:.3f}/{st['profile'][1]:.3f}/{st['profile'][2]:.3f} "
          f"min-gain {st['min_gain']:.4f} | gap {st['gap']:+.3f}")
check("(G1) L=4's UNIFORM CLARITY DOES NOT PERSIST: at L=5 the min-gain ledger has "
      "4/6 clear (> 0.01) and 2/6 MARGINAL (< 0.01) -- no systematic period "
      "strengthening of the conditioning gains (the honest three-point finding)",
      sum(1 for m in mono5 if m > 0.01) == 4 and sum(1 for m in mono5 if m < 0.01) == 2,
      f"min-gains {[f'{m:.4f}' for m in mono5]}")
check("(G1b, panel-required) #3555's LITERAL criterion -- strict monotonicity "
      "(min-gain > 0) -- PERSISTS 6/6 at L=5: only the gain MAGNITUDE fails to grow "
      "(the weakening is of 'clarity', not of monotonicity)",
      all(m > 0 for m in mono5))
check("(G2) SAMPLED-NULL CLEARING DROPS FROM ALL-TESTED TO TYPICAL at L=5: 5/6 clear; the "
      "failing seed's event DISCLOSED (a sampled-null failure, NOT a monotonicity "
      "failure -- its min-gain is positive)",
      sum(1 for g in gaps5 if g > 0) == 5 and len(fails) == 1
      and mono5[5] > 0,
      f"gaps {[f'{g:+.3f}' for g in gaps5]}; non-clearing seed {fails}")

# ===========================================================================
print("=" * 78)
print("Part 3  (G3) the three-point gap series: NO period trend")
print("=" * 78)
m3, m4, m5 = (float(np.median(gaps3)), float(np.median(gaps4)),
              float(np.median([g for g in gaps5])))
check("the gap medians fluctuate with NO monotone period trend (the #3555 "
      "'comparable-or-larger, not doubled' verdict extends: at three points there is "
      "no growth law; gap magnitudes are event/seed-dominated)",
      not (m3 < m4 < m5) and not (m3 > m4 > m5),
      f"medians L=3/4/5: {m3:+.3f} / {m4:+.3f} / {m5:+.3f}")

note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
note_words = " ".join(note_text.replace("**", "").split())
check(
    "source note declares fixed 300-permutation sampled-null scope",
    "deterministic fixed 300-permutation sampled-null comparison" in note_words
    and "not an exact full-permutation or exhaustive permutation-null p95 certificate" in note_words,
)
check(
    "source note forbids exhaustive or MC-free null theorem",
    "does not claim an exhaustive permutation-null p95" in note_text
    and "Monte-Carlo-free null theorem" in note_text,
)
check(
    "source note declares dependency-edge rescope repair",
    "2026-06-13 dependency-edge rescope repair" in note_text
    and "current source-positive is exactly the finite-runner-defined diagnostic" in note_words,
)
check(
    "source note confines load-bearing inputs to runner-defined finite objects",
    "Load-bearing inputs are confined to the finite objects instantiated by" in note_text
    and "`K=5`, `K=7`, and `K=8`" in note_text
    and "explicit sparse Fock evolution and SVD-polar determinant readout" in note_text,
)
check(
    "source note makes inherited framework language non-load-bearing labels",
    '"Born", "record", "instrument", "C^3 carrier", "hopping",' in note_text
    and "not imported framework closures" in note_words,
)
check(
    "source note forbids downstream retained-derivation citations",
    "must not cite this packet as a retained derivation" in note_words
    and "Born/readout chain" in note_text
    and "framework-native `C^3` carrier" in note_text,
)
check(
    "source note forbids selector/null and record-conditional overclaim",
    "selector/null theorem beyond the code-defined sampled diagnostic" in note_words
    and "record-conditional interpretation from approved premises" in note_words
    and "large-period law" in note_words,
)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: extends the period series to three points (L = 3, 4, 5 rings; uniform")
print("  expm_multiply machinery -- no dense step unitary anywhere; measured peak")
print("  footprint ~2.5 GB, single-run safe, panels serialize).  THE MIN-GAIN LEDGER")
print("  replaces the monotone/stall dichotomy.  (G1) #3555's STRICT monotonicity")
print("  persists 6/6 at L=5; the gain MAGNITUDE does not (4/6 clear, 2/6 marginal):")
print("  no systematic strengthening.  (G2) sampled-null clearing drops from all-tested to")
print("  5/6 (failing seed disclosed).  (G3) gap medians {~0.14, ~0.19, ~0.09}:")
print("  trendless.  THREE-POINT VERDICT: the record-conditional structure is")
print("  event/seed-dominated at accessible periods -- period scans at these sizes")
print("  cannot decide the conditional-law question (the honest redirect: the next")
print("  lever is analytic or a different observable, not larger rings).  NOT claimed:")
print("  asymptotics, concentration, CLT premises, L>=6 (memory contract), Z^3.")
print("  Conditionality inherited (#3554/#3555: Born cap, named instruments, supplied")
print("  carrier, guarded domain, discrete-time, R1 boundaries untouched).  The U(1)")
print("  factor is NOT identified with a physical gauge field.  No new axiom/")
print("  primitive/measure/weight; r untouched.  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
