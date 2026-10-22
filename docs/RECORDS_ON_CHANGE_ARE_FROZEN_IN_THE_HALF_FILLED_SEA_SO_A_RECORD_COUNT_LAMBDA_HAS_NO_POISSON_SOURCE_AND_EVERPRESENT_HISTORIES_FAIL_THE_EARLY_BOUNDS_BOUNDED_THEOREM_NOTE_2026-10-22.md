---
claim_id: records_on_change_are_frozen_in_the_half_filled_sea_so_a_record_count_lambda_has_no_poisson_source_and_everpresent_histories_fail_the_early_bounds_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Tests record-count rules meant to give the Poisson counts an everpresent (Sorkin-type) Lambda needs. (a) Record on change, where a site records only when its actual occupation changes. If a site-diagonal antiunitary reverses both half-ticks, the half-filled sea has equal odds at both half-ticks. The fewest-change transport is then the identity, so record-on-change makes zero vacuum records (count 0, variance 0). Checked on a 1D pair-walk ring, N = 8, 10, 12, CL-1 gate form: TV <= 7.8e-16. In 1D the only breaking is the ring holonomy mod 2 pi; 2 pi is an exact gauge (frozen). At holonomy pi + 1 the rate per site falls with N (3.4e-2, 1.7e-2, 8.9e-3 at N = 6, 8, 10). Those counts are collective: the Fano factor grows in proportion to the window (0.80, 1.61, 4.02 for 2, 4, 10 sites), so there is no sqrt(N) law. A drifting mass angle gives local single hops: rate 0.142 per site per unit drift, Fano 2.00. (b) Prefactor. Lambda/L^2 is conjugate to V4, and a minimum-uncertainty packet gives Lambda_rms L^2 = L^4/(2 sigma_V) with sigma_V^2 = (F/r) v_c V4, where r is records per site per half-tick. With the past cone today (0.1229 H0^-4): imported Poisson per half-tick, or a fair Born coin per site per half-tick, overshoots by 6.7 to 14.9. Expansion-driven changes (through mass angles) give about 2e-40 of the measured value, and split-driven changes at most 5e-31. (c) History. Under S/V dynamics on the past light cone (ADGS model 1, amplitude A = (1/2) sqrt(2 r/(F sig))), rms Omega_L = A/(3 sqrt(V H^4)): 2.73 A in the radiation era, 1.81 A in the matter era, 0.95 A today, so Lambda tracks H^2. Histories from a = 1e-20 survive (H^2 > 0) only for A <~ 0.15. Today's Omega_L = 0.685 is then a >= 7 sigma fluctuation, and the best factorised joint probability with BBN and recombination bounds is about 8e-18. A late-window diagnostic (switched on at z = 3, conditioned on today) gives w0 = +0.17 [-0.97, +0.89] and wa = -0.86 [-3.03, +1.50]; 0 of 82 histories fall in a DESI DR2 box or a LambdaCDM box. Gate result: FAILURE. Supplied model, finite diagnostic: toy gate parameters, LambdaCDM (Planck 2018), the eps0 range, the S/V dynamics, approximate BBN and CMB bounds, and DESI central values."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/records_on_change_are_frozen_in_the_half_filled_sea_so_a_record_count_lambda_has_no_poisson_source_and_everpresent_histories_fail_the_early_bounds_2026_10_22.py
---

# Records on change are frozen in the half-filled sea, so a record-count Lambda has no Poisson source, and everpresent histories fail the early bounds

