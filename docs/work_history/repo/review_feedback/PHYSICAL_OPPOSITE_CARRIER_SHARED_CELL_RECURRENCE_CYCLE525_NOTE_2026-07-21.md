# Physical opposite-carrier shared-cell recurrence — Cycle 525 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_opposite_carrier_shared_cell_recurrence_cycle525_2026_07_21.py`.

## Result

Cycle 525 closes the smallest stated `W_recur` discriminator for the
Cycle-522 opposite-carrier grammar.  Three selected M64 cells are multiplied
as actual Pauli representatives on one shared Cycle-269 patch, in both a
straight chain and a bent path.  The shared middle cell occurs once.  No pairwise
tensor surrogate is used.

The joint selected physical encoder covers total three-cell number
`n=0,...,3`, hence

```text
dimension = 1 + 18 + 153 + 816 = 988.
```

This widens the recurrent test beyond `n<=2` and exercises both opposite-
carrier `n=3` orbits.  At training L5 and held L6, every one of the six actual
cell-factor orders has 8,272 physical rays and 8,288 nonzero amplitudes.  Each
order and the joint S3 relation are isometric.  The result is a bounded
two-seam **algebraic recurrence**, not a primitive or autonomous volume law.

The feasible three-incident-seam extension was also executed.  Four selected
cells on the Cycle-324 degree-three star cover total `n<=2`, dimension 301.
All 24 actual factor orders have 4,816 physical rays and 4,816 nonzeros at L5
and held L6.  Their joint S4 encoder, all six stream orders, three-slot
comparator, physical intertwiner, mass fixture, and all 24 frames pass.  Thus
Cycle 525 closes both the smallest two-seam terminal through `n=3` and the
first selected-grammar degree-three terminal through `n=2`.

The physical update is rebuilt on the selected joint code.  No new comparison
to the inherited Cycle-311 physical coin is made: Cycle 522 already measured
that coin's local selected-code leakage, while Cycle 525 executes only the
rebuilt code-space completion.

## Exact target contract

| item | declared Cycle-525 target |
|---|---|
| physical object | three addressed M64 cells sharing one middle cell |
| geometries | straight two-edge chain and right-angle two-edge path |
| sizes | periodic L5 train and L6 held |
| state domain | arbitrary amplitudes in all 988 total-`n<=3` columns |
| update | one three-cell coin, two incident FSWAPs, one onsite contact |
| covariance | all 24 proper-cubic frames and the path/corner arm exchange |
| completion witness | exact Gram plus `E G = G_physical E`, leakage, inverse, roles, mass, and deletions |
| excluded outcomes | a tensor-assumed pair code, host-selected carrier, global parity service, or interpretation of schedule as time |

The secondary degree-three target uses four addressed star cells, all 301
total-`n<=2` columns, a joint 24-state S4 role, and three incident FSWAPs.

The cutoff, cells, geometry, reference, role preparation, coefficients,
factor order, coupling, boundary, and tolerance are explicit.

## Joint physical encoder

For each local odd label `S`, Cycle 522 retains

\[
D(S)=\{d\notin S:(d\mathbin{\mathsf{xor}}1)\in S\},\qquad
a'_d=a_d\sqrt{\frac{6-|S|}{|D(S)|}}.
\]

The inherited cell flag-plus-companion constraint supplies two equal gauge
terms for each selected carrier.  For a triple of local labels, the runner
forms every product of those terms and multiplies the representatives in all
six orders

```text
ABC, ACB, BAC, BCA, CAB, CBA.
```

One shared stabilizer-ray reducer receives these actual products.  In
particular, the two seam encoders do not receive separate copies of cell B.
For both geometries and both sizes the exact census is:

| item | result |
|---|---:|
| logical columns | 988 |
| physical rays per order | 8,272 |
| nonzeros per order | 8,288 |
| six-order nonzeros | 49,728 |
| rows in the flagged joint encoder | 49,632 |
| maximum raw Gram entry | below `8e-16` per order |
| processed order/joint Gram residual | 0 |
| minimum joint Gram eigenvalue | within `1e-14` of 1 |

Adjacent physical orders remain distinct: both `ABC-BAC` and `ABC-ACB`
have operator residual approximately 2.  Selecting one silently is therefore
not the relational compiler.

## Locally enforced cell and multi-edge roles

Every selected local carrier has its equal-amplitude `f/r` partner.  Across
the complete local M64 inventory on all three cells, the runner finds zero
pairing failures, zero port-constraint commutator failures, and zero
fixed-sector commutator failures at L5 and L6.

