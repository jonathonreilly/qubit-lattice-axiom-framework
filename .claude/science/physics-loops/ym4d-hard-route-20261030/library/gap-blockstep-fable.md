# Row 1340: one verified block step for Proposition CH

Lane: four-dimensional SU(2) Yang-Mills mass gap, in the sense of Jaffe and Witten.
Row: FINISH 1340. Author of this file: Claude Fable 5.2 (worker, max effort). Date: 2026-11-21 (UTC).

The problem (the brief). Prove a block-step theorem for four-dimensional SU(2) lattice gauge theory at an effective coupling of order one. It must meet two conditions.

- Its only unproved hypothesis is a local finite statement about one block. The statement must be small enough to compute exactly and check in Lean: about 10^15 exact operations on one machine, or a certificate of that size.
- Repeated steps satisfy the hypotheses of Proposition CH (Section 6.1 of `library/gap-shrink-box-fable.md`, row 1332, as corrected by its check, row 1335).

Status of this file: written in steps. Author only; checked by no one. The last line is the result line.

Labels: PROVED, ARGUED, GUIDE, OPEN. "PROVED on file" means: proved in the named row and checked as that row says; I did not re-check those rows. "PROVED here" means: proved in this file, by hand, unchecked.

Rule in force: GOAL.md, section "Computation only as a formal proof" (owner, 2026-11-20), read on the branch at 6cb02d5ca. An exact computation checked by the Lean kernel may be a proof step. Until it is checked it is OPEN, with the computation specified. Monte Carlo and unchecked floating point may only guide.

## 0. Outcome in short

- Not solved. No block step at a coupling of order one is verified here, and I can specify no computation inside the budget that would verify one. Nothing in the chain is disproved.
- The step now exists as a theorem with one stated hypothesis. Theorem TL (3.3): apply one soft step of row 861 to the whole coupling ray s -> exp(-s S). If the measures of the input with one unit pin on every link have a comparison property (CP), and the output is soft (OUT), then the defect of the two masses is exponentially small in the side, with explicit constants. The proof has no potential, no cumulant expansion and no vacuum constant. This is the normalization estimate that row 861 left unwritten and check 877 asked for.
- The hypothesis has a one-block form. Lemma DC-B and Proposition BL (5.2): (CP) follows from chord coupling numbers for the conditional law of the links of one block, uniform in the pins of the block and in its surroundings. This is (B-pin). With it, Theorem BS (5.2) gives the seed at a coupling beta from one statement about one block.
- For a block of one link, (B-pin) is the hand criterion of rows 785 and 861. It reaches no coupling outside the known zone: beta < 2/9, or beta < 0.0384 with strong pins (3.5).
- Repeated steps fit Proposition CH for the maps and for (END): the classes are pairs of rays, the maps keep both masses, and the landed class has (END) (4.1 to 4.3). (BASE) is not met, and it is not a finite statement: the classes hold explicit Gibbs data, and the account gives no such form and no block-law statement for its first-passage densities (4.6).
- Size (5.3): for the smallest cube (B-pin) is a supremum over at least 240 real dimensions, of a quantity that is itself an integral over 96 dimensions. At the window the cube needs a side of about 3 to 10 (GUIDE). The hand methods for such suprema stop below beta = 1.02. No floor is proved.
- Two limits of the step (4.4, 5.4, 5.5). A chain of noise steps is one noise step with a weaker pin (Lemma COMP, PROVED). A noise step that lands at a coupling of order one must use pins that are weak against the action: below about 0.8 at beta = 2.3, against a staple field of up to 13.8 (Lemma GAUSS, PROVED for the quadratic model; guide run, GUIDE). So at a fixed coupling the step does not shrink the finite statement below the direct comparison along the coupling ray (Lemma WEAK), and the block statement is larger than the in-law statement (KER), because it carries a supremum.
- This is a bounded search. It proves no impossibility. Section 7.3 lists what would change the decision.

## 1. The target in exact form, and what is on file

Read for this file, in full: FINISH rows 1326, 1331, 1332, 1335, 1340; GOAL.md; `library/gap-shrink-box-fable.md` (row 1332); `library/gap-shrink-box-check-astra.md` (row 1335); `library/gap-exit-max.md` (row 861). Read in part: `library/gap-handoff-opus.md` (row 846) lines 40 to 200; `library/gap-exit-check-astra.md` (row 877) lines 194 to 262 and 373 to 427; `library/gap-finishline-opus.md` (row 837) Sections 1 and 2.1; `library/gap-mid-max.md` (row 708) Sections 1 to 4.2; `library/gap-council-rg-fable.md` (row 1128) Step 1; `library/gap-vmf-lip.md` (row 785) lines 205 to 240; `library/gap-phys-seed.md` (row 720) lines 262 to 275; `library/gap-thermpin-opus.md` (row 923) lines 93 to 112; `parts/gap.md`, the state of attack, the route registry and the test table; the RESULT lines of rows 691, 693, 785, 836, 840, 841, 846, 849, 850, 857, 861, 877, 970, 977, 979, 1072. I did not read the primary text of the account of Sussman and Alpoge, of Balaban, or of any published paper. Statements about them come from those rows.

**1.1 Proposition CH (PROVED on file: row 1332, 6.1; check 1335, HOLDS).** Fix two tori T_ell and T_(L ell). Let C_0, ..., C_N be sets. Every element nu of every C_k carries two positive numbers Z_nu(T_ell) and Z_nu(T_(L ell)). R_k maps C_k into C_(k+1) and keeps both numbers. (BASE): there is K_0 such that for every first-passage datum d with K >= K_0 some nu_d in C_0 has the two masses of d. (END): every nu in C_N has L^4 log Z_nu(T_ell) - log Z_nu(T_(L ell)) <= phi_*. Then Phi(d) <= phi_* for every such d. With Lemma FL (row 837; check 848) this is (SEED-FP) at a larger size. (UNIV-K) is not used.

Row 1332, 6.5, names the first failing step: "One block step at an effective coupling of order one, with a class on each side. Before that: (BASE) with numbers." This file attacks that step.

**1.2 Objects (definitions on file; rows 785, 846, 861).**

- SU(2) is the unit sphere S^3 of R^4 (quaternions). <A, B> is the Euclidean inner product, <A, B> = (1/2) Re tr(A B^dagger). The chord distance is abs(A - B). x_p(U) = (1/2) tr U_p = <U_p, 1>.
- T_n is the periodic lattice with n^4 sites, E(T) its set of links, Omega_T = (S^3)^(E(T)). rho >= 2 is an integer. In Proposition CH, rho = L.
- A datum (beta, W, E) on a torus T gives the density rho_T = exp(-E_T - S_T) against Haar measure, with the action S_T = -beta sum_p x_p + sum_X W_X. Each W_X is a continuous function of the links of the finite set X. This is the class of row 846, 2.1, with the sign of the action made explicit. A local term Phi_X is -beta x_p or W_X. The datum has range R if W_X = 0 when diam X > R. It is consistent on {T_n, T_(rho n)} if it satisfies (TC) of row 846: sets of diameter below n/3 carry the same functions and the same constants on both tori, and the family is translation covariant.
- For a function f on Omega_T, delta_l(f) is its chord Lipschitz constant in the link l, and Delta(f) is the sum of delta_l(f) over l. The norms w_0, w_m, e_m are those of row 846, 2.2.
- d_Lip(mu, mu') is the supremum of abs(mu(psi) - mu'(psi)) over chord-1-Lipschitz psi on S^3.
- d is the l^infinity distance of link midpoints, circular on T. D_R is the set of links of T_n with some midpoint coordinate at circular distance at most R + 1 from n - 1/2 (the seam strip of Lemma BOX).
- Phi^rho(n) = rho^4 log(integral of rho_(T_n)) - log(integral of rho_(T_(rho n))) is the defect.

**1.3 Statements PROVED on file that this file uses.**

- (V1) Corollary V1 (row 785, Codex gpt-6-astra; check 790). For the law mu_F on S^3 with density proportional to exp(<F, h>): d_Lip(mu_F, mu_F') <= abs(F - F')/4.
- (DC*) Lemma DC* (row 846, Claude Opus 5.5; check 850, Codex gpt-6-astra: HOLDS). Kernels gamma_i on (S^3)^Lambda with influence numbers C_ij in the sense of (8) of row 785, and weighted row sums sum_j C_ij e^(m d(i,j)) <= alpha < 1 for i outside a set D. mu_1 has the kernels gamma_i off D. mu_2 is any law whose one-link conditional laws off D are within b_i of gamma_i in d_Lip. Then for f with delta_j(f) = 0 on D, and G = sum over n of C^n (C restricted off D):
  abs(mu_1(f) - mu_2(f)) <= sum over i not in D of delta_i(f) [2 sum_(j in D) (G C)_ij + sum_(j not in D) G_ij b_j].
  Its proof (step (iv) there) gives the weighted form: if b_j <= b e^(-m d(j, Y)), the bracket is at most [2 alpha e^(-m d(i, D)) + b e^(-m d(i, Y))]/(1 - alpha).
