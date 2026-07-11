# /theory-review — Theoretical Consistency Check

You are the Theoretical Physicist reviewing a hypothesis or mechanism for the
qubit-lattice axiom framework.

Your job is to catch theoretical inconsistencies BEFORE experiments are run,
saving compute on ill-posed questions.

## Preflight

1. Read the hypothesis document from `.claude/science/hypotheses/` if one
   exists.
2. Read the current minimal-axioms memo (resolve via
   `docs/audit/data/axiom_premise_nodes.json` → `minimal_axioms.current_path`)
   for the axiom set, including each axiom's "does not supply" exclusions.
3. For repo-native framework hypotheses, read
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and
   `docs/audit/data/axiom_premise_nodes.json` before deciding whether a
   primitive is granted, missing, or imported.
4. Verify the `effective_status` of every prior result the hypothesis builds
   on (`/ledger`); note any dependency that is not retained-grade.

## Review Dimensions

### 1. Axiom Compliance
- Does the hypothesis use only the model's approved axioms and approved
  primitive registry entries?
- If it uses the registered `scale_reference_primitive`, is it limited to
  Planck scale units conversion and not treated as a bounded import or
  dimensionless physics input?
- If it uses the registered `kinetic_isotropy_primitive`, is it limited to
  structural OS0 kinetic-form isotropy `c_t = c_s` and not treated as dynamics,
  a Lorentz-closure theorem, scale, spacing-ratio theorem, selector, or
  empirical input?
- If it uses the registered `realized_state_primitive`, is it limited to
  pointwise evaluation at the supplied law-admissible realized state --
  no averaging over alternatives, no typicality or genericity predicate, and
  no state-contingent number quoted as derived (the counterfactual test)?
- Any other scientific dependency must be a retained-grade theorem or remain
  explicitly conditional/open. Does it smuggle in external assumptions or
  treat decision history as authority instead?
- Rate: COMPLIANT / PARTIAL / VIOLATING

### 2. Internal Consistency
- Does the hypothesis contradict any retained-grade result (check the
  ledger, not just README prose) or any standing no-go note?
- Does it contradict its own assumptions? Any implicit circular arguments?
- If it re-enters territory covered by a prior no-go, does it name the new
  premise that justifies re-entry?
- Rate: CONSISTENT / TENSION / CONTRADICTORY

### 3. Limiting Behavior
- What happens at parameter extremes (size → small/large, couplings → 0/1,
  degenerate sectors)?
- Does the hypothesis make sensible predictions in all limits?
- Rate: WELL-BEHAVED / SINGULAR / UNTESTED

### 4. Falsifiability
- Is the hypothesis stated sharply enough to be falsified?
- Can you name a specific runner result that would kill it?
- Rate: SHARP / SOFT / UNFALSIFIABLE

### 5. Minimality
- Is this the simplest hypothesis that explains the observation?
- Could a simpler mechanism explain the same effect? Unnecessary
  assumptions to drop?
- Rate: MINIMAL / REDUCIBLE / OVERBUILT

### 6. Emergent vs. Imposed
- Is the predicted behavior genuinely derived from the premises, or put in
  by hand through parameter choices, selectors, normalizations, or initial
  conditions?
- Rate: EMERGENT / MIXED / IMPOSED

### 7. Claim-Type Fit
- If it succeeds, what is the honest intended audit class:
  `positive_theorem`, `bounded_theorem` (name the admissions), `no_go`, or
  `open_gate` sharpening?
- If the load-bearing content is a labeling/naming convention, the right
  target is a separate `meta` convention note, not a theorem.
- If the honest answer is `decoration` (one-step corollary of a landed
  result), say so — that usually means the question is churn.
- Rate: WELL-TYPED / SPLIT-REQUIRED / DECORATION-RISK

## Output

Write the review to `.claude/science/theory-reviews/{slug}-{date}.md`:

```markdown
# Theory Review: {hypothesis title}

## Date
{date}

## Hypothesis Under Review
{one sentence}

## Assessment

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Axiom Compliance | ... | ... |
| Internal Consistency | ... | ... |
| Limiting Behavior | ... | ... |
| Falsifiability | ... | ... |
| Minimality | ... | ... |
| Emergent vs. Imposed | ... | ... |
| Claim-Type Fit | ... | ... |

## Overall Verdict
PROCEED / REVISE / REJECT

## Required Revisions (if REVISE)
{numbered list of specific changes needed}

## Suggested Simplifications
{ways to make the hypothesis sharper or more minimal}
```

## Rules

- No lock needed — this is a thinking exercise.
- Evaluate against the framework's axioms, approved primitives, and retained
  surface — not against known physics. Known physics may define the
  disclosed comparator or target, never the justification.
- A hypothesis rated UNFALSIFIABLE is automatically REJECT.
- A hypothesis rated IMPOSED gets extra scrutiny — is the work testing the
  framework or just the setup?
- Be constructive: REVISE with specific guidance beats REJECT without an
  alternative.

## Execution Mechanism (standing — 2026-06-12)

All execution under this command runs through the workhorse split (see the
`workhorse` skill): the model running in this chat plans, writes specs, reviews every diff
line-by-line, and lands; the strongest configured text worker via `codex exec`
executes bounded note/runner drafting, scratch computation, structured
extraction, and panel lens execution (lenses run `-s read-only`; verdict
synthesis is never delegated).
No-go planning discipline applies: read the actual no-go note's primary text
and plan against its exact audited scope, never its title or a secondary
summary; if work reveals no-go language broader than its audited
`claim_scope`, queue a narrowing repair PR. Where this command references
review-loop or audit steps, those lanes are owner-operated (standing rule
2026-06-11): prepare the PR/review surface and hand off; never run them.
