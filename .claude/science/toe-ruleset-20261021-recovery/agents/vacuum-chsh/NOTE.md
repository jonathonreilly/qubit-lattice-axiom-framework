# Vacuum CHSH vs separation on the half-filled staggered sea (finite diagnostic)

2026-10-27. Probe for the TOE-ruleset campaign. Supplied model, finite scan, unaudited.
Files: criteria.md (pre-registered), probe.py, probe_modes.py, out.txt, LOG.md.

## Setup (all supplied, none derived)
- Kogut-Susskind staggered hopping on an antiperiodic 96^3 torus, half filling, staggered mass
  m in {0, 0.1, 0.3, 1}. The vacuum is the Slater state that fills the negative band. Main's
  minimal axioms supply no Hamiltonian or vacuum (MATTER_ABOVE_THE_HALF_FILLED_SEA...2026-09-03;
  HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR...2026-09-02). The "half-filled sea"
  vacuum ruling is panel memory only and is not on main.
- Exact correlations: h^2 = sum sin^2 k + m^2, so P_- = (1 - h |h|^-1)/2 with |h|^-1 obtained by
  FFT. This matches dense diagonalisation on 8^3 to 8e-16. Block states are Gaussian, built from
  C_AB. They reproduce C to 3e-16.
- Blocks: s1 (one site), s2 (two sites), s4 (a 2x2 plaquette), with full Fock CHSH up to 8 modes.
  Larger regions (cube, 3x3, 4x4) get Gaussian negativity and mode-optimised CHSH lower bounds.
  Separation B = A + r n, with n = axis (r <= 16) or body diagonal (r <= 10).
- CHSH_SSR uses observables even in each block's modes. CHSH_noSSR uses JW qubits (A then B)
  with all operators allowed. The noSSR value is labelled; it is not a statement about the register.
- E_N is the fermionic log negativity (Shapourian-Shiozaki-Ryu). The direct Fock value equals the
  Gaussian formula to 1e-15. E_SSR is E_N of the local-parity-projected state.
- Optimiser check: the dual-rail one-particle test state gives 2.828427125 under both SSR and noSSR.

## Results (raw lattice numbers)
| Vacuum | Largest r with CHSH > 2 | E_N vs r | E_SSR |
|---|---|---|---|
| m = 0 (Dirac points) | none, at any r >= 1, for any shape/direction/SSR choice | > 0 wherever C_AB != 0; falls about r^-6 with an odd/even oscillation | > 0 only at r = 1 (s2 0.041, s4 0.39); 0 to 1e-14 from r = 2 |
| m = 0.1, 0.3 | none | exponential decay, e.g. p4x4 axis r = 17 about 1e-7 (m = 0.1) | as m = 0 |
| m = 1 | none | exponential decay; reaches the double floor (< 1e-13) at r about 14 (axis) and 8 (diagonal); unresolved beyond that, not a measured zero | as m = 0 |
| D4 free sea | NOT DONE | — | — |

- Exact zeros come from the staggered selection rule: C(x,y) != 0 only if y - x has exactly one odd
  component (hop), or all components even (mass term, absent at m = 0). So at m = 0, s1 is a product
  state at even axis r and at every diagonal r.
- Under SSR, s1 gives exactly 2: the even algebra of one mode is commutative.
- noSSR s1 (exact Horodecki): the raw value is at most 1.09 even when adjacent.
- Mode-optimised noSSR 1+1 (closed form; lower bound for the region): there is no violation in any
  region up to 4x4 plaquettes (16 modes per side). The best raw value is 1.82 (m = 0) to 1.90 (m = 1),
  for adjacent 4x4 plaquettes. As r grows the value settles at a local plateau. The plateau comes from
  the purest mode pair and rises with block size and mass (s4 0.63 to p4x4 1.41 at m = 0), but stays
  below 2.
- The SSR 2+2 isometry search on the cube and 3x3 gives a flat objective and stops at once. It is
  uninformative, and it is not counted as a negative.

## Verdict (reading, hedged)
1. Pre-registered rule: on this scan, r*_CHSH does not exist. No vacuum, block or optimiser found a
   violation, even for adjacent blocks. "Violation dies at finite r" holds only vacuously. The
   finite-r cutoff is not resolved, because the small lattice blocks are already Bell-local at contact.
2. Entanglement does persist beyond every scanned r in the fermionic E_N sense. Analytically,
   E_N > 0 whenever C_AB != 0. This is shown analytically for one mode per side; for larger blocks
   it is numerical, with E_N ~ |C_AB|^2. This measure counts single-particle
   A-B coherence, which SSR-respecting local observables cannot access. The SSR-accessible E_SSR
   already vanishes at r = 2.
3. Compared with PSI OQP12 (Turturean, letter of 22 Oct 2026, Thm 1 / Cor 1): the lattice numbers
   agree in sign. Bell-local at large separation, entangled at every separation. The lattice says
   nothing about their constant C*, because our blocks never violate. Their violating regime
   (beta = sqrt2 for tangent regions, after Summers-Werner) needs the infinite-mode local algebras
   of the continuum. Fixed few-site lattice blocks do not reach it.
   The plateau trend is the lattice image of their "nearly pure modes" obstruction. Larger blocks
   contain purer modes and push the plateau toward 2. A violation at small r therefore needs larger
   blocks (more modes) than this budget allows.
4. Massless contrast: there is no qualitative difference from the massive case in the CHSH data.
   The difference is only the power-law vs exponential decay of E_N. This is consistent with PSI's
   C* being independent of m. It does not test their m > 0 hypothesis.

## Relation to repo notes
- Uses CHSH_TSIRELSON_LATTICE_QUBITS_BOUND_NOTE_2026-05-20: the qubit-pair bound 2 sqrt2 is the
  ceiling, and here it is never approached.
- NATIVE_PARITY_ENTANGLER_AND_CHSH_NOTE_2026-09-08 reaches 2 sqrt2 only with a heralded, regrouped
  dual-rail resource. This agrees with our self-test: SSR violation needs >= 2 modes per side and
  nearly pure one-particle sharing. The sea does not supply that.
- DYNAMICS_CLAUSE_BELL_VALUES_..._2026-09-24 gets 2 sqrt2 from an isolated Heisenberg singlet. The
  free sea's small blocks are far more mixed. Nothing is contradicted.
- D4: the CL file's nearest-neighbour W(F4) fermion fails root reflection positivity (a Lee-Wick
  pair at w = 1). The zoom fixed point has pole positivity only beyond 4 slices. No spatial-slice
  Hamiltonian ground state is defined, so there is no D4 sea to test.

## Open questions
- Smallest block (modes per side) that violates CHSH_SSR when adjacent, and then its r*. This needs
  a smooth surrogate objective (for example SSR-sector Horodecki) rather than a flat see-saw value.
- Whether the 1+1 plateau reaches 2 as block size goes to infinity at fixed r. That would be the
  lattice route toward PSI's regime.
- A D4 sea, once a positive transfer matrix exists.