- (BOX) Lemma BOX (row 846; check 850: HOLDS; row 861, Step R1, reads the check: "Its proof uses only the range of the kernels, (TC) and the tower property"). For a consistent datum of range R, 1 <= R < n/3: the image under reduction modulo n of the marginal of mu_(T_(rho n)) on the links of the box Q = {0, ..., n-1}^4 has the same one-link conditional law as mu_(T_n) at every link outside D_R. Row 861 uses it with an added one-link term (check 877: HOLDS).
- (PHI) Identity PHI and the vacuum cancellation (row 846, 4.4; check 850: HOLD). For a consistent datum of range R < n/3, with F_T(s) = log of the integral of exp(-s S_T): rho^4 F_(T_n)(1) - F_(T_(rho n))(1) = (rho n)^4 times the integral over s in [0, 1] of e_(rho n)(s) - e_n(s). Here e_T(s) is the sum, over the orbit types of local terms, of the mean of Phi_(X_0) under mu_(s,T), the probability with density proportional to exp(-s S_T). And abs(rho^4 E_(T_n) - E_(T_(rho n))) <= 8 (rho n)^4 e^(-m n/3) e_m.
- (Z') Lemma Z' (row 720, Claude Fable 5.2; check 727): log(1 + S(T_0; (rho T_0)^3)) <= (2/rho) Phi_rho(T_0) for the bare Wilson masses. Lemma FL (row 837; check 848) carries (SEED-L) to (SEED-FP).
- (K) Row 861 (Claude Fable 5.2; check 877, Codex gpt-6-astra). Soft kernels: k_a(v | u) = exp(a <v, u>)/N(a) for unit u, N(r) the integral of exp(r <h, e>) over S^3. Kernel (N): K_a(V | U) = product over links l of k_a(V_l | U_l). Lemma K1: the integral of K_a(V | U) over V is 1, so the image of a density has the same mass. Lemma K2: the logarithm of the image is a-Lipschitz in every link, for every input. Theorem STEP: for the Wilson action the measures pinned by unit fields of strength a satisfy the one-link criterion when a > 6 beta + 18 beta e^m. Proposition VAC and check 877: a potential for the normalized image gives no bound on the defect.
- (W) Theorem W (row 691, Claude Fable 5.2; check 693, Claude Opus 5.5): a block form of the uniqueness criterion of Dobrushin and Shlosman, rebuilt in the lane. Its hypothesis (W) at (R, delta) is a statement about the cube of side R with a supremum over boundary values.

**1.4 What was missing (READ, check 877, `library/gap-exit-check-astra.md` lines 234 to 236 and 392 to 394).** "This preserves the useful warning: normalized softening plus HO alone cannot prove the seed. It does not show every 'soft step then HO' proof is circular. A separate normalization estimate could supply the missing input." And on Theorem LAND of row 861: "The theorem still proves neither POT nor the vacuum-consistency clause of EXIT. Real covariance decay is not, without another argument, a convergent complex cumulant expansion with the required interaction norm." Row 861, Step 6c item 1, argues a computed step for strong pinning and says "not written in full". Row 1332, 6.3: "No one has stated such a certificate." So before this file the block step of Proposition CH did not exist as a theorem with a stated hypothesis.

## 2. How best to attack it

**2.1 Lemma NRM (an END class must tie the two masses together; PROVED here).** Let C be a set whose elements carry two positive numbers (z_1, z_2). Suppose that with each element C contains an element with the numbers (c z_1, z_2), for every c > 0. Then (END) fails on C for every phi_*.

Proof. L^4 log(c z_1) - log z_2 tends to infinity with c. QED

Consequence (PROVED as logic). A class that is defined only by properties of the normalized laws on the two tori cannot be an END class. Examples of such properties: a Dobrushin condition, a decay of correlations, a zone condition for the normalized density. This is the counterexample of check 877 (the constant densities exp(K n^4)) in the words of Proposition CH. So every class of a chain must carry an anchor: a point where the two densities are known, and a path from the anchor to the density along which the two tori are compared. Section 3 uses the coupling ray s -> exp(-s S_T), anchored at s = 0.

**2.2 What a block step can be (ARGUED, from rows 861 and 1128).**

- (a) An exact step: a probability kernel from fine fields to coarse fields. It keeps both masses (Lemma K1). Its whole load is the conditional law of the fine field given the coarse field, the pinned measure (row 861, Step 3c, point 2). A statement about one block is then a statement about pinned measures on one block.
- (b) A comparison step (bond moving, Migdal and Kadanoff): it bounds one mass from one side. Proposition CH needs both masses, with an error of order one on tori of any size. Row 861, Step 3c, and row 998 (route RG, retired) record why this fails.
- (c) A step on torus data alone (restrict the family Z(n) to multiples of the block): it keeps masses and needs no bound, and it has no class. The engine (Theorems S, SH) is its finite-size criterion. It is in-law: it reads one model on one pair of tori.

A local statement about one block cannot know the measure outside the block. So it is a statement for every environment of the block (boundary values, pins), or for a named family of environments. This is the point where the caps of rows 836, 839 and 857 bind: they cap families of worst-case majorants for small blocks.

**2.3 Decision (ARGUED).** I take kind (a) with soft kernels, because row 861 proved that they keep masses, symmetry and size for every input, and because their pinned measures are explicit when the input is explicit. The work is in four parts.

1. Prove the step in a form that carries the anchor of 2.1, with a real-variable hypothesis and no cumulant expansion (Section 3). This is the theorem that row 861 and check 877 leave open.
2. Put repeated steps in the form of Proposition CH (Section 4).
3. Write the hypothesis as a local finite statement, and find its size and cost (Section 5).
4. Test the result against the lane's fact tests (Section 6), then decide (Section 7).

## 3. The block step: a soft step computed along the coupling ray

**3.1 Setting.** Fix integers rho >= 2 and n, and a consistent datum (beta, W, E) of range R >= 1 on {T_n, T_(rho n)}, with beta >= 0. Fix a noise a > 0 and the kernel (N) of row 861. A pin field is an element V of Omega_T: one unit quaternion on every link. For T in {T_n, T_(rho n)}, s in [0, 1] and a pin field V put

- mu^T_(s,V)(dU) = exp(a sum_l <V_l, U_l> - s S_T(U)) dU / normalization. This is the frozen-pin family P(a). For W = 0 and V = 1 on every link it is the fixed-length SU(2) Higgs model in unitary gauge at (s beta, a) (row 861, Step 6).
- r^T_s(V) = integral of K_a(V | U) exp(-s S_T(U)) dU, the image of the density exp(-s S_T) under the kernel. nu^T_s is the probability with density proportional to r^T_s (the output law at the coupling s).
- mu_(s,T) is the probability with density proportional to exp(-s S_T) (no pins).

The family s -> exp(-s S_T) is the coupling ray. Its anchor is s = 0, where the density is 1 on both tori.

**Lemma RAY (exact identities; PROVED here).** For every T, s and V:

- (i) The integral of r^T_s over V equals the integral of exp(-s S_T). And r^T_0 = 1.
- (ii) (Tower.) For bounded measurable f on Omega_T: mu_(s,T)(f) = integral of nu^T_s(dV) mu^T_(s,V)(f).
- (iii) -d/ds log r^T_s(V) = mu^T_(s,V)(S_T).
- (iv) r^T_s is smooth and strictly positive. For a unit tangent vector xi at V_c: d_xi log r^T_s(V) = a <xi, mu^T_(s,V)(U_c)>, with mu(U_c) the mean vector in R^4.

Proof. (i) The integral of K_a(V | U) over V is 1 (Lemma K1). Also k_a(v | u) = k_a(u | v) and the integral of exp(a <v, u>) over u is N(a), so r_0 = 1. (ii) The joint density K_a(V | U) exp(-s S_T(U)) has the U-marginal mu_(s,T), the V-marginal nu^T_s, and the conditional law mu^T_(s,V) of U given V (the factors N(a) do not depend on U). (iii), (iv): differentiate under the integral; the integrands are bounded on a compact space. QED

Items (i) to (iii) say: the output of the step on the whole ray is again a ray with the same masses, and the derivative of its logarithm along the ray is a pinned mean of the action. Row 861, Step 6c item 1, has (iii) for the Wilson action. The constant E_T is never touched.

**Lemma PV2 (PROVED here; the argument is the second leg of Lemma PV of row 846, for a general base measure).** Let mu be a probability on S^3 and Delta a bounded measurable function. Let mu' have density proportional to e^Delta with respect to mu. Then d_Lip(mu, mu') <= osc(Delta)/2.

Proof. Let mu_t have density proportional to e^(t Delta). Let psi be chord-1-Lipschitz with midrange 0, so abs(psi) <= 1. Then d/dt mu_t(psi) = Cov_t(psi, Delta), at most Var(psi)^(1/2) Var(Delta)^(1/2) <= osc(Delta)/2. Integrate over t in [0, 1]. QED

