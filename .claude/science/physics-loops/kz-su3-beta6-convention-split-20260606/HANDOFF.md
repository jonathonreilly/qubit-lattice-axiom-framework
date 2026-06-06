# Handoff

## Current Status

Stacked branch:

```text
physics-loop/kz-su3-beta6-convention-split-20260606
```

Intended base:

```text
physics-loop/kz-external-lift-gate-20260606
```

Parent PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2804

PR for this block: pending.

## Result

The old `W_lift ~= 0.05` bracket width is reproduced by the finite SU(3)
source-bundle vector figure at plotted `lambda=3.0`, while Wilson `beta=6`
maps to `lambda=1.5` under the paper action convention. At `lambda=1.5`, the
same source-vector extraction gives width `0.245195`.

This prunes the old source/convention shortcut. It does not close the parent
K-Z external-lift gate.

## Remaining Blocker

The route still needs a direct finite `SU(3)`, Wilson `beta=6` table/source-data
bracket or a repo-owned beta=6 SDP reproduction.

## Next Action

Commit, push, open the stacked PR, patch this pack with the PR URL, then
continue the 12-hour campaign.
