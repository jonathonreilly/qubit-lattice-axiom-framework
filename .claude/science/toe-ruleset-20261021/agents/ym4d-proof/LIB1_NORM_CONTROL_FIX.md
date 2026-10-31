# LIB1: repair of the active/full norm control

**Coordinator repair; independent affected confirmation pending.** This
addresses only B1 in [the original review](REVIEW_LIB1.md). The written
conditional theorem, its bounded-hole and stronger-rate requirements, and
the remaining reference-integration/source estimates are unchanged.

The original source and evidence are preserved at commit
`f15a7ad33f90d3de8ef2f8b40cada95d009f60bd`. The original checker is also
preserved byte-for-byte in [the archival copy](checks/lib1_norm_control_original.py).
Its criteria, result, stdout, stderr and original review are not rewritten.
The original author's PRE-STATED prefix is unchanged. This note and the
small evidence clarification in LIB1 distinguish the original execution
from the subsequent repair.

## Defect and exact repair

The previous full-norm inequality became easier when its left side was
replaced with the active norm. Its separate control compared two literal
powers of two; it did not exercise that left-side computation. An actual
source substitution therefore passed every predicate while the report
still said that substitution had been rejected.

The corrected [checker](checks/lib1_check.py) factors the full-output
computation into `full_output_norm`. Both the exhaustive inequality and
the exact witnesses call this same function. The function computes the
maximum over every graph vertex with the full support weight. The unused
active-set argument is deliberately available to the actual mutation tests.

Two independently specified finite witnesses distinguish weight and root
selection:

| Witness | Exact input | Full output | Active output | Full weight, active roots only |
|---|---|---:|---:|---:|
| Four-cycle, retained vertex 0 | One singleton activity of coefficient 1, input full norm 2 | 16 | 2 | 16 |
| Path 0-1-2, retained vertices 0 and 2 | Two singleton activities of coefficient 1 | 8 | 2 | 4 |

For the first, saturation makes the support all four vertices, hence its
weight is `2^4=16`. For the second, the output supports are `{0,1}` and
`{1,2}`. At inactive vertex 1, both terms contribute `2^2`, giving 8;
either retained vertex sees only one term. These expected numbers do not
come from the checker's rooted-maximum implementation. The reported values
are now its actual computed values, checked against those expectations.

## Executions

The [new criteria](checks/lib1_norm_control_criteria.md) were frozen before
implementation and execution, after exposure to the complete original
checker and review. The [runner](checks/lib1_norm_control_run.py) executes
isolated source copies sequentially and preserves every stdout and stderr.
It keeps the original memory, load, niceness, thread and deadline gates.
The original author outputs are never destinations for these executions.

The [execution receipt](checks/lib1_norm_control_execution.json) records:

| Actual source executed | Outcome |
|---|---|
| Original checker with active norm substituted for full norm | Exit 0; still falsely reports the substitution rejected, reproducing B1 |
| Corrected complete checker | Exit 0; original enumeration plus seven new exact witness predicates pass |
| Corrected checker, both roots and weight replaced by active | Exit 1 at `exact_cycle_output_full_norm` |
| Corrected checker, only roots restricted to active | Exit 1 at `exact_inactive_root_output_full_norm` |
| Corrected checker, only weight restricted to active | Exit 1 at `exact_cycle_output_full_norm` |

All five executions reached the intended result with empty stderr. The
three rejected mutants failed the expected mathematical assertion, rather
than a syntax error, unrelated exception or resource refusal. The baseline
retains all previous exhaustive comparisons and adds the specified exact
witnesses. These are finite implementation diagnostics, not a second proof
of the graph theorem or a new Yang–Mills estimate.

The old documentation validator belongs to its original immutable artifact
set. Its hashes are not restamped to describe this changed checker. The
new repair receipt binds the corrected source and evidence separately.

## Review and scope

The coordinator read the complete original review, checker, criteria and
author log; the theorem's model/domain and norm clauses, plus its evidence
section, were read for the affected interface. This is not a full rereview
of the 721-line author theorem or of its literature proofs.

Independent affected confirmation is pending. The original HOLD remains
historical evidence against its original source. No full-norm estimate for
unbounded holes, actual source-return completion, continuum existence,
physical mass gap, formal audit or whole-PR approval follows from this fix.
