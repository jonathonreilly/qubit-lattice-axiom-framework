# FINISH row 895, gap-glue-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone commit: de5181bd72f54e89fd7411085e39524f751c384c (read-only clone /Users/jonreilly/ym4d-lead/clone, pulled 2026-11-13, already up to date).
Author: Claude Fable 5.2, max effort. Row 895. Status of this file: UNCHECKED author text.
Marks: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE (numeric, never a proof), OPEN.

## Target

The glue half at order one. Row 892 (Lemma SPLIT, Corollary O1) reduced the Theorem SH seed to two one-box
numbers of the first-passage action: the centre-even thermal sum S_ev at most 1/10 and the flux part Q_0 at
most 1/20. Proposition W needs glue at level 160^(-16). This note attacks S_ev at most 1/10 on one box,
uniformly in the cutoff. It must: state the crux lemma exactly; decide whether the glue half carries
confinement content or is pure even-sector mixing; decide whether it separates from the flux half; attempt
the crux lemma as a real proof and say where it stops; test each step against U(1) Coulomb, Z_2, frozen 2T.

## Plan (one step per response; each step is appended here before the next starts)

1. Read row 892 (SPLIT, O1, the graph) and record the exact definitions of S_ev, Q_0 and the one-box form.
2. Read SEED-FP (finish line lines 110-160), Theorem SH, and the seed proofs of rows 835/836; record why they stop near 1/3.
3. Read row 863's B1 (the two-slice law as a Schroedinger bridge) and the fact tests (rows 786, 838, 839, 843, 845).
4. State the crux lemma (GLUE) exactly, in one-box form, with its constants.
5. Structure: does GLUE carry confinement content, or is it even-sector mixing? Can it separate from the flux half? Decide with proofs or counterexamples (U(1), Z_2, 2T tests).
6. Attack A: even-sector Poincare / bridge form of B1. Real proof attempt; record where it stops.
7. Attack B: block criterion in the even sector and comparison with strong coupling; record where it stops.
8. Assemble: what is proved, what is open, the RESULT line.

## Step 1. Row 892's one-box form (READ D/library/gap-crux-core-max.md L263-281, L327-352, L380-420, L421-479)

Definitions (READ L267). B a periodic box. T = T_(B,0) its positive trace-class transfer operator. C_2, C_3, C_4 the commuting centre flips of the three spatial directions. P_chi the eight sector projections. Z_chi(t) = Tr(T^t P_chi), at least 0. lambda_0 the top eigenvalue, simple, with an even eigenvector.
- S(t; B) = Tr T^t/lambda_0^t - 1 (full thermal sum; the object of (SEED-FP) and Theorem SH).
- S_ev(t; B) = Z_0(t)/lambda_0^t - 1 (the centre-even thermal sum; chi = 0).
- q_i = Tr(T^t (1 - C_i)/2)/Tr T^t = (1 - Z^(v_1i)/Z^0)/2; Q_0 = max_i q_i.

Lemma SPLIT (READ L269-270; PROVED there, unchecked; check row 893). If 3 Q_0 is below 1: (1 + S_ev)/(1 - Q_0) at most 1 + S at most (1 + S_ev)/(1 - 3 Q_0). Also S_ev at most S, Q_0 at most S/(1 + S).
Corollary O1 (READ L272). (b) S_ev at most 1/10 and Q_0 at most 1/20 give S below 3/10. (c) S at most s gives S_ev at most s and Q_0 at most s.
Thresholds of Theorem SH (READ L273, from D/library/gap-seed-shape.md L116-125): t(r) = 1/1650 (r = 2), 1/100 (3), 1/25 (4), 1/10 (6), 3/10 (r at least 24), r = b/a, on S(a; b^3). (SEED-FP) uses 1/5041 at r = 2.

The pair (READ L275-280):
  GLUE-FP: S_ev(a; b^3) at most t(r)/2 (1/10 at r at least 24).
  (Q-FP) = (CORE): Q_0(a; b^3) at most t(r)/7 (1/20 at r at least 24).
One box (a, b, b, b), one time, twist 0, no rate.

Proposition W (READ L401-402). b at least 24 a, a even, a at least 82. GLUE at level S_ev(a; b^3) at most 160^(-16) and S_ev(a/2; b^3) at most 1, plus (WALL)_40 for the seven sectors, give Q_0 at most 1/20, S below 3/10, and a gap on every larger cube. 160^(-16) = e^(-81.2).

Row 892's verdict on GLUE (READ L448, L260): "GLUE | even sums small at one physical size | with (NGD): seed | no flux node | needed by every chain | OPEN; no tool tonight". "No flux node supplies GLUE."

Row 892's fact-test table already places the U(1) failure in GLUE for the relative nodes (READ L290-291): (KURT) and (FUSE-E) hold for U(1), "the failure must then sit in GLUE". And (NGD) is "false for Z_2 above 2.191 and frozen Q_8, 2T (ARGUED: gapped and deconfined), and empty for U(1) Coulomb" (READ L325).

Consequence for this note (ARGUED from the READ lines; made exact in Step 5). The fact tests split between the halves:
- U(1) Coulomb must fail GLUE (photons: the even sector is gapless). 
- Z_2 above 2.191 and frozen Q_8, 2T are "gapped and deconfined": they are expected to PASS GLUE and fail the flux half. So the T-FIN test does not bind a proof of GLUE; a proof of GLUE may be blind to the difference between SU(2) and 2T. The test that binds GLUE is T-U1 alone, plus the worst-case caps.

## Step 2. (SEED-FP), Theorem SH, and the strong-coupling seed proofs (READ)

(SEED-FP) (READ D/library/gap-finishline-opus.md L119-125). One physical size ell, s_* below 1/5041, K_0; for every first-passage datum (K, beta) with K at least K_0: S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) at most s_*. It is the thermal sum of the BARE Wilson transfer operator of the periodic cube of physical side ell at physical time ell/2. By the exact identities READ there (L127: the integral of rho_k dV_k equals Z at every level; the dilation identity, SA L6863-6869) every partition-function form of the seed is a statement on the account's densities with no loss. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
- "The seed must be a statement about the actual measure" (READ L147). A seed for a plain Wilson weight at the unit scale does not give (SEED-FP) (READ L149, ARGUED there). So "one box of the first-passage action" means: the bare Wilson measure at the first-passage data (K, beta), box of fixed physical size, lattice sides a = ell_t/a_K, b = ell_s/a_K tending to infinity with K.
- Uniformity needed (READ L156-160): one physical size, one margin, all large K. No uniformity in volume, in g, in a complex coupling or in boundary values.
- The twisted forms are outside the account's present scope (READ L160): the account runs on untwisted tori only. S_ev = (1/8) sum over temporal twists k of Z^k / lambda_0^a - 1 reads twisted tori. So GLUE-FP in its literal form is a bare-lattice statement.

Theorem SH (READ D/library/gap-seed-shape.md L89-110, L116-126; checked row 707 by the same model family). Setting: symmetric Z with a positive trace-class transfer operator in each direction, simple top eigenvalue. S(a; B) at most t(r) implies a gap on every cube of side at least b. Facts used: (T) S(t + t'; B) at most S(t; B) S(t'; B); Lemma A; Lemmas K, X. It holds "for every model in that abstract setting" (L57). Ceiling (READ L209-221): two-phase Ising gives S to 1 with no gap, so no threshold above 1 exists in the class. Massless ceiling (L223-243): the compact Gaussian with windings; the oscillator factor grows like exp(0.11 r^3).
GUIDE (READ L265, the free-gas model of Section 5): the thermal sum of a massive theory is the volume times the density of one-particle states: g(a; b^3) is close to b^3 (m/(2 pi a))^(3/2) e^(-m a).

