lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T19:18Z

# ref-chart: the joint critical reference chart (outline Proposition 2.4, Balaban CMP 122 Proposition 1)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; queue row 133; pinned at `6a1fad49b` on `claude/ym4d-hard-route`; research text, not an audit, same-model, no gate yet. No numerics were run; every step below is a written argument.

**Outcome (filled in at the end, Section 10).** In progress.

## 1. Scope, sources, credit

Moves: `library/sa-ledger.md` rank 6 (2.13), at the obligation `library/sa-2.13-2.md` Section 7 names first, which I4 of `library/sa-2.8-terms.md` and the (D-F) floor screening also read: the outline's Proposition 2.4 (SA L17656), cited there to Balaban, CMP 122 (1989) 175-202, Proposition 1. If it holds, I4 is no longer cited-pending and Lemmas 3.1-3.2 of `sa-2.13-2.md` lose their reference-chart premise; if it fails, the reference law of the R operation has no centre and Package C's healing step has to be rebuilt.

Sources. The outline is Ethan Sussman and Levent Alpoge's `YM4_sketch_500.tex` at `31a47c543775` (Claude and Codex are the authors of its text), fetched once to a scratch folder outside the repository, SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` (the same file `sa-2.13-2.md` used). `SA Lx` is its TeX line. Read: SA 17576-17662 (the R operation, (0)-(4), the reference law, Proposition 2.4), SA 7955-8001 and 8160-8190 (the centred average (QC1)-(QC4), its linearisation (QC15)), SA 9660-9672 (Theorem 1), SA 9734-9746 (Theorem 4), SA 9776-9786 (Theorem 6, localisation), SA 18025-18092 (the complex-pair exponent and (pointwise-pair)). Balaban's CMP 122 is not in `~/ym4d-papers/` and `library/lit-balaban.md` found no legal copy, so his proof was not read; I checked CMP 119 Sect. 1 (it treats the large-field decomposition, not the box minimiser) and use CMP 102 only through its port in `library/a1-balaban.md`. The proof below is a convexity argument; it is not a reconstruction of Balaban's contraction proof.

Credit. The statement, the reference law it serves and the proof sketch (Hessian at least $c\|\partial B\|^2$ less a small multiple of $\|B\|^2$; tree-gauge Poincaré inequality) are the outline's, after Balaban CMP 122 Proposition 1 and CMP 122 (1989) 355 (1.7)-(1.9). The background, its uniqueness and analytic chart are Balaban's CMP 102 Theorem 1 as ported in `library/a1-balaban.md` (Codex); the decay of its datum derivative is Balaban's CMP 102 (190), proved in `library/a3-derivative.md` (Claude, Codex). The counting lemma is `library/sa-2.8-terms.md` Lemma BC. The use of complete-action criticality to centre the complex denominator is `library/sa-2.13-2.md` Section 3 (Codex).

Standing of the inputs read here (each a gated implication, none an audit):

