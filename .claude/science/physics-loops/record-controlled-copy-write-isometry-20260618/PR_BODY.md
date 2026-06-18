# Summary

This PR is a source-side science repair for the audited-conditional `record_formation_to_kraus_isometry_bridge_2026-06-06` row. It does not audit, retag, or edit any audit/status surface.

The current blocker asks for a theorem deriving the ideal pointer-label record-write isometry from finite controlled-copy/fresh-fragment dynamics. This branch adds that theorem:

```text
U_cc(pi/4)(|psi>|0>) = P_0|psi>|eta_0> + P_1|psi>|eta_1>
<eta_0|eta_1> = 0
C_R|eta_r> = |r>
W|psi> = P_0|psi>|0> + P_1|psi>|1>
K_r = <r|W = P_r
```

# Claim Status

- Actual current branch status: `exact-support`
- Trace class: `direct_blocker_closure`
- Reachability: closes the source-side controlled-copy-to-write-isometry blocker only
- Independent audit required before any effective-status movement: yes
- Bare retained/proposed retained claim: no

# Artifacts

- New theorem note: `docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`
- New runner/output/cache: `scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py`, `outputs/record_formation_controlled_copy_write_isometry_2026_06_18.json`, `logs/runner-cache/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.txt`
- Updated target bridge note/runner/cache: `docs/RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`, `scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py`, `logs/runner-cache/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.txt`
- Loop pack: `.claude/science/physics-loops/record-controlled-copy-write-isometry-20260618/`

# Verification

```text
python3 scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py
python3 scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
python3 -m py_compile scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
git diff --check
```

# Boundaries

This PR does not derive arbitrary persistent dynamics to `W`, derive the bounded quantum-Darwinism record reading from Minimal Axioms, choose a physical Hamiltonian/action/coupling/clock/rate, derive Born probabilities from post-record counts, or close downstream generation/Koide/selector choices.

No files under `docs/audit/**`, publication effective-status surfaces, front-door status, lane registry, active review queue, or lane status board are changed.