Strong-coupling seed proofs (READ D/library/gap-seed23-opus.md L34-64, L66-95, L372-438; D/library/gap-blockcrit-opus.md L244-311; FINISH rows 835, 836, checks 840, 841).
- Route of proof. D-shape: Phi_B(a; beta) = 2 F(a, B) - F(2a, B) = 12 a |B| int_0^beta (abar_(2a,B)(s) - abar_(a,B)(s)) ds, and S(a; B) at most e^(Phi_B) - 1 (READ seed23 L77-80). So the whole seed is a comparison of the mean plaquette of two tori, (a, B) against (2a, B), integrated over the coupling from 0. The comparison is (17): a Dobrushin (Wasserstein, chord metric on S^3) contraction across a/2 slices with the cut set D exempt. It bounds the FULL S, so both halves at once.
- Ranges. Ungauged single link: 18 partners times beta/4 gives 2/9. Temporal gauge (Theorem T): 14 partners, 2/7. Line-field gauge (Theorem F): 12 partners, 1/3. Star blocks with per-event forest gauge (Theorem ST): 0.3609. GUIDE larger flat blocks: about 0.42.
- Why they stop (READ, PROVED there). (i) Lemma AVG: in every tree gauge the mean number of free partners of a free link exceeds 12; with the uniform constant 1/4 per partner (Corollary V1, attained at zero field) no single-link argument passes 1/3. (ii) Proposition CEIL: every vertex block has a vertex with 7 free links; worst-case internal propagation has spectral radius at least (2 + sqrt 10) beta/4, so the method is void at beta at least 0.775. (iii) The price per shared plaquette is the worst case of Corollary V1 at zero field: it is a sup over exteriors. (iv) Order one needs "exterior-uniform or annealed responses of blocks larger than the correlation length" ((BC-ord1), OPEN there).
- U(1) test of that method (READ blockcrit L293-311). Theorem U: Villain U(1) at beta at least 2^14 fails (BC) for every block shape "at the coefficient step". Proposition GFF: the massless Gaussian field has exactly zero margin for every block family; the margin is positive iff m is above 0. "So (BC) sees the mass exactly."
- The flux half in layer form holds to 2/3 (READ seed23 L415-423) by a background-uniform one-flip ratio bound; the glue half for 1/3 to 2/3 is OPEN there (L427-428).

What Step 2 fixes for this note (ARGUED from the READ lines).
1. Every proved seed in the lane proves the full S, never S_ev alone. No proof in the lane uses the even projection. So "GLUE separately" has no proved instance beyond the full-seed range (beta below 0.3609).
2. The strong-coupling proofs are comparisons of two tori through a contraction in the worst-case chord metric. They stop near 1/3 for a counting reason (12 partners times 1/4) and near 0.775 for a spectral reason; both are worst-case single-site statements. Neither is specific to the even sector.
3. The massless Gaussian has zero margin in every block criterion. So a block criterion is exactly a mass detector, and for U(1) the missing mass is the photon, an EVEN-sector object. The T-U1 failure of any glue proof must therefore sit in the even sector itself.

## Step 3. Row 863's B1 and what the lane already says on the glue half (READ)

