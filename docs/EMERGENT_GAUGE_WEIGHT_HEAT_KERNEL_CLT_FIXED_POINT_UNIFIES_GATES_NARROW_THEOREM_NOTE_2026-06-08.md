# Emergent-Time Gauge Weight Is the Heat-Kernel: the Universal Convolution-CLT Fixed Point — Unifying the Gauging and Action Gates

**Date:** 2026-06-08
**Type:** narrow theorem (CLT universality) + a gate-unification reduction + named residuals
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_emergent_gauge_weight_heat_kernel_clt_fixed_point_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_emergent_gauge_weight_heat_kernel_clt_fixed_point_2026_06_08.txt`
**Status:** source proposal. The convolution-CLT core (Parts 1–5) is exact/computed. The
gate-unification reading and the residual map are honest structural statements resting on
one open premise (ADM-1). Authority role: source proposal; audit lane sets status.

## The problem this addresses (the unified gate)

The interacting-gauge sector's two foundational gates were each reduced — in this program
— to one open input:

- **ST1 (why is color gauged?)** → ADM-1: the local color frame is a gauge redundancy /
  no preferred frame (PR #3332, named premise).
- **ST2 (which gauge action?)** → is the gauge link a continuous diffusion with the
  canonical-Laplacian generator (PR #3339: the heat-kernel is the *unique* diffusion
  kernel among the candidates).

The retained `RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06` warns that *Record alone*
supplies no continuous Markov generator. **But the framework is discrete in time** —
emergent time is *accumulated record steps* — so the gauge link executes a **discrete
Markov walk** on the group, and its emergent-time (fine-resolution, many-step) propagator
is governed by the **convolution central limit theorem** on the group. That changes the
picture decisively.

## Verdict

**The heat-kernel weight is the *universal* convolution-CLT fixed point of bi-invariant
gauge-link dynamics, and bi-invariance is exactly ADM-1 — so a single open premise
forces both gates.** Concretely:

1. **Universality (the microscopic action-form ambiguity washes out).** For a group-valued
   degree of freedom (gauge link / plaquette holonomy) evolving by i.i.d. **bi-invariant**
   (Ad-invariant) Markov steps of small spread `ε`, the emergent-time-`t` propagator
   (`n = t/ε` steps) converges to the **heat kernel** `P_t = exp(tΔ/2)` — for *any*
   bi-invariant step distribution. The runner shows Wilson-, heat-kernel-, and
   Gaussian-(Manton-)type steps **all flow to the same heat kernel** (Part 2), with
   convergence improving as `ε→0` (the diffusion limit). The Wilson/HK/Manton ambiguity
   the action-form no-go could not resolve **dissolves under emergent-time coarse-graining**.

2. **Bi-invariance is load-bearing (Part 3, teeth).** A non-central (drifted) step has a
   non-scalar group-Fourier matrix and does **not** flow to the heat kernel; only
   bi-invariant steps do. Bi-invariance = *no preferred color frame* = **ADM-1**.

3. **Generator uniqueness (Part 4).** On a simple compact group the only Ad-invariant
   second-order generator is `c·Δ` (the Casimir), and bi-invariance kills the drift. So
   the CLT limit is the heat semigroup, with **only the rate `c` free** — and the rate is
   the `g_bare=1`/`β=6` scale (retained convention).

## The unification (the design payoff)

```
   ADM-1  (no preferred color frame)
     │  ⇒  the gauge-link update cannot single out a color direction
     ▼
   bi-invariant (Ad-invariant) Markov update
     │  ⇒  convolution CLT on the group (Parts 1–5)
     ▼
   emergent-time gauge weight = HEAT KERNEL  (ST2 action form)
```

The *same* premise (ADM-1, no preferred color frame) that **gauges color (ST1)** also
**forces the emergent heat-kernel action (ST2)**. The interacting foundation's two gates
collapse to **one open input** — the color-frame gauge redundancy (ADM-1 = the open
color-Record gate) — rather than two separate admissions. This is the program's
consolidation made into a theorem: close ADM-1 and *both* gates close together.

This also sharpens PR #3339: that note proved the heat-kernel is the *unique* convolution
**semigroup** (the fixed object); this note proves it is the *universal* **attractor** —
every bi-invariant microscopic dynamics flows to it — so the selection is robust, not a
knife-edge.

## What this does NOT claim (named residuals)

- **ADM-1 / bi-invariance itself is NOT derived.** It is the open color-Record gate (PR
  #3332; today's `RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE` records the same gate for
  κ_EW). This note *reduces both gates to it*, it does not close it.
- **The rate `ε`** (overall emergent-time scale) is the `g_bare=1`/`β=6` convention, not
  supplied (consistent with the retained semigroup boundary).
- **The i.i.d. step homogeneity** (emergent-time stationarity) is a structural input.
- **Scope:** this fixes the *single group-valued weight* (the action **form** — the
  per-link/per-plaquette-holonomy weight). The **inter-link spatial coupling** (the full
  Yang–Mills interaction) is a separate matter, not addressed here.
- No new axiom or import: the convolution CLT on compact groups, characters, and Casimirs
  are standard math; the open premise is named, not assumed as background.

## What the runner verifies (`PASS=15 FAIL=0`)

Part 1 (bi-invariant ⇒ Casimir-form coefficient); Part 2 (CLT universality: HK/Wilson/
Gauss → same heat kernel; ε→0 convergence); Part 3 (teeth: central → scalar Fourier matrix
→ heat kernel, drifted → non-scalar → not); Part 4 (Casimir Ad-invariant, no drift); Part 5
(SU(3) cross-check, reproduces `exp(−2/3)`); Part 6 (unification + residuals).

## Path forward (the design problem)

The whole interacting-gauge foundation now funnels through **one** question: *is the
gauge-link emergent-time update bi-invariant (no preferred color frame)?* That is ADM-1,
the color-Record gate. Routes: (a) the einselection/decoherence derivation that the
RECORD axiom disclaims (G4-open) supplying a *gauge-invariant* pointer partition; (b) a
first-principles argument that one-qubit-per-site locality + the commutant fibre leave no
frame for the update to prefer. Either closes ST1 **and** ST2 at once.

## Cross-references

- The semigroup boundary (retained): [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
- The action-form ambiguity this dissolves: [`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md)
- The color fibre = commutant (retained): [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- Program companions: PR #3332 (ADM-1 / minimal coupling), PR #3339 (HK = unique diffusion kernel), PR #3341 (continuum = IR-emergence)
- Standard method (not imports): central limit theorem for convolutions on compact Lie groups (Heyer, *Probability Measures on Locally Compact Groups*; Liao, *Lévy Processes in Lie Groups*); heat kernel on compact groups.
