# Distributed phase-field CAR compiler — Cycle 263

**Date:** 2026-07-17

**Type:** constructive prefix-gauge state code and bounded edge-gauge CAR
comparator with an exact rank/locality/holonomy tournament

**Status:** exact full-Fock local preparation and exact bounded CAR incidence
constructed in different encodings; no common physical compiler closes

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/distributed_phase_field_car_compiler_cycle263_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface.

## Result up front

Cycle 263 replaces Cycle 260's unique moving parity head with a **distributed
phase field** on every edge of each alternating Cycle-230 A/B cycle. Two exact
ordinary-M2 stabilizer/Clifford grammars are tested.

The first, the **prefix-gauge code**, uses one matter `M_j`, one prefix `P_j`,
and one edge phase `T_j` per mode. Its local checks are

```text
C_j = Z_(M_j) Z_(P_j) Z_(P_(j+1)) Z_(T_j),
K_j = X_(P_j) X_(T_(j-1)) X_(T_j).
```

On a cycle of length `m=2L`, all `2m` checks commute and are independent on
`3m` M2 factors. The code exponent is exactly `m`, with even and odd sectors
of exponent `m-1`. It therefore has **exact full-Fock rank** and **both parity
sectors**. The encoding is a bounded three-role-layer Clifford circuit:

```text
P <- |+>, T <- |0>,
CNOT(M_j -> T_j),
CNOT(P_j -> T_j),
CNOT(P_(j+1) -> T_j).
```

No total-parity query, moving head, seam, or host controller occurs in this
state preparation. The overhead is three M2 per mode, or 18 M2 per coarse
cell.

The distributed field does not make the full CAR update local. Adjacent
logical two-mode gates have bounded support four, but the natural encoded
closing-edge hopping representative has weights

```text
L=3,4,5,6: 8,10,12,14 = 2L+2.
```

Dropping its intermediate parity on the named held-out state gives exact
residual `2`. Attempting to read one local `T` phase as the missing parity
anticommutes with two `K` checks and leaks from the code. Thus local
preparation and full rank close, while bounded cyclic CAR does not.

The second, the **edge-gauge comparator**, uses one M2 on every alternating-
cycle edge and defines weight-2 parity/hopping images

```text
B_j = Z_(e_(j-1)) Z_(e_j),
A_j = X_(e_j) Z_(e_(j-1)).
```

These operators satisfy the exact even-CAR incidence table: `A_j`
anticommutes with precisely `B_j,B_(j+1)` and with the two incident hoppings.
Their product around the cycle is a central weight-`2L` loop/holonomy
operator.

The unmarked code has exponent `2L-1` after fixing that loop and obeys

```text
product_j B_j = I.
```

It therefore represents only the even sector of **each isolated alternating
cycle**, which is narrower than the total-even sector of the connected
Cycle-252 graph. One marked parity M2 `h` can modify one `B` so that

```text
product_j B_j = Z_h
```

and restore exponent `2L`. But this adds a marked seam, breaks a fixed coarse-
translation branch, and retains the weight-`2L` holonomy condition. It also
does not yet provide the local inter-cycle parity transfers needed by the
onsite six-mode coin.

The exact result is therefore:

- distributed prefix constraints close full-Fock state rank and bounded local
  preparation but not the closing CAR exchange;
- the edge-gauge grammar closes bounded CAR incidence but only cycle-even
  rank, or full cycle rank after a marked/nonlocal repair; and
- no one encoding satisfies both clauses together.

This is a scoped failure of the **fixed stabilizer/Clifford grammar** tested
here. Non-Pauli encoders, measurement/reset, coherent marker formation, the
full connected bounded-degree edge code, and open boundaries remain live.
There is no shared obstruction and no axiom pressure.

## 1. Cycle geometry and lawful domains

As established in Cycle 260, the Cycle-230 reverse-direction matching `A` and
outer-edge matching `B` decompose the `6L^3` mode vertices into

```text
3L^2 alternating cycles of length 2L.
```

Every mode belongs to exactly one such cycle. A steps have bounded cell radius
two on the Cycle-252 square-pyramid graph; B steps are physical outer edges.
The prefix and edge fields are placed on these same bounded roles.

The runner uses periodic `L=3,4,5` and held-out `L=6`. It verifies the same
rank and support laws at all four sizes. The alternating cycles are
noncontractible around the periodic coarse torus, which is why their loop
condition has weight `2L` rather than bounded plaquette support.

