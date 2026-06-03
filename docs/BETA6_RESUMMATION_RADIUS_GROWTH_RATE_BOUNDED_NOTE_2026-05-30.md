# Beta=6 SU(3) Wilson Delta(beta) — Resummation-Radius Growth-Product Bound

**Date:** 2026-05-30
**Type:** bounded_theorem (a conditional lower bound on the K-built resummed
radius of convergence of the connected strong-coupling series, with an exact
growth-product threshold; does NOT close beta=6 and asserts no value of
`<P>(6)`)
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not quote, set, or predict audit outcomes.
**Primary runner:** [`scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py`](../scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py)

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

This note answers the decisive radius question **conditionally**: writing the
resummed radius `R = 1 / limsup_n |d_n|^(1/n)`, it derives a closed-form lower
bound for the radius of the **K-built (links-meet-<=2-faces,
Euler-`18^(1-F)`) sector** as a function of the single growth product
`g_K = lambda_K rho_comb`, where `lambda_K` is the K-built cluster-count growth
rate and `rho_comb` is the per-cube connected-cumulant / set-partition factor.
The exact threshold is `g_K < 81`. It is **not** a closure: neither `lambda_K`,
`rho_comb`, nor the `>=3`-face (baryon-channel) sector is pinned by the
reproven primitives, so the note records a conditional bound and names
precisely the open inputs that fix `|beta_c|`. `0.594` is a Monte-Carlo
comparator only
(`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`),
never a derivation input here.

## 1. Reproven primitives and explicit open inputs

The algebraic/cumulant pieces are recomputed in the runner from framework
primitives; the Bars, Klarner/Eden, and Fisher entries are **comparators only**,
never inputs. The K-built cluster-count growth rate `lambda_K` is **not**
derived here.

Load-bearing markdown-linked authorities: the retained recurrence / finite
Picard-Fuchs source for the `J` coefficients below. Other filenames in this
note are context, comparators, or future-route pointers and are intentionally
not citation-graph dependencies.

- **(A) `J` Taylor coefficients** from the on-main RETAINED order-3
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

## 2. The K-built proliferation bound (the new conditional theorem)

The full connected `Delta` is a linked-cluster sum over connected polycube
clusters `C` (closed-surface cube clusters glued along shared faces) rooted at
the marked plaquette:

```text
Delta(beta) = sum_C W(C),    W(C) ~ (Euler weight 18^(1-F)) x (cumulant) x beta^{n(C)}.
```

Within the **K-built regime** — every link meets `<= 2` faces, the regime in
which the `18^(1-F)` Euler law and the `K = log J` cumulant structure hold — the
per-cube geometric scaling is **fixed and reproven**:

- a single cube has `F = 6`, Euler weight `18^(1-6) = 18^(-5)` (matches the
  `d_5 = 4/18^5` anchor) and `n = F-1 = 5` action plaquettes;
- the two-cube box (sharing one face) has `F = 10`, Euler weight `18^(-9)`
  (matches the on-main `beta^9` two-cube-box leading term) and `n = 9`;
- sharing more than one face, or sharing the marked face, creates a `>= 3`-face
  junction — the SU(3) baryon/epsilon channel (leading `3/18^10` at `beta^10`) —
  which **leaves** the K-built / Euler-`18` regime. Hence inside the regime the
  per-cube increment is fixed: `dF = dn = 4`.

The number of distinct rooted connected `k`-cube clusters on `Z^4` grows like
`lambda_K^k`. This note does **not** prove `lambda_K <= 7`: `2d - 1 = 7` is the
self-avoiding path continuation factor, not a valid upper bound on branched
connected animals. Bounding the per-cube connected-cumulant / Mobius
combinatorial factor by a per-cube constant `rho_comb`, the magnitude of the
order-`(beta)` contribution of all `k`-cube K-built clusters is conditionally
controlled by the product `g_K = lambda_K rho_comb`:

```text
|.| <=  g_K^k  x  18^{-(4k+1)}  x  |beta|^{4k+1}.
```

Here `F = 4k+2`, so the Euler factor is `18^(1-F) = 18^{-(4k+1)}`.
This corrects an earlier off-by-one display exponent; it changes only the
overall prefactor, not the per-cube ratio. The `k`-sum is a geometric series in
`|beta|^4` that converges iff `g_K 18^{-4} |beta|^4 < 1`. This gives the
closed-form **K-built radius bound**

```text
R_Euler(g_K) = 18 / g_K^{1/4},
```

monotone decreasing in `g_K`, with the exact threshold (reproven in the
runner)

```text
R_Euler = 6   <=>   g_K = g_crit = (18/6)^4 = 81.
```

**Theorem (K-built resummation-radius lower bound).** *In the K-built
(links-meet-`<=2`-faces, Euler-`18^(1-F)`) sector of `Delta`, the geometric
Euler suppression (`18^{-4}` per cube), and the action-plaquette growth
(`|beta|^4` per cube) give the conditional radius bound
`R_Euler(g_K) = 18/g_K^{1/4}`. In particular `R_Euler > 6` exactly when
`g_K < 81`. If a separate retained or admitted source later supplies
`lambda_K <= 7`, this theorem specializes to
`rho_comb < 81/7 = 11.5714...`; that numerical specialization is not asserted
as an internal count theorem here.* Proof: the geometric-series convergence
radius above; primitives (A)-(C) are reproven in the runner, while
`g_K = lambda_K rho_comb` is the explicit conditional growth input. ∎

**Consequence.** Geometric proliferation, lattice-animal count, and Euler
suppression reduce the K-built problem to the single product threshold
`g_K < 81`; they do not by themselves close beta=6. Any sub-`6` singularity of
`Delta` must be sourced either by `g_K >= 81` or by the `>= 3`-face
baryon-channel sector outside this K-built bound.

