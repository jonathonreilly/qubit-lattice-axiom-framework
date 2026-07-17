# Rough-terminal same-code local instrument — Cycle 277

**Date:** 2026-07-17

**Type:** exact bounded coherent dilation and conditional two-outcome quantum
instrument on the Cycle-251 physical-M2 code

**Status:** positive same-code local quantum instrument; pointer preparation,
readout, trace, and outcome selection remain explicit imports; no occurrence
or Record is claimed

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/rough_terminal_same_code_local_instrument_cycle277_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface.

## Result up front

Cycle 277 consumes the Cycle-251 operator endpoint without changing codes and
without splicing in Cycle-271 states. In one coarse cell `x`, choose the
proper-cubic scalar matter observable

```text
Q_x = product_(d=0)^5 B_hat_(x,d),
```

the mapped total occupation parity of the six intrinsic modes in that cell.
In the Cycle-251 rough-terminal code, `Q_x` is an ordinary physical Pauli with

```text
phase       0
X weight    0
Z weight   12
support     12 M2 factors.
```

It commutes with every physical code check and with the complete bounded
auxiliary even-CAR algebra. Both signs of `Q_x` remain lawful in both fixed
common matter/auxiliary parity sectors at `L=3,4,5` and held-out `L=6`.

Add one pointer M2 `p`, prepared in `|0>`. With

```text
P_+ = (I+Q_x)/2,
P_- = (I-Q_x)/2,
```

the bounded coherent correlation is

```text
U_(x,p) = P_+ tensor I_p + P_- tensor X_p.
```

This is a unitary on support 13. Because the physical `Q_x` is a product of
12 `Z` factors, the same truth table is obtained by 12 serial CNOTs from
those factors to the pointer. The direct bounded unitary or that compiled
schedule is supplied instrument dynamics. The runner does not assert that
each intermediate CNOT separately preserves the code; the complete `U_(x,p)`
does.

If pointer Z readout, pointer trace, and conditional outcome selection are
admitted, the exact Kraus operators are

```text
K_+ = <0|U|0> = P_+,
K_- = <1|U|0> = P_-,

I_+(rho) = P_+ rho P_+,
I_-(rho) = P_- rho P_-.
```

Completeness and immediate repeatability residuals are exactly zero. The two
pointer eigenstates have overlap zero and trace distance one. The unconditioned
channel is the ordinary dephasing map

```text
rho -> P_+ rho P_+ + P_- rho P_-.
```

Its Choi rank is two, so an environment of dimension at least two is required
for this exact binary projective channel. One pointer M2 is therefore minimal
for this declared dilation. This is not a minimum-content theorem for all
instruments or for Record formation.

The instrument is nondemolition only at the stated resolution. It preserves
`Q_x`, is immediately repeatable, and commutes with the actual onsite
`beta=-0.3` coin and `g=0.37` contact. It anticommutes with the six physical
stream generators crossing the boundary of `x`; no nondemolition claim is
made after a stream layer.

The coherent unitary establishes a reversible correlation. It is not an
occurrence and not a Record. The conditional instrument additionally imports
pointer preparation, pointer readout effects, a partial trace, and an outcome
label/normalization rule. It does not derive irreversible actualization,
numerical Born weights, a physical clock, energy, or rate.

All 24 proper-cubic frames and the full 27-element L=3 translation group
covary the `Q_x`/pointer family. A provisioned covariant pointer field changes
the Cycle-251 overhead from 22 to 23 M2 factors per coarse cell. The actual
single-cell instrument needs only one pointer.

This is the strongest same-code local instrument currently attached to the
physical-M2 matter lane. It is sectorwise because Cycle 251 still lacks a
bounded preparation joining its two parity-locked auxiliary sectors. There is
no route-independent obstruction and no axiom pressure.

**Compiler circuit depth is not physical time. `Q_x` is not physical energy,
no generator coefficient is called a rate, and a coherent pointer is not a
Record.**

## 1. Same-code physical observable

Cycle 251 uses `22N` physical M2 factors for `N=L^3` coarse cells and local
check rank `15N+1`. The scalar cell parity is built from the exact mapped
matter operators already present in that code. No new fermion-to-qubit
dictionary or comparison map is introduced.

The exact size census is:

| `L` | base check rank | `Q_x` support | check leakage | auxiliary commutators | instrumented M2/cell |
|---:|---:|---:|---:|---:|---:|
| 3 | 406 | 12 | 0 | 0 | 23 |
| 4 | 961 | 12 | 0 | 0 | 23 |
| 5 | 1876 | 12 | 0 | 0 | 23 |
| 6 held out | 3241 | 12 | 0 | 0 | 23 |

