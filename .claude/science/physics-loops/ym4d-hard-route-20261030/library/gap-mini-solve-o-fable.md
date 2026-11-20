lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T16:12Z

# gap-mini-solve-o-fable (queue row 1219)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 3, one fresh session, pinned at commit 8148dff3d. Not an audit. Nothing here is checked by another model. Research-stage working state.

Problem (row 1219): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Labels used below: PROVED (every step written here), ARGUED (argument given, a step is not fully written), GUIDE (heuristic or numeric guidance, not a proof step), OPEN.

## 0. Plan (written first, 2026-11-20T03:44Z)

1. Repo search: read the RESULT lines of the earlier gap rows, `parts/gap.md`, `library/open-core.md`, and `library/prior/gap-onebound-read-sol.md` (row 1218).
2. Choose one line of attack that the earlier rows have not closed or killed. State it as one precise statement.
3. Attack it in steps. Append each step here before the next.
4. End with one RESULT line.

Status of this file: step 1 in progress.

## Continuation by Claude Opus 5.5 (2026-11-20T04:12Z)

The Fable run above stopped at step 1 when the Mac mini account reached its Fable weekly limit (lead note on row 1219). This run is Claude Opus 5.5, max effort, Mac mini worker 3, one fresh session, pinned at commit 3065cacc7. It keeps the plan above and continues from step 1. Earlier header lines named the Fable run (lead anthropic/claude-fable-5-2/max, lease to 2026-11-20T15:44Z, commit 8148dff3d). Not an audit; nothing here is checked by another model.

## 1. Repo search (step 1, done 2026-11-20T04:35Z)

Read at the pin 3065cacc7: the FINISH rule sections and row 1219; `GOAL.md`; the RESULT lines of rows 1179-1225; `parts/gap.md` L1-104 (state of attack); `library/prior/gap-onebound-read-sol.md` (row 1218) in full; row 1179 (`library/gap-mini-branch-fable.md`) Sections 5.3-6; the opening of the parallel row 1220 (`library/gap-mini-solve-p-fable.md`).

State taken as given (cited, not re-derived):

- The Jaffe-Witten gap clause follows from one lattice estimate and the continuum datum. Row 1179 Theorem BP (check 1183, cross-provider, HOLDS AFTER CORRECTION): (N-phys) gives a cutoff-uniform gap M_* = (2/L) log(1/(40328 eps)) on the centre-blind algebra; with a continuum datum with (H2) and (TOT) (the T0 chain) it gives the gap clause. The branch selection (BS) and the wall (W) are not inputs of the gap clause.
- (N-phys) (row 1161 L146-148): at one physical side L, for all fine cutoffs j, some integer u_j in [3, n_j/K] has s_+(u_j; n_j^3) <= 1/2, where s_+ is the periodic centre-neutral excited thermal trace of the cube n_j^3.
- Row 1180 (check 1187, HOLDS): (N-phys) holds iff every fine coupling has a finite one-cube seed size nu(beta_j) and limsup_j a_j nu(beta_j) is finite. So (N-phys) is a uniform neutral lattice gap at weak coupling plus an asymptotic-scaling-type bound.
- Restatements on file, each checked: two-slice information (26) and the binary test (28) (row 1186, check 1191); the probability ratio (row 1192, check 1203); the mass detector Q (row 1204, check 1210); the wall test (row 1211, check 1214). Each is equivalent to (N-phys) up to constants; none is proved.
- Fifteen plain-brief rows of Claude Fable (1188-1202, letters a-l) each screened candidate attacks and found each on the lane's map. Lesson recorded after row 1198: do not start from a candidate list.
- Row 1218 (new input): (A) the One-Bound thermal seed (A-B*) is stronger than (N-phys) and has a proved conditional ascent; (B) Hexagon 2610.00341v7 Corollary 166 proves BP(n, 1/2) for the straight-path block law of SU(2) Wilson at beta_W <= k + 2, b = 2^k, on tori of side R <= exp(2^k/(17k)); (C) Zeng's packages are conditional. Credit: A, D. Bhattacharjee, U. Bhattacharya, J. M. Lockwood, T. Romanov, I. J. Sessford, S. Singha Roy; B, the first four of them; C, Zeng Chunping.
- Duplicate check (rule 0a): the parallel row 1220 (worker 1, same brief) states in its Section 1 that it answers "does (B)'s weak-coupling theorem shorten the way" with a Lemma NULL. This row therefore does not attack Corollary 166's use.

Status: step 2 (choice of the attack) next.
