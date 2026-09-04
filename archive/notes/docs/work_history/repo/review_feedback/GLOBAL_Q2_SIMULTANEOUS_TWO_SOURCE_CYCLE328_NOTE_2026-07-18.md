# Global-Q2 simultaneous two-source compiler — Cycle 328

Date: 2026-07-18
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/global_q2_simultaneous_two_source_cycle328_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 328 compiles a simultaneous global Q=2 source sector on the complete
Cycle-322/Cycle-315 `M64 tensor M64` matter seam. The preparation has both
reservoirs occupied simultaneously. Each endpoint may emit, transport, and
absorb while the actual Cycle-230 contact remains in the factor schedule.

The ambient Q2 tensor is large, so the runner uses an exact sparse reachable
restriction: it stores only source-sector occupation labels reached by the
declared two-update protocol, with a dense 4,096-component matter vector at
each label. The lawful code, ambient dimension, reachable count, total charge,
and leakage are all explicit. No state-amplitude truncation or Krylov tolerance
defines the code; Krylov exponentiation applies the exact sparse local source
generator inside that declared sector.

For both tested statistics choices and both endpoint roles,

```text
E_Q2 G_Q2 = G_physical,Q2 E_Q2.
```

The largest forward residual is `1.41399e-15`; the largest conjugate inverse
residual is `2.46944e-15`. The physical statement is the complete Cycle-315
matter encoding tensored with supplied orthogonal Q2 occupation labels. A
primitive M2 synthesis of the bosonic or labelled source-sector factors is not
claimed.

Two supplied mediator statistics are probed:

- bosonic mediator statistics: one symmetric mediator species, with field
  double occupation allowed;
- independently labelled mediator statistics: distinct A-labelled and
  B-labelled mediator species, with coincident spatial/direction modes allowed.

Both give an exact, nonfactorizing occupation response through held `L=6`.
For the bosonic sector,

```text
<R_A R_B>                         = 0.5929377077947355
<R_A><R_B> connected subtraction = -0.001529375553990353
product of separate Q1 responses = 0.59479432751664
joint minus Q1 product            = -0.001856619721904429.
```

For the independently labelled sector,

```text
<R_A R_B>                         = 0.5929583577037859
<R_A><R_B> connected subtraction = -0.0018359698128539437
joint minus Q1 product            = -0.0018359698128540547.
```

The two joint survivals differ by `2.0649909050374227e-05`, so the observable
is statistics-sensitive. These are finite reservoir-occupation correlations.
They are not force, not energy, not stress, not gravity, not metric response,
and not time.

The actual contact is retained and firewalled but not identified by this
response. Deleting contact changes the two-depth joint-reservoir observable by
only `0` in the bosonic run and `1.11022e-16` in the labelled run. The result
therefore does not attribute the nonfactorization to contact.

## Lawful global-Q2 codes

Let the one-body source modes be

```text
R_A, R_B, and F_(x,d) for every cell x and direction d.
```

For lattice size `L`, the number of one-body modes is

```text
N = 2 + 6 L^3.
```

The bosonic code is the symmetric two-occupation sector, except that each
reservoir is hard limited to one occupation. Its ambient dimension is

```text
N(N+1)/2 - 2.
```

The independently labelled code has one A-sector label in `R_A` or a field
mode and one B-sector label in `R_B` or a field mode. Its ambient dimension is

```text
(1 + 6 L^3)^2.
```

The initial occupation is `R_A R_B` in either code. Total Q remains exactly
two. The independent labels are a supplied statistics/species choice; they
are not derived source identities.

| L | role | bosonic ambient | bosonic reachable | labelled ambient | labelled reachable |
|---:|---|---:|---:|---:|---:|
| 3 | training | 13,528 | 1,744 | 26,569 | 1,849 |
| 4 | training | 74,689 | 1,831 | 148,225 | 1,849 |
| 6 | held | 843,049 | 1,831 | 1,682,209 | 1,849 |

Each reachable label carries the complete 4,096-state matter seam. Lawful-Q2
leakage is exactly zero for both statistics through all reported sizes. The
largest norm drift is `1.04361e-14` for the bosonic held run and
`3.55271e-15` for the labelled held run.

