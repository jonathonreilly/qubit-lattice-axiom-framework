# A finite one-cell dissection cost is an exact off-support count

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No axiom or
primitive is proposed or adopted. Cycle 731 of the emergent-geometry lane.

Primary runner:
[`scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py`](../scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py)
(45 PASS / 0 FAIL, fail-closed), with canonical cache
[`logs/runner-cache/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.txt`](../logs/runner-cache/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.txt)
and receipt
[`outputs/physical_cost_identity_indicator_certificate_cycle731_2026_08_04_receipt_2026-08-04.json`](../outputs/physical_cost_identity_indicator_certificate_cycle731_2026_08_04_receipt_2026-08-04.json).

Independent checker:
[`scripts/physical_cost_identity_indicator_certificate_cycle731_independent_check_2026_08_04.py`](../scripts/physical_cost_identity_indicator_certificate_cycle731_independent_check_2026_08_04.py)
(15 PASS / 0 FAIL, fail-closed), with canonical cache
[`logs/runner-cache/physical_cost_identity_indicator_certificate_cycle731_independent_check_2026_08_04.txt`](../logs/runner-cache/physical_cost_identity_indicator_certificate_cycle731_independent_check_2026_08_04.txt)
and receipt
[`outputs/physical_cost_identity_indicator_certificate_cycle731_independent_check_2026_08_04_receipt_2026-08-04.json`](../outputs/physical_cost_identity_indicator_certificate_cycle731_independent_check_2026_08_04_receipt_2026-08-04.json).

## Supplied model and premise boundary

Every result below is a theorem of a **supplied finite structural model**, not
of the framework axioms alone. The model chooses the unit four-cube, its
five-corner normalized-volume-one simplex pieces, exact interior-disjoint
24-piece dissections, and an all-pairs spatial-adjacency charge.

