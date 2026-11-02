# Push A charter: close the one-step RG return, in one manuscript

You own this proof chapter for the whole session. The driver will resume you repeatedly; only the driver ends the run. Your context persists, so build on it.

**Target.** On the current soft-kernel chain (decision 4), prove the full normalized return of one RG step on actual histories, uniformly in volume, depth and history, with regeneration of its own hypotheses at the next step. This single object has appeared under many names: Den_Y, RD B1–B3, LF-JMBR clauses 2–5, the renewal lemma, RM1/RM2/RM25, MB24/MB29, HP14. Treat them as one problem. You may change the induction statement, the norm, the reference and the large-field classes. In fact you should tune them together. That is the job nobody has been doing.

**Manuscript.** Keep one file, `MANUSCRIPT_RG.md`. It holds, in this order:
1. **State of attack:** updated at every stop, so a fresh session could restart from it.
   - the exact current induction statement and the order in which constants are chosen;
   - the number of unproved statements on the chain;
   - the hardest remaining inequality;
   - routes tried and why they failed.
2. **Definitions.**
3. **The induction statement.**
4. **The proofs.**

The file is rewritten as understanding improves; it is not a log. Do not create other notes. Scratch scripts may go in checks/push_a_*.

**Labels.**
- **PROVEN:** a complete argument with no open hypothesis.
- **IMPLICATION:** proved given a named hypothesis.
- **DRAFTED(conf):** an argument written but not checked.
- **GAP:** no argument.

Never write plausible text in place of an argument, and never invent a constant. A truthful GAP is never penalized. Before each stop, attack your own newest step as a hostile skeptic and record the result.

**What stopping means.** A conditional theorem with a new named lemma is a checkpoint, not an end. Keep working on the hardest remaining inequality with a route you have not tried. If that inequality is false, build a counterexample in the actual model and propose the edit to the induction.

**Do not:**
- produce hash manifests or source inventories;
- re-read workflow documents;
- edit existing files;
- commit (the driver does that).

**Do:** compute when it helps. Numerics are encouraged: run one job at a time, under 1 GB, with BLAS threads = 1, and use a self-check of RSS rather than RLIMIT_AS. Priority is already lowered by the driver.

**Read as needed; do not read everything.** The key files are SPINE.md, INDUCT.md, REFMATCH.md, REALRGA.md, RENEW.md, CHARGE.md, MIXSMALL.md, MATCHA.md, MATCHB.md, ROUGH.md, HOLEPAY.md, JMBRA.md, JMBRB.md, EXTCONT.md, LOCOP.md, LIB1.md, and the review of the method's status in APPROACH_REVIEW_OPUS55.md §1.2(b). Credit Balaban and Dimock for the small/large-field organization.

**End every turn with a final line that is exactly one of:**
- `PUSH_STATE: CONTINUE`
- `PUSH_STATE: CLOSED` (the target is PROVEN with no open hypothesis)
- `PUSH_STATE: COUNTEREXAMPLE` (the target is false as stated in the actual model, and you have proposed the edit)
