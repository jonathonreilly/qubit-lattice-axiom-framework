# Color Link-Index Routing Carrier Budget

**Date:** 2026-06-05
**Claim type:** meta support map and exact finite-dimensional route pruning.
**Trace class:** negative route-pruning support map.
**Status authority:** independent audit lane only. This source note does not
apply audit verdicts, edit audit data, or assert package promotion.
**Primary runner:**
[`scripts/frontier_color_link_index_routing_carrier_budget_2026_06_05.py`](../scripts/frontier_color_link_index_routing_carrier_budget_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_color_link_index_routing_carrier_budget_2026_06_05.txt`](../logs/runner-cache/frontier_color_link_index_routing_carrier_budget_2026_06_05.txt).

**Local support inputs:**

- [`COLOR_MR_CARRIER_ROUTING_SPLIT_2026-06-05.md`](COLOR_MR_CARRIER_ROUTING_SPLIT_2026-06-05.md)
- [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
- [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- [`CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md)
- [`RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md`](RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md)

## Purpose

The previous split isolated link-index routing as the sharp remaining
construction needed after carrier block content is available. This note asks:

```text
What is the smallest qubit-built link-end carrier that could even host the
base-SU(3) color index?
```

The answer is exact and finite-dimensional:

- one primitive qubit endpoint cannot host the color fundamental or a faithful
  native `su(3)` connection algebra;
- two qubits can host a 3D symmetric subspace `Sym^2(C^2)` plus a 1D
  complement, so they are the minimal qubit-built carrier budget for a color
  endpoint;
- that two-qubit budget is only a carrier budget. It still needs a symmetric
  projection/constraint, a link-end pairing convention, an `SU(3)`-restricted
  connection on the symmetric block, endpoint Gauss generators, observables,
  and dynamics/action.

## Result

| carrier candidate | Hilbert dimension | color `3` possible? | status |
|---|---:|---|---|
| one primitive qubit `C^2` | 2 | no | exact obstruction |
| two qubits `C^2 ⊗ C^2` without a constraint | 4 | not as a pure endpoint | needs block preservation |
| two-qubit symmetric subspace `Sym^2(C^2)` | 3 | yes as a carrier | minimal qubit-built host |

This is not a derivation of link routing. It is a budget:

```text
base-SU(3) link-index routing needs at least
  two qubits per color endpoint
  + symmetric-subspace projection/constraint
  + SU(3)-restricted transport on that 3D block.
```

The one-qubit route is closed. The two-qubit symmetric route remains open but
now has a precise carrier target.

## Exact finite-dimensional facts

1. A single qubit has Hilbert dimension `2`, matrix algebra dimension `4`, and
   traceless Hermitian local Lie dimension `3`. The color fundamental needs
   Hilbert dimension `3`, and `su(3)` has Lie dimension `8`.
2. Non-trivial irreducible `su(3)` representations have minimum dimension `3`;
   there is no non-trivial `2`-dimensional `su(3)` representation.
3. Two qubits have Hilbert dimension `4`, and the swap decomposition is
   `C^2 ⊗ C^2 = Sym^2(C^2) ⊕ Anti^2(C^2)` with dimensions `3 + 1`.
4. The Gell-Mann `su(3)` action can act on the symmetric `3` and leave the
   antisymmetric complement inert. That is a reducible `3 ⊕ 1` carrier, not a
   generic `U(4)` link.

## Routing ledger

| required structure | supplied by carrier budget? | comment |
|---|---|---|
| endpoint can host a color `3` | yes, with two qubits and a symmetric constraint | exact finite-dimensional support |
| one-qubit endpoint color route | no | exact obstruction |
| symmetric-subspace projection/constraint | no | must be supplied as link ontology or dynamics |
| canonical choice of which two qubits form the endpoint | no | must be supplied by a graph/link construction |
| `SU(3)`-restricted link transport | no | generic `U(4)` is too large |
| endpoint Gauss generators and Wilson observables | no | separate gauge-bridge construction |
| action/couplings/rates/time | no | dynamics residual |
| post-record histories/counts | downstream only | available after realized atoms exist |

## What this unlocks

The next positive link route is now concrete:

```text
construct a two-qubit link endpoint,
project or constrain it to Sym^2(C^2),
place SU(3) transport on that block,
and show endpoint Gauss/Wilson observables preserve the record algebra.
```

Without those steps, any color lane using a one-qubit link endpoint should be
read as `SU(2)+U(1)` support or as an open color-routing import, not as color
link routing.

## Boundaries

- Does not derive physical color.
- Does not establish a repo-wide quantum-link ontology.
- Does not build the two-qubit endpoint projection dynamically.
- Does not derive `SU(3)` link variables, Gauss generators, Wilson
  observables, action, couplings, rates, time, confinement, or continuum QCD.
- Does not identify color-singlet records as the physical record algebra.
- Does not select a Koide/generation dial location.
- Does not apply audit verdicts.

## Runner summary

The runner verifies:

- one-qubit carrier dimension and algebra dimensions;
- non-trivial `su(3)` irreps have no 2D representation in the checked
  Cartan-Weyl dimension formula range;
- two qubits are the minimal qubit count with Hilbert dimension at least `3`;
- the two-qubit swap decomposition gives `3 + 1`;
- a block-preserving `su(3) ⊕ 0` action is possible on `Sym^2 ⊕ Anti^2`, but
  generic `U(4)` transport is not the same object;
- the carrier budget does not supply projection, link routing, Gauss/Wilson
  observables, action/couplings, or record-readout antecedents.

Expected result:

```text
SCORECARD PASS=51 FAIL=0
```

## No-Go Discipline Gate (N1-N8)

**Status:** PASS for the scoped route-pruning claim only. This note prunes a
one-primitive-qubit color-endpoint route and names the two-qubit symmetric route
as an open carrier target; it does not claim physical color is impossible.

| Gate | Result |
|---|---|
| N1 alternative routes | Checked one-qubit endpoint, generic two-qubit endpoint, symmetric two-qubit endpoint, generic `U(4)` transport, and record-readout routes. Only the one-qubit endpoint is pruned; the others remain explicit residuals. |
| N2 wall independence | Endpoint carrier, symmetric projection, transport law, Gauss/Wilson observables, dynamics/action, and record identification are independent residuals; none is collapsed into another here. |
| N3 hidden-wall scan | "Canonical", "standard", and "carrier" language is limited to finite-dimensional algebra or listed as a residual. No hidden dynamics, action, or readout rule is imported. |
| N4 residual matching | The pruned residual is exactly "one primitive qubit cannot host a color fundamental/native `su(3)` endpoint"; it is not reused as evidence against two-qubit or higher routes. |
| N5 rhetoric audit | Negative language is at the endpoint Hilbert-dimension/Lie-algebra level only, not at the full lattice, gauge-dynamics, or physical-color level. |
| N6 partial-closure scan | The legitimate partial-closure path is the admitted two-qubit `Sym^2(C^2)` endpoint route, which this note keeps open. No new axiom or primitive is claimed. |
| N7 steelman | A reviewer can still build color by supplying a two-qubit endpoint plus a preserved symmetric sector and restricted `SU(3)` transport; this note is compatible with that route. |
| N8 cross-cycle echo | Prior record/color bridge notes reduced color to named residuals rather than proving impossibility; this note follows that pattern and only narrows the carrier-budget residual. |