| Input | What is read | Where, gate |
|---|---|---|
| P81 | unique regular critical orbit $\Phi(\mathbf V)$ of the localised problem; raw identity $M_{\mathbf B}\Phi_{\mathbf V_0}(B)=e^{iB}\mathbf V_0$; holomorphic on $\|B\|_\infty<r_{\rm B}$ about every real datum strictly inside the admissible radius $\bar\varepsilon$; $r(\Phi(B))\le C(\varepsilon_1+\|B\|_\infty)$, real and complex; (8.2) $\lvert\partial U(p)-1\rvert\le B\varepsilon_1\eta^2\mathsf L(p)^{-2}$, $\lvert J(U)(b)\rvert\le B\varepsilon_1\mathsf L(b)^{-3}$ | `a1-balaban.md` (8.1)-(8.2), 9.1; gate row 91, F0 by rows 95, 99 |
| T4 | at a real critical reference, on the whole polydisc: $\xi_y\lvert h_c\rvert+\xi_y^2\lvert\nabla h_c\rvert\le C_4e^{-\theta d_{\mathbf B}(y,y_c)}\lvert e\rvert$ for the response to a raw datum change $e$ at the determining bond $c$, $\theta=\delta_0/8$ | `a3-derivative.md` 6-7 (Theorem 4, first paragraph); gate row 89; with P82° (rows 98, 100) and $U_0\in{\rm Reg}$ (`a3-close.md` (1), gate row 106) |
| RD | row-map bounds: the $k$-step average is holomorphic and bounded on $\{s\sup_{S_c}\lvert a\rvert\le r_*\}$ about a regular reference; derivative densities (9)-(10); endpoint factors of condition number $\le2$ | `a3-derivative.md` 4.1-4.2, 7.5; gate row 89 |
| BC | $\sum_{\text{tops }y}e^{-\theta' d_{\mathbf B}(y,E)}\le C_{\rm BC}(D+4)^4$ for $E\subset\Omega_k$ of diameter $\le D$, under GEO4 | `sa-2.8-terms.md` (4.2); gate row 107; GEO4 by `geo-5.md`, gate row 127 |
| SEP | the localised problem of $X$ is a separated sequence with the gaps of GEO4 and the gap condition of `a3-close.md` (1) | outline Theorem 6(a); `assign-adopt.md` Lemma A; premise as in `sa-2.8-terms.md` Section 3 |

## 2. Counterexample first

Pass/fail criteria fixed before the proof: a counterexample is an admitted datum of the reference problem (exterior data $\varepsilon$-regular with $\varepsilon\le C\varepsilon_k$, box data in the mild class) at which either (a) the axial-gauge Hessian of $f(V)=A(U_{k,X}(V))$ in the box variables has a direction with $h(w)\le o(1)\lVert w\rVert^2$ as the depth $k$, the exterior volume or the coupling vary with $M$ fixed, or (b) the minimum of $f$ over the class is not attained in its interior, or is attained twice. Four attempts.

1. *A soft mode at flat data from the fine scales.* The freed Hessian at $\mathbf V=\mathbf 1$ is $\min\{\lVert dY\rVert^2:Y\text{ has linearised averages }(0,w)\}$, a minimum over $L^{4k}$ times as many fine variables as box variables. A soft mode would be a $w$ whose fine extensions can all be nearly curl-free. Excluded exactly: the curl of the linearised average is a positive average of the fine curl with $\lVert\cdot\rVert_{2\to2}\le1$ at every step (Lemma E), so $\lVert dY\rVert^2\ge\lVert d_k(0,w)\rVert^2$ at every depth, with no constant.
2. *A soft mode from gauge directions.* Gauge transformations at box sites are exact symmetries of $f$; the tree of $\delta_{\rm ax}$ with its external bond fixes them completely, with no residual constant gauge (Lemma G). A curl-free level-$k$ field vanishing on the tree and outside the box is zero (Lemma P). No soft mode.
3. *A long-range mode through the exterior.* Freeing the box couples it to the whole of $X$ through the background. The exterior averages stay fixed, so the background's response to box data decays exponentially in the joined metric (T4), including down the collar tower; the far exterior enters the Hessian only through sums that Lemma BC bounds without depth or volume. No long-range soft mode.
4. *A minimiser on the boundary of the class.* This needs a gradient at the flat-cycle centre of the class of size comparable to $c(M)a_\Lambda$. The gradient there is the box multiplier, which is at most a constant times the regularity of the background, $C(M)\varepsilon$ (Lemma M), while the class has fixed radius $a_\Lambda$. Excluded for $\varepsilon\le\varepsilon_*(M)$.

None fires. The obstruction would need curvature of the order of $a_\Lambda$, which is outside the admitted regime once $a_\Lambda$ is chosen after $M$. The proof follows.

## 3. The reference problem, the slice and the class

Level-$k$ units throughout: $\mathbb T^{(k)}$ has unit spacing, the bare lattice has spacing $\eta=L^{-k}$, a top $y$ has scale $\xi_y\le1$. On $\mathfrak{su}(2)$ (traceless Hermitian $2\times2$ matrices, also their complexification) $\lvert\cdot\rvert$ is the operator norm; for $Z=z\cdot\sigma$, $\lvert Z\rvert=\lvert z\rvert$ and $\tfrac12\operatorname{tr}Z^2=\lvert Z\rvert^2$. $a_p(U)=1-\tfrac12\operatorname{Re}\operatorname{tr}U_p$, $A=\sum_pa_p$.

**The problem.** $X$ is a component of the class at level $k$, $\Lambda^{\rm pr}$ its box (side $\le C_\Lambda M$), $\Lambda:=\Lambda^{\rm pr}\cap\mathbb T^{(k)}$ its sites. The localised problem of $X$ (SA 9786, Theorem 6(c)) has determining bonds: the level-$k$ bonds of $X$ off its collar, and the collar tower, whose data are the lift of the level-$k$ field (the value $\mathbf 1$ inside a block, $V(c)$ on a bond from the block of $c_-$ into that of $c_+$). Its datum is therefore a function of the level-$k$ field $V$ on $X$ alone. A lifted test loop has the holonomy of a level-$k$ plaquette or of a closed loop inside one block (value $\mathbf 1$), so its error is at most the largest level-$k$ plaquette error. Write $U_{k,X}(V)=\Phi(V)$ for its background (P81) and
\[
 f(V):=A(U_{k,X}(V)).
\]

**Variables, class.** $\mathsf B_{\rm var}$ is the set of level-$k$ bonds with an end point in $\Lambda$; $n_b:=\lvert\mathsf B_{\rm var}\rvert\le8(C_\Lambda M+1)^4$. $\Lambda^+$ is the set of level-$k$ sites within $\ell^\infty$-distance $1$ of $\Lambda$, and $S$ the set of level-$k$ plaquettes with all four corners in $\Lambda^+$. A plaquette containing a variable bond has a corner in $\Lambda$, hence lies in $S$; every other test loop is a function of the exterior data alone. Hypothesis (H$_\varepsilon$): every level-$k$ plaquette with no variable bond has $\lvert V_p-1\rvert<\varepsilon$. The class $\mathcal K(a)$ is the set of $V$ with exterior data fixed and $\lvert V_p-1\rvert<a$ for $p\in S$. For a datum write $\alpha(V)$ for its datum norm (largest test-loop error); on $\mathcal K(a)$, $\alpha(V)<\max(a,\varepsilon)$ by the remark on lifts. Gauge transformations $u$ at the sites of $\Lambda$ act only on variable bonds, and $f(V^u)=f(V)$ by covariance of the average and gauge invariance of $A$.

**Trees.** $T$ is the tree of $\delta_{\rm ax}$ on $\Lambda$ and $e_0=(x_0,z_0)$ the external bond of $T_0$, $x_0\in\Lambda$, $z_0\in\Lambda^+\setminus\Lambda$. The shell $\Lambda^+\setminus\Lambda$ is the set of sites of the boundary of a lattice cube of side $\ge3$ in dimension four; it is connected through its own bonds, so it has a spanning tree $T_{\rm ext}$ of exterior bonds. $T^*:=T\cup\{e_0\}\cup T_{\rm ext}$ is a spanning tree of $\Lambda^+$ (two trees glued at the single site $z_0$). For a bond $b$ of $\Lambda^+$ not in $T^*$, $\gamma_b$ is its fundamental cycle in $T^*$: $b$ followed by the tree path back.

**Lemma G (slice).** Each gauge orbit of variable data meets $\Sigma:=\{V:V=\mathbf 1\text{ on }T\cup\{e_0\}\}$ in exactly one point, and a point of $\Sigma$ is critical for $f$ if and only if it is critical for $f|_\Sigma$.

*Proof.* $V^u(e_0)=u(x_0)V(e_0)$ ($z_0\notin\Lambda$ is not transformed), so $V^u(e_0)=\mathbf 1$ forces $u(x_0)=V(e_0)^{-1}$; along $T$ outward from $x_0$, $u(x)V(x,x')u(x')^{-1}=\mathbf 1$ forces $u(x')=u(x)V(x,x')$. Every site of $\Lambda$ is reached once, so $u$ exists and is unique. Linearising, the map from $\mathfrak{su}(2)$-valued functions on $\Lambda$ to variations on $T\cup\{e_0\}$ is triangular with invertible diagonal, so every tangent vector at $V\in\Sigma$ is a gauge direction plus a tangent vector of $\Sigma$. $f$ has zero derivative along gauge directions. $\square$

**Coordinates.** For $b\in\mathsf B_{\rm var}\setminus(T\cup\{e_0\})$ write $\gamma_b=b\cdot\pi_b$ and let $R_b$ be the transport of $V$ along $\pi_b$: it uses only bonds of $T\cup\{e_0\}$ (value $\mathbf 1$ on $\Sigma$) and of $T_{\rm ext}$ (exterior data), so it does not depend on the variables. The *centre* $V^{\rm c}\in\Sigma$ is $V^{\rm c}(b):=R_b^{-1}$, and every $V\in\Sigma$ is $V=e^{iu}V^{\rm c}$ with $u(b)=\tfrac1i\log(V(b)R_b)=\tfrac1i\log\operatorname{hol}_{\gamma_b}(V)$. Put $\varphi(u):=f(e^{iu}V^{\rm c})$.

**Surfaces.** Fix a corner $o$ of $\Lambda^+$ and, for a site $x$, the axial path $P(x)$ from $o$ (directions $1,2,3,4$ in turn); it stays in the cube $\Lambda^+$. For a bond $e=(v,v+e_\mu)$ the closed path $P(v)\,e\,P(v+e_\mu)^{-1}$ bounds a staircase strip of at most $3(C_\Lambda M+3)$ plaquettes of $\Lambda^+$, all in $S$: the two axial paths agree in the directions before $\mu$ and run at distance one in the directions after $\mu$. A closed path $\gamma$ of $\Lambda^+$ is the product of these triangles over its bonds, so it bounds a surface $\Sigma_\gamma$ of at most $\lvert\gamma\rvert\cdot3(C_\Lambda M+3)$ plaquettes of $S$, and its holonomy is an ordered product of conjugated plaquette holonomies of those plaquettes. Fundamental cycles have length $\le\lvert\Lambda^+\rvert+1$, so
\[
 \lvert\Sigma_{\gamma_b}\rvert\le A_M:=3(C_\Lambda M+3)\big((C_\Lambda M+3)^4+1\big).
\]
For unitary matrices $\lvert\prod_iW_i-1\rvert\le\sum_i\lvert W_i-1\rvert$, and conjugation preserves $\lvert W-1\rvert$.

**Lemma S (class and ball).** Let $\varepsilon\le a\le\tfrac1{8A_M}$. (i) If $V\in\Sigma\cap\mathcal K(a)$ then $\lvert u\rvert_\infty\le2A_Ma=:\rho_1(a)$. (ii) $\lvert V^{\rm c}_p-1\rvert\le C_{\rm c}(M)\varepsilon$ for $p\in S$, with $C_{\rm c}(M)=4C_{\rm sh}(M)$ and $C_{\rm sh}(M)$ the area constant of loops in the shell, defined in the proof. (iii) If $\lvert u\rvert_\infty\le\rho\le\tfrac14$ then $\alpha(e^{iu}V^{\rm c})\le C_{\rm c}(M)\varepsilon+8\rho$.

*Proof.* (i) $\lvert\operatorname{hol}_{\gamma_b}(V)-1\rvert\le\sum_{p\in\Sigma_{\gamma_b}}\lvert V_p-1\rvert<A_Ma\le\tfrac18$, and $\lvert\log W\rvert\le2\lvert W-1\rvert$ on that ball. (ii) Write $\partial p$ as a product of conjugated fundamental cycles of its bonds not in $T^*$, times a closed path in the tree $T^*$, which is trivial. Variable non-tree bonds contribute $\operatorname{hol}_{\gamma_b}(V^{\rm c})=\mathbf 1$. An exterior non-tree bond $e$ of the shell has $\gamma_e$ inside the shell (the tree path between two shell sites is in $T_{\rm ext}$), of length $\le\lvert\partial Q\rvert+1\le8(n+1)^3+1$, where $Q=\Lambda^+$ is a cube of side $n:=C_\Lambda M+3$ and $\partial Q=\Lambda^+\setminus\Lambda$. *Shell filling:* a closed path $\gamma$ of $\partial Q$ is a product of at most $40n(n+1)^2\lvert\gamma\rvert$ conjugated boundaries of plaquettes of $\partial Q$. Indeed: in a three-dimensional face the axial triangles give at most $2n$ plaquettes per bond. Let $R$ be $\partial Q$ minus the open top face $\{x_4=n,\ 0<x_1,x_2,x_3<n\}$; for $v\in R$ let $\delta(v)$ drop straight down to $x_4=0$ inside its side face. For a bond $e=(v,v')$ of $R$, $\delta(v)^{-1}e\,\delta(v')\,\bar e^{-1}$ ($\bar e$ the bond below at height $0$) is trivial if $e$ is vertical and bounds a vertical strip of $\le n$ plaquettes of one side face if $e$ is horizontal; so a loop in $R$ is filled by $\le n$ plaquettes per bond plus a filling of its projection in the bottom face, in all $\le3n\lvert\gamma\rvert$. A general loop is first moved into $R$: each excursion $\sigma$ through the open top face, between rim points $r,r'$, is replaced by a path $\tau$ in the rim (the boundary of a three-cube, $\le6(n+1)^2$ sites), at the cost of filling $\sigma\tau^{-1}$ in the closed top face; there are at most $\lvert\gamma\rvert/2$ excursions. Adding up gives the bound. All these plaquettes have no variable bond, so $\lvert\operatorname{hol}_{\gamma_e}-1\rvert\le C_{\rm sh}(M)\varepsilon$ with $C_{\rm sh}(M):=40n(n+1)^2(8(n+1)^3+1)$. A plaquette has at most four non-tree bonds. (iii) $\lvert e^{iu}-1\rvert\le2\lvert u\rvert$; each plaquette of $S$ has at most four variable bonds; the other test loops are exterior or lifts. $\square$

Thus $\Sigma\cap\mathcal K(a)\subset\{\lvert u\rvert_\infty<\rho_1(a)\}$, a convex set, and $\{\lvert u\rvert_\infty\le2\rho_1(a)\}$ consists of data with $\alpha\le C_{\rm c}(M)\varepsilon+32A_Ma$.

## 4. Two exact linear facts

**Lemma E (energy of the linearised averages, every depth).** Let $K$ be the derivative at $U=\mathbf 1$ of one step of the actual block map (QC3), on the unscaled bond logarithms of the finer lattice, and $K^{(k)}=K\circ\cdots\circ K$ ($k$ factors), the derivative of $\mathcal M^k$ at $\mathbf 1$. For a set $S'$ of level-$k$ plaquettes let $\mathcal N_0(S')$ be the bare plaquettes in its ancestor rectangles (the $L\times L$ squares of (6.2) below, iterated). Then for every $\mathfrak{su}(2)$-valued bare $1$-form $Y$,
\[
 \sum_{p'\in S'}\lvert d_k(K^{(k)}Y)(p')\rvert^2\le\sum_{p\in\mathcal N_0(S')}\lvert dY(p)\rvert^2 ,
 \tag{4.1}
