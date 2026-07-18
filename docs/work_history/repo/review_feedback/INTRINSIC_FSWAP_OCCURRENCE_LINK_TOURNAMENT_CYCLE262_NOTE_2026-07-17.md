# Intrinsic FSWAP occurrence-link tournament — Cycle 262

**Date:** 2026-07-17

**Type:** exact finite three-route constructive tournament with bounded
split-fault controls

**Status:** three exact ideal constructions; no unconditional certificate that
the FSWAP acted on the named data invocation

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

Companion runner:

```text
scripts/intrinsic_fswap_occurrence_link_tournament_cycle262_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit surface.

## Result up front

Cycle 262 tests three independent bounded ordinary-`M_2` routes for linking a
coherent close carrier to the **actual Cycle-230 two-mode FSWAP invocation**:

1. a pointer coupled to the same FSWAP bond generator eigenspaces;
2. a two-query Choi comb routed through the same physical bond; and
3. an exactly verified two-rail encoded FSWAP gadget with local syndromes and
   an explicit component-fault family.

All three have exact constructive content. Route A has an input-independent
nondemolition pointer for arbitrary lawful data. Route B applies FSWAP to the
data and to a Choi probe by two invocations of the same physical bond. Route C
has an isometric two-rail code and a ten-site local gadget satisfying

```text
G_gadget E_rep = E_rep FSWAP
```

with zero leakage. The runner supplies bounded collision-free placements and
checks every declared bond after one translation in all 24 proper-cubic
frames.

None of these ideal constructions passes the stronger occurrence-link test:
delete only the factor that acts on the named data while leaving auxiliary
factors alive. In Route A the constant pointer remains one. In Route B the
second invocation still returns the exact FSWAP Choi carrier after the first,
data invocation is deleted. In Route C independent component flags can remain
present while a rail or phase component is deleted; moreover phase deletion
and full-gadget deletion preserve the code and pass both equality syndromes.
These are explicit false positives, not numerical near misses.

The tournament therefore improves the constructive boundary but does **not**
establish a route-independent obstruction. Every tested route uses an
after-the-fact auxiliary carrier whose coupling to the named data invocation
is supplied and factorable. An intrinsic environment/history monitor, a
different verified primitive, a process-comb construction with inseparable
invocation identity, or a local actualization mechanism remains live. The
negative result is restricted to the three declared constructions and their
declared fault families. There is **no axiom pressure**.

Coherent carriers are not Records. Projector weights are not Born
probabilities. A finite circuit order is not physical time, and no generator
coefficient is called a rate. Three-dimensional space remains supplied by the
Lattice axiom rather than derived here.

## 1. Source and scope boundary

The current minimal axioms supply physical `Z^3`, nearest-neighbor adjacency,
translations, proper-cubic rotations, the one-site algebra `M_2(C)`, one fixed
covariant local admissibility rule, and the fact that Records form and are
permanent. They do not select a Hamiltonian or update, a fresh-site
preparation, an occurrence monitor, a Record-formation map, a probability
rule, a time metric, or a rate.

The predecessor chain used here is deliberately narrow:

- Cycle 230 supplies the actual local two-mode CAR FSWAP and contact/seam
  fixture; it does not supply an ordinary-site occurrence monitor.
- Cycle 243 separates coherent event, physical close, commit, and Record
  formation. This cycle tests only the event-to-close seam.
- Cycle 259 supplies the strongest preceding flag-plus-Choi close and its
  decisive split fault: deleting the data factor while auxiliaries survive.
- The bounded pointer-conservation note supplies a controlled-copy firewall,
  not a selected pointer or a Record law.
- The record/history/order/time/rate firewall forbids renaming circuit order
  as time or a coherent close carrier as a Record.

The runner rereads these sources and the minimal axioms. No Thirring engine is
used or compared. Standard FSWAP algebra, Choi-state testing, repetition-code
syndromes, and signed-permutation cubic frames are prior mathematical tools.
The repo-local novelty is only their exact juxtaposition against the
Cycle-259 data-factor-only fault and the resulting dependency ledger. No
priority claim is made.

## 2. Common FSWAP fixture and tests

In occupation order `|00>, |01>, |10>, |11>`, the supplied gate is

```text
     [1 0 0  0]
F =  [0 0 1  0]
     [0 1 0  0]
     [0 0 0 -1].
