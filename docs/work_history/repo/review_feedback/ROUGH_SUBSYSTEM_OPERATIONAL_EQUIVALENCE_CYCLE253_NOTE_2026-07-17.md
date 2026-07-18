# Rough-subsystem operational-equivalence audit — Cycle 253

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

This review note and its runner are the only Cycle-253 artifacts.  No axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit-status
surface is edited.

## Result up front

Cycle 251's auxiliary even-CAR commutant is **exactly unobservable relative to
the restricted mapped matter-even algebra**, including the fixed
free-plus-contact update.  It is **not algebraically unobservable relative to
the full bounded local M2 algebra** of the declared physical factors.

The distinction is executable.  In each puncture cell `x`,

```text
B_aux,x = product_(a=0)^5 Z_(sink-x, direction-a)
```

is a bounded local physical M2 algebra effect of weight 6.  Its spectral
effects

```text
P_(x,+) = (I+B_aux,x)/2,
P_(x,-) = (I-B_aux,x)/2
```

separate nonempty physical-code sectors.  A bounded auxiliary hop
`A_aux,xy` of weight at most 18 exchanges the two endpoint parity outcomes,
commutes with every mapped matter operator, and preserves all code
constraints.  Therefore states related by `A_aux,xy` have identical
expectations for every mapped matter-even observable but opposite expectation
of `B_aux,x`.  The exact expectation gap is `2`, and `P_(x,+)` gives
probabilities `1` and `0` on the displayed pair.

Every `B_aux` and `A_aux` commutes with the mapped Cycle-230 update.  The
matter-even operational equivalence and the auxiliary distinction are both
preserved by that update.  The update does not dynamically erase the
auxiliary information.

That algebraic distinction is not automatically a readable experiment.  The
current framework says that the full one-site possibility domain is `M_2(C)`
and no possibility is privileged, but also that **only records are readable**.
It expressly leaves measurement, readout-context selection, local
observability, and physical-observable identification downstream.  Cycle 253
does not supply a six-site parity record instrument, record-formation rule, or
readout decoder.  Thus the framework licenses neither unconditional claim:

1. it does not license silently calling the auxiliary algebra gauge or
   unobservable; and
2. it does not license silently calling `B_aux,x` an already readable
   measurement.

The exact answer is category-relative:

- in a declared **law-selected record category** whose operational algebra is
  the mapped matter-even algebra, auxiliary states are equivalent;
- in the full bounded physical M2 algebra, they are distinct;
- in the current bare Record framework, the final readout category is open, so
  the quotient is conditional and **not automatically gauge**.

An explicit gauge twirl erases the auxiliary distinction while retaining the
matter density matrix, but the twirl is a supplied operational quotient.  It
is not a pure-state isometry E, a derived record process, or an axiom.  Cycle
251 therefore remains a strong local operator/subsystem compiler, not the
requested bounded full-Fock physical-state compiler.  There is no shared
obstruction and no axiom pressure.

## 1. Exact framework reading

The current source distinguishes possibility structure from readability:

1. Physical sites are the supplied `Z^3` sites
   (`docs/MINIMAL_AXIOMS_2026-06-29.md:35-41`).
2. Each site has the full one-site algebraic possibility domain `M_2(C)`, with
   no privileged possibility (`:43-53`).
3. A record locks one admissible local possibility; only records are readable
   (`:63-72`).
4. Choices not supplied by the structure remain conditional/open (`:74-81`).
5. Measurement, readout-context selection, local observability, and
   physical-observable identification remain outside the axioms
   (`:120-134,156-170`).

The existing Cycle-21 classification already separates the
**foundation-maximal site-record category** from a law-selected smaller
pointer category
(`FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md:19-24`).
It proves that an entangling or distributed presentation is not automatically
gauge merely because its update statistics agree; exact record-net closure is
still required (`:36-60`).  Conversely, it allows a smaller selected pointer
algebra when the law and record decoder actually supply one (`:129-152`).

Cycle 253 uses that established split.  It does not enlarge the framework's
observable principle or select a record context.

## 2. Actual rough-code distinguishers

Let `S` be the Cycle-247 rough-code stabilizer group and `A_m` the mapped
matter even-CAR algebra.  Cycle 251 constructs the complete local commutant
`A_g=A_m'` modulo `S`.  Its bounded generators are

```text
B_aux,x = product of the six puncture-spoke Z factors,
A_aux,xy = A(s_x,u_x) Ahat_(u_x,v_y) A(v_y,s_y).
```

They satisfy

