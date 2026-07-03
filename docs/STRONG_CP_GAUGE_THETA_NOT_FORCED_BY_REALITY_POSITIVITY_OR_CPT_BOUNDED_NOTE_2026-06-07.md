# Strong-CP: the Gauge Angle θ_gauge=0 Is Not Forced by Reality, Positivity, or CPT (Gauge-Side Obstruction Extending the RP No-Go)

**Date:** 2026-06-07
**Scope:** bounded obstruction note (gauge-side; extends the reflection-positivity no-go; NOT a closure)
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_strong_cp_gauge_theta_not_forced_by_reality_positivity_cpt_exact.py`](../scripts/audit_companion_strong_cp_gauge_theta_not_forced_by_reality_positivity_cpt_exact.py) (sympy/numpy, 6/6)
**Runner cache:** [`logs/runner-cache/audit_companion_strong_cp_gauge_theta_not_forced_by_reality_positivity_cpt_exact.txt`](../logs/runner-cache/audit_companion_strong_cp_gauge_theta_not_forced_by_reality_positivity_cpt_exact.txt)

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
| **reality** of `Z(θ)` | **No** | *assuming* CP-symmetric sector weights `Z_Q = Z_{−Q} > 0`, `Z(θ) = Σ_Q cos(θQ) Z_Q` is real for **all** `θ` (the `sin` terms cancel pairwise). runner (1) |
| **positivity** of `Z(θ)` | **No** | a positive `Z(θ)` **exists** at a representative nonzero `θ` (a toy CP-symmetric sector model) — positivity is compatible with `θ ≠ 0`. runner (2) |
| **CPT** (the Record K/CPT orbit) | **No** | the topological charge `Q` is **CPT-even** (standard parities P-odd × T-odd × C-even = +1), so the K/CPT orbit identifies a configuration with a **same-`Q`** image — it does **not** identify `θ` with `−θ`. runner (4) |

And the decisive structural point: the mass-side `{0, π}` quantization rides on the **K-reality of a
determinant** (a Hermitian operator has a real determinant); `θ_gauge` is a **topological coupling, not a
determinant phase**, so that mechanism **does not transfer**. runner (5).

And **conditionally on the action containing the `F̃F` slot**, `θ_gauge` is genuinely **physical** — the vacuum
energy `F(θ) = −log Z(θ)` depends on `θ` (`F'(0) = 0` marks `θ = 0` as the CP point, but nothing in
reality/positivity/CPT **selects** it), so it is not a removable/gauge label. Whether the framework's action
*has* that slot is precisely the open action-class gate below. runner (3),(3b).

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

## No-Go Discipline (N1-N8)

- **N1 — alternative routes.** (1) **RULED OUT BY PRIOR:** reflection positivity cannot forbid the
  CP-odd imaginary half, per the retained RP no-go. (2) **ATTEMPTED:** reality of `Z(θ)` does not
  select `θ=0`, since CP-paired sectors make `Z(θ)` real for all `θ`. (3) **ATTEMPTED:** positivity
  does not select `θ=0`, since explicit positive nonzero-`θ` sector sums exist. (4) **ATTEMPTED:**
  Record K/CPT does not identify `θ` with `-θ`, since `Q` is CPT-even. (5) **ATTEMPTED:** transfer
  the mass-side determinant-reality mechanism; it fails because `θ_gauge` is a topological coupling,
  not a determinant phase. (6) **OPEN:** derive the gauge action class itself and exclude `F̃F` by
  single-plaquette/minimality; that is the named residual, not closed here.
- **N2 — wall independence.** The measure-side walls are independent: realness, positivity, CPT
  parity, and determinant-reality transfer fail for different reasons, and closing one does not close
  the others.
- **N3 — hidden-wall scan.** The only admitted context is the θ-vacuum sector decomposition/action
  slot. The note makes that conditional explicit; no framework axiom is treated as supplying the
  `F̃F` action class.
- **N4 — residual matching.** The RP citation attacks exactly the CP-odd imaginary half-square
  residual; the mass-orientation citation attacks the determinant phase residual, which is explicitly
  contrasted and not imported to the gauge side.
- **N5 — rhetoric audit.** The phrase "not forced" is scoped to reality, positivity, CPT, RP, and
  determinant-reality transfer. The note does not claim every possible future route to `θ_gauge=0`
  is impossible.
- **N6 — partial-closure scan.** The live partial closure remains single-plaquette/minimality of the
  gauge action. If that action class is derived independently, this no-go becomes a route-pruning
  input rather than an admission.
- **N7 — steelman.** The strongest objection is that a future retained gauge-action derivation might
  force the single-plaquette class and thereby exclude `F̃F`. That is accepted as the open residual;
  it is not supplied by reality, positivity, CPT, or Record.
- **N8 — cross-cycle echo.** This matches prior strong-CP RP and single-plaquette boundary notes: a
  local clean principle prunes one route, while the action-class/minimality question remains separate.

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
