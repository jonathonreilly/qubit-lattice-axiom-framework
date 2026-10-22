Ruleset A: the hypercube does not select Pati-Salam or the Standard Model inside Spin(10)

Date: 2026-10-22
Type: bounded theorem (exact commutant and representation checks) plus a mean-field diagnostic and a gate verdict
Runner: scripts/hypercube_spin10_breaking_ruleset_a_2026_10_22.py (22 PASS / 0 FAIL, about 7 s, under 250 MB)
Target: agents/minimal-toe (Ruleset A, decisive calculation 2) and agents/minimal-toe-merged (vacuum orientation)

Claim scope
-----------
Exact finite checks on Cl(10), built from 5 modes (32 dims, with the 16 as the even half), and on the vector 10. The
hypercubic group W(B4) has order 384. The checks cover:
- which commutants inside so(10) the hypercubic group can leave, for the natural ways it can act on the 10 Clifford
  generators;
- the content each reading leaves, in anomalies and spin;
- whether SU(2)_R x U(1)_B-L -> U(1)_Y can be a structural (one-body) commutant at all;
- a Casimir-exchange mean-field comparison of the vacuum orientations named by the merged ruleset.
This is a supplied model and a finite diagnostic, with no physical identification. Known group theory (Cartan's involutions
of so(n), the 16 branchings) is used, not disputed.

1. Involutions (A1, A2)
------------------------
- Theorem A1. Conjugation by a product of k Clifford generators leaves so(k) + so(10-k), with dims 36, 29, 24, 21, 20 for
  k = 1..5.
- Pati-Salam so(4) + so(6) (dim 21) is exactly the flip of 4 (or 6) generators.
- Spin(9), the direction of A's 16x16 10-condensate, is the flip of one (a Pin reflection).
- Theorem A2. Theta = G1G2G3G4 squares to +1, lies in Spin(10) and splits the 16 as 8 + 8 = (4,2,1) + (4b,1,2).
So "Pati-Salam" is the same statement as "the lattice reaches the internal Clifford algebra through one rank-4 involution".

2. The hypercube acting on the generators (B1-B4)
--------------------------------------------------
Theorem B1. These are the commutants in so(10) of W(B4), with the commutant of the rotation subgroup in brackets:

| Action on the 10 generators | Reading | Commutant |
|---|---|---|
| 4v + 6.1 | Gamma_mu carried on each lattice direction | 15 = so(6) (15) |
| 4v + Lambda^2 | the 6 = hypercube planes | 0 (0) |
| 4v + 4v + 2.1 | spin and taste vectors | 2 (2) |
| 4v + abs(4) + 2.1 | one link mode per direction, reversal = particle-hole | 3 (3) |
| 4.det + 6.1 | the lattice sees the internal algebra only through Theta, via reflections | 21 = Pati-Salam (45) |
| 10.1 | the lattice is blind to the internal algebra | 45 |

Pati-Salam appears exactly when the lattice acts through a sign on 4 generators. It then acts only through
orientation-reversing elements, since the rotations act trivially. No natural lattice-tied action gives it.

Theorem B2. In the Gamma_mu realisation the central inversion x -> -x does map to Theta. But the same group contains every
axis reflection (conjugation by Gamma_mu), so the unbroken internal algebra is C(G1..G4) = so(6), not C(Theta) = 21. The
so(4) is locked to lattice rotations.

Theorem B3 (untwisted: so(4) becomes Lorentz).
- The 16 is (2,1,4) + (1,2,4b): 8 Weyl fermions, which is half a family.
- There is no internal SU(2).
- SU(4)^3 is anomalous: tr_L H^3 - tr_R H^3 = -12. A left 4 plus a right 4b is the same as two left 4s, so R4 fails.

Theorem B4 (twisted, Dirac-Kahler type gamma_mu x Gamma_mu).
- The states present are (j_a, j_b) = (0,0), (1,0) and (1/2,1/2). Every state has integer spin.
- This contradicts the measured spin 1/2 of every SM fermion.
Hence the lead "4 tied to the lattice directions and reduced to spin by twisting, 6 internal" is FALSIFIED in both forms.

3. The last step cannot be structural (C1-C5)
----------------------------------------------
- C1. Y = (N1+N2)/2 - (N3+N4+N5)/3 and X = 2N - 5 reproduce the SM hypercharges and the U(1)_chi charges (-5, -1, 3).
- Theorem C2. C_so10(SM) = span(X, Y). The commutant of the SM on the 16 inside gl(16) is abelian and of dim 6, because the
  16 is multiplicity-free.
  - So any set F of one-body selectors (any unitaries on the 16) with C(F) containing the SM has C(F) containing
    C(C(SM)) = SM x U(1)_chi, of dim 13.
  - Exact SU(3) x SU(2) x U(1)_Y is never a commutant. This agrees with the merged ruleset's dimension 13 for aX + bY,
    and shows that 13 is the floor for any structural selector.
