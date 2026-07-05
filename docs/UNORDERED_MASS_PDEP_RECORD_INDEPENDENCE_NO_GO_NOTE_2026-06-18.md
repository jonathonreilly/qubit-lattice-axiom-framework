# Unordered-Mass P-dep Record-Independence No-Go

**Date:** 2026-06-18
**Claim type:** no_go
**Actual current-surface status:** source-side no-go support; independent audit
owns any verdict or effective-status propagation.
**Target row:**
`unordered_mass_multiset_registrability_bridge_narrow_theorem_note_2026-06-11`
**Primary runner:**
`scripts/unordered_mass_pdep_record_independence_no_go_2026_06_18.py`

## Result

Record alone cannot derive P-dep.

More precisely, the Record axiom clauses from
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) used by the
unordered-mass bridge are:

- finite scalar additivity over pairwise-disjoint record collections, with
  `I(empty)=0`;
- `K`/CPT orbit constancy for the realized central sector;
- the boundary that Record supplies no readout context, decomposition,
  weighting, normalization, probability, within-sector data, or occupancy rule.

Those clauses do not force a registrable scalar's per-record contribution to be
a function only of the registered datum `([k], lambda_k)`. There are
Record-compatible supplied contexts with the same `([k], lambda_k)` data and
different unregistered `K`-even context scales `q`, and the family

```text
I_q(S, delta) = q * sum_{k in S} lambda_k(delta)
```

is finitely additive, has `I_q(empty)=0`, and is constant on the `K`/CPT orbit
for each fixed `q`. Yet two contexts with the same registered sector datum and
different `q` give different per-record scalar values. Therefore P-dep is an
extra extensionality/readout-identification premise, not a consequence of
Record additivity plus orbit constancy.

## Countermodel

Use the same supplied `C3` circulant eigenvalue surface as the conditional
unordered-mass note:

```text
lambda_k(delta) = a + 2 B cos(delta + 2 pi k / 3),
sigma(k) = -k mod 3.
```

Then

```text
lambda_{sigma(k)}(-delta) = lambda_k(delta).
```

For every fixed unregistered scale `q`, `I_q` satisfies Record's two operative
constraints:

1. finite additivity:
   `I_q(A union B, delta) = I_q(A, delta) + I_q(B, delta)` for disjoint finite
   sector sets `A` and `B`;
2. orbit constancy:
   `I_q({sigma(k)}, -delta) = I_q({k}, delta)`.

Now compare two supplied contexts that are identical in the registered data
`([k], lambda_k)` but differ in the unregistered scale, for example `q=1` and
`q=2`. At a generic nonzero `lambda_k`, the same registered datum receives two
different values:

```text
I_1({k}, delta) != I_2({k}, delta).
```

That violates P-dep, while preserving every Record clause used above. Hence no
proof of P-dep can be obtained from Record alone.

## No-Go Discipline Gate

The full N1-N8 checklist for this negative claim is recorded in
`.claude/science/physics-loops/unordered-mass-pdep-record-independence-20260618/NO_GO_DISCIPLINE_CHECKLIST.md`.
Its disposition is `PASS` for this narrow route-local no-go only: Record
finite additivity plus `K`/CPT orbit constancy do not derive P-dep. The
checklist does not close a future physical-readout/extensionality theorem,
convention ratification, or owner-approved premise route.

## Implication For The Conditional Row

This no-go does not make the unordered-mass bridge positive retained. It narrows
the source-side repair target:

- a future positive repair must provide a separate physical-readout or
  extensionality theorem that excludes unregistered `K`-even context data like
  `q`;
- or the row must stay explicitly conditional on P-dep;
- or the repo must approve P-dep as a premise through the governance/audit
  process, which this note does not request or enact.

## Boundaries

This note introduces no new axiom, primitive, admission, normalization,
probability rule, fitted value, or observed comparator. It does not edit audit
results. It does not edit ledgers, queues, publication matrices, Tier-A
registries, lane registries, active review queues, or repo-wide status boards.

It also does not dispute the existing conditional theorem. Inside a supplied
context where P-dep is assumed, the unordered-mass multiset algebra remains the
same. The no-go is only against deriving P-dep from Record alone.

## Verification

Run:

```bash
python3 scripts/unordered_mass_pdep_record_independence_no_go_2026_06_18.py
```

Expected result:

```text
SUMMARY: UNORDERED MASS P-DEP RECORD-INDEPENDENCE NO-GO PASS=18 FAIL=0
```
