# w Scale-Absorption Classification over Landed Readouts

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope boundary:** Bounded classification result over the named landed-readout
class only; no wall/gate is closed, no CTX-match is claimed, no `w`
reclassification is made, no reading-exclusion closure is made from closed
proposal PR #4847, and no axiom, primitive, policy, registry, audit, or
publication surface is edited.
**Audit boundary:** independent audit lane only. This source note writes no
audit-lane decision, sets no audit status, forecasts no later decision, and
derives no effective status.
**Primary runner:** [`scripts/frontier_w_scale_absorption_classification_2026_07_02.py`](../scripts/frontier_w_scale_absorption_classification_2026_07_02.py)
**Runner output:** [`outputs/frontier_w_scale_absorption_classification_2026_07_02.txt`](../outputs/frontier_w_scale_absorption_classification_2026_07_02.txt)

## FIREWALL

No wall closed. This note does not close the `kappa_EW` wall, CTX-match, any generation-sector gate, or any owner-governed axiom surface.
The `kappa_EW` rows are conditional on CTX-match, and the generation rows are conditional on the landed chain's flow-selection premise.
This note edits no registry and does not reclassify `w`.
PR #4847 is cited only as a closed/unmerged owner-gated proposal; its quoted
sentence is historical/proposal context only, not landed text and not an
in-flight dependency.
The block16/block11 relationships are review-pending, and the audit lane owns status.
This source note and runner edit no axiom, primitive, policy, registry, audit,
or publication surface.
[checks 25-31]

## Purpose

Block16 proved the single-pair diagonal degeneration on the supplied two-cell class.
This note generalizes that degeneration to finite landed readout families and separates diagonal ratio/shape degeneration, single-family scale absorption, and the exact residual places where `w` can still be observed.
The goal is not to choose `w`; it is to classify which landed readouts still have physical sensitivity to `w` after their own stated premises are enforced.

## Supplied And Read Surface

The read files for this block are limited to the named parent notes and primitive memo:

