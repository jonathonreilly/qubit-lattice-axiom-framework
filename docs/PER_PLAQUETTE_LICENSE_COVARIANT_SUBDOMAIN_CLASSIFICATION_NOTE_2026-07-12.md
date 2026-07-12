# Covariant One-Step Link-Subdomain Completeness Classification

**Date:** 2026-07-12  
**Claim type:** bounded_theorem  
**Type:** bounded_theorem  
**Status:** exact finite classification support on the enumerated domains  
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.  
**Primary runner:**
[`scripts/per_plaquette_license_covariant_subdomain_classification_2026_07_12.py`](../scripts/per_plaquette_license_covariant_subdomain_classification_2026_07_12.py)  
**Cached output:**
[`logs/runner-cache/per_plaquette_license_covariant_subdomain_classification_2026_07_12.txt`](../logs/runner-cache/per_plaquette_license_covariant_subdomain_classification_2026_07_12.txt)

## Role

This note closes the finite completeness question left open by block 01. That
block exhibited four named one-step domains and a radius-2 falsifier, but it
did not prove that the four domains exhaust the covariant one-step family or
place radius 2 in the same computed table. Here the order-eight undirected-link
stabilizer is constructed explicitly, its orbits are exhausted, and every
cell of the resulting length-4/length-6 classification is recomputed.

This exact finite classification neither changes block 01's conditional
derivation status nor changes the block-02-wired parent. Its role is upstream
support for that parent's bounded enumeration row.

## Definitions

Let `e1=(1,0,0)`, `e2=(0,1,0)`, and `e3=(0,0,1)`, and fix the undirected
reference link `l={0,e1}`. With the self-plus-nearest-neighbor relation `R`,

```text
C_1(l) = {p : min(d(p,0),d(p,e1)) <= 1}.
```

Inside this 12-point set define the three disjoint sets

```text
E = {0,e1},
A = {-e1,2e1},
T = {+e2,-e2,+e3,-e3,e1+e2,e1-e2,e1+e3,e1-e3}.
```

Thus `C_1(l)=E∪A∪T`. Let `G_l` be the subgroup of proper cubic rotations that
stabilizes the axis of `l`, acting affinely about the midpoint `e1/2`. A
rotation that preserves `e1` fixes the endpoints individually; one that sends
`e1` to `-e1` swaps them.

A covariant domain assignment containing its carrier endpoints is determined
at the reference link by a set `D` with `E subseteq D`. Choice-independent
transport to every other undirected link requires `D` to be `G_l`-invariant;
conversely, stabilizer invariance makes that transport well defined. A
one-step domain additionally obeys `D subseteq C_1(l)`.

## Theorem (completeness)

Under the undirected-link stabilizer `G_l` of the reference link `{0,e1}`
(order 8), the ten-point complement `C_1({0,e1}) minus {0,e1}` decomposes into
exactly two orbits:

```text
A = {-e1,2e1}                                      (size 2),
T = {+e2,-e2,+e3,-e3,e1+e2,e1-e2,e1+e3,e1-e3}    (size 8).
```

Hence the `G_l`-invariant subsets of `C_1({0,e1})` that contain the endpoints
form exactly the four-element lattice

```text
E,  E∪A,  E∪T,  E∪A∪T = C_1.
```

Therefore every covariant one-step license domain in the stated family is one
of those four domains. Graph-radius-2 and larger covariant domains exceed
one-step reachability.

### Proof

The proper cubic rotations are the 24 determinant-`+1` signed permutation
matrices. Exactly eight send `e1` to `+e1` or `-e1`. Acting about `e1/2`, all
eight fix `{0,e1}` as a set; four preserve the endpoints and four swap them.
Direct multiplication of all 64 ordered pairs is closed in the same set, so
these eight transformations form `G_l`.

Axial rotations and the endpoint swap exchange the two points of `A`. The
four transverse directions at one endpoint are exchanged by axial rotations,
and the endpoint swap connects them to the four transverse points at the
other endpoint. Thus `A` and `T` are orbits. They are disjoint, have sizes 2
and 8, and exhaust the ten non-endpoint sites, so there are no other orbits.
The endpoint set `E` is itself the remaining size-2 orbit.

An invariant subset is a union of whole orbits. Requiring `E` leaves an
independent include/exclude choice for `A` and for `T`, giving exactly `2^2 = 4`
orbit unions. The runner independently filters all `2^10 = 1024` subsets
of the non-endpoint sites and finds only those four. Stabilizer
invariance is precisely what removes dependence on the choice of cubic
rotation used to transport the reference domain, proving the covariance
claim in both directions.

