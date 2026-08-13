---
claim_id: m3_corner_in_m4_is_not_unital_color_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The corner pad ι : M_3(C) → M_4(C), ι(X)=diag(X,0), is an injective *-homomorphism of C-algebras that is not unital. Its image of I_3 is the rank-3 projection P=diag(1,1,1,0), not I_4. A two-site qubit composite whose algebra is M_2(C)⊗M_2(C) ≅ M_4(C) therefore does not carry M_3(C) as its unit algebra by this pad. The result does not install SU(3), does not name QCD, and does not adopt a color axiom."
upstream_dependencies:
  - minimal_axioms
runner: scripts/m3_corner_in_m4_is_not_unital_color_hypothetical_2026_08_13.py
---

# M_3 Corner in M_4 Is Not a Unital Color Algebra

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact two-site tensor algebra `T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)`
and the corner pad `ι : M_3(C) → M_4(C)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/m3_corner_in_m4_is_not_unital_color_hypothetical_2026_08_13.py`](../scripts/m3_corner_in_m4_is_not_unital_color_hypothetical_2026_08_13.py)

## Result Up Front

The Qubit axiom supplies one site with possibility algebra `M_2(C)`. The
two-site tensor composite is `T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)`. Padding
`M_3(C)` into the top-left corner of `M_4(C)` is an injective multiplicative
*-map, but it sends `I_3` to a rank-3 projection, not to `I_4`. The padded
copy is a corner, not the unit algebra of the two-site composite.

This is a type mismatch for the cheap pad. It is not a derivation of color,
not an installation of `SU(3)`, and not a Qubit rewrite.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The corner pad is proved to be an injective non-unital *-homomorphism M_3(C) → M_4(C) on explicit matrix units; unital color-algebra identification, SU(3), QCD, and axiom adoption remain outside the claim."
trace_class: negative_route_pruning
target_claim_id: two_site_tensor_composite_unit_algebra_is_not_m3_by_corner_pad
target_blocker_text: "does the two-site qubit composite carry M_3 as its unit algebra via the corner pad?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed pad ι(X)=diag(X,0) on T_2 ≅ M_4(C); other embeddings and other composite types remain separate"
hypothetical_axiom_status: "C2 tensor composite leftover: non-unital corner is not the color algebra; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The current Qubit axiom names the full one-site possibility domain with
algebraic presentation `M_2(C)`. Write

`T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)`

for the two-site tensor composite. Complex dimensions are

`dim_C(M_2(C)) = 4`, `dim_C(T_2) = 16 = dim_C(M_4(C))`, `dim_C(M_3(C)) = 9`.

Let `{E_{ij}}_{1 ≤ i,j ≤ 3}` be the standard matrix units of `M_3(C)`, and
let `I_3` (resp. `I_4`) be the unit of `M_3(C)` (resp. `M_4(C)`). Define the
corner pad

`ι : M_3(C) → M_4(C)`, `ι(X) = diag(X, 0)`

as a 4×4 block: the top-left 3×3 block is `X` and the last row and column are
zero. Equivalently, if `X = (X_{ab})_{1≤a,b≤3}`, then

`ι(X)_{ab} = X_{ab}` for `1 ≤ a,b ≤ 3`, and `ι(X)_{a4} = ι(X)_{4b} = 0`.

Write `P = ι(I_3) = diag(1,1,1,0)`.

No axiom is edited. The map `ι` is a displayed mathematical test object, not
a proposed Qubit rewrite and not a registered primitive.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the corner pad installs `M_3(C)` as the unit
algebra of the two-site qubit composite `T_2 ≅ M_4(C)`.

| Obligation | Role | Disposition |
|---|---|---|
| exhibit `ι` on matrix units and on `I_3` | object | proved; runner checks `E_{12}` and `I_3` |
| `ι` C-linear, *-preserving, multiplicative, injective | Theorem 1 | proved on the displayed pad |
| `ι(I_3) = I_4` | unitality | fails; `ι(I_3) = P ≠ I_4` |
| `rank(ι(I_3)) = rank(I_4)` | full-support unit | fails; ranks `3 ≠ 4` |
| install `SU(3)`, name QCD, adopt a color axiom | out of scope | not claimed |

## Theorem 1 — The pad is an injective *-homomorphism

`ι` is injective and C-linear. It preserves the involution and the product:

