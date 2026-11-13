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


## Resumed 2026-11-13 after the 03:06Z interrupt

Clone now at commit 9f1e04272b03270994c98fb4b9716e071924bac4 (branch claude/ym4d-hard-route; `git pull --ff-only`
said "Already up to date"). The header commit 2b6acd1732dd is the commit of the first run. Steps 1a-6 above are
finished and are not redone. I re-read this file in full before writing this line.

Remaining plan (one step per response, each appended before the next):

- R1. Read row 850 (D/library/gap-handoff-check-astra.md) in full. Record its verdict on Lemma DC*, Lemma BOX,
  Theorem O-SEED, Theorem HO, Identity PHI. Update the "PROVED given ..." marks of Steps 3b-6 where it bears.
- R2. Read rows 865 and 868 (the complete-account port of (SD-cyl)). Record what bears on the route and on Step 7.
- R3. Step 6c: one more line of attack on the strip of (HIGGS-FS) that takes no supremum over environments
  (reflection positivity of the flat-pinned measure). One response. Record what it proves and where it stops.
- R4. Step 7: map each step to the statements of the Sussman-Alpoge account it needs, with line ranges I read myself.
- R5. Step 8: fact tests on the final argument (U(1), Q_8, 2T, worst-case caps). Summary. RESULT line.

## Step R1. Row 850's check of row 846, and what it changes above

READ D/library/gap-handoff-check-astra.md L1-238, in full (short name CK; a line-by-line check of row 846 by
Codex gpt-6-astra xhigh; a check, not an audit). I also re-read HO L114-140 (Lemma DC*, Lemma BOX) against my uses.

**Inputs of Steps 3b-6 that row 850 checked.**
- Lemma DC* HOLDS (CK L25-31). The orientation is delta(f)^T G b; no column-sum hypothesis on C is needed.
- Lemma BOX HOLDS (CK L126-128). Its proof uses only the range of the kernels, (TC) and the tower property.
- Lemma TRUNC, Identity PHI and the cancellation of common vacuum terms HOLD (CK L130-146).
- Theorem O-SEED and Theorem HO HOLD AFTER CORRECTION (CK L162-168, L208-214): the star zone needs the domain
  6x + u_m < 1; all zones need beta >= 0 and 0 < alpha < 1.
- Not rechecked by row 850: Theorem V and Corollary V1 of VL (their check is row 790, READ through HO L12).

**My uses of DC*, verified again against the statement at HO L118-128 (PROVED given DC*, V1 and Theorem V).**
- Corollary K9: D = links of C_2, mu_2 = the conditional law given V_D, b = 0, delta(f) = 0 on D. DC* gives
  2 alpha Delta(f) e^(-m d)/(1 - alpha). The constant 8 alpha |C_1|/(1 - alpha) stands.
- Theorem STEP: D empty; f = <e, U_k> has delta_k(f) <= 1; b_j = C_jc |u - u'|. DC* gives sum_j G_kj b_j, the
  orientation that row 850 confirms. The weighted sum over k is a column sum of G C; C is symmetric. (5.1) stands.
- Lemma HL2: D = D_1 (R = 1, strip width 2), b = 0, alpha = 1/2. The distance n/2 - 5/2 agrees with CK L39-41
  at R = 1 for a support of one link. Lemma BOX is used for a measure with the extra one-link term a <1, U_l>,
  which is not gauge invariant; its proof does not use gauge invariance (CK L128). The bound stands.
So the marks "PROVED given Lemma DC* of HO" in Steps 3b-6 now read: PROVED given Lemma DC* and Lemma BOX (both
checked line by line by Codex astra xhigh, row 850) and Theorem V with Corollary V1 of VL (check row 790).

**Corrections that row 850 makes to statements I recorded in Step 1a and Step 2.**
1. Step 1a recorded "(HO L252) the first-passage density is in no zone". Row 850 corrects this (CK L196-202):
   the supplied representation and estimates do not establish membership in any corrected zone; no impossibility
   of a resummation is proved. A sum that contains labels or characteristic functions can have a bounded global
   log potential (chi + chi^c = 1). The brief's sentence "lies in no zone" inherits this correction.
   This agrees with Lemma K2 above: after one soft step every input has a globally Lipschitz log density.
2. (T-WC) in Step 2: the bound 0.775 is a ceiling on one family of majorants (CK L192-194). It is not a ceiling
   on the true response or on every block method. The twist bound of row 839 is a separate statement.
