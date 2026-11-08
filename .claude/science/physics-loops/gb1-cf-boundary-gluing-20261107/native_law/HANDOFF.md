# Neighborhood propagation and electric-record milestone

The five-state link admits an exact electric-value measurement by a finite
sequence of adjacent operations: 19 two-site gates, seven onsite gates and
one fresh output instrument. The active code is restored, its occupied-sector
coherence is preserved, and the completed instrument commutes with both
endpoint gauge actions. It therefore extends to the glued finite gauge
patches by identity on other links, including entangled inputs.

The original fixed-spectator global code must expand to admit the output
record. This is an actual encoding change on the same native qubits.
There is no infinite supply/reuse theorem and no autonomous all-origin
formation law. Tensor quantum states, controls, coherent preparation,
a driven schedule, Born readout and future freezing of the output are explicit
conditions. No physical axiom is inferred or adopted from the circuit.
A separate copy law supplies a genuine permanent-record relay along arbitrary
finite paths, with formation order stated as a condition.

## Source identity and recovery

Main: f5af11cd0102cfd0b51aef0911f600130bf5beb1.
Research parent: febb4c812b1d38e9b33f2c97149ff2b8f0f363ea.
Branch: physics-loop/gb1-cf-pair-20261107, existing ready PR #10142.
The new proof is docs/SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_BOUNDED_THEOREM_NOTE_2026-11-08.md.
Its scope sidecar and exact runner/cache are linked there. Exact hashes are
in outputs/source_hashes.json. Earlier pair, boundary and native-placement
proofs and source receipts are unchanged.

SUPERVISOR_CANDIDATE.md freezes a phase-sensitive two-state experiment and
a different full-code electric measurement with two returned work qubits.
The fresh-context worker derived a controlled-reversal readout, then the
simpler full-code electric predicate using no work qubits. Its complete
INDEPENDENT_PROPAGATION.md and ELECTRIC_READOUT_CHECK.md are copied unchanged.
The supervisor read and hand-checked both full arguments, including the
different off-code extensions. Exact simulation uses its own
Gaussian-rational sparse vectors, not the worker's code (there was none).
Shared raw model and model family remain limits on independence.

## Execution

The new runner completed under successful numeric preflight, a unique
machine lease, nice priority, single math threads, a 60-second CPU/wall
guard and a 270 MB RSS monitor. The final baseline took 0.053744 seconds
with 24,920,064 peak RSS bytes. The content-bound cache is fresh.
All code columns, both pointer inputs, the full clean-work input basis of
the alternate circuit and full basis of the controlled-reversal circuit
were checked exactly. The relay was tested on all binary six-neighbor
contents, all 24 proper rotations and straight lengths through 32;
arbitrary distance follows from induction, not finite enumeration.

Four separately invoked mutations exit 1 at the intended mathematical
property: dropped routing return, wrong square root, record-first phase
loss, and omitted electric uncomputation. Full stdout/stderr are in
outputs/mutations.json. Initial development execution is retained separately;
it preceded the compact electric circuit. The numeric lease was released.

The first cache-identity query mistakenly passed the cache filename rather
than the runner filename, yielding sha_mismatch. Repeating the documented
API with the runner path returned fresh and no evidence issue. No cache
header was edited and no rerun was used to hide that caller error.

FINAL_SOURCE_CHECK.md confirms the complete source, scope, runner and cache
at the frozen identities. It separately derives the two-work routing counts,
checks both electric extensions, and verifies the relay/permanence scope.
The checker authored the compact circuit, so this is research source checking,
not formal fresh review. Its exact receipt hash is in outputs/verification.json.
Full pipeline/landing checks remain pending; no audit data or authority
surface is modified.

After that check, whitespace validation required deleting exactly one trailing
blank line from the source note, scope sidecar and runner. The byte-recovery
certificate outputs/eof_normalization.json records old/new hashes: appending
one LF recovers each complete reviewed source. No argument or code changed.
The cache and all four mutations were rerun on the normalized bytes under
a new numeric lease, then released. Mathematical stdout certificates match
the preserved pre-EOF cache exactly; outputs/final_execution.json records
the final execution. The unchanged source-check receipt remains historical
evidence for the recovered bytes, not a claim that it read the later cache.

## Axiom wording and next decision

The user requires approval of exact old/new wording before opening a separate
axiom-only PR. The current proposal changes just the two governing
Admissibility occurrences of nearest-neighbor to neighborhood. It is recorded
in AXIOM_WORDING_PENDING.md, with an untouched isolated worktree prepared for
that future PR. No approval has yet been received; no axiom PR is opened.
Current science continues under the unchanged source hashes.

The next physics target is one explicit homogeneous joint data/record law
with prepared-code provenance, fresh-output allocation and magnetic
plaquette evolution. The conditional readout closes a finite communication
and observable-interface step, not that whole law or a mass gap.

Editable task prompts changed: root GOAL.md was extended;
native_law/INDEPENDENT_SPEC.md was created. Follow-up worker assignments were
bounded tool messages. No shared skill, axiom, registry, or platform prompt
was edited in this research branch.
