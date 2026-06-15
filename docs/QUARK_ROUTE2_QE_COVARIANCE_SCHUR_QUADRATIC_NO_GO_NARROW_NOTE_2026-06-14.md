# The Route-2 q_E Pin, Follow-On No-Go: the Covariance Bridge λ = q_E/q_T = κ² Is Not Forced Even by a Quadratic O_h-Invariant Functional (Sym²-Trivial-Multiplicity = 3); the E-Center Datum ρ_E Remains Open

**Date:** 2026-06-14
**Claim type:** no_go (strengthening of the Route-2 q_E covariance sharper no-go linked below; closes the quadratic route it left with a live mechanism)
**Status authority:** independent audit lane only. This source note does not set, predict, or estimate an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`](../scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py) (PASS=11 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.txt`](../logs/runner-cache/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.txt)

## The pin and what was left open

The `s3_time_primitive_chain` open gate's single missing Route-2 up-sector readout datum is
`c_TE = γ_T(center)/γ_E(center) = −8/9` (equivalently `ρ_E = β_E/α_E = 21/4`; `q_E = 1 + ρ_E/6 = 15/8`;
with the granted T-side `q_T = 5/6`, the covariance `λ := q_E/q_T = 9/4`). The standalone positive theorem
[`OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md`](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md)
derives the same-domain `O_h` shell leverage `κ = dim(T1)/dim(E) = 3/2` on the 7-site
octahedral star, so the *value* `9/4 = κ²` is structurally present; the sharper no-go
[`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md) showed
`O_h` equivariance does **not** supply the *bridge* `λ = κ²` (`Hom_Oh(E,T1) = 0`; the A1 center-excess
gives the **same** `1/6` increment to E and T; positivity leaves the `ρ_E > −6` continuum).

The one derivation hope #3844 left with a live mechanism was the **Sym² / "quadratic-forces-the-square"**
route: the bright tensor observable is built from the Einstein tensor (bilinear in the metric), so perhaps
the per-channel response scales as the **square** of the projector weight, forcing `q_E/q_T = κ²`. A
`/exercise` wall-exercise attacked exactly this. **Result: no derivation; the quadratic route is closed as
a theorem, and the datum remains an open readout input unless separately derived or explicitly admitted.**

## Exact content (every load-bearing fact independently re-verified by the runner)

**Reproven from #3844 (self-contained, so this note does not hard-depend on #3844 landing).**

- **K1 — `κ = 3/2` derived.** The 6-arm `O_h` permutation rep decomposes multiplicity-free as
  `A1g ⊕ Eg ⊕ T1u`; via the antipodal involution `A = ρ(−I)` the per-arm projector weights are
  `(P_A1, P_E, P_T1) = (1/6, 1/3, 1/2) = dim/6`, so `κ := P_T1/P_E = 3/2`, `κ² = 9/4`.
- **K3 — commutant independence.** `E`, `T1` are inequivalent `O_h` irreps, so `Hom_Oh(E,T1) = 0` (the
  Reynolds intertwiner vanishes): equivariance carries **independent** scalars `λ_E, λ_T`.
- **K4 — endpoint algebra.** With shell normalization + the granted T-side (`β_T/α_T = −1 → q_T = 5/6`;
  `α_T/α_E = −2`): `q_E = 1 + ρ_E/6`, `c_TE = −2·q_T/q_E`; the chain `ρ_E=21/4 ↔ q_E=15/8 ↔ c_TE=−8/9 ↔
  λ=9/4` holds exactly.
- **K5 — the pinning.** `9/4 = κ²` exactly; the bridge `λ = q_E/q_T = κ²` is **not** a consequence of K1/K3.

**The new closures (this note's contribution).**

- **Q1 — the quadratic-route kill (Schur).** `Sym²(perm₆)` contains the trivial rep **exactly 3 times**.
  Since `A1g, Eg, T1u` are each multiplicity-1, by Schur a general `O_h`-invariant quadratic form is
  `a·‖·‖_A1 + b·‖·‖_E + c·‖·‖_T1` with `a, b, c` **free** — three independent invariant quadratics, and the
  `E:T1` weight ratio `b:c` is a **free** reduced-matrix-element ratio. **So even a genuinely quadratic
  `O_h`-invariant functional does not force the covariance to `κ²`;** `9/4` is one point on a continuum.
  (Sanity: `Λ²(perm₆)` trivial mult = 0; trivial-in-`perm₆` = 1.)
- **Q2 — the inverse-square characterization (sharpest gap statement).** `λ = κ²` holds **iff** the
  per-channel lift scales as the **inverse square** of the channel's own per-arm projector weight,
  `q_X ∝ w_X⁻²`: `(w_E/w_T1)⁻² = 9/4`. The most common quadratic/bilinear constructions carry **one** power
  of the leverage — `(w_E/w_T1)⁻¹ = 3/2 = κ` (not the square) — and the Sym²-diagonal scaling `~ w_X²`
  gives `(w_E/w_T1)² = 4/9` (the wrong value, on the wrong channel). **No named functional produces an
  inverse-square-of-projector-weight center lift.**
- **Q3 — the ratio box-instability (corroboration; recomputed from the linked box-size scan cache).** From
  the box-scan outputs `q_E(N), q_T(N)` over `N ∈ {13,15,17,19,21,25}`, the recomputed ratio
  `λ(N) = q_E/q_T` is the **least** box-stable of the three quantities — `spread(λ) = 29.70 ≫
  spread(q_E) = 12.25 ≫ spread(q_T) = 2.96` — and `λ` equals `9/4` **only** at the pinning box `N=15`
  (`λ(N) = −0.04, 2.25, 29.66, 9.18, 6.59, 4.98`). So the "dynamics cancels in the ratio" reframing fails:
  the dynamics **amplifies** in the ratio; #3835's bulk-limit no-go is strengthened, not reframed away.

## Verdict

No derivation of `ρ_E = 21/4` was found. The covariance bridge `λ = q_E/q_T = κ²` is forced by **nothing
named**: equivariance leaves `λ_E, λ_T` independent (K3), the carrier is channel-blind (K5), and **now the
quadratic-invariant route is closed** — by Schur, an `O_h`-invariant quadratic form has a **free** `E:T1`
ratio (Q1), so `κ²` is one point on a continuum, not a consequence. The gap is exactly `q_X ∝ w_X⁻²` (Q2),
realized by no named functional, and the live box-scan ratio is the least box-stable quantity (Q3).
**`ρ_E = β_E/α_E` is a free direction in the (shell, center-excess) readout plane: an open supplied
datum, not adopted here.** `21/4` is moreover a nearest-rational over-idealization of a non-rational live
number (the box-size scan cache `q_E(N=15) = 1.876246` reconstructs a live `ρ_E = 6·(q_E−1) ≈ 5.26`, not
the exact `5.25`).

## No-go discipline gate (N1–N8)

- **N1 (alternative routes).** The quadratic route is separated into three sub-checks: (a) the abstract
  invariant-count — `Sym²(perm₆)` trivial mult = 3, so the `E:T1` quadratic ratio is free (Q1); (b) the
  scaling characterization — `λ=κ² ⇔ q_X∝w_X⁻²`, while the natural quadratic gives `q∝w` (one power) or
  `w²` (wrong value) (Q2); (c) the live functional — its actual ratio `λ(N)` is box-unstable and meets
  `9/4` only at `N=15` (Q3). None forces `λ=κ²`. These compose with #3844's already-separated equivariance
  / carrier / positivity routes.
- **N2 (wall independence).** Q1 (Schur free ratio), the equivariance independence (K3), the carrier
  channel-blindness (K5), and positivity (the `ρ_E>−6` continuum) each independently fail to fix `ρ_E`;
  closing one does not close the others.
- **N3 (hidden-wall scan).** `κ=3/2`, the projector weights, `Hom(E,T1)=0`, the `Sym²` and `Λ²` trivial
  multiplicities, the endpoint rationals, and the `(w_E/w_T1)` powers are all derived in exact arithmetic
  in the runner; no value is asserted by name or imported. Q3's `q_E(N), q_T(N)` are #3835's published
  outputs (cited), with the ratio and spreads recomputed here.
- **N4 (residual matching).** The residual is exactly the E-center datum / covariance `λ` named by the
  April naturality no-go and located at `λ=κ²` by #3844; this note removes the quadratic-functional escape
  from that residual without changing its logical force.
- **N5 (rhetoric).** "Closes the quadratic route" means the `Sym²`/quadratic-invariant mechanism cannot
  force `λ=κ²` (a theorem, Q1). It is **not** a claim that `ρ_E` is underivable by any future construction
  (N7), nor that `9/4=κ²` is a derivation or adopted input.
- **N6 (partial-closure).** Real partial content: `κ=3/2` is derived same-domain (K1); the missing step is
  the single covariance rule `λ=κ²` ⇔ `q_X∝w_X⁻²` (Q2) — a sharply characterized future derivation or
  owner-approved input target. No input is adopted here.
- **N7 (steelman).** A future genuinely **nonlinear** (non-quadratic) tensor observable, or a derived
  readout-covariance primitive supplying a `w⁻²` center-lift law, could still yield `λ=κ²`; this note does
  **not** prove impossibility over such constructions — it closes the finite-star / equivariant /
  carrier-linear / positivity / simple-covariance / **quadratic-invariant** routes.
- **N8 (cross-cycle echo).** Consistent with the naturality no-go (`ρ_E` free in the restricted class), the
  box-size scan (no bulk limit gives `15/8`), the `c_TE=−R_conn` cross-domain coincidence, and
  the linked `λ=κ²` relocation note; this note adds the quadratic-route closure.

## What is / is not claimed

- **Is:** `Sym²(perm₆)` has trivial multiplicity 3, so an `O_h`-invariant quadratic form has a free `E:T1`
  ratio (Q1, exact); `λ=κ² ⇔ q_X∝w_X⁻²` while the natural quadratic gives `κ` or `4/9` (Q2, exact); the
  recomputed `λ(N)` is the least box-stable quantity and meets `9/4` only at `N=15` (Q3, from the #3835
  cache); `κ=3/2`, `Hom(E,T1)=0`, and the endpoint chain are reproven exactly (K1/K3/K4/K5). The missing
  datum `ρ_E` therefore remains open in the finite-star / equivariant / carrier-linear / positivity /
  quadratic-invariant scope.
- **Is not:** does **not** derive `ρ_E=21/4`/`c_TE=−8/9`; does **not** prove impossibility over arbitrary
  future nonlinear observables (N7); does **not** identify `c_TE` with the color fraction `−R_conn` (that
  is the separate cross-domain coincidence no-go); does **not** use the `N=15` proximity as a derivation
  (the box-scan closed the limit route); adds no axiom, primitive, or fitted value.

## Provenance

This note records the narrowed output of a route-exercise pass; the load-bearing facts are the exact
runner checks above, not the exercise transcript.

## Load-bearing inputs

- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) — the P_R reduction + endpoint algebra (K4).
- [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) — the no-go this note further sharpens; its forbidden-inputs discipline binds here.
- [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) — the 7-site star + the A1 center-excess `1/6` (K5).
- [`CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md`](CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md) — the separate cross-domain color route (not this note's slot).
- [`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) — the open gate the datum belongs to.
- [`OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md`](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md) — the same-domain `κ=3/2` shell-leverage theorem, reproven locally here.
- [`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md) — the `λ=κ²` sharper no-go this note strengthens.
- [`QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md) — the box-size scan whose `q_E(N), q_T(N)` cache feeds the recomputed Q3 ratio.

## Forbidden-imports check

No PDG / observed / fitted value is consumed. The `O_h` projectors, `κ=3/2`, the `Sym²`/`Λ²` trivial
multiplicities, `Hom(E,T1)=0`, the endpoint rationals, and the `(w_E/w_T1)` powers are all derived in
exact arithmetic in the runner. The Q3 inputs `q_E(N), q_T(N)` are the linked box-scan outputs,
cited as such; the ratio and spreads are recomputed. The rationals `5/6, 15/8, −2, −8/9, 9/4, 21/4` appear
only as comparison targets, per the naturality no-go's comparator discipline.