- [`docs/C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md`](C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md)
- [`docs/EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md)
- [`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [`docs/OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md)
- [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

The runner guards three exact parent sentences.
Block16 is present and contains the diagonal formula.
The parent `kappa_EW` note contains `Pi_phys = C + kappa_EW S` and the common-`K_EW` cancellation sentence.
The scale-reference primitive says it is a units conversion, not a physics axiom.
[checks 1-3]

## Supervisor-Supplied Context

The following context is used as supervisor-supplied context rather than as a read dependency.
First, landed charged-lepton readouts have the chain shape: lepton masses enter landed results as mass ratios plus one absolute scale calibrated through the scale-reference primitive.
The Koide-shape functional is degree-0 homogeneous in the masses; with `m_i = y_i^2`, it is `Q(y) = sum(y_i^2) / (sum(y_i))^2`, up to a fixed rational normalization.
Second, PR #4847 is a closed/unmerged owner-gated proposal; the supplied
proposal sentence is "Possibilities are distinguished by the supplied algebraic
structure alone."
This note cites that sentence only as historical/proposal context. It is not a
landed premise and is not a live dependency.
Third, the inherited two-cell setup is `I = u x_A + v x_B`, with `w = v/u` modulo overall scale, and flow-selected states have `x_A = x_B`.

## T1 - Multi-Readout Degeneration

Let `(x_i, x_i)`, `i = 1..n`, be any finite family of diagonal records in the supplied two-cell class.
Every readout has the form `I_i = u x_i + v x_i = (u+v) x_i`.
Therefore every pairwise ratio is `I_i/I_j = x_i/x_j`, provided the denominator is nonzero.
The runner checks this for three distinct `(u,v)` pairs with three different sums.
[check 4]

The same common factor cancels from normalized fractions: `I_i / sum_j I_j = x_i / sum_j x_j`.
The runner checks the normalized table exactly.
[check 5]

Any degree-0 homogeneous rational functional of the diagonal readout vector is also independent of `w`.
For the Koide-shape witness, the runner uses square-content masses so that the scaled roots remain exact fractions.
For a generic degree-0 rational witness, it uses `(I_1^2 + 2 I_2 I_3) / (I_1 + I_2 + I_3)^2`.
Both witnesses are unchanged across the same finite family of different sums.
[checks 6-7]

The diagonal premise is load-bearing.
Off the diagonal, the exact ratio `I(1,0) / I(0,1) = u/v` moves with `w`.
The runner checks three distinct values.
[check 8]

## T2 - Prefactor Absorption under Single-Family Calibration

Dimensionful diagonal readouts carry `w` only through the common prefactor `s = u + v`.
For the specified families `(u,v)=(1,1)`, `(3,2)`, and `(1/2,5/2)`, the sums are `2`, `5`, and `3`.
The runner checks that every raw diagonal table is exactly `s` times the same content table.
[check 9]

The single-family calibration premise is essential:
the calibration readout must come from the same readout family as the reported values.
With `I_cal` from the same family, `I_i/I_cal = x_i/x_cal`, so the three specified families give identical calibrated tables.
[check 10]

The same absorption occurs when units are assigned through the scale-reference primitive against one family member.
If the reference value is `M_ref`, then `I_i * (M_ref / I_cal) = M_ref x_i/x_cal`.
The runner checks the same exact physical table for all three specified families.
[check 11]

Honesty boundary:
cross-family calibration is not covered by T2.
If `I_i` comes from one family and `I_cal` comes from another family with a different sum, the ratio keeps the factor `s/s'`.
The runner exhibits two different cross-family ratios.
[check 12]

## T3 - Instance Classification of Landed Readouts

Each row below is classified only under the row's stated premise.
EW rows are conditional on CTX-match.
Generation rows are conditional on the landed chain's flow-selection premise.

| Landed readout row | Condition | Classification | Runner check |
|---|---|---|---|
| `sin^2(theta_W)` shape `g1^2/(g1^2+g2^2)` with a common `K_EW` factor | conditional on CTX-match; same-family quadratics | `w`-free by common-factor cancellation | 13 |
| Koide-shape `Q` | conditional on flow-selected diagonal states | `w`-free by T1b degree-zero homogeneity | 14 |
| Mass ratios | conditional on flow-selected diagonal states | `w`-free by T1a | 15 |
| Absolute mass scale | single-family calibration plus scale-reference routing | `w`-free by T2 | 16 |
| `8/9` central-sector count | cardinality fact, not a readout value | `w`-free trivially | 17 |

For the count row, the parent wall says the central-sector partition gives the cardinality count `8/9` and "does not pick the inter-sector weight."
The runner separately changes `Pi_phys = C + kappa_EW S` while the cardinality count stays `8/9`.
[check 17]

Conclusion row:
NO landed physical readout in these lanes is `w`-sensitive under its stated premise.
The runner records exactly those five rows and checks that every row is classified `w-free`.
[check 18]

## T4 - Residual Characterization

A `w`-sensitive observable must do at least one of the following:

1. evaluate off the equipartition diagonal;
2. compare readouts across families with different `(u+v)` without common calibration;
3. report an absolute normalization not routed through the scale-reference primitive.

For clause (i), the runner uses two same-sum weight pairs.
An off-diagonal record changes value, while the matching diagonal record does not.
[check 19]

For clause (ii), the runner compares a numerator readout from one family with calibration readouts from different-sum families.
Those cross-family ratios differ.
Replacing the denominator by same-family calibration restores the common `x_i/x_cal` value.
[check 20]

For clause (iii), the runner reports raw absolute diagonal readouts across the three specified families.
The raw values differ.
Routing through the scale-reference primitive against one family member gives one exact table.
[check 21]

This triple is the entire remaining physical content of the missing `w` supplier on this class.
It is the `W_readout_coupling` gate stated operationally:
off-diagonal access, cross-family comparison without common calibration, or unrouted absolute normalization.

## T5 - Reading-Exclusion Context without an Inconsistency Overclaim

T5 has two conditional exclusion facts and one prominent steelman.

First, under the closed/unmerged owner-gated #4847 proposal sentence, set-level
exchange relabelings would not be presentation-preserving if equivalent
owner-approved text landed in the future.
The proposal sentence is:
"Possibilities are distinguished by the supplied algebraic structure alone."
Because #4847 is closed/unmerged, this note makes no live exclusion closure.
The hypothetical consequence is conditional on equivalent owner-approved text
landing independently.
[check 22]

Second, full set-level level-set closure has a counting-collapse consequence.
On a two-possibility domain, exchange closure forces the single-record values to satisfy `I(A)=I(B)=c`.
By finite additivity, a finite collection of records then has readout `c` times the record count.
The runner checks an unequal assignment rejected by closure and equal assignments collapsed to count.
[check 23]

**Steelman / Honesty Witness.**
There is no unconditional claim that a set-level reading contradicts the axioms.
The runner checks a toy majority rule:
available possibilities are exactly those locked by at least half of two neighbors.
This rule varies with neighbor conditions.
It also commutes with every bijection of a two-possibility domain.
Therefore an equivariant availability rule exists.
That steelman blocks the stronger claim that set-level reading is inconsistent with the axioms.
The exclusion above rests on the owner-gated sentence and its recorded approval path, not on contradiction.
[check 24]

## Consequence

On this class, `w` now has the following bounded status map:

- degenerate at flow-selected states by T1;
- absorbed under single-family calibration plus scale-reference routing by T2;
- absent from every landed instance listed in T3;
- alive exactly on the named T4 triple.

Governance hand-off, without acting:
after independent audit, the owner may reclassify `w` as a vacuous rescaling convention relative to the landed class.
That is a registry-surface and owner-only action.
The alternative is to keep `W_readout_coupling` as a registered-number gate for the T4 residue.
This note edits no registry.

## Does NOT

- Does not close any wall.
- Does not reclassify `w`.
- Does not claim CTX-match.
- Does not turn the closed/unmerged #4847 proposal sentence into landed axiom
  text or a live dependency.
- Does not make an unconditional inconsistency claim against set-level readings.
- Does not derive a new generation-sector value.
- Does not supply a new readout context, weighting, selector, probability rule, or bridge.
- Does not edit axiom, primitive, policy, registry, audit, or publication
  surfaces.
- Does not remove the T4 residual gate.
- Does not treat review-pending block16/block11 relationships as settled.

## Dependencies And Context

Direct read dependencies are the five files listed in the supplied surface section.
The parent block16 runner was consulted only for output style and check-line convention.
Supervisor-supplied context is labeled in its own section. Closed/unmerged PR
#4847 is historical/proposal context only, not a graph dependency.
No other repo files are used as mathematical premises here.

## No-Promotion Statement

This note proposes no axiom change, no primitive change, no policy change, and no registry action.
The independent audit lane is the only status authority.
