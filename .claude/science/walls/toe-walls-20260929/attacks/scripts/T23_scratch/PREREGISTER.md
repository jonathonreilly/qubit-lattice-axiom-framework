# T23 pre-registration (written before t23_test.py was run)

Question the test decides: is the "orientation bit" of L08-W5 (S3 sign, sign(Delta), Brannen delta sign)
a mirror-image (handedness) bit, as the wall states, or a label that the Lattice axiom's own PROPER
rotations already flip? And is any single-sector orientation sign observable?

Setting: the one-component staggered surface on the periodic 4^3 torus used by the landed hw=1 notes
(kernel of D = all 2-periodic functions = the 8 corner waves (-1)^{c.x}; hw=1 triplet = c in {e1,e2,e3}).
Site-permutation unitaries U_g (g = signed permutation matrix) act on corner waves by permuting c
(sign-free). Label level only; operator-level dressing is a separate premise (P3 in the report).

Blocks and readings

A  Group theory of O (24 proper) and O_h (48) on the hw=1 triplet.
   PASS (wall misframed for L08-W5):  (A1) the induced map O -> S3 is onto; every transposition is the image
   of some det=+1 rotation; (A2) the kernel of sgn o pi inside O is the tetrahedral group T (order 12) and
   sgn o pi differs from det (det is trivial on O); (A3) elements of O_h acting on the triplet as an even
   permutation form a group of order 24 containing the inversion (the stabiliser of a circulant W(delta) is
   T_h, achiral).
   FAIL (wall stands as stated): the image of O in S3 is only A3, or every transposition needs det=-1.

B  Circulant W(a,b)=aI+bC+conj(b)C^2 (the Koide/Brannen mass operator).
   PASS: TS W TS = conj(W) exactly (K equals proper-rotation conjugation on the Hermitian section);
   spectra of W(delta) and W(-delta) coincide; Tr W^n identical; orbit of W(delta) under pi(O) is {W(delta),W(-delta)}.
   FAIL: any of these differ.

C  Contrast with the Cl(3)/M2(C) pseudoscalar omega = sigma1 sigma2 sigma3 = i.
   PASS: every det=+1 signed permutation is implemented by a unique-up-to-scale linear X in M2(C)
   (X sigma_i = R_ji sigma_j X) and fixes omega; no det=-1 one is implemented linearly, each is implemented
   antilinearly (X K); the characters sgn o pi and det are distinct on O_h (agree on exactly half the group).
   FAIL: the S3-sign and omega-sign flip under the same elements (then they would be one Z2).

D  Absolute versus relative.
   Two sectors W1=W(1,b1), W2=W(1,b2), b_i = r e^{i d_i}. Take the O-invariant joint observable Tr(W1 W2)
   and the pair of spectra.
   PASS: flipping BOTH signs changes no O-invariant (Tr(W1W2), spectra); flipping ONE sign changes Tr(W1W2)
   when d1 d2 != 0 mod pi/3 (relative orientation is observable, absolute is not).
   FAIL: an O-invariant sensitive to the absolute sign, or insensitive to the relative sign.

Outcome map
 - A,B,C,D all PASS  -> "orientation bit" of L08-W5 is a proper-rotation frame label: MISFRAMED as a
   handedness wall for the flavor member; the true residual is (i) state-level breaking O -> T_h
   (existence, registered data) and (ii) cross-sector relative products.
 - A fails -> STANDS (no route moved).
 - C fails -> the two Z2 are one; bundle T23 stays a single bit.

## Addendum (added AFTER A-D and the dressed-symmetry run, so NOT pre-registered; labelled post hoc)
Block E: reading of the circulant W(a,b) as a spin-1 (vector) triplet in a uniaxial field along the
body diagonal n=(1,1,1)/sqrt3.  Pass reading: W = (a-b1) I + 3 b1 n n^T -/+ sqrt3 b2 (n.L) exactly, with
(L_k)_{ij} = -i eps_{kij}; the pi-rotation about [1,-1,0] acts on vectors as -TS, sends n -> -n, and sends
b2 -> -b2.  Fail reading: the identity fails (then "vector triplet in a [111] field" is not a valid reading).
Block F (dressed symmetries, operator level) was run as exploration; its numbers are reported as checked
but were not part of the pass/fail map.  Dressed proper-rotation character decomposed by hand below
(E,8C3,3C2,6C4,6C2') = (8,2,0,4,0) -> 2 A1 + 2 T1 (computed in t23_dressed2.py, decomposition in the report).
