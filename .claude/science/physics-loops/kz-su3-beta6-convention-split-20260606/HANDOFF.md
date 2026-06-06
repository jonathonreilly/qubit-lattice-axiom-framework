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

PR for this block: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2808

GitHub verification: open PR, base
`physics-loop/kz-external-lift-gate-20260606`, head
`physics-loop/kz-su3-beta6-convention-split-20260606`, mergeable
`MERGEABLE`, merge state `UNSTABLE`.

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

Continue the 12-hour campaign. Prefer a retained-positive stretch route over
another shallow no-go, with the record dynamics clock/rate normalization gate
and repo-owned finite SU(3), Wilson beta=6 reproduction as the top live
candidates.