## 2. Exact prefix-gauge full-Fock code

For one cycle of length `m`, use `3m` ordinary M2 factors ordered as

```text
M_0,...,M_(m-1), P_0,...,P_(m-1), T_0,...,T_(m-1).
```

The `C/K` checks have maximum weights four and three. Each `K_j` overlaps
`C_(j-1)` and `C_j` twice, so all checks commute. The exact rank census is:

| `L` | cycle length | physical M2 | check rank | code exponent | exponent in either fixed parity |
|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 18 | 12 | 6 | 5 |
| 4 | 8 | 24 | 16 | 8 | 7 |
| 5 | 10 | 30 | 20 | 10 | 9 |
| 6 held out | 12 | 36 | 24 | 12 | 11 |

Across all `3L^2` cycles, this gives `18L^3` physical M2 factors, `12L^3`
independent local checks, and code exponent `6L^3`, exactly the Cycle-230 full
occupation space.

### Encoding and logical operators

Starting from logical matter, `P` in product `|+>` states, and `T` in product
`|0>` states, the three CNOT role layers above conjugate the initial
stabilizers into `K_j,C_j`. The finite graph degree makes each role layer
parallel and bounded.

The encoded logical Pauli representatives are

```text
Zbar_j = Z_(M_j),
Xbar_j = X_(M_j) X_(T_j).
```

They commute with every `C/K`, have the exact logical Pauli pairing, and keep
the total matter parity

```text
P_m = product_j Zbar_j
```

independent of the stabilizer group. Fixing `P_m=+1` or `-1` reduces the code
by one exponent in either case. No parity sector is silently deleted.

This establishes a bounded full-Fock **state isometry** and local preparation.
It does not by itself establish that every fermionic operator has a bounded
image.

## 3. Bounded logical FSWAP and closing-edge discriminator

For adjacent positions in the declared cycle ordering, the two logical
qubits use only

```text
M_j,T_j,M_(j+1),T_(j+1).
```

Conjugating an ordinary two-logical-qubit FSWAP by the encoding circuit gives
an exact bounded logical FSWAP on that four-factor neighborhood with zero code
leakage.

The periodic closing edge is different. In a fixed Fock ordering, its exact
hopping generator contains the intermediate parity:

```text
Xbar_0 Zbar_1 ... Zbar_(m-2) Xbar_(m-1).
```

The displayed physical representative has weight `m+2=2L+2`. This is a
growing representative in the declared Clifford encoding, not a claimed
minimum over every possible non-Clifford code.

The endpoint-only shortcut is rejected exactly. At held-out `L=6`, occupy
positions 0 and 6 while leaving position 11 empty. Exchanging 0 and 11 has
intrinsic sign `-1` from the occupied intermediate mode; the endpoint-only
gate gives `+1`. The state-vector residual is `2`.

The tempting distributed repair is to multiply by a local edge phase `Z_T`.
That operator anticommutes with the two neighboring `K` checks. It exposes the
gauge representative rather than a gauge-invariant prefix and creates two
local constraint violations. The field stores parity relationally; one edge
value is not the missing global prefix observable.

Deleting one independent `C` or `K` lowers check rank by one and admits one
additional code direction. Omitting `CNOT(M_j -> T_j)` on an occupied input
likewise violates the corresponding `C_j`; the preparation layer is load
bearing.

## 4. Bounded edge-gauge comparator

The second grammar tests the opposite allocation of resources. Put one
ordinary M2 `e_j` on each alternating-cycle edge and define

```text
B_j = Z_(e_(j-1)) Z_(e_j),
A_j = X_(e_j) Z_(e_(j-1)).
```

For every `L=3,4,5,6`, the runner checks exactly:

- `A_j` anticommutes with `B_j` and `B_(j+1)` and no other `B`;
- `A_j` anticommutes with `A_(j-1),A_(j+1)` and no disjoint hopping;
- every `B` has weight two and every `A` has weight two; and
- the loop product commutes with the complete `A/B` family.

With the displayed orientation convention, the actual two-mode fermionic
swap is the exact local polynomial

```text
FSWAP_e = (B_u + B_v + i B_u A_e - i B_v A_e)/2.
```

The executable `4 x 4` matrix residual is zero. Its physical Pauli terms have
maximum weight three in the unmarked edge code and four when the marked
parity M2 lies at an endpoint. Thus the comparator closes an actual bounded
logical FSWAP, not merely a commutator table.

