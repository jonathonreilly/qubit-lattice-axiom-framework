lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T15:53Z

# yjoin-port: the joined-datum comparison of Y and four shorter arguments (registry row Y-PATH, FINISH row 627)

Provenance: Claude Opus 5.5 (high), Mac mini worker 2, commit fbf9ba1cd, 2026-11-10. A port, not an audit. Source Y = YM4_1400.tex of Sussman and Alpoge (authors of the text with Claude and Codex), repository ethanwsussman/Yang--Mills-LLM-experiment at 2bc0658f91d2, fetched to a private scratch copy (136,637 lines); 'Y n' = line n. Everything taken from Y is credited to Y and is `unchecked` until another provider checks this port.

## 0. Result

Stop condition (i): the port is complete. Statements J1, J1', J2, J3 (with Lemma AVG and Lemma J3.5), D, C, M and BT are written with hypotheses, constants and Y lines, and each step was checked as written. No step failed and no counterexample was found.

- (1) `mb:real-collar-datum` (J1, section 2): holds with Y's constant `2 pi C_lift B_3 eps_1/(3(L^2-1))`. Two steps Y gives in a sentence are calculated: the geometric sum `sum_{t>=1} L^{-2t} = 1/(L^2-1)` (J1.4b), and the logarithm bound `|log h| <= (pi/3)|h - 1|` for `|h - 1| <= 1` (Lemma L3). One step Y uses without saying it: the face lift adds no curvature term to `mb:rigidity-defect`, because its block transports are 1 and its average is exact (J1.4).
- (2) `mb:real-collar-norm` (J2, section 3): holds with `C_mu = e^{6 mu delta_0} B_5 C_row 2 pi C_lift B_3/(3(L^2-1))`. The conversion `e^{6 mu delta_0}` is `e^{(delta_0/2) 12 mu}`, with `12 mu` the weighted length of a staircase path from a wide-collar point to `W^c` (`l^1 <= 4 l^inf` in four dimensions, J2.2).
- (3) The global use (J3, section 4): `sup_{b in R} |S_g S_X^{-1} - 1| <= 4 C_mu eps_* e^{-(delta_0/2) M R_m}`. Y's step "followed by averaging on these blocks" is done here as Lemma AVG: the level-`j` relative average moves by at most `2 L^j |A|_inf`, uniformly in `j`, by iterating the one-step expansion of `library/b98.md` Lemma 8 (needs `sum_n alpha_n` small and `L^j |A|` small). **The last equality `= o(delta'_j)` needs, as inequalities:** (FD) `theta_j <= theta_m + B_bar (m - j)`, with the stage window `m - j <= N_m = R_m` (stages run from `k_flat = m - N_m`, Y 63834); (RC) `R_m >= (log(theta_m - c_5))^r`, `r >= 2`; and `theta_m >= max(2c_5, 2e^2)`, `B_bar L (log theta_m)^r <= theta_m`, `(delta_0/2) M >= 1`. Then the ratio to `delta'_j` is at most `(8 C_mu eps_*/A_1) e^{-(delta_0 M/4) (log(theta_m/2))^2}` (Lemma J3.5). Without the stage window the equality can fail: (FD) alone lets `theta_j` grow with `m - j`.
- (4) Y-DENS (D, section 5): holds; case split `q <= k_0 + 1` (inside the new box: shell clause `(1 - 3beta_s/4)`; outside: deep exterior, at most `(2/25) T_d`; astride the face: wholly in `Omega_j \ Omega_q`, `kappa_x`) and `q > k_0 + 1` (in one original layer: exterior clause, at most `T_d/2`; astride: Hölder translation, errors at most `T_d/4` in the compressed range). Fit: (D-s) `C_L delta'_j + C_D eps_* e^{-c R_j} <= (beta_s/2) eps_j`.
- (5) Y-CONT (C, section 6): holds under (C-s) `C_mc pi delta'_j < eps_j`; no plaquette bound is used.
- (6) Y-BELT (BT, section 7): holds under (BT-s); three centre comparisons (test cube `C eps_* e^{-c M_2 R_m}`, annulus `C eps_* e^{-c R_m}`, `S^-` to `S` `C(L) delta'_j`) and an exhaustive case split by the number of ends in the old `Omega_m`.
- (7) Y-MEAN (M, section 6): the pivot is on the regular branch by `library/ypath-port.md` P3 (ported there, not redone); the collar block means are on their chart by C.4.
- (8) Section 8: no step of (4)-(7), nor of (1)-(3), reads a plaquette bound of `U^+` on the outer cell layer of `X` at a sharp threshold. Two places enter that layer and the earlier readings do not list them: the datum bound BT.0 and the outer band of the annulus in BT.2. Both read datum holonomies (1, or lifted top holonomies of `V_m` bounded by T4) and admitted radii only. This is what Proposition 5.3 of `inset-chart.md` needs.

What stays open: the inputs of section 9. Two of them carry the analysis and are **assumptions at the lines Y uses them**, not proved there: IN-PR (weighted kernels of the coupled inverse, "Assume ...", Y 13155; response inputs of A3, Y 16084-16085) and IN-POLY (the joined response polydisc / common admitted datum ball, Y 13244, 13345). The averaging input IN-AVX is `library/b98.md` Lemma 8, which waits for its other-provider check.

## Repo search

- `library/prior/ypath-read.md` (gpt-6-luna, not checked) sections 3 and 5: used as a map. Its line numbers agree with the file. It gives no calculations.
- `library/inset-chart.md` 5.3 and Proposition 5.3: the consumer. `library/inset-chart-check.md` item (7) is a second reading of Proposition 5.3 (HOLDS); used below as a cross-check, not as a premise.
- `library/ypath-port.md` (row 626, this worker, same day): the port of (Y-PATH). Its notation (section 2) is used here, and its input IN-POLY is J1.6 below.
- `library/b98.md` Lemma 8 (Codex, rebuild of Balaban CMP 98 Proposition 3): the one-step averaging expansion (A4). It is the input for the averaging step J3.3, which Y gives by one sentence.
- `library/open-core.md` and the FINISH rows: no entry attacks `mb:real-collar-datum`, `mb:real-collar-norm`, the global collar coordinates or the four short arguments. Rows 617, 622, 623, 626 are the consumer, its check, the reading and the path port.

## 1. Setting, norms and order of constants (Y 12959-13060, 13283-13299)

**Collars (Y 12961-12982).** `mu >= max{rho, frakM, L^2}` is a power of `L`, `rho >= L^2`. A part `A_a` is a union of cubes of side `s_a = mu xi_{j_a}` (bare units, `xi_l = L^l`). `A_a^{(-r)}` removes `r` layers of these cubes. Hypotheses: (C1) `F_a = A_a \ A_a^{(-4)}` lies in the ambient layer `j_a`, i.e. `F_a subset Omega_{j_a} \ Omega_{j_a+1}`; (C2) `dist_inf(A_a^c, A_b^c) >= 10 max(s_a, s_b)` for `a != b`. Put `W = meet_a A_a`, `W^{(-r)} = meet_a A_a^{(-r)}`, `Q_a = A_a \ A_a^{(-3)}` (the wide collar). Y 12978-12982 proves `Q_a subset F_a subset W` and that the `Q_a` are pairwise disjoint (as Y 12978-12982: a point of `F_a` is within `4 s_a` of `A_a^c`, hence at least `6 s_b` from `A_b^c`).

**Joined sequence (Y 13011-13060).** `Omega_q^W` as Y 13011-13017. As Y 13047-13058: on `W^{(-2)}` the joined masks equal the ambient ones; every new row lies in a unique `Q_a` (the collar rows). On a collar row the localized datum `V^W` is the exact face lift (Y 13060-13071) of the ambient level-`j_a` datum; its one-step average is exactly the preceding lifted datum, and it equals 1 on every bond inside one ambient `j_a`-block (Y 13072-13083).