\]
where $d$ is the oriented lattice curl $Y(b_1)+Y(b_2)-Y(b_3)-Y(b_4)$ on each lattice. No constant depends on $k$.

*Proof.* One step, at a positive coarse plaquette $p'=(y;\mu\nu)$ with bonds $c_1=(y,y+Le_\mu)$, $c_2=(y+Le_\mu,y+Le_\mu+Le_\nu)$, $c_3=(y+Le_\nu,y+Le_\nu+Le_\mu)$, $c_4=(y,y+Le_\nu)$. By (QC15) (SA 8177-8189: the derivative of the contour mean at the identity is the arithmetic mean, and the derivative of $U[c]$ cancels in each closed logarithm), $(Ka)(y,y')=\sigma_a(y)+L^{-4}\sum_{x\in B(y)}a([x,x+Le_\mu])-\sigma_a(y')$. In $(Ka)(c_1)+(Ka)(c_2)-(Ka)(c_3)-(Ka)(c_4)$ the eight $\sigma$ terms cancel in pairs. Since $B(y+Le_\mu)=B(y)+Le_\mu$, the rest is $L^{-4}\sum_{x\in B(y)}$ of the oriented sum of $a$ around the $L\times L$ square with corner $x$ in the $\mu\nu$ plane, which by the abelian Stokes identity is the sum of $da$ over its $L^2$ plaquettes, all of orientation $\mu\nu$. So
\[
 d(Ka)(p')=(P\,da)(p'),\qquad (Pf)(y;\mu\nu)=L^{-4}\sum_{x\in B(y)}\sum_{r,s=0}^{L-1}f(x+re_\mu+se_\nu;\mu\nu),
 \tag{6.2}
\]
the matrix of `sa-2.13-2.md` (6.2), now as an exact linear identity with nonnegative entries. Row sums are $L^2$. A fine plaquette $(z;\mu\nu)$ occurs for $L^2$ pairs $(r,s)$, each fixing $x$ and hence the unique block $B(y)\ni x$, with weight $L^{-4}$: column sums are $L^{-2}$. Schur's test gives $\lVert P\rVert_{2\to2}\le(L^2\cdot L^{-2})^{1/2}=1$, also for $\mathbb R^3$-valued vectors since $\lvert Pf\rvert\le P\lvert f\rvert$ entrywise. Iterate $k$ times (the chain rule at the identity at every level) and restrict the rows to $S'$ and the columns to the entries those rows read. $\square$

This is the step `sa-2.13-2.md` Section 7 found missing between a tree curl inequality and the freed Hessian: the freed Hessian at flat data is a minimum of $\lVert dY\rVert^2$ over fine extensions of the box datum, and (4.1) bounds it below by the level-$k$ curl energy of that datum, with constant one at every depth.

**Lemma P (tree Poincaré inequality at level $k$).** Let $w$ be $\mathfrak{su}(2)$-valued on $\mathsf B_{\rm var}$ with $w=0$ on $T\cup\{e_0\}$, and $w^0$ the level-$k$ $1$-form on the bonds of $\Lambda^+$ equal to $w$ on variable bonds and $0$ on the others. Then
\[
 \lVert w\rVert_2^2\le C_{\rm P}(M)\sum_{p\in S}\lvert dw^0(p)\rvert^2,\qquad C_{\rm P}(M):=n_bA_M^2 .
 \tag{4.2}
\]

*Proof.* For a variable bond $b\notin T\cup\{e_0\}$, $w^0$ vanishes on every bond of $\gamma_b$ but $b$ (bonds of $T\cup\{e_0\}$ by hypothesis, bonds of $T_{\rm ext}$ because they are exterior). So $\pm w(b)$ is the oriented sum of $w^0$ around $\gamma_b$, which is the oriented sum of $dw^0$ over the $2$-chain $\Sigma_{\gamma_b}$ of Section 3 (its boundary is $\gamma_b$, by the telescoping of the axial triangles). With multiplicities, $\Sigma_{\gamma_b}$ has $N_b\le A_M$ plaquettes, so $\lvert w(b)\rvert^2\le A_M\sum_{p}m_b(p)\lvert dw^0(p)\rvert^2$, and $\sum_bm_b(p)\le n_bA_M$. $\square$

Balaban's constant for the axial tree is $CM^5$ (outline, SA 17656); (4.2) is cruder and suffices, since only its dependence on $M$ alone is used.

## 5. The freed problem: envelope, second variation, multipliers

Fix a real datum $V$ of the reference problem with $\alpha(V)<\bar\varepsilon$ and let $U=\Phi(V)$, real, regular, $r(U)\le B\alpha(V)$ (P81, (8.2)). For every determining bond $c$ (level-$k$ rows and tower rows) put
\[
 \tilde q_c(U'):=\tfrac1i\log\big[(M_{\mathbf B}U')(c)\,V(c)^{-1}\big],
\]
defined for $U'$ near $U$ (raw rows, left logarithms). Fine variations are left variations $e^{iY}U'$, $Y$ an unscaled bare $\mathfrak{su}(2)$-valued $1$-form; $Y=\eta h$ with $h$ the continuum potential. $\operatorname{Hess}A(U)[Y,Y]:=\frac{d^2}{ds^2}A(e^{isY}U)|_0$, and likewise $D^2\tilde q_c(U)[Y,Y]$.

