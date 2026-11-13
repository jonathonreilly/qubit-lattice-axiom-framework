# FINISH row 862, gap-pe-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Row 862. Author: Claude Fable 5.2 (max effort). Date: 2026-11-12.
Clone commit: 2b6acd1732dde4e18293f0fe0e2814edbca36da3 (/Users/jonreilly/ym4d-lead/clone, pulled --ff-only, already up to date).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Marks: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE, OPEN.

## Target

Lemma PE (restricted-ensemble expansion) of D/library/gap-s1-opus.md lines 530-600 (row 842, unchecked).
With that file's Theorem BAD and Theorem CH-D it would give Theorem S1 in the form (S1-loc) or (S1-T):
for each n >= 2 and beta >= beta_0(n), the Wilson SU(2) measure on the twisted thin torus
(Z/n)^2 x (Z/M)^2, centre twist in the thin plane, has a transfer-matrix gap in a base direction,
uniformly in M.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read the source: gap-s1-opus.md lines 530-600 (Lemma PE), then the statements it uses
   (Theorem BAD, Theorem CH-D, G2, G3, Lemma L, (S1-loc), (S1-T)). Record exact statements with line numbers.
2. Fix the reduction: what exactly PE must deliver for (S1-T). Choose the route for the thin geometry
   (2D polymer expansion in the base, or a base transfer-matrix argument). Record the fact tests the route must pass.
3. Local Peierls bound: conditional cost of a bad region given its boundary, explicit in n and beta.
4. Chart Jacobian (Faddeev-Popov) and the quadratic form on a good region: bounds explicit in n and beta.
5. Gaussian decoupling across blocks: the massive covariance (mass from the twist, SU(2) only) and its decay.
6. Sum over Z_2 labels and polymer activities; convergence criterion (Kotecky-Preiss) with explicit constants.
7. Assemble: state Lemma PE as proved or its strongest proved part; state (S1-T) with all hypotheses; run the fact tests
   (U(1) Coulomb must fail; Q_8 and 2T; Dobrushin caps; (AN1)).
8. Final status table and RESULT line.

## Log

### Step 1a. Reading of D/library/gap-s1-opus.md (all 670 lines; S1O below)

Short names: S1O = D/library/gap-s1-opus.md; CH = D/library/gap-twist-chart.md.

- READ S1O:125-166 (setup). Lambda = (Z/n)^2 x (Z/M)^2; site y = (x, b), x fibre, b base. Per base point: n^2 sites,
  4 n^2 links, 6 n^2 plaquettes. A^tw = sum_p d_p, d_p = 1 - (1/2) tr U_p off P_0, 1 + (1/2) tr U_p on P_0;
  P_0 = the (1,2)-plaquettes at fibre point (n-1, n-1), one per base point. 0 <= d_p <= 2. mu^tw = Z^{-1} e^{-beta A^tw} dU.
  Twist eater V: U_1 = i sigma_1 on x_1 = n-1, U_2 = i sigma_2 on x_2 = n-1, else 1; A^tw(V) = 0.
  Symmetries: base translations, base reflections, base centre flips.
- READ S1O:178-197 (Lemma RP). mu^tw is reflection positive for base reflections through site planes, M even.
  So a transfer matrix in a base direction exists (as a positive form; the note does not write the operator).
- READ S1O:240-256 (Theorem BAD). n >= 2, M even >= 4, beta >= 1, 0 < delta <= 2, every set S of base points:
  mu^tw(every b in S is delta-bad) <= eps^{|S|}, eps = 6 n^2 beta^{6 n^2} e^{27 n^2} e^{-beta delta/4}.
  Remark 2 (S1O:277): it is a bound for the torus measure, NOT for conditional measures.
- READ S1O:305-317 (Theorem CH-D). D connected, all plaquettes of Sigma_D with d_p <= delta <= delta_0(n). Then
  U^h = eps V exp(X), X transverse (D_0^* X = 0), sup|X| <= C(n) sqrt(delta), [eps] in H^1(K_D; Z_2) a gauge-invariant
  datum; X unique (h unique up to sign) among charts with sup|X'| <= eps_1(n); (b') sum_p d_p >= (mu_n/16) sum_l |X_l|^2;
  (c'') locality at rate 1/(3n) in the path metric. C(n) = 6.1e4 n^9, delta_0(n) ~ n^{-32}.
