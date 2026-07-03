# Record-Content Readout License Split and the Registration Unreachability of the Unit-Variance Point

**Date:** 2026-07-02

**Claim type:** bounded_theorem

**Audit status:** set only by the independent audit lane. This source note
does not set, predict, or apply an audit verdict.

**Primary runner:** [`scripts/record_content_readout_license_split_registration_unreachability_2026_07_02.py`](../scripts/record_content_readout_license_split_registration_unreachability_2026_07_02.py)

## Purpose

The 2026-07-02 Record-axiom clarification supplies the readout clause:

> "Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`."

This note applies that clause to the floor-vs-increment split left by the
native-carrier registration kernel rate-vs-unit-variance-point row
(`NATIVE_CARRIER_REGISTRATION_KERNEL_RATE_VS_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md`,
not a citation-graph dependency here). The kernels used below are re-derived
in-packet from the supplied graph-first carrier content, not imported as a
black-box conclusion.

Three adjacent rows are prose-named for orientation only: the binary
registration capacity row
(`GAUGE_LINK_BINARY_REGISTRATION_CAPACITY_STEP_KERNEL_PIN_THEOREM_NOTE_2026-07-02.md`,
not a citation-graph dependency), the informative-fraction occupancy residual
row
(`INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_OCCUPANCY_RESIDUAL_THEOREM_NOTE_2026-07-02.md`,
not a citation-graph dependency), and the per-record-step rate-dial row
(`GAUGE_LINK_PER_RECORD_STEP_RATE_DIAL_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md`,
not a citation-graph dependency). Their names locate the question; the
calculation below does not depend on their citation graph.

The results are: the identity-channel floor writes no record and is
readout-construction content, while the record-determined component is exactly
`T_V - T_id = -Re chi_3`; for `(1-p) delta + p T_V`, the record-determined
per-step variance is at most `Delta m^2 = 0.605570 < 1`, so the unit point is
not attainable as record-determined content at any informative fraction; and
at the total-variance unit point `p* = 0.409731`, the record-determined share
is `0.248120` while the reconstruction share is `0.751880`.

The runner recomputes these values from the centered Weyl grid. External
anchors are used only as gates.

The license split is therefore a status distinction inside a computed
transfer construction. It is not a deletion of the total calculation.

## Supplied surfaces (cited at audited scope)

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  readout clause quoted above.
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  supplies the graph-first carrier content from which the in-packet kernels are
  re-derived.
- [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md)
  supplies the canonical normalization and the zero-sum logarithm branch.
