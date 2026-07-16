---
claim_id: reconstructed_h_quasilocal_from_analytic_dispersion_microcausality_bridge_narrow_theorem_note_2026-06-06
claim_type_author_hint: bounded_theorem
---

# Fixed-Mass One-Particle Log-Transfer Kernel: One-Coordinate Contour Bound

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Claim boundary:** bounded one-particle fixed-mass contour support. This note
does not prove a Lieb-Robinson bound, microcausality, or a sharp light cone.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py`](../scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py)
**Cached output:**
[`logs/runner-cache/reconstructed_h_quasilocal_microcausality_bridge_runner.txt`](../logs/runner-cache/reconstructed_h_quasilocal_microcausality_bridge_runner.txt)

## Question

What does the supplied free staggered two-step dispersion prove before any
many-body Lieb-Robinson composition or continuum causal interpretation is
added?

It proves a one-particle kernel statement. At fixed `m > 0`, the decaying
one-particle transfer eigenvalue has an analytic continuation in one momentum
coordinate while the transverse momenta remain real. The corresponding axis
Fourier coefficients decay exponentially for every contour height strictly
below `arcsinh(m)`. The physical Hamiltonian carries the required overall
`1/a_tau` factor.

## Inputs and object types

- The free `d`-dimensional one-particle dispersion is supplied by
  [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md):

  ```text
  E_d(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu)),   m > 0.
  ```

- The distinction between the decaying one-particle channel and its
  second-quantized Fock lift is supplied by
  [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md).

- `a_tau > 0` is the supplied blocked-time interval appearing in
  `H_hat = -log(T_hat^2)/(2 a_tau)`. This note does not identify that
  parameter with a record clock or derive a record-time normalization.

## Spectrum split and correct units

On the one-particle space, the decaying contraction is

```text
K e_p = exp(-2 E_d(p)) e_p,
spec(K) subset [exp(-2 E_max), exp(-2 E_min)],
E_min = arcsinh(m),
E_max = arcsinh(sqrt(m^2 + d)).
```

This interval is **not** the full Fock spectrum. On a finite periodic volume,
the second-quantized transfer is

```text
T_hat^2 = Gamma(K),
spec(T_hat^2)
  = { exp(-2 sum_p n_p E_d(p)) : n_p in {0,1} }.
```

The vacuum eigenvalue is `1`, and multiparticle products can lie below the
one-particle interval. Correspondingly,

```text
H_hat = -log(T_hat^2)/(2 a_tau)
      = sum_p (E_d(p) / a_tau) n_p.
```

Thus the one-particle Hamiltonian symbol is `E_d(p)/a_tau`, not `E_d(p)`
unless the special convention `a_tau = 1` has been imposed.

## One-coordinate contour theorem

Fix one coordinate, say `p_1`, keep `p_perp` real, and write

```text
R(p_1,p_perp) = m^2 + sin^2(p_1) + sum_{mu>1} sin^2(p_mu).
```

For `p_1 = x + i y`,

```text
Re R = m^2 + sum_{mu>1} sin^2(p_mu)
       + sin^2(x) cosh(2y) - sinh^2(y).
```

Therefore, for every fixed `0 < rho < arcsinh(m)` and every
`|y| <= rho`,

```text
Re R >= m^2 - sinh^2(rho) > 0.
```

The radicand stays in the open right half-plane. The principal square-root
and `arcsinh` branches are analytic on this **one-coordinate strip**. No
simultaneous polystrip of the same width is asserted.

For the axis coefficient

```text
h(n e_1)
  = (1/a_tau) (2 pi)^(-d)
    int_{T^d} E_d(p) exp(i n p_1) d^d p,
```

compactness of the shifted contour gives a finite

```text
M_rho(m,d) = sup |E_d(p_1 + i y,p_perp)|,
             |y| <= rho, p_perp real,
```

and contour shifting yields

```text
|h(n e_1)| <= (M_rho(m,d)/a_tau) exp(-rho |n|).
```

This is the bounded mathematical content of this source packet: a
fixed-mass one-particle axis-kernel bound with correct energy units.

## Open bridges not supplied here

This note does **not** supply any of the following:

1. a Fock-space interaction decomposition with a certified exponentially
   weighted overlap norm;
2. a quasilocal Lieb-Robinson composition with a declared weight and velocity;
3. an exact vanishing commutator outside a sharp cone;
4. a continuum scaling theorem turning an LR envelope into the exact causal or
   chronological relation consumed by HKM/Malament rigidity;
5. a record-formation event map or record-derived event order.

The existing `FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`
is a separate candidate for item 2. It is not part of this theorem and must be
reviewed at its own scope before any downstream consumer treats it as an
accepted causal input.

The interacting/gauged log-transfer problem remains separate. This note is
free `U = 1`, fixed `m > 0`, and one-particle at the contour step.

## What this note does not claim

- It does not identify the one-particle interval with the full Fock spectrum.
- It does not drop the `1/a_tau` Hamiltonian scale.
- It does not assert a simultaneous complex polystrip of width `arcsinh(m)`.
- It does not assert a general-dimension gapless power-law exponent.
- It does not identify sampled group velocity with a Lieb-Robinson velocity.
- It does not claim a strict or sharp light cone.
- It does not apply an audit verdict.

## Runner checks

The runner checks the source boundary, the one-particle/Fock spectrum split,
the `E_d/a_tau` scaling, the exact right-half-plane strip inequality, and a
direct real-contour versus shifted-contour Fourier identity on a deterministic
`d = 3` grid.

```bash
PYTHONPATH=scripts python3 scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py
```
