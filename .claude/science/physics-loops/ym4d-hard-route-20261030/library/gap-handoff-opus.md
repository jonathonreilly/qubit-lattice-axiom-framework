lead: anthropic/claude-opus-5-5 (max effort), FINISH row 846 (`gap-handoff-opus`), run 2026-11-13 on the lead's MacBook
clone: /Users/jonreilly/ym4d-lead/clone at f1c86d81909cfef4bc95cfa244a7086b1f1599fb ("docs(ym4d): add rows 843-846, four more Opus max lanes"); `git pull --ff-only`: "Already up to date"

# gap-handoff-opus: the hand-off (EXIT), and the openness of the block criterion and of the seed

**No mass gap is proved here.** Nothing in this file is checked by another model. It is research text and grants no status. One author, by hand, in one session. No repository file was edited.

**Marks.** PROVED = proved by hand in this file (one author; not an independent check). READ = read at the cited path and line. ARGUED = an argument short of proof, or a composition not written line by line. GUIDE = recalled physics, published numbers or arithmetic used in no proof. OPEN = no proof exists.

**Paths.** D = `.claude/science/physics-loops/ym4d-hard-route-20261030` in the clone. Short names, all in D/library: AS = `gap-assume-opus.md` (row 838); FL = `gap-finishline-opus.md` (row 837); BC = `gap-blockcrit-opus.md` (row 836); S23 = `gap-seed23-opus.md` (row 835); VL = `gap-vmf-lip.md` (row 785); PS = `gap-phys-seed.md` (row 720). FIN = D/FINISH.md; row 846 is at FIN L922.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the account (complete account and outline at their commit 31a47c543775). Every statement about the account is cited through FL (row 837), which read it in the primary text; I did not download it. Tadeusz Balaban: the block renormalization method that the account follows. Lane inputs, with their authors as the files state: Theorem V, Corollary V1, Lemma DC, Lemma INF, Theorem DOB (VL; Codex gpt-6-astra; checked by Claude Opus 5.5, row 790); Lemma Z' and Theorem ZD-c (PS; Claude Fable 5.2 and lane authors; checked by Claude Opus 5.5, row 727); Theorem SH (Claude Fable 5.2; checked row 707); Lemmas G, DC', MG, LF and Theorem F (S23; Claude Opus 5.5; not checked); Lemmas G, F, GF, Theorem R, Theorem ST, Corollary SEED, Proposition CEIL (BC; Claude Opus 5.5; not checked); Lemma FL and the (SEED-FP) chain (FL; Claude Opus 5.5; argued, not checked). The comparison method is Dobrushin's; the perturbation step of Lemma PV below is in the spirit of Holley and Stroock (recalled, not read).

**What was read.** FIN row 846 (L922). AS header and 3.3, 3.9 and the report (L1-20, L461-475, L517-548). FL in full (L1-266). BC in full (L1-342). S23 in full (L1-501). VL in full (L1-609). PS L260-280 (Lemma Z' and Corollary Z1') and the verdict line of `gap-phys-seed-check.md` (L48, L122: "Lemma Z'. HOLDS").

## 0. Checkpoint (updated in place)

- Final (01:05Z). All sections written: 1 brief answer; 2 the class of actions, its norm, the zones; 3 Lemma PV and Lemma INF-W; 4 Lemmas DC*, BOX, TRUNC, Identity PHI, Theorem O-SEED, Corollary SEED-HO, what is not open; 5 Theorem O-BC; 6 EXIT and Theorem HO; 7 the order-one steps; 8 marks and RESULT.
- Corrected during writing: the distance constants of Theorem O-SEED (representatives sit within R + 1/2 of the centre; constants e^(3m/2) and e^(5m/2)), and the worked size (n = 226).
- Not done: any order-one estimate; an independent check; a literature search. Scripts (arithmetic only): `scratchpad/lane846/scripts/radii.py`.

## 1. Answer in brief

1. **What lands, and where.** The landing zone is an open set O of effective actions on a coarse lattice: a plaquette coupling beta plus a gauge-invariant many-body interaction W with exponentially decaying Lipschitz seminorms, in global Gibbs form (no large-field labels, no small-field cut-offs). O is cut out by one explicit inequality per criterion (Section 2.3). At W = 0 the three inequalities reduce to the proved Wilson ranges: beta < 2/9 (chord Dobrushin, row 785), beta < 1/3 (tree gauge, row 835), beta < (sqrt 37 - 5)/3 (star blocks, row 836).
2. **What landing buys (Theorem HO, PROVED given READ inputs and the hypotheses of EXIT).** The landing zone needs no reflection positivity of the effective theory. The account's exact identity (integral of rho_k = bare Z, READ through FL 2.2) carries partition functions down the chain unchanged. Lemma Z' (checked, row 727) turns the defect Phi_rho(n) = rho^4 F(n^4) - F((rho n)^4) of two untwisted hypercubic tori into the bare thermal sum, using the bare transfer matrix. Inside O, Phi_rho(n) is bounded by (rho n)^4 e^(-m n/6) (e^(-m n/8) in the star form) times explicit constants (Theorem O-SEED). So landing at n_* steps past first passage gives the seed at the fixed physical size rho n L^(n_*), uniformly in the cutoff.
3. **Openness.** The single-link price beta/4 per shared plaquette (Corollary V1) degrades by the factor lambda(w) = e^(2w)(1 + 2w) under a many-body perturbation of size w, plus an additive cross term w (Lemma PV, PROVED). The chord Dobrushin seed, the tree-gauge seed and the star block criterion all stay valid with explicit margins (Theorems O-SEED, O-BC, PROVED; the tree-gauge variant ARGUED). Example radii at w (the Lipschitz norm per link): 0.14 at beta = 1/9 (chord), 0.058 at beta = 1/4 (tree gauge), 0.053 at beta = 1/4 and 0.026 at beta = 0.3 (stars). The star criterion holds exactly when 6(lambda - 1)x + w < (1 - alpha_*(beta))(1 - 6x)/2, x = beta/4.
4. **What is not open.** The seed as a spectral statement (a bound on a thermal sum) needs a transfer matrix for the perturbed measure. Multi-plaquette terms break reflection positivity in general. So the free-energy defect is the open quantity, and the spectral statement is recovered only through the bare (TM). This is why the hand-off must run through exact partition-function identities.
5. **How many steps at order one.** The account stops at first passage, at a weak coupling g <= gamma_H with no number (READ through FL 1.1). The band between the last weakly coupled scale one can control and the landing zone spans a fixed physical length ratio: about 10 (from a m = 1 to a m of about 10, GUIDE) up to about 600 (from beta_W = 4 down, GUIDE). With block factor L that is about ln(ratio)/ln L steps: one to six steps for L from 3 to 9; one step if L exceeds the ratio, but then that one step integrates an L^4 block at order-one coupling. Each step must keep seven properties (Section 7.2); the quantitative one, a non-perturbative bound on one block integral at order-one coupling, is OPEN and is the crux.

## 2. The class of actions, its norm, and the landing zones (definitions)

### 2.1 The class

Conventions as in BC 1 (READ BC L18-26): SU(2) = S^3 in R^4, chord metric, Haar probability sigma, x_p = Re U_p = (1/2) tr U_p, lane beta = Wilson beta_W, x = beta/4. On a periodic four-torus T (link set E_T, all periods at least 6) a datum (beta, W, E) defines the density

    rho_T(U) = exp( -E_T + beta sum_p eps_p x_p(U) - sum_X W_X(U) )   on SU(2)^(E_T), against Haar,          (2.1)

with centre signs eps_p (eps = 1 on the untwisted tori used for the seed). Here:

