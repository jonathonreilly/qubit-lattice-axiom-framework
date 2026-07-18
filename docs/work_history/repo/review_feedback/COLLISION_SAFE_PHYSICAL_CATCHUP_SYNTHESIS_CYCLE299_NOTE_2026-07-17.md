# Collision-safe physical catch-up synthesis — Cycle 299

**Date:** 2026-07-17

**Type:** constructive physical-gate synthesis with full N1--N8 review

**Status:** collision ordering closed by bounded auxiliary ports; encoded
state, coin routing, and contact remain open

**Authority:** none

**Audit:** unset

**Constitutional effect:** none. No axiom, foundation, Qualification,
primitive, registry, policy, queue, or audit status is edited or proposed.

Companion runner:

```text
scripts/collision_safe_physical_catchup_synthesis_cycle299_2026_07_17.py
```

## Result in plain English

The `sqrt(3)` overlap-order residual in Cycle 297 was not a substrate
obstruction.  It came from making multiple matter arrivals act on one shared
cell tag.  Cycle 299 resolves that collision with a bounded covariant resource:
six auxiliary port M2 per cell, one per oriented matter half-edge.

For an undirected outer edge `(u,v)`, the literal Cycle-269 operators provide
the XOR control

```text
(I - B_u B_v)/2.
```

`B_u B_v` is phase-zero, pure `Z`, and weight eight.  Adding the two endpoint
port M2s gives a **ten-M2** auxiliary-tag swap.  Each port belongs to exactly
one outer edge, so auxiliary swap pairs are disjoint.  The diagonal face
controls commute even when their face supports overlap.  The completed
catch-up product is therefore algebraically independent of edge enumeration,
with no global parity service, preferred edge order, or host-side controller.

The cost is explicit:

```text
15 Cycle-269 face M2/cell + 6 auxiliary port M2/cell = 21 M2/cell.
```

This is not a minimum.  Smaller covariant layouts and autonomous schedules
remain open.

The physical and decoded claims are deliberately separate.  The physical
surface is the ten-M2 catch-up gate and its check/Wilson algebra.  The decoded
surface is a four-bit matter/port stream-plus-catch-up word that preserves the
declared `B_v Z_port(v)=+1` relation.  There is **not an assembled encoded
macrostep**, no bounded state encoder, and no full-Fock intertwiner.

## Exact controls and residuals

| control | result |
|---|---|
| local physical catch-up | `1024 x 1024`, unitarity/involution/auxiliary-tag-number residuals zero |
| decoded edge word | `16 x 16`, unitary/involutive, constraint commutator and leakage zero |
| catch-up deletion | decoded one-carrier constraint-leakage operator norm `1` |
| physical support | control weight `8`, catch-up `10`, inherited FSWAP `9`, union `11` M2 |
| constraints | ranks `162,384,750,1296` for `L=3,4,5,6`; code exponent unchanged at `164,386,752,1298` |
| collisions | all `864,2048,4000,6912` same-cell even fixtures plus `128` deterministic random even masks per size; zero order/inverse/phase failures |
| covariance | all 24 frames and all 27 `L=3` translations; descriptor and decoded-action failures zero |
| tested shared-cell axis word | cyclic-frame residual `sqrt(3)`, reversal residual `2` |
| disjoint-port product | cyclic-frame and reversal residuals zero |

The shared-cell failure is only a result about that explicit three-axis word.
It does not rule out a palindromic coloring, another constant-depth coloring,
an autonomous phase register, or a smaller port system.  The successful
disjoint-port word already defeats the corresponding broad scheduling
negative.

Compiler colors and edge enumeration are substeps, **not physical time**.
The port tag is not a Record.  No excitation count or gate phase is called
physical energy, a rate, gravity, or a source law.

## Supplied structure inventory

Load-bearing inputs are:

1. the Cycle-269 local-check-only square-pyramid face code and `B_v/A_e`
   dictionary;
2. the inherited outer-edge FSWAP and decoded arrival convention;
3. six auxiliary port M2 per coarse cell;
4. local relations `B_v Z_port(v)=+1` and a prepared total-even decoded input;
5. XOR control `(I-B_u B_v)/2` and stream-then-catch-up order;
6. periodic training `L=3,4,5`, held `L=6`, deterministic random fixtures,
   and the stated acceptance tests.

Derived are the support/rank ledgers, commuting order-free physical catch-up
product, decoded collision closure, covariance descriptors/actions, inverse,
deletion, and lawful-domain results.  Not derived are a preparation law,
bounded state map `E`, encoded coin/stream/catch-up update, contact, coupling
selection, energy/stress, clock, metric/tensor response, occurrence, Record,
or Born rule.

