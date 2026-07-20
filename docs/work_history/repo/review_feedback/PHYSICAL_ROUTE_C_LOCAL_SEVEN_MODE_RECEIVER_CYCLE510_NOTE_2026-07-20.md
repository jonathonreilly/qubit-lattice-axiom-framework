# Physical Route-C local seven-mode receiver — Cycle 510

Date: 2026-07-20

Authority: **none**

Audit: **unset**

Disposition: **constructive local-algebra pre-response certificate; combined
physical update, global compiler, response train, and held rows remain open**

## Result up front

Cycle 510 constructs bounded local Route-C receiver components for the
physical-M2 campaign.  It joins the Cycle-311 local six-mode CAR code shell to
seven literal M2 hard-core mediator occupations and supplies a
charge-preserving reciprocal collision, a parked-to-directional emitter, and
an exact moving stream.  The runner passes `18/18` controls.

For the collision factor only, the declared code shell admits the formal lift

\[
U_{\rm shell}=(E\otimes I)U_{\rm collision}(E\otimes I)^\dagger
 +I-(E\otimes I)(E\otimes I)^\dagger,
\]

and the one-seeded-ray residual for its on-code intertwiner is
`1.9118895389845036e-16`.  The post-update constraint residual is zero and the
adjoint-inverse residual is `3.715300541732851e-16`.

This is not an independently constructed physical-site generator and not yet
the campaign's global compiler.  The witness is a conjugation-defined,
one-ray, collision-only code-shell lift.  It does not execute the displayed
off-code completion operator-wide, act on the raw M2 ambient space, test
physical-frame covariance of `E`, compose emitter/stream/collision into one
lift, synthesize a bounded primitive gate word, prove shared-cell multi-edge
compatibility, prepare the code autonomously, or execute any of the eight
frozen Route-C response rows.  Those distinctions are part of the result, not
packaging caveats.

The selected mediator statistics are also supplied rather than derived:
seven ordinary hard-core qubit/spin M2 factors use ordinary SWAP.  Fermionic
exterior Fock with FSWAP and a local gauge remains a live alternative.  The
Cycle-501 one-mediator seam cannot distinguish them because ordinary SWAP and
FSWAP differ only on double occupation.

## Frozen evidence

| item | exact value |
|---|---|
| runner SHA-256 | `57592ac109321cb273f73b312d205cefc18427329d20c34f18f63d56dcbd5175` |
| result transcript SHA-256 | `f8c12e463d6b44df22964b04a05d0b60e332ab408e4340fdd61421555762d84a` |
| scientific payload SHA-256, excluding resources | `7ee5dcebc9a1b53816df87db754f97b783cb3963b0ee08895dd6d090540af1d8` |
| canonical direct-dependency-map SHA-256 | `016c9248154063abdb5ca998c240be0a1c1e8980e0305d3580785e6fbc60b5fb` |
| tests | `18/18` |
| response / held rows | `0 / 0` |
| status | `local-pre-response-certificate` |

The exact transcript is
[`outputs/physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20.log`](../../../../outputs/physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20.log),
and the environment/hash receipt is
[`outputs/physical_route_c_local_seven_mode_receiver_cycle510_receipt_2026_07_20.json`](../../../../outputs/physical_route_c_local_seven_mode_receiver_cycle510_receipt_2026_07_20.json).
The runner is
[`scripts/physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20.py`](../../../../scripts/physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20.py).

Cold replays matched every scientific field while wall time and peak RSS
varied, as expected.  The receipt therefore hashes the complete transcript and
separately hashes the canonical payload with `resources` removed.  The
dependency-map digest covers the six reported direct files; it is not
represented as a transitive import closure.

## Exact local construction

The logical cell is

\[
\mathcal H_{\rm cell}=\Lambda^\bullet(\mathbb C^6)\otimes
(\mathbb C^2)^{\otimes 7},
\]

with dimension `64 * 128 = 8192`.  The seven mediator bits are one parked bit
and six directed bits.  A global-Q6 experiment reaches the local sectors
`Q=0..6`; the physical but unreachable `Q=7` block is not included in that
code-space count.

The reciprocal collision is one exponential of the Hermitian sum over three
unoriented axes plus their conjugates.  Its sector oracle is:

