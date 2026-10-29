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
H_RP is exact for the Wilson action on the torus and on the sphere's equator (banked). Everything else rests on the
UV RG below.

**Route to H_Euc.** *Sphere (leading)*: on S^4_R rotations are exact, the Killing-field Ward identity has no shell term,
SO(5) invariance survives R → ∞ by compactness, and rotated-lattice universality is ultraviolet at fixed volume
(Proposition T, banked). Open items are ultraviolet: the regularised sphere theory, seam transparency, universality's
N1–N5 / W0–W3, large-field comparison. *Flat (alternative)*: needs the infrared input TQ; its reductions are banked;
TQ itself is unproved, and whether RP plus Wilson-specific inputs can give it is undecided (CODEX_REVIEW_TQ).

## Open inputs of the full theorem — status and who is on it

| Input | Status (banked pieces in [S26-BANKED]) | File / worker |
|---|---|---|
| Coupling flow | conditionally reduced (FLOW55) to one trivial-background estimate (UIR^♮) | UIR55 (running) |
| BFT-0 identification | slice form banked; the nonlinear slice lemma (NSL) open | NSL55 (running) |
| BFT-1/2 | banked on 𝒞_glob, conditional on named lane-A linear inputs (K^(σ), GV-E, TR∞) | — |
| BFT-3 | implication on 𝒞_glob (Theorem BFT3-glob) | BFT34_55; Codex review running |
| BFT-4 | not implied by analyticity + BFT-3 (Prop. CX); reduced to local ARGUED items + (CovLift) | BFT4W55 (running) |
| BFT-5 (b) background transfer | Theorem GA banked; needs an actual alignment with uniform quotient/source/defect bounds, then (LOC-GA) off 𝒞_glob | ALIGN55 (running) |
| BFT off 𝒞_glob (large fields) | OPEN: (G♯-patch), (UHL), (SL-cov), (LOC-GA); RLARGE W-cb♯/FI-1 banked conditionally | not yet assigned |
| Node A (single-level measure) | reductions + BL-TILT banked; multiscale convexity (LC°) open | LCONV55 (running) |
| SRC (source-inserted RG; gives CD, OS0) | Prop. B, Lemma V banked; SRC-E′/O/W′, SRC-OW, Prop. E open | SRCAN55 (running) |
| H_Euc, sphere route | equatorial RP, Proposition T banked; construction + seam + UV items open | SPHERE55 (running) |
| H_int | free comparator banked for a narrower class; Yang–Mills side open | HINT2_55 (running) |

## Systemic defects to check in every claim
Symbol collisions (verify which object each symbol denotes, by file and string); stale minima (what was the
inequality evaluated at?); checks that cannot decide (could it have failed?); status arguments are not proofs.
Line numbers in PROOF.md drift — locate by string.

## Next steps
1. As each running worker reports: Codex astra-max review, then bank only what it confirms.
2. Assign the large-field inputs (BFT off 𝒞_glob, (LOC-GA)) once ALIGN55 and NSL55 report.
3. When every row above is closed and cross-checked: assemble the proof of T_OS in one document, have it reviewed
   end to end by both families, then package PR 10114 for the owner's publication pass.
