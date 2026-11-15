# Author brief: execute APPROACH_REC_LIB.md

You are one Codex author context on the Mac mini. Read briefs_rec/APPROACH_REC_LIB.md and execute it.

## Inputs to read (this folder)
- OSLEAF55.md: §1.3-§1.4, Theorem REC, (L3) and (E0′).
- CODEX_REVIEW_OSLEAF.md: items 2 and F6.
- ASSEMBLY55.md: N9 and item 18.
- SRCCD55.md §2.2-§2.3, with CODEX_REVIEW_SRCCD.md §7.
- MASS_GAP_TARGET.md: the Hamiltonian it consumes.
- HANDOFF.md: the full-proof bar.

Use grep -n and offsets for large files.

## Literature
Literature is used for method only: open sources, nothing paywalled or pirated, no bot-check bypass. Nothing from it is load-bearing. Mark anything recalled from memory [m].

## Write
- **REC_LIB.md**: the rebuilt theorem, organised as separate library lemmas. Each lemma gets a statement, a full proof, and a status (PROVEN / ARGUED / OPEN).
  - Its very first edit is a PRE-STATED section containing statements only. Record that section's stat and byte size in REC_LIB_LOG.md.
- **REC_LIB_LOG.md**: provenance.
- **checks/rec_\***, only if you run a check:
  - write checks/rec_criteria.md first;
  - run one process at a time with `nice -n 10` and BLAS=1;
  - RSS must stay under 2 GB (the script checks itself);
  - start only when at least 50% of memory is free and load is under 20;
  - no multiprocessing pools.

End REC_LIB.md with three tables and a list:
- **"Statement match"**: compare REC-LIB's hypotheses with OSLEAF55's E0′-E3 and test algebra, line by line.
- **"Consumers"**: what in OSLEAF55, ASSEMBLY55 N9 and MASS_GAP_TARGET this discharges.
- **"Open residue"**.
- **Binding fixes to OSLEAF55**, if any.

## Rules
- Edit only REC_LIB.md, REC_LIB_LOG.md and checks/rec_*.
- No commits, pushes or PRs. No audit or ledger files. No axiom edits.
- Final message: under 300 words, giving a verdict per proof step and the open residue.
