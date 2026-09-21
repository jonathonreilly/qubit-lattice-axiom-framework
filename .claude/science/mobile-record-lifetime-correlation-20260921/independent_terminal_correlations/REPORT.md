# Terminal content correlations at fixed positive formation intensity

**Independent result.** Starting completely empty, terminal connected correlations of bounded single-site content observables decay exponentially with graph distance on `Z^d`, for every fixed positive formation intensity, finite mobility, and strictly positive bounded pair matrix. The same conclusion holds for any spatial product initial law, including unequal site marginals. Constants below are explicit and conservative. Local fixation alone would not imply this conclusion: independence of spatial input and a quantitative bound on propagation of dependence are additional ingredients.

This concerns the supplied stochastic dynamics, not a physical field, equilibrium phase diagram, or TOE claim. The terminal object is the pointwise locally fixed configuration; an infinite system need not reach it at one finite global time.

## Model and quantitative statement

Sites of `Z^d`, with fixed finite integer `d>=1`, are vacant or contain one of six immutable contents. Births into vacancies have rates `epsilon` times the product of pair weights with occupied neighbors. Occupied-vacant neighbors exchange at heat-bath rate at most `kappa`, with unit symmetric edge proposals. There are no removals or occupied-occupied exchanges. Assume

\[
\epsilon>0,\quad 0\le\kappa<\infty,\quad
0<\min_{a,b}W_{ab}\le\max_{a,b}W_{ab}<\infty.
\]

The original symmetric matrix premise is retained; row-six normalization is not needed for this proof. Set

\[
z=2d,\quad w_-=\min(1,\min W),\quad w_+=\max(1,\max W),
\quad \alpha=6\epsilon w_-^z,\quad\beta=6\epsilon w_+^z,
\quad \Lambda=(z+1)(\beta+2z\kappa).
\tag{1}
\]

The birth hazard of each vacancy lies in `[alpha,beta]`. Let `X_infinity(x)` denote the eventual occupied content at `x`, and let `D=dist(x,y)>=1`. For bounded real content functions `f,g`, write `M_f=||f||_infinity`, `M_g=||g||_infinity`. Then

\[
\left|\operatorname{Cov}\big(f(X_\infty(x)),g(X_\infty(y))\big)\right|
\le M_fM_g\min\left\{1,
8(C+1)\exp\!\left[-\frac{\gamma D}{8e\Lambda}\right]\right\}.
\tag{2}
\]

For the empty initial state one may take

\[
\gamma=\alpha,\qquad C=1+2z\kappa/\alpha.
\tag{3}
\]

For a homogeneous product initial law with vacancy density `v_0`, replace `C` in (3) by `(1+2z kappa/alpha)v_0`. For an arbitrary spatial product law, let `v_*=sup_x Pr(X_0(x) is vacant)`. A uniform choice is

\[
\gamma=\alpha/2,\qquad
C=\frac{2(\beta+2z\kappa)}{\alpha}\,v_*
       \left(1+\frac{4z\kappa}{\alpha}\right)^d.
\tag{4}
\]

The graph-distance version of (2) holds uniformly on finite nearest-neighbor tori with the same parameters, using `z=2d` as a degree bound. All expectations are over the initial law and the independent update randomness. A nonzero one-point content bias is compatible with (2); the bound concerns the connected correlation, not its disconnected product of means.

## 1. Existence and a fixation tail

Use independent site/content proposal clocks of rate `epsilon w_+^z` and edge proposal clocks of rate `kappa`, with independent thinning marks. Cancelling unchanged factors in the heat-bath ratio makes its acceptance depend only on the endpoints and their neighbors. Birth updates read a closed one-site neighborhood. A hop update reads the union of the two endpoint neighborhoods.

Backward exploration from finitely many sites through these bounded local clocks is dominated by a finite-offspring branching process with total rate linear in its size. It does not explode in finite time. This constructs the unique local process for an arbitrary initial law independent of the future clocks. No infinite product of bond weights is used.

For a translation-invariant initial law, put `v(t)=Pr(X_t(0) is vacant)`. Expected incoming and outgoing hop fluxes cancel, so

\[
v'(t)=-E[\text{birth hazard at }0],\qquad
v(t)\le v_0e^{-\alpha t}.
\]

The expected number of births at a site after time `T` equals `v(T)`. Its expected arrivals and departures are each at most `z kappa v(T)/alpha`. Thus its expected number of future successful updates is at most

\[
(1+2z\kappa/\alpha)v_0e^{-\alpha T}.
\tag{5}
\]

This is the previously sealed local-activity estimate. Finite expected activity gives a last successful update almost surely, and `v(t)->0` makes the final site occupied. Consequently `Pr(T_fix(x)>T)` is bounded by (5). Countability gives simultaneous local fixation at all sites.

