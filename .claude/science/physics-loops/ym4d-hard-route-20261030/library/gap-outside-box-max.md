lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T03:55Z

# gap-outside-box-max: change the frame, not the inequality (row 1004)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, fresh session, pinned at commit 95fecd964. Not an audit. No status is granted by this note. Research-stage working state.

## Plan (at most eight steps; one step per response; each result is appended before the next step)

1. **Read the frame.** `parts/gap.md` (lead rules, registry, test table, price), row 1002 (`library/prior/gap-kflow-read-opus.md`), row 1003's scope, and the exercise skill at main commit 8b11ae2bb9. Record here: the crux as it stands, the consumers ((W), (CAS), the gap), the four-test spec check, the test table.
2. **Assumption lens.** List what the present frame fixes without saying so (space, boundary, state space, coupling, group, time). Each entry is one candidate frame change.
3. **Generate.** Seeds (a)-(e) of the row plus my own. Each idea stated as mathematics, with the exact statement to prove and its consumer.
4. **Test.** Four-test spec check and the test table (Lemma PT, Theorem D2, Lemma SHEET, compact U(1), the 2D O(N) filter) on every idea. Same crux renamed = FAIL, named as such. Grep the lane before any novelty claim.
5. **Rank** survivors by (what it would change) / (cost to find out).
6. **Top survivor:** first lemma, proof by hand or counterexample.
7. **Second survivor:** first lemma, proof by hand or counterexample.
8. **Close.** Marks (PROVED, ARGUED, OPEN, FAILS), work items as complete briefs, RESULT line.

## Log

- 2026-11-15T15:55Z: file created. Steps follow below, in order.

## Header (exercise skill, Output rules)

- Written by: Anthropic, Claude Fable 5.2, max effort, Mac mini worker 2, one fresh session. Commit 95fecd964. Date 2026-11-15.
- **Nothing in this file is checked by another model.**
- Skill used: `exercise` at main commit 8b11ae2bb9 (fetched to a scratch folder with `proof-search-governance.md`, `assumption-import-audit.md`, `RULES.md`, `procedures/research.md`, `procedures/check.md`, same commit). The framework refresher list is replaced by `GOAL.md` and `FINISH.md` of this target, as the skill allows for a standalone proof target.
- Binding limits of the brief: no subagents, no commit, no other file edited, no computer-assisted step in any proof, scope = the frame (row 1003 has the inputs inside the frame, row 1005 the literature on frame changes).
- What this run did not cover (kept true as the run goes): see the end of the file.

## Status block (kept current)

| Step | State | Main result |
|---|---|---|
| 1 Read the frame | done | Section 1 |
| 2 Assumption lens | not started | |
| 3 Generate | not started | |
| 4 Test, grep | not started | |
| 5 Rank | not started | |
| 6 Top survivor | not started | |
| 7 Second survivor | not started | |
| 8 Close | not started | |

## 1. The frame as it stands (step 1)

Read in full: `GOAL.md`; `parts/gap.md`; FINISH rows 1002 to 1005 and the sections Where it stands, How we work, Working efficiently, Rules; `library/prior/gap-kflow-read-opus.md` (row 1002); the skill and its governance file. Read in part: `library/gap-crux-exercise3-max.md` L100-160 and L686-760 (the wall, Lemma PT, Proposition KF); `library/gap-crux-restate.md` L1-80 (objects, (TM), (TM-c), candidates C1 to C5); `library/gap-phys-seed.md` L286-335 (Theorems ZD, ZD-c, Corollary Z4); `library/gap-mid-max.md` L58-70 ((CAS)); `library/gap-tiltproof-max.md` L236-262 (Theorem D2).

### 1.1 The crux (quoted, not rewritten)

Objects (`gap-crux-restate.md` Section 1): Wilson SU(2) on a periodic torus with sides n_mu >= 3; Z(n), F = log Z, f = inf F(n)/|n|; for a 3-box B the transfer operator T with eigenvalues lambda_0 > lambda_1 >= ...; m(B) = log(lambda_0/lambda_1); S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k; D(a) = F(a^4) - f a^4 >= 0.

The wall (row 998 L129-131): "(W) There is a physical size L in P with z^-(L) > 256 D_0 + 30, where D_0 bounds D^+ on the sizes from L/4 on." Here z^-(L) = liminf_j (L/a_j) m_j((L/a_j)^3) and D^+(L) = limsup_j D_j(L/a_j) along the account's trajectory.

Price on record (`parts/gap.md`): (W) iff (BDD-Delta) and (Z-UNB) (Theorem ZD-c). (W) follows from (CAS): D(2a) <= theta D(a) with theta < 1 on a bounded range, with an extensive base. In words: one selective inequality at every scale between first passage and the seed size. Selective means false for a product with a massless factor (Lemma PT).

Consumers: (W) -> (PHYS-SEED) -> uniform gap on all larger dyadic cubes (Theorem S) -> the mass gap of the limit theory. The mass gap is a later target; T0 itself does not ask for it (`GOAL.md`).

### 1.2 What the present frame fixes

- F1 space: a hypercubic lattice, all four directions periodic, one lattice spacing in all directions.
- F2 shape: the symmetric torus a^4 for D; the box (2N)^3 at time N for the seed.
- F3 boundary: none. Twists enter only as the centre flips C_nu of (TM-c).
- F4 state space: gauge-invariant L^2 of the link field on one periodic 3-slice, all flux sectors together.
- F5 coupling: one real coupling beta for the whole torus; the trajectory (a_j, beta_j) moves it with the cutoff only.
- F6 theory: gauge group SU(2), Wilson weight, no matter field.
- F7 time: the Euclidean lattice time of the transfer operator. No other flow.
- F8 engine: Theorem S, which uses (TM), Lemma A and the invariance of Z under exchange of two axes; it holds for every group of the class.

### 1.3 The tests an idea must face

Test table of `parts/gap.md` (copied there from row 998 6c). For a tool for T_W the theorem-grade tests are: compact U(1) at weak coupling, the free photon, the product with a massless factor (Lemma PT, Corollary PT1), Theorem D2 (no supremum over tilts), Lemma SHEET (no uniformity over coupling fields). Row 1002 adds the 2D O(N) filter (a plausibility test, not a theorem).

**Reading of "the four-test spec check" (a reading; the phrase is defined in no file of the lane, searched in FINISH, library/, parts/, docs/ai_methodology).** I take it as point 2 under the test table: a tool for T_W must use (S1) the non-abelian structure (else compact U(1) binds), (S2) a rate (else the free photon binds), (S3) the whole state space (else a product with a massless factor binds), (S4) typical fields (else D2 or SHEET binds). To these I add (S5) the 2D O(N) filter: the step names its four-dimensional or gauge-specific input. And the row's own rule (S0): a frame change that returns the same crux under another name is a FAIL.

### 1.4 Open now / closed until the compare step

Open now: the statements quoted above. Closed until step 4 (the compare step): the attack files of the lane (the four exercises, the direction and brainstorm notes, `gap-ac-lat.md`, `gap-ds-gauge.md`, `gap-zf-box-*.md`, the literature digests under `prior/`). Step 3 is written before they are opened; step 4 opens them by grep and nothing is called new before that.
