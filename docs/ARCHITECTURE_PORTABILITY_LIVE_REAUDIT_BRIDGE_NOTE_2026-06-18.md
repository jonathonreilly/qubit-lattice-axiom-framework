# Architecture Portability Live Re-Audit Bridge

**Date:** 2026-06-18
**Claim type:** bounded_theorem (source-side finite configured-sweep bridge;
not full Newton closure)
**Actual current-surface status:** source-side re-audit bridge; independent
audit owns any verdict or effective-status propagation.
**Target row:**
`work_history.repo.review_feedback.architecture_portability_audit_2026-04-11`
**Primary runner:**
`scripts/architecture_portability_live_reaudit_bridge_2026_06_18.py`

## Result

The archived `ARCHITECTURE_PORTABILITY_AUDIT_2026-04-11.md` row failed
correctly as live evidence. It was a work-history packet without the
source-note computation, runner output, per-architecture measurements, or
registered boundary checks needed for audit.

The current source-side re-audit target is different and narrower:

- [`ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md`](ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md)
- [`scripts/frontier_architecture_portability_sweep.py`](../scripts/frontier_architecture_portability_sweep.py)
- [`logs/runner-cache/frontier_architecture_portability_sweep.txt`](../logs/runner-cache/frontier_architecture_portability_sweep.txt)
- archive firewall:
  [`scripts/archive_architecture_portability_firewall_2026_06_16.py`](../scripts/archive_architecture_portability_firewall_2026_06_16.py)

That live packet repairs the audit blocker at the source-artifact level: the
runner constructs four configured architecture rows, measures source-mass
scaling and attraction sign on all four, measures Born `I_3` only on the
ordered and staggered barrier-supported rows, archives deterministic output,
and states the finite-scope boundaries.

## Safe Re-Audit Scope

The live re-audit target is only this bounded finite configured sweep:

- ordered 3D cubic, side `14`;
- staggered 3D cubic, side `14`;
- Wilson 3D cubic, side `14`;
- random geometric 2D control row, side `10`, `n=100`, mass-scaling only;
- source amplitudes `0.4`, `0.6`, `0.8`, `1.0`, `1.5`;
- mass exponent within `10%` of `1.0` on at least three of four rows;
- attraction sign toward source on all four rows;
- Born `I_3 < 1e-6` only where measured, namely ordered and staggered rows.

The primary cache reports:

```text
beta within 10% of 1.0: 4/4 architectures (need >= 3) -> PASS
Attractive force:       4/4 architectures (need all) -> PASS
Born rule I_3 < 1e-6:   all measured pass -> PASS
OVERALL: PASS -- bounded source-mass portability companion established
```

## Boundary

This bridge does not edit audit results, restore the archived work-history
packet as evidence, or claim:

- standalone Newton closure;
- both-masses closure;
- cross-architecture distance-law closure;
- a 3D distance-law result for the 2D random-geometric control row;
- Wilson Born-rule measurement;
- architecture-independent universality outside the configured finite sweep;
- retained or retained-bounded effective status.

The correct source-side reading is:

> the old archived row remains a failed historical packet, while the live sweep
> is now an executable bounded finite source-mass / attraction portability
> companion that can be independently re-audited under its narrowed scope.

## Verification

Run:

```bash
python3 scripts/frontier_architecture_portability_sweep.py
python3 scripts/archive_architecture_portability_firewall_2026_06_16.py
python3 scripts/architecture_portability_live_reaudit_bridge_2026_06_18.py
```

Expected bridge result:

```text
SUMMARY: ARCHITECTURE PORTABILITY LIVE REAUDIT BRIDGE PASS=51 FAIL=0
```
