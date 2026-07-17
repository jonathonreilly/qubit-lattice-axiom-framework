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
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "Exact gauge tensor block, exact lattice WTI, exact xi-affinity of the one-loop rainbow drag over a DECLARED gauge-line family D_w(xi), and the exact tadpole closed form (1 - xi)(C_s - C_t); finite-grid one-loop STATIC-RESPONSE sign witnesses that BOTH mutual-drag PROXIES are positive (a-proxy, b-proxy > 0) in one shared formal sign-bookkeeping convention carried by two proxy reconstructions, with the total xi-slope witnessed decreasing strictly through the sampled probe ladder (family-internal trend; no limit claim). The signs of the physical RG coefficients a, b, the anisotropic-inverse gauge line, RG-coefficient extraction, continuum limits, physical magnitudes, the spatial mixing coefficient, and LV sufficiency remain open."
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
closed inverse (isotropic weights), the lattice Ward-Takahashi identity
with anisotropic velocities, the exact xi-affinity of the one-loop
rainbow drag response over a DECLARED anisotropic gauge-line family
`D_w(xi)` with a WTI-derived slope, and the exact tadpole closed form
`(out_s - out_t)_tad = (1 - xi)(C_s - C_t)`; (witness tier) finite-grid
one-loop STATIC-RESPONSE sign witnesses that BOTH mutual-drag proxies are
positive in one shared formal sign-bookkeeping convention (carried by TWO
proxy reconstructions — see the Sign Chain section), so the
exchange-matrix difference mode contracts in the proxy algebra, plus a
witness that the TOTAL drag's xi-slope decreases strictly through the
sampled probe ladder (family-internal trend; no limit claim). It does
not derive the anisotropic-inverse gauge line, RG beta-function
coefficients (in particular, the SIGNS of the physical RG coefficients
`a, b` remain open — only fixed-probe proxy signs are witnessed),
continuum coefficients, the spatial-only power-divergent
mixing coefficient, the fixed-point anomalous dimension, or LV-bound
sufficiency.

## Statement

**Exact tier (machine precision on the stated finite objects):**

1. Gauge tensor block: plaquette quadratic form `== K delta - qhat qhat^T`
   (link-midpoint), exact zero mode, exact xi-family closed inverse;
   `tr(T^a T^b) = delta^{ab}/2`.
2. Exact lattice WTI with anisotropic velocities; midpoint vertex is the
   Ward-exact vertex (control violates).
3. The drag integrals use the DECLARED anisotropic gauge-line family
   `D_w(xi)_munu = (delta_munu - (1 - xi) qhat_mu qhat_nu / K_w) / K_w`,
   `K_w = sum_mu w_mu qhat_mu^2`: equal to the item-1 closed inverse at
   `w = 1` for `xi > 0` (at `xi = 0` it is the Landau-limit pseudoinverse
   `P_T/K`, not the ordinary inverse tested in item 1), but for `w != 1`
   NOT transverse (`qhat^T D_w(0) != 0`) and
   NOT the inverse of an anisotropic Wilson tensor — a declared
   definition, disclosed in the import ledger. Over this family the
   one-loop RAINBOW drag response `a_rb(xi)` is EXACTLY affine in the
   gauge parameter over `xi in {0, 0.5, 1.0, 1.7}` (deviation < 1e-11),
   and its xi-slope equals a WTI-derived longitudinal closed form
   assembled WITHOUT vertex functions (< 1e-10). The same-order
   fermion-line seagull TADPOLE has the exact closed form
   `(out_s - out_t)_tad = (1 - xi)(C_s - C_t)` (probe-independent;
   deviation < 1e-11), so its xi-slope is `-(C_s - C_t)`. The sign of the
   TOTAL drag `a_rb(xi) + a_tad(xi)` is xi-robust across the SAMPLED
   WINDOW `xi in [0, 1.7]` (family-internal statement; the affine total
   crosses zero near `xi ~ 26`, far outside the sampled window, so no
   all-xi sign claim is made).

**Witness tier (labeled finite-grid one-loop witnesses; no continuum
claim):**

4. At the smallest sampled probe `delta = 0.05`, the RAINBOW xi-slope is
   within rel. `5e-3` of `+(C_s - C_t)`, a PURE gauge-line integral (no
   `delta -> 0` limit claim); `C_s`, `C_t` individually still grow at `N = 24`
   (log-divergent pieces) while the difference's increments shrink
   through `N = 24` (`+0.000823`, last increment 0.3% of the value) — a
   finite-grid convergence witness for the split.
5. The xi-shift of the rainbow response is constant-dominated over the
   log/const fit window (log-coefficient shift 11% of the constant
   shift; the log/const split is a fit-pivot-dependent diagnostic, not
   an extracted RG coefficient), the per-delta rainbow xi-slopes
   approach the V4 constant monotonically through the sampled ladder,
   and the TOTAL xi-slope (rainbow plus tadpole) decreases strictly
   through the four sampled probes (`+0.000127 -> +0.000018` against
   the scale `C_s - C_t = +0.000797`): a family-internal xi-robustness
   TREND witness (finite samples; no `delta -> 0` limit claim).
