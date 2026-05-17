# V1-V5 Self-Grounding -- Block 21 (yt_zero_import_authority_note)

Target: `yt_zero_import_authority_note` — 469 desc, unaudited, claim_type
`positive_theorem`. Block constructs a strengthening as a new
positive theorem note (the parent note itself is not modified).

## V1: Definitions clear

The block defines and verifies the following named theorem:

**Boundary-Ratio Invariance Theorem.** Let `u_0' > 0` be any positive
real (not necessarily the canonical-surface value `u_0 = ⟨P⟩^{1/4}`).
Define the lattice-side UV-boundary couplings by:

```
    alpha_LM'    := alpha_bare / u_0'
    g_s(M_Pl)    := sqrt(4 pi * alpha_LM')
    y_t(M_Pl)    := g_s(M_Pl) / sqrt(2 N_c)
```

Then for every `u_0' > 0`:

```
    y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(2 N_c) = 1 / sqrt(6)
```

with no `u_0'`-dependence.

Corollary 1 (Cancellation lemma): the `1/sqrt(u_0')` tadpole cancels
identically in the ratio because `n_link = 1` is the common vertex power
on both gauge and Yukawa legs (D15).

Corollary 2 (Input enumeration): the load-bearing input set for the
ratio is exactly `{N_c, Ward identity structure}`.

Corollary 3 (External-observable independence): the load-bearing
function `boundary_couplings(u_0', alpha_bare)` consumes zero SM
observable; static string-level check verifies the function source
contains no PDG numerical comparator.

No new symbols are introduced into the framework; everything is built
from the retained Ward Identity Theorem (T1, T2), retained Coupling
Map Theorem (D14, D15 with `n_link = 1`), and framework-internal
group-theoretic facts (`N_c = 3`, `N_iso = 2`).

## V2: Inputs explicit

All inputs are listed in the note's "Retained foundations" section:

- **(I1) AX1: Cl(3) local algebra**, **(I2) AX2: Z³ spatial substrate**
  — `A_min` axioms.