Finally, `-2e1 = (-2,0,0)` belongs to the radius-2 domain of `{0,e1}` but not
to `C_1({0,e1})`. Every graph-radius-`r` domain with `r >= 2` contains this
same witness, so none is a one-step domain.

## Computed classification table

For each rooted loop, the tested license requires the full loop support to be
contained in the transported domain of every constituent link. The loop
generator uses the block-01/parent convention: root at the origin, no
immediate backtracking, and no repeated undirected edge. The last column is
the per-domain one-tick / `R`-locality upper-bound test `D subseteq C_1`; it
does not separately assert that an update law has been established as
`R`-local.

| domain | size | length-4 family | length-6 family | one-tick / `R`-local bound (`D subseteq C_1`) |
| --- | ---: | ---: | ---: | :---: |
| `E` (endpoints) | 2 | empty (0/24) | 0/264 | yes |
| `E∪A` | 4 | empty (0/24) | 0/264 | yes |
| `E∪T` | 10 | all plaquettes (24/24) | 0/264 | yes |
| `C_1` | 12 | all plaquettes (24/24) | 0/264 | yes |
| radius-2 | 38 | 24/24 | 264/264 | NO |

The radius-2 cardinality is computed rather than assumed. Each endpoint's
cubic Manhattan radius-2 ball has 25 sites, their intersection has 12 sites,
and their union therefore has `25 + 25 - 12 = 38` sites.

The previously unchecked `E∪A` row is empty at both enumerated lengths:
`0/24` and `0/264`. The radius-2 row admits the full length-6 enumeration.
Its named exterior point is also the block-01 falsifier instance: source `(-2,0,0)` and target `(0,0,0)`
are at graph distance 2, so allowing that
dependency is the witnessed violation class of one-tick confinement.

## Theorem (enumerated-domain interval classification)

On the enumerated lengths 4 and 6, every domain in the four-element lattice
that contains the transverse orbit lies in the interval `[E∪T,C_1]` and gives
the same selection: all 24 plaquettes and no length-6 loop. Both domains that
omit the transverse orbit lie in `[E,E∪A]` and give the constant-empty family.
Equivalently,

```text
E, E∪A       -> 0/24 and 0/264;
E∪T, C_1     -> 24/24 and 0/264.
```

The radius-2 domain is covariant but lies outside the one-step interval; it
gives `24/24` and `264/264`.

### Proof

Completeness leaves exactly the four one-step rows in the table. The two rows
containing `T` have the identical computed vector `(24,0)`, while the two rows
missing `T` have `(0,0)`. This exhausts the lattice, so the statement is a
theorem on the enumerated domains rather than an extrapolation from selected
examples. The independently computed radius-2 row fails the one-tick
containment test and has vector `(24,264)`.

The classification therefore isolates exactly what these finite enumerations
can and cannot distinguish. In particular, they cannot select `C_1` over its
strict `E∪T` subdomain. As block 01 states, the permissive one-tick derivation,
not the enumeration outcomes, pins the full `C_1` bound.

## Boundaries

- This theorem concerns the enumerated lengths 4 and 6 only; no other loop
  length is classified.
- This is a classification of covariant domains, not a classification of
  licenses beyond the endpoint-containing, stabilizer-invariant one-step
  family.
- This does **not** prove that the fundamental action is per-plaquette and
  makes no per-plaquette-action claim.
- The table checks domain containment in `C_1`; it does not derive the
  block-01 `(P-FUND-1TICK)` premise or enlarge the finite-graph theorem into a
  physical-spacetime statement.
- `theta_bare` is untouched.
- This block does not amend an axiom or approved primitive.
- Blocks 01 and 02 and their artifacts are not modified by this classification.

## Dependencies and context

- [PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md](PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md)
  — supplies the four named domains, enumeration convention, radius-2
  falsifier instance, and the statement that the derivation rather than the
  finite outcomes pins `C_1`; its conditional boundary is unchanged.
- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) — supplies
  only the finite-graph definition of `C_t` and the `R`-local reachability
  scope.
- The block-02-wired parent enumeration note
  `PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  is downstream context under the same rooted-loop convention. It remains
  backticked rather than linked here, preserving the acyclic citation
  direction.

## Verification

```bash
python3 scripts/per_plaquette_license_covariant_subdomain_classification_2026_07_12.py
python3 scripts/precompute_audit_runners.py --runners scripts/per_plaquette_license_covariant_subdomain_classification_2026_07_12.py --force --allow-non-main --push-mode none
python3 scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py | tail -5
python3 scripts/frontier_per_plaquette_from_adjacency_license_2026_06_09.py | tail -3
git status --short
```

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "The order-eight stabilizer exhausts endpoint-containing covariant one-step domains, and the length-4/length-6 table classifies those four domains plus radius 2."
```
