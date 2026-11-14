# FINISH row 892, gap-crux-core-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone commit: 9add61ac36cdac3db031bcb368c6273f1bf58f46 (/Users/jonreilly/ym4d-lead/clone, pulled ff-only, already up to date).
Author: Claude Fable 5.2, max effort, FINISH row 892. Hand work only. No repository file edited.
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Labels: PROVED (mine, here), READ (path and line), ARGUED, GUIDE, OPEN.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for their account; Balaban for his estimates.

## Target

Synthesis of the night's crux forms (FINISH rows 860 to 891) for a mass gap in 4D SU(2) lattice Yang-Mills.
Then an attack on the weakest statement that still reaches the consumer with a cutoff-uniform rate.

## Plan (one step per response; each step is appended here before the next starts)

1. Read FINISH rows 860 to 891 (RESULT text and check verdicts). Record each node's exact statement and its status.
2. Read the consumer statements (FQ), (F-h), FUSE-suff (D/library/gap-es1-opus.md 200-236) and the finish line (SEED-FP) (D/library/gap-finishline-opus.md 110-160). Read the fact-test rows 786, 838, 839, 843, 845.
3. Build the implication graph: edges with labels (PROVED, READ, ARGUED, unknown), checked or unchecked, and which nodes reach the consumer.
4. Apply the fact tests to each sufficient node. Choose the weakest sufficient statement. Compare it with (E17).
5. State the crux lemma of the chosen statement exactly. Attack stage 1.
6. Attack stage 2 (continue, or record where stage 1 stopped and which node it hit).
7. Attack stage 3, or move to the next-weakest candidate if the attack stopped at a graph node.
8. Final: compact graph table, chosen statement, how far the attack got, the single next statement. RESULT line.

## Step 1a. Rows 860 to 867 (READ D/FINISH.md lines 937-944)

