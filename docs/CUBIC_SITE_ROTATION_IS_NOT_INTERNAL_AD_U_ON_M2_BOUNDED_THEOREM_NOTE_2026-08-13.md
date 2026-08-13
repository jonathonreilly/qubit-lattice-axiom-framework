---
claim_id: cubic_site_rotation_is_not_internal_ad_u_on_m2_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The proper cubic 90° site rotation R about z is a 3×3 integer matrix on Z^3. The candidate internal conjugator U=exp(-i π/4 σ_z) is an element of SU(2) ⊂ M_2(C) and does not map sites to sites. The declared extra matching that R on Bloch vectors equals Ad_U on Pauli matrices holds for this pair, but the current Lattice and Qubit sentences do not identify the two actions. The matching is displayed; a spin-orbit axiom is not adopted. The note does not claim that spin-1/2 is impossible and does not force r=1/2."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cubic_site_rotation_is_not_internal_ad_u_on_m2_2026_08_13.py
---

# Cubic Site Rotation Is Not the Internal Ad_U on M_2(C)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** one spatial 90° cubic rotation about a site, one internal
`SU(2)` conjugator on the one-site algebra `M_2(C)`, and the declared extra
Bloch-chart matching between them.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cubic_site_rotation_is_not_internal_ad_u_on_m2_2026_08_13.py`](../scripts/cubic_site_rotation_is_not_internal_ad_u_on_m2_2026_08_13.py)
**Parents:** the current axiom memo only
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)).
**Runner cache:** not produced in this block.

## Result Up Front

A proper cubic site rotation and an internal `SU(2)` conjugation are
different kinds of map. They can be paired by an extra Bloch-chart matching,
but the current axioms do not make that pairing.

1. The spatial 90° rotation about `z` is the integer matrix
   `R=[[0,-1,0],[1,0,0],[0,0,1]]` acting on site coordinates in `Z^3`.
   It is orthogonal of determinant one. It has no matrix elements in
   `M_2(C)` and is not an element of `SU(2)`.
2. The internal candidate `U=exp(-i π/4 σ_z)=diag(e^{-iπ/4}, e^{iπ/4})`
   lies in `SU(2) ⊂ M_2(C)`. It does not act on `Z^3`: it does not map
   sites to sites. `R` and `U` live on different spaces.
3. The *declared extra matching* “`R` on Bloch vectors equals `Ad_U` on
   Pauli matrices” holds for this pair: both send `e_1 ↦ e_2` on the Bloch
   chart. That matching is extra. The Lattice sentence names rotations of
   sites; the Qubit sentence names the algebra `M_2(C)` at each site.
   Neither sentence identifies the two actions.
4. The matching is displayed. A spin-orbit axiom is not adopted. A theory
   can have cubic site symmetry and an internal `SU(2)` that are not
   identified.
5. This note does not claim spin-1/2 is impossible. It does not force
   `r=1/2`. It does not edit axioms.

A predicate “`R` equals `U` as matrices” fails because one matrix is `3×3`
and the other is `2×2`. A predicate “the axioms identify `R` with `Ad_U`”
fails because the quoted Lattice and Qubit sentences do not make that
identification.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact 3×3 versus 2×2 type separation and an explicit extra Bloch-chart matching are proved on declared objects; spin-orbit identification is not adopted and spin-1/2 remains live."
trace_class: negative_route_pruning
target_claim_id: cubic_site_rotation_internal_ad_u_identification
target_blocker_text: "do not treat spatial cubic rotation as internal Ad_U on M_2(C) without an extra matching"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed R, U, Ad_U, and the extra Bloch matching; no spin-orbit axiom is adopted"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)` for the standard basis of
the site-coordinate module, and also for the Bloch chart of the Pauli
triple.

The spatial 90° rotation about `z` is the `3×3` integer matrix

```
R = [[ 0, -1,  0],
     [ 1,  0,  0],
     [ 0,  0,  1]].
```

