# Refuting pass — block 32 (supervisor-run, disjoint machinery; 2026-09-17)

Routes compared (controls `specs/supervisor_control_block32_mintree.py` (integer program), `..._treedp.py` (general dynamic program), `..._ssdp.py` (single-seed program), `..._crosscheck.py`, `..._climb.py`, `..._climb_seeded.py`; refuting pass `specs/supervisor_control_block32_refuter.py`, run from `scripts/` as `python3 <specs>/supervisor_control_block32_refuter.py . <specs>`; outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the extremal minima (T2) | the exact single-seed dynamic program: `0` at `c = 1`, `3/50` and `2/25` at `99/100` | an integer program over node, arrow, fork and flow variables (scipy `milp`, floating point) on the whole family, no single-seed reduction | `Z_A`: cost `0` with `(7, 7, 1, 0)` at `c = 1`, `3/50` with `(6, 6, 1, 0)` at `99/100`; `Z_B`: `0` with `(9, 9, 1, 0)`, `2/25` with `(8, 8, 1, 0)` — equal to the exact program |
| the rule on the boxes | the runner's dictionary automaton | a numpy array implementation | agreement on all `112` and `200` sites |
| the component lemma (T1) | the runner's search from the root | union-find over every arrow and fork among the 1-sites | the same components (`42`, `60` nodes, one seed each) |
| the reduction (T1) | brute force on `90 + 51` tiny realizations in `3×3×4` | brute force on `60` further tiny realizations in `3×3×5` with another seed, against the exact program (single-seed, `39`) and the integer program (all, `60`) | `0` disagreements |
| `c* > 1`? | twelve climbs, four seeded perturbation climbs: maximum `1` | simulated annealing with one-to-three-site moves and temperature, `4×4×7`, `240` s | best `1/3`; nothing above `1` |

Findings: nothing refuted. Fold items: the general dynamic program (`..._treedp.py`) reported `E − c|A| − 3|S|` instead of `E − 3(|S| − 1) − c|A|` (a constant `3`), caught by the brute-force cross-check and corrected; the runner's B2 compared the family against itself instead of against the fork-free family (always equal), corrected to compare against the fork-free minimum. Facts settled while executing: the general program with partition states is exact but too slow at seven sites per level; the component lemma makes it unnecessary on the extremal realizations, whose components hold one seed; the integer program's optimal trees differ from the exact program's in shape but never in cost.
