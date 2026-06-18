# Outcome Factorization Is Not Forced By One-Copy Born Marginals

**Date:** 2026-06-18
**Claim type:** no_go
**Status:** source-side bounded no-go; independent audit required.
**Primary runner:** `scripts/frontier_statistics_outcome_factorization_not_forced_2026_06_18.py`
**Runner cache:** `logs/runner-cache/frontier_statistics_outcome_factorization_not_forced_2026_06_18.txt`

## Boundary

This note proves a narrow negative boundary for the W8a statistics atom:
retained one-copy Born weights plus finite scalar additivity on a two-outcome
quotient do not force the two-registration outcome-factorization law

```text
m(j,k) = p_j p_k,   j,k in {s,d}.
```

Therefore the missing premise in
`STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_BOUNDED_NOTE_2026-06-12.md`
cannot be discharged by merely citing one-copy Gleason/Busch Born authority or
finite additivity. A separate record-stack independence, stationarity, or
preparation theorem is still required.

This is not a global no-go against future outcome independence. It only prunes
the route "derive factorization from retained one-copy Born marginals alone."

## Retained Inputs Used As Context

- `GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`
  supplies the retained one-copy Born form on finite qubit-lattice projection
  lattices.
- `BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
  supplies the retained one-qubit effect-valued Born form.
- `PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`
  shows that the downstream agreement-conditioning flow consumes only
  outcome-level factorization, not a full product state.

These inputs define the surface whose insufficiency is tested. This note does
not consume any unaudited unraveling measurement as proof input.

## Theorem

Let `{s,d}` be a supplied two-outcome quotient with one-copy weights

```text
p_s = p,          p_d = 1-p,          0 <= p <= 1.
```

A two-registration finite-additive joint law with these marginals is determined
by one parameter

```text
a = m(s,s),
m(s,d) = p - a,
m(d,s) = p - a,
m(d,d) = 1 - 2p + a,
```

with positivity interval

```text
max(0, 2p - 1) <= a <= p.
```

The product-factorized law is the single point `a = p^2`. Except at the
endpoints `p in {0,1}`, the interval contains other admissible points, so the
marginals and finite additivity do not force factorization.

For the concrete interior point `p = 1/2`, two admissible joint laws are:

```text
product:     (m_ss,m_sd,m_ds,m_dd) = (1/4, 1/4, 1/4, 1/4),
correlated:  (m_ss,m_sd,m_ds,m_dd) = (1/2, 0,   0,   1/2).
```

Both have one-copy marginals `(1/2,1/2)` and both are finite-additive
probability assignments. Only the first one satisfies
`m(j,k)=p_j p_k`.

## Born-Realizable Witness

The counterexample is not merely abstract probability bookkeeping. On
`C^2 tensor C^2`, with `P_s = |0><0|` and `P_d = |1><1|`, the diagonal density
matrices

```text
rho_product    = diag(p^2, p(1-p), (1-p)p, (1-p)^2),
rho_correlated = diag(p,   0,      0,      1-p)
```

are positive, trace-one, and have the same one-copy marginals
`diag(p,1-p)`. Their Born joint weights on
`P_j tensor P_k` are respectively product-factorized and perfectly
correlated. Thus even adding a two-copy Born-realizable witness does not make
one-copy marginals select the product law.

## Consequence For The Statistics Atom

The W8a statistics reduction remains valid under the supplied
outcome-factorization premise. This no-go shows why that premise is real:
the retained one-copy Born/Gleason surface and finite additivity alone leave a
family of admissible joint laws. A future positive repair must add or derive a
record-stack independence theorem, a preparation/reset theorem, or another
approved source of quotient-level product weights.

## Non-Claims

This note does not:

- derive or refute physical repeated-registration independence;
- claim that actual record dynamics is correlated;
- decide R-D, occupancy cells, the wave-9 tri-guise dictionary, or any value of
  `r`;
- update audit ledgers, queues, publication matrices, active review state, or
  lane registries;
- add a probability axiom or a new Record axiom.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_statistics_outcome_factorization_not_forced_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=40 FAIL=0
VERDICT: bounded no-go passes; outcome factorization is not forced by retained one-copy Born marginals plus finite additivity.
```
