# J:derive:review-20261012-excluded-walk-preparation:a1 — excluded-walk preparation and observable control

Worker: Claude Sonnet 5.5, same family as the sources, unrefereed. Nothing below is an audit verdict or a retained status.

## Plain-language summary

The supplied model is a two-particle walk whose pair, once the same-site configuration is removed, has a huge set of zero-energy states: the free "flat band" of transverse spin states at every relative momentum, plus one extra singular state (zeta) that exists only because of the removal. Earlier notes (landed on main) show that a packet prepared in the free positive band near energy lambda, projected once and normalized once, develops a measurable canonical-current change, but only in a two-scale regime: total momentum about lambda^2 or lambda^3 and a very long time. The question here was what happens for generic total momentum K of order lambda at the inverse-energy time 1/lambda.

What I did:

1. Rebuilt the two auxiliary results (the high-momentum leakage lower bound and the cone-packet counterexample) from the model, with a check that shares no code with the sources (Steps 1-6). The canonical-current cancellation is kept exactly. No defect found in either source result.
2. Proved a new sufficient condition under which the zero-space state comparison IS uniform, and showed it carries over to the canonical current (Steps 7-14). The condition is that the preparations carry no mass at the cone scale |q| of order lambda. The counterexample is exactly a violation of it.
3. For the actual band preparation at K of order lambda (the first branch of the target) I could not close the problem. I proved an exact amplitude identity, a bound showing the cone-scale region can change the dressing amplitude by an amount of the same order as the dressing itself, and computed (numerically) that this source is not small (Steps 15-18). The first unresolved step is Step 19.

## Reading statement

Read in full before choosing premises: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines) on main `a77a3449c91a753b06ce2a63876cd460b62cb4cf`. Both pinned source objects were verified by hash and read in full (all 457 and 549 lines; hashes in `RECOVERY_STATUS.json`). Main's projected-band note (`docs/EXCLUDED_WALK_PROJECTED_FREE_BAND_CANONICAL_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md`) was read in full (880 lines). The memory-current, quantitative-memory and boost notes were read in their headers, scope statements and the passages quoted below, and searched for relevant claims; their proofs were not re-read in full.

## Step 0. Setting and premises

