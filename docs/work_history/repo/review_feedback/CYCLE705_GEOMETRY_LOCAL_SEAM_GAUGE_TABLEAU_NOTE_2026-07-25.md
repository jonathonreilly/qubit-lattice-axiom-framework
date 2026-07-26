# Cycle 705 geometry-local seam-gauge tableau held discriminator

**Date:** 2026-07-25

**Type:** meta

**Authority:** none

**Audit:** unset

**Dependencies:**
[Cycle 703 patch BKSF tableau covariance](CYCLE703_BKSF_PATCH_TABLEAU_COVARIANCE_NOTE_2026-07-25.md),
[Cycle 703 local-Gauss held-patch grammar](CYCLE703_LOCAL_GAUSS_HELD_PATCH_GRAMMAR_ADDENDUM_2026-07-25.md), and
[Cycle 703 local-Gauss reference adversarial note](CYCLE703_LOCAL_GAUSS_REFERENCE_ADVERSARIAL_NOTE_2026-07-25.md).

## Result and claim ceiling

This checkpoint tests a geometry-aware Route-B state chart on the existing
seven-mode-per-cell local-`D` BKSF graph.  It adds one abstract edge-gauge
qubit to each
coarse matter seam.  A bounded diagonal stabilizer copies an elementary-face
cell-parity word into that gauge bit, and a directly constructed two-endpoint
spoke word reads the bit.  A closed-form staggered seam orientation is
evaluated from the transported coframe, origin, endpoint coordinates, and
periodic chart cut.  The candidate constructor never calls the target path
helper, inspects an interval of cells, or requests a runtime exterior-order or
global parity service.  There is no supplied Hamiltonian cell path on the
edge-qubit constructor interface.  The graph-edge addresses and coframe/origin
labels used here are abstract placement data; they are not yet an injective
one-M2-per-`Z^3`-site placement or nearest-neighbour routing circuit.

The construction is an exact positive on the frozen open L and `2 x 2`
fixtures, but its target transfer is negative on all three held families:

- the phase-aware common E, stabilizer rank, inverse tableau, leakage,
  translations, 24 proper-cubic frames, and 576 ordered frame products close
  on all five finite fixtures;
- every onsite coin, directed seam, and onsite contact is present in the full
  scheduled `G_edge`, with zero edge-qubit support collisions and active complete
  seam-factor deletion;
- after deterministic stabilizer-coset descent, every individual Pauli
  summand has constant support, every seam representative has weight at most
  `17`, and its cell diameter is at most `3`;
- the frozen face rule matches every target seam coset on L and `2 x 2`;
- without refit, it misses `5` of `12` seams on open `3 x 3`, `55` of `81`
  seams on periodic `L=3`, and `132` of `192` seams on periodic `L=4`;
- even an independently enlarged ansatz allowing an arbitrary product of all
  cell parities in the elementary radius-one neighborhood of each seam fails
  on at least one seam in every held family.

This is a route-specific negative for the frozen one-face copy rule and the
named elementary-radius-one diagonal span.  It is not a no-go for larger
bounded neighborhoods, multiple face channels, non-diagonal Gauss laws,
subsystem codes, or recurrent local gauge dynamics.  There is no
route-independent no-go, minimum-content claim, or axiom pressure.

## Frozen gauge/tableau construction

Let `q_e` be the edge-gauge qubit on a coarse seam `e`.  The underlying BKSF
graph retains the six matter modes, scalar reference mode, 12 octahedral
edges, six reference spokes, and the ordinary matter stream edge in every
cell neighborhood.  It adds no parallel intercell reference fermion edge.

In the transported local coframe, axis 0 is the row direction.  An axis-1
seam on an exposed negative-axis-0 boundary uses the opposite edge of its
elementary 0-1 face.  If the positive face is absent, or if the negative face
is present, the copied word is the identity.  Axis-0 and axis-2 seams also
copy the identity.  Writing `D_e` for that product of whole-cell matter
parities, the added row is

```text
S_e = Z(q_e) D_e = +1.
```

