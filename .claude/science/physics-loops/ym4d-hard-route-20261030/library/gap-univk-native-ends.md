lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T10:08Z

# Row 1410, gap-univk-native-ends: the terminal formula of a good aligned label at its two native real endpoints

Started 2026-11-22T22:08Z (date -u). Pinned at commit 49b80b216. Author: Claude Fable 5.2 medium, Mac mini worker 2.
Checked by no one. Kind of result: reading row (their text), then a classification of our own.

Credit: the objects read here are those of the accounts of Ethan Sussman and Levent Alpoge
(with Claude and Codex as authors of their text): YM4_1400.tex ("Y"), complete account part III ("III"),
the short outline ("O"). Balaban's block renormalisation is the base of all of it.

## 0. Plan

1. Repo search and prior rows: rows 1404, 1406 and checks 1405, 1408 (read in full).
2. Source reading, one anchor per step: Y 129569-129680 (terminal inventory and post-cancellation remainder),
   Y 72678-72686, 73932-74049, 75063-76486 (branch identities), III 32176-32199, O 18044-18204,
   III 13337-13393 (per-cell domination).
3. Per label type (shell exit, last-shell exit, completed component, restored component, live arrest):
   the native terminal density at the real endpoint of run A and of run B, factor by factor.
4. log w^B - log w^A on P_h as a list of terms with source line and class
   (stored-leaf, read, action, quadratic, scalar).
5. Decisive outcome: all site charges, or a named excess with its coefficient.
6. Next two rows.

Each step below is appended when done.

## 1. Prior rows and repo search (written at step 1)

Read in full: row 1404 (`library/gap-univk-pos2.md`), check 1405 (`library/gap-univk-pos2-check-astra62.md`), row 1406 (`library/gap-univk-pwc.md`), check 1408 (`library/gap-univk-pwc-check-astra62.md`).

What binds this row:
- The pair compared is that of Theorem CAP (row 1404, 5.2): `A on P_h` and `tests of A with weights of B on P_h`, P_h = S^A ∩ S^B on a common resolution. Delta_h := log w^B - log w^A on P_h holds weight factors only.
- Check 1408: row 1406's slot F8 put three different objects in one slot (the free outgoing field, the prepared old core, the carrying action). Its table also mixed production inputs with stored outputs. So neither the failure nor the truth of the site-only (PW-C) is on file.
- Check 1408 L21: a leaf can store the output of a production. Subtract its two stored values, or resolve the production and compare inputs. Never both.
- Check 1408 L65: for a weighted action the exact difference is -<c_B - c_A, a_A> - <c_B, a_B - a_A> (coefficient part and moving-read part).

Repo search. `library/open-core.md`: no hit for "native end", "terminal formula", "terminal densit", "post-cancellation" (one grep). FINISH rows naming this comparison: 1404 to 1408 and this row. Obligations used, not redone: CV and PD-REST (`library/open-registry.md` L19, L418), ZONE-CAPACITY, ZONE-FORM, ZONE-RESERVE (L543-545, owner `b4-typed`).

## 2. Sources read (appended as read)

Y = `YM4_1400.tex` (local, 136637 lines). III = part III (local). O = short outline at 31a47c543775, fetched by URL into /tmp/ym4d-native-ends-w2/src (32992 lines).
- Y 129540-129689 (arguments of the production formula; post-cancellation rule; live arrests).
- Y 72640-72709 (reference cutoff; constancy in the free top argument). Y 73880-74104 (old Wilson factor; the restored identity; drop-out fibre).
- Y 75055-75083, 75660-75709 (late drop-out reference measure; first chart). Y 75995-76054 (carried fresh field). Y 76440-76494 (shell stop: disjoint variables, bare normalized Haar).
- III 32150-32209 (operation split by age). O 18020-18214 (history operation, exponent, inner Wilson, drop-out evaluations, later reads).

