# Scale-ladder probe: Record apparatus and readout weights

Provenance: a fresh-context agent of the same model family; not an independent
reviewer. No docs were edited.

## Record apparatus

- **A2, mediated-output fine-tuning. Productive reframe.**
  - Probe A-1 used a toy emitter–chain–receiver with N=10. It is generic, not the campaign device.
  - The region-rung effective theory is a two-level system:
    - λ_eff = λ²|G_1N(0)|;
    - Δ_eff = (d_e − d_r) + λ²(G_11 − G_NN).
  - Tolerances below are the error that adds 1e-2 worst-case infidelity, for λ ≤ 0.02:

    | Perturbation | Tolerance | Scaling with λ |
    |---|---|---|
    | Relative bond error, fixed read time | 1.1–1.5e-2 | flat |
    | Relative bond error, best read time | ≈0.10–0.14 | flat |
    | Chain onsite error | 3.4–4.1e-2 | flat |
    | Common endpoint detuning | 5–6e-2 | flat |
    | Differential endpoint detuning | ≈0.115·λ_eff | λ^2.01, the only relevant parameter |

  - The campaign's 1e-13 bond bound is about 1/M, with M the receiver length. The cause would be the "complete output with literal phase" target, not transfer itself.
  - Hypothesis: the fine-tuning is a hidden phase-reference (clock) obligation.
- **A1, autonomous occurrence. Reframe.** The λ→0, T~1/λ² devices sit in the van Hove regime.
  - γ = 2πλ²ρ(E) would be derived rather than supplied.
  - The GKSL time would become the coarse time τ = λ²t.
  - What this needs is a quantitative finite-patch Davies theorem. Finite M gives recurrences.
- **A4, permanent halt. No help.** Finite closed systems are quasi-periodic.
- **A3, preparation. No help, with a sharpened obstruction.** Unital channels cannot raise purity, so preparation means supplying a non-unital, low-entropy resource.

## Readout weights

- **B1/B2, menu abundance and regularity. Reframe, not resolve.** Gleason on a C⁴ block, plus rung-consistency.
  - Product frames: unknown frame-function dimension 195 against 15 for Born. The site marginal is a free odd function, 13 dimensions against 3.
  - Adding entangling images raises the excess to 838.
  - Clifford-closed frames (940 states, 4225 bases): 205 against 15. The site marginal is 6 against 3.
  - So a finite apparatus set is insufficient. Non-contextuality across apparatus unitaries is Gleason's assumption renamed.
- **B3, normalization on Record contents. Reframe.** Commuting with outcome merging is Busch-type additivity, equivalent to the missing clause.
- **B4, fair-coin weight class. No help.**
- **B5, frequency consistency. Candidate resolution, conditional.** For the order-blind positive formation class:
  - the field is translation-covariant and 1-dependent;
  - 1-dependence gives mixing, and mixing gives ergodicity;
  - the multidimensional ergodic theorem then gives conditional frequencies.

  This must still be checked against the "stationarity insufficient" note.

## Proposed probes, not run

- **A-2.** Phase versus probability metric on the campaign device.
- **A-3.** A van Hove fit of γ_eff against λ².
- **B-3.** Exact sampling of a 1-dependent field to check frequency convergence.
