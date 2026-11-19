# Information-minimisation law: what it is and what it explains (info-min-law, 2026-10-22)

Runner: `runner.py`, output in `out.txt`: 14 PASS / 0 FAIL, 9 s, 84 MB. Working-rule exploration with zero premise weight. Axioms unchanged.

## 1. Candidate laws

| # | Statement | Well-defined? | Verdict |
|---|---|---|---|
| L1 | Reality is the shortest record history consistent with local admissibility (Kolmogorov) | No: uncomputable, not local, and the minimum is the empty history | Rejected |
| L2 | The update minimises the information written per tick | Yes, but its minimum writes no records, which contradicts "Records form" | Rejected as the primary law |
| L3 | The state minimises description length given the records (MaxEnt) | For a state only, no dynamics; on main (PRR/Jaynes note) | Corollary |
| L4 | Minimum Fisher information (Frieden EPI) | Needs a supplied J per field: ad hoc | Rejected; one use survives (Born) |
| **IM** | **Least-surprise history.** Each half-tick, the transition from the actual configuration minimises relative entropy (KL) to a reference process supported on the half-tick's nonzero elements, where each change of occupation, link unit or edge unit costs surprise 1/eps, in the limit eps -> 0, with the odds held as the marginals | **Yes**: local, label-free, computable (it is the Schrodinger-bridge / entropic optimal-transport problem) | **Chosen** |

**Theorem (IM = CL-2 transport).** min KL(pi || R_eps) at fixed marginals equals min [E_pi(changes)/eps − H(pi)] + const. As eps -> 0, the minimiser converges to the plan with the fewest changes, and among those the greatest entropy (Cominetti–San Martín 1994, exponential-penalty LP limit). The plan is unique because H is strictly concave. With both marginals fixed, H(pi) = H(X) + H(Y) − I(X;Y). So "greatest entropy" is exactly **least mutual information between before and after**: the law commits to no more correlation than fewest-changes forces. CL-2's two clauses therefore merge into one principle: *the history carries the least information beyond what the odds force*. A1: on 6 random tick supports the eps = 0.003 Sinkhorn plan hits the LP minimum and matches an independent max-entropy solve (1e-4, solver tolerance); A2 checks the identity.

IM restates CL-2, so it predicts nothing new by itself; its value is a single objective to test elsewhere.

## 2. Implications, domain by domain

**Born rule.** This is the decisive positive result.
- (a) Under IM, a transport of finite information exists only if every block of the half-tick conserves its total odds. Any off-support move has infinite surprise.
- For a phase-blind local weighting f(|a|), block conservation under a non-monomial unitary mixing gives Jensen's equation G(S) + G(2s − S) = 2G(s), so f = c|a|^2. This rederives the born-reading theorem in IM language.
- B1 (1D walk, 60 ticks): forced off-support mass per tick 8e-2, 4e-2, **1e-16**, 4e-2, 8e-2, 0.17 for p = 1, 1.5, **2**, 2.5, 3, 4.
- **Born is the unique weighting for which the least-information history exists at all.**
- (b) Independent route (Wootters 1981). Fisher information of record odds about a rotation angle:
  - It is the same at every state only for p = 2, with value 4 (C1).
  - The constant-Fisher solutions are cos^2(c·theta) with c odd. Their information is 4c^2, which is least at c = 1. Every c >= 3 also gives zero odds to a supported superposition, which violates the Admissibility support reading (C2).
  - For 3 outcomes, Born odds make the Fisher metric equal to 4 times the round metric on amplitudes (C3).
- Status: **derived, conditional** on H1–H4 (unitary block mixing, a local phase-blind f, a non-monomial mixer), or on state-uniform distinguishability.

**Unitarity.** CL-2 already has "records never condition the odds". If the half-tick neither creates nor destroys distinguishability (Born-Fisher metric preserved), Wigner's theorem makes it unitary or antiunitary. **Derived, conditional** on lossless odds, which is CL-2 content and not IM. The antiunitary option is open for a discrete tick; its square is unitary.

