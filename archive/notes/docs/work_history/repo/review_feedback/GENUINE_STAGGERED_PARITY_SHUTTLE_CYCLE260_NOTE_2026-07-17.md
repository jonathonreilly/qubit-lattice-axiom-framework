# Genuine staggered parity shuttle — Cycle 260

**Date:** 2026-07-17

**Type:** constructive phase-indexed Fock-ordering attempt with an autonomous
local parity-shuttle implementation and bounded-grammar discriminator

**Status:** exact dynamical exchange-sign transport constructed; bounded
size-independent physical macro-update and autonomous phase-marker preparation
remain open

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/genuine_staggered_parity_shuttle_cycle260_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface.

## Result up front

The original route-3 request has now been instantiated as a **genuine
staggered/dynamical parity shuttle**. It is not Cycle 249's static coherent
frame schedule under another name.

The constructive device is a **phase-indexed Fock ordering** carried by
physical shuttle registers, not a host-side change of notation.

The Cycle-230 stream has two perfect matchings:

```text
A: reverse-direction pairs inside each coarse cell,
B: outer-edge pairs between neighboring coarse cells.
```

Their union decomposes into `3L^2` alternating cycles, each of length `2L`.
On every cycle, choose phase-A Fock order

```text
(v_0,v_1,v_2,...,v_(2L-1)),
```

so every A pair is adjacent. The phase-B order is its one-site rotation

```text
(v_1,v_2,...,v_(2L-1),v_0),
```

so every B pair is adjacent. Changing between the two orderings requires the
exact Fock sign

```text
D(n) = (-1)^[ n_0 * (n_1+...+n_(2L-1)) ].
```

The runner exhausts all basis states and active B edges through held-out
`L=6`. Conjugating an adjacent two-mode FSWAP by `D` reproduces the intrinsic
fermionic transposition with **zero failures** over:

| `L` | cycles | cycle length | basis/edge tests | failures |
|---:|---:|---:|---:|---:|
| 3 | 27 | 6 | 5,184 | 0 |
| 4 | 48 | 8 | 49,152 | 0 |
| 5 | 75 | 10 | 384,000 | 0 |
| 6 held out | 108 | 12 | 2,654,208 | 0 |

This is a real constructive result: phase-indexed ordering can remove the
exchange string algebraically, and a moving ordinary-M2 accumulator can
compute the required sign using only bounded local microsteps.

It does **not** close the physical compiler. The explicit shuttle needs

```text
2(2L-1)+1 = 4L-1
```

local transport/phase/uncompute factors per ordering transition, giving
`11,15,19,23` at `L=3,4,5,6`. Its causal light cone and macro-update depth grow
with the held size. Calling the phase change a host relabeling would hide this
exact physical cost.

The shuttle also needs one seam/head and an orientation on every alternating
cycle. Nearest-neighbor head exclusion does not enforce that sector: at cycle
lengths `6,8,10,12`, it allows respectively `11,38,112,309` multi-head states,
as well as the zero-head state. Local phase equalities leave one global
stagger logical. A fixed orientation branch reverses under 324 of the tested
frame/cycle images; covariance is restored only when an explicit orientation
carrier transforms with the cycle.

Thus the construction supplies one fixed local microstep rule, bounded
support, and constant M2 overhead, but not a bounded size-independent
`G_physical` satisfying the original macrostep contract. The one-seam,
orientation, and synchronized stagger sector remain supplied preparation
data. This is a failure of the **exact grammar** tested here, not a general
staggered-compiler no-go. Distributed gauge encodings, bounded Clifford/gamma
registers, measurement/reset, open boundaries, and other dynamical codes
remain live. There is no shared obstruction and no axiom pressure.

| campaign clause | Cycle-260 disposition |
|---|---|
| bounded full-Fock `E` | open; phase-indexed state convention and marker preparation are not one bounded isometry |
| one bounded `G_physical` | fails in this grammar; only the microstep is bounded, while the transition has `4L-1` factors |
| locally enforced phase constraints | partial; local equalities/exclusions leave global phase and head sectors |
| no global parity/order service | fails in this grammar; the seam/orientation sector supplies a Fock cut |
| all 24 proper-cubic frames and coarse translations | exact for the joint schedule/marker descriptor family; no completed macro-unitary is claimed |
| mass/contact/seam | predecessor targets only; physical intertwining not reached |
| leakage/deletion/held size | exact through held-out `L=6` |
| supplied structure | inventoried explicitly below |

