# Strong-CP: the Gauge Angle θ_gauge=0 Is Not Forced by Reality, Positivity, or CPT (Gauge-Side Obstruction Extending the RP No-Go)

**Date:** 2026-06-07
**Type:** bounded obstruction note (gauge-side; extends the reflection-positivity no-go; NOT a closure)
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_strong_cp_gauge_theta_not_forced_by_reality_positivity_cpt_exact.py`](../scripts/audit_companion_strong_cp_gauge_theta_not_forced_by_reality_positivity_cpt_exact.py) (sympy/numpy, 6/6)

## Result

The total strong-CP angle splits as `θ̄ = θ_gauge + arg det(M_q)`
([`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](./STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)). The **mass side**
(`arg det M_q ∈ {0, π}`, oriented to `0` on the selected surface) is constrained because the K/CPT-real
(Hermitian) generation mass circulant `M = aI + bC + b̄C²` has a **real determinant**
([`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](./STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)). This note
records that the **gauge side** `θ_gauge` (the `F̃F` / topological coupling, weighting topological sectors by
`e^{iθQ}` in `Z(θ) = Σ_Q e^{iθQ} Z_Q`) is **not** closed by the analogous clean routes:

| route | does it force `θ_gauge = 0`? | why |
|---|---|---|
| reflection positivity | **No** (documented no-go) | `F̃F` is Θ-anti-invariant → the phase cancels in every reflection-Hermitian observable; RP cannot detect it ([`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](./STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)) |
| **reality** of `Z(θ)` | **No** | with CP-symmetric sector weights `Z_Q = Z_{−Q} > 0`, `Z(θ) = Σ_Q cos(θQ) Z_Q` is real for **all** `θ` (the `sin` terms cancel pairwise). runner (1) |
| **positivity** of `Z(θ)` | **No** | `Z(θ) > 0` for nonzero `θ` (`Z_0` dominates). runner (2) |
| **CPT** (the Record K/CPT orbit) | **No** | the topological charge `Q` is **CPT-even** (P-odd × T-odd = +1), so the K/CPT orbit identifies a configuration with a **same-`Q`** image — it does **not** identify `θ` with `−θ`. runner (4) |

And the decisive structural point: the mass-side `{0, π}` quantization rides on the **K-reality of a
determinant** (a Hermitian operator has a real determinant); `θ_gauge` is a **topological coupling, not a
determinant phase**, so that mechanism **does not transfer**. runner (5).

`θ_gauge` is also genuinely **physical** — the vacuum energy `F(θ) = −log Z(θ)` depends on `θ` (`F'(0) = 0`
marks `θ = 0` as the CP point, but nothing in reality/positivity/CPT **selects** it), so `θ_gauge` is not a
removable/gauge label. runner (3),(3b).

## What this means

`θ_gauge = 0` is **not forced** by any local reality/positivity/CPT property of the framework measure. The
mass side reaches `{0, π}` because it is a determinant phase under K-reality; the gauge side has no such handle.
What remains is the **action-class** question — whether the framework's gauge action contains the `F̃F`
operator at all. The single-plaquette action class **excludes** it
([`NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md`](./NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md), `O(a^6)`, no leading `F̃F`), but
**multi-plaquette** operators are the named open boundary, and the framework's gauge action is itself not
derived (the plaquette/coupling are inputs). So `θ_gauge` stays a genuine admission, gated on the
**un-derived gauge action-class**.

This is the gauge-side analogue of the matter-side situation for the charged-lepton Koide value
(`r = |b|²/a²`), which is likewise an admission gated on the un-derived staggered realization. In both cases
the *kinematic* axioms `{Lattice, Quantum, Record}` fix the **structure** but not the value, because the value
rides on a **dynamics** (the gauge action here; the matter realization there) the axioms do not supply.

## Scope — what this is and is not

- **Is:** a verified obstruction — three clean routes (reality, positivity, CPT) shown **not** to force
  `θ_gauge = 0`, extending the existing reflection-positivity no-go, with the determinant-reality mechanism of
  the mass side shown **not** to transfer to the gauge side.
- **Is not:** a claim that `θ_gauge ≠ 0`, or that `θ̄ ≠ 0` (the framework's `θ = 0` note is a bounded
  selected-surface result and is unaffected); a new axiom, primitive, or admission; a closure of the strong-CP
  problem; a statement that no future route can derive `θ_gauge = 0` (the multi-plaquette action-class boundary
  remains open).
- **Open residual:** does the framework's (un-derived) gauge action-class contain the `F̃F` operator? — the
  single-plaquette-vs-multi-plaquette boundary.

## Forbidden-import / reprove-and-cite discipline

- The reality and positivity of `Z(θ)`, the CPT-evenness of `Q`, and the K-reality (real determinant) of the
  mass circulant are **reproven** from the θ-vacuum sum and the C₃ primitive in the runner (sympy/numpy, 6/6).
- The reflection-positivity no-go, the θ-vacuum structure `Z(θ) = Σ_Q e^{iθQ} Z_Q`, and the CPT transformation
  of the topological charge are **comparators** only — named for provenance and cross-check, never derivation
  inputs.
- No PDG values appear; `θ = 0` is the empirical target, not derived here.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](./STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)
- [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](./STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
- [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](./STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
- [`NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md`](./NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md)
- [`STRONG_CP_THETA_ZERO_NOTE.md`](./STRONG_CP_THETA_ZERO_NOTE.md)

**Independent audit required.** This note asserts no effective-status change.
