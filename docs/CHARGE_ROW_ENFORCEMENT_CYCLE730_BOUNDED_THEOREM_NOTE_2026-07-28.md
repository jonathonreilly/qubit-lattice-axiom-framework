# Charge-row enforcement integrated into the refusal sandwich — Cycle 730

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle730_charge_row_enforcement_2026_07_28.py`](../scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py)
- [`frontier_cycle730_enforcement_independent_check_2026_07_28.py`](../scripts/frontier_cycle730_enforcement_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 724 made the token rows enforcement (any refusal bit gates the
station macro off); Cycle 728 compressed the W1 obstruction census to one
marked-edge holonomy bit. This cycle joins them: the radius-one charge
rows `L_s = A_s XOR B_s XOR ref_s XOR ref_{s+1}` — with the marked-edge
twist `XOR h` at the declared station `s* = 0` — are computed reversibly
into the same OR-cascade that already carries the token rows, so a charge
violation now *refuses the macro* rather than merely being visible to an
external audit. On the landed two-bank and ring fixtures:

- **extended word 99,310 semantic gates** versus 98,034 for the Cycle-724
  sandwich (added 1,276 gates, ratio 1.013; word `sha256
  7d4b7fac…`); charge-row compute/uncompute is exact (zero uncompute
  failures), and the static reference chain and `h` register are
  provably never written by the enforced word;
- **lawful behavior unchanged**: the full charge-extended wrap
  reproduces the Cycle-724 lawful trajectories exactly (literal reverse
  exact; every auxiliary — B/work/syndrome/MCX/OR/charge scratch, refs,
  `h` — returns clean), and along the lawful trajectory every active
  charge row evaluates to zero at every station (11/35/130-station
  fixtures, zero failures);
- **exhaustive violation census, prediction = observation**: 183
  injected violations (182 single reference-bit flips + 1 `h` flip)
  produce 341 refusal events; per-station predicted and observed refusal
  sets agree with zero mismatches, and 183 literal compiled branches
  match the host simulation branch by branch;
- **enforcement theorem (the compression is now enforcement)**: on the
  ring-11 fixture, over all 8,388,608 rail/`h` cases, every charge row
  passes unmolested **iff** the token parity equals the supplied `h` —
  the marked-edge holonomy bit of Cycle 728 is now a physically enforced
  refusal law, not a bookkeeping identity;
- **honest residual, frozen**: a matched-parity multi-token witness
  (tokens at sites 0 and 5, `h = 0`, canonical references) passes every
  local row — the sandwich enforces the **parity sector**, not the token
  count. `w1_closed: false` stands;
- deletion controls (charge-compute gate, OR-cascade gate) are detected;
  the physical layer routes the 12-bank extension end to end
  (18,051,374 routed nearest-neighbor gates forward; 1,435,386 physical
  primitives each direction; controller M2 1,691 + charge-scratch M2 130
  + one `h` M2); the compiled extended orbit reruns the six Cycle-713
  branches (130 H applications, zero equality/inverse/return failures)
  and the Cycle-713 mass/contact anchors are byte-pinned unchanged.

## Supplied / derived / open

### Supplied

- the clean static reference chain, the `h` register and its genesis
  value, and auxiliary cleanliness (declared supplies, as in Cycles
  724/728);
- one source controller token; oriented program ring; clean data
  genesis; everything the Cycle-719 controller core itself declares.

### Derived

- the charge-extended sandwich word and its exact reversibility;
- lawful-trajectory charge-row nullity; the exhaustive refusal census
  with zero prediction mismatches;
- the ring-11 enforcement theorem (pass iff token parity equals `h`)
  over all rail/`h` cases;
- the matched-parity residual witness; deletion detection; the routed
  physical layer and unchanged inherited anchors.

### Open

- W1 itself: matched-parity multi-token states satisfy every local row;
  parity-sector enforcement does not count tokens. Closing W1 needs a
  genuinely nonlocal certificate or a new mechanism, not more local
  rows;
- everything the landed Cycle-713/719/724/728 surfaces leave open at
  their scopes; no time/Record/Born/source content is touched.

## Negative-claim discipline

No new negative claim ships. The matched-parity residual is a frozen
witness bounding the positive claim's scope, not a no-go.

## Verdict

The W1 ledger line advances from "witnessed, then compressed" to
"compressed, then enforced": the one marked-edge holonomy bit is now a
refusal law of the same physical M2 sandwich that enforces token rows,
with prediction-exact censuses and the parity-sector residual honestly
frozen. Independent audit still required.