**Norms.** `|g - 1|` is the operator norm; `d(g,h) = |log(g h^{-1})|` the geodesic distance on SU(2), bi-invariant. For a unitary `h` with angle `phi = |log h|` in `[0, pi]`: `|h - 1| = 2 sin(phi/2)`. Hence (N) `(2/pi) d(g,h) <= |g h^{-1} - 1| <= d(g,h)` (as in ypath-port section 2), and (L3) below.

**(L3) Lemma.** If `|h - 1| <= 1` then `|log h| <= (pi/3) |h - 1|`.
*Proof.* `2 sin(phi/2) <= 1` with `phi in [0, pi]` gives `phi <= pi/3`. The function `x / sin x` increases on `(0, pi/2]`, so `phi / (2 sin(phi/2)) <= (pi/6)/sin(pi/6) = pi/3`. Square.

**Inputs with constants** (all fixed before `M`; Y lines in section 7): `B_3` (regularity improvement, IN-IMP), `C_lift` (rigidity coefficient, IN-RIG), `a_0, a_1, C_B` (IN-BG), `r_B` (joined response polydisc, IN-POLY), `B_5, delta_0` (point response, IN-PR), `C_row` (row sum at rate `delta_0/2`, IN-ROW), `C_1, c_3` and `K_lin` (one-step averaging expansion, IN-AVX). Order: `L, rho, frakM, mu` first; then the input constants; then `C_mu` (J2); then `M`; then the ceilings `eps_1` (and `eps_*`); then the coupling floor.

## 2. (Y-JOIN 1) `mb:real-collar-datum`, Y 13283-13349

**Statement J1.** Assume the collar geometry of section 1, the floors of the real background theorem (no-inward determining sets, separation, weighted-response floors, at least `6 rho` sites per direction at the last level; Y 13285-13289). Let `V` be a real datum all of whose test holonomies are within `eps_1` of one, and let `eps_1` satisfy

(J1-s) `B_3 eps_1 <= a_0`, `2 B_3 eps_1 <= c_reg` (the threshold of IN-AV), and `2 C_lift B_3 eps_1 / (L^2 - 1) <= 1`.

Let `U` be critical in the regular orbit of `V`, and `U_W^o` the normalized representative of the regular orbit of `V^W`. Then there is a real gauge `g` on the joined first member, equal to 1 off the wide collars and equal to 1 at both ends of every common row, such that the induced datum of `(U|_{Omega_0^W})^g` is `e^{iB} V^W` with `B = 0` off the collar rows and

  `||B||_inf <= 2 pi C_lift B_3 eps_1 / (3 (L^2 - 1))`.  (mb:real-collar-datum)

*Proof, step by step.*

J1.1 (radius; Y 13293-13295). By IN-IMP, `U` has radius `eps := B_3 eps_1 <= a_0`. Cited, not redone.

J1.2 (restriction; Y 13295-13299). As Y 13295-13299 by `mb:restriction-identity` (IN-RES): `U|_{Omega_0^W}` is critical at its induced datum, which equals `V^W` on common rows.

J1.3 (curvature of the averages; Y 13301-13308). Fix `a` with `j = j_a >= 1`. By `mb:uniform-real-average` (IN-AV, Y 10980-10998) with `k = j` and the threshold of (J1-s): `|dW_q(p) - 1| <= 2 eps L^{2(q-j)}` for every plaquette `p` inner in `Q_a` and `0 <= q <= j`, where `W_q = M^q U`. Raw group defects, not divided by any spacing. At `q = j` the inner bonds of `Q_a` are determining rows, so `W_j = V_j` there (Y 13306-13308; this is the definition of the determining rows).

J1.4 (the aligned gauge on `Q_a`; Y 13309-13318). Let `U_0` be the face lift of `W_j = V_j` on `Q_a`. Define the descending gauge as Y 10885-10895 (`g_j = 1` on level-`j` sites; `g_n(x) = W_{0,n}(y,x)^{-1} g_{n+1}(y) W_n(y,x)` on the block of a next-level centre `y`). Let `e_n` be the largest `|M^n(U^g)(b) - M^n(U_0)(b)|` over level-`n` bonds `b` of `Q_a`. Then

  `e_n <= e_{n+1} + C_lift varpi_n(U)`,  `e_j = 0`.  (J1.4a)

This is `mb:rigidity-defect` (IN-RIG, Y 10862-10871) with `d_T = 0` (the gauge makes the contour values equal in every block, Y 10892-10895). The term `C_L varpi(U_0)` of `mb:rigidity-defect` is absent for the lift, and Y uses this without saying it: every level-`n` block (`n < j`) lies inside one level-`j` block, where the lift is 1, so its contour transports are 1, its transported value is exactly its bond value, and its one-step average is exact (Y 13076-13083). So the comparison `mb:bond-reconstruction` for `U_0` has error 0. `e_j = 0` since `M^j(U^g) = W_j = V_j` on level-`j` bonds (`g = 1` on level-`j` sites) and the lift at level `j` is `V_j`.

The calculation Y gives by one sentence ("The denominator comes from summing the smaller curvature bounds over `q < j`", Y 13316-13317): by J1.3, `varpi_n(U) <= 2 eps L^{2(n-j)}`. Summing (J1.4a) from `n = q` to `j - 1`:

  `e_q <= sum_{n=q}^{j-1} 2 C_lift eps L^{-2(j-n)} <= 2 C_lift eps sum_{t>=1} L^{-2t} = 2 C_lift eps / (L^2 - 1)`.  (J1.4b)

This is Y's bound, with `C_lift` the constant `C_L` of `mb:rigidity-sum`.

J1.5 (one gauge, common rows unchanged; Y 13318-13333). The `Q_a` are disjoint (section 1), so the gauges on the `Q_a` and 1 elsewhere define one gauge `g`. Let a common row have an end in `Q_a`. Its layer end lies in `W`. Case (i): in `F_a`; by (C1) the row has level `j_a`. Case (ii): outside `F_a`; then it lies in `A_a^{(-4)}`, which is at sup distance at least `s_a` from `Q_a = A_a \ A_a^{(-3)}`, so the row has bare length at least `s_a = mu xi_{j_a} >= L^2 xi_{j_a} = xi_{j_a+2}`, and a row of level `n` has bare length `xi_n`, so `n >= j_a + 2`. Both ends of a row of level `n` lie in `Omega_n subset Omega_{j_a+1}`; but its end in `Q_a subset F_a` lies outside `Omega_{j_a+1}` by (C1). So case (ii) does not occur. In case (i) the row joins level-`j_a` sites, where `g = 1` (J1.4). So `g` fixes every common row. If `j_a = 0` there are no new rows of that part (Y 13333).

J1.6 (the logarithmic datum; Y 13335-13349). By J1.2 and J1.5 the induced datum of `(U|)^g` equals `V^W` on common rows, so `B = 0` there. On a collar row of level `q < j_a` the induced datum is `M^q(U^g)` on that row, and `V^W` is the lift there (section 1), so the group discrepancy is at most `e_q <= 2 C_lift eps/(L^2 - 1) <= 1` by (J1.4b) and (J1-s). Lemma (L3) gives `|B| <= (pi/3) e_q`, so

  `||B||_inf <= (pi/3) 2 C_lift B_3 eps_1/(L^2 - 1) = 2 pi C_lift B_3 eps_1 / (3(L^2 - 1))`.

This is (mb:real-collar-datum), and the step is checked. Square.

**Statement J1' (the endpoint identification; Y 13350-13366).** Assume also (J1-r) `2 pi C_lift B_3 eps_1/(3(L^2-1)) < r_B`. Then for `0 <= t <= 1` the datum `e^{itB} V^W` lies in the joined response polydisc (a polydisc is a product of discs, and `||tB|| <= ||B||`). The point `t = 0` carries the regular orbit of `V^W` (the orbit of `U_W^o`); the point `t = 1` carries the orbit of `(U|)^g`, which is critical at `e^{iB}V^W` by J1.2 and gauge covariance of restriction, with radius at most `B_3 eps_1 <= a_0` (J1.1), hence is the regular orbit by the uniqueness of IN-BG at `a_0`. With `f := H_W(B)` (the response in its normalized slice, IN-POLY), restoring the gauges gives `U|_{Omega_0^W} = (e^{i eta f} U_W^o)^w`, with `w = v_q[U_W^o; f]^{-1}` at the level-`q` tops off the collars (Y 13362-13366). These are Y's statements; the uniqueness and the polydisc are inputs (IN-BG, IN-POLY), not redone.

