# Generation Dial Local Stability Grammar

**Date:** 2026-06-05
**Claim type:** positive_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note does not set, predict, or propose an
audit outcome.
**Primary runner:** [`scripts/generation_dial_local_stability_grammar_2026_06_05.py`](../scripts/generation_dial_local_stability_grammar_2026_06_05.py)
(sympy; **SCORECARD 13 PASS / 0 FAIL**).
**Cached log:** [`logs/runner-cache/generation_dial_local_stability_grammar_2026_06_05.txt`](../logs/runner-cache/generation_dial_local_stability_grammar_2026_06_05.txt).

## Scope and honesty

This note isolates the one-dimensional stability grammar used by
`GENERATION_DIAL_DYNAMICS_STABILITY_CLASSIFIER_2026-06-05` (the **consumer this
grammar serves** — rendered as a plain reference, not a load-bearing markdown
dependency, since this reparametrization lemma `r(s) = 2^(s-1)` is self-contained
and consumes none of that note; the genuine direction is classifier → this
grammar, so the plain reference breaks the spurious audit-graph 2-cycle).

It proves that the positive ratio coordinate `r` and the dial coordinate `s`
are smooth monotone reparametrizations:

```text
r(s) = 2^(s-1),        s(r) = log2(2r) = 1 + log(r)/log(2).
```

Therefore local stability can be computed in the `s` coordinate without
changing the map multiplier or the flow linearization at a fixed point.

This is only a grammar. It does not identify which map, flow, partition, or
fixed point is physically selected.

## Theorem

For positive `r`, define

```text
h(s) = r(s) = 2^(s-1),
L(r) = s(r) = 1 + log(r)/log(2).
```

Then:

```text
L(h(s)) = s,
h(L(r)) = r,
dh/ds = (log 2) h(s) > 0.
```

So `r` and `s` are locally equivalent stability coordinates on the positive
ratio line.

## Map stability is preserved

Let a map `G` on the positive `r` coordinate fix `r*`, and suppose locally

```text
G(r) = r* + alpha (r-r*) + higher order terms.
```

The conjugated map in the `s` coordinate is

```text
F(s) = L(G(h(s))).
```

At the corresponding fixed point `s*=L(r*)`, the local multiplier is the same:

```text
F'(s*) = alpha = G'(r*).
```

Therefore the standard one-dimensional map classifier applies:

```text
|F'(s*)| < 1  -> stable
|F'(s*)| = 1  -> neutral / higher-order analysis needed
|F'(s*)| > 1  -> repelling
```

## Flow stability is preserved

Let a flow on the positive `r` coordinate have a fixed point `r*` and local
linearization

```text
dr/dtau = beta (r-r*) + higher order terms.
```

The induced `s` flow is

```text
ds/dtau = (1/(r log 2)) dr/dtau.
```

At `s*=L(r*)`, the local linearization is again `beta`. Therefore:

```text
beta < 0  -> stable
beta = 0  -> neutral / higher-order analysis needed
beta > 0  -> repelling
```

## Named generation maps

The two maps already used in the charged-lepton/generation lane become
especially clean in the `s` coordinate:

```text
r' = 2r^2          -> s' = 2s
r' = sqrt(r/2)    -> s' = s/2
```

Thus:

- Lueders/record sharpening fixes `s=0` but repels it;
- the reverse/thermalizing branch fixes `s=0` and stabilizes it.

This is a coordinate-clean statement. It does not say the reverse branch is the
physical charged-lepton arrow.

## What this unlocks

This gives the repo a reusable local-stability theorem for record-function
dials:

1. Convert positive sector ratios to a log dial coordinate.
2. Classify local maps by `|F'(s*)|`.
3. Classify local flows by the sign of `f'(s*)`.
4. Keep value selection separate from stability classification.

That is the right abstraction for the dynamics push. It lets downstream notes
say "this setting is stable under this supplied dynamics class" without
claiming "this setting is forced by the minimal axioms."

## Runner coverage

The runner verifies:

- `r(s)` and `s(r)` are inverse coordinates;
- `r(s)` has positive derivative;
- local map multipliers are preserved by the `r <-> s` coordinate change;
- local flow linearizations are preserved by the coordinate change;
- `r->2r^2` gives `s'=2s`;
- `r->sqrt(r/2)` gives `s'=s/2`;
- the finite map and flow classifiers return stable, neutral, or repelling
  according to the standard criteria.

## Net

The `s` coordinate is not just convenient notation. It is the correct local
stability coordinate for the positive generation ratio, and it makes the
dynamics proposal auditable: stability is a property of a named map or flow,
not a hidden value-selection principle.
