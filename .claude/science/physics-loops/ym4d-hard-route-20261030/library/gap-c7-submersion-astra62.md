# Repo search

FINISH row 1409, laptop Codex assignment `gpt-6.2-astra` at max effort. Research text pinned at `401d6e844984`. Bounded Markdown/TeX searches covered `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). Terms included Bakry–Émery, O'Neill, horizontal lifts, Riemannian submersion and straight-path decimation. A separate search for John Lott, `math/0211065`, weighted fibre transport, the literal `(M-neutral)` and the C7 filename returned no lines on those refs.

- **The map and the lift.** Main's July 12 `WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS` (0.2) gives the Haar split $(A,A^{-1}V)$. Its `DEEP_FIBER_COARSE_GAUGE_GIBBSIANNESS` sequel gives an exponentially quasilocal SU(3) marginal when its influence majorant is below $1/2$. Row 1383 gives the equal spread lift, conditional-score identity LIFT and Fisher bound $J(D_*\mu_\beta)\le J(\mu_\beta)/2$. These supply the coordinates and lift. They leave constancy of the horizontal Wilson score on regular quotient fibres to test here. [Row 1383, §2](gap-short-step-variance-fable.md) · [Check 1385](gap-short-step-variance-check-astra62.md)
- **Curvature.** On main, `research/mass-gap/library/prior/gap-fullread-2.md` §1 records Piazza–Shen's 2D, all-volume log-Sobolev bound from boundary convolution. Beside it, `gap-crux-lit-nonab.md` 31–42, 58 records Mondal's conditional $\Delta E\ge\hbar^2\Delta/2$ and Shen–Zhu–Zhu's strong-coupling bound $|\beta|<1/[16(d-1)]$ in their convention. PR 10114's `LCONV55.md` C2 identifies the bare-action quotient Hessian with the horizontal Hessian. Its `FLOW.md` 3743–3751 tests covariance of a length-three straight derivative. None gives weighted Wilson block transport.
- **The observable.** The November 8 digest §11 points to `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on PRs 10114/10133, a positive lower bound on a one-time-step plaquette correlation. PR 10141's `research/ym4d/library/fp1.md` (8) compares two flat, constrained curl-energy minima. Neither controls the neutral thermal trace. [November 8 search](prior/repo-search-2026-11-08.md)
- **The lane and account.** F1 and idea 18 propose block-scale and averaged orbit curvature. Row 957's sampled Hessian failure is GUIDE. C1 of row 1380 bounds the response estimate for lab-frame corner moves below by $((72/7)K+(3/2)B)\|[h]\|^2$. TAD's mass-like cost is argued. Row 1402 §2.3 proposes C7, and check 1407 leaves the weighted transport and scale factor open. Sussman and Alpoge, with Claude and Codex (supplied `31a47c543775`), give local coarea in QC25 (outline 8329–8349) and the linear curl factor $n^{4-d}$ for their averaged map in CF4, CF8–CF10 (8465–8478, 8519–8554). CA-I 2699–2712 leaves the mass gap outside Theorem 0. Bałaban's constrained propagator estimates enter the ultraviolet work. The target-specific prior is absent. The registry's H-C7a/b concern translations of histories and independence from the target coupling. [F1](gap-afield-a-max.md) · [Idea 18](gap-brainstorm2-max.md) · [Row 957](gap-ps-disint-max.md) · [C1 and TAD](gap-mech-direction-fable.md) · [Row 1402](gap-band-fresh-fable.md) · [Check 1407](gap-band-fresh-check-astra62.md) · [Outline index](sa-index/README.md) · [Obligations](sa-index/obligations.md) · [Bałaban record](lit-balaban.md)

## Plan saved at the start

1. Read the target-specific prior and the owner's goal, finish rules, filter, and named checks. Check ownership and search the repository and outline index before deriving anything.
2. Specify a Wilson map, metrics in physical units, measures, and a stiffness tied to a physical observable. Write down the conditional measures and the Lott transport test, including the treatment of orbit strata.
3. Apply (t1)–(t5) and requirement (b) before attempting a proof. Compare compact U(1), dimensions four and five, and large beta on a fixed lattice. Test equivalence to the seed.
4. Prove the outcome at the scope of the specified map and class. Record the consequences for the checked chain, the next two rows, and their decisive outcomes. Research text only.