6. Drag directions, both sectors, one shared sign-bookkeeping convention
   (finite-grid STATIC
   self-energy responses at fixed probes — direction proxies, NOT RG
   beta-function coefficients; no shell derivative, counterterm split,
   or log-coefficient extraction is performed):
   gauge sector faster (exact offset
   `dv_B = sqrt(1.05/0.95) - 1 = +0.05131`) gives fermion response
   `dv_F = +0.00098 g^2` (POSITIVE: dragged toward the gauge speed;
   kinetic split: rainbow `-0.00210`, tadpole `+0.00080`, total
   `-0.00131`, and `dv_F = -g^2 C_F` times the total; `C_F = 3/4`
   discharged in-runner from the su(2) generator algebra);
   fermion sector faster (`dv_F = +0.10526`) gives gauge response
   `dv_B = +0.03017 g^2` (POSITIVE: dragged toward the fermion speed).
   In the exchange-matrix convention this supplies fixed-probe
   PROXY-SIGN support: `a`-proxy `= +0.0191 g^2 > 0` and
   `b`-proxy `= +0.2866 g^2 > 0`, difference-mode
   contraction rate `(a+b)`-proxy `= +0.3057 g^2` (eigenstructure
   `{0, -(a+b)}` with common-speed null direction `(1,1)` checked
   exactly on the proxy matrix). Magnitudes are finite-grid scheme
   proxies (probe and deformation conventions stated in the runner); the
   PROXY signs are the witnessed content, and the signs of the physical
   RG coefficients `a, b` remain open.
7. Robustness proxies: drag sign and magnitude stable `N = 10 -> 12` at
   all four probe deltas (at `xi = 1` the tadpole split vanishes, so
   this checks the total); TOTAL fermion drag (rainbow plus tadpole)
   sign stable and monotone under halving the gauge deformation
   (`-0.00131 -> -0.00066`).

## Sign Chain: Shared Sign Bookkeeping, Both Sector Signs

All two-point objects below are reconstructions (calculational devices of
the finite-lattice Euclidean calculus), not registered content. The shared
sign-bookkeeping input is the Euclidean weight on the finite lattice:

```text
Z = Int dA dpsibar dpsi exp( -S_G[A] - psibar Dslash[A] psi ),
```

with `S_G` the Wilson plaquette action at quadratic (abelianized) level and
`Dslash[A]` the midpoint-gauged anisotropic kernel (velocities `v_mu`;
one-gluon vertex `v_mu cos(k_mu + q_mu/2)`; seagull `-v_mu sin(k_mu)`).
Everything downstream is mechanical:

- **Gauge quadratic form (exact, V1).** The plaquette action on the mode
  `A_mu(x) = Re[eps_mu e^{i q.(x + e_mu/2)}]` equals
  `(V/4) eps^T M eps` (with `V = N^4` the site count; the `V/4` carries
  the quadratic-expansion `1/2` times the `Re[]` mode-average `V/2`, as
  coded in the runner — valid for non-self-conjugate modes
  `q != -q mod 2pi`, the modes the runner samples; self-conjugate modes
  carry twice this) with `M = K delta - qhat qhat^T`, `qhat = 2 sin(q/2)`,
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
  with `Sigma = Sigma_rb + Sigma_tad`. The gauge line inside both is the
  DECLARED family `D_w(xi)` of the Statement (item 3): at the deformed
  weights `w != 1` it is a declared definition, NOT the inverse of an
  anisotropic Wilson tensor, and NOT the covariance of any positive
  Euclidean weight (`D_w(0)` has a negative eigenvalue at some momenta
  for `w != 1`), so every xi-statement in this chain is
  family-internal. The tadpole's kinetic split has
  the exact closed form `(out_s - out_t)_tad = (1 - xi)(C_s - C_t)`
  (probe-independent; V3), so its xi-slope `-(C_s - C_t)` near-cancels
  the rainbow's smallest-sampled-probe xi-slope, gated in-runner within
  rel. `5e-3` of `+(C_s - C_t)` at probe `delta = 0.05` (V4/V5;
  finite-probe witness, no `delta -> 0` limit claim).
  Near the probe
  the kinetic coefficients read `v_mu -> v_mu - g^2 C_F out_mu` (linear
  in `v`), so with `v_F = v_s/v_t` the drag response is
  `dv_F = -g^2 C_F (out_s - out_t)`, `C_F = 3/4` (su(2) fundamental,
  discharged in-runner from the generator algebra).
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

Both sector SIGN proxies therefore share one formal sign bookkeeping,
carried by TWO proxy reconstructions: the fermion-sector proxy from the
expansion of `e^{-S}` with the gauge line replaced by the declared
family `D_w(xi)`, and the gauge-sector proxy from `-tr log Dslash`
against the deformed kernel. (This is a shared-bookkeeping statement,
not a claim that one established functional integral produces both — at
`w != 1` the declared family is not the covariance of any positive
Euclidean weight.) The `w = 1` gauge quadratic form is positive
on the transverse sector, so the weight orientation is not a free dial;
the remaining naming freedoms — the joint rephasing `A -> -A`,
`g -> -g`, and where the minus sign is placed in the definition of
`Sigma` — leave every O(g^2) observable, in particular both relative
drag signs, invariant. The drag DIRECTIONS (toward each other or away
from each other) are the witnessed content at the stated finite grids.