```

The runner verifies exactly

```text
F^dagger F = I,  F^2 = I,  F = F^dagger,
[F,(-1)^N] = 0, Tr F = 0.
```

It also retains the Cycle-259 two-dimensional local fixture

```text
E_local |0_L> = |00>,
E_local |1_L> = |11>,
F E_local = E_local Z_L,
```

with zero intertwining residual and zero leakage. This is a two-mode local
fixture, not the missing global CAR compiler.

For this tournament, a route passes the strong occurrence-link test only if:

- its ideal map is exactly nondemolishing on arbitrary lawful data;
- its close carrier accepts the ideal named data invocation;
- deleting only that data factor, while declared auxiliaries survive, is
  rejected;
- keeping the data action while deleting a close factor does not silently
  turn a valid event into a claimed occurrence certificate; and
- all preparation, constraints, placement, covariance, and fault-domain
  imports are explicit.

The last-but-one bullet records false negatives separately; it does not make
them equivalent to false positives.

## 3. Route A — same-bond interaction-current pointer

Define the exact FSWAP eigenspace projectors and one supplied generator by

```text
P_+ = (I+F)/2,
P_- = (I-F)/2,
H_F = pi P_-,
exp(-i H_F) = P_+ - P_- = F.
```

This is a same-bond generator decomposition. Calling its projector coupling
an interaction-current **candidate** does not derive a physical current from
the framework.

### Exact nondemolition arm

With a fresh pointer qubit, the isometry

```text
V_product = F tensor |1>
```

implements the ideal FSWAP channel on every data density matrix and leaves a
fixed pure pointer. Equivalently it is the fresh-`|0>` restriction of the
supplied unitary `F tensor X_pointer`. Tracing out the pointer returns
`F rho F^dagger` exactly.

The data-factor-only deletion is

```text
V_product -> I tensor |1>.
```

The auxiliary survives and its reduced state is still `|1><1|` exactly, while
the data channel is wrong. On seeds `262,263,264,999`, the data residuals are

```text
0.6103484381443923
0.8161271130036260
0.5008268574045632
0.7350726405290439
```

and every pointer residual is zero. The zero residual for arbitrary data is
an operator identity; the four states are regression and held-out controls,
not the basis of that claim.

### Eigenspace-sensitive arm

The sensitive alternative is

```text
V_sensitive = F P_+ tensor |0> + F P_- tensor |1>.
```

Its pointer depends on the FSWAP eigenspace, but tracing it out dephases
coherence between `P_+` and `P_-`. For the same four inputs, the ideal-data
residuals are respectively

```text
0.3051742190721961
0.4080635565018130
0.2504134287022816
0.3675363202645219.
```

Thus this exact candidate is sensitive but fails arbitrary-data
nondemolition. It does not prove that every possible same-bond monitor must
fail.

The after-the-fact data-only control remains exact: `|00>` and
`(|01>+|10>)/sqrt(2)` are lawful `+1` FSWAP eigenstates, so identity and FSWAP
have identical final density matrices on both. That only excludes a uniformly
faithful effect whose sole input is final data; it does not exclude a live
interaction or environment monitor.

**Route-A disposition:** exact bounded ideal partial; the constant pointer is
spoofed by split deletion and the tested sensitive pointer is demolishing.

## 4. Route B — same-bond two-query Choi comb

Let `D` be the two data modes, `P` two stored probe modes, and `R` two
reference modes. Prepare

```text
|Phi_4>_PR = (1/2) sum_j |j>_P |j>_R
```

by two Hadamards and two nearest-neighbor CNOTs on four fresh ordinary
`M_2` sites. The target Choi vector and effect are

```text
|J_F> = (F_P tensor I_R)|Phi_4>,
Q_F = |J_F><J_F|.
```

The data and probe do not use two abstractly named FSWAP gates. They are
routed through the same physical two-site bond:

```text
1. invoke F on the physical bond holding D;
2. swap registers D and P through a supplied bounded local routing network;
3. invoke F again on that same physical bond, now holding P;
4. undo the register routing.
```

The total ideal map is exactly `F_D tensor F_P tensor I_R`. Hence the data is
nondemolished relative to the ideal FSWAP channel for arbitrary lawful data,
the probe is exactly `Q_F`, and its projector weight is one.

Invocation-specific deletion exposes the link gap:

| case | `Q_F` weight | data residual from ideal |
|---|---:|---:|
| ideal | `1` | `0` |
| first/data invocation deleted | `1` | `0.6103484381443923` |
| second/probe invocation deleted | `0` | `0` |
| both invocations deleted | `0` | `0.6103484381443923` |

The first fault is the decisive false positive: same physical bond identity
does not make the second invocation evidence that the first invocation acted.
The second fault is a false negative for a close rule that requires the Choi
carrier.

Two held routing deletions each give `Q_F` weight `1/16 = 0.0625`, data
residual `0.5262607663572775`, and nonzero probe residual. They are visible
faults and do not mimic exact completion.

For the diagnostic invocation

```text
U(theta) = cos(theta) I - i sin(theta) F,
```

the exact `Q_F` weight is `sin(theta)^2`, because `Tr F=0`. The runner checks
`theta=0, pi/6, pi/4, pi/2` and the held-out value `pi/7`, whose weight is
`0.18825509907063323`.

**Route-B disposition:** exact same-bond, same-gate-family, arbitrary-data
partial; invocation identity remains factorable, so the Choi carrier certifies
the diagnostic invocation rather than the named data invocation.

## 5. Route C — verified encoded FSWAP gadget

Encode two logical occupation bits into two repetition rails:

```text
E_rep |a b> = |a a b b>,
physical order = (a_0,a_1,b_0,b_1).
```

Fresh rails in `|a 0 b 0>` are locally prepared by `CNOT_(a0,a1)` and
`CNOT_(b0,b1)`. The code is locally enforced by the nearest-neighbor equality
stabilizers

```text
S_a = Z_(a0) Z_(a1),
S_b = Z_(b0) Z_(b1).
```

The supplied three-component physical gadget is

```text
G_gadget = CZ_(a0,b0) FSWAP_(a0,b0) FSWAP_(a1,b1).
```

All components commute in this fixture. The runner checks all six component
schedules and obtains

```text
||G_gadget E_rep - E_rep F|| = 0,
||(I-E_rep E_rep^dagger) G_gadget E_rep|| = 0.
```

This is the strongest new constructive result of the tournament: a bounded
ordinary-`M_2`, locally constrained, zero-leakage logical FSWAP gadget. Its
physical two-site component unitaries and scheduling are supplied; the result
does not derive them from the current admissibility rule.

The explicit bounded fault family gives:

| data fault | min/max code-acceptance weight | leakage norm | logical residual |
|---|---:|---:|---:|
| omit rail 0 | `0 / 1` | `sqrt(2)` | `2 sqrt(2)` |
| omit rail 1 | `0 / 1` | `sqrt(2)` | `2 sqrt(2)` |
| omit phase | `1 / 1` | `0` | `2` |
| omit full gadget | `1 / 1` | `0` | `2 sqrt(2)` |
| held: omit rail 0 and phase | `0 / 1` | `sqrt(2)` | `2` |
| held: omit rail 1 and phase | `0 / 1` | `sqrt(2)` | `2` |
| held: only phase survives | `1 / 1` | `0` | `2` |

Rail omissions are detectable on some inputs but have a unit-acceptance
lawful subspace, so they are not rejected uniformly over arbitrary lawful
data. Phase deletion, full-gadget deletion, and the held phase-only fault stay
inside the code and pass both equality checks on every code state while
implementing the wrong logical channel.

If three independent coherent component flags survive their corresponding
data-component deletions, all seven nonideal data faults have some input with
unit code acceptance: seven explicit false-positive rows. Conversely, deleting
any one flag while the ideal data gadget acts creates three explicit false
negatives for an all-flags-required close. These flags and syndrome carriers
are coherent projectors, not Records.

**Route-C disposition:** exact verified logical FSWAP and useful leakage
diagnostics, but no fault-independent occurrence link. A code syndrome checks
code membership, not the full logical operation.

## 6. Ordinary-M2 placement and covariance audit

The runner gives a concrete collision-free placement for each route. Site
counts and maximum base-coordinate `L1` radii are:

| route | ordinary `M_2` sites | radius | local content |
|---|---:|---:|---|
| A | `4` | `2` | data bond, pointer, close candidate |
| B | `7` | `3` | data bond, two probe stores, two references, candidate |
| C | `10` | `3` | four rails, three flags, two syndromes, candidate |

Every declared interaction, preparation, syndrome, and candidate edge has
Manhattan length one. The runner enumerates all determinant-`+1` signed
permutation matrices, obtains exactly 24 frames, applies each frame plus the
held translation `(11,-7,13)`, and rechecks collisions and every edge. All
residuals are zero.

This is covariance of the supplied finite placements and role relabeling. It
does not select a global scheduler or derive the physical update. Fresh
ancilla states, reset, component gates, routing, and enforcement are locally
prepared or locally applied in the declared circuit model, but their lawful
availability under the unique framework admissibility rule remains supplied.

## 7. Supplied-structure inventory

| supplied item | used for | not derived here |
|---|---|---|
| `Z^3`, NN adjacency, translations, 24 proper-cubic frames | bounded placement | three-dimensionality |
| one ordinary `M_2(C)` per site | all carriers | privileged basis or state |
| occupation basis and actual Cycle-230 `F` | data fixture | global CAR compiler |
| fresh `|0>` sites and Bell/repetition preparation | pointers, Choi probe, rails | autonomous reset/preparation law |
| `H_F=pi P_-` and projector coupling | Route A | physical-current identification |
| bounded routing and two bond invocations | Route B | inseparable invocation identity |
| FSWAP, CZ, CNOT, Hadamard, register swaps | circuit components | selection from admissibility |
| equality stabilizers and component flags | Route C checks | occurrence implication |
| projector comparison and thresholds | diagnostic weights | Born rule or selected readout |
| circuit ordering | evaluation convention | physical time or rate |
| named close candidates | event-to-close probes | actualization, permanence, Record formation |

The three open seams should not be multiplied into aliases:

- `K_link`: make surviving local evidence faithful to the exact named data
  invocation under split faults;
- `K_prep`: derive lawful local preparation, reset, routing, and constraint
  enforcement from the selected substrate update; and
- `K_form`: turn a successful coherent close into actualized permanent Record
  content.

`K_law` is an umbrella for selecting the physical update that may close
`K_link` and `K_prep`; it is not counted as a fourth independent wall here.

## 8. Exact tests, controls, and residuals

The companion runner has 21 assertions:

- source and note firewalls: `2`;
- FSWAP and local fixture: `2`;
- Route A generator, nondemolition, demolition, and invariant controls: `4`;
- Route B local preparation, ideal comb, split invocations, routing deletions,
  and underrotation interpolation: `5`;
- Route C preparation/enforcement, exact gadget, rail faults, code-preserving
  faults, and split flags: `5`;
- placement and 24-frame covariance: `2`; and
- scoped tournament disposition: `1`.

Lawful-domain coverage is analytic where an operator intertwiner or channel
factorization is asserted. Random density matrices test seeds `262,263,264`
and held seed `999`; `pi/7`, two routing deletions, three combined component
faults, one nontrivial translation, and all proper-cubic frames are held
controls. No sampled agreement is promoted to an all-state theorem.

Leakage is zero for every ideal construction. Route C reports exact nonzero
leakage for rail omissions and exact zero leakage for logical, code-preserving
faults, preventing “no leakage” from being confused with “correct gate.”

## 9. TOE dependency ledger after Cycle 262

| wall | Cycle-262 state | exact remaining dependency |
|---|---|---|
| `C_ref` | explicit local pointer, Choi, and code references; unchanged/open | derive lawful fresh reference preparation without a privileged hidden frame |
| `C_num` | unchanged: the two-mode occupation/parity fixture and repetition rails are supplied finite codes | a same-encoding full-Fock number/parity realization and its lawful preparation remain open |
| `C_wrap` | unchanged: no wrapped phase, winding, or history coordinate is constructed | derive any physical unwrapping/history relation separately; circuit schedules are not such a relation |
| `C_int` | strongest gain: exact zero-leakage encoded FSWAP gadget plus same-bond probes; still open | select the physical component update and close `K_link` under split faults |
| `C_local` | all three placements bounded, NN, and 24-frame covariant; still open globally | compile the full Cycle-230 CAR cell and local prep/enforcement under one substrate law |
| `C_source` | no source or gravity rule introduced; unchanged/open | derive resource/source coupling and observable identification |

Maturity scores remain:

| lane | score | reason |
|---|---:|---|
| operational quantum / records | `2/5` | exact coherent gates and closes, but no occurrence-faithful actualized Record |
| time | `1/5` | circuit order only; no physical time metric or rate |
| inertia / matter | `3/5` | one-particle FSWAP fixture preserved; global matter compiler remains open |
| gravity / source | `2/5` | resource ledger context exists elsewhere; no new source law here |
| Born / probability | `1/5` | projector weights are diagnostics, not probabilities |

## 10. No-go discipline: full N1–N8 audit

No impossibility, minimum-content, or axiom-pressure statement is allowed to
leave this note without the following audit. The result survives only as a
bounded disposition of the tested routes.

### N1 — alternative-route enumeration

The following materially different routes were actually constructed and
tested, not merely named:

| marker | route | outcome |
|---|---|---|
| `ATTEMPTED-A1` | same-bond input-independent pointer | exact nondemolition; split-fault false positive |
| `ATTEMPTED-A2` | same-bond FSWAP-eigenspace-sensitive pointer | sensitive; arbitrary-data demolition |
| `ATTEMPTED-A3` | final-data-only invariant-state check | exact identity/FSWAP indistinguishability on two lawful inputs |
| `ATTEMPTED-B1` | same-physical-bond two-query Choi comb | exact ideal; data-invocation deletion false positive |
| `ATTEMPTED-B2` | Choi underrotation and routing controls | exact interpolation; routing faults visible |
| `ATTEMPTED-C1` | two-rail repetition-code FSWAP gadget | exact logical FSWAP and zero leakage |
| `ATTEMPTED-C2` | equality syndromes plus component flags | detects some faults; code-preserving logical faults and split flags survive |

These attempts span constant, input-sensitive, process-probe, and encoded
syndrome mechanisms. They do not exhaust intrinsic Hamiltonian monitors,
environment-history witnesses, quantum-switch/process-matrix protocols,
teleportation-verified gates, autonomous local actualization, or stronger
fault-tolerant codes.

### N2 — condition-independence audit

The residual conditions are `K_link`, `K_prep`, and `K_form`.

- `K_link` does not imply `K_prep`: a stipulated inseparable occurrence flag
  says nothing about how fresh sites or routing are lawfully produced.
- `K_link` does not imply `K_form`: a faithful coherent witness need not
  actualize or persist as a Record.
- `K_prep` does not imply `K_link`: perfect Bell/code preparation leaves the
  Route-B and Route-C split faults intact.
- `K_prep` does not imply `K_form`: reversible preparation is not permanent
  locking.
- `K_form` does not imply `K_link`: actualizing an independently generated
  false-positive flag preserves the wrong fact.
- `K_form` does not imply `K_prep`: the Record axiom says Records form but does
  not supply these carrier preparations.

They are pairwise nonredundant at this resolution. The tested failures share
the factorability of their supplied evidence links; that is a property of the
constructions, not proof of a substrate-wide wall.

### N3 — hidden-condition scan

- **Dimensionality:** `Z^3` and cubic frames are supplied, not derived.
- **Boundary/size:** every artifact is finite; no thermodynamic limit is used.
- **Translation/rotation:** covariance is checked for all 24 frames and a
  nonzero translation; role labels and scheduling remain supplied.
- **Reversibility:** all tested carriers are coherent finite maps; irreversible
  environment/history monitors are not excluded.
- **Environment:** no uncontrolled environment is modeled, so no conclusion
  covers environment-mediated occurrence evidence.
- **Archive/actualization:** no coherent carrier is promoted to Record.
- **Stochasticity:** none is used; projector weights are not probabilities.
- **Lawful domain:** all-state claims follow from operator identities; held
  samples remain only regressions.
- **Fault model:** data-factor, invocation, routing, component, flag, leakage,
  and combined held faults are explicit; adversarial faults outside those
  finite families remain open.
- **Primitive/type imports:** basis, gates, preparation, routing, projectors,
  and schedules are inventoried rather than hidden in “local.”

No hidden global Jordan–Wigner ordering, parity service, or host-side
controller is introduced by these finite local occurrence probes. This note
does not claim that the still-open global CAR compiler has thereby been
closed.

### N4 — residual matching

The residuals match existing sources without inflating them:

- the minimal Lattice/Qubit/Admissibility/Record axioms supply sites, local
  algebra, static constraint, and permanent Records, while explicitly leaving
  update, probability, formation, and time open;
- the pointer theorem shows that a supplied controlled copy can carry
  information but does not select the pointer, preparation, or formation law;
- Cycle 243 already separates event, close, commit, and Record maps;
- Cycle 259 already exhibits the split data-factor false positive; and
- Cycle 262 adds same-bond and encoded constructive tests but does not close
  that seam.

Standard local-fermion encodings and fault-tolerant verification are prior-art
directions, not evidence for a no-go and not a retained solution to this
invocation-occurrence question.

### N5 — rhetoric and resolution audit

Allowed resolution:

```text
These three bounded constructions do not certify the named data invocation
when their auxiliary evidence link is independently factorable.
```

Forbidden overclaim:

```text
No local nondemolition occurrence certificate can exist.
```

The note uses “false positive” only relative to a declared fault row and close
criterion. “Exact” refers to finite operator equalities. “Current” refers to
a tested generator-eigenspace candidate, not a derived physical observable.
“Verified” refers to code intertwining and the stated syndrome family, not
universal fault tolerance.

### N6 — partial-closure and primitive scan

Partial closures are substantive:

- Route B removes abstract gate-family mismatch by reusing the same physical
  bond and locally preparing the Choi probe.
- Route C supplies the exact encoded FSWAP intertwiner, local equality
  constraints, zero leakage, all six schedules, and an explicit bounded fault
  table.
- Every route has constant site overhead and full proper-cubic placement
  covariance.

The approved primitive surface was reread. Scale reference, kinetic isotropy,
and realized-state evaluation do not supply an occurrence link, carrier
preparation, physical update, actualization rule, time metric, or Born law.
No primitive is silently stretched to close `K_link`, `K_prep`, or `K_form`.

Live partial-closure paths are: couple the witness to an unavoidable
environment/history channel of the same interaction; test a causally ordered
or quantum-switch process witness whose invocation identity cannot be split;
construct a teleportation-verified primitive with explicit local resource
faults; search stronger codes that detect logical component omission; and
derive a local actualization map separately from coherent verification.

### N7 — steelman

The strongest hostile reviewer should reject any broad no-go here. Route A
tests only two simple Stinespring choices. Route B uses sequential calls, so a
more intrinsic comb may bind invocation identity differently. Route C uses a
distance-two equality code whose stabilizers were designed for rail mismatch,
not arbitrary logical-gate omission. All carriers remain reversible and
after-the-fact. A live interaction current exported continuously to an
environment, a verified gate primitive with inseparable syndrome production,
or an actualizing local history rule could evade every listed fault.

That steelman succeeds. Therefore the retained conclusion is constructive and
bounded: Cycle 262 identifies exactly where these three links factor, while
leaving route-independent obstruction and constitutional need unestablished.

### N8 — cross-cycle echo

The same rhetorical hazard has appeared before: fixed transcripts can survive
event deletion; common-control flags can certify a command rather than the
data action; Choi probes can certify a replica rather than the named call; and
code membership can survive a wrong logical operation. Cycle 262 does not
rename those echoes as independent impossibility evidence. It sharpens them
with a same-bond comb and an exact encoded gadget.

Conversely, prior local-fermion, pointer, process, and QEC constructions warn
against constitutional escalation from one architecture. No prior cycle
supplies a route-independent theorem matching all three remaining conditions.
The cross-cycle verdict is therefore unchanged: no shared obstruction, no
minimum-content claim, and no axiom pressure.

## 11. Disposition and next experiment

Route-by-route:

- **Route A:** retained as an exact sensitivity-versus-nondemolition tradeoff
  fixture, not an occurrence certificate.
- **Route B:** retained as the strongest same-physical-bond Choi construction;
  invocation-specific deletion remains decisive.
- **Route C:** retained as the strongest constructive result of this
  occurrence-link tournament—an exact bounded zero-leakage encoded FSWAP
  gadget—and as a precise demonstration that local code acceptance is weaker
  than logical-operation occurrence. It is a two-mode fixture, not the
  campaign's missing full Cycle-230 CAR compiler.

No shared obstruction survives as constitutional evidence. The optimal next
campaign is a genuinely intrinsic occurrence link: couple the FSWAP bond to a
local environment/history degree of freedom through one nonfactorable
physical update, demand exact arbitrary-data nondemolition, and rerun the
same split-fault, deletion, leakage, held-size, preparation, and 24-frame
controls. If that construction succeeds coherently, actualization and Record
formation must still be tested as a separate `K_form` campaign.