**Lemma V (envelope and second variation).** (a) There is a unique family $\lambda=(\lambda_c)$, $\lambda_c\in\mathfrak{su}(2)$, with $DA(U)[Y]=\sum_c\operatorname{tr}(\lambda_c\,D\tilde q_c(U)[Y])$ for every $Y$. (b) For $w$ on $\mathsf B_{\rm var}$, $\frac d{dt}f(e^{itw}V)|_0=\sum_{c\in\mathsf B_{\rm var}}\operatorname{tr}(\lambda_cw_c)$. (c) With $Y_1:=\frac d{dt}\big|_0\tfrac1i\log\big(\Phi_V(tw)U^{-1}\big)$ (bond by bond),
\[
 h_V(w):=\frac{d^2}{dt^2}f(e^{itw}V)\Big|_0=\operatorname{Hess}A(U)[Y_1,Y_1]-\sum_c\operatorname{tr}\big(\lambda_c\,D^2\tilde q_c(U)[Y_1,Y_1]\big).
 \tag{5.1}
\]

*Proof.* P81 gives the holomorphic chart $\Phi_V$ on $\lVert B\rVert_\infty<r_{\rm B}$ with $M_{\mathbf B}\Phi_V(B)=e^{iB}V$, so $\tilde q\circ\Phi_V(B)=B$ for small $B$ and $D\tilde q(U)\circ D\Phi_V(0)=\mathrm{id}$: $D\tilde q(U)$ is onto, the fibre $\{\tilde q=0\}$ is a submanifold near $U$ with tangent space $\ker D\tilde q(U)$, and $U$ is critical on it (P81: the background is a critical configuration of the constrained problem). A linear form vanishing on the kernel of a surjection factors through it, uniquely: (a). For (b) and (c) let $U(t)=\Phi_V(tw)$ (data $e^{itw}V$ on $\mathsf B_{\rm var}$, $V$ elsewhere); by gauge invariance $f(e^{itw}V)=A(U(t))$. Write $U(t)=e^{iY(t)}U$, $Y$ holomorphic, $Y(0)=0$, $Y'(0)=Y_1$. Exactly, $\tilde q(U(t))=tw$ on $\mathsf B_{\rm var}$ and $0$ on the other rows. Differentiating $A(e^{iY(t)}U)$ once gives $DA(U)[Y_1]=\sum\operatorname{tr}(\lambda_cD\tilde q_c[Y_1])=\sum_{\mathsf B_{\rm var}}\operatorname{tr}(\lambda_cw_c)$. Differentiating twice gives $\operatorname{Hess}A(U)[Y_1,Y_1]+DA(U)[Y''(0)]$, and differentiating $\tilde q(e^{iY(t)}U)=tw$ twice gives $D^2\tilde q[Y_1,Y_1]+D\tilde q[Y''(0)]=0$; insert (a). $\square$

So the gradient of $f$ in the box variables is the box part of the multiplier, and the freed-average Hessian is the Lagrangian Hessian, with the full multiplier, evaluated on the linearised background of the box datum. At a critical point of $f$ the box multipliers vanish and only the exterior ones remain. $Y_1=\eta h$ with $h=\sum_{c\in\mathsf B_{\rm var}}h_{c,w_c}$, the superposition of the T4 responses (the derivative is linear in the datum direction).

