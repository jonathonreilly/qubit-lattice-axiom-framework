# Anomaly-Forces-Time F-B framing fix

**Date:** 2026-05-17

**Claim type:** meta
**Status:** audit-prep framing-honesty fix; not a new science claim. Records the
addition of an explicit "what's derived vs what's inherited" Remark to
Step 4 of `docs/ANOMALY_FORCES_TIME_THEOREM.md`, addressing the
mis-framing flagged by hostile audit finding F-B in [PR #1262](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1262).

**Status authority:** independent audit lane only.

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
cluster decomposition, Cl(3)/Z^3). The chain is not circular — but
the inheritance must be visible at the Step-4 boundary, not hidden.

## Effect on theorem status

**Unchanged.** The bounded_theorem submission status, the load-bearing
class B, and the conditioning on independent audit ratification all
remain unchanged. This is a honesty-of-framing fix, not a science
change.

## What this PR does NOT change

- The proof chain (same five steps; same conclusion)
- The bounded_theorem status (still B-class conditional bridge)
- Admission (i) (ABJ-to-inconsistency) — still a bare external admission
- Admission (iv)'s status — still proposed_retained (audit-pending);
  not weakened by being labeled "inherited at Step 4"
- The theorem title — kept as-is. The shorthand "Anomaly forces 3+1"
  is accurate for the compound derivation; the new Remark explains
  what the shorthand compresses

## Verification

`scripts/frontier_anomaly_forces_time_fb_framing_fix.py` checks:

- The Remark is present in `docs/ANOMALY_FORCES_TIME_THEOREM.md`
- The Remark explicitly names "derived from Step 3" and "inherited from
  admission (iv)"
- The proof structure (5 steps, conclusion `d_t = 1`) is unchanged

## Cross-references (non-load-bearing)

- `docs/ANOMALY_FORCES_TIME_THEOREM.md` (parent, modified)
- `docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md` (admission iv's source)
- [PR #1262](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1262) (original F-A/F-B/F-C/F-E hostile audit findings)
- [PR #1500](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1500) (companion F-C citation correction)
