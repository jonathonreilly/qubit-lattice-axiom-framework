## Repo search

**Checked sources.** Row 1485, research at `c3f9aafbb`. The target-specific prior is absent. The November 8 survey of main and PRs 10114, 10133, 10134 and 10141 predates this question. Its nearest hit, PR 10114 at `f76f6c649c`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` lines 106–149, gives a lower bound for a chosen plaquette-loop transfer observable. I checked that passage. The same PR's literature check at lines 111–122 and 163–170 and main's `research/mass-gap/library/gap-form-exercise.md` lines 139–145 concern twisted partition functions. Main's SU(3) beta-six tensor-network note, lines 10–30 at `8b11ae2bb9`, treats single-link coefficients. None of those estimates bounds the correlation of arbitrary functions of a pair of SU(2) pivot matrices. The registry search found no other owner of this test. [Lead survey](prior/repo-search-2026-11-08.md) · [Registry](open-registry.md)

**Checked sources.** Row 1348 (1) supplies the positively oriented, left-factor pivot and the quadratic form from all single-cut plaquettes. Row 1350 §7 checks these identities. Row 1475 §5 and check 1484 distinguish the ordered auxiliary-field counterexample from this pure Wilson question and identify the scalar pressure that an iteration must carry. [1348](gap-blockstep3-astra62.md) · [1350](gap-blockstep3-check-opus.md) · [1475](gap-k2-pivot-environment-astra62.md) · [1484](gap-k2-pivot-environment-check-opus.md)

**Checked sources.** The Sussman–Alpoge outline defines the finite Wilson law at lines 240–277, distinguishes preservation of mass from identification of observables at 394–408, and proves convergence of the connected logarithm under the Kotecký–Preiss hypothesis at 1310–1326. CA-I lines 56439–56456 and 56530–56539 assume the earlier-level representation and a ceiling in Bałaban's weak-coupling construction. The indexed passages give no order-one Wilson interface coefficient. Credit for the two texts goes to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L394-L408) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L56439-L56456)

## Result at \(\beta=23/10\)

**Open.** The maximum row sum \(R\) is greater than \(49/225\). Its proved upper bound is greater than one, and no trial here attains one. With the zero-transverse-corner pivots used in 1475 §5, the four outward rows attain the maximum. Each mixed inward–outward coefficient can be tested using eigenvalues alone. Individually resolved plaquette forms do give a trial row sum of one, which is why an upper-bound calculation must respect the loss of information when the twelve forms are added. The scalar pressure consequence for the pure-Wilson pivot is given below.

## The eight conditional laws

**Proved.** Use the central sites \(C=\{0,1\}^4\) and its translates \(C\pm2e_\mu\). Write \(F_i\) for the three-dimensional face of \(C\) meeting neighbour \(i\). Orient all links in positive lattice directions as in 1348. Use the zero-transverse-corner pivot of 1475 §5 unless indicated. The 32 links of \(C\) have array \(X\). Each neighbour has 32 internal links \(Y_i\) and eight crossing links \(u_{i,s}\), one at each vertex \(s\) of \(F_i\). The 24 plaquettes internal to each box come from six choices of direction pair and four choices of transverse coordinates. At each interface the 12 edges of a three-cube give the 12 single-cut plaquettes. A double cut would require a fourth box on a coarse square, absent from this union. Thus the counts are \(9\cdot32+8\cdot8=352\) links and \(9\cdot24+8\cdot12=312\) plaquettes. These counts use two **sites** per direction, as in 1348 (1).

**Proved.** On one interface, write \(A_{st},D_{st}\) for the positive tangential links at its source and target, and \(r_s=u_*^{-1}u_s\) with \(*\) the pivot. With \(q=\operatorname{Re}\operatorname{tr}/2\), its actual matrix is the unique real symmetric matrix such that for every unit quaternion \(v\),
\[
 v^t Q_i v=\beta\sum_{st} q\!\left(A_{st}^{-1} v r_sD_{st}r_t^{-1}v^{-1}\right).
 \tag{1}
\]
The sum runs over the 12 tangential edges. At \(v=u_*\) the words give the Wilson single-cut plaquettes by cyclicity. Homogenizing the two appearances of \(v,\bar v\) yields the unique quadratic form, including its scalar part. The source \(A\) lies in \(C\) for a positive face and in the neighbour for a negative face.

**Proved.** Let \(S_C,S_i\) sum the internal \(q\)'s and \(E_i=u_*^tQ_i u_*\). At fixed \(X\) put
\[
 L_i(X_{F_i})=\int \exp(\beta S_i(Y_i)+E_i)\,dY_i\,du_i,\qquad
 d\mu_C(X)=
 \frac{e^{\beta S_C(X)}\prod_i L_i(X_{F_i})}{\int e^{\beta S_C}\prod_i L_i\,dX}\,dX .
 \tag{2}
\]
All base Haar measures are probabilities. The scalar \(e^{-312\beta}\) cancels in this normalized law. In the unnormalized star mass it multiplies the denominator in (2). Conditional on \(X\), the eight arm laws factor, each with the integrand of \(L_i\) divided by \(L_i\). For centred functions \(f,g\) on two different matrices define \(K_if(X)=\mathbb E[f(Q_i)\mid X]\). The exact covariance is \(\int K_if(X)K_jg(X)\,d\mu_C(X)\). This includes the tilt from all eight neighbours even when \(f,g\) use only two.


## What the choice of source face does to maximal correlation

**Proved.** For central tangential array \(A\) on one face, transport the neighbour's boundary array back into the central frame, calling it \(B\). Gauge-transform at each of the eight boundary vertices in that neighbour so the crossing links become identities. Apply the same change to every incident neighbour link, including links leading to its other layer. Conditional on the original crossing values, product Haar on those links is preserved, all neighbour plaquettes keep their traces, and the crossing action becomes \(\beta\sum_e q(A_e^{-1}B_e)\). The original eight crossing values are therefore independent product Haar in these coordinates, independently of \(X,B\) and the other transformed neighbour links. Each of the eight changes uses only its own neighbour. The conditional distribution of \(B\) given \(A\) is covariant under vertex gauges of \(A\), by applying the same gauges on its boundary.

**Proved.** For \(v\in SU(2)\) introduce the quadratic form on unit quaternions
\[
 D(A,B)(v)=\beta\sum_{e}q(A_e^{-1}vB_e v^{-1}).
 \tag{3}
\]
An outward-facing interface in 1348 has \(Q(v)=D(A,B)(v u_*^{-1})\). An inward-facing interface has
\[
 Q(v)=D(A^k,B^k)\big((u_*^{-1}v)^{-1}\big),\qquad
 A^k_{st}=k_sA_{st}k_t^{-1},\quad B^k_{st}=k_s B_{st} k_t^{-1},
 \quad k_s=u_*^{-1}u_s,\ k_*=1 .
 \tag{4}
\]
Indeed the untransported neighbour link in the latter case is \(u_sB_{st}u_t^{-1}\). Substitution in (1) gives (4) because \(D(B,A)(t)=D(A,B)(t^{-1})\). Conditional on \(X,B\), the seven \(k_s\) and \(u_*\) in (4) are independent Haar. These statements concern the tilted Wilson law in (2).

**Proved.** Write \(H_i f\) for the outward conditional expectation of \(f\), obtained with (3), an independent Haar right translation and the conditional law of \(B\) at \(X_{F_i}\). This defines the outward convention on any face for use in the formula below. Let \(J\) send a form \(D(v)\) to \(D(v^{-1})\), and \(P_S\) average central vertex gauges independently at sites of \(S\). Then
\[
 K_i f=H_i f\quad(i\text{ positive}),\qquad
 K_i f=P_{F_i\setminus\{*\}} H_i(f\circ J)\quad(i\text{ negative}).
 \tag{5}
\]
This follows from (4), conditional covariance of \(B\), and Haar inversion. Here and below a face in a vertex subscript denotes its vertex set. The \(P_S\) are commuting orthogonal projections in \(L^2(\mu_C)\), since the central marginal is invariant under the product of the vertex gauge groups. In particular the inward marginal of \(f\) equals the outward marginal of \(f\circ J\), including its variance.

**Proved.** For an outgoing interface a gauge at the private target pivot sends \(Q(v)\) to \(Q(vh)\). For an incoming interface a common gauge on its private source box sends \(Q(v)\) to \(Q(h^{-1}v)\). In each case all other matrices stay fixed. Averaging a probe over this rotation preserves its covariance with any other face and reduces its variance. The supremum defining \(\rho\) can therefore be taken on the invariant subspace for this rotation. In particular **every pair of linear probes has only the scalar trace channel**. The rotation average of \(v^t Qv\) is \(\operatorname{tr}Q/4\), because right or left multiplication is transitive on the unit three-sphere. Equivalently the average of any linear probe \(\operatorname{tr}(M Q)\) is \(\operatorname{tr}(M)\operatorname{tr}(Q)/4\).

**Proved.** In each mixed pair the supremum can be restricted further to functions of the four ordered eigenvalues on **both** faces. For the chosen pivots the potential exceptional central vertex of every inward face is \(o=(0,0,0,0)\), outside every outward face. In (2), \(H_i f\) on the outward face is already invariant at \(o\). By (5) the inward field may consequently be averaged at \(o\) as well. It is then invariant at every central vertex, so the outward field too can be averaged over all central gauges. A common centre gauge acts on the outward probe by the remaining left rotation and on the inward probe by the remaining right rotation. These averages on the probe preserve the cross covariance. Left and right unit quaternions together give \(SO(4)\). A left rotation sends \(1\) to any desired unit vector, and quaternion conjugations realize its stabilizer at \(1\), all three-dimensional rotations of the imaginary quaternions. Two real symmetric matrices with the same spectrum are \(SO(4)\)-conjugate (change the sign of an eigenvector if needed). Orthogonal averaging and variance contraction now give the asserted restriction. The argument allows arbitrary square-integrable probes.


## A comparison of the four pair coefficients

**Proved.** By coordinate permutation symmetry it suffices to write \(p\) for two positive faces, \(n\) for two negative faces, \(m\) for mixed perpendicular faces and \(o_1\) for opposite faces. Each central face has three other faces of its sign and three perpendicular faces of the other sign. For the stated convention,
\[
                 0\le o_1\le m\le n\le p,\qquad
             \max_i\sum_{j\ne i}\rho_{ij}=3p+3m+o_1 .
 \tag{6}
\]
Here is the reflection argument giving the inequalities.

**Proved.** Reflect by interchanging two coordinates, writing \(\theta\) for this interchange and \(+\) for the closed half with \(x_\mu\ge x_\nu\). For real half-supported functions set \(b(F,G)=\mathbb E_{\mu_C}[F\,\theta G]\). This symmetric bilinear form is positive semidefinite. To see this, use the full 352-link measure. No bond joins strict opposite halves. Every plaquette that meets both strict halves lies in the \(\mu,\nu\) plane and has two vertices fixed by reflection. Its two paths of length two between these vertices are interchanged by reflection. Its Wilson factor, as a kernel between a positive half-configuration and a reflected negative one, is \(\exp(\beta\,U\cdot V)\) with \(U,V\) the two path quaternions. Expanding the exponential in tensor powers gives a sum of inner products of identical features on the two copies, each with a nonnegative coefficient. The finite product over these plaquettes has the same property. At fixed plane links all remaining weights factor into a positive plane weight and identical single-half weights. Integration gives a sum of squares for \(b(F,F)\) by absolute convergence for bounded probes. Truncation gives positivity for \(L^2\) probes. In particular \(b\) satisfies Cauchy–Schwarz. Centred half-supported functions may be used directly.

**Proved.** Map a perpendicular pair geometrically to \(F=\{x_\mu=1\}\) and \(\theta F=\{x_\nu=1\}\), always writing its conditional fields in the outward convention (5). Reversing a transverse coordinate in (3) reverses the two tangential links together, preserving their scalar product after conjugation. Reflecting normal coordinates hence preserves the outward rule under the relabelling, including the law of the transported neighbour. Put \(I=F\cap\theta F\), its four shared sites. For a centred variance-one outward probe let \(G=H_F f\). For a positive pair the self-pairing is \(b(G,G)\). For a negative pair it is \(b(P_{I\setminus\{r\}}G,P_{I\setminus\{r\}}G)\), where \(r\) is the image of the common root. For a mixed pair it is \(b(P_I G,P_I G)\). Indeed the projections at sites outside the other's face can be moved to the other factor and have no effect. For the mixed pair the exceptional root on the inward face is outside the other face. Incoming probes are identified with outward probes by \(J\), with equal variances by (5). These statements also give the polarized pairings for two different probes. Since \(\theta\) fixes every site of \(I\), each of these projections is self-adjoint for \(b\). Its range and kernel are \(b\)-orthogonal. Positivity orders the self-pairings. For each projected form, Cauchy–Schwarz implies its supremum over two unit probes equals its supremum over a single unit probe. This proves \(m\le n\le p\).

**Proved.** For an opposite pair replace both fields by their full vertex-gauge averages as in the mixed-pair proof. Its positive face is supported in \(+\) and its negative face in the opposite closed half. Apply Cauchy–Schwarz for \(b\) to the positive field and the reflection of the negative one. Each self-pairing is now a fully gauge-averaged perpendicular pair, bounded by \(m\) times the respective probe variance. For this identification, projections on a face outside its four shared sites can again be moved to the other factor. It follows that \(o_1\le m\). This uses diagonal reflection of this open, symmetric finite graph only.

## A refuted upper-bound shortcut in the actual Wilson law

**Proved.** Keeping the twelve separate summands of \(Q_i\), even as an unordered collection, already gives a row sum at least one at \(\beta=23/10\). For a single summand in (1) write \(A=(a_0,\mathbf a)\) and \(r_s D r_t^{-1}=(d_0,\mathbf d)\). Dividing the quadratic by \(\beta\) gives the function
\[
                 a_0d_0+\mathbf a^t R(v)\mathbf d,
\]
where \(R(v)\) is the rotation of imaginary quaternions. Its nonconstant coefficient matrix is uniquely \(\mathbf a\mathbf d^t\) because \(1\) and the nine rotation entries are linearly independent, as follows by Haar orthogonality of the three-dimensional rotation representation (or by averaging the squared linear form over rotations). Its left Gram matrix divided by its trace is \(\mathbf a\mathbf a^t/|\mathbf a|^2\). The exceptional zero vectors have measure zero by absolute continuity with respect to product Haar in the original links, or the pivot coordinates. Thus on each positive interface the enlarged observation reads \(\sum_{e\in F_i} h(A_e)\), where \(h(a)=a_1^2/|\mathbf a|^2-1/3\), defined arbitrarily when \(\mathbf a=0\).

**Proved.** Under the full Wilson law a forest has product Haar link marginal. Indeed, on each tree, integrating independent vertex gauges successively from the leaves gives independent Haar values on its edges for every initial assignment. The law is gauge invariant. In particular any two distinct central links are independent Haar. The nonconstant \(h\) has mean zero by rotational symmetry, with variance \(s^2>0\). Dividing each face sum by \(\sqrt{12}\,s\) gives variance one. Perpendicular positive faces share the four edges of a square, so their correlation is exactly \(4/12=1/3\). There are three other positive faces. This refutes the enlargement for a positive row. The actual \(Q_i\) gives the **sum** of the twelve rank-one coefficient matrices. The trial used the individual normalized left Gram matrices. This trial therefore supplies no refutation of (6).


## Bounds for arbitrary square-integrable probes

**Proved.** The following explicit bounds apply at \(\beta=23/10\). They give a strict gap from one for *each* pair. The size needed in (6) is much smaller.
\[
 p\le 1-\tfrac23 e^{-2\beta\,119},\qquad
 n,m\le 1-\tfrac{494}{495}e^{-2\beta\,119},\qquad
 o_1\le \min\{m,\,1-e^{-2\beta\,132}\}.
 \tag{7}
\]
One can replace \(e^{-2\beta\,119}\) by \(2^{-822}\) and \(e^{-2\beta\,132}\) by \(2^{-911}\). Indeed \(e<5/2+(1/6)\sum_{j\ge0}4^{-j}<11/4\), hence \(e^2<8\), and \(3\beta\cdot119=8211/10,\ 3\beta\cdot132=9108/10\).

**Proved, reference comparison.** Keep the coefficient map (1) at its stated \(\beta\). For a selected pair remove from the density the plaquettes touching its 12 central tangential links, 12 neighbour tangential links and eight crossings per interface. In this reference measure all the read links have independent Haar law. For an outward face the conditional field at a given central face array is a symmetric function \(H(A_1,\ldots,A_{12})\) under **all** permutations of the twelve edges because its transported remote tangential links in (3) are independent Haar. For an inward face the field is the corresponding symmetric function followed by the rooted gauge average in (5).

For completeness, on independent Haar edges expand \(H=\sum_D H_D\), where \(H_D\) is obtained by averaging all edges outside \(D\) and applying identity minus averaging in each edge of \(D\). These commuting product projections are orthogonal for distinct \(D\) and sum to the identity by multiplication. For a symmetric \(H\), components of a given order have equal squared norms. Only components on the four edges that perpendicular faces share can pair. At order \(k\ge1\) the shared fraction of the squared norm is \(\binom4k/\binom{12}k\le 1/3\) (zero for \(k>4\)). Conditional expectation contracts variance. Thus the perpendicular outward reference coefficient is at most \(1/3\).

If one face is inward, every proper subset of the shared square is a forest. Vertex gauges fixing a single root act transitively on a forest's edge assignments, by solving along each tree starting at the fixed vertex if present. Edge-coordinate averaging commutes with fixed vertex gauges by left and right Haar invariance. The inward field's projection onto any such proper subset is therefore constant. Only the fourth-order component on the shared square can pair. On each side its norm is at most \(\binom{12}4^{-1/2}\) times the original probe standard deviation, since the rooted gauge projection is contractive and commutes with the edge projections. The reference bound is \(1/\binom{12}4=1/495\). Opposite faces read disjoint sets and have reference coefficient zero.

**Proved, transfer to the actual star.** For perpendicular faces, the removed central plaquettes number 23 because only the square at the two opposite coordinates avoids both sets of central edges. The two neighbour boxes contribute \(2(6+12)=36\). The two selected crossings contribute 24. The six remaining interfaces contribute \(4+4+4(4+4-1)=36\), counting their central edges lying in either selected face. This gives 119. For opposite faces these four counts are \(24,36,24,6\cdot8\), giving 132. If \(\nu\) is the resulting reference and \(\mu\) the full Wilson law, \(a\le d\mu/d\nu\le b\) with \(a/b=e^{-2\beta N}\) for these choices of bounds and removed count \(N\). For either sign,
\[
 \operatorname{Var}_\mu(f\pm g)\ \ge\
 a(1-\rho_\nu)(\operatorname{Var}_\nu f+\operatorname{Var}_\nu g)
 \ \ge\ (a/b)(1-\rho_\nu)(\operatorname{Var}_\mu f+\operatorname{Var}_\mu g).
\]
Here each variance is the infimum over subtracted constants, and the middle bound uses \(2xy\le x^2+y^2\). Choose the sign yielding the smaller variance for centred unit-variance probes under \(\mu\). This proves (7). Using the Haar bounds directly for the interacting measure would omit precisely this change of law.


## An explicit trial on the summed matrix

**Proved.** There is a centred probe of the actual \(Q\) giving
\[
                 p>\frac{49}{675},\qquad
          \max_i\sum_{j\ne i}\rho_{ij}>\frac{49}{225}.
 \tag{8}
\]
It also permits a direct check of how much transmission through shared raw links this probe can see.

Let \(S_i^{\rm cut}=\sum_{e\in F_i}c_{i,e}\), where \(c_{i,e}\) is the physical trace \(q(U_p)\) of its crossing plaquette. Set
\[
 T_i=\frac{\operatorname{tr}Q_i}{4\beta},\qquad
 M(Q)=\frac{\int (v^t Qv)e^{v^tQv}\,dv}{\beta\int e^{v^tQv}\,dv},
 \qquad \Phi_i=T_i-\frac14 M(Q_i).
 \tag{9}
\]
Given all internal links and all \(r_s\) in the eight interfaces, the eight pivots have independent densities proportional to \(e^{v^tQ_i v}\). There are no corner plaquettes in the star. Thus \(\Phi_i\) is the conditional expectation of \(R_i=T_i-S_i^{\rm cut}/4\) in these variables. Formula (9) defines a single bounded function on a real symmetric matrix through the displayed Haar integral.

**Proved.** In the original orientation let \(A_e,B_e\) be the source link and the target link transported to the same endpoints using the actual crossings. Then \(T_i=\sum_e q(A_e)q(B_e)\) and \(c_{i,e}=q(A_e^{-1}B_e)\). This follows by averaging (1) over its argument and by invariance of \(q\) under conjugation by the pivot. Average over independent Haar gauges at the source vertices of the interface, with the full Wilson configuration initially fixed. Each pair \(q(A_e),q(B_e)\) becomes \(h\cdot a,h\cdot b\), with \(h\) uniform on \(S^3\), \(|a|=|b|=1\), \(a\cdot b=c_{i,e}\). This follows by cyclicity and Haar invariance of the relative gauge between the two endpoints. Two distinct cube edges give independent relative gauges by the forest integral. The second and fourth coordinate moments of \(h\) are \(\delta_{ab}/4\) and \((\delta_{ab}\delta_{cd}+\delta_{ac}\delta_{bd}+\delta_{ad}\delta_{bc})/24\). Rotation invariance determines the tensor up to its coefficient, fixed by \(|h|^2=|h|^4=1\). The edge product has mean \(c_{i,e}/4\) and variance \((2+c_{i,e}^2)/48\). Since the Wilson law is invariant under these gauge changes,
\[
             \mathbb E R_i=0,\qquad
       \operatorname{Var}\Phi_i\le\operatorname{Var}R_i
            =\sum_e\mathbb E(2+c_{i,e}^2)/48\le 3/4.
 \tag{10}
\]

**Proved.** Take two positive faces, and on their fixed-plane square set \(Y=\sum_{e\in I}(q(X_e)^2-1/4)\), summing the four edges. It has mean zero and variance \(1/4\) by the same moments and the forest integral. For a shared edge its covariance with \(q(A_e)q(B_e)\) after gauge integration is \(3c_{i,e}/24-c_{i,e}/16=c_{i,e}/16\), while distinct-edge contributions vanish. The physical \(S_i^{\rm cut}\) is gauge invariant and has zero covariance with \(Y\). Because \(Y\) is measurable in the internal links, (9) now gives \(\mathbb E[\Phi_iY]=\bar c/4\), where \(\bar c=\mathbb E c_{i,e}\) is common to the twelve edges by face symmetry. The square observable is fixed by the diagonal reflection. Apply Cauchy–Schwarz for the positive reflection form on the full star, with \(\Phi_i\) supported on one closed half. It gives \(\mathbb E[\Phi_i\Phi_j]\ge(\bar c/4)^2/(1/4)=\bar c^2/4\).

**Proved.** For this star \(\bar c\ge r_1(\beta)>7/15\). Here is the finite-volume reason the open-box electric argument of 1348, lines 245–249, still applies. Reflect through the midplane \(x_\nu=1/2\) in the *tangential* direction of the selected crossing plaquette. The two halves of the star are identical. The bonds through this plane form a matching, so changing upper-half vertex frames sets them to identity and allows their original Haar values to be integrated. All straddling plaquettes then pair a tangential edge on one half with its reflected edge on the other. After integrating the interiors the same boundary weight \(F\) occurs on both sides. Vary the selected plaquette coupling \(t\) only. Dividing its factor by \(z(t)=\int e^{tq(g)}\,dg\) and the other crossing factors by their corresponding \(z(\beta)\) gives a quadratic form in \(F\) of the tensor product of the normalized electric convolutions, one per edge.

On the spin-\(j/2\) matrix coefficients, the normalized convolution has multiplier \(r_j(t)=I_{j+1}(t)/I_1(t)\), \(j\ge0\). This is 1348's one-link formula, obtained by integrating the character \(\sin((j+1)\theta)/\sin\theta\) against \(e^{t\cos\theta}(2/\pi)\sin^2\theta\,d\theta\) and dividing by \(j+1\) and \(z(t)\). Each adjacent ratio \(I_{k+1}/I_k\) for \(k\ge1\) is the positive mean of \(x\) with density proportional to \(e^{tx}(1-x^2)^{k-1/2}\) on \([-1,1]\). The derivative of this mean is its variance. The integral formula follows by expanding the exponential and integrating the even powers, or from 1348's proof at line 127. Thus every \(r_j\) is nondecreasing. By expansion of \(F\) in matrix coefficients, the normalized quadratic form is nondecreasing. Differentiating the original integrals at \(t=\beta\) therefore gives \(\bar c\ge z'(\beta)/z(\beta)=r_1(\beta)\). The recurrence \(I_{k-1}-I_{k+1}=2k I_k/t\), verified coefficient by coefficient in \(I_k(t)=\sum_{\ell\ge0}(t/2)^{2\ell+k}/(\ell!(\ell+k)!)\), gives
\[
  r_1(\beta)=\frac{\beta}{4+\beta I_3(\beta)/I_2(\beta)}
       > \frac{\beta}{4+\beta^2/6}=\frac{1380}{2929}>\frac7{15}.
\]
The last comparison is \(20700>20503\). In particular \(\Phi\) has positive variance. Normalizing (9) by its standard deviation and using (10) proves (8).

**Proved, limitation of this trial.** On an inward face, averaging the source gauges in the private neighbour gives \(\mathbb E[R_i\mid X]=0\), so \(K_i\Phi_i=0\). On an outward face \(K_i\Phi_i=\mathbb E[R_i\mid X]\) is the sum of twelve mutually orthogonal components, one for each central face edge \(st\). Each component is invariant under gauges outside \(s,t\) and has zero average at either of these two sites separately, since averaging one endpoint of \(q(A_e)q(B_e)\) gives exactly \(c_{i,e}/4\). Conditional expectation onto \(X\) commutes with these gauge projections by invariance of the joint law. Distinct endpoint sets are therefore orthogonal. All twelve component norms agree by face symmetry. Only four components can pair across two positive faces, giving
\[
       \frac{|\mathbb E\Phi_i\Phi_j|}{\operatorname{Var}\Phi_i}
       \le \frac{\operatorname{Var}(K_i\Phi_i)}
                       {3\operatorname{Var}\Phi_i}<\frac13 .
\]
The strict inequality follows from positive conditional variance on a set of central configurations of positive probability. At all central links equal to identity and all crossing links equal to identity, choosing every neighbour face link \(+1\) or every one \(-1\) gives \(Q=\pm12\beta I\) and \(\Phi=\pm9\). Continuity gives separated ranges on product neighbourhoods, both charged by the strictly positive Wilson density at each central array in a neighbourhood of identity. This also proves the variance claim without a simulation. Thus this particular family of normalized trials has a row sum strictly below one even though the separately resolved plaquette trial attains one.


## A sufficient bound involving one observed face

**Proved.** The residual angular channel on two incoming faces has norm at most \(1/8\). More generally the following three one-face quantities give a sufficient upper test. Use the outward field \(Hf\) from (5) with its **actual** joint law in (2). Take suprema over centred probes of variance one. Define
\[
 d=\sup_f\|Hf\|_2^2,\qquad u=\sup_f\|P_FHf\|_2^2,\qquad
 w=\sup_f\|(\mathrm{id}-P_{\{s\}})P_{F\setminus\{s\}}Hf\|_2^2
\]
for one corner \(s\) of \(F\). The norms use \(\mu_C\). The bounds are
\[
 n\le\max(m,1/8),\qquad
 3p+3m+o_1\ \le\ d+\max(2u,4w)+4u .
 \tag{11}
\]

To verify them, first take the private rotation average on the probe. Split the resulting probe orthogonally into its spectral part and the part with zero average under the remaining rotation. This is an orthogonal split in the probe marginal by invariance under a common central gauge. That gauge commutes with reflection and the vertex-gauge projections, so the pairings between the two parts vanish. For \(Hf\), expand the identity as \(\prod_{t\in F}(P_{\{t\}}+(\mathrm{id}-P_{\{t\}}))\). The resulting components, labelled by the set \(D\) of sites carrying identity minus averaging, are mutually orthogonal. Every component with \(D\not\subset I\) has zero pairing across the positive pair. By face symmetry the component norms are invariant under cube symmetries. Each singleton lies on three of the six square faces. A set of at least two distinct vertices lies on at most two of them, since it varies in at least one coordinate. Thus the squared norm on one shared square receives \(1/2\) of the total singleton norm squared and at most \(1/3\) of the higher-order total. Absolute cross pairings are bounded by the corresponding norms by Cauchy–Schwarz.

For the spectral part, after all other sites have been averaged, invariance under a common gauge implies invariance at the one remaining site. Hence the singleton component vanishes. The empty component has squared norm at most \(u\). This gives the upper bound \((d+2u)/3\) on \(p\) in this sector. For the angular part the empty component vanishes, since full vertex averaging includes the common gauge. All eight singleton norms agree and each squared norm is at most \(w\). The bound on \(p\) in this sector is \(d/3+(1/2-1/3)8w=(d+4w)/3\). For the negative pair the angular sector can use only the one root, whose squared norm is at most \(1/8\) by orthogonality and \(d\le1\). Its spectral sector gives precisely the fully averaged perpendicular pairing in (6). Finally \(o_1\le m\le u\), proving (11).

**Scope of (11).** The three quantities use one face marginal and one conditional arm law. The other arms still tilt that marginal through (2). Their norms can overpay information private to a single face. For instance, with independent Haar central links an artificial symmetric face observation \(\prod_{e\in F}\operatorname{sign}q(X_e)\) has \(d=1\). Each pair is independent by integrating a private fair edge sign on each side. Thus mere conditional-variance contraction and pair transmission are genuinely different tests on this geometry. A quantitative upper estimate of (11) for the Wilson sum (1) is open.

## Spectral trials from arm partition functions

**Proved.** There are also explicit probes whose conditional fields see only physical boundary data. Write \(h_s(Q)=\int e^{s v^tQv}\,dv\), and use \(B_i(s)=h_s(Q_i)/h_1(Q_i)\). Let \(Z\) denote the star mass with weights \(e^{\beta q}\). In \(Z_i(s)\) the crossing coupling on arm \(i\) is \(s\beta\). In \(Z_{ij}(s,t)\) the two indicated couplings are \(s\beta,t\beta\), with every other coupling kept. Integration of the pivots gives
\[
 \mathbb E B_i(s)=Z_i(s)/Z,\qquad
 \mathbb E B_i(s)B_j(t)=Z_{ij}(s,t)/Z,\qquad
 \mathbb E B_i(s)^2\le Z_i(2s-1)/Z.
\]
The last inequality is \(h_s^2\le h_1 h_{2s-1}\) by Cauchy–Schwarz. In particular \(K_i B_i(0)=z_2/L_i(X_{F_i})\), since dropping that interface leaves just the open neighbour. The local pressure variation proved below and the full support of the central density give \(u>0\) in (11). For the zero-coupling probe the second-moment upper bound is one, since \(Z_i(-1)=Z\). Multiplying each crossing link at transverse vertex \(s'\) by the checkerboard sign \((-1)^{|s'|_1}\) reverses all twelve crossing traces and affects no other star plaquette.

For a common parameter \(s\) with positive variance on both faces, their marginal laws agree and the following lower bound uses ordinary partition functions alone:
\[
 \rho_{ij}\ \ge\
 \frac{|Z\, Z_{ij}(s,s)-Z_i(s)^2|}{Z\,Z_i(2s-1)-Z_i(s)^2}.
 \tag{12}
\]
It follows by centring and normalizing the actual \(B_i(s)\). These conditional fields are the central-gauge-invariant ratios \(L_i^{(s)}(A)/L_i(A)\), where \(L_i^{(s)}\) changes just the crossing coupling. Thus (12) supplies the same perpendicular trial bound for all sign choices. Its interacting partition ratios have not been evaluated here.

## The unnormalized pivot step

**Proved using prior work.** The fixed-central-array arm weight \(L(A)\) in (2) has appreciable variation already in pure Wilson. In row 1348 (17), let \(f\) be the normalized open \(2^4\)-box face density on its twelve tangential links. The ratio of the mass of two joined boxes to \(z_2^2 z(\beta)^{12}\) is exactly \(J=\int f L\,dA/\int L\,dA\), since Haar integration of the transported crossing kernel gives \(\int L\,dA=z_2 z(\beta)^{12}\). Use the existing bound \(J\ge1+24r_1(\beta)^6\). By the rational estimate above, \(J>6/5\), since \(120\cdot7^6>15^6\). Any scalar \(c\) with \(\sup_A|\log L(A)-c|\le\delta\) gives \(J\le e^{2\delta}\), hence \(\delta>\tfrac12\log(6/5)>1/12\) by integrating \(1/t\) on \([1,6/5]\). This rules out a uniform \(1/100\) **scalar-only approximation of this local arm**. Its variation may be carried as a local interaction. [1348, (17)](gap-blockstep3-astra62.md) · [1350, verification of (17)](gap-blockstep3-check-opus.md)

**Proved implication.** On each torus keep \(Z^z(\tau)=c_2^{V_\tau}\mathcal I^z_\tau\) with \(V_\tau\) its number of coarse sites, \(c_2=e^{-6\beta 2^4}z_2\), and \(\mathcal I^z_\tau\) the full remaining *unnormalized* integral of (1) of row 1348, including the signed corner tensors. There are eight twists at each of \(\tau=v,2v\). With \(Z_+(\tau)=2^{-3}\sum_z Z^z(\tau)\), the neutral purity is \(P=Z_+(2v)/Z_+(v)^2\). A common site pressure cancels since \(V_{2v}=2V_v\). Uniform per-mass log error at most \(\delta\) after that common adjustment gives log-purity error at most \(3\delta\), by positivity of the twist averages and the triangle inequality. The zero-transverse-corner pivots have product Haar marginal by the forest argument, even in the twisted laws. Their marginal normalization discards exactly the scalars needed for this comparison. These pressure identities are the ones in 1475 §5. A positive answer to the local test would supply a transmission bound on this open star. Carrying it through a join requires the charged boundary variables, the four-linear tensors and a bound on the winding contribution to these sixteen log masses. The single-arm lower bound above concerns local variation, and gives no lower bound on that winding contribution.


**Proved.** The spectral trial \(B_i(0)\) in (12) has strictly positive correlation even on opposite faces. Put \(F(A)=z_2/L(A)\). In (2) its conditional field on each opposite face is precisely \(F\), a continuous nonconstant function by the preceding arm bound. Reflect through \(x_\mu=1/2\) in the normal direction of this pair. The two interface-side central tangential arrays now lie on the two boundary slices of the reflection cut. Use the electric matching change of variables from the proof of (8). It preserves \(F\) under the boundary vertex gauges. If \(\Psi>0\) is the common half weight after its interior is integrated, \(\bar F\) is the Wilson mean, and \(C\) is the product of normalized electric convolutions across the cut, the covariance of the two probes is
\[
 \frac{\langle\Psi(F-\bar F),\,C\,\Psi(F-\bar F)\rangle}
      {\langle\Psi,\,C\,\Psi\rangle}.
\]
Here \(F\) uses the central cube of the slice, and both \(\Psi\) and \(C\) use the full slice including the transverse neighbours. Each electric multiplier \(I_{j+1}(\beta)/I_1(\beta)\) is strictly positive. By the product matrix-coefficient basis the quadratic form of \(C\) is strictly positive on every nonzero vector. The numerator vector is nonzero since \(\Psi>0\) and \(F\) is nonconstant. The diagonal Cauchy–Schwarz argument in (6), applied to this same fully gauge-averaged trial, gives at least this covariance on perpendicular faces. Thus \(0<o_1\le m\le n\le p\) in the actual star. Disjoint raw reads on opposite faces still transmit physical information.

**Proved, quantitative lower bound for every pair.** In fact the same opposite-face trial gives
\[
         o_1\ \ge\ 16\,r_1(\beta)^{20}e^{-576\beta}>2^{-2024}.
 \tag{13}
\]
To see how positivity can be quantified, normalize \(l=L/[z_2 z(\beta)^{12}]\). In the notation of the pressure bound, \(l=Cf\), since the convolution on the twelve central face edges integrates the normalized boundary weight \(f\) of the neighbour. The remaining slice edges carry constants in this identity. The 24 internal plaquettes in the neighbour give \(0<f,l\le K=e^{24\beta}\), since \(z_2\ge1\) by Jensen and each plaquette has zero mean under product Haar. For a central face square let \(q_\square\) be its normalized trace. Its Haar mean is zero and its squared Haar norm is \(1/4\). Convolution on its four edges gives \(Cq_\square=r_1^4 q_\square\), by the fundamental multiplier on each link. The open-box estimate of 1348 at line 249 gives \(\langle f,q_\square\rangle\ge r_1\). Consequently \(\|a-l\|_2^2\ge4r_1^{10}\) for every real constant \(a\), by pairing with \(q_\square\). These norms and inner products are for product Haar on one slice.

Rescale the probe to \(z(\beta)^{12}B_i(0)\), so its conditional field is \(1/l\). Put \(a=1/\mathbb E_{\mu_C}(1/l)\), hence \(0<a\le K\), \(U=\Psi(1/l-1/a)\), and \(g=a-f\). Then \(Cg=a-l\) and
\[
 \langle U,Cg\rangle=\int\frac{\Psi}{a l}(a-l)^2
       \ge \frac{4(\inf\Psi)r_1^{10}}{K^2},\qquad
 \langle g,Cg\rangle\le\|g\|_2^2\le K^2.
\]
Cauchy–Schwarz for \(C\), followed by \(\langle\Psi,C\Psi\rangle\le(\sup\Psi)^2\), bounds the rescaled covariance below by \(16r_1^{20}(\inf\Psi/\sup\Psi)^2/K^6\). The rescaled variance is at most \(z(\beta)^{24}\le e^{24\beta}\) by the checkerboard identity. The seven open three-cubes and the six crossings with four links each give \(7\cdot12+6\cdot4=108\) spatial edges in the slice. There is one midplane plaquette per such edge, leaving \((312-108)/2=102\) plaquettes in each reflected half. Therefore \(\inf\Psi/\sup\Psi\ge e^{-204\beta}\). Substitution proves (13). For its rational version use \(r_1>1/4,\ e^2<8\), and \(36+864\cdot23/10<2024\). This lower bound comes from the actual eigenvalue probe on the original continuous matrices.

## Margin for a rational Wilson-weight certificate

**Proved using 1348 (13).** Keep the continuous matrix map (1). Replace each of the 312 Wilson factors by the positive rational degree-ten minorant \(P_\beta(q)\) from that row and denote the resulting maximum row sum by \(R_P\). The ratio of the largest to smallest reweighting factor is bounded by
\[
 D=(1+13\,2^{-20})^{312}
 \le (1-4056\,2^{-20})^{-1}<251/250.
\]
Use \((1+x)^{312}\le e^{312x}\le(1-312x)^{-1}\) at \(x=13\,2^{-20}\). Applying the variance comparison in (7) in both directions gives \(D^{-1}(1-\rho_P)\le1-\rho\le D(1-\rho_P)\) for each pair. Consequently \(R_P\le122/125\) proves the requested strict Wilson inequality. A row sum at least \(257/251\) for explicit polynomial-law trials proves a strict Wilson refutation using the same trials re-centred and re-normalized. For the latter claim apply the same comparison in the affine spans of the individual trial functions, in which the maximal coefficient is their absolute correlation. Both margins allow for all seven terms.

**Proved scope.** At the polynomial weight, any specified rational polynomial trial and its first two moments have exact rational Haar integrals. Expand (1) in the original real quaternion coordinates. In one link all odd coordinate monomials integrate to zero, and a monomial with exponents \(2a_k\), \(A=\sum a_k\), integrates to \(\prod_k(2a_k-1)!!/[2^A(A+1)!]\) by separating a four-dimensional standard Gaussian into radius and direction. A degree-\(k\) trial needs degree at most \(60+4k\) in each original link for second moments, from at most six incident degree-ten plaquette weights and at most two copies of the pivot per summand in (1). The uncompressed product monomial space for the 352 links has up to \(\binom{64+4k}{4}^{352}\) coordinates at that bound. Finite-degree cubature can certify these trial moments. The upper alternative requires control of *all* probes, including the orthogonal complement of any chosen finite test space. A matrix of moments of selected probes alone gives a lower bound on the supremum.

**Result — open.** Combining (6)–(8) and (13) gives \(49/225+4\cdot2^{-2024}<R\le 7-(2966/495)2^{-822}\). The interval contains one. Pure-Wilson descent and winding-pressure control also remain open. All new estimates have written hand arguments with exact constants. No numerical result or Lean computation is used as evidence. This is author research and grants no status.

## Next two rows and their decisive outcomes

1. **Sketched. Certify the row for the summed matrices.** Bound the one-face quantities in (11) in the tilted star marginal, or bound the positive reflection forms in (6) directly, including their high-degree remainder. A strict upper bound below one in (6) or (11) certifies local transmission. For refutation, use (12) or rational polynomial probes to evaluate trial correlations by ordinary finite integrals. Certified lower bounds summing to at least one decide the negative case. The rational margins above allow the comparison back to the Wilson law without discretizing the class of probes.
2. **Sketched, conditional on a local pass. Test one join with charged boundary variables.** Keep the shared links and all four-linear corner tensors and carry each of the sixteen unnormalized masses. The positive outcome is an explicit contraction stable under joins with a common bulk pressure and the winding error required for the \(1/100\) budget of 1471, or a strict decrement with a quantified scalar error for the next step. A charged boundary probe violating the proposed bound after a join refutes that extension. A local refutation in the first row ends this particular gluing route. [End-class conditions](gap-k2-end-class-fable.md)
