lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T03:35Z

# A3: derivative of the constrained background
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed; requested effort: max); checkout `1ddede8fb5da70ea56d528637c22ee0092d22b70`; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, `31a47c543775`; T. Balaban, CMP **102** (1985), 277–309, **99** (1985), 389–434, and the averaging/gauge inputs CMP **98** (1985), 17–52 and **99** (1985), 75–102; research text, not an audit, granting no status.
Continuation (Sections 6.1 to 12) and review of Sections 1 to 6: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, checkout `63a8c52e2`; outline re-fetched at `31a47c543775` (sha256 `d7f77d4d...4d6f`, matches `sa-map.md`) into a private scratch folder; Balaban's CMP 102 read from `~/ym4d-papers/cmp102.txt`, pp. 306-309. Same caveat: research text, not an audit, no status. Sections 1 to 6 are Codex's, kept verbatim; my corrections to them are in Section 11.

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

### 6.1 The fixed point is the Landau pair of Theorem 3

*From here on the text is the Claude continuation.* Equation numbers continue from (34). Section 6 left one step open: the solution of the gauge-augmented system (28) has not yet been shown to satisfy \(RD^{\mathsf T}a=0\), or to be the potential \(\mathcal H\) of Theorem 3. This subsection closes that step. It uses no premise beyond P81 and P82 and the outline's own definitions. Every argument is finite-dimensional, so a neighbourhood that is not uniform is allowed wherever the identity theorem then carries the identity to the whole polydisc. This is the device of SA 10580 (k), credited to Sussman and Alpoge with Claude and Codex as authors.

**Notation.** For a \(\mathfrak g^c\)-valued 0-form \(\chi\), let \(X_\chi(A)\) be the generator of the gauge action in the chart, defined by \(e^{i\eta(A+tX_\chi(A)+O(t^2))}U_0=(e^{i\eta A}U_0)^{e^{it\chi}}\). It is holomorphic in small \(A\), linear and local in \(\chi\), and \(X_\chi(0)=-D\chi\), because \(e^{it\chi(x)}U(x,x+e_\mu)e^{-it\chi(x+e_\mu)}=e^{-it\eta\nabla_\mu\chi(x)+O(t^2)}U(x,x+e_\mu)\). Let \(m(A)=M_{\mathbf B}(e^{i\eta A}U_0)\) be the plain constraint map, \(v[A](y)\) the node factor of the node's **own** level (\(v_j\) at a top of level \(j\)), and \(\tilde q(A)\) the straightened rows with the outward block factor moved into the row. Thus \(\tilde q=\mathcal Q^{\rm st}\) on interior rows; at an outward row \(c\) with outer end \(z\), \(e^{i\tilde q(A)(c)}\mathbf V_0(c)=e^{i\mathcal Q^{\rm st}(A)(c)}\mathbf V_0(c)\,\mathsf v_{j-1}(z)[A]^{-1}\). The chart formula SA 9628–9630, with \(v_j(z)=v_{j-1}(z)\mathsf v_{j-1}(z)\), then reads
\[
 m(A)(c)=v[A](c_-)\,e^{i\tilde q(A)(c)}\,\mathbf V_0(c)\,v[A](c_+)^{-1},
\tag{35}
\]
with one factor per node. The block factor \(\mathsf v_{j-1}(z)[A]\) is the block mean of the level-\((j-1)\) straightened field on the bonds inside \(B(z)\) (SA 7092–7096). These bonds are interior rows of \(\Gamma_{j-1}\) (SA 9614). Hence \(\mathsf v_{j-1}(z)[A]=\mathsf v_z(\tilde q(A)|_{B(z)})\). Comparing with the reduced datum SA 9640 gives \(\tilde q(A)=B\iff\mathcal Q^{\rm st}(A)=\mathsf b(B)\). It also gives \(D\tilde q_A=\mathcal T_AK_A\), with \(\mathcal T_A\) the identity plus a part that is nilpotent of order two (outward rows read interior rows only), so \(\ker D\tilde q_A=\ker K_A\) and \(\operatorname{ran}D\tilde q_A^{\mathsf T}=\operatorname{ran}K_A^{\mathsf T}\).

