# Color Link Sym2 Endpoint Projection

**Date:** 2026-06-05
**Type:** bounded_theorem
**Claim type:** bounded_theorem — exact finite-algebra support under an
admitted two-qubit endpoint.
**Status authority:** independent audit lane only. This source note does not
apply audit verdicts, edit audit data, or assert package promotion.
**Primary runner:**
[`scripts/frontier_color_link_sym2_endpoint_projection_2026_06_05.py`](../scripts/frontier_color_link_sym2_endpoint_projection_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_color_link_sym2_endpoint_projection_2026_06_05.txt`](../logs/runner-cache/frontier_color_link_sym2_endpoint_projection_2026_06_05.txt).

**Local support inputs:**

- [`COLOR_LINK_INDEX_ROUTING_CARRIER_BUDGET_2026-06-05.md`](COLOR_LINK_INDEX_ROUTING_CARRIER_BUDGET_2026-06-05.md)
- [`CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md)
- [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)

## Purpose

The carrier-budget block showed that a color link endpoint cannot be one
primitive qubit, while a two-qubit endpoint has enough room to host
`Sym^2(C^2)`. This note asks the next narrow question:

```text
If a two-qubit link endpoint is admitted, is the Sym^2 projection itself
canonical and exact?
```

Yes. Given a two-qubit endpoint `C^2_a x C^2_b`, the swap operator
`S_ab` canonically gives

```text
P_sym  = (I + S_ab) / 2
P_anti = (I - S_ab) / 2
```

with ranks `3` and `1`. The symmetric block carries the standard Gell-Mann
`su(3)` action; the antisymmetric block is inert. This supplies the projection
algebra needed by the carrier budget.

## Result

On an admitted two-qubit endpoint:

| object | exact fact |
|---|---|
| swap `S_ab` | involution, `S_ab^2 = I` |
| `P_sym` | orthogonal projector, rank `3` |
| `P_anti` | orthogonal projector, rank `1` |
| decomposition | `C^2 x C^2 = Sym^2(C^2) + Anti^2(C^2)` |
| embedded color algebra | Gell-Mann `su(3)` acts on `Sym^2(C^2)` and kills `Anti^2(C^2)` |

So the projection/constraint subpiece of the color link carrier budget has an
exact algebraic target:

```text
admitted two-qubit endpoint
  -> canonical swap projector
  -> rank-3 symmetric endpoint
  -> possible SU(3)-restricted transport carrier.
```

## What remains open

This theorem does not supply the endpoint. It says what to do if the endpoint
is supplied.

Remaining gates:

- derive or admit a two-qubit link-end carrier;
- identify which two qubits form each link endpoint;
- make the symmetric sector dynamically preserved;
- construct the link variable as `SU(3)` transport on the symmetric block;
- define endpoint Gauss generators and Wilson observables;
- supply action, couplings, rates, and time;
- identify color-singlet records as the physical record algebra.

## Why this moves link routing

Before this block, "two-qubit symmetric endpoint" was a carrier budget. After
this block, its projection algebra is exact and checkable. The remaining
problem is no longer "find a rank-3 projector"; it is "justify the two-qubit
endpoint and its SU(3)-restricted transport as framework dynamics."

That makes later attempts sharper: a positive link-route branch must now target
endpoint ontology, block preservation, and transport law, not the elementary
projection algebra.

## Boundaries

- Does not derive physical color.
- Does not establish a repo-wide quantum-link ontology.
- Does not derive the two-qubit link endpoint from the one-qubit site axiom.
- Does not select which endpoint qubits belong to a physical link.
- Does not derive an `SU(3)` link variable, Gauss generator, Wilson observable,
  action, coupling, rate, time, confinement, or continuum QCD.
- Does not identify color-singlet records as the physical record algebra.
- Does not select a Koide/generation dial location.
- Does not apply audit verdicts.

## Runner summary

The runner verifies:

- the two-qubit swap is an involution;
- `P_sym` and `P_anti` are orthogonal projectors with ranks `3` and `1`;
- the Gell-Mann generators embedded through the symmetric basis are Hermitian,
  traceless on the symmetric block, close under sample `su(3)` commutators,
  commute with `P_sym`, and annihilate `P_anti`;
- a generic one-qubit operation does not preserve the symmetric projection;
- the artifact keeps endpoint ontology, transport law, Gauss/Wilson
  observables, action/couplings, record-readout, and dial selection out of
  scope.

Expected result:

```text
SCORECARD PASS=66 FAIL=0
```
