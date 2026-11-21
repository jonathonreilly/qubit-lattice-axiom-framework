# Repo search

**GUIDE.** Row 1147, checkout `1274390c6`. The target-specific prior inventory is absent. The lead's 8 November search covered main and PRs 10114, 10133, 10134 and 10141. It concerned thirteen ultraviolet obligations. Its gap supplement identifies the soft-kernel route on 10114/10133 and the hard-route snapshots on 10134/10141. I checked the transfer comparison on PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 73–92, 119–149 and 315–339. It gives a local loop test and a contraction for bare coupling at most \(1/32\). I also searched the YM source paths on refreshed main `8b11ae2bb9` and the four PR refs for the cylinder criterion. Main's finite-clock Villain note of 14 September, lines 4 and 79–94, uses an abelian model. PR 10141's `research/ym4d/library/fp1.md`, lines 302–314, bounds a single-scale gauge lift. The registry's W at line 892 is the Wightman reconstruction node. The infrared cylinder criterion is row 1145's open conclusion, assigned here by row 1147.

## Target and result

**GUIDE.** The question is the strict inequality in row 1145, §10, for some fixed \(L\) on row 720's grid. Put \(\beta=\beta_j,\ n=L/a_j,\ N=n^3,\ T=n/2\). Scalar factors exponential in the time period cancel from \(J=2\log Z_T-\log Z_{2T}\). Row 1145, §§7, 9–11, gives \(J(s_0)=o(1)\) and the exact response to the common spatial coupling. Row 1146 confirms both facts. Its corrections identify (APR) as a hypothesis and locate the proof of the Bessel-ratio bound at row 1145, line 394. Row 1143, §§6–8, gives the fixed-box expansion and a coercive comparison on open boxes. I use its distinction between flat connections on open and periodic boxes. Row 720, Theorem ZD-c, supplies the consumer. The council synthesis, §§2–4, and the route table in `parts/gap.md` record the failures of absolute surface bounds, twist-only estimates and uniform conditioning on cell boundaries.

**GUIDE.** Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the transfer representation and the conditional first-passage trajectory. Credit Tadeusz Bałaban for the renormalization group. The indexed outline at `31a47c543775`, lines 2315–2335 and 20781–20801, gives (GL8) and (RF25). CA-I lines 56419–56455 state the hypotheses of first passage. The outline at lines 588–599, 9568–9577 and 31871–31882 distinguishes a physical spectral gap from polynomial decay and constrained covariance estimates. CA-I lines 2698–2712 explicitly exclude a mass gap from Theorem 0. Along the supplied trajectory \(\beta\to\infty,\ \beta=O(\log n)\). All proof steps below are analytic. “PROVED” describes a hand argument in this research note and grants no repository status. [Pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2698-L2712)

**OPEN.** Does the signed response stay below \(\log(1+1/1650)\) when the last spatial couplings reach \(\beta\)? Equation (30) leaves only spatial plaquettes crossing a single box face, during a time interval whose physical duration tends to zero. The modified cylinder satisfies the thermal seed with a positive coupling on every plaquette. How much restoring those last couplings changes the signed free energy remains open.

## 1. An open spatial box at isotropic coupling

**GUIDE.** The earlier block-product example C8 in `gap-face-exercise-fable.md`, §3.1, disconnects four-dimensional blocks. Row 910, `gap-cutth-max.md`, Lemma J, identifies the thermal cost of joining two free boxes. Here time stays periodic and every temporal plaquette stays on. A single spatial box can propagate an excitation through the entire time cylinder. We need an estimate uniform as the temporal coupling diverges.

**PROVED (spatial gauge estimate).** Let \(Q\) be an open rectangular spatial box with side lengths at most \(b\), \(b\ge2\), and \(A(U)=\sum_{p\subset Q}a(U_p)\), \(a(u)=1-\tfrac12\operatorname{tr}u=|1-u|^2/2\). Norms are quaternion lengths. There is a vertex gauge such that
\[
                   \sum_{e\subset Q}|1-U_e|^2\le C b^2 A(U).                 \tag{1}
\]
Use the open comb of rows 1028 and 1143, choosing its first plane as follows. If the first side has \(b_1\) vertices, choose \(x_1=r\) with sum of the \(23\)-plaquette actions there at most \(A/b_1\). Fix to one all 1-links, all 2-links in that plane, and all 3-links on its line \(x_2=0\). These links form a spanning tree. A 2-link is compared to its copy on the plane by a chain of \(12\)-plaquettes. For a 3-link first move to the plane using \(13\)-plaquettes, then to the line using \(23\)-plaquettes. Each step compares two parallel links with the other two links fixed to one. Either direction of travel gives the same norm bound. The chains have length at most \(2b\). A \(1i\)-plaquette occurs in at most \(b_1\) chains. A selected-plane \(23\)-plaquette occurs in at most \(b_1 b\) chains. Square by Cauchy–Schwarz, sum the chains, and use the choice of plane. This gives (1). Planes of thickness one cause no difficulty, since chains of length zero have zero cost.

**PROVED (a uniform open-box estimate).** Let \(E,V\) count the edges and vertices of \(Q\), let \(d=E-V+1\), and suppose \(E\ge1,\ \beta\ge1,\ 0<s\le\beta\). The physical transfer with temporal coupling \(\beta\) and all internal spatial couplings \(s\) has a simple top eigenvalue \(\lambda_0\). On its orthogonal complement,
\[
 1-\lambda_1/\lambda_0\ \ge\
       \exp[-C E(1+b^2\beta/s)].                                            \tag{2}
\]
The constant is absolute. In particular at \(s=\beta\) the right side is independent of \(\beta\).

**PROVED (normalization and localization).** Write \(c_\beta(u)=e^{-\beta a(u)}/I(\beta)\), where \(I\) is row 1143's one-link integral. Its convolution has norm one and is positive by the Wilson character expansion. The Haar angle density is \(2\sin^2 r/\pi\). The bounds \(2r^2/\pi^2\le1-\cos r\le r^2/2\) and integration on \(r\le\beta^{-1/2}\) give \(c\beta^{-3/2}\le I(\beta)\le C\beta^{-3/2}\). A ball of quaternion radius \(c_0/\sqrt\beta\) has Haar mass at least \(c_1\beta^{-3/2}\) for fixed small \(c_0>0\). In position coordinates the projected transfer is
\[
 K(U,Y)=M(U)M(Y)\int\prod_{e=(v,w)}
    c_\beta\!\left(U_e(g_vY_eg_w^{-1})^{-1}\right)\prod_v dg_v,\qquad
 M=e^{-sA/2}.                                                               \tag{3}
\]
This is the symmetric placement of the two magnetic factors in (GL8). Its continuous kernel is strictly positive, its spectrum is nonnegative, and its norm is at most one. Top simplicity follows by applying the Rayleigh principle to the absolute value of an eigenfunction, since a sign change on two sets of positive Haar measure gives strict improvement. A nonnegative top eigenfunction is strictly positive by (3), excluding an orthogonal eigenfunction of one sign. Denote it by \(\psi\), with \(\|\psi\|_2=1\).

**PROVED.** Gauge the tree links of both configurations to one along the same tree. Bound the \(d\) chord factors by \(C\beta^{3/2}\), then integrate the normalized tree factors from the leaves. Thus \(K(U,U)\le(C\beta^{3/2})^d\). There is also a lower bound \(\lambda_0\ge e^{-C_0E}\). Test the normalized indicator of the set where, after fixing one tree, all chords have distance at most \(c_0/\sqrt\beta\) from one. Its Haar measure is at least \((c_1\beta^{-3/2})^d\), by independence conditional on the tree transports. On a pair of configurations in this set each magnetic factor is at least \(e^{-CE}\), since the number of plaquettes is at most \(2E\). In (3) leave one vertex gauge \(g_*\) unrestricted and restrict every other gauge to a ball of radius \(c_0/\sqrt\beta\) around it. Conjugation by \(g_*\) preserves distances from one. Every electric factor is at least \(c\beta^{3/2}\), and the restrictions have mass at least \((c_1\beta^{-3/2})^{V-1}\). The Rayleigh quotient gives the assertion since \(E-(V-1)=d\).

