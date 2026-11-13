# FINISH row 861, gap-exit-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Author: Claude Fable 5.2 (max effort). Date: 2026-11-12.
Clone: /Users/jonreilly/ym4d-lead/clone at commit 2b6acd1732dde4e18293f0fe0e2814edbca36da3 (read-only).
Sussman-Alpoge sources: /Users/jonreilly/ym4d-lead/sa at commit 31a47c543775 (as given by the brief; not re-verified yet).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Labels: PROVED (mine, in this file), READ (path and line), ARGUED, GUIDE, OPEN.

## Target

The hand-off (EXIT) of D/library/gap-handoff-opus.md (row 846). Exact gauge-covariant
block-spin steps past the Sussman-Alpoge first passage must turn the last-scale density
into a global Gibbs density inside an explicit open zone O where the strong-coupling
criteria hold. The open crux is the non-perturbative block bound at the order-one band:
the last step must reach a per-link Lipschitz norm of about 0.05 at beta = 1/4.
This file attacks the order-one block bound itself.

## Plan (one step per response; each step is appended before the next starts)

1. Read row 846 (gap-handoff-opus.md): the exact (EXIT) statement, the zones O, the numbers.
   Read row 848's check (gap-e17phys-check-astra.md). Record what is fixed.
2. Read (SEED-FP) in gap-finishline-opus.md lines 110-160 and the fact tests
   (rows 786, 838, 839, 843, 845). Record the constraints as a checklist.
3. Survey the candidate block maps from first principles (decimation, heat-kernel smearing,
   Balaban averaging, Migdal-Kadanoff bond moving with exact controls, multigrid).
   For each: what is exact, what is controlled, where U(1), Q_8 and 2T sit.
4. Choose the best route. State the monotone or controlled quantity. State the crux lemma exactly.
5. Attempt the crux lemma as a real proof. Stage A.
6. Attempt, stage B (continue or second line of attack). Record exactly where it stops.
7. Map each step to the statements of the Sussman-Alpoge account it needs, with line ranges.
8. Fact tests on the final argument (U(1), Q_8, 2T, worst-case caps). Summary. RESULT line.

## Step 1a. What row 846 fixes (READ D/library/gap-handoff-opus.md L1-379, in full)

Short name HO = D/library/gap-handoff-opus.md.

- (HO L49-58) The class. A datum (beta, W, E) on a periodic four-torus gives the density
  rho_T(U) = exp(-E_T + beta sum_p eps_p x_p(U) - sum_X W_X(U)) against Haar, x_p = (1/2) tr U_p.
  Each W_X is continuous, gauge invariant, midrange zero.
- (HO L60-65) The norm. w_m = sup_l sum_(X contains l) |X| e^(m diam X) dbar(W_X), with dbar the largest
  one-link chord Lipschitz constant. lambda(w) = e^(2w)(1 + 2w).
- (HO L76-80) Zones. O_DOB: (9 beta/2) e^m lambda(w_0) + w_m <= alpha. O_LF: 3 beta e^m lambda(w_0) + w_m <= alpha.
  O_ST: e^(2m)[alpha_*(beta) + (1 + alpha_*) u/(1 - 6x - u)] <= alpha, u = 6(lambda(w_m) - 1)x + w_m, x = beta/4.
- (HO L86-94) Radii at m -> 0: w <= 0.058 at beta = 1/4 (tree gauge); 0.053 at beta = 1/4 (stars).
- (HO L256-266) EXIT(n_*, rho, zeta): (E0) exact masses, automatic for probability kernels; (E1) global Gibbs
  form (2.1), no labels, no characteristic functions; (E2) torus consistency (TC); (E3) zone; (E4) uniformity in the cutoff.
- (HO L270-278) Theorem HO: EXIT gives S_bare(T_0; (rho T_0)^3) <= t(rho) at a fixed physical size, by the defect
  bound of Theorem O-SEED and Lemma Z'. No reflection positivity of the effective theory is used.
- (HO L252) The first-passage density is in no zone: (R1) x_K >= gamma_H^(-2); (R2) large-field labels and
  small-field characteristic functions; (R3) local terms bounded on a polydisc only.
- (HO L291-309) The band. Groups (G1) weak steps with explicit constants, (G2) order-one steps, (G3) landing.
  Length ratio across (G2): about 10 (from a m = 1) to about 600 (from beta_W = 4). GUIDE numbers.
- (HO L313-323) Each step must keep (P1) exactness, (P2) symmetry, (P3) locality with a rate, (P4) torus and
  cutoff consistency, (P5) vacuum structure, (P6) large-field resummation, (P7) quantitative transport.
  (P7) in the band is marked OPEN and is called the crux.
- (HO L246) Ceiling. Perturbed vertex-block criteria fail for beta >= 0.775 whatever W (from BC Proposition CEIL).

Observation for this file (mine, ARGUED): the zone is defined by worst-case one-link influence.
So the target of the last step is a worst-case statement about the output action,
but the step itself may use any property of the input measure, not only worst-case ones.

## Step 1b. What row 848's check fixes (READ D/library/gap-e17phys-check-astra.md L1-216, in full)

- (L92-106) Verdict FAILS for one claim: an argument built on the outline (`sa_ym4.tex`, "SA") is not a matched
  port of the complete account (`sa_ca_I.tex`, `sa_ca_II.tex`, "CA-I", "CA-II"). Example: CA-I Theorem 0 (iv)
  at CA-I L2715-2826 states its witness with a lattice background-curvature kernel on the reference torus,
  not with the continuum kernel that the outline uses.
- (L64-70) The complete account does prove the complex chessboard estimate (CA-II L61205-61415).
- (L12) The library holds an index `library/sa-index/` for choosing bounded line ranges.

Rule taken for this file: every citation of the account names the file (SA outline, CA-I or CA-II) and the lines
I read myself. A statement read only through another lane file is marked "READ through".
A statement of the outline is not presented as a statement of the complete account.

## Step 2. The finish line and the fact tests (checklist)

Short names: FL = D/library/gap-finishline-opus.md; FIN = D/FINISH.md.

