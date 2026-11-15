lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T11:45Z

# gap-hcphys-max (FINISH row 982): (HC-phys) on the account's lattices, N2 of row 978

Research-stage working state. Nothing here is a public claim. Marks used: PROVED, ARGUED, OPEN.
Pinned at commit a2764492e, branch `claude/ym4d-hard-route`. Worker: Mac mini worker 3, one session, no subagents.
Scripts and data: `library/guide/lane982/`.

## 0. Plan (at most eight steps; one step per response; each step appends its result here before the next)

1. **Read and scope.** FINISH.md (rules, Build on published work, efficiency rules), GOAL.md, row 978 output `library/gap-ladder-max.md` (Section 8 N2, 5.6 (a), 5.7, Theorem BR), rows 720, 975, 977 as the row names them. Grep `library/open-core.md` and the FINISH rows for every lemma before attacking it. Record overlaps.
2. **Port question of N2.** Which convexity of the fluctuation action at each scale below the unit the account's small-field statements give, and in which norm. Quote file and line. Port, never redo.
3. **Fact tests, one verdict each, before any proof.** The four of N2 (free photon and compact U(1) fail through the rate only; the weights w_p of row 720 (M3); the per-scale loss of order g_k^2; the square-root test of 5.7), the two of this lane (row 977 Theorem D2: no supremum over tilts; row 975 Lemma META: a transience input must be named), and frozen Q_8, 2T, K7, FT-FK.
4. **The inequality left at the unit scale.** Exact statement of the crux lemma, with quantifiers and the order of constants.
5. **Attack, route 1.**
6. **Attack, route 2.**
7. **Attack, route 3** (only if routes 1 and 2 fail).
8. **Next step and RESULT line.**

Status of the plan: steps 1 and 2 written (2026-11-15T00:25Z). Step 3 next.

## Step 1. Scope, sources read, duplicate check (rule 0a)

**Read.** GOAL.md in full. FINISH.md: lines 1-100, 299-356, rows 970-983. `gap-ladder-max.md` (row 978): Steps 1, 3, 4, 5, 7 (headers), 8. `gap-fc-max.md` lines 121-228 (Theorem BR, its objects B1-B5, corollaries, hand checks). The account of Sussman and Alpoge: `theorem_0_complete_account_raw_I.tex` and `_II.tex` at commit `31a47c543775`, fetched by URL into a scratch folder (the folder `~/ym4d-papers` does not exist on this worker); read at CA-II 75150-75215, 80014-80050, 80152-80200, 81161-81215, 83869-83905, 84178-84210, and grepped as stated below. CA-III was not fetched.

**The statement of the row (from `gap-ladder-max.md` 5.2, 5.6 (a), 8.4 N2).** A family of cutoffs iota with coupling beta_iota and spacing a_iota (in the unit of the account, the first-passage scale). B is the periodic cube of physical side 2 ell, nu the vacuum law of a slice, P the vacuum chain, p_s(u, .) its s-step density.

- (HC-traj)_(alpha, s): ||P^m p_s(u, .)||_2 <= ||p_s(u, .)||_(1 + e^(-2 alpha m)) for nu-almost every u and every m >= 0.
- (HC-phys): there is M_H > 0, free of iota, with (HC-traj)_(alpha, s) at 2 s a_iota = l (a fixed physical time) and alpha >= M_H a_iota.
- Theorem BR (`gap-fc-max.md` 5.2, checked row 949 per the lane): (LSI-br)_s with rates alpha_s on the bridge laws nu_s, 0 < s < 1/beta, gives (HC-vac) with alpha = (1/2) integral of alpha_s ds.

**Duplicate check.** `library/open-core.md`: no hit for HC-phys, HC-traj, LSI-br, hypercontract, Sobolev (count 0). FINISH rows that name (HC-phys), (LSI-br), (HC-traj) or (LSI-traj-seed): 947, 968, 970, 974, 975, 977, 978, 982. Rows 979-981 and 983 are checks and a reading test; none attacks (HC-phys). Matches that I name and do not attack:

- (LSI-traj-seed)_a of row 970 (OPEN there): the log-Sobolev inequality on the bridge interpolations of P^k p_1(u, .) at one fixed coupling. The unit-scale inequality of Step 4 below is the same statement for an effective action. I state the match there.
- B11 with crux (HC) (`gap-skeleton-max.md` L190-195), named in row 978 Step 7.
- (TILT-COV-sup), (LOC-COV), (ABS-flow): refuted or open in rows 970, 973, 977. Not attacked.
- (UNIV-K)/(CC), (NOCRIT), (VIR_K), Theorem ZD with (BDD-Delta) and (Z-UNB) of row 720: named in row 978; not attacked.

## Step 2. The port question of N2

**Question.** Which convexity of the fluctuation action at each scale below the unit do the account's small-field statements give, and in which norm?

**Answer (port; credit Sussman and Alpoge, with Claude and Codex as authors of their text, and Balaban for the operator theorem they quote).**

(P1) *The form bound, and its status.* CA-II 80163-80172, Definition 8.3:def-box-precision: "From the operator theorem at free current we take the following hypothesis. At each real background configuration of the step, Q is real symmetric and a_- <= Q <= a_+ as forms, ||Q(b, b')|| <= a_+ e^(-c_A dist(b, b')) ..., where 0 < a_- <= a_+ and c_A > 0 do not depend on the level, on K, m, the background configuration or the volume." Q is the fluctuation form on g^(B+), B+ the free bonds of the new small-field domain; "All inner products, adjoints and order relations between operators refer to the Euclidean inner product of g^(B+)" (80156-80158). The same bound is the antecedent of CA-II 75164-75195, Lemma 8.2:lem-fluctuation-positivity: "Assume, as the antecedent of this lemma, the lower bound ... Q(U, 0) >= gamma_0/2 on the constraint surface". So the account takes the lower bound as a hypothesis from Balaban's operator theorem (it cites CMP 95 Proposition 1.2 and CMP 99b at 75158-75159). In this repository it is A2 of the ledger (rows 78, 90: real A2 on separated layers; not the full A2).

