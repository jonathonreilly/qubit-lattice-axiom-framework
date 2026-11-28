# Check of library/gap-band-cut-covariance-astra62.md (FINISH row 1571)

Checker: Claude (Opus 5.5). Status: complete. Not checked: PV internal proofs, PR 10114 eqs. (11) and (15), row 929 Lemma M as written (re-derived instead), literature attributions.

## Plan
1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read check 1556 section (v) (lemma (B)), row 1553 section 1.5, row 1566.
3. Check the note line by line: U(1) flux lower bound (Villain), transfer to Wilson, constants, quantifiers, same observable.
4. Comparison tests: photon at nonzero momentum, strong coupling, anisotropic strip.
5. Three SU(2) attempts, the "what (B) gives" section.
6. Compare with row 1566; equivalence test.
7. RESULT line.

## Step 1. Sources read (done)
- GOAL.md; FINISH.md "Working efficiently" and "Rules" (incl. "Equivalent is not progress").
- Target note in full (276 lines). Check 1556 sections (iv), (v), RESULT. Row 1553 sections 1.2-1.5. Row 1566 in full.
- Next: the PV note on main (equations (3.1), (4.1), (5.1)-(5.3), (6.1), section 6 filling), since the Villain flux bound rests on it.

## Step 2. Line-by-line work so far (hand checks; details in later sections)
- (3) sign and trace identity, (4) row/column symmetry, (5): re-derived, hold.
- Coset factorization, parallelogram step, harmonic norm ||h||^2 = V/n^4 = w/n = 1/R: re-derived, hold.
- Constants of M_beta: 4*162*2 = 1296 and 8 pi^2 512^3 8^4 re-derived; A>0 needs beta > 1157, so beta >= 2000 gives A ~ 2.2.
- Mixture lemma: midpoint excess in [0, delta r^2/2] (triangular weights sum r^2, half of it), Schur bound, strong Stieltjes moment via Friedrichs: hold.
- Bessel step: PF2 of the convolution, log-convexity of j! b0^-j w_j, ratio >= j/(j+1): hold.

## Step 3. PV statements read (main `8b11ae2bb`, the periodic finite-clock Villain note)
Read: section 1 (conventions, a(beta) = beta/384 - beta_1, beta >= 2000), section 3 ((3.1), Fejer regularization, harmonic subgroup H), section 4 ((4.1)-(4.3), 107-edge count), section 5 ((5.1)-(5.3), 32 colours, Q_ee = 6, source phase is the ORIGINAL rho(a)), section 6 ((6.1), small-current filling with ||mu||_1 <= 3R||rho||_1 <= 9 r^(3/2)||rho||, R <= 2r-1 <= 3r), section 7. The statements match every use the note makes. I did not re-check PV's own proofs; they are a main-repo note, outside this row.

---

# Check report

Provenance: Claude Opus 5.5 (high reasoning), lane note `library/gap-band-cut-covariance-astra62.md` as on disk at this check (276 lines). Hand check, no numeric run, not an audit. Overall FINISH class: CORRECT-NO-ADVANCE on (B) (it stays open), with one new proved comparison result (the U(1) refutation).

## A. Decisive outcome: (B) fails for weak 4D compact Wilson U(1) (lines 145-245)

**A1. Reduction (3)-(5), lines 124-150 — HOLDS.**
- (3): K^2 d1 d2 log K = K d1d2K - (d1K)(d2K). Integration by parts in X (D_c is skew under Haar on the moved links, since the axes read only 2- and 3-links) gives -2 int (d1K)(d2K). As kernels, d1K is D_c S and d2K is -S D_c, so int (d1K)(d2K) = Tr((D_c S)^2) = -sum_ij lam_i^v lam_j^v |<i,D_c j>|^2. Sign and factor 2 re-derived.
- (4): at s=t=z=0 the sewing measure K(A,B)^2 is symmetric and H_xy(X,Y) = H_yx(Y,X), so column sums equal row sums. Then 2|c_x c_y| <= c_x^2 + c_y^2 gives (4).
- (5): for U(1) the constant cut rotation preserves every spatial plaquette (each 1j plaquette at x_1 = 0 holds two cut links with opposite orientation) and commutes with T. So D_c = iQ and the left side of (3) is 2 Tr(Q^2 T^2v). Positivity of T is not needed here. The random axis sign i sgn(sin Q_x) multiplies H_xy by eps_x eps_y, which disappears inside |.|. So the test is the literal U(1) analogue of (B) at s=t=z=0, a member of the sup. With Q integer, E Q^2 >= Pr(Q odd).

