lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T15:53Z

# yjoin-port: the joined-datum comparison of Y and four shorter arguments (registry row Y-PATH, FINISH row 627)

Provenance: Claude Opus 5.5 (high), Mac mini worker 2, commit fbf9ba1cd, 2026-11-10. A port, not an audit. Source Y = YM4_1400.tex of Sussman and Alpoge (authors of the text with Claude and Codex), repository ethanwsussman/Yang--Mills-LLM-experiment at 2bc0658f91d2, fetched to a private scratch copy (136,637 lines); 'Y n' = line n. Everything taken from Y is credited to Y and is `unchecked` until another provider checks this port.

(in progress; sections are written as they are checked)

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
