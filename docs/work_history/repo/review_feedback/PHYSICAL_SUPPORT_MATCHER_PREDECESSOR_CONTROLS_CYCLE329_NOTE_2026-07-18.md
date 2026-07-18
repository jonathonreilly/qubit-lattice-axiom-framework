# Physical support matcher and predecessor controls — Cycle 329

Date: 2026-07-18

Branch: `codex/bare-metal-mvp-probes-20260713`

Authority: none

Audit: unset

Constitutional effect: none

Companion runner:

```text
scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit-status surface. It drafts no axiom language. It attacks
the clean anti-splicing seam left by Cycle 326: replace its supplied aggregate
`identity_match` and `dependencies_ready` controls with outputs of fixed
bounded physical circuits.

## Result up front

All three routes are positive:

1. a direct bounded comparator;
2. a relational hash/syndrome comparator;
3. local causal-certificate propagation.

They consume the actual Cycle-314/Cycle-312 stable block labels and bounded
physical-support incidence flags. Predecessor readiness additionally consumes
three individual physical predecessor-closed flags. They derive one
`identity_match` bit and one `dependencies_ready` bit by fixed reversible
X/CNOT/Toffoli updates. There is no host conjunction.

The exact direct route has zero anti-splicing false positives, zero
anti-splicing false negatives, and zero false positives under every tested
one-bit support corruption at trained `L=3` and held `L=6`. The more compact
nine-bit syndrome has the same result on the five actual fixture identities,
all actual mixed label/support splices, all single support-bit faults, and all
one-delete/one-insert support substitutions. The propagated route sends a
fresh certificate through all 135 identity bits; deletion of any stage kills
the certificate.

Every route then drives Cycle 326's physical local receiver:

```text
(match, ready, occurrence, close-law) = (1,1,1,1)
  -> (fresh,candidate) = (0,1).
```

Setting occurrence or close-law to zero still produces no candidate even when
the derived match and readiness bits equal one. Occurrence remains separate.
Close law remains separate. Fresh capacity remains separate. Typing remains
separate. Permanence remains separate. Matcher-to-clock remains separate.
Calibration remains separate.

A derived match is not occurrence. A ready predecessor set is not an actual
event. A commit candidate is not a Record. None of these comparator gates
derives permanence, elapsed time, rate, or realized-history membership.

The broad candidate negative that no bounded support-derived matcher can feed
the Cycle-326 receiver is contradicted by all three constructions. Broad gate
status: FAIL / DO NOT SHIP. There is no shared obstruction and no axiom
pressure.

## 1. Common physical fixture

The selected five actual blocks are the same Cycle-314 dependency fixture,
expressed geometrically so it can also be rebuilt at held size:

```text
0: coin at (0,0,0)
1: coin at (0,0,1)
2: coin at (1,1,1)
3: distractor edge through (0,0,0), direction 0
4: target edge through (0,0,1), direction 2
```

The two edge partners use the opposite endpoint across the periodic seam.
Their catalog local indices remain `0` and `8` at `L=3` and `L=6`. The exact
physical block supports are extracted with Cycle 312's
`block_mode_support`, not replaced by a synthetic overlap graph.

| fixture diagnostic | trained `L=3` | held `L=6` |
|---|---:|---:|
| union support-incidence flags | `89` | `102` |
| target support size | `16` | `20` |
| stable-label bits | `33` | `33` |
| padded identity word | `135` | `135` |
| swap-equivalent executions | `3` | `3` |
| distinct dependency signatures | `1` | `1` |
| target host positions | `3,4` | `3,4` |
| target predecessors | `0,1,2` | `0,1,2` |
| Cycle-314 event truth residual | `1.6541950504657498e-15` | same |

The label word contains one kind bit, ten local-index bits, and two eleven-bit
payload fields. The support word is a 102-bit bounded local-union incidence
vector. Small-size aliases are not hidden: the target support has 16 modes at
`L=3` and 20 at `L=6`, while the compiled word width remains fixed.

The reachability relation is rebuilt from the actual support intersections.
All three lawful executions give the same target label, support, and three
predecessors although the target's schedule position changes. This is the
schedule quotient. The comparator consumes this stable physical identity; it
does not compare update indices.

## 2. Route 1 — direct bounded comparator

For an observed identity word `x` and fixed expected word `e`, the route
temporarily flips every data bit for which `e_i=0`. It then computes an AND
chain using only Toffoli gates, copies the final equality bit, reverses the
chain, and restores the data bits. Symbolically,

```text
M(x,e) = AND_i [x_i = e_i].
```

This equation describes the gate output; the runner does not evaluate it with
a host `all` and pass the result to Cycle 326. The conjunction is the output of
the fixed reversible gate list.

Four comparator instances check the target and the three expected predecessor
identities. A fifth six-input comparator consumes

```text
(pred0_match, pred0_closed,
 pred1_match, pred1_closed,
 pred2_match, pred2_closed)
