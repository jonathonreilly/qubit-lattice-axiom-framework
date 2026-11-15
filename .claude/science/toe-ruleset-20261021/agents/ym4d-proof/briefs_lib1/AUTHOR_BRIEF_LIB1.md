# Author brief LIB-1: rebuild the most valuable shared lemma from the library rebuild list

Lead: Claude Opus 5.5, 2026-10-29. One Codex author context runs on the Mac mini. This is the third lane in the queue, after SOFTHARD and REC-LIB.

Owner directive, 2026-10-29: "if we need their proofs or lemmas just rebuild them and put them in the repo / PR / library."

## Pick the target (first, and recorded in the PRE-STATED section)

Read the following:
- SOFTHARD.md, in particular the section "Library rebuild list", plus REVIEW_SOFTHARD.md;
- HANDOFF.md, the "Remaining proof path" steps 1-6;
- ASSEMBLY55.md, CODEX_REVIEW_ASSEMBLY.md and APPROACH_REGISTRY.md.

Use grep -n and offsets for large files.

Choose **one** lemma that meets all of these conditions:
- (a) It is needed on the route currently in force. That route is decision 4, the soft kernel, which stays in force until the owner rules whatever SOFTHARD recommends. Prefer a lemma that is needed on **both** routes.
- (b) It feeds a named open item in HANDOFF steps 1-5, or in the assembly's ordered list.
- (c) Its open source text (the arXiv PDFs under ARXIV_DIR, or arXiv itself) contains a complete proof strategy, so a full rebuild is realistic in one session.
- (d) It is not already proven in this folder. Check with grep, and cite what you checked.

If SOFTHARD.md is missing or has no rebuild list, pick from CODEX_REVIEW_ASSEMBLY's ordered list using the same criteria (a)-(d).

Record the candidates you considered and the reason for your choice.

## Rebuild

1. State the lemma exactly, in our notation: our lattice, our kernel and our norms. Make the hypotheses match the consumer word for word.
2. Write a full proof on our structures. Literature supplies the method only, and nothing from it is load-bearing. Mark anything recalled from memory as [m], and treat it as open residue, not as proof.
3. Credit the original authors by name: Balaban, Dimock, and others as appropriate.
4. Give a "Consumers" table showing which open items it discharges or narrows, with exact quotes.
5. Exact finite checks are optional:
   - write `checks/lib1_criteria.md` first;
   - run with nice, and BLAS=1;
   - keep RSS under 2 GB, checked by the script itself;
   - require at least 50% memory free and load under 20;
   - no multiprocessing pools.

## Write

- **LIB1.md**: its first edit is the PRE-STATED section, which holds the target choice and the statements only. Log that section's stat and byte size in LIB1_LOG.md.
- **LIB1_LOG.md**.
- **checks/lib1_\***.

## Rules

- Statuses are PROVEN, ARGUED or OPEN.
- Edit no other file.
- No commits, pushes or PRs.
- No audit or ledger files, and no axiom edits.
- Final message under 300 words: the chosen lemma, the verdict, the consumers and the residue.