```text
[B_aux,x, A_m] = [A_aux,xy, A_m] = 0,
{A_aux,xy, B_aux,x} = {A_aux,xy, B_aux,y} = 0,
[A_aux,xy, B_aux,z] = 0 for z not in {x,y}.
```

For `L=3,4,5` and held-out `L=6`, the runner finds:

| `L` | `N=L^3` | maximum `B_aux` weight | maximum `A_aux` weight | rank increment of either generator | stabilizer leakage | matter commutators |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 6 | 18 | 1 | 0 | 0 |
| 4 | 64 | 6 | 18 | 1 | 0 | 0 |
| 5 | 125 | 6 | 18 | 1 | 0 | 0 |
| 6 held out | 216 | 6 | 18 | 1 | 0 | 0 |

At `L=3`, adding either sign of `B_aux,x` to the physical stabilizers raises
rank from `406` to `407` with no phase inconsistency.  Both spectral sectors
are therefore nonempty.  Acting with `A_aux,xy` maps one sector into the other
at both endpoints while leaving the complete matter functional unchanged.

This is stronger than dimension counting.  It gives a concrete bounded
physical algebra element with distinct eigenvalues on the multiplicity
states.

### Resolution audit

The runner searches every physical weight-one Pauli at `L=3`.  None both
preserves the code and commutes with the mapped matter algebra.  It also
enumerates all `4^6` Pauli words on the six spokes of one puncture cell.  The
only nonidentity member of the code-preserving matter commutant is the
displayed weight-6 `B_aux,x`.

Therefore Cycle 253 proves a six-site bounded-block distinguisher, not a
one-site distinguisher.  It does not claim a global minimum over all mixed
face/spoke bounded ansatzes.  The two-cell auxiliary hop supplies the conjugate
distinction with weight at most 18.

## 3. Restricted matter-even operational equivalence

Let two code states be related by an auxiliary unitary:

```text
|Psi_1> = A_aux,xy |Psi_0>.
```

For every `O_m in A_m`,

```text
<Psi_1|O_m|Psi_1>
  = <Psi_0|A_aux,xy O_m A_aux,xy|Psi_0>
  = <Psi_0|O_m|Psi_0>.
```

This holds for the full algebra, not only the generator list, because
`A_aux,xy` commutes with every generator and therefore every polynomial,
adjoint, limit, and bounded functional calculus element on the finite code.

The matrix control uses the fixed Cycle-230 six-mode coin at `beta=-0.3`
from the Cycle-219 family, the Cycle-230 contact at `g=0.37`, and two
same-parity auxiliary states.  It
finds

```text
initial reduced-matter residual: 0,
post-update reduced-matter residual: 0,
[G_physical,A_aux] residual: 0.
```

Thus Cycle 251 is an exact subsystem compiler for every experiment whose
declared preparations, effects, and update words stay in the matter-even
operational algebra and do not read the auxiliary sector.

That is **restricted matter-even operational equivalence**.  It is a real
positive result and should be retained.

## 4. Full bounded local M2 distinguishability

For the same two states,

```text
<B_aux,x>_(Psi_0) = +1,
<B_aux,x>_(Psi_1) = -1.
```

The bounded effects `(I +/- B_aux,x)/2` therefore distinguish them perfectly.
The matrix residuals are exactly

```text
B expectations:               (+1,-1),
P_plus effect probabilities:  (1,0).
```

Since `B_aux,x` is a product of six Pauli `Z` elements on six declared
physical `M_2` factors, it belongs to the bounded local algebra generated by
the physical site factors.  Quotienting it away changes that algebra and is a
choice of operational category, not a consequence of the code rank.

This does not say a six-body measurement is presently selected or easy.  It
says the two pure code states are not equal as functionals on the full bounded
local M2 algebra.

## 5. Mapped update invariance

The fixed Cycle-230 physical word is generated entirely by the mapped matter
algebra.  Hence

```text
[G_physical,B_aux,x] = 0,
[G_physical,A_aux,xy] = 0.
```

The executable matrix control gives

```text
post-update B expectations:  (+1,-1),
[G_physical,B_aux,x] residual: 0.
```

The actual-graph Pauli check finds zero commutator failures against the entire
mapped matter generator family through held-out `L=6`.  The auxiliary
distinction is a conserved spectator of this supplied update.  Calling it
gauge can be operationally consistent only after the observable/readout class
is restricted; it is not justified by dynamical scrambling or deletion.

No iteration count or gate layer in this argument is physical time.

## 6. Gauge twirl and the pure-state isometry firewall

On the finite two-auxiliary-mode control, the conditional expectation

```text
T_g(rho) = (1/16) sum_(P in Pauli_2) (I_m tensor P) rho (I_m tensor P)^dagger
```