It acts on `Z^3` by left multiplication on column site coordinates. This is
the Lattice action: proper cubic rotations about a site.

The Pauli matrices on the one-site algebra `M_2(C)` are

```
σ_x = [[0, 1], [1,  0]],
σ_y = [[0,-i], [i,  0]],
σ_z = [[1, 0], [0, -1]].
```

The internal candidate is

```
U = exp(-i π/4 σ_z) = diag(e^{-iπ/4}, e^{iπ/4})
  = (1/√2) diag(1-i, 1+i).
```

Conjugation is `Ad_U(M) = U M U†`. Standard `SU(2)` calculus gives

```
Ad_U(σ_x) = σ_y,
Ad_U(σ_y) = -σ_x,
Ad_U(σ_z) = σ_z.
```

The identity gates of the companion runner obtain `R` only by calling
`spatial_Rz90()` and obtain `Ad_U(σ_x)` only by calling `ad_Uz90(sigma_x)`.

## Quoted Axiom Sentences

The current public axiom memo is
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

**Lattice** (rotations of sites):

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic
> rotations about each site.

**Qubit** (algebra `M_2(C)` at each site):

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Neither sentence identifies a cubic site rotation with an internal
conjugation `Ad_U` on `M_2(C)`. Admissibility requires the nearest-neighbor
rule to be covariant under proper cubic rotations; that covariance is a
constraint on the admissibility rule, not an identification of `R` with
`Ad_U`.

## Theorem 1 — R is a proper cubic 3×3 matrix, not an element of SU(2)

`R` has integer entries. Direct multiplication gives

```
R^T R = I_3,    det R = 1.
```

So `R` is a proper rotation matrix on the site-coordinate module. Every
entry of `R` is an integer acting on `Z^3`. The matrix is `3×3`. It
therefore has no matrix elements in `M_2(C)`: elements of `M_2(C)` are
`2×2` complex matrices. In particular `R` is not an element of `SU(2)`.

## Theorem 2 — U lives in SU(2) and does not map sites to sites

`U` is `2×2`. Its entries are `e^{-iπ/4}=(1-i)/√2` and
`e^{iπ/4}=(1+i)/√2`. Then

```
U U† = I_2,    det U = e^{-iπ/4} e^{iπ/4} = 1,
```

so `U ∈ SU(2) ⊂ M_2(C)`. Left multiplication by `U` acts on `C^2`, or by
conjugation on `M_2(C)`. It does not act on `Z^3`: a `2×2` matrix does not
send a site `(x,y,z) ∈ Z^3` to another site. Therefore `R` and `U` live on
different spaces.

## Theorem 3 — the Bloch matching holds and is extra

On site coordinates, `R e_1 = e_2`. On the Bloch chart the same list of
standard basis vectors labels the Pauli triple, and

```
Ad_U(σ_x) = σ_y
```

is the corresponding 90° rotation about `z`. The declared extra matching
“`R` on Bloch vectors equals `Ad_U` on Pauli matrices” therefore holds for
this pair: both send `e_1 ↦ e_2` on the Bloch chart.

That matching is extra. Quote Lattice (rotations of sites) and Qubit
(algebra `M_2(C)` at each site). Neither sentence identifies the two
actions. The matching is a further pairing of a `3×3` lattice rotation with
a `2×2` internal conjugator. It is not a consequence of the axiom text.

## Theorem 4 — display the matching; do not adopt a spin-orbit axiom

The pair `(R, Ad_U)` is exhibited above. Displaying a matching is not the
same as adopting it as axiom content. This note does not adopt a
spin-orbit axiom. A theory can have cubic site symmetry and an internal
`SU(2)` that are not identified. Cubic covariance of the Lattice and
Admissibility wording can stand while the one-site algebra retains its
internal `SU(2)` without a forced weld of the two actions.

## Theorem 5 — no spin-1/2 impossibility and no r=1/2 force

