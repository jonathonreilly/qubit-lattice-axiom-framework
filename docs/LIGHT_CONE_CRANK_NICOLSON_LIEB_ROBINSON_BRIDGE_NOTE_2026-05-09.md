# Bounded Crank-Nicolson Lieb-Robinson Diagnostic for Light-Cone Framing

**Date:** 2026-05-09
**Type:** bounded_theorem
**Claim scope:** For finite-dimensional finite-range Hamiltonians with
support size `q`, support diameter `R`, per-site overlap weight `W`, and
subcritical Crank-Nicolson step size, the Cayley step
`U_CN = (I - i a_tau H/2)(I + i a_tau H/2)^(-1)` is unitary and is exactly
the time-`a_tau` evolution of the quasilocal effective generator
`H_CN = (2/a_tau) arctan(a_tau H/2)`. For any exponential weight `mu > 0`
with `x_mu := (a_tau/2) W exp(mu R) < 1`, this generator has finite weighted
overlap
`W_CN,mu <= (2/a_tau) artanh(x_mu)`, and its repeated steps obey

```text
    ||[alpha_t^CN(A_x), B_y]||
      <= 2 ||A_x|| ||B_y|| exp(-mu d(x,y) + 4 W_CN,mu |t|).
```

The result is a bounded finite-range-to-Crank-Nicolson bridge. It does not
prove locality for the full gauged/interacting exact reconstructed
Hamiltonian unless that Hamiltonian is separately supplied with retained
finite-range or quasilocal weighted-overlap constants.
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome.
**Primary runner:** `scripts/light_cone_crank_nicolson_lr_2026_05_09.py`

## Why this note exists

The light-cone framing note records 1+1d staggered-Dirac dispersion and
finite-spacing Crank-Nicolson containment behavior. A prior review
flagged that the note identified the containment behavior with standard
Lieb-Robinson behavior without deriving a constant for the actual
Crank-Nicolson time-step kernel.

The Hamiltonian-side work now available in
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
uses the overlap-weight convention. This repair supplies the missing
Crank-Nicolson composition step in the same convention and keeps the exact
framework reconstructed-H boundary explicit.

## Setup

Let `H` be a finite-dimensional Hermitian Hamiltonian. The
Crank-Nicolson step is the Cayley transform

```text
    U_CN(a_tau) = (I - i a_tau H/2) (I + i a_tau H/2)^(-1).
```

For a finite-range support family `H = sum_Z h_Z`, write:

```text
    q := max_Z |Z|,
    R := max_Z diam(Z),
    W := sup_x sum_{Z contains x} ||h_Z||.
```

The retained finite-range LR bridge gives the Hamiltonian-side velocity
`v_LR = 2 e q W R`. For the Crank-Nicolson step we need one stronger
weighted norm. For any `mu > 0`,

```text
    W_mu(H) := sup_x sum_{Z contains x} ||h_Z|| exp(mu diam(Z))
             <= W exp(mu R).
```

The Neumann expansion of the resolvent

```text
    (I + i a_tau H/2)^(-1) = sum_{n >= 0} (-i a_tau H/2)^n
```

is the source of the finite-step exponential tail when
`x_mu := (a_tau/2) W_mu(H) < 1`.

## Bounded Statements

**(CN-A) Cayley unitarity.** For Hermitian `H`, `U_CN(a_tau)` is unitary
because the numerator and denominator are adjoints and commute as
polynomials in `H`.

**(CN-B) Effective generator.** Spectral calculus gives

```text
    U_CN(a_tau) = exp(-i a_tau H_CN),
    H_CN := (2/a_tau) arctan(a_tau H/2).
```

For `x_mu := (a_tau/2) W_mu(H) < 1`, the odd power series for `arctan`
and the weighted convolution inequality give

```text
    W_mu(H_CN)
      <= (2/a_tau) sum_{n >= 0} x_mu^(2n+1)/(2n+1)
      <= (2/a_tau) artanh(x_mu)
      =: W_CN,mu.
```

The inequality uses absolute coefficients; it is conservative and does not
depend on cancellation in the alternating `arctan` series.