maps both auxiliary-related states to

```text
rho_m tensor I_g/4.
```

The two twirled states have residual `0`; the conditional-expectation residual
is `3.43e-17`.  This is an explicit constructive route for a declared
gauge-insensitive operational theory.

But `T_g` is a mixed channel.  It does not construct a bounded pure-state
isometry E from the Cycle-230 Fock space into the rough code.  A pure E must
choose or coherently prepare a representative in each parity-locked auxiliary
sector and must satisfy covariance and locality.  Treating every gauge density
as equivalent can eliminate the need to predict the gauge state for restricted
observables; it does not manufacture a pure encoder or a record configuration.

## 7. Record firewall

The phrase “distinguishable by `B_aux,x`” is algebraic until a record instrument
is supplied.  The current Record axiom supplies:

- occurrence of records;
- locking of one admissible one-site possibility;
- permanence and one record per site; and
- content-only additive scalar readout over disjoint records.

It does not supply:

- a `B_aux,x` measurement or preparation context;
- a rule coordinating six local `Z` records into one parity effect;
- the formation trigger or probability for either parity record;
- an auxiliary-sector readout decoder; or
- a declaration that only `A_m` is physically observable.

A future law may choose a record category blind to `A_g`, in which case the
subsystem quotient is record-faithful by construction and must be audited as
such.  A future law may instead admit the six-site parity effect or its local
record decomposition, in which case the auxiliary states are operationally
different.  Cycle 253 selects neither law.

Applying `A_aux`, copying an auxiliary bit, performing a gauge twirl, or
evaluating an expectation is not called a Record.

## 8. Covariance, locality, and held-out control

The entire `B_aux/A_aux` family is mapped into itself by all 24 proper-cubic
frames and by all coarse-cell unit translations, with zero family mismatch.
Therefore the distinguishing algebra is not a single marked measurement port.

The scope remains the supplied puncture macrocell.  Cycle 251's period-16
physical role marker and its selected sector remain supplied; this result does
not establish homogeneous unit translation on undifferentiated physical
sites.

The exact weights and commutators persist at held-out `L=6`, so the distinction
is not a trained-size artifact.

## 9. Supplied-structure and deletion inventory

Supplied rather than derived:

1. the Cycle-230 six-mode Fock cell, fixed coin/contact parameters, and update
   order;
2. the Cycle-235 square-pyramid physical placement and stabilizer convention;
3. the Cycle-247 puncture sinks, rough terminals, and stream dressing;
4. the Cycle-251 `B_aux/A_aux` dictionary and parity-locked subsystem reading;
5. the puncture macrocell, period-16 physical marker, incident order, and
   ordering-gauge repair;
6. the choice of operational algebra: mapped matter only, full bounded local
   M2, or a record-selected subalgebra;
7. the two auxiliary code sectors used by the discriminator;
8. the six-site spectral effect if it is promoted from algebraic effect to a
   record instrument;
9. the full auxiliary Pauli gauge twirl and its uniform weights;
10. any pure gauge representative, parity-sector identification, or state
    preparation used by a future E; and
11. ordinary finite-dimensional quantum states and expectation functionals.

Deletion controls and discriminators:

- restrict effects to `A_m`: auxiliary-related states have residual `0`;
- add the bounded `B_aux,x` effect: expectation gap becomes `2`;
- apply the supplied full gauge twirl: the full density-matrix residual returns
  to `0` while the matter state is unchanged;
- delete the rough stream dressing: Cycle 251 finds exactly two local code
  violations;
- delete one independent physical code constraint: one logical direction is
  added;
- delete the record instrument: algebraic distinguishability remains, but no
  readable experiment has been supplied; and
- delete a pure gauge preparation: the subsystem channel remains meaningful,
  but no pure-state E has been defined.

## 10. Prior-result and novelty boundary

Cycle 21 supplies the maximal-site versus law-selected record-category split.
Cycle 249 supplies the precedent that retaining a coherent gauge orbit can
avoid selecting a deterministic section while leaving absolute base/topology
preparation separate.  Cycle 251 supplies the exact auxiliary commutant and
sectorwise update independence.

Cycle 253's new content is limited to:

1. the actual-code `+/-B_aux,x` sector consistency and bounded-hop state-pair
   discriminator;
2. the complete weight-one and six-spoke Pauli resolution control;
3. exact restricted-density versus full-effect residuals for the fixed update;
4. the explicit gauge-twirl conditional expectation; and
5. the framework-specific classification of algebraic, readable, and
   pure-isometry claims.

No external prior-art engine is used and no physical-observable principle is
imported.

## 11. Dependency ledger