- 860 gap-hs-max (Fable max; checked by 864). Theorem HS HOLDS (864): electric-energy bound through one transfer step, group-blind (verbatim for U(1), Q_8, 2T, 2O, 2I). P1, P2 HOLD (864): (LS) equals (E17) up to e^(-c#E); P_- is exactly the event that the half-integer Z_2-cycle of a slice has odd omega-class. Parity form of (E17): that event has probability at most C a^p eta_*^(a/2). OPEN. GUIDE: spin-2 density 2e-5 at beta 2.3; half-integer edge density about 0.33 (cycle plausibly percolates, no Peierls count).
- 864 check (astra xhigh). HOLDS: HS, HS-2, P1, P2. HOLDS AFTER CORRECTION: HS-1, OS, DS, DS-1, DS-2, P3, B1. FAILS: V1 (the U(1) argument that the filter plus (HS) cannot force (LS)); U(1) fails the spin-5/2 filter bound on Sym^5 V (norm at least I_1/I_0). So the filter is NOT ruled out as an input. (E17) OPEN.
- 861 gap-exit-max (Fable max; check 877). Proposition FREE (soft block step gives the zone's per-link size for free, also for U(1)). PIN-MIX proved only for noise a above 6 beta + 18 beta e^m (lands only beta below 0.0384). Proposition VAC (vacuum constant of any exact step = F_T - log Z_T, so soft step then Theorem HO is circular). Theorem HL plus (6.3): the seed reduces to torus comparison of local means along a path, proved b below 0.3609 and a above 24 beta. OPEN crux: (PATH) and PIN-MIX: torus comparison of local means from 0.361 to the band 2.3-2.6; no inequality found that avoids a sup over environments and fails for U(1).
- 862 gap-pe-max (Fable max; check 880). Lemma PE as printed FALSE in (S1-T) clause. Window theorems A, B at weak coupling on twisted thin torus, even M up to M_1. Off the order-one crux. OPEN: M above M_1, a lower bound on the Z_2 string tension.
- 863 gap-crux-skeleton-max (Fable max; check 879). Three attacks stop at the same statement: (SHIFT) = (PATH)/Proposition MIX; (INC) = (M5-G); (TORUS) = (SEED)/Proposition Delta. PROVED: A2 (time-like-only model seeded at every beta_t), B1 (two-slice law is the Schroedinger bridge of the electric orbit kernel and the slice law), B2 (Hopf fixed-box gap at least 2 exp(-6 beta_t #B), extensive), T2 (cut-and-reglue identity). OPEN: glue and flux halves at one physical size; (BASE-Phi). Next named: (KS-ZONE), (INC-FP).
- 865 gap-sdcyl-ca-astra (astra xhigh port; check 868). Conditional: (SD-cyl-CA) gives rho_CA = c_K/(3 C_K); corrected (E17-phys-CA) at rate log(3 C_K/c_K)/(3d) implies (FQ) with cutoff-independent K_F. OPEN: continuum-kernel identification, the account's analytic suppliers, flux and glue estimates.
- 866 gap-z2parity-astra (astra max; check 870). (E17) is exactly the slice-homology parity problem. PROVED: marked area-order zero; relative homological analyticity (HA) of the centre-odd marker implies the parity bound. HA is OPEN and STRONGER than the parity bound. HA fails for Z_2 at beta 5/2 and in a background-uniform SU(2) version. A bound uniform in the environment is false (explicit finite-beta Z_2 test); an averaged inequality is not refuted. Next: averaged relative bound in HA by summing contractible decorations before absolute values.
- 867 gap-sep-opus (Opus max; check 869). Lemma QS: e_(1/2) at most r_(1/2)(5 beta)^4 (0.5806 at 2.3). Proposition TL: the parity of any edge set is a 't Hooft loop, E[(-1)^N_h(R)] = Z(flip R)/Z; so the parity statement IS the wrapping 't Hooft surface. NEW FACT TEST T3 (GUIDE plus Borgs-Seiler recalled): the deconfined N_t = 3 state at 2.3 has the same one-slice local law within 1.5 percent; so no bound on the one-slice law of bounded sets uniform in t can force (E17). A carrying input must fail at short periods, as (SEED-FP) does by its cube shape.

## Step 1b. Rows 868 to 875 (READ D/FINISH.md lines 945-952)

- 868 check of 865 (Opus high). All six statements HOLD. (E17-phys-CA) implies (FQ) with K(a) = K_F cutoff-independent. Conditional on the account's (h1)-(h3) kernel comparison and hypotheses. (E17-phys-CA) OPEN. Not independent for parts reused from 844.
- 869 check of 867 (astra xhigh). HOLDS AFTER REPAIRS: Lemma QS, Proposition TL (with the dual-surface qualification), SEP(b) (certified separation 0.0359). FAILS: the six-candidate exclusion, and fact test T3 as stated (N_t = 3 sampler invalid; Borgs-Seiler mismatch). So T3 is NOT established.
- 870 check of 866 (Opus high). HOLDS: (E17) is the slice-homology parity problem; marked area-order zero; HA implies (E17) with area gain; a zero-free disc implies HA; Z_2 Peierls test refuting an environment-uniform conditional bound (beta above 2.191); HA fails for Z_2 at 5/2 and in background-uniform SU(2). HA is strictly stronger than (E17): an order-one confinement statement (area law for the odd electric-flux fraction). HA passes the U(1) Coulomb test as a target (ARGUED). The note's proved steps are group-blind.
- 871 gap-ha-astra (astra max; check 874). Interpolating measures mu_(k,lambda) (each plaquette weight 1 + lambda eta t_p); response R_(m,v)(lambda) = E S_m - E S_(m+v) (R1); deficit F(1) = integral of R over [0,1] (R2). (C1): the part near 0 is proved small. (C2): integral of |R| over [lambda_0, 1] at most C a^p e^(-ga). (D3) is equivalent to HA after shrinking its disc.
- 874 check of 871 (Opus high). HOLDS: S1-S6. (C1) holds with rho = e tanh(beta)/6 below 1/2; F at least 0 by transfer positivity. CORRECTION: (C2) is NOT weaker than (E17): (C2)+(C1) implies (E17); (E17) implies (C2) only if the response has a sign (F monotone in lambda, unproved). So (C2) restates (E17) or is strictly stronger. (C2) passes U(1) Coulomb (ARGUED), Z_2 at 5/2 and frozen 2T (PROVED) as a target.
- 872 gap-filter-ls-opus (Opus max; check 873). Proposition EXP HOLDS (873): d log Tr(P L(s)^t)/d log s = t times the one-slice count of high-spin edges, any group and spin set. EXC: integral of Delta(s) ds/s at least c_0, Delta = Cov(N_hi, 1_odd)/p. EXC implies (E17) with eta_* = e^(-2 c_0) (HOLDS AFTER CORRECTION on the consumer rate).
- 873 check of 872 (astra xhigh). FAILS: the negative conclusion that the filter cannot carry (E17); the localization dichotomy; the dressing-size bounds. So EXC is open and not ruled out.
- 875 gap-exc-astra (astra max; check 881). OPEN: isotropic EXC neither proved nor refuted. Electric-only reference has a positive boost response of order the length. Large boosts reverse the sign on even-a tori; the natural endpoint has a negative single-link kernel.

## Step 1c. Rows 876 to 883 (READ D/FINISH.md lines 953-960)

- 876 gap-brainstorm2-max (Fable max; check 883). Lemma SQ HOLDS (883): (lambda_chi/lambda_0)^(2t) at most 1/kappa + (1 - 1/kappa)(lambda_1^+/lambda_0)^t. Theorem SQ-F displayed bound HOLDS: p_chi(a) at most (1 + S_ev(a/2)) max(S_ev(a)^g, e^(-ga)), g = (kappa - 1)/(8 kappa). (KURT): the flux ground state's fourth moment kappa at least 1 + c_0 at the seed size, uniformly in the cutoff. (HC): half-box creation of the flux state with polynomial amplitude (Lemma RPF, plateau bound, HOLD AFTER SCOPE CORRECTION).
- 883 check of 876 (astra xhigh). FAILS: that (KURT) alone supplies pure (F-h); the reframing that the consumer needs (F-h) only; the claimed logical weakening of (LOC) and (E17). So (KURT) is NOT established as weaker than (E17). Flux and glue estimates OPEN.
- 877 check of 861 (astra xhigh). HOLDS: FREE, K1-K4', STEP (threshold beta below 1/sqrt(216 pi)), VAC, HL, HL2, HL3, (6.3), TS, K5-K9. FAILS: Corollary VAC2's literal equivalence with EXIT. Normalized softening alone supplies no seed.
- 878 gap-crux-exercise2-max (Fable max; check 884). Theorem E: sheet doubling plus (TS-theta) gives geometric growth of the odd-flux free energy above the seed. (TS-theta): theta below 4 with F(n_1, n_i given 2n_j, 2n_k) at least F(n_1, n_i given n_j, n_k)/theta - C. It stops at a locality statement for excited states of the (F-h)/(LOC) kind. U(1) Coulomb has theta = 4 exactly (ARGUED). Lemma TD: q(2n_j) at most 2(1+S)^2 (q(n_j) + S_v/2). Narrowed: Q_8 and 2T tests bind only routes through (E17), (FQ), HA, EXC; void for a direct route to (ES); theorem-grade form: Z_2 above 2.191.
- 879 check of 863 (astra xhigh). HOLDS: B1, T2. FAILS as written: T2's probabilistic (reglue) obstruction, the path converse, several identifications. No open input discharged.
- 880 check of 862 (astra xhigh). Flip-even transfer gap on the twisted thin torus for even M up to M_1(n, beta) is checked. Weak coupling; off the order-one crux.
- 881 check of 875 (Opus high). All five HOLD. Electric-only reference has order-L_i positive boost response with gamma = log(r_V^(2T)/r_(1/2)) about 0.010 at 2.3, but the same passes for U(1), Q_8, 2T, Z_2 references. EXC LIVE and unproved, thin margin. Sharpest open statement: an order-L_i lower bound, at least -theta gamma_min L_i with theta below 1, uniform over tori, twists and b, on the boosted-minus-unboosted, odd-minus-all magnetic-cut plaquette response integrated over b in [0, beta]; available bound 4 beta n, order a^3. (This is EXC-W, the area form.)
- 882 check of 859 (astra xhigh). HOLDS: tube identity (twist covariance = variance of a conserved Z_2 charge). FAILS: numerical strand exclusion; chessboard recursion (C_3 not supplied). (TOP_j) OPEN. (SEED-DEC) is new packaging.

## Step 1d. Rows 884 to 891 (READ D/FINISH.md lines 961-968)

- 884 check of 878 (astra xhigh). HOLDS: F5's variational inequality, Lemma TD and its zero-thermal-sum law, Lemma CX1, (TS-theta) for untwisted Z_2 at beta at least 5/2 with theta = 1, C = log 2, n_0 = 8. HOLDS AFTER CORRECTION: Theorem E with its actual thermal and seed constants. FAILS: the printed Coulomb theta = 4 selectivity; the exact compact-Villain Gaussian identification; the argument exempting Q_8 and 2T from every (ES) test. OPEN: full compact-Villain (TS-theta); nonzero-background Z_2 extension. NOTE for the graph: (TS-theta) HOLDS for deconfined Z_2 at 5/2 (theta = 1), so (TS-theta) alone does not separate; the seed carries the selectivity.
- 885 reading (luna). Marginal-dimension method needs random currents and switching; gauge-side: Forsstrom-Viklund 2025 (Z_2 plaquette currents), Aizenman Part III Theorem 9.1 (3D Z_2 area and perimeter by duality), Duncan-Schweinhart 2025 (Potts gauge plaquette random cluster). None non-abelian.
- 886 gap-kurt-max (Fable max; check 889 has no RESULT yet: UNCHECKED). (KURT) not proved, not refuted. Theorem 4.1 moment hierarchy: theta^(pt) M_2p at most M_p^2 + rho^t (M_2p - M_p^2). Kurtosis-energy relation: kappa = 3r/(3r - 2), r = (mean energy of g^2 - 1)/(2E); (KURT) is equivalent to lambda_bar at most (4/3)(1 + 1/c_0) E, which contains m at most C E; strictly stronger than the consumer needs. Counterexamples with kappa = 1 exactly, heavy flux and zero even sum (product chain; anisotropic Z_2 gauge theory): (KURT) does not follow from transfer-operator structure. Weaker target (FUSE-E): E at least g m for the heavy electric sectors (rests on 876's bound). OPEN: (HB) a box with a hidden centre bit has a light even excitation; (FUSE-E); (KURT).
- 887 gap-seeddec-max (Fable max; check 891 has no RESULT yet: UNCHECKED). (TOP_j) PROVED in exact form (Lemma B, T1, Theorems TOP, TOP+); recursion z_(j+1) at most C_3 z_j^2, C_3 = 1,120,616; (SEED-DEC-H) is z_0 below 8.93e-7 but gives only exp(-c L^0.301), not (E17): NO RATE, does not reach the consumer (lead decision). (SEED-DEC-U): 64 P(a box of half the torus side is unclean) at most (K/8) sqrt(S_ev), no reflection positivity, for every magnetic background, reaches the consumer. Selectivity by contraposition: P(unclean) at least 7/512 for frozen Z_2, at least 1/(64 N_G) for frozen Q_8 and 2T. Identity (PAR): the parity cycle's law is a signed mixture (Gauss's law carried by negative timelike plaquette traces): no bound conditioning on a typical gauge field exists. Filling-Peierls barrier: P(half-integer edge) below 1/9 at best against GUIDE 0.33. OPEN: (S1) low-density short-range noise model for the SU(2) one-slice law (a local perimeter law for the equal-time 't Hooft functional); (S2) rigidity of minimal fillings at density 0.12 to 0.17 (zero-temperature 3D +-J Ising, group-blind).
- 888 gap-excmag-max (Fable max; check 890 has no RESULT yet: UNCHECKED). Magnetic bound R(beta) at least -theta gamma L_i is the area form EXC-W. Theorem 3.3: R(0) = R'(0) = 0, R''(0) = 4 L_i pi_5 (D_(5/2) - D_(1/2)), about -20 gamma L_i. Theorem 9.3: finite flux tension of the unboosted model, p_(1,b) at least (1/2)(1+eps)^(-L_i)(r_(1/2) e^(-4b))^(a L_i) on every torus and twist. ARGUED: carriers cross at b* about 0.31-0.34; the electric gain is erased there, group-blind. OPEN crux: (DRESS), a positive order-L_i excess of half-integer spin at least 5/2 temporal plaquettes on the fundamental flux sheet at isotropic coupling (EXC-W on the right object).
- 889, 890, 891: queued checks, no RESULT in FINISH at this commit. Rows 886, 887, 888 are unchecked.

## Step 2a. The consumer and the finish line (READ)

Notation (READ D/library/gap-es1-opus.md L40-58). Frame 1: direction 1 is time. Box A = (a, c, d), time a. e(B) = log lambda_0(B). S_ev(t; B) = Z_0(t; B)/lambda_0(B)^t - 1 (even thermal sum). X = sixteen crossed sectors z = (chi; m). p_z = Z_z(a; A)/Z_0(a; A), sum of p_z over X is 4. s_z = sector thermal sum. Delta(c, d) = a(2 e(a, c, d) - e(2a, c, d)). delta = 4 Delta(a, a) + 2 Delta(2a, a) + Delta(2a, 2a). (ES) at a: eps = S_ev(a; a^3) at most 1e-7 and delta at most 1e-7.

- (F-h) (READ gap-es1-opus.md L205): p_z at most K S^(1/2) for every z outside the light set L of four sectors, S = S_ev(a; (a, c, d)).
- (F-l) (READ L206): s_z at most K S for the four light sectors.
- FUSE-suff (READ L208-216; PROVED there, checked row 753 with K read as max(1, K)): (F-h) and (F-l) at the three shapes (a, a), (2a, a), (2a, 2a), plus six even sums at most 1e-16/(144 K^2), give delta below 1e-7, so (ES).
- The step named OPEN there (READ L223): (F-h) is a LOWER bound on an even sum by the square of a heavy weight. It needs (1) an operator creating the flux object, (2) a cluster estimate in the twisted sectors (two such objects at distance about a/2 cost at most the sum of their energies plus a controlled error).
- q_(r,i)(m) = Tr(T_(r,m)^(n_r) P_i^-)/Tr(T_(r,m)^(n_r)) = (1/2)(1 - Z^(m+v_ri)/Z^m) (READ D/library/gap-vortex-astra.md L128-133). Q_F = max over m with m_2 = 0 and i in {3, 4} of q_(1,i)(m) (L175).
- (FQ) (READ gap-vortex-astra.md L201-204): 8 Q_F at most K(a) sqrt(S), Q_F below 1/192, K(a) at most C_1 a^(p_1). PROVED there (checked row 780): (FQ) implies (F-h), through p_(chi,m) at most 8 Q_F for chi nonzero (4). "It gives the fusion input (F-h), not the separate even seed."
- (E17) (READ gap-vortex-astra.md L206-210): with the proved witness S at least eta(beta)^a, Q_F at most C_2 a^(p_2) eta_*^(a/2) suffices, eta_* = min of eta on the interval; K = 8 C_2 a^(p_2). "An area exponent is unnecessary."
- (SEED-FP) (READ D/library/gap-finishline-opus.md L119-125): one physical size ell, s_* below 1/5041, and for every first-passage datum (K, beta) with K at least K_0, S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) at most s_*. Thermal sum of the bare Wilson transfer operator of the periodic cube, physical time ell/2.
- (SEED-FQ) (READ L170): the consumer's form needs (FQ), (F-l) and the six even sums, with ONE constant K independent of the cutoff at a fixed physical size.
- Cutoff uniformity (READ L147-150): FUSE-suff asks even sums at most 1e-16/(144 K^2); along the trajectory a = ell/a_K tends to infinity, so K must be bounded independently of the cutoff at the fixed physical size. (E17) is a fixed-coupling statement; along the trajectory it must be replaced by a lower bound on S_ev in physical units (OPEN there).
- Order of difficulty (READ L171): (SEED-FQ) needs even sums near 1e-16, a larger box than (SEED-FP) (m a about 42 + 2 log K against about 12 inverse masses).

Consequence for the graph (ARGUED from the READ lines). "Reaches the consumer" means: implies (F-h) at the three shapes with K cutoff-uniform at one physical size. No flux statement supplies the glue half (the six even sums small, cutoff-uniformly). The glue half is a separate open input for every node below, unless a node implies (SEED-FP) directly.

## Step 2b. Fact-test rows (READ D/FINISH.md lines 863, 915, 916, 920, 922)

- 786 (astra max; check row 794): (U-tor) for periodic Villain U(1): at every fixed beta at least 2^14 the gauge-invariant Langevin gap on (Z/M)^4 tends to 0 as M grows. A group-blind proof of a volume-uniform gap is ruled out by a written theorem. Not proved for the Wilson cosine.
- 838 (Opus max, unchecked): Q_8 (freezing near 1.15) and 2T (near 2.15) bind at order one; 2I does not (freezing near 5.7). Haar moments of Q_8, 2T, 2O, 2I first differ from SU(2) at degrees 4, 6, 8, 12. So a tool at the crossover must see spin 2 or 3. (E17) cannot hold on a fixed physical torus along the SA sequence; it is a fixed-coupling target. Lemma W gives a cutoff-uniform even-sum witness; (E17-phys) is the physical form.
- 839 (Opus max; check row 849): seed = chi-square mutual information between slices; twist deficit = chi-square distinguishability of a slice and its centre flip. One-layer worst case (AS-bg) gives E^- at least m b - log(C b^2) below beta_W 2/3; PROVED false above 4 G_3 = 1.0109 at the flat background (Frohlich-Simon-Spencer): a ceiling for every background-uniform layer twist bound.
- 843 (Opus max; check row 854): spin-5/2 charged filter (Theorem 3.4): on V_(5/2) the SU(2) Wilson convolution lies strictly below the Q_8, 2T and U(1) eigenvalues at every beta. (HS) then (LS) were named; (LS) carries (E17).
- 845 (Opus max; check row 852): Theorem AG: annealed condition (AN) implies a gap; (AN1) is the worst case in disguise per the brief (row 845, checked). U(1) Villain fails (AN) at the coefficient step.

Fact tests as I will apply them (from the brief):
- T-U1: the argument must fail for U(1) in its Coulomb phase.
- T-FIN: it must use something Q_8 and 2T lack where they would otherwise pass. Theorem-grade form (row 878/884): Z_2 gauge theory above beta 2.191 (deconfined, perimeter law for the 't Hooft... no: area law for 't Hooft, perimeter for Wilson).
- T-WC: no worst-case environment bound (caps 2/3, 0.775, 4 G_3 = 1.0109; (AN1)).
- T-SHAPE (row 867's T3, NOT established per check 869): kept only as a heuristic; a carrying input should fail at short periods.

## Step 2c. Exact node statements, part 1 (READ D/library/gap-z2parity-astra.md L80-100, L245-331)

Torus Lambda = (Z/a)^2 x (Z/c) x (Z/d), a at least 3, c, d in {a, 2a}, time direction 1, time period a. Spatial twist m, cut cocycle omega_i, i = 3, 4.
q_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr L_m^a = Pr{<omega_i, C> = 1} = (1 - Z^(m+v_1i)/Z^m)/2, C the mod-two cycle of half-integer spatial spins in the one-slice law.

- (P) = (E17), parity form (L92-96): max over m_2 = 0, i = 3, 4 of q_(m,i)(a) at most C_0 a^p eta_*^(a/2), at fixed order-one coupling, uniformly over those tori and twists.
- Marked polynomial (M) (L256-262): nu_ce = product of cosh(beta x_p) dU/Z_ce, t_p = tanh(beta x_p), Z_k(lambda) = E_ce product over p of (1 + lambda eta_(k,p) t_p). Z_k(0) = 1, Z_k(1) = Z^k/Z_ce. Half-integer character coefficients are multiplied by lambda.
- (M1) surface identity: Z_k(lambda) = sum over closed S of lambda^|S| (-1)^<k,S> A_ce(S), A_ce(S) = E_ce product of t_p over S (signed in general).
- (M2), PROVED there, checked 870: F_(m,v)(lambda) = log Z_m - log Z_(m+v) = O(lambda^(A_i)), A_i = a L_i at least a^2.
- HA (L303-311): for I = [43/20, 5/2] there are r above 1, B, a_0 with F_(m,v) holomorphic on |lambda| below r and |F_(m,v)| at most B N there, N = 6 a^2 c d.
- HA implies (P) with area gain (M3): q at most 12 B a^4 e^(-(log r) a^2). PROVED there, checked 870.

Reading for the graph: (P) asks a LINEAR exponent (rate g = -(1/2) log eta_*). HA, EXC-W, (DRESS) and the 't Hooft surface with an area law give an AREA exponent. An area law is far more than the consumer needs. The linear exponent is the size of the statement.

## Step 2d. Exact node statements, part 2 (READ D/library/gap-ha-astra.md L206-262, L455-500)

- mu_(k,lambda) = product of (1 + lambda eta_(k,p) t_p) d nu_ce / Z_k(lambda); score S_(k,lambda) = sum over p of eta_(k,p) t_p/(1 + lambda eta_(k,p) t_p).
- (R1): R_(m,v)(lambda) = E_(m,lambda) S_(m,lambda) - E_(m+v,lambda) S_(m+v,lambda). (R2): F' = R, F(1) = integral of R over [0, 1]. Checked 874.
- (R): integral over [0, 1] of |R| at most C_R a^(p_R) e^(-ga). (R) implies (E17) (q at most F(1)/2). HA implies (R) (R3). PROVED there, checked 874.
- (C1): 0 at most F(lambda_0) at most (N/100) 2^(-A) at lambda_0 = 1/2400. (C2): integral over [lambda_0, 1] of |R| at most C_R a^(p_R) e^(-ga). (C2) + (C1) imply (E17). Checked 874; correction: (C2) is not weaker than (E17).
- Elementary real bound (L199-205): |F(lambda)| at most K_v M_R with K_v = a L_j at most 2 a^2. So an area-size UPPER bound on the real logarithm is free; the needed quantity must become small.

## Step 2e. Exact node statements, part 3 (READ D/library/gap-filter-ls-opus.md L128-196)

- Proposition EXP (checked 873, HOLDS): K(s) scales the high (half-integer spin at least 5/2) kinetic blocks by s; L(s) = z^|E| K(s)^(1/2) B_m K(s)^(1/2); p(s) = Tr(P_- L(s)^t)/Tr L(s)^t; log p(s_1) - log p(s_0) = t times the integral of Delta(s) ds/s, Delta(s) = <N_hi>_(-,s) - <N_hi>_(all,s).
- EXC (L168-172): an interval I in 2.3-2.6, s_* above 1 (natural: s_G = r_V^(2T)/r_(5/2)) and c_0 above 0 with integral from 1 to s_* of Delta(s) ds/s at least c_0, all admissible tori, twists, i, at t = a.
- EXC-W (L174): Delta(s) at least delta L_i on [1, s_*].
- Proposition 3.2 (b), PROVED, rearrangement: EXC with constant c_0 holds iff p(1) at most e^(-c_0 a) p(s_*). So EXC = (E17 at rate c_0) + "the boosted model is not more confining than e^(c_0 a) times SU(2)". EXC implies (E17) only when c_0 at least g = -(1/2) log eta_* (the consumer's rate; check 873's correction).
- Identity is group-blind; EXC analogue fails wherever p stays of order one.

## Step 2f. Exact node statements, part 4 (READ D/library/gap-excmag-max.md L235-237, L357-363; D/library/gap-kurt-max.md L359-412, L479-505)

- (DRESS) (excmag L235): integral from 1 to S of sum over e of [P_(s,beta)(j_e high | odd) - P_(s,beta)(j_e high)] ds/s at least kappa L_i, kappa above 0, uniformly in tori and twists, with the odd sector carried by the spin-1/2 sheet. "(DRESS) is EXC-W."
- (EMPTY) (excmag L357): in one slice of the boosted model a given straight line is empty, in the even sector, with probability at least c_3^(L_i). Implies R(beta) at least -C L_i only. EXC-W is strictly more.
- (HB) (kurt L479-483): on the seed boxes, if an electric sector has kappa - 1 at most eta_0 (hidden centre bit), then the even sector has an excitation with m a at most M_0, M_0 below log(1/s). Given (HB), the seed excludes the hidden bit, (KURT) holds with c_0 = eta_0, and SQ-F gives the electric part of (F-h).
- (FUSE-E) (kurt L497-505): lambda_chi/lambda_0 at most (lambda_1^+/lambda_0)^g for the heavy electric sectors (E at least g m), some g above 0. Then p_chi(a) at most (1 + S_ev(a/2)) S_ev(a)^(g/2). (KURT) implies (FUSE-E) by (SQ); (FUSE-E) does not imply (KURT) (Example 6.1).
- Example 6.2 (kurt L372-399), PROVED there, unchecked: an anisotropic Z_2 gauge theory (frozen space-like plaquettes, hot time-like ones) has a heavy flux sector, even sum 0 and kappa = 1. So (F-h) is not a class property. It needs isotropy or the exchange of axes.

### Working memo (mine; ideas to test in Steps 3-7; nothing here is proved yet)

M1. The consumer needs no rate. FUSE-suff uses (F-h) only through H_L = sum of the twelve heavy p_z. Theorem V (b) needs H_L + sum over L of s_z + S' small in ABSOLUTE terms (about 1.4e-8 per shape). So an absolute one-size bound, 96 Q_F at most about 1e-8 at the size where the even sums are below 1e-8, already gives (ES). A rate enters only through (FQ)'s form K sqrt(S). To verify against Theorem V (b)'s exact hypotheses.
M2. Consequence to test: a stretched-exponential flux bound (row 887's (SEED-DEC-H), exp(-c L^0.301)) would reach (ES) at fixed coupling, against the lead decision recorded in row 887.
M3. Trace algebra: time doubling squares the odd ratio, r(2 n_1) at most r(n_1)^2 (1 + S_ev)^2; transverse doubling at most doubles q with an additive thermal term (Lemma TD of row 878). The additive floor is of size S^4, below sqrt(S). So (TS-theta) is not needed by the consumer; it is needed only to keep an AREA law. To check against Theorem E's hypotheses.
M4. Transverse reflection positivity gives a fusion dichotomy: for an odd O supported in a slab at distance d from its mirror image, <O, T~^t O>^2 at most <O thetaO>^2 + rho^t ||O thetaO||^2, and <O thetaO> at most ||O||^2 theta'^d in the crossed frame. With O = E[phi | slab] this needs one regularity input on the flux ground state (row 876's (HC)). Isotropy enters as theta' = theta. Example 6.2 is consistent (theta' = 1 there).

## Step 2g. Theorem V and Corollary V1 (READ D/library/gap-es1-opus.md L60-80); memo M1 confirmed

READ. Theorem V (b): for every set L of four sectors with eta_L = H_L/2 + (1/2) sum over L of s_z below 1, Delta(c, d) at most -log(1 - eta_L) + log(1 + S') - 2 log(1 + eps). Corollary V1: with h = H_L for the four sectors of largest weight, sigma_L = sum over L of s_z, h at most 1/2 and eta_L at most 1/2:

  h/2 - h^2/2 - 2 eps_cd  at most  Delta(c, d)  at most  h + sigma_L + S'_cd.

READ L78: "(HEAVY) ... is not a side condition but the statement itself."

**Proposition ABS (PROVED here from Corollary V1; two lines).** Fix a at least 3. Suppose that at each shape (c, d) in {(a, a), (2a, a), (2a, 2a)} there is a set L of four sectors with
  H_L + sigma_L + S'_cd at most 1.4e-8,
and eps_aa at most 1e-7. Then (ES) holds at a. Conversely, if (ES) holds at a and the three eps_cd are at most 1e-7, then at each shape the four heaviest... precisely: h(1 - h) at most 2 Delta(c, d) + 4 eps_cd at most 6e-7, so h at most 6.1e-7.
Proof. Upper bound of V1: Delta(c, d) at most 1.4e-8 at each shape (eta_L at most 0.7e-8 below 1/2). delta = 4 Delta(a, a) + 2 Delta(2a, a) + Delta(2a, 2a) at most 7 x 1.4e-8 below 1e-7. Converse: each Delta is at least 0 (Lemma K (b), READ L50), so each Delta(c, d) is at most delta at most 1e-7 (coefficients at least 1); lower bound of V1; h(1 - h) at most 6e-7 with h at most 1/2 forces h at most 6.1e-7. (The case h above 1/2 is excluded by Theorem V (a), (c): Q at least 2h(1 - h) and Q/4 at most Delta + 2 eps; if h is in (1/2, 1) take the continuity-free form Q at most 4(1 - e^(-Delta - 2 eps)) at most 1.2e-6 directly, which forces every p_z(1 - p_z) at most 1.2e-6, so each p_z is within 1.3e-6 of 0 or 1; the sum is 4, so exactly four are near 1, and h at most 12 x 1.3e-6.) QED

Reading. The flux half of the consumer is, exactly (necessary and sufficient up to the constants above, given the even sums): the twelve heavy crossed weights are at most about 1e-8 at ONE size. No rate, no K sqrt(S), no exponent. Through (4) of gap-vortex-astra.md (p_(chi,m) at most 8 Q_F), it follows from

  (Q-ABS)  Q_F at most 1.4e-10 at the three shapes, at the one size a where the even sums and the four light sector sums are at most about 4e-9.

(FQ) and (E17) are sufficient for (Q-ABS) only together with the glue half at that size; they ask more: (FQ) asks Q_F at most K sqrt(S) with S near 1e-16, (E17) asks a linear exponent at every a. A bound of any shape that tends to 0 with a at fixed coupling gives (Q-ABS) at fixed coupling.

## Step 2h. Route E's statements (READ D/library/gap-crux-exercise2-max.md L485-515); memo M3 is already in the lane

- Objects: torus (n_1, n_i, n_j, n_k), v = v_(1i), Z^(+-) = (Z^0 +- Z^v)/2, q = Z^-/Z^+ (odd over even), F = -log q.
- Lemma WS (time doubling, found again there; it is Lemma A (a)): q(2 n_1) at most q(n_1)^2 (1 + s_+(n_1))^2. (WS2): F(2 n_1, 2 n_i | n_j, n_k) at least 4 F(n_1, n_i | n_j, n_k) - 6 log(1 + s).
- Lemma TD (checked 884, HOLDS): q(n_1, n_i | 2 n_j, n_k) at most 2 (1 + S)^2 [q(n_1, n_i | n_j, n_k) + S_v/2], S_0, S_v the full thermal sums of T_0, T_v in direction j at time n_j.
- (TS-theta) (L502-504): theta below 4, C, n_0 with F(n_1, n_i | 2 n_j, 2 n_k) at least F(n_1, n_i | n_j, n_k)/theta - C.
- Theorem E (checked 884, HOLDS AFTER CORRECTION): (TS-theta) and thermal sums at most s_* give Phi(2n) at least (4/theta) Phi(n) - D, Phi(n) = F(n, n | n, n). Seed: an odd-flux weight below about four per cent on a symmetric torus whose glue thermal sum is at most 1.
- READ L500: "Lemma TD controls the transverse step only while q is at least of the order of the crossed thermal sums. This is the mechanism inside Theorem S."

So memo M3 is Lemma WS plus Lemma TD; not new. What Proposition ABS adds (ARGUED composition, constants not optimized): WS2 and two uses of TD give q(2n, 2n | 2n, 2n) at most [4 (1 + S)^4 (q + S_v)]^4 (1 + s)^6 without (TS-theta). The floor is the fourth power of a crossed thermal sum. By Proposition ABS the consumer needs only an absolute bound, so (TS-theta) is not needed to reach the consumer. It is needed only to keep an area law. It cannot be the weakest sufficient node.

## Step 2i. Lemma RPF and (HC) (READ D/library/gap-brainstorm2-max.md L362-366, L426-452); memo M4 is already in the lane

- Lemma RPF (row 876; check 883: HOLDS AFTER SCOPE CORRECTION): O a real function of the time-zero links in 0 < x_2 < c/2, |O| at most 1, odd under the centre flip; O' = theta_2 O; C = <O O'>; f(t) the propagator of O; phi = (O O' - C) Omega. Then <phi, (L/lambda_0)^t phi> at least f(t)^2 - C^2. Plateau: f(t)^2 at most C^2 + rho^t.
- Stage 3 there (ARGUED): either E at least m/2 (heavy; then p_z at most K S^(1/2) up to the multiplicity (MULT)), or the winding lines have long-range order across the box. READ L445: "given the glue half, the flux half is one order-one statement ... winding lines of length a are disordered across the box. In thermal words: 1/a is below the deconfinement temperature. For frozen Q_8 and 2T at beta 2.3 this statement is false ...; for U(1) the glue half fails first."
- (HC) (L365, L448): some centre-odd operator of the inner half-box creates the flux ground state with amplitude at least a^(-p); equivalently E[(E[g | right half])^2] at least a^(-p), g = Psi/Omega. OPEN. Proved there only with a worst-exterior gap (fails the worst-case test).
- READ L452: (HC) and (KURT) "both say: the flux tube is a local object. Neither is a confinement statement, and both are expected to hold in every phase, including the rivals'."

So memo M4 is row 876's Top 2; not new. What I keep from it: after (HC), the SU(2)-specific flux input is ONE ORDER-ONE inequality at one size. The same holds on the absolute side (Theorem SH's thresholds). Step 4 makes this the common core.

## Step 2j. Decoder nodes (READ D/library/gap-seeddec-max.md L164-209, L258-263, L285-294)

- (U) (L164, PROVED there, unchecked; check row 891 has no RESULT): union bound, no reflection positivity, any law with gamma a cycle: P(omega(gamma) nonzero) at most (L/g)^3 max over boxes of P(N unclean). With g = L/4: at most 64 max P(a box of side L/2 is unclean).
- (SEED-DEC-U) (L202, L285): 64 p_0(a/4) at most (K(a)/8) sqrt(S_ev(a)) and below 1/192, at the consumer's size, time period and backgrounds. "This is the form that reaches (FQ)." READ L209: it asks p_0 below about 1e-12 at the consumer's size.
- (SEED-DEC-H) (row 887 RESULT): z_0 below 8.93e-7 (chessboard norm of "unclean" at level 0) gives exp(-c L^0.301), no linear rate.
- (S1) (L258, L287): a noise model for the SU(2) one-slice law in the window; a local perimeter law for the equal-time 't Hooft functional. (S2) (L259, L288): rigidity of minimal fillings at noise density 0.12 to 0.17 (zero-temperature 3D +-J Ising, dependent disorder, boundary stability); group-blind.
- READ L263: "the route stops at the same place as (SEED-FP): an order-one statement about the bare measure at a few correlation lengths."
- READ L294: a decision left to the lead: "whether the consumer can use a flux half without a rate (then (SEED-DEC-H) matters)".

Answer to L294 from Proposition ABS (PROVED above from Corollary V1): YES. The (ES) chain accepts a flux half without a rate: an absolute bound at one size. The rate is forced only by the form (FQ) (K sqrt(S), with S tending to 0 exponentially in a). So at fixed coupling a stretched-exponential bound reaches (ES), provided it holds at the three shapes with the backgrounds m (m_2 = 0), or reaches (SEED-FP) with m = 0 only (Step 4, Lemma SPLIT). Whether (SEED-DEC-H)'s chessboard step holds with backgrounds is not established (OPEN; the m = 0 chain does not need it).

## Step 2k. Seed-path nodes (READ D/library/gap-exit-max.md L345-351, L714-724)

- PIN-MIX(L, a, alpha, m) (L345-351): for every torus of the family, every cutoff and first-passage datum, (pi/2) a min(a/4, 1) X_m(L, a) at most alpha below 1: under every unit pinning of the other block holonomies the covariance of one block holonomy with another decays exponentially, with a weighted sum below the threshold. Theorem LAND follows (check 877: HOLDS AFTER CORRECTION).
- (PATH) (L714-719): the local means of exp(-s S), s in [0, 1], compare between T_n and T_(rho n) with an error whose integral over s, times (rho n)^4, is below (rho/2) log(1 + s_0). Proved range b below 0.3609. This is the whole seed (both halves) in path form (identity (6.3), check 877 HOLDS; Lemma Z', checked row 727).
- Fact tests READ L721-724: (PATH) on [0, beta] says "no freezing and no Coulomb phase up to beta. It must use the continuous non-abelian group."

## Step 3. The implication graph

### 3.1 Nodes (exact statements are in Steps 2a to 2k)

Consumers. (GAP); (SEED-FP); (ES) = (SEED-EV); FUSE-suff; (F-h); (F-l); (FQ); GLUE = "the even sums of the consumer are small at one physical size, cutoff-uniformly".
Absolute flux nodes (they bound the odd weight itself). (E17) = (P) = TH (the wrapping 't Hooft surface with a linear exponent); HA; (R); (C2) with (C1); EXC; EXC-W; (DRESS); (EMPTY); (SEED-DEC-U); (SEED-DEC-H); (S1); (S2); (E17-phys-CA).
Relative flux nodes (they compare flux with glue). (KURT); (FUSE-E); (HB); (HC) with Lemma RPF; (TS-theta) with Theorem E.
Whole-seed nodes. (PATH); PIN-MIX.
Two nodes added here (Step 2g and Step 4): (Q-ABS), the absolute flux half of (ES); (Q-FP), the flux half of (SEED-FP).

### 3.2 Edges

Marks: PROVED-c = proved in the lane and checked by another provider (row given); PROVED-u = proved in the lane, not checked; PROVED-h = proved here; ARGUED; "?" = unknown.

| # | Edge | Mark | Source |
|---|---|---|---|
| 1 | (E17) <=> (P) (odd class of the half-integer Z_2-cycle) | PROVED-c | row 860 P1, P2; check 864 HOLDS; check 870 HOLDS |
| 2 | (P) <=> TH: parity of an edge set is a 't Hooft loop, E[(-1)^N] = Z(flip)/Z | PROVED-c after repair | row 867 Prop TL; check 869 (dual-surface qualification) |
| 3 | HA => (P), with area gain | PROVED-c | row 866 (M3); check 870 |
| 4 | HA => (R) => (C2); (C2) + (C1) => (E17); (C1) holds | PROVED-c | row 871 (R3), (C1); check 874 |
| 5 | (E17) => (C2) | ? (only if the response has a sign) | check 874 |
| 6 | (P) => HA | ? ; HA is strictly stronger as a statement (off-real) | check 870 |
| 7 | EXC(c_0) <=> p(1) at most e^(-c_0 a) p(s_*); EXC(c_0 at least g) => (E17) | PROVED-c after correction | row 872 Prop 3.2; check 873 |
| 8 | (E17) => EXC | ? (needs the boosted model not exponentially more confining) | row 872 3.2 (b) |
| 9 | EXC-W => EXC, and => area law | PROVED-u (rearrangement; 3.2 (a) was in check 873's scope: the consumer rate HOLDS AFTER CORRECTION) | row 872 |
| 10 | (DRESS) <=> EXC-W, if the carrier switch stays outside [1, S] | PROVED-u | row 888 (check 890 has no RESULT) |
| 11 | (EMPTY) => R(beta) at least -C L_i only; does not give EXC-W | PROVED-u | row 888 Prop 9.4 |
| 12 | (SEED-DEC-U) => (FQ) | PROVED-u | row 887 (U); check 891 has no RESULT |
| 13 | (S1) + (S2) => (SEED-DEC-U) | ARGUED (outline, Prop RIG) | row 887 L250-260 |
| 14 | (SEED-DEC-H) => odd weight at most exp(-c L^0.301), m = 0 | PROVED-u given the chessboard estimate | row 887 |
| 15 | (FQ) => (F-h) | PROVED-c | gap-vortex-astra (4); check row 780 |
| 16 | (F-h) + (F-l) + six even sums => (ES) (FUSE-suff) | PROVED-c | gap-es1-opus 5; check row 753 |
| 17 | (ES) => two of three seeds, (G_ev), gap on centre-blind functions | PROVED-c | Theorem R, R4, EV-L; checks 744, 732 |
| 18 | (SEED-FP) => (GAP), given the account | PROVED-c for (a), (b); ARGUED for (c)-(f) | gap-finishline-opus 2.5 |
| 19 | (E17-phys-CA) => (FQ) with K_F cutoff-independent | PROVED-c, conditional on the account's (h1)-(h3) and hypotheses | rows 865, 868 |
| 20 | (E17) at fixed coupling => (FQ) at fixed coupling (witness S at least eta^a) | PROVED-c | gap-vortex-astra L206-210; row 780 |
| 21 | (E17) on a fixed physical torus along the first-passage sequence | FALSE as stated (asks too fast a decay) | row 838 item 2 (unchecked) |
| 22 | (KURT) => (FUSE-E), g about (kappa - 1)/kappa | PROVED-u; Lemma SQ itself PROVED-c | row 886 7.6; check 883 (SQ HOLDS) |
| 23 | (KURT) => pure (F-h) | FAILS as claimed | check 883 |
| 24 | (FUSE-E) => p_chi(a) at most (1 + S_ev(a/2)) S_ev(a)^(g/2) | PROVED-u | row 886 7.6 (check 889 has no RESULT) |
| 25 | (HB) + seed => (KURT) at the seed | ARGUED (by its definition) | row 886 7.5 |
| 26 | (HC) + Lemma RPF => dichotomy: E at least m/2, or winding lines ordered across the box | ARGUED (Stage 3); RPF PROVED-c after scope correction | row 876; check 883 |
| 27 | (TS-theta) + a four per cent flux seed + bounded thermal sums => geometric growth of -log q | PROVED-c after correction | row 878 Theorem E; check 884 |
| 28 | (TS-theta) holds for untwisted Z_2 at beta at least 5/2 (theta = 1) | PROVED-c | check 884 |
| 29 | (PATH) => seed at the Wilson coupling (both halves) | PROVED-c for the identities; the composition ARGUED | row 861 (6.3); check 877; Lemma Z' row 727 |
| 30 | PIN-MIX => LAND (uniform landing; exponential clustering of block loops) | PROVED-c after correction | row 861; check 877 |
| 31 | soft step + Theorem HO => seed | circular (Prop VAC); the literal equivalence VAC2 FAILS | check 877 |
| 32 | (Q-ABS) + GLUE(4e-9) => (ES); (ES) => heavy weight at most 6.1e-7 | PROVED-h (Proposition ABS, from Corollary V1) | Step 2g |
| 33 | every absolute node that tends to 0 with a => (Q-ABS) at fixed coupling, large a | PROVED-h (trivial) | Step 2g |
| 34 | (SEED-FP) <=> (Q-FP) + GLUE-FP, constants within a factor 7 | PROVED-h (Lemma SPLIT) | Step 4 |
| 35 | (TS-theta) is not needed to reach a consumer (only to keep an area law) | ARGUED (composition of WS2, TD, ABS) | Step 2h |

### 3.3 Which nodes reach a consumer, and how

- Reaches (GAP) with a cutoff-uniform rate by a checked chain: (SEED-FP) only (edge 18; its rate is M_* = 2 log(1/(5041 s_*))/ell).
- Reaches (FQ) cutoff-uniformly by a checked conditional edge: (E17-phys-CA) only (edge 19). It still needs GLUE and (F-l).
- Reaches (FQ) or (ES) at FIXED coupling: (E17) = (P) = TH (edges 1, 2, 20); HA; (C2); EXC with c_0 at least g; EXC-W; (DRESS) (through EXC-W); (SEED-DEC-U). With Proposition ABS also: (SEED-DEC-H) for m = 0 into the (SEED-FP) chain; (TS-theta) with any theta below 4 plus its seed; (FUSE-E) with any g above 0 (edge 24 gives a positive power of S_ev, enough for the absolute form).
- Does not reach a consumer alone: (EMPTY) (a lower bound on the wrong side), (S1) or (S2) singly, (HB) without the seed, (HC) without the order-one disorder statement and (MULT), (KURT) by check 883's verdict on pure (F-h) (it does give edge 22, then 24).
- Whole-seed nodes (PATH), PIN-MIX reach (SEED-FP) only at a Wilson coupling, not along first passage (gap-finishline-opus 2.3, READ Step 2a).
- No flux node supplies GLUE. Every chain through (FQ), (F-h) or (ES) needs GLUE and (F-l) in addition.

## Step 4. The weakest sufficient statement

### 4.1 Lemma SPLIT (the periodic seed is a glue number and a flux number; PROVED here)

Setting (READ gap-es1-opus.md L38-40, the class). B a periodic box, T = T_(B,0) its positive trace-class transfer operator, C_2, C_3, C_4 the commuting centre flips, P_chi the eight sector projections, Z_chi(t) = Tr(T^t P_chi) at least 0, lambda_0 the top eigenvalue, simple, with an even eigenvector. S(t; B) = Tr T^t/lambda_0^t - 1 (the full periodic thermal sum, the object of (SEED-FP) and of Theorem SH). S_ev(t; B) = Z_0(t)/lambda_0^t - 1. For i = 2, 3, 4: q_i = Tr(T^t (1 - C_i)/2)/Tr T^t = (1 - Z^(v_1i)/Z^0)/2, and Q_0 = max of the three q_i. (This is q_(1,i)(m) of gap-vortex-astra.md at m = 0.)

**Lemma SPLIT.** If 3 Q_0 is below 1, then (1 + S_ev)/(1 - Q_0) at most 1 + S at most (1 + S_ev)/(1 - 3 Q_0). Also S_ev at most S and Q_0 at most S/(1 + S).
Proof. Tr T^t - Z_0 = sum over chi nonzero of Z_chi. Each nonzero chi has a bit chi_i = 1, so the sum is at most the sum over i of [sum over chi with chi_i = 1 of Z_chi] = (q_2 + q_3 + q_4) Tr T^t, at most 3 Q_0 Tr T^t. It is at least the largest of the three inner sums, Q_0 Tr T^t. So Q_0 at most 1 - Z_0/Tr T^t at most 3 Q_0. Divide Z_0 = lambda_0^t (1 + S_ev) by Tr T^t = lambda_0^t (1 + S). For the last claims: Z_0 at most Tr T^t, and Z_0 at least lambda_0^t (the vacuum is even), so Q_0 at most 1 - 1/(1 + S). QED

**Corollary O1 (PROVED here; thresholds READ).** (a) If s_* is at most 1/6, S_ev at most s_*/2 and Q_0 at most s_*/7, then S at most s_*. (Arithmetic: (1 + s/2) at most (1 + s)(1 - 3s/7) for s at most 1/6.) (b) If S_ev at most 1/10 and Q_0 at most 1/20, then S at most 1.1/0.85 - 1, below 3/10. (c) Conversely S at most s_* gives S_ev at most s_* and Q_0 at most s_*.
With the thresholds READ in D/library/gap-seed-shape.md L116-125 (Theorem SH, checked by Claude Opus 5.5, row 707; same model family as its author): t(r) = 1/1650 (r = 2), 1/100 (3), 1/25 (4), 1/10 (6), 3/10 (r at least 24), r = b/a, on S(a; b^3). And (SEED-FP) uses 1/5041 at r = 2 (Corollary S3', checked rows 698, 699).

So the seed, in every shape the lane has, is the pair

  GLUE-FP: S_ev(a; b^3) at most t(r)/2 (1/10 at r at least 24),
  (Q-FP): Q_0(a; b^3) at most t(r)/7 (1/20 at r at least 24),

one box, one time, m = 0, no rate. By cubic symmetry of b^3 the three q_i are one number. So (Q-FP) is ONE inequality: on the torus (a, b, b, b), Z^(v_12)/Z^0 at least 1 - 2 t(r)/7 (at least 9/10 at r at least 24).

### 4.2 Fact tests of the sufficient nodes, as targets

| Node | U(1) Coulomb must fail | Q_8, 2T, Z_2 above 2.191 must fail | no worst case | strength against the consumer |
|---|---|---|---|---|
| (E17) = (P) = TH | fails (ARGUED, rows 866, 870) | fails (odd weight of order one; Z_2 PROVED row 870) | passes as a target | linear exponent at every size and background: more than needed |
| HA | fails (ARGUED, check 870, 874 S7) | fails (PROVED for Z_2 at 5/2, check 870) | fails in a background-uniform version (PROVED, check 870) | area law and a complex disc: far more than needed |
| (C2) | fails (ARGUED, check 874) | fails (PROVED, check 874) | passes as a target | restates (E17) or more (check 874) |
| EXC, EXC-W, (DRESS) | EXC fails where p stays of order one (PROVED tautology, row 872) | same | electric reference response is group-blind (check 881); selection sits in (DRESS) (row 888) | (E17) plus a boosted-model comparison; EXC-W an area law |
| (SEED-DEC-U) | fails (ARGUED, row 887) | fails (PROVED by contraposition, row 887, unchecked) | passes (one event in a ball) | relative sqrt(S) form; absolute form by ABS |
| (KURT) | HOLDS for U(1) (kappa at least 3/2, row 886): the failure must then sit in GLUE | fails (hidden bit, kappa to 1) | passes | stronger than the consumer needs (row 886) |
| (FUSE-E), any g above 0 | holds (flux-two state, ARGUED row 886 table): failure sits in GLUE | fails for the electric sectors | passes | weakest relative node |
| (HB) | empty for U(1) (no bit) | false, "as it must be" (row 886) | needs the vacuum of a deconfined box (row 886) | order-one, relative |
| (TS-theta) + seed | theta = 4: marginal (the printed selectivity FAILS, check 884) | (TS-theta) HOLDS for Z_2 (theta = 1, check 884); the seed fails | passes | keeps an area law: not needed |
| (PATH), PIN-MIX | fail (power-law torus comparison; LAND forces clustering) | fail across freezing (ARGUED, row 861) | PIN-MIX is a sup over pinnings: worst case | the whole seed, at a Wilson coupling |
| (Q-ABS), (Q-FP) | fail: the Coulomb odd weight is scale-free and not small (ARGUED from the Gaussian form, row 878; proved lane statement row 786 not re-read) | fail: the electric sectors are light, q near 1/2 (ARGUED; Z_2 Peierls range theorem-grade) | pass: a number of the true measure | exactly the consumer's flux half |

### 4.3 The choice

**Chosen statement: (Q-FP) at an SH shape.** For one pair (a, b) with b at least 24 a (or the pair of another line of the table), on the periodic torus (a, b, b, b):

  (CORE)  Z^(v_12)/Z^0 at least 9/10, that is Q_0(a; b^3) at most 1/20,

for bare Wilson SU(2) at one coupling in the band; in the real problem, for every first-passage datum at one physical pair (a, b). It reaches (GAP) with the cutoff-uniform rate of Theorem SH together with GLUE-FP (Corollary O1 (b), then edge 18). It is the flux half of the weakest consumer in the lane, and by Lemma SPLIT it is necessary for that consumer up to the factor 7.

**Against (E17).** (CORE) is genuinely weaker as an input: one torus, m = 0, no rate, threshold 1/20, against every size, every background with m_2 = 0, and the rate eta_*^(a/2). Formal comparison:
- (E17) does not give (CORE) by a written edge: the tori differ ((a, a, c, d) against (a, b, b, b)). With GLUE the bridge exists: (E17) feeds chain I ((FQ), FUSE-suff, (ES), Theorem R), which gives the gap; if the periodic seed is among Theorem R's two seeds, (CORE) follows by O1 (c). ARGUED.
- (CORE) with GLUE-FP gives, by Theorem SH, the gap of the full periodic transfer operator on every cube of side at least b. Then the m = 0 odd weights decay exponentially in the time, at the seed's own rate. That is an (E17)-type bound at m = 0, not at the rate eta_* and not with backgrounds. ARGUED from the READ statement of Theorem SH.
So: not equivalent as statements; weaker as an input; after GLUE both say that electric flux is heavy at all sizes above the seed.

**Three corrections this makes to the night's ledger** (all from Proposition ABS, Lemma SPLIT and READ lines):
1. A rate is an output, not an input. (E17), HA, (C2), EXC, EXC-W and (DRESS) all ask for a rate or an area law. The consumer's flux half is one number at one size ((Q-ABS) for chain I, (CORE) for chain II).
2. Row 887's open question (L294) is answered yes: a flux bound without a rate reaches a consumer at fixed coupling. The lead's decision "the consumer needs a rate, so (SEED-DEC-H) alone does not reach it" holds only for the form (FQ). (SEED-DEC-H) still needs its own seed z_0 below 8.93e-7, which is OPEN, and GLUE.
3. (TS-theta) is not on the critical path (edge 35).

### 4.4 The incomparable alternative, and what each costs

(CORE) is absolute. The relative nodes are incomparable with it: (FUSE-E) with some g above 0 (weakest), (KURT), (HB), (HC) with RPF.
- Cost of (CORE): one order-one inequality with no small parameter, false for every rival, for the true measure at a few correlation lengths. In thermal words (READ row 876 L445): 1/a is below the deconfinement temperature.
- Cost of (FUSE-E)_g: PROVED here from edge 24 and SPLIT: if S_ev(a/2) at most 1, S_ev(a) at most 160^(-2/g) and (FUSE-E)_g holds for the seven nonzero sectors of the box, then every p_chi is at most 2/160, and Q_0 at most 4 max p_chi at most 1/20, so (CORE) holds. So (FUSE-E)_g buys (CORE) with a stronger GLUE (level 160^(-2/g)) and ANY explicit g above 0. Its own content is the absence of a hidden centre bit; it holds in U(1) and fails for the frozen finite groups. (Check: Q_0 = sum over chi with chi_i = 1 of Z_chi/Tr T^t, four terms, each at most p_chi since Z_0 at most Tr T^t.)
- Common core of both (the statement every flux node implies at its own shape, and which with GLUE suffices):

  (NGD), "no gapped deconfinement at the seed shape": there is s_0 above 0 with: S_ev(a; b^3) at most s_0 implies Q_0(a; b^3) at most 1/20.

  (CORE) implies (NGD) trivially. (FUSE-E)_g implies (NGD) with s_0 = 160^(-2/g) (given S_ev(a/2) at most 1). (NGD) with GLUE at level min(s_0, 1/10) implies the seed. (NGD) is false for Z_2 above 2.191 and frozen Q_8, 2T (ARGUED: gapped and deconfined), and empty for U(1) Coulomb (its hypothesis fails; ARGUED). So (NGD) has the right fact-test profile and is the weakest statement in the graph that still reaches a consumer with a cutoff-uniform rate.

## Step 5. Attack, stage 1: the crux lemma stated exactly, in three frames

Torus (a, b, b, b), directions (1, i, j, k), b at least 24 a. v = v_(1i). rho = Z^v/Z^0, in (0, 1] (READ row 878 I2: 0 below Z^v at most Z^0). q = (1 - rho)/2 = Q_0 (the three choices of i give one number).

**Crux Lemma (NGD), exact.** There are a, b at least 24 a and s_0 in (0, 1/10] such that, for bare Wilson SU(2) at the coupling considered (in the real problem: for every first-passage datum at one physical pair (a, b)): S_ev(a; b^3) at most s_0 implies q at most 1/20. Its unconditional form is (CORE): q at most 1/20.

**Face F1 (time 1; the definition).** q = Tr(T_1^a (1 - C_i)/2)/Tr T_1^a: the thermal weight, at time a on the cube b^3, of the states with odd flux along a side.

**Face F2 (time i; the winding-line sector). PROVED here.** Let T be the transfer operator of the box (a, b, b) (sides 1, j, k), C_1 the flip of the short direction, lambda_0 its top eigenvalue, lambda_- its top eigenvalue on C_1-odd vectors, theta_P = lambda_-/lambda_0, and s_+ = Tr(T^b P_+)/lambda_0^b - 1, s_- = Tr(T^b P_-)/lambda_-^b - 1 (both at least 0). Then
  theta_P^b/(2 + s_+)  at most  q  at most  theta_P^b (1 + s_-).
Proof. Z^0 = Z_+ + Z_-, Z^v = Z_+ - Z_- with Z_+ = lambda_0^b (1 + s_+), Z_- = lambda_-^b (1 + s_-). q = Z_-/(Z_+ + Z_-) at most Z_-/Z_+ at most theta_P^b (1 + s_-). And x/(c + x) increases in x, with Z_-/lambda_0^b at least theta_P^b and theta_P at most 1: q at least theta_P^b/(1 + s_+ + theta_P^b) at least theta_P^b/(2 + s_+). QED
So (CORE) follows from theta_P^b (1 + s_-) at most 1/20. With E_P = -log theta_P: E_P at least (3 + log(1 + s_-))/b. In the units of the short side: E_P a at least about 0.13 at b = 24 a.

**Face F3 (time j; the vortex energy). PROVED here.** Let T_0, T_v be the transfer operators of the box (a, b, b) (sides 1, i, k) without and with the spatial twist v (positive, trace class, READ (TM-tw)), tau_0, tau_v their top eigenvalues (tau_v at most tau_0, READ gap-es1-opus.md L38), eps_v = log(tau_0/tau_v) at least 0, S_v = Tr T_v^b/tau_v^b - 1. By the symmetry of the torus T_0 is the operator T of F2, so tau_0 = lambda_0. Then
  q  at most  eps_v b + s_+ ,    eps_v b  at most  2q/(1 - 2q) + S_v ,
and the exact identity  tau_v^b (1 + S_v) = lambda_0^b [(1 + s_+) - theta_P^b (1 + s_-)].
Proof. Z^v = Tr T_v^b = tau_v^b (1 + S_v) and Z^v = Z_+ - Z_- (the identity). Z^0 = Z_+ + Z_- = Z_+/(1 - q). So rho = Z^v/Z^0 at least tau_v^b (1 - q)/(lambda_0^b (1 + s_+)) = x (1 - q) with x = e^(-eps_v b)/(1 + s_+). From 1 - 2q at least x (1 - q): q at most (1 - x)/(2 - x) at most 1 - x at most eps_v b + s_+. And rho at most e^(-eps_v b)(1 + S_v) because Z^0 at least lambda_0^b; so eps_v b at most -log(1 - 2q) + log(1 + S_v) at most 2q/(1 - 2q) + S_v. QED
So (CORE) follows from

  (VF)  eps_v(a; b, b) at most 1/(25 b),   with   s_+ at most 1/100.

(VF) is a LOWER bound on a top eigenvalue: tau_v at least tau_0 e^(-1/(25 b)). Every trial vector gives a proved bound on that side. This is the one face in which the needed inequality points in the variational direction. Reading: v makes the winding line of direction 1 antiperiodic in direction i; eps_v is the energy of that boundary condition, the tension of a centre vortex line of length b.

**Sizes (GUIDE; recalled lattice numbers, they decide nothing).** At beta 2.3 the string tension is about 0.136 per plaquette, so at a = 10 the true E_P a is about 14, against the 0.13 that (CORE) asks. The flux half of the weakest seed has about two orders of slack in the exponent. Its content is not a size: it is that the winding-line sector has a gap at all at this shape (it has none, to this accuracy, in a deconfined box).

**Fact tests of (VF) as a target (ARGUED).** U(1) Coulomb: eps_v is the energy of a flux pi spread over the (1, i) section, of order beta pi^2/(2a) per unit time at this shape, so eps_v b is of order 12 pi^2 beta: fails. Frozen Q_8: twisted flat connections exist, but their centralizer is the centre (2 elements) against 8 for the trivial one, so tau_v/tau_0 is about 1/4 per step and eps_v b is about b log 4: fails. Z_2 above 2.191: the vortex has tension of order 2 beta per plaquette: fails. Weakly coupled SU(2) in a small box: the confining holonomy costs a Casimir energy of order b^2/a^3: fails, as it must (deconfined at temperature 1/a). No worst-case quantity enters.

## Step 6. Attack, stage 2: the variational face (VF), and where it stops

Transfer operator form (READ D/library/gap-filter-ls-opus.md L128-129 at s = 1): L_m = z^|E| K^(1/2) B_m K^(1/2), K the product of the one-edge kinetic convolutions, B_m the magnetic multiplier with the spatial twist m. Here T_0 = L_0, T_v = L_v on the box (a, b, b). The twist is carried by a co-closed line ell of b plaquettes (plane (1, i), fixed (x_1, x_i), all x_k) on which the weight e^(beta x_p) is replaced by e^(-beta x_p), x_p = (1/2) tr U_p (READ row 867 Proposition TL, checked 869 with the dual-surface qualification). So B_v = B_0 D_ell with D_ell = product over p in ell of e^(-2 beta x_p), and e^(-2 beta) at most e^(-2 beta x_p) at most e^(2 beta).

**Lemma VAR1 (the untwisted vacuum as trial vector; PROVED here).** Let Omega_0 be the unit top eigenvector of T_0 and nu the probability measure d nu = z^|E| B_0 |K^(1/2) Omega_0|^2 dU/tau_0. Then tau_v/tau_0 at least E_nu[D_ell] at least exp(-2 beta sum over p in ell of E_nu[x_p]) at least e^(-2 beta b).
Proof. <Omega_0, T_v Omega_0> = z^|E| <K^(1/2) Omega_0, B_0 D_ell K^(1/2) Omega_0> = tau_0 E_nu[D_ell]; nu has mass <Omega_0, T_0 Omega_0>/tau_0 = 1. The top eigenvalue of the positive operator T_v is at least the quadratic form at a unit vector. Jensen. QED
So eps_v is at most 2 beta u b with u the mean plaquette of nu. (VF) asks eps_v at most 1/(25 b). The vacuum trial vector misses by the factor 50 beta u b^2. It pays a thin vortex: a perimeter cost per unit length of the line.

**Lemma VAR2 (power method; PROVED here).** For every n at least 1 put W_n = <Omega_0, T_v^n Omega_0>/tau_0^n. Then (i) eps_v at most -(1/n) log W_n; (ii) W_(2n) at least W_n^2, so the bounds (i) improve along doublings; (iii) W_n is the expectation, in the stationary process of T_0, of the thin open sheet: the product of D_ell over n consecutive half-steps.
Proof. (i) T_v is positive with top eigenvalue tau_v and Omega_0 is a unit vector: <Omega_0, T_v^n Omega_0> at most tau_v^n. (ii) <Omega_0, T_v^(2n) Omega_0> = ||T_v^n Omega_0||^2 at least <Omega_0, T_v^n Omega_0>^2 (Cauchy-Schwarz, unit vector). (iii) Expand T_v^n = (z^|E| K^(1/2) B_0 D_ell K^(1/2))^n between two copies of Omega_0 and divide by tau_0^n: this is the transfer representation of time-ordered products of multiplication operators, with the weight D_ell inserted at each of n magnetic half-steps. QED
ARGUED: if <Omega_0, Omega_v> is not 0 the bounds (i) converge to eps_v, so eps_v = lim of -(1/n) log W_n. Then

  (VF)  <=>  the open 't Hooft sheet of size n x b in the untwisted vacuum has W_n at least c e^(-n/(25 b)) for all n.

In words: a perimeter law for the thin vortex sheet, with an area coefficient below 1/(25 b^2) per plaquette. That is node TH in its equal-time form, and it is node (S1) of row 887 ("a local perimeter law for the equal-time 't Hooft functional").

**Why the attempt stops here (PROVED limits, then ARGUED).**
- Jensen gives only the first cumulant, -2 beta u n b. To reach (VF) the measure must supply the whole first-order term back: the event that the sum of x_p over the sheet is at most about 0 must have probability at least about e^(-n/(25 b)). That is a large-deviation statement about n b plaquettes. No inequality of the class gives it.
- Moving or averaging the line does not help (PROVED): the operators T_(v,ell) for the a b positions of the line are unitarily equivalent (centre link flips), so tau_v at least the top eigenvalue of their average, which is K^(1/2) B_0 [average of D_ell] K^(1/2). The same holds for any convex combination over the homologous dual lines gamma. The bound obtained is E_nu of the average of D_gamma, a sum over thin lines. It is not small only if lines of plaquettes with x_p at most 0 percolate, which they do not at beta 2.3 (GUIDE: negative plaquettes are rare).
- A thick vortex cannot be written as a change of variables. The two classes of boundary conditions are not connected by consistent twists: a pair (Omega_1, Omega_i) must commute or anticommute. The rotation of the cut links by an angle phi about an axis interpolates the operators, with a defect line that again costs a perimeter.
So (VF) holds only through the true response of the vacuum to a thick vortex. This is the vortex free energy itself. The attack on (CORE) stops at node TH = (S1), in the form: a perimeter law for the open thin vortex sheet at one box.

**What stage 2 adds to the graph.** Edge 36: (CORE) <=> (VF) up to the thermal sums s_+, S_v (PROVED-h, Step 5 F3). Edge 37: (VF) <= perimeter law for W_n with area coefficient below 1/(25 b^2) (PROVED-h; the converse ARGUED). The direction of the missing inequality is now a lower bound on a positive expectation. No small number is asked: at b = 24 a the area coefficient may be as large as 1/(25 b^2).

Correction to Step 6 (label). In "Why the attempt stops here" the first bullet (the large-deviation reading of what must beat Jensen) is ARGUED, not PROVED. The second bullet (unitary equivalence and the convex-combination bound) is PROVED; its last sentence is GUIDE. The third is ARGUED.

## Step 7. Attack, stage 3: the next-weakest candidate, the relative form, and where it stops

Stage 2 stopped at node TH = (S1). The next-weakest candidates are the relative nodes of 4.4. I take the conditional form (NGD) through the kurtosis nodes, with the checked Lemma SQ.

READ inputs. (a) Lemma SQ identity (check 883 Section 2, HOLDS): for the stationary chain of P (the ground-state transform of the transfer operator), a real eigenfunction g of a sector of order two, P g = theta g, E g^2 = 1, kappa = E g^4: <g^2, P^t g^2> - theta^(2t) kappa at least 0. (b) Theorem SQ (check 883 Section 3, HOLDS AFTER CORRECTION, for the Wilson operator, which is nonnegative): h = g^2 - 1 is invariant under all centre flips, has mean 0 and norm squared kappa - 1, and <g^2, P^t g^2> at most 1 + (kappa - 1) rho^t, rho = lambda_1^+/lambda_0. (c) Theorem SQ-F (READ gap-brainstorm2-max.md L490; check 883: the displayed bound HOLDS): for a periodic box B, a even, a/2 at least 3, every chi nonzero: p_chi(a) at most (1 + S_ev(a/2)) max(S_ev(a)^gamma, e^(-gamma a)), gamma = (kappa_chi - 1)/(8 kappa_chi).

**Proposition K (a kurtosis floor of any size gives (CORE) from glue; PROVED here from (c) and Lemma SPLIT).** Let B = b^3, a even, a/2 at least 3, eta above 0, gamma = eta/(8 (1 + eta)). If kappa_chi at least 1 + eta for the seven nonzero sectors, S_ev(a/2; B) at most 1, S_ev(a; B) at most 160^(-1/gamma) and a at least log(160)/gamma, then every p_chi(a) is at most 1/80 and Q_0 at most 1/20. With b at least 24 a, Corollary O1 (b) and Theorem SH give the gap on every cube of side at least b.
Proof. (kappa - 1)/(8 kappa) increases in kappa, so gamma_chi at least gamma; both terms of the max are at most 1/160; the prefactor is at most 2. Q_0 = sum of four terms Z_chi/Tr T^a, each at most p_chi (Step 4.4). QED
This repairs edge 23 in absolute form. Check 883's verdict stands: (KURT) does not give the pure (F-h) (exponent 1/2, no prefactor). But (KURT) with ANY eta above 0, plus GLUE at the level 160^(-8(1+eta)/eta), gives the periodic seed directly, with no use of (F-h), (F-l) or (FQ). Edge 38: (KURT)_eta + GLUE => (SEED-FP) at an SH shape. PROVED-h.

**Lemma R (the wall mode; PROVED here from (a), (b)).** For g as in (a), with kappa above 1: rho at least 1 - kappa (1 - theta^2)/(kappa - 1).
Proof. By (b), on the flip-invariant vectors orthogonal to the vacuum P has spectrum in [0, rho], so <h, P h> at most rho (kappa - 1). By (a) at t = 1, <h, P h> = <g^2, P g^2> - 1 at least theta^2 kappa - 1. Divide by kappa - 1. QED
(The same line at general t is Theorem SQ. Lemma R is its t = 1 case read as a variational bound: h = g^2 - 1 is an even trial vector.)

**The crux in its sharpest relative form.**

  (WALL)_M: for the flux ground function g of each nonzero sector of the box, if kappa at most 2 then kappa - 1 at least (a/M) kappa (1 - theta^2).

Reading. kappa - 1 is the variance of g^2: at least (9/16) times the vacuum measure of the wall {|g| at most 1/2}. And 1 - theta^2 is the one-step energy of g: its flip rate. (WALL)_M says: a flux state that is close to a hidden bit flips through its wall slowly, in a time at least of order a/M. In physical time this is a fixed fraction of the short period, so the statement is cutoff-uniform in form.

**Proposition W (PROVED here from Lemma R, Proposition K, Corollary O1; Theorem SH READ).** Let b at least 24 a, a even, a at least 82. Assume GLUE: S_ev(a; b^3) at most 160^(-16) and S_ev(a/2; b^3) at most 1. Assume (WALL)_40 for the seven sectors. Then kappa_chi is above 2 for every nonzero chi, Q_0 at most 1/20, S(a; b^3) below 3/10, and every cube of side at least b has a gap.
Proof. Suppose kappa_chi at most 2. (WALL)_40 and Lemma R give 1 - rho at most 40/a, at most 40/82 below 1/2. Since log(1 - x) at least -x - x^2 on [0, 1/2]: a log rho at least -40 - 1600/a at least -59.6. So rho^a at least e^(-59.6), above 160^(-16) = e^(-81.2). But S_ev(a) at least rho^a (the operator is nonnegative). Contradiction. So kappa_chi above 2 = 1 + eta with eta = 1, gamma = 1/16, 160^(-1/gamma) = 160^(-16), log(160)/gamma = 81.2 at most a. Proposition K applies. QED

**Fact tests of (WALL) (ARGUED unless marked).**
- Z_2 above 2.191, frozen Q_8 and 2T: the winding-line bit flips by a thin vortex membrane placed in one time step (for thin vortices a tilted sheet has more area than a flat one), so the wall has no duration: kappa - 1 is far below 1 - theta^2. (WALL) fails. Consistent with Example 6.2 of row 886 (PROVED there: kappa = 1 exactly with theta anything).
- U(1): kappa at least 3/2 (row 886 Theorem 5.1, PROVED there, unchecked) and 1 - theta^2 is of order e^2/a, so (WALL)_M holds for M of order e^2. U(1) passes (WALL) and fails GLUE. The whole chain fails for U(1) at GLUE, as it must.
- No worst case: (WALL) is one inequality between two moments of one function under the true vacuum measure.
- SU(2), expected (GUIDE, recalled physics, decides nothing): a centre flip of a connected group is a thick vortex; its action falls with its duration (classically like beta pi^2/(2 tau) per plaquette against 2 beta u for the thin one), so flips last several steps and, in a deconfined box, as long as a wall takes to sweep the box. The even mode g^2 - 1 is then slow. The slack is large: Proposition W needs a wall mode of rate at most 40/a, where screening masses in a deconfined box at temperature 1/a are a few times 1/a.

**Where stage 3 stops.** (WALL) is row 886's (HB) with its thresholds made exact (Lemma R is the implication (WALL)_M => "an even excitation with rate at most M/a"). It is OPEN. I tried three ways to prove it and each stops:
1. From connectedness alone. Check 883 already notes kappa above 1 strictly on connected SU(2)^E, with no uniform separation. A one-dimensional double well with a high barrier is a connected diffusion with kappa near 1 and a gapped even sector, so connectedness cannot give (WALL) (the exact diffusion identity E[g^2 Gamma(g)] = E kappa/3 is satisfied there with kappa to 1: PROVED by the chain rule for L(g^4); the Kramers profile gives the value 1/3). What (WALL) needs is the curvature at the top of the barrier, not the barrier's existence.
2. From the absence of one-step jumps. E[(g_1^2 - g_0^2)^2] = 2 <h, (1 - P) h> at most 2 (kappa - 1) (PROVED: P nonnegative). If one-step increments never flip the sign of g, this bounds kappa - 1 below by a constant times 1 - theta. That gives (WALL)_M only with M of order a: a duration of one lattice step. Proposition W needs a duration a/40 in lattice steps, a physical time. No local one-step property gives a physical time.
3. From another even trial vector. Products of three flux functions of sectors summing to zero are even, but Jensen is not available for them; the difference g_2^2 - g_3^2 has small norm for near-bits. No bound.
So (WALL) needs the dynamics of the wall at the scale a: the unstable mode at the centre-symmetric holonomy must relax no faster than 40/a. That is control of the vacuum of a deconfined box, which row 886 named as the obstacle to (HB). The route stops at node (HB).

**Common stop.** Stage 2 stops at: a perimeter law for the open thin vortex sheet (the vortex is free). Stage 3 stops at: a near-bit flips slowly (the vortex is thick in time). Both say that the centre vortex of SU(2) at the seed scale is a thick, light object. Neither is implied by a statement of the class; each is false for the frozen finite groups for the reason that their vortices are thin.

Corrections before the final step.
- Step 2g, constants of (Q-ABS). The budget 1.4e-8 per shape must hold for H_L + sigma_L + S' together. With H_L at most 96 Q_F: take Q_F at most 5e-11 (H_L at most 4.8e-9), each of the four light sums s_z at most 1e-9, S' at most 4e-9; the total is 1.28e-8. Read "(Q-ABS)" with these numbers wherever "1.4e-10" or "GLUE(4e-9)" appears above (Step 2g, edge 32). The proposition and its proof do not change.
- Step 7, way 2. The inequality E[(g_1^2 - g_0^2)^2] at most 2 (kappa - 1) is PROVED. Its consequence "kappa - 1 at least a constant times 1 - theta when increments do not flip the sign" is ARGUED (it is the discrete form of the exact diffusion relation; I did not write a discrete proof).

## Step 8. Final

### 8.1 The graph, compact

Two consumer chains. Chain I: (FQ) -> (F-h) -> FUSE-suff -> (ES) -> Theorem R (all checked), with GLUE and (F-l). Chain II: (SEED-FP) or an SH shape -> gap (checked), -> (GAP) given the account. Their exact flux halves: (Q-ABS) for chain I (Proposition ABS), (CORE) = (Q-FP) for chain II (Lemma SPLIT, Corollary O1).

| Node | Kind | Implies | Implied by | Reaches a consumer | Status tonight |
|---|---|---|---|---|---|
| (SEED-FP) | whole seed | (GAP) given the account (checked chain) | GLUE-FP + (CORE) (PROVED-h, factor 7) | yes, cutoff-uniform | OPEN |
| (CORE): Q_0(a; b^3) at most 1/20, b at least 24 a | absolute, one number | flux half of the SH seed; (NGD) | (VF) + s_+ small (PROVED-h); (KURT)_eta + GLUE (PROVED-h); (WALL)_40 + GLUE (PROVED-h) | yes, with GLUE-FP at 1/10 | OPEN; the weakest absolute form |
| (NGD) | conditional core | seed, with GLUE | (CORE); (FUSE-E)_g; (KURT); (WALL) | yes, with GLUE | OPEN; weakest statement that passes the tests |
| (Q-ABS) | absolute, chain I | (ES) with GLUE (PROVED-h) | every absolute node at fixed coupling, large a | yes at fixed coupling | OPEN |
| (E17) = (P) = TH | absolute, rate | (FQ) at fixed coupling (checked); (Q-ABS) | HA; (C2)+(C1); EXC with c_0 at least g (checked) | fixed coupling only; physical form (E17-phys-CA) (checked, conditional) | OPEN; asks more than needed |
| HA | absolute, area, complex | (P), (R), (C2) (checked) | ? | fixed coupling | OPEN; fails for Z_2 and background-uniform (checked) |
| (C2) | absolute, rate | (E17) with (C1) (checked) | HA (checked); (E17) only with a sign (?) | fixed coupling | OPEN; not weaker than (E17) (check 874) |
| EXC | absolute, rate + boost | (E17) if c_0 at least g (checked after correction) | EXC-W | fixed coupling | OPEN, live (check 881) |
| EXC-W = (DRESS) | absolute, area | EXC | ? | fixed coupling | OPEN; sign of (DRESS) not established (row 888, unchecked) |
| (SEED-DEC-U) | absolute, local event | (FQ) (unchecked) | (S1) + (S2) (ARGUED) | fixed coupling | OPEN (row 887, unchecked) |
| (SEED-DEC-H) | absolute, no rate | stretched-exponential odd weight at m = 0 | z_0 below 8.93e-7 | yes for chain II at fixed coupling, by SPLIT (PROVED-h); not through (FQ) | OPEN; corrects the lead decision of row 887 |
| (S1) | perimeter law for the equal-time 't Hooft functional | (VF) in its sheet form (edge 37) | ? | through (VF) -> (CORE) | OPEN; stage 2 stops here |
| (KURT)_eta | relative | (FUSE-E) (unchecked); (CORE) with GLUE at 160^(-8(1+eta)/eta) (PROVED-h) | (HB) + seed; (WALL) + GLUE (PROVED-h, eta = 1) | yes with GLUE, any eta above 0 | OPEN (row 886, unchecked); pure (F-h) FAILS (check 883) |
| (FUSE-E)_g | relative | (CORE) with GLUE at 160^(-2/g) (PROVED-h, from row 886's bound re-derived) | (KURT) | yes with GLUE, any g above 0 | OPEN |
| (HB) = (WALL)_M | relative, order one | an even excitation of rate at most M/a (Lemma R, PROVED-h) | ? | yes: (WALL)_40 + GLUE -> seed (Proposition W, PROVED-h) | OPEN; stage 3 stops here |
| (HC) + RPF | relative, regularity | dichotomy heavy or ordered (ARGUED) | ? | only with an order-one disorder statement, which is (CORE) | OPEN; dominated by Theorem SH with (CORE) |
| (TS-theta) | area-keeping transverse step | growth with a seed (checked) | holds for Z_2 (checked) | not needed (edge 35) | OPEN; off the critical path |
| (PATH), PIN-MIX | whole seed, path or pinned form | seed at a Wilson coupling; LAND | proved only below 0.361 / 0.0384 | at a Wilson coupling only | OPEN; PIN-MIX is worst-case in form |
| (E17-phys-CA) | absolute, physical | (FQ), K_F cutoff-independent (checked, conditional) | the account's kernel suppliers | yes, with GLUE and (F-l) | OPEN |
| GLUE | even sums small at one physical size | with (NGD): seed | no flux node | needed by every chain | OPEN; no tool tonight |

### 8.2 The chosen statement

(CORE), the flux half of the weakest consumer: on ONE periodic torus (a, b, b, b), b at least 24 a, Z^(v_12)/Z^0 at least 9/10. Its conditional form (NGD) (S_ev(a; b^3) at most s_0 implies (CORE)) is the weakest statement in the graph that reaches a consumer with a cutoff-uniform rate and has the right fact-test profile: false for Z_2 above 2.191 and the frozen Q_8, 2T (ARGUED), empty for U(1) Coulomb, no worst case.
It is genuinely weaker than (E17) as an input: one torus, m = 0, no rate, an order-one threshold. It is not a formal consequence of (E17) without GLUE (the tori differ); with GLUE both lead to the gap, and the gap then returns an (E17)-type bound at m = 0 at the seed's rate. The relative nodes ((FUSE-E), (KURT), (HB)) are incomparable with (CORE); each buys (CORE) with a stronger GLUE, and all of them imply (NGD).

### 8.3 How far the attack got

PROVED here (by hand, elementary, checked by no one):
1. Proposition ABS: the (ES) chain needs only an absolute one-size bound on the heavy weights; a rate enters only through the form (FQ).
2. Lemma SPLIT and Corollary O1: (1 + S_ev)/(1 - Q_0) at most 1 + S at most (1 + S_ev)/(1 - 3 Q_0); the SH seed is S_ev at most 1/10 and Q_0 at most 1/20.
3. Faces F2, F3: theta_P^b/(2 + s_+) at most q at most theta_P^b (1 + s_-); q at most eps_v b + s_+; eps_v b at most 2q/(1 - 2q) + S_v. So (CORE) follows from (VF): eps_v at most 1/(25 b), a lower bound on a top eigenvalue.
4. Lemmas VAR1, VAR2: the vacuum trial vector gives only a perimeter bound, eps_v at most 2 beta u b; eps_v is at most -(1/n) log of the open thin-sheet expectation W_n, with W_(2n) at least W_n^2.
5. Proposition K: (KURT) with any eta above 0 plus GLUE at 160^(-8(1+eta)/eta) gives (CORE) (repairs edge 23 in absolute form).
6. Lemma R and Proposition W: rho at least 1 - kappa (1 - theta^2)/(kappa - 1); (WALL)_40 plus GLUE at 160^(-16), a at least 82, b at least 24 a, gives kappa above 2, (CORE), the SH seed and the gap on every larger cube.
Not proved: (CORE), (NGD), (VF), (WALL) for SU(2) at any coupling in the band. Nothing at order one is proved. No mass gap.
Stops: stage 2 at TH = (S1) (a perimeter law for the open thin vortex sheet, area coefficient below 1/(25 b^2)); stage 3 at (HB) (a near-bit flips slowly). Three attempts on (WALL) recorded with their exact limits (Step 7). Both stops say the same thing: at the seed scale the centre vortex of SU(2) is thick and light.

Ledger corrections (from the PROVED items and READ lines): (i) a rate is an output, not an input; (ii) row 887's question L294 is answered yes, so (SEED-DEC-H) matters at fixed coupling for chain II (it still needs its own seed and GLUE); (iii) (TS-theta) is off the critical path; (iv) (KURT) reaches the seed in absolute form although the pure (F-h) claim fails.

Limits of this note. Rows 886, 887, 888 are unchecked (checks 889 to 891 have no RESULT at this commit); edges that use them are marked. Theorem SH's check (row 707) is by the same model family as its author. The reading "(E17) with GLUE gives (CORE)" is ARGUED. All sizes quoted for SU(2) (string tension, screening masses, slack factors) are GUIDE from recalled numbers. No numeric run was made. I did not open the Sussman-Alpoge sources; statements about the account are READ from lane files that cite them (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). Balaban's estimates are not used here.

### 8.4 The single next statement

(WALL)_40 at one SH box, the exact form of row 886's (HB), in one line for the flux ground function g = Psi_chi/Omega of the periodic box b^3 at time a (b at least 24 a, a at least 82):

  Var(g^2)  at least  min{ 1, (a/40) E[g^4] (1 - theta_chi^2) }.

With GLUE (S_ev(a; b^3) at most 160^(-16), S_ev(a/2; b^3) at most 1) it gives the seed (Proposition W). It is sufficient, not necessary; the necessary and sufficient core is (NGD), and (VF) is its absolute face. A proof must use that a centre flip of SU(2) is thick in time: it is false where the flip is a thin membrane (Z_2, Q_8, 2T), true and useless for U(1) (GLUE fails there), and it names no environment. A proof lane should first decide it in a model where both the wall and the flip rate are computable (the weakly coupled small box, where the wall is the trace-zero holonomy of the toron valley), then say what replaces the one-loop wall at order one.

RESULT: Row 892 (Claude Fable 5.2 max, unchecked): graph built (38 edges, checked ones marked); the weakest sufficient statement is (CORE), one order-one number at one size with m = 0 and no rate (on the torus (a, b, b, b), b at least 24 a, Z^v/Z^0 at least 9/10), in conditional form (NGD); it is genuinely weaker than (E17), which with HA, (C2), EXC, EXC-W and (DRESS) asks a rate or area law the consumer does not need (Proposition ABS, Lemma SPLIT, PROVED here), and (SEED-DEC-H) and (KURT) do reach the seed in absolute form (Proposition K); the attack proved the three-frame form of (CORE) and its variational face (VF) and reduced the relative route to the one-line inequality (WALL)_40 (Proposition W), but proved nothing at order one: it stops at (S1) (perimeter law for the open vortex sheet) and at (HB) (a near-bit flips slowly); next statement for a proof lane: (WALL)_40, Var(g^2) at least min{1, (a/40) E[g^4] (1 - theta^2)} for the flux ground function at one SH box.
