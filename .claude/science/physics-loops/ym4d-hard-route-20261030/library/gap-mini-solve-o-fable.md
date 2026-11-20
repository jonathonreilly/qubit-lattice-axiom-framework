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

## 2. How to attack it (step 2, written 2026-11-20T05:20Z)

**What has to be proved.** Given the checked chain (Section 1), the gap clause needs one lattice statement, (N-phys), plus the account's continuum datum. The continuum datum (H2), (TOT), (P1)-(P4) is PROVED for the account's datum in `library/gap-chain-ce-opus.md` (L235, L365). So the only open lattice input of the gap clause is (N-phys). This row attacks (N-phys) and nothing else. Rule 0a: the existence core in `library/open-core.md` is not touched.

**What (N-phys) asks, in physical terms (GUIDE; arithmetic only, no run).** In a periodic box of side L, at Euclidean time L/K, the sum over all centre-neutral excitations of e^(-E (L/K)) is at most 1/2, uniformly in the cutoff.

- Massless benchmark: the free lattice photon has log(1 + s) about 2K^3/pi^2 at aspect K (two polarisations, density of modes (L/2 pi)^3 d^3k). At K = 512 this is about 2.7e7. So (N-phys) is selective only because K is large. This is the lane's Lemma FLOOR (row 988), found again.
- Gapped benchmark: a dilute gas of particles of mass M gives log(1 + s) about c (LM)^3 e^(-LM/K). So (N-phys) at K = 512 needs LM of order 1.5e4. Row 1181's GUIDE (about 1.1e4 correlation lengths) agrees.
- Comparison with the One-Bound seed (A-B*) of row 1218 (new here, GUIDE). With the same dilute-gas model, (A-B*) at y_0 = 1/20 needs M T_0 a of about 22. That is the same Euclidean time as (N-phys) needs (about 29/M at K = 512). The box is smaller: sides 2T_0 to 48T_0, about 44/M to 1000/M. The excitation density allowed at that temperature is within a factor of about 20 of the density (N-phys) allows. The two seeds ask for the same physics at the same temperature. Neither is closer to a proof.

**Routes considered before choosing (each grepped; all match the record).**

1. Port of the 2D O(N) mechanisms (Ding-Huang-Yang; OpenAI O(3), O(4)). Failing step on file: Lemma PC (row 1188), the twist cost is extensive on a 3D slice. Also row 1197 (GC), no free collective coordinate. Reason in one line: Mermin-Wagner-type gains need codimension 2 defects. In 4D gauge theory the defect is a sheet, so the gain per unit area is O(1/log R) and the cost is O(area).
2. Bakry-Emery, curvature of the orbit space, Polchinski flow, multiscale LSI: method 31 (rows 957, 968), row 1181.
3. Local-to-global methods (spectral independence, trickle-down, entropy factorization, Dobrushin-Shlosman, information percolation by SDPI): `library/prior/gap-lit-tiltcov.md` Step 3, `library/prior/gap-lit-annealed.md`. Each is an engine. Its local input at block scale is a one-scale seed of kind (K-one).
4. Thermodynamic and trace-anomaly form (carry the interaction measure down in temperature): row 1198 (ANOM), Remark TH.
5. Carry to finer cutoffs by RG transport: row 978 ((NOCRIT), (UNIV-K), (CC)). For one continuum datum, liminf suffices (row 1180), so the carry is not the obstruction. The seed for the continuum torus theory is.
6. Hypercontractive or Doob-transform routes: rows 978, 982, 1207, 1208.
7. Gap from confinement, centre vortices, Tomboulis, Mack-Petkova: rows 1179, 1190; `library/gap-cr-tomboulis-check-opus.md`. Not on the gap clause's path (Theorem BP).
8. Positive dual or random-surface expansions: row 1209 (dual gas FAILS); row 1201 (positivity of the four-linear weight, OPEN).
9. Variational or chessboard bounds on Z and lambda_0 separately: method 35. The two bounds are extensive and their errors do not cancel.
10. The new published inputs: (A) asks for the same physics (above). (B) Corollary 166 is row 1220's item. (C) is conditional on (TUN) and (SPEC); row 1218 finds no Wilson certificate.

**Assessment.** By the checked chain, (N-phys) is a statement about the continuum SU(2) theory on a torus. Its spectrum depends on the one variable z = L Lambda, and (N-phys) asks for a dilute glueball gas at z near 1e4. Every route above needs, at some step, an analytic estimate at the scale where the running coupling is of order one. No analytic tool reaches that scale; the best hand bounds for 4D SU(2) Wilson stop at beta_W of about 0.35, and the band is 2.3-2.6. The no-computer rule (GOAL.md) excludes a finite verification at the band. In this row's judgement, no attack available here can close (N-phys). This is a judgement, not a theorem.

**Choice.** Plain-brief rows 1188-1202 each tried a fresh candidate and found the map. This row does not run another. It writes this assessment and checks one statement that could change the lead's plan, Section 3: does a one-scale seed exist that is weaker than (N-phys), still carried to the gap by a checked engine, and provable at weak coupling with present tools? If yes, the lane should switch to it. If no, the reason should be one statement.
