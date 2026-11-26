## Repo search

Row 1573, research text at `ef017f4d8`. The target-specific prior is absent. I searched Markdown and TeX on `origin/main` (`8b11ae2bb`), `pr/10114` (`f76f6c649`), `pr/10133` (`89faef229`), `pr/10134` (`1e70c7211`) and `pr/10141` (`c73ad7b17`). Searches covered neutral purity and normalization, PUR-io, replica exchange and sewing, Haar isotopy, quaternion half-turns, even flux, conditional midpoint scores and Dobrushin comparison. Exact searches for a paired-link circle and for reparametrizing a swap by the thermal marginal returned no hits. The initial seam matches included the unrelated cycle-295 conjugate-source and cycles 319/324/327/330 FSWAP notes.

- Main, `.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/compact-forest-exchange.md`, (5)–(7). Exchanging selected forest chords of two posterior samples preserves product reference measure. For separate readers the covariance is half the mean of the product of the reader differences times $\tanh(\Delta_R/2)$. This is an endpoint involution for one fixed posterior.
- PRs 10114 and 10133, soft-route `MANUSCRIPT_RG.md`, RX8–RX9. In the fixed-depth flat-orbit limit, exchanging one unaligned link raises the sum of the two plaquette actions by $2[1-\operatorname{Re}\operatorname{tr}(U'_e U_e^*)/2]$ almost surely. This prices a mixed plaquette in a partial exchange. The question here concerns the two ends of a projected cylinder. The other two PRs supplied no relevant replica-exchange hit.
- In this lane the ordinary swap trace is already I3 of `gap-crux-skeleton-max.md`. Row 1337, `gap-solve44-astra62.md`, (1)–(2), writes the crossed affinity as the ordinary purity and differentiates it under *independent angular heat noise*. Row 1373, `gap-seed3-astra62.md`, uses projected thermal circles and prefix affinities. Row 1121, `gap-conv-in-law-check-opus.md`, §8.6, gives the mutual-plus-reverse information cost of an exchange and the one-site degree obstruction. Check 1123, `gap-l3-closure-check-astra.md`, lines 146–151, limits the obstruction to continuous site maps. Row 1258, `gap-mini-solve-ag-opus.md`, Proposition RR, bounds the doubling defect by the supremum of the absolute slab log cross-ratio. These endpoint and information identities are prior work.
- Row 1529, `gap-mech-attack-fable.md`, §3, and check 1539 identify the ordinary purity at infinite hopping in the Sp(2) construction. Spin inversion is outside SO(5), and the two independent neutral projections require additional treatment there. Row 1556, `gap-mech-direction4-check-astra62.md`, (v), constructs a Haar circle with a centre flip at its half-turn and integrates a mixed log-kernel derivative. Rows 1565/1566/1568 and checks 1570–1572 identify its consumer as relative electric-flux weights. Check 1571 proves weak compact Wilson U(1) fails the **electric** bound. Their neutral-spectator counterexample applies when the spectator lies wholly in the chosen projection. I use these results with that convention.
- Main’s `research/mass-gap/library/gap-flux-exercise.md` and `gap-skeleton-final.md` classify three sector choices for axis-exchange amplification. The Dobrushin search reaches `gap-form-exercise.md` and the prior digests `gap-fullread-1.md` and `gap-vir-lit.md`. Their primary source `gap-mid-max.md`, Theorem DOB, gives the periodic strong-coupling seed for $0<\beta<1/18$ via a one-link influence bound. The neutral interpolation needs a full-face mixed-derivative estimate.
- `open-registry.md` assigns TWO-PER to row 1520. Its statement transports purity in the *coupling* with a moving period. R11 concerns relative thermal transport as the coupling varies. The construction below varies the gluing at one fixed coupling and pair of periods. The older `prior/repo-search-2026-11-08.md` indexes 13 different targets. In the bounded searches I found no construction of the specific paired-link half-turn below. This is a search result with no priority claim.

**Published-work boundary.** The Sussman–Alpoge outline, with Claude and Codex, distinguishes mass preservation from a specified pushforward at lines 394–416 and requires a separate spectral estimate at 588–599 and 4629–4643. The pointers are `sa-index/chunk-01.md`, `sa-index/chunk-04.md` and `sa-index/obligations.md`. In CA-III, 10.7:prop-clustering-mass-gap, lines 108223–108268, *assuming* a unique vacuum and a positive gap gives exponential reflected decay. The converse purity estimate is outside that proposition. The supplied source revision is `31a47c543775`.

## Work plan

1. Check the target-specific prior, the registry, and the source ranges indexed for this row.
2. Search for existing statements and methods on neutral sewing, replica swaps, and gluing of two time periods. Record the exact overlap.
3. Test a candidate on the gapless model with an SU(2) factor and on a neutral spectator. Identify which configuration space and measure its endpoints use.
4. Prove a new first lemma or attack one precise obstruction by three distinct methods. Check the inference to purity, selectivity, and the status of the seed.

## Choice of interpolation and tests before using it

Write $v=u/2$, $k=k_v^+$ for the positive symmetric kernel of $P_0T^v$ on raw spatial links (including gauge averaging), and $S(x_1,x_2)=(x_2,x_1)$. The construction to test moves **one end** of two cylinders. It pairs adjacent spatial links and rotates the two relative quaternion axes in their common plane. The proposed estimate will concern the mean mixed boundary response along the resulting orbits. Fix the odd release block factor $b>1$, the level $g_0$ and a positive $\ell\in1024\mathbb N$. At cutoff $K$, $n=\ell b^K$, $u=n/512$ and $T$ is taken at the calibrated $\beta_K$. The target is $P_K\ge457/625$ for infinitely many $K$ at one fixed choice of these witnesses.

| Test | What the candidate has to do |
|---|---|
| (g4), neutral spectator | Sewing must exchange *all* degrees of freedom in the neutral Hilbert space. For a product $T_W\otimes T_m$ with centre acting on $W$ alone, the required endpoint ratio is $P_WP_m$. Moving only the $W$ fields returns $P_W$ and fails immediately. A neutral Gaussian field with physical mass tending to zero gives an explicit gapless member with an SU(2) factor below. This is a test of the transfer argument on products. The specified release trajectory is for pure Wilson. |
| (g1), (g2) | A neutral photon oscillator at the first nonzero spatial momentum suffices to make the endpoint small at this aspect. This gives an exact free comparison. For compact U(1) the odd-flux probability is removed by the three half-turn projections. The coset inequality behind row 1565 also controls a shift by two units, which stays in the projected space. For 5D SU(2) a free colour-singlet pair passes the light-state test. The corresponding interacting estimate is open. |
| (g3), twins | The endpoint is exactly one for the rank-one Wilson transfer at $\beta=0$ in every dimension and group. A mixed log-kernel derivative eliminates arbitrary one-end factors, including nonconstant rank-one vacuum profiles. This feature can be tested throughout a small positive coupling interval using pinned-boundary comparison. It does not distinguish 3D Villain at all couplings. |
| (g5), scale | Use $n=\ell b^K$, $v=n/1024$ at the release coupling itself. At fixed $n$ the neutral eigenvalue ratios of each fixed index tend to one as $\beta\to\infty$ by row 1215, (5). Thus for any fixed positive time the neutral purity tends to zero there, by $\sum p_i^2\le\max p_i$. |
| (g6), (t3), (t6) | The consumer is row 1468 §3.1. A finite-box identity will give the normalization, and an inequality must control its size at infinitely many release roots. No transport from a bare band is assumed. The quaternion construction uses SU(2). Its algebra alone has no phase or dimension selectivity. The sewing identity also makes sense for SU(3) and Villain kernels. Its quantitative estimate in those models requires separate evidence. |

The corrected twin test concerns a *line of proof*. A geometric construction that works in a gapped and a gapless model is admissible as a way to measure the response. An upper bound on that response must still distinguish the laws.

## A circle action on the doubled Wilson slice

**Lemma 1 (hand proof).** For every even spatial side there is a product of local circle actions on two copies of the raw SU(2) slice. Its diagonal circle preserves product Haar, commutes with simultaneous gauge and centre transformations, and equals the full replica swap at angle $\pi$ almost everywhere. Each moving link has speed at most one in the unit three-sphere metric. The orbit of every regular pair is smooth. No global continuity in the input field is assumed.

Pair the two links in direction $j$ incident to each vertex with even $j$-coordinate, along each $j$-line. Orient both into this vertex for the construction and invert back afterwards. This partitions the positive-direction spatial links into dimers. For one dimer let $(x_i,y_i)$ be the two replica values of link $i=1,2$. In unit quaternions put

$$
 r_i=x_i^{-1}y_i=\cos\theta_i+\sin\theta_i\, a_i,\qquad
 q_i=\cos(\theta_i/2)+\sin(\theta_i/2)\,a_i,\qquad m_i=x_iq_i .
$$

Here $0<\theta_i<\pi$ and $a_i$ is an imaginary unit vector. Assume $a_1,a_2$ are nonparallel. With $d=(a_1\times a_2)/|a_1\times a_2|$, rotate both axes about $d$ through $s$. Keep $m_i,\theta_i$ fixed, form $q_i(s)$ with the rotated axis, and output $(m_iq_i(s)^{-1},m_iq_i(s))$. The normal $d$ stays fixed along the orbit, so the angles add. At $\pi$ both axes reverse and each $q_i$ becomes $q_i^{-1}$. This exchanges the two replicas on both links. The speed and the Euclidean norm of the second angle derivative of each moving link are at most $\sin(\theta_i/2)\le1$. On the exceptional set for a dimer define its action as the identity for all $s$. The regular set is invariant.

For the Haar assertion, the change from $(x_i,y_i)$ to $(x_i,r_i)$ gives independent Haar variables. Conditional on $r_i$, right translation gives $m_i$ Haar. The two angles are independent of the two independent uniform axes. This follows from the polar volume form $\sin^2\theta\,d\theta\,d\omega$ on $S^3$ and proves that the exceptional set is null. Conditional on $\gamma=a_1\cdot a_2$, the frame
$(a_1,(a_2-\gamma a_1)/\sqrt{1-\gamma^2},d)$ is Haar on SO(3). Its law is invariant under every common spatial rotation, which acts transitively and freely on these frames. The motion is right multiplication of that frame by the *fixed* rotation through $s$ about its third body axis. It therefore preserves the conditional law, hence the full product Haar law. Independent angles on different dimers also preserve it. Write $R_s$ for the diagonal circle.

A simultaneous gauge transformation conjugates both $r_i$ in the same head frame. Rotations and the cross product respect that conjugation. The midpoints transform as the original oriented links, proving covariance. A common centre sign on a link multiplies its midpoint by that sign and fixes its relative quaternion. These assertions include the Borel convention on exceptional pairs.

**Where the projection occurs.** The two independent vertex-gauge and centre projections will be performed in the kernel. At intermediate angles $R_s$ is a deterministic map of *raw* links. If independent frame covariance is wanted throughout, put a relative frame $h$ in the compact group of vertex gauges and centre translations, with normalized Haar law. Keep it fixed and use the conjugated circle
$(x,y)\mapsto (a,h^{-1}b)$, where $(a,b)=R_s(x,hy)$. Under $(g_1,g_2)$ replace $h$ by $g_1hg_2^{-1}$. Diagonal covariance proves equivariance of this lifted motion. Fubini proves preservation of the extended reference measure. Its half-turn is $(hy,h^{-1}x)$, the swap on the two physical orbits. Forgetting the relative frame can randomize intermediate points. No deterministic quotient motion after forgetting it is used below.

**Regularity boundary.** Even allowing arbitrary mixing of all raw links, a jointly continuous homotopy from the identity to the replica swap is impossible. Insert one freely varying $S^3$ link in the first copy, set every other link to one, and project the output onto that same first-copy link. The purported homotopy would join the identity of $S^3$ (degree one) to a constant (degree zero). For a continuous endpoint, a Haar-almost-everywhere equality to the swap would already be equality everywhere by full support. This explains why smoothness *along* an orbit suffices here and why the null sets cannot simply be filled to give continuous field dependence. It extends the sitewise argument of check 1123 to coupled maps on the full raw slice.

## A deterministic motion on gauge and centre orbits

There is also an intrinsic construction when the pins must be physical orbits at *every* angle. Let $Q$ be the spatial link space modulo vertex gauges and the three centre translations, with the pushforward of product Haar. The neutral Hilbert space identifies with $L^2(Q)$. The following construction on $Q^2$ verifies that the swap can be reached even after forgetting all relative frames.

Fix a maximal tree. Its $r=|E|-|V|+1$ fundamental chord holonomies are independent Haar matrices before quotienting by common conjugation. Indeed the tree fixes the vertex frames recursively and the chord variables change only by fixed left and right translations conditional on the tree. This is the tree disintegration of Sussman–Alpoge, outline 7660–7681, also used in [the slice information calculation](gap-solve19-astra62.md). A centre translation multiplies each chord by its sign on the corresponding fundamental cycle. The fundamental cycles span the graph cycle space over $\mathbb F_2$ by elimination of their unique chords. The three straight windings have independent parity vectors, so select three fundamental cycles whose winding parities form a basis. Away from zero real parts, exactly one centre translation makes all three selected real parts positive. The resulting law is the product of three Haar hemisphere laws and ordinary Haar on all remaining chords. This follows by splitting into the eight sign cells and translating each onto the chosen one.

Write each quaternion as $\cos\theta_i+\sin\theta_i\,a_i$. The angles are independent with density proportional to $\sin^2\theta_i$ on $(0,\pi/2)$ for the selected three and $(0,\pi)$ otherwise. The axes are independent uniform two-sphere vectors. Remove common conjugation by using the frame of the first two axes in Lemma 1, on their full-measure nonparallel set. This frame choice is on file in [the Coulomb frame check, step (4)](gap-coulomb-frame-check-opus.md). What survives is the list of angles, the uniform dot product of the first two axes, and the remaining $r-2$ uniform axes in that frame. The latter are independent of the frame and dot product by rotation invariance and independence. These data reconstruct the orbit uniquely. For each remaining axis, height and azimuth are independent uniform interval coordinates off a meridian and its poles. This gives a full-measure smooth chart with product interval densities in $D=r+1+2(r-2)=3r-3=6n^3$ coordinates.

Send each interval coordinate through its own cumulative distribution and the inverse standard normal cumulative distribution. This identifies the chart smoothly with $\mathbb R^D$ equipped with standard Gaussian probability. For two chart points keep their normalized sum fixed and rotate their normalized difference through angle $s$ in each of $D/2$ fixed coordinate planes. This orthogonal motion preserves the product law, stays inside the chart for every angle, and at $\pi$ exchanges the two complete orbits. Conjugating back gives the claimed circle. Fix exceptional pairs off the chart. The quaternion dimer action of Lemma 1 additionally has a uniform link-speed bound, which is the bound used in (4)–(5). The chart construction has no such estimate here.

## Sewing the two projected cylinders

Use the symmetric magnetic sandwich for the Wilson transfer. In raw link variables $K_v(x,y)$ is the cylinder integral with the two end spatial actions at half weight and all temporal links integrated. It is symmetric, strictly positive and smooth at finite volume. This follows directly by reflecting the finite cylinder and differentiating its positive compact-group integral. Temporal links implement the vertex gauge averages. With normalized spatial Haar $dx$ put

$$
 k(x,y)=\tfrac18\sum_z K_v(x,C_z y),\quad
 L(X,Y)=k(x_1,y_1)k(x_2,y_2),\qquad X=(x_1,x_2),\quad Y=(y_1,y_2).
$$

These are the kernels of $A=P_0T^v$ and $A\otimes A$ on the raw space (extended by zero on the orthogonal complement). Projection commutes with $T$. The cylinder construction uses the transfer conventions of `gap-transfer.md` and the trace construction GL3/GL8 of the Sussman–Alpoge outline, lines 2195–2213 and 2313–2334. Kernel composition gives $\int k^2=\operatorname{Tr}A^2=Z_+(u)$. Define

$$
 d\mu(X,Y)=\frac{L(X,Y)^2}{Z_+(u)^2}\,dX\,dY,\qquad
 H(s)=\frac{\int L(X,Y)L(X,R_sY)\,dX\,dY}{Z_+(u)^2}.
$$

**Lemma 2 (hand proof).** $H$ is positive, $H(0)=1$, $H(\pi)=P_K$. At $\pi$ the four kernels in the numerator occur in the cycle $x_1,y_1,x_2,y_2,x_1$. Its integral is $\operatorname{Tr}A^4=Z_+(2u)$. In particular independent projection of the two starting copies gives precisely the one projection on the long circle since $P_0^4=P_0$. Haar preservation and Cauchy–Schwarz give $H(s)\le1$. The two endpoints reuse the prior crossed-affinity identity. Lemma 1 supplies the deterministic interpolation between them.

For regular $X,Y$, set
$$
 h(s,t;X,Y)=\partial_s\partial_t\log L(R_sX,R_tY),\qquad
 J(X,Y)=\log\frac{L(X,Y)}{L(X,SY)} .
$$
Simultaneous replica exchange leaves $L$ unchanged. The four corner values of $\log L$ are consequently $f,g,g,f$ with $f-g=J$. The fundamental theorem of calculus gives
$$
 J=\tfrac12\int_0^\pi\!\int_0^\pi h(s,t;X,Y)\,ds\,dt,\qquad
 P_K=\mathbb E_\mu e^{-J}.                                                   \tag{1}
$$
The other ends of the cylinders move independently in this calculation. Each mixed derivative is a sum of two pinned-cylinder covariances, one for each replica. More explicitly, at given transformed pins sample the centre label with mass proportional to $K_v(x,C_z y)$, then sample the intervening gauge links with the Wilson weight for those ends. The left and right scores are the derivatives of the log Boltzmann weight along the two prescribed pin velocities. For $v\ge2$ no plaquette reads both ends, giving the mixed derivative as their covariance in this *joint* law. The end spatial half-weights give single-end terms and drop out. Keeping the centre label in that covariance retains the covariance of the conditional means. Fixed-volume smoothness and strict positivity on a compact space bound the derivatives of $\log k$. The angle velocities are bounded even near exceptional dimers. This justifies differentiation on every regular orbit and Fubini under $\mu$, whose density is absolutely continuous. Only finitely many small $K$ could have $v<2$.

At the calibrated coupling consider the bound
$$
 B_K:=\tfrac12\int_0^\pi\!\int_0^\pi
         \mathbb E_\mu |h(s,t;X,Y)|\,ds\,dt
 \ \le\ \log(625/457)
 \quad\hbox{for infinitely many }K\hbox{ at one }(\ell,g_0).                 \tag{2}
$$
There is one absolute value *after* summing the link velocities and the two replica covariances. Jensen gives $-\log P_K\le\mathbb E_\mu J\le B_K$. Equation (1) alone is an equivalent readout. Estimate (2) pays extra for fluctuations, even after cancellation among the links. Its Wilson proof is open.

## What the signed and absolute responses cost

Let $p(x,y)=k(x,y)^2/Z_+(u)$ and $m=p_X\otimes p_Y$. Under $\mu$ the two $(x_i,y_i)$ are independent samples of $p$. The exchanged endpoints $(x_1,y_2)$ and $(x_2,y_1)$ each have law $m$. Hence
$$
 \mathbb E_\mu J
 =\int (p-m)\log p
 =D(p\Vert m)+D(m\Vert p).                                                \tag{3}
$$
Indeed $\log p=2\log k-\log Z_+(u)$, and the integral of $\log m$ against $p-m$ vanishes by equality of the marginals. This is the exchange information identity of row 1121, Lemma JI, applied to the projected cylinder. In particular controlling the signed mean in (1) already entails controlling the reverse relative entropy on independently recombined ends. A small purity deficit alone can coexist with a large reverse cost.

**Separation on the same boundary space (hand proof).** Take two nonnegative smooth functions $a,b$ of the trace of one contractible spatial plaquette, supported in disjoint open trace intervals and normalized in spatial Haar $L^2$. Both are gauge and centre invariant. Their Haar norms and the measures of fixed positive superlevel sets are independent of $n$, since one free edge makes that plaquette Haar. At each $v$ take a one-step transfer with kernel
$$
 a(x)a(y)+c^{1/v}b(x)b(y)+\delta,\qquad c=1/4,\quad \delta>0 .
$$
It is positive semidefinite, smooth, strictly positive pointwise and already independently projected at both ends. At fixed $n,v$, its $v$-step kernel tends uniformly to $aa^*+cbb^*$ as $\delta\downarrow0$ by finite product integration. Its rank is at most three. The purity tends to $(1+c^4)/(1+c^2)^2=257/289>457/625$.

Take the first pair of ends in a positive superlevel set of $a$ and the second pair in one of $b$. Their $\mu$-probability has a positive lower limit independent of size. On this event the direct kernel product stays bounded below, while both crossed kernels tend uniformly to zero. Thus $\mathbb E_\mu |J|\to\infty$. Pointwise (1) gives $B_K\ge\mathbb E_\mu |J|$. Choosing $\delta=\delta_K$ small at each $v_K$ gives a sequence with passing purity at every cutoff and $B_K\to\infty$. This separates (2) from the seed for positive transfer kernels *using the very same circle on the same projected slice*. One can even take $c=c_K\downarrow0$ first and then choose $\delta_K$ small enough that $B_K\ge K$ while $P_K\to1$. The constructed kernels are nonlocal transfer data. Logical separation on the single prescribed pure Wilson trajectory is unknown.

## The gapless spectator and the projected U(1) comparison

**A neutral spectator that the motion detects.** Take an independent real nearest-neighbour Gaussian scalar in four dimensions. In lattice units give it mass $m_K=b^{-2K}$ and take spacing $a_K=b^{-K}$, so that $m_K/a_K\to0$. At fixed $K$ the action is $\tfrac12\sum_{x,\mu}(\phi_{x+\hat\mu}-\phi_x)^2+\tfrac12m_K^2\sum_x\phi_x^2$, with periodic spatial boundaries. This has a positive trace-class transfer at each finite spatial size. The centre acts trivially on the scalar. In the doubled scalar slice keep the replica means fixed and rotate the differences on disjoint adjacent pairs of sites by the usual planar rotation. This preserves Lebesgue measure and exchanges the entire scalar pair at $\pi$. Taking it together with Lemma 1 gives $H_{\rm product}(s)=H_W(s)H_m(s)$, including both endpoints. Polynomial scores and Gaussian tails justify (1) for the enlarged example. Taking the Wilson factor at $\beta=0$ makes the gapless product example independent of any continuum hypothesis for interacting Yang–Mills. The finite-box inequality below applies to every independent Wilson factor.

One real sine or cosine oscillator at spatial momentum $(2\pi/n,0,0)$ has squared lattice frequency $\kappa=m_K^2+4\sin^2(\pi/n)$. Orthogonal spatial Fourier transformation factors the transfer into oscillators. The Gaussian integration of `gap-seam-max.md`, Lemma M, gives $\cosh\omega=1+\kappa/2$ and $\operatorname{Tr}T_q^u/\lambda_{q,0}^u=(1-e^{-u\omega})^{-1}$. Its purity is therefore $\tanh(u\omega/2)$. Every other factor has purity at most one. Since $\omega=2\operatorname{arsinh}(\sqrt\kappa/2)$, at each fixed $\ell$ we have $u\omega\to2\pi/512$. The full product thus has $\limsup P_{\rm product}\le\tanh(\pi/512)<457/625$ independently of $W$. This uses a nonzero spatial mode. Its continuum dispersion is $|p|$ on increasing physical tori, as follows from the same formula with lattice momentum $a_Kp$ and $\omega/a_K\to|p|$. Hence there are positive excitation energies arbitrarily close to zero in infinite volume. In particular (2) fails at its claimed inequality on a gapless member with an SU(2) factor. A cut rotation confined to the Wilson factor misses this example entirely.

**Weak compact U(1), with the same three order-two projections as the seed.** There is a stronger test than the free photon. In this comparison the half-turns keep all three integer electric charges *even*. Starting from the coset inequality of row 1565 one can exclude the passing neutral purity of this very projection. The distinction between even charge and zero integer charge matters.

Write $w=u$, $n/w=512$. For a coset $\mathcal D$ of exact dual integer two-forms in closed integer two-forms, let $S$ be row 1565's unit sheet increasing the first electric charge by one and preserving the others. Write $W_j(y)$ for the Villain mass of $\mathcal D+jS$ with real plaquette offsets $y$ and Villain parameter $\gamma$. Row 1565, lines 153–203, checked by 1571 §A2–A3 given the periodic Villain input, gives
$$
 \sqrt{W_{j+1}(y)W_{j-1}(y)}\ge d_\gamma W_j(y),\qquad
 d_\gamma=\exp[-1/(2\gamma)-M_\gamma/2] .
$$
The bound is uniform in the coset, offsets and these even tori. Also $d_\gamma\to1$. In the displayed bound of row 1565 for $M_\gamma$, $A=\gamma/384-(107\log3+\log4)/(4\pi^2)\to\infty$ and the two polynomially weighted exponential series tend to zero by domination at fixed large $A$. Use this coset conclusion *before* summing over odd charges.

For $f_j=\log W_j(y)$, the second difference with step two is the sum of the three unit second differences at $j-1,j,j+1$ with weights $1,2,1$. Consequently
$$
 W_{2}(y)+W_{-2}(y)\ \ge\ 2d_\gamma^{\,4} W_0(y).
$$
Sum over cosets having electric vector $(0,0,0)$. The two shifted families have electric vectors $(2,0,0)$ and $(-2,0,0)$ and are disjoint. All three families survive the indicated projection. By the seam character expansion in row 1565 these sums are precisely thermal charge masses. Choose $\gamma$ large enough that $d_\gamma^4>1/2$. Row 1565's positive-mixture lemma (6), valid for every fixed $t=1/\gamma$, represents the compact Wilson character weights at every sufficiently large $\beta_W$ by positive mixtures of these offset Gaussian weights. The inequality survives the integration. Thus for Villain at all sufficiently large $\gamma$, and for Wilson at all sufficiently large $\beta_W$,
$$
 Z_{\rm even}(u)\ \ge\ (1+2d_\gamma^4)Z_{Q=0}(u),\qquad
 P_{\rm even}\le\frac{\lambda_0^u}{Z_{\rm even}(u)}
             \le\frac1{1+2d_\gamma^4}<\tfrac12 .
$$
Here $\lambda_0$ is the largest physical transfer eigenvalue. Its eigenfunction is strictly positive and unique since the finite projected-to-gauge kernel is strictly positive. Every flat U(1) translation preserves that normalized positive eigenfunction, so it has zero integer charge and $\lambda_0^u\le Z_{Q=0}(u)$. The first purity inequality is $\sum p_i^2\le\max p_i$. This proves failure of (2) at sufficiently weak 4D compact U(1) for the literal three half-turns. If one projects instead under the *whole* continuous centre, the two shifted cosets leave the projected space and this proof gives no such conclusion. The free transverse-oscillator test still applies to that projection in the free model.

## Keeping the actual marginal at every angle

**Lemma 3 (hand proof).** The projected one-period Wilson marginal itself supplies a clock for Lemma 1. Put
$$
 \rho(x)=\int k(x,y)^2\,dy/Z_+(u),\qquad
 w(X)=\rho(x_1)\rho(x_2),\qquad \bar w(X)=\frac1{2\pi}\int_0^{2\pi}w(R_rX)\,dr.
$$
For each regular orbit define $\Theta_X(t)=\int_0^t w(R_rX)/\bar w(X)\,dr$ and $V_sX=R_{\Theta_X^{-1}(s)}X$. Both densities are strictly positive at finite volume. The clock uses only the diagonal of $P_0T^u$ and its scalar normalization cancels. In particular it does not require the long-period mass.

The orbit average is constant along the orbit, and the clock satisfies $\Theta_X(t+t')=\Theta_X(t)+\Theta_{R_tX}(t')$. This proves the group law after inversion. The symmetry of $w$ under $S$ gives $w(R_{r+\pi}X)=w(R_rX)$ almost everywhere and $\Theta_X(\pi)=\pi$. Therefore $V_\pi=S$ almost everywhere. In Haar orbit coordinates the conditional measure $w(R_tX)\,dt$ is uniform in the new angle. More explicitly, average any test function against $w(X)dX$ first around the old orbit using Haar invariance. In this average, $dt\,w(R_tX)=\bar w(X)d\Theta_X(t)$ and applying $V_s$ is translation by $s$ in the latter integral. This proves invariance of $w(X)dX$. The same argument applies on a constant exceptional orbit. This time change also applies on the physical orbit chart using its own reference probability. The estimates for (2) use the dimer action and the projected kernel.

Under the original sewn law $\mu$, the two pins $V_sX$ and $V_tY$ now each have the exact doubled one-period marginal for every $s,t$. In particular a bad event depending on either end alone has exactly its thermal probability, without any volume or coupling loss. At each fixed pair of initial ends this reparametrizes the square in (1) separately in its two coordinates with positive derivatives. Both the signed integral and the integral of the absolute mixed derivative are invariant under this substitution. Thus **the very same $B_K$ in (2) can be evaluated with thermally distributed single ends at all intermediate angles.**

One can also interpolate positive overlaps using this clock. With $dm=w(X)w(Y)\,dX\,dY$ and $f=\sqrt{d\mu/dm}$, the function $\int f(X,Y)f(X,V_sY)\,dm$ has endpoints $1,P_K$. A rank-one kernel gives $f\equiv1$ and this entire path is constant. For a general kernel the law of the pair of transformed ends relative to $m$ has density $f(V_{-s}X,V_{-t}Y)^2$. At $(0,\pi)$ its ratio to the straight density is $e^{-2J}$. Equality of the individual marginals supplies no bound on that ratio. More strongly, a motion fixing $X$, preserving $\mu$ and reaching $SY$ at a common half-turn would give $L(X,SY)=L(X,Y)$ almost everywhere. Positivity then makes all two-by-two minors of $k$ vanish. By continuity and full support they vanish everywhere, and fixing one pair of reference points factors $k(x,y)$ into a function of $x$ times a function of $y$. This rank-one obstruction applies to full joint invariance. The time change preserves each end marginal for every positive cylinder.

## Pinned comparison at small coupling

The following positive result covers a coupling interval in the gapped twins. Let $N=(d-1)n^{d-1}$ be the number of spatial links, $m_G=4$ for SU(2) and $m_G=2$ for U(1). Use $\beta$ fixed with $q=6(d-1)\beta/m_G<1$, $v\ge3$. For the ordinary, vertex-gauge-averaged cylinder let $M$ be the supremum of $|D_xD_y\log K_v|$ over all pins and tangent directions of speed at most one on each link. Then
$$
 M\le 6(d-1)N\beta^2\sum_{r\ge v-2}(r+1)q^r.                              \tag{4}
$$
This uses the pinned Dobrushin–Föllmer estimate (2.15) in row 1568, Theorem E, checked in 1572, Step 7. Its matrix $C$ is symmetric, supported on plaquette-neighbour links, with row sum at most $q$. It bounds a covariance by the coordinate Lipschitz constants contracted against $\sum_{r\ge0}(r+1)C^r$. For the full left boundary score only the inward temporal plaquettes contribute to the mixed derivative. Each differentiated plaquette has at most three free readers, each with chord-Lipschitz constant at most $\beta$, since quaternion multiplication and inversion preserve chord distances and the pinned velocity has norm at most one. The sum of left Lipschitz constants is at most $3N\beta$. One right-side free link occurs in at most $2(d-1)$ of those inward plaquettes, giving maximum right Lipschitz constant $2(d-1)\beta$. A plaquette-neighbour step changes the time coordinate by at most one. The supports are at least $v-2$ steps apart. These facts in (2.15) prove (4), including the overlaps on a *whole* face.

**Effect of centre averaging.** Put $K_z(x,y)=K_v(x,C_z y)=K_v(C_z^{-1}x,y)$. The mixed derivative of $\log\sum_z K_z$ is the mean of the individual mixed derivatives plus the covariance of their two first derivatives, with probabilities $K_z/\sum_z K_z$. To bound the range of the left derivative over $z$, keep $x$ and its velocity fixed and join any two right pins by componentwise geodesics of length at most $\pi$, traversed simultaneously at speed at most one. Integration gives range at most $\pi M$. The range of the *right* derivative is also at most $\pi M$ by the second expression for $K_z$, now moving only the left pins. Bounded variables of ranges $a,b$ have covariance of absolute value at most $ab/4$, by Cauchy–Schwarz and the interval variance bound. Thus
$$
 \sup |D_xD_y\log k|\le M+\pi^2 M^2/4,\qquad
 B_K\le\pi^2\big(M+\pi^2 M^2/4\big).                                      \tag{5}
$$
The last inequality includes both replicas and the factor $1/2$ in (2). This proof also works when the centre average is an integral. The quadratic term pays for the fluctuations of the centre label.

For the U(1) version of the circle, write each link pair as $m_i e^{\mp i\delta_i/2}$ with $-\pi<\delta_i<\pi$. Under pair Haar, the midpoints are independent Haar and the two differences are uniform on a square. At fixed $r=\max|\delta_i|$ move around the boundary of the concentric square by arclength, one circuit in $2\pi$. Conditional arclength is uniform because each side has the same normal speed as $r$ grows. The half-turn sends $\delta$ to $-\delta$. Each link speed is at most two. The paths are piecewise smooth, so integrate between the finitely many corners to get (1). This only multiplies the last bound in (5) by at most four. At $v=n/1024$ the polynomial $N$ is dominated by the exponential in (4). Hence (2)'s finite-box inequality holds for all sufficiently large $n$ at any such fixed $\beta$, in particular for 4D SU(2) at $\beta<2/9$, 4D compact Wilson U(1) at $\beta<1/9$, and 5D SU(2) at $\beta<1/6$. The corresponding line of proof fails in the order-one band and at the release roots when the row-sum majorant $q$ exceeds one. This is a failure of this comparison estimate. It supplies no lower bound on the physical $B_K$.

## Composition through the actual midpoint law

Write $v=r+r'$ with $r=\lfloor v/2\rfloor$ and $r'=\lceil v/2\rceil$ for $v\ge2$. For one replica fix $x,y$ and its endpoint tangents $\xi,\eta$. On the middle slice put
$$
 d\nu(z)=k_r^+(x,z)k_{r'}^+(z,y)\,dz/k_v^+(x,y),\qquad
 F(z)=D^x_\xi\log k_r^+(x,z),\quad G(z)=D^y_\eta\log k_{r'}^+(z,y).
$$
Composition uses $P_0^2=P_0$. Differentiating the two factors and their common normalizer gives the exact carry
$D^x_\xi D^y_\eta\log k_v^+(x,y)=\operatorname{Cov}_\nu(F,G)$.

There is a quadratic estimate here that keeps the midpoint pins in their true conditional law. Apply Lemma 3 to two independent middle slices with $w_\nu(z_1,z_2)=(d\nu/dz)(z_1)(d\nu/dz)(z_2)$. Denote the new angle generator by $\mathcal D$, and write $F_1=F(z_1)$, $G_1=G(z_1)$. Then
$$
 \left|D^x_\xi D^y_\eta\log k_v^+(x,y)\right|
 \le 2\|\mathcal D F_1\|_{L^2(\nu^2)}
        \|\mathcal D G_1\|_{L^2(\nu^2)}.                                  \tag{6}
$$
In fact the signed covariance equals twice the inner product of the odd parts of $F_1,G_1$ under the half-turn, by expanding $(F(z_1)-F(z_2))(G(z_1)-G(z_2))$ under $\nu^2$. For a stationary circle, the squared norm of the odd part of $F_1$ is at most $\|\mathcal DF_1\|^2$. To see this, apply scalar Fourier Parseval along each orbit, sum the squared coefficients of odd integer frequencies, and use $j^2\ge1$ there. Average over the initial point and use stationarity. The same holds for $G_1$, proving (6). Finite-box positivity bounds the reciprocal densities and all orbit derivatives used in this argument.

Each factor on the right of (6) is a mixed response of a **shorter projected slab**. For example, $\mathcal D F_1=D^{z_1}_{\dot z_1}D^x_\xi\log k_r^+(x,z_1)$, where $\dot z_1$ is the first-copy velocity at angle zero in the midpoint circle. The outer pins stay fixed during this derivative. One may insert (6) for the two replicas in (2) and average at the prescribed angles. The factor two in (6) cancels the prefactor $1/2$ in that bound.

The attempted iteration stops at a specific change of weight. The midpoint velocity equals its bounded link velocity from Lemma 1 times $\bar w_\nu/w_\nu$. For its squared norm under $\nu^2$, the weight on raw pairs is therefore $\bar w_\nu^2/w_\nu$. Even exact stationarity gives no upper bound on that inverse density. Moreover the two shorter responses are conditional root-mean-squares, while (2) is an absolute first moment in a periodic ensemble. Iterating (6) as a scalar inequality for $B_K$ would require those conditional estimates. No such replacement follows from (6). This calculation exposes where a law-dependent, dimension-sensitive estimate could enter a doubling step.

## Spectral positivity and the sign of the response

A possible shortcut in (2) would be to use reflection positivity to remove the absolute value. It fails already for the actual Wilson cylinder at every finite $\beta>0$. At *each* fixed $s,t$, $h(s,t)$ takes both signs on sets of positive $\mu$-measure. To prove this, average $\log L(R_sX,R_tY)$ over **independent product Haar** ends. The integral is constant in both angles. The bounded orbit derivatives give $\int h=0$ under that reference. The group law and Haar invariance make the distribution of $h$ the same at every angle pair. If it vanished almost everywhere, (1) and Fubini would imply $J=0$ and $P_K=1$.

For $\beta>0$ the one-link electric convolution has strictly positive multipliers in every spin (GL3). Its finite product is strictly positive as a quadratic form. The magnetic multipliers in the sandwich are everywhere positive and preserve the physical neutral subspace. The constant and a nonconstant elementary spatial plaquette trace are linearly independent there. Thus $A$ has at least two positive eigenvalues and $P_K<1$. This rules out $h=0$ almost everywhere. Zero Haar mean forces both signs. At finite volume $\mu$ and product Haar have the same null sets. This is the neutral-swap instance of the orbit-sign test used on the electric cut in check 1570. The sign of the *mean integrated* cost (3) is consistent with both signs at each angle.

The spectral version exhibits the missing estimate directly. Normalize the neutral eigenfunctions in spatial Haar, let $\psi_0>0$ be the normalized vacuum, and put $r_j=\lambda_j/\lambda_0$. In the vacuum measure $\pi_0=\psi_0^2\,dx$, define
$$
 R(x,y)=\frac{k_v^+(x,y)}{\lambda_0^v\psi_0(x)\psi_0(y)}-1 .
$$
Multiplying test functions by $\psi_0$ is unitary from $L^2(\pi_0)$ to raw $L^2(dx)$. Subtracting the vacuum projection therefore gives $\|R\|_{L^2(\pi_0\otimes\pi_0)}^2=\sum_{j>0}r_j^{2v}$, the neutral thermal excess at time $u$. Single-end vacuum factors cancel from the mixed derivative. What remains is
$$
 D_xD_y\log(1+R)=\frac{D_xD_yR}{1+R}
                  -\frac{(D_xR)(D_yR)}{(1+R)^2}.
$$
Even control of the thermal excess gives neither the differentiated kernels nor lower-tail control of $1+R$ at recombined pins. The separated-support transfer above supplies an explicit failure of that inference. Reflection positivity gives $P_K\le1$ and an exact positive spectrum. This route yields no order-one upper estimate on (2).

## Remaining comparison and release test

For 5D weak SU(2), a precise sufficient obstruction to (2) at a given box would be a neutral excited level of energy $E=-\log(\lambda/\lambda_0)$ with $uE<\log 2$. Then the vacuum thermal probability, and hence purity, is at most $(1+e^{-uE})^{-1}<2/3<457/625$. In the free linearized adjoint-field test, two transverse creation operators at opposite first spatial momenta give such a state. Contracting their adjoint indices with $\delta_{ab}$ makes it a global colour singlet. Nonzero momenta are unaffected by the flat centre translation. The pair has $E=2\omega$ with $\omega=2\operatorname{arsinh}\sin(\pi/n)$, so $uE\le4\pi/512<\log 2$. This free argument also works in 4D. Proving the corresponding neutral energy bound in the *interacting* weak 5D Wilson theory is open here. To exclude an infinitely-often seed one needs failure at every sufficiently late cutoff for each proposed pair of witnesses. A conjectured phase diagram alone supplies no finite-box inequality.

For SU(3) a fixed-conjugacy-class rotation can miss the inverse. A diagonal element with eigenvalues $e^{it},e^{it},e^{-2it}$, $0<t<\pi/3$, has a different eigenvalue multiset from its inverse. This limitation occurs at every coupling. For a positive symmetric SU(2) heat-kernel plaquette law the geometric and sewing lemmas still apply. The small-coupling constants in (4) are for the cosine Wilson action. No assertion about all couplings of the gapped three-dimensional compact Villain twin follows from those constants.

**Standing.** The paired-link circle, the separate circle on physical orbits, the time change preserving the thermal marginal, the neutral gluing formula, the conditional doubling inequality, and the stated small-coupling and comparison bounds have hand arguments above. The small-coupling bound uses row 1568's pinned covariance theorem. The interacting U(1) comparison uses row 1565's coset and positive-mixture results with the periodic Villain input identified there. No computation discharges a proof step. This is author research without an independent check or a Lean verification of these new lemmas.

The remaining statement on this route is exactly (2) for the physical SU(2) Wilson kernel at the release roots. The three attempts require, respectively, contraction of pinned influences at large coupling, control of the conditional midpoint responses in (6), and control of differentiated kernels with small denominators under recombination. The product comparison and the even-charge U(1) calculation distinguish the proposed estimate from the electric cut test. I cannot establish its required selectivity for interacting 5D SU(2), or its truth or falsity at the 4D release roots.

RESULT — A Haar-preserving paired-link circle reaches the full replica swap almost everywhere. A deterministic circle also exists directly on gauge and centre orbits. The thermal time change preserves the actual neutral marginal, and the half-turn reads $Z_+(2u)/Z_+(u)^2$. The sufficient mixed-covariance bound (2) holds at small fixed Wilson coupling, fails for the gapless neutral spectator and for weak 4D compact U(1) with the three order-two projections, and remains open on the calibrated SU(2) trajectory. Neither (PUR-io) nor the mass gap is proved or disproved.