**Lemma BC$'$ (single-top count).** Under GEO4 ($\operatorname{dist}(\Omega_j^c,\Omega_{j+1})\ge c_g\xi_j$, $64\log L\le\theta\min(M,\rho)\le\theta c_g$), for every top $y_c$ of the reference problem,
\[
 \sum_{\text{tops }y}e^{-\theta d_{\mathbf B}(y,y_c)}\le C_{\rm BC'}:=\sum_{R\ge0}\Big(\tfrac{2(R+1)}{c_g}+3\Big)\Big(2(R+1)L^{2(R+1)/c_g+2}+3\Big)^4e^{-\theta R}<\infty .
\]

*Proof.* A path of $d_{\mathbf B}$-length $<R+1$ from $y_c$ (level $q$) reaches only levels $j$ with $\lvert j-q\rvert\le(R+1)/c_g+1$: between levels it crosses each intermediate layer, at cost $\ge c_g$ (step 1 of the proof of Lemma BC). Its Euclidean length is at most $R+1$ times the largest scale met, $\le\xi_qL^{(R+1)/c_g+1}$. Level-$j$ tops form a lattice of spacing $\xi_j\ge\xi_qL^{-\lvert j-q\rvert}$, so at most $(2(R+1)L^{2(R+1)/c_g+2}+3)^4$ of them lie in that Euclidean ball, for each of at most $2(R+1)/c_g+3$ levels. Sum over $R$: the $R$-th term is at most a polynomial in $R$ times $L^{8(R+1)/c_g}e^{-\theta R}$, and $8\log L/c_g\le\theta/8$ by $64\log L\le\theta c_g$, so the series converges. $\square$

For a top in $\Omega_k$ this is also Lemma BC with $E=\{y_c\}$.

**Lemma M (multipliers).** For every determining bond $c$, $\lvert\lambda_c\rvert\le C_{\rm M}\,r(U)$ with $C_{\rm M}:=4L^3C_4C_{\rm BC'}$.

*Proof.* For $\lvert e\rvert=1$ at $c$, Lemma V(a) with $Y=\eta h_{c,e}$ (the response to the datum direction $e$ at $c$, for which $D\tilde q[\eta h_{c,e}]=e$ at $c$ and $0$ elsewhere) gives $\operatorname{tr}(\lambda_ce)=DA(U)[\eta h_{c,e}]=\langle J(U),h_{c,e}\rangle_{\rm f}=\eta^4\sum_b\operatorname{tr}(J(U)(b)h_{c,e}(b))$; $J$ is the left-variation gradient in the fine pairing (`a3-derivative.md` 7.3). Group the bare bonds by tops: a top $y$ carries at most $4(\xi_y/\eta)^4$ bonds, each of scale within a factor $L$ of $\xi_y$, so $\lvert J(b)\rvert\le r(U)L^3\xi_y^{-3}$ (P81) and $\lvert h_{c,e}(b)\rvert\le C_4\xi_y^{-1}e^{-\theta d_{\mathbf B}(y,y_c)}$ (T4 at the real critical reference $U$, $B=0$). With $\lvert\operatorname{tr}(XY)\rvert\le2\lvert X\rvert\lvert Y\rvert$, $\lvert\operatorname{tr}(\lambda_ce)\rvert\le8L^3C_4r(U)\sum_ye^{-\theta d_{\mathbf B}(y,y_c)}$; and $\sup_{\lvert e\rvert=1}\operatorname{tr}(\lambda e)=2\lvert\lambda\rvert$. Apply Lemma BC$'$. $\square$

The cancellation that makes this volume- and depth-free is in $J$: the force on a bare bond is $\eta^3J$, of order $\eta^3r(U)$, not the $\eta^2r(U)$ of a single plaquette. Lemma M agrees with `a3-derivative.md` Section 7 ($\lvert\omega\rvert_Y\le C(\kappa+r)$), here derived from the envelope identity.

**Lemma R (rows).** Let $c$ be a determining bond of scale $s$ with carrier $S_c$, and $U'$ a real reference with $r(U')\le\bar\varepsilon$ (or $U'=\mathbf 1$). The map $a\mapsto\tilde q_c(e^{i\eta a}U')-\tilde q_c(U')$ (complex $a$) is holomorphic on $\{s\sup_{S_c}\lvert a\rvert<r_*\}$ and bounded there by a constant $C_{\rm R}(L)$. Consequently, for $s\sup_{S_c}\lvert h\rvert\le r_*/4$ and $s\sup_{S_c}\lvert a\rvert\le r_*/4$,
\[
 \lvert D^2\tilde q_c(U')[\eta h,\eta h]\rvert\le\tfrac{3C_{\rm R}}{r_*^2}(s\sup_{S_c}\lvert h\rvert)^2,\qquad
 \big\lvert D\tilde q_c(e^{i\eta a}\mathbf 1)[\eta h]-K^{(k)}_c[\eta h]\big\rvert\le C'_{\rm R}\,(s\sup_{S_c}\lvert a\rvert)(s\sup_{S_c}\lvert h\rvert),
 \tag{5.2}
\]
with $C'_{\rm R}=C'_{\rm R}(L)$; by homogeneity the first bound holds for every $h$.

*Proof.* The row is the $k$-step recursion (6)-(8) of `a3-derivative.md` 4.1 with its accumulated endpoint factors; under $s\sup\lvert a\rvert\le r_*$ the recursion stays in its fixed analytic ball ($\lvert a_r\rvert\le2r_*t_r$) and the endpoint factors have condition number at most $2$, so the group-valued row stays in a fixed ball about its reference value and its left logarithm is holomorphic and bounded by a constant. For the first bound apply the one-variable Cauchy estimate to $z\mapsto\tilde q_c(e^{iz\eta h}U')$ on $\lvert z\rvert=r_*/(2s\sup\lvert h\rvert)$, which keeps the $a$-ball. For the second, let $F(a):=\tfrac1i\log(\mathcal M^k(e^{i\eta a})(c))$ at the flat reference; $DF(0)=K^{(k)}_c\eta$. A left variation $e^{is\eta h}$ at the base $e^{i\eta a}$ is the additive variation $h+O(\eta\lvert a\rvert\lvert h\rvert)$ of $a$ (Baker-Campbell-Hausdorff on each bare bond), and the left logarithm of the row at $F(a)$ differs from $F$ by a factor $1+O(\lvert F(a)\rvert)$ with $\lvert F(a)\rvert\le C s\sup\lvert a\rvert$ (Schwarz's lemma on the bounded holomorphic $F$). Finally $\lvert DF(a)[h]-DF(0)[h]\rvert\le\sup_{t\le1}\lvert D^2F(ta)[a,h]\rvert$, bounded by the two-variable Cauchy estimate on the same ball by $C(s\sup\lvert a\rvert)(s\sup\lvert h\rvert)$. $\square$

No gradient of $a$ is needed: the radius condition of the recursion is on $s\sup\lvert a\rvert$ only.

**Lemma N (local axial gauge).** Let $N$ be the union of the level-$k$ blocks of the sites of $\Lambda^+$: a bare cube of side $\ell_N:=C_\Lambda M+4$ (level-$k$ units), inside the level-$k$ part of the localised problem. There is a gauge transformation $g$ with $U^g=e^{i\eta A_g}$ on the bare bonds of $N$ and
\[
 \lvert A_g\rvert\le\bar a:=6\ell_NB\alpha(V).
\]

*Proof.* Complete axial gauge in $N$ from a corner, on the bare lattice; extend $g$ arbitrarily outside $N$ (only covariance is used there). A bare bond $b$ of $N$ off the axial tree has $U^g(b)$ equal to the holonomy of its axial triangle, which bounds a staircase strip of at most $3\ell_N/\eta$ bare plaquettes of $N$, each with $\lvert U_p-1\rvert\le B\alpha\eta^2$ (P81 (8.2), $\mathsf L(p)=1$ in the level-$k$ part). So $\lvert U^g(b)-1\rvert\le3\ell_NB\alpha\eta$, and $\lvert\log W\rvert\le2\lvert W-1\rvert$. $\square$

**Plaquette Hessian.** For a plaquette $p=b_1b_2b_3^{-1}b_4^{-1}$ and left variations $Y_i$ of its bonds, moving all factors of $U_p(t)$ to the left gives $U_p(t)=e^{itZ_1}e^{itZ_2}e^{itZ_3}e^{itZ_4}U_p$ with $Z_1=Y_1$, $Z_2=\operatorname{Ad}(U_1)Y_2$, $Z_3=-\operatorname{Ad}(U_1U_2U_3^{-1})Y_3$, $Z_4=-\operatorname{Ad}(U_p)Y_4$. Put $d_UY(p):=\sum_iZ_i$. By Baker-Campbell-Hausdorff, $e^{itZ_1}\cdots e^{itZ_4}=e^{iW(t)}$ with $W'(0)=\sum Z_i$, $W''(0)=i\sum_{i<j}[Z_i,Z_j]$, so, using $\operatorname{tr}[Z_i,Z_j]=0$ and $\lvert\operatorname{tr}(XE)\rvert\le2\lvert X\rvert\lvert E\rvert$,
\[
 H_p(U)[Y,Y]:=\tfrac{d^2}{dt^2}a_p(e^{itY}U)\big|_0=\lvert d_UY(p)\rvert^2+R_p,\qquad\lvert R_p\rvert\le8\lvert U_p-1\rvert\textstyle\sum_{b\in\partial p}\lvert Y(b)\rvert^2
 \tag{5.3}
\]
for real $U$ (then $\lvert Z_i\rvert=\lvert Y_i\rvert$). At $U=\mathbf 1$, $d_UY=dY$. If $U=e^{iX}$ on the bonds of $p$ with $\lvert X\rvert\le x_0\le\tfrac18$, then $\lvert\operatorname{Ad}(T)-1\rvert\le2\lvert T-1\rvert$ for unitary $T$ gives $\lvert d_UY(p)-dY(p)\rvert\le16x_0\sum_{b\in\partial p}\lvert Y(b)\rvert$. Everything is gauge covariant: $H_p(U^g)[\operatorname{Ad}(g)Y,\operatorname{Ad}(g)Y]=H_p(U)[Y,Y]$.

## 6. Theorem H: the freed-average Hessian has a uniform gap

**Theorem H.** There are $\alpha_*(M)>0$ and $c_*(M):=1/(8C_{\rm P}(M))$, depending on $M$, $L$ and the constants of P81, T4, RD, BC and GEO4 only, such that for every real datum $V$ of the reference problem with $\alpha(V)\le\alpha_*(M)$ and every $w$ on $\mathsf B_{\rm var}$ vanishing on $T\cup\{e_0\}$,
\[
 h_V(w)\ \ge\ c_*(M)\,\lVert w\rVert_2^2 .
\]
No constant depends on the depth $k$, on $X$ or its volume, on the datum or on the frame. At $V=\mathbf 1$ the bound holds with $C_{\rm P}(M)^{-1}$ in place of $c_*$, with no loss.

*Proof.* Let $U=\Phi(V)$, $\alpha=\alpha(V)$, $r=r(U)\le B\alpha$, $h=\sum_{c\in\mathsf B_{\rm var}}h_{c,w_c}$, $Y=Y_1=\eta h$, and $E:=\Lambda^+$, a set of level-$k$ tops of diameter $\le C_\Lambda M+2$ containing the tops of all variable rows. T4 at the real critical reference $U$ gives, for a bare bond $b$ assigned to the top $y_b$,
\[
 \lvert h(b)\rvert\le C_4n_b\lVert w\rVert_\infty\,\xi_{y_b}^{-1}e^{-\theta d_{\mathbf B}(y_b,E)} .
 \tag{6.1}
\]
Bonds of one plaquette, or of one row carrier, have tops within $d_{\mathbf B}$-distance $D_L$ of each other and scales within a factor $L$; $D_L$ depends on $L$ only. Split $\operatorname{Hess}A(U)[Y,Y]=\Sigma_{\rm near}+\Sigma_{\rm far}$ over $p\in\mathcal N_0(S)$ and $p\notin\mathcal N_0(S)$.

*Far plaquettes.* By (5.3), $H_p\ge-8\lvert U_p-1\rvert\sum_{\partial p}\lvert Y\rvert^2$. For $p$ assigned to the top $y$: $\lvert U_p-1\rvert\le r\eta^2L^2\xi_y^{-2}$ (P81) and $\lvert Y(b)\rvert\le\eta LC_4n_b\lVert w\rVert_\infty e^{\theta D_L}\xi_y^{-1}e^{-\theta d_{\mathbf B}(y,E)}$. A top carries at most $6(\xi_y/\eta)^4$ plaquettes, so its contribution is at most $192L^4e^{2\theta D_L}C_4^2n_b^2\,r\lVert w\rVert_\infty^2e^{-2\theta d_{\mathbf B}(y,E)}$: the powers of $\eta$ and $\xi_y$ cancel exactly. Lemma BC ($\theta'=2\theta$) gives $\Sigma_{\rm far}\ge-E_{\rm far}$ with
\[
 E_{\rm far}:=192L^4e^{2\theta D_L}C_4^2n_b^2C_{\rm BC}(C_\Lambda M+6)^4\,r\lVert w\rVert_\infty^2 .
\]

*Multiplier term.* By Lemmas M and R and (6.1), a row $c$ of scale $s_c$ with top $y_c$ contributes at most $2C_{\rm M}r\cdot3C_{\rm R}r_*^{-2}(LC_4n_b\lVert w\rVert_\infty e^{\theta D_L}e^{-\theta d_{\mathbf B}(y_c,E)})^2$ (the factor $s_c$ cancels the $\xi^{-1}$ of (6.1)); a top carries at most $8$ rows. Lemma BC bounds the sum by
\[
 E_{\rm mult}:=48C_{\rm M}C_{\rm R}r_*^{-2}L^2e^{2\theta D_L}C_4^2n_b^2C_{\rm BC}(C_\Lambda M+6)^4\,r\lVert w\rVert_\infty^2 .
\]

*Near plaquettes.* $\mathcal N_0(S)$ lies in the cube $N$ of Lemma N (ancestor rectangles of a plaquette with corners in $\Lambda^+$ lie in the blocks of those corners), in the level-$k$ part, where $\xi=1$. Use the gauge $g$ there and $Y':=\operatorname{Ad}(g)Y$, so $\lvert Y'(b)\rvert\le\eta C_4n_b\lVert w\rVert_\infty$. With $x_0=\eta\bar a\le\frac18$, (5.3) and $\lvert x+y\rvert^2\ge\frac12\lvert x\rvert^2-\lvert y\rvert^2$ give
$H_p(U)[Y,Y]=H_p(U^g)[Y',Y']\ge\tfrac12\lvert dY'(p)\rvert^2-(1024\eta^2\bar a^2+8B\alpha\eta^2)\sum_{\partial p}\lvert Y'\rvert^2$. There are at most $6\ell_N^4\eta^{-4}$ such plaquettes, so
\[
 \Sigma_{\rm near}\ge\tfrac12\sum_{p\in\mathcal N_0(S)}\lvert dY'(p)\rvert^2-E_{\rm near},\qquad
 E_{\rm near}:=24\ell_N^4(1024\bar a^2+8B\alpha)C_4^2n_b^2\lVert w\rVert_\infty^2 .
\]

*Flat comparison.* By Lemma E, $\sum_{\mathcal N_0(S)}\lvert dY'\rvert^2\ge\sum_{p'\in S}\lvert d_k(K^{(k)}Y')(p')\rvert^2$. On each level-$k$ bond $c$ of $\Lambda^+$ (a row of the problem, with carrier in $N$), covariance of the rows, $(M_{\mathbf B}U^g)(c)=g(c_-)(M_{\mathbf B}U)(c)g(c_+)^{-1}$, turns $\tilde q(\Phi_V(tw))=tw$ into $D\tilde q^{\,g}_c(U^g)[Y']=w'_c$, with $w'_c:=\operatorname{Ad}(g(c_-))w_c$ on $\mathsf B_{\rm var}$ and $0$ on exterior bonds; $w'$ vanishes on $T\cup\{e_0\}$ and $\lVert w'\rVert_2=\lVert w\rVert_2$. Lemma R (second bound, flat base, $a=A_g$, $s=1$, $\bar a\le r_*/4$) gives $K^{(k)}Y'=w'^0+m$ on the bonds of $\Lambda^+$ with $\lvert m_c\rvert\le\mu_0:=C'_{\rm R}\bar aC_4n_b\lVert w\rVert_\infty$. Hence, by Lemma P and $\lvert d_km\rvert\le4\mu_0$,
\[
 \sum_{p'\in S}\lvert d_k(K^{(k)}Y')\rvert^2\ge\tfrac12\sum_S\lvert d_kw'^0\rvert^2-16\lvert S\rvert\mu_0^2\ge\tfrac1{2C_{\rm P}(M)}\lVert w\rVert_2^2-16\lvert S\rvert\mu_0^2,\qquad\lvert S\rvert\le6(C_\Lambda M+4)^4 .
\]

*Sum.* By (5.1), $h_V(w)\ge\frac1{4C_{\rm P}}\lVert w\rVert_2^2-8\lvert S\rvert\mu_0^2-E_{\rm near}-E_{\rm far}-E_{\rm mult}$. With $r\le B\alpha$, $\bar a=6\ell_NB\alpha$ and $\alpha\le1$, every subtracted term is at most $C_5(M)\alpha\lVert w\rVert_\infty^2$, where
\[
 C_5(M):=C_4^2n_b^2\Big[24\ell_N^4\big(36864\,\ell_N^2B^2+8B\big)+288\lvert S\rvert C_{\rm R}'^2\ell_N^2B^2+\big(192L^4+48C_{\rm M}C_{\rm R}r_*^{-2}L^2\big)e^{2\theta D_L}C_{\rm BC}(C_\Lambda M+6)^4B\Big].
\]
Since $\lVert w\rVert_\infty\le\lVert w\rVert_2$, $h_V(w)\ge(\frac1{4C_{\rm P}}-C_5\alpha)\lVert w\rVert_2^2\ge c_*\lVert w\rVert_2^2$ when
\[
 \alpha\le\alpha_*(M):=\min\Big\{\bar\varepsilon,\ 1,\ \frac{r_*}{24\ell_NB},\ \frac1{48\ell_NB},\ \frac1{8C_5(M)C_{\rm P}(M)},\ \frac{2c_*(M)}{n_bC_{\rm M}BC_X}\Big\}
\]
(the last entry is used in Section 7; $C_X$ is the absolute constant there). At $V=\mathbf 1$: $U=\mathbf 1$, $\lambda=0$, $g=1$, $m=0$, and $h_{\mathbf 1}(w)=\lVert dY\rVert^2\ge\sum_S\lvert d_kw^0\rvert^2\ge C_{\rm P}^{-1}\lVert w\rVert_2^2$ exactly. $\square$

**What the identification consists of.** The freed Hessian is not the next-fibre Hessian of `a2-full.md` (that one keeps the box rows) and not the pivot chart of `a2-curved.md`. By (5.1) it is the Lagrangian Hessian on the linearised background of the box datum; near the box it is compared, in one local axial gauge, with the flat curl form, and the flat curl form dominates the level-$k$ curl energy of the datum by the exact identity (6.2) at every depth; far from the box, and in the multiplier term, only gauge-invariant pointwise quantities enter, and T4 with Lemma BC sums them without depth or volume. The tree Poincaré inequality (4.2) is the last step, not the first.

## 7. Proposition 2.4 rebuilt

Order of choice: $L$; the geometric constants ($\rho,\mu,M_1'$, GEO4); the constants of P81, T4, RD, BC (they depend on $L$ and the geometric constants); $M$ and $C_\Lambda$; then $n_b,A_M,C_{\rm P},C_{\rm c},\ell_N$ (explicit in $M$), $c_*(M)$, $\alpha_*(M)$; then
\[
 a_\Lambda:=\frac{\alpha_*(M)}{64A_M},\qquad
 C_{\rm m}(M):=\frac{8n_b^{1/2}C_{\rm M}BC_{\rm c}(M)}{c_*(M)},\qquad
 C_{2.4}(M):=C_{\rm c}(M)+8C_{\rm m}(M),
\]
\[
 \varepsilon_*(M):=\min\Big\{a_\Lambda,\ \frac{\alpha_*(M)}{2C_{\rm c}(M)},\ \frac{A_Ma_\Lambda}{C_{\rm m}(M)},\ \frac{a_\Lambda}{2C_{2.4}(M)}\Big\};
\]
then $M_0$; then the coupling ceiling, which must give $\varepsilon\le C\varepsilon_k\le\varepsilon_*(M)$ (in the application $\varepsilon\le C\varepsilon_k$, SA 17656). All of these are chosen after $M$ and before $\gamma$, as the outline requires.

**Theorem 2.4 (implication from P81, T4, RD, BC, GEO4, SEP).** Let the real exterior data of the reference problem satisfy (H$_\varepsilon$) with $\varepsilon\le\varepsilon_*(M)$. Then:

(a) On $\mathcal K(a_\Lambda)$ the background $U_{k,X}(V)$ exists, and $f(V)=A(U_{k,X}(V))$ has exactly one critical gauge orbit $\mathcal O_\Lambda$ meeting $\mathcal K(a_\Lambda)$. It is the set of minima of $f$ on $\mathcal K(a_\Lambda)$, and the minimum is strict modulo gauge: $f(V)\ge f(V_\Lambda)+\frac{c_*}4\lvert u(V)-u_\Lambda\rvert_2^2$ in the coordinates of Section 3.

(b) Its representative $V_\Lambda$ that equals $\mathbf 1$ on $T\cup\{e_0\}$ satisfies $\lvert\partial V_\Lambda(p)-\mathbf 1\rvert\le C_{2.4}(M)\varepsilon$ for $p\in S$, so $\alpha(V_\Lambda)\le C_{2.4}(M)\varepsilon$, and $U_0:=U_{k,X}(V_\Lambda)$ has $\lvert\partial U_0(p)-\mathbf 1\rvert\le BC_{2.4}(M)\varepsilon\,\eta^2\mathsf L(p)^{-2}$ and $\lvert J(U_0)(b)\rvert\le BC_{2.4}(M)\varepsilon\,\mathsf L(b)^{-3}$ everywhere.

(c) $\lambda_c(V_\Lambda)=0$ for every $c\in\mathsf B_{\rm var}$. Hence $J(U_0)(b)=0$ at every bare bond $b$ with both end points in $\bigcup_{y\in\Lambda}B^k(y)$, and at every bare bond from such a block into an adjacent block: $J(U_0)=0$ in $\Lambda^{\rm pr}$.

(d) In $\delta_{\rm ax}$ gauge the Hessian is bounded below: $\frac{d^2}{dt^2}f(e^{itw}V_\Lambda)|_0=h_{V_\Lambda}(w)\ge c_*(M)\lVert w\rVert_2^2$ for $w=0$ on $T\cup\{e_0\}$; and $\varphi$ is $\frac{c_*}2$-convex on $\{\lvert u\rvert_\infty\le4A_Ma_\Lambda\}$.

(e) $V_\Lambda$ is real-analytic in the exterior data and continues holomorphically (Theorem C).

*Proof.* Put $\rho_1=2A_Ma_\Lambda$, $\rho_2=2\rho_1=\alpha_*/16\le\frac1{16}$.

1. *Class and room.* By Lemma S(i), $\Sigma\cap\mathcal K(a_\Lambda)\subset\{\lvert u\rvert_\infty<\rho_1\}$. By Lemma S(iii), every $V(u)=e^{iu}V^{\rm c}$ with $\lvert u\rvert_\infty\le\rho_2$ has $\alpha(V(u))\le C_{\rm c}\varepsilon+8\rho_2\le\frac{\alpha_*}2+\frac{\alpha_*}2$, so P81 gives its background and Theorem H applies to it.

2. *Convexity.* For $\lvert u\rvert_\infty<\rho_2$ and $w$ vanishing on $T\cup\{e_0\}$ write $e^{i(u+tw)}e^{-iu}=e^{iX(t)}$ bond by bond. Then $X'(0)=\Psi(\operatorname{ad}iu)w$ with $\Psi(z)=(e^z-1)/z$, so $\lvert X'(0)-w\rvert\le4\lvert u\rvert\lvert w\rvert$; and $\lvert X''(0)\rvert\le C_X\lvert u\rvert\lvert w\rvert^2$ with an absolute $C_X$ ($X''(0)$ is holomorphic in $u$ on $\lvert u\rvert\le\frac14$, vanishes at $u=0$ where $X(t)=tw$, and is bounded there by the Cauchy estimate in $t$; Schwarz's lemma in $u$). Both vanish on $T\cup\{e_0\}$. With $g(Z):=f(e^{iZ}V(u))$, $\frac{d^2}{dt^2}\varphi(u+tw)=D^2g(0)[X',X']+Dg(0)[X'']=h_{V(u)}(X'(0))+\sum_c\operatorname{tr}(\lambda_c(V(u))X''(0)_c)$ by Lemma V. Theorem H and Lemma M give
\[
 \tfrac{d^2}{dt^2}\varphi(u+tw)\ge c_*(1-4\rho_2)^2\lVert w\rVert_2^2-2n_bC_{\rm M}B\alpha_*C_X\rho_2\lVert w\rVert_\infty^2\ge\tfrac{c_*}2\lVert w\rVert_2^2 ,
\]
using $\rho_2\le\frac1{16}$ and the last entry of $\alpha_*$ (it makes $2n_bC_{\rm M}B\alpha_*C_X\rho_2\le c_*/4$).

3. *Existence.* By Lemmas V(b) and M and $r(\Phi(V^{\rm c}))\le B\alpha(V^{\rm c})\le BC_{\rm c}\varepsilon$, $\lvert\nabla\varphi(0)\rvert_2\le2n_b^{1/2}C_{\rm M}BC_{\rm c}\varepsilon$. On the convex set $\{\lvert u\rvert_\infty<\rho_2\}$, step 2 gives $\varphi(u)\ge\varphi(0)+\nabla\varphi(0)\cdot u+\frac{c_*}4\lvert u\rvert_2^2$, so $\varphi(u)>\varphi(0)$ once $\lvert u\rvert_2>4\lvert\nabla\varphi(0)\rvert_2/c_*$. A minimiser $u_\Lambda$ of the continuous $\varphi$ on the compact $\{\lvert u\rvert_\infty\le\rho_1\}$ therefore has $\lvert u_\Lambda\rvert_\infty\le\lvert u_\Lambda\rvert_2\le C_{\rm m}\varepsilon\le A_Ma_\Lambda<\rho_1$: it is interior, so $\nabla\varphi(u_\Lambda)=0$, and $V_\Lambda:=V(u_\Lambda)$ is critical for $f$ (Lemma G).

4. *Uniqueness and minimality.* If $u_1,u_2$ are critical in $\{\lvert u\rvert_\infty<\rho_2\}$, then $0=(\nabla\varphi(u_2)-\nabla\varphi(u_1))\cdot(u_2-u_1)\ge\frac{c_*}2\lvert u_2-u_1\rvert_2^2$. Every critical orbit meeting $\mathcal K(a_\Lambda)$ has its slice point in $\{\lvert u\rvert_\infty<\rho_1\}$ (step 1, Lemma G), so it is $\mathcal O_\Lambda$. For $V\in\mathcal K(a_\Lambda)$, convexity on the segment from $u_\Lambda$ to $u(V)$ gives the strict inequality of (a).

5. *Bounds.* For $p\in S$, $\lvert V_\Lambda(p)-1\rvert\le\lvert V^{\rm c}_p-1\rvert+8\lvert u_\Lambda\rvert_\infty\le(C_{\rm c}+8C_{\rm m})\varepsilon$ (Lemma S(ii)); the other test loops are below $\varepsilon$. So $V_\Lambda\in\mathcal K(a_\Lambda)$ (by $\varepsilon\le a_\Lambda/(2C_{2.4})$) and P81 (8.2) gives the background bounds of (b).

6. *Vanishing current.* $f$ is critical at $V_\Lambda$ in every variable direction (Lemma G), so by Lemma V(b) $\sum_{\mathsf B_{\rm var}}\operatorname{tr}(\lambda_cw_c)=0$ for all $w$, i.e. $\lambda_c=0$ on $\mathsf B_{\rm var}$, and $DA(U_0)=\sum_{c\notin\mathsf B_{\rm var}}\operatorname{tr}(\lambda_cD\tilde q_c)$. A level-$k$ row $(y,y')$ reads the bare bonds of the pillars of $B^k(y)\cup B^k(y')$ and the straight crossings between them; internal contours stay in one block and a crossing between blocks adjacent in direction $\mu$ is parallel to $e_\mu$ and lies on the segments of that row only (SA 8167-8176), at every level of the hierarchy. A bare bond with both end points in $B^k(y)$, $y\in\Lambda$, is therefore read only by rows with an end point at $y$, all variable; a bare bond crossing from $B^k(y)$ into $B^k(y'')$ only by the row $(y,y'')$, variable. Tower rows lie at distance $\ge2M\check R-M$ (GEO1). So $J(U_0)(b)=0$ there.

7. *Hessian.* (d) is Theorem H at $V_\Lambda$ and step 2. (e) follows from Theorem C below (real points of the holomorphic branch are the critical points of this theorem). $\square$

**Comparison with the outline and the consumers.** Every clause of SA 17656 holds as an implication, with $C(M)=C_{2.4}(M)$, $c(M)=c_*(M)$ and the class radius $a_\Lambda$ fixed after $M$; the constants are cruder than Balaban's $CM^5$, $cM^{-5}$, which no consumer reads. The consumers read: I4 of `sa-2.8-terms.md` (uniqueness and minimality in the mild class, $\lvert\partial S_p-\mathbf 1\rvert\le C(M)\varepsilon_k\eta^2$, the axial gap): (a), (b), (d). The Lagrange form used by Lemma LM there ($\lambda_\Lambda=0$): (c). The (D-F) and I5 entry "the new box at $(C(M)+4M_0)\varepsilon_k$": (b) with the cutoff $\lvert u'\rvert<M_0\varepsilon_k$, by Lemma S(iii). The healing step's "$U_0$ belongs to the domain of the carried tests" (SA 17622) reads (b). Not supplied here, and not part of Proposition 2.4: the claim of `sa-2.8-terms.md` 2.2(c) that $A(P_X(0))\ge A(U_{k,X}(\mathcal M^kP_X(0)))$, which needs the background to minimise over a class containing $P_X(0)$; its gate already replaced that step by the sign-free decomposition.
