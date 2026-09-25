# Formation under the clock field: does the lattice fill from the voids and jam? — run 2

Worker `w-jonathonsmac4f50-j9bc3`, model `claude-opus-5-5`. Blocks 53 and 95 were written by the same model family (Claude). The log is `logs/probes/C:formation-with-the-clock-fill:a2/w-jonathonsmac4f50-j9bc3__d01e2faf__20260925T015328Z.json`.

## Model

**Block 95 as landed on main.** The field follows the records on the neutralised torus: `log w_z = 6 log κ Σ_{r∈C} G(z − r)`, where `G` is the mean-zero inverse of `Δ = 6I − Adj`. Here `log κ = −g`. Formation is outside block 95's scope; it is supplied by this task.

**Events:**
- formation at every empty site at rate `z w_x`;
- a hop of a record at `x` to each empty neighbour at rate `w_x/6`, as the task states.

The landed note's hop rate at `W = 1` is `w_x/12`, because the heat-bath factor is 1/2. That is the same process with `z` doubled, since only the ratio of formation to hopping matters here.

**Simulation.** A numba kinetic Monte Carlo on the 16³ torus, starting empty. Events are selected exactly, with no time step. Every clock is updated after every event through precomputed factors `exp(−6g G(d))`. Floating point.

## Results

**Checkpoints.** At each filling fraction the run records:
- the time;
- the largest cluster's share of records (6-neighbour clusters);
- the fraction of formation events within graph distance 2 of the largest cluster, against the fraction of **empty** sites within that distance at the same moment (the null for uniform formation).

| g, z | events to jam | time to 50% / 99% / 100% | largest-cluster share at 20% / 30% filling | formation near the cluster ÷ null, while null < 0.9 |
|---|---|---|---|---|
| 0.5, 1e-3 | 551 k | 304 / 1290 / 3290 | 0.04 / 0.71 | 0.54 |
| 0.5, 1e-4 | 2.06 M | 1250 / 9150 / 34300 | 0.68 / 0.91 | 0.29 |
| 1, 1e-3 | 258 k | 239 / 522 / 1330 | 0.09 / 0.81 | 0.63 |
| 1, 1e-4 | 747 k | 944 / 1960 / 13500 | 0.22 / 0.91 | 0.38 |

**Reading.**
- **Every run jams** (4096/4096). The fill slows sharply at the end: the last 1% takes most of the time. The last empty sites sit inside the cluster, where clocks are slow, but formation there never stops.
- **New records form mostly in voids.** Near the largest cluster the formation rate is 0.29–0.63 of what uniform formation would give. The avoidance is stronger at small z, where hops have time to gather records into clusters between formations.
- **Records join clusters.** The largest cluster holds 68–91% of the records by 20–30% filling. For g = 0.5, z = 1e-4 that happens at 20% filling, below random site percolation (≈ 0.31 on the cubic lattice): the attraction clumps the records.

## Verdict

The expectation was that new records form mostly in voids, join clusters, and the lattice eventually jams. All three hold at all four points. There is no HIT.
