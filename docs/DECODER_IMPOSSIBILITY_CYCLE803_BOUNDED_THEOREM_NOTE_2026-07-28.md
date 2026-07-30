# The missing decoder does not exist — the W7 scope wall is an impossibility with exact shape — Cycle 803

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the decoder derivation attempt; the
obstruction sharpened to a theorem-shaped impossibility at landed scope)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle803_decoder_derivation_2026_07_28.py`](../scripts/frontier_cycle803_decoder_derivation_2026_07_28.py)
- [`frontier_cycle803_decoder_independent_check_2026_07_28.py`](../scripts/frontier_cycle803_decoder_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 786 named the W7 scope wall as one missing callable —
`decode_companion_choi_to_linkstate(...) -> U320.LinkState`. This cycle
attempted the derivation and the honest outcome is **OBSTRUCTED_DEEPER**:
the decoder **cannot exist as specified**, and the obstruction is now
exact:

- **the prepared object is mixed, not pure**: the Cycle-720 Choi
  tableau has stabilizer rank 11 of 15 on the relevant sector — the
  induced link-sector object is a mixed state of rank 16. There is no
  pure `LinkState` to decode to; the target type is unreachable from
  the resource;
- **the calibration is not well-defined**: the identity the decoder
  must satisfy forces the same prepared resource to decode to two
  distinct required outputs (the e0 and e1 calibration rows; squared
  distance 2). This is a structural contradiction, not a numerical
  miss — certificates B and C fail BY DESIGN as the honest encoding of
  the obstruction (the receipt records these two designed FAIL lines
  explicitly — they are the finding, not a defect);
- **cross-terms were correctly not reached** under the frozen
  calibration-stop rule (a decoder that fails calibration has no
  composite claim to test);
- **the checker confirmed everything and closed the escape route**:
  two independent exact GF(2) methods re-derive rank 11/15 (density
  rank 16, purity 1/16); the e0/e1 witness re-verified with the
  Cycle-720/U320/S322 indexing identification audited (no strawman);
  and the purifiable-subfamily hunt over the complete bounded
  enumerated 720 preparation family found **pure members: 0 of
  3,744** — no 720-preparable object induces a pure link-sector
  state; decoder, calibration, and cross-term stages correctly never
  run. Checker status:
  `CONFIRMED_OBSTRUCTION_ON_BOUNDED_ENUMERATED_720_FAMILY` (105 s).

**What this does to W7**: the scope wall stops being a to-do and
becomes a shape. Extending the response law through the 720 route
requires exactly one of two named supplies — a **purification choice**
(physical content: which purification of the rank-16 object is the
state) or a **mixed-input response surface** (extending U320 beyond
pure amplitudes). Neither is landed; both are now named with the
theorem that forces the choice.

## Supplied / derived / open

### Supplied

- the decoder signature and calibration identity (786); the 720
  preparation; everything the Cycle-719/720/749/720-family packages
  declare.

### Derived

- the 11/15 rank computation; the mixed-rank-16 conclusion; the
  e0/e1 ill-definedness witness; the calibration-stop discipline.

### Open

- the two named supplies (purification choice; mixed-input response
  surface); the response law on other landed surfaces. The
  purifiable-subfamily question is CLOSED negative at the bounded
  enumerated family (0/3,744).

## Negative-claim discipline

The impossibility is scoped to the landed 720 preparation and the 786
decoder signature into pure `LinkState`; it does not foreclose the two
named supply routes, and it makes no claim about unlanded preparations.

## Verdict

Asked to build the named missing decoder, the derivation returned
something better than a failure: a proof of why no such function
exists — the resource is mixed and the calibration contradicts itself.
A wall with exact shape is a wall you can plan against. Independent
audit still required.
