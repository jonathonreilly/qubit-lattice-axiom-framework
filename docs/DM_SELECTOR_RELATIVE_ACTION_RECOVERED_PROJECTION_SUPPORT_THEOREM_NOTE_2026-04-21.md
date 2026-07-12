# DM Selector Relative-Action / Recovered Projection Support Theorem

**Date:** 2026-04-21  
**Status:** bounded projection support for a supplied candidate on the open DM gate
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_dm_selector_relative_action_recovered_projection_support_2026_04_21.py`

## Statement

The supplied observable-relative-action candidate and the recovered
right-sensitive threshold candidate remain distinct constructions.
However, they are no longer disconnected on the current branch science.

There is a reproducible recovered projection packet of the conditional
candidate:

- the relative-action source is uniquely nearest to the preferred recovered
  lift in Frobenius distance on `H`,
- uniquely nearest in Euclidean distance on the active target `(delta, q_+)`,
- uniquely nearest in threshold-profile distance on the exact witness-volume
  family at the checked anchor positive window,
- and uniquely nearest across all checked common positive windows in each of:
  - affine-invariant Riemannian distance on `A_mu(H)`,
  - forward LogDet divergence `D(A_rel || A_i)`,
  - reverse LogDet divergence `D(A_i || A_rel)`,
  - inverse-eigenvalue parameter distance.

The same preferred recovered lift is the unique point returned by the
intrinsic threshold breakpoint candidate

```text
tau_b,min = min_i log(1 + b_i).
```

So the remaining selector burden narrows again. The live positive target is no
longer to discover some disconnected recovered-bank object. It is to justify
the projection principle from the supplied conditional candidate to that preferred
recovered lift, or else to replace both current selector objects by a finer
microscopic law.

## Prior branch state

Two same-day support theorems had already sharpened the selector lane:

1. `docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md`
   identified the canonical recovered-bank breakpoint candidate
   `tau_b,min`, which belongs uniquely to the preferred recovered lift and
   already selects it on the exact threshold-volume family.
2. `docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md`
   showed that the supplied observable-relative-action candidate on the fixed
   `N_e` seed parameterization does not land on the recovered branch and
   instead carries a later breakpoint `tau_b,rel`.

That left two conditional candidate constructions with no physical bridge.

## New support theorem

### 1. Shift-independent nearest recovered point

Let `H_rel` be the conditional relative-action source and let
`{H_i}` be the recovered bank.

Then:

- the unique nearest recovered point to `H_rel` in Frobenius norm is lift `0`,
- the unique nearest recovered active target to
  `T_rel = (delta_rel, q_+,rel)` in Euclidean norm is also lift `0`,
- and at the checked anchor positive window the threshold-profile
  distance

```text
||V_tau(H_rel) - V_tau(H_i)||_{L^2([0, tau_max])}
```

is minimized uniquely by lift `0`.

So even before invoking any SPD geometry, the supplied candidate points
canonically to one recovered-bank image.

### 2. Common-positive-window geometry agrees

For every checked common positive shift

```text
mu = max repair + offset,
offset in SHIFT_OFFSETS,
```

set `A_mu(H) = H + mu I`.

Then the unique nearest recovered point to `A_mu(H_rel)` is again lift `0`
under each of:

- affine-invariant Riemannian distance,
- forward LogDet divergence,
- reverse LogDet divergence,
- inverse-eigenvalue parameter distance.

So the preferred recovered neighbor is stable across the checked common
positive windows and across a nontrivial intrinsic metric family.

### 3. Agreement with the recovered threshold candidate

The same preferred recovered lift `0` is already selected by the exact
recovered-bank breakpoint candidate `tau_b,min`.

Therefore the branch now has:

- one supplied relative-action candidate,
- one recovered-bank threshold candidate,
- and one canonical recovered projection packet identifying the same
  preferred recovered lift.

## Consequence

This does **not** close the DM selector law.

It does sharpen the remaining microscopic burden again.

Before this note, the live selector statement was:

- derive and bridge the supplied relative-action candidate to the recovered right-sensitive
  selector branch, or replace both by a finer microscopic law.

After this note, the sharper positive target is:

- justify why a physical selector uses the recovered projection of
  the supplied candidate onto the preferred recovered lift
  singled out by `tau_b,min`, or
- derive a finer microscopic law that supersedes both current selector
  objects.

So the remaining bridge is no longer a generic matching problem. It is a
projection-principle problem.

## Boundary

This is a support theorem, not closure.

It does **not** prove that any one checked metric is itself the physical
selector law, and it does **not** derive the projection principle from bare
axioms.

It proves only that the supplied conditional calculation and recovered branch
are metrically related: the same preferred
recovered lift is consistently nearest across the checked projection packet.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_selector_relative_action_recovered_projection_support_2026_04_21.py
```

Expected:

```text
SUMMARY: PASS=12 FAIL=0
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21](DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md)
- [dm_selector_relative_action_recovered_branch_separation_support_theorem_note_2026-04-21](DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- [scalar_selector_remaining_open_imports_2026-04-20](SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md)
