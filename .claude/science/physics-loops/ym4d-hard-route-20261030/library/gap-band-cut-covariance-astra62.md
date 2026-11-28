## Repo search

Row 1565, author research at `ef0804c54`. All estimates below are written arguments. There was no Lean run or independent check, and this note grants no status. The target-specific prior inventory was absent. I searched `origin/main` (`8b11ae2bb`), `pr/10114` (`f76f6c649`), `pr/10133` (`89faef229`), `pr/10134` (`1e70c7211`) and `pr/10141` (`c73ad7b17`). Bounded `git grep` terms included cut covariance, mixed boundary response/derivative/covariance, four-corner twist/cylinder, pinned-spin stiffness, Dobrushin with Wilson or plaquette, strong-coupling mixing/expansion, cylinder twist, Dirichlet-to-Neumann with Maxwell/gauge, helicity modulus and harmonic flux variance.

- Main's `su2-gauge-aligned-response-20261108/gates/original-source-four-response-check.md`, lines 24–30, refers to a mixed covariance on a cube. The lane's `GOAL.md` specifies a hidden posterior after a normalized kernel transition. The target search found no two-end Wilson decay estimate. The helicity hits concern spin ice.
- On PRs 10114 and 10133, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, (11), lower-bounds the **one-step** vacuum correlation of a centered simple loop, at every positive coupling. Its (15) bounds a Gibbs covariance by the two oscillation vectors contracted with $(I-C)^{-1}/4$ when the one-link influence matrix has a symmetric majorant of row sum less than one. `MASS_GAP_CONSTRUCTION_ASTRA.md`, line 425, records the four-dimensional majorant $18\beta$. Main's `research/mass-gap/library/gap-mid-max.md`, §10, proves the corresponding small-coupling comparison. I use it for the pinned strong-coupling twin below. [Comparison proof and corrections](gap-dob-astra.md)
- In the lane, row 929 already computes the free-photon transverse Mehler kernel and the compact harmonic rotor. Row 1556(v) already constructs the cut action, identifies its pinned covariance, and gives the four-corner and spectator arguments. Registry R10 concerns a one-step $Q2$ posterior, R11 thermal transport and R12 the carry from bare coupling. I found no registry owner of the two-end estimate. The brief explicitly pairs rows 1565 and 1566. [Free-photon model, §3.1](gap-seam-max.md) · [Row 1556(v)](gap-mech-direction4-check-astra62.md) · [Registry](open-registry.md) · [November 8 search](prior/repo-search-2026-11-08.md)
- At the supplied Sussman–Alpoge revision `31a47c543775`, the outline, lines 1670–1686 and 1714–1729, compares free exact-form curvature to its continuum kernel on a periodic torus. CA-II, lines 69516–69541, gives $d_1\Delta_1^+d_1^*$ for that covariance. CA-III, lines 108223–108268, deduces scalar reflected decay given crossing-cumulant decay or a simple vacuum and positive gap. None supplies a conditioned Wilson slab estimate. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex. The Balaban estimates quoted in the lane concern regular backgrounds and their propagators. [Outline index, chunk 02](sa-index/chunk-02.md) · [CA index](sa-index/ca-full/index.tsv) · [Balaban source record](lit-balaban.md)

- For replica exchange, rows 1099, 1118 and 1131 already cancel disconnected swaps and mark the excess above a paired factor's minimum over partial exchanges. For the abelian flux test, main's `PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md` gives a positive expansion with damped coclosed currents, following Fröhlich and Spencer. Row 786 applies its coexact covariance estimate to continuous compact links. I reuse the expansion below. The five-ref searches for odd-period cosets, Villain flux sectors, bilateral moments and shifted-Gaussian mixtures located no matching flux-parity lower bound or Wilson transfer of that bound. [Exchange construction](gap-conv-in-law-astra.md) · [Periodic Villain application](gap-tu-retry.md)

## Initial plan

1. Check the target inventory, row 1556, the outline index and the specified repository refs for overlap.
2. Test the mixed boundary derivative in the Coulomb and massive comparison models.
3. Attack the remaining finite-band Wilson estimate, recording each distinct argument and its last justified step.
4. Derive the four-corner consequence and identify what the release seed still requires.

## Comparison tests

Write $D$ for spacetime dimension, $m=D-1$ for spatial dimension and $\Sigma$ for the whole cut on a spatial slice. Thus $|\Sigma|=n^{D-2}$ and $n/v\in\{512,1024\}$. Write $\mathcal B_D$ for the left side of row 1556(v), with the same power $2+\epsilon$ being tested in each dimension. Failure at $s=t=0,\ z=0$ suffices. All proof arguments below are by hand.

| Model | What happens to this observable |
|---|---|
| Weak 4D compact $U(1)$ | **Fails for the interacting Wilson cosine action** at all sufficiently large fixed $\beta_W$, and for Villain at $\beta\ge2000$. A volume-independent lower bound on the odd electric-flux probability gives $\mathcal B_4\ge c/n^2$ at $s=t=z=0$, equation (7). In the free photon the absolute row is of order $v^{-2}$ even after discarding the harmonic mode. |
| Weak 5D $SU(2)$ | With a full three-dimensional cut, the same $v^{-2-\epsilon}$ is **false for free gauge bosons** with the random curvature axes in a common colour frame. Both the presence of a Coulomb phase and the transfer of this calculation to independently gauge-averaged interacting ends are additional issues. The Wilson verdict is open. The four-corner multiplier in five dimensions is $n^3$, so this literal exponent would give $O(v^{1-\epsilon})$ for the log twist ratio. |
| Strong 4D $SU(2)$ | **Holds** uniformly in the pins, all rotations and twists for $0\le\beta\le\beta_s<1/18$. There is exponential decay with the slab thickness. The proof below uses the established one-link comparison. |
| 3D compact $U(1)$ | On a two-dimensional spatial slice there is no $23$ plaquette. Use the fixed abelian generator $i$, which gives the same centre half-turn, or an untouched plaquette sign. **Holds** for Wilson and Villain at sufficiently strong coupling. Göpfert–Mack's Villain confinement theorem does not by itself estimate these conditional, rotated-end derivatives at arbitrary coupling. Their decay there remains open in this argument. |

