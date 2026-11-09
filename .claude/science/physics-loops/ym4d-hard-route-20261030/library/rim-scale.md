lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T09:05Z

# rim-scale: the final-stage literal test on the lifted rim (FINISH row 609)

Status: being written section by section (started 2026-11-09T21:05Z). Pinned at 791f9e9bd.
Provenance: one session of Claude Fable 5.2 (medium), worker on the Mac mini. No other model checked this file. No numeric job was run; everything is by reading and by hand. Research-stage working state; it grants no status.

Credit. The object studied is the retained operation and its final-stage test in Ethan Sussman and Levent Alpoge's `YM4_1400.tex` (their text names Claude and Codex as authors), commit 2bc0658f91d2; "Y n" means line n of that file. The rim example, the inset split, the averaging-energy estimates and the regular-background proposition used below are theirs. The method (test on the localized background, contrapositive payment) is Tadeusz Bałaban's, CMP 119 (1988) 243-285 and CMP 122 (1989) 175-202; I read pp. 180-182, 193-195 of CMP 122 and p. 257 of CMP 119 on the page images in `~/ym4d-papers`.

## 0. Result

| Statement | Verdict |
|---|---|
| A1 (consumer audit, `P_rim`) | PASS within a keyword-bounded audit (section 4): 13 consumers found; none uses more than a level-unit bound `C eps_m` on `P_rim`; ten of them do not read the outer cell layer of `X` at all. Not a proof that no other consumer exists in the 136,637 lines. |
| A2 as written in the row (change the threshold on `P_rim` only) | **FALSE; stop condition (ii) holds in a wider form (section 5).** The mis-scaling is not confined to `P_rim`. In layer 1 of the tower at `dX` there are bare plaquettes with no lifted bond that fail the literal threshold whenever a rim plaquette of `V_m` exceeds `7 eps_m L^{-2(m-1)}`. Field: Y's own abelian example with `a` multiplied by `L^2`. |
| A2 restated (RIM-SCALE', section 6): on the outer cell layer of `X` test at `c_0 eps_m L^{-2 lambda(p)}`, `lambda(p)` = joined level | **The failure branch is empty on the support of the carried density tests** (Theorem 6.2), so no payment is needed there. Off that support the contrapositive gives a level-m plaquette with `norm(V_m(dp') - 1) >= c_1 eps_m` and the Wilson witness `>= (c_1^2/4) theta_m eps_m^2` on its four blocks (Corollary 6.3). Both are implications from four inputs of Y that I read but did not rebuild; the hypothesis I could not check is named in 6.4. Ownership across ages (W-d) is not addressed. |
| A3 nesting | Holds for RIM-SCALE' exactly as far as it holds for Y's inset rule: every earlier guard and every implication of Y 64221-64362 reads only the inset (section 7.1). |
| A3 admission (G0-COV-ADMIT, final-stage operation, real point) | Index 0: follows from the plaquette clause by Lemma A of `g0-cover.md`. Index n >= 1: the difference clause does NOT follow from a plaquette test; it follows from the curvature and current bound of the critical background by Y's `prop:bg-local-gauge` (Y 25030-25066). So the lead's risk is real and is settled in class M, with one geometric fit unchecked (section 7.2). |
| Stop (i) | Not met: no consumer found that needs the bare threshold on `P_rim`. |
| Stop (iii) | Not met: no circle (section 6.4). |

In one sentence: the right restatement is not "level-m threshold on `P_rim`" but "layer units on the whole outer collar", and with that scaling the rim clause is a consequence of the carried tests, so the rim branch of H-C-MARK disappears instead of being paid.

## 1. Repo search and scope

- `grep -n "RIM-SCALE\|rim-scale\|G0-COV-ADMIT\|G0-COV-PAY\|RIM-LB\|RIM-C" library/open-core.md`: no hit. FINISH rows 488, 502, 522, 552 (hc-mark, hcm-false, hcm-r2, leaf-rguard) keep the literal test; rows 524, 547, 551, 568 change the background. None changes the threshold. Row 609 is the only row on this statement. No other row covers it.
- Read from our library: `g0-cover.md` (whole), `t0-approach.md` Part 2 R2, R5 and Part 4.2 Item A, `hcm-false.md` section 2. Their results are inputs: every renewed operation that reaches its final stage runs the literal rim test, and no earlier passed test implies it (`hcm-false.md` section 2).
- NOT READ: Y outside the line ranges cited below. The audit in section 4 is bounded by the search terms listed there.

## 2. What the sources say (read firsthand)

**B1. Bałaban's lift is the face lift.** CMP 119 (1.3): `(Q^{s*} V)(b) = V(c)` for `b in B(c)`, the bonds from block `B(c_-)` to block `B(c_+)`. CMP 122 (1.20), p. 180: the localized background `U^{(n)}_{k,Z}` uses the fields `V` on `Z cap Omega_k^c` and `M(Q^{s*}_k V_k)` on `Z cap Omega_k`, on the determining set (1.19) built with `B_k(Z)`. CMP 119 (2.13)-(2.14), pp. 256-257: `B_j(Omega)` is the tower `Omega = Omega_0 > Omega_1 > ... > Omega_j` with `dist(Omega_n, Omega_{n-1}^c) >= L^n xi M_1`, used on `Omega \ Omega^{~-2}`. So Bałaban's localized background has the same tower at the boundary of `Z` and the same lifted datum as Y's.

**B2. Bałaban's main-step test does not read the tower.** CMP 122 (1.75), p. 193, on the page image: `chi_{k,Lambda} = chi({ inf_{V_k|Lambda} sup_{p in Omega_k^c} |U_{k,Z}(dp) - 1| < 2 eps_k eta^2 })`. The supremum is over `p in Omega_k^c`, the old large-field part of `Z`. The tower lies in `Z cap Omega_k`.

**B3. The stage test (1.24), p. 182.** Its last line is `|U^{(n)}_{k,Z}(dp) - 1| < c (1 - beta/2) eps_j (L^{k-j} eta)^2 for p in Omega_{j-1} \ Omega_{j+1}`, with `c = 3` for `j = k`. For `j = k` the set `Omega_{k+1}` is not defined in the pages I read; Y reads the region as all of `X cap Omega_m` (Y 72324-72326). Under that reading Bałaban's test has the same rim. (1.80), p. 195, states `|U_0(dp) - 1| < 2 eps_k eta^2 + ...` "for p in Omega_k"; on a tower plaquette this contradicts identity (R1) below unless the plaquettes of `V_k` there are below `C eps_k eta^2`. I did not resolve which convention Bałaban intends; nothing below depends on it.

**B4. The payment on p. 193** is a contrapositive on the box `Lambda`: small plaquettes of `V_k` on `Z cap Lambda^c` give, by an axial gauge on `d^+ Lambda`, an extension with `|dV_k - 1| < O(1) M^2 eps`, hence "`|V_k(dp') - 1| > (O(1) B_3 M^2)^{-1} eps_k` for some `p' in Z cap Lambda^c`", and "This condition is enough to get the exponential small factor". It is a statement about the extension into `Lambda` tested on `Omega_k^c`, not about the tower at the boundary of `Z`.

**Y1. Y states the defect of the literal test itself.** Y 63876: "adjacent to `X^c`, the background localised in `X` is constrained bond by bond on the bare lattice. There the test therefore demands `|dV_k - 1| < C eps_k eta_k^2` of the block field itself, while the carried tests provide only `2 eps_k`." Y 72318-72322: "In the outer joining collar the tower can descend to the bare scale. There a bound in its local units gives the top-scale threshold only with an additional bound on the lifted top datum. When the stage tests that collar, we must estimate its failure separately." Y 72424-72427: "the pointwise certificate must use the joined layer of the rim plaquette, which is zero here".

**Y2. Y already has an inset form of the test.** Y 64306-64308: `chi_in` is "the literal final clauses restricted to plaquettes whose corners are all in `X` with one full level-m cell layer removed". Y 64482-64504: "The inset test can also define the split of a separate operation from its first formation", with `G = chi_in kappa_x`. Y 64084-64086: one comparison "does not require the discarded sharp bound at the artificial bare rim of `X`".

