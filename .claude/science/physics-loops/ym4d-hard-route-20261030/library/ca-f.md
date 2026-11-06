lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T00:31Z

# ca-f: step F of `library/ca-claude.md`, the completion layers at the collar (FINISH row 386)

Provenance: Claude Opus 5.5, max effort, Mac mini worker; checkout pinned at `9c36ea22b`; 2026-11-06. Research text, not an audit, no status. Proved by Claude, not yet checked by the other model. No computer-assisted step and no numerical run was used.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number below. In particular the partner current of a cut layer (`4.25:lem-cut-layer-partner`), the current-partner estimates (`4.25:lem-current-partner`), the cancellation identity of `4.22:lem-current-localisation` and the weighted Lipschitz form of the layer theorem are theirs. Tadeusz Balaban for the current formula CMP 109 (3.11)-(3.13) and the walk-difference theorem CMP 99b Theorem 3.14. `library/ca-claude.md` (Claude, Mini worker) for Lemmas A, B, E and Proposition C, used here as written.

Kind of result (How we work, item 9): proof of a step the account assumes, namely the bound on the layers and their currents on the collar at the completion site (CA-I 142563-142574, the "collar corollary" read through the level-zero chain proposition). It is an implication from named inputs. It replaces the second route of Proposition F in `ca-claude.md` section 6.3.

## 0. Summary

1. **The interface (section 2).** Step F needs (IF-a), the four entries of each completion layer at the collar with a decay in d_sc(., S), and (IF-b), the current of the actual segment t_s H_s. The second route of Proposition F fails at two places: it cuts the field datum f_1 into cube pieces whose datum norms the account does not bound (D1), and it reads the source identity at t_s < 1, where no associated fields are defined (D2).
2. **Lemma S (section 4), proved.** The account's own partner current of a cut layer, at cut parameter 0, is the segment current. Its commutator vanishes, so the incomplete step (*) of `4.25:lem-cut-layer-partner` is not used. For every t in [0,1], eta^3 |s^#[t H]| <= t Kcur E_y(H), with the same Kcur = 3 + 18d + 2.2 K_J as `ca-claude.md`.
3. **Proposition R (section 5), proved as an implication.** One weight p_T = e^{-delta_R d_sc(., T)} serves the whole datum; it lies in the account's weight class by d^ >= w d_sc alone. The field datum is never cut: after the cancellation it is a field datum of a current supported in T (weighted field-datum lemma) plus the decoupling bracket (Balaban's walk-difference theorem in the datum norm). The layer theorem then gives the four entries at the collar with decay e^{-delta_R d_sc(y,S)}, and Lemma E turns this into e^{-delta_R [(Rc_k - 1) + (L-2)(h-1)]}.
4. **Proposition F' (section 6), proved as an implication.** With k = h + Rc_k, (CL) of `ca-claude.md` holds on the whole square under one ceiling (Gamma_F) of supremum form on gamma, chosen last. Proposition C then gives CA as in `ca-claude.md`, with the inputs of section 3 in place of its item 2.
5. **Open.** The inputs (N1) (the layer theorem, owner `stage-claude`) and (N3) (CMP 99b Theorem 3.14 in the datum norm, registry B99b-T314, no owner) are cited, not rebuilt; (G-sep) is the account's placement of the sources, not re-derived. (B-in) is still the first place CA can fail.

## 1. Sources and scope

- **Two files the row names are missing.** `gates/ca-gate.md` and `library/prior/b-in.md` are not in this checkout at `9c36ea22b`. `git log --all` finds neither, and `git ls-remote` gives the remote head `9c36ea22b` too, so they were not pushed. I read the BLOCK only from FINISH rows 382 and 386: "BLOCK at step F of library/ca-claude.md, the passage from the localised layer bound to the full response tuple and current, including partial layer segments (needs the response theorem in its weighted datum norms and the current of the actual segment)"; "Prove the interface the gate names (the response theorem in its weighted datum norms after cancellation, and the current of the actual segment t_s H_s with controlled associated fields)". If the gate names a further defect, this note does not treat it.
- **No duplicate attack.** I grepped `library/open-core.md`, `library/l17c.md`, `library/open-registry.md` and the FINISH rows. Step F is covered only by rows 347 (`ca-claude`), 382 (`ca-gate`) and 386 (this row). Two inputs below belong elsewhere, and I do not attack them:
  - the layer (response-field) theorem, which `library/stage-claude.md` section 2.4 records as cited but absent from the account (its antecedent (L); owner `stage-claude`, H-STAGE rows of `open-registry.md`);
  - Balaban CMP 99b Theorem 3.14 (registry row B99b-T314, published statement cited by statement, no owner).
