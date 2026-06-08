# No Axiom-Native CP Source — r, δ, θ Are Unforced Coefficients of the Record-Forced Action (No-Go) Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** named-obstruction no-go + backward synthesis of established admissions
**Claim type:** no_go
**Status:** no-go proposal. Establishes that `{Lattice, Quantum, Record}` supply
**no** source of a CP-odd term in the action, and records (backward, from the
already-landed per-item results) that the three remaining Tier-A admissions —
`r = 1/2`, `δ`, and `θ_gauge` — are exactly three **unforced coefficients** of
the one Record-forced gauge-invariant-local action form-class. Adds no axiom, no
fitted/imported value. Audit verdict set by the independent audit lane.
**Authority role:** no-go source proposal (the shared CP-odd-coefficient residual).
**Primary runner:**
[`scripts/shared_cp_odd_action_class_no_axiom_native_source_2026_06_08.py`](../scripts/shared_cp_odd_action_class_no_axiom_native_source_2026_06_08.py)
(exact numpy/sympy, PASS=4).

## The shared residual

Three Tier-A admissions each need a CP-odd / chirality-dependent **coefficient**
in the action that the kinematic axioms do not supply: `r = |b|²/a²` (the
doublet:singlet generation-Yukawa magnitude), `δ` (the CP-odd generation-Yukawa
phase, which sets the charged-lepton mass values), and `θ_gauge` (the coefficient
of the `F̃F` topological term). `DYNAMICS_FORM_FROM_RECORD_PRESERVATION` (retained)
forces the action **form-class** (gauge-invariant-local Wilson — the observable
algebra is the commutant of the per-vertex Gauss generators, plus a conserved
pointer and local transfer) but fixes only the **basis** of admissible terms, not
the **coefficients**. This note asks the head-on question: is there an
axiom-native source for the CP-odd coefficients — which would unlock all three at
once?

## Result: no axiom-native CP source

A candidate route and seven alternatives were attacked and independently verified;
**none** sources an axiom-native CP-odd action term.

- **The arrow is a boundary condition, not a dynamical T-violation (candidate
  route refuted).** The natural hope — *Record is irreversible = the arrow =
  T-violation; by CPT, T-violation ⟺ CP-violation, so the arrow sources CP* —
  fails at the root. The record-write microdynamics is **time-symmetric**: the
  generator (e.g. `H = (π/2)|1⟩⟨1|⊗X`) is real-symmetric, so `Θ U Θ⁻¹ = U⁻¹`
  (`Θ = K`) and `T = e^{−H}` is self-adjoint with `T = Tᵀ`. The **same** generator
  produces a forward (record-increasing) or reversed (record-decreasing) arrow
  purely from the initial state, so the arrow lives in the Past-Hypothesis
  boundary, not in the map. A boundary arrow carries **zero** CP-odd dynamical
  content; coarse-graining a T-even broadcast unitary gives a detailed-balance
  channel (zero steady-state current), so there is no dynamical T-violation for
  CPT to convert.
- **CPT protects CP, it does not source it.** `Θ_CPT M Θ_CPT⁻¹ = M*` forces
  `det M ∈ ℝ` (C₃ circulant `det = a³ − 3a|b|² + 2|b|³ cos3δ`, `Im = 0`; staggered
  `M` real) → the matter CP-odd phase is quantized to `{0, π}`. CPT pushes *toward*
  CP-conservation. A CPT *anomaly* would produce CPT-**odd** output, orthogonal to
  the CPT-**even** `θ`/`δ` targets — and none exists (the Haar measure is real and
  bi-invariant; `Re Tr U_P` is even under `U → U*`).
- **The only axiom-native orientation object is one sign-only Z₂.** The Cl(3)
  volume element `ω = σ₁σ₂σ₃ = i·I`, the `Z³` lattice orientation `det R = ±1`,
  `sign(Vandermonde)`, and complex-conjugation-as-an-outer-`O(3)`-reflection are
  the **same** single bit (derived four ways). It can flip a sign
  (`θ → det(R)·θ`, `δ → −δ`) but cannot continuously source any coefficient; it is
  scalar on the rank-2 sector and blind to coupling type.
- **No falsification — Record does not forbid CP.** The real additive-log readout
  is CP-blind (reads `log|·|`, even in `δ`), but blindness is a **consumer**
  property, not a prohibition: the CP-odd Jarlskog scalar
  `J = Im(M₀₁ M₁₂ M₂₀) = |b|³ sin3δ` is itself a perfectly real scalar, and the
  spectrum realizes the full Koide pattern for any `δ`. So `δ ≠ 0` is physical and
  consistent with the real readout; "real readout ⇒ CP-even ⇒ `δ` unphysical" is a
  category error.

