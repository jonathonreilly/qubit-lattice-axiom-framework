# Physical root-free orbit-tree preparation tournament — Cycle 648

Status: **PASS — exact sheet-resolved Wilson seed and even tree decoder; full root-free preparation remains open**
Authority: **none**
Audit: **unset**
Accepted: **false**
Constitutional effect: **none**

## Exact target

The target is an autonomous preparation of the Cycle-642 orbit-tree
gauge/parity sector on physical M2 sites.  It must work on periodic L3, L6,
and held L7; use bounded physical neighborhoods and constant spatial overhead;
commute with ordinary lattice translations and all 24 proper-cubic frames and
their 576 products; and use no root, coordinate-zero sheet, global path,
global parity query, or host-side sector branch.  A unitary route must return
its work under the inverse.  A dissipative route must expose its syndrome
environment and lawful input domain.

A Wilson-only seed, covariance of the already fixed code, an abstract
incidence decoder, or a partial syndrome pump does not meet this target.

Every executable premise is pinned to immutable commit
`014cebe47bff2fbbd981b174a8b0ab8e70dfda53`.  The runner imports only
byte-equal Cycle-642 and Cycle-644 mirrors.  It neither imports nor cites
uncommitted Cycle 646 or Cycle 647 work.

## Strongest result

Cycle 644's identical Bell/S tensor failed because it put both phase gates in
every cell.  The complete four-M2 restriction audit now shows four commuting
local patterns.  They have an exact circuit:

```text
H(q0), CNOT(q0,q1), S(q1) iff z=0,
H(q2), CNOT(q2,q3), S(q3) iff y=0.
```

All other Wilson-support M2s use their unique local X/Y/Z eigenstate.  For
even L, the X eigenvalue is negative on internal roles 12, 13, and 14 in
every cell.  There are no per-loop markers and no runtime parity query.

This prepares every one of the `3L^2` translated Wilson signs as `+1` on
L3/L6/L7, with maximum numerical residual at most `3.11e-15`.  Every
elementary gate touches at most two M2s; each block uses at most six gates;
and the inverse returns each four-M2 block to blank at floating residual below
`8e-11`.  Removing one required phase gate produces a nonzero Wilson residual.

The advance is exact but not root-free.  The four tensor patterns are selected
by two coordinate-zero sheets.  A unit translation in x changes no block;
unit translations in y and z each disagree on exactly `2L^2` blocks.  The
sheet count `(0,L^2,L^2)` also fails an axis cycle.  Fixed-code all24/all576
covariance still passes, but preparation covariance does not follow.  Every
bounded local stabilizer has zero expectation in this seed, so it fixes the
Wilson sector rather than preparing the full code.

## Route A — direction-sensitive crossing tensor

Disposition:
`EXACT_DIRECTION_SENSITIVE_WILSON_SEED__TWO_SUPPLIED_SEAM_SHEETS_LOCAL_CODE_OPEN`.

The local restrictions within each four-M2 crossing block commute.  Their
four exact common-plus states are two Bell pairs with zero, one, or two local
phase gates.  This repairs the Cycle-644 `L^2` plus / `2L^2` zero split:

| size | translated Wilsons | plus | maximum residual | y-shift mismatches | z-shift mismatches |
|---|---:|---:|---:|---:|---:|
| L3 | 27 | 27 | `1.3322676295501878e-15` | 18 | 18 |
| L6 | 108 | 108 | `2.6645352591003757e-15` | 72 | 72 |
| L7 held | 147 | 147 | `3.1086244689504383e-15` | 98 | 98 |

The result removes loop-specific sign markers and growing prepared paths.  It
does not remove the coordinate-zero phase sheets or prepare Cycle-642 local,
equality, and face checks.

## Route B — weight-three/four reset duals

Disposition:
`WEIGHT3_4_POSITIVE_DUALS__FULL_L3_AND_HELD_PREPARATION_INCOMPLETE`.

For the exact Cycle-644 old-local/Wilson-preserving scope, the meet-in-the-
middle search finds:

```text
support 1: 169
support 2: 61
support 3: 60
support 4: 46
not covered by this search: 67
```

Thus weights three and four add 106 exact positive syndrome-dual witnesses to
the previous 230.  Each accepted correction anticommutes with its target,
commutes with every other selected generator and all three Wilson rows, and
gives a complete local Kraus pair `K0=P+`, `K1=R P-`.

