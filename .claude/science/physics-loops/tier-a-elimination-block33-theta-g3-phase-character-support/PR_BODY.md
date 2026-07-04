# Summary

Loop pack:
`.claude/science/physics-loops/tier-a-elimination-block33-theta-g3-phase-character-support/HANDOFF.md`

Block33 adds exact-support evidence for theta G3. On the supplied SU(3)
central-sector projection from Block32, closed Heisenberg triples have an
orientation-odd cocycle `q_c = k(ABC) - k(ACB)`; swapping two staples maps
`q_c` to `-q_c`, so a central phase character conjugates while real weights
remain even.

# Claim Status

- Honest status: exact-support / bounded theorem.
- Trace class: upstream support for `strong_cp_theta_zero_note`, specifically
  the G3 phase-type insertion blocker.
- No theta retirement, no `theta_bar = 0`, no physical phase source, no
  physical SU(3) sector registration, no Tier-A registry edit.

# Artifacts

- `docs/THETA_G3_CENTRAL_SECTOR_PHASE_CHARACTER_EXACT_SUPPORT_NOTE_2026-07-04.md`
- `scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py`
- `logs/runner-cache/theta_g3_central_sector_phase_character_exact_support_2026_07_04.txt`
- `.claude/science/physics-loops/tier-a-elimination-block33-theta-g3-phase-character-support/HANDOFF.md`
- `.claude/science/physics-loops/tier-a-elimination-block33-theta-g3-phase-character-support/TRACE_GATE.md`
- `.claude/science/physics-loops/tier-a-elimination-block33-theta-g3-phase-character-support/CLAIM_STATUS_CERTIFICATE.md`

# Verification

- `PYTHONPATH=scripts python3 scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py` -> `PASS=115 FAIL=0`
- `python3 -m py_compile scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS; newly seeded rows=1
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS; existing 23 warnings / 178 notices, no errors
- `git diff --check` -> PASS

# Remaining Blockers

- Physical G3 phase source, coefficient, and action entry.
- Physical SU(3) central cocycle sector/readout registration.
- G1 defect closure or suppression.
- Theta mass-side determinant-channel bridge.
