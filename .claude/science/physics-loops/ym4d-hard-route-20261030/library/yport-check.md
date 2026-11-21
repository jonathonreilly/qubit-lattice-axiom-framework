lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T00:45Z

# yport-check: line-by-line check of ypath-port (row 626) and yjoin-port (row 627)

Provenance: Claude Fable 5.2 (medium), Mac mini worker 1, commit 2759e806f, 2026-11-10. A check, not an audit. The two ports were written by Claude Opus 5.5 (high); this check is by a different model of the same provider. No numeric job was run. Source Y = `YM4_1400.tex` of Sussman and Alpoge (with Claude and Codex as authors of their text), commit 2bc0658f91d2, 136,637 lines; "Y n" is line n. Every Y statement is theirs.

## 0. Verdict

**No item FAILS.** No inequality of either port was found false. Six items need a repair of text (a missing smallness condition, a wrong reason with a right conclusion, or a scope statement); each repair is written below and none changes a conclusion or a constant that a consumer reads, except C_2 if repair R1b is preferred to R1a.

| Item | Verdict |
|---|---|
| (1) P3.1 | HOLDS WITH REPAIR (R1, R2) |
| (1) P3.2 | HOLDS |
| (1) P3.4 | HOLDS |
| (1) P5.3 | HOLDS |
| (1) P7.1 | HOLDS |
| (2) order of dependence, Decisions 1 and 2 | HOLDS; no cycle; list in section 2 |
| (3) care point on (E2) | HOLDS WITH REPAIR (R3: the constant fixed before `M` is the rate `delta_0`, Y 17399 and 63873; the port's reason "a is of order 1/M_1" is not Y's) |
| (4) J1 | HOLDS WITH REPAIR (R4, step J1.5) |
| (4) J2 | HOLDS (one wording precision in J2.2) |
| (5) Lemma AVG | HOLDS (strict inequality `2 tau < c_3`); it is Y's own `prop:averaging-1a-1-6`, Y 3785-3800, which the port does not cite |
| (5) (FD), (RC), Lemma J3.5 | HOLDS |
| (5) stage window | HOLDS: Y does not state the window at Y 65062-65067; it is at Y 63684, 63836, 1121, 1182, and is named at Y 64765-64766 |
| (6) Y-DENS | HOLDS WITH REPAIR (R5: scope of (E1)) |
| (6) Y-CONT | HOLDS WITH REPAIR (R6: (C-s)) |
| (6) Y-BELT | HOLDS |
| (6) Y-MEAN | HOLDS |
| (7) section 8 against Proposition 5.3 | HOLDS, with one precision (J1.3 reads plaquettes of `U^+` in the joining collar at the regularity radius, kind (1)) |
| (8) IN-RESP, IN-POLY, IN-PR | Y states and proves statements of this form at another place (`dnr:response`, `dnr:physical`, `dnr:coupled`, Y 41183-41232, 41391-41409, 41506-41525); Y does not cite them at the lines of use, and the match of constants and data is not written. They stay assumptions until that match is ported |
| (8) IN-AVX | Y states it (`prop:averaging-1a-1-5`, Y 3766-3783) with a proof by sketch (Y 4528); the consequence the port needs is Y's `prop:averaging-1a-1-6` (Y 3785-3800, proof Y 4528-4536). Not an assumption in Y; `library/b98.md` Lemma 8 is the hand rebuild and still waits for its check |
| (9) twelve quoted passages | all twelve texts agree with Y; five line citations are off by 2 to 14 lines (list in section 9) |

What stays open: the match of IN-RESP, IN-POLY, IN-PR to Y's `dnr` propositions (a port, not done here); the hypothesis IN-FRAME of J3 (a reading of two Y sentences, Y 65029-65032); the other inputs of the two ports' input tables, which I did not check beyond the lines cited.

## Repo search

- The two ports and `library/prior/ypath-read.md`: read. `library/inset-chart.md` 5.3 and Proposition 5.3: read. `library/b98.md` statement (c), (d), (A3)-(A5) and Lemma 8: read.
- `library/open-registry.md` row Y-PATH names this row as the check. `library/open-core.md` and the FINISH rows: no other row checks the two ports (rows 617, 622, 623, 626, 627 are the consumer, its check, the reading and the two ports). This row attacks no open lemma.

## 1. Item (1): the five calculated points of the path port

Notation as in ypath-port section 2. `d` is the angle on the unit 3-sphere SU(2), `|g h^{-1} - 1| = 2 sin(d(g,h)/2)`.

**P3.1 (anchors).** Replaces Y 64929-64940 ("Sweeping the fixed contour stencils shows that their transports lie within `C(L)e` of the central transport, and hence within `C(L)e` of `W` by the regular averaging formula. Changing the nonpivots by `2 delta'_j` moves each literal transport by at most `C(L) delta'_j`. The averaged end contours have the same bound ... Thus `d(H_a,W) <= C(L)(e + delta'_j)` in either formula").