## 3. What is rigorous, what is the named obstruction

**Rigorous (this note + cited on-main):**

- cube-sector high-truncation zero evidence stabilizes near `8.2052 > 6`; this
  is context for the single-cube sector, not the load-bearing theorem here;
- within the K-built regime, `R_Euler(g_K) = 18/g_K^{1/4}`, hence
  `R_Euler > 6` exactly for `g_K = lambda_K rho_comb < 81`.

**Named open inputs (the sharpened obstruction).** The growth rate `mu` — hence
the resummed radius — is pinned by exactly two quantities **not** fixed by the
reproven primitives:

1. **`g_K = lambda_K rho_comb`**, the product of K-built cluster-count growth
   and per-cube connected-cumulant / set-partition combinatorial growth.
   Bounding it `< 81` is precisely a Kotecky-Preiss / tree-graph
   (Brydges-type) cluster-expansion convergence statement, which the framework
   treats as an **external** result
   (`KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`,
   comparator). It is therefore an admissible import -> bounded -> retire target,
   not a framework-internal closure today.
2. **The `>= 3`-face (baryon/epsilon) channel sector**, `beta^10` onward, whose
   weight class is stronger than `18^(1-F)` and is **not** bounded by the K-built
   argument of Section 2.

Neither is pinned here; both are the same class of input the campaign already
named — an externally-supplied cluster-expansion / no-real-bulk-transition
certificate on the externally-computed series, never on the circular
`kappa/witness` pair
(`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`).

## 4. Comparator reconciliation

The single-plaquette / cube-sector radius evidence stabilizes near `8.2052`.
The thermodynamic Fisher / Lee-Yang zero is `|beta| ~ 5.54` (lattice-QCD
comparator). These are **not** in conflict: `8.2052` is cube-sector /
single-plaquette context, while a sub-`6` thermodynamic singularity, if it
exists, must — by the Section 2 theorem — be sourced by `g_K >= 81` or by the
baryon-channel sector, neither of which the reproven primitives bound. The
location `|beta_c|`
remains the under-determined `rho_{p,q}(6)` object restated in the beta-plane
(`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`).

## 5. No-Go Discipline Gate

**Status:** PASS for this bounded-with-open-inputs claim. The negative boundary
is narrow: this note does not say the beta=6 wall is gone or confirmed. It says
the K-built Euler sector is reduced to the explicit growth-product condition
`g_K < 81`, while the baryon/epsilon sector remains outside the bound.

**N1 — Alternative route enumeration.**

| Route tested against the boundary | Marker | Result |
|---|---|---|
| Single-cube `J`-zero / cube-sector radius | ATTEMPTED | Finite truncations stabilize above 6; this does not control multi-cube growth. |
| Euler suppression alone | ATTEMPTED | Gives the exact `18^{-4}` per-cube factor, but needs the count/combinatorics product. |
| Self-avoiding path count `2d-1=7` | ATTEMPTED | Not a valid branched-animal bound; demoted to an illustrative specialization only. |
| Kotecky-Preiss / Brydges cluster-expansion input | OPEN IMPORT ROUTE | Would close the K-built side by proving `g_K < 81`; not derived here. |
| `>=3`-face baryon/epsilon sector | OPEN CHANNEL | Leaves the K-built Euler-`18` regime and must be bounded separately. |
| Thermodynamic Fisher-zero comparator | COMPARATOR ONLY | Motivates the wall but is not an input to the theorem. |

**N2 — Wall-independence audit.** The K-built walls `lambda_K` and `rho_comb`
collapse to the single product `g_K = lambda_K rho_comb` for this radius bound.
The baryon/epsilon sector is independent: bounding `g_K` does not bound that
sector, and bounding that sector does not prove `g_K < 81`.

**N3 — Hidden-wall scan.** "K-built," "Euler-18," "Kotecky-Preiss,"
"Brydges," "Fisher," and "Klarner/Eden" are explicitly classified. External
cluster expansion machinery and thermodynamic zero locations are not consumed
as proof inputs.

**N4 — Residual matching.** The residual attacked is the K-built growth budget,
not the full beta=6 plaquette value and not the full thermodynamic radius.
The cited beta-plane frontier note is context for that same residual.

**N5 — Rhetoric audit.** The claim is sector-scoped. It does not assert a
lattice-wide closure, a full-series convergence theorem, a beta=6 value, or a
proof that the thermodynamic Fisher-zero surface is absent.

**N6 — Partial-closure path scan.** The legitimate retirement path is to supply
a retained/admitted cluster-expansion bound proving `g_K < 81`, plus a separate
bound on the `>=3`-face baryon/epsilon sector. No new axiom is requested.

**N7 — Steelman.** A hostile reviewer can point out that the real branched
cluster growth may exceed the self-avoiding path factor, and the combinatorial
cumulants may push `g_K >= 81`; then the K-built sector could still have a
sub-6 radius. This is exactly why the branch was narrowed to the product
threshold and not landed as a closure.

**N8 — Cross-cycle echo.** The same beta=6 wall appears in the analytic-class
frontier and `rho_{p,q}(6)` notes. This note preserves that wall, but makes one
piece of it discoverable as the concrete product bound `g_K < 81`.

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
- [E] anchor Euler weights (`18^{-5}`, `18^{-9}`); per-cube increment `dF=dn=4`;
  `R_Euler(g_K) = 18/g_K^{1/4}`; threshold `g_crit = 81`; if an external
  `lambda_K <= 7` bound is supplied later, the corresponding
  `rho_crit = 81/7 = 11.5714`.

**SCORECARD: PASS = 23, FAIL = 0.**

## See also

- `BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`
- `BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`
- `BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`
- `GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`
- `GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`
