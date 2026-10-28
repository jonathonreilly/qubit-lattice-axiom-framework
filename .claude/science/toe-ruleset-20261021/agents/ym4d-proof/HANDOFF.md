# YM4D proof push: handoff (2026-10-28)

## Goal
- Constructive UV stability (layer 1) and existence (layer 2: OS axioms, non-triviality) of 4D lattice SU(N) Yang-Mills.
- Method: a soft gauge-covariant RG with S4' averaging ("decision 4": soft chosen over Balaban's hard delta-constraint).
- Credit Balaban (CMP series; the 1987 CMP 109:249-301 PDF is in literature/) and Dimock in every public text.
- Nothing has been posted or landed.

## Where things stand
- **Master file: PROOF.md.**
  - Tally 72 PROVEN / 2 / 7 / 24 OPEN + 1.
  - The CROSS-LANE STATUS map is at the end of the session-23 consolidation.
- **Frozen, outside-readable piece: LINEAR_PACKAGE.md v1.1.**
- **Lane files** (each has a matching REVIEW_* per session; read the latest review first, since it lists the binding fixes):
  - RLARGE.md v3: large-field R-operation;
  - FLOW.md: coupling flow, normalisation u = 2N/g², ghost share 1/22, T-tel exact;
  - BFT_A.md and BFT_B.md: background-field theorem clauses 0-5, as stated in REVIEW_S22 Part 5;
  - HW.md, PLD.md, SQ.md, SF.md (computer-assisted certificates), HIST.md.
- **Existence lane: ../ym4d-existence/E/EXISTENCE.md.**
  - Paused until the layer-1 outputs exist.
  - Its consumer list says which layer-1 outputs it needs.

## Critical path (REVIEW_RLARGE_V3 top 3, plus the other lanes)
1. **(LI^U) future-insensitivity.** The wall is (CRC-1), a two-species cluster expansion. HW session 5 was running.
2. **Node-A in-step returned price.** PLD session 5 was running (NA-PRICE on the extracted representation).
3. **The (CLS-min) chain.** (CLS-min) ⇐ (REG-min) ⇐ (EPS-0b), the lattice Uhlenbeck gauge, taken as lane B's S_E. SQ session 4 was running.
4. **BFT.**
   - (NC-Γ) via the (PW-i) dual form: BFT A session 8 was running.
   - Lane B session 8 PROVED GE-T, N2-loc, N1-loc and CL-iv. Its review, REVIEW_BFT_B_S8.md, was running.
   - Still open: non-residual g_Z at θ > 0, (CovLift)(v), (Mult-Y)/GAP 1, and m > 0.
   - BFT-5 has no owner yet.
5. **FLOW.** (T-a1) and the m_n lemma were in FLOW session 13 (running). Still open: (T-a2), (T-b), (T-c), (L-loc2).

On resume: check each lane file's newest section and the REVIEW_* files. Agents running at handoff may have finished; do not trust this list over the files.

## Process rules (binding)
- **Hostile review after every session**, written to REVIEW_<LANE>_S<n>.md by a reviewer that did not write the session.
- **Provenance.**
  - The PRE-STATED section is the very first edit of a session and holds statements only. Log its stat and byte size in the *_LOG.md file.
  - Write the criteria files before the scripts. They may contain no constants derived in the same session.
- **Numerics.**
  - Take the lock with `until mkdir <scratch>/locks/numeric; do sleep 20; done`, run, then `rmdir` exactly once.
  - Never pkill.
  - Run with nice 10 and one thread.
  - Run only when load < 8 and at least 30% of memory is free.
  - Keep each job under 20 min and under 1 GB.
  - Run one numeric job machine-wide (8 GB machine).
- **Statuses.** Use PROVEN / ARGUED / OPEN honestly. A failed check is reported as a fail, with any post-hoc probe labelled post-hoc.
- **Never edit the axioms.**
- **Imports are allowed** but must be re-verified on our structures.
- **No Sci-Hub/LibGen**, and pay for nothing.
- **Landing (only once the full proof is complete and reviewed):**
  - one PR (note + runner + cache), landed by an independent review-loop agent;
  - then draft the HN / OpenAI-thread text for the owner to approve word for word.

## Update after the handoff list was written: HW session 5 finished
- **Theorem CRC-2T** proves (CRC) for every column-relaxed pattern. It is not yet reviewed; the review writes REVIEW_HW_S5.md.
- **The smallness condition tightens.** The binding condition is g_K² < 4.9e-97/(c_A + c_U), and it fails the recorded ceiling of 1e-94.
  - g_0 therefore has to be lowered.
  - Recheck the downstream constants, including the SF thresholds.
