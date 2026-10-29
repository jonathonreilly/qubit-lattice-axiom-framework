# YM4D proof push: handoff (rewritten in session 26, 2026-10-29)

*Supersedes the session-24 handoff (in git history). It is a map with pointers, not a statement of results: every
result named here is stated exactly in the file it points to, and a result counts only if it is in PROOF.md's
[S26-BANKED] block (established by Claude Opus 5.5 AND checked by Codex gpt-6-astra at max).*

## Goal (owner)
- **The full theorem T_OS on R^4**: a Euclidean SU(N) Yang–Mills theory satisfying OS0–OS3, not free, obtained as a
  limit of lattice theories. **No mass gap is claimed.** A finite torus is a laboratory, not the target (PLAN_S26 §7).
- Method: a soft gauge-covariant RG with S4′ averaging (decision 4), building on T. Balaban's programme (CMP 1983–89)
  and J. Dimock's expositions. **Credit Balaban and Dimock in every public text.** Imports must be re-derived on our
  structures.
- **Nothing is posted or landed.** No statement in this repository claims 4D Yang–Mills existence. The PR (10114)
  is packaged for publication only when every input below is closed and cross-checked; the owner approves public
  text word for word.

## Rules in force
- **Workers: Claude Opus 5.5 at max (at least xhigh), model and effort set explicitly; deliverable line one is the
  model ID, checked. Reviewers: Codex gpt-6-astra at `model_reasoning_effort=max`, banner checked.** Opus does the
  work; Codex reviews it (owner). Nothing is banked without the cross-family check.
- Sessions 24–25 ran on the wrong model (claude-opus-5). Their content was re-reviewed by Opus 5.5 (§SWEEP55 in
  SESSION25_RESULTS.md: 571 claims, 301 confirmed / 55 not verified / 215 refuted); only what was confirmed and
  banked may be used.
- Workers never run git; one deliverable each, append-only, PRE-STATED first, criteria before scripts, exact
  arithmetic only. Never edit the axioms.
- Balaban's CMP papers are copyrighted: local copies only (`~/Documents/balaban-cmp/`, empty so far), never in the
  repository; no Sci-Hub/LibGen; no CAPTCHA/bot-check bypass. The open arXiv expositions (Dimock I–III 1108.1335 /
  1212.5562 / 1304.0705; Covariant Axial Gauge 1410.2798; QED d=3 1502.02946, 1512.04373, 1712.10029, 2009.01156,
  2204.07201; Goswami 2204.08252) are downloaded to the session scratchpad only — re-download from arXiv next session.
- Magnitudes matter only in two-sided feasibility windows ((TC), Compatibility (K), the complex-width interface);
  one-sided constants need no decade ledgers (PLAN_S26 §12, SMALLNESS_DAG).

## Read these, in this order
1. This file.
2. PROOF.md — the provenance banner, **[S26-BANKED]** (what holds) and **[S26-REVIEW]** (what was reverted). The
   105-item tally (72/2/7/24+1) predates both and is not a measure of progress.
3. PLAN_S26.md §7–§14 (target, role split, consensus, Balaban corrections, the sphere route, corrections).
4. SESSION25_RESULTS.md from §SWEEP55 to the end (§BANKED, §STOP, §RESUME, and later entries).
5. The worker file and its CODEX_REVIEW_*.md for whichever input you take.

## The architecture (CONFIRMED as an implication: PANEL_P1, unanimous panel PLAN_S26 §10)
T_OS on R^4 follows, along one diagonal subsequence a_j → 0, R_j → ∞ with no uniqueness, clustering or gap, from:
- **H_reg** — cutoff- and volume-uniform moment bounds for a determining observable family (OS0 + compactness);
- **H_RP** — reflection positivity for one common reflection, errors → 0;
- **H_Euc** — the Euclidean symmetry defect → 0 on a dense subgroup (only non-lattice rotations are hard);
- **H_int** — a calibrated local non-freeness witness bounded away from the free class.
H_RP: Wilson reflection positivity on the torus is IMPORTED-AND-REVERIFIED in PROOF.md (L9a), not cross-family banked; the sphere's equatorial RP is banked; the coordinate reflections θ_μ at the pole are now proved (CODEX_REVIEW_SPHERE item 2). Everything else rests on the
UV RG below.

**Route to H_Euc.** *Sphere (leading)*: on S^4_R rotations are exact, the Killing-field Ward identity has no shell term,
SO(5) invariance survives R → ∞ by compactness, and rotated-lattice universality is ultraviolet at fixed volume
(Proposition T, banked). Open items are ultraviolet: the regularised sphere theory, seam transparency, universality's
N1–N5 / W0–W3, large-field comparison. *Flat (alternative)*: needs the infrared input TQ; its reductions are banked;
TQ itself is unproved, and whether RP plus Wilson-specific inputs can give it is undecided (CODEX_REVIEW_TQ).

## Open inputs of the full theorem — status and who is on it