(P2) *The norm.* The Euclidean l^2 norm of the fluctuation variable A = (A(b)), one Lie-algebra vector per free bond of the lattice of level k, "taken in the rescaled normalisation in which the unscaled fluctuation field is g_k A" (CA-II 80039-80041). So in the unscaled link-angle metric of level k the convexity constant is a_-/g_k^2 = a_- beta_k, with beta_k the running coupling of level k. It is a four-dimensional statement: the bonds b run over a four-dimensional region Lambda_(k+1).

(P3) *The class of laws.* CA-II 81161-81190, Proposition 8.3:prop-lipschitz-stability: a "Hamiltonian on W" is H(y) = (1/2) <y, A y> + <h, y> - P(y) on a product W of open convex sets K_b with B(0, r_in) in K_b in B(0, b-hat); it is "coercive for phi" if T_phi A T_phi^(-1) >= lambda_A and sup_W ||T_phi P'' T_phi^(-1)|| <= eps_0 < lambda_A, "and then lambda := lambda_A - eps_0"; the Gibbs measure is nu_H = Z_H^(-1) 1_W e^(-H) dy. At phi = 0 this is: Hess H >= lambda on the convex set W. So each small-field fluctuation law is uniformly log-concave on a convex window, with a constant free of the level, in the norm of (P2). The window is the product of norm balls of radius b_k = A_1 (log x_k)^(p_0) (80031-80045).

(P4) *What the account derives from it, and what it does not.* Derived: Lipschitz stability (81161), a two-sided density bound (81493), sub-Gaussian tails of linear functionals (81804), exponential decay of correlations in the class (83869; its proof assumes the Helffer-Sjostrand covariance representation as a stated hypothesis). Not derived: CA-II 84184-84186 says of that proof "It uses no spectral gap of -L, no variance inequality for log-concave measures in terms of the inverse Hessian". A grep of CA-I and CA-II for "Sobolev", "Bakry", "hypercontract" finds no log-Sobolev or hypercontractive statement (CA-I: 0 hits; CA-II: one hit, a discrete Sobolev norm in a model section). CA-I 2708 lists a mass gap among the things not asserted. So a log-Sobolev inequality for a small-field fluctuation law is not in the account. It would be a new lemma: the Bakry-Emery criterion on a convex domain gives the constant lambda (RECALLED, classical; to be rebuilt if used).

(P5) *What is outside the port.* (a) Large-field regions carry no convexity statement. (b) The convexity is conditional: it is for the fluctuation law of one step given the coarser field. (c) The account's control stops at the first-passage scale, the unit. So below the unit the port gives: conditional, four-dimensional, small-field, uniform log-concavity with constant a_- beta_k in the level-k link metric. Step 3 tests whether this can feed (LSI-br), which is an inequality for a slice law in the fine link metric.

Kind of result: a reading of their text (port answer). No statement of theirs is corrected.

## Step 3. Fact tests (before any proof; one verdict each; no run was made)

The statement under test is the route of N2: *(LSI-br) on the fine lattice from the port (P1)-(P3) at every level below the unit, plus one inequality at the unit scale.* Notation: beta_0 = beta_iota is the bare coupling, beta_k the running coupling of level k, K the level of the unit, L the block side, l_unit = L^K a the unit in fine lattice steps.

### 3.0 Lemma CAP (the size the bridge constants must have). PROVED given Theorem BR, steps (ii) and (iv); by hand; not checked

