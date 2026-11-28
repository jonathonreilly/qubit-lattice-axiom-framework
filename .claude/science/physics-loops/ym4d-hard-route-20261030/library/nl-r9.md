# nl-r9: nonlinear bounds for the current-corrected first system
Provenance: Codex (GPT-6 family; requested effort: max; exact runtime model/effort identifiers are not exposed), checkout `032a0ee22eb6cf0baaedf2a948ea0bc8747bad32`, Sussman–Alpoge source `31a47c543775`. Research text; no audit or scientific status.

## 1. Contract and source boundary

Queue row 139 asks for [NL] of `dec-field.md` Section 5, for the actual R9 operators, on the complex **independent-current** domain and throughout the decoupling polydisc. Write
\[
 \|a\|_{X,w}=\sup_y w(y)\max\{\xi_y|a|_y,\xi_y^2|\nabla_{\mathbf U}a|_y\},\qquad
 \|f\|_{F,w}=\sup_y w(y)\xi_y^3|f|_y.
\]
The row norm \(Y_w\) uses the dimensionless straightened rows. With \(B=Ce^{16\bar\kappa}\ge1\), the requested bounds are
\[
 \|W_s(a)-W_s(v)\|_{F,w}\le C_WB^2r\|a-v\|_{X,w},\qquad
 \|\mathcal C(a)-\mathcal C(v)\|_{Y,w}\le C_Cr\|a-v\|_{X,w},
 \tag{1.1}
\]
for \(\|a\|_{X,1},\|v\|_{X,1}\le r\le r_0/B\), as well as holomorphy and vanishing at zero. In particular (1.1) requires \(DW_s(0)=0\); vanishing of \(W_s(0)\) alone is insufficient.

The source for R9 and its claimed reduced nonlinear expression is Ethan Sussman and Levent Alpoge, **with Claude and Codex as authors of their text**, [YM4 outline at the specified revision](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), lines 10129–10192, 10356–10415 and 10562–10576. All use of that prescription below carries this credit. The source was fetched once to `/tmp/sa_ym4.tex`; searches and excerpt retrieval are not proof steps.

The linear input [PW], when explicitly invoked below, means the **named, same-model, Claude-gate-pending implication** of `pw-bridge.md`, not an independently checked fact. Its premises are [Energy], [Coefficients], [Walk geometry] and [Parameter geometry] in its Section 6. Theorem Sigma of `a3-clauses.md` is not a substitute for these current-corrected operators; its Section 4.3 expressly leaves them out. No identity such as \(\widehat QH(s)=1\) or \(RD^{\mathsf T}H(s)=0\) is assumed at decoupled parameters.

This note was written section by section. Only written arguments, rather than calculations run by a computer, establish its conditional conclusions. Balaban's nonlinear treatment was read in the supplied local copies of CMP **99**, 389–434; CMP **109**, 249–280; and CMP **119**, 243–285. Exact passages and the mathematical content used are recorded with the arguments below.

## 2. Counterexample tests and the formula that must be specified

**First test: do not estimate the unreduced current correction as a force.** In local scale-one units take flat links and an independent current
\(J_1(x)=(\gamma_0/2)(-1)^{x_1/\eta}T_3\), zero in the other directions, on an interior patch. Extend it by zero outside the patch. Choose colors with \(b_0=\langle i[T_1,T_2],T_3\rangle\ne0\). At \(A=0\), with the auxiliary site field \(\lambda=T_1\) on this patch, vary \(\lambda\) by \(v=T_2 1_{\{x\}}\). In the current form
\[
 c_J(A,\lambda)=\langle i[\lambda,A]-i[A,\lambda^+]-i[\lambda,D\lambda],J\rangle_f
\]
only the last term contributes. The outgoing and incoming differences of \(v\) are respectively \(-T_2/\eta\) and \(T_2/\eta\). Consequently
\[
 \eta^{-4}dc_J(0,\lambda)[0,v]
 =\eta^{-1}\langle i[T_1,T_2],J_1(x)-J_1(x-\eta e_1)\rangle
 ={\gamma_0 b_0\over\eta}(-1)^{x_1/\eta}.
 \tag{2.1}
\]
Every regular-pair condition holds for these flat links and this bounded independent current. The torus can have arbitrary fine mesh inside a scale-one layer; the patch avoids any parity condition on its period. This is the hand counterexample of `dec-field.md` Proposition 2.1, reproduced to fix its scope. It refutes a pointwise estimate on the auxiliary current block, **not** the nonlinear bound (1.1). A proof that differentiates this current pointwise and then calls it a bounded coefficient cannot prove [NL].

**Second test: removing the wrong quadratic part leaves a linear term.** Put \(d_s(a)=\mathcal C(a-H(s)d_s(a))\). Direct differentiation at zero gives
\[
 d_s(0)=d_s'(0)=0,\qquad d_s''(0)=\mathcal C''(0),
 \tag{2.2}
\]
independently of \(s\) and independently of any identity for \(H(s)\). Thus the derivative of the unreduced current force \(-d_s'(a)^{\mathsf T}p\) at zero is \(-\mathcal C''(0)[a,\cdot]^{\mathsf T}p\). It is not legitimate to obtain a factor \(r\) for this derivative merely from holomorphy and \(d_s'(0)=0\). The term that begins quadratically is
\[
 -\big(d_s'(a)-\mathcal C_2'(a)\big)^{\mathsf T}p,
 \qquad \mathcal C_2(a)=\tfrac12\mathcal C''(0)[a,a].
 \tag{2.3}
\]
In particular, replacing \(\mathcal C_2(a)\) here by \(\mathcal C_2(\mathsf Sa)\), simply because \(\mathsf S^{\mathsf T}\Delta^{(2)}\mathsf S\) occurs in \(\mathsf G_1^{-1}\), is invalid on the full balls: the remaining linear operator is
\(\mathsf S^{\mathsf T}\Delta^{(2)}[p]\mathsf S-\Delta^{(2)}[p]\), in matched raw-row units. The two quadratic forms agree on the physical slice; that does not make their ambient derivatives identical. No assertion that this operator is nonzero for every pair is needed for this diagnostic.

