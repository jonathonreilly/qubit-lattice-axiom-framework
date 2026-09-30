# T32 pre-registration (written before any run)

Wall: rigorous infinite-volume area law + mass gap of SU(3) Wilson at beta = 6, 3+1D (L06-W8).
Route under test (R2, outside the lane): Chatterjee, CMP 385 (2021) 1007, Thm 2.2/2.4:
  exponential decay of correlations under arbitrary boundary conditions (Def 2.3) => unbroken centre symmetry
  on some slab (Def 2.1) => area law for centre-charged reps. So the wall's two halves are ONE premise.
The lane's own cheapest named step: replace imported Sommer numbers by a framework-run larger-lattice MC.

Nothing here can prove the wall. The test decides whether the reduction's hypotheses are FALSIFIED
by cheap pure-glue numerics at beta = 6 (route dies) or survive (route stays a reduction whose
remaining obligation is blocked-equivalent).

## Code validity gates (if either fails, no physics is read from the run)
G1. Plaquette <P> at beta = 6.0 on 8^4 within 0.5934 +/- 0.004 (finite-size shift on 8^4 is <~0.001).
G2. Plaquette at beta = 1.0 within 0.0556 +/- 0.003 (leading strong coupling beta/18).

## Physics readings
T-A  String tension, volumes 8^4 and 12^4, beta = 6.0 (APE-smeared spatial links, force F(r) fitted to sigma + e/r^2):
  PASS: sqrt(sigma) a in [0.19, 0.25] on BOTH volumes AND the two volumes agree within 15%.
  FAIL: either outside the window, or volume difference > 15% (area law not reproduced / not volume-stable
        at these sizes => the "framework-run area law" is not established by this runner).
  Prediction: 0.21-0.23 (imported value 0.216, sigma a^2 = 0.0465).
T-B  Creutz ratios, unsmeared, 8^4 and 12^4: chi(R,R) must be positive and decrease with R (Bachas concavity),
  chi(4,4) within 40% of sigma. Prediction: chi(2,2) ~ 0.12 (NOT the 0.226 of the repo's 4^4 note, which I predict
  is a 4^4 artifact). FAIL: chi(2,2) >= 0.2 on 8^4 or non-monotone by > 2 errors.
T-C  Gap (0++ glueball, smeared spatial plaquette operator, zero momentum): effective mass m_eff(t=1->2) in
  [0.55, 1.2] in lattice units on 12^4; 8^4 and 12^4 agree within 30%. FAIL: m_eff consistent with 0
  (no exponential decay) or volume-unstable > 30%.
T-D  Centre symmetry in a slab (Def 2.1 hypothesis) at beta = 6.0 on L_s^3 x N_t periodic:
  Prediction: N_t = 4, 6 deconfined (<|P|> > 0.25, phases clustered near 0, +-2pi/3);
  N_t >= 10-12 confined (<|P|> < 0.12, no clustering). Route-R2 KILL reading: centre symmetry broken at
  ALL N_t up to 12 at beta = 6 (then Def 2.1 fails for the pure-glue theory). Route survives otherwise.
T-E  Exact arithmetic: the repo's compact-cube gap bound (16/a)*3^(-2 n_links)*exp(-2 a v n_faces) versus volume:
  reading: the bound is not volume-uniform (goes to 0). Pre-registered as expected; no computation can rescue it.

## What would change the outcome label
- If T-A or T-C FAIL for the pure-glue beta = 6 measure: the wall would be MISSTATED about the pure-glue theory
  (its target statement false), and I would say so.
- If T-D shows centre symmetry broken at all tested N_t: R2 dies for this beta.
- Otherwise: outcome PRICED (wall = one strong-mixing premise, numerically supported, unproved).

## Amendment A1 (written after the first validation run, before any physics run)
Gate G2 as written above was WRONG: I used the leading strong-coupling term beta/18 = 0.0556 and forgot the
O(beta^2) single-plaquette terms. In 4D the first correction from neighbouring plaquettes is O(beta^5), so
the correct comparator at beta = 1 is the exact one-plaquette Haar integral, computed independently by
Haar-sampling (20 x 5e5 draws): u(1) = 0.06019. MC gave 0.0604 +- 0.0004 (4^4), 0.0601 +- 0.0002 (6^4).
G2 (as written) is recorded as failed by the amended comparator; G2' (match u(1) = 0.0602 within 0.001) passes.
G1 passed: 8^4, beta = 6: 0.59423 +- 0.00015 (naive error), inside 0.5934 +- 0.004.