The size independence after `L=4` is a finite-depth support result. It is not
an infinite-volume or continuum limit.

## Simultaneous source generator

At endpoint `X`, the local bosonic exchange is

```text
T_X = sum_d (
        c^dagger_X,reverse(d) c_X,d b^dagger_X,d r_X
      + c^dagger_X,d c_X,reverse(d) r^dagger_X b_X,d
      ).
```

The bosonic creation amplitude includes `sqrt(n_d+1)`. Reservoir occupation is
zero or one. The independently labelled route uses the same one-Q vertex in
the A and B species factors.

The local Q1 block has dimension 448. The local bosonic Q2 block has dimension
1,728. Both sparse generators are Hermitian exactly and preserve

```text
Q,
N_matter,
P = P_matter + 2 P_mediator.
```

| local sector | generator Hermiticity | `[T,Q]` | `[T,N_matter]` | largest `[T,P_i]` | source-frame residual |
|---|---:|---:|---:|---:|---:|
| Q1 | `0` | `0` | `0` | `0` | `0` |
| Q2 bosonic | `0` | `0` | `0` | `0` | `0` |

All 24 proper-cubic source-frame permutations are tested. The relative
coefficient two, source angle, bosonic square-root factors, and mediator
statistics are supplied structure. A unit-weight Q2 source remains open.

## Complete update and physical lift

The factor order is

```text
matter coin
mediator coin
source A
source B
edge FSWAP
mediator stream
contact.
```

Bosonic coin and stream are the symmetric second-quantized one-body maps. The
labelled route applies the same one-body map to each species. The source
exponential uses sparse Krylov action on each bounded local active block; it
does not form the full ambient Q2 tensor.

The physical lift uses Cycle 315's AB and BA matter encodings and bounded
matrix-unit completions. Q2 occupation labels remain orthogonal spectator
factors for matter coin, FSWAP, and contact and active factors for source coin
and stream.

| statistics | edge role | forward EG | inverse EG | input labels | output labels |
|---|---|---:|---:|---:|---:|
| bosonic | AB | `1.41398e-15` | `2.43413e-15` | 4 | 76 |
| bosonic | BA | `1.41398e-15` | `2.43413e-15` | 4 | 76 |
| labelled | AB | `1.40641e-15` | `2.46944e-15` | 5 | 91 |
| labelled | BA | `1.40641e-15` | `2.46944e-15` | 5 | 91 |

A bounded rail inventory sufficient for either Q2 choice uses two mediator
rails per direction or two labelled species: 12 mediator M2 per cell plus one
local reservoir M2 and the inherited 29 matter-code M2, for a candidate 42 M2
per cell. On the two-cell seam the count is 109 M2: inherited 83, 24 mediator
rails, and two reservoir M2. The rail symmetrization/species constraints and
their primitive physical synthesis are supplied, not derived by the runner.

## Nonfactorizing simultaneous response

The matter preparation is the symmetric one-one state used in Cycle 322. Both
reservoirs are occupied in the same state, then two complete updates are
applied. The response observables are reservoir means, joint reservoir
survival, connected reservoir covariance, and probability that both Q units
occupy field modes.

### Bosonic sector

| L | role | `<R_A>` | `<R_B>` | `<R_A R_B>` | connected covariance | both fields | norm drift |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | training | `0.771016915085996` | `0.7710169150859959` | `0.5929377077947355` | `-0.001529375553990353` | `0.050903877622746244` | `6.21725e-15` |
| 4 | training | same | same | same | same | `0.05090387762274617` | `1.04361e-14` |
| 6 | held | same | same | same | same | `0.05090387762274617` | `1.04361e-14` |

### Independently labelled sector

| L | role | `<R_A>` | `<R_B>` | `<R_A R_B>` | connected covariance | both fields | norm drift |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | training | `0.7712291018346233` | `0.7712291018346233` | `0.5929583577037859` | `-0.0018359698128539437` | `0.05050015403454247` | `3.55271e-15` |
| 4 | training | same | same | same | same | same | `3.55271e-15` |
| 6 | held | same | same | same | same | same | `3.55271e-15` |

The separate-Q1 comparator multiplies the two diagonal Cycle-322 reservoir
survivals:

