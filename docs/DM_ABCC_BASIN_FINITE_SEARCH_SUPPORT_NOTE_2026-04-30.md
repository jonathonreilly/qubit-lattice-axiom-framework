# DM A-BCC Basin Finite-Search Support Note

**Primary runner:** scripts/frontier_dm_abcc_basin_enumeration_completeness.py

**Date:** 2026-04-30 (2026-05-18: claim_scope formalized as conditional
provenance for a finite scan only per audit verdict boundary
instruction).
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-18 narrowing):** the load-bearing content
of this note is **conditional provenance for a finite scan only**:
the salvaged finite-search observations (30 PASS stamps on a large
bounded scan, five named chart representatives Basin 1/N/P/X/2 on
the tested source surface, active-chamber classification of C_base
vs C_neg rows on the printed finite representatives) are recorded
from the prior archived wrapper. This note **does NOT** claim
exhaustiveness, an audited bounded theorem, or that no narrow basin
was missed. The audit verdict's repair sub-target ("add the archived
wrapper and/or completed runner certificate as direct audit inputs,
then re-audit the finite-search observations under the non-exhaustion
scope") remains separate open work; the archived source wrapper at
`archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/`
is referenced but not in-`docs/` retained.
**Status authority:** independent audit lane only.
**Status:** support. Salvage note for finite-search observations preserved
after the A-BCC basin-enumeration completeness wrapper failed audit.

---

## 0. Provenance

The source wrapper
[`DM_ABCC_BASIN_ENUMERATION_COMPLETENESS_THEOREM_NOTE_2026-04-20.md`](../archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/DM_ABCC_BASIN_ENUMERATION_COMPLETENESS_THEOREM_NOTE_2026-04-20.md)
is archived under recovery tag
`archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/`.
The audit rejected the theorem-grade exhaustiveness claim because a dense
grid plus local minimization is not a proof that no narrow basin was missed.

## Archived wrapper + runner certificate (load-bearing for restricted packet, inlined 2026-05-18)

The audit verdict on this note (claim_type `bounded_theorem`,
verdict `audited_conditional`) identified one packet-visibility gap:
the archived source wrapper at
`archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/`
and the corresponding runner certificate were referenced but
not directly visible inside the retained docs packet. This section
inlines that load-bearing content so the finite-search provenance is
auditable without leaving the retained docs surface.

**Scope of this inlining.** The audit verdict also flagged that the
runner script `scripts/frontier_dm_abcc_basin_enumeration_completeness.py`
hard-codes the retained basin chart and expected signature labels — i.e.
the runner does not independently derive all listed observations from
axioms. That is a derivation-from-axioms issue and is **not** addressed by
this inlining. This repair only addresses packet visibility of the
referenced archive + cached runner stdout. The note's claim scope remains
**finite-search provenance under explicit non-exhaustion**; nothing in
this section promotes the bounded finite-search observations to an
exhaustiveness theorem.

### A. Archived wrapper provenance

- **Archive path:** `archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/DM_ABCC_BASIN_ENUMERATION_COMPLETENESS_THEOREM_NOTE_2026-04-20.md`
- **Archive directory naming:** `dm-abcc-finite-search-salvage-2026-04-30/`
  encodes the failure reason — a finite/heuristic search was promoted to
  a completeness theorem; salvage attempted in this support note.
- **Wrapper status line (verbatim from the archived header):**
  > **Status:** RETRACTED 2026-04-30 — audit failed; this note is
  > archived under `archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/`.
  > Claims below are NOT supported by current runners or current audit lane.
- **Wrapper retraction rationale (verbatim from archived `## Retraction`
  section, sourced from `docs/audit/data/audit_ledger.json`):**
  > Issue: the runner verifies a large finite search and reproduces 30
  > PASS stamps, but the note promotes that search to a theorem-grade
  > exhaustiveness certificate. Why this blocks: a dense grid plus
  > Nelder-Mead can miss a narrow basin between seeds; the empirical
  > 99.5-percentile Lipschitz estimate is not a worst-case bound, the
  > far-field exclusion is random sampling rather than an analytic lower
  > bound, and the claim that any unknown candidate basin would be
  > reached analogously is exactly the missing theorem. Repair target:
  > replace the heuristic certificate with an interval/branch-and-bound
  > proof over the R=50 box, or a computer-algebra/root-isolation
  > enumeration with certified eigenvalue-gap/Lipschitz bounds and a
  > deterministic far-field asymptotic exclusion. Claim boundary until
  > fixed: it is safe to claim that the current runner found only
  > Basin 1, Basin 2, and Basin X in the active chamber under the
  > retained sigma set, clustered them to the five-basin chart, and
  > found no additional basin in this finite multistart/random-sampling
  > scan; it is not an audited retained completeness theorem.

