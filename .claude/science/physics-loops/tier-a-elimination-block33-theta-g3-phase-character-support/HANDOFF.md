# Handoff

## Current Block

Block33 targets theta G3 after the SU(3) central-sector projection support in
Block32.

Branch: `physics-loop/tier-a-elimination-block33-theta-g3-phase-character-support-20260704`
Base: `physics-loop/tier-a-elimination-block32-theta-su3-sector-projection-20260704`

## Expected Claim Movement

The block should not edit the Tier-A registry. Its movement is:

```text
On a supplied SU(3) central-sector projection, closed Heisenberg triples have
an orientation-odd central cocycle q_c whose phase character conjugates under
reflection. Real class weights are even; the complex character is the finite
odd-sensitive slot a future physical G3 theorem would need to supply.
```

## Boundaries

- No theta retirement.
- No `theta_bar = 0` derivation.
- No physical G3 phase source or coefficient.
- No physical SU(3) sector/readout registration.
- No G1 defect theorem.
- No mass-side determinant bridge.
- No registry, audit verdict, primitive, axiom, or publication edit.

## Verification

- `PYTHONPATH=scripts python3 scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py` -> PASS (`PASS=115 FAIL=0`)
- `python3 -m py_compile scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS; newly seeded rows=1
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS; existing 23 warnings / 178 notices, no errors
- `git diff --check` -> PASS
- New audit row -> `theta_g3_central_sector_phase_character_exact_support_note_2026-07-04`, `claim_type=bounded_theorem`, `audit_status=unaudited`, `effective_status=unaudited`, `criticality=leaf`

## Next Exact Action

Commit, push, and open a stacked PR on Block32. Then verify hosted
`audit_pipeline` if GitHub checkout is available.
