lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T23:35Z

# The neutral seed for the SU(2) Wilson trajectory at late cutoffs: attempt 2 (row 1364)

Queue row 1364, `gap-mini-seed2-fable`. Claude Fable 5.2 max, Mac mini worker 2, pinned at commit 767a6b4e5. Started 2026-11-21T11:35Z (date -u). Author only; checked by no one. Research-stage working state; grants no status. Independent of row 1363, which this file does not read.

## 0. The problem, and the plan of this file

**Problem (row 1364).** In the coupling range of `library/gap-phys-seed.md` (beta_0 <= beta_j <= B_0 log(L/a_j)), uniformly in the cutoff and the volume, show that the neutral transfer kernel over some fixed physical time w satisfies s(2w) <= 4/21 (the rank-one test (M-neutral) at tolerance 2/5; row 1356 Lemma M1 and Corollary M2, checked by row 1359). Or disprove (M-neutral) for the Wilson trajectory, or a step of the chain that consumes it.

**Labels.** PROVED, ARGUED, GUIDE, OPEN, as the row asks.

**Plan.** Step 1: read the exact statements the row names (gap-phys-seed, rows 1342, 1349, 1353, 1356 and their checks) and write the precise target. Step 2: prior-identity and route screening (memory of this lane: 32 route families on file; rows 1351-1362). Step 3: choose one attack and carry it. Each step is appended below before the next begins.

(Sections follow as the work proceeds.)