## 3. (Y-JOIN 2) `mb:real-collar-norm`, Y 13368-13396

**Statement J2.** Under J1 and J1', for every joined bond `x` with top `y`:

  `N_x(f) <= C_mu eps_1 e^{-delta_0 d_B(y, W^c)/2}`,  `C_mu := e^{6 mu delta_0} B_5 C_row 2 pi C_lift B_3 / (3(L^2 - 1))`.  (mb:real-collar-norm)

`N_x` is the maximum of the potential, first covariant difference and `D^T D` readouts at `x`, times the first, second and third power of the joined top spacing (Y 13368-13372). `d_B` is the ambient weighted distance (bare length divided by the local ambient spacing), `d_{B^W}` the joined one.

*Inputs.* (IN-PR) For every `t in [0,1]` and every collar row `c` with top `y_c`, each of the three readouts of `(d/dt) H_W(tB)` at `x` is bounded, in the normalization of `N_x`, by `B_5 e^{-delta_0 d_{B^W}(y, y_c)} |B(c)|` summed over `c` (Y 13372-13376; `mb:point-response`, Y 13145-13163, and "the same calculation applies ... to each proved differentiated field readout", Y 13161-13163). (IN-ROW) `sup_y sum_c e^{-delta_0 d_{B^W}(y, y_c)/2} <= C_row`, independent of depth and volume (Y 13376-13377, `mb:extended-source`, Y 13165-13178).

*Proof.*

J2.1 (half the rate for the sum). For each `t`, by IN-PR and IN-ROW,
  `N_x((d/dt) H_W(tB)) <= B_5 ||B||_inf sum_c e^{-delta_0 d_{B^W}(y,y_c)} <= B_5 C_row ||B||_inf e^{-(delta_0/2) inf_c d_{B^W}(y,y_c)}`,
writing `e^{-delta_0 d} = e^{-delta_0 d/2} e^{-delta_0 d/2}` and bounding the second factor by its supremum over `c`.

