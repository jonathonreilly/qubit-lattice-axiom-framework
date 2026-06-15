# The O_h Seven-Site-Star Shell-Leverage Constants (Positive Theorem): Per-Arm Isotypic Weights (1/6, 1/3, 1/2), κ = dim(T1)/dim(E) = 3/2, and Hom_Oh(E,T1) = 0

**Date:** 2026-06-10
**Claim type:** positive_theorem (exact, unconditional, box-independent representation theory)
**Status authority:** independent audit lane only. This source note does not set, predict, or estimate an audit outcome.
**Primary runner:** [`scripts/frontier_oh_seven_site_star_shell_leverage_positive_theorem_2026_06_10.py`](../scripts/frontier_oh_seven_site_star_shell_leverage_positive_theorem_2026_06_10.py) (PASS=5 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_oh_seven_site_star_shell_leverage_positive_theorem_2026_06_10.txt`](../logs/runner-cache/frontier_oh_seven_site_star_shell_leverage_positive_theorem_2026_06_10.txt)

## Statement

On the framework's 7-site octahedral star support (1 center + 6 arms ±x,±y,±z), the 6-arm `O_h`
permutation representation decomposes **multiplicity-free** as `A1g ⊕ Eg ⊕ T1u`, and:

1. **(L1–L2) Per-arm isotypic weights are exactly `(A1, E, T1) = (1/6, 1/3, 1/2) = dim/6`** — the
   universal multiplicity-free transitive-permutation-rep value (every arm's `O_h`-orbit is all 6 arms).
   The isotypic projectors are mutually orthogonal equivariant idempotents of ranks `(1,2,3)` summing to
   the identity (built group-theoretically: `P_A1` = Reynolds average, `P_T1 = (I−A)/2` with `A` the
   antipodal involution `= ρ(−I)`, `P_E = (I+A)/2 − P_A1`).
2. **(L3) The shell leverage** `κ := P_T1(arm,arm)/P_E(arm,arm) = (1/2)/(1/3) = 3/2 = dim(T1)/dim(E)`,
   and `κ² = 9/4`. Equivalently the per-arm weight ratios `A1:E:T1 = 1:2:3` are the irrep dimensions.
3. **(L4) `Hom_Oh(E,T1) = 0`** (E and T1 are inequivalent irreps; the Reynolds intertwiner vanishes), so
   the `O_h`-equivariant commutant on the arm space is 3-dimensional (one independent scalar per block) —
   equivariance imposes **no** relation between the E and T1 scales.
4. **(L5) Structural / box-independent:** the projectors are pure group averages with no dynamics,
   Green's function, or embedding-box input, so `κ = 3/2` is an exact constant of the star geometry,
   invariant under arm relabeling and independent of any embedding box size.

All verified in exact finite-group arithmetic (`|O_h| = 48` signed permutation matrices) in the runner.

## What is / is not claimed

- **Is:** the exact multiplicity-free decomposition, the per-arm weights `(1/6, 1/3, 1/2)`, the leverage
  `κ = 3/2 = dim(T1)/dim(E)` (`κ²=9/4`), `Hom_Oh(E,T1)=0` with independent E/T equivariant scales, and the
  box-independence of all of these — a clean unconditional structural lemma about the support star.
- **Is not:** this lemma does **not**, by itself, derive any Route-2 readout entry, mass ratio, or the
  value `ρ_E = 21/4` / `c_TE = −8/9`. Those require the additional **covariance bridge `q_E/q_T = κ²`**,
  which this structure does **not** supply — see the companion no-go
  [`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)
  (in review). This note carves out only the load-bearing positive content. Adds no axiom, primitive, or
  fitted value.

## Load-bearing inputs

- [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) — fixes the
  7-site octahedral star support and the `O_h`-adapted A1/E/T1 channels used here.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the `Z³` lattice / cubic `O_h`
  point-group symmetry whose representation theory this lemma computes.

## Forbidden-imports check

No PDG / fitted / observed value is consumed. The decomposition, projectors, per-arm weights, `κ=3/2`,
and `Hom_Oh(E,T1)=0` are all computed in exact finite-group arithmetic from the `O_h` action on the
6 arms. The fractions `1/6, 1/3, 1/2, 3/2, 9/4` are theorem outputs, not inputs.
