# The silence is not a conservation law — three invariants proven, none rules — Cycle 813

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the k >= 4 silence attacked at the
conserved-invariant level; the level exhausted and ruled out)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle813_silence_theorem_2026_07_28.py`](../scripts/frontier_cycle813_silence_theorem_2026_07_28.py)
- [`frontier_cycle813_silence_independent_check_2026_07_28.py`](../scripts/frontier_cycle813_silence_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The multi-source family's sharpest unexplained datum: k = 2 and k = 3
produce six transients; k = 4 (20 keys) and k = 5 (4 keys) are silent
through T = 8192. This cycle asked whether the silence is STRUCTURAL —
a conserved quantity forbidding cleanliness outright — and the answer
is a clean no, at a precisely drawn level:

- **three invariants proven**: UNWRITTEN_LINK_VECTOR_ZERO,
  UNWRITTEN_LINK_OCCUPANCY_ZERO, UNWRITTEN_LINK_PARITY_EVEN — each
  machine-proven evolution-invariant and machine-proven NECESSARY for
  a clean postimage at general k;
- **identity controls 6/6**: all six known transient moments satisfy
  all three (a necessary condition failing at a known clean moment
  would have refuted the derivation);
- **the census: 0 of 24 silent keys are excluded** — every silent
  key's conserved values are COMPATIBLE with cleanliness; the
  invariants do not explain the silence;
- **the checker exhausted the level** (4.9 s, all certificates PASS):
  invariance re-verified with zero drift across 24 keys, both strata,
  48 boundary crossings; necessity re-verified by constructing
  violating near-clean configurations and confirming the landed test
  rejects each; the compatibility census recounted 24/24; and the
  missed-invariant hunt EXHAUSTED the full linear invariant class and
  the 533,409-monomial degree <= 2 GF(2) class — **no conserved
  linear or quadratic invariant rules out any silent key**.

**Verdict: `SILENCE_UNEXPLAINED_AT_THIS_LEVEL`** — and the level is
now exact: whatever explains the k >= 4 silence is not a conservation
law of linear or quadratic type. The explanation lives in
time-dependent structure or deeper horizons; the three proven
invariants are new landed structure for whatever comes next.

## Supplied / derived / open

### Supplied

- the landed cleanliness test and evolution (reimplemented from the
  Cycle-719/736/758/790/791/792/794/798 lineage); everything those
  packages declare.

### Derived

- the three invariance proofs and necessity implications; the 6/6
  identity controls; the 24-key compatibility census; the checker's
  class exhaustions.

### Open

- the silence's actual mechanism (not a linear/quadratic conservation
  law — the sharpest negative available at this level); the 38 open
  higher-k keys at deeper horizons; the 162 open k <= 3 keys.

## Negative-claim discipline

The exclusion of the conserved-invariant explanation is scoped to the
linear and degree <= 2 GF(2) classes over the declared state basis;
the silence itself remains scoped to T <= 8192; no claim attaches to
higher-degree or non-conserved structures.

## Verdict

Asked whether the silence is a conservation law, the framework
answered no three times over — three real invariants, none of which
rules — and the checker closed the entire level behind it. A question
that survives a complete level of attack is sharper, not safer.
Independent audit still required.
