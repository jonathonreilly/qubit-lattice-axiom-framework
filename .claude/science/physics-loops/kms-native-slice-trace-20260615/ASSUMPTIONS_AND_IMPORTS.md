# Assumptions And Imports

## Framework Inputs

- `A_min` only through the RP note's hypothesis set.
- RP transfer matrix `T : H_phys -> H_phys` on finite `H_phys`.
- Spectrum-condition support for `H = -(1/a_tau) log(T / M_T)`, with `H >= 0`.
- Finite-dimensional cyclic trace, used as elementary linear algebra.

## Retired Imports

- K1 no longer invokes Bratteli-Robinson Lemma 5.3.4 for insertion
  bookkeeping. The note now proves
  `tr(T^(L_tau-j) O T^j) = tr(T^L_tau O)` by cyclicity.
- K4 no longer invokes Bratteli-Robinson Theorem 5.3.30 as the proof. The
  note now proves uniqueness using matrix units, including degenerate energy
  blocks.

## Remaining Boundary

- The result still depends on independent audit of the upstream RP and
  spectrum-condition notes.
- Wick rotation remains the explicit convention already paid for by the RP
  reconstruction; this PR does not attempt a continuum Tomita-Takesaki theorem.
