# The anchors close unconditionally through b = 10 — the hypothesis discharged on the real objects — Cycle 823

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the fixed-b discharge of the general-b
theorem's hypothesis, corrected onto the actual constructor objects)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle823_hypothesis_discharge_2026_07_28.py`](../scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py)
- [`frontier_cycle823_discharge_independent_check_2026_07_28.py`](../scripts/frontier_cycle823_discharge_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 817 left the general-b sector theorem conditional on one
hypothesis — H_TEMPLATE_PREIMAGE_ZONE_CLASS — discharged at no b. This
cycle discharged it, with the adversarial exchange enforcing the
standard on the way:

- **the hypothesis is finitely decidable at fixed b** — no surrogate
  needed;
- **the first assembly took a shortcut and was caught**: v1 ran the
  check on an embedded-table surrogate (with a hard-coded offset)
  never mechanically equated with 817's actual constructor objects;
  the checker REFUTED the discharge on exactly that gap;
- **v2 runs on the real thing**: the decidable check evaluated
  DIRECTLY on Cycle-817's actual constructor objects — **PASS at
  every b = 3..10**, so the sector theorem is UNCONDITIONAL at each
  of those b (subject to its other, already-verified conditions);
  the b = 11 pattern also passes; NO general-b claim is made;
- **the checker's re-pointed fidelity attack confirms**: independent
  AST extraction and element-wise comparison of the objects the v2
  actually checks against 817's constructors — equal at every
  b = 3..11; the perturbed negative control still correctly rejected;
  6/6;
- the v1 surrogate computations are retained as labeled diagnostics.

**What this does to the anchors lane**: the wall that Cycle 817
narrowed to one hypothesis is now DOWN at b = 3 through 10 — the
sector theorem holds unconditionally there by derivation, not
exhaustion (the six exhaustive rings become independent confirmations
at their b). The remaining open is the hypothesis at general b, with
the b = 11 pattern as the standing candidate.

## Supplied / derived / open

### Supplied

- the 817 conditional theorem and its constructor objects; everything
  the 737/738/740/817 packages declare.

### Derived

- the fixed-b decidability; the per-b discharges on the actual
  objects; the fidelity comparison; the retraction record.

### Open

- H_TEMPLATE_PREIMAGE_ZONE_CLASS at general b (the b = 11 pattern
  pending its own general verification); b >= 12.

## Negative-claim discipline

Discharges are per-b facts on the actual objects; no general-b claim;
the v1 surrogate is diagnostic only.

## Verdict

The lane that was one hypothesis wide is now, through ring ten, zero
hypotheses wide — and the first attempt's shortcut was caught by the
same discipline that caught sixteen before it. Independent audit
still required.
