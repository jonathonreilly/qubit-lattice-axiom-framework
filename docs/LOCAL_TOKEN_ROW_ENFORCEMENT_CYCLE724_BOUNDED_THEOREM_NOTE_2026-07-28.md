# Cycle 724: radius-one refusal guard for the supplied token row

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle724_local_token_row_enforcement_2026_07_28.py`](../scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py)

Independent check:

- [`frontier_cycle724_token_row_independent_check_2026_07_28.py`](../scripts/frontier_cycle724_token_row_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

All controller ordinals and orbit counts are circuit structure. None is
called physical time, duration, rate, or energy.

## Result up front

[Cycle 723](REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md)
wrapped every controlled macro of the
[recurrent two-rail controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
in a reversible dirty-rail refusal. Cycle 724 extends that sandwich with one
specific radius-one refusal guard:

- per station, the refusal syndrome becomes the reversible OR of `B_s`,
  `work_s`, and the four radius-one neighbor occupancies `A_(s-1)`,
  `B_(s-1)`, `A_(s+1)`, and `B_(s+1)`. The OR cascade uses four fresh clean
  scratch bits, and the computation is uncomputed exactly. All rail inputs
  remain invariant inside the controlled-data block. The extended `H` word
  has 98,034 gates, compared with 95,850 for Cycle 723 and 61,562 before the
  refusal wraps;
- on the supplied lawful one-token trajectory, no named radius-one dirty
  input is set at Q-time. The held 2/5/12-bank cases and the padded
  130-station orbit preserve their exact data action, rail return, auxiliary
  return, and inverse, while reproducing the Cycle-723 gate-count and digest
  anchor;
- in the adjacent two-token sector at positions `(0, 1)`, each controlled
  data macro encountered by either token is suppressed. The output equals an
  independently constructed identity-substituted prediction, and both tokens
  remain visible at return;
- the padded-program census contains six cases for every one of the 91
  nonidentity stations, for 546 cases total. Each dirty input is transported
  to the named target row at its Q-time. Every case witnesses the target
  syndrome in the literal station block, the suppressed block is exactly
  identity on its full input, and the full literal orbit agrees with the
  independent identity-substituted prediction with exact rail and auxiliary
  return;
- on the declared 130-station ring, the two-token sector at positions
  `(0, 65)` passes this specific radius-one guard and equals its own unwrapped
  hostile-sector prediction. This finite example shows that the guard added
  here does not discharge the separately supplied global one-token
  condition. It is not a theorem about every finite-radius constraint or
  arbitrary ring length; and
- deletion controls for one OR-compute gate and one uncompute gate are
  active. The structural physical layer, 24 proper-cubic frames, 576 frame
  products, translations, the compiled extended orbit on all six
  [physical endpoint-instrument](PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  branches, and the inherited pin/residual anchors re-certify.

## Exact conditional claim

Given the unchanged Cycle-719 controller inventory, the Cycle-723 clean
syndrome and MCX-scratch inputs, and four additional clean OR-cascade bits per
station, every nonidentity controlled data macro is guarded by the six named
radius-one inputs. A dirty input suppresses that macro and is left visible in
its original rail or work register; the syndrome and both scratch families
return clean. The lawful supplied trajectory is unchanged.

This is a bounded circuit construction, not autonomous sector preparation.
It does not enforce every radius-one constraint, remove the supplied global
one-token condition, or establish that another local, topological, boundary,
preparation, or multiscale construction cannot remove that supply.
`w1_closed: false`.

## Supplied / derived / open

### Supplied

- the Cycle-719 controller inventory: one source token, oriented ring
  geometry, program content and order, and clean data/controller genesis;
- the Cycle-723 zero `B`, `work`, and syndrome rows and two clean MCX scratch
  bits per station;
- four new clean OR-cascade intermediate bits per station; and
- the global one-token existence and uniqueness condition.

### Derived

- the six-input radius-one refusal guard around every nonidentity controlled
  data macro, with exact OR uncomputation;
- unchanged lawful behavior in the held and padded cases, forward and inverse;
- exact adjacent-collision refusal against an independent
  identity-substituted prediction;
- a target-row-complete 546-case padded census with literal syndrome and local
  identity witnesses;
- the finite `(0, 65)` two-token example that passes this particular guard;
  and
- active deletion controls plus the re-certified structural physical,
  covariance, compiled-orbit, and inherited-anchor surfaces.

### Open

- global one-token existence and uniqueness remain supplied because this
  construction does not derive them, not because their derivation by every
  other route has been ruled out;
- the
  [local-Gauss/BKSF route](work_history/repo/review_feedback/CYCLE703_LOCAL_GAUSS_REFERENCE_ADVERSARIAL_NOTE_2026-07-25.md),
  including its controller mode-graph mapping and physical preparation, is
  not assessed here and remains a live alternative;
- autonomous register preparation/genesis and every inherited Cycle-719 open
  item at its original scope; and
- occurrence, physical time, permanent Record, Born weighting, and
  source/gravity meaning.

## No-go discipline gate

Gate disposition: **PASS after narrowing**. The original universal
bounded-radius wording failed the negative-claim stress test and was removed.
Only the positive finite guard result above ships.

- **N1 — alternative routes:** at least five distinct routes remain live and
  untested here: a local-Gauss/topological charge sector; a supplied boundary
  marker with local propagation; a preparation or admission dynamics that
  selects one token; a hierarchical or multiscale constraint; and a carried
  counter/accumulator compiled into the controller program. Their existence
  blocks a universal route-impossibility conclusion.
- **N2 — wall independence:** this note uses one explicit global one-token
  supply and does not inflate it into multiple independent walls.
- **N3 — hidden conditions:** a universal locality theorem would require
  additional hypotheses about a uniform fixed-radius predicate, arbitrary
  ring size, boundary conditions, and admissible auxiliary state. None is
  silently assumed; that theorem is not claimed.
- **N4 — residual matching:** no prior no-go is used as a witness against the
  global one-token residual. Cycle 703 is cited only as a live alternative.
- **N5 — rhetoric resolution:** the tests cover literal station blocks and
  the complete declared program at radius one, with finite boundary examples
  at 11 stations in the independent checker and 130 stations in the primary
  runner. They do not cover all radii, all local encodings, or a
  lattice-wide impossibility.
- **N6 — partial-closure paths:** the Cycle-703 local-Gauss route, explicit
  boundary conventions, and preparation/admission dynamics are not excluded
  and need not be classified as new axioms.
- **N7 — steelman:** a locally checked topological charge sector or a
  physical preparation mechanism could select a unique controller
  excitation while preserving the present reversible refusal word. This
  package tests neither terminal obligation, so it cannot foreclose them.
- **N8 — cross-cycle echo:** the Cycle-719 source note records several nearby
  supplied interfaces retired by later bounded mechanisms and explicitly
  rejects impossibility or axiom-pressure promotion. The same history
  requires the present boundary to remain construction-specific.

## Verdict and next experiment

The six named dirty inputs now guard every nonidentity controlled data macro
on the declared controller programs, reversibly and with the supplied lawful
behavior unchanged. W1 remains open because the global one-token condition is
still an input. The finite distant-token witness explains only why this
radius-one guard does not close W1.

The next constructive legs are the live local-Gauss/BKSF mapping, a
preparation/admission route for the token sector, the source-lift tournament
definition recorded in the campaign handoff, and the public
factorization-object API for the restriction compiler. Renewal,
boundary-free geometry, and genesis remain open as inherited.
