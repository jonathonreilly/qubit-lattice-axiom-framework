# Gravity Sign Well/Hill Diagnostic

**Date:** 2026-04-10; narrowed 2026-05-27
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_gravity_sign_well_hill_diagnostic.py`
**Historical runner:** `scripts/frontier_correct_coupling.py`
**Status authority:** independent audit lane only

---

## Status

This row is narrowed to a configured finite 1D diagnostic. It does not claim a
framework derivation of physical gravity sign, a derivation of the staggered
scalar/lapse coupling from the baseline axioms, or any irregular-graph
portability result.

The retained-bounded one-hop support available here is
[`STAGGERED_SCALAR_PARITY_LAPSE_COUPLING_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_SCALAR_PARITY_LAPSE_COUPLING_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md),
which certifies the displayed finite operator forms only. It does not prove
that the baseline framework forces those forms.

## Bounded Claim

In the configured 1D external-potential test:

```text
n = 61
mass = 0.30
dt = 0.12
steps = 20
mass point = 38
initial packet center = 30
well: V(x) < 0
hill: V(x) > 0
```

the stipulated parity and lapse Hamiltonian forms distinguish well from hill:

```text
identity: well -> TOWARD, hill -> TOWARD   (negative control)
parity:   well -> TOWARD, hill -> AWAY
lapse:    well -> TOWARD, hill -> AWAY
```

The diagnostic is defined by the final centroid displacement relative to the
initial packet center:

```text
disp > 0  => TOWARD the mass point
disp < 0  => AWAY from the mass point
```

The runner verifies that all six evolutions conserve norm to numerical
tolerance and that the signs above hold.

## Lapse regularization (explicit, load-bearing — 2026-05-28 repair)

The 2026-05-28 audit verdict flagged a previously **silent, load-bearing**
regularization in the lapse coupling:

> *"the configured well potential gives N = 1 + Phi/m < 0, while the
> runner silently floors N to 0.01 before taking sqrt(N). That floor is
> unstated and load-bearing."*

This is now made explicit. The lapse coupling forms the local lapse
`N(x) = 1 + Phi(x)/m` and applies `sqrt(N)` on both sides of the
Hamiltonian (`sqrt(N) H sqrt(N)`). In the configured **well** potential,
`Phi < 0` near the source drives `N < 0`, so a naive `sqrt(N)` would be
complex. The runner floors `N` to `LAPSE_FLOOR = 0.01` before the square
root:

```text
N_reg(x) = max(1 + Phi(x)/m, 0.01).
```

The runner now prints a `LAPSE REGULARIZATION REPORT` quantifying how
load-bearing the floor is on the configured cases:

```text
well: min(1 + Phi/m) = -79.0000, floored sites = 15/61  (floor ACTIVE, load-bearing)
hill: min(1 + Phi/m) = +1.2658,  floored sites =  0/61  (floor inactive)
```

So the lapse **well** row is a result on a **regularized** (floored)
lapse configuration, NOT a source-stated `N >= 0` lapse. The floor is
load-bearing for the lapse-well direction: 15 of 61 sites are clamped,
and the raw lapse reaches `-79`. The lapse **hill** row needs no floor.

**The parity and identity rows do NOT use any floor** and reproduce the
displayed directions without regularization; they are the clean core of
this diagnostic. The lapse-well TOWARD result must be read as carrying
the explicit `LAPSE_FLOOR = 0.01` regularization, not as a physical
`N >= 0` lapse evolution.

## What This Note Does Not Claim

- No claim that the lapse-well direction holds for a source-stated
  `N >= 0` (unregularized) lapse: it is a regularized-N result with an
  explicit `LAPSE_FLOOR = 0.01` floor active on 15/61 well sites.

- No derivation of the parity or lapse coupling from A1/A2/minimal axioms.
- No claim that either coupling is physically selected by the framework.
- No graph self-gravity result.
- No irregular-graph directional observable closure.
- No statement about Part 1 force-sign language from the historical runner.
- No retained verdict and no direct ledger retag.

## Relation To The Historical Runner

`scripts/frontier_correct_coupling.py` remains a historical broad diagnostic.
It prints graph/self-gravity sections and older direction labels that are not
part of this repaired row. The audit blocker specifically asked to narrow the
source to the Part 4 well/hill diagnostic and remove the stale broader graph
and lapse-direction claims. This note and its new runner do that.

## Verification

Run:

```bash
python3 scripts/frontier_gravity_sign_well_hill_diagnostic.py
```

Expected result:

```text
Gravity sign well/hill diagnostic: PASS
PASS=20 FAIL=0
```

## Audit Request

Please re-audit only the bounded configured diagnostic above. The intended
safe scope is this finite well/hill separation if the auditor agrees the runner
closes the stated signs. Broader gravity-sign physics remains out of scope. Any
effective status is assigned only by the independent audit lane.