## 1. Explicit ordinary-M2 architecture

For each of the six Cycle-230 mode vertices in a coarse cell, the candidate
uses nine ordinary physical M2 roles:

| register | role |
|---|---|
| `M` | matter occupation |
| `P` | moving parity accumulator |
| `H` | moving head flag |
| `O` | fixed seam/origin marker for that cycle |
| `D` | cycle-orientation / forward-reverse flag |
| `S` | even/odd bond-stagger flag for the partitioned local rule |
| `R_0,R_1` | collect / phase / uncompute stage |
| `Q` | A/B ordering phase |

The census is therefore

```text
9 M2 per mode x 6 modes = 54 ordinary physical M2 per coarse cell.
```

This is constant overhead. A B step lies on one Cycle-252 outer edge. An A
step joins opposite directions in one cell; those vertices have graph
distance two through any transverse pyramid, so the maximum microstep radius
is two. No global Jordan-Wigner string is applied as one gate.

The candidate local constraints are:

1. nearest-neighbor exclusion for `H` and `O` on each alternating cycle;
2. local equality/checkerboard conditions for the phase and bond-stagger
   registers;
3. `P=0` at completed phase boundaries;
4. a head may move only on the bond selected by `S`;
5. a phase flip may occur only after the head returns to its seam with `P`
   uncomputed; and
6. the orientation bit reverses with a proper-cubic frame that reverses the
   alternating cycle.

Items 1 and 2 do not uniquely prepare the required global sector. That failure
is measured rather than hidden.

## 2. One fixed autonomous local phase rule

The law candidate is a partitioned reversible microstep, not a host gate
list. On an active oriented bond `(j,j+1)` carrying the head:

```text
COLLECT:
    CNOT(M_(j+1) -> P_j)
    SWAP(P_j,P_(j+1))
    SWAP(H_j,H_(j+1))
    toggle the local bond stagger

PHASE at the closing bond:
    CZ(M_seam,P_head)
    reverse D and enter UNCOMPUTE

UNCOMPUTE:
    SWAP(H_j,H_(j-1))
    SWAP(P_j,P_(j-1))
    CNOT(M_j -> P_(j-1))
    toggle the local bond stagger

RETURN:
    require H=O and P=0
    toggle Q between A and B.
```

All factors act on bounded ordinary-M2 neighborhoods. `S,R,D,H,O` make the
rule autonomous at the register level: no classical host chooses the next
edge or inserts the sign. Repeated application of the same local rule moves
the head, accumulates the parity, applies the phase, and reversibly cleans the
work register.

For a cycle word `n`, the forward sweep obtains

```text
P = n_1 xor ... xor n_(2L-1),
```

and the closing `CZ` gives the required `D(n)`. The reverse sweep restores
`P=0`. Exhaustive finite tests give zero phase and uncompute failures through
held-out `L=6`.

The phrase “one fixed local rule” must not be confused with a bounded macro
compiler. One ordering transition completes only after `4L-1` local factors.
Consequently

```text
G_physical(L) = U_microstep^(4L-1) ...
```

has a size-growing light cone. Although the head detects return locally, the
map identified with one Cycle-230 macrostep is not a size-independent bounded
neighborhood update.

## 3. Exact phase-indexed FSWAP identity

Let `i<j` be the positions of two modes in phase-A order. The intrinsic
fermionic transposition sign is

```text
(-1)^[ n_i n_j + (n_i xor n_j) sum_(i<k<j) n_k ].
```

Every B pair is adjacent in phase-B order, where its local gate has only the
ordinary FSWAP occupied-pair sign `(-1)^(n_i n_j)`. If `n'` is the occupation
word after swapping that B pair, the runner checks exactly

```text
D(n) (-1)^(n_i n_j) D(n')
  = intrinsic fermionic transposition sign
```

on every basis state of every alternating cycle at `L=3,4,5,6`.

This positive identity is why the route is worth retaining. The sign problem
has moved from the active matching gate into a typed physical ordering
transition; it has not been dismissed by relabeling.

The route does not yet furnish a full global Fock `E`. In particular, the
axis-cycle order must still be integrated with the six-mode onsite coin,
which mixes direction modes belonging to different alternating cycles. That
integration is downstream of the already failed bounded transition and is not
inflated into a separate impossibility wall.

## 4. Phase-marker preparation audit

### One-seam/head sector

The locally natural marker rule forbids adjacent heads. On a periodic cycle it
does not impose exactly one head:

