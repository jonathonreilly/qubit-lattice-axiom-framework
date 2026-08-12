# Finite column-family parity and minimum-support census — Cycle 733

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No axiom or
primitive is proposed or adopted. Audit status is set only by the independent
audit lane, and effective status is pipeline-derived.

Primary runner:
[`scripts/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.py`](../scripts/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.py)
(deterministic exact arithmetic; fails closed).

Independent checker:
[`scripts/physical_column_family_parity_law_forced_orbits_cycle733_independent_check_2026_08_04.py`](../scripts/physical_column_family_parity_law_forced_orbits_cycle733_independent_check_2026_08_04.py)
(does not import or execute the primary).

## Supplied model and dependencies

This is a finite theorem about the supplied one-cell, one-tick corner-simplex
model declared by [Cycle 725](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md).
The box is `{0,1}^4`; the first three coordinates are spatial and the fourth is
the tick coordinate. A piece is the convex hull of five corners with normalized
lattice four-volume one. A dissection is 24 such pieces with disjoint interiors
that fill the box.

The [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) supply only spatial `Z^3`
nearest-neighbour adjacency and proper cubic rotations. The registered
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies only equal tick/edge graining. Neither selects this four-box, the
corner-simplex domain, the cost family, a physical assembly cell, or a
tick--Admissibility realization.

The spatial cost and its exact floor support are taken from
[Cycle 731](PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md).
The primary hash-binds the Cycle 725 and Cycle 731 notes, runners, and receipts;
the independent checker AST-validates the carried Cycle 731 certificate against
the current Cycle 731 primary before using it.

Cycle 732 is ordering/context only. Cycle 733 reconstructs the entire
column-cost family and its parity systems locally and consumes no Cycle 732
certificate, witness, or bound.

## Cost family

For a nonempty set `S` of the four columns, define the cost of a piece to be the
number of its ten corner pairs whose Hamming distance in the selected columns
is greater than one. A dissection cost is the sum over its 24 pieces.

There are 15 nonempty column sets. The four singletons give zero on every
piece. The remaining 11 fall into five symmetry classes of sizes
`[1,1,3,3,3]`, classified by spatial-column count and whether the tick is
included. All 29 ordered pairs within those classes are joined by an explicit
cell symmetry. Adding a column never decreases any piece cost.

Every nonzero family member takes at least two values on the 13 exhibited
geometric dissections. This proves only that none is constant on the supplied
dissection domain; it is not a statement about other cells or cost families.

## Exact parity result

The finite sample has 2,736 rational interior points in 57 symmetry orbits.
No point lies on any minimal piece boundary. Each point is therefore in exactly
one piece of any valid dissection.

For each of the ten nonzero proper column sets, exact elimination over `GF(2)`
produces point weights `w_q` and a constant `c` such that, on every one of the
2,672 minimal pieces `p`,

```text
cost_S(p) = c + sum_{q inside p} w_q  (mod 2).
```

Each exhibited solution has even weight support. A dissection contains 24
pieces, so both the repeated constant and the sample-point sum are even. Every
valid supplied-model dissection consequently has even cost for each of the ten
proper nonzero column sets.

The full four-column cost is different. The 13 exhibited dissections contain
both parities. Separately, four explicit pieces have incidence rows whose sum
is zero over `GF(2)` (228 points are covered exactly twice) while their full
costs sum to 25. This is a dual inconsistency certificate for the affine parity
system. Exhaustion over one-, two-, and three-piece row combinations confirms
that four is the smallest support of this particular dual form.

On every minimal piece, the full cost splits exactly as

```text
full cost = spatial cost
          + pairs that step in the tick and exactly one spatial direction.
```

The identity holds on all 2,672 pieces; deleting the second term leaves only
64 matches. Thus, within this defined family and supplied cell, the second term
carries the possible odd contribution.

## Exact minimum and support census

The full cost of a minimal piece has spectrum
`6:400, 7:1216, 8:864, 9:192`. Every dissection contains 24 pieces, so its full
cost is at least `24*6=144`. The monotone-path dissection, constructed from the
24 orders in which the four columns can switch from zero to one, attains 144.

A complete exact-cover enumeration over the 400 cost-six pieces visits 502,838
nodes and returns 15,800 covers. Sample coverage is not treated as geometric
sufficiency. The primary separately checks all 276 piece pairs in one
representative of each of the 391 symmetry orbits; all representatives have
disjoint interiors and full coverage, and the 48-element action carries those
certificates to all 15,800 solutions. The independent checker repeats the
enumeration from the opposite point order and redoes the geometry checks.

The 15,800 minimum dissections use 192 pieces, exactly four 48-piece symmetry
orbits. Every minimum dissection contains members of all four, so removing any
one orbit leaves no minimum dissection. The other 208 cost-six pieces occur in
none of the complete list.

Every minimum full-cost dissection has spatial cost 108 and tick-coupled term
36. Every used piece belongs to Cycle 731's 1,792-piece spatial floor support.
The converse fails: an exhibited spatial-floor dissection has full cost 163.

All 2,672 sample-incidence footprints are distinct. Therefore a one-piece hole
in any of the 15,800 dissections can be refilled by its removed piece and by no
other supplied minimal piece: any genuine one-piece refill would necessarily
have the same complete interior-sample footprint.

Exactly two costs are constant on the 57 piece orbits: the spatial and full
costs. Their joint values overlap between the 192 used and 208 unused pieces,
so they do not separate the classes. The full 11-cost vector does: it has 12
values on the used class and 13 on the unused class, with empty intersection.
This is a finite classification of the computed cost-six support, not a local
rule selected by the framework.

## Proof boundary

