lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T05:39Z

# Row 1406, gap-univk-pwc: the weight comparison (PW-C) of one good label on the common passing set

Started 2026-11-22T17:39Z (date -u). Pinned commit 45371abb5. Written by Claude Fable 5.2 (medium). Not yet checked by another model.

## 0. Plan

1. Read row 1404 (`library/gap-univk-pos2.md`) and check 1405 in full; restate (PW-C), (COMMON), P_h.
2. Repo search: grep open-core, FINISH rows for (PW-C), (COMMON), factor inventory.
3. Source reading: Y 129569-129680 (inventory, live-arrest charge), outline 5434-5464 (formation criterion), III 13106-13126, 13733-13739.
4. (COMMON) for the inner history spaces.
5. Factor-by-factor charge of log w^B - log w^A on P_h; first failing factor, if any.
6. If a charge fails: direct exponential-moment test (check 1405).
7. Result, next two rows.

Status: all steps done; see Sections 1 to 9.

Credit. The charts, labels, zones, loads, marks, the read split, the per-cell domination lemma, the factor inventory and the formation test are objects and statements of the complete account (CA-I, II, III), of YM4_1400.tex ("Y") and of the short outline YM4_sketch_500.tex ("O") by Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Theorems CAP and M are row 1404's, as corrected by check 1405. The formed-copy bound (5) with a volume charge and action pieces is the B4 note's (`library/b4-typed.md` L157-198), owner `b4-typed`, registry entries ZONE-FORM, ZONE-RESERVE, ZONE-CAPACITY (`library/open-registry.md` L543-545).

## 1. Statement and repo search

**(PW-C)** (row 1404, 6.1-6.2; check 1405 L29-31). For every good aligned label h, at every required real centre, on both tori, almost everywhere on P_h = S^A intersect S^B of a common resolution:
  | log w^B - log w^A | <= K l_k V + sum over recent zones b of K (k - b + 1) l_b n_b(h),
with l_b the load of zone b (III (9.1:eq-centre-normalisation-d)), n_b the number of level-b cells of zone b, V = N_w^4, and K free of h, the centre, the torus and the cutoff.

**Repo search.** `library/open-core.md`: zero hits for PW-C, zr-formation-test, "action reserve", "fractional action". FINISH rows with PW-C: 1404, 1405, 1406 only. The outline's formation test and its unrestricted-zone remark are on file in `library/b4-typed.md` L157-198 (cited there, not proved), `library/sa-histories.md` and check 1403. Check 1405 L5-8 ran the five-ref search for the comparison itself: no competing row. So the decision below is not on file. The formation estimate itself has an owner (ZONE-FORM) and is not redone here.

## 2. Sources read in this row

O = short outline at 31a47c543775 (32992 lines, fetched by URL into /tmp/ym4d-pwc-w2/src). I, II = parts I, II at the same revision (fetched, same folder). III and Y = the local copies.
- Y 129540-129700 (arguments of the production formula; bounds on the class discs; live arrests). Y 81910-81944 and 82000-82010, 82140-82147 (= O 5346-5401, 5434-5464): the formation test.
- O 5285-5470 (capacity, regular-zone channel, unrestricted bare zone, counterexample to carrier oscillation, sufficient structural bound).
- III 11845-12060 (normalisation, chart, labels, slots, classes, marks, loads); 13090-13130 (read split); 13338-13415 (per-cell domination, statement); 13615-13745 (resolved interpolation); 53950-53964 (x_(r) = theta_r - zeta_(r)).
- I 156837-156930 (positivity dichotomy, "Proof outstanding").
- This lane: row 1404 and check 1405 in full; `library/b4-typed.md` L150-200, 228-232; `library/gap-univk-log.md` Section 3 by grep (scalars, (RULE), (H4)).
Not read: the proofs of the per-cell domination lemma and of the resolved interpolation lemma; `library/c1-repr.md` and `library/pd.md` beyond what rows 1404 and 1405 quote.

## 3. (COMMON) at the leaf resolution (PROVED GIVEN three printed statements; unchecked)

**3.1 Which resolution.** III 11955-11960: "At the last lattice only the outermost stage of the assembly is present: no inner stage of the assembly remains open, and every piece entering the assembly is terminal, a leaf." So the resolution to use is the *leaf resolution*: the integration variables of the stop-level operation on the live components of h (the histories omega of T^w, I 156846-156852), with every healed inner piece kept as a stored number, not reopened. This answers check 1405 L29 ("Reopening a healed inner history can expose variations that have canceled in its stored, summed entry"): at the leaf resolution no healed history is reopened. Lemma RES of row 1404 allows any common resolution, so this choice is free.

