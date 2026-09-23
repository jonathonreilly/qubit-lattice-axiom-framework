# Proof Search Governance

Use this protocol when a physics-loop target is a theorem, a multi-step
mathematical bridge, or a hard reduction whose completion depends on proving
nontrivial intermediate obligations. It governs the search process; it does
not supply physics premises or weaken the repo's claim-status gates.

## Contents

- Exact Target Contract
- Approach-Family Registry
- Independent Search Rounds
- Concrete-Return Contract
- Theorem-Strength Gap Test
- Candidate-Proof Audit
- Round Synthesis And Handoff

## Exact Target Contract

Before route generation, record:

```text
Target statement | Quantifiers/domain | Allowed premises |
Forbidden weakenings | Required edge/degenerate cases |
Completion witness | Outcomes that do not count as closure
```

Keep the target neutral. Do not assume an affirmative proof exists or instruct
workers to suppress a counterexample, a scoped no-go, or an exact remaining
gap. A runtime budget is work capacity, not evidence that the target is true.

## Approach-Family Registry

Classify a family by the tuple:

```text
(primary mathematical object/formulation,
 load-bearing mechanism or invariant,
 terminal proof obligation)
```

Do not classify families by agent name, wording, note type, or whether the
deliverable is a runner, literature bridge, or theorem note. Those are artifact
types, not mathematical approaches.

Maintain `APPROACH_REGISTRY.md` with:

```text
Family | Object/formulation | Mechanism/invariant | Terminal obligation |
Strength vs target | Status | Concrete evidence | Reopen condition
```

Use `weaker`, `unknown/comparable`, `target-equivalent`, or `stronger` for the
strength relation. Use `unexplored`, `active`, `provisional`,
`blocked-local`, `blocked-equivalent`, `retired`, or `candidate-complete` for
status.

## Independent Search Rounds

- Start with materially incompatible families, not several phrasings of the
  favored route.
- Give early workers neutral, route-local briefs. Do not disclose the favored
  approach or other workers' conclusions unless their task is explicitly
  synthesis or adversarial review.
- Redirect new work toward underexplored families when one family becomes
  saturated.
- Cross-pollinate only after independent routes have produced a concrete
  mathematical core and exposed their real gaps.
- When parallel agents are unavailable, emulate independence with separate
  context-isolated passes before synthesis.

## Concrete-Return Contract

Every route pass must return at least one of:

- a formal lemma with a proof or proof skeleton whose open steps are named;
- an explicit construction with admissibility checks;
- equations, an invariant, or a dependency reduction;
- a counterexample, falsifier, or exhaustive finite certificate;
- an exact missing lemma with its dependency graph and the step that failed.

Reject status-only reports, vague optimism, repeated background summaries, and
claims that a global compatibility step is "routine."

## Theorem-Strength Gap Test

For every unresolved terminal lemma `L` and target `T`:

1. state `L` formally under the same premises as the route;
2. test whether `L => T`;
3. test whether `T => L`, possibly after a routine translation;
4. classify the strength relation in the registry.

If `L` is target-equivalent or stronger, the route is not near closure merely
because it reached `L`. Mark it `blocked-equivalent` unless the route supplies
a genuinely new mechanism that advances the proof of `L`.

Reopen a blocked family only when a new invariant, construction, premise,
decomposition, or proof mechanism changes the obligation map. Record that
mechanism as the reopen condition; a new worker or new wording is not enough.

## Candidate-Proof Audit

Before marking `candidate-complete`, independently check:

- the conclusion matches the exact target contract, including quantifiers;
- the proof-obligation graph is acyclic and every leaf is discharged;
- every reduction preserves hypotheses, domains, and admissibility;
- every constructed object satisfies the definition actually required;
- boundary, degenerate, disconnected, singular, normalization, and convention
  cases relevant to the target are covered;
- no target-equivalent theorem is imported, renamed, or used circularly;
- computational evidence is used as proof only when exhaustive or supported by
  a theorem that makes it decisive.

## Round Synthesis And Handoff

After each round, report family coverage, concrete gains, exact gaps, saturation,
redirects, and blocked-family reopen conditions. Preserve several incompatible
routes while budget remains; an elegant reduction does not earn dominance if
its terminal obligation is target-equivalent.

At handoff, state the strongest rigorously proved result, the exact remaining
obligation, its strength relation to the target, and the best new mechanisms
that could reopen blocked families. Never hide the remaining gap behind
"routine," "standard," or "compatibility."