| cycle length | locally allowed words | zero-head | one-head | multiple-head |
|---:|---:|---:|---:|---:|
| 6 | 18 | 1 | 6 | 11 |
| 8 | 47 | 1 | 8 | 38 |
| 10 | 123 | 1 | 10 | 112 |
| 12 | 322 | 1 | 12 | 309 |

The exact-one condition is a global number sector for this grammar. A product
state with a named seam is preparable, but it supplies a cut and breaks the
unmarked translation orbit. A uniform coherent one-head state removes the
classical cut only by requiring a cycle-wide W-state preparation. Neither is
derived by the displayed local constraints.

### Synchronized stagger phase

Put one phase M2 at each coarse cell and impose local equalities on all coarse
nearest-neighbor edges. Their ranks are:

| `L` | phase M2 | local equality rank | surviving global phase logical |
|---:|---:|---:|---:|
| 3 | 27 | 26 | 1 |
| 4 | 64 | 63 | 1 |
| 5 | 125 | 124 | 1 |
| 6 held out | 216 | 215 | 1 |

The constraint family enforces synchronization but does not choose which A/B
phase is realized. A supplied product `Q=0` convention is bounded to prepare
once it is selected; the law does not select that convention. Deleting one
independent equality admits one additional desynchronized logical direction.
Therefore the **stagger variable remains supplied**.

### Orientation and frames

The unoriented alternating-cycle family is carried into itself by all 24
proper-cubic frames and coarse translations. A fixed orientation is not: the
runner finds 324 frame/cycle reversals at `L=3`. With `D` transformed as an
orientation carrier, the joint family has zero frame or translation failures.

This is covariance of the full supplied marker grammar. It is not autonomous
preparation of an orientation sector. A macrostep may be covariant even when
its colored microphases permute under frames; Cycle 260 checks that joint
schedule/marker-family conjugacy. It does not claim frame conjugacy of a
bounded macro-unitary, because no such unitary closes in this grammar.

## 5. Bounded-support and deletion controls

The positive and negative controls are separated:

- every microstep has graph radius at most two and uses constant register
  overhead;
- the exact macro transition has `4L-1` local factors, so its support/light
  cone is not bounded independently of `L`;
- on held-out `L=6`, occupy the seam mode and position 6. Deleting that remote
  parity pickup changes the exact phase from `-1` to `+1`, giving state-vector
  residual `2`;
- deleting the reverse uncompute leaves `P=1`, a unit leakage probability on
  the named basis state;
- deleting one independent phase equality adds a desynchronized phase
  logical;
- deleting the exact-one marker preparation admits zero-head and multi-head
  histories; and
- replacing local FSWAP by ordinary SWAP deletes the occupied-pair minus sign,
  the same residual-`2` exchange control retained from Cycle 230.

No failed branch is repaired by postselection, a host scheduler, or a silent
parity query.

## 6. Fixed update and fixture firewall

The target remains

```text
G_coarse = W_0.37 Gamma(S C_(beta=-0.3)),
beta=-0.3,
g=0.37.
```

The predecessor rest mass is `0.4534056541748851`, and the Cycle-230 principal
`L=3` sea rank is 73. Contact remains identity on the zero- and one-particle
sectors. The seam fixture remains the predecessor target.

The exact phase-indexed FSWAP identity closes only the exchange-sign
subproblem. Because the ordering transition is not a bounded size-independent
physical macro-update and the marker sector is not autonomously prepared, the
runner does **not** synthesize or claim one fixed bounded `G_physical` for the
actual coin/A-B FSWAP/contact word. It also does not claim physical
one-particle mass or rank-73 seam intertwining.

This is unfinished integration after a scoped candidate failure, not evidence
that the matrices, mass mechanism, contact, or seam fail.

## 7. Three-dimensional, Record, and time firewall

The Cycle-252 branching graph and cubic `Z^3` placement are supplied spatial
structure. This route does not derive three dimensions. Proper-cubic
covariance is not a Lorentz or boost theorem.

`Q,S,R,D,H,O,P` are coherent/reversible compiler registers. They are not
actualized, permanent, readable framework Records. Head motion, microstep
count, A/B phase, bond stagger, runner duration, and the `4L-1` depth are
compiler resources. **Compiler phases are not physical time.**

Cycle 255's physical-close deletion remains open: a completion Record must
fail to form when the physical update is deleted. Cycle 260 supplies no
Record-formation law, physical close, duration, metric normalization, rate,
energy, lapse, Born weight, actualized history, source, or gravity response.

