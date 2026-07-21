# Physical local Wilson fill disk — Cycle 537 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py`.

## Result

Cycle 537 gives an explicit constructive topology answer to Cycle 532's
three-Wilson initialization wall.  Attach one auxiliary square **fill disk**
to each of the three axial Wilson loops.  Put M2 on the disk's interior edges,
one bounded `Z` check on every disk face, and one bounded `X` star on every
interior disk vertex.  The product of all face checks on one disk is exactly
the former Wilson initializer.  No growing Wilson initializer row is present
in the new stabilizer list.

The result is stronger than an abstract rank quotient.  The runner constructs
every local fill check, explicitly dresses every Cycle-532 local constraint,
matter generator, gauge generator, onsite pair, contact word, and B block,
and then recomputes the full matter commutant.  At L5 and held L6 the filled
code is exactly

```text
H_local-fill = H_target,full-Fock tensor H_gauge(N-1),
```

sectorwise across the shared matter/gauge parity center.  Both matter parities
remain nonempty.  The full-Fock `Gamma(P)`, Cycle-219 mass, Cycle-230 contact
and seam, inverse, and deletion comparators are preserved through this
faithful matter factor.

This is nevertheless a partial closure, not a completed encoding into the
existing physical substrate.  The three cap sheets are added topology.  The
runner constructs their intrinsic bounded local complex and an all 24 / 576
compile-time proper-cubic presentation orbit.  It does not embed those cap
sheets into Cycle 532's old period-32 three-dimensional periodic placement as
one fixed frame-independent triangulation, and it does not construct a
state-preparation/code-space-isometry circuit.  The note therefore does **not
call an abstract code quotient an encoding**.

Put tersely: this is **not an abstract code quotient presented as an
encoding**.

## Fill-disk construction

For one axial Wilson `W`, Cycle 537 partitions its physical Pauli support into
`L` bounded owner-cell chunks

```text
W = w_0 w_1 ... w_(L-1).
```

The chunks are disjoint within the axis, mutually commuting, and have support
at most nine M2 in the tested construction.  The root sign is fixed locally so
their Pauli product, including phase, is exactly the strict-pinned Wilson.

The auxiliary disk is an `L x L` square cell complex.  Boundary edges are not
new M2.  Its interior edges carry

```text
E_int = 2 L (L-1)
```

new M2.  There are `F=L^2` faces and `(L-1)^2` interior vertices.  Every
fourth boundary segment carries one `w_j`; the other boundary segments are
rough identity boundary.  A face check is its carried `w_j`, if any, times
`Z` on its incident interior edges.  An interior-star check is `X` on its four
incident edges.

The exact Euler count is

```text
F + V_int - E_int = L^2 + (L-1)^2 - 2L(L-1) = 1.
```

Thus each disk adds one more independent local check than physical M2 and
removes exactly one topological code qubit.  Three disks remove the three
Cycle-532 spin characters.  Interior edges cancel pairwise in the product of
all face checks, leaving exactly `W`.  Face/star commutators vanish because an
interior star meets a face in zero or two edges.

At the required sizes:

| quantity | L5 | held L6 |
|---|---:|---:|
| rough-code M2 | 2,750 | 4,752 |
| added fill M2 | 120 | 180 |
| total M2 | 2,870 | 4,932 |
| fill face/star checks per axis | 25 + 16 | 36 + 25 |
| stabilizer rank | 1,996 | 3,421 |
| code exponent | 874 | 1,511 |
| exact law | `7N-1` | `7N-1` |

The average M2 overhead is `6(L-1)/L^2` per coarse cell and is therefore
bounded.  Each fill face has support at most eleven M2 in the concrete table;
each interior star has weight four.  These are intrinsic cap-sheet
neighbourhoods, not long Wilson rows disguised as single gates.

## Local dressing of the physical algebra

Let a Cycle-532 Pauli `P` commute with all three Wilsons.  For one disk, mark
the boundary faces whose chunks anticommute with `P`.  The number of marked
faces is even because `[P,W]=0`.  The runner finds a minimum pairing and joins
each pair by a path in the disk dual grid.  Multiplying `P` by `X` on every
crossed interior edge cancels its face-check syndrome.  Call the result
`P_fill`.