Here is a separate uniform extension that removes translation invariance for the fixation estimate. Label each **initial vacancy** by its initial site `a`. A vacancy label moves opposite to a record hop and is killed by a birth. No event creates a new vacancy label. Let `S_a(t)` indicate that this vacancy still exists and `K_a(t)` count its hops. Its hop rate is at most `z kappa`, and its killing rate is at least `alpha`. For any `delta>0`, the compensator inequality gives

\[
E[S_a(t)e^{\delta K_a(t)}]
\le \Pr(X_0(a)\text{ vacant})
    e^{[-\alpha+z\kappa(e^\delta-1)]t}.
\tag{6}
\]

Indeed, a hop multiplies this quantity by `e^delta`, a killing sends it to zero, and other events leave it unchanged. Stopping the hop count first and then using its bounded-rate exponential-moment domination justifies the calculation. No independence between the vacancy path and the environment is assumed.

If the label from `a` occupies `x` at time `t`, it made at least `dist(a,x)` hops. Summing (6) over labels and choosing `e^delta=1+alpha/(2z kappa)` when `kappa>0` yields

\[
\begin{aligned}
\Pr(X_t(x)\text{ vacant})
&\le v_*e^{-\alpha t/2}\sum_{a\in\mathbb Z^d}e^{-\delta|a-x|_1}\\
&=v_*\left(\frac{1+e^{-\delta}}{1-e^{-\delta}}\right)^d e^{-\alpha t/2}
=v_*\left(1+\frac{4z\kappa}{\alpha}\right)^d e^{-\alpha t/2}.
\end{aligned}
\tag{7}
\]

For `kappa=0`, the stronger direct bound `v_*e^{-alpha t}` implies (7). On a torus, choose one minimal coordinate displacement for each site; the finite sum is no larger than the `Z^d` sum.

At `x`, the rate of births is at most `beta V_x`; the rate of incident accepted hops is at most `kappa sum_(y~x)(V_x+V_y)`. Integrating (7) gives a uniform expected future-update count bounded by `C e^{-gamma T}` with (4). As above, this proves occupied fixation and

\[
\Pr(T_{\rm fix}(x)>T)\le C e^{-\gamma T}.
\tag{8}
\]

This auxiliary conclusion holds even for correlated initial laws. Spatial independence is needed later, not in (6)-(8).

## 2. Quantitative control of spatial dependence

Fix a site `x` and radius `R`. Couple the full process with the process on the induced ball `B_R(x)`, deleting crossing edges and using the same initial variables and proposal clocks inside the ball. Let `Y_{x,R}(T)` be its content at `x` at time `T`. This finite process is a function only of the initial variables in that ball, its birth clocks and its internal edge clocks.

A potential backward dependency step moves at most distance two. For each queried site, birth clocks contribute at most `beta(z+1)` to the sum of rates times possible parent sites. Its at most `z` incident edge clocks each contribute at most `2 kappa(z+1)`. Their sum is at most `Lambda` in (1). These are potential dependencies; rejected proposals may be overcounted.

For a chronological potential dependency path of `m` steps, summing over the successive clock and parent choices bounds its expected count by

\[
\frac{(\Lambda T)^m}{m!}.
\tag{9}
\]

This uses the Poisson factorial moment formula and the volume `T^m/m!` of the ordered time simplex. Repeated use of the same clock at distinct times is included. Any path escaping `B_R(x)` contains an initial segment of `m=floor(R/2)+1` such steps. Union bounding their number proves

\[
\Pr\big(X_T(x)\ne Y_{x,R}(T)\big)
\le \frac{(\Lambda T)^m}{m!}.
\tag{10}
\]

On the event that no potential dependency escapes, both update constructions agree. Crossing-edge clocks and acceptance functions reading outside neighbors cause an escape and are therefore covered. The range-two allowance is essential: on `0--1--2`, hopping a record at `0` into a vacancy at `1` has acceptance `W_(a,b)/(1+W_(a,b))` when a record of content `b` sits at `2`.

Now put `R=floor((D-1)/2)`. The two balls around `x,y` are disjoint, and `m=ceil(D/4)`. Under a spatial product initial law, the two finite-process observables are independent, including when their site marginals differ. Combining (8) and (10), each terminal observable differs from its finite-ball approximation with probability at most

\[
p=C e^{-\gamma T}+\frac{(\Lambda T)^m}{m!}.
\]

For bounded variables, the product moment changes by at most `4M_fM_g p`, and the product of means by at most the same amount. Independence of the approximants therefore gives

\[
|\operatorname{Cov}_\infty(f_x,g_y)|
\le 8M_fM_g\left[C e^{-\gamma T}+\frac{(\Lambda T)^m}{m!}\right].
\tag{11}
\]

