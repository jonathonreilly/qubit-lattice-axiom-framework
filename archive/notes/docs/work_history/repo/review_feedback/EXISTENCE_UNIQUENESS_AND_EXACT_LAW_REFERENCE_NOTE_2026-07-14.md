# Existence, Functional Uniqueness, And Exact-Law Reference

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a finite model-theoretic and language-placement
probe. It does not identify a physical law, amend an axiom, register a premise,
select a boundary, or set an audit verdict.

**Runner:**
[`scripts/existence_uniqueness_exact_law_reference_probe_2026_07_14.py`](../../../../scripts/existence_uniqueness_exact_law_reference_probe_2026_07_14.py)

## Question

The current Admissibility axiom says there is one fixed nearest-neighbor rule,
and the Qualification says a law gives exactly one answer on every state in
its supplied domain. Why is any further exact reference needed?

## Result

Three statements that sound similar in ordinary English are logically
different:

1. **existence in reality:** one particular rule governs the actual world;
2. **functional uniqueness:** once a rule and input are supplied, it gives one
   answer—possibly a complete set or probability distribution; and
3. **exact identification:** the theory tells us which rule or which exact
   observable-equivalence class is meant.

The current text supplies the first as ontology and requires the second of any
object called a law. It does not supply the third. A theory can have many
models, each containing one fixed rule, while those rules give different
record predictions. Reality may use only one model; the theory still cannot
derive which prediction to make.

In plain language, “the chef used one recipe” does not tell us which recipe.
It rules out mixing recipes during the bake. It does not predict the cake.

## 1. Exact Two-Model Separation

For neighbor counts `(n_0,n_1)`, let one model interpret the fixed rule as

```text
q_1(0|n_0,n_1) = 1/2,
```

and a second interpret it as

```text
q_2(0|n_0,n_1)
  = 2^n_0 / (2^n_0 + 2^n_1).
```

Each model has exactly one fixed rule. Each rule gives exactly one positive,
normalized, label-covariant distribution for every input profile. At
`(n_0,n_1)=(2,1)`, the models predict `1/2` and `2/3`.

Therefore neither “there is one fixed rule” nor “a law gives exactly one
answer” proves the value. The ambiguity is across models, not inside either
law.

This is why changing `rule` to `law`, or adding `determines physical
continuation`, does not by itself close the TOE. Both exact laws already
determine a continuation distribution and still disagree.

## 2. What An Exact Physical-Equivalence Class Would Need

The constitution need not privilege one microscopic presentation when several
presentations have exactly the same physical predictions. It may identify an
exact physical-equivalence class instead.

But that class is defined only after the complete physical test repertoire is
known. The runner constructs two raw deterministic laws with the same visible
record and different hidden-token evolution. Every read-only future protocol
gives the same transcript, so the raw laws are equivalent in that restricted
operational theory. Adding one admitted hidden-token probe separates them.

Thus “equivalent” cannot be a generic escape word. A valid referent must state:

```text
which contexts and adaptive protocols are physical;
which boundaries/preparations are compared;
which finite record transcripts count as observables; and
that every representative gives the same law for all of them.
```

That theorem may produce a smaller canonical equivalence class than a single
microscopic table. It is still exact predictive specification.

## 3. Determinism Does Not Change The Identification Need

Two deterministic append laws can each have one successor from every state,
while one writes `0` and the other writes `1`. Determinism removes a separate
sample coordinate. It does not identify the successor function.

This cleanly separates two constitutional questions:

- Does the exact law need one-history sampling semantics? Only if it branches
  and the existing ontology does not otherwise link the measure to one actual
  history.
- Does the constitution need to identify the exact law? Yes, unless a theorem
  uniquely derives it or proves exact physical equivalence.

The second survives both stochastic and deterministic architectures.

## 4. Minimum Placement Consequence

There are only three honest outcomes.

### Unique derivation

If the present four axioms prove one exact law, no axiom update is needed. The
proof makes the existing existential rule definite.

### Exact adopted referent

If one law is fundamental input, Admissibility must identify it by a stable
exact reference. The short axiom need not contain its equations. The referenced
source must fill the complete law contract and thereby become part of the
foundation.

### Exact equivalence-class theorem

If several raw laws differ only in unphysical presentation, Admissibility may
reference the exact class or its defining theorem. The theorem must cover every
admitted context and claimed observable, not only one low-energy or restricted
test set.

A placeholder such as `[CANONICAL-LAW]`, `QCA`, `multiway`, `causal`,
`reversible`, or `the simplest rule` does not close any outcome. It names a
future job, not the physical object.

## 5. Language Guard For The Final Iteration

The final public sentence should not imply that the rule's exact value follows
from the words `fixed`, `one`, or `determines`. Those words state constancy,
cardinality within the actual model, and functionality. The stable reference
does the identificatory work.

The shortest logical skeleton after an adopted referent exists is:

```text
The fixed nearest-neighbor law is the exact law specified by <reference>.
```

Covariance can remain in the same existing sentence. Whether `record-valued
realization` is additionally needed depends on the referenced law type:

- a sampled law can include one-history semantics in its exact definition;
- a deterministic uniquely extendible law derives one successor; and
- a measure-only branching object still needs a physical link to the one
  realized record history.

No Record sentence follows merely from this semantic repair. Preservation,
record identity, and formation should first be theorem-tested against the
exact referent.

## 6. No-Go Discipline Gate

**Gate result:** `PASS` for the narrow claim that one fixed law per model and
one answer per law input do not identify one value across the two displayed
models. No claim is made that exact identification cannot be derived.

### N1 — alternative routes

The live routes are exact derivation, adopted exact reference, exact
physical-equivalence class, deterministic unique continuation, sampled law,
and boundary-conditioned global uniqueness.

### N2 — wall-independence audit

The paired stochastic laws separate structural existence from value. The
paired deterministic laws independently separate functional uniqueness from
function identity. The hidden-token pair tests equivalence relative to
contexts rather than repeating the value separation.

### N3 — hidden-wall scan

`One`, `fixed`, `answer`, `model`, `law`, `physical`, `equivalent`, `context`,
and `observable` are all typed. The stable reference cannot point to a family
with an unresolved coefficient.

### N4 — residual matching

The `1/2` versus `2/3` transcript tests exact-law value. The hidden probe tests
operational quotient. Neither tests record permanence, gravity, or continuum
dynamics.

### N5 — rhetoric audit

The result says the current theory is underdetermined for the displayed test,
not that Nature has several simultaneous laws or that no unique law exists.

### N6 — partial-closure paths

Every structural sentence remains useful. Covariance, locality, causal
consistency, generated composition, and record preservation can narrow or
validate the exact referent even though they do not name it alone.

### N7 — steelman

The strongest counterposition is that “one fixed rule” abbreviates an exact
canonical object already defined elsewhere. If such a stable object exists and
is foundation-authorized, the semantic gap is already closed. Repository and
Bridger searches have found candidates and contracts but no selected complete
referent. This probe would immediately accept one once present.

### N8 — cross-cycle echo

The result formalizes the repeated correction from the availability census,
complete sampled-law pair, reversible family, and QCA classification audit:
classification and existential commitment are not physical selection.

## Verification

```bash
python3 scripts/existence_uniqueness_exact_law_reference_probe_2026_07_14.py
python3 -m py_compile scripts/existence_uniqueness_exact_law_reference_probe_2026_07_14.py
python3 scripts/vocab_lint.py docs/work_history/repo/review_feedback/EXISTENCE_UNIQUENESS_AND_EXACT_LAW_REFERENCE_NOTE_2026-07-14.md
git diff --check
```
