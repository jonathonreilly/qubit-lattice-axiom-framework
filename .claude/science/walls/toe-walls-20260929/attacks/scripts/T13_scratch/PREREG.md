# T13 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks).
Wall: T13 = L04-W4 (d_t <= 1, B-AXIS.3 / N5), L04-W5 (d_t odd), L04-W11 (d_s = 3).

Claim under test (route R1, "N5's second clock is not a second time"):
the operator-layer criterion "an independent commuting positive transfer on a
disjoint tensor factor is a second clock" (N5 note :16-33, :63-73) does not
measure the number of time dimensions. Two sub-claims, each with a pass and a fail
reading fixed here.

## Test 1: kinematic witness in a system whose single time is not in doubt (witness.py)
Model: open transverse-field Ising chain, L = 8, H = sum ZZ + sum X (one time by
construction: one Hamiltonian, connected, nearest neighbour).
A = site 0, B = site 7, H_A = I + X_0, H_B = I + X_7 (non-scalar, positive).
- PASS (route survives): [H_A,H_B] = 0 exactly; H_A, H_B linearly independent;
  U(s,t) = exp(-i s H_A - i t H_B) is an R^2 homomorphism; U(1,0) is not on the
  orbit of exp(-i tau (H_A+H_B)). i.e. the N5 witness exists in a one-time system.
  AND ||[H_A,H]|| > 0 for the connected chain, = 0 for the chain with the bonds
  touching A and B cut (decoupled).
- FAIL: any of the N5 conditions fails in the connected chain, or
  ||[H_A,H]|| = 0 in the connected chain (then the witness is special to
  multi-clock worlds and the route is dead).

## Test 2: commutant census of local translation-invariant charges (census.py)
Infinite qubit chain, translation-invariant operators built from Pauli strings of
range <= r (r = 3..6), non-identity. Count = nullity of c -> [H, sum c_s s].
Models: (a) tilted Ising, ZZ + 0.9045 X + 0.8090 Z (non-integrable, generic);
(b) critical Ising ZZ + X (free fermion); (c) XX chain XX + YY.
- PASS: (a) nullity = 1 (H only) for every r in 3..6; (b) and (c) nullity >= 2 and
  non-decreasing with r, growing.
  Reading: in a connected generic law the commutation criterion returns exactly
  one generator, but in free/integrable laws (every comparator the campaign uses)
  it returns many while d_t = 1 by construction; so "count of commuting local
  generators" cannot define d_t; it defines a genericity condition.
- FAIL: (a) nullity >= 2 at some r (a generic connected law has a second local
  charge: the genericity reading is dead) or (b),(c) nullity = 1 (free comparators
  have a single generator: then B-AXIS.3 would hold for them and the
  false-positive argument is void).

## Test 3: cone lemma sanity (cone.py)
- Claim: an SO_0(p,q)-invariant convex cone with nonempty interior in R^{p+q} that
  is pointed exists iff p = 1. Checks: for p >= 2 a path in SO_0(p,q) from identity
  to an element mapping a timelike v to -v (rotation by pi in a time plane);
  for p = 1 sign(v_0) of timelike v is preserved by 10^5 random products of
  boosts and rotations; the quadrant cone in R^2 has null form q(s,t) = s t,
  signature (1,1).
- FAIL: a counterexample element (p = 1 flips sign) or p >= 2 with no such path.

## Test 4: what the Qubit axiom's Clifford wording fixes (cliff.py)
Compute dim, centre and centre type for Cl(p,q) and Cl^0(p,q), p+q <= 5, and
identify M_2(C) (dim 8, centre C). Also check Herm(2): det has signature (1,3) and
PSD = {det >= 0, tr >= 0}.
- Prediction: full Cl(p,q) = M_2(C) exactly for (3,0) and (1,2); even part
  Cl^0(p,q) = M_2(C) exactly for (3,1) and (1,3) among p+q = 4; none at p+q = 5.
- Reading if true: the axiom's Cl(3,0) wording is consistent with 3+0, 2+1 and
  (as even algebra) 3+1, so it cannot fix d_t without a bridge premise.
- FAIL: any other (p,q) gives M_2(C), or one of the predicted ones does not.
  (Then the pinned-signature numerology is wrong or wider.)

## Addendum (written after cone.py first ran; disclosed)
My Test 3 wording "iff p = 1" was sloppy: the overall sign of the form is a
convention, and SO_0(2,1) = SO_0(1,2) has an invariant pointed cone (axis = the
single direction of the minority sign). The correct statement, checked in the
revised cone.py, is: a closed pointed convex cone with nonempty interior invariant
under SO_0(p,q) (n = p+q >= 2) exists iff min(p,q) = 1. The first run of cone.py
(p >= 2 case used a mixed vector, so it did not test the full claim) is kept as
cone_v1.out; the revised run is cone.out. With d_s = 3 fixed by the Lattice axiom,
min(d_t,3) = 1 iff d_t = 1, which is the only way the lemma touches the wall.
