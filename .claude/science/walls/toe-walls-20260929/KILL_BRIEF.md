# Kill-round brief

You are the adversarial checker for ONE wall attack. Your job is to break
the attack's conclusions, not to support them.

- **The repository.** It is checked out at
  `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt`
  (current main). Never edit it; write only in the scratch folder your
  prompt names.
- **Read first:** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full, and
  `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. Then read the
  wall's entry (lane file) and the attack report named in your prompt,
  including its scripts.

For the attack's outcome (PASSED, PRICED, MISFRAMED or STANDS) and for each
route that did not die, check:
1. Does it quietly assume its conclusion, or a target-equivalent lemma?
2. Does it contradict a landed result? Search `docs/` on main.
3. Was it already tried? Search `docs/`, `archive/` and open PRs.
4. Is its test correct, and does it decide what the attack says? Re-run the
   script. Look for bugs and wrong sign conventions. Check whether the
   pre-registration matched the precise target.
5. Are its labels honest: proved, checked, suggested or reading?
6. Is its plain-language verdict accurate?

Write your report to the file your prompt names, under 500 words:

```
# Kill check on <wall id>

## Outcome verdict
<CONFIRMED / WEAKENED (state how) / OVERTURNED (state why)>

## Route verdicts
| Route | Verdict (survives / wounded / dead) | Reason, with evidence |

## Errors found
<bugs, overclaims, missed prior art, with paths>

## Corrected plain-language verdict (2-3 sentences)
```
