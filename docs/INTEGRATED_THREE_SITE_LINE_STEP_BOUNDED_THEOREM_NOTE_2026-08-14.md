---
claim_id: integrated_three_site_line_step_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On a displayed 3-site line, one update uses a lock-occupancy snapshot: every unread site with n≠0 forms and locks the sign of n_x; locked sites stay. Source and tick are the cumulative formation count, not extra tables. A displayed seed lock at the left site makes the center form on step 1 and the right site form on step 2 because the center occupancy has changed. Step 3 is the identity. This is one coupled Record/source/clock comparator on a line, not a TOE, not Newton, not pairing-on-a-readout, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/integrated_three_site_line_step_2026_08_14.py
---

# One Integrated Step On A Three-Site Line

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `Q` update of locks on a displayed 3-site line.
Not a unique member. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/integrated_three_site_line_step_2026_08_14.py`](../scripts/integrated_three_site_line_step_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Sites `L, C, R` sit on a line. Occupancy of a site is `1` iff it
carries a lock. At an unread site the directed kernel is
`n_x = (o_right − o_left)/3`. The **one** update is:

- locked sites stay;
- an unread site with `n_x ≠ 0` forms and locks the sign of `n_x`;
- source and tick equal the number of locks that were created by
  the update (seed locks do not count).

A displayed seed locks `L`. Step 1: only `C` sees `o_L=1`,
`n_x=−1/3`, `C` locks `−`. Step 2: `R` now sees `o_C=1`, forms.
Step 3: all three locked, identity. Source/tick go `0 → 1 → 2 → 2`.

Clock `a` and pairing `B` are not tables in this law. This is still
a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact occupancy-to-lock update on a 3-site line couples formation, source, and tick. No axiom text."
trace_class: frontier_discovery
target_claim_id: integrated_three_site_line_step
target_blocker_text: "disconnected L0 tables; need one Record/source/clock update"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit; recoil beyond this line remains open"
conditional_surface_status: "exact for the displayed 3-site line comparator"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name this update.

## Theorem 1 — seed only

`locks = (−, ·, ·)`. Source `0`. Tick `0`. `C` has `n_x = −1/3`.
`R` has `n_x = 0` (both neighbors unread).

## Theorem 2 — step 1 forms `C` only

After one update: `(−, −, ·)`. Formations this step: `1`.
Cumulative source/tick: `1`.

## Theorem 3 — step 2 forms `R` because `C` is now occupied

After two updates: `(−, −, −)`. Formations this step: `1`.
Cumulative source/tick: `2`. This is recoil on the line: `C`’s
record changes `R`’s later menu.

## Theorem 4 — step 3 is permanence

Locks unchanged. Formations `0`. Source/tick stay `2`.

## Theorem 5 — one function, not three tables

`step(locks)` returns new locks. `source` and `tick` are the
same integer (cumulative formations). There is no separate `a=1`
or `B=xy` table in this law.

## Theorem 6 — not a TOE

Quoted Record and Admissibility do not name the line, the seed, or
the update. Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “step 2 does not form `R`” must fail.
2. Predicate “step 3 increments source” must fail.
3. Predicate “empty seed forms `C`” must fail.
4. Predicate “note adopts a gravity law” must fail.

Identity gates: `occupancy(locks)`, `nx(site, locks)`, `step(locks)`,
`formed(before, after)`.

## Honest-auditor / Boundary

Three sites, four snapshots, exact `Q`. Not Newton. Not pairing on
a readout. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Born derivation.
- No `1/r^2`. No QCD.
- Qubit remains `M_2(C)`.
