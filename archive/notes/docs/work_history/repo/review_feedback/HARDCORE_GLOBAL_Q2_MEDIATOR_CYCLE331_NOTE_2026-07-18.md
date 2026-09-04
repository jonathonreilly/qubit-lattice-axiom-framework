# Hard-core global-Q2 mediator compiler — Cycle 331

Date: 2026-07-18
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/hardcore_global_q2_mediator_cycle331_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 331 constructs an exclusion-preserving hard-core global Q=2 mediator
sector on the Cycle-328/Cycle-315 complete matter seam. One M2 represents each
mediator direction mode and double occupation of a mode is forbidden. Both
reservoirs are initially occupied and both endpoint source vertices act in the
same two-update protocol.

The direct projected bosonic coin does not close the hard-core sector. Its
projected two-particle unitarity residual is `1.9876159799998123`, and the
largest discarded double-occupation probability is
`0.2962962962962965`. This failure is route-specific to projection of the
Cycle-214 bosonic two-particle lift.

An explicit covariant alternative succeeds. The collision-conditioned
hard-core completion applies the inherited Cycle-214 field coin when exactly
one mediator occupies a cell and identity on onsite Q2, the 15-dimensional
two-distinct-direction sector. It is exactly unitary and has zero covariance
residual under all 24 proper-cubic frames. The identity-on-onsite-Q2 choice is
a supplied collision rule, not a derived statistics law.

On the declared code, in both endpoint roles,

```text
E_hc G_hc = G_physical,hc E_hc.
```

The forward residual is `1.424451840365576e-15`; the inverse residual is
`2.467582322780598e-15`. The hard-core response is lawful, normalized,
nonfactorizing, translation covariant, and stable through held `L=6`.
It is a nonfactorizing occupation response on the common code.

At `L=6`:

```text
<R_A> = 0.7715478142474343
<R_B> = 0.7715478142474342
<R_A R_B> = 0.5929377077947355
connected covariance = -0.0023483218752577972
both-field probability = 0.0498420792998697.
```

Joint survival equals the Cycle-328 bosonic value at this precision, but the
reservoir means, connected covariance, and both-field probability differ. The
joint differs from the labelled Cycle-328 value by
`-2.0649909050374227e-05`. Thus the full response vector, not every individual
component, distinguishes the tested statistics/coin laws.

These are finite occupation responses. They are not force, not energy, not
stress, not gravity, not metric response, and not time. The construction does
not select hard-core statistics as physical.

## Hard-core source code and exact ledgers

The source-sector one-body modes are reservoirs `R_A,R_B` and mediator modes
`F_(x,d)`. A lawful Q2 label is a pair of distinct modes. The endpoint source
exchange is

```text
T_X = sum_d (
        c^dagger_X,reverse(d) c_X,d sigma^+_(X,d) sigma^-_(R_X)
      + h.c.
      ).
```

Creation is blocked when the target mediator mode is occupied. The local Q1
source block has dimension 448; the local hard-core Q2 block has dimension
1,344. Both generators preserve exactly

```text
Q,
N_matter,
P = P_matter + 2 P_mediator.
```

| local charge | Hermiticity | `[T,Q]` | `[T,N]` | largest `[T,P_i]` | largest frame residual |
|---:|---:|---:|---:|---:|---:|
| 1 | `0` | `0` | `0` | `0` | `0` |
| 2 | `0` | `0` | `0` | `0` | `0` |

The coefficient two and source angle remain supplied. Unit-weight hard-core Q2
is open.

## Coin tournament

The Cycle-214 one-particle coin is proper-cubic and unitary. Its symmetric
two-boson lift creates double occupation from distinct input directions. After
discarding those outputs, the remaining 15-by-15 matrix is nonunitary. A
projection plus renormalization would be state dependent and is not retained.

The retained local completion is block diagonal by onsite mediator number:

```text
C_hc^(0) = 1,
C_hc^(1) = C_214,
C_hc^(2) = I_15.
```

Every block is unitary. Onsite number is locally readable from the six
hard-core M2, so no host collision query is needed. Nevertheless, the Q2
identity block is extra law content. A uniform hard-core XY coin or another
interacting completion can give a different response and remains open.

The direction-preserving stream is a permutation of hard-core modes and cannot
create double occupation. The complete update order is matter coin, hard-core
field coin, sources A/B, FSWAP, stream, and actual contact.

## Response and Cycle-328 comparison

The preparation and readout match Cycle 328: symmetric one-one matter, both
reservoirs occupied, two updates, then reservoir means, joint survival,
connected covariance, and both-field probability.

| L | role | `<R_A R_B>` | connected covariance | both fields | lawful leakage | norm drift |
|---:|---|---:|---:|---:|---:|---:|
| 3 | training | `0.5929377077947355` | `-0.0023483218752577972` | `0.0498420792998698` | `0` | `7.10543e-15` |
| 4 | training | same | same | `0.0498420792998697` | `0` | `1.13243e-14` |
| 6 | held | same | same | `0.0498420792998697` | `0` | `1.13243e-14` |

