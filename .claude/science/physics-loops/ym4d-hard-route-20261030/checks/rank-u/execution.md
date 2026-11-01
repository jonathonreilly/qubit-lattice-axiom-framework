# Execution record

Source: 892504e4c63f195fbd791a1db913f67b4b749459.
No numerical job, SVD, optimization, simulation or symbolic-code calculation
was run for this item. No numerical PASS/FAIL is asserted.

The sparse checkout omitted scripts/automation_lock.py. Its exact HEAD
contents were copied into tooling/automation_lock.py in this allowed output
folder and supplied to the real scripts/lab_ops.py through PYTHONPATH.
PYTHONDONTWRITEBYTECODE=1 prevented imported bytecode writes elsewhere.

The actual preflight command was the following, with PYTHONPATH pointing at
tooling/ and OPENBLAS_NUM_THREADS, OMP_NUM_THREADS, MKL_NUM_THREADS and
VECLIB_MAXIMUM_THREADS all set to 1:

    python3 scripts/lab_ops.py preflight --numeric --min-mem-pct 50 \
      --target .claude/science/physics-loops/ym4d-hard-route-20261030 \
      --role worker --model gpt-6-astra --effort max

Observed output (exit 1):

    ok      disk: 37 GB free, limit 10
    ok      memory: 65% free, limit 50
    ok      load: 1.8, limit 10
    ok      model floor: gpt-6-astra allowed for worker
    ok      nice: works here
    note    memory cap: ulimit unavailable; a job must watch its own memory
    ok      network: origin reachable
    refuse  numeric lock: held by excess-v6d until 2026-11-01T13:36:48.648418+00:00
    preflight: refuse (numeric lock)

Subsequent calls to `python3 scripts/lab_ops.py numeric-lock status` also
reported held by excess-v6d. At the status check paired with the clock reading
2026-11-01 11:16:21 UTC, the recorded lease began at
2026-11-01T10:36:48.648418+00:00 and expired at the time above.
The other worker's lock was not modified. No acquire succeeded or was
treated as successful; no numeric job was launched while waiting.

During the wait the exact staggered construction refuted the requested
limit clause. The task therefore reached its mathematical stopping point
without a numerical run. The registered numerical proposals in CRITERIA.md
are unexecuted. The proof rests solely on the identities and inequalities
written in ../../library/rank-u-staggered-limit.md.