The current support note inherits exactly the wrapper's "safe claim
boundary" sentence as its retained scope; everything beyond that
sentence is left out of this support packet.

### B. Archived wrapper finite-search observations (verbatim from archive)

The following observations are the load-bearing finite-search content
from the archived wrapper, preserved here under the explicit
non-exhaustion scope. Coordinates and stamp counts are quoted from the
archived note; their auditable provenance is the cached runner
certificate in Section C.

- **Runner result on land:** `PASS = 30, FAIL = 0` on the bounded
  finite scan (no exhaustion claim).
- **Retained finite-scan chart (five basins, source-surface
  coordinates `(m, δ, q_+)`):**
  - Basin 1 = (0.657061, 0.933806, +0.715042); σ = (2,1,0); C_base; IN chamber
  - Basin N = (0.501997, 0.853543, +0.425916); σ = (2,1,0); C_base; OUT of chamber
  - Basin P = (1.037883, 1.433019, −1.329548); σ = (2,1,0); C_neg;  OUT of chamber
  - Basin 2 = (28.006,    20.722,    +5.012);    σ = (2,1,0); C_neg;  IN chamber
  - Basin X = (21.128264, 12.680028, +2.089235); σ = (2,0,1); C_neg;  IN chamber
- **Active-chamber finite-scan partition** (the C_base vs C_neg split
  on the printed finite representatives):
  - C_base ∩ chamber on the printed representatives: `{Basin 1}`
  - C_neg ∩ chamber on the printed representatives: `{Basin 2, Basin X}`
  - Out-of-chamber finite-scan representatives: `{Basin N, Basin P}`
- **Bookkeeping correction recorded by the wrapper:** Basin 2 is
  present in the finite scan's σ=(2,1,0) IN-chamber slice but was
  omitted from the older four-basin enumeration in
  `DM_ABCC_CLOSURE_VIA_CHAMBER_BOUND_AND_DPLE_F4_NOTE_2026-04-19.md`.
  The finite scan therefore records a five-basin print; this is a
  bookkeeping-level correction on the finite-search surface only and
  carries no exhaustiveness claim on the larger chart problem.

### C. Cached runner certificate (verbatim stdout)

`scripts/frontier_dm_abcc_basin_enumeration_completeness.py` is the
companion runner. Its completed stdout under cache key
`logs/runner-cache/frontier_dm_abcc_basin_enumeration_completeness.txt`
(runner SHA-256
`cb0d1b2f7c2a5ffdc7b7b5d4f9af3e395ea50de047ba43e182da85c9281d023d`,
`exit_code: 0`, `elapsed_sec: 409.70`, `status: ok`,
TOTAL `PASS=30 FAIL=0`) is reproduced below verbatim to make the
PASS provenance auditable inside the retained packet.