- X runs over finite nonempty link sets; W_X is a continuous function of the links of X, invariant under every gauge transformation; each W_X has midrange zero (sup + inf = 0). Constants are moved into E.
- delta_k(W_X) is the chord Lipschitz constant of W_X in the link k (BC L24). dbar(W_X) = max over k in X of delta_k(W_X).
- diam(X) is the l^infinity diameter of the set of link midpoints, circular on T. Two links of one plaquette are at distance at most 1 (VL L485-486).
- E_T = sum over X of E_X, a family of real constants indexed by link sets.
- **Torus consistency (TC).** A family of tori (here the hypercubic tori T_n, n in a set N_0) is consistent if every set X with diam(X) < n/3 on T_n lifts to Z^4 with the same diameter, and W_X, E_X are the same functions (after the lift) on every torus of the family, and translation covariant. Sets of diameter at least n/3 (this includes every wrapping set) may carry torus-dependent terms; only their norm is controlled. (n/3 is used because a translation of T_n that maps a set to itself forces diameter at least n/3: a cyclic subgroup of Z/nZ of order k >= 2 has a coset of circular diameter at least floor(k/2) n/k >= n/3. PROVED.)

### 2.2 The norm

For m >= 0 put

    w_m = ||W||_m = sup over links l of  sum_(X contains l) |X| e^(m diam X) dbar(W_X),
    e_m = sup over links l of  sum_(X contains l) e^(m diam X) |E_X|,
    lambda(w) = e^(2w) (1 + 2w).

w_0 <= w_m. Consequences used below (all PROVED, one line each):

- (N1) osc of W_X in one link l is at most 2 delta_l(W_X) (chord diameter 2). So for V_l(h; w) = -(sum of W_X over X containing l), as a function of U_l = h: osc_h V_l <= 2 w_0 and Lip_h V_l <= w_0.
- (N2) Cross coefficient c_lk(W) = sum over X containing l and k of delta_k(W_X). Row sums: sum over k != l of c_lk e^(m d(l,k)) <= sum over X containing l of e^(m diam X) sum over k in X of delta_k <= w_m. Column sums: sum over l != k of c_lk e^(m d(l,k)) <= sum over X containing k of |X| e^(m diam X) delta_k(W_X) <= w_m.
- (N3) Midrange zero gives ||W_X||_inf = osc(W_X)/2 <= sum over k in X of delta_k(W_X) <= |X| dbar(W_X). So the sum over X of diameter > R containing a given link of ||W_X||_inf is at most e^(-m R) w_m.
- (N4) Per site, with one representative X_0 per translation orbit: sum over orbits of sum over k in X_0 of delta_k(W_(X_0)) = |T|^(-1) sum over X of sum over k in X of delta_k(W_X) = |T|^(-1) sum over k of sum over X containing k of delta_k(W_X) <= 4 w_0 (four links per site).

**Balaban-type terms (ARGUED).** The account's localized terms obey abs(E^(j)(X; ., z)) <= E_0 e^(-kappa d_j(X)) on a polydisc about the identity (READ through FL L59, CA-I L58187-58290), and d_j(X) is at least the diameter in units of the scale. Cauchy estimates turn this into Lipschitz bounds, so the norm is finite for m < kappa, but only on the small-field domain. The norm above asks for Lipschitz bounds on all of SU(2)^X. So a density in the account's form (sums over large-field labels, small-field characteristic functions, READ through FL 1.2-1.3) is not in the class. Getting into the class is part of EXIT (Section 6).

### 2.3 The landing zones

Fix alpha in (0, 1) and m > 0. A datum (beta, W, E) on a consistent family of hypercubic tori is in

- **O_DOB(alpha, m)** if (9 beta/2) e^m lambda(w_0) + w_m <= alpha (no gauge fixing);
- **O_LF(alpha, m)** if 3 beta e^m lambda(w_0) + w_m <= alpha (the line-field tree gauge of S23 5.2-5.3; the periods are even);
- **O_ST(alpha, m)** if e^(2m) [ alpha_*(beta) + (1 + alpha_*(beta)) u/(1 - 6x - u) ] <= alpha, u = 6 (lambda(w_m) - 1) x + w_m, x = beta/4, alpha_*(beta) = (3 beta/2)(1 + beta/4)/(1 - beta - 3 beta^2/8) (BC L178), W invariant under the hyperoctahedral group as well as translations;

and in each case e_m < infinity. Each zone is defined by a non-strict inequality in finitely many continuous functions of (beta, w_0, w_m); the union over alpha < 1 and m > 0 of the zones is open in the topology of these quantities, and is star-shaped: if (beta, W) is in a zone, so is (s beta, s W) for 0 <= s <= 1, because the left sides increase in beta, w_0, w_m (PROVED: lambda, alpha_* and u/(1 - 6x - u) increase in their arguments where finite).

**At W = 0** (PROVED): lambda = 1, w = 0, and the conditions read 9 beta/2 < 1, 3 beta < 1, alpha_*(beta) < 1 as m -> 0, that is beta < 2/9, beta < 1/3, beta < (sqrt 37 - 5)/3 = 0.3609: the ranges of rows 785, 835, 836.

**Radii at m -> 0 (PROVED arithmetic, checked by `scratchpad/lane846/scripts/radii.py`, GUIDE).** The largest w = w_0 = w_m allowed:

| zone | beta | largest w |
|---|---|---|
| O_DOB | 1/9 | 0.143 |
| O_DOB | 0.2 | 0.021 |
| O_LF | 1/4 | 0.058 |
| O_LF | 0.3 | 0.021 |
| O_ST | 1/4 | 0.053 (threshold of u: 0.1411) |
| O_ST | 0.3 | 0.026 (threshold of u: 0.0753) |
| O_ST | 0.35 | 0.0042 (threshold of u: 0.0130) |

## 3. One-link openness

### 3.1 Lemma PV (perturbed von Mises-Fisher laws; PROVED from Corollary V1)

For F in R^4 and a bounded measurable V on S^3 put mu_(F,V)(dh) = exp(<F, h> + V(h)) sigma(dh) / normalization. Let V be chord-Lipschitz with constant ell and osc V <= theta, and let V' be bounded measurable. Then for every chord-1-Lipschitz psi on S^3 and every F' in R^4,

    | mu_(F,V)(psi) - mu_(F',V')(psi) |  <=  (1/4) e^theta (1 + 2 ell) |F - F'|  +  (1/2) osc(V' - V).          (PV)

At V = V' = 0 this is Corollary V1, d_Lip(mu_F, mu_F') <= |F - F'|/4 (READ VL L209-220; checked row 790).

*Proof.* Both sides are unchanged if a constant is added to psi, to V or to V'. So take psi with midrange 0 (then |psi| <= 1, since osc psi <= 2 on the chord diameter 2) and inf V = 0 (then 1 <= e^V <= e^theta and Lip(e^V) <= e^theta ell).
Leg 1, (F, V) to (F', V). Write mu_G for the plain vMF law. Then mu_(G,V)(psi) = A(G)/N(G) with A(G) = mu_G(psi e^V), N(G) = mu_G(e^V) >= 1. Write A/N - A'/N' = (A - A')/N + (A'/N') (N' - N)/N, with |A'/N'| = |mu_(F',V)(psi)| <= 1. By Corollary V1 applied to g/Lip(g): |A - A'| <= Lip(psi e^V) |F - F'|/4 and |N - N'| <= Lip(e^V) |F - F'|/4. The product rule gives Lip(psi e^V) <= e^theta + e^theta ell. So leg 1 is at most e^theta (1 + 2 ell) |F - F'|/4.
Leg 2, (F', V) to (F', V'). Put Delta = V' - V and mu_t = mu_(F', V + t Delta). The integrands are bounded on a compact space, so d/dt mu_t(psi) = Cov_t(psi, Delta). By Cauchy-Schwarz, |Cov_t(psi, Delta)| <= Var_t(psi)^(1/2) Var_t(Delta)^(1/2) <= 1 . osc(Delta)/2 (a function with values in an interval of length s has variance at most s^2/4). Integrate over t in [0, 1]. QED

**Remark (PROVED).** The factor e^theta (1 + 2 ell) is the whole cost of the many-body terms at the level of one link; it is 1 + O(theta + ell). Lemma F5 (stated and proved at AS L379; used in AS 3.3, READ AS L468) shows a loss of this kind is real: the sharp 1/4 belongs to the exact vMF law.

### 3.2 Lemma INF-W (the influence matrix of a perturbed action; PROVED from (PV), (N1), (N2) and VL L340-346)

Let mu_T be the probability with density (2.1) on a torus with all periods at least 6. Its conditional law at a link l, given the other links w, is mu_(F_l(w), V_l(.; w)), with F_l = beta times the sum over plaquettes p through l of eps_p times the unit staple of p at l (READ VL L340-346), and V_l(h; w) = -(sum over X containing l of W_X(h, w)). If w, w' differ only at the link k, then |F_l(w) - F_l(w')| <= beta n(l, k) |w_k - w'_k| (n(l, k) = number of plaquettes containing l and k; READ VL L340-346), and osc_h [V_l(h; w') - V_l(h; w)] <= 2 c_lk(W) |w_k - w'_k|, because sup_h |W_X(h, w') - W_X(h, w)| <= delta_k(W_X) |w_k - w'_k| for each X containing l and k (the other W_X do not change). The quantities theta = osc_h V_l <= 2 w_0 and ell = Lip_h V_l <= w_0 of (PV) are given by (N1). So by (PV), the chord influence numbers of Lemma DC (READ VL L222-232, (8)) can be taken as

    C_lk  =  (beta/4) n(l, k) lambda(w_0)  +  c_lk(W),                                                    (3.1)

