# Mass gap for 4D SU(2) lattice Yang-Mills: status after FINISH rows 833-911

FINISH row 912. Consolidation note. No new mathematics.
Source clone commit: b54013480cb6b3b110fc3a06d8e80c1b6abba3c8 (lane directory
.claude/science/physics-loops/ym4d-hard-route-20261030, file FINISH.md rows 833-911).
Written 2026-11-13 by Claude Opus 5.5 (high effort). Every statement carries its row number "(row N)".
Where a check row's verdict differs from the row it checks, the check wins, and the text says so.

## Section plan

1. Where the proof stands
2. Checked results
3. Unchecked results still standing
4. Claims overturned by checks
5. The crux in its current exact forms, and which implies which
6. The walls, their stopping reasons and the shared assumptions
7. Live attacks and their exact next statements
8. Stopped attacks and why
9. Process lessons, stated as rules

Conventions. "Checked" means proved by one model and checked line by line by another provider or model. The checker is named. Codex astra xhigh checked most Claude rows; Claude Opus 5.5 high checked the Codex rows 865, 866, 871, 875 and 905. GUIDE marks numbers that guide only and prove nothing. ARGUED marks reasoning that is not a proof. READ marks a statement read from a source.

## 1. Where the proof stands

### 1.1 In plain words

- Ethan Sussman and Levent Alpoge wrote an account of 4D SU(2) lattice Yang-Mills: an outline (YM4_1400) and a complete account (CA-I to CA-III). Claude and Codex are authors of their text. The account controls the renormalization-group flow from the bare cutoff down to a "first-passage" scale (row 837).
- At first passage the effective action is Balaban's. The coupling g is small but not explicit. The last integral is known only up to a factor e^(O(ell^4)). The account makes no statement there on block laws, on decay or on a gap (row 837).
- The lane owns a continuation. Suppose one number is small: the thermal sum of the transfer operator on one periodic cube of fixed physical size, below 1/5041, uniformly over all first-passage data. Then Theorem S and Corollary S3' give a gap on every larger cube at every cutoff. With the account's continuum datum this gives the continuum mass gap (GAP) (row 837). This number is the seed.
- The seed is the one missing input. It is a statement on the actual bare measure along first passage, at an effective coupling of order one. A seed for a plain Wilson weight at the unit scale does not replace it. That would need a comparison of the actual effective weight with a Wilson weight, and nobody has one (row 837).
- The proved results sit at strong coupling. The seed and a volume-uniform gap hold for bare beta_W below 0.3609 (rows 836, 841). An area law holds below 2/3 (row 834, citing row 825; check 857). The surface-class bounds and (E17) hold on (0, 6/25] (rows 833, 847). The order-one band is near beta_W 2.3 to 2.6, with a m = 1 near 2.38 (row 837, GUIDE). So the band lies a factor of about 6.4 to 7.2 above the checked seed range (my arithmetic on row 837's GUIDE band and the 0.3609 endpoint of row 836).
- The seed splits into two halves (rows 892, 893). The glue half asks that the even-sector thermal sum is small: a pure even-sector mixing statement (rows 895, 896). The flux half asks that a twisted-to-untwisted ratio is near one on one torus. Neither half is proved at order one. Every attack of this round stops at one of the two halves at a box of a few correlation lengths (rows 859, 863, 892, 895).

### 1.2 Exactly

**(SEED-FP), the finish line** (row 837, `library/gap-finishline-opus.md` section 2.2). Fix the account's data: odd L, a reference coupling g at most gamma_H, first-passage data (K, beta) with beta in W_K(g), and bare spacing a_K = L^(-K) in the first-passage unit. There are K_0, a physical size ell with ell/(2 a_K) an integer at least 3 for every K at least K_0, and a number s_* below 1/5041, such that for every first-passage datum (K, beta) at g with K at least K_0:

  S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) at most s_*.

Here S is the thermal sum of the bare Wilson transfer operator of the periodic cube of physical side ell at physical time ell/2 (row 837).

**Forms on the account's own tori** (row 837). The integral of the account's density rho_K equals the bare partition function exactly, so the seed is a statement on the total masses of rho_K. (SEED-L): the upper limit of Phi_L = L^4 log Z_(K,ell,beta) - log Z_(K,L ell,beta) over first-passage data is at most phi_* below (L/2) log(13/10). (SEED-Delta) compares one torus with the infinite-volume pressure. Lemma FL turns (SEED-L) into (SEED-FP) at the larger size 6^(k_1) L ell (row 837). Check 848 found Lemma FL HOLDS, with phi' between phi_* and (L/2) log(13/10) in its application (rows 844, 848).

