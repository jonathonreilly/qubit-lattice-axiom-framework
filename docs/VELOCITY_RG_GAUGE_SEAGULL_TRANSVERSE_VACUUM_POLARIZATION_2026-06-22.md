# Gauge-Sector Velocity Drag from the Seagull-Completed Transverse Vacuum Polarization

> **Key terms used in this doc** are indexed A–Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-22
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. Any `audit_status` and `effective_status` fields
are pipeline-derived.

**Primary runner:**
[`scripts/velocity_rg_gauge_seagull_transverse_vacuum_polarization_2026_06_22.py`](../scripts/velocity_rg_gauge_seagull_transverse_vacuum_polarization_2026_06_22.py)
**Cached runner output:**
[`logs/runner-cache/velocity_rg_gauge_seagull_transverse_vacuum_polarization_2026_06_22.txt`](../logs/runner-cache/velocity_rg_gauge_seagull_transverse_vacuum_polarization_2026_06_22.txt)

## What this is

Cross-sector front-speed alignment `v_fermion = v_gauge` is the last open residual
of emergent Lorentz invariance: `B4` does not cover it (the relative speed is a
free `B4` invariant), and the only handle is the velocity-RG mutual-drag flow. The
gauge half of that flow needs the one-loop gauge-boson vacuum polarization
`Pi_munu(q)` from the gauged staggered/Kähler-Dirac fermion loop. A bubble-only
assembly is **not transverse** (it leaves a lattice gluon-mass artifact); this
note adds the **two-gluon seagull tadpole**, which restores transversality, and
reads off the gauge-sector velocity coefficient.

This note does **not** amend, narrow, retire, or re-approve any registered
primitive (the kinetic-isotropy primitive is unchanged) or set any lane status. It
records framework-internal structural facts about the gauge-sector velocity drag
and an honest, sign-robust statement about cross-sector non-cancellation. Companion
to the landed velocity-RG log-flow note
[`VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md`](VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md)
(the shared-form-factor route no-go + log-flow positivity) and the landed
[`KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md`](KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md).

## Feynman rules (framework free propagators; gauged in the hopping)

Gauging `k_mu -> k_mu + A_mu` inside the staggered hopping `sin(k_mu)`:
- fermion line `Sf(k) = (-i sum_mu v_mu sin(k_mu) gamma_mu) / (sum_mu v_mu^2 sin^2 k_mu)`
- one-gluon vertex `D_mu(k->k+q) = i gamma_mu cos(k_mu + q_mu/2)`
- two-gluon seagull `D_munu = -i delta_munu gamma_mu sin(k_mu)`
- `Pi_munu(q) = Tr[Sf(k) D_mu Sf(k+q) D_nu] - Tr[Sf(k) D_munu]`, colour factor `T_F = 1/2`.

The vacuum polarization carries **no internal gauge line**, so `Pi` is gauge
(`xi`) independent; the gauge-sector coefficient read off from it is
gauge-invariant.

## Runner-Checked Facts (`PASS=7 FAIL=0`, memory-safe)

1. **Euclidean Clifford** `{gamma_mu, gamma_nu} = 2 delta_munu` (Hermitian set).
2. **Transversality from the seagull.** The lattice Ward identity
   `khat_mu Pi_munu` is satisfied to `< 2%` at `N=16` (violations
   `8.4e-4 … 7.1e-3`, finite-grid, vanishing in the continuum) — whereas the
   bubble-only assembly is `~20%` non-transverse. The seagull tadpole cancels the
   diagonal gluon-mass artifact.
3. **`B4` isotropy at `v=1`.** `Pi_T(temporal) = Pi_T(spatial)` to `8.5e-13` — the
   gauge sector is `B4`-isotropic at isotropic input (`c_t = c_s` protected).
4. **`eta = v_F/v_b = 1` is a fixed point.** The induced gauge anisotropy vanishes
   (`~1e-13`) at zero relative-anisotropy input.
5. **Gauge-sector finite-grid proxy `lambda_G > 0`.** With anisotropic input,
   the runner's finite-grid fit splits as `slope(q) = A_G log(1/q) + B_G` with
   `A_G > 0` (the IR velocity-RG attractor log) and `B_G = lambda_G > 0` (the
   gauge-side proxy for the power-divergent constant — residual D, gauge sector).
6. **Cross-sector non-cancellation (sign-robust).** The fermion-half velocity
   anisotropy has the **opposite** sign (negative) in **both** Feynman (`xi=1`)
   and Landau (`xi=0`) gauge, while `lambda_G > 0`. The bare fermion-velocity
   *magnitude* is gauge-dependent, but its *sign* is gauge-robust, so the two
   sectors **add** in the net relative-velocity drag — they do not cancel.

## Consequence

`eta = 1` is a fixed point in the checked proxy, but it is **not protected by a
cancellation** in that proxy: the gauge-sector fitted `lambda_G` is positive, and
the fermion-sector sign adds with the same effect rather than cancelling it. So
the cross-sector relative-velocity coefficient (residual D) is a nonzero
finite-grid proxy obstruction — the naturalness issue is **quantified, not
closed**. The `~1e-20` Lorentz-violation scale is an external comparator for
context only, not a runner input or a fitted target.

## Honest boundary

- **Sign and structure, not the precise number.** The transversality, `B4`
  isotropy, fixed point, finite-grid `lambda_G > 0`, and sign-robust
  non-cancellation are the runner-checked content. The **precise net**
  coefficient needs a **gauge-invariant fermion-velocity prescription**: the bare
  self-energy `Z` is gauge-dependent (Feynman vs Landau differ), so the
  fermion-half magnitude is not fixed here — only its gauge-robust sign. That
  prescription is the named open item.
- **Proxy / normalization.** Magnitudes are at the structural/proxy level; the
  taste/doubler overall factor is a flagged normalization. The physical-magnitude
  conversion, anomalous dimension, and `(mu/M_Pl)^gamma` damping stay **open**.
- No new axioms or registered primitives are introduced. The gauge/fermion lines
  are the framework free-propagator setup used by the runner. The external
  Lorentz-violation scale is disclosed as context-only comparison, not as
  support for the bounded theorem.

## Reproduce

```
python3 scripts/velocity_rg_gauge_seagull_transverse_vacuum_polarization_2026_06_22.py
# expect: TOTAL: PASS=7 FAIL=0   (peak RSS ~180 MB, single process, chunked BZ loop)
```