All kernel differences between two path choices are products of the interior
`X` stars: the dual incidence kernel has dimension

```text
E_int - (F-1) = (L-1)^2,
```

exactly the number of displayed stars.  Path choice therefore changes only a
stabilizer representative, not the code action.  This is why the construction
may choose short local paths without corrupting algebra products.

The runner applies this procedure separately to:

- every bounded rough local stabilizer;
- all mapped matter parity/hopping generators;
- every explicit `Zg/Ag` gauge generator;
- all 15 onsite hoppings and 15 contact words; and
- every outer-edge B polynomial block.

It then checks all stabilizer, matter, and gauge commutators directly.  The
ancilla dress is `X`-only, so it does not alter any pairwise symplectic product
between dressed matter generators.  The held-size certificate also reports
the maximum added support and maximum dual-path length rather than assuming
locality from a drawing.

## Exact target-times-gauge certificate

For `N=L^3`, the filled stabilizer rank is

```text
rank(S_fill) = 15N + 1 + 3 E_int.
```

Since the physical exponent is `22N+3E_int`, the code exponent is `7N-1`,
the same as Cycle 532's explicitly fixed sector but with zero supplied Wilson
rows.  Adding any of the three old Wilson Paulis increases the filled
stabilizer rank by zero.

The exact quotient values recur at L5 and held L6:

| object | L5 dimension/rank | held L6 dimension/rank | law |
|---|---:|---:|---:|
| matter even algebra | `1499/1498` | `2591/2590` | `(12N-1)/(12N-2)` |
| explicit dressed gauge | `249/248` | `431/430` | `(2N-1)/(2N-2)` |
| full matter commutant | `249/248` | `431/430` | same as gauge |

The explicit gauge family exhausts the independently computed full
commutant.  Matter parity equals gauge parity on code.  Both signs of the
common center are consistent, and each fixed-parity exponent equals

```text
(6N-1) target + (N-1) gauge = 7N-2.
```

This proves the algebraic factorization.  It is not presented as a realized
state encoder because no preparation isometry is constructed.

## Full-Fock dynamics and fixtures

The filled matter representation has the same quotient dimension, radical,
and symplectic form as the Cycle-532 fixed matter factor.  Every dressed gauge
row commutes with it.  Therefore the same local matter polynomial gives each
target FSWAP and the three per-cell B blocks give `Gamma(P)` on every Fock
sector while acting as gauge identity.

The runner re-executes Cycle 532's strict-pinned target controls:

- complete full-Fock quadratic `Gamma(P)` theorem;
- complete L5/held-L6 low-sector censuses;
- two-cell 4,096-state and straight/corner three-cell controls;
- all onsite Givens and contact pairs;
- one-particle mass and the `g=0.37` contact/seam fixtures;
- FSWAP inverse, leakage, deletion, and phase perturbation.

The filled code's own dressed onsite/contact/B supports and commutators are
also enumerated.  No phase is called physical energy, no compiler count is
called a rate or causal time, and no puncture or gauge value is called a
Record.

## Cold certificate

The final independent cold invocation was

```text
python3 scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py \
  --mode fill-disk-certificate
```

and returned status
`cycle537-local-fill-disk-algebraic-partial-closure`, with all `10/10`
certificate groups passing.  The runner's internal resource envelope was
`156.56098329194356 s`, `137,707,520` maximum RSS bytes, and zero process
swaps.  The external `/usr/bin/time -l` envelope was `158.95 s` with the same
maximum RSS and zero swaps.

The exact recurrence and support controls were:

- L5/L6 stabilizer ranks `1996/3421` and code exponents `874/1511`;
- old-Wilson rank increments `(0,0,0)` at both sizes;
- matter dimension/rank `1499/1498` and `2591/2590`;
- gauge and full-commutant dimension/rank `249/248` and `431/430`;
- maximum added disk `X` support by local/matter/gauge family `9/4/4`, and
  maximum dual path length four, at both sizes;
- maximum dressed local/matter/gauge support `34/14/22`, fill face/star
  support `11/4`, onsite/contact/B support `7/16/17`; and