- The **Lattice** axiom in
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  spatial `Z^3` nearest-neighbour adjacency and the 24 proper cubic rotations.
- The registered
  [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies only equal tick/edge graining. It does not select cells or supply a
  rule-to-tick correspondence.
- The simplex class, dissection rule, all-pairs charge, and interpretation of
  the fourth coordinate as a physical tick are declared inputs. The physical
  tick–Admissibility bridge and physical assembly-cell–simplex bridge remain
  open.

The landed
[`PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md`](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md)
is prior authority for this supplied one-cell model and its exact cost bracket
`[108,128]`. The present runners reconstruct that bracket's certificate surfaces
locally before using them. Cycles 726–730 are chronological context only: no
source, witness, certificate, or theorem from them is consumed here.

The exact indicator identity is a finite combinatorial analogue of local defect
accounting. It is **not** a derivation of physical Admissibility or a physical
defect density: model pieces are not framework sites, and certificate-support
membership is not shown to be physical availability.

## What this settles

For every exact 24-piece dissection in the declared minimal-piece class, the
spatial adjacency cost obeys

```text
cost(dissection) = 108 + number of its pieces outside one fixed support.
```

The fixed support contains 1,792 of the 2,672 minimal pieces and is invariant
under the carried order-48 action. It consists of 38 of the 57 piece orbits.
The result is an identity for every dissection in the declared class, not just
the four exhibited dissections.

This follows from an exact floor certificate at denominator 216 and constant
756. Its value is `23,328 = 108 * 216`, while every individual piece has slack
either 0 or 216. Generic sample points lie on no piece boundary, so the
certificate rows sum to the fixed point census over any exact dissection. The
sum of the individual slacks is therefore `216 * (cost - 108)`, and the binary
slack spectrum converts that sum into an off-support count.

The exact ceiling 128 then gives a membership corollary: every declared-class
dissection contains at least four support pieces, and any cost-128 dissection
contains exactly four. This uses the exact Cycle-725 ceiling, reconstructed here;
it does not extend to coarser or different piece classes.

The support is also the union of pieces that occur in cost-108 dissections.
Zero total slack forces every piece of a cost-108 dissection into the support.
Conversely, the runners force a representative from each of the 38 support
orbits, construct a cost-108 completion within the support, and verify all 38
completions by exact point cover and pairwise integer separation. The carried
action transports the representative result to every piece in its orbit. Six
stored completions, seeded at orbits `12,13,45,50,53,56`, cover all 38 orbits;
none of the 501,942 five-subsets of these **38 stored completions** does. This
last finite statement is not a minimum over every possible cost-108 dissection.

## Finite objects and exact evidence

The unit four-cube has 16 corners and 4,368 five-corner subsets. Exact determinant
expansion gives normalized-volume spectrum
`0:1360, 1:2672, 2:320, 3:16`. The declared class retains the 2,672 volume-one
pieces, so every dissection in that class has 24 pieces. Coarser pieces are
excluded by the declared class; their existence is not denied.

A piece's charge counts its corner pairs whose spatial `L1` separation exceeds
one. Its exact spectrum is `3:64, 4:384, 5:1152, 6:768, 7:304`. The carried
action is the 24 proper spatial cubic rotations times tick reversal. It has
order 48 and partitions the pieces into 57 orbits of sizes 16 and 48. It is a
declared carried action, not a claim about the full symmetry of a four-cube.

The sample construction uses superincreasing barycentric weights. The measured
barycentric integer bound is 3, the common denominator is 12,810, and the orbit
construction yields 2,736 distinct points with zero piece-boundary incidences.
The runner uses no optimisation solver. Certificates are literal integers and
all completions are deterministic exact-cover searches whose terminal condition
also checks the genuine dissection predicate.

Four headline dissections have `(cost, off-support)` pairs
`(108,0), (114,6), (108,0), (128,20)`. They are checks on concrete examples;
the universal identity follows from the certificate summation above.

## Exact ceiling asymmetry in the fixed certificate family

The same generic-incidence matrix carries a zero-gap ceiling certificate at
denominator 3 and value 384, with slack spectrum `0,2,3,4`. Five orbit rows obey

```text
3 M[3] + M[17] - M[1] - M[15] - 2 M[27] = 0.
```

The coefficient sum is zero and the corresponding charge combination is `-2`.
For every integer-weight, integer-constant, positive-integer-denominator ceiling
certificate in this **fixed incidence family**, the slacks therefore obey

```text
3 s[3] + s[17] - s[1] - s[15] - 2 s[27] = 2 D.
```

Orbits 17, 1, 15 and 27 each have an exact cost-128 completion and hence must be
tight in any zero-gap ceiling certificate in this family. Thus `3 s[3] = 2D`.
It follows that 3 divides every positive integer denominator; the exhibited
denominator 3 is least. A binary indicator would require `s[3]/D` to be 0 or 1,
but `3x=2` has no binary solution. Accordingly, no zero-gap ceiling certificate
in this fixed generic-incidence integer family has slack only in `{0,D}`.

This does not exclude an indicator in another point family, a non-incidence
certificate formalism, a different piece class, or another domain.

The full 57 orbit rows have exact rank 13; adjoining the constant column does
not increase the rank. Up to sign and positive scale there are 49 primitive row
classes. A complete sweep of all `C(49,5)=1,906,884` five-class supports finds
185 minimal dependencies: charge combinations `-2:22, 0:136, 2:26, 4:1`.
These are finite properties of this reconstructed matrix.

## Local-invariant sweep

Charge alone decides 752 pieces: charges 3 and 4 are inside the support, while
charge 7 is outside. The 1,920 pieces of charges 5 and 6 split. None of the six
declared scalar invariants—least spatial gap, largest spatial gap, number of
zero-gap pairs, number of body-diagonal pairs, tick-difference count, and orbit
size—separates the 38 support orbits from the other 19. This is an exhaustive
statement about those six named invariants on these 57 orbits only, not about
all local descriptions.

## Independent reconstruction and hostile controls

The independent checker imports and executes no primary implementation. It reads
only the sparse certificate literals from the primary's AST, then separately
rebuilds exact determinants, the charge census, coordinate action, piece orbits,
sample chamber, incidence matrix, certificate slacks, row ranks, all 38 floor
completions, and all four ceiling-tight completions. Its 15 gates independently
confirm the indicator identity and fixed-family ceiling exclusion.

Hostile controls raise the floor constant through a tight row, alter the exact
five-row dependency, duplicate a simplex in a dissection, and move an entire
orbit across the support. Each mutation is detected. The primary separately
checks all 116 one-step floor-certificate moves and all 10 single-coefficient
relation changes. A review mutation of the expected floor value also makes the
primary exit nonzero, exercising its fail-closed contract.

## Boundary and honest read

- The theorem is only for normalized-volume-one corner simplices in one supplied
  cell. Coarser, non-corner, nonsimplicial, multi-cell, repeated-tick, boundary,
  thermodynamic, and continuum cases are open.
- The 216 denominator is a carrier, not a minimum claim. The denominator-3
  minimum applies only to positive integer denominators in the fixed ceiling
  incidence family.
- “No ceiling indicator” is restricted to that family. Other sample points or
  proof formalisms remain live routes.
- “No separating invariant” is restricted to the six declared scalars. A
  seventh or composite invariant may separate the support.
- The 38 completions establish support reachability only after exact separator
  checks. Sample-point cover alone would not have sufficed.
- The six-versus-five statement concerns the stored one-per-orbit completions,
  not every possible collection of cost-108 dissections.
- No physical tick, physical assembly-cell, framework Admissibility, arbitrary
  domain, regularity, face-to-face, or physical defect-density claim is made.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — spatial nearest-neighbour
  adjacency and proper cubic rotations only.
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) —
  equal tick/edge graining only.