**What the published calculations actually do.** Balaban, CMP **99**, pp. 418–423, (3.116)–(3.120) and (3.127)–(3.137), first extends the Hessian off the gauge slice and then includes the quadratic constraint/current term. The estimate following (3.130) keeps one derivative on a test field; it expressly withholds the Laplacian estimate. CMP **109**, pp. 261–263, (1.8)–(1.16), introduces the independent pair \((U,J)\); it supplies no difference bound on that independent \(J\). CMP **119**, pp. 267–273, (3.15) and (3.28)–(3.31), uses the change of variables \(a\mapsto a-hD(a)\), then subtracts lower Taylor orders before representing the remainder. It imports the nonlinear change of variables rather than reproving its estimates there.

The actual nonlinear formulas underlying these uses are in the supplied additional paper, Balaban, CMP **102**, pp. 286–295: (49), (55)–(58), (78)–(89), (91)–(98), and (119)–(120). In particular, (80) has four scalar remainder terms; its derivative has five terms after the quadratic cross term is differentiated. Sections 3–6 below reprove the estimates and the algebra needed from these passages. No theorem of those papers is used as a citation-only premise.

**Specification boundary.** SA 5775–5784 explicitly calls the nonlinear maps specified data. The cited R9 passages 10368–10372 and 10562 give a reduction prescription, but do **not** print its formula or the assignments of every remaining walk datum. To avoid promoting an interpretation into a source fact, name the following input:

**[RED]:** the \(W_s\) meant by the consumer is the reduced Balaban expression (4.4) below, with the raw-row convention and the operator assignments in Section 4. This is an explicit, reviewable specification, not a consequence of [PW]. The proof will establish [NL] for that expression. Identification of any separately supplied \(W_s\) with (4.4) must be checked; agreement on the physical slice alone does not establish agreement on the independent-current domain. This is narrower than an unconditional assertion about an unspecified off-shell extension.

## 3. The local nonlinear calculus

Retain the actual straightened rows, their finite one-step formulas and their carrier geometry, as used in `a3-derivative.md` Section 4, `a2-curved.md` Section 8 and [Coefficients] of `pw-bridge.md`. These are **[Rows]**: a row of length \(m_c\) has its actual adjacent-block carrier; scales on it are comparable within a constant depending on fixed \(L\); a fine bond lies in a bounded number of these carriers; and each carrier has bounded determining diameter. The one-step formula is the straightened Federbush formula, including its two endpoint factors, not the plain average. For this geometric/formula input the following estimates are rederived here. They do not invoke Theorem Sigma or its propagators.

### 3.1 Holomorphy, row density and the constraint remainder

For matrices in a sufficiently small fixed norm ball, the series for \(e^X\) and \(\log(1+X)\) converge absolutely. Products along a one-step contour use at most \(C_L\) factors. If a group mean is implicit, its equation after translation is
\(N^{-1}\sum_i\log(e^{-Z}e^{X_i})=0\). The series give
\(\log(e^{-Z}e^X)=X-Z+E(Z,X)\), with
\(|E|\le C(|Z|+|X|)^2\) and \(|\partial_ZE|\le C(|Z|+|X|)\).
For \(\max|X_i|\le\epsilon\), iteration of
\(Z=N^{-1}\sum_i(X_i+E(Z,X_i))\) in \(|Z|\le2\epsilon\) has contraction constant at most \(3C\epsilon\). Choose it below \(1/2\). The iterates converge uniformly on smaller balls, so their Cauchy integrals converge and the mean is holomorphic. Constants use \(N^{-1}\sum_i1=1\), not \(N\).

In the actual one-step formula, write \(T_{yx}\) for the prescribed internal Federbush transport and \(\mathcal M\) for the plain average. The endpoint factor and the straightened raw logarithm are
\[
\begin{aligned}
 u_W(u)(y)&=\exp\!\left[L^{-4}\sum_{x\in B_L(y)}
     \log\{T_{yx}(e^{iu}W)T_{yx}(W)^{-1}\}\right],\\
 F_W(u)(c)&=\frac1i\log\{u_W(u)(c_-)^{-1}\mathcal M(e^{iu}W)(c)
                u_W(u)(c_+)\mathcal M(W)(c)^{-1}\}.
\end{aligned}
\]
These are SA PX141, with the authorship credit of Section 1. The outer endpoint factor is an exponential of averaged relative logarithms, not an additional implicit group mean. The latter occurs only inside the specified transports. Gauge equivariance gives the recursion \(u_{n+1}=F_{W_n}(u_n)\): its accumulated gauge factors multiply in the order \(v_{n+1}=v_n|_{\rm next}\,u_{W_n}(u_n)\), and do not change this recursion for its logarithms.

The flat derivative of \(F_W\) has absolute row sum \(L\) and column sum \(L^{-3}\): the endpoint contour contributions cancel to leave the average of length-\(L\) straight segments; each input bond occurs in \(L\) translated segments of weight \(L^{-4}\). Finite incidence and Taylor's formula for the preceding analytic functions give
\[
 \|D F_W(u)\|_{\rm row}\le L(1+C_L(v+|u|)),\qquad
 \|D F_W(u)\|_{\rm col}\le L^{-3}(1+C_L(v+|u|)),
 \tag{3.1}
\]
where \(v\) bounds the reference link logarithms on this step. The absolute coefficient sums of any fixed higher derivative on a smaller one-step ball are also bounded by constants depending only on \(L\). This is a finite-dimensional statement at one step, not a dimension-dependent Cauchy estimate at depth \(j\).

