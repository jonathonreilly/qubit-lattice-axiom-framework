lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T06:24Z

# gap-invent-selective-max (FINISH row 1013): invented selective mechanisms for 4D SU(2)

Working file of one worker session, pinned at commit d06a5b87b on `claude/ym4d-hard-route`. Research-stage working state. It grants no status and nothing here is a public claim. Marks used: PROVED (written argument, checkable by hand), ARGUED (argument with a named hole), OPEN, FAILS.

Status of this file: IN PROGRESS. Sections are appended step by step; the last section present is the point reached.

## Plan (eight steps, one per response; each appends its result before the next)

1. **Inputs.** Read `FINISH.md`, `GOAL.md`, `parts/gap.md`, the four prior reads named by the row (`library/prior/gap-o4-pinned-cell-read-opus.md`, `gap-o3-continuum-rg-read-opus.md`, `gap-2don-proofs-read-opus.md`, `gap-gauge-stiffness-read-opus.md`), `library/gap-crux-fp.md`; fetch the exercise skill at main commit 8b11ae2bb9. Write the kill sheet: the exact statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the U(1), Q_8, 2T, five-dimensional, instanton/refilling and four-test spec checks, each with its file and line.
2. **Discovery logic of the 2D proofs** (a reconstruction, not a fact about how they were found): a short list of design rules, each with the place in the papers that shows it; which choices were forced by "zero gain for the abelian model", which were free.
3. **Invention.** At least six candidate mechanisms for 4D lattice SU(2) that are not the direct port of row 1011, each with (a) monotone, (b) class and closure under conditioning, (c) selective identity, (d) dimension-4 input, (e) consumer.
4. **Kill fast.** Each candidate against the kill sheet; a candidate that renames the crux is a FAIL.
5. **Survivor 1:** first lemma, proof by hand or counterexample.
6. **Survivor 2** (if any): first lemma, proof by hand or counterexample.
7. **Novelty check** (the only literature step), ranking by (what it would change) / (cost to find out), and complete work-item briefs.
8. **Summary and the RESULT line.**

## Step log

(step 1 in progress, started 2026-11-15T18:25Z)

Status block (kept current):

- Step 1 (inputs, kill sheet): done, Section 1.
- Steps 2-8: not started.

Progress marker 1a (18:40Z). Read in full: `GOAL.md`; `FINISH.md` L1-90, L299-356 and rows 998-1013 (L1077-1098); `parts/gap.md`; the four prior reads (rows 1007, 1009, 1010, 1012). Still to read in this step: the in-progress file of row 1011, `library/gap-crux-fp.md` (five-dimensional test, Proposition V), the statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the exercise skill, `library/open-core.md` (duplicate check).

## 1. Step 1 result: provenance, inputs, and the kill sheet (done 2026-11-15T19:05Z)

**Provenance.** Anthropic, Claude Fable 5.2, max effort, one session on Mac mini worker 2, no subagents. Nothing in this file is checked by another model. The target is a standalone proof target, so the contract of `GOAL.md` (no computer-assisted step; proofs that could be formalized in Lean) replaces the framework refresher read of the exercise skill. The skill was fetched at main 8b11ae2bb9 with its one reference file `proof-search-governance.md` into `/tmp/row1013-skill/` and read in full. Its literature lens is not run (the row: rows 1007, 1009, 1010, 1012 are that lens).

**Credit.** The 2D mechanisms restated below are OpenAI's (author line "OpenAI"; posted, unrefereed; github.com/openai/math, commits adc7f1241b42 and 4eaee8754825) and Ding, Huang and Yang's (arXiv:2611.04908). The readings I start from are rows 1007, 1009, 1010, 1012 (Claude Opus 5.5, unchecked). Balaban's and Sussman-Alpoge's work is credited where it is used.