and for every m >= 0, with the 18 plaquette partners of a link at distance at most 1 (READ VL L340-346),

    sum over k != l of C_lk e^(m d(l,k))  <=  (9 beta/2) e^m lambda(w_0) + w_m.                           (3.2)

The same bound holds for the gauge-fixed conditional laws of S23 Lemma MG (a) and of BC Lemma GF Step 3, because setting the fixed links to 1 does not increase any seminorm delta_k, and the conditional density of a free link is again of the form mu_(F, V) (PROVED: the densities are the restrictions of (2.1) to the gauge slice; S23 Lemma G and BC Lemma F use only gauge invariance of the density, READ S23 L150-162, BC L66-72, and (2.1) is gauge invariant). In the line-field gauge off the defect set D, a free link has exactly 12 free plaquette partners (READ S23 L326-331), so the Wilson part of the row sum is 3 beta e^m lambda(w_0).

## 4. Openness of the seed

The seed of rows 785, 835, 836 is proved in two parts: a comparison of local means between two tori (a Dobrushin-type statement about the measure), and the conversion of a free-energy defect into a thermal sum (a spectral statement, which uses the transfer matrix). This section shows that the first part, and with it the free-energy defect, is open under many-body perturbations, with explicit constants. Section 4.6 explains why the second part is not, and why the hand-off does not need it to be.

### 4.1 Lemma DC* (comparison with the condition off D, with kernel discrepancies and weights; PROVED)

Let Lambda be finite, Omega = (S^3)^Lambda, D a subset of Lambda, d a metric on Lambda, m >= 0. For i not in D let gamma_i be kernels with numbers C_ij as in (8) of VL (READ VL L222-232), and suppose

    sum over j of C_ij e^(m d(i,j)) <= alpha < 1   for every i not in D.

Let mu_1 have gamma_i as conditional law at every i not in D. Let mu_2 be any law on Omega, and b_i (i not in D) numbers with d_Lip(mu_2(U_i in . | U_(not i)), gamma_i(. | U_(not i))) <= b_i, mu_2-almost surely. Let f have finite seminorms and delta_j(f) = 0 on D, with support S of delta(f). Then, with Ctilde = C on (Lambda \ D)^2 and G = sum over n of Ctilde^n,

    |mu_1(f) - mu_2(f)| <= sum over i not in D of delta_i(f) [ 2 sum_(j in D) (G C_(.D))_ij + sum_(j not in D) G_ij b_j ].     (DC*)

If moreover b_j <= b e^(-m d(j, Y)) for a set Y, then |mu_1(f) - mu_2(f)| <= Delta(f) [ 2 alpha e^(-m d(S, D)) + b e^(-m d(S, Y)) ] / (1 - alpha).

*Proof.* Take P = (1/N') sum over i not in D of Gamma_i, built from the kernels gamma_i, N' = |Lambda \ D|. (i) READ S23 L183-197 (the proof of Lemma DC'): P^t f converges uniformly to a function h of the coordinates in D; mu_1(f) = mu_1(h); and |mu_1(h) - mu_2(h)| <= osc(h) <= 2 sum over j in D of delta_j(h) <= 2 sum over i not in D of delta_i(f) sum over j in D of (G C_(.D))_ij. (ii) New step. mu_2 need not be invariant under Gamma_i. Let Gammatilde_i be its conditional expectation at i. For bounded g with finite seminorms, mu_2(g) = mu_2(Gammatilde_i g), and |Gammatilde_i g - Gamma_i g| <= delta_i(g) b_i, since both average the same delta_i(g)-Lipschitz function of the i-th coordinate. So |mu_2(g) - mu_2(P g)| <= (1/N') sum over i not in D of delta_i(g) b_i. Put g = P^t f and sum over t. With delta'(P^t f) <= (R'^T)^t delta'(f) (READ S23 L186-188) and (1/N') sum over t of R'^t = (I - Ctilde)^(-1) (READ S23 L194), this gives |mu_2(f) - mu_2(h)| <= sum over i, j not in D of delta_i(f) G_ij b_j. (iii) Add (i) and (ii). (iv) Weights. Along any path i_0, ..., i_r whose rows lie off D, d(i_0, i_r) is at most the sum of the step lengths, so the sum over j of (Ctilde^n C_(.D))_ij e^(m d(i,j)) <= alpha^(n+1) and the sum over j of G_ij e^(m d(i,j)) <= 1/(1 - alpha). Hence the D-term is at most 2 alpha e^(-m d(i,D))/(1 - alpha). For the b-term use d(i, Y) <= d(i, j) + d(j, Y): it is at most b e^(-m d(i, Y))/(1 - alpha). Sum against delta_i(f). QED

### 4.2 Lemma BOX (the box cut between two hypercubic tori; PROVED)

Let rho >= 2 and n >= 6 be integers, and (beta, W, E) a datum that is consistent on {T_n, T_(rho n)} (2.1), with W of finite range R (W_X = 0 when diam X > R) and 1 <= R < n/3. Let Q = {0, ..., n-1}^4 in T_(rho n), E_Q the links (y, y + e_mu) of T_(rho n) with y in Q, and pi : E_Q -> E(T_n) the reduction modulo n (a bijection). Let mutilde be the image under pi of the E_Q-marginal of mu_(T_(rho n)). Let D_R be the set of links of T_n with some midpoint coordinate at circular distance at most R + 1 from n - 1/2. Then mutilde and mu_(T_n) have the same conditional law at every link l not in D_R, namely the kernel of (2.1) on T_n at l.

*Proof.* Let l not be in D_R, and let k lie in a plaquette through l or in a set X containing l with W_X != 0. Then d(k, l) <= R, so every midpoint coordinate of k is at circular distance more than 1 from n - 1/2. Such a coordinate lies in {1, 3/2, ..., n - 2}, and both endpoints of k then have coordinates in {1, ..., n - 2}. So these links, plaquettes and sets lift to objects of T_(rho n) made of links of E_Q, and pi maps them back. Their diameters are at most R < n/3, so by (TC) they carry the same functions on both tori. In T_(rho n) the conditional law of l given all other links is the kernel of (2.1), a function of these links only. By the tower property it is also the conditional law of l given the other links of E_Q, and its image under pi is the kernel of T_n at l. QED

