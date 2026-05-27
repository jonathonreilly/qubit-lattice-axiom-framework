---
claim_id: yt_direct_same_surface_sparse_transfer_response_certificate_note_2026-05-27
claim_type_author_hint: bounded_support
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Direct Same-Surface Sparse Transfer Response Certificate

**Claim type:** bounded-support microbench / certificate scaffold.
**Role:** first concrete implementation target after the strict top/W response
coefficient obstruction.
**Status:** bounded support only; no retained or proposed-retained Y_T closure.
**Primary runner:**
`scripts/frontier_yt_direct_same_surface_sparse_transfer_response_certificate.py`
**Generated output:**
`outputs/yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json`

## Purpose

The current Y_T closure stack has pruned two shortcuts:

```text
current structural source law -> physical top Yukawa source coordinate
same-source/W-row/symbolic-top support -> coefficient-certified top pole row
```

The live audit-clean positive route is now a strict same-surface top/W response
certificate.  The certificate has to compute, on one accepted transfer/action
surface,

```text
dM_t/dh, dM_W/dh,
```

then read

```text
y_readout = (g_2 / sqrt(2)) (dM_t/dh) / (dM_W/dh)
```

without inserting the top coefficient as an input.

This packet builds the response-certificate harness.  It is deliberately not a
production dynamics solve.  It makes the failure mode mechanical: a backend
that contains `kappa` is read correctly and rejected as non-proof.

## Certificate Schema

The strict positive certificate must eventually supply:

```yaml
same_source_id: ...
surface_id: ...
top_pole_isolated: true
w_pole_isolated: true
dM_t_dh: coefficient-bearing expression with no free kappa input
dM_W_dh: coefficient-bearing expression on the same source
vacuum_contact_subtraction_done: true
finite_volume_ir_controls_pass: true
same_model_class: accepted physical same-surface transfer backend
same_scale_g2: same-scale certified, or explicitly ratio-scoped
contains_free_top_coefficient_input: false
no_forbidden_imports: true
proposal_allowed: true only after all fields close
```

This runner evaluates that schema on two backends:

1. a tainted counterfamily backend, which should fail as closure;
2. a candidate action backend stub, which is blocked until an accepted finite
   same-surface top/W transfer/action backend is supplied.

## Counterfamily Backend

The counterfamily backend is a diagonal three-sector transfer matrix with a
single source `h`:

```text
Lambda_0(h) = 1
Lambda_W(h) = exp[-a_t g_2 v(h) / 2]
Lambda_t(h) = exp[-a_t kappa v(h) / sqrt(2)]
v(h) = v_0 + A h
```

It produces isolated vacuum, W, and top rows and gives

```text
dM_W/dh = g_2 A / 2
dM_t/dh = kappa A / sqrt(2)
```

so the response readout returns

```text
(g_2 / sqrt(2)) (dM_t/dh) / (dM_W/dh) = kappa.
```

That is useful because it verifies the response machinery and taint scan.  It
also proves that this backend cannot certify Y_T closure: the top coefficient
entered as an input.

## Candidate Action Backend

The candidate action backend is intentionally blocked on the current branch.
The missing object is an accepted finite same-surface top/W transfer/action
backend with:

- one physical source id for the top and W rows;
- isolated vacuum, W, and top spectral projectors;
- a source generator with no free `kappa`, no hardcoded `1/sqrt(6)`, and no
  observed mass target;
- coefficient-certified Feynman-Hellmann rows for `dM_t/dh` and `dM_W/dh`;
- contact/vacuum subtraction;
- finite-volume and infrared controls;
- same model class;
- same-scale `g_2`, or an explicit ratio-only scope.

Until that backend exists, the strict response route remains open.  This note
therefore provides the harness and failure certificate, not the response
evidence itself.

## Status Boundary

Actual current-surface status:

```yaml
actual_current_surface_status: bounded-support microbench / open strict-response backend
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
proposal_allowed_reason: |
  The harness rejects a kappa-tainted counterfamily backend and records the
  missing accepted finite top/W transfer backend.  It does not derive a
  coefficient-bearing top pole response row.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: >
  Supply an accepted finite same-surface top/W transfer/action backend with
  isolated vacuum/W/top projectors, then rerun this certificate to compute
  dM_t/dh and dM_W/dh without kappa as an input.
```

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- claim the strict top/W response certificate passes;
- derive `y_t`, `m_t`, `v = 246 GeV`, or same-scale `g_2`;
- provide production Monte Carlo evidence;
- provide a physical finite transfer/action backend;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG
  targets, `alpha_LM`, plaquette/u0, Planck, alpha_s, or fitted selector as
  proof inputs.

## Verification

Run:

```text
python3 scripts/frontier_yt_direct_same_surface_sparse_transfer_response_certificate.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
