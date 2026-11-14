# Check of library/gap-flat-astra.md (FINISH row 822), by Claude Opus 5.5, line by line

Clone `/Users/jonreilly/ym4d-lead/clone` at commit `ac5c2ff617a422d6fa04d4f3a887a25d5b9c8208`.
Lane D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
Target `D/library/gap-flat-astra.md` (691 lines), read in full. Author: Codex gpt-6-astra max, FINISH row 817.
Context read: `gap-joint-astra.md` lines 40-480 ((J1)-(J4), (J12)-(J17)); `gap-joint-check-opus.md` (anchors for (J12), (J14)); `gap-kappa-order.md:31-74` (Proposition SC, Lemma M, Lemma F, Lemma T); `gap-block-astra.md:595-680` ((B30)-(B32)); `gap-tree-astra.md:285-350` ((G12)-(G13)); `gap-expose-astra.md:574-599` ((E16)-(E17)).

Method. Every step was re-derived by hand. One small GUIDE run (Python fractions and floats, under 1 MB) re-did the rational arithmetic and the binary icosahedral moments after the hand derivation. It decided nothing.

Notation is the note's. O is the set of odd link-connected closed surfaces. Xi is multiaffine in the polymer variables w(S).

## 1. (F1)-(F5): telescoping and the marked-family expansion

**(F2).** By (J1)-(J2), `Z_(m+v) = int C Xi(w_m^O)`, since `w_(m+v)(S) = (-1)^(v(S)) w_m(S)`. So `p_m(v) = (1/2Z_m) int C [Xi(w_m) - Xi(w_m^O)]`. Flipping one odd variable S changes Xi by `2 w(S) d_S Xi = 2 w(S) Xi_comp(S)`, evaluated at the current signs. With F first, the first |F| flips give `Xi(w_m) - Xi(w_m^F) = sum_(S in F) 2 w_m(S) Xi_comp(S)(w^[S])`. Divide by `2Z_m` and integrate: this is `sum_(S in F) D_m(S)`. The right side of (F2) does not depend on the order inside F. HOLDS. F must lie in O; A_K and B do.

**(F4).** For a multiaffine f, `f(y + delta) = sum_H prod_(S in H) delta_S (d_H f)(y)`, where `d_H f` is free of the variables in H. Take `delta_S = -2 w(S)` for S in F. `d_H Xi` vanishes unless H is pairwise compatible; then it equals `Xi_comp(H)` at the unflipped weights. So `Xi(w) - Xi(w^F) = sum_(H nonempty) (-1)^(|H|+1) 2^|H| prod w(S) Xi_comp(H)(w)`. Dividing by `2Z_m` gives the coefficient `(-1)^(|H|+1) 2^(|H|-1)`. The exterior weights are unflipped, as the note says. HOLDS.

**(F5).** With F first, the earlier odd surfaces of S in F are `F_(<S)`. Expand `Xi_comp(S)(w^[S])` the same way in the flipped variables of `F_(<S)` compatible with S. This gives `sum (-2)^|H| prod_(T in H) w(T) Xi_comp(H u {S})(w)`. Multiply by `C w_m(S)`, integrate, divide by `Z_m`. HOLDS. All sums are finite.

Verdict: HOLDS.

## 2. (F6)-(F9): exterior identity, Jensen, product majorant, class bounds

**(F6).** `C prod_(S in H) w_m(S) = prod_(p in Q) sinh(beta eta_p x_p) prod_(p not in Q) cosh(beta x_p)`, since sinh is odd. A surface compatible with H shares no link with Q. So none of its faces lies in N(Q): such a face would carry a link of E(Q). Expand the far exponentials as cosh plus signed sinh, giving a sum over `R subset P_far`. The flip `U_l -> -U_l` kills every term whose sinh set `Q u R` is not closed. Q is closed, so `Q u R` is closed exactly when R is. By the unique decomposition of (J2), closed `R subset P_far` correspond one to one to compatible families of surfaces compatible with H. The two sides agree term by term, with signs. For `H = {S}` and m = 0 this is (J14). HOLDS.