```text
0.7712291018346235^2 = 0.59479432751664.
```

Both simultaneous results differ from this product and have nonzero connected
covariance. This closes a common-code two-source correlation observable. It
does not identify a force, exchange energy, interaction potential, or source
tensor.

## Statistics discriminator

The bosonic and labelled joint survivals differ by
`2.0649909050374227e-05`; their both-field probabilities differ by about
`4.03724e-4`. The one-body coin, stream, matter preparation, source angle,
update depth, and readout are held fixed. The difference therefore
distinguishes the two supplied mediator-statistics laws within this finite
protocol.

The result does not select which statistics is physical. Hardcore and
fermionic antisymmetric mediator sectors remain untested. Those alternatives
can alter bunching, source amplitudes, signs, rail constraints, and response.

## Deletions and firewalls

Deleting source B leaves its reservoir occupied with expectation
`1.0000000000000044` in the bosonic route and `1.0000000000000036` in the
labelled route. Norm drift stays below `4.45e-15`. This confirms that the joint
observable depends on both endpoint source vertices.

The contact firewall retains the actual Cycle-230 phase on 4,047 matter
columns. Contact deletion has operator norm `1.9911500883709052`. Yet the
selected two-depth joint-reservoir observable is contact-insensitive at the
reported precision. Contact is present in physical EG and remains available
for other observables or depths, but it is not identified here.

The mass firewall is unchanged:

| control | value |
|---|---:|
| Cycle-219 mass fixture | `0.4534056541748851` |
| two-cell seam mass | `0.4534056541748851` |
| uniform eigenvector residual | `3.85718e-16` |

## Covariance and translations

The source generators, mediator coin, one-body stream, and inherited matter
seam cover all 24 proper-cubic frames. Twelve preserve the endpoint role and
twelve implement endpoint reversal. Source-frame residuals and field-coin
residuals are zero. The one-body stream passes 3,888 frame/cell/direction
tests with zero failures. The inherited complete-seam raw covariance maximum
is `2.16778e-16`.

All L=3 translations are tested for both statistics choices. Each has 27
translated source pairs. The maximum response-or-norm residual is
`6.21725e-15` for bosons and `3.55271e-15` for labelled mediators.

These are covariance tests of source families. The initial edge, reservoir
occupations, matter preparation, and readout remain supplied.

## Supplied structure, derived results, and open work

Supplied structure:

- the complete Cycle-315/Cycle-322 `M64 tensor M64` AB/BA matter seam;
- matter coin, edge FSWAP, actual contact, and factor order;
- global-Q2 preparation with `R_A R_B` occupied;
- coefficient-two source generators and source angle;
- bosonic or independently labelled mediator statistics;
- field coin, stream, finite periodic sizes, and two update depths;
- sparse reachable restriction and Krylov evaluation protocol;
- reservoir/joint/both-field observables and separate-Q1 product comparator;
- orthogonal Q2 physical factors and candidate rail inventory.

Derived here:

- exact Q2 Q, matter-number, and vector source ledgers;
- exact simultaneous-source norm and lawful-sector closure;
- AB/BA common-code physical EG for two statistics choices;
- nonfactorizing joint reservoir response and connected covariance;
- a nonzero mediator-statistics discriminator;
- source deletion, frame, endpoint-reversal, translation, held-size, mass, and
  contact firewalls.

Open:

- hardcore mediator statistics;
- fermionic antisymmetric mediator statistics and ordering/sign audit;
- unit-weight auxiliary or paired-mediator global Q2;
- primitive M2 synthesis of bosonic rail symmetry or species constraints;
- multi-edge simultaneous-source recurrence;
- autonomous Q2 preparation and statistics selection;
- a contact-sensitive operational observable;
- physical calibration as momentum, force, energy, stress, gravity, metric
  response, or time.

## TOE dependency ledger and maturity