**Read in full:** `GOAL.md`; `FINISH.md` L1-90, L299-356, rows 998-1013; `parts/gap.md`; `library/prior/gap-2don-proofs-read-opus.md`, `gap-o4-pinned-cell-read-opus.md`, `gap-o3-continuum-rg-read-opus.md`, `gap-gauge-stiffness-read-opus.md`; the 82 lines of row 1011's file that exist at this pin (`library/gap-pinned-cell-gauge-max.md`: plan and input summary only, no result yet). **Read in part:** `library/gap-crux-exercise3-max.md` L690-722 (Lemma PT), `library/gap-crux-exercise4-max.md` L342-437 (Proposition NP), `library/gap-tiltproof-max.md` L202-262 (Theorem D2), `library/gap-sepinput-max.md` L300-404 (Lemma SHEET), `library/gap-crux-fp.md` L248-288 (the range form of the tests, the five-dimensional test), `library/gap-outside-box-max.md` L70-80 (row 1004's reading of the four-test spec check). **Not read:** the rest of the lane (about 800 library files); the primary 2D texts are opened in step 2 only where a design rule needs the exact place.

### 1.1 What the 2D solution is, in the lane's terms (from rows 1007, 1009, 1010; all OpenAI's mathematics, unchecked)

- The band is crossed at one fixed bare coupling b, by a mixing bound uniform over all bond strengths in [0, b] (O(3) paper Proposition 2.1; O(4) paper Theorem 3.1). No first-passage data, no (CAS).
- Its engine is a class statement: sup over all pinned squares of side R, all boundary pins, all strengths in [0, b] of the twist stiffness H is at most h. One step gives the same with h - delta at side l R, delta = (log l)/pi - C log B (S^3) or (log l)/(4 pi) - C log B (S^2). The gain is the bracket term of the rotation Ward identity and is zero for S^1.
- Small stiffness gives decay of charged observables (cheap local rotations, coarse orientations, disagreement percolation), then mixing of all observables by abelian conditional decompositions with association. The seed follows by the coupling integral d/dt Delta_t(n) = 8 n^2 [e_t(n) - e_t(2n)], which is the lane's Theorem D (f).
- The RG (exact, weak coupling only, contraction near L^(-2)) carries one box number to all finer cutoffs under an exponent condition. Transcribed to 4D by row 1010 (unchecked): mixing exponent below 3/2 times the one-loop exponent.

### 1.2 The kill sheet (each test with its exact form, source and what it binds)