Proof-obligation disposition: **CLOSED for the stated finite supplied-model
domain**. The parity certificates, dual obstruction, exact-cover enumeration,
geometric representative checks, and complete support comparison discharge the
finite leaves. The disposition is **CONDITIONAL for any physical
interpretation**, because the four-box, tick realization, corner-simplex domain,
and cost family are supplied rather than selected by the framework.

This result does not derive or assert:

- a framework Admissibility rule or physical cell/simplex selection;
- a physical tick--Admissibility bridge or charge/action interpretation;
- a result for nonsimplicial, noncorner, coarser, multi-cell, or multi-tick
  dissections;
- an arbitrary-size, boundary, continuum, metric, curvature, action, or field
  equation theorem;
- a maximum dissection cost or complete cost spectrum;
- minimal support for the ten positive parity certificates;
- a certificate-independent local rule that predicts the 192-piece support.

## No-Go Discipline Gate

The finite parity obstruction and exact nonparticipation/separation statements
are `derived_no_go_boundary` assertions inside this bounded theorem. They are
not a framework `no_go` result. The following N1--N8 record applies only to the
explicit finite universes above.

### N1 — Alternative route enumeration

1. **Parity counterexample route — ATTEMPTED.** The 13 geometric dissections
   contain both full-cost parities, directly refuting a constant full-cost
   parity law while leaving the ten proper-set certificates intact.
2. **Affine-certificate escape route — ATTEMPTED.** Exact `GF(2)` elimination
   declares the full affine system inconsistent, and the four-piece dual row
   combination proves that inconsistency without trusting failed search.
3. **Smaller-dual route — ATTEMPTED.** All one-, two-, and three-piece row
   combinations are excluded; the exhibited four-piece obstruction is minimal
   only within this declared dual-support class.
4. **Missed minimum through a higher-cost piece — ATTEMPTED.** Since every
   piece costs at least six and a dissection has exactly 24 pieces, equality at
   144 forces every piece to be in the complete 400-piece cost-six pool.
5. **False-positive sample-cover route — ATTEMPTED.** All 391 exact-cover
   orbit representatives are separately checked for pairwise geometric
   separation, volume, and coverage. A hostile sample-disjoint but overlapping
   simplex pair confirms that this gate discriminates.
6. **Orbit-representative failure route — ATTEMPTED.** The complete 48-map
   action permutes the 2,672 pieces and the 15,800 solutions; the geometric
   representatives cover every solution orbit.
7. **Excluded-piece escape route — ATTEMPTED.** The complete minimum list is
   reconstructed independently from the opposite sample-point order. The used
   set is the same 192 pieces; all 208 complements are absent.
8. **One-hole alternate route — ATTEMPTED.** Any one-piece refill must cover
   the identical complete generic-sample footprint, and all 2,672 footprints
   are distinct.

### N2 — Wall-independence audit

The finite negative residual has two explicitly separate statements: affine
full-set parity inconsistency and nonparticipation in the finite minimum-support
class. Neither implies the other; each has its own certificate/enumeration.
The open physical bridges (cell/simplex selection and tick--Admissibility
realization) can widen interpretation but cannot change either finite result.

### N3 — Hidden-wall scan

“Supplied cell,” “cost family,” “minimal piece,” “sample,” and “symmetry” are
explicit constructions. The primary declares and hashes every load-bearing
upstream input. No standard/canonical physical selection is inferred from the
Minimal Axioms or kinetic-isotropy primitive.

### N4 — Residual matching

Cycle 725 supplies the finite model and adjacency bracket. Cycle 731 supplies
the spatial floor certificate/support. Neither establishes the Cycle 733
column-family parity systems, full-set obstruction, full-cost enumeration, or
192/208 support partition. The Cycle 733 evidence attacks exactly those new
finite residuals.

### N5 — Rhetoric audit

- `per_element`: all 2,672 minimal pieces are checked.
- `per_site`: not applicable; this finite object has no lattice-site field.
- `per_mode`: not applicable; no modal decomposition is used.
- `per_block`: the complete supplied one-cell by one-tick box is checked.
- `lattice_wide`: not tested and not claimed.

The same substantive five-line certificate lands in both canonical cached
stdout paths.

### N6 — Partial-closure path scan

The primitive registry was checked. Minimal Axioms and kinetic isotropy do not
select this model. A future physical selection bridge could widen the result's
interpretation without changing the finite theorem; no new axiom is needed or
proposed here.

### N7 — Steelman

The strongest objection is that exact coverage of finitely many interior
points does not prove that convex simplices have disjoint interiors. That
objection defeats the submitted enumeration if sample covers are accepted as
dissections. The repaired artifact accepts it: every positive solution orbit
now carries an exact separating-direction check for all 276 simplex pairs.
For the negative direction, every genuine minimum dissection would necessarily
be one of the enumerated sample exact covers, so complete absence remains
sufficient.

### N8 — Cross-cycle echo

Cycle 725 and Cycle 730 already separate sample exact covers from geometrically
checked dissections. Cycle 731 keeps the cell/charge choice supplied. Cycle 733
preserves both disciplines, adds no framework-selection claim, and treats Cycle
732 as context rather than laundering its result as an input.

No-Go Discipline result: **PASS for the finite full-set obstruction and exact
minimum-support exclusions at the scope above**.

## Artifacts

- Primary cache:
  `logs/runner-cache/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.txt`
- Independent cache:
  `logs/runner-cache/physical_column_family_parity_law_forced_orbits_cycle733_independent_check_2026_08_04.txt`
- Generated receipt:
  `outputs/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04_receipt_2026-08-04.json`

The receipt is generated by the primary and binds the exact declared input
bytes. Reviewer PASS on this source packet is not an audit verdict.
