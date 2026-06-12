# The Reconstructed Free Hamiltonian `H = −log(T̂²)/(2a_τ)` Has an Axis Quasi-Local Kernel: Analytic-Dispersion Support for the Microcausality / Lieb-Robinson Bridge — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_support_theorem (free `U=1` surface; axis-kernel quasi-locality support for the reconstructed Hamiltonian)
**Status:** unaudited source repair candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py`](../scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py)
**Cached output:** [`logs/runner-cache/reconstructed_h_quasilocal_microcausality_bridge_runner.txt`](../logs/runner-cache/reconstructed_h_quasilocal_microcausality_bridge_runner.txt)

## Audit context

The parent microcausality / Lieb-Robinson note
[`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md)
(M2) needs the reconstructed Hamiltonian `H` to be **finite-range / quasi-local** so the standard
Lieb-Robinson bound applies. Its support note
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
bounds the **action-density** norm but states explicitly that it "**does not prove the exact
non-perturbative `H = −log(T)/a_τ` finite-range step**", and the audit row records the same gap
("the load-bearing finite-range-H … step is not [established] … not the locality structure
(finite range) needed for Lieb-Robinson"). This source repair takes the narrower, auditable route:
it supplies a one-axis reconstructed-`H` kernel support packet for the free surface. It does **not**
claim the full `d`-dimensional kernel theorem, the interacting `U`-integrated theorem, or the parent
Lieb-Robinson constant.

## 2026-06-12 audit-scope narrowing

The audit row requested one of two repairs: prove the full free staggered two-step dispersion kernel
or restrict to the supplied `1+1d`/axis result, weaken the rate to a positive strip bound, and remove
the stale `2erJ` Lieb-Robinson sentence. This note adopts the second route.

The paired runner computes the axis marginal
```
H_axis(x) = H(x,0,0)
```
by Fourier transforming the averaged free dispersion over transverse momenta. The retained claim is
only that, for `m > 0`, this axis kernel has a positive exponential tail compatible with the
analyticity strip. The full off-axis kernel, the interacting reconstructed Hamiltonian, and any
standalone parent microcausality/Lieb-Robinson closure remain outside this note.

## Safe statement

On the free (`U=1`) staggered surface the reconstructed Hamiltonian is, in momentum space, the
exact free staggered dispersion (retained rungs)
```
E(p) = arcsinh( sqrt( m² + Σ_μ sin² p_μ ) ),    spec(T̂²) = e^{−2E(p)},
```
from
[`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
(`retained_bounded`) and
[`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
(`retained_bounded`). Its axis marginal kernel is `H_axis(x) = H(x,0,0)`, obtained by averaging
`E(p)` over transverse momenta and Fourier transforming the remaining axis momentum.

**Theorem (axis-kernel quasi-locality support for the reconstructed `H`, free surface).**

1. **The transfer matrix is gapped away from 0.** `spec(T̂²) = e^{−2E(p)} ⊂ [e^{−2E_max}, e^{−2E_min}]`
   with `E_min = arcsinh(m) > 0` and `E_max = arcsinh(√(m²+d)) < ∞`, so `min spec(T̂²) > 0` and
   `H = −log(T̂²)/(2a_τ)` is well-defined and self-adjoint (`= E(p) ≥ 0`).

2. **The axis marginal has a positive analytic strip for `m>0`.** The radicand `R(p) = m² + Σ_μ sin² p_μ ≥ m² > 0`
   on the real torus and extends holomorphically as a polynomial in `cos 2p_μ`. In the complex
   strip before the first `R=0` singularity, one can choose the analytic branches of `√R` and
   `arcsinh(√R)`. Along the axis variable this gives a positive strip bound
   `a_axis >= c(m) > 0`; the one-variable singularity scale `arcsinh(m)` is the comparison scale used
   by the runner, not a full `d`-dimensional correlation-length theorem.

3. **Hence `H_axis` has a positive exponential tail.** By the one-variable Paley-Wiener / Bernstein
   implication, Fourier coefficients of a strip-analytic axis marginal decay exponentially:
   `H_axis(x) = O(poly(|x|) e^{-a_axis |x|})` for some `a_axis > 0`. The runner verifies a compatible
   finite-window fit `x^{-p} e^{-a|x|}` with positive `a` on `m in [0.1, 1]`.

4. **The mass gap is load-bearing.** At `m = 0` the radicand vanishes at `p = 0` **on** the real
   torus, the axis analyticity strip closes (`a = 0`), and `H_axis(x)` is a **pure power law**
   (`~ x^{−4}`, `R² > 0.999`), i.e. **not** quasi-local. So axis quasi-locality is supplied
   specifically by `m > 0`.

This is an axis-kernel support packet for the finite-range/quasi-local `H` gap. It does not by
itself supply the parent microcausality bound (M2), the full interaction graph summability needed
for a Lieb-Robinson theorem, or a `v_LR <= 2erJ` constant.

## The genuine open piece

The **interacting** reconstructed Hamiltonian `H = −log(T̂[U]²)/(2a_τ)` quasi-locality (`U`-integrated
`SU(3)`) is **not** addressed here — its dispersion is not the closed-form free `E(p)`. The full
free `d`-dimensional kernel theorem is also not asserted here. This note is an axis-kernel support
repair for the parent finite-range-H gap.

## Boundary (honest)

- **Free (`U=1`) axis marginal only.** The interacting quasi-locality and the full off-axis/free
  `d`-dimensional kernel theorem are separate and open.
- **Quasi-local support, not strictly finite-range closure.** `H_axis(x)` has an exponential tail with
  an algebraic prefactor; this is support for the bridge, not the bridge theorem itself.
- **The decay rate is a positive strip bound.** The one-axis nearest-singularity comparison gives the
  scale `arcsinh(m)`; the retained claim is only `a_axis > 0`, with numerics confirming a compatible
  finite-window rate.
- No fitted/observed value; no new axiom (retained dispersion + standard analyticity-to-decay).

## Forbidden imports check

No new axiom. The dispersion `E(p)` is the retained free staggered transfer-matrix spectrum (rungs
B, C, both `retained_bounded`); the axis strip positivity and the one-variable Paley-Wiener
exponential-decay implication are standard mathematics applied on this surface and checked in the
runner. The full off-axis/free kernel and interacting cases are named open, not asserted.

## Runner check breakdown

Class A: (1) `spec(T̂²)` gapped away from 0 for `m>0`; (2) `R(p) ≥ m² > 0` on the torus gives a
positive axis analyticity strip; (3) the axis kernel `H(x,0,0)` fits `x^{-p} e^{-a|x|}` with
exponential rate `a > 0` compatible with `arcsinh(m)`; (4) `m=0` is pure power-law (`R² > 0.999`),
the gap is load-bearing. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is narrow: the free reconstructed Hamiltonian has the staggered dispersion
`E(p)`; its radicand stays `>= m² > 0` on the real torus, giving a positive strip for the axis
marginal, and by the one-variable Paley-Wiener implication the axis kernel `H(x,0,0)` has an
exponential tail (verified numerically by a combined power times exponential fit at a positive rate
compatible with `arcsinh(m)`). The gapless `m=0` case is pure power-law, confirming the mass gap is
the load-bearing input. This is support for the parent microcausality / Lieb-Robinson finite-range-H
gap; it does not close the full bridge, the full off-axis/free kernel theorem, or the interacting
`U`-integrated case. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py
```
