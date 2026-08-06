# Historic intake: Analysis: Asymmetric Decoherence

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_analysis
Stratum: march_2026_event_network_era
Era: march_event_network — assumes fixed causal DAG with recorded/free sectors traversing the same path topology

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Delay-field distortion does NOT cause decoherence, even asymmetrically: V remains ~1.000 at y=0 and unchanged at all off-center positions for ALL p from 0.0 to 0.9, for both symmetric and asymmetric field distortion, at cluster radii 1 and 2. Only p=1.0 (which changes sector-labeling, not just the field) produces any visibility change.

Original verdict: Hypothesis REFUTED — decoherence in this model requires topological DAG changes, not field perturbations.
Scope: Fixed causal DAG; delay-field/amplitude perturbations on existing edges only; cluster radii 1 and 2; distortion parameter p in [0,1].
Escape conditions (negative claims): The negative is stated to depend on the distortion being a FIELD acting equally on all paths through a region on a FIXED DAG, and on visibility being defined as (max-min)/(max+min) over a full phase sweep (invariant to path-independent amplitude rescaling); the escape named is topology change (add/remove nodes, change the DAG), which the note says gives massive effect (I3 up to 1e9). p=1.0 escapes by changing sector-labeling rather than the field.

## Why pulled (supervisor decision, on the record)

Exact no-go: field perturbations cannot decohere on a fixed DAG (V unchanged for all p<1, both symmetries, radii 1-2); escape conditions stated (topology change; p=1 relabels sectors); survives the era's own corrections and is re-confirmed by the corrected-propagator single-pass failures.

## Provenance (pinned)

- Original path: `.claude/science/analyses/asymmetric-decoherence-2026-03-30.md`
- Source commit: `7009321794f635282e2e9f6f28c129b62d50d990`
- git blob: `399ce6ae2a5d42f25f88532532a49e50979af375`
- sha256: `fc5de417d555c655dc21489130ab0d303afaec619a112daceb215c40f65cc738`
- Lines: 34; runners named: none

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