## Amendment A2 (before any physics result was read)
The machine was heavily loaded (load average 100+); the 12^4 job had not produced one measurement after 7 minutes.
I killed it and replaced it by 6^4 and 10^4 (same beta = 6.0, same observables) so that the volume series is
6^4, 8^4, 10^4 (plus the 4^4 reproduction of the repo's runner). All T-A..T-C thresholds are applied to
8^4 and 10^4 (the "12^4" in T-A, T-B, T-C reads "10^4"); 6^4 is a third volume. T-D (Polyakov) stays
12^3 x N_t with N_t in {4, 6, 8, 10}; the N_t = 12 point is dropped.

## Amendment A3 (bug found in the first analysis, before any smeared result was interpreted)
The first 6^4 and 8^4 runs gave smeared W(1,1) = 0.023 (should be ~0.6): the APE smearing used the Hermitian
conjugate of the staple (my heat-bath staple A is the conjugate of the smearing staple S = A^dagger). Fixed in
su3mc.py (smearing now adds dag(A)). The first-run outputs are kept in runs_bad_smear/ for the record and NOT used.
Unsmeared data (plaquette, Creutz ratios, Polyakov loops) do not use smearing and are unaffected; the 4^4 unsmeared
reproduction W(1,1) = 0.596, W(1,2) = 0.387, W(2,2) = 0.197, chi(2,2) = 0.246 agrees with the repo runner's
0.597 / 0.391 / 0.205 / 0.226.
Amendment A4: T-B numerical thresholds were WRONG: I predicted chi(2,2) ~ 0.12 from memory and set the fail line at
0.2. Unsmeared chi(2,2) is 0.238 (4^4), 0.257 (6^4), 0.2615 (8^4), i.e. the repo's 0.226 is NOT a small-volume
artifact; T-B's numeric clauses "chi(2,2) < 0.2" and "chi(4,4) within 40% of sigma" FAILED as written and are
recorded as failed. The monotone-decrease clause (Bachas concavity) is unaffected and is judged separately.
The extracted sigma comes from the smeared static-potential force fit (T-A), which is the pre-registered route.

## Amendment A5 (added while runs were in progress, before their results were read)
Extra Polyakov runs on 8^3 x N_t (N_t = 6, 8, 10) were launched because the 12^3 x 10 run was slow under load.

## Results against the pre-registration (written after the runs; numbers in analysis_output.txt)
- G1 passed (0.5942 on 8^4, 0.5939 +- 0.0001 on 10^4). G2 as written failed (my error); G2' passed.
- T-A FAILED as written: sqrt(sigma) a = 0.205 +- 0.007 (10^4, best plateau; window passed), 0.165 (8^4 best plateau;
  window failed, images at R = L/2); volumes differ by ~20% > 15%; plateau and smearing systematics ~15%.
- T-B numeric clauses FAILED (thresholds wrong, Amendment A4); monotone-decrease clause passed (chi 0.26, 0.13, 0.07;
  forces 0.184, 0.095, 0.070, 0.055).
- T-C PASSED: 0++ effective mass 0.72 +- 0.12 (6^4), 0.84 +- 0.13 (8^4), 0.89 +- 0.10 (10^4) at tau 1 -> 2.
- T-D: N_t = 4 broken (|Pbar| 0.251, cos3theta 0.999); N_t = 6 broken by clustering (0.977 on 12^3; 0.77 on 8^3) but
  |Pbar| = 0.09 failed the 0.25 magnitude clause; N_t = 8 marginal (cos3theta 0.28-0.36); N_t = 10 unbroken
  (cos3theta 0.05-0.10, |Pbar| <= 0.018). Kill reading (broken at all N_t) NOT met.
- T-E as expected: the compact-cube constant falls as 3^(-2 n_links).
Only the 120-configuration 10^4 run and 300-configuration 8^4 run underlie the string-tension numbers.