This note does not claim spin-1/2 is impossible. It does not force
`r=1/2`. It does not edit axioms. The only negative claim is that the
current Lattice and Qubit sentences do not already identify `R` with
`Ad_U`, and that `R` and `U` are not the same matrix.

## Mutation Predicates

Two hostile predicates are tested by the runner and must fail.

1. **“`R` equals `U` as matrices.”** Fail: `R` is `3×3` and `U` is `2×2`.
   Shape mismatch already falsifies matrix equality.
2. **“The axioms identify `R` with `Ad_U`.”** Fail: the quoted Lattice and
   Qubit sentences name site rotations and the one-site algebra
   separately; they do not identify the two actions.

Identity gates must call `spatial_Rz90()` and `ad_Uz90(sigma_x)`.

## No-Go Discipline Gate

The negative claim is type separation plus non-identification in the
current axiom wording. The gate does not certify a spin-statistics
impossibility or a forced spin-orbit weld.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Matrix equality | treat `R` and `U` as the same array | shapes `3×3` versus `2×2` | **ATTEMPTED** |
| Axiom identification | read Lattice and Qubit as already welding `R` to `Ad_U` | quoted sentences do not identify the actions | **ATTEMPTED** |
| Silent spin-orbit axiom | adopt the Bloch matching as axiom content | matching is displayed and extra; not adopted | **ATTEMPTED** |
| Spin-1/2 prohibition | infer that spin-1/2 cannot occur | not claimed | **NOT CLAIMED** |
| Force `r=1/2` | replace an open spin residual by a forced half-integer | not claimed | **NOT CLAIMED** |

### N2 — wall independence

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `R` as `SO(3,Z)` matrix / `U` as `SU(2)` matrix | no | no | different spaces |
| Bloch-chart matching / axiom identification | no: a displayed pairing is extra | no: axiom text does not create the pairing | independent |
| cubic site symmetry / internal `SU(2)` | no | no | both can exist unidentified |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `R` | declared `3×3` integer 90° rotation about `z` on `Z^3` |
| `U` | declared `exp(-i π/4 σ_z)` in `SU(2)` |
| `Ad_U` | conjugation on `M_2(C)`, not a site map |
| Bloch chart | declared extra matching surface; not axiom content |
| spin-orbit axiom | not adopted |
| `r=1/2` | not forced |
| observations | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice proper cubic rotations about each site; Qubit one-site algebra `M_2(C)` | exact current wording only; no identification borrowed |

No other scientific parent is used.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | one `R` and one `U` | no classification of every possible pairing |
| per site | one site-centered cubic rotation and one one-site algebra | no composite carrier |
| per mode | the `z`-axis 90° case | no exhaustion of all cubic words |
| per block | identification of spatial `R` with internal `Ad_U` | no spin-statistics theorem |
| lattice-wide | `R` acts on `Z^3`; `U` does not | no lattice-wide dynamics |

### N6 — live partial-closure paths

A later retained derivation could still introduce an extra matching, or a
named primitive, that welds a cubic rotation to an internal conjugator.
That path remains live. It is not taken here, and it is not an axiom edit.

### N7 — hostile steelman

> Once Bloch vectors are drawn as arrows in the same `R^3` that carries
> the lattice, `R` and `Ad_U` are “the same rotation,” so the axioms
> already contain spin-orbit coupling.

The steelman names the extra matching and then pretends the axioms stated
it. Theorem 3 grants the matching as extra and denies the attribution.

### N8 — what is not shipped

**Gate disposition:** PASS for (i) `R` is a proper `3×3` cubic rotation
and not an element of `SU(2)`, (ii) `U` is in `SU(2)` and does not map
sites, (iii) the Bloch matching holds and is extra, and (iv) the two
mutation predicates fail. FAIL / DO NOT SHIP for “spin-1/2 is
impossible,” “force `r=1/2`,” “an axiom update is necessary,” or “adopt a
spin-orbit axiom.”