- READ S1O:390-433 (TB, GR). |d_p - (1/8)|(D_1 X)_p|^2| <= C_5 |u_p|^3; Delta_1 = D_1^* D_1 + D_0 D_0^* >= mu_n
  = (2 sin(pi/2n))^2 >= 4/n^2; |Delta_1^{-1}(l,l')| <= (2/mu_n) exp(-a_n d_D), a_n >= 1/(7n).
- READ S1O:441-463 (Prop. U1). U(1): the fibre-constant parts of X_1, X_2 are massless on the base.
- READ S1O:503-511 (Prop. FLUX). Flux -1 around a hole of a good region forces a bad point in the hole.
- READ S1O:514-546 (W1, W2; ARGUED there). (S1-loc): |X|,|Y| <= K, |Cov| <= C(n,beta,K) exp(-(c/n) dist).
  (S1-T): the base transfer matrix has a gap >= c/n uniformly in M; equivalently |Cov(F,G)| <= 2 exp(-(c/n) d)
  for |F|,|G| <= 1 on the two sides of a pair of base planes at distance d.
- READ S1O:550-575 (Lemma PE, OPEN there). beta_PE(n), absolute c_PE, C(n,beta,K); for beta >= beta_PE(n), even M,
  gauge-invariant F over X, G over Y in [-1,1], |X|,|Y| <= K: |Cov(F,G)| <= C(n,beta,K) exp(-(c_PE/n) dist(X,Y)),
  and (S1-T) with the same rate. Needed (their list): (a) local conditional Peierls activity; (J) the Jacobian
  with the Faddeev-Popov ratio; (c) Gaussian decoupling across blocks, Z_2 labels of holes, convergence.

First remark of mine (ARGUED; to be settled in Step 2). (S1-T) as written, "|Cov(F,G)| <= 2 exp(-(c/n) d) for ALL
|F|,|G| <= 1 on two sides", is a statement about ALL functions, including non-gauge-invariant ones and including
functions of the base Z_2 flux through large loops. The Z_2 vortex gas has its own correlation length. A dilute gas
of vortices of density rho ~ e^{-c beta} gives a transfer-matrix gap of order one in the vortex sector only if
vortices are independent at distance; the gap for the Z_2-odd (centre-flip odd) sector is -log of the ratio of the
second to the first eigenvalue, which is governed by the string tension times the transverse size M: NOT uniform in M
in the flip-odd sector unless handled. This must be checked before any expansion is written.

### Step 1b. Reading of the check of row 842: D/library/gap-s1-check-astra.md (all 195 lines; CK below)

Check by Codex gpt-6-astra xhigh (row 856), a research check, not an audit.
- READ CK:15-45. RP, CB, Z, BAD (SU(2), n >= 2, even M >= 4), BAD-b, beta_BAD: HOLD.
  The "group-free" rider of BAD FAILS: Lemma Z needs a zero-action twist eater (twisted U(1) has none).
- READ CK:47-64. CH-D HOLDS AFTER CORRECTION: D finite and connected; in (c'') "every link l based at b_0 that
  belongs to both complexes". Constants unchanged. CH-T holds.
- READ CK:66-80. BAD-s and TB HOLD.
- READ CK:82-112. GR HOLDS AFTER CORRECTION (replacement proof by the product splitting; rate a_n = sqrt(mu_n/192)
  >= 1/(7n), prefactor 2/mu_n). Transverse covariance kernel bound:
  |Cov_G(l,l')| <= (4/beta) [2/mu_n + 64 e^{2a}/mu_n^2] exp(-a_n d_D(b(l), b(l'))).
