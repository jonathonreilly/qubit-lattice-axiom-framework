# Promotion Value Gate — Cycle 707b (erratum)

## V1 — the claim, one sentence

Probe P4 names the rival to valley-linear as `S = L√(1-φ)` and pairs it with
`F~M = 0.50`, but that expression is weak-field **linear** (power 1); the
action actually measured is `L(1-√f)` (power 1/2), so the printed formula
belongs to the class it is offered as the alternative to.

## V2 — new at the searched commit `922b9b12a6`?

Yes. Searched `"three condition values"`, `"spent-delay"`, `"valley-linear"`,
`"mass.law exponent"`, `"F ~ M"`. No landed note records the discrepancy. The
sources involved (`ACTION_UNIQUENESS_NOTE`, `ACTION_CROSSOVER_NOTE`,
`action_universality_probe.py`) are each internally consistent; only P4's
transcription is not.

## V3 — load-bearing?

Modestly, but on a real surface. B(c) is a named admission on a lane whose
parent row is `criticality: critical` with 773 transitive descendants and
`deps: []`. Anyone attacking B(c) from P4's text would try to discriminate two
members of the same universality class — an undecidable comparison, because
there is nothing to decide. The erratum redirects that effort at the sublinear
class, which is the genuine alternative.

## V4 — cost

None. No axiom, no primitive, no import, no convention. No measured number,
log, cached artifact or verdict changes.

## V5 — thin?

**It is small, and it is labelled an erratum rather than a theorem.** The
defence is that it is a correction, not a contribution to theory: it is exact,
confirmed independently two ways (the runner, and the probe's own
`action_value()` source), and was verified by an adversarial reviewer that
rejected the surrounding cycle — the reviewer's words: *"P4 really pairs
`S=L√(1−φ)` with `0.50`, while ACTION_UNIQUENESS tests `L(1−√f)`; these are
distinct … Thus P4 misstated the formula, not the intended universality class."*

The theorem-shaped content that accompanied it (a perturbative mechanism for
the exponent) was rejected for overreach and is **deliberately not reissued**;
it is recorded in `PR_BACKLOG_707.md`. What remains is exactly the part that
survived attack.

**Risk I would flag myself:** an erratum on a support note is low-value per
unit reviewer attention, and a reviewer may reasonably prefer it be folded into
a future B(c) derivation rather than landed alone. I judge it worth landing
separately because it is small, self-contained, and actively misleading if left
in place.

## Verdict

Proceed. 4 PASS / 0 FAIL, cold-run at `6a39ef9991`, PIN MATCH `14090a58…`.
