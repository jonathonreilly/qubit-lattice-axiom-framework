lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T04:29Z

# Gate: NT2 (queue item 8e) at 2285befef

**Provenance.** Reviewer anthropic/claude-opus-5-5, effort high, Mac mini worker, neutral side, commit 2285befef. The text under review was written by openai/gpt-6-astra/max, so the model differs from the author's, but this is one model's reading, not an audit, and it grants no status. Criteria were written before any run: `checks/gate_nt2/CRITERIA.md`. New lemmas: `library/nt2-coherence-and-positive-norm.md`.

**Result.** The arithmetic of Text 8 is right. Library A, B, C, D, the restricted Theorem 4.3 and (COV8) hold at their stated scope. Three things change the reading:

1. The clause |K_vert(tau_*)| >= kappa_* has no chart-free meaning.
2. The consistency equation is not what stands between L3 and a coherent law.
3. L1's rejection does not apply to any coherent law. The running clause does the rejecting, and only for positive-norm potentials.

## 1. Verdicts

| Statement | Verdict | Note |
|---|---|---|
| NT2, Text 8.1, as a necessary ultraviolet test on a state | CORRECT-NO-ADVANCE | Well posed apart from D2, D5. Not an identification on its own: D1. Text 8.1 says so itself, but places the boundary wrongly. |
| (NT2-C) formulas: K_comp, K_vert sign, C_B, C_Gamma, 3/2 factors | ADVANCE | C1a from exact SU(2) products. All normalizations by hand. |
| (NT2-g), (NT2-R), b_W = 11/(3 pi^2), g_YM = 2g | ADVANCE | Agrees with both producers' stated coefficient, in the same normalization. |
| Clause |K_vert(tau_*)| >= kappa_* | CORRECT-NO-ADVANCE | Depends on an unnamed chart: D2. Nothing may rest on it as written. |
| L1 | CORRECT-NO-ADVANCE | Algebra exact (C3a, C3c). The family rejected is not coherent: D3. |
| L2 | ADVANCE | Fixed global amplitude survives blocking. |
| L3, finite cutoff, (B1)-(B3) | ADVANCE | C2a; the evenness argument for O(h^6) stands. |
| L3, "the missing equation is (B4)" | CORRECT-NO-ADVANCE | (B4) is free: D1. The coherent law stays unproved, now conditional on one-step statements only. |
| Dilation mixture, library D | ADVANCE | Every step checked. One hypothesis can be dropped: D6. |
| Stepwise running counterexample, library A | ADVANCE | u differences oscillate by 2c about the mean. |
| Restricted Theorem 4.3, recursion (4)-(5) | ADVANCE, as an implication | Stands at each step. Hypotheses (G0), (3) unproved, and they are the content. |
| Sigma_+, Sigma_-, formula (6), the failure of the old proof | ADVANCE | C3b: 15 pairings, difference exactly 48 a^3. |
| (COV8), (C-1) to (C-3), CT2 implies finite-window COV8 | ADVANCE, as a reduction | See Note under D6 for a simpler repair. |
| `library/witness-running-tests.md` as a whole | Holds at stated scope | Boundary sentence of section B: D1. Scope of section C: D3. |

## 2. Defects

**D1. The coherent L3 is not stopped by consistency (High). `library/witness-running-tests.md` lines 94-105, Text 8.2 row L3, Text 8.5.** Claimed: M_* mu_(m+1) = mu_m is the missing equation. It costs nothing. Any fine law blocked down solves it, and any kernel on the fibres of a deterministic M, applied top-down from a coarse law, solves it exactly with no limit (Lemma C).

The real need is a law whose fine modes carry less amplitude than its coarse modes. The top-down law mu^TD does this: conditional Wilson on each fibre at a prescribed gamma_j, discarding the factor that drives the true flow. Proposition TD: given only the one-step package read for that law, (NT2-M) holds, for any chosen sequence gamma_j. So b_W is an input and passes, and any other b passes (NT2-M) too.

This improves on the dilation mixture as a test of sufficiency, since it presupposes no solution of NT2. Status: implication. The one-step package is unverified for mu^TD, H-MOM especially, because its chessboard source needs RP.