- Step (1), first part. IN-TRANS (Y 3717) gives `(1 + varpi)^{m(m-1)/2} - 1`, and `m(m-1)/2 <= m_L^2`. `(1+x)^N - 1 <= e^{Nx} - 1 <= 2Nx` for `Nx <= 1`: holds (`e^t - 1 <= 2t` on `[0,1]`). With (N): `d <= (pi/2) 2 m_L^2 C_av e = pi m_L^2 C_av e`. Holds.
- Step (1), the mean. The port writes: "Geodesic balls of radius below pi/2 on the 3-sphere are convex, and the mean is the unique zero ... so `d(mean_i T_i, T_1) <= max_i d(T_i, T_1)`". The conclusion is true, but convexity of the ball does not by itself give it; a proof assistant needs the next lemma. **Repair R1a.** *Lemma.* Let `T_1, ..., T_n` in SU(2), `V` in SU(2) with `theta_i := d(T_i, V) < pi/2` and `sum_i log(T_i V^{-1}) = 0` (Y's mean, Y 3714, where `|T_i V^{-1} - 1| < 1`, so `theta_i < pi/3`). Put `r := max_i d(T_i, T_1) < pi/2`. Then `d(V, T_1) <= r`. *Proof.* In the unit quaternions, `T_i V^{-1} = cos theta_i + u_i sin theta_i` and `log(T_i V^{-1}) = theta_i u_i`. Multiply `sum_i theta_i u_i = 0` on the right by `V` and use `u_i V = (T_i - cos theta_i V)/sin theta_i` (for `theta_i = 0` the term is absent): `sum_i c_i T_i = (sum_i c_i cos theta_i) V` with `c_i = theta_i / sin theta_i > 0`. Since `cos theta_i > 0`, `V = sum_i a_i T_i` with `a_i > 0`. Then `1 = |V| <= sum_i a_i`, and `<V, T_1> = sum_i a_i <T_i, T_1> >= cos r sum_i a_i >= cos r`. So `d(V, T_1) <= r`. Square. The hypothesis `r < pi/2` is `pi m_L^2 C_av e < pi/2`, which (S-e) gives.
  (Alternative R1b, if R1a is not wanted: the mean of the constant family is its member, so IN-MEAN gives `d(mean_i T_i, T_1) <= C_mean max_i d(T_i, T_1)`; then `C_2 = 2(1 + 2 C_mean) pi m_L^2 C_av + (1 + 2 C_mean) pi m_L`.)
- Step (1), last line: `d(ABC, A'BC') <= d(A,A') + d(C,C')` by bi-invariance; total `3 pi m_L^2 C_av e`. Holds.
- Step (2): `exp(X(q^+)) = W (q^+)^{-1}` with `|X| <= pi(1 - L^{-3}) < pi` (Y 75211-75212), so `d(W, q^+) = |X(q^+)| <= sum_r alpha_r d(H_r^+, q^+) <= 3 pi m_L^2 C_av e`. Holds. That `S` on `D(c)` is on the regular branch is IN-AV (Y 10999-11001).
- Step (3): telescoping with bi-invariance gives `pi m_L delta'_j` for a literal anchor; `(1 + 2 C_mean) pi m_L delta'_j` for a regular one. Holds. On the literal branch of the actual field, compare with the literal anchors of `S`, which are within `pi m_L^2 C_av e` of `q^+`, hence within `4 pi m_L^2 C_av e` of `W`; the bound `6 pi ...` covers it.
- **Repair R2 (missing smallness condition).** IN-MEAN gives the Lipschitz constant `C_mean` only on a chart of some radius `rho_mean` (Y 3714: "families ... of small diameter ..., where the radii do not depend on n"). The port never names it. Add to (S-e): `2 pi m_L^2 C_av e_* <= rho_mean / 2`; add to (S-d): `2 pi m_L delta'_j <= rho_mean / 2`. Then the end families of `S` and of the actual field, and the segment between them, lie in the chart. Y's words are "each stays in its regular mean chart" (Y 64938-64939).

Sum: `d(H_a, W) <= C_2 (e + delta'_j)`. HOLDS WITH REPAIR.

**P3.2 (coarse pivot bound).** Replaces Y 64941-64951 (the display `d(q,W) <= (1 - L^{-3})(d(q,W) + C(L)(e + delta'_j))` and "This puts the actual pivot within `C(L)(e + delta'_j)` of the induced pivot, since the other bonds of the corridor are already close").

- `d(q,W) = |X|` since `|X| < pi`; `|X| <= sum alpha_r d(H_r, q)` since `|log(H_r q^{-1})| = d(H_r, q)`; triangle; `L^{-3} d(q,W) <= (1 - L^{-3}) C_2 (e + delta'_j)`. Holds.
- `d(q, q^+) <= (L^3 - 1) C_2 (e + delta'_j) + 3 pi m_L^2 C_av e <= L^3 C_2 (e + delta'_j)`, since `3 pi m_L^2 C_av <= C_2`. Holds.
- `b = P_-^{-1} q P_+^{-1}`; the corridor has `L` bonds, `L - 1` of them nonpivots; `d(b, b^+) <= L^3 C_2 (e + delta'_j) + (L - 1) pi delta'_j <= C_3 (e + delta'_j)`. Holds.

HOLDS.

**P3.4 (one-row contraction).** Replaces Y 64953-64958 ("In a fixed double-block gauge of the induced field, the derivative in the middle bond is then close to its flat value `L^{-3} I`. The regular one-row inverse gives the sharper bound `C(L) delta'_j` for the pivot increment").

- `D_b T_n = I - L^3 D_b G_n`, norm at most `L^3 (L^{-3}/2) = 1/2`. Holds.
- `T_n(b^+) - b^+ = -L^3 (G_n(b^+) - G_S(b^+))`, since `W = G_S(b^+)` (P2(iii)); norm at most `L^3 Lambda pi delta'_j <= r_1/2` by (S-d). The segment from `S` to `n` lies in the `r_2`-ball since `pi delta'_j <= r_2`. Holds.
- Self-map of the closed `r_1`-ball: `|T_n(b) - b^+| <= r_1/2 + r_1/2`. Fixed point unique. Lipschitz: `|Phi(n) - Phi(n')| <= (1/2)|Phi(n) - Phi(n')| + L^3 Lambda |n - n'|`. Holds.
- Every solution of `F(q) = W` is in the ball by P3.2 with (S-e), (S-d) (`C_3 (e + delta'_j) <= r_1`), and is on the regular branch by P3.3, where `F = G_n`. So the pivot is `Phi(n)` and `d(b, b^+) <= 2 L^3 Lambda pi delta'_j = C_4 delta'_j`. Holds.
- The flat value: Y 75238-75241, `B(w) dF_q = H(w) - sum_i alpha_i H(v_i)`; at `v_i = 0`, `H = 1`, `B = 1`, `dF_q = 1 - (1 - L^{-3}) = L^{-3}`. Holds.

HOLDS. The radii `r_1, r_2` and `Lambda` are the port's names for Y's "uniform on the small one-row chart" (Y 64963); they are inputs (IN-ROW).

**P5.3 (scaled plaquette estimate).** Replaces Y 65006-65009 ("The scaled plaquette estimate on this complete stencil gives the following bound for the difference of defects").

- Backward link: `U'(b)^{-1} = e^{-i U(b)^{-1} H(b) U(b)} U(b)^{-1}`. Holds.
- Induction `U'(l_1) ... U'(l_k) = e^{i h_1} ... e^{i h_k} T_{k+1}`. Holds. `T_5 = dU(p)`.
- `h_1 = H_mu(x)`, `h_2 = U_mu(x) H_nu(x+mu) U_mu(x)^{-1}`, `T_3 U_mu(x+nu)^{-1} = dU(p) U_nu(x)`, so `h_3 = -Ad_{dU(p)}[U_nu(x) H_mu(x+nu) U_nu(x)^{-1}]`; `T_4 = dU(p) U_nu(x)`, so `h_4 = -Ad_{dU(p)} H_nu(x)`. Holds.
- Sum: `h_1 + h_2 = H_mu(x) + nabla_mu H_nu(x) + H_nu(x)`; `h_3 + h_4 = -nabla_nu H_mu(x) - H_mu(x) - H_nu(x) + R`. So the sum is `nabla_mu H_nu - nabla_nu H_mu + R`. Holds.
- `|g Z g^{-1} - Z| = |(g-1) Z - Z (g-1)| <= 2 |g-1| |Z|`; `|R| <= 4 |dU(p) - 1| ||H||_p`. Holds.
- `|prod e^{i h_k} - 1 - i sum h_k| <= e^s - 1 - s <= s^2` for `s <= 1` (`e^s - 1 - s <= (e - 2) s^2`), `s <= 4 ||H||_p`. Holds.

HOLDS. In P5.4 the use needs `4 C_5 delta'_j <= 1`; (S-d) has `C_5' delta'_j <= 1/4`, so one needs `C_5 <= C_5'`, that is `S(a) <= S(a/2)`. This is true for the suprema and should be said ("w.l.o.g. `S(a/2) >= S(a)`"). The total `2 + 4 + 4 = 10` holds.

**P7.1 (ratio of thresholds).** Replaces Y 63876 ("the thresholds of two levels may differ by `eps_j/eps_i <= C(1 + (j-i)^{1/2})`, the bound valid for every pair of levels") and Y 64246-64247.

- IN-FR is Y 4583: `-C <= x_i - x_j <= C(j - i)` for `i <= j <= k`. The port's form agrees.
- `x_i / x_j <= 1 + C_fr (j-i)` (uses `x_j >= 1`); `sqrt(1 + C n) <= (1 + sqrt C)(1 + sqrt n)`. Holds.
- `log x_j <= log x_i + C_fr / x_i`; `(1 + t)^{p_0} <= e^{p_0 t} <= 2` when `x_i log x_i >= C_fr p_0 / ln 2`. Holds (needs `p_0 >= 0` and `x_i > 1`; both hold, Y 1103, 1115).

HOLDS. The fits in P6 and P7.3 were also checked: `(1 + sqrt n) <= 2^n`; `c(i,j) - c(i,j+1) = beta_s 2^{-(j-i+2)}`; `4 C_L' C_eps (delta'_j/eps_j) 2^{-n} <= beta_s 2^{-(n+2)}` is (S-r). All hold.

## 2. Item (2): order of dependence

Decision 1 (the path reads the promoted-datum bound only through `U^+` and its radius): confirmed at Y 64863-64869, 64976-64977. Decision 2 ((E2) does not use the removal of the preceding guard): confirmed; (E2) at Y 64234-64252 is a bound on the response, and Y 64265-64268 uses it as a premise. Y 65488-65491 says the same from the other side: "To remove the preceding guard on an enlarged support, use the separate comparison in `hi:preceding-guard-support`".

The port's list is within one transition. Over all transitions the order is lexicographic in (stage, step); written as a list:

1. Stage zero: the first regularity guard on the untouched incoming datum (Y 134198-134200).
2. For `j = k_flat, ..., m - 1` in increasing order, with `q = j + 1`:
   - (a_j) promoted-datum bound `C e_q` on the entering support, from the tests carried at that moment; the preceding guard is a carried factor here, not a removed one (Y 65417-65491, 134201-134205).
   - (b_j) the path and the ball, from (a_j) through `U^+` and its radius only (Y 64860-64977).
   - (c_j) (E1), from (b_j) and IN-RESP (Y 64979-65014).
   - (d_j) (E3) and (E2), from the decaying form of (c_j), G-W and threshold arithmetic (Y 64437-64455, 64234-64252).
   - (e_j) removal of the preceding guard on the enlarged support, from (c_j), (d_j) and the prospective guard at the fixed datum (Y 64221-64463).
3. (a_{j+1}) may read (e_j) ("After removal and before integration the collar assignment uses the new positive stage test", Y 65462-65465). No step reads a later step of the same stage or any step of a later stage.

No cycle. HOLDS.

## 3. Item (3): the care point on (E2)

What must be fixed before `M`: the response rate `a`, with `C_R` and the top sums `S(a)`, `S(a/2)`.

- Y's rate is `delta_0`: the error term is `C delta'_j e^{-delta_0 dist} eta_i^2 <= C (delta'_j/eps_j)(1 + (j-i)^{1/2}) e^{-c(M/M_1)(j-i)} eps_i eta_i^2` (Y 63873).
- Y's order of constants (Y 17399): "First comes `L`, and with it ... the rates `delta_0`, `delta_*`, `delta'`, and the ceiling ... Next come `M_1` and `R_1 M_1` ... Then comes `kappa-bar` ... The final choices are `M` and the field strengths of the construction, taken so small that `O(LM) alpha_0` is below the ceiling." And: "every constant, rate and ceiling ... is independent of `k`, `K`, `l`, of the sequence ..., and also of `M_1, R_1` once these are large enough."
- So `delta_0` is fixed with `L`, before `M_1`, `R_1` and before `M`. The ceiling comes after `M` (Y 4391: "`M alpha_0` ... lies below a number that depends only on `L`"), as the port says.
- The shell width: "For each intervening layer the path crosses a width of at least a fixed multiple of `M` in its own units" (Y 64448-64450). This is the port's G-W.

**Repair R3.** In P6 the port says "in Y the response rate `a` is of order `1/M_1` (walk cubes of side `M_1`), so `a w M/2 = c M/M_1`". Y does not say this: Y's rate is `delta_0`, which depends on `L` alone, and the factor `M/M_1` at Y 63873 bounds `delta_0 dist` from below. Replace the sentence by: "`kappa = a w M/2` with `a = delta_0` (Y 63873) fixed with `L` (Y 17399); Y's `c(M/M_1)(j-i)` is a lower bound for `delta_0 dist`, and `M_1` is fixed before `M`." Replace the citation "Y 16100-16106" in the remark of P7 by Y 17399 (Y 16104 only defines separated sequences). The conclusion (`kappa >= 2 ln 2` by taking `M` large, after `a`, `C_R`, `S`) is unchanged. HOLDS WITH REPAIR.

## 4. Item (4): J1 and J2, each constant

**J1.** `B_3 eps_1 = eps` (Y 13296-13297). `2 eps L^{2(q-j)}` (Y 13304-13307, from `mb:uniform-real-average`, Y 10990-10995, with `k = j`). Recursion (J1.4a): `mb:rigidity-defect` (Y 10876-10884) has `C_L {varpi(U) + varpi(U_0)}`; the port drops the `U_0` term because the reconstruction error `|U~_0(b) - M(U_0)(c)|` is exactly 0 for the face lift. I checked this: inside one ambient `j`-block the lift is 1, so the block transports are 1 and `U~_0(b) = U_0(b)`; if `c` crosses a `j`-block face then `b` crosses the same face and both equal `V_j` of that face, and the one-step average of the lift is the lift (Y 13076-13083). So the `U_0` term is absent. Note that `varpi(U_0)` itself is not 0 (plaquettes at the edges of the `j`-blocks carry the coarse defect); the port's argument rightly goes through the reconstruction error and not through `varpi(U_0)`. Sum: `sum_{t>=1} L^{-2t} = 1/(L^2-1)`; result `2 C_lift eps/(L^2-1)`, Y's value (Y 13317-13320). (L3): `phi <= pi/3`, `phi/(2 sin(phi/2)) <= (pi/3)/1`; holds. Constant `2 pi C_lift B_3 eps_1/(3(L^2-1))`: agrees with Y 13341-13344.

**Repair R4 (J1.5, case (ii)).** The port writes "Both ends of a row of level `n` lie in `Omega_n`". This is false for an outward row: its second end is outside `Omega_n` (Y 16104: rows have "one end point in `L_j` and the other end point either in `L_j` ... or, when `j >= 1`, outside `Omega_j`"). Y's reason is separation ("Separation would put its end in `Q_a` inside `Omega_{j_a+1}`", Y 13329-13330). Replace by: "The layer end of a row of level `n` lies in `Omega_n`. Its other end is at sup distance `xi_n` from it. By separation, `dist_inf(Omega_{n-1}^c, Omega_n) > R_1 M_1 xi_{n-1} >= L xi_{n-1} = xi_n` (Y 16104-16107, `R_1 >= L`), so the other end lies in `Omega_{n-1}`. Since `n - 1 >= j_a + 1`, both ends lie in `Omega_{j_a+1}`, and the end in `Q_a subset F_a` cannot, by (C1)." The conclusion is unchanged. That the layer end lies in `W` holds because rows of the joined set lie in its first member `Omega_0 cap W` (Y 13017). HOLDS WITH REPAIR.

**J2.** J2.1: splitting the rate, `C_row` at rate `delta_0/2` (Y 13370-13372). Holds. J2.2: `|z - z'|_1 <= 4 |z - z'|_inf <= 12 s_a`, weighted length `12 mu` (Y 13372-13376). Holds; the last parenthesis of the port ("absorbed by taking the segment between lattice points") is better replaced by: "take any monotone lattice staircase in the coordinate box of `z` and `z'`, stopped at its first exit from `A_a`; each of its points `w` has `|w - z'|_inf <= 3 s_a`, so it is outside `A_a^{(-4)}`, hence in `F_a`, in the layer `j_a`." J2.3: stopping at the boundary of `W^{(-3)}`; `W \ W^{(-3)}` is covered by the `Q_a`. Holds. J2.4: `e^{(delta_0/2) 12 mu} = e^{6 mu delta_0}` (Y 13396). `C_mu = e^{6 mu delta_0} B_5 C_row 2 pi C_lift B_3/(3(L^2-1))`. Holds. HOLDS.

## 5. Item (5): J3

**Lemma AVG.** Recursion `a_{n+1} <= L(1 + K_lin alpha_n) a_n + C_1 L^2 a_n^2` from b98 (A4) and (A5): in (A5) the main term is `sum_x w t_x` with `w = L^{-(d+1)}`, `|t_x| <= L |A'|`, so it is at most `|A'|`; the other four coefficients vanish at `Y = Y_x = 0` (b98 lines 84-100, 384-388). `b_{n+1} <= b_n (1 + K_lin alpha_n + C_1 L^{n+1} b_n)`: holds. Induction `b_n <= 2 b_0`: `sum_{i<=n} L^{i+1} <= 2 L^{n+1} <= 2 L^j`; exponent at most `K_lin sigma + 4 C_1 tau <= ln 2`. Holds. One precision: (A4) asks `|A'| < alpha_1 <= c_3` strictly, so write `2 tau < c_3`.

The port presents Lemma AVG as its own calculation of Y's "followed by averaging on these blocks". **Y has this statement:** `prop:averaging-1a-1-6` (Y 3785-3800), `M^n(e^{i eta_k A} U_0) = (e^{i a_n} M^n U_0)^{v_n}`, `|a_n| <= 2 L^n eta_k sup|A|`, with the same constant 2; its proof at Y 4528-4536 is the same recursion, `t_{n+1} <= t_n (1 + C varpi_n + C L^n eta_k t_n)`, `sum_{n<k} L^n eta_k <= 2 L^{-1}`. The port should cite it. Lemma AVG agrees with it. HOLDS.

**J3.1-J3.4.** `dist_inf(R, X^c) >= 2 a_m - C_st L^m >= a_m`; weighted length at least `a_m/L^m = M R_m` (Y 65054-65056); `tau = C_mu eps_* e^{-delta_0 M R_m/2}`; `sigma <= 2 B_3 eps_*/(L^2-1)`; final bound `4 tau`. Each holds given (H-J), (H-R), (IN-FRAME). (IN-FRAME) is the port's reading of Y 65029-65032; Y does not prove at those lines that the node factors of the two responses cancel in the ratio. It stays a hypothesis.

**(FD).** Y 1103-1107: `lambda_low (j-i) - c_5 <= theta_i - theta_j <= B_bar (j-i)` for `i <= j`. The port's form and its use with `(j, m)` agree. **(RC).** `R_m = R(min_{i<=m} theta_i)`, `R(y)` the least power of `L` not below `(log y)^r` (Y 1108-1111); `theta_i >= theta_m - c_5` needs `lambda_low >= 0`, which the port should state; `R_m <= L (log theta_m)^r` holds since `(log y)^r >= 1`.

**Lemma J3.5.** `theta_j <= 2 theta_m`; `delta'_j >= (A_1/2) e^{-u/2}`; `R_m >= u^2`; ratio at most `(8 C_mu eps_*/A_1) e^{u/2 - cMu^2} <= (8 C_mu eps_*/A_1) e^{-cMu^2/2}`; `log theta_j <= 3u` since `u >= log 2`. Each line holds. HOLDS.

**The stage window.** The finding holds. At the place of use Y writes only: "The last equality uses the frame drift and `R_m >= (log(theta_m - c_5))^r`, with `r >= 2`" (Y 65062-65064). The window `m - j <= N_m = R_m` is not stated there. Y has it at: Y 63684 (`k_flat = k - N_k >= 1`), Y 63836 ("Stages: for `j = k_flat, ..., k - 1`"), Y 1121 ("The waiting depth is `N_j = R_j`"), Y 1182 (`t_flat = t - N_t >= 0`). In the Y-DENS argument Y does name it: "With the frame comparison in the waiting window" (Y 64765-64766). Without it the equality is not derivable: `theta_i = theta_m + B_bar (m - i)` is a frame when `lambda_low <= B_bar`, and then `delta'_j` falls below `e^{-cMR_m}` for `m - j` large. HOLDS.

## 6. Item (6): Y-DENS, Y-CONT, Y-BELT, Y-MEAN

**Y-DENS (D).** D.1 as Y 64699-64716. D.2: `eps(theta)` decreases for `log theta > 2 p_0`; `theta_q >= theta_j - B_bar`; holds. D.3: (a) `(1 - 3 beta_s/4) T_d` (Y 64719-64721); (b) `2 L^{-2} T_d <= (2/25) T_d`; (c) as Y 64726-64733. Holds. D.4a: `2 max{3, L_flat^2} L^{-2} <= 1/2` from `L_flat < L/2`, `L >= 5`. Holds. D.4b: `E_H/T_d = C_H eps_* L^{-2} L^{-alpha q}/eps_j`, `E_2/T_d <= C_2' L^{-q}/eps_j`, `q >= R_m/2`, `eps_j >= (A_0/2) e^{-u/2}`, `R_m >= u^2`; holds (uses `alpha <= 1` and `p_0 >= 0`). The comparison of group defects needs no constant: `|g - 1| = 2 sin(phi/2)` is 1-Lipschitz in `phi`. D.6: reserves `(3 beta_s/4) T_d` and `T_d/4`; `beta_s <= 1/3` is enough for the first to be the smaller (the port writes `beta_s < 1/4`, which I did not find stated in Y; only `beta_s <= 1/3` is needed). Fit (D-s): holds.

**Repair R5 (D.5, scope of (E1)).** ypath-port P5.4 states (E1) "for every bare plaquette `p` of the old level-`j` carriers at the new prepared face". D.5 applies it to the halo plaquettes of the density box, which are not at that face. The proof of P5.1 gives `xi_y |H(y)|, xi_y^2 |nabla H(y)| <= 8 S(a) C_R C_4 delta'_j` at every top `y`, so (E1) holds, with the same `C_L`, at every bare plaquette whose stencil has local scale at least `xi_j` in the preceding sequence and where `|dU^+(p) - 1| <= xi_j^{-2}`. Y places the density box there: "the whole density box is in the old prepared layer `j`" (Y 64714-64715), and uses the cost `C_L delta'_j L^{-2j}` (Y 64772-64774). State (E1) in P5.4 in this form. HOLDS WITH REPAIR.

**Y-CONT (C).** C.1-C.3 as Y 64791-64801. C.4: holds. **Repair R6.** (C-s) is written with `C_mc pi`, but after the change of stage centre the port's own constant is `C_mc pi (1 + C(L))`, and the derivative bound is used on a chart whose radius is on the input side. Replace (C-s) by: `pi (1 + C(L)) delta'_j <= rho_mc` and `C_mc pi (1 + C(L)) delta'_j < eps_j`. HOLDS WITH REPAIR.

**Y-BELT (BT).** BT.0-BT.3 are citations of Y 64087-64168 and of J1, J2, Lemma AVG and the path port; the statements agree with Y's displays (Y 64078-64081, 64134-64137, 64165-64166). BT.4: (a) `delta_j + delta_j/2 + delta_j/4 < 2 delta_j`; (b) `2 delta'_j + delta_j/4 < 2 delta_j` (the port's `2 delta'_j <= delta_j` needs `C_L + C(L) >= 1`, w.l.o.g.); (c) `delta_j + delta_j/2 + delta_j/4 < 2 delta_j` with `C_L <= C_e`. The three cases are exhaustive. HOLDS.

**Y-MEAN (M).** (i) is P3.1-P3.4 (item (1)); (ii) is C.4 with `rho_mc`. HOLDS, with R1, R2 and R6.

## 7. Item (7): section 8 of the join port against Proposition 5.3

Proposition 5.3 of `library/inset-chart.md` says: on the outer cell layer `E` of `X` the backgrounds enter only (1) through their existence as regular critical orbits with radius below a fixed ceiling, and (2) through the values of their top rows `V_m`; no threshold of the literal final guard on a plaquette of `E` is used.

Section 8 agrees with it, row by row. I checked the two places it adds: BT.0 (Y 64087-64106: "At the exterior tower a tested holonomy is either the identity or the lifted top holonomy ... They do not divide the top plaquette deviation by the square of the fine spacing") and BT.2 (Y 64108-64137: outer box "`X` inset by a quarter of a level-`m` cell"; the same "top data used on its two boundary bands"). Both read datum values, kind (2).

One precision, which the table of section 8 leaves implicit. J1.3 does read plaquettes of `U^+` and of its averages inside the wide collar `Q_a`, and for the joining collar at `dX` (J3) and for the outer band of BT.2 this collar lies in `E`. The bound read is `2 B_3 eps_1 L^{2(q-j)}`, which comes from the radius `B_3 eps_1` of the orbit (regularity improvement, IN-IMP, Y 13296-13297), not from a guard. So it is kind (1): a bound `C eps_*` at the scale of the layer, not the sharp threshold. With this said, section 8 gives what Proposition 5.3 needs. HOLDS.

## 8. Item (8): the four open inputs

I searched Y for each. I read the statements at the lines given, not their proofs.

- **(IN-RESP)** the real Landau response, used at Y 64979-64986 with no citation. Y proves a statement of this form at `dnr:response` (Y 41183-41205): for `|B'| < r = c b^{-8}` a unique solution, holomorphic, with `||H||_{1,w} <= C b |B'|_w` and `||delta H||_{1,w} <= C b |delta B'|_w`, where `||A||_{1,w} = sup_y w(y) max{xi_y |A|_y, xi_y^2 |nabla A|_y}` for every weight with `w(y)/w(z) <= e^{theta d(y,z)}` (Y 40735-40743). With `w(y) = e^{theta d(y, y_c)}` the difference bound is the point response with rate `theta` and constant `C b`. `dnr:physical` (Y 41391-41409) identifies it: "Every sufficiently small critical field on this slice is this response at its own reduced datum." The constants are "independent of depth, fine mesh, compatible volume, and admitted region shape" and "uniform in every larger admissible final tile size and separation" (Y 40701-40712), which is the independence of `M` that item (3) needs. Not written in Y: that the response of Y 64979 is this one, that its "plain row logarithm" is the reduced datum `B'` (the change is through `mb:reduced-datum`, Y 41407-41409), and that `d` of `dnr:norms` is `d_B` of the preceding joined sequence. **Status: proved in Y at another place in a form that needs a matching step; an assumption in the port until that step is ported.**
- **(IN-POLY)** the joined response polydisc of radius `r_B`. At the lines of use it is assumed ("Assume it stays in the common admitted datum ball", Y 13244; `r_B` is named only at Y 13345). The radius `r = c b^{-8}` of `dnr:response` with the uniqueness clause of `dnr:physical` is a statement of this form on any admitted separated sequence. Whether the joined sequence `B^W` and its datum meet the hypotheses of the `dnr` section (the regular-pair domain on the complete gauge cubes and collars, Y 40705-40709) is not written. **Status: as (IN-RESP).**
- **(IN-PR)** weighted pointwise kernels of the coupled inverse for the three readouts. Assumed at Y 13155-13157; Y 16084-16085 calls existence and uniqueness "response inputs of A3". Y 25753-25790 lists five ingredients for the coupled inverse and says where each is proved, ending with "the response on the full first-order regular-pair domain in `dnr:response`". The three readouts with their powers of the spacing are in `dnr:response-bounds` and `dnr:current-bound` (Y 41196-41200, 41221-41224: `|j_s(H)|_{3,w} + |P_{1,s} H|_{3,w} <= C b^4 |B'|_w`), and the coupled system in `dnr:coupled` (Y 41506-41525). **Status: as (IN-RESP).** The row sum (IN-ROW) then follows from the weighted norm with a supremum over rows, not from a separate Schur premise.
- **(IN-AVX)** the one-step averaging expansion. Y states it as `prop:averaging-1a-1-5` (Y 3766-3783: `Q^1(W_0, a) = Q(W_0) a + C^1`, `||S(W_0)||_row <= L`, `||Q(W_0) - S(W_0)|| <= C varpi`, `|C^1| <= C |a|^2`) and gives the proof as a sketch ("proved by universality and Cauchy bounds", Y 4528). The iterated form is `prop:averaging-1a-1-6` (Y 3785-3800; Y 4528-4536). **Status: stated in Y with a sketched proof; not an assumption of Y. The hand proof is `library/b98.md` Lemma 8, which waits for its other-provider check.**

## 9. Item (9): twelve quoted passages against Y

| # | Port, place | Quoted text (start) | Cited | Found | Text |
|---|---|---|---|---|---|
| 1 | ypath 1(b) | "This constructs the old datum without using the preceding guard on that ball" | 64976-64977 | 64976-64977 | agrees |
| 2 | ypath 1(d) | "On admitted real data the collar response fits these reserves, by its weighted bound on the old shells" | 64265-64268 | 64265-64267 | agrees |
| 3 | ypath P7 | "For M large, the decay e^{-c(M/M_1)(j-i)} across the shells dominates 1+(j-i)^{1/2}" | 63876 | 63876 | agrees |
| 4 | ypath P3.4 | `B(w) dF_q = H(w) - sum_i alpha_i H(v_i)` | 75226-75240 | 75238-75241 | agrees |
| 5 | ypath IN-TRANS | `(1 + varpi)^{m(m-1)/2} - 1` | 3717-3727 | 3717 | agrees |
| 6 | yjoin J1.4 | "The denominator comes from summing the smaller curvature bounds over q < j" | 13316-13317 | 13321-13322 | agrees; lines off by 5 |
| 7 | yjoin 0, 9 | "Assume it stays in the common admitted datum ball" | 13244 | 13244 | agrees |
| 8 | yjoin 0, 9 | "Assume the actual coupled inverse has weighted pointwise kernels" | 13155 | 13155-13156 | agrees |
| 9 | yjoin J2 | "The same calculation applies ... to each proved differentiated field readout" | 13161-13163 | 13174-13177 | agrees; lines off by 13 |
| 10 | yjoin J2.4 | "independent of the depth and volume" | 13394-13396 | 13394-13395 | agrees |
| 11 | yjoin BT.1 | "It does not require the discarded sharp bound at the artificial bare rim of X" | 64083-64086 | 64085-64086 | agrees |
| 12 | yjoin BT.4(c) | "without assuming an additional collar bound on the crossing itself" | 64196-64198 | 64197-64198 | agrees |

Other line citations that are off (text right): the citations of yjoin section 3 into Y 13368-13396 are in general about 5 lines early (for example the rate `delta_0/2` sentence, cited Y 13376-13377, found Y 13370-13372 with the `12 mu` sentence at Y 13372-13376); yjoin BT setting, "the preceding guard kept during these comparisons", cited Y 64038-64039, found Y 64043-64044; yjoin section 4 and J3.5, the stages and `delta'_j := g_j A_1 p_1(g_j)`, cited Y 63834, found Y 63836; yjoin J2, `mb:extended-source`, cited Y 13165-13178, found Y 13179-13190. Also checked and agreeing: Y 65055-65056 ("no layer has spacing greater than `L^m`"), Y 65053 ("keeps these carriers out of finer layers"), Y 65056-65057 ("followed by averaging on these blocks"), Y 64806-64807 (bounded derivative of the mean contour map), Y 64105-64106, Y 4391, Y 64962.

## 10. The repairs, in one list

- R1 (ypath P3.1): replace the convexity sentence by the lemma of section 1 (R1a), or by IN-MEAN with the changed `C_2` (R1b).
- R2 (ypath (S-e), (S-d)): add the chart radius `rho_mean` of IN-MEAN: `2 pi m_L^2 C_av e_* <= rho_mean/2`, `2 pi m_L delta'_j <= rho_mean/2`. Also say `S(a/2) >= S(a)` w.l.o.g., so that `C_5 <= C_5'`.
- R3 (ypath P6, P7 remark): the rate is `a = delta_0`, fixed with `L` (Y 17399, 63873); cite Y 17399 for the order.
- R4 (yjoin J1.5): outward rows have one end outside `Omega_n`; use separation (text in section 4).
- R5 (ypath P5.4, yjoin D.5): state (E1) at every bare plaquette of old local scale at least `xi_j` with `|dU^+(p) - 1| <= xi_j^{-2}`.
- R6 (yjoin (C-s)): `pi (1 + C(L)) delta'_j <= rho_mc` and `C_mc pi (1 + C(L)) delta'_j < eps_j`.
- Citations: add Y 3785-3800 and 4528-4536 for Lemma AVG; correct the five line ranges of section 9; state `lambda_low >= 0` in (RC) and `2 tau < c_3` in (J3-s).

RESULT: all nine items checked, none FAILS; (1) P3.2, P3.4, P5.3, P7.1 HOLD and P3.1 HOLDS WITH REPAIR; (2) no cycle, order listed; (3), (4) J1, (6) Y-DENS and Y-CONT HOLD WITH REPAIR (six text repairs R1-R6, no conclusion changed); J2, J3 with the stage-window finding, Y-BELT, Y-MEAN, section 8 and the twelve quotes HOLD. Open: IN-RESP, IN-POLY, IN-PR are proved in Y in the `dnr` propositions (Y 41183-41232, 41391-41409, 41506-41525) but the match to the lines of use is not written and must be ported; IN-AVX rests on `library/b98.md` Lemma 8 (unchecked); IN-FRAME stays a hypothesis.
