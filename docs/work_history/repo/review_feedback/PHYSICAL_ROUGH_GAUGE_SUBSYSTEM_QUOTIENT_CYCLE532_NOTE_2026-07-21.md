# Physical rough-gauge subsystem quotient — Cycle 532

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py`

## Result

Cycle 532 turns Cycle 247's previously untyped `N-1` rough-boundary
multiplicity into an exact local gauge subsystem.  This is a constructive
replacement for Cycle 529's globally charted double-shadow values
`(A n,A P n)`, conditional on one explicitly typed topological
initialization.

For `N=L^3`, the rough-terminal face code has 22 physical M2 factors per
coarse cell.  Its bounded loop and cell constraints have rank `15N-2`.
Initializing the three all-plus Wilson/spin signs raises the rank to `15N+1`,
so the fixed-spin code exponent is

```text
22N-(15N+1)=7N-1=6N+(N-1).
```

The first term is the complete six-mode-per-cell target Fock exponent.  The
second is exactly an N-1 gauge-qubit factor.  The equality is not inferred
from dimension alone.  Exact symplectic reduction at L5 and held L6 proves
that the mapped matter even algebra has the target dimension and rank, and
that explicit bounded gauge operators exhaust its full commutant.

The physical B action is the product of three mapped FSWAP polynomials per
cell.  It has the same exact target action `Gamma(P)` as Cycle 529 on all
Fock sectors, commutes with the complete gauge algebra, has M2 support at most
13 per stream block, and requires no site-major `A/AP` chart, parity query,
bank preparation, bank swap, or runtime frame/sector selector.  Relative to
the Cycle-529 15-call logical B schedule, the six shadow-CZ and six bank-SWAP
calls disappear modulo gauge; the three target FSWAP actions remain.  This is
not a claim that the old literal 15-call two-M2 list is reused.

The periodic compiler is not unconditional.  With only bounded local checks,
three spin/Wilson twists remain and the matter quotient has three extra
central characters.  The displayed fixed-target factorization initializes
three growing Wilson words of maximum weight 33 at L5 and 39 at held L6.  No
bounded circuit preparing that fixed-spin face-code state is supplied.  This
is a typed gauge-sector/topological initialization, not a global sector
selector queried by the runtime.  It is the exact remaining boundary and is
not hidden inside `E`.

## Construction

Use Cycle 247's proper-cubic puncture graph.  Each coarse cell contains six
matter vertices, one auxiliary sink at the center, six matter-sink spoke M2
factors, and one rough terminal M2.  The original square-pyramid graph
contributes 15 face M2 factors per cell, so the total is

```text
15 face + 6 spoke + 1 terminal = 22 M2/cell.
```

Let `B_v` and `A_e` be the framed face-code parity and hopping Paulis.  For a
matter stream edge `e=(u_x,v_y)`, Cycle 247's lawful matter generator is

```text
Ahat_e = A_(u_x,v_y) X_(h_x) X_(h_y).
```

It preserves every cell constraint, unlike the undressed stream.  The new
gauge generators are

```text
Zg_x  = Z_(h_x) B_(sink_x)
      = product of the six spoke Z factors at x,

