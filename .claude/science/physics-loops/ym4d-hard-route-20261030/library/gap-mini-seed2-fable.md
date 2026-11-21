lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T23:35Z

# The neutral seed for the SU(2) Wilson trajectory at late cutoffs: attempt 2 (row 1364)

Queue row 1364, `gap-mini-seed2-fable`. Claude Fable 5.2 max, Mac mini worker 2, pinned at commit 767a6b4e5. Started 2026-11-21T11:35Z (date -u). Author only; checked by no one. Research-stage working state; grants no status. Independent of row 1363, which this file does not read.

## 0. The problem, and the plan of this file

**Problem (row 1364).** In the coupling range of `library/gap-phys-seed.md` (beta_0 <= beta_j <= B_0 log(L/a_j)), uniformly in the cutoff and the volume, show that the neutral transfer kernel over some fixed physical time w satisfies s(2w) <= 4/21 (the rank-one test (M-neutral) at tolerance 2/5; row 1356 Lemma M1 and Corollary M2, checked by row 1359). Or disprove (M-neutral) for the Wilson trajectory, or a step of the chain that consumes it.

**Labels.** PROVED, ARGUED, GUIDE, OPEN, as the row asks.

**Plan.** Step 1: read the exact statements the row names (gap-phys-seed, rows 1342, 1349, 1353, 1356 and their checks) and write the precise target. Step 2: prior-identity and route screening (memory of this lane: 32 route families on file; rows 1351-1362). Step 3: choose one attack and carry it. Each step is appended below before the next begins.

(Sections follow as the work proceeds.)

## 1. The target, exactly (written 11:44Z, date -u)

Read for this section: GOAL.md; FINISH.md L1-84, L299-356 and the rows 754, 755, 760, 842, 862, 1007, 1009, 1010, 1342, 1349, 1353, 1355, 1356, 1359-1364; `parts/gap.md` L8-104 and L223-320; `library/gap-phys-seed.md` L280-330 (Lemma Z3, Theorems ZD and ZD-c, the two lead notes); `library/gap-mini-mneutral-fable.md` L1-130 (Lemma M1, Corollary M2); `library/gap-mini-neutral-step-fable.md` L52-72 and L380-412 ((N-phys), Corollary BT2).

Notation (row 1353, 2.1 and 6.1; row 1356, Section 2). The spatial box is the periodic lattice n^3. T is the Wilson transfer operator on the gauge-invariant functions of the slice configurations. P_0 is the mean of the eight centre translations. lambda_0 is the vacuum eigenvalue. x_a = lambda_a/lambda_0, a >= 1, are the relative eigenvalues of the neutral sector (electric flux zero, magnetic twist zero). s(u) = sum over a >= 1 of x_a^u.

- (N-phys): there is an admissible physical side L such that for all late j: 4 divides n_j, n_j >= 2^70, and there is an integer u_j with 3 <= u_j <= n_j/512 and s_j(u_j; n_j^3) <= 1/2.
- (M-neutral) at tolerance 2/5 is s(2w) <= 4/21 at some w <= n/1024 (row 1356, Corollary M2 (i); check row 1359). It gives (N-phys) with no loss in the time, and (N-phys) gives it at w >= 3u/2.
- With Z_+(t) = Tr(P_0 T^t) = lambda_0^t (1 + s(t)): 1 + s(u) <= Z_+(u)^2/Z_+(2u) (Lemma TP of row 1342).

Reading in thermal terms (on file: Lemma Z, Lemma Z', Proposition Delta, rows 1180 and 1184; not new). The number log(1 + s(u)) is the volume n^3 times the thermal pressure of the neutral sector at the temperature 1/u, in units of that temperature. A free gas of three massless vector particles has pressure (pi^2/15) T^4, so it gives log(1 + s) about 0.66 (n/u)^3, at least 0.66 x 512^3. (N-phys) asks for log(3/2) = 0.405. For a massive particle of mass m the one-particle term is n^3 (m/(2 pi u))^(3/2) e^(-m u); at n = 512 u it is below 1/2 once m u is at least about 22, so the physical side is L at least about 1.1 x 10^4/m (my arithmetic, GUIDE). So the seed is a low-temperature statement far above the correlation length. It is not a statement at the scale where the running coupling is small.