**(F7).** The far faces use no link of E(Q). So `Z_m = int dU_ext prod_far e^(...) [int dU_(E(Q)) exp(beta sum_(p in N(Q)) eta_p x_p)]`. Fix the exterior. Each p in N(Q) contains some link e of E(Q) once (periods at least 3). By right invariance, `int tr(U_e M) dU_e = int tr V dV = 0`. By Fubini and linearity, the conditional mean of the sum is zero. Jensen gives `int exp(f) >= exp(int f) = 1`. Faces of Q are included in N(Q); this is consistent. So `Z_m >= Z_(far,m) > 0`. HOLDS.

**Count.** A closed S has even, nonzero degree at each used link, so at most `4|S|/2 = 2|S|` links. Each link lies in at most six faces. Faces of S use `4|S|` incidences; each face of `N(S)\S` uses at least one. So `|N(S)\S| <= 12|S| - 4|S| = 8|S|`. Also `N(Q)\Q = union_S (N(S)\Q) subset union_S (N(S)\S)`, which gives the subadditive bound. HOLDS.

**(F8).** Bound each cosh in `N(Q)\Q` by `cosh beta >= 1`, so the exponent may be raised to `sum_S |N(S)\S|`. The remaining integrand is `prod_Q |sinh|` (links in E(Q) only) times the far product (links outside E(Q) only). It factors as `[prod_S int dU_(E(S)) prod_(p in S)|sinh|] Z_(far,m)`, since the E(S) are disjoint. Dividing by `Z_m >= Z_(far,m)` cancels `Z_far`. HOLDS. It is uniform in volume, twist and shape.

**(F9).** From (F4): `|T_m(F)| <= sum_(k>=1) 2^(k-1) e_k(b) <= sum_k 2^(k-1) B^k/k! = (e^(2B)-1)/2`, where `e_k` is the elementary symmetric sum. From (F5) and (F8): `|D_m(S)| <= b(S) sum_(H subset F_(<S)) prod_(T in H) 2b(T) <= b(S) prod_(T in F)(1+2b(T)) <= b(S) e^(2B)`. Sum over S. HOLDS. No positivity of an intermediate polynomial is used.

Verdict: HOLDS.

## 3. (F10)-(F14): product Hoelder, moments, bad faces, constants

**(F10) and its proof.** This is Finner's inequality (product probability spaces, functions of coordinate subsets, `sum_(p ni e) 1/h_p <= 1` at each coordinate). The successive-integration proof is valid also when a function depends on links integrated at different steps. Write `g_p^(0) = f_p`. At step t integrate link e_t. Factors not containing e_t pull out. For the factors containing e_t apply Hoelder in `U_(e_t)` with exponents h_p, adding the constant 1 with the leftover exponent if the reciprocals sum to less than one. This replaces `g_p^(t-1)` by `g_p^(t) = (E_(e_t)[(g_p^(t-1))^(h_p)])^(1/h_p)`. Induction gives `(g_p^(t))^(h_p) = E_(e_1..e_t restricted to links of p)[f_p^(h_p)]`, by Fubini and independence. So each face keeps one fixed exponent h_p through all its steps. The link constraint at step t counts each incident factor once with 1/h_p. After the last link, each factor is `||f_p||_(h_p)`. HOLDS.

**Moments (F11).** Density `(2/pi) sqrt(1-x^2)` on [-1,1] is right (`x = cos theta`, weight `(2/pi) sin^2 theta`). `d/dx[x^(2l-1)(1-x^2)^(3/2)] = (2l-1) x^(2l-2)(1-x^2)^(3/2) - 3 x^(2l)(1-x^2)^(1/2)`. Its integral vanishes; with `(1-x^2)^(3/2) = (1-x^2)(1-x^2)^(1/2)` this gives `(2l-1)(M_(l-1) - M_l) = 3 M_l`, that is `(2l+2) M_l = (2l-1) M_(l-1)`. So `M_1 = 1/4`, `M_2 = 1/8`, `M_3 = 5/64`. `(5/64)^(1/6) < 2/3` is `5*729 = 3645 < 4096`. HOLDS.

**sinh.** sinh is convex on `[0, infinity)` with `sinh 0 = 0`, so `sinh(beta t) <= t sinh beta` for `0 <= t <= 1`. Oddness gives the absolute form. HOLDS.

