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

### Step 1. Criteria and the test, copied before any number (00:40Z)

**N5 criteria, copied verbatim from `library/gap-ladder-max.md` 8.4 (row 978), before reading any number:**

> **N5, GUIDE, optional (reading, no simulation).** From published SU(2) thermodynamics (pressure and energy density against T/T_c), evaluate the test of 5.6 (b): the largest alpha/m_0++ with pi(t + 2m) <= (1 - tanh(alpha m)) pi(t) on the measured range. Criteria before reading: REFUTES a rate M_H if one pair of temperatures violates the inequality by more than twice the quoted error; otherwise it gives an upper bound on M_H/m_0++ and decides nothing else. It can only lower the M_H that N2 may aim at.

Row 983 repeats them: "REFUTES a rate M_H if one pair of temperatures violates the inequality by more than twice the quoted error; otherwise it gives an upper bound on M_H/m_0++ and decides nothing else."

**Status of the test itself.** `gap-ladder-max.md` 5.6 (b) is labelled ARGUED (author Fable, checked by no one). It rests on Lemma IHC (PROVED by hand there, unchecked) and on the existence of pi(t) = lim_B X(t; B)/|B| (sub-additivity, not rebuilt). This row does not check either. Everything below is GUIDE: a reading of published numerics. By GOAL.md it can refute or guide and never discharges.

**Duplicate check (rule 0a).** Grep of `library/open-core.md` and FINISH rows for pressure, thermodynamic, interaction measure, Engels, Borsanyi, Caselle: no row reads SU(2) equation-of-state data. Rows 931 (`gap-direction-max.md` (ANOM)) and 978 use the interaction measure only as recalled physics. No overlap. This row attacks no open lemma; it is a reading test.

**Repo search.** `library/gap-direction-max.md` 190-210 (the seed as an integrated relative interaction measure, recalled), `library/gap-glue-max.md` 169-170 (SU(2) glueball-gas and gluon-gas regimes, GUIDE). Neither quotes a table.

### Step 2. The test in physical units (00:45Z; algebra by hand)

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

### Step 3. Sources (01:00Z)

Fetched from arXiv (API search, then e-print TeX) into `/tmp/hcrate983/src_<id>/`, outside git; read with grep/sed and python3 -I. Nothing committed.

| Source | What it gives | Continuum? |
|---|---|---|
| T. Hirakida, E. Itou, H. Kouno, "Thermodynamics for pure SU(2) gauge theory using gradient flow", PTEP 2019 033B01, arXiv:1805.07106 (v5) | Table "Data of thermodynamic quantities" (Appendix, label `table:thermo-data`): Delta/T^4, s/T^3, eps/T^4, P/T^4 at T/T_c = 0.95, 0.98, 1.01, 1.04, 1.08, 1.12, 1.28, 1.50, 1.76, 2.07, "The errors are statistical ones." | Yes: double limit (a, t) -> (0, 0), Wilson action, N_tau = 8, 10, 12 (6 at 2.07). Text: systematic error of Delta about equal to the statistical one; of s "at most three times" the statistical one; Lambda_MSbar uncertainty moves s by at most 6 percent. |
| P. Giudice, S. Piemonte, "Improved thermodynamics of SU(2) gauge theory", EPJC 77 (2017) 821, arXiv:1708.01216 | Symanzik-improved action, integral method, N_tau = 4, 5; data as xmgrace files in `anc/` (pressure, trace anomaly, energy density, entropy) | No (fixed N_tau = 5, stated "close to the continuum limit"). Cross-check only. |
| M. Caselle, A. Nada, M. Panero, "Hagedorn spectrum and thermodynamics of SU(2) and SU(3) Yang-Mills theories", JHEP 07 (2015) 143, arXiv:1505.01106 | Wilson action, integral method; Hirakida et al. say it "takes the continuum extrapolation" | To be read in Step 4. |

**A misprint in the Hirakida table, repaired by an identity.** The row T/T_c = 1.12 lists P/T^4 = 0.772(69). The same row has s/T^3 = 1.18(2), eps/T^4 = 1.10(1), Delta/T^4 = 0.871(13). The identities s/T^3 = (eps + P)/T^4 and Delta = eps - 3P give P/T^4 = 0.08 and 0.076. So the entry is 0.0772(69): a dropped zero. Every other row satisfies both identities within its errors (checked by hand: 1.28: 1.38 + 0.188 = 1.568 vs 1.57; 1.50: 1.51 + 0.298 = 1.808 vs 1.81; 1.76: 1.56 + 0.365 = 1.925 vs 1.92; 2.07: 1.67 + 0.451 = 2.121 vs 2.12). I use 0.0772(69).

**What these sources cannot give.** All of them stop at T/T_c about 2 to 3 (Hirakida at 2.07). The test is tightest at T_2 from about 1.1 to 2 T_c (Step 2), so the range is adequate for the infimum. Below T_c every source has P/T^4 consistent with zero, so pairs with T_2 <= T_c carry no constraint (B = +infinity within error).