- READ CK:114-118. FLUX HOLDS (R a filled rectangle).
- READ CK:120-138. U1 holds after a factor: the action Hessian at V is K_V/4, >= mu_n/4 on transverse fields.
- READ CK:140-166. W1 and W2 FAIL as arguments.
- READ CK:168-189. **The covariance form of (S1-T) is FALSE for this measure.** Counterexample (CK:174-187): the base
  Polyakov loop F_t = (1/2) tr prod_j U_4(x, t, j) on the slice b_3 = t. A centre flip of the direction-4 links gives
  mu(F_t) = 0. As beta -> infinity at fixed M, mu(F_0 F_d) -> 1 (concentration on the zero set, where the base Z_2 field
  is flat). So Cov(F_0, F_d) > 3/4 for large beta, against 2 exp(-(c/n) d). Also (CK:185): a torus expectation is a
  trace state, not a vacuum state; site-plane RP does not by itself give a positive one-step transfer operator.
  Also (CK:170): (S1-T) => (S1-loc) needs bounded diameters, not bounded cardinalities.

Consequence for this row (mine). The remark at the end of Step 1a is confirmed by CK's counterexample: Lemma PE as
printed (S1O:550-553) includes a false clause. The flux-odd sector (odd under a base centre flip) has a gap of order
(string tension) x M, tiny for M << exp(c beta). So Step 2 must first restate the target correctly:
the gap c/n can hold only (a) on the sector even under the base centre flips, or (b) for all sectors once the
transverse period M exceeds about n e^{c beta}... or (c) for local gauge-invariant observables (S1-loc), which are
flip-even automatically (S1O:160-163, Step 2 (iii) there).

### Step 1c. Reading of CH = D/library/gap-twist-chart.md (all 262 lines)

- READ CH:23-27. (X,Y) = -2 tr(XY) on su(2); e_c = i sigma_c/2; (1/2) tr exp(X) = cos(|X|/2); rho = geodesic distance
  of the 3-sphere of radius 2. Gamma_1 = i sigma_1, Gamma_2 = i sigma_2.
- READ CH:33-47. tau_l = Ad(V_l^{-1}) diagonal with signs; D_0 lambda (y,mu) = lambda(y+mu) - tau_l lambda(y);
  D_1 X; D_0^*; Delta_0 = D_0^* D_0. (1.1): U_p = z_p W E_p W^{-1}, d_p = 1 - cos(|Y_p|/2), Y_p = log E_p.
  (1.2): (V e^X)^{exp lambda} at l is V_l exp(tau_l lambda(y)) exp(X_l) exp(-lambda(y+mu)).
- READ CH:92-97 (Lemma L). |d omega|^2 + |d^* omega|^2 >= mu_n |omega|^2 on all cochains; Delta_0 >= mu_n.
- READ CH:103-111 (Lemma G). |g_c(y,y')| <= (2/mu_n) exp(-alpha_n |b - b'|_1); weighted sup norm of G_0 <= K_n = 25 n^6.
- READ CH:115-129 (G1-G4). G2: near-commuting with Gamma_1, Gamma_2 implies near the centre. G3: commutator near -1
  implies near (Gamma_1, Gamma_2) up to conjugation. G4: absolute constants C_3, C_4 (second derivatives of BCH).
- READ CH:131-150 (Lemma R), 152-166 (Lemma T: lambda = G_0 D_0^*(X^0 + N(lambda, X^0)) by contraction), 168-177 (Lemma Q).
- READ CH:181-193 (part (b)). READ CH:197-206 (constants): eps_1 = 1/(4200 C_3 n^7), eps_2 = min(eps_1, 1/(13 C_4 n)),
  C(n) = 6.1e4 n^9, delta_0 = (eps_2/C(n))^2, C_c(n) = 1.1e4 n^7 C(n).
- READ CH:258. Open there: derivative bounds for U -> X (the Jacobian).

Step 1 is complete. Statements I may use as inputs (all PROVED by others, checked once each, not audited):
RP, CB, Z, BAD, BAD-s (S1O, checked CK); CH-D with CK's corrections; TB; GR with CK's replacement proof; FLUX; U1.
