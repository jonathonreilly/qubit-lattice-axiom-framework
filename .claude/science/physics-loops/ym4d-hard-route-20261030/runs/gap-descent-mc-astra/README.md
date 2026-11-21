# Row 1101 Monte Carlo records — GUIDE only

The research note is `../../library/gap-descent-mc-astra.md`.
No numerical output is a proof or grants scientific status.

`su2.cpp` implements the finite anisotropic Wilson theory and the periodic
reduced face. `manifest.json` specifies all jobs, seeds and raw-record layout.
It is the frozen source actually used. `su2_guarded.cpp` is a later I/O-safe
successor, not used for these measurements; `io_guard_check.json` records
output-equivalence and intentional failure checks. Do not replace the frozen
source when checking the production manifest hash.
Each `.npz` holds float32 slice averages, small Wilson loops, and winding
loops. Face-anchor archives also hold the point spin correlation. Each job's
JSON binds its archive and decompressed records by SHA-256. Configurations
and binaries live only in the scratch directory recorded in the manifest.

`pilot_v1/` preserves the first ten chains, their original source and analysis,
and the interruption record for the eleventh. They are not production data.
The original analysis accepted one unresolved shifted fit. The research note
explicitly rejects that candidate. Use the current analysis only for the
current eight-step-smearing records, not the two-step pilot records.
`handoff_overlap/` preserves one completed chain affected by a pause race.
The canonical replacement was reproduced serially with the same seed and
matching raw/configuration/warm-up hashes. It is not an extra independent
sample. `serial_reproduction.json` records this repair.

There are 74 retained gauge chains: the 72 grid/anchor chains and two 16^4
beta=2.5 isotropic controls. `extra_manifest.json` describes the larger-volume
control and the serial reproduction. There are also 18 standalone O(4)
chains. The final summary contains 37 gauge ensembles, each with two starts.

One cycle is one heat-bath sweep plus one over-relaxation sweep. Production
records are four cycles apart. The O(4) controls instead use one heat-bath
plus four over-relaxation sweeps, and record every two cycles.
They include 8^2 and 12^2 matched-geometry controls and 128^2 published-value
controls. Winding indices enumerate directions other than the measured axis:
for axis 0 they mean 1,2,3; for axis 2 they mean 0,1,3.

The source-only commands below are a recovery recipe. Do not launch while
another machine numeric lock is held. Create a new empty scratch directory,
recover the missing `automation_lock.py` helper from the pinned main revision
if needed, and export its directory as PYTHONPATH. Run preflight with at least
50% free memory; acquire the numeric lock with the holder named in the drivers
and confirm `status: acquired`. Set OMP, OPENBLAS, MKL, VECLIB and NUMEXPR
thread variables to 1. The drivers run serially and enforce the memory gate.
The actual session ran at nice 20; a request to lower that number to 10 was
denied. Two documented scheduling overlaps occurred; the affected retained
chain was reproduced serially. The numeric lock has now been released.

```sh
clang++ -O3 -std=c++17 su2.cpp -o "$SA/su2"
clang++ -O3 -std=c++17 o4_control.cpp -o "$SA/o4_control"
nice -n 10 python3 run_grid.py "$SA"
nice -n 10 python3 run_extra.py "$SA"
nice -n 10 python3 run_o4.py "$SA"
nice -n 10 python3 analyze.py
nice -n 10 python3 verify_records.py "$SA"
nice -n 10 python3 report_tables.py
```

The three sampling drivers expect the scratch path as an argument.
`run_extra.py` also preserves/reproduces the historically affected chain;
that duplicate is not pooled. `run_grid.py` skips complete archived jobs.
Use a fresh task directory for reproduction and never overwrite these
evidence records. The fixed seeds reproduce existing data; independent
replication requires new seeds. Release the numeric lock after all sampling
and analysis have ended. Large configurations and binaries stay in scratch.

Analysis uses 64-measurement bins and a 128-measurement comparison, with the
mean recomputed in each deleted-bin sample. The saved analyses include every
channel's connected correlation, effective masses, autocorrelation estimates,
chain agreement, and all candidate/rejected windows. `fit_inventory.csv` and
`effective_masses.csv` flatten them for inspection. `tables.md` is generated
evidence, not the research verdict. The plots show selected candidate fits;
they do not certify the slowest observable sector.
The matched beta=2.5 16^4 scalar control fails in one direction by 3.36
combined errors. No descent point shows a three-error downward violation.
The research note states the resulting OPEN verdict and all limitations.
