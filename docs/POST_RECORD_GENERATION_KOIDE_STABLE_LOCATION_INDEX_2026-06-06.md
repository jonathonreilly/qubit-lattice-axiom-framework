# Post-Record Generation/Koide Stable-Location Index

**Date:** 2026-06-06
**Type:** exact support / supplied stable-location index
**Claim type:** positive_theorem
**Status:** exact-support source-side for supplied generation/Koide
stable-location indexing; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py`](../scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_generation_koide_stable_location_index_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_generation_koide_stable_location_index_2026_06_06.txt)
**Bounded row export:**
[`outputs/post_record_generation_koide_stable_location_index_slice_2026_06_07.json`](../outputs/post_record_generation_koide_stable_location_index_slice_2026_06_07.json)

## Result

This block converts the generation/Koide dial queue into a stable-location
index:

```text
129 koide_or_generation_selector rows
  + 4 generation_or_koide_stable_feature rows
  + supplied stable-setting certificate semantics
  => 133-row generation/Koide stable-location index
```

The index records where a stable location can live on a dial under a supplied
score, rule, map, or kernel. It is not a selected dial.

## Current row map

On the current ledger snapshot, the upstream selector/dial subdivision has
`129` `koide_or_generation_selector` rows. This block splits those selector
rows as:

| Selector row class | Rows |
|---|---:|
| `koide_value_or_phase_location` | 50 |
| `obstruction_or_open_gate` | 45 |
| `generation_structure_location` | 13 |
| `selector_surface_location` | 5 |
| `readout_carrier_or_record_location` | 9 |
| `measure_weight_or_source_location` | 4 |
| `other_generation_koide_location` | 3 |

The flow/thermal stable-setting certificate also exposes `4`
`generation_or_koide_stable_feature` rows:

- `flavor_r_half_is_the_records_flow_separatrix_2026-06-02`;
- `generation_dial_dynamics_stability_classifier_2026-06-05`;
- `koide_oo_rd_premise_relation_on_current_surface_narrow_theorem_note_2026-06-12`;
- `stable_post_record_dial_location_certificate_2026-06-06`.

Total generation/Koide dial-relevant rows indexed here: `133`.

The source packet for the four stable-feature rows is explicit:

- [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md);
- [`GENERATION_DIAL_DYNAMICS_STABILITY_CLASSIFIER_2026-06-05.md`](GENERATION_DIAL_DYNAMICS_STABILITY_CLASSIFIER_2026-06-05.md);
- [`KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md`](KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md);
- [`STABLE_POST_RECORD_DIAL_LOCATION_CERTIFICATE_2026-06-06.md`](STABLE_POST_RECORD_DIAL_LOCATION_CERTIFICATE_2026-06-06.md).

## Meaning

A supplied stable-location certificate can say:

- this supplied coordinate has an exact dial location such as `r=1/2`;
- this supplied map makes the location a fixed point, separatrix, root, or
  score optimum;
- this supplied finite/algebraic check supports the location under that rule.

It cannot say:

- the stable location is selected by physics;
- the location forces Koide or generation;
- the Record axiom derives the score, rule, map, kernel, selector, or measure;
- an obstruction/open-gate row has been promoted.

This preserves the dial discipline: stable locations can be indexed and audited
without forcing the dial.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "generation/Koide dial rows have a stable-location index under supplied rules; selected-dial status remains blocked without a selector"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch indexes stable locations and does not select or force a generation/Koide dial value."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundaries

- Does not edit `docs/audit/data`.
- Does not apply or predict audit verdicts.
- Does not promote any row.
- Does not select or force a generation/Koide dial location.
- Does not turn a stable location into a selected dial.
- Does not derive the stable-setting rule, selector, measure, kernel, clock, or
  physical arrow from Record.
- Does not claim Koide closure.

## Runner certificate

The runner verifies:

- source anchors in this note, the selector/dial subdivision, the stable-setting
  certificate, the conditional evidence ladder, and the two generation/Koide
  stable-feature source notes;
- exact finite examples for `Q(r)=(1+2r)/3`, the supplied `r -> 2r^2`
  separatrix at `r=1/2`, and the objectivity maximum
  `r*=w_p/(2 w_s)`;
- selected-dial status remains blocked without a selector rule;
- bounded ledger-row export exists for the selected generation/Koide index;
- the `129` Koide/generation selector rows split into the row classes above;
- the `4` generation/Koide stable-feature rows are present;
- the combined generation/Koide dial-relevant index has `133` rows;
- the audit ledger hash is unchanged after the scan;
- no audit verdict, audit-data write, retained/promoted claim, selected-dial
  derivation, stable-location-to-selected-dial conversion, or generation/Koide
  dial-selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py
```
