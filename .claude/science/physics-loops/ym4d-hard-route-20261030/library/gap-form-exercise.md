lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-12T09:53Z

# gap-form-exercise: is "base, one-way step, sufficiency" needed for (G_ev), or a habit?

Queue row 735 of `FINISH.md`. Second run of the exercise skill v2 (skill text
fetched from the URL of the row at revision `1eb15ac428`, read in full).

**Header.**

- Written by: Anthropic, Claude Fable 5.2, effort high, one Mac mini worker
  session, as AUTHOR. No subagents.
- Commit: `196d4707b` on `claude/ym4d-hard-route`. Date: 2026-11-11 (UTC).
- **Nothing in this file is checked by another model.**
- Refresher read: this target's `GOAL.md` contract reads no framework axiom, so
  the skill's refresher list is replaced by `GOAL.md` (read in full) and the
  `FINISH.md` sections "How we work", "Working efficiently" and "Rules" (read
  in full). This replacement is the one the skill allows for a standalone
  proof target.
- **What this run did not cover** (kept true):
  - No check by another model. No blind check of the plain version, and no independent kill pass (no subagents allowed; the passes of Step 7 are one session).
  - **No proved case was read in full.** Read in part, with pages in 2.A: Gopfert and Mack (preprint pages 1 to 10 of 51 sheets; the proofs not read); Piazza and Shen (pages 1 to 5, parts of 8, 9); Forsstrom (pages 1 to 4); Adhikari and Cao (pages 1 to 6); Gosset and Mozgunov (pages 1 to 3); Nachtergaele (abstract, pages 10, 11); Martinelli's lectures (pages 9 to 11, 43, 44, from a crude text of the PostScript); Duminil-Copin and Tassion (pages 2, 9, 10); Kopper (pages 1 to 4); Ito and Seiler 0711.4930 (pages 1 to 8); Chatterjee 2602.00436 (pages 1 to 6). Abstract only: Shen, Zhu and Zhu; Tomboulis; Ito and Seiler 0803.3019.
  - **Recalled, not read:** Osterwalder and Seiler; Knabe's own paper (read as quoted); Stroock and Zegarlinski; Martinelli and Olivieri (read through Martinelli's lectures); Ito's and Muller-Schiemann's papers on the Migdal-Kadanoff model; the two-dimensional character formula; the Peierls facts on the Ising model; the a-theorem; every statement on U(1) in four dimensions.
  - Project Euclid (bot check) and the Hamburg server (403) refused downloads; I stopped there.
  - The lane's own Theorem DOB was seen through one-line search hits only. Rows 712 and 720 were read in the ranges listed in Step 5, not whole. The 36 verdicts of rows 712 and 720 were not re-derived.
  - The other branches were searched in part only; Section 5.3 lists what was and was not searched.
  - (TM-tw-Z2), the Z_2 transfer operator with twists, is an input of Proposition Z2 and is not written anywhere in the lane.
  - The sketch of 7.2 (route B) is not a proof. Routes A, C, D were not attempted.
  - Nothing here is about SU(N), N >= 3, and no statement about SU(2) at a coupling of order one is proved.

**Status block** (kept current).

| Step | State | Main result |
|---|---|---|
| 0 record, closed list | done | open and closed lists written; own literature pass, since the lane's digests are closed |
| 1 wall twice | done | no blind check ran (no subagents) |
| 2 inventory | done | ten source notes (2.A), the lane's statements (2.B), beliefs (2.C), one table (2.D) |
| 3 reason up | done | C1 to C9: none of the proved cases read has a step in the size without exact closure; base = sufficiency in all of them; F is vacuous as logic, its content is the far base |
| 4 assumptions | done | 23 rows; first five: b2 (N fixed), c1+c2 (F and the far base), a2+a1 (periodic, global), c4+c3 (one-way, scalar), c6 (class-wide) |
| 5 compare | done; scope of the branch search in 5.3 | C1, C2, C4, C6 partly in rows 712, 720; C7, C9 found again; the form-by-form table and the Martinelli-Olivieri step are added |
| 6 filters | done | no verdict of the 36 changes; one necessity claim (row 712, L92) is too strong as a claim about proofs; one in-class test added (compact Gaussian, every value above s_1) |
| 7 routes | done | seven routes; E (a control inside class K) and F (a reading item) survive; A and C blocked-equivalent; B and D wounded; the form F retired as the default brief |
| 8 attempts | done | Proposition Z2 (the full and kappa seeds of Z_2 at beta >= 91, N = 3; argued, given the Z_2 transfer operator); Remark 2D; one guide run, pass |
| 9 report | done | the form is a habit as a proof form: none of the ten proved cases read has it outside exact closure; the wall stays: no known means to verify a criterion at the scale xi |

## Step 0. Where the record is; what is open and what stays closed

**The record of the wall** (found by name and by `grep -n`; arguments not read before Step 5).

- The consumer: `library/gap-skeleton-final.md` Sections 13.15, 13.16 (L547-600); `library/gap-flux-exercise.md` 8.2 to 8.4 and Step 9; `library/gap-flux-exercise-check.md` Section 7.
- The form under test: FINISH row 735 (this row) and `library/exercise-skill-v2.md` Section 5.2, proposal 2 (L1211-1216). The proposal points to `library/gap-phys-seed.md` L155-164 for the form as row 720 wrote it; that file is closed until Step 5, so Steps 1 to 4 use the wording of the row.
- 49 files `library/gap-*.md` and 20 files `library/prior/gap-*.md`; FINISH rows 697 to 734.

