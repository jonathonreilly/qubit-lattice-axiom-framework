# Flat propagator port: queue row 95
Provenance: OpenAI Codex (GPT-6; exact serving variant and effort setting not exposed in this session), requested effort max; checkout `02c07af230c9eb378a9a04b05247eec1408070c2`; Sussman–Alpoge outline `31a47c543775`; T. Balaban, CMP **89** (1983), 571–597, **95** (1984), 17–40, **96** (1984), 223–250, and **99** (1985), 389–434; research text, not an audit, granting no status.

## 1. Contract and sources

This note attacks row 95, hence the flat inputs to rows 81, 82, 84 and 85. The order is F0 of `a1-balaban.md` §3.9, including the default level-0 seam; the flat column bound in `a3-profile-gate.md` §2 D1; then F1–F5 of `a3-balaban.md` §13. A counterexample to a required input blocks its use by these consumers; a proof must supply the actual consumer norms, including uniformity in depth and mesh. No computation discharges a statement here.

Credit **T. Balaban** for the averaging operators, scalar and vector propagators, Landau projection, Gram inverses, multiscale walk method and estimates taken from the four papers. Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**, for the outline, default determining-set convention and its requested transfer. The outline was fetched once from the specified revision to `/tmp/sa_ym4.tex`. The papers are read in their owner-supplied location; no paper is copied into the repository. Formula reconstructions are identified at their use.

The precise starting obligation is the conjunction in `a1-balaban.md` (3.21)–(3.23), its two energy inequalities and its two coarse Gram inequalities. In particular the vector energy assertion is on the domain of the positive inverse, with physical cell volumes and the stated extensions:
\[
 \langle A,(d^*d+dR_{\rm f}d^*+Q^*aQ)A\rangle
 \ge c\bigl(\|\nabla A\|_2^2+\|s^{-1}A\|_2^2\bigr).
 \tag{F0-E}
\]
The scalar and vector occurrences of \(d\) in this formula are respectively the site gradient and bond curl. They will be distinguished below when necessary. The projection \(R_{\rm f}\) is Balaban's nonlocal Landau projection, not the projection that simply subtracts each pillar mean.

## 2. F0 first: the seam calculation and the precise obstruction to a shortcut

Write \(D\) for the scalar gradient, \(C\) for the bond curl, and \(\Delta=D^*D\). All fine inner products have weight \(\eta^4\). A physical row of length \(s\) is
\[
 Q_cA=n^{-5}\sum_{v\in P_-}\sum_{t=0}^{n-1}
 A_\mu(v+t\eta e_\mu),\qquad n=s/\eta,
 \tag{2.1}
\]
where \(P_-\) contains \(n^4\) sites. Thus \(Q_c\mathbf a=a_\mu\) for a constant field. The dimensionless row is \(K_c=sQ_c\). The row mass form is \(\sum_c a_c s_c^2|Q_cA|^2\), with fixed upper and lower positive bounds on the dimensionless \(a_c\). In physical top pairing the diagonal in \(Q^*aQ\) is therefore \(a^{\rm phys}_c=a_cs_c^{-2}\). Constants below can absorb those fixed bounds. Formula (2.1) is the flat straight average underlying Balaban CMP 95; its dimensionless normalization is the outline's \(K\).

### 2.1 What changes at level zero

The CMP 96 p. 224 scan prints (2.3) with \(\Lambda_0=\Omega_1^c\) and says that the definitions apply to sites and bonds. The preceding paragraph defines a site's bond set by **touching** it. Complementing a bond set and taking the touching-bond set of the complementary sites are different operations. The scan alone must not be used to exchange these operations. Following the task, call the latter, inward-retaining choice the retained convention, and explicitly check the difference convention required by the consumer. The argument below uses the difference convention irrespective of the interpretation of that notation in the paper.

