# LIB1 B1 repair criteria

Written before the repair implementation and its executions. The coordinator
has read the complete original review and checker; this is an exposed,
affected repair, not a blind mathematical review of LIB1.

The original review found that replacing the computed full output norm by
the active norm survives every predicate. The original checker and receipts
at commit f15a7ad33f90d3de8ef2f8b40cada95d009f60bd remain recoverable. Preserve
an exact archival checker copy, the original criteria, outputs, source theorem,
PRE-STATED prefix and original review. Do not relax any threshold.

1. Factor the full-output computation used by the exhaustive inequality
   check into one function. The exact witnesses must invoke that same
   function, so a substitution changes both uses.
2. On the four-cycle, retain vertex 0 and saturate its singleton support.
   With coefficient one and weight 2 per support vertex, directly compute
   input full norm 2, output full norm 16 and output active norm 2.
3. Detect lost inactive roots separately: on the path 0-1-2 with retained
   vertices {0,2}, the two singleton inputs saturate to {0,1} and {1,2}.
   Each has coefficient one. The full rooted sum is 8 at inactive vertex 1;
   restricting roots to the retained vertices gives 4. The active norm is 2.
   The expectation 8 follows by adding the two independently specified
   supports, not from the implementation's maximum operation.
4. Reproduce the original active-for-full survivor on a copied source.
   Run the corrected complete baseline and actual in-memory/source-copy
   mutants: both roots and weight replaced by active, roots alone active,
   and weight alone active. Each must fail the named exact full-norm witness.
   A parser failure, resource refusal or unrelated exception is not detection.
5. Preserve the original resource gates: macOS free memory >=50%, RSS <2GB,
   all load averages <20, niceness >=10, five thread variables equal to 1,
   no pools and the existing 60-second per-program deadline. Resource refusal
   is neither a mathematical counterexample nor successful validation.
6. Use separate temporary execution directories and new repair receipt
   names; never overwrite the old author outputs. Record source hashes,
   commands, exit status, stdout/stderr and exact rejection names.

This fixes evidence discrimination only. The theorem, bounded-hole/stronger
norm-rate conditions, unresolved reference integration and full continuum
targets are unchanged. Independent affected confirmation is required before
reporting B1 resolved. No whole-PR or formal-audit disposition is assigned.
