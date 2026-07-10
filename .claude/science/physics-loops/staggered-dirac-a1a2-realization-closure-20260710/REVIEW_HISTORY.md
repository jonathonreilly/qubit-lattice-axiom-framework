# Review History

## Iteration 1 — block, fixed

Reviewers found:

1. retyping the canonical parent to `no_go` was polarity-unsafe for 53 direct
   and roughly 1,025 transitive positive consumers;
2. the runner chose an arbitrary eigenvector when the neighbor sum was scalar;
3. the Record check omitted formation, site disjointness, uniqueness, and
   permanence;
4. finite quotients were overextended to infinite `Z^3` without the explicit
   quasi-local/Fourier proof;
5. the N1-N8 record did not meet the no-go-discipline schema;
6. `antiperiodic=True` meant `(-,-,-)` and was underlabelled;
7. the output log was in an ignored path.

Fixes:

- restored the canonical parent unchanged and created a separate no-go claim;
- implemented the full top eigenspace, including scalar ties;
- added a nonempty permanent record history and disjoint-site additive readout;
- replaced the basis-selecting hard-core law with the frame-invariant exchange
  interaction `I-SWAP`;
- added the infinite quasi-local model and exact Fourier symbol proof;
- narrowed the headline to the genuinely new kinetic/corner no-go;
- added the complete N1-N8 tables;
- named `(-,-,-)` holonomy explicitly and moved output to runner cache.

## Iteration 2 — block, fixed

All three reviewers accepted the four-axiom countermodel core. Remaining
findings were:

1. §5 unnecessarily enlarged the theorem to every approved primitive although
   the construction instantiates the four axioms;
2. infinite `ell^2(Z^3)` wording conflated a Bloch-symbol zero with a
   normalizable zero eigenvector;
3. the N4 witness table needed exact source line locators;
4. N6 needed exact paths, statuses, all three registered primitives, and the
   owner-governed/convention paths;
5. the load-bearing law/state Qualification text was not quoted;
6. the duplicated checklist had broken links relative to its loop directory;
7. graph-visible statistics/label links were contextual rather than
   load-bearing.

Fixes narrow §5 exactly to Lattice, Qubit, Admissibility, and Record; use
Bloch-symbol zero-set language; type the full `M_2(C)` possibility domain and
constant law map explicitly; quote the Qualification; supply N4/N6 paths,
lines, statuses, primitive scan, and N7 counter-authority; repair checklist
links; and leave statistics/label echoes as unlinked context.

## Iteration 3 — pass

Three independent reviewers passed the focused re-review:

- code/math: exact four-axiom scope, full-`M_2(C)` availability model,
  constant law map, Bloch-symbol precision, runner/cache freshness;
- physics boundary: complete current-axiom model, finite/infinite separation,
  no empirical imports, no manual-science blocker;
- no-go/governance: N1-N8, exact source locators and statuses, portable links,
  separate claim parsing, and positive-parent dependency polarity.

The canonical parent is unchanged from `origin/main`. Independent audit is
still required before the new no-go receives any effective status.

A final wording-only runner change made the `{k=0}` Bloch-symbol zero set
explicit; code/math re-review passed and confirmed the regenerated cache.

## Audit compatibility validation — pass

At source commit `1dce05887`, a detached disposable worktree passed the full
16-stage audit pipeline and `audit_lint.py --strict` with no errors. The new
row parsed as a separate `no_go`, `unaudited`, ready leaf with the intended
runner, four expected dependencies, and zero inbound edges. The disposable
generated ledger/status changes were removed with the worktree and never
entered this branch.