- [Cycle 725 exact one-cell bracket](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md) —
  prior authority for the supplied model and `[108,128]`; reconstructed locally.

## Proof-obligation disposition

CONDITIONAL. The indicator identity, support reachability, fixed-family ceiling
exclusion, and six-invariant census are exact finite results on the supplied
model. Any physical reading is conditional on the two open bridges above.

## Review record

The submitted branch passed its own 45 gates, but review found material premise
and evidence defects: it promoted the finite support count to physical
Admissibility/defect density; said coarser pieces could not be substituted rather
than declaring their exclusion; its exact-cover search did not require pairwise
separation at the terminal state; it lacked fail-closed exit, canonical caches,
and an independent checker; and its negative conclusions lacked a complete
No-Go Discipline packet. The repair narrows the model, makes every completion a
genuine dissection, adds an independently implemented 15-gate reconstruction,
generates receipts, fails closed, and records the exact negative scopes. No audit
verdict is authored or applied.

## No-Go Discipline Gate

This N1–N8 record covers two retained finite exclusions: (A) no binary zero-gap
ceiling indicator exists in the fixed generic-incidence integer certificate
family; and (B) none of six named scalar invariants separates the support on the
57 carried orbits. No universal `no_go` claim ships. The primary cache contains
the required five-line N5 resolution certificate.

**N1 — Alternative route enumeration.** Each route is marked `ATTEMPTED` and
executed in the landed runners.

1. `ATTEMPTED` — exact row-algebra route: reconstruct the five rows and verify
   the dependency at residual zero with charge combination `-2`.
2. `ATTEMPTED` — primal-tightness route: independently construct genuine
   cost-128 dissections through the four required tight orbits.
3. `ATTEMPTED` — binary Diophantine route: reduce the residual to `3x=2` and
   exhaust `x in {0,1}`.
4. `ATTEMPTED` — positive-denominator route: derive `3 | D`, exhibit `D=3`,
   and show rescaling cannot turn `2D/3` into either 0 or `D`.
5. `ATTEMPTED` — independent reconstruction route: rebuild all incidence rows,
   ranks, slacks, and completions without importing primary implementation.
6. `ATTEMPTED` — exhaustive dependency-population route: sweep all 1,906,884
   five-class supports and re-multiply every reported dependency.
7. `ATTEMPTED` — local-invariant route: enumerate all values of the six named
   scalars on all 57 orbits and test support/outside value-set intersection.
8. `ATTEMPTED` — hostile mutation route: perturb a dependency coefficient,
   floor constant, dissection, and support orbit; all fail their target gates.