The physical code projector is extended as `P_code tensor I_p`. Since
`[Q_x,S]=0` for every code check `S`, both `P_+` and `P_-` map the code to
itself. Therefore `U_(x,p)` preserves the code exactly at completion.

The auxiliary independence is stronger than a dimension count. Every
Cycle-251 bounded auxiliary `B_tilde` and `A_tilde` commutes with `Q_x`, so

```text
[U_(x,p), A_aux tensor I_p] = 0.
```

An explicit two-qubit matter/pointer calculation tensored with three distinct
auxiliary density operators gives the same pointer state
`diag(0.7,0.3)` with matrix residual zero. Thus the conditional probabilities
depend only on the matter reduced functional in the declared sector.

## 2. Sectorwise state domain

Let `P_m` be total matter parity. For every combination

```text
P_m = +/-1,
Q_x = +/-1,
```

the phase-aware stabilizer rank is `15N+3`, with zero inconsistencies at all
four sizes. All four parity/outcome combinations are nonempty. The Kraus
operators commute with `P_m`, hence a state beginning in either fixed common
matter/auxiliary sector remains in that sector.

The lawful state domain is any density operator already supported in one
fixed common-parity Cycle-251 code sector, tensored with pointer `|0><0|`.
Cycle 251 supplies the sectorwise algebraic factorization but not a bounded
preparation of an arbitrary such state. Cycle 277 does not repair or hide
that preparation dependency.

Cycle 271 states are not imported. Its Wilson-sector edge code is a different
physical code with a different comparison map. No local reduced state from
that lane is silently attached to the Cycle-251 rough-terminal code.

## 3. Coherent dilation and exact instrument

On the abstract `Q_x` eigenvalue qubit and pointer, `U_(x,p)` is exactly CNOT:

```text
|+>|0> -> |+>|0>,
|->|0> -> |->|1>.
```

The runner verifies:

| control | residual |
|---|---:|
| unitarity | 0 |
| logical matrix minus CNOT | 0 |
| 8192-entry physical parity truth table | 0 failures |
| `K_+-P_+` | 0 |
| `K_--P_-` | 0 |
| Kraus completeness | 0 |
| immediate repeatability | 0 |
| pointer eigenstate overlap | 0 |
| pointer eigenstate trace distance | 1 |

For a coherent equal superposition of `Q_x` signs, the unitary produces a Bell
correlation and pointer reduced purity `1/2`. That entanglement is reversible.
Nothing in the unitary selects one term, makes it permanent, or promotes the
pointer to a Record.

If the pointer is not prepared in `|0>` but is maximally mixed, the two
`Q_x` eigenstates produce identical pointer outputs with trace distance zero.
Pointer preparation is therefore load bearing for the claimed readout.

The Choi matrix of the unconditioned dephasing channel has exact numerical
rank two. Standard Stinespring/Kraus theory then bounds the exact environment
dimension below by the Kraus/Choi rank. One M2 closes that declared dimension
and no smaller nontrivial environment does.

## 4. Covariance and locality

The six-direction product makes `Q_x` a proper-cubic scalar. The runner
applies the inherited Cycle-251 bounded ordering-gauge repair and tests every
cell under:

- all 24 proper-cubic frames; and
- every displacement in the full 27-element L=3 translation group.

There are zero transformed-`Q` failures and zero pointer-role permutation
failures. The pointer M2 is assigned one scalar role at each coarse-cell
instrument site. The covariant family uses the inherited period-16 puncture
roles and coarse cells; this is not homogeneous translation of
undifferentiated physical M2 factors.

The physical `Q_x` support is twelve and the joint support is thirteen for
every `L`. A 12-CNOT serial parity accumulation has constant gate count and
constant compiler depth. The macrocell routing and pointer position are
supplied. No claim is made that the sequence defines a clock or duration.

## 5. Actual mass/contact compatibility

At the abstract six-mode cell, `Q_x=(-1)^{N_x}`. The actual Cycle-230 Fock
coin preserves total cell parity, and the contact

```text
exp(i g binom(N_x,2)), g=0.37,
```

is diagonal in occupation. The 128-dimensional cell-plus-pointer matrices
give

```text
[U_Q, Gamma(C_beta=-0.3) tensor I_p] = 0,
[U_Q, W_0.37 tensor I_p]             = 0
```

to residual zero on the fixture. Contact remains identity on the zero- and
one-particle subspaces. The rest-to-analytic mass ratio is
`0.9999999999999998`, and the imported L=3 principal-sea rank remains 73.