Choose `T=m/(2e Lambda)`. Since `m!>=(m/e)^m`, the second term is at most `2^{-m}`. Also `gamma<=alpha<=beta<=Lambda`, so `gamma/(2e Lambda)<log 2`. Both terms are bounded by their coefficient times `exp[-gamma m/(2e Lambda)]`. Using `m>=D/4` and the elementary bound `|Cov|<=M_fM_g` proves (2).

This argument gives exponentially accurate local approximations to the terminal observables. It does not assert an exact finite coding radius or independence beyond a fixed distance.

## 3. Necessary distinctions and counterexample

At a fixed finite time, the same construction already gives, for every product initial law,

\[
|\operatorname{Cov}(f(X_t(x)),g(X_t(y)))|
\le M_fM_g\min\{1,\,8(\Lambda t)^m/m!\},\quad m=\lceil D/4\rceil,
\tag{12}
\]

where the content functions can be extended by zero on vacancies. This factorial spatial tail is not uniform in time. One cannot simply take `t->infinity` in it. The fixation estimate is what makes the terminal bound possible.

Fixation by itself says nothing about connected correlations. For an exact counterexample within the same positive-rate model, initially fill every site with `+e1` or fill every site with `-e1`, each with probability one half, using one common random choice. The law is translation invariant and already absorbed. For the first coordinate observable, every one-point mean is zero and every two-point connected correlation is one, at every separation. The law is not a spatial product law; being a mixture of product laws does not suffice.

Finite tori absorb globally, whereas `Z^d` generally does not become full at any finite time. Bound (2) is uniform in torus volume, in its torus graph distance. For homogeneous product data, the same finite-time coupling and uniform fixation tails also show convergence of terminal finite-dimensional torus marginals to those of the infinite local terminal configuration. This conclusion uses local approximation; it does not exchange an infinite global absorption time with a volume limit.

All constants fix `d`, `W`, `epsilon>0` and finite `kappa`. They deteriorate when `epsilon->0` at fixed positive `kappa`, `kappa->infinity`, a positive weight floor is lost, or rates/degrees become unbounded. No conclusion about those singular limiting terminal laws follows from (2). At `epsilon=0` an empty start stays empty, so there is no final occupied record field. Multiplying both rates by the same positive constant only changes time units; the terminal law and the dimensionless bounds remain unchanged. A simultaneous small-rate limit at fixed `kappa/epsilon` is thus different from observing the system at a fixed physical time in that limit.

## Exact controls and source seal

`check.py` independently solves the full finite-generator absorption equations with rational arithmetic on a three-site path and checks every resulting harmonic equation. For the neutral menu `(3/2,1/2,1)`, the endpoint covariance of the first content coordinate is `1/162` at `(epsilon,kappa)=(1,0)`, `19/2928` at `(1,1)`, and `1979/270438` at `(1,10)`. Thus the theorem does not assert absent finite-separation correlations. The `(1/7,1/7)` result equals `(1,1)`, checking time rescaling. No general monotonicity in mobility is inferred from these examples.

For `W=1`, the empty-start terminal field is exactly independent uniform contents: motion is independent of content, and every final site contains a distinct record carrying an independent uniform birth mark. More generally homogeneous product marginals evolve as a product under independent vacancy filling; symmetric motion preserves each such product. The exact absorption check also tests a biased homogeneous product law and obtains means `1/3`, `1/3` and product moment `1/9`, hence zero covariance.

The checker verifies **1,519 exact vacancy-label exponential-drift inequalities**, the range-two acceptance discriminator `3/5 != 1/3`, and the radius/depth identity for 1,000 distances. It checks the fully occupied correlated counterexample directly. These controls check finite generators and important constants; the infinite-distance bound rests on the proof above, not on a fitted numerical decay curve.

The reused local-activity report has SHA-256 `7b4bad382af9d326a7de018db2bc8acd272fd960e16ac5c1a8cd4dba853e4ca4`; its seal is `e5a93c93d7a74d69713108035d53e78692bf6cd7bd2c4f87ca41bf281dfa0eb4`. All its artifact hashes were reverified unchanged. Original model identities are reused from that receipt: commit `689941783bea870e08458e079ddb208257d0083d`, event-law note `8cc06519d7f3acc088b1e450c151f0870ab21d2987ef2b0224d40ba6a5e7e4e2`, finite-rate note `423eba32f704e510331bfbb6dba78ea0a35db129854547b155fd76f27248d917`.

No new primary terminal-correlation calculation or quantum-interface file was read before this seal. This continuation read only the sealed local-activity report/receipt and checked unchanged instruction hashes. The context already contained the separately completed empty-start publication review; no terminal-correlation result is imported from it. Files created here are confined to the assigned independent directory; no primary source, Git, PR, audit or editable prompt was changed. `python3 check.py > RUN.log` reproduces the exact controls. `SEAL.json` records complete output and source identities.
