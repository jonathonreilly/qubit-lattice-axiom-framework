# Physical transition occurrence/close tournament — Cycle 332

Date: 2026-07-18

Branch: `codex/bare-metal-mvp-probes-20260713`

Authority: none

Audit: unset

Constitutional effect: none

Companion runner:

```text
scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit-status surface. It drafts no axiom language. It starts
from the actual Cycle-314 event transition and the derived Cycle-329 matcher
and readiness controls. It stops at a conditional transition witness, close
certificate, and commit candidate.

## Result up front

All three bounded routes are positive:

1. a transition-sensitive reversible occurrence witness;
2. a relational two-boundary close certificate;
3. a protected-history predecessor route.

Route 1 compiles the exact Cycle-314 event-flipping stream permutation into a
fixed reversible permutation on two boundary registers and one witness. On
the constrained code at trained `L=3` and held `L=6`, all 508 nonvacuum rows
produce witness one, both vacuum rows produce zero, and every wrong active
pre/post pairing produces zero. An `h` flip with the wrong physical base row,
a spliced post-boundary, and deletion of the transition table also produce
zero. The full permutation and its square are exact.

Route 2 requires five separately formed predicates:

```text
pre-boundary lawful,
transition witness,
post-boundary lawful,
Cycle-329 identity match,
Cycle-329 predecessor readiness.
```

A fresh local causal certificate reaches close only when all five pass.
Readiness alone cannot close. Twenty topological schedules give one relational
outcome; deleting any dependency or certificate stage suppresses close.

Route 3 takes three earlier Cycle-326 candidate bits, reversibly fans each into
a three-bit protected block, checks the expected predecessor identity in its
Cycle-329 slot, and derives the three individual predecessor-closed flags.
Deleting any one replica or either fanout per predecessor suppresses readiness.
The inverse restores one candidate plus two blanks, so the route explicitly
does not establish permanence.

Every positive route is conditional on physical inputs. Two boundary
registers remain supplied. Their preparation and selection as the history
being tested remain supplied. An occurrence witness is not a selected actual
member. A commit candidate is not a Record. Forward nonreturn is not
permanence.

False event controls are explicit, and all 24 proper-cubic frames are tested
at each declared size.

The broad candidate negative that no bounded transition-sensitive route can
replace the Cycle-326 occurrence/close controls is contradicted. Broad gate
status: FAIL / DO NOT SHIP. There is no shared obstruction and no axiom
pressure.

## 1. Exact Cycle-314 transition fixture

Cycle 314's physical stream is a permutation on 1,020 ambient rows. Its
rank-127 constrained event code has 510 active physical rows: two vacuum and
508 nonvacuum. For a physical row `a`, let `S(a)` be the exact stored
`stream_mapping`. The transition program toggles one fresh witness iff

```text
a is nonvacuum and b = S(a).
```

The truth table is compiled into a permutation on `(a,b,w)`:

```text
(a,b,w) -> (a,b,w XOR T(a,b)).
```

No boundary is erased. Applying the same permutation twice restores the
input. This is a reversible discriminator, not a dissipative occurrence law.

| exact transition control | `L=3` | held `L=6` |
|---|---:|---:|
| ambient rows | `1020` | `1020` |
| active constrained-code rows | `510` | `510` |
| lawful nonvacuum transitions | `508` | `508` |
| vacuum boundaries | `2` | `2` |
| code-preservation failures | `0` | `0` |
| lawful false negatives | `0` | `0` |
| active-pair false positives | `0` | `0` |
| `h`-only false-event survivors | `0` | `0` |
| spliced-post survivors | `0` | `0` |
| deleted-transition survivors | `0` | `0` |
| permutation failures | `0` | `0` |
| involution failures | `0` | `0` |

The two boundary registers are the actual Cycle-314 ambient code registers,
not ten-bit classical substitutes for them. Using Cycle 326's conservative
45-M2 event patch per boundary, route 1 has a 91-M2 two-boundary-plus-witness
support. Boundary storage is explicit fresh capacity.

The retained occurrence statement is conditional:

```text
given a supplied pair of boundary registers on the declared transition graph,
the witness distinguishes nonvacuum Cycle-314 stream transition from no such
transition or a spliced pair.
```

It does not derive which boundary pair nature realizes, a global member
selection rule, or irreversible actuality.

## 2. Route 1 disposition — transition witness

The fixed permutation tests the entire active two-boundary pair space rather
than only one representative particle-number sector. It is sensitive to the
full physical stream row relation, not only `h_pre XOR h_post`. A forced `h`
flip on the wrong base row fails. Because `stream_mapping` is a permutation,
the post-boundary belonging to another active pre-boundary also fails.

The Cycle-329 compact physical matcher supplies `(match,ready)=(1,1)` for the
actual target identity and three predecessors. The transition witness can
occupy Cycle 326's occurrence-control input. Close law remains separately
supplied in this route. A deleted transition gives occurrence zero and leaves
the fresh candidate cell blank.

Strongest exact result: a bounded, reversible, deletion-faithful discriminator
for the actual event substep. Residual: two-boundary preparation and selected
history membership remain imports.

## 3. Route 2 — relational two-boundary close certificate

Route 2 uses the five-bit fresh-stage certificate

```text
q_(i+1) ^= q_i AND predicate_i,
```

with predicates ordered as pre boundary, transition, post boundary, identity
match, and predecessor readiness. Every stage is a reversible Toffoli update
on the full space. The forward code supplies fresh stage bits.

| close-certificate control | result |
|---|---:|
| lawful certificate, `L=3,6` | `1` |
| Cycle-326 receiver | `(fresh,candidate)=(0,1)` |
| readiness alone | `0` |
| `h`-only wrong boundary | `0` |
| spliced post-boundary | `0` |
| Cycle-329 target anti-splice | `0` |
| any of five stage deletions | `0` |
| relational topological orders | `20` |
| distinct terminal sets | `1` |
| any DAG-edge deletion close survivors | `0` |

The DAG is

```text
pre -> transition -> post -> close
identity-match ----------------> close
predecessor-ready -------------> close.
```

The maximum dependency rank and certificate depth are update depths, not
time. The conservative source, Cycle-329 syndrome matcher, certificate, and
receiver support is 720 M2. That number includes two 45-M2 boundary patches,
the 621-M2 Cycle-329 compact comparator apparatus, one transition witness, six
certificate-stage M2, and fresh/candidate receiver cells.

The close certificate derives the declared conditional close predicate. It
does not type its output as Record or establish permanent history.

## 4. Route 3 — protected-history predecessor route

For each of the three Cycle-329 predecessor slots, an earlier lawful
Cycle-326 candidate bit controls two CNOTs into fresh blanks:

```text
(c,0,0) -> (c,c,c).
```

On computational candidate labels this is a reversible fanout. On coherent
inputs it is an entangling isometry, not cloning of an arbitrary state.
Calling it pointer copying would still not make it a Record.

An exact three-bit equality circuit derives `closed_i=1` only for `(1,1,1)`.
Cycle 329 then checks that each closed flag is attached to the expected
physical predecessor identity before forming aggregate readiness.

| protected-history control | result |
|---|---:|
| three protected blocks | `(111,111,111)` |
| protected closed flags | `(1,1,1)` |
| Cycle-329 `(match,ready)` | `(1,1)` |
| current transition witness | `1` |
| Cycle-326 receiver | `(0,1)` |
| nine single-replica deletions | readiness `0` |
| six fanout-gate deletions | readiness `0` |
| wrong predecessor identity | readiness `0` |
| false current boundary | candidate `0` |
| exact inverse | `(100,100,100)` |

The six blank replicas are supplied capacity. Nine M2 store the three
protected blocks. The conservative two-boundary, exact Cycle-329 direct
matcher, protected-history, witness, certificate, and receiver support is
1,198 M2.

The inverse erases the replicas and returns the candidate plus blanks. This
explicit reversibility is why the route is protected against the enumerated
single deletions but is not permanent history. It also does not derive the
earlier candidates' occurrence laws; those are prior conditional outputs.

## 5. Proper-cubic and held-size controls

The exact Cycle-314 event-frame mapping commutes with the stream permutation,
keeps `h` scalar, and preserves the transition truth relation. Cycle 329's
label/support matcher is rebuilt on every rotated actual block support.

Across trained `L=3` and held `L=6`:

| covariance/domain control | result |
|---|---:|
| proper-cubic frames per size | `24` |
| total frame-size cases | `48` |
| stream/frame commutator failures | `0` |
| `h` scalar failures | `0` |
| physical support covariance failures | `0` |
| Cycle-329 match/readiness failures | `0` |
| malformed-domain rejections | `8/8` |

No preferred frame is selected. The witness and close-certificate roles are
cubic scalars. The apparatus remains bounded over the declared held size.

## 6. False-event, anti-splice, and deletion ledger

The tournament distinguishes four false authorizations:

- readiness with no supplied pre/post event pair;
- an `h` flip without the exact physical base-row transition;
- a post-boundary belonging to another pre-boundary;
- correct boundaries attached to a corrupted Cycle-329 target or predecessor
  identity.

All four suppress close or candidate. Deleting the transition program, any
relational certificate stage, any DAG edge, any protected replica, or either
fanout per predecessor also suppresses the relevant output.

These are bounded fault classes. No theorem about arbitrary high-weight
corruption, indefinite storage, or thermodynamic irreversibility is inferred.

## 7. Reversibility and capacity inventory

| structure | status after Cycle 332 |
|---|---|
| Cycle-314 stream transition relation | derived previously and compiled exactly |
| Cycle-329 identity match/readiness | derived previously and rechecked |
| conditional transition witness | derived by route 1 |
| conditional two-boundary close certificate | derived by route 2 |
| predecessor-closed flags from protected candidate blocks | derived by route 3 |
| two physical boundary registers | supplied capacity and preparation |
| selection of the tested boundary pair as actual history | absent |
| fixed transition/comparator program | supplied coefficients/placement |
| fresh witness/certificate/history cells | supplied finite capacity |
| earlier candidate occurrence | prior conditional input, not rederived |
| Record typing | absent |
| permanence | absent; exact inverses exhibited |
| clock matcher, interval, rate, calibration | absent |

An occurrence witness is not a selected actual member. A conditional close is
not irreversible actualization. A commit candidate is not a Record. Forward
nonreturn is not permanence. Circuit depth is not time.

## 8. Route-by-route disposition

| route | disposition | retained result | residual boundary |
|---|---|---|---|
| reversible transition witness | **positive, strongest exact discriminator** | entire active pair space, exact inverse, false-event and splice rejection | boundary pair and its selection supplied |
| relational two-boundary close | **positive** | readiness alone cannot close; 20 schedules, all edge/stage deletions | fresh certificate and fixed close grammar supplied |
| protected prior candidates | **positive, bounded fault protection** | identity-bound closed flags; replica/fanout deletion detection | reversible, finite, earlier occurrence supplied; no permanence |

There is no retained route-negative result. No impossibility or
minimum-content statement is submitted to N1-N8. The broad negative fails and
no route-specific limitation is promoted to constitutional evidence.

## 9. TOE dependency ledger and maturity

| wall | Cycle-332 movement | still open |
|---|---|---|
| `C_ref` | two boundary identities are physically compared and anti-spliced | boundary preparation, pair selection, and program placement remain supplied |
| `C_num` | unchanged | no coefficient selection or numerical grade is added |
| `C_wrap` | advances from event readiness to an exact conditional transition witness and close certificate; protected predecessor inputs are explicit | selection of actual history member, permanence, typed Record, recurrence, clock matcher, interval, and rate remain open |
| `C_int` | the actual Cycle-314 stream substep is transition-sensitive | no autonomous occurrence selection or interaction-to-actuality law |
| `C_local` | three bounded routes pass held size, frames, deletion, and false-event controls | economical primitive layout, capacity renewal, overlap, and indefinite history remain open |
| `C_source` | unchanged | no energy, stress, resource, lapse, or gravity response is inferred |

Using the packaged Cycle-331 baseline, conservative planning scores become:

| lane | integrated | strict floor | conditional | maturity | Cycle-332 disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 66% | 32% | 93% | 3.7/5 | exact transition and close predicates; candidate still not Record |
| causal time / clock | 37% | 19% | 68% | 2.1/5 | conditional occurrence/close witness; no selected member, permanence, or clock |
| inertia / matter | 76% | 37% | 97% | 4.3/5 | unchanged |
| gravity / source / resource | 42% | 17% | 70% | 2.3/5 | unchanged |
| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 | unchanged; no selected actual member or probability law |

These are planning scores, not truth probabilities or audit verdicts.

## 10. Novelty and optimal next campaign

The retained repository result is the exact integration of Cycle 314's
physical stream transition, Cycle 329's physical anti-splice controls, and
Cycle 326's candidate receiver through three bounded constructions.
Reversible truth-table permutations, causal certificates, repetition blocks,
CNOT fanout, and DAG schedule quotients are prior-art mechanisms. No global
novelty priority is claimed for them.

Thirring machinery is not used or compared.

The next campaign should not enlarge the comparator. The decisive remaining
wall is selection: determine whether the substrate supplies a physical rule
that selects one lawful two-boundary pair as an actual history member while
remaining compatible with reversibility, frames, deletion, and Born
probability. Independently test a relational member-selection rule, an
environment/export route, and a protected recurrent route. Do not call a
selected pointer value a Record without typing and permanence. If a negative
is contemplated, apply full no-go discipline N1-N8 first.

## Verification

Run from the repository root:

```text
python3 scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py
```