The loop product has one `Y`-type action on every edge, hence weight `2L`.
Fixing its Hermitian sign removes one exponent.

### Unmarked cycle-even code

With `2L` edge M2 factors and one loop condition, the exponent is `2L-1`.
Because every edge `Z` occurs twice,

```text
product_j B_j=I.
```

This is exactly the even sector of that one alternating cycle. Taking a tensor
product over all cycles would incorrectly fix every cycle parity even. The
Cycle-230 onsite coin mixes direction modes from different cycles while
preserving only total parity, so this tensor product is not the complete
total-even matter code.

### Marked full-rank comparator

Add one M2 `h` and replace one parity by

```text
B_0 -> Z_h B_0.
```

Then `product B=Z_h`, and after the same loop condition the exponent is `2L`,
with bounded `A` weight two and maximum `B` weight three. This restores the
cycle's missing parity slot algebraically.

The price is explicit:

- the chosen `B_0` is a marked seam;
- a fixed marker branch has 90 coarse-translation mismatches in the `L=3`
  test orbit;
- the loop condition still has weight `2L`; and
- a coin process that changes individual cycle parities would have to update
  the appropriate remote `h` registers or replace them with another local
  dynamical field.

Allowing the marker to transform gives a covariant family, not autonomous
marker preparation. Omitting the loop condition adds one Wilson logical.
Deleting the marked `Z_h` returns `product B=I` and removes the odd slot.

## 5. Direct Bravyi–Kitaev comparison

Bravyi and Kitaev, *Fermionic quantum computation*, Annals of Physics 298
(2002), arXiv:`quant-ph/0003137`, Section 8, is directly relevant and is used
only as bounded prior art.

Their bounded-degree edge-qubit construction supplies local `B/A` images and
cycle stabilizers for the even fermionic algebra. The displayed physical code
is total-even, and initial code-state preparation is a separate cost. That
result is the connected-graph analogue of the positive edge-gauge mechanism,
not a supply of this campaign's missing full-parity state map.

Cycle 263 does not claim a new general edge encoding. Its fixture-specific
contribution is:

1. the exact M/P/T full-rank prefix code on the Cycle-230 matching cycles;
2. its three-role-layer bounded preparation and both-parity census;
3. the exact weight `2L+2` natural closing representative and residual-2
   shortcut control;
4. the two-violation local phase-read discriminator;
5. the degree-two edge-code rank/holonomy comparator through held-out `L=6`;
6. the marked-parity repair and its translation audit; and
7. the explicit demonstration that these two positive closures belong to
   different encodings and cannot be feature-spliced.

The Bravyi–Kitaev even code does not supply an odd one-particle/rank-73
full-Fock `E`, a selected holonomy sector, the Cycle-230 onsite coin/contact,
or autonomous physical preparation. No global novelty priority is claimed.
No Thirring machinery is used or compared.

## 6. Covariance and supplied orientation

The unmarked alternating-cycle descriptor family maps into itself under all
24 proper-cubic frames and tested coarse translations with zero family
failures. Frames reverse 324 oriented `L=3` cycle images. The prefix checks and
edge `A` convention are carried to their framed counterparts by a bounded
orientation/framing Clifford repair.

This is exact covariance of the unmarked code family, not autonomous
selection of one orientation field. The marked `h` extension has a covariant
orbit only when its marker transforms as supplied data; a fixed marker branch
breaks coarse translations.

No frame result is a boost or Lorentz theorem. The three-dimensional cubic
lattice remains axiomatic input.

## 7. Contract disposition

| campaign clause | prefix code | edge-gauge comparator |
|---|---|---|
| constant overhead | closed, 18 M2/cell | closed per edge role; marked extension adds one per cycle |
| exact full-Fock rank | **closed** | cycle-even unmarked; full cycle rank only after marked `h` |
| both parity sectors | **closed** | marked comparator only |
| locally enforced bounded checks | **closed** | local `A/B`; holonomy weight `2L` |
| bounded A/B FSWAP/CAR | adjacent only; closing edge fails | **closed** incidence algebra |
| no global JW/reference service | state preparation yes; closing update no | unmarked even only; marked repair supplies seam |
| all 24 frames / translations | unmarked family closed up to bounded framing | unmarked family closed; fixed marked branch fails |
| actual beta/contact/mass/seam | not reached | not reached |
| deletion/leakage/held size | closed | closed |

No column closes the full requested compiler, and clauses may not be borrowed
between columns.

## 8. Fixed update and fixture firewall