```

and produces readiness. Thus a closed flag from the wrong support cannot fill
a predecessor slot. The expected words and circuit placement are compiled
program structure; the final matcher/readiness bits are not supplied.

Exact route-1 ledger:

| diagnostic | result |
|---|---:|
| lawful false negatives, both sizes | `0` |
| other-fixture target false positives | `0` |
| all mixed actual label/support splice false positives | `0` |
| all single support-bit corruption false positives | `0` |
| wrong predecessor-slot identity survivors | `0` |
| single predecessor support-bit corruption survivors | `0` |
| six single-missing-predecessor cases | readiness `0` |
| matcher-copy deletion | `(match,ready)=(0,1)` |
| readiness-copy deletion | `(1,0)` |
| maximum primitive gate support | `3 M2` |
| comparator receiver overhead | `1089 M2` |
| with separate Cycle-326 controls | `1093 M2` |
| conservative source-plus-receiver patch | `1138 M2` |

The large overhead is honest. It includes four 135-bit observed identity
words and clean reversible comparison workspace. It is bounded and constant
over the declared sizes but is not yet a primitive nearest-neighbor layout or
an economical compiler.

## 3. Route 2 — relational hash/syndrome comparator

For a 135-bit identity word, the compact route computes the nine-bit Hamming
syndrome

```text
s(x) = (sum_i x_i mod 2,
        XOR of the nonzero binary addresses i+1 for which x_i=1).
