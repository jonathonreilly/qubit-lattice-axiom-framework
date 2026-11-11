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
- What this run did not cover: filled in at the end (Section "Not covered").

**Status block** (kept current).

| Step | State | Main result |
|---|---|---|
| 0 record, closed list | done | open and closed lists written; own literature pass, since the lane's digests are closed |
| 1 wall twice | done | no blind check ran (no subagents) |
| 2 inventory | done | ten source notes (2.A), the lane's statements (2.B), beliefs (2.C), one table (2.D) |
| 3 reason up | not started | |
| 4 assumptions | not started | |
| 5 compare | not started | |
| 6 filters | not started | |
| 7 routes | not started | |
| 8 attempts | not started | |
| 9 report | not started | |

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