The target is unchanged:

```text
G_coarse = W_0.37 Gamma(S C_(beta=-0.3)),
beta=-0.3,
g=0.37.
```

The predecessor rest mass is `0.4534056541748851`, contact is identity on the
zero- and one-particle sectors, and the Cycle-230 principal `L=3` sea rank is
73. The rank-73 seam remains a target.

The prefix code supplies the strongest state `E` in this cycle but not a
bounded full cyclic CAR update. The edge code supplies bounded local CAR
incidence but not the unmarked full-parity state space or local holonomy
preparation. Therefore the actual coin/A-B FSWAP/contact `G_physical`, mass,
contact, and seam intertwining are not synthesized or claimed in either
encoding.

Wrapped phase is not physical energy. A generator element is not a rate.

## 9. Deletion, leakage, and preparation controls

- Delete one independent prefix `C/K`: rank falls from `2m` to `2m-1`, adding
  one code direction.
- Delete the matter-to-edge CNOT: an occupied input violates its local `C`.
- Replace the closing string by endpoints only: the named state has residual
  `2`.
- Read one `T` edge as physical prefix parity: exactly two `K` violations.
- Delete the edge-code loop: one Wilson logical is admitted.
- Delete the marked `Z_h`: `product B` becomes identity and the odd slot is
  removed.
- Keep the marked `Z_h` but translate a fixed marker pattern: the branch does
  not map to itself.

No deletion is repaired by postselection, host parity lookup, or borrowing a
different encoding's constraint.

## 10. Supplied-structure inventory

Cycle 263 supplies or inherits:

1. the Cycle-230 A/B alternating-cycle decomposition and occupation basis;
2. one oriented edge role per alternating-cycle step;
3. the M/P/T register placement and `C/K` stabilizer signs;
4. product `P=|+>`, `T=|0>` initialization and the three CNOT role layers;
5. one declared Fock ordering for the logical closing-edge test;
6. the edge-gauge `A/B` orientation convention and Hermitian loop sign;
7. one marked parity M2 and marked `B_0` only in the comparator branch;
8. periodic `L=3,4,5` and held-out `L=6`;
9. proper-cubic framing repairs and tested coarse translations;
10. `beta=-0.3`, `g=0.37`, mass, principal sea, and seam targets; and
11. ordinary complex quantum mechanics, tensor composition, and classical
    stabilizer enumeration.

No update law, parameter selection, marker formation, holonomy selection,
Record law, probability, time metric, source, or gravity response is derived.

## 11. Three-dimensional, Record, and time firewall

The distributed fields are compiler/gauge carriers. `P`, `T`, edge M2, and
the marked `h` are not actualized, permanent, readable framework Records.

The three CNOT role layers, orientation repair, edge colors, stabilizer
elimination, and runner duration are compiler resources. **Compiler schedules
are not physical time.** Cycle 263 supplies no occurrence law, physical close,
Record formation, causal duration, rate, energy, lapse, Born weight, realized
history, source, or gravity coupling.

Three-dimensional space remains axiomatic. Code covariance under the 24
proper-cubic frames is spatial covariance only.

## 12. TOE dependency ledger after Cycle 263

| workstream | Cycle-263 effect | remaining dependency |
|---|---|---|
| `C_ref` | moving head and seam are removed from the prefix state code | Fock cut reappears in closing exchange; marked edge repair and orientation remain supplied |
| `C_num` | exact full-Fock rank and both parity sectors close in the prefix code | same-encoding bounded CAR and physical number interpretation remain open |
| `C_wrap` | loop/holonomy cost is isolated exactly as weight `2L` | local/topological sector preparation and realized winding history remain open |
| `C_int` | bounded adjacent logical gates and exact bounded edge-code CAR incidence constructed | full coin/A-B/contact in one encoding, repeated law, and rate remain open |
| `C_local` | strong gain: 18-M2/cell local prefix preparation and a bounded-A/B comparator, all-frame family, deletion and held-size controls | closing exchange versus rank/holonomy tradeoff remains |
| `C_source` | unchanged | no energy/action/stress/source/gravity law selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.

## 13. No-go-discipline gate

The narrow negative under audit is:

> Neither of the two fixed stabilizer/Clifford grammars tested here combines
> locally prepared full-Fock rank with bounded cyclic CAR, local holonomy, and
> unmarked covariance.

It is not a no-go for all distributed gauge, non-Pauli, measurement-assisted,
or open-boundary fermion compilers.

