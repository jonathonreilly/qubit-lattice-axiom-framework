# Connected-edge same-code local instrument — Cycle 278

**Date:** 2026-07-17

**Type:** exact bounded same-code local quantum instrument candidate with
sector-state statistics and a first-wrap boundary control

**Status:** positive conditional instrument on the Cycle-269/271 connected
edge code and Cycle-275 total-even matched sector states; preparation,
readout, occurrence, and Record formation remain supplied or open

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/connected_edge_same_code_local_instrument_cycle278_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface. It
does not use or splice the Cycle-251 code.

## Result up front

Cycle 278 constructs the first bounded coherent pointer coupling directly on
the same connected physical-M2 edge code that carries the Cycle-271 local
process quotient and the Cycle-275 explicit matched sector projectors.

At one coarse cell `x`, let the six mapped occupation-parity operators be

```text
B_(x,d) = (-1)^(n_(x,d)),  d=0,...,5.
```

They are bounded physical Pauli operators in the Cycle-269/271 code. Define
the proper-cubic scalar **contact-active projector**

```text
Q_x = 1_{N_x >= 2},       N_x = sum_d n_(x,d).
```

This is the support projector of the actual Cycle-230 contact generator
`binom(N_x,2)`. It is not called energy. Its exact Walsh expansion is a
64-term polynomial in the six commuting `B_(x,d)` operators. Couple one fresh
pointer M2 by

```text
U_I = (I-Q_x) tensor I_p + Q_x tensor X_p.
```

`U_I` is unitary and self-inverse. With the pointer prepared in `|0>`, a
supplied pointer-`Z` read gives the conditional instrument

```text
I_0(rho) = (I-Q_x) rho (I-Q_x),
I_1(rho) = Q_x rho Q_x.
```

The construction has constant overhead and bounded support:

| item | exact result |
|---|---:|
| extra pointer M2 | 1 per active instrument cell |
| union of physical matter M2 touched | 18 |
| total matter-plus-pointer neighborhood | 19 |
| maximum Pauli-term weight before pointer | 12 |
| maximum polynomial-term weight with pointer | 13 |
| local-check leakage | 0 |
| Wilson transitions | 0 |

For the explicit Cycle-275 normalized projectors in every one of the eight
Wilson sectors, the exact pointer-one weights are

| matched state family | `p(pointer=1)` |
|---|---:|
| uniform fixed-sector projector | `57/64` |
| fixed sector plus `B_0=+1` | `13/16` |
| fixed sector plus `B_0=-1` | `31/32` |

These values hold at `L=3,4,5` and held-out `L=6`. The complete instrument
process is identical across **all eight Wilson sectors** for the maximal Cycle-271
pre-wrap onsite cones, namely iterations `1,1,2,2`. The cone-avoiding
comparison membranes commute with the actual coin/contact/A-B gate algebra,
the instrument effect, and the sector projectors.

The result closes a real part of the physical-M2-matter-to-instrument bridge:
there is now one explicit bounded pointer interaction and one explicit family
of physical input density operators in the **same code**. It does not prepare
those global projectors by a bounded process, select the microscopic law,
read or reset the pointer autonomously, choose one outcome, or turn the
pointer into a permanent fact.

This is an instrument candidate, **not occurrence and not Record formation**.
Compiler iteration is not physical time. There is no shared obstruction and
no axiom pressure.

## 1. Same-code physical operator

For an occupation string `n in {0,1}^6`, the commuting `B` characters give a
Fourier basis. Therefore

```text
Q_x = sum_(m in {0,1}^6) c_m product_d B_(x,d)^(m_d),

c_m = 2^-6 sum_n 1_(|n|>=2) (-1)^(m dot n).
```

The runner evaluates all 64 coefficients exactly as rational numbers. All 64
are nonzero. Every Pauli word commutes with every local check and all three
Wilson operators. Each `B_(x,d)` is already an explicit generator of the
declared full-cell Cycle-271 cone algebra, so closure under products puts the
whole effect and both Kraus operators in that same algebra.

