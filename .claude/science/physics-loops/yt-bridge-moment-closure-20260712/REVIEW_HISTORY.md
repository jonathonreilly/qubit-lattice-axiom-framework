# Review History

## Pre-review checkpoint — 2026-07-12

- Selected exact current-axiom countermodel after five-route fan-out.
- Removed all fitted/observational/proxy-family inputs from the proof chain.
- Exact runner precheck: `10 PASS / 0 FAIL` (`A=8`, `B=2`).

## Review-loop iteration 1 — fix required

- Code/math: exact Pauli and moment algebra independently reproduced, but
  countermodel certification and paired artifacts were incomplete.
- Physics/import/governance: blocked the stable positive claim-ID flip because
  a negative status would falsely chain-satisfy positive consumers.
- No-go discipline: failed N1-N8 completeness and first-order scope.
- Narrow fixes applied:
  - preserved the original note/runner/cache unchanged;
  - created a distinct no-go identity and negative-route-pruning trace;
  - instantiated Admissibility, permanent records, additive readout, and an
    automorphism-covariant supplied law family;
  - narrowed every conclusion to first order;
  - added the complete N1-N8 packet, primitive scan, hostile steelman, and
    in-flight partial paths;
  - strengthened the runner and regenerated its output/cache.
- Independent check: direct time-dependent two-level evolution plus numerical
  quadrature reproduced `R_+=0.499202718338`, `R_-=0.774036826397`, and
  `R_+-R_-=-0.274834108058` with absolute errors below `1e-13`.
- Iteration 2 found two final narrow classes: fully specify the supplied-law
  meta-family and make every negative conclusion explicitly first-order.

## Review-loop iteration 3 — pass

- Code/math: `PASS`; the runner compiles and returns `13 PASS / 0 FAIL`, its
  output is byte-identical to the paired certificate, and the cache hash is
  fresh.
- Independent check: Bloch-equation finite differencing and quadrature agree
  with the exact responses to below `4e-13` and with the exact response
  difference to `2.22e-16`.
- Physics, citation chain, imports, Nature, and governance: `PASS`; the model
  meta-family is defined on density/Hermitian/real-integrable data, uses the
  time-ordered propagator, fixes the readout functional before record
  formation, and preserves the original positive claim identity unchanged.
- No-Go Discipline N1-N8 and Labeling Convention: `PASS`; all conclusions are
  first-order, the trace is negative route pruning, and the physical YT lane
  remains open.
- Audit compatibility: the validation pipeline ingested the distinct claim as
  `no_go`, `unaudited`, dependent only on `minimal_axioms`, paired it to the
  new runner, and placed it in the audit queue. Strict lint reported no
  errors. All pipeline-generated audit/effective-status files were removed
  from the science block afterward.