### N1 — alternative-route enumeration

| route | honesty marker | exact disposition |
|---|---|---|
| local M/P/T prefix stabilizer code | **ATTEMPTED** | exact full-Fock rank, both parities, and bounded preparation close |
| bounded adjacent logical FSWAP in prefix code | **ATTEMPTED** | support four and zero code leakage for nonclosing edges |
| endpoint-only closing FSWAP | **ATTEMPTED** | held-out named state gives residual `2` |
| read one local `T` as the missing prefix | **ATTEMPTED** | anticommutes with two local `K` checks |
| unmarked edge-gauge code | **ATTEMPTED** | bounded exact `A/B`; fixes each alternating cycle even and needs weight-`2L` loop condition |
| marked parity-M2 edge code | **ATTEMPTED** | restores cycle rank; introduces marked seam, translation failure, and nonlocal holonomy |
| omit the loop stabilizer | **ATTEMPTED** | admits one uncontrolled Wilson logical rather than the target matter state |
| full connected Bravyi–Kitaev edge code plus odd join | **LIVE, NOT RULED OUT** | bounded total-even prior art; odd/full-state preparation remains to construct |
| non-Pauli or bounded Clifford/gamma subsystem | **LIVE, NOT RULED OUT** | outside the fixed CSS/Pauli grammars |
| measurement/reset or open-boundary gauge formation | **LIVE, NOT RULED OUT** | may select flux without a periodic marked seam |

The two positive but incompatible closures block a general no-go.

### N2 — condition-independence audit

The collapsed compiler conditions are:

- `K_state`: exact full-Fock/both-parity state map with bounded local
  preparation and no marked holonomy service; and
- `K_gate`: bounded correct CAR/FSWAP images in that same encoding.

Loop, covariance, deletion, mass/contact/seam, and held-size are acceptance
tests on the common candidate, not inflated independent physics walls.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `K_state`,`K_gate` | no: prefix code closes `K_state` but not the cyclic gate | no: edge code closes bounded `K_gate` but not unmarked full state | yes |

The full onsite-coin/inter-cycle integration is downstream after a common
state/gate code and is not counted as a third wall.

### N3 — hidden-condition scan

The phrases “we assume,” “by construction,” “background,” “canonical,” “the
framework provides,” “naturally,” “obviously,” “standard QFT,” “registered,”
and close variants were audited. The cycle decomposition, orientation,
logical ordering, product ancillas, check signs, loop eigenvalue, marked
parity site, boundary, parameters, and framing repair are explicit in the
supplied inventory.

“Full-Fock” refers to the exact state dimension and both logical parity
sectors of the declared occupation map. It does not imply that the complete
CAR operator algebra is bounded.

### N4 — residual matching

| witness | exact residual there | Cycle-263 use | match? |
|---|---|---|---:|
| Cycle 248 | full-rank spectator `E`, growing exchange | same state/locality tradeoff shape only | yes as comparator, not inherited proof |
| Cycle 251 | bounded even algebra, auxiliary state preparation open | same gate/state tradeoff shape only | yes as comparator, not inherited proof |
| Cycle 260 | one-head phase transition exact but depth `4L-1` and marker supplied | motivates distributed rather than mobile phase storage | yes |
| Bravyi–Kitaev Section 8 | bounded-degree even edge algebra and cycle stabilizers, total-even code | direct edge-gauge prior-art boundary | yes |
| Cycle 252 | coherent odd rank with three topological joins; ordinary-M2 CAR fails | topological/odd context only | no as negative witness |
| Cycle 256 | endpoint-star radius-1 Pauli grammar fails | different code and grammar | no as negative witness |
| Cycle 230 | beta/mass/contact/seam fixtures | retained targets, not negative evidence | no as negative witness |

Cycle 263's rank, residual-2, gauge-violation, loop-weight, and marker-
translation tests are the primary evidence.

### N5 — resolution and rhetoric audit

| resolution | tested | not established |
|---|---|---|
| one prefix check | exact commutation and deletion rank | every non-Pauli constraint |
| one adjacent logical edge | bounded support-four gate | periodic closing edge |
| one closing edge | natural string and endpoint/phase shortcuts | all bounded non-Clifford gates |
| one alternating cycle | exact rank, CAR incidence, and holonomy | connected degree-five graph compiler |
| all cycles at `L=3,4,5,6` | scaling laws and covariance descriptor family | thermodynamic no-go |
| marked odd repair | exact cycle rank and translation mismatch | coherent/dynamical marker formation |
| all 24 proper frames | code-family/framing covariance | boosts or Lorentz closure |
| compiler layers | bounded preparation schedule | physical time or Records |

