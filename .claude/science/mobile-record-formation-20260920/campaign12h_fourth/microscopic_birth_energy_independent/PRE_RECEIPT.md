# Independent PRE receipt

The PRE packet was completed without reading the withheld microscopic birth
energy author note/control or any forbidden comparison packet. The five
authorized scientific sources are snapshotted under sources/ and bound by
SOURCE_BINDINGS.json. Applicable instruction snapshots are under instructions/.
The inherited model and reasoning effort were retained. Same model family
and independently authored machinery do not eliminate shared reasoning risks.

The deliverable is PRE_MICROSCOPIC_STAR_RECONSTRUCTION.md. It derives the
complete 16-state physical space for every integer S>=1, the exact
factorization/spectrum and canonical dressed preparation, resolved/coherent
actual outputs and intensities, all positive integer microscopic energy
moments, the full initial GKLS derivative, the distinct bare preparation,
the zero effective Hamiltonian, and the joint resource limit. The resulting
counterexample concerns inference of microscopic energy control from density
convergence. It makes no impossibility claim about other models or reservoirs.

Reproduction command, from this directory, using a fresh attempt name:

    python3 microscopic_star_complete_matrix_check.py --attempt reproduction

The script uses only Python standard libraries, NumPy, SciPy and SymPy.
It reads the five pinned original sources to enforce their identity, imports
no other campaign Python, enumerates the full site/electric tensor basis
for S=1,2,4, and constructs every local operator directly. Source hashes
are checked at the beginning and end of the completed execution.

Run 02 completed 222 individual checks with no failed check. Of these,
the exact symbolic controls establish matrix identities; the floating
controls are corroboration and are not interval arithmetic certificates.
All 16 full 256-dimensional Liouville propagation cases are stored in
RESULTS_02.json: both instruments, epsilon=1/4,1/8,1/16,1/32,
delta=1.7, kappa=0.4, times 0.03 and 0.2. The largest observed trace
error divided by epsilon is 3.2917917432720776. The largest propagated
trace defect is 4.192515046065182e-12, the largest Hermiticity defect is
2.963823242375306e-12, and the minimum density eigenvalue is
-1.436851255696694e-13. These numerical diagnostics do not establish a
uniform bound by themselves.

The exact full initial energy derivative returned by both instruments is

    18 delta kappa / [epsilon²(1+3epsilon²)].

The exact recycling term equals this value and the loss-energy term is
zero for the dressed state; both terms were assembled and checked.
The bare initial energy derivative is zero. Resolved plus, resolved
minus and coherent marks respectively give m=2,1,3/2 in the note's
conditional moment formula.

The checks reject a wrong compensation coefficient and an omitted
epsilon^-1 jump scaling. A relative-sign mutation of a coherent channel
changes the output density but preserves its particular energy moments;
the packet explicitly records that energy-only checks would miss it.
The separate integrity verifier accepts genuine bytes and rejects an
altered expected hash, a missing file and a path outside this packet.
Those are provenance tests, not mathematical evidence.

Failure history:

1. An initial broad instruction filename inventory produced a truncated
   display. It was narrowed; no scientific content from forbidden files
   was read and the truncated listing was not used as verification.
2. The first status-file patch was rejected because an added line lacked
   its patch marker. No file was written; the patch syntax was corrected.
3. Run 01 stopped after 66 successful checks on the projector-rank
   comparison. The program compared unsimplified SymPy rational
   expressions by structural equality. Projector identities and their
   eigenvalue identities had passed. Run 02 applies simplify to the
   three traces before the same exact rank comparison. No scientific
   formula or numerical tolerance was changed. RUN_01_runner.py,
   RESULTS_01.json and both Run 01 logs preserve that complete attempt.
   Their source hash matches the failed receipt. The current runner's
   hash matches the completed Run 02 receipt.
4. A combined receipt/status patch failed because a status hunk did not
   match its exact wrapped source text. Neither file was changed by that
   failed patch. The receipt addition and status update were separated.

The full exact matrix entries, all Gauss basis words, local transitions,
marked outputs, spectrum projectors, check names and numeric values are
in RESULTS_02.json. RUN_02.stdout.log and RUN_02.stderr.log retain the
execution output. The latter is empty.

Verification limits: the matrix control is independently authored from
the withheld author's code but is a self-check of this PRE derivation.
It does not replace the root's comparison or any formal independent
audit. The all-S proof uses the tree Gauss constraint; finite S samples
alone do not supply it. The finite-time density comparison uses the
already supplied target theorem together with contractivity, and has
not re-proved that theorem on general graphs. No current-main source,
publication, audit status or other worker's files were modified.

PRE_SEAL.json binds this packet as it stood before author comparison.
After sealing, verify its artifacts with:

    python3 verify_pre_seal.py PRE_SEAL.json

The hash of PRE_SEAL.json itself is sent to the parent. Any subsequent
comparison or correction belongs in new POST files, leaving these PRE
artifacts unchanged.