**Why qubits.**
- Least information per site alone selects a **classical bit** (a rebit is also cheaper than a qubit), so info-min alone is wrong here.
- Adding continuous reversible transitions, local tomography and pairwise interaction gives the 1-bit system with Bloch dimension 3, M_2(C) (Masanes–Müller–Augusiak–Pérez-García PNAS 2013; Dakic–Brukner 2009). Real/quaternionic fail parameter multiplicativity (D2); real QM is excluded by experiment (Renou et al. 2021).
- Status: **plausible/derived-by-literature**. "At most 1 bit per site" is the info-min content; continuity and tomography are inserted.

**Why 3 dimensions.**
- D1: M_2(C) holds at most 3 mutually anticommuting generators, because they are trace-orthogonal in the 3-dimensional traceless space. So a one-qubit site whose possibility rotations are the spatial rotations (Müller–Masanes, NJP 2013) gives **d = 3 exactly**. The axioms' Cl(3,0) presentation already writes this identification in.
- The identification "spatial rotations = Bloch rotations" is **inserted**, a bridge. The CL-1 staggered/cube hop spreads the Clifford algebra over the 2^d cube, which works in any d, so the framework does not itself enforce d <= 3.
- Cross-checks (not info-min): Polya transience first at d = 3 (return 0.3405; F1; weak, quantum walks are transient at d = 2, Štefaňák–Jex–Kiss 2008); graviton polarisations (d + 1)(d − 2)/2 = 0, 2 at d = 2, 3 (F2); Ehrenfest: no stable atoms at d >= 4.
- Status: **plausible** (two-sided bracket). Info-min alone favours d = 1 (E2: log2(2d) bits per neighbour address).

**Why a cubic 6-NN neighbourhood.**
- Theorem (E1): every translation-transitive graph on a rank-3 lattice needs a symmetric generating set.
  - Z^3 is torsion-free, so the set has even size, and rank 3 forces at least 3 independent pairs, i.e. at least 6 elements.
  - With exactly 6, the 3 representatives generate Z^3 iff they form a basis. A surjection Z^3 -> Z^3 is an isomorphism (Hopfian).
  - So the graph is isomorphic to simple cubic 6-NN, and its stabiliser (order 48) is transitive on the neighbours. Isotropy comes free.
- In {-2..2}^3: no size-4 spanning set; 2821 of 37820 size-6 sets generate, all bases.
- **Derived**: given translation-transitivity ("no site is privileged", one site per cell) and d = 3, least neighbour information selects Z^3 with 6-NN uniquely.
- Caveats: non-Bravais nets (diamond 4, srs 3) have lower degree but privilege sublattices. D'Ariano–Perinotti (PRA 2014): a unitary isotropic 2-dim-cell QCA in 3D needs a larger generating set (reported BCC; **to verify**); CL-1 escapes via the 2x2x2 partitioned tick, so the minimal graph is the admissibility graph, not the update support.

**Records and the arrow.**
- With Record, IM accounting makes each record carry, on average, exactly its outcome's entropy. This is the register's lossless-accounting theorem (CANDIDATE_LAWS_v3 line 145), so records are an optimal (Shannon) code of the history.
- CL-2's exclusion of bound sites reads as "write no bit already fixed by a constraint", the minimal-write side of L2.
- The arrow is record accumulation, which is monotone because records are permanent.
- Status: **plausible reading**; that records form is **inserted** (Record).

**Gauge redundancy.**
- Minimal description length removes redundancy; gauge redundancy is the price of a **local** description of a Gauss-law constraint (invariant data are nonlocal loops). Reading: gauge = least redundancy keeping the rule nearest-neighbour. Not derived; groups and register sizes stay **inserted/fitted**.
- Status: **missing** (the group).

**Gravity.**
- Jacobson (1995): delta Q = T dS with S = eta·A on every local Rindler horizon gives the Einstein equation, G = 1/(4 eta).
- Reading: the vacuum entanglement area law supplies eta, so G = 1/(4 eta) in cell units would replace "G FITTED" with a computation (cf. agents/induced-G).
- Needs Unruh temperature (approximate local boost invariance) and controls eta's species/UV dependence.
- Status: **plausible**. The coefficient calculation is the open, testable step.

