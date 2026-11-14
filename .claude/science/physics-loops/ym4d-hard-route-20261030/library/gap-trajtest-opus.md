lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T04:53Z

# gap-trajtest-opus (row 974): GUIDE refutation test of (LSI-traj-seed) through X(2m+2; B)

Queue row 974 of FINISH.md (attack A2 of row 970). Pinned commit 27a48373b. Started 2026-11-14T16:53Z.
A run guides or refutes; it proves nothing.

## Status log
- 2026-11-14T16:53Z: file created with plan.
- 17:04Z: Sections 1-3 written (criteria before any run); control C1 run; batch 1 (small boxes) started 17:04Z.

## Plan (at most eight steps; one per response)
1. Read row 970 section 7.3 ((LSI-traj-seed)_a, (EC-traj)), Proposition HC and X(2m+2; B) in gap-direction-max.md,
   Corollary BR-J (K_a) and row 954 (m_G >= K_a). Write the exact target quantity and the needed rate.
2. Read the slab / chain code in library/guide/ (lanes 950-970); choose the estimator of X; time a smoke test.
3. Write the pre-set criteria (REFUTED / NOT REFUTED / INCONCLUSIVE) and controls in this file BEFORE any run.
4. Smoke run at side 4, beta 2.3; check controls.
5. Main runs: sides 4-8, beta 2.3 and 2.6, sample size N and 2N; record error bars.
6. Fit the decay rate in m; compare with the needed rate.
7. Verdict against the pre-set criteria; what is left.
8. RESULT line.

## 1. Inputs and the exact target (READ; no new claim) — written 16:59Z

**1.1 Read.** FINISH row 974 (this row) and row 970's head; `gap-direction2-max.md` (row 970) Sections 1, 4, 7 in full;
`gap-direction-max.md` (row 931) Steps 4-5 (L165-195, L265-330: S, X, (5.3), Theorem V, Proposition HC);
`gap-fc-max.md` L55-100, L206-224 (K_a, C_beta); `gap-lsij-scale-opus.md` (row 954) Section 7.2-7.4;
`gap-avgcurv-max.md` L56 (sizes on the box (a; (4a)^3)).

**1.2 Objects (quoted in short).** T = T_B(beta) the gauge-invariant Wilson transfer operator of the periodic spatial box B,
r_i = lambda_i/lambda_0 = e^(-E_i). S(t; B) = sum_(i>=1) r_i^t, X(t; B) = log(1 + S(t; B)) (row 931 L172-175). By (5.3) of row 931,
1 + S(2s) = E_(u~nu) ||p_s(u, .)||^2_(L^2(nu)): X(2s) is the chi^2 (Renyi-2) mutual information of two vacuum slices at lag s.
Equivalently 1 + S(t) = Tr T^t/lambda_0^t = Z(B x t)/lambda_0^t: X(t) is the free-energy excess of the periodic torus B x t over
t copies of the vacuum (a finite-temperature quantity at N_t = t).
- Proposition HC (row 931 L305-312): (HC-vac)_alpha => X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m) for all m >= 0, and E_1 >= alpha.
- Lemma TRAJ (row 970 7.1): (LSI-traj)_s with (1/2) int alpha_s ds >= alpha gives the same bound.
- (LSI-traj-seed)_a (row 970 7.3): (LSI-traj)_s on the box (a; (4a)^3) with (1/2) int alpha_s ds >= K_a.
  Necessary consequence (EC-traj): D(mu^(u,k+1) | nu) <= e^(-A) D(mu^(u,k) | nu) for every start u and every k, A/2 >= K_a
  (mu^(u,k) = bridge-point law of the chain started at u, at step k).
- Needed rate (row 968 L56, C_beta = 12.51 at beta 2.3, 12.63 at 2.6; K_a = (C_beta + 3 log a)/(a - 2)):
  beta 2.3: K_20 = 1.194, K_30 = 0.811, K_40 = 0.620, K_60 = 0.427, K_80 = 0.329, K_100 = 0.269, K_150 = 0.186, K_200 = 0.143.
  beta 2.6: K_30 = 0.815, K_40 = 0.624, K_60 = 0.430, K_100 = 0.270 (the same to 0.005).
  Per step of the chain the chi^2 quantity must fall by e^(-2 K_a); per unit of Euclidean time t, by e^(-K_a).
- Row 954 (GUIDE): on the seed box the flux states are heavy; the necessary condition is m_G >= K_a (m_G the lightest local
  energy). beta 2.3: m_G about 1.3 (plaquette channel), above K_30. beta 2.6: E_1 <= 0.87 +- 0.11 on L = 14 (no plateau),
  recalled m_G about 0.49; undecided between a = 30 and a = 60. On sides 4-8 the lightest states are torelons
  (E = 0.33 at L = 4, beta 2.3); they are absent from the seed box (energy about sigma x side).

