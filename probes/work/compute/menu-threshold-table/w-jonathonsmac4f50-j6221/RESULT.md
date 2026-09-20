menu-threshold-table, independent run 2 of 2
worker w-jonathonsmac4f50-j6221 (claude-opus-5), unit C-menu-threshold-table-a2

The task: turn the scan logs under X:menu-size-threshold, X:formation-3plus1-sphere-memory and
X:formation-2plus1-sphere-memory into plateau curves, brackets for the half-of-large-beta crossing, and a table of
the bracket against menu size N for dim = 2 and 3 - and, if fewer than half the grid points are logged, to report
what is missing and stop. Fewer than half are logged, so this is that report.

(1) INVENTORY
  X:menu-size-threshold: 5 of 140 grid points logged (3.6%)
  X:formation-3plus1-sphere-memory: 0 of 20 grid points logged (0.0%); 1 further run(s) present that are not grid points: [3 sphere 1 32 1500 750 1]
    DATA DEFECT in X:formation-3plus1-sphere-memory: fable-check__3f4f3536__20260918T234707Z.json carries a stdout file that does not hash to the log's stdout_sha256; the log's own self-check already recorded FAIL: FAIL: stdout file does not match the log's stdout_sha256 (edited after the run?)
  X:formation-2plus1-sphere-memory: 0 of 10 grid points logged (0.0%)
  overall: 5 of 170 grid points logged (2.9%), the task's threshold being half

(2) THE POINTS THAT ARE LOGGED, WITH THE DRIFT CHECK
  the points that ARE logged, with the last two rows of their memory table (the drift check):
    X:menu-size-threshold [2 edges12 1.5 128 3000 1500 1]: plateau_|m|=0.0163; levels 2149->3000: |m| 0.0162 -> 0.0120 (relative change 35.0%) -> STILL DRIFTING  [rows from: stdout file]
    X:menu-size-threshold [2 fib100 12 128 3000 1500 1]: plateau_|m|=0.9350; levels 2149->3000: |m| 0.9370 -> 0.9347 (relative change 0.2%) -> settled  [rows from: stdout file]
    X:menu-size-threshold [3 axes6 8 32 3000 1500 1]: plateau_|m|=1.0000; levels 2149->3000: |m| 1.0000 -> 1.0000 (relative change 0.0%) -> settled  [rows from: stdout file]
    X:menu-size-threshold [3 edges12 0.5 32 3000 1500 1]: plateau_|m|=0.0060; levels 2149->3000: |m| 0.0055 -> 0.0115 (relative change 52.2%) -> STILL DRIFTING  [rows from: stdout file]
    X:menu-size-threshold [3 fib50 6 32 3000 1500 1]: plateau_|m|=0.9496; levels 2149->3000: |m| 0.9499 -> 0.9494 (relative change 0.1%) -> settled  [rows from: stdout file]
    X:formation-3plus1-sphere-memory [3 sphere 1 32 1500 750 1]  (NOT a grid point): plateau_|m|=0.0155; levels 1106->1500: |m| 0.0120 -> 0.0102 (relative change 17.6%) -> STILL DRIFTING  [rows from: MISMATCHED stdout file, ignored (rows from the log's own stdout_tail)]
  The drift check compares the last two rows of each run's memory table. Two of the six runs are still drifting
  at the end of their run (both near their threshold, where the plateau is smallest), so even those points would
  not give a reliable plateau.

(3) A DATA DEFECT FOUND WHILE READING
  logs/probes/X:formation-3plus1-sphere-memory/fable-check__3f4f3536__20260918T234707Z.json has a stdout file
  beside it that is a different run's output: the .txt reads beta=6.0 with plateau_|m|=0.9242, while the log's
  command, summary and stdout_tail all read beta=1.0 with plateau_|m|=0.0155 and agree with each other. The .txt
  hashes to 1e144e11... against the recorded c22d492e..., and the log's own self-check had already recorded
  FAIL "stdout file does not match the log's stdout_sha256 (edited after the run?)". I triaged it machine (the
  file was overwritten after the run, not the log mis-written) and the run above falls back to the log's own
  stdout_tail for that point, which gives |m| 0.0120 -> 0.0102 over levels 1106 -> 1500: still drifting.
  That run is also not a grid point: the grid asks for T = 3000, T0 = 1500 at L = 32 (or T = 2000, T0 = 1000 at
  L = 64) and this run used T = 1500, T0 = 750.

(4) WHAT IS MISSING
  what is missing (the exact argument lists a later run would need):
  X:menu-size-threshold: 135 missing, grouped by (dim, menu):
    dim=2 menu=axes6: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=2 menu=corners8: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=2 menu=edges12: beta in ['0.5', '0.75', '1', '2', '3', '4', '6', '8', '12'] (9 runs)
    dim=2 menu=fib100: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8'] (9 runs)
    dim=2 menu=fib20: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=2 menu=fib200: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=2 menu=fib50: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=3 menu=axes6: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '12'] (9 runs)
    dim=3 menu=corners8: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=3 menu=edges12: beta in ['0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (9 runs)
    dim=3 menu=fib100: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=3 menu=fib20: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=3 menu=fib200: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12'] (10 runs)
    dim=3 menu=fib50: beta in ['0.5', '0.75', '1', '1.5', '2', '3', '4', '8', '12'] (9 runs)
  X:formation-3plus1-sphere-memory: 20 missing, grouped by (dim, menu):
    dim=3 menu=sphere: beta in ['0.4', '0.5', '0.6', '0.75', '1', '1.5', '2', '3', '6', '12'] (20 runs)
  X:formation-2plus1-sphere-memory: 10 missing, grouped by (dim, menu):
    dim=2 menu=sphere: beta in ['0.4', '0.5', '0.6', '0.75', '1', '1.5', '2', '3', '6', '12'] (10 runs)
  The full list of 0 missing argument lists is in the run's output, one per line, in the form
  "cd probes/lib && python3 formation_levelplane.py <args>"; the first few are:


(5) WHY THIS STOPS HERE
  with 2.9 percent of the grid logged there is no (dim, menu) with more than one coupling, so no plateau
  curve, no half-of-the-large-beta-value crossing and no bracket can be formed, for either dimension.
  The task's expectation - that the bracket rises without bound with the menu size N in 2+1 and
  approaches the sphere's in 3+1 - is therefore neither supported nor contradicted by what is logged.
  Stopping here, as the task instructs.

(6) READING
  2.9 percent of the grid is logged, and no (dim, menu) pair has more than one coupling, so there is no plateau
  curve to cross, no bracket to locate and no bracket-against-N table for either dimension. The task's expectation
  - that in 2+1 the bracket rises without bound with the menu size and in 3+1 approaches the sphere's - is neither
  supported nor contradicted by the logged data, so there is no HIT: this is a missing-data report, as instructed.
  What the five on-grid points do show, for whatever it is worth to the supervisor: dim=3 axes6 at beta=8 sits at
  |m| = 1.0000 (a finite menu can lock completely), dim=3 fib50 at beta=6 at 0.9496 and dim=2 fib100 at beta=12 at
  0.9350, while the two low-beta points (dim=2 edges12 at 1.5, dim=3 edges12 at 0.5) are at the finite-size floor
  and still drifting.