The separate-Q1 survival product is `0.59479432751664`; the hard-core joint
difference is `-0.001856619721904429`.

Comparison with the bosonic and labelled Cycle-328 values:

| statistic/law | joint survival | connected covariance | both fields |
|---|---:|---:|---:|
| bosonic | `0.5929377077947355` | `-0.001529375553990353` | `0.05090387762274617` |
| independently labelled | `0.5929583577037859` | `-0.0018359698128539437` | `0.05050015403454247` |
| hard-core collision-conditioned | `0.5929377077947355` | `-0.0023483218752577972` | `0.0498420792998697` |

Equal bosonic/hard-core joint survival does not make the protocols equivalent;
the means, covariance, both-field probability, lawful supports, and local coin
laws differ.

## Physical common code and support

The sparse reachable hard-core labels tensor the complete 4,096-state matter
seam. The physical lift uses Cycle 315's AB/BA matter encodings and bounded
matrix-unit completions, with hard-core occupation labels as supplied
orthogonal factors.

| edge role | forward EG | inverse EG | encoded norm | output norm |
|---|---:|---:|---:|---:|
| AB | `1.42445e-15` | `2.46758e-15` | `1.0000000000000038` | `0.9999999999999968` |
| BA | `1.42445e-15` | `2.46758e-15` | `1.0000000000000038` | `0.9999999999999968` |

| L | role | ambient hard-core Q2 | reachable labels |
|---:|---|---:|---:|
| 3 | training | 13,366 | 1,712 |
| 4 | training | 74,305 | 1,819 |
| 6 | held | 841,753 | 1,819 |

The hard-core source needs one reservoir M2 and six mediator M2 per cell in
addition to the 29-M2 matter substrate: 36 M2 per cell and a 97-M2 two-cell
patch. This is sufficient bounded support, not a minimum theorem. Primitive
synthesis of every Q-sector factor remains supplied/open.

## Covariance, translations, deletions, and firewalls

The source, Q1 coin, Q2 identity coin, stream, and matter seam cover all 24
proper-cubic frames. Twelve include endpoint reversal. The inherited raw seam
covariance maximum is `2.16778e-16`; hard-core source and coin frame residuals
are zero.

All L=3 translations are tested. The 27-response maximum residual is
`7.10543e-15`.

Deleting source B leaves `<R_B>=1.0000000000000044`. Contact remains
nontrivial on 4,047 columns and has deletion norm `1.9911500883709052`.
Deleting contact changes the selected two-depth joint survival by zero, so the
contact firewall is retained but the response does not identify contact.

The mass firewall remains

```text
Cycle-219 mass = two-cell mass = 0.4534056541748851,
eigenvector residual = 3.85718e-16.
```

## Supplied structure, derived results, and open work

Supplied structure:

- complete Cycle-315 matter seam, FSWAP, and actual contact;
- hard-core mediator statistics and exclusion rule;
- coefficient-two source and angle;
- Cycle-214 Q1 mediator coin;
- identity-on-onsite-Q2 collision rule;
- both-reservoir preparation, two-update schedule, and response readout;
- sparse reachable restriction, physical occupation factors, and sizes.

Derived here:

- exact Q/N/vector source ledgers and proper-cubic covariance;
- exact hard-core lawful-sector and norm closure;
- AB/BA physical EG and held-size behavior;
- nonfactorizing response and comparison with both Cycle-328 statistics;
- source deletion, translations, support, mass, and contact firewalls.

Open:

- derivation or operational selection of the collision-conditioned coin;
- uniform hard-core XY or other interacting coins;
- fermionic antisymmetric mediator statistics;
- unit-weight hard-core Q2 or paired mediators;
- multi-edge recurrence and primitive Q-factor synthesis;
- a contact-sensitive observable;
- physical calibration as force, energy, stress, gravity, metric response, or
  time.

## TOE dependency ledger and maturity

| wall | Cycle-331 effect | remaining import |
|---|---|---|
| `C_ref` | hard-core response shares the Cycle-328 simultaneous preparation/readout | preparation, depth, and observable remain supplied |
| `C_num` | exclusion-preserving Q2 closure is explicit through held L6 | statistics/coin selection, higher Q, and multi-edge closure remain open |
| `C_wrap` | unchanged | schedule and update count are not time or rate |
| `C_int` | hard-core source has exact coefficient-two ledgers and actual contact | coefficient, coin completion, and contact-sensitive readout supplied/open |
| `C_local` | 36-M2-per-cell, 97-M2-patch candidate closes AB/BA EG | primitive Q-factor synthesis and multi-edge overlap open |
| `C_source` | third simultaneous statistics/coin law gives a distinct full response vector | no statistics selection, unit-weight Q2, calibration, or metric response |

The third exact statistics route advances source-law discrimination but adds a
supplied collision rule. Conservative scores are:

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 65% | 31% | 92% | 3.6/5 |
| causal time / clock | 36% | 18% | 66% | 2.0/5 |
| inertia / matter | 76% | 37% | 97% | 4.3/5 |
| gravity / source / resource | 42% | 17% | 70% | 2.3/5 |
| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 |