The object selected for the filter is the deterministic two-link product of row 1383 with the physical connection $L^2$ metrics. Its conditional law fails the transport test for every positive coupling, including on the regular gauge quotient. Equations (7) and (9) give the obstruction and the scale factors. The neutral Wilson seed remains open.

## One proposed step and its physical readout

Take a rectangular periodic lattice with even side lengths at least 16 in fine units. The seed boxes eventually meet this restriction in every direction, including Euclidean time. Let $d=4$ or $5$, $G=SU(N)$ with $N=2$ or $3$, and $\chi(g)=\operatorname{Re}\operatorname{tr}(g)/N$. On anti-Hermitian Lie algebra elements put $\langle X,Y\rangle=-\operatorname{Re}\operatorname{tr}(XY)/N$. Write $X_e=\dot U_eU_e^{-1}$. For mesh $\ell$ use the connection metric
$$
 g_\ell(X,X)=s_\ell\sum_{e\in E_\ell}|X_e|^2,\qquad s_\ell=\ell^{d-2}.
 \tag{1}
$$
The factor is fixed by the physical $L^2$ norm of a variation of a connection. Its infinitesimal holonomy angle is $\ell\,\delta A$ to leading order in the mesh, and its cell volume is $\ell^d$. Use (1) at both $\ell=a$ and $\ell=2a$. The gauge group $G^{\mathrm{sites}_\ell}$ acts by $U_{xy}\mapsto k_xU_{xy}k_y^{-1}$. Give its principal quotient the metric of horizontal lifts.

For each coarse positive edge from an even site, set $V_c=D(U)_c=u_cv_c$, in path order. These strings have disjoint fine edges. Let $z$ denote all off-string links, $h_c=u_c$, and $U(V,h,z)$ the resulting fine field with $v_c=h_c^{-1}V_c$. Put $S=\sum_p(1-\chi(U_p))$. The two probability measures are exactly
$$
 d\mu_\beta=Z^{-1}e^{-\beta S}dU,\qquad
 d\nu_\beta=D_*d\mu_\beta=Z^{-1}H_\beta(V)\,dV,\qquad
 H_\beta(V)=\int e^{-\beta S(U(V,h,z))}\,dh\,dz.                    \tag{2}
$$
All bare coordinate measures here are normalized Haar products. Inserting $v_c=h_c^{-1}V_c$ in each Haar integral gives the conditional probability
$$
 d\mu_{\beta,V}(h,z)=H_\beta(V)^{-1}e^{-\beta S(U(V,h,z))}\,dh\,dz. \tag{3}
$$
In particular the effective potential is $-\log H_\beta$ up to a constant. Gauge reduction pushes both probability measures forward. On the regular quotient one must include the orbit-volume density in the potential relative to quotient Riemannian volume.

Choose a non-wrapping spatial rectangle $\Gamma$ of fixed physical size on the common grid. $W_\Gamma=\chi(\operatorname{hol}_\Gamma)$ is gauge invariant and electric-centre neutral. Its two realizations obey $W_f=W_c\circ D$ pointwise. Fix its normalization on both lattices, including the source $JW_\Gamma$. A positive stiffness that a Bakry–Émery bound can actually certify is the Dirichlet energy per unit equilibrium variance of this probe,
$$
 R_\ell(W)=\frac{\int|\nabla_{g_\ell}W|^2\,d\mu_\ell}
                 {\operatorname{Var}_{\mu_\ell}W},\qquad
 k_\ell(W)=s_\ell R_\ell(W),                                        \tag{4}
$$
with $\mu_a=\mu_\beta$ and $\mu_{2a}=\nu_\beta$. Positivity follows from full support and the smooth nonconstant loop. $R_\ell$ has the units of an inverse squared configuration-space distance. $k_\ell$ is its dimensionless form. For the external source $J$, let $B(J)=\log\mathbb E e^{JW_\Gamma}$. Its Legendre transform has stiffness $I_\Gamma=(B^*)^{\prime\prime}(\mathbb E W_\Gamma)=1/B^{\prime\prime}(0)=1/\operatorname{Var}W_\Gamma$. This is the free-energy cost to change the mean of the same physical loop. A positive lower bound $\operatorname{Ric}_{g_\ell}+\operatorname{Hess}_{g_\ell}V_\ell\ge\rho_\ell g_\ell$ on the smooth compact link space gives $R_\ell(W)\ge\rho_\ell$ by the integrated Bochner identity. On an eigenfunction of the negative weighted Laplacian with eigenvalue $\lambda>0$, it gives $\lambda^2\|f\|_2^2\ge\rho_\ell\lambda\|f\|_2^2$. Expanding the centred loop in eigenfunctions gives the bound. Thus $x_\ell=s_\ell\rho_\ell$ is a certified floor for $k_\ell$. The same loop integrals are defined on the gauge quotient by horizontal gradients. No global smooth Bochner argument on a singular quotient is being assumed.

