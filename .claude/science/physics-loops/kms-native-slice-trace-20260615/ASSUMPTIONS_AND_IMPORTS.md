# Assumptions And Imports

## Framework Inputs

- `A_min` only through the RP note's hypothesis set.
- RP two-step transfer matrix `T := T_hat^2 : H_phys -> H_phys` on finite
  `H_phys`.
- Spectrum-condition support for `H = -(1/(2 a_tau)) log(T / M_T)`, with
  `H >= 0`.
- Even raw Euclidean time length `L_tau`, blocked count `N_tau := L_tau/2`,
  and `beta_th = N_tau * (2 a_tau) = L_tau * a_tau`.
- Finite-dimensional cyclic trace, used as elementary linear algebra.

## Retired Imports

- K1 no longer invokes Bratteli-Robinson Lemma 5.3.4 for insertion
  bookkeeping. The note now proves
  `tr(T^(N_tau-j) O T^j) = tr(T^N_tau O)` by cyclicity on the two-step
  blocked carrier.
- K4 no longer invokes Bratteli-Robinson Theorem 5.3.30 as the proof. The
  note now proves uniqueness using matrix units, including degenerate energy
  blocks.
- The stale one-step normalization `T = exp(-a_tau H)` is retired; the runner
  now constructs `T = exp(-2 a_tau H)`.

## Remaining Boundary

- The result still depends on independent audit of the upstream RP and
  spectrum-condition notes.
- Wick rotation remains the explicit convention already paid for by the RP
  reconstruction; this PR does not attempt a continuum Tomita-Takesaki theorem.