The program order of the two seam endpoints is also local data.  If
`(x,y,z)` is the coordinate of the negative endpoint in the transported
coframe, set `r=y` on an open chart or an even-`z` torus layer and
`r=L-1-y` on an odd-`z` torus layer.  An axis-0 seam is forward when `z+r` is
even, an axis-1 seam is forward when `z` is even, and an axis-2 seam is
forward.  The direction is reversed on crossing the periodic cut in that
axis.  This is a bounded staggered orientation 1-cochain: it uses the two
endpoint chart labels, not the ordered cell list or an interval query.  On the
five scored target charts it agrees with the endpoint order induced by the
prior even snake grammar; a separate combinatorial check finds zero endpoint-
orientation mismatches on every seam.

For program endpoints `(L,m_L)` and `(R,m_R)`, write `u,v` for the matter
vertices, `r_L,r_R` for the two scalar references, and
`Q_R=product_(m != m_R) B_(R,m)`.  The two raw local words are constructed
directly as

```text
- Q_R A_(r_L,u) A_(v,r_R),
  Q_R B_u B_v A_(r_L,u) A_(v,r_R).
```

No path-dressed stream term is created and then cancelled.  Both words read
`Z(q_e)`.  They also flip each copied gauge bit whose `D_f` contains exactly
one endpoint cell; those bounded collateral `X(q_f)` factors are required to
preserve one common E after the matter hop changes the two endpoint parities.
Their exact common-E decode is

```text
local_word_e Z(q_e) product_(f toggled by e) X(q_f)
    -> target_hop_e times P_between(e) times D_e.
```

Here `P_between(e)` appears only when the edge-qubit word is decoded and scored
against the supplied prior Fock target; it is absent from the edge-qubit
constructor.  Exact Pauli-phase decoding verifies that the residual is a
product of whole-cell parity blocks on every seam.  The seam is exact
precisely when `D_e=P_between(e)`.  The L and `2 x 2` freeze determines the
displayed face rule before the open `3 x 3` and periodic rows are inspected;
the three-dimensional staggered extension is fixed as part of the chart rule,
not fitted to held residuals.

The stabilizer has one unique `Z(q_e)` pivot per seam, so every added row is
independent.  Starting from the landed patch tableau, the common E is extended
analytically: a logical `X_i` also flips every `q_e` whose copied word contains
`Z_i`, and `X(q_e)` is the destabilizer paired with `S_e`.  The resulting
`W/V` rows have the exact canonical symplectic matrix and full rank.  This is
an abstract graph-edge stabilizer isometry, not a dimension-only count.

The compact `S_e` can equivalently be factored through one bounded face qubit as
`Z(f_e)D_e=+1` and `Z(q_e)Z(f_e)=+1`.  That factorization changes routing and
ancilla count but not the logical copied word.  It therefore cannot repair a
held target outside the tested face-parity span by itself.

## Common-E typing and finite census

| Fixture | total edge qubits | scheduled coin / seam / contact | target seam misses | radius-one span misses | max seam weight / cell diameter |
| --- | ---: | ---: | ---: | ---: | ---: |
| frozen open L | 58 | `36 / 2 / 45` | 0 | 0 | `13 / 2` |
| frozen open `2 x 2` | 80 | `48 / 4 / 60` | 0 | 0 | `14 / 2` |
| held open `3 x 3` | 186 | `108 / 12 / 135` | 5 | 2 | `14 / 3` |
| held periodic `L=3` | 648 | `324 / 81 / 405` | 55 | 30 | `17 / 2` |
| held periodic `L=4` | 1,536 | `768 / 192 / 960` | 132 | 104 | `17 / 2` |

For the open fixtures the typing is

```text
E_gauge : H_matter -> H_gauge_code,
G_edge E_gauge = E_gauge G_candidate.
```

On the periodic fixtures, before a Wilson vector is selected, it is

```text
E_direct_sum : H_matter tensor C^8_Wilson -> H_gauge_code,
G_edge E_direct_sum
    = E_direct_sum (G_candidate tensor I_8).
```

The displayed fixed tableau uses the `+++` slice only to orient columns.  The
three Wilson characters are retained as typed spectators, every update acts
sector-identically, and no matter-only Wilson genesis is claimed.  A supplied
Hamiltonian cell path is used only by the adversarial target oracle to state
the prior Fock-chart seam signs.  The edge-row helper is separated from
the scorer and is statically checked to contain no path helper, interval,
ordered-cell index, or target-order query.  Only after those rows exist does a
wrapper attach target logical labels for exact common-E scoring.

