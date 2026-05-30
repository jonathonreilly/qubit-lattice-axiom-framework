---
claim_id: yt_strict_same_source_top_w_pole_row_contract_note_2026-05-30
claim_type_author_hint: open_gate
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Strict Same-Source Top/W Pole-Row Contract

**Claim type:** open_gate / evidence contract.
**Role:** define the exact strict-response evidence needed to bypass the
Tier-A source-measure source-unit premise.
**Status authority:** independent audit lane only. This source note is a
contract only; it does not claim positive Y_T closure without an evidence
certificate or retained-grade top-response theorem.
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

- source-coordinate invariance of the top/W ratio
  ([`YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md`](YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md));
- neutral Higgs carrier-ray support
  ([`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md));
- strict W/Z denominator response rows
  ([`YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md`](YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md));
- symbolic top row shape
  ([`YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md`](YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md)).

But the current repo does not yet have:

- coefficient-certified top response row;
- strict same-source pole-response evidence;
- shared covariance/contact-subtraction/finite-volume certificate;
- same-scale `g_2` authority for a numerical `y_33`.

Therefore this note is an evidence contract, not a proof of Y_T.
The current blocking no-go/boundary rows are
[`YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md`](YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md)
and
[`YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md`](YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md).

## Evidence Boundary

```yaml
production_certificate_present: false
strict_same_source_top_w_response_evidence_present: false
contract_passes_schema: true
response_value_claimed: false
```

If a future certificate supplies the required rows and passes this contract,
then it can replace the Tier-A source-measure premise for the source-unit part
of Y_T.  Downstream use would still depend on `g_2`, matching/running, and
top-carrier/hypercharge audit state.

## Non-Claims

This note does not claim:

- Y_T closure;
- a measured `dM_t/dh` or `dM_W/dh`;
- a production top-correlator result;
- a same-scale `g_2` value;
- matching/running closure;
- use or repair of `H_unit`, `yt_ward_identity`, or `y_t_bare`;
- use of PDG targets, observed top/W/Z masses, `alpha_LM`, plaquette/u0,
  Planck, alpha_s, or fitted selectors as proof inputs.

## Boundary Summary

This contract supplies only:

- the exact schema for non-P-cal top/W response evidence;
- the source-coordinate cancellation condition;
- the transfer-pole derivative form.

It does not supply:

- actual same-source pole-response measurement or theorem;
- same-scale `g_2` authority;
- matching/running closure;
- a unilateral audit/status outcome.

## Verification

Run:

```text
python3 scripts/frontier_yt_strict_same_source_top_w_pole_row_contract.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