**(SEED-FP)** (READ FL L112-118). There are K_0, a physical size ell, and s_* < 1/5041 such that for every
first-passage datum (K, beta) at g with K >= K_0: S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_*.
This is a thermal sum of the bare Wilson transfer operator at a fixed physical size, uniform in the cutoff.

**(SEED-L)** (READ FL L124-126). limsup of Phi_L = L^4 log Z_(K,ell,beta) - log Z_(K,L ell,beta) is below (L/2) log(13/10).
Both tori are in the account's family. Lemma FL (FL L128-132) carries (SEED-L) to (SEED-FP).

**Exactness** (READ through FL L122: SA L17285 and CA-I L2582). The integral of rho_k equals the bare Z at every level, exactly.

**Why a plain Wilson seed at the unit scale is not enough** (READ FL L138-141). The regular terms E have norm E_0 of
order one. The account bounds the difference only by e^(O(ell^4)).

Fact tests (each is a fact about what a correct argument must do; READ FIN rows as cited):

- (T-U1) The argument must fail for U(1) in its Coulomb phase. Row 786 (FIN L863): for periodic Villain U(1) at
  beta >= 2^14 the gauge-invariant Langevin gap on (Z/M)^4 tends to 0 as M grows (proved by Codex gpt-6-astra max;
  check is row 794).
- (T-Q8), (T-2T) The argument must use something that Q_8 and the binary tetrahedral group 2T lack where they
  would otherwise pass. Row 838 (FIN L915): Q_8 freezes near beta 1.15 and 2T near 2.15 (GUIDE there); their Haar
  moments first differ from SU(2) at degrees 4 and 6 (PROVED there). Row 843 (FIN L920): the commutator contraction
  holds verbatim for both; a tool at the crossover must see spin 2 or 3.
- (T-WC) Worst-case caps. Single-site Dobrushin bounds cap at 2/3; vertex-block bounds cap at 0.775
  (row 836 Proposition CEIL, READ through HO L246). Background-uniform layer twist bounds are false above
  4 G_3 = 1.0109 (row 839, FIN L916, Proposition TB2).
- (T-AN) The annealed condition (AN) of row 845 (FIN L922) removes uniformity over exteriors, but its open part
  (SP-ext) is a space-time Peierls bound for bad exteriors. The brief states the lead's reading: (AN1) is the
  worst case in disguise (row 845, checked).
- (T-band) The order-one window is bare beta_W about 2.3 to 2.6. The real object is the first-passage action.

Consequence for the design (mine, ARGUED). Any step that bounds the output action by a worst-case influence of the
input action is capped by (T-WC) and cannot start at beta_W 2.3. So the block bound must use an average over the
integrated variables under the true measure, and must be allowed to fail on a set of rare configurations that is
then resummed. A step that never looks at the group beyond compactness cannot pass (T-U1).

## Step 3a. Soft block kernels: what is exact, and what is free

