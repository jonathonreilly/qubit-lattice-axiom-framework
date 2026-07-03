# Beta=6 SU(3) Wilson Delta(beta) — Tree-Sector Product Bound and Compact-Deficit Obstruction

**Date:** 2026-05-30
**Type:** bounded_theorem / negative_route_pruning (a conditional lower bound
on the tree-like K-built resummed radius of convergence of the connected
strong-coupling series, plus a finite cubical-incidence obstruction to the
stronger all-K-built fixed-increment bridge; does NOT close beta=6 and asserts
no value of `<P>(6)`)
**Status:** review-loop source proposal. This note writes no audit verdict and
supplies no direct effective-status change.
**Primary runner:** [`scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py`](../scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py)
**Cached log:** [`logs/runner-cache/frontier_beta6_resummation_radius_growth_rate_2026_05_30.txt`](../logs/runner-cache/frontier_beta6_resummation_radius_growth_rate_2026_05_30.txt) (PASS=32 FAIL=0)

## 2026-06-07 Source-Boundary Manifest

This repair makes the audit boundary explicit without broadening the claim. The
runner proves the finite tree-sector algebra and compact-deficit counterexample
from on-main recurrences and cubical incidence checks:

```text
R_tree(g_tree) = 18 / g_tree^(1/4),
R_tree > 6 iff g_tree < 81,
compact 2x2x1 K-built block: k=4, F=16, n=15.
```

The row still has exactly three open growth inputs:

1. a retained or explicitly admitted `g_tree = lambda_tree rho_tree < 81`
   tree-cluster/cumulant bound;
2. a compact K-built face-deficit growth bound; and
3. a separate `>=3`-face baryon/epsilon-sector bound.

Accordingly, this row can be re-audited as a bounded source certificate for the
tree-sector product threshold and the finite compact-deficit obstruction. It
cannot be used as an all-K-built convergence proof, a beta=6 plaquette value,
or a closure of the full connected strong-coupling series.

## 0. Scope and what this note is for

The connected SU(3) Wilson single-plaquette series

```text
Delta(beta) := P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n
```