Wrapped phase is not physical energy. A generator element is not a rate. A
moving parity bit is not a Record.

## 8. Supplied-structure inventory

The candidate supplies or inherits:

1. the Cycle-230 six-mode CAR cell, fixed A/B stream factorization, occupation
   basis, and update order;
2. `beta=-0.3`, `g=0.37`, the principal sea branch, mass target, and seam
   target;
3. the Cycle-252/square-pyramid physical mode placement and its outer edges;
4. one alternating-cycle decomposition of the two stream matchings;
5. phase-A and phase-B Fock ordering conventions;
6. one seam/head sector and an orientation on every alternating cycle;
7. the nine ordinary-M2 register roles per mode;
8. the partitioned local microstep truth table and checkerboard bond stagger;
9. a synchronized initial A/B phase and clean work registers;
10. periodic sizes `L=3,4,5` and held-out `L=6`;
11. all 24 proper-cubic frame actions and tested coarse translations; and
12. classical enumeration adequate to exhaust all displayed basis tests.

The framework does not derive the ordering, seam, orientation, stagger phase,
register preparation, update law, or parameter choice here.

## 9. Prior-art and novelty boundary

This cycle directly uses the dynamic-ordering idea, so the relevant bounded
prior art is explicit:

- Bravyi and Kitaev, *Fermionic quantum computation*, Annals of Physics 298
  (2002), arXiv:`quant-ph/0003137`, Section 8, gives a constant-cost
  bounded-degree even-fermion simulation with edge qubits and cycle
  stabilizers. It restricts the displayed code to total even parity and
  separately exposes code-state preparation cost; it does not supply this
  campaign's odd one-particle/rank-73 full-Fock `E` or autonomous phase
  preparation.
- Pineda, Barthel, and Eisert, *Unitary circuits for strongly correlated
  fermions*, arXiv:`0905.0669`, uses time-adaptive Jordan-Wigner reordering as
  a computational circuit technique. That does not by itself make the
  ordering transition a fixed bounded physical law.
- Kivlichan et al., arXiv:`1711.04789`, uses fermionic swap networks for
  algorithmic simulation; its depth-growth setting is prior art for moving
  fermionic modes, not a proof of this physical compiler.

Cycle 260's fixture-specific contribution is the exact A/B-cycle phase
identity, the explicit physical head/accumulator register grammar, exhaustive
held-size sign test, marker-sector census, full-frame orientation audit, and
the `4L-1` transition residual. No general dynamic-Jordan-Wigner or swap-
network novelty is claimed. No Thirring machinery is used or compared.

## 10. TOE dependency ledger after Cycle 260

| workstream | Cycle-260 effect | remaining dependency |
|---|---|---|
| `C_ref` | exact sign is moved into explicit seam/orientation/stagger registers | autonomous one-seam/orientation/phase preparation, sea and macro roles remain supplied |
| `C_num` | both occupation parities are retained in the basis sign test | no bounded full-Fock physical `E` including the marker sector |
| `C_wrap` | cycle cut and orientation are explicit rather than hidden | unmarked winding/phase-sector preparation and realized history remain open |
| `C_int` | genuine gain: every B FSWAP sign is reproduced by an exact dynamical shuttle | bounded macro transition, full coin/A-B/contact `G_physical`, repeated law, and rate remain open |
| `C_local` | bounded radius-two microsteps, constant 54-M2/cell overhead, all-frame joint schedule-family covariance, held-size and deletion controls | macro light cone grows as `4L-1`; marker sector is global/supplied |
| `C_source` | unchanged | no energy/action/stress/source/gravity law selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.

## 11. No-go-discipline gate

The narrow negative under audit is:

> The declared phase-indexed A/B-cycle, one-head moving-accumulator grammar
> does not provide a bounded size-independent physical macro transition or a
> locally selected one-seam/orientation/stagger sector.

It is not a no-go for all staggered, dynamical, gauge, Clifford, or
measurement-assisted ordinary-M2 compilers.

### N1 — alternative-route enumeration