## What This Supplies

The exchange-matrix note states: for ANY positive pair `a, b > 0` the
speed-difference mode contracts at rate `a + b`. Its named residual was
the positivity itself — "open physical loop input." This note supplies
finite-grid one-loop STATIC-RESPONSE sign witnesses for both proxies
from the chain's own reconstruction objects (midpoint-gauged anisotropic
kernel, Wilson quadratic form — the unaudited action surface restated
and re-certified here), in one shared sign-bookkeeping convention
(carried by two proxy reconstructions) whose residual naming freedoms
are checked drag-sign-invariant, plus the exact algebraic scaffolding
(tensor block, WTI, rainbow xi-affinity over the declared gauge-line
family, tadpole closed form) that makes the witness xi-robust within
the sampled window `xi in [0, 1.7]` of that declared family rather than
a single-gauge accident. The signs of the physical RG coefficients
`a, b` and physical gauge independence proper (the anisotropic-inverse
gauge line) are named open below.

The next path this opens: with both static-response signs witnessed and
the TOTAL drag's xi-slope witnessed decreasing strictly through the
sampled probe ladder (a family-internal xi-robustness trend at finite
grid), the remaining physical inputs for the parent row are (i) the
anisotropic-inverse gauge line (replacing the declared family with the
true inverse of the deformed Wilson tensor), (ii) RG-coefficient
extraction (shell derivative / log-coefficient), and (iii)
magnitude-level items (continuum extrapolation of `a, b`, the
spatial-only power-divergent mixing coefficient, the fixed-point
anomalous dimension, and the LV-bound sufficiency comparison).

## What Remains Open

- Continuum limits: all loop integrals are finite-grid
  (`N <= 12` fermion-loop, `N <= 24` gauge-line); magnitudes are scheme
  proxies at stated probes (`delta = 0.30`, `q = 0.3`,
  `eps in {0.05, 0.10}`). No continuum coefficient is claimed.
- The anisotropic gauge line is the DECLARED family `D_w(xi)` (the
  isotropic transverse-tensor FORM with `K` replaced by `K_w`; not a
  projector for `w != 1`): for `w != 1` it is not transverse, not the
  inverse of an anisotropic Wilson tensor, and not the covariance of any
  positive Euclidean weight. Re-deriving the drag from the
  true deformed-tensor inverse — and hence physical gauge independence
  proper — is open.
- The V6 witnesses are STATIC self-energy responses at fixed probes, not
  RG beta-function coefficients; no shell derivative, counterterm split,
  or log-coefficient extraction is performed. The V5 log/const split is
  a fit-pivot-dependent diagnostic.
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
| Euclidean weight `e^{-S}` on the finite lattice | shared sign bookkeeping for both sector proxies (carried by two proxy reconstructions; not one established functional integral producing both) | reconstruction-calculus definition (no new axiom) | disclosed |
| Wilson quadratic level + midpoint gauging | action surface of the chain under test | stated by unaudited chain rows; restated and re-certified internally here (no chain row consumed as an authority; deps intentionally empty) | disclosed |
| su(2) factors `C_F = 3/4`, `T_F = 1/2` | group normalization | exact arithmetic; `C_F` computed in-runner from `sum_a T^a T^a = C_F I` | discharged by runner |
| Anisotropic gauge-line family `D_w(xi)` (isotropic transverse-tensor form over `K_w`; not a projector for `w != 1`) | drag propagator in all V3-V7 integrals | declared definition; equals the exact closed inverse at `w = 1` for `xi > 0`; NOT the deformed-tensor inverse for `w != 1`; `D_w(0)` not positive semidefinite for `w != 1` | disclosed; anisotropic-inverse route named open |
| Half-integer BZ grid `k = ((n + 1/2)/N) 2 pi - pi` | zero-mode-avoiding loop discretization | stated sampling convention | disclosed |
| Positive mutual drag `a, b > 0` | the exchange-matrix note's named residual | finite-grid one-loop PROXY sign witnesses, both sectors (rainbow plus tadpole totals) | not discharged; finite-grid PROXY sign witnesses only; physical RG-coefficient signs, continuum, and framework-level positivity open |
| Physical magnitudes of `a, b` | downstream quantitative input | finite-grid scheme proxies only | named residual |
| Spatial mixing coefficient; anomalous dimension; LV sufficiency | parent-row remaining items | open bridge | not addressed |

## Verification

Run:

```bash
python3 scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py
```

Expected final line:

```text
TOTAL: PASS=25 FAIL=0
```

## Audit Boundary

This note does not run audit, set audit status, or promote any chain row.
It is an exact-support artifact plus labeled finite-grid witnesses for one
named residual. Independent review and audit must decide whether it can
serve as a one-hop authority in the velocity-RG chain.
