# B98-I: the signed averaging bound for the iterated block average

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, 2026-11-06, commit 392550b85. Written during the check `gates/b98-gate.md` (FINISH row 374) as the repair of its finding 1. Proved by Claude, not yet checked by the other model. Research text; no status is granted.

Credit. The averaging maps are Tadeusz Balaban's (CMP 98 (42); CMP 109 (0.10)-(0.12)). The statement repaired is CA-II `8.11:lem-signed-averaging` of the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), at `31a47c543775`. The one-step lemmas used are `library/b98.md` Lemmas 1-5 (Codex), checked in `gates/b98-gate.md`. The method of summing one-step errors through the composed linear map follows CMP 98 (127)-(129), which does this for Balaban's relative averages.

## Why this is needed

CA-II `8.11:lem-weighted-flux` (about L123076-123216) applies the signed bound (B3) to V = \bar U^{k_o}(U), the composition of k_o one-step maps of CA-I Definition 1.5, with block side n = L^{k_o} = η^{-1}. `b98.md` Lemma 5 proves (B3) for one averaging step with block side n. That does not give the composition: each of the k_o steps adds a nonlinear error, and a sup-norm bound on links gains a factor (d+1) per step. Lemma I below sums the errors through the exact composed linear map, uniformly in k_o.

## Setting

Work in fine lattice units. Fix d ≥ 2 (d = 4 in the application), N, an odd L ≥ 3, k ≥ 1, and put n = L^k. Level-j sites form y_0 + L^j Z^d, for 0 ≤ j ≤ k; every level-(j+1) site is a level-j site. Put h_L = (L−1)/2 and O_m = {o ∈ Z^d : |o_ν| ≤ (L^m − 1)/2}. A level-(j+1) site y has the block B(y) = y + L^j O_1 of level-j sites. The m-fold block of a level-(j+m) site y is B^m(y) = y + L^j O_m. This holds because every integer q with |q| ≤ (L^{m+1}−1)/2 has exactly one form q = L^m q' + o with |q'| ≤ h_L and |o| ≤ (L^m−1)/2. A level-j bond c = (c_-, c_+) in direction μ has c_+ = c_- + L^j e_μ.