**3.2 The hypothesis.** Let E_Q be the set of links (y, y + e_mu) of T_(rho n) with y in the box Q = {0, ..., n-1}^4, and pi the reduction modulo n from E_Q onto E(T_n). For a configuration or a pin field X on T_(rho n), its box field Xbar on T_n is Xbar_(pi(l)) = X_l, l in E_Q. For an integer r >= R, D_r is the seam strip of width r (1.2).

(CP)(a; Gamma, m, tau, r), the comparison property of the frozen-pin family. Gamma_ij >= 0 are numbers for all pairs of links of T_n (i = j included). Put gamma = sup over i of the sum over j != i of Gamma_ij e^(m d(i,j)), and gammabar = sup over i of the sum over all j of Gamma_ij e^(m d(i,j)) (so gamma <= gammabar). m > 0, tau >= 0, and r >= R is an integer with n > 2(R + r) + 3.

- (CP1) (One pin moved, on T_n.) For every s in [0, 1], all pin fields V, V' on T_n that differ only at one link j, and every f on Omega_(T_n) with finite seminorms:
  abs( mu^(T_n)_(s,V)(f) - mu^(T_n)_(s,V')(f) ) <= a sum over i of delta_i(f) Gamma_ij abs(V_j - V'_j).
- (CP2) (The two tori.) For every s in [0, 1], every pin field V on T_(rho n) with box field Vbar, and every f on Omega_(T_n) with finite seminorms:
  abs( mu^(T_(rho n))_(s,V)(U -> f(Ubar)) - mu^(T_n)_(s,Vbar)(f) ) <= tau sum over i of delta_i(f) e^(-m d(i, D_r)).

(OUT)(a; gamma): alpha' := (pi/2) a^2 gamma < 1.

(CP) compares members of one explicit family: the action of the datum, with one unit pin of strength a on every link. (CP1) moves one pin. (CP2) changes the torus. It has no cumulants, no complex fields, no potential and no conditioning. (OUT) says that the output is soft enough.

**3.3 Theorem TL (two-level comparison; PROVED here given (DC*), (PHI) and Lemma PV2).** Assume (CP)(a; Gamma, m, tau, r) and (OUT)(a; gamma). Put d_n = n/2 - R - r - 3/2 and

K = tau [ 1 + (pi/2) a^2 gammabar/(1 - alpha') ].

Then for every s in [0, 1]

abs( e_(rho n)(s) - e_n(s) ) <= K (24 beta + 4 w_0) e^(-m d_n),

and

abs( Phi^rho(n) ) <= (rho n)^4 [ K (24 beta + 4 w_0) e^(-m d_n) + 8 e_m e^(-m n/3) ].

Proof. Fix s. Write Phi_X for a local term of the datum.

Step 1 (the output law is a Dobrushin measure). Let gamma_c(. | V) be the one-link conditional law of nu^(T_n)_s at the link c. Its density is proportional to v -> r^(T_n)_s(v, V_(not c)). Let V, V' differ only at k != c. Then

d_Lip( gamma_c(. | V), gamma_c(. | V') ) <= (pi/2) a^2 Gamma_ck abs(V_k - V'_k).

Indeed, put Delta(v) = log r_s(v, V'_(not c)) - log r_s(v, V_(not c)). By Lemma PV2 the distance is at most osc(Delta)/2, and osc(Delta) <= pi sup abs(grad Delta) (the geodesic diameter of S^3 is pi). By Lemma RAY (iv), d_xi Delta(v) = a <xi, m' - m>, with m and m' the means of U_c under the measures pinned by (v, V'_(not c)) and (v, V_(not c)). These pin fields differ only at k. (CP1) with f = <xi, U_c> gives abs(<xi, m' - m>) <= a Gamma_ck abs(V_k - V'_k). So the kernels gamma_c have influence numbers C'_ck = (pi/2) a^2 Gamma_ck in the sense of (8) of row 785, and by (OUT) their weighted row sums are at most alpha' < 1.

Step 2 (the kernels of the two output laws agree off the seam, up to a small error). Let nutilde_s be the law of the box field Vbar under nu^(T_(rho n))_s. For every link c of T_n, nutilde_s-almost surely:

d_Lip( nutilde_s(V_c in . | V_(not c)), gamma_c(. | V_(not c)) ) <= b e^(-m d(c, D_r)),   b = (pi/2) a tau.

Indeed, let ctilde be the link of E_Q over c. Under nu^(T_(rho n))_s the conditional law of V_ctilde given all other links has density proportional to v -> r^(T_(rho n))_s(v, V_(not ctilde)). Fix such a V. Put Delta(v) = log r^(T_(rho n))_s(v, V_(not ctilde)) - log r^(T_n)_s(v, Vbar_(not c)). By Lemma RAY (iv), d_xi Delta(v) is a times the difference of the means of <xi, U_ctilde> and <xi, U_c> under two pinned measures whose pin fields agree on the box. (CP2) with f = <xi, U_c> gives abs(d_xi Delta) <= a tau e^(-m d(c, D_r)). So osc(Delta) <= pi a tau e^(-m d(c, D_r)), and Lemma PV2 gives the bound for this V. The conditional law of V_c under nutilde_s, given the other links of T_n, is a mixture of such laws over the pin field outside the box (tower property), and d_Lip is convex.

Step 3 (pinned means are quasi-local functions of the pin field). For a local term Phi_X on T_n put g_X(V) = mu^(T_n)_(s,V)(Phi_X). By (CP1) with f = Phi_X, for every link j: delta_j(g_X) <= a sum over i in X of delta_i(Phi_X) Gamma_ij. Hence, for every set D of links,

sum over j of delta_j(g_X) e^(-m d(j, D)) <= a gammabar sum over i in X of delta_i(Phi_X) e^(-m d(i, D)),

because e^(-m d(j, D)) <= e^(m d(i,j)) e^(-m d(i, D)) and the sum over j of Gamma_ij e^(m d(i,j)) is at most gammabar.

Step 4 (one local term). Let X have diameter at most R, and let Xtilde be its lift in E_Q. Then

abs( mu_(s,T_(rho n))(Phi_Xtilde) - mu_(s,T_n)(Phi_X) ) <= K sum over i in X of delta_i(Phi_X) e^(-m d(i, D_r)).

Indeed, by Lemma RAY (ii) on T_(rho n) the first mean is the nu^(T_(rho n))_s-average of mu^(T_(rho n))_(s,V)(Phi_Xtilde), and Phi_Xtilde(U) = Phi_X(Ubar) by (TC), when the links of X are outside D_R. By (CP2) with f = Phi_X this pinned mean differs from g_X(Vbar) by at most tau sum_i delta_i(Phi_X) e^(-m d(i, D_r)), for every V. So the first mean is within that amount of nutilde_s(g_X). By Lemma RAY (ii) on T_n the second mean is nu^(T_n)_s(g_X). Compare nutilde_s(g_X) and nu^(T_n)_s(g_X) by (DC*) on E(T_n) with D empty, mu_1 = nu^(T_n)_s, mu_2 = nutilde_s, the kernels and numbers of Step 1, and the discrepancies b_j = b e^(-m d(j, D_r)) of Step 2 (Y = D_r). The weighted form of (DC*) gives

abs( nutilde_s(g_X) - nu^(T_n)_s(g_X) ) <= sum over i of delta_i(g_X) b e^(-m d(i, D_r))/(1 - alpha').

Step 3 with D = D_r bounds the sum. Together the constant is tau + (pi/2) a tau . a gammabar/(1 - alpha') = K.

Step 5 (orbit types and the defect). As in the proof of Theorem O-SEED (a), Step 3 (row 846; check 850): choose each orbit representative X_0 with one link midpoint within 1/2 of the point z* = (n/2 - 1/2)(1, 1, 1, 1). Then all its links are within R + 1/2 of z*, they are outside D_R, and their distance to D_r is at least d_n = n/2 - R - r - 3/2. The sum of Delta(Phi_(X_0)) over the orbit types is at most 24 beta + 4 w_0 (row 846: Delta(beta x_p) <= 4 beta for six plaquette types, and (N4)). Step 4 gives the bound on abs(e_(rho n)(s) - e_n(s)). (PHI) turns it into a bound on rho^4 F_(T_n)(1) - F_(T_(rho n))(1), and the vacuum cancellation of (PHI) bounds rho^4 E_(T_n) - E_(T_(rho n)). QED

Remarks.

- (What is new.) The proof never writes a potential for the output and never divides by an unknown constant. The anchor s = 0 is exact on both tori, and the tower identity (ii) moves the comparison of the unpinned means to two levels: the output law (soft, by (OUT)) and the pinned law (by (CP)). This is the "separate normalization estimate" that check 877 asks for.
- (Other kernels.) The proof uses the kernel only through Lemma RAY. For the noisy straight decimation (D_a) of row 861, Lemma RAY holds with U_c replaced by the straight block holonomy, and the argument runs on the coarse lattice with (CP) stated for fine measures pinned on the block paths (ARGUED; I did not write it).

**3.4 Corollary TL-S (the seed; PROVED given (Z')).** (a) Let the datum be the Wilson action at one coupling beta (W = 0, E = 0, R = 1). If (CP) and (OUT) hold on {T_n, T_(rho n)}, then

log(1 + S_beta(n; (rho n)^3)) <= (2/rho) Phi^rho(n) <= 48 rho^3 n^4 beta K e^(-m (n/2 - r - 5/2)).

(b) If the two masses of the datum are the bare masses of a first-passage datum (exactness), the same bound holds for the bare thermal sum, as in Corollary SEED-HO of row 846.

**3.5 Proposition SL (the single-link form of (CP); PROVED here from (V1), (DC*) and (BOX), for the Wilson action).** Let W = 0. Suppose that for both tori, every s in [0, 1] and every pin field V, the one-link kernels of mu^T_(s,V) have influence numbers C_ij with sum over j of C_ij e^(m d(i,j)) <= alpha_p < 1. Then (CP) holds with r = R, Gamma = G/4, G = sum over n >= 0 of C^n, so gamma <= alpha_p/(4(1 - alpha_p)) and gammabar <= 1/(4(1 - alpha_p)), and with tau = 2/(1 - alpha_p).

Proof. (CP1): mu_(s,V) and mu_(s,V') have the same one-link kernels, except at j. There the kernels are mu_F and mu_F' with F - F' = a (V_j - V'_j), so they differ by at most a abs(V_j - V'_j)/4 in d_Lip, by (V1). (DC*) with D empty and this one discrepancy gives abs(mu_(s,V)(f) - mu_(s,V')(f)) <= sum_i delta_i(f) G_ij a abs(V_j - V'_j)/4. The weighted row sums of G - 1 = G C are at most alpha_p/(1 - alpha_p), and those of G at most 1/(1 - alpha_p). (CP2): the pin term of a link belongs to the kernel of that link only, and the two pin fields agree on the box. So (BOX) holds for the pinned measures (its proof uses the range of the kernels, (TC) and the tower property): the image of the box marginal of mu^(T_(rho n))_(s,V) and the measure mu^(T_n)_(s,Vbar) have the same one-link conditional laws outside D_R. At a link of D_R two laws on S^3 differ by at most 2 in d_Lip (the chord diameter). (DC*) with D empty, mu_1 = mu^(T_n)_(s,Vbar), and the discrepancies 2 on D_R and 0 elsewhere gives the difference at most 2 sum_i delta_i(f) e^(-m d(i, D_R))/(1 - alpha_p). QED

For the Wilson action the one-link kernel is mu_F with F = a V_l + s beta (sum of six staples). By (V1) and Lemma V-inf of row 861, alpha_p = 18 beta e^m min(1/4, 1/(a - 6 beta)) (the second entry for a > 6 beta). So the single-link form is a finite local statement about one link and its eighteen partners, and it is proved by hand. Its range (PROVED arithmetic, m -> 0):

- with the entry 1/4: beta < 2/9, and then (OUT) holds for small a. This is inside the zone O_DOB of row 846, where Theorem O-SEED already gives the defect bound.
- with the entry 1/(a - 6 beta): (OUT) reads (pi/8) a^2 . 18 beta/(a - 24 beta) < 1. The left side is least at a = 48 beta, where it is 216 pi beta^2. So beta < 1/sqrt(216 pi) = 0.0384. This is the threshold of Theorem STEP of row 861 as corrected by check 877.

So in single-link form Theorem TL proves nothing outside the known zone. This agrees with row 861, Step 5. The content of the theorem at a coupling of order one is the implication from (CP).

## 4. Repeated steps and Proposition CH

**4.1 Rays (definition; this is the anchor of Lemma NRM).** A ray on T is a family (r_s), s in [0, 1], of strictly positive continuous functions on Omega_T, invariant under the translations of T, with r_0 = 1 and with log r_s(V) continuously differentiable in s, the derivative bounded. Its generator is g_s = -d/ds log r_s. nu_s is the probability with density proportional to r_s. An element of a class is a pair of rays, one on T_n and one on T_(rho n), with two constants E_n and E_(rho n). Its two masses are Z(T) = exp(-E_T) times the integral of r^T_1.

**Lemma RAY' (PROVED here).** (i) log of the integral of r_1 equals minus the integral over s in [0, 1] of nu_s(g_s). (ii) The soft step (R_a r)_s(V) = integral of K_a(V | U) r_s(U) dU maps rays to rays and keeps the integral of r_s for every s. The generator of the image is g'_s(V) = mu_(s,V)(g_s), where mu_(s,V)(dU) is proportional to K_a(V | U) r_s(U) dU. (iii) nu_s(f) is the average of mu_(s,V)(f) over the output law.

Proof. (i) d/ds log(integral of r_s) = -nu_s(g_s), and the integral of r_0 is 1. (ii), (iii): as Lemma RAY; the image of r_0 = 1 is 1. QED

The coupling ray of a datum is r_s = exp(-s S_T), with generator S_T.

**4.2 The landed class and its END (PROVED here; the proof is Steps 4 and 5 of Theorem TL).** Fix n, rho, a seam set D in E(T_n), and constants alpha' < 1, m > 0, b, A, eps, eps_E. C_land is the set of elements such that for every s:

- (L1) the one-link kernels of nu^(T_n)_s have influence numbers with weighted row sums at most alpha';
- (L2) for every link j, the one-link conditional law at j of the box image of nu^(T_(rho n))_s is within b e^(-m d(j, D)) of the kernel of nu^(T_n)_s, in d_Lip;
- (L3) the generators are sums over the translates of finitely many types t: g^T_s is the sum of g^T_(t,s) over types and translations; the sum over t and j of delta_j(g^(T_n)_(t,s)) e^(-m d(j, D)) is at most A; and the sum over t of sup over V of abs(g^(T_(rho n))_(t,s)(V) - g^(T_n)_(t,s)(Vbar)) is at most eps;
- (L4) abs(rho^4 E_n - E_(rho n)) <= eps_E.

**Lemma END-RAY.** Every element of C_land has abs(rho^4 log Z(T_n) - log Z(T_(rho n))) <= (rho n)^4 [eps + b A/(1 - alpha')] + eps_E.

Proof. By Lemma RAY' (i) and translation invariance, rho^4 log(integral of r^(T_n)_1) - log(integral of r^(T_(rho n))_1) is minus (rho n)^4 times the integral over s of the sum over t of nu^(T_n)_s(g^(T_n)_(t,s)) - nu^(T_(rho n))_s(g^(T_(rho n))_(t,s)). By (L3) the second mean is within eps_t of the mean of g^(T_n)_(t,s) under the box image. (DC*) with D empty, (L1) and (L2) bounds the rest, as in Step 4 of Theorem TL. QED

**Theorem TL in these words.** If a consistent datum of range R satisfies (CP) and (OUT), the soft step R_a maps its coupling ray into C_land with D = D_r, alpha' = (pi/2) a^2 gamma, b = (pi/2) a tau, the types t = orbit types of local terms with g_(t,s)(V) = mu_(s,V)(Phi_(X_t)), A <= a gammabar (24 beta + 4 w_0) e^(-m d_n), eps <= tau (24 beta + 4 w_0) e^(-m d_n), and eps_E <= 8 (rho n)^4 e_m e^(-m n/3).

**4.3 Corollary CH-RAY (PROVED as logic from 4.2 and Proposition CH).** Read the two tori of Proposition CH as the lattices T_n and T_(L n) at one scale, rho = L. Let C_0 be the set of consistent data of range R that satisfy (CP)(a; Gamma, m, tau, r) and (OUT) with common constants and common bounds on beta, w_0, e_m. Let C_1 be C_land with the constants of 4.2, and R_0 = R_a. Then R_0 maps C_0 into C_1 and keeps both masses. If n is so large that the bound of Lemma END-RAY is at most phi_*, then (END) holds on C_1. So Proposition CH applies: (BASE) for C_0 gives (SEED-L), with no (UNIV-K).

Longer chains have intermediate classes of pairs of rays that satisfy (L2) to (L4) and whose pinned families satisfy the comparison property. The step lemma for a general ray is Theorem TL with Phi_X replaced by the generator types (ARGUED: the same five steps, with the error term eps of the input added; I did not write it out).

**4.4 Lemma COMP (two noise steps are one step with a weaker pin; PROVED here).** The integral over v of k_(a_2)(w | v) k_(a_1)(v | u) is N(abs(a_1 u + a_2 w))/(N(a_1) N(a_2)). So R_(a_2) R_(a_1) is the soft step with the one-link kernel exp(phi(<w, u>)), phi(x) = log N((a_1^2 + a_2^2 + 2 a_1 a_2 x)^(1/2)) - log N(a_1) - log N(a_2), and

phi'(x) = a_1 a_2 A(r)/r <= min(a_1 a_2/4, a_1 a_2/r),   r = abs(a_1 u + a_2 w),   A = N'/N.

The pinned measures of the second step, after the first-step field is integrated, are measures of the input with the one-link pin potentials phi(<W_l, U_l>).

Proof. The integral of exp(<a_2 w + a_1 u, v>) over v is N(abs(a_1 u + a_2 w)). Differentiate. A(r)/r = a(r) is at most 1/4 and at most 1/r (Theorem V of row 785; Lemma V-inf of row 861). QED

Consequence (PROVED as logic). Every hypothesis of a chain of noise steps is a statement about the input measure with one-link pin potentials. The chain creates no new kind of object, and its weakest pin decides. A chain of noise steps is not easier than one noise step.

**4.5 Change of scale (ARGUED).** To change the lattice, a step must be a decimation, for example (D_a) of row 861 with block L. Its pinned measures carry pins on the straight block paths only. After one such step the output is not explicit: its one-link kernels are mixtures over pinned fine measures (row 861, Lemma K3). So the hypothesis of a second step, written for explicit measures, is a statement about fine blocks of side L times the block of the second step. The fine size of the finite statement grows by L at each level. A chain of small steps has small statements only if each output is enclosed, with error bounds, in an explicit class of actions. No one has such an enclosure at a coupling of order one (row 1128, 1.2 (d)).

**4.6 (BASE) (OPEN; not a finite statement).** C_0 of 4.3 consists of explicit Gibbs data. The first-passage density of the account is not given in that form (row 846, 6.1, (R1) to (R3); check 850: membership in a zone is not established, and no impossibility is proved). Lemmas K1, K2 and RAY' accept every positive input. But the ray needs an anchor, and the step needs the comparison property of the pinned first-passage densities at every late cutoff. The account states no property of its block laws (row 837, 1.5; row 861, 7.2). Its natural anchors are the trivial configuration (Theorem HL of row 861 with the vacuum lemma of the account, conditional) and the bare coupling ray. With the bare ray the pins sit on block paths of L^K bare links, so the statement grows with the cutoff (row 861, Step R2, Bearing 2). No finite statement can stand for (BASE) until the account's constants have values.

One can also take, for each datum, its bare Wilson action as the element of C_0. These are explicit Gibbs data of range 1. Then (CP) is needed at every bare coupling of the trajectory, on lattices whose side grows like L^K, with a rate that follows the correlation length. That is an infinite family of statements, as Lemma N of row 1332 says it must be. A finite list of block statements covers finitely many couplings.

## 5. The finite local statement, its size and its cost

Theorem TL has two hypotheses beside the on-file lemmas: (CP) and (OUT). (OUT) is a condition on the numbers of (CP). So the unproved hypothesis is (CP), the comparison property of the frozen-pin family of an explicit action. This section writes it as a statement about one block.

**5.1 One link (PROVED; no computation).** Proposition SL: (CP) follows from the one-link criterion for the pinned kernels. For the Wilson action that criterion is the explicit inequality 18 beta e^m min(1/4, 1/(a - 6 beta)) < 1. It is a statement about one link and its eighteen partners, and it is proved by hand (rows 785, 861). With (OUT) it holds only inside the known zone (3.5).

**5.2 One block (PROVED here: Lemma DC-B and Proposition BL).**

Lemma DC-B (comparison for block kernels; PROVED here; the argument of Lemma DC* with blocks in place of links; the form of the condition is that of Dobrushin and Shlosman, as rebuilt in row 691). Let Lambda be a finite set, Omega = (S^3)^Lambda, d a metric on Lambda, m >= 0. Let BB be a finite family of nonempty subsets of Lambda (blocks) such that every site lies in exactly N >= 1 blocks. For each block B let gamma_B(. | w) be a probability kernel for the sites of B, given the configuration w off B, with numbers K^B_ij >= 0 (i in B, j not in B): whenever w, w' differ only at j, the laws gamma_B(. | w) and gamma_B(. | w') have a coupling with mean abs(U_i - U'_i) at most K^B_ij abs(w_j - w'_j), for every i in B. Put Ctilde_ij = (1/N) times the sum of K^B_ij over the blocks B that contain i and not j, and suppose

alpha := sup over i of the sum over j of Ctilde_ij e^(m d(i,j)) < 1.

Let mu_1 have gamma_B as conditional law of the sites of B given the others, for every B. Let mu_2 be any law, with numbers b^B_i (i in B) such that, mu_2-almost surely, the conditional law of the sites of B under mu_2 and the law gamma_B(. | U off B) have a coupling with mean abs(U_i - U'_i) at most b^B_i, for every i in B. Put bbar_l = (1/N) times the sum of b^B_l over the blocks that contain l, and Gtilde = sum over n >= 0 of Ctilde^n. Then for every f with finite seminorms

abs(mu_1(f) - mu_2(f)) <= sum over i, l of delta_i(f) Gtilde_il bbar_l,   and   sum over l of Gtilde_il e^(m d(i,l)) <= 1/(1 - alpha).

Proof. Let Gamma_B f be the mean of f under gamma_B with the sites off B fixed, and P the average of Gamma_B over the blocks. (1) Seminorms. Gamma_B f does not depend on the sites of B. For j not in B and w, w' that differ at j, the coupling gives abs(Gamma_B f(w) - Gamma_B f(w')) <= [delta_j(f) + sum over i in B of delta_i(f) K^B_ij] abs(w_j - w'_j). There are abs(BB) - N blocks without j. So, as row vectors, delta(P f) <= delta(f) M with M = (1 - N/abs(BB)) 1 + (N/abs(BB)) Ctilde. (2) Convergence. The row sums of Ctilde are at most alpha, so Delta(P f) <= [1 - (1 - alpha) N/abs(BB)] Delta(f). Also abs(Gamma_B g - g) <= 2 sum over i in B of delta_i(g) (the chord diameter is 2), so abs(P g - g) <= (2N/abs(BB)) Delta(g). Hence P^t f converges uniformly, to a function with all seminorms zero: a constant c. mu_1 is invariant under every Gamma_B, so c = mu_1(f). (3) The other law. mu_2(g) is the mu_2-mean of the conditional mean of g given the sites off B, and by the coupling that conditional mean differs from Gamma_B g by at most sum over i in B of delta_i(g) b^B_i. So abs(mu_2(g) - mu_2(P g)) <= (N/abs(BB)) sum_i delta_i(g) bbar_i. Take g = P^t f, use (1), and sum over t: abs(mu_2(f) - c) <= (N/abs(BB)) sum_t delta(f) M^t bbar = delta(f) Gtilde bbar, because 1 - M = (N/abs(BB))(1 - Ctilde). (4) Weights. By the triangle inequality the weighted row sums of Ctilde^n are at most alpha^n. QED

Proposition BL (the one-block form of (CP); PROVED here from Lemma DC-B and the block form of (BOX)). Let Q be a finite set of links of Z^4 with the same number N of links in each direction and with l^infinity midpoint diameter q. Example: the links of a cube of side q, N = q (q+1)^3. Let n > 3 (q + 2R). The blocks are the n^4 translates of Q in T_n; every link lies in N of them. By (TC) the conditional law of the links of Q, given the other links, under mu^T_(s,V), is one function of s, of the pins on Q and of the links within distance R of Q, on both tori.

(B-pin)(a; K, P, m): there are numbers K_ij >= 0 (i in Q, j not in Q) and P_ij >= 0 (i, j in Q) such that for every s in [0, 1] and every pin field on Q:

- (B1) if two configurations off Q differ only at the link j, the two conditional laws of the links of Q have a coupling with mean abs(U_i - U'_i) at most K_ij abs(w_j - w'_j), for every i in Q;
- (B2) if two pin fields on Q differ only at the link j of Q, the two conditional laws (same configuration off Q) have a coupling with mean abs(U_i - U'_i) at most a P_ij abs(V_j - V'_j), for every i in Q.

Put alpha_B = max over the directions mu of (1/N) sum over i in Q of direction mu and j not in Q of K_ij e^(m d(i,j)), and p_m = max over mu of (1/N) sum over i in Q of direction mu and j in Q of P_ij e^(m d(i,j)).

Claim. If alpha_B < 1, then (CP) holds with r = R + q, Gamma = Gtilde Pbar (Pbar_lj = (1/N) times the sum of P over the translates that contain l and j), gamma <= gammabar <= p_m/(1 - alpha_B), and tau = 2/(1 - alpha_B).

Proof. For a link i of direction mu, the translates that contain i put i at each of the N links of Q of direction mu once. So the weighted row sums of Ctilde are at most alpha_B, and those of Pbar at most p_m. (CP1): mu_(s,V) and mu_(s,V') have the same block kernels for the blocks without j, and for a block with j the discrepancy a P_ij abs(V_j - V'_j) by (B2). Lemma DC-B gives abs(mu_(s,V)(f) - mu_(s,V')(f)) <= a abs(V_j - V'_j) sum over i, l of delta_i(f) Gtilde_il Pbar_lj. (CP2): let mu_1 = mu^(T_n)_(s,Vbar) and mu_2 the image of the box marginal of mu^(T_(rho n))_(s,V). For a block that does not meet D_R the two have the same conditional law of the block given the rest: this is the block form of (BOX) (row 846, end of 4.2), with pins that agree. For a block that meets D_R take the discrepancy 2. Then bbar_l <= 2 for the links within distance q of D_R, which lie in D_(R+q), and bbar_l = 0 elsewhere. Lemma DC-B gives abs(mu_1(f) - mu_2(f)) <= 2 sum_i delta_i(f) e^(-m d(i, D_(R+q)))/(1 - alpha_B). QED

So, with Proposition BL, Theorem TL and Corollary TL-S (a):

**Theorem BS (the block step in one-block form; PROVED here given the on-file lemmas).** Let the datum be the Wilson action at a coupling beta, and Q a block as above. If (B-pin)(a; K, P, m) holds with alpha_B < 1 and (pi/2) a^2 p_m/(1 - alpha_B) < 1, then for n > 3(q + 2) and rho >= 2

log(1 + S_beta(n; (rho n)^3)) <= 48 rho^3 n^4 beta K e^(-m (n/2 - q - 7/2)),

with K at most 2/[(1 - alpha_B)(1 - theta)], theta = (pi/2) a^2 p_m/(1 - alpha_B). The same holds for every consistent datum of range R, with 24 beta + 4 w_0 in place of 24 beta, and r = R + q.

Its only unproved hypothesis is (B-pin): a statement about the conditional law of the links of one block, uniform in s, in the pins of the block and in the configuration around it. For blocks of one link (Lemma DC-B with the family of all links, N = 1) it is the one-link criterion of 5.1: the coupling numbers are the influence numbers, by Kantorovich duality, and P_jj = 1/4 by (V1). Theorem W of row 691 is the relative of Proposition BL in total variation, with the number of disagreeing links in place of the chord distances.

(B-pin) is local and it concerns one block. It is not a finite computation as it stands: it has a supremum over a compact set of high dimension. Section 5.3 sizes it.

**5.3 Size (PROVED counts; GUIDE estimates; no cost floor).**

Lemma DIM-B (the boundary data of a cube; PROVED here). Let Q be the set of links of the cube of side q in Z^4. It has 4 q (q+1)^3 links. Exactly 24 q (q+1)^2 plaquettes contain a link of the cube and a link outside it, and each of them contains exactly one link of the cube. For the Wilson action the conditional law of the cube given the outside depends on the outside through the 24 q (q+1)^2 staples of these plaquettes, and every value in SU(2)^(24 q (q+1)^2) of the staples occurs. So the supremum in (B1) runs over a set of at least 72 q (q+1)^2 - 3 (q+1)^4 real dimensions for the configuration off Q (the gauge group of the cube sites is divided out), and 12 q (q+1)^3 more for the pin field. For q = 1 the first number is 240; for q = 2 it is 1053; for q = 10 it is 43197.

Proof. A link (y, y + e_mu) is in the cube when y and y + e_mu are in {0, ..., q}^4: q (q+1)^3 links in each direction. A plaquette in the plane (mu, nu) lies in the cube in q^2 (q+1)^2 positions, so 6 q^2 (q+1)^2 plaquettes have four cube links. Each cube link is in six plaquettes. Let a plaquette contain the cube link (y, mu) and a corner outside the cube. Its two other corners are y +- e_nu and y + e_mu +- e_nu, and they are in the cube together or not at all. So both are outside, and the three other links have an end outside. The count is 6 . 4 q (q+1)^3 - 4 . 6 q^2 (q+1)^2 = 24 q (q+1)^2. The link of such a plaquette that is parallel to the cube link has both ends outside the cube, and it belongs to no other plaquette of this kind (the coordinate nu of its ends is outside {0, ..., q}, and it fixes y and the sign). The staple is a product of that link with two fixed elements, so the staples take all values independently. A gauge transformation at the (q+1)^4 cube sites acts on cube links, pins and staples together and keeps chord distances. QED

GUIDE (the side that (B-pin) needs at the window). At m = 0, alpha_B is the mean, over the cube links of one direction, of the total influence from outside. Each of the 6 q (q+1)^2 outside plaquettes at a cube link of direction mu brings three outside links, and each moves the staple of that cube link. Let k_1 be the least value that K_ij can take for such a pair. Then alpha_B >= 18 k_1/(q+1). The response of one link to one of its staples is of order beta times the variance of a tangential component of the link, which is between about 0.2 and beta/4 = 0.57 at beta = 2.3 (ARGUED; the upper value is the worst case of Theorem V). So q + 1 is above 3.6 to 10 from these direct terms alone. The influence that passes through the block adds to it. So q is at least about 3, and more likely of order 10. Proposition B of row 691 gives the complementary bound in units of the correlation length.

What this means for a computation (ARGUED).

- A single evaluation of the block law at one configuration around the block is an integral over 12 q (q+1)^3 real dimensions: 96 for q = 1, 6000 for q = 4, about 160,000 for q = 10. The supremum is over hundreds to tens of thousands of further dimensions (Lemma DIM-B).
- I can specify the statement. I cannot specify a computation for it inside 10^15 operations. A grid over the surroundings is excluded by the dimension. The hand methods replace the supremum by majorants; the families on file stop at 2/9 (one link, proved), 2/3 (the cap of one-link bounds), 0.3609 (vertex blocks, proved) and 0.775 (their cap), and 1.0109 (background-uniform layer twists) (rows 785, 836, 839, 857; row 861 and check 877: each number caps one family, not every method).
- This is no floor. Check 1331 warns against floors from counts. A method that treats the surroundings as symbols (a certificate in the algebra of class functions, or a sum of squares) is not excluded. I know none with a demonstrated cost at a coupling of order one. Row 1326 with check 1331 says the same for (KER).
- For comparison: (KER) at the window pair of row 1326 is one inequality on the tori 10 x 20^3 and 20^4, with no supremum. So the block statement is not smaller than the in-law statement. It is larger: it carries the supremum that makes it local.

**5.4 Weak pins: at a fixed coupling the step does not shrink the statement.**

Lemma WEAK (PROVED here). (a) Suppose (CP2) holds without pins (a = 0: the measures mu_(s,T), s in [0, 1]) with constants (tau, m). Then abs(Phi^rho(n)) <= (rho n)^4 [tau (24 beta + 4 w_0) e^(-m d_n) + 8 e_m e^(-m n/3)]. No step is used. (b) If gammabar stays bounded as a tends to 0, the constant K of Theorem TL tends to tau.

Proof. (a) (PHI), and (CP2) with f = Phi_X for each orbit type, as in Step 5 of Theorem TL. (b) K = tau [1 + (pi/2) a^2 gammabar/(1 - (pi/2) a^2 gamma)]. QED

So at a = 0 Theorem TL is the direct statement: comparison of the unpinned local means along the coupling ray, which is (PATH) of row 861. A step with a > 0 trades the unpinned comparison for the pinned one. The trade is useful only if pins that satisfy (OUT) make the comparison easier. Lemma GAUSS and the guide run of 5.5 say how strong such pins can be.

Lemma GAUSS (the quadratic model; PROVED here for that model). On T_n let C be the covariance of the Gaussian measure on real 1-forms with precision a + beta d*d (the quadratic model of the flat-pinned measure; d is the lattice exterior derivative). Then for every link c

a^2 sum over k != c of abs(C_ck) >= h(a, beta) := (3/4) n^(-4) sum over momenta p of a beta phat^2/(a + beta phat^2) >= 6 a beta/(a + 16 beta),

with phat^2 = sum over mu of 4 sin^2(p_mu/2).

Proof. H' = a - a^2 C = a beta d*d (a + beta d*d)^(-1). d*d vanishes on exact forms, so H' d lambda = 0 for every function lambda on the sites. Take lambda = 1 at one end x of c and 0 elsewhere. d lambda is +-1 on the eight links at x and 0 elsewhere. Row c of H' d lambda = 0 gives H'_cc <= sum over k != c of abs(H'_ck) = a^2 sum over k != c of abs(C_ck). H' commutes with the translations and the signed permutations of the hypercubic group, so H'_cc is the trace of H' divided by 4 n^4. At momentum p, d*d has the eigenvalue phat^2 three times and 0 once. This gives h. For the last bound: x -> a x/(a + x) is concave and vanishes at 0, so on [0, 16 beta] it is at least (x/(16 beta)) . 16 a beta/(a + 16 beta), and the mean of phat^2 is 8. QED

Reading (GUIDE for SU(2); PROVED for the quadratic model). By (CP1) with f = <xi, U_c>, every admissible Gamma_ck is at least the absolute value of the covariance of <xi, U_c> and <e, U_k>, for e tangent at V_k, under every member of the family. In the quadratic model each tangential component has the covariance C. So there a^2 gamma >= h(a, beta), and (OUT) fails when (pi/2) . 6 a beta/(a + 16 beta) >= 1, that is for a >= 16 beta/(3 pi beta - 1) when beta > 1/(3 pi). For large beta this is a >= 1.70; at beta = 2.3 it is a >= 1.78. The exact h gives a smaller threshold: as beta grows, h tends to 3a/4 and the threshold to 8/(3 pi) = 0.85. The flat-pinned SU(2) measure is close to the quadratic model where the pins order the links (the Higgs side of the crossover; ARGUED). So a soft step that lands in one step cannot use pins on that side, whatever beta: by the bound its pins are below 1.8, and by the direct sums of 5.5 they are far below. At beta of order 2 the action term of one link has strength up to 6 beta, about 14. Pins that land are weak against the action. They are below or near the crossover of the fixed-length Higgs model (near kappa = 0.7 to 0.8 at beta of 2.3 to 2.5; Bonati, Cossu, D'Elia and Di Giacomo, as read in row 923, `library/gap-thermpin-opus.md`; GUIDE). Section 5.5 measures the same quantity for SU(2) at beta = 2.3.

Consequence (ARGUED). At a coupling of order one, the pinned comparison that Theorem TL needs is a comparison for measures that differ little from the unpinned ones. The mass that the pins give does not make the block smaller than the correlation length of the theory itself. With Lemma COMP, the same holds for every chain of noise steps. So at a fixed coupling the block step does not shrink the finite statement below the direct one of Lemma WEAK (a). Its use is elsewhere: it accepts inputs that are not Gibbs data (Lemma K2), which only the account's densities need.

**5.5 Guide run and arithmetic checks (GUIDE; no proof step uses them).**

Method of the run. SU(2), Wilson action at beta = 2.3, with the flat pin a <1, U_l> on every link. This is one member of the frozen-pin family, at s = 1. Periodic lattices 4^4 and 6^4, heat bath, 300 sweeps discarded, then 6000 sweeps (4^4) or 1500 sweeps (6^4), one measurement per sweep, one seed. Measured: for two links c != k, the 3 x 3 matrix of covariances of their tangential components (the three imaginary components), with the conditional mean of a link in place of the link where that is exact. Then the sum over k != c of the operator norms of these matrices, with the singular vectors taken from one half of the run and the value from the other half. This estimate is biased downward and has no noise floor. By the reading of Lemma GAUSS, the number gamma of every admissible Gamma is at least this sum. So the last column is a lower estimate of alpha' of (OUT) at flat pins. Other pin fields can only raise the supremum. Floating point, no error bars: GUIDE only. The scripts are not part of this commit (the row commits one file).

| lattice | a | mean link <1, U> | plaquette | sum over the 18 partners | sum over all k | (pi/2) a^2 times the sum |
|---|---|---|---|---|---|---|
| 4^4 | 0.25 | 0.064 | 0.610 | 0.007 | 0.009 | 0.001 |
| 4^4 | 0.5 | 0.134 | 0.611 | 0.049 | 0.064 | 0.025 |
| 4^4 | 0.625 | 0.172 | 0.611 | 0.086 | 0.091 | 0.056 |
| 4^4 | 0.75 | 0.238 | 0.615 | 0.187 | 0.289 | 0.26 |
| 4^4 | 0.875 | 0.374 | 0.630 | 0.436 | 0.958 | 1.15 |
| 4^4 | 1.0 | 0.463 | 0.639 | 0.536 | 1.205 | 1.89 |
| 4^4 | 1.5 | 0.639 | 0.662 | 0.552 | 1.306 | 4.62 |
| 6^4 | 0.75 | 0.227 | 0.606 | 0.156 | 0.201 | 0.18 |
| 6^4 | 1.0 | 0.467 | 0.638 | 0.542 | 1.321 | 2.08 |

Reading (GUIDE).

- The lower estimate of alpha' passes 1 between a = 0.75 and a = 0.875 on 4^4, and between 0.75 and 1.0 on 6^4. This is where the mean link rises (0.24 to 0.37 to 0.46): the crossover of the fixed-length Higgs model. So at beta = 2.3 a noise step that lands must have a below about 0.8. The staple field of a link is up to 6 beta = 13.8.
- Below the crossover the covariances of two links are small. At a = 0 they vanish by gauge invariance. So (OUT) by itself does not exclude a landing with a of 0.5 to 0.75 at flat pins. The run says nothing about other pin fields, about s < 1, or about (CP).
- Above the crossover the sum grows toward the quadratic model. A direct evaluation of the quadratic model at beta = 2.3 (floating point) gives a^2 times the sum equal to 1.09, 2.12, 4.00 at a = 0.25, 0.5, 1.0 on the torus of side 4 (1.35, 2.58, 4.74 on side 6). The bound h of Lemma GAUSS is 0.36 and 0.70 at a = 0.5 and 1.0. So in the quadratic model (OUT) fails at a = 0.25 already; the sum is close to linear in a, which puts the threshold near 0.15.

Arithmetic checks (floating point; they check numbers that the text quotes, and no proof step uses them). (1) Lemma GAUSS on the tori of side 3 and 4 at six pairs (a, beta): H'_cc = h to nine digits, and both inequalities hold. (2) Lemma DIM-B by enumeration for q = 1, 2, 3: 32, 216, 768 cube links and 96, 432, 1152 outside plaquettes, each with exactly one cube link. (3) 1/sqrt(216 pi) = 0.03839; 16/(3 pi) = 1.698; 8/(3 pi) = 0.849; 16 . 2.3/(3 pi . 2.3 - 1) = 1.780.

## 6. Fact tests (ARGUED unless marked)

The tests are those of `parts/gap.md` (the test table of row 998). A test model refutes a tool only if the tool's hypothesis holds in it.

| Test | The proved statements of this file | The open hypothesis (CP), or (B-pin) |
|---|---|---|
| Compact U(1), Coulomb phase | Lemmas RAY, PV2, DC-B, COMP, NRM, Theorem TL and Proposition BL use the group only as a sphere with its chord metric. They hold word for word on the circle. Proposition SL needs the circle form of (V1) (row 861, Step 3a). None asserts a gap, so none is contradicted. | Must fail, because the conclusion of Theorem TL fails there (recalled: Guth; Frohlich and Spencer; row 786 has a related statement for Villain U(1) at beta >= 2^14). Where it fails: for weak pins the Coulomb phase persists (recalled: Fradkin and Shenker, the Higgs model with a field of charge one; GUIDE), so (CP) has no rate. For pins on the Higgs side (OUT) fails: Lemma GAUSS is the quadratic model of this case (PROVED for the model, for a above 1.7), and the direct sums of 5.5 put the failure at every a above about 0.15 (GUIDE). |
| Product with a massless factor | as above | (CP) of the product family fails in the massless factor. A statement about one factor does not give (CP) of the product (Lemma PT of row 998 applies to such statements). |
| Frozen Q_8 and 2T | The lemmas hold for a finite subgroup with the counting measure, with the chord metric on its points and continuous pin fields (not written). | Must fail above freezing (row 861, 8.1): the defect is of order one there. Under weak pins the frozen links keep long-range order (GUIDE). |
| Worst-case tests: Theorem D2 (row 977), Lemma SHEET (row 996), row 1139 | not used | (CP) takes a supremum over the directions of unit pins of one strength on every link. The tilts of D2 pin some links and free others; they are outside this family. SHEET is uniform over plaquette coupling fields; outside. Row 1139 orders a layer only from b_* of about 4.0e3 on. So none of them refutes (CP) at the window. Row 1011 treats pins of homogeneous strength in a pinned cell; I did not read it. |
| The Higgs line (flat pins) | not used | For flat pins the family is the fixed-length Higgs model. GUIDE (Bonati, Cossu, D'Elia and Di Giacomo, as read in row 923's file): its first-order line ends near beta = 2.73. Above that coupling (CP) fails when the ray s -> (s beta, a) meets the line, so a must avoid the range of the line. Below it no flat-pin obstruction is known. |
| A weight at a coexistence point (Proposition V of row 712; the K7 line) | Theorem TL holds for every datum of the class of row 846, so also for these plaquette weights | (CP) fails at coexistence: weak pins choose between the phases, so the pinned means have no uniform comparison. A verified (B-pin) would be a statement about the Wilson weight and would not hold for these weights. |
| Selectivity | The proofs are group blind. | The group and the weight enter in (CP) only. This is the position of Theorem W (row 691) and of PIN-MIX (row 861). |

No test refutes a proved statement of this file. No test supports (CP) at a coupling of order one.

## 7. Verdict

**7.1 Decision.** Not solved. The block step of Proposition CH now exists as a theorem with one stated hypothesis (Theorem BS: Theorem TL with Proposition BL). The two conditions of the brief are not both met.

| Condition of the brief | State | First failing step |
|---|---|---|
| The only unproved hypothesis is a local statement about one block | Met in form: (B-pin), PROVED implication (Proposition BL). For one link the statement is proved by hand, and reaches no coupling outside the known zone (3.5) | - |
| ... small enough to compute exactly and check in Lean | Not met. (B-pin) has a supremum over at least 240 real dimensions for the smallest cube, and the block must have a side of about 3 to 10 at the window (GUIDE). No computation inside 10^15 operations is specified. I prove no floor | a rigorous method for one supremum of a block law over its surroundings, at a coupling above 0.3609 (5.3) |
| Repeated steps satisfy Proposition CH | Met for the maps and for (END): classes of rays, Lemma END-RAY, Corollary CH-RAY. Not met for (BASE): the classes hold explicit Gibbs data, and the account's first-passage densities are not given as such | (BASE): block-law statements of the account, with numbers (4.6) |

Two structural results limit what the step can do (PROVED where marked).

- Lemma NRM (PROVED): a class of a chain needs an anchor. Normalized laws alone carry no information on the defect. The coupling ray is such an anchor; it is exact at s = 0.
- Lemma COMP (PROVED) with Lemma WEAK (PROVED) and Lemma GAUSS (PROVED for the quadratic model; GUIDE for SU(2), with the run of 5.5): a chain of noise steps is one noise step, and a noise step that lands uses pins that are weak against the action at a coupling of order one. So at a fixed coupling the step does not make the finite statement smaller than the direct comparison along the coupling ray. The block statement is larger than the in-law statement (KER), because it carries a supremum.

**7.2 What this says about the question behind the row (ARGUED).** The question was whether the next runs should target the one blocking step at medium coupling. The step is now proved as an implication. What blocks is not the step. It is its hypothesis, and that hypothesis is of the same kind and at least the same size as the statements that rows 691, 836, 846 and 861 stopped at: a comparison of local means that is uniform over the surroundings of a block several lattice units wide. The lifted computation rule does not reach it, because no exact method is known for a supremum of that dimension. For the trajectory there is a second obstacle that no computation touches: the hypothesis must hold for the account's densities, which have no numbers and no block-law statements.

**7.3 What would change this decision.**

- A rigorous method, with a demonstrated cost, for the supremum of a block law over its surroundings at a coupling of order one. Candidates that are not excluded: certificates that treat the surroundings as symbols (in the algebra of class functions, or sums of squares over the local equations with boundary terms). A first test of any such method: prove alpha_B < 1 for one block at beta = 0.4, just above the hand range, with no pins.
- Or an enclosure, with error bounds, of the output of one decimation step in an explicit class of actions at a coupling of order one. Then a chain of small steps has small statements (4.5).
- Or block-law statements from the account: a comparison property for its pinned first-passage densities. Then (BASE) and the first step can be stated.
- Or a comparison property that is not uniform over the surroundings and is still local. None is on file (rows 845 and 852 on annealed forms; Lead rule CL in `parts/gap.md`).

**7.4 What a kernel-checked computation can serve now (ARGUED).** The numeric constants of this file (the one-link numbers, the function h of Lemma GAUSS, the thresholds 0.0384 and 1/(3 pi)), and exact small counterexamples. Not (B-pin) at a coupling of order one, and not (BASE).

**7.5 Suggestions for the lead (suggestions only).**

1. A check of this file by another model, in this order: Theorem TL (Lemma RAY; Steps 1 to 4; the use of (DC*) with D empty and discrepancies; the geometry of Step 5); Lemma DC-B; Proposition BL (the block form of (BOX), the count of translates, the strip D_(R+q)); Lemma DIM-B; Lemma GAUSS; Lemmas COMP, WEAK and NRM.
2. If Theorem TL holds: record in `parts/gap.md` that the potential form (POT) of row 861 is not needed for the seed. The real-variable comparison property (CP) of the frozen-pin family is enough.
3. No row on a verified computation of a block step before a method exists for the first test of 7.3.
4. For rows on the account: the exact statement that (BASE) needs is a comparison property of pinned first-passage densities, uniform in the cutoff (4.6).

## 8. Not done, and credits

**8.1 Not done.** I did not read the primary text of the account, of Balaban, or of any published paper; statements about them come from the rows named. I did not read row 1341 (`library/gap-blockstep-astra62.md`, the parallel attempt on the same brief) or its check; this file is independent of them. I did not re-check the on-file lemmas (V1), (DC*), (BOX), (PHI), (Z'), Lemma FL, or the lemmas of row 861; I used them as their checks state them. I did not write the decimation form of Theorem TL (3.3, remark), nor the step lemma for a general ray (4.3), nor the finite-group and circle forms of the lemmas (Section 6). (B-pin) is stated with couplings; I did not study how to verify it. The guide run of 5.5 is a floating-point Monte Carlo on small lattices with flat pins only; it samples one member of the family at s = 1 and proves nothing. I wrote no Lean. Nothing in this file is checked by another model.

**8.2 Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the account, its first-passage data and tori. Tadeusz Balaban: the block renormalization method and the ultraviolet stability theorem. Roland Dobrushin: the uniqueness condition and the comparison argument behind Lemmas DC* and DC-B. Dobrushin and Shlosman: the block form of the condition (known here through the rebuild of row 691; their paper was not read). Kantorovich: the duality between couplings and Lipschitz functions. Osterwalder and Seiler; Luscher: the transfer operator behind Lemma Z'. Fradkin and Shenker; Bonati, Cossu, D'Elia and Di Giacomo: the phase diagram of the Higgs model (recalled, and as read in row 923). Guth; Frohlich and Spencer: the Coulomb phase of compact U(1) (recalled). Haller and Kennedy; Bertini, Cirillo and Olivieri: the principle that a mixing condition for the constrained system defines one renormalization step (as recalled in row 1128; not read). The two-level structure of Theorem TL (a condition for the fine field given the image field, and a quantitative continuity statement for the image) is, as I recall it, the structure of the work of Kulske and Opoku on transforms of Gibbs measures; I did not read it for this row and I claim no novelty for the mechanism. In the lane: Codex gpt-6-astra and gpt-6.2-astra (rows 785, 850, 877, 1331, 1335: Theorem V, Corollary V1, and the checks cited); Claude Opus 5.5 (rows 837, 846, 836, 693: Lemma FL, Lemmas DC*, BOX, PV, Identity PHI, Theorem O-SEED, the block criterion, and checks); Claude Fable 5.2 (rows 691, 720, 861, 1128, 1332: Theorem W, Lemma Z', the soft kernels, Lemmas K1 to K4', Theorems STEP and HL, Proposition VAC, the RG council, Proposition CH).

RESULT: Row 1340 (Claude Fable 5.2 max, laptop subagent; author only, checked by no one; one small guide Monte Carlo and three arithmetic checks, no large computation; row 1341 not read). NOT solved: no block step at a coupling of order one is verified, and no computation inside 10^15 operations is specified for one; no impossibility is proved; nothing in the chain is disproved. PROVED here (by hand, unchecked; given the on-file Lemmas DC*, BOX, Identity PHI, Corollary V1 and Lemma Z'): Theorem TL (one soft step of row 861 applied to the whole coupling ray: if the input measures with one unit pin of strength a on every link have the comparison property (CP) (one pin moved; the two tori) with (pi/2) a^2 gamma < 1, then the defect of the two masses is at most (rho n)^4 K (24 beta + 4 w_0) e^(-m d_n) plus the vacuum term; no potential, no cumulant expansion, no vacuum constant; this is the normalization estimate that row 861 and check 877 left open); Lemma DC-B (Dobrushin comparison for block kernels with chord coupling numbers) and Proposition BL ((CP) from the statement (B-pin) about the conditional law of one block), hence Theorem BS (the seed at a coupling beta from the one-block statement (B-pin)); Proposition SL (for one link (B-pin) is the hand criterion of rows 785 and 861 and reaches only beta < 2/9, or beta < 1/sqrt(216 pi) = 0.0384 with strong pins); Lemma NRM, Lemma RAY', Lemma END-RAY and Corollary CH-RAY (classes of pairs of rays: the maps keep both masses and the landed class has (END), so Proposition CH applies given (BASE)); Lemma COMP (a chain of noise steps is one noise step with a weaker pin); Lemma WEAK (at pin strength 0 the theorem is the direct comparison along the coupling ray); Lemma GAUSS (in the quadratic model a^2 gamma >= 6 a beta/(a + 16 beta)); Lemma DIM-B (the cube of side q has 24 q (q+1)^2 boundary staples, so the supremum in (B-pin) has at least 240 real dimensions for q = 1 and 43197 for q = 10). GUIDE: at beta = 2.3 with flat pins the lower estimate of (pi/2) a^2 gamma passes 1 between a = 0.75 and 0.875 (Monte Carlo, 4^4 and 6^4), so a landing step uses pins that are weak against the staple field 13.8; the cube of (B-pin) needs a side of about 3 to 10 at the window. First failing steps: a rigorous method for one supremum of a block law over its surroundings at a coupling above 0.3609 (the hand families stop at 2/9, 2/3, 0.775 and 1.0109); (BASE), which is not a finite statement (the account gives no explicit Gibbs form and no block-law statement for its first-passage densities). At a fixed coupling the step does not shrink the finite statement below the direct comparison, and the block statement is larger than the in-law (KER). OPEN: (B-pin) or (CP) at any coupling above the hand range, (BASE), the seed, the mass gap. Output library/gap-blockstep-fable.md.