**Lemma 6.1 (node factor along a pure gauge).** Let \(A_t\) be defined by \(e^{i\eta A_t}U_0=U_0^{e^{it\chi}}\). At every node \(y\),
\[
 \tfrac{d}{dt}v[A_t](y)\big|_{t=0}=i\big(\chi(y)-(Q'\chi)(y)\big),
\tag{36}
\]
where \(Q'\) is the pillar average of SA 9634.

*Proof.* Federbush's mean (SA 7065) is the solution of \(\sum_i\log(V_iV^{-1})=0\). It is left and right equivariant, so the averaged contour variables are covariant: \(W^g(y,x)=g(y)W(y,x)g(x)^{-1}\). At one step, with \(W=W_0^{e^{it\chi}}\),
\(W(y,x)W_0(y,x)^{-1}=e^{it\chi(y)}e^{-it\operatorname{Ad}(W_0(y,x))\chi(x)}\). The block factor \(\mathsf u(y)=\exp(L^{-4}\sum_{x\in B(y)}\log[W(y,x)W_0(y,x)^{-1}])\) therefore has derivative \(i(\chi(y)-q\chi(y))\), where \(q\) is the one-step transported site mean, the linear part of \(\bar R_{W_0}\) (SA 7110–7112). This is the linearization of SA 7792, \(\mathsf u(W_0,\mathsf a^w)=w(\bar R_{W_0}w)^{-1}\). By the covariance of \(\mathcal M\) (SA 7072–7080), the next straightened field \(\mathsf u(c_-)^{-1}\mathcal M(W)(c)\mathsf u(c_+)\) is, to first order, the pure gauge of \(\mathcal M(W_0)\) by \(e^{itq\chi}\). Induction over the steps \(v_{n+1}=v_n\mathsf u_n\) telescopes:
\(\tfrac d{dt}v_j(y)=i\sum_{n<j}(\chi_n(y)-\chi_{n+1}(y))=i(\chi(y)-\chi_j(y))\), with \(\chi_{n+1}=q_n\chi_n\) and \(\chi_j=Q'\chi\) at the top. \(\square\)

**Lemma 6.2 (criticality gives the multiplier equation).** Let \(A\) be in the chart with \(K_A\) onto, and let \(e^{i\eta A}U_0\) be critical (SA 9616) for the datum it carries. Then \(F'(A)=K_A^{\mathsf T}\omega\) for exactly one \(\omega\).

*Proof.* Let \(h\in\ker K_A\). By (35), \(Dm_A(h)(c)=i[\sigma(c_-)m(c)-m(c)\sigma(c_+)]\) with \(i\sigma=(Dv[A]h)v[A]^{-1}\). Exact covariance gives \(Dm_A(X_\chi(A))(c)=i[\chi(c_-)m(c)-m(c)\chi(c_+)]\). Take \(\chi=\sigma\) at the nodes. Then \(h-X_\chi(A)\in\ker Dm_A\). By (35), \(m\) is a submersion because \(\tilde q\) is, so \(\ker Dm_A\) is the tangent space of the constraint set. Criticality and gauge invariance of \(A_{\Omega_0}\) give \(\langle F'(A),h-X_\chi\rangle=0=\langle F'(A),X_\chi\rangle\). Hence \(F'(A)\) annihilates \(\ker K_A\), and finite-dimensional duality gives \(\omega\). \(\square\)

**Lemma 6.3 (a Landau pair near \(B=0\)).** Assume P81 in the form used here: \(\Phi\) is holomorphic, \(\Phi(0)=U_0\), \(M_{\mathbf B}\Phi(B)=e^{iB}\mathbf V_0\), and \(\Phi(B)\) is critical for real \(B\). There is a real neighbourhood \(N\) of \(0\), and a real-analytic pair \((H_N,u_N)\) on it with value \((0,\mathbf 1)\) at \(0\), such that
\(\Phi(B)=(e^{i\eta H_N}U_0)^{u_N}\), \(RD^{\mathsf T}H_N=0\), and \(u_Nv[H_N]=\mathbf 1\) at the tops. It is unique among pairs near \((0,\mathbf 1)\).

*Proof.* Put \(A_B=\frac1{i\eta}\log(\Phi(B)U_0^{-1})\) bondwise, so \(A_B\to0\). Define \(A^g\) by \(e^{i\eta A^g}U_0=(e^{i\eta A}U_0)^g\), and
\(\Psi(A,g)=(RD^{\mathsf T}A^g,\ (g^{-1}v[A^g])|_{\rm tops})\). Then \(\Psi(0,\mathbf 1)=(0,\mathbf 1)\). By \(X_\chi(0)=-D\chi\) and (36), its \(g\)-derivative at \((0,\mathbf1)\) in the direction \(i\chi\) is \((-R\Delta\chi,\,-iQ'\chi)\). The map \(\chi\mapsto(R\Delta\chi,Q'\chi)\) is an isomorphism onto \(\operatorname{ran}R\oplus\mathfrak g^{c,\rm tops}\). Indeed \(Q'\) is onto, and \(R\Delta:\ker Q'\to\operatorname{ran}R\) is an isomorphism (P82; directly: \(\operatorname{ran}R=\Delta\ker Q'\) by definition, and \(\Delta\chi=0\), \(Q'\chi=0\) force \(\chi=0\) for a regular \(U_0\), since a covariantly constant \(\chi\) satisfies \(|Q'\chi(y)-\chi(y)|\le C_L\kappa|\chi(y)|\) by the pillar transport bound SA 10742). The holomorphic implicit function theorem gives a unique \(g(A)\) near \(\mathbf 1\) with \(\Psi(A,g(A))=(0,\mathbf 1)\). Put \(H_N=A_B^{g(A_B)}\) and \(u_N=g(A_B)^{-1}\). Reality holds because \(\Psi\) is real on real arguments. \(\square\)

**Proposition 6.4 (identification; Theorem 3, second paragraph).** Under P81, P82 and the choices of Section 6, Theorem 3's Landau pair exists on the whole datum polydisc and is unique. It is \((\mathcal H,u)=(a,u_B)\), with multiplier \(\omega=\lambda_0+\nu\). On the whole polydisc,
\[
 RD^{\mathsf T}a=0,\qquad F'(a)=K_a^{\mathsf T}\omega,\qquad \mathcal Q^{\rm st}(a)=\mathsf b(B),\qquad u_Bv[a]=\mathbf 1\ \text{at the tops}.
\tag{37}
\]

*Proof.* Let \(B\in N\) be real. The configuration \(\Phi(B)^{u_N^{-1}}=e^{i\eta H_N}U_0\) is critical for its node-conjugated datum, since action and constraint sets are gauge covariant. Lemma 6.2 gives \(F'(H_N)=K_{H_N}^{\mathsf T}\omega_N\). Here \(\omega_N\) is continuous, and \(\omega_N(0)=\lambda_0\) since \(J=K_0^{\mathsf T}\lambda_0\) and \(K_0\) is onto. By (35) and \(u_Nv[H_N]=\mathbf 1\) at the tops, \(m(H_N)(c)=u_N(c_-)^{-1}e^{iB(c)}\mathbf V_0(c)u_N(c_+)=v(c_-)e^{i\tilde q(H_N)(c)}\mathbf V_0(c)v(c_+)^{-1}\). So \(\tilde q(H_N)=B\), that is \(\mathcal Q^{\rm st}(H_N)=\mathsf b(B)\). With \(RD^{\mathsf T}H_N=0\), the pair \((H_N,\omega_N-\lambda_0)\) solves (28). On a smaller \(N\) it lies in the radius-\(r\) uniqueness ball of (29), so it equals \((a(B),\nu(B))\). The holomorphic function \(RD^{\mathsf T}a(B)\) vanishes on \(N\), hence on the polydisc, and (28) becomes (37). For complex \(B\), define \(u_B\) along a spanning tree from one top \(y_0\): \(u_B(y_0)=v[a](y_0)^{-1}\), and \(u(x')=\Phi(B)(x,x')^{-1}u(x)\,(e^{i\eta a}U_0)(x,x')\) along tree bonds. The relation \(\Phi(B)=(e^{i\eta a}U_0)^{u_B}\) on non-tree bonds, and \(u_Bv[a]=\mathbf 1\) at the other tops, are holomorphic identities. They hold on \(N\), where \(u_B=u_N\), so they hold everywhere. For uniqueness, any holomorphic pair with value \((0,\mathbf 1)\) at \(0\) is near \((0,\mathbf 1)\) for small real \(B\); by Lemma 6.3 it equals \((H_N,u_N)\) there, and it equals \((a,u_B)\) everywhere by the identity theorem. Reality for \({}^{\mathfrak c}\) follows from uniqueness of the fixed point, since every ingredient of (29) commutes with \({}^{\mathfrak c}\). \(\square\)

So A1's uniqueness is used only through P81's \(\Phi\); no transversality is needed away from \(A=0\). The outline's (k) asserts transversality at every small \(\mathbf H\), which is not needed here.

## 7. The remaining members of Theorem 4 at a critical reference

Fix \(B\) in the polydisc, a direction \(e\) at the bond \(c\), and put \(h=\partial_{e_c}a\), \(\dot\omega=\partial_{e_c}\nu\), \(\theta=\delta_0/8\), and \(w(y)=e^{\theta d_{\mathbf B}(y,y_c)}\). By (34),
\(\|h\|_{X,w}+\|\dot\omega\|_{Y,w}\le C_1|e|\). Differentiating (37) at the fixed reference gives
\[
 F''(a)h=(DK_a[h])^{\mathsf T}\omega+K_a^{\mathsf T}\dot\omega,\qquad RD^{\mathsf T}h=0,\qquad K_ah=D\mathsf b(B)e_c .
\tag{38}
\]
Here \(|\omega|_Y\le|\lambda_0|+\|\nu\|_Y\le C(\kappa+r)\).

**7.1 The member \(D^{\mathsf T}D\mathsf h\).** By SA 9627, \(F''(0)=\Delta^{\rm W}_{U_0}=D^{\mathsf T}D+\Delta'\), and \(F''(a)=F''(0)+N_0'(a)\). *Local bound for \(\Delta'\):* the exact plaquette Hessian PX114 (SA 11313–11327) has remainder \(|\mathcal R_p(v,w)|\le C\|P-1\|\eta^2|v|_p|w|_p\), with \(\|P-1\|\le\kappa\eta^2\mathsf L^{-2}\). The exponential chart differs from left variations by the Baker–Campbell–Hausdorff term, which contributes \(\eta^4\sum_bO(\eta|J||v||w|)\) with \(|J|\le C\kappa\mathsf L^{-3}\). In the pairing \(\eta^4\sum_b\), these give
\(|\Delta'v|(b)\le C\kappa\mathsf L(b)^{-2}\max_{p\ni b}|v|_p\). Hence \(\|\Delta'v\|_{F,w}\le C\kappa\|v\|_{X,w}\). From (38),
\[
 D^{\mathsf T}Dh=(DK_a[h])^{\mathsf T}\omega+K_a^{\mathsf T}\dot\omega-\Delta'h-N_0'(a)h ,
\]
and (9), (11), (12) bound each term:
\[
 \xi_y^3|D^{\mathsf T}Dh|_y\le C\big((\kappa+r)\|h\|_{X,w}+\|\dot\omega\|_{Y,w}\big)w(y)^{-1}\le C e^{-\theta d_{\mathbf B}(y,y_c)}|e| .
\tag{39}
\]

**7.2 The Laplacian member, by a lattice Weitzenböck identity.** Use start-point transport, \(\nabla_\mu f(x)=\eta^{-1}[\operatorname{Ad}(U(x,x+e_\mu))f(x+e_\mu)-f(x)]\), for site functions and for the components \(h_\nu(x)\) of 1-forms. Then \((Dh)_{\nu\mu}=\nabla_\nu h_\mu-\nabla_\mu h_\nu\) and \(D^{\mathsf T}h=\sum_\nu\nabla_\nu^{\mathsf T}h_\nu\). Expanding \((D^{\mathsf T}D+DD^{\mathsf T})h_\mu=\sum_\nu\nabla_\nu^{\mathsf T}\nabla_\nu h_\mu+\sum_\nu[\nabla_\mu,\nabla_\nu^{\mathsf T}]h_\nu\) gives the exact identity
\[
 \Delta_Uh_\mu=(D^{\mathsf T}Dh)_\mu+(DD^{\mathsf T}h)_\mu-\sum_{\nu\ne\mu}[\nabla_\mu,\nabla_\nu^{\mathsf T}]h_\nu ,
\tag{40}
\]
at every bond whose neighbours lie in \(\Omega_0\). The term \(\nu=\mu\) is absent, since transports along one line compose. For \(\nu\ne\mu\), direct expansion gives
\([\nabla_\mu,\nabla_\nu^{\mathsf T}]f(x)=\eta^{-2}[\operatorname{Ad}(T_1)-\operatorname{Ad}(T_2)]f(x+e_\mu-e_\nu)\), where \(T_1,T_2\) are the two transports from \(x+e_\mu-e_\nu\) to \(x\) around one plaquette. So the commutator is at most \(C\eta^{-2}|\partial U(p)-\mathbf 1||f|\le C\kappa\mathsf L^{-2}|f|\). Another transport convention changes (40) only by terms of the same kind. Now \(DD^{\mathsf T}h=DRD^{\mathsf T}h+D(1-R)D^{\mathsf T}h=D(1-R)D^{\mathsf T}h\) by (38). P82's member \(D(1-R)D^{\mathsf T}:X_w\to F_w\), together with (39) and (40), gives
\(\xi_y^3|\Delta_{U_0}h|\le Ce^{-\theta d_{\mathbf B}(y,y_c)}|e|\) at those bonds. This member belongs to the scalar gauge sector. It is not the covariant-Laplacian bound for \(G\) that Balaban's CMP 99b Theorem 3.12 excludes (SA 11714).

**7.3 The current member.** \(J(U)\) is the left-variation gradient of the action (SA 7375). With \(U_a=e^{i\eta a}U_0\), \(F'(a)=\Xi_a^{\mathsf T}J(U_a)\), where \(\Xi_a=\sum_{n\ge0}(\operatorname{ad}i\eta a)^n/(n+1)!\) acts bond by bond and \(|\Xi_a-1|\le C\eta|a|\le Cr\). Differentiating \(J(U_a)=(\Xi_a^{\mathsf T})^{-1}F'(a)\) and using (38) gives
\(\delta J=(\Xi_a^{\mathsf T})^{-1}[(DK_a[h])^{\mathsf T}\omega+K_a^{\mathsf T}\dot\omega]+O(\eta|h|)\,|K_a^{\mathsf T}\omega|\). The last term is at most \(C(\kappa+r)\eta\mathsf L^{-3}|h|\). So \(\xi_y^3|\delta J|\le Ce^{-\theta d_{\mathbf B}(y,y_c)}|e|\) at every bond whose plaquettes lie in \(\Omega_0\), where \(J\) is the gradient of \(A_{\Omega_0}\).

**7.4 The Hölder member.** By (33), \((h,\dot\omega)=S_0^{-1}(f',b')\) with \(f'=-D_{(a,\nu)}N_1(h,\dot\omega)\) and \(b'=D\mathsf b(B)e_c-DN_2(a)h\). Both have weighted norm at most \(C|e|\), by (26) and (30). P82's Hölder member for the field output (with \(\alpha_{\rm H}\) fixed) gives
\(|\nabla h(b)-\nabla h(b')|\le C\xi_y^{-2-\alpha_{\rm H}}|b-b'|^{\alpha_{\rm H}}e^{-\theta d_{\mathbf B}(y,y_c)}|e|\) for \(|b-b'|\le\xi_y\), with the covariant comparison along a straight path.

**7.5 Multiplier and top factor.** The bound \(|\dot\omega(c')|\le Ce^{-\theta d_{\mathbf B}(y_{c'},y_c)}|e|\) is (34), in the counting normalization of Section 3. If the outline's datum pairing carries cell weights \(\mu_c\), its multiplier is \(\mu_c^{-1}\omega\), and the bound has to be converted; this is matching item M1 of Section 12. By (37), \(u_B=v[a]^{-1}\) at the tops. The node factor of a top \(y\) of level \(j\) is a product of \(j\) block means. The \(n\)-th mean reads the level-\(n\) straightened field in \(B^{n+1}(y)\subset B^j(y)\), whose derivative in the fine field has row norm at most \(C_LL^n\eta\), by (5) and (8). The means are Lipschitz (Section 4.1). So
\(|\dot u(y)|\le C_L\sum_{n<j}L^n\eta\sup_{B^j(y)}|h|\le C\sup_{B^j(y)}\mathsf L|h|\le Ce^{-\theta d_{\mathbf B}(y,y_c)}|e|\). The pillar has \(d_{\mathbf B}\)-diameter \(O(1)\), and its bonds have scale \(\xi_y\) within a factor \(L\).

**7.6 The bounds of Theorem 3.** \(\|\mathcal H(B)\|_X\le C\sup|B|\) is (31). Subtracting \(J=K_0^{\mathsf T}\lambda_0\) from (37) gives \(D^{\mathsf T}Da=K_0^{\mathsf T}\nu+(K_a-K_0)^{\mathsf T}\omega-\Delta'a-N_0(a)\), so \(|D^{\mathsf T}D\mathcal H(B)|_{(-3)}\le C\sup|B|\). Also \(|u_B-\mathbf 1|\le C\sup_{\rm pillar}\mathsf L|a|\le C\sup|B|\) at the tops. The regularity radius \(C(\varepsilon_1+\sup|B|)\) of \(\Phi(B)\) follows from \(|\nabla a|\) and 7.3 at \(B\).

**7.7 Higher datum derivatives.** Since (34) holds on the whole polydisc, Cauchy's formula on polydiscs of radius \(c_*(1-\vartheta)r_{\rm B}\) about points of the \(\vartheta r_{\rm B}\)-ball gives the outline's (BGR25)–(BGR27) (SA 12160–12215). I checked the argument: it uses only the supremum datum norm, so the number of bonds does not enter. The same applies to every member above, Hölder included, because each one is bounded on the larger ball before Cauchy is applied.

**Conclusion of Sections 6–7.** Conditional on P81 and P82, the first paragraph of Theorem 4 holds on the whole polydisc, with rate \(\delta_0/8\), constants independent of depth, volume and regions, and every listed member. This is Balaban's CMP 102 (190), the estimate he states and does not prove ("We do not perform these calculations here", p. 308). It is proved here in the outline's Landau gauge, with the kernel convention of Section 1. The second-variation calculation that Balaban omits at (189) is not needed on this route: the constraint is kept nonlinear, and every nonlinear term is local (Section 4).

## 8. The linear input can be smaller than P82 as stated

Section 3 asks row 82 for the inverse of \(S_0\), whose field block \(L_0+DRD^{\mathsf T}\) contains the curvature term \(\Delta'\) and the constraint-curvature term \(W_0\). It also asks for an identification of Balaban's current corrections with \(W_0\). Neither request is needed.

**Lemma 8.1.** Let \(S^\circ=\begin{pmatrix}D^{\mathsf T}D+DRD^{\mathsf T}&-K_0^{\mathsf T}\\K_0&0\end{pmatrix}\) at the real regular reference. Suppose \(S^\circ\) has the bounds (4) with constant \(C^\circ\), the Hölder member and the member \(D(1-R)D^{\mathsf T}:X_w\to F_w\). Then Sections 6–7 hold with \(S^\circ\) in place of \(S_0\), once \(\kappa\) and \(r\) are small with respect to \(C^\circ\).

*Proof.* By 7.1 and by (11) with \(p=\lambda_0\), \(\|(\Delta'-W_0)v\|_{F,w}\le C_2\kappa\|v\|_{X,w}\). Move \((\Delta'-W_0)a\) into the field remainder, \(N^\circ_1=N_1+(\Delta'-W_0)a\). Then (26) holds with Lipschitz constant \(C_Nr+C_2\kappa\). Choose \(C^\circ C_2\kappa\le1/8\) and \(C^\circ C_Nr\le1/8\). Then (29), (31), (33), (34) and 7.1–7.6 hold verbatim, because \(S_0\) entered only through (4) and its members. For 7.4, write the field output as \(S^{\circ-1}\) of a force that includes \(-(\Delta'-W_0)h\). The smallness of \(\kappa\) is allowed: \(\kappa=C_L\mathfrak M\bar\varepsilon\), and Theorem 4 assumes \(\bar\varepsilon\le c(L)/\mathfrak M\), with \(\bar\varepsilon\) chosen after \(\mathfrak M\). \(\square\)

**Lemma 8.2 (what "weighted" must mean).** Let \(\mathcal W_\theta\) be the class of positive \(w\) with \(w(y)\le e^{\theta d_{\mathbf B}(y,z)}w(z)\). The bound (4) holds for every \(w\in\mathcal W_\theta\) if and only if each block of the kernel of \(S^{\circ-1}\) has the weighted row sums of SA (BGR11), first line, at rate \(\theta\), with the amplitudes of (2). The implication from row sums to (4) is the computation of SA (BGR19). For the converse, fix \(i\) and use \(w=e^{-\theta d_{\mathbf B}(\cdot,i)}\in\mathcal W_\theta\) (triangle inequality), with a test vector \(v_j=s_je^{\theta d(i,j)}\) times unit colour phases. \(\square\)

So P82's "weighted summation statements" are exactly these row sums, and Section 3's phrase "uniformly in the weight centre" should read "for every \(w\in\mathcal W_\theta\)". Section 10 uses the set-distance weight \(e^{\theta d_{\mathbf B}(\cdot,W^c)}\), which belongs to \(\mathcal W_\theta\).

**Remark (unproved; for row 82).** Balaban's propagators use his comb rows and \(R^{\mathsf c}\). The difference \(S^\circ(R)-S^\circ(R^{\mathsf c})\) is \(D(R-R^{\mathsf c})D^{\mathsf T}\oplus0\), and the rows differ by \(K_0-K^{\rm B}\). Suppose both differences are \(O(\kappa)\) as maps \(X_w\to F_w\), respectively \(X_w\to Y_w\) together with the transposed leg. Then the same Neumann series carries a comb-slice inverse to the outline's \(R\) and \(K_0\). These are comparisons in the scalar sector and in the rows, not propagator bounds. They are not proved here. At \(\mathbf V_0=\mathbf 1\) both differences vanish (SA 9732).

## 9. The other two paragraphs of Theorem 4

**9.1 Regular references that are not critical.** Let the reference \(U\) be regular, real or complex, with current \(J=F'_U(0)\) and \(\|J\|_F\le\varepsilon\), possibly with \(J\notin\operatorname{ran}K_0^{\mathsf T}\). The system \(F'(a)+DRD^{\mathsf T}a=K_a^{\mathsf T}\lambda\), \(\mathcal Q^{\rm st}(a)=\mathsf b(B)\) becomes
\((a,\lambda)=S^{\circ-1}(-J-N^\circ(a,\lambda),\ \mathsf b(B)-C(a))\), with \(N^\circ=\Delta'a+N_0(a)-(K_a-K_0)^{\mathsf T}\lambda\) and no \(W_0\). On the radius-\(r\) ball this map is a \(1/4\)-contraction into itself once \(C^\circ(\varepsilon+C_b\sup|B|)\le r/2\). So the system has one small solution, of size \(C(\varepsilon+\sup|B|)\), analytic in \(B\). It is analytic in \(U\) wherever \(S^{\circ-1}\) is analytic in \(U\) with the bounds (4); that is P82 on the complex domain. Its response obeys (33), so the members for \(h\), \(\nabla h\), \(\dot\lambda\) and Hölder hold as in 7.4. The differentiated equation gives
\((D^{\mathsf T}D+DRD^{\mathsf T})h=K_a^{\mathsf T}\dot\lambda+(DK_a[h])^{\mathsf T}\lambda-\Delta'h-N_0'(a)h\), bounded as in (39). P82 gives \(D(1-R)D^{\mathsf T}h\), and (40) with \(DD^{\mathsf T}=DRD^{\mathsf T}+D(1-R)D^{\mathsf T}\) gives \(\Delta_Uh\). This is exactly the outline's list of second-order members away from criticality. *Limit:* for a pair \((\mathbf U,\mathbf J)\) whose current is an independent variable, the outline itself says the system needs a separately specified operator (SA 11798, "an independent-current extension is an additional specified operator"). Once that operator is specified, the same contraction applies if it differs from \(\Delta'\) by \(O(\varepsilon)\) in \(X_w\to F_w\). Until then that case is a specification item, not a proof item.

**9.2 \(\mathbf V_0=\mathbf 1\) on a single lattice.** Here \(U_0=\mathbf 1\), \(\lambda_0=0\), \(\Delta'=W_0=0\), \(a(0)=\nu(0)=0\), and \(DN(0,0)=0\). There are no outward rows, so \(\mathsf b(B)=B\). By (33), \(\mathsf H_k=\partial_B\mathcal H(0)\) is the field part of \(S^{\circ-1}_{\rm flat}(0,\cdot)\), the flat constrained Landau lift. The periodisation clause is therefore purely flat and linear. Suppose the infinite-lattice flat block operator has a Bloch symbol holomorphic in \(|\operatorname{Im}p|<\delta_0\) in level-\(k\) units, which is Balaban CMP 95–96 for the flat case, cited and pending as part of P82. Poisson summation then makes the torus kernel equal to \(\sum_{n\in\ell_k\mathbb Z^4}\) of the \(\mathbb Z^4\) kernel. For lifts within half the torus, the terms \(n\ne0\) sum to at most \(Ce^{-c\delta_0\ell_k/2}\). The torus operator has no zero mode: the global constant gauge transformations are not in \(\ker Q'\). Nothing nonlinear enters.

## 10. Theorem 6(c) from Theorem 4

Theorem 6(c) (SA 9776–9786) compares \(U=U_{\mathbf B}(\mathbf V)\) on a \(\mu\)-collared region \(W\) with the localised background \(U^\circ_W\), the background of the joined sequence \(\mathbf B'\) with the joined datum \(\mathbf V^J\). The A3 gate (§7) rejected an earlier two-background argument on three counts: missing restriction compatibility, \(L^2\) bounds where pointwise bounds are needed, and a collar sum that assumed a polynomial count of multiscale balls. The weighted form of Sections 6–8 removes the last two. The first is proved below, in Lemma 10.2.

**Premises.** (R1) *Restriction compatibility:* \(U|_W\), modulo \(\mathcal G^{\rm res}(\mathbf B')\), is the background of \(\mathbf B'\) with datum \(\mathbf V^U:=M_{\mathbf B'}(U|_W)\). This is Theorem 6(b) for the joined sequence. (R2) *Collar datum:* after a node gauge equal to \(\mathbf 1\) at the old nodes, \(\mathbf V^U=e^{iB_0}\mathbf V^J\), with \(B_0\) supported on the collar bonds and \(\sup|B_0|\le C_L\varepsilon_1\le r_{\rm B}\). (R3) *Geometry, in the given metric \(d_{\mathbf B}\):* every collar bond has \(d_{\mathbf B}(y_c,W^c)\le c_1\mu\) (SA 9786: the collar is \(O(1)\) layers of cubes of side \(\mu\xi_{j_a}\) inside the single layer \(j_a\)). (R1) and (R2) are proved below, in Lemmas 10.2 and 10.3. They use only P81 and three properties of the joined sequence: (G1) \(\Omega'_0=W\) and \(\Omega'_q\subset\Omega_q\) for every \(q\); (G2) each \(\Omega'_q\) is a union of level-\(q\) blocks; (G3) \(\operatorname{dist}_\infty(W^c,\Omega'_1)>\rho\eta\). (G2) follows from the pillar partition of SA 9601: a block meeting a deeper member would sit in two pillars. (G3) follows from (G1) and separation (Theorem 6(a)). (G1) is how I read SA 9786: the collar lies in the single layer \(j_a\), and its new bonds have levels \(q<j_a\). So the tower is cut at depth \(j_a\) in the collar (cutting at a depth is the operation of SA 9646 and 9769). On that reading (G1) holds, since the collar lies in \(\Omega_{j_a}\subset\Omega_q\) for \(q\le j_a\). I have **not** checked the erosion rules (SA 9646) line by line against this reading, so (G1) stays a named premise. By (G1) every point has a finer or equal unit in \(\mathbf B'\) than in \(\mathbf B\), so \(d_{\mathbf B}\le d_{\mathbf B'}\). Hence \(e^{\theta d_{\mathbf B}(\cdot,W^c)}\) lies in \(\mathcal W_\theta\) for the joined metric: \(d_{\mathbf B}(y,W^c)\le d_{\mathbf B'}(y,z)+d_{\mathbf B}(z,W^c)\). This matters because the tower makes the collar's \(d_{\mathbf B'}\)-width grow with the number of levels, while its \(d_{\mathbf B}\)-width is \(O(\mu)\).

**Lemma 10.1.** Assume P81 and P82 for the joined sequence, which is separated by Theorem 6(a), and (G1)–(G3). Then (R1)–(R3) hold (Lemmas 10.2, 10.3), and \(U|_W=(e^{i\eta f}U^\circ_W)^w\), with \(w=v[f]^{-1}\) at the tops away from the collars (elsewhere \(w\) is unrestricted, as in the outline) and, over every top \(y\) of the joined sequence,
\[
 \xi_y|f|,\ \xi_y^2|\nabla f|,\ \xi_y^3|D^{\mathsf T}Df|\ \le\ C\,e^{\theta(c_1\mu+D_L)}\,\varepsilon_1\,e^{-\theta d_{\mathbf B}(y,W^c)},\qquad \theta=\delta_0/8 .
\tag{41}
\]
This is Theorem 6(c), with \(\delta_W=\theta\) and \(C_\mu=Ce^{\theta(c_1\mu+D_L)}\sim e^{O(\mu)\delta_0}\), as the outline states.

*Proof.* Take \(U_*=U^\circ_W\) as the reference of Sections 6–7 for \((\mathbf B',\mathbf V^J)\): it is real, regular and critical by P81. By (R1), (R2) and Proposition 6.4, \(U|_W\) is \((e^{i\eta\mathcal H(B_0)}U_*)^{u_{B_0}}\) up to \(\mathcal G^{\rm res}(\mathbf B')\) and the node gauge of (R2); both are absorbed into \(w\), and both are \(\mathbf 1\) at the old nodes. Put \(f=\mathcal H(B_0)=\int_0^1D\mathcal H(tB_0)[B_0]\,dt\). The response (33) is linear in its forcing, so \(D\mathcal H(tB_0)[B_0]\) is the field part of \((1+S_0^{-1}DN)^{-1}S_0^{-1}(0,D\mathsf b(tB_0)B_0)\). Use the weight \(w(y)=e^{\theta d_{\mathbf B}(y,W^c)}\) with the given metric, which lies in \(\mathcal W_\theta\) for the joined metric (above), so (4) for \(\mathbf B'\) applies (Lemma 8.2). By (R2), (R3) and the locality of \(D\mathsf b\),
\(\|D\mathsf b(tB_0)B_0\|_{Y,w}\le C_be^{\theta(c_1\mu+D_L)}C_L\varepsilon_1\). Then (4) and the Neumann bound give the first two members of (41). The third follows from 7.1 applied to the same linear response at each \(t\). \(\square\)

No sum over collar bonds is taken, so no count of metric balls enters: the summation is inside the weighted operator bound of Lemma 8.2. The bounds are pointwise, so the gate's \(L^2\)-to-pointwise gap does not arise.

**Lemma 10.2 (restriction compatibility, (R1)).** Assume P81 for \(\mathbf B'\) and (G1)–(G3). Then \(U|_W\) is critical and regular for \((\mathbf B',\mathbf V^U)\), and so, by A1's uniqueness, it lies in the orbit of \(U_{\mathbf B'}(\mathbf V^U)\) modulo \(\mathcal G^{\rm res}(\mathbf B')\).

*Proof.* This is the gate's "smaller tangent space" direction, written out following mechanism 9 (SA 9913). Let \(U'(t)\in C(\mathbf B',\mathbf V^U)\) be a curve with \(U'(0)=U|_W\), and let \(\tilde U'(t)\) equal \(U'(t)\) on \(W\) and \(U\) elsewhere.
(i) By (G3), every bare bond of \(W\) within \(\rho\eta\) of \(W^c\) has no end point in \(\Omega'_1\). It is therefore a level-\(0\) row of \(\mathbf B'\), whose average is the bond itself, so \(U'(t)=U\) there.
(ii) *Induction on the level.* Every level-\(m\) bond \(b\) with no end point in \(\Omega'_{m+1}\) has \(\mathcal M^m\tilde U'(t)(b)=\mathcal M^mU(b)\). For \(m=0\) this is (i), together with \(\tilde U'=U\) off \(W\). For \(m\ge1\): if \(b\) has an end point in \(\Omega'_m\), it is a row of \(\Gamma'_m\), which is constrained. Otherwise \(B^m(b_\pm)\cap\Omega'_m=\emptyset\) by (G2), so every level-\((m-1)\) bond of its double block has no end point in \(\Omega'_m\), and the induction hypothesis applies.
(iii) A row \(c\in\Gamma_j\) of the given family has no end point in \(\Omega_{j+1}\supset\Omega'_{j+1}\) (G1). So by (ii) \(M_{\mathbf B}\tilde U'(t)=\mathbf V\), and \(\tilde U'(t)\) is a curve in \(C(\mathbf B,\mathbf V)\).
(iv) A plaquette of \(\Omega_0\) not contained in \(W\) meets \(W\) only in bonds of the layer in (i), so it sees no variation. Hence \(A_{\Omega_0}(\tilde U'(t))-A_{\Omega_0}(U)=A_W(U'(t))-A_W(U|_W)\).
Criticality of \(U\) now gives criticality of \(U|_W\). \(U|_W\) is regular at the radius of \(U\). Its datum is \(C_L\varepsilon_1\)-regular, because its test loops are plaquettes of \(\mathcal M^qU\), bounded by (7). A1's uniqueness for \(\mathbf B'\) (P81) then applies. \(\square\)

**Lemma 10.3 (one-step reconstruction; SA Lemma 1a.1.9, proved here).** Let \(W\) be a level-\(m\) field on the double block of a level-\((m+1)\) bond \(c\), with all plaquettes within \(\varpi\le c_L\) of \(\mathbf 1\), in block axial gauge: \(W(y,x)=\mathbf 1\) for \(x\in B(y)\), \(y=c_\pm\). Then \(|W(b)-\mathbf 1|\le C_L\varpi\) for every bond inside \(B(c_\pm)\), and \(|W(b')-\mathcal M(W)(c)|\le C_L\varpi\) for every corridor bond \(b'\), that is, every bond from \(B(c_-)\) into \(B(c_+)\).

*Proof.* Two paths in one block, or in the double block, with common end points and length at most \(8L\), bound a lattice surface of at most \(C L^2\) plaquettes. This is the strip filling of SA PX43. The unitary product inequality then puts their transports within \(CL^2\varpi\) of each other. Federbush's mean of points within \(\delta\) of each other lies within \(C\delta\) of each of them. So \(|W(\Gamma_{y,x})-\mathbf 1|\le C_L\varpi\) for the comb \(\Gamma_{y,x}\), and the loop "comb to \(b_-\), then \(b\), then back along the comb from \(b_+\)" gives the first claim. For \(b'\), any two corridor bonds are joined, through combs, by a loop of length \(O(L)\), so their values agree within \(C_L\varpi\). Each segment \([x,x']\) in the definition of \(\mathcal M\) (SA 7072–7080) consists of bonds inside the blocks and one corridor bond, so each closed transport \(W_x\) is within \(C_L\varpi\) of \(\mathbf 1\). The same holds for \(W[c]\) compared with a corridor bond, and the second claim follows. \(\square\)

**Corollary 10.4 ((R2)).** Assume P81 and that the collar lies in the single layer \(j=j_a\). There is a gauge transformation \(G\) equal to \(\mathbf 1\) at the level-\(j\) sites (the old nodes there) such that, for every collar bond \(b\) of level \(q<j\), \(|\mathcal M^q(U^G)(b)\,\mathrm{lift}(\mathbf V_j)(b)^{-1}-\mathbf 1|\le C_L\varepsilon_1\).

*Proof.* Choose \(G=G_{j-1}\cdots G_0\) step by step from the top. \(G_m\) puts \(\mathcal M^m\) of the current field into block axial gauge relative to the level-\((m+1)\) centres. It is \(\mathbf 1\) on \(\mathbb T^{(m+1)}\) and extended arbitrarily to the fine sites. By covariance (SA 7065–7080) it leaves every coarser average unchanged. Lemma 10.3 at level \(m\) gives \(|W_m-\mathrm{lift}_1(W_{m+1})|\le C_L\varpi_m\) bond by bond. Every level-\(m\) bond lies either inside a level-\((m+1)\) block or in exactly one corridor, since blocks are cubes. \(\mathrm{lift}_1\) copies bond values, so errors pass from one level to the next with coefficient one. With \(E_j=0\), this gives \(E_q\le C_L\sum_{q\le m<j}\varpi_m\). By (7), or SA PX44, \(\varpi_m\le C_L\varepsilon_1L^{2(m-j)}\) inside one layer, and the sum is at most \(C_L\varepsilon_1\). The iterated \(\mathrm{lift}_1\) is the outline's lift: \(\mathbf 1\) inside level-\(j\) blocks and \(\mathbf V_j(c)\) on bonds from \(B(c_-)\) into \(B(c_+)\). \(\square\)

So (R1)–(R3) hold under P81 and (G1)–(G3), and Lemma 10.1 rests only on P81, P82 and the geometric premise (G1). Without the one-layer hypothesis, the sum in Corollary 10.4 picks up a seam term. That is why the outline requires the collar to lie in one layer (SA 9913).

## 11. Review of Codex's Sections 1–6 (kept above, verbatim)

I re-derived (27) (the exact block inverse), (29), (31) and (33)–(34), and checked (5), (7)–(9) against the definitions (SA 7065–7108, 11550–11575). They are correct conditional on P81 and P82. Ranked by what each item breaks:

1. **Gap, now closed.** Section 6 stopped before showing that the fixed point satisfies the Landau condition and is Theorem 3's \(\mathcal H\). Without that step, (34) bounds the response of the augmented system, not of the background. Closed by Proposition 6.4.
2. **Imprecise premise.** Section 3 states (4) "uniformly in the weight centre". Centred weights give the decay in (34), but not Section 10's set-distance weight or the row sums. The intended premise is (4) for every \(w\in\mathcal W_\theta\), which is equivalent to BGR11 row sums (Lemma 8.2).
3. **Over-strong premise.** P82 asks for the \(W_0\)- and \(\Delta'\)-corrected inverse and for an identification of CMP 99b's current corrections with \(W_0\). Not needed (Lemma 8.1). Similarly, P81 is used only through \(\Phi\) and its criticality at real data, not through Balaban's Landau representation in Proposition 9.
4. **Section 5 is off the critical path and partly unproved.** Its identity (14), \(E\bar H=K_0^{\mathsf T}M\), needs \(RD^{\mathsf T}\bar GK_0^{\mathsf T}=0\) (the physical gauge identity of PX96), which Section 5 does not prove. Its claim that (24) is (189) is not used anywhere. Sections 6–10 do not depend on Section 5.
5. **Open matching item (M1), correctly flagged in Section 1.** The multiplier is in the counting row pairing. The outline's value bound for \(\dot\omega\) must be read in that normalization or converted by its cell weights.
6. **Radius.** (31)–(34) hold on the contraction polydisc. Theorem 3's \(r_{\rm B}\) has to be taken no larger. This is allowed, since the outline only bounds \(r_{\rm B}\) from above.

The local estimates of Section 4 (one-step functions, the depth-uniform row bound, Cauchy densities, and the Wilson remainder with its cubic cancellation) were spot-checked against SA PX141–PX154 and PX114, not re-derived line by line. A gate should re-derive (11) and (12), which carry every weighted Lipschitz bound.

## 12. Verdict, open items, and what changes

**Moves:** the shared blocker, nonlinear A3 part 2 (`route-decisions.md` 1 and 4.2 item 1; `sa-ledger.md` #3).

| Statement | Verdict (one same-provider continuation, not gated) | Rests on |
|---|---|---|
| Theorem 4, first paragraph: potential, gradient, \(D^{\mathsf T}D\), \(\Delta_{U_0}\), current, Hölder, \(\dot\omega\), \(\dot u\), on the whole polydisc, uniform in depth; Balaban CMP 102 (190) | **proved, conditional** (implication, every step written) | P81, P82° (Lemma 8.1), M1 |
| Theorem 3, second paragraph: Landau pair \((\mathcal H,u)\), multiplier \(\omega\), uniqueness, reality, bounds | **proved, conditional** (Proposition 6.4, 7.6) | P81 (only \(\Phi\)), P82° |
| Theorem 4, second paragraph (non-critical regular references) | proved for a reference with its own current (9.1); for an independent current the outline does not yet specify the system | P82° on complex backgrounds; M2 |
| Theorem 4, third paragraph (\(\mathbf V_0=\mathbf 1\), periodisation) | reduces to the flat linear symbol; no nonlinear content (9.2) | flat part of P82 (CMP 95–96) |
| Theorem 6(c), localised comparison | **proved, conditional** (Lemmas 10.1–10.4: restriction compatibility, collar datum, decay); no count of multiscale balls and no \(L^2\) step | P81, P82°, geometric premise (G1) |
| `sa-2.8.md` (L), one-plaquette inequality | implication from Lemma 10.1 by the scalar step of `sa-2.8.md` §9 and gate §7, when its two backgrounds are an instance of 6(c); that instance is not checked here | as 6(c) |
| Balaban CMP 102 (189), second-variation decay | not needed on this route | (none) |

**Open, hardest first.** (1) **P82°, row 82:** the weighted inverse of \(S^\circ\) at a real, curved, regular critical reference, with the outline's \(R\) and \(K_0\), the Hölder member, \(D(1-R)D^{\mathsf T}:X_w\to F_w\), and BGR11 row sums at rate \(\theta\), uniformly in depth. It is the only quantitative input, and it is where this route fails if it fails. §8's remark shows how CMP 99b's comb-slice bounds would serve, given \(O(\kappa)\) comparisons of \(R\) with \(R^{\mathsf c}\) and of \(K_0\) with Balaban's rows, which are not proved. (2) **P81, row 81:** \(\Phi\) holomorphic, critical at real data, regular, uniform in depth. (3) **(G1)**, a check of the outline's tower rules for Theorem 6(c). (4) **M1**, the multiplier normalization. The outline pairs \(\omega\) with \(\mathcal Q^{\rm st}\) through "datum cell weights" \(\mu_c\) (SA 11761–11770) and never fixes them in Theorems 3–4. The bound holds for the counting multiplier and converts by \(\mu_c^{-1}\), so this is a convention for the outline to fix, not a proof gap. **M2**, the independent-current operator, is a specification item (9.1).

**What changes.** Row 82's target is smaller: no current corrections, no \(W_0\) identification, and its "weighted" clause is exactly the BGR11 row sums. Rows 83 (`floor-screen`) and `sa-2.8` (L) can cite Lemma 10.1 under P81, P82° and (G1). The A3 gate's §7 objections (polynomial ball count, \(L^2\) versus pointwise) do not apply to this route. Nonlinear A3 part 2 now carries no open nonlinear estimate of its own: it is closed modulo the linear input P82° and the A1 input P81. If P82° fails at curved backgrounds, both routes still stop at A3, now at its linear core.

**Method notes.** No numeric job was run and none was needed: the only quantitative input is linear and belongs to row 82. No step is computer-assisted. Credits: T. Balaban (CMP 95, 96, 98, 99, 102: the averaging, propagators, background construction, and the statement (190) proved here); Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at `31a47c543775` (the straightened recursion, the nonlinear-constraint contraction of mechanism 7, the identity-theorem device of (k), PX114, BGR1–BGR27, and the statements of Theorems 3, 4 and 6); OpenAI Codex for Sections 1–6 of this file.

**Result.** Conditional on P81 and P82°, the following are proved: Theorem 4 with all its members, which is Balaban's (190); Theorem 3's Landau pair; and Theorem 6(c), which also needs the geometric premise (G1). Still open: P82° (row 82, the first point of failure), P81 (row 81), (G1), M1 and M2.
