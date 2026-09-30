# T25 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family check).
Wall: T25 = matter content (SM table, taste cube, dark host) and species labels are supplied.
Members: L05-W10, L08-W3, L09-W1, L10-W8, L12-W1.

Operators are copied from the repo's own runners (read only):
 scripts/audit_companion_cl3_taste_abstract_c8_orbit_scope_2026_06_12.py  (S3 perms, Y, T3)
 scripts/verify_cl3_sm_embedding.py  (fibre SU(2)_weak, Gell-Mann SU(3) on symmetric base)

## Test A (decisive for the T25-specific claim): can ONE 8-state taste cube host both the SM gauge content and the generation triplet?
Question: the lane reads C^8 = (C^2)^3 as (i) one generation's left-handed gauge content Q_L(3,2)_{1/3} + L_L(1,2)_{-1}
(6+2) and (ii) via its Hamming-weight-1 triplet as the three generations (C3/S3 orbit). Both on the same 8 states.
Computed: Q = T3 + Y/2 on hw=1; commutators of C3, transpositions and the Hamming-weight grading with Y, T3, SU(3);
the subgroup of S3 that stabilises the gauge algebra; the dimension of {Hermitian hw=1 operators that commute with Q and C3};
zero-mode census of the supplied walker on the 4^3 torus versus the SM Weyl count.
PASS (double use is consistent; route "reuse the cube" survives) iff ANY of:
  (a) C3 commutes with Y, T3, and all SU(3) generators (norm < 1e-10), or
  (b) Q is a scalar on hw=1 (the three hw=1 states carry identical charges), or
  (c) the space {H = H^dag on hw=1 : [H,Q]=0, [H,C3]=0} has dimension >= 3 (split masses allowed).
FAIL (cube cannot host both) iff Q has >= 2 distinct eigenvalues on hw=1 AND the S3-stabiliser of the gauge algebra does not
contain C3 AND that space has dimension 1 (scalars only).
Prediction: FAIL. Q on hw=1 = {2/3, 0, -1/3}; stabiliser = {e, T12}; space dim = 1.

## Test B (does the species/taste structure come from the rule class or is it an independent supply?)
Enumerate all translation-invariant nearest-neighbour Hermitian 2-band rules on Z^3 covariant under the 24 proper cubic rotations,
for coin representations of the rotation group: spinor (rotor lift, G1), spinor x sign (G2), E (2-dim S3 irrep), trivial (1+1), 1+A2.
Compute the dimension of the covariant class and, for a random member, the band-touching set on the BZ.
PASS ("taste cube is forced by locality+covariance, given a spinor coin") iff: spinor class has dimension exactly 3
(c0, c1 sum cos, A sigma.sin) and every member with A != 0 has exactly the 8 touching points {0,pi}^3, and at least one
non-spinor class has a different census (so the census depends on the coin representation).
FAIL iff the spinor class has more parameters or a touching set other than the 8 corners.
Prediction: PASS. Meaning if PASS: the taste cube is not an independent supply; it is priced at the coin's rotor action (T20) + the existence of a rule (T02).

## Test C (labels): what is left of the labelling wall?
C1: the 24 proper rotations act on the three hw=1 corners as the full S3 (order 6), not only C3.
C2: for a circulant mass operator with complex b, a transposition maps b -> b*; spectrum unchanged; the assignment of the
    mass order to the Z3 characters flips (orientation is a rotation, not an observable, within one sector).
C3: two circulant sectors (e.g. lepton-like, quark-like) with arbitrary (a, |b|, delta) have a mixing matrix V = U_u^dag U_d
    that is a permutation matrix (|V_ij|^2 in {0,1}); non-monomial mixing needs sector-relative C3 breaking.
PASS ("labels reduce to registered data plus cross-sector alignment") iff C1 gives order 6, C2 spectrum invariant, C3 monomial.
FAIL otherwise.