**1.3 Duplicate check (rule 0a).** `grep -n "LSI-traj\|EC-traj"` over FINISH.md and `library/open-core.md`: the only
rows are 970 (source) and 974 (this row). No other row runs this test.

## 2. What the decay rate of X(2m + 2; B) can show (analysis before any run) — written 17:01Z

**2.1 Lemma RATE (PROVED; spectral calculus).** On a fixed box B, put rho_X(m) := (1/2) log[X(2m + 2)/X(2m + 4)] (the per-step
rate of X in K-units). (a) S(t) = sum_(i>=1) e^(-E_i t) is log-convex, and -d log S/dt decreases to E_1(B) as t -> infinity.
(b) rho_X(m) -> E_1(B) as m -> infinity. (c) If X(2m + 2; B) <= C e^(-2 alpha m) for all m (any constant C, in particular
C = 72 beta |B|), then E_1(B) >= alpha. (d) Conversely, if E_1(B) < alpha, the bound fails, but only at
m >~ [log(C/g_1) ]/(2 (alpha - E_1)) with g_1 the degeneracy of the lowest level.
Proof. (a) Cauchy-Schwarz on the sum of exponentials; its log-slope is the Gibbs mean of E_i at "time" t, which decreases to
the minimum. (b) S -> 0, so X = S (1 + O(S)), and S ~ g_1 e^(-E_1 t). (c) is Proposition HC's last line (r_1^(2m+2) <= S <= 2X once
X <= 1). (d) from (b). QED
Reading. The "decay rate of X" that can refute the route is the large-m rate, which is E_1(B). At small m the rate of X
is NOT bounded below by E_1: X = log(1 + S) and S is exp(extensive), so X ~ log S can fall like a power (the free energy of
the torus B x t; Stefan-Boltzmann t^(-3) above deconfinement, ARGUED). But there the prefactor 72 beta |B| of Proposition HC
dominates: X(t)/|B| at the deconfinement point is about 0.66/t_c^3 or less (SU(2) Stefan-Boltzmann, RECALLED), against
72 beta e^(-K_a (t - 2)); for beta 2.6 (t_c about 12, RECALLED) and K_30 = 0.815 this is 3.8e-4 against 0.054. So the slow
small-m decay does not violate the bound of Proposition HC. (ARGUED; numbers recalled.)

