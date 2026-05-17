# PR #230 Block112 Helmholtz Action-Integrability Obstruction

Status: exact negative boundary / current PR230 response surface lacks
Helmholtz mixed-derivative rows for accepted same-source EW/Higgs action.

## Scope

The cleanest closure route is still an accepted same-surface EW/Higgs action or
canonical `O_H`, followed by physical Euclidean `C_ss/C_sH/C_HH(tau)` pole
rows.  Block112 tests a narrower possible shortcut: whether current
source-response and finite correlator rows already contain enough mixed
response data to integrate a same-source action coordinate and fix the
source-Higgs overlap.

For a response one-form to be the gradient of an action, its mixed Jacobian
must satisfy the Helmholtz symmetry condition.  Even after imposing that
symmetry, the actual mixed source-Higgs row value remains data; it cannot be
read from a source-only row.

## Result

The current surface does not contain the required mixed rows.

The runner verifies:

- parent certificates are present and none authorizes proposal wording;
- Block109 still selects the `O_H`/action plus source-Higgs pole-row root;
- Block110 blocks the finite-algebra-to-action shortcut;
- Block111 blocks finite-packet-to-Schur-K-prime promotion;
- no strict same-surface action, canonical `O_H`, source-Higgs pole-row, W/Z
  response, matched covariance, or `delta_perp` row artifact exists;
- all `63` higher-shell row files are present and schema-clean;
- all `63` chunks contain finite taste-radial alias rows, but canonical
  `O_H` identity is false on all chunks;
- source-Higgs time-kernel rows are nonempty on `0` chunks;
- W/Z response rows are nonempty on `0` chunks;
- scalar source-response slopes are present on all `63` chunks, but they are
  source-direction data only.

The finite counterfamily makes the obstruction explicit:

- a nonsymmetric two-coordinate response Jacobian can share the same visible
  source signature while failing Helmholtz integrability;
- symmetric positive quadratic actions can share the same source-source block
  while giving distinct normalized source-Higgs overlaps `0.0`, `0.25`, and
  `0.6`.

Thus source-only response and finite taste-radial rows do not determine an
accepted action coordinate or `kappa_sH`.

## Claim Boundary

This is an inverse-variational obstruction only.  It does not model PR230
dynamics, claim retained or `proposed_retained` closure, infer an EW/Higgs
action from finite rows, identify taste-radial `x` with canonical `O_H`, or
relabel `C_sx/C_xx` as physical `C_sH/C_HH`.

Forbidden proof inputs remain excluded: `H_unit`, `yt_ward_identity`, observed
targets, `alpha_LM`, plaquette/`u0`, reduced pilots, and unit assignments
`kappa_s=1`, `c2=1`, `Z_match=1`, or `g2=1`.

## Artifacts

- Runner:
  `scripts/frontier_yt_pr230_block112_helmholtz_action_integrability_obstruction.py`
- Certificate:
  `outputs/yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json`
- Campaign status integration:
  `scripts/frontier_yt_pr230_campaign_status_certificate.py`
- Assumption/import stress integration:
  `scripts/frontier_yt_pr230_assumption_import_stress.py`

## Validation

```text
python3 -m py_compile scripts/frontier_yt_pr230_block112_helmholtz_action_integrability_obstruction.py scripts/frontier_yt_pr230_campaign_status_certificate.py scripts/frontier_yt_pr230_assumption_import_stress.py scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py scripts/frontier_yt_retained_closure_route_certificate.py scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# OK
python3 scripts/frontier_yt_pr230_block112_helmholtz_action_integrability_obstruction.py
# SUMMARY: PASS=15 FAIL=0
python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
# SUMMARY: PASS=432 FAIL=0
python3 scripts/frontier_yt_pr230_assumption_import_stress.py
# SUMMARY: PASS=115 FAIL=0
python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py
# SUMMARY: PASS=200 FAIL=0
python3 scripts/frontier_yt_retained_closure_route_certificate.py
# SUMMARY: PASS=325 FAIL=0
python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# SUMMARY: PASS=79 FAIL=0
python3 docs/audit/scripts/audit_lint.py --strict
# OK: no errors; 5 known warnings
bash docs/audit/scripts/run_pipeline.sh
# Pipeline complete; generated docs/audit diffs restored
git diff --check
# OK
```

## Exact Next Action

Supply one accepted mixed-response/action artifact: a same-surface EW/Higgs
action certificate with Helmholtz-symmetric source/Higgs/W/Z response Hessian
rows, canonical `O_H` and `C_ss/C_sH/C_HH` pole rows, or a strict W/Z packet
with matched top-W/Z covariance and an allowed absolute pin.  Do not promote
source-only or finite taste-radial rows to an action-integrability certificate.
