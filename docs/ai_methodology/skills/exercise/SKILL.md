---
name: exercise
description: "Use when repo physics or proof work hits a hard wall (a blocked lane) and the goal is to get past it or to price it: state the wall in plain words, list what is known to be true with a mark on every item, reason up from that list before reading earlier attacks, list every assumption (target, formulation, reduction, discard tests, beliefs, working rules) and ask what follows if it is wrong, audit the tests that were used to discard ideas, re-judge every method that was set aside, compare with earlier work, make real attempts, and report in plain language. Trigger on requests for 'exercise', 'assumptions exercise', 'first-principles exercise', 'Elon exercise', 'math sector search', 'reframing exercise', 'audit the discard tests', 'why are we stuck', or help getting unstuck on a blocker without immediately adding new theory."
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

The exercise has two halves. The first half looks at the problem with the
earlier attacks closed: what is known to be true, and what follows from that
alone. The second half looks at the lane's own filters: its assumptions, the
tests it used to discard ideas, and its verdicts on the methods it set aside.
A lane can be blocked by a filter as well as by the mathematics.

An exercise has succeeded when it delivers at least one of:

- **a route with its first test actually run**, and the result recorded;
- **an exact price**: a proof, or decisive checked evidence (an exhaustive
  finite certificate, or a runner backed by a theorem that makes it
  decisive, where the target's contract allows such evidence), that the wall
  is equivalent to a named premise or to one exact open statement;
- **a misframing**: checked evidence (a proof, runner or exact counterexample)
  that the wall comes from a supplied model, method, reading or habit rather
  than from the axioms or the target, together with the question that
  replaces it;
- **a corrected filter**: a discard test or a verdict shown false or too
  strong in its valid form (step 6), with the methods that come back and the
  range where they come back.

An argument that has not been checked counts as a suggestion, not as a price,
a misframing or a corrected filter.

A long map of possible attacks with nothing tried is not success. Say so if
that is all the exercise produced.

The exercise may produce routes, proof plans, lemmas with proofs, runners and
literature bridges. It must not apply audit verdicts, promote claims, add
axioms, primitives or imports, or treat existing repo content as
unquestionable.

## Relation to other procedures

- `docs/ai_methodology/procedures/research.md` step 3 says when a target
  runs the exercise. This file says how.
- `/first-principles` derives one target from the allowed premises. The
  exercise uses the same discipline on a wall: the inventory of step 2 is
  that command's premise ledger, with a mark on every entry. A route that
  leaves step 7 as a derivation goes to `/first-principles`.
- A race or a panel is several independent attempts or readers on one
  question. It answers a question that is already posed. The exercise asks
  whether the question and the filters are right. On a blocked part, run the
  exercise first and brief the race or panel from its work items (step 9).
  The judicial panel of the audit path is a different thing; the exercise
  never touches it.
- The exercise is not a check. Its statements are `argued` until
  `procedures/check.md` records a check of them.

## Model And Tool Boundary

Use the strongest available reasoning model/profile, as configured by the
user. Report the actual model, effort and provider at the top of the output.
Use subagents only when the caller allows them. Subagents that attack the
physics must be maximum-reasoning physics agents, not lightweight
summarizers; report their actual model and vendor family, and do not describe
same-family agents as independent referees. Every main agent and subagent
performs the Framework Refresher Read before its slice. Do not use
image-generation or visual artifact tools for this skill.

For theorem, proof, or multi-step bridge work, read
[`../physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md)
before step 7 and apply all of it: the exact target contract, the
approach-family registry, independent rounds, the concrete-return contract,
the theorem-strength gap test, the candidate-proof audit, and the round
synthesis and handoff.

For literature, browse current scholarly sources when network access is
available and cite them precisely. Literature suggests proof templates,
known no-go results and known escapes. It is never imported as authority: an
external proof is translated into repo objects, checked by a runner or proof
artifact where possible, and then reviewed like native theory. A published
theorem enters the inventory (step 2) with its source and with how much of it
was read.

A run (a script, a numerical test, a search) can refute a statement or guide
a guess. It discharges nothing by itself. Where the target's contract forbids
computer-assisted steps, every statement the exercise marks as proved has a
written proof.

## Framework Refresher Read

Before step 0, do a short framework refresher read. If a current repo-native
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
- `docs/audit/data/derivation_obligations.json` for registered derivation
  obligations that touch the wall;
- `docs/ai_methodology/skills/review-loop/SKILL.md` for review and audit
  boundaries, especially the axiom/approved-primitive distinction and the
  Record guardrails;
- `docs/repo/CONTROLLED_VOCABULARY.md` when proposing names, statuses or new
  surfaces.

Each subagent states which refresher surfaces it read before giving
conclusions. The refresher prevents stale framework language. It does not
exempt framework premises from challenge: in this exercise every premise,
the axioms included, is an assumption.

A target whose `GOAL.md` contract reads no framework axiom or primitive (a
standalone proof target) reads that contract and its rules in place of the
list above. Say in the output that this replacement was made.

## Arguments

- problem/wall text: required unless resuming a named exercise packet or
  working from a caller's brief;
- `--artifact`: write a durable packet under `.claude/science/exercises/<slug>/`;
- `--slug SLUG`: optional packet slug;
- `--subagents N`: independent route fan-out in step 7; default `0`, which
  means context-isolated passes by the main agent;
- `--no-web`: perform the literature search offline and mark unverified or
  unavailable sources;
- `--test-budget H`: hours allowed for step 8's attempts and tests (default 2).

**The brief.** A caller that runs the exercise inside a target names, in its
brief: the wall (file and section of the statement); where the definitions
are; the files to keep closed until step 5 (attack files, route notes,
digests of methods, lists of set-aside methods); the output file; the budget;
the binding limits (for example no commits, no subagents). Without a brief,
the main agent makes this list in step 0 and writes it down.

Without `--artifact` and without a brief, return the report (step 9) in the
conversation, with the tables as an appendix. Inside a target folder, write
one file, the one the brief names. With `--artifact`, write:

```text
.claude/science/exercises/<slug>/
  EXERCISE.md            # the run, in step order, appended step by step;
                         # opens with the header and the status block
  SUMMARY.md             # the plain-language report (step 9), read first;
                         # it links to EXERCISE.md rather than copying it
  APPROACH_REGISTRY.md   # the proof-search governance registry
  scripts/               # step 8's scripts; outputs beside them
```

## Output rules

**Write as you go.** Put each step on disk before you think about the next
step. Text on disk is the only thing that survives a lost session. When a
step grows long, stop, write what you have and the exact point where you
stopped, and continue. If the output file already holds work of an earlier
run, keep it and continue from it.

**Header.** The file opens with: who wrote it (provider, model, effort,
session), the commit, the date, the words "nothing in this file is checked by
another model" until a check record exists, and a list "what this run did not
cover". Keep that list true: a source read in part is listed as read in part.

**Status block.** After the header, keep one short block current: one line
per step, done or not, with its main result. Bring it up to date after each
step, so that the file is complete if the run ends early.

**Marks.** Every item of the inventory and every statement of the run
carries one mark. A mark is never stronger than the weakest input it names.
Standing words are those of `docs/ai_methodology/RULES.md` section 1.

```text
Inventory items (step 2):
  DEF       a fact of the definitions, with the place of the definition
  AXIOM     a framework axiom or approved primitive, with what its source
            note grants
  SUPPLIED  a model, comparator, reading, convention or method that we chose
  THM       a theorem, with its source and its standing:
              checked (path of the check record) | argued | retained
            for a published theorem also how it was read in this run:
              read in full | read in part (which pages) | recalled
            and whether the source writes the proof for the case used
  BELIEF    from physics, numerics, experience or habit; used in no proof

Statements made by the run:
  argued    proved here from named inputs; each input with its mark
            ("argued, given X" when an input X is open, recalled or a belief)
  refuted   an explicit counterexample, written so that it can be checked
  guide     a run or a number; it decides nothing
  reading   an interpretation
  open      not proved
```

Nothing the exercise writes is `checked`. A statement becomes `checked` only
through a check record by a model that did not write it (`RULES.md`
section 3). Say who checked what in plain words: "proved by <model>, not yet
checked", "checked line by line by <model> (same provider), first failing
step none".

## Step 0: Locate the record, and keep the attack files closed

After the refresher read and before generating anything, find where the
repo's own record of the wall is. Do not read the arguments yet.

- landed notes and runners on main whose titles or scopes name the object;
- this lane's open PRs, probe notes, queue rows, registries and indexes;
- decision records, panel syntheses and earlier exercise packets under
  `.claude/science/exercises/` and `archive/campaigns/`;
- held or unlanded blocks on campaign and backlog branches, and candidate
  packs with kill sheets under `.claude/science/candidates/`.

Search by the physical or mathematical object and its synonyms, not only by
words in titles: unlanded blocks are where earlier answers most often hide.

Sort what you find into two lists and write both down:

- **Open now:** the target statement, the statement of the wall, the
  definitions, and the statements (not the proofs, not the route discussion)
  of theorems that the lane has `checked` or cites.
- **Closed until step 5:** attack files, route notes, digests and surveys of
  methods, lists of set-aside methods, earlier exercises on the same wall.

The purpose of the closed list is a fresh look, not ignorance. Step 5 opens
every file on it, and no item is called new before that.

Literature: reuse the lane's literature record. If the lane has none, run
the search described in step 7 now and record it, including a search that
found nothing. Before step 5, read from it only statements of results:
theorems, known no-go results, known counterexamples. With `--no-web`, search
available local sources and name missing coverage; do not invent a completed
search.

Do not re-derive a mapped wall or re-run a recorded test unless the exercise
names what is new.

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
demotion or no-go. Where the lane has a checked statement of the wall, quote
it with its path and do not rewrite it.

**Blind check.** When a fresh agent is allowed, give it only the plain
version and ask it to say back what is blocked and what would count as
passing. Fix the plain version until the restatement matches the precise
one. Otherwise correct the plain version in step 9 and say that no blind
check ran. Keep both versions neutral: do not smuggle the desired answer, or
the favoured escape, into either.

## Step 2: The inventory: what is known to be true

List what is known to be true about the problem. Use only the "open now"
list of step 0, the refresher read and the literature's statements of
results.

```text
# | Item, in one or two sentences | Mark (DEF / AXIOM / SUPPLIED / THM / BELIEF) |
Source (path:line or citation) | Standing and reading state (for THM)
```

Rules:

- Every item gets a mark. An item with no mark is not in the inventory.
- A theorem stated from memory is marked `recalled`, with what was not
  re-read. A theorem read in part names the pages read.
- A belief stays in the table. It is marked BELIEF and no proof step may use
  it. Beliefs from numerics name the numbers and where they come from.
- Include what is known about the nearest models where the target is false
  or true for a known reason. These become the tests of step 6.
- Framework lanes: enumerate approved primitives from
  `docs/audit/data/axiom_premise_nodes.json` and read their source notes
  (step 4 says what each grants). Walls often sit in the SUPPLIED items. A
  wall built from supplied parts presses on those parts, not on the axioms,
  and the report must say so.

## Step 3: Reason up from the inventory

Reason only from the items of step 2. Do not import the framing of the
earlier work, and do not argue by analogy with an earlier attempt. Answer, in
this order, and prove what can be proved in a few lines:

1. **What follows at once.** Short facts that the inventory gives directly.
   Each one names the items it uses.
2. **The least a solution must contain.** What must any proof, derivation or
   construction of the target contain, whatever its method? Which known
   models must it fail on, and so which property must it use?
3. **The smallest object.** What is the smallest object, carrier, sector or
   finite set of numbers that holds the information the target needs? If a toy
   model in which the wall still bites can be built in under an hour, build
   it and confirm that it bites.
4. **Where the result can come from.** Which mechanisms could make the
   target true, and in which ways can it fail? Is it one problem or several
   (by range, by sector, by scale; a selector, readout, dynamics,
   normalization or representation problem)?
5. **Make the requirement less wrong.** Is the target stated too strongly,
   or inherited from a stale route? What does the consumer actually need?
6. **Price it.** If the target cannot be derived, what is the exact missing
   input?

End the step with a short numbered list of conclusions (C1, C2, ...). Each
conclusion names the inventory items it rests on. A conclusion that rests on
a BELIEF is a belief. Later steps cite these numbers.

## Step 4: The assumptions table

List every assumption you can find, in these six groups. Take them from the
wall's statement, the governing notes' premise lists and the runners, not
from memory. Then add the hidden ones: finiteness, locality, smoothness,
symmetry, perturbative level, choice of state, boundary conditions, readings
of the axioms, and "obvious" steps. Where the lane already has an
assumptions and imports ledger with a counterfactual pass
(`../physics-loop/references/assumption-import-audit.md`), start from its
rows and do not write them again.

- **(a) Target.** What is wanted: which theorem, which limit, which
  observables, which domain, which strength, and who consumes it.
- **(b) Formulation.** What the problem is built on: axioms and approved
  primitives (marked as such), definitions, the model, conventions, boundary
  conditions, choices of representation.
- **(c) Reduction.** Every step from the target to the wall: the route
  chosen, the intermediate statement, "one tool proves all of it", "one
  parameter value at a time", runner and numerical choices.
- **(d) Discard tests.** Every rule the lane uses to set an idea aside: "it
  also holds for model X", "it needs a small number", "its constant depends
  on the answer", "it bounds the wrong quantity", "it was tried".
- **(e) Beliefs.** What physics, numerics or reputation say, and what the
  plan depends on.
- **(f) Working rules.** Owner rules, the limits of the target's contract,
  method defaults.

```text
ID | Assumption, in plain words | Where it is used (path:line) |
Needed or habit (needed by the target / needed by the method / habit) |
If it is wrong or dropped: what follows | Does a change make the problem easier? |
Check (already run: path and result / cheapest check / none known)
```

Rules:

- Every row gets a real "if wrong". If no consequence is visible, say what
  would have to be inspected to know.
- "Needed by the method" is not "needed by the target". Say which.
- Group (f) is questioned on paper only. The run obeys every owner rule and
  every limit of the contract. You may write what a different rule would
  give, marked "not used". Name an axiom change only as a price.
- Framework lanes, group (b): the scale-reference primitive grants the
  Planck scale reference as units conversion only: it does not make
  downstream rows bounded and grants no dimensionless content. The
  kinetic-isotropy primitive grants only structural OS0 kinetic-form isotropy
  `c_t = c_s`, with no dynamics, Lorentz-closure theorem, absolute scale,
  spacing-ratio theorem, selector or empirical content. The realized-state
  primitive grants only pointwise evaluation at a supplied law-admissible
  realized state; it supplies no state, state-selection rule, measure,
  typicality or genericity assumption, weighting, probability rule, or any
  state-contingent value (quantities that vary across the law-admissible
  family remain registered data).

**Ranking.** Rank the assumptions by how much the problem changes if the
assumption is dropped. For the first five, write one line: what the lane
would do differently. Mark the rows whose drop would change an owner
decision.

## Step 5: Compare with the earlier work

Now open the "closed" list of step 0 and read it. For every conclusion of
step 3 and every assumption ranked in step 4:

```text
Item | Already in the earlier work? (yes / partly / new) | Where (path:line) |
Search scope for a "new" mark
```

Rules:

- Before you write "new", search the whole record of the lane for the
  statement itself: every file of the target folder, its indexes and
  registries, its queue rows, and the open PR branches. Search by the
  objects of the statement and by at least two wordings. Write the scope
  next to the mark. A search of named sections only gives "not found in
  <those sections>", never "new".
- Where the earlier work is right and the inventory is wrong, correct the
  inventory in place and say so at the item.
- Where the earlier work has a stronger form, say so and use it.
- Credit the earlier row, note or author for every item marked "yes" or
  "partly".
- End with two short lists: what the fresh pass added, and what it only
  found again.

## Step 6: The blockage: discard tests and set-aside methods

This step applies steps 2 to 4 to the lane's filters.

**6a. List every method that was set aside.** One row per method, from the
lane's files and digests. Do not sample.

```text
# | Method (with its authors) | Reason given | Where (path:line; read
first-hand, or taken from a digest) | Kind of reason (fails a test / circular /
needs a small number / wrong quantity / other setting / unverified / open premise)
```

**6b. First principles on the blockage.** From the definitions: what exactly
must a tool do here? Which kinds of statement can do it at all? Which
property of the model is the least that a tool must use? Write the blockage
in one sentence.

**6c. Audit every discard test in its logical form.** Definitions:

- A **tool** is a hypothesis H together with a written proof of "H(M)
  implies T(M)" for every model M of a class K that contains ours. T is the
  statement the lane needs, with its constants and quantifiers. A method
  with no written proof of this implication is a candidate, not a tool.
- A **test** is a comparison model M'.

The valid form has two parts.

- **Refutation.** A method is refuted as a tool on K only by a model M' in K
  where H(M') is true and T(M') is false, for the same T. Then "H implies T"
  is false on K.
- **Constraint.** For a tool with a written proof, T(M') false gives H(M')
  false. So a proof of H for our model must use a property that M' does not
  have. The test says what the proof of H must use. It does not refute the
  tool.

The test does not refute the tool when:

- the proof also runs for M', and T(M') is true there;
- M' is outside K;
- T(M') fails for another constant, quantifier or range than the tool's T;
- H(M') is not known.

The range form: let H be blind to the difference of M and M' at a parameter
value (H(M) implies H(M') there). Then the hypothesis of a sound tool fails
for M at every value where T(M') fails, and the tool proves nothing for M
there. So a test has a range. Write from which value it binds.

For each test, fill one row:

```text
Test (model M') | In which class K | The exact T that fails in M' |
How the failure is known (THM with standing and reading state / BELIEF) |
What a tool must use to pass | From which parameter value the test binds
```

Rules:

- A test that rests on a BELIEF is a belief. Say so, and look for a test of
  the same kind that rests on a theorem.
- A pass is no support. A hypothesis that implies T on K is false in every
  model of K where T fails, so it passes every valid test. A pass says only
  which property a proof of H must use.
- Ask whether the tests are enough. Step 2 lists the nearest models where
  the target is false; each one is a test.
- The other kinds of reason have a valid form too. "Circular": not circular
  when the constant depends on a smaller case (an induction), or in a proof
  by contradiction at a first bad point. "Needs a small number": valid as a
  range only; write the proved range. "Wrong quantity": name the quantity
  the target needs and the gap between the two. "Other setting": name the
  hypothesis of the tool that fails in ours. "Was tried": a failed search
  rules out nothing; name what was tried.

**6d. Re-judge every verdict.** One row per row of 6a:

```text
# | The verdict assumes (how the tool is used, in which range, for which
form of the target) | Valid in the corrected form? (valid / valid only in
range R / too strong / wrong / moot) | If not valid: what comes back, and where
```

Rules:

- A verdict that you did not re-derive is "valid as reported; not
  re-derived". Do not upgrade it.
- A verdict shown wrong or too strong is a result. Prove it or mark it.
- A tool that comes back goes to step 8.
- State where the corrected verdicts matter: on the path of the target, or
  off it.

## Step 7: Routes: generate, try to kill, rank

**Sources of routes.** The first-ranked assumptions of step 4, dropped or
changed; the tools that came back in step 6; a new form of the target from
step 3; the "least a tool must use" of 6b.

**Independent routes.** With `--subagents N`, fan out to `N` agents; with
`0`, use context-isolated passes. Give each a neutral, route-local brief
built from step 1's precise version and step 4's table. Do not give any
agent the favoured approach or another agent's conclusions. Choose the
briefs so that the approach families are materially different. Always
include one lens from outside the lane's own vocabulary, and one pass whose
brief is to argue that the wall is misframed and to name the question that
replaces it. Each pass returns one to three routes under the
concrete-return contract: a lemma with its proof skeleton, a construction,
an equation or invariant, a falsifier, or an exact missing obligation.
Reject vague returns ("topology might help").

```text
Route | Family (object, mechanism, terminal obligation) | Assumption it drops or changes |
What you would have to believe for it to work | First artifact | Cost |
What it would change if it worked
```

**Outside view.** Reuse the literature record of step 0 and update it only
for new route questions. Literature always runs
(`docs/ai_methodology/RULES.md` section 2, rule 7). `--no-web` skips live
search: the agent may still cite sources it knows, marked `recalled`. Prefer
primary sources. Look first for known no-go theorems and known escapes for
this kind of wall, then for proof templates.

```text
Source | What it shows | Premises | Maps to the repo? | What does not map |
Translation or runner | Import risk | Citation | Read in full / in part / recalled
```

**Mathematical lenses.** Choose them from the wall's structure; do not run a
fixed checklist. For each lens used, give the object that changes, the
invariant or theorem type, a minimal toy example, what would falsify it and
the first artifact. Before choosing, glance down this list so the search is
not too narrow: finite groups and representations; operator algebras and
noncommutative geometry; categories and universal properties; algebraic
topology, cohomology, K-theory and index theory; spectral graph theory and
combinatorics; convexity, optimization and variational methods; probability,
information theory and large deviations; dynamical systems, ergodic theory
and stability; PDE and functional analysis; number theory and lattices; logic
and independence. Lenses considered and found empty get one line each.

**Reframes.** Try moving the boundaries that repo walls usually hide behind:
pre-record vs recorded; object vs readout; selector vs admissible dial;
dynamics vs kinematics; finite carrier vs limiting family; exact theorem vs
bounded theorem vs no-go; value derivation vs value availability; central
sector vs within-sector data; representation choice vs physical observable;
supplied model vs axiom content; local pattern vs global or collective
structure; obstruction vs missing input. A reframe is useful only if it is
stated in framework objects, not lane fixtures.

**Try to kill every route.** Before ranking, give each route to a different
agent or pass whose brief is to break it. It checks:

- whether the route quietly assumes the target;
- whether it contradicts a checked or landed result;
- whether it was already tried (step 5);
- whether it fails a test of step 6 in the valid form;
- whether it breaks an owner rule or needs a new axiom, primitive or import;
- whether its terminal obligation is target-equivalent. If it is, the route
  is `blocked-equivalent` under the proof-search governance and is not near
  closure.

Record a verdict for every route: survives, wounded (with the named gap) or
dead (with the reason; a test kills a route only in the valid form of
step 6).

**Rank.**

```text
Rank | Route | Family | Assumption challenged | What you would have to believe |
Terminal obligation | Strength vs target | Kill verdict | Cost | First artifact |
What it changes | Stop/reopen condition
```

Rank by what the route would change if it worked, divided by what it costs
to find out. A cheap test that would move an owner decision outranks an
elegant reduction that ends at a target-equivalent lemma.

## Step 8: Real attempts

Within the budget, take the best two or three routes and go as far as you
can on each: prove the first lemma, find a counterexample, or reduce the
route to one exact statement.

- Before each attempt, search the lane's open registry and queue for the
  statement. If another row holds it, stop, name the match, and take the
  next route.
- A reduction counts only if the equivalence is proved, or the remaining
  statement is named exactly with its quantifiers and constants.
- A dropped assumption that gives a different target counts only if the new
  target is proved to give the old one, or the missing step is named.
- Say for each result whether it is on the path of the target or off it.

For each run (script, numerical test, search):

- pre-register the pass and fail reading before running, and never change
  it after the result is seen. If the result shows the reading was badly
  chosen, add a new, dated follow-up test with its own reading;
- state exactly which class a search covered. A search that finds no pass
  in a finite class is a bounded result ("no pass in the searched class"),
  not a no-go, and a run that fails to refute a lemma does not prove it;
- do not let a verdict rest on extrapolating a fit over many orders of
  magnitude. When it would, compute the decisive quantity directly;
- keep the script, the output and the result, and hold the numeric lock
  where the repo requires one;
- report and preserve the actual result immediately, including failures.
  Before interpreting a failure as a scientific negative conclusion or no-go,
  obtain a fresh adversarial check under the allowed review configuration.
  Prefer another vendor's model where configured; label a same-family check
  honestly and do not call it an independent referee. If the user prohibits
  subagents, use a separate primary-session pass and state that it is not
  independent. Record the interpretation, corrections and review limitation
  without changing the original result or pre-registered reading;
- say plainly whether it moved the wall, and in which direction.

If no route can be attempted inside the budget, say why, and give the
smallest test that would decide the top route and what it needs. A deferred
test must name who or what it is waiting on: the owner, a probe queue, or a
missing input.

Results of the exercise are exercise evidence, not repo claims. A result
worth keeping goes through the normal note, check and review path.

## Step 9: Report

The report leads with plain language. Write it for the owner, who will act
on it. Every claim in it carries one mark of the Output rules.

1. **The wall, in plain words:** step 1's plain version, corrected by the
   exercise.
2. **What the exercise found:** three to six plain sentences. Include what
   changed since the exercise started, and the attempts with their results.
3. **Filters corrected:** each discard test or verdict that changed, in its
   valid form, with the range and what comes back. "None" is an answer.
4. **Routes worth doing:** at most three. For each, say what you would have
   to believe, what it costs, the first test, and what it would change.
5. **What not to do next,** with the reason.
6. **The exact price,** if the exercise found one: the premise, decision or
   open statement the wall is equivalent to.
7. **Work items:** each a complete brief that a fresh session can run with
   no other context: the statement, the files and lines to read, the points
   to test first, the stop rule, the output file. The first item is the
   check request for the statements of this run, by a model that did not
   write them. Add a list "not proposed", with reasons.
8. **Appendix:** the tables of steps 2 to 8, the approach registry, and
   short lists of the assumptions most likely to be wrong, the assumptions
   most expensive to be wrong, and literature proofs worth translating.

End the file with one line that starts `RESULT:` and states what was proved
(with marks), what was corrected, and what stays open.

Before you finish, read the report's strong words ("new", "every", "no
candidate", "exact", "proves", "theorem", "sound") against what the run
actually did, and correct each one that says more.

The report must not claim the wall is solved without a proof, a decisive
runner or a decisive no-go artifact.

## Non-Negotiables

- Plain language first. The report's first three sections contain no
  undefined jargon and no lane fixture presented as framework content.
- Fresh first, compare later. Steps 2 to 4 are written with the attack
  files closed, and step 5 opens all of them. Nothing is "new" without the
  search of step 5.
- Every inventory item and every statement carries a mark, and a mark is
  never stronger than its weakest input.
- A discard test refutes a tool only in the valid form of step 6. Every
  set-aside method is re-judged; none is skipped.
- Do not over-rely on existing framework content. It is evidence, and the
  exercise may find it wrong, overbroad or misframed.
- Do not miss approved primitives or overstate what they grant (step 4).
- Owner rules and the limits of the target's contract are not broken in the
  exercise. They are listed in group (f) and questioned on paper only.
- Do not apply audit verdicts, promote claims, add axioms, primitives or
  imports, or declare the wall solved without an actual proof, runner or
  decisive no-go artifact.
- Name an axiom change only as a price. Draft candidate wording only when the
  owner asks for it. It must start from a layman-simple sentence, say why the
  existing axioms cannot supply it, and be marked as not adopted.
- Do not import literature as proof. Translate it into repo-native theory,
  check it, and cite the source. Credit by name every author whose work is
  used.
- A run may refute or guide. It never discharges a statement by itself.
- Write the file as you go. Say who wrote it and who checked what.
- Report honestly when the exercise produced only a map.
- Before quoting a subagent's result, check its strong words ("every",
  "no candidate", "exact", "proves") against what it actually computed.
