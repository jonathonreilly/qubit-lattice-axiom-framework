---
claim_id: two_set_content_law_is_not_a_density_matrix_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "A displayed probability μ on a two-point set X={A,B} is a function X→Q. It is not an element of M_2(C) and does not uniquely determine a density matrix ρ. Two explicit densities share the same diagonal (3/5,2/5) and the same Born weights on {P_z,I−P_z} while remaining unequal. The identification of μ with a density is extra. The result does not claim that Born is false, does not force Bloch radius 1/2, and does not adopt L_phys."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_set_content_law_is_not_a_density_matrix_2026_08_13.py
---

# Two-Set Content Law Is Not A Density Matrix

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact type separation between a probability on a two-point set
and a one-qubit density matrix.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_set_content_law_is_not_a_density_matrix_2026_08_13.py`](../scripts/two_set_content_law_is_not_a_density_matrix_2026_08_13.py)

Scientific parent on `origin/main`: the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `X={A,B}` and let `μ` be the probability

`μ(A)=3/5`, `μ(B)=2/5`.

This `μ` is a function `X→Q`. A density matrix is a `2×2` matrix
`ρ=ρ†≥0` with `Tr ρ=1`. Those are different types of object.

Two trial matrices with the same diagonal as the displayed masses,

`ρ0=diag(3/5,2/5)`,

`ρ1=[[3/5,1/5],[1/5,2/5]]`,

are both densities and are unequal. Once off-diagonal entries are allowed,
no unique `ρ` has Born weights on `{P_z,I−P_z}` equal to `μ`. Even the
further dictionary `A↔P_z` is extra: the two-set law does not name a
projector.

The note displays `μ` and the pair `{ρ0,ρ1}`. It does not adopt a
dictionary that would turn `μ` into a matrix. It does not claim that Born
is false. It does not force a Bloch radius `r=1/2`. It does not adopt
`L_phys`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 2-set law is exhibited as a function X→Q; two exact densities share its Born weights on {P_z,I−P_z} and remain unequal. Uniqueness of a density representer and any dictionary into M_2(C) stay extra. No Born-false, axiom-edit, or L_phys claim is made."
trace_class: negative_route_pruning
target_claim_id: two_set_content_law_density_identification
target_blocker_text: "a 2-set content law is not itself a density matrix and does not uniquely determine one"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed μ and the pair {ρ0,ρ1}; no general Born reconstruction is claimed"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let

`X={A,B}`

and let `μ:X→Q` be the probability with

`μ(A)=3/5`, `μ(B)=2/5`.

In particular `μ(A)+μ(B)=1`. As a function on a two-point set, `μ` has no
matrix off-diagonal.

Let `M_2(C)` be the full one-site possibility presentation named by the
Qubit axiom. A **density** here is a matrix `ρ∈M_2(C)` satisfying

`ρ=ρ†`, `ρ≥0`, `Tr ρ=1`.

Write

`ρ0=[[3/5,0],[0,2/5]]`

and

`ρ1=[[3/5,1/5],[1/5,2/5]]`.

Both are Hermitian of trace one. The principal-minor test gives
`det ρ0=6/25>0` and `det ρ1=1/5>0`, so both are positive definite and
hence densities. Their common diagonal is `(3/5,2/5)`. They differ by the
off-diagonal entry `0` versus `1/5`.

Let

`P_z=[[1,0],[0,0]]`

and `I−P_z=[[0,0],[0,1]]`. For any density `ρ`,

`Tr(ρ P_z)=ρ_{00}`, `Tr(ρ(I−P_z))=ρ_{11}`.

## Theorem 1 — A Two-Set Law Has No Off-Diagonal

`μ` is a function `X→Q`. It assigns a rational mass to each point of a
two-element set. That object has no matrix entries and therefore no
off-diagonal.

The matrices `ρ0` and `ρ1` are unequal and both have diagonal
`(3/5,2/5)`. Equality of those two diagonal entries with the values of
`μ` is a numerical coincidence of lists of length two, not an
identification of types.

## Theorem 2 — Born Weights On One Projector Pair Do Not Select A Unique Density

Suppose one asks for a density `ρ` whose Born weights on the menu
`{P_z,I−P_z}` equal `μ`, in the sense

`Tr(ρ P_z)=μ(A)`, `Tr(ρ(I−P_z))=μ(B)`.

Both `ρ0` and `ρ1` satisfy those two scalar equations, because both have
diagonal `(3/5,2/5)`. They are not the same matrix. Therefore there is no
unique `ρ` with that property once off-diagonal entries are allowed.

The predicate “`μ` uniquely determines `ρ`” therefore fails on the
displayed pair `{ρ0,ρ1}`.

Even the remaining dictionary `A↔P_z` (and `B↔I−P_z`) is extra. The
domain of `μ` is the two-point set `{A,B}`, not the projector pair
`{P_z,I−P_z}`. Matching two numbers to two diagonal entries does not
supply that identification.

## Theorem 3 — Axiom Types Already Separate The Objects

The current Admissibility axiom supplies a distribution over
*possibilities*:

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

The current Qubit axiom supplies the algebraic presentation of that
domain:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

A law on a 2-set is a probability on `{A,B}`. It is not an element of
`M_2(C)`. A density `ρ` is an element of `M_2(C)` (with the three density
axioms). The identification of the 2-set law with such a matrix is extra:
neither quoted sentence names a map from two-point content laws to
densities, and Theorems 1 and 2 show that the tempting diagonal
dictionary is not unique and is not typed.

## Theorem 4 — Display, Do Not Translate

The objects used in this note are exactly

- the function `μ` on `{A,B}` with values `3/5` and `2/5`,
- the set of trial densities `{ρ0,ρ1}`.

They are displayed together so that the shared diagonal and the unequal
off-diagonals are visible. This note does not adopt a dictionary sending
`μ` to either matrix, or sending `{A,B}` to `{P_z,I−P_z}`.

This note does not claim that Born is false. It does not deny that some
later derived bridge could attach Born weights to a derived density. It
only records that the displayed 2-set law is not already that density.

## Theorem 5 — No Forced Bloch Radius And No `L_phys`

The Bloch vector of a qubit density is read from

`ρ=(I+r·σ)/2`.

For `ρ0` one has `r=(0,0,1/5)`. For `ρ1` one has `r=(2/5,0,1/5)`. In
neither case is the radius forced to `r=1/2`, and this note does not
impose that value.

This block does not adopt `L_phys`. No physical-law dictionary, and no
named `L_phys` object, is used as a premise or as a conclusion.

## No-Go Discipline Gate

The negative claim is the type mismatch `μ∉M_2(C)` together with the
failure of uniqueness for a density with the same `{P_z,I−P_z}` Born
weights as `μ`. The gate does not certify a global non-derivability
theorem for Born weights.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Read `μ` as already a matrix | treat a function `X→Q` as an element of `M_2(C)` | [Theorem 1](#theorem-1--a-two-set-law-has-no-off-diagonal): `μ` has no off-diagonal | **ATTEMPTED** |
| Diagonal dictionary | set `ρ=diag(μ(A),μ(B))` and call that *the* density | [Theorem 2](#theorem-2--born-weights-on-one-projector-pair-do-not-select-a-unique-density): `ρ1` is another density with the same Born weights on `{P_z,I−P_z}` | **ATTEMPTED** |
| Projector labels | identify `A` with `P_z` because both are “the first alternative” | Theorem 2: that pairing is extra structure | **ATTEMPTED** |
| Force `r=1/2` | replace the displayed masses by a Bloch radius one half | [Theorem 5](#theorem-5--no-forced-bloch-radius-and-no-l_phys): the displayed densities do not have that radius | **ATTEMPTED** |
| Adopt `L_phys` | name a physical-law object that would identify `μ` with `ρ` | Theorem 5 refuses the adoption | **ATTEMPTED** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| 2-set law / density matrix | no: a function `X→Q` names no off-diagonal | no: a density is not a law on `{A,B}` | distinct types |
| common diagonal / uniqueness | no: many densities share a diagonal | no: uniqueness would still need a typed dictionary | independent |
| Born weights on one pair / full state | no: `{P_z,I−P_z}` reads only the diagonal | no: a unique `ρ` would still need a law-to-state map | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `μ` | displayed probability on `{A,B}`; not a global measure on `M_2(C)` |
| `ρ0`,`ρ1` | explicit trial densities; not a classification of all densities |
| `{P_z,I−P_z}` | one computational-basis menu used only to test uniqueness |
| `A↔P_z` | hostile extra dictionary, not axiom content |
| `r=1/2` | refused constraint |
| `L_phys` | refused adoption |
| observations or empirical frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution-over-possibilities sentence; Qubit `M_2(C)` presentation sentence | exact current wording only; no density identification borrowed |

No other scientific parent is used.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the two values of `μ` and the two trial matrices | no classification of every map from 2-set laws to states |
| per site | one algebraic comparison, no lattice dynamics | no composite or intervention theorem |
| per mode | the single menu `{P_z,I−P_z}` | no exhaustion of all measurement menus |
| per block | type mismatch and uniqueness failure | no complete Born/Record closure |
| lattice-wide | not executed | no lattice-wide dynamics or Born no-go |

### N6 — live partial-closure paths

A later derivation could still produce a density from a richer physical
construction (a derived menu of effects, a derived state, and a derived
trace evaluation). That construction is not supplied by displaying `μ`.
This note does not close those routes and does not declare them
impossible.

### N7 — hostile steelman

> Once `{A,B}` is read as the computational basis, `μ` is just the
> diagonal of a density, and any convenient off-diagonal may be set to
> zero. Then `μ` *is* `ρ0`.

The steelman assumes the dictionary that Theorem 2 flags as extra, and
it silently sets the off-diagonal to zero even though `ρ1` is an equally
legal density with the same Born weights on that one menu. The type gap
remains.

### N8 — cross-cycle echo

This block uses only the current axiom memo. It does not inherit a
density-identification from any other note.

**Gate disposition:** PASS for (i) `μ` is a function `X→Q` and not a
matrix, (ii) `{ρ0,ρ1}` are unequal densities with the same
`{P_z,I−P_z}` Born weights as `μ`, and (iii) the identification is extra.
FAIL / DO NOT SHIP for "Born is false," "an axiom update is necessary,"
or "no density can ever be derived from a later bridge."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Qubit and Admissibility sentences | type baseline | supplied; no edit |
| displayed `μ` | 2-set content law | constructed here |
| displayed `{ρ0,ρ1}` | uniqueness witness | constructed here |
| Born trace on `{P_z,I−P_z}` | uniqueness test only | not a claim that Born is false |
| `L_phys` | none | not adopted |
| axiom edits | none | not performed |

## Review Record

Independent audit remains required before any effective status may
change. No axiom file is edited here.