- Theorem C3. C(Theta, J) = u(2) + u(3) = 13 for a complex structure J that pairs inside the 4 and inside the 6. C(J) =
  u(5) = 25.
- Theorem C4. The hypercube supplies no such J. The commutant of W(B4), and of its rotation subgroup, on R^4 is the
  scalars, so J^2 = -1 is impossible: the u(2) inside so(4), which would make the weak SU(2) one of the two so(4) factors
  plus hypercharge, is not selected.
- C5. Breaking U(1)_chi needs a Fock (pair) operator. Since nu^c is the unique Y = 0 state, the SM-singlet one-family pair
  is nu^c nu^c, with Delta(B-L) = 2. It carries charge -1 under A's protecting Z4 = exp(i pi X/2) = -i, so it breaks that
  Z4.
So SU(2)_R x U(1)_B-L -> U(1)_Y is obtainable only dynamically, through a nu^c nu^c-type condensate that breaks R4's
protecting Z4. That is consistent with a seesaw, but it is not structural.

4. Vacuum orientation (D1-D5; coordinator request)
--------------------------------------------------
Theorem D1. C(16) = 45/4, and:
- 16x16 = 10 (C = 9) + 120 (21) + 126 (25);
- 16x16b = 1 + 45 (16) + 210 (24).
One chiral 16 has NO 45 bilinear, so the orientation aX + bY needs the mirror or a composite 45.

The binding strengths (2C16 - C_R)/2 are:

| 1 | 10 | 45 | 120 | 210 | 126 |
|---|---|---|---|---|---|
| 11.25 | 6.75 | 3.25 | 0.75 | -0.75 | -1.25 |

Theorem D2. The 10 pairing has uniform gaps for every direction (Clifford identity), as the singlet does.

Diagnostic D3 (flat-band BCS with unit cutoff, channel coupling g0 * Delta C, g0 = 0.25 and 0.4).
- The free-energy order, lowest first, is: singlet << 10 (Spin(9)) << 45 J_12 < best aX+bY < X < Y.
- For example, at g0 = 0.25: -5.09, -1.65, -0.117, -0.068, -0.062, -0.062.

Diagnostic D4. At equal coupling the uniform-gap 45 direction J_12 beats every aX + bY. J_12 leaves U(1) x Spin(8), of
dim 29. The reasons are that Y leaves nu^c ungapped and X has gaps 5:1:3. The best of the 82 sampled Cartan directions is
a single plane.
So aX + bY is not even the best orientation inside the 45 channel.

D5. A hypercube selector that keeps only Theta-commuting orientations does not help. The singlet, J_12 and aX+bY all
commute with Theta.

Verdict for the merged ruleset's question:
- With the mirror present, the singlet wins, and chirality is lost.
- With the family alone, the 10 wins, giving Spin(9).
- The SM orientation is selected in neither case.
Taste multiplicity from the 2^3 cell or the 2^4 hypercube multiplies every channel equally and does not change the order.

5. Owner principle: the 5 from covariant clusters of one-mode sites (E1-E5)
-------------------------------------------------------------------------
Per-site 5 modes (Rulesets A and B, and the merged ruleset) are FLAGGED as a smuggling risk. Sections A, C and D are
statements about the abstract Spin(10) and do not depend on where the modes live. Section B and the checks below do.

- Theorem E1. No W(B4)-covariant cluster has 5 sites.
  - About a site, every other orbit is even and has at least 8 sites (at least 6 under O_h in 3D).
  - About a body centre, every orbit is even and has at least 16 sites.
  - Other centres have no fixed site, and the inversion pairs the sites. This last case is argued, not enumerated.
- Theorem E2. Irrep dimensions divide the group order (Frobenius, cited). The orders are 384, its double cover 768, 12288
  with shifts mod 2, 48 and 96. All are of the form 2^a 3^b, so no symmetry-protected lattice multiplet has dimension 5 or
  10. A 16 is allowed.
- Theorem E3. A 1-dim character appears on an orbit iff it is trivial on the stabiliser. The smallest orbits that carry
  each one are:
  - "flip sign" (-1 on axis reflections, +1 on permutations): the 16 corners (1,1,1,1);
  - perm sign: 192 sites;
  - det: 384 sites.
  - Flip sign has no O(4) counterpart, since O(4)/SO(4) = Z2 leaves only det. It is a hypercubic artefact.
- Theorem E4. Take the 33-site cluster: the centre plus the corners at distance 1 and 2.
  - Its trivial modes (x3) and flip-sign modes (x2) form a 5 = 3 + 2.
  - The lattice commutant on their 10 Majoranas is so(6) + so(4), exactly Pati-Salam.
  - Adding mode number J gives u(3) + u(2) = 13 = SM x U(1)_chi.
  - This is ruleset B's C2 + C3 split, now coming from lattice characters instead of being put on a site.
