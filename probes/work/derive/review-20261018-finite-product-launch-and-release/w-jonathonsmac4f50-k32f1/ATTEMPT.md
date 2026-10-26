# Finite product-seed launcher-to-output interface: attempt a1

Same-family (Claude Sonnet 5.5), unrefereed. Owner-requested research work; not accepted science, no audit verdict, no premise adopted.
Verdict: PARTIAL. A new, scoped, checked result is proved for the ladder core (any left-lead state, all times, complete output). The route to a full finite launcher-to-output theorem stops at step 14.

Read before choosing premises: `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 130 lines). Source hashes of the three frozen notes (commit `77565121a9e2598aa4daed6413c5c723241654a5`) all match (RECOVERY_STATUS.json).

## 0. Plain-language summary

The notes already give (i) a finite launcher that fires a narrow wave packet down a line from a single occupied site, but with nothing at the far end (`COMMON_PRODUCT_RESONANT_LAUNCH...md:44-80`); (ii) a mediator-plus-vacancy theorem that turns any finite number-conserving positive clock network into a controlled hopping link with complete-output error (`REAL_MEDIATED_VACANCY_NETWORK...md:197-234, 273-370`); (iii) a six-site ladder that is perfectly transparent at one momentum with sector-dependent phase (`...NETWORK...md:379-487`); and (iv) a packet theorem on infinite leads that is only an asymptotic statement (`...NETWORK...md:578`). What nobody had is the piece in the middle: what the actual output looks like at a finite time when a launched packet (not a stationary wave, not an infinite-time limit) goes through the ladder.

This attempt closes that middle piece for the ladder core. It shows, for any starting vector sitting on the incoming lead, an exact formula for the outgoing lead at every time, plus an explicit complete-output error bound. It also finds two things the source does not mention: the ladder has one bound state just above the band in each sector, and it has sharp resonances only about 0.03 away from the design momentum. The scattering stage costs error proportional to the launcher's Poisson-tail amplitude (about 1.7 rho or 5.2 rho), not its bandwidth. What is not done: removing the finite launcher's far end and the finite output cut from the infinite-lead formula. That step is the first unresolved one.

## 1. Setting and premises (all ASSUMED unless stated)

1. [ASSUMED] Axioms read as: Lattice, Qubit, Admissibility, Record give a nearest-neighbour lattice of qubits, nothing more. No dynamics is supplied by them (`docs/MINIMAL_AXIOMS_2026-06-29.md:114-130`). All Hamiltonians below are supplied devices, exactly as in the three notes. No new primitive is used; `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive` are not needed.
2. [ASSUMED] Supplied device, from `REAL_MEDIATED_VACANCY_NETWORK...md:18-34, 99-177, 386-392, 450-457`: the positive mediator (NV2), the repulsion-protected controlled link, the compensated one-head comparison generator, and the six-clock ladder with coefficients f = 1/sqrt(8), a = c = f/2, b = 3f, eta_L = eta_R = 1 - 5f/2, eta_A = eta_B = 2 - 5f/2, eta_v = eta_w = 2 - 3f/4, controlled hop -p (p = old X1X2 = +-1) on A-B. Units: lead hopping 1, lead diagonal 2.
3. [ASSUMED] Launcher from `COMMON_PRODUCT_RESONANT_LAUNCH...md:10-80`: emitter coupled by gamma = rho j to a lead, packet profile beta_n(t) (line 54-58), window lemmas. Imported, not re-proved. Only a numerical consistency check is run (check.py E5).
4. [ASSUMED] One-head sector: the emitter is the only occupied clock site; old/mediator/passive reference arbitrary (NV20 handles the rest, see step 15).

## 2. Reconciliation of existing launch results and choice of interface

| Object | Where | What it gives | What it does not give |
|---|---|---|---|
| Resonant launcher | `COMMON_PRODUCT_RESONANT_LAUNCH...md:44-80` | finite device, endpoint seed, complete vector within 3 eps/8 of a normalised packet on [t_minus, T], positive blocks, loads | a plain line with a cap; no ladder, no gate; second cycle not addressed |
| Mediator / clock return | `REAL_TWO_BODY...md:788-1069` | W gate with common clock output on a finite window; W^2 at the next cycle (line 1058-1067) | not a launcher/release; the clock sits in a 3-dim subspace |
| Controlled link in a finite network (NV20, section 9) | `REAL_MEDIATED...md:179-234, 273-370` | complete-output error for ANY finite positive number-conserving clock network incl. launcher+ladder+output, charges only the near blocks | which clock vector the network produces |
| Ladder, stationary | `...md:379-487` | transparency at k = pi/2, t_+- = -(3 +- 4i)/5, positive inventory | not a launch |
| Packets on infinite leads | `...md:490-584` | pole-free band, coarse constants (5)-(6), asymptotic packet statement | explicitly "not a finite-time full-output bound" (line 578) and lists the missing finite-launch items (line 582) |

Choice. NV20 and the launcher are each finite and already complete at their own interfaces. The first unsolved interface is therefore the one between them: finite-time one-head transport of an actual launched profile through the ladder to an output lead, with complete output. That is what this attempt works on. The hypotheses are the enumerated ones above; no impossibility claim is made (the task allows an obstruction only for enumerated hypotheses, and none is found).

## 3. Steps

Labels: PROVED (argument given here), CHECKED (executed by check.py), ASSUMED, READING, SUGGESTED (argument not complete).

### A. Exact algebra of the ladder core (all CHECKED, exact over Q(sqrt 2))

1. CHECKED (A1, A2). All ladder weights and onsites are strictly positive; shifted diagonals at E = 2 are f, f/4, f. Reproduces the source (`...md:455-457`); not counted as new.
2. CHECKED (A3). With zeta = e^{ik}, E = 2 - zeta - 1/zeta, F_p(zeta) = H_core,p - E - zeta (e_L e_L^T + e_R e_R^T), the polynomial D_p(zeta) = det[zeta F_p] equals (1/8) P1 P2 with two explicit quintics over Q(sqrt 2) (listed in check.py). Degree 10.
3. CHECKED (A4). tau_p(zeta) := (1/zeta - zeta)[F_p^{-1}]_RL = (1 - zeta^2) cof_LR(zeta F_p) / D_p and r_p := (1/zeta - zeta)[F_p^{-1}]_LL - 1 give tau_+(i) = -(3+4i)/5, tau_-(i) = -(3-4i)/5, r(i) = 0 exactly (source values).
4. CHECKED (A5). Exact polynomial identity N(z)N(1/z) + R(z)R(1/z) = D(z)D(1/z). Since the coefficients are real, |tau|^2 + |r|^2 = 1 on |zeta| = 1 for every k. (The source proves unitarity by a flux argument; this is an independent algebraic proof for this ladder.)
5. CHECKED (A6). Exact resolvent identity at six rational zeta (1/3, -2/5, 3/4), both sectors, two sources, three observation sites, with transparent boundary conditions: the Green function from left-lead site n' >= 0 to right-lead site n >= 0 is [F_p^{-1}]_RL zeta^{n+n'}. PROVED by hand as well (Schur complement: on the left exterior the solution is u(0) zeta^n plus the Dirichlet half-line Green function; the port equation then has right-hand side zeta^{n'} (zeta^{-1} - zeta)/(zeta^{-1} - zeta) = zeta^{n'}; on the right exterior u(n) = u_R zeta^n).

### B. Bound state and resonance poles (CHECKED, 50-digit roots plus winding number)

6. CHECKED (B1, B3). In each sector D_p has exactly one zero with |zeta| < 1, real and negative: zeta_b = -0.602417 (p = +1), -0.615848 (p = -1), i.e. a bound state of the one-head ladder at E_b = 4.262396, 4.239625, above the band [0,4]. No zero on |zeta| = 1 (so no embedded eigenvalue and no threshold resonance); nearest to the circle: ||zeta| - 1| = 3.68e-4 (p = +1), 2.12e-2 (p = -1). NEW relative to the source, which does not locate the bound state (`...md:572`, "a local product seed has no bound-state component" is only flagged as not asserted).
7. CHECKED (B2). The nearest resonance poles are at |k - pi/2| = 0.0323 (p = +1, |zeta| - 1 = 3.7e-4) and 0.0257 (p = -1). So the source's band of half-width 1e-4 (`...md:538`) is far inside the true pole-free arc, but the transparent point is only about 0.03 from a sharp pole in each sector. This sets how narrow the incoming spectrum must be.

### C. Main theorem (ladder core, infinite leads)

Setting. H_p = one-head Hamiltonian of the infinite two-lead graph (ladder core, left lead n' = 0, 1, ... with n' = 0 the port L, right lead n = 0, 1, ... with n = 0 the port R, as in the source's convention `...md:394`). psi0 = a finitely supported (or l^2) vector on the left lead, norm 1, ghat0(k) = sum_{n'} psi0(n') e^{ik n'}. P_R = restriction to the right lead.

8. PROVED (closed formula; roots from step 6 CHECKED; brute-force confirmation CHECKED in C1). For all real s,

   (P_R e^{-isH_p} psi0)(n) = (1/2pi) integral_{-pi}^{pi} e^{-isE(k)} tau_p(e^{ik}) e^{ikn} ghat0(k) dk + e^{-isE_b} <u_b|psi0> u_b(R, n),   n >= 0,

   with u_b the normalised bound state (u_b(L,n') = v_L zeta_b^{n'}, u_b(R,n) = v_R zeta_b^n, v = null vector of F_p(zeta_b)).
   Proof. For a finitely supported psi0, <delta_{R,n}| e^{-isH} |psi0> = -(1/2 pi i) oint_Gamma e^{-isz} G(z) dz with Gamma around the spectrum. Substitute z = 2 - zeta - 1/zeta. Gamma becomes a circle |zeta| = r0 < |zeta_b| (step 6 shows the spectrum is [0,4] plus E_b only, and G has no other singularity). By step 5, G(R n, L n') = [F^{-1}]_RL zeta^{n+n'} is meromorphic in |zeta| < 1 with one simple pole (step 6). Move the contour to |zeta| = 1, picking up the residue at zeta_b, which is the Riesz projector term. dz = (zeta^{-2} - 1) d zeta and (zeta^{-1} - zeta) turns the integrand into tau e^{ik(n+n')} dk/2 pi. Extension to l^2 by density and unitarity. QED. Disjoint confirmation: C1, maximum deviation 1.9e-13 against dense diagonalisation, two sectors, four states (Gaussian, broadband, port-adjacent), three times, bound-state term required (without it the error is 0.10, C2).
9. PROVED. Let w(s) = U_Z(s) mirror(psi0) be the free whole-line evolution (E(k) = 2 - 2 cos k) of w0(x) = psi0(-x). By step 8, up to the bound-state term, P_R e^{-isH} psi0 = P_R U_Z(s)F^{-1}[tau ghat0]. Hence, with t_c = tau_p(k = pi/2) = -e^{-i theta} e^{+-i theta} (source (8)) and
   e_R := ||(tau_p - t_c) ghat0||_{L^2(dk/2pi)} + |<u_b|psi0>|,
   one has ||P_R e^{-isH} psi0 - t_c P_R w(s)|| <= e_R. (Parseval; restriction is a contraction.)
10. PROVED. Complete output without a square root of the spectral error being wasted on the left lead and core: let a = e^{-isH} psi0 (norm 1 exactly, all sites, core and left lead included), b = t_c P_R w(s), eta = ||(1 - P_R) w(s)||^2. Then ||a - b||^2 <= eta + 2 e_R sqrt(1 - eta) <= eta + 2 e_R.
    Proof. b is supported in the right lead. ||a - b||^2 = ||P_R a - b||^2 + ||(1 - P_R) a||^2 and ||(1 - P_R) a||^2 = 1 - ||P_R a||^2 <= 1 - (sqrt(1-eta) - e_R)^2. Add. QED. Every internal-core and left-lead component of the actual state is thereby accounted for, with no postselection. (check.py E1, E2: measured complete error is below this bound; the square-root loss is real slack, E3.)
11. PROVED. Position bound for eta. Let nbar = sum n'|psi0|^2, sigma0^2 its variance, vbar = <2 sin k>, sigma_V^2 its variance in ghat0. The exact operator identity U_Z(s)^* X U_Z(s) = X + s V(K), V = 2 sin K, gives mean position mu_s = -nbar + s vbar and std at most sigma0 + s sigma_V, so by Chebyshev eta <= (sigma0 + s sigma_V)^2/(mu_s + 1)^2 whenever mu_s + 1 > 0. For the Poisson profile sigma_V ~ sqrt(2) rho (D6), so the bound is usable only for rho < eps/(4 sqrt 2) and the crossing time is about 4/(rho^2 eps), not 1/rho^2. CHECKED (D5): bound dominates the exact free-evolution weight at four times. The exact eta plateaus at the backward-momentum weight (about 0.16 rho^2): backward-moving components never cross.
12. CHECKED + PROVED. Certified spectral constants. tau_p is a rational function with |tau_p| <= 1 on the circle (step 4). A coefficient bound for |N'|,|D'| and a root-product lower bound of |D| on the arc |k - pi/2| <= h give a certified Lipschitz constant Lip_p(h) (e.g. h = 0.005: 3937 for p = +1, 3616 for p = -1; observed sup |tau'| = 3.6 and 37; D1). For the exact launcher profile |ghat0|^2 = rho^2 |1 - z^{m+1}|^2 / (kappa |1 - z|^2), z = a e^{i(k - pi/2)}, kappa = 1 - a^{2(m+1)} (D2, checked against FFT), with |1 - z|^2 >= 4 a delta^2/pi^2:
    e_R <= rho sqrt(pi/(a kappa)) sqrt(Lip^2 h + 4/h)
    (Lipschitz arc plus |tau - t_c| <= 2 outside), about 200 rho after optimising h (D3). Exact values: e_R/rho = 1.737 (p = +1), 5.161 (p = -1), constant to 6% for rho = 0.1 .. 0.02 (D4). So the scattering stage costs O(rho) because of the Poisson tail, not O(bandwidth) = O(rho^2). The source's constants (5)-(6), 4.8e7, are about 1e4 times looser; that is scope cleanup, not counted.
13. CHECKED. End-to-end finite device (single head; positive blocks): emitter, line of M + 1 sites, ladder, output line of N sites. Dense/sparse exact dynamics. rho = 0.10 (2598 sites) and rho = 0.05 (9468 sites). The measured complete error is below launcher-stage distance + sqrt(eta + 2 e_R) (E1, E2); the launcher-stage distance ||psi(t1) - beta(t1)|| is below the sum of the source's component bounds (E5, consistency only). Measured complete errors: p = +1: 0.248 (rho 0.10), 0.144 (0.05); p = -1: 0.541, 0.282, i.e. O(rho). Against the physical target "plain launcher packet times t_p" the errors are 0.152/0.522 (rho 0.10) and 0.076/0.269 (0.05).

### D. The unresolved step and what is imported

14. SUGGESTED, NOT PROVED, FIRST UNRESOLVED STEP (Lemma B). Passing from the infinite-lead formula of steps 8-11 to the actual finite device. Two separate transfers:
    (a) Right cut: replace the half-infinite output lead by the capped finite one. The source's Duhamel/cone argument (`COMMON_PRODUCT_RESONANT_LAUNCH...md:68-70`) applies verbatim with the hopping-operator norm of the device (largest hopping row sum 2.237 from check.py F1), giving a super-exponentially small term once the output length exceeds about 4 e ||T|| times the elapsed time.
    (b) Left terminus: the launcher is a finite cavity ending at the emitter. The infinite-lead formula assumes a half-infinite left lead. The backward-momentum part of the launched profile (weight about 0.16 rho^2, amplitude about 0.4 rho) is reflected by the terminus and returns. A direct Duhamel estimate appears to fail (READING, an order-of-magnitude estimate not run): Cauchy-Schwarz with local smoothing gives sqrt(time) x rho = O(1) over the 1/rho^2 crossing time. The route I see: cut the packet's exponential back tail (weight below (eps/64)^2 beyond X = 2 ln(64/eps)/rho^2 behind the front), apply the cone bound to the remainder, and require the terminus to be farther than the cone reaches during the whole crossing. That forces launch time t1 >= (4 e ||T|| s_after + X)/2 with s_after ~ 4/(rho^2 eps), which is longer than the source's window T = 2u0 = 2 L/rho^2 by a factor of order 1/(L eps). The source's component lemmas have explicit time dependence (survival, geometric, dispersion 2 rho (j t)^{1/6}) so an extension looks plausible, but the source's window composition (`...md:44-52`) was not redone, and monotonicity in rho at fixed L was assumed. Not proved. The numerical evidence (E1, E2) shows the end effect is below the measured error at the sizes tested.
15. ASSUMED (imported, not re-proved). NV20 and section 9 for the mediator and vacancy layers: error 164 lambda [1 + |s|(U + M)] + (2/U)(1 + |s| M) with M <= ||B_near|| <= 4 + 9f (blocks incident on A,B; all launcher and output blocks are disjoint from {A,B}, so section 9's local-support form applies; `REAL_MEDIATED...md:273-370`). The common scalar -e^{-i theta} and the sector phases combine into W exactly as in the source (`...md:468-470`).
16. CHECKED arithmetic, conditional on 14 and 15 (F1-F3). For eps = 1/10 the composed sufficient family (rho = 3.9e-7 from e_R <= 200 rho and the square-root loss; launch time 3.3e15; port at 6.6e15; S = b_eff t = 3.6e15; U = 2e18; lambda = 2e-38; 1.3e16 qubits and 2.6e16 positive blocks; incident bound 4 + 8 lambda + lambda^2 C_load = 4.000...) satisfies the incident cap Lambda = 5. The counts use the compensated formula (clock qubits + 4 + q positive blocks). These are astronomically large sufficient constants, not a practical device, not optimised, and F2 shows the cost rises by about 1e5 per decade of eps. The arithmetic does not verify step 14's timeline beyond using it.

## 4. What is new relative to the sources

NEW (scoped): steps 6-7 (bound state above the band; pole positions), 8-11 (all-time output formula and complete-output chain for any left-lead vector through this ladder), 12 (O(rho) scaling with exact constants and a certified bound), 13 (end-to-end finite-device consistency), plus the crossing-time analysis in 11 and 14 that shows the source's launch window is too short for any cone-based finite release.
NOT new / not counted: the scattering matrix and t_p (steps 1, 3), the packet normalisation and asymptotics, constants cleanup, retrieval of the three notes, the known W^2 / no-halt limitation (`REAL_TWO_BODY...md:1058-1067`).
Scope of the HIT line in check.py: the ladder-core finite-time theorem on infinite leads with complete output. It is not the finite launcher-to-output theorem asked for; that needs step 14.

## 5. Not done and why

- No full finite theorem: step 14 (Lemma B) is open; steps 15-16 depend on it and on imports.
- A rigorous bound for eta better than Chebyshev, and a left-lead/core exact formula that would remove the square-root loss in step 10, are not attempted.
- No claim about physical supply, preparation, capture, reset, reuse, permanent halt, or second cycles (W^2 at the next return is untouched).
- No obstruction was found for the enumerated hypotheses; none is claimed.