The common-E identity is exact for `G_candidate` on every fixture.  On the two
freeze fixtures `G_candidate=G_target`.  On the three holds the common E is
still a valid isometry and the full edge-qubit schedule is still code
preserving, but the listed seam factors decode to the wrong target logical
Paulis.  Those nonzero target residuals are not called leakage or tableau
failure.

## Support, covariance, translations, and deletion

Each raw stream reads one adjacent edge gauge bit.  A deterministic,
strictly-weight-decreasing multiplication by loop, local-`D`, Wilson, and
edge-gauge stabilizers gives a signed-coset representative.  The runner
records raw and descended weights separately, reconstructs every descent,
and checks its decoded action.  The retained support claim concerns each
individual Pauli summand, not a complete factor union, logical loader, or
arbitrary tableau destabilizer.

The transported coframe and origin rebuild the face rule.  All four lifted
translations are executed on every open fixture; all `L^3` translations are
executed on each periodic fixture.  The signed stabilizer character, logical
`Z`, phase-oriented logical `X`, and seam cosets are compared under all 24
proper-cubic frames.  The gauge-address and face-cell action composes on all
576 ordered frame products.  These are transformed common-E checks: the
logical `X` comparison includes the second-quantized Fock-permutation crossing
`Z` factors.

Every edge-gauge stabilizer is rank-active because it owns a unique gauge
pivot.  Deleting any one lowers the stabilizer rank by one.  On `2 x 2`,
deleting the nontrivial face-copy factor changes the target seam action.
Removing the complete first seam factor changes the edge-qubit schedule digest
on every fixture.  The redundant all-cell local-`D` relation and the three
periodic Wilson deletions remain as typed in the landed patch tableau.

## Held discriminator and stronger local span

The target oracle supplies the prior path-chart interval only to score the
frozen candidate.  The held open failures include a length-four row chord:
the target interval contains two face tails, whereas the frozen boundary rule
copies only the adjacent elementary face.  It also deliberately does not
propagate that boundary selection into the interior.  Periodic boxes have no
exposed negative-axis-0 boundary, so the frozen copied word is identity there;
their path-chart chords and axis-2 seams remain exact target discriminators.

To ensure that this is not merely the wrong coefficient on the one frozen
face, the runner first decodes each two-term edge-qubit seam and verifies, with
exact Pauli phases and both term permutations, that its common right-`Z`
residual consists only of complete six-bit cell-parity blocks.  It then grants
each seam an arbitrary product of all whole-cell parities at cell-Manhattan
distance at most one from either endpoint.  Residual cells outside that
neighborhood are an exact span witness because the six logical `Z` bits of
different cells are independent in common E.  The exact miss counts are `2`,
`30`, and `104` on open `3 x 3`, periodic `L=3`, and periodic `L=4`.

This stronger test still has a deliberate ceiling.  Radius two, cube cells,
multiple quantum face channels, off-diagonal constraints, and a recurrent
gauge field change the ansatz.  The periodic `L=3` and `L=4` results are held
finite discriminators, not an asymptotic lower bound.

## Supplied and derived structure

Supplied:

- the Cycle-703 seven-mode local-`D` BKSF graph, local incidence-order gauge,
  and prior target Fock chart used only by the scorer;
- one transported ordered coframe and its origin;
- one blank edge-gauge qubit per matter seam;
- fixed `+++` Wilson rows for the displayed periodic tableau, or the explicit
  eight-dimensional Wilson input for direct-sum typing; and
- the complete coin/seam/contact factor inventory.

Derived and executed:

- the closed-form local staggered seam orientation and its zero endpoint-order
  mismatches on all five scored charts;
- the frozen elementary-face copy word and its L/`2 x 2` exactness;
- the analytic phase-aware gauge tableau, common-E decoding, inverse, rank,
  leakage, and stabilizer deletions;
- the full scheduled `G`, collision coloring, individual-summand support, and
  active complete-factor deletion;
- every lifted/open or torus translation, all 24 frames, all 576 products;
  and
- the no-refit held residuals plus the stronger elementary-radius-one span
  witnesses.

Not supplied or derived:

- a selected Hamiltonian path or ordered-cell index for the edge-row
  helper, or any runtime global parity query or exterior-order service;
