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

Setting of Theorem BR. For gauge-invariant continuous f let u_s be its bridge interpolant (u_s = N_s/h_(s'), `gap-fc-max.md` 5.2 (i)), and let gam_s be the best constant in Var_(nu_s)(phi) <= (1/gam_s) integral |grad phi|^2 d nu_s over gauge-invariant phi.

(a) *Energy bound.* For every 0 < eps < 1/(2 beta): integral over [eps, 1/beta - eps] of E_(nu_s) |grad u_s|^2 ds <= ||f||_2^2 - ||P f||_2^2 = <f, (1 - P^2) f>_nu.

(b) *Cap.* (1/2) integral over (0, 1/beta) of gam_s ds <= (e^(2 E_1) - 1)/2. With (BR-gap), E_1 >= (1/2) integral of gam_s ds: the integrated bridge Poincare constant equals the gap up to the factor (e^(2 E_1) - 1)/(2 E_1).

(c) *Consequence for Theorem BR.* alpha_s <= gam_s (a log-Sobolev inequality gives the Poincare inequality with the same constant: put phi = 1 + t g and let t -> 0; RECALLED, classical). So A/2 <= (e^(2 E_1) - 1)/2, and also A/2 <= (1/(2 beta_0)) sup_s alpha_s.

Proof. (a) Step (ii) of Theorem BR with q = 2 constant: F(s) := integral u_s^2 d nu_s has F' = integral |grad u_s|^2 d nu_s. Step (iv), Jensen at the two ends with q = p = 2: F(eps) >= ||u_0||^2_(L^2(nu)) = ||P f||_2^2 and F(1/beta - eps) <= ||f||_2^2. Subtract.
(b) Take f = f_1, the first excited state, of mean zero and norm one. The mean of u_s under nu_s is the mean of f (the kernels of step (iv) map nu_s to nu). F is non-decreasing, so Var_(nu_s)(u_s) = F(s) >= F(eps) >= ||P f_1||^2 = e^(-2 E_1). Hence E_(nu_s) |grad u_s|^2 >= gam_s e^(-2 E_1). Integrate, use (a): e^(-2 E_1) integral of gam_s ds <= 1 - e^(-2 E_1). Let eps -> 0. QED

Reading. Along a family with E_1 = M a_iota the average over s of gam_s is at most 2 beta_0 M a_iota (1 + o(1)), and (HC-phys) needs the average of alpha_s to be at least 2 beta_0 M_H a_iota. So **the bridge constants are of the order beta_0 a_iota times a physical mass, with the bare coupling beta_0.** The number 1/beta_0 is the length of the bridge. This is exact; no renormalised coupling enters.

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