Here is why iterating (3.1) does not create a depth constant. For a row \(m=L^j\eta\), put \(t_n=L^n\eta/m\), \(0\le n\le j\). The local regular gauge and the finite plaquette-sliding formula give reference bounds \(v_n\le C_L\epsilon t_n\). More explicitly their induction uses
\[
 v_{n+1}\le Lv_n+C_L(v_n^2+p_n),\qquad
 p_{n+1}\le L^2(1+C_Lv_n)p_n+C_Lp_n^2,
\]
starting with \(v_0\le C_L\epsilon t_0\), \(p_0\le C_L\epsilon t_0^2\). In the second formula the linear flux is the sum of the \(L^2\) fine plaquettes; every remaining term contains either an additional link logarithm or an additional plaquette error. Division by \(t_{n+1}^2\) bounds the curvature growth by a product with logarithm \(C_L\sum_n(\epsilon t_n+\epsilon t_n^2)\). Division of the first formula by \(t_{n+1}\) leaves a sum bounded by \(C_L\sum_n(\epsilon+\epsilon^2)t_n\). Taking fixed larger comparison constants and then small \(\epsilon\) closes both inductions by first exit. This is the local regular-gauge calculation, not a claim that small plaquettes alone produce a gauge.

For an input with \(m\sup|a|\le\rho\), set \(u_0=\eta a\), \(u_{n+1}=F_{W_n}(u_n)\). The same product bound yields \(|u_n|\le2\rho t_n\), after choosing \(\epsilon,\rho\) small. Indeed
\(\sum_{n<j}t_n\le(L-1)^{-1}\), so every extra product in (3.1) is at most \(\exp(C_L(\epsilon+2\rho)/(L-1))\), which can be made less than two. The accumulated endpoint factors have the same bound on their condition numbers, since their logarithmic sizes are \(O_L(|u_n|)\). This also keeps all complex logarithms and means in their defining balls.