- ASSUMED (supplied model, not axiom content): the two-spin Weyl walk, continuous generator clock, antisymmetric pair sector, same-site exclusion, spatial coordinates and the canonical additive symmetric energy placement. The axiom memo says a kinetic branch or time metric is downstream content needing its own derivation (`docs/MINIMAL_AXIOMS_2026-06-29.md:114-130`); the registry lists only scale-reference, kinetic-isotropy and realized-state primitives (`PRIMITIVE_REGISTRY_CHECK.md:31-129`). Nothing here uses or derives them. Every statement is a statement about the supplied model.
- Notation (the sources' notation). Relative torus measure mu = dq/(2pi)^3. s = sin q, eps = |s|, n = s/eps, c = constant normalized singlet, T_j = sigma_{1,j} c. In (c, T) coordinates H0(K,q) = sigma_1.sin(K/2+q) + sigma_2.sin(K/2-q), P = 1 - |c><c|, H_D(K) = P H0 P on ran P, H_* = H_D(0). F = pointwise projector on transverse triplets, I0 = int 1/(4 eps^2), zeta = n.T/(2 eps sqrt(I0)), Pi = F + |zeta><zeta|, Z = ran Pi, Q = P - Pi. E_sigma = spectral projector of H_* onto 0 < |E| <= sigma. B_kappa u = i d x u with d_j = kappa_j cos q_j (zero on singlets), b = |kappa|, A_kappa = Pi B Pi, g = B zeta, U_lambda(tau) = exp(-i tau H_D(lambda kappa)/lambda). Physical time is t = tau/lambda ("inverse-energy time" for band energy of order lambda).
- Fixtures: the exact section of check.py uses a rational discrete cubic-orbit q-measure (96 points). The float sections use Pauli matrices and discrete weighted q-measures. A fixture is only used to test an inequality whose proof is written below with fixture-independent constants. Continuum constants are computed by quadrature (Bessel/heat-kernel for I0; spherical quadrature in q-space for shells). The fixtures have no pair-parity restriction; no proof below uses parity.

## Part A. Recovered lemmas (self-contained)

**Step 1 [PROVED; CHECKED E1, E1b, E2].** Zero space. With H0(0) = [[0, 2 s^T],[2 s, 0]], H0(0) zeta = c/sqrt(I0) (direct multiplication) and zeta is orthogonal to c pointwise, so H_* zeta = P H0 zeta = P c = 0. If psi is in ran P and H_* psi = 0 then H0 psi = alpha c, so psi - alpha sqrt(I0) zeta is a free-kernel vector; hence ker H_* = ran F + span(zeta) = Z. Exact check: on a 48-point rational fixture the rank of P H0 P over Q gives kernel dimension 2N + 2 on the whole space, i.e. 2N + 1 physical (the extra one is the auxiliary c). There is no gap at zero.

**Step 2 [PROVED; CHECKED E3, E4].** H_*^2 = 4 P eps^2 P - 4 eps^2 F - 4|v><v| with v = s.T (from H0^2 = 4 eps^2 (1 - F), Fc = 0, H0 c = 2v). With L_a = P cos(2 q_a) P + |v_a><v| + |v><v_a|, v_a = s_a T_a, summing over a gives sum_a L_a = 3P - H_*^2/2 - 2 eps^2 F. Both are verified exactly on all 384 coordinate unit vectors of the rational fixture.

**Step 3 [PROVED; CHECKED E5].** Canonical-current cancellation. By cubic symmetry <zeta, s_a^2 zeta> = 1/(12 I0), <v, zeta> = 1/(2 sqrt(I0)), <v_a, zeta> = 1/(6 sqrt(I0)). So the free centred term gives <zeta,(cos 2q_a - 1) zeta> = -1/(6 I0) and the placement correction gives +1/(6 I0); the sum is zero. The exact fixture gives -1/6 and +1/6 for unnormalized zeta (divide by I0), summing to 0. Consequence: the leakage in Step 5 is a momentum-space leakage of the state, not a current defect.

**Step 4 [PROVED; CHECKED E6, A2].** Cutoff inverse and averaging. Write a physical vector with no transverse part as x = (F_s, G_x) (singlet profile F_s with zero mean; longitudinal profile G_x), orthogonal to zeta, i.e. int G_x/(2 eps) = 0. For 0 < r put m_r = int (G_x/2eps) 1_{eps>=r} and xi_r = (P_s[(G_x/2eps) 1_{eps>=r}], F_s/(2 eps)). Then exactly H_* xi_r - x = -[G_x 1_{eps<r} + 2 eps m_r] n.T (checked in exact arithmetic for five cutoffs, with the cutoff mean m_r retained: dropping it breaks the identity). Since M_T H_* xi = i [e^{-iTH_*} - 1] xi / T,

    ||M_T x|| <= ||H_* xi_r - x|| + 2 ||xi_r|| / T.                     (4.1)

Applied to the band family of Step 5 with r = 1/T this reproduces the source's E_lambda(T) (I re-derived each constant: for r <= 5 lambda/8 the residual equals A sqrt(r)/sqrt(I0) at most, ||xi_r|| <= 2/(a lambda n) + beta sqrt(I0)/n + 3A/(4 sqrt(I0 r)), using int_{eps<r} eps^-2 <= r and int_{eps>=r} eps^-4 <= 9/r). Inequality (4.1) is also tested numerically with random xi (A2).

**Step 5 [PROVED given the continuum constants; CHECKED C1-C7, A1-A4].** High-momentum leakage lower bound for globally projected positive-band packets at K = 0. Let a = 5/4, Gamma = 1_{[a lambda, 7 lambda/4]}(H0(0)), w = ||Gamma zeta||^2, phi = Gamma zeta/sqrt(w), beta = <c,phi>, n_l = sqrt(1-beta^2), chi = P phi / n_l (one global normalization), A = <zeta, chi> = sqrt(w)/n_l. For T >= 8/(5 lambda), Step 4 gives ||M_T chi - A zeta|| <= E(T) = 4/(a lambda n_l T) + 2 beta sqrt(I0)/(n_l T) + 3A/(sqrt(I0) sqrt(T)). Let Qf be multiplication by 1_{eps>=1/2}, Z_Q = ||Qf zeta||^2 >= 23/324. By Jensen, (1/T) int_0^T ||Qf e^{-itH_D} chi||^2 dt >= ||Qf M_T chi||^2 >= [A sqrt(Z_Q) - E(T)]_+^2. The time-zero weight of chi on eps >= 1/2 is only the c-tail beta^2 ||Qf c||^2/n_l^2 <= lambda^3 (C7).
Checked by independent quadrature (not the source's formulas): I0 = 0.25273101 (Bessel integral; spherical quadrature agrees to 1.3e-4 relative), the cone-integral bounds int_{eps<r} eps^-2 <= r, vol <= r^3/3, int_{eps>=r} eps^-4 <= 9/r (C2), the amplitude bounds sqrt(lambda)/(3 pi) <= A <= 2 sqrt(lambda) (C3: in fact A/sqrt(lambda) = 0.2239 for all lambda <= 1/16), the asymptotics w = lambda/(8 pi^2 I0), beta^2 = 9 lambda^3/(32 pi^2) (C4), and at T = lambda^(-7/4) the bound / lambda converges to 0.0383 as lambda goes from 1e-9 to 1e-12 (C6), above the source's explicit constant 23/(11664 pi^2) = 2.0e-4. Order lambda in the averaged weight versus lambda^3 at time zero. The nonzero-K extension (source L17-L22, with a one-time global projection and |K| <= lambda^(5/2) scale) is imported, not re-derived here. It is also not needed below.
Scope: this is a statement about where the state goes. The current response of the same family is Step 3 plus the two-scale results on main.

**Step 6 [PROVED in the source; its pieces re-derived and CHECKED K1-K5, U4].** Normalized cone packet counterexample to operator-norm convergence. kappa = e_1, eta = 1/100, Omega_lambda = two balls of radius lambda eta about +-lambda e_3 (normalized volume lambda^3 eta^3/(3 pi^2)), u_lambda = the unit odd transverse field of constant modulus on Omega_lambda with direction (1 - nn^T) e_2 on the positive ball and its negative on the other. Then

    liminf_{lambda->0} || U_lambda(tau*) u_lambda - e^{-i tau* A_kappa} u_lambda || >= 2/sqrt(5) - (8 + 4 tau*) eta > 1/sqrt(5),   tau* = pi/sqrt(5).

Argument (re-derived): (i) A_kappa u_lambda stays within 2 eta |tau| of u_lambda because the diagonal block i (d.n) n x has norm <= 2 eta on Omega and ||1_Omega g|| <= sqrt(lambda eta^3/(48 I0))/(1-eta) (I recomputed this constant independently from eps >= (2/pi)|q| and the ball volume: it matches). (ii) The excluded generator equals the free one plus V = -|h><c| - |c><h|; free evolution preserves the q-support, ||V u|| is O(lambda^(3/2)) on it, so the rescaled Duhamel error is O(sqrt(lambda)). (iii) On the balls the rescaled free symbol tends to M(p) = [[0, 2p^T],[2p, i kappa x]]; at p = e_3 the invariant block M0 has M0^3 = 5 M0, and exp(-i tau* M0) T_2 = (3/5) T_2 - (4i/5) c, a change of norm 2/sqrt(5) (exact, sympy: K1, K2).
Checks: K3 confirms M0 from the actual Pauli symbol at lambda = 1e-6 (this validates the sign of the i kappa x block); K4 confirms the pointwise mismatch is >= 0.8875 for 800 sampled p in the eta balls (minimum 0.8875, above the source's 0.7582 floor); U4 builds an actual finite fixture with the exact projection P and torus-volume weights and finds ||U_lambda(tau*)u - e^{-i tau* A}u|| = 0.894 at lambda = 1e-2, 1e-3, 1e-4 (the eta -> 0 value 2/sqrt(5)). The counterexample is a statement about states, not currents (the source says so; Step 13 shows why).

## Part B. A sharp preparation class for uniform state comparison (NEW)

**Step 7. Statement of the problem [definition].** Domain: unit vectors x of the zero space Z (no band projection, so no renormalization question; for total-momentum packets the global norm in the direct integral is one). Time: |tau| <= T fixed, physical time tau/lambda, K = lambda kappa with kappa fixed (or in a bounded set). Norm: the Hilbert norm. Comparison: U_lambda(tau) x versus e^{-i tau A_kappa} x. "Uniform" means the supremum over a set S_lambda of unit vectors tends to zero with lambda.
Known (sources): for a fixed x the error tends to zero (D8 of the degenerate-dynamics probe, vector-dependent), and Step 6 shows it is not uniform on the unit ball.

**Step 8. Lemma E [PROVED; CHECKED L1].** Let f be in L^2(mu) with int f/eps = 0 (equivalently y = f n.T is orthogonal to zeta). For all sigma, r > 0,

    ||E_sigma y|| <= (1 + sqrt(E2 J1(r))) ||f 1_{eps<r}|| + sigma ||f|| / (2 r),

with E2 = int eps^2 = 3/2 and J1(r) = int_{eps<r} eps^-2 <= r (r <= 1/2).
Proof. Put m_r = int (f/2eps) 1_{eps>=r} = - int (f/2eps) 1_{eps<r} (zero mean) and xi = (f/2eps 1_{eps>=r} - m_r) c; it has zero mean so lies in ran P, and H_* xi = (f 1_{eps>=r} - 2 eps m_r) n.T because P acts trivially on a vector with no singlet part. Then y - H_* xi = (f 1_{eps<r} + 2 eps m_r) n.T. By Cauchy-Schwarz |m_r| <= ||f 1_{eps<r}|| sqrt(J1)/2, so ||2 eps m_r|| <= sqrt(E2 J1) ||f 1_{eps<r}||. Also ||xi|| <= ||f||/(2r). Finally E_sigma y = E_sigma (y - H_* xi) + E_sigma H_* xi, and ||E_sigma H_* xi|| <= sigma ||xi||. No pointwise bound on f is used (the main-note version assumes |f| <= L/eps). Checked on 1000 random, singular and cone-concentrated f on a fixture with a near-cone shell (worst ratio of left side to bound 0.66).

**Step 9. Lemma N [PROVED; CHECKED L2].** Cone mass is carried by the effective orbit. Write e^{-i tau A} x = u(tau) + alpha(tau) zeta, u in ran F. Then i u' = D u + alpha g and i alpha' = <g,u>, where D = F B F is multiplication by a pointwise Hermitian matrix (D u = i (d.n) n x u) and |alpha| <= 1. Multiplication by 1_{eps<r} commutes with D, so d/dtau ||1_{eps<r} u|| <= |alpha| ||1_{eps<r} g||, with |g| <= b/(2 eps sqrt(I0)) and so ||1_{eps<r} g|| <= b sqrt(J1(r))/(2 sqrt(I0)). Hence

    ||1_{eps<r} u(tau)|| <= ||1_{eps<r} F x|| + |tau| b sqrt(J1(r))/(2 sqrt(I0)).

**Step 10. Lemma G [PROVED; re-derivation of D9-D11; CHECKED S4, U1].** Let H = H_*/lambda + B + R with ||B|| <= b and ||R|| <= r_lambda = lambda b^2/4 + lambda^2 b^3/24 (Taylor bounds on the Pauli symbol, checked S3-S5). For x in Z, ||x|| = 1, sigma > 0 and v(tau) = e^{-i tau A} x, set y_sigma = -H_*^{-1} 1_{|H_*|>sigma} B v (norm <= b/sigma, derivative norm <= b^2/sigma) and w = v + lambda y_sigma. Using H_* v = 0 and B v in ran P one finds exactly i w' - (H_*/lambda + B) w = -E_sigma B v + lambda (i y_sigma' - B y_sigma). Duhamel for the self-adjoint H_*/lambda + B, then for R, gives

    sup_{|tau|<=T} ||U_lambda(tau) x - v(tau)|| <= 2 lambda b (1 + T b)/sigma + T M + T r_lambda,   M = sup_{|tau|<=T} ||E_sigma B v(tau)||.

**Step 11. Theorem U [PROVED; CHECKED U1, U2, R2].** For |tau| <= T, x in Z unit, any 0 < sigma, 0 < r <= 1/2, with w_r(x) = ||1_{eps<r} F x||,

    ||U_lambda(tau) x - e^{-i tau A_kappa} x|| <= 2 lambda b (1+Tb)/sigma + T r_lambda
        + T b (1 + sqrt(3r/2)) [ w_r(x) + sqrt(3) (T b + 1) sqrt(r) ] + T sigma b/(2r).

Proof. B v = B u + alpha g with g in ran F. E_sigma kills F and zeta, so E_sigma B v = E_sigma y with y = Q(longitudinal part of B u) = f n.T, f = n.(i d x u) - beta/(2 eps sqrt(I0)), beta = <zeta, B u>. Then int f/eps = 0, ||f|| <= b, and ||f 1_{eps<r}|| <= b ||1_{eps<r} u|| + b sqrt(J1)/(2 sqrt(I0)). Insert Step 9 for u(tau) and Step 8 for E_sigma y, then Step 10; finally J1 <= r, E2 = 3/2, 1/(2 sqrt(I0)) <= sqrt(3) (I0 >= 1/12). Tested on 24 (lambda, x, T) cases with the fixture's own constants (U1) and numerically along lambda -> 0 in the continuum constants for x = zeta (R2: the bound falls as lambda^(1/4)).

**Step 12. Corollary (the class) [PROVED; CHECKED R1, R2, U4, U5, K5].** Let S_lambda be sets of unit vectors in Z. Suppose for every R > 0, limsup_{lambda->0} sup_{x in S_lambda} ||1_{eps<R lambda} F x|| = 0 ("no cone-scale mass"). Then sup_{x in S_lambda, |tau|<=T} ||U_lambda(tau) x - e^{-i tau A_kappa} x|| -> 0 for every T and kappa. Proof: a diagonal argument gives rho_lambda with rho_lambda/lambda -> infinity, rho_lambda -> 0 and sup w_{rho_lambda} -> 0; take r = rho_lambda, sigma = sqrt(lambda rho_lambda) in Step 11. Rate: if w_r(x) <= C r^theta on S for all r <= 1/2, the error is O(lambda^(theta'/(1+2 theta'))) with theta' = min(theta, 1/2), at most lambda^(1/4) (r = lambda^(1/(1+2 theta')); exponents checked symbolically in R1). Examples: any set bounded in L^p (p > 2) has theta = (3/2)(1 - 2/p) by Holder and the volume bound r^3/3; the single vector zeta has theta = 1/2 (as w_r(zeta) <= sqrt(r)/(2 sqrt(I0))).
Sharpness (what is and is not claimed). The counterexample of Step 6 has w_r = 1 for every r >= (1+eta) lambda, so it violates the condition; U5 shows that moving the same transverse vector out to |q| = R lambda makes the error fall (0.894 at R = 1, 0.100 at 10, 0.008 at 100, 0.001 at 1000). The condition is not necessary: K5 shows that for p0 parallel to kappa the cone-scale mismatch vanishes exactly, and it grows to 2/sqrt(5) as the angle between p0 and kappa goes to pi/2. So the claim is "sufficient, and sharp in the sense that the violating family in the source is exactly the one that fails"; an if-and-only-if statement would need the direction of concentration and is not proved. The general-direction failure (angle between 0 and pi/2) is CHECKED at the cone-scale matrix level only.

