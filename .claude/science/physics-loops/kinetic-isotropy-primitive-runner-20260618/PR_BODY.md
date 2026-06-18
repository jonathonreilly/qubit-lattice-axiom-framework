## Summary

Registers a primitive-boundary runner for the critical
`kinetic_isotropy_primitive` meta row.

Current `origin/main` has the approved primitive source note and machine
premise registry entry, but the audit ledger row has `runner_path: null`. This
PR adds a primary runner that verifies source, policy, registry, no-overclaim
boundaries, and the existing axiom/primitive purity guard.

## Trace gate

- trace_class: methodology
- target_claim_id: `kinetic_isotropy_primitive`
- reachability: supports audit handling by providing an explicit primary runner
- artifact_role: runner_certificate
- handoff: `.claude/science/physics-loops/kinetic-isotropy-primitive-runner-20260618/HANDOFF.md`
- certificate: `.claude/science/physics-loops/kinetic-isotropy-primitive-runner-20260618/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `python3 scripts/kinetic_isotropy_primitive_boundary_check_2026_06_09.py` -> `PASS=31 FAIL=0`
- `python3 scripts/cached_runner_output.py scripts/kinetic_isotropy_primitive_boundary_check_2026_06_09.py`
- `python3 -m py_compile scripts/kinetic_isotropy_primitive_boundary_check_2026_06_09.py`
- `python3 docs/audit/scripts/check_axiom_premise_clean.py`
- `git diff --cached --check`
- forbidden audit/status path guard clean

## Discipline

No audit result, ledger JSON, queue, publication effective-status, front-door
status, lane registry, active-review queue, or premise registry files are
edited. This PR does not prove downstream Lorentz restoration, dynamics,
spacing, masses, couplings, selectors, readout bridges, or any observable.
