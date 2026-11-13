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