- **Account sources.** CA-I, CA-II, CA-III and the outline fetched by URL into a scratch folder of this lane. SHA-256 values agree with `arr.md` section 1. Line numbers below are of those raw TeX files (I: = CA-I, II: = CA-II). Balaban CMP 99b pp. 426-427 and CMP 109 pp. 271-273 read in the OCR in `~/ym4d-papers`.
- **Used as written.** Lemmas A, B, E and Proposition C of `ca-claude.md`. The gate (row 382) gave Lemma A, Lemma B (from (B-in) and S-B), Proposition C and Lemma E ADVANCE. (B-in) stays open; this note does not touch it.

## 2. What step F must deliver, and where the second route of Proposition F fails

**The chain.** At a completion date d' = (k;L) the presented chain on the core is (I:142563-142570)

  e^{i eta t_4 H_4} e^{i eta t_3 H_3} U_2,   J_2 + s^#_{sigma_3}[t_3 H_3] + s^#_{sigma_4}[t_4 H_4],

with b2, b3, b4 the points (t_3,t_4) = (0,0), (1,0), (1,1); the consumers read these and the segments between them (I:142334-142338). Each layer H_s is built by the account at its own kernel (W_s, sigma_s), with W_3 = U_2. The left-factor step reads the size of H_s with the covariant derivative at the pair after the preceding layers (I:142476-142480). Nothing below depends on whether the account builds H_4 at U_2 or at e^{i eta H_3} U_2: Lemma S is applied at the kernel of each layer, and the size N_y is bounded for any base by the lattice fact of `ca-claude.md` section 6. So (CL) is proved on the whole square [0,1]^2, as Proposition C of `ca-claude.md` reads it.

**The account's own sentence for the segments** (I:142571-142577): "The parameters t_s enter through the definition of the layer currents s^#_{sigma_s}[t_s H_s], which carries them. Clauses (i)-(iii) of the level-zero chain proposition bound every entry by functions increasing in the layer sizes F_s." The level-zero chain proposition is assumed there (hypothesis (e) of `4.27:prf-displacement-averaging`, I:142269-142291) and is printed nowhere. So step F must supply exactly the following.