Two independent Cycle-315 edge companions still fail on the exact 24-state
role shell:

```text
independent constraint commutator = sqrt(3)
independent braid residual        = 2
common rank factor                = 2
```

This is the same narrow role-algebra counterexample as Cycle 319, not a
failure of the opposite-carrier code.  The endpoint exchanges obey the S3
braid exactly.  The local repair uses the six-state order register in three
M2 and

\[
J_{S3}=2|s\rangle\langle s|-I_6,
\qquad |s\rangle=6^{-1/2}\sum_{\pi\in S_3}|\pi\rangle.
\]

Its plus sector has rank 988.  The constraint is an involution, commutes with
both adjacent exchanges, fixes the actual joint selected encoder, and
commutes with the rebuilt physical update within numerical tolerance.  Its
dense coefficients and two unused-state exclusions remain supplied local
rules.

## Two-seam update and the intertwining equation

For each geometry, Cycle 525 uses

\[
U_{12}=D_3S_2S_1\Gamma(C\oplus C\oplus C),\qquad
U_{21}=D_3S_1S_2\Gamma(C\oplus C\oplus C),
\]

where `C` is the Cycle-219 `beta=-0.3` coin and

\[
D_3=\exp\!\left(ig\sum_{j=A,B,C}\binom{n_j}{2}\right),
\qquad g=0.37.
\]

The middle-cell port modes addressed by the two FSWAPs are distinct.  Both
stream orders are unitary, their commutator is zero, and
`U_12-U_21=0` on this declared patch.  This is a property of the executed
port lists, not an arbitrary collision theorem.

For each physical order block `E_pi`, the executed completion is

\[
G_{\rm physical,\pi}
=E_\pi G E_\pi^\dagger+I-E_\pi E_\pi^\dagger.
\]

On their S3-correlated direct sum, the certificate gives processed zero for

\[
E G-G_{\rm physical}E
\]

and for the directly evaluated terminal code leakage.  Randomized ambient forward/inverse
tests and physical joint-constraint commutators are below the declared
tolerance at L5 and held L6.  The off-code identity action and the dense
matrix-unit application are supplied.

The logical coin has 94,342 active coefficients, each FSWAP has 988 signed
entries, and contact is nontrivial on 645 columns.  Every sector
`n=0,1,2,3` has the expected dimensions and unitary update.

The uniform one-particle result is

```text
Cycle-219 mass fixture   0.4534056541748851
three-cell recurrence   0.4534056541748851
eigenvector residual    3.534751832054436e-16
```

The wrapped contact phase is not called physical energy, a matrix element is
not called a rate, and the supplied schedule is not physical time.

## Proper-cubic covariance and staggered comparator

At L5 and L6 the complete selected local physical encoder, rebuilt coin,
stream, and contact pass all 24 proper-cubic frames.  The carrier selector
has zero frame failures.  On both the chain and bent path, the three-cell
exterior representation maps the two-seam update to the rotated update;
all 576 frame products close, and arm exchange maps `U_12` to `U_21`.

The bounded staggered comparator retains one active edge role and a local
slot M2.  Its slot operator, square, arm-exchange covariance, active-role
transport, and two-slot macro unitarity pass exactly, with zero host branch
queries.  The slot initialization, fixed edge cycle, and matrix rule remain a
supplied schedule.  No physical phase controller or autonomous edge-choice
law is claimed.

## Three incident seams

The four-cell star repeats the physical construction rather than inferring it
from the native Cycle-324 result.  For every logical column the runner
multiplies the selected cell-role terms in all 24 orders on one shared
physical patch.  At L5 and held L6:

| item | selected star result |
|---|---:|
| logical columns through total `n=2` | 301 |
| physical rays per order | 4,816 |
| nonzeros per order | 4,816 |
| 24-order nonzeros | 115,584 |
| processed order/joint-S4 Gram residual | 0 |
| joint physical encoder rows/nonzeros | 115,584 / 115,584 |
| joint S4 register | 5 M2 |

The three overlapping S3 subgroup checks share the uniform role vector but
do not form a commuting, order-independent stabilizer family: their maximum
constraint commutator is `1.2570787221094177`.  The joint S4 constraint has
rank 301, is an involution, commutes with all three adjacent exchanges, and
satisfies both adjacent braid relations and the far commutator exactly.