In 4D $U(1)$ the specified axis is $i\,\mathrm{sgn}(\sin Q_x)$ in angle notation, away from a null set. At zero rotation its sign disappears inside the absolute value. This permits a test with ordinary link derivatives even though rotating the entire random-sign cut at a general angle is different from a uniform abelian translation. The five-dimensional test keeps the same untouched $23$ plaquette. [Weak-coupling source and boundary conditions](prior/gap-lit-u1.md) · [Twin-test corrections, §(iv)](gap-mech-direction4-check-astra62.md)


### Photon test at a nonzero momentum (proved for the free models)

Use the positive $1$-link coordinates on the two ends. For $k\in(2\pi/n)\mathbb Z_n^m$, put $h_j=e^{ik_j}-1$, $\kappa=\sum_j|h_j|^2$ and $\cosh\omega=1+\kappa/2$. For $k\ne0$, Gauss projection leaves the transverse subspace $h^\perp$. In each transverse polarization the cross coefficient in $\log K_v$ is $\beta\sinh\omega/\sinh(v\omega)$ by row 929, Lemma M. This also follows by solving the tridiagonal Dirichlet equation $q_{j+1}-2\cosh(\omega)q_j+q_{j-1}=0$ between $q_0,q_v$. In units of one link angle, the spatial kernel for the same link direction at the two ends is therefore
\[
 M(r)=n^{-m}\sum_{k\ne0}e^{ik\cdot r}
       \beta\,\frac{\sinh\omega(k)}{\sinh(v\omega(k))}
       \left(1-\frac{|h_1|^2}{\kappa}\right).
\]
This is an end-to-end *log-kernel Hessian*. A bulk curvature two-point function would have different boundary conditions.

On $\Sigma$ fix $x_1=y_1=0$. Take the Fourier coefficient in $y_\parallel$ at $q=(2\pi/n,0,\ldots,0)$ along direction 2. Up to a unit phase it is $1/n$ times the sum of the displayed nonnegative multipliers over $k_1$, with $k_\parallel=q$. At $k_1=0$ the transverse factor is one and $\omega=2\operatorname{arsinh}(\sin(\pi/n))\le2\pi/n$. Since $v\omega\le1$, $\sinh(v\omega)\le v\omega\cosh 1$ and $\sinh\omega\ge\omega$. Thus at either aspect,
\[
 \sum_{y\in\Sigma}|M(x-y)+h_0|
 \ \ge\ \frac{\beta}{nv\cosh 1}
 \ \ge\ \frac{\beta}{1024\cosh 1}\,v^{-2}.                 \tag{1}
\]
Here $h_0$ can be any scalar independent of $y$, even a function of both boundary configurations. In particular the compact harmonic rotor contributes precisely such a term. This avoids a choice about removing the zero mode. In the one-colour model at $s=t=0$ the two plaquette signs have modulus one and drop out pair by pair.

For the matching power in (1), $\omega\ge c_m|j|/n$ at grid point $k=2\pi j/n$ in the principal zone. This follows from $\sin(\pi |j_i|/n)\ge 2|j_i|/n$ and the positive minimum of $\operatorname{arsinh}(s)/s$ on $[0,\sqrt m]$. Bounded $\omega$ and $a/\sinh a\le C e^{-a/2}$ for $a\ge0$ give $\sinh\omega/\sinh(v\omega)\le (C_m/v)e^{-c_m v|j|/(2n)}$. The grid sum is bounded by a convergent exponential sum on $\mathbb Z^m$ since $v/n\ge1/1024$. Hence $\sum_{y\in\Sigma}|M(x-y)|\le C_m\beta/(nv)$. In the 4D compact rotor, $\phi_1=n\overline A_1$ changes by $n^{1-m}$ per link. Its periodized Gaussian has precision $\beta n/v$ for $m=3$. At fixed $\beta$, each of the two aspects gives a strictly positive smooth function on the circle with bounded log second derivative. Its contribution to the row is at most $C(\beta)n^{1-m}=C(\beta)n^{-2}$. Thus the rough $v^{-2}$ count is sharp in the free-photon test, including the absolute value. [Mode and rotor normalizations](gap-seam-max.md)

