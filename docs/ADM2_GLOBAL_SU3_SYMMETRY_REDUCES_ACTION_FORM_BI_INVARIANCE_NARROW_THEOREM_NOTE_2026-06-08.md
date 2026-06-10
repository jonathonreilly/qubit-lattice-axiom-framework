# ADM-2 Reduces to Global SU(3) Equivariance Plus an Annealed Regime

**Date:** 2026-06-08
**Type:** narrow theorem (a reduction with a named caveat) — locates ST2's residual
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_adm2_global_su3_symmetry_reduction_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_adm2_global_su3_symmetry_reduction_2026_06_08.txt`
**Status:** source proposal. The reduction and the quenched/annealed dichotomy
are finite-sample SU(3) computations plus the stated compact-group mechanism.
Authority role: source proposal; audit lane sets status.

> **Correction (2026-06-08, review-loop).** The earlier "ADM-2′ is strictly
> weaker than ADM-1 / ST2 is more tractable than ST1" reading is withdrawn.
> It ranked a static symmetry constraint against a dynamical generator premise.
> The `global ⊂ local` diagnostic below is true as a symmetry comparison, but
> closure-irrelevant: ADM-2′ still requires an undelivered continuous-time
> gauge-link dynamics and an annealed mixing regime. The reduction and the
> quenched/annealed dichotomy stand; the residual ranking does not.

## Context

PR #3346 (corrected) reduced ST2's gauge **action-form** to **ADM-2** = *the emergent-time
gauge-link step measure is Ad-invariant (bi-invariant)*, whence the convolution CLT gives
the heat-kernel action. ADM-2 is a **dynamical** premise, distinct from ST1's **static**
local-frame-redundancy ADM-1 (which a find-the-escape panel found does not discharge). This
note asks what the **retained global SU(3) symmetry** (global `SU(3)` = commutant of the
observables, `graph_first_su3_integration_note`) reduces in ADM-2, and which dynamical
residuals remain.

## Verdict

ADM-2 reduces to ADM-2′ (the gauge dynamics is global-SU(3)-equivariant) plus an
annealed regime. This does **not** close ADM-2 and does **not** advance ST2 past ST1:
in the **quenched** regime (a fixed neighbour background) the single-link step is **not**
central, and ADM-2′ still requires a supplied continuous-time gauge-link dynamics.
The result is a genuine *reduction*, not a discharge or residual-ranking theorem.

## What is shown (exact / computed — runner `PASS=11 FAIL=0`)

1. **The increment is in the adjoint; equivariance forces centrality (Parts 0–1).** A
   right-multiplicative step `U → U·V` transforms under a *global* rotation as `V → gVg†`.
   The staple force `drift(U,S) = su(3)-part of (US†)` is **equivariant**
   (`drift(gUg†,gSg†)=g·drift·g†`, verified to `10⁻¹⁶`). So an equivariant dynamics
   (equivariant drift + isotropic noise) has a **central** (Ad-invariant) increment measure
   — for the **free** link, directly (nonscalar-dev `1.2×10⁻³`). That is ADM-2 for the free link.

2. **The honest caveat — quenched vs annealed (Part 2).** For the **interacting** link the
   step depends on the neighbour **staple**. Conditioned on a *fixed* (quenched) staple, the
   single-link step is **not** central (nonscalar-dev `0.24`) — the background **picks a
   color direction**. Centrality is **restored** only when the staple is **annealed** —
   averaged over its global-SU(3)-equivariant fluctuation (nonscalar-dev `3.2×10⁻³`; the
   dichotomy is a factor `~74`). Algebraically: averaging an equivariant function over an
   equivariant background restores conjugation-invariance.

3. **The reduction (Part 3).** The annealed step's fundamental Fourier coefficient is a real
   scalar `φ<1` (central), so the PR #3346 convolution-CLT applies → heat-kernel attractor.
   **Therefore ADM-2 (action-form) ⟸ ADM-2′ = global-SU(3)-equivariance of the gauge
   dynamics, in the annealed (fast-equivariant-neighbour) regime.**

4. **ADM-2′ is load-bearing (Part 4, teeth).** A **non-equivariant** dynamics (a fixed
   external color field — explicit symmetry breaking) is **not** central even annealed
   (nonscalar-dev `0.34`). So the global symmetry is genuinely required.

5. **Global-vs-local diagnostic (Part 5).** On the hopping contraction `M=δ_ij=I`,
   a **global** rotation is invariant (`‖g†Mg−M‖=0`) while a **local** one is not
   (`‖g_x†Mg_y−M‖≈1.55`). This verifies the symmetry inclusion `global ⊂ local`,
   but it is **not** a closure ranking between ADM-2′ and ADM-1. ADM-2′ remains a
   dynamical-generator premise plus an annealed-regime premise.

## What this reduces to, and what stays open

- **ST2 (action-form) → ADM-2′ + annealed regime.** ADM-2′ = *the emergent-time gauge
  dynamics is global-SU(3)-equivariant*. It is **plausible from retained structure** — the
  retained hopping bilinear is SU(3)-**covariant**, so a dynamics built from it is
  equivariant — but it is about the **dynamics generator**, not just the observables, so it
  is the **named open residual**, not itself retained.
- **The annealed-regime caveat is real and open.** ADM-2 holds for the **annealed**
  (equivariantly-fluctuating-neighbour) effective step, **not** the **quenched** (fixed-
  background) per-step. Whether the emergent-time gauge dynamics is annealed (neighbours
  fluctuate equivariantly on the step timescale) is a genuine open dynamical question — the
  quenched alternative is a wall.
- **No residual ranking against ST1 is established.** The surviving ST2 wall is still an
  undelivered continuous-time gauge-link dynamics, not merely a static global symmetry fact.

## What this does NOT claim (boundary)

- **Does NOT close ADM-2.** It reduces ADM-2 to ADM-2′ + the annealed regime, both named open.
- **Does NOT claim the quenched single-link step is central** — it explicitly is not (Part 2).
- **Does NOT close ADM-1** (the static local-frame gate; the panel's `forced_finding` stands).
- **Does NOT claim ST2 is ahead of ST1** or that ADM-2′ is a strictly weaker residual in the
  sense relevant to closure.
- No new axiom or import: global `SU(3)` = retained commutant; the convolution-CLT
  consequence is PR #3346 / standard math; the staple force and Haar average are standard.
- The withdrawn reading "ST2 is more tractable than ST1 because ADM-2′ is weaker" is not a
  status result. This note establishes only the reduction mechanism plus the
  quenched/annealed dichotomy.

## Cross-references

- ST2 → ADM-2 (the premise reduced here): PR #3346 (`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08`)
- ST1 / ADM-1 (the static gate, distinct): PR #3332 (`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08`)
- Global `SU(3)` = commutant (retained): [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- Record supplies no continuous generator (retained): [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
- Standard method (not imports): heat-bath / Langevin staple force on lattice gauge links; Haar average / depolarizing twirl; convolution CLT on compact groups.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [emergent_gauge_heat_kernel_clt_attractor_conditional_on_bi_invariant_dynamics_narrow_theorem_note_2026-06-08](EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md)
