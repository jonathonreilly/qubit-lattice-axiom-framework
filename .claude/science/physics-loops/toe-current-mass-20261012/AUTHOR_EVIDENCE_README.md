# Current-based mass filter evidence

Primary source: `../CURRENT_MASS_FILTER_PROBE.md`. This is author evidence
for a conditional theorem, not independent review or an audit verdict.
Its chain, scaling and full-spin GNS state are explicit supplied inputs.

The actual-current mass window converges strongly to P1 iff delta/a²
diverges (with delta→0). Smooth compact joint symbols produce actual
almost-local odd spin creators, with nonuniform locality bounds. Sharp
projections alone are not called almost-local spin elements. Even seeds
have zero one-particle vacuum columns. The exact 4m² endpoint is a null
spectral atom; leakage occurs strictly above it in the continuum-momentum GNS.

The analytic freeze is `frozen/ANALYTIC_BEFORE_CONTROLS.md`, SHA-256
`4916b1ead5abcc222cd55a1b82e249ca30642ec20639e2237c9fb1fd1b2526d1`.
The final note appends evidence and tightens two rate-summary sentences to
match the already-stated finite-ratio hypothesis. Its literal analytic delta
and final analytic version are retained. `frozen/PRE_EXECUTION_FREEZE.json`
pins the inputs, references, candidate, literal mutants, proof and protocol.
`freeze.py` is the historical preparer; use the already-frozen inputs for
reproduction.

From this directory, the recorded reproduction command is:

```sh
python3 run_batch.py
```

It verifies every pin before and after each subprocess, uses a real
60-second timeout, and records commands, complete stdout/stderr and
receipts in `logs/`. It replaces the current execution logs; preserve an
archive copy of `logs/` and `results/` before rerunning if the original
receipts must be retained. The source pins use their recorded absolute
paths. The historical `frozen/revision_1/` evidence is left intact.

The baseline exits 0; known-wrong source variants intentionally exit 1.
The batch exits 0 when those outcomes match the frozen contract.
`logs/*.stdout.json` contains all numerical rows and raw mode, matrix,
occupation, window and quadrature arrays. `results/EXECUTION_INDEX.json`
indexes receipts, and `results/MUTANT_FINDINGS.json` retains every failed,
changed and exactly unchanged row.

The original float64 kernel root failed two narrow-window loss tolerances.
Version 2 refines that reference using a 70-digit original-kernel determinant,
preserving the old float64 roots in the output and the unchanged tolerances.
The complete initial run is in `frozen/revision_1/`, authenticated by
`frozen/REVISION_HISTORY.json`. The candidate and proof were unchanged.
These are diagnostics, without interval-certified error bounds; numerical
output does not prove infinite-chain domains, locality or local-net limits.

Review clarification: item 1 of the preserved pre-execution protocol calls
the symbolic boost check an all-n identity. The implemented exact SymPy
calculation checks the two-particle specialization of M13. The general
particle-number identity is supplied by the analytic proof in section 4,
not by that finite symbolic control. The historical protocol is unchanged.

Raw external sources in `sources/external_raw/` and parent/instruction
snapshots are provenance, not proposed publication content. No editable
prompt files changed. Root owns review, repository landing and audit.


## Publication navigation

This is a live presentation of the original README with the separately accepted control-scope clarification. The historical command and paths above document the original evidence directory; do not run that overwriting batch in this packet. Use the canonical primary and root execution contract. Original files are reconstructed through [EVIDENCE_MAP.json](EVIDENCE_MAP.json).
