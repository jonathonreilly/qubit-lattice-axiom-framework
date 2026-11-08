# Native placement milestone

The explicit five-state SU(2) model admits a geometric four-qubit link code
on length-five coarse edges. The code is orthogonal to the all-zero four-bit
vector. That property makes all 125 translated grid origins orthogonal and
locally distinguishable, without an external phase register. Their direct
sum is invariant under every native translation and proper cubic rotation.
A local detector on 24 qubits supplies an exact finite-range extension of a
supplied cubic electric/plaquette Hamiltonian. Each phase carries one full
copy of the gauge model, preserving all boundary flux and multiplicities.

This is a chosen code with an extra encoding-origin degree of freedom. It
uses 12 active qubits and 113 fixed spectators per coarse cell. Neither an
origin-free single-copy encoding nor a native nearest-neighbor probability/
record law has been proved. No axiom or physical framework is being protected
from falsification: ordinary equal-site-count encoding fails the explicit
finite dimension tests, while coarse coding succeeds. Both the framework
and the gauge model remain physical hypotheses.

## Sources, branch and recovery

Main: f5af11cd0102cfd0b51aef0911f600130bf5beb1.
Instruction ref: 56c5c0ab64f532c5784e895b2f9aa6894fa334e0.
Research parent: 17f68f575f3de7c1a24a4761e01c8307a9e99955.
Branch: physics-loop/gb1-cf-pair-20261107; PR #10142 remains ready.
The existing root STATE.yaml is the current checkpoint. The earlier pair
and boundary proofs, source identities and execution receipts are unchanged.
Exact new source hashes are in outputs/source_hashes.json.

The complete source is
docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md.
The linked scope stress test keeps the two finite capacity witnesses separate
from any general no-go, with no negative-packet PASS claimed. Author status
is a conditional bounded theorem proposed for review; formal landing and
audit remain pending. No authority or registry changes are made.

## Independent paths and decisive evidence

SUPERVISOR_CANDIDATE.md was frozen before reading the independent result.
It constructs the spacing-five all-origin code and local projectors.
INDEPENDENT_PLACEMENT.md was independently derived with only the raw model
and current axiom/registry sources. It proves the capacity bounds and builds
a different spacing-nine construction with separate local markers and 729
orthogonal phases. It also gives an explicit failure of naive coherent
phase averaging and distinguishes exact reversal from projective reversal.
Those findings agree with the scope of the chosen code, whose four-qubit
size is sufficient and not claimed optimal. The supervisor read the complete
independent proof. Same-family separate-context provenance is disclosed; no
cross-provider independence or formal review status is claimed.

The checker read the complete final note, scope sidecar, exact runner source
and normal-run canonical cache. NATIVE_SOURCE_REVIEW.md independently verifies
the spacing-five phase separation, local detector, geometric action, corner
algebra and Hamiltonian identity. Its sole scope finding was corrected:
regional Gauss gluing is realized on the fixed coarse graph; subdivision
requires separately allocated source/target encodings. The sidecar was also
labelled meta, with no scientific grade. NATIVE_CLARIFICATION_REVIEW.md confirms
these exact changes and unchanged proof coverage. Both receipts are copied
unchanged. Separate mutation execution and literature/prior-work statements
remain supervisor verification, not reviewer-certified evidence.

The two-source clarification patch is preserved in
outputs/source_clarification.patch. Applying it in reverse with
`git apply --unidiff-zero -R` to copies of the final files recovers the two
completely reviewed original hashes. Both supervisor and checker verified
that recovery. No runner mathematics changed after execution.

The primary runner executed under a successful numeric preflight, unique
lease, nice priority, single math threads, 60-second wall/CPU bounds and a
270 MB RSS monitor. The baseline took 0.008235 seconds with 24,920,064 peak
RSS bytes. It checked all 625 matrix-unit products, all phase differences,
all proper rotations, disjoint allocation on a 15-cubed torus, phase-detector
supports and graph incidence ranks. It never constructed a 3375-qubit matrix.
The exact phase-separation witness list is preserved in stdout.

Three separately invoked faulty candidates exited 1 at the intended check:
reversal parity, nonzero overlap with the all-zero vector, and a preferred
grid origin. The full baseline and mutation stdout/stderr are in
outputs/execution.json. The numeric lease release is recorded in
outputs/lease_release.txt. The content-bound canonical cache is
logs/runner-cache/gb1_cf_native_placement_exact_2026_11_08.txt.
The large-state and infinite-volume assertions are mathematical proofs,
not claims of dense numerical testing. Full pipeline checks remain a landing
obligation, not an author research test or an audit substitute.

## Next scientific decision

Test whether a single covariant nearest-neighbor probability/record law can
realize the encoded observables and preparation, including its origin sectors.
An externally timed gate compiler or averaging a finite-range Hamiltonian
does not establish that law. If the law fails, compare a different code,
restricted emergent sector, gauge model, joint composition, or local site
content. The finite dimension witness does not choose between those physical
alternatives. No vacuum, mass gap or continuum closure follows.

Editable task prompt: native_placement/INDEPENDENT_SPEC.md was created; the
existing GOAL.md task contract was extended with the new target and the
user's instruction to test the framework itself. No existing shared prompt,
axiom file, or platform-supplied instruction was modified.