**The chain from (SEED-FP) to (GAP)** (row 837, table 2.5):
- (a) The seed gives a gap at least M_* a_K on every periodic cube of integer side at least ell/a_K, with M_* = 2 log(1/(5041 s_*))/ell. PROVED (Corollary S3', checks rows 698 and 699, as cited in row 837).
- (b) Every limit state at that spacing has a unique vacuum and a transfer-norm bound e^(-M_* t) in all four directions. PROVED (Theorem L3, Proposition P, check row 703, as cited in row 837).
- (c) The account's volume-first limit points are such limit states. ARGUED (row 837).
- (d) The continuum datum (OS reconstruction from separated-support curvature monomials) is READ from the account, conditional on its packages A-H (row 837).
- (e) The datum supplies the hypotheses of Proposition P'. ARGUED, not checked (row 837).

**The split** (row 892, check 893). Lemma SPLIT and Corollary O1 HOLD: (1 + S_ev)/(1 - Q_0) at most 1 + S at most (1 + S_ev)/(1 - 3 Q_0). So the Theorem SH seed holds when the glue half S_ev is at most 1/10 and the flux half Q_0 is at most 1/20 on one box. The flux half in its weakest absolute form is (CORE): on one periodic torus (a, b, b, b) with b at least 24 a, Z^(v_12)/Z^0 at least 9/10 (row 892). Row 892 called (CORE) genuinely weaker than (E17); check 893 found that this weakening is NOT established.

**The second consumer chain** (row 892). Chain I is (FQ) to (F-h) to FUSE-suff to (ES) to Theorem R, all checked, and it needs the glue half too. It reads twisted partition functions, and the account runs on untwisted tori only (row 837). (E17) is a fixed-coupling target and cannot hold on a fixed physical torus along the account's sequence (row 838). Its physical replacement (E17-phys-CA) gives (FQ) with a cutoff-independent constant K_F, conditional on the complete account's kernel suppliers (port row 865 by Codex astra, check row 868 by Claude Opus 5.5).

**The hand-off** (rows 846, 850, 861, 877). Exact block-spin steps past first passage that land the effective density in an explicit open zone (EXIT) give the bare seed at one physical size for every large cutoff (Theorem HO, HOLDS AFTER CORRECTION by check 850). The step from HO to Lemma FL needs a strict seed margin (check 850). An exact soft block step makes the per-link size small for free, but its vacuum constant equals F_T - log Z_T, so normalized softening alone supplies no seed (row 861; check 877 holds FREE and VAC, and fails only the literal equivalence of Corollary VAC2 with EXIT). EXIT itself is OPEN (rows 846, 850, 861).

**The one missing input, exactly.** (SEED-FP) at one physical size, uniformly in the cutoff (row 837). By the split it is the glue half and (CORE) at one box (rows 892, 893). No row of 833 to 911 proves either at order-one coupling.

## 2. Checked results

Each item names its row and its check row. The checker's verdict is the one stated. "After correction" means the checker repaired a step and the conclusion stands as repaired.

### 2.1 Strong coupling

- **Seed and gap below beta_W 1/3** (row 835, check 840 by Codex astra xhigh). Theorem F: the full seed (both halves) and a volume-uniform gap m(L^3) at least 3/(50a) on periodic cubes in all flux sectors, for 0 below beta_W below 1/3 (example beta 1/4, a = 282, m at least 1/4700). Theorem T: the seed below 2/7 in temporal gauge. All eleven statements HOLD. Repairs: Lemma MG needs the proved hypothesis (C1+); Lemma AVG needs its stated endpoint and scope. Imported V1, transfer, cut and shape theorems are named inputs, not rechecked (check 840).
- **Block criterion, seed and gap below 0.3609** (row 836, check 841 by Codex astra xhigh). A gauge-invariant block criterion (BC) with Theorem R (contraction, block and Langevin gaps, exponential clustering, uniform in torus and flux sector). Theorem ST: the star-block coefficient 6x(1 + x)/(1 - 4x - 6x^2), x = beta/4, is below 1 for beta below (sqrt 37 - 5)/3 = 0.3609 on every torus with periods at least 3. Corollary SEED gives the seed and a volume-uniform gap there. Repairs: Lemma GF's family quantifier fails and a covering-family repair is proved; Corollary SEED needs a free-energy convention fix. The remark that the bound first holds near a = 360 is not certified and not used. Conditional on the imported transfer and shape results (check 841).
- **Surface classes to 6/25** (row 833, check 847 by Codex astra xhigh). Theorem T6: B_O at most (51/100) N_perp (0.9697)^A on 0 below beta at most 6/25. So (RTAIL-SOS), RTAIL, (RTAIL*), (J12) and (E17) hold on (0, 6/25]. T1-T5 and the binary icosahedral transfer HOLD with minor corrections. The seed continuation past 2/9 is NOT checked (check 847).
- **Area law stays at 2/3, with exact barriers** (row 834, check 857 by Codex astra xhigh). HOLDS: the worst-case single-site chord coefficients are exactly (beta/4) times adjacency; the decimated chart; Lemma F; the 4 G_3 obstruction given Frohlich-Simon-Spencer. After correction: the in-star return to 2/3; Theorems A2 and A2' with their constants, conditional on the open hypothesis (SE); the 0.7385 decimated ceiling with an explicit environment (check 857).
- **Information identities and the layer twist bound** (row 839, check 849 by Codex astra xhigh). HOLDS: Lemma Z'' (Renyi telescoping, improving Lemma Z' to 1/(rho - 1)); Proposition TB; Proposition K; the seed as a chi-square mutual information, a min-entropy and a rank-one statement; the twist deficit as a chi-square distinguishability. After correction: Corollary TB1 (E^- at least m b - log(C b^2) below beta_W 2/3), Proposition TB2 (the 1.0109 ceiling), Proposition Q, the widened (SEED-L) margin (check 849).

### 2.2 Weak coupling, thin torus

- **Bad-point bound and chart** (row 842, check 856 by Codex astra xhigh). HOLDS: Lemmas RP and CB (base reflection positivity and a chessboard estimate, even M at least 4), Lemma Z, Theorem BAD for SU(2) with its threshold beta_BAD(n) of order n^34 log n, BAD-b, BAD-s, Lemma TB, Proposition FLUX, CH-T. After correction: the finite-region chart CH-D, Lemma GR, Proposition U1 (check 856).
- **Flip-even transfer gap in a window of base sizes** (row 862, check 880 by Codex astra xhigh). Theorem A: for n at least 2, beta at least beta_0(n) (of order n^54 log n) and even M with 4 at most M at most M_1(n, beta) = 1/(1922 n^2 eps_1), the base-direction Wilson transfer operator of the twisted thin torus has gap at least 1/(12.4 n) on the flip-even gauge-invariant sector. Theorem B: decay at rate 1/(6.2 n) up to an additive 4 N M eps_1. HOLDS: T3, F4-F6, T1-T2, the exact Z_2 covariance, Lemma CP. After repair: H3 (an explicit quintic bound 60r), keeping H4 and the printed constants; HS0 with a stated domain (check 880). This is a stand-alone weak-coupling four-dimensional gap in a window, not uniform in M (row 862).

### 2.3 Plumbing to the account

- **Physical witness and consumer** (row 844, check 848 by Codex astra xhigh). HOLDS: Lemma W (i)-(iv) (cylinder limit, log-convexity, even-gap bound), the tent witness, Proposition W-phys, the corollary from (E17-phys) to (FQ) given (SD-cyl), Lemmas A and F, Lemma FL of row 837. After correction: the scope of four repairs to `gap-assume-opus.md` 3.2; the complex chessboard is the already proved lemma with a rectangular dictionary (check 848).
- **Complete-account port** (row 865 by Codex astra xhigh, check 868 by Claude Opus 5.5 high). (SD-cyl-CA) from CA-I Theorem 0 (iv) with the account's lattice kernel and half-error gives rho_CA = c_K/(3 C_K), S_ev at least rho_CA^(2A/(3d)), and (E17-phys-CA) implies (FQ) with a cutoff-independent K_F. All six statements HOLD. Conditional on the account's (h1)-(h3) kernel comparison, its corollary hypotheses, the volume-transfer premises and the rectangular port. The outline-to-CA dictionary of first-passage data is unchecked. The parts reused from row 844 are not independently checked (both Opus) (check 868).
- **Hand-off zones** (row 846, check 850 by Codex astra xhigh). HOLDS: Lemmas DC*, PV (explicit zone radii), BOX, TRUNC, Identity PHI, the cancellation of vacuum constants. After repairs: Theorems O-SEED and HO keep their constants. The step from HO to Lemma FL needs a strict seed margin (check 850).
- **Exact block steps** (row 861, check 877 by Codex astra xhigh). HOLDS: Proposition FREE (soft step gives the zone's per-link size for any input, U(1) too), Lemmas K1-K4', Theorem STEP with threshold corrected to beta below 1/sqrt(216 pi), Proposition VAC, Theorem HL, Lemma HL2, Corollary HL3, identity (6.3), Lemma TS, Lemmas K5-K9 (loops, truncated loop correlations, twisted masses and reflection positivity transport exactly). After correction: Theorem LAND, Step R2, the account summaries (check 877).

### 2.4 Reductions of the crux

- **Spin filter** (row 843, check 854 by Codex astra xhigh). After correction: Theorem 3.4 and Corollaries 3.5, 3.7 (on V_(5/2) the SU(2) Wilson convolution lies below the Q_8, 2T and U(1) eigenvalues at every beta) and their kinetic exposure. HOLDS: the restriction table, finite-group eigenvalues, the (LC) pair, commutator bounds, Bessel lemmas, small-beta expansions (check 854).
- **(LS) is (E17); the parity form** (row 860, check 864 by Codex astra xhigh). HOLDS: Theorem HS (high-spin rarity through one transfer step), HS-2, P1, P2. So (LS) equals (E17) up to e^(-c#E), and the odd sector is the event that the half-integer Z_2-cycle of a slice has odd class. After correction: HS-1, Lemma OS, Lemma DS and its parts, P3, B1 (check 864).
- **Parity and homological analyticity** (row 866 by Codex astra max, check 870 by Claude Opus 5.5 high). HOLDS: (E17) is the slice-homology parity problem; the marked area-order zero; HA implies (E17) with area gain; a zero-free disc implies HA; the density-1/3 construction; the Z_2 Peierls test refuting an environment-uniform conditional bound (valid for beta above 2.191); HA fails for Z_2 at beta 5/2 and in a background-uniform SU(2) version (check 870).
- **'t Hooft form and a local separation** (row 867, check 869 by Codex astra xhigh). After repairs: Lemma QS (e_(1/2) at most r_(1/2)(5 beta)^4, at most 0.5806 at beta 2.3) and its probability constants; Proposition TL (the parity of an edge set is a wrapping 't Hooft surface) with the dual-surface qualification; SEP(b) with certified separation 0.0359 (check 869).
- **Response integral** (row 871 by Codex astra max, check 874 by Claude Opus 5.5 high). HOLDS: real-segment HA is automatic and insufficient; the interpolating measures and (R1); (R2); (C1) with reduction to (C2); (D3) equivalent to HA after shrinking the disc; the thin nearly flat event has probability at most 2^(-V/625) (check 874).
- **Filter identity and EXC** (row 872, check 873 by Codex astra xhigh). HOLDS: Proposition EXP, d log Tr(P L(s)^t)/d log s = t times the one-slice high-spin count, and the conditional response algebra. After correction: Lemma 3.1 and the (E17) consumer rate; so EXC implies (E17) (check 873).
- **EXC stays live** (row 875 by Codex astra max, check 881 by Claude Opus 5.5 high). All five statements HOLD: the corrected EXC; the electric-only reference has an order-L_i positive boost response with gamma about 0.010 at beta 2.3 (group-blind); large boosts reverse sign at fixed volume when the cut-crossing edge count is even; k_S(-I) below -163/660 on [2.3, 2.6]; identity (22) leaves a residual equivalent to EXC (check 881).
- **Squaring bound** (row 876, check 883 by Codex astra xhigh). HOLDS: Lemma SQ, (lambda_chi/lambda_0)^(2t) at most 1/kappa + (1 - 1/kappa)(lambda_1^+/lambda_0)^t, and the displayed SQ-F bound. After scope correction: Theorem SQ, the diffusion and window statements, Lemma RPF and the plateau bound (check 883).
- **Moment hierarchy and kurtosis** (row 886, check 889 by Codex astra xhigh). HOLDS: the moment hierarchy (Theorem 4.1), the discrete energy identity, the symmetry theorems (kappa at least 3/2 when the flip lies on a circle of symmetries, as for U(1)). After correction: the diffusion, sign, energy-density and counterexample statements (kappa = 1 examples with heavy flux) (check 889).
- **Decoder hierarchy** (row 887, check 891 by Codex astra xhigh). HOLDS: deterministic patching, the hereditary 1/4 rule, Lemma T1, the ratio-ten hierarchy, Theorems TOP and TOP+, frozen finite-group selectivity, identity (PAR). HOLDS under the chessboard estimate: the same-class recursion z_(j+1) at most C_3 z_j^2 with C_3 = 1,120,616, which escapes the failure found by check 882. After correction: the snake's scope, the level-zero rate, the domain of (SEED-DEC-U), the filling-Peierls barrier (check 891).
- **Magnetic response identities** (row 888, check 890 by Codex astra xhigh). HOLDS: the flux-response identities, Theorem 3.3's derivative formula (R(0) = R'(0) = 0, R''(0) = 4 L_i pi_5 (D_(5/2) - D_(1/2))), Proposition 7.5, Theorem 9.3 (finite flux tension of the unboosted model on every torus and twist), Proposition 9.4. After correction: the EXC-W identification, Proposition 6.1, the reading of (DRESS) (check 890).
- **Implication graph and (CORE)** (row 892, check 893 by Codex astra xhigh). HOLDS: Lemma SPLIT, Corollary O1, faces F2 and F3, Lemma VAR1, Proposition K ((KURT) with glue gives (CORE)), Lemma R, Proposition W ((WALL)_40 with glue at 160^(-16), a at least 82, b at least 24 a, gives the seed). After correction: Proposition ABS, (VF), Lemma VAR2. Of ten spot-checked edges, five HOLD and three HOLD AFTER CORRECTION (check 893).
- **(WALL)_40 is a kurtosis floor** (row 894, check 897 by Codex astra xhigh). HOLDS: Proposition D and Corollary D1 (under the glue hypothesis, (WALL)_40 is exactly kappa at least 2), Theorem A1, Lemma B4, Corollary B4', Proposition B5, six exact 2D kurtosis values (SU(2), 2T, 2O: 2; Q_8: 4; U(1): 3/2; Z_2: 1), the connected counterexample. After correction: Corollary K' (kappa at least 1.66 suffices at the same glue level), D2, A2, A3, B6, B1 (check 897).
- **Glue identities** (row 895, check 896 by Codex astra xhigh). HOLDS: faces G1, G3, G2 (its fixed-threshold equivalence needs correction), Lemma CS (its exclusion of other methods FAILS), Lemma LOC for its stated support condition, Lemma MC, Lemma UP as an upper bound, Lemma G5 with its constants (110592), Proposition TR as a conditional comparison, the even D-shape, the virial identity. After correction: G4, Proposition SEP, Remark UNTW, Proposition FIB (check 896, per-statement verdicts in `library/gap-glue-check-astra.md`).
- **(VAR-SLAB) reduction** (row 899, check 901 by Codex astra xhigh). HOLDS: for the half-torus slab twist ratio rho, E[rho^2] = 1, Var(rho) = 4p(1-p), p/(1-2p) = E_tw[sinh^2(X/2)] with X = log rho, the Poincare inequality and the conditional reduction of the flux half at one coupling to the gauge-invariant Langevin gap and the L^2 force response (FR), with a correction to the force description. Also Proposition W1-t, Lemmas W4-uni, W3-psi, W2-L2 on their domains; Lemma W1-abs after correction (check 901).
- **Free-wall structure** (row 898, check 902 by Codex astra xhigh). HOLDS: FW1-FW6 (free space walls carry no centre sector and no twist; super-multiplicativity; the deficit's sign and monotonicity; the crossing identity; the enlargement bound), the abstract counterexample to a vector engine, the tube corollary. After correction: the conditional engine from (WALL-1), (WALL-2), restricted to dyadic cubes with explicit constants (check 902).
- **Free field passes the wall inequalities** (row 903, check 906 by Codex astra xhigh). HOLDS: in the free massive scalar with Neumann walls, (WALL-1) with optimal C_1 = 1 and (WALL-2) with C_2 = 1/floor(2b/a); the Proca towers; bare-Gaussian sub-multiplicativity. HOLDS AFTER CORRECTION overall (check 906).
- **Doubling identities and the conditional engine** (row 907, check 909 by Codex astra xhigh). HOLDS: the ring dictionary for p(a), the void domination defect, both doubling identities, both abstract C_2 obstructions, Theorem C (the conditional engine on dyadic cubes from a doubling bound and a seed), the fixed-size SU(2) tube coefficients. After correction: (CUT-TH) needs k = 4(1+theta')/(1-theta) unless its bounds are symmetric (check 909).
- **Doubling equals joining** (row 910, check 911 by Codex astra xhigh). HOLDS: Lemma J, so (H-DBL) with constant k is exactly (JOIN-TH_(k-2)); Theorem C' (doubling is needed only on cold boxes, S(a; B) at most 1/(3k^4)); Lemma DS; Theorem 2P' given the fixed-size coefficient input; the positive fixed-size join excess at small beta. After correction: Theorem 2P's class, range and seed data (check 911).
- **Transport decision** (row 905 by Codex astra max, check 908 by Claude Opus 5.5 high). HOLDS: S1 (a closing sector forces a divergent all-time cost, conditional on an all-time hypothesis on one invariant spectral family); S2 (the literal centre-even pin path is invalid). After correction: S3 (full-trace pin repair with seed X at most 64 delta_n, which carries glue plus flux) and S4 ("not supplied, not refuted") (check 908).
- **Other checked reductions.** Row 863 (check 879): B1 (the two-slice law is the Schroedinger bridge of the electric orbit kernel and the slice law) and T2 (cut and reglue) HOLD; Lemma A2 (the model with only time-like orientations is seeded at every beta_t) and B2 (Hopf bound, extensive) HOLD AFTER CORRECTION. Row 859 (check 882): the tube identity HOLDS (the tube-conditioned twist covariance is the variance of a conserved Z_2 charge at every separation). Row 878 (check 884): F5, Lemma TD, Lemma CX1 HOLD, and (TS-theta) HOLDS for untwisted Z_2 at beta at least 5/2 with theta = 1, C = log 2, n_0 = 8; Theorem E HOLDS AFTER CORRECTION.

### 2.5 Obstructions (walls), checked

- **Single-link tree gauge stops at 1/3** (Lemma AVG, row 835; check 840, with stated endpoint and scope). Slab blocks with Lemma SC never beat 2/9 (Proposition NG, row 835; check 840).
- **Vertex blocks with worst-case single-link responses fail at beta 0.775 or more** (Proposition CEIL, row 836; check 841). Row 861 limits this: the cap bounds one family of majorants, not every block method (check 877 holds the account summaries after correction).
- **No weighted single-site Dobrushin passes 2/3** (row 834; check 857).
- **Background-uniform layer twist bounds are false above 4 G_3 = 1.0109** at the flat background, given Frohlich-Simon-Spencer (Proposition TB2, row 839; check 849 after correction; also row 834, check 857).
- **The annealed condition is the worst case**: literal (AN1) is equivalent to an essential worst-case exterior bound (check 852 of row 845).
- **Clustering cannot give the flux half**: the tube identity (row 859; check 882).
- **Environment-uniform conditional parity bounds are false**: the Z_2 Peierls test, beta above 2.191 (row 866; check 870). HA fails for Z_2 at beta 5/2 and in the background-uniform SU(2) version (check 870).
- **Filling-Peierls barrier**: P(half-integer edge) would need to be below about 1/9, against GUIDE 0.33 (row 887; check 891 after correction).
- **Normalized softening supplies no seed** (Proposition VAC, row 861; check 877).
- **Reflection positivity across the free axis gives a void image inequality**, with defect at least delta_e(1) (row 907; check 909).
- **Doubling is not structural**: two-sector and two-coupling counterexamples survive in row 898's class (Theorems 2P, 2P', Lemma DS, row 910; check 911).
- **Villain U(1) at beta at least 2^14 fails (BC) for every block shape at the coefficient step** (Theorem U, row 836; check 841); the massless Gaussian field has zero margin (Proposition GFF, same rows).

## 3. Unchecked results still standing

No other provider or model has checked these. Each stands as its author marked it.

### 3.1 Proved by the author, unchecked

- **Finite-subgroup moments** (row 838). The Haar moments of Q_8, 2T, 2O and 2I first differ from SU(2) at degrees 4, 6, 8 and 12. The commutator average I/4 is shared by every non-abelian finite subgroup. Row 804's pair filters are shared by Q_8. Q_8 breaks the bound a at most 1/4 (its supremum is 1/2). So a tool at the crossover must see spin 2 or 3, not spin 6 (row 838).
- **Lemma QS density corollaries** beyond those check 869 named: P(spin at least 2) at most 0.016 and filter exposure at most 6.6e-4 for beta at most 2.5 (row 867; check 869 repaired the constants of QS but its RESULT does not list these corollaries).
- **Row 863's hand bounds** 0.350 at most f(2.5) at most 1.40 (row 863; check 879's RESULT does not report them).
- **The account does not give (UNIV-FP)** (row 904, Claude Opus 5.5 high). READ YM4_1400 L94031-94510: the universality proposition compares two bare weights Wilson + h_0 with h_0 in a fixed ball of irrelevant analytic profiles, at one frozen endpoint after retuning, with constants independent of horizon and volume. It leaves out large-field histories, does not compare vacuum factors and is "not uniform over growing volumes" (row 904). Unchecked.
- **Row 858's partial mined** (row 900, Claude Opus 5.5 high). Of 59 items in row 858's partial file, 40 are covered by later rows, 8 partly, 7 untouched, none refuted (row 900).

### 3.2 Argued, unchecked

- Steps (c) and (e) of the chain from (SEED-FP) to (GAP) (row 837).
- Strong-coupling results reach the continuum only as a landing zone for a renormalization hand-off; Dobrushin-type results survive perturbation of the action, surface-class results as stated do not (row 838).
- A seed past 2/9 follows from row 833's bounds only through the unchecked continuation from (FQ) (rows 833, 847).
- kappa tends to 1 for SU(2) below the centre crossover, so no size-free regularity theorem for (KURT) exists; kappa is near 3 at the seed size (row 886).
- The seed fails along the continuum trajectory in the decoder form: the bare parity cycle becomes a local loop condensate (row 887).
- (TS-theta) is off the critical path; "(E17) with GLUE gives (CORE)" (row 892).
- A mixed bare weight with fixed beta_F is not covered by the account's universality, and both of its forms lose the Wilson large-field small factor (row 904).
- At small beta the Wilson wall exchanges single tubes, so the image bound is false while (WALL-1) and (WALL-2) hold at leading order (row 907).
- Compact U(1) just above its transition must fail the doubling at a wall-induced crossover scale (a proposed new fact test); frozen finite groups satisfy (JOIN-TH) (row 910).
- The flux half is a torus artifact for the tr F^2 sector (row 898).
- Untouched items of row 858: route W (a vector-state Theorem S on free-wall boxes, crux (W-ENG)); (UNIV-FP); the sheet-coupling identity E6, crux (SURF). Row 858's route M should not be followed (row 900).
- Novelty: (SEED-DEC) is a new packaging inside the lane, literature novelty not established (check 882 of row 859). Row 836's novelty was not established (row 836). Lemma A2's quantitative statement and B1 are new inside the searched corpus (check 879).

### 3.3 GUIDE numbers in use (discharge nothing)

- Order-one band beta_W 2.3 to 2.6, a m = 1 near 2.38 (row 837).
- Larger flat blocks reach a block coefficient below 1 to about beta 0.42 (row 836).
- True spin-2 density at beta 2.3 is 2e-5; odd spin at least 5/2 below 6e-7, on an 8^4 heat bath (row 860). Half-integer edge density about 0.33 at beta 2.3 (rows 866, 887).
- e_F 0.267 for SU(2) at beta 2.3; 0.40 to 0.75 on the U(1) Coulomb branch; 0.93 frozen 2T; 0.96 frozen Q_8 (row 867).
- One SU(2) tube in a one-plaquette 2+1 model has kappa below 2 at every coupling (1.53 at beta 2.3); the hidden bit forms with the even gap open there (row 894).
- The flat-wall slab at beta 2.3 orders at thickness 1 to 4, is undecided at 6 and is disordered at 8 (row 899).
- Free scalar: (WALL-2) supremum about 0.012 (row 903); doubling ratio at most 2.8 (row 907).
- A Z_6 analogue shows a carrier crossing and a positive dressing response after it (row 888).

### 3.4 Literature readings (bounded searches, not proofs of absence)

- Hand-off (row 851, Codex luna high): quantitative perturbation neighbourhoods of Dobrushin uniqueness, strong-mixing to RG hand-offs for lattice gases and the Abelian Higgs model, and Balaban's small-field sequence are known. No published theorem combines them into row 846's hand-off for pure SU(2).
- Annealed criteria (row 853, Codex luna high): stationary-averaged coupling and space-time Peierls methods are known for non-gauge, chiefly finite-spin systems. None gives a usable criterion for stationary Wilson SU(2) block dynamics.
- Finite subgroups and high-spin rarity (row 855, Codex luna high): no literature supplier for an interacting one-slice high-spin rarity bound.
- Marginal-dimension method (row 885, Codex luna high): Aizenman and Duminil-Copin (2021, Theorem 1.2) rests on the ferromagnetic random-current law and source switching. Gauge-side uses exist only for abelian or finite abelian groups: Forsstrom-Viklund 2025 (Z_2), Aizenman Part III Theorem 9.1 (3D Z_2), Duncan-Schweinhart 2025 (prime-q Potts gauge). None is non-abelian. The arXiv download failed; the papers were read through a web reader (row 885).

## 4. Claims overturned by checks

Each entry gives the claim, its row, the check and the reason. The check's verdict holds. Where a row's own RESULT still reads the old way, read it through this list.

### 4.1 Claims that FAIL

1. **A universal ban on a strict count improvement** (Proposition L, row 833). Check 847: FAILS by C5's own weighted sum. Its narrower direct-certificate form holds.
2. **tau_1 at most 0.2580 as a proved bound; tau_* = 1/4** (Lemma P2 and Theorem A2, row 834). Check 857: P2's algebra holds, but the bound is not proved, and tau_* = 1/4 is false on C5. The recalled O(4) Simon-Lieb star range is unverified. So the area law past 2/3 through A2 rests on an open hypothesis (SE) that fails at the value row 834 used.
3. **Lemma GF's unrestricted family quantifier** (row 836). Check 841: FAILS; a covering-family repair is proved. The claim that the star bound first holds near a = 360 is not certified.
4. **Overextensions and recalled literature claims** of the compression note (row 839). Check 849: FAILS for the overextensions it lists and several recalled literature claims (the checker verified the sources). No blanket information-theoretic no-go is established.
5. **Restating S1 as (S1-loc) or (S1-T)** (arguments W1, W2, row 842; the lead adopted these targets in row 842). Check 856: W1 and W2 FAIL as arguments for restating S1; the torus-covariance form and equivalence of (S1-T) FAIL; the twisted-U(1) rider of Theorem BAD FAILS.
6. **The unrestricted L2 restriction map; the defect is largest at spin 5/2** (row 843). Check 854: both FAIL.
7. **(SD-cyl) as a port matched to the complete account** (row 844). Check 848: FAILS; the argument rests on the outline. Row 865 redid the port on CA-I Theorem 0 (iv), and check 868 holds it, conditionally.
8. **(AN) avoids worst-case exteriors; (SP-ext) is the crux of the conversion** (row 845). Check 852: literal (AN1) allows a schedule repeating one block jump, so it is equivalent to an essential worst-case exterior bound; nontrivial pure-exterior (SP-ext) with eps below 1 FAILS under repeated block updates. AG' needs the total gauge-jump coefficient; GFF-AN needs its weight domain. Row 845's remark that the 0.775 ceiling does not limit (AN) is therefore moot.
9. **The n = 226 landing example; the 0.0042 star radius** (row 846). Check 850: both FAIL (0.0041 is safe).
10. **"The account's first-passage density lies in no zone"** (row 846). Row 861 changed this to "membership not established", and check 877 holds the account summaries after correction.
11. **The strand-counting threshold P(half-integer edge) below 1/4.684, and the chessboard recursion z_(j+1) at most C_3 z_j^2** (row 859). Check 882: the numerical strand exclusion FAILS; the recursion as stated FAILS (C_3 not supplied); (TOP_j) stays OPEN; abstract squaring on tripling scales does not deliver (E17). Row 887 later proved a same-class recursion with C_3 = 1,120,616 (check 891).
12. **Filter plus (HS) cannot force (LS), because U(1) shares every input** (V1, row 860), and the chessboard obstruction at its line 200. Check 864: both FAIL. U(1) does not satisfy the filter bound on Sym^5 V (its restriction has norm at least I_1/I_0). So the spin-5/2 filter is a live SU(2)-specific input.
13. **Corollary VAC2: soft step then Theorem HO is equivalent to EXIT** (row 861). Check 877: the literal equivalence FAILS; normalized softening alone supplies no seed. Theorem STEP's threshold is corrected to beta below 1/sqrt(216 pi).
14. **Lemma PE's (S1-T) clause** (row 842). Row 862 found it FALSE by an exact Z_2 model and replaced it by the window Theorem A (check 880 holds the replacement). Check 880 also corrects row 862's fixed-rho no-uniform-gap wording, its forced additive torus term claim and Lemma CP's flux rider.
15. **Row 863's obstructions and identifications**: T2's probabilistic (reglue) obstruction, the path converse, the finite-periodic and ground-state identification, the full-periodic and (ES) identification, and the flat four-torus class count. Check 879: all FAIL as written.
16. **The shrinking-disc example as a limit on analytic continuation** (row 866). Check 870: it has no closure structure, so it refutes only a generic positivity and factor inference, not the Wilson polynomials or HA.
17. **The six-candidate exclusion and fact test T3** (row 867). Check 869: both FAIL. T3's N_t = 3 GUIDE sampler has an invalid update partition (its full-sweep kernel does not preserve the Wilson law), so its rows support nothing; the Borgs-Seiler use has a limit and observable mismatch. Ginibre's original text could not be read. Row 859 had already treated these separations as unverified.
18. **(C2) is weaker than (E17)** (row 871). Check 874: (C2) is NOT weaker than (E17); with (C1) it implies (E17), and the converse needs a sign of the response that is unproved. So (C2) restates (E17) or is stronger. Read row 871's "weaker" as "weaker than HA".
19. **The filter cannot carry (LS) = (E17)** (row 872's negative verdict). Check 873: FAILS, with Step 5.3's operator inequality, its universal volume-loss claim, the localization necessity and dichotomy, and the dressing-size bounds. EXC is not ruled out.
20. **(KURT) alone supplies pure (F-h); the consumer needs (F-h) only; (KURT) is logically weaker than (LOC) and (E17)** (row 876). Check 883: all three FAIL.
21. **U(1) Coulomb has theta = 4 exactly, so (TS-theta) is selective; the compact-Villain Gaussian identification; Q_8 and 2T are exempt from every (ES) test** (row 878). Check 884: all three FAIL. Separately, row 878's claim that "heat kernel" does not occur in YM4_1400.tex is wrong; row 900 found 17 lines (row 900, unchecked, a grep fact).
22. **The hidden-bit converse; discrete (KURT) implies (FUSE-E); unqualified full-consumer sufficiency** (row 886). Check 889: all FAIL. Check 893 confirms that edge 22 of row 892's graph ((KURT) implies (FUSE-E)) FAILS.
23. **No bound conditioning on a typical gauge field exists; every Peierls method is excluded** (row 887, from identity (PAR)). Check 891: the universal exclusion of typical-field conditioning FAILS, and the all-Peierls exclusion FAILS. (PAR) itself holds.
24. **The carrier crossing at b* about 0.31 to 0.34 erases the electric gain** (row 888, argued from second-order data). Check 890: inferring the crossing or the erasure from the second-order data FAILS. EXC is less blocked than row 888 argued.
25. **(CORE) is genuinely weaker than (E17)** (row 892). Check 893: the weakening is not established. Edge 10 ((DRESS) equivalent to pointwise EXC-W) FAILS; edge 22 FAILS (item 22).
26. **The eight-vacua and Z_2 topological-order identification of the scenario to exclude; B1's extra kurtosis and vacuum-density inferences** (row 894). Check 897: both FAIL. The near-bit scenario stands as a kappa statement (Lemma B4, Proposition B5 hold), not as a topological order.
27. **Row 895 as written** (the glue half). Check 896: FAILS as written overall. Lemma CS's exclusion of other methods FAILS. Lemma LOC's converse and method ceiling (that even-sector block criteria inherit 1/3, 0.3609, 0.775) do not follow. Proposition FIB's exhaustive dichotomy FAILS. Lemma UP's "only with factor 1728" FAILS. Proposition TR's converse FAILS. The frozen Q_8 and 2T PASS verdict FAILS: it contradicts prior work (`gap-crux-exercise2-check-astra.md` 227-266, two inequivalent even flat vectors). The U(1) failure at (Z0) is GUIDE, not an established test. Proposition SEP, Remark UNTW and face G4 hold only after correction.
28. **The three next attacks pass the fact tests** (row 898). Check 902: FAILS. Unrestricted (FLUX-Z2) is false; U(1) has the asserted quotient; the periodic Q_8/2T exemption is already refuted; the pin path has no conserved pure-gauge even sector.
29. **SA6: every wall's proof is group-blind, stated for every compact group with a centre** (row 899). Check 901: FAILS in that generality. SA1, SA2, SA3, SA5 and the "five ways to one comparison" reading hold after scope and premise corrections; SA4 holds for the named torus consumer.
30. **The "two orders" sentence; an all-shapes extrapolation of the GUIDE value C_1 at most 1.7** (row 903). Check 906: both FAIL. The Wilson-limit identification of the Neumann wall needs correction.
31. **Attack 3 as stated does not survive** (row 905's own verdict). Check 908 narrows this: the full-trace pin repair carries glue plus flux, not glue only, and the transport family is not closed under row 898's stop rule. Two forms stay live (section 7.2).
32. **Step 10's universal flux-removal test; Step 11's depleted-family cancellation** (row 907). Check 909: both FAIL. (CUT-TH) needs k = 4(1+theta')/(1-theta) unless its bounds are symmetric.
33. **Step 4.3's unnormalized no-flux probability identity** (row 910). Check 911: FAILS by a missing c_0 factor, which cancels in the thermal excess. The conclusions of row 910 stand.

### 4.2 Claims that hold only after a correction that changes their reading

- Lemma MG needs (C1+); Lemma AVG needs its endpoint and scope (row 835, check 840).
- Corollary SEED needs a free-energy convention fix (row 836, check 841).
- The four repairs to `gap-assume-opus.md` 3.2 (row 844) hold with a stated scope (check 848). Row 838's 3.2 had the class distance, gamma, eps_0 and the exponent wrong (row 844).
- Lemma FL's application uses phi' between phi_* and (L/2) log(13/10) (rows 844, 848).
- HO to FL needs a strict seed margin (row 846, check 850).
- The low-spin filter theorems need proof repairs and a plane-normalization factor (row 843, check 854).
- Lemma QS needs normalization and arithmetic repairs (row 867, check 869).
- H3 needs an explicit quintic bound 60r (row 862, check 880).
- Proposition ABS, (VF) and Lemma VAR2 (row 892, check 893); edges 12, 14, 27 (check 893).
- Corollary K' (kappa at least 1.66) needs numerical, domain and scope corrections (row 894, check 897).
- The conditional WALL engine holds only on dyadic cubes with explicit constants (row 898, check 902).
- S1 of row 905 is conditional on an all-time hypothesis on one invariant spectral family; its Villain U(1) application stays ARGUED (check 908).

## 5. The crux in its current exact forms, and which implies which

Source: the implication graph of row 892 (38 edges, `library/gap-crux-core-max.md` Step 3 and table 8.1), its check 893, and rows 894 to 911. Status words: PROVED-c means proved and checked; PROVED-u means proved, unchecked; FAILS means a check refuted the edge.

### 5.1 Two consumer chains

- **Chain II (the seed chain).** (SEED-FP), or a Theorem SH seed shape at one box, gives a gap on every larger cube, and with the account (GAP) (rows 837, 892). By Lemma SPLIT (PROVED-c, rows 892, 893) its two halves are GLUE and (CORE).
- **Chain I (the fusion chain).** (FQ) to (F-h) to FUSE-suff to (ES) to Theorem R, all checked, with GLUE and (F-l) (row 892). Its exact flux half is (Q-ABS): an absolute one-size bound on the heavy flux weights; a rate enters only through the form (FQ) (Proposition ABS, row 892, PROVED-c after correction by check 893).

### 5.2 The forms, exactly

- **GLUE.** S_ev(a; b^3) at most 1/10 on one box (row 892), or the stronger levels 160^(-16) (Proposition W) and 160^(-8(1+eta)/eta) (Proposition K) (row 892). No flux node supplies it (row 892).
- **(CORE).** On one periodic torus (a, b, b, b) with b at least 24 a: Q_0 at most 1/20, that is Z^(v_12)/Z^0 at least 9/10. One order-one number, one size, m = 0, no rate (row 892).
- **(NGD).** The conditional form: S_ev(a; b^3) at most s_0 implies (CORE) (row 892).
- **(VF).** The variational face of (CORE): eps_v at most 1/(25 b), a lower bound on a top eigenvalue (row 892; PROVED-c after correction, check 893).
- **(S1) in sheet form.** A perimeter law for the open thin vortex sheet, with area coefficient below 1/(25 b^2) (row 892). Row 887's (S1) is the same idea as a noise model: a low-density short-range model of the SU(2) one-slice law, that is, a local perimeter law for the equal-time 't Hooft functional (row 887).
- **(KURT)_eta.** The flux ground function's fourth moment kappa at least 1 + eta at the seed size, uniformly in the cutoff (rows 876, 886). In Hamiltonian form kappa = 3r/(3r - 2) (row 886, after correction by check 889).
- **(WALL)_40.** Var(g^2) at least min{1, (a/40) E[g^4] (1 - theta_chi^2)} for g = Psi_chi/Omega on the periodic box b^3 at time a, b at least 24 a, a at least 82 (row 892). Under GLUE it is exactly kappa at least 2 (Proposition D, row 894, check 897). The sufficient floor is kappa at least 1.66 (Corollary K', row 894, after correction by check 897).
- **(HB).** A box with a hidden centre bit has a light even excitation; equivalently, a near-bit flips slowly (rows 886, 892). (HB) = (WALL)_M (row 892).
- **(FUSE-E)_g.** E at least g m for the heavy electric sectors (row 886).
- **(E17).** The fixed-coupling twist deficit. Exact equivalents: (LS) up to e^(-c#E) (row 860, check 864); the slice-homology parity problem, the odd class of the half-integer Z_2-cycle having probability at most C a^p eta_*^(a/2) (rows 860, 866, check 870); the wrapping 't Hooft surface (row 867, check 869).
- **HA.** Relative homological analyticity of the centre-odd marker (row 866). It fails for Z_2 at beta 5/2 and in a background-uniform SU(2) version (check 870).
- **(C2).** The integral of the absolute response |R| over [lambda_0, 1] at most C a^p e^(-ga) (row 871, check 874).
- **EXC.** The integral of Delta(s) ds/s from 1 to s_* at least c_0, Delta = Cov(N_hi, 1_odd)/p (row 872, corrected by check 873). Sharpest open form (check 881): an order-L_i lower bound, at least -theta gamma_min L_i with theta below 1, uniform over tori, twists and b, on the boosted-minus-unboosted, odd-minus-all magnetic-cut plaquette response integrated over b in [0, beta]. The available bound is 4 beta n, of order a^3 (check 881).
- **EXC-W and (DRESS).** EXC-W is the area form of EXC; the magnetic bound R(beta) at least -theta gamma L_i is EXC-W in other units (row 888, after correction by check 890). (DRESS): a positive order-L_i excess of half-integer spin at least 5/2 temporal plaquettes on the fundamental flux sheet at isotropic coupling (row 888).
- **(SEED-DEC-U).** 64 P(a box of half the torus side is unclean) at most (K/8) sqrt(S_ev), with no reflection positivity, for every magnetic background (row 887; domain corrected by check 891).
- **(SEED-DEC-H).** z_0 below 8.93e-7; it gives an odd weight exp(-c L^0.301), not (E17) (row 887).
- **(E17-phys-CA).** (E17) in physical units at rate log(3 C_K/c_K)/(3d) (row 865, check 868).
- **(PATH) and PIN-MIX.** A torus comparison of local means along a coupling path from 0.361 into the band, and a pinned block mixing lemma (row 861). Proved only below 0.3609 and, by pinning, below 1/sqrt(216 pi), about 0.0384 (row 861, check 877).
- **(VAR-SLAB) with (FR).** 4p(1-p) at most E[|grad X|^2]/lambda, X = log rho, lambda the gauge-invariant Langevin gap (row 899, check 901). The flux half at one coupling follows from lambda and one L^2 force response (FR) (row 899, check 901).
- **Free-wall doubling (H-DBL) = (JOIN-TH_(k-2)).** g(a; B with B) - 2 g(a; B) = F_join(a; B) - a J_0(B), so the doubling bound with constant k is exactly: the thermal excess of the joining free energy of two free boxes is at most (k - 2) g(a; B) (Lemma J, row 910, check 911).
- **(GLUE-FP)_sigma.** By Lemma G5 it follows from (Z0) m_ev((24a)^3) a at least 2[110592 G + log(1/sigma)] and (COUNT) g(a/2; a^3) at most G (row 895; G5 HOLDS by check 896).
- **(GLUE-1).** S_ev(a; b^3) at most 1/10 at one coupling in the band (row 898), sought through THERM-DI-beta or THERM-DI-pin (rows 905, 908).

### 5.3 Edges

Sufficient edges into the seed chain:
- GLUE + (CORE) give the SH seed (Lemma SPLIT, Corollary O1, row 892; PROVED-c, check 893).
- (VF) plus a small s_+ gives (CORE) (faces F2, F3, row 892; PROVED-c, check 893).
- (KURT)_eta with GLUE at 160^(-8(1+eta)/eta) gives (CORE) and the periodic seed without (F-h) (Proposition K, row 892; PROVED-c, check 893).
- (WALL)_40 with GLUE at 160^(-16) gives the seed and the gap on every larger cube (Proposition W, row 892; PROVED-c, check 893). Under GLUE, (WALL)_40 is kappa at least 2 (row 894, check 897), so this edge is Proposition K with eta = 1 (row 894).
- kappa at least 1.66 with GLUE suffices (Corollary K', row 894; PROVED-c after correction, check 897; it rests on row 754's trace bound).
- (SEED-DEC-H) reaches chain II at fixed coupling through SPLIT (row 892, ledger item ii; check 893 did not report on this edge). It still needs GLUE and its own seed (row 892).
- (VAR-SLAB): lambda and (FR) give the flux half at one coupling (row 899; PROVED-c, check 901).
- The free-wall engine: a doubling bound with constant k on cold boxes and a seed S(a; B) at most 1/(3k^4) give the gap on dyadic cubes (Theorems C, C', rows 907, 910; PROVED-c, checks 909, 911). (WALL-1) and (WALL-2) imply the doubling bound (row 898, check 902 after correction); (WALL-2) is sufficient, not necessary (row 907, check 909). On free walls there is no centre sector and no twist (FW1, row 898, check 902).
- EXIT gives the bare seed at one physical size (Theorem HO, row 846; PROVED-c after correction, check 850).

Edges into (E17) and the fusion chain:
- (E17) gives (FQ) at fixed coupling (checked; row 892).
- (E17-phys-CA) gives (FQ) with cutoff-independent K_F (row 865, check 868), conditional on the account's kernel suppliers.
- HA gives (E17) with area gain; a zero-free disc gives HA (row 866, check 870).
- (C2) with (C1) gives (E17) (row 871, check 874).
- EXC gives (E17) with eta_* = e^(-2c_0) (row 872, check 873 after correction).
- (SEED-DEC-U) reaches (FQ) (row 887, unchecked as an edge; its domain corrected by check 891).

Edges that FAIL or are not established:
- (CORE) strictly weaker than (E17): not established (check 893).
- (DRESS) equivalent to pointwise EXC-W (edge 10): FAILS (check 893).
- Discrete (KURT) implies (FUSE-E) (edge 22): FAILS (checks 889, 893).
- (KURT) alone gives pure (F-h): FAILS (check 883).
- (C2) weaker than (E17): FAILS (check 874).
- (FUSE-E) suffices for the full consumer without qualification: FAILS (check 889).
- Soft step then HO equivalent to EXIT: FAILS (check 877).
- The ring forms of (CUT-TH) as targets: rejected; they add a flux statement on the ring and fail frozen Z_2, Q_8 and 2T (row 910, check 911 after wording correction).

Comparisons:
- (E17), HA, (C2), EXC, EXC-W and (DRESS) ask for a rate or an area law that the seed chain does not need (row 892). Whether (CORE) is strictly weaker than (E17) is open (check 893).
- The relative nodes (FUSE-E), (KURT), (HB) are incomparable with (CORE); each buys (CORE) with a stronger GLUE (row 892).
- (TS-theta) is off the critical path (row 892, ARGUED).
- (UNIV-FP) does not follow from the account (row 904, unchecked).
- The glue half is a pure even-sector mixing statement, but every proved seed proves both halves or neither, because untwisted free energies determine S and never S_ev (Remark UNTW, row 895; HOLDS AFTER CORRECTION, check 896).

### 5.4 Where every form stops

All forms stop inside the order-one band at a box of a few correlation lengths, where (SEED-FP) sits (rows 859, 863, 892). Row 892 states the common stop: at the seed scale the centre vortex of SU(2) is thick and light. Its stage 2 stops at (S1); its stage 3 stops at (HB) (row 892).

## 6. The walls, their stopping reasons and the shared assumptions

Source: row 899 (`library/gap-wall-assume-max.md`, Claude Fable 5.2 max) and its check 901 (Codex astra xhigh). Row 899 is the assumptions exercise run once on five walls. Check 901 holds its proved lemmas and holds SA1-SA5 and the "five ways to one comparison" reading after scope and premise corrections; it fails SA6 as stated (section 6.2).

### 6.1 The five walls

**W1. Background-uniform layer bounds fail above 4 G_3 = 1.0109** (rows 834, 839; checks 849, 857).
- Stopping reason: at the flat background the Frohlich-Simon-Spencer infrared bound makes every background-uniform one-layer twist bound false above 1.0109 (Proposition TB2, row 839, check 849 after correction).
- Scope: a theorem about one point of the background space, the flat pair, at one layer; group-blind and action-robust; it blocks suprema (row 899, Step 1.4).
- Does not block: bounds that are not uniform over backgrounds; thick slabs; a different conditioning variable (row 899). Proposition W1-t (PROVED, check 901) adds a ladder: a background-uniform slab bound of thickness t is false wherever the flat Dirichlet slab orders, since kappa_t is at least gbar^2/64. Sufficiency is OPEN. GUIDE at beta 2.3 puts the critical thickness near the deconfinement length (row 899).

**W2. The annealed condition (AN1) is the worst case in disguise** (row 845, check 852).
- Stopping reason: literal (AN1) lets an adversary freeze the exterior and resample one block for ever, so moments see the essential supremum (check 852; row 899 Step 2.4).
- Does not block: label-path sums over the random schedule, region-charged Peierls bounds, signed or vector L^2 forms, Lyapunov weights (row 899). Check 852 names the open repair: conditions only on surviving path sums. None of these doors has a supplier, and each gives clustering only, with W3 behind it (row 899).

**W3. Clustering cannot give the flux half** (row 859, check 882).
- Stopping reason: the tube-conditioned twist covariance is the variance of a conserved Z_2 charge at every separation (row 859, check 882 HOLDS). The proof needs the conserved charge, so it needs the torus, which the consumer forces (row 899).
- Does not block: the same number seen along the coupling, as a variational quantity in the crossed frame, or as an even thermal density of long tubes (row 899, Step 3.4). It blocks state clustering, not a comparison theorem (row 899, ARGUED; holds after correction, check 901). The comparison form is the lane's Proposition MIX of row 708 (row 899).

**W4. Path counting fails at the real spin densities** (rows 859, 887; checks 882, 891).
- What is established: row 859's strand threshold FAILS (check 882). Row 887's filling-Peierls barrier (P(half-integer edge) below about 1/9 needed, GUIDE 0.33) holds after correction (check 891). As a theorem W4 is arithmetic on two majorants with GUIDE densities (row 899).
- Structural content: Lemma W4-uni (PROVED, check 901): uniform cycles and boundaries have the same law in every box, so no one-box label event decides the class at maximal density.
- Does not block: a coarse electric variable; signed methods; a different scale (row 899). Check 891 also fails the universal exclusion of typical-field conditioning and the all-Peierls exclusion, so those doors stay open.

**W5. (KURT) and (WALL)_40 are the hard problem in disguise** (rows 886, 894; checks 889, 897).
- Stopping reason: under GLUE, (WALL)_40 is exactly kappa at least 2, so it is not an easier node than (KURT) (Proposition D, row 894, check 897). The abstract class cannot give kappa: there are in-class counterexamples with kappa = 1 and heavy flux (row 886, check 889 after correction; row 894, check 897).
- Does not block: a proof that uses locality and transverse extent. The sufficient floor is kappa at least 1.66 (Corollary K', check 897). GUIDE: one tube has kappa 1.53 at beta 2.3, so the floor must come from transverse extent (row 894).

### 6.2 The shared assumptions (row 899, check 901)

- **SA1. The arena is the unit lattice at one order-one beta_W, in bare variables** (W1, W2, W4, W5), while the real object is first passage. Breaking it needs block variables at the correlation length, and the account gives neither a block law nor a transfer operator there (row 899). HOLDS AFTER CORRECTION (check 901).
- **SA2. Uniformity in a conditioning variable** (W1, W2, W5), with different extremal points: the flat background for the layer twist, the zero field for the single-site response (row 899). HOLDS AFTER CORRECTION (check 901).
- **SA3. Absolute values**, where the true quantity is a likelihood-ratio mean with heavy cancellation (W1, W2, W4) (Lemma W1-abs, identity (PAR); row 899). HOLDS AFTER CORRECTION (check 901). (VAR-SLAB) is the one concrete signed form (row 899).
- **SA4. The torus and its conserved centre charge**, forced by the consumer (W3, W5) (row 899). HOLDS for the named torus consumer (check 901).
- **SA5. One coupling** (all five). Breaking it is prior lane work: Theorem D-shape, Lemma M and Proposition MIX of row 708, with open inputs (NOCRIT), (VIR-log), (BOOT_eps) (row 899). HOLDS AFTER CORRECTION (check 901).
- **SA6. Every wall's proof is group-blind**, so SU(2) enters only through what the walls leave open; in each table that is the vacuum's response to a thick centre vortex (row 899). Check 901: the statement for every compact group with a centre FAILS. The walls' proofs use no SU(2)-specific input (rows 834, 839, 845, 859, 894), but the blanket claim over all centred compact groups is not established.

### 6.3 The reading that joins them

The five walls close five ways of proving one statement: a comparison of two symmetric Gibbs laws at one plaquette, the content of Proposition MIX (row 899, ARGUED; holds after scope and premise corrections, check 901). W1 closes it by a background-uniform layer bound; W2 by block moments quantified over all schedules; W3 says that state clustering is not a comparison; W4 closes the electric route by supports; W5 closes the route through abstract regularity of the flux ground function (row 899).

### 6.4 Other walls of this round and what they leave open

- Single-link tree gauges stop at 1/3 (row 835, check 840); vertex blocks with worst-case single-link responses stop at 0.775 (row 836, check 841). The 0.775 cap bounds one family of majorants, not every block method (row 861). Exterior-uniform or annealed responses of blocks larger than the correlation length stay open (row 836).
- Normalized softening supplies no seed (row 861, check 877). It leaves open exact steps whose landing is proved by other means (EXIT, rows 846, 861).
- Reflection positivity across the free axis gives only a void image inequality (row 907, check 909). It leaves open one-sided substitutes that do not dominate by an operator bound R at least kappa Q (row 907).
- Doubling is not structural: reflection positivity, integrality, super-multiplicativity, axis exchange and homogeneous Holder or chessboard bounds all survive a direct sum and cannot prove (H-DBL) (row 910, check 911). It leaves open a quantitative single-phase input (row 910).
- The account's universality does not give (UNIV-FP) (row 904, unchecked). It leaves open a comparison of full unnormalized measures on several tori for weights that differ on large fields, uniform in K (row 904).

## 7. Live attacks and their exact next statements

Each attack names its next statement, what would close it, and what has been tried. None has a proved step at order-one coupling.

### 7.1 The free-wall engine and (JOIN-TH)

- **Set-up.** Replace the torus consumer by boxes with periodic time and free space walls (row 898). Free space walls carry no centre sector and no twist; each plane flip is a gauge transformation (FW1, row 898, check 902). So the flux half and the twist disappear from the consumer, and the Q_8/2T test does not apply in its periodic form (row 898; check 902 fails the broader fact-test endorsements, section 4 item 28).
- **Next statement.** (JOIN-TH_kappa) for Wilson SU(2) at order one: on cold free-wall boxes B, the thermal excess of the joining free energy of two boxes, F_join(a; B) - a J_0(B), is at most kappa g(a; B) with kappa an absolute constant (Lemma J, row 910, check 911). Row 910 adds the input such a proof needs: a quantitative single-phase statement, no second sector whose vacuum comes within a thermal energy at the next scale, and walls that do not prefer a heavier phase (row 910).
- **What would close it.** (JOIN-TH_(k-2)) gives the doubling bound with constant k (Lemma J). The doubling bound on cold boxes and a seed S(a; B) at most 1/(3k^4) at one cold box give the gap on dyadic cubes (Theorems C and C', rows 907, 910; checks 909, 911). The limit-state node from the free-wall engine to (GAP) is OPEN (row 907).
- **Tried.** The free massive scalar passes (WALL-1) with C_1 = 1 and (WALL-2) with C_2 = 1/floor(2b/a) (row 903, check 906), so the free field does not kill the engine; its proof uses an image identity that Wilson lacks (row 903). Reflection positivity across planes perpendicular to the free axis gives only a void image inequality (row 907, check 909). The ring forms of (CUT-TH) add a flux statement and fail the frozen-group tests (row 910, check 911). (H-W), (H-tau) is only a sufficient split (row 910). Doubling is not structural (Theorems 2P, 2P', Lemma DS; row 910, check 911). The join excess is positive at small beta at fixed sizes, so k = 2 is not available (row 910, check 911). On free walls the doubling carries a new input at every scale that the seed does not imply (row 910).
- **Fact tests.** The engine fails for U(1) through the seed (row 907). Compact U(1) just above its transition should fail the doubling at a wall-induced crossover scale (row 910, ARGUED).

### 7.2 Transport forms THERM-DI-beta and THERM-DI-pin

- **Set-up.** Carry a seed from the proved range near beta 0.36 into the band by a box-uniform mean transport inequality dX/d(parameter) at most -C a dX/da, with C uniform in the box (rows 898, 905).
- **Next statements** (check 908 of row 905). THERM-DI-beta: on the coupling path, for X the centre-even thermal sum, a box-uniform constant C on [0.3609, beta_1], still subject to the Q_8/2T test. THERM-DI-pin: on the full-trace pin path, with the starting seed X at most 64 delta_n supplied; at h = 0 the full trace carries every electric-flux sector, so this route proves glue plus flux, not glue only (check 908).
- **What would close it.** THERM-DI-beta gives (GLUE-1), S_ev(a; b^3) at most 1/10 at one coupling in the band (rows 898, 905). THERM-DI-pin gives the whole seed at that coupling (check 908). Both live on the bare Wilson window, not on first passage (row 895, Proposition TR), so a weight comparison or hand-off is still needed (row 837).
- **Tried.** A closing sector forces a divergent all-time transport cost (S1, row 905, check 908, conditional on an all-time hypothesis on one invariant spectral family), which is the selectivity mechanism. The literal centre-even pin path is invalid: centre flips do not commute with the spatial pin terms (S2, rows 902, 905, 908). No constant is supplied on any subinterval of (0, 78 beta_1] or [beta_0, beta_1], and none is refuted (S4, check 908). Row 710's bound carries a volume term (check 908). Proposition TR holds as a conditional comparison: an even level with a uniform positive starting energy that tends to zero later along growing boxes rules out a uniform finite C (row 895, check 896).

### 7.3 (VAR-SLAB) with (FR) and the Langevin gap

- **Set-up.** For the half-torus slab twist ratio rho under the two-slice law: E[rho^2] = 1, Var(rho) = 4p(1-p), p/(1-2p) = E_tw[sinh^2(X/2)] with X = log rho, and 4p(1-p) at most E[|grad X|^2]/lambda (row 899, check 901). It is a positive form with no cancellation, quadratic in a local response, at one coupling, with no supremum over boundary slices (row 899).
- **Next statements** (row 899, Step 7.2). (FR): for the 6|B| boundary links b, E_w[|Delta G_b|^2] at most eps^2, where Delta G_b is the change of the mean boundary force at b when the opposite boundary slice, at time distance a/2, is centre-flipped. Then p(1-p) at most (3|B|/(2 lambda)) eps^2. And lambda, the gauge-invariant Langevin gap, at order one.
- **What would close it.** (FR) with small eps and lambda bounded below give the flux half at one coupling (row 899, check 901). For p at most 1e-4 on a 20^3 box this needs eps about 9e-5 lambda^(1/2) (row 899, GUIDE arithmetic). The glue half is still needed separately.
- **Tried.** The author could not bound E|grad X|^2 below its trivial size at order one. The natural route, covariance decay inside the slab, returns the flux energy and only the spectral inequality S_-(a) at most S_-(a/2)^2 (row 899, Step 7.4). lambda is proved below beta_W 1/4, and below 8/27 on some tori (row 899, citing row 837); Theorem R of row 836 gives a Langevin gap wherever (BC) holds, so below 0.3609 (rows 836, 841). lambda at order one sits behind W2 (row 899).
- **Fact tests.** U(1) Coulomb fails in both factors: p stays away from 0 and the Langevin gap tends to 0. Ordered Z_2, frozen Q_8 and 2T have p near 1/2 (row 899).

### 7.4 EXC and (DRESS)

- **Next statement** (check 881). An order-L_i lower bound, at least -theta gamma_min L_i with theta below 1, uniform over tori, twists and b, on the boosted-minus-unboosted, odd-minus-all magnetic-cut plaquette response integrated over b in [0, beta]. The available bound is 4 beta n, of order a^3 (check 881). In row 888's terms: (DRESS), a positive order-L_i excess of half-integer spin at least 5/2 temporal plaquettes on the fundamental flux sheet at isotropic coupling, and (EMPTY) for the boosted model, with a uniform small-b expansion through b* (row 888).
- **What would close it.** EXC with c_0 at least g gives (E17) with eta_* = e^(-2c_0) (rows 872, 873). (E17) gives (FQ) at fixed coupling (row 892), and chain I then needs GLUE and the physical form (rows 837, 865, 868).
- **Tried.** The electric-only reference has a positive boost response gamma about 0.010 at beta 2.3, of order L_i, but group-blind: the same argument passes for U(1), Q_8, 2T and Z_2 references; the margin is thin (check 881). Large boosts reverse the sign at fixed volume when the cut-crossing edge count is even (rows 875, 881). The natural endpoint has a negative single-link kernel, k_S(-I) below -163/660 on [2.3, 2.6] (rows 875, 881). At b = 0, R''(0) = 4 L_i pi_5 (D_(5/2) - D_(1/2)), about -20 gamma L_i (Theorem 3.3, row 888, check 890). The unboosted model has finite flux tension on every torus and twist (Theorem 9.3, row 888, check 890). The carrier crossing and erasure argued by row 888 do not follow from the second-order data (check 890). (DRESS) is not equivalent to pointwise EXC-W (edge 10, check 893). The spin-5/2 filter is SU(2)-specific (check 864).

### 7.5 The decoder: (SEED-DEC-U) and (S1)

- **Next statements** (row 887, check 891). (SEED-DEC-U): 64 P(a box of half the torus side is unclean) at most (K/8) sqrt(S_ev), for every magnetic background, with the domain check 891 states. Its carrying input (S1): a low-density short-range noise model for the SU(2) one-slice law, that is, a local perimeter law for the equal-time 't Hooft functional. A group-blind second input (S2): rigidity of minimal fillings at density 0.12 to 0.17, a zero-temperature 3D +-J Ising question (row 887). In row 892's sheet form, (S1) is a perimeter law for the open thin vortex sheet with area coefficient below 1/(25 b^2), which gives (VF) and so (CORE) (row 892).
- **What would close it.** (SEED-DEC-U) reaches the (FQ) consumer (row 887). (SEED-DEC-H), z_0 below 8.93e-7, reaches chain II at fixed coupling through SPLIT, with GLUE (row 892).
- **Tried.** (TOP_j) proved in an exact form, with eight classes and ratio ten (check 891); ratio 4 fails by a period-8 snake, 5 to 9 undecided (row 887). The same-class recursion holds with C_3 = 1,120,616 under the chessboard estimate (check 891). Selectivity holds by contraposition: P(unclean) at least 7/512 for frozen Z_2, at least 1/(64 N_G) for frozen Q_8 and 2T (check 891). Identity (PAR): the parity cycle's law is a signed mixture, with Gauss's law carried by negative timelike plaquette traces (check 891). A filling-Peierls count needs P(half-integer edge) below about 1/9, against GUIDE 0.33 (check 891 after correction). The universal exclusion of typical-field conditioning FAILS (check 891), so that door is open. RIG is unfinished (check 891).

### 7.6 The (KURT) floor 1.66

- **Next statement** (rows 894, 897). For 4D SU(2) at one SH box (b at least 24 a, a at least 82) in the band: the flux ground function g = Psi_chi/Omega has fourth moment kappa at least 1.66 (kappa as defined in rows 876 and 886). Equivalently, exclude a near-bit with kappa at most 1.13 that is the only light level of its sector (Lemma B4, Proposition B5, row 894, check 897).
- **What would close it.** With GLUE at the level of Corollary K', kappa at least 1.66 gives (CORE), the SH seed and the gap on every larger cube (rows 892, 894; checks 893, 897).
- **Tried.** The moment hierarchy and the symmetry theorems (row 886, check 889): kappa at least 3/2 when the flip lies on a circle of symmetries (U(1); at least 2 for the O(4) vector multiplet), a mechanism absent for SU(2), Q_8, 2T and Z_2. Counterexamples with kappa = 1 and heavy flux (rows 886, 894; checks 889, 897), so (KURT) does not follow from transfer-operator structure. Exact 2D values: SU(2) 2, Q_8 4, U(1) 3/2, Z_2 1 (check 897). GUIDE: one tube has kappa 1.53 at beta 2.3, so the floor must come from transverse extent (row 894). The hidden-bit converse FAILS (check 889); the Z_2 topological-order reading FAILS (check 897). Row 892 suggests deciding the statement first in the weakly coupled small box, where the wall is the trace-zero holonomy of the toron valley (row 892, Step 8.4).

### 7.7 The glue half (GLUE-FP)

- **Next statement** (row 895, Lemma G5, check 896 HOLDS). (Z0): m_ev((24a)^3) a at least 2[110592 G + log(1/sigma)], together with (COUNT): g(a/2; a^3) at most G, at the seed scale, uniformly in the cutoff. Transport form: (BETA)_C on [0.3609, beta_1], on the bare Wilson window (row 895, Proposition TR as a conditional comparison, check 896).
- **What would close it.** (GLUE-FP)_sigma at the level a flux node needs: 1/10 for (CORE) (row 892), 160^(-16) for Proposition W (row 892), the Corollary K' level for kappa 1.66 (row 894). Every proved seed proves both halves or neither, since untwisted free energies determine S and never S_ev (Remark UNTW, row 895, after correction by check 896).
- **Tried.** The glue half is a pure even-sector mixing statement, the bulk mass gap of local observables at one size (row 895; SEP holds after correction, check 896). Lemma LOC holds for its support condition, but its claim that even-sector block criteria inherit the ceilings 1/3, 0.3609 and 0.775 does not follow (check 896). Lemma MC holds: averaged block conditions are the worst case (check 896). Lemma CS holds, but its exclusion of other methods FAILS (check 896). Row 863: the Hopf bound on the fixed-box gap, 2 exp(-6 beta_t #B), is extensive, so it gives nothing at seed size; Lemma A2 seeds the model with only time-like orientations at every beta_t (check 879 after correction). Row 895 names four stops: the vacuum functional is not known to be local; local-to-global methods read finite blocks where averaging is the worst case; global exact inequalities point the wrong way; transport uniformity is the absence of a critical point. Row 863's suggested side targets: (KS-ZONE), a uniform gap and seed for beta_s beta_t below an absolute constant with beta_t free, and (INC-FP), the glue half as a bridge-form Poincare inequality (row 863). No tool is named for the glue half at order one (rows 892, 895).

### 7.8 Other open items that stay live

- Theorem S1 on the twisted thin torus: every M above M_1(n, beta), odd M, the constants of CH, a lower bound on the Z_2 string tension (row 862, check 880).
- (E17-phys-CA) itself, and the literal continuum-kernel identification (rows 865, 868).
- EXIT, the order-one hand-off from first passage (rows 846, 850, 861, 877).
- HA off the real axis: plausible on the real segment as an area law for the odd electric-flux fraction, unassessed off it, strictly stronger than (E17) (check 870).
- (HS) and (LS) beyond row 860's interval; (LS) equals (E17) (check 864).
- Full compact-Villain (TS-theta) and its nonzero-background Z_2 extension (check 884), off the critical path (row 892).
- (SE) for the area law past 2/3, and a nonlinear diamagnetic inequality for O(4) spins in SO(4) backgrounds beyond 0.7385 (rows 834, 857).
- (RTAIL-BR) on (6/25, 3/10] and surfaces outside G_** above 3/10 (rows 833, 847).
- The marginal-dimension method needs a positive geometric representation that SU(2)'s signed surface expansion lacks (rows 878, 885).

## 8. Stopped attacks and why

A stop records a named reason at a named step. It does not say that the target is false.

- **(UNIV-FP), attack 2 of row 898** (row 904, unchecked). The account's fixed-horizon universality (YM4_1400 L94031-94510) compares two bare weights only for profiles in a fixed ball, at one frozen endpoint, on normalized final regular laws on one fixed volume; it leaves out large-field histories and vacuum factors and is not uniform over growing volumes (row 904, READ). A mixed weight with fixed beta_F is not covered, and both of its forms lose the Wilson large-field small factor (row 904, ARGUED). On row 898's unchecked multiplet premise the mixed weight's plain seed is about 7, so a seed difference below s_*/2 is false for that pair (row 904). Row 898's stop condition applied, and attack 2 stopped (row 904). With it the follow-on steps (FLUX-Z2) and (MULTIPLET) did not run (rows 898, 904); check 902 found unrestricted (FLUX-Z2) false. What is missing: a comparison of full unnormalized measures on several tori for weights that differ on large fields, uniform in K, and a large-field ledger in which x_0 does not suppress vortices (row 904).
- **Attack 3 in its literal form** (row 905). The even-sector pin path has no conserved pure-gauge even sector (rows 902, 905, 908). Check 908 overrides row 905's verdict that attack 3 does not survive: two forms stay live (section 7.2).
- **Reflection positivity across the free axis as the route to (WALL-2)** (row 907, check 909). It gives only convexity, monotonicity, FW6 and an image inequality whose defect is at least delta_e(1), so the bound is void; the same holds for every operator bound R at least kappa Q (row 907).
- **(CUT-TH) with a ring sum** (row 910, check 911). Both ring forms add a flux statement on the ring and fail frozen Z_2, Q_8 and 2T; the doubling is attacked as (JOIN-TH) instead (row 910).
- **The pure-exterior form (SP-ext) of the annealed conversion** (row 845, check 852). Nontrivial (SP-ext) with eps below 1 fails under repeated block updates. The open repair conditions only on surviving path sums, which lack a model-specific supplier (check 852).
- **The filter split (HS) then (LS)** (row 860). (HS) is proved on [2.15, 2.5] and is the wrong target: (LS) equals (E17) up to e^(-c#E), so the split removes nothing (row 860, check 864). The filter itself continues as EXC (section 7.4).
- **Soft block steps then Theorem HO** (row 861, check 877). The vacuum constant of any exact step is F_T - log Z_T, so normalized softening alone supplies no seed. Pinned block mixing is proved only for noise above 6 beta + 18 beta e^m, which lands only for beta below about 0.0384 (row 861; check 877 corrects the threshold to 1/sqrt(216 pi)).
- **The literal slab route to the seed** (row 835, check 840). Lemma HR puts the torus comparison in the spatial-link marginals, and Proposition NG shows slab blocks with Lemma SC never beat 2/9. Gauge invariance moved the seed to 1/3 instead.
- **The area law beyond 2/3 by single-site, in-slab gauge or decimated Dobrushin** (row 834, check 857). The slab law has only global symmetries; the single-site coefficients are exactly (beta/4) times adjacency; the in-star return is exactly 2/3. A2 depends on (SE), and the value tau_* = 1/4 is false on C5 (check 857).
- **Compression and information theory as a handle on the seed** (row 839, check 849). The candidates are group-blind or restate the seed. Check 849 notes that no blanket information-theoretic no-go is established.
- **Fresh-framing exercises on the current inventory** (row 878). The fresh pass re-derived row 859's idea list almost one for one. Lead decision: no further fresh-framing exercise runs on this inventory until a new input lands (row 878).
- **Row 858's planned route M** (row 900). Its sign gives upper bounds only, it holds for U(1), and its usable form is already (MON') and (AF-step) (row 900, unchecked).
- **Link-tilt localization; convexity along doublings** (row 878). Killed: the hypothesis of the first contains the target; the sign condition of the second is false in the class (row 878; check 884 does not address these).
- **Fable runs stopped by process events** (rows 858, 859, 861, 862, 863). All five stopped at 03:06Z when the lead's turn was interrupted. They could not be resumed and were relaunched about 06:20Z from their saved files (rows 858-863). Row 858 then stopped a second time on an API safeguards flag; its fresh replacement is row 878 (row 858). Row 859's resume also stopped on a safeguards flag and was finished on Claude Opus 5.5 max; a fresh Fable brainstorm ran as row 876 (row 859). These are process stops, not mathematical ones (section 9).

## 9. Process lessons from this round, stated as rules

1. **Write as you go.** A max-effort lane creates its file on its first call with the plan, then appends one step per response. The lead checks that the file grows. Reason: rows 834 and 842 were relaunched after two output-cap losses each (rows 834, 842); later briefs carry this save protocol (rows 858-911).
2. **A lead interrupt must not kill a lane.** Run long lanes so that an interrupt of the lead's turn cannot stop them, and check for live subagents before an interrupt. Reason: five Fable lanes stopped at 03:06Z as a side effect of an interrupt of the lead's turn, not an owner decision, and could not be resumed (rows 858, 859, 861, 862, 863).
3. **After a safeguard stop, relaunch fresh; do not resume.** Give the fresh run the saved file as input, without resume framing. Reason: the resume requests of rows 858 and 859 were stopped by the API's safeguards (flag reasoning_extraction); row 878 ran fresh and finished. Rows 863 and 886 each had one response withheld by a safety classifier after a step was on disk, so the save protocol limited the loss to one step (rows 863, 886).
4. **One output path per row.** A relaunched or resumed row writes to a file name that no older row owns. Check a file's provenance before reading it as a row's output. Reason: `library/gap-crux-exercise-max.md` is row 743's original 60-line file, which the Mini relay re-pushes; row 858's own partial is `library/gap-crux-exercise-r858-max.md` (row 858).
5. **Mine every stopped partial before planning the next lanes.** Reason: no later lane had read Steps 2-4 of row 858's partial; row 900 found 7 untouched items there (row 900).
6. **Queue work on the idle runner.** Move a queued item to whichever runner is idle, and use an allowance before it expires. Reason: row 866 moved from the laptop to the Mini to start at once and to use the Mini's last weekly Codex allowance (row 866).
7. **Check negative claims as hard as positive ones.** A "cannot", "no route" or exclusion claim gets a line-by-line check before any decision rests on it. Reason: checks reversed the negative verdicts of rows 860 (V1, check 864), 872 (check 873) and 888 (check 890), and the exclusions of rows 887 (check 891), 867 (check 869) and 895 (check 896).
8. **"X is weaker than Y" needs both directions.** State the direction that is proved, and mark the other OPEN. Reason: row 871's (C2), row 876's (KURT) and row 892's (CORE) were each called weaker than (E17) or (LOC); checks 874, 883 and 893 found the weakening not established or false.
9. **Check fact-test verdicts against prior checked rows before recording them.** Reason: row 895's frozen Q_8/2T PASS contradicted prior work (check 896); row 898's three endorsements failed (check 902); row 878's Coulomb theta = 4 and its Q_8/2T exemption failed (check 884).
10. **Validate a GUIDE sampler before quoting it.** Show that the sampler's kernel preserves the target law. Reason: row 867's N_t = 3 sampler had an invalid update partition, so fact test T3 supported nothing (check 869).
11. **Read a literature input in the primary source.** Mark a recalled statement as recalled and do not let it carry a step. Reason: several recalled literature claims of row 839 failed (check 849); row 834's recalled O(4) Simon-Lieb star range is unverified (check 857); Ginibre's text could not be read (check 869).
12. **A port names the complete-account line it matches.** Reason: row 844's port rested on the outline (check 848); row 865 redid it on CA-I Theorem 0 (iv) and passed check 868.
13. **Lead decisions wait for the check, or are marked provisional.** Reason: row 842's lead adopted (S1-loc) and (S1-T) on arguments W1 and W2, which check 856 failed; row 887's lead decision on (SEED-DEC-H) was corrected by row 892.
14. **The checker recomputes every worked example and constant.** Reason: row 846's n = 226 example and 0.0042 radius failed (check 850); row 861's STEP threshold was corrected (check 877); row 836's a = 360 remark is uncertified (check 841); row 834's tau_* = 1/4 is false on C5 (check 857).
15. **Briefs give absolute source paths; a "does not occur" claim gives its grep.** Reason: row 898's author could not find YM4_1400.tex, which is at `/Users/jonreilly/ym4d-lead/sa1400/YM4_1400.tex` (row 898); row 878's claim that "heat kernel" does not occur there is wrong (row 900).
16. **Record what a check reuses and who wrote it.** A check is independent only across provider or derivation. Reason: check 868 is not independent for the parts reused from row 844 (both Opus); row 863's comparison with earlier rows is a second sample of one model family, not a check (row 863); Theorem SH's check (row 707) is by the author's model family (row 892).
17. **Record failed reads and downloads.** Reason: the arXiv download of row 885 failed on DNS and the papers were read through a web reader (row 885); Ginibre's text could not be read (check 869).

RESULT: The chain from the Sussman-Alpoge first-passage action to the continuum mass gap is in place, with two argued and unchecked links (steps (c) and (e) of row 837), up to one missing input, the seed (SEED-FP) at one physical size at order-one coupling, which splits into a glue half and the flux half (CORE), and no row of 833-911 proves either half above the checked strong-coupling range beta_W below 0.3609 (rows 836, 837, 841, 892, 893). Checks overturned or corrected 33 claims this round, among them every "weaker than" claim of rows 871, 876 and 892 and the negative verdicts of rows 860, 872, 888 and 905; the live attacks are the free-wall engine through (JOIN-TH), THERM-DI-beta and THERM-DI-pin, (VAR-SLAB) with (FR) and the Langevin gap, EXC with (DRESS), the decoder (SEED-DEC-U) with (S1), the kappa floor 1.66 and (GLUE-FP), while (UNIV-FP) stopped at row 904.