**Statement to filter.** For $x>0$ write $\mathcal B_\ell(x)$ for the class with $\operatorname{Ric}+\operatorname{Hess} V_\ell\ge (x/s_\ell)g_\ell$. Test the following factor-two step at each admitted Wilson coupling in the band. Horizontal lifts for $D$ must transport the normalized conditionals. The requested dimension carry and a positive gauge O'Neill contribution to the floor would take the form
$$
 \mathcal B_a(x)\ \Longrightarrow\
 \mathcal B_{2a}\big(2^{d-4}x+\eta_G\big),
 \qquad \eta_{SU(2)}>0,\quad \eta_{U(1)}=0 .
$$
One may allow $\eta_G$ to depend on the size and coupling for this first test. The plus sign denotes an improvement of a curvature *lower bound*. Row 1386's inverse-coupling recursion subtracts its group gain. Identifying a stiffness that relates these two estimates would require a physical comparison. Already at one step a genuine improvement could be read against the bound $I_\Gamma\ge\rho_\ell/\mathcal E_\ell(W)$, where $\mathcal E_\ell(W)=\int|\nabla W|^2d\mu_\ell$. Exact fibre transport is a prerequisite regardless of the size or sign of the proposed increment.

## Which measure horizontal transport must preserve

Let $p:(M,g)\to(B,b)$ be a smooth Riemannian submersion with measure $\phi\,d\mathrm{vol}_g$. Lott's Theorem 2(1) requires horizontal transport to carry $\phi\,d\mathrm{vol}_{F}$ to a scalar multiple on the destination fibre. Normalizing the two fibre masses makes this an exact equality of probabilities. In (3.9) the horizontal curvature average and the nonnegative terms $2|A_X|^2+|T_X|^2$ are accompanied by **minus the conditional variance** of the logarithmic rate of the fibre measure. The transport hypothesis makes this variance zero in (3.10)–(3.11). It is stronger than positivity of $H_\beta$ or compactness of the fibres. [John Lott, Theorem 2 and equations (3.9)–(3.11)](https://arxiv.org/pdf/math/0211065)

For one pair the differential is $(X_1,X_2)\mapsto X_1+\operatorname{Ad}_{u}X_2$. For a prescribed velocity $Y=\dot V V^{-1}$ row 1383's equal spread gives the metric-horizontal lift
$$
 X_1=Y/2,\qquad X_2=\operatorname{Ad}_{u^{-1}}Y/2,\qquad X_z=0.     \tag{5}
$$
Indeed both summands in the differential then equal $Y/2$. Every other solution differs by $(K,-\operatorname{Ad}_{u^{-1}}K)$ on a pair and by free off-string velocities. Their inner product with (5) vanishes, so any such change adds its squared norm. Distinct pairs are orthogonal. The metric that gives a true submersion on raw coarse links is therefore $\widehat g=(s_a/2)\sum_c|Y_c|^2$. The physical coarse metric is a constant multiple of $\widehat g$, so it has the same horizontal lifts. In (3) this transport takes $h_c$ to $r_c(t)h_c$, with $\dot r_cr_c^{-1}=Y_c(t)/2$, $r_c(0)=1$, and fixes $z$. It preserves the reference $dh\,dz$. Equivalently the induced fibre volume is a fixed multiple of that product (one pair gives $2s_a|X_h|^2$ vertically). Consequently (3) passes Lott's hypothesis exactly when
$$
 S(U_t)-S(U_0)\ \text{is constant on the starting fibre for each path},\qquad \beta>0. \tag{6}
$$
At $\beta=0$ normalized Haar passes. Equation (6) tests the interacting probability.

### An explicit regular fibre where (6) fails