These are operator compatibility diagnostics. Measuring local cell parity
can disturb a spatially extended one-particle or sea state, and the runner
does not claim to prepare or preserve the rank-73 sea. The cell parity is not
physical energy and the pointer coupling is not a rate.

## 6. Nondemolition boundary and deletions

The complete conditional instrument is projective and immediately
repeatable:

```text
P_s P_t = delta_(s,t) P_s.
```

Every mapped onsite/internal matter `A` commutes with `Q_x`. Exactly six
mapped outer stream `A` generators, one across each cell boundary direction,
anticommute with it at `L=3,4,5,6`. Therefore:

- the instrument is nondemolition for `Q_x` itself and compatible with the
  onsite coin/contact;
- it is not nondemolition under the complete free stream; and
- immediate repetition does not imply repetition after a compiler update.

Deletion controls distinguish the clauses:

1. deleting one physical `Z` factor from `Q_x` produces five exact local-check
   anticommutators at every tested size;
2. deleting the pointer coupling makes the two eigenvalue pointer outputs
   identical, changing overlap from zero to one;
3. deleting pure pointer preparation by using `I/2` makes pointer-output trace
   distance zero; and
4. tracing the pointer without conditional selection gives only the
   unconditioned dephasing channel, not a selected fact.

The first deletion tests same-code preservation. The latter three expose the
supplied apparatus/conditioning resources rather than pretending the coherent
unitary actualizes an outcome.

## 7. Explicit instrument-import inventory

The conditional instrument imports all of the following:

1. one pointer M2 in a declared bounded macrocell role;
2. pointer preparation in `|0><0|`;
3. the selected bounded controlled-`Q_x` unitary or its 12-CNOT compilation;
4. pointer Z readout effects `|0><0|` and `|1><1|`;
5. ordinary quantum partial trace over the pointer/environment;
6. the trace functional used to form `p_s=Tr(P_s rho)`;
7. conditional outcome selection and normalization by `p_s` when nonzero;
8. a declared instrument placement relative to the Cycle-230 update;
9. the Cycle-251 fixed common-parity code sector and its initial state;
10. the inherited period-16 puncture/macrocell role pattern and bounded
    routing; and
11. ordinary complex quantum mechanics and tensor composition.

The construction does not supply a physical pointer-preparation mechanism, a
readout interaction, irreversibility, stable amplification, occurrence,
Record formation, a numerical probability law derived from the substrate, or
an actual-history selector. These are explicit remaining interfaces, not
silent consequences of the Kraus formulas.

## 8. Lawful domain

The exact claim applies to:

```text
one scalar cell-parity observable Q_x,
on the Cycle-251 rough-terminal physical code,
inside either fixed common matter/auxiliary parity sector,
with a supplied pure pointer and supplied conditional-instrument operations.
```

It does not cover odd matter field operators, arbitrary six-mode observables,
a destructive stream-spanning detector, a prepared full-Fock join of both
parity sectors, a global Wilson-sector readout, or a physical occurrence.

The pointer outcome label is not a Record. The order “prepare, couple, read,
trace, condition” is a compiler/instrument prescription, not derived physical
time. The pointer phase is not physical energy, and a unitary generator
element is not a rate.

## 9. Prior-art and novelty boundary

