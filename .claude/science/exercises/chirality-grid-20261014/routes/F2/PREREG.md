# F2 pre-registrations (written 2026-10-14 ~13:36Z, before any script was run)

## T1: does the free chiral projector's Chern number fix the GW index? (2D, checked numerically)
The theorem of route F2-R uses the link: for an exact Ginsparg-Wilson operator D = 1 + gamma5*eps,
the index in a smooth U(1) background of flux n equals (sign) x c1(eps-bundle of the FREE operator) x n.
Test: overlap with Wilson kernel (r = 1 and r = 0.6), masses m in {-0.5, 0.5, 1.0, 1.5, 2.5, 3.0, 3.5, 4.5},
L in {8, 10}, uniform flux n in {1, 2, 3}. c1 by Fukui-Hatsugai-Suzuki on a 48x48 grid.
- PASS: index = s * c1 * n for ONE global sign s, every case, |index - integer| < 1e-6.
- FAIL: any case mismatches.
(This checks the link only on the tested kernels; it is not a proof of the link.)

## T3: price of the finite-auxiliary (rational) approximation, free 4D kernel (checked numerically)
Shamir domain-wall effective operator with N auxiliary layers: GW defect delta_N = sech^2(N*artanh(lam_T,min)).
Zolotarev optimal rational sign with n poles: delta_n ~ 4*exp(-n*pi*K(k')/K(k)), k = lam_W,min/lam_W,max.
Required defect: delta = 1e-35 (U(1)_em kept exact; W/Z mass shift below rho-parameter precision, Planck cutoff)
and delta = 1e-88 (photon-mass bound if U(1)_em is not kept exact). These targets are order-of-magnitude
readings (suggested), not derived.
- PASS (finite approximation is a modest, countable matter-per-site price in the FREE theory):
  best N_req <= 100 per Dirac field at delta = 1e-35 for some M in {0.5, 1.0, 1.5}.
- INTERMEDIATE: 100 < N_req <= 1000.
- FAIL: N_req > 1000 for every M.
(Free theory only: gauge backgrounds lower lam_min; this is a lower bound on the price.)

## T3 amendment (13:37Z, after first run, reading unchanged)
t3's recalled Zolotarev closed form had K and K' swapped; t3b's first run evaluated on the wrong x-scale
(kept as t3b_zolotarev_direct_WRONGSCALE.out). Corrected direct high-precision computation is t3b/t3c.
The pre-registered PASS/INTERMEDIATE/FAIL reading is unchanged.

## T4: one fermion component per site (qubit-compatible staggered) carries an exact GW index (2D, checked)
Written 13:38Z before running. Adams-type staggered overlap in 2D: D_st (one component per site, KS phases),
Adams term r(1 - Gamma55) with Gamma55 = eps * eta5 * (C1C2+C2C1)/2, eps = (-1)^(x1+x2), chosen so that
Gamma55 commutes with eps; H = eps (D_A - m); index = -(1/2) Tr sign(H). L in {8, 12} (even), flux n in {1,2,3}.
The eta5 choice is fixed by a free-field check (Gamma55 hermitian, [Gamma55, eps] = 0, Gamma55 -> +-1 on the
4 zero modes split 2+2) BEFORE any flux run; if no choice passes, T4 is reported as NOT RUN.
- PASS: for r = 1 and some m window inside (0, 2r): index = s*n (|s| = 1, one global sign) for all L, n,
  integer to 1e-6.  This shows a nonzero exact-GW index with ONE fermion component per site.
- FAIL: index 0 or non-proportional to n for every m in {0.3, 0.6, 1.0, 1.4}.

## T4 result (13:38Z): FAIL as pre-registered. Diagnosis (reading): the candidate list for eta5 lacked the
factor i, so the accepted Gamma55 (eta5 = 1) does not commute with the free D_st (||[G55,Dst]|| = 4) and the
kernel H is not gapped (gaps down to 1e-16).  The free-field acceptance criteria were too weak.  T4's verdict
stands; a separate follow-up T4b is registered below.

## T4b (registered 13:39Z, before running): corrected Adams operator
Candidates: Gamma5 = phase * eta5 * (C1C2+C2C1)/2 with phase in {1, i}, eta5 in {1, (-1)^x1, (-1)^x2, (-1)^(x1+x2)}.
Free-field acceptance (all required, L = 8): Gamma55 hermitian; [Gamma55, eps] = 0; Gamma55 = +-1 (2+2) on
the 4 free zero modes; ||[Gamma55, D_st]|| < 1e-10 in the free theory.  First accepted candidate is used.
Flux runs and PASS/FAIL reading exactly as T4 (m in {0.3, 0.6, 1.0, 1.4}, L in {8,12}, n in {1,2,3}, r = 1).

## T5 (registered 13:41Z, before running): does a weak-coupling gauge background keep the kernel gapped?
Proxy only: 4D U(1), L = 6, Gaussian Feynman-gauge link angles theta = g*A with <A A> = 1/phat^2 (zero mode
removed), g in {0.5, 0.65} (order of SM couplings near the Planck scale), 8 configurations each.
Wilson kernel M = 1, r = 1.  Measure lam_min = min |eig H_W|, and the Zolotarev pole count n for delta = 1e-35
using the measured kappa = lam_min/lam_max (rate from t3b's direct computation interpolated, labelled).
- PASS (finite-pole approximation stays a modest price at weak coupling): lam_min >= 0.3 for every config.
- FAIL: any config with lam_min < 0.05 (near-zero modes; exponential suppression degrades).
- otherwise INTERMEDIATE.  Not an equilibrium ensemble; not non-abelian; L = 6 only.

## T5 ABORTED (13:50Z): the L = 6 sparse shift-invert run reached 564 MB resident (over the 0.25 GB
machine limit) after 10 min without output; killed.  No result.
## T5b (registered 13:51Z, before running): identical to T5 except L = 4 (dense eigvalsh, 1024x1024),
12 configurations per g.  Same PASS/FAIL/INTERMEDIATE reading.  L = 4 is a very small proxy.
