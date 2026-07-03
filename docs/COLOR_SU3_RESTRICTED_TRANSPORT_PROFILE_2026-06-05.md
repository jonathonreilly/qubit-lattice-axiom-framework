# Color SU(3)-Restricted Transport Profile

**Date:** 2026-06-05
**Type:** bounded_theorem
**Claim type:** bounded_theorem — exact finite-algebra support under an
admitted transport rule.
**Status authority:** independent audit lane only. This source note does not
apply audit verdicts, edit audit data, or assert package promotion.
**Primary runner:**
[`scripts/frontier_color_su3_restricted_transport_profile_2026_06_05.py`](../scripts/frontier_color_su3_restricted_transport_profile_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_color_su3_restricted_transport_profile_2026_06_05.txt`](../logs/runner-cache/frontier_color_su3_restricted_transport_profile_2026_06_05.txt).

**Local support inputs:**

- [`COLOR_LINK_SYM2_ENDPOINT_PROJECTION_2026-06-05.md`](COLOR_LINK_SYM2_ENDPOINT_PROJECTION_2026-06-05.md)
- [`COLOR_LINK_INDEX_ROUTING_CARRIER_BUDGET_2026-06-05.md`](COLOR_LINK_INDEX_ROUTING_CARRIER_BUDGET_2026-06-05.md)
- [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- [`RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md`](RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md)

## Purpose

The projection block supplies an exact rank-3 symmetric endpoint once a
two-qubit link endpoint is admitted. This note asks the next narrow question:

```text
Given admitted Sym^2 endpoints and the standard SU(3) endpoint transport law,
does endpoint dressing make the color line invariant in the expected 0 -> 1
-> 2 profile?
```

Yes. Under the admitted transformation rule, the finite algebra is exact:
bare link transport is endpoint-variant, a half-dressed line is invariant at
one endpoint, and a fully dressed meson/Wilson-type line is invariant at both
endpoints.

## Setup

Work on the rank-3 symmetric endpoint carrier supplied by the projection
block. Let `T^a = lambda^a/2` be the Gell-Mann generators on that carrier.
For endpoint transformations `g_A, g_B in SU(3)`, admit the standard link rule:

```text
q_A     -> g_A q_A
q_B     -> g_B q_B
U_AB    -> g_A U_AB g_B^{-1}
q_A^*   -> q_A^* g_A^{-1}
```

This rule is a bounded input here. The note verifies what follows from it; it
does not derive the rule from the three framework axioms.

## Result

| object | endpoint profile | reason |
|---|---:|---|
| bare link `U_AB` | `0` | transforms at both endpoints |
| half-dressed line `q_A^* U_AB` | `1` | left endpoint cancels, right endpoint remains |
| fully dressed line `q_A^* U_AB q_B` | `2` | both endpoint transformations cancel |
| closed trace `Tr(U_loop)` | closed-loop invariant | infinitesimal trace of a commutator vanishes |

So, once the two-qubit Sym2 endpoint and SU(3)-restricted transport rule are
admitted, the color transport profile matches the finite two-endpoint
Gauss-law pattern.

## What this supplies and what it does not supply

This block supplies only the finite algebra after the transport rule is supplied:

```text
admitted Sym2 endpoint
  + admitted SU(3) transport transformation law
  -> endpoint-invariant color-singlet line algebra.
```

It does not close:

- derivation of the two-qubit endpoint;
- derivation of the SU(3) transport law;
- dynamic preservation of the symmetric endpoint sector;
- gauge action, coupling, beta function, rates, time, or continuum limit;
- confinement or QCD dynamics;
- identification of the invariant line as the physical record algebra;
- production of realized record atoms.

The exact post-record layer can record realized invariant atoms after a
formation/readout bridge supplies them. It does not supply the bridge.

## Boundaries

- Does not derive physical color.
- Does not establish a repo-wide quantum-link ontology.
- Does not derive the two-qubit endpoint or the SU(3) transport law.
- Does not derive Gauss generators from the axioms; it checks the admitted
  infinitesimal endpoint action.
- Does not derive an action, coupling, beta function, rate, time, confinement,
  or continuum QCD.
- Does not identify color-singlet records as the physical record algebra.
- Does not select a Koide/generation dial location.
- Does not apply audit verdicts.

## Runner summary

The runner verifies:

- Gell-Mann `T^a` generators are traceless Hermitian and satisfy sample
  `su(3)` commutators;
- the bare link is endpoint-variant;
- the half-dressed line cancels the left endpoint variation but not the right;
- the fully dressed line cancels both endpoint variations;
- closed trace variation is the trace of a commutator and vanishes;
- the result keeps endpoint ontology, transport-law derivation, action,
  couplings, record readout, and dial selection out of scope.

Expected result:

```text
SCORECARD PASS=74 FAIL=0
```
