lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T11:15Z

# tail-two-step-c: blind two-step kill test of the tail induction, independent side

Pinned at commit c0e57d701 (working tree of branch claude/ym4d-hard-route). Finished. Nothing here is a status claim.

Provenance: Anthropic claude-opus-5-5, max effort, Mac mini worker; working tree at `c0e57d701`. Same model as the attempt, so this is not independent in model and it is not an audit. Side: independent, blind to `library/tail-two-step.md`. All references below are to `parts/hard-core--independent.md` unless named.

## Verdict

No counterexample to any conclusion was found. The route is not killed. Closure as written fails at two coefficients and one rate, each with a repair proposed here and not proved.

| Falsifier of the item | Source-free | One source insertion |
|---|---|---|
| g-dependent near region | **not found.** Rough sets and anchors are g-free; a reach of order log(1 / g) occurs only in a double-exponentially small tail (Section 4) | not found: the chart reads no f |
| Budget spent twice | **not found.** At most 19/48 of the 1/2 is used, once (Section 3) | not found: at most 11/24 used, margin 1/24 (Section 6) |
| Coefficient without the contraction | **found as written, D1:** the block-scale part of the marginal form. Conclusion believed true, by a different argument | **found as written, D2:** the variable-source part of the marginal R form has no clause that gives its factor a_k |

| Statement | Verdict (steers research, grants no status) |
|---|---|
| (BANACH), Lemma 4.7c in the norm of (TAIL) | ADVANCE: every far-field and site monomial is contracted at the level of the steps, with D5 local and its repair in hand |
| (ONE) | ADVANCE at regular W; one line missing at W with a far hole, D6 |
| (GROUP), (CRUDE), Lemma 4.7j on the shared label | ADVANCE, with the anchor of the tree read as in D7 |
| Recursion for cc_k, the factor L^{-a} on the quadratic remainder | CORRECT-NO-ADVANCE: the reason given does not give the factor, D1 |
| Weight exp(-kappa (|Y| - C_0)_+) of I(k + 1)(c) for all outputs but term (2) | CORRECT-NO-ADVANCE: rates do not match as written, D3 |
| Lemma 6.4f (v), R sector at variable f | CORRECT-NO-ADVANCE: the size used has no source in I^f(k), D2. A model family obeying (c^f) violates the inference |
| Lemma 6.4e for C_{k+1}, and (VS) through term (2) | CORRECT-NO-ADVANCE: the insertion argument does not apply to (ONE), D4 |

## 0. What was read

Read: `FINISH.md`, `GOAL.md`; of `parts/hard-core--independent.md` the state of attack, Obligations, Requests, Texts 3.1 to 3.3, 4.5j, the tree norm, 4.5k, the head of 4.6, 4.7, 4.8, 4.9, 6.0 to 6.4f, 9.4, 11.1; of `parts/hard-core--independent--ct.md` the head and Section 2; `parts/hard-core--independent--good.md`, Section 11; `library/ultralocal_cluster_expansion.md` to line 100. Not read: `library/tail-two-step.md`, the mapped file, any gate, any other library file. The part file quotes gate verdicts in its own text, and those quotations are the only gate wording seen.

## 1. Frozen definitions at `c0e57d701`