- **New wall: (E2^𝔉).** This is the good-buffer screening bound, required uniformly over the column-relaxed family. It needs an input from node A, which is the PLD lane's work.

## Update: BFT lane A session 8 finished
- **Proven (unreviewed):**
  - Lemma DF;
  - Theorem PW-cc, the co-closed half of the dual (PW-i), uniform in k and T;
  - Propositions RF and TE;
  - Lemma RC.
- **Conflict with lane B.** Lane A argues that (GE-T) and (PW-i) for Γ_E are *false* at large k, because of a root-funnel spike: the measured ratio is ρ = 8.02, but on a Coulomb stand-in, not on S_E itself. Lane B claims GE-T is PROVEN, with root charges.
  - REVIEW_BFT_B_S8.md has been asked to settle this. Look for the section "Cross-lane GE-T adjudication".
- **Lead decision pending:** whether to adopt lane A's representative that moves the spikes to level 0 (one slice or two). Make it after that review.
- **Still open:** (PW-ii), which Proposition SR needs, and the factor k in (NC-Γ).

## Update: PLD session 5 finished (node-A in-step price)
- **Proven (unreviewed):**
  - Lemmas GEO, FT^far and COL-DEC: on HW's route the law conversion costs nothing (c_f = 0).
  - Lemma DIL-L.
  - Lemma MD: a returned defect whose own kernel centre is good is priced by its own kernel.
- **Implication:** Theorem NA-PRICE^E (i), (SDP)^{A,far} ⇐ (CLS-min) + (SF-cap) + (J-NS^cd).
- **New wall: (J-NS^cd).** A bad coarse centre sits above a finer defect whose own centre is also bad. It needs an energy-graded price, i.e. (SDP) one level down; check whether induction on levels closes it.
- **Also open:** c_lcr is uncertified. The working value is θ ≈ 8e-7.
- **Reviews running:** REVIEW_PLD_S5.md (it includes whether this supplies HW's (E2^𝔉)) and REVIEW_BFT_A_S8.md.

## Update: SQ session 4 finished (the Uhlenbeck / CLS-min wall)
- **Theorem EPS-T:** lattice ε-regularity, PROVEN but unreviewed. Its Moser constants are not explicit.
- **Route β gives a chain of implications:** Proposition EPS-0b-avg ⇒ (EPS-0) ⇒ (REG-min) ⇒ (CLS-min). The funnel product is integrable, not bounded.
- **Route α:** the lattice Uhlenbeck gauge LU-ex is PROVEN. (CVX-K) is still OPEN but is not needed.
- **Check failures:** two checks failed and are disclosed (q4b P0; q5 T2, which was rerun post-hoc as T2b).
- **Review:** REVIEW_SQ_S4.md is running. It decides whether (CLS-min) is actually delivered to RLARGE.
- **If it holds,** two of the three RLARGE critical-path walls reduce to: (E2^𝔉), (J-NS^cd), and the explicit constants.

## PAUSED 2026-10-28 for handoff: what was stopped mid-run
At the owner's request, every agent below was stopped. No result from any of them is complete.
- **FLOW session 13 ((T-a1) and the m_n lemma).** It was stopped during its f16 smoke run.
  - FLOW.md, FLOW_LOG.md and checks/f16_* may contain a partial §103+.
  - Treat everything after the [RFL12-fix] entries as unfinished and unreviewed.
- **Reviews stopped before writing anything.** Rerun each one, using the same scope as the session claims above:
  - REVIEW_BFT_B_S8, including the cross-lane GE-T adjudication against BFT_A §36-§40;
  - REVIEW_BFT_A_S8;
  - REVIEW_HW_S5;
  - REVIEW_PLD_S5;
  - REVIEW_SQ_S4.
- **Numeric lock.** It was held by a stopped agent. No process was running, so it was released.
- **Not committed:** literature/balaban_cmp109 PDF and its extracted text. The paper is copyrighted, so they stay local and are left out of the public repo.

Suggested order on resume:
1. Run the five reviews.
2. Settle GE-T and decide one slice or two for BFT.
3. Lower g_0 and recheck the SF thresholds.
4. Work (J-NS^cd) and (E2^𝔉) together; both need node-A pricing.
5. Rerun FLOW S13.
