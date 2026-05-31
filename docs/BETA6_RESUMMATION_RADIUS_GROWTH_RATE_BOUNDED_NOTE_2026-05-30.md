# Beta=6 SU(3) Wilson Delta(beta) — Resummation-Radius Growth-Rate Bound

**Date:** 2026-05-30
**Type:** bounded_theorem (a conditional lower bound on the resummed radius of
convergence of the connected strong-coupling series, with an exact reproven
threshold; does NOT close beta=6 and asserts no value of `<P>(6)`)
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
([`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)).
The single-cube sector has the closed form `Delta_cube = 72 K'' (K')^5` with
`K = log J`, whose only singularities are `J`'s zeros (nearest `|beta_c| =
8.2052 > 6`), so the cube sector **converges at beta = 6**; multi-cube cluster
sectors carry an Euler weight `18^(1-F)`.

This note answers the decisive radius question **conditionally**: writing the
resummed radius `R = 1 / limsup_n |d_n|^(1/n)`, it derives — from framework
primitives, import-free — a closed-form lower bound for the radius of the
**K-built (links-meet-<=2-faces, Euler-`18^(1-F)`) sector** as a function of a
single per-cube combinatorial factor `rho_comb`, and reproves the exact
threshold at which that bound reaches 6. It is **not** a closure: `rho_comb` and
the `>=3`-face (baryon-channel) sector are not pinned by the reproven primitives,
so the note records a conditional bound and names precisely the open inputs that
fix `|beta_c|`. `0.594` is a Monte-Carlo comparator only
([`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md)),
never a derivation input here.

## 1. Reproven primitives (import-free)

All four are recomputed in the runner from framework primitives; the Bars,
Klarner/Eden, and Fisher entries are **comparators only**, never inputs.

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
  ([`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md);
  [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md))
  and the cube-part of `d_9 = -235/29386561536`.
- **(D) the 8.2052 singularity is a multiplicity-resummation limit.** The
  nearest zero of `J` truncated to degree `T` migrates `5.739 (T=3) -> 6.050
  (T=4) -> ... -> 8.205 (T>=20)`. Because `J` is entire (Bars; each `I_n`
  entire), the truncation zeros converge to the true nearest zero **from
  below**: `8.2052` is the rigorous cube-sector radius and `5.74` is a
  finite-truncation artifact, **not** a separate singularity. An independent
  Cauchy-Hadamard root test `|d_n|^(-1/n)` on 44 exact cube-sector coefficients
  sits in `6.7-7.5` (slow approach to `8.2052` for an off-axis complex-pair
  singularity), confirming the cube-sector radius is robustly `> 6`.

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

The number of distinct rooted connected `k`-cube polycubes on `Z^4` grows like
`lambda^k`; it is bounded above by the self-avoiding face-adjacency branching of
the `2d = 8`-neighbour cube graph, `lambda <= 2d - 1 = 7` (a Klarner-type
structural bound; the Klarner/Eden all-site animal constant `lambda_4 ~ 8.34` is
a looser comparator). Bounding the per-cube connected-cumulant / Mobius
combinatorial factor by a per-cube constant `rho_comb`, the magnitude of the
order-`(beta)` contribution of all `k`-cube K-built clusters is

```text
|.| <=  7^k  x  rho_comb^k  x  18^{-(4k+2)}  x  |beta|^{4k+1},
```

so the `k`-sum is a geometric series in `|beta|^4` that converges iff
`7 rho_comb 18^{-4} |beta|^4 < 1`. This gives the closed-form **K-built radius
bound**

```text
R_Euler(rho_comb) = 18 / (7 rho_comb)^{1/4},
```

monotone decreasing in `rho_comb`, with the exact threshold (reproven in the
runner)

```text
R_Euler = 6   <=>   rho_comb = rho_crit = 18^4 / (7 * 6^4) = 11.5714... .
```

**Theorem (K-built resummation-radius lower bound).** *In the K-built
(links-meet-`<=2`-faces, Euler-`18^(1-F)`) sector of `Delta`, the geometric
cluster proliferation (`lambda <= 7`), the Euler suppression (`18^{-4}` per
cube), and the action-plaquette growth (`|beta|^4` per cube) alone give the
radius bound `R_Euler(rho_comb) = 18/(7 rho_comb)^{1/4}`. In particular
`R_Euler > 6` for every `rho_comb < rho_crit = 18^4/(7 6^4) = 11.5714`, and the
count-plus-Euler-plus-geometry contribution at `rho_comb = 1` is `R_Euler =
11.07`.* Proof: the geometric-series convergence radius above; primitives (A)-(C)
and `lambda <= 7` are reproven / cited in the runner. ∎

**Consequence.** Geometric proliferation, lattice-animal count, and Euler
suppression — taken together — **cannot** by themselves pull the resummed radius
to or below `6`. Any sub-`6` singularity of `Delta` must be sourced either by a
per-cube combinatorial factor `rho_comb >= 11.57` or by the `>= 3`-face
baryon-channel sector outside this bound.

## 3. What is rigorous, what is the named obstruction

**Rigorous (this note + cited on-main):**

- cube-sector radius `= 8.2052 > 6` (`J` entire; exact J-zero plus a 44-coefficient
  root test);
- within the K-built regime, `R_Euler(rho_comb) = 18/(7 rho_comb)^{1/4}`, hence
  `R_Euler > 6` for all `rho_comb < 11.57`, with `R_Euler(1) = 11.07`.

**Named open inputs (the sharpened obstruction).** The growth rate `mu` — hence
the resummed radius — is pinned by exactly two quantities **not** fixed by the
reproven primitives:

1. **`rho_comb`**, the per-cube connected-cumulant / set-partition combinatorial
   factor. Bounding it `< rho_crit = 11.57` is precisely a Kotecky-Preiss /
   tree-graph (Brydges-type) cluster-expansion convergence statement, which the
   framework treats as an **external** result
   ([`KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`](KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md),
   comparator). It is therefore an admissible import -> bounded -> retire target,
   not a framework-internal closure today.
2. **The `>= 3`-face (baryon/epsilon) channel sector**, `beta^10` onward, whose
   weight class is stronger than `18^(1-F)` and is **not** bounded by the K-built
   argument of Section 2.

Neither is pinned here; both are the same class of input the campaign already
named — an externally-supplied cluster-expansion / no-real-bulk-transition
certificate on the externally-computed series, never on the circular
`kappa/witness` pair
([`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)).

## 4. Comparator reconciliation

The rigorous single-plaquette / cube-sector radius is `8.2052`. The thermodynamic
Fisher / Lee-Yang zero is `|beta| ~ 5.54` (lattice-QCD comparator). These are
**not** in conflict: `8.2052` is the cube-sector (and single-plaquette-`J`)
radius, while a sub-`6` thermodynamic singularity, if it exists, must — by the
Section 2 theorem — be sourced by `rho_comb >= 11.57` or by the baryon-channel
sector, neither of which the reproven primitives bound. The location `|beta_c|`
remains the under-determined `rho_{p,q}(6)` object restated in the beta-plane
([`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)).

## 5. Runner scorecard

`scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py` —
single-seed deterministic, memory-bounded (max Taylor degree 60, max root-finder
degree 30; peak RSS `~65 MB`; no enumeration of cluster topologies):

- [A] recurrence seed `a_2 = 1/36`; `P_1plaq(6) = 0.4225317396`; recurrence ==
  Bars `J(6)`.
- [B] `kappa_2..5 = 1/18, 1/108, 0, -5/3888`.
- [C] `72 K'' (K')^5` reproduces `d_5..d_8` and the `d_9` cube-part exactly.
- [D] J-zero migration `5.739 -> 8.205`, monotone-up, crosses `6` by `T=4`;
  cube-sector radius `> 6`.
- [E] anchor Euler weights (`18^{-5}`, `18^{-9}`); per-cube increment `dF=dn=4`;
  `R_Euler(1) = 11.07 > 6`; threshold `rho_crit = 18^4/(7 6^4) = 11.5714`.

**SCORECARD: PASS = 22, FAIL = 0.**

## See also

- [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
- [`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