**Fewest-changes transport.** Already CL-2. IM unifies its two clauses into one objective, and it is the ε→0 Schrödinger bridge. **Derived (identity).**

**Lambda.**
- Hubble-cutoff holographic dark energy gives w ≈ 0 (Hsu 2004): excluded.
- The info-min form that works in magnitude is Sorkin's: Lambda is conjugate to 4-volume (unimodular, as in CL-3's "constant per proper 4-volume"), and the 4-volume is a **count of records** with Poisson noise, so Lambda ~ N^{-1/2}.
- G1: 1/sqrt(Hubble 4-volume in Planck cells) = 1.4e-122, against observed Lambda·l_p^2 = 2.9e-122. That is a factor of 2, with an O(1) prefactor not derived and the Planck-size cell **assumed**.
- CL-2's record count is random (bound sites unrecorded), so the mechanism has a home. It predicts a **fluctuating Lambda, w != -1**: against the register's w = −1, toward DESI DR2.
- Status: **estimate/speculation**, and the most interesting new lead.

**Walls (chirality, families, masses).**
- Info-min prefers Weyl (2 components) to Dirac (4), so it *wants* chirality; the wall is Nielsen–Ninomiya (locality), not information. "3 families = 3 Bloch directions" is numerology without a mechanism. Masses: nothing.
- Status: **missing**.

## 3. Severe scorecard

| Item | Status | Check |
|---|---|---|
| CL-2 transport = one information principle (IM) | **Derived** (identity + LP-limit theorem) | A1, A2 |
| Born rule | **Derived, conditional** (block unitary, local phase-blind f, non-monomial mixer; or uniform distinguishability) | B1, B2, C1–C3 |
| Unitarity | Derived conditional on lossless odds (Wigner) | — |
| 6-NN simple cubic, given d = 3 and translation-transitivity | **Derived** | E1 |
| Qubit (complex, 2-dim) | Plausible; continuity, tomography and interaction are inserted | D1, D2, literature |
| d = 3 | Plausible; the Bloch = space identification is inserted, and info-min alone gives d = 1 | D1, E2, F1, F2 |
| Records form / arrow | Inserted; optimal-code reading plausible | register |
| Gauge redundancy | Missing (group); locality reading only | — |
| Gravity (Einstein eq.) | Plausible via Jacobson; G from the area-law coefficient not computed | — |
| Lambda size | Estimate within a factor of 2 (Sorkin count noise; cell size assumed); predicts w != -1 | G1 |
| Chirality / families / masses | Missing | — |

**Does it explain everything?** No. It explains the *form* of the probabilistic core: Born, the transport, unitarity given lossless odds, and the neighbour graph given d. That is real unification: three CL-2-level choices become one objective. It does not explain why there is something to record, d, the gauge groups, chirality, families or masses. Minimisation needs a constraint to be nontrivial. Every derivation above has a "something must happen" input (records form, continuity, interaction) that info-min does not supply.

## 4. Anti-smuggling gate (rule IM)

1. **No measured number chosen.** Pass. eps -> 0 is a limit, not a value.
2. **No observed structure by name.** Pass. IM constrains only transitions, changes and odds.
3. **Prediction it was not built for.** Born uniqueness counts as a derivation, not a new prediction. The Lambda-as-count-noise extension predicts a fluctuating Lambda with w != −1 and |Lambda| ~ H^2. That extension is a **separate, UNTESTED rule** and conflicts with CL-3 as written.
4. **Axiom bent.** None (IM restates CL-2). The Lambda extension would bend nothing either, but it replaces CL-3's "supplied constant".

Forced: Born (given H1–H4), transport uniqueness, 6-NN (given d, transitivity). Supplied: d = 3 (Bloch = space bridge), records forming, continuity, gauge content, Lambda prefactor and cell size.

## 5. Next decisive steps

1. Area-law coefficient eta of the CL-1 sea per face, giving G/a^2 = 1/(4 eta) unfitted (Jacobson).
2. Variance of the CL-2 record count per 4-volume, giving Lambda(t) to test against DESI DR2.
3. Verify the D'Ariano–Perinotti lattice result against the CL-1 cube tick.