## What is forced, and the one partial result

- **Forced (the form-class):** Record-preservation + Gauss invariance + locality +
  Hermiticity force the gauge-invariant-local Wilson form-class
  (`DYNAMICS_FORM_FROM_RECORD_PRESERVATION`); and `M(δ, r)` is Hermitian and
  C₃-covariant for **all** `(δ, r)`, while `Re Tr U_P` and the CP-odd `Im Tr U_P`
  are gauge-invariant for **any** `θ` — so `(r, δ, θ)` are free.
- **Partial result (conditional, not forced):** the single-plaquette class is
  `F̃F`-free at leading order (the CP-odd single-plaquette operator is `O(a⁶)`
  cubic single-plane `Tr F³`, while `F̃F` is `O(a⁴)` bilinear multi-plane; for
  `su(2)`, `Tr F³ ≡ 0`). So **if** minimality held, `θ_gauge = 0` would follow.
  But the Lattice axiom supplies finite-range, **not** minimal-range, locality, and
  the clover (range-2) `F̃F` is gauge-invariant, local, real-density, RP-compatible
  and CPT-even — equally admissible. `θ_gauge = 0` is therefore **gated** on an
  un-derived minimality admission, not forced
  (`STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE`).

## The unification (backward synthesis)

The three remaining Tier-A admissions collapse to **one** irreducible residual:
the Record-forced action form-class leaves its CP-odd/magnitude **coefficients**
unconstrained, and the axioms supply no object that pins any of them. `r = 1/2`,
`δ`, and `θ_gauge` are three unforced coefficients of the **one** forced
form-class, sharing one obstruction — there is no axiom-native CP-source (the arrow
is a boundary, CPT protects CP, the orientation is one sign-only bit, Record's
negative list disclaims couplings). This is the same un-derived-couplings wall as
the `β = 6` plaquette: no known approach derives the action coefficients; they are
always an input.

## What is and is not claimed

- **Is:** no axiom-native source of a CP-odd action term exists (arrow = boundary
  not dynamical T-violation; CPT = CP-protecting; orientation = one sign-only Z₂;
  Record real-readout CP-blindness is a consumer property); the three admissions
  are unforced coefficients of one forced form-class; `θ_gauge = 0` is conditional
  on an un-derived minimality admission; there is **no** falsification (`δ ≠ 0` is
  physical, consistent with the real readout).
- **Is not:** does **not** derive `r`, `δ`, or `θ`; does **not** solve strong-CP;
  does **not** prove the coefficients can never be derived in a richer theory (the
  residual is the un-derived-couplings research target, the `β = 6` wall); does
  **not** introduce a new axiom, tag, or class. The per-item obstructions are
  already landed; the new runner-backed content is the arrow→CP-odd refutation and
  the single-place verification of the shared obstruction.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the three axioms
  and Record's negative list (no couplings, weighting, arrow, measurement
  dynamics); the time-symmetry of the record-write generator, `det M ∈ ℝ` under
  CPT, the orientation Z₂, and the coefficient-freedom of `(r, δ, θ)` are reproven
  in the runner.

Companion + context (plain references, not load-bearing deps):
`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05`,
`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`,
`AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29`,
`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07`,
`STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07`,
`KOIDE_R_HALF_DYNAMICAL_DIRAC_GATE_CLOSED_FULLY_RESOLVED_ADMISSION_NO_GO_NOTE_2026-06-08`,
`KOIDE_PHASE_DELTA_SPECTRAL_FUNCTIONAL_NO_GO_STATIC_CLOSURE_PARALLEL_TO_R_HALF_NOTE_2026-06-08`,
`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`.

## Forbidden-imports check

No PDG / fitted / literature numerical comparator is consumed. The time-symmetry
of the record-write generator, the CPT identity `det M ∈ ℝ`, the orientation Z₂,
the CP-odd Jarlskog scalar `J = |b|³ sin3δ`, the single-plaquette `Tr F³` order
counting, and the coefficient-freedom of `(r, δ, θ)` are reproven in the runner
from the three axioms. `θ = 0`, `δ ≈ 2/9`, and `r = 1/2` are named as
comparator/target only, never as ingredients.