| wall | Cycle-253 disposition |
|---|---|
| `C_ref` | sharpens: operational algebra, record context, gauge twirl, macrocell, and physical marker are explicit choices | no law-selected record category or gauge representative is derived |
| `C_num` | unchanged algebraic gain: `N-1` auxiliary multiplicity is exact and may be quotiented for restricted effects | quotienting does not give a pure E or select the parity-correlated representative |
| `C_wrap` | unchanged | no clock, physical energy, phase direction, or realized winding is derived |
| `C_int` | gain: the fixed free-plus-contact update is exactly auxiliary-independent for matter effects | the conserved auxiliary effect remains available in the full local algebra |
| `C_local` | sharp gain: explicit weight 6 and weight 18 physical distinguishers, zero restricted residual, all-frame family, held-out `L=6` | final record/observable category and bounded pure-state E remain open |
| `C_source` | unchanged | no resource, source, stress, or gravity law is supplied |

The optimal next question is operational rather than another rank census:
does the proposed physical law derive a record instrument whose effect algebra
is exactly `A_m`, or does it admit bounded auxiliary parity effects?  In
parallel, a pure local E remains useful if the campaign insists on physical
state preparation rather than subsystem equivalence classes.

## 12. No-go discipline N1–N8

The narrow negative statement under audit is:

> The present framework does not by itself license an unconditional
> identification of every Cycle-251 auxiliary state as gauge-equivalent.

This is not a no-go against a law-selected matter-even quotient.

### N1 — Alternative-route enumeration

| route | marker | disposition |
|---|---|---|
| restrict all preparations/effects to the mapped matter-even algebra | **ATTEMPTED** | succeeds exactly: reduced-state residual is zero before and after the update; the conclusion becomes a conditional equivalence |
| retain the full bounded local M2 algebra | **ATTEMPTED** | `B_aux,x` gives expectation gap `2`; unconditional equivalence fails in this category |
| supply a six-site auxiliary parity record instrument | **ATTEMPTED** | the exact spectral effects are constructed, but formation/readout implementation is not supplied; this route would make the states readable and distinct |
| quotient by the full auxiliary gauge twirl | **ATTEMPTED** | succeeds as a mixed operational channel with residual zero; it does not supply a pure E |
| retain the coherent auxiliary orbit without a section | **ATTEMPTED / PARTIAL** in Cycles 249 and 251 | succeeds for gauge-independent even predictions but leaves absolute gauge preparation and parity-sector identification open; no pure-E route is ruled out |
| fix all nonroot auxiliary parities | **ATTEMPTED** in Cycle 251 | rank-matches and keeps both parities, but this selector chooses a marked root and breaks coarse translations |
| impose covariant nearest-neighbor auxiliary parity equalities | **ATTEMPTED** in Cycle 251 | rank-matches, but this selector loses the odd matter sector at `L=4,6` |
| transport the full site/record net as a law-relative groupoid | **ATTEMPTED** at the category level by Cycle 21 | can make a larger quotient exact only after site, record, boundary, decoder, and readout closure; those data are not supplied here |

Multiple routes positively support a conditional subsystem interpretation, so
no broad unobservability no-go can ship.

### N2 — Wall-independence audit

After collapsing downstream wording, two conditions remain:

- `K_obs`: specify and close the physical preparation/effect/record algebra;
- `K_E`: if a pure-state compiler is required, construct a bounded local
  parity-correlated isometry and preparation.

| pair | does closing first close second? | does closing second close first? | independent? |
|---|---|---|---|
| `K_obs`, `K_E` | no: a matter-only quotient or gauge twirl defines predictions without a pure encoder | no: choosing one pure representative does not decide whether `B_aux` is observable | yes |

Record-instrument selection is part of `K_obs`, not inflated into a third
independent wall.  The period-16 marker remains a supplied placement condition
but is not used to prove this operational distinction.

### N3 — Hidden-wall scan

The mandatory phrase scan classifies the load-bearing choices: the framework
provides the M2 possibility domain and Record rules only by direct citation;
“physical observable” is narrowed to “physical M2 algebra effect” unless a
record instrument is supplied; “gauge” always names a declared operational
quotient; “by construction” is replaced by exact commutator/rank residuals;
and the background macrocell, marker, state preparation, update parameters,
and twirl weights are in the supplied inventory.  No standard-QFT,
measurement, Born, decoherence, or Record import is hidden.

### N4 — Residual matching