## Updated six-wall dependency ledger

| wall | Cycle-299 movement | still open |
|---|---|---|
| `C_ref` | unchanged | physical normalization, phase zero, reference genesis |
| `C_num` | auxiliary port constraints make the tag/occupation relation explicit, but the prepared total-even decoded input is supplied | common prepared encoded state and selected charge/occurrence sector |
| `C_wrap` | unchanged; the order-free product removes host enumeration, but compiler substeps are not time | event equivalence, recurrent clock, interval/rate calibration |
| `C_int` | unchanged; no Cycle-230 contact executes | same-code contact/resource ledger, recoil, protection, dressed inertia |
| `C_local` | materially advanced: the collision-order seam is constructively closed for the bounded gate/decoded-action surfaces with constant overhead and all-frame covariance | bounded physical state `E`, joint matter-coin/port routing, assembled full-Fock update, contact seam |
| `C_source` | unchanged by this gate-level result | one physical moving response law with reciprocal two-source and gravity/clock/tensor semantics |

## TOE lane update

These are evidence-weighted planning estimates, not audit verdicts or
probabilities.

| TOE lane | integrated | strict floor | conditional | maturity | disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 53% | 24% | 76% | 2.7/5 | score held; collision-safe physical gate structure improves `C_local`, but encoded state evolution, occurrence, and Record remain open |
| causal time / clock | 33% | 17% | 60% | 1.7/5 | unchanged; removal of host gate order is not a clock derivation |
| inertia / matter | 63% | 28% | 83% | 3.2/5 | unchanged; no dressed dispersion or physical mass bridge is earned |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 | unchanged; no source/response observable is executed on this physical code |
| Born / probability / realized history | 33% | 14% | 79% | 1.7/5 | unchanged; no squared norm is promoted to occurrence or probability |

## No-Go Discipline

The scoped negative is: “the supplied shared-cell three-axis tag word is
cyclic-frame and reversal invariant.”  The exact residuals `sqrt(3)` and `2`
falsify that statement.  This is a narrow finite-matrix result.

The candidate broad negative—“no bounded covariant collision-safe catch-up
word exists”—is false because the disjoint-port construction closes it.  Any
broader claim about minimum overhead, state compilation, or all auxiliary
routes fails N1 and must not ship.

**Gate status: FAIL for the candidate broad negative; do not ship it.**

### N1 — alternative routes

| route | marker | disposition |
|---|---|---|
| shared-cell three-axis word | **ATTEMPTED** | exact cyclic-frame and reversal residuals are nonzero |
| six-port disjoint auxiliary word | **ATTEMPTED** | exact constructive closure through held size |
| palindromic constant-depth coloring | **OPEN / UNTESTED** | may remove the tested word's order residual with fewer auxiliaries |
| alternate covariant edge coloring | **OPEN / UNTESTED** | may close with different compiler phases |
| autonomous local phase register | **OPEN / UNTESTED** | may internalize the schedule without host control |
| smaller auxiliary-port quotient | **OPEN / UNTESTED** | may reduce the six-port overhead |
| bounded encoded state lift | **OPEN / UNTESTED** | required before the gate becomes an encoded update theorem |
| joint matter-coin/port-routing word | **OPEN / UNTESTED** | required because the Cycle-219 coin mixes direction ports |
| same-code contact layer | **OPEN / UNTESTED** | required for the Cycle-230 interaction seam |

The broad obstruction and every minimum-overhead claim fail N1.

### N2 — wall-independence audit

The remaining conditions are `W_state` (bounded encoded state lift), `W_coin`
(joint direction-coin/port routing), and `W_contact` (same-code contact).

| first condition | second condition | closing first closes second? | closing second closes first? | independent? | reason |
|---|---|---:|---:|---:|---|
| `W_state` | `W_coin` | no | no | yes | a state lift supplies no update preserving it; a local update supplies no preparation/isometry |
| `W_state` | `W_contact` | no | no | yes | encoding free transport does not implement contact; contact does not construct `E` |
| `W_coin` | `W_contact` | no | no | yes | direction mixing and multiparticle contact test distinct local words |

No raw conditions collapse, and none is a shared obstruction certificate.

### N3 — hidden-condition scan

Explicit imports include the face code, outer FSWAP, six port auxiliaries,
local port constraints, prepared total-even decoded input, XOR control, update
order, periodic sizes, random seed, and acceptance thresholds.  The
all-frame test removes any implicit preferred axis from the completed
disjoint-port product.  No continuum, clock, energy, metric, probability, or
host renewal premise is used.

