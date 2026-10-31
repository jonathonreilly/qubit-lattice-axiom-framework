# LIB1 B1 version-2 criteria — before implementation and execution

[R-fix 2026-10-29 B1]

This is the narrow author repair requested by `REVIEW_LIB1.md`, binding
finding B1. The frozen `lib1_criteria.md`, `lib1_check.py` and their outputs
stay unchanged. The written theorem and the immutable PRE-STATED prefix
stay unchanged. The v1 run and the review's mutation outcomes are already
known; these are repair acceptance criteria, not an unexposed experiment.
The v1 criteria 1–5 remain in force. This file replaces the B1 portion of
criterion 6 for the new script and qualifies the other three static
wrong-output comparisons as contrasts, not new implementation-mutation runs.

## Shared computation and independently derived exact values

Factor one `full_output_norm(grouped, out_labels, allv, lam)` function and
call it both in the bounded-hole inequality and in the following witnesses.
It must use every graph vertex as a root and every output-support vertex
in the exponential weight. All arithmetic is exact, with μ=log 2 and unit
positive activity coefficients. Expected values below come from the norm
definition and explicit supports, independently of that function or its
generic `norm` routine. Record computed values before asserting them.

1. Four-cycle 0–1–2–3–0, Λ={0}, Ω=Γ, one input support {0}.
   Saturation adds the connected inactive set {1,2,3}, giving Γ.
   The input full norm is 1·2^1=2. Each of the four full output root sums
   is 1·2^4=16. The output active norm has its sole root 0 and only one
   active support vertex, hence 1·2^1=2. Assert computed input full=2,
   output full=16, and output active=2; assert the full value first among
   the output values. A literal comparison 16≠2 without invoking the
   shared computation does not satisfy this criterion.
2. Three-vertex path 0–1–2, Λ={0,2}, Ω=Γ, unit input supports {0} and {2}.
   Saturation gives distinct outputs {0,1} and {1,2}. Each full support
   contributes 2^2=4, so the full rooted sums at 0,1,2 are (4,8,4).
   Only the inactive root 1 attains 8. The input full norm is 2 and the
   output active norm is 2. Assert shared computed output full=8 and the
   other two computed norms=2. This must reject a full weight with roots
   restricted to Λ, which would return 4. It also covers the separately
   parameterized root mask in the generic norm routine.

## One sequential invocation, baseline and actual mutations

Run `checks/lib1_check_v2.py` once. It executes the unchanged finite graph
suite plus the new witnesses once as baseline. Then compile two distinct
in-memory copies of that exact v2 source, with exactly one substitution in
the shared full-output function in each copy, and invoke each copy's
`main()` once. Do not modify expected constants, assertions, generic norm,
inequality call sites, resource gates, or any frozen file in those copies.

| Trial | Sole substituted return expression | Required outcome |
|---|---|---|
| Baseline | `norm(grouped, out_labels, allv, allv, 1)` | Every finite predicate and exact witness passes. |
| Active for full | `norm(grouped, out_labels, lam, lam, 1)` | `AssertionError` at `four_cycle_full_output_norm_exact`; record computed 2 versus expected 16. |
| Inactive roots omitted | `norm(grouped, out_labels, lam, allv, 1)` | `AssertionError` at `overlap_full_output_norm_exact`; record computed 4 versus expected 8. |

Each trial runs the same finite predicates before the witnesses, including
all 2,184 bounded-hole inequalities. A crash, failure at another predicate,
missing/multiple replacement anchor, or resource refusal is not the required
mutation rejection. Bind each trial to the exact compiled source hash and
record the before/after substitution. Preserve a distinct JSON outcome for
each trial, plus a suite receipt and stdout/stderr, all under
`checks/lib1_*_v2*`. Create outputs exclusively; refuse existing paths.
Only those two substitutions are implementation mutations tested by v2.
The three inherited static contrasts acquire no new mutation-run claim.

## Resource and evidence boundaries

Use exact Python integers/Fractions, Python `-B`, `nice -n 10`, and
`OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=VECLIB_MAXIMUM_THREADS=NUMEXPR_NUM_THREADS=1`.
No pools, multiprocessing, numerical libraries, or background workers.
Keep the original script-enforced resource requirements: macOS
`memory_pressure -Q` free memory at least 50%, every load average below
20, maximum process RSS strictly below 2,000,000,000 bytes, nice at least
10, and all five thread variables equal to 1. Check at each trial start,
periodically, and on its outcome, including expected assertion failures.
One shared 60-second deadline covers the entire invocation. Record any
unverifiable gate, refusal, or sandbox failure honestly; it establishes
neither a mathematical failure nor successful B1 coverage.

Bind source and criteria hashes, measured resources, exact witness values,
predicate counts, trial outcomes and exit classifications. The suite is
successful only if the baseline completes and both actual mutants fail at
their specified exact assertions after satisfying the resource gates.
These are same-author finite regression checks, not independent review or
proof of the all-volume theorem. Original-reviewer confirmation remains
pending; B1 repair supplies no LAND or audit status.