- a radius-two/cube/multichannel or non-diagonal gauge law;
- a recurrent local correction rule and cleanup theorem;
- constant-depth preparation of the connected BKSF/gauge tableau; or
- autonomous coframe or Wilson genesis.

## No-Go Discipline Gate

**Gate result: FAIL for a broad no-go.  Retain only the exact frozen-route
negative and the constructive common-E/tableau closures.**

### N1 — alternative-route enumeration

1. **Path-dressed construction followed by algebraic cancellation —
   ATTEMPTED AND REJECTED.** Querying the interval before cancelling it violates the lane;
   none of its results are retained.  The replacement builds the endpoint
   words directly and has a static forbidden-query check.
2. **No seam gauge (`D_e=I`) — ATTEMPTED.** It matches path edges but misses
   the nontrivial `2 x 2` chord.
3. **One frozen elementary-face copy per edge gauge — ATTEMPTED.** It closes L
   and `2 x 2`, then misses `5`, `55`, and `132` held seams.
4. **Arbitrary elementary-radius-one cell-parity products — ATTEMPTED.** Exact
   support-span witnesses remain on every held family.
5. **Local stabilizer-basis changes — ATTEMPTED at the declared code.** They
   reduce representatives to weight at most 17 but cannot change decoded
   logical seam action.
6. **Factoring through bounded face ancillas — ATTEMPTED.** Exact algebraic
   reduction shows that it
   realizes the same copied word and does not enlarge its logical span.
7. **Radius-two or cube-supported copies, multiple face channels,
   non-diagonal Gauss laws, subsystem gauge inputs, and recurrent local
   dynamics — OPEN.** Each changes the ansatz and remains live.
8. **A different graph-edge state chart — OPEN.** It must compare one common E
   on training and held fixtures without importing a path-selected parity
   service.

### N2 — wall-independence audit

`W_face-transfer` is the held logical miss of the frozen copy rule, and
`W_radius-one` is the stronger named support-span miss.  They are not
independent: `W_face-transfer` is a strict tested subcase of `W_radius-one`, so
the collapsed route wall is `W_local-diagonal`.  The other walls are
`W_preparation` (bounded-depth genesis of the exact tableau), `W_coframe`
(genesis of its supplied local chart), and `W_Wilson` (matter-only selection
of a periodic character).

| collapsed pair | closing first closes second? | closing second closes first? | independent? |
| --- | --- | --- | --- |
| local-diagonal / preparation | no | no | yes |
| local-diagonal / coframe | no | no | yes |
| local-diagonal / Wilson | no | no | yes |
| preparation / coframe | no | no | yes |
| preparation / Wilson | no | no | yes |
| coframe / Wilson | no | no | yes |

The exact common E retires the finite-isometry wall but none of those four
collapsed walls.

### N3 — hidden-wall scan

The target path chart, freeze/hold split, coframe and origin, boundary
conditions, one edge gauge per seam, diagonal face-copy character, support
radius, fixed/direct-sum Wilson choice, stabilizer descent, scheduled factor
order, and absence of a preparation circuit are explicit.  “Arbitrary span”
means arbitrary products of the listed radius-one cell parities, not arbitrary
local quantum codes.  The staggered orientation 1-cochain is also an explicit
chart texture: it agrees with the target's endpoint order and its torus version
uses the origin-selected periodic cut (including on odd `L=3`).  It does not
contain the interval parity, but autonomous genesis of this orientation is not
proved.  The executable rejects path/interval/order queries in the edge-
row helper rather than relying on an algebraic cancellation claim.

### N4 — residual matching

The common E decodes every onsite and seam summand rather than comparing only
operator commutators.  Both term permutations and exact Pauli phases are
checked; every seam residual is verified to be a complete-cell `Z` word.  The
zero freeze residuals and held counts score exactly the prior path-chart
target.

| cited witness | witness residual | residual used here | match? |
| --- | --- | --- | --- |
| Cycle-703 patch tableau covariance | existence and phase/covariance of finite common E | finite common-E extension and transformed decoding | yes, constructive dependency |
| Cycle-703 local-Gauss held-patch grammar | path-chart seam target, per-summand weight, held chords | the same target seam cosets and local support score | yes |
| Cycle-703 local-Gauss reference adversarial note | direct reference-edge and path-string alternatives | frozen one-face/radius-one edge-gauge transfer | no; context only, not a no-go witness |

