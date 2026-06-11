# /exercise — Physics Wall Exercise

Run the repo-native exercise skill from:

`docs/ai_methodology/skills/exercise/SKILL.md`

## Invocation

```text
/exercise "<physics wall or blocker>" [--artifact] [--slug SLUG] [--literature] [--subagents N] [--no-web]
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
3. Perform the Framework Refresher Read required by the skill before executing
   the exercise. If a current repo-native `framework-refresher` skill or
   command exists, read/use it first; otherwise read the current minimal axioms,
   primitive registry check, approved primitive source notes, axiom-premise
   registry, Tier-A admissions registry, review-loop skill, and controlled
   vocabulary directly.
4. If subagents are used, require every subagent to perform the same framework
   refresher read and state which refresher surfaces it read before giving
   conclusions.
5. State the wall neutrally before proposing routes.
6. Build the assumptions ledger from approved axioms/primitives upward through
   every explicit and implicit premise used by the stuck lane.
7. For every assumption, record what opens if it is wrong.
8. Run the Elon-style first-principles reduction: weaken requirements, delete
   unnecessary premises, find the minimum object, and identify the fastest
   falsifying runner or proof artifact.
9. Run the literature proof search unless `--no-web` is supplied or network
   access is unavailable. Literature suggests proof templates only; it is not
   imported as repo authority without translation, review, and audit.
10. Run the broad mathematics sector search and require each sector entry to
   name a concrete object, invariant/tool, and first artifact.
11. Run the reframing exercise, especially across pre-record/recorded,
   selector/dial, dynamics/kinematics, and central-sector/within-sector
   boundaries.
12. Synthesize a ranked attack-vector portfolio with first artifacts and stop
    conditions.
13. If `--artifact` is supplied, write the durable packet under
    `.claude/science/exercises/<slug>/`; otherwise return the structured
    exercise in the response.

## Non-Negotiables

- Use maximum available reasoning. If subagents are used, they must be
  maximum-thinking physics agents and must run the framework refresher before
  their assigned exercise.
- Do not over-rely on existing framework content. It may be useful evidence,
  but the exercise is allowed to find it wrong, overbroad, or misframed.
- Do not miss approved primitives. The registered `scale_reference_primitive`
  grants the Planck scale reference as units conversion only, without making
  downstream rows bounded and without granting dimensionless content. The
  registered `kinetic_isotropy_primitive` grants only structural OS0
  kinetic-form isotropy `c_t = c_s`; it does not supply dynamics, a
  Lorentz-closure theorem, scale, spacing-ratio theorem, selector, or empirical
  content. The registered `realized_state_primitive` grants only pointwise evaluation at a supplied law-admissible realized state; it does not supply a state, state-selection rule, measure, typicality or genericity assumption, weighting, probability rule, or any state-contingent value (quantities that vary across the law-admissible family remain registered data).
- Do not apply audit verdicts, promote claims, add axioms/primitives, or
  declare the wall solved without an actual proof, runner, or decisive no-go
  artifact.
- Do not import literature as proof. Translate it into repo-native theory,
  script/review it, and cite the source.
