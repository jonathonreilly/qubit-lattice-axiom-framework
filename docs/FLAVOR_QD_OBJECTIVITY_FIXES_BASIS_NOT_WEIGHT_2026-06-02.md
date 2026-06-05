# Flavor QD Objectivity Fixes Basis Not Weight

**Date:** 2026-06-02
**Claim type:** no_go.
**Runner:** `scripts/flavor_qd_objectivity_fixes_basis_not_weight_2026_06_02.py`.

This source note records a narrow route closure. It sets no grade, changes no
existing row, and does not treat any axiom or primitive as a source of bounded
status for consumers.

## Question

Does Quantum-Darwinism objectivity, understood as redundant broadcast of
distinguishable pointer information, force the uniform count over the two
K-real sectors `(1:1 -> r=1/2)` rather than the dimensional/Born weighting
`(1:2 -> r=1)`?

## Result

No. Objectivity fixes the pointer basis, not the sector weight.

- The two K-real sectors form the objective alphabet: a rank-1 singlet and a
  rank-2 doublet.
- A spectrum-broadcast branching state has full redundant objectivity for any
  probability weights on that two-symbol alphabet. The observer plateau is
  `H(weights)`, a readout value, not a selector of those weights.
- The tracial reference `I/3` pushes through the two effects to `(1/3, 2/3)`,
  hence `r=1`. The uniform sector reference `(1/2, 1/2)` is a different
  reference-state choice.
- The runner verifies that `I/3` is invariant under sampled `U(3)` conjugations
  while the uniform-sector reference is not.
- Conjugation fixes both real effects and induces no rank-1/rank-2 swap, so the
  K-real/CPT route does not force a uniform sector count.

The remaining Koide measure question is therefore a reference-state or measure
choice, not an objectivity/basis consequence.

## No-Go Discipline Gate

This gate applies only to the narrow claim: QD objectivity does not force the
uniform sector weight.

### N1 - Alternative route enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Redundancy route | Use repeated environmental copies to select a weight. | Fails for this claim: redundancy exists for both tested weights. |
| Plateau route | Use the observer mutual-information plateau to select uniformity. | Fails for this claim: the plateau equals `H(weights)` and reports the supplied weights. |
| Tracial route | Use the canonical tracial state to force uniform sectors. | Fails for uniformity: `I/3` gives `(1/3, 2/3)`. |
| Invariance route | Use `U(3)` invariance to prefer the uniform sector state. | Fails for uniformity: the runner samples invariance of `I/3`, not the uniform-sector state. |
| K-real/CPT route | Use conjugation to swap the two sectors. | Fails for this claim: both effects are real and are fixed individually. |
| Maximum-information route | Add an indifference or maximum-entropy rule over objective labels. | Possible extra principle, but not QD objectivity itself. |

### N2 - Wall Independence

The collapsed residual is one measure/reference choice. Basis selection and
weight selection are separate; closing the basis route does not close the
weight route.

### N3 - Hidden-Wall Scan

"Objectivity" is used only in the broadcast/redundancy sense tested by the
runner. A maximum-entropy or indifference rule would be an additional premise
and is not silently included.

### N4 - Residual Matching

The runner checks the residual actually claimed: whether objectivity selects
the two-sector weights. It does not claim to settle all possible measure
principles, all reference-state principles, or a full Koide value derivation.

### N5 - Rhetoric Audit

The negative statement is restricted to the QD objectivity route. It is not a
claim that no future principle can select `(1/2, 1/2)`.

### N6 - Partial-Closure Path Scan

An owner-approved measure admission, a derived reference-state theorem, or a
new maximum-information principle could select the uniform weighting. That
would be an explicit admission or derivation target, not content imported from
the Lattice, Quantum, or Record axioms.

### N7 - Steelman

A hostile reviewer can argue that objective records should be counted by
labels rather than by Born weight, and that a maximum-objective-information
principle would then prefer `(1/2, 1/2)`. That is a coherent possible
additional principle; it is outside QD objectivity as tested here.

### N8 - Cross-Cycle Echo

Prior Koide-measure work repeatedly separates basis/alphabet facts from
measure/reference facts. This note preserves that separation: it closes one
objectivity route and leaves the measure residual explicit.

**Gate result:** pass for the narrow route closure only.
