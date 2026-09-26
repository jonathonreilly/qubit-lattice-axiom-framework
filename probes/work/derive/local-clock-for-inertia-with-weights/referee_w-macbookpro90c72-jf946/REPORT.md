# Referee: local-clock-for-inertia-with-weights a2

Worker `w-macbookpro90c72-jf946` (`grok-4.6`). Author `w-jonathonsmac4f50-j42a0` (`claude-opus-5`). The attempt's script is not imported.

## Verdict

Confirmed partial, on the 3-torus at `(p, q, r) = (3, 1, 2)`. Distance-one rates can keep `π` stationary on every three-record state. One four-record state makes that same class impossible.

## What was checked

- **The local clock.** There are 70200 three-record states with a record at the origin. The rate `1/π_x` fails on 3168 of them. The largest defect is 3, at `(0,0,0):+y`, `(0,0,1):+z`, `(0,1,0):+y`.
- **Conservation.** Every three-record event, and every event of the four-record witness, keeps the record count and the multiset of contents.
- **Three records.** At `c = 1` the balance is 332 equations in 274 patterns, with a strictly positive solution whose rates lie in `[1, 25]` and which meets every equation in exact arithmetic. At `c = 1/2` there are 334 equations in 274 patterns, with rates in `[1, 1396/75]`, again exact.
- **Four records.** Adjoining `(1,0,1):−x`, `(1,0,2):+z`, `(1,1,2):−x`, `(1,2,1):−x` gives 333 equations in 275 patterns. A rational Farkas vector is nonpositive on every pattern and sums to `−36/5`.

A `4×4×4` window and any wider locality class were not examined. The three-record rate vector is one exact solution, not a canonical closed form.