**Step 13. Corollary (canonical current) [PROVED given D14 from main; CHECKED L3, L4].** The bounded canonical current J_a(K) = P[sin K_a cos 2q_a]P - |h'_a><h| - |h><h'_a| (main, projected-band note, J5-J6, D14) satisfies ||J_a(lambda kappa)/lambda - kappa_a L_a|| <= lambda^2 [...] (imported D14; L3 confirms O(lambda^2) scaling on the fixture, ratio 100.0 for a factor 10 in lambda). With v(tau) in Z and psi = U_lambda x,

    | <psi, J_a psi>/lambda - kappa_a <v, calJ_a v> | <= ||J_a/lambda - kappa_a L_a|| + 2 |kappa_a| (1+sqrt 3) ||psi - v||,

(calJ_a = Pi L_a Pi; <v, L_a v> = <v, calJ_a v> since Pi v = v). So on a class as in Step 12 the current converges uniformly on compact tau intervals, to kappa_a <v(tau), calJ_a v(tau)>, with the explicit rate of Step 11. This is a uniform-current statement for zero-space preparations: it does not apply to a band preparation (Step 18).

**Step 14. Corollary (normalizable total-momentum packets) [PROVED; CHECKED L5].** For a section Psi(kappa) in Z over a bounded kappa set, global norm one, and K = lambda kappa (measure dK = lambda^3 dkappa, unchanged norm; no fiberwise renormalization), Step 11's bound is linear in ||Psi(kappa)|| and in the fiber near-cone mass, and (a+b)^2 <= 2a^2 + 2b^2 gives

    ||U_lambda(tau) Psi_lambda - e^{-i tau A} Psi_lambda||^2 <= 2 A0^2 + 2 A1^2 ||1_{eps<r} F Psi||^2_global,

