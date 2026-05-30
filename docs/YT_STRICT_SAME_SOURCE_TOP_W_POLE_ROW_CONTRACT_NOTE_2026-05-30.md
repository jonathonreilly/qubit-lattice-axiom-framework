---
claim_id: yt_strict_same_source_top_w_pole_row_contract_note_2026-05-30
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Strict Same-Source Top/W Pole-Row Contract

**Claim type:** bounded theorem / evidence contract.
**Role:** define the exact strict-response evidence needed to bypass the
Tier-A source-measure source-unit premise.
**Status:** exact-support contract only; no positive Y_T closure without an
evidence certificate or a retained top-response theorem.
**Primary runner:** `scripts/frontier_yt_strict_same_source_top_w_pole_row_contract.py`
**Generated output:** `outputs/yt_strict_same_source_top_w_pole_row_contract_2026-05-30.json`

## Question

The Tier-A route closes the Y_T source scalar by accepting the source-measure
P-cal/RN-Fisher source unit.  Is there a non-P-cal route?

Yes, but it must be an observable same-source response route:

```text
same source h
  -> dM_t/dh and dM_W/dh on the same transfer/action surface
  -> y_33 = (g_2/sqrt(2)) (dM_t/dh)/(dM_W/dh).
```

This note defines the strict evidence contract for that route.  It does not
produce the evidence.

## Required Evidence Certificate

A strict certificate must supply all of the following:

```text
same_source_id
same_transfer_action_surface
isolated_top_pole Lambda_t(h)
isolated_W_pole Lambda_W(h)
vacuum pole Lambda_0(h)
contact-subtraction prescription
finite-volume / IR controls
model-class checks
shared jackknife or bootstrap covariance
same-scale g_2 authority, or a deliberately scoped y_33/g_2 ratio
```

The pole masses must be read on the same source surface:

```text
M_X(h) = -a_t^{-1} log[Lambda_X(h) / Lambda_0(h)].
```

The derivatives must use the same source coordinate `h`:

```text
R_topW = (dM_t/dh) / (dM_W/dh).
```

Then the response readout is

```text
y_33 = (g_2/sqrt(2)) R_topW.
```

The `1/sqrt(6)` target is equivalent to

```text
R_topW = sqrt(2) / (g_2 sqrt(6)).
```

## Why This Bypasses The Source-Unit Pin

If the source is reparameterized by any local coordinate change
`h = f(s)` with nonzero derivative, both responses pick up the same Jacobian:

```text
dM_t/ds = (dM_t/dh) f'(s),
dM_W/ds = (dM_W/dh) f'(s).
```

Therefore

```text
(dM_t/ds)/(dM_W/ds) = (dM_t/dh)/(dM_W/dh).
```

This route does not need the absolute RN/Fisher source unit.  It needs a
same-source physical response measurement or theorem.  That is why it is the
clean alternative to the Tier-A P-cal source-measure route.

## Current Repo Boundary

The current repo already has the algebraic pieces:

- source-coordinate invariance of the top/W ratio;
- neutral Higgs carrier-ray support;
- strict W/Z denominator response rows;
- symbolic top row shape.

But the current repo does not yet have:

- coefficient-certified top response row;
- strict same-source pole-response evidence;
- shared covariance/contact-subtraction/finite-volume certificate;
- retained same-scale `g_2` authority for a numerical `y_33`.

Therefore this note is an evidence contract, not a proof of Y_T.

## Evidence Status

```yaml
production_certificate_present: false
strict_same_source_top_w_response_evidence_present: false
contract_passes_schema: true
response_value_claimed: false
proposal_allowed: false
```

If a future certificate supplies the required rows and passes this contract,
then it can replace the Tier-A source-measure premise for the source-unit part
of Y_T.  The resulting status would still depend on `g_2`, matching/running,
and top-carrier/hypercharge audit state.

## Non-Claims

This note does not claim:

- retained Y_T closure;
- a measured `dM_t/dh` or `dM_W/dh`;
- a production top-correlator result;
- a retained same-scale `g_2` value;
- matching/running closure;
- use or repair of `H_unit`, `yt_ward_identity`, or `y_t_bare`;
- use of PDG targets, observed top/W/Z masses, `alpha_LM`, plaquette/u0,
  Planck, alpha_s, or fitted selectors as proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
target_blocker_text: "strict same-source top/W pole response evidence"
source_of_blocker_text: "yt_fh_top_w_response_ratio_gate_note_2026-05-25 and yt_top_response_coefficient_underdetermination_no_go_note_2026-05-25"
reachability_to_target: supports
artifact_role: evidence_contract
closed_on_this_surface:
  - exact schema for non-P-cal top/W response evidence
  - source-coordinate cancellation condition
not_closed:
  - actual same-source pole response measurement/theorem
  - same-scale g_2 authority
  - matching/running
proposal_allowed: false
proposal_allowed_reason: >
  This is a contract for future evidence. It does not supply the evidence.
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Verification

Run:

```text
python3 scripts/frontier_yt_strict_same_source_top_w_pole_row_contract.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