| route | honesty marker | exact disposition |
|---|---|---|
| keep one fixed A ordering | **ATTEMPTED** | A pairs are adjacent; the B seam retains the occupation-dependent exchange string |
| switch to the rotated B ordering | **ATTEMPTED** | all B pairs become adjacent and the exact FSWAP intertwiner passes |
| physical moving-accumulator transition | **ATTEMPTED** | exact phase and uncompute pass; macro factors grow `11,15,19,23` |
| bounded-window parity pickup | **ATTEMPTED** | omitted held-out position 6 gives exact residual `2` |
| nearest-neighbor one-head exclusion | **ATTEMPTED** | admits zero and multiple heads at every tested size |
| synchronized local phase equalities | **ATTEMPTED** | leave one global A/B stagger logical; deletion admits a domain direction |
| explicit orientation carrier | **ATTEMPTED** | repairs all-frame family covariance, but its sector preparation remains supplied |
| distributed Z2 prefix/gauge field | **LIVE, NOT RULED OUT** | could store the cut parity locally with a holonomy rather than a moving unique head |
| bounded Clifford/gamma or non-Pauli register | **LIVE, NOT RULED OUT** | altered auxiliary content lies outside this shuttle grammar |
| measurement/reset or open-boundary shuttle | **LIVE, NOT RULED OUT** | may form/remove a head without a periodic one-particle sector |

The positive exact reorder and live alternatives forbid a general no-go.

### N2 — condition-independence audit

The collapsed conditions for this exact grammar are:

- `K_transition`: a bounded size-independent physical implementation of the
  phase-order transition; and
- `K_marker`: local/autonomous preparation of the unique seam, orientation,
  and synchronized stagger sector.

Actual coin/A-B/contact synthesis and mass/seam intertwining are downstream
acceptance tests after those two conditions, not extra independent walls.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `K_transition`,`K_marker` | no: an exact shuttle still starts from a supplied head sector | no: a prepared head does not shorten the `4L-1` parity light cone | yes |

The onsite-coin/cross-cycle integration is unfinished downstream work. It is
not used to inflate the negative.

### N3 — hidden-condition scan

The phrases “by construction,” “background,” “canonical,” “the framework
provides,” “naturally,” “obviously,” “standard QFT,” “registered,” and close
variants were audited. No phrase supplies a hidden ordering transition. The
matching cycles, cut, orientation, phase convention, head number, stagger,
clean work state, macro completion rule, boundary, parameters, and frame
action all appear in the supplied inventory.

“Autonomous” refers only to repeated application of the fixed conditional
microstep after those registers are supplied. It does not mean autonomous
formation of their initial sector.

### N4 — residual matching

| witness | exact residual there | Cycle-260 use | match? |
|---|---|---|---:|
| Cycle 230 | intrinsic A/B FSWAP factorization and ordinary-SWAP sign failure | supplies the exact stream target and occupied-pair control | yes |
| Cycle 248 | endpoint shortcut residual `2 sqrt(2)` and `6L^2+4` fixed-order support | motivates a physical order transition rather than endpoint-only exchange | yes |
| Cycle 249 | colored coherent preparation is compiler scheduling, not time | firewall only; not evidence against the shuttle | no as negative witness |
| Cycle 252 | coherent sign carriers do not close ordinary-M2 incident CAR | altered-auxiliary context only | no as route-failure witness |
| Cycle 256 | radius-1 endpoint-star Pauli dressing leaves 972 incident failures | motivates a dynamical/nonstatic route; different grammar | no as negative witness |
| Pineda–Barthel–Eisert | dynamic reordering is a computational circuit resource | direct conceptual comparator for `K_transition` | yes, scope comparator |
| Kivlichan et al. | swap-network movement has algorithmic depth cost | direct depth comparator, not a lower-bound proof here | yes, bounded comparison |

The primary evidence is Cycle 260's own exhaustive phase identity, size law,
marker census, and deletion residuals.

### N5 — resolution and rhetoric audit

| resolution | tested | not established |
|---|---|---|
| one active B pair | exact conjugated FSWAP sign | full six-mode coin |
| one alternating cycle | all basis states through length 12 | arbitrary graph partition |
| one microstep | radius at most two, reversible register action | bounded macrostep |
| one ordering transition | exact `4L-1` shuttle | constant-depth alternative transition |
| marker constraints | nearest-neighbor exclusion and equality ranks | every possible local marker code |
| `L=3,4,5,6` | cycle census, exhaustive signs, marker counts, size law | thermodynamic no-go |
| all 24 proper frames | joint oriented-cycle family | Lorentz covariance |
| compiler phases | explicit A/B/stage registers | physical time or Records |

