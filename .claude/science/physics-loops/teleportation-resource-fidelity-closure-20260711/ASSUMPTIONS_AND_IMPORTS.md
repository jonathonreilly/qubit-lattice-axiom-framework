# Assumptions and imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Supplied physical two-qubit density matrix `rho_RB` | Defines the theorem domain | admitted normalization/boundary condition | Source-note scope | yes | yes, for this scoped theorem | not applicable; keep as an explicit hypothesis | not a native preparation claim |
| Ideal Bell projective measurement and complete two-bit record | Defines the fixed protocol | admitted normalization/boundary condition | Source-note harness | yes | yes | not applicable; keep as an explicit hypothesis | no nonideal apparatus claim |
| Fixed correction `Z^z X^x` | Fixes the Bell/Pauli frame | admitted normalization/boundary condition | Note and runner | yes | yes | not applicable; keep as an explicit hypothesis | disclosed convention; no optimization claim |
| Finite-dimensional density-matrix, Born-rule, and partial-trace machinery | Defines and evaluates the protocol channel | standard/literature correction | Inline note and runner implementation | yes | yes | elementary tensor-algebra expansion | all load-bearing operations are explicit |
| Qubit Bloch representation and rotationally invariant Haar measure | Converts the exact Pauli channel to average fidelity | zero-input structural | Source-note direct derivation | yes | yes | completed inline from `|r|=1` and equal sphere moments | inline mathematical identity; not an `A_min` claim |
| Floating-point matrix arithmetic | Replays the complete operator-basis identity and physical controls | support-only | Paired runner and cache | no | yes, as verification | independent re-audit | exhaustive linear-basis corroboration, not a premise for theorem truth |
| General Choi/entanglement-fidelity average relation | Compact cross-check of the direct Bloch average | literature theorem | Explicitly non-load-bearing shortcut in note | no | no | direct Bloch derivation already retires it | cross-check only |
| Classical measure-and-prepare optimum `2/3` | Comparator defining “beats classical” | zero-input structural | Source-note Haar second-moment derivation | yes, for threshold wording only | yes | completed inline | inline mathematical theorem; scoped to Haar-uniform pure qubits with no shared entanglement |
| Negativity, Horodecki CHSH, isotropic, and amplitude-damping diagnostics | Contextual resource characterization | standard/literature correction | Runner diagnostics | no | no | none required | support-only; excluded from theorem proof |
| Seeded random resources, Pauli-axis probes, trial count, and tolerance | Numerical stress-test choices | insensitive nuisance | Reproduction command | no | no | exact operator-basis gate removes sampling dependence | support-only controls |

No observed value, fitted selector, resource-preparation output, literature
number, unit identification, or broader teleportation claim is consumed as a
proof premise.

## Counterfactual sensitivity

| Changed premise or diagnostic | Effect on the scoped result |
|---|---|
| Require `rho_RB` to be produced by native preparation dynamics rather than supplied | The conditional channel identity is unchanged, but preparation becomes a separate open bridge; this theorem does not close it. |
| Nonideal or incomplete Bell measurement/record | The Bell-character cancellation need not hold; theorem no longer applies. |
| Different fixed Pauli frame | The same proof holds with the identity-error Bell label relabeled; `Phi+` is convention-specific. |
| Non-Haar input ensemble | The exact Pauli channel remains, but the three squared Bloch moments need not equal `1/3`. |
| Shared entanglement allowed to the classical comparator | The measure-and-prepare `2/3` bound is no longer the relevant comparator. |
| Remove CHSH, negativity, damping, random probes, or tolerances | No effect on the theorem; only contextual or stress-test output is lost. |
| Remove the exact operator-basis gate | The analytic proof remains, but executable corroboration of arbitrary Bell coherences is weakened. |