with A0, A1 the sums of the r-independent and the w_r-coefficient terms with b replaced by sup b. So uniform global convergence holds when the global near-cone mass at scale R lambda tends to zero for every R.

## Part C. The band-preparation interface at K = lambda kappa (PARTIAL)

**Step 15 [PROVED; CHECKED U3].** For any psi_0 in ran P and psi_tau = U_lambda(tau) psi_0, the dressing amplitude alpha(tau) = <zeta, psi_tau> obeys exactly i alpha' = <g + R_lambda zeta, psi_tau>, because (H_D(lambda kappa)/lambda) zeta = (H_*/lambda) zeta + B zeta + R zeta and H_* zeta = 0. g = B zeta is transverse and orthogonal to zeta. The amplitude changes only through the overlap of the state with g (to order lambda).

**Step 16 [PROVED].** Any part of the state on eps < r changes alpha by at most |<g, 1_{eps<r} psi>| <= b sqrt(J1(r))/(2 sqrt(I0)) <= sqrt(3) b sqrt(r) per unit tau. For the band preparation, whose whole transverse content lives at eps in [5 lambda/8, 7 lambda/8] (r of order lambda), this is O(sqrt(lambda)): the same order as the initial dressing A_lambda = 0.2239 sqrt(lambda) (C3). So order counting alone neither allows the cone-scale region to be dropped nor shows it dominates.