| witness | witness residual | Cycle-253 residual | match? |
|---|---|---|---|
| `MINIMAL_AXIOMS_2026-06-29.md:43-79` | physical site possibility domain and Record readability | distinguishes algebra membership from readable effect | yes |
| same file `:120-170` | measurement, local observability, and physical-observable identification remain downstream | prevents promotion of `B_aux` to an already selected record effect | yes |
| `FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md:19-60,129-152` | maximal-site versus law-selected record categories; no automatic gauge quotient | classifies the auxiliary quotient as record-category-relative | yes |
| `ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md:15-54,94-143` | exact commutant and sectorwise factorization, no bounded E | tests whether the commutant is also operationally invisible | yes, distinct next interface |
| same file `:226-247` | fixed update is auxiliary-independent sectorwise | verifies update-invariant restricted equivalence and conserved full-algebra distinction | yes |
| Cycle 251 `:188-208` | two local selector failures | retains them only as route-specific controls | yes |

No mass, energy, Born, or Record-formation residual is cited as evidence for
the observable-category conclusion.

### N5 — Rhetoric audit

| resolution | exact test | conclusion |
|---|---|---|
| one physical M2 factor | all weight-one Paulis at `L=3` | no code-preserving matter-commutant element found; no one-site distinguisher claimed |
| one six-spoke puncture block | exhaustive `4^6` Pauli census | unique nonidentity commutant word is weight-6 `B_aux` |
| two neighboring puncture cells | explicit `A_aux,xy` | weight at most 18, flips exactly two `B_aux` outcomes |
| finite full code | signed stabilizer ranks and exact matrix effects | both sectors nonempty; expectation gap `2` |
| `L=3,4,5,6` lattice families | rank, support, commutator, frame, translation tests | bounded family persists, including held-out size |
| all possible bounded mixed-face distinguishers | not enumerated | no global minimum-support or universal measurement no-go claimed |

The note says “not automatically gauge,” not “cannot be gauge.”

### N6 — Partial-closure path scan

No new axiom is needed to use the positive result.  A downstream law can:

1. declare `A_m` as its operational effect algebra and treat `A_g` as gauge;
2. provide a record-faithful conditional expectation/twirl;
3. retain the full coherent auxiliary orbit and formulate states as subsystem
   equivalence classes; or
4. add a supplied auxiliary record instrument and keep the sectors physical.

These are definitions/bridges inside a completed law, subject to record-net
audit.  They are not automatic consequences of the four axioms and not
candidate axiom pressure.

### N7 — Steelman

> Only records are readable, Cycle 230 uses only even matter operators, and no
> auxiliary record instrument has been selected.  Therefore demanding equality
> on the full microscopic M2 algebra may be operationally gratuitous: the
> Cycle-251 code already supplies every prediction the declared experiment can
> ask, and the auxiliary CAR should simply be treated as gauge.  Cycle 249's
> coherent-retention mechanism shows that one need not choose a gauge section
> to run an exact local quantum protocol.

This steelman is persuasive **conditional on declaring the matter-only record
category**.  It defeats any broad claim that a pure E is necessary for every
operational use.  It does not defeat the narrow conclusion: the current
foundation does not itself select that category, and the bounded `B_aux`
effect proves that the quotient changes the full local algebra.

### N8 — Cross-cycle echo

- Cycle 21 separated foundation-maximal, selected-pointer, and transported-net
  equivalences; selected records retired some apparent distinctions only after
  the category was declared.
- Cycle 249 retained a coherent gauge orbit instead of selecting a
  deterministic section, while preserving its base/topological preparation
  firewall.
- Cycle 251 converted the rough multiplicity into an exact local auxiliary
  even-CAR commutant and proved sectorwise update independence.
- Cycle 253 shows that this algebraic subsystem result already closes
  matter-even operational predictions, while full local-algebra and Record
  equivalence remain category choices.

The recurring route for retiring representation walls is an explicit
record-faithful operational quotient, not an axiom and not silent deletion.
Because that route remains live and constructive, there is no general
unobservability obstruction and no axiom pressure.

## Time firewall

The fixed update word, its onsite/stream/contact layers, state preparation,
auxiliary hop, Pauli twirl, effect evaluation, circuit depth, and iteration
count are algebraic or compiler coordinates.  None is causal time, proper
time, physical frequency, physical energy, a generator rate, a Record, or
realized history.  The runner does not interpret schedule ordering as time.

## Executable artifact

```text
scripts/rough_subsystem_operational_equivalence_cycle253_2026_07_17.py
```

The runner checks source contracts, actual rough-code sector consistency,
bounded local distinguishers, single-site and six-spoke resolution controls,
restricted density-function equivalence, full-effect distinguishability,
mapped update invariance, an explicit gauge twirl, all 24 frames, coarse
translations, and held-out `L=6`.
