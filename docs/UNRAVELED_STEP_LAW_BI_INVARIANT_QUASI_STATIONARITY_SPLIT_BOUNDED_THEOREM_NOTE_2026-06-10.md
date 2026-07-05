# The Bi-Invariant Quasi-Stationarity Split of the Unraveled Step Law: the Stationarity Failure Localizes to the Bi-Frame (Measured), the Moment Spectra Are Quasi-Frozen

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** retire-mode depth-scan probe of the unraveled-step stationarity
and structural-centrality residuals. The claim is finite-horizon, small-system, and
instance/seed-labeled; it is not a CLT premise, invariant-measure theorem, asymptotic
stationarity theorem, or new measure/weight premise.
**Primary runner:** [`scripts/frontier_unraveled_step_law_bi_invariant_quasi_stationarity_split_2026_06_10.py`](../scripts/frontier_unraveled_step_law_bi_invariant_quasi_stationarity_split_2026_06_10.py)
**Runner cache:** [`logs/runner-cache/frontier_unraveled_step_law_bi_invariant_quasi_stationarity_split_2026_06_10.txt`](../logs/runner-cache/frontier_unraveled_step_law_bi_invariant_quasi_stationarity_split_2026_06_10.txt)
**Status authority:** source proposal; the independent audit lane grades. Runner
`PASS=21 FAIL=0` — exact deterministic outcome-tree enumeration to depth 11, exact
Born weights under the declared conditional chain, two parameter instances, a 5-seed
robustness scan, and a fixed-seed Haar-null diagnostic. The genuinely new increment over
[`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md)
is the **depth-5→11 scan** plus the **moment-spectrum read-out**; the qualitative
non-centrality and the curvature functional are prior landed-source content, attributed
up front.

## What is probed, and the honest first answer

The landed unraveled-step source note left four named residuals on the CLT route; this
note probes **residual 1 (stationarity)** and **residual 2 (structural centrality)**
with an exact depth-scan of the Born-weighted step-law ensemble. **(S1)** The
link-level step mean `E[dU](n)` moves
**O(1) at every depth step** (per-step motion ≥ 0.6 at instance A, ≥ 1.3 at B): no Cauchy
decay, no equilibration onset at this system size and horizon.

## The split (per-depth moment spectra — with the inference done honestly)

**(S2)** The **singular-value spectrum of `E[dU](n)` is quasi-frozen** (10–100× below the
raw motion at instance A; ~10× at B, where the smallest singular value is least frozen)
while the **eigenvalue spectrum moves at the raw scale**. Frozen singular values with
moving eigenvalues **do not by themselves deduce** a bi-frame (a conjugation with rotated
phases also produces that pattern — explicit counterexample); the bi-frame reading is
therefore **measured directly**: the two-sided factors `V, W` of consecutive means differ
at order 1 (median `|V−W|` comparable to `|V−I|`, both instances, in-runner). And the
**second-moment tensor's spectrum quasi-freezes as well**; the split is not a
first-moment accident. **Scope, precisely:** what is quasi-stationary is the
**bi-orbit-projected spectrum of the step *mean*** (and the exhibited second moment) —
*not* the whole step law; the bi-orbit-quotient **law** remains the named open object.
The stationarity failure is concentrated in the **bi-frame** — the edge's independent
left/right gauge directions — at this size and horizon.

**(S3) The invariant marginal, seed-disclosed.** The gauge-invariant curvature marginal
`E[C]` (from
[`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`](INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md))
sits in a narrow band at the published seeds (11–17% relative) — **and the published
instance-A seed is the tightest of a 5-seed scan whose bands reach ~33%**; the runner's
gates are set to the scan (max < 35%, median < 20%), so the pinning is **typical, with
seed-dependent magnitude**, not a regime constant. The boundedness control (an equally
bounded gauge-*variant* scalar) wanders wider — **5.1× at A, 1.8× at B**, scan ratios
median ≥ 1.5 with min ≥ 0.9 — typical separation, honestly gated.

**(S4) Residual 2 across depth, null-controlled.** The singular spectrum is
**nonzero-stable** across the whole horizon — a bi-invariant law has *zero* mean, so this
quantifies the structural non-centrality from the landed unraveled-step note across
depth (no decay; consistent with its `ε`-independence finding). A matched fixed-seed
**Haar-average null** shows the sv-freeze has separation at instance A (real motion
slower than the null) but is **not distinguished from the null at instance B** —
"quasi-frozen" at B is scoped accordingly.

## What this relocates, and what it does not deliver

- **Relocation, not delivery:** residual 1 stands, but its failure **localizes to the
  bi-frame** (measured, not just inferred) at this size and horizon; residual 2 stands,
  **quantified across depth**. No CLT premise is delivered; all four residuals from the
  landed unraveled-step note stand.
- **Honest grade:** finite horizon (depth 11), small system (3-ring), two instances plus
  a 5-seed scan, **seeds disclosed as load-bearing** — not an invariant-measure theorem,
  not a proof of asymptotic stationarity. All bands, ratios, and spectra are
  seed/instance-labeled numbers.
- **The path this opens:** the step law **modulo the bi-frame** — whether a group-level
  step measure can be built on the bi-orbit quotient, and what residual 3's
  edge-anchoring looks like there — open, named, not claimed.
- Conditionality inherited from the landed unraveled-step note: Born weights are used
  only under the declared chain, including
  [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md),
  [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
  [`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md),
  and
  [`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md).
  This note does not upgrade the parent Born assembly's live-ledger status. Named
  instruments with supplied `ε`; supplied `C³` carrier; named hopping; guarded full-rank
  domain. Discrete-time boundary rows untouched; no new axiom, primitive, measure, or
  weight; the `r` dial is untouched. The independent audit lane grades.

## Cross-references

- The four residuals probed:
  [`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- The curvature functional:
  [`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`](INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- The mean-level context:
  [`INTERLEAVED_MEAN_MAP_PERIPHERAL_COUNT_COLLAPSE_ALMOST_PERIODICITY_REMOVAL_BOUNDED_THEOREM_NOTE_2026-06-10.md`](INTERLEAVED_MEAN_MAP_PERIPHERAL_COUNT_COLLAPSE_ALMOST_PERIODICITY_REMOVAL_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- The slaving picture and exact one-body rules:
  [`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  and
  [`SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09.md).
- Standard math (method only): quantum-trajectory trees; singular value decomposition and
  two-sided orbits; class functions; Haar averages as null models; weak measurements.
