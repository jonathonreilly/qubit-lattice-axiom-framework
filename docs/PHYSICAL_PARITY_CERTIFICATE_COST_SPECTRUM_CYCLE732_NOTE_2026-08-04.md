# Exact even cost spectrum in the supplied one-cell corner-simplex model

Date: 2026-08-04

Claim type: bounded_theorem

Status: unaudited source note

Audit authority: none; audit status belongs to the independent audit lane.

## Result

For the supplied unit four-cube model, the exact adjacency-cost spectrum of a
24-piece dissection is

`{108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128}`.

Here the supplied corners are `{0,1}^4`, with three coordinates labelled spatial and
one labelled tick.  An allowed piece is a five-corner simplex of normalized volume one.
The declared charge counts vertex pairs whose spatial L1 separation exceeds one.  A
dissection is an exact cover by 24 allowed pieces.

This is a theorem about that finite supplied object.  The framework does not select the
corner-simplex model, the charge, a physical cell, or a physical tick realization.
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies only the spatial
grading and proper-rotation language.  Equal tick/edge graining is the only premise
imported from
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md).

## Exact finite construction

There are 4,368 five-corner subsets and 2,672 normalized-volume-one pieces.  Their
charge census is

`[(3,64), (4,384), (5,1152), (6,768), (7,304)]`.

The 24 proper spatial rotations, extended by the tick flip, form a 48-element action.
They split the pieces into 57 charge-constant orbits of sizes 16 and 48.

Superincreasing barycentric weights construct 2,736 sample points, 57 free orbits of
size 48.  No sample point lies on any allowed-piece boundary.  The resulting exact
incidence matrix has 2,672 rows and 2,736 columns; its row loads range from 6 to 409 and
its column loads from 90 to 224.

Exact GF(2) elimination produces a 228-point, zero-constant certificate satisfying

`incidence(piece, certificate) = charge(piece) (mod 2)`

for every allowed piece.  Each point is interior to exactly one piece in any supplied
dissection, so summing the congruence gives the cost modulo two.  The certificate has
even cardinality; every supplied-model dissection therefore has even cost.

The independent checker reconstructs the incidence without importing or executing the
primary runner and obtains a different zero-constant certificate with 168 selected
points.  It verifies all 2,672 congruences using pure-Python big-integer elimination.
Thus the parity conclusion does not depend on the primary certificate's symmetry
restriction or pivot choices.

The exact 108 and 128 bound certificates are load-bearing carried data from
[`PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md`](PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md).
The runner parses Cycle 731's six certificate literals, checks its generated receipt,
and re-verifies every row.  The floor numerator is `23328 = 108*216`; the ceiling
numerator is `384 = 128*3`.

Eleven pinned 24-piece covers attain costs

`[108,110,112,114,116,118,120,122,124,126,128]`.

Both runners verify distinct unit-volume pieces, exact point coverage once, and all 276
pair separations in each witness.  The independent checker sweeps 2,928 canonical
primitive normals in `[-4,4]^4`, broader than the primary's ternary-plus-facet family.
Parity, the two exact bounds, and attainment prove the displayed spectrum.

## Two ansatz-bounded negative results

These negatives concern only the fixed 2,736-point incidence ansatz.  They do not rule
out other point families, analytic identities, cochain constructions, or geometric
certificates.

First, exhaustive closure enumerates all 98 subgroups of the 48-element action.  Among
the 12 subgroups of order at least 12, with order census
`[(48,1),(24,3),(16,3),(12,5)]`, exactly one permits an invariant certificate in the
fixed incidence ansatz.  It has order 12; the primary's 228-point certificate has that
stabilizer.  This is a sharp invariance result inside the ansatz, not a claim that every
parity proof must break symmetry by index four.

Second, the same fixed incidence-plus-constant system is inconsistent modulo three.
The four rows indexed `[(72,1),(74,2),(176,2),(479,1)]` have weighted incidence entries
only 0 or 3 and total coefficient 6, but their weighted charges total 31.  This exact
dual relation contradicts a modulo-three solution in that matrix.  It is a discrete
row relation, not a claim of a geometric triple cover and not an exclusion of other
certificate mechanisms.  Full elimination agrees.  Among 8,008 six-corner subsets,
1,104 contain a locally inconsistent subsystem: 864 with four contained allowed pieces
and 240 with six.