**A2. Villain flux lower bound, lines 153-196 — HOLDS** (given the PV statements of Step 3).
- Charge: the seam twist puts e^{i theta N_p} on the n^2 01-plaquettes at x_1 = 0. Then q = sum N_01 over the 23-section, which is the 23-period of the closed integer form F = *N. Checked.
- Sheet S: closed (independent of x_0, x_1), 23-period one. Harmonic part 1/n^2, ||h||^2 = V/n^4 = w/n = 1/R <= 1/256. S - h is exact by Hodge on the torus.
- Coset weight Z_D = e^{-||h_0||^2/2beta} Theta(u). Parallelogram law: sqrt(Z_{D+S} Z_{D-S})/Z_D = e^{-||h||^2/2beta} sqrt(Theta(u+b)Theta(u-b))/Theta(u). Re-derived.
- Interpolation: PV (5.2) keeps the original source phase rho(a). So with d_rho congruent to rho(b) mod 2 pi, the integrand at t = +-1 is exactly the one for u +- b, and the mixture weights do not depend on the source. For intermediate t the integrand only has to be positive, which holds because z_rho < 1/2. I computed [log(1+z cos x)]'' >= -z/(1+z), which is stronger than (6.1). phi(1)+phi(-1)-2phi(0) = int (1-|t|) phi'' with int (1-|t|) = 1. Checked.
- Small currents (r < w/8): the graph has fewer than 2r edges, below w, the shortest period, so there is no winding. A filling mu with entries in 2 pi Z gives rho(b) = <mu, S-h> = -<mu,h> mod 2 pi, and |<mu,h>| <= ||mu||_1/n^2 <= 9 r^{3/2}||rho||/n^2. Count: at most 4V/r currents of size r in an ensemble, z/(1-z) <= 2e^{-A||rho||^2}, and t e^{-At/2} <= 2/(Ae). Constant 4*162*2 = 1296 and the factor V/n^4 = 1/R <= 1: checked.
- Large currents (r >= w/8, winding included): |d_rho| <= pi and V = R^3 w^4 <= 512^3 (8r)^4 give the second term 8 pi^2 512^3 8^4 sum r^3 e^{-4 pi^2 A r}. Checked. Uniformity in n and v comes only from R <= 512 and V/n^4 <= 1, and both hold at the fixed aspect.
- Threshold: A > 0 needs beta > 384 beta_1, about 1157. At beta = 2000, A is about 2.2. Agrees with PV.
- Rectangular torus: PV is written for equal sides L. Every step used here is local or uses the shortest period: the 107-edge count, the 32 colours (all periods even: n even, w = 2v even), Q_ee = 6, and no winding below the shortest period. PV's large-current Laplacian bound, which does use L, is not used: the note replaces it by |d_rho| <= pi. The claimed "verbatim" transfer HOLDS.
- Parity: D -> D +- S are bijections from even to odd 23-period cosets. So Z_odd >= d_beta Z_even and eta_beta = d_beta/(1+d_beta). Checked.

