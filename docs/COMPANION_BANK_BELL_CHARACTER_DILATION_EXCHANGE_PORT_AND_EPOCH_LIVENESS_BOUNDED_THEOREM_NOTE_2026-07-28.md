# Cycle 721: literal physical-M2 input-Bell compiler, even-exchange port, and collision-free epoch composition

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary constructive runners:

- [`frontier_cycle721_car_bell_input_m2_compiler_2026_07_28.py`](../scripts/frontier_cycle721_car_bell_input_m2_compiler_2026_07_28.py)
- [`frontier_cycle721_encoded_input_clifford_port_2026_07_28.py`](../scripts/frontier_cycle721_encoded_input_clifford_port_2026_07_28.py)
- [`frontier_cycle721_collision_free_epoch_composition_2026_07_28.py`](../scripts/frontier_cycle721_collision_free_epoch_composition_2026_07_28.py)

Independent adversarial reconstruction:

- [`frontier_cycle721_tournament_independent_adversary_2026_07_28.py`](../scripts/frontier_cycle721_tournament_independent_adversary_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

All runner ordinals, gate words, schedule slots, and layer indices in this
package are circuit structure. None is called physical time, duration, rate,
or energy. All couplings are state-level on the declared code; no matter,
FTL, mass, or charge transfer is claimed or implied.

## Result up front

Cycle 720 closed the recurrent companion update, the local Choi pump, and a
fixed-sector CAR-domain live-input map, and declared as its next decisive
experiment a three-route literal physical-input and epoch-integration
tournament, leaving `input_Bell_measurement_physical_M2_compiled: false` in
its receipt. Cycle 721 runs that tournament. All three routes close
positively at the bounded ceiling, on the same supplied sector/genesis
inventory as Cycle 720.

**Route 1 — literal M2 compilation of the input-side even-CAR Bell
measurements.** Every row of the doubled even-CAR Bell family — six onsite
parities and five adjacent-Majorana pairs per cell plus one oriented seam row
per nearest-neighbor edge, `11N+E` rows in the frozen
`P.direct_graph_basis` order — is compiled into a literal physical word
`H(ancilla); controlled-Pauli per supported M2; H(ancilla)` with one retained
measurement ancilla per row at the row's anchor cell and nearest-neighbor
returned routing. The live input is presented on a companion-encoded input
bank (a full mirror of the physical register at `[q, 2q)`): the input-side
image of each row is the same companion-represented physical row, so every
compiled word has support at most two cells and graph diameter at most one —
the preregistered Cycle-720 gate — on all six boxes

| box | rows = 11N+E | max word support (cells/diameter) | max private-dual support |
|---|---:|---:|---:|
| `1x1x1` | 11 | 1 / 0 | 1 / 0 |
| `2x2x2` | 100 | 2 / 1 | 1 / 0 |
| `3x2x2` | 152 | 2 / 1 | 1 / 0 |
| `5x3x2` | 389 | 2 / 1 | 1 / 0 |
| `4x4x4` | 848 | 2 / 1 | 1 / 0 |
| `5x5x3` | 995 | 2 / 1 | 1 / 0 |

The compiled family is abelian and Hermitian with unchanged GF(2) rank
(`11N+E` on every box). The dilation identities are exact and exhaustive: the
retained ancilla's transported `Z` equals `Z(ancilla) * R_i` and its `X` is
fixed, while every other measured row and every Choi graph row is invariant.
Bell-branch corrections remain the frozen Cycle-720 one-cell private duals
with one-hot syndrome duality, even kernel sums, and an active
deleted-dual unit sign residual. The exact two- and three-mode fixed-sector
CPTP certificates of Cycle 720 rerun unchanged. On this package's surface the
Cycle-720 receipt flag `input_Bell_measurement_physical_M2_compiled` becomes
**true** at the bounded ceiling.

**Route 2 — direct local encoded-input Clifford port.** An 18-primitive
one-cell word (six three-CNOT exchanges between a co-located six-M2 live bank
and the port cell's matter modes) couples a live even-CAR input by reversible
exchange: exact on the full 36-row port-cell dictionary in both directions,
with exact joint-parity bookkeeping and odd-input detection. The
seam-extended coupling word — synthesized by greedy symplectic transvections
against the four seam bilinears of each incident edge — turns out to be
**port-local as well**: support one cell, diameter zero, on every tested axis
and box. In the companion representation the non-port endpoint factors of a
seam bilinear are common to the bank-ended and matter-ended forms, so seam
coupling leaves nothing cross-cell to correct. This is the constructive
counterpoint, on the same code, to the Cycle-720 raw-mode diagnostic in which
the frozen raw-X/Jordan-Wigner route reached seven support cells and graph
diameter four on the held box.

**Route 3 — collision-free epoch composition.** The four stages — local Choi
pump preparation, input Bell coupling, retained correction banks, and the
recurrent matter word `G` — compose into one explicitly scheduled epoch on
one literal site map, in two declared variants: the primary leg couples the
input through the Route-1 compiled Bell words, the alternate leg through the
Route-2 exchange port. A global register table spans code, companion-encoded
bank, routed-only `G` sites (discovered by introspecting the routed word's
site-addressed instructions and mapped through the exact `U.placement`
bijection), Bell ancillae, pump syndrome bank, pump Bell purifiers, the
unchanged coframe surface, and one mobile rail per cell. A Cycle-54-style
slot walk (clean, live-with-owner, retained; retained access requires an
executed declared handoff) walks up to 76,376 slots and 159,219 register
touches on the held `5x3x2` box with **zero** collisions, ownership
violations, premature reads, or unconsumed handoffs, for both variants on
every box. Staged-versus-flattened tableau action is exact for the
preparation/coupling/correction stages on `1x1x1` and `2x2x2` with the `G`
tail anchored by the unchanged imported Cycle-720 one-step certificate; the
imported `3x2x2` recurrent one-step conjunction, the `2x2x2`
orientation/interleave/deletion gates, the three mass/contact residuals, and
the five Cycle-230 fixture residuals all rerun unchanged. Schedule-key and
per-family census multisets transport exactly over all 24 frames and eight
translation parities (192 contexts), with the four coframe-constraint
failure fields zero. Deleted-handoff, deleted-return-word,
stage-B-before-pump hostile interleave, and duplicate-owner controls are all
detected.

**Independent adversarial reconstruction.** The checker blocks runtime
import of the three primary runners (transitive guard) and rebuilds the
lower-level algebra from the Cycle-720 modules with its own independently
written Clifford conjugation. It reports 6/6 PASS: the exchange-port
dictionary, the dilation identities on an independently rebuilt
companion-encoded row family, atlas one-hot duality with one-cell support,
the seam orientation classes over all 24 frames and eight parities (2,304
quadruples), an independently reconstructed epoch schedule with its own
liveness walk (including detected fault injections), and the inherited
fixture residuals plus a dense fixed-sector Kraus rebuild. Its dense
self-test covers 8,208 comparisons with zero mismatches. Its one wording
correction is adopted in the Route-3 section below.

## Route 1: compiled measurement words

The compiler consumes the Cycle-720 surface unchanged: fixtures from
`O.arbitrary_fixture(Q.shape_cells(shape))`, the frozen `(graph, tags)` order
of `P.direct_graph_basis`, targets from the even-CAR Bell runner's
`target_rows`, the frozen private-dual atlas of `P.build_private_atlases`,
and `P.returned_route` / `P.route_execution_failures` for rail accounting.
Two consistency anchors bind the compiled family to the landed Choi surface
exactly: the physical restriction of every graph row equals an independently
rebuilt tag row, and the coarse-input half of every graph row equals its
target row binarily, on every box with zero failures.

The measured joint row is `R_i = canonical(physical_i * shift_q(physical_i))`
— the code-side row times the same companion-represented row on the input
bank. Ancillas live at `[2q, 2q + rows)`, one rail M2 per cell above them;
route transitions are literal rail moves with returned work verified forward
and inverse. Measurement outcomes stay in retained ancillae; no reset,
postselection, or dissipative erasure appears anywhere in the package.

The conflict-coloring census obeys an exact structural law on every box:

```text
measurement layers = 3 + (maximum cell degree)
```

three onsite layers from the Z/XX path coloring plus exactly one seam layer
per unit of maximum cell degree — greedy first-fit attains the Koenig
edge-coloring bound of the bipartite box graph in the emitted edge order.
Measured: `3, 6, 7, 8, 9, 9` on the ladder above, saturating at nine on both
interior-complete boxes (`4x4x4`, `5x5x3`). Correction coloring is constant
at eleven from `3x2x2` on. Constancy across arbitrary boxes is not the
covariant statement; the local incidence profile is.

Compiled-schedule covariance is exact over all 24 proper-cubic frames and
eight translation parities on `2x2x2` and `3x2x2` (384 contexts): signed and
binary family multisets transport exactly for the onsite families, and every
transported seam quadruple lands in one of the two fixture-derived
orientation classes (3,072 forward and 3,072 reversed classes, zero
failures), with census vectors invariant. The unchanged Cycle-720
`V.frame_certificate` / `V.product_certificate` surfaces (24 frames, 576
ordered products) retain zero named failures. The adjacent-pair generating
set itself is a Jordan-Wigner path chart and is deliberately not compared as
a set; the covariant objects are the dictionary families and orientation
classes.

Controls: deleting one private dual leaves a unit Bell sign residual;
deleting the final return link breaks the forward returned-route walk and
deleting the first link is detected as well; hostile ancilla pairing
(measuring row `i` into row `j`'s ancilla) produces dilation failures; an
unlawful odd input row is detected by the joint parity row. A dense
`8x8` Clifford-conjugation self-test over all signed weight-one/two rows and
all gate instances has zero mismatches.

Supplied for this route, beyond the Cycle-720 inventory: the
companion-encoded input bank convention — the live input is presented in the
code's own companion representation. A bare global-Jordan-Wigner input
register was considered at design time and rejected before certification
because its seam characters drag global strings across the bank; that design
history is recorded here as the reason for the supplied convention, not as a
tested negative claim about any route.

## Route 2: even-exchange port and seam coupling

The port is the lexicographic-minimum cell as a supplied chart convention;
covariance is evaluated at the transported image of the port, where signed
and binary port-dictionary multisets, seam orientation classes, and census
vectors are exact over all 24 frames and eight translation parities on both
tested shapes (zero failures in every counter). The lexicographic-minimum
default itself is not frame-covariant (168 of 192 contexts relocate it);
that is chart bookkeeping, not a covariance failure.

The mixed-gauge factorization anchors rerun exactly
(`F.phase_fixed_factorization` on `2x2x2` and `3x2x2`: dimension identity,
CPTP construction, factorwise intertwiner, and zero coordinate failures,
tableau digests `e83b7b24...` and `10ec1180...`). Its own locality census
reports the canonical tableau is **not** radius-two bounded on the tested
boxes. That census is the measured ceiling for any future literal
`V_s`-restriction input compiler; no such compiler is constructed here, and
the factorization module exposes no public tableau/coordinate API. The
`V_s`-restriction route therefore stays `UNTESTED/OPEN`, with the named
reopen condition being a public immutable factorization-object API in a
future cycle.

Controls: single-CNOT deletion, a middle-CNOT direction flip (the literal
reversal of a three-CNOT swap is palindromic and is reported as an identity,
not a control), a stray appended primitive on the seam word, odd-input
detection, and a wrong-port word are all detected.

The exchange port consumes the cell's prior matter state reversibly into the
retained bank; it is not the gauge-mixed logical injection `E_s`, which
remains the Bell/Choi route of this same package.

## Route 3: epoch composition

The epoch schedule is a fixed finite slot table. Per-box slot counts for the
four stages (primary variant, `A/B/C/D`): `1x1x1` 23/3/11/421; `2x2x2`
225/9/112/17,304; `3x2x2` 345/11/172/26,940; `5x3x2` 897/13/448/75,018. The
alternate variant replaces stage B by the 18-primitive port word
(`23-897/18/0/...` — the exchange port needs no correction stage). Stage-D
counts are the unchanged routed nearest-neighbor primitive counts of the
Cycle-720 recurrent word.

The two input legs use one bank namespace with a checker-supplied
qualifier: standalone Route 2 declares a six-M2 port bank at `[q, q+6)`,
while the composed epoch embeds a port-indexed six-qubit block inside the
Route-1 companion-encoded bank `[q, 2q)`; the two coincide only at port
index zero.

The `G` word's instructions are site-coordinate-addressed; the namespace
builder verifies `U.placement` exposes one unique site per code qubit,
preserves the code block `[0, q)` and the bank `[q, 2q)` unchanged,
enumerates routed-only `G` sites after the bank, and shifts every auxiliary
allocation above the discovered `G` footprint. The instruction schema
actually used (`kind`, `sites` coordinate tuples) is recorded in the report
rather than assumed.

Handoff edges are derived from the literal slot order (cross-stage transfers
and syndrome/ancilla write-then-read channels) and then enforced by the
walk; the four controls demonstrate each failure class is detected rather
than merely absent: deleting a declared handoff edge, deleting a route
return word, moving a stage-B slot before the pump row it depends on, and
scheduling two words on one register in the same slot each produce the named
violation.

The one-time epoch, the clean initial banks, the declared stage order, and
both input-leg conventions remain supplied. No renewal, positive-density
multi-source composition, or autonomous scheduling is claimed.

## Independent adversarial reconstruction

The checker imports only the landed Cycle-720 modules, asserts that none of
the three Cycle-721 primaries is imported even transitively, and validates
its own independently written signed conjugation against dense matrices
(8,208 comparisons, zero mismatches) before using it. It then rebuilds,
without consulting the primaries' code paths: the six-SWAP exchange word and
the full 36-row port dictionary exchange with parity bookkeeping and the
one-cell census; the companion-encoded measured-row family with abelian
structure, unchanged `11N+E` rank, the `H`-controlled-Pauli-`H` dilation
identities, and the two-cell/diameter-one census; an independent one-hot
private-dual verification against the Choi graph; the fixture-derived seam
orientation classes over all 192 frame/parity contexts; an independently
reconstructed four-stage epoch schedule walked by its own
clean/live/retained state machine, with injected dropped-handoff and
duplicate-owner faults detected; and the inherited mass/contact and
Cycle-230 residual anchors plus a dense two-mode fixed-sector Kraus
completeness rebuild. It supplies one wording correction (the epoch
F2-leg namespace qualifier), adopted above.

## Supplied / derived / open

### Supplied

- the full Cycle-720 inventory, unchanged: Cycle-219/230 fixtures and
  parameters; per-cell six-mode labels and companion-port convention; one
  fixed total-parity label; local center-sector signs and mixed gauge factor
  or reference purification; three coframe bits per cell and the uniform
  eight-origin channel; finite open boxes, boundary root, axis order,
  spanning-tree/router tables; one-time preparation epoch; clean Bell,
  syndrome, route, and preparation registers; the fixed four-layer update
  schedule;
- the companion-encoded input bank convention (Route 1) and the co-located
  six-M2 port bank with the lexicographic-minimum port chart (Route 2);
- clean measurement ancillae and rail M2 for the compiled words;
- the declared stage order of the composed epoch (Route 3).

### Derived

- a literal physical-M2 measurement word for every doubled even-CAR Bell
  row, with retained ancilla, returned routes, and the two-cell/diameter-one
  support gate met on all six boxes up to `995` rows;
- exact dilation identities and unchanged `11N+E` rank, abelian and
  Hermitian, with the frozen one-cell private-dual correction surface;
- the conflict-coloring law `measurement layers = 3 + maximum cell degree`
  with interior saturation, and constant correction coloring from `3x2x2`;
- an 18-primitive reversible even-exchange input port exact on the full
  port dictionary, with port-local seam-extended coupling (one cell,
  diameter zero) on every tested axis;
- exact compiled-schedule and port-dictionary covariance over 24 frames and
  eight translation parities via dictionary families and fixture-derived
  seam orientation classes;
- a collision-free composed epoch (preparation; coupling; corrections;
  recurrent `G`) on one literal site map for both input legs, certified by
  a slot-walk register-liveness state machine with detected-failure
  controls, unchanged recurrent/fixture gates, and exact schedule-key
  transport;
- active deletion, hostile-order, stray-primitive, wrong-port, odd-input,
  and route-deletion controls throughout.

### Open

- autonomous preparation or local enforcement of the total-parity, center,
  mixed-gauge, coframe, clean-ancilla, clean-bank, root, and epoch domains;
- a public immutable `V_s` tableau/coordinate API and a literal
  `V_s`-restriction input compiler (measured ceiling recorded above);
- a boundary-free translation-invariant recurrent genesis law; periodic
  topology, fault repair, positive-density multi-source composition, and
  renewal;
- the eight-origin coframe channel covariance of the composed epoch beyond
  the unchanged Cycle-720 surface;
- objective actuality/admission, physical time/rate, source/gravity meaning,
  permanent Record, Born weighting, and realized-history selection.

## Six dependency categories (not independent walls)

| category | Cycle-721 change | remaining dependency |
|---|---|---|
| `C_ref` | no runtime exterior-order query; compiled words, port words, and schedules are explicit local circuits | root/boundary, parity label, center signs, gauge reference, epoch, mode labels, parameters, finite router, and the two input-bank conventions remain supplied |
| `C_num` | the input-side Bell measurements are literally compiled; the CAR-domain live-input map of Cycle 720 now has a physical instruction surface | physical selection/enforcement of the parity and center sector; the `V_s`-restriction compiler |
| `C_wrap` | the composed epoch is a fixed finite slot table with a verified liveness walk; retained banks carry all outcomes | every ordinal remains circuit structure; occurrence, empirical interval/rate, and permanent Record remain open |
| `C_int` | free/seam/contact/mass and Cycle-230 fixtures rerun unchanged under the compiled surface | coupling selection, physical rate/protection, and downstream source/work ledger remain open |
| `C_local` | two-cell/diameter-one gate met by every compiled word; port-local seam coupling; conflict-coloring law with interior saturation | autonomous genesis/enforcement, boundary-free recurrence, periodic/fault-tolerant family |
| `C_source` | unchanged at the physical compiler layer | no energy/stress/resource source, reciprocal response, sign/scale law, or gravity identification is selected here |

## Negative-claim discipline

No new negative claim ships in this package. The only negative-flavored
statements are: (i) supplied-convention boundaries (the companion-encoded
input bank and the port chart), including the design-history record that a
bare global-Jordan-Wigner input register was rejected before certification —
an untested design decision, not a route falsification; (ii) the inherited
Cycle-720 raw-mode Bell diagnostic, cited strictly at its original one-frozen-
route scope; and (iii) the package-inventory statement that no literal
`V_s`-restriction compiler is constructed here, with its reopen condition
named. None of these is promoted to a no-go, minimum-content result,
wall-independence theorem, shared obstruction, or axiom-pressure claim.

## Verdict and next experiment

All three declared routes of the Cycle-720 tournament close positively at
the bounded ceiling on the unchanged supplied inventory: the input-side
even-CAR Bell measurements are literally compiled and meet the preregistered
two-cell/diameter-one gate on every box; a direct local encoded-input
Clifford port exists and its seam-extended coupling is port-local; and the
four-stage epoch composes collision-free on one literal site map for both
input legs, with a verified register-liveness walk. There is no shared
obstruction and no axiom pressure. Nothing here selects a sector, prepares
its own inputs, removes a boundary, or touches time, Record, Born, or
source content.

The Cycle-720 gate for downstream work is now satisfied at this package's
resolution. The next decisive experiment is the one Cycle 720 already
named: feed the unchanged Cycle-612 endpoint/interval harness and the
coherent source-lift tournament through this composed epoch toward the
repo-side response/prediction chain, without refitting any fixture. In
parallel, three constructive legs remain live at their recorded scopes: a
public immutable factorization-object API to open the `V_s`-restriction
compiler (its measured locality ceiling is recorded above); the Cycle-719
W1 leg (wrap the five-M2 refusal primitive around every controller macro);
and the local Gauss/charge-sector route toward autonomous sector
enforcement. Renewal, boundary-free genesis, and multi-source composition
stay open exactly as inherited.
