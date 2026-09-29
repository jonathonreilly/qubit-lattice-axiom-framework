---
name: exercise
description: "Use when repo physics work hits a hard wall and the goal is to get past it: state the wall in plain words, find the premise it actually rests on, generate independent routes around it, try to kill them, run the cheapest decisive test, and report in plain language what the wall is and what it would take to pass it. Trigger on requests for 'exercise', 'assumptions exercise', 'Elon exercise', 'math sector search', 'reframing exercise', 'why are we stuck', or help getting unstuck on a physics blocker without immediately adding new theory."
---

# Exercise

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

## What the exercise is for

A wall is a place where a lane keeps failing in the same way. The exercise
exists to get past it, or to show exactly what getting past it would cost.
It is not a completeness drill and not a defence of the current framework
story.

An exercise has succeeded when it delivers at least one of:

- **a route with its first test actually run**, and the result recorded;
- **an exact price**: a proof, or a sharp argument, that the wall is
  equivalent to a named premise, so passing it is a decision rather than a
  calculation;
- **a misframing**: evidence that the wall comes from a supplied model,
  method or reading rather than from the axioms, with the cheaper question
  that replaces it.

A long map of possible attacks with nothing tried is not success. Say so if
that is all the exercise produced.

The exercise may produce routes, proof plans, runners and literature bridges.
It must not apply audit verdicts, promote claims, add axioms or primitives,
or treat existing repo content as unquestionable.

## Model And Tool Boundary

Use the strongest available reasoning model/profile, as configured by the
user. Subagents that attack the physics must be maximum-reasoning physics
agents, not lightweight summarizers; report their actual model and vendor
family, and do not describe same-family agents as independent referees. Every
main agent and subagent performs the Framework Refresher Read before its
slice. Do not use image-generation or visual artifact tools for this skill.

