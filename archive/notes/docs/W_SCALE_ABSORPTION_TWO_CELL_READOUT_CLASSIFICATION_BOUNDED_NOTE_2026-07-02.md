---
claim_id: w_scale_absorption_two_cell_readout_classification_bounded_note_2026-07-02
claim_type: bounded_theorem
claim_scope: "Bounded support: for supplied two-cell readouts I=u*x_A+v*x_B, diagonal equal-content records carry w only through a common prefactor; ratios, normalized fractions, and degree-zero shape functionals are w-free on that diagonal; same-family calibration plus the scale-reference primitive absorbs the prefactor; w-sensitive content remains only in off-diagonal evaluation, cross-family comparison without common calibration, or unrouted absolute normalization. The listed current-source instances are classified only under their stated premises. No wall, CTX-match, w registry action, axiom, policy, audit verdict, or publication surface is changed."
upstream_dependencies:
  - c2_w_supplier_reading_fork_fixed_point_unidentifiability_bounded_note_2026-07-02
  - ew_kappa_weighting_not_axiom_derivable_no_go_note_2026-06-09
  - scale_reference_primitive
  - occupancy_atom_is_the_outcome_dictionary_flow_selects_equipartition_bounded_note_2026-06-12
runner: scripts/frontier_w_scale_absorption_two_cell_classification_2026_07_02.py
---

# w Scale-Absorption For Supplied Two-Cell Readouts (Bounded Note)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit boundary:** independent audit lane only. This note sets no audit
verdict, predicts no audit outcome, and edits no audit-lane-owned data.
**Primary runner:**
[`scripts/frontier_w_scale_absorption_two_cell_classification_2026_07_02.py`](../scripts/frontier_w_scale_absorption_two_cell_classification_2026_07_02.py)
**Cached runner output:**
[`logs/runner-cache/frontier_w_scale_absorption_two_cell_classification_2026_07_02.txt`](../logs/runner-cache/frontier_w_scale_absorption_two_cell_classification_2026_07_02.txt)

## Firewall

This is a bounded finite-algebra classification. It does not close any wall,
claim CTX-match, select `w`, reclassify a registry entry, adopt a readout
context, or change axiom, primitive, policy, audit, or publication surfaces.

The classification is limited to the supplied two-cell form
`I = u*x_A + v*x_B` and to the listed current-source instances under their
stated premises. It says nothing about future readouts or unlisted surfaces.

## Source Surface

The current source dependencies are:

- [`C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md`](C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md)
- [`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md)
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md)

Only the current source facts are used: the two-cell diagonal identity
`I(x,x) = (u+v) x`, the parent `Pi_phys = C + kappa_EW S` family and
common-factor cancellation, the scale primitive's units-conversion boundary,
and the flow-selected equal-content premise.

## Diagonal Common-Factor Classification

For diagonal equal-content records `(x_i,x_i)`, every readout in the supplied
family has the form:

```text
I_i = u*x_i + v*x_i = (u+v)*x_i.
```

Therefore, as long as denominators are nonzero:

- pairwise ratios satisfy `I_i/I_j = x_i/x_j`;
- normalized fractions satisfy `I_i/sum_j I_j = x_i/sum_j x_j`;
- any degree-zero homogeneous rational functional of the readout vector is
  unchanged by the common factor.

The diagonal premise is load-bearing. Off the diagonal, for example,
`I(1,0)/I(0,1)=u/v`, so `w=v/u` remains observable.

## Same-Family Calibration

Dimensionful diagonal readouts carry `w` through the common prefactor
`s=u+v`. If the calibration readout is from the same family, then
`I_i/I_cal = x_i/x_cal`, so the prefactor cancels.

If a physical unit is assigned through the approved
[`scale-reference primitive`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) against one
member of the same family, the same cancellation gives
`I_i*(M_ref/I_cal)=M_ref*x_i/x_cal`.

This is not a cross-family theorem. If the numerator and calibration come from
families with different prefactors, the ratio carries `s/s'`.

## Listed Current-Source Instances

Each row is classified only under its stated premise:

| Current-source instance | Premise | Classification |
|---|---|---|
| EW shape `g1^2/(g1^2+g2^2)` | CTX-match and a common same-family factor | `w`-free by common-factor cancellation |
| Koide-shape witness | flow-selected equal-content diagonal | `w`-free by degree-zero homogeneity |
| mass ratios | flow-selected equal-content diagonal | `w`-free by pairwise ratio cancellation |
| absolute mass scale | same-family calibration plus scale-reference routing | `w`-free after routing |
| `8/9` central-sector count | cardinality fact, not an inter-sector weight | independent of `w` as a count |

The last row is not a weighting rule. The parent no-go remains: the
central-sector count does not pick the inter-sector weight.

## Residual Triple

On this supplied class, `w`-sensitive content remains in exactly the following
places:

1. off-diagonal evaluation;
2. cross-family comparison without common calibration;
3. raw absolute normalization not routed through the scale-reference primitive.

This is a bounded residual map, not a registry decision. Whether `w` should
later be treated as a convention relative to a retained surface is owner and
audit-lane business outside this note.

## Does NOT

- Does not close any wall or gate.
- Does not claim CTX-match or adopt an EW readout context.
- Does not reclassify `w`.
- Does not turn a scale-reference primitive into a bounded-status source.
- Does not derive a new generation-sector value.
- Does not supply a new readout context, weighting, selector, probability rule,
  or bridge.
- Does not assert anything about future or unlisted readouts.
- Does not edit axiom, primitive, policy, registry, audit, or publication
  surfaces.

## Dependencies

- [`C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md`](C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md)
- [`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md)
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md)

## No-Promotion Statement

This note promotes nothing. It records finite two-cell algebra and leaves all
status decisions to the independent audit lane.