J2.2 (a collar point is near `W^c`; Y 13378-13382). Let `z in Q_a`. Its sup distance to `A_a^c` is at most `3 s_a`; let `z'` be a nearest point of `A_a^c`. Every point `w` of the segment `[z, z']` has `dist_inf(w, A_a^c) <= |w - z'|_inf <= 3 s_a`, so `w` is outside `A_a^{(-3)}`, hence in `Q_a subset F_a` until it leaves `A_a`. A lattice staircase path along the segment has bare length `|z - z'|_1 <= 4 |z - z'|_inf <= 12 s_a` (four dimensions) and stays in `F_a`, in the ambient layer `j_a` by (C1), where the spacing is `xi_{j_a}`. Its weighted length is at most `12 s_a / xi_{j_a} = 12 mu`. Since `W subset A_a`, `z' in A_a^c subset W^c`; so `d_B(z, W^c) <= 12 mu`. (The staircase's lattice points are within one bare spacing of the segment; this changes the bound by at most a lattice unit and is absorbed by taking the segment between lattice points of the closed cube representatives, Y 12965.)

J2.3 (distance conversion; Y 13382-13391). Let `y` be a top and `c` a collar row. Take a joined path from `y` to `y_c` and stop it at its first point `z` on the boundary of `W^{(-3)}`. Up to `z` the path is in `W^{(-2)}`, where the joined and ambient masks agree (section 1), so its joined weighted length up to `z` equals its ambient weighted length, which is at least `d_B(y, z)`. The point `z` lies in a wide collar, so by J2.2 `d_B(y, W^c) <= d_B(y, z) + 12 mu`. Hence

  `inf_c d_{B^W}(y, y_c) >= d_B(y, W^c) - 12 mu`.  (J2.3)

If `y` lies in a wide collar, the right side is at most 0 by J2.2, and (J2.3) is trivial.

J2.4 (integration; Y 13391-13396). `H_W(0) = 0`, so `f = int_0^1 (d/dt) H_W(tB) dt`, and each readout of `N_x` is linear in the field at the fixed reference `U_W^o` (Y 13368-13372: the readouts of the comparison potential in its slice), so `N_x(f) <= sup_t N_x((d/dt)H_W(tB))`. By J2.1 and (J2.3),

  `N_x(f) <= B_5 C_row ||B||_inf e^{6 mu delta_0} e^{-delta_0 d_B(y,W^c)/2}`,

and J1 gives `||B||_inf`. This is (mb:real-collar-norm) with the constant `C_mu` above. The factor `e^{6 mu delta_0}` is `e^{(delta_0/2) 12 mu}`, as Y says. Checked. Square.

Remark (what `C_mu` depends on). `C_mu` depends on `mu` through `e^{6 mu delta_0}` and on the input constants only; Y 13394-13396: "independent of the depth and volume". It is not uniform as `mu -> infinity` (Y 13248-13250). In the global use (section 4) `mu` is a fixed constant, not `M R_m`; this matters, since a collar width growing like `M R_m` would cancel the decay.

## 4. (Y-JOIN 3) The global real collar coordinates, Y 65019-65067

**Setting (Y 65021-65031).** A stage transition `j -> q = j+1` of the operation of level `m`, so `k_flat = m - N_m <= j <= m - 1` (Y 63834: stages `j = k_flat, ..., k-1`; Y 1182 and 1121: `t_flat = t - N_t`, `N_t = R_t`; here `R_m` is Y's `\check R_m`). The prospective real datum `omega` is fixed, with its global critical orbit `U_g := U_m^{(n+1)}` and its local orbit `U_X := U_{m,X}^{(n+1)}` admitted. `S_g = M^j U_g`, `S_X = M^j U_X`. `a_m = M R_m L^m` (bare side of a level-`m` cell).

**Hypotheses.**
- (H-J) (Y 65026-65028, 13414-13425) The global and the local sequences agree on `W := X` as separated sequences, with real data agreeing on every determining bond with both ends in `X` ("the two joined problems have the same determining rows and data in the interior of `X`; the difference comes from the outer joining collar"). The localization to `X` is a joined sequence of section 1 with parts of level `j_a = m` and a fixed collar width `mu` (not growing with `M` or `R_m`). Its four-layer collars lie in `X \ O_m subset Omega_m`, the top layer, which needs `4 mu <= 2 M R_m` (`O_m = Omega_m^c cap X = H_m^{[8 a_m]}`, `X = H_m^{[10 a_m]}`, Y 63760-63766).
- (H-eps) Both data have all test holonomies within `eps_*` of one, and `eps_1 := eps_*` satisfies (J1-s), (J1-r). For the global datum this is part (ii) of the certificate `I` of inset-chart 5.2; for the local datum part (i).
- (H-R) (Y 65034-65053) Every point of the collar read set `R` (the order-`j` average carriers of the fine rows of `K`, the full double blocks of the new level-`q` rows and of every inherited coarse row whose stencil reads a changed fine bond, and the four-layer test-cube enlargements of the old groups at the `Omega_q` seam) is at bare sup distance at least `a_m` from `X^c`; and every point of `R` has joined top spacing at least `xi_j = L^j` (Y 65050-65053: "keeps these carriers out of finer layers").
- (IN-FRAME) (Y 65028-65031, 13362-13366) On `R` the two coordinates are the node-framed averages: with `U_g|_W = (e^{i eta f_g} U_W^o)^{w_g}` and `U_X|_W = (e^{i eta f_X} U_W^o)^{w_X}` (J1' applied to each), the axial readings with the same retained node data are `P_• (b) = S_j[f_•](b) M^j U_W^o(b)`, where `S_j[f]` is the double-bar average of `library/b98.md` (A3) with `U_1 = e^{i eta f}`, `U_0 = U_W^o`. So `S_g(b) S_X(b)^{-1} = S_j[f_g](b) S_j[f_X](b)^{-1}`. This is the reading of "Use the prescribed block axial readings with the same retained node data. On the full blocks these readings include the node factors of the real response."

**Statement J3.** Under these hypotheses, with `tau := C_mu eps_* e^{-delta_0 M R_m/2}`, if (J3-s) `2 tau <= c_3`, `M R_m >= 2 C_st` and `4 C_1 tau + 2 K_lin B_3 eps_* <= ln 2`, then

  `sup_{b in R} |S_g(b) S_X(b)^{-1} - 1| <= 4 C_mu eps_* e^{-(delta_0/2) M R_m}`.  (J3)

So Y's `C eps_* e^{-c M R_m}` holds with `C = 4 C_mu`, `c = delta_0/2`.

*Proof.*

J3.1 (distance; Y 65034-65056). `K subset Omega_q^c cap X subset O_m`, and `O_m` is two level-`m` cells inside `X`, so `dist_inf(K, X^c) >= 2 a_m`. The carriers add at most `C_st L^m` (Y 65038-65041), so with `M R_m >= 2 C_st`, `dist_inf(R, X^c) >= 2 a_m - C_st L^m >= a_m` (for the old groups this is (H-R)). A path from `y in R` to `X^c` has bare length at least `a_m`, and every spacing is at most `L^m` ("no layer has spacing greater than `L^m`", Y 65055), so its weighted length is at least `a_m / L^m = M R_m`. Thus `d_B(y, W^c) >= M R_m` on `R` (`W = X`).

J3.2 (the comparison field). Apply J1, J1', J2 to each of the two backgrounds against the common joined background `U_W^o` (Y 13414-13425): for every bond `x` of `R`, `N_x(f_g), N_x(f_X) <= C_mu eps_* e^{-delta_0 M R_m/2} = tau`. The real gauge `g` of J1 is 1 on `R`, which is at distance `>= a_m > 3 mu L^m` from the collars.

J3.3 (averaging; the calculation behind Y's "followed by averaging on these blocks", Y 65056-65057). **Lemma AVG.** Let `U_0` be real on the carrier of a level-`j` bond `b`, with `alpha_n` the largest raw plaquette defect of `M^n U_0` on the level-`n` double-block read boxes of the carrier, `alpha_n <= c_3` and `sum_{n<j} alpha_n <= sigma`. Let `A` be a perturbation of the bare bonds of the carrier with `L^j |A|_inf <= tau`. If `2 tau <= c_3` and `K_lin sigma + 4 C_1 tau <= ln 2`, then `|log S_j(b)| <= 2 L^j |A|_inf`.

*Input (IN-AVX), `library/b98.md` Lemma 8 (Balaban CMP 98 Proposition 3, rebuilt by Codex, not yet checked by another provider).* For a real background `V_0` with plaquette defects `< alpha <= c_3` on the read boxes and `V_1 = e^{iA'}`, `|A'| < c_3`: `log S_{V_0}(V_1)(c) / i = L (Q(V_0) A')_c + C(V_0, A', c)` with `|C| <= C_1 L^2 |A'|^2` (b98 (A4)), and by the five-term formula (A5), `L |(Q(V_0) A')_c| <= L |A'| (1 + K_lin alpha)`. The second bound is read off (A5) as follows: the main term `sum_x w t_x` has `|t_x| <= L |A'|` and `sum_x w = L^d L^{-(d+1)} = L^{-1}`, so it is at most `|A'|`; each of the other four terms has a coefficient that vanishes at `Y = Y_x = 0` and is analytic on the fixed chart, hence is at most `K (|Y| + max_x |Y_x|) <= K c_d L^2 alpha` (each relative loop encloses at most `c_d L^2` plaquettes, b98 Lemma 8), multiplied by `|h_x|, |t_x|, |k_x| <= c_d L |A'|` or `L^{-1}|a| <= L^{-1}|A'|` and by weights summing to `L^{-1}`; so `K_lin := 4 K c_d^2 L^2` works.

*Proof of Lemma AVG.* By b98 (c), `S_{n+1} = S_{M^n U_0}(S_n)`, `S_0 = e^{iA}`. Let `a_n` be the largest `|log S_n|` on the level-`n` bonds of the carrier, and `b_n = L^{-n} a_n`. As long as `a_n <= c_3`, IN-AVX gives

  `a_{n+1} <= L (1 + K_lin alpha_n) a_n + C_1 L^2 a_n^2`, i.e. `b_{n+1} <= b_n (1 + K_lin alpha_n + C_1 L^{n+1} b_n)`.

Claim: `b_n <= 2 b_0` for `0 <= n <= j`. Induction: if it holds up to `n < j`, then `a_i = L^i b_i <= 2 L^j b_0 <= 2 tau <= c_3` for `i <= n`, and

  `b_{n+1} <= b_0 prod_{i=0}^{n} (1 + K_lin alpha_i + 2 C_1 L^{i+1} b_0) <= b_0 exp(K_lin sigma + 2 C_1 b_0 sum_{i=0}^{n} L^{i+1})`.

`sum_{i=0}^{n} L^{i+1} = L (L^{n+1} - 1)/(L - 1) <= 2 L^{n+1} <= 2 L^j` for `L >= 2`. So the exponent is at most `K_lin sigma + 4 C_1 L^j b_0 <= K_lin sigma + 4 C_1 tau <= ln 2`, and `b_{n+1} <= 2 b_0`. Hence `|log S_j(b)| <= a_j <= 2 L^j |A|_inf`. Square.

J3.4 (apply). Take `U_0 = U_W^o`, `A = eta f_•`. Its radius is at most `B_3 eps_*` (J1.1), and the read set lies in layers of top level at least `j`, so by IN-AV `alpha_n <= 2 B_3 eps_* L^{2(n-j)}` and `sigma := sum_{n<j} alpha_n <= 2 B_3 eps_*/(L^2 - 1) <= 2 B_3 eps_*`. The bare link angle at `x` is `|eta f(x)|`, and `N_x(f) >= xi_x |f(x)|` with `xi_x / eta >= L^j` on `R` (H-R), so `L^j |eta f(x)| <= N_x(f) <= tau` (J3.2). Lemma AVG gives `|log S_j[f_•](b)| <= 2 tau`, and by (IN-FRAME) and unitarity,

  `|S_g S_X^{-1} - 1| <= |S_j[f_g] - 1| + |S_j[f_X] - 1| <= |log S_j[f_g]| + |log S_j[f_X]| <= 4 tau`.

(`|e^{iZ} - 1| <= |Z|` for Hermitian `Z`.) This is (J3). Square.

J3.5 (the last equality `= o(delta'_j)`; Y 65062-65067). Y names two conditions. As inequalities:

- (FD) frame drift, Y 1103-1107: for `i <= l`, `lambda_low (l - i) - c_5 <= theta_i - theta_l <= B_bar (l - i)`. Used with `(i, l) = (j, m)`: `theta_j <= theta_m + B_bar (m - j) <= theta_m + B_bar N_m = theta_m + B_bar R_m` (stage window, setting above).
- (RC) `R_m >= (log(theta_m - c_5))^r` with `r >= 2`. Proof from Y's definitions: `R_m = R(min_{i<=m} theta_i)`, `R(y)` the least power of `L` not below `(log y)^r` (Y 1108-1111); by the lower half of (FD) with `l = m`, `theta_i >= theta_m - c_5` for `i <= m`, and `R` is nondecreasing. Also `R_m <= L (log theta_m)^r`, since `min_i theta_i <= theta_m`.

With `delta'_j = g_j A_1 p_1(g_j) = A_1 theta_j^{-1/2} (log theta_j)^{p_1} >= A_1 theta_j^{-1/2}` (Y 63834, 1111-1117; `log theta_j >= 1` since `theta_j >= gamma^{-2} > e`):

**Lemma J3.5.** Assume (FD), (RC), `theta_m >= max(2 c_5, 2 e^2)`, `B_bar L (log theta_m)^r <= theta_m`, and `c M >= 1` with `c = delta_0/2`. Put `u := log(theta_m/2) >= 1`. Then for every `s >= 0`

  `4 C_mu eps_* e^{-c M R_m} <= (8 C_mu eps_*/A_1) 3^s u^s e^{-c M u^2/2} delta'_j (log theta_j)^{-s}`,

and the factor `u^s e^{-cMu^2/2}` tends to 0 as `theta_m -> infinity`. So the bound is `o(delta'_j)`, and `o(delta'_j (log theta_j)^{-s})` for each fixed `s` (Y 65066-65067).

*Proof.* By (FD) and `R_m <= L(log theta_m)^r`: `theta_j <= theta_m + B_bar L (log theta_m)^r <= 2 theta_m`. So `delta'_j >= A_1 (2 theta_m)^{-1/2} = (A_1/2) e^{-u/2}` (since `2 theta_m = 4 e^u`). By (RC) and `theta_m - c_5 >= theta_m/2`: `R_m >= u^r >= u^2`, so `e^{-c M R_m} <= e^{-c M u^2}`. Hence `4 C_mu eps_* e^{-cMR_m} / delta'_j <= (8 C_mu eps_*/A_1) e^{u/2 - c M u^2} <= (8 C_mu eps_*/A_1) e^{-cMu^2/2}`, using `u/2 <= cMu^2/2` (`u >= 1`, `cM >= 1`). Finally `log theta_j <= log(2 theta_m) = u + log 4 <= 3u`, so `(log theta_j)^s <= 3^s u^s`. Square.

(If `p_1 < 0`, use `delta'_j >= A_1 theta_j^{-1/2} (3u)^{p_1}` instead; this multiplies the bound by `(3u)^{|p_1|}`, and the conclusion is unchanged, since `u^{s + |p_1|} e^{-cMu^2/2} -> 0`.)

So the last equality of Y needs exactly: the stage window `m - j <= N_m = R_m`, the upper frame drift `B_bar`, and `R_m` at least the square of `log(theta_m - c_5)`. Without the stage window it fails: (FD) alone allows `theta_j` as large as `theta_m + B_bar (m - j)` with `m - j` unbounded in terms of `theta_m`, and then `delta'_j` can be below `e^{-cMR_m}`.

**Inputs of J1-J3 from outside the argument:** IN-IMP, IN-RES, IN-AV, IN-RIG, IN-BG, IN-POLY, IN-PR, IN-ROW, IN-AVX, IN-FRAME, (H-J), (H-R), the stencil constant `C_st`; Y lines in section 9.

## 5. (Y-DENS 4) The lower density test on the inset-positive real collar chart, Y 64699-64789

**Setting.** `h < j < m`, `q = j + 1`, a point `(omega, B)` of the real collar chart: `omega` with `G(omega) = 1` (the inset guard `chi_in`, `kappa_x` and T3 pass at the fixed prospective orbit `U^+`), `U^+` admitted with radius `e <= e_*`, and `B` in the approximate ball. The lower density test at level `j` reads the plaquettes of its four-layer halo in the preceding background localized as the density test prescribes (density box with the lifted `V_j` on the pure level-`j` tower; Y 64776-64782), with threshold `T_d := eps_j L^{-2j}` (Y 61975-61977 for the form at level zero; Y 64735-64737 and 64788 for the threshold at level `j`).

**Statement D.** Assume (S-e), (S-d), (S-r) of ypath-port section 2, and (D-s) below. Then every plaquette `p` of the halo of every lower density cube of level `j` has `|dU_dens(p) - 1| < T_d` at every point of the chart, where `U_dens` is the background the density test reads. So the lower density test equals 1 there.

*Steps.*

D.1 (placement; Y 64699-64716). Bases are in `(Omega_j^{~4} \ Omega_q^~) cap X`; the halo extends less than one level-`j` cell, so (eight-cell gap to `Omega_{j-1}^c`, exclusion of `Omega_q^~`) it lies in `Omega_{j-1} \ Omega_q`, hence in `Omega_q^c cap X subset O_m` (the top inset of `X`), and it misses `Z''_j` (five cells from `Omega_j` for `j <= k_0`, seven at `j = k_0 + 1`, and `Z''_j` outside `Omega_{j-1}` later). As Y 64699-64716; the distances are those of `eq:elab-history-prepared-boxes` (Y 63776-63800).

D.2 (adjacent thresholds). `eps_q <= 2 eps_j`. *Calculation.* `eps(theta) = A_0 theta^{-1/2}(log theta)^{p_0}` decreases for `theta > e^{2 p_0}`; by (FD) `theta_q >= theta_j - B_bar`; so `eps_q <= eps(theta_j - B_bar) <= 2 eps(theta_j)` once `theta_j >= theta_D(B_bar, p_0)`. (Y states `eps_{k+1} <= C eps_k`, Y 4583.)

D.3 (case `q <= k_0 + 1`; Y 64718-64737). Three cases for a halo plaquette `p`, with the clause of the prospective guard that `G(omega) = 1` supplies:
- (D3a) wholly inside the new prepared box `Z''_q`: new shell clause, `|dU^+(p) - 1| < (1 - 3 beta_s/4) eps_j L^{-2j} = (1 - 3beta_s/4) T_d` (`F_j = 1` since `j <= k_0`).
- (D3b) wholly outside it: deep exterior clause with `i_0 = j`, `|dU^+(p) - 1| < (1 - beta_s/2) eps_q L^{-2q} <= 2 L^{-2} T_d <= (2/25) T_d` by D.2 and `L >= 5`.
- (D3c) astride the new face: the face is `5 a_q` (or `7 a_q` at `q = k_0 + 1`) from `Omega_q`, and `dist(Omega_j^c, Omega_q) >= 8 a_q`; a bare plaquette astride it has all corners at distance in `[5a_q - 1, 7 a_q + 1] subset (0, 8 a_q)` from `Omega_q` (`a_q >= 2`), so it is wholly in `Omega_j \ Omega_q`. The preceding guard reads it, and the crossing test `kappa_x` gives `|dU^+(p) - 1| < (1 - 3beta_s/4) T_d`.
So in case `q <= k_0 + 1`: `|dU^+(p) - 1| < (1 - 3beta_s/4) T_d` for every halo plaquette (`3beta_s/4 < 1 - 2/25`).

D.4 (case `q > k_0 + 1`; Y 64739-64770). The halo misses both prepared boxes and lies in the prospective layer `q`.
- (D4a) `p` wholly in one of the two original layers at the `Omega_j` wall: exterior clause, `|dU^+(p) - 1| <= (1 - beta_s/2) max{3, L_flat^2} eps_q L^{-2q} <= 2 max{3, L_flat^2} L^{-2} T_d <= (1/2) T_d`, by D.2, `L_flat < L/2` and `L >= 5` (`6/L^2 <= 6/25 < 1/2`).
- (D4b) `p` astride the wall: translate it by a bounded number of bare spacings to `p'` wholly in the original layer `j`, inside the same prospective comparison cube; `p'` has the bound of (D4a). In a common real gauge, IN-HOL (`mb:local-regularity-conclusion`, Y 15778-15812; `mb:holder-reduction`, Y 11901-11917) bounds the change of the curl by `E_H := C_H eps_* L^{-(2+alpha) q}`, and the terms of order at least two in the plaquette logarithm vary by `E_2 := C_2' L^{-3q}` (Y 64757-64763). The calculation Y gives as "both errors are `o(eps_j L^{-2j})`" (Y 64763-64767): with `q = j + 1`, `E_H / T_d = C_H eps_* L^{-2} L^{-alpha q} / eps_j` and `E_2 / T_d <= C_2' L^{-q} / eps_j`. By IN-COMP (Y 64764-64765: in the compressed range `q >= m - C_c log R_m`, and `m >= R_m`), `q >= R_m - C_c log R_m >= R_m/2` once `R_m >= R_0(C_c)`. By the proof of Lemma J3.5 (`theta_j <= 2 theta_m`, `R_m >= u^2`, `u = log(theta_m/2)`), `eps_j >= A_0 theta_j^{-1/2} >= (A_0/2) e^{-u/2}`. So `(E_H + E_2)/T_d <= (2(C_H eps_* + C_2')/A_0) e^{u/2 - (alpha ln L/2) u^2}`, which is at most `1/4` once `u` is large (that is, `gamma` small). So `|dU^+(p) - 1| <= (1/2 + 1/4) T_d`.
(The comparison of group defects through the plaquette logarithm uses (L3) and (N); both defects are below 1.)

D.5 (transfer and localization; Y 64772-64789). By (E1) of ypath-port P5.4 (the halo is in `X cap Omega_m^c`, outside the old shells by D.1), `|dU^-(p) - 1| <= |dU^+(p) - 1| + C_L delta'_j L^{-2j}`. The density test background is the localization of the preceding background on the density box with the lifted `V_j` (Y 64776-64782); the inner plaquettes have the three-small-cube margin to the boundary of that localization, and the joined comparison (J1, J2, and the plaquette difference of Y 13398-13411) bounds the difference by `C_D eps_* e^{-c R_j} L^{-2j}` (Y 64783-64786; input IN-DBOX for the distance `c R_j` in level-`j` units).

D.6 (fit). The smallest reserve in D.3-D.4 is `(3beta_s/4) T_d` (`beta_s < 1/4`). The condition

  (D-s) `C_L delta'_j + C_D eps_* e^{-c R_j} <= (beta_s/2) eps_j`

gives `|dU_dens(p) - 1| < (1 - beta_s/4) T_d < T_d`. (D-s) holds at weak coupling: `delta'_j / eps_j = (A_1/A_0)(log theta_j)^{-(p_0 - p_1)}`, and `eps_* e^{-c R_j} / eps_j -> 0` by the argument of Lemma J3.5 with `c` in place of `cM` (it needs `u >= 1/c`, a floor on `theta_j`). Checked. Square.

Inputs of D: `G(omega) = 1` (inset guard clauses: shell, deep exterior, exterior; `kappa_x`), (E1) (ypath-port P5.4), IN-HOL, IN-COMP, IN-DBOX, J1-J2 with the plaquette difference (Y 13398-13411), (FD), the geometry of D.1 (Y 63776-63800, 63885-63896, 64701-64716).

## 6. (Y-CONT 5) and (Y-MEAN 7): contour indicators and the regular branch, Y 64791-64810 and 64929-64953

**Statement C (Y-CONT).** On the approximate collar ball over an admitted `omega`, every contour indicator of the old exterior belt equals 1 at its original threshold `eps_j`, provided (C-s) `C_mc pi delta'_j < min(eps_j, rho_mc)`.

*Steps.*
C.1 (Y 64791-64796). The indicators use the order-`q` blocks based between the first and third layers outside `Omega_q`. These blocks lie in the collar `K`; the new gauge insertion starts beyond the third layer. As Y.
C.2 (Y 64796-64800). All internal links of such a block are tested exterior nonpivots, so on the ball `|n(b) S(b)^{-1} - 1| < 2 delta'_j`, hence `d(n(b), S(b)) < pi delta'_j` by (N).
C.3 (Y 64799-64801). After promotion the block contains no finer determining node, so in the prospective axial frame the mean contours of the reference `S` on the block are trivial: each equals 1. Y states this; it is the definition of the block axial frame with no interior node (input IN-AXF).
C.4 (Y 64802-64808; the calculation). Let `T_B` be the mean contour map of the full block, from the internal links (sup of `d` per link) to the contour values. IN-MC: on the regular chart of radius `rho_mc` about the reference it has derivative at most `C_mc` (Y: "The mean contour map on the full block has a bounded derivative"; by IN-MEAN, lem:averaging-1a-1-1, Y 3714, and Cauchy estimates). The segment `n_t(b) = exp(t log(n(b)S(b)^{-1})) S(b)` stays in the ball (ypath-port P4(i)), so `d(T_B(n), T_B(S)) <= C_mc max_b d(n(b), S(b)) < C_mc pi delta'_j`. With C.3, `d(T_B(n), 1) < C_mc pi delta'_j < eps_j` by (C-s), and `|T_B(n) - 1| <= d(T_B(n), 1)` by (N). "Also after changing the stage centre" (Y 64803-64804): the same bound holds with `S^-` in place of `S`, since `|S^- S^{-1} - 1| <= C(L) delta'_j` (BT.3 below, Y 64139-64168; ypath-port P4-P5), which changes `C_mc pi` to `C_mc (pi + pi C(L))`. Checked. Square.

**Statement M (Y-MEAN).** On the approximate collar ball, (i) the actual pivot of every newly imposed coarse row is on the regular branch, and (ii) every block mean of the exterior collar used by the mean-contour axial readings is on its regular chart.

*Port.* (i) is ypath-port P3.1-P3.4 (Y 64910-64958), ported and checked there (pivot within `C_3(e + delta'_j)` of `b^+`, then within `C_4 delta'_j`; regular branch by IN-REG under (S-e), (S-d)). Not redone. (ii) is C.4 with `rho_mc` in place of `eps_j`: `d(T_B(n), 1) < C_mc pi delta'_j <= rho_mc`. On the double block of `c` the plaquette defects of the induced field are at most `C_av e` (`O_L(e)`, Y 64929-64935; ypath-port P1(iii)), and the regular averaging formula puts the central transport within `C(L) e` of `W` (ypath-port P3.1 step (2)). Checked.

Inputs: IN-AXF (Y 64799-64801), IN-MC/IN-MEAN (Y 3714, 64806-64808), the approximate collar test (Y 64032-64038), ypath-port P3 and its inputs (IN-AVF, IN-TRANS, IN-REG, IN-ROW).

## 7. (Y-BELT 6) The fifth and sixth ordinary approximate-test groups, Y 64027-64211

**Setting (Y 64027-64052).** Last stage: `j = m - 1`, `Y = Z''_m(X)`, `K = (Omega_m^c \ Y) cap X`. `S = M^j U_{m,X}^{(N_m)}` (centre of the approximate collar test), `S^-` the preceding-stage average, `L_j` the applicable ordinary centre (localized strip centre `V_j^{bg,loc}` on the actual strip read and substitution mask, the ordinary global centre otherwise; Y 64125-64133), `V^bg_{j,sq'}` the ordinary test-cube centre, formed on `sq'^{~4}`. The fifth and sixth groups are the ordinary approximate tests `1{|V_j(b) V^bg_{j,sq'}(b)^{-1} - 1| < 2 delta_j}` on the tested bonds `b` of `sq'^{~2}` other than the pivots, with bases in `(Omega_m^{~2} \ Omega_m) cap X` and `(Omega_m \ Lambda_m^~) cap X` (Y 64046-64052; test `chi'_k` as Y 61973). All comparisons are in the common block axial frame of the full read blocks (Y 64075, 64130, 64192-64193; input IN-FRAME').

**Statement BT.** At every point of the complete chart (fixed admitted `omega` with `I(omega) = 1`, `T4 = 1`, and `B` in the approximate ball; the preceding guard kept during these comparisons, Y 64038-64039), every test of the fifth and sixth groups equals 1, provided

  (BT-s) `(C_L + C(L)) delta'_j <= delta_j / 2` and `C_e eps_* (e^{-c R_m} + e^{-c M_2 R_m}) <= delta_j / 4`,

with `C_e` the largest constant of BT.1 and BT.2.

*Steps.*

BT.0 (datum bound for `U_{m,X}`; Y 64087-64106). Each tested holonomy of the joined datum of `X` is within `eps_*` of one: retained level-`j` plaquettes keep their old holonomies; a level-`m` plaquette with a corner in a carried density cube is bounded by that test (T4); the density cubes on `Omega_m^{~4}` cover the plaquettes near the old seam; any other newly tested plaquette has its averaging blocks in the preceding member of level `j` outside the old `Omega_m`, and the exact one-step average of the fine plaquettes (old rows) gives the coarse bound; at the exterior tower a tested holonomy is 1 or a lifted top holonomy of `V_m`. These are datum bounds at the level of the datum, not divided by any fine spacing. This is part (i) of the certificate `I(omega)` of inset-chart 5.2 (input (I3), its proof is row 624, `library/i3-cert.md`). Cited, not redone.

BT.1 (test-cube comparison; Y 64046-64082). The complete reads stay at distance at least `c M R_m` from `dX` (each added test layer has width `M_2 R_m` in level-`m` units; interior bases at least one level-`m` cell from `X^c`, exterior bases in `O_m` within two cells of `Omega_m`; Y 64053-64060). The test-cube box meets neither the prepared seam nor the tower collar at `dX` (Y 64060-64066), and the prospective joined sequence has top level `m` throughout it. On the box the top rows of `U_{m,X}` are `V_m`, so its joined datum for the test-cube localization is the one induced by the lift of `V_m`, whose background is the ordinary test-cube background (Y 64068-64073). By BT.0 the datum is below the ceiling of J1. Apply J1, J2 (`W` = the test-cube box, collar width fixed, distance of the read from the box boundary at least `c M_2 R_m` in level-`m` units, Y 64075-64077) and Lemma AVG as in J3.2-J3.4:

  `|S(b) V^bg_{j,sq'}(b)^{-1} - 1| <= C_e eps_* e^{-c M_2 R_m}`  (BT.1)

with `C_e = 4 C_mu`, `c = delta_0/2` times the fraction of Y 64076. This is Y's display at Y 64078-64081, with the averaging step done by Lemma AVG. It reads no plaquette bound of `U^+` at the artificial bare rim (Y 64083-64086).

BT.2 (annulus comparison; Y 64108-64137). Outer box: `X` inset by a quarter level-`m` cell, rounded on the `M_1`-grid; excluded inner box `(Omega_m^{~2})^c cap X`. On the annulus both backgrounds (`S^-` side and ordinary side) have the same regions, the same determining rows and the same top data on the two boundary bands (the earlier stages alter rows only beyond the inner band; the new gauge draws of the last stage start outside `Omega_m^{~3}`; Y 64115-64123). Joining at level `m` on the outer band and at level `j` on the inner band gives one datum for both. By the two-sequence form of J1-J2 (Y 13414-13425: each against the common joined background, twice the constant) and Lemma AVG, with distance of order `M R_m` to the annulus boundary:

  `|L_j(b) S^-(b)^{-1} - 1| <= C_e eps_* e^{-c R_m}`.  (BT.2)

(Y states the weaker rate `e^{-c R_m}`; the distance gives `e^{-c M R_m}`. Only the weaker one is used.)

BT.3 (`S^-` to `S`; Y 64139-64168). As Y and ypath-port P1-P5: the finer determining set at the prospective averages, then the freed level-`j` rows moved to their actual values; nonpivot increments `< 2 delta'_j` by the approximate collar test; freed pivots by the contour argument of `hi:real-finer-collar-path` (ypath-port P3.4, increment `C_4 delta'_j`); the datum increment is supported in the collar, and the real response bounds, on the common axial reads inside the old `Omega_m`,

  `|S^-(b) S(b)^{-1} - 1| <= C(L) delta'_j`.  (BT.3)

Y does this "after the approximate collar test and before the sharper collar split" (Y 64167-64168). The response bound is input IN-RESP (ypath-port section 4).

BT.4 (the case split; Y 64170-64211). Let `b` be a tested nonpivot of the fifth or sixth group. For unitaries, `|x_1 x_2 ... x_r - 1| <= sum_i |x_i - 1|` (telescoping and unitary invariance). Three cases, exhaustive since a bond has 2, 0 or 1 endpoints in the old `Omega_m`:

- (a) both ends in the old `Omega_m`. The carried or completed fluctuation test gives `|V_j(b) L_j(b)^{-1} - 1| < delta_j` (with the ordinary strip shift on its actual mask; Y 64170-64172). Then
  `|V_j V^bg^{-1} - 1| <= |V_j L_j^{-1} - 1| + |L_j S^{-,-1} - 1| + |S^- S^{-1} - 1| + |S V^bg^{-1} - 1| < delta_j + C_e eps_* e^{-cR_m} + C(L) delta'_j + C_e eps_* e^{-c M_2 R_m} < 2 delta_j` by BT.1-BT.3 and (BT-s).
- (b) neither end in the old `Omega_m`. Then the end outside `Omega_m` is in `K` (Y 64176-64177; geometry input), so the approximate collar test gives `|V_j S^{-1} - 1| < 2 delta'_j`, and `|V_j V^bg^{-1} - 1| < 2 delta'_j + C_e eps_* e^{-c M_2 R_m} < 2 delta_j` by BT.1 and (BT-s) (`2 delta'_j <= delta_j`).
- (c) one end in the old `Omega_m` (a crossing of the old wall, direct graded rule). The full exterior endpoint block lies in `K`, the interior endpoint is in the first stored ordinary strip layer, and the completed strip test gives `|V_j(b) L_j(b)^{-1} - 1| < delta_j` in the original plain coordinate (Y 64184-64189). The centres are compared on the full two blocks by the mean-contour axial reading (Y 64190-64199): the exterior contour of the ordinary frame is determined by the internal bonds of the exterior block, which the direct collar test reads, so `|L_j(b) S(b)^{-1} - 1| <= C_L delta'_j + C_L eps_* e^{-c R_m}` (Y 64200-64203) without a collar bound on the crossing itself. With BT.1: `|V_j V^bg^{-1} - 1| < delta_j + C_L delta'_j + C_L eps_* e^{-cR_m} + C_e eps_* e^{-c M_2 R_m} < 2 delta_j` by (BT-s) (`C_L <= C_e` w.l.o.g.).

In the incident-bond convention a crossing in the mask is case (b) with the direct collar bound in that convention's frame (Y 64209-64211). Checked. Square.

The calculation Y gives as "fit in the remaining `delta_j`": (BT-s) holds at weak coupling, since `delta'_j / delta_j = (log theta_j)^{-(p_0 - p_1)}` (Y 63876, 1115-1118: `delta_j = (A_1/A_0) eps_j`, `delta'_j = g_j A_1 p_1(g_j)`) and `eps_* e^{-c R_m} / delta_j <= (2 eps_* A_0/(A_1 A_0)) e^{u/2 - c u^2} -> 0` by the argument of Lemma J3.5 (`delta_j >= A_1 theta_j^{-1/2} >= (A_1/2) e^{-u/2}`).

Inputs of BT: (I3) (BT.0), IN-FRAME' (Y 64075, 64130, 64192-64193), the geometry (Y 64053-64066, 64108-64123, 64176-64177, 64184-64187), J1-J2 and Lemma AVG (BT.1, BT.2), IN-RESP and ypath-port P3-P5 (BT.3), the carried and completed fluctuation and strip tests (Y 64170-64172, 64186-64189), the approximate collar test (Y 64032-64038).

## 8. (Item 8) Does any step read a plaquette bound on the outer cell layer of `X` at a sharp threshold?

Answer, by the text: **no, in each of (Y-JOIN), (Y-DENS), (Y-CONT), (Y-BELT), (Y-MEAN).** The outer cell layer `E` of `X` (the artificial bare rim) is entered only in two ways: (1) through the existence of the admitted regular orbits and their radius below a fixed ceiling, and (2) through datum holonomies of the joined datum there, which are 1 or lifted top holonomies of `V_m` and are bounded by the carried top density tests (T4), not by the literal final-guard threshold on plaquettes of `U^+`. Place by place:

| Argument | Where its reads lie | Reads in `E`? | What is read there |
|---|---|---|---|
| J1-J3 (Y-JOIN global use) | collar read set `R`, at weighted distance `>= M R_m` from `dX` (J3.1) | the joining collar `Q_a subset X \ O_m` meets `E` | J1 reads the datum tests (H-eps), at the collar the lift of `V_m`: kind (2); J1.1 reads the radius: kind (1). The output is used only on `R`. |
| D (Y-DENS) | halo in `Omega_{j-1} \ Omega_q subset O_m`, two level-`m` cells inside `X` (D.1); density box in layer `j` | no | clauses of `chi_in`, `kappa_x` on the top inset (Y 64707-64708); Hölder in a comparison cube in the inset |
| C, M (Y-CONT, Y-MEAN) | order-`q` blocks in `K` (C.1); double blocks in the old member of level `j` (ypath-port P2(i)) | no | no plaquette bound at all in C; in M only `C_av e` on the double block (kind (1)) |
| BT.0 | the joined datum of `X`, including the exterior tower | yes | tower holonomies 1 or lifted top holonomies, density-cube tests of `V_m` (Y 64095-64106): kind (2). "They do not divide the top plaquette deviation by the square of the fine spacing" (Y 64105-64106). |
| BT.1 | test-cube box, clear of the tower collar at `dX` (Y 64063-64066) | no | "does not require the discarded sharp bound at the artificial bare rim of `X`" (Y 64083-64086) |
| BT.2 | annulus with outer boundary `X` inset by a quarter level-`m` cell | the outer band lies in `E` | the common top data `V_m` on the band (datum, kind (2)) and the regularity of both backgrounds (kind (1)); the output is used at distance of order `M R_m` from the band |
| BT.3 | collar `K` and old `Omega_m` | no | response along the path (ypath-port) |
| BT.4 (c) | crossing of the old wall, exterior block in `K` | no | the strip test and the internal bonds of the exterior block; "without assuming an additional collar bound on the crossing itself" (Y 64196-64198) |

The two places that come nearest are BT.0 and BT.2, which the earlier readings (`prior/ypath-read.md` 5, inset-chart 5.3, inset-chart-check (7)) do not list: BT.2's outer band is inside `E`. What it reads there is datum (kind (2)), so Proposition 5.3 of `inset-chart.md` is not affected. Its premise for BT.2 is that the `V_m` tests on the outer band are within `eps_*` of one, which is T4 with the covering of the outer six cells by carried density cubes (Y 76692-76697, used in inset-chart Lemma 5.2). That is the statement Proposition 5.3 needs.

## 9. Inputs from outside the argument (cited, not proved here)

| Input | Used in | Content | Y lines | Status in Y at those lines |
|---|---|---|---|---|
| IN-IMP | J1.1 | regularity improvement: radius `B_3 eps_1` | 13293-13295 | stated, cited to the background theorem |
| IN-RES | J1.2, J1' | `mb:restriction-identity`: restriction is critical at its induced datum | 12920-12955 | proved there, given regular uniqueness |
| IN-AV | J1.3, J3.4 | `mb:uniform-real-average`: `|dM^n U - 1| <= 2 eps L^{2(n-k)}`, regular mean branches | 10976-11001 | proved (curvature recursion) |
| IN-RIG | J1.4 | `mb:rigidity-defect`, `mb:rigidity-sum`: coefficient 1 on the coarse difference, `C_L varpi` per level | 10833-10885 | proved from `mb:finite-stokes`, `mb:mean-versus-comb` |
| IN-BG | J1', D, BT | `bgc:proper-background`: existence, radius `C_B eps`, uniqueness at `a_0` | 35634-35646 (proof from 35651) | proposition with proof |
| IN-POLY | J1' | the joined response polydisc of radius `r_B`; the real path stays in the common admitted datum ball | 13345-13350; 13244 ("Assume it stays in the common admitted datum ball") | **assumed at these lines**; `r_B` is named only at 13345 |
| IN-PR | J2.1 | weighted pointwise kernels of the coupled inverse; point response `B_5 e^{-delta_0 d}` for all declared readouts | 13155-13163; 25741 ff.; 16080-16090 | **assumed** ("Assume the actual coupled inverse has weighted pointwise kernels", 13155); Y lists these as response inputs of A3 (16084-16085) |
| IN-ROW | J2.1 | row sum at rate `delta_0/2` uniformly bounded | 13165-13178, 13376-13377 | the Schur premise of `mb:extended-source` is an input |
| IN-AVX | J3.3 | one-step averaging expansion (A4)-(A5) | Balaban CMP 98 Prop. 3; rebuilt as `library/b98.md` Lemma 8 | b98 Lemma 8 is a hand proof by Codex, not yet checked by another provider |
| IN-FRAME, IN-FRAME' | J3.4, BT | coordinates compared in the common node / block axial frame, so that their ratio is the double-bar average `S_j` | 65028-65031, 13362-13366, 64075, 64130, 64192-64193 | stated as the convention |
| (H-J), (H-R), `C_st` | J3 | geometry of the joining collar at `dX`, clearance and spacing of the read set | 65026-65055, 63760-63766 | stated with reasons |
| (I3) | BT.0, (H-eps) | datum bound `Ce_q` on the entering support (certificate `I`) | 64087-64106, 65417-65563, 134201-134205 | proved in Y on the entering support; port is row 624 |
| `G(omega) = 1`, T3, T4 | D, BT | the inset guard clauses at the fixed prospective orbit | 63876, 64234-64313 | the guard (inset-chart 5.4) |
| (E1), IN-RESP | D.5, BT.3 | the response along the collar path | 64979-65014 | ported in `library/ypath-port.md` P5 (IN-RESP open there) |
| IN-HOL | D.4 | local regularity, Hölder bound of the curl | 15778-15812, 11901-11917 | proved under their analytic inputs |
| IN-COMP | D.4 | compressed range `q >= m - O(log R_m)`, `m >= R_m` | 64764-64765, 63776-63778 | stated |
| IN-DBOX | D.5 | density localization box, three-small-cube margin, error `C eps_* e^{-c R_j}` | 64776-64786 | stated, by the joined comparison |
| IN-AXF, IN-MC | C | trivial mean contours in the prospective axial frame; bounded derivative of the mean contour map | 64799-64808; 3714 | stated; IN-MEAN proved at 3714 |
| (FD), (RC) | J3.5, D.2, D.4, BT | frame drift and `R_m >= (log(theta_m - c_5))^r` | 1103-1111, 4583 | definitions |

## 10. For the consumer (`library/inset-chart.md` 5.3)

- (Y-JOIN) as used in inset-chart 5.3 and Proposition 5.5 (T6): hypotheses part (ii) of `I` (global datum within `eps_1`) and the geometry floors, as the note says; add (J1-s), (J1-r) on `eps_1`, the fixed collar width `mu` with `4 mu <= 2 M R_m`, and the conditions of Lemma J3.5 for `o(delta'_j)`. Conclusion J3 with `C = 4 C_mu`, `c = delta_0/2`.
- (Y-DENS), (Y-CONT), (Y-BELT), (Y-MEAN): their hypotheses on `omega` are `G(omega) = 1`, T4, `I(omega) = 1` and the admitted `U^+` with radius below the ceiling, as inset-chart 5.3 and Proposition 5.5 say; the smallness conditions are (D-s), (C-s), (BT-s) and those of ypath-port (S-e), (S-d), (S-r), all of the form "`delta'_j/eps_j` small and `eps_* e^{-c R}` small against `delta_j`", which hold at weak coupling by Lemma J3.5 and its variants.
- Proposition 5.3: confirmed for these arguments (section 8), with BT.0 and BT.2 added to its evidence list.
