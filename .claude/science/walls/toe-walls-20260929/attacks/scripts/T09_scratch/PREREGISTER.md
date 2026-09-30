# T09 pre-registration (written before any T09 script was run)

Attacker: Claude Sonnet 5.5 (same family as the supervisor).

## Question (cheapest decisive test, lane suggestion L04-W3 "smallest local state space")
The lane's ticks result is for ONE COMPONENT per site (June site-licence dichotomy).
A qubit has TWO components (C^2) and the Cl(3,0) presentation makes them a spin-1/2 carrier
for the 24 proper cubic rotations. So "one-qubit ticks" with amplitude mixing are untested.

Class tested (all premises stated):
 Z^3, translation by one site, radius-1 cross support {0, +-e_i}, ONE simultaneous unitary
 tick U(k) = A_0 + sum_i (A_i^+ e^{ik_i} + A_i^- e^{-ik_i}) on C^s per site, exactly covariant
 under all 24 proper cubic rotations for some representation rho of the binary octahedral
 group 2O on C^s (all 8 irreps of 2O; direct sums up to dimension 6 integer / 8 spinorial).

## Test 1 (tick census)
 Claim tested: a NONTRIVIAL covariant unitary tick (some A_{+-e_i} != 0) exists on s = 2.
 Also: which is the smallest s with a nontrivial tick, and does it have a curved isotropic cone?
 - PASS reading (route "one-qubit tick gives a cone" survives): a nontrivial unitary solution
   at s = 2 for some rep, with non-flat bands and an isotropic linear or curved band at small k.
 - FAIL reading (wall extends to amplitude-mixing on one qubit): every s = 2 rep gives only
   A_{+-e_i} = 0 (least-squares residual bounded away from 0 over >= 100 random starts with the
   neighbour norm pinned), and the spin-1/2 x taste family is killed by the exact cross-term lemma.
 - Then report s_min over the census and whether the s_min solution has an isotropic cone,
   a mass gap, and flat bands.

## Test 2 (Hermitian generator, same carrier)
 Same covariance, but Hermitian nearest-neighbour generator H(k) instead of a unit-time tick.
 - PASS reading (the carrier is not the obstruction; the tick is): a nonzero covariant Hermitian
   H on s = 2 (spin-1/2) exists; report its free parameters and its spectrum.
 - FAIL reading: none exists.

## Test 3 (nonnegative versus unitary inside one covariant coin algebra)
 Six-direction coin algebra C = e_A P_A + e_E P_E + e_T P_T (commutant of the 24 rotations on
 the six cardinal directions), U(k) = D(k) C.
 - Nonnegative row-stochastic members: entries m_same, m_back, m_side >= 0, sum = 1.
 - Unitary members: |e_A| = |e_E| = |e_T| = 1.
 Claim: they intersect only in permutation coins (rigid transport, no dispersion); every other
 stochastic member has spectral radius < 1 at every k != 0 (damped), with a strict finite front.
 - PASS (wall as stated by the lane): overlap only at permutation coins; damping D > 0 elsewhere.
 - FAIL (wall misstated): a non-permutation stochastic covariant coin with an undamped
   dispersive branch on an open set of k.
 Also check the 1D telegraph (Kac) template: real reversal weight -> damped with strict front;
 reversal weight continued to i*eps -> unitary massive Dirac walk (Gaveau-Jacobson-Kac-Schulman).

## What would move the wall
 - A tick route passes only if Test 1 PASS at s = 2 (the one-qubit carrier of Qubit axiom).
 - Otherwise the price becomes "carrier dimension s_min > 2, or a Hamiltonian instead of a tick",
   and the wall is PRICED, not passed. The cone (finite front) itself is not the wall: any
   local update, stochastic included, has one (Test 3 front check).