Consequence for GOAL: without RP, the running clause excludes no law of this type, and no moment-matching clause can, because the running is chosen. RP and locality are the only handles. T1 has RP and Text 8.1 does not state it. Repair, unproved: state NT2 on the RP gauge-invariant state of T1, and record whether mu^TD is RP on gauge-invariant functions as the open test. I expect not.

**D2. K_vert has no chart-free value (High). Text 8.1, "|K_vert(tau_*)|>=kappa_*"; H-TREE; `library/witness-blocked-tree-limit.md` (NV), (REG-T).** The text says the split fails under nonlinear field redefinitions. It already fails under linear colour-diagonal gauge slices, by the part's own Proposition 2.2. Box 3^4, corner triple:

| Chart | K_comp | K_vert | K_T |
|---|---|---|---|
| Landau | 0.36466 | 0.26135 | 0.62600469 |
| Maximal tree 1 | 0.58922 | 0.03679 | 0.62600469 |
| Maximal tree 2 | 0.45395 | 0.17205 | 0.62600469 |
| Rank-one slice, Lemma K | 0.62600 | 0.00000 | 0.62600469 |

Lemma K gives a family of linear slices on which K_vert(tau_*) takes every real value, with K_T fixed. "One fixed gauge chart" is unnamed, so the clause has no truth value. Also, (REG-T) "for every coefficient" cannot hold for K_comp, K_vert between a tree chart and periodic Feynman. It can hold for K_T, and for the split only against a Landau-type chart, where E_i is the Feynman solution.

Repair, unproved: drop the clause, keep K_T in (NT2-M), and report the vertex as GOAL says, as a corollary against the named class: for every covariance c some triple in a fixed family has |K_T - K_comp[c]| >= kappa. Theorem 3.16 is the lattice-scale form. It holds for all charts at once, and it needs a family of triples, not one.

**D3. L1 is rejected only as a non-coherent family (Medium). Text 8.2 row L1 and the sentence "caught by positive moment matching", Text 8.5.** The excess sits at the template scale at every m by assumption. A local map of the fine field, which is what the old gate's L1 is, is seen by NT2 through M, and there the excess is irrelevant: normalized slope 3.75, 0.211, 0.0730, 0.0370 at n = 1, 3, 5, 7, about 1.8 / n^2 (Lemma X). The algebra of section C stands, and it is the wrong test for a coherent law. Such a law is rejected elsewhere: D4.

