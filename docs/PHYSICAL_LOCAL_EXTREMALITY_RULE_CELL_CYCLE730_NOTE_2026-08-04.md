# Per-piece zero-slack criterion and finite endpoint-support census — Cycle 730

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted. Audit status is set only by the independent
audit lane, and effective status is pipeline-derived.

Primary runner:
`scripts/physical_local_extremality_rule_cell_cycle730_2026_08_04.py`
(47 PASS / 0 FAIL; deterministic exact arithmetic; fails closed).

Independent checker:
`scripts/physical_local_extremality_rule_cell_cycle730_independent_check_2026_08_04.py`
(15 PASS / 0 FAIL; the checker does not import or execute the primary).

## Supplied model and exact scope

This is a finite theorem about the supplied one-cell, one-tick corner-simplex
model declared by [Cycle 725](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md).
The box is `{0,1}^4`; the first three coordinates are spatial and the fourth is
the tick coordinate. A piece is the convex hull of five corners with normalized
lattice four-volume one, and a dissection is a family of 24 such pieces with
disjoint interiors that fills the box. The declared adjacency charge of a piece
counts corner pairs whose spatial `L1` separation exceeds one.

The [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) supply only the spatial
`Z^3` nearest-neighbour grading and proper cubic rotations. The registered
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies only equal tick/edge graining. Neither selects corner-simplex pieces,
the dissection domain, the charge functional, a physical assembly cell, or a
tick--Admissibility realization.

Within this supplied model, Cycle 725 proves that minimal-piece dissection cost
lies in `[108,128]`, with both endpoints attained. The Cycle 730 runner also
reconstructs the piece census, charge, certificates, and endpoint witnesses;
the Cycle 725 receipt is separately hash-bound to prevent the shared model and
endpoint context from drifting silently.

## Exact theorem

For a minimal piece `p`, let `M[p,o]` count the generic interior sample points
of point orbit `o` inside `p`. For the floor certificate, integers `u_o`, `Z`,
and positive denominator `D=24` satisfy

```text
sum_o M[p,o] u_o + Z <= D charge(p)
```

on all 2672 pieces. Define the nonnegative floor slack

```text
s_floor(p) = D charge(p) - sum_o M[p,o] u_o - Z.
```

Every sample point lies in the interior of exactly one piece of any valid
dissection. Hence, for any valid dissection `T` of cost `C`,

```text
sum_{p in T} s_floor(p) = 24 (C - 108).
```

The ceiling certificate reverses the inequality and has denominator six, so

```text
sum_{p in T} s_ceiling(p) = 6 (128 - C).
```

All slacks are nonnegative. Therefore, conditional on `T` already being a
valid dissection:

- `C=108` exactly when every piece of `T` has zero floor slack;
- `C=128` exactly when every piece of `T` has zero ceiling slack.

This is an additive per-piece endpoint-equality criterion. It does **not** make
realizability piecewise or coordination-free: compatibility, disjointness, and
coverage remain global conditions on a dissection.

## Finite support census

The floor zero-slack set contains 2416 pieces in 51 symmetry orbits. The
ceiling zero-slack set contains 1040 pieces in 23 orbits; 784 pieces are in
both sets and none is in neither.

The primary inspects 200000 sample exact covers at each endpoint. It does not
equate a sample exact cover with a geometric dissection. Whenever a cover adds
a previously unseen orbit, the runner separately checks all 276 piece pairs
for an exhibited separating direction and checks volume and full sample
coverage. It stores a validated 24-piece witness for every orbit classified as
realized. The result is:

- floor: 38 realized orbits and 13 excluded orbits;
- ceiling: 21 realized orbits and 2 excluded orbits.

At the floor, every piece in the 13 excluded orbits has a one-step
sample-cover orphan certificate. Force the piece, remove every zero-slack piece
sharing an interior sample point with it, and one uncovered sample point has no
remaining candidate. This excludes 624 pieces, all in the first round. The
receipt stores one forced-piece/orphan-point certificate per orbit, while the
runner checks all 624 pieces.

At the ceiling, the same one-step test excludes no piece. The two excluded
orbits instead have independently replayable exhaustive forced-cover searches.
The primary reports and stores the visited-node counts and fails if the search
hits its 20000000-node cap. The independent checker reruns these searches with
a different point-selection order.

The classification is thus exact only for the supplied finite model and these
two endpoint zero-slack sets. “Excluded” means that no valid dissection at the
corresponding endpoint contains the piece. It does not exclude the piece from
non-extremal dissections or from another cell/dissection model.

## Additional exact checks

- There are 4368 five-corner subsets, 2672 normalized-volume-one pieces, and
  nonzero normalized volumes are `1,2,3`.
- Piece charge has spectrum `3:64, 4:384, 5:1152, 6:768, 7:304`.
- The supplied box action used here has 24 proper spatial rotations and the
  independent tick flip, giving 48 maps and 57 piece orbits of sizes 16 or 48.
- The generic sample has 2736 points, no orbit collisions, and no incidence on
  any piece boundary.
- The floor and ceiling certificates have values `2592=24*108` and
  `768=6*128` and are checked on all pieces with integer arithmetic.
- A monotone-path dissection attains 108. A separate dissection with one
  positive-floor-slack piece has cost 110 and slack `48=24*(110-108)`.

## Proof boundary

Proof-obligation disposition: **CLOSED for the stated finite conditional
domain**. The certificate identities, geometric witnesses, and exclusion
certificates discharge every leaf of the finite theorem. The disposition is
**CONDITIONAL for any physical interpretation**, because the corner-simplex
model and charge are supplied rather than selected by the framework.