**Step 17 [CHECKED I1-I4].** Cone-scale computation. Take the positive-band packet phi (a flat radial profile on |p| in [5/8, 7/8], p = q/lambda), kappa = (1,1,1), and evolve each fiber with the exact Pauli symbol H0(lambda kappa, q)/lambda at time tau. The transverse (K = 0 flat-band) population is O(1) and stable as lambda goes from 1e-3 to 1e-4: 0.0218, 0.0770, 0.2080, 0.5095 at tau = 0.25, 0.5, 1, 2 (I2). The overlap <g, u_shell(tau)>/sqrt(lambda), with exact g and the exact torus measure on the shell, converges as lambda -> 0 to the nonzero values 0.039, 0.070, 0.090, 0.133 (I3). Integrated over tau in [0,2] it is 0.17, against A_lambda/sqrt(lambda) = 0.2239 (I4). These are first-order source coefficients for the dressing amplitude, not an evolved-state computation: no claim is made about the sign or size of the resulting current change.

**Step 18 [READING; follows from Steps 12, 16, 17].** (a) The two-scale argument on main (delta = 2^-68 lambda^2 and later delta = lambda^3) makes the band component fast against the zero-space motion, so the band decouples from the dressing. At K = lambda kappa and tau/lambda they are comparable and the decoupling is not available; Theorem U does not apply to the band preparation, whose Q-part is not in Z and sits entirely at the cone scale (w_{R lambda} = 1 for the band vector). (b) The shell contributes to alpha at the same order as the initial dressing (Steps 16, 17), so the zero-space evolution of the initial amplitude A_lambda zeta alone is not the leading-order prediction. (c) Canonical-current response at K of order lambda is of order lambda^2 (= lambda |kappa| times the far-region weight of order A_lambda^2); the trivial bound is |Delta J_a| <= 2 ||J_a|| <= 2 (1+sqrt 3) lambda |kappa_a|. Neither the sign nor the size of the order-lambda^2 coefficient is determined here, and I assert no decay or drift law.

