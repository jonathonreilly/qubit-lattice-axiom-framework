threshold-and-plateau-tables, independent run 2 of 2
worker w-jonathonsmac4f50-jcbe9 (claude-opus-5), unit C-threshold-and-plateau-tables-a2

The task: turn the five 3+1 scan directories into (1) plateau against beta per lattice and L with seed scatter,
(2) the bracket where memory appears, (3) the dichotomy table by dimension, (4) lowk_ratio against beta - and, if
fewer than half the points are logged, to list what is missing and stop. Fewer than half are logged.
Every stdout file was checked against its log's stdout_sha256 before being read.

(1) INVENTORY
  X:formation-3plus1-threshold-fine: 0 of 22 grid points logged (0.0%)
  X:lightcone-threshold-fine: 0 of 30 grid points logged (0.0%)
  X:formation-3plus1-seeds: 2 of 30 grid points logged (6.7%)
  X:formation-by-dimension: 0 of 16 grid points logged (0.0%)
  X:lightcone-by-dimension: 0 of 22 grid points logged (0.0%)
  overall: 2 of 120 grid points logged (1.7%), the task's threshold being half

(2) EVERYTHING THAT IS LOGGED
  everything that IS logged, with the plateau, the kernel normalisation and a drift check over the last
  three rows of the memory table (the task's own criterion):
    X:formation-3plus1-seeds [3 sphere 2 48 3000 1500 2]: plateau=0.7366, lowk_ratio=0.9924; last three rows 1539:0.7336 2149:0.7374 3000:0.7374, spread 0.5% -> settled  [stdout file]
    X:formation-3plus1-seeds [3s sphere 2 48 3000 1500 3]: plateau=0.8946, lowk_ratio=1.0717; last three rows 1539:0.8937 2149:0.8943 3000:0.8944, spread 0.1% -> settled  [stdout file]
  Both runs are settled by the task's own criterion (spread over the last three memory-table rows below 5 per
  cent): the backward lattice at beta = 2 on 48^3 plateaus at 0.7366 with lowk_ratio 0.9924, the light cone at
  the same beta and box at 0.8946 with lowk_ratio 1.0717.

(3) WHAT IS MISSING
  what is missing, per scan, with the exact argument lists:
  X:formation-3plus1-threshold-fine: 22 missing
    dim=3 menu=sphere L=32: beta in ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2'] (11 runs)
    dim=3 menu=sphere L=48: beta in ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2'] (11 runs)
  X:lightcone-threshold-fine: 30 missing
    dim=3s menu=sphere L=32: beta in ['0.3', '0.35', '0.4', '0.45', '0.5', '0.55', '0.6', '0.65', '0.7', '0.75', '0.8', '0.85', '0.9', '0.95', '1'] (15 runs)
    dim=3s menu=sphere L=48: beta in ['0.3', '0.35', '0.4', '0.45', '0.5', '0.55', '0.6', '0.65', '0.7', '0.75', '0.8', '0.85', '0.9', '0.95', '1'] (15 runs)
  X:formation-3plus1-seeds: 28 missing
    dim=3 menu=sphere L=48: beta in ['1.5', '2', '3'] (14 runs)
    dim=3s menu=sphere L=48: beta in ['0.75', '1', '2'] (14 runs)
  X:formation-by-dimension: 16 missing
    dim=1 menu=sphere L=4096: beta in ['2', '6', '12', '24'] (4 runs)
    dim=4 menu=sphere L=12: beta in ['0.5', '0.75', '1', '1.5', '2', '3'] (6 runs)
    dim=4 menu=sphere L=16: beta in ['0.5', '0.75', '1', '1.5', '2', '3'] (6 runs)
  X:lightcone-by-dimension: 22 missing
    dim=1s menu=sphere L=4096: beta in ['2', '6', '12', '24'] (4 runs)
    dim=2s menu=sphere L=256: beta in ['1', '2', '3', '6', '12', '24'] (6 runs)
    dim=4s menu=sphere L=12: beta in ['0.2', '0.3', '0.4', '0.5', '0.75', '1'] (6 runs)
    dim=4s menu=sphere L=16: beta in ['0.2', '0.3', '0.4', '0.5', '0.75', '1'] (6 runs)
  The full list of 0 missing argument lists is in the run's output, one per line; the first few are:


(4) CONSEQUENCES
  consequences for the four tables the task asks for:
    (1) plateau against beta: no lattice has more than one coupling logged, so there is no curve and no
        seed scatter (the only two logged runs are a pair at the same beta with different neighbourhoods).
    (2) the memory bracket needs a largest beta with plateau < 0.1 and a smallest with plateau > 0.5 that
        is not drifting: no lattice has both, so no bracket can be given.
    (3) the dichotomy by dimension: the only two logged runs are both at dimension 3, beta = 2, L = 48
        (one backward, one light-cone); dimensions 1, 2 and 4 have no logged run in these five scans, so
        every entry of the table would read 'undecided' - a table of undecideds, not a result.
    (4) lowk_ratio against beta: two points, one per lattice, at the same beta; no curve.
  Stopping here, as the task instructs.

(5) READING
  1.7 per cent of the grid is logged: two runs, both at dimension 3, beta = 2, L = 48, one per lattice. None of
  the four tables can be formed - there is no second coupling for any lattice, no seed repeat, and nothing at all
  at dimensions 1, 2 and 4. This is a missing-data report, as the task instructs, and there is no HIT: the task's
  expectations are neither supported nor contradicted by what is logged.
  For the supervisor: the two points that do exist are consistent with the campaign's earlier numbers (the
  backward lattice ordering later than the light cone at the same beta) and both have a kernel normalisation
  within 8 per cent of 1.
