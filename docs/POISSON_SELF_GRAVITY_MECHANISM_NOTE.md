# Poisson Self-Gravity Mechanism Finite Control No-Go

**Date:** 2026-04-05; finite no-go repair 2026-05-26
**Runner:** `scripts/poisson_self_gravity_mechanism.py`
**Claim type:** no_go
**Status:** bounded finite-packet no-go for mechanism closure; no
audit-ratified self-gravity mechanism claim is made here.

## Scope

This note is the mechanism-level checkpoint for the exact-lattice
Poisson-like self-gravity lane. Earlier wording summarized upstream
diagnostics, and the old companion runner only printed a hard-coded
`MechanismVerdict`. That was not enough to make the mechanism-level row
independently auditable.

This repair makes the binding claim negative and finite:

The current exact-lattice Poisson self-gravity packet does not close a
self-gravity mechanism. It remains a control/no-go packet because the
zero-coupling and matched-null controls survive, fixed-field propagation
stays Born-linear, but the nonzero-coupling self-consistency loop is still
nonconverged on the checked rows and the end-to-end nonlinear Born row is
only a nonconverged finite-iteration diagnostic.

No new axiom, new physical source law, or new audit verdict is introduced.
The runner imports implementation helpers from:

- `scripts/poisson_self_gravity_loop.py`
- `scripts/poisson_self_gravity_loop_v3.py`
- `scripts/poisson_self_gravity_born_audit.py`

Those files are used as included algorithm sources for the finite packet,
not as retained-status ledger authorities. The mechanism runner recomputes
the checks below rather than trusting any source note's status language.

## Binding Finite Claim

On the checked exact-lattice packet (`h = 0.25`, `W = 3`, `L = 6`, screened
Poisson-like kernel, fixed source patches, and the audit-window source and
coupling rows used by the runner):

1. The loop-level `epsilon = 0` reduction is exact to the stated hard bars:
   detector centroid shift is zero, escape ratio is one, and the zero row
   converges.
2. The nonzero loop rows keep frozen-field Sorkin/Born `I3/P` at the
   cancellation floor and preserve the weak-field TOWARD sign.
3. The loop response stays in the small-control regime: the loop/instant
   centroid ratio remains close to one and the force-mass exponent remains
   near linear on the checked source strengths.
4. The V3 matched-null packet shows a nonzero centroid/phase-ramp response
   at nonzero coupling, but those rows do not converge under the checked
   loop tolerance and remain small-control effects.
5. The representative end-to-end nonlinear Born row is re-derived as a
   finite-iteration diagnostic: step-local Born remains machine-clean, while
   the end-to-end row is not a converged Born theorem.

Together these facts block a mechanism-closure reading for the current
packet. A positive mechanism would need exact zero/matched-null controls,
step-local and end-to-end Born control, a stronger-than-escape observable,
and a stable converged nonzero-coupling loop with material effect size.
The current packet does not supply that combination.

## What This Note Does Not Claim

- It does not claim a retained or audit-ratified self-gravity mechanism.
- It does not claim a converged nonzero-coupling nonlinear loop theorem.
- It does not claim end-to-end Born preservation or end-to-end Born failure
  as a converged theorem; the end-to-end row is diagnostic because the
  subset loops are nonconverged.
- It does not use the upstream source notes as retained dependencies.
- It does not add or request any new axiom.

## Runner Certificate

The companion runner is the binding artifact for this row. It recomputes:

- the loop quick hard bars: exact zero reduction, frozen Born floor,
  TOWARD sign, loop/instant ratio, mass-law exponent, and nonconvergence
  on the nonzero quick rows;
- the V3 quick matched-null and stronger-observable checks;
- the representative finite-iteration end-to-end Born diagnostic row; and
- source-note hygiene checks ensuring this file remains a no-go repair.

Expected local certificate:

```text
RUNNER STATUS: PASS (PASS=26 FAIL=0)
```

## Reopen Conditions

Reopen the mechanism lane only with a new packet that supplies all of:

1. exact identity at zero coupling through the same checked machinery;
2. matched-null stability under the same update pipeline;
3. step-local and end-to-end Born checks that are both converged and
   defensible;
4. a stronger-than-escape observable that remains nontrivial; and
5. a stable converged nonzero-coupling loop with material effect size.

Until then, this row is a finite control/no-go boundary, not a mechanism
claim.
