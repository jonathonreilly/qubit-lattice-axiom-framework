# Native I_S Scalar-Kernel Fork Resolution (Bounded)

**Date:** 2026-06-16
**Claim type:** bounded_theorem
**Claim boundary:** settles only the local scalar-bilinear propagator-kernel
fork: after scalar projection, the one-loop kernel carries one remaining
fermion denominator, `D_psi^-1 D_g^-1`, not the literal untraced
`D_psi^-2 D_g^-1` form. It does **not** settle the taste-normalization
convention, the final numeric `I_S`, any P1 or Delta_R value, or any top-mass
surface.
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. No audit verdict asserted here.
**Primary runner:**
[`scripts/yt_p1_i_s_native_kernel_settled_2026_06_16.py`](../scripts/yt_p1_i_s_native_kernel_settled_2026_06_16.py)
**Cached log:**
[`logs/runner-cache/yt_p1_i_s_native_kernel_settled_2026_06_16.txt`](../logs/runner-cache/yt_p1_i_s_native_kernel_settled_2026_06_16.txt)

## The Fork

The composite-`H_unit` scalar-bilinear vertex was ambiguous between two
kernel shapes:

- `N_S(k) / (D_psi(k)^2 D_g(k))`, the literal untraced two-fermion-propagator
  denominator;
- `N_S(k) / (D_psi(k) D_g(k))`, the scalar-projected denominator after one
  power of `D_psi` is cancelled by the Dirac trace.

This note settles that fork only.

## Kernel Derivation

For `H_unit = (1/sqrt(N_c N_iso)) sum psi_bar psi`, the scalar insertion is the
identity. The one-gluon vertex diagram has two untraced fermion propagators and
one gluon propagator, but the scalar projection reduces one fermion denominator:

```text
S(k) = -i slash{s} / D_psi(k)
slash{s} slash{s} = D_psi(k) 1

Tr[ S(k) 1 S(k) ] = -Tr[slash{s} slash{s}] / D_psi(k)^2
                  = -4 / D_psi(k).
```

Thus, once `N_S(k)` is the trace-reduced scalar numerator, the finite-part
kernel is `N_S(k) / (D_psi(k) D_g(k))`. Keeping `N_S(k)` while also keeping
`D_psi^-2` double-counts the pre-trace denominator.

The continuum limit gives the same result. With
`D_psi -> k^2`, `D_g -> k^2`, and `N_S -> 4`, the settled kernel has leading
power `4/(k^2+m^2)^2`. The literal `D_psi^-2 D_g^-1` form instead has the
wrong `~4/k^6` small-`k` power against that subtraction.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  repo baseline Lattice + Quantum + Record language. The axiom baseline is an
  approved premise and is not a source of bounded status.
- [`YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md`](YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md)
  supplies the bounded composite-`H_unit` scalar-bilinear setup and the
  one-loop lattice-PT Feynman-rule context.

## What This Does Not Claim

- It does not choose whether a full-BZ staggered integral should carry an
  additional taste normalization.
- It does not assert `I_S = 3.90`, `I_S ~ 32`, or any final scalar matching
  coefficient.
- It does not import or retire the literature bracket `[4,10]`.
- It does not repair Delta_R, P1, Higgs, top, bottom-Yukawa, or publication
  surfaces.
- It does not derive the scalar-bilinear matching bridge from the framework
  axioms; this is a bounded one-loop lattice-PT kernel statement.

## Runner Certificate

The runner verifies:

1. the untraced diagram bookkeeping has one scalar insertion, two quark-gluon
   vertices, two fermion propagators, and one gluon propagator;
2. a concrete Euclidean Clifford representation satisfies the gamma algebra;
3. the scalar projection supplies one numerator factor of `D_psi`;
4. the settled kernel has the correct small-`k` continuum power;
5. the literal `D_psi^-2 D_g^-1` form is rejected by the same continuum
   subtraction;
6. the settled kernel's finite-part quadrature is stable under a fixed
   illustrative normalization, without selecting the final `I_S` value.

Run:

```text
python3 scripts/yt_p1_i_s_native_kernel_settled_2026_06_16.py
```

Expected result:

```text
TOTAL: PASS=9 FAIL=0
```
