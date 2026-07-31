# The meeting theorem, and the chain one link short — Cycle 839

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the per-separation meeting theorem; the
meet-configuration table; the reachability split; the causal chain's
named gap)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle839_meeting_derivation_2026_07_28.py`](../scripts/frontier_cycle839_meeting_derivation_2026_07_28.py)
- [`frontier_cycle839_meeting_independent_check_2026_07_28.py`](../scripts/frontier_cycle839_meeting_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The (3,3) tie was a correlate; this cycle derives the structure and
measures how far it reaches:

- **the meeting theorem** (rule-derived; checker re-derived
  independently): on 11 stations under radius-1 propagation the
  two-arc meeting times by separation are s=1:(1,5), s=2:(1,5),
  s=3:(2,4), s=4:(2,4), **s=5:(3,3)** — with the representative
  meeting centers printed; only s = 5 is symmetric;
- **the meet-configuration table**: the exact local configurations
  produced at the meets (s=1 falls outside the landed family;
  projected unique states s2 = 21/34, s3 = 25/33, s4 = 26/32,
  s5 = 21/21); **only s = 5 places both A tokens in the combined
  centers simultaneously** — B clean, no collision, no reflection
  symmetry;
- **the reachability split** (bounded, every microstep through tick
  162129 checked): from the meet-configurations, s = 2..4 reach the
  exact weight-44 funnel **0/44 each**; s = 5 reaches it **9/44 —
  exactly the nine backbone entrants** (checker re-ran s=4 and s=5 in
  full);
- **the verdict is PARTIAL, honestly**: correlation and reachability
  are exact; the causal tie-to-funnel mechanism — WHY the symmetric
  meet enables the funnel — is the one named missing link (the
  Cycle-840 hunt takes it up at the meet-configuration level).

## Supplied / derived / open

### Supplied

- the landed update rules and catalogs; everything the cited packages
  declare.

### Derived

- the per-s meeting theorem with rule chains; the meet-configuration
  table; the full reachability split; the token-placement uniqueness.

### Open

- the missing link (the meet-level discriminator — Cycle 840); the
  delayed station-0 meets; the pulse phase.

## Negative-claim discipline

The theorem and split are exact at their declared bounds; PARTIAL
means precisely that no causal claim is made beyond them.

## Verdict

Separation five is now the only distance at which the two wavefronts
arrive as equals — a theorem — and the only distance from which the
funnel is ever reached — a census. Between the two stands one
unexplained step, and it is the campaign's next target. Independent
audit still required.
