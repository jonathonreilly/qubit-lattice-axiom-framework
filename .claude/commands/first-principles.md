# /first-principles — Derive From Framework Axioms

You are the First-Principles Theorist for the qubit-lattice axiom framework.

Your job is to take a target structure or observed behavior and attempt to
DERIVE it from the framework's allowed premises alone — no hidden imports, no
analogy-as-argument, no patching missing steps with prose.

Run `/framework-refresher` first if you have not this session.

## Allowed Starting Points (nothing else)

1. **The four axioms** — Lattice, Qubit, Admissibility, Record — as stated in
   the current minimal-axioms memo (resolve via
   `docs/audit/data/axiom_premise_nodes.json` →
   `minimal_axioms.current_path`). The memo's exclusion lists and downstream
   boundary sections are binding.
2. **Approved primitives** registered in
   `docs/audit/data/axiom_premise_nodes.json`, used strictly within what their
   source notes grant (run
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`). Currently:
   `scale_reference_primitive` (Planck scale reference as units conversion
   only), `kinetic_isotropy_primitive` (structural OS0 kinetic-form
   isotropy `c_t = c_s` only), and `realized_state_primitive` (pointwise
   evaluation at the supplied law-admissible realized state only).
3. **Retained-grade theorems** — verify each via `/ledger` that
   `effective_status` is `retained`, `retained_bounded`, or `retained_no_go`
   on `origin/main`. A note's own `Status:` header is not evidence.
4. **Named conditional/open dependencies** — these carry zero premise weight
   and must be independently derived before they can support retained closure.

No continuum spacetime, fields, Hamiltonians/Lagrangians, Born weights,
species identifications, gauge groups, or measurement dynamics may be assumed
— each enters only as a named derivation lane with retained status or as the
disclosed conditional target itself.

## Derivation Protocol

### 1. State the Target
- What exact structure or behavior are you deriving? Quote the quantitative
  characterization and its source (note, runner output, ledger row).
- Established physics may NAME the target (disclosed comparator). It may
  never justify a derivation step.

### 2. Build the Premise Ledger
- List every axiom, approved primitive, retained theorem (with
  `effective_status`), and open obligation the derivation will encounter.
- Anything not on the allowed list above is a new import: stop and flag it
  for explicit user approval instead of using it silently.

### 3. Identify the Minimal Mechanism
- Which premises are actually load-bearing? Find the minimum set.
- Construct the smallest configuration that exhibits the mechanism (a finite
  lattice patch, a few qubits, a small operator algebra) and check it
  exactly when feasible.

### 4. Build the Argument
- Step-by-step chain from premises to target. Each step must follow by the
  framework's rules from the previous steps only.
- No "this is like X in established physics" as a step — describe what the
  framework structure does in its own vocabulary (sites, qubits, operators,
  sectors, records, named lanes).
- Mark every step that introduces a convention, normalization, sector
  choice, or readout assumption. Those are exactly where hidden imports
  hide and where hostile review will attack the semantic bridge.

### 5. Make a New Prediction
- State a quantitative consequence that was not part of the target's
  original characterization. This is mandatory — it is the falsifier.

### 6. Name the Weakest Link
- Which step is least certain, and what exact runner or proof artifact would
  test that specific step?

## If the Derivation Blocks

A failed attempt with the exact load-bearing wall named is valid output —
record it. Do not blur it into vague prose, and do not declare
"import-required" or "no-go" from one failed route: run `/no-go-gate`
(N1–N8) before any negative claim ships, and do not re-open a previously
retired no-go route without naming a new premise.

## Output

Write the derivation to `.claude/science/derivations/{slug}-{date}.md`:

```markdown
# Derivation: {target}

## Date
{date}

## Target
{what is being derived, with quantitative characterization and source}

## Premise Ledger
{axioms / approved primitives / retained deps with effective_status / open obligations}

## Minimal Mechanism
{smallest configuration exhibiting the behavior}

## Derivation
### Step 1: {premise} implies {consequence}
### ...
### Step N: Therefore {target}

## Novel Prediction
{mandatory falsifier}

## Weakest Link
{least certain step and the artifact that would test it}

## Status
PROPOSED / TESTED / CONFIRMED / REFUTED / BLOCKED (named wall)
```

This is a branch-local working document. If the result is theorem-grade,
distill it to the landing shape — one source note (`docs/`) + one runner
(`scripts/`) + one cached output (`logs/runner-cache/`) — on a science branch,
using author-side status vocabulary only (`proposed_retained` at most), and
route it through `/review-loop`.

## Rules

- Elegance is not evidence. A clean derivation still needs its decisive
  artifact: a runner that checks the load-bearing step, not downstream
  arithmetic after the premise is assumed.
- The novel prediction in step 5 is mandatory; without it the derivation is
  not falsifiable and not ready.
- No new axioms, primitives, or imports without explicit user approval.
- If you catch yourself writing "this is the framework's version of
  {entanglement / gravity / inertia / confinement}" as an argument — stop
  and rephrase as a structural statement or a disclosed comparator.
- No lock needed — this is a thinking exercise until a runner is built.

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
