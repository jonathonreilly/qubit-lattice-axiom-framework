lead: anthropic/claude-opus-5-5 (max effort), FINISH row 838, run 2026-11-12 on the lead's MacBook
clone: /Users/jonreilly/ym4d-lead/clone at 676d510b879523452f4a08c5ba4071b0ef1353f6 ("docs(ym4d): add row 838, the assumptions exercise in depth")
skill: origin/main `docs/ai_methodology/skills/exercise/SKILL.md` (Step 2 method: every premise, hidden ones included, with "what if wrong", cheapest test, prior test)

# gap-assume-opus: the assumptions exercise in depth, across the whole mass-gap skeleton

**No mass gap is proved here.** Nothing in this file is checked by another model. It is research text and grants no status.

**Marks.** READ = I read the statement at the cited path and line. PROVED = proved by hand in this file, not checked by another model. ARGUED = a written argument with a named gap or a physical premise. GUIDE = numerics or recalled physics; no proof step rests on it. OPEN = no proof exists. A small GUIDE script (19 MB) is at `scratchpad/lane838/scripts/subgroups.py` with its output beside it; no verdict rests on it.

**Paths.** D = `.claude/science/physics-loops/ym4d-hard-route-20261030` in the clone. Short names, all under D/library unless said: SK = `gap-skeleton-final.md`; FP = `gap-crux-fp.md` (row 712; its Part 2 is the first assumptions exercise); FX = `gap-flux-exercise.md` (row 731); FE = `gap-form-exercise.md` (row 735); CX = `gap-crux-exercise-astra.md` (row 750); SX = `gap-shape-exercise-astra.md` (row 814); PS = `gap-phys-seed.md`; MB = `gap-skeleton-max-b.md`; FU = `gap-fusion-astra.md`; VO = `gap-vortex-astra.md`; EX = `gap-expose-astra.md`; EXT = `gap-ext-astra.md`; JO = `gap-joint-astra.md`; TR = `gap-tree-astra.md`; CF = `gap-cf-astra.md`; SL = `gap-seed-limit.md`; RS = `gap-crux-restate.md`; GOAL = D/GOAL.md; FIN = D/FINISH.md, where row n sits at line n + 76 (row 780 at L856, row 838 at L914).

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the account (outline YM4_1400 at 2bc0658f91d2; complete account at 31a47c543775). Balaban: the renormalization group method behind it. Earlier exercises: Claude Fable 5.2 max (FP), Claude Fable 5.2 high (FX, FE), Codex gpt-6-astra max (CX, SX). Proved lane results are credited to their rows as the files say. Hartung, Jakobs, Jansen, Ostmeyer and Urbach, arXiv:2201.09625 (Table IV, read in a text extraction of the PDF, own scratch directory, not committed): the finite-subgroup transition couplings used in Part 3.

**What was read.** SK in full (L1-L645). The skill on origin/main in full. SX in full. CX Steps 0-7 (L1-L716). FE Steps 4, 6, 9 (L244-L629). FX Steps 4, 9 (L207-L668). FP Parts 1-2 and 3b.3 (L26-L186, L270-L289). PS Part 1 and Part 4 (L53-L150, L406-L424). MB Part 0.1 (L26-L36). FU L41-L152, L338-L378, L534-L574. VO L83-L212. EX L560-L610. EXT L70-L135. JO L100-L180. TR L180-L300. CF L73-L165, L428-L580. GOAL in full. The RESULT entries of FIN rows 780-838 (L856-L914), and rows 667, 668, 671, 717, 718, 736, 784.

**Where the earlier exercises stand (not repeated here).** Five ledgers exist: FP Part 2 (rows a1-f3, L105-L186), FX Step 4 (a1-h3, L207-L246), FE Step 4 (a1-f2, L244-L280), CX Step 4 (A1-F7, L325-L418) and SX Step 2 (A1-A24, L141-L172) with its variation table (L198-L229). Part 2 below cites them row by row and says whether their variation was complete. Rows they did not vary are marked **new**.

---

## Part 1. The ledger

Kinds: DEF = definition or target clause. SUP = supplied by the account or the literature. CH = a method choice. IN = a proved result the approach rests on (its check state given). RULE = an owner or lead rule. BEL = a belief from physics. HID = a hidden assumption, never written as one. PROC = process. Each row says where the skeleton or the approach uses it.

### (a) The target statement

