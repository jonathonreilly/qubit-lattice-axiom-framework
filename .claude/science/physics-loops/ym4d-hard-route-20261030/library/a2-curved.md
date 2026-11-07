# A2 at curved backgrounds for the outline's plain block average
Provenance: OpenAI Codex (GPT-6 family; exact serving variant not exposed), effort max requested (runtime setting not exposed); repository commit d7043777dc88f8cb2136c576ced456af34d979f6; Sussman–Alpoge outline commit 31a47c543775; research text, not an audit and grants no status.

## 1. Target and source identity

**Disposition for the full A2 request: STOPPED.** The proved subcases and the remaining attack are recorded in §13.

The target is Obligation A2, lines 3835–3862 of
[the pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex): a lower bound for the actual gauge-fixed constrained Hessian, in fluctuation-scale units, uniform in previous depth, compatible volume and the admitted conditioning sets, and half that bound throughout the claimed complex domains. The plain block derivative, internal-contour gauge and background constraints must be those of that outline. The flat statements CF18 and WI15 concern the unweighted classical value and do not identify its curved Hessian.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the outline, its definitions, A2, and the flat comparison strategy. Tadeusz Balaban supplies the background-field/block-renormalization programme underlying this question. The local curved comparison and localization route is taken from this checkout's `c0-loc.md`, `lc-u.md`, `fan-ext.md` and `fd-local.md`, with their specified gates. Source labels are not proofs. No numerical or machine-assisted calculation will discharge a statement here.

## 2. Conditioning cannot reduce an already established gap

**Proved.** The conditional inverse in the outline, lines 10196–10208, is
\(C^{(k)}(Y)=(\chi_Y\mathsf A\chi_Y)^{-1}\) on the free nonpivot coordinates in \(Y\). It retains the parent precision, including its crossing interactions. Let \(I_Y\) be zero extension of those coordinates. If
\(\operatorname{Re}\langle u,\mathsf A u\rangle\ge c\|u\|^2\), then
\[
 \operatorname{Re}\langle v,I_Y^*\mathsf A I_Yv\rangle
 =\operatorname{Re}\langle I_Yv,\mathsf A I_Yv\rangle
 \ge c\|I_Yv\|^2=c\|v\|^2.                     \tag{2.1}
\]
This works for every subset, every boundary shape, and complex matrices as well as real ones. The same proof gives the bound \(c/2\) after a complex continuation has been bounded on the parent space. It does not discard boundary plaquettes or re-solve the background on \(Y\). Changing the underlying layered background problem is a separate quantifier in A2.

Thus the attempted counterexample by cutting a thin neck or deleting part of a block cannot lower the gap of a *fixed* parent precision. A Neumann restriction obtained by dropping crossing terms would be a different operator. The pivot map must be applied after zero extension: \(B=\mathsf C_V I_Yv\); imposing support on \(B\) instead of on its free coordinates is another different restriction.

## 3. The operators that must be compared

