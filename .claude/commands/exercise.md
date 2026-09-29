# /exercise — Physics Wall Exercise

Run the repo-native exercise skill from:

`docs/ai_methodology/skills/exercise/SKILL.md`

## Invocation

```text
/exercise "<physics wall or blocker>" [--artifact] [--slug SLUG] [--literature] [--subagents N] [--no-web] [--test-budget H]
```

Examples:

```text
/exercise "we cannot derive the K-real generation readout instrument"
/exercise "Koide r=1/2 is available as a dial but not selected" --artifact --literature
/exercise "Planck-scale primitive keeps leaking into bounded status" --subagents 5
```

## Required Behavior

1. Read the skill file above before acting.
2. Perform the skill freshness check described in
   `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`.
3. Perform the Framework Refresher Read required by the skill. Every subagent
   does the same and states which surfaces it read.
4. Step 0: search the repo's own record (landed notes, open PRs, decision
   records, panels, earlier exercises, probe queues) for the wall and earlier
   attempts before generating anything.
5. Step 1: state the wall twice, plainly for a non-physicist and precisely.
   Sort its ingredients into what the axioms say, what was supplied and what
   was proved. Check the plain version with a blind restatement.
6. Step 2: list every premise the wall actually uses, with path:line, a real
   "what if wrong?", whether it was already tested, and the cheapest test.
7. Step 3: reduce from first principles. Loosen the requirement, delete
   premises, find the smallest toy where the wall still bites, and build it if
   cheap.
8. Step 4: fan out independent routes with neutral briefs across materially
   different families. Include one lens from outside the lane and one agent
   arguing that the wall is misframed. Every return must be concrete.
9. Step 5: outside view. Known no-gos and escapes first, then proof templates.
   Choose mathematical lenses from the wall's structure, and try the reframes.
10. Step 6: give every route to a different agent to break. Record a kill
    verdict; target-equivalent endings are `blocked-equivalent`.
11. Step 7: rank by what a route would change, divided by its cost.
12. Step 8: run the cheapest decisive test or tests within the budget,
    pre-registered, and record the results. A deferred test names what it is
    waiting on.
13. Step 9: report plain language first. Label every claim proved, checked,
    suggested or reading. Give at most three routes, what not to do, and the
    exact price if one was found. With `--artifact`, write the packet under
    `.claude/science/exercises/<slug>/`.

## Non-Negotiables

- Use the strongest available reasoning. Subagents must be maximum-reasoning
  physics agents that run the framework refresher before their slice. Report
  their actual model family and do not call same-family agents independent
  referees.
- Do not over-rely on existing framework content. It may be useful evidence,
  but the exercise is allowed to find it wrong, overbroad, or misframed.
- Do not miss approved primitives. The registered `scale_reference_primitive`
  grants the Planck scale reference as units conversion only, without making
  downstream rows bounded and without granting dimensionless content. The
  registered `kinetic_isotropy_primitive` grants only structural OS0
  kinetic-form isotropy `c_t = c_s`; it does not supply dynamics, a
  Lorentz-closure theorem, scale, spacing-ratio theorem, selector, or empirical
  content. The registered `realized_state_primitive` grants only pointwise
  evaluation at a supplied law-admissible realized state; it does not supply
  a state, state-selection rule, measure, typicality or genericity assumption,
  weighting, probability rule, or any state-contingent value (quantities that
  vary across the law-admissible family remain registered data).
- Do not apply audit verdicts, promote claims, add axioms/primitives, or
  declare the wall solved without an actual proof, runner, or decisive no-go
  artifact.
- Do not import literature as proof. Translate it into repo-native theory,
  script/review it, and cite the source.
- A map of attacks with nothing tried is reported as exactly that.
