lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T11:15Z

# tail-two-step-c: blind two-step kill test of the tail induction, independent side

Pinned at commit c0e57d701 (working tree of branch claude/ym4d-hard-route). In progress; written section by section. Nothing here is a status claim.

Provenance: Anthropic claude-opus-5-5, max effort, Mac mini worker; working tree at `c0e57d701`. Same model as the attempt, so this is not independent in model and it is not an audit. Side: independent, blind to `library/tail-two-step.md`. All references below are to `parts/hard-core--independent.md` unless named.

## 0. What was read

Read: `FINISH.md`, `GOAL.md`, of `parts/hard-core--independent.md` the state of attack, Obligations, Requests, Texts 3.1 to 3.3, 4.5k, the head of 4.6, 4.7, 4.8, 6.0 to 6.4f. Later sections of this file name anything further. Not read: `library/tail-two-step.md`, the mapped file, any gate, any other library file except the four the firewall allows.

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
| w, degree 2 | density, form through s | beta(e)(F_0^*(w), F_0^*(w)) + C sup||e|| t_#^2 (D_e / L)^a | form goes to the coupling; the rest has (D_e / L)^a |
| degree >= 3 in zeta | Cauchy on |zeta| <= c / t_# | C sup||e|| t_#^3 | t_# |
| w off the zone, through the tail of e | a_l <= L^{-A} rho_Y(l) | C L^{-A} sup||e|| t_#^2 | L^{-A} |
| w^> at d' > r' | density, kernels, H^# | C(L, M) sup||e|| g^eta | g^eta |
| s_* | density; H^# at rate c_3; tail of e | C sup||e|| ( t_S^2 + t(W_0) t_S + H_0 + exp(-c_3 (L - 1) D_*) ) | t_S is below g^C; H_0 below g^eta |
| s_* w_* | same | that times t_# / c | same |

Here t_S := C_s L^{-2} C(L) eps_0 exp(-c_K D_*) Vol(Z)^{1/2} / g. Sum over the old Y of a given Y', with n < 170 cubes, so at most L^4 80^{338} of them, and use t <= C_s L^{-2} t' (g' / g) (Vol(Z) / Vol(Y'))^{1/2}. Then

    sum_{Y -> Y'} ||Gamma_Y - Gamma_{Y, 1}(0) - beta_Y||_{Y'}  <=  C P(M) y_k [ (M / L)^a t'^2 + L^{-2} t'^3 ]  +  C P(M) Vol(Z) c'^2 (M / L)^a y_k  +  C(L, M) ( g^eta + p exp(-c_3 T_{k+1} / 8) + exp(-p^2 / 3) ) y_k,        (TWO-1)

with C absolute, P(M) = Vol(Z)^{3/2} (log Vol(Z))^{3/2}. The floor t_fl does not carry the L^{-2} of t, so it cannot be merged with t': its term is the middle one, C P(M) Vol(Z) c'^2 (M / L)^a y_k, and it goes to bb_{k+1}. Its constant is the absolute C of (BANACH), so it needs c' only for t_fl <= c. So in the source-free case **every coefficient of the linear old factor carries a contraction: L^{-a} up to powers of M on the second-order remainder, L^{-2} on the third, and g^eta on everything that reads a far state or a site.** This is the recursion of Text 4.7, and it needs nothing beyond the inputs named in Section 8.

**Step 2.** Apply (TWO-1) at level k + 1 to e', whose norm at a real base is the left side of (TWO-1):

    y_{k+2} contribution  <=  ( C P(M) (M / L)^a )^2 y_k  +  [ C(L, M) (g_{k+1}^eta + ...) ] C P(M) (M / L)^a y_k + ...        (TWO-2)

Nothing compounds. R' has thickness (R_P^+ + 1) / L + R_P^+, the anchor stays g-free by (WALL), and the floor t'_fl is the same number, so it enters each step once, in bb.

**T_12.** Case (A): by (CRUDE) and (GROUP), ||z||_{Y, R} <= tt_k^{3/2} e^{n_x}, n_x <= 32. Case (B), with c_0 in X_2:

    E[ ||Phi_2^{[{c_0}]}|| ]  <=  C ||Phi_2||_bd [ alpha_2(c_0) exp(-(kappa_G / 2) chi_2(c_0)) + exp(-A_2^2 / 4) ],

and T_12 has at most tt_k^2 exp(kappa C_0) times this, which is at most y_k^{5/4} after the weight of Section 4. No contraction is asked of it. The tree in Lemma 4.7j (b) should be read from the old support P, not from A_q: a link that reads c can lie in A_q, with tau_k(A_q; .) = 0, but tau_k(P; .) >= L R_loc, and c_3 L R_loc >= kappa_G. With that reading (b) holds.