The outline's defining formulas distinguish three forms (lines 10138–10208):
\[
 K_1=\Delta_U^{\rm W}+DRD^{\mathsf T}+Q^{\mathsf T}aQ
       -\Delta'_\pi[J]
       -\mathsf S^{\mathsf T}\Delta^{(2)}[\mathsf H^{\mathsf T}J]\mathsf S,
\]
\[
 \Delta_k=(QK_1^{-1}Q^{\mathsf T})^{-1}-a
                 -\mathsf E^{(2)}[\mathsf H_1^{\mathsf T}J],
 \qquad
 \mathsf A=\mathsf C_V^{\mathsf T}
                  (\mathsf G_V^{(2)}+\Delta_k)\mathsf C_V.       \tag{3.1}
\]
Here \(Q\) in the first two expressions is the straightened, per-length, layered row map; the pivot map \(\mathsf C_V\) solves the *plain one-step* derivative at \(V=\mathcal M^kU\). The projection \(R\) is onto \(\Delta_U\ker Q'\), whereas the local curved notes use the orthogonal projection onto \(\ker r_N\). Neither replacing one projection by the other nor omitting either current correction preserves (3.1).

The real/complex regular-pair class is explicit at outline lines 10128–10138: local curvature is bounded by \(\alpha_0\eta^2\xi_j^{-2}\), local potentials and their first differences have the stated small scale-weighted bounds, and \(J\) is an independent variable bounded by \(\gamma_0\xi_j^{-3}\). On shell it is the actual current. The geometries are separated unions of aligned cubes; outer Dirichlet compression and the inner-plaquette Hessian are distinguished in the outline. These distinctions are retained in the attack below.

## 4. An exact transfer between the two real gauge projections

**Proved implication.** This addresses the projection mismatch without asserting the missing Hessian identification. All spaces below are finite real Hilbert spaces with their physical density pairings. Let \(D\) map sites to bonds, let \(r\) be a site readout, and let \(C\) be a bond constraint. Put \(Z=\ker r\), let \(P\) be the orthogonal projection onto \(Z\), and let \(R\) be the orthogonal projection onto \(D^*D Z\). Suppose
\[
 CDZ=0,\quad \|z\|\le p\|Dz\|\ (z\in Z),\quad
 \beta(Dz,v)=0\ (z\in Z, v\in\ker C),                 \tag{4.1}
\]
where \(\beta\) is symmetric, and suppose the actual graph estimate is
\[
 \|v\|^2+\|D^*v\|^2
       \le K\{\beta(v,v)+\|PD^*v\|^2\},\qquad Cv=0.    \tag{4.2}
\]
Then
\[
 \|v\|^2\le K(1+2p^2)\beta(v,v)+2p^2\|RD^*v\|^2,
                    \qquad Cv=0.                       \tag{4.3}
\]
In particular the Landau gauge has a gap with no extra dimension or depth factor whenever \(p,K\) are uniform.

To prove this, minimize \(\|v-Dz\|^2\) over \(z\in Z\). The second inequality in (4.1) makes \(D|_Z\) injective, so the quadratic has a unique minimizer. Write \(v=v_0+Dz\). Its normal equation is \(PD^*v_0=0\), and \(Cv_0=0\). Orthogonality and the null identity give
\[
 \|v\|^2=\|v_0\|^2+\|Dz\|^2,\qquad
 \beta(v,v)=\beta(v_0,v_0)\ge0.
\]
Equation (4.2) bounds both \(\|v_0\|\) and \(\|D^*v_0\|\) by \(\sqrt{K\beta(v,v)}\). Also
\[
 \|Dz\|^2=\langle z,D^*Dz\rangle
       \le p\|Dz\|\|D^*Dz\|,
\]
so \(\|Dz\|\le p\|D^*Dz\|\), including the zero case. Since \(D^*Dz\in\operatorname{ran}R\),
\[
 D^*Dz=RD^*v-RD^*v_0.
\]
Its norm is at most \(\|RD^*v\|+\sqrt{K\beta(v,v)}\). Square, use \((a+b)^2\le2a^2+2b^2\), and add the bound for \(v_0\). This proves (4.3).

This proves a change of gauge estimate, not an identification of gauges. The null identity is for the stationary **Lagrangian** Hessian. For Wilson's Hessian alone it is false at nonzero current: differentiating gauge invariance gives
\(D^2A(U)[D_Uz,v]=-DA(U)[(d_vD_U)z]\), with the appropriate chart derivative. The current term cannot be deleted on the strength of gauge invariance. The summed Ward identity in `c0-loc.md` §9 supplies (4.1) only after its actual smooth constraint chains and stationarity equation have been matched.

## 5. The curved one-step statement, including its complex half-gap

**Proved: the following node-free, zero-previous-depth subcase.** Fix odd \(L\ge3\). Work in unit fine-lattice spacing on a compatible torus. Use exactly the outline's plain one-step average, its middle crossing pivots, and its soft internal-contour gauge with positive coefficient one. Let \(V\) be real, in block axial gauge
\(V(y,x)=1\), and suppose every plaquette has \(\|V_p-1\|\le\epsilon_L\). There exist positive \(\epsilon_L,r_L,c_L\), independent of the torus, such that the Hessian of Wilson action plus this gauge functional in the actual pivot chart of the fibre through \(V\) is at least \(c_LI\). At a constrained critical \(V\), this is the physical \(k=0\) fluctuation Hessian. Its holomorphic pivot-chart continuation is at least \(c_L/2\) in real Hermitian part when \(W=e^{iE}V\), \(\|E\|_\infty<r_L\). Both bounds hold after every free-coordinate conditioning of §2. The proof also permits an independent-current perturbation of size \(r_L\) in the constraint-curvature term, after decreasing \(r_L\).

Here is the complete local argument. Put
\[
 q_V(a)_c={1\over i}\log\{\mathcal M(e^{ia}V)_c
                                  \mathcal M(V)_c^{-1}\},\quad
 K_V=Dq_V(0),\quad
 G_VB={1\over i}{d\over dt}(e^{itB}V)(y,x)\big|_{t=0}.
                                                               \tag{5.1}
\]
The last formula is used at the axial real center, where its contour value is one. Let \(d_V\) be the transported four-leg plaquette derivative, normalized so that the Wilson Hessian at a flat field is \(\|d_VB\|^2\). All norms here are counting norms and all pairings on colors use \(\tfrac12\operatorname{tr}(XY)\).

First prove a local flat estimate. Take a rectangle of \(3^4\) whole \(L\)-blocks. Its bond space contains all bonds with both endpoints in that rectangle. Let \(T_L\) collect (i) all internal plaquette curls, (ii) every internal averaged-contour sum in its blocks, and (iii) every plain row joining neighboring blocks of the rectangle. This finite linear map is injective. Indeed, zero curl within a block makes every coordinate-order path between two sites have the same sum: exchange neighboring perpendicular steps, each exchange contributing precisely the curl of its intervening plaquette. A comb followed by one internal bond and the reverse of the next comb can be reduced by these same exchanges. Thus zero averaged-contour sums force every internal bond to vanish. A plaquette crossing a block face then equates neighboring crossing-bond values, because its other two bonds are internal. The transverse face grid is connected, so all crossing values on a face equal some \(b_c\). Every length-\(L\) segment for the corresponding plain row contains exactly one such crossing and otherwise internal bonds. Its internal endpoint-contour terms vanish. Hence that row equals \(b_c\), and zero rows kill all crossing bonds. This proves injectivity, including all three color components.

Define \(m_L=\min_{\|b\|=1}\|T_Lb\|^2\). The unit sphere of this fixed finite-dimensional real space is compact: any minimizing sequence has a convergent subsequence, and injectivity excludes a zero minimum. Thus \(m_L>0\), by a written existence argument, not an enumeration. The same inequality holds on complex vectors by separating real and imaginary parts. Applying it to the rectangle around each block and retaining the bonds starting in the central block gives
\[
 \|B\|^2\le A_L\{\|d_0B\|^2+\|G_0B\|^2+\|K_0B\|^2\}.       \tag{5.2}
\]
Here \(A_L=\nu_L/m_L\), where \(\nu_L\) is the maximum number of these \(3^4\)-block rectangles containing any one listed plaquette, contour or row. It is finite and depends only on this fixed stencil. Periodic unfolding proves (5.2) on a smaller compatible torus too: repeat the torus until these rectangles embed, apply the estimate, and divide all squared norms by the number of copies. No holonomy has been set to one on the whole torus. This is the local kernel argument behind Sussman–Alpoge's CF18, rewritten for a direct curved perturbation.

For that perturbation, a coordinate comb gauge on one rectangle makes each real link \(1+O_L(\epsilon_L)\). To check this assertion, compare the comb to the start of a bond followed by that bond with the comb to its end. Moving the extra step through at most \(12L\) other steps replaces their ratio by a product of at most \(12L\) conjugated plaquettes. Unitarity and telescoping bound its deviation from one by \(12L\epsilon_L\). The same construction works on a fixed enlargement containing all row carriers.

It can be replaced here by a gauge *constant on each block*. Let \(s\) be the comb gauge. Covariance and axiality give the transformed internal mean \(s(y)s(x)^{-1}\). Since all transformed internal links are \(1+O_L(\epsilon_L)\), their path products and their mean are also \(1+O_L(\epsilon_L)\). Therefore \(s(y)s(x)^{-1}=1+O_L(\epsilon_L)\). Replacing \(s(x)\) by \(s(y)\) throughout that block still makes every link in the rectangle \(1+O_L(\epsilon_L)\). This replacement preserves axiality and transforms \(G_V,K_V,d_V\) by orthogonal color maps. It needs no global gauge and no bound on global holonomies.

All finite maps used in that frame have uniform analytic derivative bounds on a sufficiently small fixed link ball. Here is their existence proof. The exponential and \(\log(1+X)=\sum_{n\ge1}(-1)^{n+1}X^n/n\) converge with their derivatives uniformly on a smaller ball. For the contour mean, write its inputs as \(e^{X_i}\), its output as \(e^Z\), and
\(\log(e^{X_i}e^{-Z})=X_i-Z+R_i(X_i,Z)\). The series give \(\|D_ZR_i\|\le C(\|X_i\|+\|Z\|)\). Thus
\(Z=\overline X+\overline{R_i(X_i,Z)}\) is a contraction of constant at most \(1/2\) on a fixed small ball. Its iterates converge uniformly there, giving the actual analytic mean and bounded derivatives on every smaller ball. The remaining products, logarithms and exponentials form a finite composition with fixed \(L\). Consequently the coefficients of \(d_V,G_V,K_V\), in this block-constant frame, differ from their flat coefficients by at most \(D_L\epsilon_L\). One may define \(D_L\) as the maximum derivative norm on the closed smaller ball, multiplied by its finite coordinate counts and the preceding comb bound. This is finite before volume or background is chosen.

Use \(\|a+b\|^2\le2\|a\|^2+2\|b\|^2\) in each local estimate, then sum its bounded overlaps. It gives
\[
 \|B\|^2\le2A_L\{\|d_VB\|^2+\|G_VB\|^2+\|K_VB\|^2\}
                          +D'_L\epsilon_L^2\|B\|^2.
\]
Choose \(D'_L\epsilon_L^2\le1/2\) and put \(A'_L=4A_L\). On the actual tangent fibre this proves
\[
 \|B\|^2\le A'_L\{\|d_VB\|^2+\|G_VB\|^2\},\qquad K_VB=0.    \tag{5.3}
\]

It remains to include the curved fibre, rather than replace its Hessian by curl squared. The derivative at a middle pivot at the identity is \(L^{-3}I_3\): exactly \(L\) of the \(L^4\) straight segments contain that pivot, and no internal contour does. No other pivot occurs in the row. At a real flat field it is \(L^{-3}\) times an orthogonal transport. The same local comparison therefore makes each pivot derivative invertible, with inverse norm at most \(2L^3\), once \(\epsilon_L\) is smaller. Let \(h_V\) be that pivot-supported right inverse, \(\iota\) zero insertion of free coordinates, and
\[
 C_V=\iota-h_VK_V\iota,\quad K_VC_V=0,\quad (C_Vu)_{\rm free}=u.
\]
These are the outline's actual pivot choices, not a minimum-norm replacement.

Set \(R_V(a)=q_V(a)-K_Va\). To construct the chart, solve
\(d=R_V(t-h_Vd)\) on a small ball. Its derivative in \(d\) has norm at most \(M_L\|t-h_Vd\|\|h_V\|\), by the bounded second derivative just proved. A sufficiently small ball makes it at most \(1/2\), and \(R_V(a)=O_L(\|a\|^2)\) makes that ball invariant. Iteration proves a holomorphic solution and a graph \(\Psi_V(t)=t-h_Vd(t)\). Differentiating the identity twice at zero gives
\[
 D\Psi_V(0)=I,\qquad
 D^2\Psi_V(0)[B,B]=-h_VD^2q_V(0)[B,B].                    \tag{5.4}
\]
Each component uses only its own double block, so this is a local graph, uniformly in volume.

Let \(F=A_{\rm Wilson}+\mathrm{GF}\). Since \(D\mathrm{GF}(V)=0\) at an axial field, the exact chart Hessian on \(B=C_Vu\) is
\[
 F''_V[B,B]-\langle J(V),h_VD^2q_V(0)[B,B]\rangle.         \tag{5.5}
\]
The Wilson plaquette product differentiated twice has sixteen ordered pairs of insertions. At plaquette holonomy one their traces sum to \(|d_VB(p)|^2\). In each remaining term insert \(V_p-1\); its norm is at most \(\epsilon_L\), and the unitary prefixes preserve each insertion norm. Summing the at-most-six plaquette incidences of a bond gives
\[
 |A''_V[B,B]-\|d_VB\|^2|\le D''_L\epsilon_L\|B\|^2.
\]
The gauge Hessian is exactly \(\|G_VB\|^2\): the first derivative of \(1-\tfrac12\operatorname{tr}e^{iX}\) at zero vanishes and its second derivative is the color norm squared. Finally \(\|J(V)\|_\infty\le C\epsilon_L\). This follows by differentiating each incident plaquette once, subtracting its identity contribution (the inserted generator is traceless), and bounding the remaining trace by \(C\|V_p-1\|\). The local second derivative of \(q_V\), the bound for \(h_V\), and the fixed overlap of double blocks therefore bound the last term of (5.5) by \(D'''_L\epsilon_L\|B\|^2\). Equations (5.3)–(5.5) give
\[
 (5.5)\ge\{(A'_L)^{-1}-D''''_L\epsilon_L\}\|B\|^2
             \ge {1\over2A'_L}\|B\|^2
             \ge c_L\|u\|^2,
 \qquad c_L={1\over2A'_L},                               \tag{5.6}
\]
after one further fixed decrease of \(\epsilon_L\). All choices precede the torus size. The expression is the constrained Hessian even without stationarity as a chart Hessian; stationarity makes its intrinsic fibre interpretation independent of second-order chart changes.

For completeness, the complex step is an operator estimate. Continue the same finite formulas, including the inverse pivot blocks and the full gauge functional, holomorphically. Their derivative coefficients on a smaller ball have a maximum \(M'_L\), uniformly over the real local reference class above. Each matrix coefficient of the chart Hessian reads a fixed stencil; each coordinate occurs in at most a fixed number of those stencils. Hence the difference matrix has both absolute row and column sums at most \(M''_L\rho\) when \(\|E\|_\infty\le\rho\). For a matrix \(T\), Cauchy in each row gives
\[
 \sum_i|(Tv)_i|^2
 \le\Big(\sup_i\sum_j|T_{ij}|\Big)
       \Big(\sup_j\sum_i|T_{ij}|\Big)\sum_j|v_j|^2.
\]
Therefore \(\|\mathcal E_W-\mathcal E_V\|_{2\to2}\le M''_L\rho\), without a dimension factor. This proof uses absolute coefficients of the analytic bilinear matrix; it does not replace its transpose by a Hermitian adjoint. For \(\rho\le r_L:=c_L/(2M''_L)\), reduced further to stay in the analytic chart,
\[
 \operatorname{Re}\langle u,\mathcal E_Wu\rangle_H
 \ge\langle u,\mathcal E_Vu\rangle_H-M''_L\rho\|u\|^2
 \ge(c_L/2)\|u\|^2.                                    \tag{5.7}
\]
An independent-current change in (5.5) has the same finite-stencil bound, linear in its supremum norm, so it can be included in \(\rho\) by increasing \(M''_L\). Conditioning follows from (2.1). This proves the advertised smaller statement; it has no previous blocking depth to be uniform over.

## 6. An explicit regular curved family at every depth

Take a four-torus of side \(T\), with \(T\) an arbitrarily large compatible multiple of all fixed geometric scales. Let \(\eta=L^{-k}\), \(N=T/\eta\), \(Z=\operatorname{diag}(1,-1)\), and
\[
 f=2\pi/T^2,\qquad \theta=f\eta^2=2\pi/N^2.
\]
For periodic integer coordinates \(n_\mu\in\{0,\ldots,N-1\}\), define
\[
 U_2(n)=e^{i\theta n_1Z},\qquad
 U_1(n)=\begin{cases}1&n_1\ne N-1,\\
                         e^{-i\theta N n_2Z}&n_1=N-1,
          \end{cases}
 \qquad U_3=U_4=1.                                      \tag{6.1}
\]
Every \(12\)-plaquette is \(e^{i\theta Z}\), and every other plaquette is one. Away from the first-coordinate seam the exponent is \(\theta(n_1+1)-\theta n_1=\theta\). On that seam it is
\(-\theta Nn_2+\theta N(n_2+1)-\theta(N-1)=\theta\); at the simultaneous second-coordinate wrap it is \(-\theta(N^2-1)\), with the same exponential because \(\theta N^2=2\pi\). This checks the seam explicitly.

The Wilson current vanishes exactly. The two incident \(12\)-plaquettes at a bond give equal and opposite first variations, while the others give zero; traces against either off-diagonal color generator vanish separately. On a lifted cube of side \(D\), the same field has the local gauge potential \(A_2=f(x_1-x_{1,0})Z\), with the other components zero. This local representation can be obtained by integrating the difference of the two abelian link potentials: its plaquette sums are zero, so path independence on the rectangular lift constructs the gauge. Hence \(|A|\le fD\), \(|\nabla A|\le f\). Choosing \(T\) so large that \(C M_1L^2 f<\alpha_0\) supplies the outline's real local-gauge clause on every required \(O(M_1\xi_j)\) cube, including the next fluctuation scale \(\xi_{k+1}=L\), as well as \(|U_p-1|\le f\eta^2\) and \(J=0\). The constant sequence of whole-torus regions is admitted. Increasing \(T\) also supplies nonwrapping room; it changes no coercivity constant sought in A2.

All the actual means in this abelian field reduce, on their admitted branches, to averages of phases. A blocked plaquette has flux \(f\xi_j^2\): the contour contributions cancel at the vertices and each displaced square encloses the same constant flux. Thus the means remain on the regular branch for every \(k\) when \(f\) is fixed sufficiently small. Block and tower axial gauges are available within the same Cartan subgroup: transform each nonroot site by its contour phase, proceeding from the highest block level down. The root value is fixed at each stage. Curvature and the vanishing current are unchanged. The family is therefore genuinely curved and regular, rather than a proposed curvature array without links.

**Proved: the neutral sector of this attack does not lose a gap with depth.** Restrict variations to multiples of \(Z\). On this sector all adjoint transports are the identity and all mean logarithms are linear in the variations. Consequently the actual plain derivative, its iterates, and the contour gauge derivative are precisely their flat scalar versions; every constraint second derivative is zero. The bare Hessian is
\[
 E^{f}_{\rm bare}(w)=\cos\theta\sum_{p\parallel12}|dw(p)|^2
                       +\sum_{p\not\parallel12}|dw(p)|^2.
                                                               \tag{6.2}
\]
This follows by differentiating \(1-\cos(\theta+t\,dw)\) twice; on the other plaquettes \(\theta=0\). For \(0<f<1\) and \(\eta\le1\), set \(a_f=1-f^2/2>0\). Integrating \(1-\cos t=\int_0^t\sin s\,ds\le t^2/2\) gives
\[
 a_f\|dw\|^2\le E^{f}_{\rm bare}(w)\le\|dw\|^2.          \tag{6.3}
\]

We verify the depth-uniform lower comparison rather than import CF18. Let \(n=L^k\). At one step differentiation of the plain map gives \(P_L=S_L-d\sigma\), and on gradients \(P_Ldf=d(r_Lf)\), since every internal contour telescopes to its endpoint difference. Composition of the straight averages is the straight length-\(n\) average: the block digits enumerate each start and each path position exactly once. Induction therefore gives
\(P^{[k]}w=S_nw+d\psi_k(w)\). Taking coarse curl cancels this gradient. A coarse plaquette of \(S_nw\) is the mean, over its \(n^4\) starts, of the boundary sum on an \(n\)-by-\(n\) square. Cancellation of internal edges expresses it as a positive average of fine plaquette curls. Call the matrix \(T_n\). Each row has total weight \(n^2\). Each fine plaquette is counted \(n^2\) times over all starts and coarse plaquettes of its orientation: there are \(n\) choices of starting coordinate in each longitudinal direction, with the transverse starts fixed. Each occurrence has weight \(n^{-4}\), so every column has weight \(n^{-2}\). Thus
\[
 \|T_nF\|^2\le n^2\sum_{c,p}T_n(c,p)|F_p|^2=\|F\|^2,
 \quad dP^{[k]}w=T_ndw.                                  \tag{6.4}
\]
The norms are the raw-link curl energies at the two lattices; these have the same action normalization in four dimensions. No fine-spacing factor is omitted.

For the operator comparison, change from raw \(w\) to the physical fine coordinate \(h\) by \(w=\eta h\); the per-length row is \(Qh=S_n(\eta h)\). The following gauge algebra uses physical pairings, and passing back to \(w\) preserves its coarse datum and classical value. All inverse formulas in the neutral statements of §§6–7 are formed within the invariant Cartan sector.

Here the weighted classical value really is the neutral specialization of (3.1). To check this, put \(Q=S_n\), with its per-length normalization, and let \(Z_s=\ker Q'\) in the site space. The neutral covariant derivative is the ordinary \(D=d\), and \(R\) projects onto \(D^*DZ_s\). The restriction of \(D\) to \(Z_s\) is injective: a periodic function with zero gradient is constant, and its block mean can vanish only if the constant is zero. For any fine field \(w\), choose the unique \(z\in Z_s\) satisfying \(D^*Dz=-RD^*w\). This exists by the definition of that range. Adding \(Dz\) preserves \(Qw\), because \(QD z=dQ'z=0\); preserves the weighted curl energy; and makes \(RD^*(w+Dz)=0\). Thus the minimum of the fine gauge-fixed form at \(Qw=b\), minus its fixed row mass \(\langle b,ab\rangle\), is exactly the minimum of the weighted curl energy at \(Qw=b\). Completing the square for a positive fine precision \(K\) gives that minimum including row mass as \(\langle b,(QK^{-1}Q^T)^{-1}b\rangle\): the minimizer is \(K^{-1}Q^T(QK^{-1}Q^T)^{-1}b\), and its cross term against \(\ker Q\) vanishes. Positivity here follows because a zero of curl, gauge and row mass is zero: a closed field is a gradient plus a constant, its zero straight average removes the constant and makes its potential have constant block mean, and the gauge term then kills that gradient. The Fourier argument for the decomposition of closed fields is given in §7. The current corrections in (3.1) vanish on the neutral sector.

Replacing \(S_n\) by \(P^{[k]}\) leaves this minimum unchanged. Their difference is a coarse gradient. Such a discrepancy can be repaired at zero curl cost by a fine gradient: for \(P^{[k]}\) prescribe the potential at the coarse centers; for \(S_n\) prescribe its block means. These prescriptions are onto on disjoint blocks, and both maps send gradients to the corresponding coarse gradients. This proves both inequalities between the two minima. It supplies the exact identification with the actual neutral precision.

Define the neutral classical value
\(E_k^f(b)=\min_{P^{[k]}w=b}E^{f}_{\rm bare}(w)\). The constraint is onto: each one-step plain row has its own pivot coefficient \(L^{-3}\), so successive pivot lifts give a lift of any datum. In finite dimension a positive semidefinite quadratic has a minimum on such an affine space, by orthogonal projection of its image under the square root. Equations (6.3)–(6.4) imply
\[
 E_k^f(b)\ge a_f\|db\|^2.
\]
Let \(C_0\) be the flat one-step pivot map on the current lattice. Equation (5.2), with \(K_0C_0u=0\), gives
\[
 E_k^f(C_0u)+\|G_0C_0u\|^2
       \ge {a_f\over A_L}\|C_0u\|^2
       \ge {a_f\over A_L}\|u\|^2.                        \tag{6.5}
\]
This constant is independent of \(k,T\), and every conditioned neutral-coordinate subset has the same bound by (2.1). This rebuilds the relevant CF18/WI15 lower-bound mechanism for a nonzero-curvature family. It does not treat the two charged colors.

## 7. Relative Schur stability and the neutral complex neighbourhood

**Proved linear-algebra lemma.** Let \(K_0>0\) be real symmetric, \(Q\) real and onto, and \(K\) complex symmetric, with
\[
 \|K_0^{-1/2}(K-K_0)K_0^{-1/2}\|\le e<1/2.
\]
Put \(W_0=QK_0^{-1}Q^T\), \(S_0=W_0^{-1}\), and \(W=QK^{-1}Q^T\). Both inverses defining \(S=W^{-1}\) exist, and
\[
 \|S_0^{-1/2}(S-S_0)S_0^{-1/2}\|
                      \le {e\over1-2e}.                 \tag{7.1}
\]
Indeed set \(B=K_0^{-1/2}(K-K_0)K_0^{-1/2}\) and
\(Z=K_0^{-1/2}Q^TW_0^{-1/2}\). Then \(Z^TZ=I\), so \(Z\) is a real isometry. The Neumann series for \(I+B\) gives
\[
 W_0^{-1/2}(W-W_0)W_0^{-1/2}
      =Z^T[(I+B)^{-1}-I]Z=:D,\qquad
 \|D\|\le e/(1-e)<1.
\]
Consequently \(S=S_0^{1/2}(I+D)^{-1}S_0^{1/2}\), and a second Neumann series gives (7.1). These are bilinear transposes of the holomorphic matrices; Hermitian norms enter only their bounds. No eigenvalue bound for \(K_0\) uniform in dimension was needed. If \(e\le1/4\), then \(\operatorname{Re}\langle b,Sb\rangle_H\ge\tfrac12\langle b,S_0b\rangle_H\).

Apply this to the neutral family of §6. Quotient the fine bond space by \(\ker d\), and the coarse bond space by \(\ker d\). The induced plain average is well-defined by (6.4) and is onto. Closed coarse data have closed fine lifts: a gradient lifts by assigning its site potential at the coarse nodes and extending to fine sites; the identity \(P^{[k]}df=d(r_nf)\) gives its exact image. A harmonic constant lifts by dividing its bond values by \(n\). To see that these exhaust the closed data, Fourier transformation turns closedness into \(t_\mu b_\nu=t_\nu b_\mu\); for a nonzero momentum some \(t_\mu\ne0\), giving a gradient, and zero momentum gives the constants. This also checks that minimizing over a coarse equivalence class gives exactly the prescribed-data classical value: any closed discrepancy can be repaired at zero curl cost.

On the fine quotient, (6.2) is strictly positive. A complex Cartan perturbation changes its plaquette weights to \(\cos(\theta_p+z_p)\), without changing \(P^{[k]}\) or its kernel. For \(|z_p|\le r\le1\), the exponential series gives \(|\sin(\theta_p+tz_p)|\le4\), \(0\le t\le1\), so the weight difference is at most \(4r\). Its relative form norm is at most \(4r/a_f\). Choose \(r\le a_f/16\); (7.1) proves that the complex neutral Schur form has Hermitian real part at least half its real reference value, uniformly in depth and volume. The real identification in §6 continues holomorphically: both sides are finite rational matrix functions of the plaquette weights after quotienting their fixed kernels, their denominators are nonzero on this relative ball, and their Taylor coefficients agree because their values agree for all positive real weights near the reference weights.

The physical perturbation radius can also be taken independent of depth. Write the Cartan increment as \(W=e^{i\eta E Z}U\), with \(|E|,|\nabla E|\le\rho\). Its fine plaquette-angle increment is at most \(4\rho\eta^2\). Exact abelian curvature averaging makes the level-\(s\) plaquette increment at most \(4\rho\xi_s^2\). Let \(a_s\) bound the raw relative edge phase at that level, so \(a_0\le\rho\eta\). Each averaged edge differs from its central straight edge by an average of closed-loop fluxes. The loops fill at most \(C L^2\) level-\(s\) plaquettes, by commuting the at-most-\(6L\) path steps. Thus, with a fixed \(C_L\),
\[
 a_{s+1}\le L a_s+C_L\rho\xi_s^2,
 \quad {a_s\over\xi_s}
       \le\rho+{C_L\rho\over L}\sum_{t<s}\xi_t
       \le\rho+{C_L\rho\over L(L-1)}.                   \tag{7.2}
\]
The last inequality uses \(s\le k\), \(\xi_k=1\). The scalar phases are followed on their continuous relative branches; the bounds keep every closed logarithm on its admitted branch. Global flux and the large seam links in (6.1) do not affect these relative abelian identities.

At the current lattice, an internal contour has at most \(4L\) links. Its phase increment \(\gamma_{y,x}\) is at most \(4La_k\le C'_L\rho\). The gauge Hessian is now exactly \(\sum_{y,x}\cos\gamma_{y,x}\,|G_0b(y,x)|^2\) as a bilinear form. For \(|\gamma_{y,x}|\le1/4\), its Hermitian real part is at least half the real gauge form, since the exponential series bounds \(|\cos\gamma-1|\le1/2\) on that disc. Choose \(\rho_L>0\) so that \(4\rho_L\le a_f/16\), \(C'_L\rho_L\le1/4\), and the finite mean branches above remain admitted. The pivot map is still \(C_0\), because the neutral constraint is exactly linear. Adding the two half-bounds and using (6.5) proves
\[
 \operatorname{Re}\langle u,\mathsf A^{\rm neutral}_{k,W}u\rangle_H
                   \ge {a_f\over2A_L}\|u\|^2             \tag{7.3}
\]
for every previous depth and volume. An independent Cartan current contributes no commutator or constraint-curvature term in this sector. All neutral coordinate compressions satisfy (7.3). This closes the real and complex neutral versions of the explicit curved test family.

## 8. The nonabelian constraint's second jet has no depth factor

**Proved coefficient estimate.** This ports the second-jet summation in c0-loc.md §9 to the actual straightened Federbush map. The same density mechanism appears as PX141–154 in the Sussman–Alpoge outline, lines 11520–11647; the derivation below checks the particular factors it uses. Fix \(L\). For a row \(c\) of length \(\xi=L^j\eta\), write
\[
 q_c(H)=\xi^{-1}a_j(c),\qquad
 a_0=\eta H,\quad a_{s+1}=F_{W_s}(a_s),\quad
 W_s=\mathcal M^sW_0 .
\]
The one-step function is, literally,
\[
 \begin{split}
 u_W(a)(y)&=\exp\!\left[L^{-4}\sum_{x\in B(y)}
       \log\{T_{yx}(e^{ia}W)T_{yx}(W)^{-1}\}\right],\\
 F_W(a)(c)&={1\over i}\log\{
 u_W(a)(c_-)^{-1}\mathcal M(e^{ia}W)(c)
 u_W(a)(c_+)\mathcal M(W)(c)^{-1}\}.
 \end{split}                                                   \tag{8.1}
\]
Here \(T\) is the outline's internal Federbush mean, not a chosen single path. All coefficients below are evaluated at \(H=0\), and \(W_0\) can be complex. On the row's dependence cube assume the outline's regular-pair local gauge, with the adjacent-scale factor included in \(a\):
\[
 |A|+|E|\le a/\xi,\qquad
 |\nabla A|+|\nabla_U E|\le a/\xi^2,\qquad
 W_0=e^{i\eta E}U,\quad U=e^{i\eta A}.
                                                               \tag{8.2}
\]
A sufficiently small \(a=a(L)>0\) gives
\[
 \sup_b\sum_{b'}\|D_bD_{b'}q_c(0)\|
       \le C_L\,\xi(\eta/\xi)^4 .                              \tag{8.3}
\]
The other-leg bound is identical. \(C_L\) is independent of the depth, volume and chosen row.

First check that repeated maps remain in their analytic balls with summable radii. In the one local gauge put \(t_s=L^s\eta/\xi\), \(v_s=\sup|\log W_s/i|\), and \(p_s=\sup|\partial W_s-1|\), taking the suprema on the dependence cone. Expanding a fine plaquette using (8.2) gives \(v_0\le C_La t_0\), \(p_0\le C_L(a+a^2)t_0^2\). There is no term of order \(\eta|E|\) in the plaquette: the four linear insertions telescope to a first difference; the remaining terms contain two link logarithms. The finite one-step formulas give
\[
 v_{s+1}\le Lv_s+C_L(v_s^2+p_s),\qquad
 p_{s+1}\le L^2(1+C_Lv_s)p_s+C_Lp_s^2.                         \tag{8.4}
\]
For the first inequality compare every contour with the central straight segment. A swap of adjacent perpendicular steps inserts a conjugated plaquette, and at most \(C_L\) swaps are needed. Products and logarithms on the fixed small ball give the displayed remainder. For the second put that one-step patch in comb gauge. Each non-tree bond differs from one by at most \(C_Lp_s\), by moving its extra step through the comb. At the identity the coarse plaquette derivative is the average of the \(L\)-square fluxes; its absolute row sum is \(L^2\), by the cancellation used in (6.4). Its Taylor remainder on this finite patch is \(C_Lp_s^2\). Undoing the comb gauge changes the plaquette norm by at most \(1+C_Lv_s\), because the comb has at most \(C_L\) links with condition numbers \(1+O(v_s)\). These arguments use finite convergent series and the mean contraction from §5, so they apply to complex links too.

Let \(z_s=v_s/t_s+p_s/t_s^2\). Dividing (8.4) by \(t_{s+1}\) and \(t_{s+1}^2\) gives
\[
 z_{s+1}\le z_s+C_Lt_s(z_s+z_s^2),\qquad
 \sum_{s<j}t_s={1-L^{-j}\over L-1}.
\]
As long as \(z_s\le1\), multiplication yields
\(z_s\le z_0\exp(2C_L/(L-1))\).
Choose \(a\) so this last quantity is less than \(1/2\) and all raw logarithms lie in the fixed one-step ball. Induction excludes a first exit. In particular
\[
 v_s\le C'_L a t_s,\qquad \sum_{s<j}v_s\le C'_La/(L-1).
                                                               \tag{8.5}
\]
The dependence cube fits in the stipulated local gauge cube; no global logarithm or gauge is being chosen.

At \(W=1,a=0\), differentiation of (8.1) cancels the two internal-contour terms in the plain derivative. The remaining raw map is \(S_L\). Its row sum is \(L\), and its column sum is \(L^{-3}\): a given fine bond lies on \(L\) start-position segments, each of weight \(L^{-4}\). The analytic functions in (8.1) have finitely many inputs and outputs at fixed \(L\). Their first and second derivatives are bounded on a closed smaller ball by the exponential/logarithm series and the mean contraction already proved. A fine bond occurs in only a fixed number of output carriers. Thus, for \(A_s=D F_{W_s}(0)\), entrywise Taylor expansion and these finite incidence counts give
\[
 \|A_s\|_{\rm row}\le L(1+C_Lv_s),\quad
 \|A_s\|_{\rm col}\le L^{-3}(1+C_Lv_s),\quad
 \sup_i\sum_{c,h}\|(D^2F_{W_s}(0))_{c;i,h}\|\le C_L .
                                                               \tag{8.6}
\]
This does not infer a column bound from a row bound. Each error entry is bounded by a derivative maximum times \(v_s\); the number of entries incident to a fixed input is finite at fixed \(L\); dividing by \(L^{-3}\) is absorbed in \(C_L\). For a single dependence cone, restricting the matrices only decreases the sums. The starting gauge was unitary, so changing into it preserves the color norms.

Put \(P_{b,a}=A_{b-1}\cdots A_a\). By (8.5), after decreasing the ceiling once,
\[
 \|P_{b,a}\|_{\rm row}\le2L^{b-a},\qquad
 \|P_{b,a}\|_{\rm col}\le2L^{-3(b-a)} .                        \tag{8.7}
\]
Indeed each multiplicative error product is at most
\(\exp(C_L\sum_s v_s)\le2\). Multiplying a fixed constant larger than one at each level would be incorrect here.

The second-derivative chain rule, proved by differentiating the first-derivative product once and assigning the differentiated factor its level, is
\[
 D^2a_j=\sum_{s<j}P_{j,s+1}
       D^2F_{W_s}(0)[P_{s,0}\,\cdot,P_{s,0}\,\cdot].
                                                               \tag{8.8}
\]
Fix output \(c\) and first fine input \(b\), then sum the absolute coefficients over the second input. In the \(s\)-term, an entry of the outer product is at most \(2L^{-3(j-s-1)}\). The fixed first input has inner column sum \(2L^{-3s}\); the summed second input has inner row sum \(2L^s\). The remaining output/input sums of the one-step Hessian are bounded by (8.6). Hence the raw coefficient sum is at most
\[
 C_L\sum_{s<j}L^{-3(j-s-1)}L^{-2s}
 = C_LL^{-3j+3}\sum_{s<j}L^s
 \le C'_LL^{-2j}.                                           \tag{8.9}
\]
The two physical input derivatives supply \(\eta^2\), and the per-length output supplies \(\xi^{-1}\). Since
\(\eta^2\xi^{-1}L^{-2j}=\xi(\eta/\xi)^4\), (8.9) proves (8.3). Symmetry of the second derivative proves the exchanged-leg estimate.

Now let a **specified** row multiplier satisfy
\(|\omega_c|\le\gamma\xi_c^{-3}\).
Use the physical row volume \(\xi_c^4\) and define the fine mass norm by
\(\|H\|_{\rm m}^2=\sum_b\eta^4\sigma_b^{-2}|H_b|^2\), where \(\sigma_b\) is the retained scale at that fine bond. Then
\[
 \left|\sum_c\xi_c^4
       \langle\omega_c,D^2q_c(0)[H,V]\rangle\right|
       \le C_L\gamma\|H\|_{\rm m}\|V\|_{\rm m}.                \tag{8.10}
\]
To check the geometry in this last step, a determining row's carrier consists of its endpoint pillars, lies inside the preceding region and outside the next region, and meets only the two adjacent retained scales. A fixed fine bond therefore belongs to carriers at only adjacent levels and to a fixed number of rows at each such level. This is the separated, whole-block geometry specified at outline lines 10115–10127; it is not a claim for arbitrary overlapping nests. Multiplying (8.3) by \(\xi_c^4|\omega_c|\) gives
\(C_L\gamma\eta^4\xi_c^{-2}\).
On that carrier \(\xi_c/\sigma_b\) and \(\sigma_b/\sigma_{b'}\) are bounded by fixed powers of \(L\). After division by the square roots of the fine masses on both legs, the symmetric coefficient matrix has row and column sums at most \(C_L\gamma\). The Cauchy/Schur calculation in §5 proves (8.10).

Thus this particular proposed depth instability fails: the quadratic constraint term with a scale-bounded row current costs \(C_L\gamma\), not \(k\gamma\). The estimate holds for the actual nonabelian map and complex regular references. It supplies a form bound for a given multiplier; it has not estimated the induced multiplier \(\mathsf H^{\mathsf T}J\) in (3.1).

## 9. Closing the multiplier estimate on shell

**Proved.** For the actual independent straightened rows in the separated geometry, at a sufficiently small regular pair, there is a right inverse \(E\) with
\[
 QE=1,\qquad
 \sum_b\eta^4\sigma_b^{-3}|(E\psi)_b|
                \le C_L\sum_c\xi_c|\psi_c|.                   \tag{9.1}
\]
Consequently, if \(J=Q^{\mathsf T}\omega\) and
\(\sup_b\sigma_b^3|J_b|\le\gamma\), then
\[
                 \sup_c\xi_c^3|\omega_c|\le C_L\gamma.
                                                               \tag{9.2}
\]
No inverse propagator estimate enters this assertion. The construction is the row-seed method of Sussman–Alpoge PX127–135, simplified here because (9.1) needs no gradient bound on the seed.

Here are explicit seeds, including small blocks. In a pillar of odd side \(n=2m+1\ge3\) fine spacings, fix an orientation \(\mu\). Its strictly internal \(\mu\)-bonds have longitudinal positions \(i=-m,\ldots,m-1\); put \(x_i=i+1/2\). Make the seed constant over all \(n^3\) transverse sites, and set its longitudinal values to
\[
 \phi_\pm(i)=A_n\pm B_n x_i/n,\qquad
 A_n={n\over n-1},\quad
 B_n={6n^2\over(n-1)(n-2)} .                                \tag{9.3}
\]
The two full-grid per-length rows reading the pillar have functionals
\[
 \ell_\pm(\phi)=n^{-2}\sum_i(n/2\pm x_i)\phi(i).
\]
Indeed the outgoing row has \(i+m+1=n/2+x_i\) start positions containing that bond, the incoming row has \(m-i=n/2-x_i\), and the three transverse sums remove \(n^3\) of the \(n^5\) denominator. Symmetry gives \(\sum_i x_i=0\). Summing consecutive squares, or subtracting \(\sum_{r=0}^{n-2}r^2\) after shifting by \((n-2)/2\), gives
\(\sum_i x_i^2=(n-1)n(n-2)/12\).
Substitution in (9.3) therefore gives
\[
 (\ell_+(\phi_+),\ell_-(\phi_+))=(1,0),\qquad
 (\ell_+(\phi_-),\ell_-(\phi_-))=(0,1).
\]
Moreover \(|\phi_\pm|\le4n/(n-1)\le6\). These are signed profiles, with their sign retained. A jump at the pillar boundary is allowed because no energy estimate is asserted for this lift.

Assign each determining row to a top endpoint of its own scale, choosing the inner endpoint for an outward row. Insert \(\phi_+\) or \(\phi_-\) in that pillar with the desired color, normalized in its row frame. At most eight seeds use one pillar; different orientations use different bond components. For a bare row insert its value on that single bare bond. Let \(E^0\) be their sum. The seed support has physical volume at most \(\xi_c^4\), belongs to its own retained layer, and its amplitude is at most \(6|\psi_c|\). Thus
\[
 \sum_b\eta^4\sigma_b^{-3}|(E^0\psi)_b|
                     \le6\sum_c\xi_c|\psi_c|.                 \tag{9.4}
\]
At a flat reference the same-level response is the identity on the full regular row grid, before restricting to the determining rows. Every lower row misses the seed because its carrier is outside its next region. Every row at least two levels higher misses it because its carrier is inside the seed's next region. Only the next level can receive leakage.

On the full flat grids \(Q_{j+1}^0=Q_L^0Q_j^0\): the transverse digits and the longitudinal segment positions enumerate each finer start and segment position exactly once, including the per-length normalization. The next-level leakage is therefore a restriction of \(Q_L^0\) applied to the prescribed same-level row values. This map has column sum \(L^{-4}\). In the row norm
\(\|\psi\|_{1,\xi}=\sum_c\xi_c|\psi_c|\),
its norm is at most \(L^{-3}\). Restrictions to determining rows can only decrease this norm.

At a curved reference choose the real local small gauge on each seed pillar and undo it after inserting (9.3). The scalar estimates (9.4) are unchanged. The first-derivative products in (8.7), telescoped against their flat products, have per-length row error \(C_La\) and column error \(C_La n^{-4}\). To see the latter power directly, every telescoping term has one column error \(L^{-3}C_Lv_s\), the other raw factors contribute \(L^{-3(j-1)}\), and the final per-length factor contributes \(n^{-1}\); summing \(v_s\) uses (8.5). The row error follows with row factors instead.

On an overlapping carrier, two real local gauges differ by a nearly constant unitary matrix. Their link connection equation changes that matrix on one fine edge by at most \(C_La\eta/\xi\); summing along a path of length at most \(C_L\xi/\eta\) bounds its change by \(C_La\). Thus the flat exactness of the seed in one frame differs from its exactness in the other frame by \(C_La\), with no factor depending on fine depth. At the next level the leading response is \(Q_L^0\) with unitary color changes on its entries. Its absolute column bound stays \(L^{-4}\). All deviations are bounded by the coefficient errors just obtained, the seed amplitude six, and the fixed number of incident carriers. In the weighted row norm they total at most \(C_La\). Supports still eliminate every level except the same and the next. We have therefore proved
\[
 QE^0=1+T,\qquad
 \|T\|_{1,\xi\to1,\xi}\le L^{-3}+C_La=:\vartheta<1.
                                                               \tag{9.5}
\]
This argument also covers a complex regular reference, with seeds fixed at its real center. The additional coefficient differences are included in \(a\).

The convergent series \((1+T)^{-1}=\sum_{r\ge0}(-T)^r\) defines \(E=E^0(1+T)^{-1}\). Its norm in (9.1) is at most \(6/(1-\vartheta)\). This proves (9.1), including surjectivity of \(Q\). For the physical density pairings, stationarity then gives
\[
 |\langle\omega,\psi\rangle_{\rm rows}|
   =|\langle J,E\psi\rangle_{\rm fine}|
   \le {6\gamma\over1-\vartheta}\|\psi\|_{1,\xi}.
\]
Take \(\psi\) supported on one row and in a unit color direction maximizing the absolute scalar product with \(\omega_c\). Since its row volume is \(\xi_c^4\), this proves (9.2), for real or complex coefficients.

The condition \(J=Q^{\mathsf T}\omega\) holds at an admitted physical critical field in the fixed Landau slice; here is the algebra, following PX93 rather than presuming an inverse bound. Put \(Z_s=\ker Q'\), \(\Delta=D^{\mathsf T}D\), and \(R=\operatorname{proj}(\Delta Z_s)\). The admitted removal of residual gauge directions makes \(D|_{Z_s}\) injective. For \(f=\Delta z\), \(z\in Z_s\), the scalar inverse \(G'=(\Delta+Q'^{\mathsf T}aQ')^{-1}\) obeys \(G'f=z\). It follows that
\[
 S=1-DG'RD^{\mathsf T},\quad
 RD^{\mathsf T}S=0,\quad QS=Q .
\]
For the last identity only \(QD Z_s=0\) is needed. At one step, differentiating a fine gauge transform gives contour variation
\(\lambda(y)-\operatorname{Ad}(T_{yx})\lambda(x)\).
The derivative of \(u\) in (8.1) is consequently the center value minus its transported block mean. Subtracting the two endpoint factors leaves the coarse gradient of that mean. Iteration proves the same statement on every retained row. At an outward endpoint the appropriate full-pillar mean is obtained recursively from its finer leaf means; if all leaf means vanish, so does it. Thus \(QD Z_s=0\), including outward rows.

For \(v\in\ker Q\), \(Sv\) is a tangent vector in the fixed slice, so physical criticality gives \(\langle J,Sv\rangle=0\). The difference \(v-Sv\) is an allowed infinitesimal gauge variation; gauge invariance of the Wilson action gives \(\langle J,v-Sv\rangle=0\). Therefore \(J\) annihilates \(\ker Q\). Because \(Q\) is onto by (9.1), ordinary finite-dimensional duality gives the unique \(\omega\) with \(J=Q^{\mathsf T}\omega\). Any right inverse \(H\) of \(Q\), in particular either outline readout when defined, has \(H^{\mathsf T}J=\omega\). This proves the on-shell bound for that actual readout without assuming its decay.

Combining (9.2) and (8.10) now closes the form estimate at such a physical pair:
\[
 \beta=\Delta_U^{\rm W}-D^2q[\omega],\qquad
 |\beta[H,V]-\langle d_UH,d_UV\rangle|
       \le C_L(\alpha_0+\gamma_0)\|H\|_{\rm m}\|V\|_{\rm m}.
                                                               \tag{9.6}
\]
For the Wilson term the sixteen plaquette insertions used in §5 give an error bounded by \(C|\partial U_p-1|\eta^2\) on each incident pair of physical fine variables. The regular bound \(|\partial U_p-1|\le\alpha_0\eta^2\sigma_p^{-2}\), the bounded plaquette incidences, and adjacent-scale comparability give \(C_L\alpha_0\) in the mass norm. The constraint term is (8.10) with (9.2). Thus (9.6) concerns the actual stationary Lagrangian form of the straightened constraints, with its nonzero multiplier retained.

## 10. The full-color fine Landau form on a uniform torus

**Proved smaller coercivity theorem.** Take a whole torus with all determining rows at the same physical scale one, fine spacing \(\eta=L^{-k}\), and no node or seam restrictions. Suppose the real background is a critical point for the actual straightened constraint, satisfies the regular-pair bounds, and has the stated local gauges on the fixed cubes used below. For sufficiently small \(\alpha_0,\gamma_0\), independent of \(k\) and volume, the actual physical fine form
\[
 K_{\rm phys}=\beta+DRD^{\mathsf T}+Q^{\mathsf T}Q
 \quad\hbox{satisfies}\quad
 \langle H,K_{\rm phys}H\rangle\ge c_L\|H\|^2 .
                                                               \tag{10.1}
\]
Here \(\beta\) is (9.6), \(Q\) is the straightened \(k\)-step map, and \(R\) is precisely the outline's Landau projection. This is a statement about the fine precision, before the row mass is subtracted in (3.1).

We first prove the projected graph estimate for these actual means. The flat inequality needed is
\[
 \|h\|^2+\|\partial h\|^2
 \le C_T\{\|dh\|^2+\|P_0D_0^*h\|^2\},
 \qquad Q_0h=0,\quad P_0=1-r_0^*r_0 .                        \tag{10.2}
\]
This is the flat torus step of c0-loc.md (6.4), whose Fourier calculation can be checked as follows. At coarse momentum \(p\) and aliases \(q=p+2\pi n\), write
\[
 \delta_\mu(q)=(e^{i\eta q_\mu}-1)/\eta,\quad
 \delta'_\mu(p)=e^{ip_\mu}-1,\quad
 \widehat r(q)=\prod_\mu b_\mu(q),\quad
 \widehat Q_\mu(q)=\widehat r(q)b_\mu(q),
\]
where \(b_\mu(q)=\eta\sum_{s=0}^{\eta^{-1}-1}e^{i\eta q_\mu s}\); centering phases are chosen consistently with \(Q_0D_0=D' r_0\). Finite root-of-unity sums give \(\sum_{\rm alias}|\widehat r|^2=1\). Put \(B(p)=\sum|\widehat r|^2/|\delta|^2\). For \(p\ne0\), concavity of sine gives
\[
 B(p)|\delta'(p)|^2\ge c_1=(2/\pi)^{10},\qquad
 |\delta'(p)|^2\sum_{\rm alias}|\widehat Q_\mu|^2/|\delta|^2
       \le c_2=(\pi/2)^2 .
\]
For the lower bound keep the \(q=p\) term, use \(|b_\mu(p)|\ge2/\pi\), \(|\delta(p)|\le|p|\), and \(|\delta'(p)|\ge2|p|/\pi\). For the upper bound use \(|b_\mu|\le1\), \(|\delta(q)|\ge2|q|/\pi\), \(|q|\ge|p|\), and \(|\delta'(p)|\le|p|\).

Set \(\varphi=D_0^*h\), \(c=r_0\varphi\), \(g=(-\Delta)^{-1}r_0^*B^{-1}c\), and \(\zeta=\delta' B^{-1}c/|\delta'|^2\). At \(p=0\) set these to zero: \(c=0\) there because only the zero fine alias survives in \(r_0\), and a divergence has zero mean. Then \(r_0g=c\), \(D'^*\zeta=B^{-1}c\), and \(e=D_0g-Q_0^*\zeta\) is divergence free. The component identity
\(|\delta|^2I=\delta\delta^*+(\delta\wedge)^*(\delta\wedge)\)
gives \(e=d^*(-\Delta)^{-1}de\) and \(de=-dQ_0^*\zeta\). The displayed Fourier bounds imply
\[
 \|g\|\le g_0\|c\|,\qquad
 \|(-\Delta)^{-1}de\|\le b_0\|c\|,
 \quad g_0=(\pi/2)^2/c_1,\quad b_0=\sqrt{c_2}/c_1.
\]
For the first, bound each inverse fine Laplacian by \((\pi/2)^2|p|^{-2}\) and use \(B^{-1}\le |p|^2/c_1\). For the second, use the second Fourier bound and \(B^{-1}\le|\delta'|^2/c_1\). Pair \(g\) with \(\varphi\); \(Q_0h=0\) removes \(Q_0^*\zeta\). The result is
\(\|c\|\le b_0\|dh\|+g_0\|P_0\varphi\|\).
Hodge's component identity now bounds \(\|\partial h\|^2=\|dh\|^2+\|\varphi\|^2\) by \(C(\|dh\|^2+\|P_0\varphi\|^2)\). Each \(Q_0\) row has positive density of integral one, bounded by one, on a cube of side at most three. The cube variance inequality, followed by the zero moment of its component of \(h\), bounds its mass by \(9d(1+3^d)\) times the local gradient energy. The variance inequality itself follows by writing each difference \(h(x)-h(y)\) as the sum on the four coordinate segments, applying Cauchy on each segment, and averaging \(x,y\); every bond is counted at most the cube length times its transverse volume. Summing the bounded overlaps proves (10.2), with \(C_T\) independent of \(\eta\) and the torus.

The corresponding inhomogeneous inequality has an added term \(C\|Q_0h\|_{\rm rows}^2\). Here is the required lift with an energy bound. For \(n=\eta^{-1}\ge128\), replace the transverse constants of (9.3) by normalized triangular tents supported in the central half of their intervals. On longitudinal internal bonds use a tent \(p\), of average one, and put \(t=(i+m+1)/n\). If \(a=\operatorname{av}(tp)\), \(v=\operatorname{av}((t-a)^2p)\), the profiles
\[
 p[1-a(t-a)/v],\qquad p[1+(1-a)(t-a)/v]
\]
have respective moments \((1,0)\) and \((0,1)\) against \((1-t,t)\), by direct expansion. Each of the intervals \([5/16,3/8]\) and \([5/8,11/16]\) has tent mass at least \(1/128\); the pair-variance identity gives \(v\ge2^{-18}\). Thus the profiles have a uniform supremum and first difference bounded by \(C/n\). Tensoring, summing the at most eight incident seeds and counting volumes gives a lift \(E_0\) with \(Q_0E_0=1\) and
\(\|E_0b\|+\|\partial E_0b\|\le K\|b\|_{\rm rows}\).
For the finitely many odd \(3\le n<128\), use (9.3): its supremum is at most six and each physical difference is at most \(12n\), so the same bound holds with a larger fixed \(K\). At \(n=1\) use the identity. Apply (10.2) to \(h-E_0Q_0h\) and use \(\|dE_0b\|+\|D_0^*E_0b\|\le C K\|b\|\). This proves the inhomogeneous version.

On a fixed coordinate cube the regular local gauge makes \(U=e^{i\eta A}\), with \(|A|\le C_L\alpha_0\). The first-derivative comparison in §§8–9 gives
\[
 \|(Q-Q_0)h\|_{\rm rows}\le C_L\alpha_0\|h\|,\quad
 \|r-r_0\|_{2\to2}\le C_L\alpha_0,\quad
 \|(D-D_0)f\|\le C_L\alpha_0\|f\|.                           \tag{10.3}
\]
For the site estimate each coefficient is its uniform block weight times an adjoint transport. The hierarchical product of those transports differs from one by \(C_L\sum_s v_s\le C_L\alpha_0\), from (8.5). Weighted row and column sums give the estimate. Distinct site pillars are disjoint and each coefficient is a unitary transport, so \(rr^*=r_0r_0^*=1\). Consequently \(P=1-r^*r\) differs from \(P_0\) in norm by \(C_L\alpha_0\). In particular
\[
 \|(P D^*-P_0D_0^*)h\|
       \le C_L\alpha_0(\|h\|+\|\partial h\|).
\]
The curl and full component gradient have the same connection comparison as \(D\). Insert (10.3) in the inhomogeneous flat estimate and absorb the term \(C_L\alpha_0(\|h\|+\|\partial h\|)\). This proves on that cube
\[
 \|h\|^2+\|\nabla_Uh\|^2
 \le C_L\{\|d_Uh\|^2+\|PD_U^*h\|^2+\|Qh\|_{\rm rows}^2\}.
                                                               \tag{10.4}
\]
For the flat comparison use a model torus containing the supported field and all its row and site carriers, extending by zero; the constant in (10.2) is independent of that torus. This is the coordinate-patch repair D3 in the c0-loc gate.

For completeness, globalization does not require differentiating the hierarchical site frames. Choose translates of a fixed tent of width \(R\), then divide each by the square root of the sum of their squares. With translation spacing \(R/2\), that denominator is bounded above and below, the overlap is bounded, and \(\sum_i\chi_i^2=1\), \(\sum_i|\partial\chi_i|^2\le C/R^2\). Use cubes enlarged by a fixed number of unit blocks for their row carriers. On a site pillar or a bond-row carrier the oscillation of each \(\chi_i\) is at most \(C/R\). Since \(P=1-r^*r\) is block diagonal on the site pillars with norm at most one, direct insertion of \(\chi_i-\chi_i(y)\) on its two sides gives
\[
 \sum_i\|[P,\chi_i]f\|^2\le C R^{-2}\|f\|^2.
\]
The same row/column argument for \(Q\), using its bounded density from (8.7), gives
\(\sum_i\|Q(\chi_iH)-\chi_i(c_-)QH\|^2\le C_LR^{-2}\|H\|^2\).
The product rule for \(d_U,D_U^*\) adds at most \(C/R\) times \(H\). Finally \(\|D_U^*H\|\le2\|\nabla_UH\|\), by Cauchy over its four components. Apply (10.4) to each \(\chi_iH\) in its own real local gauge and sum. Gauge covariance preserves all norms. The errors are bounded by
\(C_LR^{-2}(\|H\|^2+\|\nabla_UH\|^2)\).
Choose \(R\) first so this can be absorbed, and then choose \(\alpha_0\) for (10.3) on those fixed cubes. The required local gauges exist by the regularity premise when its fixed read cubes contain these cubes. A periodic lifted cover handles holonomy; it does not identify distinct lifted occurrences in a local gauge. Thus (10.4) holds globally with constants independent of depth and volume.

We next check the null identity rather than infer it from gauge invariance of the Wilson Hessian. The exact factorization defining the straightened map makes its variation under a fine gauge parameter \(\lambda\) the coarse gauge variation with a smooth parameter \(\widetilde r(A)\lambda\). At \(A=0\), this map is \(Q'\), as calculated in §9. It is onto because \(Q'Q'^{\mathsf T}=1\) at the real center; finite-dimensional continuity keeps it onto nearby. For \(z\in\ker Q'\) define smoothly
\[
 \lambda_z(A)=z-\widetilde r(A)^{\mathsf T}
    [\widetilde r(A)\widetilde r(A)^{\mathsf T}]^{-1}
                  \widetilde r(A)z .
\]
The resulting infinitesimal fine gauge field \(X_z(A)\), expressed in the increment coordinates, satisfies \(Dq(A)X_z(A)=0\), \(DF(A)X_z(A)=0\), and \(X_z(0)=D_Uz\). Set \(\mathcal L=F-\langle\omega,q\rangle\). Since \(D\mathcal L(0)=0\), differentiating \(D\mathcal L(A)X_z(A)=0\) in any direction proves
\[
                       \beta(D_Uz,v)=0
                       \quad\hbox{for every }v.               \tag{10.5}
\]
Only a finite local neighborhood is used for this identity, so its radius need not be uniform in the number of variables.

The scalar Poincare constant on \(\ker Q'\) is uniform too. On each unit pillar, the coordinate-path variance proof gives \(\|z-\operatorname{av}z\|\le C\|\partial z\|\). In its local gauge \(Q'z=0\) and (10.3) give \(|\operatorname{av}z|\le C_L\alpha_0\|z\|\); also \(\|\partial z\|\le\|D_Uz\|+C_L\alpha_0\|z\|\). Absorption and summation over the disjoint pillars yield
\(\|z\|\le p_L\|D_Uz\|\), uniformly in depth.

At this single retained scale the mass norm in (9.6) is just \(\|H\|\). Put \(\widetilde\beta=\beta+Q^{\mathsf T}Q\). The global (10.4) and (9.6), after taking \(C_L(\alpha_0+\gamma_0)\) small enough, give
\[
 \|H\|^2+\|D_U^*H\|^2
       \le K_L\{\widetilde\beta[H,H]+\|PD_U^*H\|^2\}
                         \quad\hbox{for all }H.
\]
Equations (10.5) and \(QD_Uz=0\) make \(\widetilde\beta(D_Uz,v)=0\). Apply the already proved argument of §4 with the ambient constraint taken to be zero. It gives
\[
 \|H\|^2\le K_L(1+2p_L^2)\widetilde\beta[H,H]
                         +2p_L^2\|RD_U^*H\|^2.
\]
Both terms on the right are nonnegative by that same orthogonal-decomposition proof. Dividing by the larger coefficient proves (10.1). At a physical critical field the outline's invariant extension is \(S^{\mathsf T}\Delta_U^{\rm W}S\); the multiplier is the \(\omega\) of §9. Hence its fine second variant is \(S^{\mathsf T}\beta S+DRD^{\mathsf T}+Q^{\mathsf T}Q\). Equation (10.5) gives \(S^{\mathsf T}\beta S=\beta\), so this is the actual \(K_{\rm phys}\) of (10.1), not a Feynman replacement.

## 11. Real A2 on that uniform, node-free torus, at every depth

**Proved.** In the setting of §10, let \(V=\mathcal M^kU\) be in the next step's block axial gauge, with every next block node free. Then, after one fixed further decrease of the regularity ceilings, the actual physical coarse precision \(\mathsf A\) in (3.1) satisfies
\[
                       \mathsf A\ge c_L I                   \tag{11.1}
\]
for every previous depth and every compatible volume for which the stipulated local gauges are available. Every free-coordinate conditioning has the same bound. This treats all three colors and a nonzero physical current.

The step that prevents the row-mass subtraction from losing the bound is the following comparison, for every fine field \(h\):
\[
 \|d_V Qh\|^2
       \le C_L\{\|d_Uh\|^2+\alpha_0^2\|h\|^2\}.              \tag{11.2}
\]
To prove it, choose a single real local gauge on the dependence cube of a coarse plaquette. In that frame the actual row map differs from \(Q_0\) by the row and column estimates of (10.3), while the links of \(V\) differ from one by \(C_L\alpha_0\), by (8.4)–(8.5). At coarse spacing one, taking a plaquette difference of a row error costs only four neighboring rows. At fine spacing \(\eta\), \(d_U-d_0\) is bounded by \(C_L\alpha_0\) times the field because each connection factor is \(1+O(\eta\alpha_0)\). The exact flat identity is \(d_0Q_0h=T_nd_0h\), with physical normalizations and norm at most one, as checked in (6.4). Therefore, in that frame,
\[
 d_VQh=T_nd_Uh+\mathcal R h,\qquad
                    \|\mathcal R h\|\le C_L\alpha_0\|h\|
\]
on the enlarged carrier. Sum over the coarse plaquettes. The positive scalar majorant of \(T_n\) has the same row and column sums even when the unitary input and output frames differ from one plaquette to another. Every error carrier meets only a fixed number of neighboring coarse cells. The same Schur bound therefore proves (11.2) globally. This uses a local small potential, not a globally small torus logarithm.

Let \(f(b)\) be the action on the local critical branch for the straightened datum \(b\), with base datum zero. Its Hessian at zero is the minimum of \(\beta\) under \(Qh=b\). This finite-dimensional assertion does not need an assumed response bound. Indeed choose the slice \(PD_U^*h=0\). By (10.4), on its intersection with \(\ker Q\), (9.6) makes \(\beta\) strictly positive in the graph norm. The row lift gives surjectivity; subtracting \(D_Uz\), with \(z\in\ker Q'\), puts any lift in this slice without changing its row value. The slice equation has a unique solution because \(D_U|_{\ker Q'}\) has the scalar Poincare bound proved above. The finite constrained Hessian is therefore invertible on this slice. The implicit-function theorem, which here follows by writing its nonlinear remainder as a contraction after applying that finite inverse, supplies the local branch. No uniform branch radius is claimed or used in differentiating at zero.

Differentiate \(F'(A)=Dq(A)^{\mathsf T}\omega(A)\) and \(q(A)=b\) along this branch. Its tangent \(h_b\) satisfies \(Qh_b=b\), and \(\beta(h_b,v)=0\) for every slice vector \(v\in\ker Q\). Differentiating the value twice gives
\[
 f'(0)=\omega,\qquad f''(0)[b,b]=\beta[h_b,h_b]
                         =\min_{Qh=b}\beta[h,h].              \tag{11.3}
\]
The last equality follows by writing \(h=h_b+v\), killing the cross term by the differentiated equation and using positivity on the slice kernel. The gauge null identity (10.5) permits passage to and from that slice, without changing the value.

This is also the critical value for the *plain* datum \(e^{ib}V\). The exact straightening factorization says that \(q(A)=b\) gives a plain datum gauge equivalent to \(e^{ib}V\). Prescribe the inverse of its node factor at the coarse nodes and extend this to a fine gauge transformation; this restores the plain datum and preserves the action. Conversely, a nearby field with the given plain datum can be transformed with a fine gauge equal to one at those nodes until its node factor is one. Here is the local solvability check for that converse. At the reference the derivative of the node factor, on gauge parameters zero at the coarse nodes, is minus \(Q'\). On each pillar \(Q'\) is the uniform mean of unitary transports; the center has weight \(n^{-4}\). On the other \(n^4-1\) sites, insert the inverse transported desired value divided by \(1-n^{-4}\). This gives a right inverse while the center stays zero. Thus for \(n\ge3\) that derivative is onto; the finite implicit-function theorem solves the node-factor equation near the reference. For \(k=0\) the plain and straightened data already coincide. The two local critical values consequently agree, and (11.3) is the physical coarse Hessian in relative group coordinates. Completing the square for \(K_{\rm phys}\), and eliminating its gauge term along \(D_U\ker Q'\), also gives directly
\[
              f''(0)=(QK_{\rm phys}^{-1}Q^{\mathsf T})^{-1}-I .
                                                               \tag{11.4}
\]
In this uniform setting there are no outward datum factors.

Put \(\delta=C_L(\alpha_0+\gamma_0)\) in (9.6). On the chosen slice, (10.4) implies
\(\|h_b\|^2\le G_L(\|d_Uh_b\|^2+\|b\|^2)\).
Choose \(G_L\delta\le1/2\). Equations (9.6) and (11.2) then give, with fixed positive \(c_0(L)\),
\[
 \begin{split}
 f''(0)[b,b]&\ge\tfrac12\|d_Uh_b\|^2-G_L\delta\|b\|^2,\\
 \|d_Vb\|^2&\le C'_L\|d_Uh_b\|^2+C''_L\alpha_0^2\|b\|^2,\\
 f''(0)[b,b]&\ge c_0(L)\|d_Vb\|^2
                           -C'''_L(\alpha_0+\gamma_0)\|b\|^2.
 \end{split}                                                   \tag{11.5}
\]
All three follow by substitution; the constants precede the depth and volume.

Finally put \(b=C_Vu\) in the actual next-step plain pivot chart. Its second derivative is (5.4), so its action Hessian is
\[
 f''(0)[b,b]-\langle\omega,h_VD^2q_V(0)[b,b]\rangle .
\]
The multiplier bound (9.2), the finite one-step derivative bounds and the inverse pivot bound in §5 make the absolute value of this last term at most \(C_L\gamma_0\|b\|^2\). Since \(V\) is axial, the gauge Hessian adds exactly \(\|G_Vb\|^2\). The actual one-step estimate (5.3) applies: (8.4) bounds the current plaquette curvature by \(C_L\alpha_0\), which is below its ceiling after the fixed shrinkage. Hence
\[
 \begin{split}
 \langle u,\mathsf A u\rangle
 &\ge c_0(L)\|d_Vb\|^2+\|G_Vb\|^2
                          -C_L(\alpha_0+\gamma_0)\|b\|^2\\
 &\ge\left\{{\min(c_0(L),1)\over A'_L}
                      -C_L(\alpha_0+\gamma_0)\right\}\|b\|^2\\
 &\ge {\min(c_0(L),1)\over2A'_L}\|u\|^2 .
 \end{split}
\]
This proves (11.1), with the multiplier and pivot-curvature terms of the actual operator included. Conditioning is exactly §2.

## 12. Its complex half-gap at nearby physical critical pairs

**Proved.** Keep the uniform, node-free geometry of §11 and its real critical reference \(U,J_U\). Let \(W=e^{i\eta E}U\) be a complex critical field for its corresponding straightened datum, and let \(J_W\) be its physical current. Suppose
\[
 \|E\|_\infty+\|\nabla_UE\|_\infty+
                         \|J_W-J_U\|_\infty\le\rho .          \tag{12.1}
\]
There is a fixed \(\rho_L>0\), independent of depth and volume, such that every defining inverse in (3.1) exists at these pairs and
\[
              \operatorname{Re}\langle u,\mathsf A_Wu\rangle_H
                              \ge(c_L/2)\|u\|^2              \tag{12.2}
\]
when \(\rho\le\rho_L\), with \(c_L\) from §11. The hypothesis specifies nearby critical pairs; it does not assert the existence of a critical branch filling a prescribed datum ball. The proof treats the bilinear analytic operators and takes their Hermitian real part only at the end.

Here are uniform estimates for the inverses and the perturbation. Write
\(\|h\|_1^2=\|h\|^2+\|\nabla_Uh\|^2\).
First the real precision in §10 controls this full norm, not just mass. On a torus expansion of the covariant differences gives
\[
 \|\nabla_U h\|^2
 \le C\{\|d_Uh\|^2+\|D_U^*h\|^2+\alpha_0\|h\|^2\}.
                                                               \tag{12.3}
\]
To check the error, expand the curl square and the divergence square. Equal-direction products cancel the component-gradient terms; every remaining pair is a commutator of two translated covariant differences. The two orders of translation differ by an adjoint plaquette holonomy, of norm \(C\alpha_0\eta^2\); the two difference denominators cancel \(\eta^2\). Summing the finitely many orientations bounds their pairing by \(C\alpha_0\|h\|^2\). Replacing the antisymmetrized component derivative by the transported four-leg \(d_U\) changes its coefficients by \(C\eta\alpha_0\), which is covered by the same bound after Cauchy. Applying this calculation to \(h=D_Uz\), where the exterior derivative is a plaquette commutator acting on \(z\), gives
\[
 \|\nabla_UD_Uz\|
              \le C(\|\Delta_Uz\|+\|z\|),\qquad
 \Delta_U=D_U^*D_U .                                        \tag{12.4}
\]
Indeed the commutator is bounded by \(C\alpha_0\|z\|\), and
\(\|D_Uz\|^2\le\|z\|\|\Delta_Uz\|\).
For \(z\in\ker Q'\), the scalar Poincare estimate further gives
\(\|z\|+\|D_Uz\|\le C_L\|\Delta_Uz\|\).

In the decomposition \(h=h_0+D_Uz\) used in §4, the graph estimate bounds \(\|h_0\|_1^2\) by \(C_L\widetilde\beta[h,h]\), and
\(\|\Delta_Uz\|\le\|RD_U^*h\|+\|D_U^*h_0\|\).
Equation (12.4) therefore proves
\[
 c'_L\|h\|_1^2\le\langle h,K_{\rm phys}h\rangle
                                    \le C'_L\|h\|_1^2.       \tag{12.5}
\]
The upper bound follows directly from (9.6), bounded row density and \(\|R\|\le1\).

The coefficient estimates used next have constants uniform in depth. For clarity, they follow from Cauchy's formula applied *before* inverting any propagator. Let \(E_0=E/\rho\) when \(\rho>0\) and vary the reference as \(e^{i\eta zE_0}U\). Choose a fixed complex \(z\)-disc inside the regular local-potential ceiling, leaving room around the real center. The argument (8.4)–(8.7) holds on that whole disc. Cauchy's integral formula, applied entrywise and then summed absolutely, gives
\[
 \|Q_W-Q_U\|_{2\to2}+\|r_W-r_U\|_{2\to2}\le C_L\rho,
\]
and gives \(C_L\rho\,\xi(\eta/\xi)^4\) for the difference of the second-jet leg sums in (8.3). The physical density factors are those already checked there. The same argument on the bounded raw output logarithm \(a_k\), or on the plain reference \(\log\mathcal M^k(e^{i\eta zE_0}U)\) in each local gauge, gives
\[
                 \|V_W-V_U\|_{\rm local}\le C_L\rho.         \tag{12.6}
\]
For the plain reference this uses the reference recursion (8.4), not a product of plain derivative row norms. Local frames remain fixed at \(U\) while \(z\) varies.

We need row lifts in both energy and absolute-sum norms. Use the smooth profiles of §10 in fixed real local gauges, calling the resulting seed map \(E^0\). On this uniform row grid there is no next-level leakage. The coefficient comparison gives \(Q_UE^0=1+D_U^{\rm row}\), with row and column sums of the error at most \(C_L\alpha_0<1/4\). The seeds have
\(\|E^0b\|_1\le C_L\|b\|_2\) and
\(\|E^0b\|_{1,{\rm abs}}\le C_L\|b\|_{1,{\rm abs}}\),
where the fine absolute norm includes volume \(\eta^4\).
Undoing a local gauge changes the covariant derivative into the ordinary seed derivative plus a bounded local potential, so it preserves the energy bound up to a fixed factor. The same error estimate and (12.6) hold at \(W\). Hence
\[
 E_W=E^0(Q_WE^0)^{-1},\quad Q_WE_W=1,\quad
 \|E_W\|_{2\to H^1}+\|E_W\|_{\ell^1\to L^1}\le C_L,
 \quad
 \|E_W-E_U\|_{2\to H^1}+
       \|E_W-E_U\|_{\ell^1\to L^1}\le C_L\rho .               \tag{12.7}
\]
These follow by the convergent row/column Neumann series and the inverse difference identity. They do not use a Green function. Since both currents are stationary,
\(\omega_W=E_W^{\mathsf T}J_W\) and
\(\omega_U=E_U^{\mathsf T}J_U\).
The absolute-sum bound in (12.7) gives
\[
                         \|\omega_W-\omega_U\|_\infty
                                      \le C_L\rho.           \tag{12.8}
\]
Combining this with the second-jet Cauchy bound gives a \(C_L\rho\) mass-form difference for the constraint correction. The Wilson difference has norm at most \(C_L\rho\) as a form on \(H^1\): its leading curls differ by \(C_L\rho\) times the field, and its remaining plaquette coefficients differ by \(C_L\rho\eta^2\), using (12.1). Consequently
\[
                     |\beta_W[h,v]-\beta_U[h,v]|
                             \le C_L\rho\|h\|_1\|v\|_1.      \tag{12.9}
\]

We next check the scalar Gram inverse defining the actual \(R\). Put \(r=Q'\), \(M=\Delta+r^{\mathsf T}r\), \(G'=M^{-1}\). The scalar variance proof in §10, now retaining the mean term, gives
\[
                  M_U\asymp 1+\nabla_U^*\nabla_U .
\]
The coefficient changes of \(D\) and \(r\) are \(O(\rho)\) in this form norm, so a normalized Neumann series gives \(G'_W\) and bounds \(G'_W-G'_U\) by \(C_L\rho\) from \(H^{-1}\) to \(H^1\). It also gives the same bound on \(L^2\).

The real site Gram \(B_U=r_UG_U'^2r_U^{\mathsf T}\) has a uniform lower bound. Construct a site lift \(E_s\) by a tensor product of smooth bumps supported in the interior of each unit pillar, with mean one. Choose a twice continuously differentiable bump, so its first two discrete differences are bounded in physical units; on the finitely many spacings with fewer than 128 sites use a center-supported lift and enlarge the fixed bound. Normalize its actual \(r_U\) response by its \(3\)-by-\(3\) mean matrix, which is within \(C_L\alpha_0\) of the identity. Thus \(r_UE_s=1\). The bounds \(|A|,|\nabla A|\le C_L\alpha_0\) in that pillar give
\(\|M_UE_s b\|\le C_L\|b\|\):
two differences of the seed are bounded, the connection terms read only \(A,\nabla A\), and \(\|r_U^{\mathsf T}b\|=\|b\|\).
Therefore
\[
 \|b\|^2
 =\langle G'_Ur_U^{\mathsf T}b,M_UE_sb\rangle
 \le C_L\|G'_Ur_U^{\mathsf T}b\|\|b\|.
\]
This proves \(B_U\ge C_L^{-2}I\). Its upper bound follows from bounded \(G'_U,r_U\). The preceding \(L^2\) difference estimates give
\(\|B_W-B_U\|\le C_L\rho\), so \(B_W^{-1}\) exists uniformly for a fixed small \(\rho\). The exact formula
\[
 R_W=1-G'_Wr_W^{\mathsf T}B_W^{-1}r_WG'_W
\]
now proves \(\|R_W\|\le C_L\) and \(\|R_W-R_U\|\le C_L\rho\). This verifies the defining Gram inverse, rather than assuming that a complex orthogonal projection is positive.

We also require the regularity of \(S=1-DG'RD^{\mathsf T}\). Equation (12.4) and \(\Delta_UG'_Uf=f-r_U^{\mathsf T}r_UG'_Uf\) bound \(G'_U\) from \(L^2\) to the norm
\(\|z\|+\|D_Uz\|+\|\nabla_UD_Uz\|\).
The operator \(\Delta_W-\Delta_U\) maps \(H^1\) to \(L^2\) with norm \(C_L\rho\): expanding \(D_W^*D_W-D_U^*D_U\) leaves a multiplication by \(E\) times one difference and a multiplication by \(\nabla_UE\), plus its bounded quadratic term. The resolvent identity and the just-proved scalar inverse bounds therefore give the same second-derivative bound for \(G'_W\), and \(C_L\rho\) for its difference. It follows that
\[
                  \|S_W\|_{H^1\to H^1}\le C_L,\qquad
                  \|S_W-S_U\|_{H^1\to H^1}\le C_L\rho.        \tag{12.10}
\]

At these complex critical pairs the gauge-null proof (10.5) is an algebraic holomorphic identity: the local coarse-parameter map still has full rank, and the bilinear Gram at its base is \(r_Wr_W^{\mathsf T}=1\). Thus \(S_W^{\mathsf T}\beta_WS_W=\beta_W\). Define temporarily
\[
 K_W=\beta_W+D_WR_WD_W^{\mathsf T}+Q_W^{\mathsf T}Q_W.
\]
Equations (12.5), (12.9) and the estimates for \(R,D,Q\) give
\[
       \|K_U^{-1/2}(K_W-K_U)K_U^{-1/2}\|\le C_L\rho.          \tag{12.11}
\]
In particular \(K_W\) is invertible.

There is no circular definition here. Let \(N_W=D^2q_W[\omega_W]\). The actual first two fine precisions are, at a physical current,
\[
 G_{0,W}^{-1}=K_W+N_W,\qquad
 G_W^{-1}=K_W+S_W^{\mathsf T}N_WS_W.
\]
These identities follow respectively from \(F_W''=\beta_W+N_W\) and the defining gauge identity \(\Delta^{\rm W}-\Delta'_\pi[J_W]=S_W^{\mathsf T}F_W''S_W\). By (8.10), (12.8), (12.10), the extra terms are bounded by \(C_L(\gamma_0+\rho)\) in the graph form. Taking the original current ceiling small and then \(\rho\) small makes both inverses exist. Their row Gram inverses exist by the same comparison argument in the next paragraph, using (12.7). Thus their defining \(H_W\) is a right inverse and \(H_W^{\mathsf T}J_W=\omega_W\). Substitution in the defining second variant gives \(G_{1,W}^{-1}=K_W\), as asserted.

Here is the promised row-Gram and Schur comparison with a varying constraint. Put
\[
 T=1+E_W(Q_U-Q_W),\qquad Q_WT=Q_U.
\]
Equation (12.7) gives \(\|T-1\|_{H^1\to H^1}\le C_L\rho\), so \(T\) is invertible. By (12.5) and (12.11), \(T^{\mathsf T}K_WT\) differs from \(K_U\) by relative form norm at most \(C_L\rho\). Apply §7 with the now fixed \(Q_U\). It proves the existence of the actual row Gram inverse and
\[
 \|S_{1,W}-S_{1,U}\|\le C_L\rho,\qquad
 S_{1,W}=(Q_WK_W^{-1}Q_W^{\mathsf T})^{-1}.                  \tag{12.12}
\]
For the absolute bound, the real Schur form has \(S_{1,U}\le C_LI\): test its variational minimum with \(E_Ub\) and use (12.5), (12.7). The same argument, starting from the corresponding real positive first precision, proves the earlier row-Gram assertion for \(G_W\). All transposes here are bilinear; §7 supplies the norm control.

Finally \(H_{1,W}^{\mathsf T}J_W=\omega_W\). The one-step functions of \(V_W\)—the actual pivot elimination, its inverse pivot blocks, the quadratic gauge term and the plain constraint's quadratic term—are the finite analytic functions proved in §5. Equations (12.6), (12.8) bound their changes by \(C_L\rho\), with fixed row and column overlap. Equation (12.12) bounds the only nonlocal coarse factor. Inserting these estimates in the literal expression (3.1) gives
\[
                         \|\mathsf A_W-\mathsf A_U\|
                                      \le C_L\rho .
\]
Choose \(\rho_L\) within all the preceding inverse radii and below \(c_L/(2C_L)\). The real estimate (11.1) then gives (12.2), and (2.1) gives every coordinate conditioning. This completes the complex extension for the stated physical critical-pair subcase.

## 13. Current checkpoint at the pinned sources

The hand derivations close real A2 on uniform, node-free tori at physical critical backgrounds, at every previous depth, and its complex half-gap for the nearby physical critical pairs specified in (12.1). Every coordinate conditioning preserves these bounds. They also close the actual constraint's second-jet estimate and the on-shell multiplier estimate for separated layers. The explicit regular constant-flux family (6.1) is covered by the real theorem; the direct neutral calculation has the broader complex statement in §7. These are research derivations, without a new independent gate or audit.

The session budget is exhausted. Full A2 is neither proved nor refuted: arbitrary separated layers and seam/node conditions, and the independent-current continuation, remain outside §§11–12. The next attack is the weighted version of (10.4) for the actual pruned rows and boundary gauge, retaining outward datum jets, followed by a bound on \(H[J]^{\mathsf T}J\) without physical stationarity. No explicit configuration refuting A2 was found.

STOPPED