**(F12).** Read "bad face" as "face of S touching a link of S of degree four or six"; the count is over faces of S (precision P1). An r- or i-link lies in exactly two (r,i)-faces; other links in none. So a link of degree at least four carries a nonhorizontal face of S (in fact at least two). Thus branching links number at most 4V. Each carries at most two horizontal faces, so at most 8V bad horizontal faces; with the V nonhorizontal faces, at most 9V bad faces. Lemma M gives at least A horizontal faces, so `V <= |S| - A = k(S)`. HOLDS.

**Exponents.** Only faces of S carry functions in u(S). At a degree-2 link, `1/h + 1/h' <= 1/2 + 1/2`. At a degree-4 or 6 link every incident face of S is bad, so the sum is at most `6/6 = 1`. The condition is per link, so singular vertices do not matter. HOLDS.

**(F13).** With these exponents, (F10), (F11) and the sinh bound give `int prod |sinh| <= (sinh beta/2)^(|S|-B) ((5/64)^(1/6) sinh beta)^B <= (sinh beta/2)^|S| (4/3)^B`, since `2(5/64)^(1/6) < 4/3`. With `|N(S)\S| <= 8|S|` this is `q^|S| (4/3)^B <= q^(A+k) gamma^k`, `gamma = (4/3)^9 = 262144/19683 < 16` (`16*19683 = 314928`). All h_p = 6 gives `q_6^|S|`. HOLDS.

**(F14).** q and q_6 increase in beta, so beta = 1/2 suffices. `log cosh t <= t^2/2` gives `cosh^8(1/2) <= e`. The sinh(1/2) series: after `1/48` the term ratios are `(1/4)/((2n+2)(2n+3)) <= 1/80`, so `sinh(1/2) <= 1/2 + (1/48)(80/79) = 1/2 + 5/237 < 1/2 + 1/30 = 8/15`. `e <= 8/3 + 5/96 = 261/96 < 11/4`. So `q < (4/15)(11/4) = 11/15` and `q_6 < (2/3)(8/15)(11/4) = 176/180 = 44/45`. `e^(1/4) <= 1/(1-1/4) = 4/3 < 15/11` (44 < 45), so `11/15 < e^(-1/4)`. HOLDS. GUIDE: q(1/2) is about 0.681.

Verdict: HOLDS (precision P1 on wording only).

## 4. (F15)-(F18): flat planes, the shape count, the class theorem

**(F15).** `k = 0` forces `V = 0` and exactly one horizontal face per stack. The closure argument of Lemma F then forces a translated flat (r,i) plane. So `A_0` has N_perp members, none branching, and `b = q^A` works. (F9) gives (F15). It is compatible with (J13): `216^(-A) < (11/15)^A`. HOLDS.

**(F16).** Slices are the N_perp two-tori with fixed transverse coordinates. An (r,i)-face has its four links in its own slice. Closure at an r- or i-link of slice sigma reads `d X_sigma = (d Y)` restricted there, where Y is the chosen nonhorizontal set. So, given Y, two solutions on a slice differ by a horizontal mod-2 two-cycle of the slice. Each r- or i-link of the slice lies in exactly two faces of the slice; equal coefficients propagate over the connected torus, so the cycle is empty or the whole plane. At most two solutions per slice. HOLDS.

An (r,j)-face has r-links in two slices and j-links that are not horizontal; a (j,k)-face has no horizontal links. So at most 2v slices are affected. On any other slice X_sigma is empty or a full plane. Since `|S| <= A + K < 2A`, at most one such full plane occurs: N_perp + 1 choices. Completions are at most `4^v (N_perp+1)`. With `v <= k <= K` and at most `binom(N_p, v)` nonhorizontal sets, the first bound follows. The second uses `binom(N_p, v) <= N_p^v` and `(4N_p)^v <= (4N_p)^K`. HOLDS.

**(F17).** On A_K, `b(S) = q^(A+k) gamma^k <= q^A gamma^K <= (11/15)^A gamma^K`, since `q < 1 < gamma`. Multiply by (F16): `B_(A_K) <= U_K`. Then (F9). The class A_K does not depend on beta. HOLDS.