- Theorem E5 (Schur). Nothing protects that 5.
  - A generic W(B4)-invariant update acts on each multiplicity space as an arbitrary Hermitian block. Its internal
    commutant is therefore abelian: 11 distinct levels, commutant 11, against 25 for the lattice group alone.
  - The 3 + 2 degeneracy behind SU(3) x SU(2) costs 3 tuned equalities, and one more for SU(5). R4 forbids such tuning.
- General consequence. Lattice covariance alone never protects a non-abelian internal frame built from one-mode sites. A
  Spin(10), Pati-Salam or SM frame must be:
  (i) accidental, which means tuned;
  (ii) supplied per site, which is flagged;
  (iii) emergent, with the lattice group forbidding every relevant or marginal breaking operator, as for staggered taste.
  Under (iii), the lattice's image in Spin(10) sets the residual commutant, and that is exactly what section B computes.

Against measurement
-------------------
- Measured spin 1/2 of all SM fermions falsifies the twisted reading (B4).
- Measured chiral, anomaly-free weak and colour content falsifies the untwisted reading (B3).
- The observed unbroken group SU(3) x SU(2) x U(1)_Y is not produced. The best structural floor is SM x U(1)_chi, which then
  needs a Delta L = 2 condensate. That condensate fits a seesaw (measured neutrino masses) but has no derived scale.

Gate verdict (anti-smuggling)
-----------------------------
No rule is adopted. The only route to Pati-Salam is a candidate rule: "the hypercube's orientation reversal acts on the
internal algebra as a product of D = 4 generators". It FAILS clause (2) in substance:
- It supplies a 4-plane in R^10, a point of Gr(4,10) with 24 parameters, by hand.
- Its only lattice input is the coincidence that the number 4 equals D.
- The mechanism that would really tie generators to directions (Gamma_mu per direction) gives so(6) instead.
Row 12 of Ruleset A stays M for the subgroup, and the hypercube 4+6 lead is a FAILURE, not a reduction.

The cluster version, "the frame is the trivial + flip-sign part of the 33-site corner cluster", is the closest structural
hit: it gives Pati-Salam, and with J it gives SM x U(1)_chi. It still FAILS the gate:
- (1) it needs 3 tuned degeneracies;
- (2) the choice of cluster and of which isotypic modes are light is supplied;
- (3) it makes no untuned prediction;
- it bends the Qubit axiom only through zoom, so that is acceptable.

Repairs worth testing (UNTESTED)
--------------------------------
(a) A rule that forbids family-mirror bilinears locally, for example family and mirror on different rungs. That removes the
    singlet and 45 channels together, which leaves only the 10/126 channels of one 16. The SM orientation would then need a
    126-type nu^c nu^c plus a separate SU(5)-type selector, and neither is derived.
(b) Look for a structural complex structure J elsewhere, for example a time orientation in the Z^3 x tick reading, where the
    hypercube is not isotropic. C4 rules it out only for the full 4D hypercube.
(d) Route (iii) of section 5: design a cluster update whose lattice group forbids every relevant Spin(10)-breaking
    operator on an emergent 16. The 16 is allowed by E2. Then compute the image of the lattice group in Spin(10). This is
    the only route that is consistent with the owner principle and with R4.
(c) Compute composite-45 four-fermion channels non-perturbatively. D3 is single-exchange mean field and is not decisive
    against strong-coupling SMG physics.

Smuggling review
----------------
- Supplied: the 5-mode Cl(10) realisation, used as an abstract algebra. Read as one site holding 5 modes, it is a
  smuggling risk under the owner principle; the list of W(B4) actions in B1 (natural, but not exhaustive); the
  Casimir-exchange channel strengths (one-gauge-boson, MAC-type); flat-band BCS with unit cutoff; couplings g0; the U(5)
  labelling used for X and Y.
- Forced (exact): the involution commutants; B1-B4; C2 (13 is the floor); C4 (no hypercube J); D1, D2; E1-E5.
- Cited, not rederived: Frobenius divisibility (E2).
- Measured inputs used: spin 1/2 of SM fermions; chirality and anomaly freedom of observed content.
- Cited, not rederived: Cartan's classification of involutions; the MAC heuristic.
- Repo context checked:
  - A3_ROUTE4_SPIN6_CHAIN (main; SU(4) -> SU(3) x U(1)_B-L derivable given retained colour);
  - GRAPH_FIRST_SU3_INTEGRATION and SELECTOR (main; su(2) + su(3) after a selected axis on the 2^3 taste cube, a quartic
    selector);
  - agents/pati-salam (rung-1 cell (4,2), no mass pattern keeps exactly SU(4) x SU(2));
  - agents/minimal-toe-merged (aX+bY, dim 13): consistent, and C2 sharpens it.
