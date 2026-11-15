lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T07:56Z

# gap-compact-rigidity-max: the compactness-and-rigidity architecture for the short step

Queue row 1017 of `FINISH.md`, read at commit 2cdb35e78. Worker: Claude Fable 5.2, max effort, Mac mini worker 2. Started 2026-11-15T19:56Z (`date -u`). No file is edited except this one (and any new lemma file under `library/` named below). No commit, no push: a relay copies this file.

This is research-stage working state. It grants no status. Marks used: PROVED (every step written here, by hand), ARGUED (argument given, one named step not written out), OPEN, FAILS (explicit counterexample or failing step).

## Plan (at most eight steps; one step per response; each step is appended before the next starts)

1. **Read and pin.** FINISH rules; `parts/gap.md` (Corollary Z4, Theorem ZD-c, the test table); rows 1002, 1011, 1013 and their notes; grep the lane for earlier compactness, limit-point and rigidity attempts ((N) of row 978, limit points of effective actions, `library/gap-ladder-max.md`, `library/gap-crux-fp.md`). Duplicate-attack check against `library/open-core.md` and the FINISH rows. Output: the exact statements this note reads, with file and line.
2. **Exercise skill and literature lens.** Fetch the exercise skill at main commit 8b11ae2bb9 into a new folder under /tmp, follow it. Literature: Kenig-Merle concentration-compactness and rigidity; limits of lattice gauge measures; generalized symmetries; what is published and what each source proves.
3. **Task (1), the compactness step.** State it exactly: topology, what is kept, what can be lost. Test it against the no-rigidity models first (Lemma PT, Proposition NP, the five-dimensional test of `library/gap-crux-fp.md`, a product with a massless factor).
4. **Task (2), the rigidity statement.** State it exactly. Test it against compact U(1) (it must fail there), frozen Q_8 and 2T.
5. **Task (3), first surviving piece.** Prove it by hand, or build the counterexample.
6. **Task (3) continued** if step 5 grows long, or the second surviving piece.
7. **Task (4), the consumer.** Which form of (W) or of the seed the contradiction yields; what it changes in `parts/gap.md`.
8. **Verdict table and RESULT line.**

## Step log

(Each step below is appended when it is finished. A step that stops early says where it stopped.)

