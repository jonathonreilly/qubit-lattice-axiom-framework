## Summary

Repairs the audited-conditional lattice total momentum row after the
Noether Step 4b narrowing landed and audited clean.

- narrows the source claim to conserved two-step translation sectors;
- removes canonical `P_x` divergence, full one-site momentum, `H_phys`,
  boost, and continuum corollary claims;
- replaces the old mostly-trivial runner with a nontrivial finite-sector
  check that distinguishes exact `T_2` symmetry from unsupported `T_1`
  symmetry.

## Verification

- `python3 -m py_compile scripts/lattice_total_momentum_conservation_check.py`
- `python3 scripts/lattice_total_momentum_conservation_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `git diff --check`

## Audit Queue Result

`lattice_total_momentum_conservation_theorem_note_2026-05-02` is now:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `claim_type`: `bounded_theorem`
- ready for audit: yes
- queue rank after this branch pipeline: 915
- runner: `scripts/lattice_total_momentum_conservation_check.py`

No audit verdict is applied in this PR.