Select the coarse winding row in direction 1 at transverse coordinate zero. Keep its initial links at the identity. To fix the orbit type, put one nontrivial coarse 1-link on each of two parallel rows at coarse transverse coordinates $y_2=2,4$. Put $T=i\,\operatorname{diag}(1,-1,0,\ldots,0)$. Pick $P=\exp(\pi T/2)$ and $Q$ a determinant-one scalar multiple of the cyclic shift. In both groups $P$ has distinct eigenvalues. A matrix commuting with $P$ is diagonal, and commuting with $Q$ makes all its diagonal entries equal. The two row holonomies therefore have common centralizer $Z(G)$. They can be based at the origin by paths made of identity 2-links. Realize each product with the first fine link equal to one. All other links start at one except the single off-string link described below.

Move every coarse link of the selected row to $\exp(tT)$, holding all other coarse links fixed. This path is gauge-horizontal throughout. At each row vertex the outgoing $T$ cancels the incoming $\operatorname{Ad}_{\exp(-tT)}T=T$ in the inner product with any infinitesimal site rotation. Off the row both are zero. By (5) all fine links along the row move to $\exp(tT/2)$.

Take the fine 1-link from $e_2$ to $e_2+e_1$. Its odd transverse coordinate excludes it from every retained pair. Define two fine fields on the same fibre by putting $D_\pm=\exp(\pm\pi T/2)$ there. Hold that link fixed under transport. Exactly one elementary square contains both this link and a moving row link. In its trace we may choose the orientation giving $\chi(\exp(tT/2)D_\pm^{-1})$. All other plaquettes either have the same increment for both fields or have zero increment. On this square
$$
 \chi(\exp(tT/2)D_\pm^{-1})=
 \frac{N-2+2\cos(t/2\mp\pi/2)}{N}.
$$
Write $P_t$ for horizontal fibre transport and $L_t=d(P_t^*\mu_{\beta,V(t)})/d\mu_{\beta,V(0)}$ for its conditional density ratio. In the log ratio at the two starting points, $H_\beta(V(0))/H_\beta(V(t))$ cancels. Equation (3) gives the finite identity
$$
 \log L_t(U_+)-\log L_t(U_-)=\frac{4\beta}{N}\sin(t/2).             \tag{7}
$$
For every $\beta>0$ this differs from zero for $0<t<2\pi$. Its derivative at zero is $2\beta/N$. The two smooth density ratios differ on fibre neighbourhoods of positive conditional measure. Thus even the infinitesimal score has strictly positive conditional variance. No uniform lower bound on the mass of those neighbourhoods as $\beta$ varies is needed.

**After dividing by gauge transformations.** Write $q_f,q_c$ for the site-gauge quotients and $\bar D\,q_f=q_cD$. Because every coarse site transformation extends to the fine sites, equivariance of (2)–(3) gives the conditional probability over $[V]$ as $(q_f)_*\mu_{\beta,V}$. Indeed the integral of any gauge-invariant test against (3) depends only on $[V]$, and its further integral gives the fine expectation. This includes the orbit-volume weighting.

A lift (5) of a coarse gauge-horizontal $Y$ is orthogonal to every fine vector whose image under $dD$ is coarse-gauge vertical. This follows from $g_a(Y^\uparrow,Z)=\widehat g(Y,dD\,Z)$. In particular it is horizontal for the fine gauge action, and its projection is the horizontal lift for $\bar D$ with the induced metric. On the chosen path the two distant holonomies stay fixed, so every coarse stabilizer is exactly the diagonal centre. For a fine stabilizer, its value at the origin commutes with both of those same loop holonomies, and propagating a central value along a connected graph gives the same value everywhere. Thus the whole calculation lies over the regular orbit type. In each fibre, representatives are identified by interior site rotations and by the common centre at the coarse sites. These transformations preserve (3), commute with the lifted transport, and preserve $S$ at both endpoints. One can distinguish the two starting orbits directly. Concatenate the remote loop with holonomy $P$, based at the origin, and the distinguished square based there. Its normalized trace is $\chi(PD_+^{-1})=1$ versus $\chi(PD_-^{-1})=(N-4)/N$. Consequently $L_t$ descends as the density ratio for the quotient conditionals. Equation (7) survives unchanged. Local smooth lifts near these regular fields also preserve the strict inequality on an open set of nearby base points.

