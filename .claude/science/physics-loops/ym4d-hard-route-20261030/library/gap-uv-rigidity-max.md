lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T12:21Z

# gap-uv-rigidity-max: rigidity with kept ultraviolet data (queue row 1028)

Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit d8496276a.
Started 2026-11-16T00:21Z. Research-stage working state. Nothing here grants status.
No subagents. No commit, no push: the relay copies this file.

Marks used below: PROVED (every step written here, checkable by hand), ARGUED
(argument given, a named step not written out), OPEN, FAILS (with the failing step).

## Plan (at most eight steps; one step per response; each result is appended here)

1. **Sources and scope.** Read the row's read-first list (`parts/gap.md`;
   `library/gap-compact-rigidity-max.md` with both checks; the repaired (W) of
   `library/gap-zd-astra.md` item 18; `library/gap-dichotomy.md`) and the exercise
   skill at main commit 8b11ae2bb9. Run the duplicate check against
   `library/open-core.md` and the FINISH rows. Record the exact definitions this
   item reads: D, CE, Proposition SI, Proposition OM, (LIOU), Theorem D2, Lemma PT-inf.
2. **Task (1), link (a).** State the kept ultraviolet condition exactly. Decide
   whether CE's construction keeps it or can be strengthened to keep it, and what
   uniformity in the trajectory that needs. Test it against Theorem D2, Lemma PT-inf
   and the product with a massless factor.
3. **Task (2), link (b).** Prove or refute: a uniformly recurrent element with a
   limit c at minus infinity has D constant equal to c. Use the exact definition of
   uniformly recurrent in Proposition OM.
4. **Task (3), the free value.** Compute or bound c for SU(2) on the symmetric
   torus. Decide whether the constant element D = c is a critical element under the
   engine's axioms.
5. **Task (4), controls.** Run the whole chain (a)-(b)-(c) against compact U(1),
   frozen Q_8 and 2T, and the five-dimensional test of `library/gap-crux-fp.md`.
   The chain must fail on each control or name what separates it.
6. **Surviving link.** If a link survives, write its first lemma and prove it by
   hand, or build the counterexample.
7. **Exercise record.** Fill the output format the exercise skill asks for
   (wall statement, attempts, what each attempt gave, the residual).
8. **Verdicts.** Table of marks per task and link, credits, what stays open, and
   the RESULT line.

## Status log

- 00:21Z file created, plan written. Step 1 not started.
