# A3: derivative of the constrained background
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed; requested effort: max); checkout `1ddede8fb5da70ea56d528637c22ee0092d22b70`; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, `31a47c543775`; T. Balaban, CMP **102** (1985), 277–309, **99** (1985), 389–434, and the averaging/gauge inputs CMP **98** (1985), 17–52 and **99** (1985), 75–102; research text, not an audit, granting no status.

## 1. Task, normalization and source boundary

Queue row 85 concerns the nonlinear datum derivative, not the curvature-profile theorem of row 84. Its consumers are the localized comparison in the Sussman–Alpoge outline, Theorem 6(c), floor screening at lines 18334–18415, and the one-plaquette inequality (L) in `sa-2.8.md`, §9. The target is Theorem 4 at lines 9734–9746, with the analytic Landau pair of Theorem 3. Balaban's corresponding statements are CMP 102, (182)–(190) and Proposition 9, pp. 307–309. His text explicitly leaves the second-variation decay calculation (189) unwritten. Neither its appearance in Proposition 9 nor a citation to it supplies that calculation here.

Write \(\eta=L^{-k}\), \(\xi_y=L^{n(y)}\eta\), and let \(d_{\mathbf B}\) be the determining-family distance. For a datum perturbation at one determining bond \(c\), the value derivative is \(h_c=\partial_s\mathcal H(B+se_c)|_{s=0}\). The desired bounds begin with
\[
 \xi_y|h_c|+\xi_y^2|\nabla h_c|
 \le C e^{-m d_{\mathbf B}(y,y_c)}|e|.
\tag{1}
\]
Balaban uses the kernel with respect to the weighted coarse counting measure: if
\(D\mathcal H(B)b(x)=\sum_c\xi_c^4 K(B;x,c)b(c)\), then
\(K(B;x,c)e=\xi_c^{-4}h_c(x)\). Thus (1) has the source factor
\(\xi_c^{-4}\) in that kernel convention; it is not an extra factor in the value derivative. The gradient has output factor \(\xi_y^{-2}\). Theorem 4 also requires current, second-order and Hölder members, and value bounds for the multiplier and top gauge factor. Potential bounds in an unspecified gauge do not imply these statements.