Short name VL = D/library/gap-vmf-lip.md. READ VL L208-220: Corollary V1, for all F, F' in R^4,
d_Lip(mu_F, mu_F') <= |F - F'|/4, with mu_F the law on S^3 with density proportional to exp(<F, h>), and d_Lip the
dual chord-Lipschitz distance. READ VL L222-236: Lemma DC, chord form (influence numbers C_ij, row sums at most alpha < 1).

**Notation.** SU(2) = S^3 in R^4 (quaternions). <A, B> is the Euclidean inner product, <A, B> = (1/2) Re tr(A B^dagger).
N(r) = integral over S^3 of exp(r <h, e>) sigma(dh), e any unit vector. For v in S^3, u in R^4, a >= 0:

    k_a(v | u) = exp(a <v, u>) / N(a |u|).            (the von Mises-Fisher density with field a u)

Fine torus T (side n L), coarse torus T' (side n, sites L Z^4). For a coarse link c from x to x' = x + L e_mu let
Gamma_c be a finite set of fine paths from x to x', with weights p_gamma >= 0 of sum 1, and

    Ubar_c(U) = sum over gamma of p_gamma U(gamma)   in R^4,   |Ubar_c| <= 1.     (block average)

    K_a(V | U) = product over coarse links c of k_a(V_c | Ubar_c(U)),     rho'(V) = integral K_a(V | U) rho(U) dU.

Special cases. (N) noise: L = 1, Ubar_c = U_c. (D_a) noisy straight decimation: Gamma_c is the one straight path, so
|Ubar_c| = 1. (D) straight decimation: the limit a -> infinity of (D_a). Averages over tubes of paths give |Ubar_c| < 1
in general. Balaban's averages are different functions (defined near the identity); they are not used here.

**Lemma K1 (exactness and covariance; PROVED).** (i) The integral of K_a(V | U) over V is 1 for every U. So the
integral of rho' equals the integral of rho: clause (E0) of EXIT (HO L260) holds. (ii) If g is a fine gauge
transformation and h its restriction to the coarse sites, then K_a(V^h | U^g) = K_a(V | U). So rho' is invariant under
the coarse gauge group when rho is gauge invariant. (iii) If the families Gamma_c and the weights are covariant under
the translations by L and the hyperoctahedral group, rho' inherits these symmetries of rho.
*Proof.* (i) sigma is rotation invariant, so the integral of exp(a <v, u>) over v is N(a |u|), also at u = 0.
(ii) U^g(gamma) = g_x U(gamma) g_x'^(-1) for a path from x to x'. So Ubar_c(U^g) = g_x Ubar_c(U) g_x'^(-1).
Left and right multiplication by unit quaternions are isometries of R^4. So <V^h_c, Ubar_c(U^g)> = <V_c, Ubar_c(U)>
and |Ubar_c(U^g)| = |Ubar_c(U)|. Then rho'(V^h) = integral K_a(V^h | U^g) rho(U^g) dU = rho'(V) (Haar is invariant
under U -> U^g). (iii) The same change of variables. QED

**Lemma K2 (the a priori Lipschitz bound; PROVED).** Let rho >= 0 be integrable and not almost everywhere zero.
No other hypothesis. Then rho' is strictly positive and continuous, and for V, V' that differ only at one coarse link c:

    | log rho'(V) - log rho'(V') |  <=  a |V_c - V'_c|.                                   (K2)

*Proof.* For every U: K_a(V | U) = K_a(V' | U) exp(a <V_c - V'_c, Ubar_c(U)>), and
|<V_c - V'_c, Ubar_c>| <= |V_c - V'_c| because |Ubar_c| <= 1. So
e^(-a |V_c - V'_c|) K_a(V' | U) <= K_a(V | U) <= e^(a |V_c - V'_c|) K_a(V' | U). Integrate against rho.
Positivity: k_a >= e^(-a)/N(a) > 0. QED

So the chord Lipschitz constant of the output action S' = -log rho' in every coarse link is at most a.
This holds for an input with characteristic functions, with large-field labels, with any coupling.

**Lemma K3 (the coarse one-link law is a mixture; PROVED).** Let mu^(c)_V be the probability with density
proportional to [product over c' != c of k_a(V_c' | Ubar_c'(U))] rho(U). Then the conditional density of V_c given
the other coarse links, under rho', is

    p(v | V_(not c)) = E_(mu^(c)_V) [ k_a(v | Ubar_c) ].

So the conditional law is the mixture of the laws mu_(a u) over the law of u = Ubar_c under mu^(c)_V.
*Proof.* rho'(V) = Z^(c)(V_(not c)) E_(mu^(c)_V)[k_a(V_c | Ubar_c)], with Z^(c) the normalisation of mu^(c)_V.
The integral over V_c of the second factor is 1 (Lemma K1 (i)). QED

**Lemma K4 (coarse influence = pinned fine covariance; PROVED from Corollary V1).** For a set A of coarse links
and fields h = (h_c), c in A, each in the closed unit ball of R^4, let mu_(A,h) be the probability with density
proportional to [product over c in A of exp(a <h_c, Ubar_c>)/N(a |Ubar_c|)] rho(U). Call these the pinned measures.
Let V, V' differ only at the coarse link k != c. Then

    d_Lip( p(. | V_(not c)), p(. | V'_(not c)) )  <=  (a^2/4) kappa_ck |V_k - V'_k|,
    kappa_ck = sup | Cov_(mu_(A,h)) ( phi(Ubar_c), <e, Ubar_k> ) |,

the supremum over A = all coarse links but c, all h, all unit e, and all 1-Lipschitz phi on the unit ball of R^4.
*Proof.* Let psi be chord-1-Lipschitz on S^3 and Psi(u) = mu_(a u)(psi). By Corollary V1, Psi is (a/4)-Lipschitz
on R^4. By Lemma K3 the two conditional means of psi are the means of Psi(Ubar_c) under mu^(c)_V and mu^(c)_V'.
Put h_k(s) = (1 - s) V_k + s V'_k (in the unit ball) and h_c' = V_c' for the other links; mu_s = mu_(A, h(s)).
The integrands are bounded, so d/ds mu_s(Psi(Ubar_c)) = a Cov_(mu_s)(Psi(Ubar_c), <V'_k - V_k, Ubar_k>).
Divide Psi by a/4 and integrate over s in [0, 1]. QED

**Proposition FREE (PROVED).** For every input rho as in Lemma K2, every L, every family of block averages and
every torus: (i) the total masses agree; (ii) the output action has chord Lipschitz constant at most a in every link;
(iii) the chord influence numbers of Lemma DC for the one-link laws of rho' may be taken as C'_ck <= a^2/4 for
every pair c != k. So on a coarse torus with link set E' and diameter D, for every m >= 0,

    sum over k != c of C'_ck e^(m d(c,k))  <=  (a^2/4) |E'| e^(m D).

*Proof.* (i), (ii) are Lemmas K1, K2. (iii): |Cov(X, Y)| <= (osc X/2)(osc Y/2); osc phi <= 2 on the unit ball and
osc <e, Ubar_k> <= 2. So kappa_ck <= 1. QED

**The same for U(1) (PROVED).** Replace S^3 in R^4 by S^1 in R^2. Lemmas K1-K3 hold word for word. In Lemma K4 use
|d/dt mu_(F_t)(psi)| = |Cov(psi, <h, F' - F>)| <= |F' - F| (both factors have oscillation at most 2). So Proposition FREE
holds for U(1) with a^2 in place of a^2/4. It holds for every coupling, in particular in the Coulomb phase.

**Reading (ARGUED).** Clause (E0), the total form of (E1) (a strictly positive global density with a global
Lipschitz logarithm), the size part of (E3) and of (P7), and obstacles (R1)-(R3) of HO 6.1 in their total form
cost nothing: one soft step gives them for any input and for U(1). On any fixed torus even a weighted Dobrushin
condition holds for small a. So none of these carries information. This does not contradict Theorem HO: its proof
(HO L176-180) also uses (E2), the torus consistency (TC) of the local terms and of the vacuum constants, with
finite norms w_m and e_m. With an exact soft kernel the constant of the output is -log Z_T itself. So in EXIT the
whole load is on (E2), (P3)-(P5): a torus-consistent local decomposition of S', vacuum part included.
The "five per cent at beta = 1/4" is not an accuracy problem. It is a locality problem.

## Step 3b. Noisy straight decimation: loops, reflection positivity, and what a uniform landing implies

In this step the kernel is (N) or (D_a): Ubar_c = U(gamma_c) is a group element, gamma_c the straight path.
Then <v, u> = x(v u^(-1)), so k_a(v | u) = f_a(v u^(-1)) with the class function f_a = exp(a x)/N(a).

**Lemma K5 (characters; PROVED).** For every irreducible representation D^j of SU(2), j >= 1/2, and a > 0 there is
a number lambda_j(a) in (0, 1) with  integral D^j(v) f_a(v u^(-1)) dv = lambda_j(a) D^j(u).  Given U, the coarse
links V_c are independent. So for a product A'(V) = product over c of one matrix element of D^(j_c)(V_c),

    E[ A'(V) | U ] = Lambda(A') A'(Ubar(U)),     Lambda(A') = product over c of lambda_(j_c)(a)  in (0, 1].

*Proof.* Substitute v = w u: the integral is M D^j(u) with M = integral D^j(w) f_a(w) dw. M commutes with D^j
because f_a is a class function, so M = lambda_j Id with lambda_j = (2j+1)^(-1) integral chi_j f_a (Schur).
lambda_j > 0: exp(a x) = sum a^n x^n/n!, and x^n = (chi_(1/2)/2)^n is a nonnegative combination of characters in
which chi_j occurs for n = 2j. lambda_j < 1: |chi_j| <= 2j+1 with strict inequality on an open set, and f_a > 0
has integral 1. QED  (Recalled, not used: lambda_j(a) = I_(2j+1)(a)/I_1(a). GUIDE.)

**Lemma K6 (loops and truncated correlations transport exactly; PROVED).** Write mu = rho/Z, mu' = rho'/Z.
(i) For a closed coarse path C that uses each coarse link at most once, and C^L the fine loop made of the straight
paths: mu'(chi_j(V(C))) = lambda_j(a)^|C| mu(chi_j(U(C^L))).
(ii) For products A', B' as in Lemma K5 with disjoint link supports:
Cov_mu'(A', B') = Lambda(A') Lambda(B') Cov_mu(A' o Ubar, B' o Ubar).
*Proof.* chi_j(V(C)) is a sum of products as in Lemma K5 with all j_c = j. For (ii): given U, A' and B' are
independent, so E[A' B' | U] = E[A' | U] E[B' | U]; apply Lemma K5 to each factor and to the means. QED

So the coarse theory has the same truncated loop correlations as the fine theory, up to explicit nonzero factors.
A noise or decimation step neither creates nor destroys a decay rate of loop correlations.

**Lemma K7 (masses of twisted sectors; PROVED).** Lemma K1 (i) needs only rho >= 0. So the image of each
centre-twisted density has the mass of that twisted density. The vortex free energies are invariant under the step.

**Lemma K8 ((N) and (D_a) keep reflection positivity; PROVED).** Let theta be the reflection of the fine torus in
a pair of hyperplanes Pi of coarse sites (x_mu = 0 and x_mu = nL/2). Suppose integral conj(theta F) F rho dU >= 0
for every bounded F of the links in the closed positive half. Then the same holds for rho' and every bounded F'
of the coarse links in the closed positive half.
*Proof.* Coarse links lie in Pi (set E_0), or in the positive half off Pi (E_+), or in the negative half (E_-).
The straight path of a link of E_0 lies in Pi; that of a link of E_+ lies in the closed positive half. Fix the
values V_0 on E_0. Put G(U) = integral dV_+ [product over c in E_+ of k_a(V_c | U(gamma_c))] F'(V_+, V_0), a function
of the fine links of the closed positive half. theta permutes E_- and E_+, fixes E_0, and k_a(v^(-1) | u^(-1)) = k_a(v | u).
So the V_- integral of [product over E_- of k_a] conj(theta F') is conj(theta G). The remaining factor
P_0(U) = product over c in E_0 of k_a(V_c | U(gamma_c)) is positive and depends only on links in Pi, which theta fixes.
With F_(V_0) = G P_0^(1/2): integral conj(theta F') F' rho' dV = integral dV_0 integral conj(theta F_(V_0)) F_(V_0) rho dU >= 0. QED

Remark (ARGUED). For averages over tubes of paths the normaliser N(a |Ubar_c|) of a link in Pi couples the two
sides through |Ubar_c|^2, with a negative coefficient at lowest order (1/N decreases in r). So tube averages are not
covered by this proof. A coarse link lies in three coarse hyperplanes, whose intersection is its straight line. So among
soft kernels of this family, the straight path is the choice that keeps all coarse site reflections.

**Corollary K9 (a uniform landing gives clustering of block loops; PROVED given Lemma DC* of HO L124-130, an
author proof whose check is row 850).** Let rho' be the image of rho under (N) or (D_a). Suppose that on a coarse
torus the one-link laws of rho' have chord influence numbers with sum over k != c of C'_ck e^(m d(c,k)) <= alpha < 1.
Let C_1, C_2 be closed coarse paths with disjoint links, each link used once, at distance d. Then

    | Cov_mu( chi_(1/2)(U(C_1^L)), chi_(1/2)(U(C_2^L)) ) |
        <=  lambda_(1/2)(a)^(-|C_1| - |C_2|)  (8 alpha |C_1| / (1 - alpha))  e^(-m d).

*Proof.* Put f = chi_(1/2)(V(C_1)), g = chi_(1/2)(V(C_2)), D = the links of C_2. For each value y of V_D the
conditional law mu'_y of V given V_D = y has the same one-link kernels as mu' at every link off D. Lemma DC* with
mu_1 = mu', mu_2 = mu'_y, b = 0 gives |mu'(f) - mu'_y(f)| <= 2 alpha Delta(f) e^(-m d)/(1 - alpha). Then
Cov_mu'(f, g) = mu'( g (mu'_(V_D)(f) - mu'(f)) ), |g| <= 2, and Delta(f) <= 2 |C_1| (chi_(1/2) = 2 <., 1> has
chord Lipschitz constant 2 in each link). Lemma K6 (ii) converts to mu. QED

Consequences (PROVED from K9 and Proposition FREE).
1. If one soft step lands a family of densities with (L, a, alpha, m) independent of the torus, then the L by L
   Wilson loops of the input family cluster at the rate m per L fine units, uniformly in the torus. A proof of
   EXIT with such a last step contains a proof of this clustering at the landing scale.
2. On one fixed torus the landing of Proposition FREE needs a^2 of order e^(-m D)/|E'|. Then the factor
   lambda^(-8) is at least of order e^(4 m D) |E'|^4 and the bound of K9 is empty. So nothing is created for free.
3. The controlled quantity that U(1) cannot fake is the rate m at fixed a, uniformly in the torus: a measure whose
   loop correlations do not decay exponentially has no uniform landing with m > 0, whatever the block kernel
   of type (N) or (D_a). (The U(1) input fact is cited in Step 8.)

## Step 3c. The candidate block maps, judged against (P1)-(P7) and the fact tests

Marks in this table: PROVED refers to Steps 3a, 3b. Everything else is ARGUED (my reading; recalled physics is GUIDE).

| Map | Exact (P1) | Output size | Output locality (P3)-(P5) | Remarks |
|---|---|---|---|---|
| (D) straight decimation, a = infinity | yes (a marginal) | no a priori bound | needs mixing of the input given the frozen 1-skeleton | keeps loops exactly and keeps reflection positivity (K6, K8 in the limit); output can be as rough as the input |
| (N) noise, L = 1 (heat-kernel type smearing of each link) | yes (K1) | free: Lipschitz constant at most a (K2) | equals clustering of the pinned input (K4, K9) | a semigroup in a for the heat kernel; one step of total noise equals many small steps |
| (D_a) noisy straight decimation | yes (K1) | free (K2) | as (N), at block scale L | keeps reflection positivity (K8), loops (K6), twisted masses (K7) |
| soft tube averages | yes (K1) | free (K2) | as (N); better ultraviolet behaviour expected at weak coupling | reflection positivity not shown (remark after K8) |
| Balaban averaging with delta or sharp constraints, as in the account | yes (an exact change of variables, READ through FL L122) | set by the running coupling; no a priori bound | proved at weak coupling by the account's method; uses small-field and large-field regions | output is not a global Gibbs density (HO L252, (R2), (R3)) |
| Migdal-Kadanoff bond moving | no: the moved-bond partition function is a one-sided bound (recalled: Tomboulis; the lane's digest D/library/prior/gap-lit-2.md L45-49 records the Ito-Seiler objection) | closed recursion on one-plaquette class functions | exact by construction, but for the wrong measure | group blind: the recursion drives 4D U(1) to strong coupling too (GUIDE). The defect needs absolute accuracy O(1) on log Z (HO L315), which a one-sided bound cannot give |
| multigrid (several scales at once) | yes if each level is a kernel | as its last level | as its last level | a composition of the maps above; nothing new at the level of one step |

**What the table says (ARGUED).**
1. Exactness, symmetry and size are properties of the kernel. Soft kernels give them for free.
2. Every exact map moves the whole difficulty into one place: the conditional law of the fine field given the coarse
   field (the pinned measure) must cluster, with a rate, uniformly enough to give a torus-consistent local expansion
   of S' = -log rho'.
3. There are two sources of such clustering. (a) Pinning: the term a <V_c, Ubar_c> is strong compared with the
   coupling of the action. This is the mechanism of every weak-coupling renormalization step (the account's included).
   It works at any coupling if a is large enough (Step 5), but then the output is as stiff as the input.
   (b) Intrinsic clustering of the input at the block scale. This is the statement one wants to prove.
4. So a step that makes progress at order one must take a small enough to gain size, and must then get its locality
   from (b). No choice of kernel removes this. The number of steps is not the issue: one soft step with L above the
   correlation length and small a lands, if (b) holds at scale L.

**Fact tests on the table.** U(1): rows (N), (D_a) hold word for word for U(1) (Step 3a); they are group blind and
by themselves prove nothing; the group enters only through (b). Q_8 and 2T: the kernels k_a restrict to any finite
subgroup (replace Haar by the counting measure; Lemmas K1-K3, K6 for class functions hold with the same proofs;
Corollary V1 does not, but a total-variation form of K4 does). So again nothing here separates the groups.
Worst-case caps: K4 with a supremum over all pinning fields is a worst-case bound; Step 5 shows it cannot land an
input from outside the known zone.

## Step 4. The route chosen here, the controlled quantity, and the crux lemma

**Route (the best one found in this file; other routes are not excluded).** After the last step that the account's
method controls, apply one noisy straight decimation (D_a), block L, noise a, to the last-scale densities rho_T.
For (D_a) (and (N), L = 1) the output is a generating function (PROVED, by the definition of K_a with |Ubar_c| = 1):

    rho'_T(V) = N(a)^(-|E'|) Xi_T(a V),     Xi_T(J) = integral exp( sum over c of <J_c, U(gamma_c)> ) rho_T(U) dU,   J_c in R^4.   (4.1)

So S'_T(V) = |E'| log N(a) - log Xi_T(a V), and log Xi_T(J) - log Z_T is the cumulant generating function of the
straight block holonomies under mu_T = rho_T/Z_T. EXIT in this form asks: do the joint cumulants of the block
holonomies decay like trees, with a rate, consistently between tori?

**Exact invariants of a step (PROVED, Steps 3a-3b; all group blind).** Total mass; masses of twisted sectors;
loop expectations up to the factors lambda_j(a)^|C|; truncated loop correlations up to such factors; reflection
positivity in coarse hyperplanes. The a priori bound: the Lipschitz constant of S' is at most a.

**The quantity to control.** For unit pinning fields h on all coarse links but c put

    kappa^u_ck = sup | Cov_(mu_(A,h)) ( phi(U(gamma_c)), <e, U(gamma_k)> ) |      (A = E' minus c; |h_c'| = 1; |e| = 1; phi chord-1-Lipschitz on S^3),
    X_m(L, a) = sup over c of  sum over k != c of  e^(m d(c,k)) kappa^u_ck .        (the weighted pinned block susceptibility)

No quantity was found that is monotone along steps and not group blind. X_m is controlled, not monotone.

**Lemma K4' (unit fields; PROVED).** For (N) or (D_a): C'_ck <= (pi/2) a min(a/4, 1) kappa^u_ck.
*Proof.* As Lemma K4, with two changes. (1) Psi(u) = mu_(a u)(psi) is min(a/4, 1)-Lipschitz on S^3: a/4 by
Corollary V1; and 1 because mu_(a u') is the image of mu_(a u) under the rotation R in the plane of u, u' with
R u = u', and |R v - v| = |u' - u| |P v| <= |u' - u| (P the projection on that plane). (2) Move V_k to V'_k along
the great-circle arc, of length theta <= (pi/2) |V_k - V'_k|; all fields stay unit, and
d/ds mu_s(Psi) = a Cov_(mu_s)(Psi(U(gamma_c)), <dV_k/ds, U(gamma_k)>). QED

**Crux Lemma PIN-MIX(L, a, alpha, m) (statement; OPEN at order one).** There are L, a > 0, m > 0 and alpha < 1 such
that for every torus of the family, every cutoff K >= K_0 and every first-passage datum,

    (pi/2) a min(a/4, 1) X_m(L, a)  <=  alpha.                                                   (PIN-MIX)

In words: under every unit pinning of the other block holonomies, with strength a, the covariance between a
Lipschitz function of one block holonomy and another block holonomy decays exponentially in their distance, with
a weighted sum below 1/((pi/2) a min(a/4, 1)).

**Theorem LAND (PROVED given Lemma DC* of HO, as in K9).** Assume PIN-MIX(L, a, alpha, m) for densities rho_T. Then
for every torus of the family: (i) the integral of rho'_T is Z_T; (ii) rho'_T is a strictly positive smooth
gauge-invariant density with Lipschitz constant of its logarithm at most a per link; (iii) its one-link laws satisfy
the weighted chord Dobrushin condition with (alpha, m); (iv) the L by L loops of mu_T cluster as in Corollary K9;
(v) if rho_T is reflection positive in coarse hyperplanes, so is rho'_T.
*Proof.* K1, K2, K4', K9, K8. QED

**What Theorem LAND does not give (OPEN to write; ARGUED to be within reach of PIN-MIX in a complex form).**
Theorem HO of row 846 uses the potential form (E1)-(E2) with finite w_m, e_m and (TC). (4.1) gives a potential
through the cumulant expansion of log Xi_T, which converges if the pinned covariance bounds hold for complex
pinning fields in a polydisc (then Cauchy estimates give tree bounds for all cumulants). Its terms depend on the
torus by exponentially small amounts, not exactly as (TC) asks. Lemma DC* allows such kernel discrepancies (the
numbers b_i, HO L122), so Theorem O-SEED should survive with one more exponentially small term. I did not write this.
Step 6 gives an exact identity that avoids the potential for L = 1.

**Why U(1) cannot fake PIN-MIX (PROVED implication, ARGUED input).** By Theorem LAND (iv), PIN-MIX with m > 0
uniformly in the torus forces exponential clustering of loop characters. The Coulomb phase has a massless photon
(recalled: Guth; Froehlich-Spencer; the lane's theorem of row 786 proves non-summable plaquette-score correlations
for periodic Villain U(1) at beta >= 2^14, READ D/library/gap-tu-retry.md L92-98 and L240-250; a score is not a
character polynomial, so that theorem is not literally the negation of K9; the single-character statement is
recalled, not read). For a frozen finite group (Q_8 above its freezing coupling) loops do cluster, yet PIN-MIX
must still fail: Theorem LAND (iii) makes every twisted mass ratio tend to 1 with the size (ARGUED: a twist is
locally invisible to a Dobrushin measure), while a deconfined phase suppresses twisted sectors (GUIDE). There the
failure is long-range order of the pinned gauge-variant covariances.

## Step 5. Attempt, stage A: the two halves of PIN-MIX that can be proved, and why they do not overlap

PIN-MIX asks for two things at once: a rate m > 0 (locality) and a weighted sum below the threshold (size).
The size half is free for small a (Proposition FREE gives kappa <= 1 per pair, but no summability).
This step proves the locality half by pinning, at every coupling, and then computes where the two halves meet.

READ VL L59-76, Theorem V (author proof by Codex gpt-6-astra; HO L12 records its check as row 790): for every F
in R^4, unit e and chord-1-Lipschitz phi, |Cov_(mu_F)(phi, h.e)| <= a(|F|) <= 1/4, with a(k) = z'(k)/(k z(k)).
READ VL L99, (1): E_F h = a(k) F. READ VL L336-346: the one-link field of the Wilson action is F = beta times
the sum of six unit staples; two distinct links share at most one plaquette (sides at least 3); a link has 18
plaquette partners; changing one partner changes F by at most beta times the chord distance.

**Lemma V-inf (large fields; PROVED from Theorem V).** a(k) <= 1/k. If the segment from F to F' stays outside the
open ball of radius r_0 > 0, then d_Lip(mu_F, mu_F') <= |F - F'|/r_0.
*Proof.* |E_F h| <= 1 and E_F h = a(k) F give a(k) k <= 1. Along F_t = F + t(F' - F):
d/dt mu_(F_t)(psi) = Cov_(F_t)(psi, h.(F' - F)), at most a(|F_t|) |F' - F| <= |F' - F|/r_0. Integrate. QED

**Theorem STEP (locality from pinning at any coupling; PROVED given Theorem V of VL and Lemma DC* of HO).**
Input: the Wilson density rho = exp(beta sum_p x_p) on a torus with all sides at least 3, any beta >= 0.
Kernel: (N), L = 1, noise a. Let m >= 0 and suppose

    alpha_p e^m < 1,     alpha_p = 18 beta / (a - 6 beta),     a > 6 beta.

Then X_m(1, a) <= alpha_p e^m / (1 - alpha_p e^m), and so, for every link c,

    sum over k != c of C'_ck e^(m d(c,k))  <=  (pi/2) a min(a/4, 1) alpha_p e^m / (1 - alpha_p e^m).        (5.1)

In particular C'_ck <= (pi/2) a min(a/4, 1) (1 - alpha_p e^m)^(-1) alpha_p e^m e^(-m d(c,k)): the one-link laws of
the output depend on far links exponentially weakly, at every coupling, if the noise is weak enough.
*Proof.* Fix c, unit fields h on the links other than c, and the pinned measure mu = mu_(A,h). Its one-link law
at l != c, given the other links, is mu_(F_l) with F_l = a h_l + beta S_l, S_l the sum of the six staples,
|S_l| <= 6. So |F_l| >= a - 6 beta = r_0, and the same holds on the segment between two such fields with the
same h_l. By Lemma V-inf and the READ geometry, on Lambda = E minus c the pinned kernels satisfy (8) of Lemma DC
with numbers C_lj = beta n(l,j)/r_0, a symmetric matrix with weighted row and column sums at most alpha_p e^m
(18 partners, distances at most 1, HO L57).
Let k != c, e a unit vector, and g(u) = E_mu[<e, U_k> | U_c = u]. For two values u, u' the conditional laws of the
links of Lambda are Gibbs for the pinned kernels with boundary values u and u'; their kernels at j differ by at
most b_j = beta n(j,c) |u - u'|/r_0 in d_Lip (Lemma V-inf again). Lemma DC* (HO L118-128, with D empty) gives
|g(u) - g(u')| <= sum_j G_kj b_j, G = sum_n C^n. So Lip(g) <= sum_j G_kj C_jc.
For chord-1-Lipschitz phi: Cov_mu(phi(U_c), <e, U_k>) = Cov_mu(phi(U_c), g(U_c)), and
|Cov(X, Y)| <= (osc X/2)(osc Y/2) <= 1 . Lip(g) (the chord diameter is 2). So kappa^u_ck <= sum_j G_kj C_jc.
Weights: e^(m d(c,k)) <= e^(m d(k,j)) e^(m d(j,c)); weighted column sums of powers are at most powers of weighted
column sums. So the sum over k of e^(m d(c,k)) kappa^u_ck is at most (1 - alpha_p e^m)^(-1) alpha_p e^m.
(5.1) is Lemma K4'. QED

**Where the two halves meet (PROVED arithmetic from (5.1); the sharp-constant line is ARGUED).**
- Locality half: needs a > 6 beta + 18 beta e^m, so a > 24 beta at least.
- Size half: needs the right side of (5.1) below 1. For a <= 4 and m -> 0 this reads (9 pi/4) beta a^2 < a - 24 beta.
  A solution a exists exactly when 1 > 4 (9 pi/4)(24) beta^2 = 216 pi beta^2, that is beta < 0.0384.
- For a >= 4 the right side of (5.1) is at least 9 pi beta e^m. So (5.1) lands nothing with beta >= 1/(9 pi) = 0.0354
  at large a, and nothing with beta >= 0.0384 at any a.
- With the sharp constants one expects from the same mechanism (no factor pi/2; the vMF constant 1/4 at the
  unpinned link c; ARGUED, not proved): C'_ck about min(a/4, 1) (beta/4) n(c,k) a/(a - 24 beta), and a landing only
  for beta below about 0.1.
- The direct chord Dobrushin range of the lane is beta < 2/9 (HO L82). So the pinned route lands only inputs that
  are already inside the known zone. For an input outside the zone, pinning strong enough to give locality
  returns an output that is as stiff as the input: as a -> infinity the output is the input.

**Why iterating does not help in worst-case form ((i) PROVED; (ii) formal algebra; the reading ARGUED).**
Add independent Gaussian noise of variance 1/a to every coordinate of a Gaussian field with precision matrix P.
The new precision is P' = a P (P + a)^(-1) = a - a^2 (P + a)^(-1).
(i) Let P = -Delta + mu^2 on a finite torus (lattice Laplacian, mu >= 0; for mu = 0 read the statement as the limit).
(P + a)^(-1) has positive entries and (P + a)^(-1) 1 = (a + mu^2)^(-1) 1. So the off-diagonal entries of P' are
negative, P' 1 = (a mu^2/(a + mu^2)) 1, and the Dobrushin row sum of P' (the sum over y != x of |P'_xy|/P'_xx) is
1 - (a mu^2/(a + mu^2))/P'_xx. It is below 1 for mu > 0 and equal to 1 for mu = 0, for every a. Noise cannot move
a massless Gaussian off the boundary of the Dobrushin condition. This is the spin-wave picture of U(1) (GUIDE as
to relevance).
(ii) To first order in 1/a, P' = P - P^2/a. Take formally P = D(1 - O) with a constant diagonal D, a translation
invariant matrix O with nonnegative entries, zero diagonal and row sum sigma, and q = (O^2)_xx. Then the row sum
of P' is sigma' = sigma + (sigma - 1)(sigma + q) D/a + O(a^(-2)). So a row sum above 1 grows under weak noise and
one below 1 shrinks. (For sigma > 1 this P is not positive, so no Gaussian measure exists; the algebra is a
caricature of how worst-case influence numbers of a compact model transform, nothing more.) The zone is the basin
where the worst-case bookkeeping closes; from outside it does not enter. This agrees with the caps of rows 836
and 839 and with the brief's remark on (AN1).

**Verdict of stage A.** PROVED: the locality half of the crux at every coupling (Theorem STEP), and the size half
(Proposition FREE). Their overlap, with bounds that take a supremum over the pinning fields, is beta < 0.0384
(proved) and about 0.1 at best (argued). The order-one band needs the overlap at a of order one with the locality
coming from the input measure itself, not from pinning. That is not a worst-case statement.

## Step 6. Attempt, stage B: an exact one-observation form of the defect, and where the attempt stops

Stage A took a supremum over all pinning fields. This stage shows that the defect itself needs only one pinning
field, the flat one, and needs it in a comparison form. It then locates the open region exactly.

**Setting.** Wilson density rho_T = exp(beta sum_p x_p) on the hypercubic torus T = T_n (n^4 sites). For a >= 0 let
mu^T_a be the probability with density proportional to exp(a sum over links l of <1, U_l> + beta sum_p x_p(U)).
This is the pinned measure of Step 4 with L = 1 and all fields equal to 1; it is the fixed-length SU(2) Higgs model
in unitary gauge with hopping a (GUIDE as to the name). Put A(a) = N'(a)/N(a) and

    e_T(a) = E_(mu^T_a) <1, U_l> - A(a)       (the same for every link l, by the translations and reflections of T).

**Theorem HL (the Higgs-line identity; PROVED).** For every beta >= 0 and every T: the integral of e_T over [0, s]
converges as s -> infinity, and

    log Z_T = 6 beta |T| - 4 |T| integral_0^infinity e_T(a) da.                                          (6.1)

So for integers rho >= 2 and n:   Phi^rho(n) = rho^4 log Z_(T_n) - log Z_(T_(rho n)) = -4 (rho n)^4 integral_0^infinity [ e_n(a) - e_(rho n)(a) ] da.   (6.2)
*Proof.* Put A_T(a) = integral [product over l of k_a(1 | U_l)] rho_T(U) dU. Then A_T(0) = Z_T. The integrand is
smooth in a and bounded, so d/da log A_T(a) = sum over l of E_(mu^T_a)[<1, U_l> - A(a)] = 4 |T| e_T(a). As a -> infinity
the product law of the U_l with densities k_a(1 | .) tends weakly to the point mass at U = 1, and rho_T is
continuous, so A_T(a) -> rho_T(1) = exp(6 beta |T|) (six plaquettes per site, x_p = 1). Integrate from 0 to s and
let s -> infinity. In (6.2) the terms 6 beta |T| cancel exactly. QED

**Lemma HL2 (the strongly pinned part of the line is exponentially small; PROVED given Theorem V of VL and
Lemma DC* of HO).** Let n >= 8, d_n = n/2 - 5/2, a_1 = 78 beta. Then

    | integral over a >= a_1 of [ e_n(a) - e_(rho n)(a) ] da |  <=  72 beta 2^(1 - d_n) / (d_n - 1).

*Proof.* For a >= a_1 every one-link field of mu_a is F_l = a 1 + beta S_l with |F_l| >= a - 6 beta. By Lemma V-inf
the kernels satisfy (8) with C_lj = beta n(l,j)/(a - 6 beta), weighted row sums 18 beta e^m/(a - 6 beta). Choose m
with 18 beta e^m/(a - 6 beta) = 1/2 (possible with m >= log 2 since a - 6 beta >= 72 beta). Box cut: let Q = {0,...,n-1}^4
in T_(rho n) and mutilde the image of the marginal of mu^(T_(rho n))_a on the links of Q. The one-link kernel at l
depends only on the links of the plaquettes through l. So, exactly as in the proof of Lemma BOX (HO L132-138, which
uses only this locality), mutilde and mu^(T_n)_a have the same one-link kernels at every link whose midpoint
coordinates are all at circular distance more than 2 from n - 1/2. Take l with midpoint within 1/2 of the antipode
of the seam point; its distance to the excluded set D is at least d_n. Lemma DC* (D as stated, b = 0) with
f = <1, U_l> (Delta(f) <= 1) gives |e_n(a) - e_(rho n)(a)| <= 2 (1/2) e^(-m d_n)/(1 - 1/2) = 2 (36 beta/(a - 6 beta))^(d_n).
Integrate: with x = (a - 6 beta)/(36 beta) the integral over a >= a_1 is 72 beta times the integral of x^(-d_n) over x >= 2. QED

**Corollary HL3 (a second derivation of the strong-coupling defect bound; PROVED given the same inputs).**
If beta < 2/9, choose m > 0 with alpha = (9 beta/2) e^m < 1. Then for n >= 8 and rho >= 2

    |Phi^rho(n)| <= 4 (rho n)^4 [ 78 beta . 2 alpha e^(-m d_n)/(1 - alpha) + 72 beta 2^(1 - d_n)/(d_n - 1) ].

*Proof.* By Theorem V, a(|F|) <= 1/4 for every field. So for every a >= 0 the pinned kernels satisfy (8) with
C_lj = beta n(l,j)/4: pinning never increases the single-link bound. The box cut and Lemma DC* give
|e_n(a) - e_(rho n)(a)| <= 2 alpha e^(-m d_n)/(1 - alpha) for a in [0, a_1]. Add Lemma HL2 and use (6.2). QED
This reaches the conclusion of Theorem O-SEED (a) of row 846 at W = 0 by a different path: it integrates the
pinning strength at fixed beta and never visits a coupling below beta. It is a cross-derivation, not a check of row 846.

**The map of what is proved (PROVED from Theorem V and the lemmas above).** In the quarter plane of (beta, a), the
comparison |e_n(a) - e_(rho n)(a)| <= C e^(-m n) is proved by the single-link criterion in the region

    { beta < 2/9, all a >= 0 }  union  { a > 24 beta, all beta >= 0 }.

Every way of computing the defect at (beta, 0) by thermodynamic integration from a trivial point (beta = 0, or
a = infinity) ends at the point (beta, 0). For beta >= 2/9 that point is outside the proved region, and so is the
segment { (beta, a) : 0 < a <= 24 beta } below it. Row 846's Identity PHI is the path along the axis a = 0.

**The planted average is free (PROVED; a remark).** Let eta be a field of imaginary quaternions and
xi_c = V_c eta_c the corresponding tangent field. For every smooth positive density p on a compact group,
the integral of p (-d_xi d_xi log p) equals the integral of p (d_xi log p)^2 >= 0 (integrate d_xi d_xi p = 0).
So the output action of any step is convex on average over its own law, for every input and every group.
Average convexity therefore carries no information; a Bakry-Emery argument on SU(2) (Ricci curvature 2 on the
unit S^3, recalled) needs the pointwise bound Hess S' >= -kappa > -2, and the pointwise defect is a^2 times a pinned
variance: the same quantity as in PIN-MIX, in an l^2 form.

**Where the attempt stops (exact statement).** The order-one block bound, on the bare Wilson measure, is
equivalent by (6.2) and Lemma HL2 to

    (HIGGS-FS)   4 (rho n)^4 | integral_0^(78 beta) [ e_n(a) - e_(rho n)(a) ] da |  below the seed margin,

uniformly along the first-passage data in the form (SEED-L) of FL L124-126 (there rho = L and the two tori are in
the account's family; on the bare lattice n is the side in bare units). For beta >= 2/9 no proof exists for
the range 0 < a <= 24 beta. The single-link criterion fails there (its row sum is 18 beta min(1/4, 1/(a - 6 beta)) >= 1).
Vertex-block criteria applied to the pinned measure would move the line a = 24 beta down by a constant factor
(ARGUED) but cannot reach a = 0 above their caps (row 836). At a -> 0 the statement is the comparison of the
plaquette mean of the pure gauge theory between the two tori (the coefficient of a^3 in e_T is a multiple of
the plaquette mean, ARGUED by gauge averaging), which is the original problem. I found no inequality that
controls the pinned measure in the strip 2/9 <= beta <= 2.6, 0 < a <= 24 beta without a supremum over
environments, and no monotonicity in a or in beta that is not shared by U(1). The attempt stops here.