| wall | Cycle-328 effect | remaining import |
|---|---|---|
| `C_ref` | two reservoirs are now prepared and read jointly on one common code | reservoir placement, symmetric matter state, two-update depth, and readout remain supplied |
| `C_num` | global Q2 simultaneous source-sector closure replaces separate Q1 columns | statistics choice, local preparation, higher Q, and multi-edge closure remain open |
| `C_wrap` | unchanged | update depth and factor order are not clock time or rate |
| `C_int` | two source vertices act simultaneously on complete matter Fock sectors with exact ledgers | coefficient two, source angle, statistics, and contact-sensitive observable remain supplied/open |
| `C_local` | sparse Q2 labels tensor the same bounded AB/BA physical matter seam and close through held L6 | Q-factor primitive synthesis and multi-edge overlap remain open |
| `C_source` | nonfactorizing and statistics-sensitive simultaneous-source occupation responses are derived | no statistics selection, unit-weight Q2, calibrated source tensor, or metric response |

The exact simultaneous Q2 response is a real source-lane advance, but remains
dimensionless, prepared, statistics-dependent, and uncalibrated. A conservative
score update is:

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 64% | 30% | 91% | 3.5/5 |
| causal time / clock | 35% | 17% | 64% | 1.9/5 |
| inertia / matter | 76% | 37% | 97% | 4.3/5 |
| gravity / source / resource | 41% | 17% | 69% | 2.2/5 |
| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 |

## No-Go Discipline Gate

The broad candidate negative is that simultaneous global-Q2 sources cannot be
closed on the complete physical matter seam or cannot yield a nonfactorizing
common-code response. Both the bosonic and independently labelled
constructions are bounded counterexamples. Stronger questions about statistics
selection, hardcore exclusion, unit weights, multi-edge recurrence,
preparation, and calibration retain live routes.

Gate status: **FAIL / DO NOT SHIP** the broad negative. There is no shared
obstruction and no axiom pressure.

### N1 — alternative routes

| route | marker | actual disposition |
|---|---|---|
| bosonic global-Q2 mediator | **ATTEMPTED** | exact sparse closure and nonfactorizing response; double occupation and square-root source amplitudes supplied |
| independently labelled global-Q2 mediators | **ATTEMPTED** | exact sparse closure and nonfactorizing response; A/B species identities supplied |
| hardcore global-Q2 mediator | **OPEN / UNTESTED** | no exclusion-preserving coin/source compiler is implemented |
| fermionic antisymmetric mediator | **OPEN / UNTESTED** | no exterior field lift or full frame/order sign audit is implemented |
| unit-weight auxiliary global-Q2 | **OPEN / UNTESTED** | Cycle 325 is global-Q1 and its supplied pair program is not lifted here |
| paired-mediator unit-weight Q2 | **OPEN / UNTESTED** | no two-mediator unit-weight source sector is built |
| multi-edge simultaneous source network | **OPEN / UNTESTED** | no overlapping Q2 source-edge recurrence is compiled |
| calibrated physical source observable | **OPEN / UNTESTED** | no operational force, energy, stress, source tensor, or metric observable is supplied |

Two routes succeed and six materially different stronger routes remain open.

### N2 — wall-independence audit

The collapsed walls for a stronger source theorem are:

- `W_stats`: derive or select mediator statistics;
- `W_unit`: replace coefficient two with a unit-weight Q2 ledger;
- `W_multiedge`: compile overlapping simultaneous-source edges;
- `W_prepare`: derive Q2 preparation and source/readout placement;
- `W_energy`: calibrate an operational energy/stress/source observable.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---|---|---|
| `w_stats`, `w_unit` | no | no | yes |
| `w_stats`, `w_multiedge` | no | no | yes |
| `w_stats`, `w_prepare` | no | no | yes |
| `w_stats`, `w_energy` | no | no | yes |
| `w_unit`, `w_multiedge` | no | no | yes |
| `w_unit`, `w_prepare` | no | no | yes |
| `w_unit`, `w_energy` | no | no | yes |
| `w_multiedge`, `w_prepare` | no | no | yes |
| `w_multiedge`, `w_energy` | no | no | yes |
| `w_prepare`, `w_energy` | no | no | yes |

Statistics selection does not impose unit weights. Unit weights do not compile
multi-edge recurrence. Multi-edge recurrence does not derive Q2 preparation.
Preparation does not calibrate a physical source observable. No directed
implication collapses another wall.

### N3 — hidden-wall scan