Row 863 (READ D/library/gap-crux-skeleton-max.md L104-136, L186-244; check row 879, D/library/gap-crux-skeleton-check-astra.md L55, L262, L386-400).
- I1 (slice chain): P f = Omega^(-1) T(Omega f)/lambda_0 is a self-adjoint Markov operator on L^2(nu), nu = Omega^2 dU, spectrum {r_i = lambda_i/lambda_0}.
- I2: S(2s; B) = chi^2(law of (slice 0, slice s) || nu x nu), in the stationary (infinite-time) chain. HOLDS (check L235).
- B1 (HOLDS, check L55): the two-slice law of the infinite-time measure is pi(dU, dU') = a(U) k_orb(U, U') a(U') dU dU', a = e^(-V/2) Omega/sqrt(lambda_0); it is the static Schroedinger bridge from nu to nu with reference kernel k_orb. The spectrum of P is a function of (k_orb, nu); the magnetic coupling enters only through nu.
- B2 (HOLDS AFTER CORRECTION): Hopf: r_1 at most tanh(3 beta_t |B|); extensive; holds for every compact group.
- B3 (HOLDS AFTER CORRECTION, check L262, L327): 1 - r_1 = inf E_pi[(f(U') - f(U))^2]/(2 Var_nu f); (INC). Gaussian check: for nu = N(0, sigma) and a Gaussian kernel of variance eps the bridge has r about 1 - eps/(2 sigma): "the gap is small exactly when the vacuum has a collective coordinate of large equal-time variance"; the photon has sigma(k) = 1/(2|k|), unbounded.
- Check 879's correction (L386-400): the finite-ring two-slice law is NOT the bridge of B1; keep the ground-state (infinite-time) setting. The corrected proposal is the lane's (M5-G) with a separate state count (M5-H).
- Attack 2 there (4.4): Bakry-Emery on nu needs Hess(-2 log Omega) at least -(1/2 - kappa) pointwise: "STOP 1. No pointwise information on Hess log Omega"; the same demand on the 4D action fails beyond beta about 0.1. "STOP 2. A pointwise curvature bound is false in the window; an averaged one is the problem itself."
- Row 863's split of the tests (READ L132): "U(1) fails it and Q_8, 2T pass it at large beta (they are gapped in the even sector); the flux part W-fl is where Q_8 and 2T fail. So the two fact tests separate the two parts: the thermal part needs the non-abelian input, the flux part needs the continuity input."

The lane's earlier exact form of the glue half (READ D/library/gap-means-astra.md L616-650): two estimates on the infinite-time ground-state law, centre-even gauge-invariant functions, fixed physical time tau:
  (M5-G) (1/2) int pi(dx) P(x, dy) |f(x) - f(y)|^2 at least c Var_pi(f), with one c, tau for all fine cutoffs and large cubes;
  (M5-H) Tr_ev e^(-t H) at most exp{C [1 + (R/t)^3]} for tau at most t at most R/2 (a thermal state count).
"Writing (M5-G) itself is a variational restatement of the missing gap, not a discovery of that producer" (L640-642).

Remark 2.A of D/library/gap-crux-fp.md (READ L119-124). Tr(T^a P_0) = (1/8) sum of Z[k] over the 8 temporal twists. The exchange of directions 1 and 2 maps planes (1,3), (1,4) to (2,3), (2,4), which are not in the sum, so Lemma X (which needs W(a, b) = W(b, a)) does not apply to the centre-even trace. The sum over all 64 twists is symmetric; from any time direction it is 8 times the trace of the direct sum over the 8 magnetic twists m of T^(m) P_0. In a confining phase that direct sum has eight nearly equal top eigenvalues (thermal sum near 7). "A gap of the glue half alone needs a different step from one size to all sizes. OPEN."

Fact tests (READ through row 892 Step 2b, L87-100; the rows themselves not re-read). 786: Villain U(1) at beta at least 2^14 has gauge-invariant Langevin gap tending to 0 with the torus. 838: Q_8 and 2T bind at order one; Haar moments first differ from SU(2) at degree 4 (Q_8), 6 (2T). 839: worst-case layer twist bounds stop at 4 G_3 = 1.0109. 843: the spin-5/2 filter separates SU(2) from Q_8, 2T, U(1). 845: (AN1) is the worst case in disguise.

State of knowledge entering Step 4 (ARGUED from Steps 1-3).
- The lane has the glue half in three equivalent-looking forms: GLUE-FP (one number of one box), W-gap + W-hs (row 863), (M5-G) + (M5-H) (the earlier lane). None has a proof beyond beta 0.3609, and there only as part of the full seed.
- Nobody has yet decided: (a) is GLUE-FP separable from the flux half; (b) does it carry confinement content; (c) what is the weakest crux lemma for it. These are Steps 4 and 5.

## Step 4. The crux lemma, exact, in four faces

Setting. Torus (a, b, b, b), directions (1, 2, 3, 4), b at least 24 a, a at least 3. Frame 1: time is direction 1; box B = b^3; T = T_(B,0); flips C_2, C_3, C_4; Z[k](t) = Tr(T^t C^k) for k in Z_2^3 (the temporal twists; Z[k] at most Z[0], READ row 892 L329); P_0 = (1/8) sum_k C^k; Z_0(t) = Tr(T^t P_0) = (1/8) sum_k Z[k](t). Even eigenvalues lambda_0 > lambda_1^+ >= lambda_2^+ >= ... >= 0 (T is positive; the vacuum is even and simple). r_i = lambda_i^+/lambda_0. S_ev(t) = sum over i >= 1 of r_i^t.

**Crux lemma (GLUE-FP)_sigma, exact.** There are physical sizes ell_t and ell_s at least 24 ell_t and an index K_0 such that, for every first-passage datum (K, beta) with K at least K_0, with a = ell_t/a_K and b = ell_s/a_K (integers):
  S_ev(a; b^3) at most sigma.
Levels: sigma = 1/10 (Corollary O1 (b), with Q_0 at most 1/20); sigma = 160^(-16) together with S_ev(a/2; b^3) at most 1 (Proposition W, with (WALL)_40). It is a statement on the bare Wilson measure (Step 2). It reads the eight temporally twisted tori.

**Lemma G1 (spectral face: gap times count; PROVED).** For integers 0 < t_0 < a:
  r_1^a  at most  S_ev(a)  at most  r_1^(a - t_0) S_ev(t_0)  at most  r_1^(a - t_0) S(t_0).
Also S_ev(t + t') at most S_ev(t) S_ev(t').
Proof. r_i^a = r_i^(a - t_0) r_i^(t_0) at most r_1^(a - t_0) r_i^(t_0) for i >= 1; sum. S_ev at most S (SPLIT). The last line: sum_i r_i^(t + t') at most (sum_i r_i^t)(sum_i r_i^t'), all terms nonnegative. QED
Reading. GLUE-FP is an even gap of the cube (r_1 small to the power a) and a count of even states at a shorter time. The count may be the full count S(t_0), which is an untwisted number.

**Lemma G2 (free-energy face; PROVED).** For every integer s >= 1 put D_ev(a, s) = log Z_0(a) + log Z_0(s) - log Z_0(a + s). Then
  log(1 + S_ev(a))  at most  D_ev(a, s)  at most  log(1 + S_ev(a)) + log(1 + S_ev(s)).
Also 1 + S_ev(a) at most Z_0(a) Z(s)/Z(a + s) with the untwisted Z = Z[0].
Proof. Z_0(t) = lambda_0^t (1 + S_ev(t)). So D_ev = log[(1 + S_ev(a))(1 + S_ev(s))/(1 + S_ev(a + s))]. Use 0 at most S_ev(a + s) at most S_ev(s). For the last claim: Tr T^(a + s) at most lambda_0^a Tr T^s, so lambda_0^a at least Z(a + s)/Z(s). QED
Reading. GLUE-FP at level sigma follows from (Z_0(a))^2 at most (1 + sigma) Z_0(2a), and implies (Z_0(a))^2 at most (1 + sigma)^2 Z_0(2a). It is a near-multiplicativity in the time of the average of the eight twisted partition functions. Only the numerator Z_0(a) needs the twists.

**Lemma G3 (mixing face: the centre-quotient chain; PROVED, given row 863's I1, I2).** Let P = Omega^(-1) T Omega/lambda_0 on L^2(nu), nu = Omega^2 dU. P commutes with the C_i, and nu is C_i-invariant. So P maps centre-blind functions to centre-blind functions: it defines a reversible Markov chain on the centre orbits (the quotient of the slice configurations by gauge transformations and by Z_2^3), with stationary law nu-bar. Let pbar_s(x, y) = (1/8) sum_k p_s(x, C^k y), p_s the density of P^s with respect to nu. Then for every integer s >= 1:
  S_ev(2s) = integral of (pbar_s(x, y) - 1)^2 nu(dx) nu(dy) = E_(x ~ nu)[ chi^2( Pbar^s(x, .) || nu-bar ) ].
Proof. C_i Omega = Omega (the vacuum is even), C_i commutes with T and preserves Haar measure; so P C_i = C_i P and nu is invariant. P_0 is then the orthogonal projection of L^2(nu) on the centre-blind functions and P^s P_0 has the kernel pbar_s with respect to nu. It is self-adjoint with eigenvalues r_i^s (i >= 0) on the even eigenvectors and 0 elsewhere. Its Hilbert-Schmidt norm squared is the integral of pbar_s^2 and equals sum_(i >= 0) r_i^(2s) = 1 + S_ev(2s). The integral of pbar_s is 1 (P^s 1 = 1). QED
Reading. GLUE-FP at time a = 2s: started from a nu-typical slice, the chain of centre orbits is within chi-square sigma of stationarity after a/2 steps, on average over the start. In form the glue half is exactly a mixing statement for the centre-blind chain. No odd function enters it.

**Lemma G4 (Casimir face, time along a long side; PROVED from (TM-tw) and the permutation symmetry, READ D/library/gap-es1-opus.md L32).** Frame 2: time is direction 2; box A = (a, b, b) in directions (1, 3, 4). For m = (m_3, m_4) in Z_2^2 let T'_m be the transfer operator of A with spatial twist m_3 in the plane (1, 3) and m_4 in the plane (1, 4); C'_1 the flip of direction 1; P'_+ = (1 + C'_1)/2; tau_0 = lambda_0(A) (every eigenvalue of T'_m is at most tau_0). Put sigma_m = Tr(T'_m^b P'_+)/tau_0^b and Cas(a, b) = b e(a, b, b) - a e(b, b, b), e = log lambda_0. Then
  1 + S_ev(a; b^3) = exp(Cas(a, b)) (1/4) sum over m of sigma_m ,   sigma_0 at least 1,
  Cas(a, b) at most log 4 + log(1 + S_ev(a; b^3)).
Proof. The class k_2 v_12 + k_3 v_13 + k_4 v_14 is, seen from frame 2, the temporal twist k_2 (flip C'_1) and the spatial twist (k_3, k_4). So Z[k](a; b^3) = Tr(T'_(k_3,k_4)^b C'_1^(k_2)). Average over k: Z_0(a; b^3) = (1/4) sum_m Tr(T'_m^b P'_+). Divide by lambda_0(b^3)^a = tau_0^b exp(-Cas). The vacuum of T'_0 is C'_1-even, so sigma_0 at least 1; every sigma_m is at least 0. QED
Reading. Seen along a long side, GLUE-FP says three things at once: (i) the vacuum energy of the box with one short side a exceeds the bulk value by at most about log(1.1)/b (no Casimir energy at the length a); (ii) the C'_1-even thermal sums of that box at the long time b are small; (iii) the twisted boxes add nothing. Part (i) is the content at the scale a; parts (ii), (iii) are at the time b at least 24 a.

Fact-test profile of (GLUE-FP) as a target (ARGUED; exact statements in Step 5).
- U(1) Coulomb: fails. Face G4 (i): the photon Casimir energy; log(1 + S_ev) is about (pi^2/45) (b/a)^3 = 3000 at b = 24 a (GUIDE value; READ the massless ceiling of gap-seed-shape.md L223-243 for the scalar: exp(0.11 r^3)).
- Z_2 at large beta, frozen Q_8 and 2T: pass (gapped and deconfined, ARGUED). In face G4 they pass with sigma_0 near 4 and the other sigma_m near 0: the average is still 1.
- SU(2) itself at a short physical time a (temperature 1/a above deconfinement): fails with the gluon gas, log(1 + S) of order (pi^2/15) (b/a)^3 (GUIDE). So a proof must use the physical size of a. No scale-free argument can give it.
- No worst case in the statement: G3 is an average over nu.

## Step 5. Structure: is the glue half confinement, or mixing? Does it separate from the flux half?

### 5.1 Proposition SEP (the two halves are independent in the class; PROVED given the named inputs)

The class is that of D/library/gap-es1-opus.md L32 (positive trace-class twisted transfer operators commuting with the flips, Z^(e+m)(t, B) = Tr(T_(B,m)^t C^e), permutation symmetry, simple even top eigenvalue).
(a) Products. Let M_1 be a model of the class and M_2 a symmetric model with positive trace-class transfer operators and simple top eigenvalue, made a member of the class with trivial flips and twists (C = 1, T_(B,m) = T_B). Then M_1 x M_2 (transfer operators T_1 tensor T_2, flips C tensor 1) is in the class as far as the listed properties go (all are multiplicative; I did not re-check the crossing Lemma R1 for products), and on every box
  1 + S_ev(M_1 x M_2) = (1 + S_ev(M_1)) (1 + S(M_2)),   q_i(M_1 x M_2) = q_i(M_1).
Proof. Tr((T_1 tensor T_2)^t (P_0 tensor 1)) = Z_0(M_1) Z(M_2); the top eigenvalue is the product; Tr((T_1 tensor T_2)^t ((1 - C_i)/2 tensor 1))/Tr((T_1 tensor T_2)^t) = q_i(M_1). QED
(b) Flux half true, glue half false. M_1 = Wilson SU(2) at beta below 0.3609 on a seed box (full seed PROVED in the lane: Corollary SEED of row 836, checked row 841), so Q_0(M_1) is small. M_2 = n copies of any model with S above 0 on that box; (1 + S(M_2))^n is as large as one likes. For a failure at every size take M_2 = Coulomb U(1) (gapless; row 786 for Villain; RECALLED, not re-read).
(c) Glue half true, flux half false. Z_2 gauge theory at large beta: gapped, S_ev small, electric sectors degenerate, Q_0 near 1/2 (ARGUED here; the lane holds the Peierls range as theorem-grade, row 892 L292, not re-read).
Consequence. No theorem that uses only the class (as Theorems S, SH, R do) can derive GLUE-FP from any flux statement, or (CORE) from GLUE-FP. This is the exact form of row 892's "no flux node supplies GLUE".

Fact-test remark on (b). Inside pure SU(2)-valued gauge theories the role of M_2 is played by a soft scalar glueball: for the mixed weight exp(beta_F x + beta_A (4 x^2 - 1)/3) the first-order line ends at a critical point where the plaquette-energy correlation length diverges while the string tension stays finite (RECALLED lattice knowledge, GUIDE; the lane's test K7, READ D/library/gap-brainstorm2-max.md L465). So GLUE is false at order one for a reflection-positive local action with the same group, the same symmetries and the same flux half. Consequence (ARGUED): no proof of GLUE at order one can use only symmetry, positivity, locality and the group; it must be quantitative in the action.

### 5.2 Remark UNTW (untwisted free energies never isolate the glue half; PROVED)

The untwisted partition functions Z(t; B), t >= 1, are the power sums Tr T^t. They determine the eigenvalues of T with multiplicity and nothing on their parity. A model and its copy with the flips declared trivial have the same untwisted Z on all tori and different S_ev (S_ev becomes S). So every bound on S_ev that reads only untwisted tori is a bound on S. By Lemma SPLIT, 1 + S = (1 + S_ev)/(1 - U) with U = 1 - Z_0/Z in [Q_0, 3 Q_0].
Consequences. (i) Every proved seed in the lane (D-shape, Step 2) bounds 2F(a) - F(2a) on untwisted tori, so it proves both halves or nothing. That is why "GLUE alone" has no proved instance. (ii) The account runs on untwisted tori only (READ finish line L160). On the account's objects the glue half is not a separate statement: the only one-box number there is S itself. GLUE-FP proper needs the eight temporally twisted tori (face G2) or a direct mixing estimate for centre-blind functions of the untwisted measure (face G3 gives the gap part from untwisted correlations; the count part can be the full count S(t_0), Lemma G1).
(iii) A split that does live on untwisted objects (PROVED, Lemma G1): S_ev(a) at most r_1^(a - t_0) S(t_0). The even gap r_1 is the decay rate of centre-blind correlations of the untwisted infinite-time measure. S(t_0) is an untwisted free-energy number at a shorter time. Neither factor needs a twist. This is the form in which the glue half separates on the account's objects: (GAP_ev) the even gap of one cube, and (COUNT) a crude full count.

### 5.3 Both halves live on one compactified box (ARGUED from Lemma G4 and row 892's face F2, both PROVED)

Look along a long side. The box is A = (a, b, b): the theory on a circle of length a.
- Flux half (row 892 F2): q is theta_P^b up to thermal sums, theta_P the top C'_1-odd eigenvalue ratio of A. It is the mass of the winding (Polyakov) line of the short circle: E_P at least about 3/b.
- Glue half (Lemma G4): it is the Casimir energy of the short circle, Cas(a, b) at most about log 1.1, with the even and twisted traces of A at the long time b.
So in thermal words, at temperature 1/a on the volume b^3: the flux half says the winding line is disordered (confined phase, any small mass); the glue half says the pressure is at most log(1.1)/(b/a)^3 = 6.9e-6 in units of the temperature to the fourth power at b = 24 a (GUIDE arithmetic).

| Model on the box (a, b^3), b = 24 a | winding line of the short circle | pressure / Casimir energy | flux half | glue half |
|---|---|---|---|---|
| SU(2), a above about 14/m (GUIDE) | massive | exponentially small | holds | holds |
| SU(2), 1/T_c below a below about 14/m (GUIDE) | massive | glueball gas, not yet small | holds | FAILS |
| SU(2), a below 1/T_c (GUIDE) | ordered | gluon gas, about (pi^2/15)(b/a)^3 in the exponent | fails | fails |
| U(1) Coulomb | no small weight (row 878, ARGUED there) | photon gas, about (pi^2/45)(b/a)^3 | fails | fails |
| Z_2 large beta, frozen Q_8, 2T | ordered | exponentially small | fails | holds |
| mixed action at its critical end point (K7, GUIDE) | massive | soft scalar: not small at any a | holds | fails |
| a finite group at its freezing point (first order, GUIDE) | two phases | two even vacua: S_ev at least about 1 | fails | fails |

All four combinations occur. The second row is the important one for SU(2) itself: there is a window of sizes where the flux half already holds and the glue half does not. The glue half is the stronger demand on the size of the box (GUIDE: it needs a above about 3.8/sqrt(sigma) against 1.4/sqrt(sigma), with m = 3.7 sqrt(sigma), T_c = 0.7 sqrt(sigma), recalled numbers that decide nothing).

### 5.4 The decision

1. In form, GLUE-FP is a pure even-sector mixing statement. Exactly: it is the chi-square mixing of the chain of centre orbits (Lemma G3). No odd function and no twist of the flux half enters its statement.
2. It carries no centre-flux confinement content. PROVED in the class: it holds for a deconfined gapped model and fails for a confining model with a soft neutral mode (Proposition SEP). It is the half that survives for a group with trivial centre, where the flux half is empty.
3. It carries the thermodynamic content: no gluon gas at temperature 1/a (no Casimir energy at the length a, Lemma G4). For SU(2) this is the mass gap itself at one size. It is the half that U(1) fails (the photon). T-FIN does not bind it inside the window (Q_8 and 2T are frozen there and pass it); T-FIN binds it only through the cutoff: a finite group fails GLUE at its own freezing point, so a cutoff-uniform proof must use the Lie group in the ultraviolet, where the account already does (ARGUED).
4. Separation. As statements the two halves separate completely (Proposition SEP). As proofs they have never been separated: every proved seed reads untwisted tori and so proves S (Remark UNTW). On the account's objects the separable form is Lemma G1: (GAP_ev) times (COUNT). And every consumer in the lane needs a flux input beside GLUE: (CORE) for Theorem SH; the heavy/light dichotomy of the sixteen crossed sectors for (ES) (READ D/library/gap-es1-opus.md Corollary V1, L78-82). No consumer takes GLUE alone (READ gap-crux-fp.md Remark 2.A (d), OPEN there).
5. Order of the halves. Proved implications between them run one way only and need a third input: GLUE with a kurtosis floor or (WALL) gives (CORE) (row 892, Propositions K, W). No statement in the lane gives GLUE from flux, and Proposition SEP (b) shows none can inside the class. So GLUE is upstream: it is the part of the seed that is the mass gap; the flux half is the part that says the gapped phase is the confining one.

## Step 6. Attack A: the even gap through the bridge and Poincare forms. Where it stops

### 6.1 Lemma G5 (GLUE-FP from one even gap and one crude count; PROVED given Lemma E', READ D/library/gap-seed-shape.md L60-70)

Let a be even, a/2 at least 3, b at least a. Put m_ev = -log r_1(b^3) (the even gap of the cube b^3) and G_0(t) = g(t; (2t)^3) = log(1 + S(t; (2t)^3)) (a full, untwisted count). Then
  S_ev(a; b^3)  at most  exp[ (2b/a)^3 G_0(a/2) - m_ev a/2 ].
At b = 24 a: (2b/a)^3 = 110592. So (GLUE-FP)_sigma follows from the pair
  (GAP_ev) m_ev((24a)^3) a at least 2 [110592 G + log(1/sigma)],   (COUNT) G_0(a/2) at most G.
Proof. Lemma G1 with t_0 = a/2: S_ev(a; b^3) at most r_1^(a/2) S(a/2; b^3). Lemma E' (h at least y above t at least 3: g(t; B^h) at most (h/(y - t)) g(t; B)) in the three directions from the cube (2t)^3 to b^3, with t = a/2, y = a: g(a/2; b^3) at most (b/(a/2))^3 g(a/2; a^3). And S at most e^g. QED
Reading. (COUNT) may be any finite number, uniform in the cutoff: it says only that the pressure-times-volume of the cube a^3 at the time a/2 is bounded. A crude G costs size, not truth (GUIDE: with G = 6, about the free gluon gas, m_ev a at least 1.33e6). (GAP_ev) is the mass gap of local observables on one cube (Step 7, Lemma LOC). Both are untwisted statements.
Fact tests. U(1) Coulomb: (COUNT) holds (a photon gas has a finite G); (GAP_ev) fails: m_ev is about 2 pi/b, so m_ev a is about 2 pi/24, fixed. Z_2 at large beta, frozen Q_8, 2T: (GAP_ev) holds; (COUNT) with the full count holds with G about log 8 (ARGUED). The U(1) failure sits in (GAP_ev), in the even sector, as Step 2 item 3 required.

### 6.2 Lemma CS (the Casimir term has a sign; PROVED from Lemma A, READ gap-seed-shape.md L53)

For all c, d and 3 at most x at most x': e(x, c, d)/x at least e(x', c, d)/x'. So Cas(a, b) at least 0 for a at most b, and with Lemma G4:
  1/4 at most (1/4) sum_m sigma_m at most 1 + S_ev(a; b^3),   0 at most Cas(a, b) at most log(1 + S_ev) + log 4.
Proof. Z(x, y, c, d) = Tr S^x with S the transfer operator of the box (y, c, d) in the direction of length x. Lemma A (a): x -> (Tr S^x)^(1/x) is non-increasing. So (1/x) log Z(x, y, c, d) at least (1/x') log Z(x', y, c, d) for every y. Divide by y and let y grow: (1/y) log Z(x, y, c, d) tends to e(x, c, d). QED
Reading (ARGUED). Every exact inequality of the class points one way: S at least 0, S_ev at least 0, kappa at least 0, Cas at least 0, e(x)/x non-increasing, Z(2t) at most Z(t)^2. The glue half is the reverse inequality with a small defect: Cas at most log 1.1, that is e(b, b, b)/b at least e(a, b, b)/a - log(1.1)/(a b). The direction looks variational (a lower bound on the top eigenvalue of the cube). It is not: the comparison term e(a, b, b)/a is itself a top eigenvalue, and no trial vector of the cube reproduces it to the accuracy 1/(a b) on a b^3 sites. Inside the class a reverse inequality with defect comes only from a seed at a smaller scale (Theorem SH) or from a contraction estimate.

### 6.3 The even D-shape (PROVED given the D-shape, READ D/library/gap-seed23-opus.md L77-80)

Let mu_(ev,a,s) be the mixture of the eight temporally twisted measures of the torus (a, b^3) at coupling s with weights Z[k]/sum Z[k] (a probability measure, since every Z[k] is positive), u_(ev,a)(s) its mean plaquette, twisted plaquettes counted with their sign, and u_inf(s) the mean plaquette of the infinite-time measure on the box b^3. Then
  log(1 + S_ev(a; b^3; beta)) = 6 a b^3 integral_0^beta [u_(ev,a)(s) - u_inf(s)] ds.
Proof. d/ds log Z_0(a) = sum over k of (Z[k]/sum Z[k]) d/ds log Z[k] = 6 a b^3 (u_(ev,a) - 1) for the weight exp(-s sum (1 - x_p)); d/ds (a log lambda_0) = lim over t of (a/t) d/ds log Z(t) = 6 a b^3 (u_inf - 1) (log Z(t)/t converges to e with convex terms, so derivatives converge where e is differentiable; the identity holds in integrated form). At s = 0 both sides vanish (T is then the projection on constants). QED
Reading. The glue half along a coupling path is: the mean plaquette of the twist-averaged short torus equals the infinite-time mean to within log(1.1)/(6 a b^3) = 1.1e-6/a^4 at b = 24 a, in the integral over all couplings below beta. The proved range of any such comparison is s below 0.3609 (Step 2). From 0.36 up, at every s, nothing is proved, although below about s = 2 the correlation length is under one lattice spacing (GUIDE).

### 6.4 The attack on (GAP_ev) in bridge form, and its four stops

Target (B3 of row 863 restricted to the even sector): for every centre-blind f with nu(f) = 0 on the cube: Var_nu(f) at most C E_pi[(f(U') - f(U))^2], with 1/(2C) = 1 - e^(-m_ev). By B1 the pair law pi is the bridge of (k_orb, nu).

Stop 1 (curvature; READ row 863 4.4). Bakry-Emery on nu needs a pointwise bound on Hess log Omega. None is known. The same demand on the four-dimensional action fails above beta about 0.1. Evenness gives nothing here: curvature is local and every local function is even (Lemma LOC, Step 7).

Stop 2 (comparison with the free kernel; PROVED limit). P(U, dU') = K(U, U') g(U') dU'/(K g)(U), g = e^(-V/2) Omega (I1). The even gap of the free kernel K is known exactly (row 863 A2: it is -4 log u_(1/2)(beta_t) on gauge-invariant functions). Any comparison of the Dirichlet forms of P and K through the oscillation of g (Holley-Stroock), or of cross-ratios (Hopf, B2), has an extensive exponent: log g is a sum over the box. So it gives m_ev at least exp(-c |B|) and nothing at the seed size. PROVED as stated in B2; it holds for U(1), so it must be extensive.

Stop 3 (the slice law is not a local Gibbs measure). To use the product form of K link by link one needs the conditional laws of nu, that is, the locality of log Omega. That log Omega has exponentially decaying interactions is the gap itself in another form (ARGUED). The four-dimensional measure is local, so a local attack must run there.

Stop 4 (annealed L^2 conditions are the claim; Lemma MC, PROVED, standard). In the stationary chain of P the maximal correlation coefficient between the sigma-algebras of the slices at times at most 0 and at times at least w is exactly r_1^w (even functions: the even r_1).
Proof. For F past-measurable and G future-measurable with mean 0, the Markov property gives E[F G] = <fhat, P^w ghat>_nu with fhat(x) = E[F | x_0 = x], ghat(y) = E[G | x_w = y], which have mean 0 and norms at most those of F, G. So |E[F G]| at most r_1^w ||F|| ||G||, with equality for the first eigenfunction at times 0 and w. QED
So the L^2(mu) decoupling of two slabs, which is what a quasi-factorization of the variance (a block-dynamics gap with exteriors averaged under the true measure) would take as its input, is the statement r_1^w small itself. A non-circular input must be a finite-block statement. The finite-block statements with a theorem behind them are worst-case in the exterior (Step 7). That is where Attack A stops.

What Attack A gained. Lemma G5 (the exact two-estimate form on untwisted objects, with constants). Lemma CS (the sign structure). The even D-shape. Lemma MC (why an annealed slab condition is not a reduction). Nothing at order one.

## Step 7. Attack B: block criteria in the even sector; the strong-coupling proofs; where it stops

### 7.1 Lemma LOC (every local gauge-invariant function is centre-blind; PROVED)

Let R be a set of links of the slice b^3 and i a direction such that, for some j, no link of R crosses the plane between x_i = j and x_i = j + 1. Let f be a gauge-invariant function that depends only on the links of R. Then f(C_i U) = f(U).
Proof. C_i multiplies by -1 the links that cross one fixed plane, say between x_i = 0 and x_i = 1. Let h_x = -1 for 1 at most x_i at most j and h_x = +1 otherwise. The gauge transformation h multiplies by -1 exactly the links that cross the plane (0, 1) or the plane (j, j + 1). On R it acts as C_i. f is gauge-invariant and reads only R. QED
Consequences.
(i) Every gauge-invariant function supported in a region that does not wrap the torus lies in the even sector H_0. Conversely (ARGUED: contractible Wilson loops separate generic points of the quotient by gauge and by the flat Z_2 fields, because the centralizer of a generic local holonomy group is the centre) such functions generate H_0. So the even gap is the decay rate of the truncated correlations of local observables. The odd sectors contain only winding observables.
(ii) So GLUE is the bulk statement (the mass gap of the local algebra, at one size), and the flux half is the part of the seed that the torus method needs and a bulk gap does not (in agreement with gap-crux-fp.md, row a2 of its table, READ L114).
(iii) "A block criterion in the even sector" is the same thing as a block criterion. Conditional laws of finite blocks and local observables never see the flips. In the strong-coupling proofs the flux sectors enter only at the last step, where two tori are compared through untwisted free energies (Remark UNTW). So evenness cannot improve any local constant: the counts 18, 14, 12 partners, the constant 1/4, Lemma AVG's ceiling 1/3, the star range 0.3609 and Proposition CEIL's 0.775 are the same for the glue half as for the full seed (READ Step 2; PROVED there).

### 7.2 Proposition FIB (an averaged block condition in L^2 is the worst case; PROVED, standard direct-integral fact)

Let B be a finite block of links of the torus, mu the Wilson measure, and A a bounded self-adjoint operator on L^2(mu) that commutes with multiplication by every bounded function of the links outside B. (Every polynomial in the conditional expectations E_(B') given the exterior of sub-blocks B' of B is such an operator: block dynamics, heat-bath sweeps of B.) Then A is the direct integral of its fibres A^tau on L^2(mu_B^tau) over the exterior configurations tau, the norm of A is the essential supremum of the fibre norms, and the bottom of the spectrum of A on the complement of the fibrewise kernel is the essential infimum of the fibre gaps. The Wilson measure has full support and the fibre data are continuous in tau, so essential infimum means infimum over ALL exteriors.
Proof. L^2(mu) is the direct integral of the spaces L^2(mu_B^tau) with respect to the exterior marginal (disintegration). An operator commuting with the diagonal algebra is decomposable (von Neumann), and norms and spectra of decomposable operators are essential suprema and unions over fibres. QED
Consequence (ARGUED). Local-to-global theorems for spectral gaps (block dynamics recursions, finite-size criteria of the Knabe and martingale type, Dobrushin-Shlosman conditions) take a finite-block input. By Proposition FIB an L^2(mu) version of that input is not weaker than the exterior-uniform one. This is the L^2 counterpart of the lane's "(AN1) is the worst case in disguise" (row 845, checked, Wasserstein form). With Lemma MC (Step 6): an averaged condition is either the worst case (finite blocks) or the claim itself (slabs).

### 7.3 Why the strong-coupling proofs stop near 1/3, and what that says at order one (READ Step 2, then ARGUED)

- They are exterior-uniform single-link (or small-block) contractions. The constant 1/4 per shared plaquette is attained at zero staple field. At small beta the zero field is the typical case, so the constant is sharp there; what is lost is the incoherence of the 12 partner influences, which a row sum adds in absolute value.
- At order one small blocks fail for a real reason, not a technical one: with a smooth exterior a small block is nearly Gaussian and its optimal coefficient exceeds 1 (READ blockcrit L287: the star tends to 2). Only blocks larger than the correlation length can pass, and there the exterior-uniform coefficient is a finite but large computation (READ (BC-ord1), blockcrit L291; OPEN). By the owner's rule a numeric evaluation of it cannot discharge anything.
- Fact tests of this route. U(1) Coulomb fails it at the coefficient for every block (READ Theorem U; Proposition GFF: zero margin for a massless Gaussian). Z_2 at large beta and frozen Q_8, 2T pass block criteria on gauge-invariant functions (ARGUED: dilute vortex sheets); this is correct, since they pass GLUE (Step 5). SU(2) at a short physical size: a block criterion is a bulk statement and does not see the box; the failure of GLUE-FP at short a then sits in the size condition "block range at most a" (ARGUED).

### 7.4 Lemma UP (a count climbs in scale only with a loss; PROVED from Lemma E' and (T), READ gap-seed-shape.md L51, L70)

For t at least 3: G_0(2t) at most 1728 G_0(t), with G_0(t) = g(t; (2t)^3).
Proof. Lemma E' at time 2t from the cube (3t)^3 to (4t)^3: g(2t; (4t)^3) at most (4t/(3t - 2t))^3 g(2t; (3t)^3) = 64 g(2t; (3t)^3). g is non-increasing in the time: g(2t; (3t)^3) at most g(t; (3t)^3). Lemma E' at time t from (2t)^3 to (3t)^3: at most 27 g(t; (2t)^3). QED
Reading. Exact inequalities carry a bounded count from one scale to the next only with a fixed factor, so to a power of the scale. (COUNT) in Lemma G5 is needed at the half-time of the seed box itself. It does not follow from a count at the first-passage scale. A gain per doubling needs a gap: for the full sums the full gap (flux included, where Lemma E' is available), for the even sums the even gap (where no enlarging lemma is known, Remark 2.A). This is the exact place where the two halves cannot be separated in a proof by recursion: the enlarging step reads untwisted tori.

### 7.5 What Attack B leaves (ARGUED)

A proof of (GAP_ev) at order one must be one of the following, or something not listed (the list is not closed):
(i) an exterior-uniform statement on blocks larger than the correlation length ((BC-ord1)); finite, not by hand at present;
(ii) a global exact step that yields a reverse inequality with defect (Lemma CS shows the class has none; Theorem SH needs a seed);
(iii) the account's renormalization continued from first passage down to an effective coupling below 0.3609, where Theorem ST applies by hand; this needs control of the effective action across the window (READ finish line L147-151: not available);
(iv) a new inequality special to the Wilson weight on SU(2) (it must fail for the mixed action at its critical end point, K7).
None is supplied here.

## Step 7b. Attack C: the transport face. The whole even sum moves along the coupling with no count

Attacks A and B are static (one coupling). The proved seeds live at beta below 0.3609. This step carries the even thermal sum from there to the window by one differential condition. Overlap, stated first: for the first level and the magnetic coupling this is row 863's 4.5 (READ Step 3: Feynman-Hellmann and Gronwall; "a restatement, not a reduction"), and the lane's (PATH)/(SHIFT) node. What is added here: the all-level form, which transports the whole sum so that (COUNT) is not needed, and the fact-test profile.

Setting. A fixed box B, bare Wilson coupling s (all plaquettes). T(s) = e^(-s N_s/2) K_s e^(-s N_s/2) is an entire family of positive trace-class operators; on H_0 its nonzero eigenvalues lie on real-analytic branches (Rellich, Kato; standard for a self-adjoint analytic family of compact operators). Along each even branch other than the vacuum put E(s) = log lambda_0(s) - log lambda(s), positive.

  (BETA)_C on [beta_0, beta_1]:  every even branch has  -d log E/ds  at most  C.

**Proposition TR (PROVED, given the analytic branches).** If (BETA)_C holds on [beta_0, beta_1] for the box B, then for every real a with a e^(-C(beta_1 - beta_0)) at least 1:
  S_ev(a; B; beta_1)  at most  S_ev(a e^(-C(beta_1 - beta_0)); B; beta_0).
Proof. Gronwall on each branch: E(beta_1) at least E(beta_0) e^(-C(beta_1 - beta_0)). So e^(-a E(beta_1)) at most e^(-a' E(beta_0)) with a' = a e^(-C(beta_1 - beta_0)). Sum over the branches; the branches list the even spectrum with multiplicity at each s. A real power t at least 1 of the ratios is summable because T is trace class. QED
The same holds for the full sum S with all branches, and then for the seed itself.

Corollary TR1 (ARGUED composition; the strong-coupling inputs are READ, Step 2). Take beta_0 below 0.3609. There the full seed holds at some size, and Theorem SH (i) makes S(n; (2n)^3; beta_0) as small as one likes along n = j^k a_seed (K s_k at most (K s)^(j^k)); Lemma E' carries it to the shape (n, b^3) with the factor (b/n)^3. So for every finite C, (BETA)_C on [beta_0, beta_1] gives (GLUE-FP)_sigma for bare Wilson SU(2) at beta_1, at an explicit size a_1 about n e^(C(beta_1 - beta_0)) with b = 24 a_1, at both levels sigma. No count is needed and no twist is read (the even branches are those of the untwisted T). With (BETA) for all branches it gives the full seed and the flux half too.

Reading (GUIDE; recalled physics, decides nothing). (BETA)_C says: no energy level of the box falls faster than at the logarithmic rate C per unit of beta. 1/C is a lower bound for the lattice beta function read on every level. In the scaling region the true rate is 3 pi^2/11 = 2.69 for every physical level. The average rate between 0.36 and 2.5 is about 1.3 (correlation lengths about 0.1 and 1.5). Any finite C serves: C sets the size, not the truth. In thermal form, with X = log(1 + S_ev): d_s X at most -C a d_a X, that is, the thermal shift of the action is at most C times the thermal energy (in the continuum: the interaction measure is at most the energy density, pressure at least 0).

Fact tests of (BETA)_C on [0.3609, beta_1], beta_1 in the window (ARGUED; transition points RECALLED, GUIDE).
- U(1): fails at its confinement-Coulomb transition near beta 1.01 (a level falls through; in a large box the rate is of the order of the volume). Inside the Coulomb phase the levels of a fixed box hardly move, so (BETA) holds there: the failure is at the transition point, in the even sector. Correct: the path carries a small sum into a phase where it is large.
- Z_2: fails at its first-order point (0.4407). Frozen Q_8 and 2T: fail at their freezing points, 1.15 and 2.15 (READ row 892 L91), both on the path below the window. So in the transport form T-FIN binds the glue half, although in the static form it does not (Step 5): a proof of (BETA) across 1.15 and 2.15 must tell SU(2) from Q_8 and from 2T, that is, it must see Haar moments of degree 4 and 6 (READ row 838 through row 892 L91).
- K7: at a first-order point of the mixed action a level falls at a rate of the order of the volume; at its critical end point the scalar level has no uniform rate. (BETA) fails, as it must.
- No worst case: (BETA) is a statement on eigenvalues of the true operator.
- Cutoff: Proposition TR gives a size that grows like e^(C beta_1). It is uniform in the cutoff only if C is the exact asymptotic rate, with no slack. So this face serves the bare Wilson window (the lane's order-one problem), not first passage by itself. For first passage the static forms of Steps 4 to 6 are the right ones, with the account in the ultraviolet.

Where Attack C stops. (BETA)_C is true exactly when no level collapses on the path. In a finite box it holds with some C (analyticity; the gap of a fixed box never closes, READ B2). The content is the uniformity of C in the volume. I tried three ways to get it:
1. Operator inequalities between the electric part and the generator (the Hamiltonian virial identity, lambda dG/d lambda = 2 lambda Delta N - G for H = K/lambda + lambda N, PROVED by Feynman-Hellmann; G a level gap, Delta N its magnetic energy above the vacuum's). A form bound K at most kappa lambda (H - E_0) + const has a constant that is the concavity defect of the ground energy over a coupling interval, which is extensive (PROVED by the tangent-line computation). So it bounds no single level.
2. Convexity. log lambda_0 is convex in s. log(lambda_0 lambda_1) is the top eigenvalue of the antisymmetric square, whose kernel has both signs in the position basis; no convexity follows. No bound.
3. Monotonicity. G lambda is non-decreasing exactly when Delta N is at least 0 (PROVED from the identity). Asymptotic freedom makes Delta N negative at weak coupling (GUIDE), so the monotone case is false in the window: the gap must fall faster than 1/lambda.
So (BETA) needs the same input as (GAP_ev): control of how the low even levels of a large box move, which is the absence of a critical point on the Wilson axis. This is row 863's verdict on paths, now for the whole even sum.

## Step 8. Final

### 8.0 Corrections and overlaps found after the steps were written

1. Overlap with the lane, Lemma G5. The gap-times-count form of the FULL seed is already in the lane with better constants: Theorem ZD-c (READ D/library/gap-phys-seed.md L311-336, checked row 727): the seed is equivalent to (BDD-Delta) (the Casimir free energy of the symmetric torus stays bounded) with (Z-UNB) (L m(L^3) unbounded), and "one size with L m(L^3) above 256 D_0 + 29.64 is enough". It already splits (Z-UNB) into the zero-flux gap m_0 and the flux levels E_e (L328). Lemma G5 is the even analogue at the SH shape: it needs only the zero-flux part of (Z-UNB), with a count. Its constant 110592 is crude; the lane's proof at the shape r = 2 should give the even analogue with a constant near 1024 D_0 + 4 log(1/sigma) (ARGUED; not written). The lane's reading of the tests agrees with 6.1: "in every comparison model the failing half is (Z-UNB), and (BDD-Delta) holds" (L336).
2. Lemma G4 is the lane's crossing identity (Lemma R1 (a), READ gap-es1-opus.md L60-64) applied at the shape (a, b, b, b), not a new identity. Lemma CS restates Lemma K (b)'s sign for this shape.
3. Proposition SEP (b). A rigorous neutral factor without a gap, inside the class: the compact Gaussian model with windings of gap-seed-shape.md 4.2 (PROVED there, READ L229-241: positive trace-class, simple top eigenvalue, m(L^3) at most 1/(2 R^2 L^3)). It replaces "Coulomb U(1), RECALLED". The crossing Lemma R1 (a) holds for a product with a neutral factor (PROVED: both sides carry the factor Z(M_2) of the same torus, by the permutation symmetry of M_2).
4. Step 7b, way 1. The identity for the best constant (the concavity defect of psi(mu) = inf spec(K + mu N) over [mu, mu kappa/(kappa - 1)]) is PROVED. That this defect is extensive is ARGUED (psi is extensive and strictly concave in general).
5. Step 7b, Corollary TR1. The small sums at beta_0 come on the shape of the table line that applies (r = 4 after the first enlargement); Lemma E' then gives the factor (b/(3n))^3. The conclusion does not change. Proposition TR needs every eigenvalue of T(s) on gauge-invariant functions to be positive for s above 0; this holds because the one-link kernel has all character coefficients positive (READ check 879 L9, from SA 2195-2257).
6. GUIDE run (decides nothing): 2D Ising strips of width 3 to 10 at J = 0.2, 0.44, 0.7 do not refute Lemma CS (e(x)/x non-increasing, Cas at least 0) nor the crossing identity g(a; b) - g(b; a) = b e(a) - a e(b) (agreement to 1e-14). Script: lane895/guide/cs_check.py in the scratchpad; under 100 MB, seconds.
7. Rows 893 (check of row 892) and 894 ((WALL)) have no output at this commit. Lemma SPLIT, Corollary O1 and Proposition W are used as READ, unchecked.

8. GUIDE run for 8.4 (c) (decides nothing): in the electric model the link levels are E_j(s) = -log(I_(2j+1)(s)/I_1(s)); the largest -d log E_j/ds over 2j + 1 from 2 to 39 is 1.139 at s = 0.36, 0.647 at 1.0, 0.449 at 2.0, 0.390 at 2.5, always at j = 1/2 and decreasing in s. Gauge-invariant levels are sums of link levels, so the same bound holds for them (a ratio of sums is at most the largest ratio). So (BETA)_C holds there with C = 1.14 on [0.36, 3], in every volume. Script: lane895/guide/beta_electric.py in the scratchpad.

### 8.1 The crux lemma

**(GLUE-FP)_sigma.** One physical pair ell_s at least 24 ell_t, K_0, and for every first-passage datum with K at least K_0, a = ell_t/a_K, b = ell_s/a_K: S_ev(a; b^3) at most sigma (1/10; or 160^(-16) with S_ev(a/2; b^3) at most 1).
Equal forms (all PROVED equivalences, Step 4): the even spectral sum; near-multiplicativity in time of the average of the eight temporally twisted partition functions (G2); chi-square mixing of the chain of centre orbits after a/2 steps, averaged over the slice law (G3); no Casimir energy at the length a times the twisted even traces of the thin box (G4).
Weakest sufficient pair on untwisted objects (Lemma G5): 
  (Z0) the zero-flux gap of ONE cube: m_ev((24a)^3) a at least 2 [110592 G + log(1/sigma)], and
  (COUNT) g(a/2; a^3) at most G, any finite G uniform in the cutoff.
(Z0) carries the difficulty. By Lemma LOC it is the decay of truncated correlations of local observables across the cube: the bulk mass gap at one size, in units of the inverse side. U(1) Coulomb fails (Z0) (its value stays about 2 pi/24) and passes (COUNT).
Transport form for the bare Wilson window (Proposition TR): (BETA)_C on [beta_0, beta_1] with beta_0 below 0.3609, any finite C uniform in the volume. It needs no count and reads no twist.

### 8.2 The decisions asked for

1. Confinement content or mixing? In form GLUE-FP is a pure even-sector mixing statement (G3), and the even sector is the sector of local observables (LOC). It carries no centre-flux content: it holds for deconfined gapped models and fails for a confining model with a soft neutral mode (Proposition SEP, PROVED in the class). What it carries is thermodynamic: at temperature 1/a there is no gas of light quanta (no Casimir energy at the length a). For SU(2) that is the mass gap itself. In the box seen along a long side, the glue half is the vacuum energy of the circle of length a and the flux half is the mass of its winding line (5.3).
2. Can it be separated from the flux half? As a statement: yes, completely, in both directions (SEP). As a proof: only if the proof is volume-uniform. A zero-flux gap on all large cubes gives the bulk gap of the centre-blind functions with no flux input and no shape theorem (it is (G_ev); Theorem EV-L, READ finish line L109). A one-box number does not: every one-box consumer needs a flux input ((CORE) for Theorem SH, the heavy/light dichotomy for (ES)), the enlarging lemmas read untwisted tori (Lemma UP, Remark 2.A), and untwisted free energies determine S, never S_ev (Remark UNTW). So the flux half is the price of a one-box criterion, not of the bulk gap.
3. Which tests bind it? Statically, at a coupling in the window: U(1) (even sector, the photon) and K7 (a soft scalar at a critical end point). Q_8 and 2T do not bind it there: they are frozen and pass. In the transport form the finite groups do bind it: their freezing points 1.15 and 2.15 lie on the path. No worst case appears in any statement; worst cases appear in every available local method (Proposition FIB).
4. Why the strong-coupling proofs stop near 1/3: a count of partners (12) times a worst-case constant (1/4). It is not a property of either half. Local criteria are automatically even (LOC), so the glue half inherits the ceilings 1/3, 0.3609, 0.775 unchanged, and Villain U(1) fails every block criterion at the coefficient (READ Theorem U).

### 8.3 What is proved here, and what is open

PROVED here (by hand, elementary; checked by no one):
- G1 (gap times count), G2 (free-energy face), G3 (chi-square mixing of the centre-orbit chain), G4 (Casimir face; the lane's crossing identity at this shape).
- Proposition SEP (independence of the halves in the class, by products with a neutral factor) and Remark UNTW.
- Lemma G5 (GLUE-FP from one zero-flux gap and one crude untwisted count, constant 110592 at b = 24 a).
- Lemma CS (e(x)/x non-increasing; Cas at least 0; (1/4) sum of sigma_m at most 1 + S_ev).
- The even D-shape (6.3).
- Lemma MC (maximal correlation of two slabs is r_1^w) and Proposition FIB (an L^2-averaged block condition is the worst case over exteriors); both standard.
- Lemma LOC (local gauge-invariant functions are centre-blind).
- Lemma UP (G_0(2t) at most 1728 G_0(t)).
- Proposition TR (level-wise transport of the whole even sum under (BETA)_C), and the Hamiltonian virial identity with its two consequences (7b).
ARGUED, not proved: the converse in LOC (local functions generate H_0); the fact-test entries for Z_2, Q_8, 2T, K7 and SU(2) at short sizes; Corollary TR1's composition; all thermal readings. GUIDE: every number quoted for SU(2), and the Ising run.
OPEN: (GLUE-FP) at either level; (Z0); (COUNT) at the seed scale; (BETA)_C uniformly in the volume; (BC-ord1). Nothing at order one is proved. No mass gap. No tool for the glue half is named.

Where the real attempt stops, in one place each. Static, slice form: the vacuum functional is not known to be local, and curvature is pointwise false in the window. Static, four-dimensional form: every local-to-global method reads a finite block, and an averaged block condition is the worst case (FIB), which fails for small blocks at order one. Global exact inequalities: all point the wrong way (CS). Transport: the uniformity of C in the volume is the absence of a critical point on the Wilson axis.

### 8.4 Next statements

For first passage (static): (Z0) with (COUNT), in the form of the lane's (Z-UNB), zero-flux part, with (BDD-Delta). A proof lane cannot be queued on it until a means is named. Three bounded items would sharpen it without touching the crux (none is on the critical path by itself):
(a) the even analogue of Theorem ZD at the shape r = 2 with the lane's constants (replaces 110592);
(b) a cross-provider check of G3, G4, SEP, UNTW, G5, CS, MC, FIB, LOC, UP, TR;
(c) (BETA)_C tested on the solvable members: the electric model of row 863 A2 (there -d log E/ds is at most about 1.2 for s above 0.36, from the Bessel ratio; GUIDE arithmetic, not proved here) and two-dimensional Yang-Mills.
For the bare Wilson window (transport): (BETA)_C on [0.3609, 2.6]. It is the one form of the glue half in which all the fact tests bind at named points of the path (U(1) at 1.01, Z_2 at 0.44, Q_8 at 1.15, 2T at 2.15, K7 at its line), so a proposed mechanism can be tested against it step by step.

Limits of this note. No statement here is checked by another model. The lane files were read in bounded ranges; rows 786, 838, 839, 843, 845, 870, 878 were read only through row 892's digest. The Sussman-Alpoge sources were not opened; statements on the account are READ from lane files that cite them (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). Balaban's estimates are not used here. Transition points and all SU(2) sizes are recalled lattice numbers, GUIDE only. The class membership of products was verified for the listed properties and for the crossing identity R1 (a), not for every lemma of the class.

RESULT: Row 895 (Claude Fable 5.2 max, unchecked): PARTIAL, nothing proved at order one and no tool named for the glue half. Decided, with proofs in the class: (GLUE-FP) is in form a pure even-sector mixing statement (chi-square mixing of the chain of centre orbits, Lemma G3) and the even sector is the sector of local observables (Lemma LOC), so the glue half is the bulk mass gap at one size; it carries no centre-flux content and is independent of the flux half in both directions (Proposition SEP), it carries the thermodynamic content (no Casimir energy at the short length, Lemma G4, with a sign, Lemma CS); it separates from the flux half as a statement and in any volume-uniform proof, but not in a one-box proof: untwisted free energies give S and never S_ev (Remark UNTW), counts climb only with loss (Lemma UP), and every one-box consumer needs a flux input. Crux lemma stated exactly with its weakest sufficient pair (Lemma G5): the zero-flux gap of one cube, m_ev((24a)^3) a at least 2[110592 G + log(1/sigma)], with a crude untwisted count g(a/2; a^3) at most G (the even analogue of the lane's (Z-UNB) with (BDD-Delta)); transport form (Proposition TR): (BETA)_C, every even level falls at logarithmic rate at most C on [0.3609, beta_1], carries the whole even sum from the proved range with no count. Tests: U(1) fails in the even sector; Z_2, Q_8, 2T pass statically and fail the transport form at their transition points; K7 fails. The real attempt stops at four named places: nonlocal vacuum functional and pointwise curvature; averaged block conditions are the worst case (Proposition FIB) or the claim (Lemma MC); exact inequalities point one way; uniformity of C in the volume is the absence of a critical point. OPEN: (GLUE-FP), (Z0), (COUNT) at the seed scale, (BETA)_C.
