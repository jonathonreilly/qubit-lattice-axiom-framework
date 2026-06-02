# The Natural (Bloch/Hopf/Adjoint) Spinor->Vector Map Quotients the Spinor Z_2: It Does Not Identify the Records-Side and Value-Side Z_2

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note adds no axiom and no import; it answers
an open sub-question negatively for the natural candidate map.
**Primary runner:** [`scripts/frontier_koide_adjoint_map_quotients_spinor_z2.py`](../scripts/frontier_koide_adjoint_map_quotients_spinor_z2.py) (SCORECARD PASS=12)

## Context (the open sub-question)

[`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md)
identifies the generation triplet `C^3` with the grade-1 (vector)
subspace of the qubit's own `Cl(3,0)`, and leaves open (its "Next paths"
section):

> The vector-vs-spinor sign is a concrete sub-question: is there a framework
> operator intertwining the grade-1 `+-1` (`Gamma_chi` adjoint eigenvalue) with a
> spinor `sigma_z` eigenvalue? If so it would discharge the signed-readout sign
> via the same map.

Equivalently (in the session's terminal-gate language): does a reality-respecting
`C^2 (site spinor) -> C^3 (generation vector)` map IDENTIFY the records-side
`Z_2` (the spinor `2 pi = -1` double-cover sign on `C^2`) with the value-side
`Z_2` (the `Gamma_chi` sign partition `+1 | -1, -1` on `C^3`, = the signed-
`sqrt(m)` sign)? If so, the two terminal `Z_2` bits collapse to one and the
carrier discharges. This note answers it for the **natural** candidate -- the
Bloch / Hopf / adjoint map.

## Claim

The natural spinor->vector map is the **adjoint / Bloch / Hopf map**
`q |-> q v q^{-1}` on `Im(H) = R^3` (the `SU(2) -> SO(3)` double cover), where
`H_1 = SU(2)` is the unit quaternions and the spinor `2 pi = -1` sign is the
central element `z = -1`. This map **QUOTIENTS the spinor `Z_2` rather than
transporting it**: its kernel is exactly `{+1, -1}`, so `adjoint(z) = I_3`.
Therefore the records-side spinor `Z_2` and the value-side `Gamma_chi` `Z_2` are
**not the same object** under the adjoint map, and it does not discharge the
signed-readout sign. The only `z`-carrying glue is a non-equivariant, frame-
dependent `spinor-axis <-> [1,1,1]` identification added by hand (an import, not
reality-canonical). **Classification: open import/residual, not a bridge closure.**

### The computation (runner, all 12 checks pass)

- `adjoint(z) = adjoint(-1) = I_3`: the central spinor element maps to the
  identity rotation -- it is in the kernel of `SU(2) -> SO(3)`, quotiented not
  transported.
- `adjoint(q) = adjoint(-q)` for all unit `q` (2-to-1 double cover); the kernel
  is **exactly** `{+1, -1}` = the spinor `Z_2`. So the spinor `Z_2` is precisely
  what the map kills.
- `Gamma_chi` lifts to the pure unit quaternion `q_gc = (0, 1, 1, 1)/sqrt(3)`
  (the `pi`-rotation about `[1,1,1]`): `adjoint(q_gc) = Gamma_chi = 2 v v^T - I`
  (eigenvalues `+1, -1, -1`), and `q_gc^2 = -1 = z`. So `z` appears in `C^2` as
  `q_gc^2`, but `adjoint(q_gc^2) = adjoint(z) = I_3` on `R^3`.
- `z` acts as `-1` on the spin-1/2 (pseudoreal, Frobenius-Schur indicator
  `FS = -1`) module `C^2`, but as `+1` on the spin-1 (real, `FS = +1`) module
  `R^3` where the `Gamma_chi` sign partition lives. Since `z` acts as `(-1)^{2j}`
  on spin-`j`, it is `+1` on every integer-spin (vector) module. So `z` simply
  cannot be the `Gamma_chi` sign on `R^3`.
- The value-side `Z_2` is the `Gamma_chi` adjoint-eigenvalue sign `{+1, -1, -1}`
  on `R^3`, which is **not** `z` (z acts as `+I_3` there). The two `Z_2` are
  distinct objects under the adjoint map.

### Generalization

Any rotation-equivariant candidate map from quaternionic spinor data to `Im(H)` satisfies
`f(q v q^{-1}) = adjoint(q) f(v)`; at `q = z = -1`, `adjoint(z) = I`, so `z` acts
trivially on the image. Every such map factors through `SO(3) = H*/{+-1}` and
**structurally kills `z`**. Carrying `z` nontrivially onto `R^3` therefore
requires a **non-equivariant**, frame-dependent identification of a spinor axis
with `[1,1,1]` -- a posited import, not a reality-canonical structure.

### Consistency with the landed surface

This is exactly the structure of
[`BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md`](BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md)
(`retained_bounded`): `z` is central in `SU(2)` and acts `+1` on every
non-spinorial (integer-spin / vector) representation, so the on-site spinor sign
is decoupled from the rest. The present note is the quaternionic / map-level
statement of the same decoupling, applied to the specific generation-ID bridge
question.

## No-Go Discipline Gate

This gate applies only to the natural rotation-equivariant adjoint/Bloch/Hopf
candidate for unifying the two `Z_2` signs.

- **N1 alternative routes:** (1) adjoint/Bloch/Hopf map `q v q^{-1}`; (2)
  lifting `Gamma_chi` to the quaternion `q_gc`; (3) arbitrary
  rotation-equivariant quaternion-to-vector candidates; (4) left multiplication
  by `z` on the spinor/quaternion; (5) frame-dependent
  `spinor-axis <-> [1,1,1]` glue. Routes (1)-(3) kill `z` on `R^3`; route (4)
  stays spinor-internal; route (5) remains an open import/residual.
- **N2 wall independence:** the adjoint-map no-go and the possible
  frame-dependent glue are distinct. Closing the natural adjoint route does not
  close non-equivariant glues.
- **N3 hidden-wall scan:** "natural" means rotation-equivariant and
  reality-canonical in the SU(2)->SO(3) sense. No non-equivariant frame or
  generation-axis identification is admitted.
- **N4 residual matching:** the parent bridge asked whether the grade-1 vector
  identification can also transport the spinor sign. This note answers only
  that residual for the natural adjoint map; it does not answer the full bridge.
- **N5 rhetoric audit:** "the two `Z_2` are not the same object" means "not
  under the adjoint/Bloch/Hopf map or any rotation-equivariant factor-through
  `SO(3)` map." It does not mean no future non-equivariant bridge can relate
  them.
- **N6 partial-closure scan:** a retained frame-selection theorem, a
  site-to-generation sign bridge, or a binary-octahedral discrete sign carrier
  could still identify the signs by additional structure.
- **N7 steelman:** a later framework-native choice of body diagonal
  `[1,1,1]` and spinor axis could make the non-equivariant glue canonical. That
  would defeat the broader bridge residual while preserving the adjoint-map
  quotient result.
- **N8 cross-cycle echo:** the retained binary-octahedral note already
  decouples the central spinor sign from integer-spin/vector reps. This note is
  the map-level version for the Koide generation bridge, not a new axiom or a
  full bridge no-go.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| [`binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28`](BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md) | retained_bounded |
| [`internal_external_su2_merger_from_universal_property_narrow_theorem_note_2026-05-27`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md) | retained_bounded |
| [`per_site_su2_spin_half_theorem_note_2026-05-02`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md) | retained |
| [`parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23`](PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_NARROW_THEOREM_NOTE_2026-05-23.md) | retained_bounded |
| [`koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) | retained_bounded |
| [`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md) | audited_failed (referenced only as the sign a bridge would discharge; not load-bearing) |

The parent note
[`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md)
is on origin/main; its ledger row is freshly merged. This note is its
companion, answering its open vector-vs-spinor-sign sub-question for the natural
candidate.

## Non-circularity

The quaternion algebra, the adjoint rotation, the kernel, and the `Gamma_chi`
lift are direct computations; `Q = 2/3` and the bridge are never assumed. The
conclusion (the two `Z_2` are distinct under the adjoint map) is computed, not
posited.

## Next paths this opens

- This is **not** a closure of the bridge. The adjoint/Bloch/Hopf map is one
  (the natural, rotation-equivariant) candidate; it quotients `z`. The remaining
  routes are non-equivariant: a **left-multiplication** action of `z` on `H`
  (`q |-> z q = -q`) is nontrivial but stays **`C^2`-internal** (it does not
  descend to `R^3` / the generation vector at all), and a frame-dependent
  `spinor-axis <-> [1,1,1]` glue would carry `z` onto `R^3` only by hand.
- Whether any of those non-equivariant glues is forced by a further framework
  structure (rather than posited) is the live question; on the rotation-
  equivariant / reality-canonical surface, the natural map does not transport the
  sign.
