# V1-V5 Self-Grounding -- Block 15 (yt_boundary_theorem)

## V1: Definitions clear

All symbols are SM RGE outputs of the standard 5-channel 2-loop system:
`(g1, g2, g3, y_t, lambda)`. The map `Phi : [0.5, 1.2] -> R` is defined
operationally as

    Phi(X) = y_t(t_Pl) after integrating the SM RGE from t_v to t_Pl with
             initial condition (g1, g2, g3, y_t, lambda) = (g1_v, g2_v, G_S_V, X, LAMBDA_V).

All RGE inputs (G1_V, G2_V, G_S_V, LAMBDA_V) are computed from canonical-surface
constants in `canonical_plaquette_surface`. The threshold matching at
(M_T_POLE, M_B_MSBAR, M_C_MSBAR) is verbatim from
`scripts/frontier_yt_boundary_consistency.py`.

The Lipschitz constant `L_observed` is defined operationally as
`max_i |Phi(X_{i+1}) - Phi(X_i)| / |X_{i+1} - X_i|` over the working grid.
No additional Lipschitz machinery is invoked beyond this finite-difference
operational definition.

## V2: Inputs explicit

All inputs (I1)-(I5) are listed in the Inputs section of the note.
Critically:

- (I1, I2): EW couplings at v from 1-loop M_Z running. Used as fixed
  initial-condition surface; not derived in this block. Sourced from the
  standard SM EW running and consumed by all yt-lane runners on the canonical
  surface.
- (I3): `g_3(v) = sqrt(4 pi alpha_s(v))` with `alpha_s(v) = alpha_bare / u_0^2`
  from the Coupling Map Theorem (block 10 narrow). RETAINED CANONICAL SURFACE.
- (I4): SM 2-loop beta coefficients on `(g1, g2, g3, y_t, lambda)`. STANDARD
  SM RGE; coefficients reproduced verbatim from the parent
  `frontier_yt_boundary_consistency.py` runner.
- (I5): SM threshold matching at top/bottom/charm pole masses. STANDARD
  procedure.

No PDG observable is consumed by any LOAD-BEARING check. The runner does
print `m_t (obs) = 172.69 GeV` for context only; it is not consumed by any
of (T1)-(T5).

## V3: Each step verifiable

| Check | Method |
|---|---|
| (T1) globalness, max\|y_t\| bound | Sample max\|y_t\| on trajectory across 8-point X-grid; compare to X+0.05 bound |
| (T2) strict monotonicity | Compute Phi on 33-point grid; check all 32 forward differences > 0 |
| (T3) Lipschitz global | Finite-difference local L on 33-point grid; check max < 10 |
| (T3) Lipschitz near root | Finite-difference local L on 21-point grid in [0.9, 1.0]; check max < 1.5 |
| (T4) sign change | Verify Phi(X_LOW) < WARD_TARGET < Phi(X_HIGH) |
| (T4) brentq subinterval agreement | Run brentq on 3 different subintervals containing X*; verify roots agree to 1e-7 |
| (T4) X* value | Verify X* = 0.973 (to 5e-3) |
| (T5) Yukawa-Landau onset | Extension scan in [1.20, 1.30]; locate first X with Phi > 5 |
| step-size stability | Re-run brentq at max_step in {2.0, 1.0, 0.5, 0.2}; verify spread < 1e-5 |

All 23 checks PASS. No check uses an external observable. No check has a
hidden dependency on a fitted constant.

## V4: No hidden imports

Imports:
- `canonical_plaquette_surface` for `CANONICAL_ALPHA_BARE`, `CANONICAL_ALPHA_LM`,
  `CANONICAL_ALPHA_S_V`, `CANONICAL_PLAQUETTE`, `CANONICAL_U0`. These are
  retained canonical-surface constants on `main`.
- `numpy`, `scipy.integrate.solve_ivp`, `scipy.optimize.brentq`. Standard.

NO imports of:
- audit-data files (forbidden by hard rules)
- CANONICAL_HARNESS_INDEX, DERIVATION_ATLAS, DERIVATION_VALIDATION_MAP
- any PDG observable for load-bearing computation

## V5: Distinct from prior blocks

| Block | Target | Scope | This block's distinction |
|---|---|---|---|
| 08 | yt_vertex_power | n_link = 2 at vacuum-polarization vertex (operator-counting at LAGRANGIAN level) | This block is at RGE-trajectory level, consumes n_link=2 as input |
| 10 | alpha_s_derived | algebraic CMT-to-coupling-map identity (alpha_eff = alpha_bare / u_0^{n_link}) | This block is the 17-decade backward-RGE WELL-DEFINEDNESS, consumes alpha_s(v) as input |
| 11 | u_0_plaquette_quartic | 1/4 exponent from L = 4 plaquette length | This block does not touch u_0 exponent |
| 14 | yt_ward_identity_derivation | contact-4-fermion vanishing on Q_L | This block consumes the Ward identity as a cited boundary condition, asks about UNIQUENESS of the backward-extrapolation root |
| **15 (this)** | yt_boundary_theorem (sliced) | numerical well-definedness / monotonicity / no-blow-up / Lipschitz / unique-root of the BC-transfer MAP | No prior block touches the MATHEMATICAL WELL-DEFINEDNESS of the backward-RGE root-finder |

The map `Phi : y_t(v) -> y_t(M_Pl)` is a new object introduced in this block.
No prior runner computes monotonicity or Lipschitz of this map; no prior runner
proves the unique-root claim; no prior runner locates the Yukawa-Landau onset.

The parent `frontier_yt_boundary_consistency.py` runner finds the root via
brentq but does NOT prove uniqueness, does NOT compute Lipschitz, and does
NOT locate the Landau onset.