**A3. Transfer to the Wilson cosine weight, lines 199-245 — HOLDS.**
- Offset uniformity: F_0 - y = du + h_perp, where h_perp may carry a coexact part. The parallelogram law still costs exactly e^{-||h||^2/2beta}, and the Theta bound is uniform in u. Checked.
- Mixture lemma (6): the normalized Hankel entry is e^{-t r^2/2} times the midpoint excess, which lies in [0, delta r^2/2] (triangular weights sum to r^2, times 1/2). A Schur row-sum bound gives a perturbation below gamma_t/2, and the Poisson symbol of the Gaussian Toeplitz matrix is positive. Both Hankel forms (k = 0, 1) are positive. The strong Stieltjes moment step via the Friedrichs extension is correct: Ran A contains the Laurent polynomials, so ker A = 0 and A^{-k} 1 = x^{-k}. lambda is finite by sum_j e^{-t(j-y)^2/2} >= e^{-t/8}. Checked.
- Bessel input: I_j is the convolution of s_j = b0^j/j! with its reflection, so it is PF2 (Cauchy-Binet), and second differences are <= 0. g_j = j! b0^{-j} I_j is log-convex (a sum of products of 1/(j+i)), which gives I_{j-1}I_{j+1}/I_j^2 >= j/(j+1). This is the known Turan-type bound. Tail plus finite window plus I_j/I_0 -> 1 gives the uniform bound. Checked.
- Tonelli: prod_p I_{|F_p|} = int prod_p e^{-(F_p-y_p)^2/(2*2000)} dlambda^{(x)P}(y), with t = 1/2000, that is Villain coupling 2000. Evenness of I takes care of the Hodge sign. Then Z^W_odd >= d_2000 Z^W_even. Checked.
- (7): B_4 >= 2 eta_2000/n^2 >= (2 eta_2000/1024^2) v^{-2}, because n <= 1024 v. Checked.

**Constants and quantifiers (asked explicitly).** eta_2000 = d/(1+d) with d = exp[-1/4000 - M_2000/2] is explicit. beta_* is existential: it comes from delta(1/2000) and the Bessel limit, and it is astronomically large because gamma_{1/2000} ~ e^{-1000 pi^2}. The order is: t = 1/2000, then gamma_t, then delta(t), then J, then beta_*. The bound holds for every beta_W >= beta_*, every v >= 3 and n with n/v in {512, 1024}, with eta independent of n and v.
- It holds at one cut (x_1 = 0, direction 1); every other cut follows by translation and cubic symmetry.
- It holds at z = 0 and s = t = 0 only. (B) is a max/sup, so one member suffices to refute it: for every C and eps, take v > (C 1024^2/(2 eta))^{1/eps}.
- A lower bound at the other twists is neither claimed nor needed.
- The same observable: yes. Same axis rule restricted to U(1), same sewing mu_{0,2v}, same sup over x. The second route (lines 260-265) gives the same order again through the four corners, without the conserved charge.

## B. Comparison tests

**B1. Photon test at a nonzero momentum (lines 33-51) — HOLDS.**
- The Dirichlet chain cross coefficient beta sinh(omega)/sinh(v omega) was re-derived by summation by parts.
- The q = (2pi/n) e_2 Fourier coefficient over the cut is (1/n) sum_{k_1} f(k_1, q) with f >= 0. A constant h_0 has no q-coefficient, so the bound is robust to any zero-mode treatment.
- omega = 2 arsinh(sin(pi/n)) <= 2pi/n, v omega <= 2pi/512 < 1, and sinh a <= a cosh 1 on [0,1]. Together these give (1).
- Upper bound: |M| <= n^{-m} sum_k f, so the row is <= n^{-1} sum_k f <= C beta/(n v). Rotor term C(beta) n^{-2}.
- So the free 4D row is Theta(v^-2). The 5D unit-vector step holds for the linearized model only, as the note says: the cross-covariance is rho I by colour independence, and the two variances are equal by sewn-torus symmetry.

**B2. Strong coupling (lines 72-82) — HOLDS.** 6(D-1) neighbours. Oscillation 4 beta, TV <= osc/4, so q = 6(D-1) beta. Constant 1/4 * 3 * 2beta * 2beta = 3 beta^2. The degree >= v-2 follows from midpoint distance. The bound is uniform in the pins, so it covers every R_s and twist. The Dobrushin-Follmer covariance inequality is cited (PR 10114 (15)), not re-derived. The 3D Villain line is a sketch with an existential small beta.

