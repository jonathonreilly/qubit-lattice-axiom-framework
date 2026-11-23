# Repo search

Row 1425, lane `d0f9609f3081`. The five Markdown/TeX refs searched were `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). The word-bounded search for “ring response”, “two-strand ring”, “two-cycle reading”, “traceless ring”, “relative-orientation moment”, “rank-two plaquette”, `Y_alt` and the row name returned no hits. A broad search without word boundaries picked up “during response” in unrelated files. Method terms included “spin foam”, “single-loop convolution”, “quaternion sphere moment”, “torus commutator kernel” and “two-dimensional Yang–Mills” near “torus”. The broad method pass was capped.

| Source | Statement used and its scope |
|---|---|
| Main, `research/mass-gap/library/prior/gap-crux-lit-nonab.md` §T6 and `gap-crux-lit-2.md` 237 | Character dualization gives an exact partition-function representation. The finite-loop bootstrap has an additional cutoff. The two-square moment remains open in those sources. |
| PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149, located by the November 8 search | The one-loop convolution obeys $\bar k_B\ge(1+v_N/\rho)^{-1}\lvert F\rangle\langle F\rvert$, with $\rho=(I_2/I_1)^b$ for an SU(2) loop of length $b$. This lower form concerns a single loop across a time step. [November 8 digest](prior/repo-search-2026-11-08.md) |
| Rows 1341, 1418 and 1421 | Uniform-quaternion moments integrate Haar polynomials. The Wilson site tensor carries $b_n^{1/4}$ per corner. With the common vacuum divided out, a fixed exterior contraction is its exterior weight times a **joint** expectation in the complete internal Wilson law. Row 1421's spectral-block reduction (3) covers at most one cycle per connected component. [1341](gap-blockstep-astra62.md) · [1418](gap-rg-step-sizing-astra62.md) · [1421](gap-rg-signed-inclusion-astra62.md) |
| Lane, Lemma T in `gap-kappa-order.md` §3 | A rectangle of $A$ fundamental half-traces glues to $4^{-(A-1)}q(U_{\partial})$. Cutting a torus on its two generating circuits leaves their commutator on that boundary. This evaluates one of the eleven leading supports below. [Lemma T](gap-kappa-order.md) |
| Row 1424, (4), (6), (7) | Interchanging axes cancels the single-fundamental response, including internal spins. For two strips per square it gives the explicit traceless second moment in (7), invariant under both inversions. Its sign was left open. [1424](gap-rg-two-cycle-astra62.md) |

A follow-up on “diagonal reflection positivity” found a positive planar two-point Gram form in main’s `research/ym4d/library/ro1.md` (6.2). The “2-torus commutator bound” in PRs 10114/10133, `ym4d-existence/EXISTENCE.md` 3758–3761 and its snapshots, reports finite-configuration tests of a ribbon bound. Both concern other observables. The mixed-plaquette-torus/strong-coupling figure-eight query returned no hits on the five refs.

The row-specific prior file is absent, FINISH 1425 has no separate “Repo prior work” entry, and the registry and outline/CA index queries returned no matching owner or bracket. Sussman and Alpoge, writing with Claude and Codex, supply the Wilson law and its positive one-bond coefficients in SA 238–278 and 2195–2243, the quaternion identification at 2773–2781 and the curvature row and column counts at 8519–8549, in the supplied snapshot `31a47c543775`. Those statements fix conventions for the calculation. [Index and chunks 01, 02, 03, 08](sa-index/README.md) · [Obligations](sa-index/obligations.md)

## Plan saved at creation

1. Check the owner's goal, finishing rules, prior work, and ownership. Read rows 1418, 1421 and 1424 and the indexed source passages needed for the gate.
2. Freeze the outgoing normalized response and its gain sign from row 1424 before evaluating the ring.
3. Keep the shared Wilson denominator and all internal spins. Seek a uniform rational enclosure for the four-dimensional block. Examine the five-dimensional classical factor and the fixed-charge restriction with their own normalizations.
4. Record the exact inputs, outputs, scratch code, any limitations, and the Lean replay statement. End with the next two rows and their decisive outcomes.

Research text. This row grants no status.

## Frozen response and acceptance test

Freeze the **magnitude of the alternating outward coefficient** with the same-angle independent-conjugation value as its reference. This is one actual component of the vacuum-normalized block after all pairings. Use precisely the two exterior routings, the phases of $t$, the rooted plaquettes $P=(12)$ and $Q=(34)$ and the common division by $z_B$ in row 1424. Write $B_d=\{0,1\}^d$, $q(g)=\operatorname{tr}(g)/2$ and $A(\beta)=\int e^{\beta q(g)}\,dg$ for probability Haar $dg$. The vectors $h,k$ are the imaginary parts of the two unit-quaternion holonomies. Set $W=|h|^2|k|^2$, $T=(h\cdot k)^2-W/3$, $b=2I_2(\beta)/I_1(\beta)$ and $C_2=b^9/64$. The frozen reference is $Y_{\rm alt}^{\rm rot}=-Y_{\rm grp}/3$ at the same Wilson law of the two angles. Write $\rho_d=Y_{\rm grp}/3=(2C_2/27)\mathbb E_d W>0$, and orient the signed reading as $-Y_{\rm alt}$. Then

$$
\Delta_d=Y_{\rm alt}+\rho_d=\frac{4C_2}{9}\mathbb E_d T,
\qquad -Y_{\rm alt}=\rho_d-\Delta_d.
$$

The positive sign of $\Delta_d$ is the direction towards zero. The exact test for a **strict decrease in magnitude** is $0<\Delta_d<2\rho_d$. Equivalently $0<\mathbb E_d T<\mathbb E_d W/3$. Use $g_d=|Y_{\rm alt}|/\rho_d=|1-6\mathbb E_d T/\mathbb E_d W|$ for the relative magnitude. Report $g_4$ against one and $2g_5$ against one, with the uncorrected five-dimensional factor two. These are comparisons for a specified tensor entry. Identifying that entry with an inverse coupling would need another argument. For fixed abelian charges use the invariant-line traceless routing itself, without dividing by its vanishing reference. The classical factor follows by matching the $2^d$ fine cells to a squared coarse flux $2^4$ times the fine value. This convention, including the overshoot test, was saved before any ring evaluation.

## Gate result

**Reject this ring as a decrement of the frozen four-dimensional magnitude, pending formal replay.** Uniformly for $2\le\beta\le513/256$, the complete normalized moment and its contribution to row 1424 (7) satisfy

$$
 -\frac{2054}{10^{11}}\le \mathbb E_4 T\le-\frac{1829}{10^{11}},
 \qquad
 -\frac{4072}{10^{14}}\le \Delta_4\le-\frac{3488}{10^{14}}.
$$

The already negative alternating coefficient moves farther from zero. Its relative magnitude increases by between $109/10^9$ and $484/10^9$. In five dimensions the moment interval crosses zero, but $2g_5\ge131133152/10^8>13/10$ throughout the band. At every fixed U(1) charge assignment the traceless response vanishes before integration.

These are exact-arithmetic enclosures with a specified analytic tail. **The numbers are not yet Lean-replayed.** No Lean executable is installed on this runner. This is research text and grants no status.

## Integrating four marked links exactly

On each rooted square leave its two links meeting at the vertex opposite the root unconditioned. Fix every other internal link. A face touching two of the four free links must be one of the two marked squares. Within one square the two links determine their unique face. Between the squares, a free link along axis 1 or 2 has the other coordinate in that pair equal to one, while every link of the other square has that coordinate zero. This rules out a shared face. The argument also works with a fifth coordinate. Each free link belongs to $d-1$ internal faces, of which $d-2$ remain after extracting its marked square.

Absorb the fixed transports and inverse orientations into the two Haar links on each square so that the rooted holonomy is $H=XY$. Each of the $d-2$ other incident half-traces becomes a Euclidean dot product of the link quaternion with a unit staple. Thus the conditional, unnormalized law of one pair is proportional to

$$
 e^{S\cdot X+V\cdot Y+\beta q(XY)}\,dX\,dY,
 \qquad |S|,|V|\le (d-2)\beta .
$$

There is another such pair for $K$. The pairs are conditionally independent given the other links. Their normalizers multiply **inside** the outer Wilson integral. The four-link integration leaves precisely the original $z_B$ after integrating the exterior. In particular, the staple directions in the two pairs can remain correlated.

Put $Q(h)=hh^t-|h|^2 I_3/3$. The product of two isotropic SU(2) kernels, centered at group elements $g_1,g_2$, has a convolution centered at $g_1g_2$. If $s=|S|$, $v=|V|$ and $G=g_1g_2$, its unnormalized density at $H$ is $A(\sqrt{s^2+v^2+2sv\,q(G^{-1}H)})$. This follows by integrating $X$ with $Y=X^{-1}H$ and adding its two linear sources. The full density includes $e^{\beta q(H)}$. Its conditional mean quadrupole has the form $a(nn^t-I_3/3)$, with $n$ the direction of the vector part of $G$. It is zero if that vector vanishes. In fact $a\ge0$. At fixed $q(H)$ the angular variable $t=n\cdot h/|h|$ is uniform on $[-1,1]$ before weighting. Its density is proportional to $F(t)=A(\sqrt{c+et})$, with $c+et\ge0$. The nonnegative Taylor coefficients of $A(\sqrt{x})$ give $F''\ge0$. Twice integrating the degree-two Legendre polynomial by parts gives $\int P_2(t)F(t)dt=\tfrac18\int(1-t^2)^2F''(t)dt$ over this interval.

The following enclosure bounds $a$ and $a/\mathbb E(|h|^2\mid\mathrm{exterior})$ over all staple vectors. Testing any fixed axis against either upper bound gives an unnormalized integral solving $(\Delta_S-1)f=(\Delta_V-1)f=0$, by differentiating against unit quaternions. A negative interior minimum violates this equation. Applying the minimum principle in the two balls successively reduces these linear upper tests to $|S|=|V|=(d-2)513/256$. This step preserves the relative orientations. It leaves a one-variable character sum and the coupling interval for the numerical enclosure.

## Uniform enclosures from the character expansion

For equal boundary radii $R=(d-2)513/256$, write $u=q(G)$, $U_n(\cos\theta)=\sin((n+1)\theta)/\sin\theta$ and $L_n(x)=2I_{n+1}(x)/x$, continued at zero. Define $a_n=(n+1)[L_n(R)/L_0(R)]^2$. With the two separate staple masses $A(R)^2$ removed, the three unnormalized integrals for one marked square are

$$
\begin{aligned}
 Z &=\sum_{n\ge0}a_nL_n(\beta)U_n(u),\\
 \beta^2 W_1 &=\sum_{n\ge0}a_n[3\beta L_n'(\beta)-n(n+2)L_n(\beta)]U_n(u),\\
 \beta^2 D &= (1-u^2)\sum_{n\ge0}a_n L_n(\beta) U_n''(u).
\end{aligned}
$$

Here $W_1/Z$ is the conditional mean of $|h|^2$, and $D/Z=a$ is the coefficient of $nn^t-I_3/3$ above. Schur convolution gives eigenvalue $L_n(R)/L_0(R)$ on spin $n/2$ for each of the two links. For a four-vector source $b$ in place of $\beta e_0$, its integral at spin $n/2$ is $L_n(|b|)U_n(G\cdot b/|b|)$. This follows by rotating the source and using central convolution on unit quaternions. For each $n$, the spatial trace-free Hessian contributes $L_n(\beta)U_n''(u)(G_iG_j-\delta_{ij}|G_{\rm vec}|^2/3)/\beta^2$. For the radial integral $W_1$, use $Z-\partial_\beta^2 Z$ and $\beta^2 L_n''+3\beta L_n'=(\beta^2+n(n+2))L_n$, obtained coefficientwise from the Bessel series.

The script retains $0\le n\le20$. In each of $\beta^2 Z,\beta^2W_1,\beta^2D$ the absolute tail is at most

$$
 4(513/256)^2\frac{(R/2)^{42}}{(21!)^2}.
$$

Indeed $|U_n|\le n+1$, the three test functions have magnitude at most one before multiplication by $e^{\beta q(H)}$, and its Haar mass is $A(\beta)<2$ by row 1421. GL4 bounds the omitted kernel by $\sum_{n>20}(R/2)^{2n}/(n!)^2$, whose successive ratios are below $1/2$. This argument bounds the integral of the tail before differentiating its displayed polynomial representation.

The positive Taylor series for $L_n$ has terms $t_k=(\beta/2)^{n+2k}/[k!(n+k+1)!]$. The bracket in $W_1$ multiplies each $t_k$ by $6k+n(1-n)$. After $k=32$, a geometric bound of ratio $1/2$ encloses the value and the weighted remainder, using $\sum_{j\ge0}j/2^j=2$. Chebyshev's recurrence and its first two derivatives supply the polynomials on 2,048 closed cells of $[-1,1]$, crossed with four closed cells of $[2,513/256]$. The script checks both lower denominators are strictly positive in every box. It encloses all operations by integers with 112 binary fractional bits, including outward conversion of exact fractions.

The scratch program `/tmp/ym4d-row1425.a4IgI8Ax/conditional_ring.py` produced these exact lines in `/tmp/ym4d-row1425.a4IgI8Ax/conditional.log`.

```text
d=4 eta<=1450/10000 xi<=1037/10000 N=20 K=32 angle_cells=2048 beta_cells=4
d=4 W1/Z>=5047/10000
d=5 eta<=2934/10000 xi<=2269/10000 N=20 K=32 angle_cells=2048 beta_cells=4
d=5 W1/Z>=4354/10000
```

Here $D\le\eta W_1$ and $D\le\xi Z$. For smaller radii apply the minimum principle above to the integrals of $\eta |h|^2-P_{2,\ell}(h)$ and $\xi-P_{2,\ell}(h)$ for each fixed unit $\ell$, where $P_{2,\ell}(h)=[3(\ell\cdot h)^2-|h|^2]/2$. The largest conditional mean of $P_{2,\ell}$ equals $a$. The tensor contraction of the two conditional means is $a_Ha_K[(n_H\cdot n_K)^2-1/3]$. Conditional independence gives $\mathbb E(W\mid\mathrm{exterior})=\mathbb E(|h|^2\mid\mathrm{exterior})\mathbb E(|k|^2\mid\mathrm{exterior})$. Integrating these inequalities in the common positive Wilson law gives the following exact rational enclosures. The computational inequalities are **open pending Lean replay**.

| $d$ | $\mathbb E_d T$ | $\mathbb E_d T/\mathbb E_d W$ | $2^{d-4}g_d$ |
|---|---|---|---|
| 4 | $[-1037^2,2\cdot1037^2]/(3\cdot10^8)$ | $[-1450^2,2\cdot1450^2]/(3\cdot10^8)$ | $[1-4(1450/10000)^2,\ 1+2(1450/10000)^2]$ |
| 5 | $[-2269^2,2\cdot2269^2]/(3\cdot10^8)$ | $[-2934^2,2\cdot2934^2]/(3\cdot10^8)$ | $[2-8(2934/10000)^2,\ 2+4(2934/10000)^2]$ |

The relative intervals also certify $1-6\mathbb E_d T/\mathbb E_d W>0$. The alternating coordinate keeps its original negative phase and cannot overshoot. The five-dimensional lower endpoint exceeds $13/10$. In four dimensions this first relative interval contains one. The two conditional bounds on the raw moment both contain zero. All $24$ or $80$ Wilson faces remain in the normalized integral. The four-dimensional torus contraction below resolves the sign left by this conditional estimate.

## Four-dimensional contraction on a smaller graph

Regard the graph of the open four-cube as $C_4\times C_4$. Each $C_4$ goes round the square of one pair of axes. The 16 mixed plaquettes form the square tiling of a torus. The four horizontal circuits and four vertical circuits carry the remaining eight Wilson plaquette weights. The marked circuits are the row and column through the common root. The pure two-dimensional torus integral acquires eight additional Wilson weights, one per circuit. [Earlier disc and torus Schur integral, Lemma T](gap-kappa-order.md)

In the spin expansion let $m_{ij}$ be the nonnegative twice-spin of a mixed face. Write $a_j,b_i$ for the spins (in the same integer units) on the horizontal and vertical circuits. At every bond the two incident mixed spins have to couple through its circuit spin. Their ordinary SU(2) triangle inequalities and parity restrict a circuit spin on all four of its bonds. At the two marks the circuit spin must be at least two. In fact, differentiating the character expansion with a three-vector source $t$ in $e^{\beta q(U)+t\cdot h}$ gives the trace-free insertion at the root. Write $J$ for the Hermitian angular momenta of spin $n/2$ and $Q^{ab}(J)=(J_aJ_b+J_bJ_a)/2-\delta_{ab}J^2/3$. The coefficient matrix for $Q^{ab}(h)e^{\beta q(U)}/A(\beta)$ is $-4b_n Q^{ab}(J)/\beta^2$. Indeed the shifted source length is $(\beta^2+|t|^2)^{1/2}$ and its direction is a translated SU(2) character argument. Only the second derivative of the representation of that translation survives the spatial trace-free projection. Its first derivative is $\pm 2iJ_a/\beta$. This also explains the two-order lowering at each mark in a Taylor expansion.

For a fixed $m$, each unmarked circuit can first occur at the smallest spin in the intersection of its four triangle/parity intervals. Each marked circuit costs its smallest allowed spin minus two. Adding the sixteen mixed spins gives a lower bound on the Taylor degree of its contribution. A scratch integer enumerator, `/tmp/ym4d-row1425.a4IgI8Ax/spin_order.py`, found no support below degree 16 and eleven mixed-spin arrays of minimum degree 16. Its counts through degree 24, grouped by minimum degree, were $11,56,155,386,1110$ at degrees $16,18,20,22,24$. These counts precede the contraction at the marked vertex, which can annul an allowed term. The all-fundamental torus is one of the eleven. A sign inferred from that torus alone would omit ten contributions at its very first possible degree. The marked vertex and the omitted signed sum are evaluated below.

At a vertex $(i,j)$ denote the surrounding mixed spins by $r=m_{i-1,j-1}$, $s=m_{i,j-1}$, $t=m_{i-1,j}$ and $u=m_{ij}$, all indices modulo four. Put $a=a_j,b=b_i$. There are two orthonormal coupling schemes from $V_s$ to $V_a\otimes V_b\otimes V_t$, one through $r$ in $a\otimes t$ and one through $u$ in $b\otimes t$. Write $O_{ru}$ for their real overlap. The Clebsch–Gordan coefficients on the two paths are ordered $(a,t;r),(b,r;s)$ and $(b,t;u),(a,u;s)$. For a horizontal link Haar projects $D_aD_u\overline{D_s}$ onto its invariant, giving one Clebsch–Gordan tensor at each end divided by $s+1$. A vertical link gives the corresponding divisor $u+1$. The contraction at the vertex is $(s+1)O_{ru}$ by summing the final magnetic index. Multiplying these factors on the torus leaves $\prod_{ij}\lambda_{m_{ij}}$, where $\lambda_n=I_{n+1}/I_1$. Each circuit retains $b_n=(n+1)\lambda_n$.

At the marked vertex replace $O_{ru}$ by $\langle r|K|u\rangle$ and include $16/\beta^4$. Here $K=J_a\cdot J_b\,(J_a\cdot J_b+1/2)-C_a C_b/3$, $C_x=x(x+2)/4$, from contracting the two symmetrized trace-free generators. In these bases the mixed matrix element of $J_a\cdot J_b$ is $(C_s+C_t-C_r-C_u)O_{ru}/2$, since the total angular momentum is $s/2$. The script squares the operator by matrix multiplication and evaluates the Racah factorial sum with its four triangle square roots kept symbolic. Each triangle root occurs twice across the lattice, so the coefficient of each product of $\lambda_n$ is rational.

The scratch producer `recouple.py` and interval evaluator `evaluate.py`, in the scratch directory above, grouped coefficients at identical spins before evaluating the Bessel factors. At spin order $\sum m+\sum a+\sum b-4\le34$ the band enclosure for the retained **unnormalized** numerator, in units of $10^{-15}$, was $[-27496232,-21388987]$. The degree-16 Taylor coefficient about zero was $15655/169075682574336$ before vacuum division (the vacuum has constant term one). At orders 16 and 18 the band contributions have opposite signs. The sign in the band depends on the bound for the omitted degrees. Full arithmetic outputs are in `groups34.log` and `evaluate34.log`.

## Bounding every omitted spin

Introduce one complex variable $z$ multiplying a face of twice-spin $n$ by $z^n$, on **all 24 faces**. Write $F_z(g)=\sum b_n z^n\chi_n(g)$ and write $G_z^{ij}$ for the corresponding character-matrix series with $-4Q^{ij}(J_n)/\beta^2$ on a marked circuit. Let $N(z)$ be the resulting partition integral with the two tensor insertions contracted. Thus $N(1)=z_B\mathbb E_4 T$. The factorial GL4 bound makes these finite products entire in $z$, including the two insertions of quadratic angular momentum. A link sign $(-1)^{\sum_{j<i}x_j}$ on the positive $i$-link at $x$ flips every face holonomy by the central element $-1$. Haar is invariant and each representation acquires $(-1)^n$. Hence $N$ is even. A cutoff at spin order 40 retains powers through $z^{44}$.

Slice perpendicular to axis four. Fix the 8 fourth-direction links to identity by gauge transformations of the upper sites. The two slice fields each live on the 12 edges of an ordinary three-cube. The 12 crossing faces act as one-bond convolutions between the slices. One crossing face uses $G_z$ at the edge along axis three from the root. The lower cube has one marked spatial face and five ordinary faces, and the upper cube has six ordinary faces. This is a bound on the same integral at complex $z$.

For a radius $t>1$ put $\widehat b_n=b_n t^n$, $P=\sum \widehat b_n^2$, $P_Q=\sum C_n^2 \widehat b_n^2$, $M=\sup_n \lambda_n t^n$, $M_Q=\sup_n C_n\lambda_n t^n$ and

$$
 \alpha_k=\frac{1}{k+1}\sum_{m,n:\, V_k\subset V_m\otimes V_n}\widehat b_m \widehat b_n,
 \qquad E_5=\sum_{k\ge0}(k+1)^2\alpha_k^5 .
$$

The eleven ordinary crossing convolutions have joint norm at most $M^{11}$. The marked one has norm into the direct sum over $i,j$ at most $M_Q$. Indeed $4/\beta^2\le1$ and projecting the nine matrices $J_iJ_j$ onto their symmetric trace-free part can only decrease $\sum_{ij}\|J_iJ_j v\|^2=C_n^2\|v\|^2$. For a single face, Schur orthogonality gives $\int |F_z|^2=P$ and $\int\sum_{ij}|G_z^{ij}|^2\le P_Q$. The latter sum is central by rotation covariance.

The six faces of a three-cube form a sphere. Integrating class functions on them with product link Haar gives their sixfold convolution at the identity. This follows by cutting along a tree of adjacent faces and applying Schur gluing, or by matching the two representation labels at each edge and retaining the spherical dimension factor $(k+1)^2$. The Fourier eigenvalues of $|F_z|^2$ have modulus at most $\alpha_k$ by character multiplication. Its fivefold convolution therefore has supremum at most $E_5$. The squared upper-slice norm is at most $P E_5$, and the sum of the squared lower-slice norms is at most $P_Q E_5$. Cauchy–Schwarz in the direct sum now gives

$$
 \sup_{|z|=t}|N(z)|\le M^{11}M_Q\sqrt{P P_Q}\,E_5 .
$$

For the entire unmarked vacuum series $Z(z)$ the corresponding bound is $M^{12}P E_5$. In particular all spins outside the enumerated core enter a single scalar remainder before the vacuum division.

The exact auxiliary sums are enclosed in `circle_tail.py`. Through $n=24$ it uses the positive Bessel series. For $x=t(513/256)/2$, $\widehat b_n\le x^n/n!$. For the radii used below, $E=2\cdot26^4 x^{25}/25!$ bounds $\sum_{n>24}(n+1)^4 \widehat b_n$ by the successive-term ratio. Squaring this sum bounds the scalar and quadratic-moment square tails. If $S_0=\sum_{n\le24}(n+1)\widehat b_n$, removing either high index from the positive sum for $\alpha$ costs at most $(2S_0+E)E$ in $\sum_k(k+1)^2\alpha_k$, by the tensor-product dimension identity. Since $\alpha_k\le P$ (integrate $F_t^2$ against a normalized character), its cost in $E_5$ is at most $5P^4(2S_0+E)E$. This proves the tail rule used in the script even when finite Bessel upper endpoints are rounded outward.

At $t=11/4$ the upper integer circle bound was $216821257148$. Cauchy's coefficient inequality, evenness and the geometric series from degree 46 give

$$
 |N(1)-N_{\le44}(1)|
 \le \frac{216821257148(4/11)^{46}}{1-(4/11)^2}
 \le \frac{1543100}{10^{15}} .
$$

The core, using 128 closed coupling cells, gave $10^{15}N_{\le44}(1)\in[-26408095,-22452766]$. Thus **$10^{15} z_B\mathbb E_4 T\in[-27951195,-20909666]$** throughout the band, including its endpoints. Computational standing is open pending kernel replay. The tighter cutoff and the scratch logs appear below.

A different Haar calculation checks the leading sign structure. Write $T=q([H,K])/2+1/6-2[q(H)^2+q(K)^2-q(H)^2q(K)^2]/3$. In a normalized trace word, integrating two occurrences of a link uses Schur gluing. For $2p$ occurrences the $S^3$ moment equals $2^p/(p+1)!$ times the sum over pairings of those gluing integrals by the radial Gaussian moment formula in row 1424. The independent trace contraction in `sphere_fixture.py` gave four copies of $-5/195689447424$, four of $5/1320903770112$, two of $5/86973087744$ and one of $5/77309411328$. Their sum agrees with the recoupling coefficient $15655/169075682574336$. The single all-fundamental torus term also equals $4^{-15}(5/72)$ by Lemma T and the independent Haar angle moments. This checks degree 16. The sign on the requested band uses the higher orders and the circle bound.

## How to reproduce the finite sums

For each row or column of mixed faces, the allowed circuit spins form the intersection of $[|m-m'|,m+m']$ in steps of two over its four edges. Intersect with $n\ge2$ at a mark. For the numerator each column has mixed-spin sum at least two because it crosses the marked row, so its sum at cutoff $k$ is at most $k-6$. Enumerate every ordered quadruple of nonnegative integers in this range. Adjacent columns must have a common parity difference on their four entries, which is equivalent to equality of their four relative-parity vectors. When columns are appended, every already constrained circuit minimum can only increase. Prune only when the known mixed cost plus these minima and the minimum cost of the remaining columns, after subtracting the marked offsets, already exceeds $k$, or a triangle intersection is empty. Close the fourth column back to the first. Enumerate every allowed circuit spin with the remaining total budget. For the vacuum set the minimum per column and both marked offsets to zero. The producer folds the two cycle reflections fixing the root and interchange of the two cycles, multiplying by the size of each mixed-array orbit. These changes preserve each labelled Haar integral because characters are invariant under inversion and each marked projection of $Q(h)f_\beta(H)$ is even under $H\mapsto H^{-1}$. The transpose interchanges the two contracted quadrupoles.

In `recouple.py`, the ordinary local overlap is

$$
 O_{ru}=(-1)^{(a+2t+3b+r-u)/2}\sqrt{(r+1)(u+1)}
 \begin{Bmatrix}a/2&t/2&r/2\\ b/2&s/2&u/2\end{Bmatrix}.
$$

The phase follows by putting the two Clebsch–Gordan paths in the orders specified above. Each edge triple $(a,t,r)$ contributes a triangle factor whose square is $(v-a)!(v-t)!(v-r)!/(v+1)!$, $v=(a+t+r)/2$. The two paths have the common final spin $s/2$. These conventions specify the relative signs needed to sum the supports and retain their cancellations.

For the common vacuum, the degree-28 core gave $10^{15}Z_{\le28}(1)\in[1256795084726467,1259476223854567]$. The circle bound at $9/4$ was $15466258$, giving a tail at most $524181115/10^{12}$ from degree 30 on. In particular

$$
 \frac{1256270903611467}{10^{15}}\le z_B\le
 \frac{1260000404969567}{10^{15}} .
$$

This vacuum sum retains all internal representations.

## Final interval and checks

The final four-dimensional core retains spin order 42, hence all terms through $z^{46}$. With 512 coupling cells it gave $10^{15}N_{\le46}(1)\in[-25591398,-23250036]$. The preceding circle bound at $11/4$, now starting at degree 48, adds at most $204047/10^{15}$ to either end. The last shell contains $1899868$ cap-labelled assignments counted with orbit multiplicity. The degree-28 common vacuum was enclosed on 128 coupling cells. The exact outward divisions, with $l_N,u_N<0<l_Z,u_Z$, use $[l_N/l_Z,u_N/u_Z]$. Row 1421's $136/157\le b<87/100$ and $\Delta_d=b^9\mathbb E_dT/144$ give the normalized ring units. The minimum principle for $W_1-w_*Z$ propagates the four-dimensional check $w_*=5047/10000$ to the full staple balls, so $w_*^2\le\mathbb E_4 W\le1$ for the relative magnitude.

| Quantity | Final rational enclosure on the whole band |
|---|---|
| $z_{B_4}\mathbb E_4 T$ | $[-25795445,-23045989]/10^{15}$ |
| $z_{B_4}$ | $[1256270903611467,1260000404969567]/10^{15}$ |
| $\mathbb E_4 T$ | $[-2054,-1829]/10^{11}$ |
| $Y_{\rm alt}+Y_{\rm grp}/3$ in $d=4$ | $[-4072,-3488]/10^{14}$ |
| $g_4-1$ | $[109,484]/10^9$ |
| $\mathbb E_5 T$ | $[-5148361,10296722]/300000000$ |
| $Y_{\rm alt}+Y_{\rm grp}/3$ in $d=5$ | $(87/100)^9[-5148361,10296722]/(144\cdot300000000)$ |
| $2g_5$ | $[131133152,234433424]/10^8$ |
| Fixed U(1) charges, either dimension | $[0,0]$ for the traceless ring coefficient |

For U(1), on an oriented line of any fixed charge the matrix of a holonomy is its scalar trace. Subtracting its scalar part gives zero. Equivalently, at a compatible root bond the invariant line is spanned by the disconnected routing, so the orthogonal traceless routing vanishes. An inadmissible assignment has zero coefficient. The vanishing reference makes the ratio $g_d$ undefined there.

The independent sphere fixture also checks signed sectors above the first order. With every mixed spin fundamental and the two marked circuits in physical spin one (integer label two), the unweighted character integrals with zero, one or two extra adjoint circuits were respectively $5/1179648$, $-5/3538944$ (both tested positions), and $-5/31850496$. A second local calculation used the symmetric-power highest vector $(x_1y_2-y_1x_2)^p x_1^{a-p}x_2^{b-p}$, $p=(a+b-c)/2$, for the injection $V_c\to V_a\otimes V_b$. Ordinary polynomial differentiation gives its lowered states. The monomial $x^{a-i}y^i$ has squared norm $1/\binom ai$. Direct inner products, with $J_a\cdot J_b$ applied as a differential operator at the mark, agreed in sign and squared magnitude for **all 1689 distinct local cases visited**, including all 295 marked cases. The polynomial and trace-word checks reuse the stated support geometry. They check the contractions by different arithmetic paths.

## Lean replay obligation

Let $P_d$ be all internal faces of $\{0,1\}^d$, let $dU$ be product probability Haar on its positive links with inverse on reverse links, and set

$$
 f_\beta(g)=e^{\beta q(g)}/A(\beta),\quad
 z_{B_d}=\int\prod_{p\in P_d}f_\beta(U_p)\,dU,\quad
 \mathbb E_d X=\frac{\int X\prod_{p\in P_d}f_\beta(U_p)\,dU}{z_{B_d}}.
$$

Take the two rooted positive circuits $0,e_1,e_1+e_2,e_2,0$ and $0,e_3,e_3+e_4,e_4,0$, at $x_5=0$ in dimension five. **The exact statement to check** is that for every real $\beta\in[2,513/256]$ the first eight enclosures in the final table hold simultaneously for these integrals and the frozen response, and that for every fixed assignment of integer U(1) charges the last row holds. In particular the replay must derive the coefficient identity (7) for the stated two routings, positivity of both vacua, $g_4>1$, and $2g_5>1$.

The arithmetic witnesses live in `/tmp/ym4d-row1425.a4IgI8Ax/`. The following paths are relative to that scratch directory.

| Replay input | Exact acceptance check |
|---|---|
| `recouple.py 42`, `groups42.txt`, `groups42.local`, `groups42.log` | Prove completeness of the triangle/parity enumeration and its root-preserving orbit count. Recompute the signed rational coefficient of every spin histogram. |
| `recouple.py 28 vacuum`, `vacuum28.txt`, `vacuum28.local`, `vacuum28.log` | Repeat with all ordinary faces and zero marked offsets. The empty configuration contributes one and the first nonconstant shell consists of eight cubes at degree six. |
| `evaluate.py 42 512`, `evaluate.py 28 128 vacuum`, `evaluate42.log`, `vac-eval28.log` | Outward integer arithmetic on every parameter cell must imply the two retained intervals above before division. |
| `circle_tail.py`, `circle.log` | Establish the temporal-gauge convolution identity, three-cube sphere gluing, character majorants and even Cauchy remainder. Check the two integer circle bounds $216821257148$ and $15466258$, and the degree-48 and degree-30 tails. |
| `conditional_ring.py`, `conditional.log` | Check $8192$ closed parameter boxes per dimension, both denominator signs, the GL4 and Taylor tails, and the minimum-principle extension for the normalized conditional moments. |
| `spin_order.py`, `sphere_fixture.py`, `magnetic_check.py`, `sphere.log`, `magnetic.log` | The eleven degree-16 supports give the stated Haar coefficient, and the independent polynomial overlaps agree in every visited local case. |
| `quotient.py`, `quotient.log` | Check the ordinary vacuum interval is positive, divide the signed endpoints in the stated order, and reproduce the final table. |

The proposed trusted base is the Lean kernel checking proof terms and the foundational axioms of the imported real analysis and Haar theory, to be reported by `#print axioms`. Integer products, comparisons, square-root enclosures and the sums must have kernel-checked witnesses. Python and its exact integers are certificate producers. No compiled-evaluator axiom, `native_decide`, unchecked floating point or external interval oracle is needed. The runner had no Lean installation, so the computational proof obligation remains open. The single-threaded arithmetic ran under the lab numeric lease with an RSS cutoff. The sandbox declined the requested `nice` adjustment and the programs completed at the runner's assigned priority.

## Next two rows

1. **Replay the signed gate.** Accept the numerical rejection when the kernel checks the full normalized table, records its axioms, and rejects fixtures that reverse the marked sign or omit the common vacuum. A failed identity or an interval reaching zero reopens the four-dimensional gate.
2. **Require a surviving coefficient before the four-direction inclusion.** A different exterior response must first show a strict four-dimensional decrement with its phase and reference fixed in advance, its fixed-charge zero, and its five-dimensional comparison. Only then test the proposed contraction-preserving rearrangement, entry throughout the band, a positive vacuum and a rational $v>0$ with $M_I(0)\le v/16$ and $M_I(v)-M_I(0)\le15v/16$ including every tail. A certified excess rejects those centres. The present ring supplies an increase in the frozen magnitude.