## No-Go Discipline Gate

The broad candidate negative is that a covariant exclusion-preserving hard-core
Q2 source cannot close on the common physical seam. The collision-conditioned
completion is a bounded counterexample. The failure of the directly projected
bosonic coin applies only to that projection. Stronger claims about coin
selection, fermionic statistics, unit weights, contact-sensitive observables,
or calibration retain open routes.

Gate status: **FAIL / DO NOT SHIP** the broad negative. There is no shared
obstruction and no axiom pressure.

### N1 — alternative routes

| route | marker | actual disposition |
|---|---|---|
| direct projected bosonic hard-core coin | **ATTEMPTED** | projection leaks double occupation up to `0.296296` and has unitarity residual `1.98762` |
| collision-conditioned hard-core completion | **ATTEMPTED** | exact Q1 Cycle-214/Q2 identity completion, common-code EG, and nonfactorizing response |
| uniform hard-core XY coin | **OPEN / UNTESTED** | no interacting XY angle or response compiler is selected |
| fermionic antisymmetric mediator | **OPEN / UNTESTED** | no exterior field lift or sign/frame audit is built |
| independently labelled mediator | **ATTEMPTED** | Cycle 328 succeeds with supplied A/B species labels |
| bosonic mediator | **ATTEMPTED** | Cycle 328 succeeds with supplied symmetric statistics and double occupation |
| unit-weight hard-core Q2 | **OPEN / UNTESTED** | coefficient two remains in the source ledger |
| contact-sensitive hard-core observable | **OPEN / UNTESTED** | selected joint survival is unchanged by contact deletion |

### N2 — wall-independence audit

The stronger theorem walls are coin selection `W_coin`, statistics selection
`W_stats`, unit-weight completion `W_unit`, contact identification `W_contact`,
and physical calibration `W_energy`.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---|---|---|
| `w_coin`, `w_stats` | no | no | yes |
| `w_coin`, `w_unit` | no | no | yes |
| `w_coin`, `w_contact` | no | no | yes |
| `w_coin`, `w_energy` | no | no | yes |
| `w_stats`, `w_unit` | no | no | yes |
| `w_stats`, `w_contact` | no | no | yes |
| `w_stats`, `w_energy` | no | no | yes |
| `w_unit`, `w_contact` | no | no | yes |
| `w_unit`, `w_energy` | no | no | yes |
| `w_contact`, `w_energy` | no | no | yes |

No directed implication collapses another wall.

### N3 — hidden-wall scan

The executable scan covers note and runner and reports zero hits. The supplied
inventory exposes exclusion, source, coefficient, Q1 coin, Q2 identity block,
preparation, schedule, sparse restriction, physical factors, sizes, and
readout.

### N4 — residual matching

| witness | boundary | Cycle-331 treatment | match? |
|---|---|---|---|
| `GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CYCLE328_NOTE_2026-07-18.md:360` | hard-core route open | exact route constructed | yes |
| same file, line 47 | bosonic statistics supplied | projection comparator | yes |
| same file, line 49 | labelled statistics supplied | retained response comparator | yes |
| same file, line 75 | contact not identified | same firewall retained | yes |
| `PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md:26` | complete Fock seam | 4,096 matter states per label | yes |

Projection leakage is not used against interacting hard-core coins, fermionic
fields, or labelled species. Equality of one joint component is not used to
claim bosonic/hard-core equivalence.

### N5 — rhetoric audit

“Hard-core” names the supplied exclusion code; it does not claim physical
statistics selection. “Collision-conditioned” exposes extra law content.
Response differences are occupation differences, not force or energy.

### N6 — partial-closure paths

Live routes include uniform XY coins, fermionic exterior fields, unit-weight
Q2 auxiliaries, paired mediators, contact-sensitive depths/readouts, multi-edge
closure, and operational statistics selection.

### N7 — hostile steelman

A hostile reviewer should reject necessity or uniqueness claims for the Q2
identity coin, 36 M2 count, or hard-core statistics. Many covariant onsite
two-particle unitaries exist. The retained identity is one sufficient bounded
completion selected for a clean discriminator.

### N8 — cross-cycle echo

Cycle 328 showed bosonic and labelled Q2 closure. Cycle 331 tests the open
hard-core wall, falsifies only naive projection, and closes a different
covariant completion. Fermionic and unit-weight routes remain live. The broad
gate remains **FAIL / DO NOT SHIP**.

## Optimal next campaign

Test a nontrivial proper-cubic hard-core XY coin against the identity collision
block, or construct the fermionic antisymmetric mediator. Demand the same
ledgers, EG, response vector, frames, translations, held sizes, deletions, and
firewalls. No response difference should be called force, energy, stress,
gravity, metric response, or time.

## Verification

```text
python3 scripts/hardcore_global_q2_mediator_cycle331_2026_07_18.py
```

Expected result:

```text
RESULT HARDCORE_GLOBAL_Q2_MEDIATOR_CERTIFIED
```
