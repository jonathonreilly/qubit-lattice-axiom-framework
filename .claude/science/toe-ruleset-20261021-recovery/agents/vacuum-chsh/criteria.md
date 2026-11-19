# Pre-registered criteria: vacuum CHSH vs separation on the lattice sea

Written 2026-10-27 BEFORE any script. Changes after the first run go in LOG.md, never here.

## Supplied model (not derived)
- Kogut-Susskind staggered hopping on Z^3, half filling, single-particle
  h = sum_mu (i/2) eta_mu(x) (T_mu - T_mu^dag) + m eps(x), eps = (-1)^{x1+x2+x3}.
  Vacuum = Slater state filling every negative eigenvalue of h (supplied choice; main's
  minimal axioms do not supply a Hamiltonian or vacuum). Torus L^3, antiperiodic in all
  three directions (no exact zero modes at m = 0), L = 48 and 64 to check convergence.
- Masses m in {0, 0.1, 0.3, 1.0}.
- D4 free sea: used only if the repo/CL file gives a Hamiltonian (positive transfer
  matrix) with a spatial-slice ground state. Otherwise recorded as NOT DONE with reason.

## Observables
- Blocks A, B of fixed shape: (s1) one site; (s2) two sites transverse to the separation;
  (s4) 2x2 plaquette transverse to the separation. CHSH only when total modes <= 8.
  Negativity also for larger blocks (2x2x2 cube) via the Gaussian formula.
- Separation: B = A + r*n, n = (1,0,0) (axis) and n = (1,1,1) (body diagonal).
- CHSH_SSR: max over dichotomic observables EVEN in each block's modes (block-local
  fermion parity superselection). CHSH_noSSR: modes of A then B read as qubits in that
  Jordan-Wigner order, all local operators allowed (labelled; not a register statement).
  1-mode blocks: exact (CHSH_SSR = 2 identically; CHSH_noSSR by the Horodecki formula).
  Larger: see-saw, >= 12 random restarts; report best and spread (best - median).
- E_N: fermionic log negativity (Shapourian-Shiozaki-Ryu partial time reversal).
  E_SSR: same quantity on the local-parity-projected state rho_SSR.

## Decision rules (tolerances fixed now)
- "Violation at r": best CHSH - 2 > 1e-6 (see-saw is a lower bound; a positive excess is
  a witnessed violation). "No violation found at r": best < 2 + 1e-9 over all restarts,
  with see-saw spread recorded. For s1 noSSR the Horodecki value is exact.
- r*_CHSH = largest r (scan r = 1..16 axis, 1..10 diagonal) with a violation.
  "Bell violation dies at finite r" = r*_CHSH exists and no violation at every larger
  scanned r. This is a finite-scan statement only, not a theorem for all r.
- "Entanglement persists beyond r*": E_N > 1e-10 at some r > r*_CHSH. E_N < 1e-12 counts
  as zero (PPT); between 1e-12 and 1e-10 = unresolved.
- Checks required before any reading: Gaussian rho reproduces the input correlation matrix
  to 1e-12; FFT correlation matches dense diagonalisation on L = 8 to 1e-12; Gaussian
  negativity formula matches the direct Fock partial transpose to 1e-10; see-saw s1 noSSR
  matches Horodecki to 1e-8; L = 48 vs 64 values agree to 1e-6 where reported.

## Readings allowed
Raw numbers are finite diagnostics of a supplied model. Comparison with PSI OQP12 (a
continuum theorem about type-III local algebras) is qualitative only: same sign of the
effect or not. No physical vacuum is claimed.