The six individual mapped `B` words have weight five. Their physical support
union contains 18 M2 factors, independent of `L`; cancellations leave every
Walsh word at weight at most 12. Adding one carried pointer gives a 19-M2
neighborhood and one M2 of overhead. This is bounded operator support. The
cycle does not synthesize `U_I` into a selected nearest-neighbor primitive
gate law or derive the pointer placement from homogeneous initial data.

## 2. Actual coin/contact compatibility

The runner imports the actual fixture

```text
beta = -0.3,
g    = 0.37,
W_g  = exp(i g binom(N_x,2)).
```

At the intrinsic 64-dimensional cell resolution it verifies

```text
[Q_x, Gamma(C_beta)] = 0,
[Q_x, W_g]           = 0,
[Q_x, Gamma(A)]      = 0,
```

to printed matrix residual zero on the current fixture. The first equality is
number conservation of the actual dense onsite coin; the third is the onsite
direction-reversal FSWAP layer. The intercell `B` stream can change `N_x`, so
the instrument is an intervention at a declared process location rather than
a conserved cell label.

`Q_x=0` throughout `N_x=0,1`. Thus the pointer coupling is exactly identity on
the one-particle local sector and does not change the Cycle-219/230 mass
fixture. This is preservation of the operator fixture, not an encoding of the
odd one-particle state in the total-even projectors.

## 3. Exact pointer statistics and conditional states

Let `P_w` be the normalized fixed-Wilson stabilizer projector from Cycle 275.
Every nonidentity product of the six local `B` operators has zero expectation
in `P_w/Tr(P_w)`. The six occupation bits therefore have the uniform local
functional, giving

```text
Pr(N_x>=2) = (64 - 1 - 6)/64 = 57/64.
```

Adding `B_0=+1` fixes mode zero empty and leaves five locally uniform bits:

```text
Pr(N_x>=2 | B_0=+1) = 1 - (1+5)/32 = 13/16.
```

Adding `B_0=-1` fixes one occupied mode, so contact is inactive only when the
other five are empty:

```text
Pr(N_x>=2 | B_0=-1) = 1 - 1/32 = 31/32.
```

The runner reconstructs all 64 local configuration weights from the exact
Pauli moments for every size, sector, and bias. Every weight is nonnegative,
the sums are one, the stabilizer systems are consistent, and all eight sectors
give the displayed values.

The normalized conditional states are explicit:

```text
rho_(w,r) = Q_r P_w Q_r / Tr(Q_r P_w),
Q_0=I-Q_x, Q_1=Q_x,
```

and likewise for the two biased families. This is ordinary conditional
quantum-state algebra. `Tr(rho Q_r)` is a supplied quantum trace pairing, not
a frequency theorem or one actually selected history.

## 4. Pre-wrap process equality

For the maximal pre-wrap onsite cone, Cycle 271 moves every Wilson seam out of
the accumulated actual stream-gate cone. Cycle 275 supplies a comparison
membrane `M_(w,K)` with

```text
M_(w,K) P_0 M_(w,K) = P_w,
[M_(w,K), A_K] = 0.
```

Because `Q_x` is in `A_K`, adjoining the pointer interaction preserves this
equality. For any supplied pointer preparation `eta_p`, any sequence of actual
Cycle-230 gates whose cone remains contractible, and either pointer outcome,
the transported joint process functional is sector independent.

The exact tested rows are:

| `L` | maximal pre-wrap iteration | Wilson sectors | state families per sector | failures |
|---:|---:|---:|---:|---:|
| 3 | 1 | 8 | 3 | 0 |
| 4 | 1 | 8 | 3 | 0 |
| 5 | 2 | 8 | 3 | 0 |
| 6 held out | 2 | 8 | 3 | 0 |

This is not a splice with Cycle 251. The physical `B` algebra, local checks,
Wilson sectors, comparison maps, global projectors, and pointer coupling all
live in the connected Cycle-269/271/275 edge-code lane.

## 5. Covariance and preservation

