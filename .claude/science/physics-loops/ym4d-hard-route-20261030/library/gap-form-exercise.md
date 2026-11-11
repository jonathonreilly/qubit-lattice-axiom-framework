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
| 2 inventory | not started | |
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

