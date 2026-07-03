# Emergent-Time Gauge Weight Is the Heat-Kernel: the Universal Convolution-CLT Attractor of Bi-Invariant Gauge-Link Dynamics

**Date:** 2026-06-08
**Type:** narrow theorem (CLT universality) — within a supplied discrete i.i.d. step model,
reduces ST2's action-form residual to a named dynamical premise
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_emergent_gauge_weight_heat_kernel_clt_fixed_point_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_emergent_gauge_weight_heat_kernel_clt_fixed_point_2026_06_08.txt`
**Status:** source proposal. The convolution-CLT core (Parts 1–5) is exact/computed; Part 6
demonstrates the corrected scope. Authority role: source proposal; audit lane sets status.

> **Correction (2026-06-08).** An earlier version of this note claimed the CLT result
> **unifies** the two gates via the identity *"bi-invariance = ADM-1, so one premise forces
> both gates."* A find-the-escape panel **refuted** that identity (`forced_finding`): the
> gauge-covariance law `U_μ(x) → g(x) U_μ(x) g(x+μ)†` is *indifferent* to whether the
> dynamical step measure is Ad-invariant, so bi-invariance of the step measure (call it
> **ADM-2**) is a **dynamical** premise **strictly stronger than**, and **not implied by**,
> the **static** fibre-frame redundancy **ADM-1** (PR #3332). **The gates are not unified.**
> This note now states only the honest conditional: ST2's action-form reduces to ADM-2.

## The problem this addresses

PR #3339 reduced ST2 ("which gauge action?") to: is the gauge link a continuous diffusion
with the canonical-Laplacian generator (the heat-kernel is the *unique* diffusion kernel
among the candidates). The retained `RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06` warns
that *Record alone* supplies no continuous Markov generator. The route tested here supplies
a discrete-emergent-time lane model: emergent time is represented by accumulated record
steps, the link follows an i.i.d. small-step walk on the group, and the fine-resolution,
many-step propagator is governed by the **convolution central limit theorem** on the group.

## Verdict

**Within that supplied discrete i.i.d. small-step lane, the heat-kernel weight is the
*universal* convolution-CLT attractor of bi-invariant gauge-link dynamics; ST2's
action-form residual therefore reduces to the dynamical premise ADM-2 (the step measure is
Ad-invariant) — which is strictly stronger than, and distinct from, the static ADM-1.**
Concretely:

1. **Universality (the microscopic action-form ambiguity washes out).** For a group-valued
   degree of freedom (gauge link / plaquette holonomy) evolving by i.i.d. **bi-invariant**
   (Ad-invariant) Markov steps of small spread `ε`, the emergent-time-`t` propagator
   (`n = t/ε` steps) converges to the **heat kernel** `P_t = exp(tΔ/2)` — for *any*
   bi-invariant step distribution. The runner shows Wilson-, heat-kernel-, and
   Gaussian-(Manton-)type steps **all flow to the same heat kernel** (Part 2), with
   convergence improving as `ε→0` (the diffusion limit). The Wilson/HK/Manton ambiguity
   the action-form no-go could not resolve **dissolves under emergent-time coarse-graining**.

2. **Bi-invariance is load-bearing (Part 3, teeth).** A non-central (drifted) step has a
   non-scalar group-Fourier matrix (deviation `0.489`) and does **not** flow to the heat
   kernel in the tested contrast; bi-invariance is load-bearing for this reduction.

3. **Generator uniqueness (Part 4).** On a simple compact group the only Ad-invariant
   second-order generator is `c·Δ` (the Casimir), and bi-invariance kills the drift. So
   the CLT limit is the heat semigroup, with **only the rate `c` free** — the `g_bare=1`/`β=6`
   scale (retained convention). SU(3) cross-check (Part 5) reproduces `exp(−2/3)`.

4. **ADM-1 does NOT imply ADM-2 (Part 6 — the corrected scope).** The gauge-covariance law
   `U → g(x) U g(x+μ)†` is a **kinematic** property of the connection, **indifferent** to
   the dynamical step measure: the drifted (non-bi-invariant) step is **equally
   gauge-covariant-valid** (the law is measure-blind) yet is non-bi-invariant *and* does
   not flow to the heat kernel. So *frame-redundant / gauge-covariant* (ADM-1) does **not**
   entail *bi-invariant step measure* (ADM-2). **ADM-2 is strictly stronger; the gates are
   not unified.**

## What this reduces, and what stays open

- **ST2 (action-form) → ADM-2, inside the supplied lane model.** The emergent gauge weight
  flows to the heat-kernel when the emergent-time gauge-link step measure is Ad-invariant
  (ADM-2). This locates ST2's residual sharply and shows the action-form ambiguity is a
  coarse-graining artifact **conditional on ADM-2** — which is **open**: per
  `record_classical_semigroup_boundary` and
  `record_markov_generator_embeddability_boundary` (both retained), Record alone supplies no
  such continuous generator.
- **ST1 (ADM-1) and ST2 (ADM-2) are DISTINCT open premises** — not one. The find-the-escape
  panel's `forced_finding` on ADM-1 stands: global color redundancy is exact and retained
  (global `SU(3) ∈` commutant — `graph_first_su3_integration_note`, `cl3_color_automorphism_theorem`,
  both retained), but the **global → local** step is not dischargeable from `A_min` + retained.
  For the **irreducible** color triplet the genuine central-sector partition map
  `D(M)=Σ_k P_k M P_k` is **trivial** (Schur: the only central projectors are `{0, I_3}`), so
  the wall is **not** register-not-read-shaped — it is the *Record-supplies-no-continuous-
  dynamics* boundary. (The loose "frame = unregistered reconstruction" route is the form
  demoted by `REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06`.)

## What this does NOT claim (boundary)

- **Does NOT unify the gates** (corrected; see above). ADM-1 ≠ ADM-2; ADM-1 does not imply ADM-2.
- **Does NOT derive ADM-2** (the step measure's Ad-invariance) — it is the named open
  dynamical premise; Record alone supplies no continuous generator (retained boundary).
- **Does NOT derive** the discrete-emergent-time i.i.d. walk model, stationarity, or the
  small-step diffusion scaling; those are the bounded lane premises used by the CLT check.
- **Does NOT supply** the rate (`g_bare` convention) or the inter-link spatial coupling
  (full Yang–Mills dynamics — separate). Scope: the single group-valued weight (action *form*).
- No new axiom or import: the convolution CLT on compact groups, characters, and Casimirs
  are standard math; the open premise is named, not assumed.

## Cross-references

- The semigroup / no-continuous-generator boundaries (retained): [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md), [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
- The action-form ambiguity this dissolves (conditional on ADM-2): [`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md)
- Global color redundancy (retained): [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`CL3_COLOR_AUTOMORPHISM_THEOREM`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
- The ADM-1 gate's open status (corroborating, open_gate): [`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md), [`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08`](GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md)
- The demoted loose route: [`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06`](REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md)
- Program companions: PR #3332 (ADM-1 / minimal coupling), PR #3339 (HK = unique diffusion kernel), PR #3341 (continuum = IR-emergence)
- Standard method (not imports): central limit theorem for convolutions on compact Lie groups (Heyer; Liao, *Lévy Processes in Lie Groups*); heat kernel on compact groups.