- zero matter-, gauge-, onsite-, contact-, B-, stabilizer-, covariance-,
  inverse-, and leakage-control failures.

The exact target controls returned `280875/839160` mode pairs and zero
quadratic coefficient failures, `281626/840457` complete low-sector tests,
4,096 two-cell states, and 988 states for each straight and corner three-cell
control.  The Cycle-219 mass residual was `2.220446049250313e-16`; the onsite
intertwiner/inverse/leakage residuals were
`5.272182555577386e-15`, `7.504184205291937e-15`, and zero.  The Cycle-230
contact deletion residual was `0.36789306705608243`; the seam singular values
were `[0.49577140670498115, 0.45566604871445016]`, with `6/0` seam
pass/fail subchecks.

Deletion controls returned full L3 fill rank `442`, fill-face-deleted and
fill-star-deleted ranks `441/441`, Wilson rank increment one after the face
deletion, and two face-syndrome violations after deleting one required
dressing `X`.  The deleted fourth FSWAP term retained residual one and the
phase-inconsistency counts were all zero.  The L5 and held-L6 signed-axis
presentation orbits both had zero all-24 frame failures and zero all-576
group-product failures.  These are compile-time retriangulated presentation
tests, not evidence for the still-missing single fixed physical cap
embedding.

## Proper-cubic presentation

The three disks are attached as an axial triple at one macro-origin.  A proper
cubic frame sends `(axis,j)` to

```text
(target_axis, sign * j mod L).
```

The runner checks all 24 signed-axis maps and all 576 products.  It also
re-executes Cycle 532's physical rough-code frame repair and 684,288 single
face `X/Z` group-law cases.  Every frame-specific cap is generated at compile
time; there is no runtime frame or sector query.

The retained covariance claim is deliberately narrow: this is a 24-member
compile-time **retriangulated cap presentation orbit**.  Cycle 537 does not
claim that one fixed square triangulation, embedded in the old period-32
three-torus, is invariant under every frame.  Closing that physical embedding
is a remaining obligation, not a cosmetic drawing task.

## Deletion, lawful domain, inverse, and leakage

- Deleting one independent fill-face check lowers rank by one and makes its
  axial Wilson independent again.
- Deleting one interior-star check lowers rank by one and re-admits one disk
  path-choice degree.
- Deleting one required dressing `X` produces a nonzero fill-face syndrome.
- Deleting the fourth FSWAP polynomial term retains Cycle 532's residual-one
  witness.
- Complete dressed matter and gauge rows have zero stabilizer leakage and zero
  gauge transition.
- FSWAP squares to identity and the full involutive B action retains its exact
  inverse.
- Off-code disk syndromes are explicitly outside the lawful filled code; no
  off-code physical interpretation is silently assigned.

## Alternative topology routes tested

The square disk was not selected without comparators:

| route | concrete result | disposition |
|---|---|---|
| cyclic relational spin field | `L` new M2 and `L` checks per axis, net exponent reduction zero | local and covariant, but replaces each Wilson character by one new logical |
| rooted open chain | `L-1` M2 and `L` checks, net rank correct | a linear algebra dressing crosses the root with support growing in L |
| fan disk | net rank correct and dihedral-covariant | central star has weight L (`5 -> 6` on train/held), so no uniform bounded-check theorem |
| square fill disk | face/star weights `<=11/4`, target factor exact | constructive algebraic partial closure; old-periodic embedding/preparation open |
| dynamic puncture sweep | moving defect could measure/fix twists with local gates | open; needs an autonomous reversible protocol, causal schedule, and inverse audit |
| open-cube/cut-sheet presentation | cut the three periodic planes and cap them at rough boundaries | open; must restore periodic target streams and one fixed cubic embedding |

The route failures are mechanism-specific.  They are not constitutional
evidence.

## Supplied structure and novelty boundary

Supplied rather than derived are:

- the strict-pinned Cycle-532 rough graph, matter/gauge Paulis, and target
  coefficients;