Von Neumann/Lüders projective measurements, controlled-pointer dilations,
Kraus instruments, Choi rank, Stinespring environment bounds, stabilizer
logical-Pauli measurement, and quantum nondemolition measurement are
established prior art. Kretschmann, Schlingemann, and Werner's
[*The Information-Disturbance Tradeoff and the Continuity of Stinespring's
Representation*](https://arxiv.org/abs/quant-ph/0605009) supplies relevant
Stinespring context. Cycle 277 claims no new general measurement theorem,
minimal-environment theorem, or Record mechanism.

The fixture-specific contribution is limited to:

1. the exact weight-12 scalar `Q_x` in the Cycle-251 physical code;
2. its support-13 one-pointer dilation and exact Kraus residuals;
3. zero physical-code and auxiliary leakage through held-out `L=6`;
4. both outcomes in both common-parity sectors;
5. all-frame/full-translation covariance on the supplied physical roles;
6. exact onsite mass/contact compatibility and six-stream nondemolition
   boundary; and
7. deletion and import controls separating correlation from occurrence.

No global novelty priority is asserted. No Thirring engine is used or
compared.

## 10. Six-wall and all-lane effect

| wall | Cycle-277 effect | remaining dependency |
|---|---|---|
| `C_ref` | one explicit bounded pointer role and binary reference basis | physical pointer preparation, stable reference, readout, and homogeneous role generation |
| `C_num` | exact binary `Q_x` projectors inside either fixed common-parity sector | common both-parity physical preparation and a selected number reference remain open; trace weights belong to the separate Born/instrument bridge |
| `C_wrap` | same common-parity sector is preserved; no Wilson state is imported | bounded preparation joining Cycle-251 parity sectors and its supplied marker |
| `C_int` | coherent pointer coupling commutes with actual onsite coin/contact | stream boundary has six anticommutators; instrument placement and microscopic coupling selection supplied |
| `C_local` | strong gain: same-code support-13 unitary, one-M2 overhead, zero leakage, covariance, Kraus map | code-preserving physical subgate schedule, pointer preparation/readout dynamics, and full-Fock common encoder |
| `C_source` | unchanged | no energy, stress, source, resource, or gravity response selected |

The five-lane planning scores remain the Cycle-270 baseline because this
single instrument probe does not justify percentage revision:

| lane | effect |
|---|---|
| operational quantum / Records | local instrument algebra advances; occurrence and Record formation remain open |
| causal time / clock | unchanged; compiler ordering/depth is not time |
| inertia / matter | same-code local parity coupling and onsite mass/contact compatibility advance; stream nondemolition is open |
| gravity / source / resource | unchanged; pointer energy/resource ledger is not selected |
| Born / probability / realized history | Kraus/trace rule is explicitly imported; no numerical Born law or actual history is derived |

The full Cycle-270 baseline remains:

| lane | integrated maturity | strict substrate floor | conditional bridge maturity |
|---|---:|---:|---:|
| operational quantum / Records | 42% | 18% | 63% |
| causal time / clock | 32% | 17% | 58% |
| inertia / matter | 58% | 24% | 77% |
| gravity / source / resource | 34% | 12% | 58% |
| Born / probability / realized history | 30% | 14% | 74% |

These are planning estimates, not audit verdicts or probabilities that the
framework is correct.

## 11. N1–N8 no-go-discipline gate

The main result is positive. The narrow boundaries are that this declared
instrument is not stream-nondemolition and does not by itself create an
occurrence or Record. No general measurement, preparation, or occurrence
no-go is claimed.

### N1 — alternative-route enumeration

| route | honesty marker | exact disposition |
|---|---|---|
| weight-12 scalar `Q_x` plus one pure pointer | **ATTEMPTED** | succeeds: support 13, zero leakage, orthogonal pointer states |
| delete the pointer coupling | **ATTEMPTED** | fails distinguishability: pointer overlap becomes one |
| maximally mixed rather than pure pointer preparation | **ATTEMPTED** | fails readout: pointer-output trace distance is zero |
| delete one physical factor of `Q_x` | **ATTEMPTED** | fails same-code preservation with five check anticommutators |
| demand nondemolition across the subsequent free stream | **ATTEMPTED** | fails for this observable: six boundary-stream anticommutators |
| immediate repetition with no intervening stream | **ATTEMPTED** | succeeds with exact repeatability residual zero |

Contact predicates, six direction-resolved pointers, destructive detectors,
autonomous dissipative apparatuses, and permanent commit mechanisms remain
live and untested. Their status prevents any broader negative.

### N2 — condition-independence audit

The collapsed open-condition set is:

- `C_inst`: physically supply pointer preparation, coupling, readout, trace,
  and conditional selection;
- `C_stream`: extend or replace the observable so a desired claim survives
  the complete free stream; and
- `C_record`: supply irreversible occurrence/permanent Record formation.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| `C_inst`,`C_stream` | no; a valid local instrument may disturb stream hopping | no; a conserved observable supplies no apparatus | yes |
| `C_inst`,`C_record` | no; a conditional map does not actualize a branch | no; a Record mechanism need not use this parity pointer | yes |
| `C_stream`,`C_record` | no; nondemolition does not make a fact permanent | no; a destructive occurrence need not be stream-nondemolition | yes |

The algebraic code representation is closed for `Q_x` and is not inflated
into a fourth open condition. Cycle-251 full-Fock preparation is a declared
domain restriction, not silently counted as a failure of this sectorwise
instrument.

### N3 — hidden-condition scan

The required phrase scan was applied. Pointer `|0>`, the readout basis,
partial trace, trace functional, conditional normalization, sector state,
macrocell roles, routing, and instrument placement are explicit imports.
“By construction,” “as is standard,” “naturally,” “obviously,” “standard
QFT,” “framework provides,” “registered,” “canonical,” “background,” and
“bridge context” provide no hidden proof step. The phrase “prior art” in the
novelty section is non-load-bearing and cited.

No hidden condition was promoted, so the N2 count remains three.

### N4 — residual matching

| witness | witness residual | Cycle-277 residual/use | match? |
|---|---|---|---|
| Cycle-251 note, local commutant sections | mapped matter `B/A` commute with exact auxiliary even-CAR; bounded state preparation absent | `Q_x` is made only from those `B` operators; zero auxiliary commutators; preparation remains supplied | **yes** |
| Cycle-251 note, fixed-update section | onsite coin/contact and mass fixture intertwine sectorwise | instrument commutators with the same onsite word are zero | **yes** |
| Cycle-230 note | six-mode cell parity is even; contact is identity at `N<=1` | exact abstract parity/contact compatibility | **yes** |
| Cycle-266 note | coherent environment correlation is not occurrence or Record formation | category firewall only; no physical constructor is imported | **no; not a negative witness** |
| Cycle-271/275 Wilson-state notes | matched states belong to a different edge code | no state is imported into Cycle 251 | **no; explicitly dropped** |

No mismatched residual is used to promote or close the instrument theorem.

### N5 — resolution and rhetoric audit

- “Same-code” is tested on the literal Cycle-251 checks and matter/auxiliary
  operators; it does not mean the two parity sectors have a bounded common
  preparation.
- “Nondemolition” is tested for `Q_x`, immediate repetition, internal onsite
  operators, coin, and contact. It is false for the six boundary stream
  generators and is not stated lattice-wide.
- “Minimal pointer” means Choi rank two for this declared binary dephasing
  channel. Other instruments, encodings, or occurrence mechanisms were not
  minimized.
- “Instrument” means the conditional Kraus map after importing ordinary
  readout/trace/selection. The coherent unitary alone is only a correlation.
- “Not an occurrence” and “not a Record” are typed at the one-block coherent
  and conditional-map resolutions; no universal Record impossibility is
  claimed.

### N6 — partial-closure path scan

This cycle retires the need to bridge codes merely to obtain a local matter
instrument: the Cycle-251 mapped scalar parity already admits a bounded
code-preserving dilation and exact conditional map. It does not retire
physical apparatus supply or actualization. Live constructive paths include
a contact predicate that is less disruptive on the one-particle sector, a
code-preserving subgate schedule, a repeated syndrome-style apparatus, an
autonomous dissipative pointer, and a permanent commit interface.

These are physics/implementation routes, not vocabulary fixes and not axiom
requests. No approved primitive is relabeled as a wall.

### N7 — steelman

A hostile reviewer should say that Cycle 277 has wrapped a standard Lüders
measurement around one logical Pauli while importing every difficult part of
an actual laboratory instrument: a pure pointer, readout, partial trace,
conditional selection, and the sector state. The optional 12-CNOT compilation
may also leave the code between substeps. That criticism is correct. The new
result is valuable only as a same-code bounded dilation/Kraus theorem with
exact covariance and leakage controls; it is not an occurrence mechanism,
Record constructor, autonomous apparatus, or prepared full-Fock compiler.
Contact-predicate and dissipative routes remain capable of closing more.

### N8 — cross-cycle echo

Cycle 251 left an exact physical operator endpoint and asked for bounded
preparation/operational use. Cycle 277 consumes its local `B` algebra directly
rather than importing another code. Cycle 266 already separated coherent
environment correlation from occurrence and Record formation; the same
separation is enforced here. Cycles 271/275 retired a matched-state condition
in a different Wilson edge code, so their state mechanism is deliberately not
reused. Cycle 274 showed that an operator witness does not itself select a
physical witness state; Cycle 277 supplies a sectorwise conditional state map
but still imports the input and readout.

The repeated lesson is that algebra, prepared state, conditional instrument,
occurrence, and permanent Record are distinct dependency nodes. Earlier
closures therefore narrow the current interface without establishing a
shared obstruction.

**N1–N8 status: PASS for the scoped positive theorem and narrow stream/readout
boundaries; FAIL for any general measurement, occurrence, or Record no-go.**
There is no route-independent obstruction and no axiom pressure.

## 12. Optimal next campaign

The highest-value next probe is an actual same-code apparatus dynamics that
replaces at least one imported instrument operation. Two concrete routes are:

1. construct a bounded contact-predicate pointer whose one-particle action is
   identity and test whether it reduces stream disturbance; or
2. attach a finite dissipative/commit carrier to the Cycle-251 pointer and
   test an explicit fault/deletion grammar for permanence without calling
   coherent copying a Record.

Any next route must retain the same-code constraint, include its apparatus
resource/energy ledger without declaring phase to be energy, and keep physical
clock/rate calibration separate.