The literal rhetoric-trigger scan returned zero hits across all four
Cycle-299 package paths.  This scan is a prose control, not a physics premise.

### N4 — residual matching

| witness and file line | residual class | exact scope | matched to broad obstruction? |
|---|---|---|---:|
| shared-cell frame/order `sqrt(3),2`, `scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py:679` | `8 x 8` three-tag word difference | one supplied shared-cell axis word | no |
| disjoint-port frame/order `0,0`, `scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py:687` | disjoint swap-product difference | explicit six-port alternative | defeats broad collision negative |
| physical catch-up residuals `0`, `scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py:232` | `1024 x 1024` local gate unitarity/involution/tag-number | ten-M2 gate only | no state-compiler match |
| decoded deletion leakage `1`, `scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py:304` | `16 x 16` constraint-space operator norm | one-carrier decoded edge word | no physical full-update match |
| collision failures `0`, `scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py:532` | decoded mask/action/inverse counts | declared even fixtures through `L=6` | no state-compiler match |

The failed shared-cell residual and successful port residual concern matched
schedule equations.  Neither is evidence about the unexecuted state, coin,
or contact equations.

### N5 — rhetoric and resolution audit

“Collision-safe” means the completed physical catch-up product and decoded
even-mask action are order independent on the declared surfaces.  It does not
mean an assembled encoded full-Fock macrostep has been tested.  “Physical”
modifies the displayed ten-M2 gate, not the decoded state action.  “Covariant”
means the gate descriptor and decoded action transform across all 24 frames;
it does not make one serialized backend schedule observable.

| resolution | tested | unresolved |
|---|---|---|
| local gate | complete ten-M2 matrix | encoded state action |
| decoded edge | complete four-bit word | physical assembled stream/catch-up matrix |
| decoded collisions | all same-cell even subsets and random extended masks | exponential full-code census |
| symmetry | all frame/translation descriptors and decoded fixtures | an encoded macrostep conjugacy |
| physical semantics | support, commutators, constraints, squared masks | time, rate, energy, gravity, Record, occurrence |

### N6 — partial-closure paths

1. construct a bounded state lift satisfying all local port constraints;
2. lift the Cycle-219 six-mode coin jointly to direction ports;
3. test an assembled encoded stream/catch-up update on coherent states;
4. add the Cycle-230 contact only on that same encoded code;
5. independently search smaller palindromic/color/register alternatives.

These are constructive non-axiom paths.  Existing approved primitives are not
being recast as walls, and no new primitive or axiom is proposed.

### N7 — steelman

A hostile reviewer should insist that six ports are probably not minimal and
that the true compiler may use a smaller palindromic coloring or autonomous
phase register.  More importantly, the local constraint suggests a direct
Clifford extension of a fixed-sector Cycle-269 state map, followed by a joint
coin/port conjugation; if that construction works, the present gate is one
piece of a complete physical compiler.  The exact commuting XOR product and
dimension-neutral constraint rank support trying this route and defeat any
claim that collision ordering itself blocks the substrate.

### N8 — cross-cycle echo

| earlier seam | search/retirement mechanism | status |
|---|---|---|
| Cycle 296 fixed tag stayed behind moving matter | add a logical conditional transposition | logical ownership seam retired |
| Cycle 297 two arrival controls shared one cell tag and failed to commute | split the tag into the six proper-cubic half-edge orbit and use one XOR control per undirected edge | decoded collision-order seam retired with constant overhead |
| Cycle 269 local checks exposed Wilson sectors | retain the positive sector-indexed compiler and keep state preparation separate from local update | no general local-update obstruction; state map remains open |

The repeated mechanism is to expose the hidden local degree of freedom and
test the corresponding bounded update, while keeping preparation and
semantics separate.

**Disposition:** **no shared obstruction was identified** and **no axiom
pressure was established**.  Collision ordering is no longer the active
`C_local` seam for this construction.  Encoded state preparation, joint coin
routing, and contact are the next tests.

## Optimal next campaign

Construct a bounded physical state lift into the six-port constraint space.
If that succeeds, conjugate the actual Cycle-219 six-mode coin into a joint
matter/port word and test a complete encoded free macrostep before adding the
Cycle-230 contact.  If it fails, retain fixed-sector, open-boundary, subsystem,
and resource-state routes separately; one state-map failure is not a shared
substrate obstruction.

## Verification

```text
python3 -m py_compile \
  scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py \
  scripts/collision_safe_physical_catchup_synthesis_cycle299_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/collision_safe_physical_catchup_synthesis_cycle299_2026_07_17.py
```
