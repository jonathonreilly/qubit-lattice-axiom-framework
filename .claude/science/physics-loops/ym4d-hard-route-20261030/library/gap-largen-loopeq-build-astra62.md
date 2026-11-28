# Repo search

The lead searched main and PRs 10114, 10133, 10134 and 10141. I checked the November 8 digest, main at `8b11ae2bb`, and the YM4D source paths on those PRs. The closest outside-lane hit was `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on PR 10114, lines 106–149. It gives a positive one-step transfer witness. Row 1710, `prior/gap-largen-lit-luna.md`, gives the published identities and small-coupling bounds. There was no target-specific prior file or matching owner in `open-registry.md`.

Within the lane, `gap-loop-grow-astra.md`, Theorem B, already determines the SU(2) law from full finite-volume Ward data. The marked-edge calculation in `gap-purity-mp-strategy-fable.md` §3.8 stops at repeated visits. Theorem A in `gap-mixed-opus.md` concerns SU(2) Langevin dynamics. The new estimate below integrates a plaquette Hessian against the Wilson law at large rank.

I checked the outline index, the neighboring entries in chunks 01 and 29, and the matching obligations. The 4.12–4.19 account index yielded no master-loop result. Outline lines 588–599 and 31871–31882 give a spectral example with decay $(1+t)^{-2}$ and support down to zero. Lines 778–779 limit the scalar block estimate. CA-I 2705–2710 lists “a mass gap” among the conclusions left open. These observations come from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at `31a47c543775`. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L588) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2705)

## Result

**PROVED here by hand, pending independent review.** For 4D Wilson SU(N), fix $0\le b_0<1/(4\sqrt{22})$ in the convention $Nb\,{\rm ReTr}U_p$. For all sufficiently large finite $N$, the finite-rank moment equation has a unique normalized solution in the class below. Its heat step contracts in a gradient norm. A second contraction for the Poisson equation gives exponential decay of $N^2$ times the connected Wilson-loop correlation. Both rates are uniform in volume and $0\le b\le b_0$.

For $N\ge1024$ and $b\le1/20$, the spatial rate is at least $\log(12/11)$ in lattice units. The range includes $1/24<b\le1/20$. At $b=1$, an explicit trial law rules out this absolute contraction on the full one-form space. The SU(2) specialization at the end addresses the purity card.

This is research text at checkout `3ebf83885`. The proof is analytic. Lean verification and independent review are pending. This note grants no repository status.

## A conditional estimate for one SU(N) link

Use $d\mu=Z^{-1}\exp(Nb\sum_p\operatorname{ReTr}U_p)\,dU$, one orientation per unit square. Here $dU$ is product Haar, $U_p$ is the ordered link product around $p$, and $D=2(d-1)$. Use the unscaled Hilbert–Schmidt metric on anti-Hermitian traceless matrices. Condition on all links except $h$. Its density is proportional to $\exp(Nb\operatorname{ReTr}(QH))$. Each incident plaquette contributes a unitary matrix to the staple $H$. Thus $\|H\|_{\rm op}\le D$. Let $\operatorname{tr}=\operatorname{Tr}/N$.

**PROVED. Lemma 1 (the SU(N) trace correction).** Fix $N\ge3$, $b>0$ and $\delta=1/2-bD>0$. Put $Y=\operatorname{Im}\operatorname{tr}(QH)$ and $m_N=D[\tan(\pi/N)+1/(N\sqrt\delta)]$. For any smooth real or complex vector $v(Q)$ in a fixed Euclidean space, the conditional expectation obeys

$$
 E_h[|Y|\,|v|^2]\le m_NE_h|v|^2+
 \frac{2D}{N^{3/2}\delta}E_h[|v|\,|\nabla_h v|].
 \tag{1}
$$

**Proof.** Put $\theta=2\pi/N$. Multiplication by $e^{\pm i\theta}I$ preserves Haar measure on SU(N). The ratio of the rotated density to the original density has expectation one. Jensen's inequality gives $\pm\sin\theta\,E_hY\le(1-\cos\theta)E_h\operatorname{Re}\operatorname{tr}(QH)$. Hence $|E_hY|\le D\tan(\pi/N)$.

In the chosen metric, ${\rm Ric}(X,X)=N|X|^2/2$. Indeed, the bi-invariant connection is $\nabla_XZ=[X,Z]/2$ in left-invariant frames. Its Ricci form is $\frac14\sum_a|[X,T_a]|^2$. Diagonalize $X=i\,{\rm diag}(x_j)$. The two real off-diagonal basis vectors for $j<k$ each contribute $(x_j-x_k)^2$. Their total is $2N\sum_j x_j^2$, since $\sum_jx_j=0$. Along $Q(t)=e^{tX}Q$ the absolute second derivative of $\operatorname{ReTr}(Q(t)H)$ is at most $D\,{\rm Tr}(-X^2)$. This follows by diagonalizing the positive matrix $-X^2$. The weighted Ricci form is therefore at least $\kappa=N\delta$.

Let $S_h=Nb\,{\rm ReTr}(QH)$, $L_h=\Delta_h+\nabla S_h\cdot\nabla$, and let $P_t$ be its heat semigroup. In a normal frame, differentiating $|df|^2/2$ twice yields $|\nabla df|^2+\langle df,\nabla^i\nabla_i df\rangle$. Commuting the last derivative gives $\nabla^i\nabla_i df=d\Delta f+{\rm Ric}\,df$. The drift contributes $-{\rm Hess}\,S_h(df,df)$ after subtracting $\langle df,dL_hf\rangle$. Thus the Bochner identity gives $(\partial_t-L_h)|\nabla P_tf|^2\le-2\kappa|\nabla P_tf|^2$. The maximum principle yields ${\rm Lip}(P_tf)\le e^{-\kappa t}{\rm Lip}(f)$. On the compact connected group this bound and stationarity give uniform convergence to $E_h f$. Integration of $-\partial_t E_h[(P_t f)^2]=2E_h[|\nabla P_t f|^2]$ for real $f$ gives ${\rm Var}_hY\le{\rm Lip}(Y)^2/\kappa$. Cauchy–Schwarz for the trace gives ${\rm Lip}(Y)\le D/\sqrt N$. Consequently $E_h|Y|\le m_N$.

For $F=|Y|$, integrate $-\partial_t P_tF$ against $|v|^2$. Reversibility gives ${\rm Cov}_h(F,|v|^2)=\int_0^\infty E_h\langle\nabla P_tF,\nabla |v|^2\rangle\,dt$. The Lipschitz bound gives (1). One can first use $F=(Y^2+\epsilon^2)^{1/2}$, with the same Lipschitz constant, and pass to the limit. This proves the lemma.

## The plaquette Hessian in the quadratic form

**PROVED. Lemma 2.** Assume $N\ge3$, $b>0$ and $\delta>0$ as in Lemma 1. Use a finite box with free boundary or a periodic cube of side at least five. Permit a multiplier $s_p\in[0,1]$ on each plaquette. Write $S=Nb\sum_p s_p\operatorname{ReTr}U_p$ and take $E$ under the resulting Wilson law. Let $\alpha$ be a smooth real one-form on the full product of link groups. Write $A=\|\alpha\|_{L^2(\mu)}$, $B=\|\nabla\alpha\|_{L^2(\mu)}$, and put

$$
 c=N-1/N,\qquad r=N/c,\qquad k=4\sqrt{D/3}.
$$

Then, with indices of the Hessian raised using the product metric,

$$
 \big|\langle\alpha,{\rm Hess}\,S\,\alpha\rangle_\mu\big|
 \le N\,4Db^2r(D+m_N)A^2+
 2\sqrt N\,b k\left(\sqrt r+\frac{bDr}{N\delta}\right)AB .
 \tag{2}
$$

**Proof.** Write the component at link $e$ as a matrix $A_e$ in the frame $XQ_e$, and put $u_e=|A_e|_{\rm HS}$. Differentiate the plaquette along product geodesics twice, with the velocities fixed. Each square gives 16 ordered terms indexed by its sides $e,f$. If $e=f$, insert $A_e^2$. For distinct sides insert one matrix at each side. An inverse link gives the insertion on the other side with the derivative sign. Denote the real trace for the resulting bilinear term by $C(A_e,A_f)$, including its sign. By cyclicity, unitary invariance and Hilbert–Schmidt Cauchy–Schwarz, $|C(V,W)|\le |V||W|$. The two slots may use the same vector.

Choose $h$ uniformly among the sides outside $\{e,f\}$. With the two slots fixed the trace is linear in $Q_h$ or $Q_h^*$, over the reals. For an orthonormal basis $T_a$ of $\mathfrak{su}(N)$, $-\sum_a T_a^2=cI$. The sum commutes with conjugations, and its trace is $N^2-1$. Thus the partial Laplacian in that occurrence gives $-cC$. Write $C_a$ for its partial first derivative in direction $T_aQ_h$. Conditional integration by parts gives

$$
 c\,E C(A_e,A_f)=
 E\sum_a\big[C_a(X_a A_e,A_f)+C_a(A_e,X_a A_f)
                  +(X_aS)C_a(A_e,A_f)\big].
 \tag{3}
$$

Here $X_a$ differentiates only $h$. Formula (3) follows by integrating the total derivative of $C_a(A_e,A_f)e^S$ in Haar measure. Along $h\ne e$ the product connection differentiates $A_e$ componentwise.

The first sum costs at most $\sqrt c\,|\nabla_h A_e|u_f$. Indeed, move $X_a A_e$ to the front of the trace. Its Hilbert–Schmidt partner contains $T_a$ and $A_f$, separated by unitary matrices independent of $a$. The squared norms of those partners sum to $c|A_f|^2$ by $-\sum_a T_a^2=cI$, in either order. Cauchy–Schwarz over $a$ proves the assertion. The other differentiated slot costs $\sqrt c\, u_e|\nabla_h A_f|$.

The right-frame score is the projection of $-Nb\,{\rm skew}(Q_hH)$ onto traceless matrices, where ${\rm skew}(M)=(M-M^*)/2$. Its operator norm is at most $Nb(D+|Y_h|)$, with $Y_h$ from Lemma 1. Inserting this score once in the trace costs at most $Nb(D+|Y_h|)u_eu_f$. This step keeps the operator norm on the score and the Hilbert–Schmidt norm on the other two slots.

Give a tuple $(p,e,f,h)$ weight $t=s_p/(4-|\{e,f\}|)$. Both $\sum t E u_e^2$ and $\sum t E u_f^2$ are at most $4DA^2$. Also $\sum t E|\nabla_h A_e|^2\le(4/3)B^2$. Indeed, two distinct sides $e,h$ lie in at most one square. Within it $f=e$ costs $1/3$. Each of the two other available $f$'s costs $1/2$. The same count holds with $e,f$ exchanged. Thus each differentiated-slot sum, without $\sqrt c$, is at most $k AB$. Use $2u_eu_f\le u_e^2+u_f^2$ in the scalar-score term. Applying (1) conditionally and using the same two counts yields

$$
 \sum t E |Y_h|u_eu_f\le 4D m_N A^2+
                  \frac{2D k}{N^{3/2}\delta}AB .
$$

Insert these estimates into (3), multiply by $Nb/c$ on its right-hand side, and sum. This gives (2). Real and imaginary parts give the Hermitian quadratic-form version for complex one-forms.

## A contraction with finite propagation in the link index

**PROVED.** Set

$$
 v=4Db^2r(D+m_N),\qquad
 u=bk\left(\sqrt r+\frac{bDr}{N\delta}\right),\qquad
 \eta=\tfrac12-v-u^2,\qquad q=v+\sqrt{v^2+2u^2}.
 \tag{4}
$$

When $\eta>0$, $q<1$. Work in $L^2(\mu;T^*G^E)$. Write $L=\Delta+\nabla S\cdot\nabla$ on functions, with $\Delta\le0$. On one-forms use the operators

$$
 H_0=\nabla_\mu^*\nabla+(N/2)I,\qquad
 H_1=H_0-{\rm Hess}\,S,\qquad
 K=H_0^{-1/2}({\rm Hess}\,S)H_0^{-1/2}.
 \tag{5}
$$

All are defined first by their forms on the compact product. The Hessian multiplier is smooth and bounded there. The product connection preserves the subbundle belonging to each edge. Hence $H_0^{-1/2}$ preserves the edge index, even though its result can depend on all link values.

The $H_0$ form equals $B^2+NA^2/2$. Divide (2) by this expression. In the variables $(\sqrt{N/2}\,A,B)$, the numerator is bounded by the quadratic form of the matrix with rows $(2v,\sqrt2 u)$ and $(\sqrt2 u,0)$. Its largest eigenvalue is $q$. Thus $\|K\|\le q$. Completing the square in (2) also gives $H_1\ge N\eta I$. The estimate holds on the entire space of one-forms.

The weighted Bochner commutation identity is $d(-L)=H_1d$. For the Laplacian the first derivative commutes past the second covariant derivatives with the Ricci term. Differentiating the drift gives two terms, the drift on the one-form and ${\rm Hess}\,S\,df$. This yields (5) with the displayed minus sign. This is the Helffer–Sjöstrand covariance method on one-forms. For smooth $g$, solve $-Lw=g-\mu g$ with mean zero. On the finite compact connected product the kernel consists of constants, by $\langle f,-Lf\rangle=\|df\|^2$. Ellipticity gives a smooth solution. Then

$$
 dw=H_0^{-1/2}(I-K)^{-1}H_0^{-1/2}\,dg.
 \tag{6}
$$

In particular $z_{j+1}=H_0^{-1/2}dg+Kz_j$ contracts by $q$ per step. This solves the differentiated Poisson equation for the loop generator. The norm on $dw$ in this iteration is $\|H_0^{1/2}dw\|_2$.

Join two distinct edges when they belong to the boundary of a common square. Define $R$ as the graph distance between the edge supports of $f$ and $g$. The $(e,h)$ block of ${\rm Hess}\,S$ vanishes unless $e=h$ or the two edges are adjacent. Each multiplication by $K$ can advance the one-form index by at most one graph step. Integration by parts gives ${\rm Cov}(\bar f,g)=\langle df,dw\rangle_\mu$, using the Hermitian inner product. In (6) every term of degree $j<R$ has zero pairing. Since $\|H_0^{-1/2}\|\le\sqrt{2/N}$, summing the remaining terms yields

$$
 |{\rm Cov}(\bar f,g)|\le
 \frac{2}{N(1-q)}\|df\|_{2,\mu}\|dg\|_{2,\mu}\,q^R .
 \tag{7}
$$

In (7), $q^0=1$. Each step can change the one-form index by at most one, while $H_0^{-1/2}$ can spread coordinate dependence across the box.

## The range and the boundary

**PROVED.** In four dimensions $D=6$. For each fixed

$$
 0\le b<b_*=\frac1{\sqrt{352}}=\frac1{4\sqrt{22}}
 \tag{8}
$$

there is $N_0(b)<\infty$ such that (4) contracts for every $N\ge N_0(b)$. The constants can be chosen uniformly on each closed subinterval $[0,b_0]$ of (8). In fact $\delta>0$ there, $m_N\to0$, and $\eta\to1/2-176 b^2$. All losses in (4) increase with $b$ and decrease with $N$. One may choose $N_0$ as the first integer $N\ge3$ with $\eta_N(b_0)>0$. At $b=0$ the score and $K$ vanish directly.

An explicit rectangle is $0\le b\le 1/20,\ N\ge1024$. Here $\delta\ge1/5,\ r<1001/1000,\ m_N<1/12$. Indeed $\tan(\pi/N)\le2\pi/N<8/N$ and $\sqrt5<3$. Also $bDr/(N\delta)<1/500$. Thus $v<11/30$ and $u^2<13/160$, by substitution in (4). It follows that $\eta>1/20$ and $q<11/12$. For the last inequality, $q$ solves $q^2-2vq-2u^2=0$, and $(11/12)^2-2(11/30)(11/12)-2(13/160)=1/180>0$.

**PROVED. Fixed exterior links.** Take as active edges those with both endpoints in an ordinary coordinate box. A unit square which meets an active edge has four active edges or just one. In the latter case one coordinate crosses a box face. Its two vertices inside the box form the single active edge. Its action is a linear staple there. This also permits interpolation of any such boundary action from zero to its full value. Conditioning a single active link still gives the law of Lemma 1 with $\|H\|_{\rm op}\le D$.

Let $d_e$ count full squares at $e$. Define $A_i^2=\sum_e(d_e/D) E u_e^2$ and $A_o^2=A^2-A_i^2$. For full squares the count $4DA^2$ in Lemma 2 becomes $4DA_i^2$. The $4B^2/3$ count is unchanged. Thus its bound uses $A_i$ wherever (2) uses $A$. Each boundary term has only a diagonal Hessian, of absolute size at most $Nb\, u_e^2$. There are at most $D-d_e$ such terms at $e$. The total absolute form is bounded by $Nv A_i^2+2\sqrt N u A_i B+NbD A_o^2$. Compare with $B^2+NA_i^2/2+NA_o^2/2$. The contraction factor is at most $\bar q=\max(q,2bD)<1$, and the lower bound on $H_1/N$ is $\bar\eta=\min(\eta,\delta)>0$. Boundary terms preserve the edge index. Thus (7) holds with $\bar q$, uniformly in the exterior assignment. On the explicit rectangle $\bar q\le11/12$ and $\bar\eta\ge1/20$.

## The finite-rank master equation

**PROVED.** On a free or periodic lattice let $\mathcal W$ be the algebra spanned by products of normalized traces of closed lattice paths, as actual functions on $G^E$. Reversing a path gives the conjugate trace. Thus all finite-rank trace identities are imposed. A normalized moment law here is a bounded linear functional in the uniform norm on $\mathcal W$, taking $1$ to $1$. This includes expectations under arbitrary probability laws on link configurations.

For a product $F=\prod_i W_{\ell_i}$, the symmetrized finite-$N$ master equation is $\nu(LF)=0$. To see the marked equations, integrate the Haar derivative of $(X_a W_{\ell_i})\prod_{j\ne i}W_{\ell_j}\,e^S$ at one edge, and sum over $a$. Sum these identities over $i$ and the edge to get the displayed stationarity equation. Each visit inserts $T_a$, with the reverse-link derivative carrying a minus sign. The same visit twice gives $-cI$. For two visits the coefficient identity is

$$
 \sum_a(T_a)_{ij}(T_a)_{kl}=-\delta_{il}\delta_{jk}
                                    +N^{-1}\delta_{ij}\delta_{kl}.
$$

Indeed the $T_a$ form a complex orthonormal basis of the traceless matrices and $T_a^*=-T_a$. The two terms are the matrix entries of the traceless projection with this sign. Contracting within one word cuts the trace. Contracting across words joins two traces. Taking the second word from $S$ gives the plaquette deformation and the SU(N) trace correction. Thus $L\mathcal W\subset\mathcal W$. This construction includes repeated edges, inverses, and products. Jafarov's finite-$N$ formula gives the marked identity for the loop sequences specified there. [Jafarov, Theorem 8.1](https://arxiv.org/abs/1610.03821)

Here is a norm and a time step on the moment hierarchy itself. Complete $\mathcal W/\mathbb C1$ in $\|F\|_{\nabla}=\|dF\|_{2,\mu}$. The weight is given explicitly by the bare Wilson action. Take $P_t=\exp(tL/N)$. The commutation in (5) gives $dP_tF=\exp(-tH_1/N)dF$. Therefore

$$
 \|P_tF\|_{\nabla}\le e^{-\eta t}\|F\|_{\nabla}.
 \tag{9}
$$

The transposed time-one step contracts differences of normalized moment laws by $e^{-\eta}$ in the dual norm, whenever this norm is finite. Equation (6) gives a second, geometric iteration for the inverse on centered sources. The two rates refer to different operators. Spatial decay follows directly from (6).

The heat step preserves the completed loop algebra. Let $J$ be the closure of the loop polynomials, including constants, in unweighted Haar $L^2$. The Haar Laplacian $\Delta$ preserves the finite-dimensional span of loop products of total length at most $m$. Its spectral projections preserve these spans, by the coefficient identity above. Hence $J$ reduces the Haar heat operator. The Wilson multipliers $S,\Delta S,|dS|^2=(\Delta S^2-2S\Delta S)/2$ preserve $J$, as do $e^{\pm S/2}$ by their uniformly convergent series. Conjugating $-L$ by multiplication by $e^{S/2}$ gives $-\Delta+(\Delta S)/2+|dS|^2/4$. Its bounded real potential preserves $J$, and so does its heat semigroup, by the bounded-perturbation series. This proves $P_t J\subset J$.

Every smooth element of $J$ has loop-polynomial approximants in $C^2$. Use the low-frequency Haar spectral projection $\mathbf{1}_{[0,M]}(-\Delta)$. The cutoff sends each loop polynomial to a loop polynomial by the finite-dimensional observation. The cutoff has finite-dimensional range on the compact product. Its image on the loop polynomials is therefore closed and contains the image of $J$. For smooth functions the tails tend to zero in every Sobolev norm, by applying powers of $I-\Delta$. Sobolev embedding gives $C^2$ convergence. In particular the smooth $P_tF$ have these approximants. This argument also justifies extension of (9).

If $\nu(LF)=0$ on loop polynomials, uniform continuity and the $C^2$ approximants give $\nu(LP_tF)=0$. Thus $\nu(P_tF)=\nu(F)$. In finite volume $P_tF$ converges uniformly to $\mu F$. For instance (5) gives the scalar gap by applying $d$ to each nonconstant eigenfunction, and one further fixed heat step maps $L^2$ continuously to $C^0$ by compact elliptic smoothing. It follows that $\nu F=\mu F$. This proves uniqueness in the specified class, also for any solution of all the marked equations. A singular initial probability law may have infinite dual energy norm at time zero. Finite-volume smoothing makes its evolved law have a smooth density at positive time. The uniform claim in (9) is the rate in the stated norm. Finite-volume uniqueness alone was already available for full Ward data in $\mathrm{SU}(2)$ in `gap-loop-grow-astra.md`, Theorem B.

## Connected loops and the volume limit

**PROVED.** Let $W_\ell=N^{-1}{\rm Tr}\,U_\ell$ and let $|\ell|$ count edge visits. At an edge visited $n_e$ times, each differentiated term has components $N^{-1}{\rm Tr}(T_a V)$ up to sign, with $V$ unitary. Bessel's inequality bounds their squared sum over $a$ by $1/N$ for one visit. The triangle inequality and $\sum_e n_e^2\le|\ell|^2$ give $\|dW_\ell\|_\infty\le|\ell|/\sqrt N$. The same bound uses the total length for a product, since $|W_\ell|\le1$. Thus on the explicit rectangle

$$
 N^2\big|\,\mu(W_\ell W_{\ell'})-\mu W_\ell\,\mu W_{\ell'}\,\big|
 \le 24|\ell|\,|\ell'|(11/12)^R .
 \tag{10}
$$

Reverse a loop to place a conjugate on either factor. On a compact subinterval of (8), use $2\bar q^R/(1-\bar q)$ in place of $24(11/12)^R$, with $\bar q<1$ chosen at its upper endpoint and its minimum rank. This controls the fluctuation scale $N^2{\rm Cov}$.

To pass to infinite volume, fix a local smooth $f$ inside a cube. Multiply each boundary staple by $t\in[0,1]$. Differentiating its expectation in $t$ gives a sum of covariances with $Nb\,{\rm ReTr}(Q_e V)$, with $V$ fixed and unitary. This observable has gradient norm at most $Nb\sqrt N$. If the boundary edges have distance at least $R$ from the support, (7) bounds the total change from free to fixed exterior by

$$
 \frac{2 b\sqrt N}{1-\bar q}\|df\|_\infty\,|\partial P|\,\bar q^R ,
 \tag{11}
$$

where $|\partial P|$ counts squares having a single active edge. For side $L$ the count is $O_d(L^{d-1})$. The distance grows at least linearly in the side for fixed support. Each graph step changes an edge midpoint by at most one in each coordinate. Thus (11) tends to zero, uniformly in all fixed exterior fields. For a Wilson product its prefactor is also uniform in $N$.

Product compactness gives a subsequential Gibbs law from free cubes. Indeed a fixed inner conditional expectation is continuous in its finitely many exterior links, by the finite Haar integral and positive denominator. Passing the conditional-expectation identity against exterior cylinder tests to the limit gives the Gibbs specification. For any two Gibbs laws, condition them on the outside of the same growing cube. Each conditional mean differs from the same free mean by (11). Equality follows for smooth local tests, which are dense on finite products. This proves uniqueness of the infinite-volume Gibbs law. Free and periodic limits coincide by the same interior specification. Equation (10) passes to that law. It also holds for each subsequential limit of the scaled covariances at large rank.

**PROVED. The fluctuation estimate has nonzero local variance.** On the explicit rectangle take one simple plaquette $p$ in the bulk. Integration by parts at one of its links gives $c\,\mu W_p=\mu\sum_a(X_aS)X_aW_p$. The score estimate in (3) and Lemma 1 imply $|\mu W_p|\le br(D+m_N)<1/3$. For $b=0$ the mean vanishes by Haar invariance. At a single visit the exact traceless projection gives $\sum_a|X_aW_p|^2=(1-|W_p|^2)/N$. The scalar gap $N\eta$ and the four visits give ${\rm Var}(W_p)\le4/(N^2\eta)$, with ${\rm Var}(W)=E|W-EW|^2$. Hence $E|W_p|^2<1/4$ and $\|dW_p\|_2^2\ge3/N$.

For any ordered pair of its four links, the squared Hilbert–Schmidt norm of that block of $\nabla dW_p$ is at most one. For distinct links apply Bessel to one insertion in $N^{-1}{\rm Tr}(T_a U T_b V)$, then sum $|T_b|^2$ over $b$. This gives $(N^2-1)/N^2$. On the same link the insertions are symmetrized, and the triangle inequality gives the same bound. Thus $\|\nabla dW_p\|_2^2\le16$. By (5), $\|LW_p\|_2^2=\langle dW_p,H_1dW_p\rangle\le(1+q)(16+2)\le36$. Finally Cauchy–Schwarz in $\langle W_p-\mu W_p,-LW_p\rangle=\|dW_p\|_2^2$ gives

$$
 N^2{\rm Var}(W_p)\ge\tfrac14.
 \tag{12}
$$

This survives the free volume limit. It excludes collapse of all scaled covariances to zero. Existence of a full $N\to\infty$ fluctuation law is a separate question.

The mass in (10) is in lattice units. For time translates of fixed supports, $R\ge n-C$ at time separation $n$. In a positive transfer representation the centered autocorrelation at time $n$ is a moment of a positive measure on $[0,1]$. Any positive weight on $[s,1]$, $s>11/12$, would give a lower bound proportional to $s^n$. Thus (10) excludes energies below $\log(12/11)$ in the centered Wilson sector of that representation. This uses the spatial estimate, independently of the artificial heat time in (9).

## Coupling comparison

Use $Nb\,{\rm ReTr}U_p$ per geometric square throughout the comparison.

| CITED result | Published range in this convention, $d=4$ | Conclusion used for comparison |
|---|---|---|
| Hao Shen, Rongchan Zhu and Xiangchan Zhu, Assumption 1.1, Theorems 1.2 and 1.4, Corollaries 1.5 and 1.6 | SU(N), $\lvert b\rvert<1/48$ | Infinite-volume uniqueness, functional inequalities, large-rank factorization and local covariance decay. The proof uses a pointwise plaquette Hessian estimate. [Paper](https://arxiv.org/abs/2204.12737) |
| Nissim, Theorems 1.1 and 1.5 | U(N), $0<b<\widetilde b(4)$. The large-rank proof takes $\widetilde b(d)=\min\{(3C_d^*)^{-1},10^{-6d}\}$ before Proposition 3.20. The finite set of small ranks may require a smaller choice. | Thermodynamic limit, covariance decay and factorization. The theorem states existence of a threshold. Its proof choice in 4D is at most $10^{-24}$. The group differs from ours. [Paper](https://arxiv.org/abs/2510.22788) |
| Cao, Nissim and Sheffield, *Dynamical approach*, Definition 1.4 and Theorem 1.6 | SU(N) and U(N), $0<b<1/24$ | Rectangular area law. Its curvature estimate applies to a conditioned spin system in one fewer dimension. [Paper](https://arxiv.org/abs/2509.04688) |
| Cao, Nissim and Sheffield, *Expanded regimes*, Definition 2.3 and Theorems 1.2 and 4.1 | U(N). Their parameter $t$ has action $2t\,{\rm ReTr}U_p$, so $b=2t/N$. Theorem 4.1 uses $N\ge10^{10}d^{10}$ and $t\le10^{-10d}/d$. In 4D this gives $b\le10^{-40}/(2N)$. | Rectangular area law. Theorem 1.2 gives a dimension-only threshold on $t$ for all ranks. The exponent in (2.2) of the paper includes $d$. [Paper](https://arxiv.org/abs/2505.16585) |

**CITED.** Cao, Park and Sheffield's Theorem 5.7 gives the single-location U(N) master equation. Their Theorem 1.8 gives the finite-lattice surface sum. Absolute summability there groups surfaces by plaquette counts before taking the outer absolute sum. Their equation (1.2) gives $b=2\beta_{\rm CPS}$. The SU(N) argument above uses the traceless correction in (3). [Cao, Park and Sheffield](https://arxiv.org/abs/2307.06790)

The explicit interval $1/24<b\le1/20$ lies past both numerical SU(N) thresholds above. Equation (8) extends it further if the minimum rank may depend on the upper endpoint. These are still small bare inverse couplings. The proof compares Wilson laws with full, weakened or fixed boundary interactions at the same spacing.

## What limits the range

**PROVED.** The range-limiting estimate is (2). At large rank in 4D its score term costs $144 b^2$. Absorbing the differentiated slots costs a further $32 b^2$. Their sum must be less than the Ricci allowance $1/2$. The conditional requirement $6b<1/2$ has slack at that endpoint. The loss of the score term occurs exactly where the proof bounds a sum of six staple matrices by six. The split and merge identities themselves hold at every $b$.

On a homogeneous periodic cube let $p_b=\mu{\rm Re}\operatorname{tr}U_p$. Test (5) on a one-form supported at one edge and constant in its right frame, of norm one. Its connection energy is $N/2$ by the commutator calculation in Lemma 1. Vertex gauge symmetry makes the mean plaquette matrix, based at either insertion point, a scalar. The diagonal Hessian pairs $X^2$ with that matrix. Its expectation is $-NbD p_b$, while the $H_0$ form equals $N$. Thus $\|K\|\ge bD|p_b|$.

**PROVED. The full one-form operator has norm greater than one at $b=1$ for large rank and large periodic cubes.** Write $V=L^4$ for the number of lattice sites and $|P|=6V$. Convexity of $\log Z$ and $Z(0)=1$ imply $bp_b\ge(\log Z(b))/(N^2|P|)$.

First construct a one-link trial law $\tau_N$ on SU(N). Draw $N$ independent angles uniformly from $[-a,a]$, $a=4/5$, and conjugate their diagonal unitary matrix by an independent Haar unitary. Call the result $U$. Its mean is $tI$, with $t=\sin(a)/a$. For Haar U(N), randomly labeled eigenangles have density $\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2/N!$ relative to independent uniform angles on the circle. Indeed each off-diagonal conjugation tangent in diagonal coordinates is multiplied by the eigenvalue difference in two real directions. The angles supply the other directions. Repeated eigenvalues have volume zero, and integrating the squared Vandermonde determinant gives $N!$ by Fourier orthogonality. Haar conjugation gives the conditional law on each conjugacy class.

Push $U$ to $Q=e^{-i\arg(\det U)/N}U$, using the principal argument. The same map pushes Haar U(N) to Haar SU(N) by left SU(N) invariance. Relative entropy decreases under a measurable map, by conditional Jensen for $x\log x$. Applying this fact to the two constructions gives

$$
 h_N:=N^{-2}{\rm Ent}(\tau_N\mid{\rm Haar}_{SU(N)})
 \le N^{-2}\{\log N!+N\log(\pi/a)\}+(1-1/N)I_a ,
 \qquad I_a=-E\log|e^{i\theta}-e^{i\phi}|.
$$

Here $\theta,\phi$ are independent uniform angles on the trial arc. The trial mean is $z_N I$ by conjugation invariance, and $|z_N-t|\le\pi/N$.

For $0\le x\le1$, $\log(\sin x/x)\ge\log(1-x^2/6)\ge-x^2/5$, with the value at zero taken by continuity. The triangular difference density gives $E\log|\theta-\phi|=\log(2a)-3/2$, by integrating $2(1-s)\log s$ on $[0,1]$. Also $E(\theta-\phi)^2=2a^2/3$. It follows that

$$
 I_a\le 3/2-\log(8/5)+8/375<16/15 .
$$

For the last step use $\log x\ge2(x-1)/(x+1)$ for $x\ge1$. Also $t\ge1-a^2/6=67/75$, so $t^2>19/24,\ t^4>5/8$.

Fix all temporal links to $I$ except those across one time seam. The fixed links form a forest. Condition on their original Haar values and gauge them to $I$ recursively from the roots. Each remaining independent Haar link is multiplied on either side by fixed unitaries. Thus the normalized partition function equals the integral with the forest set to $I$. Give the other $(3+1/L)V$ links independent law $\tau_N$. Each spatial square then has mean normalized real trace $|z_N|^4$. Temporal squares off the seam have mean $|z_N|^2$. The seam squares also have nonnegative mean since their four random links are distinct. The entropy inequality $\log\int e^S\,dH\ge E_\tau S-{\rm Ent}(\tau\mid H)$ follows by Jensen. It gives at $b=1$

$$
 \frac{\log Z(1)}{N^2|P|}
 \ge \tfrac12|z_N|^4+\tfrac12(1-1/L)|z_N|^2
                 -(\tfrac12+1/(6L))h_N .
$$

The joint lower limit as $N,L\to\infty$ exceeds $(17/12-16/15)/2=7/40$. The constant one-form test therefore gives $\liminf\|K\|>21/20$. The test uses a gauge-dependent form and a negative Hessian direction. Its sign helps the lower bound on $H_1$. Contraction on the subspace generated by Wilson sources remains open at this coupling.

The Hilbert–Schmidt bound on each of the 16 trace terms in Lemma 2, summed before integration by parts, gives $|{\rm Hess}\,S|\le4DNb$ in operator norm. Hence the operator in (5) has norm at most $8Db=48$ here. If its upper spectral edge were at most $1-\epsilon$ uniformly, the damped operator $(48I+K)/49$ would contract by $1-\epsilon/49$, still with one edge step per iteration. The trial law tests the lower spectral edge. **GUESSED.** A positive rank-uniform Wilson fluctuation gap at $b=1$ remains plausible. The uniform upper-edge estimate is open.

## Group, dimension and the SU(2) consumer

**PROVED.** On U(1) a charge-$j$ observable uses $e^{ij\theta}$. Its derivative has size $|j|$, and its one-link Laplacian eigenvalue is $j^2$. The Wilson action still inserts charge one. Raising the test charge gives no commutator term in the Ricci form. The circle has a parallel one-form $d\theta$ of zero connection energy, so the Haar version of $H_0$ has a kernel. For a simple Haar plaquette, the charge-$j$ trace has mean zero and variance one for every nonzero integer $j$. Hence high charge cannot replace the $N^{-2}$ fluctuation factor. If charge $j$ is also put into the action $b\cos(j\theta)$, the absolute second derivative grows as $bj^2$. Disjoint observables of independent Haar links already have zero covariance. This example distinguishes the one-form estimate used here from spatial clustering itself.

Dimension enters through $D=2(d-1)$, the number of squares at one edge, and the incidence count in (3). The asymptotic loss is $[4D^2+16D/3]b^2$. This coefficient is $256/3$ in 3D, $176$ in 4D and $896/3$ in 5D. It uses no four-dimensional running coupling or phase distinction.

**PROVED. SU(2) specialization.** The trace of every SU(2) matrix is real, since its two eigenvalues are conjugates. Thus $Y_h=0$ for every actual staple, also with fixed SU(2) exterior. In (2) omit $m_N$ and the derivative cost from (1). Now $r=4/3$, hence $\eta=1/2-(704/3)b^2$. Equations (6), (7), (9) and the volume argument hold for $0\le b<\sqrt{3/1408}$. The card uses $\beta(1-{\rm Tr}U_p/2)$ per square. Thus $\beta=4b$, and the SU(2) interval in its units is $0\le\beta<\sqrt{3/88}$. The earlier SU(2) Theorem A of `gap-mixed-opus.md` already gives an invariant Langevin bound for $\beta<1/4$. The specialization here gives a direct spatial covariance estimate.

**ARGUED.** The purity card asks for a lower bound $457/625$ on the neutral trace ratio at $u=n/512$, for infinitely many calibrated cutoffs. A time gap alone leaves the number of excited states uncontrolled. For example, a neutral transfer matrix with eigenvalues $1$ and $M$ copies of $a\in(0,1)$ has the fixed gap $-\log a$. Its purity at fixed $u$ is $(1+Ma^{2u})/(1+Ma^u)^2$, which tends to zero as $M$ grows. Our SU(2) interval is at fixed small bare coupling. It supplies neither a passing cutoff nor an exponential estimate at fixed physical rate along $\beta_K$. The crux remains open. [Purity definition](../lean/gapchain/GapChain/Purity.lean#L25) · [Passing cutoffs](../lean/gapchain/GapChain/PurIo.lean#L25) · [Consumer](../lean/gapchain/GapChain/Offset.lean#L701)
