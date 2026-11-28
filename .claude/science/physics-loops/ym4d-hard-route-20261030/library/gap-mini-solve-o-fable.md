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

Status of this file: step 1 in progress (Fable run). Superseded: the Opus continuation below finished steps 1-4.

## Continuation by Claude Opus 5.5 (2026-11-20T04:12Z)

The Fable run above stopped at step 1 when the Mac mini account reached its Fable weekly limit (lead note on row 1219). This run is Claude Opus 5.5, max effort, Mac mini worker 3, one fresh session, pinned at commit 3065cacc7. It keeps the plan above and continues from step 1. Earlier header lines named the Fable run (lead anthropic/claude-fable-5-2/max, lease to 2026-11-20T15:44Z, commit 8148dff3d). Not an audit; nothing here is checked by another model.

## 1. Repo search (step 1, done 2026-11-20T04:35Z)

Read at the pin 3065cacc7: the FINISH rule sections and row 1219; `GOAL.md`; the RESULT lines of rows 1179-1225; `parts/gap.md` L1-104 (state of attack); `library/prior/gap-onebound-read-sol.md` (row 1218) in full; row 1179 (`library/gap-mini-branch-fable.md`) Sections 5.3-6; the opening of the parallel row 1220 (`library/gap-mini-solve-p-fable.md`).

State taken as given (cited, not re-derived):

- The Jaffe-Witten gap clause follows from one lattice estimate and the continuum datum. Row 1179 Theorem BP (check 1183, cross-provider, HOLDS AFTER CORRECTION): (N-phys) gives a cutoff-uniform gap M_* = (2/L) log(1/(40328 eps)) on the centre-blind algebra; with a continuum datum with (H2) and (TOT) (the T0 chain) it gives the gap clause. The branch selection (BS) and the wall (W) are not inputs of the gap clause.
- (N-phys) (row 1161 L146-148): at one physical side L, for all fine cutoffs j, some integer u_j in [3, n_j/K] has s_+(u_j; n_j^3) <= 1/2, where s_+ is the periodic centre-neutral excited thermal trace of the cube n_j^3.
- Row 1180 (check 1187, HOLDS): (N-phys) holds iff every fine coupling has a finite one-cube seed size nu(beta_j) and limsup_j a_j nu(beta_j) is finite. So (N-phys) is a uniform neutral lattice gap at weak coupling plus an asymptotic-scaling-type bound.
- Restatements on file, each checked: two-slice information (26) and the binary test (28) (row 1186, check 1191); the probability ratio (row 1192, check 1203); the mass detector Q (row 1204, check 1210); the wall test (row 1211, check 1214). Each is equivalent to (N-phys) up to constants; none is proved.
- The finished plain-brief rows of Claude Fable (1188-1202, letters a-l except j, which is still open) and rows 1179-1184 each screened candidate attacks and found each on the lane's map. Row 1220 Section 1 reports the lesson drawn after row 1198: do not start from a candidate list.
- Row 1218 (new input): (A) the One-Bound thermal seed (A-B*) is stronger than (N-phys) and has a proved conditional ascent; (B) Hexagon 2610.00341v7 Corollary 166 proves BP(n, 1/2) for the straight-path block law of SU(2) Wilson at beta_W <= k + 2, b = 2^k, on tori of side R <= exp(2^k/(17k)); (C) Zeng's packages are conditional. Credit: A, D. Bhattacharjee, U. Bhattacharya, J. M. Lockwood, T. Romanov, I. J. Sessford, S. Singha Roy; B, the first four of them; C, Zeng Chunping.
- Duplicate check (rule 0a): the parallel row 1220 (worker 1, same brief) states in its Section 1 that it answers "does (B)'s weak-coupling theorem shorten the way" with a Lemma NULL. This row therefore does not attack Corollary 166's use.

Status: step 1 done. Step 2 is Section 2.

## 2. How to attack it (step 2, written by about 2026-11-20T04:40Z)