```

The syndrome is produced by a fixed CNOT network. The same reversible equality
circuit compares it with the expected syndrome. The five actual fixture
identities have five distinct syndromes at each size.

Exact tested scope:

| syndrome diagnostic | result |
|---|---:|
| syndrome width | `9` |
| actual identities distinguished | `5/5` at each size |
| actual mixed label/support splice false positives | `0` |
| lawful false negatives | `0` |
| single support-bit fault false positives | `0` |
| one-delete/one-insert support fault false positives | `0` |
| wrong predecessor-slot identity survivors | `0` |
| single predecessor support-bit fault survivors | `0` |
| missing predecessor cases | readiness `0`, `3/3` |
| matcher/readiness copy deletions | corresponding output `0` |
| maximum primitive gate support | `2 M2` for hash, `3 M2` for equality |
| comparator receiver overhead | `621 M2` |
| with separate Cycle-326 controls | `625 M2` |
| conservative source-plus-receiver patch | `670 M2` |

This is the strongest resource result, not the strongest universal identity
theorem. A nine-bit linear syndrome cannot be collision-free on every one of
the `2^135` possible words. The retained claim is exactly the enumerated
actual fixture, splice, one-bit, and delete/insert fault classes. Route 1 is
the exact comparator when arbitrary multi-bit corruption must be excluded.

## 4. Route 3 — local causal-certificate propagation

The third route lays a fresh certificate stage beside every identity bit. With
`q_0=1`, the fixed local rule is

```text
q_(i+1) ^= q_i AND [x_i=e_i].
```

The equality polarity is implemented by a temporary X on the data bit when
the expected bit is zero. Every update is a reversible three-M2 gate on the
full state space. On the declared fresh-stage forward code, the terminal
certificate exists only if the previous certificate and current identity bit
both pass.

Four such paths validate target plus predecessor identities. A six-stage
certificate then alternates the three validated identity outputs with their
three individual predecessor-closed flags and feeds the Cycle-326 receiver.

Exact controls:

| diagnostic | result |
|---|---:|
| lawful false negatives | `0` |
| other-fixture target false positives | `0` |
| single target support-bit fault survivors | `0` |
| wrong predecessor-slot identity survivors | `0` |
| target certificate stages checked | `135` per size |
| survivors after deleting any tested stage | `0` |
| missing predecessor cases | readiness `0`, `3/3` |
| target/readiness path deletion | corresponding output `0` |
| maximum primitive gate support | `3 M2` |
| comparator receiver overhead | `1094 M2` |
| with separate Cycle-326 controls | `1098 M2` |
| conservative source-plus-receiver patch | `1143 M2` |

This route makes the dependency order inside the matcher explicit. Its stage
depth is circuit depth, not physical time. Fresh certificate stages are
supplied capacity, not permanent Records.

## 5. Anti-splicing and fault disposition

The actual target identity is a conjunction of its stable label and full
bounded support-incidence word. Route 1 rejects all other complete fixture
identities, all 24 mixed target splices obtained by combining any actual label
component with any actual support component except the lawful target pair,
and all 102 single support-flag flips at each size. Route 2 rejects the same 24
actual splices, all single support faults, and every target support
delete/insert substitution. Route 3 rejects every other complete fixture
identity and every deleted certificate stage.

False-negative controls rerun every lawful route at both sizes and under every
frame. Missing each of the three predecessor-closed flags separately leaves
identity match equal to one but readiness equal to zero. Swapping a predecessor
identity into a different slot fails that slot's fixed comparator.

The individual predecessor-closed flags remain physical inputs. Cycle 329
derives the aggregate readiness control from their identity-checked slots; it
does not derive earlier close occurrence or permanence.

## 6. Schedule quotient, held size, and proper-cubic covariance

At both `L=3` and held `L=6`, the independent distractor and target exchange
schedule positions 3 and 4. All three executions have one reachability
signature and every route gives one `(match,ready)=(1,1)` output.

For each of all 24 proper-cubic frames at both sizes, the runner rotates every
actual block label and every actual physical support mode, then independently
rebuilds the corresponding Cycle-312 block. There are 48 frame-size cases:

| covariance control | result |
|---|---:|
| frame-size cases | `48` |
| physical support-map mismatches | `0` |
| direct comparator failures | `0` |
| syndrome comparator failures | `0` |
| certificate comparator failures | `0` |

The comparator program rotates with its label/support fixture; no frame is
selected as a preferred physical orientation. Equality and predecessor
readiness are scalar output roles.

## 7. Cycle-326 integration and semantic firewall

For each route, derived `(match,ready)=(1,1)` is inserted into the existing
seven-M2 Cycle-326 local close permutation. With event-ready `h=1`, supplied
occurrence `1`, supplied close-law `1`, fresh `1`, and candidate `0`, the
receiver produces `(fresh,candidate)=(0,1)`.

Two deletion controls preserve the semantic split:

| inputs changed after matcher succeeds | receiver output |
|---|---|
| occurrence `1 -> 0` | `(fresh,candidate)=(1,0)` |
| close-law `1 -> 0` | `(fresh,candidate)=(1,0)` |

Therefore:

- derived match is not occurrence;
- predecessor readiness is not present-event occurrence;
- a close enable is not derived by the matcher;
- fresh capacity is not created by equality;
- a commit candidate is not a Record;
- reversible certificate or comparator state is not permanence;
- gate depth is not elapsed time;
- matcher-to-clock identification and calibration remain absent.

## 8. Supplied-structure inventory

| structure | Cycle-329 status |
|---|---|
| Cycle-314 physical event-ready `h` | previously derived; reverified at `L=3,6` |
| stable labels and bounded supports | extracted from actual Cycle-312 physical blocks |
| dependency predecessor set | derived from the common-support schedule quotient |
| individual predecessor-closed flags | supplied physical inputs from earlier candidate closes |
| fixed comparator coefficients/program | supplied compiled program structure |
| comparator placement/routing | supplied bounded layout; primitive NN synthesis absent |
| aggregate identity matcher | derived by all three routes |
| aggregate predecessor readiness | derived by all three routes |
| occurrence | separate supplied input |
| close law | separate supplied input |
| fresh capacity | separate supplied input |
| Record typing | absent |
| permanence | absent |
| matcher-to-clock law | absent |
| interval/rate calibration | absent |

The result removes two aggregate host Booleans from Cycle 326. It does not
remove every supplied preparation or program coefficient.

## 9. Exact executable ledger

The cold runner requires eight checks:

1. note authority, audit, route, and semantic contract;
2. exact event source plus trained/held common-support fixture;
3. direct comparator route;
4. relational syndrome route;
5. causal-certificate route;
6. schedule, frame, held-size, and Cycle-326 integration controls;
7. lawful-domain and supplied/derived inventory;
8. positive three-route synthesis without occurrence or Record promotion.

Nine of nine malformed-domain calls are rejected: unsupported sizes, empty or
mismatched comparator words, non-binary input, empty syndrome input,
mismatched certificate words, an undeclared route, and a malformed
predecessor-flag tuple.

Pass counts are executable contracts, not independent empirical predictions.

## 10. Route-by-route disposition

| route | disposition | strongest retained result | residual boundary |
|---|---|---|---|
| direct comparator | **positive, exact on 135-bit words** | exact equality and slot-checked readiness, arbitrary single-bit support corruption rejected | large bounded overhead; word preparation and layout supplied |
| relational syndrome | **positive, resource winner** | 9-bit signature, actual splice and weight-one/two support classes rejected | untested multi-bit syndrome collisions remain possible |
| causal certificate | **positive, deletion-transparent** | every bit/stage causally exposed; all stage deletions suppress match | large fresh-stage capacity and routing supplied |

There is no retained route-negative result. The broad negative is directly
falsified, so no impossibility or minimum-content claim is submitted to N1-N8.
No route-specific limitation is promoted to constitutional evidence.

## 11. TOE dependency ledger and maturity

| wall | Cycle-329 movement | still open |
|---|---|---|
| `C_ref` | Cycle-326's aggregate matcher is replaced by physical label/support comparison; all frame rotations are checked | label/support flag preparation, fixed comparator program, and primitive placement remain supplied |
| `C_num` | unchanged | no coefficient synthesis, numerical eligibility, or probability grading is added |
| `C_wrap` | predecessor readiness is now physically aggregated from identity-checked closed inputs and is schedule-quotient invariant | predecessor occurrence/permanence, present occurrence, close law, Record typing, clock matcher, interval, and rate remain open |
| `C_int` | unchanged | the matcher does not derive interaction occurrence or alter contact |
| `C_local` | advances through three bounded gate-level routes, held size, all frames, deletion, and exact Cycle-326 integration | economical encoding, primitive NN routing, autonomous flag preparation, and recurrent capacity remain open |
| `C_source` | unchanged | no energy, action, stress, resource, lapse, or gravity response is formed |

Using the combined accepted Cycle-327/Cycle-328 baseline, conservative
planning scores become:

| lane | integrated | strict floor | conditional | maturity | Cycle-329 disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 65% | 31% | 92% | 3.6/5 | aggregate anti-splice controls become bounded physical circuits; no Record |
| causal time / clock | 36% | 18% | 66% | 2.0/5 | physical predecessor readiness advances; occurrence and `R -> tau_C` remain absent |
| inertia / matter | 76% | 37% | 97% | 4.3/5 | unchanged |
| gravity / source / resource | 41% | 17% | 69% | 2.2/5 | unchanged |
| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 | unchanged; no occurrence, grade, or realized member |

These are planning scores, not truth probabilities or audit verdicts. Rebase
the unchanged lanes if concurrently packaged cycles alter the baseline.

## 12. Novelty and prior-art boundary

The retained repository result is the exact three-route integration of the
actual Cycle-314/Cycle-312 bounded-support event identity with Cycle 326's
physical receiver, including held-size, schedule, corruption, deletion, and
frame controls. Reversible equality circuits, Hamming syndromes, Toffoli
chains, causal certificates, and comparator ancillas are prior-art mechanisms.
No global novelty priority is claimed for them.

Thirring machinery is not used or compared.

## 13. Optimal next campaign

The next clean wall is now the occurrence/close predicate itself. A disciplined
campaign should independently test:

1. a local irreversible-looking but globally reversible occurrence witness
   tied to the actual Cycle-314 event transition;
2. a relational two-boundary close certificate that cannot be made true by
   event readiness alone;
3. a protected-history route in which earlier identity-checked candidates
   supply the predecessor-closed flags without assuming permanence.

The first two routes must keep event-ready, actual event, and close distinct.
The third must not call forward nonreturn permanence or a candidate a Record.
If all constructive routes fail and any negative is contemplated, apply the
full no-go discipline N1-N8 before shipping it.

## Verification

Run from the repository root:

```text
python3 scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py
```