The search is repeated on the actual L3 Cycle-642 independent basis.  Its 454
rows split into 403 dressed local, 39 equality, and 12 face rows.  It finds all
39 equality duals at support one and the same `169/61/60/46` support census on
the local rows; none of the 12 face rows receives a positive witness in this
executed representative search.  Of all 375 positive algebraic witnesses,
316 have physical L1 diameter at most 80.  Support weight alone is therefore
not physical locality.

The one-representative-per-pair-syndrome search is complete at weights one and
two but is only a positive-witness search at weights three and four.  The 79
uncovered algebraic rows, and the larger set outside diameter 80, are not
claimed to lack other corrections.  L6/L7 full pumps are not run after the L3
terminal remains incomplete.  The syndrome environment is not returned by a
Stinespring inverse, and preparation covariance is not established.

Deleting one Pauli factor from a support-three witness gives a nonzero
syndrome signal.  Every retained witness has zero off-target syndrome bits;
that is the leakage control on the executed basis.

## Route C — root-label-blind leaf pump

Disposition:
`EXACT_ROOT_LABEL_BLIND_EVEN_SYNDROME_LEAF_PUMP__ODD_PARITY_AND_PHYSICAL_ROUTING_OPEN`.

For one Cycle-642 axis, an auxiliary logical-edge X toggles exactly the two
incident face checks and commutes with all equality and dressed local rows.
The runner peels every current leaf simultaneously.  A negative leaf selects
its incident edge and passes its syndrome to the surviving neighbor.  A final
two-vertex center selects its shared edge once when both signs are negative.
The rule reads adjacency and local syndrome bits, never the vertex named
`root`.

Every even face syndrome is exhausted on all three sizes:

| size | even syndromes/axis | odd syndromes/axis | even failures | odd residual | rounds |
|---|---:|---:|---:|---:|---:|
| L3 | 8 | 8 | 0 | exactly 1 | 1 |
| L6 | 64 | 64 | 0 | exactly 1 | 2 |
| L7 held | 128 | 128 | 0 | exactly 1 | 3 |

The exhaustive decoder commutes with all 24 proper-cubic actions and all 576
products at every size.  This is covariance of the abstract tree decoder,
not preparation covariance in physical space.

Odd syndrome is outside the lawful domain.  It leaves one defect because
auxiliary edge X corrections generate the even boundary image.  A supplied
single-defect absorber would close that bit, but would reintroduce the sector
service the target forbids.  The inherited Cycle-642 face measurements also
have maximum routed pair lengths `136/344/345`; no crossing schedule, static
fine-nearest-neighbor gadget, or returned routing history is constructed.

Deleting one selected edge correction leaves a nonzero two-endpoint syndrome.
The measurement/reset map is dissipative, so a unitary inverse is not claimed;
the missing returned syndrome environment remains explicit.

## Held-size, covariance, inverse, leakage, and lawful-domain controls

- Route A executes L3/L6/L7 Wilson expectations, circuit inverses, phase-gate
  deletion, local-stabilizer leakage, ordinary translations, and the inherited
  fixed-code all24/all576 check.
- Route B executes exact L3 syndrome witnesses and factor deletion.  Its
  failure to run full held pumps is explicit.
- Route C exhausts every even and odd abstract face syndrome on L3/L6/L7 and
  checks all24/all576 decoder equivariance.  It separately refuses odd parity
  and physical-routing credit.
- The Cycle-642 target-times-gauge ranks and the Cycle-219 mass, Cycle-230
  contact deletion, and Cycle-230 seam fixtures remain exact pinned
  comparators.  No new full `E G = G E` surface is claimed.

State preparation and fixed-code covariance remain separate fields throughout
the receipt.

## N1-N8 discipline

The freshness check fetched origin main.  This cycle follows the newer
no-go-discipline body with SHA-256
`7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7`
and proof-search governance with SHA-256
`be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258`.

N1 records the three executed families above.  Five materially different
routes remain open and are not counted as failures: an injective graded PEPS,
a distributed Clifford cellular automaton, defect/code growth, a reversible
routed syndrome controller, and translation-invariant dissipative cooling.
Only one executed family is target-equivalent, below the required five.

N2 keeps five scoped walls: coordinate sheets, incomplete dual coverage, odd
face parity, physical face routing, and preparation covariance.  All 20
ordered directions are explicit with `closure_implied=false` and interface
evidence.  Independence beyond the executed interfaces is not asserted.

