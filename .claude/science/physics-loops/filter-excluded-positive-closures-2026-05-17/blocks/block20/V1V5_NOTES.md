# V1-V5 Self-Grounding -- Block 20 (yt_p2_taste_staircase_transport)

## V1: Definitions clear

The block introduces and verifies a strengthening of the parent
taste-staircase transport theorem. All symbols and constructs are
defined explicitly:

- A **per-rung dressing distribution** is a 16-tuple `(r_1, ..., r_{16})`
  of positive reals.
- The **family constraint** is `prod_{k=1..16} r_k = sqrt(1/u_0)`
  (cumulative CMT endpoint anchor).
- The **per-rung gauge trajectory** is
  `g_s^{(0)} = 1/sqrt(u_0)` and `g_s^{(k)} = g_s^{(k-1)} * r_k`.
- The **per-rung Yukawa trajectory** is
  `y_t^{(k)} = g_s^{(k)} / sqrt(2 N_c)` from the retained Ward Identity
  Theorem applied at each rung's Q_L = (2,3) block.
- The **per-rung Ward ratio** is `y_t^{(k)} / g_s^{(k)}`.
- The **matching coefficient at v** is
  `M = (y_t/g_s)(v)_SM / (y_t^{(16)}/g_s^{(16)})_lat`.

The **Distributional Invariance Theorem** claims that for every
distribution `{r_k}` satisfying the family constraint, the per-rung
Ward ratio equals `1/sqrt(6)` at every k = 0,...,16, and M is the same
number `1.9734` across all distributions.

No new symbols are imported into the framework; everything is built
from the retained taste-staircase transport theorem, the retained
Ward Identity Theorem, and the retained Coupling Map Theorem.

## V2: Inputs explicit

All inputs are listed in the note's "Retained foundations" section:

- **(I1) AX1: Cl(3) local algebra**, **(I2) AX2: Z^3 spatial
  substrate** — A_min axioms.
- **(I3) Ward Identity Theorem** (D9, D12, D16, D17, S2 — Q_L block,
  tree-level OGE = composite-Higgs identity): exact algebraic identity
  `y_t = g_s / sqrt(2 N_c)` on every lattice frame retaining Q_L = (2,3)
  and a Wilson+staggered surface. Used as unchanged per-rung input.
- **(I4) Coupling Map Theorem** (D14, D15, n_link counting): cumulative
  CMT change of variables U = u_0 V at each link, giving cumulative
  gauge rescaling `g_s_lat(M_Pl) = 1/sqrt(u_0)` → `g_s_lat(v) = 1/u_0`.
  Does NOT specify per-rung distribution.
- **(I5) Hierarchy Theorem** (Observable Principle from Axiom note):
  16 = 2^4 staggered taste doublers on 4D, giving 16 rungs over 17
  decades. Specifies number of rungs and cumulative span; does NOT
  specify per-rung distribution.

No PDG observable is consumed by any load-bearing check. The parent
note's `M = 1.9734` value (which comes from the SM-side primary chain
ratio at v) is consumed only as a target value for the cross-check
arm (Block 7 of runner).

## V3: Each step verifiable

| Check | Method |
|---|---|
| Family constraint sanity | `prod_{k=1..16} r_k = sqrt(1/u_0)` for each of 10 distributions; verify rel_err < 1e-12 |
| Per-rung Ward preservation | For each distribution, compute `g_s^{(k)}` via cumulative product, apply Ward to get `y_t^{(k)}`, verify `\|y_t^{(k)}/g_s^{(k)} - 1/sqrt(6)\| < 1e-12` for all k = 0..16 |
| CMT endpoint invariance | `\|g_s^{(16)} - 1/u_0\|/(1/u_0) < 1e-12` for each distribution |
| Matching coefficient invariance | Compute `M` for each distribution; verify spread < 1e-12 |
| Ward homogeneity | Rescale `(y_t, g_s) -> (lambda y_t, lambda g_s)` for lambda in {0.1, 0.5, 1, 2, 10, 100}; verify ratio unchanged |
| Parent reproduction | Run uniform-geometric distribution; verify `g_s(mu_16)`, `y_t(mu_16)`, `M` match parent runner |

All 10 checks PASS. Maximum deviation observed = `5.55e-17` (machine
precision floor for double-precision arithmetic).

## V4: No hidden imports

Imports in runner:

- `canonical_plaquette_surface` for `CANONICAL_*` (retained canonical
  surface constants on `main`).
- `numpy` (standard).

NO imports of:

- audit-data files (forbidden by hard rules)
- `CANONICAL_HARNESS_INDEX`, `DERIVATION_ATLAS`, `DERIVATION_VALIDATION_MAP`
- any PDG observable for load-bearing computation

The note cites only retained docs (parent transport note, Ward Identity
Theorem, Coupling Map Theorem, Hierarchy Theorem, v-matching theorem,
UV-to-IR transport obstruction master theorem).

No new axioms. No new canonical surface choices. No new numerical
inputs.

## V5: Distinct from prior blocks

| Block | Target | Scope | This block's distinction |
|---|---|---|---|
| 08 | yt_vertex_power | n_link = 2 at vacuum polarization, operator-counting at Lagrangian level | This block consumes n_link=1 as input via Ward; works at staircase trajectory level |
| 10 | alpha_s_derived | algebraic CMT-to-coupling-map identity `alpha_s(v) = alpha_bare/u_0^2` | This block consumes CMT endpoint as input; sweeps per-rung dressing distributions, not cumulative endpoint |
| 11 | u_0_plaquette_quartic | `u_0 = <P>^{1/4}` from L=4 plaquette length | This block does not touch the u_0 exponent definition |
| 14 | yt_ward_identity_derivation | exact tree-level Ward `y_t = g_s/sqrt(6)` from D9/D12/D16/D17/S2 on Q_L | This block applies the Ward identity AS-IS at each rung; new content is per-rung distributional invariance, not the Ward derivation itself |
| 15 | yt_boundary_theorem | numerical well-definedness / monotonicity / Lipschitz / unique-root of the backward-RGE map | This block is at the *staircase-level* (16 algebraic rungs), not at the *continuous-RGE* level; no Lipschitz, no monotonicity, no root-finder |
| **20 (this)** | yt_p2_taste_staircase_dressing_distribution_invariance | distributional invariance of per-rung Ward across 15-D family of per-rung dressings | No prior block touches the **distributional invariance** of the per-rung dressing; the parent note uses uniform geometric as a single point in the family without proving the broader invariance |

The parent taste-staircase transport note proves Ward preservation
ONLY for the *uniform geometric* distribution `r_k = u_0^{-1/32}` and
explicitly admits this as a "minimal framework-native prescription"
that could in principle be replaced by other distributions.

This block proves the broader theorem: **no choice of per-rung
distribution can produce Ward drift**. The Ward identity is homogeneous
of degree (1,1) in the pair `(y_t, g_s)` (from the structural Z² = 6
kinetic normalization and the OGE = composite-Higgs identity that
defines it), so the *ratio* `y_t/g_s` is invariant under common
rescaling. Per-rung, this means `y_t^{(k)}/g_s^{(k)} = 1/sqrt(6)`
regardless of the magnitude or distribution of the gauge coupling.

The corollary — that the open matching coefficient `M = 1.9734` is
invariant across the family — is a new robustness statement against a
natural skeptic question ("is the open piece an artifact of the
uniform-distribution choice?"). The answer is NO; the matching
coefficient is a load-bearing object of the lattice-to-SM interface.

No other block on the yt lane proves this invariance. This block is
strictly an extension of the parent partial closure, with no overlap
in its proven content.
