# T26 pre-registration (written BEFORE running test_T26.py)

Wall T26 = L06-W1 (gauge group not selected from the carrier: su(3)+su(2)+u(1) vs u(6)) +
L06-W2 (colour carrier MR_color not derived).

Lane's own "cheapest test" (L06-W1): compute the full symmetry algebra of the actual
nearest-neighbour hopping on the 8-state taste cube and see if the factorwise algebra is
forced with no supplied factor rule.

Route 1 under test ("the lattice's own hopping and covariance select the gauge algebra"):
  R1a (strict, constant-hopping gauge invariance): the gauge algebra g must commute with the
      fibre matrices of the actual cube-edge hopping S_i (= X_i on the corner cube), or with the
      Cl(3) version Gamma_i.  Then g <= Commutant{h_i}.
  R1b (twisted / lattice-covariance): the gauge algebra must be *normalised* (set-invariant) by the
      internal action of the lattice symmetries: translation X_i, and cube axis permutations.

Objects (taken from scripts/frontier_graph_first_su3_integration.py, same definitions):
  g8 = graph-first algebra (selected axis 1): weak su(2) = {X1,Y1,Z1}/2, su(3) = Gell-Mann on the
  swap-symmetric block of the other two axes (x) fibre, u(1)_Y = 1/3 on Sym, -1 on Anti.  dim 12.

PASS readings (route survives = hopping/covariance selects or at least admits g8):
  P1: g8 (or its su(3) part) commutes with the cube-edge hopping S_i (or a tau-symmetrised version).
  P2: the covariance-closure of g8 under {X_i, axis perms} is a proper subalgebra of u(8) that is
      still factorwise (dim <= ~12-16, i.e. g8 is already covariant).
FAIL readings (route dies):
  F1: su(3) part does not commute with S_2 + S_3 (the tau-symmetric base hopping)  -> fails P1.
  F2: commutant of {S_i} is abelian (dim 8) and commutant of {Gamma_i} is u(2)+u(2): it contains no
      su(3) at all.
  F3: closure of su(3) part under translations X_i has dim > 12 (translation moves the colour algebra
      to a different su(3)); closure of g8 = u(8) (dim 64) or su(8) (63).
Also record the control: the weak-factor closure under B_3 (su(2)_1 -> su(2)^3, dim 9) which SHOULD be
covariant-friendly, so the failure is specific to the colour block and not an artefact of the method.

Second check (lemma, irreducibility): on the irreducible carrier C^6 = (3,2), the commutant of
g6 = su(3)+su(2)+u(1) is scalars; so constant hopping fibre matrices commuting with g6 are scalars, and
scalars commute with all of u(6): dynamics of this class cannot separate g6 from u(6).
Numerical readings: commutant dim of g6 in M_6 = 1 (pass of lemma), commutant of u(6) = 1.
Maximality (Dynkin): no algebra strictly between g6 and u(6): checked as: for random cross-factor
generator added, closure = u(6) (dim 36); i.e. dim jumps 12 -> 36.

## Addendum written after the first run of test_T26.py, before running test_T26b.py
First run showed: (i) the "centre" printed in test A was the bicommutant dimension, not a centre;
recomputed properly in test_T26b.py. (ii) closure of g8 under translations = 18, not 63.
Pre-registered readings for test_T26b.py:
  B1: closure(g8, translations) equals exactly su(4)_base (x) I_2 + I_4 (x) su(2)_weak (dim 15+3 = 18).
      PASS-for-route-1 would be: closure = g8 (dim 12). FAIL: dim > 12.
  B2: the subset of translations t in Z_2^3 that normalise g8: expect exactly {X1^a (X2X3)^b}: 4 of 8.
      (a translation along axis 2 or 3 alone does not.)
  C : on a bond (two qubits) su(3)_Sym intersected with span of single-site operators {A(x)1 + 1(x)B}
      has dim 3 (so(3) only); so 5 of the 8 su(3) generators are irreducibly two-site.
      PASS-for-site-local-colour would be: dim 8.  FAIL: dim <8.
  D : isotropy (commutant) of the derived selector's vacuum H(phi=(1,0,0)) = X1 (x) 1_4 in u(8) has dim 32 (u(4)+u(4)),
      not 12/18: the factorwise group is not the isotropy of the derived selector's vacuum.
      Also intersect: dim(g8 ∩ isotropy).

## Addendum 2 (before running test_T26c.py): robustness to the reading of "lattice translation"
The internal action of a lattice translation on the taste cube is a READING. Two natural ones:
  (X) corner-flip X_i (taste cube = 2x2x2 block of sites), (Z) doubler phase Z_i (taste cube = corners of the
  Brillouin zone; translation acts as (-1)^{n_i}).  Also the Pauli group <X_i,Z_i> (both are symmetries of
  the free staggered action).
Pre-registered: closure(g8, Z_i) > 12 and closure(g8, <X_i,Z_i>) > 12, i.e. the enlargement is not an
artefact of choosing X.  FAIL of the claim would be closure = 12 under Z_i.