3. The star radius 0.0042 at beta = 0.35 FAILS; 0.0041 is safe. The radii at beta = 1/4 that Step 1a quotes
   (0.058 tree gauge, 0.053 stars) are safe at m = 0 (CK L85-100). The worked example n = 226 with m = 1,
   alpha = 1/2 FAILS its zone hypotheses (CK L51-53). I use neither.
4. Theorem HO needs less than EXIT asks (CK L142-146, L224-225): a common extensive vacuum constant cancels
   exactly whatever its size; local terms need pairwise torus consistency at each cutoff, not equality across
   cutoffs. This bears on the paragraph "What Theorem LAND does not give" in Step 4: only the uncancelled
   part of the vacuum term needs a uniform bound.
5. The margin in (HIGGS-FS). READ through CK L170-172: Lemma Z' states log(1 + S(T_0; (rho T_0)^3)) <= (2/rho) Phi_rho(T_0).
   With (6.2) the seed condition is one-sided and explicit:

       8 rho^3 n^4 integral_0^infinity [ e_(rho n)(a) - e_n(a) ] da  <=  log(1 + s_0),   s_0 < 3/10 fixed (CK L218).     (HIGGS-FS')

   Only an upper bound on Phi is needed. (Phi >= 0 holds for free when the transfer operator is positive: the
   trace of T^(2n) is at most the square of the trace of T^n. ARGUED, standard; so the one-sided form does not make
   the problem easier. It says the thermal sum is the whole defect.)

## Step R2. Rows 865 and 868 (the complete-account port of (SD-cyl)), and what they change here

READ D/library/gap-sdcyl-ca-astra.md L1-313 in full (short name SDC; row 865, a port by Codex gpt-6-astra xhigh)
and D/library/gap-sdcyl-ca-check-opus.md L1-104 in full (short name SDK; row 868, its check by Claude Opus 5.5 high:
all six statements HOLD, conditional on the account's own premises). Also READ D/library/gap-e17phys-opus.md L28
(the definition of S_ev) and D/library/gap-phys-seed.md L268-272 (Lemma Z').
Credit for the account: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

**What the two rows give (READ through; I did not re-read the account lines in this step).**
- The witness of CA-I Theorem 0 (iv), CA-I L2715-2826, on the cubic tori T_m: S_2(f, h) = zeta'^2 g_(K-s)^4 b_0 K_s^star(f, h)(1 + R),
  |R| <= 1/2, with c_K |f| |h| <= K_s^star(f, h) <= C_K |f| |h| on the class T(d; theta), d <= 1/40, and
  zeta'^2 g_(K-s)^4 >= (4/9) xbar_s^(-2), xbar_s = g^(-2) + B(s + 1) (SDC L20, L32-40; SDK L50). The constants do not
  depend on the cutoff. The observable is O(f) = sum over bare plaquettes p of f(x(p)) [1 - x_p(U)] (SDK L42:
  CA-I L208, L101-102). The account's theorem is conditional on its packages (SDK L100).
- Proposition W-phys-CA (SDC L218-240; SDK L70-77): S_ev(n_A; B) >= rho_CA^(2A/(3d)), rho_CA = c_K/(3 C_K), for spatial
  boxes with sides multiple of ell_star^CA and A = n_A a_K >= 2d. So the even gap is at most (2/(3d)) log(3 C_K/c_K)
  in physical units. This is an upper bound on a gap. It proves no decay.
- The dictionary between the outline's first-passage data (K, beta) and the complete account's data
  (g_0 in (0, g_-(g)], K = K(g_0, g), CA-I L111, L682) is unchecked (SDK L87). Step 7 below must respect this.

**Bearing 1. The witness does not obstruct the exit, and does not help it (PROVED given W-phys-CA).**
Let a seed S(T; B) <= t < 1 hold at a box B and time T to which W-phys-CA applies, A = T a_K. The even sector is a
sub-sum of the full thermal sum (READ through CK L176). So rho_CA^(2A/(3d)) <= t, that is

    A >= (3d/2) log(1/t) / log(3 C_K/c_K).

Since d <= 1/40 and c_K <= C_K, the right side is at most (3/80) log(1/t)/log 3: below 0.3 units for t = 1/5041.
A landing after the first passage has coarse spacing at least one unit. So this necessary condition is not binding.

**Bearing 2. No cutoff-uniform landing at the bare scale (PROVED given CA-I Theorem 0 (iv) as quoted, and K9).**
Fix a noise a, alpha < 1 and m > 0. Suppose the kernel (N) (L = 1) applied to the bare first-passage measures on
the tori T_m lands them with these constants for all K >= K_0. Take the tent pair (f, h_2) of SDC L173-203
(r = d/4, supports at distance at least 5d/2, both in the class). Plaquettes p != q with disjoint links are closed
paths as in K6, K9, and x_p = chi_(1/2)(U_p)/2. So |Cov(x_p, x_q)| <= lambda_(1/2)(a)^(-8) (8 alpha/(1 - alpha)) e^(-m d(p,q)).
A ball of radius r holds at most 6 (d/a_K)^4 plaquette centres (a_K <= d/8), and d(p, q) >= 5d/(2 a_K) - 2. Hence

    (2/9) b_0 c_K xbar_s^(-2) r^2  <=  S_2(f, h_2)  <=  r^2 36 (d/a_K)^8 lambda_(1/2)(a)^(-8) (8 alpha/(1 - alpha)) e^(2m) e^(-5 m d/(2 a_K)).

The left side does not depend on K. The right side tends to 0 as a_K = L^(-K) -> 0. So the supposition fails for
large K. Meaning: a soft step keeps the witness exactly (K6: the factor lambda^8), so the smeared bare theory is as
non-trivial as the bare theory; a landing must sit at a block scale that grows like L^K in bare units. The
account's steps supply that scale. This is a consistency statement, not progress on the band.

**Bearing 3. Matched locators (for Step 7).** T_m = R^4/(2 L^m Z^4) (CA-I L108, L410-412); bare sites L^(-K)(Z + 1/2)^4
(CA-I L418); first-passage data (CA-I L111, L682); the observable and the connected function (CA-I L208, L218, L731);
rectangular trace subadditivity (CA-II L140995-141056); vacuum-density premises (CA-II L141276-141347); the complex
chessboard estimate (CA-II L61205-61415). All READ through SDC and SDK here. Step 7 re-reads what it cites.
The trace inequality of Step R1 item 5 (Phi >= 0) has its complete-account form at CA-II L140995-141056 (READ through SDC L97).

## Step 6c. The vacuum constant: a correction to Step 4, and what every exact step must supply

I re-read HO L44 (TC), L160-163 (vacuum cancellation) and L255-268 (EXIT) for this step.
Clause (E2) asks that the datum (beta, W, E) is torus consistent: the constants E_X are the same on both tori for
sets of diameter below n/3, and e_m is bounded uniformly.

**Proposition VAC (the vacuum constant of an exact step; PROVED).** Let T run over T_n and T_(rho n). Let r'_T > 0 be
a density on the coarse links with integral Z_T (for example the image of a density of mass Z_T under any kernel
with integral of K(V | U) dV = 1). Suppose r'_T = exp(-E_T + beta' sum_p x_p - sum_X W_X) for a datum (beta', W, E).
Put F_T = log integral exp(beta' sum_p x_p - sum_X W_X) dV and Phi = rho^4 log Z_n - log Z_(rho n). Then
(i) E_T = F_T - log Z_T.
(ii) rho^4 E_n - E_(rho n) = [rho^4 F_n - F_(rho n)] - Phi.
(iii) For every configuration V_0: -E_T = log r'_T(V_0) - beta' sum_p x_p(V_0) + sum_X W_X(V_0).
*Proof.* Integrate the representation over V for (i). Subtract for (ii). Evaluate at V_0 for (iii). QED

**Corollary VAC2 (PROVED given Theorem O-SEED as corrected by row 850).** Let (beta', W) be torus consistent and
in a zone. Then |rho^4 F_n - F_(rho n)| <= delta_loc(n), the local part of the bound of Theorem O-SEED (Identity
PHI and Lemma TRUNC; exponentially small in n). So by (ii)

    | Phi + (rho^4 E_n - E_(rho n)) |  <=  delta_loc(n).

(a) If E satisfies (TC) with finite e_m, then |Phi| <= delta_loc(n) + 8 (rho n)^4 e_m e^(-mn/3). This is Theorem O-SEED.
(b) Conversely, if Phi is not exponentially small along the family, no datum with (E1)-(E3) exists.
(c) Given the potential part, the constants E_T are fixed by the single number log r'_T(V_0) (by (iii)).
So clause (E2) for the vacuum constants is equivalent to the conclusion of Theorem O-SEED. It is new information
only if log r'_T(V_0) is known by an independent local formula, with its absolute normalisation.

**What this does to the soft kernels of Steps 3-4 (PROVED).** For (N) and (D_a), r'_T(V) = N(a)^(-|E'|) Xi_T(a V) (4.1).
The cumulant expansion of log Xi_T(a V) - log Z_T, and every potential built from the one-link laws of rho'_T,
represents the normalised density p'_T = r'_T/Z_T. For p'_T the constant is E = F (the identity integral of p' = 1),
and Theorem O-SEED applied to p'_T says 0 = 0. For r'_T the constant is F_T - log Z_T, with log Z_T unknown.
At V_0 = 1 the number in (c) is log A_T(a), the flat-pinned partition function of Step 6.
So for a soft step:  EXIT  <=>  PIN-MIX in its potential form, and  rho^4 log A_n(a) - log A_(rho n)(a)  exponentially small.
By Theorem HL's derivative formula the second statement differs from the target Phi by
4 (rho n)^4 integral_0^a [e_n - e_(rho n)] da', which the potential form of PIN-MIX controls. So it is the target.

**Correction to Step 4.** The paragraph "What Theorem LAND does not give" says that Theorem O-SEED should survive
for the cumulant potential "with one more exponentially small term". I withdraw that sentence. The cumulant
potential has the local structure, but its vacuum constant is the unknown itself. Theorem LAND (i)-(v) stands as
stated. Its landed measure is a correct object for clustering, for reflection positivity and for any consumer
of a normalised Gibbs measure. It gives no bound on the free-energy defect, so it does not give the seed.
Step 3a already said "the constant of the output is -log Z_T itself"; this step draws the consequence.

**Which steps do supply the constant (ARGUED from Theorem STEP and Lemma HL2; not written in full).**
A step supplies log r'_T(V_0) when a path of measures joins the pinned integral to an explicit one and local
means compare between tori along the whole path. Three paths occur in this file and in row 846.
1. Strong pinning, the path in the fine coupling at fixed (a, V): d/ds log r'_T(V; s) = beta sum_p <x_p> under the
   measure pinned by (a, V) at coupling s beta; r'_T(V; 0) = 1 for (N) and (D_a). For a > 24 beta e^m the pinned
   kernels satisfy the single-link criterion for all s in [0, 1] and all V (the proof of Theorem STEP). So the
   step is computed: local terms and constants are torus consistent up to exponentially small terms. This is the
   mechanism of every Balaban-type step (there with a saddle point at fixed block field). The price is Step 5:
   in worst-case norms the output is not softer than the input.
2. Weak pinning, the path in a at V = 1: Theorem HL. It crosses the strip 0 < a <= 24 beta.
3. No pinning, the path in the coupling of the last computed action S: Identity PHI of row 846 (CK L134-140).
   For the Wilson action it reads (PROVED: d/d beta log Z_T = 6 |T| <x_p>_T and Z_T(0) = 1)

       Phi^rho(n) = 6 (rho n)^4 integral_0^beta [ <x_p>_(T_n, b) - <x_p>_(T_(rho n), b) ] db.                       (6.3)

**The crux in path form (statement; OPEN on the band).** (PATH) For the last computed action S (model case: the
Wilson action with beta in the band): the local means of the measures exp(-s S), s in [0, 1], compare between T_n
and T_(rho n) with an error whose integral over s, times (rho n)^4, is below (rho/2) log(1 + s_0). In the model
case this is (6.3) at most (rho/2) log(1 + s_0). Row 850 confirms the proved range of the lane's criteria at W = 0:
b < 2/9 (single link), b < 1/3 (line-field gauge), b < (sqrt(37) - 5)/3 = 0.3609 (stars) (CK L71). The interval
from 0.361 to the band is OPEN. A soft step does not shorten this interval (Corollary VAC2).

**Fact tests on (PATH) (ARGUED; recalled physics is GUIDE).** U(1): in the Coulomb phase the plaquette mean
converges in the size like a power (massless photon), so (6.3) is not small. Q_8 and 2T: across the freezing
coupling the two tori differ by order one on a window of width about 1/|T|, so (6.3) jumps by a constant (the
number of flat sectors enters Phi). So (PATH) on [0, beta] says: no freezing and no Coulomb phase up to beta.
It must use the continuous non-abelian group. This agrees with rows 838 and 843.

**Two side facts (kept short).**
- Lemma TS (the defect is a sum of thermal sums; PROVED given positivity of the bare transfer operator in each
  direction, the lane's Lemma A, READ through D/library/gap-phys-seed.md L268-272). With Z(t; B) = lambda_0(B)^t (1 + S(t; B)):
  0 <= rho log Z(n; B) - log Z(rho n; B) <= rho S(n; B). Telescope over the four directions:

      0 <= Phi^rho(n) <= rho^4 S(n; n^3) + rho^3 S(n; rho n . n^2) + rho^2 S(n; (rho n)^2 . n) + rho S(n; (rho n)^3).

  With Lemma Z' this is two-sided: the defect at beta is a spectral quantity at beta alone. But a bound on a
  thermal sum needs a count of states as well as a gap, and the lane obtains that count from the defect (Lemma Z').
  So Lemma TS does not remove the path.
- The flat-pinned line is reflection positive, and that gives no rate (PROVED; ARGUED as to use). In unitary
  gauge the transfer kernel between time slices is e^(-V/2) K_0 P_a e^(-V/2), K_0 the product of the one-link
  convolutions by exp(beta x) and P_a = integral over g of [product over sites of exp(a x(g_x))] R(g), R the gauge
  rotation. K_0 >= 0 and P_a >= 0 (positive character coefficients, Lemma K5), and they commute. So
  rho^4 log A_n(a) - log A_(rho n)(a) >= 0 for every a >= 0. Chessboard bounds control mixed quantities by
  homogeneous ones; here they bound correlations by the susceptibility. They do not bound the susceptibility.
- Why single-link criteria cannot see the strip (PROVED arithmetic for the Gaussian caricature). Take the real
  Gaussian with precision P = a + beta d*d on 1-forms. Its row sum is 18 beta/(a + 6 beta), below 1 only for
  a > 12 beta. Yet P^(-1) = (a - beta Delta)^(-1) (1 + (beta/a) d d*) decays exponentially for every a > 0, at the
  rate of the mass sqrt(a/beta). So between a = 0 and a of order 12 beta to 24 beta the failure of Steps 5-6 is a
  failure of one-link bookkeeping for curl-type couplings, even with typical fields. A proof in the strip needs
  blocks of side about sqrt(beta/a) or a different tool.

**Clarification of the equivalence in Step 6c (PROVED given Theorem O-SEED's local part).** Define (POT): the
normalised densities p'_T = r'_T/Z_T have data (beta', W) that are torus consistent and in a zone. This is what
"PIN-MIX in its potential form" means above. Theorem LAND derives the Dobrushin condition for p'_T from PIN-MIX.
It does not derive (POT); that needs the cumulant form with tree bounds and is OPEN to write.
Given (POT): A_T(a) = Z_T p'_T(1), and log p'_T(1) = -F_T + beta' sum_p 1 - sum_X W_X(1). The two sums cancel in the
defect up to the tails of W (TC), and the defect of F is at most delta_loc(n). So

    rho^4 log A_n(a) - log A_(rho n)(a)  =  Phi^rho(n) + O( delta_loc(n) + tails ).

Hence, for a soft step: EXIT for r'_T  <=>  (POT) and Phi^rho(n) exponentially small. The second clause is the
conclusion that EXIT was meant to give. The route "soft step, then Theorem HO" is therefore circular for the seed.

## Step 7. What each step needs from the Sussman-Alpoge account (lines read by me in this step)

Sources at /Users/jonreilly/ym4d-lead/sa (revision 31a47c543775 as recorded by rows 848 and 865; hashes not
recomputed here): CA-I = theorem_0_complete_account_raw_I.tex, CA-II = theorem_0_complete_account_raw_II.tex.
The account is by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of its text. The estimates it
quotes from Balaban's papers are Balaban's. I cite the complete account only (rule of Step 1b). I did not read
the outline in this step. Statements below are the account's; it marks several of them as conditional.

**7.1 What I read.**

| Locator (READ) | Content |
|---|---|
| CA-I L98-112 | tr 1 = 1; L odd; L_0 "is bound once, by there exists, and is never given a value"; T_m of side 2 L^m; K steps, bare spacing L^(-K); K(g_0, g) the first-passage number of steps |
| CA-I L406-420 | T_m = R^4/(2 L^m Z^4); bare sites L^(-K)(Z + 1/2)^4; 2 L^(m+K) bare sites per side |
| CA-I L678-686 | reference window g_-(g) <= g' <= g; 0 < g_0 <= g_-(g); K := K(g_0, g); m >= m_T(g_-(g)) |
| CA-I L788-800 | block lattices T^(k) = L^(k-K)(Z + 1/2)^4; every site of T^(k) is a site of T^(k-1) (L odd) |
| CA-I L2536-2553 | clause (0): g_k in (0, g), a subset of (0, gamma_H], for k <= K; g_K in [g_-(g), g); bounds on x_i - x_j |
| CA-I L2555-2561 | clause (i) is Balaban's ultraviolet stability theorem as used; "No statement about the laws of the block variables is a clause of the present theorem"; their proofs are outstanding |
| CA-I L2562-2574 | (i-a): rho_k is a sum over histories of large-field operations applied to characteristic functions, times exp of -A(g_k^(-2), U_k) plus localised terms; each term gauge invariant, analytic on a domain, bounded by const e^(-kappa d_j(X)) |
| CA-I L2575-2581 | (i-b): chi_k e^(-g_k^(-2) A(U_k) - E_- N_k) dV_k <= rho_k dV_k and integral rho_k dV_k <= e^(E_+ N_k), E_+ <= C (1 + log g_k^(-2)) |
| CA-I L2582 | (i-c): integral rho_k dV_k = integral rho_0 dU |
| CA-I L2583-2595 | (i-d): exact insertion; V_(K-s) = M^(K-s) U with M the block-averaging map; "it asserts nothing about the values of the laws of the block variables" |
| CA-I L2715-2800 | clause (iv): the witness (3.1:eq-main-3), the sandwich for K_s^star, the bound (2/9) b_0 c_K |f_1| |f_2| (g^(-2) + B(s+1))^(-2) <= S_2, the volume transfer with C_T(g) d^2 |
| CA-I L3352-3392 | Remark "block-law statements": the block law nu^B_(K,s) = rho_(K-s) dV/integral rho_0; statement (a) is not a clause; bounds on the block laws are not part of Theorem 0 |
| CA-II L140995-141036 | Lemma trace sub-additivity: 0 <= Z_(k n)(W) <= Z_n(W)^(k^4) for mirror-periodic W and even cell counts; its proof rests on the positivity of the Wilson transfer operator (Osterwalder-Seiler) |
| CA-II L141276-141420 | Lemma torus-independence of the vacuum-energy density: under hypotheses (a)-(c), E_m = sum over j < K of three parts: exactly extensive counts, and local terms of Balaban's format "evaluated at the trivial configuration U = 1" with bounds e^(-kappa d(X)); non-wrapping terms agree between tori; conclusion |E_m/(2L^m)^4 - E_m'/(2L^m')^4| <= deltabar_vac, a constant of L and the parameters only |
| CA-II L61205-61232 | Lemma chessboard estimate for complex cell observables, from reflection positivity in antipodal pairs of link planes |

**7.2 The map.**

| Step here | What it needs from the account | Supplied? |
|---|---|---|
| 3a: K1-K3, Proposition FREE, applied to rho_K | rho_K >= 0, integrable, mass Z_bare | Yes: (i-b), (i-c), CA-I L2575-2582. Coarse sites are fine sites (CA-I L788-800), so straight paths exist |
| 3a: K1 (ii)-(iii), gauge and lattice covariance of rho_K | covariance of the block-averaging map M | Definition 1.5:def-block-average (CA-I L788 on); I read only its first lines. Not checked here |
| 3b: K5-K7 on the bare measure, block L^(K+j) | nothing | - |
| 3b: K8 on the bare measure | reflection positivity of the bare Wilson measure | Yes: used at CA-II L61205-61232 and L141034-141036 |
| 3b: K8 on rho_K (Theorem LAND (v)) | reflection positivity of the block law | No. No block-law statement is a clause (CA-I L2555-2561, L3352-3360) |
| 4: PIN-MIX, (POT) | decay of block-holonomy covariances under pinned block laws | No. Same lines. The account makes no statement of this kind at any scale |
| 5, 6: Theorems STEP, HL, HL2, HL3 | none (model case: Wilson action) | For rho_K they would need global mixed Lipschitz bounds on log rho_K. (i-a) gives analytic local terms on domains and labels, not this |
| 6c: Proposition VAC, item 1 (computed steps) | the vacuum constants of the K account steps as local torus-consistent terms | Yes, conditionally: CA-II L141276-141386, hypotheses (a)-(c). The constants are the format terms at U = 1, as in VAC (iii) |
| 6c: (PATH) | the defect of the remaining level-K integral | No. (i-b) bounds its logarithm only by E_- N_K and E_+ N_K (CA-I L2575-2581) |
| 6c: Lemma TS, Phi >= 0 | positivity of the transfer operator | Yes: CA-II L140995-141036 (even cell counts) |
| R2: Bearing 2 | the witness with constants independent of K | Yes, as clause (iv), CA-I L2756-2790, conditional as the account states |

**7.3 Consequences (ARGUED from the lines above, unless marked).**
1. The account's K steps are computed steps in the sense of Step 6c: their vacuum energy is a sum of local
   terms fixed at the trivial configuration. The lemma states only the uniform constant deltabar_vac. Its
   hypothesis (c) puts the wrapping threshold at d_(j+1)(X) >= 2 L^min(m,m') L^(K-j-1)/(4M) - 2 (CA-II L141366-141370).
   So the same proof gives a difference of densities that decays exponentially in L^min(m,m')/M. This is the
   clause (E2) for the account's own vacuum terms, conditional on (a)-(c). I did not write this variant out.
2. What the account does not supply is the defect of the remaining integral at level K. Its action has coupling
   g_K in [g_-(g), g) with g <= gamma_H: weak coupling on a unit lattice of side 2 L^m >= 2 L^11 M. The whole
   infrared problem sits there. (I did not read the definition of the normalisation in CA-II Notation
   8.22:not-partition-sources-cells; the split "vacuum terms plus remaining integral" is READ through hypothesis (a).)
3. The reference coupling g is at most gamma_H, and the book's constant L_0 is never given a value (CA-I L103-106).
   So the number of weak steps (G1) from first passage to the band has no explicit bound in the account.
   "Finitely many steps past first passage" needs explicit constants that the account does not state.
4. The dictionary between the lane's first-passage data (K, beta) and the account's (g_0, K(g_0, g)) is unchecked
   (SDK L87). Nothing in this file depends on it; the model statements are about the Wilson action.

## Step 8. Fact tests on the final argument, answers to the brief, summary

**8.1 Fact tests.**

| Test | Proved statements of this file | Open statements (PIN-MIX, (POT), (PATH)) |
|---|---|---|
| U(1), Coulomb phase | K1-K9, FREE, LAND (as an implication), VAC, TS and the Higgs-line identity hold word for word. STEP, HL2, HL3 hold with the circle constants (Lemma V-inf holds on S^1). None of them asserts a gap in the band, so none is contradicted | Must fail. PIN-MIX implies exponential clustering of loop characters (K9, PROVED implication); a massless photon forbids it (recalled, GUIDE; row 786 proves a related non-summability, not this one). (PATH): power-law finite-size terms make (6.3) of order one (ARGUED) |
| Q_8 and 2T | The kernel lemmas restrict to finite subgroups (Step 3c). Corollary V1 and Theorem V do not: they use the sphere S^3. So STEP, HL2, HL3 in this form use the continuous group, but only at strong coupling or strong pinning | Must fail above freezing. (PATH): (6.3) jumps by a constant across the freezing coupling (ARGUED). PIN-MIX: a Dobrushin landing makes twisted mass ratios tend to 1, a frozen phase suppresses them (ARGUED, GUIDE). A proof of (PATH) must use what the finite groups lack; this file does not find it |
| Worst-case caps | STEP and HL2 take a supremum over pinning fields. They stop at beta < 0.0384 (landing) and at a > 24 beta (comparison), far below 2/3, 0.775 and 1.0109. Consistent | PIN-MIX takes a supremum over coarse pinning fields of strength a per block, not over fine boundary values. Rows 836 and 839 do not exclude it (ARGUED). (PATH) takes no supremum |
| (AN1) | not used | not used |
| The band and the real object | The model statements are for the Wilson action. Step 7 says what the account supplies for the first-passage density and what it does not | (PATH) is stated for the last computed action; in the model case for beta_W in 2.3 to 2.6 |

**8.2 Answers to the brief's questions.**
1. Which block transformation has a chance? Every exact map with a probability kernel keeps the masses. Soft
   kernels (noise, noisy straight decimation) also give the size for free: one step lands any input, U(1)
   included, at a per-link Lipschitz constant a of our choice (Proposition FREE). So the per-link number 0.05
   at beta = 1/4 is not the crux. Noisy straight decimation keeps loops, truncated loop correlations, twisted
   masses and reflection positivity (K6-K8). Bond moving is not exact. No kernel removes the two real loads:
   locality of the output (PIN-MIX, (POT)) and its vacuum constant (Proposition VAC).
2. What is monotone or controlled? I found no quantity that is monotone along exact steps and not group blind.
   The exact invariants are group blind. The controlled quantity for locality is the weighted pinned block
   susceptibility X_m(L, a). For the seed it is the path integral (6.3). U(1) cannot fake either: K9 turns a
   uniform landing into exponential clustering of loops, and (6.3) sees power-law finite-size terms.
3. The crux lemma, and where the attempt stops. For locality: PIN-MIX(L, a, alpha, m) (Step 4). PROVED by pinning
   at every coupling when a > 24 beta e^m (Theorem STEP); the output then lands only for beta < 0.0384. For the
   seed: the soft route is circular (Corollary VAC2 and its clarification), so the crux is (PATH) (Step 6c):
   torus comparison of local means along a path of measures from a trivial point to the last computed action.
   For the Wilson action it is proved for b < 0.3609 by the lane's criteria (row 850) and for a > 24 beta on
   the Higgs line (Lemma HL2). It is OPEN from 0.361 to the band. I found no inequality for that interval
   that avoids a supremum over environments and is not shared by U(1). The attempt stops there.
4. Which statements of the account each step needs: Step 7, with the lines read.

**8.3 Statements of this file by mark.** All proofs are author proofs by Claude Fable 5.2. None is checked.
No numeric run was made.

PROVED (given the named inputs: Theorem V and Corollary V1 of VL, check row 790; Lemma DC* and Lemma BOX of HO,
checked line by line by Codex astra xhigh at row 850; the account's clause (iv) where stated):
- Lemmas K1-K4, K4', Proposition FREE and its U(1) form (Steps 3a, 4).
- Lemmas K5-K8, Corollary K9 (Step 3b). Theorem LAND (i)-(v) (Step 4).
- Lemma V-inf, Theorem STEP, the arithmetic of the overlap beta < 0.0384 (Step 5). The Gaussian statement (i) of Step 5.
- Theorem HL (the Higgs-line identity), Lemma HL2, Corollary HL3 (Step 6).
- Proposition VAC, Corollary VAC2 and the clarification; identity (6.3); Lemma TS; positivity on the flat-pinned
  line; the Gaussian caricature of the strip (Step 6c).
- Bearing 1 (given W-phys-CA of rows 865, 868) and Bearing 2 (given clause (iv) of the account) (Step R2).

ARGUED: the reading of the candidate table (Step 3c); the sharp-constant estimate "about 0.1" (Step 5); the
computed-step statement for strong pinning with general V (Step 6c, item 1); the fact tests on the open
statements (8.1); the consequences 7.3. GUIDE: recalled physics of the Coulomb phase, of frozen finite groups
and of the Higgs crossover.

WITHDRAWN: the sentence of Step 4 that Theorem O-SEED "should survive" for the cumulant potential (see Step 6c).
CORRECTED from row 850: "the first-passage density lies in no zone" (Step R1, item 1); the scope of the 0.775 cap.

OPEN:
- PIN-MIX at order one, and its potential form (POT) with tree bounds for the cumulants of block holonomies.
- (PATH) on the interval from 0.361 to the band; in the Higgs-line form, the strip 2/9 <= beta, 0 < a <= 24 beta.
- A computed block step in the band whose output is softer than its input in a norm that the zone accepts.
  Step 5 shows that worst-case norms do not decrease under strongly pinned noise steps.
- For the account: the defect of the remaining level-K integral; explicit constants for the steps between
  first passage and the band; any statement on block laws (Step 7).

RESULT: PARTIAL, with one negative structural result. PROVED (author proofs, unchecked): an exact soft block step gives the zone's per-link size for free for any input and for U(1) (Proposition FREE), so the 0.05 target is not the crux; locality of the landed action is the pinned block mixing lemma PIN-MIX, proved by pinning at every coupling only for noise a > 6 beta + 18 beta e^m (Theorem STEP), which lands only beta < 0.0384; the vacuum constant of any exact step equals F_T - log Z_T (Proposition VAC), so "soft step then Theorem HO" is circular for the seed and Step 4's optimistic sentence is withdrawn; the Higgs-line identity and (6.3) reduce the seed to torus comparison of local means along a path, proved for b < 0.3609 and for a > 24 beta. OPEN (the crux, stated exactly as (PATH) and PIN-MIX): that comparison on the interval from 0.361 to the band beta_W 2.3-2.6, where no inequality was found that avoids a supremum over environments and fails for U(1); the complete account supplies exact masses and, conditionally, torus-consistent vacuum terms for its own steps (CA-II L141276-141386), but no block-law statement and no bound on the defect of the remaining level-K integral.
