# Koide r Is the Weighting-Principle Dial; Record Dynamics Is Weighting-Blind

**Date:** 2026-06-15
**Type:** bounded theorem
**Claim type:** bounded_theorem
**Status:** source note awaiting independent audit handling.
**Primary runner:** [`scripts/frontier_r_weighting_principle_dial_2026_06_15.py`](../scripts/frontier_r_weighting_principle_dial_2026_06_15.py)
**Cached output:** [`logs/runner-cache/frontier_r_weighting_principle_dial_2026_06_15.txt`](../logs/runner-cache/frontier_r_weighting_principle_dial_2026_06_15.txt)

## Claim

`r` is the weighting-principle dial. On the two-sector record, with singlet sector weight
`w_singlet` and doublet sector weight `w_doublet`, the registered Koide-block parameter is

`r = w_doublet/(2 w_singlet)`.

Dimension weighting gives sector weights `(1/3, 2/3)`, hence `r=1` and `Q=1`. Equal-sector
weighting gives sector weights `(1/2, 1/2)`, hence `r=1/2` and `Q=2/3`. Therefore
r=1/2 is the equal-sector charged-lepton setting.

Accordingly, the record-preserving dynamics is weighting-blind inside this
supplied two-sector context: it conserves the singlet and doublet block weights,
so it does not select the prior weighting. Hence `r` is the registered weighting
choice, the dial, while the equal-sector charged-lepton value is one setting.

## Derivation

The finite-dimensional check builds the cyclic record operator `C` on the generation
three-space and forms `S = C + C^2`. The projection `(S+I)/3` is the +2 singlet
projector, and its complement is the -1 doublet projector. These projectors define the
two record sectors with ranks 1 and 2.

The runner computes `r` from the weighting ratio, then computes `Q = 1/3 + 2r/3`. For
dimension weighting it obtains `r=1`, `Q=1`; for equal-sector weighting it obtains
`r=1/2`, `Q=2/3`. The two computed values differ, so the dial is genuine.

The same weightings are realized as density states by spreading each sector weight
uniformly inside its block. The runner verifies that tracing those states against the
singlet and doublet projectors recovers the declared block weights.

Weighting-blindness is checked by the record map
`D_S(rho) = P_singlet rho P_singlet + P_doublet rho P_doublet`. On random density states,
the runner verifies that this map preserves both block weights. As a discriminating
control, it conjugates a singlet state by a non-block-diagonal unitary and verifies that
the singlet block weight changes. The conservation is therefore special to the
record-preserving map, not a tautology.

## Significance

This identifies what `r` records in this two-sector map: the chosen weighting
principle on the record sectors. The record dynamics conserves the registered
sector weights, so the weighting choice is carried forward by the record rather
than selected by it. This sharpens the r-dial: dimension weighting and
equal-sector weighting are distinct settings of the same map.

## Boundary (honest)

This does NOT force r=1/2. The value `r=1/2` is one setting of the dial, while `r=1`
is another. This note does not derive which weighting a sector carries; that remains
registered or initial-condition data. It also does not address delta.

## Dependencies

- [RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15](RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md) for Stage 2 conservation.
- [FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md) for the pointer and two-sector record.
- `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11`.

## Forbidden-imports check

No new axiom is imported here. The runner computes `r` from the weighting ratio and
does not hardcode or force the answer. The relation `Q = 1/3 + 2r/3` is the standard
Koide-block relation used for the two computed settings.