The executable literal scan covers the note and runner and reports zero hits.
The supplied inventory exposes the matter code, Q2 preparation, statistics,
source amplitude law, coefficient, coin, stream, factor order, sparse
restriction, Krylov evaluation, sizes, physical Q factors, and observables.

### N4 — residual matching

| exact witness | inherited boundary | Cycle-328 treatment | match? |
|---|---|---|---|
| `TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md:43` | global Q2 simultaneous emission absent | declared Q2 sector constructed | yes |
| same file, line 112 | complete Cycle-315 matter seam | retained matter code | yes |
| `FULL_FOCK_UNIT_WEIGHT_MEDIATOR_PAIRED_TWO_SOURCE_CYCLE325_NOTE_2026-07-18.md:311` | global Q2 open | coefficient-two Q2 route tested here | yes |
| `PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md:26` | complete two-cell Fock space | 4,096 matter states per Q2 label | yes |
| same file, line 172 | coin-FSWAP-contact covariance | retained matter schedule | yes |

The contact-deletion zero is matched only to the selected two-depth joint
reservoir observable. It is not used against contact-sensitive observables,
other depths, or scattering preparations. Bosonic and labelled results are not
used against hardcore or antisymmetric statistics.

### N5 — rhetoric audit

“Nonfactorizing” means the tested joint occupation differs from both the
product of its reservoir means and the separate-Q1 product. It does not mean a
force, binding energy, or gravitational interaction was measured.

“Statistics-sensitive” means two supplied finite mediator laws yield different
joint probabilities with other protocol inputs held fixed. It does not select
a statistics law or claim exhaustive alternatives.

“Contact not identified” reports a deletion result for one observable and
depth. The actual contact remains present in the compiler and nontrivial as an
operator.

### N6 — partial-closure paths

Live constructive paths include:

- build a hardcore occupation code with an exclusion-preserving coin;
- build the fermionic antisymmetric field lift and audit all signs/frames;
- lift the Cycle-325 unit-weight pair program to global Q2;
- construct a paired-mediator unit-weight source;
- tile Q2 source factors over adjacent edges and test overlaps;
- search depths/observables that operationally identify contact;
- derive local Q2 preparation or statistics selection.

Each can retire a supplied import without axiom language.

### N7 — hostile steelman

A hostile reviewer should reject a claim that either tested statistics is
physical or necessary. Bosonic bunching and independent A/B species are both
supplied. Hardcore spins, fermionic mediators, anyonic/dressed sectors, or
other bounded completions can change the response.

The reviewer should reject a claim that the nonfactorizing number is a force or
energy. The contact-deletion control is especially restrictive: this readout
does not identify contact at all. The result is an exact common-code
occupation correlation and statistics discriminator, no more.

The reviewer should also reject a claim that 42 M2 per cell is minimal. It is
a sufficient rail inventory whose Q-factor primitive synthesis remains open.

### N8 — cross-cycle echo

The recent constructive sequence closes successive declared sectors:

- Cycle 315 built the complete two-cell matter Fock seam and contact;
- Cycle 318 supplied local coefficient-two recoil balance;
- Cycle 322 placed two coefficient-two sources on one physical edge but used
  one Q1 response column at a time;
- Cycle 325 supplied a unit-weight global-Q1 mediator-pair alternative;
- Cycle 328 prepares both reservoirs together and closes two global-Q2
  statistics sectors with joint observables.

Each advance exposes new choices rather than proving their necessity. The
broad gate remains **FAIL / DO NOT SHIP**.

## Optimal next campaign

The sharpest next discriminator is the hardcore Q2 route. It should define an
exclusion-preserving local field coin/source law, compile it on the same seam,
and compare its joint survival, covariance, and both-field probability against
the bosonic and labelled values. This directly tests whether the present
statistics sensitivity brackets a third bounded law.

The orthogonal source-law priority is unit-weight global Q2. Both campaigns
must retain the same firewalls and must not interpret occupation differences
as force, energy, stress, gravity, metric response, or time.

## Verification

```text
python3 scripts/global_q2_simultaneous_two_source_cycle328_2026_07_18.py
```

Expected release result:

```text
RESULT GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CERTIFIED
```