**PROVED.** Set \(h=2C_0E+2\log 8\) and \(D=\{sA\le h\}\). For a pair in \(D\), make separate gauge choices using (1), allowed by the independent gauge invariance of (3). With the same restricted vertex gauges as above, the triangle inequality gives a total electric action at most \(C(b^2h/s+E/\beta)\). Thus throughout \(D\times D\),
\[
 K(U,Y)\ge \beta^{3d/2}\exp[-C(E+h+\beta b^2h/s)]
           \ge \epsilon\,\lambda_0\psi(U)\psi(Y),\qquad
 \epsilon=\exp[-C' E(1+b^2\beta/s)] .
\]
For the second inequality use \(\lambda_0\psi(U)^2\le K(U,U)\). Indeed \(K-\lambda_0|\psi\rangle\langle\psi|\) is a positive operator with continuous kernel. Testing on normalized local averages shrinking to \(U\) makes its diagonal nonnegative. Also \(\|1_{D^c}K\|\le e^{-h/2}\) by the left factor \(M\) in (3). Every unit eigenfunction \(\phi\) with \(\lambda\ge\lambda_0/2\), including \(\psi\), therefore has \(\|1_{D^c}\phi\|\le1/4\).

**PROVED.** For a real such \(\phi\perp\psi\), write \(f=\phi/\psi\), \(d\mu=\psi^2dU\). The eigenvalue equation and symmetry give
\[
 1-\lambda/\lambda_0
 =\frac{1}{2\lambda_0}\int K(U,Y)\psi(U)\psi(Y)(f(U)-f(Y))^2\,dU\,dY.
\]
Keeping \(D\times D\) gives at least \(\epsilon[\mu(D)\int_D f^2d\mu-(\int_D f\,d\mu)^2]\). Each of the first two factors is at least \(15/16\). The last integral in absolute value is at most \(1/16\) by orthogonality and the two tail bounds. Eigenvalues below \(\lambda_0/2\) already have deficit at least \(1/2\). Absorbing the fixed factor proves (2). In this argument the cost of the good-set minorization may be much smaller than the tail norm. The Dirichlet form avoids subtracting that tail norm from the minorization.

## 2. A time-independent array of open boxes

**PROVED.** Write \(\widehat K=M C_\beta^{\otimes E}M\) before vertex projection, using a hat also on a transfer on a single free link. For a spatial box of maximum side \(b\) at \(s=\beta\),
\[
 \frac{\widehat\lambda_1}{\lambda_0}\le1-\delta,\qquad
 \delta=\min\{e^{-C b^5},\,c/(1+\beta)\},\qquad
 \operatorname{Tr}(\widehat K/\lambda_0)\le
                 \exp[C b^3\log(2+\beta)].                                \tag{4}
\]
The strictly positive top eigenfunction is vertex invariant by simplicity. In the invariant subspace use (2). In the other subspaces use row 1145, (16)–(18). Its proof applies also to an open graph. Temporal links at one vertex have conditional one-link parameter at most \(6\beta\), the maximal spatial degree is six, and seven colors still suffice. Conditioning on spatial links gives independent temporal layers. For a nontrivial vertex representation of weight \(w=\sum_v(d_v-1)\), the temporal holonomy coefficient therefore has norm at most \(\exp[-kw/(7(1+6\beta))]\) at period \(k\). Taking the character coefficient of the gauge-twisted trace and then \(k\)-th roots gives \(\|\widehat K_\pi\|/\lambda_0\le\exp[-1/(7(1+6\beta))]\). This uses precisely the local-charge estimate of row 1145. For the trace in (4) use \(\lambda_0\ge e^{-C_0E}\) and integrate the diagonal \(\widehat K(U,U)\le(C\beta^{3/2})^E\). On a single free link \(\lambda_0=1\) and the same estimates follow from its one-link multipliers.

**PROVED (cold boxes on the physical sequence).** Partition each spatial circle into consecutive intervals of lengths \(b\) or \(b+1\), where \(b^2\le n/2\). This is possible by distributing the remainder among \(\lfloor n/b\rfloor\) intervals. Let \(\Sigma\) contain the spatial plaquettes whose four vertices do not lie in one resulting box. There are at most \(6n^3/b\) such plaquettes per slice. In each of its two directions a plaquette crosses a boundary for at most \(\lfloor n/b\rfloor\) choices of its base coordinate. Let the spatial couplings be \(\beta\) off \(\Sigma\) and zero on \(\Sigma\), keeping all temporal couplings at \(\beta\). Before vertex projection the transfer factors into one \(\widehat K\) per box and one electric convolution per crossing link. The product vacuum is invariant under the full gauge group of the original torus. The normalized physical thermal trace is bounded above by the unprojected trace, and below by one from that vacuum. Positivity of the spectrum and (4) give
\[
 0\le J_{\rm cut}\le
  C n^3 \exp[C(b+1)^3\log(2+\beta)-(T-1)\delta_{b+1}],                  \tag{5}
\]
where \(\delta_{b+1}\) denotes (4) with that side bound. Indeed the excited trace of each factor at time \(T\) is at most its normalized one-step trace times \((1-\delta)^{T-1}\). Take logarithms of the product and use \(\log(1+x)\le x\) and \(J\le 2\log\operatorname{Tr}(K/\lambda_0)^T\).

**PROVED.** One can take \(b=\lfloor\gamma(\log n)^{1/5}\rfloor\) with fixed sufficiently small \(\gamma>0\). Then \(e^{-C(b+1)^5}\ge n^{-1/4}\) eventually, and \(c/(1+\beta)\ge n^{-1/4}\) along the trajectory. The right side of (5) tends to zero. Every fixed physical size in (24) works in this modified ensemble. Its action at every time agrees with the isotropic spatial action on a fraction at least \(1-2/b\) of the spatial plaquettes. C8 of `gap-face-exercise-fable.md` already observes the danger of interpreting such a fraction. Estimate (5) controls the full long temporal trace with all temporal bonds present.

**PROVED (the remaining spatial integral).** Restore a common coupling \(u\) on \(\Sigma\), with the other couplings fixed as in (5). For \(k=T,2T\) write \(\bar w_{k,\Sigma}(u)\) for the mean normalized trace over the \(k|\Sigma|\) affected plaquettes. Then the original left side of (24) equals
\[
 \limsup_j 2T|\Sigma|\int_0^\beta
       [\bar w_{T,\Sigma}(u)-\bar w_{2T,\Sigma}(u)]\,du .                 \tag{6}
\]
Differentiation of the finite positive partition integrals gives the formula with endpoint difference \(J(\beta)-J_{\rm cut}\) before the limsup. The term \(1\) in \(a=1-w\) cancels. Equation (5) and \(J(s_0)=o(1)\) from row 1145 identify the two limsups. Row 910's joining identity motivates retaining this signed subtraction. No monotonicity in the set of retained plaquettes was used.

## 3. Restricting (6) to a short interval in time

**PROVED.** There is a second localization. Choose any \(0<\eta<1\). Decrease the fixed \(\gamma>0\) in §2 depending on \(\eta\), put \(b=\lfloor\gamma(\log n)^{1/5}\rfloor\), and take \(h=\lceil n^\eta\rceil\). Set the coupling to zero on \(\Sigma\) for just \(h\) consecutive magnetic layers in one period of length \(T\). All other plaquettes have coupling \(\beta\). Use two repeats of this schedule at length \(2T\). For this pair of cylinders,
\[
                             J_{\rm hole}=o(1).                              \tag{7}
\]
The assertion holds with arbitrary nonnegative magnetic weights on the other layers, provided the same schedule is repeated and the partition functions are finite and positive. For these general weights the conclusion is the absolute bound \(|J_{\rm hole}|=o(1)\).

**PROVED (uniform kernel estimate).** Take one unprojected box factor \(G=\widehat K\) from (4). The same bounds hold for \(G=C_\beta\) on a single free link, with its one-link Haar measure. Write \(\lambda,\psi\) for its normalized top data, with \(\|\psi\|_2=1\). The full position kernel before projection has upper bound \(U=(C\beta^{3/2})^E\) and lower bound \(l=\beta^{3E/2}e^{-C(1+\beta)E}\), from \(a\le2\) in all the weights. Choose constants so \(U\ge1\). The Perron equation gives \(\sup\psi/\inf\psi\le U/l\). Since Haar mass is one, \(\sup\psi\ge1\) and \(\inf\psi\ge l/U\). Also \(\lambda\ge e^{-C_0E}\). For integer \(r\ge2\), apply the spectral norm bound to the middle \(r-2\) operators between the two kernel rows \(G(x,\cdot),G(\cdot,y)\). Each row has \(L^2\) norm at most \(U\). This proves, pointwise,
\[
 \left|\frac{G^r(x,y)}{\lambda^r\psi(x)\psi(y)}-1\right|
 \le \exp[C(1+\beta)(b+1)^3-(r-2)\delta_{b+1}].                           \tag{8}
\]
Taking \(C\) larger covers the single free link as well.

**PROVED.** In an exact transfer word one may assign magnetic weights to whole layers by using alternating convolution and multiplication. Equivalently use a half-electric factor at each end of each layer as in (GL8). To keep the pointwise comparison (8) in position coordinates, reserve \(r=h-1\) full cut steps between two cut endpoints, leaving their two outside half magnetic weights in the rest of the word. In more detail, on a period with site weights \(M_i^2\) use the edge kernel \(M_i C_\beta^{\otimes 3N} M_{i+1}\), with indices periodic. The \(h-1\) edges between the \(h\) cut layers have the cut transfer. All other edges form a nonnegative rest kernel \(R\). One vertex projection in the trace enforces Gauss' law. For Wilson weights it commutes with each edge operator and is idempotent. Equivalently include the vertex average in \(R\) for each period. This formulation also allows nonnegative rest kernels with their projections explicitly inserted.

**PROVED.** Choose \(\gamma\) so \(C(b+1)^5\le(\eta/3)\log n\) eventually. Then \(\delta_{b+1}\ge n^{-\eta/3}\) for large \(j\), using \(\beta=O(\log n)\). The right side of (8) at \(r=h-1\) is \(o(n^{-4})\). Multiply the pointwise bounds for at most \(4n^3\) factors. The complete cut segment lies pointwise between \(1-\varepsilon_j\) and \(1+\varepsilon_j\) times its vacuum kernel \(\Lambda^r\Psi(x)\Psi(y)\), with \(\varepsilon_j\to0\). For one period integrate this inequality against the transposed \(R\). For two periods insert it twice, keeping all other kernels nonnegative. The vacuum expressions are \(c_R=\Lambda^r\langle\Psi,R\Psi\rangle\) and \(c_R^2\). Their ratio cancels exactly. This bounds \(|J_{\rm hole}|\) by \(2\log[(1+\varepsilon_j)/(1-\varepsilon_j)]\), proving (7) whenever \(c_R>0\).

**PROVED (the short remaining integral).** Let \(D_j\) now denote the \(|D_j|=h|\Sigma|\) spacetime plaquettes just omitted in the first cylinder. Restore the common coupling \(u\) on this set and on its two copies in the longer cylinder. Write \(w_{1,D}(u),w_{2,D}(u)\) for their respective normalized-trace means, averaged over the full affected set in each cylinder. Then (24) is equivalent to
\[
 \limsup_j\,2|D_j|\int_0^{\beta_j}
                [w_{1,D}(u)-w_{2,D}(u)]\,du<\log(1+1/1650)                 \tag{9}
\]
at one fixed grid size. This follows from the same finite differentiation used for (6), now using (7). All temporal plaquettes have their original coupling, even in the short interval. The affected spatial fraction in any layer is at most \(2/b\), and the affected physical duration is \(a_j h\to0\). Coupling restoration still acts on a growing number of plaquettes. Neither small fraction implies an estimate for (9).

## 4. A quantitative obstruction to restoring the omitted plaquettes

**PROVED (plaquette covariance).** On a four-dimensional Wilson \(SU(2)\) torus with sides at least three, let the real plaquette couplings \(t_p\) obey \(|t_p|\le B\). The density is proportional to \(\exp(\sum_p t_p w_p)\). For every real array \(v_p\),
\[
 \operatorname{Var}_{t}\!\left(\sum_p v_p w_p\right)
                  \ge \frac{c}{(1+B)^2}\sum_p v_p^2 .                     \tag{10}
\]
Here \(c>0\) is absolute. The power of \(1+B\) is optimal for this class. This is a lower bound on fluctuations in either actual cylinder of (24), including its isotropic endpoint.

**PROVED (two links of one plaquette).** Choose two opposite links \(x,y\) of a marked plaquette \(p\), viewed as vectors in \(S^3\subset\mathbb R^4\). Given all other links, \(w_p=x^t O y\) for an orthogonal real \(O\). Quaternion multiplication by a unit element and quaternion conjugation are orthogonal maps. No other elementary plaquette contains both links. Thus the pair density is proportional to
\[
       \exp(a\cdot x+d\cdot y+t_p x^t O y),\qquad |a|,|d|\le 5B.
\]
The observable restricted to this pair is a constant plus two linear terms and \(v_p x^t O y\). Introduce an auxiliary standard normal \(z\) in four real dimensions. The Gaussian moment identity represents the interaction by multiplying its measure by
\[
  \exp[-|t_p|+\sqrt{|t_p|}\,z\cdot(x+\operatorname{sgn}(t_p)O y)].
\]
Integrating \(z\) recovers \(e^{t_p x^t O y}\), including \(t_p=0\). Given \(z\), the two links are independent with linear fields. Given \(x,y\), \(z\) is a translated standard normal with translation of length at most \(2\sqrt B\). Consequently the event \(|z|\le 2\sqrt B+4\) has conditional and unconditional probability bounded below by the standard normal mass of the radius-four ball. On that event the lengths of both linear fields are at most \(C(1+B)\).

**PROVED.** A link with density proportional to \(e^{H\cdot x}\) has covariance at least \(c(1+|H|)^{-1}\) on the three-dimensional subspace perpendicular to \(H\). At zero field any three-dimensional subspace works. Rotational invariance gives tangential variance \(\tfrac13\mathbb E\sin^2 r\), where \(r\) is the angle to \(H\). For \(|H|\le1\) the density is comparable to Haar. For \(|H|\ge1\) integrate on \(1/(2\sqrt{|H|})\le r\le1/\sqrt{|H|}\). The density in \(r\), after removing \(e^{|H|}\), is proportional to \(\sin^2 r\,e^{-|H|(1-\cos r)}\). Its integral is at most \(C|H|^{-3/2}\), and this interval contributes at least \(c|H|^{-5/2}\) to the integral with the extra \(\sin^2 r\). For independent \(x,y\), the component \(v_p(x-\mathbb Ex)^tO(y-\mathbb Ey)\) is orthogonal in \(L^2\) to constants and to all functions of either single variable. Its variance is \(v_p^2\operatorname{tr}(C_x O C_y O^t)\), where \(C_x,C_y\) are the two covariances. The two tangential three-planes, after transporting the second by \(O\), intersect in at least two dimensions. The trace of the product of their orthogonal projections is at least two. Positivity of covariance and monotonicity of the trace pairing on positive matrices give a variance at least \(c v_p^2/(1+B)^2\) on the stated event. Average over \(z\) using total variance.

**PROVED.** Choose such a pair for every plaquette in the support of \(v\). Declare two plaquettes in conflict when some elementary action plaquette touches a chosen link from each. This includes overlapping pairs. Each marked plaquette conflicts with at most \(2\cdot6\cdot4\cdot6\) others. Color greedily and take a color carrying at least \(1/289\) of \(\sum v_p^2\). Conditional on all the other links, the pairs in this color are independent and the observable is a sum of their individual contributions plus a constant. The preceding conditional bound proves (10). For sharpness keep just one nonzero coupling \(B\) and take the corresponding plaquette observable. Its holonomy is tilted Haar, by integrating one of its links. Its variance is at most \(\mathbb E(1-\cos r)^2\le C(1+B)^{-2}\), by the same angle integral with \(r^4\) in the numerator.

**PROVED (cost in each cylinder).** Write \(A(t,t')=\int\sqrt{d\mu_t\,d\mu_{t'}}\) for the Hellinger affinity of the full lattice laws. If both coupling arrays lie in \([-B,B]\), restrict the log partition function to their line segment. Its second derivative is the variance in (10) with \(v=t'-t\). Subtracting the quadratic with this lower curvature and applying midpoint convexity gives
\[
              -\log A(t,t')\ge
                  \frac{c\|t'-t\|_2^2}{8(1+B)^2}.                         \tag{11}
\]
The partition function ratio for this affinity is its value at the midpoint divided by the geometric mean of the endpoints. The same argument holds on a cylinder with the replicated set of couplings, since it is itself a torus. Along (9), the full and cut Gibbs laws thus have affinity at most \(e^{-c'|D_j|}\) in one period and \(e^{-2c'|D_j|}\) in two. Their total variation distances are at least one minus these bounds, since the minimum of two densities is at most their geometric mean.

**PROVED.** In the action convention \(a=1-w\), let \(W=e^{-\beta\sum_{D_j}a(U_p)}\) in the one-period cut law. Since \(0<W\le1\), its affinity with the restored law is \(\mathbb E\sqrt W/\sqrt{\mathbb EW}\ge\sqrt{\mathbb EW}\). Thus \(-\log\mathbb EW\ge c'|D_j|\). Its relative second moment satisfies
\[
          \log\frac{\mathbb EW^2}{(\mathbb EW)^2}\ge c'' |D_j|.
                                                                            \tag{12}
\]
Apply (11) to cut couplings \(0\) and \(2\beta\) on \(D_j\), with midpoint \(\beta\), and use \(\beta\ge1\). The two-period estimate has twice the same lower bound. More generally any route inside \([-C_*\beta,C_*\beta]\) from the cut to the restored array, using consecutive full-law affinities at least \(q>0\), needs at least \(c(C_*,q)\sqrt{|D_j|}\) steps. Indeed (11) bounds the Euclidean length of each increment by \(C(C_*,q)\beta\), while the endpoints are \(\beta\sqrt{|D_j|}\) apart. This applies to arbitrary intermediate spatial profiles.

**OPEN.** Put \(F_i=-\log[Z_{i,\mathrm{full}}/Z_{i,\mathrm{hole}}]\) for \(i=1,2\) repeats of the period, using the action convention above. What (9) needs is the signed upper bound on \(F_2-2F_1\). Each cost is extensive in the number of restored plaquettes by (11). Equation (12) rules out bounded relative second moments for direct reweighting. Neither estimate imposes a sign on \(F_2-2F_1\).

## 5. Keeping every plaquette on a periodic spatial cube

**PROVED (a lower gap bound at weak bare coupling).** Let \(m(b,\beta)=\log(\lambda_0/\lambda_1)\) for the isotropic Wilson transfer on the **periodic** spatial \(b^3\) cube, including all physical flux sectors, \(b\ge3,\ \beta\ge1\). Then
\[
 m(b,\beta)\ \ge\
         \exp[-C(b^8+b^{11/2}\sqrt\beta)] .                              \tag{13}
\]
In particular, at fixed \(b\) the exponent in this lower bound grows only as \(\sqrt\beta\). Row 1143, (7)–(10), gives upper bounds on the flux energies. Here the lower bound uses the connected paths among the three spatial holonomies. The open-box estimate (2) has no such paths to traverse.

**PROVED (constructing the path).** Use the comb representation of row 1143, §1, now for the three spatial directions. Let \(B(H)\) have unit interior links and \(H_i\) on all wrapping links in direction \(i\). Take \(H_i\) to be the wrapping \(i\)-link at transverse coordinate zero in the comb gauge. Then
\[
 D(U,H):=\sum_e |U_e-B(H)_e|^2\le C b^5 A(U),\qquad A(B(H))\le C b^5 A(U).
                                                                            \tag{14}
\]
For an interior link, at most \(2b\) predecessor plaquettes compare it with a tree link, each once within that chain. The squared distance is at most \(Cb A(U)\). Move a wrapping link in at most \(2b\) transverse unit steps to the representative \(H_i\). Each step costs a plaquette distance and the distances of two interior links from one, hence at most \(C\sqrt{b A(U)}\). There are at most \(3b^2\) wrapping links and \(3b^3\) interior links. This proves the first bound. Telescoping each plaquette and counting at most four occurrences of an edge proves the second.

**PROVED.** Join each \(U_e\) to \(B(H)_e\) by a shortest group geodesic. The distance at intermediate points from \(B(H)_e\) is at most \(|U_e-B(H)_e|\). By (14) their total magnetic action is at most \(C b^5 A(U)\). Next shrink each \(H_i\) to a nearest central sign. Write \(H_i=z_i(\cos\theta_i+\nu_i\sin\theta_i)\), \(z_i=\pm1,\ 0\le\theta_i\le\pi/2\), and shrink the angle linearly to zero. The only nontrivial plaquettes of \(B(H)\) are commutators. Their actions are \(2\sin^2\theta_i\sin^2\theta_j|\nu_i\times\nu_j|^2\) by the quaternion identity in row 1143, §2. Each decreases on this path. Finally join the three signs to one through one common circle subgroup. All commutators there are trivial. Each link travels with speed at most an absolute constant when the three pieces have equal time. Concatenating with a reversed path gives the same type of bound for two endpoints. This construction works for independently conjugated endpoints. In a frozen finite subgroup the last continuous paths can be absent. In \(U(1)\) the commuting part has no action cost at all, so this argument would still admit a photon.

**PROVED (integrating a tube of paths).** Set \(E=3b^3,\ V=b^3,\ d=E-V+1,\ H_0=2C_0E+2\log 8\), and \(D=\{\beta A\le H_0\}\). The diagonal upper bound, the vacuum lower bound \(e^{-C_0E}\), and both \(1/4\) eigenfunction tail bounds in §1 hold verbatim on the torus. They used a spanning tree, a plaquette incidence bound, and \(M\le1\). For \(U,Y\in D\), choose comb representatives. In the kernel of the projected \(k\)-step transfer put the single vertex projection at the last endpoint. Leave one \(g_*\) unrestricted. Restrict each other vertex gauge to distance \(c_0/\sqrt\beta\) from \(g_*\). First connect \(U\) to \(g_*Yg_*^{-1}\) by the preceding path. Use its \(k-1\) intermediate time slices. Restrict each intermediate link to a ball of radius \(c_0/\sqrt\beta\) about the prescribed link. The actual endpoint \(g\cdot Y\) differs on each link from the prescribed endpoint by at most \(2c_0/\sqrt\beta\), and has exactly the same magnetic action as \(Y\).

**PROVED.** On these restrictions the sum of the electric exponents over the path is at most \(CE(\beta/k+k)\). This follows by squaring the one-step distances bounded by \(C/k+C/\sqrt\beta\) on each link. The sum of the magnetic exponents is at most \(Ck(b^5 H_0+E)\), by telescoping the four link errors of each plaquette around the prescribed slice. There are \(kE\) normalized electric factors, \((k-1)E\) restricted independent intermediate Haar variables, and \(V-1\) restricted endpoint gauges. The ball estimates in §1 now give
\[
 K^k(U,Y)\ge \beta^{3d/2}\exp[-C(b^3\beta/k+k b^8)] .
\]
Here \(k\ge1\). At \(k=1\) the electric distance estimate and endpoint integration still apply. Since \(\lambda_0\le1\) and \(\lambda_0\psi(U)^2\le(C\beta^{3/2})^d\), the same bound, with the power of \(\beta\) replaced by \(\lambda_0^k\psi(U)\psi(Y)\), follows upon increasing \(C\). Apply the good-set Dirichlet argument of §1 to \(K^k\), using the two tail estimates for the original eigenfunctions of \(K\). This yields \(1-(\lambda_1/\lambda_0)^k\ge c\exp[-C(b^3\beta/k+k b^8)]\) when \(\lambda_1\ge\lambda_0/2\). Take \(k=\max(1,\lceil\sqrt\beta/b^{5/2}\rceil)\) and use \(k m\ge 1-e^{-km}\). The factor \(k^{-1}\) is absorbed by increasing \(C\) in (13). The other case has \(m\ge\log2\).

**PROVED (extent of this continuation).** Suppose \(T_j=L/(2a_j)\) as in (24), but take a periodic spatial cube of side \(b_j=o(\beta_j^{1/11})\) in lattice units. All couplings are isotropic. Then its \(J\) tends to zero. The trace bound in (4) before the box estimate is valid on the torus as well, so the excited trace is at most
\(\exp[C b_j^3\log(2+\beta_j)-(T_j-1)m(b_j,\beta_j)]\).
Equation (13) gives \(m\ge e^{-o(\beta_j)}\), while \(\log T_j\ge c\beta_j\) eventually by first passage. This also works at bounded \(b_j\). The physical spatial side of these cylinders tends to zero. At the required \(b=n\), even the term \(b^8\) alone is larger than \(\log T\), so (13) gives no effective decay at aspect ratio \(T/n=1/2\).

## 6. A signed comparison on the unmodified cylinders

**GUIDE.** Row 1131, `gap-council-prob-astra.md`, uses a two-sheet cover and marks individual plaquette supports. Here the two ways of sewing **entire spatial slices** are summed exactly at each time step. This keeps cancellations between all spatial supports. I use the unprojected temporal-gauge transfer \(F=M C_\beta^{\otimes 3N}M\) at the actual isotropic coupling. Write \(\widehat Z_k=\operatorname{Tr}F^k\). Row 1145, (17), gives \(J-\widehat J=o(1)\) at physical time. The sign calculation below uses its pointwise open-slab extension.

**PROVED (open endpoints).** For spatial configurations \(x,y\), let \((PF^r)(x,y)=\int F^r(x,g\cdot y)\,dg\), with independent Haar gauges at the vertices. Uniformly in \(x,y,g\),
\[
 \left|\frac{F^r(x,g\cdot y)}{(PF^r)(x,y)}-1\right|
 \le \left[1+\sum_{d\ge2}d^2 e^{-r(d-1)/(7(1+6\beta))}\right]^N-1 .       \tag{15}
\]
This strengthens the trace application of (16)–(17) in row 1145 to a kernel statement. In the projected open slab fix the spatial endpoints \(x,y\) and let the \(r\) temporal gauge vectors be \(g_t\). Conditional on all spatial links the \(g_t\) in distinct layers are independent. The seven-color one-link estimate of that row bounds the Fourier transform of their ordered product in \(\otimes_v\pi_{d_v}\) by \(e^{-r\sum_v(d_v-1)/(7(1+6\beta))}\), uniformly in the specified spatial links. Integrating over the interior spatial fields preserves the bound. Its character-dimension sum gives (15) by Fourier inversion because the contribution of a representation of dimension \(D\) has modulus at most \(D^2\) times the transform norm. On the other hand, changing each intermediate spatial slice by the cumulative temporal gauges sends all temporal factors to ordinary convolution and sends the last endpoint to \(g\cdot y\). Thus the density of the ordered gauge product is exactly the ratio in (15), up to inversion convention. This change has unit Haar Jacobian and keeps every magnetic factor. Continuity makes the bound pointwise. At \(r=T-1\) the right side tends to zero.

**PROVED (the sewing identity).** Use two ordered representatives \(x_t,y_t\) at each of \(T\) cyclic time indices. Put
\[
 A_t=F(x_t,x_{t+1})F(y_t,y_{t+1}),\qquad
 B_t=F(x_t,y_{t+1})F(y_t,x_{t+1}).
\]
Let \(\nu\) have density proportional to \(\prod_t (A_t+B_t)/2\) relative to product Haar. It is invariant under arbitrary interchanges of \(x_t,y_t\) at individual slices. In its expansion the \(2^{T-1}\) even choices of crossed edges each integrate to \(\widehat Z_T^2\), and the equally many odd choices to \(\widehat Z_{2T}\). Following the two paths proves this including the wrap. With \(E=3N\) define
\[
 D_t=\sum_{e}(x_{t,e}-y_{t,e})\cdot(x_{t+1,e}-y_{t+1,e}).
\]
The dot is the Euclidean quaternion dot product. All magnetic factors cancel in \(A_t/B_t=e^{\beta D_t}\). Expanding the difference product with the parity signs gives
\[
 \tanh(\widehat J/2)
       =\mathbb E_\nu\prod_t\frac{A_t-B_t}{A_t+B_t}
       =\mathbb E_\nu\prod_t\tanh(\beta D_t/2).                           \tag{16}
\]
No independence of neighboring signs is assumed.

**PROVED (local sewing is nearly deterministic).** On the physical sequence,
\[
               \nu\{\min_t |D_t|< E\}\le C T e^{-cN}                     \tag{17}
\]
for all sufficiently fine cutoffs. To prove it, condition in the preceding expansion on its straight or crossed choices. Relabel the slices to follow the chosen paths near the time edge under consideration. The absolute value of \(D_t\) is unchanged. There are just two sampling laws, two ordinary \(T\)-loops or one ordinary \(2T\)-loop in temporal gauge. First bound the temporal energy of a matched step \((x,x')\) in a \(k\)-loop, \(k=T,2T\). Scalar normalizations may be removed so \(C_\beta(u,v)=e^{-\beta a(uv^{-1})}\) on each link. Write \(F_{\rm bad}\) for the symmetric one-step kernel restricted to \(\sum_e a(x_ex_e'^{-1})>E/4\). Both \(k\)'s are even on the grid. Trace Hölder bounds the probability of this event by
\[
     [\operatorname{Tr}F_{\rm bad}^{\,k}/\operatorname{Tr}F^k]^{1/k}.
\]
Indeed the numerator before Hölder is \(\operatorname{Tr}F_{\rm bad}F^{k-1}\), and the even Schatten power of the self-adjoint restricted kernel has trace \(\operatorname{Tr}F_{\rm bad}^{\,k}\). This is at most \(e^{-k\beta E/4}\) by its position integral. The unrestricted trace is at least \(\exp[-CkE(1+\log\beta)]\) by restricting all spatial links to the radius-\(c_0/\sqrt\beta\) ball. Thus except with probability \(e^{-c\beta E}\) each of the two matched scalar products sums to at least \(3E/4\).

**PROVED.** The two unmatched scalar products have sum of modulus at most \(E/2\) except with probability \(Ce^{-cN}\). Write the two matched pairs as \((x,x')\), \((y,y')\). In two independent loops the joint distribution is invariant under rotating the second pair by the same product vertex gauge \(g\). In a single \(2T\)-loop the other factors in this four-slice marginal are \(F^{T-1}(x',y)F^{T-1}(y',x)\). By (15) one may replace them by their projected kernels at cost at most a fixed factor in either direction for normalized probabilities. The resulting law has the same independent rotation invariance. For fixed fields average
\(\sum_e[x_e\cdot(g\cdot y')_e+x'_e\cdot(g\cdot y)_e]\)
over the independent vertex gauges. Its mean is zero since the endpoints of an edge are distinct and each endpoint gauge is Haar. Changing one gauge changes the sum by at most \(24\). Revealing the \(N\) gauges in order therefore gives a martingale with conditional increment ranges of width at most \(24\). A mean-zero variable in a width-\(w\) interval has exponential moment at \(t\) bounded by \(e^{t^2w^2/8}\), since the second derivative of its log moment is a tilted variance at most \(w^2/4\). Iterate and optimize in \(t\) to get the stated exponential bound. Combine matched and unmatched bounds and sum over \(T\) edges to obtain (17).

**PROVED (parity at the isotropic point).** Choose the larger of \(A_t,B_t\) at each edge, that is, the matching of smaller squared quaternion distance. Let \(p_j(L)\) be the probability under \(\nu\) that these matchings exchange the two sheets after one turn. Ties can be assigned arbitrarily. Equation (17) gives
\[
 \left|\tanh(\widehat J/2)-(1-2p_j(L))\right|
                 \le C T e^{-cN}+2T e^{-\beta E}.                         \tag{18}
\]
Indeed the product of the signs in (16) is the parity sign. The product of the absolute hyperbolic tangents differs from one by at most \(2T e^{-\beta E}\) on the good event. Therefore (24) is equivalent to
\[
                    \liminf_j p_j(L)>\frac{1650}{3301}
                       \quad\hbox{at some fixed }L.                         \tag{19}
\]
Here \(\tanh[\log(1651/1650)/2]=1/3301\), and (15) or row 1145 (17) removes the unprojected trace error.

**PROVED (obstruction to an absolute or local swap estimate).** The expectation of the absolute product in (16) tends to one, irrespective of the parity mean needed in (19). More precisely the observed preferred parity recovers the parity in the expansion of \(\nu\) with probability at least \(1-CTe^{-cN}\). In the matched labeling used to prove (17), the signed advantage is at least \(E\) on the good event. Thus the two induced laws on *unordered slice histories* from the two covers have total variation distance at least \(1-CTe^{-cN}\), even if their partition functions are comparable. Also, changing the two link fields on at most \(E/32\) edges per slice cannot reverse this parity on the good event. At a time edge the union of changed links has size at most \(2E/32\), and the change per link in \(D_t\) is at most eight. Slice relabeling itself flips two signs and preserves the parity. This last bound concerns the specified temporal-gauge coordinates. It puts no restriction on a transformation of a positive fraction of an entire slice. Equation (19) still needs the relative weights of the two parity classes.

## 7. How short the cut segment can be

**PROVED.** In (7)–(9) one can also use
\[
 b=\lfloor\gamma[\log(2+\beta)]^{1/5}\rfloor,\qquad
 h=\lceil C_1(1+\beta)\log n\rceil .                                     \tag{20}
\]
Here \(\gamma>0\) is sufficiently small and \(C_1\) sufficiently large, both independent of \(j\). The omitted fraction of all spatial plaquettes in the cylinder is at most \(2h/(bT)\). Both \(b\to\infty\) and \(a_j h\to0\).

**PROVED.** The spectral deficit on the *invariant* subspace of each box is at least \((1+\beta)^{-1/2}\) eventually, by (2) and the choice of \(\gamma\). Repeat the row-kernel estimate (8) for its projected kernel, using that same deficit. Its pointwise lower bound \(l\) and upper bound \(U\) used in §3 still apply after gauge averaging, and its top eigenfunction is the same. At \(r=h-1\),
\(r(1+\beta)^{-1/2}\) dominates \(C(1+\beta)(b+1)^3+6\log n\), since \(\beta=O(\log n)\). The resulting projected relative error is \(o(n^{-5})\). By (15), with the number of vertices of the box and the same degree bound, its unprojected kernel has relative error \(o(n^{-5})\) from its projected one when \(C_1\) is large enough. Indeed the sum in (15) is \(O(\exp[-r/(7(1+6\beta))])\) once the exponent exceeds one. A free crossing link has the same estimate from its one-link multiplier bound. Multiplying the estimates and integrating against the rest gives (7) and (9).

**PROVED (a limit of this shortening, even after gauge projection).** For the time-independent cut array of §2, take the elementary \(12\)-plaquettes crossing interval boundaries in **both** coordinate directions. All four spatial links of each of these plaquettes are free crossing links. For \(b\ge2\) these selected plaquettes are edge-disjoint. There are
\(M_*=\lfloor n/b\rfloor^2 n\) of them. Multiply the product vacuum by any product of their fundamental traces. These are \(2^{M_*}\) mutually orthogonal physical eigenfunctions. The vacuum is constant on the crossing links, an unpaired fundamental factor integrates to zero on a free edge, and the one-link convolution multiplies every fundamental coefficient by \(r_\beta=I_2(\beta)/I_1(\beta)\). A product with \(k\) marked plaquettes has eigenvalue \(\Lambda r_\beta^{4k}\). Therefore the cut array's stand-alone period-\(h\) defect obeys
\[
                 J_{\rm cut}(h)\ge M_*\log(1+r_\beta^{4h}).                 \tag{21}
\]
This uses \(J\ge\log\operatorname{Tr}(G/\Lambda)^h\) on the physical space. The one-link angle estimate in row 1145, (21), gives \(1-r_\beta\le C/\beta\), and \(r_\beta\le e^{-c/(1+\beta)}\) there. Hence if \(h=o(\beta\log M_*)\), the right side of (21) diverges along the trajectory. Erasing the ends by the stand-alone cut segment, as in (8), requires a time of order at least \(\beta\log n\) for the choices in (20). This is a lower bound on the length required by the stand-alone kernel estimate.

## 8. Can cancellation of partition-function zeros control the real integral?

**GUIDE.** Return to the homogeneous spatial coupling \(s\) in (24), with fixed temporal coupling \(\beta\). Row 1145, §9, gives one uncanceled zero or pole within a disk of radius \(\beta(1+o(1))\) under the ultraviolet witness. Theorem ZB-chain in `gap-zf-box-x.md`, §§3.1–3.2, transports smallness along disks for a zero-free free-box problem. The following estimate permits poles throughout the chain. It counts the distinct uncanceled points one must keep in the actual *periodic thermal ratio*.

**PROVED.** Put \(R(z)=Z_T(z)^2/Z_{2T}(z)\), with the common electric normalization of row 1145, §7. Fix \(0<\epsilon<1\). For an absolute sufficiently large \(A_\epsilon\) let
\[
 w=A_\epsilon\,\beta/\log n,\quad
 \mathcal U=\{z:\operatorname{dist}(z,[0,\beta])\le w\},\quad
 M=\#\{z\in\mathcal U:\operatorname{ord}_z R\ne0\}.                        \tag{22}
\]
Count each point once after cancellation, however large its multiplicity. Along any subsequence on which \(M\le n^{1-\epsilon}\), **\(J(\beta)\to0\)**. Conversely a fixed positive lower bound for \(J(\beta)\) forces \(M>n^{1-\epsilon}\) eventually. The width is bounded in bare spatial-coupling units by (RF25), and \(w/\beta\to0\). Failure of (24) at a size forces this many points along a subsequence at that size.

**PROVED (removing the poles).** The real derivative extends to the meromorphic function \(D=R'/R\). Every point counted in (22) is a simple pole of \(D\) with signed integer residue. Define
\[
                 P(z)=\prod_{\zeta\ {\rm counted}}\frac{z-\zeta}{4(\beta+w)}.
\]
On \(\mathcal U\), each factor has modulus at most one. We show
\[
             |P(z)D(z)|\le C NT\quad
             \text{if }\operatorname{dist}(z,[0,\beta])\le w/2 .             \tag{23}
\]
Fix a real center \(x\in[0,\beta]\). For period \(k=T,2T\) write \(V(q)=Z_k(x+q)/Z_k(x)\) using the normalized-trace source. It has \(V(0)=1\) and \(|V(q)|\le e^{3Nk|q|}\), since it is an exponential moment of a sum of \(3Nk\) numbers in \([-1,1]\). There are at most \(C Nk w\) zeros in \(|q|\le w\), counting multiplicity. Indeed, the circle mean of \(\log|V|\) at a radius between \(2w\) and \(3w\) is bounded by \(9Nk w\), and factoring the interior zeros shows that each zero in \(|q|\le w\) adds at least \(\log 2\) to this mean over its value at zero.

**PROVED.** Choose \(r\in(3w/4,w)\) whose boundary avoids both sets of zeros. Divide \(V\) by one factor \(r(q-a)/(r^2-\bar a q)\) for every zero \(a\) inside, with multiplicity, obtaining a zero-free analytic \(g\). The factors have modulus one on the circle, so \(\log|g|\le 3Nk r\) there and \(\log|g(0)|\ge0\). The nonnegative harmonic function \(3Nk r-\log|g|\) has circle mean at most \(3Nk r\). Differentiating its disk Poisson kernel at \(|q|\le w/2\le 2r/3\) bounds the gradient by \(C/r\) times the mean. By the Cauchy–Riemann equations this gives \(|g'/g|\le C Nk\). The reflected-pole term \(\bar a/(r^2-\bar a q)\) from each factor is at most \(3/r\) there. Thus \(D(x+q)\) is a function bounded by \(C NT\) plus \(\sum_\zeta m_\zeta/(x+q-\zeta)\) over the uncanceled poles in the disk, with \(\sum|m_\zeta|\le C NT w\). Every denominator here is a factor of \(P\), and \(|P(z)/(z-\zeta)|\le 1/[4(\beta+w)]\). This proves (23), with removable singularities filled. No lower bound on either individual partition function away from the real line was required.

**PROVED (propagating the strip bound).** Write \(s_0=c/(1+\beta)\). Row 1145, (22), and Cauchy's integral formula give
\(\sup_{|z|\le s_0/2}|D(z)|\le\exp[-c_1 n/(1+\beta)]\) eventually. Polynomial prefactors are absorbed since \(\beta=O(\log n)\). Both bounds in (RF25) at fixed reference coupling give \(\beta\asymp\log n\), so \(w\) eventually exceeds \(4s_0\). Logarithmic convexity of the circle maximum for \(P D\), between radii \(s_0/2\) and \(w/2\) at zero, gives the inner smallness exponent a weight at least \(c/\log(2+w/s_0)\) on the disk of radius \(w/8\). This convexity follows from the maximum principle applied to \(\log|P D|\) minus the affine interpolant in \(\log|z|\). Now advance centers along the real interval in steps at most \(w/8\), taking \(\lceil8\beta/w\rceil\) steps in total. At each center grow the radius \(w/8\) to \(w/4\) inside the outer radius \(w/2\) of (23). The weight is \(1/2\), and the grown disk contains the next inner disk. Consequently on the **whole** real interval
\[
 \log|P D|\le\log(C NT)-
 \frac{c n}{(1+\beta)\log(2+w/s_0)}\,\exp[-8(\log2)\beta/w].               \tag{24a}
\]

**PROVED (return to real couplings).** Choose \(A_\epsilon\) so \(8\log 2/A_\epsilon<\epsilon/4\). Remove from the real interval the disks of radius \(n^{-12}\) about the \(M\) points. Off them, \(-\log|P|\le M\log[4(\beta+w)n^{12}]\). If \(M\le n^{1-\epsilon}\), the negative term in (24a) dominates this loss and \(\log(C NT)\) by a positive power of \(n\). Thus the integral of \(|D|\) on the remaining interval tends to zero. The removed length is at most \(2M n^{-12}\). There the exact finite-volume derivative bound \(|D(s)|\le12NT\) follows directly from the real plaquette means. Its contribution also tends to zero. In fact this proves \(\int_0^\beta |J'(s)|\,ds\to0\) along that subsequence. Add \(J(0)=o(1)\) to obtain (22)'s conclusion.

**PROVED given the named ultraviolet witness.** For the admitted spatial multiples of \(\ell_\star^{\rm CA}\) with \(L/2\ge2\mathsf d\), row 865, `gap-sdcyl-ca-astra.md`, lines 218–242, gives \(S_{\rm ev}(T)\ge \rho_{\rm CA}^{\,L/(3\mathsf d)}\). It uses the reference-lattice witness and source-transfer assumptions of that row, with \(\rho_{\rm CA}=c_{\mathcal K}/(3C_{\mathcal K})\), as specified using CA-I 2715–2738, 2763–2781. Hence \(J(\beta)\ge\log(1+\rho_{\rm CA}^{\,L/(3\mathsf d)})>0\). At **every** such fixed size the lower count in (22) holds for all sufficiently fine cutoffs. The singularities occur in conjugate pairs off the real axis. This rules out restoring the endpoint by a continuation with only a bounded or polylogarithmic number of surviving singular points in that tube. It gives no lower bound exceeding the seed threshold at every \(L\), since the witness lower bound decreases with \(L\).

## 9. Canceling the two extensive joining costs at the ends of the slab

**GUIDE.** Equations (11)–(12) leave open cancellation by weights depending on the two end slices. Such weights can be arbitrarily large even if they factor into a left and a right weight. Thus the small overlap on full path space is insufficient to test this possibility. The following two bounds concern the integrated slab kernel itself. They use the same conditional even-sector witness as §8.

**PROVED given that witness.** Write \(K_h=P F^h\) on the full isotropic spatial cube and \(C_h=P G^h\) on the time-independent cut array, where \(G\) is the product transfer from §2. Use \(h\) in (20) or §3. Optimization over arbitrary real functions of the end configurations gives the lower bound
\[
 \inf_{f,g}\ \sup_{x,y}
   |\log[K_h(x,y)/C_h(x,y)]-f(x)-g(y)|
      \ \ge\ \tfrac12\log\!\frac{1+e^{-M_{\mathcal K}a_jh}}
                                  {1-e^{-M_{\mathcal K}a_jh}}-o(1).          \tag{25}
\]
Here \(M_{\mathcal K}=2\log(1/\rho_{\rm CA})/(3\mathsf d)\) as in row 865. The right side diverges when \(a_jh\to0\). This tests restoring the full interaction *after* allowing both endpoint normalizations and integrating out every internal field.

**PROVED.** For a strictly positive symmetric kernel \(H\) define
\(\Delta(H)=\sup_{x,y,u,v}\log[H(x,u)H(y,v)/(H(x,v)H(y,u))]\).
Both cut-kernel estimates give \(\Delta(C_h)=o(1)\) because vertex averaging preserves the two pointwise bounds around its invariant product vacuum. Separable endpoint factors cancel from this cross ratio. If the error on the left of (25) for specified \(f,g\) is \(d\), then \(\Delta(K_h)\le4d+o(1)\).
To bound it below, form the Markov kernel \(p_x(dz)=K_h(x,z)\psi(z)dz/(\lambda_0^h\psi(x))\). For two rows let \(m\le p_x/p_y\le M\) be their ratio extrema. Its \(p_y\)-mean is one and \(M/m\le e^{\Delta(K_h)}\). The affine chord bound for \((t-1)_+\) on \([m,M]\) yields \(\|p_x-p_y\|_{\rm TV}\le(M-1)(1-m)/(M-m)\) unless the rows coincide. For \(M/m=R\), maximizing in \(m\in[1/R,1]\) gives \((\sqrt R-1)/(\sqrt R+1)\), attained at \(m=1/\sqrt R\). Thus row averaging contracts the oscillation of any real bounded function by at most \(\tanh(\Delta(K_h)/4)\). Apply it to an excited eigenfunction divided by the positive vacuum. This quotient is continuous and bounded at each finite cutoff. The witness supplies an eigenvalue ratio at least \(e^{-M_{\mathcal K}a_jh}\). Inverting the bound gives (25).

**PROVED given that witness (an averaged obstruction).** Normalize \(K_h(x,y)^2\,dx\,dy\) to a probability \(Q_h\). This is the two-endpoint marginal on a homogeneous cylinder of period \(2h\), since its two halves have the same symmetric kernel. Even with freely chosen end marginal densities \(p,q\), one has the exact identity
\[
 \sup_{p,q}\int\sqrt{dQ_h\,p(x)q(y)\,dx\,dy}
      =\frac{\lambda_0^h}{\sqrt{\operatorname{Tr}(P F^{2h})}}
      \le(1+e^{-2M_{\mathcal K}a_jh})^{-1/2}.                              \tag{26}
\]
Indeed the integral is the bilinear form of \(K_h\) on the unit vectors \(\sqrt p,\sqrt q\), divided by its Hilbert–Schmidt norm. Its maximum is attained at \(p=q=\psi^2\). The bound uses just the one even excitation. Thus the upper limit of even the best product affinity at the shortened period is at most \(1/\sqrt2\). For the cut array the corresponding affinity tends to one by (8) or (20). Multiplying its end kernel by arbitrary positive factors of the separate ends and renormalizing its square still yields a law within \(o(1)\) in total variation of a product, uniformly in those factors whenever the normalizer is finite. This follows directly from the uniform relative bounds around the cut product kernel. It also gives the same \(1/\sqrt2+o(1)\) bound on its affinity with \(Q_h\), by Cauchy–Schwarz and \(\int(\sqrt p-\sqrt q)^2\le2\|p-q\|_{\rm TV}\).

**OPEN.** Estimates (25)–(26) refute a pointwise or a short-period product approximation to the restored slab. The required weighting is the long-period rest kernel in §3. Its exact cancellation with the nonseparable slab correction is what (9) measures. The short-period marginal in (26) does not give that signed long-period estimate.

## 10. A positive interval of actual restoration

**PROVED.** The short-slab reduction also works with **strictly positive** couplings on the interface throughout. There are absolute \(c,C>0\) such that one may take
\[
 H=\left\lceil C(1+\beta)(b+1)^3 e^{C(b+1)^5}\right\rceil,\quad
 m=\lceil 10\log n\rceil,\quad h=1+mH,\quad
                  u_*=\frac{c}{H(b+1)^2}.                                 \tag{27}
\]
Choose \(b\) as in (20), decreasing \(\gamma\) if necessary. Then \(a_j h\to0\). Put the full coupling \(\beta\) on every plaquette except \(D_j\) of §3. Uniformly for a common \(0\le u\le u_*\) on \(D_j\), the resulting thermal defect tends to zero. Thus (9) with this \(h\) has exactly the same limsup if its lower integration endpoint is raised to \(u_*\). This bounds a signed part of the needed response with the entire exterior at full isotropic coupling.

**PROVED (the reference measure).** Assign each positive spatial link to the cell containing its base vertex. One component \(c\) then carries the transfer of its open box tensored with those of at most \(3(b+1)^2\) outgoing free links. Use the vacuum transform of this component, with invariant probability \(\mu_c=\psi_c^2\,dU\). Its \(\ell\)-step transition density relative to \(\mu_c\) is \(D_{\ell,c}(x,y)=G_c^\ell(x,y)/(\lambda_c^\ell\psi_c(x)\psi_c(y))\). For any prescribed fixed small \(\sigma>0\), choosing the constants in \(H\) suffices for \(\|D_{\ell,c}-1\|_\infty\le\sigma\) for every \(\ell\ge H\). For the internal box use the projected row estimate (8) with gap (2), then (15). The choice \(\ell\ge H\) absorbs the exponent \(C(1+\beta)(b+1)^3\) and the box vertex count. The outgoing link factors have errors at most \(C e^{-c\ell/(1+\beta)}\), and their product obeys the same assertion upon increasing \(C\). With the specified \(b\), \(H\) is bounded by a fixed power of \(1+\beta\).

**PROVED.** Assign each oriented spatial plaquette of \(\Sigma\) to its base cell \(c\), and call the sum of its assigned traces \(X_c\). There are at most \(6(b+1)^2\) such plaquettes per cell. Their links belong to \(c\) and at most its three positive-direction neighbors. A component occurs in at most four such groups. Write \(G_u=e^{u\sum X_c/2}G e^{u\sum X_c/2}\), dropping scalar exponentials in the time length. In the open kernel of \(G_u^{mH}(x,y)\) fix both end configurations. Sample the intermediate block endpoints independently with laws \(\mu_c\). Given those endpoints, sample independent normalized \(H\)-step bridges of each component in each time block. This is a probability reference. Relative to \(\Lambda^{mH}\Psi(x)\Psi(y)\), the open kernel is the expectation of the product of the factors
\[
              D_{H,c},\qquad
              \exp\!\left[u\sum_{t\ {\rm in\ block}}X_c(U_t)\right].
\]
The upper time endpoint is excluded in the sum. The extra factor for symmetric endpoint weights is \(e^{u[\sum X_c(y)-\sum X_c(x)]/2}\), separable in \(x,y\). The expression follows by multiplying the transition densities and then undoing the vacuum transform. For \(|u|\le u_*\) both types of factors differ from one by at most \(\sigma\).

**PROVED (terms that depend on both ends).** Join labels when they read a common component and their time blocks coincide or are adjacent. Each closed neighborhood has size at most \(4\cdot3\cdot5=60\). Families in different connected components use disjoint endpoint and bridge variables. Apply the connected-set expansion of row 1145, §7, to these labels. Explicitly a connected nonempty \(X\) has activity \(\mathbb E\prod_{i\in X}(F_i-1)\) of modulus at most \(\sigma^{|X|}\). There are at most \(60^{2(r-1)}\) sets of size \(r\) through a label by the tree-traversal bound. Choose \(\sigma\) with \(60\sum_{r\ge1}60^{2(r-1)}(\sigma e^2)^r\le1\), and then choose \(c\) in (27). The Kotecký–Preiss tree estimate, in Sussman and Alpoge's outline lines 1225–1269 and 1273–1347, bounds the absolute connected log sum with weight \(e^{\sum |X|}\) by \(C n^3m\), exactly as in that row. This bound is uniform in the two fixed end configurations. In a four-term logarithmic cross ratio every list that misses the first or last block cancels, since it is independent of the corresponding end. A connected list touching both contains at least \(m\) labels counting repetitions. Consequently
\[
                  \Delta(G_u^{mH})\le C n^3m e^{-m}=o(1).                  \tag{28}
\]
For the real symmetric kernel fix any \(z\) and set \(v(x)=G_u^{mH}(x,z)/\sqrt{G_u^{mH}(z,z)}\). The ratio \(G_u^{mH}(x,y)/[v(x)v(y)]\) lies between \(e^{-\Delta}\) and \(e^\Delta\). Inserting these bounds once and twice against the same nonnegative rest kernel, with vertex projection, proves the assertion in (27).

**PROVED (why the same expansion cannot complete the restoration).** Even after canceling every list missing one of the ends, the absolute sum used for the cross ratio in (28) diverges for some endpoints as soon as \(u\sqrt{H\beta}\ge C'\), for \(\beta\) sufficiently large and \(m\ge3\). This uses the repeated-polymer obstruction of row 1145, (26), now inside the interacting-box reference. Choose one of the four-free-link plaquettes \(p\) of (21) and an interior time block. Let \(A\) be the singleton magnetic label of its base cell on that block. Its activity \(z_A\) is independent of the two outer endpoints. Conditional on the four link paths of \(p\), the mean trace of each other plaquette assigned to the group at each time is zero. Indeed it contains a free crossing link outside these four. The same parallel pair of crossing links determines a unique elementary plaquette. All free-link paths in this interior block are independent of other links and invariant under multiplying the entire path by \(-1\). This follows also for links assigned to one component, since their endpoint laws and bridges tensor. Conditional Jensen therefore gives \(z_A\ge \mathbb E e^{uY_p}-1\), where \(Y_p=\sum_t w_p(U_t)\) within the block. Its law is symmetric by a single free-link center flip.

**PROVED.** Compare these four reference paths to four stationary electric walks. Their endpoint densities at length \(H\) are each at most two, so the reference expectation of \(Y_p^2\) is at least \(2^{-4}\) times its stationary value. There the time-separation-\(d\) moment is \(r_\beta^{4d}/4\) by the four-link eigenfunction and its Haar norm. Summing \(0\le d\le c_2\beta\), using \(1-r_\beta\le C/\beta\) and \(H\ge C_2\beta\), gives \(\mathbb E Y_p^2\ge c_3 H\beta\). Thus \(z_A\ge c_3 u^2 H\beta/2\). Now choose a component read by \(A\) that carries a free link of \(p\). Let \(B\) be the connected polymer of its \(m\) electric labels, one per block. Its activity at fixed endpoints is
\[
             z_B(x,y)=D_{mH,c}(x_c,y_c)-1 .
\]
This follows by integrating the kernels \(D_{H,c}-1\) against independent intermediate \(\mu_c\)'s, since the mean projection commutes with this Markov semigroup. Some rectangular difference of \(z_B\) is nonzero. Otherwise it would be a sum of separate end functions, and integration against \(\mu_c\) in either variable would force it to be zero. The free link has a nonzero fundamental multiplier at time \(mH\), excluding that possibility. \(A\) and \(B\) are incompatible. Lists with one \(B\) and \(k\) copies of \(A\) have combined connected coefficient \((-1)^k z_B z_A^k\), by extracting the term linear in the \(B\) marker in \(\log(1+t_A z_A+t_B z_B)\). Take the four endpoints that give the nonzero rectangular difference. These terms survive the end subtraction for every \(k\), and their absolute sum diverges once \(z_A\ge1\).

**OPEN.** This obstruction applies to the stated absolute expansion after the endpoint cancellation. The sector bound of row 865 and (25)–(26) also prevent a uniformly or typically separable short slab at full coupling, in their stated measures. None of them excludes cancellations between different connected lists *and* the long-period rest kernel.

## 11. Resumming the plaquettes responsible for the divergence

**PROVED.** Split \(\Sigma=\Sigma_1\sqcup\Sigma_2\) according as one or both plaquette directions cross interval boundaries. **Every plaquette in \(\Sigma_2\) can be restored to full strength**, throughout the shortened interval as well as outside it, in (7), (9), (20) and (27). Only \(\Sigma_1\) needs the weak coupling \(u\) in (27). Thus all repeated insertions on the four-free-link plaquettes used to refute the preceding absolute expansion can be summed exactly.

**PROVED.** The graph consisting of crossing links alone is the Cartesian product of three one-dimensional graphs consisting of isolated vertices and disjoint edges. Each connected component with edges is therefore an open box of side lengths one or two, in fine lattice units. Its internal plaquettes are precisely the plaquettes crossing two boundaries. Turning on all their magnetic weights preserves the tensor product before vertex projection, now over the original open boxes and these small boxes. The proof of (4), (8) and (15) applies to each small box with bounded \(E\), including an isolated free link. For (27) group each small box with one coarse cell containing one of its vertices, by a fixed choice. At most \(C(b+1)^2\) such components are assigned to a cell, since each has at least one vertex on the boundary of that cell, and they have disjoint vertex sets. A group of one-boundary plaquettes based in a cell reads only components assigned within a bounded coarse-cell distance (at most two in each coordinate), each read by only a bounded number of groups. The neighborhood constant in the connected-set proof stays absolute. Choose \(\sigma,c,C\) for this larger constant. Endpoint mixing still follows for the tensor factors with at most \(C(b+1)^2\) small-box errors. These changes prove the stated positive restoration.

**PROVED (a slow observable after this resummation).** Let \(G'\) denote the unprojected time-independent transfer with all double-boundary and all internal plaquettes on, and the single-boundary ones off. For \(b\ge8,\ b/\beta\) sufficiently small, there exist \(M'\ge c n^3/b^3\) physical plaquette observables whose trial states give
\[
 \log\operatorname{Tr}\!\left[P(G'/\Lambda')^t\right]
   \ge M'\log\big[1+(1-Cb/\beta)^t\big],\qquad t=1,2,\ldots,              \tag{29}
\]
where \(\Lambda'\) is the product vacuum eigenvalue. In particular shortening a stand-alone thermal buffer to \(o((\beta/b)\log M')\) fails even after the resummation.

**PROVED.** In an internal box let \(r_e=\mathbb E\,\tfrac12\operatorname{tr}(U_e U_e'{}^{-1})\) in the stationary one-step vacuum law of the *unprojected* box, with two successive spatial configurations \(U,U'\). Then \(\sum_e(1-r_e)\le CE/\beta\). To see this, use unnormalized electric kernels at \(v=\beta,\beta/2\), keeping the spatial coupling fixed at \(\beta\), and write \(\lambda(v)\) for the top eigenvalue in this convention. At \(\beta\) the trial-set bound of §1 gives \(\lambda(\beta)\ge I(\beta)^E e^{-CE}\), and at \(\beta/2\) the norm upper bound gives \(\lambda(\beta/2)\le I(\beta/2)^E\). Testing the latter transfer on the former vacuum gives
\(\mathbb E_\beta e^{(\beta/2)\sum_e a(U_eU_e'{}^{-1})}\le\lambda(\beta/2)/\lambda(\beta)\le e^{C'E}\).
Jensen proves the estimate.

**PROVED.** Pair neighboring cells across disjoint faces in direction one by matching successive pairs along each row of cells. This gives at least \(c(n/b)^3\) pairs. On each shared face there are at least \(c b^2\) crossing \(12\)-plaquettes whose two crossing links are single-link components. Choose their transverse coordinates strictly away from interval endpoints in directions two and three, including the upper end of the step in direction two. Their other two links are in the two different original boxes. On these choices the sum of the deficits \(1-r_e\) of the internal links, over all choices, is at most \(C b^3/\beta\) by the preceding estimate and bounded incidence. Choose one plaquette \(p\) for which the sum is at most \(C b/\beta\). Its two single links have deficit at most \(C/\beta\). The four component paths are independent in the product vacuum, and their equal-time single-link marginals are Haar. For each link the joint law at two times is invariant under simultaneous left and right multiplication by independent group elements at its two endpoints. Thus, conditional on \(U_e\), the expectation of \(U'_e\) as a quaternion is \(r_e U_e\), since the increment has a central law independent of \(U_e\). The one-step Rayleigh quotient of \(w_p\) times the product vacuum for the normalized transfer is consequently \(\prod_{e\in p}r_e\ge1-C b/\beta\). Its squared norm is \(1/4\) and its mean is zero. The spectral measure of this unit trial vector is supported in \([0,1]\). Jensen for \(x^t\) gives its \(t\)-step quotient at least \((1-C b/\beta)^t\).

**PROVED.** Plaquettes chosen on different matched faces read disjoint *components*. Products of the individually normalized trial multipliers, one for each member of any subset of the chosen plaquettes, give an orthonormal family times the product vacuum. Every vector is invariant under the physical vertex gauges. The diagonal matrix elements of the normalized \(t\)-step transfer factor over the chosen faces. Summing this family proves (29).

**PROVED (the next positive expansion also stops).** In the repaired version of (27), isolate a single selected one-boundary plaquette from the magnetic group of its cell, as its own magnetic label. This changes the uniform neighborhood bound by an absolute factor only. For an interior block of length \(H\) its singleton activity is at least \(c u^2 H\beta/b\). Indeed its trace sum is symmetric under a center flip of one of its free crossing links. The stationary two-time moment at separation \(d\) is at least \((1-Cb/\beta)^d/4\) by the same Rayleigh and Jensen proof. Comparing its component paths in the reference to their stationary laws loses at most a constant, since their endpoint transition densities are uniformly bounded. Summing \(0\le d\le c'\beta/b\) gives the stated bound on the activity. The argument with the electric polymer \(B\) of §10 applies to a component group containing one of these free links. Hence this explicit real resummation, followed by the absolute log expansion with that marked face, still diverges for a cross ratio when \(u\sqrt{H\beta/b}\ge C'\).

**OPEN.** An ordinary face plaquette couples **two distinct** large-box fields and two crossing links. The proof of (29) uses all four. Adding all such interactions joins the large boxes across every coarse face. The tensor law used in the positive estimate then ceases to hold. The facts that each small component is cold and that the exceptional physical four-volume vanishes do not estimate the signed cost of this joining.

## 12. A test directly on the remaining face interpolation

**PROVED given the witness where stated.** Leave all \(\Sigma_2\) plaquettes at full strength as in §11. Keep \(b,H,u_*\) of (27), but use \(m=\lfloor n/(H\log n)\rfloor,\ h=1+mH\). Let \(D_j\) consist only of the \(h\) layers of \(\Sigma_1\). Again the physical duration tends to zero. Let \(R_D(u)\) denote the ratio of the two replicated-schedule partition functions as in (22), and \(J_D=\log R_D\) on the real axis. The exact remaining inequality is
\[
        \limsup_j 2|D_j|\int_{u_*}^{\beta_j}
                  [w_{1,D}(u)-w_{2,D}(u)]\,du < \log(1+1/1650)           \tag{30}
\]
at one fixed grid size. On every admitted witness size this integral, **including** its factor \(2|D_j|\), has lower limit at least \(\log(1+\rho_{\rm CA}^{L/(3\mathsf d)})\). In particular an \(o(1)\) error for deleting these plaquettes from the thermal defect itself is ruled out on those sizes. This is a lower bound on the *signed* correction.

**PROVED.** Equation (28) and the nonnegative rest-kernel comparison give \(|J_D(u)|\le C n^3m e^{-m}\) for every real \(|u|\le u_*\). Increasing endpoints from \(0\) to \(u_*\) and differentiating as in (9) proves (30), with the witness lower bound at its restored endpoint supplied by §8. This proof does not need complex positivity of the rest kernel.

**PROVED (surviving singularities after the resummation).** For the width \(w=A_\epsilon\beta/\log n\) of (22), with \(A_\epsilon\) sufficiently large, the conclusion of (22) also holds for \(R_D\). In particular on admitted witness sizes \(R_D\) has more than \(n^{1-\epsilon}\) distinct uncanceled zeros or poles in this tube eventually. The small complex-disk bound for the *homogeneous* interpolation cannot be used here. Instead one can start from the real interval established in §10.

**PROVED.** Form \(D=R_D'/R_D\) and the zero-removing polynomial \(P\) as in §8 for this new ratio. The proof of (23) applies with \(NT\) replaced by \(|D_j|\), since the exponential moments now involve at most \(2|D_j|\) bounded insertions. For real \(u\), \(|J_D''(u)|\le6|D_j|^2\), by the two separate variance formulas. Taylor's formula on a real interval of length \(e^{-m/3}/(1+|D_j|)\), using the bound on \(|J_D|\), gives \(\sup_{|u|\le u_*/2}|D(u)|\le e^{-m/5}\) eventually. Here \(m\ge n/(\log n)^{C'}\), while \(u_*^{-1}\) is at most a fixed power of \(\log n\).

**PROVED.** To pass from the segment to a disk, take \(r=u_*/4\). The rectangle \([-r,r]\times[0,r]\) in the complex plane lies in the domain of (23). For \(B_0=C(1+|D_j|)\), the subharmonic function \(\log(|P D|/B_0)\) is nonpositive there and at most \(-m/5\) on the bottom. The harmonic function
\[
 v(x,y)=\cos(\pi x/(2r))\,
            \frac{\sinh[\pi(r-y)/(2r)]}{\sinh(\pi/2)}
\]
vanishes on both sides and the top and is in \([0,1]\) on the bottom. The maximum principle bounds the subharmonic function above by \(-m v/5\). On \(|x|\le r/2,\ 0\le y\le r/2\) the minimum of \(v\) is an absolute positive number. Use the reflected rectangle below the real axis as well. The initial disk of radius \(r/2\) therefore has log bound \(\log B_0-cm\). Propagate it exactly as in (24a), replacing \(n/(1+\beta)\) by \(m\), and \(s_0\) by \(r\). The initial logarithmic denominator is \(O(\log\log n)\). If the number of points is at most \(n^{1-\epsilon}\), the same removal of radius-\(n^{-12}\) disks gives \(\int_0^\beta |J_D'|\,du\to0\) along that subsequence. This proves the assertion. The required face contribution can thus coexist with very strong cancellation of individual partition zeros, but any such cancellation must still leave the stated number of distinct points.

## 13. What the singularity count can decide

**PROVED (comparison).** The two-level transfer in row 1145, §7, also tests whether the lower count in (22) can by itself decide the real threshold. Keep its two eigenvalues \(1,\exp[-d+(d-\kappa/T)z/\beta]\), where \(d=(1+6\beta)^{-1}\) and \(\kappa>0\) is fixed. Put \(v=\exp[-Td+(Td-\kappa)z/\beta]\). The exact ratio is \((1+v)^2/(1+v^2)\). Both choices \(\kappa=1,13\) have exponential smallness of their log ratio on the initial strip and a positive, cutoff-independent endpoint value. At \(z=\beta\) their excess ratios are \(2e^{-\kappa}/(1+e^{-2\kappa})\). The first exceeds \(1/1650\) since \(e<3\). The second is smaller since \(e>2\) and \(2/2^{13}<1/1650\).

**PROVED.** All the zeros and poles of these ratios lie on the line
\[
 \operatorname{Re}z=\beta+\frac{\kappa\beta}{Td-\kappa},\qquad
 \operatorname{Im}z=\frac{\beta}{Td-\kappa}\,\phi .
\]
The zero phases are \(\phi=(2r+1)\pi\), and the pole phases \(\phi=(r+1/2)\pi\), \(r\in\mathbb Z\). There are no common points. Each model has \(\Theta(n/(\beta\log n))\) distinct points in the tube (22), by their displayed spacing and \(T=n/2\). The real offsets of the two lines differ by \(O(\beta^2/n)\). Thus the cardinality order and bounded-width localization occur on both sides of the proposed numerical threshold. These examples test an inference from analytic data. Equation (30) requires the joining law of the Wilson measure.

**OPEN (stopping point).** For one fixed physical grid size the missing estimate is an upper bound below \(\log(1651/1650)\) on \(F_2-2F_1\) when the ordinary crossing faces in (30) are restored from \(u_*\) to \(\beta\), where here each \(F_i\) uses \(u_*\) as its reference. Direct positive weights have the extensive overlap loss (11)–(12), also with \(u_*\) in place of zero by (11) and \(u_*/\beta\to0\). The two endpoint replacements fail by (25)–(26) on witness sizes. The repeated-activity series still diverges after exact corner resummation in §11. Full-slice absolute matching gives (17)–(19) and leaves the relative parity probabilities undetermined. The connected-holonomy estimate (13) loses its usable exponent before \(b=n\). Singularity counts alone fail the two-level test above. I have no estimate of the required signed face difference or a lower bound that excludes the seed at every size. There was no numerical proof step or guide run. The new hand arguments await independent checking.

RESULT — PROVED by hand, unchecked. Equation (24) is equivalent to (30), with every temporal plaquette and every double-boundary plaquette at full coupling, and only ordinary spatial faces varied during a vanishing physical time interval. The signed response up to the positive \(u_*\) in (27) vanishes in the limit. On admitted witness sizes more than \(n^{1-\epsilon}\) distinct zeros or poles survive cancellation near the remaining real interpolation for every fixed \(0<\epsilon<1\). OPEN. The strict bound in (30), (W), and the four-dimensional \(SU(2)\) mass gap remain open.