The permitted pending inputs are row 81 (Balaban's regular critical orbit and its analytic chart, with the actual outline average and boundary rows matched) and row 82 (the background propagators and their weighted regularity package, on the specified complex domains). The decay assertion (189)–(190) itself is excluded from those inputs. In particular, a pending port must distinguish Balaban's comb projection \(R^{\mathsf c}\) from the outline's \(R\); the outline says they coincide at a flat pillar, not at every curved background.

The pinned outline was fetched once to `/tmp/sa_ym4.tex`. The supplied Balaban OCR files remain outside the repository. Searches and file hashes are source bookkeeping, never mathematical certificates. The sparse checkout's workflow and physics-loop instructions are read with `git show` at the pinned revision; the user's narrower delivery rules govern. Only this file is an output.

## 2. Counterexample tests before the proof

**Flat holonomy with increasing depth.** The example in `a1-orbit.md`, §7.1, has coarse datum \(V_1=e^{tZ}\), other components one, with \(Z=\operatorname{diag}(i,-i)\). At bare spacing \(\eta=s^{-1}\), \(s=L^k\), take \(U_1=e^{tZ/s}\). Its scale-correct potential is constant, its divergence and gradient vanish, and its coarse datum is exactly \(V\). The pillar gauge \(u(x)=e^{t(x_1-y_1)Z/s}\) puts it in the face-supported axial representative. Since \(|x_1-y_1|/s<1/2\), its complex gauge factor is bounded uniformly for bounded \(t\). The growing axial counting-norm derivative is therefore not a counterexample to (1). This test is a globally supported datum change and by itself proves no off-diagonal decay.

**A single coarse-link lift.** Giving one coarse link angle \(t\) produces angle \(t\) on some fine plaquettes of the discontinuous exact lift. Its normalized fine curvature grows like \(s^2\). This refutes the use of that lift as a uniformly regular seed, as §7.2 of `a1-orbit.md` explains. It does not refute the regular critical background, which is a different configuration.

**Changing the geometry or using arbitrary floor data.** A derivative on one admitted datum chart cannot be integrated between different determining families without a common restriction problem, matched collar rows, and an admitted interpolation. Nor does it apply to an arbitrary large datum excluded from its chart. Those are hypotheses to establish for Theorem 6(c) and floor screening, not counterexamples to the derivative theorem. The previous gate's failures of the patch argument and of the two-background continuation are retained; neither Theorem CL nor §7 of `a3-response.md` is used as a proved inverse or continuation theorem.

At this checkpoint these tests have produced no configuration violating (1). Absence of a counterexample is not a proof. The argument below must supply the weighted Hessian estimate and retain all unmatched premises explicitly.

## 3. The precise pending inputs and pairings

All bounds below concern finite lattices, with constants independent of their size and depth. Fix the construction constants before choosing the small radii. A first-difference stencil and a determining row carrier meet only a bounded number of adjacent layers. A row of length \(s\) has its two endpoint blocks as carrier, scales there comparable to \(s\) within a fixed power of \(L\), and carrier diameter at most \(D_L\) in the determining distance. A fixed fine bond belongs to a bounded number of carriers. These are the **actual row carriers**, not the large Euclidean patches invalidated by the A3 gate. They follow from the cubical nesting and the omission of inward rows. Inward-row variants require their own linear input and are not included below.

Use the fine pairing \(\eta^4\sum_b\operatorname{tr}_{\rm col}\) and the **counting** row pairing \(\sum_c\operatorname{tr}_{\rm col}\). A multiplier \(\lambda(c)\) is dual to the raw, dimensionless row logarithm in this pairing. If the row pairing is instead \(\sum_c\xi_c^4\operatorname{tr}_{\rm col}\), its multiplier is \(\xi_c^{-4}\lambda(c)\). This conversion is necessary: it leaves the scalar Lagrangian, and hence its Hessian, unchanged. All multiplier value bounds below refer to \(\lambda\).

For a positive scalar weight satisfying
\[
 w(y)\le e^{\theta d_{\mathbf B}(y,z)}w(z),
\]
put
\[
 \|a\|_{X,w}=\sup_y w(y)\max\{\xi_y|a|_y,\xi_y^2|\nabla a|_y\},\quad
 \|f\|_{F,w}=\sup_y w(y)\xi_y^3|f|_y,\quad
 \|b\|_{Y,w}=\sup_c w(y_c)|b(c)|.
\tag{2}
\]
Stencils are included in the local norms; moving a stencil endpoint changes the weight by a fixed factor. Write \(X,Y,F\) for weight one. Transposes below are bilinear, including at complex arguments.

**P81, cited-pending.** Row 81 must supply the regular real critical orbit at the actual determining datum, its local regular gauges and current bound, and the analytic averaging/critical charts of CMP 102 Theorem 1, Proposition 8 and the analyticity part of Proposition 9. On a row carrier these give a small local potential with size \(\kappa/\xi\), first difference \(\kappa/\xi^2\), and curvature \(\kappa\eta^2/\xi^2\), where \(\kappa=C_L\mathfrak M\bar\varepsilon\) is small. The straightened factorization, including the outward-node reduced datum, is the one at SA 9627–9646 and 11507–11549. The estimates proved below use those formulas, not (189) or (190).

**P82, cited-pending, with an essential matching requirement.** Row 82 must supply the following linear package at that reference, in the outline's \(K_0,R\) convention. Let \(J=F'(0)=K_0^{\mathsf T}\lambda_0\), let
\[
 W_0h=(D K_0[h])^{\mathsf T}\lambda_0,\quad
 L_0=F''(0)-W_0,\quad
 G=(L_0+DRD^{\mathsf T}+K_0^{\mathsf T}K_0)^{-1},
\]
\[
 C_0=K_0GK_0^{\mathsf T},\quad
 H=GK_0^{\mathsf T}C_0^{-1},\quad T=G-HK_0G.
\tag{3}
\]
The operators exist and are the correctly identified CMP 99b constrained-current propagators. In the normalization just specified, \(\lambda_0\) is bounded by \(C\kappa\). For \(0\le\theta\le\delta_0/2\), uniformly in the weight centre,
\[
 \|Tf+Hb\|_{X,w}
 +\|-H^{\mathsf T}f+(C_0^{-1}-1)b\|_{Y,w}
 \le C_{\rm lin}(\|f\|_{F,w}+\|b\|_{Y,w}).
\tag{4}
\]
The individual factors in (3), their transposes in the indicated spaces, the analogous operators before the \(W_0\) correction, and \(D(1-R)D^{\mathsf T}:X_w\to F_w\), have the corresponding bounds. The field output has the gradient Hölder bound with factor \(\xi^{2+\alpha}\), for each fixed \(0<\alpha<1\). The scalar constrained inverse makes \(\Delta:\ker Q'\to\operatorname{ran}R\) an isomorphism. These are linear estimates and identities, independent of the datum response being proved.

This is the input to be checked against CMP 99b (3.42)–(3.49), (3.124)–(3.138), Theorems 3.12–3.13, and their port. It includes the weighted summation statements, not just pointwise exponential kernels: a polynomial count of multiscale metric balls is not assumed. It does **not** include a covariant-Laplacian bound for \(G,G_1\); Balaban explicitly excludes that member. Nor does calling a propagator “background” identify its current correction with \(W_0\). That identity, the row lengths and the \(R^{\mathsf c}\)-to-\(R\) port are part of the pending input. A port only in the comb slice does not satisfy P82.

The subsequent assertions are conditional on P81–P82. They do not turn either pending row into a proved input.

## 4. Local nonlinear bounds, including both legs of the constraint

This section rebuilds the nonlinear estimates needed after the linear input. The straightened recursion and the geometric-series organization are from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (SA 11507–11639, PX141–PX154), following T. Balaban, CMP 98 Propositions 4–5. Keeping the raw row normalization throughout removes several otherwise misleading scale factors.

### 4.1 Finite one-step functions and the geometric sum

A group mean near a common transport has uniform analytic bounds independently of the number of averaged paths. Indeed write its defining equation as
\(N^{-1}\sum_i\log(e^{-Z}e^{X_i})=0\), after translating the common transport to one. The absolutely convergent exponential and logarithm series on a fixed matrix ball give
\(\log(e^{-Z}e^{X})=X-Z+E(Z,X)\), with
\(|E|\le C(|X|+|Z|)^2\), \(|\partial_ZE|\le C(|X|+|Z|)\).
For \(\max|X_i|\le a\), the map
\(Z\mapsto N^{-1}\sum_i[X_i+E(Z,X_i)]\) maps \(|Z|\le2a\) into itself and has Lipschitz constant at most \(3Ca<1/2\), after decreasing \(a\). Its iterates converge geometrically and holomorphically. All bounds use the sum of averaging weights, which is one. The same proof covers the prescribed finite path multiplicities.

Let \(F_W(a)\) be one straightened step, including its two endpoint block factors. Each path has at most \(C_L\) bonds. Matrix multiplication, the preceding mean and the logarithm series consequently make \(F_W\) holomorphic and uniformly bounded on a fixed raw ball, with \(F_W(0)=0\). Its derivative at \(W=1,a=0\) is the straight segment average: the endpoint contour derivatives cancel against the block factors. Its absolute row sum is \(L\). A fixed fine bond is traversed by \(L\) translated length-\(L\) segments, each of averaging weight \(L^{-4}\), so its column sum is \(L^{-3}\). Scalar Cauchy estimates on a smaller ball give
\[
 \|D_aF_W(a)\|_{\rm row}\le L(1+C_L\delta),\qquad
 \|D_aF_W(a)\|_{\rm col}\le L^{-3}(1+C_L\delta),
 \quad \delta=\|\log W/i\|_\infty+\|a\|_\infty.
\tag{5}
\]
All higher one-step derivatives needed here have bounded absolute coefficient sums. This last assertion costs only a finite power of \(L\): one step has a fixed finite number of input bonds and color coordinates. It is not applied to a depth-dependent coordinate count.

Fix a row of length \(s=L^j\eta\), put \(t_r=L^r\eta/s\), and work in its local regular gauge. The recursion is exactly
\[
 a_0=\eta a,\qquad a_{r+1}=F_{W_r}(a_r),\qquad
 W_r=\mathcal M^rU_0,
\tag{6}
\]
with the accumulated endpoint factors multiplied in their specified order. Gauge covariance proves the factorization by induction: apply one average to the previous factorization and remove its two new endpoint factors. No further factor growing with the number of steps appears.

Here is the uniform radius check. Write \(\alpha_r=\|\log W_r/i\|\), \(\omega_r=\|\partial W_r-1\|\). Straight products and the finite plaquette-sliding expansion in a one-step block give
\[
 \alpha_{r+1}\le L\alpha_r+C_L(\alpha_r^2+\omega_r),\quad
 \omega_{r+1}\le L^2(1+C_L\alpha_r)\omega_r+C_L\omega_r^2.
\tag{7}
\]
For the second inequality use the small comb gauge in that one block: the linear flux has exactly \(L^2\) terms, while all products containing at least two plaquette errors are bounded by their convergent geometric majorant. Undoing the gauge costs \(1+C_L\alpha_r\). These are finite one-step estimates. Initially \(\alpha_0\le C_L\kappa t_0\), \(\omega_0\le C_L\kappa t_0^2\). Dividing (7) by \(t_{r+1}\), respectively \(t_{r+1}^2\), bounds the normalized curvature by a product with logarithm at most \(C_L\sum_r t_r(\kappa+\kappa^2)\). Its bound is twice its initial bound when \(\kappa\) is small. The normalized potential has, in addition, an additive forcing bounded by \(C_L\kappa\sum_rt_r\). Choose its proposed bound larger than twice that forcing plus twice its initial bound; its quadratic contribution is then absorbed by decreasing \(\kappa\). This proves, by first exit,
\(\alpha_r\le C_L\kappa t_r\), \(\omega_r\le C_L\kappa t_r^2\).
The only series used is \(\sum_{r<j}t_r\le(L-1)^{-1}\).

If \(s\sup|a|\le r_*\), the same first-exit product from (5) gives
\(|a_r|\le2r_*t_r\), for a fixed sufficiently small \(r_*\). Hence
\[
 \|P_{v,u}\|_{\rm row}\le C_LL^{v-u},\qquad
 \|P_{v,u}\|_{\rm col}\le C_LL^{-3(v-u)},\qquad
 P_{v,u}=D F_{W_{v-1}}\cdots D F_{W_u}.
\tag{8}
\]
Indeed the extra product is at most
\(\exp(C_L(\kappa+r_*)\sum_rt_r)\).
The product of condition numbers of the endpoint factors has the same bound, since its logarithm is bounded by \(C_L\sum_r|a_r|\). Decrease \(r_*,\kappa\) so it is at most two. This supplies room for the complex means and all covariance identities used above.

### 4.2 Raw rows, transposes and weighted derivatives

Let \(q(a)=\mathcal Q^{\rm st}(a)\), \(K_a=q'(a)\), and
\(C(a)=q(a)-q(0)-K_0a\). Equation (8), multiplied by the physical input factor \(\eta\), yields for each row of length \(s\)
\[
 \sum_b|K_a(c,b)|\le C_Ls,\qquad
 |K_a(c,b)|\le C_L\eta^4s^{-3}.
\tag{9}
\]
These are counting-coordinate derivatives. The factor \(\eta^{-4}\) occurs only on taking the fine transpose. The row has its actual double-block support. A fine bond belongs to only a bounded number of such carriers, at adjacent scales. Thus (9) gives \(K_a^{\mathsf T}:Y_w\to F_w\), with bounded norm, as well as \(K_a:X_w\to Y_w\).

For completeness, Cauchy estimates preserve the density in (9). Fix an entry and a direction \(h\), and use the circle
\(|z|=r_*/(4s\sup_{S_c}|h|)\), where \(S_c\) is the carrier. On that circle the same entry bound holds. Dividing by the circle radius gives
\[
 |D K_a[h](c,b)|\le C_L\eta^4s^{-3}
                         (s\sup_{S_c}|h|).
\tag{10}
\]
Two circles give the corresponding bound on \(D^2K_a[h,k]\) with the product of the two normalized suprema. The zero-direction case follows by linearity. Entrywise integration from zero gives the extra factor \(\|a\|_X\) for \(K_a-K_0\), and for \(D K_a-D K_0\). Taking the row sums uses the row version of the same Cauchy argument; taking the transpose uses (10), the fine \(\eta^{-4}\), and bounded carrier overlap. This proves, for \(\|a\|_X\le r\le r_*/4\),
\[
 \begin{split}
 \|C'(a)h\|_{Y,w}&\le C r\|h\|_{X,w},\qquad
 \|C'(a)^{\mathsf T}p\|_{F,w}\le Cr\|p\|_{Y,w},\\
 \|(C''(a)[h,\cdot])^{\mathsf T}p\|_{F,w}
   &\le C\|h\|_{X,w}\|p\|_Y,\\
 \|((C''(a)-C''(0))[h,\cdot])^{\mathsf T}p\|_{F,w}
   &\le Cr\|h\|_{X,w}\|p\|_Y .
 \end{split}
\tag{11}
\]
The last two estimates also hold with the weight on \(p\) and the unweighted norm on \(h\). On a carrier, a weight changes by at most \(e^{\theta D_L}\); absorb that fixed number in \(C\). This is why these are estimates in every weight in (2), rather than just unweighted analytic bounds. There is no sum over all fine coordinates without its density factor.

### 4.3 The local Wilson remainder

Put \(F'(a)=J+F''(0)a+N_0(a)\). Then
\[
 \|N_0(a)\|_F\le Cr^2,\qquad
 \|N_0'(a)h\|_{F,w}\le Cr\|h\|_{X,w}.
\tag{12}
\]
Here is the local cancellation that prevents a fine-mesh loss. At one plaquette transport its four oriented variations to a common corner and write \(X_r=\eta a_r\). Its varied product is \(\prod_{r=1}^4e^{iX_r}P_0\). At \(P_0=1\), cyclicity gives the cubic trace as the sum of
\(\operatorname{tr}(\sum X_r)^3/6\) and
\(\operatorname{tr}[(\sum X_r)\sum_{r<s}[X_r,X_s]]/2\), with the common factor \(i^3\). The first vanishes for traceless two-by-two matrices. Since \(\sum X_r=\eta^2Da\), the remaining cubic action density is a fixed linear combination of \(Da\,[a_r,a_s]\). The cubic terms multiplied by \(P_0-1\), using \(|P_0-1|\le C\kappa\eta^2\xi^{-2}\), have differentiated density bounded by \(C\kappa\eta\xi^{-2}|a|^2\). Terms of degree at least four have differentiated density bounded by \(C|a|^3\): expand the four exponentials and sum their absolutely convergent series, using \(\eta|a|<r_*\). All constants are finite geometric majorants of those series.

For the leading cubic density, variation gives one term with \(Dh\) and two with \(h\). Summation by parts moves \(D\) off \(h\). At a common corner the commutator sum equals a fixed multiple of \([a_\mu,a_\nu]\), plus terms with a factor \(\eta\) and a first difference, and terms with two such factors. The covariant product identity
\[
 \nabla[a,b]=[\nabla a,b]+[a,\nabla b]
                         +\eta[\nabla a,\nabla b]
\tag{13}
\]
follows by substituting the transported neighboring values \(a+\eta\nabla a\), \(b+\eta\nabla b\). When a difference hits an already differentiated remainder, its preceding \(\eta\) cancels the inverse mesh, and \(\eta|\nabla^2a|\le C|\nabla a|\) on the enlarged stencil. Background commutators contribute at most \(C\kappa\eta\xi^{-2}|a|^2\). Thus the force is bounded by
\[
 C\bigl(|a||\nabla a|+\eta|\nabla a|^2
              +|a|^3+\kappa\eta\xi^{-2}|a|^2\bigr)
 \le Cr^2\xi^{-3}.
\]
Each bond meets at most six plaquettes. At the action boundary the missing neighboring plaquette can prevent a cancellation. That boundary is in layer zero, by separation from \(\Omega_1\), so \(\xi=\eta\) there: even the crude boundary term \(C\eta^{-1}|a|^2\) is at most \(Cr^2\xi^{-3}\). Thus the argument uses the actual inner-plaquette action, without inserting exterior plaquettes. Analytic differentiation on a local circle of radius \(r/\|h\|_{X,\mathrm{stencil}}\), using the bound at radius \(2r\), proves the second inequality in (12). Weight transfer is local as in (11). This is the force estimate behind CMP 102 (39), (85)–(98); it uses first differences, not a supposed Laplacian bound for a propagator.

## 5. The calculation omitted in (189)

One can keep the constraint nonlinear in the main proof (§6). Nevertheless the same bounds give the missing estimate for Balaban's straightened functional. This section supplies that calculation explicitly, using his construction CMP 102 (47)–(80), with credit to T. Balaban. It is useful also for checking that the nonlinear-constraint method has not suppressed a second variation.

Use bars for the *linear* operators before the constraint-current correction: \(\bar H:Y\to X\) is the lift with \(K_0\bar H=1\), \(RD^{\mathsf T}\bar H=0\). Write \(E\) for the symmetric quadratic extension of the Wilson Hessian used in CMP 102 (41). It agrees with that Hessian on the slice. Its construction gives
\[
 E\bar H=K_0^{\mathsf T}M,\qquad
 M=\bar H^{\mathsf T}E\bar H,
\tag{14}
\]
where \(M\), \(\bar H\) and \(\bar H^{\mathsf T}\) have the linear bounds in P82. These identities also follow by multiplying
\(\bar G^{-1}\bar H=K_0^{\mathsf T}(K_0\bar GK_0^{\mathsf T})^{-1}\)
and using the zero gauge term: \(M=(K_0\bar GK_0^{\mathsf T})^{-1}-1\).

Define \(d(a)\) and \(z(a)\) by
\[
 d(a)=C(a-\bar H d(a)),\qquad z(a)=a-\bar H d(a).
\tag{15}
\]
Since \(C\) starts quadratically, the map for \(d\) has Lipschitz constant \(Cr\) on a ball of radius \(Cr^2\), by (11). For \(r\) small it maps that ball into itself and is a contraction. Its iterates converge holomorphically. Moreover
\(q(z(a))=q(0)+K_0a\), exactly. Put
\[
 A=C'(z),\quad N=(1+A\bar H)^{-1},\quad
 d'=NA,\quad Z=z'=1-\bar H d'.
\tag{16}
\]
The inverse is its norm-convergent geometric series. The series and its transpose converge in every weighted space in (2), because (11) and P82 bound both \(A\bar H\) and \(\bar H^{\mathsf T}A^{\mathsf T}\) by \(Cr\). In particular
\[
 d'=O(r),\quad d'^{\mathsf T}=O(r),\quad
 Z-1=O(r),\quad Z^{\mathsf T}-1=O(r),\quad N-1=O(r),
\tag{17}
\]
in their respective spaces, with the same statements for \(N^{\mathsf T}\).

Differentiate (15) twice, retaining both terms in the derivative of \(z\). For arbitrary \(h,k\),
\[
 d''[h,k]=N C''(z)[Zh,Zk],\qquad
 (d''[h,\cdot])^{\mathsf T}p
   =Z^{\mathsf T}(C''(z)[Zh,\cdot])^{\mathsf T}N^{\mathsf T}p.
\tag{18}
\]
This identity controls the transposed leg as well as the ordinary derivative; an unweighted bound on \(d\) alone would not do that. It and (11), (17) give
\[
 \|(d''[h,\cdot])^{\mathsf T}p\|_{F,w}
       \le C\|h\|_{X,w}\|p\|_Y.
\]
Let \(d_2(a)=\tfrac12C''(0)[a,a]\), \(d_3=d-d_2\). Subtract the second derivative of \(d_2\) from (18). Insert successively \(Z^{\mathsf T}=1+(Z^{\mathsf T}-1)\), \(Zh=h+(Z-1)h\), \(N^{\mathsf T}=1+(N^{\mathsf T}-1)\), and
\(C''(z)=C''(0)+(C''(z)-C''(0))\).
Each difference has one factor \(Cr\), by (11), (17), and \(\|z\|_X\le2r\). Thus
\[
 \|(d_3''[h,\cdot])^{\mathsf T}p\|_{F,w}
       \le Cr\|h\|_{X,w}\|p\|_Y.
\tag{19}
\]
This subtraction is essential for the term containing the background current.

Let \(p_0=\bar H^{\mathsf T}J\), with \(\|p_0\|_Y\le C\kappa\). Denote the cubic-and-higher Wilson functional by \(V_0\), so its gradient is \(N_0\). Pulling the action back by (15), and separating its constant, linear and quadratic terms, gives exactly
\[
 V(a)=-\langle p_0,d_3(a)\rangle
       -\langle K_0a,Md(a)\rangle
       +\tfrac12\langle d(a),Md(a)\rangle+V_0(z(a)).
\tag{20}
\]
To verify the identity, expand the quadratic form at \(a-\bar Hd\), use (14), and split \(-\langle p_0,d\rangle\) into its quadratic term and \(-\langle p_0,d_3\rangle\). On the slice this is the original action; off the slice it is its specified quadratic extension, exactly as in Balaban's (80).

Differentiation gives
\[
 \begin{split}
 V'(a)={}&-d_3'{}^{\mathsf T}p_0-K_0^{\mathsf T}Md
       -d'{}^{\mathsf T}MK_0a+d'{}^{\mathsf T}Md
       +Z^{\mathsf T}N_0(z).
 \end{split}
\tag{21}
\]
Here is every term of its derivative in direction \(h\):
\[
 \begin{split}
 V''(a)h={}&-(d_3''[h,\cdot])^{\mathsf T}p_0
       -K_0^{\mathsf T}Md'h\\
 &-(d''[h,\cdot])^{\mathsf T}MK_0a
       -d'{}^{\mathsf T}MK_0h\\
 &+(d''[h,\cdot])^{\mathsf T}Md
       +d'{}^{\mathsf T}Md'h\\
 &-(d''[h,\cdot])^{\mathsf T}\bar H^{\mathsf T}N_0(z)
       +Z^{\mathsf T}N_0'(z)Zh.
 \end{split}
\tag{22}
\]
By (19), the first has norm at most \(C\kappa r\|h\|_{X,w}\). The next three have norm at most \(Cr\|h\|_{X,w}\): respectively use \(d'=O(r)\), \(K_0a=O(r)\), and \(d'{}^{\mathsf T}=O(r)\). The next two are \(O(r^2)\|h\|_{X,w}\), since \(d=O(r^2)\) and both first derivatives are \(O(r)\). The penultimate one is \(O(r^2)\|h\|_{X,w}\), by (12) and (18). The last is \(O(r)\|h\|_{X,w}\), by (12) and boundedness of \(Z,Z^{\mathsf T}\). All compositions here are between the spaces specified above; the weight is carried by the differentiated leg. Consequently
\[
                 \|V''(a)h\|_{F,w}\le Cr\|h\|_{X,w}.
\tag{23}
\]
If \(h\) is supported in a pillar or its fixed enlarged cube at \(y'\), choose \(w(y)=e^{\delta_0d(y,y')/4}\). Its norm on that support and its first-difference stencil is bounded by a fixed multiple of the unweighted norm. Equation (23) becomes
\[
 |V''(a)h|_y\le Cr\,\xi_y^{-3}
       e^{-\delta_0d(y,y')/4}\max\{|h|_{(-1)},|\nabla h|_{(-2)}\}.
\tag{24}
\]
This is (189), with \(r\) the \(\varepsilon_3\) radius and with its actual derivative norm. The proof does not infer off-diagonal decay from an unweighted Cauchy estimate: locality (11), the transposed identity (18), and the weighted linear estimates are used separately.

## 6. Solve and differentiate the actual critical equations

This proof uses the nonlinear constraint directly. It also provides the multiplier readout which a field-only inverse can miss. The exact Lagrange Hessian and block algebra follow the source equations BGR1–BGR9 (SA 11735–11870), credited to Sussman and Alpoge with Claude and Codex as authors; the nonlinear estimates are those just proved.

Let \(\nu=\lambda-\lambda_0\), and set
\[
 \begin{split}
 N_1(a,\nu)={}&N_0(a)
 -\{(K_a-K_0)^{\mathsf T}\lambda_0-W_0a\}
 -(K_a-K_0)^{\mathsf T}\nu,\\
 N_2(a,\nu)={}&C(a).
 \end{split}
\tag{25}
\]
There is no omitted constraint-curvature term. In particular
\(W_0a=(D K_0[a])^{\mathsf T}\lambda_0\), and its subtraction makes the braces quadratic. Equations (11)–(12) imply on \(\|a\|_X+\|\nu\|_Y\le r\)
\[
 \|N_1\|_F+\|N_2\|_Y\le C_Nr^2,\quad
 \|D N(a,\nu)(h,\sigma)\|_{F_w\oplus Y_w}
       \le C_Nr(\|h\|_{X,w}+\|\sigma\|_{Y,w}).
\tag{26}
\]
For the braces use the last line of (11) multiplied by \(\lambda_0\); for the last term use the two product-rule terms
\(-(DK_a[h])^{\mathsf T}\nu\) and \(-(K_a-K_0)^{\mathsf T}\sigma\).
These account for every derivative in (26).

Write
\[
 S_0=\begin{pmatrix}L_0+DRD^{\mathsf T}&-K_0^{\mathsf T}\\K_0&0\end{pmatrix}.
\]
Its inverse is
\[
 S_0^{-1}(f,b)=
 \bigl(Tf+Hb,\ -H^{\mathsf T}f+(C_0^{-1}-1)b\bigr).
\tag{27}
\]
Indeed \(K_0T=0\), \(K_0H=1\), and multiplication of the first component by \(G^{-1}-K_0^{\mathsf T}K_0\) leaves
\(f+K_0^{\mathsf T}[-C_0^{-1}K_0Gf+(C_0^{-1}-1)b]\).
Since \(H^{\mathsf T}=C_0^{-1}K_0G\), this is the first equation. The same identities give zero for a homogeneous solution. Thus (27) is an exact inverse, and (4) is the required bound for it.

The gauge-augmented equations are
\[
 F'(a)+DRD^{\mathsf T}a=K_a^{\mathsf T}(\lambda_0+\nu),
                  \qquad q(a)=\mathsf b(B).
\tag{28}
\]
They are exactly the fixed-point equation
\[
 (a,\nu)=S_0^{-1}\bigl(-N_1(a,\nu),\mathsf b(B)-N_2(a,\nu)\bigr).
\tag{29}
\]
Here \(q(0)=\mathsf b(0)=0\). At an interior row, \(\mathsf b(B)=B\); at an outward row its extra factor uses only the finer determining bonds in the outer endpoint block. It is a fixed finite one-step function, holomorphic on a fixed ball. Hence \(\|\mathsf b(B)\|_Y\le C_b\|B\|_\infty\), and a single datum bond enters only a fixed number of rows at distance at most \(D_L\). The same local Cauchy argument gives
\[
 \|D\mathsf b(B)e_c\|_{Y,w_{y_c}}\le C_b e^{\theta D_L}|e|.
\tag{30}
\]
The coarse datum is therefore differentiated before substitution, including the outward-node factor.

Choose \(r<r_*/8\) so that \(C_{\rm lin}C_Nr\le1/4\), and then choose
\(r_B\le r/(4C_{\rm lin}C_b)\), also within the real-data and analytic-chart ceiling of P81. Decrease it once more if required to put the closed doubled datum ball inside those ceilings. Equation (29) maps the closed radius-\(r\) ball into its radius-\(r/2\) ball and is a contraction with constant at most \(1/4\). Its iterates starting at zero converge geometrically, uniformly on the datum ball. They are holomorphic, so their limit is holomorphic: on each finite-dimensional complex line, the Cauchy integral formula passes through the uniform limit and proves complex differentiability. Uniqueness holds in the radius-\(r\) ball. The estimate from (29) also gives
\[
             \|a(B)\|_X+\|\nu(B)\|_Y\le 2C_{\rm lin}C_b\|B\|_\infty.
\tag{31}
\]

Differentiate (28), with the reference \(U_0,D,R\) held fixed. Put \(h=\partial_{e_c}a\), \(\dot\lambda=\partial_{e_c}\nu\). The Hessian is
\[
 L_a h=F''(a)h-(D K_a[h])^{\mathsf T}\lambda,
\]
and the exact equations are
\[
 (L_a+DRD^{\mathsf T})h-K_a^{\mathsf T}\dot\lambda=0,
             \qquad K_a h=D\mathsf b(B)e_c.
\tag{32}
\]
Equivalently,
\[
 (1+S_0^{-1}DN(a,\nu))(h,\dot\lambda)
                    =S_0^{-1}(0,D\mathsf b(B)e_c).
\tag{33}
\]
In every weight under consideration the perturbation has norm at most \(1/4\), by (26). Its inverse is the absolutely convergent geometric series, whose norm is at most \(4/3\). Taking \(\theta=\delta_0/8\), (4), (30) and (33) prove, on the entire datum polydisc,
\[
 \xi_y|h|_y+\xi_y^2|\nabla h|_y
       +|\dot\lambda|_y
       \le C e^{-\delta_0 d(y,y_c)/8}|e|.
\tag{34}
\]
No number of layers occurs in the smallness choice or in the inverse-series bound. This proves the potential/gradient part of (190), conditional on precisely P81–P82, once the gauge identification below is made.
