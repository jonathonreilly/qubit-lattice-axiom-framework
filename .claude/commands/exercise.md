# /exercise — Physics Wall Exercise

Run the repo-native exercise skill from:

`docs/ai_methodology/skills/exercise/SKILL.md`

`docs/ai_methodology/procedures/research.md` step 3 says when a target runs
it. The skill says how. This file is a summary; where the two differ, the
skill wins.

## Invocation

```text
/exercise "<physics wall or blocker>" [--artifact] [--slug SLUG] [--subagents N] [--no-web] [--test-budget H]
```

Examples:

```text
/exercise "we cannot derive the K-real generation readout instrument"
/exercise "Koide r=1/2 is available as a dial but not selected" --artifact
/exercise "Planck-scale primitive keeps leaking into bounded status" --subagents 4
/exercise "every attack on this lemma stops at the same step; audit the tests that discarded the other tools"
```

## Required Behavior

1. Read the skill file above before acting.
2. Perform the skill freshness check described in
   `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`.
3. Perform the Framework Refresher Read required by the skill: the current
   minimal axioms, primitive registry check, approved primitive source notes,
   axiom-premise registry, derivation-obligation registry, review-loop skill
   and controlled vocabulary. Every subagent does the same and states which
   surfaces it read. A standalone proof target that reads no framework axiom
   reads its `GOAL.md` contract instead, and says so.
4. Write the output file as you go: header (model, effort, commit, what the
   run did not cover), a status block kept current, then each step on disk
   before the next is thought through. Every item and statement carries a
   mark; no mark is stronger than its weakest input.
5. Step 0: locate the repo's own record of the wall (landed notes, open PRs,
   queue rows, registries, decision records, panels, earlier exercises, held
   blocks, candidate packs), by object as well as by title. Sort it into
   "open now" (target, wall, definitions, statements of theorems) and
   "closed until step 5" (attack files, route notes, digests of methods,
   set-aside lists). Reuse the literature record, or run and record the
   search. `--no-web` makes that search offline, with unavailable or
   unverified sources labelled explicitly.
6. Step 1: state the wall twice, plainly for a non-physicist and precisely.
   Check the plain version with a blind restatement where a fresh agent is
   allowed.
7. Step 2: the inventory. List what is known to be true, each item with a
   mark: definition, axiom or primitive, supplied choice, theorem (source,
   standing, how much of the source was read), or belief.
8. Step 3: reason up from the inventory only. What follows at once; the
   least a solution must contain; the smallest object; where the result can
   come from; whether the requirement is stated too strongly; the price.
   End with numbered conclusions.
9. Step 4: the assumptions table, in six groups: target, formulation,
   reduction, discard tests, beliefs, working rules. For each row: where it
   is used, needed or only habit, what follows if it is wrong, whether a
   change makes the problem easier, the check. Owner rules are listed and
   kept. Rank the rows by how much the problem changes if they are dropped.
10. Step 5: open the closed files and compare. Mark each item yes, partly or
    new, with the place. Search the whole lane record for the statement
    before writing "new", and write the search scope.
11. Step 6: the blockage. List every method that was set aside, with the
    reason given. Say from the definitions what a tool must do. Audit every
    discard test in its valid form: a method is refuted as a tool only by a
    model in its class where its hypothesis holds and the needed statement
    fails; otherwise the test only says what a proof of the hypothesis must
    use, and from which parameter value. Say how each test's failure is
    known (theorem or belief). Re-judge every verdict.
12. Step 7: routes. Take them from the dropped assumptions, the tools that
    came back and the new forms of the target; add independent passes across
    materially different families (`--subagents N`, default 0 = isolated
    passes), with one lens from outside the lane and one pass arguing that
    the wall is misframed. Revisit the literature for new questions only.
    Give every route to a different pass to break; target-equivalent endings
    are `blocked-equivalent`. Rank by what a route would change, divided by
    its cost.
13. Step 8: real attempts on the best two or three routes: prove the first
    lemma, find a counterexample, or reduce to one exact statement. Search
    the open registry and queue before each attempt. Pre-register every
    run; never change a reading after seeing the result; say exactly which
    class a search covered; compute decisive quantities directly. Report and
    preserve raw failures immediately. Before interpreting them as negative
    conclusions or no-go results, obtain a fresh adversarial check under the
    allowed review configuration, and label same-family checks honestly. A
    deferred test names what it is waiting on.
14. Step 9: report plain language first: the wall, what was found, filters
    corrected, at most three routes, what not to do, the exact price, work
    items as complete briefs (the first is the check request), and one
    `RESULT:` line. Read the report's strong words against what the run did.
    With `--artifact`, write the packet under
    `.claude/science/exercises/<slug>/`; inside a target, write the one file
    the brief names.

## Non-Negotiables

- Use the strongest available reasoning. Use subagents only when the caller
  allows them; they must be maximum-reasoning physics agents that run the
  framework refresher before their slice. Report their actual model family
  and do not call same-family agents independent referees.
- Fresh first, compare later: steps 2 to 4 are written with the attack files
  closed; nothing is "new" without the search of step 5.
- A discard test refutes a tool only in the valid form of step 6. Every
  set-aside method is re-judged.
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
- Owner rules and the limits of the target's contract are not broken in the
  exercise. They are questioned on paper only.
- Do not apply audit verdicts, promote claims, add axioms, primitives or
  imports, or declare the wall solved without an actual proof, runner, or
  decisive no-go artifact. A price, a misframing or a corrected filter needs
  a proof or decisive checked evidence.
- A run may refute or guide. It never discharges a statement by itself.
- Name an axiom change only as a price. Draft wording only when the owner asks,
  starting from a layman-simple sentence.
- Do not import literature as proof. Translate it into repo-native theory,
  script/review it, and cite the source.
- Nothing the exercise writes is `checked`. Say who wrote it and who checked
  what.
- A map of attacks with nothing tried is reported as exactly that.