Write \(q(a)=\mathcal Q(a)\), \(K_a=q'(a)\), \(K=K_0=\widehat Q\). Multiplying the step products by the initial factor \(\eta\) proves, for every row \(c\) and every bond \(b\),
\[
 \sum_b|K_a(c,b)|\le C_Lm_c,\qquad
 |K_a(c,b)|\le C_L\eta^4m_c^{-3}.
 \tag{3.2}
\]
For the second inequality an entry is no larger than its product's absolute column sum, \(C_L\eta L^{-3j}\). This supplies its density factor without summing all fine coordinates with weight one.

Cauchy differentiation preserves that density. On a row carrier use a circle of radius \(c/(m_c\sup|h|)\) in direction \(h\), wholly inside the larger ball just proved. Thus
\[
 |D K_a[h](c,b)|\le C_L\eta^4m_c^{-3}(m_c\sup|h|),
\]
and two circles give the product of two normalized suprema for \(D^2K_a[h,k]\). The same statements for absolute row sums follow by applying Cauchy's integral to the row vector and its \(\ell^1\) norm. Zero directions follow by linearity. Integrating between \(0\) and \(a\) supplies one factor \(\|a\|_X\) for a difference of derivatives.

Use the fine bilinear pairing \(\eta^4\sum_b\langle\cdot,\cdot\rangle\) and the counting row pairing. A transpose contributes \(\eta^{-4}\); (3.2) cancels it. Bounded carrier overlap and comparable scales then give, uniformly in the admitted weights,
\[
\begin{aligned}
 &\|K\|_{X_w\to Y_w}+\|K^{\mathsf T}\|_{Y_w\to F_w}\le C,\\
 &\|\mathcal C(a)\|_Y\le C\|a\|_X^2,
 \quad\|\mathcal C'(a)h\|_{Y,w}\le Cr\|h\|_{X,w},
 \quad\|\mathcal C'(a)^{\mathsf T}p\|_{F,w}\le Cr\|p\|_{Y,w},\\
 &\|(\mathcal C''(a)[h,\cdot])^{\mathsf T}p\|_{F,w}
       \le C\|h\|_{X,w}\|p\|_Y,\\
 &\|((\mathcal C''(a)-\mathcal C''(0))[h,\cdot])^{\mathsf T}p\|_{F,w}
       \le Cr\|h\|_{X,w}\|p\|_Y .
\end{aligned}
 \tag{3.3}
\]
Here \(\mathcal C=q-Ka\), so \(\mathcal C(0)=\mathcal C'(0)=0\). The last two bounds also hold with the weight on \(p\) instead of \(h\). Within a carrier a weight changes by at most \(e^{\theta D_L}\), a fixed constant. The segment integral of \(\mathcal C'\) proves its member of (1.1). Only the local constraint map has been treated here, not any current-corrected inverse.

### 3.2 The Wilson force after subtraction of its first two Taylor orders

Let \(F_{\mathbf U}(a)\) be the inner-plaquette Wilson action in the exponential link chart, with its holomorphic extension. Define
\[
 N_0(a)=F_{\mathbf U}'(a)-F_{\mathbf U}'(0)-F_{\mathbf U}''(0)a.
\]
The current in this definition is the actual derivative of the reference action. It is subtracted exactly; it is not identified with the independent \(\mathbf J\).

We reprove the estimate used by Balaban, CMP 102 (91)–(98). At one plaquette transport the four oriented insertions to a common corner and put \(X_i=i\eta a_i\). Its varied holonomy is \(\prod_{i=1}^4e^{X_i}P\), with \(|P-1|\le C\alpha_0\eta^2m^{-2}\). For traceless two-by-two matrices \(X\), the identity \(X^2=\tfrac12\operatorname{tr}(X^2)I\) implies \(\operatorname{tr}X^3=\operatorname{tr}(X^2Y)=0\). Thus the cubic coefficient of \(\operatorname{tr}\prod_ie^{X_i}\) is \(\sum_{i<j<k}\operatorname{tr}(X_iX_jX_k)\). Expanding the following expression triple by triple gives the exact identity
\[
 \sum_{i<j<k}\operatorname{tr}(X_iX_jX_k)
 =\tfrac12\operatorname{tr}\left[(\sum_iX_i)\sum_{i<j}[X_i,X_j]\right].
 \tag{3.4}
\]
Indeed the three contributions from an ordered triple have signs \(+,-,+\), each twice its ordered trace. Repeated indices contribute zero by the preceding square identity.

The sum of the oriented insertions is the first plaquette variation, of size \(\eta^2\nabla_{\mathbf U}a\), with possible corner-transport remainders bounded by \(C\alpha_0\eta^3m^{-2}|a|\). The latter are harmless under the estimate below. Terms with \(P-1\) have cubic differentiated density at most \(C\alpha_0\eta m^{-2}|a|^2\). Terms of degree at least four have differentiated density at most \(C|a|^3\): after division by the fine volume \(\eta^4\), the degree-\(n\) bound is \(C_n\eta^{n-4}|a|^{n-1}\), and the absolutely convergent exponential majorant sums these for \(\eta|a|\) small.

It remains to estimate the derivative of the cubic term in (3.4). Varying the first factor gives a covariant difference on the variation; summation by parts transfers it to the commutator sum. In one flat-corner notation put \(v=a_\mu(x)\), \(w=a_\nu(x)\), \(u=\nabla_\mu a_\nu(x)\), \(t=\nabla_\nu a_\mu(x)\). The four oriented values are \(v,w+\eta u,-v-\eta t,-w\), and their commutator sum is
\[
 2[v,w]+2\eta[v,u]+2\eta[t,w]-\eta[v,t]
                  +\eta[w,u]-\eta^2[u,t].
 \tag{3.5}
\]
This follows by listing its six pairs. In a background the same list uses transported values; moving to the common corner contributes the curvature remainders already bounded. On the leading commutator use the exact product rule
\[
 \nabla[v,w]=[\nabla v,w]+[v,\nabla w]+\eta[\nabla v,\nabla w].
\]
Every other term in (3.5) already has a factor \(\eta\); bound its extra backward difference by the sum of its two endpoint magnitudes divided by \(\eta\). This uses first differences only. Varying either of the other two factors in the cubic term directly gives \(C|a||\nabla a|\). Therefore the complete force remainder at an interior bond is bounded by
\[
 C\bigl(|a||\nabla_{\mathbf U}a|+\eta|\nabla_{\mathbf U}a|^2
              +|a|^3+\alpha_0\eta m^{-2}|a|^2\bigr).
 \tag{3.6}
\]
At an action boundary a paired plaquette can be missing. This boundary lies in the bare layer, where \(m=\eta\); the crude remaining bound \(C\eta^{-1}|a|^2\) has the same scaled estimate. Each bond has a fixed finite plaquette stencil. Since \(\eta\le m\), (3.6) is at most \(Cr^2m^{-3}\) on \(\|a\|_X\le r\le\rho\).

Cauchy differentiation on that fixed stencil, with direction-circle radius \(r/\|h\|_{X,\mathrm{stencil}}\), uses the same bound at \(2r\) and yields
\[
 \|N_0(a)\|_F\le Cr^2,\qquad
 \|N_0'(a)h\|_{F,w}\le Cr\|h\|_{X,w}.
 \tag{3.7}
\]
Weights transfer only across this stencil. Holomorphy follows from the same convergent series. This proof imposes neither a difference bound on the independent current nor a mesh-uniform bound on \(J(\mathbf U)\).

## 4. The reduced operator data and the five-term expression

All transposes in this section are bilinear. Use counting raw rows, with \(K=\widehat Q=\mathsf mQ\), \(H=\mathsf H\mathsf m^{-1}\), and physical fine pairing. Put \(W_0=Q\mathsf GQ^{\mathsf T}\) (the row Gram, not the nonlinear map). The raw row precision is
\[
 M=\mathsf m^3(W_0^{-1}-a)\mathsf m^{-1}
   =\mathsf m^3W_0^{-1}\mathsf m^{-1}-a_0I.
 \tag{4.1}
\]
This conversion is essential: the per-length row pairing has weight \(\xi_c^4\), whereas the raw row pairing is counting measure. In particular \(H^{\mathsf T}f=\mathsf m^3\mathsf H^{\mathsf T}_{\rm physical}f\). Formula (4.1) is symmetric in counting measure.

Use the prescribed \(H(s)\) of o1-decoupled Definition D. Give \(W_0^{-1}\) its own \(-\nu\nu\) block walk expansion of `h-walk.md` at coefficient \(j=0\), with the same full-hull parameter convention. Define \(M_s\) by that expansion in (4.1), retaining the local diagonal \(-a_0I\) without a parameter. This specifies one remaining datum which the bare [PW] statement does not name. No formula in terms of inverses of \(H(s)\), or products of independently decoupled Gram factors, is used.

**Linear bounds actually needed.** Under [Energy], [Walk geometry], [Parameter geometry], the repaired o1 construction, and the same-model [PW] input for its field output, enlarge the common constant in \(B=Ce^{16\bar\kappa}\) so that
\[
 \|H(s)\|_{Y_w\to X_w},\quad
 \|H(s)^{\mathsf T}\|_{F_w\to Y_w},\quad
 \|M_s\|_{Y_w\to Y_w}\le B.
 \tag{4.2}
\]
Here is the derivation of the two bounds beyond the field member of [PW]. For the transpose,
\[
 w(c)|H(s)^{\mathsf T}f(c)|
 \le\|f\|_{F,w}\,w(c)\eta^4
       \sum_b |H(s)(b,c)|\xi_b^{-3}w(b)^{-1}.
\]
The last sum is exactly the first member of (O1), o1-decoupled Theorem B(c). Its proof is a supported-source local-energy estimate followed by Cauchy–Schwarz on each pillar and an exponential pillar sum; it applies to the independent-current domain. Thus no transpose pointwise regularity or derivative of \(f\) has been silently assumed.

For \(M_s\), inject \(u\delta_c/\xi_c\) in the \(\nu\)-source slot of the eight-unknown system. Its dual norm is \(|u|\), and elimination gives \(\nu=-W_0^{-1}(u\delta_c/\xi_c)\). The output norm includes \(\xi_{c'}^3|\nu(c')|\), precisely the normalization in (4.1). For each walk the local-energy estimate therefore bounds this output by
\(C(C/M_1)^n e^{-(\tau_L/2)t_\omega(c',c)}|u|\).
The parameter count from Definition D is
\(|s^\omega|\le e^{16\bar\kappa}e^{64\bar\kappa t_\omega/\ell_{\mathsf P}}\).
Choose the same floors and partition size as `pw-bridge.md` (6.5). A reserved fraction of the exponential controls the weight and sums output/source pillars; the remaining walk count sums \(\sum_n(C_L/M_1)^n\le2\). There are only boundedly many rows per pillar. This proves a bound \(Ce^{16\bar\kappa}\) on the normalized Gram inverse in (4.1). Add \(a_0\) for its diagonal. This uses the multiplier component of the energy norm, not an unproved Laplacian bound. Uniformly convergent holomorphic walk sums give joint holomorphy of \(M_s\). The field bound in (4.2), by contrast, is used from **[PW]**, whose Claude gate remains pending.

For small \(a\), set
\[
 d=d_s(a)=\mathcal C(a-H(s)d),\qquad
 z=a-H(s)d,\qquad Z=z'=1-H(s)d_s'(a),\qquad
 p_s=H(s)^{\mathsf T}\mathbf J,
 \quad d_{3,s}=d_s-\mathcal C_2.
 \tag{4.3}
\]
The promised explicit reduced prescription is
\[
\boxed{\begin{aligned}
 W_s^{\rm red}(a)={}&-d_{3,s}'(a)^{\mathsf T}p_s
                    -K^{\mathsf T}M_s d_s(a)\\
                  &-d_s'(a)^{\mathsf T}M_sKa
                    +d_s'(a)^{\mathsf T}M_s d_s(a)
                    +Z^{\mathsf T}N_0(z).
\end{aligned}}
 \tag{4.4}
\]
Products in (4.4) are part of the definition of the reduced nonlinear expression after insertion of its data. For example \(M_s\) is its own walk sum, whereas \(\mathfrak G(s)\) in R9 remains the separately assigned composed expansion of `pw-bridge.md` Section 7. These choices cannot be changed by invoking an undecoupled identity at \(s\ne1\).

**Deriving the reduction before decoupling.** At an on-shell reference put \(E=\Delta^{\rm W}-\Delta'_\pi[J(\mathbf U)]\). The gauge identity used here can be checked directly. On a bond the logarithm of
\(e^{it\lambda_-}e^{it\eta a}\mathbf U e^{-it\lambda_+}\mathbf U^{-1}\), divided by \(i\eta\), is
\[
 t(a-D\lambda)+\tfrac12t^2
 \big(i[\lambda_-,a]-i[a,\lambda^+]-i[\lambda_-,D\lambda]\big)+O(t^3).
\]
This follows by multiplying the three exponential series through degree two and then using \(\log(1+X)=X-X^2/2+O(X^3)\). Compare the degree-two coefficients of the gauge-invariant inner action before and after this transformation. With \(\lambda=G'RD^{\mathsf T}a\), the result is
\(\langle\mathsf Sa,\Delta^{\rm W}\mathsf Sa\rangle_f
=\langle a,\Delta^{\rm W}a\rangle_f-c_{J(\mathbf U)}(a,\lambda_a)\).
Polarization gives \(E=\mathsf S^{\mathsf T}\Delta^{\rm W}\mathsf S\), with exactly the current form of SA 10175–10190 and Balaban CMP 99 (3.117)–(3.120).

For completeness this identity also explains the physical gauge condition on \(H\). If \(Q'\lambda=0\), then \(G'\Delta\lambda=\lambda\) and \(R\Delta\lambda=\Delta\lambda\), directly from the definitions of \(G'\) and \(R\). Thus \(\mathsf SD\lambda=0\), and \(QD\lambda=\bar DQ'\lambda=0\) by the straightened-row gauge identity. Pair the lift's saddle equation with \(D\lambda\). Its only surviving term is \(\langle\Delta\lambda,RD^{\mathsf T}Hb\rangle\). The scalar constrained inverse identifies \(\Delta(\ker Q')\) with \(\operatorname{ran}R\); this is part of the named scalar inverse input of h-walk Lemma U. Nondegeneracy of the pairing on the range of the symmetric projector \(R\) therefore gives \(RD^{\mathsf T}H=0\). Also \(KH=1\) follows by multiplying the defining Gram inverse. All these identities are at \(s=1\), on shell. Multiplication of the lift's defining inverse now gives, in the raw convention,
\[
 EH=K^{\mathsf T}M,\qquad H^{\mathsf T}EH=M.
 \tag{4.5}
\]
For example the per-length equation is
\(E\mathsf H=Q^{\mathsf T}(W_0^{-1}-a)\);
substitution of the physical-to-counting transpose and (4.1) proves the first formula. The second follows by \(KH=1\). These equalities are used **here only**, before continuation and decoupling.

On the physical linear slice, expand the action at \(z=a-Hd\). Its constant, linear and quadratic parts are
\[
 F(0)+\langle J,a\rangle_f
       +\tfrac12\langle a,Ea\rangle_f-\langle H^{\mathsf T}J,\mathcal C_2(a)\rangle.
\]
The remaining scalar function, using (4.5), is exactly
\[
 -\langle p,d-\mathcal C_2(a)\rangle
 -\langle Ka,Md\rangle
 +\tfrac12\langle d,Md\rangle+V_0(z),\qquad V_0'=N_0.
 \tag{4.6}
\]
Differentiate each of its four terms. The second gives two terms; symmetry of \(M\) combines the derivative of the third into one. The result is (4.4) at \(s=1\). This reproduces Balaban CMP 102 (80), (85), (88), (89) and the derivative of its last term. Formula (4.4) then continues this **reduced expression**, as SA mechanism (j) prescribes. It never reapplies (4.5) at a general pair or at decoupled parameters.

On the slice the quadratic term displayed here also equals the one using \(E-\mathsf S^{\mathsf T}\Delta^{(2)}[\mathsf H^{\mathsf T}J]\mathsf S\) in the outline's \(\mathsf G_1\). Off the slice, their ambient gradients need not coincide. Accordingly (4.4) gives the gradient of the extension (4.6), and represents the correct slice derivative at physical data. It is not asserted to be the unreduced action gradient on arbitrary independent-current data. Precisely this distinction necessitates [RED].

## 5. The nonlinear change of variables, including its transposed derivatives

Let \(C_*\ge1\) dominate the constants of (3.3), (3.7) and the carrier weight transfers. Fix the pair ceiling and all geometric floors first. Choose
\[
 0<r_0\le\min\{\rho_{\rm local}/16,\, (2^{12}C_*^4)^{-1}\}.
 \tag{5.1}
\]
It is independent of depth, mesh, volume and \(M_1\). The explicit factor \(B\) is introduced only afterwards.

On the larger \(a\)-ball of radius \(R=4r_0/B\), iterate
\(d\mapsto\mathcal C(a-H(s)d)\) from zero in \(\|d\|_Y\le4C_*R^2\). Its argument has norm at most \(R+4C_*BR^2\le2R\), so the map stays in the ball by (3.3). Its Lipschitz constant is at most \(2C_*BR\le1/4\). Successive differences are bounded by a geometric series, proving existence and uniqueness in this ball. The same estimates on any smaller \(a\)-ball give, by uniqueness,
\[
 \|d_s(a)\|_Y\le4C_*\|a\|_X^2,\qquad
 \|z(a)\|_X\le2\|a\|_X.
 \tag{5.2}
\]
The iteration is jointly holomorphic in \((a,s,\mathbf U,\mathbf J)\), and uniformly convergent on smaller open domains. Cauchy's formula passes to the limit, proving joint holomorphy. This proves existence of the nonlinear map (4.3), rather than taking it as a new analytic input.

For derivatives in \(a\), put
\[
 A=\mathcal C'(z),\qquad N=(1+AH(s))^{-1}.
\]
The inverse and its transpose have geometric series with norm at most two in every \(Y_w\): for the transpose use \(H(s)^{\mathsf T}A^{\mathsf T}:Y_w\to Y_w\), bounded by \(2C_*Br<1/2\). Implicit differentiation gives
\[
 d'=NA,\qquad Z=1-H(s)d',\qquad
 d''[h,k]=N\mathcal C''(z)[Zh,Zk],
 \tag{5.3}
\]
\[
 (d''[h,\cdot])^{\mathsf T}p
 =Z^{\mathsf T}\big(\mathcal C''(z)[Zh,\cdot]\big)^{\mathsf T}N^{\mathsf T}p.
 \tag{5.4}
\]
The last identity follows by pairing the previous one with \(p\) and moving each factor, in its actual order, to the other leg. It is needed because an ordinary derivative bound alone gives no force bound for a transpose.

For \(\|a\|_X\le r\le r_0/B\), (3.3), (4.2) and the geometric series imply
\[
\begin{gathered}
 \|d'\|_{X_w\to Y_w}+\|d'{}^{\mathsf T}\|_{Y_w\to F_w}\le Cr,\\
 \|Z\|_{X_w\to X_w},\ \|Z^{\mathsf T}\|_{F_w\to F_w}\le2,\\
 \|Z-1\|+\|Z^{\mathsf T}-1\|+\|N-1\|+\|N^{\mathsf T}-1\|\le CBr,\\
 \|(d''[h,\cdot])^{\mathsf T}p\|_{F,w}
       \le C\|h\|_{X,w}\|p\|_Y.
\end{gathered}
 \tag{5.5}
\]
Each difference norm has the domain and range of its corresponding preceding factor. The last line also permits the weight on \(p\).

Subtract \((\mathcal C''(0)[h,\cdot])^{\mathsf T}p\) from (5.4). Telescope the four factors in this order: \(Z^{\mathsf T}\), the argument \(Zh\), \(\mathcal C''(z)\), and \(N^{\mathsf T}\). Their differences from the factors at zero have norms respectively \(CBr\), \(CBr\), \(Cr\), and \(CBr\), by (3.3) and (5.5). All unchanged factors are bounded. Hence
\[
 \|(d_{3,s}''(a)[h,\cdot])^{\mathsf T}p\|_{F,w}
       \le CBr\|h\|_{X,w}\|p\|_Y.
 \tag{5.6}
\]
Since \(d_{3,s}'(0)=d_{3,s}''(0)=0\), integration along \(ta\), \(0\le t\le1\), also gives
\[
 \|d_{3,s}'(a)^{\mathsf T}p\|_F\le CB r^2\|p\|_Y.
 \tag{5.7}
\]
This is the precise replacement for an informal invocation of Schwarz's lemma in the current term. It proves the weighted differentiated estimate directly and shows which extra operator norm causes its factor \(B\). No analyticity statement on a shrinking ball has been used to manufacture a missing zero Taylor coefficient.

## 6. Nonlinear bound for the explicit reduced map

**Theorem.** Assume [Rows], the regular-pair and geometric inputs above, (4.2), and the inner Wilson action. The map \(W_s^{\rm red}\) of (4.4) is jointly holomorphic, satisfies
\(W_s^{\rm red}(0)=D W_s^{\rm red}(0)=0\), and satisfies the \(W\) member of (1.1) for all \(r\le r_0/B\). Its constants are uniform in depth, mesh, volume and \(M_1\) above the named floors, on the whole admitted decoupling polydisc and the original independent-current domain. Together with Section 3.1 this is [NL] **under [RED]**.

*Proof.* In differentiating (4.4), the reference pair, the parameters and hence \(H,M_s,p_s\) are fixed. For any direction \(h\), the eight terms are
\[
\begin{aligned}
 D W_s^{\rm red}(a)h={}&-(d_{3,s}''[h,\cdot])^{\mathsf T}p_s
                       -K^{\mathsf T}M_s d'h\\
 &-(d''[h,\cdot])^{\mathsf T}M_sKa
                       -d'{}^{\mathsf T}M_sKh\\
 &+(d''[h,\cdot])^{\mathsf T}M_s d
                       +d'{}^{\mathsf T}M_s d'h\\
 &-(d''[h,\cdot])^{\mathsf T}H(s)^{\mathsf T}N_0(z)
                       +Z^{\mathsf T}N_0'(z)Zh.
\end{aligned}
 \tag{6.1}
\]
Here are their bounds after division by \(\|h\|_{X,w}\), in the displayed order:
\[
 CB^2\gamma_0r,\quad CBr,\quad CBr,\quad CBr,
       \quad CBr^2,\quad CBr^2,\quad CBr^2,\quad Cr.
 \tag{6.2}
\]
For the first, \(\|p_s\|_Y\le B\|\mathbf J\|_F\le B\gamma_0\) by the transpose estimate in (4.2), and (5.6) supplies \(CBr\). The second and fourth use \(d',d'{}^{\mathsf T}=O(r)\), the bounds for \(K,K^{\mathsf T}\), and \(\|M_s\|\le B\). For the third use (5.5) with \(\|M_sKa\|_Y\le CBr\). The fifth uses \(\|M_sd\|_Y\le CBr^2\); the sixth has two factors \(O(r)\). For the seventh, (3.7) gives \(\|H(s)^{\mathsf T}N_0(z)\|_Y\le CBr^2\). The last uses (3.7) and both bounds for \(Z\). This accounts for every differentiated factor.

In particular the independent current is read only through \(H(s)^{\mathsf T}\mathbf J\) in the explicit current term. Its possible rapid oscillation is harmless for this estimate; (O1) pairs it against a summable column. No use of \(D\mathbf J\), \(\Delta H(s)\), or an off-shell Ward identity occurs. The dependence of the operator data themselves on \(\mathbf J\) is allowed and holomorphic; it is held fixed in (6.1).

Choose the fixed current ceiling at most one. Since \(B\ge1\), \(r\le r_0/B\le1\), the sum of (6.2) is at most \(C_WB^2r\). Integrating (6.1) on the segment \(v+t(a-v)\) proves (1.1), since that segment stays in the unweighted \(r\)-ball. The weight is placed on the differentiated leg throughout, not on the size of either background field. Substitution of zero in (4.4) proves vanishing; (2.2), (3.7) and (6.1) prove that its derivative at zero vanishes. The already established convergences and compositions prove holomorphy. All constants come from fixed one-step functions, geometric sums, carrier overlap and the named linear bounds, which proves the asserted uniformity. \(\square\)

Notice that no extra requirement \(B^2\gamma_0\ll1\) was introduced for this first system. Its nonlinear coefficient may be of order \(B^2\gamma_0\), but it is multiplied by the field radius. This is distinct from the unsubtracted linear current terms of SA's second system.

## 7. Why the remaining specification issue is substantive

Physical agreement, holomorphy, and removal of the first two scalar Taylor orders do not uniquely specify a bounded independent-current continuation. Here is an explicit witness; it is **not** a counterexample to (4.4).

Work on a torus with flat reference links, top scale one and mesh \(\eta=L^{-k}\), with all regions equal to the torus. For any pair define the local cubic functional
\[
 R_P(a)=\eta^4\sum_x\chi_s(x)\xi_x^3
   \left\langle D_{\mathbf U}^{\mathsf T}\mathbf J(x),
          \{a_1(x),\{a_2(x),a_3(x)\}\}\right\rangle,
 \qquad \{X,Y\}=i[X,Y].
 \tag{7.1}
\]
Here \(\chi_s(x)\) can be the product of the parameters on the cubes meeting this local stencil; it equals one at \(s=1\). On the scale-one torus \(\xi_x=1\). All fields in a bracket are based at \(x\). The factor \(\xi_x^3\) makes its force have the same scaling as \(F\). The expression is holomorphic, local, gauge covariant as a scalar functional, and starts in degree three in \(a\).

At an actual current, \(D_{\mathbf U}^{\mathsf T}J(\mathbf U)=0\) exactly. To prove this, differentiate the gauge-invariant inner action at the reference along an infinitesimal gauge transformation: its tangent is \(-D_{\mathbf U}\lambda\). Hence \(\langle J(\mathbf U),D_{\mathbf U}\lambda\rangle_f=0\) for every site field \(\lambda\); the nondegenerate bilinear pairing implies the identity. Thus (7.1) and all its field derivatives vanish on the physical-current graph. Adding its gradient to (4.4) leaves the physical slice reduction and the linear propagator data unchanged, and still gives a holomorphic map vanishing to second order at \(a=0\).

Nevertheless its gradient is not uniformly bounded as required by [NL]. Normalize \(T_i=\sigma_i/2\) to unit norm with the color pairing \(2\operatorname{tr}\), so \(\{T_i,T_j\}=-\epsilon_{ijk}T_k\). On an interior patch take
\[
 \mathbf J_1(x)={\gamma_0\over2}(-1)^{x_1/\eta}T_1,
 \quad \mathbf J_\mu=0\ (\mu\ne1),\qquad
 a_1(x)=a_2(x)=tT_2,\quad a_3=a_4=0.
 \tag{7.2}
\]
The field \(a\) may be constant on the whole torus; its first differences vanish and \(\|a\|_X=t\). Cut the current off outside the patch; the regular-pair domain puts no restriction on that cutoff. At an interior site
\[
 D^{\mathsf T}\mathbf J(x)=-{\gamma_0\over\eta}(-1)^{x_1/\eta}T_1.
\]
For \(s=1\), the first two components of the field gradient of (7.1) vanish at (7.2), because they contain \(a_3\). In the third component invariance of the color pairing gives
\[
 \nabla_aR_P(a)_3(x)
 =\{\{D^{\mathsf T}\mathbf J(x),a_1(x)\},a_2(x)\}
 ={\gamma_0t^2\over\eta}(-1)^{x_1/\eta}T_1.
 \tag{7.3}
\]
Each equality is a two-commutator calculation with the displayed basis. Fix \(t\le r_0/B\), \(\gamma_0>0\), \(\bar\kappa\) and all construction constants. The ratio of (7.3) to \(B^2t^2\) is \(\gamma_0/(B^2\eta)\), unbounded as \(k\to\infty\). The bounded contribution of \(W_s^{\rm red}\) cannot cancel this lower bound: the triangle inequality subtracts at most \(CB^2t^2\). Thus
\(\widetilde W_s=W_s^{\rm red}+\nabla_aR_P\) fails any proposed uniform constant in (1.1), already at \(s=1,w=1\), while preserving those qualitative physical and Taylor-order requirements.

This witness rules out an inference from the physical reduction and holomorphy alone to [NL] on the independent-current domain. It does not say the intended SA reduction contains (7.1), nor that the intended [NL] is false. It explains why [RED] cannot be hidden. The repair is to use the explicit five-term formula (4.4), with \(d_s-\mathcal C_2\) in its current term and the assigned raw precision (4.1); Sections 3–6 then prove the desired estimate.

## 8. Recovery checkpoint and verification limits

The checkout remains at `032a0ee22eb6cf0baaedf2a948ea0bc8747bad32`. The SA download at `31a47c543775` has SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. The `pw-bridge.md` read here has SHA-256 `aa5a5b6e6dff9952c4556cf86e8f0d418b5a644c09154133ea6f0a0d5cf833f3`. Its named implications remain same-model, with Claude review pending. No result of that pending review is presumed.

The source passages for this note are the requested queue rows and sections, plus `a3-derivative.md` Sections 3–5, `a2-curved.md` Section 8, SA PX141–PX154, and the local Balaban passages identified in Section 2. The three requested Balaban papers were read in bounded excerpts; CMP 102 was additionally needed to expose the actual nonlinear formulas imported by CMP 119. Their contributions have been rederived in the local calculus, the reduction, and the two nested derivative identities above. No scan of unrelated folders, numerical run, computer algebra, finite enumeration or computer-assisted certificate supplies a mathematical step.

The failed routes are the pointwise absorption of the auxiliary current block, unsubtracted use of \(-d_s'{}^{\mathsf T}p\), replacement of its second jet by a slice-only quadratic form on the whole ball, and identification of an independent-current continuation solely by its physical values. The next decision is concrete: match the consumer's nonlinear datum and its remaining walk assignments to (4.1)–(4.4), or exhibit its different formula and recheck the eight terms of (6.1). No new model axiom, audit, independent gate or status is supplied by this note.

## Result

**Proved by the written arguments:**

- From [Rows] and the regular-pair local gauges, \(\mathcal C\) is jointly holomorphic, \(\mathcal C(0)=\mathcal C'(0)=0\), and its weighted member of [NL] holds uniformly; Sections 3.1 and 3.2 also establish the transposed constraint calculus and Wilson remainder needed by the first system.
- From those local estimates and (4.2), the explicitly specified reduced map (4.4) is jointly holomorphic, vanishes to second order, and satisfies \(\|W_s^{\rm red}(a)-W_s^{\rm red}(v)\|_{F,w}\le C_WB^2r\|a-v\|_{X,w}\) on every unweighted ball \(r\le r_0/B\), uniformly in depth, mesh, volume and \(M_1\). The field member of (4.2) uses **[PW] from the same-model, Claude-gate-pending `pw-bridge.md`**; the transpose and raw precision members follow from the named repaired energy/walk/parameter inputs as shown in Section 4.
- Consequently **[RED] + [Rows] + [PW] and its named energy/coefficient/walk/parameter premises imply [NL] for R9**, and then `dec-field.md` Proposition 5.1 gives its unique small field, joint holomorphy and weighted first-response bounds for \(\|B'\|<cB^{-4}\). This is a conditional implication, not an independently checked result.
- The explicit configurations (2.1) and (7.2) refute respectively the auxiliary pointwise-current shortcut and any inference of uniform [NL] from physical agreement plus holomorphic quadratic vanishing alone. Neither refutes (4.4).

**Where rank 4 stops:** the pinned SA passages give a prescription rather than a complete displayed independent-current \(W_s\), so identification **[RED] remains an explicit specification obligation**; an unconditional [NL] for a uniquely pre-existing R9 map has not been established here. If (4.1)–(4.4) are the adopted data, the first-system nonlinear estimate is supplied as the implication above. The pending Claude gate on [PW] remains pending. The removed-system comparison still requires matching changed data and nonlinear residuals in `dec-field.md` (6.3); its first-system bound does not repair the false o1 comparison claims. Complex box localisation 6(c) and the Landau node-lift comparison remain later rank-4 obligations. No rank-4 completion or Yang–Mills existence claim follows.
