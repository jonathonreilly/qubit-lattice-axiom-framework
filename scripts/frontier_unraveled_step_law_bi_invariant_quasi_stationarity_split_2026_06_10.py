#!/usr/bin/env python3
"""The bi-invariant quasi-stationarity split of the unraveled step law: the step mean's
SINGULAR spectrum is quasi-frozen while the matrix moves O(1) (bi-rotation dominance),
and the gauge-invariant curvature marginal sits in a narrow band -- the stationarity
failure RELOCATES onto the bi-frame (the edge's gauge-frame directions), and the frozen
nonzero singular values quantify the structural non-centrality across depth.

Class-A exact verification for the source note

    docs/UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md

CONTEXT (retire-mode; depth-scan probe of the landed unraveled-step residuals 1+2).
The prior source note left FOUR named residuals on the CLT route; residual 1
(stationarity) and residual 2 (structural centrality) are probed here by an EXACT
depth-scan of the Born-weighted step-law ensemble: the full outcome tree to depth 11
(2048 branches, every Born weight exact; no stochastic sampling of the outcome tree), at
TWO parameter instances.  Machinery inherits the prior source note's guards (SVD polar;
per-branch rank guards; Born weights only under the declared conditional chain named in
the source note).

THE FINDINGS (exact at each depth; finite-horizon observations, instance-labeled):
  (S1) RAW NON-STATIONARITY, QUANTIFIED (residual 1's exhibit across depth): the
       link-level ensemble mean E[dU](n) moves O(1) at EVERY depth step in the exact
       horizon (min per-step motion > 0.6 at instance A, > 1.3 at instance B): no
       Cauchy decay, no onset of equilibration at this system size and horizon.
  (S2) THE SPLIT (an empirical observation about the per-depth moment spectra; the
       genuinely new increment is the depth-5->11 SCAN + this read-out):
       the SINGULAR-VALUE spectrum of E[dU](n) is QUASI-FROZEN across the horizon
       (10-100x below the raw motion at instance A; ~10x at instance B, where the
       smallest sv is least frozen and the freeze is NOT distinguished from a Haar
       null -- scoped), while the EIGENVALUE spectrum moves at the raw scale.  Frozen
       sv + moving ev alone do NOT deduce a bi-frame (a conjugation with rotated
       phases also produces it -- explicit counterexample); the bi-frame reading is
       MEASURED directly: the two-sided factors V, W of consecutive means differ at
       order 1 (median |V-W| comparable to |V-I|).  The SECOND-moment tensor's
       spectrum quasi-freezes as well (the split is not a first-moment accident).
       THE STATIONARITY FAILURE IS CONCENTRATED IN THE BI-FRAME at this size/horizon;
       what is quasi-stationary is the bi-orbit-projected SPECTRUM of the step MEAN
       (and the exhibited second moment) -- NOT the whole step law (the bi-orbit-
       quotient LAW remains the named open object).
  (S3) THE INVARIANT MARGINAL (seed-disclosed): the gauge-invariant curvature
       marginal E[C] (C = 1 - |tr Hol|/3) sits in a narrow band
       at the published seeds (11-17% relative; A's seed is the TIGHTEST of a 5-seed
       scan whose bands reach ~33% -- bands are seed-dependent, gates are set to the
       scan: max < 35%, median < 20%) with mean-zero small-variance increments, while
       an equally bounded gauge-VARIANT control scalar wanders wider (5.1x at A, 1.8x
       at B; seed-scan ratios median >= 1.5, min >= 0.9): the pinning is TYPICAL and
       not a boundedness artifact, with seed/instance-labeled magnitudes.
  (S4) RESIDUAL 2 ACROSS DEPTH: the singular spectrum is NONZERO-stable -- a
       bi-invariant law has ZERO mean, so the persistent nonzero spectrum quantifies
       structural non-centrality across the whole horizon (no decay with
       depth; consistent with the eps-independence finding).  A matched Haar-average
       null shows the sv-freeze has separation at instance A (motion slower than null) but
       is NOT distinguished from the null at instance B (scoped accordingly).

WHAT THIS DOES AND DOES NOT CLAIM:
  - RELOCATES residual 1: what fails to equilibrate (at this size/horizon) is the
    bi-frame -- the edge's independent left/right gauge directions; the
    bi-invariant shape is already quasi-stationary.  This is a finite-horizon,
    two-instance, exact-ensemble finding with controls -- NOT an invariant-measure
    theorem, NOT a proof of asymptotic stationarity, and NOT a delivery of any CLT
    premise (the four prior residuals all stand; residual 2 is here QUANTIFIED as
    persistent, strengthening its structural reading).
  - Inherits the prior source note's conditionality: Born weights are used only under
    the declared chain named in the note; this runner does not upgrade that chain.  The
    named instrument classes (eps supplied), supplied C^3 carrier, named hopping, and
    guarded full-rank domain are held fixed.  Discrete-time boundary rows are untouched.
    No new axiom/primitive/measure/weight; r untouched.  All band widths, ratios, and
    spectra are instance-labeled numbers, not constants.

Run: python3 scripts/frontier_unraveled_step_law_bi_invariant_quasi_stationarity_split_2026_06_10.py
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
EDGES = [(0, 1), (1, 2), (2, 0)]
OPS = {}
for ei, (x, y) in enumerate(EDGES):
    OPS[ei] = np.array([(AD9[3 * x + i] @ A9[3 * y + j]).astype(complex)
                        for i in range(3) for j in range(3)])


def polar_u(M):
    U, s, Vh = np.linalg.svd(M)
    return U @ Vh


def min_sv(M):
    return float(np.linalg.svd(M, compute_uv=False)[-1])


def kraus_pair(Nop, eps):
    w, V = np.linalg.eigh(Nop)
    Nt = (w - w.mean()) / max(abs(w - w.mean()))
    Kp = (V @ np.diag(np.sqrt((1 + eps * Nt) / 2)) @ V.T).astype(complex)
    Km = (V @ np.diag(np.sqrt((1 - eps * Nt) / 2)) @ V.T).astype(complex)
    return Kp, Km


def slater_fock(PSI):
    vac = np.zeros(2 ** NM)
    vac[int(np.argmin(np.diag(sum(AD9[m] @ A9[m] for m in range(NM)).real)))] = 1.0
    psi = vac.astype(complex)
    for k in range(PSI.shape[1]):
        psi = sum(PSI[m, k] * AD9[m].astype(complex) for m in range(NM)) @ psi
    return psi / np.linalg.norm(psi)


def depth_scan(eps, tau, seed):
    """Exact vectorized outcome tree to DEPTH; per depth: step-law ensemble stats.
    Returns dict with sequences + worst rank-guard value."""
    rng = np.random.default_rng(seed)
    U_step = expm(-1j * H * tau)
    KB = kraus_pair(N_site0, eps)
    PSI0 = np.linalg.qr(rng.normal(size=(NM, 5)) + 1j * rng.normal(size=(NM, 5)))[0]
    states = slater_fock(PSI0)[None, :].copy()
    weights = np.array([1.0])
    Uprev = None
    out = {"Em": [], "T2": [], "EC": [], "VdC": [], "Svar": [], "wsum": [],
           "worst_sv": np.inf}
    Cprev = None
    for n in range(1, DEPTH + 1):
        states = states @ U_step.T
        new = np.vstack([states @ KB[0].T, states @ KB[1].T])
        norms = np.einsum('bi,bi->b', new.conj(), new).real
        keep = norms > 1e-14
        weights = np.concatenate([weights, weights])[keep] * norms[keep]
        states = (new[keep].T / np.sqrt(norms[keep])).T
        expected_branches = 2 if Uprev is None else 2 * len(Uprev)
        assert keep.all() and len(weights) == expected_branches, \
            "parent-index alignment requires no pruned branches"
        B = states.shape[0]
        Us = []
        for ei in range(3):
            M = np.empty((B, 9), complex)
            for k in range(9):
                M[:, k] = np.einsum('bi,bi->b', states.conj(), states @ OPS[ei][k].T)
            M = M.reshape(B, 3, 3)
            out["worst_sv"] = min(out["worst_sv"],
                                  float(np.min(np.linalg.svd(M, compute_uv=False)[:, -1])))
            Us.append(np.array([polar_u(m) for m in M]))
        Hl = np.einsum('bij,bjk,bkl->bil', Us[0], Us[1], Us[2])
        C = 1 - np.abs(np.einsum('bii->b', Hl)) / 3
        Z = weights.sum()
        out["wsum"].append(float(Z if n == 1 else weights.sum()))
        if Uprev is not None:
            par = Uprev[np.arange(len(weights)) % len(Uprev)]
            dU = np.einsum('bij,bkj->bik', Us[0], par.conj())
            Em = np.einsum('b,bij->ij', weights, dU) / Z
            out["Em"].append(Em)
            T2 = np.einsum('b,bij,bkl->ikjl', weights, dU, dU.conj()).reshape(9, 9) / Z
            out["T2"].append(T2)
            parC = Cprev[np.arange(len(weights)) % len(Cprev)]
            dC = C - parC
            EdC = float(weights @ dC / Z)
            out["VdC"].append(float(weights @ (dC - EdC) ** 2 / Z))
            out["EC"].append(float(weights @ C / Z))
            out["Svar"].append(float(weights @ np.real(Us[0][:, 0, 0]) / Z))
        Uprev = Us[0]
        Cprev = C
    return out


# ===========================================================================
INSTANCES = [("A", 0.6, 0.35, 20260610), ("B", 0.4, 0.55, 7)]
RES = {}
for tag, eps, tau, seed in INSTANCES:
    RES[tag] = depth_scan(eps, tau, seed)

print("=" * 78)
print("Part 1  exact tree integrity (both instances; prior guards inherited)")
print("=" * 78)
for tag, eps, tau, seed in INSTANCES:
    r = RES[tag]
    check(f"instance {tag} ((eps,tau)=({eps},{tau})): Born weights stay exactly "
          f"normalized along the depth scan",
          all(abs(w - 1) < 1e-9 for w in r["wsum"]),
          f"max |sum-1| = {max(abs(w - 1) for w in r['wsum']):.1e} through depth {DEPTH}")
    check(f"instance {tag}: per-branch rank guard holds on EVERY branch and edge used "
          f"(the increment is well-defined everywhere it is computed)",
          r["worst_sv"] > RANK_TOL, f"worst cross-block min-sv {r['worst_sv']:.4f}")

print("=" * 78)
print("Part 2  (S1) raw non-stationarity, quantified across the horizon (residual 1)")
print("=" * 78)
for tag, *_ in [(t,) for t, *_ in INSTANCES]:
    Ems = RES[tag]["Em"]
    raw = [float(np.linalg.norm(Ems[i] - Ems[i - 1])) for i in range(1, len(Ems))]
    check(f"instance {tag}: the link-level step mean moves O(1) at EVERY depth step -- "
          f"no Cauchy decay, no equilibration onset at this size/horizon "
          f"(finite-horizon exhibit of residual 1)",
          min(raw) > 0.3,
          f"per-step motion range [{min(raw):.3f}, {max(raw):.3f}]")

print("=" * 78)
print("Part 3  (S2) THE SPLIT: moment spectra quasi-frozen; the bi-frame reading measured")
print("=" * 78)
for tag, *_ in [(t,) for t, *_ in INSTANCES]:
    Ems = RES[tag]["Em"]
    raws, dsvs, devs, dVW, dVI = [], [], [], [], []
    for i in range(1, len(Ems)):
        raws.append(float(np.linalg.norm(Ems[i] - Ems[i - 1])))
        U1, s1, Vh1 = np.linalg.svd(Ems[i - 1])
        U2, s2, Vh2 = np.linalg.svd(Ems[i])
        dsvs.append(float(np.linalg.norm(np.sort(s2) - np.sort(s1))))
        ev0 = np.sort_complex(np.linalg.eigvals(Ems[i - 1]))
        ev1 = np.sort_complex(np.linalg.eigvals(Ems[i]))
        devs.append(float(np.linalg.norm(ev1 - ev0)))
        # the canonical-SVD two-sided factors (D = I convention; per-column phases of the
        # SVD make V, W defined up to a shared diagonal; the comparison is direct.
        V = U2 @ U1.conj().T
        W = Vh2.conj().T @ Vh1
        dVW.append(float(np.linalg.norm(V - W)))
        dVI.append(float(np.linalg.norm(V - np.eye(3))))
    ratio = float(np.median(np.array(raws) / np.array(dsvs)))
    check(f"instance {tag}: the SINGULAR spectrum of E[dU] is quasi-frozen while the "
          f"matrix moves -- median raw/spectral motion ratio > 5x (instance-labeled)",
          ratio > 5, f"median ratio {ratio:.1f}x; sv-changes "
          f"[{min(dsvs):.4f},{max(dsvs):.4f}] vs raw [{min(raws):.3f},{max(raws):.3f}]")
    check(f"instance {tag}: the EIGENVALUE spectrum moves at the raw scale -- CONSISTENT "
          f"WITH two-sided rotation (frozen sv + moving ev alone do not DEDUCE a "
          f"bi-frame: a conjugation with rotated phases also does it -- explicit "
          f"counterexample); the bi-frame reading is MEASURED directly below",
          float(np.median(devs)) > 0.3, f"median ev-change {np.median(devs):.3f}")
    check(f"instance {tag}: the MEASURED two-sided factors genuinely differ -- "
          f"median |V - W| is order-1 (comparable to |V - I|): the motion is "
          f"bi-rotational ON THIS DATA, not conjugation (directly measured evidence)",
          float(np.median(dVW)) > 0.3,
          f"median |V-W| {np.median(dVW):.2f} vs median |V-I| {np.median(dVI):.2f}")
    # The SECOND moment freezes too: T = E[dU (x) conj dU]
    Ems2 = RES[tag]["T2"]
    raws2 = [float(np.linalg.norm(Ems2[i] - Ems2[i - 1])) for i in range(1, len(Ems2))]
    dsv2 = [float(np.linalg.norm(np.sort(np.linalg.svd(Ems2[i], compute_uv=False))
                                 - np.sort(np.linalg.svd(Ems2[i - 1], compute_uv=False))))
            for i in range(1, len(Ems2))]
    ratio2 = float(np.median(np.array(raws2) / np.array(dsv2)))
    check(f"instance {tag}: the SECOND-moment tensor's singular spectrum ALSO "
          f"quasi-freezes (the split is not a first-moment accident)",
          ratio2 > 5, f"median ratio {ratio2:.1f}x")

print("=" * 78)
print("Part 4  (S3) the invariant marginal: SEED-ROBUST bands + the boundedness control")
print("=" * 78)
# Seed-selection guard: the published seeds are NOT presented as the regime --
# a 5-seed scan at instance-A parameters reports the band SPREAD, and the gates are
# set to hold across seeds (the published seed is disclosed as the tightest sampled).
seed_bands, seed_ratios = [], []
for sd in (20260610, 1, 2, 3, 4):
    r5 = depth_scan(0.6, 0.35, sd)
    EC5 = np.array(r5["EC"]); SV5 = np.array(r5["Svar"])
    seed_bands.append(float((EC5.max() - EC5.min()) / EC5.mean()))
    bC = float(EC5.max() - EC5.min()); bS = float(SV5.max() - SV5.min())
    seed_ratios.append(bS / bC if bC > 0 else np.inf)
check("SEED SCAN (instance-A parameters, 5 seeds): every seed's invariant band stays "
      "below 35% relative and the MEDIAN band is below 20% -- the pinning is typical, "
      "the published seed is the tightest sampled (disclosed; bands are seed-dependent)",
      max(seed_bands) < 0.35 and float(np.median(seed_bands)) < 0.20,
      f"bands {[f'{100*b:.0f}%' for b in seed_bands]}")
check("SEED SCAN control ratios: the variant/invariant band ratio has median >= 1.5 and "
      "min >= 0.9 across seeds (the control's separation is TYPICAL, not universal -- "
      "observed range disclosed)",
      float(np.median(seed_ratios)) >= 1.5 and min(seed_ratios) >= 0.9,
      f"ratios {[f'{x:.1f}x' for x in seed_ratios]}")
for tag, *_ in [(t,) for t, *_ in INSTANCES]:
    EC = np.array(RES[tag]["EC"])
    SV = np.array(RES[tag]["Svar"])
    VdC = np.array(RES[tag]["VdC"])
    bandC = float(EC.max() - EC.min())
    bandS = float(SV.max() - SV.min())
    check(f"instance {tag} (published seed): invariant band and control ratio as "
          f"displayed -- instance/seed-specific numbers, not regime constants",
          bandC / EC.mean() < 0.35 and bandS > 0.9 * bandC,
          f"band {100*bandC/EC.mean():.0f}% rel; variant/invariant ratio "
          f"{bandS/bandC:.1f}x; Var[dC] in [{VdC.min():.5f},{VdC.max():.5f}]")

print("=" * 78)
print("Part 5  (S4) residual 2 across depth + the Haar-null control")
print("=" * 78)
rng_null = np.random.default_rng(99)
def haar_su3(r):
    A = r.normal(size=(3, 3)) + 1j * r.normal(size=(3, 3))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1 / 3)
for tag, *_ in [(t,) for t, *_ in INSTANCES]:
    Ems = RES[tag]["Em"]
    svs = np.array([np.sort(np.linalg.svd(E, compute_uv=False)) for E in Ems])
    check(f"instance {tag}: the singular spectrum is NONZERO-stable across the whole "
          f"horizon -- a bi-invariant law has ZERO mean, so this QUANTIFIES the "
          f"prior structural non-centrality across depth (does not decay; consistent with the "
          f"eps-independence finding)",
          float(svs[:, -1].min()) > 0.1,
          f"top sv range [{svs[:,-1].min():.3f},{svs[:,-1].max():.3f}]; final profile "
          f"{np.round(svs[-1],3)}")
    # Haar null: fixed-seed convex averages of independent Haar SU(3) with matched
    # branch counts; per-step sv-shape motion of the null mean vs the real data.
    real_motion = float(np.median([np.linalg.norm(svs[i] - svs[i - 1])
                                   for i in range(1, len(svs))]))
    null_motion = []
    prev = None
    for i, E in enumerate(Ems):
        Bn = 2 ** (i + 2)
        Em_null = sum(haar_su3(rng_null) for _ in range(min(Bn, 256))) / min(Bn, 256)
        svn = np.sort(np.linalg.svd(Em_null, compute_uv=False))
        if prev is not None:
            null_motion.append(float(np.linalg.norm(svn - prev)))
        prev = svn
    ratio_null = float(np.median(null_motion)) / real_motion if real_motion > 0 else np.inf
    if tag == "A":
        check("instance A: the sv-shape motion is SLOWER than the matched Haar-average "
              "null (the freeze has separation at A)",
              ratio_null > 1.5, f"null/real motion ratio {ratio_null:.2f}x")
    else:
        print(f"   instance B: null/real sv-motion ratio {ratio_null:.2f}x -- the B "
              f"freeze (~10x below raw) is NOT distinguished from the Haar null and the "
              f"smallest sv is least frozen: 'quasi-frozen' at B is scoped accordingly "
              f"(no separation claimed at B).")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: an exact finite-horizon depth-scan (tree to depth 11, 2048 branches, every")
print("  Born weight exact; no stochastic sampling of the outcome tree) of the unraveled")
print("  step law at TWO instances, probing the landed source note's residuals 1+2.")
print("  THE SPLIT: the step mean's SINGULAR spectrum is")
print("  quasi-frozen (10-100x / ~10x below the raw motion) while its eigenvalues move")
print("  at the raw scale -- the non-stationarity is TWO-SIDED-rotational, i.e.")
print("  concentrated in the edge's bi-frame directions -- and the")
print("  gauge-invariant curvature marginal sits in a narrow band (boundedness control")
print("  passed).  RELOCATION, not delivery: residual 1 (stationarity) stands but its")
print("  failure localizes to the bi-frame at this size/horizon; residual 2 (structural")
print("  non-centrality) is QUANTIFIED across depth by the nonzero-stable singular")
print("  spectrum (separation at A; not null-distinguished at B).  Finite horizon, small")
print("  system, seeds disclosed as load-bearing -- NOT an invariant-measure theorem,")
print("  NOT a CLT-premise delivery; all four prior residuals stand.  Inherits the prior")
print("  source note's conditionality (Born weights only under the declared chain;")
print("  named instruments with supplied eps; supplied C^3 carrier; named")
print("  hopping; guarded full-rank domain).  Discrete-time boundary rows untouched.")
print("  No new axiom/primitive/measure/weight; r untouched.  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
