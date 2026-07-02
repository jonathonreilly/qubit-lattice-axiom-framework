# Outcome Factorization Is Not Forced By One-Copy Born Marginals

**Date:** 2026-06-18
**Claim type:** no_go
**Status:** source-side bounded no-go; independent audit required.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces.
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

## No-Go Discipline Gate

**Status: PASS.** The claim is narrow: one-copy Born/Gleason marginals plus
finite scalar additivity do not force quotient-level two-registration
factorization.

**N1 alternative routes.**

| route | attempt | disposition |
| --- | --- | --- |
| finite table algebra | Derive `m(j,k)=p_j p_k` from normalization, marginals, and additivity. | ATTEMPTED: the current theorem leaves the free parameter `a=m(s,s)` in the positivity interval. |
| one-copy Gleason/Busch | Treat retained one-copy Born authority as selecting the two-registration joint law. | ATTEMPTED: `GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` and `BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md` fix the marginals only, not the coupling. |
| exchange symmetry | Add symmetry under swapping the two registrations. | ATTEMPTED: the current correlated witness is symmetric and still nonfactorized. |
| two-copy Born realization | Require a density-matrix witness on `C^2 tensor C^2`. | ATTEMPTED: the current product and correlated diagonal states realize the same marginals. |
| downstream product weakening | Use the retained product-to-outcome weakening theorem as a source theorem. | RULED OUT BY PRIOR: `PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md` shows the downstream flow consumes outcome factorization once supplied; it does not supply the law. |

**N2 wall independence.** The collapsed wall set has one wall: quotient-level
two-registration factorization is not forced by the tested one-copy surface.
No inflated independent wall count is asserted.

**N3 hidden-wall scan.** "Supplied" names the quotient under test, not a proof
input that supplies factorization. "Registered" and "two-registration" name
the target law's domain. "Framework-native" marks future positive-repair
directions only. No hidden admission is used to prove the negative boundary.

**N4 residual matching.** The context citations are not prior no-go witnesses.
Their residual use matches the boundary: Gleason/Busch supply one-copy
marginals; the product-to-outcome weakening consumes outcome factorization but
does not derive it.

**N5 rhetoric audit.** The note avoids global impossibility language. The
tested resolution is only the supplied two-outcome, two-registration quotient
law.

**N6 partial-closure path scan.** The note does not say a new axiom or
primitive is required. Valid future closures include a record-stack
independence theorem, stationarity/reset theorem, or an explicit supplied
import later retired by audit. Approved primitives are not treated as bounded
walls here.

**N7 steelman.** A future theorem could use durable records, stationarity, and
reset/preparation structure to derive iid record stacks, which would supply the
product law needed by the statistics atom. That would not contradict this
no-go, because it would add a source beyond one-copy Born marginals plus finite
additivity.

**N8 cross-cycle echo.** Prior product-structure boundaries in this repo were
kept valid only after narrowing them to "not forced by these tested inputs."
This note follows that shape: it prunes a false shortcut and leaves the
positive repair route open.

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
TOTAL: PASS=56 FAIL=0
VERDICT: bounded no-go passes; outcome factorization is not forced by retained one-copy Born marginals plus finite additivity.
```
