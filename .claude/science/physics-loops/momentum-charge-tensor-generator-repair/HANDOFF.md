# Handoff

This branch repairs `momentum_charge_commute_theorem_note_2026-05-02` by
narrowing it to retained tensor-product translations and their
finite-block spectral generators.

Changes:

- Source note now cites the retained tensor-product bridge as the sole
  load-bearing authority.
- Claim scope removes full physical `P_total^mu`, arbitrary `H_phys`,
  Wigner classification, cross-section, and energy-label completeness.
- Runner checks `[T_a,Q_total]=0`, `[K_mu,Q_total]=0`, pairwise generator
  commutation, and common finite-block diagonalization.

Independent audit is still required before the row can regain retained
effective status.