- Y 73062-73266, 73373-73492 (records, five read rules, local operation, tied exponent, retained inner factors).
- Y 74892-75056 (complete quadratic form Q_tau; reference envelope; strip fields and the shell test chi'). Y 77105-77416 (source excess recursion; frozen inner Wilson weight; parameter tube).
- Y 130020-130339 (aligned nested terms; summing the aligned terminal terms). Y 130590-130617 (gauge exponent on a cube: eps_j^2 <= C g_j^2 (log x_j)^(2 p_0), q_flat >= p_0).
- III 11845-12059 (terminal term, chart, labels, slots, loads). III 12925-13134 (production arrays, marks, classes (b1)-(b3), read split). III 13600-13824 (resolved interpolation, live components). III 17195-17282 (load envelope: z_s' <= C_zeta (1+s') e_s'). III 17381-17545 (comparison of aligned terms; whose raw Wilson strength). III 53953-53963 (x_(r) = theta_r - zeta_(r)). III lines 18, 308, 597 (exponent order: q_flat >= p_0 + 2(d+1) r_pr + 1).
- O 5286-5470 (regular channel, unrestricted bare zone, formation test).
Not re-read: III 13337-13393 (per-cell domination). I use it only through row 1406 Section 4.1 as corrected by check 1408 L39-41. Parts I and II were not fetched; nothing below reads them.

## 3. The native terminal density, type by type (written 2026-11-22T22:15Z by date -u)

Kind of result: reading of their text. Every formula below is theirs; the arrangement by type is mine. Unchecked.

**3.0 Common frame, both runs.** Run c is A (length n) or B (length n+1), on one scaffold theta_s = X + c_0 s. The coupling of run c at depth r is x^c_(r) = theta_r - zeta^c_(r) (III 53958-53960). For a label h the native term is
  tau^c_h = chi T^w e^(A^w - E^c),
"chi is the product of the characteristic functions of the label, T^w the large-field operation at the stop and A^w the effective action at the stop" (III 11859-11862). The chart is: V = V' V^c_Lambda on a live second-class component, V'' = V' M_B''(U^c_0) on a removed component with stored shell variables, raw variables elsewhere (III 11867-11873; Y 130226-130231). "Conditional right translation thus preserves the free Haar factors, and the recorded tree constraints act on the common relative variables" (Y 130233-130236).

Three facts fix where a coupling can appear.
 (W1) Two weights have different roles: "The real physical weight x and the reference weight theta have different roles" (Y 74893-74894). theta is common to the two runs. x is not.
 (W2) The five read rules (Y 73148-73157): class membership and old cores read the stored label entries Z_j; backgrounds, data, measures and gauge nests read the determining entries; density tests and the last-shell test read the action regions; "Coupling and vacuum weights use their specified action supports".
 (W3) In the account's own comparison the raw Wilson strength is not moved: on the dial domain "the raw Wilson strength and the gains are those of A" (III 17489). The shift of the coupling enters the assembly as the zeta-entries of the array (III 11972, 12965), with load gfrak_j [z^sharp_j + ...] (III 12049), where gfrak_j := g_j^2 (log x_j)^(2 q_flat) is the load weight (their fraktur g) and g_j the coupling. In the native pair of Theorem CAP (row 1404) both ends keep their own strength. So the native difference has a Wilson coefficient term where the account's hybrid has a zeta-entry. This is the same number written in two places; it must be counted once (check 1408 L21).

**3.1 Type S: shell or last-shell exit (late open stop), free outgoing field.**

| Factor | Native form at the real endpoint of run c | Depends on the run through |
|---|---|---|
| Fresh box field | "unrestricted fresh Haar coordinates on the bonds with an end in the box" (Y 75682-75684); "Their fresh output therefore carries bare normalized Haar" (Y 76475-76476). "After the central integration the term is constant in the free top argument on the box" (Y 72679-72680). Density 1. | nothing |
| Reference cutoff | none at this exit: "There is no failure event for that cutoff on the free Haar argument" (Y 72685-72686); "The shell and last-shell failures are separated before the operation that assigns the reference-law density" (Y 76473-76475) | nothing |
| Old shell variables | normalized Haar on the free shell bonds after the frame tree, Jacobian one (Y 76467-76471, 75690-75696) | nothing (measure); the weights below |
| Tests | tree constraint and the two shell tests "imposed on the retained variables before a reference field is drawn" (Y 72680-72682); the failing test with its recorded value | test thresholds are scaffold data; the tested field can move with the run's background |
| Own core Wilson term | none: a drop-out's "kept factors have no new core Wilson term" (Y 74073-74074) | - |
| Carrying action | e^(-A(upsilon 1_X, U)) on "the bare plaquettes whose corners lie in X", U real, compatible: M^j U(b) = V_j(xi)(b), with upsilon(p) >= c theta_j on the action layer that owns p (Y 74072-74097; O 18130-18157). "This is an exact redistribution of factors in the same integrand" (O 18136-18137). | coefficient upsilon^c (the run's action weight x^c on its action layer); the fibre through the stored averages |
| Kept factors K_omega | tests, integrations, gauge factors, complete kept forms Q_tau, elimination factors "left when it stopped" (O 18132-18133); pivot factors J_c; gauge normalizers z(theta_j, eps_j) (Y 75078-75084) | tau^c = x^c/theta in each Q_tau; the backgrounds read |
| Older marked cores inside | "Any older marked core retains its own joint integral and reference bound" (Y 75687-75688): type C below, read at real pairs | as type C |
| Later reads of the fresh field | "Outgoing averages can use the fresh slot, and a boundary weight reading it stays in the joint integral" (Y 76042-76044). At the last lattice the fresh field is the terminal variable itself. | only if a terminal boundary weight reads the box |

**3.2 Type C: completed component (an island with its operation T'_i(X)).**

  T'_i(X) F(p) = |W_4|^(-1) sum_omega integral over S_omega of e^(Phi_omega(xi; p)) F d mu_omega(xi),   Phi_omega = Phi°_omega(xi) - (1/2) q_X(xi; z) + V_X(xi; z)
(Y 73202-73208, 73248-73253; O 18028-18055). mu_omega is "a product of normalized Haar measures and Lebesgue measures" and normalizers "remain in the integrand" (Y 73214-73217).

| Factor | Native form | Depends on the run through |
|---|---|---|
| Inner Wilson term | exp{-A(x'' zeta_1 1_X, U''(xi))}: mask zeta_1 1_X (the old core), field U''(xi) "real and [...] formed from the prepared determining sequence, with its old innermost datum and its new fluctuation datum", "independent of the external pair" (Y 73913-73922; III 32187-32193 writes the weight (g''_k(.))^(-2) zeta_1 Gamma_X at U''_(k+2)) | coefficient x''^c; the map xi -> U''(xi) if the background map reads the weight profile |
| Main quadratic | q_X = norm(phi^(1/2) D H B)^2 "formed at the real glued background" (O 18057-18058), with the reference weight: "Use w_fr = theta on the component" (Y 73952-73953). "The reference measures, the bare stored fluctuation slots and the reference quadratic q_X are common to the two systems" (Y 77207-77209). | coefficient: none (theta). Field: the glued background, through the exterior increment |
| Shell fluctuation B | Lebesgue, tree gauge Jacobian one, test chi'(B) = 1{abs(B) < r_t}, r_t = delta'_t / g_t = A_1 p_1(g_t) (Y 74987-74995). Here g_t = theta_t^(-1/2) (Y 73074, 73079-73080). | nothing |
| Stored strip fields A^s_j | "The one-step operations in that core integrate the stored strip fields A^s_j against Lebesgue measure" (Y 74983-74984). Exponent -(1/2) <A^s, Q_tau A^s>, Q_tau = tau K_A + K_G, tau = x/theta (Y 74894-74903). The reference bound enlarges to "the full Euclidean spaces for the strip fields" (Y 75016-75018). | coefficient tau^c in front of K_A; K_A, K_G through the background |
| Normalizers | Gaussian mass of tau K or its ratio to D_0 (Y 74907-74910); gauge normalizer; pivot factors; "E_X is included once in the scalar normalization at its original levels" (Y 74047-74049) | tau^c, x^c |
| Kept potential V_X | localized terms, abs(V_X) <= C N_0(omega) (O 18080-18084); it contains P_X + I_X of 3.3 | the slots of the run's array (stored leaves, list entries) and the reads |
| Inner islands | "an inner operation is read at a real admissible pair in Phi°_omega" (O 18097-18098) | recursively type C; healed ones are stored leaves |

**3.3 Type R: restored component (the reference law drawn; the component stays in the class).** With S_old(s) = A(x'', U''_i(s)), S_ref(v) = theta_i A(zeta_0, U_(i,X)(v)), S_0 = theta_i A(zeta_0, U_0), D_X^(-1) = e^(S_0 + I_X - E_X) (Y 73937-73947), the exact product is
  e^(-S_old) chi_X e^(-S_ref) / D_X = e^(-S_new) chi_X e^(-q_X/2 - S_core) e^(P_X + I_X - E_X)   (Y 74028-74034),
"an identity in (s, v) before either variable is integrated. It remains valid [...] at a prescribed terminal raw field" (Y 74035-74038).

| Factor | Native form | Depends on the run through |
|---|---|---|
| Carrying action | S_new = A(w', W-bar), w' "the actual outgoing weight", W-bar the completed background; "belongs to the new label's action" (Y 74011-74012, 74041) | coefficient w'^c; field W-bar |
| Core term | S_core = A(w zeta_1, W^in(f)), w = x'' (Y 73985) | coefficient w^c; field |
| Quadratic | q_X/2, extracted at weight theta (Y 73977, 73983-73984) | field only |
| Remainder P_X | exterior: Delta_(w(1-zeta_0))(W-bar, W'') + A((w_fr - w)(1 - zeta_0), W-bar) + theta Delta_(zeta_0)(W-bar, W^Z); middle: theta A(zeta_1, W^0) + theta Delta_zeta(W^0, W_g^0) - (theta Delta_zeta(W_g^f, W_g^0) - q_X/2) + theta Delta_zeta(W_g^f, W'') - A((w - theta) zeta, W''); core errors Delta_(w zeta_1)(W^in(f), W^in(gamma^flat)), Delta_(w zeta_1)(W^in(gamma^flat), W''); and W_X = A(w' - w_fr, W-bar) (Y 73961-74023) | every term with w or w': linear in the run's weight; the theta terms through fields only |
| Reference centre | I_X = minus the log of the centred reference integral, E_X its counting factor (Y 73944-73947); S_0 "cancels in the rewrite" | I_X: weight theta, so through the exterior data only |
| Measure | restored box field v on its reference tree slice (delta_G); chart V = V' V^c_Lambda; "The cancellation changes none of those coordinates or constraints" (Y 74069-74070) | the chart multiplier V^c_Lambda |
| Uses | "the original old action is used once in this rewrite. One must not also keep it as a separate reserve, or append the old factor D_X^(-1)" (Y 74044-74046) | - |

**3.4 Type L: live arrest W.** Retained quadratic q_W "at the new root on the top storey"; the sum of its class-z marks is D_W^z with abs(D_W^z) <= K_G N(W) Delta_n^c; "The collar cells of distinct live arrests are charged on their disjoint regions"; "At the last lattice the weight is read at the root without intervening links"; the exterior difference "is filed in the potential" (Y 129652-129676). By reading site the entry is "the Gaussian piece, its shifted value minus the base, its grain piece, or its retained weight" (Y 129608-129612).

**3.5 What a leaf is.** A healed region's history "is summed inside the stored boundary terms R' and B' of that R-step" (III 17530-17533). So at the last lattice the factors of 3.1 to 3.4 occur only for components live at the stop. Everything healed is a stored number, compared as a stored value (III 13106-13133), never as its production (check 1408 L21). The classes inside a live component are of kind (b3): "They are carried in the label of the term" and "cannot be dialled by the splitting through which the surviving classes are dialled" (III 13044-13058). So the terms of Section 5 that sit inside live components are exactly the part of the native difference that the account's dial does not move.

## 4. Two elementary lemmas for a good aligned label (written 2026-11-22T22:17Z by date -u)

Kind of result: proof of a step their text uses without stating it in this form. PROVED here by hand, unchecked. Repo search for the names: `library/open-core.md` has no hit for REG-P, RD-BG, BND-S, QS-M, STRIP-Q, "Lemma AL", "Lemma WIL"; FINISH rows have none (one grep each).

**4.1 Lemma AL (an aligned label has no bare unrestricted zone).** Let h be aligned: its first index exceeds n_c >= 1 (III 11939-11946). Then:
 (a) Omega_j = Lambda_j = the torus for every j <= n_c.
 (b) Zone m := Omega_m minus Omega_(m+1) is empty for m <= n_c - 1.
 (c) Every zone m is contained in Lambda_(m-1). So on zone m the label's tests of level m-1 hold, and m - 1 >= n_c - 1.
 (d) If a zone m meets a live component C, then m >= j(C) - 1. If h is good (no live component of age a_0 or more), then m > k - a_0 - 1.
Proof. (a) The first index is the level of the first large-field region, so Z_j = Lambda_j^c is empty for j <= n_c. With Lambda_j inside Omega_j (Y 73089-73091), Omega_j is the torus too. (b) follows from (a). (c) Omega_(j+1) is inside Lambda_j (Y 73091), so zone m is inside Omega_m, which is inside Lambda_(m-1); nonempty lower zones have m >= n_c by (b). (d) "zone n is inside Omega_(n+1)^c, inside Lambda_(n+1)^c = Z_(n+1)", so C meets Z_(m+1) and j(C) <= m + 1 (III 13793-13800); age(C) = k - j(C) < a_0 gives the last bound. QED
Reading. The outline's pointwise failure needs "a bare region where the real field is unrestricted", with a plaquette U_p = -I (O 5348). By (c) an aligned label has no such region when n_c >= 2: every zone carries the tests of the level below it. Check 1408 L65 said this in words ("It constructs no such good label"). Lemma AL is the statement.

**4.2 Input (REG-P), printed in three places, not proved here.** On the support of the label's tests, at each real field F at which a coupling-weighted Wilson term of Section 3 is evaluated, the bare plaquettes of layer l satisfy
  norm(dF(p) - 1) <= C_R R_l^2 eps_l eta_l^2,   eta_l the bare mesh in level-l units, R_l = Ř_l.
Printed: for the old core and U''(xi), "Where that cutoff is nonzero the real inner datum gives curvature C Ř_l^2 eps_l eta_l^2 on layer l" (Y 77210-77212); for later reads, abs(dU_k - 1) <= C R_j^2 eps_j eta_j^2 "with no loss in k - j" (O 18191-18198); for the drop-out fibre, "The field is regular layer by layer, as on the support of a history" (O 18148-18149) and "Layer regularity is imposed both on U and on the relevant stored averages" (Y 74098-74100). The only exception printed is "The bare layer uses the uniform Wilson bound" (Y 77216-77217). Owner of the support identification: PD-REST. Not verified here: that the layers of a prepared sequence inside a component of an aligned label never include layer 0 (true for the label's own zones by Lemma AL; for the prepared layers it needs t_flat >= 1, which I did not read).

**4.3 Lemma WIL (a weight change against a regular field is a site charge at the printed load).** Let F be a real SU(2) field satisfying (REG-P) on a set of N_l unit cells of layer l, and let delta c be a real weight on its bare plaquettes there. Then
  abs( A(delta c, F) ) <= C_4 C_R^2 R_l^4 eps_l^2 sup(abs(delta c)) N_l,
with C_4 the number of plaquettes per bare site. If moreover eps_l^2 <= C g_l^2 (log x_l)^(2 p_0), R_l <= C (log x_l)^(r_pr) and q_flat >= p_0 + 2 r_pr, then
  abs( A(delta c, F) ) <= C' gfrak_l sup(abs(delta c)) N_l,   gfrak_l := g_l^2 (log x_l)^(2 q_flat).
Proof. For real U in SU(2), a(U) = (1/2) norm(U - I)^2 (O 5320-5332). So a_p(F) <= (1/2) C_R^2 R_l^4 eps_l^2 eta_l^4. A unit cell of layer l holds at most C eta_l^(-4) bare plaquettes (O 5335). Multiply and sum. The second line inserts the three inequalities. QED
The three inequalities are printed: eps_j^2 <= C g_j^2 (log x_j)^(2 p_0) and q_flat >= p_0 (Y 130613-130615); q_flat >= p_0 + 2(d+1) r_pr + 1 (III line 18, the order of exponents). The form R_l = (log theta_l)^r is Y 73431 and 73074-73075 (R_j = Ř_j, ell_j = log theta_j); I did not verify that the r there is the r_pr of III. This lemma is the outline's regular channel (O 5334-5344: "The usual scale alpha_n^2 ~ theta_n^(-1) (log theta_n)^(2q) has precisely the form of the coefficient multiplying a marginal amplitude in the load"), with the factor R_l^4 kept.

**4.4 Corollary WIL-z.** For the two runs, sup abs(x^B_(l) - x^A_(l)) = z_l (III 12010; x = theta - zeta). So a term -(x^B - x^A) A(mask, F) on N_l cells of layer l, with F as in (REG-P), is at most C' gfrak_l z_l N_l in modulus. The load of zone l holds gfrak_l z^sharp_l with z^sharp_l >= z_l + z_(l-1) (III 12014, 12049). So the term is at most C' l_l N_l, and a term on zone m with the weight of level m-1 is at most 2 C' l_m N_m when gfrak_(m-1) <= 2 gfrak_m.
This replaces row 1406's Proposition NS as the statement about the actual Wilson coefficient terms of a good aligned label. Proposition NS stays true under its hypothesis; its hypothesis (a fixed fraction of free plaquettes with a_p >= 1 on P_h) is excluded by (REG-P) and Lemma AL.

## 5. log w^B - log w^A on P_h, term by term (written 2026-11-22T22:17Z by date -u)

Setting: a good aligned label h, the leaf resolution (live components resolved into the variables of Section 3; everything healed kept as a stored number), a point of P_h = S^A ∩ S^B, zero residual source, real centres. Conventions of check 1408: a positive factor f gives log f_B at its B read minus log f_A at its A read; a weighted action gives the coefficient part -<c_B - c_A, a_A> and the moving-read part -<c_B, a_B - a_A> (L65); a stored output is compared as a value (L21). "Site charge" means: at most K (k-b+1)(l_b + l_(b-1)) per cell of zone b, the shifted charge that check 1408 L41 confirmed.

| # | Term of Delta_h | Type | Source | Class | Bound on P_h and its standing |
|---|---|---|---|---|---|
| D1 | Haar and Lebesgue reference measures, tree constraints on the relative variables, fresh box Haar of type S | all | III 11879-11886; Y 130233-130236, 76475-76476 | zero | 0, given the history-and-slot bijection that check 1408 L19 asks for (COMMON+) |
| D2 | Tests and characteristic functions | all | Y 72680-72682, 74994 | not in Delta_h | they define P_h; the test leg and (SHELL) are separate (row 1404, Theorem CAP) |
| D3 | Free outgoing field of type S | S | Y 72679-72680, 75682-75684 | zero | 0: the term is constant in it. Row 1406's F8 is not a term |
| D4 | Carrying action of a drop-out, coefficient part: -<upsilon^B - upsilon^A, a_p(U)> on the bare plaquettes with corners in X | S | Y 74072-74076, 74090; O 18134-18137, 18156-18157 | action difference | site charge by Corollary WIL-z, GIVEN (REG-P) for the fibre field (O 18148-18149). PROVED GIVEN (REG-P) |
| D5 | Carrying action, moving read: -<upsilon^B, a_p(U^B) - a_p(U^A)> | S | O 18139-18146, 18171-18174 | read difference | zero if the fibre field is a common chart variable; otherwise (RD-BG) below. NOT DECIDED: the text gives the fibre as a set of evaluations, not one map |
| D6 | Inner Wilson term, coefficient part: -(x''^B - x''^A) A(zeta_1 1_X, U''(xi)) | C | Y 73913-73917, 77200-77201; III 32187-32193 | action difference | site charge by Corollary WIL-z GIVEN (REG-P) on the old core (Y 77210-77212). The printed bound C_W c-bar N_0 (Y 77213-77216) is the same count before the factor R_l^4 eps_l^2 is kept |
| D7 | Inner Wilson term, moving read: -x''^B [A(zeta_1 1_X, U''^B(xi)) - A(zeta_1 1_X, U''^A(xi))] | C | Y 73918-73921 | read difference | zero if the inner background map reads only xi and scaffold data. NOT DECIDED; otherwise (RD-BG) |
| D8 | Main quadratic -(1/2)[q_X^B - q_X^A] | C, R | Y 73952-73953, 77207-77209; O 18057-18058 | quadratic difference, field only | the coefficient is theta in both runs, so the coefficient part is 0. The field part moves the glued background only; with abs(B) < r_t = A_1 p_1(g_t) (Y 74994-74995) it is a bounded form. Site charge GIVEN (RD-BG) |
| D9 | Stored strip quadratics: -(1/2)(tau^B - tau^A) <A^s_j, K_A A^s_j>, tau = x/theta | C, S (kept forms) | Y 74894-74903, 74983-74986 | quadratic difference, coefficient part | abs(tau^B - tau^A) <= z_j / theta_j. Site charge IF the support bounds the strip field: (BND-S). Otherwise this is the named excess (STRIP-Q) of Section 6 |
| D10 | Stored strip quadratics, field part: -(1/2) <A^s, (K^B - K^A) A^s> at fixed tau | C, S | Y 74985-74986 ("Changing the background changes their quadratic forms and elimination factors") | read difference | as D9, with (RD-BG) in place of z_j / theta_j |
| D11 | Gaussian masses of tau K, their ratios to D_0, determinants of I + (tau - 1) B | C, S | Y 74907-74910, 77290-77296 | scalar | per scalar coordinate abs(log det ratio) <= 2 abs(tau^B - tau^A) <= 2 z_j / theta_j <= 2 gfrak_j z_j on the half-disc, by the convergent logarithm series (Y 77290-77291). Site charge, PROVED GIVEN that count: coordinates per stored site are bounded (Y 75050-75051) |
| D12 | Gauge normalizers z(a_j(y)) / z(x_j), the one-point pieces | all | III 11914-11921; Y 130606-130617 | scalar | printed: "The change of the gauge exponent on a cube is at most C E_1 eps_j^2 / gfrak_j [...] this is C E_1 per cube on the admitted dial" (Y 130611-130616). Site charge as printed, for the omitted cubes of the label |
| D13 | Pivot and elimination factors J_c = abs(det m_c)^(-1) | C, S | Y 75023-75044 | read difference | they depend on the chart row V only; equal at a common chart point unless the row is read through a run's background. (RD-BG) |
| D14 | Restored identity, the terms linear in the run's weight: -A(w', W-bar) (carrying), -A(w zeta_1, W^in(f)) (core), -A((w - theta) zeta, W''), A((w_fr - w)(1 - zeta_0), W-bar), W_X = A(w' - w_fr, W-bar), and the three Delta_w terms | R | Y 73961-74027 | action difference | each is a weight (x^B - x^A) times a mask against a real field of (REG-P), or a difference of two such. Site charge by Corollary WIL-z, GIVEN (REG-P) at W-bar, W'', W^in |
| D15 | Restored identity, the theta terms and I_X - E_X | R | Y 73944-73947, 73975-73979 | read difference; scalar | coefficient theta is common; they move only through the exterior data and the chart multiplier V^c_Lambda. "E_X is included once in the scalar normalization" (Y 74048). (RD-BG) and (SC-CELL) of row 1406 |
| D16 | Live arrest: sum_z D_W^z at the root | L | Y 129652-129676 | stored-leaf-like (marks at a live site) | site charge as printed: abs(D_W^z) <= K_G N(W) Delta_n^c on disjoint collar cells. Check 1408 L30: identify the filing cells with the charged cells |
| D17 | Stored boundary leaves B, B' read by a live component or at the top: stored members | all | III 13106-13119 | stored-leaf difference | site charge by the per-cell domination (III 13337-13393), with (INC-1) and the shifted load: row 1406 4.1, confirmed by check 1408 L39-41 |
| D18 | Reading parts G^rd and own members G^own of those leaves | all | III 13120-13133 | read difference; stored-leaf | "accounted for by the last entry of the classical load" (III 13126-13128); per-cell sums are (PC-RD), owner ZONE-FORM |
| D19 | List leaves E, P-flat, Q, R, D; zeta-, b- and weight entries outside live components | all | III 11968-11972, 12963-12967 | stored-leaf difference | loads S^+_i[E], S^+_i[R], gfrak_j [z^sharp_j + ...] (III 12047-12049); per-cell form (PC-LIST), owner ZONE-FORM |
| D20 | Kept potential V_X of a live component beyond D14, D15: localized terms formed from the run's array | C, R | O 18078-18098; Y 77183-77204 | stored-leaf and read | the printed bound abs(V_X) <= C N_0 is a modulus bound, not a difference bound: "Their absolute bounds include the unpaired plain values" (Y 77221-77222). A difference bound is the formation test O (eq:zr-formation-test). Owner ZONE-FORM. OPEN |
| D21 | Label scalars: vacuum terms of cubes not inside Lambda_j(h), node constants, E_X | all | III 11905-11921 | scalar | (SC-CELL) of row 1406 4.2. OPEN, owner ZONE-FORM |
| D22 | Run-level vacuum constant | - | III 11923-11926 | scalar | outside Delta_h, removed by (RULE) (row 1395) |

Counting rule applied: D4, D6, D14 are the native form of the zeta-entries inside live components (fact (W3)); D19 holds the zeta-entries outside them. No entry is in both.

**5.1 The two named inputs for the read and quadratic terms.**
 (RD-BG) At a common chart point of P_h, each real background of Section 3 (U'', W-bar, W'', W^in, the glued background, V_Lambda, M_B''(U_0)) differs between the runs by a field whose plaquette norm on layer l is at most C (z^sharp_l / theta_l) R_l^2 eps_l eta_l^2. With (REG-P) and the first-order expansion of the action this makes every moving-read term a site charge of the size of Corollary WIL-z. It is a response bound of a constrained minimizer to a change of the weight profile. It is not printed in the passages read. It is an instance of the outline's requirement "If a parameter changes the arguments as well, prove the corresponding derivative bound" (O 5443). Owner: ZONE-FORM. If the background maps read scaffold data only, (RD-BG) holds with zero.
 (BND-S) On S_omega every stored strip coordinate satisfies abs(A^s_j) <= C (log theta_j)^(p_1). Then D9 is at most (z_j / theta_j) Gamma C^2 (log theta_j)^(2 p_1) <= C'' gfrak_j z_j per coordinate when q_flat >= p_1, a site charge. Not printed where I read: the reference bound integrates the strip fields over "the full Euclidean spaces" after "Dropping restrictions" (Y 74958, 75016-75018), which leaves open whether a restriction exists. Owner of S_omega: PD-REST.

## 6. Decisive outcome (written 2026-11-22T22:17Z by date -u)

**6.1 What is established.** For a good aligned label, on P_h:
 (i) Row 1406's excess does not exist. The free outgoing field has no weight (D3). Every Wilson term with a run-dependent coefficient (D4, D6, D14) is evaluated at a field of (REG-P), and Lemma AL removes the bare unrestricted layer. Corollary WIL-z then gives the site charge at the printed load, with the one-level shift already on file. PROVED GIVEN (REG-P); unchecked.
 (ii) The main quadratic has the common coefficient theta (D8). Row 1406's F9 with a coefficient difference Q^B - Q^A does not occur for it.
 (iii) One coefficient term can leave the site charge: the stored strip quadratic D9.
   **(STRIP-Q)** X_h := sum over live histories and levels j of (1/2)(tau^B_j - tau^A_j) <A^s_j, K_(A,j) A^s_j>, with abs(tau^B_j - tau^A_j) <= z_j / theta_j <= C gfrak_j z_j (log x_j)^(-2 q_flat) <= C l_j (log x_j)^(-2 q_flat).
  Its coefficient is controlled and smaller than the load by a power of the logarithm. It is a site charge exactly under (BND-S). Without (BND-S) it is unbounded pointwise along a Gaussian direction, and it is then the target of a moment row, of Gaussian type: the printed reserve "the unspent part of the complete forms gives at least beta sum_j abs(A_j)^2" (Y 74956-74957), with K_A <= Gamma, gives per coordinate E exp(eta Gamma y^2 / 2) <= (1 - eta Gamma / (2 beta))^(-1/2), a cost at most eta Gamma / (2 beta) <= C l_j per coordinate for eta Gamma <= beta. The coordinate count is at most C N_0 (Y 75050-75051). This is Lemma G1 of row 1406 without the conditioning. It is a computation in a product model; under the restricted A law it is the statement (QS-M) of Section 7.
 (iv) Everything else is a read difference, a stored-leaf difference or a scalar, with the owners named in the table: (RD-BG), (PC-RD), (PC-LIST), (SC-CELL), (INC-1), the formation test for V_X (all ZONE-FORM), (COMMON+) and (BND-S) (PD-REST).

**6.2 Verdict.** Neither of the row's two outcomes holds unconditionally.
 - The Wilson action of free bonds is NOT a remaining excess. `gap-univk-actx` as written by row 1406 has no target and should not run (as check 1408 advised).
 - The complete difference fits site charges GIVEN (REG-P), (RD-BG), (BND-S) and the ZONE-FORM site inputs. Then the one-law count moment (CAP-M0) of check 1405 L38 suffices for the weight leg.
 - If (BND-S) fails, the single named excess is (STRIP-Q), with coefficient z_j / theta_j. It is a Gaussian quadratic, not a Wilson action, and its moment is (QS-M).
 Theorem MA of row 1406 (confirmed by check 1408 L45) takes either case: with S_j := the strip quadratic and eta_j = z_j / theta_j.

**6.3 Is this equivalent to the open target?** No. (REG-P), (BND-S) and (RD-BG) are one-run or one-label statements about supports and background maps. They compare no two total masses. The comparison content stays in (CAP-M0), (SHELL), the test leg and ZONE-FORM. I cannot show that ZONE-FORM's inputs are weaker than (LOG); check 1408 L85 gives separations for the moment inputs only.

**6.4 Remark ZENV (a fallback that needs no regularity; PROVED GIVEN two printed bounds).** The printed envelope step gives z_s' <= C_zeta (1 + s') e_s' for s' in [w, n] (III 17216-17218) and e_(s+m) <= rho^(-m) e_s (III 17232). A zone at distance d = k - b from the stop has depth w + d (III 17357-17363, as cited by check 1408 L81). So
  sum_b (k - b + 1) q_a^((k-b-1)_+) z_b <= C_zeta e_w sum_(d >= 0) (d + 1)(1 + w + d) q_a^((d-1)_+) rho^(-d) <= C (1 + w) e_w,
because q_a <= rho^4 (III 17370). So the load augmented by the bare shift, l_b + z_b, has the envelope C (1 + w) e_w. At a fixed stop depth w this is the printed rate with a larger constant. It sharpens check 1408 L81 (which had x_b in place of 1 + w + d). It is not uniform in w. It is not needed when Corollary WIL-z applies.

## 7. Next two rows and their decisive outcomes

**Row 1, `gap-univk-native-ends-check` (cross-provider check of this row).** Check: the type table of Section 3 against Y 72678-76486 and O 18026-18204 (is any factor with a run-dependent coefficient missing; is the strip form Q_tau really in the kept factors of a live history); Lemma AL (d) and the claim that prepared layers of an aligned label exclude layer 0; Lemma WIL's exponent count (is the r of Y 73431 the r_pr of III line 18); the counting rule under (W3) (no zeta-entry counted twice); Remark ZENV.
 Decisive outcome: if a coupling-weighted term at an unrestricted field is found in a good aligned label, name it; it is the action excess and Section 6.1 (i) falls. If none, the Wilson channel of the weight leg is closed GIVEN (REG-P).

**Row 2, `gap-univk-strip-reads` (proof row, one label, real points).** Decide (BND-S) from the definition of S_omega (CMP 122b (1.70)-(1.71) through `library/pd.md`, and Y 74981-75021). If it fails, prove (QS-M): under the restricted A law of the good labels, E exp( sigma sum_j <A^s_j, K_j A^s_j> ) <= e^(E_S V) for one sigma > 0, from the unspent Gaussian reserve (Y 74956-74969). Then decide (RD-BG): write the inner and glued background maps as functions of (xi, weight profile) and bound their derivative in the profile (start from Y 73985-74009, the graded row response and the screened background comparison).
 Decisive outcomes: (1) (BND-S) or (QS-M) holds and (RD-BG) holds with the factor z^sharp / theta: the weight leg needs only (CAP-M0) and ZONE-FORM's site inputs, and no action-moment row. (2) a background moves at order one in the profile (no factor 1 / theta): then the moving-read term is the named excess, of size z times a regular action, and Remark ZENV is the only printed way to pay it (rate with the factor 1 + w).
Order: Row 1 first. It is short, and Row 2 is wasted if a missing term is found.

## 8. Status

| Statement | Mark |
|---|---|
| Section 3 tables | READ, lines quoted; arrangement by type mine; unchecked |
| Lemma AL | PROVED from the printed label definitions; unchecked |
| (REG-P) | printed in three places (old core, later reads, fibre); support identification with PD-REST; prepared layer 0 not verified |
| Lemma WIL, Corollary WIL-z | PROVED GIVEN (REG-P) and three printed exponent inequalities; unchecked; the identification r = r_pr not verified |
| D3 (free field has no weight), D8 (common coefficient theta) | READ |
| D11 scalar bound | PROVED GIVEN the printed coordinate count; unchecked |
| Remark ZENV | PROVED GIVEN III 17216-17218, 17232, 17370; unchecked |
| (STRIP-Q) as the only coefficient term that can leave the site charge | ARGUED from the inventory of Section 3; holds only if that inventory is complete (Row 1) |
| (BND-S), (RD-BG), (QS-M), (COMMON+), D5, D7, D20, D21 | OPEN |
| (INC-1), (PC-RD), (PC-LIST), (SC-CELL), formation test for V_X | OPEN, owner ZONE-FORM (not redone) |
| (CAP-M0), (SHELL), test leg, (RAR), term D, (GEO), (LOG), the seed | OPEN, untouched |

No numeric job was run; none was needed. Memory was 57 percent free at the start. Files written in the repository: this file only. Scratch: /tmp/ym4d-native-ends-w2/src (the short outline, fetched by URL at 31a47c543775). Parts I and II were not fetched.

Finished 2026-11-22T22:17Z (date -u). All steps of the plan are done; Sections 1 to 8.

RESULT: Reading row done, author only, unchecked. Per type (shell exit, completed, restored, live arrest) the native terminal density is written factor by factor with its run dependence. For a good aligned label on P_h: the free outgoing field carries no weight, so row 1406's Wilson excess is not a term; every Wilson term with a run-dependent coefficient sits at a layerwise regular field and is a site charge at the printed load (Lemma AL: an aligned label has no bare unrestricted zone; Lemma WIL and Corollary WIL-z; PROVED GIVEN the printed regularity (REG-P)); the main quadratic has the common coefficient theta. Neither decisive outcome holds unconditionally: the difference fits site charges GIVEN (REG-P), a background response bound (RD-BG), a support bound on the stored strip fields (BND-S) and ZONE-FORM's site inputs; if (BND-S) fails the one named excess is the stored strip Gaussian quadratic (STRIP-Q) with coefficient z_j/theta_j, a Gaussian moment target (QS-M), not a Wilson action moment. gap-univk-actx as written has no target. Remark ZENV: the bare-shift envelope is C(1+w)e_w from printed bounds. OPEN: (RD-BG), (BND-S) or (QS-M), (COMMON+), the formation test for V_X, (INC-1), (PC-RD), (PC-LIST), (SC-CELL), then (CAP-M0), (SHELL), the test leg, (RAR), term D, (GEO). Next rows: a cross-provider check of this row, then gap-univk-strip-reads.