| Input | Status (banked pieces in [S26-BANKED]) | File / worker |
|---|---|---|
| Coupling flow | reduced (FLOW55, UIR55; both Codex-confirmed) to tree-jet bounds at orders 2-4 + (ρ-null) + finite-volume uniformity | UIR2_55 (running) |
| BFT-0 identification | banked conditionally (NSL + Theorem ID, Balaban's convention, trivial background, 𝒞_glob); identification with PROOF's per-level BR1 actions not banked — needed only if a consumer uses them | NSL55 + CODEX_REVIEW_NSL |
| BFT-1/2 | banked on 𝒞_glob, conditional on named lane-A linear inputs (K^(σ), GV-E, TR∞) | — |
| BFT-3 | banked conditionally on the global potential-small domain (Lemma WD, route C); per-level identification and the full curvature-small class open | BFT34_55 + CODEX_REVIEW_BFT34 |
| BFT-4 | (a) on 𝒞_glob banked conditionally on the linear/contraction package only ((R) PROVEN, RLOC55 + Codex); (b): Lemma AVG reduction banked (centred-norm factor ≤ 2), but "no consumer" NOT banked (CODEX_REVIEW_BFT4B: (I_k^E)″ needs critical-value polymers identified with its invariant, centred-norm class) — target off 𝒞_glob is (c₀) on the invariant consumer domain + that identification | OFFGLOB2_55 on (c₀) (running) |
| BFT-5 (b) background transfer | GA, RED″ (log chart), HD_log/FW_log, Λ_LP algebra, L1/L2 + N1-L banked (conditional); left-trivialised alignment obstructed (CW); open: periodic (P2-tw)_log, (AC)_log, the periodic harmonic/path repair, the source-infimum restriction, covariant output conversion | queued (ALIGN3) |
| BFT off 𝒞_glob (a SMALL-field problem: small curvature, arbitrary holonomy/frames) | local components banked (routing, cc localisation, Lemma AX, U1/U2, exact lift); Theorem OFF NOT banked — GAP at uniform root-preserving frame patching (FP ⇏ UQ), complex-frame convention, GP as a defined inverse; identification, BFT-3/4, boxes open | OFFGLOB2_55 (running) |
| Node A / one RG step (small-field region) | reductions + BL-TILT banked; bare-action / exponential-chart non-convexity confirmed, the full conditional-chain no-go NOT verified (CODEX_REVIEW_LCONV); needed: one-step conditional positivity + per-step cluster expansion (I1) + main-term coercivity (BFT-coer, I2) | STEP55 (running) |
| SRC (source-inserted RG; gives CD, OS0) | Prop. B, Lemma V, SA-CF/SA-PC/SA-TC/SA-S, SA-K banked (scoped); open: (A) complex envelopes for the tilted chain incl. large coarse fields, (B) real conditional decay = a decaying polymer representation (same object as BFT-4), (LOC-e), the OS0 extension estimate | not yet assigned (waits on LARGE55, BFT-4) |
| H_Euc, sphere route | construction, RP (5 planes), Ward algebra, Proposition T, Lemma 3.5′ (nonvacuity repair), W0/N5 as conditional implications banked; open: LCS-a (trace-channel matching), N5-T* (seam RG at rough coarse fields), N5-C, all-product W1/W3/coarse-image bounds, layer 1 on the sphere lattice with variable coupling, U-sep, and the separated-products → full-OS-algebra positivity bridge | unassigned (next free slot) |
| H_int | identification-free witness on e banked on the free side (NONFREE55 + Codex: T_NF against canonical free theories and finite mixtures; owner to confirm the definition); YM side = (TS-e-up), (TS-e-low) at every short scale | TSE55 (running) |

## Systemic defects to check in every claim
Symbol collisions (verify which object each symbol denotes, by file and string); stale minima (what was the
inequality evaluated at?); checks that cannot decide (could it have failed?); status arguments are not proofs.
Line numbers in PROOF.md drift — locate by string.

## Next steps
1. As each running worker reports: Codex astra-max review, then bank only what it confirms.
2. Assign the large-field inputs (BFT off 𝒞_glob, (LOC-GA)) once ALIGN55 and NSL55 report.
3. When every row above is closed and cross-checked: assemble the proof of T_OS in one document, have it reviewed
   end to end by both families, then package PR 10114 for the owner's publication pass.

## The current work list (2026-10-29)
**CODEX_REVIEW_ASSEMBLY.md, "Corrected ordered OPEN work list" (17 items), is the authoritative list of remaining work**
and supersedes the table above wherever they differ. Its first two items precede all estimates: (1) fix ONE OS
formulation and observable algebra — DONE and banked (OSLEAF55 + Codex: separated Schwinger distributions; REC, EXT, CLOSURE); (2) an absolute non-freeness criterion and witness on that same
algebra (NONFREE55, running) — the single most dangerous item. DIAG is proven (Codex R2). ASSEMBLY55's 18 mismatch labels
are superseded by the review's scope-specific verdicts.

## Large-field architecture (LARGE55; Codex verdict 2026-10-29: candidate route, NOT adopted — nothing dropped from RLARGE)
Recommendation: keep RLARGE v3's R-operation (returned-cluster renormalisation, forced in d = 4 by Theorem DENSE) and
HIST-sum's arithmetic; replace v3's HW/PLD/SQ moment-pricing layer by Balaban-type level-by-level pricing (Lemmas MIS,
COL, KA, PRICE). Would drop 15 of RLARGE §4.2's 38 rows incl. (CLS-min)⇐(REG-min), (AE)⇐(MS-Sob), (SDP)^A, and (KS-N).
New/remaining inputs I1-I11 (LARGE55 §6.4); (LF-diff) (I10) is needed by UNIV and SRC on every route.
Codex's milestone that would make the route comparison real: one normalised, history-compatible step on a chart with a hole
(main-term price, mismatch implication, normalised returned-activity analytic norm incl. a ZERO-FREE normaliser, reference
comparison, failed returns) — this is STEP55's task.
