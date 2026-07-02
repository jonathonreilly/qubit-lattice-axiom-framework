# Cross-Sector Velocity-RG: the Log-Flow Attractor is Framework-Internal; the Power-Divergent f0 Does Not Factorize (Heat-Kernel-Robust)

> **Key terms used in this doc** are indexed A–Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.

**Primary runner:**
[`scripts/velocity_rg_logflow_framework_internal_2026_06_21.py`](../scripts/velocity_rg_logflow_framework_internal_2026_06_21.py)
**Cached runner output:**
[`logs/runner-cache/velocity_rg_logflow_framework_internal_2026_06_21.txt`](../logs/runner-cache/velocity_rg_logflow_framework_internal_2026_06_21.txt)

## What this is (structural support + an f0-route no-go; NOT a closure of naturalness)

This note does **not** amend, narrow, retire, or re-approve any registered
primitive (the kinetic-isotropy primitive
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
is unchanged), and it does not set the status of the velocity-RG lane rows. It
records two narrow framework-internal facts: a **structural support** result (the
log-flow drag positivity is reproducible on the framework's own retained
propagators) and a **route no-go** (the `f0` shared-form-factor route does not
factorize for the power-divergent drag). It closes the `f0` route for that hard
part; it does not close the naturalness problem. Companion to the landed
[`KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md`](KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md).

