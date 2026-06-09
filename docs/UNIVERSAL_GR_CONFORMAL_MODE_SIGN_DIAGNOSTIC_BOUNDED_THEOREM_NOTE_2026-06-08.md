# Finite W-Native Conformal-Mode Sign Diagnostic

**Date:** 2026-06-08
**Claim type:** bounded_theorem / finite-Brillouin-zone sign diagnostic
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_conformal_mode_sign_diagnostic.py`](../scripts/frontier_universal_gr_conformal_mode_sign_diagnostic.py)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_conformal_mode_sign_diagnostic.txt`](../logs/runner-cache/frontier_universal_gr_conformal_mode_sign_diagnostic.txt)

## Summary

This repair keeps the finite computation and narrows the claim to the result it
actually supports. The runner forms the finite 4D Brillouin-zone stress-bubble
kinetic matrix

```text
M_(mu nu),(rho sigma) = [Pi_mu nu,rho sigma(k) - Pi_mu nu,rho sigma(0)] / k^2
```

for the staggered Kahler-Dirac stress vertex over all ten symmetric metric
components. At tested sizes `N=4,6`, the full `10x10` matrix contains one
negative eigenvalue with finite overlap against the trace/conformal direction
and negligible overlap against the tested `yz` transverse-traceless direction.

The result is a useful finite diagnostic: the naive pure-trace quadratic form
is positive because that one-vector probe is not the same as diagonalizing the
full coupled metric-sector matrix. The diagonalized finite matrix instead has a
single opposite-signed, trace-character direction in the tested setup.

This note does **not** prove that the direction is the continuum GR
Hamiltonian constraint, does **not** prove the exact two-DOF graviton count,
does **not** exclude scalar-tensor completions, and does **not** determine how
the induced cosmological constant couples to continuum modes.

## Theorem (Bounded Finite-BZ Diagnostic)

For the runner-defined finite matrix at mass `m=0.7` and momentum along one
spatial axis:

- **T1:** the normalized pure-trace probe is positive,
  `<trace|M|trace> = +0.0295`. This shows that a single pure-trace probe alone
  is not a decisive conformal-mode sign test for the coupled `10x10` matrix.
- **T2:** the full metric-weighted `10x10` diagonalization at `N=6` has exactly
  one eigenvalue below `-1e-4`: `-0.0099`. Its eigenvector has trace/conformal
  overlap `0.49` and tested `yz` transverse-traceless overlap `0.000`.
- **T3:** the lowest eigenvalue magnitude shrinks between the tested sizes
  (`N=4: -0.0496` to `N=6: -0.0099`), while the runner-defined transverse
  projected `6x6` block has no eigenvalue below `-5e-3`.

`TOTAL: PASS=3 FAIL=0`.

## What This Establishes

The row establishes a bounded finite-matrix sign/character diagnostic:

- the naive pure-trace quadratic form is positive in the tested finite setup;
- the full `10x10` matrix has one opposite-signed eigen-direction;
- that direction has nontrivial trace/conformal character and negligible
  overlap against the tested `yz` TT basis vector; and
- the lowest eigenvalue moves toward zero from `N=4` to `N=6` in the tested
  refinement.

This is compatible with a GR-like conformal-factor sign pattern, and it is a
useful diagnostic for later Ward-identity and continuum-constraint work. It is
not itself that later work.

## What Remains Open

- Full stress-vertex and contact-term validation for the physical metric
  Hessian.
- A continuum limit controlling the gauge/constraint sector rather than only
  comparing `N=4` and `N=6`.
- The Hamiltonian-constraint or diffeomorphism Ward identity that would turn
  this sign/character diagnostic into a continuum constraint theorem.
- Exact two-DOF graviton counting.
- Any scalar-tensor exclusion or fifth-force statement.
- Any conclusion about the induced cosmological constant's physical coupling
  to continuum modes or its magnitude.

## Relation to Inventory

This row is downstream context for the finite-`k` W/stress route in
[`UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md`](./UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md).
It is also compatible with the sign vocabulary used in
[`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](./UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md)
and the algebraic normal-form context in
[`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md`](./UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md).

The row does not settle those neighboring rows, does not close the universal-GR
program, and does not change the status of the induced-cosmological-constant
surface.

## Honest Auditor Read

The source is a finite diagnostic. The runner checks one memory-safe 4D
Brillouin-zone construction (`N<=6`, `16x16` staggered blocks, `10x10`
metric-sector matrix). The strongest valid reading is that the coupled finite
matrix contains an opposite-signed trace-character direction missed by the
naive pure-trace probe. The result should be audited as finite support for a
candidate conformal-sector sign pattern, not as a proof of GR closure, a proof
against scalar-tensor physics, or a cosmological-constant theorem.