For the 5D linearized test take three independent photons in a common colour frame with the spatial zero modes removed. At $s=t=z=0$, the sewn Gaussian curvature vectors $F_{23}(x),F_{23}(y)$ are nondegenerate at each site. After normalizing their individual variances, their joint law is $(G,\rho G+\sqrt{1-\rho^2}\,G')$ for independent standard three-component Gaussians. The expected absolute scalar product of the two *unit* vectors has a strictly positive minimum for $-1\le\rho\le1$. It is continuous by bounded convergence, positive on the interior by the positive joint density, and equals one at either endpoint. With the linearized curvature axes the mixed derivative is $M(x-y)\widehat F_{23}(x)\cdot\widehat F_{23}(y)$. The absolute row is bounded below by this minimum times (1) with $h_0=0$. This proves the failure at the photon level even with fluctuating axes. A weak-coupling expansion at fixed volume would require an error uniform as $v,n\to\infty$ to transfer this result. In particular, independent end gauge averaging and the nonabelian holonomies are part of that problem.


## The Wilson estimate and three attempts

For fixed ends $X,Y$, let $\nu_{X,Y}$ be the positive Wilson law of the slab interior. The spatial half-weights on the two boundary slices contribute addends depending on only one end to $\log K_v$. After removing these addends, the derivative at $x$ comes from the **single temporal plaquette** incident to that boundary $1$-link. Denote its log-weight derivative by $F_x$, and the corresponding far derivative by $G_y$. With normalized half-trace, $|F_x|,|G_y|\le\beta$. The frozen axis is part of the pin. In unfixed variables each score depends on at most three free links. The closest support times are in $[0,1]$ and $[v-1,v]$. Finite differentiation gives row 1556(v)'s identity
\[
 H_{xy}(X,Y):=D_x^{(1)}D_y^{(2)}\log K_v(X,Y)
       =\operatorname{Cov}_{\nu_{X,Y}}(F_x,G_y).
\]
The **one band lemma** at issue is
\[
 \max_{z}\sup_{s,t,x}\sum_{y\in\Sigma}
 \int |H_{xy}(R_sB,R_t C_z A)|\,d\mu_{z,2v}(A,B)
 \le C v^{-2-\epsilon}
 \quad\text{at every }\beta\in[2,3],\quad n/v=512\text{ or }1024.       \tag{B}
\]
Here and below the divisibility and $v\ge3$ are as in the question. The end distribution inside the integral is exactly as displayed.

### 1. Conditional single-link comparison

**Small-coupling result.** In $D$ dimensions there are at most $6(D-1)$ plaquette neighbours per free link. Freezing links only deletes variables. With the Wilson cosine or half-trace action, changing one shared neighbour changes the log density at a free link by a function of oscillation at most $4\beta$. The total-variation change is at most one quarter of that oscillation, by interpolation of the normalized densities. Thus a symmetric comparison matrix $C$ with row sum at most $q=6(D-1)\beta$ works. Dobrushin's covariance inequality quoted above gives
\[
 |\operatorname{Cov}(F_x,G_y)|
 \le \tfrac14\sum_{ij}\delta_i F_x [(I-C)^{-1}]_{ij}\delta_j G_y
 \le \frac{3\beta^2 q^{\,v-2}}{1-q},\qquad q<1 .
\]
Here $\delta_i$ is single-link oscillation. Each of the at most three initial oscillations is at most $2\beta$ and the far oscillation vector has supremum at most $2\beta$. Adjacent links on a plaquette have time midpoints at distance at most one. Hence every contributing power of $C$ has degree at least $v-2$. This argument works before the end average, including for any rotated pins. Multiplication by $n^{D-2}\le(1024v)^{D-2}$ leaves exponential decay up to a polynomial. This proves the strong-coupling entries in the table, uniformly on closed subintervals of $q<1$, with zero response at $\beta=0$. For 3D Wilson the explicit interval is $\beta<1/12$. The lane's sharper small-coupling chord-metric estimates use different comparison coefficients. [Total-variation comparison](gap-dob-astra.md) · [Chord-metric method, §4](gap-vmf-lip.md)

For the 3D Villain weight $\phi_\beta$ defined below, its Fourier series gives $\phi_\beta\to1$ uniformly as $\beta\downarrow0$ and a bounded log derivative at each fixed positive $\beta$. A single shared plaquette now gives a variation coefficient at most $\tfrac12\operatorname{osc}\log\phi_\beta$. The row sum is less than one for sufficiently small $\beta$. The same distance argument applies with $\|(\log\phi_\beta)'\|_\infty$ as the score bound.

**Attempt at the band.** The actual unweighted worst-case single-link variation matrix already has a bulk row of sum $>1$ at every $\beta\ge2$ on sufficiently thick slabs. Fix an interior link and one of its eighteen neighbours. The six staples have disjoint sets of other links. Prescribe the five staples outside the shared face to have sum zero as four-vectors, using five equally spaced unit quaternions on a circle. Make the sixth staple $+1$ or $-1$ by changing just the designated neighbour. The remaining two edges of that staple may be set to one. The two one-link conditional laws have Haar densities proportional to $e^{\pm\beta h}$ with $h=\operatorname{Re}U$. Their total-variation distance is $\mathbb E_\beta\operatorname{sgn}h$, where $\mathbb E_\beta$ uses the plus sign. It increases with $\beta$ because its derivative is $\operatorname{Cov}_\beta(\operatorname{sgn}h,h)\ge0$. At $\beta=2$ it is
\[
 \frac{\mathbb E_{\rm Haar}\sinh(2|h|)}{\mathbb E_{\rm Haar}\cosh(2h)}
 \ \ge\ \frac{2\mathbb E_{\rm Haar}h^2}{\cosh 2}
 \ =\ \frac1{2\cosh 2} \ >\ \frac1{10}.
\]
The equality uses rotational symmetry on the unit three-sphere. Each of the eighteen coefficients takes its own supremum. Their sum therefore exceeds $18/10$. This supplies an obstruction to this particular comparison method on the actual Wilson specification. The witnesses are allowed conditioning configurations. They give no lower bound on a typical pinned covariance.


### 2. Replica exchange with the temporal coupling kept in the band

**An anisotropic result.** Give temporal plaquettes strength $2\le b_t\le3$ and spatial plaquettes strength $\kappa\ge0$. In this paragraph $b_t$ denotes a plaquette coupling, unrelated to the release block factor. Define
\[
 p=1-e^{-12},\qquad a=-\tfrac12\log p,\qquad
 L=\frac{1+\sqrt p}{1-\sqrt p},\qquad J=6(m-1),\qquad
 \kappa_*=-\tfrac14\log\!\left(1-\frac1{2JL}\right)>0 .
\]
For $0\le\kappa\le\kappa_*$ the whole pinned row is bounded **at every pair of ends** by $4b_t^2 L n^{m-1}e^{-a(v-2)}$. This keeps a positive spatial interaction. The electric-only transfer at $\kappa=0$ and the replica exchange for local Gibbs factors are prior work. [Electric reference, §1](gap-crux-skeleton-check-astra.md) · [Exchange of cell variables, §4](gap-conv-in-law-astra.md) · [Bare Wilson plaquette marking, §3](gap-council-prob-astra.md)

To see which variables an exchange can join, use temporal gauge on this *open* slab. Starting with the identity gauge on the lower end, take cumulative products of the temporal links at each spatial vertex. Changing the spatial links on each interior slice by this gauge preserves their Haar measure. Changing the temporal links to their cumulative products is triangular and Haar preserving. Only the terminal product $g$ remains in the action. Thus the kernel integrates the spatial links $U_{j,e}$, $1\le j\le v-1$, and the vertex variables $g$ with product Haar, between $X$ and $Y^g$. The interior temporal factor couples $(j,e)$ only to $(j+1,e)$. A spatial factor couples the four links of a plaquette in a single slice. The terminal gauge variables occur only at the top. In these coordinates $F_x$ reads the single vertex $(1,e_x)$ of this graph, and $G_y$ reads $(v-1,e_y)$ and the two terminal gauge variables at the ends of $e_y$. Spatial boundary derivatives are constants under the pinned law.

Take two independent copies with these same pins. For each factor let $W$ be the product of its two weights and $w_*$ the minimum of that product over all exchanges of its incident variable pairs. Given the copies, mark the factor independently with probability $1-w_*/W$ and join its incident variables when marked. In the joint density a closed factor is $w_*$ and an open factor is $W-w_*$. Swapping a whole marked component preserves the joint measure. This is the local exchange cancellation used by Redner, Machta and Chayes and, for gauge covariance, Adhikari and Cao, in the forms credited in the lane. On the event that the component at $(1,e_x)$ misses level $v-1$, its swap changes the sign of $F_x-F_x'$ and leaves $G_y-G_y'$ fixed. Since $2\operatorname{Cov}(F_x,G_y)=\mathbb E[(F_x-F_x')(G_y-G_y')]$, this gives
\[
 |H_{xy}|\le 2b_t^2\,\mathbb P\{(1,e_x)\text{ reaches level }v-1\}.       \tag{2}
\]
The top gauge integral stays inside both replicas. It creates no shortcut to that level from below it.

A factor of strength $b$ has $e^{-2b}\le w_*\le W\le e^{2b}$. Along any fixed path of distinct factors the conditional probability that all are marked is at most the product of $p$ per temporal step and $p_s=1-e^{-4\kappa}$ per spatial step. This uses conditional independence only. Stop a simple incidence path on first reaching level $v-1$. A maximal vertical run before that time has one direction and some length $\ell$. Counting the two signs for $\ell>0$, its total weight with the extra factor $e^{a\ell}$ is at most $1+2\sum_{\ell\ge1}(p e^a)^\ell=L$. A spatial step has at most $2(m-1)$ incident plaquette choices and three other links to exit to. With $h$ spatial steps there are $h+1$ vertical runs, possibly empty. Summing the weights of simple paths is bounded by $L(Jp_sL)^h$. Overcounting by unrestricted run choices in this last sum is harmless, since the probability bound was applied to simple paths. Total vertical length is at least $v-2$, so
\[
 \mathbb P\{(1,e_x)\text{ reaches level }v-1\}
 \le e^{-a(v-2)}\,\frac{L}{1-Jp_sL}
 \quad\text{if }Jp_sL<1.
\]
At $\kappa\le\kappa_*$ the denominator is at least $1/2$. Summing (2) proves the assertion, also for the rotated pins and their sewn average.

**Where this stops at isotropy.** At $\kappa=b_t\ge2$, $J(1-e^{-4\kappa})L>1$. The convergent path sum is lost. Bounding the actual jointly marked paths, or retaining the signed score differences on their crossing event, would use information about the interacting pins and interior that the deterministic bounds discarded. The estimate just proved also works for abelian Wilson weights and in five dimensions at sufficiently small spatial coupling. It establishes no selectivity for the isotropic band.


### 3. A spectral attempt to refute (B) on its periodic, unrotated member

**An exact necessary test.** Set $s=t=0$ and $z=0$. For real coefficients $c_x$ put $D_c=\sum_{x\in\Sigma}c_xD_x$, and write $S=T^v$ for the gauge-projected transfer power, $K$ for its real symmetric kernel. The periodic sewing measure is $K(X,Y)^2\,dX\,dY/Z^0(2v)$. The signed response satisfies
\[
 \int K^2 D_c^{(1)}D_c^{(2)}\log K\,dX\,dY
   =2\|T^{v/2}D_c T^{v/2}\|_{\rm HS}^2 .                         \tag{3}
\]
Indeed, integration by parts in $X$ gives $-2\int (D_c^{(1)}K)(D_c^{(2)}K)$. Conditional Haar on the moved links makes $D_c$ skew-symmetric because its axes are independent of all of them. By symmetry of $K$ the integral without the factor $-2$ is $\operatorname{Tr}((D_cS)^2)$. In a real transfer eigenbasis with positive eigenvalues $\lambda_i$, its negative is $\sum_{ij}\lambda_i^v\lambda_j^v|\langle i,D_cj\rangle|^2$. The differentiated kernel is bounded at fixed volume, so $D_cS$ is Hilbert–Schmidt and the trace product is absolutely summable. Zero eigenvalues give no trace term. Positive-eigenvalue eigenfunctions are smooth by the integral equation. The square-root sandwich in (3) is equivalently defined by these Hilbert–Schmidt matrix elements. This proof uses derivatives only along the cut, also for the measurable normalized axes.

By symmetry, the absolute row and column sums under this sewing agree after interchanging their labels. Applying $2|c_xc_y|\le c_x^2+c_y^2$ to (B) would give
\[
 \frac{2}{Z^0(2v)}\|T^{v/2}D_c T^{v/2}\|_{\rm HS}^2
       \le C v^{-2-\epsilon}\sum_{x\in\Sigma}c_x^2.               \tag{4}
\]
In particular a lower bound $c_0 v^{-2}\|c\|_2^2$ on the left along one unbounded admissible sequence at a fixed band coupling would refute (B). For $SU(2)$ the half-turn commutes with $T$, but the full rotation varies transverse plaquette energies at intermediate angles. One cannot diagonalize $T$ in charges of this circle on that basis. In the positive real vacuum alone $\langle 0,D_c0\rangle=0$ by skew-symmetry. A one-step loop witness neither bounds these weighted off-diagonal matrix elements from below at time $v$ nor gives the absolute row from above.

An actual $SU(2)$ odd-sector trial uses the trace $W$ of a straight winding spatial loop, normalized by $1/2$. The positive simple vacuum $\psi_0$ is centre-even, so $W\psi_0$ is odd under $C_1$ and has norm at most one. Equation (11) of the one-step loop witness in the repo search gives $\lambda_-/\lambda_0\ge\eta_n$ by the Rayleigh quotient, where $\lambda_-$ is the largest $C_1$-odd eigenvalue. With at most $4n$ spatial plaquettes touching the $n$ distinct loop links, it allows
\[
 \eta_n=\frac{e^{-20\beta n}}{16(1+\tfrac14 r_f^{-n})},
 \qquad r_f=I_2(\beta)/I_1(\beta).
\]
Thus the odd probability at period $2v$ is bounded below by $\eta_n^{2v}/\operatorname{Tr}((T/\lambda_0)^{2v})$. Even replacing the denominator by its smallest possible value of one would leave this expression exponentially small in $nv$. A positive odd probability at each finite size does not give the order-one probability that would refute (B) by the twist ratio.

For $U(1)$ one can take ordinary angle derivatives in this test since their absolute values equal the random-sign ones at $s=t=0$. The simultaneous *constant* rotation of the cut multiplies by a flat abelian link cochain and commutes with $T$. For $c_x=1$, $D_c=iQ$ is then the conserved integer electric charge. Equation (3) gives the exact lower bound
\[
 \mathcal B_D\ \ge\ \frac{2}{n^{m-1}}\,
       \frac{\operatorname{Tr}(Q^2 T^{2v})}{\operatorname{Tr}T^{2v}}.   \tag{5}
\]
The trace is over the full physical slice before centre projection. In four dimensions any positive $\limsup$ of this charge variance would rule out (B) at that coupling. The periodic Villain covariance bound in row 786 controls *coexact* two-forms. Its lower side vanishes on the harmonic flux tested by (5). [Periodic Villain estimate, §1](gap-tu-retry.md) · [Check of its projection and boundary conditions](gap-tu-check-opus.md)


#### A flux lower bound for the interacting compact Villain test

**Result.** For the 4D compact $U(1)$ **Villain** action at each $\beta\ge2000$, on the actual $n^3\times 2v$ tori, there is an $\eta_\beta>0$, independent of $n,v$, such that $\Pr(Q\text{ odd})\ge\eta_\beta$. In particular $\mathcal B_4\ge 2\eta_\beta/n^2$ by (5). This disproves the analogue of (B) for this interacting Coulomb model. The extra step beyond row 786 is to keep an *integer* shift of flux through the positive current expansion, reducing its phase modulo $2\pi$ before estimating the cost.

Use the Villain weight $\phi_\beta(\theta)=\sum_{j\in\mathbb Z}e^{-j^2/(2\beta)}e^{ij\theta}$. Integration over link angles gives the centered discrete Gaussian on integer two-forms $N$ satisfying $\delta N=0$. A uniform cut translation through angle $\theta$ at the time seam contributes $e^{\pm i\theta q}$, where $q$ is the sum of $N_{01}$ over the transverse $23$-section there. Thus $q$ has the thermal charge distribution, up to its immaterial overall sign. On the translated dual torus $F=*N$ is a closed integer two-form with $23$ period $q$. Closure makes that period independent of the other two coordinates. Put $w=2v$, $V=n^3 w$ and $R=n/w\in\{256,512\}$.

Let $S$ have $23$ component one at $x_2=x_3=0$ for all $x_0,x_1$, zero elsewhere, and no other components. It is closed with period one. Its harmonic projection $h$ has the single constant component $1/n^2$, so $\|h\|^2=V/n^4$. There is a real one-form $b$ with $db=S-h$, since a closed periodic two-form of zero harmonic projection is exact (invert the lattice Laplacian on each nonzero Fourier mode). Let $K_{\mathbb Z}=d\mathbb Z^{E}$ on this dual torus. For a coset $\mathcal D=F_0+K_{\mathbb Z}$ in the closed integer forms, write $F_0=h_0+du$ with $h_0$ harmonic. Its weight factors as
\[
 Z_{\mathcal D}=e^{-\|h_0\|^2/(2\beta)}\,\Theta(u),\qquad
 \Theta(u)=\sum_{F\in K_{\mathbb Z}+du} e^{-\|F\|^2/(2\beta)}.
\]
It suffices to bound $\sqrt{\Theta(u+b)\Theta(u-b)}/\Theta(u)$ uniformly below. Directly differentiating the source $u+tb$ would charge the whole thin sheet.

**Input from the repository.** Use equations (3.1), (4.1) and (5.1)–(5.3) of the periodic finite-clock Villain note (PV). They give the current expansion of this Gaussian theta function on integer curls. At each finite Fejér order, $\Theta(u)$ up to a source-independent normalizer is approximated by a positive mixture of integrals of products
\[
 \prod_\rho \big[1+z_\rho\cos(\xi_\rho+\langle\rho,u\rangle)\big].
\]
The phases $\xi_\rho$ include the **joint** harmonic integration. Within an ensemble the surviving currents $\rho$ are coclosed, supported on disjoint sets of edges, with entries in $2\pi\mathbb Z$. A support of size $r$ is connected at distance one, $\|\rho\|^2\ge4\pi^2r$, and
\[
 0<z_\rho\le e^{-A\|\rho\|^2}<\tfrac12,\qquad
 A=\beta/384-(107\log3+\log4)/(4\pi^2)>0 .
\]
For the rectangular torus the Poisson and subgroup identities use the same cochain lattice. In (4.1) the disjoint-support mergers and the bound of 107 lifted neighbouring edges are local. All four periods are even, so the 32 colours by orientation and transverse parities and the diagonal $d^*d(e,e)=6$ in (5.1) apply verbatim. Joint integration keeps winding currents. These are all the geometric requirements through (5.3). At each fixed torus the Fejér approximation converges by Gaussian Fourier domination. [PV, §§3–7](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md#L160) · [Continuous compact model in row 786, §1.2](gap-tu-retry.md)

For each current choose $d_\rho\in[-\pi,\pi]$ congruent to $\langle\rho,b\rangle$ modulo $2\pi$. Interpolate each positive factor by adding $t d_\rho$ to its phase, $-1\le t\le1$. At $t=0,\pm1$ this gives exactly the Fejér expressions for $u,u\pm b$. Intermediate $t$ need only define a positive integrand. By (6.1) the second derivative of its logarithm is bounded below by $-\sum_\rho z_\rho d_\rho^2/(1-z_\rho)$. This sum is uniformly bounded, as follows.

- For $r<w/8$ the distance-one connected support lifts to a box of side at most $3r$. Adding at most $r-1$ joining edges produces a graph of fewer than $2r$ edges, too short for a nonzero winding. PV's coordinate-ordered filling in §6 gives a two-chain $B_\rho$ with $\delta B_\rho=\rho$, coefficients in $2\pi\mathbb Z$, and $\|B_\rho\|_1\le9r^{3/2}\|\rho\|$. The construction sums at most $3(3r)$ unit plaquettes per occupied edge against its integer-multiple coefficient. Consequently $\langle\rho,b\rangle=\langle B_\rho,S-h\rangle\equiv-\langle B_\rho,h\rangle\pmod{2\pi}$. Thus $d_\rho^2\le81r^3\|\rho\|^2/n^4$.
- For $r\ge w/8$, including winding supports, use $|d_\rho|\le\pi$. At any $r$ there are at most $4V/r$ disjoint supports of that size. In the large range $V=R^3w^4\le512^3(8r)^4$.

For example a uniform bound on the sum is
\[
 M_\beta=\frac{1296}{Ae}\sum_{r\ge1} r^2 e^{-2\pi^2 A r}
       +8\pi^2\,512^3\,8^4\sum_{r\ge1} r^3 e^{-4\pi^2 A r}<\infty .
\]
The first term uses $V/n^4\le1$ and $t e^{-At/2}\le2/(Ae)$. The second uses $z_\rho/(1-z_\rho)\le 2e^{-A\|\rho\|^2}$. Both bounds apply before averaging the phases and ensembles. The logarithm of a positive integral inherits the lower second-derivative bound by addition of a nonnegative variance. Integrate against $1-|t|$ on $[-1,1]$ and take the finite-volume Fejér limit. This yields $\sqrt{\Theta(u+b)\Theta(u-b)}\ge e^{-M_\beta/2}\Theta(u)$ for **every** offset $u$.

The geometric mean of the two shifted harmonic factors costs $e^{-\|h\|^2/(2\beta)}$. Hence
\[
 \tfrac12(Z_{\mathcal D+S}+Z_{\mathcal D-S})
 \ \ge\ \sqrt{Z_{\mathcal D+S}Z_{\mathcal D-S}}
 \ \ge\ d_\beta Z_{\mathcal D},\qquad
 d_\beta=\exp[-1/(2\beta)-M_\beta/2]>0.
\]
Each of $\mathcal D\mapsto\mathcal D+S$ and $\mathcal D\mapsto\mathcal D-S$ is a bijection from even-period cosets to odd-period cosets. Summation gives $Z_{\rm odd}\ge d_\beta Z_{\rm even}$, proving the asserted lower bound with $\eta_\beta=d_\beta/(1+d_\beta)$. Equivalently the half-turn twisted-to-periodic ratio is at most $1-2\eta_\beta$ at both aspects. This proof uses the integer-Gaussian character weights throughout.


#### Transferring the flux bound to the Wilson cosine weight

**Offset uniformity.** The Villain proof just given works, with the same $d_\beta$, if each plaquette has an arbitrary real offset $y_p$ in the integer Gaussian weight $e^{-\|F-y\|^2/(2\beta)}$. In a coset $\mathcal D$ split $F_0-y=du+h_\perp$ by orthogonal projection onto real exact forms. The perpendicular term can now contain a coexact part. Passing to $\mathcal D\pm S$ sends it to $h_\perp\pm h$ and the exact part to $d(u\pm b)$. Taking the geometric mean still costs precisely $e^{-\|h\|^2/(2\beta)}$. The theta estimate was uniform in $u$. In particular, $Z_{\rm odd}(y)\ge d_\beta Z_{\rm even}(y)$ holds *before* any averaging over the offsets.

**A positive mixture lemma.** Fix $t>0$. There is a $\delta(t)>0$ such that a positive summable sequence $w_j$, $j\in\mathbb Z$, with
\[
 -\delta(t)\le\log w_{j-1}-2\log w_j+\log w_{j+1}\le0
 \quad\text{for every }j
\]
admits a positive finite measure $\lambda$ on $\mathbb R$ with
\[
     w_j=\int_{\mathbb R} e^{-t(j-y)^2/2}\,d\lambda(y)
     \quad (j\in\mathbb Z).                                      \tag{6}
\]
Real centres in (6) are essential to this argument.

Put $m_j=e^{t j^2/2}w_j$. For $k=0,1$ normalize the Hankel matrix $(m_{i+j+k})_{i,j\in\mathbb Z}$ by dividing every entry by the geometric mean of its two diagonal entries. The resulting entry with $r=|i-j|$ lies in
\[
  [e^{-tr^2/2},\,e^{-(t-\delta)r^2/2}].
\]
Indeed the logarithm of the additional $w$ ratio is the midpoint excess of $\log w$ over the two endpoints at distance $r$. Summing the second differences with triangular weights of total mass $r^2$ bounds that excess between zero and $\delta r^2/2$. The matrix $(e^{-t(i-j)^2/2})$ has an $\ell^2$ lower bound $\gamma_t>0$. Its Fourier multiplier by Poisson summation is $\sqrt{2\pi/t}\sum_{\ell\in\mathbb Z}\exp[-(\theta-2\pi\ell)^2/(2t)]$, a strictly positive continuous function on the circle. Choose $0<\delta(t)<t/2$ small enough that
\[
 \sum_{r\in\mathbb Z}
   \big(e^{-(t-\delta(t))r^2/2}-e^{-tr^2/2}\big)<\gamma_t/2 .
\]
Dominated convergence ensures such a choice. This row and column sum bounds the operator norm of the perturbation. Both Hankel forms are strictly positive on finitely supported vectors, by undoing the positive diagonal normalization on their supports.

Both forms are needed for the **bilateral** moments. On Laurent polynomials in a real indeterminate $x$, take the functional $\ell(x^j)=m_j$. The $k=0$ form defines the inner product $\ell(\bar f g)$, and the $k=1$ form makes multiplication by $x$ a nonnegative densely defined symmetric operator in its Hilbert completion. Take its nonnegative self-adjoint Friedrichs extension $A$. Its range contains every Laurent polynomial, since $x(x^{-1}f)=f$ there. Self-adjointness therefore gives $\ker A=0$. On the constant vector, $A^j1=x^j$ for every integer $j$. For negative powers apply injectivity to $A(x^{j-1})=x^j$. The spectral measure of $A$ at $1$ is thus a finite positive measure on $(0,\infty)$ with moments $m_j$ for all $j\in\mathbb Z$. Push it forward by $y=t^{-1}\log x$ and multiply the result by $e^{t y^2/2}$. Completing the square gives (6). The resulting $\lambda$ is finite since $\sum_j e^{-t(j-y)^2/2}\ge e^{-t/8}$ and $\sum_j w_j<\infty$.


**Wilson application (sufficiently weak coupling).** Set $w_j=I_{|j|}(\beta_W)$, the Fourier coefficients of $e^{\beta_W\cos\theta}$, and $b_0=\beta_W/2$. These coefficients are positive, even and summable. Their log second differences tend uniformly to zero from below as $\beta_W\to\infty$. Here is a proof covering the unbounded character index.

First, $w$ is the convolution of $s_j=b_0^j/j!$ on $j\ge0$ (zero elsewhere) with its reflection. The Toeplitz matrix of $s$ has nonnegative ordered $2\times2$ minors by the decreasing successive ratio $b_0/j$ and its interval support. The reflected sequence has the same minor property by transposition. The $2\times2$ Cauchy–Binet formula, first on finite intermediate index sets and then by convergence of the entries, passes it to the convolution. In particular $w_j^2\ge w_{j-1}w_{j+1}$. For $j\ge0$,
\[
 j!\,b_0^{-j} w_j=\sum_{r\ge0}\frac{b_0^{2r}}{r!}
                       \frac{j!}{(j+r)!}
\]
is log-convex in $j$. Each term has that property by its product of reciprocal linear factors, and Cauchy–Schwarz preserves it under summation. Thus $w_{j-1}w_{j+1}/w_j^2\ge j/(j+1)$ at every $j\ge1$, uniformly in $\beta_W$. For each fixed $j$, $w_j/w_0\to1$ because the normalized measure $e^{\beta_W\cos\theta}d\theta$ concentrates at $0$ and its $j$th cosine equals one there. To get the claimed uniform second-difference bound, first use $j/(j+1)$ outside a fixed finite interval, then take $\beta_W$ large on that interval.

Choose $t=1/2000$ in (6), then choose a finite $\beta_*$ so the Wilson coefficients meet $\delta(t)$ for every $\beta_W\ge\beta_*$. Expand the Wilson plaquette weights in characters and integrate the compact link angles exactly as for Villain. The closed dual integer forms now have weight $\prod_p w_{F_p}$. By (6) this is a **positive** integral of precisely the shifted Gaussian products at Villain coupling $2000$. The signed Hodge orientation only relabels or reverses the real centres. Tonelli on each parity class and the offset-uniform inequality give
\[
 \Pr_{\beta_W}(Q\ {\rm odd})\ge\eta_{2000},\qquad
 \mathcal B_4(\beta_W,n,v)\ \ge\ \frac{2\eta_{2000}}{n^2}
       \ \ge\ \frac{2\eta_{2000}}{1024^2}\,v^{-2}
 \quad(\beta_W\ge\beta_*).                                      \tag{7}
\]
This gives an explicit estimate in the opposite direction for the actual **compact Wilson comparison model**, already at $s=t=z=0$. The weak-coupling threshold is existential and can be very large. The argument does not locate the phase boundary or give an upper bound of order $v^{-2}$ for this interacting law. The proof uses the positive current expansion of Fröhlich and Spencer in the repository’s periodic formulation, together with the offset and moment arguments above. Guth’s Villain loop estimate is earlier evidence for the Coulomb regime.


The harmonic cost also distinguishes the 3D abelian twin in this test. The primal $01$ component of a unit sheet averages to $n^{-(D-2)}$, with squared norm $2v\,n^{3-D}$. At $D=3$ this is $2v$ and the geometric-mean harmonic factor alone loses $e^{-v/\beta}$. At $D=4$ it is bounded at fixed aspect. For $SU(2)$ the character expansion has nonabelian intertwiners and the plaquette-axis circle has only a discrete centre symmetry at its half-turn. Neither the closed-integer-form law nor the conserved charge used in (5) is available for that circle in four or five dimensions. The free 5D test in (1) identifies the borderline power. I cannot establish this failure for the 5D interacting law.

## What (B) would give

Use the centre twists of ’t Hooft and the four-corner identity of row 1556(v). For a pair of ends $X,Y$ outside the central-plaquette null set, the four log-kernel values at $(0,0),(\pi,0),(0,\pi),(\pi,\pi)$ are $f,g,g,f$, with $f=\log K_v(X,Y)$ and $g=\log K_v(X,C_1Y)$. The frozen axes make the mixed angle derivative the sum of all $H_{xy}$ along the two orbits. Integrating over the square gives $2(f-g)$. Substituting $X=B,\ Y=C_zA$ and using (B) gives
\[
 \mathbb E_z|\ell_z|\le h_v:=\tfrac{\pi^2}{2} Cn^2 v^{-2-\epsilon},
 \qquad
 \ell_z=\log\frac{K_v(B,C_{z+e_1}A)}{K_v(B,C_zA)} .
\]
Sewing gives $Z^{z+e_1}(2v)/Z^z(2v)=\mathbb E_z e^{\ell_z}$. Jensen gives a log ratio at least $-h_v$. Applying it starting at $z+e_1$ gives the upper bound $h_v$. Spatial permutations give the three generators. Therefore all eight masses at each of $u,2u$ agree up to log differences at most $3h_{u/2},3h_u$, respectively. At both aspects $h_v=O(v^{-\epsilon})$. The OpenAI authors' two-dimensional pinned-spin stiffness proof uses a scale-by-scale signed current-variance decrement and control of the pins. No corresponding decrement has been proved here. [Row 1556(v)](gap-mech-direction4-check-astra62.md) · [’t Hooft sectors on file, §§3.0–3.1](gap-flux-exercise.md) · [OpenAI pinned-spin proof, §7.3 of the source record](prior/gap-2don-proofs-read-opus.md)

There is a second check on the abelian power. Denote the actual supremum on the left of (B) at a given $\beta,n,v$ by $\mathcal B_4(\beta,n,v)$, and put $p_-=\operatorname{Tr}(\tfrac12(1-C_1)T^{2v})/Z^0(2v)$. The same periodic Jensen calculation, using the actual row in place of its proposed bound, gives
\[
 \mathcal B_4(\beta,n,v)\ \ge\
 \frac{2}{\pi^2 n^2}\left[-\log(1-2p_-)\right].
\]
Here $1-2p_-=Z^{e_1}(2v)/Z^0(2v)>0$. In the compact abelian test $p_-\ge\eta_{2000}$ at sufficiently weak Wilson coupling, so the four corners also rule out the extra power without differentiating a continuous symmetry. In the target $SU(2)$ theory the trial estimate preceding (5) does not give such a lower bound.

Put $a_t=Z_+(t)/Z^0(t)$. The bounds force $|\log a_{2v}|\le3h_v$. The purity at this coupling still contains the independent factor
\[
 \frac{Z_+(2u)}{Z_+(u)^2}
 =\frac{Z^0(2u)}{Z^0(u)^2}\,\frac{a_{2u}}{a_u^2}.
\]
In particular the common normalization across the two periods, and control at the calibrated release roots $\beta_K$ for infinitely many $K$ at one fixed $l,g_0$, are both required. [Sixteen-mass consumer, §3.1](gap-k2-tool-design-fable.md)

**Spectator check.** Tensor the transfer with a neutral circle heat kernel with eigenvalues $e^{-j^2/(2n)}$, $j\in\mathbb Z$, the harmonic rotor normalization of row 929. Let all cut rotations and twists act solely on the original field. The product kernel splits, its mixed log derivative is exactly $H_{xy}$, and integration over the spectator restores the same sewn marginal on the original ends. Its independent multiplier on purity is $\sum_j p_j^2\le\max_j p_j$, with $p_j\propto e^{-u j^2/(2n)}$. Since $u=n/512$, $\max_j p_j\le(1+2e^{-1/1024})^{-1}<1/2$. Thus even an original purity of one becomes smaller than $457/625$ at every release size. This separates the observables in the transfer-kernel setting. The product is a comparison theory. [Rotor, §3.1](gap-seam-max.md) · [Scope of the spectator argument, §(iii)](gap-mech-direction4-check-astra62.md)

RESULT — The isotropic 4D SU(2) Wilson bound (B) at $2\le\beta\le3$ remains open after single-link comparison, replica exchange and the spectral test. The absolute row decays for strong coupling and for the stated anisotropic strip. It is at least a positive constant times $v^{-2}$ for sufficiently weak 4D compact Wilson $U(1)$. The 5D interacting SU(2) test remains open. The band lemma would control relative twist weights only. No release seed or mass gap is proved.