**What has to be proved.** Given the checked chain (Section 1), the gap clause needs one lattice statement, (N-phys), plus the account's continuum datum. The continuum datum (H2), (TOT), (P1)-(P4) is PROVED given the account's premises (row 916, `library/gap-chain-ce-opus.md` L235, L365; check row 917 by gpt-6-astra: the seven P' conditions hold under the named seed, lane and account premises). It stays open with the T0 chain. So the only open lattice input of the gap clause, beside the T0 chain, is (N-phys). This row attacks (N-phys) and nothing else. Rule 0a: the existence core in `library/open-core.md` is not touched.

**What (N-phys) asks, in physical terms (GUIDE; arithmetic only, no run).** In a periodic box of side L, at Euclidean time L/K, the sum over all centre-neutral excitations of e^(-E (L/K)) is at most 1/2, uniformly in the cutoff.

- Massless benchmark: the free lattice photon has log(1 + s) about 2K^3/pi^2 at aspect K (two polarisations, density of modes (L/2 pi)^3 d^3k). At K = 512 this is about 2.7e7. So (N-phys) is selective only because K is large. Compare Lemma FLOOR (row 988, `library/gap-unit-max.md` L174): a seed forces side times gap above 17.04 at threshold 1/5041.
- Gapped benchmark: a dilute non-relativistic gas of g one-particle states of mass M gives log(1 + s) about g (2 pi)^(-3/2) K^(3/2) (LM)^(3/2) e^(-LM/K). With g = 10 and K = 512, s <= 1/2 needs LM of about 1.25e4, that is u M of about 25. Row 1181's GUIDE (about 1.1e4 correlation lengths) agrees.
- Comparison with the One-Bound seed (A-B*) of row 1218 (new here, GUIDE). With the same dilute-gas model, (A-B*) at y_0 = 1/20 needs g (2 pi)^(-3/2) (M tau)^(3/2) e^(-M tau) <= y_0/(2 x 96^3), tau = T_0 a, so M tau of about 22. That is about the same Euclidean time as (N-phys) needs (about 25/M at K = 512). The box is smaller: sides 2T_0 to 48T_0, about 44/M to 1000/M. The excitation density allowed at that temperature (about 2.7e-12 M^3) is within a factor of about 13 of the density (N-phys) allows (log(3/2)/L^3, about 2.1e-13 M^3). The two seeds ask for the same physics at the same temperature. Neither is closer to a proof.

**Routes considered before choosing (each grepped; all match the record).**

1. Port of the 2D O(N) mechanisms (Ding-Huang-Yang; OpenAI O(3), O(4)). Failing step on file: Lemma PC (row 1188), the twist cost is extensive on a 3D slice. Also row 1197 (GC), no free collective coordinate. Reason in one line: Mermin-Wagner-type gains need codimension 2 defects. In 4D gauge theory the defect is a sheet, so the gain per unit area is O(1/log R) and the cost is O(area).
2. Bakry-Emery, curvature of the orbit space, Polchinski flow, multiscale LSI: method 31 (rows 957, 968), row 1181.
3. Local-to-global methods (spectral independence, trickle-down, entropy factorization, Dobrushin-Shlosman, information percolation by SDPI): `library/prior/gap-lit-tiltcov.md` Step 3, `library/prior/gap-lit-annealed.md`. Each is an engine. Its local input at block scale is a one-scale seed of kind (K-one).
4. Thermodynamic and trace-anomaly form (carry the interaction measure down in temperature): row 1198 (ANOM), Remark TH.
5. Carry to finer cutoffs by RG transport: row 978 ((NOCRIT), (UNIV-K), (CC)); check row 917 finds full (UNIV-K) OPEN. Row 1180: for one continuum datum, liminf suffices. In either form the seed is still needed on a box where the running coupling is of order one.
6. Hypercontractive or Doob-transform routes: rows 978, 982, 1207, 1208.
7. Gap from confinement, centre vortices, Tomboulis, Mack-Petkova: rows 1179, 1190; `library/gap-cr-tomboulis-check-opus.md`. Not on the gap clause's path (Theorem BP).
8. Positive dual or random-surface expansions: row 1209 (dual gas FAILS); row 1201 (positivity of the four-linear weight, OPEN).
9. Variational or chessboard bounds on Z and lambda_0 separately: method 35. The two bounds are extensive and their errors do not cancel.
10. The new published inputs: (A) asks for the same physics (above). (B) Corollary 166 is row 1220's item. (C) is conditional on (TUN) and (SPEC); row 1218 finds no Wilson certificate.

**Assessment.** By the checked chain, (N-phys) is a statement about the continuum SU(2) theory on a torus. Its spectrum depends on the one variable z = L Lambda, and (N-phys) asks for a dilute glueball gas at z near 1e4. Every route above needs, at some step, an analytic estimate at the scale where the running coupling is of order one. No analytic tool reaches that scale; the best hand bounds for 4D SU(2) Wilson stop at beta_W of about 0.35, and the band is 2.3-2.6. The no-computer rule (GOAL.md) excludes a finite verification at the band. In this row's judgement, no attack available here can close (N-phys). This is a judgement, not a theorem.

**Choice.** Plain-brief rows 1188-1202 each tried a fresh candidate and found the map. This row does not run another. It writes this assessment and checks one statement that could change the lead's plan, Section 3: does a one-scale seed exist that is weaker than (N-phys), still carried to the gap by a checked engine, and provable at weak coupling with present tools? If yes, the lane should switch to it. If no, the reason should be one statement.

## 3. Is there a weaker seed that present tools can prove? (step 3, written by about 2026-11-20T04:44Z)

**Answer: no, for one reason, which is on file.** Row 998 6b (`library/gap-crux-exercise3-max.md` L525-527): "every engine found is blind, so its seed sits in the band". This row finds the same reason and adds nothing that changes it. The steps:

(a) PROVED (one line). Let an engine be a theorem "for every model in a class M, a seed Phi_n(mu) <= phi_0 on one box gives a uniform neutral gap". If M contains a model with no gap, then that model has Phi_n > phi_0 on every box. Row 998 6b records that every engine the lane found is blind, that is, valid on a class that contains models with no gap (compact U(1) at weak coupling, the free photon). For such an engine, the seed fails on those models.

(b) ARGUED (asymptotic freedom; the rigorous form needs the account's small-volume control). On a box of physical side l with g(l) small, SU(2) is close to three free photons in every quantity a seed can read continuously. For thermal-trace seeds the toron moduli suggest the SU(2) small-box trace is not smaller than the free one (heuristic; related statements on file: the One-Bound paper (A), Theorem 7.59 as read by row 1218, "the fixed-lattice-size SU(2) gap closes as coupling increases"; row 1215, "the periodic neutral levels coalesce at fixed spatial size").

(c) ARGUED. By (a) and (b), a seed for a blind engine fails on every box where g(l) is small. So it must be verified on boxes where the running coupling is of order one or larger. For 4D SU(2) at weak bare coupling, present analytic tools control only small g(l) (Balaban, the account) or beta_W below about 0.35 (strong coupling; row 1218: (A) Theorem 9.5 to 9/25, (B) Theorem 3 to 0.348; both written proofs, not checked here). Neither reaches those boxes. "Present tools" is not a mathematical object, so (c) is a judgement.

(d) The only way out is an engine that is not blind: a step that carries the one selective fact provable today (the one-loop running at small coupling) through the band. That is the lane's (K-flow) (lead rule W2, `parts/gap.md` L97). Row 998 6c point 5: constraints, no refutation device, no mechanism. This row found no candidate either.

**The new published inputs do not change (a)-(d).** (A)'s ascent is of the same thermal-purity kind as the lane's older periodic-seed engine (row 1218), which the record classes as blind; this row did not read (A)'s proof to confirm that its class contains a gapless model. Section 2 shows its seed needs the same physics as (N-phys): a dilute glueball gas at Euclidean time about 22-25/M. (B)'s Corollary 166 is row 1220's item. (C) assumes (TUN) and (SPEC).

## 4. For the lead (evidence only; this row edits no other file)

1. Plain-brief rows on (N-phys) have now returned the lane's map about sixteen times (rows 1179-1184, the eleven finished rows a-l, and this one). Row 998 9.5 ("What not to do next") already lists "another fresh-framing exercise by this model family". This row is one more data point for it.
2. A row that could change the state of (N-phys) would have to bring one of: a non-blind engine (item (d)), or an analytic estimate for 4D SU(2) at order-one running coupling. Neither has a candidate in the record or in this row.
3. Switching the seed to the One-Bound form (A-B*) buys a smaller box (about 44/M to 1000/M instead of about 1.25e4/M) but asks for the same excitation density at the same temperature, within a factor of about 13, and it also controls the charged sectors. It is logically stronger than (N-phys). GUIDE: no reason to switch.

## 5. Marks

| Statement | Mark |
|---|---|
| The gap clause needs only (N-phys) beside the account's datum | cited: row 1179 Theorem BP with check 1183; rows 916-917 (`gap-chain-ce-opus.md` L235, L365) |
| Massless benchmark log(1 + s) about 2K^3/pi^2; dilute-gas benchmark, LM about 1.25e4 at K = 512 | GUIDE (arithmetic, no run) |
| (A-B*) and (N-phys) ask for the same physics at Euclidean time about 22-25/M, densities within a factor of about 13 | GUIDE (same model) |
| Ten routes considered, each matched to the record (Section 2) | match list; no new attack |
| 3 (a): a blind engine's seed fails for every gapless model of its class | PROVED (one line) |
| 3 (b)-(c): every seed of a blind engine must be verified where the running coupling is of order one | ARGUED; this is row 998 6b |
| (N-phys); a non-blind engine; the mass gap | OPEN |

No numeric run was made; the numeric lock was not taken. Nothing here is checked by another model.

RESULT: Row 1219 (Fable 5.2 started 03:44Z and stopped at step 1 at the Fable limit; continued by Claude Opus 5.5 max, Mac mini worker 3, 04:12Z-04:50Z; author only, checked by no one; no numeric run). The mass gap is NOT proved and nothing is disproved. The only open lattice input of the gap clause is (N-phys) (row 1179 Theorem BP, check 1183; the continuum datum is PROVED given the account's premises, rows 916-917). Ten routes considered here (2D-mechanism ports, curvature and multiscale LSI, local-to-global engines, the trace-anomaly form, RG carry, hypercontractive and Doob forms, confinement, positive duals, separate variational bounds, the three new published inputs) each match the record at a named failing step; no attack off the map was found, so none was run. PROVED (one line): a blind engine's seed fails for every gapless model of its class. ARGUED (= row 998 6b): every such seed must be verified where the running coupling is of order one, which no present analytic tool reaches. GUIDE: the One-Bound seed (A-B*) and (N-phys) ask for the same dilute glueball gas at Euclidean time about 22-25/M (densities within a factor of about 13); (A-B*) only has a smaller box. OPEN: (N-phys), a non-blind (K-flow) engine, the mass gap. Output library/gap-mini-solve-o-fable.md.
