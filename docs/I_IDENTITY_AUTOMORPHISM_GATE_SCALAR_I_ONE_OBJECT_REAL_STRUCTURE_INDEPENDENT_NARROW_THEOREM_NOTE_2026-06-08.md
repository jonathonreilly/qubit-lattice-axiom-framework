# The i-Identity Automorphism Gate — Scalar i Is One K-Odd Object, the Real Complex Structure Is K-Even and Independent (Narrow Theorem) Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** narrow structural theorem (complex-structure K-parity classification) + unification gate
**Claim type:** bounded_theorem
**Status:** proposal. A finite, decidable algebraic classification of the framework's complex structures
under the global Record `K`/CPT conjugation, run as the diagnostic gate that licenses or refutes a
single-lever unification of the Tier-A floor before any value computation. Adds no axiom, no fitted value.
Audit verdict set by the independent audit lane.
**Authority role:** diagnostic gate for the r/δ/θ unification program.
**Primary runner:**
[`scripts/i_identity_automorphism_gate_2026_06_08.py`](../scripts/i_identity_automorphism_gate_2026_06_08.py)
(exact numpy, PASS=7).

## The gate

The remaining Tier-A admissions (`r=1/2`, the Koide phase `δ`, `θ_gauge=0`) all live in the conjugate
(phase/CP-odd/orientation) sector the real Record readout drops. A natural unification hope is that a
*single* complex unit `i` underlies all of them, so one structural choice moves them together. This note
tests that hope by classifying every appearance of `i` (and the orientation objects) under the global
Record `K`/CPT conjugation `K(X) = conj(X)` (antilinear, `K(i) = −i`): an object **carries the scalar i**
iff `K` flips its sign (`K(X) = −X`, K-odd); it is a **real structure** iff `K` fixes it (`K(X) = X`,
K-even) — and a real structure can still be a *complex structure* (square to `−1` on a subspace) while
being invisible to `K`.

## Result

**The scalar/algebraic `i` is one object (K-odd).** The Quantum scalar `i·I₂`, the `su(2)` generator
`σ_y`, the Cl(3,0) volume element `ω = σ_xσ_yσ_z` (verified `= i·I₂` exactly), the composition `i` of
`M₂(ℂ)⊗M₂(ℂ)` (verified shared: `(i·I₂)⊗I₂ = I₂⊗(i·I₂) = i·I₄`), and the generation-Yukawa phase `δ`
(`K(M)` sends `δ → −δ`) are **all** flipped by the *single* global `K`. So the CP/phase/reality
sub-sector is internally unified by one conjugation.

**The real complex structure is K-even and independent.** The framework-native generation complex
structure `J_cs = (C − C²)/√3` is a **real** operator with `J_cs² = −(I − P_triv)` (a genuine complex
structure on the doublet) — so `K(J_cs) = J_cs` (K-even); the scalar conjugation cannot flip it. The
generation orientation `sign(Vandermonde)` is likewise a real `Z₂` (S₃ sign rep), K-even.

**Therefore there are (at least) two independent complex structures under `K`** — the K-odd scalar `i`
and the K-even real structure. The naive "one `i` / one lever moves all four" unification is **not
licensed** in its strong form.

| object | complex structure? | K-parity |
|---|---|---|
| Quantum `i·I₂` | yes | **odd** |
| `su(2)` `σ_y` | yes | **odd** |
| Cl(3) volume `ω = iI` | yes (`= i·I₂`) | **odd** |
| composition `i` (#2573) | yes (shared) | **odd** |
| Yukawa phase `δ` | scalar-`i` phase | **odd** (`δ→−δ`) |
| generation `J_cs` | yes (on doublet) | **even** (real) |
| `sign(Vandermonde)` | `Z₂` orientation | **even** (real) |

## What this licenses (and forecloses)

- **Licensed:** pursue `θ`-reality-class + `δ`-phase + the scalar-`i` holomorphic *readability* of `r`
  **jointly** through the single scalar-`i` = Record `K`/CPT conjugation — they are genuinely one object.
- **Licensed separately:** treat the KO-dimension / real structure `J` (the candidate lever that decides
  the `r=1/2`-vs-`1` polarization and the `δ`-sign) as a **distinct single `Z₂`** living in the K-even
  sector (with `J_cs` and the Vandermonde orientation) — to be tested on its own.
- **Foreclosed (the det_C-style error this gate exists to catch):** assuming the scalar `i`
  (composition/phase) and the real-structure polarization are the *same* object. They provably are not —
  `K` flips one and fixes the other. The unification is **two-axis**, not one-`i`; do not run a value
  computation that assumes a single `i` buys all four.

## What is and is not claimed

- **Is:** a finite algebraic classification — the scalar `i` (qubit / `σ_y` / volume element / composition
  / Yukawa phase) is one K-odd object; `J_cs` and the orientation `Z₂` are K-even and independent; hence
  the complex-structure content of the wall is (at least) two-dimensional, and the single-`i` unification
  is not licensed in its strong form.
- **Is not:** does **not** derive `r`, `δ`, or `θ`; does **not** claim the two-axis structure closes any
  admission; does **not** assert the KO-dimension lever succeeds (that is a separate, gated test that
  currently *leans* `r=1`); introduces no axiom or fitted value.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Quantum qubit `M₂(ℂ)=Cl(3,0)`, the
  C₃ generation circulant, and the Record `K`/CPT conjugation; the `ω = i·I₂` identity, the shared
  composition `i`, the `δ→−δ` phase flip, and the K-evenness of `J_cs` / the Vandermonde orientation are
  reproven in the runner.

Companion + context (plain references, not load-bearing deps):
`NO_AXIOM_NATIVE_CP_SOURCE_RDELTA_THETA_UNFORCED_COEFFICIENTS_OF_RECORD_FORCED_ACTION_NO_GO_NOTE_2026-06-08`,
`KOIDE_R_HALF_DYNAMICAL_DIRAC_GATE_CLOSED_FULLY_RESOLVED_ADMISSION_NO_GO_NOTE_2026-06-08`,
`KOIDE_PHASE_DELTA_SPECTRAL_FUNCTIONAL_NO_GO_STATIC_CLOSURE_PARALLEL_TO_R_HALF_NOTE_2026-06-08`.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The `ω = i·I₂` identity, the shared composition `i`, the
`δ → −δ` action of `K` on the circulant, the K-evenness of `J_cs` (real, `J_cs² = −(I−P_triv)`), and the
real Vandermonde orientation are all reproven in the runner from the qubit and the C₃ primitives. No
SM value, selector, or comparator enters.