- **(I3) Ward Identity Theorem T1, T2**
  ([`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](../../../../../../../docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md)):
  exact algebraic identity `y_t_bare = g_bare / sqrt(2 N_c)` on every
  lattice surface retaining `Q_L = (2,3)`. Used unchanged.
- **(I4) Coupling Map Theorem D14, D15**
  ([`docs/YT_VERTEX_POWER_DERIVATION.md`](../../../../../../../docs/YT_VERTEX_POWER_DERIVATION.md)):
  `n_link = 1` per single vertex; the same power enters gauge and
  Yukawa vertices.
- **(I5) `N_c = 3`** (from AX1 Cl(3) spatial dim) and **`N_iso = 2`**
  (from D5, Cl(3) ⊃ su(2) inclusion). Framework-internal group-
  theoretic facts.

No PDG observable is consumed by any load-bearing check. The parent
authority note's central values (`y_t(v) = 0.9176`, `m_t(pole) = 172.57
GeV`) are cited as cross-check context only (Block 9) and are NOT
load-bearing for this theorem.

## V3: Each step verifiable

| Check | Method |
|---|---|
| Input enumeration sanity | Block 1: verify `N_c = 3`, `N_iso = 2`, `Q_L` dim = 6, predicted ratio = `1/sqrt(6)`; `tol = 1e-15` |
| Canonical-surface ratio identity | Block 2: compute ratio at `u_0 = ⟨P⟩^{1/4}`, verify `|ratio - 1/sqrt(6)| < 1e-13` |
| Tadpole-independence sweep | Block 3: scan `u_0' ∈ [1e-3, 1e3]` on 61 log-spaced points; verify worst ratio deviation `< 1e-13`; cross-check magnitudes scale as `1/sqrt(u_0')` |
| Ward homogeneity | Block 4: rescale `(g_s, y_t) -> (λ g_s, λ y_t)` for `λ ∈ {1e-3, 1e-2, 0.1, 1, 10, 100, 1e3}`; verify ratio unchanged |
| External-observable independence | Block 5: static `inspect.getsource()` check that `boundary_couplings` source contains no banned PDG string (12 banned strings) |
| Minimal input set | Block 6: counterfactual `N_c ∈ {2,3,4,5}` shows ratio varies; counterfactual `alpha_bare ∈ {0.001, 0.01, 0.1, 1, 10}` shows ratio invariant |
| Magnitude reproduction | Block 7: verify `y_t(M_Pl)` on canonical surface matches `YT_ZERO_IMPORT_CHAIN_NOTE` table value `0.4358` to `< 5e-4` |
| Robustness stress test | Block 8: 10000 random `u_0'` draws (log-uniform `[1e-4, 1e4]`); verify max deviation `< 1e-13` |
| Authority-note cross-check | Block 9: verify color projection `sqrt(8/9)` reproduces `sqrt((N_c² - 1)/N_c²) = 8/9` (downstream sanity) |

All 19 checks PASS. Maximum deviation observed across 10000+ tadpole
draws: `5.55e-17` (double-precision machine epsilon floor).

## V4: No hidden imports

Imports in runner:

- `canonical_plaquette_surface` for `CANONICAL_*` (retained canonical
  surface constants on `main`). Used ONLY in Block 2 (canonical-surface
  cross-check) and Block 7 (magnitude reproduction); NOT used in the
  load-bearing tadpole-independence sweep (Block 3) or robustness
  stress test (Block 8), which both use sampled `u_0'` values
  independent of the canonical surface.
- `numpy` (standard).
- `math` (standard).
- `inspect` (standard; used in Block 5 for the static source check).

NO imports of:

- audit-data files (forbidden by hard rules)
- `CANONICAL_HARNESS_INDEX`, `DERIVATION_ATLAS`, `DERIVATION_VALIDATION_MAP`
- any PDG observable for load-bearing computation
- any output of `frontier_yt_*` runners (block is self-contained)

The note cites only retained docs (Zero-Import Authority Note, Ward
Identity Theorem, Vertex-Power Theorem, EW Color Projection Theorem,
Zero-Import Chain Note, Minimal Axioms).

No new axioms. No new canonical surface choices. No new numerical
inputs.

## V5: Distinct from prior blocks

| Block | Target | Scope | This block's distinction |
|---|---|---|---|
| 08 | yt_vertex_power | `n_link = 2` at vacuum polarization (operator counting for gauge sector) | This block uses `n_link = 1` per single vertex (D15) and proves the *ratio* invariance from the common `n_link = 1` on both gauge and Yukawa legs |
| 10 | alpha_s_derived | algebraic CMT-to-coupling-map identity `alpha_s(v) = alpha_bare/u_0^2` | This block is at the M_Pl boundary (UV), not the v endpoint (IR); it uses `n_link = 1` at the vertex, not `n_link = 2` at the vacuum polarization |
| 11 | u_0_plaquette_quartic | `u_0 = <P>^{1/4}` from L=4 plaquette length | This block does not touch the `u_0` exponent definition; in fact, it proves the ratio is *independent* of `u_0` |
| 14 | yt_ward_step3 | exact tree-level Ward `y_t = g_s/sqrt(6)` from D9/D12/D16/D17/S2 on `Q_L`; same-1PI gate diagnostic | This block consumes the Ward identity AS-IS at the M_Pl boundary; new content is the **tadpole-factor invariance** of the boundary ratio (NOT the Ward derivation itself, which is upstream input) |
| 15 | yt_boundary | numerical well-definedness / monotonicity / Lipschitz / unique-root of the backward-RGE map | This block is at the *algebraic* boundary identity, not the *numerical* backward-RGE root-finder; no Lipschitz, no monotonicity, no root-finder |
| 20 | yt_p2_taste_staircase_dressing | distributional invariance of per-rung Ward across 15-D family of per-rung dressings (16 rungs of the taste staircase) | This block is at the M_Pl boundary alone (the `k = 0` rung), not across the staircase; the invariance class here is *tadpole-factor* `u_0'`, not *per-rung dressing distribution* `{r_k}` |
| **21 (this)** | yt_zero_import_boundary_ratio_authority | tadpole-factor invariance of the M_Pl boundary ratio `y_t(M_Pl)/g_s(M_Pl) = 1/sqrt(6)` across all `u_0' > 0`; load-bearing input enumeration; PDG-string-level static independence check | No prior block proves the structural rigidity of the boundary ratio under canonical-surface tadpole-factor choice |

The parent zero-import authority note records the ratio as exact on
the canonical surface only, via the Ward Identity Theorem applied at
the canonical `u_0`. The parent Ward Identity Theorem includes the
remark (lines 90-99) that "the tadpole factor `1/sqrt(u_0)` is common
to both `g_s(M_Pl)` and `y_t(M_Pl)` via D15 ... and cancels in the
ratio", but does not upgrade this to a theorem about invariance
under tadpole-factor *choice*.

This block proves: **the ratio identity is invariant under all
positive choices of `u_0'`, not just the canonical-surface `u_0`**.
The load-bearing input set for the ratio is minimal (Corollary 2,
verified by Block 6 counterfactual scan), and the framework-side
ratio computation consumes zero PDG observable (Corollary 3, verified
by Block 5 static source check).

No other block on the yt lane proves this structural rigidity at the
M_Pl boundary. This block is strictly an extension of the parent
authority note's "zero external observables" claim, in the direction
of sharpening it to "zero canonical-surface inputs on the ratio".

No prior block touches the *tadpole-factor invariance* of the boundary
ratio.
