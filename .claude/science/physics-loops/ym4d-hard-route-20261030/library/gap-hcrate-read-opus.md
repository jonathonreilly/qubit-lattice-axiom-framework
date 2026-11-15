lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T12:32Z

# gap-hcrate-read-opus (FINISH row 983): reading refutation test of gap-ladder-max 5.6 (b) against SU(2) lattice thermodynamics

Pinned commit: 8c5ce1366 (branch claude/ym4d-hard-route). Started 2026-11-15T00:32Z.

## Plan (at most eight steps)

1. Read FINISH.md rules, GOAL.md, row 983, row 978 N5, and `library/gap-ladder-max.md` 5.6 (b); copy the N5 criteria verbatim into this file before any number.
2. Fix the exact test: what pi(t) is, what t and m are, what alpha/m_0++ is, how the inequality pi(t+2m) <= (1 - tanh(alpha m)) pi(t) reads in terms of p/T^4 or epsilon/T^4 vs T/T_c; check open-core and FINISH rows for overlap.
3. Locate published SU(2) thermodynamics sources (Engels et al. 1995; Caselle et al. 2015 / Giusti-Pepe 2016; Borsanyi et al. 2022 SU(2) EoS) by URL; fetch into own /tmp folder.
4. Extract the pressure/energy-density tables with quoted errors, continuum-extrapolated where given.
5. Need m_0++/T_c for SU(2) (Lucini-Teper-Wenger) to convert m into a T/T_c step; record value with error.
6. Evaluate the inequality on all pairs in the measured range: list violations > 2 sigma (REFUTES), else the largest alpha/m_0++ consistent (upper bound on M_H/m_0++).
7. Cross-check by a second derivation path (different source table or epsilon vs p) where available.
8. Verdict and RESULT line.

## Step log

### Step 1. Criteria and the test, copied before any number

**N5 criteria, copied verbatim from `library/gap-ladder-max.md` 8.4 (row 978), before reading any number:**

> **N5, GUIDE, optional (reading, no simulation).** From published SU(2) thermodynamics (pressure and energy density against T/T_c), evaluate the test of 5.6 (b): the largest alpha/m_0++ with pi(t + 2m) <= (1 - tanh(alpha m)) pi(t) on the measured range. Criteria before reading: REFUTES a rate M_H if one pair of temperatures violates the inequality by more than twice the quoted error; otherwise it gives an upper bound on M_H/m_0++ and decides nothing else. It can only lower the M_H that N2 may aim at.

Row 983 repeats them: "REFUTES a rate M_H if one pair of temperatures violates the inequality by more than twice the quoted error; otherwise it gives an upper bound on M_H/m_0++ and decides nothing else."

**Status of the test itself.** `gap-ladder-max.md` 5.6 (b) is labelled ARGUED (author Fable, checked by no one). It rests on Lemma IHC (PROVED by hand there, unchecked) and on the existence of pi(t) = lim_B X(t; B)/|B| (sub-additivity, not rebuilt). This row does not check either. Everything below is GUIDE: a reading of published numerics. By GOAL.md it can refute or guide and never discharges.

**Duplicate check (rule 0a).** Grep of `library/open-core.md` and FINISH rows for pressure, thermodynamic, interaction measure, Engels, Borsanyi, Caselle: no row reads SU(2) equation-of-state data. Rows 931 (`gap-direction-max.md` (ANOM)) and 978 use the interaction measure only as recalled physics. No overlap. This row attacks no open lemma; it is a reading test.

**Repo search.** `library/gap-direction-max.md` 190-210 (the seed as an integrated relative interaction measure, recalled), `library/gap-glue-max.md` 169-170 (SU(2) glueball-gas and gluon-gas regimes, GUIDE). Neither quotes a table.

### Step 2. The test in physical units; algebra by hand

**Identification.** X(t; B) = log Z(B x t) - t log lambda_0(B) = log(1 + S(t; B)) (`gap-ladder-max.md` 5.1-5.2). With lattice spacing a, temperature T = 1/(t a), volume V = |B| a^3, the vacuum-subtracted pressure is p = (T/V) X in the infinite-volume limit. So

  pi(t) = lim X/|B| = a^3 p/T = (p/T^4) (a T)^3 = (p/T^4)(T) / t^3.