**2.2 Measurement consequence (PROVED, (d) + arithmetic).** On B = L^3 with L = 4 to 8, a direct violation of
X(2m + 2) <= 72 beta |B| e^(-2 K_a m) needs (K_a - E_1) t > log(72 beta L^3) (= 9.3 to 11.4 at L = 4 to 8): with
K_a - E_1 of order 0.2 that is t of order 50 to 60, where X ~ e^(-E_1 t) is far below any Monte Carlo resolution. A
thermodynamic-integration estimate of X itself (X = 6 |B| t int_0^beta (<P>_(B x t) - <P>_(B x inf)) d beta') resolves only
X >~ 0.01 at affordable cost (the plaquette noise enters times 6 |B| t). So the measurable form of the test is the large-m rate,
E_1(B), read from correlators: for any positive correlator C(tau) = sum_i c_i e^(-E_i tau), the effective energy
E_eff(tau) = log[C(tau)/C(tau + 1)] is >= the lowest energy of the sector reached, at every tau (log-convexity; PROVED).
So **an effective energy below K_a, with its error, refutes; a plateau above K_a supports but does not prove.**
A lower bound on X itself, for the record: for any n gauge-invariant mean-zero observables with Gram matrix C(0) and
lag matrix C(t), S_n(t) := Tr[C(0)^(-1) C(t)] <= S(t), because P^t >= 0 (Wilson SU(2) transfer matrix is positive,
RECALLED: Luscher 1977) and the compression of a positive operator to a subspace has a smaller trace (PROVED).

**2.3 The entropy form (EC-traj) (ARGUED).** Averaged over u ~ nu, (EC-traj) gives I_s(k + 1) <= e^(-A) I_s(k) with
I_s(k) = I(U_0; Y_s^(k)) the mutual information of the start and the bridge point at step k (data processing: I_s(k) <= I(U_0; U_k)
<= X(2k), row 931). For a Gaussian chain I(U_0; U_k) = sum over modes of -(1/2) log(1 - e^(-2 omega k)), a positive mixture of
exponentials with rates >= 2 E_1: the per-step rate is >= E_1 at every k, so (EC-traj) adds no constraint beyond E_1 >= K_a.
A non-Gaussian chain can do worse at intermediate k; estimating I_s(k) in dimension 4 L^3 x 3 is the hard estimator of
row 970 A2 and is not attempted here (out of budget; see Section 6).

**2.4 Transfer to the seed box (READ, row 954 7.4).** On B = L^3, E_1(B) = min(E_flux(L), m_G, ...), where E_flux(L) is the
torelon (centre-odd, winding) energy, about sigma L - pi/(3L) (RECALLED). On the seed box (a; (4a)^3) the side is 4a >= 120,
so E_flux >> 1 and E_1 = m_G (the lightest glueball, 0++). Hence a small-box E_1 below K_a refutes (HC-vac) only on that box
and does NOT transfer, when it comes from the flux sector. Only the local, centre-even, zero-winding energy transfers, and
only on boxes where the torelon PAIR (centre-even, energy about 2 E_flux) is heavier than it.

**2.5 The test, therefore.** Measure, sector by sector, upper bounds E_eff(tau) on the lowest energies of L^3 boxes:
(F) centre-odd flux sector (smeared Polyakov lines along the three spatial axes, zero momentum);
(G) centre-even local sector (smeared plaquette and 2x2-loop sums, zero momentum, 0++);
and compare (G) with K_a on boxes where 2 E_flux > E_G. The seed is refuted for every a with K_a > m_G (Lemma RATE (c) on
the seed box). Since K_a falls with a, the outcome is a range a < a_min(beta), not a verdict on the route as a whole.

## 3. Pre-set criteria (written 17:02Z, BEFORE any run)

**3.1 Runs.** SU(2) Wilson, periodic L^3 x N_t, heat bath (Creutz sampler) plus over-relaxation, plain numpy, script
`guide/lane974/traj974.py` (new; the heat-bath pattern of `guide/lane968/tilt.py` and the APE smearing of
`guide/lane954/glueball954.py`). beta 2.3: L = 4, 6, 8 (N_t = 16). beta 2.6: L = 4, 6, 8 (flux record), then L = 16 (N_t = 24)
for the local sector if memory and time allow. Sample sizes N and 2N (a second, independent stream with another seed);
errors by jackknife over 20 blocks; both N-values reported.

**3.2 Observables (Section 2.5).** Per time slice, zero spatial momentum, after n_ape steps of spatial APE smearing
(alpha 0.5) at two levels:
(F) Polyakov lines along x, y, z (half trace of the ordered product along the axis), summed over the transverse plane,
    averaged over the three axes; centre-odd. Effective energy E^F(tau) = log[C(tau)/C(tau + 1)].
(G) plaquette and 2x2-loop sums (spatial, all three planes), connected; a 4-operator basis (2 shapes x 2 smearing levels).
    E^G_var(tau) := -(1/tau) log lambda_max(C(0)^(-1) C(tau)), and the single-operator E^G(tau) of the best operator.
All of these are upper bounds on the lowest energy of the sector reached, at every tau, for the exact correlator
(Section 2.2; PROVED). Lattice noise is the only caveat; hence the error rule below.

**3.3 Thresholds.** K_a = (C_beta + 3 log a)/(a - 2): K_30 = 0.81, K_40 = 0.62, K_60 = 0.43, K_100 = 0.27 at both beta.

**3.4 Verdicts, per (beta, a).**
- REFUTED (the seed (LSI-traj-seed)_a fails at this beta, via Lemma RATE (c) on the seed box): some G-sector upper bound
  satisfies E^G(tau) + 2 err < K_a, at tau >= 1, in the stream of size N AND in the combined 2N (stable under doubling), on a
  box where the result transfers: (TR) the flux plateau value obeys 2 E^F > E^G + 2 err, so the state is not a torelon pair.
- REFUTED ON THE BOX ONLY (no transfer): an upper bound below K_a - 2 err in sector F, or in G on a box failing (TR).
- NOT REFUTED (GUIDE support only): on a transferable box, every G-sector value at tau = 1, 2, 3 minus 2 err stays above
  K_a, and two consecutive tau agree within errors (a plateau) above K_a.
- INCONCLUSIVE: otherwise (noise before a plateau, or no box passing (TR)).
- A published glueball mass with its error is a separate data path; the same rules apply to it, recorded separately.

**3.5 Controls (pre-set).** (C1) beta 0.5, L = 4, N_t = 4: plaquette <(1/2) tr U_p> = I_2(0.5)/I_1(0.5) = 0.1237 up to O(u^5);
pass if within 5e-4. (C2) beta 2.3, L = 4: E^F near row 954's torelon energy 0.33 (variational, open time; `gap-lsij-scale-opus.md`
7.4); pass if the plateau lies in [0.25, 0.45]. (C3) beta 2.3, L = 8: the G plateau within 0.3 of row 954's plaquette-channel
m_G of about 1.3 (7.2). A failed control voids the runs it covers.