Setting of Theorem BR. For gauge-invariant continuous f let u_s be its bridge interpolant (u_s = N_s/h_(s'), `gap-fc-max.md` 5.2 (i)). Let gam: (0, 1/beta) -> [0, infinity) be piecewise continuous with Var_(nu_s)(phi) <= (1/gam_s) integral |grad phi|^2 d nu_s for gauge-invariant phi in C^1 with bounded gradient (the hypothesis of (BR-gap)). The first excited state f_1 is continuous, since P has a continuous kernel.

(a) *Energy bound.* For every 0 < eps < 1/(2 beta): integral over [eps, 1/beta - eps] of E_(nu_s) |grad u_s|^2 ds <= ||f||_2^2 - ||P f||_2^2 = <f, (1 - P^2) f>_nu.

(b) *Cap.* (1/2) integral over (0, 1/beta) of gam_s ds <= (e^(2 E_1) - 1)/2. With (BR-gap), E_1 >= (1/2) integral of gam_s ds: the integrated bridge Poincare constant equals the gap up to the factor (e^(2 E_1) - 1)/(2 E_1).

(c) *Consequence for Theorem BR.* alpha_s <= gam_s (a log-Sobolev inequality gives the Poincare inequality with the same constant: put phi = 1 + t g and let t -> 0; RECALLED, classical). So A/2 <= (e^(2 E_1) - 1)/2, and also A/2 <= (1/(2 beta_0)) sup_s alpha_s.

Proof. (a) Step (ii) of Theorem BR with q = 2 constant: F(s) := integral u_s^2 d nu_s has F' = integral |grad u_s|^2 d nu_s. Step (iv), Jensen at the two ends with q = p = 2: F(eps) >= ||u_0||^2_(L^2(nu)) = ||P f||_2^2 and F(1/beta - eps) <= ||f||_2^2. Subtract.
(b) Take f = f_1, the first excited state, of mean zero and norm one. The mean of u_s under nu_s is the mean of f (the kernels of step (iv) map nu_s to nu). F is non-decreasing, so Var_(nu_s)(u_s) = F(s) >= F(eps) >= ||P f_1||^2 = e^(-2 E_1). Hence E_(nu_s) |grad u_s|^2 >= gam_s e^(-2 E_1). Integrate, use (a): e^(-2 E_1) integral of gam_s ds <= 1 - e^(-2 E_1). Let eps -> 0. QED

Reading. Along a family with E_1 = M a_iota the average over s of gam_s is at most 2 beta_0 M a_iota (1 + o(1)), and (HC-phys) needs the average of alpha_s to be at least 2 beta_0 M_H a_iota. So **the bridge constants are of the order beta_0 a_iota times a physical mass, with the bare coupling beta_0.** The number 1/beta_0 is the length of the bridge. This is exact; no renormalised coupling enters.

Hand check in one Gaussian mode (`gap-fc-max.md` 5.4): gam_s = c/(1 + c s) + c/(1 + c s'), the integral of gam_s over (0, 1/beta) is 2 omega, and E_1 = omega. (b) reads omega <= (e^(2 omega) - 1)/2, true, and sharp as omega -> 0. In the proof, e^(-2 omega) 2 omega <= 1 - e^(-2 omega) is the same inequality.

### 3.1 The tests

| # | Test | Verdict | Reason (by hand) |
|---|---|---|---|
| T1a | Free photon: fails through the rate only | PASS | (P1)-(P3) hold exactly (Gaussian levels, no window needed). Level by level the slice covariance is the sum over levels of R_0 D_k C_k D_k^T R_0^T (R_0 the restriction to the slice, D_k the map from the level-k fluctuation to the fine field, C_k its covariance), and the sum has no last term: there is no unit. The rate is the lowest mode energy pi a/ell, not uniform in ell. Nothing else fails. |
| T1b | Compact U(1): fails through the rate only | PASS | At weak coupling the coupling does not run, so first passage never occurs and the family "first-passage data" is empty. The small-field port holds at every level. The route claims nothing. What U(1) lacks is the unit, that is the rate. |
| T2 | Weights w_p of row 720 (M3) | The port alone FAILS it, as it must; the unit inequality has to carry it | (P1)-(P3) read the quadratic form at the identity and a small-field window. They hold for w_p at the coupling beta_W = p beta/2 as for the Wilson weight. At beta_t(p) two phases coexist (row 720, THM GIVEN van Enter and Shlosman), so no rate exists there. So no statement that follows from (P1)-(P3) and "the coupling at the unit is of order one" can be true. The unit-scale inequality must be stated for the actual effective weight, with a hypothesis that is false for w_p at beta_t(p). Step 4 states it so. |
| T3 | Per-scale loss: exact at one loop, or a power of log(1/a) | **FAIL for the port as posed, by one power of log(1/a_iota)** (ARGUED; the exact half is Lemma CAP) | Needed (Lemma CAP): sup_s alpha_s >= 2 beta_0 M_H a_iota, bare beta_0. Given by the port: stiffness a_- beta_k at level k in the level-k link metric (P2), running beta_k. Linear count: one level-k bond moves L^(3k) fine slice links by L^(-k) each, so ||R_0 D_k||^2 is of order L^k. A level-by-level bound (Step 4, Lemma TEL) then gives 1/alpha of order the sum over k of L^k/(a_- beta_k), dominated by k = K: alpha of order a_- beta_K a/l_unit. Rate A/2 <= alpha/(2 beta_0) of order (beta_K/beta_0)(a/l_unit). With beta_0 = beta_K + b_0 log(l_unit/a) (one loop) the factor beta_K/beta_0 tends to 0 like 1/log(1/a_iota). Benchmark: a Gaussian field with independent levels of stiffness beta_k satisfies (P1)-(P3) and has exactly this slice precision. So no argument from (P1)-(P3) alone gives more. The true slice law is tighter than the benchmark by the factor beta_0/beta_K (if the gap holds; Lemma CAP), and this comes from the transfer structure: the time-like coupling of two slices is the bare beta_0 at every scale. |
| T4 | Square-root test of row 978, 5.7 | PASS for the level-by-level form; FAIL for a one-shot four-dimensional constant | A scalar constant for the four-dimensional law gives the rate (M a)^2/2 (5.7). The sum over levels of R_0 D_k C_k D_k^T R_0^T has norm of order L^K/(a_- beta), linear in l_unit/a. So the square root appears when each level is used once with its own response map. This names the form: entropy telescoped over levels (Lemma TEL). |
| T5 | Row 977, Theorem D2: no supremum over tilts above beta about 1.07 | Binds at the unit; below the unit the supremum is over small-field backgrounds only | (P1) is uniform over "each real background configuration of the step", inside the small-field domain. The pinned sheets of D2 are large-field data at the level of the sheet. At the unit the coupling is in the account's window, far above 1.07: the unit inequality must be on the actual kernels or on flow-weighted data. |
| T6 | Row 975, Lemma META: name a transience input | Named, not derived: (TR-LF) below the unit; at the unit it is part of the crux | An entropy inequality does not pass through a mixture over large-field regions for free. (TR-LF): a large-field event of level k at time 0 has left the chain after a time of order L^k steps (its energy is of order 1/L^k per step). The account bounds the probability of such events per unit of four-dimensional volume; a decay in time of their indicator under P is not in the text read (OPEN, a port question). At the unit the metastable sets are the ties of row 970. |
| T7 | Frozen Q_8 and 2T | PASS, vacuous | No Lie algebra, no small-field Gaussian level, no bridge gradient. The port does not apply and the route claims nothing. |
| T8 | K7 (mixed weight) | As T2 | On the tail beta_F -> infinity the port sees the quadratic form only. K7 binds a unit inequality claimed for every action with a given quadratic form. |
| T9 | FT-FK (an argument on the kinetic kernel only fails FT-U1 and SMALL-BOX) | PASS | Lemma CAP uses the kinetic kernel only and claims no rate. Every rate here comes from the unit inequality, which reads the whole weight. |
| T10 | SMALL-BOX | Consistent | The cube has a fixed large physical side 2 ell; (SIZE-phys) of row 978 fails for small ell, as it must. |

### 3.2 What the tests decide

1. **The port does not feed (LSI-br) at a cutoff-uniform rate (T3).** It is short by beta_K/beta_0. The loss is not in the constants a_-, a_+: it is the difference between the stiffness of a four-dimensional block field (running) and the time-like coupling of two fine slices (bare). A proof of (HC-phys) on the fine lattice must use an identity of the transfer structure at every level, not a convexity bound.
2. The level-by-level form passes the square-root test (T4), and fails through the rate only in the abelian models (T1).
3. Everything specific to SU(2) and to the Wilson class sits in the unit inequality (T2, T5, T6, T8).

So the direction is: do not ask the sub-unit levels for convexity in the fine metric. Ask them only for what is exact under the block map, and put the whole inequality at the unit. Step 4 does this.

### 3.3 Lemma TEL (the level-by-level count behind T3 and T4). PROVED for independent levels, given the tensorisation of entropy (RECALLED, classical)

Let A_0, ..., A_K be independent, A_k in R^(n_k) with law mu_k, and Ent_(mu_k)(phi^2) <= (2/rho_k) integral |grad phi|^2 d mu_k. Let D_k: R^(n_k) -> R^N be linear and Y := sum over k of D_k A_k. Then for every C^1 function f on R^N with bounded gradient:

  Ent(f(Y)^2) <= 2 E <grad f(Y), (sum over k of D_k D_k^T/rho_k) grad f(Y)> <= 2 ||sum over k of D_k D_k^T/rho_k|| E |grad f(Y)|^2.

Proof. For the product law, Ent(g^2) <= sum over k of (2/rho_k) E |grad_(A_k) g|^2 (sub-additivity of entropy over independent coordinates). Put g = f(Y); grad_(A_k) g = D_k^T grad f(Y). QED

Use. With rho_k = a_- beta_k (P2, P3 with the Bakry-Emery constant) and D_k D_k^T of norm of order L^k on the slice, the law of Y has a log-Sobolev constant at least 1/||sum D_k D_k^T/rho_k||, of order a_- beta_K L^(-K). For Gaussian levels with precision at most a_+ beta_k the covariance of Y is at least sum D_k D_k^T/(a_+ beta_k), so the constant is at most a_+ beta_K L^(-K) times a number: the count is sharp in the benchmark. (That ||R_0 D_k||^2 is of order L^k is the linear count of T3; the account's kernel bounds for the minimisers were not read. ARGUED.) For dependent levels there is one more term, the covariance of f^2 with the score of the finer levels; it is not needed, since the route fails T3 already in the benchmark.

**Why the true slice law can be tighter than the benchmark (ARGUED, one paragraph).** Lemma CAP says: Var_nu(f)(1 - e^(-2 E_1)) is at most the bridge energy of f, which carries 1/beta_0. For a gauge-invariant f that lives at the unit scale and has variance of order one this forces a fine gradient with |grad f|^2 of order beta_0 a M, not beta_K a M: larger than the linear count by beta_0/beta_K. The gradient of such an f is rough: it is a smooth kernel times adjoint rotations by the fine holonomies, and its projection on the smooth response D_K is smaller than its norm by a factor that is a product over the levels below K of (1 - c g_k^2). That product is a power of beta_K/beta_0. Lemma CAP fixes the power at one for the functions that saturate the gap. So a proof on the fine lattice needs the exponent exactly: this is the "exact at one loop" of fact test T3. I do not attempt it.

## Step 4. The inequality left at the unit scale

### 4.1 What is exact below the unit

(EX) *Invariance of torus partition functions.* A block map with a normalised kernel leaves Z(B x t) unchanged for every torus on which it is defined (row 978, A1; PROVED there in one line). So

  X_iota(t; B) = log Z_iota(B x t) - t lim over t' of (1/t') log Z_iota(B x t')

is the same number for the fine weight and for the unit-scale effective weight on the blocked torus. No metric and no fine variable occurs in X.

(PQ-EX), a port question that stays OPEN here: the account builds its effective weights on tori with four equal sides l = 2 L^m (outline 21521-21532, quoted in row 978 Step 7 from row 720). X needs the slabs B x t with t different from the side of B, and t' -> infinity. Whether the account's steps apply to these tori with the same constants was not read.

(TH) is the start value of row 978, 5.2 and 5.7: X_iota(tau_0/a_iota; B) <= Theta(ell), from (APR) or from two-sided stability. It is the only other input from below the unit.

### 4.2 Three forms of the unit inequality, in decreasing strength

Let B be the cube of physical side 2 ell, E_0 = 0 < E_1 <= E_2 <= ... the energies of the gauge-invariant transfer operator on B (r_i = e^(-E_i)), and for real t > 0: S(t) = sum over i >= 1 of e^(-E_i t), X(t) = log(1 + S(t)), U(t) := -X'(t) = sum over i of E_i e^(-E_i t)/(1 + S(t)). U(t) is the mean energy of the box in its thermal state at inverse temperature t; X(t) + t U(t) is the entropy S_th(t) of that state.

- **(U1)** (HC-traj) in unit steps: ||P^(m T) g||_2 <= ||g||_(1 + e^(-2 alpha_* m)) for g = p_s(u, .), 2 s a_iota = tau_0, T = l_unit/a_iota fine steps per unit, all integers m >= 0, with alpha_* > 0 free of iota. This is (HC-phys) with M_H = alpha_*/l_unit, asked at whole units of time only.
- **(U2)** the decay that Lemma IHC returns: X(t + 2 m T) <= (1 - tanh(alpha_* m)) X(t) for t = tau_0/a_iota and all m.
- **(U3)** the entropy-energy form: there is kappa > 0, free of iota, with

  (UNIT-EE)_kappa   U(t) >= kappa a_iota X(t), that is S_th(t) <= (t + 1/(kappa a_iota)) U(t), for all real t in [tau_0/a_iota, ell/a_iota].

**Lemma EE (PROVED, by hand).** (a) (U1) gives (U2) (Lemma IHC of row 978, with P^T in place of P; its proof uses reversibility, Chapman-Kolmogorov, Holder and Jensen only). (b) (UNIT-EE)_kappa and (TH) give X(ell/a_iota) <= Theta e^(-kappa (ell - tau_0)). So (SEED-phys) holds as soon as kappa (ell - tau_0) >= log(Theta(ell)/log(1 + s_*)). (c) Conversely, X(t_1) = X(t_0) exp(-integral over [t_0, t_1] of U/X): the seed is exactly a lower bound on the integral of U/X. (d) Where S(t) <= 1: U(t)/X(t) >= E_1/2. So with t_c the first time with S(t_c) <= 1, X(t) <= (log 2) e^(-E_1 (t - t_c)/2) for t >= t_c.

Proof. (b), (c): X is C^1 and positive, (log X)' = -U/X. (d): X = log(1 + S) <= S, and U >= E_1 S/(1 + S) >= E_1 S/2. QED

**Lemma COUNT (PROVED, by hand): hypercontractivity is used only to count states.** Let N(E) be the number of i >= 0 with E_i <= E. (a) For every t: N(E) <= e^(t E)(1 + S(t)). (b) If X(t) <= 2 Theta e^(-M (t - tau)) for t >= tau (the conclusion of Corollary CU, lengths in lattice units), then for 0 < E <= 2 Theta M:

  log N(E) <= E tau + (E/M)(1 + log(2 Theta M/E)).

(c) For t >= t_c: S(t) <= e^(-E_1 (t - t_c)) S(t_c). (This is the step of Lemma Z of row 720.)

Proof. (a) Markov: N(E) e^(-t E) <= sum over i >= 0 of e^(-t E_i). (b) Put t = tau + (1/M) log(2 Theta M/E) >= tau in (a); then X(t) <= E/M. (c) Each term has e^(-E_i t) <= e^(-E_1 (t - t_c)) e^(-E_i t_c). QED

Reading of (b): E/M quanta, each with a phase space of order Theta M/E. It is the count of a gas of mass M in the box, with Theta in place of the volume. So **(HC-phys) with (TH) is, at the level of the thermal sum, the statement that the box has at most the states of a massive gas, up to energies of the order of the volume.** The gap alone does not give this (it gives (d) of Lemma EE only). This is what separates (HC-phys) from the gap, in a form with no metric.

### 4.3 The unit inequality as the crux lemma

**(UNIT).** For the family of first-passage data of the account, at one ell with kappa (ell - tau_0) >= log(Theta(ell)/log(1 + s_*)): (UNIT-EE)_kappa holds on the cube of physical side 2 ell, with kappa free of the cutoff. By (EX) it is a statement on the unit effective weights alone: the coupling there is in the account's window, of order one in the sense that no further scale is integrated, and the cube has (2 ell/l_unit)^3 unit cells.

Order of choice. The family and its unit; tau_0 = l and Theta(ell) from (TH); then kappa; then ell.

By Lemma EE (d) and Lemma COUNT (c), the seed follows from two halves (and (UNIT) holds beyond t_c with kappa a_iota = E_1/2): a gap M_1 on the cube, and a bounded thermal sum at one time t_c with t_c a_iota bounded. These are (Z-UNB) and (BDD-Delta) of row 720, Theorem ZD (named match, row 978 5.7). In the hypercontractive form (U1) it is (LSI-traj-seed) of row 970 for the unit effective action in place of the Wilson weight at 2.3 (named match). By T2 the statement must be false for the weights w_p at beta_t(p): there E_1 tends to 0 with the volume, so (d) fails, as it must.

## Steps 5 to 7. The attack on (UNIT), three routes

Each route is stated with its argument, the exact step where it fails, and what is left.

### Route 1 (Step 5). Theorem BR on the fine lattice, fed by the port: the route N2 posed

Plan. Telescope the entropy of a slice function over the levels (Lemma TEL), use the Bakry-Emery constant a_- beta_k of each small-field level (P2, P3), and add one log-Sobolev inequality for the unit level. Put the result in Theorem BR.

What holds. Lemma TEL in the benchmark. The square-root scaling (T4). Lemma CAP.

Where it fails, three places.

1. *The bare coupling (T3).* Theorem BR returns A/2 <= (1/(2 beta_0)) sup alpha_s (Lemma CAP (c)). The levels k <= K give 1/alpha at least of order L^K/(a_+ beta_K) in the benchmark. So the rate is at most of order (beta_K/beta_0)/l_unit in physical units, and it tends to 0 like 1/log(1/a_iota). Remark on size: the true mass is exponentially small in units of l_unit when the unit is at weak coupling, so this bound lies above the true mass until beta_0 is of order beta_K/(M l_unit). The failure is on the tail of the family. The tail is what (SEED-phys) reads (row 978, R3). Once the levels between the unit and the correlation length are counted as well, the loss against the true rate is the factor (stiffness at the correlation length)/beta_0, at every cutoff.
2. *No convexity at the unit level.* The level K, and every level between l_unit and the correlation length, has no small-field statement. A log-Sobolev constant rho_K for the four-dimensional unit law, free of the volume, is not in the account and is false for w_p at beta_t(p) (T2).
3. *Dependent levels and large fields.* The telescoping for dependent levels has a covariance term, and the mixture over large-field regions needs (TR-LF) (T6). Not reached.

What would repair place 1: the exponent of the roughness of the gradient, exactly one (paragraph after Lemma TEL). It is a statement on the non-Gaussian structure at every level, not a port. Left OPEN, not attacked further: place 2 stops the route in any case.

Verdict: FAILS at place 1 on the tail and at place 2 at every cutoff.

### Route 2 (Step 6). A functional inequality with no metric, for the chain in unit steps

Plan. Avoid the fine metric: use the form of the unit-step chain, E_c(phi) := <phi, (1 - P^(2T)) phi>_nu = (1/2) E |phi(U_0) - phi(U_(2T))|^2, and look for an inequality Ent_nu(phi^2) <= C E_c(phi) that gives (U1).

(a) *The plain form is false in every model (PROVED, two lines).* nu has no atoms. Take phi = 1_A/nu(A)^(1/2). Then Ent_nu(phi^2) = log(1/nu(A)), which is unbounded, and E_c(phi) <= ||phi||_2^2 = 1. So no inequality Ent_nu(phi^2) <= C E_c(phi) holds on L^2(nu), for any reversible chain on a space without atoms. Equivalently, the continuous-time semigroup e^(-tau (1 - P^(2T))) is at least e^(-tau) times the identity on non-negative functions, so it is bounded from L^p to L^q for no q > p.

(b) *Restricted to the trajectory class.* The functions p_s(u, .) have entropy at most X(2s) <= Theta, so (a) does not apply to them. But the step from a log-Sobolev inequality to hypercontractivity (Gross) differentiates along a flow and uses the inequality on powers of the evolved function. In discrete time there is no flow except the bridge of Theorem BR, and the bridge is in the fine metric: Route 1.

(c) *The exact dual form (RECALLED: Carlen and Cordero-Erausquin 2009, subadditivity of entropy and Brascamp-Lieb inequalities; not rebuilt).* E[F(U_0) G(U_m)] <= ||F||_p ||G||_p for all F, G is equivalent to: (1/p)(Ent_nu(rho_0) + Ent_nu(rho_m)) <= Ent_(J_m)(rho) for every density rho with respect to the two-slice law J_m, with marginal densities rho_0, rho_m. This has no metric and it can be stated for two slabs of unit-scale variables. It is equivalent to the two-function form of hypercontractivity, so it is a restatement of (U1), not a smaller statement. The passage from slabs of block variables back to fine slices needs the block variables of a slab to screen the fine past from the fine future; that holds only up to the decay of the fluctuation covariances (CA-II 83869), and L^p norms are not stable under such errors.

(d) *A remark that is exact (PROVED, one line).* 1 + S(2s) = integral of p_s(u, w)^2 nu(du) nu(dw), so X(2s) is the Renyi divergence of order 2 of the two-slice law J_s from the product nu x nu. (U2) says that this divergence contracts by 1 - tanh(alpha_* m) per m units of extra lag, from the one start J_s. It is a strong data-processing inequality for one divergence and one start law.

Where it fails: at (b). No functional inequality without a metric lies between (U1) and a log-Sobolev inequality. The only embedding of the chain in a flow is the fine bridge.

Verdict: FAILS; it returns (U1) or (U2) unchanged. What is left of it: the forms (c) and (d) as statements, for a later direct attack.

### Route 3 (Step 7). The entropy-energy form (U3), by a count of states

Plan. Prove (UNIT-EE) on [tau_0, ell] in three ranges. Cold range, S(t) <= 1: Lemma EE (d) gives it from the gap, with kappa a_iota = E_1/2. Hot end: U/X is of order 3/t for a gas of massless quanta (X of order |B|/t^3; RECALLED, Stefan-Boltzmann). Middle range: from the hot end down to t_c.

What holds. Lemma EE and Lemma COUNT. With them the seed needs exactly: (i) a gap M_1 on the cube; (ii) X(t_c; B) <= log 2 at a time t_c with ell - t_c >= (2/M_1) log((log 2)/log(1 + s_*)).

Where it fails: at (ii), the middle range. The start value Theta is of the order of the volume of the cube. The hot-end rate 3/t integrates to a power, X(t) <= X(tau_0)(tau_0/t)^3, which is not small at t = ell for the cube of side 2 ell. So (ii) needs the count of Lemma COUNT (b) with a mass: at most the states of a massive gas, for energies up to the order of the volume. The gap does not give this (it bounds the lowest state only). By Proposition Delta of row 709, in the form quoted in row 978, 5.7 (X(t; b^3) <= (b/t)^3 Delta(t^4) for b >= t; not re-read here): (ii) with t_c = ell/2 follows from Delta((ell/2)^4) <= (log 2)/64 on the symmetric torus of side ell/2, and then the seed needs M_1 ell >= 4 log((log 2)/log(1 + s_*)), about 32.6 at s_* = 1/5041; or the seed follows at once, with no gap, from Delta(ell^4) <= log(1 + s_*)/8. Both are (BDD-Delta) with (MONO-Delta) of row 720, Corollary MB1. **Named match: rows 720 and 727. I stop here and do not attack it** (rule 0a).

A crossed-channel identity, for the record (PROVED from the hypercubic symmetry of the torus partition function). With B' := (2n)^2 x t and mu_0(B') the top eigenvalue of its transfer operator, X'(.; B') its thermal sum: X(t; (2n)^3) = 2n log mu_0(B') - t log lambda_0((2n)^3) + X'(2n; B'). The seed quantity is a difference of two ground-state energies plus a thermal sum of the crossed channel at the longer time 2n. It moves the count to the box B' and does not remove it.

Verdict: FAILS at (ii); what is left is rows 720's open pair, (BDD-Delta) and (MONO-Delta), with the gap (Z-UNB).

### Where the attack stands

(UNIT) failed by three different routes: in the fine metric (Route 1), with no metric as a functional inequality (Route 2), and as a count of states (Route 3). Each stops at the same object: the thermal sum of the cube between the hot end and the cold range, at a coupling of order one. No counterexample to (UNIT) or to (HC-phys) was found: Lemma COUNT (b) agrees with a gas of mass M_H <= m_0++ in every regime that I can check by hand. The stop rule of the row is met.

What this changes in N2: the inequality left at the unit is not an inequality in the fine link metric. Forms (U2) and (U3) do not see the levels below the unit at all, so the loss of T3 does not occur in them. It occurs in any proof of (U1) through Theorem BR on the fine lattice, because A <= (1/beta_0) sup alpha_s (Lemma CAP (c)).

## Step 8. Verdicts, marks, what stays open, next step

### 8.1 Verdicts on the row

1. **Port question.** Below the unit the account's small-field statements give this and no more: each fluctuation law, given the coarser field, is uniformly log-concave on a convex product window, with a constant free of the level, in the Euclidean norm of the rescaled fluctuation variable (unscaled field g_k A). In the level-k link metric the constant is a_- beta_k. The lower form bound is a hypothesis that the account takes from Balaban's operator theorem (CA-II 80163-80172, 75164-75195, 81161-81190, 80039-80041). The account states no log-Sobolev, Poincare or hypercontractive inequality (CA-II 84184-84186; greps in `guide/lane982/SOURCES.md`).
2. **Can this feed (LSI-br)?** Not at a cutoff-uniform rate. Theorem BR needs bridge constants of order beta_0 a_iota M with the bare coupling (Lemma CAP, exact). The port has the running coupling beta_k. The level-by-level count (Lemma TEL) is short by beta_K/beta_0, one power of log(1/a_iota), on the tail of the family (T3, ARGUED). A fine-lattice proof needs an identity of the transfer structure at every level.
3. **The inequality left at the unit.** (UNIT): the entropy-energy inequality U(t) >= kappa a_iota X(t) for the thermal states of the cube, on the physical time interval [tau_0, ell]. It is a statement on torus partition functions, hence on the unit effective weights alone (given (EX) on slabs, port question PQ-EX). (HC-phys) in unit steps implies its integrated form (Lemma EE). With (TH), (HC-phys) is the count of a massive gas (Lemma COUNT (b)).
4. **The attack.** (UNIT) failed by three routes: fine metric, no metric, count of states. All three stop at the thermal sum of the cube between the hot end and the cold range. No counterexample was found.

Kind of result: a reading of the account (port answer); new implications inside this target's gap lane (Lemmas CAP, TEL, EE, COUNT); a direction verdict on N2. It is not a check of the account's proofs and not a correction of its text.

### 8.2 Marks

| Statement | Mark |
|---|---|
| Port answer (P1)-(P5), with the quoted lines | read from the text; quotes to be re-read by the checker |
| Lemma CAP (a), (b), (c) | PROVED given Theorem BR steps (ii), (iv) and (BR-gap); (c) uses the classical step from log-Sobolev to Poincare (RECALLED); not checked |
| Lemma TEL (independent levels) | PROVED given tensorisation of entropy (RECALLED, classical); not checked |
| T3 verdict (loss beta_K/beta_0) | ARGUED: the linear count of ||R_0 D_k||^2, the benchmark as a member of (P1)-(P3), and the Bakry-Emery constant on a convex window (RECALLED) are not rebuilt |
| Roughness exponent equal to one | ARGUED consequence of Lemma CAP if the gap holds; OPEN as a statement at each level |
| T1b (compact U(1): no first passage), T6 (TR-LF) | ARGUED; (TR-LF) OPEN, a port question |
| Lemma EE (a)-(d) | PROVED ((a) given Lemma IHC of row 978, unchecked there until row 981 reports) |
| Lemma COUNT (a)-(c) | PROVED |
| Route 2 (a): no log-Sobolev inequality for the form of 1 - P^(2T) on a space without atoms | PROVED |
| Route 2 (c): the dual entropy form | RECALLED (Carlen and Cordero-Erausquin 2009), not rebuilt, not used |
| Crossed-channel identity (Route 3) | PROVED given the hypercubic symmetry of the torus partition function |
| (EX) on slabs with unequal sides, for the account's weights (PQ-EX) | OPEN, port question |
| (UNIT), (HC-phys), (U1), (U2) | OPEN |
| (BDD-Delta), (MONO-Delta), (Z-UNB) of row 720; (LSI-traj-seed) of row 970 | OPEN, named matches, not attacked |

### 8.3 What this run did not cover

- CA-III and the outline were not opened. CA-I was only grepped. Proofs of the account were not read, only the statements quoted in Step 2.
- Balaban's operator theorem (CMP 95, 99b) was not read; `~/ym4d-papers` does not exist on this worker.
- The minimiser kernels D_k of the account were not read; the count ||R_0 D_k||^2 of order L^k is the linear count.
- Proposition Delta (row 709) and Theorem ZD (row 720) were used as quoted in row 978, not re-read.
- No numeric run. No GUIDE test was needed for a verdict.
- The telescoping for dependent levels and the large-field mixture were not written, because Route 1 fails before them.

### 8.4 Next step (each item is a complete brief)

**N1, check (another model, high effort).** Check line by line `library/gap-hcphys-max.md`: Lemma CAP (3.0), with the two end inequalities of Theorem BR (iv) at q = p = 2 and the claim Var_(nu_s)(u_s) = F(s) for a mean-zero f; Lemma TEL (3.3); Lemma EE and Lemma COUNT (4.2); Route 2 (a); the crossed-channel identity. Re-read the quoted lines of CA-II (list in `guide/lane982/SOURCES.md`) and say whether (P1)-(P4) state them faithfully. Verdict per statement. Moves: the direction verdict on N2.

**N2, for the lead (I may not edit other files).** Do not queue a proof of (LSI-br) on the fine lattice from the account's small-field convexity: it is short by beta_K/beta_0 (T3) and has no input at the unit (T2). In `gap-ladder-max.md` 8.4 N2, the statement to keep is (U1) or (U2) in unit steps, or (UNIT-EE); the levels below the unit enter through (EX) and (TH) only. Row 978's reduction and row 720's Theorem ZD meet at one object, the thermal sum of the cube between the hot end and the cold range (Lemma COUNT), so they are not two independent chances.

**N3, reading (Claude Opus 5.5, high; port, quotes only).** Two port questions. (PQ-EX): do the account's steps, as written, build the effective weight and keep Z on tori with unequal sides (a slab B x t with t different from the side of B, and t -> infinity for lambda_0), with the same constants? Start at the outline lines 21521-21532 and the CA statements they cite. (TR-LF): does the account bound the decay in time of a large-field indicator of level k, or only its probability per unit of four-dimensional volume? Quote file and line; answer yes, no, or not found with the greps used.

**N4, hand computation, optional (one observable, one loop).** Test of the roughness exponent of 3.3. Take one explicit gauge-invariant slice function f at block scale (the trace of a plaquette of once-blocked links, in the account's block average). Compute to one loop the two sides of Lemma CAP (a) with gam replaced by the actual ratio: E_nu |grad f|^2/(beta_0 Var_nu(f)) against 1 - (the spectral average of e^(-2E) in the state f Omega). Criteria before the computation: if the one-loop ratio shows the factor beta_0/beta_1 (one block step) with coefficient one, the mechanism is confirmed at one level and a fine-lattice identity is worth a direction row; if the coefficient differs from one, the paragraph after Lemma TEL is wrong and is withdrawn. It decides nothing on (UNIT).

**N5, for the rows at fixed coupling (968 to 977).** Lemma CAP (b) bounds what any bridge route can return: (1/2) integral of gam_s ds <= (e^(2 E_1) - 1)/2. Lemma COUNT (b) is a necessary condition for (HC-traj) with a start value: log N(E) <= E tau + (E/M)(1 + log(2 Theta M/E)). Both can be used as fact tests of a claimed rate.

RESULT: Row 982 (Claude Fable 5.2 max, Mac mini worker 3; author, checked by no one; no numeric run). Port answer: below the unit the account gives only conditional, four-dimensional, small-field uniform log-concavity of each fluctuation law, constant a_- in the Euclidean norm of the rescaled variable (a_- beta_k in the level-k link metric), with the form bound taken as a hypothesis from Balaban's operator theorem (CA-II 80163-80172, 75164-75195, 81161-81190); it states no log-Sobolev or hypercontractive inequality. PROVED by hand (unchecked): Lemma CAP (the bridge constants of Theorem BR must be of order beta_0 a M with the bare coupling; (1/2) integral gam_s ds <= (e^(2 E_1) - 1)/2), Lemma TEL (level-by-level log-Sobolev count, independent levels), Lemma EE ((HC-phys) in unit steps gives the entropy-energy form U >= kappa X, which is exactly what the seed reads), Lemma COUNT ((HC-phys) with (TH) is the state count of a massive gas), Route 2 (a) (no metric-free log-Sobolev inequality for the unit-step chain). ARGUED: the port fed into Theorem BR is short by beta_K/beta_0, one power of log(1/a), on the tail (fact test T3 fails); the other tests pass or bind only the unit inequality. The crux lemma (UNIT) failed by three routes (fine metric, no metric, count of states), all at the thermal sum of the cube between the hot end and the cold range; no counterexample. OPEN: (UNIT), (HC-phys), the port questions (PQ-EX) and (TR-LF), the roughness exponent; named matches not attacked: (LSI-traj-seed) of row 970, (BDD-Delta), (MONO-Delta), (Z-UNB) of row 720. Next: N1 check; N2 the lead should not queue (LSI-br) from sub-unit convexity; N3 port reading of (PQ-EX) and (TR-LF).