- [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
  is respected: the note does not derive that a record step occurs.

## Setup: the two step densities, re-derived

On the named holonomy-family transition-density reading, the carrier is
`V = C^8` with `su(3)` content `3 + 3 + 1 + 1`. Let `chi_3(x)` be the
fundamental character and `chi_8(x) = |chi_3(x)|^2 - 1`.

The native carrier step density is
`T_V(x) = (|chi_3(x)|^2 + 1) / 2 = 1 + chi_8(x) / 2`. The identity-channel
readout density is independently
`T_id(x) = |chi_3(x) + 1|^2 / 2 =
1 + (chi_8(x) + chi_3(x) + conj(chi_3(x))) / 2`. Subtracting the two
independently built densities gives `T_V - T_id = -Re chi_3`.

The reading is a defined construction: a holonomy-family transition density
on the named carrier with the stated graph-first and normalization premises.

The spectral checks used by the runner are `w_3(T_id) = 1/6`,
`w_3(T_V) = 0`, `w_8(T_V) = 1/16`, and `w_8(T_id) = 1/16`.

## Theorem 1 (the license split)

The readout clause says:

> "Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`."

In the holonomy-family reading of the native-carrier registration step, with
kernels re-derived in-packet from the graph-first carrier content
`V = C^8`, `su(3)` content `3 + 3 + 1 + 1`,
`T_V = (|chi_3|^2 + 1) / 2`, and `T_id = |chi_3 + 1|^2 / 2`,

the identity channel writes no record. Under the quoted clause, the readout
floor is therefore readout-construction, or reconstruction-side, content.
The record-determined per-step component is exactly
`T_V - T_id = -Re chi_3`, the dephasing of the `3/3bar` coherence blocks. Its
per-step variance is `Delta m^2 = 0.605570`.

The framework's record ontology already licenses reconstructions as
calculational devices. The clause does not delegitimize the total; it
distinguishes the two components' status. This note adjudicates no naming
question. It computes both components and their consequences.

## Theorem 2 (registration unreachability under the record-licensed reading)

For the admissibility-supported per-step family
`(1-p) delta + p T_V`, `0 <= p <= 1`, the record-determined per-step variance
is `p * Delta m^2 <= Delta m^2 = 0.605570 < 1`. The margin of the exclusion is
`1 - Delta m^2 = 0.394430`. The informative fraction that would be needed for
unit record-determined variance is `1 / Delta m^2 = 1.651337 > 1`.

Thus the unit-variance point is not attainable as record-determined content
of registration steps at any informative fraction. This is a range exclusion
for the named reading, named carrier, named per-step family, and single-step
calibration. It strengthens the occupancy row's off-lattice statement under
the record-licensed reading, but that row is not a citation-graph dependency
here. The composed-step license split is an open refinement.

## Theorem 3 (shares at the unit point)

The branch identities and companions are
`<Re chi_3 * s2_naive>_Haar = -19/8` exactly,
`<Re chi_3 * s2_min>_Haar = -2.422278270`,
`<s2_min>_Haar = 9.466227112`, and `<s2>_T_V = 9.762523409`.

The increment and floor are
`increment = -<Re chi_3 * s2_min>_Haar = 2.422278270`,
`floor = <T_id * s2_min>_Haar = 7.340245139`, and
`increment + floor = <s2>_T_V`. The per-step mass-normalized increment is
`Delta m^2 = increment / 4 = 0.605570`.

At the informative fraction where the total per-step variance is unit,
`p* = 4 / <s2>_T_V = 0.409731`. The shares of the unit variance are
`record-determined share = p* * increment / 4 = 0.248120` and
`reconstruction share = p* * floor / 4 = 0.751880`.

The shares sum exactly to one by definition. Under the current axioms the two
landed numbers therefore carry distinct status: the total `m^2 = 2.440631`
is the transfer-level and reconstruction-side quantity, while the increment
`Delta m^2 = 0.605570` is the record-determined quantity. Which of the two the physical transfer
normalization names is for the audit lane; both are computed, exact where
possible, and located, never forced.

## Boundary

- This note does not claim: that the total lacks license. Reconstructions are
  licensed calculational devices in the record ontology; the clause
  distinguishes status, it does not forbid reconstruction-level matching.
- This note does not claim: that it can name the physical transfer
  normalization. It does not adjudicate which component the physical transfer
  normalization names.
- This note does not claim: that a record step occurs; the semigroup boundary
  is respected.
- This note does not claim: that the license split has already been extended
  to composed steps. That is an open refinement.
- This note does not claim: that the reading is unique. The reading is a
  defined construction with named premises.
- This note does not claim: any Wilson action-surface selection.
- This note does not claim: any continuum limit.
- This note does not claim: an audit verdict or any effective-status
  promotion.

Forward surface:

- the composed-step license decomposition;
- whether the transfer-surface normalization should be read at the
  record-determined or reconstruction level, which is an identification
  question rather than a computation;
- alternative licensed readout families, where the license split localizes
  what any family must now separate.

## Falsifiers

- Section A falsifier: the centered Weyl-grid Haar density is not normalized,
  the independently built densities do not satisfy
  `T_V - T_id = -Re chi_3`, or the spectral coefficients miss the stated
  anchors.
- Section B falsifier: the naive-principal branch identity does not converge
  toward `-19/8`, the zero-sum branch misses the stated moment anchors, or the
  increment/floor/total identity fails.
- Section C falsifier: `Delta m^2` reaches or exceeds one, the exclusion
  margin is not positive at the stated scale, or the monotone informative
  fraction bound fails for the checked exact fractions.
- Section D falsifier: the unit-total point is not at `p* = 0.409731`, the two
  shares miss `0.248120` and `0.751880`, or the shares do not sum to one.
- Section E falsifier: the source-boundary guard cannot find the note, the
  four dependency notes, the required dependency markers, the preserve markers,
  or the forbidden-string exclusions.

## Verification

Run:

```bash
python3 scripts/record_content_readout_license_split_registration_unreachability_2026_07_02.py
```

Expected:

```text
TOTAL: PASS=63 FAIL=0
```