| # | Test | Exact statement used here | Source (file:line) and standing | What a candidate must show |
|---|---|---|---|---|
| K1 | Lemma PT, Corollary PT1 | For a product model, D = D_1 + D_2, 1 + S = (1 + S_1)(1 + S_2), m = min(m_1, m_2); a seed of the product is a seed of each factor. Product with compact U(1) in its massless phase: no seed at any size. | `gap-crux-exercise3-max.md` L690-722; proved by hand, check 999 HOLDS (PT1 after correction: theorem-grade for Villain U(1) at beta at least 2^14) | Its conclusion step (monotone small implies gap of all observables) must read the whole state space; a gain that reads the SU(2) factor only is allowed, but then the last step must fail for the product. |
| K2 | Proposition NP | K copies of strong-coupling SU(2) times ordered Ising: D contracts by any theta on any J doublings, and the model has no seed. | `gap-crux-exercise4-max.md` L383-412; check 1006 HOLDS | Its induction must not read the model only through finitely many values of D. |
| K3 | Theorem D2 | SU(2) Wilson (also Q_8, 2T), even box: pinning the links of directions 2, 3 on one slice leaves an O(4)-symmetric two-dimensional sheet for the direction-1 links, with the infrared bound G-hat(p) at most 1/(2 beta E(p)); so every tilt-uniform covariance bound kbar is at least lam_* k00, lam_* at least 8.54 on side 4. | `gap-tiltproof-max.md` L240-246; proved given Lemmas RP, GD (rebuilt in row 1000) | No hypothesis that is a supremum over bulk tilts or over pins of interior link sets. |
| K3' | Slab device (mine, a corollary of the D2 construction; ARGUED, the infrared-bound theorem RECALLED) | Pin all links inside two parallel lattice hyperplanes at distance 1 to the identity. The free links between them, g(y) = U_4(y), carry exactly the three-dimensional O(4) spin model with weight exp(beta q.q'). For large beta it has long-range order (Frohlich, Simon and Spencer 1976, RECALLED). At distance R the cross-slab holonomy is a three-dimensional field with stiffness of order beta/R. | this file | A class closed under conditioning on link sets must not contain pinned hyperplanes closer than about beta; cubes with pinned boundary are allowed only if the step never produces thin cells. |
| K4 | Lemma SHEET, and its fixed-b form | All-fields form: with coupling B on the side plaquettes of a tube and 0 elsewhere, Cov(x_(p_i), x_(p_j)) tends to 1/4 as B grows; the supremum over coupling fields of lambda_max of the plaquette covariance is at least (n - 1)/4. Fixed-b form (to be checked per candidate): with strengths in [0, b] the class contains every lower-dimensional gauge system cut out of the lattice (tubes, thin slabs with free sides). | `gap-sepinput-max.md` L358-380; check 997 (same provider) | A class with strengths in [0, b] is allowed only if its claim holds for these cut-out systems at the same b. |
| K5 | Compact U(1) | Coulomb phase at weak coupling (Guth; Frohlich and Spencer; in the lane for Villain at beta at least 2^14). | `parts/gap.md` L195 | The gain must vanish identically for an abelian group. |
| K6 | Frozen Q_8, 2T | Finite non-abelian subgroups: no seed (T_per; T_ev in the frozen limit) at large coupling. | `parts/gap.md` L199; check 884 | The selective identity must use the Lie algebra (infinitesimal rotations, connectedness), not only that the group is non-commutative. |
| K7 | Five-dimensional test | SU(2) Wilson in five dimensions has massless gluons at weak coupling (GUIDE, numerics; transition near 1.6). A tool blind to the dimension stops below that coupling. | `gap-crux-fp.md` L88, L266, L283 | The dimension-4 input must be named, and the gain must fail in d = 5 (for example: the action of a scale-R wave grows like R in d = 5). |
| K8 | Instanton and refilling | Replacing a rough region by a small-curvature field that agrees with the exterior needs a small-curvature extension of boundary link data; the winding of the boundary data (pi_3(SU(2)) = Z) can obstruct it. | row 1010, `gap-o3-continuum-rg-read-opus.md` L136, L201 (RECALLED there, unchecked) | A candidate that fills or deforms fields must say what it does in a sector with winding. |
| K9 | Four-test spec check (row 1004's reading; the phrase is defined in no file) | A tool for T_W must use (S1) the non-abelian structure, (S2) a rate, (S3) the whole state space, (S4) typical fields; and (S0) a candidate that returns the crux under another name is a FAIL. | `gap-outside-box-max.md` L75 | One line per candidate for S0-S4. |

**Valid form of every test (exercise skill, step 6c).** A model M' refutes a candidate only if the candidate's hypothesis H holds in M' and its conclusion T fails there. Otherwise the test says what a proof of H must use. A pass is no support.

### 1.3 The consumers a candidate may feed (from `parts/gap.md` and rows 1009, 1010)

- (C-mix) the 4D analogue of Proposition 2.1: a mixing bound for Wilson SU(2) at every weak bare coupling, with an explicit length X(beta) whose exponent is below 3/2 times the one-loop exponent, uniform in plaquette strengths up to beta as far as Theorem D (f) needs it. With the carry of row 1010 6.5 (partly RECALLED, with the refilling obstruction K8) it gives the seed on the trajectory.
- (C-W) the wall (W) directly; (C-CAS) one contraction factor theta below 1 of the Casimir free energy on a bounded range of sizes; (C-seed) the periodic seed at one size.