The greatest common divisor of differences among the eleven exhibited costs is two.
That fact alone makes parity the greatest universal congruence modulus for this supplied
cost spectrum.  The modulo-three obstruction is additional ansatz-specific structure,
not a second proof excluding every larger modulus.

## No-Go Discipline packet for the bounded negatives

- N1 — Alternative routes: tested full GF(2)/GF(3) elimination, explicit dual
  verification, exhaustive subgroup closure, an independently coded big-integer GF(2)
  solve, and the local six-corner census. Other point families and analytic identities
  remain open routes.
- N2 — Wall independence: the two walls are finite linear-algebra statements about the
  fixed matrix. They are independent of physical simplex selection, multi-cell gluing,
  boundary limits, dynamics, and continuum recovery, none of which is executed.
- N3 — Hidden walls: the negative wording was scanned for `any`, `all`, `must`,
  `impossible`, `cannot`, `universal`, and `no rule`. Every surviving negative names
  the fixed 2,736-point incidence ansatz.
- N4 — Residual matching: Cycle 731 contributes only its exact finite floor/ceiling
  literals and receipt. No physical interpretation or universal certificate claim is
  inherited.
- N5 — Execution certificate: per element, all 2,672 rows are checked; per site, only
  the one supplied 16-corner cell is checked; per mode, no field/spectral/momentum mode
  is executed; per block, the full incidence, all 98 subgroups, all 8,008 six-corner
  sets, and eleven witnesses are checked; lattice-wide, no multi-cell, arbitrary-L,
  thermodynamic, boundary-limit, or continuum operation is executed.
- N6 — Partial-closure paths: a different point family, a non-point incidence basis,
  an analytic parity identity, or a symmetry-preserving proof may exist. The theorem
  does not require closing those paths.
- N7 — Steelman: the strongest objection is that a failed fixed incidence system says
  nothing about all certificate languages. The note accepts that objection and narrows
  both negatives accordingly.
- N8 — Cross-cycle echo: earlier finite-cell notes used the same supplied-model boundary.
  Cycle 730 (`PHYSICAL_CELL_ADJACENCY_ENDPOINT_STRUCTURE_CYCLE730_NOTE_2026-08-04.md`)
  is lineage context only; Cycle 732 consumes neither its support partitions nor its
  zero-slack theorem. Cycle 731 is the sole direct scientific predecessor because its
  bound certificates are imported exactly.

No-Go status for the two fixed-ansatz negatives: PASS.

## Hostile tests and claim boundary

The primary and independent artifacts reject a toggled parity point, a changed
modulo-three dual coefficient, a tightened bound constant, and a damaged dissection.
The independent checker also reconstructs the full finite action and subgroup lattice.

What is proved:

- exact finite parity and spectrum for the supplied one-cell, one-tick,
  normalized-volume-one corner-simplex model;
- exact invariance and modulo-three obstruction statements only for the fixed
  2,736-point incidence ansatz;
- eleven explicit attaining dissections.

What is not proved:

- that the framework selects this cell, allowed-piece class, charge, or dissection;
- that the supplied tick coordinate is a physical tick realization;
- uniqueness or classification of dissections or parity certificates;
- absence of another modulo-three or more symmetric certificate construction;
- any multi-cell, arbitrary-domain, arbitrary-L, boundary, thermodynamic, continuum,
  gravity, Record, or Born-rule statement.

## Artifacts

- Primary runner:
  `scripts/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04.py`
- Independent checker:
  `scripts/physical_parity_certificate_cost_spectrum_cycle732_independent_check_2026_08_04.py`
- Primary cache:
  `logs/runner-cache/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04.txt`
- Independent cache:
  `logs/runner-cache/physical_parity_certificate_cost_spectrum_cycle732_independent_check_2026_08_04.txt`
- Generated receipt:
  `outputs/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04_receipt_2026-08-04.json`

## Review-loop repair record

On 2026-08-12 the review loop independently re-derived the theorem, found the parity and
spectrum sound, and required claim repair before landing.  The repair demoted the model
to supplied finite data; made Cycle 731 a direct input-bound dependency; narrowed the
symmetry and modulo-three negatives to the fixed ansatz; removed the geometric
triple-cover and universal-certificate rhetoric; added an independent exact checker,
hostile controls, generated receipt, canonical caches, fail-closed exits, and this
N1-N8/N5 packet.  This record is source-review provenance, not an audit verdict.