This is the "pi ~ t^(-3)" of 5.6 (b) when p/T^4 is constant. The normalisation p(T = 0) = 0 is the vacuum subtraction in X; published data use the same normalisation (p from integrating the interaction measure from a low T_0 where p is set to zero).

**The pair test.** Take two time extents t < t + 2m at one spacing a. Put T_1 = 1/(t a) > T_2 = 1/((t + 2m) a) and Delta tau := 1/T_2 - 1/T_1 = 2 m a. With alpha = M_H a (Corollary CU's (HC-phys)), alpha m = M_H Delta tau/2, and 1 - tanh(x/2) = 2/(1 + e^x). The test reads

  (T)   R := (p(T_2)/T_2)/(p(T_1)/T_1) <= 2/(1 + e^(M_H Delta tau)),

that is, (T) holds iff

  M_H <= B(T_1, T_2) := log(2/R - 1)/Delta tau,

with B = +infinity when R <= 0 (p(T_2) = 0, the confined side) and B < 0 impossible since R < 1 (p/T is strictly increasing: d(p/T)/dT = eps/T^2 > 0). So **every pair gives an upper bound B(T_1, T_2) on M_H, and the largest admissible rate is M_H^max = inf over measured pairs of B.** In units of m_0++: M_H^max/m_0++ = (T_c/m_0++) inf B/T_c, with B/T_c = log(2/R - 1)/(T_c/T_2 - T_c/T_1).

**REFUTES criterion in these terms.** A given M_H is refuted if some pair has M_H > B(T_1, T_2) by more than twice the error of B propagated from the quoted errors of p/T^4 at T_1 and T_2 (equivalently: R exceeds 2/(1 + e^(M_H Delta tau)) by more than 2 sigma_R). Correlated errors between the two temperatures (same integration path) make the uncorrelated propagation conservative for a difference and I note it where it matters.

**Local form (small Delta tau).** With T_2 = T - dT, T_1 = T: Delta tau = dT/T^2, 2/R - 1 = 1 + 2 (eps/(T p)) dT + O(dT^2), so B -> 2 T eps/p = 2 T (3 + I/p), I = eps - 3p the interaction measure. This is 5.6 (b)'s local form. Since I >= 0 in the deconfined phase, B_local >= 6 T >= 6 T_c there.

**Large steps.** For T_1 -> infinity at fixed T_2, p_1/T_1 grows like T_1^3, R -> 0, and B -> +infinity. So long steps are harmless; the tight pairs are at T_2 between T_c and a few T_c, with Delta tau T_c of order 0.1-0.5.

**Lattice caveat.** The inequality holds at one fixed spacing a with t and t + 2m both even. Continuum-extrapolated p/T^4(T/T_c) is the a -> 0 value of the left side, and pairs (T_1, T_2) then range over a continuum, so I evaluate (T) on continuum data at the tabulated temperatures. Data at fixed N_t (varying beta) are not the fixed-a pairs of the test; they enter only through their continuum extrapolation, or as a cross-check with their cutoff effects counted as error.

### Step 3. Sources

Fetched from arXiv (API search, then e-print TeX) into `/tmp/hcrate983/src_<id>/`, outside git; read with grep/sed and python3 -I. Nothing committed.

| Source | What it gives | Continuum? |
|---|---|---|
| T. Hirakida, E. Itou, H. Kouno, "Thermodynamics for pure SU(2) gauge theory using gradient flow", PTEP 2019 033B01, arXiv:1805.07106 (v5) | Table "Data of thermodynamic quantities" (Appendix, label `table:thermo-data`): Delta/T^4, s/T^3, eps/T^4, P/T^4 at T/T_c = 0.95, 0.98, 1.01, 1.04, 1.08, 1.12, 1.28, 1.50, 1.76, 2.07, "The errors are statistical ones." | Yes: double limit (a, t) -> (0, 0), Wilson action, N_tau = 8, 10, 12 (6 at 2.07). Text: systematic error of Delta about equal to the statistical one; of s "at most three times" the statistical one; Lambda_MSbar uncertainty moves s by at most 6 percent. |
| P. Giudice, S. Piemonte, "Improved thermodynamics of SU(2) gauge theory", EPJC 77 (2017) 821, arXiv:1708.01216 | Symanzik-improved action, integral method, N_tau = 4, 5; data as xmgrace files in `anc/` (pressure, trace anomaly, energy density, entropy) | No (fixed N_tau = 5, stated "close to the continuum limit"). Cross-check only. |
| M. Caselle, A. Nada, M. Panero, "Hagedorn spectrum and thermodynamics of SU(2) and SU(3) Yang-Mills theories", JHEP 07 (2015) 143, arXiv:1505.01106 | Wilson action, integral method; Hirakida et al. say it "takes the continuum extrapolation" | To be read in Step 4. |

**A misprint in the Hirakida table, repaired by an identity.** The row T/T_c = 1.12 lists P/T^4 = 0.772(69). The same row has s/T^3 = 1.18(2), eps/T^4 = 1.10(1), Delta/T^4 = 0.871(13). The identities s/T^3 = (eps + P)/T^4 and Delta = eps - 3P give P/T^4 = 0.08 and 0.076. So the entry is 0.0772(69): a dropped zero. Every other row satisfies both identities within its errors (checked by hand: 1.28: 1.38 + 0.188 = 1.568 vs 1.57; 1.50: 1.51 + 0.298 = 1.808 vs 1.81; 1.76: 1.56 + 0.365 = 1.925 vs 1.92; 2.07: 1.67 + 0.451 = 2.121 vs 2.12). I use 0.0772(69).

**What these sources cannot give.** All of them stop at T/T_c about 2 to 3 (Hirakida at 2.07). The test is tightest at T_2 from about 1.1 to 2 T_c (Step 2), so the range is adequate for the infimum. Below T_c every source has P/T^4 consistent with zero, so pairs with T_2 <= T_c carry no constraint (B = +infinity within error).

### Step 5 (done before Step 4's evaluation). The unit m_0++/T_c

- T_c/sqrt(sigma) = 0.7091(36), SU(2), continuum, fit range L_t in [3, 8]: B. Lucini, M. Teper, U. Wenger, "The high temperature phase transition in SU(N) gauge theories", JHEP 01 (2004) 061, arXiv:hep-lat/0307017, table of lim_(a -> 0) T_c/sqrt(sigma). Caselle-Nada-Panero use the same value.
- m_0++/sqrt(sigma) = 3.78(7), SU(2), continuum: B. Lucini, M. Teper, U. Wenger, "Glueballs and k-strings in SU(N) gauge theories: calculations with improved operators", JHEP 06 (2004) 012, arXiv:hep-lat/0404008, Table `table_continuumG` ("The continuum limit of the lightest scalar and tensor glueball masses"). Same table: m_2++/sqrt(sigma) = 5.45(11), m_0++*/sqrt(sigma) = 6.46(14).
- Cross-check, independent data set: M. Teper, arXiv:hep-th/9812187 (review): m_0++/sqrt(sigma) = 3.74(12), T_c/sqrt(sigma) = 0.694(18).

**Value used:** m_0++/T_c = 3.78/0.7091 = 5.33, relative errors 1.9 and 0.5 percent added in quadrature: **m_0++/T_c = 5.33(10)**. Teper 1998 gives 5.39(23). The recalled "about 5.2" of `gap-ladder-max.md` 5.6 (b) is 1.3 sigma low; that matters there, because the idealised test of 5.6 (b) turned negative at r = 5.25.
Also: 2 m_0++/T_c = 10.66(20); m_2++/T_c = 7.69(16).

Hirakida et al. state T_c/sqrt(sigma) = 0.69(2) for their conversion to Lambda (Fingberg et al.); their T/T_c axis comes from their own scale setting, so the m_0++ unit is not tied to their sigma.

### Step 4. Data used (continuum, Hirakida-Itou-Kouno 2019)

From the table `table:thermo-data` of arXiv:1805.07106 (statistical errors only), T in units of T_c:

| T/T_c | 0.95 | 0.98 | 1.01 | 1.04 | 1.08 | 1.12 | 1.28 | 1.50 | 1.76 | 2.07 |
|---|---|---|---|---|---|---|---|---|---|---|
| P/T^4 | -0.0035(104) | -0.0145(87) | 0.0085(74) | 0.0054(102) | 0.0217(93) | 0.0772(69)* | 0.188(7) | 0.298(8) | 0.365(9) | 0.451(10) |
| eps/T^4 | 0.235(24) | 0.322(24) | 0.576(18) | 0.838(21) | 0.909(23) | 1.10(1) | 1.38(1) | 1.51(2) | 1.56(2) | 1.67(3) |

(* misprint repaired, Step 3.) Up to 1.08 T_c the pressure is zero within 2.3 sigma. Systematic errors are not in the table; the paper says the systematic error of the trace anomaly is about the statistical one and that of s/T^3 at most three times it. I model this by scaling all pressure errors by k = 1, 2, 3.

### Step 6. Evaluation of the pair test (GUIDE run; arithmetic only)

Run: `/tmp/hcrate983/scripts/pairs.py` and `pairs2.py`, under `numeric-lock` (holder hcrate983-worker2), memory 70 percent free, a few seconds; logs `/tmp/hcrate983/pairs.log`, `pairs2.log` (outside git). Errors of R propagated linearly, uncorrelated between the two temperatures. All 45 pairs T_2 < T_1 of the table.

**Tightest pairs (B = log(2/R - 1)/Delta tau, units T_c and m_0++ = 5.33 T_c):**

| T_2 | T_1 | R | Delta tau T_c | B/T_c | B/m_0++ | z at M_H = m_0++ | z at M_H = 2 m_0++ |
|---|---|---|---|---|---|---|---|
| 1.28 | 2.07 | 0.0986(43) | 0.298 | 9.93(15) | 1.86 | -56 | +4.4 |
| 1.28 | 1.76 | 0.198(9) | 0.213 | 10.36(23) | 1.94 | -33 | +1.3 |
| 1.12 | 2.07 | 0.0271(25) | 0.410 | 10.46(23) | 1.96 | -70 | +0.8 |
| 1.50 | 2.07 | 0.251(9) | 0.184 | 10.57(22) | 1.98 | -34 | +0.4 |
| 1.50 | 1.76 | 0.505(18) | 0.099 | 11.01(50) | 2.07 | -13 | -0.7 |
| 1.12 | 1.76 | 0.0545(51) | 0.325 | 11.01(29) | 2.07 | -49 | -1.3 |

z = (R - 2/(1 + e^(M_H Delta tau)))/sigma_R; z > 2 means the pair violates the inequality by more than twice the quoted error.

**Hand check of the top row** (independent of the script): p/T at 1.28 is 0.188 x 1.28^3 = 0.188 x 2.0972 = 0.3943; at 2.07 it is 0.451 x 8.8698 = 4.0003. R = 0.0986. 2/R - 1 = 19.29, log = 2.960. Delta tau = 1/1.28 - 1/2.07 = 0.78125 - 0.48309 = 0.29816. B = 9.93 T_c. Agrees.

**Local form, 2 T eps/p:** 31.9 T_c at 1.12, 18.8 at 1.28, 15.2 at 1.50, 15.0 at 1.76, 15.3 at 2.07 (2.8 to 6 m_0++). The finite steps are tighter than the local form by a factor of about 1.5, as Step 2 predicted (the tight pairs have T_2/T_1 about 0.6 to 0.7).

**Pairs with R > 1** (would refute every M_H > 0): only (1.01, 1.04), R = 1.43(2.96), z = 0.15. Noise at zero pressure, not a violation.

**Confined side.** Pairs with T_2 <= 1.08 have p(T_2) zero within error; R - 2 sigma_R < 0 and B = +infinity at the 2 sigma level. They constrain nothing.

**Result of the criterion.**
- **M_H = m_0++: not refuted.** Every pair passes; the closest has z = -13 (k = 1).
- **Largest rate passing every pair at 2 sigma** (M_H > B(R - 2 sigma_R) is refuted by that pair): 10.25 T_c = **1.92 m_0++** (k = 1), 1.99 m_0++ (k = 2), 2.06 m_0++ (k = 3); always the pair (1.28, 2.07). The unit adds 2 percent (m_0++/T_c = 5.33(10)).
- **M_H = 2 m_0++ is refuted at the statistical level** (z = 4.4 at the pair (1.28, 2.07), k = 1), but **not** once systematics are counted at the size the authors state (k = 3 gives the bound 2.06 m_0++). I record it as: 2 m_0++ is at the edge of the data; nothing below about 1.9 m_0++ is touched.

### Step 7. Cross-check on a second data path (Giudice-Piemonte 2017)

Different action (tree-level Symanzik improved), different method (integral method, not the gradient-flow energy-momentum tensor), different scale setting (their own beta-function), and a range up to 6.4 T_c. Data: the ancillary file `anc/plot_pressure_norm.agr` of arXiv:1708.01216 (columns T/T_c, p/p_SB, error of T/T_c, error of p/p_SB; N_tau = 4: 123 points to 4.59 T_c; N_tau = 5: 135 points to 6.40 T_c). The SB normalisation is one constant at fixed N_tau, so it cancels in R. These are fixed-N_tau data, not fixed-a pairs, so this is a cross-check with cutoff effects in the error, as said in Step 2. Run `/tmp/hcrate983/scripts/gp_pairs.py` under the numeric lock (seconds); log `/tmp/hcrate983/gp_pairs.log`.

| | N_tau = 4 | N_tau = 5 |
|---|---|---|
| Pairs refuting M_H = m_0++ at more than 2 sigma | 0 | 0 |
| inf B over pairs | 9.36 T_c = 1.756 m_0++ (T_2 = 1.28, T_1 = 2.82) | 9.35 T_c = 1.754 m_0++ (T_2 = 1.27, T_1 = 2.81) |
| largest rate passing every pair at 2 sigma, B(R - 2 sigma_R) | 9.39 T_c = 1.76 m_0++ | 9.38 T_c = 1.76 m_0++ |

min over T_1 of B, as a function of T_2 (N_tau = 5): 11.0 T_c at 1.03, 9.5 at 1.17, **9.4 at 1.24-1.33**, 9.8 at 1.51, 10.5 at 1.73, 11.6 at 1.97, 13.6 at 2.41, 16.3 at 2.95, 21.0 at 3.86, 27.6 at 5.06. Above 2 T_c this grows like about 5.5 T_2, the Stefan-Boltzmann shape of Step 2 (5.25 T_2 for p/T^4 constant). So **the infimum sits at T_2 about 1.3 T_c and is inside the measured range**; temperatures above 6 T_c cannot lower it.

**Error not in the quoted p errors.** The error of T/T_c (from the beta-function) is 0.9 percent at 1.27 and 3 percent at 2.8 T_c, mostly common to both points. A common scale shift lambda multiplies B/T_c by lambda, so B moves by about 3 percent: 9.35(30) T_c = 1.75(6) m_0++ with the unit's error included.

**Agreement between the two paths.** Hirakida's continuum table reaches only 2.07 T_c, so its tightest pair (1.28, 2.07) gives 9.93 T_c. Giudice-Piemonte's pair at the same temperatures: B at T_2 = 1.27, T_1 about 2.08 is not printed above; Hirakida's p/p_SB at 2.07 is 0.451/0.658 = 0.685 against 0.679 for Giudice-Piemonte N_tau = 5 at 2.08, and 0.286 at 1.28 T_c against 0.287 for N_tau = 5 at 1.265 T_c (nearest point). So the two sources agree there, and the lower infimum of Giudice-Piemonte comes from its longer range (T_1 about 2.8 T_c), not from a disagreement. My hand estimate before this run, with p/T^4 extrapolated to 0.52 at 3 T_c, was 9.5 T_c at (1.28, 3); the run gives 9.36.

### Step 8. Verdicts

All of this is GUIDE (a reading of published numerics plus seconds of arithmetic). It discharges nothing and enters no proof.

**V1. No rate up to the gap is refuted.** For every M_H <= m_0++, every pair of measured temperatures satisfies pi(t + 2m) <= (1 - tanh(alpha m)) pi(t). Continuum data (Hirakida-Itou-Kouno, 0.95 to 2.07 T_c): the closest pair is 13 sigma inside. Second data path (Giudice-Piemonte, N_tau = 4 and 5, to 6.4 T_c): no pair violates at 2 sigma. **Verdict on M_H = m_0++: NOT REFUTED.**

**V2. Upper bound on M_H/m_0++ (the only other thing the test decides).**
- Continuum table, measured range to 2.07 T_c: M_H/m_0++ <= 1.92 at 2 sigma with statistical errors; <= 2.06 with errors tripled for the stated systematics. Tightest pair (1.28, 2.07) T_c.
- Giudice-Piemonte, range to 6.4 T_c: **M_H/m_0++ <= 1.75(6)**, the same at N_tau = 4 and 5 (9.36 and 9.35 T_c), pair about (1.27, 2.8) T_c; error from the T/T_c scale (3 percent) and the unit (2 percent).
- So rates above about 1.8 m_0++ are REFUTED in the sense of the criterion (one pair violates by much more than twice the quoted error): with Giudice-Piemonte at M_H = 2 m_0++, R = 0.0339(2) against the threshold 0.0193 at the pair (1.265, 2.807); a common 3 percent shift of T/T_c moves B only to 9.6 T_c < 10.66 T_c. In the continuum table alone, 2 m_0++ is refuted at 4.4 sigma (statistical) and not once systematics are tripled.

**V3. What it changes for the lane: nothing on N2's target.** By the necessity remark of `gap-ladder-max.md` 5.1 (Lemma RATE (c)), a rate needs E_1(B) >= alpha, so M_H <= m_0++ already in the infinite-volume limit (RECALLED physics: E_1 of large boxes tends to the 0++ glueball mass; torelon levels grow with the box). The thermodynamic bound, about 1.75 m_0++, is weaker. So the test "can only lower the M_H that N2 may aim at" and here it does not lower it. It is a consistency check that passes with a factor of about 1.75 to spare.

**V4. A correction to 5.6 (b) of `gap-ladder-max.md`.** The recalled value "m_0++/T_c about 5.2" is low: the continuum values give **5.33(10)** (Step 5). With r = 5.33 the idealised law of 5.6 (b) (pi ~ t^(-3) up to N_c) fails: g(0.3) = log(2/(1 + e^1.599)) - 3 log 0.7 = -1.090 + 1.070 = -0.020 (hand arithmetic; e^1.599 = 4.948). So under the idealised law the test would refute a rate equal to the gap. The real pressure saves it: near T_c it is far below the Stefan-Boltzmann value (p/T^4 = 0.19 at 1.28 T_c against 0.66), exactly the "room" that 5.6 (b) ARGUED. The margin is not close: the infimum is reached at T_2 about 1.3 T_c, and there B is about 1.75 m_0++.

**V5. Where the bound comes from.** The local form 2 T eps/p is 15 to 19 T_c on 1.3 to 2 T_c (2.8 to 3.5 m_0++). Finite steps with T_2/T_1 about 0.45 to 0.7 are tighter by a factor of about 1.6, and pairs with T_2 at or below 1.08 T_c constrain nothing (zero pressure within error). The glueball gas below T_c would give B near m_0++ only as T_2 -> 0, where no data has a non-zero pressure.

**What this run did not cover.**
- Lemma IHC and 5.6 (b) are taken as written (unchecked here; N1 of row 978 checks them). The existence of pi(t) and the passage from fixed-a pairs to continuum data are not rebuilt.
- Fixed-N_tau data (Giudice-Piemonte) are not fixed-a pairs; their cutoff effect is bounded only by the N_tau = 4 vs 5 agreement (0.1 percent in B).
- Error correlations between temperatures were not available; uncorrelated propagation was used.
- The Sussman-Alpoge repository was not read: this row is about lattice thermodynamics, which their account does not tabulate. Credit for the data: Hirakida, Itou, Kouno (PTEP 2019 033B01); Giudice, Piemonte (EPJC 77 (2017) 821); Lucini, Teper, Wenger (JHEP 01 (2004) 061; JHEP 06 (2004) 012); Teper (hep-th/9812187). Caselle, Nada, Panero (JHEP 07 (2015) 143) was read and covers only T <= T_c, where the test is empty.
- Nothing was committed or pushed; downloads and scripts are in `/tmp/hcrate983/` (outside git).

RESULT: Row 983 (Claude Opus 5.5 high, Mac mini worker 2; GUIDE reading, checked by no one; seconds of arithmetic under numeric-lock): the test of gap-ladder-max 5.6 (b) on published SU(2) thermodynamics does NOT REFUTE any hypercontractive rate M_H <= m_0++ (continuum data of Hirakida-Itou-Kouno to 2.07 T_c, closest pair 13 sigma inside; Giudice-Piemonte N_tau = 4, 5 to 6.4 T_c, no pair violates); it bounds M_H/m_0++ <= 1.75(6) (Giudice-Piemonte; continuum table alone <= 1.92 statistical, <= 2.06 with systematics), tightest pair about (1.3, 2.8) T_c, so rates above about 1.8 m_0++ are refuted; this is weaker than the spectral necessity M_H <= m_0++ and changes nothing for N2; correction to 5.6 (b): m_0++/T_c = 5.33(10), not about 5.2, so the idealised t^(-3) law would fail at the gap (g(0.3) = -0.020) and only the real suppressed pressure near T_c gives the margin. OPEN, untouched here: Lemma IHC check (N1), (HC-phys), and every statement 5.6 (b) leaves ARGUED.