**D4. The running clause does have force, which Text 8.2 misses (Medium, in NT2's favour). Text 8.2 closing paragraph; `library/witness-running-tests.md` line 179.** Text 8.2 notes that a vanishing amplitude removes the moment obstruction and that a prescribed amplitude can run. But a positive-norm potential cannot run to zero. If the transverse two-point function has Kallen-Lehmann form, rho(z) = z D(z) is non-decreasing, so flux variance can only grow as r decreases (Lemma RM). So every O(4)-invariant Proca or Maxwell mixture, one-link local map of an RP Gaussian, and disorder mixture of those fails (NT2-R), whatever the amplitude, and no use of T is needed. This answers GOAL's open question for the old gate's L1, L2. The running L3 has negative spectral density (C3d), so it is not RP on its links. Whether it is RP on gauge-invariant functions is not reached. Scope: O(4) at leading order, not hypercubic alone.

**D5. Admissibility of M is not stated (Low). Text 8.1, "a local, gauge-covariant block kernel M".** Straight decimation is local and gauge covariant, but the free flux variance grows with the cutoff ratio, so (NT2-M) is false for Wilson under it. NT2 needs a smoothing condition, as in (B-5). K_T also depends on the second jet of M, so the value is per attempt, and (B-1) is the first jet of the independent attempt's map only.

**D6. Library D carries an unneeded hypothesis (Low). Lines 186-190.** Dilation covariance is called a further structural assumption. Given "the same M at successive scales" and an offset set closed under L^-1, omega' := omega at level m + 1 satisfies the block identities directly. Clustering is needed only for the plateau (D1 there). So the conditional counterexample needs less than it says.

**Note, not a defect.** Hessian continuity as in (OS_j)(d) naturally bounds the difference of blocks in transported frames, and the difference of norms is a weakening. Restating (d) as ||Gamma_pq(W) - Gamma_pq(1)||_HS would make CT2 unnecessary, if a producer can deliver it. That is a request for the owner of the interface.

## 3. Numerics

All run under the numeric lock, one job at a time, BLAS threads 1, memory free 67 to 69 percent. Every criterion in `CRITERIA.md` passed or was reported as specified. The first run of `nt2_blocked.py` stopped itself at the 2 GB limit at n = 3, S = 16 (`nt2_blocked.log`); the script was rewritten to use less memory and rerun from the start, one process per size, and `nt2_blocked.jsonl` holds that rerun.

| Check | Outcome |
|---|---|
| C1a t_4, -t_3 F_3 from exact group products, N = 120000 | Landau: 0.3529(66), 0.272(22) against 0.3647, 0.2613. Tree 1: 0.554(21), 0.33(22) against 0.5892, 0.0368. Within 4 standard errors. The tree vertex is noisy, so the Landau line carries the sign check. |
| C1b, C1c, C1d, C1e | Table in D2. Idempotence error 1e-14, gradient error 2e-15, K_T change 3e-15. |
| C2a, C2b | (B1) difference -0.036(54). Multi-amplitude Wick weights 0.1467(20) against 0.1430, 1.9 standard errors. |
| C3a to C3d | Exact pass. |
| C4 | n = 1 gives 0.21884, P = 0.5. K_vert(n, S) in Feynman prescription: 0.04146 at n = 3, S = 16; 0.03527 at n = 5, S = 10. Finite-S shifts fit S^-4. |

C4 is evidence for (NV) only in the Landau-type chart, not a bound. Extrapolation in n gives about 0.03, between 0.026 (1/n) and 0.032 (1/n^2), distinct from zero by more than the spread in S. It says nothing on K_comp or K_T for any nonlinear map.

## 4. Attacks that failed

- Sign or factor errors in K_vert, K_comp, B, T, the 3/2 factors, b_W: none found.
- The anomalous factor per block step in a nonlinear M. Gauge covariance at constant field forces unit response, so no Z accumulates for a gauge-invariant law. That is an argument by hand. It need not hold for a gauge-fixed Gaussian fine law.
- Whether a hypercubic symmetry forces K_T(tau_*) = 0. The transposition of axes 1, 2 leaves T unchanged, so no constraint.
- (3) against the free theory: a ~ L^-kappa is consistent with q_0 < 1 at fixed large L, with exponentially local flux kernels. This is plausibility, not a proof of (3).
- The mixture: positivity, block identities, reflection, anchored coupling, plateau (a - a')^2/4, NT1 inheritance all stand.

## 5. Read and not read

Read: `FINISH.md`, `GOAL.md`; `parts/witness.md` state of attack, Obligations, Requests, Text 0, 2.1-2.4, 8.1-8.9; `library/witness-running-tests.md`, `witness-moment-gap.md`, `witness-blocked-tree-limit.md`, `witness-interface-moments.md` in full; `parts/upper-chain.md` (OS_j) statement; lines of `gates/witness-3b7fd4e57.md` on D1, D2. For the coefficient only, grep lines of `parts/hard-core--independent.md` and `parts/hard-core--mapped.md`; one mapped hit printed a proof paragraph of Theorem P1, of which only the stated coefficient is used here. No proof text is carried between attempts.

Not read or not checked: Theorem 4.1 and NT1-NF beyond the statement; `witness-two-separation.md`; Text 8.3 against Jaffe-Witten; (M-1) to (M-3) beyond the statement; Fourier domination proofs in `witness-blocked-tree-limit.md` beyond the factor 24 in (B-8) and the n = 1 values; whether either producer delivers any hypothesis. The one-step package for mu^TD is not verified. RP of mu^TD and of L3 on gauge-invariant functions is open. The bottom-up version of L3 is not claimed.