**(F18).** `96 gamma < 96*16 = 1536 < 2048`. `4 N_p <= 96 a^4`. `log(96 gamma a^4) <= 11 log 2 + 4 log a = 4 log(2a) + 7 log 2`, an identity. `7 log 2 <= (7/2) log(2a)` needs `a >= 2`. So the factor is at most `exp(K (15/2) log(2a)) <= exp(3A/40)`. With `(11/15)^A <= e^(-A/4)` the product is `e^(-7A/40)`. `(N_perp+1)(K+1) <= (4a^2+1)^2 <= 25 a^4` for `a >= 1`. `K(a) < A` holds, so (F16) applies; K = 0 is covered. The supremum over a of `25 a^4 e^(-7a^2/40)` is finite, so `exp(2U_K)` is bounded. The rooted sum is at most the class sum. HOLDS.

The ARGUED limit paragraph claims only a loss in this encoding. Fair.

Verdict: HOLDS.

## 5. (F19)-(F23): the bump family

**Family.** Replacing a base face f by the other five faces of its cube is `S = P + boundary(cube)` mod 2. It is closed and keeps every stack parity: the cube's two (r,i)-faces lie in one stack. `|S| = A - 1 + 5 = A + 4` per bump, so `|S| = A + 4b`. Base edges keep degree two: the unremoved neighbour face plus one side face. A neighbour of f shares a vertex with f, so it is not a base face. Each top edge lies in the top face and one side face. Each vertical edge lies in two side faces. Vertex-disjoint bases give distinct new links; with all periods at least 3, `+e_j` and `-e_j` give different layers, so no coincidences arise between bumps of opposite sign. HOLDS.

**25-face count (F19).** Coordinates: plane (1,2) at `x_3 = x_4 = 0`, bump on base face at the origin, direction +3. N(P) is all faces touching 1- or 2-links of the plane, `|N(P)| = 9A` (from (J14)-(J16)).
Each top edge (a 1- or 2-link at `x_3 = 1`) has six faces: the top face; one horizontal neighbour at `x_3 = 1`; one face going up to `x_3 = 2`; the cube side face; two faces in direction 4. Only the side face lies in N(P): it carries a base edge. Distinct new faces: top face 1, horizontal neighbours 4, upward faces 4, direction-4 faces 8; that is 17.
Each vertical 3-link at a base vertex has six faces: two cube side faces (in N(P)); one (1,3)- and one (2,3)-face outside the cube, each containing a plane 1- or 2-link (in N(P)); two (3,4)-faces with no 1- or 2-link. So 8 new faces.
Total 25, the top face among them. So `|N(S)| <= 9A + 25b` even when neighbourhoods overlap, and `|N(S)\S| <= 8A + 21b`. HOLDS. The removed base face stays in N(P); this only helps.

**(F20)-(F21).** No link of S branches, so all h_p = 2 and `int prod |sinh| <= h^(A+4b)`. With (F19), `u(S) <= (cosh beta)^(8A+21b) h^(A+4b) = q^A w^b`. (F8) is per surface, so the product majorant holds for marked families. Summing over all subsets of base faces, with four directions each, gives `(1+4w)^A`; multiple encodings only overcount. With N_perp planes, (F21) follows. HOLDS.

**(F22).** `h <= sinh(1/2)/2 < 4/15`. `cosh(1/2)^21 <= e^(21/8)`. The bound `e^x <= 1 + x + x^2/[2(1 - x/3)]` holds for `0 <= x < 3`, since `n!/2 >= 3^(n-2)` for `n >= 2`. At `x = 5/8`: `1 + 190/304 + 75/304 = 569/304 < 2`. Then `e^(21/8) = e^2 e^(5/8) < (121/16)*2 = 121/8 < 16`. So `w < 16*256/50625 = 4096/50625`. `rho_bump < (11/15)(67009/50625) = 737099/759375 < 1` (`11*67009 = 737099`, `15*50625 = 759375`). HOLDS. GUIDE: the ratio is about 0.9707.

**Density remark.** On even base periods the even-even faces are A/4 vertex-disjoint bases, so b = A/4 and excess A. HOLDS as stated (conditional on even periods).

**(F23).** For the union, sum the smaller majorant; it is at most `U_K + N_perp rho_bump^A`. Both terms are area-small, uniformly on `0 < beta <= 1/2`. HOLDS.

**Bare-weight paragraph.** Constant spin 1/2 on an embedded closed surface with degree-two edges and manifold vertices gives `d^chi r^F` by the J15 sewing. A b-bump torus has chi = 0, so `r^(A+4b)`; a handle lowers chi by 2. The bare sum bound uses `r_(1/2) <= beta/4` from the READ (GL4). It is not used in any bound of the note. HOLDS as READ/PROVED context.