**Step 19 [UNRESOLVED; this is the first failing step].** Prove, for the band preparation Chi_{lambda,K} (free positive-band packet with total momentum lambda kappa, one global projection and one global normalization) at physical time tau/lambda, that

    U_lambda(tau) Chi = (cone-scale free evolution of the band part) + (zero-space evolution of the far part, driven by the cone-scale transverse source of Step 17) + o(sqrt(lambda)) in L^2.

This is the matching of cone-scale dynamics to the global dressing tail that the degenerate-dynamics source names as the next obligation. Without it the order-lambda^2 coefficient of the canonical-current change cannot be written down, let alone bounded below or above.

## What is new, and what is not

- Retrieval, hashes, the corrected scope notes: not new.
- Step 6 and Steps 1-5: recovered from the sources and cross-checked with code that shares nothing with theirs; no defect found. Step 5's explicit constant is checked at 0.0383 lambda against the source's conservative 2.0e-4 lambda (a quantitative improvement for K = 0 only, from the numerics, not a proof). The nonzero-K leakage extension is imported unverified.
- NEW (scoped, same-family, unrefereed): Steps 8-14. A lemma on the spectral mass of longitudinal vectors without pointwise bounds (Step 8), propagation of cone mass (Step 9), a set-wise explicit state-comparison theorem on the zero space with a class condition and rate (Steps 11-12), and its uniform canonical-current and total-momentum-packet corollaries (Steps 13-14). The main-note estimate Q11 is for the single vector zeta and states that no unit-ball estimate is asserted. A scoped grep of `docs/EXCLUDED_WALK_*` on main for equi-integrability or cone-scale criteria found none; this is not a global novelty claim, and no open PR with this title exists (`gh pr list`).
- NEW but only CHECKED: Step 17's cone-scale source coefficients.
- NOT done: canonical-current response of band preparations at K of order lambda (Step 19). Nothing here shows a decay law, a lower bound for arbitrary preparations, or that momentum leakage is a current defect (Step 3 says the opposite).

## Checks

`check.py`: 49 checks, TOTAL PASS=49 FAIL=0, 77 s wall (about 45 s CPU) in one process. Exact (Fractions, sympy): E0-E6, K1, K2, R1. Quadrature/float: C1-C7, A0-A4, S1-S5, K3-K5, U1-U5, L1-L5, R2, I1-I4. Five source-copy mutants (sign of the i kappa x block, cos 2q coefficient, dropped cutoff mean, a weakened Lemma E bound, sign of h') were each run: every one made at least one check FAIL (K5; E4+E5; E6b; L1; L3). Not every check is mutation-tested.

## Source mismatch notes

Main's boost note is not byte-identical to the PR9484 head `773321aa8fdfccc05248682dfc96bf94215034a2`: only editorial lines differ (link targets, historical-preamble wording, an appended N1-N8 scope record); main's version was used. The memory-current and quantitative-memory notes were not read in full, so any overlap with Step 17 in their later sections (for example Section 15 of the memory note) was not ruled out.
