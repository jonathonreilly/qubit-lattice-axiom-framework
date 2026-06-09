# The W Metric-Hessian Identification and the Full Finite-k Channel Table: the Induced Action is a Positive but Anisotropic, Same-Sign, Gauge-Unsuppressed Stiffness — Not the Einstein Operator

**Date:** 2026-06-09
**Claim type:** bounded_theorem / finite-Brillouin-zone source certificate
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.py`](../scripts/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.py) (PASS=12 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.txt`](../logs/runner-cache/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.txt)

## Scope (builds the named-open items of two landed rows)

[`UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md)
left open: the full finite-`k` metric-source Hessian of `W` with contact terms, the full symmetric
vertex + diffeomorphism Ward identity, the `E_g/T_2g` spin-2 isotropy, magnitude, chiral control.
[`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md)
left open: "the identification of this runner-defined vertex/seagull with the complete metric Hessian
of `W`". This note computes those objects on the native elliptic operator
`D(q) = i(σ·sin q) + m` and answers whether the opposite-signed curvature comparator that
[`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md)
had to **supply** (`V_trace = −k²/2`, `V_TT = +k²/2`) is **induced** natively by `W` at finite `k`.

## Finding 1 — the identification bridge is derived (no longer "runner-defined")

A **declared local vielbein link coupling** — hop weight
`(σ_ν + Σ_α H_{αν} h(x_mid) σ_α)/2` forward, minus backward, with `h` at link midpoints — has its
**exact** second variation of `W = log|det D[h]|` (position space, explicit `−Tr(GδDGδD)` **and** an
independent `log|det|` second difference) **equal** to the momentum-space bubble with the midpoint
vertex `V_H = (i/2) Σ H_{αν} σ_α sin(q̄_ν)`, `q̄ = q+k/2` (exact to all printed digits, three channels).
So the **naive-type stress vertex IS the exact `W` metric Hessian of a declared local metric coupling**
(linear coupling ⟹ no seagull in this scheme), and the conserved (velocity×momentum) scheme of the
landed seagull row differs from it by an **exhibited local improvement term**
`V_cons − V_naive = (i/2) Σ H σ_α (cos(q̄_α)−1) s̄_ν` (identity verified to `1.6e-16` at random
`(q,k,H)`) plus the local diamagnetic seagull — the lattice analogue of stress-tensor improvement
(Callan–Coleman–Jackiw; cited as context). The landed Ward facts are reproduced: the declared-metric
(naive) scheme fails transversality (residual `0.167`); conserved + seagull is `O(k₀³)`-transverse
(`res/k₀³ = 0.0111, 0.0108, 0.0100`).

## Finding 2 — the spin-2 sector extended, with an honest negative

Unit-Frobenius-norm channel slopes at `k = 2π/16`, `m = 1` (induced action; healthy TT = positive):

| channel | conserved scheme | naive (metric) scheme |
|---|---|---|
| TT yz (`T_2g`) | **+0.006469** | +0.009321 |
| TT (yy−zz)/√2 (`E_g`) | **+0.003091** | +0.010295 |
| gauge xy, xz | +0.005779 | +0.001495 |
| gauge xx | +0.001442 | −0.001152 |
| transverse trace (yy+zz)/√2 | +0.003091 | +0.008361 |
| full trace δ/√3 | +0.002541 | −0.001750 |

- **Both** TT channels are positive — scheme-robust, mass-robust (`m ∈ {0.5,1,1.5,2}`), BZ-convergent.
  This extends the landed yz diagnostic to the full spin-2 pair.
- **But** the `E_g/T_2g` stiffness anisotropy is **O(1)** (split ≈ 0.52), **k-stable**
  (0.522/0.523/0.523 over `k = 0.39/0.26/0.20`) and **persists (grows) toward lighter mass**
  (0.522 → 0.561 → 0.605 for `m = 1 → 0.5 → 0.25`): the induced stiffness is **UV(lattice)-dominated**,
  i.e. genuine cubic anisotropy of the induced "elastic" constants, not a finite-`k` artifact. The
  induced action does **not** deliver an emergent-SO(3)-isotropic graviton kinetic term by itself.
- The seagull is `k`-independent and cancels **exactly** in slope differences (verified `0.0e+00`), so
  the slope table is seagull-normalization-independent.

## Finding 3 — the #3220 comparator is NOT induced (a finite-k sharpening of the no-go)

- The conserved-scheme induced **trace stiffness is positive** — **same sign as TT**.
- Sharper: the transverse trace-vs-shear splitting is **zero at machine precision**
  (`+1.4e-16` at `(N16, m1, k=2π/16)`; `+8.7e-18` at `(N12, m0.7, k=4π/12)`): the `k=0` trace=shear
  **degeneracy persists at finite `k` exactly**. Mechanism (verified by the contrast): the conserved
  vertex's per-component `cos(q̄)sin(q̄)` factor is π-periodic, so the `q_y → q_y+π` BZ shift flips the
  cross-term integrand and kills `Π_{yy,zz}` exactly; the naive scheme's `sin(q̄)` is not π-periodic,
  hence its small nonzero splitting (`−1.9e-3`).
- Pure-gauge channels (`h = k_(a ξ_b)` for `k‖x`) are **not suppressed** relative to TT in either scheme
  at the slope level (max|gauge|/TT ≈ 0.89 conserved, 0.16 naive): the seagull fixes the longitudinal
  **contact** structure (transversality `O(k₀³)`), not slope-level gauge decoupling — this is the
  **measured lattice diffeomorphism-breaking of the induced action at `O(k²)`**.

**Net:** the one-loop `W` induced action at finite `k` is a healthy-**positive** but **anisotropic,
same-sign, gauge-unsuppressed** elastic stiffness — structurally **not** the Einstein/Lichnerowicz
operator. The opposite-signed trace/TT pair the degenerate-supermetric no-go needed remains **supplied,
not induced**: the curvature-sign structure must come from elsewhere (e.g. the geometric/Regge route,
retained `cubic_coxeter_regge_deficit_vanishing` context). This **strengthens the division of labor**:
matter `W` supplies positivity; the geometric route must supply the GR structure.

## What is and is not claimed

- **Is:** the identification bridge (Finding 1) is exact and runner-derived; the channel table, the
  anisotropy persistence, the exact transverse degeneracy + its π-shift mechanism, the gauge
  non-suppression, and the not-induced verdict on the supplied comparator are finite-BZ measured facts
  for the native elliptic operator, mass- and BZ-scanned as stated.
- **Is not:** not a continuum dispersion law (deep scaling `k ≪ m ≪ 1` with `q_min ≪ m` is beyond this
  runner); not a unique-coupling theorem (the local improvement freedom is exhibited, not eliminated);
  not a derivation of the GR channel signs from any route; not full GR closure; no statement about the
  geometric/Regge route beyond citing it as the remaining carrier of the curvature-sign structure.
  Adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- 3D native elliptic operator (the landed rows' setting); the time/lapse–shift channels and 4D
  symmetric `Z³×Z_τ` extension are untested here.
- The chiral-limit control remains bounded by 3D IR behavior (`m ≳ q_min` throughout; the light-mass
  trend is reported at accessible sizes only).
- The induced-stiffness magnitude is reported in lattice units (`c_TT/a²`); with the registered
  [`scale_reference_primitive`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (`a⁻¹ = M_Pl`) this is a units
  remark only — no dimensionless physics is granted.
- The `k=0` anchor facts (TT kernel of the s-form coupling; degenerate supermetric) are the landed
  rows', cited; this note's `k=0` consistency is via the scheme relation, not a re-derivation:
  [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md).

## Load-bearing inputs

- [`UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the landed finite-`k` yz diagnostic + named-open list this note builds.
- [`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the conserved vertex + seagull scheme whose identification gap this note closes.
- [`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the supplied comparator this note tests (verdict: not induced; degeneracy persists at finite `k`).
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the `k=0` scalar-kernel anchor.
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — units remark only.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. Every number is computed from the declared lattice
objects in the runner; the landed rows' constructions are reproduced in-runner where cited (naive
residual, cubic transversality). Sakharov induced gravity, Adler–Zee, and Callan–Coleman–Jackiw
improvement are cited as **context/comparators only** — no formula or value from them enters any check.