For theorem, proof, or multi-step bridge work, read
[`../physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md)
before fan-out, and apply its approach-family registry, concrete-return
contract and theorem-strength gap test.

For literature, browse current scholarly sources when network access is
available and cite them precisely. Literature suggests proof templates,
known no-go results and known escapes. It is never imported as authority: an
external proof is translated into repo objects, checked by a runner or proof
artifact where possible, and then reviewed like native theory.

## Framework Refresher Read

Before step 1, do a short framework refresher read. If a current repo-native
`framework-refresher` skill or command exists, use it first; otherwise read
directly:

- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full, for the Lattice, Qubit,
  Admissibility and Record baseline;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` for how approved
  primitives enter assumption, import, wall and bounded-status judgments;
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` for the scale-reference boundary;
- `docs/audit/data/axiom_premise_nodes.json` for the complete supplied
  foundation, and `docs/audit/data/premise_decision_history.json` only when
  historical provenance matters;
- `docs/ai_methodology/skills/review-loop/SKILL.md` for review and audit
  boundaries, especially the axiom/approved-primitive distinction and the
  Record guardrails;
- `docs/repo/CONTROLLED_VOCABULARY.md` when proposing names, statuses or new
  surfaces.

Each subagent states which refresher surfaces it read before giving
conclusions. The refresher prevents stale framework language. It does not
exempt framework premises from challenge: in this exercise every premise,
the axioms included, is an assumption.

## Arguments

- problem/wall text: required unless resuming a named exercise packet;
- `--artifact`: write a durable packet under `.claude/science/exercises/<slug>/`;
- `--slug SLUG`: optional packet slug;
- `--literature`: force the outside-view search;
- `--subagents N`: independent route fan-out, normally `4` or `5`;
- `--no-web`: skip live literature search and mark the limitation;
- `--test-budget H`: hours allowed for step 8's tests (default 2).

Without `--artifact`, return the report (step 9) in the conversation, with
the tables as an appendix. With `--artifact`, write:

```text
.claude/science/exercises/<slug>/
  SUMMARY.md          # the plain-language report, read first
  WALL.md             # plain and precise wall, history, what counts
  ASSUMPTIONS.md      # load-bearing assumptions ledger
  ROUTES.md           # route portfolio, kill verdicts, approach registry
  TESTS.md            # tests run, with results and scripts
  OUTSIDE_VIEW.md     # literature, math lenses, reframes
```

## Step 0: Has this wall already been mapped?

Before anything else, search the repo's own record for the wall and for
earlier attempts on it:

- landed notes and runners on main whose titles or scopes name the object;
- this lane's open PRs and probe notes;
- decision records, panel syntheses and earlier exercise packets under
  `.claude/science/exercises/` and `archive/campaigns/`;
- the probes work queue and its attempts, where one exists.

Record what is already proved, what was already tried and failed, and which
tests were already pre-registered. Do not re-derive a mapped wall or re-run a
recorded test unless the exercise names what is new. Repeated prior-art
misses are the most common way these exercises waste time.

## Step 1: State the wall twice

**Plain version**, written for a smart reader with no physics training:

- at most about 150 words, no undefined jargon;
- what we are trying to get, and in one sentence why it matters;
- what keeps happening instead;
- what exactly the evidence covers, and what it does not;
- what would count as getting past it;
- at most one picture or analogy, marked as an analogy.

**Precise version:** the target claim, theorem, import, selector, no-go or
bridge; its quantifiers and domain; allowed premises and forbidden
weakenings; required boundary or degenerate cases; outcomes that do not count
as closure; what currently fails; what would count as progress, closure,
demotion or no-go.

**Three-column split.** Sort every ingredient of the wall into:

```text
What the axioms say | What we supplied (models, comparators, readings, methods) | What was proved
```

Walls often sit in the middle column. A wall built from supplied parts
presses on those parts, not on the axioms, and the report must say so.

**Blind check.** Give a fresh agent only the plain version and ask it to say
back what is blocked and what would count as passing. Fix the plain version
until the restatement matches the precise one. Keep both neutral: do not
smuggle the desired answer, or the favoured escape, into either.

## Step 2: The load-bearing assumptions

List every premise the wall's proof or evidence actually uses. Take them
from the governing notes' premise lists and runners, not from memory. Then
add the hidden ones: finiteness, locality, smoothness, symmetry, harmonic or
perturbative level, choice of state, boundary conditions, readings of the
axioms, and "obvious" steps. Include the axioms and approved primitives,
marked as such.

Enumerate approved primitives from `docs/audit/data/axiom_premise_nodes.json`
and read their source notes. The scale-reference primitive grants the Planck
scale reference as units conversion only, with no dimensionless content. The
kinetic-isotropy primitive grants only structural OS0 kinetic-form isotropy
`c_t = c_s`, with no dynamics, Lorentz-closure theorem, absolute scale,
spacing-ratio theorem, selector or empirical content. The realized-state
primitive grants only pointwise evaluation at a supplied law-admissible
realized state; it supplies no state, selection rule, measure, typicality,
weighting or probability rule.

```text
ID | Kind (axiom / primitive / supplied model / method / reading / hidden) |
Assumption, in plain words | Where the wall uses it (path:line) |
What if it is wrong? | Already tested? (path, result) | Cheapest test |
Would dropping it change an owner decision?
```

Rules:

- Every row gets a real "what if wrong?". If no consequence is visible, say
  what would have to be inspected to know.
- Mark which rows the wall would survive without. Those are not load-bearing;
  keep them short.
- Cluster the load-bearing rows into candidate routes:

```text
Route | Assumptions challenged | Why this might open the wall |
Expected artifact | Risk | First test
```

## Step 3: First-principles reduction

An engineering reduction, reasoned upward from the minimum requirement:

1. **Make the requirement less wrong.** Is the target stated too strongly,
   or inherited from a stale route? What does the goal actually need?
2. **Delete.** Remove every premise and part the wall does not need.
3. **Shrink.** Find the smallest object, carrier, sector or toy model in
   which the wall still bites. If it can be built in under an hour, build it
   and confirm that it bites.
4. **Split.** Is it one wall, or two independent bits? Is it a selector,
   readout, dynamics, normalization or representation problem?
5. **Price it.** If the target cannot be derived, can the exact missing input
   be proved instead of written about?

## Step 4: Independent routes

Fan out to `N` agents (or context-isolated passes when agents are
unavailable). Give each a neutral, route-local brief built from step 1's
precise version and step 2's ledger. Do not give any agent the favoured
approach or another agent's conclusions. Choose the briefs so that the
approach families are materially different. Always include:

- at least one lens from outside the lane's own vocabulary, for example how
  another field got past the same kind of wall;
- one agent whose brief is to argue that the wall is misframed, and to name
  the cheaper question that replaces it.

Each agent returns one to three routes under the concrete-return contract: a
lemma with its proof skeleton, a construction, an equation or invariant, a
falsifier, or an exact missing obligation. For each route:

```text
Route | Family (object, mechanism, terminal obligation) | Premise it drops or changes |
What you would have to believe for it to work | First artifact | Cost |
What it would change if it worked
```

Reject vague returns ("topology might help"). A return must name the object
that changes, the invariant or theorem type that might bite, and the first
concrete artifact.

## Step 5: Outside view

Where network access allows, and always with `--literature`:

- **known results first:** no-go theorems and known escapes for this kind of
  wall, and whether the repo's wall is a case of one;
- **proof templates:** arguments that could be translated.

```text
Source | What it shows | Premises | Maps to the repo? | What does not map |
Translation or runner | Import risk | Citation
```

**Mathematical lenses.** Choose them from the wall's structure; do not run a
fixed checklist. For each lens used, give the object that changes, the
invariant or theorem type, a minimal toy example, what would falsify it and
the first artifact. Lenses considered and found empty get one line each.

**Reframes.** Try moving the boundaries that repo walls usually hide behind:

- pre-record vs recorded;
- object vs readout;
- selector vs admissible dial;
- dynamics vs kinematics;
- finite carrier vs limiting family;
- exact theorem vs bounded theorem vs no-go;
- value derivation vs value availability;
- supplied model vs axiom content;
- local pattern vs global or collective structure;
- obstruction vs missing input.

```text
Reframe | What moves | What becomes simpler | What becomes harder | New route | First test
```

A reframe is useful only if it is stated in framework objects, not lane
fixtures.

## Step 6: Try to kill every route

Before ranking, give each surviving route to a different agent (or pass)
whose brief is to break it. It checks:

- whether the route quietly assumes the target;
- whether it contradicts a landed result;
- whether it was already tried (step 0);
- whether its terminal obligation is target-equivalent. If it is, the route
  is `blocked-equivalent` under the proof-search governance and is not near
  closure.

Record a verdict for every route: survives, wounded (with the named gap) or
dead (with the reason).

## Step 7: Rank

```text
Rank | Route | Family | Premise challenged | What you would have to believe |
Terminal obligation | Strength vs target | Kill verdict | Cost | First artifact |
What it changes | Stop/reopen condition
```

Rank by what the route would change if it worked, divided by what it costs
to find out. A cheap test that would move an owner decision outranks an
elegant reduction that ends at a target-equivalent lemma.

## Step 8: Run the cheapest decisive test

Within the test budget, run the first artifact of the best-ranked route that
can be tested inside it. Where budget allows, run several. For each test:

- pre-register the pass and fail reading before running;
- keep the script, the output and the result;
- say plainly whether it moved the wall, and in which direction.

If no route can be tested inside the budget, say why, and give the smallest
test that would decide the top route and what it needs. A deferred test must
name who or what it is waiting on: the owner, a probe queue, or a missing
input.

Test results are exercise evidence, not repo claims. A result worth keeping
goes through the normal note, runner and review path.

## Step 9: Report

The report leads with plain language. Write it for the owner, who will act
on it. Every claim in it carries one label: **proved** (with its path),
**checked** (a finite or numerical test), **suggested** (an argument not yet
checked) or **reading** (an interpretation).

1. **The wall, in plain words:** step 1's plain version, corrected by the
   exercise.
2. **What the exercise found:** three to six plain sentences. Include what
   changed since the exercise started, and the tests run with their results.
3. **Routes worth doing:** at most three. For each, say what you would have
   to believe, what it costs, the first test, and what it would change.
4. **What not to do next,** with the reason.
5. **The exact price,** if the exercise found one: the premise or decision
   the wall is equivalent to.
6. **Appendix:** the tables from steps 1–8 and the approach registry.

The report must not claim the wall is solved without a proof, a decisive
runner or a decisive no-go artifact.

## Non-Negotiables

- Plain language first. The report's first three sections contain no
  undefined jargon and no lane fixture presented as framework content.
- Do not over-rely on existing framework content. It is evidence, and the
  exercise may find it wrong, overbroad or misframed.
- Do not miss approved primitives or overstate what they grant (step 2).
- Do not apply audit verdicts, promote claims, add axioms or primitives, or
  declare the wall solved without an actual proof, runner or decisive no-go
  artifact. Candidate axiom wording may be drafted only as an option for the
  owner, marked as not adopted.
- Do not import literature as proof. Translate it into repo-native theory,
  check it, and cite the source.
- Report honestly when the exercise produced only a map.
