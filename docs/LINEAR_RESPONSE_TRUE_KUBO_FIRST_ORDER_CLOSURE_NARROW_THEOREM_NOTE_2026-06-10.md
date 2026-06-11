# Linear-Response Lane: the Literal First-Order Kubo Derivative, Matched to the Measured Map and Verified as Its s→0 Limit — Convergence Closure of the Open Gate's Named Path

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/linear_response_true_kubo_convergence_closure_2026_06_10.py`](../scripts/linear_response_true_kubo_convergence_closure_2026_06_10.py) (TOTAL: PASS=34 FAIL=0)
**Runner cache:** [`logs/runner-cache/linear_response_true_kubo_convergence_closure_2026_06_10.txt`](../logs/runner-cache/linear_response_true_kubo_convergence_closure_2026_06_10.txt)

## What this note is

The open-gate note
[`LINEAR_RESPONSE_DERIVATION_NOTE.md`](LINEAR_RESPONSE_DERIVATION_NOTE.md)
(ledger row `linear_response_derivation_note`, currently an open gate)
names its own closure path in its 2026-06-07 "Open-gate perimeter" section:

> "The follow-on lane explicitly named in §"The heuristic" of this note
> (`scripts/linear_response_true_kubo.py`) remains the closure path for
> the literal Kubo theorem."

This note **completes and hardens that named path** and proposes the gate
for closure on that basis. The landed path runner
([`scripts/linear_response_true_kubo.py`](../scripts/linear_response_true_kubo.py),
frozen cache
[`logs/runner-cache/linear_response_true_kubo.txt`](../logs/runner-cache/linear_response_true_kubo.txt),
source note [`LINEAR_RESPONSE_TRUE_KUBO_NOTE.md`](LINEAR_RESPONSE_TRUE_KUBO_NOTE.md))
already implemented the parallel perturbation recurrence and ran positively
(r = 0.9716 across 44 families), but its own gate note marks that verdict
string as not load-bearing, and the comparison left unexplained magnitude
gaps (e.g. `G2_asym_z` measured +0.0531 vs kubo_true +0.3064) and one
unexplained sign miss (`R1_kreg_k15`). The new runner replaces correlation
evidence with a **limit identity**: the finite-difference measured response
converges to the derived derivative as the source strength s → 0, at the
textbook orders, on every family tested — once the derivative is computed
for the measured lane's own discretization.

## The theorem (narrow, runner-verified)

The measured lane (`ind.prop_beam`, used by both landed lanes and by the
battery) propagates one edge i→j with the factor
`exp(i k L (1 − f_edge)) · w · h²/L²` where the imposed field enters as the
**endpoint average** `f_edge(s) = ½(field[i] + field[j])`,
`field[i] = s/(r_i + 0.1)` (`uc.imposed_field`, x–z plane distance to the
source). Termwise differentiation of the finite propagation map at s = 0 —
the same one-line Leibniz step as the landed bounded theorem, applied to
this edge factor — gives the parallel perturbation recurrence

```
A_j  = Σ_{i→j} A_i · exp(i k L) · w · h²/L²
B_j  = Σ_{i→j} [B_i + A_i · (−i k L · g_edge)] · exp(i k L) · w · h²/L²
g_edge = ½ ( 1/(r_i+0.1) + 1/(r_j+0.1) )
d(cz)/ds |₀ = (1/T) Σ_det (z_j − cz_free) · 2 Re[A_j* B_j]
```

with the measured lane's own sweep order and prune rule (`|A| < 1e-30`).
**With this g_edge the recurrence is the exact first derivative of the
measured map**, and the runner verifies it as a limit, not a correlation:

1. **Convergence ladder (16 families, including all three residual cases
   `G2_asym_z`, `H1_ring`, `L1_longrange`, plus the landed lane's sign miss
   `R1_kreg_k15`, spanning all three groups).** Forward differences
   `(cz(s)−cz(0))/s` at s = 4e-3 … 2.5e-4 converge to `kubo_end` at O(s)
   (last-pair error ratios 0.49–0.53); centered differences converge at
   O(s²) (ratios ≈ 0.25); Richardson extrapolation of the centered ladder —
   an independent high-order method using only propagator runs, no B
   recurrence — agrees with `kubo_end` to ≤ 1.7e-7 relative, and an
   independent 5-point O(s⁴) stencil to ≤ 1.7e-7 relative, on all 16.
2. **Full live panel (39 families) at two steps.** Sign agreement vs
   `kubo_end` is **39/39 at both s = 1e-3 and s = 5e-4, with no
   exclusions**. Correlation r(kubo_end, measured) = 0.99941 at s = 1e-3
   and 0.99985 at s = 5e-4 (> the cached 0.9716, rising toward 1);
   through-origin slope 1.0236 → 1.0118 (walking to 1 at O(s));
   rms relative deviation 6.8% → 3.4% (halving with s).
3. **Frozen artifacts reproduced.** The landed runner is imported (not
   transcribed) and its `kubo_true` and `measured` columns are reproduced
   live for all 44 families against the SHA-pinned cache (≤ 1.5e-6); the
   cache's own headline statistics (r = 0.9716 / 0.9875 / 0.9793 / 0.9995,
   42/44 signs, ratio stats) recompute from its columns; the heuristic
   lane's frozen log (r = 0.5605, 36/44) likewise.

## What the hardening found (honest findings, all runner-verified)

- **The landed runner's `kubo_true` is the exact derivative of a
  *different* discretization, not of the measured map.** It samples the
  edge field at the edge midpoint (`g_mid = 1/(r_mid+0.1)`) where the
  measured lane endpoint-averages. The landed bounded theorem
  ([`LINEAR_RESPONSE_TRUE_KUBO_NOTE.md`](LINEAR_RESPONSE_TRUE_KUBO_NOTE.md),
  source scope: exact derivative *for the propagator with f = s/r_edge as
  defined there*) is untouched by this; what changes is the **comparison's
  interpretation**: measured(s) converges to the matched endpoint variant
  and NOT to the midpoint variant (Richardson sits ≥ 50× closer to
  `kubo_end` than the mid−end gap on every ladder family where they
  differ). The midpoint variant's per-family offset is s-independent and is
  the **dominant part of the cached magnitude gaps** (e.g.
  `A1_orig_Fam1_swept`: cached gap
  0.978 = 0.963 discretization offset + 0.015 finite-s error).
- **The three residual cases close.** `G2_asym_z`: exact derivative
  +0.0902 (measured +0.0531 at s = 1e-3 is the same sign with O(s) error;
  at the battery scale s = 4e-3 the family is genuinely nonlinear — the
  measured response there has the opposite sign of the derivative).
  `H1_ring`: −1.0934 (cached −2.1164 overstated ~2× by the midpoint
  offset). `L1_longrange`: −0.8133. All three converge with the full
  O(s)/O(s²) ladder.
- **The landed lane's "numerical edge case" reading of `R1_kreg_k15` is
  corrected.** The measured value (−0.853 at s = 1e-3) was real signal:
  the matched derivative is −0.8844 and the ladder converges to it
  (Richardson rel. error ≲ 1e-8). The landed +0.3069 sign miss was the
  midpoint-variant artifact, not measurement noise.
- **Panel classification is explicit.** 4 families are detector-dead
  (`I1_drift_y`, `T1_tree_fan4`, `H1_hub`, `X1_expander_k12`: free
  detector probability exactly 0 — measured ≡ 0 by the lane's centroid
  convention; no derivative exists to compare). 1 family is prune-zone
  (`R2_kreg_k8`: p_det ≈ 7e-63, below the lane's own |amp| < 1e-30 prune
  resolution; the matched derivative is ≈ 0, matching measured ≈ 0 at both
  steps — the cached `kubo_true` = +4.36 for R2 is a prune-semantics
  artifact of the landed B-pass continuing where the measured lane prunes).
  The remaining 39 are the live panel; nothing is excluded from it.
- **The heuristic is characterized, quantitatively.** The open-gate note's
  detector-only reweighting (recomputed live, matched to its frozen log to
  ≤ 1.5e-6) correlates with the exact derivative at only
  r = 0.52 on the live panel; on the three residual cases its sign is
  wrong while the exact derivative's sign is right — those are exactly the
  path-phase cross terms the detector-only reweighting drops and the B
  recurrence keeps.

## What is and is not claimed

**IS claimed (bounded to this lane):**
- The first-order response of the detector-centroid observable to the
  lane's declared 1/r source field is **derived in closed recurrence form**
  (the B_j perturbation propagator with the measured lane's endpoint-
  averaged edge factor) and **verified as the s → 0 limit** of the lane's
  finite-difference measured response: O(s) forward / O(s²) centered
  convergence on the 16-family ladder (including all three residual cases
  and the prior sign miss), two independent high-order cross-checks per
  family, 39/39 live-panel sign agreement at both tested steps, r and
  slope walking to 1 as s decreases.
- The previous heuristic (`kubo_heuristic = cz_weighted − cz_free`) is an
  approximation to this derivative, with its failure mode located: its
  residual sign misses are path-phase cross terms.
- The landed midpoint variant is the exact derivative of a variant
  (midpoint-sampled) discretization; its deviation from the measured map's
  derivative is quantified per family and explains the cached magnitude
  gaps and the R1 sign miss.

**IS NOT claimed:**
- Any second-order or nonlinear-regime statement (the sibling second-order
  lane [`LINEAR_RESPONSE_SECOND_ORDER_KUBO_NOTE.md`](LINEAR_RESPONSE_SECOND_ORDER_KUBO_NOTE.md)
  is untouched; the G2 sign reversal at s = 4e-3 is *reported* as a
  nonlinearity exhibit, not analyzed).
- Any retained-status claim, any change to the open-gate row's status, or
  any audit verdict — **the audit lane adjudicates**; this note only
  completes the gate note's named closure path and proposes closure.
- Any statement about the battery's PASS/FAIL rule, F~M scaling, Born
  readout, or the wave-equation (Lane 6) condition.
- Any contradiction of the landed bounded theorem's source scope (the
  midpoint-propagator derivative statement stands for its own propagator).

## Boundaries (honest)

- **This is the graph-family toy linear-response lane** (grown DAGs,
  held-out generators, off-scaffold layered generators) — the old
  graph-gravity response program. It is **NOT** the cubic-Coxeter geometric
  rows, and nothing here feeds the Regge/metric lanes.
- First order in s, at s = 0, for the specific propagator
  `exp(i k L (1−f)) · exp(−0.8 θ²) · h²/L²`, the specific regularized 1/r
  field, the specific detector-slice centroid readout, and the lane's
  sweep/prune conventions. Different propagators or fields require
  re-deriving g_edge.
- Finite-difference convergence is **exhibited on the 16-family ladder
  subset**; the other 23 live families are covered at two steps
  (s = 1e-3, 5e-4) by the panel statistics, not by full ladders. No tested
  family failed to converge; families not tested are not claimed.
- The 4 detector-dead families and the 1 prune-zone family are outside the
  theorem's domain (no detector probability / below prune resolution) and
  are listed, not silently dropped.
- Subset compute is live; the only frozen inputs are the two landed
  artifacts being reproduced (the true-kubo cache and the heuristic lane's
  frozen 44-family log), each parsed and recomputed, never trusted for the
  new claim. Default execution is the full live job (~6–10 min,
  `AUDIT_TIMEOUT_SEC = 1800` per
  [`docs/audit/RUNNER_CACHE_POLICY.md`](audit/RUNNER_CACHE_POLICY.md), same
  ceiling as the landed path runner).

## Forbidden-imports check

- No PDG or fitted value anywhere; no empirical constant enters. All
  thresholds are convergence-order bands (O(s) ⇒ ratio ½, O(s²) ⇒ ratio ¼)
  or print-precision reproduction tolerances.
- The 1/r field profile is the lane's **declared source profile**
  (`uc.imposed_field`, unchanged from the landed lanes), not an imported
  physical potential.
- The 44-family set, all generator parameters, and the s-ladder are the
  landed lanes' own conventions (epsilon 1e-3 is both landed lanes'
  default; the ladder brackets it both ways).
- Registered primitives are not consumed beyond their notes; no new
  primitive, axiom, or selector is introduced
  (cf. [`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`](ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md)).

## Load-bearing inputs (cited authorities)

| Authority | Role |
|---|---|
| [`scripts/linear_response_true_kubo_convergence_closure_2026_06_10.py`](../scripts/linear_response_true_kubo_convergence_closure_2026_06_10.py) | primary runner: matched derivative, convergence ladders, panel statistics, frozen-artifact reproduction |
| [`logs/runner-cache/linear_response_true_kubo_convergence_closure_2026_06_10.txt`](../logs/runner-cache/linear_response_true_kubo_convergence_closure_2026_06_10.txt) | SHA-pinned cache of the primary runner |
| [`docs/LINEAR_RESPONSE_DERIVATION_NOTE.md`](LINEAR_RESPONSE_DERIVATION_NOTE.md) | the open gate; names the closure path quoted above; defines the heuristic and the three residual cases |
| [`scripts/linear_response_derivation.py`](../scripts/linear_response_derivation.py) + [`logs/2026-04-07-linear-response-derivation.txt`](../logs/2026-04-07-linear-response-derivation.txt) + [`logs/runner-cache/linear_response_derivation.txt`](../logs/runner-cache/linear_response_derivation.txt) | heuristic lane: frozen 44-family log parsed and live-matched here |
| [`scripts/linear_response_true_kubo.py`](../scripts/linear_response_true_kubo.py) + [`logs/runner-cache/linear_response_true_kubo.txt`](../logs/runner-cache/linear_response_true_kubo.txt) + [`logs/2026-04-07-linear-response-true-kubo.txt`](../logs/2026-04-07-linear-response-true-kubo.txt) | the gate's named closure path: imported live and reproduced against its cache; supplies the recurrence form and the midpoint variant |
| [`docs/LINEAR_RESPONSE_TRUE_KUBO_NOTE.md`](LINEAR_RESPONSE_TRUE_KUBO_NOTE.md) | landed bounded theorem for the midpoint propagator (scope untouched; see "What the hardening found") |
| `scripts/universality_classifier.py`, `scripts/independent_generators_heldout.py`, `scripts/global_coherence_off_scaffold.py` | the lane's declared 44-family generator surfaces and propagator (imported, unmodified) |

## Bottom line

> The gate note's named closure path is complete: the literal first-order
> Kubo derivative of the lane's measured centroid response exists in closed
> recurrence form — the parallel perturbation propagator B_j with the
> measured lane's own endpoint-averaged edge field — and the measured
> finite-difference response converges to it as s → 0 at the expected
> orders on every family tested, including all three residual cases the
> heuristic missed and the one sign miss the landed midpoint variant left
> unexplained. Live-panel sign agreement is 39/39 at both tested steps with
> the dead/prune rows classified, not hidden. The heuristic of the open
> gate is now characterized as a coarse approximation to this derivative.
> Whether the `linear_response_derivation_note` row closes is for the
> independent audit lane; this packet supplies the completed, hardened
> path it names.