There is an immediate compatibility test. Let \(x\) be the inner endpoint of a bare inward bond, let \(w\ne x\) be another site in its level-1 pillar, and put \(\lambda(x)=1\), \(\lambda(w)=-1\), with zero elsewhere. Take a pillar along a flat face of a large cubical \(\Omega_1\); this is an admitted separated geometry. Then the mixed pillar average \(Q'\lambda\) is zero. For every default bare row, \(D\lambda\) is zero, since both endpoints are outside \(\Omega_1\). For a higher straight row,
\[
 Q_jD\lambda(c)=s_j^{-1}
 \bigl(\operatorname{mean}_{B^j(c_+)}\lambda-
       \operatorname{mean}_{B^j(c_-)}\lambda\bigr)=0.
 \tag{2.2}
\]
At an outward row, its outer block is a union of complete finer pillars, so the same equality holds. On the **additional** bare inward row ending at \(x\), however, \(D\lambda=\eta^{-1}\). Consequently one cannot retain those extra rows and at the same time import the identity \(QD\ker Q'=0\) with the unchanged scalar pillar kernel. This is an explicit counterexample to that particular identification, **not** to default F0. CMP 96 (2.28)–(2.34) uses the identity in its gauge change. Any reading of (2.3) that retains the inward rows must account for this before using that calculation.

For the default convention (2.2) proves the identity at every seam: interior endpoints use their own pillar means; an outward endpoint uses the mean of its \(L^4\) finer pillar means; bare rows have two bare endpoints. This is also the flat version of `a1-balaban.md` (7.20)–(7.22).

### 2.2 The omitted bonds are controlled by outward rows and the full gradient

Here is a uniform, explicit estimate, including the powers of \(\eta\). Put
\[
 M_{\rm miss}(A)=\eta^2\sum_{b\text{ crossing }\partial\Omega_1}|A(b)|^2,
 \qquad M_{\rm out}(A)=\sum_{c\text{ level-1 outward}}(L\eta)^2|Q_cA|^2.
\]
Then
\[
 M_{\rm miss}(A)\le 2L M_{\rm out}(A)
                  +160L^4\|\nabla A\|_2^2.
 \tag{2.3}
\]
To prove it, assign each crossing bare bond to the coarse face containing it, and hence to the outward row crossing that face. There are at most \(L^3\) assigned bonds per row. The parallel bonds read by that row lie in its rectangular double block. Any one of them can be joined to the assigned bond by moving its initial point along at most \(5L\) fine edges inside that rectangle. Telescoping and Cauchy–Schwarz give
\[
 |A(b)-A(b')|^2\le 5L\eta^2
           \sum_{e\text{ in the double block}}|\nabla_e A_\mu|^2.
\]
The coefficients in the physical row (2.1) are nonnegative and sum to one. Jensen's inequality therefore gives the same bound with \(A(b')\) replaced by \(Q_cA\). Use \(|u+v|^2\le2|u|^2+2|v|^2\), sum the at most \(L^3\) bonds, and multiply by \(\eta^2\). The row contribution is \(2L(L\eta)^2|Q_cA|^2\), and the gradient contribution is at most \(10L^4\eta^4\) times the indicated sum. For a fixed component each parallel double block overlaps at most two such blocks in its longitudinal direction and has disjoint transverse blocks; allowing all directions and the one-step derivative boundary gives overlap at most sixteen. This proves (2.3). The prescribed gap puts these double blocks inside \(\Omega_0\), so no unstated boundary extension enters this proof.

In particular deletion of the inward mass preserves comparability of the **full-gradient** forms
\(\|\nabla A\|_2^2+M_{\rm default}(A)\) and
\(\|\nabla A\|_2^2+M_{\rm retained}(A)\), uniformly in the mesh, depth and volume.

It does **not**, on its own, prove (F0-E). Indeed
\[
 \langle A,T_{\rm f}A\rangle
 =\|CA\|_2^2+\|R_{\rm f}D^*A\|_2^2+M_{\rm default}(A)
 =\|\nabla A\|_2^2-\|(I-R_{\rm f})D^*A\|_2^2
       +M_{\rm default}(A)
 \tag{2.4}
\]
on the whole torus. Substituting (2.3) in an old lower bound leaves a multiple of \(\|\nabla A\|_2^2\) on the wrong side with no absorption condition. A local full-gradient estimate is therefore not the Landau-vector coercivity theorem. Sections 6 and 8 establish that theorem for the actual row/projection pair. At a compressed outer boundary they use the bare mass estimate, so they do not assume that a compressed divergence obeys the uncompressed Hodge identity. No assertion below treats (2.3) as the vector theorem.

The relevant published proof starts with Balaban CMP 95 Proposition 1.1, (1.89)–(1.90), proceeds to its Proposition 1.2, then uses the two-scale decomposition CMP 96 (2.95)–(2.129), Proposition 2.5, and the walk (2.141) in Proposition 2.6. CMP 99b Theorems 3.1–3.3 explicitly reduce to those flat inputs. Its (3.48) and (3.132) are separate Gram-inverse conclusions. This dependency is stronger than finite-dimensional positivity.

## 3. Flat column bound: a complete counting proof

This part does not use a vector inverse. It proves D1 in the norm actually used by `a3-profile.md`. Credit T. Balaban for the straight average, and Sussman–Alpoge with Claude and Codex for the straightened \(K\) and this consumer formulation.

At fixed height \(j\), let \(n=L^j\). Differentiating the path sum with respect to a physical fine potential gives
\[
 K(c,b)=\eta n^{-4}N(c,b),
 \tag{3.1}
\]
where \(N(c,b)\) counts the starting sites whose oriented straight path uses \(b\). Only parallel rows contribute. The transverse coordinates of \(b\) belong to exactly one transverse block, and the longitudinal multiplicities for consecutive rows are the two complementary tents. Their sum is \(n\). One can see this without a formula for a tent: for each of the \(n\) possible starting offsets modulo \(n\), exactly one translated interval of length \(n\) contains the fixed bond. Thus, on the full height-\(j\) grid,
\[
 \sum_c |K(c,b)|=\eta n^{-3}=\eta^4s_j^{-3},
 \qquad \sum_b|K(c,b)|=\eta n=s_j.
 \tag{3.2}
\]
Deleting rows only reduces these sums. At \(j=0\) the formulas read \(K(c,b)=\eta\mathbf1_{c=b}\).

Put \(s_b=\mathsf L(b)\), the maximum pillar scale of the two endpoints. A retained row of scale \(s_j<s_b\) cannot read \(b\). Its two endpoint blocks are outside \(\Omega_{j+1}\), since inward rows are absent, and its parallel double block consists of those two complete blocks. Their union cannot contain an endpoint in a higher assigned pillar. Thus every contributing height has \(s_j\ge s_b\). This argument uses only aligned blocks; it also covers level zero. Summing (3.2) over the possibly contributing heights gives the stronger bound
\[
 \boxed{\displaystyle
   \sum_{c\in\mathbf B}|K(c,b)|
       \le {\eta^4s_b^{-3}\over1-L^{-3}}.}
 \tag{3.3}
\]
This uses a convergent geometric sum, not a count proportional to the depth. It is valid even without using the further separation fact that only neighboring heights can read one bond.

The same count with one extra source length gives
\(\sum_c s_c|K(c,b)|\le\eta^4s_b^{-2}/(1-L^{-2})\).
Jensen with the row sum \(s_c\) thus proves
\[
 \|KA\|_{\ell^2(\mathrm{rows})}^2
 \le\sum_b|A(b)|^2\sum_cs_c|K(c,b)|
 \le {1\over1-L^{-2}}\|m^{-1}A\|_2^2.
 \tag{3.5}
\]
This is the energy-to-row bound used later, with all its weights included.

The row multiplier has counting pairing, whereas the force has pairing \(\eta^4\sum_b\). Hence
\[
 (K^*\omega)(b)=\eta^{-4}\sum_c K(c,b)^{\mathsf T}\omega(c),
 \qquad
 |K^*\omega|_{(-3)}:=\sup_b s_b^3|(K^*\omega)(b)|
 \le {\|\omega\|_\infty\over1-L^{-3}}.
 \tag{3.4}
\]
All color components obey the same scalar calculation at \(U=1\). This is the flat D1 input, with its cell factor and force power restored. No propagator theorem, differentiability estimate or numerical enumeration is used.

To check that (3.1) is the iterated row, compose two averages. A starting site consists uniquely of its coarse subblock offset and its fine offset in that subblock. The successive straight segments concatenate into one straight segment of length equal to the product of the two block lengths. The two averaging factors multiply to the inverse fourth power of that product. Induction gives (3.1) for every height. At identity the site factors in the straightening cancel the endpoint contour terms, leaving precisely this path sum; this is the cancellation written in `a3-balaban.md` §8.4.

## 4. F1 and the scalar part of F0: differentiated sources

This section fills the differentiated-source portion left open in `a3-balaban.md` §13. It uses that file's **written scalar proofs**, not an unchecked literature theorem: the pillar Poincaré argument (7.10), weighted energy calculation (7.13)–(7.15), pointwise argument (7.19)–(7.20), and the scale summation proof in §5. Those arguments use no vector inverse. At \(U=1\) their covariant errors vanish. Credit T. Balaban, CMP 89 §2, CMP 95 (1.110)–(1.117), CMP 96 Proposition 2.2, and CMP 99b (3.42)–(3.47), for the regularity package and its source exponents. The following supplies the missing local argument instead of assuming that transposing a supremum estimate gives it.

Set \(S=(\Delta+V)^{-1}\), \(V=Q'^*m^{-2}Q'\), \(m=m_y\) on a pillar. Write
\(|g|=\|g\|_\infty\), and take the source Hölder seminorm on the actual fine field, including its zero extension off its support. A seminorm only on the interior of the supporting pillar would omit jumps and is not the norm proved here or in Balaban's displayed global Hölder definition (CMP 95 (1.109), scan p. 35).

The scalar local positivity used below can also be seen directly. Average coordinate-ordered paths between two sites of a pillar of side \(s\). Telescoping and Cauchy–Schwarz give
\(\|u-\operatorname{Av}u\|_{2,P}^2\le2s^2\|Du\|_{2,P}^2\): a path has at most \(4s/\eta\) edges, and an edge dividing a coordinate line into \(a\) and \(n-a\) sites is used by \((|P|/n)2a(n-a)\le |P|n/2\) pairs. The physical factors restore \(s^2\). Summing disjoint pillars gives
\[
 \|m^{-1}u\|_2^2\le C\left(\|Du\|_2^2+
                           \sum_Pm_P^2|\operatorname{Av}_P u|^2\right).
 \tag{4.0}
\]
Bare pillars are controlled directly by their identity average. This proves scalar positivity and the one/two-scale local energy inverses without a propagator premise. The scalar parametrix of §8 can be applied both in this first-order energy space and in \(H^2_m\). In the first-order version its commutator is estimated by one summation by parts; the same bounds (8.6)–(8.9) apply. It consequently gives (7.15), including differentiated sources, as a separate derivation of the scalar energy input used here. The construction needs only (4.0) and the local bump bound (5.1), so it does not depend circularly on the pointwise conclusions of this section.

### 4.1 The free local estimate, including its cancellation

For an embedded cube of side comparable to \(r\ge16\eta\), suppose
\(\Delta u=D^*g+F\) on a fixed enlargement. On a smaller concentric cube the following bounds hold:
\[
 \begin{aligned}
 |u|+r^\alpha[u]_\alpha
 &\le C_\alpha\{r^{-2}\|u\|_{2,\rm outer}
                         +r|g|+r^2|F|\},\\
 |Du|+r^\beta[Du]_\beta
 &\le C_{\epsilon,\beta}\{r^{-3}\|u\|_{2,\rm outer}
             +|g|+r^\epsilon[g]_\epsilon+r|F|\},
 \quad 0<\alpha<1,\quad0<\beta<\epsilon<1.
 \end{aligned}                                                    \tag{4.1}
\]
The second line is used only when \(g\) has the indicated Hölder norm.

Here are the kernel and harmonic details. In units \(\eta=1\), the full-space Green kernel has Fourier symbol
\(\lambda(p)^{-1}\), \(\lambda(p)=4\sum_\nu\sin^2(p_\nu/2)\). For \(q=0,1,2,3\),
\[
 |D^qG(x)|\le C_q(1+|x|_\infty)^{-2-q}.             \tag{4.2}
\]
For \(|x|=R>4\), split the Fourier integral at frequency \(R^{-1}\). The low-frequency integral is bounded by
\(C\int_0^{2/R} t^{q-2}t^3dt\le CR^{-q-2}\).
In the complementary integral integrate by parts \(q+3\) times in a coordinate attaining \(R\). The differentiated symbol is bounded by \(C|p|^{-5}\); its radial integral above \(R^{-1}\) is \(O(R)\). Multiplication by \(R^{-q-3}\) gives the same bound. Cutoff derivatives have that bound by scaling; periodicity cancels boundary terms. At bounded \(R\), direct integrability of the symbol gives (4.2). This is the argument of `a3-balaban.md` (12.1), here extended to the third difference needed below. Rescaling gives
\(|D^qG_\eta(x)|\le C(|x|+\eta)^{-2-q}\) for kernel **densities**.

Multiply \(g,F\) by a smooth sampled cutoff which is one on an intermediate cube and zero outside the outer cube. Its differences are bounded by \(C/r\) and \(C/r^2\). Define
\(v=G_\eta*(D^*(\chi g)+\chi F)\). Finite summation by parts moves \(D^*\) onto the kernel, so (4.2) and shell counting give
\(|v|\le C(r|g|+r^2|F|)\) in the intermediate cube. For its difference at points distance \(h\le r\), the near shells have total at most \(C h|g|\); in the far shells telescope the kernel and sum
\(C h|g|\int_h^{Cr}t^{-1}dt\). The term from \(F\) is smaller by an additional factor \(r\). Since
\((h/r)^{1-\alpha}(1+\log(r/h))\) is bounded, this proves the first Hölder bound for \(v\).

For \(Dv\), the differentiated-source kernel is \(K=D D^*G_\eta\), with \(|K(x)|\le C(|x|+\eta)^{-4}\). Its constant part must be cancelled. For a cutoff \(\zeta(x/r)\), equal to one near zero and compactly supported,
\[
 \left|\sum_x\eta^4K(x)\zeta(x/r)\right|
 =\left|\sum_x\eta^4G_\eta(x)DD^*\zeta(x/r)\right|\le C.
 \tag{4.3}
\]
The differences of \(\zeta\) lie at distances comparable to \(r\); the three factors in the last sum have sizes \(r^{-2},r^{-2},r^4\). Subtract \(g(x)\) in the near part of the convolution. Its remaining absolute sum is bounded by
\(C[g]_\epsilon\int_\eta^{Cr}t^{\epsilon-1}dt\le C_\epsilon r^\epsilon[g]_\epsilon\); (4.3) bounds the constant part. For two output points distance \(h\), split at \(4h\). The near contribution is at most \(C_\epsilon[g]_\epsilon h^\epsilon\). In the far contribution the third-difference bound in (4.2) gives
\[
 C h[g]_\epsilon\int_h^{Cr}t^{\epsilon-2}dt
 \le {C\over1-\epsilon}[g]_\epsilon h^\epsilon.
\]
Cutoff terms contribute at most \(C|g|h/r\), and the change in the subtracted constant is bounded by (4.3) times \([g]_\epsilon h^\epsilon\). Multiplication of the source by \(\chi\) replaces its seminorm by at most
\(C([g]_\epsilon+r^{-\epsilon}|g|)\).
This proves the second line of (4.1) for the \(g\) part, with any \(\beta<\epsilon\). For the \(F\) part use \(DG_\eta\), split its difference in the same way, and obtain
\(C|F|h(1+\log(r/h))\le C_\beta r^{1-\beta}|F|h^\beta\).

On the intermediate cube \(h_0=u-v\) is harmonic. The elementary discrete harmonic estimate is
\[
 |D^q h_0|_{\rm inner}\le C_q r^{-2-q}\|h_0\|_{2,\rm intermediate},
 \qquad q=0,1,2.
 \tag{4.4}
\]
One verification, avoiding a Sobolev endpoint, is the following. In one dimension write the value as the average plus a sum of first differences, giving
\(|f(x)|\le C(r^{-1}\sum|f|+\sum|Df|)\). Apply this identity successively in four directions. A mixed difference of order \(j\) has coefficient \(Cr^{-(4-j)}\); Cauchy–Schwarz contributes \(Cr^2\). For a harmonic function, summation by parts against \(\chi^2h_0\) and \(2ab\le\frac12a^2+2b^2\) gives
\(\|Dh_0\|_{2,\rm smaller}\le Cr^{-1}\|h_0\|_{2,\rm larger}\).
Differences of a harmonic function are harmonic on the smaller cube. Apply the last inequality successively on nested cubes to each of the mixed differences. Every term is bounded by \(Cr^{-2}\|h_0\|_2\). Applying the result to its first and second differences gives (4.4); reserve a fixed number of mesh steps for these nested cubes. The remaining cubes of bounded mesh size follow directly from the pointwise \(\ell^2\) bound. The second derivative in (4.4), followed by telescoping, supplies the Hölder estimate for \(Dh_0\). Finally \(\|v\|_2\le Cr^2\sup|v|\). These facts prove all of (4.1).

### 4.2 Application to the mixed scalar inverse

Let \(g\) be supported over \(y'\), and put \(u=SD^*g\). The scalar weighted energy proof (7.15) gives
\[
 \|u\|_{2,P}\le C m_P m_{y'}^2e^{-\mu d(P,y')}|g|.
 \tag{4.5}
\]
On any neighboring pillar,
\[
 |Vu|_P=m_P^{-2}|\operatorname{Av}_P u|
 \le m_P^{-4}\|u\|_{2,P}.
 \tag{4.6}
\]
At a non-bare output take the cubes in (4.1) with \(r\) a sufficiently small fixed multiple of \(m_y/L\). Separation puts their read sets in \(\Omega_0\), and all the pillars they meet have scales between fixed \(L\)-dependent multiples of \(m_y\). Use \(F=-Vu\) in (4.1). Equations (4.5)–(4.6), summed over this bounded collection of pillars, bound the \(u,F\) terms by the required output powers times
\((m_{y'}/m_y)^2e^{-\mu d(y,y')}|g|\).
The scale-distance inequality in `a3-balaban.md` (5.2) absorbs that ratio at a fixed loss of rate. If the source meets the local cube, its scale is comparable to \(m_y\) and its distance to \(y\) is bounded; if it does not, the local \(g\) terms in (4.1) vanish. For output differences longer than \(r\), twice the value or gradient bound gives the same local Hölder estimate with an \(L\)-dependent constant.

At a bare output, use \(|u(x)|\le\eta^{-2}\|u\|_{2,\{x\}}\) in (4.5), and then the finitely many neighboring values for each difference. Adjacent scales differ by at most \(L\). This proves the same estimates at an arbitrary outer boundary without assuming that an interior cube fits there. We have obtained
\[
 \begin{aligned}
 |SD^*g|_y&\le C m_y e^{-\delta d(y,y')}|g|,\\
 [SD^*g]_{\alpha,y}&\le C_\alpha m_y^{1-\alpha}e^{-\delta d(y,y')}|g|,\\
 |DSD^*g|_y+m_y^\beta[DSD^*g]_{\beta,y}
 &\le C_{\epsilon,\beta}e^{-\delta d(y,y')}
             (|g|+m_{y'}^\epsilon[g]_\epsilon),
 \qquad0<\beta<\epsilon<1.
 \end{aligned}                                                   \tag{4.7}
\]
The source cutoff, when used, is included in its Hölder norm. Taking \(\epsilon=\beta+\varepsilon<1\) gives the precise exponent arrangement in F0 (3.22). Together with the already written scalar energy and output estimates, (4.7) proves **F1 at the flat reference**, and the scalar inverse members of F0, on the stated default class. No assertion about the vector inverse is used in this conclusion.

## 5. F2: weights and the scalar projection

The already reconstructed scalar Gram argument can be used without altering the seam convention. For clarity, here is its normalization and the actual chain of estimates. Put
\(J_s=Q'S^2Q'^*\), \(N=J_s^{-1}\). Top inner products have weight \(m_y^4\). A smooth bump supported strictly inside each non-bare pillar, normalized to average one, has second differences bounded by \(Cm_y^{-2}\). At a bare pillar use the point field. Bumps and their one-step enlargements have bounded overlap. For their sum \(F_b\),
\[
 Q'F_b=b,\qquad
 \|(\Delta+V)F_b\|_2\le C\Big(\sum_y|b_y|^2\Big)^{1/2}.
 \tag{5.1}
\]
These are precisely the bump construction and counts in `a3-balaban.md` (7.11): sample a fixed smooth profile supported in the middle half of the cube, divide by its average, and integrate its first two ordinary derivatives over mesh intervals. Its average has a fixed positive lower bound once the pillar has at least 33 sites per side. For a smaller non-bare pillar use its central point field times the number of sites. Its ratio of side to mesh is below 33, so the same two graph-norm bounds hold with one larger absolute constant; no enumeration is required. Pair \(SQ'^*\chi\) with \((\Delta+V)F_b\), and take the supremum over counting-unit vectors \(b\). The functional on the left has counting norm \((\sum m_y^8|\chi_y|^2)^{1/2}\). Thus
\[
 \langle\chi,J_s\chi\rangle_{\rm top}
       \ge c\sum_y m_y^8|\chi_y|^2.                 \tag{5.2}
\]
Weighted scalar energy bounds give
\[
 |J_s(y,z)|_{\rm count}\le C m_y m_z^3e^{-\mu d(y,z)}.
 \tag{5.3}
\]
For example \(\|\mathbf1_wSQ'^*e_z\|_2\le Cm_wm_z^3e^{-\mu d(w,z)}\); pair the two such columns and divide by \(m_y^4\). The sum over \(w\) is bounded by the explicitly proved scale-volume sum in `a3-balaban.md` §5, giving (5.3).

In counting coordinates \(J=J_s m^{-4}\) is symmetric, \(J\ge cI\), and its entries, with a reduced rate, obey \(|J(y,z)|\le Ce^{-\nu d(y,z)}\). Both Schur sums are bounded. For \(v_y=e^{\theta d(y,z_0)}\),
\[
 |(vJv^{-1}-J)(y,z)|
 \le C\theta d(y,z)e^{-(\nu-\theta)d(y,z)}.
\]
The two Schur sums are at most \(C'\theta\). Choose \(\theta<\nu/2\) and \(C'\theta<c/2\); the geometric inverse series gives
\(\|(vJv^{-1})^{-1}\|_{2\to2}\le2/c\). Apply it to \(e_{z_0}\). Therefore
\[
 |N(y,z)|_{\rm count}\le Cm_y^{-4}e^{-\theta d(y,z)}.
 \tag{5.4}
\]
The upper Schur bound on \(J\), combined with (5.2), also gives the upper scalar Gram form in F0. Its two sides are exactly \(c\|m^2\chi\|_{\rm top}^2\) and \(C\|m^2\chi\|_{\rm top}^2\), not unweighted top norms.

Let \(F_a=SQ'^*e_a\). The density of \(P=I-R\) is
\[
 P(x,x')=\sum_{a,b}F_a(x)N(a,b)_{\rm count}m_b^{-4}F_b(x')^*.
 \tag{5.5}
\]
The scalar value and gradient bounds give \(|D^rF_a|_y\le Cm_y^{2-r}e^{-\mu d(y,a)}\), \(r=0,1\), and the corresponding gradient Hölder bounds. Inserting (5.4) in (5.5), the two intermediate powers are \(m_a^{-4}m_b^{-4}\). Move them to the matching output scales, using \(|\log_L(m_a/m_y)|\le1+d(a,y)/\rho\), and sum the remaining exponentials. This yields
\[
 |D_x^rP(x,x')(D_{x'}^*)^t|
 \le C m_y^{-2-r}m_z^{-2-t}e^{-\delta d(y,z)},
 \qquad r,t\in\{0,1\}.                              \tag{5.6}
\]
An endpoint Hölder quotient lowers that endpoint's power by its exponent; the same product calculation proves it. This recovers F2, including its density/counting distinction, and the scalar Gram-kernel part of F0. The scale sum fixes a lower bound on the separation **after** the chosen decay rates and finite set of powers. Equation (5.6) by itself is not a comparison theorem between different sequences.

## 6. F0/F3 vector coercivity: one scale, then a default seam

This section reconstructs the energy part of Balaban CMP 95 Proposition 1.1 and CMP 96's two-scale reduction. It proves more than (2.3): coercivity of the actual Landau form on a periodic **two-scale** model, with the inward rows omitted. Section 8 assembles the many-scale inverse from these models.

### 6.1 Uniform one-scale form

Normalize the coarse spacing to one and let the fine spacing be \(h=1/n\), \(n=L^j\). Bloch transformation over the coarse torus decomposes the physical \(\ell^2\) space into coarse momenta \(\vartheta\in[-\pi,\pi]^4\). In a fiber the fine momenta are \(p_\ell=\vartheta+2\pi\ell\) lying in its fine Brillouin zone. Write
\[
 d_\mu(p)={e^{ihp_\mu}-1\over h},\quad
 \omega(p)=\sum_\mu|d_\mu(p)|^2,\quad
 d_{c,\mu}=e^{i\vartheta_\mu}-1.
\]
The scalar average has coefficients
\(q_\ell=n^{-4}\sum_{x\in B}e^{ip_\ell\cdot x}\).
The physical vector average in component \(\mu\) has coefficients
\[
 q_{\mu,\ell}=q_\ell,{d_{c,\mu}\over d_\mu(p_\ell)},
 \tag{6.1}
\]
interpreted by the finite geometric sum when numerator and denominator vanish. This follows directly by summing the straight path in (2.1).

The elementary estimates needed below are uniform in \(n\):
\[
 \sum_\ell|q_\ell|^2=1,\quad
 |q_0|\ge(2/\pi)^4,\quad
 \sum_{\ell\ne0}|q_\ell|^2\le C|\vartheta|^2,
 \quad\|Q\|_{2\to2}\le1.                            \tag{6.2}
\]
The first identity is Parseval for the normalized block indicator. For the second, in each direction the absolute value is
\(|\sin(\vartheta_\mu/2)/(n\sin(\vartheta_\mu/(2n)))|\ge2/\pi\).
For the third, expand the square of the block average and use
\(1-\cos t\le t^2/2\), with both points in a unit cube. The final bound follows by Jensen in the path average and summing its column weights with physical cell volumes; the complementary tents sum to one after that conversion. Also
\(c|p|^2\le\omega(p)\le|p|^2\) in the fine Brillouin zone, and \(\omega(p_\ell)\ge c\) for \(\ell\ne0\).

For \(\vartheta\ne0\), set \(v_\ell=\overline q_\ell/\omega(p_\ell)\), \(B=\sum|v_\ell|^2\). The scalar formula for \(P\) reduces in this fiber to the rank-one orthogonal projection onto \(v\). This follows either by solving \((\Delta+aQ'^*Q')S Q'^*=Q'^*\), or by observing that multiplication of \(\Delta^{-1}Q'^*\) by a scalar does not change its range. Let \(W\) be multiplication by \(\omega(p_\ell)\) on vector components, and put \(g_\ell=d(p_\ell)v_\ell\). Then the vector form is exactly
\[
 E(A)=\|W^{1/2}A\|^2-{ |\langle g,A\rangle|^2\over B}
                              +a\|QA\|^2.           \tag{6.3}
\]
Here \(a\) lies in a fixed compact subinterval of \((0,\infty)\). The first two terms are nonnegative, since
\(\|W^{-1/2}g\|^2=B\).

First suppose \(|\vartheta|\ge t_0>0\). Their null vector is
\(z_\ell=d(p_\ell)\overline q_\ell/\omega(p_\ell)^2\), and
\[
 \|W^{1/2}z\|^2=B,\qquad Qz=d_cB,\qquad
 {|Qz|^2\over B}=|d_c|^2B\ge c>0.                  \tag{6.4}
\]
The last bound uses the \(\ell=0\) term, (6.2),
\(\omega(p_0)\le|\vartheta|^2\), and
\(|d_c|^2\ge(4/\pi^2)|\vartheta|^2\), with \(|\vartheta|\le2\pi\).
Write \(A=\alpha z+A_\perp\), orthogonally in the \(W\) inner product. The first two terms of (6.3) equal \(\|W^{1/2}A_\perp\|^2\). Since \(W\ge c t_0^2\),
\(\|QA_\perp\|\le C_{t_0}\|W^{1/2}A_\perp\|\).
Equation (6.4) and \(\alpha Qz=QA-QA_\perp\) bound \(|\alpha|\sqrt B\) by \(C_{t_0}E(A)^{1/2}\). This controls both \(\|A\|\) and \(\|W^{1/2}A\|\).

For \(0<|\vartheta|<t_0\), split off \(A_0\) and write \(A_h\) for all other aliases. The squared norm of the high part of \(W^{-1/2}g/\sqrt B\) is at most \(C|\vartheta|^6\): its numerator is at most \(C|\vartheta|^2\) by (6.2), while \(B\ge c|\vartheta|^{-4}\). Expanding the rank-one square in (6.3) and using \(2ab\le\frac14a^2+4b^2\) gives
\[
 E(A)\ge\tfrac12\|W^{1/2}A_h\|^2
             -C|\vartheta|^8|A_0|^2+a\|QA\|^2
 \tag{6.5}
\]
once \(t_0\) is small enough. The diagonal low-alias coefficients \(q_{\mu,0}\) are bounded away from zero for these \(\vartheta\), by (6.1)–(6.2). Thus
\(|A_0|^2\le C(\|QA\|^2+\|A_h\|^2)\).
Choose \(t_0\) smaller so that the negative term in (6.5) is absorbed by half of its two positive terms. This again bounds \(\|A\|^2+\|W^{1/2}A\|^2\). At \(\vartheta=0\), \(P\) is the projection onto the constant scalar alias; \(DP=0\), and \(Q\) reads exactly the constant vector alias. The same conclusion follows directly. Parseval now proves
\[
 \|A\|_2^2+\|\nabla A\|_2^2\le C E(A)              \tag{6.6}
\]
uniformly in the fine mesh and the periodic volume. This is a hand proof; no frequency grid is enumerated.

A useful consequence is a bounded one-scale Landau lift \(H\). In each fiber, prescribe only the low alias by \(A_{\mu,0}=B_\mu/q_{\mu,0}\), and set the other aliases to zero. The same sine estimate shows \(|q_{\mu,0}|\ge(2/\pi)^5\) on the whole coarse Brillouin zone. This is a right inverse with \(H^1\) norm bounded by \(C\|B\|_2\). Minimize the positive form with \(QA=B\). A variation \(D\lambda\), \(Q'\lambda=0\), leaves curl and rows unchanged; its unique minimum has \(RD^*A=0\). By (6.6) the minimizer \(HB\) obeys
\[
 \|HB\|_{H^1}\le C\|B\|_2.                         \tag{6.7}
\]
It also minimizes the curl energy in that slice, since the row mass is fixed.

### 6.2 Two scales, with only outward seam rows

Use the preceding unit coarse lattice as the finer of two **row** scales; its underlying fine mesh is still arbitrary. Let \(q,q'\) be its uniform vector and scalar averages. Mark an arbitrary union of blocks of side \(L\) in the unit lattice. On that unit lattice let \(P_s\) retain each outside site and average each marked block. Let \(U\) retain outside bonds having neither endpoint in a marked block, and the interior/outward length-\(L\) rows. Thus the actual mixed averages are \(Q=Uq\), \(Q'=P_sq'\). In particular no inward unit bond is retained.

Let \(R_s\) project onto \(\Delta\ker q'\), and \(R\) onto \(\Delta\ker(P_sq')\). Define \(H'\omega\) as the minimizer of \(\|\Delta\lambda\|_2^2\) subject to \(q'\lambda=\omega\), fixing the constant by this condition. The minimum exists and is unique: \(\Delta\) is injective on \(\ker q'\), and the spaces are finite dimensional. Its variational equation gives
\(\Delta H'\omega\perp\Delta\ker q'\).
Every element of \(\ker(P_sq')\) is uniquely a sum of an element of \(\ker q'\) and \(H'\omega\), \(P_s\omega=0\). Consequently
\[
 R=R_s+R_+,\qquad
 \operatorname{ran}R_+=\Delta H'(\ker P_s),\qquad R_sR_+=0.
 \tag{6.8}
\]

For any fine \(A\), solve \(\Delta\lambda_s=R_sD^*A\) with \(q'\lambda_s=0\), and decompose
\[
 A=H B+a+D\lambda_s,\quad B=qA,\quad qa=0,\quad R_sD^*a=0.
 \tag{6.9}
\]
The one-scale scalar Poincaré inequality and
\(\|\nabla D\lambda_s\|_2=\|\Delta\lambda_s\|_2\) give
\(\|D\lambda_s\|_{H^1}\le C\|R_sD^*A\|_2\).
Stationarity of \(HB\) makes \(CHB\perp Ca\), and (6.6) on \(a\) gives \(\|a\|_{H^1}\le C\|Ca\|_2\).

The uniform coarse curl is a contraction of the fine curl:
\[
 \|C_1qA\|_2\le\|CA\|_2.                           \tag{6.10}
\]
Indeed, telescope the four averaged paths around a coarse plaquette. Interior edges cancel and leave the average of the fine plaquettes of the translated spanning rectangles, divided by their area. Its coefficients are nonnegative and sum to one. At a fixed fine plaquette the two longitudinal tents in each of the two plaquette directions partition the total weight; the other directions partition into transverse blocks. After multiplication by the coarse volume their column sum is the fine volume. Jensen followed by summation proves (6.10). Applying it to \(HB\) bounds \(\|C_1B\|_2^2\) by \(\|CHB\|_2^2\).

On the unit lattice perform strict tree gauge inside each marked block. If \(t(x)\) is the coordinate-tree integral from that block's root to \(x\), set \(\omega=t-\operatorname{Av}t\) there and \(\omega=0\) outside. Then \(P_s\omega=0\), and
\(B_{\rm ax}=B-D_1\omega\) vanishes on those tree bonds. The endpoint-mean identity (2.2) gives \(UB_{\rm ax}=UB\). The elementary block/face estimate proved in §7 below, including its nonzero-row version, is
\[
 \|B_{\rm ax}\|_2^2\le C_L\bigl(\|C_1B\|_2^2+M_U(B)\bigr).
 \tag{6.11}
\]
Here \(M_U\) includes the bare outside bonds and \(L^2|Q_LB|^2\) on the coarse rows, so it is precisely the mixed mass.

The identity
\[
 H D_1\omega=D H'\omega                              \tag{6.12}
\]
has a direct uniqueness proof. The right side has average \(D_1\omega\), curl zero, and \(R_sD^*DH'\omega=0\) by the defining orthogonality of \(H'\). Thus it is the one-scale Landau minimizer. Put \(A''=HB_{\rm ax}+a\). Equations (6.7), (6.9)–(6.11) bound \(\|A''\|_{H^1}\) by \(C_L E_{\rm mix}(A)^{1/2}\), where
\[
 E_{\rm mix}(A)=\|CA\|_2^2+\|RD^*A\|_2^2+M_U(qA).
\]
Using (6.8), (6.9), and (6.12),
\[
 \Delta H'\omega=R_+D^*(A-A''),
 \qquad
 \|\Delta H'\omega\|_2\le C_L E_{\rm mix}(A)^{1/2}.
 \tag{6.13}
\]
Since \(P_sq'H'\omega=0\), scalar pillar Poincaré on blocks of size at most \(L\) gives
\(\|H'\omega\|_2\le C_L\|DH'\omega\|_2\).
Pair with \(\Delta H'\omega\) to obtain
\(\|DH'\omega\|_2\le C_L\|\Delta H'\omega\|_2\); the full-lattice difference identity controls its first gradient by the same quantity. Equations (6.9), (6.12)–(6.13) now prove
\[
 \boxed{\ \|A\|_2^2+\|\nabla A\|_2^2
                  \le C_L E_{\rm mix}(A).\ }        \tag{6.14}
\]
The local scale takes values \(1,L\), so (6.14) implies, and is equivalent up to \(L\)-dependent constants to, the energy norm with \(m^{-1}A\). Restoring the smaller physical row scale rescales both sides correctly. This includes the level-0 seam by setting the underlying fine spacing equal to that smaller row scale. It uses no inward mass, and the projection is the actual one in the consumer's definition.

## 7. The unit-lattice block estimate and the strict-axial part of F4

Credit T. Balaban, CMP 96 pp. 244–246, (2.123)–(2.128), Lemma 2.4, and pp. 249–250, (2.152)–(2.157). The OCR at (2.128) drops factors; the reconstruction below proves the power \(L^{-d-1}\) directly. At \(d=4\) it is the consumer's \(L^{-5}\).

Work on the unit lattice. Partition it into blocks of side \(L\). A strict coordinate tree joins the root to each site in coordinate order. Suppose \(B\) vanishes on all those tree bonds. Write \(F=CB\) and \(K_c=LQ_c\) for the dimensionless one-step straight average. Then
\[
 \|B\|_2^2\le C_d L^{d+1}\|F\|_2^2
                    +2L^{d-1}\sum_c|K_cB|^2.
 \tag{7.1}
\]
The harmless factor 2 can be increased by a dimension-only constant if both orientations are counted. We count each positive bond and plaquette once.

For an internal bond, its value equals the circulation around that bond and the two root paths. Cancel the common coordinate segments. Moving the one remaining bond through the later coordinate segments sweeps at most \((d-1)(L-1)\) plaquettes, each with coefficient of magnitude one. Therefore
\(|B(b)|^2\le dL\sum_{p\subset\text{its block}}|F(p)|^2\).
There are at most \(dL^d\) internal bonds in a block. Their total is at most \(d^2L^{d+1}\) times that block's curl norm squared. This deliberately crude count already has the required power.

For a face bond \(b\) between two blocks, join their roots through \(b\) and the two tree paths. Its path integral is \(B(b)\). For every starting site \(u\) in the first block, use instead the two tree paths and the straight path from \(u\) to \(u+Le_\mu\). Its integral is that straight-path integral. Their difference is a closed rectilinear loop in the rectangular double block, with at most \(4d+2\) straight coordinate segments.

Here is a bounded filling, including multiplicities. Project a closed rectilinear loop successively onto the lower coordinate faces of its enclosing rectangle. Sweeping one straight segment under one coordinate projection produces one rectangle of plaquettes; the connector edges cancel between consecutive segments. After all coordinate projections the loop is zero. Thus the original loop is the boundary of at most \(d(4d+2)\) rectangles. Every rectangle lies in the double block, each has area at most \(4L^2\), and each plaquette has multiplicity at most \(d(4d+2)\). Weighted Cauchy–Schwarz consequently bounds the squared circulation by \(C_dL^2\sum_{p\text{ in double block}}|F(p)|^2\). Average over \(u\), and use Jensen. The averaged straight-path integral is exactly \(K_cB\), so
\[
 |B(b)-K_cB|^2\le C_dL^2
                    \sum_{p\text{ in double block}}|F(p)|^2.
 \tag{7.2}
\]
There are \(L^{d-1}\) face bonds. Sum (7.2), use \(|a+b|^2\le2|a|^2+2|b|^2\), and sum the faces. Each block belongs to at most \(2d\) such double blocks. Increasing \(C_d\) gives (7.1). The argument is an exact discrete Stokes calculation; it uses no plaquette enumeration by a program.

For the marked-block geometry of §6.2, impose tree gauge only in the marked blocks. Internal unmarked bonds are already controlled by the bare part of \(M_U\). At a face with one unmarked neighbor, the root paths in that neighbor no longer have zero integral. Each has at most \(dL\) unit bonds, all unmarked and hence retained bare bonds. Cauchy–Schwarz bounds each squared path integral by \(dL\) times that unmarked block's bare norm squared. Summing the \(L^{d-1}\) face bonds and the average over starting sites costs at most \(C_dL^d\) times that same norm. Each unmarked block borders at most \(2d\) marked blocks. All other terms are the ones just counted in (7.1)–(7.2). Coarse face averages are retained **outward** rows. This proves (6.11) with a constant depending on \(L,d\), and supplies the missing step in (6.14).

In particular, on a union of unit-lattice blocks, extend \(B\) by zero outside, keep every relevant outward one-step average, and impose strict tree gauge and \(Q_1B=0\). Formula (7.1) gives
\[
 \|CB\|_2^2\ge c_d L^{-d-1}\|B\|_2^2.
 \tag{7.3}
\]
For the **uniform** \(k\)-step effective action \(E_k\), its variational definition and (6.10) give
\[
 \langle B,E_kB\rangle
 =\min_{q_kA=B}\|CA\|_2^2\ge\|C_1B\|_2^2.
 \tag{7.4}
\]
The minimization is modulo fine gauge; choosing the Landau representative leaves its value unchanged. Existence follows from the positive one-scale form and the right inverse in §6.1. Completing the square in that form gives
\(E_k=(q_kG_kq_k^*)^{-1}-a\), with the physical top pairing. Equations (7.3)–(7.4) prove the strict-axial, uniform-lattice version of F4's gap, with exactly \(c_4L^{-5}\), for every support subset and every additional linear conditioning constraint: restricting a quadratic-form inequality preserves it.

For completeness, its pivot coordinates have a uniform norm comparison at fixed \(L\). Remove the tree variables. On each face choose the central crossing bond as the pivot. Its coefficient in \(K_c\) is \(L^{1-d}\), whereas all other coefficients have magnitude at most that. A face pivot is read by no other one-step row: the adjacent longitudinal tent vanishes there, the transverse blocks are disjoint, and other components are different. Solving \(K_cB=0\) expresses that pivot as a sum of at most \(2L^d\) remaining variables with coefficients of magnitude at most one. Each remaining variable is read by a bounded number of neighboring rows. For the resulting local embedding \(I_{\rm piv}\),
\[
 \|z\|_2\le\|I_{\rm piv}z\|_2\le C_L\|z\|_2,
 \qquad
 I_{\rm piv}^*E_kI_{\rm piv}\ge c_4L^{-5}I.
 \tag{7.5}
\]
The lower norm bound holds because the free coordinates are unchanged. Removing further free coordinates preserves both bounds. The upper bound follows by Cauchy–Schwarz in each pivot formula and the stated overlap count. This is Balaban's local elimination mechanism in (2.155)–(2.157), with its constants exposed.

This section proves the strict-axial **gap** for the uniform \(q_k\) problem. Section 10 supplies the additional mixed-row identification, the separate soft-contour argument, and the conditional covariance kernel. The mixed identification is needed; it does not follow merely from giving two effective actions the same symbolic name.

## 8. A local system for the many-scale assembly

Credit T. Balaban for the scalar projection identity, the two-scale reduction and the partition-of-unity walk method (CMP 96 (2.17), (2.95)–(2.141)). The following local saddle system is an explicit way to carry those arguments over without silently treating the global projection as a local coefficient.

Let \(A_s=\Delta+Q'^*m^{-2}Q'\), and distinguish the scalar average \(Q'\) from the physical vector average \(Q\). Set
\(B_v=C^*C+DD^*+Q^*aQ\).
On a periodic interior model this is the component Laplacian plus the vector row mass. With matched boundary spaces retain the displayed compressed operators themselves. Consider the symmetric block matrix
\[
 \mathbb M=
 \begin{pmatrix}
 B_v&-D&0&0\\
 -D^*&I&A_s&0\\
 0&A_s&0&-Q'^*\\
 0&0&-Q'&0
 \end{pmatrix},
 \qquad X=(A,h,\lambda,\mu).
 \tag{8.1}
\]
Every coefficient is local: a fine differential stencil, a scalar pillar average, or a vector straight average on its double block. In particular \(R\) is not a coefficient of (8.1).

Eliminate the last three variables with source \((f,0,0,0)\). They give
\(h+A_s\lambda=D^*A\), \(A_sh=Q'^*\mu\), \(Q'\lambda=0\). Hence
\[
 h=SQ'^*(Q'S^2Q'^*)^{-1}Q'SD^*A=P D^*A,
 \quad (B_v-DPD^*)A=f.
 \tag{8.2}
\]
The Schur complement is exactly \(T=C^*C+DRD^*+Q^*aQ\). Invertibility of (8.1), with a uniform bound in the spaces below, will therefore prove the missing vector estimate.

### 8.1 Spaces and the local inverse bound

Use physical pairings and the norms
\[
 \begin{aligned}
 \|A\|_{E}^2&=\|\nabla A\|_2^2+\|m^{-1}A\|_2^2,\\
 \|\lambda\|_{H^2_m}^2&=
  \|m^{-2}\lambda\|_2^2+\|m^{-1}D\lambda\|_2^2
                       +\sum_{\alpha,\beta}\|D_\alpha D_\beta\lambda\|_2^2,\\
 \|X\|_{\mathcal X}^2&=
       \|A\|_E^2+\|h\|_2^2+\|\lambda\|_{H^2_m}^2
                                      +\|m^2\mu\|_{\rm top}^2.
 \end{aligned}                                                    \tag{8.3}
\]
Use zero extensions in the derivative norms at a Dirichlet boundary. At neighboring sites the choices of \(m\) differ by at most \(L\), so choosing the larger endpoint scale on bonds changes only \(L\)-dependent constants. The four source spaces are the corresponding duals: \(E^*\), \(L^2\), \((H^2_m)^*\), and the top norm \(\|m^{-2}g_3\|\). All four unknown norms have the same scaling when \(h\) has the dimension of \(DA\), \(\lambda\) that of \(mA\), and \(\mu\) that of \(m^{-3}A\).

On a one- or two-scale periodic model, normalize its smaller row scale to one. Then \(1\le m\le L\), and §6 proves the vector inverse bound \(G:E^*\to E\). Scalar Poincaré gives \(S:L^2\to H^1\). Since \(V\) is bounded on \(L^2\), \(\Delta Sf=f-VSf\) is bounded in \(L^2\); the Fourier identity
\(\sum_{\alpha,\beta}\|D_\alpha D_\beta u\|_2^2=\|\Delta u\|_2^2\)
therefore gives \(S:L^2\to H^2\). Transposition gives \(S:H^{-2}\to L^2\). The smooth scalar lift in (5.1) gives the row bound for \(N=(Q'S^2Q'^*)^{-1}\). These constants depend on \(L\), not on the underlying fine mesh or periodic volume.

For general sources \((f,g_1,g_2,g_3)\), solve the scalar part of (8.1) explicitly:
\[
 \begin{aligned}
 \mu&=N\{Q'S(g_1+D^*A)+g_3-Q'S^2g_2\},\\
 h&=Sg_2+SQ'^*\mu=P D^*A+h_0,\\
 \lambda&=S(g_1+D^*A-h),\\
 TA&=f+Dh_0.
 \end{aligned}                                                    \tag{8.4}
\]
The just-proved bounds imply
\(\|h_0\|_2\le C_L(\|g_1\|_2+\|g_2\|_{H^{-2}}+\|g_3\|_{\rm top})\).
Apply the vector energy inverse to the last equation, then the first three equations successively. Restoring scale gives
\[
 \|\mathbb M_i^{-1}F\|_{\mathcal X_i}
                  \le C_L\|F\|_{\mathcal X_i^*}.     \tag{8.5}
\]
No kernel estimate for a vector inverse was used to prove (8.5).

The boundary model is entirely bare, with \(Q'=I\), \(R=0\), and vector mass \(\eta^{-2}I\), on the actual allowed fine coordinates in that local piece of \(\Omega_0\). Its form is \(\|CA\|_2^2+\eta^{-2}\|A\|_2^2\). The elementary bound \(\|\nabla A\|_2\le C\eta^{-1}\|A\|_2\), also for zero extensions, proves its energy inverse bound uniformly over shapes. On this bare space the second-order norm is equivalent to \(\eta^{-2}\|\lambda\|_2\). Formula (8.4), with \(Q'=I\), then proves (8.5) for this boundary model too. Thus no regularity of an artificial coarse Dirichlet corner is assumed.

### 8.2 Local models, cutoffs, and the small remainder

Choose a large power \(M\) of \(L\), to be fixed below. Tile each layer by cubes of side \(Ms_j\), taking the original cube size to be a divisible power at least \(M\). Include a bare tiling outside \(\Omega_0\) when defining cutoffs. For each tile take a sampled smooth bump equal to one on it and supported in a fixed enlargement. Normalize these bumps by the square root of their summed squares. This denominator is at least one. We obtain cutoffs \(h_i\) with
\[
 \sum_i h_i^2=1,\qquad |Dh_i|\le {C_L\over Ms_i},
 \qquad |D^2h_i|\le {C_L\over M^2s_i^2}.            \tag{8.6}
\]
For the top component evaluate the same continuous cutoff at its top; for a bond component use its initial point. The identity \(\sum_i h_i^2=1\) holds on each component separately.

Take the separation larger than a fixed \(L\)-dependent multiple of \(M\), large enough for all the enlargements in this paragraph. An enlarged tile then meets at most one seam and only its two adjacent scales. To check this, reaching a layer two levels away crosses a complete collar of width at least \(\rho s_i/L\); the enlargement has radius at most \(C_LMs_i\). Choose \(\rho>C_LML\). At a fixed point only adjacent-size tiles can overlap, and the number of tiles of either size whose fixed enlargement contains it is bounded by a constant depending on \(L\), independent of \(M\). This proves bounded overlap of both the cutoffs and their read sets. A tile near \(\partial\Omega_0\) is bare by the first gap.

For an interior tile, copy the actual one- or two-scale pattern, including every complete pillar and double block meeting its cutoff support, to a larger periodic box. Include a collar of width \(C_LMs_i\). In a further collar extend by the smaller of the two row scales and then make it periodic. The marked larger blocks are a union of complete blocks. Thus this is a two-scale model of §6, irrespective of the shape of the copied interface. Its full periodic box is the assigned read set of \(\mathbb M_i^{-1}\). All its dimensions are fixed multiples, depending on \(L\), of \(Ms_i\). The nonwrapping floor makes it an embedded read set. The cutoff vanishes well before its edge. Boundary tiles use the bare model just described, copying the actual boundary and imposing zero extension at the outer edge of their assigned enlargement. All choices use only data in that enlargement.

On the support and complete read closure of \(h_i\), the coefficients of \(\mathbb M_i\) and \(\mathbb M\) coincide. Extend \(h_i\mathbb M_i^{-1}h_i\) by zero, and set
\[
 \mathbb B=\sum_i h_i\mathbb M_i^{-1}h_i,
 \qquad
 \mathbb M\mathbb B=I+\mathbb R,
 \qquad
 \mathbb R=\sum_i[\mathbb M,h_i]\mathbb M_i^{-1}h_i.
 \tag{8.7}
\]
The identities are exact: local differential stencils and averaging read sets crossing a cutoff are still in the copied region. Products containing a cutoff vanish before any artificial periodic or Dirichlet edge, so no derivative of a discontinuous extension of a local solution is taken.

Here are the commutator estimates in the actual spaces. For the scalar second-order block, the difference product rule gives terms \((Dh_i)D\lambda\) and \((D^2h_i)\lambda\), bounded in \(L^2\) by \(C_LM^{-1}\|\lambda\|_{H^2_m}\). The mass commutator has the same bound, because a cutoff's oscillation within one pillar is at most \(C_L/M\). Transposition bounds the corresponding block from \(L^2\) to \((H^2_m)^*\). For a first-order block, the commutator is a shifted multiplication by \(Dh_i\); the weighted zeroth-order part of \(E\) gives its \(C_L/M\) bound. For the vector second-order block, integrate one difference by parts: each term contains one cutoff difference, one field or field difference, and has form norm at most \(C_LM^{-1}\|A\|_E\|B\|_E\). The vector row mass is handled by inserting the cutoff at the row centre; its error is at most its double-block oscillation, \(C_L/M\). Jensen and the physical row/column counts of §3 bound the resulting row norms by the corresponding \(E\) norms. Finally
\(Q'(h_i\lambda)-h_i({\rm top})Q'\lambda\)
has size at most \(C_L/M\) times the average of \(|\lambda|\); Cauchy–Schwarz in each pillar pairs its \(m^{-2}\) norm with \(\|m^2\mu\|\). These are all the nonzero blocks of the commutator. They prove
\[
 \|[\mathbb M,h_i]X\|_{\mathcal X^*}
       \le {C_L\over M}\|X\|_{\mathcal X_i,\rm read}.
 \tag{8.8}
\]
In (8.8) the norm of a test field can be restricted to the same enlarged read set. Cutoff multiplication is uniformly bounded in all four spaces. Bounded overlap and Cauchy–Schwarz therefore sum (8.5), (8.8) to
\[
 \|\mathbb B\|_{\mathcal X^*\to\mathcal X}\le C_L,
 \qquad
 \|\mathbb R\|_{\mathcal X^*\to\mathcal X^*}\le {C_L\over M}.
 \tag{8.9}
\]
More explicitly, the map from the direct sum of local spaces to the global space, \((X_i)_i\mapsto\sum_i h_iX_i\), is bounded by the product rule and bounded overlap. Its transpose maps a global source to \((h_iF)_i\), with the same norm bound. The map \((X_i)_i\mapsto\sum_i[\mathbb M,h_i]X_i\) has norm \(C_L/M\) into the global dual space: pair it with a global test field, use (8.8) on each read set, and use Cauchy–Schwarz and overlap. Compose these two maps with the direct sum of the local inverses (8.5). This proves both estimates in (8.9), including localization of second-order dual sources, without assuming that sharp pillar indicators are bounded multipliers on \(H^2_m\).

Fix \(M\) so that \(C_L/M<1/2\), and then fix the gap and torus floor for its read sets. The constants in (8.5) were uniform in the size of the periodic local box, so this order of choice is not circular. The exact inverse is
\[
 \mathbb M^{-1}=\mathbb B\sum_{n=0}^\infty(-\mathbb R)^n,
 \qquad \|\mathbb M^{-1}\|_{\mathcal X^*\to\mathcal X}\le2C_L.
 \tag{8.10}
\]
The series converges in operator norm. The same construction, omitting the first row and column of (8.1), applies to the scalar saddle system. In that system the \(h\leftarrow g_1\) block is \(P\), and the \(\mu\leftarrow g_3\) block is \(N\), as is verified by (8.4) without \(A\). Applying the construction directly to \(A_s:H^2_m\to L^2\) gives a local series for \(S\) as well. Thus the scalar projection has an actual local expansion; it has not been inserted into (8.7) as a global coefficient.

### 8.3 Decay and the vector energy conclusion

Every factor in (8.7) has support and read set in its assigned enlargement, of layer-metric diameter at most \(D_LM\). In a nonzero product the successive supports meet, so a term of length \(n\) connects endpoints at distance at most \((n+1)D_LM\). Equation (8.9) bounds the sum of all terms of that length in operator norm by \(C_L2^{-n}\); no separate count of individual walks is needed. Consequently, between source and output pillars,
\[
 \|\mathbf1_yG\mathbf1_z\|_{2\to2}
       \le C m_y m_z e^{-\delta d(y,z)},\quad
 \|\mathbf1_yDG\mathbf1_z\|_{2\to2}
       \le C m_z e^{-\delta d(y,z)},
 \tag{8.11}
\]
and the two versions with a source derivative have factors \(m_y\) and \(1\). Here \(\delta>0\) depends only on the now fixed \(L,M\). A differentiated source enlarges its support by one stencil, which changes only the constant. These are restrictions of the output norm, not applications of a sharp cutoff inside a Sobolev norm. The source estimates are \(\|f\|_{E^*}\le m_z\|f\|_2\) and \(\|D^*g\|_{E^*}\le C\|g\|_2\).

The scalar projection and Gram inverse exist already by scalar positivity. Elimination (8.2) shows that the \(A\leftarrow f\) block is the actual inverse \(G=T^{-1}\). Since \(T\) is a sum of three nonnegative forms and now is invertible, it is positive definite. Its bounded inverse \(E^*\to E\) gives
\[
 \boxed{\langle A,TA\rangle\ge c_L
       (\|\nabla A\|_2^2+\|m^{-1}A\|_2^2).}         \tag{8.12}
\]
For an explicit finite-dimensional justification, let \(J_E\) be the positive matrix of the squared \(E\) norm. The inverse bound says
\(\|J_E^{1/2}GJ_E^{1/2}\|\le C\). This matrix is positive; inversion gives \(T\ge C^{-1}J_E\). Thus (F0-E), including the default level-0 seam, is proved rather than assumed in the assembly.

## 9. Completion of F0/F3 in the consumer norms

### 9.1 Pointwise derivatives

Let \(u=Gf\), with \(f\) supported in the pillar of \(z\). On an interior fine cube the equation is
\[
 \Delta_{\rm comp}u=f+DPD^*u-Q^*aQu.                \tag{9.1}
\]
The projection estimate (5.6) gives, at a point over \(y\),
\[
 |DPD^*u|_y
 \le C m_y^{-3}\sum_w e^{-\delta d(y,w)}
                                      \|\nabla u\|_{2,w}.
 \tag{9.2}
\]
Indeed the density of \(DP\) is at most
\(Cm_y^{-3}m_w^{-2}e^{-\delta d(y,w)}\), and Cauchy–Schwarz over the source pillar contributes \(m_w^2\). A physical vector row has sum one and maximal counting coefficient \(\eta^4s_c^{-4}\). Its physical adjoint applied to a unit row is bounded by one. Thus its mass contribution is bounded by \(Cs_c^{-4}\|u\|_{2,\rm double\ block}\). At a given point only its own and an adjacent height can contribute: a higher outward double block lies in its immediately finer region, by the gap. The number of rows at either height is bounded. These observations bound the last term of (9.1) by the same scale powers as (9.2).

For bounded \(f\), (8.11) supplies
\(\|u\|_{2,w}\le Cm_wm_z^3e^{-\delta d(w,z)}|f|\) and
\(\|\nabla u\|_{2,w}\le Cm_z^3e^{-\delta d(w,z)}|f|\).
Substitution into (9.2), and the scale sum, show that the two last terms of (9.1) are at most
\(C(m_z/m_y)^3e^{-\delta' d(y,z)}|f|\). Absorb the ratio at a fixed loss of rate. Apply the local estimate (4.1) with \(g=0\), and use the equation itself for the Laplacian. At a bare output use its pointwise \(\ell^2\) bound and finitely many differences, as in §4.2. This proves
\[
 |Gf|_y,\ |\nabla Gf|_y,\ |\Delta_{\rm comp}Gf|_y,
       [\nabla Gf]_{\alpha,y}
 \le C_\alpha(m_y^2,m_y,1,m_y^{1-\alpha})
                         e^{-\delta_1d(y,z)}|f|.
 \tag{9.3}
\]
For \(u=G\nabla^*g\), (8.11) instead gives the source factor \(m_z^2|g|\). The last two terms of (9.1) are now bounded by
\(Cm_y^{-1}(m_z/m_y)^2e^{-\delta' d(y,z)}|g|\).
Apply both lines of (4.1), now retaining the differentiated source. The result is
\[
 \begin{aligned}
 |G\nabla^*g|_y&\le Cm_y e^{-\delta_1d(y,z)}|g|,\\
 [G\nabla^*g]_{\alpha,y}&\le C_\alpha m_y^{1-\alpha}e^{-\delta_1d(y,z)}|g|,\\
 |\nabla G\nabla^*g|_y+m_y^\beta[\nabla G\nabla^*g]_{\beta,y}
 &\le C_{\epsilon,\beta}e^{-\delta_1d(y,z)}
                           (|g|+m_z^\epsilon[g]_\epsilon),
 \quad0<\beta<\epsilon<1.
 \end{aligned}                                                    \tag{9.4}
\]
This includes curl-adjoint sources by taking their componentwise first-difference combination. Integrating (9.2) in the output pillar, rather than taking its supremum, and using (8.11), gives the localized \(L^2\) bound for \(\Delta_{\rm comp}G\), with output power zero after scale redistribution. Together with (8.11), these are all the inverse and differentiated-source norms in F0 and F3. No second derivative on an arbitrary bounded differentiated source has been asserted.

### 9.2 Row Gram and lift, including their local expansions

Use dimensionless rows \(K=mQ\) with counting pairing, and put
\(\Gamma=KGK^*\). On a local two-scale model there is a uniformly bounded right inverse in the energy norm. Here is a particularly simple construction. First work on its unit intermediate lattice. Set every retained bare bond equal to its prescribed datum. Each remaining coarse row has a central face pivot, omitted from the bare rows. Its coefficient in the dimensionless length-\(L\) row is \(L^{-3}\), and it is read by no other coarse row, as checked in §7. Set that pivot to \(L^3\) times the discrepancy between the prescribed coarse datum and the average of the already assigned bare bonds; set other unassigned bonds to zero. The unit field \(v\) now has all the prescribed mixed averages and
\(\|v\|_2\le C_L\|b\|_{\rm count}\), by the finite row/column counts. Lift \(v\) to the fine lattice using the one-scale \(H\) in (6.7). This yields
\[
 KT b=b,\qquad \|Tb\|_E\le C_L\|b\|_{\rm count}.
 \tag{9.5}
\]
The one-scale case uses (6.7) directly. In a bare boundary model take \(Tb=b/\eta\); its energy norm has exactly the required four-dimensional scaling. The minimum of the positive form with \(KA=b\) is \(\langle b,\Gamma^{-1}b\rangle\), by completing the square. Testing it with (9.5) proves the local gap \(\Gamma\ge c_LI\); its upper bound follows from (6.14) and \(K:E\to\ell^2\).

Adjoin to (8.1) one counting-row multiplier \(\nu\), with blocks \(-K^*\nu\) in the vector equation and \(-KA\) in the last equation. The resulting matrix is local and symmetric. Its row Schur complement is \(-\Gamma\). The local inverse bound follows from (8.5), the local gap just proved, and the formula solving that Schur complement. Give \(\nu\) its counting \(\ell^2\) norm. The additional commutator is \(K(h_iA)-h_i({\rm row})KA\); its double-block cutoff oscillation and Jensen give the same \(C_L/M\) bound as in (8.8). Thus the entire construction (8.7)–(8.10) applies to this enlarged system. It supplies the actual global row inverse and lift with local read sets, and in particular
\[
 c_LI\le\Gamma\le C_LI,\qquad
 |\Gamma^{-1}(c,c')|\le C_Le^{-\delta_2d(y_c,y_{c'})}.
 \tag{9.6}
\]
The upper bound uses the global energy inverse and the bounded map \(K:E\to\ell^2\); the latter follows directly from the physical Jensen/column counts. The lower bound and exponential inverse follow from the enlarged local system. There is no inference from invertibility alone.

Let \(J_v=QGQ^*\), with physical top pairing. The exact conversion is
\[
 \Gamma=mJ_vm^{-3},\qquad
 J_v^{-1}=m^{-3}\Gamma^{-1}m.
 \tag{9.7}
\]
It follows that
\[
 c\|m\psi\|_{\rm top}^2\le
 \langle\psi,J_v\psi\rangle_{\rm top}
 \le C\|m\psi\|_{\rm top}^2,
 \quad
 |J_v^{-1}(c,c')|_{\rm count}\le Cm_c^{-2}e^{-\delta_3d(y_c,y_{c'})}.
 \tag{9.8}
\]
The factor \(m_{c'}/m_c\) in (9.7) is absorbed using the scale-distance inequality. Dividing the counting kernel by \(m_{c'}^4\) gives exactly F0's density \(Cm_c^{-2}m_{c'}^{-4}e^{-\delta_3d}\). Similarly (5.4) gives the scalar density \(Cm_y^{-4}m_z^{-4}e^{-\delta d}\). These reconstruct CMP 99b (3.48) and (3.132) in the consumer pairings.

The dimensionless lift is \(H_B=GK^*\Gamma^{-1}\); the physical-row lift is \(H=H_Bm\). Equations (3.3)–(3.4), (9.3), and (9.6), with the scale sum, give
\[
 \begin{aligned}
 |H_B(b,c)|&\le Cm_y^{-1}e^{-\delta_4d(y,y_c)},&
 |\nabla H_B(b,c)|&\le Cm_y^{-2}e^{-\delta_4d(y,y_c)},\\
 |H(b,c)|&\le Ce^{-\delta_5d(y,y_c)},&
 |\nabla H(b,c)|&\le Cm_y^{-1}e^{-\delta_5d(y,y_c)}.
 \end{aligned}                                                    \tag{9.9}
\]
A gradient Hölder quotient adds \(m_y^{-\alpha}\). Equivalently the physical bounds in the second line acquire the source factor \(m_c^{-1}\) for dimensionless data. The first line is a redistribution of that factor to the output, with a reduced rate.

In the force transpose used by the profile consumer, the fine pairing is \(\eta^4\sum_b\) and the row pairing is counting. If \(|f|_{(-3)}=\sup_b m_b^3|f(b)|\), then
\[
 |H_B^*f(c)|
 \le C|f|_{(-3)}\sum_y m_y^4m_y^{-1}m_y^{-3}
                          e^{-\delta_4d(y,y_c)}
 \le C'|f|_{(-3)}.                                  \tag{9.10}
\]
This explicitly cancels the fine volume; summing fine coordinates without it would be wrong. The dimensionless multiplier operator is \(E_B=\Gamma^{-1}-a^{\rm dim}\), with \(a^{\rm dim}_c=s_c^2a^{\rm phys}_c\). Its counting kernel is a diagonal bounded term plus the exponential in (9.6). It has the required bounded row supremum norm; for the profile consumer \(a^{\rm dim}=I\).

All the weighted versions used by the consumers follow by multiplying kernels by \(w(y)/w(z)\), where \(|\log w(y)-\log w(z)|\le\nu d(y,z)\), and choosing \(\nu\) smaller than the retained decay rate. The scale-volume sum is then applied with rate \(\delta-\nu>0\). In particular \(H_B\) maps weighted bounded row data to the weighted potential/first-gradient norm with factors \(m_y,m_y^2\); \(E_B\) maps weighted rows to themselves; and (9.10) has the indicated force version. These are the norms required in the profile gate, not just an unweighted \(L^2\) lift.

The exact identities \(KH_B=I\), \(RD^*H_B=0\) follow from constrained minimization. The Landau fibre covariance is
\[
 \mathcal G=G-GDRD^*G-GK^*\Gamma^{-1}KG.             \tag{9.11}
\]
The projection identities in `a3-balaban.md` §6 prove its inverse characterization; they are purely algebraic and their positivity premise is now supplied by (8.12). Both subtractions in (9.11) are retained. Its stated first-order and force bounds follow by composing the bounds above and the scalar bounds; the scale sums include all cell measures. This does not add the component-Laplacian estimate excluded for the corrected/fibre propagators by CMP 99b Theorems 3.12–3.13.

Equations (4.7), (5.2)–(5.6), (8.12), and (9.3)–(9.10) now give **F0 as stated**, and **F3**, including local one/two-scale models and the assembled default many-scale geometry. All constants depend on the fixed \(L\) and exponent choices; the localization size and lower gap bound were chosen in a written order and introduce no depth or volume dependence.

## 10. F4: top support, the actual soft gauge, and conditioning

First complete the mixed-row identification left open in §7. Give only the highest, unit-scale rows nonzero data \(B\), supported in the stipulated union of top blocks, and give all finer rows datum zero. For a fine field satisfying these mixed constraints, its uniform \(k\)-step straight average agrees with the zero-extended \(B\) on every coarse edge of a plaquette meeting that support. On an edge touching \(\Omega_k\), this is the defining top constraint. On an edge just outside \(\Omega_k\), the two endpoint blocks lie in \(\Omega_{k-1}\), by separation, and are unions of complete finer pillars outside \(\Omega_k\). Composition of straight averages expresses this edge average entirely in retained, zero, level-\((k-1)\) rows. It is consequently zero. The same assertion covers the plaquette's remaining edges. A nonzero plaquette of \(CB\) is necessarily in this neighborhood.

Apply the plaquette averaging contraction (6.10), restricted to these plaquettes. For every admissible fine field,
\(\|CB\|_2^2\le\|CA\|_2^2\).
The mixed minimizer exists by §9. Gauge variations \(D\lambda\), \(Q'\lambda=0\), preserve its rows by (2.2), and their divergences span \(\operatorname{ran}R\). Minimizing over them makes \(RD^*A=0\). Therefore subtracting the fixed row mass gives exactly
\[
 A_k=(QGQ^*)^{-1}-a,\qquad
 \langle B,A_kB\rangle=\min_{QA=(0,B)}\|CA\|_2^2
                                  \ge\|CB\|_2^2.
 \tag{10.1}
\]
Pairings on these unit top rows are counting pairings. The construction uses the compressed whole-lattice curl stipulated in F3; it does not replace it with an unverified inner-plaquette action at a boundary. Combining (10.1) with (7.3)–(7.5) proves **(13.6)** and its strict-axial pivot form for the actual top-supported mixed problem. Additional conditioning of free coordinates is a restriction of this inequality.

The outline's plain-average/soft-contour gauge is different. Here is the required separate argument. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the formulation and fixed-cell proof in the fetched outline, (CF1)–(CF18), lines 8399–8720. The following reproduces the proof rather than identifying that gauge with a tree gauge.

On the current unit lattice let \(\gamma_{y,x}(B)\) be the arithmetic mean of coordinate-order internal path integrals, and write \(\mathsf G B=(\gamma_{y,x}(B))\). The positive soft gauge form is \(\|\mathsf G B\|_2^2\) in canonical Gaussian variables. The actual plain one-step row is
\[
 P_LB=K_LB-D_L\sigma(B),\qquad
 \sigma(B)(y)=L^{-4}\sum_{x\in B_L(y)}\gamma_{y,x}(B).
 \tag{10.2}
\]
This is the derivative of the plain average: the reference-path derivative cancels its negative occurrence inside each closed logarithm, and the two block contour means remain as endpoint terms. For a gradient, path telescoping gives \(P_LD\lambda=D_L(\lambda|_{\rm centres})\); the straight row instead uses the block mean. Thus these two constraints have not been interchanged.

A central crossing pivot has coefficient \(L^{-3}\) in \(P_L\), since internal contours contain no crossing pivot. No other pivot occurs in that row. Let \(I_{\rm pl}(p)\) be the actual pivot inclusion on a Bloch cell of \(L^4\) sites with phase \(p\): extend nonpivot coordinates unchanged and solve each pivot with that coefficient. Its entries are finite Laurent polynomials in \(e^{\pm ip_\mu}\), it has uniformly bounded norm at fixed \(L\), and
\(\operatorname{ran}I_{\rm pl}(p)=\ker P_L(p)\).
The cell matrix
\[
 B(p)=I_{\rm pl}(p)^*
                  (C_p^*C_p+\mathsf G^*\mathsf G)I_{\rm pl}(p)
 \tag{10.3}
\]
has no null vector. Indeed zero curl makes all coordinate-order paths with the same endpoints have the same integral, by plaquette swaps. If also \(\mathsf G B=0\), those integrals are zero. Comparing a root path followed by one internal edge with the root path to its endpoint kills every internal edge. A plaquette across a face then says that neighboring crossing values are equal; the transverse face grid is connected, so the crossing value is a single number \(\beta\). Every averaged straight segment crosses that face exactly once, with zero internal contribution. The contour terms in (10.2) are zero. Hence the plain row is \(\beta\), and the constraint kills it. All bonds vanish, and the unchanged free coordinates vanish. This argument includes \(p=0\) and complex fiber vectors; it has not discarded a harmonic constant mode.

The fixed-dimensional matrix (10.3) is continuous on the compact Bloch torus. If its least Rayleigh quotient had infimum zero, parameters and unit free vectors approaching that infimum would have a convergent subsequence. Their limit would be a unit null vector of the limiting matrix, contradicting the preceding argument. Consequently \(B(p)\ge\gamma_LI\) for some \(\gamma_L>0\). This is an existence proof for a constant, not a numerical spectral check. Fourier transformation over the coarse cells proves the bound on every compatible torus. Zero extension and restriction prove it on every conditioning subset.

By (10.1), the actual top precision with the soft gauge therefore obeys
\[
 I_{\rm pl}^*(A_k+\mathsf G^*\mathsf G)I_{\rm pl}
                    \ge\gamma_LI.                  \tag{10.4}
\]
For a fixed positive gauge coefficient other than one, multiply \(\gamma_L\) by the minimum of that coefficient and one. This is the soft-gauge comparison required by the consumer. Its constant is \(\gamma_L\), while the strict-tree version retains the explicit \(c_4L^{-5}\).

Finally the conditional covariance kernels follow without a new gap assumption. Equation (9.6), restricted to unit top rows, gives an exponential kernel for \(A_k\). The fine scale metric dominates unit Euclidean distance because the largest scale is one. The strict and plain pivot maps are finite range and bounded at fixed \(L\); the soft gauge is block local. Thus either compressed precision \(A_{\rm piv}\) has
\[
 A_{\rm piv}\ge\gamma I,\qquad
 |A_{\rm piv}(b,b')|\le C_Le^{-\delta|b-b'|},
 \tag{10.5}
\]
with the appropriate gap just proved. For \(w_b=e^{\theta|b-b_0|}\),
\[
 |(wA_{\rm piv}w^{-1}-A_{\rm piv})(b,b')|
 \le C_L\theta |b-b'|e^{-(\delta-\theta)|b-b'|}.
\]
Unit-lattice shells contain at most \(C(r+1)^4\) bond coordinates; the two Schur sums are therefore at most \(C'_L\theta\). Choose \(\theta<\delta/2\) and \(C'_L\theta<\gamma/2\). The inverse series gives
\[
 |A_{\rm piv}^{-1}(b,b')|\le {2\over\gamma}e^{-\theta|b-b'|}.
 \tag{10.6}
\]
Restricting the coordinate index set reduces the Schur sums and preserves the gap, so the constants are uniform for conditioning subsets. Composing with the local pivot inclusion gives the covariance on bond variables, with its stated \(L\)-dependent norm comparison. This closes **F4** in both the strict source gauge and the actual flat soft-contour gauge; it grants no curved or complex gap.

## 11. F5: local read sets and comparison remainders

Here the local systems matter. A walk expansion of \(T\) that simply inserts the global \(P\) as a coefficient would fail the read-set requirement. Equations (8.1), (8.7) and the enlarged row system of §9 contain only finite-stencil derivatives and the actual finite averaging rows. Their local inverses read exactly their assigned finite periodic or bare boundary model. Those models copy the original geometry only inside the specified enlargement and use the fixed smaller-scale extension beyond it. Cutoff normalization also has a local read set: only bumps whose supports meet the point enter its denominator. Include those tiles in the enlargement. With a common tiling phase, two sequences or compatible tori agreeing there give literally the same local matrix and cutoff.

For an absolute walk estimate, refine the norm argument in (8.9) into patch norms. One enlarged patch meets at most \(D_L\) other enlarged patches, because only adjacent scales can meet and their tile spacings are comparable. The norm of one commutator transition between local spaces is at most \(B_L/M\), by (8.5) and (8.8); the norm of the starting inverse is at most \(B_L\). Increase the chosen power \(M\), if necessary, so that
\(q=D_LB_L/M<1/2\) for the scalar, vector and enlarged row systems simultaneously. Then the sum of the norms of all length-\(n\) walks from a fixed starting patch is at most \(B_Lq^n\). The reverse bound is identical. This also justifies absolute compositions of the expansions in localized operator norms. There is no factor counting fine sites and no volume factor.

Let \(D\) be the changed region, including changes of boundary coordinates, rows, and torus identifications. Terms whose complete read sets avoid \(D\) are identical in the two constructions. Any remaining term reads a connected chain of enlarged patches reaching \(D\). Each read set has layer-metric diameter at most \(D'_LM\); thus its length must be at least the distance to the changed region divided by \(D'_LM\), minus a fixed number of endpoint patches. The geometric tail \(\sum_{n\ge N}B_Lq^n\) supplies an extra exponential in that distance. If both endpoints are kept, the chain connects them and reaches \(D\); splitting its length in half retains a fixed fraction of endpoint decay as well as a fixed fraction of the distance-to-change decay. Distances up to the first encounter with \(D\) use identical geometry. When the exterior metrics differ, the endpoint factor can use the smaller of the two endpoint distances; the common interior distance to \(D\) is unchanged. In the local cube comparisons used by the construction this gives precisely an extra \(e^{-c_LM}\).

These are initially bounds in the spaces (8.3), with row counting norms for the enlarged system. Here is the derivative upgrade for the **summed remainder**, so it is not inferred from energy alone. Inside the common region the difference of two solutions with the same source satisfies the homogeneous equations of the local system. Its scalar equation is
\(A_s\delta h=Q'^*\delta\mu\).
On a local cube, a row component of \(\delta\mu\) is bounded by \(m^{-4}\|m^2\delta\mu\|_{\rm top}\); the scalar mass contribution is bounded by \(m^{-4}\|\delta h\|_2\). The local Poisson estimate (4.1) therefore gives
\(|D\delta h|\le Cm^{-3}\|\delta X\|_{\mathcal X,\rm larger}\), with the corresponding Hölder bound. The vector equation reads
\(\Delta_{\rm comp}\delta A=D\delta h-Q^*aQ\delta A\), with an additional \(K^*\delta\nu\) in the enlarged system. The latter term is bounded by (3.3) in exactly the force power \(m^{-3}\). Another application of (4.1) bounds the value, gradient, Laplacian and gradient Hölder norm of \(\delta A\) by the powers \(m^{-1},m^{-2},m^{-3},m^{-2-\alpha}\) times the local remainder norm. Source norms contribute \(m_z^3|f|\), \(m_z^2|g|\), or the counting row datum, just as in §§4 and 9. Fixed scale powers are redistributed with the proved scale sum. At bare boundary sites use the finite-difference bounds already given. Thus the remainders have the **same consumer norms** as the original operators, multiplied by the extra exponential. Identical sources cancel even where their common support meets the output cube; no spurious Hölder norm of a sharp difference source is introduced.

The scalar system gives the same argument for \(S,N,P\). For the fine projection kernel apply the scalar local estimate at both endpoints, using symmetry and the top component's norm in the scalar system. This gives the powers \(m_y^{-2-r}m_z^{-2-t}\) of (5.6), with the extra exponential and the corresponding Hölder differences. For the row Gram inverse the endpoint counting bound is already a component of the enlarged-system remainder. The lift is another block of that inverse. Formula (9.11) and finite products of these expansions preserve locality: the read set is the union of the factor read sets, and the scale-volume convolution bound sums the intermediate indices. Only the derivative norms actually asserted for the fibre covariance are used.

The unit conditional covariances of §10 can also be localized. On unit blocks take cutoffs of side \(R\), and in a larger read box copy the conditioning coordinates and the same flat local model. Compress its precision to those coordinates. The gap and exponential kernel in (10.5)–(10.6) remain uniform. For the resulting local inverse \(C_i\), the parametrix \(\sum_i\chi_iC_i\chi_i\) has remainder
\[
 \sum_i[A_{\rm piv},\chi_i]C_i\chi_i
       +\sum_i\chi_i(A_{\rm piv}-A_{{\rm piv},i})C_i\chi_i.
 \tag{11.1}
\]
The first term has two Schur sums at most \(C_L/R\): insert
\(|\chi_i(b)-\chi_i(b')|\le C\min\{|b-b'|/R,1\}\)
in (10.5) and sum its exponentially decaying shells. For the second, the already proved row-system comparison, followed by the finite-range pivot maps, gives \(C_Le^{-c_LR}\) on the cutoff support; the part with the other endpoint outside the larger box has the same bound by (10.5). Bounded overlap sums these estimates. Choose a fixed \(R=R(L)\) so their sum, times the bound for \(C_i\), is less than one half. Expanding the resulting inverse series proves its local comparison. To assign read sets, expand each precision entry in (11.1) by its already constructed row-system walks. Common inner words cancel; words in the second difference reach the changed collar. The first commutator contributes the factor \(\min\{\text{walk length}/R,1\}\). Its absolute majorant sums to \(C_L/R\), since \(\sum n q^n<\infty\). Thus the same nested expansion has local read sets and the claimed exponential remainder, rather than just a comparison between arbitrary decaying matrices.

Choose \(R\) after the earlier decay and gap constants, and increase the admitted gap/floor to contain its read sets. If a unit torus is smaller than this fixed read box, use that whole torus as one model; its size is then bounded by the same fixed constant, and the direct estimates of §10 apply. No long-distance comparison is asserted across a nonembedded common region.

This proves **F5** for the specified local flat models, their scalar/projection and vector/Gram comparisons, and the conditional coordinate inverses. It supplies an actual local term assignment and a bound for the summed remainder after a walk reaches the changed region.

## 12. Endpoint and order of constants

**PROVED — as a research statement, not an audit.** F0 in the default no-inward convention is established in §§4–6, 8–9; its level-0 seam is treated in §§2, 6–8. The flat \(K^*\) column bound is (3.3)–(3.4). F1 is §§4 and 9.1's scalar counterpart; F2 is §5; F3 is §§8–9; F4 is §§7 and 10; F5 is §11. The norms, cell measures, source Hölder exponents, top weights, and force transpose used by the consumers are displayed at those conclusions.

The order is: fix \(L\) and the finite collection of Hölder exponents; obtain the one/two-scale energy and scalar Gram constants; choose the common walk size \(M\) for all the local systems and their absolute patch majorants; obtain the decay rates and the unit conditioning gaps; choose \(R\) if the conditional-coordinate walk is required; choose the separation above the read-set requirements and the scale-volume summation thresholds; then choose compatible cube sizes and nonwrapping torus floors. All choices are functions of \(L\) and the specified exponents. None depends on the depth, fine mesh, volume, shape of the admitted layers, or conditioning subset.

The explicit configuration in §2.1 refutes only the substitution of inward-retaining rows into the unchanged scalar gauge identity. It is not a counterexample to default F0. The proof above consistently uses the default rows. No curved response, complex-domain theorem, Yang–Mills existence statement, audit outcome, or repository status is claimed.