**Interface (IF).** For s in {3,4}, write (A'_s, X_s, H_s) for the layer datum of the layer theorem at the kernel (W_s, sigma_s): potential, auxiliary field, layer. For a block (cell) y of the determining set put the four entries of CMP 109 (3.14) (I:111406-111411); at a level-zero block l_y = eta

  E_y(H_s) := max{ N^Delta_y(A'_s), N_y(H_s), l_y^3 |P_1(sigma_s) A'_s|, l_y^3 |m_H(sigma_s) X_s| }.

- (IF-a) *Response tuple at the collar.* For every y in the read sets of Col(C), E_y(H_s) is bounded by a budget term times a decay e^{-delta d_sc(y,S)} with delta > 0 independent of k, h, the history and the parameters.
- (IF-b) *Current of the actual segment.* For t in [0,1] and every bond b at y, eta^3 |s^#_{sigma_s}[t H_s](b)| <= K t E_y(H_s), with K fixed before gamma.

(IF-a) and (IF-b) give (CL) of `ca-claude.md` section 5 once gamma is small (section 6 below).

**Defect D1 of the second route (the cut of the field datum).** Proposition F cuts f_1 into its restrictions to M-cubes Q and applies clause (b) of the layer theorem to each piece, with the weight e^{-delta_P d^(.,Q)}. But f_1 is the first argument of H_3, namely the field G''(sigma) J^{b2} rewritten by the cancellation (4.22:eq-current-localisation-a), I:92472-92477 and I:92573-92582. The account measures a field datum in the weighted norm ||.||^Delta_p (I:72532-72537; I:142537: ||G~_0(sigma_3) J_3||^Delta_p <= K_# ||J_3||_p). That norm reads derivatives. A sharp restriction 1_Q f_1 has no bound in it, and the account supplies only the pointwise bound |f_1(y)| <= C sup|J^{b2}| e^{-delta_G d_sc(y,S)}. So the per-piece application of clause (b) is not justified, and the telescoped sum has no proof. (If the layer theorem took a field datum in a weighted sup norm, D1 would not arise; but both uses of the field-datum norm in the account are of the Delta type, with derivative entries as in I:94880-94884.)

**Defect D2 of the second route (the current at partial t).** Proposition F reads the source identity j = (Delta_U - P_1 + K) A' - m_H(X) + F(U,H) (I:94983-94986) at t_s H_s. That identity is stated for the solution itself, at t = 1. For t < 1 the field t H is not the layer of any datum named in the account, so "the associated fields of t H" are not defined, and the five-term estimate has nothing to act on.

Sections 4 and 5 repair D2 and D1. Neither repair cuts the field datum, and neither reads the source identity at t < 1.

## 3. Named inputs

Each input is a statement the account uses at the completion site or at the analogous site, read on its stated class. The readings are marked. Constants named here are fixed before gamma.

- **(N1) Layer theorem, clauses (a) and (b), in weighted norms.** There are a class M_delta of weights, a datum norm ||.||_{dat,p} for p in M_delta, and a constant B_H, such that for every kernel (W,sigma) of the theorem's class with |sigma| <= e^{kappa_1}, at any determining set, and any two admissible data d_1, d_2 with layer data (A'_i, X_i, H_i), at every cell y,

    max{ N^Delta_y(A'_1 - A'_2), N_y(H_1 - H_2), l_y^3 |P_1(sigma)(A'_1 - A'_2)|, l_y^3 |m_H(sigma)(X_1 - X_2)| } <= B_H ||d_1 - d_2||_{dat,p} p(y);

  and the layer datum vanishes at the datum 0. Sources: clause (b) as the account states it (I:141777-141785), the five weighted norms bounded by B_H (I:112588-112610), the bound read at a point and clause (a) at datum zero (I:72519-72527). *Reading:* every weighted norm here has the form sup_x (local size at x)/p(x), as the account reads it at I:72524-72527 ("the weight p equals 1 on supp b, so the weighted norm of b is sup|b|"); so p <= p' pointwise gives ||.||_{p'} <= ||.||_p. The datum is a pair (field datum, block datum), and its norm is at most the sum of the two component norms. This is the antecedent (L) of `stage-claude.md`; it is not attacked here.
- **(N2) Field-datum lemma, clause (a), in weighted norms.** For p in M_delta, |sigma| <= e^{kappa_1} and every current J: ||G''(sigma) J||_{dat,p} <= K_# ||J||_p, where ||J||_p := sup_x l_x^3 |J(x)| / p(x). Sources: I:72532-72535 (weight e^{-delta_P d^(.,supp J)}) and I:142537 (weight e^{-delta d^(.,Z_L)}). *Identification:* G''(sigma) is the field-datum operator of the layer H_3, since the account's first argument of H_3 is G''(sigma) J^{b2} (I:92573-92574); the alternative derivation names the same operator G~_0(sigma_3) (I:142537).
- **(N3) The decoupling difference in the datum norm.** There are K_br and delta_br > 0 such that for |sigma| <= e^{kappa_1} and every current mu supported in D_2°,

    || [G''(sigma) - G''(1)] Q''^* mu ||_{dat,p_br} <= K_br sup|mu|,   p_br(x) := e^{-delta_br d_sc(x, Lambda^c)}.

  Source: hypothesis (e) of `4.22:lem-current-localisation` cites "the walk representation [CMP 99b Theorem 3.14, (3.154)] of the dependence of G''(sigma) on sigma" (I:92460-92463). Balaban's Theorem 3.14 (CMP 99b pp. 426-427) states that the difference of two such operators "satisfies all the inequalities characteristic for operators of the considered type, with the additional factor exp(-delta_0 d(y,y'|Omega))", d(y,y'|Omega) = inf over y_1 outside Omega of |y - y_1| + |y_1 - y'|. The decoupling parameters sit only on cubes disjoint from Lambda (I:92415-92417), so the walks inside Lambda carry the same coefficient in G''(sigma) and G''(1), and d(y,y'|Omega) >= d(y,Lambda^c). The account uses this only in pointwise kernel form (I:92560-92571). (N3) is the same factor for the inequalities that make up the datum norm of (N2). Registry row B99b-T314; not attacked here.
  *Caution for the owner of (N1)-(N3).* G''_k is the propagator of CMP 99b Theorem 3.13 (hypothesis (e), I:92460-92461). Theorem 3.13 holds "with the exception of the inequality in (3.42) involving the covariant Laplace operator" (CMP 99b p. 426). If the datum norm of a field datum contains a covariant-Laplacian entry, then neither (N2) nor (N3) follows from Theorems 3.13-3.14 as printed; Balaban obtains second-order bounds for layers from the second representation and the Landau gauge (CMP 109 p. 272). This bears on (N2) as much as on (N3), so it is a question for the antecedent (L), not for step F.