The full nonabelian quotient does have singular orbits. At identity links the stabilizer contains the full diagonal $SU(N)$, while on the displayed patch it is only the centre. Lott's smooth-submersion theorem cannot simply be invoked across that change of dimension. For the gauge quotient alone, equivariant orbit transport on a single orbit type preserves the normalized invariant orbital probabilities. The block fibre contains different Wilson actions even *after* this orbital integration. Any proposal extending exact transport to the entire quotient would already have to satisfy (7) on its regular patch. [Lott's single-orbit-type example, §3](https://arxiv.org/pdf/math/0211065)

There is an entry check at the other end of the coupling range. At a fixed finite lattice the bi-invariant $SU(N)$ product has strictly positive Ricci curvature. On each simple factor its Ricci form is $\tfrac14\sum_j|[X,e_j]|^2$ for a metric-orthonormal basis, by $\nabla_XY=[X,Y]/2$ on left-invariant fields. Its kernel is the Lie algebra centre. Compactness bounds $\|\operatorname{Hess}S\|$. Hence for all sufficiently small positive $\beta$, the *fine* link law has a positive Bakry–Émery floor and (7) still breaks the transport premise. The obstruction therefore does not depend on the sampled weak-coupling curvature failure in row 957.

## Row 1386 filter

**(t1) Compact $U(1)$.** In link angles the infinitesimal site action is the same incidence map $d_0$ at every field. The gauge-horizontal space is the constant subspace $\ker d_0^*$. Constant horizontal lifts span it, so at every point
$$
 A^{\rm gauge}_X Y=\tfrac12\operatorname{pr}_{\rm vert}[\widetilde X,\widetilde Y]=0. \tag{8}
$$
This is the line at which the proposed O'Neill gain is exactly zero. The straight block map is also linear in angles and has constant horizontal spaces. Its Wilson conditional score can nevertheless vary. With the same off-string link at angles $\pm\pi/2$, the difference in (7) for $\chi(e^{i\theta})=\cos\theta$ is $2\beta\sin(t/2)$. Thus the score variance cannot be counted as the nonabelian gain. Check 1385 already obtains a strictly positive abelian conditional variance for its harmonic lift. A nonzero bracket for $SU(2)$ would have to overcome the variance in Lott's (3.9) to give an estimate without his transport hypothesis. Equation (7) supplies no comparison of their sizes. [Check 1385, lines 37–52](gap-short-step-variance-check-astra62.md)

**(t2) Five dimensions and requirement (b).** Define $c(d)$ to multiply an *inherited physical curvature floor*, with $\rho$ measured against (1) on each lattice. The squared length dilation of $D$ is $\lambda_d^2=2s_{2a}/s_a=2^{d-1}$ by (5). Thus $g_{2a}=\lambda_d^2\widehat g$. A covariant tensor lower bound $\rho\,\widehat g$ reads $(\rho/\lambda_d^2)g_{2a}$. Taking the metric adjoint in (5) gives an exact test on observables, valid for every smooth coarse function $F$,
$$
 |\nabla_a(F\circ D)|^2=\lambda_d^2|\nabla_{2a}F|^2\circ D,\quad
 \operatorname{Var}_{\mu_\beta}(W_c\circ D)=\operatorname{Var}_{\nu_\beta}(W_c),
 \quad R_{2a}(W_c)=2^{1-d}R_a(W_f).                                \tag{9}
$$
Integration in (9) uses the actual pushforward (2). For invariant $F$ its gradients are horizontal, giving the same equality on gauge classes. These equalities compare the same loop, down to its source normalization.

| Quantity for one doubling | $d=4$ | $d=5$ |
|---|---:|---:|
| Squared horizontal length dilation $\lambda_d^2$ | $8$ | $16$ |
| $c(d)=1/\lambda_d^2$, also $R_{2a}/R_a$ for the loop | $1/8$ | $1/16$ |
| Dimensionless stiffness $k_{2a}/k_a$ | $1/2$ | $1/2$ |
| Inverse susceptibility ratio for the same loop source | $1$ | $1$ |
| Classical inverse-coupling factor required by (b) | $1$ | $2$ |

For the last row the Wilson quadratic term for a smooth curvature is $\frac12\beta_\ell\ell^{4-d}\int\sum_{\mu<\nu}|F_{\mu\nu}|^2$. A plaquette contributes $\ell^4$ at second order and there are $\ell^{-d}$ cells per unit physical volume. Holding its coefficient fixed gives $\beta_{2a}=2^{d-4}\beta_a$. This is classical matching. It does not identify the potential of (2) with a Wilson action at that coupling. For (4) the factor on every doubling is instead $1/2$ in lattice units, including when the measures are successive exact images and the contour exists on every grid. The physical source has exactly the same generating function $\mathbb E e^{JW}$ on either side. Assigning $\widehat g$ to the coarse links could set the metric descent coefficient to one in **every** dimension. In the bound on $I_\Gamma$ the inherited floor and the Dirichlet energy carry the same factor, so $(c(d)\rho_a)/\mathcal E_{2a}(W_c)=\rho_a/\mathcal E_a(W_f)$. The certified bound on the physical source is consequently invariant under this rescaling. Requirement (b) fails for this proposed carry. Equation (9) does not compute the optimal Bakry–Émery constant of the coarse law.

**(t3) $SU(3)$.** The common centralizer construction and (5) apply verbatim to $N=3$. In (7) the third eigenvalue contributes one to each trace and cancels in the difference. The two infinitesimal log rates differ by $2\beta/3$. Thus the same transport hypothesis fails on regular $SU(3)$ orbits. The issue already occurs in one two-colour plane.

**(t4) Increasing $\beta$ on a fixed lattice.** The unweighted geometry is independent of $\beta$. The two conditional log rates in (7) separate linearly in $\beta$ at every positive coupling. The pointwise fine curvature floor also fails at large $\beta$, including on the principal quotient. To see it there, retain the distant pair $P,Q$, remove the off-string change, and set *every fine link* on the selected winding row to $\exp((\pi+t)T)$. This product geodesic is gauge-horizontal by the same incoming/outgoing cancellation. The row has $n_1$ fine links. Each belongs to $2(d-1)$ distinct adjacent plaquettes, each with just one moving link. On each such plaquette $S''(0)=-2/N$ since $\chi=(N-2-2\cos t)/N$. The tangent $X$ has $|X|_{g_a}^2=s_an_1(2/N)$. The projected path is a geodesic on the regular quotient, so both upstairs and downstairs
$$
 \frac{\operatorname{Hess} S(X,X)}{|X|^2_{g_a}}=-\frac{2(d-1)}{s_a}.
 \tag{10}
$$
At this fixed regular point, the geometric Ricci term and the Hessian of minus log orbit volume downstairs are finite and independent of $\beta$. The weighted curvature in this direction is therefore $C-2(d-1)\beta/s_a$ for a fixed $C$. It tends to $-\infty$. A positive pointwise floor on this box therefore requires $\beta<Cs_a/[2(d-1)]$. Row 957, Lemma SEP, uses a flipped link on a retained skeleton. The winding row here makes the negative direction horizontal at a regular point of the full gauge quotient. This argument concerns the pointwise class. It estimates no probability of a bad field.

There is also a direct physical check. On a fixed lattice $S=0$ requires every elementary holonomy to be the identity, so $W_\Gamma=1$ for the contractible rectangle. By compactness $S$ has a strictly positive minimum $m$ on any nonempty closed set $|1-W_\Gamma|\ge\delta>0$. The Wilson probability of the set is bounded by $e^{-\beta m/2}/\operatorname{Haar}\{S<m/2\}$. Thus $\operatorname{Var}W_\Gamma\to0$ and the inverse loop susceptibility diverges for both measures. These fixed-lattice limits do not address the simultaneous change of cutoff and coupling in the seed.

**(t5) A separation from the seed.** There is a Wilson comparison on which the *same neutral trace test* is true while (6) is false. Fix $0<\beta_*\le 1/25600$ and let $n$ run over large admissible sides in four dimensions with $a=L/n$ for a fixed $L$. Set $t_0=\lceil\log_2 n\rceil$. The strong-coupling part of row 708, checked in the cited note, gives
$$
 \log(1+S_{\rm per}(t_0;n^3,\beta_*))
 \le \frac{101}{10000}\frac{t_0}{n}.
$$
This uses the existing strong-coupling cube bound and Proposition Delta, before the separate transfer estimate $(\mathrm{VIR}_K)$ enters. The neutral sector contains the vacuum, so its excited trace is bounded above by the full periodic excited trace. For $t=2\lfloor n/1024\rfloor\ge t_0$ at all sufficiently large $n$, monotonicity gives
$$
 s_{n,\beta_*}(t)\le \exp\!\left(\frac{101t_0}{10000n}\right)-1\ \longrightarrow\ 0.
 \tag{11}
$$
In particular the seed inequality $s(t)\le4/21$ holds at that very aspect ratio. Equation (7) violates Lott's transport hypothesis on every one of these boxes. This disproves necessity of the geometric premise for the seed test in the Wilson family. The comparison uses fixed strong coupling, outside the prescribed asymptotically free trajectory. The argument for (7) uses a local plaquette and the conditional law, with no spectral input. [Strong-coupling cube estimate, Thm. 1(iii)](gap-seed-sc.md) · [Row 708, Prop. Delta and proof of TR1](gap-mid-max.md) · [Check of the starting estimate, §7](gap-dob-astra.md)

## Consequence for the neutral seed

**Result for row 1409.** For the two-link product map, every $\beta>0$, $N=2,3$ and the stated tori in dimensions four and five, (7) refutes exact weighted-fibre transport, even on the principal gauge quotient. Multiplying either lattice metric by a positive configuration-independent scalar leaves the horizontal transport in (5) unchanged and cannot repair (7). With the physical metrics, (9) also fixes the observable carry. This stops the Lott argument at its first interacting step. A different block map, a metric with a different horizontal distribution, or an estimate controlling the variance term in (3.9) would require a separate test. The proof makes no assertion about the sign of the full curvature difference when that variance is kept.

For the target itself, row 1367 fixes **one** admissible physical side $L$, $n_j=L/a_j$ with $4\mid n_j$ and $n_j\ge2^{70}$ eventually, and the prescribed trajectory with $\beta_0\le\beta_j\le B_0\log n_j$. At zero spatial twist, $P_0$ projects onto the sector invariant under the eight electric-centre translations. With $x_i=\lambda_i/\lambda_0$ in this sector the required bound is $\sum_{i>0} x_i^{\,2\lfloor n_j/1024\rfloor}\le4/21$ at every late cutoff, including multiplicities. Row 1356 and check 1359 give the optimal squared rank-one error $s(2w)/(1+s(2w))$ and hence this threshold at tolerance $2/5$. This direction implies (N-phys) within the time cap. The converse can require a larger admissible side. Proposition C of row 1342 with check 1349 carries the neutral input in either flux alternative to the gap on the matched reflection-positive continuum datum under (P1)–(P4), (H2) and totality. A configuration-space curvature bound on (2) would itself still need a comparison with that **transfer** trace. The one-cube estimate on the prescribed trajectory and the physical gap remain open. [Row 1367](gap-seed-astra62.md) · [Row 1356](gap-mini-mneutral-fable.md) · [Check 1359](gap-mini-mneutral-check-astra.md) · [Row 1342](gap-seed-audit-fable.md) · [Check 1349](gap-seed-audit-check-astra.md)

The new results are hand derivations awaiting a separate check. They use no computer-generated proof step, Lean evaluator, floating-point calculation or Monte Carlo run. This note grants no status.

## Next two rows and their decisive outcomes

1. **Cross-provider check of 1409.** Compute the derivative of a normalized conditional expectation using a smooth test localized near one of the two regular fibre orbits. The loop through $P$ and the distinguished square separates them. Compare this calculation with (7). Check the physical adjoint in (9), the fixed-lattice sign in (10), and the time used in (11). If the ratios differ as claimed, retire exact Lott transport for this map and metric class. If orbital disintegration cancels the difference, exhibit the cancelling factor and reopen precisely that quotient case.
2. **Resume the ultraviolet carry at the native endpoints identified by check 1408.** For each good aligned label, subtract the two complete real endpoint formulas with their own masks, chart, carrying action and inner quadratic. If the difference fits the existing site charges, the one-law count moment suffices for the weight comparison. If an excess survives on the actual common passing set with a controlled coefficient, that excess specifies the action-moment estimate to test. Use the existing PD-REST and ZONE-FORM owners for their inputs. An unresolved endpoint identification leaves that row open. No further band proof row follows from this C7 specification. [Check 1408, next-row decision](gap-univk-pwc-check-astra62.md)
