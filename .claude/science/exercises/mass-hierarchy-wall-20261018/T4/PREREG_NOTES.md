# T-F3 clarifications (written before any T4 run, 2026-10-18)

The readings in `masswall/TESTS.md` (T-F3 entry) are fixed and are not changed here. These notes only
make the computation definite where the entry leaves a choice open.

## Model (as the derivation uses it)
- Generations: the X-star triplet (F2 star placement). Lattice image on the triplet is B3 (signed
  permutations): T(e_j) -> diag sign at j, rotations -> axis permutations (FP/scripts/s1_group.py).
  The internal-T1 placement has the same image up to +-1 and is covered by the same group theory.
- Mass matrices: Dirac charged-lepton M_l (psi_R^dag M psi_L) and Majorana M_nu (psi_L^T M psi_L).
  Both transform as M -> g M g^T.
- Charged-lepton residual: g_l = image of C3[111] through a site. Neutrino residual: g_nu = image of
  C2[110] o T(e3) (half-turn through the bond midpoint (0,0,1/2)). Both are computed from geometry.
- Orders: real G-irreps that couple linearly to the bilinears (A1, E, 3_M, 3_M'). Complex couplings
  enter through two real copies (Re, Im) of each irrep component. phi_l is the C3-fixed part,
  phi_nu the g_nu-fixed part.

## Unperturbed state (fitted to data, as the derivation's F3)
- M_l^(0) = F diag(m_e e^{ia0}, m_mu e^{ia1}, m_tau e^{ia2}) F^dag. F is the C3 (Fourier) basis and the
  electron is the trivial character (derivation, TM1 section). Which of mu and tau takes omega or
  omega-bar is random. The phases are random.
- M_nu^(0) = U* diag(m1, m2, m3) U^dag, with U = [v1, c w1 + e^{i phi} s w2, -e^{-i phi} s w1 + c w2] and
  random Majorana phases. Here v1 = (1,1,0)/sqrt2, w1 = (1,-1,0)/sqrt2, w2 = (0,0,1).
  - Normal ordering: dm21^2 = 7.42e-5 eV^2, dm31^2 = 2.51e-3 eV^2 (recalled, NuFIT-like).
  - m1 is log-uniform in [1e-4, 1e-2] eV (primary). Secondary runs use m1 = 1e-4 fixed, and
    inverted ordering.
  - phi is uniform, and a draw is accepted only if the unperturbed s23^2 lies in [0.435, 0.585].
  - Charged masses are PDG pole values (recalled).
- **theta13 fit.** For each draw, the leakage operators are held fixed: their coefficients and word
  choices are frozen, and they act on the current state. The block angle theta is then re-solved by a
  root-find, so that the perturbed sin^2 theta13 = 0.0220. If no root exists in the bracket, the draw
  is kept unrefit and flagged. The vacuum-misalignment class is not refit. Since
  Delta = ||U_e1|^2 - 2/3| / c13^2, the refit only affects Delta at second order.

## "Natural size"
- Every leakage operator gets coefficient c = r e^{i chi}, with chi uniform and r log-uniform in [1/3, 3].
- It acts on unit-norm sector states (both orders are lattice-scale O(1) record patterns). It is scaled
  by the receiving sector's ||M^(0)||_F, the same scale as that sector's own leading operator.
- Loop-natural: c/(16 pi^2). This is the pre-registered "O(1) times the loop factor".
- Tree-natural: c. This is reported too, because G permits these operators at tree level.

## Operator classes (each at least 500 draws; 1000 planned)
- **L1.** Linear mixed insertions: phi_nu components (E, 3_M, A1) into M_l, and phi_l components
  (3_M, A1) into M_nu. 3_M' cannot enter a Majorana mass.
- **L2.** Second-order insertions that survive any abelian shaping symmetry: phi_l (phi_nu phi_nu) into
  M_l, and phi_nu (phi_l phi_l) into M_nu. These are built as G-covariant words: matrix products,
  triple Hadamard products and irrep projections of the real component matrices.
- **W.** Fermion-loop wavefunction leakage through the shared doublet:
  - dM_nu = P^T M_nu + M_nu P, where P is a generic C3-invariant Hermitian;
  - dM_l = M_l Q, where Q is a generic g_nu-invariant Hermitian.
- **ALL-loop.** L1 + L2 + W, all at loop-natural size. This is the primary measure.
- **TREE.** L1 + L2 at tree-natural size.
- **PHYS.** W with the SM-like data-fixed size: P = -(3/2) ln(M_Pl/M_Z)/(16 pi^2) Y_e^dag Y_e.
- **V.** Vacuum misalignment. A generic G-invariant quartic potential is used, with quadratic and
  linear coefficients tuned (registered data) so that the F3 point is stationary within each sector.
  The draw is kept only if that point is a local minimum. Cross invariants are added at lambda_x
  times O(1), at three shaping levels:
  - none;
  - Z2 x Z2 (even in each sector);
  - U(1) x U(1) (equal to Z_N, N >= 3, at degree <= 4).

  The mass matrices are recomputed at the shifted minimum.

## Applying the fixed readings (procedure pinned now)
1. **SAFE** if a framework-permitted symmetry forbids every leading leakage operator, or if the
   ALL-loop median Delta < 0.003.
2. **KILL** if the ALL-loop median Delta > 0.01, no framework symmetry forbids the operators, and
   neither of the following brings the median below 0.003:
   - one named extra structure, with its leftover operators kept at loop-natural size;
   - a tuning no stronger than eps = 1e-2 of natural size.
3. **PRICE** if the median is brought below 0.003 by one named extra structure, or by a tuning
   eps >= 1e-2.

   I read "a tuning of eps <= 1e-2" in the entry as the size limit of the tuning that PRICE covers.
   Otherwise KILL could never fire, because any leakage can be tuned away. This is an interpretation,
   and the other reading is reported alongside.
4. **OPEN** otherwise.

For every class I report t_req: the overall factor on natural size that gives median Delta = 0.003.