| mediator charge | dimension | generator nonzeros |
|---:|---:|---:|
| 0 | 64 | 0 |
| 1 | 448 | 96 |
| 2 | 1344 | 480 |
| 3 | 2240 | 960 |
| 4 | 2240 | 960 |
| 5 | 1344 | 480 |
| 6 | 448 | 96 |
| total | 8128 | 3072 |

Hermiticity, matter number, mediator charge, CAR/Pauli/hard-core transition
lawfulness, and all-24 proper-cubic covariance are exact.  The three axis
blocks commute exactly.  Consequently the single summed exponential and a
correct three-factor axis word are numerically indistinguishable here; the
single exponential is provenance discipline, not evidence selecting a new
law.  Adding six directed Hermitian terms and then their conjugates would
double-count the collision and is excluded.

The exact `N=2`, moving-`Q=1` projection agrees with the Cycle-501 generator at
zero residual.  Its finite exponential at the actual Cycle-501 seam angle
`0.31` agrees at `1.9229626863835638e-16`.  This reproduces the inherited local
seam rather than fitting a new coupling.

The emitter acts as independent parked/directional two-level rotations.  Its
unitarity, inverse, and all-24 carried covariance residuals are zero.  The
stream is the fixed local word `J S_face`: face SWAP first, then onsite
antipodal reversal.  Across 2,510 configurations through global charge six,
its moving-map, inverse, charge, and all-24 covariance failure counts are all
zero.  This certifies the unbounded/interior local map; a finite open-boundary
completion remains to be frozen before response execution.

All 576 frame products satisfy the exterior-matter and mediator-qubit group
laws exactly.

## Physical-M2 support and preservation

The Cycle-311 matter encoder has shape `510 x 64`, with Gram residual
`1.6690311775283582e-15`.  Tensoring seven literal mediator M2 factors gives a
local 8,192-dimensional logical receiver on a `510 x 128` encoded shell.  The
bounded inventory is:

| inventory | count |
|---|---:|
| Cycle-311 installed M2 per cell | 23 |
| seven mediator M2 added per cell | 7 |
| single-cell receiver M2 | 30 |
| homogeneous matter/edge-role/mediator M2 per cell | 36 |
| two-cell patch-union plus mediator M2 | 97 |
| two-block mediator `Q<=6` dimension | 6476 |
| two-block mediator exact global-`Q6` dimension | 3003 |

Cycle-315 contributes the bounded one-active-edge support audit: its port and
fixed-sector constraint commutator failure counts are zero.  It does not yet
prove simultaneous compatibility of all shared-cell edges or a global
multi-edge encoding.

The Cycle-230 contact is identity in `N<=1`, and the reciprocal collision is
identity in mediator `Q=0`.  The three safe Cycle-219 one-particle rows recheck
their analytic rest-mass identities with maximum residual
`4.440892098500626e-16`, coin unitarity residual
`1.3312813853149888e-15`, and all-24 covariance residual zero.  This is not an
encoded interacting propagation test and not a held or principal mass
prediction.

The zero-angle emitter identity is executed.  Zero/identity semantics for
collision, stream, contact, probe coin, and both source/probe mass factors are
declared but not dynamically measured here; deletion-effect distances
executed are zero.  Three malformed hard-core/domain inputs are rejected
exactly.  No deletion response has yet been measured because no Route-C
response row ran.

## Supplied, derived, and open inventory

Supplied:

1. the Cycle-219 coin/mass coordinates, Cycle-230 contact, Cycle-311 matter
   encoder, Cycle-315 one-active-edge support, and Cycle-501 local collision;
2. seven hard-core qubit/spin mediator M2 factors, ordinary SWAP statistics,
   the parked/directional labeling, emitter form, collision angle used for the
   inherited seam comparison, and stream word;
3. the formal dense identity-off-code completion and local code-shell input;
   and
4. finite test angle, numerical tolerances, deletion meanings, train mass
   points, and the global-Q6 domain.

Derived on that supplied local domain:

1. the full collision-sector dimensions and nonzero counts;
2. exact charge/lawfulness/Hermiticity and all-24/576 covariance/group laws;
3. the Cycle-501 generator and exponential seam agreement;
4. exact emitter/stream inverse and occupation-map controls;
5. the one-ray collision code-shell lift witness and constraint preservation;
   and