- three square cap-sheet cell complexes;
- one macro-origin and the three axial attachment loops;
- the frame-specific compile-time cap retriangulation;
- finite periodic L5 and L6 domains;
- Cycle-219 coin and Cycle-230 contact/factor order; and
- the abstract permission to add cap-sheet topology beyond the old period-32
  three-torus.

Not supplied are growing Wilson initializer rows, a runtime Wilson query, a
global parity callback, a site-major `A/AP` chart, or a runtime frame selector.
Also not supplied are an ordinary three-dimensional period-32 embedding of the
cap sheets or a local state-preparation/code-space-isometry circuit.

The new content is the explicit bounded fill complex, exact face-product
identity, dual-path dressing, L5/L6 target-times-gauge and full-commutant
certificate, local dynamics compatibility, deletions, and proper-cubic
presentation orbit.  This is a fixture-specific constructive topology result,
not a general bosonization theorem or a novelty-priority claim.  Thirring
machinery is not used.

## Dependency disposition

- `C_ref`: advances conditionally.  The three spin signs are no longer input
  values, but the cap topology, macro-origin, and compile-time triangulation
  are supplied.
- `C_num`: retained.  Both matter parities and the exact full-Fock factor
  survive.
- `C_wrap`: advances sharply.  Wilson signs become products of bounded local
  cap checks, but cap preparation/embedding remains open; no winding history,
  time, or energy is inferred.
- `C_int`: retained conditionally.  `Gamma(P)`, onsite Givens, mass, contact,
  seam, inverse, and leakage remain in the faithful matter factor.
- `C_local`: advances algebraically through bounded face/star constraints and
  local dressings.  It is not closed on the existing M2 substrate.
- `C_source`: unchanged.

Framework maturity scores are not raised by an imported-topology algebraic
presentation alone.

## N1–N8 no-go discipline

Broad no-go gate: **FAIL / DO NOT SHIP**.  The disposition is
`constructive-partial-closure-with-two-explicit-walls`.

### N1 — normalized alternative routes

| family | object / mechanism / terminal obligation | status |
|---|---|---|
| square fill disk | bounded-degree cap complex / Euler surplus plus dual-path dressing / physical embedding and preparation | **ATTEMPTED — algebraically positive** |
| cyclic relational field | one auxiliary cycle / local parity relations / remove rather than relocate three logicals | **ATTEMPTED — fails target rank** |
| rooted chain | open auxiliary chain / one-check Euler surplus / uniformly local algebra dressing across root | **ATTEMPTED — locality fails as tested** |
| fan cap | dihedral disk / center-star closure / uniform bounded check weight | **ATTEMPTED — held growth exposes missing theorem** |
| dynamic puncture | moving rough defect / coherent twist extraction and correction / autonomous reversible schedule | **OPEN — NOT CLOSED** |
| open cube/cut sheets | nonperiodic gauge topology / rough plane boundaries / recover periodic target streams covariantly | **OPEN — NOT CLOSED** |
| local measurement/dissipation | gauge-check outcomes or local bath / converge to filled sector / exact convergence and lawful-record audit | **OPEN — NOT CLOSED** |

These families differ in primary complex or dynamical object, load-bearing
mechanism, and terminal obligation.  The open routes block a broad negative.

### N2 — wall-independence audit

The collapsed remaining set has two walls:

```text
W_embed:
embed the cap-sheet incidence as bounded physical M2 neighbourhoods in one
fixed proper-cubic realization of the existing substrate.

W_prepare:
construct a local reversible or operationally lawful preparation/isometry for
the filled stabilizer code with branch/work leakage and inverse controls.
```

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `W_embed`, `W_prepare` | no | no | yes |

A geometric embedding alone does not prepare the code.  A preparation on the
abstract cap complex does not embed it in the existing substrate.  Wilson
selection, spin signs, and filled-code rank are closed by the local face
checks and are not separately counted.  Primitive optimization of one bounded
B block is downstream compiler work, not a third physics wall.

### N3 — hidden-wall scan

The required scan covers “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  No such phrase is
used to discharge a proof obligation.  The cap topology, rough boundary,
macro-origin, frame-specific retriangulation, finite domains, path pairing,
coefficients, missing old-periodic embedding, and missing preparation circuit
are explicit supplies or walls.  “Intrinsic local” refers to adjacency in the
new cap complex, not a hidden claim about old cubic distance.