| # | Assumption, in plain words | Kind | Where (mark) |
|---|---|---|---|
| 1 | The gap means spec(H) inside {0} union [m, infinity) with m > 0, for the OS Hamiltonian of one canonical component, with ker H = C Omega. | DEF | READ SK:29 |
| 2 | The Hilbert space is the cyclic sector of the one field tr(F^2), SA's O(f) = sum_p f(x(p)) a_p. | DEF | READ SK:33; MB:31 |
| 3 | Every canonical component of every volume-first limit must have the gap. | DEF | READ SK:29, SK:88 |
| 4 | Volume-first: infinite volume at fixed spacing and coupling, then the spacing limit. | DEF | READ MB:33 (SA 1673-1680) |
| 5 | Limits are subsequential, along SA's admissible sequence of first-passage data (K, beta_K), with beta/log(1/a) tending to 11N^2/(12 pi^2). | SUP | READ MB:32 |
| 6 | The unit of length is where the running coupling first enters the window [g^-2, g^-2 + B_sharp]; g is small. | DEF | READ SK:34; MB:32 |
| 7 | No value of m is asked; the expected value is about exp(-12 pi^2/(11 g^2)) up to a power of g. | DEF, GUIDE | READ SK:34 |
| 8 | The rate must be uniform in the cutoff in physical units; a lattice gap at one beta is neither needed nor enough. | DEF | READ FP:80 (1.3 (C)); SK:535 |
| 9 | The canonical component keeps the original subtraction. | DEF | READ sa-index/chunk-01.md:15 |
| 10 | The continuum datum (existence, OS axioms, convergence (H2), totality (TOT)) is supplied by the T0 chain; (GAP) is conditional on it. | SUP, OPEN | READ SL:200, SL:277 |
| 11 | The passage to the continuum uses reflected Hilbert norms, not sup norms of renormalized fields (Proposition P'). | IN (checked) | READ SL:200; CX:183 |
| 12 | A gap of the whole theory (more observables) is not asked. | DEF | READ SK:33 |
| 13 | O(4), Lorentz invariance and the Wightman theory are not used for the gap; only the Euclidean transfer in one lattice direction. | HID | ARGUED from SL:200 |
| 14 | Uniqueness of the limit state at fixed cutoff is not needed; every limit point is treated. | CH | READ SK:452 ((U) open) |
| 15 | (GAP) does not ask for confinement (no area law in the target). | DEF | READ SK:574 |

### (b) The interface with the Sussman-Alpoge account

| # | Assumption | Kind | Where (mark) |
|---|---|---|---|
| 16 | The object is SA's account, conditional on its packages A-H; their statements are read, their proofs mostly not. | SUP | READ SK:27; MB:28-36 |
| 17 | The account proves existence only: polynomial clustering is compatible with arbitrarily low positive spectrum, so no gap follows from its estimates. | SUP | READ CX:188 (SA:588-599); SX:58-61 |
| 18 | The account is Wilson-specific; regularisation independence is not asserted. | SUP | READ CX:353 (CA-I:2709) |
| 19 | SA's tori have four equal sides 2L^m (L odd, large) above the floor l_*(g) = 2L^11 M R(g^-2 + B_sharp). | SUP | READ PS:63-65 |
| 20 | (UV-Z): SA controls log Z of its tori only up to C l^4, at the one time extent equal to the side. | SUP | READ PS:68-74; PS:94-96 (Prop. 1.1) |
| 21 | SA integrates no scale between the unit and the torus side; control ends at the unit lattice. | SUP | READ PS:65 |
| 22 | Balaban's ultraviolet stability, as the account cites it, needs every effective coupling in (0, gamma]. | SUP | READ PS:76 |
| 23 | The infrared engine acts on the fine lattice as it is; no effective-action interface is used by Theorem S. | CH | READ FP:80 |
| 24 | The periodic seed needs only periodic partition functions (Theorem D: 1 + s <= e^Phi(n)), which are SA's objects. | IN | READ SK:386; RS L90 |
| 25 | SA's short-distance law, Theorem 0 (c)(3), for bumps of size and separation d <= d_0, is not used by the gap program. | HID, CH | READ PS:78 |
| 26 | Carrying the account past first passage to an effective coupling of order one (EXIT) is the crux itself. | DEF (reading) | READ PS:422; SK:564 |
| 27 | The vacuum-energy density is torus-independent only up to a constant delta_vac. | SUP | READ PS:76, PS:414 |
| 28 | SA's sides 2L^m match the sides of Theorem S only through Corollary S3' (every integer side >= 2N). | IN | READ SL:204; SK:440, SK:462 |
| 29 | Port rule: SA's proved statements are ported, not redone; proof work goes to their open statements. | RULE | READ GOAL:39-47 |

### (c) The seed and its continuation

| # | Assumption | Kind | Where (mark) |
|---|---|---|---|
| 30 | Theorem S: s = S(n;(2n)^3) < 1/5041 at one n >= 3 gives gap >= log(1/(5041 s))/n on the dyadic cubes. | IN (Claude Opus 5.5 row 698; Codex gpt-6-astra row 699) | READ SK:388-394, SK:434 |
| 31 | Corollary S3': one seed at size N gives the gap on every cube of integer side >= 2N. | IN (written by Codex gpt-6-astra; re-derived by the lead, Claude Fable 5.2) | READ SK:440 |
| 32 | Theorem SH: thresholds by shape, 1/1650 at r = 2 up to 3/10 for r >= 24. | IN (Claude Opus 5.5, row 707; same provider as the author) | READ SK:482, SK:498 |
| 33 | The seed is a trace over all states, with multiplicity, flux sectors included. | CH | READ FP:141 (c3); SK:402 |
| 34 | Theorem S uses only (TM), (TM-c) and axis symmetry, so it holds for every group, dimension and weight with a positive transfer operator. | IN | READ SK:442; FP:40 (F5) |
| 35 | P1: a seed at threshold t forces n m >= log(1/t); the seed cube is at least 12.9 of its own correlation lengths (14.8 at r = 2). | IN | READ PS:117-131 |
| 36 | The threshold ceiling is 1 (conditional on two recalled Ising facts); the class of the lemmas contains gapless models, so "the fall has to come from the group". | IN (conditional) | READ SK:484, SK:498 |
| 37 | The limit theorem: the conclusion of Theorem S gives clustering at rate m_0 in every limit state, on all integer sides. | IN (Claude Opus 5.5, row 703) | READ SK:444-452, SK:462 |
| 38 | Theorem EV-L: the limit half needs only the centre-even sector, (G_ev). | IN (Codex gpt-6-astra max, row 732) | READ SK:574 |
| 39 | The crossing step works for exactly three self-dual sector sets (periodic, full, kappa); none is the even sector alone; (EV-STEP) is open. | IN, OPEN | READ SK:576 |
| 40 | Theorem R: the even seed (ES), two numbers of the even sector, is equivalent at some size to one of the three seeds. | IN (Codex gpt-6-astra max, row 744) | READ SK:608, SK:620 |
| 41 | (ES) needs both numbers; the vacuum-energy defect equals the twelve heavy crossed flux weights up to even sums (Theorem V, row 751). | IN | READ SK:634-636 |
| 42 | The fusion consumer (FQ): 8 Q_F <= K(a) sqrt(S_ev), Q_F < 1/192, K polynomial, gives (F-h); small even sums are needed separately. | IN | READ VO:194-203; FU:66-69 |
| 43 | (E17): Q_F <= C a^p eta_*^(a/2), where eta_* = min over a fixed compact interval I of the one-step witness eta(beta) = e^(-80 beta) r^4/(4 + 16 r^4). | DEF (sufficient form) | READ EX:577-593; FU:97-105 |
| 44 | (V): max_k abs(log(Z^k/Z^0)) <= C a^p e^(-sigma a^2) on a fixed compact interval. | DEF | READ VO:100-105 |
| 45 | (J4): the odd-sector ratio is a signed sum over closed mod-2 surfaces against the original Z_m; the rooted bound (J12) suffices. | IN (row 816) | READ JO:141-156, JO:354 |
| 46 | The crux is (PHYS-SEED): the seed on one physical torus, uniformly in the cutoff. | DEF (crux form) | READ SK:535, SK:551 |
| 47 | (PHYS-SEED) holds if and only if (BDD-Delta) and (Z-UNB). | IN (row 720; check row 727) | READ SK:557-562 |
| 48 | Proved bare-Wilson ranges: seed and lattice gap for beta < 2/9; Langevin gap for beta < 1/4 on every torus; area law for beta < 2/3; SOS surface classes for beta <= 5/11; almost-flat class for beta <= 1/2. | IN | READ FIN:866 (790), FIN:894 (818), FIN:905 (829), FIN:901 (825), FIN:904 (828), FIN:903 (827), FIN:906 (830), FIN:893 (817), FIN:898 (822) |
| 49 | R1, the bare range up to about beta = 2, is not on the path of (GAP). | DEF (reading of row 712) | READ FP:100 (C3); SK:535 |
| 50 | The witness S_ev >= eta(beta)^t comes from one microscopic time step. | IN | READ FU:97-105 |
| 51 | Theorem CRIT: the set of couplings with a seed is open; (NOCRIT), no first critical point, is the lattice gap at every beta. | IN (row 709) | READ SK:503, SK:520 |
| 52 | A uniform gap with a state count N(E) <= A e^(theta n E), theta < 1, gives a seed; a gap alone is not shown to give one. | IN, OPEN | READ SK:449 |
| 53 | Rate filter: the lattice gap is at most C' exp(-c_AF beta (1 + o(1))). | IN (run 1, unchecked) | READ SK:65 |

### (d) The choice of variables

| # | Assumption | Kind | Where (mark) |
|---|---|---|---|
| 54 | Periodic tori: no walls, no fixed boundary. | CH | READ FP:132 (b3); CX:358 (B7) |
| 55 | The transfer operator is one lattice step along a lattice axis. | CH | READ FP:133 (b4) |
| 56 | (TM): a positive trace-class transfer operator with a simple top eigenvalue and a positive ground state, on boxes of every shape with sides >= 3. | IN (row 667 by Claude Opus 5.5; check row 671 by Codex gpt-6-astra; shapes rows 698, 699) | READ RS L33 |
| 57 | (TM-c): centre flips commute with T and give twisted partition functions as traces. | IN (corrected, rows 698, 699) | READ RS L35 |
| 58 | (TM-tw): twisted spatial weights keep (TM). It lives in check files, not in a lemma of its own. | IN (scattered) | READ FX:218 (b3), FX:660 |
| 59 | Reflection positivity at coordinate mirrors for the Wilson weight. | IN | READ FP:37 (F2) |
| 60 | Twists are classes in H^2(T^4; Z_2), six bits; flux sectors are electric, magnetic or dyonic; frames are chosen per use. | DEF | READ VO:87-90; FX:236 |
| 61 | Z^k <= Z^0 and Z^(m+v) <= Z^m for every twist. | IN (row 822 calls it a READ fact) | READ VO:93-96; FIN:898 |
| 62 | Isotropy lets each axis serve as time (crossing). | CH | READ FP:131 (b2) |
| 63 | Observables are gauge-invariant functions of one time slice; centre-blind local functions suffice for the limit half. | DEF | READ FP:115 (a3); CX:363 (B12) |
| 64 | The seed splits into a glue half (the even thermal sum) and a flux half (twist ratios near 1). | IN (P2 of row 712) | READ FP:57 |
| 65 | Surface variables: exp(beta eta x) = cosh(beta x)(1 + eta tanh(beta x)) gives closed mod-2 surfaces (J2)-(J4). | CH | READ JO:105-126 |
| 66 | Normalized Haar measure, exact gauge invariance, a compact link space, a strictly positive density. | DEF | READ CX:355-356 |
| 67 | The Langevin dynamics of (G2) is an auxiliary tool, not physical time; a uniform invariant gap gives decay (Lemma L). | IN | READ FIN:888 (812), FIN:891 (815) |

### (e) The lattice setting

| # | Assumption | Kind | Where (mark) |
|---|---|---|---|
| 68 | The Wilson action exp(-beta sum_p (1 - (1/2) tr U_p)). | DEF | READ SK:75; EXT:85-89 |
| 69 | Gauge group SU(2), centre Z_2. | DEF (owner: SU(2) first) | READ GOAL:22 |
| 70 | Four dimensions. | DEF | READ GOAL:22 |
| 71 | One beta in all six planes. | DEF | READ FP:131 |
| 72 | theta = 0 and real beta > 0. | DEF | READ CX:354 (B3) |
| 73 | Nearest-neighbour plaquettes; each link lies in six plaquettes. | DEF | READ CX:357 (B6); SX:169 |
| 74 | The coupling path: bare beta grows like 0.37 log(1/a) along SA's sequence. | DEF | READ MB:32 |
| 75 | The lane's beta is Wilson's beta_W = 4 beta of Shen-Zhu-Zhu and of the Bhattacharjee papers. | CONVENTION | READ FIN:895 (819); FIN:900 (824) |
| 76 | Integer sides >= 3. | DEF | READ CX:360 (B9) |
| 77 | Pure gauge theory: no matter, no Higgs field, no deformation to remove. | DEF | READ CX:384 (C19) |
| 78 | No transition on the Wilson axis. | BEL (GUIDE) | READ FP:159 (e1); FP:49 (F14) |
| 79 | Asymptotic freedom: the flow reaches disorder from every beta. | BEL | READ FP:161 (e3) |
| 80 | Confinement at every beta. | BEL | READ FP:160 (e2) |
| 81 | The R1 theorems are proved for the exact Wilson weight: von Mises-Fisher one-link laws, the tanh grading, the Haar moments 1/4, 1/8, 5/64. | HID | READ FIN:861 (785), FIN:893 (817), FIN:899 (823) |

### (f) The binding tests

| # | Assumption | Kind | Where (mark) |
|---|---|---|---|
| 82 | U(1) has no gap at weak coupling. It is a theorem only at large beta (Frohlich-Spencer with fixed boundary; periodic Villain for beta >= 2^14, row 786); every order-one use is GUIDE (row 784). | SUP, GUIDE | READ SK:61; FIN:858, FIN:860, FIN:862 |
| 83 | Z_2 has a gap at weak coupling and a transition; it binds the periodic seed (flux half) only. | SUP | READ SK:62, SK:578 |
| 84 | The finite-subgroup test is "the weak-coupling binary icosahedral model" 2I. | CH | READ SX:123-124; FIN:859 (783), FIN:876 (800), FIN:880 (804) |
| 85 | The Q_8 test (argued in row 780). | CH, ARGUED | READ FIN:856 (780); CF:73-80 |
| 86 | K7: the mixed fundamental-adjoint action has a first-order line ending near (1.48, 0.90). | GUIDE | READ SK:505; FP:282 |
| 87 | K6: SU(2) on a slab of width 1/T_c is critical. | GUIDE | READ SK:63 |
| 88 | The rate filter and the upper bounds on m. | IN | READ SK:65-66 |
| 89 | Two dimensions is solved exactly (positive control). | SUP | READ SK:67 |
| 90 | Valid form of a test (Proposition T1); range form (T3), ending near 0.44 (centre-blind), 1.01 (torus-blind), 1.6 (oscillation-blind). | IN (logic) | READ FP:274-285 |
| 91 | The worded test "it also holds for U(1), so it fails" is false. | IN | READ FP:276 (T2); FP:150 (d1) |
| 92 | N-test (SU(N >= 5) bulk transition) and dimension test (5D SU(2)). | GUIDE | READ FP:71-78 |
| 93 | Proposition V (one-well weights with every Wilson symmetry and a transition) stays conditional on van Enter-Shlosman covering 4D SU(2). | IN (conditional) | READ SK:537; FIN:793 (717) |
| 94 | Finite groups bind the flux half only; for (G_ev) and (GAP) they are positive controls at weak coupling. | DEF (reading) | READ SK:578; FX:636-637 |
| 95 | A test is applied to each proof step, not to the composite proof. | HID | READ FIN:859 (783: "use of SU(2) beyond contraction and flattening") |
| 96 | A positive control tests necessity claims, not tools. | IN (logic) | READ FE:382-391 |

### (g) The proof rules

| # | Assumption | Kind | Where (mark) |
|---|---|---|---|
| 97 | Every step is a written argument a person can check. | RULE | READ GOAL:14 |
| 98 | Every step is Lean-formalizable. | RULE | READ GOAL:14 |
| 99 | No computer discharge; a run may guide or refute only. | RULE | READ GOAL:10-16 |
| 100 | No new axioms; the repository's framework axioms and primitives are not used by this target. | RULE, reading | READ CX:66; SX:149-150 |
| 101 | Literature lemmas are rebuilt in the repository; citations never carry weight. | RULE | READ GOAL:17 |
| 102 | Constants are explicit or given by a stated existence argument. | RULE | READ GOAL:17 |
| 103 | Stop rule: a proof, a counterexample, or one lemma failed three ways; after two stops a max author restates. | RULE | READ SK:207 |
| 104 | An author brief on the crux names one of the means (M1)-(M4) or a fifth. | RULE (lead) | READ SK:594 |
| 105 | No route is called the only or the last one. | RULE | caller's brief |

### (h) The process

| # | Assumption | Kind | Where (mark) |
|---|---|---|---|
| 106 | Authorship: Claude Fable 5.2 max sets direction, Fable medium proves, Claude Opus 5.5 checks and ports, Codex gpt-6-astra cross-checks (and since 2026-11-12 authors), Codex gpt-6-luna reads. | PROC | READ SK:211, SK:632 |
| 107 | A check by a model that did not write the proof is the check; same-provider checks are labelled. | PROC | READ SK:211, SK:347 |
| 108 | One check per proof. | PROC (owner) | memory index (owner 2026-11-03) |
| 109 | Two runs of one model are samples, not checks; the lead's re-derivation is not independent. | PROC | READ SK:20, SK:378 |
| 110 | Progress is open statements closed (GOAL metric); in practice it is proved coupling ranges extended. | PROC | READ GOAL:90-92; FIN:909-912 (833-836) |
| 111 | Hardest first; the crux over packaging; the worth-doing test. | PROC (owner) | memory index |
| 112 | Routes are chosen by max-author plans and the lead's reading; the crux is restated after two stops. | PROC | READ SK:207, SK:374 |
| 113 | The queue races unrefereed preprints in R1. | PROC | READ FIN:895 (819); FIN:909 (833: "beyond every claim") |
| 114 | Several facts that the tests rest on are recalled or read in abstract only. | PROC | READ FIN:858 (782), FIN:882 (806), FIN:904 (828) |
| 115 | GUIDE runs steer direction ("any route at order one must be collective"). | PROC | READ FIN:896 (820) |
| 116 | A past discard keeps its stated reason; the reason is re-judged only when a lane reopens it. | PROC | READ CX:507-650; FE:334-367 |

Part 1 complete: 116 rows.

---

## Part 2. What if each assumption is wrong

Columns: what follows if the row is wrong or dropped, and what that costs in the lane's proved results; a concrete test; whether an earlier exercise varied it (path:line) and whether that variation was complete. "Complete" means the variation stated the consequence and a test, and nothing since has changed it. **new** = not varied before.

### (a) Target

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 1 | A clustering rate without spectral exclusion is weaker: SA's polynomial clustering allows no gap. No proved result changes. | Definitional. | CX A2-A3 (L341-L342). Complete. |
| 2 | A target with more observables: the infrared engine already gives a gap on the whole transfer space at each cutoff, so the infrared half is unchanged; more T0 convergence work. | Proposition P' needs only (H2) and (TOT) for the chosen class (READ SL:200). | CX A1 (L340); FP a3 (L115); FX a2 (L214); SX A17 (L165). Complete. |
| 3 | One component would suffice and remove the uniqueness costs of T7 and Z10. Nothing lost: a seed gives every component. | None needed. | CX A6 (L345); FX a1 (L213). Complete. |
| 4 | Spacing first on fixed tori: the continuum torus seed is the same (PHYS-SEED) after the limit, but the two orders are not identified. No proved result lost. | Does the lattice thermal sum converge to the continuum one at fixed temperature? Needs trace-norm convergence of the transfer; OPEN. | CX A4 (L343). Partial: no test named. |
| 5 | Another sequence: Proposition P covers any family with n a <= l_* (READ SL:264). Nothing lost. | None. | **new**; no gain. |
| 6 | A unit choice cannot turn zero into a positive mass. | None. | CX B14 (L365). Complete. |
| 7 | An explicit m would need L_* explicit. | None. | CX A7 (L346). Complete. |
| 8 | Dropping cutoff uniformity leaves lattice theorems only. This row decides whether the work of rows 785-836 is on the path of (GAP): it is only through a hand-off architecture (rows 26, 81; Part 3.3). | The worth-doing test on each R1 item: does it enter any chain to (GAP)? | FP a1 (L113); CX A5 (L344); FE a3 (L252). Complete as logic; not applied to the queue since row 785 (row 110). |
| 9 | A non-extensive box counterterm would change delta artificially; not allowed. | None. | CX B13 (L364). Complete. |
| 10 | Without T0, (GAP) has no object; the lattice results stay. | The T0 chain (its own lanes). | CX I2 (L176); FX f3 (L234). Complete as reading. |
| 11 | Sup norms of renormalized fields diverge; P' avoids them. | None. | CX C16 (L381). Complete. |
| 12 | See row 2. | - | CX A1. Complete. |
| 13 | O(4) is not needed: the Hamiltonian is the generator of one time translation (READ SL:200). Nothing lost. | None. | **new**; no gain. |
| 14 | If uniqueness were needed, T7 and Z10 would be on the path; the seed gives clustering in every limit state anyway (row 37). | None. | CX A6. Complete enough. |
| 15 | If confinement were part of (GAP), the flux half would bind the limit half too; EV-L shows it binds only the step. | None. | FX c1 (L220). Complete. |

### (b) Interface with the account

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 16 | If the packages fail, there is no continuum object; the lattice results stay. | The T0 chain. | CX I2; FX f3. Complete as reading. |
| 17 | If the account gave a gap, the crux would be ported, not proved. Two readers (CX, SX) confirm the polynomial-clustering caveat. | READ CX:188, SX:58-61 (SA:588-599). | CX I14. Complete. |
| 18 | With universality as a theorem, any action in the class could be used; no known action makes the crux easier in four dimensions. | None. | FP b1 (L130); CX B2 (L353); FE b1 (L253); SX A3 (L151). Complete. |
| 19 | Without the floor, tori near the unit could be used, but S is large there (PS 1.2). | None. | PS Part 4, E2 (L415). Complete as reading. |
| 20 | A sharper UV-Z would still be short of the seed: S is of order one or larger on small tori. | PS Proposition 1.1 (PROVED there). | Complete. |
| 21 | Integration past the unit is EXIT (row 26). | - | CX C17 (L382). Complete. |
| 22 | If Balaban's method worked at order one, the RG would close the crux. | None; it is the crux. | PS Part 4. Complete as reading. |
| 23 | If the infrared engine had to act on an effective theory, RP and (TM) would be needed for effective actions; the RG map is not shown to keep RP. Theorem S could not be used as it is. | Is the blocking map RP-preserving? Not shown. | FP 1.3 (C) (L80). Complete; the choice is sound. |
| 24 | Full and kappa seeds need twisted partition functions, which SA does not control; the periodic seed avoids this. | None. | FX c3 (L222). Complete. |
| 25 | **new.** SA's short-distance law can supply a cutoff-uniform witness for the fusion consumer (Part 3.2, Lemma W). Cost: one interface statement, (SD-cyl), must be ported. | Part 3.2. | **new.** |
| 26 | If EXIT were easier than the crux, the R1 results would be on the path as a landing zone. PS Part 4 says EXIT is the crux; I agree. | None. | PS Part 4; CX C17. Complete. |
| 27 | The density bound is multiplied by the number of unit cells; an exact cancellation is needed for (BASE-Phi). | - | PS E1 (L414). Complete. |
| 28 | Without S3', seeds on a block of sizes. | - | Rows 699, 703. Complete. |
| 29 | Redoing ported work changes no science. | - | FX f3. Kept. |

### (c) Seed and continuation

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 30 | If Theorem S failed, the infrared engine and every seed form fall. Checked by two providers. | - | FP c2 (L140) named unused structure (chessboard bounds, twists, convexity in beta); partial: none tried as a step. |
| 31 | Without S3', blocks of seed sizes. | - | No need. |
| 32 | If SH failed, the threshold falls back to 1/5041; constants only. Its only check is same-provider. | A cross-provider check (Part 3.5). | FX c4 (L223). Constants only. |
| 33 | A correlation criterion would avoid state counting, but finite scalar moments cannot certify a gap (SX (A1)). | - | FP c3 (L141); CX C7 (L372); SX A6 and Route A (L154, L358-L405). Complete. |
| 34 | - | - | FP F5, C6. Complete. |
| 35 | P1 is a theorem; a seed box of a few correlation lengths does not exist in this family. | - | FE N3 (L388). Complete. |
| 36 | A lower ceiling would bound thresholds; the ceiling is conditional on two Ising facts. | - | Rows 705, 707. Complete. |
| 37 | If the limit theorem failed, seeds give lattice gaps but no limit statement. Author Claude Fable 5.2, checker Claude Opus 5.5: same provider. | A cross-provider check (Part 3.5). | **new** as a process risk. |
| 38 | - | - | FX c1. Complete; checked cross-provider. |
| 39 | If (EV-STEP) held, confinement would leave the step's path too. | - | FX c2 (L221) and 8.5. Complete for crossing steps; other steps are row 691's. |
| 40 | - | - | CX I6-I7 (L180-L181). Complete. |
| 41 | - | - | Rows 748, 751, 753. Complete. |
| 42 | (FQ) allows K polynomial in the lattice size; at a fixed physical size that diverges as the spacing goes to zero. The continuum consumer needs K bounded. No proved result changes. | Part 3.2. | FU §6 (L559-L572) named the cutoff scope; SX A10 (L158). Partial. |
| 43 | (E17) cannot be the continuum consumer: along SA's sequence the witness eta(beta_j)^(n_j/2) is at most exp(-14.8 (L/a_j) log(1/a_j)) on a torus of fixed physical side L (Part 3.2, PROVED arithmetic), while the physical twist deficit at fixed L is expected to stay positive (ARGUED). Cost: "(RTAIL) is equivalent to (E17)" (rows 817, 823) is a statement on a fixed coupling interval, an R1 statement. | Part 3.2. | SX A10 (L158) and FU §6, partial. **The failure at fixed physical size is new.** |
| 44 | (V) is stronger than (FQ). | - | Rows 778-801. Complete. |
| 45 | The absolute (J12) is stronger than the signed target. | - | SX A11-A12 (L159-L160). Complete. |
| 46 | Another infrared engine (all-boundary criteria (W); Route Z's dominance form) would avoid the trace; none is supplied. | - | FP c1 (L139); FE a1-a2 (L250-L251); CX B15, C9 (L366, L374). Complete as alternatives. |
| 47 | The two-statement form lapses if Theorem ZD fails. Check pending (row 727). | - | Complete as reading. |
| 48 | Data. Most of these ranges have cross-provider checks (rows 790, 828, 829, 822, 826, 830). | - | - |
| 49 | If R1 were on the path, the coupling-range race would compound toward (GAP). It does only through a hand-off (Part 3.3). | Part 3.3. | FP C3, a6 (L100, L118); FE a3. Complete as logic. |
| 50 | A physical-scale witness exists given (SD-cyl) (Part 3.2). | Part 3.2. | FU §6 named the need, supplied none. **new supply.** |
| 51 | If (NOCRIT) failed, the lattice target fails at beta*; the continuum may still hold. | - | FP c5 (L143). Complete. |
| 52 | If a gap did not give a seed, the method could miss a true gap. GUIDE: at the seed temperature (about 0.5 T_c) the Hagedorn growth of glueball states satisfies theta < 1. | A state-count bound for SU(2) at the seed temperature; OPEN. | FP e5 (L163). Partial. |
| 53 | If wrong, a mechanism with a gap of order beta^(-p) would not be excluded. Unchecked (run 1). | A check of run 1's Lemma 6. | None. Low cost. |

### (d) Variables

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 54 | Walls remove winding flux but lose the trace formula and crossing; Route Z has its own crux. | - | FP b3; CX B7; FE a2; SX A5. Complete. |
| 55 | - | - | FP b4. Trivial. |
| 56 | Everything falls; checked cross-provider. | - | FX b3. Complete. |
| 57 | - | - | Rows 698-699. Complete. |
| 58 | If (TM-tw) failed where an electric and a magnetic stack meet, the full and kappa seeds and Theorem R's crossed weights fall. | Write (TM-tw) as its own lemma (FX 9.7 item 2, L660); proposed in row 731, never queued. Cheap. | FX b3. Complete as a dependency; the lemma is unwritten. |
| 59 | - | - | SX A20 (L168). Complete. |
| 60 | - | - | FX h1-h2 (L236). Complete. |
| 61 | If false for a twist, R_m <= 1 and the lower bounds of rows 816, 822 fail. Part 3.6 proves it by frames (PROVED, unchecked), so it is not only a READ fact. | Part 3.6. | None; settles a reading-state flag of row 822. |
| 62 | - | - | FP b2; SX A7. Complete. |
| 63 | - | - | FP a3; CX B12. Complete. |
| 64 | - | - | FP c6. Complete. |
| 65 | Other expansions (all spins; the SO(3) x Z_2 split of Identity 4.4; the Gaussian enlargement, equivalent to the Wilson gap by SX (B3)). | - | SX Route B (L407-L473); rows 809, 811. Partial. |
| 66 | - | - | CX B4-B5; SX A19. Complete. |
| 67 | - | - | SX A13-A14; CX E3. Complete. |

### (e) Lattice setting

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 68 | - | - | FP b1; CX B2; FE b1; SX A3. Complete. |
| 69 | Large N gives a second small number; an owner decision, named as a price only. | - | FP a4; CX B1; FE b2; SX A4. Complete. |
| 70 | In three dimensions R2 has about log beta doublings; still open. | - | FP a5; CX B1. Complete. |
| 71 | Anisotropy kills crossing. | - | FP b2. Complete. |
| 72 | A theta term removes positivity. GUIDE (recalled, Gaiotto-Kapustin-Komargodski-Seiberg 2017): at theta = pi a mixed anomaly forbids a unique trivially gapped vacuum, so any theta-blind argument for a unique gapped vacuum would fail there; theta lies outside the lane's positive class, so this binds nothing. | - | CX B3 (L354). Complete; the anomaly remark is new and inert. |
| 73 | - | - | CX B6; SX A21. Complete. |
| 74 | - | - | FE c5-c6 (L260-L261); FP c4 (L142). Complete. |
| 75 | - | - | Row 824. Complete. |
| 76 | - | - | CX B9. Complete. |
| 77 | A Higgs field: complementarity (Osterwalder-Seiler; Fradkin-Shenker, recalled) joins the Higgs and confinement regions, but every path to the pure theory at large beta crosses the order-one region at zero hopping. Removal needs a uniform rate. | - | CX C19 and M6. Complete. |
| 78 | The lattice target fails; the continuum may hold. | - | FP e1; FX e1; FE e1. Complete. |
| 79 | No gap at large beta; the problem is false. | - | FP e3. Complete. |
| 80 | The seed fails where confinement fails, even with a bulk gap. | - | FP e2. Complete. |
| 81 | **new.** Under a hand-off architecture the R1 theorems must hold for a class of effective actions. Cost: Theorem V (the von Mises-Fisher quarter) and the tanh grading are exact-Wilson. | Part 3.3. | **new.** |

### (f) Binding tests

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 82 | - | - | FP d1, T1-T3; row 784 audit. Complete for U(1) and Z_2. |
| 83 | - | - | FX d2 (L227). Complete. |
| 84 | **new.** If 2I does not bind at order one, every "group-blind for 2I" limitation in rows 783, 800, 804, 817, 823, 827, 830 is void below about beta = 5.7 (GUIDE), and the binding finite groups at the crossover are Q_8 and 2T. | Part 3.1. | **new.** |
| 85 | Row 780 argued it; CF §1 found no theorem. Part 3.1 places it: Q_8 binds above about beta = 1.15 (GUIDE). | Part 3.1. | Partial. |
| 86 | - | - | FP d2, T3. Complete as GUIDE. |
| 87 | - | - | Not varied; no gain. |
| 88 | - | - | Not varied; no gain. |
| 89 | - | - | Not varied; no gain. |
| 90 | - | - | FP 3b.3. Complete; extended by the finite-subgroup ladder of Part 3.1. |
| 91 | - | - | Complete. |
| 92 | - | - | FP 1.3. Complete as GUIDE. |
| 93 | - | - | Row 717. Complete. |
| 94 | - | - | FX 9.3 for Z_2. Complete for Z_2; extended to the ladder in Part 3.1. |
| 95 | **new.** If tests bind only the composite proof, a step whose hypothesis is produced by a step that already fails for the comparison model need not fail for it. | Part 3.1 (d). | **new.** |
| 96 | - | - | FE 6c. Complete. |

### (g) Proof rules

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 97-99 | Relaxed, R1 could move by rigorous numerics (FP f3: cluster expansions to a few tenths; finite-size criteria further, cf. the Ursachi preprint, abstract only); R2 would not move. Owner rule. | - | FP f1-f3 (L170-L172); FX f1; FE f1; CX F1; SX A24. Complete. |
| 100 | - | - | CX Step 0; SX A1-A2. Complete. |
| 101-102 | - | - | Kept. |
| 103 | If too strict, restatements multiply; each is an exact price, not progress past the wall. | - | None. Low. |
| 104 | If (M1)-(M4) are not all (belief B4, unresolved by row 736), the rule already admits a fifth. | - | FE e4. Complete as a belief. |
| 105 | - | - | Kept. |

### (h) Process

| # | If wrong or dropped; cost | Test | Varied before |
|---|---|---|---|
| 106-107 | Same-provider checks can share blind spots. The infrared-engine statements with only same-provider checks: Theorem SH (row 707), the limit theorem (row 703), Theorem DOB (row 709), the strong-coupling seed (row 704), Theorem U (row 715). | Part 3.5. | FX f2; CX F5. Partial. |
| 108 | One check lets an error survive once; the 698/699 disagreement on Corollary S3 shows a second check can catch what a first one passed. | Second checks on the infrared engine. | None. |
| 109 | - | - | Fine. |
| 110 | **new as a process risk.** Measured by R1 ranges, the effort since row 785 goes to lattice theorems off the path of (GAP) (row 49). The continuum crux has not changed since SK 13.20. | Worth-doing test on rows 785-836: which critical-path item of (GAP) moved? Reading: none. | **new.** |
| 111 | - | - | Fine. |
| 112 | The crux has about ten exact forms ((ZF_B), (W), (SEED), (PHYS-SEED), (Z-UNB), (G_ev), (ES), (V), (FQ), (E17), (RTAIL)); each is a price, not a pass. | - | FE 9.4. Complete as a rule. |
| 113 | **new.** A novelty race sends lanes to R1 beyond 1/3 (row 833) rather than to the crux or to an off-crux theorem of another kind (Part 3.4). | Owner decision; named only. | **new.** |
| 114 | Wrong recalled facts change test verdicts. Part 3.1 replaces one (no coupling was assigned to the finite-subgroup transitions in row 806) with a READ table. | Part 3.1. | Partial. |
| 115 | Labelled GUIDE; direction only. | - | Fine. |
| 116 | **new.** If reasons are not re-judged, discards outlive their reasons. | Part 3.7. | **new.** |

Part 2 complete.

---

## Part 3. Review: the ideas worth testing, with real attempts

**How I chose.** I read the 116 rows for three things: (i) a changed assumption that could reach or bypass the order-one regime; (ii) a row on which a past verdict rests and which I now doubt; (iii) a cheap decisive test. No row gives a route through the order-one regime. Six ideas survive. Two of them change verdicts the lane already acted on (3.1, 3.2). Each has its first statement written and attempted below.

**Readings registered before the tests.** The hand calculations of 3.1 (Lemmas F1-F3, F5) came first. The pass and fail readings below were fixed after them and before the GUIDE script ran. Nothing was changed after the script; it agreed with every hand value.

### 3.1 Idea 1 (rank 1). The binary icosahedral test does not bind at order one; Q_8 and 2T do

**Changed assumption.** Rows 84, 85, 94, 95: "the finite-subgroup test is the binary icosahedral group 2I", applied to each proof step at every coupling.

**Why it matters.** The 2I test drove decisions. Row 783 concluded that commutator contraction plus density flattening "do not separate SU(2) from finite subgroups" and asked for "a quantitative use of SU(2) beyond the shared contraction and density flattening" (READ CF:568-571). Row 804 set aside its pair-Casimir filters because "(G7) is shared" and built a spin-6 charged filter (READ TR:106; FIN:880). Rows 817, 823, 827 and 830 each record "group-blind for the binary icosahedral group" as a limit. Row 806 read the freezing literature and assigned no coupling (READ prior/gap-lit-icosa.md:39).

**First statement.** For which couplings does a finite subgroup G of SU(2) refute a flux-half tool that cannot tell G from SU(2)?

**Lemma F1 (moment degree; PROVED).** Let G be a finite subgroup of SU(2) acting on V = C^2. The G-average of g^(tensor n) equals the SU(2) Haar average for every n < d_G and differs at n = d_G, where d_G is the least positive degree of a G-invariant polynomial on V. For Q_8 (the binary dihedral group of order 8), 2T, 2O, 2I: d_G = 4, 6, 8, 12. Every binary dihedral group BD_n has d_G = 4.

*Proof.* The matrix entries of g^(tensor n) span the matrix coefficients of the spins j with 2j <= n. The SU(2) average of a nontrivial irreducible is zero; the G-average is the projection on its G-fixed vectors. So the averages agree up to degree n if and only if no V_j = Sym^(2j) V with 1 <= 2j <= n has a G-fixed vector, that is, no G-invariant homogeneous polynomial of degree 2j <= n. Klein's invariant degrees are 12, 20, 30 for 2I; 8, 12, 18 for 2O; 6, 8, 12 for 2T. For Q_8, generated by diag(i, -i) and [[0, 1], [-1, 0]], the polynomials x^2 y^2 and x^4 + y^4 are invariant, and no quadratic is (xy changes sign under the second generator). For BD_n, x^2 y^2 is invariant. A check by class sums of the even moments E_G[x^(2k)], x = tr(g)/2: with the class data (x = +-1: one each; Q_8: six with x = 0; 2T: six with x = 0, sixteen with x = +-1/2; 2O: those plus twelve with x = 0 and twelve with x = +-1/sqrt 2; 2I: thirty with x = 0, forty with x = +-1/2, twenty-four each with x = +-phi/2 and x = +-(phi - 1)/2), the numbers 4^k E_G[x^(2k)] for k = 1, ..., 6 are 1, 4, 16, 64, 256, 1024 (Q_8); 1, 2, 6, 22, 86, 342 (2T); 1, 2, 5, 15, 51, 187 (2O); 1, 2, 5, 14, 42, 133 (2I), against the Catalan numbers 1, 2, 5, 14, 42, 132 of SU(2). For 2I, 4^6 E = (2 4^6 + 40 + 24 L_6/2^6)/120 with L_6 = (3 + sqrt 5)^6 + (3 - sqrt 5)^6 = 20608, which gives 133; this is row 805's "133 = 132 + 1". QED

**Lemma F2 (the commutator contraction is shared by every non-abelian finite subgroup; PROVED).** If G acts irreducibly on V, then E_{A,B}[A B A^(-1) B^(-1)] = (1/4) I on V, for A, B independent and uniform on G.

*Proof.* Schur's lemma gives E_A[A M A^(-1)] = (tr M/2) I. Orthogonality of matrix coefficients gives E_B[chi(B) B^(-1)] = I/2. Together, (1/2)(1/2) I. QED. So the centre-odd norm 1/4 of rows 778 and 800 is the same for Q_8, 2T, 2O, 2I and every BD_n. For row 778's (5) and (6) this proves the sharing that row 780 argued for Q_8; (8)-(10) are not re-derived here.

**Lemma F3 (the pair-Casimir filters of row 804 are shared, Q_8 included; PROVED).** Let A_G = E_G[k_beta(g) (g tensor g tensor I)] with k_beta proportional to exp(beta tr(g)/2), and P the singlet projection of row 804's (G5). Then A_G = P + t_G (I - P) for each of Q_8, 2T, 2O, 2I, with 0 < t_G < 1 at every finite beta, and

```math
t_{Q_8}(\beta)=\frac{\cosh\beta-1}{\cosh\beta+3}.
```

So (G7)-(G11) hold for each of these groups with t replaced by t_G: the norm of the product of the two filters is at most 1/2 + 2 t_G and below 1 at every beta.

*Proof.* On V tensor V the singlet is fixed by every g. On the spin-1 part, g acts by its rotation R(g). The average of k_beta(g) R(g) commutes with every R(h) because k_beta is a class function. For 2T, 2O, 2I the rotation groups A_4, S_4, A_5 act irreducibly on R^3, so the average is a scalar t_G = E_k[4x^2 - 1]/3 by Schur's lemma; t_G < 1 because k_beta has full support and no nonzero vector of R^3 is fixed by the whole group. For Q_8 the rotations are diag(1, -1, -1), diag(-1, 1, -1), diag(-1, -1, 1) and the identity. The weights are e^beta at g = 1, e^(-beta) at g = -1 and 1 at the six others. The entry along axis 1 is (e^beta + e^(-beta) + 2 - 2 - 2)/(e^beta + e^(-beta) + 6) = (cosh beta - 1)/(cosh beta + 3). The automorphism of Q_8 that permutes i, j, k cyclically keeps traces, so the three axes agree. QED

**Lemma F4 (perfectness; PROVED from standard group theory).** The commutator subgroups are [Q_8, Q_8] = {+-1}, [2T, 2T] = Q_8, [2O, 2O] = 2T, [BD_n, BD_n] = the cyclic group of order n, and 2I is perfect (row 783 proved this through SL(2, F_5)). So among the binary polyhedral groups only 2I has the full-Haar minorization of iterated commutator laws, (30)-(31) of row 783. For Q_8, 2T and 2O the iterated commutator law lives on a proper subgroup that still contains -1. It still averages centre-odd functions to zero on its support, but it has no Haar component on G.

**Lemma F5 (the von Mises-Fisher quarter is SU(2)-specific; PROVED).** For the one-link law proportional to exp(F . q) on Q_8, the supremum over F of the largest covariance eigenvalue is 1/2, not the SU(2) value 1/4 (Theorem V of row 785).

*Proof.* Take F = f (1, 1, 0, 0)/sqrt 2 and u = (1, -1, 0, 0)/sqrt 2, c = f/sqrt 2. The elements 1 and i get weight e^c, -1 and -i get e^(-c), the other four get 1. The mean of u . q is zero, and its variance is (e^c + e^(-c))/(2 e^c + 2 e^(-c) + 4), which tends to 1/2. QED. So Lemma INF's beta/4 per neighbour, and every R1 range built on it (the seed below 2/9, the area law below 2/3), uses SU(2) beyond what Q_8 shares.

**READ (GUIDE): where each group freezes.** Hartung, Jakobs, Jansen, Ostmeyer and Urbach (arXiv:2201.09625, Table IV, Monte Carlo with hot and cold starts on 8^4 lattices, action S = -(beta/2) sum Re Tr P, which is the lane's beta): the binary dihedral group of order 8 (Q_8) at 1.15(15); 2T at 2.15(15); 2O at 3.20(10); 2I at 5.70(20). Petcher and Weingarten (Phys. Rev. D 22 (1980) 2465) report first-order transitions for these groups (abstract, as read by row 806). Above its transition a finite gauge group is frozen: plaquettes sit near the identity, a magnetic twist costs a sheet of order beta times its area, and (V) fails. Below it the group confines like SU(2), as far as the numerics show. Both statements are GUIDE.

**Proposition F6 (the test profile at a coupling; ARGUED from Proposition T3 of row 712 and the READ couplings).** Let a flux-half tool ((V), (FQ), (E17), the flux half of a seed) be claimed on an interval I = [beta_-, beta_+], with a proof that uses only properties the Wilson measure of G shares. Then G can refute the tool (GUIDE) only if beta_+ is above beta_c(G); above it, G refutes every such tool whose hypothesis holds for G there. So:

| Comparison model | What it shares with SU(2) Wilson | Binds flux-half tools (GUIDE) above | Glue half |
|---|---|---|---|
| Z_2 (the centre) | the centre; moments to degree 1 | 0.44 | does not bind (gapped) |
| U(1) (a maximal torus) | the weight exp(beta cos phi) | 1.01 | binds (photon) |
| Q_8 = BD_2 | moments to degree 3; F2; F3 | 1.15 | does not bind |
| K7 (oscillation of log w) | group, centre, RP, one-loop coefficient | about 1.57 | binds on its line |
| 2T | moments to degree 5; F2; F3 | 2.15 | does not bind |
| 2O | moments to degree 7; F2; F3 | 3.20 | does not bind |
| 2I | moments to degree 11; F2; F3; full flattening (F4) | 5.70 | does not bind |

At the SU(2) crossover, about beta in [1.5, 2.5], the binding finite groups are Q_8 and, above 2.15, 2T. The 2I test binds only on intervals that reach about 5.7. **As theorems, none of these tests binds at order one**: no finite-group failure of (V) is certified even at weak coupling (READ CF:75-80), and the U(1) failure is a theorem only for beta >= 2^14 (row 786). Every test at order one is a guide. Row 784 found this for U(1); the finite groups now join it. For the glue half, the finite groups are positive controls at every coupling (row 731 for Z_2; Adhikari and Cao for finite groups, as read in CF:138-144), so the ladder binds flux-half tools only.

**The channel a tool must see.** Above beta_c(G) a tool must use SU(2) beyond degree d_G - 1: spin 2 on (1.15, 2.15), spin 3 on (2.15, 3.2), spin 4 on (3.2, 5.7), spin 6 above 5.7. At beta = 2 the SU(2) convolution on the charged space V tensor V_j has norm r_(j - 1/2)(2) = I_(2j)(2)/I_1(2): 0.0319 for j = 2, 0.0010 for j = 3, 1.4 x 10^(-9) for j = 6. On its invariant copy V tensor V_j^G the group G has the eigenvalue E_G[k_2(g) x]: 0.536 for Q_8 and 0.436 for 2T (GUIDE values of exact formulas; script output in scratchpad/lane838/scripts/subgroups.out). So at the crossover the separation from Q_8 sits at spin 2, with a factor of about 17, and from 2T at spin 3, with a factor of about 430. The spin-6 filter (G15) of row 804 pays a factor of about 10^(-9) for a separation that no binding group asks for below 5.7.

**(d) The composite form (ARGUED).** Write a proof of (PHYS-SEED) as IR after UV: UV takes the bare measure at (beta_j, a_j) to a hypothesis H_eff on an effective measure at a fixed physical scale; IR proves that H_eff gives the seed. Proposition T1 applied to the whole proof says the proof must fail for 2I at large bare beta. It already fails at UV if UV uses continuous fluctuations, as Balaban's small-field expansion around flat connections does; no 2I measure then produces H_eff. So IR need not fail for 2I unless 2I measures at their own order-one couplings satisfy H_eff, and there 2I is a positive control by F6. In the lane's present architecture (rows 23, 46) the seed tool acts on the bare measure at bare beta tending to infinity, and there 2I binds. The flux-half work of rows 778-833 acts at fixed bare couplings in (0, 1/2], where 2I-blindness is no defect.

**Results against the registered readings.**

- Reading 1: if F3 holds for Q_8, Route A of row 804 is refuted (GUIDE) on any interval above 1.15, which is earlier than the 5.7 that 2I gives. **Holds.** The discard stands, on a stronger and different reason.
- Reading 2: if only 2I is perfect (F4), contraction plus full flattening passes every finite-group test below 5.7. **Holds.** The guide "a use of SU(2) beyond contraction and flattening" (CF:568) binds only above 5.7. But the mechanism dies by constants at order one: its minorization constant is delta = exp(-24 beta_+) (READ CF:510-513), so each block of four commutators contracts the odd part by 1 - delta^4/2, and at beta = 2 that is 1 - e^(-192)/2 (PROVED arithmetic). It needs a typical-environment minorization, in the spirit of row 820, before it can be tried.
- Reading 3: if F5 holds, the lane's Dobrushin-type R1 results see SU(2) beyond Q_8. **Holds.**

**What it buys.** A corrected profile for every order-one tool. The degree-12 search is unneeded below about 5.7. The surface bounds of rows 817-830 are not refuted by any binding group at their couplings; they are Q_8- and 2T-selective through the moments 1/8 (row 823, against 1/4 for Q_8) and 5/64 (row 817, against 3/32 for 2T). **What it does not buy:** any estimate at order one. It changes what an order-one tool must see, not whether one exists.

### 3.2 Idea 2 (rank 2). (E17) is not a continuum consumer; a physical-scale witness from the account makes the flux consumer cutoff-uniform

**Changed assumptions.** Rows 42, 43, 50 (the fusion consumer and its microscopic witness) and row 25 (the account's short-distance law is unused).

**(a) (E17) fails on a fixed physical torus (PROVED arithmetic; one ARGUED premise).** Since 0 < r <= 1, r^4/(4 + 16 r^4) <= 1/20, so eta(beta) <= e^(-80 beta)/20. Along SA's sequence beta_j/log(1/a_j) tends to 11 N^2/(12 pi^2) = 0.3715 for N = 2 (READ MB:32). On a torus of fixed physical side L, n_j = L/a_j, so

```math
\eta(\beta_j)^{n_j/2}\;\le\;\exp\!\big(-14.86\,(1+o(1))\,\tfrac{L}{a_j}\log\tfrac{1}{a_j}\big).
```

Also inf_j eta(beta_j) = 0, so (E17) "on a compact interval I" does not apply to the sequence at all. ARGUED: the deficit Q_F on a torus of fixed physical size tends to a positive continuum value (a ratio of continuum twisted partition functions, each positive). If so, (E17) fails along the sequence at every fixed L: it asks for Q_F to fall faster than any fixed exponential of L/a. I have no rigorous lower bound on Q_F at large beta: Kanazawa's inequality gives Q_F >= (W(C)/2)^(L_mu L_nu / A_C), but no lower bound on large Wilson loops at weak coupling is in the read set.

*Consequence.* (E17), and the statements "(RTAIL) is equivalent in strength to (E17)" (rows 817, 823) and the target of row 833, are statements on fixed coupling intervals: R1 statements. That is consistent with row 765, whose scope paragraph already says the witness "measures one microscopic time step" and that a physical-scale witness is needed (READ FU:559-572). What is new here is the exact failure rate at fixed physical size and the construction below.

**(b) Lemma W (PROVED).** Let B be a periodic spatial box with transfer operator T (TM), top eigenvalue lambda_0, ground state Omega, and P_ev the projection on the functions fixed by all centre flips. Let F be a real, gauge-invariant, centre-blind function of the links in a time slab of w steps, symmetric under the reflection of the slab, and K_F its slab operator (the slab kernel with F inserted; K_1 = T^w; K_F is self-adjoint by the reflection symmetry). Put c = <Omega, lambda_0^(-w) K_F Omega>, psi = lambda_0^(-w) K_F Omega - c Omega, and

```math
G(u)=\langle\psi,(T/\lambda_0)^u\psi\rangle,\qquad u=0,1,2,\dots
```

Then: (i) G(u) is the connected ground-state correlation of F with its translate by u + w steps on the cylinder over B; (ii) G is log-convex; (iii) for integers 0 <= u_1 < u_2 with G(u_1) > 0 and every a >= u_2 - u_1,

```math
S_{\rm ev}(a;B)\;\ge\;\frac{G(u_1+a)}{G(u_1)}\;\ge\;\Big(\frac{G(u_2)}{G(u_1)}\Big)^{a/(u_2-u_1)} .
```

*Proof.* (i) In the infinite-time cylinder the product of F at slab 0 and F at slab u + w has mean <K_F Omega, T^u K_F Omega>/lambda_0^(2w+u), using K_F self-adjoint, and F has mean c. Expand lambda_0^(-w) K_F Omega = psi + c Omega and use (T/lambda_0)^u Omega = Omega and psi orthogonal to Omega; the cross terms vanish. (ii) F is centre-blind, so K_F commutes with the flips and psi is even; psi is orthogonal to Omega. In an eigenbasis, G(u) = sum over even j >= 1 of mu_j^u abs(<e_j, psi>)^2 with mu_j = lambda_j/lambda_0 in (0, 1): a positive combination of exponentials, hence log-convex. (iii) Let phi = (T/lambda_0)^(u_1/2) psi divided by its norm (T is positive, so the square root exists). Then phi is a unit even vector orthogonal to Omega and <phi, (T/lambda_0)^a phi> = G(u_1 + a)/G(u_1). This is sum_j abs(c_j)^2 mu_j^a <= max_j mu_j^a <= S_ev(a; B). For the second inequality, the slopes of the convex function log G increase, so log G(x) >= log G(u_2) + (x - u_2)(log G(u_2) - log G(u_1))/(u_2 - u_1) for x >= u_2; take x = u_1 + a. QED

The same lines give an upper bound on the even gap of B: m_ev(B) <= log(G(u_1)/G(u_2))/(u_2 - u_1). That is of the known type (SK:66).

**(c) Proposition W-phys (PROVED GIVEN (SD-cyl)).** *(SD-cyl), OPEN interface input:* SA's short-distance law, Theorem 0 (c)(3) (READ PS:78), holds for the connected ground-state correlations on the cylinders over the consumer boxes (a, c, d), c, d in {a, 2a}: for a bump f and physical separations s in [d, 2d] inside (0, d_0], the correlation of O(f) and its translate by s is zeta^2 (3(N^2 - 1)/pi^4) g^4 K_free (1 + epsilon) with abs(epsilon) <= epsilon_0 < 1. SA state this on their allowed tori, four equal sides; the cylinder form is a port, not in the account.

Given (SD-cyl), take F = O(f) with the bump's time thickness at most d/2, u_1 + w and u_2 + w the lattice versions of d and 2d. The ratio G(u_2)/G(u_1) is at least rho_* := ((1 - epsilon_0)/(1 + epsilon_0)) kappa_free gamma, where kappa_free = K_free(f, tau_(2d) f)/K_free(f, tau_d f) > 0 and gamma is the ratio of the two coupling factors. None depends on the cutoff. Lemma W gives, for every consumer box of physical time extent A,

```math
S_{\rm ev}(a;B)\;\ge\;\rho_*^{\,A/d}\qquad\text{uniformly in the cutoff.}
```

**(d) Corollary (a cutoff-uniform flux consumer; PROVED GIVEN (SD-cyl) and the fusion chain of rows 765-778).** On the consumer tori of physical time extent A, (FQ) holds with K bounded if

```math
\textbf{(E17-phys)}\qquad Q_F\;\le\;\tfrac{K}{8}\,\rho_*^{\,A/(2d)},\qquad Q_F<1/192 .
```

The rate log(1/rho_*)/(2d) is a physical constant. So the flux half of (PHYS-SEED) becomes one inequality with a cutoff-independent rate at one physical size. GUIDE: with an area law Q_F of order e^(-sigma A^2), (E17-phys) holds once A is above about log(1/rho_*)/(2 sigma d). With sqrt(sigma) xi about 0.28 (PS 1.4) and log(1/rho_*) about 6 for the free 1/x^8 law, that is about 34 xi^2/d: a fixed physical size, large because d <= d_0 sits at the reference scale. The glue half (S_ev small at that size) is unchanged and OPEN.

**What it buys.** It removes the beta-dependence that makes (E17) useless on the continuum path, and it uses the account at a second place, beside (UV-Z). It turns row 765's request for "a lower thermal witness on the matched physical scale" into one named port, (SD-cyl). **What it does not buy:** the flux deficit at the physical scale. That is still confinement at a scale beyond xi.

**Why not a torus version.** On the consumer torus itself the connected correlation is also log-convex in the separation. But the trace bound then needs the excited-to-excited matrix elements of the slab operator, which are controlled only by a trace at a short time extent, a high-temperature quantity. The cylinder form avoids this. It costs the port.

### 3.3 Idea 3 (rank 3). The hand-off architecture: what a landing zone for the R1 results must satisfy

**Changed assumptions.** Rows 23, 49, 81: the infrared engine acts on the fine lattice, R1 is off the path, and the R1 theorems are exact-Wilson theorems. The alternative architecture: the ultraviolet chain carries the bare measure to an effective measure on a block lattice; an R1-type theorem for that effective measure gives decay at the block scale; reflection positivity on the fine lattice turns decay into the gap (decay of <theta F, T^t F> on a dense set excludes spectrum below the rate). In this architecture R1 work is on the path, as the landing zone.

**First statement (ROB).** An R1 theorem can serve as a landing zone only if it holds for every gauge-invariant measure on the block lattice within a fixed distance of a Wilson measure, in a norm the renormalization group controls. Which lane R1 results satisfy (ROB)?

**Attempt (ARGUED; standard tools).**
- *Dobrushin-type results* (the seed below 2/9, row 790; the Langevin gap below 1/4, row 818; the area law below 2/3, row 825). Their hypotheses are one-link influence sums below 1. Influence sums are continuous in the specification: perturbing each one-link log-density by at most epsilon in sup norm multiplies each covariance bound by at most e^(2 epsilon) (Holley-Stroock), and short-range effective terms add influences of order epsilon. So these hypotheses are open conditions, and the thresholds move continuously (for example beta < (2/9) e^(-2 epsilon) - O(epsilon)). They satisfy (ROB) with degraded constants. Lemma F5 shows the degradation is real: the sharp quarter of Theorem V is a property of the exact von Mises-Fisher law, and a change of the one-link law can double it.
- *Surface-class results* (rows 811-830). They use the single-plaquette Z_2 grading (J2) and exact Haar moments. Every renormalization step creates multi-plaquette terms, which break the closed-surface structure. They do not satisfy (ROB) as stated.
- *The infrared engine* (Theorems S, SH, R, EV-L) needs (TM) and reflection positivity for the measure it acts on, and blocking maps are not shown to keep reflection positivity (row 23). In this architecture it is not used; decay at the block scale replaces the seed.

**Result.** A landing zone exists in principle for the Dobrushin-type results, not for the surface classes. The price is the hand-off itself: the ultraviolet chain must reach an effective coupling inside the landing zone, below about 2/3. That is EXIT, the crux (PS:422). GUIDE: at one loop each doubling lowers the effective beta by about 0.26 (FP:92), so from 2.3 to 2/9 is about eight doublings, and fewer if the flow speeds up at strong coupling. So EXIT is the control of a handful of renormalization steps at order-one coupling. This prices the R1 work. It does not bypass the order-one regime: it says where R1 results would plug in if EXIT were proved.

**What it buys.** A rule for R1 lanes: state each R1 theorem for an influence-defined class, not for the exact Wilson weight, so that it can serve as a landing zone. Surface-class work then needs a separate argument that its hypotheses survive multi-plaquette terms.

### 3.4 Idea 4 (rank 5). Theorem S1: a weak-coupling four-dimensional gap on the twisted thin torus, unqueued since SK 13.5

**Changed assumption.** Rows 111 and 113 (process): parallel lanes go to strong-coupling ranges. S1 (T2 in plain-Wilson form, SK:83, SK:180) is "a mass gap for a four-dimensional SU(2) lattice theory at weak coupling with two infinite directions"; run 1 judged it "looks provable now"; its chart (CH) is proved and checked (rows 679, 695). SK:342 says S1 "is still a target of its own", and SK:343 left it unqueued "until T2 is stated again", but that restatement concerns the class of T1, which S1 does not use.

**First statement (S1; READ SK:83).** For each n >= 2 there are beta_0(n), eps_0(n) and c > 0 such that, for beta >= beta_0(n), on (Z/n)^2 x (Z/M)^2 with the twist P_0, gauge-invariant F, G in [-1, 1] supported over base sets X, Y obey abs(Cov(F, G)) <= C(n, beta) size(X) size(Y) exp(-(c/n) dist(X, Y)), uniformly in M.

**Skeleton (ARGUED, not proved).** (i) Small fields: if every plaquette defect is at most delta_0(n), (CH)(a)-(b) give a chart U^h = V e^X with transverse X and A^tw >= (mu_n/16) sum abs(X)^2, mu_n = (2 sin(pi/2n))^2. That is a Gaussian region with a transverse mass of order 1/n. (ii) Large fields: a plaquette with defect above delta_0(n) costs at least beta delta_0(n) in the action, so large-field regions carry e^(-beta delta_0(n)) per plaquette, summable once beta_0(n) is a large power of n. (iii) A two-dimensional cluster expansion in the base, with the locality (CH)(c), whose decay e^(-r/(3n)) gives the rate c/n. (iv) The centre ambiguity of the chart is the stabilizer +-1, fixed by the twist. The hard step, named in SK:310: charts over base regions with holes (the class in H^1(D; Z_2)), and the bad-region estimate.

**What it buys.** A non-perturbative weak-coupling theorem in four dimensions, of a different kind from every R1 result; a base for T4; a test of weak-coupling methods in the lane. **What it does not buy:** (AC') or the crux. Whether to queue it is the owner's decision; it is named here because the prioritization rests on row 111 ("hardest first") while the lanes of rows 833-836 already work off the crux.

### 3.5 Idea 5 (rank 6). Cross-provider checks of the infrared engine, and (TM-tw) as a lemma

**Changed assumptions.** Rows 32, 37, 58, 106-108. The statements on the path of every seed form whose only check is by the author's provider (author Claude Fable 5.2, checker Claude Opus 5.5): Theorem SH (row 707), the limit theorem and its Part B (rows 700, 703), Theorem DOB (row 709), the strong-coupling seed (row 704), Theorem U (row 715). (TM-tw), used by Theorem R, the full and kappa seeds and the fusion consumer (EV-L uses electric twists only, FX:218), is spread over two check files (FX:660 proposed a lemma; never queued).

**First test.** One Codex gpt-6-astra check of Theorem SH and of the limit theorem with Part B, and one author run writing (TM-tw) as its own lemma, followed by a check by the other provider. **Cost:** three lanes. **Buys:** independence for the infrared engine before any outward use. The rows 698/699 disagreement on Corollary S3 is the precedent: the second provider found the false step that the first check passed.

### 3.6 A note on Z^k <= Z^0 (row 61)

Row 822 calls "0 < Z^(m+v) <= Z^m" a READ fact. VO:93-96 derives it from (TM-tw) and (S2). Written out (PROVED, unchecked, given (TM-tw)): pick a time direction mu and split a twist k into its planes not containing mu (magnetic, k_mag) and containing mu (electric, carried by flips C^(e)). Then Z^k = Tr(T_(k_mag)^(n_mu) C^(e)) <= Tr(T_(k_mag)^(n_mu)) = Z^(k_mag), because the flips are commuting involutions that commute with the positive T_(k_mag). Repeat with a time direction inside a plane of k_mag: at most three frame changes reach Z^0. For the consumer's pairs (m a spatial twist in frame r, v = v_(ri)) one step gives Z^(m+v) <= Z^m. So the fact is exactly as strong as (TM-tw), which supports idea 5.

### 3.7 Past discards that rest on an assumption I now doubt

| Discard or label | Where | The doubted row | Re-judgement |
|---|---|---|---|
| Route A (pair-Casimir filters) set aside as "shared" by 2I; the search moved to the spin-6 filter (G15) | TR:106; FIN:880 (804) | 84, 95 | The discard stands for a stronger reason: Q_8 shares the filters (F3) and binds above about 1.15 (GUIDE). The move to spin 6 rested on 2I binding; below about 5.7 a spin-2 or spin-3 filter is what a binding group asks for (F6). |
| "Contraction and density flattening do not separate SU(2) from finite subgroups"; next step "a use of SU(2) beyond" them | CF:428-525, CF:568-571; FIN:859 (783); FIN:876 (800, (K25)) | 84, 95 | Contraction alone is refuted (GUIDE) above 1.15 by Q_8 (F2). Contraction with full flattening is shared only by 2I (F4), so no binding group refutes it below about 5.7. It dies instead by constants (delta = e^(-24 beta)) and needs a typical-environment minorization. |
| "Group-blind for the binary icosahedral group" recorded as a limit of the surface bounds | FIN:893, 899, 903, 906 (817, 823, 827, 830) | 84 | Not a limit at their couplings, and the bounds use moments (1/8, 5/64) that Q_8 and 2T do not share. |
| (E17) treated as the order-one target; "(RTAIL) is equivalent to (E17)" | EX:577-593; FIN:893, 899, 909 (817, 823, 833) | 43, 50 | An R1 statement on a fixed interval; it fails on a fixed physical torus (3.2 (a)). The continuum consumer is (E17-phys) with a physical witness (3.2 (d)). |
| S1 not queued | SK:342-343 | 111, 113 | It does not need T1's class; it is unqueued by priority, not by a block (3.4). |
| The test-range list (0.44, 1.01, 1.6) | FP:278-285; FIN:860 (784) | 90 | Missing the finite-subgroup ladder; with it the binding profile at the crossover is Z_2, U(1), Q_8, K7 and, above 2.15, 2T (3.1). |

**Not doubted:** Route Z's Proposition B (SK:278); the scoped transport obstructions (rows 793, 796); the failure of group-blind (TU) (row 786); the full-L^2 block certificate (row 758); Theorem O for fixed-radius loop certificates (row 760); the falsity of (EP) (row 754); the failure of linear (ES-1) (rows 748, 751). Each rests on a proof inside its stated class, and none uses a row I doubt.

### 3.8 Idea 6 (rank 4). A roughening ceiling for absolute surface expansions (GUIDE; not tested here)

**Changed assumption.** Rows 45, 65, 81: the rooted absolute bound (J12), or (RTAIL-SOS), can be pushed toward order one by better surface counting (rows 817-833).

**Reading (GUIDE).** The strong-coupling expansion of the four-dimensional SU(2) string tension meets a roughening point, most often estimated near beta_R = 1.9 (a statement found by a web search in the abstract-level text of arXiv:0907.4102; the 1980 series papers it rests on were not read). The roughening point is not a phase transition of the theory; it is where expansions around a flat sheet stop converging. Beyond it, absolute expansions around flat sheets cannot converge, and the absolute surface gas sum Sigma abs(D(S)) has its own critical point, which can lie lower. So the surface program has a method ceiling near or below beta_R, below the crossover. Past it, a rough-phase method is needed: a dual Coulomb-gas treatment of the surface, as in Frohlich and Spencer's roughening work (recalled).

**First test (named, not run).** (i) A reading item: the source and the variable of the beta_R estimate, and whether the series coefficients are positive. (ii) A hand lower bound on Sigma abs(D(S)) over an explicit family (flat sheets with independent multilevel terraces) exceeding 1 per unit area at some beta below 2. That would refute the absolute (J12) at that beta for every ordering that puts the flat sheet first. Row 816's (J13) is the kind of input needed. **Buys:** a stop condition for surface lanes before they spend effort past the ceiling.

### 3.9 The ranked list

Rank by what the idea changes, divided by what it costs to find out. None of them reaches the order-one regime with a proof.

| Rank | Idea (section) | Changed assumption (rows) | State after this file | Next step and cost |
|---|---|---|---|---|
| 1 | The finite-subgroup ladder: 2I does not bind at order one; Q_8 (about 1.15) and 2T (about 2.15) do, and they are separated from SU(2) at spin 2 and 3 (3.1) | 84, 85, 94, 95 | F1-F5 PROVED; the couplings READ (GUIDE); F6 ARGUED; three verdicts re-judged (3.7) | A cross-provider check of F1-F5 (one short lane); re-brief order-one flux-half lanes with the profile of F6 |
| 2 | (E17) cannot hold on a fixed physical torus; Lemma W turns the account's short-distance law into a cutoff-uniform witness and the flux consumer into (E17-phys) (3.2) | 25, 42, 43, 50 | The failure rate PROVED (one ARGUED premise); Lemma W PROVED; W-phys PROVED GIVEN (SD-cyl) | A port item: (SD-cyl), SA's Theorem 0 (c)(3) on cylinders over the consumer boxes |
| 3 | The hand-off architecture: R1 theorems are on the path only as a landing zone, and only Dobrushin-type ones survive perturbation (3.3) | 23, 49, 81 | ARGUED with standard tools; EXIT priced as a handful of renormalization steps at order one (GUIDE) | State each new R1 theorem for an influence-defined class |
| 4 | A roughening ceiling for absolute surface expansions near beta_R of about 1.9 (3.8) | 45, 65, 81 | GUIDE; not tested | A reading item on beta_R; a hand lower bound on the absolute surface sum |
| 5 | Theorem S1, a weak-coupling gap on the twisted thin torus, unqueued (3.4) | 111, 113 | Skeleton ARGUED; the chart (CH) already checked | Owner decision; one author lane on the bad-region estimate |
| 6 | Cross-provider checks of the infrared engine and (TM-tw) as a lemma (3.5, 3.6) | 32, 37, 58, 61, 106-108 | Named; the frame proof of Z^k <= Z^0 written (PROVED given (TM-tw)) | Three lanes |

**Past discards that rest on an assumption I now doubt** (detail in 3.7). Row 804's move from the pair-Casimir filters to a spin-6 filter rested on 2I binding at order one. The discard stands, but Q_8 is the reason, and a spin-2 or spin-3 filter is what a binding group asks for. Rows 783 and 800 set aside contraction with full flattening because 2I shares it; below about 5.7 no binding group shares it, and it fails instead by its constant e^(-24 beta). The surface rows 817-830 record a 2I-blindness that is no limit at their couplings. Rows 809-833 treat (E17) as the order-one target, but it is an R1 target. SK 13.5 left S1 unqueued for a reason that S1 does not depend on.

---

## Report (plain words)

**The wall.** The proof needs one box, about twenty particle wavelengths wide, to be quiet, and it needs this uniformly as the lattice spacing goes to zero. The account of Sussman and Alpoge controls only far smaller boxes. In between, the coupling is of order one, and no known tool reaches it. This exercise did not change that.

**What the exercise found.**
1. The lane tested order-one tools against the 120-element subgroup of SU(2). Published simulations put its freezing near beta = 5.7, so in the order-one range it behaves like SU(2) and refutes nothing. The groups that freeze inside that range are Q_8 (near 1.15) and the 24-element group (near 2.15). They differ from SU(2) already in the fourth and sixth moments, and in their commutator subgroups (proved here). Three earlier choices rested on the wrong group (3.7).
2. The sufficient target (E17), used by the recent surface lanes, asks for decay faster than any fixed physical rate on a box of fixed physical size. So it cannot be the continuum target. A short lemma (Lemma W, proved) turns the account's short-distance law into a lower bound for the even thermal sum with a cutoff-independent rate, if that law is ported to cylinders. The flux half then becomes one inequality with a physical rate, (E17-phys).
3. The strong-coupling results reach the continuum only as the landing zone of a renormalization-group hand-off. For that they must hold for classes of actions. The Dobrushin-type results do; the surface-class results, as stated, do not.
4. Tests run: the hand calculations of 3.1 and a GUIDE script that checked them (all agree); the arithmetic of 3.2. No test refuted a registered reading.

**What not to do next.** Do not search for spin-6 mechanisms for order-one couplings. Do not call (E17) or (RTAIL) the order-one crux. Do not count a larger proved coupling range as progress on (GAP) unless it is stated for a class that a hand-off could reach.

**The exact price** is unchanged: (PHYS-SEED), equivalently (ES) at one physical size uniformly in the cutoff. Its flux half now has the cutoff-uniform form (E17-phys), given the port (SD-cyl). Its glue half is untouched.

RESULT: no mass gap is proved and no route through the order-one regime was found; top ideas: (1) the binary icosahedral test does not bind at order one (freezing near beta 5.7, GUIDE) while Q_8 (about 1.15) and the binary tetrahedral group (about 2.15) do, separated from SU(2) at spin 2 and 3 (moments, filters and commutator subgroups PROVED), which re-judges rows 783, 800 and 804; (2) (E17) cannot hold on a fixed physical torus, and Lemma W (PROVED) gives a cutoff-uniform even-sum witness from the account's short-distance law, making the flux consumer (E17-phys) cutoff-uniform given the port (SD-cyl); (3) R1 results serve the continuum only as a hand-off landing zone, which Dobrushin-type results satisfy and surface-class results do not; then a roughening ceiling near beta 1.9 for absolute surface expansions (GUIDE), the unqueued weak-coupling theorem S1, and cross-provider checks of the infrared engine with (TM-tw) as a lemma.
