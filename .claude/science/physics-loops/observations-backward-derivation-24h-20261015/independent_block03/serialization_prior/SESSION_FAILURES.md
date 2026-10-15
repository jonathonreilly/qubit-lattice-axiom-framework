# Actual interrupted attempt

The first core command was:

    python3 .claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_block03/check_material.py > .claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_block03/run_stdout.txt 2>&1

Its working directory was the supplied campaign worktree. The process was the
checker's own Python PID 35412. It initially buffered all check results until
completion and spent excessive time expanding a rational expression. At the
last measurement it had run for 09:22 wall time, consumed 06:57.40 accumulated
CPU time, and used 298800 KB resident memory. The parent asked for a bounded
fallback instead of an unbounded symbolic job. I sent `kill -INT 35412` to this
owned checker only. It exited 130. The traceback locates the interruption in
the `s.cancel` polynomial expansion for the Cartesian spatial metric equation,
at `check_material.py` line 144. No completed result file was emitted, so this
attempt contributes no counted successful checks. Its mathematical intermediate
values were not saved and are not retroactively claimed as verified evidence.

Preserved artifacts:

- `check_material.py`: exact original checker, unchanged.
- `run_stdout.txt`: actual KeyboardInterrupt traceback.
- `attempt01_process_cost.txt`: actual `ps` output immediately before stopping.
- `attempt02_changes.diff`: exact changes for the bounded replacement.

The replacement combines denominators using SymPy `together` before `cancel`,
prints each check's start immediately, and saves evidence to a distinct file.
The mathematical inputs, equations, and assertions were unchanged. It ran under
an external 120-second timeout and completed in 3.738660874776542 seconds with
exit code 0 and 35 successful checks. Its resource record is
`attempt02_execution.json`; its actual output and per-check results are in
`factored_stdout.txt` and `factored_evidence.json`.

The boundary and conservation/dimension runs completed without failed checks.
There were no source edits, network calls, Git operations, author-runner imports,
or formal audit actions. The original interruption is a computational-method
failure to complete within a reasonable bound, not evidence of a failed field
equation. No unfinished checker process remains.
