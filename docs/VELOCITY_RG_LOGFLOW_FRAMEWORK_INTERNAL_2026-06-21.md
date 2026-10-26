# Supplied Wilson/Staggered Symbols: Finite IR/UV Proxy Comparison

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

## Supplied model and scope

This note checks an internal-line average proxy, not a physical one-loop drag
coefficient. The Wilson symbol in the corrected T1 parent is supplied. Neither
that integral nor a group-space heat kernel selects it from substrate axioms.
The earlier physical log-flow corroboration and power-divergent `f0` route no-go
are withdrawn. Registered primitive and audit statuses are unchanged.

The supplied four-dimensional symbols are
`D_g(k)=Σμ(2−2cos kμ)` and `D_f(k)=m²+Σμ sin² kμ`, with `m²=0` in the comparisons.
They are denominators, not full tensor propagators or self-energy integrands.
The runner separately verifies supplied SU(3) generator identities
`Σa TᵃTᵃ=(4/3)I`, `tr(TᵃTᵇ)=(1/2)δab`, and `fᵃcd fᵇcd=3δab`.
Those identities alone do not factor a physical amplitude into these proxies.

## Preserved finite calculations

Both symbols have leading `k²`: `2−2cos k=k²−k⁴/12+…` and
`sin² k=k²−k⁴/3+…`. The sampled axial ratios at `k=10⁻¹,…,10⁻⁴`
approach one. On the unchanged shifted `48⁴` mesh, region averages give
`⟨D_g⟩/⟨D_f⟩≈1.027` in `|k|<π/6`, approximately `4.03` in
`|k|≥π/2`, and `4` over the full BZ. The continuum uniform averages are
`⟨2−2cos⟩=2`, `⟨sin²⟩=1/2`. No quadrature error bound is supplied.
At each nonzero `{0,π}⁴` corner the supplied gauge symbol is nonzero
(minimum `4`) while the massless fermion symbol vanishes. Substituting the same
line into both averages returns ratio one. This localizes the **proxy** mismatch,
not all physical diagram contributions.

The runner also defines `gauge_line_HK` by the identical Wilson expression.
Its equality and UV-ratio checks therefore test a supplied common-symbol ansatz,
not an independent derivation of the native HK action. The truncated U(1)
Villain sum (`β=1.7`, `n=-50,…,50`, finite-difference step `10⁻⁴`) gives
curvature within `10⁻³` of β and the tested evenness. It does not prove exact
`S″(0)=β`: nonzero winding terms contribute, albeit very little here. Gauge
invariance and locality alone do not forbid further local higher-derivative
quadratic terms. A nearest-plaquette curl action is an additional premise.

## Conditional exchange flow and open physical obligations

For separately supplied positive constants `a,b`, the abstract exchange equations
`dv_F/dl=a(v_b−v_F)`, `dv_b/dl=b(v_F−v_b)` give a difference mode with
exponent `−(a+b)`. When the common limiting speed is nonzero this gives
`v_F/v_b→1`. The exact-support reference proves that conditional algebra.
This proxy does not derive the physical signs, magnitudes, or matching of `a,b`.
The previously imported log-flow form remains imported, not corroborated as a
framework physical prediction by these line averages.

A full gauge tensor propagator, gauge-fermion vertices, gamma traces and actual
loop integrals are still needed to determine the counterterm, power-divergent
coefficient λ, fixed point and anomalous dimension γ. The unequal proxy averages
do not exclude cancellations in those complete amplitudes. Neither a physical
`f0` no-go nor an `O(α/4π)` displacement or `~10⁻²⁰` sufficiency follows here.
The latter scales remain motivation from the parent discussion, not results.
The naturalness question and cross-sector physical identification stay open.

## Inputs

- [`EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`](EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md) — abstract exchange-matrix algebra for any positive `(a,b)`
- [`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md) — parent; the imported log-flow form + residual D
- [`EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`](EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md) — the A4 → c_s power-mixing channel
- [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md) — staggered fermion free propagator
- [`CLOSURE_T1_Z10_Z20_BZ_INTEGRALS_NOTE_2026-05-10_t1z10z20.md`](CLOSURE_T1_Z10_Z20_BZ_INTEGRALS_NOTE_2026-05-10_t1z10z20.md) — supplied four-dimensional Wilson symbol and numerical BZ estimate; no substrate selection
- [`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md`](HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md) — group-space heat-kernel context; does not select a spacetime free propagator

## Reproduce

```
python3 scripts/velocity_rg_logflow_framework_internal_2026_06_21.py
# expect: TOTAL: PASS=16 FAIL=0
```
