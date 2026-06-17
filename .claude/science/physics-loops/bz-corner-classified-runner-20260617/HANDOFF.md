# Handoff

This PR targets the stale audited-conditional BZ-corner row:

`staggered_dirac_bz_corner_forcing_theorem_note_2026-05-07`

The audit blocker offered two repair paths: prove the BZ-corner
Hamming-parity chirality/sublattice bridge, or narrow to the closed
Hamming-count plus hw=1 `M_3(C)` algebraic support. Main already carries the
honest narrowing. This PR makes that narrowed packet audit-visible by adding
16 class-A runner gates and a `runner_check_breakdown` summary.

What this can support:

- finite BZ-corner `1+3+3+1` Hamming-weight decomposition;
- hw=1 translation-character separation;
- hw=1 `M_3(C)` generation from projectors plus `C_3[111]`;
- no proper nonzero hw=1 subspace preserving both structures;
- explicit epsilon/chirality firewall.

What it does not support:

- retained status;
- physical SM-generation identification;
- BZ Hamming parity as position-space chirality/sublattice;
- any audit ledger retagging.

Files:

- `docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`
- `scripts/probe_bz_corner_decomposition.py`
- `logs/runner-cache/probe_bz_corner_decomposition.txt`

Verification:

```text
python3 scripts/probe_bz_corner_decomposition.py
python3 -m py_compile scripts/probe_bz_corner_decomposition.py
python3 scripts/cached_runner_output.py --refresh scripts/probe_bz_corner_decomposition.py
```
