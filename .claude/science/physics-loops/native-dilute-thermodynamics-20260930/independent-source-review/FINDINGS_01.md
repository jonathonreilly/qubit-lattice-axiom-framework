# Provisional source-review findings, iteration 1

Reviewer: /root/native_thermodynamics_source_review, Astra low.
Source tree: e4b261bde8908d41acbf69663901ac96164080bf.
This record precedes author fixes and is not a final verdict.

## Evidence-description correction (minor, not a mathematical blocker)

CONTROL_DERIVATION.md says under Declared negative controls: “Only actual implementation choices will be changed in scratch copies. Expected values/assertions remain unchanged.” The primary's PLANE_GRADIENT_MULTIPLICITY is consumed only to define `expected` for the gradient comparison (lines 232–233), while its actual grad15 enumeration is unchanged by that mutation. PAIR_QUARTIC_DIVISOR is a standalone normalization formula compared to an independently stated squared vector ratio (lines 124–128). The first is an oracle-coefficient mutation; the second is a formula-sensitivity control rather than a mutation of the literal H action. Their observed AssertionErrors are real and useful, but “never expected values” is too broad. Narrow the evidence description to operator, geometry, formula and oracle-coefficient sensitivity controls, explicitly distinguishing these cases. No scientific result, primary assertion, cache or mutation needs alteration or rerun for this correction.

No consequential mathematical defect has been established at this stage. Complete dispositions and final identity checks remain pending.