Cross-sector front-speed alignment `v_fermion = v_gauge` is the last open
residual of emergent Lorentz invariance: the `B4` custodial symmetry does **not**
cover it (the relative speed `v_F/v_b` is a free `B4` invariant), and the only
handle is the velocity-RG mutual-drag flow
`dv_F/dl = a (v_b − v_F)`, `dv_b/dl = b (v_F − v_b)`, which gives `eta=v_F/v_b → 1`
for any `a,b > 0`. The exact-support note
[`EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`](EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md)
proves that algebra for **abstract** positive `(a,b)`; the positive log-flow form
`a = C_F α`, `b = C_B α N_f` in the parent
[`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
was **imported** from the literature (Chadha–Nielsen; graphene velocity-RG).

This note shows the log-flow positivity is reproducible **framework-internally**
on the framework's own retained free propagators, and that the **power-divergent**
residual D drag does **not** admit a common form factor `f0` — an honest negative
with an exact, heat-kernel-robust mechanism. It does **not** close the naturalness
problem.

## Setup: the f0 hypothesis reduces to the kinematic cores

Write each one-loop velocity-drag coefficient as `(group weight) × (kinematic BZ
form factor)`. The `f0`-factorization hypothesis is `a = f0 · C_F`,
`b = f0 · W_gauge`, i.e. a *common* kinematic core `f0` for both diagrams. The
internal lines (framework's own free propagators):

- gauge line (Wilson **and** heat-kernel — derived below): `D_g(k) = Σ_μ (2 − 2 cos k_μ)`
  — the lattice Laplacian (from `CLOSURE_T1_Z10_Z20`; heat-kernel generator =
  canonical group Laplacian, `HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL`).
- staggered/Kähler-Dirac fermion line: `D_f(k) = m² + Σ_μ sin² k_μ`
  (from `LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4`).

**Group weights factor exactly.** With SU(3) generators `T^a = λ^a/2`:
`Σ_a T^a T^a = (4/3) I` (`C_F`), `tr(T^a T^b) = (1/2) δ^{ab}` (`T_F`),
`f^{acd} f^{bcd} = 3 δ^{ab}` (`C_A`) — all to machine precision. So `a = C_F
f_a^kin`, `b = (T_F N_f) f_b^kin`, and the `f0` question is **purely** whether the
kinematic cores coincide, `f_a^kin = f_b^kin`.

## The result: log-flow YES, power-divergent NO

**Log-flow (soft / IR region): common form factor.** As `k → 0` both internal lines reduce to
`k²` (`2 − 2 cos k = k² − k⁴/12`, `sin² k = k² − k⁴/3`); the line ratio `D_g/D_f →
1` (verified `1.0025 → 1.0000` at `k = 10⁻¹ … 10⁻⁴`). The IR form-factor ratio
`⟨D_g⟩/⟨D_f⟩ = 1.027 → 1`. Both log-flow drag coefficients are positive, so the
difference-mode eigenvalue `−(a+b) < 0` and `eta → 1`. So the log-flow drag
positivity is **reproducible framework-internally** (structural, proxy-level —
see boundary), corroborating the previously-imported `a = C_F α`, `b = C_B α N_f`
positivity on the framework's own propagators rather than citing it from the
literature.

**Power-divergent (UV / BZ-edge region): no common form factor.** At the BZ edge the lines
**differ structurally**: the gauge line is `4` per direction (`2 − 2 cos π = 4`,
**no doubler zero**), while the staggered fermion line is `0` (`sin² π = 0`,
**doubler zeros**). Hence the UV form-factor ratio `⟨D_g⟩/⟨D_f⟩ = 4.03 ≠ 1`
(full-BZ exact value `⟨2−2cos⟩/⟨sin²⟩ = 2/0.5 = 4`). The fermion self-energy
(internal gauge line) and the gauge vacuum polarization (internal fermion lines)
are different 1PI topologies with structurally different BZ-edge integrands, so
`f0` does **not** factorize for the power-divergent residual D. A **line-swap**
control (use the *same* internal line in both) returns ratio `1` exactly,
proving the mismatch is purely the internal-line shape.

**Heat-kernel robustness of the gauge propagator (derived, not asserted).** The free gauge
propagator is the **quadratic** expansion of the single-plaquette action in `A`,
and gauge invariance + locality force that quadratic term to the **unique** local
invariant `tr(F_p²)` — the lattice **curl** — whose momentum structure is
`k̂² = Σ(2−2cos k_μ)`, *identical* for Wilson and heat-kernel; the action choice
sets only the overall coupling (the `4/3 = C_F` in `<P>_HK = 1−exp(−(4/3)s)` is
the Casimir in the *coupling*, not a momentum structure). Verified directly: the
U(1) heat-kernel/Villain plaquette action is `(β/2)θ_p²` at quadratic order
(`S''(0)=β`, even in `θ` — no doubler-inducing structure); the derived `k̂²`
denominator is **nonzero at every BZ-edge corner** `k ∈ {0,π}⁴∖{0}` (min `= 4`),
so there is **no doubler zero** (a gauge boson has a single pole at `k=0`),
whereas the staggered fermion line vanishes there. The UV form-factor ratio is
identical (`4.03`). So the power-divergent `f0`-negative is **action-robust** —
the generic "gauge bosons have no lattice doublers, staggered fermions do" fact,
not a bare-Wilson artifact, and it survives the framework's native HK gauge
action (`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL`; CLOSURE_T1 only uses bare Wilson
for tadpole/matching).

## Consequence

`eta = v_F/v_b → 1` holds in the IR (log-flow, framework-internal). But the
power-divergent residual D is **not** protected by a common-`f0` cancellation:
the two sectors regenerate the marginal `c_s` anisotropy at different
power-divergent rates with no symmetry forcing equality, so the fixed point is
generically shifted off `eta = 1` at the `O(α/4π)` level — vastly above the
`~10⁻²⁰` Lorentz-violation bound, bridged only conditionally by the
`(μ/M_Pl)^γ` damping. Closing it needs a cross-sector custodial symmetry or an
`O(1)` anomalous dimension the framework does not currently supply.

## Honest boundary

- **Support/reduction, not closure.** The naturalness problem (residual D's
  power-divergent coefficient `λ`, the fixed-point anomalous dimension `γ`, and
  the `~10⁻²⁰` LV-bound sufficiency) stays **open**.
- **Proxy-level drag.** The drag is computed via an anisotropy-weight / internal-
  line form-factor proxy, **not** a full off-shell self-energy (γ-traces, the
  gauge tensor `D_μν^{ab}`, vertices). The absolute `a,b` are proxy-level; the
  **ratio and its IR/UV split** — the binding claim — are robust because (i) the
  group weights factor exactly and (ii) the line-swap isolates the mismatch
  to the internal-line shape alone.
- **The named missing_bridge.** A full framework-internal one-loop counterterm
  (constructing the lattice gauge tensor propagator `D_μν^{ab}` and the
  gauge-fermion vertex, neither written in `docs/`) is the path to actually
  pinning `λ`; it is **not** delivered here.
- No new axioms, imports, or comparators are introduced; the gauge/fermion lines
  are the framework's own retained free propagators. The previously-imported
  log-flow form is now corroborated framework-internally.

## Inputs

- [`EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`](EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md) — abstract exchange-matrix algebra for any positive `(a,b)`
- [`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md) — parent; the imported log-flow form + residual D
- [`EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`](EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md) — the A4 → c_s power-mixing channel
- [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md) — staggered fermion free propagator
- [`CLOSURE_T1_Z10_Z20_BZ_INTEGRALS_NOTE_2026-05-10_t1z10z20.md`](CLOSURE_T1_Z10_Z20_BZ_INTEGRALS_NOTE_2026-05-10_t1z10z20.md) — lattice gauge propagator / BZ integration
- [`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md`](HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md) — HK generator = canonical group Laplacian

## Reproduce

```
python3 scripts/velocity_rg_logflow_framework_internal_2026_06_21.py
# expect: TOTAL: PASS=16 FAIL=0
```
