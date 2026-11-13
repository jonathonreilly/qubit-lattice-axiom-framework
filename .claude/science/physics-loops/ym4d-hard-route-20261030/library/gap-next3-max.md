# FINISH row 898, gap-next3-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

## Header

- Row: FINISH 898. Author: Claude Fable 5.2, max effort. Date: 2026-11-13.
- Clone commit read: 11bb5eccae93281d0312d9d4640889a752048fae (branch claude/ym4d-hard-route, pulled --ff-only, already up to date).
- Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030 (read-only).
- Sussman-Alpoge sources: /Users/jonreilly/ym4d-lead/sa (commit 31a47c543775), read in bounded ranges only.
- Marks used: PROVED (mine, in this file), READ (path and line), ARGUED, GUIDE, OPEN.

## Target statement

Decide the next three attacks on the crux of a mass gap for 4D SU(2) lattice Yang-Mills, from the full current status (FINISH rows 830 to 897, the crux graph of row 892 and its check row 893, and SEED-FP). Justify each. Attempt the first step of the top one as a real argument and say where it stops.

Fact tests every candidate must meet (facts, not routes):
- F1. It must fail for U(1) in its Coulomb phase (no gap; Villain U(1) twist theorem, row 786).
- F2. It must use something Q_8 and the binary tetrahedral group 2T lack where they would otherwise pass (rows 838, 843).
- F3. It must not rest on a worst-case single-site bound (cap 2/3), a vertex-block Dobrushin bound (cap 0.775), a background-uniform layer twist bound (cap 4 G_3 = 1.0109, row 839), or the annealed condition (AN1) (row 845).
- F4. It must reach order one (bare beta_W about 2.3 to 2.6; the real object is the Sussman-Alpoge first-passage action, SEED-FP), or reduce the crux to a statement a known tool reaches.

## Plan (one step per response; each step is appended here before the next starts)

1. Read FINISH rows 830 to 897 (RESULT text and every check verdict). Append the row digest.
2. Read gap-crux-core-max.md (row 892), its check (row 893), and gap-finishline-opus.md lines 110-160 (SEED-FP). Append the crux-graph digest.
3. Write the one-page map: consumers, weakest open statements, what is checked, the walls and their exact stopping reasons, and the order-one pattern.
4. List at least ten candidate next attacks, each with crux lemma, payoff, why easier, fact tests F1-F4, and an honest chance.
5. Choose three: reasons, exact crux lemmas, first steps, model and effort, stop conditions, independence.
6. Attempt the first step of the top attack as a real argument. Say where it stops.
7. Self-check the choice against the fact tests and the rows read. Fix any error in place by an appended correction.
8. Write the final RESULT line.

## Step 1. Row digest (READ: D/FINISH.md, lines 907-974 = rows 830-897)

### 1a. Rows 830-838 (READ, FINISH.md lines 907-915)

- 830 (check of 827, Opus): every PROVED step of gap-sos-astra.md HOLDS. SOS surface classes area-small for beta at most 5/11. Constant e^(16/tau_S) about e^1066.
- 831 (lit, luna): Durhuus-Frohlich 1980 already STATE the 4D SU(2) area-law range beta_W below 2/3. Row 825 Theorem A is a checked proof of a stated range, not a new range.
- 832 (GUIDE): 2^4 blocks, gauge-invariant observables. Response row sum below 1 at beta 1, about 2.5 at beta 2. 2^4 blocks do not reach order one.
- 833 (Opus, later checked by 847): (RTAIL-SOS) proved on beta at most 6/25. Encoding stops near 0.2497; 1/3 needs degree-two discovery entropy below 4.51 (it is 5).
- 834 (Opus, check 857): no area law past 2/3. Slab law has only global symmetries. Worst-case single-site chord coefficients have Perron root 3 beta/2. Ceilings: 0.7385 (worst-environment decimated); 4 G_3 = 1.0109 for every background-uniform slab route (given Frohlich-Simon-Spencer). Past 0.7385 needs a nonlinear diamagnetic inequality for O(4) spins in SO(4) backgrounds (OPEN).
- 835 (Opus, check 840): Theorem F: full seed and volume-uniform gap for beta_W below 1/3 (period-2 line field gauge). Every single-link tree-gauge argument stops at 1/3 (Lemma AVG). Glue half for 1/3 to 2/3 OPEN.
- 836 (Opus, check 841): block criterion (BC); star blocks give the seed and gap below 0.3609. Ceiling: no vertex block with worst-case single-link responses works at beta 0.775 or more (Prop CEIL). Villain U(1) at beta at least 2^14 fails (BC) at the coefficient step (Theorem U). Order one needs exterior-uniform or annealed responses of blocks larger than the correlation length.
- 837 (port, Opus): the finish line. The SA flow ends at first passage on the unit lattice with Balaban's effective action; coupling small, not explicit; last integral known only to e^(O(ell^4)). (SEED-FP): one thermal-sum seed below 1/5041 at one physical size, uniform over first-passage data, gives (GAP) (ARGUED composition of checked parts). It is a statement on the actual measure, not on a Wilson weight. Order-one scale: beta_W 2.3 to 2.6 (GUIDE). No fixed beta_W finishes without a renormalization step and a weight comparison.
- 838 (assumptions, Opus): 2I does not bind at order one (freezes near 5.7); Q_8 (freezing about 1.15) and 2T (about 2.15) do. Haar moments of Q_8, 2T, 2O, 2I first differ from SU(2) at degrees 4, 6, 8, 12. A tool at the crossover must see spin 2 or 3. (E17) is a fixed-coupling target, not a physical-torus one. Roughening ceiling near beta 1.9 for absolute surface expansions (GUIDE). Theorem S1 (weak-coupling gap on the twisted thin torus) sits unqueued.

### 1b. Rows 839-847 (READ, FINISH.md lines 916-924)

- 839 (compression, Opus; check 849): no information-theory handle at order one. The seed is exactly a chi-square mutual information between slices. The twist deficit is exactly the chi-square distinguishability of a slice and its centre flip. Proposition TB2: every background-uniform layer twist bound is PROVED false above 4 G_3 = 1.0109 at the flat background (Frohlich-Simon-Spencer). The thick-slab contraction is OPEN.
- 840 (check of 835, astra): all eleven statements HOLD, two repairs. Seed and gap below 1/3 checked.
- 841 (check of 836, astra): core star and seed bounds survive (0.3609). Lemma GF's family quantifier repaired by a covering family.
- 842 (S1, Opus; check 856): S1 not proved. Theorem BAD (chessboard, no SU(2) input), Theorem CH-D (chart over good regions with holes). OPEN: Lemma PE (restricted-ensemble expansion). beta_0(n) of order n^34 log n. Restate S1 as (S1-loc) or (S1-T).
- 843 (Q_8/2T test, Opus; check 854): commutator contraction and W_a area bound hold verbatim for Q_8 and 2T (not order parameters). PROVED low-spin charged filter (V_(5/2), V tensor Sym^4 V): SU(2) Wilson convolution strictly below Q_8, 2T, U(1) eigenvalues at every beta (0.0010 against 0.44 for 2T at beta 2). Exposure about 1 percent per plaquette. Missing: (HS) volume-uniform high-spin rarity in the even one-slice law; then (LS).
- 844 (E17-phys, Opus; check 848): (E17-phys) stated: Q_F at most (K_F/8) rho_*^(A/(3d)) and Q_F below 1/192 at one physical size, rho_* = (2/7)^8/3. Lemma W PROVED. Rough read: Q_F below about e^(-3.7 A/d), near A of 47 xi^2/d under an area law. OPEN: (E17-phys) itself; the glue half.
- 845 (annealed, Opus; check 852): Theorem AG PROVED: annealed condition (AN) gives a block gap with no independence. OPEN: (SP-ext), a space-time Peierls bound for exterior badness along the chain. U(1) Villain fails (AN) at (AN2). GUIDE: small blocks plausibly reach beta near 1, not 2.
- 846 (hand-off, Opus; check 850): EXIT stated: exact block-spin steps past first passage must land the density in an explicit open zone O. Zones are open with explicit radii (Lemma PV). Theorem HO: EXIT gives the bare seed. The first-passage density as written lies in no zone. GUIDE: the order-one band spans length ratio 10 to 600, one to six steps. OPEN: EXIT.
- 847 (check of 833, astra): (RTAIL-SOS), RTAIL, (J12), (E17) on (0, 6/25] checked. Proposition L's universal ban FAILS.

### Lead note received during Step 1 (2026-11-13)

The lead reports that check row 896 (D/library/gap-glue-check-astra.md) of row 895 has landed: row 895 FAILS as written. I verify this against the file itself before using it (next sub-step). A check's verdict overrides the row it checks.

Note: the clone moved during Step 1 from 11bb5eccae93 to e728a52257bd (the lead recorded check 896 in FINISH.md row 896; one line changed). All reads after this point are at e728a52257bdf98dfe0117a593a74caec5399a24. Rows 830-847 were read at 11bb5eccae93 and are unchanged by that commit (git diff --stat: FINISH.md, 1 line).

### 1c. Rows 848-858 (READ, FINISH.md lines 925-935)

- 848 (check of 844, astra): Lemma W, W-phys, the (FQ) corollary given (SD-cyl), Lemma FL HOLD. FAILS: calling it a port matched to the complete account (it rests on the outline). (SD-cyl) needs a complete-account match. (E17-phys) and the glue estimates stay OPEN.
- 849 (check of 839, astra): the 1.0109 ceiling for background-uniform layer twist bounds HOLDS AFTER CORRECTION. No blanket information-theoretic no-go is established.
- 850 (check of 846, astra): the conditional hand-off HOLDS AFTER CORRECTION. FAILS: the n = 226 landing example. EXIT, order-one control and the continuum composition stay OPEN.
- 851 (lit): no published theorem combines Dobrushin-openness with an RG hand-off for pure SU(2). Bounded search.
- 852 (check of 845, astra): Theorem AG holds from literal (AN1)-(AN2), but literal (AN1) is equivalent to an essential worst-case exterior bound. (SP-ext) with eps below 1 FAILS under repeated block updates. Open repair: conditions only on surviving path sums; no model-specific supplier.
- 853 (lit): stationary-averaged coupling and space-time Peierls methods are known for non-gauge finite-spin systems only.
- 854 (check of 843, astra): the low-spin filter theorems HOLD AFTER CORRECTION. (HS), (LS) and the gap stay OPEN.
- 855 (lit): no literature supplier for an interacting one-slice high-spin rarity bound.
- 856 (check of 842, astra): Theorem BAD, RP, CB, Z HOLD for SU(2). FAILS: the twisted-U(1) rider of BAD, W1 and W2 as arguments for restating S1, the claimed equivalence of (S1-T). S1 stays OPEN; Lemma PE is the missing step.
- 857 (check of 834, astra): the (beta/4)A single-site barrier, the decimated chart, the 4 G_3 obstruction given FSS HOLD. FAILS as proved: tau_1 at most 0.2580; tau_* = 1/4 is false on C5. No area law past 2/3; (SE) OPEN.
- 858 (Fable exercise, stopped twice, partial): continued as row 878.

### 1d. Rows 859-866 (READ, FINISH.md lines 936-943)