**3.2 Lemma COM.** Fix a common aligned label h and a history omega of each live component. Assume
 (d1) the triple (Xi_omega, mu_omega, S_omega) is determined by (X, omega), k, g_0, ..., g_k and p (I 156907-156911; inside a proposition marked "Proof outstanding"; owner PD-REST);
 (SCAF) on the scaffold "every threshold, integer, partition and tree is read from theta_s. These are common to the two runs" (III 11932-11936);
 (CH) the chart substitution Psi_h^c is "a triangular bondwise right translation" that "preserves the product Haar measure" (III 11874-11879), and it acts on the retained variables only.
Then the two runs have one index set of histories and one measure space (Xi_h, mu_h^res) = (chart) x (product over live components of the disjoint union over omega of (Xi_omega, mu_omega)). It projects to the chart of III 11883-11886. The identification of the Lebesgue variables is the identity.
Proof. Xi_omega is a product of copies of the group and of real lines, indexed by bonds and sites that the partition, the trees and the integers of omega select. By (SCAF) these index data are the same for the two runs. mu_omega is the product of Haar and Lebesgue measures on that index set (I 156848-156849), so it is the same measure. By (CH) the pullback of each run by its own chart map does not change the product measure on the retained variables. QED

**3.3 What Lemma COM does not give.** It gives the space and the measure, not the sets. S_omega^A and S_omega^B can differ for two reasons. (i) A tested function can depend on the run (through a coupling or through the run's background). (ii) After the pullback, a test that reads retained variables is composed with a different chart map in each run. So P_h is in general a proper subset of both supports, as row 1404 assumed. The printed text fixes the thresholds only. Also not given: (d1) itself (owner PD-REST), and (FAC) at the leaf resolution (check 1405 L58: "Full (FAC) at the chosen resolution is an input").

**Verdict on (COMMON): HOLDS at the leaf resolution GIVEN (d1), (SCAF), (CH).** These are printed; (d1) is not proved there. No new obligation arises from (COMMON).

## 4. The factor inventory and the charge of each class (written 2026-11-22T17:45Z by date -u)

**4.0 Setting.** Leaf resolution of Section 3, a point xi of P_h, zero residual source, real centre. By (FAC) and the inventory of Y 129585-129600 ("the exponent consists of the raw Wilson term, the inner integrals' quadratic forms and source weights, and the normalization constants at each node, together with the kept exponent of the output [...] Haar factors, tree constraints, the tests and the inner integral kernels are part of the production too"), log w^m is a finite sum of terms. Y 129618-129622 states the rule this row applies: "the measures, constraints, tests and reference factors must either be identified by the alignment or entered with their actual changes." Delta_h := log w^B - log w^A is then the sum of the differences below. Zones and cells are those of III 13341-13346: zone n is Omega_n minus Omega_(n+1) for n below the reading level, the top zone is Omega_(k'), and Gamma^0_n is the set of level-n cubes of zone n. So n_b = |Gamma^0_b|.

| # | Factor class (Y 129569-129629) | Difference at a point of P_h | Site charge K (k-b+1) l_b n_b ? | Standing |
|---|---|---|---|---|
| F1 | Haar factors, tree constraints, delta_(G_i), integration measures | 0 | yes, trivially | Lemma COM; delta_(G_i) "is a function of the chart variable V'" (III 11889) |
| F2 | Tests and characteristic functions | not in Delta_h | not applicable | they define P_h and the test term of Theorem CAP (c); (SHELL) is the next row's |
| F3 | Stored boundary leaves B, B' read at level k' in [n, k]: stored members G_u^(n) (III 13106-13115) | sum over (l, X) of delta B^(l),(n)(X) | **yes** | 4.1: per-cell domination (a), III 13372-13380, given (INC-1) |
| F4 | Reading parts G_u^rd (III 13116-13124) and own members | B^B(X; rd^B P^B) - B^B(X; rd^A P^A) | yes given (PC-RD) | "accounted for by the last entry of the classical load" (III 13122-13124); the per-cell sum is not printed where I read |
| F5 | List leaves E, P-flat, Q, R, D | hat F^B - hat F^A on the leaf hull | yes given (PC-LIST) | the loads sum S^+_i[E], S^+_i[R] with the weights varsigma, w (III 12047-12050); the per-cell sum is the resummation lemma, cited, not checked |
| F6 | Live arrests: retained Gaussian q_W | sum_z D_W^z | **yes** | printed: "The vertex bound gives abs(D_W^z) <= K_G N(W) Delta_n^c" (Y 129655-129658); N(W) = filing cells of the collar; "charged on their disjoint regions" (Y 129667-129668) |
| F7 | Direct coupling slot on a regular zone: -x_(b) A(U) with curvature regularity | -(x^B_(b) - x^A_(b)) A(U) | **yes** | O (eq:zr-regular-weight): abs(A(delta c, U)) <= C alpha_n^2 norm(delta c) N_n; alpha_n^2 is the coefficient g_n of the load |
| F8 | **Direct coupling slot on the unrestricted fresh variables of a live component** (the "raw Wilson term", "inner Wilson factor") | -(x^B_(b) - x^A_(b)) A_Z(U), A_Z the Wilson action of the free bonds | **NO with the printed load; yes with the load l_b + z_b; yes in the mean given (ACT-X)** | Section 5 |
| F9 | Inner integrals' quadratic forms of a live history ("the old inner quadratics have their own cutoff differences", Y 129603-129605) | (1/2) <X, (Q^B - Q^A) X> | yes if the tests of S_omega bound X at the regular scale; otherwise as F8, and then no pointwise repair exists | not decided: whether S_omega bounds every Lebesgue variable is a native statement (PD-REST) that I did not find printed |
| F10 | Scalars of the label: node normalisers, the new determinant, the vacuum terms of cubes not inside Lambda_j(h) | numbers | yes given (SC-CELL) | 4.2 |
| F11 | Run-level vacuum constant (one per run and centre) | (c^B - c^A) vol(T) | no, and not needed | removed by (RULE), row 1395 Proposition SC2 and (H4); "not small: run B has one more bare level" (`library/gap-univk-log.md` L80) |

**4.1 F3 in full (PROVED GIVEN the printed lemma and (INC-1)).** Fix a class (n, k'). III (9.1:eq-per-cell-domination-2): for every cell c of Gamma^0_n,
  sum_(l >= n) sum_(X in D_l, X contains c) e^((kappa_B - c_d - 2) d_l(X)) ( |delta B^(l),(n)(X)| + |delta B'^(l),(n)(X)| ) <= K_1 y_n^(<= k'),   K_1 := K(d) + K_o(d) + K^o(d).
"Every non-zero member has such a cell c in X, with one exception", and the exception is anchored at a cell of Gamma^0_(n+1) (III 13380-13388). Assume
 (INC-1) in the exponent of the leaf resolution, the stored member of class (n, k') on (l, X) occurs with a total coefficient of modulus at most M_0 e^((kappa_B - c_d - 2) d_l(X)), M_0 free of h, the level and the torus.
Then the sum of the F3 differences of class (n, k') is at most M_0 K_1 y_n^(<= k') (n_n + n_(n+1)). Sum over the reading levels k' in [n, k] and use y_n <= l_n (III 13726): the F3 part of Delta_h is at most
  sum_n M_0 K_1 (k - n + 1) l_n (n_n + n_(n+1)).
This is the form of (PW-C), with the factor k - n + 1 from the reading levels, as row 1404 6.2 set it. The exception moves a charge from zone n to zone n + 1 at the load of zone n. So the constant c_b must be K (k - b + 1) (l_b + l_(b-1)). This changes Sigma_k^(q_a) by a factor at most 1 + 1/q_a.
Remarks. (i) (INC-1) is the incidence statement that check 1405 L29 asked for ("a bound for their sum per cell and read level"). The lemma leaves room: a multiplicity that grows like e^((kappa_B - c_d - 2) d_l(X)) is still paid. (ii) (INC-1) is an instance of the outline's carrier incidence estimate (O 5445-5459) and belongs to ZONE-FORM. It is not proved here: the assembly formula is not printed (row 1404 3.1). (iii) The lemma's status in III is not checked in this row (its hypotheses (i)-(iv) of part (b) are "assumed as hypotheses" for part (b); part (a) is stated without them).

**4.2 The scalars F10 and (SC-CELL).** At zero source E^c(0) = 0 (III 11924-11926) and the term (9.1:eq-centre-normalisation-2) vanishes. With (RULE) the run's extensive vacuum constant is divided out once per run. What stays in a label is the vacuum energy of the cubes X of level j not inside Lambda_j(h), with the opposite sign, and the node scalars of the live histories. The cubes of level j not inside Lambda_j(h) meet Z_j, so their number is at most a constant times the number of level-j cells of the large-field region of level j. This is a zone count. So the needed statement is
 (SC-CELL) the label-dependent scalar part of Delta_h, after (RULE), is a sum over the charged cells c of numbers delta c_(omega,c) with |delta c_(omega,c)| <= K l_(n(c)).
This is the scalar clause of the outline's incidence estimate ("decompose the scalar part as delta c_omega = sum_c delta c_(omega,c)", O 5447-5448; "The norm must include scalar anchors, not only oscillations", O 5443). Owner: ZONE-FORM. Not proved here. I found no scalar of a label that is extensive in the fine volume: every label-dependent scalar listed in Y 129585-129613 is attached to a node or a cube of the label's large-field region.

## 5. The first factor that breaks the site charge: F8 (written 2026-11-22T17:46Z by date -u)

**5.1 What is printed.** A live stopped component carries free group variables: "The resulting term has unrestricted fresh Haar coordinates on the bonds with an end in the box" (Y 75682-75684); "The unrestricted fresh field of a late open stop is carried upward by averaging" (Y 76015-76016). Its weight keeps a Wilson factor: "The retained inner Wilson factor and component rarity must still be present in the original mass estimate" (Y 9500-9503); "The inner Wilson factor belongs inside K_omega. On a real fibre it may supply positive action suppression" (Y 53595-53597). The coupling of a run is x_(r) = theta_r - zeta_(r) (III (9.8:eq-uniqueness-theorem-3)), so the two runs differ at level b by delta x_b := x^B_(b) - x^A_(b) = -(zeta^B_(b) - zeta^A_(b)), and z_b = sup |delta x_b| (III 12010). The load holds this difference only with the factor g_b := g_b^2 (log x_b)^(2 q_flat) (III 12007-12008, 12047-12050): l_b >= g_b z^sharp_b >= g_b z_b.
The outline states the consequence itself, for one zone parameter: "There is a genuine limitation to a reserve measured only by stored sites. On a bare region where the real field is unrestricted, a plaquette can have U_p = -I, and then a_p = 2 [...] Thus [the phase hypothesis] with this site reserve cannot hold pointwise on the entire unrestricted bare-field domain. This does not refute the complex mass estimate. The Wilson factor strongly suppresses those configurations." (O 5348-5362 = Y 81910-81927.) The step below is the same remark at the finite difference of the two runs, with the exact amount left.

**5.2 Proposition NS (PROVED, elementary; unchecked).** Let P' be a measurable set of positive measure in the leaf resolution of one label, on which the cell counts n_b are constant. Suppose that on P'
  Delta_h = - delta x_b A_Z(U) + R,   |R| <= r_0,
where A_Z(U) = sum over the plaquettes p of the free bonds of a_p(U), 0 <= a_p <= 2, and put A^* := ess sup over P' of A_Z. Then
 (a) ess sup over P' of |Delta_h| >= |delta x_b| A^* - r_0. So (PW-C) on P' forces |delta x_b| A^* <= a + sum_b c_b n_b + r_0.
 (b) |delta x_b A_Z(U)| <= 2 |delta x_b| N_Z everywhere, N_Z the number of those plaquettes.
 (c) For every t >= 0: |delta x_b A_Z(U)| <= |delta x_b| t + (|delta x_b| / x^A_(b)) ( x^A_(b) A_Z(U) - x^A_(b) t )_+ .
Proof. (a) |Delta_h| >= |delta x_b| A_Z - r_0 pointwise. (b) 0 <= a_p <= 2. (c) A_Z <= t + (A_Z - t)_+. QED

**5.3 Reading of Proposition NS for (PW-C).**
- *Amount left after exact cancellations.* No other factor cancels F8. The chart maps are right translations and F8 is evaluated at the same point of the leaf resolution in both runs; the scalars are constants; the leaves F3-F5 are bounded by their loads and cannot cancel a term of size |delta x_b| A_Z when z_b is large against l_b. With t := C alpha_b^2 N_cells (the action of a regular field on the same cells, O (eq:zr-regular-weight)), (c) splits F8 into a part C g_b z_b N_cells, which the printed load pays, and the **excess** eta_b ( S_b - x_b t )_+ with S_b := x^A_(b) A_Z(U) >= 0 and eta_b := z_b / x^A_(b). The excess is the amount left. It is zero on regular fields and it is at most 2 z_b N_Z.
- *With the printed loads: (PW-C) FAILS as a statement with K free of the couplings, unless a further bound holds.* If P_h has a part of positive measure where a fixed fraction of the free plaquettes has a_p >= 1 (the fresh coordinates are unrestricted), then A^* >= c N_Z and (a) forces z_b <= K' (k - b + 1) (l_b + l_(b-1)) for the label's zones. The printed load gives only g_b z_b <= l_b. So the site charge is short by a factor up to 1 / g_b = x_b (log x_b)^(-2 q_flat), exactly the factor beta (log beta)^(-C-1) of O 5352-5359. It holds exactly when
   (Z-ABS) z_b <= K_z (l_b + l_(b-1)) for the recent zones b,
 that is, when the coupling shifts of the two runs differ by no more than the other entries of the load. (Z-ABS) is a statement about the comparison family. It is not printed and not decided here.
- *With the augmented load: (PW-C) HOLDS for F8 by (b), with no input.* Put l_b^+ := l_b + z_b. Then |F8| <= C_L z_b n_b <= C_L l_b^+ n_b, C_L the number of free plaquettes per level-b cell (a function of L and d). The price is in the rate, not in the structure: l_b^+ / l_b <= 1 + 1/g_b <= 1 + x_b. With x_b <= theta_s = X + c_0 s (linear in the depth), Theorem M then gives O(V (x_max e_w)^(1/2)) in place of O(V e_w^(1/2)). This is still a rate when x_max e_w tends to zero (for example for a geometric e_w, or for e_w <= C K^(-3/2) log^p K with x_max <= C K). It is lost when e_w decays more slowly than 1/x_max.
- *A failure of this site charge says nothing about the sign of a density.* Both densities are positive on P_h by Theorem CAP (a). Proposition NS concerns the size of the log ratio only.

**5.4 F9 (not decided).** If a live history has a Lebesgue variable X that its tests do not bound, the same remark applies to (1/2) <X, (Q^B - Q^A) X>, and (b) has no analogue: the variable is not compact. Then only the mean form of Section 6 can hold. The printed text bounds the live arrests pointwise (F6), so F9 concerns the inner integrals of a live history only. Decide it from CMP 122b (1.71) in the row PD-REST, which owns S_omega.

## 6. The direct moment estimate (check 1405 L38): Theorem MA (PROVED GIVEN (PW-CA), (CAP-M0), (ACT-M0); unchecked)

**6.1 Theorem MA.** Setting and notation of Theorem M (row 1404, 6.1): densities rho_h^0, rho_h^1 >= 0 with one positive set P_h, Delta_h their log ratio, 0 < F^0, F^1 < infinity, <.>_0 the mean in the normalised law of rho^0 on the disjoint union. Let n_i >= 0 and S_j >= 0 be measurable, and a, c_i, eta_j >= 0 constants, with
 (PW-CA) | Delta_h | <= a + sum_i c_i n_i + sum_j eta_j S_j almost everywhere on P_h, for every h.
Assume moments under the law 0 only:
 (CAP-M0) < exp( gamma sum_i n_i ) >_0 <= e^B,   (ACT-M0) < exp( sigma sum_j S_j ) >_0 <= e^(B_S),
with gamma, sigma > 0, and put theta := max_i c_i / gamma, theta' := max_j eta_j / sigma. If theta + theta' <= 1, then
  | log F^1 - log F^0 | <= a + theta B + theta' B_S.
Proof. Put N := gamma sum_i n_i and T := sigma sum_j S_j. Then sum c_i n_i <= theta N and sum eta_j S_j <= theta' T. Upper bound: F^1 / F^0 = < e^(Delta) >_0 <= e^a < e^(theta N) e^(theta' T) >_0 <= e^a < e^N >_0^theta < e^T >_0^(theta') by Hoelder's inequality in a probability measure with the exponents 1/theta, 1/theta' and the constant function 1 for the rest. Lower bound: Jensen gives log < e^(Delta) >_0 >= < Delta >_0 >= - a - theta < N >_0 - theta' < T >_0, and < N >_0 <= log < e^N >_0 <= B, < T >_0 <= B_S, again by Jensen. (Delta is integrable because it is dominated by the integrable right side of (PW-CA).) QED

**6.2 Corollary (sign).** If Delta_h = Delta^s + Delta^a with |Delta^s| <= a + sum c_i n_i and - sum eta_j S_j <= Delta^a <= 0, then the upper bound needs no action moment: log F^1 - log F^0 <= a + theta B. The lower bound needs first moments only: log F^1 - log F^0 >= - a - theta B - sum_j eta_j < S_j >_0. This is the case of F8 when delta x_b >= 0 for every recent b (run B has the larger inverse coupling at the matched levels). For the other sign exchange the two ends, or use (ACT-M0).
Proof. e^(Delta) <= e^(Delta^s) for the upper bound; Jensen as in 6.1 for the lower. QED

**6.3 Lemma EXC (the action moment is a relative reserve; PROVED).** Let nu be a measure, S >= 0 and r >= 0 measurable with 0 < M(0) < infinity, where M(t) := integral of e^(-(1 - t) S) r d nu. If M(sigma) <= e^(B_S) M(0) for one sigma in (0, 1], then < e^(eta S) > = M(eta) / M(0) <= e^((eta / sigma) B_S) for 0 <= eta <= sigma, the mean being in the law e^(-S) r nu / M(0).
Proof. log M is convex in t (Hoelder), log(M(t)/M(0)) vanishes at t = 0 and is at most B_S at t = sigma. QED
So (ACT-M0) for the pieces S_j says: the restricted A mass does not grow by more than e^(B_S) when the fraction sigma of the Wilson action of the free bonds is removed. This is the real-point, relative form of the outline's reserve "e^(c V + sigma S_available)" (O 5382-5384) and of the mass input of the B4 note ("The required mass majorant includes exp(c_V V_omega + c_S sum_b S_(omega,b))", `library/b4-typed.md` L168). Owner of the absolute form: ZONE-RESERVE. The outline's warning binds here too: the action "cannot be spent twice" (O 5398-5399).

**6.4 The excess form, which the printed load can pay.** Apply 5.2 (c) before Theorem MA: charge eta_b x_b t_b = C g_b z_b n_b <= C l_b n_b to the sites, and take S_b^> := ( S_b - x_b t_b )_+ as the action piece. Then (PW-CA) holds for F8 with the printed loads and eta_b = z_b / x^A_(b) <= g_b z_b <= l_b (for x_b >= e). The moment needed is
 (ACT-X) < exp( sigma sum over recent b of S_b^> ) >_(A,P) <= e^(E_S V), for one sigma in (0, 1) and E_S free of the torus, the centre and the cutoff.
With (CAP-M0) at B = E V, the load envelope and the age a_0 of check 1397, exactly as in check 1405 L31-35:
  B_rec <= K C V [ e_w + ( E / gamma + E_S / sigma ) e_w^(1/2) ],
when K C e_w^(1/2) (1/gamma + 1/sigma) <= 1. The factor x_max of 5.3 does not appear.

**6.5 Lemma G1 (a model test of (ACT-X); PROVED; exact).** Let y be a standard real Gaussian, p >= 0 and 0 <= eta <= 1/2. Then
  E[ e^(eta y^2 / 2) | |y| >= p ] <= (1 - eta)^(-1) e^(eta p^2 / 2) <= e^(2 eta + eta p^2 / 2).
Proof. For p = 0 the left side is (1 - eta)^(-1/2). For p > 0 put s := p (1 - eta)^(1/2) <= p. The left side is (1 - eta)^(-1/2) Q(s) / Q(p), Q the upper tail. Write Q = m phi with m the Mills ratio. Then Q(s)/Q(p) = (m(s)/m(p)) e^((p^2 - s^2)/2) = (m(s)/m(p)) e^(eta p^2 / 2). The function t m(t) is nondecreasing on t > 0: its derivative is (1 + t^2) m(t) - t, which is nonnegative by m(t) >= t / (1 + t^2). So m(s)/m(p) <= p/s = (1 - eta)^(-1/2). Last step: - log(1 - eta) <= 2 eta on [0, 1/2] by convexity. QED
Reading. For independent coordinates, some of them conditioned to fail a test at the threshold p, the log moment of eta times the Gaussian action is at most 2 eta per coordinate plus eta p^2 / 2 per failed coordinate. With eta = z_b / x_b and p^2 of order (log x_b)^(2 q_flat), the second term is g_b z_b / 2: the printed load, per failed cell. So in the product model the mean charge holds with the printed loads, where the pointwise charge of Proposition NS fails. This is a model. It is not a statement about the restricted A law, where the coordinates are coupled and the tests of both runs act.

**6.6 (ACT-X) is not the open target in another form, as far as I can show.** It is a one-run statement at real points: it compares no two cutoffs and contains no difference of loads. In the model of 6.5 it holds while a two-cutoff comparison is not even posed. I cannot prove that it is strictly weaker than ZONE-RESERVE; it follows from the relative form of ZONE-RESERVE by Lemma EXC, and it asks for real points and for the recent zones only.

## 7. Verdicts (written 2026-11-22T17:46Z by date -u)

Kind of result (How we work, item 9): a proof of a step that the account sketches or assumes (the complete two-run log difference on the common passing set), built on its printed lemmas; no correction of their text. The outline itself states the limitation used in Section 5.

7.1 **(COMMON) for the inner history spaces: HOLDS at the leaf resolution, GIVEN (d1), (SCAF), (CH)** (Lemma COM). All three are printed; (d1) sits in a proposition marked "Proof outstanding" (owner PD-REST). The supports S^A, S^B still differ; that is (SHELL), not (COMMON).

7.2 **(PW-C) as stated in row 1404 6.2 (site charges only, printed loads, K free of the couplings): NOT TRUE IN GENERAL. First failing factor: F8,** the direct coupling slot against the Wilson action of the unrestricted fresh variables of a live component. Amount left after exact cancellations: the excess (z_b / x_b) ( x_b A_Z(U) - x_b t_b )_+ <= 2 z_b N_Z, where the printed load pays only g_b z_b per cell (Proposition NS). The shortfall is at most the factor 1 / g_b = x_b (log x_b)^(-2 q_flat). (PW-C) holds for F8 exactly under (Z-ABS), which is not printed. This is a failure of one sufficient charge. It says nothing about the sign of any density.

7.3 **(PW-C) with the augmented load l_b^+ = l_b + z_b: HOLDS for F8 with no input** (Proposition NS (b)), at the price of a factor at most x_max inside the square root of the rate.

7.4 **The other factor classes.** F1: zero difference. F3: site charge PROVED GIVEN the printed per-cell domination (a) and (INC-1), with c_b = K (k - b + 1) (l_b + l_(b-1)) because of the lemma's exception. F6 and F7: site charge printed (vertex bound; regular-zone Wilson channel). F4, F5, F10: site charge GIVEN (PC-RD), (PC-LIST), (SC-CELL); these and (INC-1) are instances of the outline's incidence estimate, owner ZONE-FORM, not proved here. F9: not decided (5.4). F11: outside (PW-C), paid by (RULE).

7.5 **Direct moment estimate: PROVED GIVEN (PW-CA), (CAP-M0), (ACT-M0)** (Theorem MA; one law only, both sides). With the excess form, (PW-CA) holds for F8 at the printed loads, and B_rec = O(V e_w^(1/2)) GIVEN (CAP-M0), (ACT-X), the site inputs of 7.4, the load envelope and the incidence of row 1395 6.2. The action moment is a relative reserve (Lemma EXC). In the product Gaussian model the mean charge holds at the printed load (Lemma G1), where the pointwise one fails.

7.6 **Not shown.** (INC-1), (PC-RD), (PC-LIST), (SC-CELL) (ZONE-FORM); (ACT-X) and (CAP-M0); (Z-ABS); F9; (FAC) at the leaf resolution and (d1) (PD-REST, CV); (SHELL) and the test term; the proofs of the per-cell domination lemma and of the vertex bound (cited from III and Y, not checked here). No unconditional Wilson estimate is proved.

## 8. Next two rows and their decisive outcomes

**Row 1, `gap-univk-actx` (proof row, one run, real points).** Decide (ACT-X) and (CAP-M0) under the restricted A law of the good labels, on both tori; decide F9 on the way. Start from the one-component mass bound of the stopped component with its "retained inner Wilson factor" (Y 9495-9503, 53588-53600; II 104043-104062; CMP 122b (1.71) through `library/pd.md`): show that the bound survives when the fraction sigma of the Wilson action of the free bonds is removed, at the cost e^(E_S) per charged cell, and that the component rarity pays the cell count at a fixed gamma. Then Lemma EXC gives (ACT-X). Use the native-good law and pay the restriction to P by 1 + s^A (check 1405 L73).
 Decisive outcomes: (1) both hold with constants free of the torus and of the couplings: B_rec = O(V e_w^(1/2)) follows from ZONE-FORM's site inputs alone, and the dial interpolation is not needed for the recent retained estimate. (2) the retained Wilson factor is already spent by the failed-test payments (no fraction sigma is left): then use 7.3 and state the rate with x_max, or prove (Z-ABS) from the matched-increment clause (Y 126432-126436); if neither is available, the recent comparison has no rate by this route.

**Row 2, `gap-univk-shellcap` reduced to (SHELL) and the test term** (row 1404 Section 8, Row 2, without (CAP-M), which moves to Row 1). Decisive outcomes as written there.
Order: Row 1 first. It decides whether the one factor that breaks the site charge is paid in the mean. The four site inputs of 7.4 stay with the owner of ZONE-FORM; a separate row for them is useful only after the assembly formula is written out factor by factor, which rows 1398, 1400, 1404 and this row did not find printed.

## 9. Status

| Statement | Mark |
|---|---|
| Lemma COM (3.2) | PROVED GIVEN (d1), (SCAF), (CH); unchecked |
| Inventory table (4.0) | READ (Y 129569-129629 and the cited lines); F4, F5, F9, F10 classified, not bounded |
| F3 site charge (4.1) | PROVED GIVEN III per-cell domination (a) and (INC-1); unchecked |
| Proposition NS (5.2) | PROVED (elementary); unchecked |
| (PW-C), row 1404 form | NOT TRUE IN GENERAL at F8 with printed loads; equivalent to (Z-ABS) for that factor |
| (PW-C) with l_b + z_b | HOLDS for F8; other factors as in 7.4 |
| Theorem MA, Corollary 6.2, Lemma EXC | PROVED (Hoelder, Jensen, log-convexity); unchecked |
| Lemma G1 | PROVED (Mills ratio); a model, not a proof step of the chain |
| (ACT-X), (CAP-M0), (Z-ABS), F9, (INC-1), (PC-RD), (PC-LIST), (SC-CELL) | OPEN |
| (SHELL), test term, (RAR), term D, (GEO), hypotheses of III 9.1, (LOG), the seed | OPEN, untouched |

Repo search for the new names: `library/open-core.md` has no hit for PW-CA, ACT-X, ACT-M, Z-ABS, INC-1, SC-CELL, "Lemma EXC" or "Lemma COM" (one grep, this lane folder). The formation estimate with action pieces is `library/b4-typed.md` (5); Theorem MA is its two-run, real-point, one-law form and cites it.

No numeric job was run; none was needed. Files written in the repository: this file only. Scratch: /tmp/ym4d-pwc-w2/src (parts I and II and the short outline, fetched by URL at 31a47c543775).

RESULT: (COMMON) holds at the leaf resolution given three printed statements (Lemma COM). (PW-C) in the site-only form of row 1404 is NOT TRUE IN GENERAL with the printed loads: the first failing factor is the direct coupling slot against the Wilson action of the unrestricted fresh variables of a live component (F8); after exact cancellations the excess action times z_b / x_b is left, short of the load by at most the factor x_b (log x_b)^(-2 q) (Proposition NS, which restates the outline's own remark O 5348-5362 at the two-run difference); it holds for F8 with the load l_b + z_b at the price of x_max in the rate. PROVED (elementary, unchecked): the stored boundary members obey the site charge from the printed per-cell domination given an incidence bound (INC-1), with c_b = K (k-b+1)(l_b + l_(b-1)); Theorem MA (one exponential moment of the cell count and one of the action under the restricted A law give the two-sided mass bound), Lemma EXC (the action moment is a relative reserve), Lemma G1 (in the product Gaussian model the mean charge holds at the printed load). OPEN: (ACT-X) and (CAP-M0) (next row gap-univk-actx), the site inputs (INC-1), (PC-RD), (PC-LIST), (SC-CELL) with owner ZONE-FORM, (Z-ABS), the Lebesgue factor F9, then (SHELL), the test term, (RAR), term D, (GEO).
