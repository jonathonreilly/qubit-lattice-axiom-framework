# Review History

## Initial local science checks

- Fresh branch created from `origin/main@9b36439830`.
- `python3 -m py_compile scripts/frontier_rhalf_open_backlog_probes_2026_07_13.py`
  passed.
- Exact runner returned
  `SUMMARY: RHALF OPEN BACKLOG PROBES PASS=57 FAIL=0`.
- No-go discipline applied to all seven construction-specific negative
  boundaries.  The shipped boundaries pass N1--N8; a general Krein or
  route-family no-go was rejected and remains outside the claim.
- Audit-owned data and status surfaces were not edited.

## Review iteration 1

The parallel reviewer fanout produced fifteen consolidated actionable
boundary/code/governance findings.  All were fixed:

- coupled the record pointer to the write isometry through
  `V^dagger(M_R tensor I)V=W^2` and computed support from `rho=I/3`;
- made Hermitian/real spectrum load-bearing and added the `i^2=-1` control;
- separated formation-weight `F` from transfer-matrix `G` and used distinct
  transport-equivalent condition tuples;
- narrowed K supply to a candidate object, keeping event-atom licensing open;
- separated algebraic `ND3`, probability support, and realized occurrence;
- narrowed the seam, commuting-scalar, and quadratic-factor wording;
- repaired premise classes, trace/certificate schemas, and dependency edges;
- applied N1--N8 to all seven shipped construction-specific negative
  boundaries and rejected every broader route-family no-go.

## Review iteration 2

- Code / runner: `PASS`.
- Physics claim boundary: `PASS WITH BOUNDED CLAIMS`.
- Imports / support: `DISCLOSED`; no observations, fits, or hidden measured
  values.
- Nature retention: `BOUNDED` exact algebraic support; physical `r=1/2`
  selection remains `OPEN`.
- No-go discipline: `PASS` for shipped scoped boundaries; the rejected broad
  Krein no-go remains outside the claim.
- Labeling convention: `PASS`, no split required.
- Repo governance: `PASS`.
- Audit compatibility: `PASS`; independent audit remains required.

## Independent math checks

- Enumerated all two-state histories independently of the matrix formula and
  recovered the quenched/annealed Markov endpoints.
- Enumerated `C_n/K` orbits through `n=32` and recovered the odd/even closed
  counts.
- Checked nested-record set inclusion across line edges and failure across the
  seam.
- Checked the Krein positive-half condition by direct component action on
  `(u,u)`, independently of the runner's block multiplication.
- Recomputed the quadratic-factor witness and sign ambiguity directly.
- Recomputed the distinct condition/canonicalization and separate `F,G`
  codomains independently.

## Audit compatibility validation

- `bash docs/audit/scripts/run_pipeline.sh` seeded
  `r_half_open_backlog_formation_law_probe_batch_exact_support_note_2026-07-13`
  as `bounded_theorem`, `unaudited`, with the paired runner and nine intended
  markdown dependencies.
- `python3 docs/audit/scripts/audit_lint.py --strict` returned zero errors.
- Pipeline-generated audit, queue, publication-effective-status, and
  front-door outputs were restored to `origin/main` and are absent from this
  branch.

Final review-loop recommendation: `PASS WITH BOUNDED CLAIMS`.
