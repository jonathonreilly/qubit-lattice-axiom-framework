lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T00:31Z

# ca-claude r1: repaired step F of `library/ca-claude.md` (FINISH row 386)

Provenance: Claude Opus 5.5, max effort, Mac mini worker; checkout pinned at `9c36ea22b`; 2026-11-06. Research text, not an audit, no status. Proved by Claude, not yet checked by the other model. No computer-assisted step.

Status: this file replaces section 6.3 (Proposition F) and item 2 of the named inputs in the Result of `library/ca-claude.md`. Every other part of that note stands as written. The full report, the defects of the old Proposition F and all line references are in `library/ca-f.md`; the input labels (N1)-(N9) and (G-sep) below are those of its section 3.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (account at `31a47c543775`), for the partner current of a cut layer, the current-partner estimates, the cancellation identity of `4.22:lem-current-localisation` and the weighted layer theorem as they state it; Tadeusz Balaban for CMP 109 (3.11)-(3.13) and CMP 99b Theorem 3.14.

## 6.3 (r1) The collar layer bound from the cancelled datum

**Inputs** (`ca-f.md` section 3). (N1) the layer theorem, clauses (a)-(b), in weighted norms (antecedent (L) of `stage-claude.md`); (N2) the field-datum lemma, clause (a), in weighted norms; (N3) CMP 99b Theorem 3.14 for the decoupling deformation, in the datum norm; (N4) the cancellation f_1 = G''(sigma) J^c + beta of (4.22:eq-current-localisation-a); (G-sep) the sources of the cancelled datum lie, as seen from Z_h, beyond S less one unit; (N5) d^ >= w d_sc and the Lipschitz description of M_delta; (N6) the partner current of a cut layer and the two estimates of `4.25:lem-current-partner`; (N7) kernel irregularity at most 1; (N8) the budget (d') as the account's proof of (c1) uses it; (N9) Lemma E, k = h + Rc_k, the level-zero ratios, and the lattice fact of section 6.

**Notation.** (A'_s, X_s, H_s) is the layer datum of H_s at its kernel (W_s, sigma_s). At a block y,

  E_y(H_s) := max{ N^Delta_y(A'_s), N_y(H_s), l_y^3 |P_1(sigma_s) A'_s|, l_y^3 |m_H(sigma_s) X_s| }.

**Lemma S (the current of the actual segment).** Let y be a level-zero block, p(W) <= 1 and E_y(H) <= 1/40. For t in [0,1] the segment current is the account's partner current of the cut layer at cut parameter 0,

  s^#_sigma[t H] := (Delta_W - P_1(sigma) + K)(t A') - t m_H(sigma) X + F(W, t H),

and for every bond b at y, eta^3 |s^#_sigma[t H](b)| <= t Kcur E_y(H), with Kcur = 3 + 18d + 2.2 K_J.

*Proof.* With chi the constant t, all lattice differences of chi vanish, so the commutator [D_W^* D_W, chi] is zero (the account's product rule; "the constant t being annihilated", I:111631-111632), and the account's J^#[chi] (I:111538-111545) is the display. The linear members are t times those of the full layer: eta^3 |Delta_W A'| <= N^Delta_y(A'); the P_1 and m_H members are entries; eta^3 |K A'| <= 18d p(W) eta |A'| <= 18d N^Delta_y(A'). The remainder: N_y(tH) = t N_y(H) <= 1/40, so eta^3 |F(W, tH)| <= K_J (1 + 1/20) 2 N_y(tH) <= 2.2 K_J t E_y(H) (I:111580-111586). QED.

**Proposition R (the response tuple at the collar).** Put delta_R := min{delta_br, w delta} and C_D := K_#(1 + C_Q) + K_br C_lambda + 1. For s in {3,4}, y in Col(C) and every block y' with d_sc(y, y') <= 2,

  E_{y'}(H_s) <= (C_D / K_u) eps_Q(k) e^{3 delta_R} e^{-delta_R [ (Rc_k - 1) + (L-2)(h-1) ]}.

*Proof.* Let T := S united with supp J^c and Lambda^c, and p_T := e^{-delta_R d_sc(., T)}. By the triangle inequality and d^ >= w d_sc, p_T(y)/p_T(y') <= e^{delta d^(y,y')}, so p_T is in M_delta. The field datum is not cut. By (N2), ||G''(sigma) J^c||_{dat,p_T} <= K_# sup|J^c| <= K_# (1 + C_Q) J_*, since p_T = 1 on supp J^c. Since p_T >= p_br, (N3) gives ||beta||_{dat,p_T} <= K_br sup|lambda_2| <= K_br C_lambda J_*. The block data lie in S, where p_T = 1. With (N8), ||d_s||_{dat,p_T} <= C_D eps_Q(k)/(K_u B_H). Clause (b) of (N1), between d_s and the zero datum, gives E_{y'}(H_s) <= (C_D/K_u) eps_Q(k) p_T(y'). Finally d_sc(y', T) >= d_sc(y, S) - 3 by (G-sep) at y in Z_h, and Lemma E bounds d_sc(y, S) below. QED.

**Proposition F' (replaces Proposition F).** There is gamma_* > 0, fixed by one ceiling of supremum form chosen last, such that for gamma <= gamma_* (CL) holds for every source, parameter, history, s in {3,4}, (t_3, t_4) in [0,1]^2, y in Col(C) and stratum bond b at y, with F_s := 2.03 sup{E_{y'}(H_s) : y in Col(C), d_sc(y,y') <= 2}.

*Proof.* Size: the base of the left-factor step is e^{i eta A'} U_2 with eta|A'| <= 1.06 F_3 < 1/80, so the lattice fact gives N_y(t_s H_s) <= 2.03 t_s sup eta|H_s| <= F_s. Current: Lemma S at the kernel W_s gives eta^3 |s^#_{sigma_s}[t_s H_s](b)| <= t_s Kcur E_y(H_s) <= Kcur F_s. Budget: by Proposition R, eps_Q(k) <= K_Q alpha^+_k, alpha^+_k <= A^+ (1+beta_0)^2 k^{1/2} rho_C alpha_{*,0} and k^{1/2} <= h^{1/2} + Rc_k^{1/2},

  F_3 + F_4 <= C_F (S_R + Rc_k^{1/2}) e^{-delta_R Rc_k} alpha_{*,0},   C_F := 4.06 (C_D/K_u) K_Q A^+ (1+beta_0)^2 rho_C e^{4 delta_R},

with S_R := sup_{h >= 1} h^{1/2} e^{-delta_R (L-2)(h-1)} finite. The ceiling (Gamma_F): sup_{R >= R_gamma} C_F (S_R + R^{1/2}) e^{-delta_R R} <= 3/Kcur is a one-sided cap of degree minus infinity, all its constants being fixed before gamma, and R_gamma = inf_k Rc_k tends to infinity as gamma tends to 0. Under it F_3 + F_4 <= (3/Kcur) alpha_{*,0} < 1/85, so F_3 + F_4 <= eps*. If p_1 > q, include the factor t_k^{p_1-q} as in the Remark on A^+. QED.

## 6.4 (r1) addition: why the old Proposition F is replaced

The old second route cut the field datum f_1 into cube pieces whose datum norms the account does not bound (defect D1 of `ca-f.md`), and it read the source identity at t_s < 1, where no associated fields are defined (defect D2). Proposition R avoids D1 by bounding the uncut datum in one weighted norm through the cancellation. Lemma S avoids D2 by the account's own definition of the partner current of a cut layer at cut parameter 0. The first route (Theta_0^loc and the reading (R)) is no longer needed.

## Result (r1): replacement for named input 2 of `ca-claude.md`

2. Step F reads the layer theorem (N1) (cited by the account, printed nowhere; antecedent (L), owner `stage-claude`), the field-datum lemma (N2), CMP 99b Theorem 3.14 in the datum norm (N3) (registry B99b-T314, no owner), and the account's placement of the sources of the cancelled datum (G-sep). **This is the second place the proof can fail**, and within it the first point is the datum norm of a field datum: G''_k is the propagator of CMP 99b Theorem 3.13, which excludes the covariant-Laplacian inequality of (3.42) (see the caution under (N3) in `ca-f.md`). The source identity at partial t and the reading of Theta_0^loc are no longer used.
