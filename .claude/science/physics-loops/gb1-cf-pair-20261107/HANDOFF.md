# GB1-CF: finite two-plaquette milestone

The specified five-state SU(2) link model works as a coupled finite patch.
With no external links or charges and Gauss law at all six vertices, the
physical sector has exactly four states: empty flux, the left loop, the right
loop and the outer loop. In the Wilson-trace basis,

`[B_L,B_R] = 3 (|L><R| - |R><L|)`.

The joint update `exp[-i theta(B_L+B_R)]`, also followed by the uniform
electric layer, is exactly gauge invariant and square-exchange invariant for
every real step angle. Ordered and left-centered Strang words have explicit
exchange defects at second and third order. These witnesses do not exclude
other schedules. The closed-patch sector has an exact two-logical-qubit
description; the full seven-link model embeds in 21 qubits on its initialized
code subspace. No axiom was changed.

This is a conditional finite-model theorem proposed for review. Full GB1-CF
is open: the supplied group, boundary sector and dynamics have not been
selected or implemented by the native lattice axioms. Global spatial code
allocation, compatible overlapping updates, translation/proper-cubic
covariance, the Admissibility/Record clauses, state selection and continuum
identification remain open. There is no vacuum or mass-gap result.

## Sources and recovery

Working branch: `physics-loop/gb1-cf-pair-20261107`.
Milestone: [PR #10142](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/10142), now ready for review at the user's request.
Scientific source commit: `2fed163ac02350f31d8af53f38ee5feaf15b7e09`.
Base and refreshed main: `f5af11cd0102cfd0b51aef0911f600130bf5beb1`.
Instruction branch read: `56c5c0ab64f532c5784e895b2f9aa6894fa334e0`.
Assembly context: PR #10139 at
`fb9508e8390bf66da8f29ddb44611d2a531768cb`; no runtime dependency on that draft.

Primary worktree: `/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics`.
The separate checker worktree's needed deliverables are copied here. Frozen
original runners and complete original logs are preserved in `outputs/`.
PRIMARY.md and CHECKER.md describe those original executions, not the later
canonical cache paths after integration. Their original hashes remain valid.

The checkpoint for this completed pair calculation is STATE.yaml. Continuing
boundary-flux work is tracked in `../gb1-cf-boundary-gluing-20261107/STATE.yaml`.
The complete public-facing mathematical argument is
`docs/SU2_FIVE_STATE_TWO_PLAQUETTE_GAUGE_SECTOR_BOUNDED_THEOREM_NOTE_2026-11-07.md`.

| Current source | SHA-256 |
|---|---|
| Theorem note | `6fe2122dbe905547319f9347e45fcc122ecc07ba6bc5e7c3ad7f626dd6d7b43f` |
| Primary production runner | `98e5dabbe9a6915309c0e10d5a83ed6d71995ab8567254f413bc05a81a09f2b2` |
| Haar production checker | `5f099d6156bee8e17bae73ff48130b9fd3738fab317cbb640f2e4bb9086f8d13` |
| Final focused note review | `5c1357c7fefdbbf8e873761c1eb4892e9221ade5ba75892ccf0577bd2c24a3f0` |

The focused review examined note hash `268835ffc74a72e29890f1291a65611caa9c0af5a9efa66da330eab12e814305`.
The delivered note differs only by removal of two trailing Markdown spaces
on the Type line, required by the diff check; no wording or formula changed.

Original primary runner hash:
`3f2e47d0b2d5737d1dfa4c2586586f860d18556ece82197ea9ca1ecaa12c4e30`.
Original checker runner hash:
`daa78235e9f850c486eba543cde39df04240ec6095f3db1998931874e80dfa66`.
The exact frozen sources are `outputs/*.frozen.py.txt`; raw preflight, lease
and execution logs are `outputs/*.raw.txt`. These provide a recovery path for
the separately authored calculations before the integration comparison.

## Verification actually performed

The sparse action and Haar derivations were completed in separate contexts
before result exposure. The supervisor read both full implementations,
derivations and original logs, reconciled ordered-product conventions, and
compared their exact matrices. The focused checker reviewed the complete
theorem note, independently checked its joint-gate identity and both encodings,
then checked the requested wording amendments at its recorded source hash.
The same model family and shared raw premises limit independence; this is
neither a different-provider check nor a formal landing review/audit.

Canonical output was generated through
`runner_cache.execute_and_write_cache` with declared timeouts 80 and 85 seconds:

- `logs/runner-cache/gb1_cf_two_plaquette_s1_2026_11_07.txt`;
- `logs/runner-cache/gb1_cf_two_plaquette_haar_check_2026_11_07.txt`.

Both executions exited zero and their source-bound cache identities were fresh.
The primary used 1.02 seconds measured internally and 29,704,192 peak RSS bytes;
the Haar checker used 0.060837 seconds and 25,706,496 bytes. All mathematical
coefficients used exact rational arithmetic. The final checker recorded 19
software/consistency checks, including two rejected coefficient mutations and
one missing-term tamper. Counts are execution diagnostics, not proof authority.
Scientific outputs were unchanged from the frozen original executions; the
primary additionally emits the later cross-implementation comparison.

Seven production-source scratch mutations were separately rejected by
scientific assertions, with full stdout and traceback evidence in
`outputs/integration_execution.txt`:

| Mutated calculation | Detecting check |
|---|---|
| Coordinate coefficient 1/2 to 1 | Exact local commutator identity |
| Outgoing endpoint action replaced by incoming action | All-vertex Gauss action on loop basis |
| Trace-plus-adjoint factor 2 to 1 | Full sparse commutator witness versus reduced action |
| Omitted horizontal link inversions | Exact geometric action on loop basis |
| Strang half-step replaced by full step | Lower-order exchange coefficients |
| Altered logical magnetic coefficient | Pauli expression versus sparse matrix |
| Electric Casimir coefficient 3/4 to 1 | Logical electric polynomial versus counted flux energy |

The mutation driver is `outputs/run_integration_checks.py`. Its scratch files
were removed and both production source hashes were unchanged afterward.
Preflight succeeded and the numeric lease was released. The original
checker also rejects the shared-link dimension-factor error directly from
Haar integration, independently of the primary sparse action.

The primary statically imports the Haar checker and declares it in
AUDIT_INPUT_PATHS. The repository helper extractor returned that exact path;
no helper-policy mapping or authority edit was needed. Neither production
runner reads a mutable workflow/spec file or an unmerged draft.

Focused syntax, vocabulary, relative-link, cache-identity and diff checks are
recorded in `outputs/verification.json`. A full pipeline and formal landing
review/audit have not been run; those remain integrated landing obligations.

## Next scientific decision

Extend the patch while retaining boundary flux sectors, then seek one local
encoding and overlap-compatible update schedule with the required spatial
symmetries. The isolated patch's two-logical-qubit compression cannot simply
be assumed to tile the lattice: adjacent patches share links, and the present
zero-external-charge sector is a boundary assumption. The strongest missing
lemma is the native spatially covariant overlapping construction at fixed
register size. Existing Admissibility and Record clauses must then be checked
for the resulting law; this milestone does not establish their compatibility.