The three FSWAPs address three distinct center-cell modes.  All pairwise
stream commutators and all six ordered-update differences vanish on the
declared star.  Every update is unitary, preserves the joint S4 code, passes
the rebuilt physical `E G = G_physical E` and leakage/inverse controls, and
retains mass `0.45340565417488515`.  The three-state slot cycle also passes
its cube, constraint-transport, and all-frame tests with zero host queries.
This is one bounded star, not a policy for overlapping stars.

## Support, leakage, deletion, and lawful domain

The physical face/port/cell-role union is 118 M2; the inherited joint S3
register raises the bounded patch to 121 M2.  The maximum actual selected
branch uses 42 M2 before that register and 45 after it.  These are observed
upper counts, not minima, and the opposite selector adds no new M2 relative
to the Cycle-319 role inventory.

On the degree-three star the face/port/cell-role union is 155 M2.  The joint
S4 register raises it to 160 M2, and the maximum selected branch support is
32 M2 including that register.  Deleting one of its 24 role amplitudes gives
Gram residual `1/24`.

Independent destructive controls give:

- deleting one of six joint-order amplitudes gives exact Gram residual `1/6`;
- deleting the middle cell's `r=1` partner without renormalization gives
  exact Gram residual `1/2` in all six physical orders;
- deleting one FSWAP column gives unitarity residual 1; and
- deleting the first seam from the declared target gives operator residual
  greater than 1.

The lawful domain rejects total number above three for the three-cell code,
above two for the four-cell star, undeclared geometry, L4 in this Cycle-525
contract, malformed occupation labels, and determinant-minus-one frames.
L4's exclusion is a domain boundary, not evidence of a universal obstruction.

The runner has a 600-second wall, 3 GB RSS guard, and zero-swap checkpoints.
These are execution controls rather than physics premises.
The final cold certificate completed in `153.60115070804022` seconds with
maximum resident memory `790298624` bytes, zero process swap, and summary
`PASS=14 FAIL=0`.

## Supplied structure and novelty boundary

Supplied or inherited are:

1. the fixed-Wilson reference, face/port dictionary, and preparation;
2. the Cycle-311 cell flag, companion, local constraint, and preparation;
3. the Cycle-522 opposite-carrier selector and normalization;
4. three addressed cells and the path/corner geometry;
5. the global `n<=3` cutoff;
6. the six-state S3 role register in three M2, its preparation, dense
   constraint, and unused-state exclusions;
7. the 24-state S4 role in five M2, its preparation, dense constraint, and
   eight unused-state exclusions;
8. the Cycle-219 coin, Cycle-230 coupling/contact, FSWAPs, and their
   application order;
9. the rebuilt dense code-space coefficients and off-code identity
   completion;
10. the active-edge roles, local slots, slot rules, and initialization used by
   the staggered comparator; and
11. L5/L6 boundaries, logical input preparation, and the supplied schedule.

Derived are the actual shared-middle selected S3 and S4 order maps, exact
Gram, joint-role codes, all two- and three-seam stream orders, the code-space
intertwiners, inverse/leakage controls, all-frame covariance, mass/contact
fixtures, and the stated deletions.

Regular representations, exterior-power coins, fermionic swaps, local gauge
codes, dense isometric extensions, and group averaging are prior-art
territory.  Cycle 525 claims only the opposite-carrier re-execution on this
bounded joint physical patch and its exact residuals.  It does not claim
uniqueness, minimality, primitive synthesis, autonomous recurrence, or global
novelty priority.  Thirring machinery is neither used nor compared.

Still open are three-cell sectors `n=4,...,18`, four-cell sectors
`n=3,...,24`, overlap of several joint role registers, recurrent volume
coverage, primitive synthesis, reference/role preparation, autonomous
collision control, causal time, Records, Born probability, source/stress,
gravity, and continuum limits.

## Full current no-go discipline

The current `origin/main` no-go procedure and proof-search normalization were
read after a freshness fetch.  The narrow negative retained here concerns
only two literal independent Z2 companions on the tested 24-state role shell.
The successful actual joint S3 encoder and staggered comparator block any
broad multi-edge, substrate, minimum-content, or axiom-pressure claim.

### N1 — alternative-route enumeration

