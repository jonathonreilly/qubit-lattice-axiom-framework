lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-12T02:35Z

# exercise-skill-v2 (FINISH row 721)

Written by Claude Fable 5.2 at high effort (Mac mini worker 1), at commit 3d74e7aa3 of `claude/ym4d-hard-route`.
This is a process item. It makes no physics claim and grants no status. Nothing here is committed or pushed by the worker; the lead lands changes by a pull request to main.

Status of this file: in progress. Parts are appended in the order of the queue row: (0) sources read, (1) evaluation, (2) improved skill, (3) command wrapper and `openai.yaml`, (4) edits to the process stack, (5) application to this lane.

## 0. Sources read

Repo search (rule "Repo first"): `grep` for `exercise-skill`, `skills/exercise`, `commands/exercise` in this checkout. Hits: FINISH row 721 only (the brief), and the local copy of the skill, which is older than main. No earlier run of this item exists; this file starts it. Open-lemma check (rule 0a): this row attacks no lemma, so there is nothing to match in `library/open-core.md`.

Fetched from the public repository at main commit 1ddab64621 into `/tmp/exskill-v2-src/` (scratch, not committed), each read whole:

| File at 1ddab64621 | Lines | Note |
|---|---|---|
| `docs/ai_methodology/skills/exercise/SKILL.md` | 424 | the existing skill ("v1" below) |
| `docs/ai_methodology/skills/exercise/agents/openai.yaml` | 7 | |
| `.claude/commands/exercise.md` | 97 | |
| `.claude/commands/first-principles.md` | 168 | |
| `docs/ai_methodology/SCIENCE_WORKFLOW.md` | 81 | **At this commit it is a section map only** (line 6: "It adds no rule and grants no status"). It names no exercise, panel, blocked lane or author run. |
| `docs/ai_methodology/RULES.md` | 200 | not in the row's list; read because the map sends every rule there. At its 200-line budget (section 7). |
| `docs/ai_methodology/SETTINGS.md` | 93 | not in the row's list; method defaults |
| `docs/ai_methodology/PROCEDURES.md` | 48 | not in the row's list; line 32 says `research` supersedes the `exercise` skill and command as entry point |
| `docs/ai_methodology/procedures/research.md` | 150 | not in the row's list; **the one place that says when the exercise runs** (step 3, lines 77-78, and the step-reference row at line 147). At its 150-line budget. |
| `scripts/sync_methodology_skills.py` | 301 | searched only; it copies skill folders and reads no skill text |

**Finding that changes part 4.** The row asks for edits to `SCIENCE_WORKFLOW.md` that say when the exercise runs. At 1ddab64621 that rule lives in `procedures/research.md` step 3, and `RULES.md` section 7 says "One home per rule". So part 4 gives the rule edit for `procedures/research.md` (line-neutral, the file is at its budget), a pointer-only edit for `SCIENCE_WORKFLOW.md`, and the edit for `first-principles.md`. The lead chooses. The local checkout's `SCIENCE_WORKFLOW.md` (242 lines) is an older file and is not the edit target.

From this checkout, read whole: `library/gap-crux-fp.md` (502 lines), FINISH rows 712 and 716, `library/gap-crux-fp-check.md`, `library/gap-skeleton-final.md` Section 13.14; FINISH rows 697 to 726 and Section 13 of the skeleton for part 5.