**B3. Anisotropic strip (lines 93-119) — HOLDS.**
- Temporal gauge on the open slab: F_x reads (1, e_x). G_y reads (v-1, e_y) and the terminal g's, which are reachable only through level v-1.
- The swap of a marked component preserves the joint law: w_* is the minimum over all partial exchanges, so it is exchange-invariant, and an open factor lies wholly inside or outside a component. This gives (2), with |F - F'| <= 2 b_t.
- Marks: P <= 1 - e^{-4b}, so p = 1 - e^{-12} at b_t <= 3. p e^a = sqrt p, so a run weighs L = (1+sqrt p)/(1-sqrt p). J = 6(m-1). Vertical length >= v-2.
- At kappa <= kappa_*, J p_s L <= 1/2. Row <= 4 b_t^2 L n^{m-1} e^{-a(v-2)}, with a ~ 3e-6.
- The bound is real, but it is effectively a one-dimensional chain decay, as the note says ("no selectivity").

## C. The three attempts on (B) for 4D SU(2), beta in [2,3]

**C1. Single-link comparison: failure point HOLDS.** The five staples on a circle sum to zero, and the sixth is +-1 through the designated neighbour. TV = E_beta sgn h, which increases in beta. At beta = 2 it is >= 2 E h^2/cosh 2 = 1/(2 cosh 2), about 0.133 > 1/10, using E_Haar h^2 = 1/4 on S^3. The row is > 1.8. As the note says, this is an obstruction to the method only.

**C2. Replica exchange: failure point HOLDS.** At kappa = b_t >= 2, J(1 - e^{-4 kappa}) L is far above 1 (L ~ 4e^12).

**C3. Spectral test: HOLDS**, with one item not checked. (3)-(4) are an exact necessary test. For SU(2) the rotation at intermediate angles does not commute with T: the new holonomy e^{s a_x} P e^{-s Ad(V) a_{x+j}} moves the cut plaquettes. The odd-sector trial gives only e^{-O(beta n v)}. Not checked: the formula for eta_n from PR 10114 eq. (11). The conclusion does not depend on it.

## D. "What (B) would give" (lines 250-274) — HOLDS

- Four corners f, g, g, f: integral = 2(f - g). E_z|l_z| <= (pi^2/2) n^2 C v^{-2-eps}. Jensen both ways gives |log Z^{z+e_1}/Z^z| <= h_v. Three generators give 3 h_v. h_v = O(v^-eps) since n <= 1024 v.
- Second check: Z^{e_1}/Z^0 = Tr(C_1 T^2v)/Tr T^2v = 1 - 2p_- > 0, since it is a positive twisted integral. So B_4 >= (2/(pi^2 n^2))(-log(1 - 2p_-)). Checked.
- The purity identity is trivial.
- Spectator: P_m = sum p_j^2 <= max p_j <= 1/(1 + 2e^{-1/1024}), about 0.333 < 1/2 < 457/625. Checked.
- The constants agree with row 1566 P2(d)-(e): (pi^2/2) * 1024^2 = 2^19 pi^2.

## E. Comparison with row 1566 (free-Maxwell zero-mode identity sum_y h = beta/(n v))

- 1566 Lemma Z HOLDS. I re-derived chi = (1/n) 1_1 + d lambda and the minimum n^{d-3}(s-t)^2/v.
- It is exactly the k = 0 term of 1565's kernel M. With k_par = 0 and k_1 != 0 the transverse factor 1 - |h_1|^2/kappa vanishes, so the signed sum over the cut sees only k = 0: n^2 * n^{-3} * beta/v = beta/(n v).
- So the two notes agree on the power v^-2. 1565 (1) is the stronger form: it bounds the absolute row, holds with any zero mode (compact rotor included), and comes from the first transverse mode. 1566's signed identity uses the noncompact zero mode.
- 1566 Step 4(a) (4D compact U(1) weak FAILS, "ARGUED" via a monopole-free theta ratio) is now a written proof in 1565 (7), given PV. 1566's N-flux implication and 1565's second check are the two directions of the same four-corner inequality. No contradiction.
- One convention differs. 1565 tests the literal power 2 + eps in every D. 1566 tests (d-2) + eps, the power the four corners need. This changes only the 3D and 5D rows. For example, by (1) with m = 2 the free 3D photon fails the literal power but passes the adjusted one. It does not change any 4D verdict.

## F. Does (B) read the gap in 4D, or is its U(1)/SU(2) split the free-field marginality? (tests of row 1553 section 1.5, as corrected by check 1556 (iv))