This is Lemma M of `gap-mid-max.md` (READ through VL L468-474 and S23 L82-84) in all four directions at once, for many-body terms of range R. The same proof gives the block form: for a vertex block B(Q') of T_n whose links and events (Wilson events and W-events, BC 2.1) avoid D_R, mutilde and mu_(T_n) have the same block kernel.

### 4.3 Lemma TRUNC (cutting the tails; PROVED)

On a torus T let Z_T(beta, W) = integral of exp(beta sum_p eps_p x_p - sum_X W_X) against Haar, and let W^(<=R) keep the terms with diam X <= R. Then |log Z_T(beta, W) - log Z_T(beta, W^(<=R))| <= |E_T| e^(-m R) w_m.

*Proof.* The two exponents differ by the sum of W_X over diam X > R. Its sup is at most the sum over links k of the sum over X containing k with diam X > R of ||W_X||_inf, which is at most |E_T| e^(-mR) w_m by (N3). And |log of the integral of e^a - log of the integral of e^(a')| <= sup |a - a'|. QED

### 4.4 The defect identity and the vacuum cancellation (PROVED)

For a datum on {T_n, T_(rho n)} (untwisted), put F_T(s) = log of the integral of exp(s(beta sum_p x_p - sum_X W_X)) against Haar, 0 <= s <= 1, and let mu_(s,T) be the corresponding probability.

**Identity PHI.** If W has range R < n/3 and the datum is consistent, then

    rho^4 F_(T_n)(1) - F_(T_(rho n))(1) = (rho n)^4 integral_0^1 [ e_(rho n)(s) - e_n(s) ] ds,
    e_T(s) = sum over orbit types [X_0] of mu_(s,T)(h_(X_0)),   h = -beta x_p (six plaquette types per site) or h = W_(X_0).

*Proof.* F_T(0) = 0 (Haar is a probability). dF_T/ds = -(sum over all terms h of mu_(s,T)(h)). Every term has diameter at most R < n/3, so its orbit under the translations of T has exactly |T| elements (2.1), and mu_(s,T) is translation invariant; so dF_T/ds = -|T| e_T(s). The orbit types are the same on both tori by (TC). Integrate and use |T_n| = n^4, |T_(rho n)| = (rho n)^4. QED

This is D-shape (d) (READ VL L506-516) with the whole action in place of the plaquette sum, on hypercubic tori in place of the time doubling.

**Vacuum cancellation.** |rho^4 E_(T_n) - E_(T_(rho n))| <= 8 (rho n)^4 e^(-m n/3) e_m.
*Proof.* Sets of diameter below n/3 have orbits of size |T| and the same constants on both tori, so they contribute rho^4 n^4 c - (rho n)^4 c = 0, with c the (absolutely convergent) sum of E_(X_0) over these orbit types. The other sets contribute at most |E_T| e^(-mn/3) e_m on each torus. |E_(T_n)| = 4 n^4. QED

So every extensive constant cancels exactly in the defect, whatever its size. Only the non-extensive part (wrapping and large sets) enters, and it is exponentially small in the side. This is why the account's vacuum term, known only to C N_0 (READ through FL L74, (RF62)), is no obstacle in principle: what EXIT must deliver is its local, torus-consistent structure, not its value.

### 4.5 Theorem O-SEED (PROVED for the chord form; PROVED given unchecked author inputs for the two gauge forms)

Let rho >= 2 and n >= 8 be integers, and (beta, W, E) a consistent untwisted datum on {T_n, T_(rho n)} with beta >= 0. Write Phi^rho(n) = rho^4 log(integral of rho_(T_n)) - log(integral of rho_(T_(rho n))) for the densities (2.1).

(a) **Chord form.** If (beta, W) is in O_DOB(alpha, m) on both tori, then

    |Phi^rho(n)|  <=  (rho n)^4 [ (2 alpha e^(3m/2)/(1 - alpha)) (24 beta + 4 w_0) e^(-m n/6) + 8 w_m e^(-m n/6) + 8 e_m e^(-m n/3) ].     (4.1)

(b) **Tree-gauge form** (n, rho n even). If (beta, W) is in O_LF(alpha, m) on both tori, (4.1) holds as written. Inputs: S23 Lemma G and Lemma LF (author proofs, not checked).

(c) **Star form.** If (beta, W) is in O_ST(alpha, m) on both tori, then (4.1) holds with e^(-mn/6) replaced by e^(-m n/8) and 2 alpha e^(3m/2)/(1 - alpha) by 2 e^(5m/2)/(1 - alpha). Inputs: BC Lemmas F, GF and Theorem R (a), (d) (author proofs, not checked) and Theorem O-BC (Section 5).

*Proof of (a).* Put R = n/6, so 1 <= R < n/3. Step 1: Lemma TRUNC on both tori changes Phi^rho(n) by at most (rho^4 4 n^4 + 4 (rho n)^4) e^(-mR) w_m = 8 (rho n)^4 e^(-mn/6) w_m. The truncated datum is still consistent and still in O_DOB(alpha, m), because truncation does not increase w_0 or w_m. Step 2: the vacuum cancellation gives the term 8 (rho n)^4 e^(-mn/3) e_m. Step 3: for the truncated datum use Identity PHI. Fix s in [0, 1]. The datum (s beta, s W) is in O_DOB(alpha, m) (star shape, 2.3), so by (3.2) the kernels of mu_(s,T_n) satisfy the weighted condition of Lemma DC* at every link, with the circular l^infinity midpoint metric. Choose each orbit representative X_0 with one link midpoint within 1/2 of the point z* = (n/2 - 1/2)(1, 1, 1, 1), the antipode of the seam point; all its links are then within R + 1/2 of z*. Then mu_(s,T_(rho n))(h_(X_0)) = mutilde(h_(X_0)) (marginal, Lemma BOX), and Lemma DC* with mu_1 = mu_(s,T_n), mu_2 = mutilde, the set D_R of Lemma BOX in place of D and b = 0 gives |mutilde(h) - mu_(s,T_n)(h)| <= 2 alpha Delta(h) e^(-m d(S, D_R))/(1 - alpha). A link within R + 1/2 of z* has every coordinate at distance at least n/2 - R - 1/2 from the seam point, and a link of D_R has one coordinate within R + 1 of it; so d(S, D_R) >= n/2 - 2R - 3/2 = n/6 - 3/2. Sum over orbit types: Delta(beta x_p) <= 4 beta (VL L479-481) for six plaquette types, and (N4) for W, so the sum of Delta(h) is at most 24 beta + 4 w_0. So |e_(rho n)(s) - e_n(s)| <= 2 alpha e^(3m/2) (24 beta + 4 w_0) e^(-mn/6)/(1 - alpha), uniformly in s. Multiply by (rho n)^4. QED

*Proof of (b).* The same three steps. In Step 3 fix the line-field gauge of S23 5.3 on T_n (its seams in all four directions at the box seams x_mu: n - 1 -> 0) and on T_(rho n) (seams at x_mu: rho n - 1 -> 0). Gauge-invariant means are unchanged (S23 Lemma G, which uses only gauge invariance of the density). The period-2 pattern and n even make the two gauges agree on E_Q off D_R, and every plaquette that contains a seam link has all its links in D_R (their midpoints lie within 1 of n - 1/2). Off D_R every plaquette has exactly one fixed link (S23 Lemma LF (c)), so a free link has 12 free plaquette partners, and Section 3.2 gives the row sum 3 beta e^m lambda(w_0) + w_m <= alpha. Lemma BOX (with the gauge-fixed densities, which are restrictions of (2.1)) and Lemma DC* then run as in (a). Delta of a gauge-fixed term is at most Delta of the term. QED

*Proof of (c).* The same three steps with R = n/8. In Step 3 use Theorem R (d) of BC (READ BC L139-140, L152) for the star family on T_n, with mutilde as in Lemma BOX and A_D the stars whose links or events meet D_R. Stars outside A_D have the same block kernels under mutilde and mu_(s,T_n) (block form of Lemma BOX). The weighted form of the decay step (BC Theorem R (e), READ L142-154) is: if every weighted column sum (1/n) sum_j K_je e^(m d(j,e)) is at most alpha' < 1, then the bound of (d) is at most 2 Delta(f) e^(-m d(S, L_D))/(1 - alpha'), L_D the links of the stars of A_D. (PROVED: column sums of products are at most the products of the column sums, the weight is submultiplicative along paths by the triangle inequality, and each link lies in at most n blocks, as in BC L154.) Theorem O-BC (b) bounds these weighted column sums by the left side of O_ST, which is at most alpha. Distances: links of stars in A_D lie within 2R + 2 of the seam point in some coordinate, and S lies within R + 1/2 of z*, so d(S, L_D) >= n/2 - 3R - 5/2 = n/8 - 5/2. QED

**Corollary SEED-HO (the bare seed from a landed datum; PROVED given Lemma Z', checked row 727).** Suppose in addition that integral of rho_T = Z_bare(T^bare) exactly, where T^bare is the bare hypercubic torus with L^N times the sides (the exactness clause (E0) of EXIT, Section 6). Then with T_0 = L^N n,

    log(1 + S_bare(T_0; (rho T_0)^3))  <=  (2/rho) Phi^rho(n)                                                (4.2)

by Lemma Z' (READ PS L268-272: g(T_0; b^3) <= (2/rho) Phi_rho(T_0), b = rho T_0). Here S_bare is the full thermal sum of the bare transfer operator, all flux sectors included (READ VL L432-434). By (4.1) the right side is at most 2 rho^3 n^4 times the bracket, which tends to 0 as n grows. So for every target t > 0 there is an explicit n_1 with S_bare(T_0; (rho T_0)^3) <= t for n >= n_1, uniformly over all data with the same (alpha, m, beta, w_0, w_m, e_m). The size T_0 is n L^(n_*) in units of the first-passage lattice (Section 6).

Worked size (GUIDE arithmetic, not optimized): alpha = 1/2, m = 1, beta = 1/4, w_0 = w_m = 0.05, e_m = 1, rho = 25 (= L^2 for L = 5, so both tori are in the account's family), t = 3/10 (the line r >= 24 of Theorem SH, READ through FL L132): the condition 2 rho^3 n^4 [56.0 e^(-n/6) + 8 e^(-n/3)] <= log 1.3 holds from n = 226 coarse sites (checked by a one-line computation; GUIDE). The bracket constant is 2 e^(3/2) (24/4 + 0.2) + 0.4 = 56.0.

### 4.6 What is not open: the spectral seed

The conversion from a defect to a thermal sum, S(a; B) <= e^(Phi_B) - 1 (READ VL L517-520) and Lemma Z', uses Z(t, B) = Tr T^t for a positive transfer operator T, that is reflection positivity of the measure whose partition functions appear. Gauge-invariant many-body terms that couple the two sides of a reflection plane are not reflection positive in general (ARGUED; standard). So "the seed holds for every action near a Wilson action with beta < 1/3" is not a theorem: the seed of a perturbed action has no transfer-matrix meaning without RP. What is open is the comparison of local means and the defect Phi^rho(n). The hand-off needs nothing more: by the exact identity (READ through FL L123 and L138: the integral of rho_k equals the bare Z at every level, "an exact change of variables"), Phi^rho(n) of the effective densities is the bare defect, and the bare (TM) (row 667, checked row 671; READ through FL L139) converts it. The effective theory never needs a transfer matrix, which also removes the obstruction of row 23 (blocking maps not shown to keep RP; READ AS L463) from the landing step.

Two further consequences (PROVED from the above). (1) Lemma Z' uses only untwisted hypercubic tori, the account's own family (READ through FL L123), so this landing needs no twisted run of the account (the obstacle of FL 2.4 item 4). (2) The landing gives the full thermal sum, both halves of the seed at once.

## 5. Openness of the block criterion (BC) of row 836

### 5.1 What carries over unchanged (PROVED)

Let (beta, W) be as in (2.1), with W gauge invariant. For a vertex set Q, put Ev^W(Q) = the links off B(Q) that share a plaquette with B(Q) (BC L47) or lie in a set X with W_X != 0 that meets B(Q).

- **Lemma G for (beta, W).** (i) gamma_B(. | y) depends on y only through Ev^W(Q). (ii) It is invariant under G_Q = SU(2)^Q. (iv) Gamma_B maps Lip into Lip and Lip_inv into Lip_inv. *Proof.* As BC L58. For (ii): each W_X is gauge invariant, and a gauge transformation supported on Q moves only links of B(Q). (iii) of BC concerns plaquettes and is unchanged.
- **Lemma F** holds word for word (READ BC L66-72): its proof uses only the G_Q-invariance of the block law.
- **Lemma GF-W.** For admissible F and any exterior link j, the bound (GF) of BC L86 holds with

      C'_cd = lambda x n(c, d) + c_cd(W)   (c != d free),    b'_c = lambda x n(c, j) + c_cj(W),    K' = (I - C')^(-1) b',     (5.1)

  lambda = lambda(w_0), whenever the largest row sum of C' is below 1. *Proof.* BC Lemma GF Steps 1-6 (READ BC L93-100), with Step 3 replaced by Section 3.2: the conditional law of a free link given the other free links, in the gauge slice, is mu_(F_c, V_c) with V_c the restricted W-potential, and (PV) with (N1), (N2) bounds its moves. Step 4 (the refined Lemma DC, READ BC L97-98) needs only valid influence numbers and row sums below 1. Consequently (2.3) of BC (READ BC L90-91) holds with K'.

### 5.2 Theorem O-BC (PROVED)

**(a) One block, one event.** Let C, b be the Wilson quantities of BC (2.2) for an admissible F and an event j (b = 0 if j is a W-event only), K = (I - C)^(-1) b, and let C' <= C + Delta C, b' <= b + Delta b entrywise with Delta C, Delta b >= 0. Let c' be the largest column sum of C + Delta C and gamma the largest column sum of Delta C, and suppose c' < 1 and the row sums of C + Delta C are below 1. Then

    1^T K'  <=  1^T K + ( gamma 1^T K + 1^T Delta b ) / (1 - c').                                          (5.2)

*Proof.* The Neumann series is monotone in nonnegative entries, so K' <= (I - C - Delta C)^(-1)(b + Delta b). Write (I - C - Delta C)^(-1) - (I - C)^(-1) = (I - C - Delta C)^(-1) Delta C (I - C)^(-1) >= 0. So K' <= K + (I - C - Delta C)^(-1)(Delta C K + Delta b). For v >= 0, 1^T (C + Delta C)^r v <= c'^r 1^T v, so 1^T (I - C - Delta C)^(-1) v <= 1^T v/(1 - c'). Finally 1^T Delta C K <= gamma 1^T K. QED