has its nearest singularity `|beta_c|` undetermined; the campaign relocated the
obstruction to the *multiplicity resummation*
(`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`).
The single-cube sector has the closed form `Delta_cube = 72 K'' (K')^5` with
`K = log J`, whose only singularities are `J`'s zeros (nearest `|beta_c| =
8.2052 > 6`), so the cube sector **converges at beta = 6**; multi-cube cluster
sectors carry an Euler weight `18^(1-F)`.

This note answers the tree-sector part of the radius question
**conditionally** and repairs an over-strong all-K-built bridge. Writing the
resummed radius `R = 1 / limsup_n |d_n|^(1/n)`, the tree-like K-built sector
(each new cube shares exactly one plaquette face) has a closed-form lower-bound
threshold controlled by the single growth product
`g_tree = lambda_tree rho_tree`: `g_tree < 81`.

The stronger statement that all K-built clusters have fixed `F=4k+2`,
`n=4k+1` is false. The runner constructs a finite four-cube `2x2x1` cubical
block whose boundary is still K-built (every boundary link has incidence two)
but has `F=16`, `n=15`, not `F=18`, `n=17`. Therefore the all-K-built sector
needs an additional compact/face-deficit growth bound. It is **not** a closure:
neither `lambda_tree`, `rho_tree`, the compact-deficit sector, nor the
`>=3`-face (baryon-channel) sector is pinned by the reproven ingredients. `0.594`
is a Monte-Carlo comparator only
(`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`),
never a derivation input here.

## 1. Reproven Ingredients and Explicit Open Inputs

The algebraic/cumulant pieces are recomputed in the runner from framework
recurrences and cubical identities; the Bars, Klarner/Eden, and Fisher entries are **comparators only**,
never inputs. The tree-sector cluster-count growth rate `lambda_tree`, the
per-tree cumulant/combinatorics factor `rho_tree`, and the compact-deficit
growth control are **not** derived here.

Load-bearing markdown-linked sources: the on-main recurrence / finite
Picard-Fuchs source for the `J` coefficients below. Other filenames in this
note are context, comparators, or future-route pointers and are intentionally
not citation-graph dependencies.

- **(A) `J` Taylor coefficients** from the on-main order-3
  dominant-weight (Picard-Fuchs) recurrence
  `6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}`,
  `a_0,a_1,a_2 = 1,0,1/36`
  ([`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md);
  [`PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md)).
  Reproduces `P_1plaq(6) = J'(6)/J(6) = 0.4225317396`; cross-checked against the
  Bars 1980 Bessel-determinant `J` (comparator) to `< 1e-8`.
- **(B) single-plaquette cumulant GF** `K = log J`:
  `kappa_m = m! [b^m] K = (1/18, 1/108, 0, -5/3888)` for `m = 2..5`.
- **(C) cube-sector closed form** `Delta_cube = 72 K'' (K')^5` reproduces the
  on-main exact connected coefficients `d_5 = 1/472392`, `d_6 = 7/5668704`,
  `d_7 = 5/17006112`, `d_8 = 5/272097792`
  (`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`;
  `BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`)
  and the cube-part of `d_9 = -235/29386561536`.
- **(D) finite J-zero stabilization evidence.** The nearest zero of `J`
  truncated to degree `T` migrates `5.739 (T=3) -> 6.050 (T=4) -> ... -> 8.205
  (T>=20)`. This shows the `T=3` value is not a stable radius witness and
  supports the on-main single-plaquette zero localization, but the bounded
  theorem below does not rely on a standalone theorem that partial-sum zeros
  converge from below. An independent Cauchy-Hadamard root test
  `|d_n|^(-1/n)` on 44 exact cube-sector coefficients sits in `6.7-7.5` (slow
  approach for an off-axis complex-pair singularity), supporting the
  cube-sector `> 6` reading without making it load-bearing here.

## 2. Tree K-built proliferation bound and the compact-deficit obstruction

The full connected `Delta` is a linked-cluster sum over connected polycube
clusters `C` (closed-surface cube clusters glued along shared faces) rooted at
the marked plaquette:

```text
Delta(beta) = sum_C W(C),    W(C) ~ (Euler weight 18^(1-F)) x (cumulant) x beta^{n(C)}.
```

For a connected union of `k` elementary cubes with `s` shared plaquette faces,
the boundary-face count is

```text
F = 6k - 2s.
```

The action-plaquette power is `n = F - 1`, because the marked plaquette is not
an action insertion. In the **tree-like K-built sector**, `s = k-1`, hence

```text
F_tree = 4k + 2,        n_tree = 4k + 1,
18^(1-F_tree) |beta|^n = 18^{-(4k+1)} |beta|^{4k+1}.
```

This also repairs the audit-flagged exponent: the Euler exponent is
`1-(4k+2)=-(4k+1)`, not `-(4k+2)`.

The number of distinct rooted connected `k`-cube clusters on `Z^4` grows like
`lambda_tree^k` in the tree sector. This note does **not** prove
`lambda_tree <= 7`: `2d - 1 = 7` is the self-avoiding path continuation factor,
not a valid upper bound on branched connected animals. Bounding the per-cube
connected-cumulant / Mobius combinatorial factor by a per-cube constant
`rho_tree`, the magnitude of the tree-sector contribution is conditionally
controlled by the product `g_tree = lambda_tree rho_tree`:

```text
|.| <=  g_tree^k  x  18^{-(4k+1)}  x  |beta|^{4k+1}.
```

so the `k`-sum is a geometric series in `|beta|^4` that converges iff
`g_tree 18^{-4} |beta|^4 < 1`. This gives the closed-form **tree-sector radius
bound**

```text
R_tree(g_tree) = 18 / g_tree^{1/4},
```

monotone decreasing in `g_tree`, with the exact threshold (reproven in the
runner)

```text
R_tree = 6   <=>   g_tree = g_crit = (18/6)^4 = 81.
```

**Theorem (tree K-built resummation-radius lower bound).** *In the tree-like
K-built sector of `Delta`, the geometric Euler suppression (`18^{-4}` per
additional cube), and the action-plaquette growth (`|beta|^4` per additional
cube) give the conditional radius bound
`R_tree(g_tree) = 18/g_tree^{1/4}`. In particular `R_tree > 6` exactly when
`g_tree < 81`. If a separate audited or explicitly admitted source later supplies
`lambda_tree <= 7`, this theorem specializes to
`rho_tree < 81/7 = 11.5714...`; that numerical specialization is not asserted
as an internal count theorem here.* Proof: the geometric-series convergence
radius above; ingredients (A)-(C) and the cubical incidence identities are
reproven in the runner, while `g_tree = lambda_tree rho_tree` is the explicit
conditional growth input. ∎

**Compact-deficit obstruction.** The all-K-built extension of this theorem is
not valid as previously worded. The runner constructs a four-cube `2x2x1` block
embedded in `Z^4`. Its boundary is closed K-built — every boundary link is
incident to exactly two plaquette faces — but the block has `k=4`, `s=4`, hence
an excess shared-face count `c=s-(k-1)=1` and

```text
F = 4k+2-2c = 16,       n = F-1 = 15,
```

not the tree values `F=18`, `n=17`. At `beta=6`, each unit of excess
shared-face count weakens the Euler/action suppression by a factor `9`.
Therefore the all-K-built sector is not reduced to the single product
`g_tree`; it needs an additional compact/face-deficit growth bound or an
equivalent area-based cluster expansion.

**Consequence.** The tree K-built problem reduces to the product threshold
`g_tree < 81`; the all-K-built problem does not. Any full beta=6 radius
statement must also control compact K-built face deficits and the `>= 3`-face
baryon-channel sector outside the K-built class.

## 3. What is rigorous, what is the named obstruction

**Rigorous (this note + cited on-main):**

- cube-sector high-truncation zero evidence stabilizes near `8.2052 > 6`; this
  is context for the single-cube sector, not the load-bearing theorem here;
- within the tree-like K-built regime, `R_tree(g_tree) = 18/g_tree^{1/4}`,
  hence `R_tree > 6` exactly for
  `g_tree = lambda_tree rho_tree < 81`;
- the all-K-built fixed-increment bridge is false: a finite `2x2x1` four-cube
  block is closed K-built but has `F=16`, `n=15`, not `F=18`, `n=17`.

**Named open inputs (the sharpened obstruction).** The growth rate `mu` — hence
the resummed radius — is pinned by exactly three quantities **not** fixed by the
reproven ingredients:

1. **`g_tree = lambda_tree rho_tree`**, the product of tree-sector cluster-count
   growth and per-cube connected-cumulant / set-partition combinatorial growth.
   Bounding it `< 81` is precisely a tree-graph / Kotecky-Preiss
   (Brydges-type) cluster-expansion convergence statement, which the framework
   treats as an **external** result
   (`KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`,
   comparator). It is therefore an admissible import -> bounded -> retire target,
   not a framework-internal closure today.
2. **The compact K-built face-deficit sector**, where excess shared-face count
   `c=s-(k-1)` changes the action/Euler power to `4k+1-2c`. This is still
   links-meet-`<=2` K-built geometry, so it is not dismissed as a baryon channel;
   it needs an area/deficit-growth bound or an equivalent cluster-expansion
   theorem.
3. **The `>= 3`-face (baryon/epsilon) channel sector**, `beta^10` onward, whose
   weight class is outside the K-built argument of Section 2.

None is pinned here; these are the same class of input the campaign already
named — an externally-supplied cluster-expansion / no-real-bulk-transition
certificate on the externally-computed series, never on the circular
`kappa/witness` pair
(`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`).

## 4. Comparator reconciliation

The single-plaquette / cube-sector radius evidence stabilizes near `8.2052`.
The thermodynamic Fisher / Lee-Yang zero is `|beta| ~ 5.54` (lattice-QCD
comparator). These are **not** in conflict: `8.2052` is cube-sector /
single-plaquette context, while a sub-`6` thermodynamic singularity, if it
exists, must come from at least one residual not controlled here: tree-sector
growth `g_tree >= 81`, compact K-built face-deficit growth, or the baryon-channel
sector. The location `|beta_c|`
remains the under-determined `rho_{p,q}(6)` object restated in the beta-plane
(`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`).

## 5. No-Go Discipline Gate

**Status:** PASS for this bounded-with-open-inputs claim. The negative boundary
is narrow: this note does not say the beta=6 wall is gone or confirmed. It says
the tree-like K-built Euler sector is reduced to the explicit growth-product
condition `g_tree < 81`, while compact K-built face deficits and the
baryon/epsilon sector remain outside the bound.

**N1 — Alternative route enumeration.**

| Route tested against the boundary | Marker | Result |
|---|---|---|
| Single-cube `J`-zero / cube-sector radius | ATTEMPTED | Finite truncations stabilize above 6; this does not control multi-cube growth. |
| Tree-sector Euler suppression | ATTEMPTED | Gives the exact `18^{-4}` per additional tree cube, but needs the count/combinatorics product. |
| Compact K-built fixed-increment extension | REFUTED | A closed K-built `2x2x1` four-cube block has `F=16`, `n=15`, not the tree values `F=18`, `n=17`. |
| Self-avoiding path count `2d-1=7` | ATTEMPTED | Not a valid branched-animal bound; demoted to an illustrative specialization only. |
| Kotecky-Preiss / Brydges cluster-expansion input | OPEN IMPORT ROUTE | Would close the tree side by proving `g_tree < 81`; not derived here. |
| Compact face-deficit growth | OPEN CHANNEL | Still K-built, but not controlled by the tree product. Needs an area/deficit-growth theorem. |
| `>=3`-face baryon/epsilon sector | OPEN CHANNEL | Leaves the K-built Euler-`18` regime and must be bounded separately. |
| Thermodynamic Fisher-zero comparator | COMPARATOR ONLY | Motivates the wall but is not an input to the theorem. |

**N2 — Wall-independence audit.** The tree-sector walls `lambda_tree` and
`rho_tree` collapse to the single product
`g_tree = lambda_tree rho_tree` for this radius bound. The compact face-deficit
and baryon/epsilon sectors are independent: bounding `g_tree` does not bound
either sector, and bounding either sector does not prove `g_tree < 81`.

**N3 — Hidden-wall scan.** "K-built," "Euler-18," "Kotecky-Preiss,"
"Brydges," "Fisher," and "Klarner/Eden" are explicitly classified. External
cluster expansion machinery and thermodynamic zero locations are not consumed
as proof inputs.

**N4 — Residual matching.** The residual attacked is the tree K-built growth
budget and the false all-K-built fixed-increment bridge, not the full beta=6
plaquette value and not the full thermodynamic radius.
The cited beta-plane frontier note is context for that same residual.

**N5 — Rhetoric audit.** The claim is sector-scoped. It does not assert a
lattice-wide closure, a full-series convergence theorem, a beta=6 value, or a
proof that the thermodynamic Fisher-zero surface is absent.

**N6 — Partial-closure path scan.** The legitimate retirement path is to supply
a later audited/admitted cluster-expansion bound proving `g_tree < 81`, a compact
K-built face-deficit/area-growth bound, and a separate bound on the `>=3`-face
baryon/epsilon sector. No new baseline premise is requested.

**N7 — Steelman.** A hostile reviewer can point out that the real branched
cluster growth may exceed the self-avoiding path factor, and the combinatorial
cumulants may push `g_tree >= 81`; even if they do not, compact face deficits
can weaken Euler suppression while staying K-built. This is exactly why the
branch is tree-scoped and not landed as a full K-built closure.

**N8 — Cross-cycle echo.** The same beta=6 wall appears in the analytic-class
frontier and `rho_{p,q}(6)` notes. This note preserves that wall, but makes one
piece of it discoverable as the concrete tree-sector product bound
`g_tree < 81` and another piece discoverable as the compact-deficit wall.

## 6. Runner scorecard

`scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py` —
single-seed deterministic, memory-bounded (max Taylor degree 60, max root-finder
degree 30; peak RSS `~65 MB`; no enumeration of cluster topologies):

- [A] recurrence seed `a_2 = 1/36`; `P_1plaq(6) = 0.4225317396`; recurrence ==
  Bars `J(6)`.
- [B] `kappa_2..5 = 1/18, 1/108, 0, -5/3888`.
- [C] `72 K'' (K')^5` reproduces `d_5..d_8` and the `d_9` cube-part exactly.
- [D] J-zero finite-truncation migration `5.739 -> 8.205`, monotone-up in the
  tested sequence, crosses `6` by `T=4`.
- [E] cubical-incidence identities for single cube, two-cube tree box,
  four-cube tree chain, and compact `2x2x1` block; tree-sector exponent
  correction `18^{-(4k+1)}`; compact K-built counterexample with `F=16`,
  `n=15`; tree threshold `R_tree(g_tree)=18/g_tree^{1/4}` and
  `g_crit=81`; if an external `lambda_tree <= 7` bound is supplied later, the
  corresponding `rho_crit = 81/7 = 11.5714`.

**SCORECARD: PASS = 32, FAIL = 0.**

## See also

- `BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`
- `BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`
- `BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`
- `GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`
- `GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`