- 859 (brainstorm 1, Fable then Opus; check 882): PROVED: the tube-conditioned twist covariance is the variance of a conserved Z_2 charge at every separation, so the flux half does not follow from the glue half by clustering. Any strand-counting bound on a local seed needs P(half-integer edge) below 0.2135, against GUIDE 0.267 at beta 2.3. Top idea: hierarchical decoder of the half-integer slice cycle, chessboard recursion z_(j+1) at most C_3 z_j^2, crux (SEED-DEC) C_3 z_0 below 1 at blocks of a few correlation lengths. Both attempts stop inside the order-one band: "they change the seed's form, not its location".
- 860 (HS, Fable; check 864): (HS) PROVED and the wrong target. (LS) equals (E17) up to e^(-c #E). P_- is exactly the event that the half-integer Z_2-cycle of a slice has odd omega-class. GUIDE (8^4): spin-2 density at beta 2.3 is 2e-5. OPEN carrying statement: the dense half-integer Z_2-cycle has trivial omega-class except with probability C a^p eta_*^(a/2); the proof must work on a percolating set (no Peierls count).
- 861 (EXIT, Fable; check 877): an exact soft block step gives the zone's per-link size for free, also for U(1) (Prop FREE); so 0.05 is not the crux. Locality of the landed action is PIN-MIX; proved only below beta 0.0384. Prop VAC: soft step then Theorem HO is circular for the seed. Theorem HL (Higgs-line identity) reduces the seed to torus comparison of local means along a path. OPEN: (PATH) and PIN-MIX from 0.361 to the band; "no inequality was found that avoids a supremum over environments and fails for U(1); no quantity monotone along exact steps and not group-blind was found".
- 862 (PE, Fable; check 880): Lemma PE as printed is FALSE in its (S1-T) clause. Corrected: Theorem A, a transfer gap at least 1/(12.4 n) on the flip-even sector of the twisted thin torus, for beta at least beta_0(n) (order n^54 log n) and even M up to M_1(n, beta). OPEN: every M above M_1; a lower bound on the Z_2 string tension.
- 863 (crux skeleton, Fable; check 879): three direct attacks each stop at the same statement: (SHIFT), (INC), (TORUS). PROVED: Lemma A2 (the model with only the three time-like orientations is seeded at every beta_t); B1 (two-slice law is the Schroedinger bridge of the electric orbit kernel and the slice law; the magnetic coupling enters the glue half only through the slice law); B2 (Hopf fixed-box gap at least 2 exp(-6 beta_t #B), extensive, nothing at seed size); T2 (cut-and-reglue identity). 0.350 at most f(2.5) at most 1.40. Next named: (KS-ZONE), (INC-FP).
- 864 (check of 860, astra): Theorem HS, P1, P2 HOLD. FAILS: the U(1) argument that the filter plus (HS) cannot force (LS). U(1) does not satisfy the filter bound on Sym^5 V. So the spin-5/2 filter is not ruled out as an input to (LS). (E17) stays OPEN.
- 865 (SD-cyl port from the complete account, astra; check 868): conditional port: (SD-cyl-CA) gives rho_CA = c_K/(3 C_K) and the corrected (E17-phys-CA) at rate log(3 C_K/c_K)/(3d) implies (FQ) with cutoff-independent K_F. OPEN: the continuum-kernel identification; the account's unresolved analytic suppliers; the flux and glue estimates.
- 866 (Z_2 parity, astra max; check 870): (E17) is exactly the slice-homology parity problem; the parity form restates the missing charged-sector estimate. PROVED: relative homological analyticity (HA) of the centre-odd marker implies the parity bound. HA is OPEN and stronger. HA fails for Z_2 at beta 5/2 and in a background-uniform SU(2) version. A bound uniform in the environment is false (explicit Z_2 test); an averaged inequality is not refuted.

### 1e. Rows 867-876 (READ, FINISH.md lines 944-953)

- 867 (separation, Opus; check 869): Lemma QS (deleting one plaquette's weight makes its four links conditionally independent): e_(1/2) at most r_(1/2)(5 beta)^4, at most 0.5806 at beta 2.3. Proposition TL: the parity of any edge set is a 't Hooft loop; the parity statement is the wrapping 't Hooft surface. GUIDE: e_F 0.267 for SU(2) at 2.3; 0.40 to 0.75 on the U(1) Coulomb branch; 0.93 frozen 2T; 0.96 frozen Q_8.
- 869 (check of 867, astra): QS and TL HOLD AFTER REPAIRS; certified separation 0.0359. FAILS: the six-candidate exclusion; fact test T3 as stated (the N_t = 3 sampler was invalid). T3 is not established.
- 868 (check of 865, Opus): all six statements HOLD. (E17-phys-CA) implies (FQ) with cutoff-independent K_F, conditional on the account's kernel comparison (h1)-(h3) and the rectangular port. (E17-phys-CA) stays OPEN.
- 870 (check of 866, Opus): (E17) is the slice-homology parity problem (HOLDS). HA implies (E17) (HOLDS). HA is an order-one confinement statement, strictly stronger than (E17), not a shortcut. HA fails for Z_2 at beta 5/2.
- 871 (HA, astra max; check 874): interpolating measures mu_(k,lambda); the deficit is the integral of a response R over [0,1]; it suffices to bound the integral of abs(R) over [lambda_0,1] (C2). Full boundary resummation leaves the SU(2) relative estimate unproved.
- 874 (check of 871, Opus): S1-S6 HOLD. (C2) is NOT weaker than (E17): it restates (E17) or is strictly stronger.
- 872 (filter carries LS?, Opus; check 873): Proposition EXP (identity): d log Tr(P L(s)^t)/d log s = t times the one-slice count of high-spin edges. The filter carries (E17) exactly when EXC holds (integral of Delta ds/s at least c_0, Delta = Cov(N_hi, 1_odd)/p).
- 873 (check of 872, astra): EXP HOLDS. FAILS: the negative conclusion. The filter route stays open: (E17) follows from EXC and nothing proved rules EXC out.
- 875 (EXC, astra max; check 881): isotropic EXC neither proved nor refuted. The electric-only reference has a positive boost response of order the length; no bound on the relative magnetic response at the required scale. Large boosts reverse the sign on even-a tori.
- 876 (brainstorm 2, Fable; check 883): reframing: the consumer (FUSE-suff, library/gap-es1-opus.md L200-236) needs the fusion inequality (F-h): two flux tubes make an even state. It does not need an absolute confinement bound. (E17), HA, (C2), EXC are sufficient routes to (F-h) through confinement. PROVED Lemma SQ, Theorem SQ, Theorem SQ-F: p_chi(a) at most (1 + S_ev(a/2)) max(S_ev(a)^g, e^(-ga)), g = (kappa - 1)/(8 kappa). So the electric part of (F-h) needs only (KURT): the flux ground state's fourth moment kappa at least 1 + c_0 at the seed size, uniform in the cutoff. Second: Lemma RPF, stops at (HC), half-box creation of the flux state with polynomial amplitude. The glue half at order one stays OPEN.

### 1f. Rows 877-887 (READ, FINISH.md lines 954-964)

- 877 (check of 861, astra): FREE, STEP (threshold corrected to beta below 1/sqrt(216 pi)), VAC, HL, K5-K9 HOLD. FAILS: Corollary VAC2's literal equivalence with EXIT. Normalized softening alone supplies no seed.
- 878 (exercise 2, Fable; check 884): no route past the wall. The fresh pass re-derived row 859's ideas almost one for one: "saturation of reformulations for this model". Route E, crux (TS-theta): theta below 4 with F(n_1,n_i | 2n_j,2n_k) at least F(n_1,n_i | n_j,n_k)/theta - C (sheet doubling). Route 2: the marginal-dimension method needs a positive geometric representation, which SU(2)'s signed surface expansion lacks. Lead decision: no further fresh-framing exercise on this inventory until a new input lands.
- 879 (check of 863, astra): B1, T2 HOLD; A2, B2 HOLD AFTER CORRECTION. FAILS as written: T2's probabilistic obstruction, the path converse, several identifications. No open input is discharged.
- 880 (check of 862, astra): the flip-even transfer gap on the twisted thin torus for even M up to M_1(n, beta) is checked.
- 881 (check of 875, Opus): EXC stays LIVE and unproved, with a thin margin. The electric-only boost response passes for U(1), Q_8, 2T, Z_2 too, so it does not single out SU(2). Sharpest open statement: an order-L_i lower bound (at least -theta gamma_min L_i, theta below 1) on the boosted-minus-unboosted, odd-minus-all magnetic-cut plaquette response; the available bound is 4 beta n, order a^3.
- 882 (check of 859, astra): the tube identity HOLDS. FAILS: the numerical strand exclusion; the stated chessboard recursion (C_3 not supplied). (TOP_j) OPEN at that time.
- 883 (check of 876, astra): Lemma SQ and the SQ-F bound HOLD. FAILS: that (KURT) alone supplies pure (F-h); the reframing that the consumer needs (F-h) only; the claimed weakening of (LOC) and (E17).
- 884 (check of 878, astra): F5, Lemma TD, CX1 HOLD; (TS-theta) holds for untwisted Z_2 at beta at least 5/2 with theta = 1. FAILS: the printed Coulomb theta = 4 selectivity; the exemption of Q_8 and 2T from every (ES) test. OPEN: compact-Villain (TS-theta).
- 885 (lit, luna): the marginal-dimension method rests on ferromagnetic random currents and the switching identity. Gauge-side: Forsstrom-Viklund 2025 (positive plaquette-current expansion for Z_2 gauge theory); Aizenman Part III Theorem 9.1 (3D Z_2 gauge by duality); Duncan-Schweinhart 2025 (plaquette random-cluster for Potts gauge). None is non-abelian.
- 886 (KURT, Fable; check 889): (KURT) not proved, not refuted. It is the fusion bound in a stronger form: kappa = 3r/(3r - 2). kappa at least 3/2 when the flip lies on a circle of symmetries (U(1), the O(4) twin); that mechanism is absent for SU(2), Q_8, 2T, Z_2. Counterexamples with kappa = 1 exactly (a product chain; an anisotropic Z_2 gauge theory): (KURT) does not follow from transfer-operator structure. OPEN: (HB) a box with a hidden centre bit has a light even excitation; (FUSE-E): E at least g m for the heavy electric sectors.
- 887 (decoder, Fable; check 891): (TOP_j) PROVED in exact form (hierarchy of 8 classes, ratio 10). Given the chessboard estimate, z_(j+1) at most C_3 z_j^2 with C_3 = 1,120,616. (SEED-DEC-H) is z_0 below 8.93e-7; but the hierarchy gives only exp(-c L^0.301), not (E17). NEW (SEED-DEC-U): 64 P(a box of half the torus side is unclean) at most (K/8) sqrt(S_ev), no reflection positivity, every magnetic background; it reaches the consumer. Identity (PAR): the parity cycle's law is a signed mixture; no bound conditioning on a typical gauge field exists. Filling-Peierls barrier: P(half-integer edge) below 1/9 at best, against GUIDE 0.33. OPEN: (S1) a low-density short-range noise model for the SU(2) one-slice law (a local perimeter law for the equal-time 't Hooft functional); (S2) rigidity of minimal fillings at density 0.12 to 0.17.

### 1g. Rows 888-897 (READ, FINISH.md lines 965-974, at e728a52257bd)

- 888 (EXC magnetic, Fable; check 890): OPEN at the isotropic point. The magnetic bound is the area form EXC-W. R(0) = R'(0) = 0, R''(0) = 4 L_i pi_5 (D_(5/2) - D_(1/2)), about -20 gamma L_i. Theorem 9.3: finite flux tension of the unboosted model, a two-sided order-L_i bound. OPEN: (DRESS), a positive order-L_i excess of half-integer spin at least 5/2 temporal plaquettes on the fundamental flux sheet at isotropic coupling; (EMPTY).
- 890 (check of 888, astra): the flux-response identities, Theorem 3.3, 7.5, 9.3, 9.4 HOLD. FAILS: inferring the carrier crossing or the erasure of the electric gain from second-order data. The erasure at b* is NOT established; EXC is less blocked than row 888 argued. Isotropic EXC and (EMPTY) OPEN.
- 889 (check of 886, astra): the moment hierarchy, the discrete energy identity, the symmetry theorems HOLD. FAILS: the hidden-bit converse; discrete (KURT) implies (FUSE-E); unqualified full-consumer sufficiency. (KURT), (FUSE-E), (HB) OPEN.
- 891 (check of 887, astra): patching, T1, the ratio-ten hierarchy, TOP, TOP+, finite-group selectivity, (PAR) HOLD. The quadratic recursion with C_3 = 1,120,616 HOLDS under the chessboard estimate. FAILS: the universal exclusion of typical-field conditioning; the all-Peierls exclusion. Both seeds OPEN.
- 892 (crux core, Fable; check 893): implication graph, 38 edges. Weakest sufficient statement (CORE): on the torus (a, b, b, b), b at least 24a, Z^v/Z^0 at least 9/10, one order-one number at one size, m = 0, no rate; conditional form (NGD). PROVED reductions: Prop ABS (the (ES) chain needs only an absolute one-size bound on heavy flux weights); Lemma SPLIT and Cor O1 (the Theorem SH seed is S_ev at most 1/10 and Q_0 at most 1/20 on one box); (VF) eps_v at most 1/(25 b); VAR1, VAR2 (vortex energy bounded by the open thin-sheet expectation W_n; W_2n at least W_n^2); Prop K ((KURT) with glue gives (CORE) and the periodic seed without (F-h)); Prop W ((WALL)_40 with glue at 160^(-16), a at least 82, b at least 24a gives kappa above 2, (CORE), the SH seed and the gap on every larger cube). The attack stops at (S1) and (HB). "The glue half is supplied by no flux node."
- 893 (check of 892, astra): SPLIT, O1, F2, F3, VAR1, K, R, W HOLD. ABS, (VF), VAR2 HOLD AFTER CORRECTION. FAILS: (CORE) strictly weaker than (E17) is not established. Edges 10 ((DRESS) equivalent to pointwise EXC-W) and 22 (discrete (KURT) implies (FUSE-E)) FAIL.
- 894 (WALL, Fable; check 897 queued, NO verdict at this commit): under GLUE (a(1 - rho) at least 51.5), (WALL)_40 is exactly kappa at least 2, i.e. (KURT)_1. The scenario to exclude under GLUE: a near-bit with kappa at most 1.13, the only light level of its sector, i.e. a Z_2 topological order of the box. Cor K': kappa at least 1.66 suffices. Exact 2D values: kappa = 2 for SU(2), 2T, 2O; 4 for Q_8; 3/2 for U(1); 1 for Z_2. GUIDE: one SU(2) tube has kappa 1.53 at beta 2.3, so (WALL)_40 can hold at an SH box only through transverse extent. UNCHECKED.
- 895 (glue, Fable): see 896.
- 896 (check of 895, astra; READ in FINISH.md line 973 and confirmed with the lead's note): row 895 FAILS as written overall. Survive: the elementary spectral, mixing and gap-count identities (constant 110592), the even D-shape and the virial identity. Need correction: Proposition SEP, Remark UNTW, face G4, Proposition FIB, Proposition TR's first part. The frozen Q_8 and 2T PASS verdict contradicts prior work. (GLUE-FP), (Z0), (COUNT) at the required size and volume-uniform (BETA) stay OPEN. So I do NOT use row 895's claims that the glue half is independent of the flux half (SEP), that every proved seed proves both halves or nothing (UNTW), or that averaged block conditions are the worst case (FIB), except as corrected in the check file (to be read in Step 2).
- 897 (check of 894): queued, no RESULT at e728a52257bd. Row 894 is unchecked.

Step 1 done. Next: Step 2 (the crux graph, its check, the glue check file, SEED-FP).

## Step 2. The crux graph (row 892), its check (row 893), the glue check (row 896), SEED-FP

### 2a. gap-crux-core-max.md lines 1-250 (READ)

Consumer chain (READ gap-crux-core-max.md L57-70, which quotes gap-es1-opus.md L40-80, L205-223 and gap-vortex-astra.md L128-210):
- Box A = (a, c, d), time a. S_ev(t; B) = Z_0(t; B)/lambda_0(B)^t - 1. Sixteen crossed sectors z = (chi; m). p_z = Z_z/Z_0.
- (ES) at a: eps = S_ev(a; a^3) at most 1e-7 and delta at most 1e-7.
- (F-h): p_z at most K S^(1/2) for the twelve heavy sectors. (F-l): s_z at most K S for the four light ones. FUSE-suff: (F-h), (F-l) at three shapes plus six even sums at most 1e-16/(144 K^2) give (ES). Checked row 753.
- q_(r,i)(m) = (1/2)(1 - Z^(m+v_ri)/Z^m). Q_F = max of q_(1,i)(m). (FQ): 8 Q_F at most K(a) sqrt(S), Q_F below 1/192. (FQ) implies (F-h). Checked row 780.
- (E17): Q_F at most C_2 a^(p_2) eta_*^(a/2) at fixed coupling.
- (SEED-FP): one physical size ell, s_* below 1/5041, S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) at most s_* for every first-passage datum with K at least K_0. Thermal sum of the bare Wilson transfer operator of the periodic cube.
- Proposition ABS (row 892, HOLDS AFTER CORRECTION per check 893): the flux half of (ES) is an ABSOLUTE one-size bound: twelve heavy crossed weights at most about 1e-8 at one size. No rate. (Q-ABS): Q_F at most 1.4e-10 at three shapes at the size where even sums are at most about 4e-9.
- Lemma WS (time doubling): q(2 n_1) at most q(n_1)^2 (1 + s_+)^2. Lemma TD (transverse doubling, checked 884): q(2 n_j) at most 2(1+S)^2 [q(n_j) + S_v/2].
- Lemma RPF and (HC) (row 876): after (HC), the SU(2)-specific flux input is one order-one inequality at one size: "winding lines of length a are disordered across the box; 1/a is below the deconfinement temperature".
- (PATH) (row 861): the whole seed in path form; "no freezing and no Coulomb phase up to beta".
- Graph edges 1-33 (READ L205-246). Checked edges: (E17) <=> parity (P) <=> wrapping 't Hooft surface TH; HA => (P); (C2)+(C1) => (E17); EXC(c_0 at least g) => (E17); (FQ) => (F-h); FUSE-suff; (ES) => gap on centre-blind functions; (E17-phys-CA) => (FQ) cutoff-uniform (conditional on the account); (TS-theta) + 4 percent flux seed => geometric growth.

### 2b. gap-crux-core-max.md lines 251-479 (READ; row 892, statements as corrected by check 893 are in 2c)

- Lemma SPLIT (L262-264): if 3 Q_0 below 1 then (1 + S_ev)/(1 - Q_0) at most 1 + S at most (1 + S_ev)/(1 - 3 Q_0). Corollary O1 (L266): S_ev at most 1/10 and Q_0 at most 1/20 give S below 3/10, the Theorem SH threshold at r = b/a at least 24 (thresholds t(r) = 1/1650 (r=2), 1/100 (3), 1/25 (4), 1/10 (6), 3/10 (r at least 24), READ L267; Theorem SH was checked by the same model family as its author, row 707).
- (CORE) (L296-300): on the periodic torus (a, b, b, b), b at least 24 a, Z^(v_12)/Z^0 at least 9/10, i.e. Q_0(a; b^3) at most 1/20. One torus, m = 0, no rate.
- (NGD) (L318): there is s_0 with: S_ev(a; b^3) at most s_0 implies Q_0 at most 1/20. False for Z_2 above 2.191 and frozen Q_8, 2T (ARGUED); empty for U(1) Coulomb.
- Face F2 (L328-331): q is between theta_P^b/(2 + s_+) and theta_P^b (1 + s_-), theta_P the ratio of the top C_1-odd eigenvalue to the top eigenvalue of the box (a, b, b) (short side a is spatial here; C_1 flips the winding lines of the short direction). (CORE) needs E_P a at least about 0.13 at b = 24 a. GUIDE: true E_P a about 14 at beta 2.3, a = 10. Two orders of slack in the exponent.
- Face F3 (L333-342): q at most eps_v b + s_+, eps_v = log(tau_0/tau_v), the vortex energy. (VF): eps_v(a; b, b) at most 1/(25 b) with s_+ at most 1/100. A LOWER bound on a top eigenvalue: the variational direction.
- Lemma VAR1 (L352-354): tau_v/tau_0 at least E_nu[D_ell] at least exp(-2 beta b u). The vacuum trial vector pays a thin vortex and misses by 50 beta u b^2.
- Lemma VAR2 (L356-358): W_n = <Omega_0, T_v^n Omega_0>/tau_0^n; eps_v at most -(1/n) log W_n; W_2n at least W_n^2; W_n is the open thin 't Hooft sheet of size n x b in the untwisted vacuum. (VF) is a perimeter law for the thin vortex sheet with area coefficient below 1/(25 b^2). This is (S1).
- Why stage 2 stops (L371-374): Jensen gives only the first cumulant. Averaging thin lines does not help (unitary equivalence, PROVED). A thick vortex cannot be written as a change of variables. "(VF) holds only through the true response of the vacuum to a thick vortex."
- Proposition K (L386-388): kappa_chi at least 1 + eta for the seven sectors, plus S_ev(a) at most 160^(-1/gamma), gamma = eta/(8(1 + eta)), gives Q_0 at most 1/20.
- Lemma R (L390-392): rho at least 1 - kappa (1 - theta^2)/(kappa - 1). (WALL)_M (L396): if kappa at most 2 then kappa - 1 at least (a/M) kappa (1 - theta^2). Proposition W (L400-401).
- Where stage 3 stops (L409-413): (WALL) is (HB) made exact. Three proof attempts fail: connectedness alone (a double well is a connected diffusion with kappa near 1); absence of one-step jumps (gives duration one lattice step, not a physical time); other even trial vectors.
- Common stop (L415): "the centre vortex of SU(2) at the seed scale is a thick, light object ... each is false for the frozen finite groups for the reason that their vortices are thin."
- Suggested first model (L472): the weakly coupled small box, where the wall is the trace-zero holonomy of the toron valley.

### 2c. Check 893 of row 892 (READ gap-crux-core-check-astra.md, all 192 lines)

HOLDS: SPLIT, O1, F2, F3, VAR1, Proposition K, Lemma R, Proposition W. HOLDS AFTER CORRECTION: ABS, (VF), VAR2. FAILS: "(CORE) genuinely weaker than (E17)" as an established ordering. Corrections I carry forward:
- (VF) is a SUFFICIENT face of (CORE), not an equivalence at the printed constants (check section 6). s_+ of the crossed (a, b, b) box is not S_ev(a; b^3); the two glue hypotheses stay distinct.
- VAR2 made precise (check section 8): with M_0 = c B_0^(1/2) K B_0^(1/2), psi_0 its positive unit vacuum, stationary law psi_0^2 dU = nu: W_n = E_nu[D_ell(X_0) ... D_ell(X_(n-1))], and c_v e^(-n eps_v) at most W_n at most e^(-n eps_v) with c_v = |<Omega_0, Omega_v>|^2 above 0 at each fixed box. "Identifying it with the equal-time spatial-loop hypothesis (S1), or with E17's wrapping partition-function ratio, needs an additional bridge."
- Correct replacement (check section 12): "CORE plus S_ev(a; b^3) at most 1/10 is a one-size sufficient condition for the SH seed. No input decay rate is needed ... Its logical ordering relative to E17 is not established." Existential (NGD) can be vacuous at a fixed box; it is useful only with a supplied glue bound and the all-datum quantifier.
- SH scope (check section 3): SH gives a volume-uniform lattice gap at each fixed seed datum. A uniform physical application requires a seed for EVERY first-passage datum at fixed physical time and shape.
- Edge 10 FAILS: (DRESS) is an integrated bound; pointwise EXC-W implies it, not conversely. Edge 22 FAILS: discrete (KURT) does not imply (FUSE-E) (kernel counterexample on Haar SU(2)). Proposition K avoids edge 22 and survives.
- Edge 12 (SEED-DEC-U => FQ): the factor 64 holds only for the spatial cube; 128 or 256 for the other consumer shapes.
- Edge 14: (SEED-DEC-H) needs z_0 below 1/1,120,616 with a uniform strict margin; the chessboard premise (CE) is unsupplied for the actual one-slice law.
- "A large-box spectral gap does not by itself bound a thermal TRACE at time proportional to box side: multiplicities can grow."
- Not covered by the check: the phase tests for U(1), finite groups, weakly coupled SU(2); the recalled sizes; the failed-attack exclusions of Steps 6-7.

### 2d. Check 896 of row 895, the glue half (READ gap-glue-check-astra.md L60-66, L116-402, L501-538)

Verdict: row 895 FAILS as written. What survives, and what I use:
- G1-G3 HOLD. G4 after correction: 1 + S_ev = exp(Cas) A_cross, A_cross = (1/4) sum over m of sigma_m, at least 1/4. So GLUE at level sigma implies only Cas at most log 4 + log(1 + sigma) (L116-137). The reading "no Casimir energy" does not follow.
- Lemma CS HOLDS: Cas = a b [e(a,b,b)/a - e(b,b,b)/b] at least 0. Its exclusion of other methods FAILS: "CS supplies a sign, not a classification of proofs or a prohibition of trial-vector arguments" (L199-215).
- SEP after correction (L139-171): neither one-box numerical half implies the other in the abstract class (a compact Gaussian product model; fixed-box Z_2 at large beta from Lemma Z2-c). Not a statement about SU(2) along first passage.
- UNTW after correction (L173-197): a bound that uses ONLY untwisted partition numbers and the class axioms bounds the full sum. It is NOT an impossibility theorem for one-box proofs.
- LOC (L216-243): local gauge-invariant functions with cuts are centre-even. The converse and the "universal ceiling" do not follow: 0.3609 is a proved sufficient range, not a demonstrated ceiling; the 1/3 and 0.775 obstructions concern their specified worst-case constructions.
- FIB after correction (L245-279): the operator inequality for ALL fibre-dependent vectors is the essential worst case. "An averaged scalar estimate, a weighted estimate with a bad-set term, or an estimate only for exterior-independent tests is a different hypothesis." The dichotomy "every averaged condition is the worst case or the claim" is NOT proved.
- UP (L296-310): G_0(2t) at most 64 G_0(t) (not 1728). A bounded count at one physical size propagates to finitely many doublings.
- Lemma G5 HOLDS (L312-332): with t = a/2, b = 24a: m_ev a at least 2[110592 G + log(1/sigma)] and G_0(a/2) at most G give S_ev(a; b^3) at most sigma. Not the weakest pair.
- TR (L334-402): on positive even branches, -E'/E at most C integrates to E(beta_1) at least exp(-C Delta beta) E(beta_0). TR1 gives a fixed-bare-coupling seed conditional on one C uniform in the boxes. D5: analyticity and non-closure of the lowest gap do NOT imply the all-level bound. "Wilson needs a separate all-level estimate."
- Fact tests (L403-433): frozen Q_8/2T PASS for static GLUE FAILS (they have a non-small even trace at every box for large beta: distinct even flat states). Z_2 passes static GLUE on a fixed box at large beta while flux fails (HOLDS AFTER CORRECTION). U(1) Coulomb failing GLUE is GUIDE only.
- OPEN: (GLUE-FP), (Z0), (COUNT) at the required size, volume-uniform (BETA).

### 2e. SEED-FP (READ gap-finishline-opus.md L100-175; row 837, a port by Claude Opus 5.5 of the Sussman-Alpoge account; credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text)

- (SEED-FP) (L119-123): K_0, a physical size ell, s_* below 1/5041, and for every first-passage datum (K, beta) at g with K at least K_0: S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) at most s_*. The thermal sum of the bare Wilson transfer operator of the periodic cube of physical side ell at physical time ell/2.
- Same statement on the account's densities (L125): the integral of rho_k dV_k equals Z at every level, exactly. The account constructs rho_K on untwisted tori with four equal sides only.
- (SEED-L) (L128): limsup of Phi_L = L^4 log Z_(K,ell,beta) - log Z_(K,L ell,beta) at most phi_* below (L/2) log(13/10). Both tori are in the account's family. By the dilation identity Phi_L = L^4 F_(K,ell,beta) - F_(K+1,ell,beta): the defect of one more block step on one torus at one bare coupling. Lemma FL (L130-136; checked row 848 with phi' in place of phi_*) turns (SEED-L) into (SEED-FP) at a larger size.
- 2.3 (L138-145): the seed must be a statement about the actual measure. A seed for a plain Wilson weight at the unit scale does not give (SEED-FP): the account bounds the difference only by e^(O(ell^4)); (SEED-L) needs absolute accuracy below 0.13 L on tori of at least (20 xi)^4 cells. "Nothing known bounds their distance from it."
- 2.4 (L147-152): one size, one margin, all large cutoffs. No uniformity in the volume, in g, or in boundary values is needed. The consumer route needs K bounded independently of the cutoff. The twisted forms are outside the account's present scope (untwisted tori only).
- 2.5 (L154-165): granted the account, (SEED-FP) is the whole remaining content of (GAP).
- 2.6 (L171): (SEED-FQ) needs even sums near 1e-16 (m a about 42 + 2 log K), against about 12 inverse masses in time for the direct seed.
- The continuation (Theorem S) "holds for every group and for every symmetric model with positive transfer operators" (L113): it uses only (TM) and axis exchange.

Step 2 done. Next: Step 3, the one-page map.

## Step 3. The one-page map (from Steps 1-2; every line points to a row read above)

### 3.1 Consumers (what a finished statement must feed)

- C-FP. (SEED-FP): S(ell/(2 a_K); (ell/a_K)^3) at most s_* below 1/5041 for every first-passage datum, one physical size. Gives (GAP) granted the account (row 837; steps (a), (b) checked, (c)-(f) ARGUED).
- C-SH. One SH shape: S(a; b^3) at most t(r); at r at least 24 it splits into GLUE S_ev(a; b^3) at most 1/10 and (CORE) Q_0(a; b^3) at most 1/20 (rows 892, 893: SPLIT, O1 HOLD). Needs the CONFINED flux pattern.
- C-ES. (ES) at a: S_ev(a; a^3) at most 1e-7 and delta at most 1e-7. Gives the gap on centre-blind (tr F^2) functions (Theorem R, EV-L; checked rows 744, 732). Its flux input is Theorem V: delta is small exactly when twelve of the sixteen crossed weights are small and four are light, for ANY set of four (READ row 892 L150-158, quoting gap-es1-opus.md L60-80).
- Every consumer needs the bound for all first-passage data at one physical size (cutoff-uniform). At a fixed bare coupling the same statements give a lattice gap.

### 3.2 Weakest open statements on the path

- Flux half, confined form: (CORE), one number, m = 0, no rate (row 892; ordering against (E17) not established, check 893). Sufficient faces, all OPEN: (VF) (variational; a perimeter law for the open thin vortex sheet), (KURT)_eta with GLUE, kappa at least 2 or 1.66 (rows 892, 894), (E17) and its forms (parity, wrapping 't Hooft surface, HA, (C2), EXC, (DRESS)), (SEED-DEC-U), (SEED-DEC-H) with (CE).
- Glue half: (GLUE-FP), S_ev at most 1/10 at one box. Sufficient pairs, all OPEN: (Z0) with (COUNT) (Lemma G5); (BETA)_C along a coupling path (TR; needs an all-level derivative bound, check 896 D5).
- Whole seed: (PATH) (torus comparison of local means along a coupling path, row 861); (SEED-L) (defect of one block step below 0.131 L, row 837); EXIT with PIN-MIX (rows 846, 861).
- Cutoff form of the flux consumer: (E17-phys-CA) (rows 865, 868; conditional on the account's kernel comparison).

### 3.3 What is checked (by another provider unless said)

- Ranges at fixed bare coupling: seed and volume-uniform gap below 0.3609 (row 836, check 841); below 1/3 by line-field gauge (row 835, check 840); area law below 2/3 (row 825, check 828; range stated by Durhuus-Frohlich 1980); SOS surface classes to 5/11 (check 830); (RTAIL-SOS) and (E17) on (0, 6/25] (check 847).
- Weak coupling, reduced geometry: flip-even transfer gap on the twisted thin torus for even M up to M_1 (row 862, check 880).
- The reduction chain: (FQ) to (F-h) to FUSE-suff to (ES) to Theorem R to (G_ev); Corollary S3'; Theorem SH (same model family); SPLIT, O1, F2, F3, K, R, W; Lemma SQ; the tube identity; (E17) = parity = wrapping 't Hooft surface; HA implies (E17); EXP; QS; TOP, TOP+; Lemma W; the conditional hand-off HO; Theorem HL; B1, T2.
- Nothing at order one is proved. No statement in 3.2 is proved at any coupling above 0.3609 (seed) or 2/3 (area law).

### 3.4 Walls, with the exact stopping reason

| # | Attack (rows) | Where it stops, exactly |
|---|---|---|
| W1 | Single-site Dobrushin, tree and line gauges (834, 835) | Worst-case chord coefficients are (beta/4) times adjacency, Perron root 3 beta/2: cap 2/3. Tree gauges: Lemma AVG, cap 1/3. |
| W2 | Vertex and star blocks (836) | Proved to 0.3609. Worst-case single-link responses fail at 0.775 (Prop CEIL; scope: that family of majorants, rows 861, 896). |
| W3 | Background-uniform slab or layer bounds (834, 839) | PROVED false above 4 G_3 = 1.0109 at the flat background (Frohlich-Simon-Spencer). Past 0.7385 needs a nonlinear diamagnetic inequality (OPEN). |
| W4 | Annealed block condition (845) | Literal (AN1) equals the essential worst case (check 852). (SP-ext) fails under repeated block updates. No supplier for surviving-path conditions. |
| W5 | Signed surface expansions (833) | Encoding entropy: stops near 0.2497; degree-two discovery entropy 5, needs below 4.51. GUIDE roughening ceiling near 1.9 for absolute expansions. |
| W6 | Information theory (839) | Every candidate restates the seed or is group-blind. No blanket no-go (check 849). |
| W7 | Spin filter, (HS), EXC (843, 860, 872, 875, 888) | (HS) proved and the wrong target. EXC is live: it needs an order-L_i bound on the relative magnetic response; the available bound is 4 beta n, order a^3. (DRESS) OPEN. |
| W8 | Parity, HA, (C2) (866, 871) | HA is an area law plus a complex disc, stronger than (E17). An environment-uniform conditional bound is false (Z_2 test above 2.191). (C2) restates (E17). |
| W9 | Decoder (859, 887) | (SEED-DEC-H) needs z_0 below 1/1,120,616 and a chessboard estimate (CE) that is not supplied for the one-slice law. (SEED-DEC-U) asks p_0 about 1e-12. Stops at (S1) and (S2). |
| W10 | Kurtosis, wall (876, 886, 892, 894) | (KURT) does not follow from transfer structure (kappa = 1 examples). Under GLUE, (WALL)_40 is exactly kappa at least 2: exclude a Z_2 topological order of the box (894, unchecked). GUIDE: one tube has kappa 1.53. |
| W11 | Variational face (892) | The vacuum trial vector pays a thin vortex (Jensen: first cumulant only). Thin lines cannot be averaged into a thick vortex. No change of variables makes a thick vortex. |
| W12 | Hand-off EXIT (846, 861) | Per-link size is free (FREE). Locality of the landed action is PIN-MIX, proved only below 0.0384. Soft step plus HO is circular for the seed (VAC). No monotone, non-group-blind quantity found. |
| W13 | Direct skeleton (863) | (SHIFT), (INC), (TORUS): one statement in three forms. Hopf gap is extensive. |
| W14 | Glue (895, 896) | Row fails as written. Elementary identities survive. Trial vectors give the wrong side for the short box. (BETA) needs an all-level estimate. No tool named. |
| W15 | Twisted thin torus S1 (842, 862) | Window M at most M_1. Beyond: flux -1 defects at positive density; a lower bound on the Z_2 string tension. Off the order-one crux. |
| W16 | Sheet doubling (878) | (TS-theta) holds for deconfined Z_2 (theta = 1); the selectivity sits in its seed. Off the critical path. |
| W17 | Fresh-framing exercises (858, 859, 876, 878) | The fresh pass re-derived the earlier idea list almost one for one. Lead decision: no further fresh-framing exercise on this inventory until a new input lands. |

### 3.5 The pattern

- Every route that survives the fact tests ends at ONE order-one number of the true SU(2) measure at a box a few correlation lengths across, with no small parameter: (CORE) or its faces; kappa at least 2; GLUE; z_0; (DRESS).
- The reductions around these numbers are in good shape (many checked). The numbers have no supplier. Reformulation has saturated (row 878).
- Three things were NOT tried, by my reading of rows 830-897 (to be verified by grep in Step 4): (i) a consumer that does not need the confined pattern (C-ES accepts any pure pattern, but every flux lane aimed at confinement); (ii) the glue half as a thermodynamic statement with a proof direction of its own; (iii) tools from outside the transfer-operator and Dobrushin frame (positive Z_2 x SO(3) representation, Tomboulis-Yaffe and Mack-Petkova inequalities, multiscale Bakry-Emery, Chatterjee's strong-mass-gap mechanism).

### Correction to 3.5 (after a grep of the lane library and a read of gap-brainstorm2-max.md L145-300)

The last bullet of 3.5 is WRONG as written. The grep shows the lane read or used all the outside tools I named: Tomboulis (49 files), Mack-Petkova (29), Polchinski and Bauerschmidt-Bodineau (16, 24), Chatterjee (32), the SO(3) x Z_2 splitting (38), Migdal-Kadanoff (33). Row 876's file already holds, as ideas: the planted Z_2 gauge theory (idea 2), the twist-eaters (15), the Migdal-Kadanoff toy (16), the heat-kernel action (17), orbit-space curvature (18), a centre-disordering mixed action (31), pattern selection (32, dropped: "(ES) gives the gap for every pattern"), (ES) as a low-temperature equation of state (G4), two rivals and two inputs (G5), a consumer with a vacuum multiplet (G11), the 2D O(4) twin (G7), 2I as a finite twin (G13).
Corrected bullet: what the FINISH rows 830-897 show is that every PROOF lane on the flux half aimed at the confined pattern ((E17), EXC, (KURT), (WALL), the decoder, (CORE)), and that the glue half had one proof lane (row 895, failed as written). The ideas G4, G5, G11 and 31 of row 876 (the gap needs only pattern purity and the glue half; the rivals of the two halves differ; a regularization can make the flux half a Z_2 expansion) were recorded and NOT given a proof lane. READ gap-brainstorm2-max.md L237, L242, L257-258, L264.

### 3.6 Inventory of ideas the lane already scored (READ gap-brainstorm-max.md L277-345, row 859; gap-brainstorm2-max.md L145-352, row 876). I do not repeat these as "new".

Row 859 (52 ideas), by title: frustration bootstrap (non-abelian diamagnetic bound); covariant spectral edge; the canonical (Doob) chain; stochastic localization along plaquette tilts; chessboard for typical backgrounds; a defect-angle identity (class function w_phi, phi from 0 to 2 pi); the twist as two SO(3) boundary rotations; the twist free energy as a running coupling with a step-scaling inequality; gradient-flow transport; Polchinski transport of a thick vortex; Nielsen-Olesen mode; non-amenability (Bourgain-Gamburd); intertwiner between sectors; expand around the rough sheet; SO(3) x Z_2 variables with Griffiths for the centre part; soft fusion; end the flow on Wilson by projection; a theorem-grade Q_8 rung; Furstenberg for the tangent flow; Witten Laplacian on one-forms as one covariant particle; Hormander; the 2D O(4) sibling; trees; topological order in reverse; self-avoiding-surface tree; just count; orbit-space curvature; Nishimori line; an exact scale identity (trace anomaly, Michael sum rules); soft percolation (finite energy, Burton-Keane); continue in the twisted geometry; anisotropic action from beta_s = 0; a second handle (large N, Higgs, level truncation); 3D first; sum over twists or walls; continuum first in a small twisted box; Hamiltonian valley with Agmon estimates; a Simon-Lieb criterion on the conditional Z_2 system; conditional theorems that halve the problem (NOCRIT); no flow, a monotone step; SU(2) as the 3-sphere (O(4) vector model); hyperbolic lattice; twist and antitwist with tube conditioning; flux from glue by clustering (REFUTED by the tube identity); chi-square martingale in the tube radius; Hellmann-Feynman continuation; equidistribution of the Stiefel-Whitney class; the mean Hessian is diagonal; cut the sheet out; level truncation ladder; the seed as one more block step by a chessboard sandwich; Simon-Lieb on the Nishimori line.
Row 876 (42 + 18 ideas): listed in the correction above, plus G1 (transverse reflection positivity fuses two tubes), G2 (Witten Laplacian with a convex-paramagnetic split), G6 (flux half as one order-one statement, a lower bound on the deconfinement temperature), G17/G18 (fusion by squaring; a window for the kurtosis).
Row 878: sheet doubling (TS-theta); the marginal-dimension method (needs a positive geometric representation).

Consequence for Step 4. A candidate counts as outside this inventory only if its crux lemma is not one of the above. I mark each candidate NEW, VARIANT (of a named idea) or KNOWN.

Step 3 done. Next: Step 4, candidates, in batches of three or four per response.

### Lead note received before Step 4 (2026-11-13)

The lead reports row 900 (D/library/gap-mine858-opus.md), which mined the partial file of row 858. Three items: (1) route W, a vector-state Theorem S on free-wall boxes (no flux sector, no twist), crux (W-ENG); (2) the account's fixed-horizon universality (YM4_1400 L94031ff), crux (UNIV-FP); (3) the integrated sheet-coupling identity E6, crux (SURF). I read the file itself before using them (next sub-step).

### 3.7 Rows 899-900 (READ at clone commit 6358162252bda961ab106b0d8dae4b3811e1daa8; FINISH.md lines 976-977; gap-mine858-opus.md L97-147)

- 899 (assumptions exercise on five walls, Fable): queued, no RESULT at this commit.
- 900 (mining row 858's partial, Opus 5.5 high, unchecked): 59 items; 40 covered later, 7 untouched, none reaching order one. The three the lead named, as READ:
  - Route W (L125-131): a box with FREE walls in all four directions; Z_free(t, l, l, l) = <1, L^t 1>, the constant-vector matrix element, so no flux sector and no twist. Vector thermal sum S_W(N; B) = sum over k at least 1 of (|c_k|^2/|c_0|^2)(lambda_k/lambda_0)^N. Crux (W-ENG): S_W(N; (2N)^3) below s_W at one N implies a gap at least log(1/(C S_W))/N on the cyclic subspace of 1 for every larger free-wall box. Axis exchange survives. Then a second node: free-wall boxes to the account's state. "It removes the flux half from the form of the seed"; what remains is the glue half on free-wall boxes.
  - (UNIV-FP) (L134-138): does the account's fixed-horizon universality (YM4_1400 L94031ff; it "does not compare different horizons") apply at the first-passage horizon with K-uniform constants, and bound the seed difference between two bare weights below s_*/2? If yes the lane may choose its bare weight, for example one with no Z_2 monopoles, where the centre is conditionally an unfrustrated Z_2 theory with Griffiths inequalities.
  - (SURF) (L140-145): integral over the sheet coupling of the absolute sheet response at most C a^p eta_*^(a/2). Probably (E17) or stronger; its free end is group-blind.
- Row 900's own reading: item 1 "moves the form of the crux, not its location"; items 2 and 3 do not move it.

## Step 4. Candidates

Format per candidate: label (NEW, VARIANT, KNOWN against 3.6-3.7); crux lemma; what it buys; why it might be easier; fact tests F1 (fails for U(1) Coulomb), F2 (uses what Q_8 and 2T lack where they would pass), F3 (no worst-case single-site or vertex-block bound, no background-uniform layer bound above 1.0109, not (AN1)), F4 (reaches order one or reduces to a statement a known tool reaches); two chances: P1 that the first lemma lands, P2 that the route supplies an order-one seed. All chances are my judgment (ARGUED). No candidate has a known tool for the order-one number; P2 is small everywhere and I say so.

One reading that orders the list (ARGUED from READ lines). The target (GAP) is a gap on the centre-blind (tr F^2) sector (READ gap-finishline-opus.md L164). Frozen finite groups are gapped there. The flux half enters the lane's consumers only because periodic boxes carry flux sectors and twists. So the two halves have different rivals (row 876 G5): the flux half is bound by Z_2, Q_8, 2T; the glue half only by gapless models (U(1) Coulomb; the mixed-action endpoint K7). Twenty rows (860-894) attacked the flux half in the confined pattern. The glue half had one row.

### 4.1 Batch 1: candidates that change the shape of the crux

**C1. Route W: a seed engine on boxes with free walls. VARIANT of row 858/900 item 1 (no proof lane yet); my variant W' is NEW as stated.**
- Setting. Free walls in the three space directions. Two readings of the same numbers: (W) free walls in time too, Z = <1, L^t 1> (row 900); (W') periodic time, Z = Tr L_B^t over the free-wall box B. In a free-wall space box every centre flip across a plane is a gauge transformation (the box has no closed winding), so there are no flux sectors and no twists (ARGUED; one line: multiply by -1 at all sites beyond the plane).
- Crux lemma (W'-ENG). There are absolute s' and C with: S_fw(a; b^3) := Tr L_(b^3)^a/lambda_0^a - 1 at most s' at one shape (a, b), b at least 2a, implies that the transfer operator of every free-wall box of sides at least b has a gap at least log(1/(C s'))/a. (W-ENG, row 900: the same with the vector sum S_W and a gap on the cyclic subspace of 1 only.)
- Buys. The whole seed becomes ONE glue number: the thermal sum of a free-wall box. No flux half, no twist (the account reads untwisted objects only, row 837 2.4 item 4), no Q_8/2T test (they are gapped and satisfy a free-wall seed). The rivals left are U(1) Coulomb and K7.
- Why easier. It is an implication in the class (positive transfer operators, axis exchange), where the lane's tools work and most results are checked. It asks nothing at order one.
- Tests. F1: the engine holds for every group; the seed fails for U(1) (photon thermal sum of a box is scale-free and of order one; row 900 gives about 9 for gap times side; ARGUED). F2: not needed, and that is the point. F3: no conditional bound. F4: reduces the crux to glue-only; no tool for the glue number.
- Risks. (i) The trace version needs axis exchange between a periodic and a free direction: exchange turns Tr into a vector element <1, L'^n 1> on a cross-section with one periodic direction. The engine must run on this mixed family. (ii) The vector version W gives a gap only on the cyclic subspace of 1; that is wall-to-wall decay, not decay of local observables (ARGUED; see Step 6). (iii) Second node: the free-wall limit state must be the account's state.
- Chance. P1 (an engine theorem in some free-wall form) 45 percent. P2 2 percent (it supplies no number).

**C2. Regularization freedom: (UNIV-FP). KNOWN (row 900 item 2); a port, not a proof.**
- Crux question. Does the account's fixed-horizon universality (READ via row 900: YM4_1400 L94031ff) hold at the first-passage horizon with constants uniform in K, and bound the seed difference between two bare weights below s_*/2?
- Buys. The right to pose (SEED-FP) for a chosen bare weight. It is the precondition of C3 and C4.
- Why easier. It is a reading of the account (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text).
- Tests. F1-F3: not applicable (inside the account). F4: does not move the crux by itself; the physics at the seed scale is the same for every weight in one universality class (ARGUED).
- Chance. P1 (a yes or no with lines) 90 percent; that the answer is a usable yes, 25 percent. P2 0 by itself.

**C3. A centre-disordering bare weight plus a consumer with a vacuum multiplet. KNOWN as ideas 31 and G11 of row 876 (top five, item 4, crux (MULTIPLET)); no proof lane.**
- Crux lemma (MULTIPLET). For the mixed weight exp(beta_F chi_F + beta_A chi_A) with beta_F fixed below the Z_2 threshold: (a) fundamental loops obey an area law for every beta_A (Mack-Petkova 1979 and Frohlich 1979, recalled in row 876; to be rebuilt in the repo); (b) Theorems S and R hold for a transfer operator with a known quasi-degenerate multiplet of eight vacua (the SO(3) bundle classes of a slice).
- Buys. The flux half by a convergent Z_2 expansion, uniform along the continuum limit. A known tool reaches it. The crux is then the glue half alone.
- Why easier. Thin vortices are cheap by choice of the weight.
- Tests. F1: U(1) has no centre quotient of this kind. F2: uses the Z_2 quotient, which Q_8 and 2T also have: they would pass (a) too, correctly (their fundamental loops are disordered by the same thin vortices). F3: none. F4: reaches the flux half only.
- Risks. Needs C2 (or the account redone for a mixed weight). The limit beta_A to infinity at fixed small beta_F is the SO(3)-type theory; whether the account's trajectory covers it is not known to me (OPEN).
- Chance. P1 30 percent (needs C2 = yes). P2 1 percent. Dominated by C1 if C1 lands, because C1 removes the flux half with no change of weight.

**C4. A monopole-free bare weight and Griffiths inequalities for the centre. VARIANT of row 859 ideas 15, 38, 52 and row 900's example.**
- Crux lemma (GKS-C). For a weight with no Z_2 monopoles, conditional on the SO(3) part the centre is a Z_2 gauge theory with couplings of one sign; then centre-odd observables obey Griffiths and Simon-Lieb type inequalities on average over the environment, and a finite-size criterion for the flux half follows.
- Buys. A finite-size criterion for the flux half with averaged (not worst-case) input.
- Why easier. Correlation inequalities exist for ferromagnetic Z_2 gauge theory (READ row 885: Forsstrom-Viklund 2025; Aizenman Part III).
- Tests. F1: fails (no centre mechanism for U(1) Coulomb). F2: FAILS the test as a route to confinement: at order one the couplings K_p = beta |x_p| are about 1.4, far above the Z_2 threshold 0.44, so the centre is slaved and Griffiths bounds point toward order (ARGUED; row 876 idea 2 says the same: "mechanism only where the centre is not slaved"). F4: no.
- Chance. P1 20 percent, P2 below 1 percent. Listed for completeness; I do not choose it.

### 4.2 Batch 2: candidates for the order-one glue number

After C1 the remaining number is (FW-SEED): S_fw(a; b^3) at most s' at one physical shape, for every first-passage datum. In words (ARGUED, as row 876 G4 for (ES)): the thermal pressure of the theory in a free-wall box at temperature 1/a is at most about s' T^4 (a/b)^3. For s' = 1/10 and b = 2a this is p/T^4 at most about 1e-2; the free gluon gas has 0.66 and the photon gas 0.22 (recalled Stefan-Boltzmann values, GUIDE). The box need not be large: the seed asks a pressure fifty times below the free value at one temperature. This is weaker in numbers than (ES) (1e-7) and than (SEED-FQ) (1e-16), if an engine with an order-one threshold exists (C1).

**C5. Transport in the coupling: (BETA) in thermal form. KNOWN ((NOCRIT), (VIR-log) of 2026-11-11; Proposition TR of row 895, check 896).**
- Crux lemma (THERM-DI). For the free-wall thermal sum X(beta, a) = log(1 + S_fw(a; b^3)) at fixed lattice shape ratio: d X/d beta at most -C a dX/da on [0.3609, beta_1], with one C. Equivalent (ARGUED): the thermal excess of the action is at most C times the thermal energy, level by level or in the mean.
- Buys. A fixed-bare-coupling seed at beta_1 from the proved seed at 0.3609 (TR1, check 896 HOLDS AFTER CORRECTION).
- Why easier. The thermal form needs the inequality only in the mean over the thermal state, not for every level (check 896 L390-392: "weaker than a bound on every branch").
- Tests. F1: fails for U(1) at the transition (a level reaches zero). F2: not needed for glue. F3: none. F4: no; uniformity of C is the absence of a critical point on the Wilson axis, and the endpoint K7 lies near it (GUIDE). Not first-passage.
- Chance. P1 10 percent (any explicit C on any interval past 0.3609), P2 1 percent.

**C6. One covariant particle: the Witten Laplacian on one-forms with a Furstenberg-Kato bound. VARIANT of row 859 ideas 19, 20, 48 and row 876 G2, G12 (top five there, never attempted).**
- Crux lemma (MN). Let R(U) = Ric + beta Hess S(U) on the tangent space of SU(2)^E. Its link-diagonal blocks are scalar and positive in the mean (READ row 859 idea 48: "the mean Hessian is diagonal"). Its off-diagonal blocks are adjoint transports times bounded scalars. Claim: the bottom of -L + R on exact one-forms is at least kappa above 0 whenever [sup norm of the centred off-diagonal part]^2 times [its correlation time under the Langevin flow] is below the mean diagonal part.
- Buys. A volume-uniform Langevin gap, hence the glue half, with no flux input.
- Why easier. It is the one mechanism in the inventory with a zeroth-order difference between SU(2) and U(1) (Ricci curvature 0 for U(1)) and with averaging in place of a supremum.
- Tests. F1: fails for U(1) (no Ricci term, no adjoint charge; the form is the massless Gaussian one). F2: not needed. F3: passes only if the Kato-type bound is in the mean; a pointwise bound is the worst case and stops at the Langevin range (row 837: a factor 9.5 below the band). F4: GUIDE of row 876: "no margin at 2.3"; so even a proved (MN) may not reach the band.
- Chance. P1 10 percent, P2 below 1 percent.

**C7. Exact block steps to a proved zone, with a locality statement in the mean. KNOWN (EXIT, rows 846, 861).**
- Crux lemma: PIN-MIX with the supremum over pinnings replaced by a mean. Stops where W4 stops (no supplier). GUIDE arithmetic (mine, recalled string tensions, decides nothing): two doublings multiply sigma a^2 by 16, from 0.136 at beta 2.3 to about 2.2, the value at strong coupling near beta 0.4. So the distance is two steps, not many. Chance. P1 5 percent, P2 1 percent.

**C8. An exact scale identity for the thermal sum. VARIANT of row 859 idea 29.**
- Crux lemma (SUM-RULE). The a-derivative of X(beta, a) at fixed physical box equals a fixed combination of plaquette expectations of the thermal state (lattice sum rules of Michael type, recalled, not read). With C5 this turns the transport inequality into a statement about the sign and size of one plaquette difference. Reduction only. Chance. P1 30 percent, P2 below 1 percent.

### 4.3 Batch 3: flux-half candidates still alive, other geometries, and rejections

**C9. (CORE) as a lower bound on the deconfinement temperature. KNOWN (row 876 G6 with Lemma RPF; row 892).** Crux: h(a/2) at most h(a/4)/sqrt 2 for the plateau function of two winding lines, given (HC). F1: U(1) fails at glue. F2: yes (frozen groups have ordered winding lines). F3: yes. F4: one order-one number, no tool. Not needed if C1 lands. P1 10, P2 1.

**C10. EXC and (DRESS). KNOWN, live (checks 881, 890).** Crux: integral of Delta(s) ds/s at least c_0 with c_0 at least the consumer rate; sharpest open form: an order-L_i bound on the relative magnetic response. F1-F3 pass as a target. F4: no tool; thin margin (gamma about 0.010 at 2.3). Not needed if C1 lands. P1 5, P2 below 1.

**C11. The decoder (SEED-DEC-H) with a chessboard estimate. KNOWN (row 887, check 891).** Crux: z_0 below 1/1,120,616 with a uniform margin, and (CE) for the one-slice law. F4: asks a number of size 1e-6 at a block of a few correlation lengths. Not needed if C1 lands. P1 5, P2 below 1.

**C12. Twins with free walls: 3D SU(2), or the 2D SU(2) principal chiral model. KNOWN as test beds (row 859 ideas 22, 34; row 876 G7); NEW only in combination with C1.** Crux: (FW-SEED) in the twin. In 3D the U(1) test does not bind (compact U(1) confines there; Gopfert-Mack, recalled) and the ultraviolet side is super-renormalizable. Same order-one crux; a cheaper place to learn whether any glue mechanism works. Off the 4D target. P1 10, P2 0 for 4D.

**C13. The twisted thin torus for all M, then growth in n. KNOWN (rows 842, 862; (MON')).** Crux: a dilute gas of flux -1 defects for M above M_1; then a one-way step in n. Off the order-one crux; the growth step is the crux again. P1 25 (all M), P2 below 1.

**C14. A Migdal-Kadanoff sandwich in the style of Tomboulis. REJECTED.** READ FINISH (literature row quoted in my grep of Step 3): Tomboulis arXiv:0707.2179 with Ito and Seiler arXiv:0711.4930, "the claim rests on an unproved inequality". The sandwich bounds log Z with an extensive error and treats U(1) and SU(2) alike (row 876 idea 16: the toy "confines U(1) wrongly"). Fails F1.

**C15. Flux from a strong mass gap (Chatterjee's mechanism). REJECTED as an attack.** Its hypothesis is decay uniform in boundary conditions (READ FINISH literature row: "the exact hypothesis (strong mass gap)"). That is a boundary-uniform statement on blocks larger than the correlation length, which row 836 names as OPEN; and C1 removes the need for the flux half.

**C16. Free-wall comparison principle. NEW as a question; no proof idea yet.** Crux question: is the free-wall thermal sum of a box monotone under enlarging the box, or under raising a coupling (a Griffiths-type property)? If free walls were extremal, (FW-SEED) on one box would bound mixed boundary conditions too. Row 876 idea 29 records that GKS fails on non-orientable surfaces (Corollary NS0), so the general inequality is false; a restricted one is OPEN. P1 10, P2 0.

### 4.4 Summary table

| # | Candidate | Half | Label | F1 | F2 | F3 | F4 | P1 | P2 |
|---|---|---|---|---|---|---|---|---|---|
| C1 | free-wall engine (W'-ENG) | removes flux | VARIANT/NEW | seed fails | not needed | Y | reduces to glue | 45 | 2 |
| C2 | (UNIV-FP) port | either | KNOWN | - | - | - | no | 90 (answer) | 0 |
| C3 | centre-disordering weight + (MULTIPLET) | flux | KNOWN | Y | Y | Y | flux only | 30 | 1 |
| C4 | monopole-free weight + Griffiths | flux | VARIANT | Y | N | Y | N | 20 | <1 |
| C5 | thermal transport (THERM-DI) | glue | KNOWN | Y | - | Y | N | 10 | 1 |
| C6 | Witten Laplacian, Furstenberg-Kato (MN) | glue | VARIANT | Y | - | mean only | N | 10 | <1 |
| C7 | exact block steps, locality in the mean | both | KNOWN | Y | Y | mean only | N | 5 | 1 |
| C8 | scale identity (SUM-RULE) | glue | VARIANT | - | - | Y | N | 30 | <1 |
| C9 | (CORE) via RPF, (HC) | flux | KNOWN | Y | Y | Y | N | 10 | 1 |
| C10 | EXC, (DRESS) | flux | KNOWN | Y | Y | Y | N | 5 | <1 |
| C11 | decoder with (CE) | flux | KNOWN | Y | Y | Y | N | 5 | <1 |
| C12 | twins with free walls | glue | KNOWN+C1 | n/a in 3D | - | Y | N | 10 | 0 |
| C13 | twisted thin torus, all M | off crux | KNOWN | Y | Y | Y | N | 25 | <1 |
| C14 | Migdal-Kadanoff sandwich | both | rejected | N | | | | | |
| C15 | strong mass gap to area law | flux | rejected | | | N | | | |
| C16 | free-wall comparison principle | glue | NEW question | ? | - | Y | N | 10 | 0 |

Honest reading of the table. No candidate has P2 above 2 percent. The differences are in P1 and in what a landed first lemma changes. C1 is the only one whose first lemma changes the crux itself.

Step 4 done. Next: Step 5, choose three.

## Step 6 (done before Step 5, because its outcome changes the choice). First step of C1: can the seed engine run on free walls?

### 6.0 What Theorem S uses (READ gap-crux-restate.md L176-205)

Setting there: W(a, b) symmetric, W(a, b) = Tr T_b^a with T_b positive trace class. Steps: (K) e(jb) at most j e(b), from Tr T^(jb) at most (Tr T^b)^j; so the deficit kappa(b) = e(b) - ell b is at least 0, convex, non-increasing. (X) a kappa(b) + g(a, b) = b kappa(a) + g(b, a); so (b - a) kappa(b) at most g(a, b). (E) 1 + S(a; 2b) at most (1 + S(a; b))^(2b/(b-a)). Then three uses of (E) and "S(2n; B) at most S(n; B)^2, because every eigenvalue has multiplicity at least one". Trace-only inputs: the sub-multiplicativity in (K) and (E), and the squaring. Both rest on integer multiplicities.

### 6.1 Setup and four elementary facts (PROVED here unless marked)

Box Lambda = product of {1..n_mu}; a direction is P (periodic) or F (free walls: no link leaves the box). Weight: product over plaquettes of exp(beta x_p), x_p = (1/2) tr U_p, Haar probability on links. In direction 1 with cross-section B: B_0(U) = product of the slice's plaquette weights; K = (projection on gauge-invariant functions) composed with (link-wise convolution by the weight); M = B_0^(1/2) K B_0^(1/2); u = B_0^(1/2) 1. K is positive because the Wilson weight has positive character coefficients and the convolution commutes with gauge transformations (this is the lane's (TM); READ gap-crux-core-check-astra.md section 8 for the same factorization; its extension to a free-wall cross-section is ARGUED: the construction is link-local). Then: periodic time gives Z = Tr M^(n_1); free time gives Z = <u, M^(n_1 - 1) u>.

**FW1 (no flux sectors behind free walls).** If direction i of the cross-section is F, the flip C of all i-links crossing a plane {x_i = c | c+1} equals the gauge transformation Omega(x) = -1 for x_i above c, +1 otherwise. Proof: Omega(x) U Omega(y)^(-1) = -U exactly on the links that cross the plane, because no link closes around direction i. The range of M lies in the gauge-invariant functions. So C acts as the identity on the range of M. QED. With three F space directions there is no centre sector and no twist. (If direction i is P, only products of two flips are gauge transformations, and the sectors return.)

**FW2 (free walls are super-multiplicative).** For an F direction mu: Z(n_mu = b_1 + b_2) at least Z(b_1) Z(b_2), the other sides and patterns fixed. Proof: cut between the sites b_1 and b_1 + 1. Under the product of the two box measures, with the crossing links Haar distributed, Z(b_1 + b_2) = Z(b_1) Z(b_2) E[exp(beta sum over crossing plaquettes of x_p)]. Jensen. Every crossing plaquette contains a crossing link U that is uniform and independent of the rest, so E[x_p] = 0. QED. Consequence: for the top eigenvalue of the time transfer, e(b) := log lambda_0 with free side b, e(b_1 + b_2) at least e(b_1) + e(b_2) (take (1/a) log and a to infinity). This is the opposite sign to Lemma K (b).

**FW3 (the wall cost is finite and the deficit is monotone).** b -> log Z(a; b) is convex in an F direction (Z = <v, R^(b-1) v> is a positive combination of exponentials of b), so e is convex in b. Put f = sup e(b)/b = lim e(b)/b and D(b) = f b - e(b), at least 0. D is concave and bounded below, so D is non-decreasing. D is bounded above: the crossing factor in FW2 is at most exp(beta N a), N the number of crossing plaquettes per time step, so e(b_1 + b_2) at most e(b_1) + e(b_2) + beta N and f b at most e(b) + beta N. Put D_inf = sup D (the cost of two free walls per unit time) and delta_e(b) = D_inf - D(b). Then delta_e is at least 0, non-increasing, tends to 0, and e(b) = f b - D_inf + delta_e(b). QED.

**FW4 (the trace seed gives the gap of its own box).** For the trace form, S(a; B) is at least (lambda_1/lambda_0)^a, so m(B) is at least log(1/S(a; B))/a. The engine's content is only the passage to larger boxes.

### 6.2 The vector engine (W-ENG) cannot be proved from positivity and axis exchange (PROVED: a counterexample in the class)

Class: functions Z(n_1, ..., n_4), symmetric, with Z(0, .) = 1 and, in each variable, Z = sum over k of w_k lambda_k^(n) with w_k at least 0 and sum w_k = 1 (the spectral form of a unit vector under a positive operator), and super-multiplicative in each variable (FW2). This is every property of the all-free family that 6.1 has.

Example. Fix f real, m above 0, z^2 above 0. With V = n_1 n_2 n_3 n_4 and V_mu = V/n_mu put

  log Z(n) = f V + z^2 sum over mu of V_mu (e^(-m n_mu) - 1).

Check. Symmetric. In the variable t = n_1 with (b, c, d) fixed: log Z = t [f bcd + z^2 (cd(e^(-mb) - 1) + bd(e^(-mc) - 1) + bc(e^(-md) - 1))] + N (e^(-mt) - 1), N = z^2 bcd. So Z(t) = sum over k at least 0 of [e^(-N) N^k/k!] (lambda_0 e^(-mk))^t: Poisson weights, eigenvalues lambda_0 e^(-mk). Z(0) = 1. Super-multiplicative: the difference of the two sides is N (1 - e^(-mt))(1 - e^(-mt')), at least 0.
Its vector thermal sum is S_W(t; (b, c, d)) = exp(z^2 bcd e^(-mt)) - 1. Its gap on the cyclic subspace is m for every box.
Now fix any s_W in (0, 1) and any C. Take N_0 at least 3, s below s_W with C s below 1, z^2 = s/(16 N_0^3), and m = mu/N_0 with 0 below mu below log(1/(C s)). Then S_W(N_0; (2N_0)^3) = exp((s/2) e^(-mu)) - 1 is below s. The conclusion of (W-ENG) asks a gap at least log(1/(C S_W))/N_0, which is at least log(1/(C s))/N_0, above mu/N_0 = m. False. QED

Reading. The walls exchange one light particle with a small coupling z. A vector sum sees a state only through its overlap with the wall vector. No integrality protects it. So row 900's crux (W-ENG), as stated, needs an input beyond positivity and axis exchange: a lower bound on the wall overlap of every light state. This is the outcome row 900 named as a stop: "a trace-only step shown necessary by a counterexample". It does not say (W-ENG) is false for the Wilson model. A second defect stands even if it were true (ARGUED): a gap on the cyclic subspace of the wall vector is wall-to-wall decay; a local observable A applied to a state is not in that subspace in general, so decay of local correlations does not follow.


### Lead note received during Step 6 (2026-11-13), and rows 899, 901 as READ (clone at b130977d2; FINISH.md line 976; gap-wall-assume-max.md L289-354; gap-wall-assume-check-astra.md, final RESULT line)

- Row 899 (Fable, assumptions exercise on five walls). Six shared assumptions: (SA1) bare unit lattice at one order-one Wilson coupling, while the real object is first passage; (SA2) uniformity in a conditioning variable; (SA3) absolute values where the true quantity is a likelihood-ratio mean with cancellation; (SA4) the torus and its conserved centre charge, forced by the consumer; (SA5) one coupling; (SA6) group-blind proofs. Reduction (VAR-SLAB): for the half-torus slab twist ratio rho under the two-slice law, E[rho^2] = 1, Var(rho) = 4p(1-p), p/(1-2p) = E_tw[sinh^2(X/2)], X = log rho; so 4p(1-p) is at most E|grad X|^2 divided by the gauge-invariant Langevin gap lambda. The flux half at one coupling follows from lambda and one L^2 force response (FR). Also: the flat-wall slab orders up to a thickness near the deconfinement length (GUIDE at beta 2.3).
- Row 901 (check, Codex astra): the VAR-SLAB identities, the Poincare step and the conditional FR reduction HOLD. SA6's "every compact group with a centre" statement FAILS. SA4 HOLDS for the named torus consumer. (FR) and lambda at order one stay OPEN.
- Use in this note. (VAR-SLAB) is a checked edge "glue in Langevin form plus (FR) gives the flux half". Together with SA4 it says the same thing as my ordering remark in Step 4: the flux half is tied to the torus consumer, and the open content sits in the glue half plus one response statement. I add it as candidate C17 in Step 5.

### 6.3 The trace engine (W'-ENG): what ports, the exact enlargement inequality, and where it stops

Family: W(a, b) = Z(P: a; F: b, F: c, F: d), time periodic, space free, c and d fixed. It is NOT symmetric in (a, b): the exchange turns the trace into a vector element. Two expansions of the same number (PROVED, notation of 6.1):

- time channel: W(a, b) = Tr M_b^a = lambda_0(b)^a (1 + S(a; b)); g(a, b) = log(1 + S) at least 0; e(b) = f b - D_inf + delta_e(b) (FW3);
- space channel: W(a, b) = <v_a, R_a^(b-1) v_a> = w_0(a) r_0(a)^(b-1) (1 + S_W(b; a)); gamma(b, a) = log(1 + S_W) at least 0, non-increasing in b; eps(a) = log r_0(a), omega(a) = log w_0(a). (w_0 above 0: ARGUED from strict positivity of the kernel.)

**Lemma FW5 (crossing with walls; PROVED).** (i) p(a) := lim over b of g(a, b)/b exists, p(a) = eps(a) - a f, and p(a) is at least 0. (ii) With c(a) := omega(a) - a (f - D_inf):
  g(a, b) = (b - 1) p(a) + c(a) + gamma(b, a) - a delta_e(b).
Proof. Equate the two expansions: a e(b) + g(a, b) = (b - 1) eps(a) + omega(a) + gamma(b, a). Divide by b and let b grow: e(b)/b tends to f, gamma is bounded. This gives (i). Insert e(b) = f b - D_inf + delta_e(b) and eps(a) = a f + p(a). QED
Reading: p(a) is the bulk thermal density per unit length; c(a) is the thermal wall term; a delta_e(b) is the zero-temperature wall-to-wall term at separation b; gamma is the vector sum of the crossed channel. The extensive wall cost D_inf cancels exactly.

**Lemma FW6 (enlarging a free side at fixed time; PROVED).** For h at least 1:
  g(a, b + h) at most g(a, b) + h p(a) + a [delta_e(b) - delta_e(b + h)], at most g(a, b) + h p(a) + a delta_e(b).
Proof. Each eigenvalue of R_a is at most r_0(a), so W(a, b + h) at most r_0(a)^h W(a, b). Take logarithms, use both expansions in the time channel and e(b + h) - e(b) = f h + delta_e(b + h) - delta_e(b). QED

**What ports.** The squaring S(2a; B) at most S(a; B)^2 holds (trace, multiplicities at least one). FW4 gives the gap of the seed box itself. FW6 replaces Lemma E.

**Where it stops.** Lemma E closed because Lemma X bounded the deficit by the thermal sum of the same family: (b - a) kappa(b) at most g(a, b). Here the same closure needs two bounds that I could not prove from the class:
  (WALL-1) b p(a) at most C_1 g(a, b). By FW5 (ii) this is a lower bound on the thermal wall term: c(a) at least -(C_1 - 1) g(a, b) + (lower-order terms).
  (WALL-2) a delta_e(b) at most C_2 g(a, b) for a at most b/2: the zero-temperature wall-to-wall term at the larger separation is dominated by the thermal sum at the shorter time.
Given (WALL-1) and (WALL-2) with absolute constants, FW6 with h = b gives g(a, 2b) at most (1 + C_1 + C_2) g(a, b), three uses give the cube, the squaring gives the step, and the recursion of Theorem S runs with 5041 replaced by a constant depending on C_1, C_2 (ARGUED; constants not written).
Why they do not follow (PROVED limits, then ARGUED). delta_e belongs to the time-channel operators M_b, which the all-free family also uses; there it equals the density of a VECTOR thermal sum between the two walls (from the symmetric identity of the all-free family, by the same division; ARGUED, written in my scratch reasoning, not here). Vector sums see states through wall overlaps. 6.2 shows that wall overlaps are not controlled by positivity and axis exchange. (WALL-2) says in physical words: the walls do not couple to the light states exponentially more strongly than the heat bath does. (WALL-1) says: free walls do not remove more thermal weight than a fixed fraction of the bulk. Both are true for a free massive field (ARGUED) and both are locality statements about walls.
I found no counterexample to (W'-ENG) in the class. A candidate (a wall that raises the mass in small boxes) violates positivity in the crossed channel: exp(-a kappa e^(-mu b)) has alternating coefficients in e^(-k mu b) (PROVED, one line). So (W'-ENG) is OPEN, neither proved nor refuted.

**A corollary that does hold (PROVED from the READ statement of Corollary S2).** Take two periodic directions (time and one space direction) and keep the two free sides (c, d) fixed. Then W(a, b) = Z(P: a, P: b; F: c, F: d) is symmetric and is a trace in both variables. Corollary S2 of gap-crux-restate.md applies verbatim: S(2n; 4n) at most ((1 + S(n; 2n))^4 - 1)^2, and a seed at most 1/20 gives a gap on the tubes (2^k n)^2 x (c, d). The thermal sum of such a seed grows with c d, so this is a statement about a tube of fixed cross-section, not a four-dimensional engine. It does show that one winding direction (hence one electric flux sector and one twist plane, no magnetic twist) can be carried without any free-direction lemma.

**Outcome of the first step.** PROVED: FW1 to FW6 and the counterexample of 6.2. OPEN: (WALL-1), (WALL-2), hence (W'-ENG). The route stops at two wall-locality inequalities in the class. If they hold for the Wilson model, the whole seed is one glue number on a free-wall box, with no flux half, no twist and no finite-group test.

## Step 5. The choice

### 5.0 One more candidate, from rows 899 and 901

**C17. The L^2 pair of row 899: (FR) with the Langevin gap. KNOWN since today (row 899, check 901 HOLDS).** Crux: (FR), E_w[|Delta G_b|^2] at most eps^2 for the boundary force under a far centre flip; then p(1 - p) at most (3|B|/(2 lambda)) eps^2. F1: fails for U(1) in both factors. F2: fails for ordered Z_2, frozen Q_8, 2T (Var is near 1). F3: an L^2 statement under the true law, no supremum. F4: no tool; row 899 says its natural proof returns the flux energy. It needs the glue half first (lambda). P1 5, P2 1.

### 5.1 What decides the choice

1. The number has no supplier in any form (Step 4 table; rows 878, 895, 899 say the same). A fourth, fifth and sixth proof lane on the number in a new form is the pattern that row 878 named saturation. So I do not spend all three attacks on the number.
2. Every form of the number in use carries avoidable load: the flux half and the twists come from the torus consumer (SA4 of row 899; FW1 here); the finite-group tests come with the flux half; the supremum comes from the criteria (SA2); the bare coupling comes from working off the account (SA1).
3. Since (VAR-SLAB) (checked, row 901) and Proposition K (checked, row 893), every flux route needs the glue half first. The glue half is on every path and has had one proof lane.
4. One route in the whole list has a KNOWN TOOL for an order-one input that is uniform in the cutoff: the centre-disordering weight (C3), where the electric flux is heavy by a Z_2 expansion at fixed beta_F. It needs the account's permission to choose the weight (C2).

So the three attacks are: remove the flux half from the consumer (C1); obtain the flux half from a known tool by choice of the weight (C2 then C3); and one glue-first attack on the number (C5 in two transports). They use three disjoint inputs: the class (positivity and axis exchange), the account, and the SU(2) measure at order one. C1 and C2-C3 are two independent ways to the same end (a crux that is glue only); either suffices.

Why these beat the others. C9, C10, C11 and C17 attack the flux half in the confined pattern at order one: each is conditional on glue, each has the finite-group tests against it, and C1 or C3 would make each unnecessary. C6 has no margin at 2.3 by row 876's own guide. C7 stops at W4/W12. C12 and C13 are off the 4D order-one crux. C14 and C15 fail a fact test. C4 fails F2. C16 has no proof idea. C8 is folded into attack 3.

### 5.2 Attack 1 (top): the free-wall seed engine

- What. Replace the torus consumer by boxes with free walls in space and periodic time. Then the seed is one glue number and the flux half, the twists and the finite-group tests leave the path (FW1).
- Exact crux lemma. In the family W(a, b) = Z(P: a; F: b, F: c, F: d) with the notation of FW3 and FW5, for all shapes with 3 at most a at most b/2 and the other two free sides at least b:
  (WALL-1) b p(a) at most C_1 g(a, b);  (WALL-2) a delta_e(b) at most C_2 g(a, b);
  with absolute C_1, C_2. Conditional theorem (ARGUED from FW6; constants to be written): then 1 + S(a; (2b)^3) at most (1 + S(a; b^3))^(k^3) with k = 1 + C_1 + C_2, and S(2a; (2b)^3) at most ((1 + S(a; b^3))^(k^3) - 1)^2. So a seed S_fw(a; b^3) below an explicit s'(C_1, C_2) gives a gap on every dyadic free-wall cube, as in Theorem S.
- Why it beats the others. It is the only candidate whose first lemma changes the crux itself. It needs nothing at order one. It also removes the object the account cannot read (twisted tori, row 837 2.4 item 4).
- First concrete step (after Step 6). Decide (WALL-2) and (WALL-1) by hand in the lattice free massive scalar field with free walls in space, where every term of FW5 is a Gaussian determinant. If either fails there with constants that grow with the box, drop the engine. If both hold, the proof must use a property the class lacks and the Wilson model has: finite range in the free direction. Look for it as a bound on the wall overlap: the weight ratio w_k/w_0 of FW5's vector form against the trace multiplicity.
- Second node, to write only after the engine: the gap of free-wall boxes gives the gap of the limit state on local observables (a port of the limit step, rows 700 and 703, from tori to boxes), and the free-wall limit state must be identified with the account's state. Both are OPEN and not started.
- Model and effort. Claude Fable 5.2 max as author (a new engine is hard, stuck direction). The Gaussian test is routine: Claude Opus 5.5. Check: Codex gpt-6-astra xhigh, line by line, first on 6.2 and FW5, FW6 of this note.
- Stop condition. Stop with success when (WALL-1) and (WALL-2) are proved with explicit constants for the Wilson weight. Stop and drop when the free scalar violates either, or when a counterexample to (W'-ENG) in the class is written. Park after one max lane that reaches neither.
- Honest chance. 20 percent that an engine theorem lands (lowered from 45 after Step 6). It supplies no number.

GUIDE for attack 1 (my hand estimate in the continuum free massive scalar; it decides nothing). With Neumann walls, Euler-Maclaurin gives g(a, b) = b p(a) + (1/2) g_2(a) + (exponentially small), g_2 the thermal sum of the wall modes, at least 0. So (WALL-1) holds with C_1 = 1; with Dirichlet walls the sign flips and C_1 is 1 + O(a/b). The zero-temperature wall term is the Casimir energy: a delta_e(b) is about a c d e^(-2mb) (m/b)^(3/2) for m b large, and (pi^2/1440) a c d/b^3 at m = 0, against g(a, b) of about b c d (m/(2 pi a))^(3/2) e^(-ma), or (pi^2/90) b c d/a^3 at m = 0. The ratio is at most about (1/16)(a/b)^4 at m = 0 and exponentially small for m a large. So (WALL-2) holds there with a small C_2. Both inequalities look true for a local free field. What an interacting proof must overcome (ARGUED): the wall vector has an overlap with the vacuum that is exponentially small in the wall volume, so the crude comparison of a vector sum with a trace loses an extensive factor.

### 5.3 Attack 2: the flux half from a known tool, by choice of the bare weight

- What. Use a weight exp(beta_F x_p + (centre-blind part)) with beta_F small and fixed, and let only the centre-blind coupling run to the continuum. Then thin centre vortices are cheap at every cutoff and the flux half is a convergent Z_2 expansion.
- Exact crux statements, in order.
  (UNIV-FP) (a question to the account; READ only through row 900, the file YM4_1400.tex is not among the sources on disk at /Users/jonreilly/ym4d-lead/sa): the account's fixed-horizon universality holds at the first-passage horizon with constants uniform in K, covers a weight of this mixed type, and bounds the difference of the seed numbers of two weights below half the margin.
  (FLUX-Z2) For beta_F with C tanh(beta_F) below 1 (C the surface-counting constant of the four-dimensional lattice), every torus, every centre-blind part and every twist v: Z^v/Z^0 is at least 1 - (C tanh beta_F)^(A_v), A_v the least area of a closed surface of odd class against v.
  Argument for (FLUX-Z2) (ARGUED here; it is the comparison of Mack and Petkova 1979 and Frohlich 1979 as recalled in row 876 idea 31, not read by me; to be rebuilt in the repo before any use). Write U = z U~, z in Z_2. Then x_p(U) = (dz)_p x~_p, so given U~ the centre is a Z_2 gauge theory with couplings K_p = beta_F x~_p, and |K_p| is at most beta_F for EVERY U~ (row 876 idea 2 proves the splitting). Its expansion in tanh K_p is a sum over closed surfaces; the twist changes the sign of the odd-class surfaces only; so the Z_2 ratio is at least 1 - (C tanh beta_F)^(A_v) for every U~. Both Z_2 partition functions are positive, so the bound survives the average over U~. On the torus (a, b, b, b) this gives Q_0 at most (1/2)(C tanh beta_F)^(ab): (CORE), uniformly in the volume and in the centre-blind coupling.
  (MULTIPLET) Theorems S and R for a transfer operator whose top of spectrum is a multiplet of eight states with splittings and mixings bounded by e^(-c x area) (row 876 G11: with cheap thin vortices the SO(3) bundle classes of a slice are nearly degenerate vacua of the periodic box, so (ES) fails as stated).
- Fact tests. F1: no such centre quotient acts in U(1) Coulomb. F2: the supremum over U~ is taken below its ceiling by the choice of beta_F, which is the point; Q_8 and 2T would pass (FLUX-Z2) too, and correctly so (their fundamental loops are disordered by the same thin vortices). F3: a uniform bound, but in its convergent range by construction. F4: a known tool reaches the flux half; the glue half stays.
- Why it beats the other flux routes. It is the only route where an order-one input is supplied uniformly in the cutoff by a convergent expansion. C9, C10, C11, C17 ask the same half of the Wilson measure at order one with no tool.
- First concrete step. Port the universality subsection of the account with line references, at the commit the lane cites for the outline (row 837 names 2bc0658f91d2): its hypotheses on the bare weight, whether the horizon may be first passage, whether the constants depend on K. Decide yes or no.
- Model and effort. Claude Opus 5.5 high for the port. If yes: Claude Opus 5.5 max rebuilds (FLUX-Z2) with constants (routine expansion); Claude Fable 5.2 medium proves or refutes (MULTIPLET); Codex gpt-6-astra xhigh checks each.
- Stop condition. Stop the whole attack if the port says no (fixed horizon only, K-dependent constants, or a weight class that excludes the mixed weight). Stop (MULTIPLET) at a proof or a counterexample in the class.
- Note. If attack 1 lands, (MULTIPLET) is not needed (free-wall boxes carry no bundle classes), but (UNIV-FP) is still worth its port: it decides SA1-type questions for every later lane.
- Honest chance. A usable yes from the port: 25 percent. The whole chain: under 10 percent. It supplies the flux half only.

### 5.4 Attack 3: the glue number first, by transport from a proved region, in the mean

- What. The glue half is on every path (5.1 item 3) and has no tool. Attack it once, before any further flux lane, in the one family of statements that has exact identities and proved starting regions.
- Exact crux lemma (GLUE-1). At one beta in [2.3, 2.6] there are a and b at least 24a with S_ev(a; b^3) at most 1/10 (periodic even form; with (CORE) it is the SH seed, Corollary O1 of row 892, checked). If attack 1 lands, the same with the free-wall sum S_fw and the engine's threshold. Transport form (THERM-DI): with X = log(1 + S_ev) at a fixed box shape, dX/d(parameter) is at most -C a dX/da along a path that starts in a proved region, with C independent of the box. In words: along the path, the thermal mean of the loss of level energies is at most C times the thermal mean energy.
- The two paths (both READ). The coupling path: Proposition TR and Corollary TR1 (row 895; check 896: TR HOLDS, TR1 HOLDS AFTER CORRECTION; start beta at most 0.3609). The pin path at fixed beta: Theorem HL of row 861 (check 877 HOLDS); proved region {beta below 2/9, all a} union {a above 24 beta, all beta} (READ gap-exit-max.md L513); the strip 0 below a at most 24 beta is open. The pin path starts at the target coupling; the coupling path must cross the bare crossover near 2.2.
- Why the mean form. Check 896 (L390-392): the thermal inequality follows from the level-wise one and is weaker; its converse is not proved. The level-wise form needs an all-level estimate (check 896 D5 gives an analytic family without one). The mean form asks one inequality between two expectations of the thermal state. This breaks SA2 and SA3 of row 899 for the glue half.
- Fact tests. F1: must fail for U(1) where a level closes (the Coulomb transition on the coupling path; the Higgs transition on the pin path). F2: not needed for the glue half (frozen finite groups are gapped). F3: no supremum if the pin configuration is kept at V = 1 (Theorem HL's path) and the inequality is in the mean. F4: at one bare coupling only (SA1 stands). GUIDE, recalled and not verified by me: the SU(2) model with a fundamental pin has a first-order line at large beta that ends near beta 2.7; if so the pin path is transition-free only below that value and cannot serve along first passage.
- First concrete step (a decision probe, not a proof lane). (1) Write dX/d(beta) and dX/d(a_pin) as differences of plaquette or pin expectations between the thermal torus and the long torus (the sum rule; C8). (2) Evaluate the mean inequality by hand in three exact settings: SU(2) at leading strong coupling, Z_2 gauge theory at large beta, the two-dimensional heat-kernel model; and show where it fails in Villain U(1). (3) Decide whether a box-uniform C can exist on the band; if yes, state the inequality as the crux lemma with its constant.
- Model and effort. Codex gpt-6-astra max for the probe. Check by Claude Opus 5.5 high. Promote to Claude Fable 5.2 max only if a box-uniform inequality survives step (2).
- Stop condition. Close the transport family if no box-uniform mean inequality survives the exact settings. In a proof lane, stop at the first step that needs a supremum over environments or over levels.
- Honest chance. A clean decision: 60 percent. A surviving inequality worth a proof lane: 10 percent. A seed at order one: 1 percent.

### 5.5 Held, with the order in which I would release them

1. (FR) with (VAR-SLAB) (C17): the best flux statement on the torus, if attacks 1 and 2 both fail. It needs the glue half first.
2. EXC (C10) and the decoder (C11): keep closed while 1 is open.
3. The twisted thin torus for all M (C13): a real theorem with a small parameter, off the order-one crux; release only by an owner decision on priorities.
4. No further fresh-framing exercise (the lead's decision in row 878 stands; this note found nothing against it).

## Step 7. Self-check and corrections

Corrections to earlier text of this note.
1. Table 4.4, row C1: P1 = 45 was written before Step 6. After Step 6 it is 20 (the vector form fails in the class; the trace form needs (WALL-1) and (WALL-2)).
2. C1 as first written offered row 900's vector form (W) and my trace form (W') side by side. After 6.2 only (W') is proposed. Row 900's (W-ENG) should not get a lane as stated.
3. (FLUX-Z2) in 5.3: the bound "1 - (C tanh beta_F)^(A_v)" hides an entropy factor. The honest form is by a cluster expansion of log(Z^v/Z^0): it is at least -2 N_v (C_0 t)^(A_v)/(1 - C_0 t), t = tanh beta_F, N_v the number of positions of an odd-class surface (at most b^2 on the torus (a, b, b, b)), C_0 the constant of connected surfaces. Since b^2 is at most e^(ab), the stated form holds with a larger C. The activities are signed (K_p has both signs); the expansion needs only their absolute bound t^|S|. Still ARGUED, not proved here.
4. FW3 and FW5 are stated for sides at least 3, as the lane's Lemma K (domain correction of rows 698, 699).
5. 6.2 uses the normalization Z(0, .) = 1 of row 900's convention (Z = <1, L^n 1>). In the convention of 6.1 (u = B_0^(1/2) 1) the total weight is the one-slice partition function instead of 1; the example adapts by one factor and the conclusion does not change (ARGUED).

Checks of my own PROVED items (re-read line by line; this is a re-read by the author, not an independent check).
- FW1: M = B_0^(1/2) P_G C_w B_0^(1/2); P_G C_w = K by the substitution U' -> gauge transform of U'; the range is gauge invariant; the plane flip is the gauge transformation by -1 beyond the plane. Holds.
- FW2: the crossing links occur only in crossing plaquettes; under the product measure each crossing plaquette has mean 0; Jensen. Holds for the Wilson weight exp(beta x). For a general weight it needs E[log w] = 0 on crossing plaquettes, which is false in general; then the statement gets a constant per crossing plaquette (not written).
- FW3: concave and bounded below gives non-decreasing; the upper bound uses |x_p| at most 1. Holds.
- 6.2: the difference of the two sides of super-multiplicativity is N (1 - e^(-mt))(1 - e^(-mt')); the seed number is exp((s/2) e^(-mu)) - 1, below s; the gap is mu/N_0. Holds.
- FW5, FW6: algebra re-done; D_inf cancels. Hold, given w_0 above 0 (ARGUED).

Fact tests of the three chosen attacks, once more.
- Attack 1 is an implication in the class; it holds for every group if it holds at all. Its seed fails for U(1) Coulomb (scale-free thermal sum of the box; row 900's estimate and the Stefan-Boltzmann values are GUIDE). It uses no worst-case bound. It reduces the crux; it does not reach order one.
- Attack 2: F1 passes; F2 is satisfied in the allowed way (the route does not need SU(2) to differ from Q_8 or 2T, because it does not go through the Wilson measure's own confinement); F3: the uniform bound is used strictly inside its convergent range; F4: reaches the flux half by a known expansion, conditional on (UNIV-FP).
- Attack 3: F1 must be exhibited by the probe (Villain U(1)); F3 passes in the mean form; F4 only at one bare coupling.

Disposition of the lead's inputs.
- Row 896 (glue check): used; row 895's no-go claims are not used (2d of Step 2).
- Row 900 item 1 (route W): taken as attack 1 in trace form; its vector form refuted in the class (6.2). Item 2 (UNIV-FP): taken as the first step of attack 2. Item 3 (SURF): not chosen; row 900 itself reads it as (E17) or stronger with a group-blind free end, and check 874 found the same for (C2).
- Rows 899 and 901 ((VAR-SLAB), (FR)): recorded as C17, held first in line (5.5). SA4 supports attack 1; SA1 supports attack 2; SA2 and SA3 shape attack 3.

Limits of this note. Nothing at order one is proved. No mass gap. The chances are judgments. I did not open the Sussman-Alpoge sources (the cited outline file is not on disk at the given path); every statement about the account is READ from lane files (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). Balaban's estimates are not used. Literature items (Mack-Petkova, Frohlich, Tomboulis, Ito-Seiler, Chatterjee, Gopfert-Mack, the SU(2)-Higgs phase diagram, Casimir and Stefan-Boltzmann values) are recalled or READ through lane rows, not read at source. No numeric run was made. Row 894 was unchecked when read (check 897 had no RESULT). My reading of rows 830-897 is from FINISH.md RESULT texts and the named files, not from every library file.

## Step 8. Final

### 8.1 The three attacks

| # | Attack | Exact crux lemma | First step | Model | Stop |
|---|---|---|---|---|---|
| 1 | Free-wall seed engine (C1, trace form) | (WALL-1) b p(a) at most C_1 g(a, b) and (WALL-2) a delta_e(b) at most C_2 g(a, b), absolute constants, in the family Z(P: a; F: b, c, d); then (W'-ENG) by FW6 and the squaring | Decide both in the lattice free massive scalar with free walls; then seek the wall-overlap bound for the Wilson weight | Claude Fable 5.2 max author; Claude Opus 5.5 for the Gaussian test; Codex astra xhigh check | Proof with constants; or a violation in the free scalar or a class counterexample; park after one max lane |
| 2 | Flux half by a known tool (C2 then C3) | (UNIV-FP) for a mixed weight at the first-passage horizon; (FLUX-Z2) Z^v/Z^0 at least 1 - (C tanh beta_F)^(A_v) for every centre-blind part; (MULTIPLET) Theorems S and R above a multiplet of eight | Port the account's universality subsection with lines; yes or no | Claude Opus 5.5 high port; then Opus 5.5 max and Fable 5.2 medium; astra xhigh checks | Stop all if the port says no; (MULTIPLET) at proof or counterexample |
| 3 | Glue number first, transport in the mean (C5 with C8) | (GLUE-1) S_ev(a; b^3) at most 1/10 at one beta in the band, via (THERM-DI): dX/d(parameter) at most -C a dX/da with box-uniform C, on the coupling path (from 0.3609) or the pin path at fixed beta (from a above 24 beta) | Sum rule for both paths; evaluate in three exact settings and in Villain U(1); decide whether a box-uniform C can exist | Codex astra max probe; Opus 5.5 high check; Fable 5.2 max only if an inequality survives | Close the family if none survives; in a proof lane stop at the first supremum over environments or levels |

Independence: attack 1 uses only positivity and axis exchange; attack 2 uses the account and a convergent Z_2 expansion; attack 3 uses the SU(2) measure at one order-one coupling. Attacks 1 and 2 aim at the same end (a crux that is glue only) by disjoint means. Attack 3 is the glue half itself.

### 8.2 What is proved here and what is open

PROVED in this note (by hand, elementary; re-read by the author; checked by no one):
1. FW1: a box with free walls in space has no centre sector and no twist (each plane flip is a gauge transformation).
2. FW2, FW3: free walls are super-multiplicative (Jensen, Wilson weight); the top eigenvalue's deficit against bulk plus wall is at least 0, non-increasing, with a finite wall cost. The sign is opposite to Lemma K.
3. 6.2: an explicit symmetric family with positive spectral forms and super-multiplicativity in every direction that satisfies the vector seed and has an arbitrarily small gap. So row 900's (W-ENG) cannot be proved from positivity and axis exchange.
4. FW5, FW6: the crossing identity with walls, g(a, b) = (b - 1) p(a) + c(a) + gamma(b, a) - a delta_e(b), and the enlargement inequality g(a, b + h) at most g(a, b) + h p(a) + a delta_e(b). The extensive wall cost cancels exactly.
5. The tube corollary: with two periodic directions and fixed free sides, Corollary S2 applies verbatim.

ARGUED here: the conditional engine from (WALL-1), (WALL-2); (FLUX-Z2) by the Z_2 splitting and a cluster expansion; the ordering remark (the flux half is a torus artifact for the target sector); the free-field plausibility of the wall inequalities (GUIDE).

OPEN: (WALL-1), (WALL-2), (W'-ENG) and its second node; (UNIV-FP); (MULTIPLET); (THERM-DI) and (GLUE-1); and, unchanged, every order-one number of the lane: (CORE), (FR), the Langevin gap, (GLUE-FP), (SEED-FP). No mass gap. Nothing at order one.

### 8.3 Where the top attack stopped

At two wall-locality inequalities. The trace engine ports through the squaring step and through an exact enlargement inequality (FW6) in which the extensive wall cost cancels. It does not close, because the two channels of the free-wall family are different functions and Lemma X's monotonicity argument has no analogue: the thermal wall term c(a) and the zero-temperature wall-to-wall term delta_e(b) are not bounded by the thermal sum from positivity and axis exchange. They look true in a free field. A proof needs a bound on how strongly a free wall couples to light states.

RESULT: Row 898 (Claude Fable 5.2 max, unchecked): the next three attacks are (1) the free-wall seed engine, crux (WALL-1) b p(a) at most C_1 g(a, b) and (WALL-2) a delta_e(b) at most C_2 g(a, b) in the family with periodic time and free space walls, which would make the whole seed one glue number with no flux half, no twist and no finite-group test (first step done: FW1-FW6 PROVED; row 900's vector form (W-ENG) refuted in the class by an explicit family; the trace form stops at the two wall inequalities, OPEN); (2) the flux half from a known tool by choice of the bare weight, crux (UNIV-FP) for a mixed weight at the first-passage horizon, then (FLUX-Z2) Z^v/Z^0 at least 1 - (C tanh beta_F)^(A_v) and (MULTIPLET); (3) the glue number first, crux (GLUE-1) S_ev(a; b^3) at most 1/10 at one coupling in the band through the mean transport inequality (THERM-DI) on the coupling path or the pin path, as a decision probe before any proof lane; held in order: (FR) with (VAR-SLAB), EXC, the decoder; no order-one statement is proved and no candidate has a known tool for the order-one number.
