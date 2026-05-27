# Mermin-Wagner / Hohenberg Bogoliubov Infrared Certificate

**Date:** 2026-05-18 (bounded-certificate repair: 2026-05-27)
**Claim type:** bounded_theorem
**Status:** bounded Bogoliubov/infrared certificate; external
Mermin-Wagner, Hohenberg, and Coleman references are parallel literature
citations, not load-bearing retained-grade imports.
**Runner:** `scripts/mermin_wagner_bogoliubov_bounded_certificate.py`
**Status authority:** independent audit lane only.

## Purpose

This packet replaces the former named-import wrapper with a direct finite
lattice certificate for the part of the Mermin-Wagner/Hohenberg machinery that
the downstream repo notes actually use:

- the finite Gibbs-state Bogoliubov inequality;
- the lattice Goldstone dispersion `E_k = 2 sum_mu (1 - cos k_mu)` on `Z^d`;
- the infrared sum `I_d(L) = L^{-d} sum_{k != 0} 1/E_k`;
- the dimension threshold `I_d -> infinity` for `d <= 2`, with the framework-
  relevant `d=3` finite-window behavior checked explicitly;
- the conditional consequence that a finite Bogoliubov double-commutator
  constant forces the continuous-symmetry order parameter to vanish when
  `I_d` diverges.

The packet does not add an axiom. It uses finite-dimensional Hilbert-space
algebra, the standard `Z^d` lattice dispersion, and explicitly stated local
Hamiltonian hypotheses. It does not derive the classical Mermin-Wagner,
Hohenberg, or Coleman theorems from `Cl(3,0)` on `Z^3`.

## Local Theorem

Let `H_L` be a finite-dimensional Hermitian Hamiltonian on a periodic
`L^d` lattice block with Gibbs state

```text
rho_beta = exp(-beta H_L) / tr(exp(-beta H_L)),   beta > 0.
```

For finite operators `A` and `C`,

```text
| <[C,A]>_beta |^2
    <= (beta/2) <{A,A^dagger}>_beta <[[C,H_L],C^dagger]>_beta.     (B)
```

This is a finite matrix inequality: diagonalize `H_L`, write the thermal
expectation in the energy basis, and apply Cauchy-Schwarz to the weighted
matrix-element sum. No continuum theorem is imported.

For a translation-invariant local Hamiltonian whose long-wavelength
continuous-symmetry charge mode has a finite double-commutator bound

```text
<[[q_k,H_L],q_k^dagger]>_beta <= C E_k
```

with `C < infinity` independent of `L`, `E_k = 2 sum_mu(1 - cos k_mu)`,
and a finite onsite anticommutator/susceptibility bound, the standard
Bogoliubov summation gives

```text
|m_L|^2 <= C' / I_d(L),
I_d(L) = L^{-d} sum_{k != 0} 1/E_k.                              (CMW)
```

Thus the bounded implication is:

```text
I_d(L) -> infinity  =>  m_L -> 0.
```

For the lattice dispersion above:

- `d=1`: `I_1(L) = (L^2 - 1)/(12L)`, so `I_1(L)` diverges linearly.
- `d=2`: `I_2(L)` diverges logarithmically by comparison with
  `int d^2 k / |k|^2`.
- `d>=3`: the corresponding infrared integral is finite at `k=0`; the runner
  checks the framework-relevant `d=3` finite-window behavior.

This is the bounded audit target in this packet.

## Runner Certificate

[`scripts/mermin_wagner_bogoliubov_bounded_certificate.py`](../scripts/mermin_wagner_bogoliubov_bounded_certificate.py)
checks the finite ingredients without using external theorem text:

- random finite Gibbs-state matrix instances of inequality (B);
- the exact one-dimensional identity for `I_1(L)`;
- monotone logarithmic growth of `I_2(L)` over a finite ladder;
- bounded/converging behavior of `I_3(L)` over a finite ladder;
- decreasing order-parameter upper bounds `sqrt(1/I_d(L))` for `d=1,2`.

The cache reports `PASS=5 FAIL=0`.

## Literature Citations In Parallel

The external literature is now cited as historical/contextual confirmation of
the same mathematical mechanism, not as an uninspected source of retained
authority:

- N. N. Bogoliubov, 1962: original inequality behind the finite-temperature
  argument.
- N. D. Mermin and H. Wagner, 1966: finite-temperature no-breaking theorem for
  continuous symmetries in one and two spatial dimensions under short-range
  hypotheses.
- P. C. Hohenberg, 1967: related finite-temperature low-dimensional ordering
  obstruction for Bose systems and crystalline order.
- S. Coleman, 1973: relativistic `1+1` zero-temperature analogue via the
  infrared singularity of massless scalar fields.

Coleman's relativistic zero-temperature theorem is not re-derived or retained
by this packet. It remains a parallel citation. Downstream claims that need the
full Coleman QFT theorem need a separate bounded, framework-derived, or
retained-grade authority packet.

## Hypotheses And Boundary

The bounded theorem is conditional on the explicit local Hamiltonian
conditions in (CMW):

- finite onsite Hilbert space or a regulated finite-dimensional local algebra;
- finite beta Gibbs state;
- translation invariance on the tested `Z^d` block;
- a continuous global symmetry with charge mode `q_k`;
- finite onsite anticommutator/susceptibility bound;
- local/short-range dynamics giving the double-commutator estimate
  `<[[q_k,H_L],q_k^dagger]> <= C E_k` with `C` independent of `L`.

The packet does not claim:

- a proof for arbitrary long-range Hamiltonians;
- a proof of every Hohenberg/Coleman hypothesis;
- a zero-temperature relativistic Coleman theorem;
- closure of the downstream `d_s=3` minimality theorem, which still depends on
  its own D9/kernel premise and audit state.

The purpose is narrower and cleaner: the repo now carries the finite
Bogoliubov/IR mechanism directly, while citing the classical papers in
parallel.
