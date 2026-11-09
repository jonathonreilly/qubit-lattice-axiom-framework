lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T09:05Z

# rim-scale: the final-stage literal test on the lifted rim (FINISH row 609)

Status: finished 2026-11-09 (one session, started 21:05Z). Pinned at 791f9e9bd. Not checked by another model.
Provenance: one session of Claude Fable 5.2 (medium), worker on the Mac mini. No other model checked this file. No numeric job was run; everything is by reading and by hand. Research-stage working state; it grants no status.

Credit. The object studied is the retained operation and its final-stage test in Ethan Sussman and Levent Alpoge's `YM4_1400.tex` (their text names Claude and Codex as authors), commit 2bc0658f91d2; "Y n" means line n of that file. The rim example, the inset split, the averaging-energy estimates and the regular-background proposition used below are theirs. The method (test on the localized background, contrapositive payment) is Tadeusz Bałaban's, CMP 119 (1988) 243-285 and CMP 122 (1989) 175-202; I read pp. 180-182, 193-195 of CMP 122 and p. 257 of CMP 119 on the page images in `~/ym4d-papers`.

## 0. Result

| Statement | Verdict |
|---|---|
| A1 (consumer audit, `P_rim`) | PASS within a keyword-bounded audit (section 4): 13 consumers found; none uses more than a level-unit bound `C eps_m` on `P_rim`; nine of them use no bound in the outer cell layer of `X` at all. Not a proof that no other consumer exists in the 136,637 lines. |
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

## 3. Setting, notation, two exact facts

