# Review History

## Iteration 1 — independence correction

The reviewer lenses were run sequentially in the root worker because this task
did not authorize subagent delegation.

The initial plain-integer path independently recomputed the determinantal
divisors and all support masks, but its global gauge check reused the same
explicit gauge formulas as the SymPy route. That was not independent enough
for the auditor's requested recheck. The implementation was changed to select
the displayed unit `5×5` minor, invert it by its integer adjugate, and derive a
different gauge section algorithmically. Plain multiplication then verifies
`I+MG=e_6 w^T` and `w^T M=0` without importing the symbolic gauge formulas.

Finding: 1. Fixed: 1.

## Iteration 2 — mechanism-distinct no-go route

The disconnected-forest attack initially reused the rational-rank mechanism,
so it did not count as an independent N1 route. The runner now implements a
direct orbit construction: peel each forest to one root per component, then
reverse the order and assign integer vertex phases that cancel zero and every
edge-phase basis vector. This covers every phase by linearity, works globally
modulo `2*pi`, and leaves a cyclic core only for the full six-edge mask.

Finding: 1. Fixed: 1.

## Iteration 3 — local review-loop

- Code / Runner: **PASS**. The primary SymPy route, plain-integer route,
  cache pin, CLI failure probe, and exact output summary agree.
- Physics Claim Boundary: **candidate retained-grade at the exact supplied
  formal scope**. No charged-lepton, Yukawa, Higgs, gauge, branch, PMNS,
  observable, or empirical conclusion was added.
- Proof Obligations: **CLOSED for re-audit**. Rank and Smith factors, a global
  torus section, and all `64` support masks now have separate exact checks.
- Imports / Support: **CLEAN**. The theorem uses only its displayed finite data
  and standard exact integer algebra; there are no open imports.
- Nature Retention: **RETAINED-grade candidate at the stated formal scope**.
  This is not an audit verdict and does not change the applied ledger state.
- No-Go Discipline: **PASS** for the narrow proper-support boundary; N1–N8 are
  recorded in `CLAIM_STATUS_CERTIFICATE.md`.
- Labeling Convention: **NOT APPLICABLE**. Labels name explicit mathematical
  objects and are not physical premises.
- Repo Governance: **PASS**. Generated ledger, publication, and front-door
  files created during validation were removed from the patch.
- Audit Compatibility: **PASS**. The full pipeline completed, seeded exactly
  this changed row as `positive_theorem / unaudited / ready=true`, and strict
  audit lint exited zero. No audit worker or verdict application was run.

## Validation evidence

- Direct runner: `PASS=60 FAIL=0`.
- Intentional-failure probe: exit `1`, `PASS=60 FAIL=1`.
- Independent external reconstruction: rational Gaussian elimination and a
  separately implemented leaf-peeling algorithm recovered support ranks
  `(0,1,2,3,4,5,5)` and removed every edge-phase basis vector on all `63`
  proper masks.
- Cache: fresh, exit `0`, complete stdout, pinned to runner SHA-256
  `c75da032ddc002833b1357f7b53a66005085cf04488de29b78459ddb5f2727f0`.
- Python compilation, vocabulary lint, strict audit lint, the repository audit
  pipeline, and `git diff --check`: pass.

Final local disposition: **pass for independent re-audit**. The existing
`audited_conditional` verdict remains authoritative until that audit occurs.