`ι(X*) = ι(X)*`, `ι(XY) = ι(X)ι(Y)`.

On the matrix unit `E_{12}` the image is the corresponding 4×4 matrix unit
with a 1 in position `(1,2)` and zeros elsewhere, including the last row and
column. On the unit,

`ι(I_3) = P = diag(1,1,1,0)`,

which is not `I_4`.

Proof. Linearity is the entrywise definition. If `ι(X) = 0`, every entry of
`X` is a top-left entry of the zero 4×4 matrix, so `X = 0`. The adjoint of
`diag(X, 0)` is `diag(X*, 0)`. The product of two top-left pads is the pad of
the product, because the extra row and column are zero. Direct inspection
gives `ι(E_{12})` and `ι(I_3)` as stated.

## Theorem 2 — The pad is not unital

`ι` is **not unital**: `ι(I_3) ≠ I_4`. Therefore `ι` is not a unital
*-homomorphism. A two-site qubit composite whose algebra is `M_4(C)` does
not carry `M_3(C)` as its unit algebra by this pad.

The unit of `T_2` is `I_2 ⊗ I_2 = I_4`. The padded copy of `I_3` is the
proper projection `P`. A unital algebra homomorphism must send units to
units, so this pad cannot be the identification “color is the two-site
composite.”

## Theorem 3 — The padded copy is a corner

`rank(ι(I_3)) = 3 ≠ 4 = rank(I_4)`. The image of the pad is the corner
algebra `P M_4(C) P ≅ M_3(C)`, not the full two-site possibility algebra.

`P` is a projection: `P^2 = P = P*`. Its range is a 3-dimensional coordinate
subspace of `C^4`. The complementary rank-1 projection `I_4 - P` is nonzero,
so the pad never uses the full two-site unit.

## Theorem 4 — No color axiom is installed

This does not install `SU(3)`, does not name QCD, and does not adopt a color
axiom. It only shows the cheap pad is the wrong type for “color is a
composite of qubits.”

The four axioms do not name a three-dimensional internal algebra. The
approved primitives (scale reference, kinetic isotropy, realized state) do
not supply one. Rejecting this pad does not create that algebra, and it does
not rewrite Qubit.

## Mutation

The predicate `ι(I_3) == I_4` must fail.
The predicate `rank(ι(I_3)) == 4` must fail.

Both failures are runner-checked by constructing `ι(I_3)` from `I_3` and
computing the exact rational rank.

## No-Go Discipline Gate

The negative claim is only that this displayed corner pad is not a unital
*-homomorphism and is not the two-site unit algebra. The gate does not
certify that color is underivable, that every embedding of `M_3(C)` fails,
or that a composite of qubits cannot carry further structure by another
construction.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Top-left corner pad `ι(X)=diag(X,0)` | test unital *-homomorphism into `T_2 ≅ M_4(C)` | Theorems 1–3: injective *-hom, not unital, rank 3 | **ATTEMPTED** |
| Opposite corner `diag(0,X)` | same unitality test | image of `I_3` is `diag(0,1,1,1)`, still a rank-3 projection | **ATTEMPTED** |
| Any unital *-hom `M_3(C) → M_4(C)` | require `k | m` for unital maps `M_k → M_m` | `3` does not divide `4`; independent of the pad calculation and not adopted here as a color theorem | **ATTEMPTED** |
| Identify a 3-plane in `C^4` with a color carrier | representation, not an algebra unit | supplies a module, not `ι(I_3)=I_4` | **ATTEMPTED** |
| Quotient `M_4(C)` onto `M_3(C)` | unital quotient of a simple algebra | `M_4(C)` is simple, so the only unital quotient is itself | **ATTEMPTED** |
| Extra neighboring sites or a different composite type | larger tensor or non-tensor composite | outside `T_2`; live and not tested as a no-go | live |
| Owner-approved primitive or retained derivation of a color algebra | governance, not this pad | not supplied by the current axioms or approved primitives | live |

