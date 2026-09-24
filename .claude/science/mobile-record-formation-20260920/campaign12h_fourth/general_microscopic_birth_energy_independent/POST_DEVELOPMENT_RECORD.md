# POST development and failures

All work remains in general_microscopic_birth_energy_independent. PRE and author
bytes are fixed. The exposure boundary, code/result bindings, and final packet
scope are recorded in POST_SOURCE_BINDINGS.json and the comparison report.

## Authentication recovery

The first exploratory inline authentication command authenticated the PRE seal
and all 52 PRE artifacts, then the author seal and 12 author artifacts. It failed
while resolving the first bound source because the inline expression used
`repo=here.parents[3]` instead of `here.parents[4]`. The resulting path contained
`.claude/.claude/`. This was a path-root mistake, not a hash mismatch. No snapshot
or manifest write had yet occurred. The final traceback line was:

    FileNotFoundError: [Errno 2] No such file or directory: '/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/.claude/science/mobile-record-formation-20260920/campaign12h_fourth/local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md'

The reusable post_authenticate.py uses the corrected repository root and then
authenticates all 52 PRE bindings, 12 author artifacts, and 8 source bindings.
POST_AUTHENTICATION.stdout/stderr preserve the successful execution. The
sources and manifest were first written only after those checks succeeded.

## Independent path comparison attempt 01

The original post_path_compare.py completed all 55 floating path comparisons
and reached its final exact symbolic derivative assertion. It used Python `==`
on two differently distributed SymPy expressions:

    assert sp.factor(sp.diff(F0,t)) == -24*(t-1)*(4*t-7)

Python's right-associated construction had already distributed the constant
into an intermediate factor; structural equality returned false even though
the expanded difference is exactly zero. This was an assertion-design failure.
The entire failed code is preserved as post_path_compare_run01.py; raw stdout
and traceback are POST_PATH_COMPARISON_01.stdout and .stderr. No JSON result
was produced by that failed attempt, and it is not counted as a completed run.

The only change in successful attempt 02 is:

    assert sp.expand(sp.diff(F0,t)+24*(t-1)*(4*t-7)) == 0

All 55 cases were rerun. Their numerical comparison tolerance was not changed.
All polynomial identities, including the derivative identity, then passed by
exact simplification. POST_PATH_COMPARISON_RESULTS.json contains every numeric
comparison and all simplified polynomial outputs. Attempt 02 stdout/stderr are
retained. This is not a relaxation of a failed physics coefficient.

## Complete-matrix attempt 01 and scope witness

post_complete_k24.py succeeded on its first run. It independently enumerates
matter words and three free cycle fields, rather than enumerate all fields as
the author builder does. It constructs local compensation gates directly,
checks the P-only simplification, then forms the full generator adjoint matrix.
It adds lambda=1/2 and all-P operator norms to the released scalar-input cases.
All 36 endpoint rows and six two-birth rows are compared with the frozen author
JSON only after the independent calculations are formed. None of the author
Python code is imported or executed. All 8,946 recorded checks passed; the
number is bookkeeping, not a substitute for the proof or independence.

The complete control's stderr contains SciPy FutureWarnings that integer W
arrays passed to diags are presently cast to float64. They are preserved. They
are not failures, and no warning-suppression rerun was used. Complete operators
and states in the calculation are real/complex float64 as intended.

An exploratory diagonal scan of the computed leading operator found the
following exact basis expectations (not an S-to-infinity analysis):

    lambda=0:  -8 on q=(1,1,0,0,0,0), E=(-1,-1,1,1,1,1,-1,-1)
    lambda=.5: -3 on q=(-1,1,1,1,0,0), E=(-1,-1,-1,1,0,0,1,-1)
    lambda=1:  -4 on q=(-1,1,1,1,0,0), E=(0,0,-1,-1,-1,-1,1,1)

The bounded report uses only the first word, for which post_scope_witness.py
records exact leading gain/loss components and a direct epsilon=.01 microscopic
calculation for both instruments. This successful control preserves its complete
stdout/stderr and JSON. The other two scan rows are retained here as exploratory
observations and are not separately promoted to new theorems. The resulting
scope distinction is that the specified cube input has positive leading power;
arbitrary P input need not. The author makes no contrary general claim.

## Boundaries

No other checker folder, current CHECKPOINT, external personal-reservoir plan,
or new full-instrument author work was read. No commits, author edits, audit
verdicts, publication operations, prompt changes, or deadline extensions were
performed. The inherited model and reasoning were retained; no subagents were
spawned. The frozen PRE's separate finite terms and ring coefficients remain
attributed to PRE, not to the released author packet.