“The transition is not bounded” always means this exact moving-head grammar's
macro transition. “The marker is not locally enforced” means the displayed
nearest-neighbor exclusion/equality constraints, not every conceivable gauge
code.

### N6 — partial-closure path scan

| path | status | possible closure |
|---|---|---|
| distributed prefix-parity/gauge field | untested | replace the moving global sweep by locally stored phase relations |
| local Clifford/gamma port registers | live after Cycle 256 | realize incident signs with constant vertex content |
| Bravyi–Kitaev-style edge code plus explicit odd-sector join | bounded even prior art; odd preparation open | close even gates while separately solving all-parity `E` |
| coherent seam/orientation orbit | untested | remove a classical cut if bounded preparation/full abstraction can be proved |
| measurement/reset head formation | untested | select a one-head sector dynamically, with leakage/Record firewall |
| open rough boundary or charge sink | target change | terminate parity flow without a periodic seam |
| recurrent local cellular automaton with no macrostep identification | live law change | treat the microstep as fundamental dynamics rather than compiling one Cycle-230 step |

These are constructive import-retirement routes, not reasons for a new axiom.

### N7 — steelman

> A hostile reviewer should accept the exact phase-indexed identity and reject
> any broader negative. The growing `4L-1` sweep results from representing the
> Fock cut by one mobile head. A distributed Z2 gauge field can store prefix
> parities on every edge, and a bounded Clifford representation can attach
> mutually anticommuting gamma labels to the five ports of a Cycle-252 vertex.
> Bravyi–Kitaev already demonstrates constant-cost bounded-degree even-fermion
> gates once an edge-code sector is prepared. Coherent enlargement retired
> earlier reference choices in Cycles 249 and 252. Measurement/reset, an open
> charge sink, or a local odd-sector join could similarly remove the unique
> periodic head. None appears in the exact grammar tested here.

This steelman is convincing. It makes a universal staggered-compiler no-go
premature.

### N8 — cross-cycle echo

| earlier boundary | later mechanism | Cycle-260 response |
|---|---|---|
| fixed spectator exchange needs a growing string | phase-indexed ordering makes each active matching adjacent | retain the positive exact reorder |
| deterministic gauge representative fails | coherent frame orbit in Cycle 249 | keep coherent seam/orientation preparation live |
| marked odd reference charge | coherent charge orbit in Cycle 252 | do not call the current seam permanent |
| static endpoint-star dressing fails | radius-2 and dynamical routes left open in Cycle 256 | instantiate a genuinely dynamical route rather than echo the static failure |
| compiler depth mistaken for time | typed Record-DAG criterion in Cycle 255 | keep the `4L-1` factors as compiler cost only |
| rough multiplicity | auxiliary even-CAR subsystem in Cycle 251 | consider distributed subsystem/gauge storage next |

Prior representation changes have retired narrower walls. The same mechanism
remains live. N1–N8 passes only for the exact grammar statement and fails for
a universal no-go, minimum content, shared obstruction, or axiom pressure.

## 12. Route disposition and optimal next campaign

**Retain:**

- the exact A/B alternating-cycle decomposition;
- phase-indexed adjacent matching orders;
- zero-residual FSWAP conjugacy through held-out `L=6`;
- the explicit 54-M2/cell autonomous microstep architecture;
- exact parity pickup/uncompute and deletion controls;
- full joint schedule-family proper-cubic/coarse-translation covariance; and
- the phase-marker and stagger-preparation census.

**Do not claim:**

- a bounded size-independent `G_physical`;
- a locally prepared one-seam/orientation/stagger sector;
- a full-Fock physical `E`;
- actual physical mass/contact/seam reproduction;
- a Record, clock, physical time, rate, energy, source, or gravity result; or
- a shared obstruction or axiom conclusion.

The optimal next campaign is a distributed phase-field compiler. Replace the
unique moving head by local prefix/gauge relations on every alternating-cycle
edge, demand exact code rank for both parities, and search for bounded local
logical A/B FSWAPs whose loop products satisfy the CAR cycle identities.
Compare directly against the bounded-even Bravyi–Kitaev construction, but add
the missing odd one-particle/rank-73 state map, autonomous sector preparation,
all 24 frames, coarse translations, and the fixed `beta=-0.3`, `g=0.37`
coin/contact fixtures. If that route fails, scope the result to its exact
stabilizer/Clifford grammar and retask to measurement/reset or open-boundary
formation.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/genuine_staggered_parity_shuttle_cycle260_2026_07_17.py
```
