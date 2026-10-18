# NT-3 = T-G1 report

**Author.** Claude Opus 5.5, worked 20:44–21:20Z. Same model family as every other agent, so not independent; not refereed. The supervisor saved this report from the worker's final message, because the worker's tool refused to write the file.

## Reading

**Literal pre-registered reading: TG1-BROKEN.** Applying the pre-registered rules as written gives TG1-BROKEN for all three 1D filters.

**Worker's interpretation: OPEN.** Every BROKEN trigger is softening next to the light momentum. The pre-registration meant to exempt that, but its light-attribution metric reads zero for the self-conjugate 6-vector sector, so it mislabelled the soft state as "non-light". A SYMMETRIC verdict is also unreachable at infinite coupling for any filter with a zero.

**Memory overrun.** The first L = 7 run reached about 1.10 GB for roughly 10 s, against the 1.0 GB cap, and was killed (`scripts/primary_L7_killed_memcap.err`). The fix was an iterative solver for sectors above 4000 states plus a 950 MB watchdog (`scripts/watchdog.sh`). All other runs peaked at 0.08–0.52 GB.

## Plain words

**What was tested.** The smallest stand-in for X2: 4 flavours with SU(4) ≅ Spin(6), and a 6-vector pairing interaction (the toy version of the 10-vector channel) with every leg filtered. Exact diagonalisation over all symmetry sectors, on:
- rings of L = 3–7 sites, with three filters whose overlaps (0.66, 0.97, 1.28) bracket X2's 3D values of 0.63 and 1.22;
- on-site and flat-filter controls;
- one 2×2×2 cube using X2's f_NN and f_F1.

**What held (checked):**
- **Ground state.** Unique and a full SU(4) singlet everywhere.
- **Static order.** The 6-vector structure factor grows at most 1.35× from 4 to 7 sites. The symmetric control grows 1.22×; long-range order would give at least 1.75×.
- **Mirror corner.** Its spectral weight sits at about 0.76·f(k)², with no size trend.
- **With the kinetic term (W = 4, 16).** The soft states become light quasiparticles, the ground state stays a unique singlet, and the 6-sector gap is O(W).
- **Cube.** Unique singlet; gap 1.31 for f_NN and 1.65 for f_F1, against 1.0 on-site.

**What failed.** The infinite-coupling gap falls with size:
- star filter: 0.45 → 0.18 → 0.074 → 0.031;
- steepest filter: down to 8e-5.

The softest state is always in the 6-vector pair channel. 87–99.95% of its pair weight sits on the two momenta nearest the light one, where the filter is nearly zero.

**Why that is forced (proof skeleton).** Any local filter that vanishes at the light momentum makes the infinite-coupling Hamiltonian gapless there.

**Follow-ups after removing the light shell:**
- the flattest filter's gap goes flat (0.58, 0.66, 0.72);
- the star filter's gap scales as 0.64 × (smallest kept f)², so the next shell takes over;
- the steepest filter's coefficient drifts 0.72 → 0.59, read as a crossover (suggested).

## Suggested, new for X2

The softest channel is the G_SM-breaking pair channel (10-vector in X2), carried by modes next to the light corner. So the GPR danger (K1 gap G2) has a second place to look: the kinetic/interaction crossover near hw1, at q* ~ (16/W)^{1/3}. K1's G1 should read "gapped away from the light corner", or be posed at finite W.

## Scope

- These are 0+1D-like clusters (rings with L ≤ 7, one 8-site cube). They cannot decide 3+1D or 4D.
- 1D has no continuous symmetry breaking (Coleman), so only precursors are visible.
- SU(4) and its 6-vector stand in for Spin(10) and its 10-vector.

## Next test (T-G1′)

A 2+1D Hamiltonian at finite W with the walker kinetic term, run with DMRG or QMC. Measure:
- the static 10/6-vector structure factor against size;
- the mirror-corner spectral gap;
- the pair susceptibility restricted to |f| ≥ f₀.

Check sign-freeness first (SIGN-1).

## Files

`PREREG.md` (dated follow-ups A1–A3) and `scripts/` (all `.out`, `.log` and `.err` files; `tables.out` holds the summary tables).
