# Velocity RG Gauge Tensor Block, Exact Lattice WTI, And Xi-Affine Drag: Exact Support

**Date:** 2026-07-17
**Claim type:** bounded_theorem
**Type:** exact support theorem / upstream support (exact tier + labeled finite-grid witness tier)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py`](../scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py)
**Cached runner output:**
[`logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.txt`](../logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.txt)

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "Exact gauge tensor block, exact lattice WTI, exact xi-affinity of the one-loop rainbow drag, and the exact tadpole closed form (1 - xi)(C_s - C_t); finite-grid one-loop witnesses for BOTH positive mutual-drag signs (a,b > 0) in one functional-integral convention, with the total xi-slope witnessed shrinking toward zero in the small-probe limit. Continuum limits, physical magnitudes, the spatial mixing coefficient, and LV sufficiency remain open."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This supplies finite-grid sign witnesses and exact algebraic support for the velocity-RG chain. It does not derive continuum one-loop coefficients or the downstream LV comparison."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target And Blocker

This note targets the named residual of
`emergent_lorentz_velocity_rg_exchange_matrix_exact_support_note_2026-06-18`
(all chain rows cited here are unaudited and are cited as surfaces, not as
retained authorities). That note's import ledger names, verbatim:

```text
| Positive mutual-drag coefficients `a,b` | Load-bearing attraction condition | open physical loop input | named residual |
```

and its "What Remains Open" asks for a framework-specific one-loop
calculation that "instantiate[s] positive `a,b` in this exact exchange
matrix." The parent conditional row is
`emergent_lorentz_interacting_velocity_rg_attractor_note_2026-06-06`; the
adjacent chain surfaces are
`velocity_rg_logflow_framework_internal_2026-06-21` and
`velocity_rg_gauge_seagull_transverse_vacuum_polarization_2026-06-22`
(whose seagull-runner conventions this runner adopts and re-certifies
internally).

This note supplies: (exact tier) the gauge quadratic form, its xi-family
closed inverse, the lattice Ward-Takahashi identity with anisotropic
velocities, the exact xi-affinity of the one-loop rainbow drag response
with a WTI-derived slope, and the exact tadpole closed form
`(out_s - out_t)_tad = (1 - xi)(C_s - C_t)`; (witness tier) finite-grid
one-loop witnesses that BOTH mutual-drag coefficients are positive in ONE
Euclidean functional-integral convention, so the exchange-matrix
difference mode contracts, plus a witness that the TOTAL drag's xi-slope
shrinks toward zero in the small-probe limit. It does not derive
continuum coefficients, the spatial-only power-divergent mixing
coefficient, the fixed-point anomalous dimension, or LV-bound sufficiency.

## Statement

**Exact tier (machine precision on the stated finite objects):**

1. Gauge tensor block: plaquette quadratic form `== K delta - qhat qhat^T`
   (link-midpoint), exact zero mode, exact xi-family closed inverse;
   `tr(T^a T^b) = delta^{ab}/2`.
2. Exact lattice WTI with anisotropic velocities; midpoint vertex is the
   Ward-exact vertex (control violates).
3. The one-loop RAINBOW drag response `a_rb(xi)` is EXACTLY affine in the
   covariant gauge parameter over `xi in {0, 0.5, 1.0, 1.7}` (deviation
   < 1e-11), and its xi-slope equals a WTI-derived longitudinal closed
   form assembled WITHOUT vertex functions (< 1e-10). The same-order
   fermion-line seagull TADPOLE has the exact closed form
   `(out_s - out_t)_tad = (1 - xi)(C_s - C_t)` (probe-independent;
   deviation < 1e-11), so its xi-slope is `-(C_s - C_t)`. The sign of the
   TOTAL drag `a_rb(xi) + a_tad(xi)` is xi-robust across the family.

**Witness tier (labeled finite-grid one-loop witnesses; no continuum
claim):**

4. As the probe momentum `delta -> 0`, the RAINBOW xi-slope approaches
   `+(C_s - C_t)`, a PURE gauge-line integral (rel. 5e-3 at
   `delta = 0.05`); `C_s`, `C_t` individually still grow at `N = 24`
   (log-divergent pieces) while the difference's increments shrink
   through `N = 24` (`+0.000823`, last increment 0.3% of the value) — a
   finite-grid convergence witness for the split.
5. The xi-shift of the rainbow response is constant-dominated over the
   log/const fit window (log-coefficient shift 11% of the constant
   shift), the per-delta rainbow xi-slopes approach the V4 constant
   monotonically, and the TOTAL xi-slope (rainbow plus tadpole) shrinks
   toward zero through the probe ladder (`+0.000127 -> +0.000018`
   against the scale `C_s - C_t = +0.000797`): the physical drag loses
   its xi-dependence in the small-probe limit.
6. Drag directions, both sectors, one convention:
   gauge sector faster (`dv_B = +0.05`) gives fermion response
   `dv_F = +0.00098 g^2` (POSITIVE: dragged toward the gauge speed;
   kinetic split: rainbow `-0.00210`, tadpole `+0.00080`, total
   `-0.00131`, and `dv_F = -g^2 C_F` times the total);
   fermion sector faster (`dv_F = +0.105`) gives gauge response
   `dv_B = +0.03017 g^2` (POSITIVE: dragged toward the fermion speed).
   In the exchange-matrix convention this witnesses `a > 0` AND `b > 0`:
   `a`-proxy `= +0.0196 g^2`, `b`-proxy `= +0.2866 g^2`, difference-mode
   contraction rate `a + b = +0.3062 g^2` (eigenstructure
   `{0, -(a+b)}` with common-speed null direction `(1,1)` checked
   exactly). Magnitudes are finite-grid scheme proxies (probe and
   deformation conventions stated in the runner); the SIGNS are the
   witnessed content.
7. Robustness proxies: drag sign and magnitude stable `N = 10 -> 12` at
   all four probe deltas (at `xi = 1` the tadpole split vanishes, so
   this checks the total); TOTAL fermion drag (rainbow plus tadpole)
   sign stable and monotone under halving the gauge deformation
   (`-0.00131 -> -0.00066`).

## Sign Chain: One Functional Integral, Both Sector Signs

All two-point objects below are reconstructions (calculational devices of
the finite-lattice Euclidean calculus), not registered content. The single
convention input is the Euclidean weight on the finite lattice:

```text
Z = Int dA dpsibar dpsi exp( -S_G[A] - psibar Dslash[A] psi ),
```

with `S_G` the Wilson plaquette action at quadratic (abelianized) level and
`Dslash[A]` the midpoint-gauged anisotropic kernel (velocities `v_mu`;
one-gluon vertex `v_mu cos(k_mu + q_mu/2)`; seagull `-v_mu sin(k_mu)`).
Everything downstream is mechanical:

- **Gauge quadratic form (exact, V1).** The plaquette action on the mode
  `A_mu(x) = Re[eps_mu e^{i q.(x + e_mu/2)}]` equals
  `(1/2) eps M eps` with `M = K delta - qhat qhat^T`, `qhat = 2 sin(q/2)`,
  `K = sum qhat^2` — EXACTLY, by direct lattice sum (link-midpoint
  convention; the site-centered half-shift candidate misses the closed
  form at the 5.6e-2 level, so between the two stated candidates the
  control selects link-midpoint). `M qhat = 0` exactly (gauge orbit), and
  the xi-family fixed form has the exact closed inverse
  `(M + xi^-1 qhat qhat^T)^-1 = P_T/K + xi qhat qhat^T/K^2`.
- **Ward identity (exact, V2).** The midpoint vertex satisfies
  `khat.Gamma(p, p-k) = S0^-1(p) - S0^-1(p-k)` exactly, INCLUDING
  anisotropic `v_mu` (a no-half-shift control violates it at O(1)).
- **Fermion sector sign.** Expanding the interacting propagator gives, at
  the same second order, TWO connected insertions: the RAINBOW (one-gluon
  exchange) and the fermion-line seagull TADPOLE, `S^-1 = S0^-1 - Sigma`
  with `Sigma = Sigma_rb + Sigma_tad`. The tadpole's kinetic split has
  the exact closed form `(out_s - out_t)_tad = (1 - xi)(C_s - C_t)`
  (probe-independent; V3), so its xi-slope `-(C_s - C_t)` cancels the
  rainbow's small-probe xi-slope `+(C_s - C_t)` (V4/V5). Near the probe
  the kinetic coefficients read `v_mu -> v_mu - g^2 C_F out_mu` (linear
  in `v`), so with `v_F = v_s/v_t` the drag response is
  `dv_F = -g^2 C_F (out_s - out_t)`, `C_F = 3/4` (su(2) fundamental).
- **Gauge sector sign.** Integrating the fermions exactly:
  `det Dslash = e^{+tr log Dslash}`, so
  `S_eff[A] = S_G[A] - tr log Dslash[A]`. The second variation of
  `-tr log Dslash` gives `Pi_munu = tr[S V_mu S V_nu] - delta_munu
  tr[S d2D]` (bubble plus seagull, the signs coded in the runner; color
  trace supplies `T_F = 1/2`). Hence `Gamma_2 = M/g^2 + Pi`: the fermion
  loop ADDS to the gauge kernel. The transverse weights read
  `c_mu = w_mu + g^2 Pi_T/qhat^2` and `v_B = sqrt(c_s/c_t)`, so
  `dv_B = +g^2 (Pi_T,s - Pi_T,t)/2` per unit `qhat^2`. The runner
  re-certifies that the deformed-kernel `Pi` is transverse to the stated
  proxy tolerance (normalized Ward residuals < 0.05 at both probes),
  which is what licenses reading a single transverse coefficient at this
  grid size.

Both sector signs therefore come from the SAME integral. The gauge
quadratic form is positive on the transverse sector, so the weight
orientation is not a free dial; the remaining naming freedoms — the
joint rephasing `A -> -A`, `g -> -g`, and where the minus sign is placed
in the definition of `Sigma` — leave every O(g^2) observable, in
particular both relative drag signs, invariant. The drag DIRECTIONS
(toward each other or away from each other) are the physical content.

## What This Supplies

The exchange-matrix note states: for ANY positive pair `a, b > 0` the
speed-difference mode contracts at rate `a + b`. Its named residual was
the positivity itself — "open physical loop input." This note supplies
finite-grid one-loop witnesses for both signs from the chain's own
reconstruction objects (midpoint-gauged anisotropic kernel, Wilson
quadratic form — the unaudited action surface restated and re-certified
here), in one functional-integral convention whose residual naming
freedoms are checked drag-sign-invariant, plus the exact algebraic
scaffolding (tensor block, WTI, rainbow xi-affinity, tadpole closed form)
that makes the witness gauge-parameter-robust rather than a single-gauge
accident.

The next path this opens: with both signs witnessed and the TOTAL drag's
xi-slope witnessed shrinking toward zero in the small-probe limit
(gauge-parameter independence of the physical drag, at finite grid), the
remaining physical inputs for the parent row are magnitude-level
(continuum extrapolation of `a, b`, the spatial-only power-divergent
mixing coefficient, the fixed-point anomalous dimension, and the LV-bound
sufficiency comparison).

## What Remains Open

- Continuum limits: all loop integrals are finite-grid
  (`N <= 12` fermion-loop, `N <= 24` gauge-line); magnitudes are scheme
  proxies at stated probes (`delta = 0.30`, `q = 0.3`,
  `eps in {0.05, 0.10}`). No continuum coefficient is claimed.
- One-loop (rainbow plus fermion-line tadpole) at quadratic (abelianized)
  gauge level with su(2) color factors; full nonabelian self-interactions
  are not included.
- Each sector's response is computed against a fixed deformed background
  for the other sector (consistent at one loop); no self-consistent
  coupled flow is solved here.
- The parent row's other repair items — the spatial-only power-divergent
  mixing coefficient and the anomalous-dimension/LV-bound sufficiency
  comparison — are untouched.
- The speed identifications `v_F = v_s/v_t` (linear kinetic coefficients)
  and `v_B = sqrt(c_s/c_t)` (quadratic kernel weights) are definitions of
  the finite-lattice reconstruction, disclosed as such.

## Import Ledger

| Input | Role | Class | Disposition |
|---|---|---|---|
| Euclidean weight `e^{-S}` on the finite lattice | fixes BOTH sector signs at once | reconstruction-calculus definition (no new axiom) | disclosed |
| Wilson quadratic level + midpoint gauging | action surface of the chain under test | stated by unaudited chain rows; restated and re-certified internally here (no chain row consumed as an authority; deps intentionally empty) | disclosed |
| su(2) factors `C_F = 3/4`, `T_F = 1/2` | group normalization | exact arithmetic | discharged by runner |
| Positive mutual drag `a, b > 0` | the exchange-matrix note's named residual | finite-grid one-loop sign witnesses, both sectors (rainbow plus tadpole totals) | not discharged; finite-grid sign witnesses only; continuum and framework-level positivity open |
| Physical magnitudes of `a, b` | downstream quantitative input | finite-grid scheme proxies only | named residual |
| Spatial mixing coefficient; anomalous dimension; LV sufficiency | parent-row remaining items | open bridge | not addressed |

## Verification

Run:

```bash
python3 scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py
```

Expected final line:

```text
TOTAL: PASS=24 FAIL=0
```

## Audit Boundary

This note does not run audit, set audit status, or promote any chain row.
It is an exact-support artifact plus labeled finite-grid witnesses for one
named residual. Independent review and audit must decide whether it can
serve as a one-hop authority in the velocity-RG chain.
