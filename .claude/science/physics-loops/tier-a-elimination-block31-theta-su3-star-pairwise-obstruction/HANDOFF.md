# Handoff

## Current Block

Block31 targets the theta gauge-side SU(3) star pairwise-reduction shortcut.

Branch: `physics-loop/tier-a-elimination-block31-theta-su3-star-pairwise-obstruction-20260704`
Base: `physics-loop/tier-a-elimination-block30-ac-reta-formation-nonsupply-20260704`

## Expected Claim Movement

The block should not edit the Tier-A registry. Its movement is:

```text
The SU(2) pairwise-reduction simplification does not transfer to SU(3):
two exact SU(3) triples have the same separate and pairwise class data but
different dagger-even triple data.
```

## Boundaries

- No theta retirement.
- No `theta_bar = 0` derivation.
- No physical SU(3) sector/readout registration.
- No G3 phase insertion.
- No primitive or axiom registration.
- No registry, audit verdict, or publication edit.

## Verification

- `PYTHONPATH=scripts python3 scripts/theta_su3_star_pairwise_reduction_obstruction_2026_07_04.py` -> PASS (`PASS=63 FAIL=0`)
- `python3 -m py_compile scripts/theta_su3_star_pairwise_reduction_obstruction_2026_07_04.py` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS; newly seeded rows=1
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS; existing 23 warnings / 178 notices, no errors
- `git diff --check` -> PASS
- New audit row -> `theta_su3_star_pairwise_reduction_obstruction_no_go_note_2026-07-04`, `claim_type=no_go`, `audit_status=unaudited`, `effective_status=unaudited`, `criticality=leaf`

## Next Exact Action

Commit, push, open a stacked review PR against Block30, then verify hosted
`audit_pipeline`.