At `L=3`, all 24 proper-cubic frames combined with the **full 27-element L=3
translation group** give 648 exact tests. A frame permutes the six directional
`B` operators. Because `Q_x` depends only on total occupation, it is a scalar
under that permutation. The pointer is carried as a scalar M2 at the
transformed instrument cell.

For every combined transformation the runner verifies:

1. the transformed six-`B` family equals the family at the transformed cell;
2. the complete local-check family is preserved;
3. the Wilson center maps into itself; and
4. the pointer rule has no preferred direction.

This is exact **local-check and Wilson preservation**. Every one of the 64
Pauli terms commutes with every bounded local check and
every Wilson. Hence the coherent interaction has zero code leakage and zero
sector transitions before any pointer read.

## 6. Repeatability, disturbance, and deletion

Since `Q_x^2=Q_x`, both conditional branches are repeatable:

```text
Tr(Q_s rho_(w,r)) = delta_(s,r).
```

The three displayed input families commute with `Q_x`, so the nonselective
channel

```text
rho -> (I-Q_x)rho(I-Q_x) + Q_x rho Q_x
```

leaves them unchanged to matrix residual zero. This is state-specific
nondisturbance, not identity on the whole even algebra.

A local even off-diagonal generator that flips two occupation bits supplies a
disturbance control. Its nonselective-channel residuals are

```text
Frobenius residual = sqrt(10),
operator residual  = 1.
```

Thus the instrument is not being mistaken for a passive pointer label.

Deletion controls are:

- deleting `U_I` leaves the initialized pointer-one weight exactly zero rather
  than `57/64`;
- deleting one factor from the first-wrap Wilson word removes its isolated
  central direction;
- the contact projector is exactly zero on `N<=1`, protecting the mass
  diagnostic;
- independently choosing unmatched `B_0=+1/-1` sector states changes the
  contact weight from `13/16` to `31/32`, so matched-state equality is not
  automatic.

## 7. First-wrap control

At the first full-cell wrap, `t=2,2,3,3` for `L=3,4,5,6`, the cone algebra
gains all three Wilson central directions. For each axis the exact word

```text
i^(3L) product_(e in gamma_axis) A_e = W_axis
```

contains `3L` bounded factors. A pointer controlled by
`(I-W_axis)/2` has weights `0` and `1` in the two opposite sector projectors.
Deleting one factor makes the central increment zero.

That is a boundary control, not the candidate local instrument: its factor
count grows with `L`. The bounded contact pointer itself still has weight
`57/64` in all uniform sector projectors at first wrap. This demonstrates two
facts simultaneously:

1. the whole-cone all-observable equality cannot continue past wrap; and
2. a particular bounded local instrument need not automatically read a Wilson
   character merely because its upper cone wraps.

No post-wrap equality is claimed for arbitrary states, observables, or
instruments.

## 8. Supplied structure and lawful domain

The construction supplies or imports:

1. the Cycle-269 connected square-pyramid edge code, local-check signs, and
   three Wilson characters;
2. the total-even target restriction;
3. the actual Cycle-230 `beta=-0.3`, `g=0.37`, coin/contact/A-B schedule;
4. one instrument cell, a process insertion location, and one pointer M2;
5. the pointer `|0>` preparation and the controlled `X` interaction;
6. the pointer-`Z` effect, ordinary quantum trace, and conditional-state rule;
7. the Cycle-275 algebraic global projectors or locally biased variants;
8. the cone-dependent comparison membrane; and
9. finite periodic sizes, a macro origin for display, and numerical matrix
   tolerances for the 64/128-dimensional controls.

The exact **preparation, trace, readout, and outcome-selection imports** are
therefore visible. In particular:

- the Cycle-275 projectors are algebraic states, not bounded preparations;
- pointer initialization/reset is supplied;
- the trace rule supplies normalized conditional weights;
- a pointer effect is not a physical read protocol;
- no law selects one conditional branch;
- no close/permanence mechanism writes a framework Record; and
- no repeated process or component-mean theorem turns the weights into
  frequencies.

