# Unraveled Record Trajectories Supply a Non-Degenerate Step Distribution on the Induced Link (Generic Full-Rank Domain) — Four Named Residuals Remain on the CLT Route

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode; the stochastic-unraveling door named by #3499, opened exactly; panel-narrowed)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_unraveled_record_step_distribution_nondegenerate_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_unraveled_record_step_distribution_nondegenerate_2026_06_10.txt`
**Status:** source proposal; the audit lane grades — **this note's reachable status is
capped at conditional regardless of the runner result** (the Born cap below). Runner
`PASS=18 FAIL=0` — exact, deterministic, **no Monte Carlo**: the outcome tree is
*enumerated*, every branch and Born weight exact. A mandatory 4-lens adversarial panel
returned `land_with_edits`; **all ten required edits are applied.**

## What #3499 left open, and what this note answers

#3499 proved the interleaved **mean** dynamics converges to a configuration-limit delta
and **explicitly left the step-distribution question to the unraveling** (it made no
step-law claim — nothing is "broken"; the question is *answered*). This note opens that
door exactly: outcome-resolved trajectories of the named weak instruments, enumerated as
an exact finite outcome tree.

**The Born cap (owner-clarified; live-ledger-verified; panel-worded).** Born outcome
weights enter as a **conditional premise routed through the framework's Born
derived-chain** — `gleason_on_qubit_lattice_projection_lattice_narrow_theorem_note_2026-05-20`
(**retained**) + the Busch/POVM qubit-authority bridge
`busch_povm_effect_gleason_qubit_authority_bridge_narrow_theorem_note_2026-06-05`
(**retained_bounded**) + the assembly note
`born_rule_from_gleason_busch_derivation_note_2026-05-20` (on main, **unaudited**) —
**capped at the assembly note's unaudited status.** Not Record-supplied: the Record
axiom's disclaimer is supply-side only (the retained_no_go
`post_record_count_probability_firewall_2026-06-06`).

## The results (exact — runner `PASS=18 FAIL=0`)

**(U1) The unraveling, exactly.** Two-outcome weak instruments with exact Kraus
completeness for both named classes — I-B-type (color-blind: a function of the site-total
`N_x`) and I-A-type (frame-naming: a function of one mode number) — interleaved with the
derived flow. Exact Born weights sum to 1 (`10⁻¹⁰`); the weighted average reproduces the
deterministic channel exactly (`10⁻¹²`).

**(U2) The domain, guarded — and the non-degenerate spread on it (the repo-new
result).** `dU = U_eff(n)U_eff(n−1)†` exists only where the inter-site coherence block is
**full rank**. The structural rank-deficient locus is exhibited: **sub-minimal occupancy
`K<3` forces rank ≤ K exactly** (the #3398 precondition, algebraic); certain real
fillings are rank-deficient (the panel's companion finding); the nf=1 sea's block is
*scalar* — full-rank but spread-degenerate. The polar is **SVD-based** and **every branch
used is rank-guarded in-runner** (the draft's unguarded eigh-polar silently produced
garbage on degenerate branches — panel-caught, replaced; the draft's `PASS` was
true-but-non-generic). On the generic full-rank domain — **including a full-rank
near-sea state** (exhibited) — the Born-weighted step distribution has **strictly
positive spread for both instrument classes** (variances instance-labeled; spread → 0 as
`ε → 0` as expected for a weak instrument, with `var ∼ ε²` — which rules out a numerical
floor and claims nothing more).

**(U3) The honest gaps — the CLT route needs *four* named residuals** (panel-completed
list, checked against the on-main heat-kernel CLT note's own premises):

```
1  STATIONARITY        increments are state-dependent (exact exhibit);
                       trajectory equilibration unproven
2  CENTRALITY          E[dU] non-scalar on generic states, and the off-scalar part is
                       ε-INDEPENDENT — STRUCTURAL, not a small residual equilibration
                       plausibly closes without argument (special states can be scalar)
3  EDGE-IDENTITY       identical distribution across edges FAILS as-is
                       (E[dU] differs O(1) between edges — exhibited)
4  MANY-EDGE STRUCTURE cross-edge independence / the multi-edge convolution: untested
                       (single-edge increments only)
```

**(U4) The covariance split** *(the trajectory-level re-exhibit of #3499-M2 and the
on-main block-01 covariance content — cited, not claimed new)*. The I-B (color-blind)
unraveling is **exactly covariant** (`E[dU](g·ψ) = g E[dU](ψ) g†` at `10⁻⁹`; the
conjugate-representation Fock lift is pinned in-runner); the I-A (frame-naming)
unraveling breaks covariance at order 1 — anchored to *its* frame, the `{P_r}` datum.
The color-blind **orientation kicks confirm #3499-M2 at the trajectory level**; and there
is **no contradiction** with block-02/#3499-M4's projective "scalar zero" erasure — that
is the `ε→1` (full-strength) limit, whereas finite `ε` is the **weak-record regime** the
on-main pointer-erasure note names.

## Where this leaves the CLT route — the next paths this opens

The route's standing after this note: the step distribution **exists** — exact,
Born-capped, non-degenerate on the guarded generic domain, gauge-covariant for the
color-blind class — and four named residuals remain (stationarity; structural
centrality; edge-identity; many-edge structure). These are **the next paths this opens,
not a wall that closes.** Everything is discrete-time (the retained R1 boundaries —
`record_classical_semigroup`, `record_markov_generator_embeddability` — are untouched);
the link remains slaved (blocks 01–03). Conditional on: the supplied `C³` carrier; the
named hopping; the named instrument classes (`ε` a supplied parameter of the standing
instrument admission); and **Born at its derived-chain cap**. No new axiom, primitive,
measure, or weight; `r` untouched; all spreads/variances instance-labeled. The audit
lane grades.

**Repo-new content** (panel-rated): U2 — the existence of the non-degenerate
Born-weighted step distribution on the generic guarded domain — plus the
trajectory-level orientation finding. U1 is textbook machinery instantiated; U3/U4's
covariance content re-exhibits block-01 at the discrete-instrument trajectory level.

## Cross-references

- The mean-level delta and the doors paragraph this answers: PR #3499 (branch-only; PR
  open). The almost-periodicity context: PR #3491 (branch-only; PR open).
- The Born derived chain (live-ledger statuses): retained Gleason; retained_bounded
  Busch bridge; the unaudited assembly note
  `born_rule_from_gleason_busch_derivation_note_2026-05-20`; the supply-side disclaimer
  `post_record_count_probability_firewall_2026-06-06` (retained_no_go).
- The nearest prior art whose content U3/U4 re-exhibit:
  [`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  (block 01, on main). The CLT premises this checks against:
  [`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08`](EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md)
  (on main). The weak-record regime naming:
  [`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  (block 02 lineage, on main).
- The `{P_r}` anchoring: the four-hats stratification (#3453, on main); the unistochastic
  fork (#3436, on main).
- Standard math (method only): Kraus instruments and unravelings; quantum-trajectory
  trees; weak measurements; SVD polar decomposition; conjugate representations.