Level `m`, class component `X`, final stage (`n = N_m`, `j = m`) of the retained operation; `U_X := U^{(N_m)}_{m,X}` is the background localized in `X`. `a_m = M R_m L^m` is the side of a level-m cell in bare units (`R_m` is Y's `\check R_m`). `tau_m := 3 (1 - beta_s/2) eps_m L^{-2m}` is the literal threshold on bare plaquettes of `X cap Omega_m` (Y 63876, Y 72324-72326). Norms are operator norms; for SU(2), `norm(1 - e^{iF}) = 2 sin(|F|/2)` with Y's Lie-algebra norm (Y 4703-4705).

Geometry used (each with its line):

- (G1) `X cap Omega_m^c` lies two level-m cells inside `X` (Y 64229-64231). So the outer two cell layers of `X` are in `Omega_m`.
- (G2) The carried density test `chi_m(Omega_m^{~4})` covers the outer six cells of `X`, with halos that may read outside `X` (Y 76692-76695, Y 78313-78315).
- (G3) At `dX` the localized determining set is a tower ("the minimal recursive tower of the component", Y 135196-135197) whose layers descend to the bare lattice (Y 72318-72319). Its datum is the block lift of `V_m`: "the identity on internal bonds and copies a top link on each bond crossing its corresponding block face"; "the one-step average of the finer lift is exactly the coarser lift" (Y 135200-135209; also Y 35166-35183). The tower is within the outer level-m cell layer: it has the scale of `M_1`-cubes (CMP 119 p. 256: `Omega^{~-2} subset Omega_j`), and Y places every interior read at weighted distance at least `c M R_m` from it (Y 77947-77949, Y 65054-65056).
- (G4) Layer zero of a tower is wider than `L^2` bare spacings and the gap between consecutive members is greater than `R_1 frakM xi_j`, with `R_1 >= L >= 13` (Y 14942-14950, Y 35693-35696).

Write `lambda(p)` for the joined level of a bare plaquette `p` (Y's "local level of the joined stage sequence", Y 72304-72305): `lambda = 0` in layer zero of the tower, `lambda = m` in the top layer.

**(R1) Rim identity (Y 72327-72338, Y 35185-35188; `hcm-false.md` (1)).** In layer zero of the tower every bare bond is a determining bond with the lifted value. A bare plaquette there is `1` unless both its directions cross faces of level-m blocks; then it is the level-m plaquette of `V_m` at the four block centres, up to conjugation and orientation. The same holds for the datum plaquettes of every layer `j < m` of the tower: each is `1` or a top plaquette of `V_m` (Y 72277-72280, Y 64102-64105, Y 71379-71381, Y 134211-134214). No minimization enters.

**(R2) One-step averaging, local form (Y `lem:small-energy-local-flux`, Y 71619-71634; I read its proof, Y 71641-71690).** Let `C` be a plaquette of the level-1 lattice and `D(C)` the union of the four centred `L`-blocks at its corners. There are `d_L > 0` and `C_L` depending only on `L` such that, if the bare plaquette logarithms satisfy `kappa := max_{p in D(C)} |F_p| <= d_L`, then all means used by `C` are on their regular branches and

`|F_C(MU)| <= sum_p T_{C,p} |F_p| + C_L sum_{p in D(C)} |F_p|^2 <= L^2 kappa + 24 L^4 C_L kappa^2 .`

The count: the row sum of `T` is `L^2` (Y 4756-4759), and `D(C)` has `(2L)^2 L^2` sites, hence at most `6 * 4 L^4` plaquettes. So

`kappa <= kappa_L := min(d_L, 1/(24 L^2 C_L))  implies  |F_C(MU)| <= 2 L^2 kappa .   (R2)`

## 4. A1: consumer audit

Method. I searched Y for: `rim`, `artificial`, `tower collar`, `joining collar`, `face lift`, `lifted top`, `partial X`, `inset`, `literal`, `chi_{\rm in}`, `final stage`, `final guard`, `final test`, `final regularity`, `six-cell`, `tested inset`, `top density test`, and read each hit between lines 62000 and 79000 and at 134200-135300 with its paragraph. A consumer is a place where the passing final-stage guard is used as a hypothesis. For each: what it reads in the outer cell layer `E` of `X`, and the bound it uses on `P_rim`.

| # | Consumer | Lines | Reads in the outer cell layer | Bound used on `P_rim` |
|---|---|---|---|---|
| 1 | Removal of the earlier guards (nesting ladder) | Y 64221-64232, 64233-64268 | none: "every earlier guard reads only `X cap Omega_m^c`"; "All these reads remain in the inset"; "The artificial bare rim occurs only in the final guard" | none |
| 2 | Crossing plaquettes of `dZ''_m`, test `kappa_x` and its reserve | Y 64270-64362 | none: the translated plaquette "lies in the deep exterior and in the inset" | none |
| 3 | Last-stage approximate collar and fluctuation tests (groups five, six) | Y 64032-64110 | none for the reads ("distance at least `c M R_m` from `dX`"); the tower rows enter as common rows whose "tested holonomy is either the identity or the lifted top holonomy. These are bounds at the respective levels of the datum" | level unit: the top-datum bound; "does not require the discarded sharp bound at the artificial bare rim" |
| 4 | Change from `S^-` to `S` | Y 64137-64160 | "The common rows, including the exterior tower rows, do not change" | none |
| 5 | Inherited strip at the final stage | Y 65378-65400 | rows close to `dX` are compared through the ordinary and preceding global backgrounds on an annulus, because near `dX` "the estimate comparing `S_g` with `S_X` need not hold" | none (the localized rim is avoided) |
| 6 | Crossing bound on the prepared member (main integration) | Y 71340-71405 | "The remaining tests at the artificial join are the identity or lifted top plaquette holonomies. Their defects obey the top datum bound" | level unit `C(M) eps_m` |
| 7 | Witness calculation for a final regularity stop | Y 72146; Y 72297-72322 | "At a final regularity stop this calculation applies to the inset and its prepared-seam test" | none |
| 8 | Certificates for the carrying datum | Y 76655-76668 | "When this union lies in the tested inset, use the last applicable stage guard... A footprint extending outside that inset uses the original density cube" | none; outside the inset the carried density test, level unit |
| 9 | Healing: top test of the new domain | Y 76690-76697 | "the old top test enlarged by four cells covers the outer six cells... The final positive test on the six-cell inset supplies the interior" | none |
| 10 | Read coverage at a compressed seam and for collar bonds | Y 77606-77616, 77925-77950 | none: carriers "in the unchanged interior of the join"; "separated from the outer tower collar" | none |
| 11 | Late stops; inset operation footprints | Y 78286-78315 | none: "the full footprint inside the spatial inset"; the final stage test "is used with the original top density tests and the old core tests" | none |
| 12 | Existence of the localized orbit before the guard | Y 134205-134222 | whole joined set: a tested holonomy "is one in the lifted collar, or equals a tested top holonomy of the datum being lifted. Hence the joined datum is `bar eps`-regular" | level unit `bar eps > C max_q e_q`; and this is before, not after, the guard |
| 13 | Extendibility trial comparison | Y 135155-135190, 135255-135262 | top plaquettes near the outside of the tested inset use a carried density cube: "defect at most `2 eps_i`"; partners are "on complete top stencils" by "clearance to the tower boundary" | level unit `2 eps_i` |

Findings.

1. No consumer in the table uses `norm(U_X(dp) - 1) <= tau_m` at a plaquette of `P_rim`, nor at any bare plaquette of the tower. Nine use no bound in the outer cell layer. Four (3, 6, 12, and 13 for the density cube) use the datum of the collar in level units, which is the bound `C eps_m` asked for in A1.
2. The analytic domain is stated in layer units too. `rg:structured-local-gauge` (Y 1251-1258): the pointwise clauses hold on every plaquette of the bare bonds of `Y cap Omega_0` and "extend through `Omega_0 \ Omega_1`, with the layer-zero radii". For the address localized to the class component the first members are those of "the joined determining set with its prescribed collar" (Y 134208-134210). So a rim plaquette is admitted at the layer-zero radius, a fixed constant, not at `tau_m`.
3. Not covered by this audit, and named as the residual risk: a term formed with the unlocalized structure whose domain lies in the outer cell layer and which some step evaluates at `U_X`. Y calls every such restriction or substitution an "analytic inclusion hypothesis" (Y 1245-1248) and requires the clauses to be verified for the resulting triple (Y 1276-1279). That is root R2 (ADMISSION), not this row. I found no place where Y does this with `tau_m` on the rim.

Verdict A1: no stop (i). The literal threshold on the collar has no consumer in the passages read; Y's own word for it is "discarded" (Y 64085).

## 5. Stop condition (ii), wider form: changing the threshold on `P_rim` alone fails

**Claim 5.1.** Keep every clause of the literal final-stage test and replace only the threshold on `P_rim` by `c_0 eps_m`. Let `P` be a level-m plaquette of `V_m` at the rim as in Y 72327-72334 (tangent to a flat outer face, crossing two faces of level-m blocks). If the localized background `U_X` exists and

`norm(V_m(dP) - 1) >= 7 eps_m L^{-2(m-1)}`  and  `1.05 tau_m <= kappa_L`,

then the modified test fails at a bare plaquette that is not in `P_rim` and has no lifted bond.

*Proof.* The two faces of level-m blocks crossed by `P` meet in a 2-plane that runs along the inward normal of the outer face through every layer of the tower. By (G4) layer 1 contains a slab of at least `L` level-1 spacings (`R_1 frakM >= L^2 > L`). Choose in it the level-1 plaquette `C` with the tangential position of `P`, with its four corners level-1 sites of layer 1. Its four bonds are determining rows of level 1, and by (R1) and (G3) the datum on `C` is `V_m(dP)` up to conjugation. The four corner blocks of `C` are `L`-blocks of the level-1 member, so `D(C)` lies in that member; no bare bond of `D(C)` is a determining bond, hence no plaquette of `D(C)` is in `P_rim`, and `D(C)` is inside `X cap Omega_m` by (G1), (G3). The background satisfies `M U_X = V` on the four rows of `C` (Y 35641-35643).

Suppose every bare plaquette `p` in `D(C)` passed the kept clause `norm(U_X(dp) - 1) < tau_m`. Then `|F_p| = 2 arcsin(norm/2) <= 1.05 tau_m =: kappa` (since `arcsin x <= (pi/3) x` on `[0, 1/2]`), and by (R2)

`norm(V_m(dP) - 1) <= |F_C| <= 2 L^2 kappa <= 2.1 L^2 tau_m < 6.3 eps_m L^{-2(m-1)}`,

a contradiction. If `U_X` does not exist the test fails by Y's convention (Y 64485-64486). `square`

**Field 5.2 (the field asked for by stop (ii)).** Take Y's example, Y 72340-72428, unchanged except for the amplitude: `A_1(x) = a x_2 T`, `A_nu = 0` otherwise, in level-m units in a fixed box containing the four order-m blocks of `P`, continued to zero outside a slightly larger box, sampled by `U(b) = exp(i eta_m A_nu(x_b))`, multiplied by Y's pure-gauge creation at level `h = m - N_m`; with

`a = a_m := 8 eps_m L^{-2(m-1)}`   in place of Y's `8 eps_m L^{-2m}`.

By Y 72353-72366 its top plaquette `P` has defect `2 |sin(a/2)| >= a (1 - a^2/24) >= 7 eps_m L^{-2(m-1)}`. So by Claim 5.1 the modified test fails. On the other side:

- every level-m plaquette of `V_m` has defect at most `C a_m`, which is below `c_0 eps_m` (so the new `P_rim` clause passes) and below `eps_m/(C M^2)` for `m >= m_0(L, M, C, c_0)`;
- the Wilson exponent of the perturbation is at most `C theta_m a_m^2 = C theta_m eps_m^2 L^{-4(m-1)}`, and by Y 72420-72424 the fresh gauge and Gaussian payments are `O(a^2)` as well;
- Y's verification that the earlier stages pass uses only `|a| -> 0` at fixed `m - h` (Y 72406-72419): the earlier reads see bare curvature at most `C |a| L^{-2h}`.

So A2 as written in the row is false: the modified test fails, no level-m plaquette near the rim reaches `eps_m/(C M^2)`, and no witness of size `c theta_m eps_m^2` exists. Status: Claim 5.1 is proved here from (R1), (R2), (G1), (G3), (G4). Field 5.2 is Y's example with one constant changed; its admissibility (the creation at level `h`, the class-size bound, the passing of the earlier stages) is Y's analysis, which I read and did not rebuild.

The same argument with Y's `cor:iterated-average-energy` (Y 4905-4920) in place of (R2) gives a failing bare plaquette in layer `j` of the tower as soon as the rim defect exceeds `C eps_m L^{-2(m-j)}`. The literal threshold is wrong by `L^{2(m - lambda(p))}` on the whole tower, not only on `P_rim`.

I stop the row's A2 here, as the row orders. Sections 6 and 7 give the repair that sections 2 to 5 force, with its proof status; they are one step, not a new lane.

## 6. The restatement RIM-SCALE' and what it gives

### 6.1 Statement

Let `X_in` be `X` with one full level-m cell layer removed, and `chi_in` the literal final clauses on the bare plaquettes with all corners in `X_in` (Y 64306-64308). Let `E` be the set of bare plaquettes of `X` with a corner outside `X_in`; by (G1) they lie in `X cap Omega_m`, and by (G3) `E` contains the tower. Define

`chi_E := 1{ U_X exists and norm(U_X(dp) - 1) < c_0 eps_m L^{-2 lambda(p)} for every p in E }`,

and the restated final guard `G' := chi_in * chi_E` (times `kappa_x` if the crossing test of Y 64309-64313 is kept). On `P_rim`, `lambda = 0`, so this is the threshold `c_0 eps_m` of the row; on layer `j` of the tower it is `c_0 eps_m L^{-2j}`; on the top-layer part of `E` it is `c_0 eps_m L^{-2m}`, the literal form with `c_0` in place of `3(1 - beta_s/2)`. This is the scaling of Bałaban's (1.24), each layer at its own spacing, applied to the layers of the localization tower as well.

### 6.2 Inputs (all Y's; read, not rebuilt)

- (I1) `bgc:proper-background` (Y 35632-35646): on the geometry of Y 35268-35275 there are `a_0, a_1, C_B`, independent of depth and volume, such that every real mixed datum whose ordinary and mixed test holonomies are within `eps <= a_1` of one has a constrained-critical `U(V)` with `M_B U(V) = V` and `R_mat(U(V)) <= C_B eps`; two critical configurations with `R <= a_0` are in one residual gauge orbit. Here `R(U) = max{ sup_p eta^{-2} L(p)^2 |dU(p) - 1|, sup_b L(b)^3 |J(U)(b)| }` with `L(.)` the assigned local scale (Y 35277-35283).
- (I2) the weighted profile, from the proof of `bgc:reset` (Y 35617-35626) and `mb:weighted-maximum` (Y 12470-12491): for a real constrained-critical `U` with `R(U) <= a_c`, the local radius obeys `r_U(x) <= K_w P(x)`, `P(x) = sup_tau e^{-delta d_B(x,tau)} |dV(tau) - 1|`, the supremum over the tested datum plaquettes `tau`, `d_B` the weighted distance; `K_w = 5K` and `delta > 0` are fixed with the geometry.
- (I3) interior datum: on the admitted incoming fibre the tested holonomies of the joined datum in `X cap Omega_m^c` are within `eps_int := C max_q e_q` of one, `e_q = R_q^2 eps_q` (Y 65412-65414, Y 78326-78336, Y 134205-134216), and their weight at the outer collar is negligible: "`eps_* e^{-c delta_c M R_m} = o(eps_m)`" (Y 71386-71391; the collar is at weighted distance at least `c M R_m`, Y 77947-77949).
- (I4) density test to top plaquette: a top plaquette with a corner in a carried density cube has defect at most `2 eps_m` (Y 135180-135190; it is `cor:iterated-average-energy`, Y 4905-4920, with `alpha = eps_m`, whose proof I read).
- (I5) `prop:small-energy-all-depth` (Y 71744-71760): there is `e_*(L) > 0` such that every real `U` and every finite set `S` of level-t plaquettes satisfy `sum_{p in N_0(S)} a_p(U) >= min{ (1/4) sum_{C in S} norm(1 - d M^t U(C))^2, e_*/2 }`, where `N_0(S)` is the set of bare plaquettes with all corners in the four order-t blocks of one `C in S`, and `a_p(U) = 1 - (1/2) Tr U_p`.

Constants: `c_0 := 5 K_w`, `c_1 := 4`.

### 6.3 Theorem and corollary

**Theorem 6.2 (RIM-REG; the rim branch is empty on the carried support).** Assume H-GEO (6.4). Let the coupling be so small that `C_B eps_int <= min(a_0, a_c)`, `eps_int <= a_1`, `2 eps_m <= a_1`, and `eps_int e^{-delta d} <= eps_m / 2` for `d` the weighted distance from `E` to `X cap Omega_m^c`. Take a real evaluation at which (a) the carried density tests of level `m` hold on the cubes that cover the outer two cell layers of `X` (G2), and (b) the interior bound (I3) holds. Then `U_X` exists, is the unique critical orbit with `R <= a_0`, and

`norm(U_X(dp) - 1) <= 2 K_w eps_m L^{-2 lambda(p)}`  for every `p in E`.

In particular `chi_E = 1`: on the support of the carried tests the restated guard `G'` equals `chi_in`, and the clause on `E` has no failure branch.

*Proof.* Tested datum plaquettes of the joined set are of three kinds (Y 134210-134214). Those of the tower are `1` or top plaquettes of `V_m` by (R1). The top plaquettes of `V_m` with bonds in `X cap Omega_m` lie in the outer two cell layers (G1), each has a corner in a carried density cube (G2), so by (a) and (I4) its defect is at most `2 eps_m`. The remaining ones are in `X cap Omega_m^c` and are within `eps_int` of one by (b). So the datum is `eps_int`-regular with `eps_int <= a_1` (enlarge `C` in (I3) so that `eps_int >= 2 eps_m`), and (I1) gives `U_X` with `R_mat(U_X) <= C_B eps_int <= min(a_0, a_c)`, unique among critical configurations of radius `a_0`. Now (I2) applies. For `x` a corner of `p in E`: the tower and top datum plaquettes contribute at most `2 eps_m` to `P(x)`; the interior ones contribute at most `eps_int e^{-delta d} <= eps_m/2`. Hence `r_U(x) <= 2 K_w eps_m`, and by the definition of `R` with `L(p) = eta L^{lambda(p)}` the bound follows. `square`

**Corollary 6.3 (contrapositive, the form of A2).** Assume H-GEO, the smallness conditions with `4 eps_m` in place of `2 eps_m`, and (b). If `chi_E` fails at a real evaluation (including `U_X` undefined), then some level-m plaquette `P` of `V_m` with all four bonds in the outer two cell layers of `X` has

`norm(V_m(dP) - 1) > c_1 eps_m = 4 eps_m`,

and every real `U` whose level-m averages on the four bonds of `P` are those of `V_m` (read on their full blocks) satisfies, for `eps_m^2 <= e_*/8`,

`sum_{p in N_0({P})} a_p(U) >= 4 eps_m^2`.

With the Wilson weight `theta_m` on these plaquettes (Y 71408-71417: the profile equals `x_m` on `X` outside the box) the event has the witness `Gamma >= 4 theta_m eps_m^2`. The four blocks of `P` lie in `X` (alignment, Y 72580-72581) and in `Omega_m`, at least one cell from `X cap Omega_m^c`, so no plaquette of the witness has a corner in the floor.

*Proof.* If every such `P` had defect at most `4 eps_m`, the proof of Theorem 6.2 with `4 eps_m` in place of `2 eps_m` would give `r_U <= 4 K_w eps_m < c_0 eps_m` on `E`, so `chi_E = 1`. The energy bound is (I5) with `S = {P}`, `t = m`: `min{(1/4)(4 eps_m)^2, e_*/2} = 4 eps_m^2`. `square`

Remarks.

1. Compared with the row's A2: the plaquette found is within two cells of the rim and its size is `4 eps_m`, with no factor `M^{-2}`. The factor `M^2` in CMP 122 p. 193 comes from the axial extension into the box `Lambda`; no extension is made here, since the collar datum is the given exterior field.
2. On a fibre where the carried tests keep their recorded values (Y 72146: "each test carried by `X` takes its recorded value"), (I4) gives defect at most `2 eps_m < 4 eps_m`, so the event of Corollary 6.3 is empty there. The witness is needed only at evaluations where the carried level-m density test is not available; I found no such evaluation in Y, but I did not search for one beyond the lines cited.
3. Disjoint ownership over ages (W-d of `t0-approach.md`, G0-COV-PAY of `g0-cover.md`) is not addressed. By remark 2 it is not needed for this branch.

### 6.4 Hypotheses of `bgc:proper-background` on this geometry; no circle

| Hypothesis | Where | Status here |
|---|---|---|
| `L >= 13`, fixed `alpha`, floors of the strong inverse | Y 35268-35275 | global choices of Y; not checked against our parts' choice of `L` |
| real datum | Y 35637 | holds: A2 is on real evaluations |
| no-inward determining set, aligned, separation greater than `R_1 frakM xi_j` between consecutive members, `R_1 >= L`, `R_1 frakM >= L^2 rho` | Y 14938-14950, Y 35262-35266 | **H-GEO, not checked.** For the tower at `dX` it holds by construction of the recursive tower. For the compressed part of the prepared nest the gaps have "the scale of the `M`-cubes" (Y 63826-63828), and for the seam between `Omega_m` and the nest I did not verify the floor `R_1 frakM`. Y asserts existence of the regular orbit for "the localized set in force" (Y 134217-134218) |
| all ordinary and mixed test holonomies within `eps <= a_1` | Y 35637-35639 | tower and top: proved above from (R1), (I4). Interior: (I3), Y's statement on the admitted incoming fibre, not rebuilt |
| a priori radius `R(U) <= a_c` for the profile (I2) | Y 35531-35533 | holds from the existence bound `C_B eps_int <= a_c` |
| the tested background is the orbit of (I1) | Y 134217 | by definition of the localized background; an undefined orbit counts as failure (Y 64485-64486) |

Stop (iii), no circle: the regularity of `U_X` on `E` is derived from bounds on the datum. On the collar the datum is the exterior field `V_m`, bounded by the carried density test of the global problem, which was imposed before this operation. The tested statement (curvature of `U_X` on `E`) is not used.

## 7. A3

### 7.1 Nesting

**Claim 7.1.** Every implication in Y from the final guard to an earlier guard, and the threshold ladder of Y 64233-64268, hold for `G'` whenever they hold for the inset form `chi_in kappa_x`.

*Proof.* `G' <= chi_in`, and `G'` and the literal guard agree on plaquettes with all corners in `X_in`. By Y 64221-64232 every earlier guard reads only `X cap Omega_m^c`, two cells inside `X`, hence inside `X_in`. The ladder (shell coefficient `1 - beta_s/2` to `1 - 3 beta_s/4`, exterior ratio `(eps_m/eps_j) max{L_flat^2, 3}/L^2`, collar response against the reserve) is stated on reads that "remain in the inset" (Y 64266-64268). The crossing plaquettes of `dZ''_m` are in `X cap Omega_{k_0+1}^c`, in the inset; their reserve uses a translated plaquette in the inset (Y 64335-64362). None of these reads a plaquette of `E`. `square`

What is not proved here: the implications themselves. They are Y's (collar response `hi:real-crossing-response`, the Hölder translation estimate), and Y states two obligations for the inset rule that remain: every retained test must be accounted for on its actual chart (Y 64503-64506), and "A bound only on the support of the literal prospective guard gives neither property for the inset rule" (Y 64583-64585). Name: INSET-CHART. It is independent of the rim.

### 7.2 Admission (G0-COV-ADMIT for the final-stage operation), real point

Clauses of `rg:structured-local-gauge` (Y 1251-1274) for the read `U_X` on the joined address.

**Pointwise real curvature clause.** On `X_in`: from `chi_in`, as in Y. On `E`: from `chi_E`, or from Theorem 6.2 without any test, the curvature is at most `c_0 eps_m L^{-2 lambda}`, which is below the layer-`lambda` radius once `c_0 eps_m` is below the fixed radius constant. This needs the radii of the collar layers to be constants fixed before the coupling ceiling; Y says so for `a_flat` (Y 1267-1269). If a radius at layer `lambda` were tied to `eps_lambda`, the ratio `eps_m/eps_lambda <= C (1 + (m - lambda)^{1/2})` (Y 63876) would not be bounded over the tower; I did not find the collar radii written out, so this is flagged.

**Good-gauge clause, index 0** (cubes of side at most `12 frakM` bare spacings in layers 0 and 1). By Lemma A (A2) of `g0-cover.md`, applied on a nonwrapping box of half-width `q <= 6 frakM + 1` with plaquettes below `c_0 eps_m`: one real gauge with `|v| <= 16 q c_0 eps_m`, `|delta v| <= 32 q c_0 eps_m`. The clause holds when `32 (6 frakM + 1) c_0 eps_m <= a_flat`. Class T.

**Good-gauge clause, index n >= 1; the lead's risk.** First the size: `xi_n = L^n xi` with `xi` the bare spacing (Y 1272-1274, Y 62947), so the cube has `12 frakM L^n` bare sites on a side and the clause is `|v| <= a_flat L^{-n}`, `|delta v| <= a_flat L^{-2n}`. Lemma A with plaquettes below `eps' = c_0 eps_m L^{-2n}` and `q = 6 frakM L^n` gives `|v| <= 96 frakM c_0 eps_m L^{-n}`, which is the first clause, and `|delta v| <= 192 frakM c_0 eps_m L^{-n}`, which misses the second by `L^n`. So the lead's hand estimate is confirmed: the plaquette test, through Lemma A, does not give the difference clause at index `n >= 1`. (I do not claim that no other gauge does; a curl bound does not control first differences in the supremum norm in general.)

The clause does follow in class M. Y's `prop:bg-local-gauge` (Y 25030-25066): on a cube `Q_{8r}` of one spacing `eta`, if `norm(F) <= kappa` with `r^2 kappa <= eps_*` and the actual current is bounded by `j` on `Q_{7r}`, there is a real gauge with `div A = 0` and, on `Q_r`, `norm(A) <= C r kappa`, `norm(DA) <= C (kappa + r j)`; "The gauge and the bound on `A` use only the curvature assumption; the current enters the derivative estimates." Put `r = 12 frakM xi_n`, and use `R(U_X) <= rho` on the cube in layers `n, n+1`: `kappa <= rho xi_n^{-2}`, `j <= rho xi_n^{-3}`. Then `xi_n |A| <= 12 C frakM rho` and `xi_n^2 |DA| <= C (1 + 12 frakM) rho`, which is the clause with `a_flat >= 13 C frakM rho`. The current bound is not a tested quantity. It holds because `U_X` is the critical orbit of (I1), whose radius `R_mat <= C_B eps` contains the current; on `E`, `rho = 2 K_w eps_m` by Theorem 6.2.

Not checked in this step: (i) that the cube `Q_{8r}`, of side `96 frakM xi_n`, fits in the part of the address where the assigned scale is at least `xi_n`, against layer gaps of `R_1 frakM xi_n`; if it reaches a bounded number of finer layers the constants change by fixed powers of `L`, if not the clause fails as stated; (ii) that `prop:bg-local-gauge`, proved for one spacing, is applied with the current of the constrained problem (multipliers on determining rows included in `J`). These are two of the geometric fits of `iem-supply.md`.

**Complex cores.** Nothing above is complex. For A1 the complex clauses were audited only as statements in layer units (finding 2 of section 4). For A3 the complex admission at an admitted real point is step AD4 of `t0-approach.md` (radius margin); the rim threshold enters it only through the real radius `c_0 eps_m` at each layer, which is small against a fixed radius. Not proved here.

## 8. Order of constants

1. `L` (odd, `>= 13` for (I1)), `M`, `M_1`, `frakM`, `R_1`, `rho`: the geometry.
2. From `L`: `d_L`, `C_L`, `kappa_L`, `alpha_L`, `e_*` (averaging, (R2), (I4), (I5)).
3. From the geometry: `a_c`, `K`, `delta`, `K_w = 5K`; then `a_0`, `a_1`, `C_B` ((I1), (I2)); `eps_*`, `C` of `prop:bg-local-gauge`.
4. `c_0 := 5 K_w`, `c_1 := 4`; `a_flat >= 13 C frakM * 2 K_w` times the ceiling on `eps_m`, and `a_flat` below the response ceiling (Y 1267).
5. The coupling ceiling `gamma`, such that for `g_m <= gamma`: `eps_int <= a_1`, `C_B eps_int <= min(a_0, a_c)`, `eps_int e^{-delta c M R_m} <= eps_m/2`, `4 eps_m <= a_1`, `eps_m^2 <= e_*/8`, `32 (6 frakM + 1) c_0 eps_m <= a_flat`.
6. Only for the counterexample of section 5: `m >= m_0(L, M, C, c_0)`.

None depends on `m`, on `K`-the-number-of-steps, or on the torus, given that the inputs are uniform as Y states.

## 9. What stays open, and the next step

Open or unchecked, in order of what they could break:

1. **H-GEO**: the joined determining set of `X` at the final stage (compressed nest, seam to `Omega_m`, tower) satisfies the separation floors of `bgc:proper-background`. If it fails, Theorem 6.2 has no existence input.
2. **(I3)**: the interior datum bound and its screening, Y's statements on the admitted incoming fibre.
3. **INSET-CHART**: Y's own obligations for running the operation with an inset guard from its first formation (Y 64482-64506, 64575-64590).
4. A1 is an audit bounded by search terms. The named residual risk is a term with the unlocalized structure evaluated at `U_X` inside the outer cell layer (R2, ADMISSION).
5. The cube fit in 7.2 and the collar radii being coupling-independent. Also (G3): that the tower lies inside the outer cell layer is inferred from the `M_1` scale of the tower and Y's distance statements, not from a displayed definition; if it is wider, `E` must be defined to contain it and nothing else changes.
6. Field 5.2 rests on Y's analysis of its own example.
7. Inputs (I1), (I2), (I5) and `prop:bg-local-gauge` are ported as read, unchecked; (I4) and (R2) I read with their proofs.

Consequences for the queue, for the lead to decide:

- The fresh-payment form of the rim branch is neither dead nor needed: with layer-unit thresholds on the outer collar the branch is empty on the carried support. HCM-R, RIM-LB and RIM-C (rows 488, 502, 522) concern a branch that exists only because the literal test asks the tower for `tau_m`. The carried form `hc-mark.md` (14) and TB-BC are not needed for this branch.
- Simplest form to adopt: define the final guard as Y's inset guard `chi_in kappa_x` and state Theorem 6.2 as a lemma (the outer cell layer is regular in layer units because of the carried density test). `chi_E` then never appears as a test.
- Next proof step: H-GEO, then an Opus 5.5 check of sections 5 and 6 against Y 72290-72432, 35632-35700, 12455-12502, 134205-134222.