The lawful domain is even observables and the three declared matched state
families in a contractible actual Cycle-230 gate cone. It excludes odd matter
states, the rank-73 sea as a prepared state, arbitrary unmatched projectors,
global bounded preparation, and arbitrary post-wrap processes. The runner
rejects `L<3`, malformed Wilson characters, and pointer dimension other than
two.

## 9. Prior-art and novelty boundary

Davies–Lewis instruments, Lüders conditional maps, and unitary indirect
measurement dilations are prior art:

- Davies and Lewis, [“An operational approach to quantum
  probability”](https://doi.org/10.1007/BF01647093), *Communications in
  Mathematical Physics* 17 (1970) 239–260;
- Lüders, [English translation of the 1951
  paper](https://arxiv.org/abs/quant-ph/0403007); and
- Ozawa, [“Quantum measuring processes of continuous
  observables”](https://doi.org/10.1063/1.526000), *Journal of Mathematical
  Physics* 25 (1984) 79–87.

The repository's earlier primary-source audit already establishes that a
dilation realizes an instrument class but does not select the physical
instrument, occurrence, context, or outcome. Cycle 278 claims no novelty for
controlled pointers, projective instruments, stabilizer projectors, or
topological-sector local indistinguishability.

The fixture-specific constructive gain is narrower:

1. the explicit `Q_(N>=2)` polynomial on the connected physical-M2 edge code;
2. its constant 19-M2 matter-plus-pointer neighborhood;
3. exact `57/64`, `13/16`, and `31/32` statistics on the Cycle-275 projectors;
4. all-eight-sector equality for the complete actual Cycle-230 pre-wrap
   process;
5. all-24/full-27 covariance and zero check/Wilson leakage; and
6. the first-wrap Wilson-pointer and factor-deletion boundary.

No Thirring engine is used or compared.

## 10. Six-wall and all-lane bridge effect

| wall | Cycle-278 effect | remaining dependency |
|---|---|---|
| `C_ref` | one pointer initialization and one physical effect are explicit | pointer preparation/reset, vacuum/sea, phase zero, and homogeneous instrument placement remain supplied |
| `C_num` | exact number-threshold effect and three state-dependent rational weights | odd one-particle/rank-73 state embedding and common full-Fock join |
| `C_wrap` | all-eight pre-wrap instrument equality plus explicit first-wrap boundary | bounded global preparation and wrapped/global process target |
| `C_int` | strong gain: the actual contact-support observable now drives a bounded same-code coherent pointer | physical read, occurrence, law selection, rate, and source ledger |
| `C_local` | strong gain: one 19-M2 instrument neighborhood with zero code/sector leakage | selected local gate synthesis, autonomous placement, bounded state preparation, and full-Fock domain |
| `C_source` | unchanged | no energy, action, stress, source, lapse, or metric response is selected |

All-five-lane effect:

- **Operational quantum / Records:** a genuine physical-M2 conditional
  instrument endpoint now exists on explicit physical density operators, but
  no occurrence, close, permanence, or Record-fibre continuation theorem is
  supplied.
- **Causal time / clock:** unchanged. The insertion index and compiler
  iteration are process-description data, not event time or duration.
- **Inertia / matter:** the one-particle mass fixture is protected and the
  actual contact support is operationally exposed, but the odd mass state and
  full-Fock compiler remain open.
- **Gravity / source / resource:** unchanged. Contact activity is neither
  physical energy nor a gravitational source.
- **Born / probability / realized history:** the trace rule gives exact
  one-shot conditional weights, but it is imported ordinary quantum
  probability; no numerical-law derivation, frequency theorem, or
  actual-member route is added.

The Cycle-270 campaign percentages are not recomputed from this bounded
partial bridge. The result is material qualitative progress in the
matter-to-instrument row, but the strict closure floors do not move while
global state preparation, law selection, readout, and occurrence remain open.

## 11. No-go discipline N1–N8

The main result is constructive. The negative boundaries are only that this
specific dilation does not itself supply bounded preparation, physical
readout, occurrence, Record formation, time, or post-wrap whole-cone equality.
The no-go-discipline skill is applied to prevent those boundaries from being
inflated.

### N1 — alternative-route enumeration

| route | marker | disposition |
|---|---|---|
| contact-active scalar pointer `Q_(N>=2)` | **ATTEMPTED** | succeeds with one pointer, bounded support, exact statistics, and all-frame covariance |
| delete the coherent matter-pointer coupling | **ATTEMPTED** | pointer-one weight becomes zero; establishes that the statistics require the interaction |
| uniform, matched `B_0=+1`, and matched `B_0=-1` sector states | **ATTEMPTED** | all succeed and give three distinct exact weight families |
| extend the whole-cone equality through first wrap | **ATTEMPTED** | fails narrowly because an explicit Wilson-controlled pointer has weights `0/1` |
| delete one factor from the Wilson discriminator | **ATTEMPTED** | succeeds in removing the isolated Wilson direction, narrowing the wrap boundary |
| retain the coherent pointer without a supplied read or trace | **ATTEMPTED** | the unitary dilation still exists, but no conditional branch or numerical readout is thereby selected |
| apply the contact pointer to the one-particle mass fixture | **ATTEMPTED** | coupling is exactly identity; it preserves rather than measures that fixture |

Live routes include an autonomous local pointer reader, redundant reversible
amplification, a dissipative or measurement/feed-forward state preparation,
an odd-parity extension, and observable-specific post-wrap instruments. The
tested boundary is not a general measurement or Record no-go.

### N2 — condition-independence audit

The collapsed condition set is:

- `K_process`: the connected code, actual update cone, and bounded pointer
  interaction;
- `K_prepare`: physical preparation of the displayed matter and pointer
  states;
- `K_read`: a trace/effect/readout map producing the conditional label; and
- `K_actual`: occurrence, close, permanence, and one realized outcome.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `K_process`,`K_prepare` | no | no | yes |
| `K_process`,`K_read` | no | no | yes |
| `K_process`,`K_actual` | no | no | yes |
| `K_prepare`,`K_read` | no | no | yes |
| `K_prepare`,`K_actual` | no | no | yes |
| `K_read`,`K_actual` | no | no | yes |

Pointer initialization is part of `K_prepare`; trace and pointer effect are
part of `K_read`; reset belongs to a repeated preparation/read protocol. They
are not inflated into extra walls.

### N3 — hidden-condition scan

The required phrase scan was applied. The connected code, total-even
restriction, state projectors, pointer preparation, trace rule, insertion
location, finite torus, comparison membrane, and actual update parameters are
all inventoried. “By construction” is not used to hide a premise. “Canonical,”
“registered,” “naturally,” “obviously,” “standard QFT,” and “the framework
provides” carry no load-bearing step. No hidden condition changed the N2
count.

### N4 — residual matching

| witness | witness residual | Cycle-278 use | match? |
|---|---|---|---:|
| Cycle 271, contractible quotient | sectorwise operator processes agree before wrap; state functionals were separate | adjoin a bounded effect inside that exact cone algebra | yes |
| Cycle 275, matched projectors | explicit state functionals agree; bounded preparation absent | derive the first same-code pointer statistics while retaining the preparation firewall | yes |
| Cycle 274, low-particle Wilson readout | selected coarse-CAR observables become sector sensitive after wrap | qualitative consistency only; those are different states and not proof here | no; dropped as proof |
| record-instrument primary-source audit | dilation/Lüders form does not select context or occurrence | keeps readout and actualization outside the coherent unitary | yes for interpretation boundary |
| Cycle 251 sectorwise compiler | different physical code and factorization | no proof role | no; excluded |

The first-wrap proof is the new runner's exact Wilson expectation and
factor-deletion calculation, not an inherited Cycle-274 residual.

### N5 — resolution and rhetoric audit

| resolution | tested statement |
|---|---|
| one intrinsic six-mode block | exact 64/128-dimensional dilation, contact compatibility, and disturbance |
| one physical edge-code cell | 18 matter M2 plus one pointer, zero constraint leakage |
| one pre-wrap process cone | all-eight matched joint-process equality |
| finite torus | `L=3,4,5,6`, including first-wrap Wilson boundary |
| global preparation | not supplied or ruled out |
| pointer occurrence/Record | not implemented; no universal impossibility claimed |
| physical time | not tested; iteration is kept as a compiler index |

“The pointer is not a Record” means only that the displayed coherent carrier
has no occurrence, close, permanence, or readable-history mechanism. It does
not say a future local transducer cannot turn its label into a Record.

### N6 — partial-closure path scan

The cycle itself is a partial-closure path: take explicit state/trace/pointer
imports, prove a bounded same-code instrument theorem, and leave each import
available for later retirement. Further constructive routes are:

1. a bounded physical preparation or local stationary state for the matched
   projector functional;
2. an autonomous reader/close transducer whose output satisfies the Record
   clauses and fails when the matter-pointer coupling is deleted;
3. a repeatable reset protocol and projective process extension;
4. an odd-parity code carrying the one-particle and rank-73 states; and
5. a selected microscopic update that contains both transport and apparatus.

Naming the pointer outcome a Record would close nothing physical. No approved
axiom or primitive is treated as an instrument, trace law, or occurrence map,
and no new axiom is requested.

### N7 — steelman

> A hostile reviewer should argue that the hard operational step is now much
> smaller than the remaining-wall language suggests. The same physical code
> contains the matter algebra, actual contact-compatible update, explicit
> states, and a constant-support pointer dilation. A bounded autonomous
> transducer could amplify that pointer into an append-only carrier, while a
> local dissipative or measurement/feed-forward protocol could realize the
> needed state functional without preparing the displayed global projector.
> Standard instrument-realization results make neither route exotic. The
> absence of those mechanisms in this runner is unfinished implementation, not
> evidence that the substrate forbids them.

This steelman is accepted. The result is promoted as a positive conditional
instrument and the remaining items as next constructions, not a no-go.

### N8 — cross-cycle echo

Cycles 223–226 repeatedly separated coherent correlation, pointer copying,
branch history, close, and permanent Record formation. Cycles 259/266 showed
that a shared-control gate close does not itself select occurrence. Cycle 271
then retired Wilson dependence for contractible operator processes, and Cycle
275 retired the matched-state-functional condition algebraically.

Cycle 278 uses the same successful mechanism as those partial closures: move
to the exact operational resolution, build the missing bounded interaction,
and preserve the semantic firewall. Earlier pointer-copy walls were narrowed
by explicit detectors and close maps rather than constitutional edits; the
same reader/transducer mechanism remains live here.

**N1–N8 status: PASS for the narrow implementation boundary.** There is no
shared obstruction, minimum-content theorem, or axiom pressure.

## 12. Disposition and next campaign

Retain:

- the 19-M2 same-code coherent contact pointer;
- exact `57/64`, `13/16`, and `31/32` sector-state statistics;
- all-eight pre-wrap process equality;
- all-24/full-27 covariance;
- zero local-check and Wilson leakage;
- repeatability, disturbance, coupling deletion, and first-wrap controls; and
- the preparation/readout/occurrence firewall.

Do not claim:

- a bounded preparation of the Cycle-275 projectors;
- an odd/full-Fock physical compiler;
- an autonomous physical read or reset;
- one selected outcome or Born-frequency derivation;
- Record formation, physical time, energy, source, or gravity; or
- post-wrap equivalence for arbitrary instruments.

The optimal next campaign is a physical close tournament on this exact
pointer: construct a bounded local transducer whose permanent output is
matter-coupling faithful, whose close fails when `U_I` is deleted, and whose
unused coherent information and reset resources are explicit. It should keep
the total-even/preparation limitation visible rather than silently borrowing
Cycle 251 or calling the pointer itself a Record.

## Verification

Run:

```bash
python3 scripts/connected_edge_same_code_local_instrument_cycle278_2026_07_17.py
```

The runner must report zero failures. PASS totals are regression controls, not
counts of independent physical predictions.