**N2 — Wall-independence audit.** The six open walls are PF (other point or
certificate families), LI (additional/composite local invariants), TR (physical
tick–Admissibility), SI (physical assembly-cell–simplex identification), PC
(other/coarser piece classes), and DE (other domains or limits).

| pair | first→second | second→first | independent? | reason |
|---|---|---|---|---|
| PF–LI | no | no | yes | changing a certificate family does not classify local scalars, and a new scalar does not supply a ceiling certificate |
| PF–TR | no | no | yes | finite dual algebra and physical rule-to-tick realization are distinct |
| PF–SI | no | no | yes | another point chamber neither identifies a physical cell nor follows from one |
| PF–PC | no | no | yes | a certificate formalism does not choose the piece class |
| PF–DE | no | no | yes | another certificate on one cell does not establish arbitrary domains |
| LI–TR | no | no | yes | support descriptors and physical tick realization are separate |
| LI–SI | no | no | yes | a separating scalar would not identify framework cells |
| LI–PC | no | no | yes | new invariants neither select nor follow from a new piece class |
| LI–DE | no | no | yes | separation on 57 orbits does not extend the domain |
| TR–SI | no | no | yes | rule-to-tick and cell-shape identification are distinct bridges |
| TR–PC | no | no | yes | a physical tick bridge does not select simplex pieces |
| TR–DE | no | no | yes | one physical correspondence does not prove arbitrary-domain combinatorics |
| SI–PC | no | no | yes | identifying a cell does not force its dissection class |
| SI–DE | no | no | yes | one-cell identification does not imply repeated-domain results |
| PC–DE | no | no | yes | closing another piece class on one cell does not close larger domains |

No wall automatically closes another; the collapsed set remains six.

**N3 — Hidden-wall scan.** The coordinate cell, volume normalization, minimal
piece restriction, dissection predicate, all-pairs charge, carried action,
generic point chamber, integer certificate family, and six scalar invariants are
all explicit. “By construction” for point genericity is backed by the measured
barycentric bound and zero boundary incidences. “Local” is restricted to
piece-orbit membership; it is not framework locality. No canonical, natural,
obvious, or standard-physics premise is smuggled into the finite conclusion.

**N4 — Residual matching.** The fixed-family exclusion matches the exact
residual `3s[3]=2D`, after four orbit slacks are forced to zero by exact primal
witnesses. The local-invariant exclusion matches a complete intersection test
for six named arrays on all 57 orbits. Neither residual speaks about another
point family, invariant language, physical cell, piece class, or domain.

**N5 — Rhetoric audit.** The primary cached stdout records: `per_element` for all
2,672 supplied pieces; `per_site` for one supplied coordinate cell only;
`per_mode` not executed because the model has no mode decomposition; `per_block`
for all completions and finite row-support censuses; and `lattice_wide` not
executed, with no lattice-wide negative asserted.

**N6 — Partial-closure path scan.** PF can close by constructing an indicator in
another chamber or proving an equivalence theorem across chambers. LI can close
by proposing and exhaustively testing more scalars or composites. TR and SI may
be imported by a later bounded theorem and retired only by theorem/audit. PC and
DE close by rebuilding the finite argument on the named class or domain. No new
axiom is declared necessary.

**N7 — Steelman.** A different generic point family or non-incidence dual may
carry a ceiling indicator, and a seventh or composite invariant may separate the
support. Those are concrete live routes. They do not refute the exact
fixed-family equation or the complete census of the six declared arrays.

**N8 — Cross-cycle echo.** Cycle 725 required this lane to distinguish the
supplied corner-simplex model from physical assembly and to price exclusions to
the retained finite certificate family. Cycle 728 repeated the warning that a
sample-point cover is not by itself a physical or regular dissection. This
repair carries both lessons forward: the terminal search now checks pairwise
separation, and every negative is restricted to its exact family and resolution.

**Status: PASS.** All eight checks are answered; all eight N1 routes are
`ATTEMPTED`; the complete N2 pair table lands; the N5 resolution lines land in
canonical primary stdout; and no universal negative is retained.