The result does not derive or assert:

- a framework Admissibility rule or an identification with that rule;
- a physical tick--Admissibility realization or physical cell selection;
- a theorem for nonsimplicial, coarser, noncorner, multi-cell, or multi-tick
  dissections;
- an arbitrary-size, boundary, continuum, metric, curvature, action, or field
  equation result;
- minimality of either certificate denominator.

Cycles 728 and 729 are ordering/context predecessors only. This single-cell
packet consumes none of their two-cell block endpoints, witnesses, seam
classes, or lift-obstruction statements.

## No-Go Discipline Gate

The finite “excluded orbit” statements are a `derived_no_go_boundary` inside
this bounded theorem. They are not a framework `no_go` result. The following
N1--N8 record applies only to the two finite endpoint-support partitions.

### N1 — Alternative route enumeration

1. **Constructive counterexample route — ATTEMPTED.** Search for a
   zero-slack exact cover containing each allegedly excluded representative.
   The ceiling searches and nine floor searches exhaust; the four remaining
   floor representatives are already stopped by a one-step orphan.
2. **False-positive sample-cover route — ATTEMPTED.** A sample exact cover may
   fail to be a dissection. Every realized orbit now carries a separately
   checked geometric 24-piece witness; the primary does not classify from an
   unvalidated cover.
3. **Orphan-escape route — ATTEMPTED.** For all 624 excluded floor pieces, the
   runner recomputes a sample point that the forced piece does not contain and
   whose every zero-slack carrier overlaps the forced piece at an interior
   sample point.
4. **Symmetry-representative failure route — ATTEMPTED.** The full 48-map
   action is reconstructed, charge and slack are constant on every orbit, and
   the floor orphan test is nevertheless run piece-by-piece rather than only
   on representatives.
5. **Endpoint escape through an off-rule piece — ATTEMPTED.** The exact slack
   sums on floor, ceiling, and cost-110 controls show that any positive slack
   changes the endpoint cost by exactly its denominator-scaled amount; no
   endpoint dissection can contain an off-rule piece.

### N2 — Wall-independence audit

The finite negative residual is one statement: non-participation in an
endpoint dissection of this supplied model. It is not split into multiple
walls. Two separate open physical interpretations lie outside the finite
claim:

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| tick--Admissibility realization / physical-cell corner-simplex identification | no | no | yes |

Closing either physical bridge would not alter the finite certificates; it
would only widen their interpretation.

### N3 — Hidden-wall scan

“Supplied,” “certificate,” and “symmetry” are explicit constructions, not
hidden framework grants. The model, charge, sample recipe, certificate
integers, and search caps are all carried. No “standard,” “obvious,”
“canonical,” or unlinked “framework provides” step is load-bearing.

### N4 — Residual matching

Cycle 725 proves the `[108,128]` endpoint bracket in the same supplied model.
It does not prove the Cycle 730 support exclusions and is not cited as a
negative witness. The current orphan/search certificates attack exactly the
residual claimed here: whether a named zero-slack piece can occur in a valid
dissection at the matching endpoint.

### N5 — Rhetoric audit

- `per_element`: all 2672 pieces and every support orbit are resolved.
- `per_site`: not applicable; the supplied object has no site field.
- `per_mode`: not applicable; no modal decomposition is used.
- `per_block`: the complete supplied one-cell by one-tick box is resolved.
- `lattice_wide`: not tested and not claimed.

The same substantive five-line certificate lands in the primary runner's
canonical cached stdout.

### N6 — Partial-closure path scan

The primitive registry was checked. Minimal Axioms supply only spatial
adjacency/rotations; kinetic isotropy supplies only equal tick/edge graining.
Neither selects the supplied simplex model or physical realization. A future
physical bridge could widen interpretation without adding a new axiom, but it
is not required for this finite theorem and is not foreclosed here.

### N7 — Steelman

The strongest objection is that exact coverage of finitely many interior
sample points does not imply pairwise-disjoint convex pieces filling the box.
That objection defeats the submitted census if sample covers are accepted as
dissections. The repaired artifact accepts the objection: classification as
realized now requires a stored witness whose volume, coverage, and all 276
pairwise separations are checked. For exclusions, every genuine endpoint
dissection would necessarily be a zero-slack sample exact cover, so an orphan
or an exhaustive absence of such a cover is sufficient in the other direction.

### N8 — Cross-cycle echo

Cycle 725 already distinguishes sample-cover bounds from geometrically checked
attainment and explicitly warns that the sample device bounds a larger family
than dissections. Cycle 726 likewise separates supplied-model finite
exclusions from physical interpretation. Cycle 730 follows those repairs:
sample coverage alone proves only one-sided impossibility; positive
realizability carries geometric witnesses; no physical or arbitrary-size
foreclosure is inferred.

No-Go Discipline result: **PASS for the finite support exclusions at the exact
scope above**.

## Artifacts

- Primary runner:
  `scripts/physical_local_extremality_rule_cell_cycle730_2026_08_04.py`
- Independent checker:
  `scripts/physical_local_extremality_rule_cell_cycle730_independent_check_2026_08_04.py`
- Primary cache:
  `logs/runner-cache/physical_local_extremality_rule_cell_cycle730_2026_08_04.txt`
- Independent cache:
  `logs/runner-cache/physical_local_extremality_rule_cell_cycle730_independent_check_2026_08_04.txt`
- Cold output:
  `outputs/physical_local_extremality_rule_cell_cycle730_2026_08_04_cold_2026-08-04.txt`
- Generated receipt:
  `outputs/physical_local_extremality_rule_cell_cycle730_2026_08_04_receipt_2026-08-04.json`