The nonmatching third residual is not counted as proof of the present
negative.  Stabilizer commutation is credited only as zero leakage; tableau
rank only as state-isometry capacity; support only as an individual-summand
bound.  None is relabeled as target transfer or preparation.

### N5 — resolution and rhetoric audit

The runner covers every scheduled factor on all five fixtures, every
stabilizer and logical loader needed to orient common E, all declared
translations, all 24 frames, all 576 products, every edge-gauge deletion, and
every held seam's radius-one span membership.

| resolution | tested? | retained wording |
| --- | --- | --- |
| individual Pauli summand support/diameter | yes, all scheduled summands | constant on the five fixtures |
| individual seam logical coset | yes, every seam | exact freeze; named held misses |
| complete scheduled finite `G` inventory | yes, all five fixtures | present, colored, collision-free |
| complete factor-union support | no | no bounded-union claim |
| arbitrary bounded gauge/face code | no | explicitly open |
| infinite family or asymptotic lower bound | no | explicitly not claimed |

The test does not cover larger support radii, arbitrary face Hilbert spaces,
nonlinear/recurrent laws, infinite volume, odd CAR fields, or autonomous
resource genesis.  “Falsifies” is restricted to the named frozen rule and
radius-one diagonal span.

### N6 — partial-closure path scan

The state side, leakage, local support, schedule, translation, and cubic
covariance all close.  Only held target transfer fails.

| partial-closure path | status | what it could close |
| --- | --- | --- |
| radius-two/cube-supported diagonal copy | open; next exact span test named | first open `3 x 3` missing face tail |
| multiple face/two-form channels | open | seam cocycle without one-word compression |
| recurrent local gauge dynamics | open | transport parity information over growing rounds |
| non-diagonal Gauss law | open | change the copied observable class |
| different common-E chart | open | remove the prior Fock-interval target residual |
| convention-only relabeling | insufficient for the fixed target comparison | can change labels, not the scored supplied target |

No row requires a new axiom, and no open construction is reclassified as an
axiom wall.  Each has a concrete acceptance test using the present fixtures.

### N7 — steelman

A hostile reviewer should promote the face bit to a recurrent local gauge
field, propagate boundary/parity information for a growing number of local rounds,
and require the work/gauge registers either to return or to advance under a
typed law.  Another strong route is a two-form face field whose local Gauss
and flatness constraints predict the seam cocycle on both `L=3` and `L=4`
without a chart-period refit.  Acceptance requires the same common-E,
scheduled-G, support, covariance, deletion, and held residual tests used here.

### N8 — cross-cycle echo

| prior echo | later mechanism | lesson applied here |
| --- | --- | --- |
| Cycle-703 finite common-E objection | phase-oriented tableau construction | capacity is credited as closed, not reused as a wall |
| Cycle-703 path-chord weight growth | edge gauges plus stabilizer descent | support wall is retired for tested cosets, logical-sign wall remains |
| earlier same-register rephase negatives | enlarged encodings | keep multichannel/subsystem routes open |
| earlier H/K/P route failures | route-specific reformulations | do not promote one failed grammar to a gauge no-go |

Thus prior negative language is not echoed into a general gauge obstruction,
and the present freeze success is not echoed into a scalable law.

## Reproduction

```bash
PYTHONPATH=scripts python3 -u \
  scripts/frontier_cycle705_geometry_local_seam_gauge_tableau_2026_07_25.py
```

Expected terminal:

```text
CYCLE705_FACE_GAUGE_COMMON_E_FREEZE_EXACT_HELD_SEAM_COSETS_5_55_132_ROUTE_OPEN
```

The retained replay passed 7 checks and failed 0.  Its cache SHA-256 is
`bfbd91fe0f942b1f214a6fa024fb7d51b3b9051f4674c1cf80362ad1ee014af6`.

As an independent math check, a separate combinatorial enumerator using no
BKSF/tableau or Cycle-705 runner helper rebuilt the snake cell orders, nearest
neighbor seams, the closed-form local orientation, exposed-boundary face rule,
and endpoint radius-one balls.  It found zero local-orientation/order
mismatches on every seam and returned `(seams, frozen misses, radius-one
misses)` equal to
`(2,0,0)`, `(4,0,0)`, `(12,5,2)`, `(81,55,30)`, and `(192,132,104)` in the
five fixture order above.
