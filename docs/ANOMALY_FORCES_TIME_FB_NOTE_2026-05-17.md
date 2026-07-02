# Anomaly-Forces-Time F-B framing fix

**Date:** 2026-05-17

**Claim type:** meta
**Authority role:** audit-prep framing-honesty fix; not a new science claim.
Records the addition of an explicit "what's derived vs what's inherited"
Remark to Step 4 of `docs/ANOMALY_FORCES_TIME_THEOREM.md`, addressing the
mis-framing flagged by hostile audit finding F-B in
[PR #1262](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1262).

**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_anomaly_forces_time_fb_framing_fix.py`](../scripts/frontier_anomaly_forces_time_fb_framing_fix.py)
**Cached output:** [`logs/runner-cache/frontier_anomaly_forces_time_fb_framing_fix.txt`](../logs/runner-cache/frontier_anomaly_forces_time_fb_framing_fix.txt)

## The framing issue

The parent theorem is titled "Anomaly Cancellation Forces 3+1 Spacetime"
and its conclusion states `d_t = 1`. The F-B hostile finding observed
that the proof chain S1-S10 forces only `d_s + d_t = even` from ABJ +
chirality; the "exactly `d_t = 1`" outcome is inherited from admission
(iv)'s single-clock evolution theorem, not derived purely from ABJ.

Specifically:
- Step 3 (chirality + `d_s = 3`) gives `d_t in {1, 3, 5, ...}` — odd
  positives only
- Step 4 (admission iv) excludes `d_t > 1` because the single-clock
  evolution theorem fixes a single generator of a one-parameter unitary
  group
- The conjunction gives `d_t = 1`

The mis-framing concern: admission (iv)'s single-clock theorem
presupposes a Lorentzian real-time structure `U(t) = exp(-itH)` with
real `t`. That presupposition already encodes "Lorentzian (rather than
Euclidean or ultrahyperbolic)" signature character. Step 4's argument
is correct within that presupposition; the presupposition itself is
inherited, not derived from ABJ.

## The fix

A new Remark in Step 4 (`docs/ANOMALY_FORCES_TIME_THEOREM.md`)
explicitly decomposes which dimensional content comes from which step:

  - **Derived from Step 3 (ABJ + chirality):** `d_s + d_t` even;
    combined with `d_s = 3`, forces `d_t in {odd positives}`. Step 3
    alone does **not** select `d_t = 1`.

  - **Inherited from admission (iv):** real-time Lorentzian
    one-parameter unitary `U(t) = exp(-itH)` with single codimension-1
    initial surface. Within that structure, `d_t > 1` is excluded by
    uniqueness of the generator.

  - **Net effect:** `d_t = 1` follows by conjunction. Neither step
    alone is sufficient.

The Remark also notes that admission (iv)'s real-time Lorentzian
presupposition is itself derived in the single-clock theorem from
retained primitives (RP positivity, microcausality, Lieb-Robinson,
cluster decomposition, the physical Cl(3) local algebra, and the Z^3
spatial substrate). The chain is not circular — but
the inheritance must be visible at the Step-4 boundary, not hidden.

## Effect on theorem status

**Unchanged.** The bounded_theorem submission status, the load-bearing
class B, and the conditioning on independent audit ratification all
remain unchanged. This is an honesty-of-framing fix, not a science
change.

## Current mainline reconciliation (2026-06-18)

The parent theorem has since sharpened the Step-4 boundary from a direct
single-clock-note dependency to the local declared `B-AXIS` premise:
one supplied blocked time step, one declared evolution axis/transfer
construction, and no admitted independent commuting transfer factor as
a second clock. This supersedes the original prose form of the F-B
remark while preserving the audit-relevant repair:

- Step 3 supplies only the computed lower bound: `d_t` is odd, so
  `d_t >= 1`.
- Step 4 supplies only the declared upper bound: conditional on
  `B-AXIS`, `d_t <= 1`.
- The conjunction gives `d_t = 1`; neither the anomaly computation nor
  `B-AXIS` alone derives the full result.
- The single-clock note is provenance context for the boundary wording,
  not a markdown dependency edge of the parent row.

The runner now verifies this current-source reconciliation rather than
the superseded exact wording of the original Step-4 remark.

## What this PR does NOT change

- The proof chain (same five steps; same conclusion)
- The bounded_theorem status (still B-class conditional bridge)
- Admission (i) (ABJ-to-inconsistency) — still a bare external admission
- Admission (iv)'s review posture — still an audit-pending source note;
  not weakened by being labeled "inherited at Step 4"
- The theorem title — kept as-is. The shorthand "Anomaly forces 3+1"
  is accurate for the compound derivation; the new Remark explains
  what the shorthand compresses

## Verification

`scripts/frontier_anomaly_forces_time_fb_framing_fix.py` checks:

- This meta note declares its primary runner and cached output
- The current parent theorem separates the Step-3 lower bound from the
  Step-4 `B-AXIS` upper bound
- The parent theorem states that it does not derive `B-AXIS`
- The single-clock source note is context only, not a load-bearing
  markdown dependency edge of the parent row
- The proof structure (5 steps, conclusion `d_t = 1`) is unchanged

## Cross-references (non-load-bearing)

- `docs/ANOMALY_FORCES_TIME_THEOREM.md` (parent, modified)
- `docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md` (admission iv's source)
- [PR #1262](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1262) (original F-A/F-B/F-C/F-E hostile audit findings)
- [PR #1500](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1500) (companion F-C citation correction)
