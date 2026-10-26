# Supplied-bank first-middle-breakpoint diagnostic

**Date:** 2026-04-21
**Type:** open_gate
**Status:** conditional finite numerical support; physical threshold selection open
**Primary runner:** `scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py`

## Premises and finite argument

Take the five recovered-bank entries, common positive shift and inverse-eigenvalue triples `(a_i,b_i,g_i)` supplied by the [atomic witness-volume note](DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md) and its helper. Their provenance and applicability are premises, not derived by this diagnostic. The word preferred labels supplied lift 0; the runner evaluates all five entries before taking an argmin.

Define `tau_b(i)=log(1+b_i)`. Conditional on `b_i>-1`, this function is strictly increasing. Thus a strictly smallest `b_0` gives the uniquely earliest middle breakpoint at lift 0. The runner compares all five supplied floating values, retaining its original `1e-12` margins and all numerical predicates. Numerical margins are observations on these fixtures, not exact certified enclosures.

For the supplied piecewise field with `c=exp(tau)-1`,

```text
V = 1                              when c <= g
V = 1-(c-g)^2/((a-g)(b-g))          when g < c <= b
V = (a-c)^2/((a-b)(a-g))            when b < c < a
V = 0                              when c >= a
```

if `c=b_0`, lift 0 has `V=(a_0-b_0)/(a_0-g_0)`. For a competitor satisfying `g_j<b_0<b_j`, its value is `1-(b_0-g_j)^2/((a_j-g_j)(b_j-g_j))`. These are conditional algebraic substitutions. The runner directly evaluates the supplied field at the computed breakpoint and checks a strict finite-bank margin; it does not prove universal branch hypotheses or exact signs from floating arithmetic.

## Supplied endpoints and withdrawn authority

The runner also retains its comparison of this breakpoint to the supplied number `tau_star=0.1316375782215522` and the next computed zero-volume endpoint. The [threshold diagnostic](DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md) reports finite numerical checks. Its old exact-onset/whole-window certificate attribution is withdrawn. The inequalities between these supplied endpoint values do not prove that lift 0 minimizes throughout the interval.

The historical stronger note, runner and cache are preserved in the immutable predecessor commit `186ae14000eef214a6e7a1c66ec27bcc5eaacd84`; external repair evidence retains the same complete bytes. No historical PASS count is current proof authority. Current canonical cache records the actual finite run, including any failures.

## Open obligations

A rigorous whole-window inequality/enclosure proof, derivation of the physical threshold law and provenance of the supplied bank remain open. This breakpoint is a named candidate within a stipulated family; no uniqueness across physical selector mechanisms or exhaustive narrowing of the research burden is claimed. Documentary substring checks report only what the parent text says. Former literal-True canonicality/burden narration is unscored.

## Reproduction

Run `PYTHONPATH=scripts python3 scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py`. The declared 300-second limit is an execution bound, not evidence for any independent helper run.
