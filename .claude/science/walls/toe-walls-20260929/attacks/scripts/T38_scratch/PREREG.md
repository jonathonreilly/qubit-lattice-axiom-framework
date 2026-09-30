# T38 pre-registration (written BEFORE running any script)

Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check only).
Wall: T38 = L08-W1 + L11-W6, "count the paired mode once or twice", target r = |b|^2/a^2 = 1/2.
Notation: H = aI + bC + conj(b)C^2 on the hw=1 triplet, eigenvalues lam_k = a + 2 Re(b w^k),
Q = Tr H^2/(Tr H)^2 = (1+2r)/3.

Route the test decides: R2 "the wall is a choice of reference measure on the two-sector menu
(block vs state), so no dynamics / ergodic / typicality / symmetry principle can supply it".
If R2 is right the wall is PRICED at one premise (block-equipartition). If a canonical measure
hits r = 1/2 without the block premise, R2 is dead and that measure is the new route.

## Test 1 (exact identities; check, not decisive)
Claim: r = 1/2 is algebraically the same statement as each of
 E1 angle(lam,(1,1,1)) = 45 deg;  E2 ||diag H||_HS = ||offdiag H||_HS (record-basis dephasing);
 E3 |<u|psi>|^2 = 1/2 with psi = lam/|lam|, u = (1,1,1)/sqrt3 (C3-character measurement, P(trivial)=1/2);
 E4 Tr rho_H^2 = 2/3 with rho_H = H/Tr H;  E5 lam^T (3I - 2J) lam = 0;  E6 e1^2 = 6 e2.
PASS: sympy proves each equals r=1/2 identically.  FAIL: any mismatch -> withdraw the reformulation claim.

## Test 2 (carrier-Gram lemma; check)
Claim: (i) an operator form Tr(Gamma H^2) induced by a C-invariant carrier Gram Gamma is invariant under the
residual clock D (b -> w b) iff Gamma is proportional to I, and then equals HS = diag(3,6,6), i.e. rho = g0/g1 = 1/2;
(ii) the Schur family of C3-equivariant identifications of the amplitude space with the carrier T1 sweeps the whole
cone diag(s^2, d^2, d^2), the natural ones (H e_0, eigenvalue vector) give HS, only the literal-coordinate one gives flat.
PASS: both hold.  Reading if PASS: ambient covariance does not force the flat point, so the continuous cone freedom is
not independent of the count bit (only the product w_d/w_s matters).  FAIL: some D-invariant induced form with rho != 1/2.

## Test 3 (symmetry-pairing lemma; check)
Claim: any unitary or antiunitary T (T commutes with C or inverts it, T^2 = +1 or -1) that is a symmetry of H and
exchanges the two doublet eigenspaces forces lam_1 = lam_2 (delta in (pi/3)Z).  At delta = 2/9 no such T exists.
PASS (route "count-once as a symmetry orbit of the physical H" dead): holds for all four T types.
FAIL (route alive): a nondegenerate H (Im b != 0, sin 3 delta != 0) invariant under some pairing T.

## Test 4 (canonical-measure scan; the decisive test of R2)
Ex ante list of measures on the space of C3-invariant operators / sector weights, all evaluated for central r
(mean and median), N = 4e6 samples, seed 20260929:
 A Lebesgue in (a,b_R,b_I) on the positive-spectrum region (flat triangle)   [= Dirichlet(1,1,1) on lam fractions]
 B uniform on the positive octant of the sphere in lam (isotropic, HS)       [= Dirichlet(1/2) on mass fractions]
 C Dirichlet(1,1,1) on mass fractions m/Sum m
 D Dirichlet(1/2) on lam fractions (Bures, diagonal)
 E |Vandermonde(lam)|^beta on the octant sphere, beta = 1, 2
 F Haar-random real / complex unit vector (all signs), median only (mean of r diverges)
 G state-counting weights (1/3, 2/3);  H stack/groupoid weights (1/2, 1);  I real-Plancherel weights (1,2)
 J Lebesgue on the disc |b| <= a (2x2-minor positivity only), and on all of R^3 projectivised
 K block-counting weights (1/2, 1/2)   [EXCLUDED from PASS: it is the quotient premise itself]
 L Dirichlet(alpha) family: the alpha with mean r = 1/2   [ONE FREE PARAMETER: excluded from PASS, reported]
PASS (R2 dead): some entry among A-J (parameter-free, no reference to the two-block quotient, using the framework's own
full positivity requirement where positivity is used) has mean or median r within [0.49, 0.51].
FAIL (R2 survives, wall PRICED): none does.  Any hit that needs a dropped constraint or a free parameter is reported as
numerology, not counted as PASS.

## Reading rules fixed in advance
- Test 1-3 are algebra checks; they cannot pass the wall by themselves.
- Only Test 4 PASS can move the outcome away from PRICED/STANDS.
- A tuned or constraint-dropping coincidence is labelled numerology.