Verdict: HOLDS.

## 6. (F24)-(F26): the group-blind complete bound

**(F24).** `|sinh(beta x_p)| <= sinh beta` and `|N(S)\S| <= 8|S|` give `u(S) <= t_0^|S|`. HOLDS.

**(F25).** (B30)'s count: a depth-first walk of length 2(n-1), each step to one of at most twenty link-neighbours (a backtrack is also a step to a neighbour), so at most `N_p 400^(n-1)` link-connected n-face sets. Every member of O is link-connected with `n >= A`. So `B_all <= sum_(n>=A) N_p 400^(n-1) t_0^n = (N_p/400) rho^A/(1-rho)`; likewise `n >= A + L` for `B_(>=L)`. HOLDS.

**(F26).** (F5) with F = O holds for every ordering, since then `F_(<S)` is the set of all earlier odd surfaces. So `|D_m(S)| <= b(S) e^(2 B_all)`. Sum over `k(S) >= L`. HOLDS.

**Range.** `tanh beta <= beta` gives `sinh beta <= beta cosh beta`; with `log cosh <= beta^2/2`, `rho <= 400 beta exp(9 beta^2/2)`. At `beta = 1/500` the first factor is 4/5 and the exponential is below `1/(1 - 1/9) = 9/8`. So `rho < 9/10` on `(0, 1/500]` by monotonicity. `B_all <= (24 a^4/400)*10*(9/10)^(a^2)` is bounded. With L = 0, `p_m(v) <= B_all e^(2B_all)`, which beats `eta_*^(a/2)` up to a constant. This is (E17), since `Q_F = max p_(m,i)` by (E16). HOLDS. GUIDE: rho(1/500) is about 0.800.

The comparison paragraph is consistent: 1/500 exceeds row 811's 1/2400 and is below Theorem DOB's 2/9 (read, not re-checked). The ARGUED items 1-3 claim deficits of these bounds only; `400 q(1/2) > 100` follows from `sinh(1/2) > 1/2` and `cosh >= 1`. Fair.

Verdict: HOLDS. Precision P2: the bound is uniform on all of `(0, 1/500]`; the "compact positive interval" wording is more cautious than needed.

## 7. Group blindness

**Identities.** (F2)-(F6) need `-1` in the centre (the link flip and the twist signs), Haar invariance and finiteness. (F7) needs the conditional mean zero; right invariance turns `int x(U_e M) dU_e` into `int x dU`, so zero Haar mean of x suffices, as stated. (F8), (F24)-(F26) need only `|x| <= 1` and the combinatorics. All hold for U(1) with `x = cos theta` and for the binary icosahedral group Gamma (`-I` in Gamma; no invariant vector in V gives mean zero). HOLDS.

**Moments.** `x^n = tr(g^(tensor n))/2^n`, so (G12) equates the moments of x through degree eleven; the note claims only degree six, which suffices (P3, wording). Independent derivation by direct class sums over Gamma: the classes give x = 1, -1 (one each), 0 (30), plus or minus 1/2 (20 each), and plus or minus `(1 +- sqrt 5)/4` (12 each sign and value). With `c^2 = (3+sqrt5)/8`, `s^2 = (3-sqrt5)/8`: `E x^2 = [2 + 40/4 + 24(c^2+s^2)]/120 = 30/120 = 1/4`, and `c^6 + s^6 = 2(27+45)/512 = 9/32`, so `E x^6 = [2 + 40/64 + 27/4]/120 = 5/64`. These agree with (F11). The bounds (F10)-(F23) use only `E x^2` and `E x^6`. So the G_K bound transfers to Gamma at `beta <= 1/2`. HOLDS. GUIDE run confirmed 0.25 and 0.078125.

**U(1).** `int cos^2 = 1/2`, so the good-face factor becomes `sinh beta/sqrt 2`. The rational chain gives `(8/15)(1/sqrt2) e > 1`, so (F14) and (F22) do fail to transfer with the same proof. The note claims only this. HOLDS.

**Weak coupling.** `rho >= 400 sinh beta > 1` for `beta >= 1/2`. For `beta >= 2`, `q >= sinh(beta)/2 > beta/2 >= 1`. Correct, and it claims only the failure of these estimates.

