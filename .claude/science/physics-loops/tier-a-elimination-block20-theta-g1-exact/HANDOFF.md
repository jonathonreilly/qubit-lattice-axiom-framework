# Handoff

## Current Block

Block 20 is a no-go for the exact global branch constraint shortcut inside
theta gauge-side G1 defect closure.

Branch: `physics-loop/tier-a-elimination-block20-theta-readiness-20260704`
Base: `physics-loop/tier-a-elimination-block19-acii-kbreaking-20260704`
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4948
Source commit: `3ea49b00d`

## Expected Claim Movement

The block should not edit the Tier-A registry. Its movement is:

```text
n=dA exactness gives dn=0 but erases the H^2(T^4,Z) flux carrier and forces
Q=0; G1 needs closed non-exact sectors or defect suppression, not global
exactness.
```

## Boundaries

- No theta retirement.
- No `theta_bar = 0` derivation.
- No primitive, axiom, registry, audit verdict, or publication edit.
- No physical SU(3) theta-sector/readout registration.
- No exclusion of future closed-nonexact, bundle, transition-function, or
  defect-suppression routes.
- No mass-side determinant-channel bridge.

## Verification

- `PYTHONPATH=scripts python3 scripts/theta_g1_exact_branch_constraint_no_go_2026_07_04.py` -> PASS (`PASS=138 FAIL=0`)
- `python3 -m py_compile scripts/theta_g1_exact_branch_constraint_no_go_2026_07_04.py` -> PASS
- `git diff --check` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS; newly seeded rows=1
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS; existing 23 warnings / 178 notices, no errors
- New audit row -> `theta_g1_exact_branch_constraint_no_go_note_2026-07-04`, `claim_type=no_go`, `audit_status=unaudited`, `effective_status=unaudited`, `criticality=leaf`
- Local review-loop emulation -> PASS WITH BOUNDED CLAIMS

## Next Exact Action

Verify PR status, then continue the Tier-A elimination campaign toward
closed-nonexact sector derivation, dynamical defect suppression, or a
mass-side determinant positive route.