**Open now** (read for this run before Step 5): `GOAL.md` (whole); `FINISH.md` L52-74, L320-350, row 735; `gap-skeleton-final.md` L1-68, L547-600; `gap-flux-exercise.md` L420-522, L615-675; `gap-flux-exercise-check.md` Section 7 (L495-525); `gap-crux-restate.md` L29-79, L170-231 (setting, the five candidates, Theorem S with its lemmas); `gap-seed-limit.md` L8-53, L182-256 (Hypothesis (G), Propositions P, P', N1, N2, Theorem L); `gap-seed-shape.md` status block, Section 3, 4.3, 7; `exercise-skill-v2.md` Section 5.2 proposal 2 and Section 4.6 (the measure, which the row names).

**Closed until Step 5:** `library/gap-phys-seed.md` and its check; every other `library/gap-*.md`; `library/prior/gap-*.md`; `library/exercise-skill-v2.md` beyond the two places above; FINISH rows 697 to 734; main and the other pull-request branches.

**Literature.** The lane's literature record is in the closed digests. So this run made its own pass, limited to the proved cases that the row names, and read the primary sources. Open copies come from two places: `~/ym4d-papers/dl-2026-11-11/` (downloaded by rows 714 and 719 under the owner's rule of 2026-11-11; I use the papers there, not the lane's digests of them), and new downloads into `/tmp/gfe-735/dl/<name>/`. Step 2 gives the reading state of each source. Nothing downloaded is committed.

## Step 1. The wall, stated twice

**Plain version.** We want to show that the lightest particle of the theory has a positive mass. The plan needs one inequality on a box of one large size, many particle wavelengths wide: the seed. Our account of the theory controls only very small boxes. So every tool tried so far was given one shape: a number measured on a box, known on a small box, with a rule that the number can only improve when the box is doubled, until it passes a mark that gives the seed. No such doubling rule could be proved. What nobody checked is whether proofs of a positive mass, in the models where one exists, have this shape at all. The evidence so far covers only models where the seed fails. Getting past the wall means: either the proved cases use a doubling rule (then copy one), or they use something else (then name it, and brief the next attempt with it). Analogy: a ladder climbed rung by rung, against a lift.

**Precise version.**

- *Target T.* (G_ev): along every sequence of sides L_i -> infinity there are n_i <= L_i/2 with S_ev(n_i; L_i^3) -> 0, m_ev(L_i^3) >= m_0 > 0 and L_i - n_i -> infinity (`gap-flux-exercise.md` L453); or one of the three seeds S_w(N; (2N)^3) < 1/5041, w in {periodic, full, kappa}, which gives (G_ev) (Corollary EV, L515). For the tree the seed is needed in the scaling form: at one physical size, uniformly in the cutoff ((SEED-phys), `gap-seed-limit.md` L186).
- *The form F under test* (row 735): a torus quantity Q; **(BASE)** a bound on Q at one small size, where the account works; **(STEP)** a one-way inequality Q(2L) >= sigma(Q(L)) for every value of Q(L) in an interval; **(SUFF)** a value of Q beyond the target gives the seed.
- *The question.* Is F needed by T, needed only by the method (the inputs that the lane has), or a habit? The test: the proved cases of a gap or of exponential clustering. For each: the statement, the argument that carries it, whether it has (BASE), (STEP), (SUFF), and what stands in the place of (STEP) if it has none.
- *Quantifiers.* "Fits F" means: the proof contains a quantity of one finite periodic system, and an inequality between its values at two sizes that is used on a range of values where the conclusion (the gap) is not yet known. An inequality that is used only below a threshold that already gives the gap is (SUFF), not (STEP). (This line fixes the word; without it every finite-size criterion would count as a step.)
- *Does not count:* a fit by a trivial Q (the indicator of the seed); a case stated from memory without that mark; a list of cases with no verdict.
- *Boundary cases:* two dimensions (exact); U(1) in four dimensions at weak coupling (T false); Z_2 at large beta (the periodic seed false, (G_ev) true: `gap-skeleton-final.md` L584).
- *Outcomes.* Confirmed (a proved case in the class has a step: copy it), habit (no proved case has one: name what replaces it and what brief follows), or split by case.

No blind check of the plain version ran (no subagents allowed).

## Step 2. Inventory: what is known to be true

Written source by source. Part A is the proved cases (the positive controls), each with its reading state. Part B is the lane's own statements. Part C is beliefs. The table with one line per item is 2.D.

### 2.A Source notes for the proved cases (each note: statement, argument, reading state)

**A1. Three-dimensional U(1), all couplings. M. Gopfert and G. Mack, Commun. Math. Phys. 82 (1982) 545-606.** Open copy: the DESY preprint 81/036 (scan, from the INSPIRE record). Read: preprint pages 1 to 10 (introduction and discussion of results), as page images. Not read: Sections 2 to 7 and the appendices (the proofs). Project Euclid and the Hamburg server refused the download (bot check, 403); I stopped there.

- Statement (their Theorem 1, Corollary 2, Theorem 4). Villain action; beta = 4 pi^2/g^2; m_D^2 = (2 beta/a^3) exp(-beta v_Cb(0)/2). Theorem 1: the surface tension of the dual Z-ferromagnet (equal to the string tension) is at least c m_D/beta, for beta/a large enough. Corollary 2: the string tension is positive for all g^2 > 0. Theorem 4: with a cutoff M that goes to infinity slowly in units of m_D, the correlation functions of a rescaled field tend to those of the free scalar field of mass m_D. They write that "m_D is asymptotically equal to the physical mass (= mass gap, or inverse correlation length)" (their page 4).
- Argument, in their words (pages 4 to 9). (1) An exact duality transformation to an integer-valued field, then to a real field with a periodic potential. (2) "The first step in the proof is to integrate out the high frequency components of the field. This produces an effective action L_eff(Phi) ... with Pauli-Villars cutoff M = lambda^(-1) m_D of order m_D. L_eff is obtained in the form of a series expansion." The bounds on the correction terms come from "iterated Mayer expansions": the Yukawa interaction of the high-frequency part is split "into pieces of decreasing strength and increasing range", and the pieces are treated one after the other by cluster expansion (their Proposition 3; hypothesis: beta/a large). (3) At the scale 1/M the effective action is L_eff = -(1/2)(Phi, -Delta(1 - Delta/M^2) Phi) - (m_D^2/beta) sum of [1 - cos(beta^(1/2) Phi)] + small terms. The mass term is in the action. On blocks of side L of order 1/M the barrier between two minima is of order m_D^2 L^3/beta, which is of order 1/(m_D beta) and "grows exponentially with beta/a". Domain walls are treated by a Peierls expansion and spin waves by the cluster expansion of Glimm, Jaffe and Spencer about mean field theory, as Brydges and Federbush did for the dilute Coulomb gas. (4) All couplings: "The corollary follows from theorem 1 ... because alpha a^2 is a monotone decreasing function of beta/a by the 3-dimensional version of Guth's inequality" (their page 4).
- Does it fit F? **No.** There is no quantity of a finite periodic system and no inequality between two sizes. The scales between the lattice spacing and the correlation length (a number of scales that grows like beta) are crossed by an expansion that controls the whole effective action from both sides, with a small number at every scale (the monopole activity; the hypothesis is beta/a large). At the correlation length the criterion is a single-scale expansion with a small number of its own, exp(-const/(m_D beta)). The range of couplings that the expansion does not cover is reached by a correlation inequality that is monotone in the coupling, not in the size.
- In the place of (STEP): (i) an exact change of variables after which the theory is weakly coupled at every scale up to the correlation length, and the mass term stands in the effective action; (ii) monotony in beta from a correlation inequality of an Abelian model (Guth).

**A1'. S. Chatterjee, arXiv:2602.00436v2 (2026), "A short proof of confinement in three-dimensional lattice gauge theories with a central U(1)".** Read: pages 1 to 6 of 13. Statement (Theorem 3.1): for G in U(n) that contains all scalar matrices of modulus one, d = 3, free boundary, every beta: |<W_l>| <= n exp(-C (1 + n beta)^(-1) T log(R + 1)). Argument: the complex rotation of McBryan and Spencer, after conditioning on the non-central part; history: Glimm and Jaffe; Frohlich's comparison inequality. It is a bound on Wilson loops (a logarithmic potential), not a gap, and it uses a central U(1). Fit: no; one inequality at one scale, valid at every coupling, from a continuous central symmetry. I list it because it is a bound at all couplings with no flow. It says nothing about SU(2) (finite centre).

**A2. Two-dimensional SU(N), log-Sobolev at all couplings. J. Piazza and H. Shen, arXiv:2610.35286v1 (2026).** Open copy in `~/ym4d-papers/dl-2026-11-11/piazza-shen-2610.35286/`. Read: pages 1 to 5 in full, Sections 5 and 6 (pages 8, 9) in part. Not read: Section 4 (Lemma 4.1), Section 7 (an example).

- Statement (Theorem 1.1): for every N >= 2 and real beta there is C_{N,beta} such that the Wilson measure on (Z/L)^2 satisfies a log-Sobolev inequality with constant C_{N,beta} for every L. (They note that the gap itself is "essentially trivial in 2D", page 2.)
- Argument ("a two-scale disintegration", "a one-step RG argument", page 2). Let w be the normalised weight of one plaquette, t = N^2 |beta|, r = 1 - (1/2) exp(-2t) < 1. Integrating the links inside a block of n = m^2 plaquettes gives exactly w^{*n}, the n-fold convolution, as a function of the boundary word ((3.1)). Lemma 2.1: w^{*k} - 1 = r^(k-1) (w - 1) * v^{*(k-1)}. Lemma 2.2: the sup norms of w^{*k} - 1, its gradient and its Hessian are at most M r^(k-1). Choose n with M r^(n-1) <= 1/3. Then the measure of the block boundaries is a small perturbation of Haar measure (Bakry-Emery applies; Ricci curvature of SU(N) is used), and the conditional measures inside the blocks are independent and have a constant exp(4 t n) by Holley-Stroock. The chain rule for entropy joins the two.
- Does it fit F? **Yes, with an exact step, and not for a torus quantity.** Q(k) = sup |w^{*k} - 1|, the distance of the effective weight of a block of k plaquettes from the Haar weight. (BASE) Q(1) <= exp(2t). (STEP) Q(k+1) <= r Q(k) for every value of Q(k): a one-way inequality that holds at every value. (SUFF) Q(n) <= 1/(3M) gives the criterion at the block scale. The step is a Doeblin bound: w >= (1 - r) > 0 on a compact group. It holds because integrating a block is an exact convolution in two dimensions. The authors say that in higher dimensions "conditional integrations would naturally produce nonlocal, larger Wilson loops" (page 2).
- The step holds for U(1) as well (their Remark 1.2 excludes U(1) only at the curvature step).

**A3. Finite gauge groups at weak coupling (this includes Z_2 at large beta).**

- *M. P. Forsstrom, arXiv:2104.03752v1 (Commun. Math. Phys. 393, 2022).* Read: pages 1 to 4 (abstract, Theorem 1.1, Remarks 1.2 to 1.13). Not read: the proofs. Statement (Theorem 1.1): G finite Abelian, B a box in Z^4, free boundary, 30 alpha(beta) < 1 (for Z_2: 30 exp(-4 beta) < 1). For f_1, f_2 that depend on the plaquette variables d sigma in disjoint sets P_1, P_2: |Cov(f_1, f_2)| <= C_1 ||f_1|| ||f_2|| (C_2 alpha(beta))^dist(P_1, P_2). Remark 1.11: periodic boundary conditions "with minor changes to the proofs" (the author's remark; not a theorem of the paper). Argument (Remark 1.13): "a coupling argument"; the infinite-volume limit by Ginibre's inequality (Remark 1.7).
- *A. Adhikari and S. Cao, arXiv:2202.10375v3 (Ann. Probab. 53, 2025).* Read: pages 1 to 6. Not read: Sections 2 to 6, the appendices. Statement (Theorem 1.1): G finite, possibly non-Abelian; beta >= (114 + 4 log |G|)/Delta_G, Delta_G the least action of a non-trivial plaquette. For conjugacy-invariant functions of loops inside rectangles B_1, B_2 at distance L: |Cov| <= 4 (4 x 10^24 |G|^2)^(|B_1| + |B_2|) ||f_1|| ||f_2|| exp(-(beta/2) Delta_G (L - 1)). Argument (their pages 2, 3, 6): defects on a unique ground state; a swapping map on pairs of configurations; the covariance is bounded by the probability that two independent defect sets connect the two regions. They note that the cluster expansion of Seiler's monograph does not extend to non-Abelian finite groups as claimed (Borgs), because linked defects do not factorise.
- Fit: **No.** One scale (the lattice spacing), one small number, exp(-beta Delta_G). The observables are functions of contractible loops, so this is the even half. No torus, no flux sector, no thermal sum. In the place of (STEP): nothing; the correlation length is below one lattice spacing.
- For the lane: these are proofs of exponential clustering of centre-blind local functions in a model where the periodic seed is false (`gap-crux-restate.md` L227: Z_2 at large beta has s >= 7 - o(1), recalled there). They do not prove (G_ev) as the lane states it (a thermal sum on cubes); they prove the clustering that (G_ev) is used for, directly.

**A4. Strong coupling.**

- *K. Osterwalder and E. Seiler, Ann. Phys. 110 (1978) 440.* **Recalled; no open copy was looked for.** Statement as recalled: for small beta the cluster expansion converges for every compact group and dimension; exponential clustering and the area law follow.
- *H. Shen, R. Zhu and X. Zhu, arXiv:2204.12737 (Commun. Math. Phys. 2023).* Read: the abstract only. Statement (abstract): for |beta| < 1/(16 (d - 1)) and SU(N) (their scaling beta N) the infinite-volume measure is unique, satisfies log-Sobolev and Poincare inequalities, and "correlations of a large class of observables decay exponentially". Argument (abstract and Piazza-Shen page 2): the Bakry-Emery condition holds for the whole measure at small beta.
- *Theorem DOB of this lane.* Statement seen only through one-line `grep` hits: Dobrushin's condition on one link, alpha = 18 beta < 1, gives the seed (both halves) for beta < 1/18; located in `gap-mid-max.md`, checked in `gap-dob-astra.md` Section 5 ("HOLDS AFTER CORRECTION"). (Disclosure: the `grep -n "Theorem DOB"` that located it printed twelve one-line hits from closed files: `gap-crux-fp.md` L41, L204, L230, L276, L405, L443, L458, L494; `gap-crux-fp-check.md` L48, L62; `gap-dob-astra.md` L205; `gap-flux-exercise.md` L303. I did not open those files before Step 5.)
- Fit: **No.** One scale, one small number (beta). The criterion (uniqueness, a contraction, a convex potential) is checked at the lattice spacing.

**A5. Finite-size criteria for quantum spin chains.**

- *D. Gosset and E. Mozgunov, arXiv:1512.00088v1 (J. Math. Phys. 57, 2016).* Read: pages 1 to 3 and the statement of Knabe's theorem as they quote it. Not read: the proofs. *S. Knabe, J. Stat. Phys. 52 (1988) 627*: read only as quoted there. Statement (Knabe, their Theorem 1 and Corollary 2): for a frustration-free, translation-invariant nearest-neighbour chain of projectors, with eps_n the gap of the open chain of n sites and eps°_m the gap of the periodic chain of m sites, n > 2, m > n: eps°_m >= ((n - 1)/(n - 2)) (eps_n - 1/(n - 1)). Gosset and Mozgunov improve the threshold to 6/(n(n + 1)), "asymptotically optimal", and state the contrapositive: a gapless frustration-free chain has open-chain gap O(n^(-2)). They note that for general (frustrated) systems no method is known, and that the question is undecidable in two dimensions (their page 2).
- *B. Nachtergaele, arXiv:cond-mat/9410110 (Commun. Math. Phys. 175, 1996).* Read: the abstract, the table of contents, Section 2 pages 10, 11 (Conditions C1 to C3, Theorem 3). Statement (Theorem 3 (i)): under C1 (local structure), C2 ("the energy is minimized locally", no frustration) and C3 (||G_{Lambda_{n+1} minus Lambda_{n-l}} E_n|| <= eps_l < 1/sqrt(l + 1) for all n >= n_l), the gap of H_{Lambda_N} is at least (gamma_{l+1}/d_{l+1}) (1 - eps_l sqrt(l + 1))^2 for every N. He writes that C3 "plays the role of a mixing condition similar to the Dobrushin-Shlosman condition" (page 11), and verifies it for valence-bond-solid states from their exact structure.
- Fit: **(SUFF) only.** Each is "a condition at one finite size gives the gap at every size". Each needs the ground-state energy of every finite piece to be exactly zero (no frustration). The base is at the same size as the criterion: the condition is verified there by exact diagonalisation or by an exact formula for the ground state. No inequality carries a quantity from a size where the condition fails to a size where it holds.
- For the lane: Theorem S is of this kind, with the deficit kappa(b) in the place that frustration-freeness makes zero (Lemma K, Lemma X). The contrapositive form is the useful part: "no seed at any size" is a quantitative statement about every size (for the lane: S(n; (2n)^3) >= 1/5041 for every n, `gap-crux-restate.md` L226).

**A6. Mixing, log-Sobolev and finite-volume conditions for classical spin systems.** *F. Martinelli, "Lectures on Glauber dynamics for discrete spin models", Saint-Flour 1997, mp_arc 97-578* (it presents the results of Stroock and Zegarlinski and of Martinelli and Olivieri). Read: pages 9 to 11 and 43, 44 of 101, from a crude text extraction of the PostScript file (formulas partly garbled; the sentences are clear). *D. Stroock and B. Zegarlinski, Commun. Math. Phys. 144 (1992) 303 and 149 (1992) 175*, and *F. Martinelli and E. Olivieri, Commun. Math. Phys. 161 (1994) 447, 487*: **not read** (Project Euclid refused; the folder of row 719 for the first is empty); what I state of them beyond Martinelli's text is recalled.

- Statements read. Definition 2.4: strong mixing SM(V, C, m): for every subset Delta of V and every site y outside V, the change of the law on Delta under a change of the boundary value at y is at most C exp(-m d(Delta, y)), uniformly in the boundary condition. Theorem 2.7: strong mixing for all multiples of one cube is equivalent to exponential decay of finite-volume covariances uniformly in the boundary condition (SMT). Page 11: "effectiveness": "in order to verify strong mixing on, e.g. all cubes, it is sufficient to verify it for a finite class of subsets"; and "a power-law decay of covariances with a large enough power depending on the dimension implies exponential decay". Theorem 2.5 (Martinelli, Olivieri, Schonmann): in two dimensions weak mixing for every finite set implies strong mixing for every square. Theorems 4.5, 4.6: assume SMT for all rectangles of sides between L and a multiple of L; then the gap g and the log-Sobolev constant c_s of the Glauber dynamics, taken as the worst case over boundary conditions, satisfy g(2L) >= (1 - k/sqrt(L)) g(L) and c_s(2L) <= (1 + k/sqrt(L)) c_s(L) for all large L. "In particular inf_L g(L) > 0."
- Recalled (Stroock-Zegarlinski): for finite-range spin systems with compact spins, the Dobrushin-Shlosman mixing condition, the uniform log-Sobolev inequality and the uniform gap of the dynamics are equivalent.
- Where strong mixing itself comes from (page 10): for the Ising model, at small beta or large beta h (a small number), and in two dimensions in the whole one-phase region through weak mixing (Higuchi; Schonmann and Shlosman) and Theorem 2.5. In more than two dimensions "strong mixing for all cubes has been proved instead for small enough beta or large enough beta h", and it is expected to be false for some sets at large beta and small h.
- Fit: **two layers.** Layer 1 (equilibrium clustering): (SUFF) only, a condition on one finite class of volumes for all boundary values; the condition is necessary as well as sufficient. Layer 2 (from clustering to the dynamical gap or log-Sobolev constant): **this is (STEP)**. Q(L) = the worst gap over boundary conditions; Q(2L) >= (1 - k/sqrt(L)) Q(L) at every value of Q(L); the product converges. The hypothesis of the step is the clustering, and the quantity is a supremum over all boundary values, not a torus quantity. Martinelli notes that the easy version of the step, g(2L) >= g(L)/16, gives only g(L) >= L^(-alpha) (page 44): a one-way step with a fixed loss gives a power law and no gap.

**A7. Sharpness of the phase transition. H. Duminil-Copin and V. Tassion, arXiv:1502.03050 (Commun. Math. Phys. 343, 2016).** Read: page 2 (Theorem 1.1 and the plan of proof), Theorem 2.1 and its plan (pages 9, 10). Not read: the proofs. (Not in the row's list; added because it is the cleanest proved case of "exponential decay in the whole one-phase region with no small number".)

- Statement (Theorem 2.1, Ising, any transitive graph, finite range): for beta < beta_c, <sigma_0 sigma_x> <= exp(-c d(0, x)); for beta > beta_c, the magnetisation is at least sqrt((beta^2 - beta_c^2)/beta^2). First proved by Aizenman, Barsky and Fernandez.
- Argument (their plan). phi_beta(S) := a boundary sum of two-point functions of a finite set S that contains 0. beta~_c := sup of the beta with phi_beta(S) < 1 for some finite S. (i) (SUFF) If phi_beta(S) < 1 for one finite S, exponential decay follows (Simon-Lieb type; BK inequality or the switching lemma). (ii) A differential inequality in beta: d/dbeta <sigma_0>^2 >= (2/beta) inf_S phi_beta(S) (1 - <sigma_0>^2). So where no finite S passes the criterion, the order parameter grows, and it is positive above beta~_c. Hence beta~_c = beta_c.
- Fit: **No (STEP) in the size.** (SUFF) at one finite set, and a **dichotomy**: at each coupling either some finite set passes the criterion, or there is long-range order. The one-way inequality is in the coupling, and it is used at every value of the order parameter. The tools are correlation inequalities of the Ising model (random currents, switching lemma) or of percolation (BK).

**A8. Mass generation at large N. C. Kopper, arXiv:math-ph/9902020 (Commun. Math. Phys. 202, 1999).** Read: pages 1 to 4 of 44 (abstract, introduction). Not read: the proofs. (Not in the row's list; added because it is the proved case nearest to ours: asymptotic freedom and a mass that is exponentially small in the coupling.)

- Statement (abstract): the two-dimensional O(N) non-linear sigma model "with a suitable ultraviolet cutoff ... for a sufficiently large (but finite!) number N of field components ... is massive and thus has exponentially decaying correlation functions". He requires N^(-1/6) < const exp(-4 pi/lambda), and reports the same shape in the lattice results of Kupiainen (N > const exp(50 pi beta)) and of Ito and Tamura (N > const exp(400 pi beta)) (page 4). The Gross-Neveu case is Kopper, Magnen and Rivasseau (his [1]; not read).
- Argument (pages 1 to 3): an interpolating scalar field; the N components are integrated out exactly; the mass stands in the effective action of the new field; then one small-field/large-field split and one cluster expansion at the scale of the mass. The small number is a power of 1/N, and it "has to beat the factor O(m^(-2)) from the spatial integration per link" (page 4): it must beat the volume of one correlation cell.
- What is not proved there (page 2): the model starts at a cutoff where the coupling lambda is of order one. "The much more difficult part of the ultraviolet analysis of the model - so far only performed in the hierarchical case for N > 2 and as long as the effective coupling stays small - is to show that the Lagrangian (1) is a good approximation to the full model." So for a fixed N the result covers a bounded range of beta, and the joint statement (ultraviolet flow, then the mass) is not proved even at large N.
- Fit: **No.** In the place of (STEP): a second small number (1/N) that does not come from the coupling, which makes the theory at the correlation length a perturbation of an exactly solved one.

**A9. The form F was tried once in exactly our setting. E. T. Tomboulis, arXiv:0707.2179 (2007); K. R. Ito and E. Seiler, arXiv:0711.4930 and 0803.3019.** Read: the abstract of Tomboulis; Ito-Seiler 0711.4930 pages 1 to 8 of 10; the abstract of 0803.3019. Not read: Tomboulis's paper itself.

- Tomboulis's claim (abstract): SU(2) in d <= 4 confines for all couplings. "The strategy is to employ approximate RG decimation transformations of the potential moving type which give both upper and lower bounds on the partition function at each successive decimation step. By interpolation between these bounds an exact representation of the partition function is obtained on progressively coarser lattices", also "in the presence of external center flux"; the result is "confining behavior for the vortex free energy order parameter (ratio of partition functions with and without external flux)".
- This is F: Q = the ratio of twisted and untwisted partition functions of a periodic box; (BASE) the lattice scale; (STEP) each decimation by a factor b, carried by one-way bounds (the Migdal-Kadanoff recursion increases Z, Ito-Seiler page 6); (SUFF) the flow reaches strong coupling.
- Ito and Seiler: (a) Their Theorem 2.1, quoted from Ito's earlier work: under the Migdal-Kadanoff recursion, "for D <= 4 and for G = SU(N) or G = U(N)", all character coefficients c_j(n), j != 0, tend to 0. (b) If the claimed step were correct it would give confinement at all couplings "whether G is abelian or non-abelian"; "this cannot be correct, however, since there exists a deconfining Kosterlitz-Thouless (KT) type transition in 4D lattice gauge theory based on abelian gauge groups" (page 6). (c) The missing link: the two interpolation parameters, for Z and for Z^+ = (Z + Z^-)/2, must be equal; this reduces to an inequality A(alpha) > A^+(alpha) between derivatives of the two free energies, "which is, as far as we can see, not proven"; it "is obvious when {c_j >= 0} are small and the formal expansion converges" (pages 7, 8).
- Reading for the lane: the one-way bounds of the step held for every group, so the step could not hold for the ratio; the part that would have to tell SU(2) from U(1) was an inequality that is known only where a small number exists.
- Recalled, not read: Ito's proofs for the Migdal-Kadanoff (hierarchical) model (Commun. Math. Phys. 95, 1984; Phys. Rev. Lett. 55, 1985); Muller and Schiemann (1988). In that model the flow of the plaquette weight is an exact map, and the step is a theorem.

**A10. Two dimensions, exact.** The torus formula Z = sum over irreducible representations of c_r^(area) (Migdal) is **recalled**; I prove the form needed here by hand in Step 8 (Proposition 2D), so no source is needed for it.

### 2.B The lane's own statements (from the open list only)

| # | Item | Mark | Source | Standing, reading state |
|---|---|---|---|---|
| L1 | Theorem S with Lemmas K, X, E, E' and Corollary S3': in the class K (W(a,b) = W(b,a) = Tr T_b^a, T_b positive, trace class, ell finite), s = S(N; (2N)^3) < 1/5041 gives m(L^3) >= log(1/(5041 s))/N for every L >= 2N. The inequalities are used below the threshold only. | THM | `gap-crux-restate.md` L170-231 | checked by two models (rows 698, 699), with the corrections printed there; read in full |
| L2 | Theorem EV-L, Proposition CL, Theorem S-w, Corollary EV: three seeds (periodic, full, kappa); each gives (G_ev) at all sizes and the clustering of every periodic limit on centre-blind local functions. | THM | `gap-flux-exercise.md` L420-522 | checked line by line by gpt-6-astra max (row 732), HOLDS, given (TM-tw); read in full |
| L3 | Scaling form: (SEED-phys) gives a gap M_* in physical units (Proposition P). Rate filter: a seed at (n, s) needs n > 8.5/m. | THM | `gap-seed-limit.md` L186-204 | argued there; a check is named in the skeleton heading 13.10, not read |
| L4 | Thresholds for other shapes tend to 1 (Theorem SH); no threshold above 1 is possible in K; the seed needs at least 12.9 correlation lengths. | THM | `gap-seed-shape.md` Sections 3, 4, 7; `gap-skeleton-final.md` L553 | argued; "checked" by the heading of 13.12 only |
| L5 | The alternative: either S(n; (2n)^3) >= 1/5041 for every n >= 3, or a uniform gap on the dyadic cubes from some size on. | THM | `gap-crux-restate.md` L226 | follows from L1 |
| L6 | The seed bounds the number of states (N1); a gap with a state count of exponent theta < 1 gives the seed (N2); a gap alone is not shown to give it. | THM | `gap-seed-limit.md` L206-236 | argued; second form checked (row 703) |
| L7 | The account controls log Z of its own tori up to C l^4, which is short of the seed by the number of unit cells. | reading | `gap-skeleton-final.md` L553 | the lead's reading of row 720; not re-read |
| L8 | (PHYS-SEED) holds if and only if (BDD-Delta) and (Z-UNB): the Casimir free energy stays bounded and (gap of the periodic cube) x (side) is unbounded. | THM | `gap-skeleton-final.md` L557-562 | unchecked on 2026-11-11 (check = row 727); statement only |
| L9 | In the class K: the Ising model with two phases has S -> 1 at every shape and no gap; the compact Gaussian model Z_R has no gap and an exact thermal sum that depends, in the continuum limit, on the shape and on R only. | THM | `gap-seed-shape.md` L205-246 | first: proved, "no gap" recalled (Peierls); second: formula proved, values GUIDE (inf over R of S = 3.1 at ratio 2) |
| L10 | Filters: U(1) in four dimensions has no gap at weak coupling; Z_2 at large beta: the periodic seed fails and (G_ev) holds. | THM, recalled | `gap-skeleton-final.md` L59, L584 | recalled by the runs; Forsstrom (A3) is a proof of the clustering half, read in part |
| L11 | The group enters the definitions through two facts only: the single-plane twist has classical cost zero (Fact T), and b_0 > 0 (Fact B). | reading | `gap-crux-restate.md` L41 | the author's statement |
| L12 | The periodic seed holds at strong coupling (beta < 1/12800; Dobrushin: beta < 1/18). | THM | heading of 13.10; `grep` hits (A4) | checked per those lines; not read |

### 2.C Beliefs (used in no proof)

| # | Belief | Where it comes from |
|---|---|---|
| B1 | Four-dimensional SU(2) has a gap and confines at every beta. | numerics, physics; the Clay problem |
| B2 | On a small torus the thermal sums are large (flux sectors nearly degenerate, many low levels of the constant modes); a seed exists only from some tens of correlation lengths. | `gap-skeleton-final.md` L553, L560 (recalled small-volume physics; guide values) |
| B3 | In the continuum limit a dimensionless torus quantity at physical size l is a function of l alone. | scaling; assumed by every step-scaling method |
| B4 | No gap is proved, in any model that is not exactly solvable, at a correlation length far above the lattice spacing without a second small number or a correlation inequality. The two-dimensional O(3) model at large beta is the nearest open case. | my reading of A1 to A9; Kopper page 2 reports the doubts of Patrascioiu and Seiler. A belief about the literature, not a theorem. |

### 2.D The proved cases in one table

Marks: all rows are THM with the reading state of 2.A. "Scale" is the size at which the criterion is verified, in correlation lengths xi.

| Case | Statement | What carries it | (BASE) | (STEP) in size | (SUFF) | In the place of (STEP) |
|---|---|---|---|---|---|---|
| A1 3D U(1), Gopfert-Mack | string tension > 0 at all g; mass about m_D | duality; iterated Mayer expansions; expansion about mean field at scale 1/m_D; Guth's inequality | no | no | expansion at scale xi | weak coupling in the dual variables at every scale (two-sided control of the effective action); monotony in beta |
| A2 2D SU(N), Piazza-Shen | log-Sobolev at all beta, uniform in L | exact block integration = convolution; Doeblin contraction; Bakry-Emery | yes | **yes, exact** (effective weight, not a torus quantity) | yes | - |
| A3 finite groups, weak coupling | clustering of loop functions | defects, coupling or swapping | = (SUFF) | no | one scale, lattice spacing > xi | a small number, exp(-beta Delta_G) |
| A4 strong coupling | clustering; log-Sobolev; the periodic seed | cluster expansion; Dobrushin; Bakry-Emery | = (SUFF) | no | one scale, lattice spacing > xi | a small number, beta |
| A5 Knabe; Gosset-Mozgunov; Nachtergaele | gap of frustration-free chains | operator inequality H^2 >= c H; martingale method | = (SUFF) | no | one finite size | exact computation at that size; zero ground-state energy at all sizes |
| A6 Stroock-Zegarlinski; Martinelli-Olivieri | strong mixing, gap of the dynamics and log-Sobolev are equivalent; one finite class of volumes suffices | all boundary values; recursion in the size | trivial | **yes**, for the dynamical gap, given the clustering | yes, and necessary | for the clustering itself: a small number, or weak mixing from correlation inequalities (2D) |
| A7 sharpness, Duminil-Copin-Tassion | clustering for all beta < beta_c | finite criterion phi_beta(S) < 1; differential inequality in beta | no | no | one finite set | a dichotomy (criterion at some size, or long-range order), from correlation inequalities; one-way in the coupling |
| A8 O(N) at large N, Kopper | mass with ultraviolet cutoff, N > exp(c beta) | interpolating field; one cluster expansion at scale xi | no | no | expansion at scale xi | a second small number, 1/N; the join with the ultraviolet flow is not proved |
| A9 Tomboulis; Ito-Seiler | (claimed) confinement at all couplings, 4D SU(2) | Migdal-Kadanoff bounds with interpolation | yes | **claimed; not proved** | yes | fails: the bounds hold for U(1) as well |
| A9' Migdal-Kadanoff model (recalled) | flow to strong coupling, D <= 4, SU(N) and U(N) | exact recursion | yes | **yes, exact** | yes | - |
| A10 2D gauge theory, exact | all thermal sums explicit | independence of plaquettes | yes | **yes, exact** (Step 8, Proposition 2D) | yes | - |


## Step 3. Reasoning up from the inventory

Only the items of Step 2 are used. Marks are at the end of each item.

### 3.1 What follows at once

**F1 (the count).** In table 2.D a (STEP) in the size occurs in four rows: A2, A9', A10, and the second layer of A6. In A2, A9' and A10 the integration over a block is exact and stays inside a family with one function (the plaquette weight); I call this *exact closure*. In A6 the step is for the gap of the dynamics, and its hypothesis is the equilibrium clustering. No row has a (STEP) for a quantity of a periodic system, in a model without exact closure, that is used to reach the clustering. *reading of 2.D; as strong as the reading states of A1 to A10.*

**F2 (base equals sufficiency).** In every row where clustering is proved without exact closure, the criterion is verified at the scale at which it is applied, and that scale is at least one correlation length: the lattice spacing in A3 and A4 (there xi is below one spacing); the scale xi in A1 and A8, with a small number that is not the coupling at that scale (the monopole activity; 1/N); one finite size by exact computation in A5; and in A7 the criterion holds at some finite size by the definition of beta_c. *reading of 2.D.*

**F3 (F is vacuous as a logical form).** Let a model of the class K have a seed at size N: s = S_w(N; (2N)^3) < 1/5041. Put Q(L) := S_w(D/2; L^3) with D as in Corollary S3'. Then (BASE) holds at L = 2N, (STEP) holds in the form Q(2L) <= 5041 Q(L)^2 for dyadic multiples of 2N, and (SUFF) is the seed. So every model with a seed fits F, with the base at the seed size. The content of F is therefore one clause only: **the base is at a size far below the seed size**, where the criterion fails. *argued, from L1.*

**F4 (monotony in the coupling points the wrong way).** In A1 the correlation inequality carries the result from large beta (where the expansion works) to smaller beta. For SU(2) the seed is known at small beta (L12) and wanted at large beta. At a fixed lattice size n it is false for large beta: by L3 a seed at (n, s) needs n > 8.5/m, and the lattice gap m tends to 0 as beta grows (the rate filter of `gap-skeleton-final.md` L64; proved there with the account, unchecked). So the set of beta at which the seed holds at a fixed n is bounded. A statement "the seed at (beta, n) gives the seed at (beta', n) for beta' > beta" is false, and a statement in the other direction gives nothing new. Monotony can only be wanted along a curve n(beta) that grows like the correlation length, and that is the scaling statement itself. *argued, given the rate filter (unchecked) and L3, L12.*

**F5 (a model that moves the wrong way blocks a class-wide step at that value).** Let Q be a function of the model and of the size. Let (STEP_x) be: "for every model of K and every L >= L_0 with Q(L) = x: Q(2L) <= sigma(x)", with sigma(x) < x. If one model of K has Q(L) = x and Q(2L) >= x at some L >= L_0, (STEP_x) is false. This is the refutation form of the skill's step 6c, applied to one value. Apply it to Q(n) = S(n; (2n)^3) and to the compact Gaussian model Z_R of L9, with R = rho/n. In the continuum form of L9, 1 + S = theta(1/(16 rho^2)) theta(4 pi^2 rho^2)^3 Pi, with Pi the oscillator product, which does not depend on rho. At the size 2n the same model has rho' = 2 rho. theta(A) = sum over P of exp(-A P^2) decreases in A. Let rho >= 1/2. For A >= pi^2: 1 <= theta(A) <= 1 + 2 exp(-A)/(1 - exp(-3A)) < 1 + 4 exp(-A) (P^2 >= 1 + 3(P - 1) for P >= 1). So theta(16 pi^2 rho^2)^3 >= 1, while theta(4 pi^2 rho^2)^3 <= (1 + 4 exp(-pi^2))^3 < 1.001. By Poisson summation theta(A) = (pi/A)^(1/2) theta(pi^2/A), so theta(1/(16 rho^2)) = 4 rho pi^(1/2) theta(16 pi^2 rho^2), with the last factor in [1, 1 + 4 exp(-4 pi^2)]. So the first factor doubles when rho doubles, up to a factor that differs from 1 by less than 10^(-15). Together: 1 + S(2n) >= 1.99 (1 + S(n)), and S grows. As rho runs over [1/2, infinity) the value S(n) runs over [s_1, infinity) with s_1 := S at rho = 1/2 (continuity in rho). Hence: **for every value x >= s_1 there is a model in K whose S(n; (2n)^3) equals x at one size and is larger at the doubled size.** No improving step for this Q can be proved from the properties of K at any value x >= s_1. *argued for the continuum formula, given L9; on the lattice the oscillator products at n and 2n differ by a factor that tends to 1 as n grows, which I did not write out; the number s_1 is a GUIDE (L9 gives inf over R of S = 3.1 at this shape, so s_1 is a few units).* For the value 1 the two-phase Ising model plays the same part (L9: S tends to 1; that it stays there at large sizes is recalled, Peierls).

**F6.** By B2 (a belief) the thermal sum of SU(2) on a small torus is above 7. The seed is below 1/1650. So a flow of this Q from the base to the seed passes every value in between. By F5, at every value above s_1 and at the value 1, the step must use a property that the compact Gaussian model, or the two-phase model, does not have. *belief, because B2 is one; the logic is F5.*

### 3.2 The least a solution must contain

Any proof of T in the scaling form (a) is false for U(1) in four dimensions, so it uses the group; (b) is a statement about a box of at least 12.9 correlation lengths (L4), where the effective coupling is of order one (`gap-skeleton-final.md` L33-35); (c) by F2 it must verify a criterion at that scale. The proved cases offer four ways to do (c): a small number at that scale; exact closure; a correlation inequality together with a parameter; a two-sided control of the effective action down to that scale. By L11 the group enters through Fact T and Fact B only, and neither is a small number at the scale xi. *argued from F2, L4, L11; "four ways" is a reading of 2.D, not a theorem that no fifth exists.*

### 3.3 The smallest object

The smallest model where F fits is two-dimensional gauge theory (Proposition 2D, Step 8): the step is exact, and the wall does not bite. The smallest model in which the wall bites is, in my reading, the two-dimensional O(3) model on a periodic circle with the seed of Corollary S2 (`gap-crux-restate.md` L215): asymptotically free, no small number at the scale xi, no exact closure for the lattice model, and open (B4). I did not build it. *reading.*

### 3.4 Where the result can come from; one problem or several

Three problems, which A8 shows apart: (U) the ultraviolet flow down to the scale where the coupling is of order one, with two-sided control; (I) a criterion at a scale of order xi; (J) the join: the output of (U) lies in the class that (I) needs. In A1 one expansion does all three, because the dual variables are weakly coupled at every scale. In A8, (I) is proved with 1/N, and (U) and (J) are not proved. In the lane, the account is (U) down to its torus floor (L7); (I) is the seed; F is an attempt to do (I) and (J) together by one inequality that needs no control of the effective action. *reading.*

### 3.5 Make the requirement less wrong

(GAP) reads the clustering of the limit state on centre-blind local functions (Theorem EV-L (d), L2). (G_ev) and the three seeds are sufficient forms of it that are global (a trace over a sector of a periodic box). A3 and A4 prove the clustering locally, with no torus quantity. So "a torus quantity" is a choice of the lane (SUPPLIED), made because Theorem S is the finite criterion it found. The local finite criterion is the one with all boundary values (C3 of `gap-crux-restate.md` L66; A6 shows that for spin systems it is necessary as well as sufficient). *argued from L2; the last clause is from A6, read in part.*

### 3.6 Price

If no step exists, the missing input is one of three statements, which I cannot show equivalent: (P-a) one of the three seeds at one physical size, uniformly in the cutoff (the crux as the skeleton states it); (P-b) the all-boundary criterion at one physical size; (P-c) a two-sided bound on the effective action at an effective coupling of order one, good enough for a single-scale criterion (`gap-skeleton-final.md` L564). *open.*

### 3.7 Conclusions

- **C1.** None of the proved cases A1 to A10 without exact closure uses a (STEP) in the size to reach clustering. (Reading; the proofs of A1 and A8 were read in their introductions only.)
- **C2.** Where a (STEP) is proved, it is exact closure (A2, A9', A10), or it takes the clustering as its hypothesis (A6, second layer).
- **C3.** In each proved case the criterion is verified at its own scale: base = sufficiency. What does it: a small number at the lattice scale; a second small number at the scale xi (dual activity, 1/N); exact computation; or a correlation inequality with a parameter, which gives a dichotomy.
- **C4.** F is vacuous as a logical form (F3). Its content is the base far below the seed size. That clause is needed by the method (the account stops at small tori, L7). It is not needed by T.
- **C5.** Monotony in the coupling cannot give the scaling form for SU(2) (F4; given the rate filter).
- **C6.** For Q = S(n; (2n)^3), no improving step can be proved from the class K at any value above s_1, nor at the value 1 (F5; argued for the continuum formula; s_1 a guide).
- **C7.** The one attempt at F in this setting (A9) failed at the inequality that had to tell SU(2) from U(1), and that inequality is known only where there is a small number.
- **C8 (belief).** The set of proved cases with xi far above the lattice spacing, no second small number, no exact closure and no correlation inequality is empty; the nearest open case is the two-dimensional O(3) model (B4). So the wall is not made by F: F is one wording of "no small number at the scale xi".
- **C9.** (GAP) reads local clustering; the torus form is the lane's choice (3.5).

## Step 4. The assumptions table

Taken from the wall's statement (row 735), the open files of Step 0 and Steps 2, 3. "Check" names a check that exists or the cheapest one.

| ID | Assumption | Where it is used | Needed or habit | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| a1 | The target is a seed, or (G_ev): a trace over a sector of a periodic box. | `gap-skeleton-final.md` L570-586 | needed by the method (Theorem S, Theorem EV-L) | (GAP) reads local clustering (C9); a local criterion would do | not by itself; it admits the tools of A3, A4, A6 | none run |
| a2 | The quantity is one of periodic systems only (no boundary values). | row 735; `gap-crux-restate.md` L66 | habit, with a reason: the account and Theorem S live on tori | all-boundary criteria (A6): necessary and sufficient for spin systems | unknown; boundary values of a gauge field are a large space | `gap-ds-gauge.md` (closed until Step 5) |
| a3 | The scaling form: one physical size, uniformly in the cutoff. | `gap-seed-limit.md` L186 | needed by the target (a continuum gap) | at one fixed beta the gap is a different, weaker statement | yes at small beta (L12); not at large beta | - |
| b1 | The Wilson action, exactly. | `gap-skeleton-final.md` L63 | needed by the account | another action in the same class (heat kernel) gives exact closure in 2D only | no in 4D | - |
| b2 | The group is SU(2); N is fixed. | `GOAL.md` T0 | needed by the target (owner: SU(2) first) | at large N a second small number exists (A8) | (I) becomes a known pattern; (U) and (J) stay open even there | A8, read in part. **Owner decision; named as a price only.** |
| b3 | The frame for exact tools is the class K. | `gap-crux-restate.md` L174 | needed by the method | a smaller class that excludes the compact Gaussian and the two-phase models | yes, if a property that defines it can be used in a proof | F5 names the two models to exclude |
| c1 | F: base, one-way step, sufficiency. | row 735 | **habit** as a proof form (C1, C4) | the criterion is verified at its own scale, as in every proved case | no: it then needs a tool at coupling of order one | this run, 2.D |
| c2 | The base is where the account works: a small torus at weak coupling. | row 735 ("a base at one small size") | needed by the method (L7) | base = seed size | no | - |
| c3 | One scalar Q with one function sigma for all beta and L. | row 735 ("for every value in an interval") | habit | a family of quantities, or the whole effective action (A1) | two-sided control is far more work, and it is what the proved multi-scale cases do | - |
| c4 | The step is one-way (an inequality). | row 735 | habit, from Theorem S and reflection positivity | (P-c) | no | A9 shows what one-way bounds cost: they hold for every group |
| c5 | The flow is in the size, at fixed beta. | row 735 | habit | a flow in beta (blocked: F4), in the shape, in the twist, in N | F4 closes one; the others not examined here | F4 |
| c6 | The step must hold at every value of an interval, for a class of models. | row 735 | habit | a step along the true trajectory only, proved by contradiction at a first bad size | unknown; no proved case of this kind was found either | - |
| c7 | The tools for a step are the exact inequalities of K (positivity, crossing, convexity). | `gap-skeleton-final.md` L42 | needed by the method | a tool that sees the group at coupling of order one | - | F5: such tools give no step above s_1 |
| d1 | "It also holds for U(1)" sets a tool aside. | `gap-skeleton-final.md` L59 | discard test | valid as a range (skill 6c); for Q = S the compact Gaussian model binds at every value above s_1 (F5) | - | F5 |
| d2 | "It needs a small number" sets a tool aside. | reason kind of the skill's 6a; used in row 712 (seen in a `grep` hit: "small number") | discard test | every proved case without exact closure has a small number (C3). Used as a filter it removes every known proof pattern; valid only as a range | - | 2.D |
| d3 | "Abelian only" sets three-dimensional U(1) aside. | `exercise-skill-v2.md` L1213 (quoting row 712) | discard test | the method is Abelian; the pattern (U), (I), (J) of 3.4 is not | - | A1 |
| d4 | "No candidate step is easier than the seed" ends the search for a step. | `gap-skeleton-final.md` L555, L566 | discard verdict | consistent with C1, C6, C7 | - | Step 6 |
| e1 | B1: SU(2) has a gap at every beta. | everywhere | belief | the target is false; the two-phase and massless models of L9 show what that would look like | - | none |
| e2 | B2: the base value is large (above 7). | `gap-skeleton-final.md` L553 | belief | a base below s_1 would escape F5 | yes | a hand estimate on the small torus (the lane has small-volume readings, closed) |
| e3 | B3: one-parameter scaling. | step-scaling candidates of row 720 | belief | sigma does not exist as a function | no | - |
| e4 | B4: no proved precedent. | C8 | belief | a precedent would be a template | yes | a literature item (Step 9) |
| f1 | No computer-assisted steps. | `GOAL.md` | owner rule; obeyed | A5-type proofs verify the criterion by machine; a seed box of tens of correlation lengths is far beyond any machine anyway | no | not used |
| f2 | T0 first, SU(2) first. | `GOAL.md` | owner rule; obeyed | see b2 | - | not used |

**Ranking** (by how much the problem changes if the assumption is dropped), with what the lane would do differently.

1. **b2** (N fixed). The only row whose drop gives a proved pattern for (I). The lane would state (GAP) at large N as a later target. *It would change an owner decision; I name it as a price and do not propose it.*
2. **c1 with c2** (F, and the far base). The lane would stop asking for a step and would state the crux as (I) and (J) of 3.4: a criterion at the scale xi, and the class of effective actions on which it is proved.
3. **a2 with a1** (periodic, global). The lane would test the all-boundary criterion against the proved gauge cases (A3, A4) before another torus quantity.
4. **c4 with c3** (one-way, scalar). The lane would ask what two-sided statement about the effective action at coupling of order one would suffice for a single-scale criterion ((P-c)).
5. **c6** (class-wide). The lane would look for a contradiction at a first bad size along the SU(2) trajectory, using asymptotic freedom below that size.

## Step 5. Compare with the earlier work

The closed list was opened after Step 4. Read first-hand: `gap-phys-seed.md` L151-242 (Part 2: the form, the 14 candidates, the tests), L340-348, L386-405, L428-434; `gap-crux-fp.md` L53-104, L135-145, L174-186, L219-247, L289-310; `gap-seed-check.md` L172-198; `prior/gap-fullread-2.md` L17-34, L172-186; `gap-ds-gauge.md` L1-14. Searched by `grep` over `library/gap-*.md`, `library/prior/gap-*.md`, `library/exercise-skill-v2.md` and `FINISH.md`: the authors of A1 to A9 (13 patterns), "habit", "positive control", "true for a known reason", "full seed", "kappa seed", "two dimensions". The other branches: see 5.3.

### 5.1 Item by item

| Item | In the earlier work? | Where | Scope of the search for "new" |
|---|---|---|---|
| The question itself | yes | `exercise-skill-v2.md` L1211-1216 (row 721, proposal 2) | - |
| The form F | yes; stated more exactly there, with Lemma FLOW (the minimum of sigma(u) - u over the interval carries the flow) | `gap-phys-seed.md` L155-164 (row 720) | I use that statement from here on |
| C1 (no proved case without exact closure has a step in the size) | **partly.** The sources are in the record, as tools that were set aside: Knabe "another setting; excluded by the rate filter", Gopfert-Mack "Abelian only", sharpness "Potts gauge models only", Kopper "N must be large" (`gap-crux-fp.md` L240, L241, L244, L246); Piazza-Shen read in full, "closed doors: two-dimensional" (`prior/gap-fullread-2.md` L17-27, L182; gpt-6-luna, row 719); Dobrushin-Shlosman and Martinelli-Olivieri by a reader's report (`gap-skeleton-final.md` L371). The question "does the proof have a step" is asked of none of them. The opposite is written as a necessity: "A proof in R2 must contain, in some form, the statement that the flow goes one way: a quantity defined at each scale that moves toward disorder under doubling, for every value of the quantity" (`gap-crux-fp.md` L92, row 712). | as cited | the statement not found in the files and patterns above; branches: 5.3 |
| C2 (a step is proved under exact closure, or given the clustering) | **partly.** The contraction of Piazza-Shen is described in `prior/gap-fullread-2.md` L23-27 (credit: that digest; my reading agrees with it). The recursion of Martinelli (Theorems 4.5, 4.6) is not in the record: `gap-ds-gauge.md` L15 says Martinelli-Olivieri were not read by anyone there. | as cited | the recursion: not found by the patterns "Martinelli", "recursive" in the files above |
| C3 (base = sufficiency) | **partly.** "Infinite-volume criteria (Dobrushin, cluster expansion, logarithmic Sobolev) are local and reach only where the coupling between neighbours is small" (`gap-crux-fp.md` L139); the split R1/R2 (L96-99). | row 712 | the form "in every proved case" not found |
| C4, F3 (F is vacuous as logic; the content is the far base) | **partly.** "For them the test is not a filter ... their (SUF) is a theorem" (`gap-phys-seed.md` L234); "the small end is the wrong end for the seed" (L430). | row 720 | the trivial fit with the base at the seed size: not found |
| C5, F4 (monotony in the coupling) | **partly.** A step across couplings is assumption c4 of row 712 (`gap-crux-fp.md` L142); monotony of the Casimir free energy along the coupling is (MONO-Delta), with Proposition NM (`gap-phys-seed.md` L340-348, L401). F4 is a weaker, different remark: the seed set at fixed lattice size is bounded in beta. Its content is in P3 of row 712 (L60: the seed size grows like exp(2.69 beta)). | rows 712, 720 | - |
| C6, F5 (blocked values for a class-wide step) | **partly.** Row 720 has the test (M1): for U(1) "every dimensionless quantity of the torus tends to a constant in L", marked GUIDE for torus quantities, and its reading 1: the proof of the step must use the group "at every value of Q and not only at the weak end" (`gap-phys-seed.md` L173, L232). Added here: for Q1 at ratio 2 a model inside the class K (the compact Gaussian model with R = rho/n) in which Q grows at every value above s_1, argued from the lane's own formula. | row 720; `gap-seed-shape.md` L223-246 | the use of Z_R as a test of a step: not found by "Z_R", "compact Gaussian" outside `gap-seed-shape.md` |
| C7 (Tomboulis; Ito-Seiler) | **yes.** `gap-crux-fp.md` L142, L234; `gap-skeleton-max.md` L130, L336, L361 (read there through a digest and the ar5iv text); `gap-skeleton-max-b.md` L152, L411. Added: Ito-Seiler's Theorem 2.1 and page 6 read first-hand. | rows 669, 670, 712 | found again |
| C8 (no precedent) | **partly**, as a statement about what was read: "No published result read gives an order-one estimate for four-dimensional Wilson SU(2). The closest mathematical analogues are ..." (`gap-skeleton-final.md` L543). | the lead, rows 713, 714 | a belief in both places |
| C9 ((GAP) reads local clustering) | **yes.** Row 731, Theorem EV-L. | `gap-flux-exercise.md` L420-465 | found again |
| b2 (N fixed) | yes | `gap-crux-fp.md` L246 | found again |
| c6 (class-wide) and the first-bad-point form | partly: for beta, "there is no first critical point" (`gap-crux-fp.md` L143) | row 712 | the size version: not found |
| The exact two-dimensional formula (for Step 8) | **yes.** Z = sum over j of (2 I_{2j+1}(beta)/beta)^A (`gap-skeleton-max-b.md` L316); `gap-phys-seed.md` L369. | rows 670, 720 | found again; only the reading as an instance of F is added |
| Z_2 at large beta: the full and kappa seeds (for Step 8) | **partly.** "Expected to hold", not proved (`gap-flux-exercise.md` L337, L519). The counting bounds for the twisted Z_2 partition functions at fixed size are in `gap-seed-check.md` L193-195 (the checker of row 698), used there for the failure of the periodic seed. | rows 698, 731 | a proof for the full or kappa seed: not found by "full seed", "kappa seed", "Z_2" in the files above |

**Correction of my inventory from the earlier work.** (1) Row 720 states F with a uniformity that the row's wording does not show: the step holds "for every L >= L_0, uniformly in j" (the cutoff index), and Lemma FLOW needs the minimum of sigma(u) - u over the whole interval. Step 1's precise version is to be read with this. (2) Row 712 lists more comparison models than my 2.B (the mixed action, SU(N >= 5) at its bulk point, five dimensions; `gap-phys-seed.md` L171-177). They are tests of the kind "T false"; this run adds none of that kind.

### 5.2 What the fresh pass added, and what it found again

Added (all subject to 5.3 for the other branches):

- the table 2.D: each proved case read for the form of its proof, with pages; the answer "exact closure, or given the clustering" for where a step in the size is proved;
- the recursion of Martinelli and Olivieri as a proved (STEP), with its hypothesis (A6);
- Gopfert and Mack's own words on how "all couplings" is reached: an expansion with a small number at every scale, then Guth's inequality (A1);
- Kopper's page 2: at large N the ultraviolet part and the join are not proved (A8);
- F3 (the trivial fit), F5 (the in-class test at every value above s_1).

Found again: C7, C9, b2, the two-dimensional formula, the first-critical-point form, most of C3 and C8.


### 5.3 The other branches

Fetched on 2026-11-11 into a scratch repository of my own (`/tmp/gfe-735/git`, depth 1, no checkout; the working checkout was not touched): main (a527a6fda), and the heads of pull requests 10114 (f76f6c649), 10133, 10134, 10135, 10141, 10144. Pull request 10132 is this branch.

- **Searched.** In pull request 10114: every `.md` file under `.claude/science/toe-ruleset-20261021/agents/ym4d-*/` (about 1,190 files), for the pattern "Knabe, Nachtergaele, Stroock, Martinelli, Gopfert, Kopper, Piazza, Duminil, one-way step, step scaling, Migdal, Ito and Seiler, finite-size criteri, positive control, exact closure" (case-insensitive). In main and in 10133, 10135, 10141, 10144: the text files whose path contains "ym4d" or "yang-mills", outside the folder of 10114 (21, 4, 4, 53 and 21 files), for the same pattern without the last two terms.
- **Not searched.** The `.py`, `.json` and `.txt` files of 10114; the copy of the 10114 folder inside 10133 where it differs from 10114; pull request 10134, which holds an older copy of this lane's folder (317 files) that the search of this branch covers only if nothing was deleted since; all files of main whose path has no "ym4d" or "yang-mills" (about 92,000).
- **Hits.** Main, 10133, 10135, 10141, 10144: none. Pull request 10114, three that touch this run:
  1. `RTARGET.md` L38-41 (and `PROOF.md` L2729): "As of 1999 the UV analysis of the full 2D O(N) model had 'so far only [been] performed in the hierarchical case' (Kopper ...). So the 2D testbed is itself an open construction, not a solved template." **This is the observation of A8 and of 3.3, made earlier there.** Credit: the lead of the soft-kernel route (PR 10114).
  2. `checks/review_massgap_block_literature.md` L111-118: a later note of Ito and Seiler (arXiv:0901.4246) read in full there; it "separates two obligations in a Migdal-Kadanoff-type route: actual flow to strong coupling and a common interpolation parameter controlling twisted and untwisted partition functions"; "a useful warning ... not a no-go theorem for all RG mechanisms". Consistent with A9; I did not read 0901.4246.
  3. `PROOF.md` L5755-5757: a Migdal-Kadanoff SU(2) toy in four dimensions used as a finite diagnostic. Not a statement about the form.
  The other hits are the words "positive control", "step scaling" and "Stroock" in unrelated places (rotation, sphere and seam notes); I read the file names and counts, not each line.
- **Result for the "new" marks.** No statement of 5.2 was found in the searched part of the other branches, except the Kopper observation (hit 1). The marks of 5.1 stand with this scope written next to them: "not found in this branch's `library/`, `library/prior/`, `FINISH.md`, and in the searched part of 10114, main, 10133, 10135, 10141, 10144".

## Step 6. The blockage: discard tests and set-aside methods

### 6a and 6d. Every method set aside, and its verdict re-judged

Two lists exist: the 22 methods of row 712 (`gap-crux-fp.md` L223-246, read first-hand; that table was itself built from digests) and the 14 flow candidates of row 720 (`gap-phys-seed.md` L187-215, read first-hand). Row 712 re-judged its 22 (L291-308) and row 731 re-judged all 36 for (G_ev) (`gap-flux-exercise.md` 6a; not re-read here). I re-judge them for one question only: does the verdict rest on the form F, or on the necessity claim of `gap-crux-fp.md` L92? "As reported" = valid as reported; not re-derived.

| # | Method (authors) | Reason given | Kind | Re-judged for this question |
|---|---|---|---|---|
| 1, 2 | Griffiths-type inequalities; dual forms with positive weights | hold for Z_2 and U(1) | U(1) | as reported. A7 and A1 show what such inequalities give where they exist: monotony in the coupling and a dichotomy, not a step in the size. By F4 monotony in the coupling carries a seed toward strong coupling only. |
| 3 | A monotone quantity along the scale (kappa; (CAS); step scaling) | exists for every group; strictness restates the seed | restates | **valid, and now with a test at each value**: F5 for Q = S. |
| 4 | Derivative in beta ((VIR_K), (DEF_K)) | three ways failed | gap; wrong quantity | as reported |
| 5, 6, 7 | Bakry-Emery; Dobrushin on one link; cluster expansion | need small beta | small number | as reported. These are the proved cases A4; in them base = sufficiency (C3). |
| 8 | Zeros of Z in complex beta | the radius shrinks with the gap | gap | as reported |
| 9 | Polchinski flow; two-scale log-Sobolev criteria | a Hessian bound at every scale | U(1); unverified | as reported. A2 is the one case where the two-scale method reaches all couplings, and it rests on exact closure. |
| 10 | Migdal-Kadanoff bounds (Tomboulis) | an unproved inequality; would confine U(1) | U(1) | valid (A9, read first-hand). **This is the form F itself**, in the lane's own setting. |
| 11 | Simon-Lieb; Aizenman-Simon | spin system | U(1) | as re-judged by row 712 (not valid in R1) |
| 12 | Infrared bounds | prove order | wrong quantity | as reported |
| 13 | Durhuus-Frohlich | orders at large beta | large beta | as re-judged by row 712 |
| 14 | Loop equations, bootstrap | numerical | rule f | as reported |
| 15 | Twist ratios; (TUBE'); Mack-Petkova | premise open | open | as reported |
| 16 | Knabe; Lemm-Mozgunov | another setting; rate filter | setting | valid as a verdict on the tool. As a control (A5): (SUFF) at one size, verified at that size. |
| 17 | Gopfert-Mack | Abelian only | setting | valid as a verdict on the tool. **As a control it was not used**: it is the one proved case with a correlation length that grows like exp(c beta), and it has no step (A1). |
| 18 | Small-volume spectrum (Luscher; Koller-van Baal) | small volume only | setting | as reported. It is the (BASE) of F. |
| 19 | Curvature of the orbit space | heuristic | unverified | as reported |
| 20 | Random-cluster sharpness (Duncan-Schweinhart) | Potts gauge models only | setting | valid; not read here. A7 is the same pattern for spins. |
| 21 | Mixing hypotheses on a box, (W), (DS-tw) | a hypothesis | open | as reported. A6: for spin systems this form is necessary as well as sufficient. |
| 22 | Large N (Kopper) | N must be large | small number | valid. As a control (A8): the mass is proved with a second small number, and the join with the ultraviolet flow is open even there. |
| Q1, Q2, Q2', Q3, Q4 | Class I flow candidates | (STEP) restates the seed | restates | valid. F5 adds: for Q1 no class-wide step exists at any value above s_1. |
| Q5 to Q8 | twist ratio; Schrodinger functional; twisted Polyakov loop; force | the flux half at most; fail at a point with two confining phases | wrong quantity | as reported |
| Q9 to Q12 | gradient flow; two-point coupling; plaquette shift; kappa | local, not one-way, or not strict | wrong quantity | as reported |
| Q13 | lowest zero-flux gap of a twisted box | (STEP) false at weak coupling in SU(2) itself | fails | as reported (a recalled one-loop number) |
| Q14 | Route T, thin torus with a twist | crux (AC') open | open | as reported |

**Where the verdicts matter.** None of the 36 verdicts changes. What changes is the status of one sentence that sits above them (6c, N1).

### 6b. First principles on the blockage

From the definitions: a tool for T must verify a clustering criterion for a box of at least 12.9 correlation lengths (L4), or a local criterion at a scale of order xi. The proved cases verify such a criterion in four ways (C3). The least property of the model that a tool must use is one that makes one of the four available at the scale xi. **The blockage in one sentence: every proved way to verify a clustering criterion at its own scale uses a small number at that scale, exact closure, or a correlation inequality with a parameter, and none of the three is known for SU(2) at the scale xi.** *reading of 2.D; "every proved way" means the cases A1 to A10.*

### 6c. The tests in their logical form

**Tests of the kind "T false" (they bind a tool).** The lane's list (`gap-phys-seed.md` L171-177; `gap-crux-fp.md` L70-76) stays as it is. This run adds one row and sharpens one.

| Test (model M') | Class | The exact T that fails in M' | How the failure is known | What a tool must use to pass | From which value it binds |
|---|---|---|---|---|---|
| The compact Gaussian model Z_R with R = rho/n, rho >= 1/2 | K (`gap-seed-shape.md` L229-241) | "S(n; (2n)^3) = x implies S(2n; (4n)^3) <= sigma(x) < x" | argued (F5), for the continuum form of the lane's formula; the lattice correction is not written; s_1 is a guide | a property that this model lacks. It has a continuous symmetry (shifts of the field) and a zero mode whose level spacing is 1/(R^2 V). | every value x >= s_1 |
| The Ising model with two phases | K | the same at x = 1 | S -> 1 proved in the lane; "no gap" and the limit along sizes recalled | uniqueness of the vacuum in the sector that is summed | the value 1 |

**Tests of the kind "T true" (the positive controls).** By the skill's rule a pass is no support for a tool. A model where T is true tests something else: a *necessity claim*, that is, a sentence "every proof of T must contain X". Such a claim is refuted by one proved case of T whose proof has no X. The lane's necessity claims, tested:

| # | Necessity claim | Where | Control | Verdict |
|---|---|---|---|---|
| N1 | "A proof in R2 must contain, in some form, the statement that the flow goes one way: a quantity defined at each scale that moves toward disorder under doubling, for every value of the quantity." | `gap-crux-fp.md` L92; it became the form F of row 720 | A1 (the correlation length grows like exp(c beta); many scales are crossed; no such quantity appears in the argument as the authors describe it); A8 (the same with 1/N) | **too strong as a claim about proofs.** Valid form: the *theorem* T implies a monotone flow trivially (F3), so "in some form" is true and empty. A proof may cross the scales by a two-sided control of the effective action with a small number (A1), and may verify the criterion at the scale xi with a second small number (A8). What comes back: the split (U), (I), (J) of 3.4 as the statement of the crux, in place of a step. Limit of this verdict: the controls were read in part (introductions), and both use a small number that SU(2) lacks. |
| N2 | (GAP) needs the seed on the whole space, flux included. | row 712, a2 | Z_2 at large beta | corrected by row 731 (found again) |
| N3 | The seed needs a box of at least 7.4 (12.9) correlation lengths. | `gap-crux-fp.md` L55 | none needed | a theorem for the seed (P1). For other criteria it is not a necessity: row 712, c1 says so. |
| N4 | "One number cannot be enough ... what matters is how a quantity changes when the size doubles." | `gap-crux-fp.md` L62 | A3, A4, A7: a criterion at one finite set or one scale | valid for the periodic free energy (every single box has a gap). Too strong in general: the criteria phi_beta(S) < 1 (A7) and the conditions of A3, A4, A6 are one-size statements. They are not partition functions of periodic boxes. |

**Are the tests enough?** For tools: Step 2 names no model that the lane's list lacks. For necessity claims the lane had no test before this run; the controls A1 to A10 are the first.

**The other kinds of reason, in the valid form.** "Needs a small number" (5, 6, 7, 22): valid as a range only, and by C3 it is true of every proved case without exact closure, so as a filter it leaves only exact closure and correlation inequalities. "Other setting" (16, 17, 20): the hypothesis that fails is named in each row of 2.D (frustration-freeness; an Abelian duality; a positive cluster representation). "Was tried": not used.

## Step 7. Routes: generate, try to kill, rank

`docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md` was read in full before this step. No subagents: the passes below are separate passes of one session, and they are not independent.

**Exact target contract (governance).** Target: T of Step 1 (a seed of one of three kinds at one physical size, uniformly in the cutoff; or (G_ev)). Domain: Wilson SU(2), four dimensions, the trajectory of the account. Allowed premises: the lane's checked statements; the account as cited. Forbidden weakenings: a fixed beta; a hypothesis that restates the seed; a numerical step. Edge cases: two dimensions; Z_2 at large beta; SU(2) at small beta; U(1) at weak coupling; the two models of 6c. Completion witness: a written proof. Not closure: a map of routes; a reduction to a target-equivalent statement.

### 7.1 Routes

Sources: the first five assumptions of Step 4 (b2 left out: an owner decision), the corrected claim N1, C3, and the "least a tool must use" of 6b.

| Route | Family (object; mechanism; terminal obligation) | Assumption changed | What one would have to believe | First artifact | Cost | What it would change |
|---|---|---|---|---|---|---|
| A | effective action at the scale xi; a single-scale criterion with a two-sided hypothesis; (I) and (J) of 3.4 | c1, c2, c4 | that a hypothesis on block variables at coupling of order one exists that a single-scale argument can use, and that the flow lands in it | the exact statement (P-c) | a long author run with no mechanism | the crux is stated as in every proved multi-scale case |
| B | all boundary values of one box, for centre-blind functions; Dobrushin-Shlosman; the mixing hypothesis | a2, a1 | that the influence of a boundary value decays for every boundary value | a test on the proved gauge cases: does the hypothesis hold for Z_2 at large beta? | one short test | whether row 691's form can be the crux |
| C | the SU(2) trajectory; contradiction at a first bad size; (Z-UNB) | c6 | that "no seed at any size" contradicts a property that the account proves below that size | Theorem ZD (row 720) is the reduction; the contradiction has no mechanism | - | - |
| D | a correlation inequality with a parameter; a dichotomy "a seed at some size, or order" (A7) | c5 | that Wilson SU(2) has a positive graphical representation, or a monotone order parameter | a search for such an inequality for the centre-even sector | one reading item, then a short author run | the only pattern among the controls that reaches a large correlation length without a small number |
| E | the lane's own class K on a proved case; Theorem S-w; the full and kappa seeds of Z_2 at large beta at N = 3 | none (a control) | nothing | Proposition Z2 (Step 8) | one hour | the filter "Z_2 at large beta" goes from recalled to argued; a proved instance of base = sufficiency inside the lane's frame |
| F | the literature; a counterexample to belief B4 | e4 | that some proved gap has a large correlation length with no small number, no exact closure and no correlation inequality | a reading item with a list of candidates | one reading lane | a template, if one exists; if none, C8 is better founded |
| G (misframing pass) | the question; "is there a step?" replaced | c1 | - | the replacing question, 7.4 | - | the brief of the next author run |

**Lenses.** Chosen from the structure of the wall (a flow across scales with no small number). *Dynamical systems:* the object is the step map on dimensionless torus quantities; the theorem type is a Lyapunov function, which excludes fixed points without computing the flow. The known one in four dimensions is the a-theorem (recalled: Komargodski and Schwimmer): it orders the two ends and does not exclude a free massless end, so it gives no gap. Toy: the two-dimensional c-function does not prove the gap of O(3) either. Found empty for T. *Probability, coupling (the outside lens):* A3 proves clustering by a swap of two independent copies on a set where the defect clusters of the two copies do not connect the two regions; the object would be a "defect" of SU(2) at the scale xi with a small density. None is known; this is route A in another language. *Logic:* Gosset and Mozgunov recall that the gap is undecidable for general two-dimensional Hamiltonians (their page 2); so a finite criterion that is necessary and sufficient cannot exist for a class that large. It bears on "necessity" claims only. *Convexity, variational:* in use (Lemma K). *Operator algebras, topology, number theory, categories:* considered; nothing to state.

**Reframes tried.** *Exact theorem against bounded theorem:* a gap for a fixed, large but finite range of beta at fixed N is what A8 gives for O(N); the analogue here would be the seed for beta in [beta_1, beta_2] by one two-sided expansion with no continuum statement. It is weaker than T and does not need the join (J). I record it; I did not try it. *Finite carrier against limiting family; local against global:* 3.5.

### 7.2 The kill pass

| Route | Assumes the target? | Contradicts a checked result? | Tried before (Step 5)? | Fails a test of Step 6 in the valid form? | Breaks a rule? | Terminal obligation target-equivalent? | Verdict |
|---|---|---|---|---|---|---|---|
| A | no | no | named as "what the account would need" (`gap-skeleton-final.md` L564; `gap-phys-seed.md` Part 4) | no | no | (P-c) is stronger than the seed in what it controls, and no mechanism exists | **blocked-equivalent.** A statement of the crux, not a route. |
| B | no | no | row 691 owns (DS-tw), a hypothesis | **the unrestricted form fails a positive control, by a sketch:** in Z_2 at large beta a boundary value with a loop of frustrated plaquettes on the boundary forces a sheet of frustrated plaquettes across the box, so the law of a plaquette at the centre depends on a boundary value at distance of the box size. (GAP) holds there (A3). So "for every boundary value" is not necessary and is false in a model where the target is true. *Sketch, not proved: I did not show that the sheet passes the centre with probability near one.* It is the gauge form of the remark in A6 that strong mixing fails for some volumes in the ordered Ising model. | no | not shown | **wounded:** the criterion must restrict the boundary values (typical, or twisted as in row 691), and then its verification is open at order one. |
| C | no | no | row 720, Theorems ZD, ZD-c | - | no | (Z-UNB) with (BDD-Delta) is equivalent to the seed (given row 720, unchecked on 2026-11-11) | **blocked-equivalent.** |
| D | no | no | row 712, methods 1, 2, 20: "no such inequality or dual form is known for SU(2)"; row 733, Lemma NP: the Z_2 splitting has no pointwise sign (`gap-kappa-order.md` L54) | F4: monotony in the coupling carries a seed toward strong coupling only; the dichotomy form is not excluded by F4 | no | unknown | **wounded:** no positive representation is known, and one sign obstruction is proved. |
| E | no | no | partly (5.1, last row) | - | no | off the path of T (a control) | **survives**; done in Step 8. |
| F | no | no | the digests ranked sources as tools, not as precedents | - | no | - | **survives** as a reading item. |
| G | - | - | - | - | - | - | gives 7.4 |

### 7.3 Rank and registry

| Rank | Route | Family | Terminal obligation | Strength against T | Status (governance) | Concrete evidence | Stop or reopen condition |
|---|---|---|---|---|---|---|---|
| 1 | E | class K on a proved case | Proposition Z2 | weaker (a control) | active; done in Step 8 | 8.1 | - |
| 2 | F | literature precedent | a proved case of the kind of B4 | unknown | unexplored | - | stop if the listed candidates all have a small number, closure or an inequality |
| 3 | D | correlation inequality, dichotomy | a positive representation for the centre-even sector of SU(2) | unknown/comparable | blocked-local | `gap-kappa-order.md` Lemma NP | reopen if a signed-weight form of the switching lemma, or a positivity after averaging over the SO(3) part, is found |
| 4 | B | boundary values | a restricted mixing hypothesis at one physical size | stronger or comparable | blocked-local (row 691 owns it) | the Z_2 sketch of 7.2 | reopen with a class of boundary values that passes the Z_2 control |
| 5 | A | effective action at scale xi | (P-c) | target-equivalent or stronger | blocked-equivalent | A8: not proved even at large N | reopen if a second small number is found for SU(2) at the scale xi |
| 6 | C | first bad size | (Z-UNB) | target-equivalent | blocked-equivalent | row 720 | reopen with a property of the account that "no seed" contradicts |
| - | the form F (a step for a torus quantity) | torus quantity; one-way inequality; a step at every value | target-equivalent at each value (row 720), and blocked at every value above s_1 for class-wide tools (F5) | - | **retired as the default brief**; blocked-equivalent | A9; C1; F5 | reopen if a step is found whose proof uses a property that the compact Gaussian and two-phase models lack, at one value above s_1 |

### 7.4 The replacing question (the misframing pass)

The lane asked: "which torus quantity has a one-way step from a small size to the seed size?" The proved cases answer a different question: **"at which scale, and by which of four means, is the criterion verified?"** The four means are: a small number at that scale; a second small number that survives to the scale xi after an exact change of variables; exact closure; a correlation inequality with a parameter. For Wilson SU(2) at the scale xi none of the four is known, and for each the reason can be named: the coupling is of order one; no dual or large-N variable is known; block integration does not close (it makes larger loops); the known positive representations fail by a sign (Lemma NP of row 733). *reading; this is a map and a price, not a proof that no fifth means exists.*

## Step 8. Real attempts

Budget: about two hours. Before each attempt I searched `library/open-core.md`, `library/open-registry.md` and the FINISH rows for the statement (patterns: "kappa", "full seed", "Z_2", "G_ev", "EV-STEP"): no row holds the statements of 8.1 or 8.2.

### 8.0 A guide run for F5, registered before it was run

**What is run.** The oscillator product of the compact Gaussian model on the lattice, Pi_m := product over the non-zero momenta k of the periodic cube of side 2m of (1 - exp(-m eps_k))^(-1), with 2 cosh(eps_k) = 2 + sum over i of (2 - 2 cos(2 pi k_i/(2m))) (`gap-seed-shape.md` L225, L237), for m = 3, 4, 6, 8, 12, 16, 24. By F5 the two theta factors at rho >= 1/2 give a factor of at least 1.99 when the size doubles, and they do not depend on m. So on the lattice S(2m) > S(m) at every rho >= 1/2 if Pi_{2m}/Pi_m > 1/1.99.

**Pass (registered 2026-11-11, before the run):** Pi_{2m}/Pi_m >= 0.51 for m = 3, 4, 6, 8, 12. Then F5 holds on the lattice at these sizes (a guide, not a proof for all m). **Fail:** a ratio below 0.51 at one of these m. Then the lattice remark in F5 is wrong at that size, and F5 stands for the continuum formula only. The run also prints s_1(m) = theta(1/4) theta(pi^2)^3 Pi_m - 1, the value of S at rho = 1/2. A run decides nothing; it can refute the lattice remark.

**Result of the run (2026-11-11, 22:27Z; numeric lock held, holder `gfe-735-fable`; memory free 54 percent; one thread; script `/tmp/gfe-735/scripts/zr_step.py` on the Mac mini, printed in 9.8; not in the repository).**

```text
m= 3  Pi=3.013613  s_1=9.6863      ratio Pi_6/Pi_3   = 0.610308  pass
m= 4  Pi=2.284136  s_1=7.0996      ratio Pi_8/Pi_4   = 0.759396  pass
m= 6  Pi=1.839234  s_1=5.5219      ratio Pi_12/Pi_6  = 0.911387  pass
m= 8  Pi=1.734563  s_1=5.1508      ratio Pi_16/Pi_8  = 0.955936  pass
m=12  Pi=1.676253  s_1=4.9440      ratio Pi_24/Pi_12 = 0.981805  pass
m=16  Pi=1.658131  s_1=4.8797
m=24  Pi=1.645753  s_1=4.8359      theta(1/4) theta(pi^2)^3 = 3.546008      RESULT: PASS
```

Reading, as registered: **pass.** At the tested sizes the lattice form of F5 holds: for rho >= 1/2 the thermal sum of the compact Gaussian model grows when the size doubles (factor at least 1.99 x 0.61 = 1.21 at m = 3). s_1 is about 4.8 for large m (guide). The run did not move the wall. It supports the remark that the test of F5 binds on the lattice too; it proves nothing for other m. No adversarial check of this run was made; it is a positive guide, not a negative conclusion.

### 8.1 Proposition Z2: in Z_2 gauge theory at large beta the full seed and the kappa seed hold at N = 3. A control; off the path of T0.

**Why.** Row 731 expects this and does not prove it (`gap-flux-exercise.md` L337, L519). It is the proved case nearest to ours inside the lane's own frame: a four-dimensional gauge theory, the periodic seed false, (G_ev) true. The question of this run is how the seed is reached there.

**Setting.** Torus n with all sides at least 3, |n| sites, 4|n| links, link variables sigma_l in {+1, -1}, plaquette variable sigma_p = the product of the four links. For a twist k in Z_2^6 with signs s^k_p as in `gap-flux-exercise.md` L111:

Z^k(n) := sum over all sigma of the product over p of exp(-beta (1 - s^k_p sigma_p)), x := exp(-2 beta).

A plaquette is *frustrated* (for k) if s^k_p sigma_p = -1. So Z^k(n) = sum over sigma of x^(number of frustrated plaquettes). W_full(n) := (1/8) sum over k of Z^k(n), W_kappa(n) := (1/8) sum over k of (-1)^Pf(k) Z^k(n) (Proposition CL (b)).

**Input (not written in the lane).** (TM-tw-Z2): the statements (TM-tw), Lemma W and Theorem S-w of `gap-flux-exercise.md` L115, L503-513 for this model. The lane states that Theorem S holds for every group (`gap-crux-restate.md` L227) and uses the Z_2 transfer operator once, unwritten (`gap-seed-check.md` L191). For Z_2 the operators are finite matrices with positive entries. I use one consequence: 1 + S_w(N; (2N)^3) <= exp(Phi_w(N)), Phi_w(N) = 16 log W_w(N^4) - log W_w((2N)^4), for w = full, kappa.

**Lemma Z2-a (flat configurations).** On the torus with sides m_1, ..., m_4 >= 2 and V = m_1 m_2 m_3 m_4 sites, the number of sigma with every sigma_p = +1 is 2^(V+3).

Proof. *At least.* For g: sites -> {+1, -1} put sigma_xy = g_x g_y; every plaquette is +1. Two functions g give the same sigma only if they differ by a global sign (the torus is connected): 2^(V-1) configurations. For a set A of directions let Z_A flip every link (x, mu) with mu in A and x_mu = 0. A plaquette in a plane (mu, nu) holds two mu-links with the same coordinate x_mu and two nu-links with the same x_nu, so Z_A changes no plaquette. The product of sigma along a straight closed line in direction mu does not change under g and changes sign under Z_A exactly when mu is in A. So the 16 maps Z_A applied to the 2^(V-1) pure gauges give 16 x 2^(V-1) different flat configurations.
*At most.* Tree T: the links (y, 1) with y_1 <= m_1 - 2; the links (y, 2) with y_1 = 0, y_2 <= m_2 - 2; the links (y, 3) with y_1 = y_2 = 0, y_3 <= m_3 - 2; the links (y, 4) with y_1 = y_2 = y_3 = 0, y_4 <= m_4 - 2. It has (m_1 - 1) m_2 m_3 m_4 + (m_2 - 1) m_3 m_4 + (m_3 - 1) m_4 + (m_4 - 1) = V - 1 links and joins every site to 0 by one path. For every sigma there is exactly one g with g_0 = 1 such that the gauge transform of sigma is +1 on T. So the number of flat sigma is 2^(V-1) times the number of flat sigma that are +1 on T. Let sigma be such a configuration. Call a link (y, mu) *inner* if y_mu <= m_mu - 2. (i) Every inner link is +1. For mu = 1 they are in T. For mu = 2, by induction on y_1: y_1 = 0 is in T; the (1,2)-plaquette at y - e_1 holds the links (y - e_1, 1) and (y - e_1 + e_2, 1), which are inner 1-links, and (y - e_1, 2) and (y, 2), so sigma(y, 2) = sigma(y - e_1, 2). For mu = 3: by induction on y_2 at y_1 = 0 with the (2,3)-plaquettes (their 2-links are inner), then on y_1 with the (1,3)-plaquettes. For mu = 4: the same with one more induction. (ii) Let (y, mu) have y_mu = m_mu - 1, and nu != mu with y_nu <= m_nu - 2. The (mu, nu)-plaquette at y holds (y, mu), (y + e_nu, mu) and two inner nu-links. So sigma(y, mu) = sigma(y + e_nu, mu). Hence sigma is one sign h_mu on all links (y, mu) with y_mu = m_mu - 1. There are at most 16 such sigma. QED

**Lemma Z2-b (the twisted sectors).** Let k != 0, with k_{mu nu} = 1, and let rho, tau be the other two directions. Every sigma has at least n_rho n_tau frustrated plaquettes for k. So Z^k(n) <= 2^(4|n|) x^(n_rho n_tau).

Proof (the argument of `gap-seed-check.md` L193-195, row 698's checker). Fix the coordinates x_rho, x_tau: a two-dimensional torus of (mu, nu)-plaquettes. Each of its links lies in exactly two of its plaquettes, so the product of sigma_p over it is +1. It holds exactly one plaquette of the stack of (mu, nu) (base point x_mu = x_nu = 0), and no plaquette of another stack. So the product of s^k_p sigma_p over it is -1, and it holds a frustrated plaquette. There are n_rho n_tau such tori, with disjoint sets of plaquettes. QED

**Lemma Z2-c.** For the symmetric torus of side m, V = m^4: 2^(V+3) <= Z^0 <= 2^(V+3) + 2^(4V) x, and

2^V <= W_full <= 2^V (1 + 2^(3V+3) x),  2^V (1 - (7/2) 2^(3V) x^(m^2)) <= W_kappa <= 2^V (1 + 2^(3V+3) x).

Proof. Z^0: the flat configurations have weight 1 (Lemma Z2-a), every other has weight at most x, and there are 2^(4V) configurations. For k != 0, 0 < Z^k <= 2^(4V) x^(m^2) <= 2^(4V) x (Lemma Z2-b). W_full: the lower bound keeps k = 0; the upper bound is (1/8)(2^(V+3) + 64 x 2^(4V) x). W_kappa: Pf(k) = k_12 k_34 + k_13 k_24 + k_14 k_23 is 1 for exactly 28 of the 64 twists (count: the number of (a, b) in Z_2^3 x Z_2^3 with a.b = 1 is 7 x 4 = 28), and Pf(0) = 0. So W_kappa >= (1/8)(Z^0 - 28 x 2^(4V) x^(m^2)), and W_kappa <= (1/8) sum over k of Z^k. QED

**Proposition Z2.** Given (TM-tw-Z2). For Z_2 gauge theory on four-dimensional tori and every beta >= 91:

S_full(3; 6^3) < 1/5041 and S_kappa(3; 6^3) < 1/5041.

Hence, by Corollary EV: (G_ev) holds along every sequence of sides, and every limit point of the periodic symmetric tori clusters exponentially on the centre-blind local functions, in all four directions, at the rate m_0 = log(1/(5041 s))/3, which is at least (2 beta - 182)/3 for beta >= 91.5. For general N >= 3 the two seeds hold at N when beta >= ((3 N^4 + 7) log 2 + 9)/2.

Proof. N = 3, V = 81 at side 3 and V' = 1296 at side 6. Full: Phi_full(3) <= 16 log(1 + 2^(3V+3) x) - 0 <= 2^(3V+7) x = 2^250 x, because log W_full((2N)^4) >= 16 V log 2 and 16 log W_full(N^4) <= 16 V log 2 + 16 log(1 + 2^(3V+3) x). Now 250 log 2 < 173.29 and log(1/(1.9 x 10^(-4))) < 8.57. So for 2 beta >= 181.86, that is beta >= 90.93: Phi_full(3) <= 1.9 x 10^(-4), and exp(1.9 x 10^(-4)) - 1 < 1.91 x 10^(-4) < 1/5041. Kappa: Phi_kappa(3) <= 2^250 x - log(1 - (7/2) 2^(3V') x^36). For beta >= 91: 2^250 x <= exp(173.29 - 182) = exp(-8.71) < 1.65 x 10^(-4), and (7/2) 2^3888 x^36 <= exp(1.26 + 2695.0 - 6552) < 10^(-1000), so the last term is below 10^(-999). Sum below 1.9 x 10^(-4). The rate: s <= exp(Phi) - 1 <= 1.001 x 2^250 x, so 5041 s <= exp(8.53 + 0.001 + 173.29 - 2 beta) <= exp(182 - 2 beta). General N: the same with V = N^4; the kappa term needs 8 beta N^2 > 48 N^4 log 2 + 2, which the stated bound gives for N >= 3: it gives 2 beta > 3 N^4 log 2, so 8 beta N^2 > 12 N^6 log 2 = (N^2/4) x 48 N^4 log 2 >= 2.25 x 48 N^4 log 2. QED

**Standing.** argued (Claude Fable 5.2, not checked), given (TM-tw-Z2), which is not written anywhere in the lane, and given Corollary EV (checked for SU(2); its proof uses only the class properties and (L), whose Z_2 form is also not written). The arithmetic is by hand: 250 x 0.693148 = 173.287; -log(1.9 x 10^(-4)) = 8.568; 3888 x 0.693148 = 2694.96; 72 x 91 = 6552; log 5041 = 8.525.

**What it shows for this run.**

1. *A consistency test of the lane's machinery on a proved case.* The conclusion (exponential clustering of functions of plaquettes at large beta) is a theorem of Forsstrom (A3: for 30 exp(-4 beta) < 1, with a rate of about 4 beta per lattice unit). Corollary EV gives the weaker rate (2 beta - 182)/3 on a smaller range. No contradiction. Had the full seed implied a false statement here, Corollary EV would have been refuted.
2. *The form.* The seed is verified at the lattice scale, at the size N = 3 where it is used, by a small number. Base = sufficiency. There is no step. The periodic seed is false in the same model (`gap-seed-check.md` L191-195: s >= 7 - o(1) at fixed size), so the choice among the three seeds is the whole content here: the choice of the phase.
3. *It moves the wall in no direction for SU(2).* It turns "expected" (row 731) into "argued, given (TM-tw-Z2)", and with it the corrected Z_2 test of row 731 has a proof inside the lane for the first time (for the range beta >= 91; the true range is far larger).

### 8.2 Remark 2D: the form F in two dimensions (found again; the reading is added)

For two-dimensional Wilson SU(2) on the torus of sides a, b: Z(a, b) = (bulk factor)^(ab) sum over j = 0, 1/2, 1, ... of c_j^(ab), with c_j = I_{2j+1}(beta)/I_1(beta) in (0, 1) for j > 0 (`gap-skeleton-max-b.md` L316, `gap-phys-seed.md` L369; recalled there, not re-derived here). So the transfer operator of the circle of length b has the eigenvalue ratios c_j^b, each once, and

S(a; b) = h(ab), h(A) := sum over j > 0 of c_j^A.

The thermal sum depends on the area only. Put Q(L) := S(L/2; L) = h(L^2/2). Then: (BASE) Q(L_0) = h(L_0^2/2) is finite at every size; (STEP) Q(2L) = h(4 x L^2/2) = sigma(Q(L)) with sigma := h(4 h^(-1)(.)), and sigma(x) < x for every x > 0 because h is strictly decreasing; in particular Q(2L) <= c_{1/2}^(3 L^2/2) Q(L); (SUFF) Corollary S2 of `gap-crux-restate.md` L215: Q <= 1/20. So F fits, at every beta, with an exact step at every value. *argued, given the recalled character formula.*

Why it fits: the partition function of every torus is a function of one number, the area, and the whole flow is the one function h. This is exact closure in its plainest form, and it is the same fact that carries A2 (the block weight is w^{*n}). In four dimensions the torus (n_1, ..., n_4) has no such reduction, and block integration leaves the family of plaquette weights.

### 8.3 What was not attempted, and what each deferred test waits on

- Route F (a precedent against B4): a reading item; it waits on the lead and a reading lane (work item 2).
- Route B: the sketch of 7.2 (failure of the unrestricted all-boundary criterion in Z_2 at large beta) was not proved. The smallest test: a Peierls bound for the sheet spanned by a boundary loop in a box of side 4. It waits on a decision whether row 691's form stays on the list at all.
- Route D: not attempted; Lemma NP of row 733 is the known obstruction.
- (TM-tw-Z2) was not written. It waits on work item 3, and it is worth doing only if Proposition Z2 is to be kept as a library control.

**Summary of Step 8.** One proposition with a proof (8.1, a control, off the path of T0), one remark (8.2), one guide run with its registered reading (8.0, pass). None moves the wall for SU(2).

## Step 9. Report

Every claim carries a mark. "argued" = proved in this file by Claude Fable 5.2, not checked by another model. "reading" = my reading of a source, with the pages of 2.A.

### 9.1 The wall, in plain words (corrected)

We want to show that the lightest particle has a positive mass. The plan needs one inequality on one large box, many particle wavelengths wide. Our account controls only very small boxes. So the lane gave every tool one shape: a number that is known on a small box and can only improve each time the box is doubled. This exercise looked at the models where a positive mass, or the decay of correlations, is proved, and asked whether those proofs have that shape. They do not, with two kinds of exception: models in which the doubling can be done exactly (two dimensions; a simplified model), and a doubling rule that takes the decay of correlations as already known. Every other proof checks its criterion directly at the scale where it is used. It can do so because something is small at that scale, or because of a special inequality that our theory is not known to have. So the doubling rule is a habit of the lane. Dropping it opens no door by itself: what is missing is the thing that makes a direct check possible.

### 9.2 What the exercise found

1. **None of the proved cases read has the form, outside exact closure** (C1, C2; reading; table 2.D; each source read in part). Ten families were read from open copies. A one-way step in the size is proved in two-dimensional gauge theory (Piazza and Shen; the exact formula) and in the Migdal-Kadanoff model (recalled), where block integration is exact, and in the recursion of Martinelli and Olivieri, whose hypothesis is the clustering itself. Three-dimensional U(1) (Gopfert and Mack), strong coupling, finite groups at weak coupling, the criteria of Knabe and Nachtergaele, sharpness (Duminil-Copin and Tassion) and O(N) at large N (Kopper) have none.
2. **In all of those the criterion is verified at its own scale** (C3; reading). What makes that possible is one of four things: a small number at the lattice scale; a second small number that survives to the correlation length after an exact change of variables (the monopole activity; 1/N); exact closure; a correlation inequality with a parameter, which gives a dichotomy "a criterion at some size, or order".
3. **The form is empty as logic** (F3; argued). Every model with a seed fits it with the base at the seed size. Its content is one clause: the base lies far below the seed size. That clause comes from the method (the account stops at small tori). The target does not ask for it.
4. **The form was tried once in exactly this setting, and it failed where it had to tell SU(2) from U(1)** (C7; found again in rows 669, 670, 712; Ito and Seiler read first-hand here).
5. **For the lane's own quantity, no step can be proved from the properties of the class at any value above about 4.8** (F5; argued for the continuum formula of `gap-seed-shape.md`; the number is a guide; a registered guide run passes on the lattice for sizes 3 to 24).
6. **A proved control inside the lane's frame** (Proposition Z2; argued, given the Z_2 transfer operator, which the lane has not written). In Z_2 gauge theory at beta >= 91 the full and the kappa seed hold at N = 3. Corollary EV then gives the clustering that Forsstrom proved by other means: the lane's machinery passes a test on a case with a known answer. The seed is reached there with no step.
7. **What changed since the start.** Nothing for SU(2): no seed, no step, no gap. What changed is the brief (9.4, 9.5) and one sentence of row 712 (9.3).

### 9.3 Filters corrected

- **N1, a necessity claim** (`gap-crux-fp.md` L92, row 712; the origin of the form F of row 720): "A proof in R2 must contain, in some form, the statement that the flow goes one way: a quantity defined at each scale ... for every value of the quantity." **Too strong as a claim about proofs.** Valid form: the theorem implies such a flow trivially (F3), so the sentence is true and empty; the proofs that cross many scales (A1, A8) contain no such quantity and use a two-sided control with a small number. Range: wherever the sentence is used to shape a brief. What comes back: the crux stated as (U), (I), (J) of 3.4. *reading plus F3; not checked; by the skill's rule this is a suggestion until a check reads A1 and A8 beyond their introductions.*
- **N4** (`gap-crux-fp.md` L62): "one number cannot be enough". Valid for the free energy of periodic boxes. Too strong in general: the criteria of A3, A4, A6, A7 are statements at one size; they are not about periodic boxes. *reading.*
- **A test added, not a correction:** the compact Gaussian model with R = rho/n, as a test of a step at each value (6c). Row 720 had the U(1) form of it as a guide.
- **Verdicts:** none of the 36 (rows 712, 720) changes. None was re-derived. For one (method 10) the source was read first-hand; for two (method 3 and candidate Q1) F5 is an argument of this run.
- **A new kind of test.** A model where the target is true tests necessity claims, not tools. The lane had none before; A1 to A10 and Proposition Z2 are its first.

### 9.4 Routes worth doing (at most three)

1. **The check of this file** (work item 1). Believe: nothing. Cost: one check lane. First test: A1 and A8 read past their introductions; if either proof holds a one-way step in the size used above its threshold, C1 falls. Change: N1 and the brief rule of 9.5 stand or fall with it.
2. **A reading item against belief B4** (work item 2). Believe: that a proved gap may exist at a correlation length far above the lattice spacing with no small number, no exact closure and no correlation inequality. Cost: one reading lane. First test: the hierarchical O(N) model and the Gross-Neveu model, read for the scale at which the mass is proved and for whether the join with the ultraviolet flow is proved. Change: a template, if one exists; otherwise C8 moves from a belief toward a documented statement about the literature.
3. **One paragraph in the skeleton** (the lead; no lane). State the crux as: a criterion at the scale xi ((I)), and the class of effective actions on which it is proved ((J)); list the four means of 9.2 and why each is absent. Believe: nothing. Change: the line "Not queued: another author run on a step inequality" gets its reason, and a rule for when an author run is justified: its brief must name one of the four means, or a fifth.

### 9.5 What not to do next

- **No long author run whose brief is a one-way step for a torus quantity.** Reasons: C1 (no precedent outside exact closure), F5 (no class-wide step above about 4.8 for the lane's quantity), C7 (the one attempt), and row 720's own result (each candidate step is as hard as the seed). This agrees with the lead's "Not queued" of 13.15 and 13.16.
- **No author run on (Z-UNB), or on a criterion at the scale xi, without a named mechanism.** Theorem ZD of row 720 already reduces the seed to (Z-UNB); the four means are the known mechanisms.
- **Do not hope for monotony in the coupling.** In A1 it carries the result toward strong coupling. For SU(2) the seed is known at strong coupling and wanted at weak coupling (F4; argued, given the rate filter).
- **Do not use "it needs a small number" to set a tool aside.** Every proved tool outside exact closure needs one (C3). The reason is valid only as a range.
- **Do not read a positive control as support for a tool.** It refutes a necessity claim, or it shows which means a proof used.

### 9.6 The exact price

No equivalence is proved here. The price, in words: **T needs a criterion verified at a scale of at least one correlation length, and none of the proved cases read verifies one without a small number, exact closure or a correlation inequality.** The three candidate statements (P-a) a seed, (P-b) a restricted all-boundary criterion, (P-c) a two-sided bound on the effective action at coupling of order one, are not shown equivalent. This part of the exercise is a map with marks, and I say so: by the skill's list the run delivers one route with its first test run (route E, a control, off the path of T0), two filter corrections that are suggestions until checked, and one in-class test.

### 9.7 Work items

**Item 1 (first): check of this file.** A model that did not write it reads `library/gap-form-exercise.md`. Statements, in order: F3, F4, F5 (Step 3.1); Lemma Z2-a, Lemma Z2-b, Lemma Z2-c, Proposition Z2 (8.1); Remark 2D (8.2). Readings to test against the sources: table 2.D, rows A1, A2, A6, A8, A9, with the open copies named in 2.A (the DESY preprint 81/036 from the INSPIRE record of Gopfert and Mack; arXiv:2610.35286; mp_arc 97-578; arXiv:math-ph/9902020; arXiv:0711.4930). Points to test first: (1) A1 beyond page 10 and A8 beyond page 4: does either proof hold an inequality between two sizes that is used above the threshold of its criterion? This is the one finding that would break C1 and N1. (2) F5: that the same model at the doubled size has rho doubled; the Poisson step; the claim on the lattice (the script is in 9.8). (3) Lemma Z2-a, the upper count (the tree and the two inductions). (4) Lemma Z2-c: 28 twists with Pf = 1. (5) Proposition Z2: the arithmetic, and whether the clause 1 + S_w <= exp(Phi_w) of Theorem S-w needs anything that a finite positive matrix does not give. (6) The verdict on N1: is "too strong as a claim about proofs" fair to row 712's "in some form"? (7) The marks "partly" and "added" of 5.1, 5.2, by a search of its own that includes the branches of 5.3 and the parts 5.3 lists as not searched. Verdict per statement: HOLDS, HOLDS AFTER CORRECTION, FAILS. Stop at a finding under (1) and report it. Output: `library/gap-form-exercise-check.md`.

**Item 2: reading item, a precedent against B4.** Read from open copies (stop at a refusal; mark what is recalled): Gawedzki and Kupiainen, the hierarchical O(N) sigma model (Commun. Math. Phys. 106, 1986); Pordt and Reiss (hierarchical sigma model); Kopper, Magnen and Rivasseau (Gross-Neveu at large N, Commun. Math. Phys. 169, 1995); Kupiainen (the 1/n expansion, Commun. Math. Phys. 73, 1980); Ito and Tamura (Commun. Math. Phys. 1999); Ito's two papers on the Migdal-Kadanoff model (Commun. Math. Phys. 95, 1984; Phys. Rev. Lett. 55, 1985); Brydges and Federbush (Debye screening, 1980); Kopper (arXiv:math-ph/9902020) in full. For each: (a) the statement; (b) the ratio of the correlation length to the lattice spacing or cutoff at which the gap is proved; (c) the small number, exact closure or inequality that carries it; (d) whether the proof joins an ultraviolet flow to the infrared criterion; (e) whether any inequality between two sizes is used above the threshold of a criterion. Stop rule: stop after the list; if every source has (c), report "B4 stands in the read set". Output: `library/prior/gap-precedent-lit.md`. Mark every number GUIDE.

**Item 3 (only if the lead wants Proposition Z2 kept as a control): the Z_2 transfer operator with twists.** Write `library/gap-z2-control.md`: for Z_2 gauge theory on boxes with sides at least 3, the finite matrices T_{B,m}, their positivity and symmetry, the flips C_nu, Tr(T_{B,m}^a C^e) = Z^{e+m}, the permutation symmetry of Z^k, and the Z_2 form of Theorem L of `gap-seed-limit.md` as far as Corollary EV uses it; then Proposition Z2 of this file with its three lemmas. Sources: `gap-transfer.md` Sections 1 to 4, 8, 9.3; `gap-flux-exercise.md` L109-122, L495-517; `gap-seed-check.md` L177, L191-195. Then one check. It closes no item on the path of T0; it makes one test model of the lane a proved one.

**Not proposed:** an author run on a step for a torus quantity; on (Z-UNB); on route A, (P-c); a large-N target (an owner decision; named in Step 4 as a price only); a proof of the sketch of 7.2 (route B); (EV-STEP) and (KP) (rows 731, 733 advise against); edits of `gap-skeleton-final.md`, `t0-tree.md` or the registry (the lead's files).

### 9.8 Appendix

The tables are in Steps 2 (2.A to 2.D), 4, 5 (5.1 to 5.3), 6 (6a/6d, 6c), 7 (routes, kill pass, rank and registry) and 8.

- **Assumptions most likely to be wrong:** the reading of A1 and A8 from their introductions (C1 rests on it); e4 = B4 (no precedent); e2 (the base value is above s_1).
- **Assumptions most expensive to be wrong:** C1 (if a proved case has a step, the lane is missing a template); e1 (the gap itself).
- **Literature proofs worth translating:** the recursion of Martinelli and Olivieri (Theorems 4.5, 4.6 of Martinelli's lectures): a proved one-way doubling step for a worst case over boundary values, given clustering, with the device that turns a fixed loss per doubling into a summable one; the plan of Duminil-Copin and Tassion (one finite criterion and a differential inequality), as the model of a dichotomy; Gopfert and Mack's iterated Mayer expansion, as the model of crossing many scales with two-sided control.

The script of 8.0 (`/tmp/gfe-735/scripts/zr_step.py`):

```python
import math, resource, sys
import numpy as np

def log_pi(m):
    b = 2 * m
    c = 2.0 - 2.0 * np.cos(2.0 * np.pi * np.arange(b) / b)
    k2 = c[:, None, None] + c[None, :, None] + c[None, None, :]
    k2 = k2.reshape(-1)[1:]          # drop k = 0
    eps = np.arccosh(1.0 + 0.5 * k2)
    return float(-np.sum(np.log1p(-np.exp(-m * eps))))

def theta(A, P=200):
    return 1.0 + 2.0 * sum(math.exp(-A * p * p) for p in range(1, P))

th = theta(0.25) * theta(math.pi ** 2) ** 3
vals = {}
for m in (3, 4, 6, 8, 12, 16, 24):
    vals[m] = log_pi(m)
    print("m=%2d  log Pi=%.6f  Pi=%.6f  s_1=%.4f" % (m, vals[m], math.exp(vals[m]), th * math.exp(vals[m]) - 1.0))
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2 * 1024 ** 3:
        sys.exit("RSS above 2 GB; stop")
ok = True
for m in (3, 4, 6, 8, 12):
    r = math.exp(vals[2 * m] - vals[m])
    print("ratio Pi_%d/Pi_%d = %.6f  %s" % (2 * m, m, r, "pass" if r >= 0.51 else "FAIL"))
    ok = ok and r >= 0.51
print("theta(1/4)*theta(pi^2)^3 = %.6f" % th)
print("RESULT:", "PASS" if ok else "FAIL")
```


## Measure of the skill (row 721, Section 4.6)

- **Discard tests or verdicts corrected.** Verdicts: 0 of 36. Necessity claims re-judged as too strong: 2 (N1, the sentence of row 712 from which the form F came; N4). Tests added: 1 (the compact Gaussian model at each value). The two corrections are readings plus one short argument (F3); by the skill's rule they are suggestions until a check.
- **Statements of this run and their status.** argued, not checked: F3; F4 (given the rate filter); F5 (for the continuum formula); Lemma Z2-a; Lemma Z2-b; Lemma Z2-c; Proposition Z2 (given (TM-tw-Z2)); Remark 2D (given the recalled character formula). reading: table 2.D, C1 to C3, C7, C9, N1, N4, 7.4. belief: C8, F6. guide: one run (pass). open: (P-a), (P-b), (P-c). No check has been made, so the counts right / right after correction / wrong are not known.
- **"New" marks.** None is written as "new". Section 5.2 lists five items as "added"; each carries the scope of 5.1 and 5.3 ("not found in this branch's `library/`, `library/prior/`, `FINISH.md`, and in the searched part of pull request 10114, main, 10133, 10135, 10141, 10144"). One item that I had taken for my own in Steps 2 and 3 (Kopper's remark that the two-dimensional testbed is itself open) was found in pull request 10114 by the search of 5.3.
- **What the compare step found by its own search:** the sentence of `gap-crux-fp.md` L92 that N1 corrects; rows c1, c4, c5 of row 712; the test (M1) and readings 1, 3 of row 720; the counting bounds of `gap-seed-check.md` L193-195; the two-dimensional formula in rows 670 and 720; the digest of Piazza and Shen (row 719); the Kopper passage and an Ito-Seiler reading in pull request 10114.
- **Cost.** About 12.5 dollars on this session's budget meter; wall time from 21:53Z to about 22:35Z by the machine clock; one session, no subagents; one numeric run under the lock (a product over at most 110,592 momenta); eight downloads of open copies into `/tmp/gfe-735/dl/`, none committed; one scratch fetch of seven refs.
- **Did the pre-registration rule bind?** Once (8.0). The run passed its registered reading; the reading was not changed.
- **Did the closed list hold?** With one leak, disclosed in A4: a search for the place of Theorem DOB printed twelve one-line hits from closed files before Step 5.
- **Should a next long run change?** The lead had already not queued another author run on a step (13.15, 13.16). This run gives that decision a reason from proved cases, and a rule: an author brief on the crux must name the means by which a criterion is verified at the scale xi (one of the four of 9.2, or a new one). It cancels nothing that was queued.
- **Notes on the skill, from this run.** (1) Step 6 has no slot for a model where the target is true. Such a model tests necessity claims ("every proof must contain X"), not tools; this run had to add that form (6c). (2) Step 5's rule for the other branches is workable from a checkout that lacks them: a scratch fetch at depth 1 with lazy blobs, searched by path; it took about ten minutes, most of it in fetching blobs one by one. (3) A positive-control run reads many sources in part; the header rule "a source read in part is listed as read in part" carried most of the honesty of this file.

**Did the exercise succeed, by the skill's own list?** A route with its first test run: yes, route E (Proposition Z2, a control; off the path of T0). A corrected filter: two, as suggestions (not checked). A misframing: the evidence is a reading of ten sources in part, and one short argument; it is a suggestion until checked, with the replacing question in 7.4. An exact price: no. Much of the result is a map with marks. **The wall is not solved: no seed, no step and no mass gap is proved for SU(2).**

**Credits.** Gopfert and Mack; Guth; Brydges and Federbush; Glimm, Jaffe and Spencer (three-dimensional U(1) and the expansions it rests on). Piazza and Shen (two dimensions; their text notes the use of Claude for literature search). Forsstrom; Adhikari and Cao; Borgs; Seiler (finite groups). Osterwalder and Seiler; Shen, Zhu and Zhu (strong coupling). Knabe; Gosset and Mozgunov; Nachtergaele (finite-size criteria). Stroock and Zegarlinski; Martinelli and Olivieri; Martinelli; Schonmann; Dobrushin and Shlosman (mixing). Aizenman, Barsky and Fernandez; Duminil-Copin and Tassion (sharpness). Kopper; Kupiainen; Ito and Tamura; Kopper, Magnen and Rivasseau (large N). Tomboulis; Ito and Seiler; Migdal; Kadanoff (the decimation route). Chatterjee (the 2026 note on a central U(1)). Sussman and Alpoge, with Claude and Codex (the account; no statement of theirs is used in a proof here). In this repository: rows 669 and 670 (the two max plans), 697 to 699 (Theorem S and its checks; the Z_2 counting argument of the row-698 check), 700, 705, 707 (limit and shape; the compact Gaussian model), 712 (first principles; the 22 methods), 719 (the digest of Piazza and Shen and of the chain criteria, gpt-6-luna), 720 (the form, Lemma FLOW, the 14 candidates), 721 (the question of this run), 731 to 733 (the three seeds, their check by gpt-6-astra, Lemma NP), and the soft-kernel route of pull request 10114 (the Kopper passage).

RESULT: argued, not checked by another model: (1) F3: the form "base, one-way step, sufficiency" is satisfied by every model with a seed, with the base at the seed size; its only content is a base far below the seed size, which the method asks for and the target does not. (2) F5: for the lane's quantity S(n; (2n)^3) no improving step can be proved from the properties of the class at any value above s_1 (about 4.8, a guide), because the compact Gaussian model of row 705 grows there (continuum formula; a registered lattice guide run passes). (3) Proposition Z2 with Lemmas Z2-a to Z2-c: in Z_2 gauge theory at beta >= 91 the full and the kappa seed hold at N = 3, given the Z_2 transfer operator with twists (not written in the lane); a proved control inside the lane's frame, reached with no step. Reading, from open copies read in part: of ten families of proved gap or clustering results, a one-way step in the size occurs only where block integration is exact (two dimensions, Piazza-Shen; the Migdal-Kadanoff model, recalled) or where clustering is the hypothesis (Martinelli-Olivieri); Gopfert-Mack, strong coupling, finite groups, Knabe, Nachtergaele, sharpness and large N verify their criterion at its own scale by a small number, exact computation or a correlation inequality. Corrected (as suggestions until checked): the sentence of row 712 that a proof "must contain" a one-way flow at every value (too strong as a claim about proofs), and "one number cannot be enough" (valid for periodic free energies only); none of the 36 verdicts of rows 712 and 720 changes. Verdict on the row's question: the form is a habit as a proof form, and the next author brief on the crux should name the means by which a criterion is verified at the scale of the correlation length (a small number there, a second small number after an exact change of variables, exact closure, or a correlation inequality), not a step. Open: every seed and (G_ev) for SU(2) at a coupling of order one; (P-a), (P-b), (P-c) and their relation; belief B4 (no precedent without one of the four means), for which a reading item is proposed; (TM-tw-Z2). No mass gap is proved.
