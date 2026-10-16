# Reproduction of this focused check

The two active check programs are `check_integrated_math.py` and
`observe_runner.py`. Each declares a 120-second limit and exact literal
repository input paths. Execute each under an external timeout, as was done
for the stored receipts. From the campaign repository root, the command shape
is:

```python
from pathlib import Path
import os, subprocess, sys

folder = Path(".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_integration")
environment = os.environ.copy()
environment["PYTHONDONTWRITEBYTECODE"] = "1"
for filename in ("check_integrated_math.py", "observe_runner.py"):
    subprocess.run([sys.executable, "-B", str(folder / filename)],
                   timeout=120, check=True, env=environment)
```

The original executions redirected each child's stdout/stderr into the named
stdout file and recorded its return code, wall time, child CPU time, maximum
resident memory and checker SHA256. The execution JSON files are those actual
records. Re-execution overwrites the corresponding current evidence outputs;
copy them first if their historical bytes need to be retained.

`check_integrated_math.py` imports the current canonical math helper and hashes
the current note, runner and helper against its frozen identities. Its
independent tensor calculation derives geometry from the metric. It writes
`independent_math_evidence.json` in this directory.

`observe_runner.py` executes the byte-identical canonical copies in
`reproduction_repaired/`. It traces repository open events and helper calls,
and the copied primary writes its receipt beneath that directory. The active
copies are reproduction fixtures, not additional author sources or canonical
audit caches. The final binding record verifies their identity against the
three canonical files. The observer uses no earlier block scripts or outputs.

The `reproduction/` directory and files under `pre_dimension/` are preserved
historical reproductions, not the active input set. `SOURCE_SNAPSHOT.json`
describes the earlier initial snapshot, and the source-movement JSON records
make subsequent changes explicit. `FINAL_BINDING.json` and `MANIFEST.json`
identify the delivered state. Prior failures are not inputs to the active
mathematical calculation; they document what actually happened.