**3.6 Limits.** Job stops above 3 GB RSS. One job at a time under the numeric lock, nice, BLAS threads 1.

## 4. Runs (GUIDE)

**4.1 Control C1 (17:03Z, `guide/lane974/logs/c1_b0.5_L4.log`).** beta 0.5, 4^4, 100 + 8000 x 2 sweeps:
<(1/2) tr U_p> = 0.12412 +- 0.00014 (naive error, no autocorrelation correction) against I_2/I_1 = 0.12372: difference
4.0e-4, inside the pre-set 5e-4. PASS (the difference is 3 naive errors; an O(u^5) cube term of coefficient about 14 would
account for it; not checked). Speed: 8^3 x 32 runs about 30 ms per sweep including measurement.

**4.2 Batch 1 (`guide/lane974/batch1.zsh`, log `logs/batch1.log`).** beta 2.3 (APE 3 and 8 steps) and 2.6 (6 and 16 steps);
L = 4, 6, 8; N_t = 32; 300 thermalisation sweeps, 2000 measurements 2 sweeps apart; two streams per point, seeds 11 and
111 (N = 2000 and 2N = 4000). Started 17:04Z.

## 5. Published data path (separate from the runs; READ) — written 17:05Z

Source: M. Teper, "Glueball masses and other physical properties of SU(N) gauge theories in D = 3+1: a review of lattice
results for theorists", arXiv hep-th/9812187, Appendix A, Table 10 (open copy fetched to /tmp/row974lit; text line ~600).
Its beta 2.2-2.6 rows come from C. Michael and M. Teper, Nucl. Phys. B305 (1988) 453 (Wilson action). Quoted:
- beta 2.3, 10^4: a sqrt(sigma) = 0.3687(22), a m_0++ = 1.216(23) (effective mass from t = a to 2a).
- beta 2.6, 20^4: a sqrt(sigma) = 0.1326(30), a m_0++ = 0.51(3) (effective mass from t = 2a to 3a).
(Also 2.4: 0.959(20) on 14^4; 2.5: 0.660(22) to 0.723(23).) Teper states these are effective masses at the given t. An
effective mass of a positive correlator is an upper bound on the lowest energy of the channel (Section 2.2), so the
pre-set REFUTED rule applies to them directly; the NOT REFUTED rule needs a plateau, which the table does not show.

Against the thresholds (Section 3.3; the 0++ is the lightest glueball, so E_1(seed box) = m_0++):
- beta 2.6: m_0++ + 2 err = 0.57 < K_40 = 0.624 < K_30 = 0.815. **REFUTED for a = 30 and 40** (published data path).
  K_a < 0.57 needs a >= 45 (K_44 = 0.571, K_45 = 0.559). K_60 = 0.430 < m_0++ - 2 err = 0.45: not refuted at a = 60.
  (TR) at 20^4: E_flux = sigma L - pi/(3L) = 0.0176 x 20 - 0.052 = 0.30 (Teper's eq. (6) with his sigma), so the torelon
  pair sits at about 0.60, above 0.57: passes, barely (ARGUED from the formula, not measured here).
- beta 2.3: m_0++ = 1.216(23); m_0++ - 2 err = 1.17 > K_30 = 0.811. Not refuted for a >= 21 (K_21 = 1.139);
  undecided at a = 20 (K_20 = 1.194). E_flux on the seed box is irrelevant (side >= 80).
Reading. This is the necessary condition m_G >= K_a of row 954 (Lemma GAP-R there; Lemma RATE (c) here), now with a
published number in place of row 954's recollection: at beta 2.6 the seed through (LSI-traj-seed)_a, (LSI-br-seed)_a or
(LSI-J-seed)_a is impossible for a <= 44; at beta 2.3 it is not excluded for a >= 21.

**4.3 Amendment to 3.1, written 17:05Z, before batch 2 runs.** The large beta 2.6 box is L = 20 (N_t = 24), not 16: with the
published sigma (Section 5), the torelon pair at L = 16 sits near 2 x 0.22 = 0.44, below m_0++ = 0.51, so L = 16 would fail
(TR); at L = 20 the pair is near 0.60. Script `guide/lane974/batch2.zsh`: 300 + 1000 x 2 sweeps, APE 8 and 20 steps, seeds
21 and 121 (N = 1000, 2N = 2000). Same criteria (3.4). Also measured there: the F sector, to check (TR) directly.
