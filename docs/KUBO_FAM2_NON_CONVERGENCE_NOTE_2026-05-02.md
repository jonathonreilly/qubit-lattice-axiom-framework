# Kubo Fam2 Non-Convergence Stretch Attempt

**Date:** 2026-05-02
**Status:** stretch-attempt note + named obstruction packet on the Fam2
non-convergence residual flagged in
`KUBO_CONTINUUM_LIMIT_FAMILIES_NOTE.md` and refined in
`KUBO_FAM2_REFINEMENT_NOTE.md`. Per skill workflow #9 deep-block stretch
attempt requirement (after 2 consecutive demotion cycles 10, 11).
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

## 0. The named residual

The parent notes establish:
- Fam1 and Fam3: kubo_true → ~+5.97 with 0.2% / 6.4% drift at H=0.25
- Fam2: kubo_true bounces from +6.6588 (H=0.50) → +6.3168 (H=0.35) →
  +7.0883 (H=0.25) → +4.5082 (H=0.20). 12.2% / 36.4% oscillation.

The hypothesis "Fam2 just needs finer H to settle near ~5.97" was
rejected by Lane α++.

**Named residual:** explain or close the Fam2 non-convergence.

## 1. A_min — minimal allowed premises

| Premise | Class |
|---|---|
| graph-first DAG growth dynamics with three family parameter sets | retained framework (parents) |
| Kubo coefficient computation via parallel perturbation propagator | retained method |
| static grown-DAG + imposed 1/r field | retained setup |
| H ∈ {0.5, 0.35, 0.25, 0.20} refinement schedule | retained protocol |

## 2. Forbidden imports

- Fitted Fam2 Kubo coefficient
- External convergence target (no PDG analog; no literature value)
- Same-surface family argument (cannot use Fam1/Fam3 mean as Fam2 target)

## 3. Worked attempt

### 3.1 Why might Fam2 not converge?

Fam2 has parameters: drift=0.05, restore=0.30. Compared to:
- Fam1: drift=0.20, restore=0.70
- Fam3: drift=0.50, restore=0.90

Fam2 has the **lowest drift and lowest restore** parameters. In growth-
DAG dynamics, low drift means the DAG growth is slow / weak; low restore
means the DAG re-equilibrates slowly after perturbation.

**Hypothesis (H1):** Fam2 has a non-zero relaxation timescale that scales
with H (or possibly diverges as H → 0), preventing simple H → 0
convergence.

### 3.2 Three obstruction routes

**(O1) Microscopic dynamics depend on (drift, restore) non-trivially.**
The Kubo coefficient's continuum limit is family-dependent because the
microscopic dynamics scale differently for different parameter regimes.
Failure mode: this is consistent with Fam2's behavior but does not
give an analytic prediction without solving the full microscopic
DAG growth equations.

**(O2) Phase transition or critical regime in Fam2.**
Fam2's parameter values (drift=0.05, restore=0.30) might lie near a
critical point in (drift, restore) parameter space, leading to non-analytic
behavior of the Kubo coefficient as H → 0. Failure mode: identifying the
critical point requires a phase-diagram analysis, which is not derived in
the parent notes; it would be a Nature-grade target.

**(O3) Discretization artifact specific to Fam2's parameters.**
The H refinement may interact pathologically with Fam2's specific
(drift, restore) values, causing non-monotonic convergence. Failure mode:
this is a numerical/discretization issue, not a physics result; rejecting
it requires analytic understanding of the discretization scheme's
behavior at low (drift, restore).

### 3.3 The named obstruction (sharpened)

The Fam2 non-convergence cannot be resolved analytically without:

1. Solving the full microscopic DAG growth equations at low (drift, restore)
   non-perturbatively, OR
2. Constructing a phase diagram in (drift, restore) parameter space and
   identifying critical points, OR
3. Analyzing the discretization scheme's behavior at very small H
   non-perturbatively.

None of these is currently derivable from minimal repo primitives. The
parent notes correctly mark the result as "later narrowed" and "Fam2 just
needs finer H is rejected." The honest tier remains **support / partial
positive (Fam1 + Fam3)** with Fam2 as documented non-convergent outlier.

## 4. What this stretch attempt closes

- Three obstruction routes (O1, O2, O3) explicitly named with concrete
  failure modes.
- The named residual is sharpened from "Fam2 doesn't converge" to
  "non-convergence requires non-perturbative analysis of (drift, restore)
  parameter space — not derivable from minimal premises."

## 5. What this stretch attempt does NOT close

- The Fam2 non-convergence itself
- The retention status of `kubo_continuum_limit_families_note` (still
  proposed_retained, unaudited; the partial positive on Fam1+Fam3 remains
  the honest tier)
- The retention status of `kubo_fam2_refinement_note` (still
  proposed_retained, unaudited; cyclic dep)

## 6. Status

```yaml
actual_current_surface_status: stretch_attempt + named_obstruction
proposal_allowed: false
proposal_allowed_reason: |
  Three obstruction routes (O1 microscopic dynamics, O2 phase transition,
  O3 discretization artifact) identified but none derivable from A_min.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 7. Cross-references

- Parents: [`KUBO_CONTINUUM_LIMIT_FAMILIES_NOTE.md`](KUBO_CONTINUUM_LIMIT_FAMILIES_NOTE.md), [`KUBO_FAM2_REFINEMENT_NOTE.md`](KUBO_FAM2_REFINEMENT_NOTE.md)
- Sister stretch attempts: PR [#260](https://github.com/jonathonreilly/cl3-lattice-framework/pull/260), PR [#268](https://github.com/jonathonreilly/cl3-lattice-framework/pull/268)