| normalized route | honesty | disposition |
|---|---|---|
| selected three-cell code plus one joint S3 order role | **ATTEMPTED** | succeeds on actual chain/corner products through `n=3`, both sizes, both seam orders, and all frames |
| selected code plus two independent Z2 edge companions | **ATTEMPTED** | exact role-shell commutator `sqrt(3)` and common rank factor two; route-specific failure |
| one active edge role plus staggered local slot | **ATTEMPTED** | bounded algebraic slot identities and covariance succeed; autonomous initialization remains open |
| one fixed physical cell-factor order | **ATTEMPTED** | each order is isometric, but neighboring orders differ by operator norm about 2 and selection is extra structure |
| straight-chain physical formulation | **ATTEMPTED** | actual shared-middle encoder and update succeed at L5/L6 |
| bent-path physical formulation | **ATTEMPTED** | actual shared-middle encoder and update succeed at L5/L6 |
| selected four-cell joint S4 / three-slot route | **ATTEMPTED** | succeeds on one actual degree-three star through `n=2`, L5/L6, all six stream orders, and all frames |
| overlapping joint registers or a larger local symmetric-group role | **OPEN / UNTESTED** | could extend incidence without selecting independent patch orders |
| full three-/four-cell Fock widening | **OPEN / UNTESTED** | must construct three-cell `n=4,...,18` and star `n=3,...,24` with resource controls |

The positive routes and open route families make the broad negative gate
**FAIL / DO NOT SHIP**.

### N2 — wall-independence audit

The collapsed remaining set is `W_number`, `W_incidence`, `W_primitive`,
`W_prepare`, `W_autonomy`, and `W_prediction`.

| first | second | first closes second? | second closes first? | independent? |
|---|---|---:|---:|---:|
| W_number | W_incidence | no | no | yes |
| W_number | W_primitive | no | no | yes |
| W_number | W_prepare | no | no | yes |
| W_number | W_autonomy | no | no | yes |
| W_number | W_prediction | no | no | yes |
| W_incidence | W_primitive | no | no | yes |
| W_incidence | W_prepare | no | no | yes |
| W_incidence | W_autonomy | no | no | yes |
| W_incidence | W_prediction | no | no | yes |
| W_primitive | W_prepare | no | no | yes |
| W_primitive | W_autonomy | no | no | yes |
| W_primitive | W_prediction | no | no | yes |
| W_prepare | W_autonomy | no | no | yes |
| W_prepare | W_prediction | no | no | yes |
| W_autonomy | W_prediction | no | no | yes |

They concern number widening; adjacent-star/higher-degree incidence;
primitive gate synthesis; reference and role preparation; a physical
collision controller; and the eventual time/Record/Born/source prediction
bridge.  The inherited-coin failure is not a seventh wall because Cycle 522
already bypasses that candidate with the rebuilt update.

### N3 — hidden-condition scan

The selector, normalization, fixed reference, cell addresses, geometries,
number cutoffs, six S3 and 24 S4 factor orders, both role registers, unused states, dense
coefficients, off-code completion, coin, contact, coupling, FSWAP ports,
input preparation, L5/L6 boundary, tolerance, and schedule are explicit.
The physical products are enumerated before reduction; no background branch
query chooses a carrier.  Primitive genesis, preparation, incidence,
autonomy, and prediction are named in N2 rather than concealed in generic
language.

### N4 — residual matching

| cited witness and executable location | witness residual | Cycle-525 use | match? |
|---|---|---|---:|
| Cycle 522 selector, `scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py:149` | selected odd carriers and exact normalization | each of the three local factors | yes |
| Cycle 522 rebuilt shell, same runner `:310` and `:820` | local/full-two-cell selected-code update | local frame and one-edge fixtures only | yes |
| Cycle 319 actual products, `scripts/physical_cycle269_three_cell_multiedge_cycle319_2026_07_18.py:345` | shared physical three-cell order maps | same terminal under changed carrier grammar | yes |
| Cycle 319 role algebra, same runner `:560` | independent-Z2 failure and joint-S3 repair | same complete 24-state role shell | yes |
| Cycle 319 update/covariance, same runner `:741` and `:848` | two incident FSWAPs, mass, frames, and slot | same logical terminal carried through selected physical E | yes |
| Cycle 324 physical star and update, `scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:364` and `:750` | 24 actual orders, joint S4, and three incident FSWAPs | same terminal re-executed under selected grammar | yes |

No time, Born, Record, source, or gravity residual is used as evidence about
recurrence.

### N5 — rhetoric and resolution audit

