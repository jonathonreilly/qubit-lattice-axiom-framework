lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T09:19Z

# Queue row 1021, `gap-registry-after-checks-max`: the route registry after the fourteen cross-provider checks, then an attack on the top route

Worker: Claude Fable 5.2 (max), Mac mini worker 1, pinned at commit ae561a40d of `claude/ym4d-hard-route`.
Started 2026-11-15T21:19Z (`date -u`). Research-stage working state. Nothing here is a public claim, and
nothing here is checked by another model.

Marks used: PROVED (every step written here, by hand), ARGUED (argument written, a step is not complete),
OPEN, FAILS (a counterexample or a failed step is written). GUIDE marks a numeric run; a run can refute
or guide, and no status rests on one.

## 0. Plan (save protocol; at most eight steps, one step per response, result appended after each)

1. Read `parts/gap.md` in full. Fetch the exercise skill at main commit 8b11ae2bb9 and the reference
   file it names into a new folder under /tmp. Write down its registry and ranking steps and its tests.
2. Read the RESULT lines and verdict tables of the fourteen gpt-6-astra checks (rows 960, 963, 965,
   968, 970, 977, 978, 982, 987, 988, 993, 996, 998, 1000). Record each verdict with its line anchor.
3. Read today's rows 1011, 1013, 1016, 1017 and their checks 1014, 1015, 1019, 1020 (RESULT lines and
   verdict tables). Record (W), Theorem CR and (LIOU) with anchors. Row 1018 (short-step hunt) is not redone.
4. Task (1): the table of every discard verdict, filter and lead rule the lane relies on, with its
   status after the checks: stands, narrowed (to what), or no longer supported (by which check line).
5. Task (2): the route registry rebuilt from that table: terminal obligation, strength against (W) or
   Theorem CR, status, cheapest decisive next step, rank, and which routes were blocked only by a
   verdict that no longer stands.
6. Task (3a): the top route. Registry grep first (`library/open-core.md`, FINISH rows). Then the first
   lemma, stated in full, and the first attack by hand.
7. Task (3b): continue the attack, or build the counterexample; a numeric run only to refute or guide,
   under the numeric lock.
8. Re-read every item marked PROVED here, print each cited line anchor, write the work-item briefs and
   the RESULT line.

## Status log

- 2026-11-15T21:19Z: file created with the plan. Nothing else done yet.