Let M be the one-step map from level-j to level-(j+1) configurations, either Balaban's CMP 98 average (`b98.md` (5)) or the symmetrised CMP 109 average of CA-I Definition 1.5(a). For a level-j bond field e with e(−b) = −e(b), and a path γ, write e(γ) for the signed sum of e along γ. The linear one-step map Q is
\[
 (Qe)_c=L^{-d}\sum_{x\in B(c_-)}\bigl[s_{c_-}(x)(e)+e([x,x'])-s_{c_+}(x')(e)\bigr],\qquad x'=x+L^{j+1}e_\mu ,
\]
for a level-(j+1) bond c, with [x,x'] the straight level-j path. For CMP 98, s_y(x)(e) = e(Γ_{y,x}). For CMP 109, s_y(x)(e) is the mean of e(Γ) over the family G(y,x) of shortest contours obtained from all permutations of the coordinate order (CMP 109 OCR 190-206). In both cases s_y(x) depends only on y and x, it is a convex combination of path sums of at most d·h_L level-j bonds, and G(y+v,x+v) = G(y,x) + v. `b98.md` Lemma 4 shows that Q is the linear part of M.

## Lemma I0 (the composed linear map)

For m ≥ 1, a level-j bond field e and a level-(j+m) bond β from β_- to β_+ (of either orientation),
\[
 (Q^me)_\beta=L^{-md}\sum_{o\in O_m}\bigl[S^m_{\beta_-}(\beta_-+L^jo)(e)+e([\beta_-+L^jo,\ \beta_++L^jo])-S^m_{\beta_+}(\beta_++L^jo)(e)\bigr]. \tag{I0}
\]
Here [·,·] is the straight level-j path, and S^m_y(x)(e) is a convex combination of signed sums of e along level-j paths from y to x of at most dL^m/2 bonds. It depends only on y and x.

Consequences:

- (I0.a) |(Q^me)_β| ≤ (d+1)L^m sup|e|, the supremum over the level-j bonds on these paths.
- (I0.b) Let P be the level-k block plaquette at the level-k site y in the (μ,ν) plane, with corners y_0 = y, y_1 = y+ne_μ, y_2 = y+n(e_μ+e_ν), y_3 = y+ne_ν, and j = 0. Then
\[
 \sum_{c\subset\partial P}\pm(Q^ke)_c=n^{-d}\sum_{x\in B^k(y)}\ \sum_{p\subset(P)_x}e(\partial p).
\]

*Proof.* Case m = 1 and β positive: this is the definition, with S^1 = s and o ∈ O_1. For a negative bond, (Q^me)_{−β} = −(Q^me)_β. Reversing the bracket in (I0) gives the same form with β_- and β_+ exchanged, since e of the reversed straight path is minus e of the path. So (I0) holds for both orientations once it holds for positive bonds.

Induction step. Assume (I0) at m for every level-(j+m) bond. Let Γ be a level-(j+m) path from y to X with consecutive bonds β_1, …, β_r. Summing (I0) along Γ, the S^m terms at the interior vertices cancel, because (β_i)_+ = (β_{i+1})_- and the offsets o are the same for every block. So
\[
 \sum_i(Q^me)_{\beta_i}=L^{-md}\sum_{o\in O_m}\bigl[S^m_y(y+L^jo)+e(\Gamma+L^jo)-S^m_X(X+L^jo)\bigr],
\]
where Γ + L^j o is the level-j path that replaces each β_i by the straight path from (β_i)_- + L^jo to (β_i)_+ + L^jo. It has r L^m level-j bonds.

Now let c be a positive level-(j+m+1) bond in direction μ and f = Q^m e. By definition, (Qf)_c is L^{-d} times the sum over X ∈ B(c_-) of s_{c_-}(X)(f) + f([X,X']) − s_{c_+}(X')(f), with X' = X + L^{j+m+1}e_μ. Apply the display to each path in these three terms, and average over the contours. The terms S^m_X(X + L^jo) and S^m_{X'}(X' + L^jo) cancel. What remains is
\[
 (Q^{m+1}e)_c=L^{-(m+1)d}\sum_{X\in B(c_-)}\sum_{o\in O_m}\Bigl\{\bigl[S^m_{c_-}(c_-+L^jo)+\overline{e}(c_-,X;o)\bigr]
 +e([X+L^jo,X'+L^jo])-\bigl[S^m_{c_+}(c_++L^jo)+\overline{e}(c_+,X';o)\bigr]\Bigr\},
\]
where \overline{e}(y,X;o) is the mean of e(Γ + L^jo) over Γ ∈ G(y,X) (or e(Γ_{y,X} + L^jo) for CMP 98). Write X = c_- + L^{j+m}q' with q' ∈ O_1. Then X + L^jo = c_- + L^jo'' with o'' = L^m q' + o, and (q',o) ↦ o'' is a bijection onto O_{m+1}. Also X' + L^jo = c_+ + L^jo'', and G(c_+,X') = G(c_-,X) + (c_+ − c_-). Define S^{m+1}_y(y + L^jo'') := S^m_y(y + L^jo) + \overline{e}(y, y + L^{j+m}q'; o). This depends only on y and o''. The straight path from X + L^jo to X' + L^jo is the straight path from c_- + L^jo'' to c_+ + L^jo'', of L^{m+1} level-j bonds. This is (I0) at m+1. Each contour in G has at most d·h_L level-(j+m) bonds, so S^{m+1} has at most dL^m/2 + d h_L L^m = dL^{m+1}/2 level-j bonds. Convexity is kept by the means.

(I0.a) follows from (I0) and the triangle inequality: dL^m/2 + L^m + dL^m/2 bonds. For (I0.b), write ∂P = c_1 + c_2 − c_3 − c_4 with c_1 = (y_0,y_1), c_2 = (y_1,y_2), c_3 = (y_3,y_2), c_4 = (y_0,y_3). By (I0) at m = k, each corner term S^k_{y_i}(y_i + o) occurs once with each sign and cancels. The straight paths form the boundary of the square (P)_{y+o} with lower corner y + o. The boundary sum of a square equals the sum of the boundary sums of its n² plaquettes, because interior edges cancel. This is an identity of additive sums, so no commutativity is needed. As o runs over O_k, x = y + o runs over B^k(y). □

## Lemma I (signed bound for the iterate)

Let G = SU(N), let U be a G-valued fine configuration, and let P be as in (I0.b). Let Δ(P) = B^k(y_0) ∪ … ∪ B^k(y_3), a box with two sides 2n−1 and the others n−1. Assume ‖U(∂p) − 1‖ ≤ f for every fine plaquette p ⊂ Δ(P), and put α = n²f. Write U^loc for U in the tree gauge of `b98.md` Lemma 3 on Δ(P), Φ^loc(p) = i^{-1} log U^loc(∂p), and A_P^loc = n^{-d} Σ_{x∈B^k(y)} Σ_{p⊂(P)_x} Φ^loc(p).

There are C_I = C_I(d) and c_I = c_I(d,L,N) > 0, independent of k, such that α ≤ c_I implies:

1. for 0 ≤ j < k, M^jU lies in the set S_c of CA-I (1.5:eq-block-average-1) for every level-(j+1) bond c with both endpoints in Δ(P), so every step that (M^kU)(∂P) reads uses formula (a) of Definition 1.5;
2. ‖(M^kU^loc)(∂P) − 1 − i A_P^loc‖ ≤ C_I α²;
3. ‖A_P^loc‖ ≤ ‖(M^kU)(∂P) − 1‖ + C_I α²;
4. for every gauge g on Δ(P) with ‖U^g_b − 1‖ ≤ 2dnf on the fine bonds of Δ(P), for example the axial gauge of CMP 98 (45) with the bound (46), ‖A_P^g‖ ≤ ‖(M^kU)(∂P) − 1‖ + (C_I + 32d²)α².

**Application.** In CA-II 8.11, η = L^{-k_o} = n^{-1} with k = k_o, f = αη² and \bar U = V = M^{k_o}U. Clause 4 is (B3) for the average that `8.11:lem-weighted-flux` uses, with C_0'' := C_I + 32d² (depending on d only) and c_2 := c_I. The identities (B1)-(B2) are `b98.md` Lemma 5's exact count.

*Proof.* Put τ = 4dα. Let R_j be the set of level-j bonds with both endpoints in Δ(P). All suprema below are over R_j at the stated level. The blocks of every level are nested and partition the lattice, and Δ(P) is a union of level-k blocks. So a level-(j+1) site in Δ(P) has its level-j block inside Δ(P), and the double block of every c ∈ R_{j+1} lies in Δ(P), with its level-j bonds in R_j. The four bonds of ∂P lie in R_k. The paths of (I0) for c ∈ R_m lie in B^m(c_-) ∪ B^m(c_+) ⊂ Δ(P).

*Step 1 (gauge, locality, covariance).* By `b98.md` Lemma 3 with D < 2n, the tree gauge gives ‖U^loc_b − 1‖ ≤ 2(d−1)nf = 2(d−1)α/n. For 4(d−1)α ≤ 1 this is at most 1/2, so U^loc_b = e^{ia_b} with a_b Hermitian traceless and ‖a_b‖ ≤ 4(d−1)α/n ≤ τ/n, by (2). Every path in CMP 98 (42) and CMP 109 (0.11)-(0.12) for c lies in the double block of c. The induction of `b98.md` Lemma 2 therefore shows that (M^kV)(c) reads only fine bonds in B^k(c_-) ∪ B^k(c_+). So (M^kV)(∂P) reads only Δ(P). Both maps are covariant: M(V^g) = (MV)^{g'}, with g' the restriction of g to the coarse sites (`b98.md` Lemma 2, and Lemma 4's last paragraph for the symmetric mean). Membership in S_c is gauge invariant, since gauge maps conjugate plaquette variables. Extend the tree gauge g_1 by 1 outside Δ(P). Then (M^kU^loc)(∂P) = g_1(y)(M^kU)(∂P)g_1(y)^{-1}, so ‖(M^kU^loc)(∂P) − 1‖ = ‖(M^kU)(∂P) − 1‖.

*Step 2 (one step).* `b98.md` Lemma 4 with block side L, together with (2), gives t_*(d) ∈ (0,1/8] and C_4(d) as follows. Let V = e^{ib} on the level-j bonds of the double block of a level-(j+1) bond c, with L‖b‖ ≤ t ≤ t_*. Then i^{-1} log M(V)(c) = (Qb)_c + r_c with ‖r_c‖ ≤ C_4 t². (Lemma 4 gives M(V)(c) = 1 + i(Qb)_c + E_c with ‖E_c‖ ≤ C_d t². Also ‖(Qb)_c‖ ≤ (d+1)t by (I0.a). Then (2) bounds log(1+Z) − Z by ‖Z‖² ≤ ((d+1)t + C_d t²)².) The plaquettes of V in that double block satisfy ‖V(∂p) − 1‖ ≤ 8‖b‖, by (1). The normalized Hilbert-Schmidt norm |·| of CA-I is at most the operator norm. So V ∈ S_c when 8‖b‖ < ω_M(L).

*Step 3 (induction over levels).* Put a^{(0)} = a. For j < k put a^{(j+1)} = i^{-1} log M(e^{ia^{(j)}}) on R_{j+1}, and r^{(j)} = a^{(j+1)} − Q a^{(j)}. By induction and locality, e^{ia^{(j)}} = M^jU^loc on R_j. Q is linear, so
\[
 a^{(m)}=Q^ma+\sum_{j=0}^{m-1}Q^{m-1-j}r^{(j)}\quad\text{on }R_m .
\]
Put K = 2(d+1)(d+2)²C_4. We prove, for 0 ≤ m ≤ k,
\[
 \|a^{(m)}\|\le(d+2)L^m\tau/n,\qquad \|a^{(m)}-Q^ma\|\le K L^{2m}(\tau/n)^2 . \tag{H_m}
\]
(H_0) holds. Assume (H_j) for j < m. Then L‖a^{(j)}‖ ≤ (d+2)L^{j+1}τ/n ≤ (d+2)τ, since L^{j+1} ≤ n. Require
\[
 (d+2)\tau\le t_*,\qquad 8(d+2)\tau<\omega_M(L),\qquad K\tau\le1 . \tag{S}
\]
Step 2 then applies at level j, puts M^jU^loc in S_c on R_{j+1}, and gives ‖r^{(j)}‖ ≤ C_4(d+2)² L^{2j+2}(τ/n)². By (I0.a) at level j+1,
\[
 \|a^{(m)}-Q^ma\|\le\sum_{j<m}(d+1)L^{m-1-j}C_4(d+2)^2L^{2j+2}(\tau/n)^2
 \le(d+1)(d+2)^2C_4\frac{L}{L-1}L^{2m}(\tau/n)^2\le KL^{2m}(\tau/n)^2 ,
\]
since L/(L−1) ≤ 3/2. With (I0.a) at level 0, ‖a^{(m)}‖ ≤ (d+1)L^m τ/n + K L^{2m}(τ/n)² ≤ (d+2)L^mτ/n, because K L^m τ/n ≤ Kτ ≤ 1. This proves (H_m) and clause 1, by gauge invariance of S_c (Step 1).

*Step 4 (the block plaquette).* (M^kU^loc)(∂P) is the ordered product of e^{±ia^{(k)}_c} over the four sides. Their norms add to s ≤ 4(d+2)τ. Require 4(d+2)τ ≤ 1/4. Then (1) gives ‖(M^kU^loc)(∂P) − 1 − iΣ_c ±a^{(k)}_c‖ ≤ 16(d+2)²τ². By (H_k), ‖Σ_c ±(a^{(k)}_c − (Q^ka)_c)‖ ≤ 4Kτ². By (I0.b), Σ_c ±(Q^ka)_c = n^{-d} Σ_x Σ_p a(∂p). For each fine plaquette, (1) and (2) with s = 4τ/n give ‖Φ^loc(p) − a(∂p)‖ ≤ 5(4τ/n)². The double sum has total weight n^{-d}·n^d·n² = n², so this replacement costs at most 80τ². Hence clause 2 holds with C_I := (16(d+2)² + 4K + 80)(4d)².

*Step 5 (clauses 3 and 4).* Clause 3 follows from clause 2, the triangle inequality and Step 1. For clause 4, let U^g = (U^loc)^h with h a gauge on Δ(P). From h(b_-)U^loc_b = U^g_b h(b_+),
\[
 h(b_-)-h(b_+)=(U^g_b-1)h(b_+)-h(b_-)(U^{\rm loc}_b-1),
\]
so ‖h(b_-) − h(b_+)‖ ≤ 2dnf + 2(d−1)nf ≤ 4dnf. Every site of Δ(P) is joined to y by a path of at most (d+2)n ≤ 2dn fine bonds. So ‖h(z) − h(y)‖ ≤ 8d²α. Now Φ^g(p) = Ad(h(x_p))Φ^loc(p), and ‖Ad(h)X − Ad(h')X‖ ≤ 2‖h − h'‖‖X‖ for unitary h, h'. With ‖Φ^loc(p)‖ ≤ 2f and total weight n², ‖A_P^g − Ad(h(y))A_P^loc‖ ≤ n²·2·8d²α·2f = 32d²α². Ad(h(y)) preserves the norm. Clause 3 then gives clause 4.

*Constants.* C_4 and t_* depend on d only. They come from `b98.md` Lemmas 1 and 4, whose majorants and inner-mean contraction do not depend on N or on the number of contours. So C_I = C_I(d). Take c_I(d,L,N) as the largest α for which 4(d−1)α ≤ 1, (S) and 4(d+2)τ ≤ 1/4 hold with τ = 4dα. It depends on L and N only through ω_M(L) of CA-I Definition 1.5. Nothing depends on k. □

**What this does not show.** It treats only the small-field formula (a) of Definition 1.5. Clause 1 shows that the large-field branch (b) is not reached under α ≤ c_I. It gives no bound on single averaged links in a general gauge, and it says nothing about CMP 98 Proposition 6 (164). The same proof with s_y(x)(e) = e(Γ_{y,x}) gives a signed form of CMP 98 Proposition 2 for Balaban's iterate \bar U^k.

## Lemma C0 (target C at k = 0)

This is finding 2 of `gates/b98-gate.md`. It treats CA-I `4.9:prop-cube-gauge-regular` at k = 0, which the consumer `4.9:lem-seed-cube-gauge` (j ≥ 0) reads and `b98.md` Lemma 12 excludes. At k = 0, η = ξ_0 = 1, r = R_1M_1 ≥ 1, □_0 = □ + r and \widetilde□ ⊂ □ + 2r. Assume the level-0 bounds of (C1), |U_0(∂p) − 1| < α_0, on the box Q := □ + 3r. The consumer supplies them: its hypothesis Reg_0 holds on 𝒩(□^a) = □^a + 4r ⊃ Q. Use the tree gauge a of `b98.md` Lemma 3 on Q, whose side is at most M* + 6r ≤ 7M*. It gives ‖U_0^a(b) − 1‖ ≤ 7(d−1)M*α_0 ≤ s/9, with s = 7dL²M*α_0 and L ≥ 3. For s ≤ 1/6 the series bound ‖log(1+Z)‖ ≤ (6/5)‖Z‖ gives U_0^a = e^{iA_0} with |A_0| < 9(d−1)M*α_0 < s. Direct differences at h = 1 give |∇A_0| ≤ 2s, |ΔA_0| ≤ 4ds and |∂*∂A_0| ≤ 8ds on □_0, as in `b98.md` (40). Their stencils reach at most 2 ≤ 2r beyond □_0, so they stay in Q. Put u^{-1} = a v^{-1} with U_0' = U_0^v (gauge composition as in `b98.md` (43)). Then (C4) holds on \widetilde□ ⊂ Q, and (C5) at j = 0 holds once B_1 > 8d. `b98.md`'s choice B_1 > C_* already gives this, because C_* includes the bounds (40) at h ≤ 1/3, which exceed 8d. □

Proved by Claude (Mini worker), not yet checked by the other model.