### N4 — residual matching

| witness | witness residual | Cycle-537 use | match? |
|---|---|---|---:|
| Cycle 532 | three Wilson rows needed beyond bounded rough checks | face products put those exact three Paulis in the local filled span | yes |
| Cycle 269 | unfixed periodic Wilson characters twist one fixed target | exact matter quotient loses precisely those three characters | yes |
| Cycle 247 | rough code carries both parities but leaves `N-1` multiplicity | filled code retains both parities and Cycle-532 gauge factor | yes |
| Cycle 529 | exact full-Fock `Gamma(P)` target with nonlocal chart | target is replayed only as positive comparator | yes for target, not embedding |
| Cycle 533 | selected-seam code-space preparation on a different 95-M2 patch | not evidence about cap-sheet topology or preparation | no; dropped |

No route-specific chart, seam-tiling, or decoder residual is cited against the
fill construction.

### N5 — rhetoric audit

| resolution | tested statement |
|---|---|
| one fill face | bounded support; explicit Pauli |
| one interior star | weight four; exact face commutators |
| one Wilson disk | face product equals the exact Wilson |
| one local matter/gauge generator | explicit short dual-path dressing |
| one B edge/cell | bounded dressed polynomial support and exact target action |
| L5 and held L6 | full stabilizer, matter, gauge, and commutant ranks |
| all target Fock sectors | inherited quadratic theorem through faithful factor |
| all 24/576 | compile-time cap-presentation orbit |
| one old-periodic fixed embedding | not constructed |
| realized state preparation | not constructed |

Accordingly the retained negative language is only “not embedded/prepared in
this cycle.”  It is not widened to “cap topology cannot be physical” or “spin
structure cannot be locally generated.”

### N6 — partial-closure paths

Cycle 537 follows the import-retirement form: import the explicit cap sheets,
prove a bounded local factor theorem, and leave embedding/preparation audits.
The existing Cycle-527 4,096-M2 microgrid may supply unused sites for a cap
embedding; Cycle-533 compute/select/uncompute may supply a preparation pattern;
dynamic puncture surgery may avoid a permanent cap.  These are constructive
engineering/physics routes, not automatic requests for an axiom.

### N7 — hostile steelman

> A hostile reviewer should reject any claim that the two remaining walls are
> fundamental.  The exact disk complex has already reduced every operator
> obligation to bounded face incidence and short dual paths.  Cycle 527 has a
> large installed local microgrid, and Cycle 533 has shown that enormous local
> truth-table isometries can be compiled without dense ambient unitaries.  An
> explicit sheet placement plus a sweep/compute/uncompute stabilizer encoder
> could therefore close both walls without changing the target algebra.  The
> terminal obligation is a physical placement and circuit, not a theorem that
> local topology cannot work.

The steelman is mathematically actionable and blocks a broad no-go.

### N8 — cross-cycle echo

Cycles 235 and 247 converted fermionic ordering into face and puncture
structure but left topological multiplicities.  Cycle 269 sharpened three of
them into spin characters.  Cycle 529 removed an exchange-law wall with a
stateful relational field but exposed a chart wall.  Cycle 532 converted the
extensive multiplicity into a genuine local gauge subsystem.  Cycle 533 then
removed a dense code-space import through explicit reversible computation.

Cycle 537 repeats the pattern: the three Wilson rows cease to be primitive
initializers once an explicit fill complex is allowed.  Earlier global walls
have repeatedly been retired by new relational carriers and concrete
compilers.  The embedding and preparation routes remain open, so there is no
shared obstruction and no axiom pressure.

## Next campaign

Embed the three cap sheets into the existing integer microgrid or construct a
dynamic puncture-surgery equivalent, then compile a literal local stabilizer
preparation/isometry.  Demand one fixed all-24 physical placement, exact
inverse, blank-work return, deletion witnesses, L5/held-L6 recurrence, and the
same full-Fock target replay.  Do not revert to a growing Wilson measurement or
call the algebraic quotient itself an encoding.
