lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-28T21:15:14Z

# gap-kernel-solve-fable (FINISH row 1674): closed-folder solve from the Lean hypothesis

Started 2026-11-28T09:15:14Z (date -u). Worker: Mac mini Claude worker 1, Claude Fable 5.2, max. Base commit 9a626d7f6. No commit, no push; the relay copies this file.

Status: IN PROGRESS. Each section is written when its step is finished. The last section in the file is the current state.

## 0. Scope, and one conflict in the instructions

- The row brief says: closed folder. Read only `lean/gapchain/GapChain/Stage0.lean`, `lean/gapchain/GapChain/Final.lean` and `library/gap-mech-direction4-fable.md` sections 1.4 and 1.5. Do not read FINISH.md, GOAL.md, the registries or any other library file.
- The dispatch text says: read FINISH.md and GOAL.md, build on all published work, and grep `library/open-core.md` and the FINISH rows before a statement is called new.
- These two texts conflict. Decision: the row brief wins, because it is the specific text for this item, and because a closed-folder look cannot be repaired after the folder is read.
- What was read before the conflict was seen: GOAL.md (in full, 94 lines; it is about the existence target and has no content on the gap), and FINISH.md row 1674 only (found by grep of the row name). No other FINISH row, no registry and no other library file was read. The header sections of FINISH.md (efficiency rules, Build on published work) were NOT read; the general working rules were applied instead.
- Consequence: no statement in this file is called new. Novelty against `library/open-core.md` and the FINISH rows was NOT checked. The check row can do that comparison.
- The session memory index (one line per earlier row) was loaded by the harness. Its lane files were not opened.
- No numeric job was run (row rule). Labels: PROVED, CITED, ARGUED, GUESSED, as the row asks.
