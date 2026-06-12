# The Reconstructed Free Hamiltonian `H = −log(T̂²)/(2a_τ)` is Quasi-Local: Analytic-Dispersion Free-Surface Support for the Microcausality / Lieb-Robinson Bridge — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (free `U=1` surface; the quasi-locality of the reconstructed Hamiltonian)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
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
(finite range) needed for Lieb-Robinson"). This note supplies a **free-surface quasi-locality
support statement** for that gap: conditional on the cited free dispersion, the reconstructed
Hamiltonian has an exponentially decaying kernel by analyticity. It does not close the interacting
case and does not set a Lieb-Robinson velocity constant.

## Safe statement

On the free (`U=1`) staggered surface the reconstructed Hamiltonian is, in momentum space, the
exact three-spatial-dimensional free staggered dispersion (cited retained-bounded rungs)
```
E(p) = arcsinh( sqrt( m² + Σ_{μ=1}^{3} sin² p_μ ) ),    spec(T̂²) = e^{−2E(p)},
```
from
[`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
(`retained_bounded`) and
[`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
(`retained_bounded`). Its position-space kernel is `H(x) = FT[E(p)]`.

**Support theorem (quasi-locality of the reconstructed `H`, free `U=1`, `d=3` surface).**

1. **The transfer matrix is gapped away from 0.** `spec(T̂²) = e^{−2E(p)} ⊂ [e^{−2E_max}, e^{−2E_min}]`
   with `E_min = arcsinh(m) > 0` and `E_max = arcsinh(√(m²+3)) < ∞`, so `min spec(T̂²) > 0` and
   `H = −log(T̂²)/(2a_τ)` is well-defined and self-adjoint (`= E(p) ≥ 0`).

2. **The dispersion is real-analytic for `m>0`.** The radicand `R(p) = m² + Σ_μ sin² p_μ ≥ m² > 0`
   on the real torus and extends holomorphically as a polynomial in `cos 2p_μ`. In the complex
   strip before the first `R=0` singularity, one can choose the analytic branches of `√R` and
   `arcsinh(√R)`, so `E(p)` is real-analytic on `T^3` with positive strip width. Along one complex
   momentum direction the nearest branch point occurs at `sin² p = −m²`, giving half-width
   `a = arcsinh(m) > 0`; possible `arcsinh` branch points at `R=-1` are farther away on that line.

3. **Hence the supplied free `H` is quasi-local (exponential-tail kernel).** By
   Paley-Wiener / Bernstein, Fourier coefficients of a function analytic in a positive strip decay
   exponentially. The runner directly checks the axis marginal `H(x,0,0)`, which fits
   `x^{−p} e^{−a|x|}` with positive fitted rate compatible with the one-axis singularity scale
   `a = arcsinh(m)` over `m ∈ [0.1, 1]`. The rigorous claim here is the positive-strip
   quasi-locality implication for the supplied `d=3` dispersion, not an exact isotropic correlation
   length formula.

4. **The mass gap is load-bearing.** At `m = 0` the radicand vanishes at `p = 0` **on** the real
   torus, the analyticity strip closes (`a = 0`), and `H(x)` is a **pure power law** (`~ x^{−4}`,
   `R² > 0.999`), i.e. **not** quasi-local. So quasi-locality is supplied specifically by `m > 0`.

This is the free-surface quasi-local `H` support needed by the parent microcausality bridge. The
actual Lieb-Robinson velocity constant and overlap-weight formulation remain owned by the dedicated
Lieb-Robinson authority; this note does not assert the stale `2erJ` velocity formula.

## The genuine open piece

The **interacting** reconstructed Hamiltonian `H = −log(T̂[U]²)/(2a_τ)` quasi-locality (`U`-integrated
`SU(3)`) is **not** addressed here — its dispersion is not the closed-form free `E(p)`. This note is
the **free-surface** quasi-local support step, matching the free scope of rungs B/C.

## Boundary (honest)

- **Free (`U=1`) only.** The interacting quasi-locality is separate and open.
- **Quasi-local, not strictly finite-range.** `H(x)` has an exponential *tail* with an algebraic
  prefactor — the standard form for the kernel of an analytic dispersion; Lieb-Robinson uses
  exponentially-decaying (quasi-local) interactions, so this is the needed structure.
- **The decay rate is controlled by the analyticity strip.** The one-axis nearest singularity gives
  a positive rate scale `a = arcsinh(m)` for the checked axis marginal; the numerics confirm a
  compatible finite-window rate, while the rigorous claim (`a > 0`, exponential) rests on
  Paley-Wiener for the supplied analytic dispersion, not on the fitted value or an exact isotropic
  correlation length.
- No fitted/observed value; no new axiom (retained dispersion + standard analyticity-to-decay).

## Forbidden imports check

No new axiom. The dispersion `E(p)` is the retained free staggered transfer-matrix spectrum (rungs
B, C, both `retained_bounded`); the analyticity of `R(p) ≥ m² > 0` and the Paley-Wiener
exponential-decay implication are standard mathematics (reproven on the surface in the runner). The
interacting case is named open, not asserted.

## Runner check breakdown

Class A: (1) `spec(T̂²)` gapped away from 0 for `m>0`; (2) `R(p) ≥ m² > 0` on the `d=3` torus
(positive analyticity strip with one-axis scale `a = arcsinh(m)`); (3) the checked axis marginal
kernel fits `x^{−p} e^{−a|x|}` with exponential rate `a > 0` compatible with that scale
(quasi-local support); (4) `m=0` is pure power-law (`R² > 0.999`), the gap is
load-bearing. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is narrow: the free reconstructed Hamiltonian is the staggered dispersion `E(p)`;
its radicand stays `≥ m² > 0` on the real torus so `E(p)` is real-analytic in a positive complex
strip, and by Paley-Wiener its position-space kernel has an exponential tail (with the runner
checking the axis marginal by a combined power×exponential fit at a compatible `arcsinh(m)` scale);
the gapless
`m=0` case is pure power-law, confirming the mass gap is the load-bearing input. This is the
quasi-local `H` structure the parent microcausality / Lieb-Robinson bridge can consume on the free
surface. The full interacting `U`-integrated case and LR velocity constant are left open. Effective
status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py
```