Ag_xy = A_(sink_x,u_x) Ahat_(u_x,v_y) A_(v_y,sink_y).
```

The terminal `Z` cancels from `Zg_x`, giving weight 6.  `Ag_xy` follows a
bounded sink-matter-stream-matter-sink path and has a weight 18 bound.  Direct
Pauli checks prove:

- every `Zg` and `Ag` commutes with every stabilizer;
- every `Zg` and `Ag` commutes with every mapped matter `B/A` generator;
- `Ag_xy` anticommutes with exactly `Zg_x,Zg_y`;
- two `Ag` operators anticommute exactly when their cubic sink edges share one
  endpoint; and
- the explicit gauge span has the same quotient dimension and symplectic rank
  as the complete matter commutant.

Thus the gauge family is not a list of unused boundary labels.  It is the
bounded even-CAR algebra of the auxiliary sink sector and supplies the full
operator commutant required by a genuine subsystem factor.

## Exact subsystem certificate

Let `S` be the fixed-spin stabilizer space and `M` the mapped matter Pauli
space in `S^perp/S`.  The runner computes `M^perp` directly, rather than
assuming that the displayed gauge family is complete.

| quantity | L5 | held L6 | exact law |
|---|---:|---:|---:|
| cells `N` | 125 | 216 | `L^3` |
| physical M2 | 2,750 | 4,752 | `22N` |
| bounded-local rank | 1,873 | 3,238 | `15N-2` |
| fixed-spin rank | 1,876 | 3,241 | `15N+1` |
| fixed-spin code exponent | 874 | 1,511 | `7N-1` |
| target Fock exponent | 750 | 1,296 | `6N` |
| gauge qubits | 124 | 215 | `N-1` |
| matter quotient dimension | 1,499 | 2,591 | `12N-1` |
| matter symplectic rank | 1,498 | 2,590 | `12N-2` |
| explicit gauge dimension | 249 | 431 | `2N-1` |
| explicit gauge symplectic rank | 248 | 430 | `2N-2` |
| full commutant dimension/rank | `249/248` | `431/430` | same as explicit gauge |

The one-dimensional radicals are the shared parity center.  On the code,

```text
product_v B_matter,v = product_x Zg_x.
```

Both signs of this common center are nonempty.  In either fixed matter-parity
sector the exponent is

```text
(6N-1) target + (N-1) gauge = 7N-2,
```

exactly the physical fixed-parity exponent.  Standard finite-dimensional
Pauli representation theory therefore gives, sector by sector,

```text
H_fixed = H_target,full-Fock tensor H_gauge,
rho_matter(O) = O tensor I_gauge
```

for every target even-CAR operator.  This is an algebraic code-space
factorization.  It does not itself produce a bounded state-preparation circuit.

## B runtime and Cycle-529 relation

For each outer edge, use the exact local polynomial

```text
FSWAP_e = (B_u+B_v+i B_u Ahat_e-i B_v Ahat_e)/2.
```

The executable `4 x 4` control has zero matrix, unitarity, inverse-square, and
target residual.  Deleting its fourth term gives residual 1.  On the physical
rough code, each polynomial acts on at most 13 M2 factors and lies in the
faithful matter algebra, hence acts as target FSWAP tensor gauge identity.
The three outer edges per cell form the Cycle-230 B matching.

Cycle 529 proved the charted identity

```text
G_529 E_529 = E_529 Gamma(P)
```

using `a=An`, `b=APn`, six CZs, three endpoint FSWAPs, and six bank swaps per
cell.  Cycle 532 proves instead

```text
G_rough E_rough = E_rough Gamma(P)
```

on the fixed-spin gauge code.  The common target action gives the exact
code-space equivalence.  The `A/AP` values are not assigned to individual
physical M2 factors; their chart transition is absorbed into the gauge
presentation.  This retires the site-major chart, its 601/1,081-support
constraints, its 121,200/309,600 preparation CNOTs, and its 23/24 fixed-chart
failures from this route.  It does not provide a local circuit translating a
prepared Cycle-529 bank state into a prepared rough-code state.

The target replay includes:

- the full quadratic coefficient theorem and hence every Fock sector;
- complete L5 and held-L6 vacuum, N=1, and N=2 censuses;
- the complete 4,096-state two-cell Fock patch;
- straight and corner three-cell domains through N=3, 988 states each;
- deterministic higher sectors;
- inverse, leakage, deleted correction, and perturbed-phase controls.

All baseline target failures remain zero.  Cycle 529's deletion counts remain
the exact comparator for the charted implementation; the rough code's own
deletions are reported separately below.

## Local onsite Givens, coin, and contact compatibility

Every one of the 15 unordered pairs of direction modes inside a cell has a
bounded Hermitian hopping representative.  Nonopposite pairs use one internal
face.  Opposite pairs use a two-edge path through a nonopposite mode and its
local parity.  The maximum physical Pauli support is 7 at both sizes.

Every representative commutes with the stabilizers and with the full gauge
algebra, and anticommutes with exactly its two target mode parities.  Therefore
the ten Cycle-523 primitive Givens factors can be lifted within the matter
factor, and the onsite coin does not require a shadow recode.  The 15 contact
parity-pair words have support at most 12 and also act as gauge identity.

The runner re-executes the Cycle-523 onsite and Cycle-230 seam comparators.  It
retains the one-particle mass, `g=0.37` contact, inverse, leakage, and seam
values conditionally through the faithful matter factor.  It does not
enumerate the `2^(22N)` physical matrix and does not claim that the old
Cycle-523 literal two-M2 schedule has already been transplanted to the face
code.  A bounded Pauli-block synthesis exists as compiler work, but its exact
one-/two-M2 list is not frozen here.

## Local constraints, physical placement, and covariance

The bounded constraints consist of the rough square-pyramid elementary loops
and one cell constraint per coarse cell.  Their maximum weight is 28,
independent of size.  The three Wilson initializers are deliberately excluded
from that description.

An explicit period-32 placement uses:

```text
terminal:                    32x,
six spokes:                  32x + 4 D_d,
twelve internal faces:       32x + 2(D_a+D_b),
three owned outer faces:     32x + 16 D_(+axis).
```

L5 and L6 have no collisions.  The maximum physical L1 diameters are 64 for a
bounded local constraint, 32 for a matter generator, 40 for a gauge
generator, and 32 for one B block.  These values are constant in L.

The fixed all-plus Wilson code, matter algebra, explicit gauge algebra, role
placement, and local framing corrections transform into themselves under all
24 proper-cubic frames.  The runner also checks the exact action on every
face `X/Z` generator for all 576 frame products: 684,288 L3 generator cases,
zero mismatches.  This is one fixed covariant code, not an abstract 24-chart
orbit and not a compile-time or runtime chart selector.

## Preparation and the topological boundary

The local constraints alone have rank `15N-2`.  Relative to the fixed target,
their matter quotient contains exactly three additional central spin
characters:

```text
local-only matter quotient dimension = 12N+2,
fixed-target matter quotient dimension = 12N-1.
```

Adding the three all-plus Wilson initializers removes exactly those three
characters.  Their maximum physical weights grow from 33 at L5 to 39 at held
L6.  No local constant-depth circuit, local dissipative rule, measurement and
feed-forward protocol, or autonomous gauge-sector formation law is supplied.

The unfixed-Wilson commutant audit is explicit.  With bounded checks only, the
matter quotient has dimension/rank `12N+2 / 12N-2`, hence a four-dimensional
radical: target total parity plus three Wilson characters.  Its full
commutant has dimension/rank

```text
L5:       252 / 248,
held L6:  434 / 430,
law:      (2N+2) / (2N-2),
```

and radical dimension four.  The bounded sink gauge generators together with
the three Wilson words span that complete commutant.  There is no Pauli
operator that both commutes with the complete mapped matter algebra and
anticommutes with any Wilson: each Wilson is itself a central member of the
matter algebra.  Thus the rough terminal changes Cycle 269's extensive
multiplicity conclusion—the `N-1` sector is now a genuine local gauge
factor—but it does **not** change Cycle 269's abelian-versus-`M8` conclusion
for the three topological characters.  Their anticommuting membrane partners
still act nontrivially on matter and cannot be called gauge-only conjugates.

The initialization is typed as:

```text
prepare any lawful rough-code state in the proper-cubic-invariant all-plus
spin sector; the N-1 gauge subsystem may be arbitrary.
```

The runtime never reads, branches on, or changes a Wilson sign.  Thus it is
not a global sector selector.  Nevertheless, supplying the initialized sector
is nonlocal preparation structure, so the campaign's unconditional local `E`
has not yet been completed.

## Deletion, leakage, and inverse controls

- Removing the two rough-terminal `X` factors from one matter stream produces
  exactly two cell-constraint violations; the dressed stream produces zero.
- Removing the left spoke factor from one gauge hop produces six matter-
  commutator failures; the complete gauge hop produces zero.
- Removing one independent Wilson initializer lowers the fixed rank by one
  and re-admits a twisted central character.
- The redundant displayed local family is distinguished from an independent
  local basis; deletion of an independent row adds one code direction.
- Deleting the fourth FSWAP polynomial term gives matrix residual 1.
- Perturbing an active phase by `1e-4` gives
  `|exp(i 1e-4)-1|=9.999999995833334e-5`.
- Every mapped matter factor commutes with all code constraints and the gauge
  algebra, so ideal code leakage and gauge transition are zero.
- Each FSWAP squares to identity and the complete involutive B product has an
  exact inverse.

No copied terminal, gauge, or Wilson value is called a Record.

## Supplied structure and novelty boundary

Supplied rather than derived are the square-pyramid puncture graph, 22 role
locations per cell, local incident-edge framing Clifford, period-32 origin,
three all-plus Wilson/spin signs, their initialized topological state, the
Cycle-219 coin, Cycle-230 contact and factor order, and finite periodic
domains.

Not supplied are a site-major `A/AP` field, global parity callback, arbitrary
gauge-state selector, runtime frame choice, or runtime sector query.  No
physical duration, energy, Record, source, gravity response, or Born rule is
inferred.

Cycle 235 and the cited Chen/Chen-Kapustin construction are prior art for the
local total-even face algebra.  Cycle 247 is prior work for the rough-terminal
both-parity algebra and its `N-1` multiplicity.  Cycle 532's new
fixture-specific content is:

1. the explicit bounded `Zg/Ag` commutant generators;
2. their exact all-size incidence and matter-commutant checks;
3. the L5/L6 full-commutant exhaustion and sectorwise tensor-factor theorem;
4. the common-center equality and both-parity census;
5. the direct relation to Cycle 529's exact full-Fock B target;
6. the bounded onsite Givens/contact compatibility audit; and
7. the all-24/576 fixed-code gauge covariance and period-32 placement.

No new general bosonization theorem or global novelty priority is claimed.
Thirring machinery is not used or compared.

## Dependency disposition

- `C_ref`: advances.  The site-major `A/AP` chart and active frame chart are
  absent from the physical presentation.  The square-pyramid framing,
  period-32 origin, and three spin signs remain supplied.
- `C_num`: advances.  Both target total-parity sectors and the exact `6N`
  target factor are present; the gauge multiplicity is now typed and counted.
- `C_wrap`: unchanged except for a sharper boundary.  Three Wilson signs are
  initialization data, not time, energy, winding history, or Records.
- `C_int`: advances conditionally.  Full-Fock B, all onsite Givens, contact,
  inverse, and the logical mass/seam comparators lie in the faithful matter
  factor.  Primitive two-M2 face-code schedules and autonomous preparation
  remain open.
- `C_local`: major advance.  Bounded local constraints, 22 M2/cell, explicit
  local gauge generators, full commutant factorization, fixed-code cubic
  covariance, and bounded B blocks close conditional on topological init.
- `C_source`: unchanged.

There is no shared obstruction and no axiom pressure.  Framework maturity
scores are not changed by this representation result alone.

## No-go discipline N1–N8

Broad no-go gate status: **FAIL / DO NOT SHIP**.  The disposition is
`partial-attempt-with-named-untested-routes`.  The current negative is only
that this displayed periodic face presentation has not locally prepared its
three fixed Wilson signs.

### N1 — alternative-route normalization

| family | object / mechanism / terminal obligation | status |
|---|---|---|
| rough-terminal subsystem | punctured face code / explicit sink commutant / local or typed spin initialization | **ATTEMPTED — positive conditional** |
| local-only rough code | arbitrary Wilson sectors / sector-twisted matter center / one fixed target without a selector | **ATTEMPTED — three extra characters remain** |
| Cycle-529 double shadow | linear `An/APn` banks / stateful swap / bounded local preparation and fixed chart | **ATTEMPTED BY PRIOR — runtime exact, chart nonlocal** |
| closed higher-form code | face flux / modified Gauss law / full odd-parity state domain | **ATTEMPTED BY PRIOR — even sector only** |
| distributed prefix code | local Clifford prefix field / bounded preparation / closing CAR exchange | **ATTEMPTED BY PRIOR — state local, closing exchange grows** |
| vertex-gamma/GSE | local Clifford gammas / loop quotient / coherent full-parity join | **ATTEMPTED BY PRIOR — local algebra, sector/rank split** |
| measurement/dissipative spin preparation | local checks plus outcomes/reset / autonomous topological initialization / bounded-depth or convergent preparation theorem | **OPEN — NOT CLOSED** |
| open or dynamically punctured topology | local rough boundaries / spin-character retirement / homogeneous periodic compiler | **OPEN — NOT CLOSED** |

These families differ in object, mechanism, and terminal obligation.  The open
preparation and topology routes forbid a general negative.

### N2 — wall-independence audit

Raw labels such as Wilson selection, stabilizer-state preparation, and
fixed-spin encoding collapse to one wall:

```text
W_topological-encoding:
prepare or autonomously form the fixed proper-cubic spin sector and its
code-space isometry using bounded local physical operations.
```

Closing that wall supplies the three signs and the initialized face code, so
they are not counted independently.  Site-major chart locality, gauge
multiplicity, matter/gauge factorization, B runtime, onsite recode, and
fixed-code covariance are closed in the conditional construction and are not
residual walls.  Literal one-/two-M2 optimization of a bounded 13-site block
is downstream compiler work, not an independent physics obstruction.

### N3 — hidden-wall scan

The mandatory phrase scan covers “we assume,” “by construction,” “as is
standard,” “the framework provides,” “bridge context,” “background,”
“naturally,” “obviously,” “standard QFT,” “registered,” and “canonical.”  No
such phrase discharges an obligation.  The square-pyramid graph, rough
terminal, framing repair, all-plus Wilson signs, topological state, macro
origin, target coefficients, and off-code/primitive synthesis are explicit in
the supplied inventory.  “Fixed” always names a tested spin sector, not a
hidden runtime lookup.

### N4 — residual matching

| witness | witness residual | Cycle-532 use | match? |
|---|---|---|---:|
| Cycle 235 | bounded even face algebra but odd target sector absent | rough terminal carries both matter parities | yes for the parity repair |
| Cycle 247 | exact rough matter algebra with `N-1` untyped multiplicity | explicit commutant factorization types exactly that multiplicity | yes |
| Cycle 269 | three unfixed Wilson characters twist one fixed finite-torus target | local-only rough code also has three extra matter characters | yes for the topological boundary |
| Cycle 529 | exact recurrent full-Fock B target but nonlocal charted encoding | same `Gamma(P)` is represented in the faithful rough matter factor | yes |
| Cycle 523 | onsite Givens/contact logical factors | bounded matter words test the same onsite pairs | yes for compatibility, not literal schedule reuse |
| Cycle 530 selected seam | one bounded braid does not tile to full B | not used as negative evidence | no; dropped |

No route-specific endpoint or translated-braid failure is cited against the
rough subsystem construction.

### N5 — rhetoric audit

| resolution | tested result |
|---|---|
| one physical M2 role | fixed frame action and placement |
| one local check | weight at most 28 and bounded diameter |
| one gauge generator | weight 6 or at most 18; exact commutators |
| one B edge | exact FSWAP polynomial, support at most 13 |
| one two-cell patch | all 4,096 Fock inputs exact |
| straight/corner three-cell patch | all 988 N<=3 inputs exact |
| L5/held L6 | complete N<=2 target census and exact subsystem ranks |
| all Fock sectors | quadratic target theorem plus faithful matter representation |
| fixed code covariance | all 24 frames and all 576 products |
| local-only arbitrary Wilson code | three extra central characters; not one fixed target |
| bounded preparation of the fixed sector | not tested successfully; no closure claimed |

Accordingly “not locally prepared” refers only to this fixed-spin periodic
presentation.  It is not widened to a statement that topological or gauge
initialization cannot be local under any mechanism.

### N6 — partial-closure path

This cycle follows the import-retirement shape.  It takes the explicit three-
Wilson initialization, proves the target-times-gauge factor theorem and the
bounded update theorem, and leaves a preparation audit for the imported
state.  Candidate retirement mechanisms are a bounded measurement/reset
protocol, autonomous dissipative code formation with a convergence theorem,
a topology/puncture refinement whose local cycles span the relevant twists,
or an operational quotient proved sufficient for the declared finite-light-
cone experiments.  None requires an axiom edit merely because it is open.

### N7 — hostile steelman

> A hostile reviewer should reject any claim that the three Wilson signs are
> an inherent nonlocal obstruction.  The runner has proved only that the
> displayed periodic stabilizer presentation needs three growing initializer
> words when prepared by direct projection.  It has not tested local
> measurement with reset, dissipative stabilization, an enlarged puncture
> complex whose bounded faces kill the twists, or a finite-light-cone quotient
> in which arbitrary spin sectors are operationally equivalent.  The new
> bounded sink gauge algebra is itself an actionable carrier for such a
> protocol.  The terminal obligation is to construct and verify one of those
> initializers, not to add an axiom.

The steelman is concrete and blocks a broad no-go.

### N8 — cross-cycle echo

Cycle 235 moved Jordan-Wigner nonlocality into a face-code spin sector.  Cycle
247 made both matter parities local but left boundary multiplicity untyped.
Cycle 269 showed that three Wilson labels in the unpunctured local-only code
are twisted target sectors, not gauge qubits.  Cycle 263 separately showed
that local state preparation and local CAR gates can close in different
encodings.  Cycle 529 found an exact stateful B cocycle but kept a global
chart.  Cycle 532 now retires the rough multiplicity and the B chart together,
while exposing only the topological encoding/init obligation.

Earlier apparent global walls were repeatedly narrowed by adding a relational
carrier or changing the code presentation.  The same mechanism remains live
for the three spin signs.  Therefore no axiom pressure follows.

## Disposition and next campaign

Retain Cycle 532 as the strongest local gauge compiler candidate:

- exact full target Fock factor with both parities;
- explicit N-1 gauge subsystem rather than excess multiplicity;
- bounded local constraints and generators;
- exact full-Fock B action and onsite compatibility;
- fixed-code all-24/576 covariance;
- no site-major chart or runtime parity/sector service; and
- one isolated typed topological initialization boundary.

The optimal next campaign is a direct preparation tournament for the three
all-plus spin signs on this exact rough code.  Compare local measurement/reset,
autonomous dissipative stabilization, and a locally filled puncture complex.
Require a literal bounded protocol or a proved convergence/light-cone theorem,
then rerun the complete factorization, B, Givens/contact, inverse, leakage,
deletion, L5/L6, and all-frame certificate.  Do not revisit `A/AP` chart
factorizations unless they supply a new mechanism for this preparation wall.