N3 lists every sheet, size/parity choice, selected basis, pair representative,
diameter threshold, tree, macro-origin, active flag, measured syndrome, and
round schedule.  N4 exactly matches Cycle 644's tensor and reset residuals and
Cycle 642's preparation omission; the different Cycle-643 square-fill target
is dropped.  N5 audits each negative phrase at element, site, mode, block, and
lattice resolution.  N6 lists five concrete partial-closure paths.

N7's strongest counter-route is a translation-invariant virtual-bond gauge
combined with a state-carried defect controller and mobile odd-defect
absorber.  N8 records rowwise mechanisms and applicability from Cycles 629,
642, 643, and 644 with exact immutable references.

```text
broad negative gate: FAIL / DO NOT SHIP
minimum-content gate: FAIL / DO NOT SHIP
shared-obstruction gate: FAIL / DO NOT SHIP
axiom-pressure gate: FAIL / DO NOT SHIP
```

No impossibility, minimum-content, shared-obstruction, or axiom-pressure claim
is shipped.  The no-go schema status is PASS because every scoped negative is
demoted to an attempted-route residual and the live alternatives remain open.

## Supplied structure

- immutable shore `014cebe47bff2fbbd981b174a8b0ab8e70dfda53`;
- finite L3/L6/L7 domains and compile-time L parity;
- Cycle-642 tree topology, orbit fibers, K129 shell, and macro-origin;
- four crossing-block pattern labels;
- coordinate-zero y and z phase sheets;
- three even-L negative X-role signs;
- the selected L3 stabilizer basis and one representative per pair syndrome;
- physical diameter threshold 80;
- measured face-syndrome bits, active flags, and synchronous leaf rounds;
- Cycle-642 shortest-path families without a crossing controller;
- pinned target-times-gauge, mass, contact, and seam comparators.

Not supplied or claimed are a global Wilson operation, runtime parity query,
host sector branch, root-free phase-sheet genesis, complete held reset pump,
odd-defect absorber, fine-nearest-neighbor face-measurement controller,
returned dissipative exhaust, physical time, energy, rate, Record, source,
stress, gravity, or Born law.

## Prior-art and novelty boundary

Bell-pair stabilizer preparation, syndrome-reset Kraus maps, tree decoding,
and virtual-bond gauge ideas are established techniques.  Cycle 648 claims no
invention of those general methods.

The new repository-local result is the exact identification and execution of
the four direction-sensitive Cycle-644 crossing states, including all `+1`
signs in the `3L^2` Wilson census with maximum numerical residual at most
`3.11e-15`, and exact `2L^2` translation mismatch.  It also adds the
support-three/four syndrome witnesses and the exhaustive root-label-blind
even-face decoder for the specific Cycle-642 orbit tree.

Thirring is not used.

## Dependency ledger

| wall | Cycle-648 movement | exact residual |
|---|---|---|
| `C_ref` | advanced | loop markers and rooted Wilson paths become two supplied coordinate-zero phase sheets; sheet genesis remains |
| `C_num` | advanced locally | exact support-three/four syndrome witnesses; no empirical or Born normalization |
| `C_wrap` | advanced | all translated Wilson signs and every even tree-face syndrome close; odd parity and physical routing remain |
| `C_int` | pinned | Cycle-642 quotient and mass/contact/seam remain comparators; no full update intertwiner |
| `C_local` | mixed | support-two Wilson circuit passes; diameter-80 reset coverage is partial; face routing lacks a controller |
| `C_source` | unchanged | no energy, rate, source, stress, gravity, Record, or autonomous reservoir genesis |

Cycle 648 does not independently rebase campaign lane coordinates.

## Scope firewall

- A Wilson-sector seed is not a full code `E`.
- A coordinate-sheet tensor is not root-free preparation.
- Support weight four is not physical locality without a distance check.
- An uncovered meet-in-the-middle row is not a theorem that no dual exists.
- An even-syndrome decoder is not arbitrary-sector genesis.
- Abstract all24/all576 decoder covariance is not physical preparation
  covariance.
- Fixed-code covariance is not state preparation.
- A compiler round is not physical time.
- A phase is not energy; a generator is not a rate.
- A gauge seed is not a Record.
- No source, gravity, or Born claim is present.

## Optimal next campaign

Replace the two coordinate-zero phase sheets by a state-carried translation
orbit or virtual-bond gauge.  Compile the leaf decoder into a reversible
fine-nearest-neighbor controller with crossing colors and a mobile odd-defect
absorber, return every routing and syndrome-history M2, and require complete
local-stabilizer coverage on L3/L6/L7 before claiming a physical preparation
map.