Verdict: HOLDS.

## 8. (F27)-(F28), RTAIL, and the RESULT line

**(F27).** `p_m = (1/2Z) int C[Xi(w) - Xi(w^G)] + (1/2Z) int C[Xi(w^G) - Xi(w^O)] = T_m(G) + R_m`. By (F4) with F = O and F = G, R_m is the (F4) sum over compatible H in O with H not inside G. HOLDS. Precision P4: in the (F4) form the exterior weights are unflipped; "signs of the earlier class" describe only the integral form.

**(F28).** `B_G <= 25 a^4 e^(-7A/40) + 4a^2 rho_bump^A <= 29 a^4 e^(-tau a^2)` with `tau = min(7/40, log(759375/737099))` (GUIDE: about 0.0298) and `A >= a^2`. Its supremum over a bounds `e^(2B_G)`. Then (F9). The lower bound: `R_m = p_m - T_m(G) >= -|T_m(G)| >= -sum_G |D_m|`, using `p_m >= 0`. That sign is the READ fact `0 < Z_(m+v) <= Z_m` of (J1) (precision P5: name it as an input). HOLDS.

**RTAIL and (E17).** By (E16), `Q_F = max p_(m,i)`. If RTAIL holds then `p_m <= C_0 a^4 e^(-tau a^2) + C a^p eta_*^(a/2)`, and `-tau a^2 + kappa a <= kappa^2/(4 tau)` absorbs the first term with `kappa = (1/2) log(1/eta_*)`. Conversely `R_m <= p_m + |T_m(G)| <= Q_F + C_0 a^4 e^(-tau a^2)`. So RTAIL on I is equivalent to (E17) on the same `I subset (0,1/2]`, up to constants and powers. The note calls it not easier. HOLDS.

**RESULT line.** It states the absolute area bound for the dressed class A_(K(a)) union B at `beta <= 1/2` with the original Z_m; (J12) and (E17) only for `beta <= 1/500`; that range does not improve the `beta < 2/9` seed; no heavy lower bound, no mass gap, no status; not independently checked. Each claim matches a step that HOLDS above. Fair.

## Verdict table

| Item | Steps | Verdict |
|---|---|---|
| 1 | (F1)-(F5) | HOLDS |
| 2 | (F6)-(F9), the `8|S|` count | HOLDS |
| 3 | (F10) and its proof, (F11), sinh bound, (F12), exponents, (F13), (F14) | HOLDS (P1 wording) |
| 4 | (F15)-(F18) | HOLDS |
| 5 | (F19) 25-face count, (F20)-(F23), bare weights | HOLDS |
| 6 | (F24)-(F26), range 1/500 | HOLDS (P2 wording) |
| 7 | Group blindness, Gamma moments, U(1) | HOLDS (P3 wording) |
| 8 | (F27)-(F28), RTAIL equivalent to (E17), RESULT line | HOLDS (P4, P5 wording) |

Precisions (none changes a conclusion):
- P1. (F12): "bad face" means a face of S touching a branching link. The bound on branching links can be 2V; 4V is safe.
- P2. (F26): uniform on all of `(0, 1/500]`.
- P3. Section 7: (G12) gives equal moments through degree eleven; degree six is what is used.
- P4. (F27): in the (F4) form all exterior weights are unflipped.
- P5. (F28): the lower bound on R_m uses `p_m(v) >= 0`, read from (J1).

No step FAILS. No correction is needed.

Checked line by line by Claude Opus 5.5. Credit Codex gpt-6-astra max for the note. This is one check, not an audit; it grants no scientific status.

RESULT: Every PROVED step of gap-flat-astra.md HOLDS on a hand re-derivation by Claude Opus 5.5 — the expansions (F2)-(F5), the exterior identity and Jensen bound (F6)-(F7), the product majorant (F8)-(F9), Finner-type Hoelder (F10) with its successive-link proof, the moments and constants (F11)-(F14), the shape count and class theorem (F16)-(F18), the 25-face bump count and (F19)-(F23), the small-beta bound (F24)-(F26) at beta <= 1/500, the group-blindness claims, and (F27)-(F28) with RTAIL equivalent to (E17) — nothing FAILS, five wording precisions change no conclusion, and the RESULT line is fair.
