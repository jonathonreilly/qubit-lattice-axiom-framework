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

## What This Note Does Not Claim

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
PASS=17 FAIL=0
```

## Audit Request

Please re-audit only the bounded configured diagnostic above. The intended
safe outcome is retained-bounded status for this finite well/hill separation
if the auditor agrees the runner closes the stated signs. Broader gravity-sign
physics remains out of scope.