**(CN-C) Quasilocal n-step LR bound.** Repeated Crank-Nicolson steps obey

```text
    ||[alpha_t^CN(A_x), B_y]||
      <= 2 ||A_x|| ||B_y|| exp(-mu d(x,y) + 4 W_CN,mu |t|)
```

for one-site observables, with finite velocity
`v_CN,mu = 4 W_CN,mu / mu`.

**(CN-D) Continuum agreement.** At fixed time `t`, repeated
Crank-Nicolson steps converge to `exp(-i t H)` with the expected
second-order error. Also
`W_CN,mu -> W_mu(H)` as `a_tau -> 0`, so the Crank-Nicolson cone converges to
the Hamiltonian weighted-overlap cone in the small-step regime.

## Proof

For (CN-A), `I - i a_tau H/2` is the adjoint of `I + i a_tau H/2`, and both
are polynomials in the same Hermitian `H`; hence they commute and the Cayley
transform is unitary.

For (CN-B), use the spectral identity
`(1 - i z)/(1 + i z) = exp(-2 i arctan z)` with `z = a_tau H/2`. In a
weighted support norm, multiplication of support families is submultiplicative
because diameters add along paths. Therefore
`W_mu(H^n) <= W_mu(H)^n`. Taking absolute values in the `arctan` series gives
the displayed `artanh` bound whenever `x_mu < 1`.

For (CN-C), expand the Heisenberg evolution under `H_CN` in nested
commutators. A path from `x` to `y` carries a factor
`exp(-mu d(x,y))`, while the weighted sum over intermediate sites is bounded
by `W_CN,mu` at each step. The same path-counting argument used by the
finite-range overlap-weight LR bridge gives the conservative envelope with
`4 W_CN,mu |t|`. Constants are not optimized; only finite velocity and the
correct subcritical dependence are load-bearing.

For (CN-D), the Cayley transform is the `[1/1]` Pade approximation to
`exp(-i a_tau H)`, with local error `O(a_tau^3 ||H||^3)` and fixed-time
global error `O(a_tau^2 t ||H||^3)` in finite dimension.

## Runner Coverage

The companion runner checks:

- Cayley-transform unitarity for random finite-range Hermitian `H`.
- Per-step commutator decay from the Neumann-series tail.
- The subcritical weighted-overlap bound
  `W_CN,mu <= (2/a_tau) artanh((a_tau/2) W exp(mu R))`.
- An n-step LR inequality on finite nearest-neighbor chains using the derived
  `v_CN,mu = 4 W_CN,mu / mu` rather than a hard-coded diagnostic velocity.
- `O(a_tau^2)` convergence of `U_CN^n` to `exp(-i t H)`.
- Small-step agreement between Crank-Nicolson and continuous-time
  commutators.

The runner is intentionally finite and diagnostic. It does not build
the exact framework transfer-matrix logarithm and does not prove a
non-perturbative quasilocal bound for the repo's full dynamics.

## Hypothesis and Import Boundary

Load-bearing inputs:

- Bounded Hamiltonian-side action-support/J-budget context from
  [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md).
- Hermiticity of the finite toy Hamiltonians built by the runner.
- Cayley-transform spectral calculus and finite power-series algebra, proved
  above in the repository notation.
- Weighted-path Lieb-Robinson combinatorics, proved above in the same
  overlap-weight convention as the retained finite-range bridge.

Not imported as proof inputs: observed containment percentages,
fitted velocities, or a retained exact-H locality theorem.

## Audit Boundary

This note closes the finite-range Crank-Nicolson bridge at bounded-theorem
scope. It separates:

- what the finite-step Cayley transform is proved to do for subcritical
  finite-range support families;
- what remains open for the framework, namely an exact finite-range or
  quasilocal estimate for the reconstructed Hamiltonian and its
  Crank-Nicolson kernel.

## References

- Hamiltonian-side bounded support:
  [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
- Parent framing context, non-load-bearing here:
  `LIGHT_CONE_FRAMING_NOTE.md`
- Standard external theorem context:
  Lieb-Robinson 1972; Hastings 2004; Nachtergaele-Sims 2010; standard
  Padé/Crank-Nicolson second-order convergence.
