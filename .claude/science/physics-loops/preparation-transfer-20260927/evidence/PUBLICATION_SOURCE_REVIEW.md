# Publication source and portable comparator review

Read the complete new QUTRIT_PREPARATION_TRANSFER_OPEN_GATE_NOTE_2026-09-27.md and primary preparation_transfer_2026_09_27.py, provenance, implementation handoff, and affected source evidence. Reused the exact-source independent Ramsey/calibration and Echo reviews. **No necessary substantive correction found for the reviewed revision.** This is source/numerical review coverage, not an audit verdict, retained status, PR-opening decision, or full mechanical integration gate.

## Argument and empirical scope

The generator, variation-of-constants solution, degenerate limit, pure-|2> calibration, equal-population target and midpoint-swap composition are correct under the explicit nonnegative, stationary, downward-only rate assumptions. The final within12-unitary invariance is correctly a projector identity; it does not certify pulse preparation or losses. The note identifies the classical population-equation equivalence and explicitly disclaims coherence, superposition establishment, native TOE derivation, precision/statistical confidence and a general no-go. It correctly includes both Ramsey agreement and the much larger Echo mismatch rather than promoting the former as sequence-independent validation.

All acquisition identities/masks agree with prior raw-source checks: 197+3, 380+3 and 246+3 stored sample decompositions; 61/31/61 gates; 36,051 correlated calibration coordinates, 11,780 Ramsey comparisons and 15,006 Echo comparisons per curve. Reference samples are disclosed as target readout calibration, distinct from fitted dynamics. The note distinguishes physical acquisition chronology from computational prediction freezing, source-review exposure from a blind claim, and original frozen transfer from the post hoc sequential/no-decay controls. No individual observation or start is excluded to obtain a favorable result.

The source factor-of-two statement is correctly bounded: notebook T1 ODE has ordinary Gamma, T1=1/Gamma, while the Echo sqrt(2/T1) collapse operators imply population rates 2/T1. The exact notebook passes total x0 through two x0/2 intervals. This does not establish an executed clock convention or authorize doubled rates. The note preserves the lack of executed schedule evidence and does not propose a multiplier chosen from target agreement. Detailed proof and exact notebook identity remain in echo/INDEPENDENT_REVIEW.md and its source excerpts; the portable runtime does not itself verify the upstream notebook's semantics.

Every table/headline value agrees with the calibration-cost-selected saved return and independent reconstructions. In particular, Echo selected full-swap RMS/mean are 15.85125734/+14.17586972 percentage points; sequential-swap 16.25478929/+14.55342685. The displayed no-swap alternatives remain controls. Both models retain three ftol returns above gradient tolerance. The supplied Jacobian diagnostics remain descriptive, not independently regenerated statistical evidence. The note's no active bounds statement applies to the full calibration and matches the supplied record.

## Runtime, lineage and independent-check coverage

Executed the final portable primary with the existing SciPy environment, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1: exit0, `TOTAL: PASS=224 FAIL=0`. Full stdout is publication_source_runner.log; SHA256 `5e2a3df58c7a28a9e785720ec43ad097f2ee71ac20a570b19115d231f76881e8`, identical to the implementation handoff. I did not rerun historical nonlinear optimizers or repeat the writer's mutation runs.

Independently compared all three packaged raw_IQ, stored time and gate arrays against the reviewed external exports: exact elementwise equality throughout. Every provenance upstream hash matched the current external source. All 34 packaged data files and the imported helper are exactly covered by the 35 literal AUDIT_INPUT_PATHS entries. The primary reads only repository-local data and the helper; NumPy/SciPy are software dependencies. It has no network/HDF5/optimizer dependency or external absolute-path runtime read. The primary pins provenance and checks all file bytes. Original freeze receipts/historical scripts are inert lineage evidence and are not falsely re-executed as a fresh prospective experiment. The final primary reproduces all supplied calibration objectives, all six Ramsey/control returns and all twelve Echo curves, retaining optimizer statuses and observed failures.

I authored the independent helper earlier in this session; it uses SI-second matrix exponentials and augmented affine QR, separately from the primary closed forms and direct solve. Accordingly this report is not an additional independent review of my own helper. Its load-bearing algorithms were previously crosschecked against exact raw source, closed forms and elementary cases; the coordinator retains responsibility for final paired-source review. The helper supplies arithmetic under assumptions, not new experimental authority. The runner's checks compare implementations and archived values, not a threshold declaring empirical agreement. No missing runtime closure was found.

## Exact reviewed identities

- Note: `48cd3a07d6152a76659bc7439d0441bf9d6d6044ee78c8a16e6cbe719b48d647`
- Primary: `436445c0a6e7b7cc0980e90e8b3339abf252732ee070b8850ffab7aecaf31616`
- Independent helper: `bce339d01716f2b66f28033fda48f8e301279cafffe6efaf79763b40888e5aa8`
- Provenance: `2775422eac8bf64bddb794e005c089bd456da17c64b103f353b021709eefbb0c`

PUBLICATION_SOURCE_IDENTITIES.json preserves all 37 note/script/data hashes, exact-array comparisons, input-count closure and stdout identity. No author note, primary, data, pack, scientific authority or audit surface was edited during this review. Later source changes require a scoped refresh rather than treating this review as blanket coverage.