6. the analytic one-particle/contact/Q0 fixture controls.

Open:

1. simultaneous shared-cell multi-edge constraints and a global lattice
   encoding/update intertwiner;
2. decomposition of the dense on-code completion into bounded physical M2
   primitives and autonomous code/source preparation;
3. mediator-statistics selection between ordinary hard-core SWAP and the live
   FSWAP/local-gauge alternative;
4. an explicit finite boundary law, exact Route-C initial state, response
   surface/statistic, schedule, free partner, deletions, and held-size-only
   control;
5. all eight Route-C train rows, the atomic A/B/C held evaluator, and law
   selection; and
6. conserved energy/stress/source, clock calibration, gravity, probability,
   Records, and realized history.

## Route-C input-freeze correction

The Cycle-509 `exact_packet` still names Route C as an obligation; it does not
freeze enough law-level input to run its response rows.  In particular,
Cycles 421/423/426 are useful bounded predecessors but are not hashed
dependencies of Cycle 509 and cannot be silently imported.

The next revision must choose the exact two-particle matter packet.  A separate
read-only packet-fork analysis, not one of the Cycle-510 controls, found a
candidate rank-one sign-character ray of the proper-octahedral action on
`Lambda^2(C^6)`.  It therefore indicates that proper-cubic covariance need not
force a mixed state, but the candidate still requires its own executable
preflight certificate.  A mixed equal-weight A/B axis-orbit packet remains
attractive because it reuses the registered corridor envelopes, but its
mixedness and `1/3` weights would be supplied.  This is a constructive choice
between live routes, not an obstruction or axiom pressure.

The revision must also repair two preregistration issues before execution:

1. the separate schedule analysis proposes sampling after the complete update
   as the smallest surface that can see a center collision; this timing claim
   must be frozen and executed in preflight, while an earlier Route-A-style
   surface would require more depth/window and cannot be called a certified
   current without a continuity law; and
2. the existing positive L19 row changes both size and probe beta relative to
   the positive L15 row.  A matched-beta L19 row or equivalent frozen
   normalization is required to isolate held-size stability.

## Six-wall and TOE-lane disposition

| wall | exact movement | residual |
|---|---|---|
| `C_ref` | none | preparation, statistics, coupling, phase/zero, and normalization remain supplied |
| `C_num` | a bounded seven-M2 charge carrier and exact sector ledger are constructed | no selected number reference, conserved source, energy, or probability follows |
| `C_wrap` | none | the stream/update index is not causal time or a rate; the repository's clock derivation still needs an explicit bridge to this 3D substrate |
| `C_int` | the summed reciprocal collision reproduces the Cycle-501 seam and rechecks contact/mass identities | encoded propagation, response, occurrence/rate/protection, and law selection remain open |
| `C_local` | advanced by the bounded local algebra, exact stream, all-24 covariance, and one-ray collision code-shell lift | a combined physical update, global shared-edge compatibility, primitive synthesis, preparation, boundary, and held remain open |
| `C_source` | directional emitter exists as a lawful local factor | its amplitude/profile is supplied and no conserved stress/source or gravity meaning is established |

No TOE lane percentage moves on this bounded, pre-response certificate.  The
campaign planning scores remain operational quantum/Records `90/49/99`, causal
time `65/40/99`, matter/inertia `80/42/99`, gravity/source/resource `59/30/94`,
and Born/probability/realized history `76/44/99` (integrated / strict /
conditional maturity, not probability or audit status).

## No-go discipline and next step

No impossibility, minimum-content, or axiom-pressure claim is made.  The
ordinary-SWAP and FSWAP statistics remain live, the pure and mixed matter
packets remain live, and global compilation has not been tested.  A route-
specific implementation gap is not constitutional evidence.

The next step is a separate input-freeze/preflight revision.  It must choose
and hash every Route-C law-level input, add a matched held-size-only row, prove
the finite boundary and sampling schedule, and pass an independent dry review.
Only then should the resource sentinel and eight-row train execute; held must
remain locked until all A/B/C train evidence is complete.
