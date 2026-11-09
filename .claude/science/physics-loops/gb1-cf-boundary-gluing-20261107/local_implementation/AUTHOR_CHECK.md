# Supervisor proof and evidence check

The supervisor read all 271 lines of INDEPENDENT.md, including its separate
source-exposed section, and the complete primary/final argument and diagnostic
source. The independent derivation did not import the supervisor's new script.
Both use the same underlying source code/quantum premises and model family;
this is a research check, not audit independence or retained status.

Load-bearing hand checks:

1. W maps J0 to 0100 with positive phase. Conjugating the all-ones projector
   by W followed by X_1 X_3 X_4 gives the full native rank-one projector.
   The AND-copy-inverse word has two Kraus branches P and I-P with no erased
   environment. Tensoring the proof gives the passive-reference identity.
2. r=4m controls need r-1 clean AND bits in the primary construction. Each
   compute/uncompute Toffoli has five pair gates. Together with decode/encode
   this yields 48m-9 pairs and 8m onsite gates, before routing.
3. A path avoiding all V_p has no old record inside it. Returned SWAP
   conjugation acts on only its two logical operands regardless of spectator
   entanglement. Old vertices are read solely as CNOT controls after moving
   a work operand beside them; their own carriers never move or change.
4. f_j b_j is unchanged when only an unfinished pointer with f_j=0 changes.
   Thus the inverse masked-copy unitary clears work even on coherent output
   branches. Using an unmasked copy would leave the new output in workspace.
5. Header/history equality and the prefix boundary f_k=1,f_(k+1)=0 select one
   clause. At completed stage N there is none. In the herald-first version
   excluding h_1=0 clauses implements the stated failed-herald halt.
6. Simultaneous controller and herald work use different F_p banks. Their
   sum 12n^3+3M fits the existing 112n^3 sites. Added completion records cost
   N vertices, with 7+d+2N<n under n>=2M+8. Their row cannot merge with the marker.
7. A controlled SWAP uses two CNOTs and one Toffoli (seven pairs); controlled
   CV needs the explicit fourth-root pair gate. This explains 344m-63 pairs
   for the controlled herald and the finite total-controller bound.

Corrections from checker feedback are retained in PRIMARY.md and incorporated
in RESULT.md: disjoint simultaneous work, failed-herald guard, and paths tied
to a rather than a residue representative. SOURCE_CHECK.md separately records
the worker's final source comparison; it is not a new independent derivation.

Diagnostic computation is exact Gaussian-rational small-register arithmetic
with unnormalized Hadamards (the known 2^m scale is included in the target).
Full native basis columns test operator equality, not merely selected input
probabilities. Boolean permutations check cleanup and compiled predicates;
wire-label permutations check routing. These checks do not simulate the full
finite torus, the controlled reader's complete multiplexer or physical formation.
General proofs carry those scoped circuit claims. No claim of efficiency,
noise robustness or a physical duration follows from the gate counts.

Faults removing uncompute and removing the mask fail mathematical comparisons,
not a metadata gate. First and final receipts are preserved separately. The
second run adds predicate/routing coverage to the initial successful source;
the final run replaces torus routes with non-wrapping box routes and tests
ordinary Z3 adjacency. Earlier executed sources and streams are retained with
their matching hashes. Two sequential numeric leases were held for the
serialized runs and released after completion. Limits were
CPU60/wall60 monitored plus outer timeout65, RSS270 MB, nice10, five library
thread variables pinned to one. verification.json binds the final source/logs.

Negative findings are explicit contract counterexamples. Possible alternatives
(presence interface, recorded selector, environment, parallel/local clock,
different code) remain live; no exhaustive no-go packet is asserted. Supplied
gate calibration, clean seed/work, suspension of unwanted H, registered Born
output and the sequencer remain named physical dependencies. Temporary F_p
borrowing changes an implementation condition, not a governing physical axiom.

Only the lane GOAL.md prompt changed. No shared prompt, skill, AGENTS.md,
axiom, primitive registry, audit ledger or platform instruction was edited.

After the source check, the supervisor reflowed one routing line and clarified
that a failed herald still receives its completion append before halting.
This makes the already stated two-append macrostep/guard order explicit; no
gate, resource bound or domain was broadened. The checked and final RESULT
hashes are both recorded in verification.json.

A final, separately checked improvement routes every pair monotonically
inside the marker-anchored finite Z3 box. ROUTING_ADDENDUM.md proves this
restriction preserves connectivity and the old resource bound, including
all reader pairs whose gauge labels cross a seam. The final diagnostics
add an ordinary Manhattan-adjacency assertion; no periodic gate shortcuts
are allowed. This supplies a finite circuit embedding, not an infinite or
continuum gauge construction. Other source arguments remain unchanged.
