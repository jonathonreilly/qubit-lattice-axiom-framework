# eps* Full-Kernel Finite-Scale Quotient: the Divided-Difference Term Flips the Proxy Sign (Bounded Finite-Cell Note, 2026-06-12)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not set, predict, or edit any audit outcome.
**Primary runner:** [`scripts/frontier_epsstar_full_kernel_coefficient_2026_06_12.py`](../scripts/frontier_epsstar_full_kernel_coefficient_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_epsstar_full_kernel_coefficient_2026_06_12.txt`](../logs/runner-cache/frontier_epsstar_full_kernel_coefficient_2026_06_12.txt)
**No-promotion statement:** This source note creates no promotion, no registry
edit, no audit verdict, and no downstream status change; status remains owned
by the independent audit lane.

## Bounded claim

Adopt exactly the finite one-particle Harper/PT protocol specified below.  On
its `Q=24`, `Ly=2`, `GL=20`, `m=0` grid, define the finite-scale full-kernel
quotient at `T_q=0.05` and decompose it using the two terms of the same PT
response by

```text
q_X(T_q) = -2 mu0 [chi_X(mu0,T_q)/T_q^2] / R0'(mu0),
X in {seagull, divided-difference, full},
chi_full = chi_seagull + chi_divided-difference .
```

The runner directly computes

```text
mu0             =   +1.515550712171
alpha_proxy     =   -9.266358431851
q_seagull(T_q)  = -274.281620146559
q_kernel(T_q)   = +278.423438570262
q_full(T_q)     =   +4.141818423703 .
```

Here `alpha_proxy` is the separately regularized fixed-Gaussian Sommerfeld
precursor.  The load-bearing decomposition instead compares the two terms of
the same finite-`T_q` response: `q_seagull < 0`, `q_kernel > 0`,
`q_kernel > |q_seagull|`, and `q_full=q_seagull+q_kernel`.  Therefore the
finite-temperature divided-difference term flips the same-response seagull
sign, while the resulting full readout also has the opposite sign from the
naive precursor proxy.
Separately, a least-squares characterization of the four declared
finite-temperature boundary roots gives

```text
mu*(T)^2 = c_grid + d_grid T^2
d_grid = +3.877078419951
```

on `T in {0.10,0.15,0.20,0.25}`.  Both finite-grid readouts are positive and
their computed relative difference is `0.06828337605706`, which lies inside
the pre-existing `0.15` comparison band.  This last inequality is an internal
finite-grid comparison, not a numerical error bar and not a second derivation.

The sign statement has an explicit algebraic robustness margin.  If each of
the four displayed quantities `q_seagull`, `q_kernel`, `q_full`, and `d_grid`
is independently perturbed by less than

```text
r_sign = 0.5 min(-q_seagull, q_kernel,
                 q_kernel-|q_seagull|, q_full, d_grid)
       = 1.938539209975,
```

all four sign inequalities remain strict.  This is a bound on perturbations of
the declared finite-grid outputs; it is not an estimate of continuum,
quadrature-order, regulator, or `T -> 0` error.

## Direct Harper/PT bridge

The finite model and PT readout are not selected by the minimal axioms.  They
enter this bounded theorem through the retained-bounded finite-matrix
construction in
[`LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md`](LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md).
For completeness, the runner instantiates that construction rather than
importing its output values:

- the `48 x 48` periodic one-particle matrix has nearest-neighbor hopping
  `t=1`, `Lx=Q=24`, `Ly=2`, and diagonal staggered mass
  `m(-1)^(x+y)` with `m=0` here;
- in the fixed Peierls gauge, every positive-y hop carries `exp(i B x)`, and
  `H1` and `H2` are the coefficients in
  `H(B)=H0+B H1+B^2 H2+O(B^3)`;
- each Brillouin-zone direction is averaged with the declared order-20
  Gauss-Legendre rule, followed by division by the 48 sites;
- for eigenpairs of `H0`, the response is

```text
chi_PT(mu,T)
  = 2 sum_i f(E_i;mu,T) <i|H2|i>
    + sum_ij K_ij(mu,T) |<i|H1|j>|^2,

K_ij = [f(E_i)-f(E_j)]/(E_i-E_j),
K_ii = f'(E_i).
```

The upstream finite-matrix derivation obtains this formula by twice
differentiating the grand-potential trace.  The current runner rebuilds the
matrices, diagonalizes them, evaluates both terms, and bisects the response
roots; no Hamiltonian, root, quotient, or fitted slope is read from the
dependency note.

## Declared finite protocol choices

The remaining choices are explicit conditions defining this theorem's finite
protocol, not framework-derived physical selectors:

| Choice | Role | Claim boundary |
|---|---|---|
| branch bracket `[1.2,2.4]`, 60 bisection steps | deterministic root readout on each listed finite-`T` row | no global uniqueness or physical branch-selection claim |
| Gaussian surface width `eta=0.05` and branch window `[1.48,1.56]` | defines the regularized `T=0` proxy root `mu0` | no delta-limit or physical surface-width claim |
| centered derivative step `h=0.02` | defines `R0'(mu0)` and `alpha_proxy` on this protocol | no `h -> 0` claim |
| quotient temperature `T_q=0.05` | defines `q_full(T_q)` | not a controlled `T -> 0` coefficient |
| slope grid `{0.10,0.15,0.20,0.25}` | defines `d_grid` by least squares | regression characterization only |
| comparison band `0.15` | frozen internal acceptance band | not derived uncertainty or physics tolerance |

These conditions are reproducibility coordinates.  They introduce no
empirical target, fitted physical parameter, unit bridge, probability rule,
or observable identification beyond the declared finite-matrix response.

## Coefficient-limit boundary

The retained-bounded diagnostic
[`EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md`](EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md)
tests the genuine fixed sequence `T={0.08,0.04,0.02,0.01}`.  Its quotient
sequence is non-asymptotic on this finite cell, its fitted extrapolant is
negative, and the extrapolated split does not satisfy the `m=0` sign-flip
inequalities.  Consequently this note makes none of the following claims:

- `q_full(0.05)` is `d mu*(T)^2/d(T^2)` at `T=0`;
- the `6.83%` difference is an `O(eta^2)` truncation estimate;
- the finite-scale `q_kernel(T_q)` is a common-limit asymptotic kernel coefficient;
- the result persists under changing `GL`, `eta`, `h`, the branch protocol,
  cell size, or a continuum limit.

The word “coefficient” in the historical filename identifies the lane.  The
load-bearing statement repaired here is only the displayed finite-scale
quotient/sign identity and the separate finite-grid regression comparison.

## Executable gates

The runner checks:

- the finite Harper/PT matrices and full divided-difference response directly;
- the `T=0` proxy root and negative `alpha_proxy`;
- nontrivial interband `|H1|` weight;
- every declared finite-temperature boundary root and the positive `d_grid`;
- the same-response identity `q_full=q_seagull+q_kernel` and its strict
  finite-scale sign-flip inequalities;
- the explicit algebraic sign-robustness radius;
- the `6.83% < 15%` arithmetic comparison, labelled as a finite-grid band;
- live markdown dependency links to the retained-bounded Harper/PT bridge and
  Richardson boundary, with no minimal-axiom dependency claim.

## Scope

This is a bounded finite-cell, finite-quadrature, finite-regulator numerical
theorem on the `m=0` axis.  It is not a first-principles framework theorem, a
controlled coefficient limit, a continuum theorem, a full `(m,T)` surface
theorem, or a physical observable/readout derivation.  Memory: one-particle
only.

The audit lane grades.

## Dependencies

- [`LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md`](LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the retained-bounded finite Harper matrix and second-order
  divided-difference response construction.
- [`EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md`](EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md)
  supplies the retained-bounded fixed-sequence diagnostic showing that this
  packet does not supply a controlled `T -> 0` coefficient.
