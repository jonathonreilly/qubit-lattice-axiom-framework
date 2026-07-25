# Record derives the readout carrier, not the alphabet, and never the product — Cycle 693

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py`
(6 PASS / 0 FAIL, exit 0, exact rational arithmetic).

## The question

[Record classical semigroup boundary](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
is `audited_conditional`, criticality `critical`. Its load-bearing sentence:

> "Most importantly, the Record premise does not itself supply the finite
> alphabet or the complex function-algebra carrier, leaving the result
> conditional on those inputs."

Repair instruction:

> "missing_bridge_theorem: add a retained bridge deriving the supplied finite
> record alphabet and the standard unital complex-linear A=C^O representation
> from accepted framework content."

Two objects are named. This cycle finds three, with three different statuses.

## What the Record axiom actually says

From `MINIMAL_AXIOMS_2026-06-29`, verbatim and complete on this point:

```text
(D) A readout value is determined by record content alone.
(A) For any finite collection of pairwise-disjoint records, scalar readout I
    is additive,
(Z) with I(empty)=0.
```

## Result: a three-way split

**1. The complex-linear carrier is DERIVED.** `(D)+(A)+(Z)` force every readout
to be the sum over the collection of a single function of record content; that
function is recovered *uniquely* from singleton readouts; and the
correspondence `{readouts} ↔ {functions O → scalars}` is a linear bijection.
Verified exhaustively over the declared coefficient grid. **The `C^O` carrier is
axiom content, not a supplied input** — the obligation already has this one for
free.

**2. The finite alphabet is NOT ENTAILED.** An explicit countably-infinite
alphabet model satisfies determinacy, additivity over finite disjoint
collections, and `I(empty)=0` in full. The Qubit axiom states only "Each site
has a domain of local possibilities" — no cardinality bound appears anywhere in
the axiom text. Finiteness is a genuine supplied input, exactly as the auditor
said.

**3. The algebra product is NOT ENTAILED — and was never named.** Additivity
constrains the *additive* structure only. Two unital commutative products live
on the very same derived carrier:

| product on the derived carrier | unital | nonzero nilpotent `w`, `w³ = 0` |
|---|---|---|
| pointwise `C³` | yes | none |
| truncated polynomial `C[x]/(x³)` | yes | `(0, −2, −2)` |

They are **not isomorphic** — one has nilpotents, the other does not. So the
axiom does not pin the algebra *even up to isomorphism*.

## Consequence for the obligation

The repair instruction asks for two objects. One is already discharged by the
axiom; one is provably beyond it; and a third input sits between them, unnamed.
**Any future bridge that "derives `A = C^O` as an algebra" is smuggling in a
product.** The instruction cannot be satisfied honestly until the product is
added to its list of inputs.

This is a narrowing of a `critical` obstruction, not a closure of it. The
useful content is that the lane now knows which third of the problem it already
has, which third is unreachable from the axiom, and which third nobody had
written down.

## Firewalls

- No dynamics, probability, measurement rule, or physical carrier
  identification is derived or claimed.
- A vector-space carrier is **not** an observable algebra, and is not called
  one here.
- No axiom or primitive is proposed or adopted; the countermodels demonstrate
  what the axiom does *not* entail and propose nothing to add.

## Scope for independent review

The derivation is exhaustive over a declared finite coefficient grid on a
three-letter fixture alphabet, in exact rational arithmetic; the two
non-entailment results are explicit countermodels, which require only one
witness each and are given. Infinite-dimensional carriers, non-commutative
products, and any physical interpretation of the alphabet are outside scope and
untested. The N1–N8 verdict remains reviewer-owned; this note self-awards none.

## Dependency citations

The runner imports nothing from the repository. It cites
[Record classical semigroup boundary](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
for the obstruction text and
[Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) for the Record clauses quoted above.