| Name | Definition used here | Where |
|---|---|---|
| radius | rho_P(l) = min(rho_e, c' g exp(c_1 d(l, P))), d read off Rg(P) | (TAIL), Text 4.7 |
| norm | ||G||_P = sum_{alpha, Xi} prod_l rho_P(l)^{alpha_l} exp(c_3 tau_k(P; supp alpha, Xi)) |G_{alpha, Xi}| | (TAIL) |
| C growth | |C_k(Y; V)| <= cc_k exp(-kappa (|Y| - C_0)_+) (t_Y^2 + t_Y^3), and in the norm t_Y becomes max(t_Y, t_fl), t_fl = C_s L^{-2} c' Vol(Y)^{1/2} | (TAIL) |
| chart | b = 2^{-1/2} g P x, x = xi + s_tot, s_tot = s(W, xi') + s_J(W); at fixed x, V reads W only within R_P | (2C), (LOCAL) |
| near labels | NV(Z): labels a link of N_1(Z) reads through the chart; unsplit, law mu_i with the cut S_i = 1[|x_i| <= p_2] | (R2), (3S) |
| rough set | Rg gains image(N_1(Z)) + B(R_P^+), R_P^+ = R_P + rho_P / L + 1 | (R2) |
| group | components of: NV meet or N_1(Z) touch; U_q, A_q; tt_k = C(L, M) g_k^{-3} (bb_k + cc_k) | (GROUP) |
| far noise | alpha_q(c) = 32 C_row g / min rho_{U_q}(l); a_q(c) = alpha_q(c) max_i (|xi_i| + 1); Lg_q = { a_q > 1/4 } | Lemma 4.7j |
| linear term | term (2) = (N_good^Z / N_good) E^Z_W[e^{e_k} - 1] | (ONE) |
| contraction | ||Gamma - Gamma_1(0) - beta(e)(F_0^*(w), F_0^*(w))||_{Y'} <= C sup||e|| (t_#^3 + t_#^2 (D_e / L)^a) + ||Rem_B||_{Y'} | (BANACH) |
| recursion | bb_{k+1}, cc_{k+1} as displayed after "The recursion, with the weighted t" | Text 4.7 |

## 2. The example, written out

All labels in this section are mine, at the level of each step. A same-model read is not independent in model.

**Data at level k.** Write g := g_k, g' := g_{k+1}, y_k := bb_k + cc_k. Take two pieces e_a of C_k(Y_a), a = 1, 2, each Y_a one level-k cube, with rough sets Z_a, in a term with Bad empty and T empty. W_0 is real. One far variable w_* sits on a level-(k+1) link c_*, off N_1(R), at d_* := d'(c_*, R), with |w_*| <= rho_R(c_*). One site U'_* has two states and lies at coarse distance D_* >= r_2 M from the output, with its refined site U_* at level k, as in Step 5 of Lemma 4.5k.

**The shared label** i_0 lies in chart cube c_0, with real noise t := x_{i_0} - s_tot,i_0(0) and v := |t|. It is read in x, law mu_i, cut |x_{i_0}| <= p_2, so |t| <= p_2 + |s_tot,i_0(0)| < 2 p_2. Two cases:

- **(A) near, near:** i_0 in NV(Z_1) and in NV(Z_2). One group q, U_q = N_1(Z_1) u N_1(Z_2).
- **(B) near, tail:** i_0 in NV(Z_1), not in NV(Z_2), c_0 off A_2, and a tail link l of Y_2 reads i_0 at level-k distance d_2 >= L R_loc from U_2. Two groups. If c_0 is in A_2 the label is part of the real base of e_2 and nothing is expanded, so that case reduces to (A) with no adjacency.

**Step k -> k + 1.** The Mayer factors give three outputs.

    T_a := (N_good^{Z_a} / N_good)(W) E^{Z_a}_W[ e^{e_a} - 1 ],     a = 1, 2,     (ONE)
    T_12 := the labelled monomials holding both factors.

In T_2 of case (B) the label i_0 is split, mu_i = mu^A + G. Its state A has |t| <= p, and its state G is a term with T not empty, outside this test. So i_0 reaches p_2 inside a tail only in T_12, because only there does the factor of Z_1 hold it unsplit.

**Step k + 1 -> k + 2.** Each output is an old polymer of level k + 1: e' := the remainder of T_1 after the extraction, with Y'_1, R'_1, and the output of T_12, with R' = R'_1 u R'_2. A new label at level k + 1, a new far variable and a new site go through the same three lines. Nothing from step 1 is carried except the function and its norm, so no label of level k is read twice.

## 3. Moving i_0 across its range: the Gaussian budget, summed once

Regimes, with A_2 := A_{q_2}(c_0) of Lemma 4.7j:

| Regime | Range of v | T_1 (linear in e_1) | T_12, case (A) | T_12, case (B) |
|---|---|---|---|---|
| I | v <= p_3 = C(L) p | main term of (BANACH) | (CRUDE), no noise used | series, factor 4 a_2(c_0) if c_0 in X_2 |
| II | p_3 < v <= min(A_2, 2 p_2) | Rem_B, exp(-p^2 / 3) | same | same as I |
| III | A_2 < v < 2 p_2, empty unless A_2 < 2 p_2 | Rem_B | same | c_0 in Lg_2, factor 2, hull chi_2(c_0) |

Everything that reads the Gaussian of i_0, per unit of v^2 in the exponent. The full budget is 1/2.

| Reader | Cost | Source |
|---|---|---|
| Rows of the action and of the old analytic polymers | q <= 1/16, once, on the whole family | (FAM) |
| Mean moved by w_* and s_* | linear: a sqrt(3) v + 3 a^2 / 2, a <= 1 / (8 n_v) | (DENS-MAJ), (R-MAJ) |
| Number of groups reading i_0, and their hulls | at most v^2 / 12, and only for v >= A_sharp | Lemma 4.7j (d) |
| C factors in T_12 | none: (CRUDE) is a sup over real fields | (CRUDE) |
| C factor in T_a | polynomial: sixth moment by Cauchy-Schwarz against the tilt, same order P(M) | "With growth" |
| Left for integrability | at least 1/4 + 5/48 | |

Sum: 1/16 + 1/12 + 1/4 = 19/48 < 1/2. **No item uses the Gaussian of i_0 a second time, and no moment of a C factor is taken in T_12, so there is no joint moment.** The label's Gaussian at level k is never read again at level k + 1: the noise of step 2 is new. No budget is spent twice. Arithmetic is in `checks/tail2c/budget_arith.py`.

## 4. Output support

Rough sets obey r_{k+1} <= (r_k + 1) / L + R_P^+ in the thickness, so r_k tends to at most (L R_P^+ + 1) / (L - 1), free of g. A born radius r_2 M shrinks by L per level down to that value, and until it does its polymer has more than L / M cubes and is paid by its weight, not by the contraction.

| Output | Support | Rough set | g-free? |
|---|---|---|---|
| T_a | bricks meeting image(N_{r_e}(Y_a)) + B(R_P^+), m <= 16 | image(N_1(Z_a)) + B(R_P^+) | yes |
| T_12 (A) | union of the two, touching | union | yes |
| T_12 (B), c_0 not in X_2 | not connected through i_0: the reset removes it | - | - |
| T_12 (B), c_0 in X_2 | A_1 u A_2 u hull, chi_2(c_0) cubes | union; the hull is a tendril, not rough | see below |

Quantities that do depend on g, and why none is a near region:

- r' of Lemma 4.7c is inside a proof. It reads no support.
- D_cap only sets where a gauge function vanishes.
- r_2 is the distance below which a site is near data. A site that close is a bad cube in the collar, which is outside this test, and the collar then pays per cube.
- The reach d(v) = rho_P + (1 / c_1) log(128 C_row (v + 1) / c') in case (B), regime III, can be of order log(1 / g). A hull of chi cubes needs v >= (c' / (256 C_row)) exp(c_1 M L chi), so its weight is at most exp(-v^2 / 4), double exponentially small in chi, against exp(-kappa chi). So it is a tail, with a range that needs no g in any constant.

**No g-dependent near region appears.**

## 5. The linear old factor in the full far-variable norm

Let Gamma(w, s) := E^{Z_1}_{exp(i w) W_0[s]}[e_1], t_# := max(t(W_0), t_fl). Every monomial class, with the term that bounds it. Rows are given at the size that each step supplies.

| Monomial | Source | Bound in ||.||_{Y'} | Contraction |
|---|---|---|---|
| 1 | vacuum | Gamma_1(0) | cancels exactly |
| w, degree 1, flat W_0 | density | 0 | colour |
| w, degree 1, W_0 not flat | density | C sup||e|| t(W_0) t_* with t_* <= t_fl exp(-3 c_1 max(d_*, R_P^+)) | extracted in beta; remainder has (D_e / L)^a |
| w, degree 2 | density, form through s | beta(e)(F_0^*(w), F_0^*(w)) + C sup||e|| t_#^2 (D_e / L)^a | the block average goes to the coupling; the rest has (D_e / L)^a on the polymer, and the block sum of the forms is D1 |
| degree >= 3 in zeta | Cauchy on |zeta| <= c / t_# | C sup||e|| t_#^3 | t_# |
| w off the zone, through the tail of e | a_l <= L^{-A} rho_Y(l) | C L^{-A} sup||e|| t_#^2 | L^{-A} |
| w^> at d' > r' | density, kernels, H^# | C(L, M) sup||e|| g^eta | g^eta |
| s_* | density; H^# at rate c_3; tail of e | C sup||e|| ( t_S^2 + t(W_0) t_S + H_0 + exp(-c_3 (L - 1) D_*) ) | t_S is below g^C; H_0 below g^eta |
| s_* w_* | same | that times t_# / c | same |

Here t_S := C_s L^{-2} C(L) eps_0 exp(-c_K D_*) Vol(Z)^{1/2} / g. Sum over the old Y of a given Y', with n < 170 cubes, so at most L^4 80^{338} of them, and use t <= C_s L^{-2} t' (g' / g) (Vol(Z) / Vol(Y'))^{1/2}. Then, **given the repair of D1**,

    sum_{Y -> Y'} ||Gamma_Y - Gamma_{Y, 1}(0) - beta_Y||_{Y'}  <=  C P(M) y_k [ (M / L)^a t'^2 + L^{-2} t'^3 ]  +  C P(M) Vol(Z) c'^2 (M / L)^a y_k  +  C(L, M) ( g^eta + p exp(-c_3 T_{k+1} / 8) + exp(-p^2 / 3) ) y_k,        (TWO-1)

with C absolute, P(M) = Vol(Z)^{3/2} (log Vol(Z))^{3/2}. The floor t_fl does not carry the L^{-2} of t, so it cannot be merged with t': its term is the middle one, C P(M) Vol(Z) c'^2 (M / L)^a y_k, and it goes to bb_{k+1}. Its constant is the absolute C of (BANACH), so it needs c' only for t_fl <= c. So in the source-free case, **given D1, every coefficient of the linear old factor carries a contraction: L^{-a} up to powers of M on the second-order remainder, L^{-2} on the third, and g^eta on everything that reads a far state or a site.** That is the recursion of Text 4.7, and it rests on the inputs named in Section 8. Without D1 the second-order line is not derived.

**Step 2.** Apply (TWO-1) at level k + 1 to e', whose norm at a real base is the left side of (TWO-1):

    y_{k+2} contribution  <=  ( C P(M) (M / L)^a )^2 y_k  +  [ C(L, M) (g_{k+1}^eta + ...) ] C P(M) (M / L)^a y_k + ...        (TWO-2)

Nothing compounds. R' has thickness (R_P^+ + 1) / L + R_P^+, the anchor stays g-free by (WALL), and the floor t'_fl is the same number, so it enters each step once, in bb.

**T_12.** Case (A): by (CRUDE) and (GROUP), ||z||_{Y, R} <= tt_k^{3/2} e^{n_x}, n_x <= 32. Case (B), with c_0 in X_2:

    E[ ||Phi_2^{[{c_0}]}|| ]  <=  C ||Phi_2||_bd [ alpha_2(c_0) exp(-(kappa_G / 2) chi_2(c_0)) + exp(-A_2^2 / 4) ],

and T_12 has at most tt_k^2 exp(kappa C_0) times this, which is at most y_k^{5/4} after the weight of Section 4. No contraction is asked of it. The tree in Lemma 4.7j (b) should be read from the old support P, not from A_q: a link that reads c can lie in A_q, with tau_k(A_q; .) = 0, but tau_k(P; .) >= L R_loc, and c_3 L R_loc >= kappa_G. With that reading (b) holds.

## 6. The same two steps with one source

f in FF_k enters through exp(I^f), I^f := S^{omega_k}(V(b)) - S^{omega_k}(V^*), and the insertion is a first-order D_u, u Lipschitz, Lip(u) <= 4 Lam.

- **Support.** Nothing in the chart reads f (6.3), so Section 4 stands as it is.
- **Budget.** ||exp I^f|| <= exp(C(L) rho g^2 v^2 + C(L) Lam a_k g Phi^w v). With rho g^2 C(L) <= 1/16 the table of Section 3 sums to 1/16 + 1/16 + 1/12 + 1/4 = 11/24, and the linear term goes in the remaining 1/24. It is spent once.
- **Far norm at constant source.** Gamma^{[c]} has the rows of Section 5: density 1 + small on good variables, and Gamma_1'(0) = 0 by colour at any c. So (TWO-1) holds at each c, given D1, and the marginal part goes into rho^R_k[c].
- **Far norm at variable f.** Two things fail, D2 and D4.

**The quadratic coefficient at variable f.** Put y the base of Y and c := f(y). Term (2) has second-order coefficient beta(e_Y^f), and the extraction subtracts the value at c. So what stays is

    R^f(W) := sum_Y [ beta(e_Y^f) - beta(e_Y^{[f(y)]}) ](F_0^*, F_0^*),

marginal, so with no factor L^{-a}. Lemma 6.4f (v) sizes it at C y_k P(M) g^{-2} a_{k + 1} Lip. Nothing in I^f(k) gives the factor a_{k + 1} Lip:

- (c^f) has size clauses and (SENS). (SENS) reads u at distance d with a factor A_s exp(-c_s d), so at d = 0 it has no gain.
- Cauchy in s on f + s (f - f(y)) has |s| of order 1, because the Lipschitz margin of FF_k is of order Lam whatever the sup of the direction is.
- (G3) is a clause on analytic polymers only.

*Model of the failure.* Let y_1, y_2 be neighbouring sites of Y at spacing a_k, let e be any R polymer, and put e^f := e (1 + (1/4) sin( (f(y_1) - f(y_2)) / (3 Lam a_k) )). It is entire in f, on FF_k its modulus is at most e (1 + sinh(1) / 4) < (4/3) e, and it reads f only on Y, so it meets every clause of (c^f), (SENS) included, up to the factor 4/3. At f of constant gradient its relative distance from e^{[f(y)]} is (1/4) sin(1/3) for every Y. So the coefficient of F^2 in R^f is of order y_k P(M) g^{-2}, with no a_k and no L^{-a}. This is a model of the inference, not of Yang-Mills.

*Why that is fatal if left.* (G1) at level k + 1 asks Lam a_{k + 1} g^2 p^{c_p}, and a_{k + 1} is exponentially small in K - k, while y_k, the size the induction carries, is of the order of bb^new_k, only quasi-polynomially small in K - k. Put in C_{k + 1} instead, R^f gives the bound cc_{k + 1} >= C P(M) y_k, with no contraction.

**The far insertion.** Lemma 6.4e inserts s D_u only for X in Y', and says that e(Y', R) is a power series in the activities in Y'. Term (2) is not: (ONE) has summed all hulls into one function, so

    D_u E^{Z, f}_W[e^f]  =  E^{Z, f}_W[D_u e^f]  +  Cov^{Z, f}_W( e^f ; S^{c_k' (f) u} + D_u EE^{an, f}_k ),

and the covariance reads supp u, off Y', through xi'. In a Gaussian toy with strictly local noise and a shared xi', it is 2 C(a, b)^2 for e = phi_a^2 and the density phi_b^2, not zero, and an insertion on X in Y' gives zero for it. At |s| = s_0 the unrestricted insertion would leave the gas near supp u. So the Cauchy argument at radius s_0 does not reach this term.

## 7. Defects, ranked by what each breaks

**D1. The quadratic remainder of the linear old factor (Text 4.7, the bracket after "Marginal part", line 1020).** The text: beta~ is the block average of beta(e), and "the rest is a form of mean zero over the block, against a field smooth at scale L, so it gains the same L^{-a}". Mean zero over a block of side L gains nothing against a field that varies at scale L, and F^* does, for W rough at its own scale: |F^*(x) - F^*(x')| is of order (|x - x'| / L)^a L^{-2} sup |F'|, with no gain at |x - x'| of order L. Take b(x) = b~ (1 + psi(x / L)), psi of mean zero, and F^*(x) = L^{-2} F_0 phi(x / L). Then the sum over a block of (b(x) - b~) |F^*(x)|^2 is b~ F_0^2 times the integral of psi phi^2, with no power of L. Text 11.1, Step 6, records the same effect, and it escapes because its family is covariant, which term (2) is not. *What breaks:* the factor L^{-a} on t'^2 in cc_{k + 1}, as derived. With no factor the recursion reads cc_{k + 1} >= C P(M) y_k and does not contract.

*Repair, unproved.* Split b - b~ into a part oscillating at scales M, P, where mean zero does gain (M / L)^a, and a block-scale part, which must be small by itself. The position enters only through the law on Z. After xi' is integrated the Gaussian part is exactly N(0, g^2 C), with C = C^0 - l N l^T, C^0 the covariance with no constraint of this step, l the lift, N := Q C^0 Q^T the covariance of the coarse field. So with T the compression of l N l^T relative to C^0_ZZ, Tr T = E_N || lift |_Z ||_{Q^0}^2 <= C Vol(Z) L^{-4} (log), by the form bound of Lemma 4.7c and |F^*| <= C_s L^{-2} |F'|, and the two laws on Z differ in total variation by at most C Vol(Z)^{1/2} L^{-2}. So

    (POS-beta)   | beta_x(e)(F, F) - beta_inf(e)(F, F) | <= C sup |e| ( Vol(Z)^{1/2} L^{-2} + C(L, M) g^eta ) |F|^2 Vol(Z) / g^2,

with beta_inf free of the block position. [Alternative: 1.2 gives the unconstrained law as the mixture of the conditional laws over the level-(k + 1) measure, and Lemma 4.7c bounds the distance from the conditional law at W = 1 by E[t^2 + t^3].] This adds C P(M) M^2 L^{-2} to the coefficient of t'^2, better than L^{-a}. It has to be written with the non-Gaussian part and for the actual map, and it is not.

**D2. No gradient clause in the R sector (Lemma 6.4f (v), line 1236, against (c^f), line 1164).** Section 6. It breaks (G3) at level k + 1, so Theorem I^f as derived. *Repair, unproved.* Add to (c^f), for u with u(y) = 0, the relative clause

    (G3-R)   || D_u e^f ||  <=  (the bound of e^f at the same base) C_R a_k Lip(u) (1 + |P|)^2,     e in { z_k, B_k, C_k }.

It should close as Lemma 6.4d does. The pull-back is relative, so Lemma 4.7c keeps its contraction, and a_k = a_{k + 1} / L gains. The new covariance with D_u I^f has a factor Lip(u) a_k g^2 p^2, or a_k on direct links, by |S^u(V)| <= sup |u| F(V). The constant part u(y) goes by Cauchy in c on |c| <= 4 rho, and the rest by the margin Delta_k. Then R^f has the size Lemma 6.4f (v) states.

**D3. Rates (Text 4.7, "(FAMILY-WALL)", line 1014; Proposition 4.7i, line 859; stage (i) item 6, line 958; the library, line 86).** (FAMILY-WALL) says an attachment has exp(-kappa' a) "with kappa' above kappa by the room in the library". But kappa' := kappa_G / 8 = kappa / 2 in Proposition 4.7i and Lemma 4.7j, and the labelled library gives r_l = kappa / 4 - a_1 / 2 - 4 - log 2 from (EI) at rate kappa. So every output other than term (2) has rate about kappa / 4, and I(k + 1)(c) asks kappa: the bound fails once |Y'| is large against log(1 / bb_{k + 1}) / kappa. *Repair, unproved, either of two.* Give the R sector its own rate kappa_R := r_l, and ask kappa_G large enough for kappa_R >= log L, which is what (POS-WALL) reads; or run (FAM) at rate up to (3/2) kappa minus entropy, which it allows, and replace b / 2 in the labelled Claim by b - a_0, which its proof allows, so that r_l > kappa for kappa large (`checks/tail2c/budget_arith.py`).

**D4. (SENS) and (VS) through term (2) (Lemma 6.4e, lines 1221, 1227, against (ONE), line 980).** Section 6. *Repair, unproved.* Bound the covariance by the gas: the polymers joining Y and supp u carry exp(-r |Y''|), so rate r / M per coarse link, above c_s, and with Cauchy in zeta on Cov_{W_zeta} - Cov_1 the t-structure stays. The result is relative to the bound of C_{k + 1}, for L large against M.

**D5. (BANACH), step (4) (line 1010).** "The ratio to N_good^Z is the exponential of the polymers that meet d, by the library at fixed (v, xi_d^perp)". rho_d reads xi' through B'_Y, with no smallness, so it is not 1 + small over xi', and a modulus in xi' over the whole volume is exponentially bad at complex W. *Repair, in hand:* treat xi' off LY as far variables, as in "Stage (ii) with labels", with rho_d in the form norm (DENS-Q), and the library on xi' with this insertion. This asks C_9 >= C_s' Vol(Z)^{1/2} / c.

**D6. (ONE) at W with a far hole (line 980).** N_good has no direct cube, so E^Z_W[e] does not say what e reads on the refinement of a hole of W, and a hole of W has no vacuum state at fixed W. *Repair, in hand:* a strictly local reference state on the refinement, with the Mobius coefficient against it attached to the mandatory polymer. It has a factor exp(-c_3 L r_2 M).

**D7. Wording.** (a) Lemma 4.7g, line 829, has Y' contain the images of the supports. (TAIL) and Proposition 4.7i need w as a variable on tendrils, so read rough sets; the proof holds with Y' := R. (b) Lemma 4.7j (b) has tau_k(A_q; .), which vanishes for a link in A_q reading a cube next to A_q. Read the tree from P: tau_k(P; .) >= L R_loc, and c_3 L R_loc >= kappa_G.

## 8. What this rests on, and what is open

(TWO-1) and (TWO-2) are labelled **implication**. Their inputs, read here at the level of statement and proof sketch and not line by line: T_k <= T_* and Lemma 4.7f, (EI), the Holder bound of 9.4, the form bound of Lemma 4.7c, the envelopes of 3.1a. Those envelopes stay an input, as the file says. D1 to D4 are open: each repair above is a proposal. Not tested: terms with a bad cube or a label in state G, by the terms of the item; mandatory polymers; the top m_* levels; the second library with a mandatory part; Lemma 6.4c, (H1), (H2).

**Numerics.** One script, `checks/tail2c/budget_arith.py`, output `budget_arith.out`: exact arithmetic of the budget, of (MARGIN) and the half-weight inequality, of the two rate slopes and of the model's size, registered criteria in its docstring, PASS. Memory was 58 percent free, under the numeric lock. It tests arithmetic only, and nothing here rests on it.