```
========================================================================
DM A-BCC basin-enumeration completeness certificate
========================================================================
Retained sigma set: [(2, 1, 0), (2, 0, 1), (0, 1, 2), (1, 2, 0)]
Retained basins:    ['Basin 1', 'Basin N', 'Basin P', 'Basin X', 'Basin 2']
Enclosure R:        50.0
Grid N per axis:    15  (N^3 = 3375 seeds / sigma)

--- T1: bounded search enclosure for chi^2 = 0 points ---
  [PASS] All five retained basins fit within |coord| ≤ 30  (max coord across basins = 28.006)
  [PASS] Enclosure R = 50.0 strictly contains all five basins  (max coord = 28.006 < R = 50.0)
  [PASS] Far-field scan: no chi^2 < 1e-5 found at ||coord|| > R over 1412 chamber samples  (min chi^2 at ||coord|| > R = 3.526e-04)
  [PASS] Asymptotic chi^2 on ray dir≈[0.86 0.43 0.26] stabilises and is bounded away from 0  (chi2 seq = ['1.70e-01', '1.75e-01', '1.77e-01', '1.77e-01'])
  [PASS] Asymptotic chi^2 on ray dir≈[0.36 0.73 0.58] stabilises and is bounded away from 0  (chi2 seq = ['1.77e-01', '1.83e-01', '1.84e-01', '1.84e-01'])
  [PASS] Asymptotic chi^2 on ray dir≈[0.28 0.28 0.92] stabilises and is bounded away from 0  (chi2 seq = ['1.89e-01', '1.92e-01', '1.93e-01', '1.93e-01'])

--- T2: dense grid + multistart chi^2 = 0 enumeration ---
    grid seeds (chamber-compatible): 1575 per sigma
    total multistart evaluations: 6300
    sigma = (2, 1, 0): 2 distinct chi^2 = 0 chart points in chamber
        [0.6571 0.9338 0.715 ]
        [28.0062 20.7218  5.0116]
    sigma = (2, 0, 1): 1 distinct chi^2 = 0 chart points in chamber
        [21.1283 12.68    2.0892]
    sigma = (0, 1, 2): 0 distinct chi^2 = 0 chart points in chamber
    sigma = (1, 2, 0): 0 distinct chi^2 = 0 chart points in chamber
    total distinct chart points across all 4 sigmas: 3
  [PASS] Enumeration discovered at least 3 distinct chart points (sanity)  (found 3)
  [PASS] Enumeration discovered at most 8 distinct chart points (no runaway)  (found 3)

--- T3: all discovered minima cluster at retained basins ---
    [0.6571 0.9338 0.715 ]  -> Basin 1 @ dist 0.0000
    [28.0062 20.7218  5.0116]  -> Basin 2 @ dist 0.0005
    [21.1283 12.68    2.0892]  -> Basin X @ dist 0.0000
  [PASS] Every discovered minimum lies within 0.15 of some retained basin  (unmatched = 0)
  [PASS] Enumeration reproduces all 3 in-chamber retained basins  (in_chamber_basins = ['Basin 1', 'Basin 2', 'Basin X'], matched = ['Basin 1', 'Basin 2', 'Basin X'])

--- T4: Lipschitz bound on chi^2 map over chamber enclosure ---
    sigma = (2, 1, 0): chi^2-gradient 99.5th pctl ≈ 0.225
    sigma = (2, 0, 1): chi^2-gradient 99.5th pctl ≈ 0.265
    sigma = (0, 1, 2): chi^2-gradient 99.5th pctl ≈ 0.404
    sigma = (1, 2, 0): chi^2-gradient 99.5th pctl ≈ 0.770
  [PASS] Lipschitz estimate is finite and bounded under all retained sigma  (L_max = 7.702e-01)
    grid half-diagonal = 6.1859
    L * h√3/2          ≈ 4.764e+00
  [PASS] Grid half-diagonal is strictly less than enclosure radius R  (seed_radius = 6.186, R = 50.0)
  [PASS] Basin-of-attraction (Basin 1, sigma = (2, 1, 0)): N-M recovers chi^2 = 0 from seed_radius  (6/8 perturbations recovered)
  [PASS] Basin-of-attraction (Basin N, sigma = (2, 1, 0)): N-M recovers chi^2 = 0 from seed_radius  (4/8 perturbations recovered)
  [PASS] Basin-of-attraction (Basin P, sigma = (2, 1, 0)): N-M recovers chi^2 = 0 from seed_radius  (3/8 perturbations recovered)
  [PASS] Basin-of-attraction (Basin X, sigma = (2, 0, 1)): N-M recovers chi^2 = 0 from seed_radius  (8/8 perturbations recovered)
  [PASS] Basin-of-attraction (Basin 2, sigma = (2, 1, 0)): N-M recovers chi^2 = 0 from seed_radius  (6/8 perturbations recovered)

--- T5: polynomial-degree (Bezout) upper bound on root count ---
    per-equation total degree (Hermitian pencil, 3x3) ≤ 8
    Bezout per sigma:  8^3 = 512
    Bezout total:      2048 (real root count ≤ this)
  [PASS] Bezout bound is finite (chi^2 = 0 system has finitely many roots)  (bound = 2048)
  [PASS] Bezout bound per sigma ≥ number of retained basins (consistency)  (bound = 512 ≥ 5 retained basins)

--- T6: cross-check with σ_hier uniqueness (σ=(2,1,0), 9/9 + sin δ_CP < 0) ---
    Basin 1: 9/9 = 9, sin δ_CP = -0.9874, chamber = True, joint pass = True
    Basin N: 9/9 = 9, sin δ_CP = +0.0397, chamber = False, joint pass = False
    Basin P: 9/9 = 9, sin δ_CP = -0.9411, chamber = False, joint pass = True
    Basin X: 9/9 = 9, sin δ_CP = +0.4188, chamber = True, joint pass = False
    Basin 2: 9/9 = 9, sin δ_CP = +0.5545, chamber = True, joint pass = False
  [PASS] Among the five retained basins, all joint-passers at σ=(2,1,0) are {Basin 1, Basin P}  (joint passers = ['Basin 1', 'Basin P'])
  [PASS] Among in-chamber basins, only Basin 1 passes joint (9/9 + sin δ_CP < 0) at σ=(2,1,0) — consistent with σ_hier uniqueness at the pinned chamber point  (in-chamber joint passers = ['Basin 1'])

--- T7: Sylvester signature partition across the five basins ---
  [PASS] Basin 1: signature component = C_base  (det = +0.9592)
  [PASS] Basin N: signature component = C_base  (det = +0.5669)
  [PASS] Basin P: signature component = C_neg  (det = -9.8609)
  [PASS] Basin X: signature component = C_neg  (det = -20296.1065)
  [PASS] Basin 2: signature component = C_neg  (det = -70538.6038)
  [PASS] A-BCC (chamber ∩ C_base) selects Basin 1 uniquely among the five retained basins  (in-chamber C_base basins = ['Basin 1'])

--- T8: exhaustiveness certificate ---
    enclosure R              = 50.0
    grid N                   = 15  (3375 seeds / sigma)
    grid half-diagonal       = 6.1859
    Lipschitz L_max          = 0.770
    chi^2 coverage / seed    ≈ 4.764e+00
    cluster tolerance        = 0.15
    min pairwise basin sep   = 0.3378
    max discovered->basin    = 0.0005
  [PASS] Cluster tolerance < half min basin separation (no cluster collisions)  (cluster tol = 0.15 < half min sep = 0.169)
  [PASS] Max discovered→basin distance < cluster tolerance  (max match distance = 0.0005 < 0.15)
  [PASS] Exhaustiveness certificate holds at stated (R, N, tolerance, L)  (R=50.0, N^3=3375, tol=0.15, half_min_sep=0.169, L=0.770)

TOTAL: PASS=30  FAIL=0
```

**Note on T8 label.** The cached stdout's T8 line is labelled
"exhaustiveness certificate" because the archived wrapper authored it
before retraction. This support note **does not adopt** that label:
the retained scope is finite-search provenance only, and the T8 line
is preserved verbatim above purely as a faithful reproduction of the
cached runner output. The audit boundary on this packet remains the
wrapper's safe-claim sentence — `{Basin 1, Basin 2, Basin X}` in the
active chamber on this finite scan, no additional basin in this finite
multistart/random-sampling scan — and explicitly **not** an audited
retained completeness theorem.

---

## 1. Surviving observations

The archived wrapper still records useful finite-search data:

- the runner reproduced a large bounded scan with 30 PASS stamps;
- the scan recovered five named chart representatives on the tested source
  surface: Basin 1, Basin N, Basin P, Basin X, and Basin 2;
- Basin 2 is a real bookkeeping correction to the older four-basin table on
  that finite scan surface;
- the active-chamber classification recorded by the scan separates the
  C_base row from the C_neg rows on the printed finite representatives.

## 2. Boundary

This note is not an exhaustion theorem. It preserves the finite-search
observations only. Any future claim that the A-BCC source-surface chart has
no additional narrow basins needs a separate proof surface or a stronger
auditable certificate.