- **(g1) HOLDS, now proved.** 4D compact U(1) is false at beta_W >= beta_* (Wilson) and at beta >= 2000 (Villain). The failure line l_1 is an order-one odd electric-flux probability p_- >= eta, fed through (5) or the four corners.
- **(g3) for 4D U(1): l_1 does not fire at the gapped twin; proved on both sides.** At 18 beta < 1, (B) holds with exponential decay uniformly in the pins, so p_- = O(v^-eps) there. The failure is therefore not repeated at both ends of the family: (B) is decided by the law, not by the algebra and the dimension. 5D SU(2): strong coupling holds, weak interacting open. 3D: the flux-sheet mechanism costs e^{-v/beta} (line 248), so l_1 does not fire.
- **The location of the split is the free-field marginality.** In 4D the free row is exactly Theta(v^-2) (1565 (1) plus its upper bound, and 1566 Lemma Z). (B) asks v^{-2-eps}. The U(1) Coulomb phase fails because its infrared is a free photon with an O(1/n) flux energy, so the charged fraction stays order one at fixed aspect. To pass, a law must beat the Gaussian scaling by a power. So (B)'s U(1)/SU(2) split is "infrared Coulomb vs not". Its truth value is set by the law, and its threshold sits at zero margin on the 4D Gaussian count. No perturbative or scale-invariant estimate can supply the eps.
- **What (B) reads is electric-flux confinement, not the gap.** (B) implies 1566's (N-flux): charged fraction O(v^-eps) (PROVED in 1566 P2(f); quantitative converse in 1565 lines 260-265). It gives no purity:
  - (g4): the spectator leaves (B) unchanged and destroys purity, so (B) holds or fails on a gapless product member exactly as for pure SU(2), and it cannot be a sole seed input.
  - GUIDE only, not proved: a gapped deconfined phase with an order-one charged-flux fraction would also fail (N-flux), hence (B).
- **Equivalent is not progress.** (B) is not equivalent to the seed or to (PUR-io). It is incomparable with both by 1566 Step 7 (spectator; seven nearly degenerate charged levels), and nothing in 1565 contradicts that. Its only proved consumer use, twist ratios within 3 h_v, is contained in the full seed at the tested coupling (1566 Step 7). So (B) is a law-reading, non-equivalent confinement statement, with no gain over the seed shown. 1565 claims no more than this (line 119: "no selectivity for the isotropic band"; RESULT: "would control relative twist weights only").

## Defects found

None that breaks a statement.

- Wording (no correction required): "an explicit estimate" in line 245 means that eta_2000 is explicit. beta_* is existential and astronomically large, and line 245 itself says the threshold is existential.
- Not checked here:
  - PV's internal proofs (main-repo note).
  - PR 10114 eqs. (11) and (15). (15) is the cited Dobrushin-Follmer inequality; (11) is the eta_n formula, which is not load-bearing.
  - Row 929 Lemma M. I re-derived its cross coefficient independently.
  - The literature attributions in lines 3-10 and 258.

RESULT — Row 1565 holds as written. For sufficiently weak 4D compact Wilson U(1) (beta_W >= beta_*, existential) and Villain at beta >= 2000, the U(1) analogue of (B) is at least (2 eta_2000/1024^2) v^-2, uniformly in n and v at fixed aspect, at the same observable (s=t=z=0 member of the sup). Holding at one cut and one twist is enough to refute it, because (B) is a sup and a max. The photon, strong-coupling and anisotropic tests hold. The three SU(2) attempts stop where stated. "What (B) would give" holds and agrees with row 1566, whose zero-mode identity is the k=0 term of 1565's kernel. Under the tests of row 1553 section 1.5: (B) reads the law in 4D ((g1) and (g3) are now proved for U(1)), but its U(1)/SU(2) split sits exactly at the 4D free-field marginal power. It reads electric-flux confinement ((N-flux)), not the gap or purity. It is not equivalent to the seed and gives no gain over it. (B) for 4D SU(2) at beta in [2,3] remains open.
Checked line by line by Claude (Opus 5.5).