| resolution | tested here | exact disposition |
|---|---|---|
| one selected M64 cell | complete local M64 inherited and frame-retested | exact algebraic physical code |
| one selected edge | full two-cell Fock inherited from Cycle 522 | exact bounded seam, not recurrence alone |
| one three-cell/two-edge path | all total `n<=3`, L5/L6 | exact actual joint encoder and update |
| two independent edge companions | complete 24-state role shell | fail only as a simultaneous commuting gauge |
| one joint S3 role | complete six-order shell | exact rank-one role factor and physical intertwiner |
| one four-cell/three-edge star | all total `n<=2`, L5/L6 | exact 24-order joint S4 encoder and all six updates |
| overlapping S4 registers / recurrent volume | not tested | no compatibility or negative statement |
| infinite volume / continuum | not tested | no statement |

“Independent edge companions fail” is restricted to that finite role shell.
“Recurrence” means two or three incident seams on one declared bounded patch,
not an autonomous indefinitely renewed lattice process.

### N6 — partial-closure paths

Cycle 522 supplies the changed local code and rebuilt one-edge algebraic
update.  Cycle 525 directly closes its smallest shared-middle terminal with a
joint S3 role and the first degree-three terminal with a joint S4 role.  The
staggered slot and three-slot cycle close the same bounded stream products by
serialization.  Adjacent joint registers, a larger shared role, or a
transported slot are the next volume paths.  Full-number and primitive
decompositions are independent widenings.  None requires an axiom edit merely
to be attempted.

### N7 — hostile steelman

A hostile reviewer should reject any claim that Cycle 525 establishes an
autonomous recurrent matter law.  The successful physical operator is still
the dense completion `E U E^dagger + I - E E^dagger`; its coefficients and
application are supplied, the joint S3/S4 registers are prepared, and the
incident streams touch distinct addressed ports.  The actionable
counter-route is to overlap two of the now-successful selected S4 stars while
preserving every intermediate constraint and constructing a local phase
controller.  That terminal is untested here.  This steelman narrows the
positive theorem to bounded two- and three-seam patches and blocks any volume
or autonomy promotion; it does not undo the exact joint physical results.

### N8 — cross-cycle echo

| prior cycle | mechanism that retired a similar boundary | Cycle-525 lesson |
|---|---|---|
| 306/311 | cell flag plus companion retained lost relational order | preserve local role data before declaring collision |
| 315 | one Z2 edge role repaired endpoint order | match the gauge to the one-edge overlap algebra |
| 319 | joint S3 or staggered slot repaired two independent-edge failure | use a joint overlap group or serialize |
| 324 | joint S4 or three-slot cycle repaired three overlapping S3 checks | selected degree-three retest succeeds; adjacent-star overlap is next |
| 515/516 | correlated order roles carried all local factor orders and frames | retain exact order characters rather than select globally |
| 519/522 | changed representative grammar removed static collisions and re-earned dynamics | rebuild coefficients after changing the code |

Every echo supplies a constructive continuation.  No shared obstruction and
no axiom pressure follow.

Gate disposition: **PASS for the narrow independent-Z2 counterexample; FAIL /
DO NOT SHIP for a broad multi-edge, recurrence, minimum-content, or axiom-
pressure negative.**

## TOE dependency ledger

| wall | Cycle-525 movement | exact remaining obligation |
|---|---|---|
| `C_ref` | joint S3/S4 relations remove selected local cell-factor orders | derive reference, selector, and role preparation |
| `C_num` | three-cell recurrence reaches `n<=3`; the degree-three star reaches `n<=2` | three-cell `n=4,...,18`, star `n=3,...,24`, number change, and volume widening |
| `C_wrap` | fixed algebraic order and L5/L6 boundary remain explicit | autonomous recurrence, interval, and causal-time law |
| `C_int` | two seams through `n=3` and three incident seams through `n=2`, with every stream order, mass, and deletions | primitive synthesis, repeated arrivals, higher-degree collisions, recoil |
| `C_local` | actual chain/corner S3 and degree-three-star S4 encoders, all frames, held L6 | adjacent role-register compatibility and recurrent volume |
| `C_source` | unchanged | autonomous conserved source/response and prediction bridge |

Maturity remains conservative: operational quantum/Records `3.4/5`, causal
time `1.8/5`, inertia/matter `4.2/5`, gravity/source `2.1/5`, and Born/
probability `2.0/5`.  Only the bounded matter/local compiler evidence moves;
no Record, clock, occurrence, source, or probability theorem is added.

The optimal next campaign is two adjacent opposite-carrier degree-three stars
sharing cells: compare two S4 registers, one larger joint role, and a locally
transported slot while requiring constraint-preserving intermediate states at
L5/held L6.  Primitive decomposition of the rebuilt coin should run as an
independent comparator, not be inferred from this algebraic recurrence.