Claim type: bounded_theorem.
Primary runner: `scripts/records_on_change_are_frozen_in_the_half_filled_sea_so_a_record_count_lambda_has_no_poisson_source_and_everpresent_histories_fail_the_early_bounds_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3, the vacuum standard) carries Lambda as a supplied constant per proper 4-volume, with w = -1. The information-minimisation lead suggested a Sorkin-type, or everpresent, Lambda: 4-volume is a record count with Poisson noise, so Lambda ~ N^-1/2. Two earlier results block this. CL-2's record per site per half-tick gives exact counts (Fano 0; PR #10002). A Poisson count must be imported (PR #9876).

This note tests rules that might give Poisson counts structurally:
- record on change: a site records only when its occupation changes; this is variant R3 of the neighbourhood-roles probe, which kept Born statistics (z 2.6);
- records created at splits;
- a Born coin at each site and half-tick.

It builds on PR #9876 (time reversal freezes half-filled-sea records; S/V tracking), PR #10002 (exact counts, Planck circle, drift of horizon-tied counts) and PR #9962 (lambda-size-rule: the Sorkin variant overshoots and tracks). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

Units: rung units, L = sqrt(8 pi) l_P, 8 pi G hbar = L^2, c = 1. The 4-volume per site per half-tick is v_c = (sig/2) L^4 with sig = sin(eps0)/sqrt3. Measured: Lambda L^2 = 7.151e-121, H0 L = 5.90e-61.

## Statement

A. Records on change in the half-filled sea.

1. Theorem (frozen vacuum). Suppose a site-diagonal antiunitary K reverses each half-tick, K U K = U^dag. Then K maps the Floquet sea at one half-tick onto the sea at the other, so the configuration odds are equal at both. The fewest-change transport between equal odds is the identity, and it is unique, since every other plan has positive expected change. Under record-on-change the vacuum therefore makes no records: the count is 0 and its variance is 0, at every window. In the 1D pair walk (CL-1 gate form: exp(-i(eps - mu/2)R) on even pairs, exp(+i(eps + mu/2)R) on odd pairs) |KUK - U^dag| = 2e-16 and TV(p_A, p_B) <= 7.8e-16 for N = 8, 10 and 12, both at (eps, mu) = (0.6, 0.3) and at (0.0375, 0.01). PR #9876 solved the same antiunitary for the 3D block tick (8^3 torus, max error 1.9e-14). The pi-flux face phases that the sea's energy selects are T-even (+pi and -pi are one holonomy), so the laws' vacuum has this symmetry.
2. Breaking the antiunitary does not give Poisson counts.
   - A gauge-real 1D chain is broken only by its ring holonomy mod 2 pi. Holonomy 2 pi is an exact gauge, and its TV is 5e-16.
   - At holonomy pi + 1 the sea moves. The eps -> 0 entropic plan reaches the LP fewest-change minimum (N = 8: 0.136365 changes per half-tick, both ways).
   - The rate per site falls with N: 3.4e-2, 1.7e-2 and 8.9e-3 at N = 6, 8 and 10. A filled band is invariant under a uniform vector potential, so the bulk stays frozen.
   - The counts that do occur are collective. The long-time Fano factor (tilted Perron root) is 0.80, 1.61 and 4.02 for windows of 2, 4 and 10 sites, so Var ~ w^2: one global mode moves, and a 4-volume count has no sqrt(N) law.
3. The one structural Poisson-like source is a changing odds. If the mass angle drifts by d per half-tick, the plan makes independent single hops. The rate is c d per site with c = 0.142, the one-step Fano factor is 2.00 for the whole ring and for a single pair (two site changes per hop), and the fresh entropy H(Y|X) lies within the Fano-inequality bound h(P_move) + P_move ln(M - 1). Fresh randomness per half-tick is bounded by how much the odds change. A stationary vacuum supplies none.

B. Lambda magnitude, prefactor computed.

4. The phase of Lambda is (Lambda/L^2) V4, so Lambda/L^2 and V4 are conjugate. A minimum-uncertainty packet has sigma_V sigma_(Lambda/L^2) = 1/2 (Gaussian check: 0.50000000), so Lambda_rms L^2 = L^4/(2 sigma_V). With r records per site per half-tick and Fano factor F, the count-volume has sigma_V^2 = (F/r) v_c V4, so Lambda_rms L^2 = (1/2) sqrt(r/(F sig/2)) / sqrt(V4/L^4). Fewer or noisier-per-record counts give a smaller Lambda.
5. The past light cone today is V4 = 0.1229 H0^-4 = 1.01e240 L^4.
   - Imported Poisson per site per half-tick (r = F = 1), or a fair Born coin per site per half-tick (r = F = 1/2): Lambda_rms is 6.7 to 14.9 times the measured value over the eps0 range. This agrees with the register's 'overshoots 6-13x'.
   - Record on change under the laws: zero from the vacuum (item 1). Expansion reads edges only through mass angles mN, so r_exp = c mu_top H sig L/2 <= 1.4e-81, giving 2e-40 of the measured value. Splits give at most one random change per site per split, r_split <= 9.2e-63, giving <= 5e-31 of it. Every structural source misses by 30 orders or more.
   - Matching today's rms needs r/F of about 2 sig A^2, with A as in item 6: about 4e-3 to 2e-2 at A ~ 0.7. No rule supplies it. A Born coin at that rate is FITTED.

C. History and (w0, wa).

6. S/V dynamics (Ahmed-Dodelson-Greene-Sorkin model 1, supplied): Lambda L^2 = A B(u)/u, with B a standard Brownian motion in u = V4/L^4 over the past light cone and A = (1/2) sqrt(2 r/(F sig)) from item 4. ADGS's alpha is A/(8 pi). Theorem (tracking): rms Omega_L = A/(3 sqrt(V H^4)). Here V H^4 is 4 pi/840 in the radiation era and 0.0338 in the matter era (beta functions), and 0.1229 today, so rms/A is 2.73, 1.81 and 0.95. Lambda ~ H^2 at every epoch, and early fluctuations are about 2.9 times today's.
7. Self-consistent Friedmann histories from a = 1e-20, 12000 each, start analytic in the radiation era; a crunch is H^2 <= 0.

   | A | alive | P(BBN) | P(rec) | rms Omega_L0 | P(today) |
   |---|---|---|---|---|---|
   | 0.05 | 1.000 | 0.380 | 0.229 | 0.027 | 2e-140 |
   | 0.10 | 0.991 | 0.195 | 0.117 | 0.055 | 1e-34 |
   | 0.15 | 0.314 | 0.044 | 0.024 | 0.086 | 2e-15 |
   | 0.20 | 0.001 | 0 | 0 | — | — |

   Survival needs A <~ 0.15. Today's Omega_L = 0.685 is then at least a 7 sigma fluctuation. The best factorised joint probability (alive x BBN x recombination x today) is about 8e-18, with bounds |Omega_L(BBN)| < 0.065, |Omega_L(z = 1100)| < 0.03 and |Omega_L0 - 0.685| < 0.02. Per half-tick Poisson (A = 4.8 to 10.7) crunches at once. PR #9876 found the same kind of tracking (Omega_L std 2.54 at BBN at coefficient 1, against 2.73 here).
8. Late-window diagnostic, a lower bound on the trouble (early bounds ignored): switch on at z = 3, A = 0.5, condition on today's Omega_L, and fit CPL to rho_L over z <= 2. The result is w0 = +0.17 [-0.97, +0.89] and wa = -0.86 [-3.03, +1.50] (16-84%). None of the 82 histories falls in a DESI DR2 box (|w0 + 0.75| < 0.12, |wa + 0.86| < 0.5) or a LambdaCDM box. Everpresent Lambda changes by O(1) per Hubble time, so |w + 1| ~ O(1). DESI's departure is about 0.25 in w0, and the hinge law keeps |dw| < 6e-4. The model matches neither.

## Candidate rules tested (not adopted)

R-EPL-1 (record on change): "A site gets a permanent record at a half-tick only when its actual occupation changes; 4-volume is the record count."
1. No measured number: pass.
2. No structure by name: pass.
3. Prediction not built for: the vacuum makes no records, so empty regions have no 4-volume, and Lambda from counts is <= 5e-31 of measured. FALSIFIED as a size rule.
4. Axiom bent: Record (rate). It replaces the adopted record-reading (every site every half-tick) and needs CL-2's pointer for unchanged sites (neighbourhood-roles).

Result: FAILURE.

R-EPL-2 (Born coin): "Each site records at each half-tick with odds 1/2, independently."
1. No measured number at p = 1/2: pass. Any other p must be FITTED.
2. No structure by name: pass.
3. Prediction: Lambda_rms 6.7 to 14.9 times measured, with tracking; every history crunches (A = 4.8 to 10.7). FALSIFIED. With p fitted so that histories survive (A <~ 0.15), today's value is a >= 7 sigma fluctuation.
4. Axiom bent: Record, plus a random source beyond 'one actual configuration distributed as its odds' (Admissibility's reading note leaves the formation probability unsupplied).

Result: FAILURE.

R-EPL-3 (split records random): FALSIFIED by item 5, <= 5e-31.

## Derivation

Items 1 to 3 build the many-body Floquet sea as a Slater determinant of the lower quasi-energy band, with odds |det|^2 over the C(N, N/2) configurations. The transport is the eps -> 0 Sinkhorn limit (eps = 1 to 0.03, log domain) on the half-tick's support: the per-pair occupation is kept, and the cost is the number of sites changed. It is checked against HiGHS. Counting uses the tilted kernel K1(s) K2(s), with mean and variance from the Perron root by central differences (h = 0.02). Item 4 uses an FFT Gaussian. Item 5 integrates LambdaCDM (Omega_m 0.3153, Omega_r 9.1e-5, Omega_L 0.6847) by nested quadrature, and uses m_top/M_P sqrt(8 pi) sig for the top mass angle. Items 6 to 8 integrate in ln a (step 0.02). The past-cone 4-volume is (4 pi/3)(chi^3 I0 - 3 chi^2 I1 + 3 chi I2 - I3), with I_k = int a^3 chi^k dt accumulated (checked offline against quadrature, not in the runner: 0.1223 at step 0.005 against 0.1229). Brownian increments are sqrt(dV) N(0, 1), seeded. P(today) is a Gaussian-window estimate at the measured rms.

## Finite checks

The runner gives 12 PASS and 0 FAIL in about 44 s, using 73 MB. Several PASS lines record failures against measurement.
- Theorems: item 1 (with the TV check), the 2 pi gauge, the prefactor 1/2, and the V H^4 constants.
- Diagnostics: the LP match, collective Fano, the N trend, the drift Fano, and the history ensembles.
- Estimates: items 5, 7 and 8.

## Boundary

Not claimed: that no record rule gives everpresent Lambda.
- The CL-1 cube tick with copy mass was not rebuilt here. The record-arrow probe reports the laws keep sigma_d K, a site-permuting antiunitary, which does not by itself force equal odds. If the copy mass breaks the site-diagonal antiunitary, the 3D vacuum may move. That is the open test, with r and F to be computed as in items 2 and 3.
- Not computed: 2D/3D plaquette-flux T-breaking, the S/V model's alternative 4-volumes (Hubble cylinder), ADGS model 2, and inhomogeneous Lambda (Barrow 2007 constrains it).
- ADGS (2004) and later analyses (Zwane, Afshordi and Sorkin 2018; Das, Nasiri and Yazdi 2023) report viable histories near alpha ~ 0.01 to 0.02 (A ~ 0.25 to 0.5). Here A >= 0.2 does not survive from a = 1e-20. The difference (crunch handling, the 4-volume, the start time) is not resolved.
- The DESI comparison is a box test on a CPL fit to rho_L, not a likelihood.

## Supplied vs forced

Supplied:
- the toy gate parameters and ring sizes;
- the half-filled sea;
- the eps0 range and v_c = (sig/2) L^4;
- LambdaCDM and the measured values;
- the S/V dynamics and the past-cone 4-volume;
- the BBN and CMB bounds (approximate);
- the start a = 1e-20;
- the DESI and LambdaCDM boxes;
- the m_top value.

Forced, given the laws:
- the frozen vacuum (equal odds, identity plan);
- the 2 pi gauge;
- collective (Var ~ w^2) counts under holonomy breaking;
- Fano 2 under drift, with randomness bounded by the odds change;
- the prefactor 1/2 and the sqrt(r/F) scaling;
- the tracking constants;
- the survival bound on A.

## Conflicts

- (i) CL-3 (vacuum standard: Lambda a constant per proper 4-volume, w = -1; hinge bound |dw| < 6e-4). Everpresent Lambda gives |w + 1| ~ O(1), so the two cannot both hold.
- (ii) The register's criterion "a size law must not drift with the horizon". Everpresent Lambda violates it by construction (item 6).
- (iii) Record-reading (every site every half-tick, adopted 2026-10-22) gives Fano 0 (PR #10002). Record on change gives no vacuum records. Neither supplies Sorkin noise.
- (iv) The info-min-law and minimal-toe-b R5(a) lead (Lambda ~ N^-1/2 within a factor 2). It has a prefactor convention of order 1. With the computed 1/2 and v_c, it overshoots 6.7 to 14.9 times and fails the history test.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records.
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1's gate form and fixed lapse, CL-2's transport and records, CL-3's constant. Zero premise weight.
- Builds on the open PRs #9876, #10002 and #9962, and on the neighbourhood-roles probe (R3 record on change).

## How to run

```
python3 scripts/records_on_change_are_frozen_in_the_half_filled_sea_so_a_record_count_lambda_has_no_poisson_source_and_everpresent_histories_fail_the_early_bounds_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 44 s with 73 MB resident, prints about 4.4 kB and ends with `TOTAL: PASS=12 FAIL=0`. It is seeded, and two runs (direct and via `scripts/runner_cache.execute_runner`) gave identical output.
