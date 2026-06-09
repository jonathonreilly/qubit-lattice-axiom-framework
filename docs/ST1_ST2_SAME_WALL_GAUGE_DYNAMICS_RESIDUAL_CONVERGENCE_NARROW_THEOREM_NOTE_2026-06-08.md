# ST1 and ST2 Sit at the Same Wall: One Undelivered Continuous-Time Gauge-Link Dynamics

**Date:** 2026-06-08
**Type:** narrow theorem (one brick) + corrected residual convergence — honest capstone
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_st1_st2_same_wall_gauge_dynamics_residual_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_st1_st2_same_wall_gauge_dynamics_residual_2026_06_08.txt`
**Status:** source proposal. The brick and the three negative checks are exact/computed; the
convergence is the honest residual map. Authority role: source proposal; audit lane sets status.

> **Why this note exists.** An attempt to discharge ADM-2′ (ST2's dynamical gate) and put ST2
> "ahead of" ST1's ADM-1 was **refuted by a red-team panel** (`over_reach_corrected`). This
> note records what genuinely survives and the corrected structural finding — and corrects the
> session's repeated over-reach (claiming ST2 progress via a global-vs-local category error).

## The one genuine brick (survives — exact, runner Part 1)

**The color-equivariance of the gauge-link force is free.** Given any internal-symmetric
coupling, the force `F(U,M) = su(3)-part(U M†)` is global-SU(3)-equivariant,
`F(gUg†, gMg†) = g F(U,M) g†` (200 configs, dev `10⁻¹⁵`). It needs no input beyond the
**retained** global SU(3) commutant (`graph_first_su3_integration_note`,
`cl3_color_automorphism_theorem`). That is a real, if modest, brick.

## What does NOT survive (each demonstrated false in the runner)

- **(X1) Equivariance does not discharge ADM-2′ — it is vacuous as a delivery of dynamics
  (Part 2).** The same equivariance identity holds for the gradient force, its **negation**
  (reversed arrow), a **non-gradient commutator flow**, and **F = 0** (no dynamics). So it
  selects, signs, or rates **no** generator. ADM-2′ asserts the *gauge dynamics* is
  equivariant; equivariance proves only the *form*, not the **existence** of the dynamics.
- **(X2) ADM-2′ is not "weaker than" ADM-1 — that is a category error (Part 3).** Global
  equivariance is automatic for any internal-symmetric coupling; under a **local** law
  `g_x ≠ g_y` the force transforms **bi-fundamentally** (dev `2.2`, `1.1` vs single-adjoint),
  not by a global adjoint. A *static* symmetry constraint (ADM-1) is not rankable against
  *dynamical* generator premises toward closure — this is the same global-vs-local indifference
  that refuted this session's earlier "bi-invariance = ADM-1" over-reach.
- **(X3) "Annealed centrality" is a Schur twirl, not the CLT premise (Part 4).** An ensemble
  twirl over global `g` gives first-moment centrality (dev `0.002`) — automatic from the
  retained global symmetry — but the interacting **per-step** kernel is non-central (dev `0.27`)
  and the increments are strongly **correlated** (lag-1 autocorr `0.99`). The PR #3346
  **i.i.d.-central** CLT needs both; the interacting walk supplies neither.

## The corrected structural finding (the value)

ST2's gauge-action-form residual, stated honestly, is:

```
  (equivariance of the force: FREE, retained)
+ (R1) a continuous-time action-gradient gauge-link GENERATOR on U, with arrow + rate
       — IMPORT. A_min delivers none: record_classical_semigroup_boundary (retained) and
       record_markov_generator_embeddability_boundary (retained_no_go) state Record supplies
       no continuous Markov generator; PR #3332 disclaims any gauge dynamics.
+ (R2) a mixing / ergodicity regime giving i.i.d.-central steps — OPEN.
+ (H_cov-as-connection): audited_conditional on ADM-1's local-frame-redundancy premise
       (PR #3332 is effective_status = audited_conditional, NOT retained).
```

**R1, R2, and ADM-1 are one un-derived input wearing three hats:** a continuous-time
gauge-link / color-einselection dynamics (generator + rate + the local frame redundancy that
makes `U` a transporter). **Therefore ST1 and ST2 sit at the *same* wall.** ST2 *relocated and
relabelled* ADM-1's open input; it did not weaken it. The single minimal residual: **derive
(or import, with owner approval) that continuous-time gauge-link dynamics.**

This is the correct, opposite reading of the session's earlier false "the two gates *unify*
into one premise": the gates do not unify, but their *residuals converge* onto one undelivered
dynamical input.

## What this does NOT claim (boundary)

- Does **not** discharge ADM-2′ or ADM-1; does **not** put ST2 ahead of ST1.
- Does **not** treat PR #3332 as retained (it is **audited_conditional**); the connection
  reading of `H_cov` is conditional on ADM-1's premise.
- The action-gradient / Langevin gauge-link generator is an **import** (an undelivered
  continuous dynamics), **not** "standard method" — a sampling algorithm for a given action is
  not a derivation of the framework's emergent-time dynamics.
- No new axiom. Statuses ledger-verified on `origin/main`.

## Cross-references

- ST2 → ADM-2 → ADM-2′ + annealed (the reduction): PR #3390 (`ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08`)
- The CLT (conditional on bi-invariant dynamics): PR #3346 (`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08`)
- The covariant hopping (**audited_conditional**, PR #3332): `MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08`
- Global SU(3) = commutant (retained): [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`CL3_COLOR_AUTOMORPHISM_THEOREM`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
- Record supplies no continuous generator: [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md), [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
- Standard method (not imports): Schur / depolarizing twirl; central limit theorem on compact groups.
