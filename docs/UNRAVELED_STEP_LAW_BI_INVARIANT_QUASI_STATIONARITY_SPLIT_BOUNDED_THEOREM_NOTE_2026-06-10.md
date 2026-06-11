# The Bi-Invariant Quasi-Stationarity Split of the Unraveled Step Law: the Stationarity Failure Localizes to the Bi-Frame (Measured), the Moment Spectra Are Quasi-Frozen

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode; depth-scan strike on #3507's residuals 1+2; panel-narrowed)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_unraveled_step_law_bi_invariant_quasi_stationarity_split_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_unraveled_step_law_bi_invariant_quasi_stationarity_split_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=21 FAIL=0` — exact,
deterministic, no MC (outcome tree enumerated to depth 11; every Born weight exact; two
parameter instances; a 5-seed robustness scan; #3507's panel-hardened guards inherited).
A mandatory 4-lens adversarial panel returned `land_with_edits`; **all eleven required
edits are applied.** The genuinely new increment over #3507 is the **depth-5→11 scan**
plus the **moment-spectrum read-out**; the qualitative non-centrality and the curvature
functional are #3507/#3491 content, attributed up front.

## What is probed, and the honest first answer

#3507 left four named residuals on the CLT route; this note probes **residual 1
(stationarity)** and **residual 2 (structural centrality)** with an exact depth-scan of
the Born-weighted step-law ensemble. **(S1)** The link-level step mean `E[dU](n)` moves
**O(1) at every depth step** (per-step motion ≥ 0.6 at instance A, ≥ 1.3 at B): no Cauchy
decay, no equilibration onset at this system size and horizon.

## The split (per-depth moment spectra — with the inference done honestly)

**(S2)** The **singular-value spectrum of `E[dU](n)` is quasi-frozen** (10–100× below the
raw motion at instance A; ~10× at B, where the smallest singular value is least frozen)
while the **eigenvalue spectrum moves at the raw scale**. Frozen singular values with
moving eigenvalues **do not by themselves deduce** a bi-frame (a conjugation with rotated
phases also produces that pattern — panel counterexample); the bi-frame reading is
therefore **measured directly**: the two-sided factors `V, W` of consecutive means differ
at order 1 (median `|V−W|` comparable to `|V−I|`, both instances, in-runner). And the
**second-moment tensor's spectrum quasi-freezes as well** (panel-verified strengthening —
the split is not a first-moment accident). **Scope, precisely:** what is quasi-stationary
is the **bi-orbit-projected spectrum of the step *mean*** (and the exhibited second
moment) — *not* the whole step law; the bi-orbit-quotient **law** remains the named open
object. The stationarity failure is concentrated in the **bi-frame** — the edge's
independent left/right gauge directions — at this size and horizon.

**(S3) The invariant marginal, seed-disclosed.** The gauge-invariant curvature marginal
`E[C]` (the #3491 functional) sits in a narrow band at the published seeds (11–17%
relative) — **and the published instance-A seed is the tightest of a 5-seed scan whose
bands reach ~33%**; the runner's gates are set to the scan (max < 35%, median < 20%), so
the pinning is **typical, with seed-dependent magnitude**, not a regime constant. The
boundedness control (an equally bounded gauge-*variant* scalar) wanders wider — **5.1× at
A, 1.8× at B**, scan ratios median ≥ 1.5 with min ≥ 0.9 — typical teeth, honestly gated.

**(S4) Residual 2 across depth, null-controlled.** The singular spectrum is
**nonzero-stable** across the whole horizon — a bi-invariant law has *zero* mean, so this
quantifies #3507's structural non-centrality across depth (no decay; consistent with the
`ε`-independence finding). A matched **Haar-average null** shows the sv-freeze has
**teeth at instance A** (real motion slower than the null) but is **not distinguished
from the null at instance B** — "quasi-frozen" at B is scoped accordingly.

## What this relocates, and what it does not deliver

- **Relocation, not delivery:** residual 1 stands, but its failure **localizes to the
  bi-frame** (measured, not just inferred) at this size and horizon; residual 2 stands,
  **quantified across depth**. No CLT premise is delivered; all four #3507 residuals
  stand.
- **Honest grade:** finite horizon (depth 11), small system (3-ring), two instances plus
  a 5-seed scan, **seeds disclosed as load-bearing** — not an invariant-measure theorem,
  not a proof of asymptotic stationarity. All bands, ratios, and spectra are
  seed/instance-labeled numbers.
- **The path this opens:** the step law **modulo the bi-frame** — whether a group-level
  step measure can be built on the bi-orbit quotient, and what residual 3's
  edge-anchoring looks like there — open, named, not claimed.
- Conditionality inherited from #3507: the Born derived-chain cap — retained
  `gleason_on_qubit_lattice_projection_lattice_narrow_theorem_note_2026-05-20`; the
  Busch/POVM qubit-authority bridge note cited there
  (`busch_povm_effect_gleason_qubit_authority_bridge_narrow_theorem_note_2026-06-05`)
  **has no row on the live ledger** (status: the audit lane's to assign; a
  differently-named Busch-extension note is retained, not silently substituted); the
  assembly note `born_rule_from_gleason_busch_derivation_note_2026-05-20` is
  **audited_conditional** on the live ledger (audit 2026-05-30). Named instruments with
  supplied `ε`; supplied `C³` carrier; named hopping; guarded full-rank domain.
  Discrete-time throughout (retained R1 boundaries untouched); no new axiom, primitive,
  measure, or weight; `r` untouched. The audit lane grades.

## Cross-references

- The four residuals probed: PR #3507 — **science landed on origin/main via cherry-pick;
  PR closed-not-merged.** The curvature functional: PR #3491 — same status. The
  mean-level context: PR #3499 — same status.
- The slaving picture and exact one-body rules: campaign blocks 01–02 (PRs #3418/#3425,
  on main).
- Standard math (method only): quantum-trajectory trees; singular value decomposition and
  two-sided orbits; class functions; Haar averages as null models; weak measurements.