- **(N4) The cancellation and the supports** (`4.22:lem-current-localisation`, index PROVED, I:92401-92625). The first argument of H_3 is f_1 := G''(sigma) J^{b2}, and by (4.22:eq-current-localisation-a) (I:92472-92477)

    f_1 = G''(sigma) J^c + beta,   J^c := 1_{(D_2°)^c} J^{b2} + r,   beta := [G''(sigma) - G''(1)] Q''^*(lambda_2 restricted to D_2°),

  with sup|r| <= C_Q sup|J_2| and sup|lambda_2| <= C_lambda sup|J_2|, where C_lambda := ||(QQ^*)^{-1}Q|| and C_Q = 1 + ||Q^*|| C_lambda depend on d and L only (I:92424-92428, I:92537-92553). The second argument of H_3 and the argument g_k B of H_4 are supported in S (I:92583-92587).
- **(G-sep) Position of the sources** (reading of the same proof). Put T := S united with supp J^c and Lambda^c. For every z in Z_h and every x in T, d_sc(z, x) >= d_sc(z, S) - 1. Sources: "The sources on the side of Omega''~_{h+1}, localised or not, lie in S" (I:92496-92497); r lives in the blocks adjacent to the boundary of D_2°, where D_2° is the union of the blocks of D_2 at block-distance at least 2 from the graded layer at the cut (I:92465-92471); "as seen from Z_h, Lambda^c lies beyond S" (I:92569-92571). The account's conclusion (c1) is stated with exactly this loss, e^{-delta_L (d_sc(z,S) - 1)} (I:92481-92484), and its proof bounds every source of f_1 through d_sc(., S). *Reading:* a point of supp J^c lies on the side of the cut, or in the graded part of D_2 next to the cut, or outside Lambda or in a block adjacent to Lambda^c; each such point is, as seen from Z_h, at least as far as S less one unit. CMP 122b (1.50)-(1.55), where D_2 is fixed, is not available here, so this placement is the account's and is not re-derived.
- **(N5) Weights and distances.** (i) d^ >= w d_sc (I:91723-91728). (ii) A positive weight p with p(y) <= e^{delta d^(y,y')} p(y') for all cells y, y' lies in M_delta. *Reading:* this is the property that "membership in this class requires" at II:6179-6189 (for M^wedge_{delta_P/2}) and the one used at II:57620-57626 (for M_delta); exponential weights in d^ are admissible (I:72519-72523, I:112607-112609).
- **(N6) The partner current of a cut layer and its estimates.** The definition (I:111538-111545), for chi := t + tau chi^_square,

    J^#[chi] := (Delta_W - P_1(sigma) + K)(chi A') - chi m_H(sigma) X - [D_W^* D_W, chi] H(sigma) X + F(W, chi H),

  the product rule and the commutators [D_W, chi] = E_chi, [D_W^*, chi] = E'_chi (I:111590-111612), and the two estimates of `4.25:lem-current-partner` (PROVED): l^3 |K B| <= 18d p(W) l|B| (I:94996-95001), and l_y^3 |F(W, h)| <= K_J (1 + 1/20) 2 N_y(h) when p(W) <= 1 and N_y(h) <= 1/40, with F(W,0) = 0 (I:111580-111586). The heading of `4.25:lem-cut-layer-partner` says its proof is incomplete at (*); step (*) is the commutator count (I:111614-111626), which is not used below.
- **(N7) Kernel irregularity.** p(W_s) <= 1 at the kernel of each layer (I:115406-115407, stated at presentations of kind (L)); here at the level-zero cells of Col(C). `ca-claude.md` (P2) uses the same; its value at the collar is not re-derived here.
- **(N8) Budget.** Sup norms of currents and block fields are in the scaled units of `4.22:lem-current-localisation` (I:92582). Put J_* := max{sup|J^{b2}|, sup|J_2|}. The budget (d') in the form the account's proof of (c1) uses it (I:92454-92456, I:92612-92618; the proof absorbs C sup|J^{b2}| with C >= 1 and C_Q sup|J_2| into C_L eps_Q(k)): K_u B_H J_* <= eps_Q(k) and K_u B_H (sup|arg_{3,2}| + sup|g_k B|) <= eps_Q(k); and eps_Q(k) <= K_Q alpha^+_k (I:91736-91739), with A^+ and rho_C as in `ca-claude.md` section 6.1 (and the factor t_k^{p_1-q} of its Remark if p_1 > q).
- **(N9) Geometry and scales.** Lemma E of `ca-claude.md` (ADVANCE): d_sc(y,S) >= (Rc_k - 1) + (L-2)(h-1) for y in Col(C), where Rc_k is the account's R-check_k. N_k := Rc_k and h := k - N_k (I:77947-77954), so k = h + Rc_k. Rc_k >= (log(x_k - c_5))^r (I:77940-77942), so R_gamma := inf_k Rc_k tends to infinity as gamma tends to 0 (as in `ca-claude.md` section 6.3). The level-zero ratio bound alpha_{i,k} <= (1+beta_0)^2 k^{1/2} alpha_{i,0} (`4.27:lem-level-zero-ratios` (a), as used at I:142464-142467). The norm of the left-factor algebra at y reads h on Delta~(y), the enlargement of the block Delta(y) (I:141270-141278), and its covariant difference reads h one lattice step further. Every block y' that meets this region has d_sc(y, y') <= 2. The lattice fact of `ca-claude.md` section 6 (proved there): if the base is e^{i eta A'} U with U G-valued and eta|A'| <= 1/80 on the stencil, then eta^2 |nabla h| <= (e^{1/40} + 1) sup eta|h|, so this norm is at most 2.03 sup eta|h| over the region.

## 4. Lemma S: the current of the actual segment (repairs D2)

**Lemma S.** Let (W, sigma) be the kernel of a completion layer, (A', X, H) its layer datum, and y a level-zero cell (so l_y = eta). Assume p(W) <= 1 and E_y(H) <= 1/40. For t in [0,1] put

  s^#_sigma[t H] := J^#[chi = t] = (Delta_W - P_1(sigma) + K)(t A') - t m_H(sigma) X + F(W, t H).     (S.1)

Then for every bond b at y,

  eta^3 |s^#_sigma[t H](b)| <= t Kcur E_y(H),   Kcur := 3 + 18d + 2.2 K_J.     (S.2)

The right side increases with t; s^#_sigma[0] = 0; and at t = 1, (S.1) is the account's representation (4.25:eq-current-partner-1) of the partner current of the layer.

**Proof.** *Step 1: (S.1) is the account's partner current of the cut layer at cut parameter 0.* Put tau = 0 in (N6), so chi is the constant t. Every forward and backward lattice difference of a constant vanishes. So E_chi = 0 and E'_chi = 0 by their formulas (4.25:eq-cut-layer-partner-5), and [D_W^* D_W, chi] = D_W^* E_chi + E'_chi D_W = 0 (I:111612). The account notes the same: "the constant t being annihilated" (I:111631-111632). Thus J^#[t] is (S.1). At t = 1 it is (4.25:eq-current-partner-1). The commutator count (*) is not used.

*Step 2: linear members.* The operators Delta_W, P_1(sigma), K, m_H(sigma) are linear and do not depend on t, so the linear members equal t [(Delta_W - P_1 + K) A' - m_H X]. By the definition of the entry, eta^3 |Delta_W A'| <= N^Delta_y(A') (I:111408-111409). The entries eta^3 |P_1 A'| and eta^3 |m_H X| are entries of E_y(H). By (N6) and (N7), eta^3 |K A'| <= 18d p(W) eta |A'| <= 18d N^Delta_y(A'), since eta|A'| <= N^Delta_y(A') (I:94880-94884). So the linear members are at most t (3 + 18d) E_y(H).

*Step 3: nonlinear member.* For fixed W, N_y is a seminorm in h (a maximum of weighted sup norms of h and of nabla_W h), so it is homogeneous of degree one. So N_y(t H) = t N_y(H) <= t E_y(H) <= 1/40. By (N6), eta^3 |F(W, t H)| <= K_J (1 + 1/20) 2 N_y(t H) = 2.1 K_J t N_y(H) <= 2.2 K_J t E_y(H).

Adding the two steps gives (S.2). At t = 0 every member vanishes, since F(W,0) = 0. QED.

**Remarks.** (1) (S.2) is the account's (4.27:eq-displacement-averaging-4), with F_s := E_y(H_s), now proved at every t and not only at t = 1. The associated fields of the segment are t A' and t X; their entries are t times those of the full layer. This is the "controlled associated fields" of the row.
(2) If the account's segment current is read instead as the linear interpolation t s^#_sigma[H], as in the family Phi_t of I:141764-141767, then (S.2) follows at once from its case t = 1. Both readings give (S.2). A reading that recomputes the associated fields of t H from a new datum is not the account's (it names no such datum) and is not needed.
(3) Lemma S is applied at the kernel W_s of each layer, whatever base the left factor acts on at a given point of the square. The size part of (CL) is treated separately in section 6.

## 5. Proposition R: the response tuple at the collar after the cancellation (repairs D1)

**Proposition R.** Assume (N1)-(N5), (N8) and (G-sep). Let delta be the rate of the class M_delta of (N1), and put

  delta_R := min{delta_br, w delta},   C_D := K_#(1 + C_Q) + K_br C_lambda + 1.

Then for s in {3,4}, every y in Col(C) and every block y' with d_sc(y, y') <= 2,

  E_{y'}(H_s) <= (C_D / K_u) eps_Q(k) e^{3 delta_R} e^{-delta_R [ (Rc_k - 1) + (L-2)(h-1) ]}.     (R.1)

The proof uses one weight for the whole datum. It does not cut the field datum, and the decay comes from the cancellation alone.

**Proof.** *Step 1: the weight.* Let T be the set of (G-sep) and p_T(x) := e^{-delta_R d_sc(x, T)}. Then p_T <= 1, and p_T = 1 on T. For cells y, y', the triangle inequality for the path distance d_sc and (N5)(i) give

  p_T(y) / p_T(y') <= e^{delta_R d_sc(y,y')} <= e^{(delta_R / w) d^(y,y')} <= e^{delta d^(y,y')},

since delta_R <= w delta. So p_T is in M_delta by (N5)(ii). Here d_sc and d^ are taken relative to B''_k, as in the account's (c1). If the layer H_3 is built at B_2, its d^ is larger: B_2 differs from B''_k only by finer blocks in the graded layer at the cut (splice (a3) of `ca-claude.md` Lemma A), and finer zones cost more in len_B (I:63975-63981). So the same chain of inequalities holds with d^_{B_2}.

*Step 2: the datum of H_3 in the weighted norm.* By (N4), the datum of H_3 is the pair (f_1, arg_{3,2}) with f_1 = G''(sigma) J^c + beta. Take the three pieces in turn.
- By (N2) at the weight p_T, ||G''(sigma) J^c||_{dat,p_T} <= K_# ||J^c||_{p_T}. Since supp J^c lies in T, where p_T = 1, ||J^c||_{p_T} = sup|J^c| <= sup|J^{b2}| + sup|r| <= (1 + C_Q) J_*.
- Since T contains Lambda^c and delta_R <= delta_br, p_T(x) >= e^{-delta_R d_sc(x, Lambda^c)} >= p_br(x) at every x. The norm is decreasing in the weight (reading of (N1)), so by (N3) with mu = lambda_2 restricted to D_2°, ||beta||_{dat,p_T} <= ||beta||_{dat,p_br} <= K_br sup|lambda_2| <= K_br C_lambda J_*.
- arg_{3,2} is supported in S, a subset of T, so its weighted norm is sup|arg_{3,2}|.

The datum norm is at most the sum of these (reading of (N1)). With (N8), and B_H > 0,

  ||d_3||_{dat,p_T} <= (K_#(1 + C_Q) + K_br C_lambda) J_* + sup|arg_{3,2}| <= C_D eps_Q(k) / (K_u B_H).

The datum of H_4 is g_k B, supported in S, so ||d_4||_{dat,p_T} = sup|g_k B| <= eps_Q(k) / (K_u B_H) <= C_D eps_Q(k) / (K_u B_H).

*Step 3: the layer theorem.* The layers H_s are the account's layers at these data and kernels, so the data are admissible; the zero datum is admissible and gives the zero layer datum by (N1)(a). Apply (N1)(b) to the data d_s and 0 at the weight p_T. At every block y',

  E_{y'}(H_s) <= B_H ||d_s||_{dat,p_T} p_T(y') <= (C_D / K_u) eps_Q(k) p_T(y').

*Step 4: the distance.* Let y be in Col(C) and d_sc(y, y') <= 2. Then d_sc(y', T) >= d_sc(y, T) - 2. Col(C) lies in Z_h (`ca-claude.md` Lemma A, input (a1)), so (G-sep) gives d_sc(y, x) >= d_sc(y, S) - 1 for every x in T, hence d_sc(y, T) >= d_sc(y, S) - 1. Lemma E gives d_sc(y, S) >= (Rc_k - 1) + (L-2)(h-1). So p_T(y') <= e^{3 delta_R} e^{-delta_R [(Rc_k - 1) + (L-2)(h-1)]}, which gives (R.1). QED.

**What this repairs.** D1 cut f_1 into pieces 1_Q f_1, whose datum norms the account does not bound. Here the field datum is never cut. Its weighted norm is computed from the cancellation (N4): the current J^c is cut only through its support, and a current's weighted norm is a sup norm (N2); the bracket beta is bounded by the walk-difference input (N3). The only comparison of distances used is d^ >= w d_sc, through the membership of p_T in M_delta. Proposition F's sums over cubes and its constant C_rho are not needed.

## 6. Proposition F': the collar layer bound (CL)

**Proposition F'.** Assume the inputs of CA in `ca-claude.md`, (N1)-(N9), (G-sep) and Lemma E. There is gamma_* > 0, fixed by the one ceiling (Gamma_F) below of supremum form, chosen last in the account's order, such that for gamma <= gamma_* the collar layer bound (CL) of `ca-claude.md` section 5 holds on the whole square of section 2, with Kcur = 3 + 18d + 2.2 K_J:

  N_y(t_s H_s) <= F_s,   eta^3 |s^#_{sigma_s}[t_s H_s](b)| <= Kcur F_s,   F_3 + F_4 <= eps* = min{1/85, (3/Kcur) alpha_{*,0}},

for every source, parameter and history, s in {3,4}, t_s in [0,1], y in Col(C) and stratum bond b at y. Here N_y is the local norm of `4.27:lem-left-factor-algebra` with the covariant derivative at the preceding partial product, and s^#_{sigma_s}[t_s H_s] is the segment current (S.1) at the kernel W_s.

**Proof.** *The sizes.* Put F_s := 2.03 sup E_{y'}(H_s), over y in Col(C) and blocks y' with d_sc(y, y') <= 2. At every point of the square the base of the left-factor step for s is U_2 (s = 3) or e^{i eta t_3 H_3} U_2 (s = 4). Its potential obeys eta|A'| <= 1.06 F_3 < 1/80 under the ceiling below, as in Proposition C of `ca-claude.md`. By the lattice fact (N9), N_y(t_s H_s) <= 2.03 t_s sup eta|H_s|, the sup over the region read at y. At a block of level m >= 0 the unit is L^m eta >= eta, so eta|H_s| <= N_{y'}(H_s) <= E_{y'}(H_s). Hence N_y(t_s H_s) <= t_s F_s <= F_s.

*The current.* By (N7), p(W_s) <= 1. Under the ceiling below, E_y(H_s) <= F_s <= 1/85 < 1/40. Lemma S at the kernel W_s gives eta^3 |s^#_{sigma_s}[t_s H_s](b)| <= t_s Kcur E_y(H_s) <= Kcur F_s. The current of each layer is taken at its own kernel, so it does not depend on the other parameter.

*The budget.* By (R.1), (N8) and (N9),

  F_3 + F_4 <= 2 (2.03) (C_D / K_u) K_Q alpha^+_k e^{4 delta_R} e^{-delta_R (L-2)(h-1)} e^{-delta_R Rc_k},
  alpha^+_k <= A^+ max_i alpha_{i,k} <= A^+ (1+beta_0)^2 k^{1/2} rho_C alpha_{*,0},
  k^{1/2} = (h + Rc_k)^{1/2} <= h^{1/2} + Rc_k^{1/2}.

Since e^{-delta_R (L-2)(h-1)} <= 1,

  F_3 + F_4 <= C_F (S_R + Rc_k^{1/2}) e^{-delta_R Rc_k} alpha_{*,0},
  C_F := 4.06 (C_D / K_u) K_Q A^+ (1+beta_0)^2 rho_C e^{4 delta_R},   S_R := sup_{h >= 1} h^{1/2} e^{-delta_R (L-2)(h-1)}.

S_R is finite because L >= 3, so (L-2) delta_R > 0.

*The ceiling.* (Gamma_F): sup_{R >= R_gamma} C_F (S_R + R^{1/2}) e^{-delta_R R} <= 3/Kcur. The function R -> (S_R + R^{1/2}) e^{-delta_R R} tends to 0 as R tends to infinity, and R_gamma tends to infinity as gamma tends to 0 (N9). Every constant in (Gamma_F) is fixed before gamma: delta_R, C_D, K_u, K_Q are fixed with the layer theory and the (d,L,M)-numbers, A^+ and rho_C with the radii, Kcur with K_J. So (Gamma_F) is a one-sided cap of degree minus infinity in the sense of `2.3:def-cap`, and it holds for gamma <= gamma_*. Under it, F_3 + F_4 <= (3/Kcur) alpha_{*,0}. Since Kcur >= 75 and alpha_{*,0} <= 1/170 by the ceilings (g) (as in `ca-claude.md` section 6.3), (3/Kcur) alpha_{*,0} < 1/85, so F_3 + F_4 <= eps*. If p_1 > q, A^+ carries the factor t_k^{p_1-q} <= (Rc_k^{1/r} + 1)^{p_1-q} (`ca-claude.md`, Remark on A^+), and the same ceiling with this factor included applies. QED.

**Remark.** Kcur is the same number as in `ca-claude.md` section 5, and (CL) is proved in the form Proposition C reads, on the whole square. So Proposition C applies unchanged.

## Result

**Proof, as an implication.** Step F of `library/ca-claude.md` holds. For every completing component C of every completion date, every source of the prescribed arrested source with its full global rider, every parameter (|sigma| <= e^{kappa_1}), and every (t_3, t_4) in [0,1]^2 of the chain e^{i eta t_4 H_4} e^{i eta t_3 H_3} U_2 (so at b2, b3, b4 and on the segments between them), the collar layer bound (CL) of `ca-claude.md` section 5 holds with Kcur = 3 + 18d + 2.2 K_J. It holds uniformly in the cutoff, the density k, the waiting depth h = k - Rc_k, the history and the arrest age, once gamma is at most gamma_*, fixed by the one ceiling (Gamma_F) of supremum form chosen last (section 6). Proof: Lemma S (section 4), Proposition R (section 5), Proposition F' (section 6). Proved by Claude, not yet checked by the other model.

With Lemmas A, B and Proposition C of `ca-claude.md` (ADVANCE at the gate, row 382), this gives CA as stated in the Result of `ca-claude.md`, with its named input 2 replaced by the inputs below. The repaired section is `library/ca-claude-r1.md`.

**Named inputs of step F** (section 3 gives the lines).

1. (N1) The layer theorem, clauses (a)-(b), in weighted norms, as the account states clause (b). The account cites it and prints no statement or proof of it. It is antecedent (L) of `stage-claude.md`, owner `stage-claude`. Not attacked here.
2. (N2) The field-datum lemma, clause (a), in weighted norms, as the account uses it twice.
3. (N3) Balaban CMP 99b Theorem 3.14 for the decoupling deformation, in the datum norm of (N2). The account cites the same theorem at the same place (hypothesis (e) of `4.22:lem-current-localisation`) and uses it only in kernel form. Registry row B99b-T314, no owner. This is the one input step F adds to those `ca-claude.md` already named.
4. (G-sep) The placement of the sources of the cancelled datum beyond S, as seen from Z_h, up to one unit. It is the account's placement in its proof of (c1); CMP 122b (1.50)-(1.55) is not available here to re-derive it.
5. (N4), (N5), (N6), (N7), (N8), (N9): the cancellation identity and its supports, the weight class and d^ >= w d_sc, the cut-layer partner current and the two estimates of `4.25:lem-current-partner`, the kernel irregularity, the budget (d'), and the geometry (Lemma E, N_k = Rc_k, the level-zero ratios), each as the account states or uses it.

**Where it can fail first.** For CA as a whole: (B-in), unchanged from `ca-claude.md`. For step F: the datum norm of a field datum in (N1)-(N3). G''_k is the propagator of CMP 99b Theorem 3.13, which excludes the covariant-Laplacian inequality of (3.42). If the datum norm contains that entry, (N2) and (N3) need the second representation and the Landau gauge, as in CMP 109 p. 272. This question belongs to the owner of (N1), and step F reads (N1)-(N3) only through the displays of section 3.

**Not used.** The cube-by-cube cut of f_1, the constant C_rho, the first route of Proposition F (Theta_0^loc and the reading (R)), the source identity at t < 1, and the commutator count (*) of `4.25:lem-cut-layer-partner`. No computer-assisted step.

**What it does not show.**
- The gate file `gates/ca-gate.md` is not in this checkout. This note answers the BLOCK as FINISH rows 382 and 386 state it. A defect the gate names beyond those rows is not treated.
- The account builds the completion layers in two ways: through the cancellation of `4.22:lem-current-localisation`, and through the data B_3, B_4, J_3 of the alternative derivation (I:142529-142546). This note uses the first, as `ca-claude.md` (P1) did. It does not prove that the two give the same layers.

**Kind (How we work, item 9).** Proof of a step the account assumes: the layer and current bounds on the collar at the completion site, which the account takes from its unprinted level-zero chain proposition (I:142269-142291, I:142571-142577). The account's own sentence "the parameters t_s enter through the definition of the layer currents" is made exact by its cut-layer partner current at cut parameter 0 (Lemma S).

**What changes for consumers.** None. (CL) is used as stated in `ca-claude.md` section 5, and Proposition C is unchanged.

**Suggested next steps, for the lead.** (a) One line-by-line check by Codex of Lemma S, Proposition R and Proposition F', with attention to the readings of (N1) (the form of the weighted norms), (N5)(ii) (membership in M_delta) and (G-sep). (b) Pass the caution on the field-datum norm (section 3, (N3)) to the owner of antecedent (L). (c) If (N3) is to be rebuilt, its input is CMP 99b section 3 (the walk expansions of Theorems 3.13-3.14), which is in `~/ym4d-papers`.
