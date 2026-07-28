# Cycle 724: local token-row enforcement at radius one, and the exact local/global split of W1

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

Cycle 723 wrapped every controlled macro of the two-rail controller in a
reversible dirty-rail refusal. Cycle 724 extends that sandwich to a **local
token row at radius one** and, in the same package, exhibits exactly where
bounded local enforcement ends:

- per station, the refusal syndrome becomes the reversible OR of
  `B_s`, `work_s`, and the four radius-one neighbor occupancies
  `A_(s-1), B_(s-1), A_(s+1), B_(s+1)` (an OR-cascade into fresh clean
  scratch, uncomputed exactly; all rail bits are invariant inside Q, so
  the sandwich remains an exact inverse pair). The extended `H` word has
  98,034 gates (against 95,850 wrapped, 61,562 unwrapped);
- **lawful behavior is unchanged**: on the lawful one-token trajectory no
  radius-one neighbor bit is ever set at Q-time (verified as its own
  sub-check), so held 2/5/12 and padded 130-station orbits, inverses,
  rail returns, and the Cycle-723 regression anchor (gate count and
  digest reproduced) all hold;
- **adjacent collisions are now refused locally**: the adjacent two-token
  sector (positions `(0,1)`) has both stations' macros suppressed on the
  collision steps, with the output equal to an independent
  identity-substituted prediction and all dirt visible at return;
- the exhaustive radius-one census — every nonidentity station, each
  neighbor dirt bit plus the `B_s`/`work_s` regression cases, 546 cases —
  shows zero prediction, survival, auxiliary-return, or refusal-event
  mismatches;
- **the local/global split is exhibited, not hidden**: the distant
  two-token sector (positions `(0, P//2)`) passes every local row and
  reproduces the unwrapped hostile prediction exactly. A bounded local
  check on an arbitrarily long ring cannot infer `sum(A+B) = 1`: distant
  multi-token sectors are locally invisible, and "at least one token"
  is equally global. This certificate PASSES by demonstrating the
  limitation;
- deletion controls (OR-cascade gate; uncompute gate) are active; the
  extended physical layer, 24 frames, 576 products, translations, the
  compiled extended orbit on all six Cycle-713 branches, and the
  inherited pin/residual anchors all re-certify.

## The claim, at its exact resolution

The Cycle-719 steelman's terminal test — "combine a locally checked
charge/token row with that refusal around every actual controller macro" —
is now executed **at its locally executable resolution**: dirty rails
(Cycle 723) and radius-one occupancy collisions (this cycle) are refused
at every macro, reversibly, with lawful behavior byte-equivalent at the
certificate surface. What remains is exactly the global remainder: the
one-token sector's global existence and uniqueness are not locally
derivable on the ring and stay **supplied**. A Gauss-style charge row in
the Cycle-703 BKSF sense would require a new supplied mode-graph mapping
for the controller M2s and is not attempted. `w1_closed: false`.

## Supplied / derived / open

### Supplied

- the Cycle-719 controller inventory unchanged (one global token at
  source, ring geometry, program content/order, clean data genesis);
- the Cycle-723 clean syndrome/scratch genesis, extended by the
  OR-cascade scratch bits of this cycle;
- the global one-token condition itself (existence and uniqueness beyond
  radius one).

### Derived

- the radius-one local token row folded into the total refusal wrap, with
  lawful behavior unchanged (held and padded, forward and inverse) and
  the Cycle-723 anchor reproduced;
- local refusal of adjacent-collision sectors with independent
  identity-substituted predictions (546-case census, zero mismatches);
- the exhibited local-resolution boundary: distant second tokens pass
  every local row and match the unwrapped hostile prediction;
- active deletion controls; re-certified physical layer, covariance
  surfaces, compiled orbit, and inherited anchors.

### Open

- global one-token existence/uniqueness (supplied; a local exact-one ring
  counter does not exist at bounded radius — this cycle's boundary
  certificate is the witness);
- the Gauss/BKSF charge-row route (requires new supplied mode-graph
  data);
- autonomous preparation/genesis of any register, and every inherited
  Cycle-719 open item (`W2`-`W7`) at its original scope;
- occurrence, physical time, permanent Record, Born weighting, and
  source/gravity meaning.

## Negative-claim discipline

No new negative claim ships. The statement that a bounded local check
cannot infer the global token count is exhibited constructively (the
distant-token sector passes and matches its prediction) and scoped to
bounded-radius checks on the ring; it is a resolution boundary of this
package's construction, recorded with its witness, not a route
impossibility theorem. Everything else restates supplied conventions or
inherited open items at their original scopes.

## Verdict and next experiment

W1's enforcement content is now split exactly: everything locally
checkable at radius one is enforced at every macro (dirty rails, adjacent
collisions), reversibly and with lawful behavior unchanged; everything
beyond radius one about the token sector is global and remains supplied,
with the boundary witnessed in-package. The next constructive legs, in
queue order: the Gauss/BKSF charge-row mapping as an explicitly supplied
mode-graph convention (which would move the global remainder into a
declared local-charge surface); the source-lift tournament definition
recorded in the campaign handoff; and the public factorization-object API
for the `V_s`-restriction compiler. Renewal, boundary-free geometry, and
genesis remain open exactly as inherited.
