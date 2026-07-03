# ST1 and ST2 Sit at the Same Wall: One Undelivered Continuous-Time Gauge-Link Dynamics

**Date:** 2026-06-08
**Type:** narrow theorem (one brick) + corrected residual convergence — honest capstone
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_st1_st2_same_wall_gauge_dynamics_residual_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_st1_st2_same_wall_gauge_dynamics_residual_2026_06_08.txt`
**Status:** source proposal. The brick and the three negative checks are exact/computed; the
convergence is a bounded residual map, not a universal no-go. Authority role: source proposal;
audit lane sets status.

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
       — explicit import candidate, not admitted here. The Lattice + Quantum + Record
       baseline does not supply it: record_classical_semigroup_boundary (retained) and
       record_markov_generator_embeddability_boundary (retained_no_go) state Record supplies
       no continuous Markov generator; PR #3332 disclaims any gauge dynamics.
+ (R2) a mixing / ergodicity regime giving i.i.d.-central steps — OPEN.
+ (H_cov-as-connection): the current ledger treats this as audited_conditional on
       ADM-1's local-frame-redundancy premise; this note does not promote it.
```

**R1, R2, and ADM-1 collapse, for this route map, to one undelivered dynamical package:** a
continuous-time gauge-link / color-einselection dynamics (generator + rate + the local frame
redundancy that makes `U` a transporter, plus the mixing regime needed for central steps).
**Therefore ST1 and ST2 sit at the *same* wall in the current residual map.** ST2 *relocated
and relabelled* ADM-1's open input; it did not weaken it. The single minimal residual package:
**derive (or import, with owner approval) that continuous-time gauge-link dynamics.**

This is the correct, opposite reading of the session's earlier false "the two gates *unify*
into one premise": the gates do not unify, but their *residuals converge* onto one undelivered
dynamical input.

## What this does NOT claim (boundary)

- Does **not** discharge ADM-2′ or ADM-1; does **not** put ST2 ahead of ST1.
- Does **not** treat PR #3332 as retained (it is **audited_conditional**); the connection
  reading of `H_cov` is conditional on ADM-1's premise.
- The action-gradient / Langevin gauge-link generator is an **unadmitted import candidate**
  (an undelivered continuous dynamics), **not** "standard method" — a sampling algorithm for a
  given action is not a derivation of the framework's emergent-time dynamics.
- Does **not** prove no future route can derive the package. It is a bounded residual map of
  the ADM-1/ADM-2 routes reviewed here.
- No new axiom, primitive, or import is added.

## No-Go Discipline Gate (for the bounded residual map)

**Result:** PASS for the narrowed `bounded_theorem` framing only. This is not a universal
no-go; it says the reviewed ST1/ST2 routes presently collapse onto one undelivered
continuous-time gauge-link/color-einselection dynamics package.

**N1 — Alternative route enumeration.**

| Route | Test / status | Why it does not close the residual |
|---|---|---|
| Global equivariance of the force | ATTEMPTED, runner Parts 1-2 | Equivariance survives as the real brick, but it also holds for `-F`, a commutator flow, and `F=0`; it does not select, sign, rate, or produce a generator. |
| Local-frame / ADM-1 connection route | ATTEMPTED, runner Part 3 and PR #3332 boundary | The force is not a single global adjoint under independent local frames, and the `H_cov`-as-connection leg remains conditional on ADM-1 rather than retained here. |
| Annealed-centrality route | ATTEMPTED, runner Part 4 | Schur twirling gives first-moment centrality only; the fixed interacting per-step is non-central and the sampled background is correlated. |
| Record-baseline generator route | RULED OUT BY PRIOR | `record_classical_semigroup_boundary` and `record_markov_generator_embeddability_boundary` say Record supplies durable realized outcomes, not a continuous Markov/gauge-link generator. |
| Compact-group CLT route | RULED OUT BY PRIOR / conditional | PR #3346 gives the CLT conditional on central/i.i.d. dynamics; it does not derive the dynamics, generator, rate, or mixing premise. |
| Registered-primitive route | RULED OUT BY PRIOR | The registered scale-reference and kinetic-isotropy primitives supply units conversion and OS0 kinetic-form isotropy only; neither supplies gauge-link dynamics. |

**N2 — Wall-independence audit.** The raw labels `R1`, `R2`, and `ADM-1` are not counted as
three independent admissions. The collapsed wall is one package: continuous-time gauge-link /
color-einselection dynamics with generator, rate, local transporter reading, and sufficient
mixing. Closing only one facet would not automatically close the others; the claim is only that
the reviewed routes converge on that single package, not that a theorem of logical equivalence
has been proven.

**N3 — Hidden-wall scan.** Phrases such as "retained" are backed by the cited SU(3) and Record
boundary rows; "standard method" is explicitly rejected as a source of dynamics; "import" is
made explicit as an unadmitted candidate; "baseline" means the named Lattice + Quantum + Record
axioms only. No hidden wall is left implicit.

**N4 — Residual matching.** The #3390 ADM-2 reduction matches the equivariance-plus-annealing
residual; #3346 matches only the central/i.i.d. CLT premise, not the generator; #3332 matches
only the conditional local-frame connection leg; the Record boundary notes match only the
claim that Record does not supply a continuous generator. No citation is used beyond its
matching residual.

**N5 — Rhetoric audit.** "Not a central per-step kernel" is tested only for the finite `SU(3)`
matrix diagnostic in the runner. "Not rankable vs ADM-1" is a category-boundary claim, not a
new theorem about every possible gauge-dynamics construction. The source language is therefore
limited to the ADM-1/ADM-2 routes reviewed here.

**N6 — Partial-closure path scan.** A future owner-approved import, retained derivation, or
definition-level retirement of the gauge-link/color-einselection package could close this wall.
The current Record axiom, scale-reference primitive, and kinetic-isotropy primitive do not
close it. The #3395 correction retires the mistaken ST2-ahead ranking but does not supply the
dynamics.

**N7 — Steelman.** A future theory layer might derive the continuous gauge-link semigroup and
mixing regime from durable record stability or color-sector einselection, making the
R1/R2/ADM-1 package a theorem rather than an import. This is a live route, so the present note
is deliberately bounded: it records the current residual convergence, not impossibility.

**N8 — Cross-cycle echo.** Similar walls appear in the Record generator-boundary notes, the
ADM-1 conditional connection route, and the ADM-2 bi-invariant-dynamics route. None is retired
by the current primitives or axioms; the known retirement mechanisms are a retained derivation
or explicit owner-approved import of the continuous gauge-link/color-einselection dynamics.

## Cross-references

- ST2 → ADM-2 → ADM-2′ + annealed (the reduction): PR #3390 (`ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08`)
- The CLT (conditional on bi-invariant dynamics): PR #3346 (`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08`)
- The covariant hopping (**audited_conditional**, PR #3332): `MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08`
- Global SU(3) = commutant (retained): [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`CL3_COLOR_AUTOMORPHISM_THEOREM`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
- Record supplies no continuous generator: [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md), [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
- Standard method (not imports): Schur / depolarizing twirl; central limit theorem on compact groups.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [adm2_global_su3_symmetry_reduces_action_form_bi_invariance_narrow_theorem_note_2026-06-08](ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08.md)
- [emergent_gauge_heat_kernel_clt_attractor_conditional_on_bi_invariant_dynamics_narrow_theorem_note_2026-06-08](EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md)
- [matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md)
