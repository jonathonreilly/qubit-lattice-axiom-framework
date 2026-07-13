# `y_t` Bridge Action Invariant Note

**Date:** 2026-04-15 (demoted 2026-05-16; obstruction link 2026-07-12)
**Claim type:** bounded_theorem
**Status:** bounded numerical-match scan (target-conditioned correlation across
selected profile families)
**Audit class:** G — load-bearing step is a target-conditioned numerical scan,
not a derivation
**Primary runner:** `scripts/frontier_yt_bridge_action_invariant.py`

## Scope

This note records a bounded target-conditioned numerical scan. It does not
derive the exact interacting bridge, the normalized gauge-surplus action
`I_2`, or the UV centroid from the framework axioms.

Given all of the following inputs:

1. the comparator `y_t(v)=0.9176`;
2. a chosen one-loop SM-like reference transport;
3. a chosen lattice-side UV bridge profile;
4. logistic, error-function, and smoothstep profile families on a fixed
   `(center_frac,width_frac)` grid; and
5. the target-based retention cut `|dev|<0.5%`;

the runner finds that the retained rows have endpoint deviation highly
correlated with

```text
I_2 = (1/Delta t) integral (g_3(t)^2-g_(3,SM)(t)^2) dt
```

and occupy a narrow band of the corresponding surplus centroid.

## Numerical result

On the stated scan surface the runner reports:

- 83 retained profiles;
- `corr(I_2,dev)=+0.999889`;
- `centroid_2=0.978185+/-0.004250`;
- top-10 `I_2` band width `0.000357`;
- `|dev|<0.1%` `I_2` band width `0.002059`; and
- per-family `I_2` monotonicity violations
  `{logistic:0, erf:3, smoothstep:0}`.

These numbers are statements about the selected scan. They do not establish
profile-family completeness, structural selection of the reference flow,
exact response linearity, or a framework-derived centroid.

## Exact obstruction now isolated

The companion
`YT_BRIDGE_ACTION_INVARIANT_GENERIC_SELECTOR_NONSELECTION_NO_GO_NOTE_2026-07-12.md`
proves a narrow exact boundary that the old scan did not contain:

> nearest-neighbor chain locality, fixed endpoints, and strict convexity of a
> quadratic selector do not by themselves select a unique normalized surplus
> average or centroid.

The companion also records the exact moment algebra behind an affine linear
response. It does not identify the auxiliary chain with the physical YT
bridge and does not turn this numerical row into a clean physical derivation.

This separation is important for claim identity. Existing consumers cite
this claim ID for the historical physical `I_2` scan. The new exact no-go has a
distinct claim ID so an eventual clean negative verdict cannot masquerade as
the old physical invariant authority.

## Claim boundary

The bounded statement licensed here is:

> Conditional on the imported endpoint, reference transport, constructive
> bridge profile, three selected profile families, scan grid, and retention
> cuts, endpoint deviation is tightly correlated with `I_2` and retained rows
> share a narrow UV centroid.

It does not establish:

- that the exact interacting lattice bridge is controlled by `I_2`;
- that the exact finite endpoint difference is a common linear functional of
  the surplus;
- that the physical endpoint-response kernel is affine or has a uniform
  nonlinear remainder bound;
- that the UV centroid band is selected by the framework;
- that the chosen families exhaust the admissible class; or
- that the one-loop reference transport is the exact physical reference.

## Remaining Nature-grade blocker

The load-bearing residual is one coherent physical bridge packet:

1. derive the microscopic bridge/source-action operator and its physical YT
   observable map;
2. derive the resulting finite endpoint-response representation, including
   profile-amplitude nonlinearity rather than only scale-coordinate kernel
   curvature; and
3. prove the kernel/support bounds that make an action-and-centroid reduction
   uniform over the derived bridge class.

The exact companion prunes the shortcut from generic locality and convexity.
It does not rule out a future operator construction from the full lattice,
algebra, and Admissibility structure.

## Audit history

Prior independent reviews classified this row as a real numerical scan rather
than a constant-printing runner, but not as a first-principles derivation. The
row remains bounded numerical evidence. Audit status and effective status are
owned only by the independent audit lane.

## Dependency context

The scan historically consumes the target-conditioned bridge stack:

- [YT_INTERACTING_BRIDGE_LOCALITY_NOTE.md](YT_INTERACTING_BRIDGE_LOCALITY_NOTE.md)
- [YT_CONSTRUCTIVE_UV_BRIDGE_NOTE.md](YT_CONSTRUCTIVE_UV_BRIDGE_NOTE.md)
- [YT_BRIDGE_REARRANGEMENT_PRINCIPLE_NOTE.md](YT_BRIDGE_REARRANGEMENT_PRINCIPLE_NOTE.md)
- [YT_BRIDGE_OPERATOR_CLOSURE_NOTE.md](YT_BRIDGE_OPERATOR_CLOSURE_NOTE.md)
- [YT_BOUNDARY_THEOREM.md](YT_BOUNDARY_THEOREM.md)

These links record the numerical scan's provenance. They do not promote the
row or close the physical bridge.