**(b) Star blocks.** Let W be invariant under translations and the hyperoctahedral group, x = beta/4, lambda = lambda(w_0), and

    u = 6 (lambda - 1) x + w_0.

If u < 1 - 6x, the star family satisfies (BC-gen) for (beta, W) with w = 1, n = 2 and coefficient

    alpha^W(star; beta)  <=  alpha_*(beta) + (1 + alpha_*(beta)) u / (1 - 6x - u).                              (5.3)

So (BC) holds for (beta, W) whenever

    6 (lambda(w_0) - 1) x + w_0  <  (1 - alpha_*(beta)) (1 - 6x) / 2.                                        (5.4)

With weights e^(m d(j,e)) the weighted column sums (1/2) sum_j K'_je e^(m d(j,e)) are at most e^(2m) [alpha_* + (1 + alpha_*) u_m/(1 - 6x - u_m)], u_m = 6 (lambda(w_m) - 1) x + w_m: the left side of O_ST.

*Proof.* Events: the 48 Wilson events with F_j = {l_c} (READ BC L189), and the W-events with F_j empty (admissible; BC Remark GF' (2), READ L102). For both choices the Wilson matrix is x times the adjacency of Gamma_7 or of K_(2,2,2,2) (READ BC L191; the full star graph is 6-regular), so its row and column sums are at most 6x. By (5.1), Delta C = (lambda - 1) C + E with E_cd = c_cd(W), and Delta b = (lambda - 1) b + e with e_c = c_cj(W). By (N2) the row and column sums of E are at most w_0. So c' <= 6x + u < 1, the row sums of C' are below 1, and gamma <= u. Apply (5.2) to each event, sum over events and divide by |B| = 8. The Wilson terms give (1/8) sum_j 1^T K_j = alpha_*(beta) (READ BC L194) and (1/8) sum_j 1^T b_j = 48x/8 = 6x. The W-terms give (1/8) sum_j 1^T e_j <= (1/8) sum over c in B of sum over j off B of c_cj(W) <= w_0, by (N2). So alpha^W <= alpha_* + (u alpha_* + 6(lambda - 1)x + w_0)/(1 - 6x - u), which is (5.3). Lemma SYM (READ BC L120-122) holds for (beta, W) by the same proof, since W is invariant under the isometries of Z^4. (5.4) is (5.3) < 1 rearranged: (1 + alpha_*) u < (1 - alpha_*)(1 - 6x - u) is 2u < (1 - alpha_*)(1 - 6x). Weights: each term of K'_j is a walk that enters the star once from j (a Wilson step of length at most 1, or a W-step through a set X, of length at most diam X) and then moves inside the star, whose link midpoints are within distance 1 of each other. So d(j, e) <= 2 for Wilson entries and d(j, e) <= diam X + 1 for W-entries; the weights multiply the Wilson part by at most e^(2m) and turn w_0 into at most e^m w_m in the entry terms. Replacing w_0 by w_m everywhere only enlarges the bound. QED

**(c) General shapes (same proof).** For any vertex-block family with a symmetric fixing rule, Wilson coefficient alpha = alpha(Q_0; beta) (BC (2.4)), r = the largest row or column sum of the Wilson matrices C^(F_j), and bbar = |B|^(-1) sum_j 1^T b_j:

    alpha^W  <=  alpha + [ ((lambda - 1) r + w_0) alpha + (lambda - 1) bbar + w_0 ] / (1 - lambda r - w_0).      (5.5)

So every block criterion verified with a margin at W = 0 survives every many-body perturbation with w_0 below an explicit radius, and the radius tends to 0 only as the Wilson margin 1 - alpha does.

### 5.3 What the perturbed criterion gives

Theorem R (a), (b), (d), (e) (READ BC L130-154; author proofs, not checked) use only (BC-gen) and Lemma GF. So under (5.4) the perturbed measure has, uniformly in the torus and in the centre signs: contraction of the block heat bath; the block gap sum_a mu(Var_(B_a) f) >= 2(1 - alpha^W) Var f; comparison; and exponential decay of correlations (PROVED given those inputs). The Langevin gap (c) needs a block Poincare constant: Lemma D1 (READ BC L33) gives 3 for each vMF law, and a bounded perturbation with osc at most 2 w_0 lowers it at most by e^(-2 w_0) (Holley-Stroock; recalled, not read), so c_* >= 3 e^(-2 w_0)(1 - 6 lambda x - w_0) (ARGUED). The gap is not on the path; the decay is: it is the decay statement the account does not make (READ through FL L81: "no decay in d is asserted").

**Where openness stops (PROVED from BC Proposition CEIL, READ BC L266-268).** Perturbation never raises the method's ceiling. The bounds (5.1) are entrywise at least the Wilson ones, so the spectral radius of C' is at least (2 + sqrt 10) x for every vertex block and admissible fixing. For beta >= 0.775 no perturbed vertex block criterion of this form can hold, whatever W.

## 6. The hand-off (EXIT), stated precisely

### 6.1 Where the account leaves the measure (READ through FL)

At first passage the account gives, on each of its tori T_l (four equal sides l = 2 L^p >= l_*(g), untwisted; READ through FL L80, L123), the density rho_K of the unit-lattice block field V_K, with integral of rho_K = Z_bare exactly (READ through FL L123, L138). Its form (READ through FL L54-67): a sum over large-field labels of characteristic functions times exp(-A(x_K(.), U_K(V)) + E_K + R_K + B_K - Ecal), with x_K in (g^(-2), g^(-2) + B_sharp], g <= gamma_H small and not explicit (FL L45-50), ||E|| <= E_0, ||R|| <= g^(kappa_0), boundary terms decaying like e^(-kappa d), large-field mass e^(-(2 - c') p_0(g)); the non-wrapping localized terms are torus independent (FL L59). No step past first passage; every step needs g_k <= gamma (FL L50).

This density is not in any landing zone of 2.3, for three separate reasons (PROVED from the definitions and the READ form): (R1) its plaquette coupling x_K >= gamma_H^(-2) is far above 1/3; (R2) it is not a global Gibbs density (2.1): it carries large-field labels and small-field characteristic functions, so its one-link conditional laws are not of the form mu_(F,V) with bounded V; (R3) its local terms are bounded only on a polydisc about the identity, not in the global Lipschitz norm of 2.2. The hand-off must remove all three.

### 6.2 Definition EXIT(n_*, rho, zeta)

Parameters: an integer n_* >= 0 (steps past first passage); rho = L^r with r >= 1 (the ratio of the two tori; rho >= 25 is convenient, Theorem SH line r >= 24); zeta = (tau, alpha, m, betabar, wbar, ebar) with tau in {DOB, LF, ST}, alpha < 1, m > 0.

EXIT(n_*, rho, zeta) asserts: there are K_0 and a physical size l_1 = 2 L^(p_1) such that, for every first-passage datum (K, beta_bare) at g with K >= K_0, and for every torus T_l of the account's family with l >= l_1:

- **(E0) Exactness.** There are densities rho_(K+1), ..., rho_(K+n_*) of block fields on the lattices of spacing L, ..., L^(n_*) (first-passage units) of T_l, with integral of rho_(K+j) = Z_bare(T_l) exactly. This holds automatically if each rho_(K+j) is the image of rho_(K+j-1) under a probability kernel (positivity and normalisation of the block-spin map).
- **(E1) Form.** rho_(K+n_*) is a global Gibbs density (2.1) on the coarse torus of side n = l/L^(n_*), untwisted, with a datum (beta, W, E): gauge invariant, translation covariant (hyperoctahedrally invariant if tau = ST), no characteristic functions, no labels.
- **(E2) Consistency.** The data on T_l and T_(rho l) satisfy (TC) of 2.1.
- **(E3) Zone.** On both tori (beta, W) is in O_tau(alpha, m), with beta <= betabar, w_m <= wbar, e_m <= ebar.
- **(E4) Uniformity.** K_0, l_1, n_* and zeta do not depend on the datum (K, beta_bare), for K >= K_0.

The coarse sides n = 2 L^(p - n_*) and rho n are even (L is odd), as the line-field form needs.

### 6.3 Theorem HO (EXIT gives the seed at a fixed physical size; PROVED given EXIT and the cited inputs)

Assume EXIT(n_*, rho, zeta). Let t(rho) be the threshold of Theorem SH at the shape r = rho (READ through FL L101: 1/1650 at r = 2, 1/25 at r = 4, 3/10 at r >= 24), and let n_1 be the least coarse side of the family with n_1 >= max(8, l_1/L^(n_*)) and

    2 rho^3 n_1^4 [ A_tau (24 betabar + 4 wbar) e^(-m n_1/k_tau) + 8 wbar e^(-m n_1/k_tau) + 8 ebar e^(-m n_1/3) ]  <=  log(1 + t(rho)),

with A_tau = 2 alpha e^(3m/2)/(1 - alpha), k_tau = 6 for tau in {DOB, LF} and A_ST = 2 e^(5m/2)/(1 - alpha), k_ST = 8. The left side tends to 0, so n_1 exists. Then for every first-passage datum with K >= K_0,

    S_bare(T_0; (rho T_0)^3) <= t(rho),    T_0 = L^(K + n_*) n_1 bare sites  =  n_1 L^(n_*) first-passage units.     (HO)

*Proof.* (E0)-(E3) are the hypotheses of Corollary SEED-HO with N = K + n_*, at the coarse side n_1, and (4.1) in the form of Theorem O-SEED for the zone tau bounds the defect by the bracket, uniformly by (E4) and monotonicity in beta, w_m, e_m. (4.2) gives log(1 + S_bare) <= log(1 + t(rho)). QED

**From (HO) to the gap (ARGUED; compositions of checked statements written in FL).** (HO) at one physical size n_1 L^(n_*), with one margin, for all large cutoffs, is the hypothesis of Lemma FL (FL L128-134, ARGUED there, not checked) with s_0 = t(rho) < 3/10 when rho >= 25. Lemma FL gives (SEED-FP), and FL 2.5 (a)-(f) (ARGUED there; its steps (a), (b) PROVED and checked) give (GAP) at a rate in physical units that does not depend on the cutoff.

### 6.4 What EXIT does not need, and what it adds (ARGUED)

- No reflection positivity of any block law (4.6), so the obstacle of row 23 does not touch the landing. No twisted run of the account (4.6). No evaluation of the last integral: the account knows it only to e^(O(l^4)) (READ through FL L76), and Theorem O-SEED never uses that bound; it computes the defect by interpolation inside the zone, where extensive constants cancel exactly (4.4).
- FL 2.3 item 3 asked for "a quantitative comparison of the actual effective weight with that Wilson weight". (E3) is exactly such a comparison, in the norm that makes it work: a per-link Lipschitz norm of the many-body terms, not a bound on the total density. In that norm a comparison of size w is harmless (Theorem O-SEED); a bound e^(O(l^4)) on the density ratio would not be.
- Consistency with the instability that FL L140 READ cites (Proposition V of `gap-crux-fp.md`: weights with the Wilson quadratic form at large quadratic coupling lose the seed at every size): those weights are at large coupling, outside every O_tau. Openness holds only inside the strong-coupling zones; that is why EXIT must reach them.
- Comparison with AS 3.3 (READ AS L468): the Holley-Stroock heuristic there ("thresholds move continuously, for example beta < (2/9) e^(-2 eps) - O(eps)") is now a theorem with constants, in the form (9 beta/2) lambda(w_0) e^m + w_m <= alpha, and the same holds for the line-field gauge (1/3) and the star blocks ((sqrt 37 - 5)/3), not only for the chord Dobrushin range. The surface-class results (rows 811-830) are not covered here; AS 3.3 argues they do not survive multi-plaquette terms as stated.

## 7. The steps at order-one coupling: how many, and what each must control

### 7.1 Three groups of steps (the split ARGUED; the counts GUIDE)

The steps K -> K + n_* fall into three groups.

- **(G1) Weakly coupled steps past the account's ceiling.** From x = gamma_H^(-2) down to the top x_top of the order-one band. Balaban's method is built for these, but the account takes none: every step needs g_k <= gamma, and gamma has no value (READ through FL L48-50). They need the account's constants made explicit down to x_top. At one loop each step lowers x by (11/(3 pi^2)) ln L = 0.3715 ln L (READ through FL L47), so (G1) has about (gamma_H^(-2) - x_top)/(0.3715 ln L) steps (GUIDE). With no value of gamma_H this has no number (as FL L183 says of the distance to the window).
- **(G2) Order-one steps.** From x_top to the landing zone. No expansion in a small parameter applies.
- **(G3) The landing step**, the last step of (G2): it must also deliver (E1), the global Gibbs form.

**The length ratio across (G2) (GUIDE).** At the landing the effective action is close to a Wilson action with beta at most about 1/3, whose leading strong-coupling mass is 4 log(4/beta), about 9.9 per lattice unit (recalled leading form, used in FL L196). So landing happens about where the coarse spacing is ten correlation lengths. The Wilson lattice has a m = 1 near beta_W = 2.38 (READ through FL L179, a GUIDE number from row 706). With two-loop scaling (recalled; asymptotic scaling is not exact there, FL L181):

| top of the band | a m at the top | length ratio to landing | steps for L = 3, 5, 7, 9, 25 |
|---|---|---|---|
| beta_W = 4 (g_std^2 = 1) | 0.016 | about 630 | 5.9, 4.0, 3.3, 2.9, 2.0 |
| beta_W = 3 | 0.21 | about 48 | 3.5, 2.4, 2.0, 1.8, 1.2 |
| a m = 1 (beta_W = 2.38) | 1 | about 10 | 2.1, 1.4, 1.2, 1.05, below 1 |

(Script `scratchpad/lane846/scripts/radii.py`, arithmetic only.) AS 3.3 (READ AS L472) estimated eight doublings from 2.3 to 2/9 at one loop; one loop overstates the ratio at strong coupling, where the coupling flows faster.

**Reading (ARGUED).** The number of steps is not intrinsic. The intrinsic quantity is the length ratio across the band: a fixed physical number, between about 10 and about 600 by these GUIDE estimates. The account takes L large after the exponents (READ through FL L48: "Then L is taken large"); with L above the ratio, (G2) is one step, but that one step integrates a block of L^4 sites at order-one coupling, so nothing is gained. For L between 3 and 9 the band is one to six steps. In every case at least one step past first passage is needed: the first-passage density is in no landing zone (6.1, (R1)-(R3); PROVED from the definitions for the density as written; whether a resummation of it lies in a zone is OPEN; (R1) alone excludes it once x_K >= 0.361, the largest Wilson range of the three zones, and Proposition CEIL excludes every vertex-block zone of this kind once x_K >= 0.775).

### 7.2 What each step must control (ARGUED: each item is a hypothesis of Theorem HO carried back one step)

For j = K + 1, ..., K + n_*:

- **(P1) Exactness.** The block-spin map is a probability kernel, so the total mass is the bare Z exactly ((E0)). Approximate maps with errors e^(o(1) |T|) would ruin the defect, which must be below about 0.13 rho in absolute terms (FL L126).
- **(P2) Symmetry.** Gauge covariance under the coarse gauge group (so the output is gauge invariant), translations by the block size, and the hyperoctahedral group. Reflection positivity is not needed (4.6).
- **(P3) Locality with a rate.** The output's terms decay in diameter at a rate m_(j+1) > 0 in the new units, with m_(j+1) bounded below uniformly. The decay is what makes the defect exponentially small in the side (4.1).
- **(P4) Torus and cutoff consistency.** The terms on non-wrapping sets are the same functions on every torus of the family and at every cutoff K >= K_0, as the account proves at first passage for its non-wrapping localized terms (READ through FL L59, CA-I 4.38); wrapping terms are controlled in the same norm ((E2)).
- **(P5) Vacuum structure.** The constant is a consistent local family with e_m finite, not only a number: its extensive part then cancels exactly (4.4). The account's (RF62) gives only a value up to C N_0 (READ through FL L74).
- **(P6) Large-field resummation.** By the last step, no large-field labels and no small-field characteristic functions, and global Lipschitz bounds in place of polydisc bounds ((R2), (R3)).
- **(P7) Quantitative transport.** Explicit maps (beta_j, w_j, m_j, e_j) -> (beta_(j+1), w_(j+1), m_(j+1), e_(j+1)), uniform in the cutoff, whose composition from the top of the band lands in O_tau(alpha, m). The landing step must output, for example, w_m below about 0.05 at beta = 1/4 (2.3, the radii table): a five per cent statement, per link and in a Lipschitz norm, about the effective action after an order-one block integral.

(P1), (P2) are properties of the choice of kernel. (P3)-(P6) are structural and are what Balaban's method proves at weak coupling. (P7) in the band is the crux: there beta_j is of order one and the many-body terms generated by an order-one block integral are of order one in every norm, so no convergent expansion in a small parameter is available. It needs a non-perturbative bound on one block integral at order-one coupling, written by hand (the lane does not use computer-assisted proofs). **OPEN.**

### 7.3 What this prices (ARGUED, with GUIDE numbers)

- **Strong-coupling ranges are worth little for EXIT; zone radii are worth more.** Raising the proved Wilson range from 1/3 to 0.36 moves the landing scale by the mass ratio 4 log(4/(1/3))/(4 log(4/0.36)), about 1.03 in length (GUIDE). Even the method ceiling 0.775 of Proposition CEIL would move it by a factor of about 1.5 (masses 9.9 against 6.6, GUIDE). Neither saves a step for L >= 3. By contrast, the radius of the zone in the many-body norm sets how accurate the landing step must be ((P7)). A row that enlarges the radius at fixed beta (for example a sharper version of Lemma PV, or a block criterion with field-dependent responses) eases the crux directly.
- **The landing statements must be class statements.** AS 3.3 (READ AS L474) asked that each R1 theorem be stated for an influence-defined class. Sections 4-5 do this for rows 785, 835, 836: each is now a statement for the class O_tau, with the constants above.
- **The order of the obligations.** (G1) needs explicit constants in Balaban's method (a port and constants task, not a new idea). (G2) needs a new idea. (G3) needs (P6), which at order-one coupling is plausible but unproved: when the small-field radius eps_k eta_k^2, with eps_k = g_k p_0(g_k) (READ through FL L67), exceeds the chord diameter 2, the plaquette small-field conditions are empty (PROVED: |1 - U_p| <= 2), but the analyticity and the large-field bounds of the account are stated only for small g.

## 8. Marks, scope, RESULT

### 8.1 The statements of this file

| Statement | Mark | Where |
|---|---|---|
| The class (2.1), the norm, (TC); the zones O_DOB, O_LF, O_ST are star-shaped, given by continuous inequalities, and reduce at W = 0 to beta < 2/9, 1/3, (sqrt 37 - 5)/3 | PROVED (definitions and monotonicity) | 2 |
| Radii of the zones (0.143 at 1/9; 0.058 at 1/4 tree gauge; 0.053 at 1/4 and 0.026 at 0.3 stars) | PROVED arithmetic; script check GUIDE | 2.3 |
| Lemma PV: perturbed vMF transport, (1/4) e^theta (1 + 2 ell) abs(F - F') + (1/2) osc(V' - V) | PROVED from Corollary V1 (READ VL L209-220, checked row 790) | 3.1 |
| Lemma INF-W: influence numbers (3.1) and weighted row sums (3.2), also in the gauge slices | PROVED | 3.2 |
| Lemma DC*: comparison with the condition off D, kernel discrepancies and exponential weights | PROVED (extends S23 Lemma DC', an author proof not yet checked) | 4.1 |
| Lemma BOX (four-direction box cut between T_n and T_(rho n), finite range) and its block form | PROVED | 4.2 |
| Lemma TRUNC; Identity PHI; vacuum cancellation (extensive constants cancel exactly) | PROVED | 4.3, 4.4 |
| Theorem O-SEED (a), chord form, bound (4.1) | PROVED | 4.5 |
| Theorem O-SEED (b), line-field tree gauge | PROVED given S23 Lemmas G and LF (author proofs, not checked) | 4.5 |
| Theorem O-SEED (c), star blocks | PROVED given BC Lemmas F, GF and Theorem R (author proofs, not checked) | 4.5 |
| Corollary SEED-HO: a landed datum with exact total masses gives the bare thermal sum through Lemma Z' | PROVED given Lemma Z' (READ PS L268-272, checked row 727) | 4.5 |
| The spectral seed is not open; the defect is; the hand-off needs only the defect | ARGUED (that general many-body terms break RP is standard, not proved here) | 4.6 |
| Lemmas G, F, GF-W for (beta, W) | PROVED (the BC proofs carried over) | 5.1 |
| Theorem O-BC (a) one-block bound (5.2); (b) stars, (5.3), (5.4) and the weighted form; (c) general shapes (5.5) | PROVED | 5.2 |
| Perturbed contraction, block gap, comparison, decay | PROVED given BC Theorem R (not checked) | 5.3 |
| Perturbed Langevin constant 3 e^(-2 w_0)(1 - 6 lambda x - w_0) | ARGUED (Holley-Stroock recalled, not read) | 5.3 |
| Perturbation does not raise the ceiling 0.775 of vertex-block methods | PROVED from BC Proposition CEIL | 5.3 |
| The first-passage density, as the account writes it, is in no zone ((R1)-(R3)) | PROVED from the definitions and the READ form | 6.1 |
| Definition EXIT(n_*, rho, zeta), clauses (E0)-(E4) | definition | 6.2 |
| Theorem HO: EXIT gives S_bare(T_0; (rho T_0)^3) <= t(rho) at T_0 = n_1 L^(n_*) first-passage units, for all K >= K_0 | PROVED given EXIT and the inputs above | 6.3 |
| (HO) gives (SEED-FP) and (GAP) | ARGUED (Lemma FL and FL 2.5, argued in FL, not checked) | 6.3 |
| The split (G1), (G2), (G3) and the obligations (P1)-(P7) | ARGUED | 7 |
| Landing near ten correlation lengths per coarse spacing; band length ratio 10 to 600; one to six steps for L from 3 to 9 | GUIDE | 7.1 |
| EXIT itself: explicit constants for (G1); the order-one block bound (P7) for (G2); the resummation (P6) | OPEN | 7 |

### 8.2 What this file did not cover

1. No proof of the account was read. Every statement about it is cited through FL, which read the primary text; I did not download it.
2. The surface-class results (rows 811-830) are not treated (AS 3.3 argues they do not survive multi-plaquette terms as stated).
3. The time-doubling form of the seed (tori (a, (2a)^3) and (2a, (2a)^3)) is not used in the hand-off: those tori have unequal sides and are not in the account's family. The hand-off uses Lemma Z' on hypercubic tori instead.
4. A polymer-activity form of (E1), turned into (2.1) by a cluster expansion, is a natural weakening; it is not written (the Kotecky-Preiss criterion is recalled only).
5. Nothing here is checked by another model. The steps that most need a check: Lemma PV leg 1 (the Lipschitz constant of psi e^V and the normalisation inf V = 0); Lemma DC* step (ii) (the orientation of G against b); Lemma BOX (the coordinate window {1, ..., n - 2}); the distance counts in Theorem O-SEED (a) and (c); the event and column sums in Theorem O-BC (b).
6. Literature: no search was run. The openness of Dobrushin's uniqueness condition under small changes of the specification is classical (recalled: Dobrushin; the books of Georgii and Simon). What may be new here is only the explicit constants in the chord vMF setting, the gauge-fixed and block versions, and the hand-off structure (defect computed on the effective densities, converted by the bare transfer matrix). The owner's rule asks for a reading row before any outward use.

### 8.3 Items the lead may queue (suggestions only)

1. A cross-provider check of Sections 3-5 (Lemma PV, Lemma DC*, Lemma BOX, Theorem O-SEED (a), Theorem O-BC (b)): short and self-contained.
2. A reading row: perturbative stability of Dobrushin and Dobrushin-Shlosman conditions, and strong-coupling block-spin maps for lattice gauge theories (is a landing zone of this form already in the literature?).
3. For (G1): a constants item on the account, asking what explicit ceiling gamma its steps admit, since every weak-coupling step past first passage needs it.
4. For (G2), the crux: a statement of (P7) for one block integral at beta_W in [2.3, 4], with the zone radii of 2.3 as the target accuracy at the last step.

RESULT: no mass gap is proved and nothing at order-one coupling is proved; EXIT is stated precisely: n_* block-spin steps past the account's first passage, each an exact gauge-covariant probability kernel, must turn the account's last-scale density (Balaban form, x_K > g^-2, large-field labels and small-field cut-offs; READ through row 837) into a global Gibbs density beta sum x_p - sum W_X - E on the coarse tori of the account's family, torus- and cutoff-consistent, inside an explicit open zone O (chord Dobrushin (9beta/2)e^m lambda(w_0) + w_m <= alpha, line-field gauge 3beta e^m lambda(w_0) + w_m <= alpha, or stars alpha_*(beta) + (1+alpha_*)u/(1-6x-u) < 1 with lambda(w) = e^(2w)(1+2w), u = 6(lambda-1)x + w); PROVED: these zones are open with explicit radii (0.143 at beta 1/9, 0.058 at 1/4 in the tree gauge, 0.053 at 1/4 and 0.026 at 0.3 for stars) by a perturbed von Mises-Fisher transport bound (Lemma PV) and perturbed influence matrices, the star block criterion of row 836 survives exactly when 6(lambda-1)x + w_0 < (1 - alpha_*(beta))(1-6x)/2 (Theorem O-BC), and inside each zone the defect rho^4 F(T_n) - F(T_(rho n)) is at most (rho n)^4 e^(-mn/6) (e^(-mn/8) for stars) times explicit constants, with all extensive vacuum constants cancelling exactly (Theorem O-SEED), so landing gives the bare seed S(T_0; (rho T_0)^3) <= t(rho) at the fixed physical size n_1 L^(n_*) uniformly in the cutoff through Lemma Z' and the bare transfer matrix, with no reflection positivity of the effective theory and no twisted tori (Theorem HO; the passage to (GAP) ARGUED via row 837's Lemma FL); not open: the spectral seed of a perturbed action (needs RP); the order-one band spans a fixed physical length ratio of about 10 to 600 (GUIDE), one to six steps for L from 3 to 9, and each step must keep exactness, symmetry, locality with a rate, torus and cutoff consistency, a local vacuum, large-field resummation and an explicit transport of (beta, w, m, e), the last being a non-perturbative order-one block bound that is OPEN and is the crux.
