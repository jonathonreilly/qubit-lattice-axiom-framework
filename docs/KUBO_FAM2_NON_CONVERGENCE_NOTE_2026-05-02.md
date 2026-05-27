# Kubo Fam2 Non-Convergence Possible-Obstruction Inventory

**Date:** 2026-05-02 (scope repair: 2026-05-27)
**Claim type:** open_gate
**Primary runner:** `scripts/frontier_kubo_fam2_non_convergence_stretch.py`
**Type:** open_gate
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The cited authorities support that Fam2 is non-convergent on the tested H ladder and that the easy near-term rescue is weakened. They do not prove the exhaustive obstruction claim that only the three named non-perturbative routes could reso"*

with repair: *"missing_bridge_theorem: prove or replace the exhaustive claim that the Fam2 residual requires one of the three named non-perturbative analyses; otherwise scope the note explicitly to documented possible obstruction routes."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The runner-documented non-convergence of Fam2 across the tested H ladder (oscillation range 12.2%–36.4%), the explicit naming of three candidate obstruction routes (O1 microscopic dynamics, O2 critical-point / phase transition, O3 discretization artifact), and the sharpening of the residual from a vague non-convergence to a statement requiring non-perturbative analysis of (drift, restore) parameter space.
- **NON-load-bearing (split off / admitted):** The exhaustive claim that Fam2 non-convergence can only be resolved via one of the three named non-perturbative routes is not proved; no bridge theorem establishes that these routes are exhaustive, so the exhaustive-obstruction framing is an admitted, non-load-bearing characterization rather than a derived result.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Scope Repair (2026-05-27)

The prior version overreached by saying the Fam2 residual "requires" one
of three named non-perturbative analyses. This repair removes that
exhaustive claim. The binding claim is now narrower:

- the recorded Fam2 refinement data are non-monotone over the sampled
  `H` schedule;
- the simple "Fam2 only needs finer `H` to settle near the Fam1/Fam3
  value" reading is not supported by the sampled data;
- three concrete possible obstruction routes are documented for future
  work;
- the list is not exhaustive, and no route is proved necessary.

This is an open-gate inventory, not a positive convergence theorem and
not a no-go theorem.

## Recorded Finite Data

The sampled `kubo_true` values under the existing finite refinement
schedule are:

| family | parameters | sampled behavior |
|---|---|---|
| Fam1 | `drift=0.20, restore=0.70` | settles near `+5.97` over the sampled range |
| Fam2 | `drift=0.05, restore=0.30` | `+6.6588` at `H=0.50`, `+6.3168` at `H=0.35`, `+7.0883` at `H=0.25`, `+4.5082` at `H=0.20` |
| Fam3 | `drift=0.50, restore=0.90` | settles near `+5.97` over the sampled range |

The Fam2 values bounce rather than moving monotonically toward the Fam1
and Fam3 sampled value. A same-surface family average is not used as a
target value; it is only the comparison that motivated the residual.

## Minimal Local Premises

| Premise | Role |
|---|---|
| graph-first DAG growth dynamics with three family parameter sets | context for the sampled families |
| Kubo coefficient computation via parallel perturbation propagator | context for the sampled quantity |
| static grown-DAG plus imposed `1/r` field | context for the sampled setup |
| `H ∈ {0.50, 0.35, 0.25, 0.20}` | finite refinement schedule |

## Forbidden Imports

- No fitted Fam2 Kubo coefficient.
- No external convergence target.
- No same-surface family argument that forces Fam2 to share a Fam1/Fam3
  limit.
- No claim that the three possible obstruction routes are exhaustive.

## Possible Obstruction Routes

**(O1) Parameter-dependent microscopic dynamics.**
The Kubo coefficient's limiting behavior may depend nontrivially on
`(drift, restore)`. Fam2 has the lowest drift and lowest restore among
the three recorded families, so it is a plausible place for slow
relaxation or a different scaling regime. This route is possible, not
proved necessary.

**(O2) Critical or near-critical parameter regime.**
Fam2's parameter pair may lie near a critical region in the
`(drift, restore)` plane, producing non-analytic or slowly settling
behavior as `H` changes. This route would require a phase-diagram
analysis before it could become a theorem.

**(O3) Fam2-specific discretization interaction.**
The refinement schedule may interact pathologically with Fam2's low
drift/restore parameters. This route would require an analysis of the
discretization scheme at low `(drift, restore)` before it could be
separated from physics.

These routes are documented candidates. The row does not prove that the
true explanation must be one of them.

## What This Open Gate Moves

- It records the finite non-monotone Fam2 sample pattern.
- It blocks the shallow interpretation that Fam2 has already visibly
  settled to the Fam1/Fam3 sampled value.
- It names three concrete next analyses with their expected proof burden.

## What This Does Not Close

- It does not resolve Fam2 non-convergence.
- It does not prove an exhaustive obstruction trichotomy.
- It does not prove a continuum limit for Fam2.
- It does not alter the status of any parent Kubo-family evidence.
- It does not consume observed values, fitted targets, or literature
  comparators.

## Status Certificate

```yaml
actual_current_surface_status: open
proposal_allowed: false
proposal_allowed_reason: "This is a possible-obstruction inventory, not a theorem closing Fam2 behavior."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