Every negative is restricted to the displayed prefix or edge grammar.

### N6 — partial-closure path scan

| path | status | possible closure |
|---|---|---|
| connected degree-five Bravyi–Kitaev code with explicit odd join | prior even mechanism, campaign implementation open | avoid per-cycle parity fixing while retaining bounded CAR |
| coherent distributed parity background | untested | replace marked `h` by a reference-free orbit |
| dynamical local flux transfer during onsite coin | untested | update cycle parities without remote marked registers |
| non-Pauli local isometry | untested | evade fixed-Clifford support pullback |
| bounded gamma/Clifford port registers | live | supply five incident anticommuting labels per vertex |
| measurement/reset syndrome preparation | untested | select loop/holonomy sectors with explicit leakage audit |
| open rough boundary / charge sink | target change | terminate parity flux without a noncontractible loop |
| operational total-even quotient | constructive precedent | close restricted predictions without a full pure `E` if separately justified |

These are constructive import-retirement routes, not new-axiom conclusions.

### N7 — steelman

> A hostile reviewer should reject any distributed-field no-go. The prefix
> code proves that full-rank, both-parity, finite-depth local preparation is
> possible; only its trivial Clifford pullback leaves the closing string. The
> edge code proves that all local CAR signs can be bounded; only its periodic
> rank and holonomy are wrong. A connected bounded-degree Bravyi–Kitaev code
> avoids fixing parity independently on every matching cycle, while a coherent
> charge background, dynamical flux transfer, or measurement-prepared odd join
> could restore the missing sector without a marked seam. Non-Pauli and gamma-
> register encoders are not represented by either tested grammar.

This steelman is convincing. A universal no-go is premature.

### N8 — cross-cycle echo

| earlier boundary | later mechanism | Cycle-263 response |
|---|---|---|
| spectator state rank versus exchange locality | rough subsystem closes even algebra | preserve both sides rather than splice them |
| deterministic gauge representative | coherent frame orbit in Cycle 249 | leave coherent parity-background route live |
| marked odd charge | coherent charge orbit in Cycle 252 | do not treat marked `h` as necessary content |
| mobile phase head | distributed M/P/T field in Cycle 263 | exact state preparation now closes; reassess the remaining gate wall |
| static endpoint-star Pauli failure | altered auxiliary content and dynamic routes | do not transfer Cycle-256 negative |
| compiler schedules mistaken for time | Cycle-255 typed Record criterion | keep three CNOT layers as compiler resources only |

Representation changes have repeatedly retired narrower walls. N1–N8 passes
only for the fixed-grammar statement and fails for a universal no-go, minimum
content, shared obstruction, or axiom pressure.

## 14. Route disposition and optimal next campaign

**Retain:**

- the 18-M2/cell M/P/T full-Fock code;
- its exact `12L^3` local-check rank and three-layer preparation;
- both parity sectors and bounded adjacent logical gates;
- the residual-2 closing shortcut and two-violation phase-read controls;
- the exact weight-2 edge-gauge CAR incidence algebra;
- the cycle-even, marked-rank, and weight-`2L` holonomy census;
- all-frame/coarse-translation descriptor-family audit; and
- all deletion and held-size controls.

**Do not claim:**

- a common bounded full-Fock CAR compiler;
- a minimum edge/gauge content theorem;
- autonomous odd/holonomy preparation;
- physical beta/mass/contact/seam reproduction;
- physical time, Records, rate, energy, source, or gravity; or
- shared obstruction or axiom pressure.

The optimal next campaign is the **connected degree-five edge-code odd-sector
join**. Instantiate the Bravyi–Kitaev-style bounded even algebra directly on
the complete Cycle-252 branching graph, audit all local cycle stabilizers and
the three torus Wilson sectors, then add a coherent distributed charge/parity
field without a marked root. Demand exact exponent `6L^3`, bounded preparation,
all 24 frames/translations, actual `beta=-0.3`, `g=0.37` coin/A-B/contact, and
mass/rank-73 seam tests in that same encoding. If the fixed stabilizer/Clifford
join fails, scope it exactly and retask to non-Pauli, measurement/reset, or
open-boundary formation.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/distributed_phase_field_car_compiler_cycle263_2026_07_17.py
```