The first five routes concern the cheap pad and close cousins inside `M_4(C)`.
The last two remain possible. Accordingly, the broad statement “color cannot
be a composite of qubits” is not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| non-unitality of `ι` / rank gap `3 ≠ 4` | almost: `P ≠ I_4` already implies unequal rank once ranks are computed | almost: rank mismatch implies `P ≠ I_4` | two readings of the same projection, not two independent walls |
| pad failure / unital-divisibility obstruction | no: a non-unital injective map can exist when no unital map exists | no: absence of a unital map does not compute `ι(I_3)` | independent holes |
| pad failure / SU(3) installation | no: rejecting a pad does not produce a Lie algebra | no: an `su(3)` basis would not make `ι` unital | independent |
| pad failure / QCD naming | no | no | independent; QCD is never used |
| pad failure / Qubit rewrite | no: the current one-site wording is untouched | no: a rewrite would be a different object | independent |

The load-bearing wall of this note is a single type mismatch: the pad is not
unital. Rank is the same projection, restated. Unital divisibility, `SU(3)`,
and QCD are not additional walls of this claim.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `T_2 = M_2 ⊗ M_2 ≅ M_4(C)` | standard finite-dimensional identification; dimension 16 is runner-checked |
| `ι(X)=diag(X,0)` | explicit test map, not attributed to the axioms |
| matrix units `E_{ij}` | standard basis of `M_3(C)` |
| `*` | conjugate transpose on finite matrices |
| rank | exact rational row rank |
| “unit algebra” | the unital algebra whose unit is the unit of `T_2` |
| “color algebra” | rejected identification only; not a derived object |
| `SU(3)`, QCD | named only to refuse installation and naming |
| observations or fitted constants | none |

No continuum limit, gauge connection, representation theory of `SU(3)`, or
empirical color quantum number is used.

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one-site possibility domain `M_2(C)`; further structure requires a retained derivation, bridge, or approved primitive | wording only; no composite or color conclusion is borrowed |

The pad identities, unitality failure, and rank computation are proved here
and checked by the runner. No other scientific parent is used.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | matrix units of `M_3(C)` and the two units `I_3`, `I_4` | no classification of every map `M_3 → M_4` as the main theorem |
| per site | two-site tensor `T_2` only | no lattice-wide color field |
| per mode | the single pad `ι` and the opposite corner | no spectral exhaustion |
| per block | unit-algebra identification via the cheap pad | no QCD, no `SU(3)`, no axiom edit |
| lattice-wide | not executed | no lattice-wide no-go |

### N6 — live partial-closure paths

1. A different composite type (not a finite tensor of one-site possibility
   algebras) could still be proposed; this note does not classify composites.
2. A unital embedding into some other algebra is a separate question; for
   `M_4(C)` it is independently obstructed by `3 ∤ 4`, but that obstruction
   is not adopted here as a color theorem.
3. A derived internal algebra could appear from Record/Admissibility
   structure rather than from padding `M_3(C)` by hand.
4. An owner-approved primitive could register a three-dimensional internal
   algebra; none of the current approved primitives does so.
5. A Qubit rewrite that changes the one-site algebra is a governance act,
   not a consequence of this pad, and is not adopted.

Scale reference, kinetic isotropy, and realized state were checked in the
premise registry. None supplies a color algebra, and none is counted as an
extra wall.

### N7 — concrete-mechanism steelman

The strongest steelman of the pad is: treat `P M_4(C) P` as “the color
block” of a two-site composite and ignore the complementary line. That still
fails as a unital identification with the two-site possibility algebra,
because the two-site unit remains `I_4` and `P ≠ I_4`. Calling the corner
“color” is a name, not a unital algebra homomorphism, and it is not adopted.

### N8 — cross-cycle echo

Historical color-selection and Hurwitz-clause notes reject other cheap
identifications. This note does not reuse those conclusions. It recomputes
only the corner pad on `T_2` and refuses to import QCD.

## FAIL / DO NOT SHIP

Do not ship any of the following from this note:

- “the axioms cannot derive color”
- “color cannot be a composite of qubits”
- “`M_3(C)` is installed as a two-site composite”
- “this constructs `SU(3)` or QCD”
- “Qubit should be rewritten to `M_3`”
- “an axiom update is necessary”

The shipped claim is only: the corner pad is a non-unital corner, not the
color algebra of the two-site unit.

## Provenance

Parent on `origin/main`: the axiom memo only. The runner binds

`AUDIT_INPUT_PATHS = (this note, docs/MINIMAL_AXIOMS_2026-06-29.md)`

as a string-literal tuple. No citation-manifest edit and no runner-cache
write are part of this surface.
