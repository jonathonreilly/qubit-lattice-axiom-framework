---
claim_id: spatial_particles_and_nonlinear_kinetic_limit_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "For a supplied local D3Q27 population process with directed nearest-neighbor transport and co-located binary collisions, exact jump drift and variance imply quantitative finite-population estimates, a nonlinear continuum kinetic limit on an explicit classical lifetime, and sufficient simultaneous particle/mesh scalings. No native carrier or nonlinear fluid identification is made."
upstream_dependencies:
  - supplied_finite_velocity_collisions_and_gibbs_equilibration_bounded_theorem_note_2026-10-08
runner: scripts/spatial_particles_and_nonlinear_kinetic_limit_2026_10_09.py
---

# Spatial particles and a nonlinear kinetic limit

**Date:** 2026-10-09

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** `17a95e60d85afc246fc7c163adef8869ab3f4194`; continued from `b178e3a5d4c1d1301255596d10ac4e1bc2aeb192`.

**Runner:** [finite controls](../scripts/spatial_particles_and_nonlinear_kinetic_limit_2026_10_09.py).

**Evidence cache:** `logs/runner-cache/spatial_particles_and_nonlinear_kinetic_limit_2026_10_09.txt`.

This note proves quantitative finite-population and mesh limits from a
specified spatial particle process to the nonlinear fixed-velocity kinetic
equation, on the stated classical lifetime. It allows varying spatial density.

The [supplied collision contract](SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md)
provides the finite reaction set. Its persistence import is not used here.
The process supplies the spatial state space, particle mass, velocity labels,
directed hop law, collision channels, rates, clocks and initial law. These
are model choices; their physical identification with the framework is open.

| Proof obligation | Disposition |
|---|---|
| Four distinct species and five conserved quantities per channel | Established directly in the linked collision contract; re-enumerated in the runner |
| Local process, exact drift and bracket | Proved in Sections 2–3 |
| Energy/Doob and density localization estimates | Proved in Section 4 |
| Classical kinetic lifetime and derivative bounds | Proved in Section 5 |
| Upwind consistency and simultaneous population/mesh limits | Proved in Sections 6–7 |
| Native excitation dynamics or nonlinear fluid closure | Open physical or mathematical extensions, not premises of these theorems |

## 1. Collision and spatial conventions

Let `V={-1,0,1}^3`, `q=27`, with velocity species indexed by `i`. For every
two distinct unordered pair-complexes having equal vector sum and equal
sum of squared speeds, include the reversible channel

\[
 r:\quad \{i,j\}\rightleftarrows\{k,l\},\qquad
 \nu_r=e_k+e_l-e_i-e_j,
\]

at a fixed positive forward/reverse coefficient `kappa_r`. There are 288
channels; every one uses four distinct species. Put

\[
 K=\sum_r\kappa_r,\qquad
 F(f)=\sum_r\kappa_r\nu_r(f_i f_j-f_k f_l).
 \tag{1}
\]

We retain two explicit prefactors `sigma>=0` and `gamma>=0`: streaming has
speed `sigma v` and the reaction term is `gamma F`. In particular the linear
diffusive scaling considered by the existing note uses
`sigma=delta^-1`, `gamma=delta^-2`, after a separate amplitude linearization.
All estimates below display both prefactors.

The spatial torus is `(R/(2 pi Z))^3` with **normalized** measure
`dx/(2 pi)^3`. For an integer `m>=2`, let

\[
 h=2\pi/m,\qquad w=m^{-3},\qquad
 \Lambda_m=(\mathbb Z/m\mathbb Z)^3.
 \tag{2}
\]

Each cell has physical side `h` and normalized measure `w`. Its center is
`x_z=h z`, with cells interpreted periodically. The distinction between `h`
and `w` is essential: `w=h^3/(2 pi)^3`. These formulas also apply to a torus
of side `L` after replacing `h` by `L/m`, while `w=m^-3` stays unchanged.

For grid fields use

\[
 \|a\|_h^2=w\sum_{z\in\Lambda_m}\sum_i |a_{zi}|^2,
 \qquad \|a\|_{1,h}=w\sum_{z,i}|a_{zi}|.
 \tag{3}
\]

Their piecewise constant interpolants `I_h a` have exactly these continuum
`L^2_x(ell^2_v)` and `L^1_{x,v}` norms.

Fix a total mass `M>0` and an integer total particle count `N>=1`. Each
particle has mass `M/N`. For occupation numbers satisfying `sum n_zi=N`,
define

\[
 p_{zi}^{N,h}=\frac{M n_{zi}}{Nw},\qquad
 w\sum_{z,i}p_{zi}^{N,h}=M.
 \tag{4}
\]

Thus `Nw` is the particle count per cell corresponding to uniform mass
density `rho=M`; density `rho` instead corresponds to count `Nw rho/M`.
Neither expression constrains the actual count of every cell. For the
unit-total-mass convention of the prior population note, take `M=1`.
The local mass density
`rho_z=sum_i p_zi` varies in space and time; no cell-mass constraint is imposed.

## 2. A strictly local population process

There are two types of continuous-time events.

1. A particle of type `i` at cell `z` hops to
   `z+sgn(v_ia)e_a` at rate `sigma |v_ia|/h`, for each nonzero coordinate
   `v_ia`. It keeps its velocity. Equivalently the occupation event has rate
   `sigma |v_ia| n_zi/h`.
2. At a single cell `z`, a channel `r` changes `n_z` by `+nu_r` at rate
   `gamma kappa_r M n_zi n_zj/(Nw)`, and by `-nu_r` at rate
   `gamma kappa_r M n_zk n_zl/(Nw)`.

Positive-rate collisions have nonnegative target counts because all four
species are distinct. No repeated-particle or factor-of-two correction is
needed. The state space is finite and all rates are finite, so the chain
exists for all times without explosion. At the labelled-particle level,
each distinct-species pair at the same cell has the indicated channel clock;
a fair assignment of the two output velocities to its two labels produces
exactly these occupation rates. This is a genuine local binary mechanism.

Collisions preserve mass, the three momentum components and assigned energy
`|v|^2` at their cell. Hops transport those quantities to a neighboring cell
without changing their global totals. Thus each trajectory preserves the
five **global** quantities `w sum_z A p_z`, where the columns of `A` are
`(1,v_x,v_y,v_z,|v|^2)^T`. There is no global random reshuffling or collision
between particles at different cells.

Define the unscaled upwind generator on density fields by

\[
 (A_h a)_{zi}
 =\sum_{a:v_{ia}\ne0}\frac{|v_{ia}|}{h}
   \bigl(a_{z-\operatorname{sgn}(v_{ia})e_a,i}-a_{zi}\bigr).
 \tag{5}
\]

The deterministic grid kinetic equation is

\[
 \dot u_z=\sigma(A_hu)_z+\gamma F(u_z),\qquad
 u(0)=u^0\ge0,\qquad w\sum_{z,i}u^0_{zi}=M.
 \tag{6}
\]

Its solution is unique, nonnegative and global for each fixed grid: the
vector field is polynomial, is inward pointing at every zero coordinate,
and conserves the total mass, giving `0<=u_zi<=M/w` and continuation.
Strictly positive initial components remain positive on finite intervals
by the integrating-factor formula for their losses and nonnegative gains.

The grid local mass balance is

\[
 \dot\rho_z=\sigma\sum_i(A_hu)_{zi}.
 \tag{7}
\]

Momentum and energy obey the corresponding velocity-weighted flux laws.
The collision term vanishes from each such local law; transport generally
does not vanish.

## 3. Exact drift and quadratic variation

Put `a_N=M/(Nw)`. A transport event has density increment
`a_N(e_target,i-e_source,i)`; a collision has increment `+/- a_N nu_r`
supported at its own cell. For a test function `Phi`, the occupation
generator is the sum of `event rate * [Phi(p+increment)-Phi(p)]` over exactly
the events in Section 2. Applying it to each coordinate gives

\[
 p(t)=p(0)+\int_0^t[\sigma A_hp(s)+\gamma F(p(s))]ds+\mathcal M(t),
 \tag{8}
\]

where `mathcal M` is a square-integrable grid-valued martingale. In particular,
the collision drift has coefficient

\[
 \frac{M}{Nw}\frac{\gamma\kappa_r M}{Nw} n_{zi}n_{zj}
 =\gamma\kappa_r p_{zi}p_{zj}.
 \tag{9}
\]

The bracket is the sum of each event rate times the outer product of its
density increment. In the norm (3), its trace rate is exactly

\[
 \begin{split}
 Q_{\rm hop}(p)&=
 \frac{2\sigma M}{Nh}\sum_{z,i}|v_i|_1p_{zi},\\
 Q_{\rm coll}(p)&=
 \frac{4\gamma M}{N}
 \sum_z\sum_r\kappa_r(p_{zi}p_{zj}+p_{zk}p_{zl}).
 \end{split}
 \tag{10}
\]

The factor 2 for hops is their two cell entries; the factor 4 for collisions
is the four distinct species. Since `|v_i|_1<=3` and
`sum_zi p_zi=M/w`,

\[
 Q_{\rm hop}\le\frac{6\sigma M^2}{Nwh}.
 \tag{11}
\]

If every component of `p` is at most `R`, the elementary inequality
`ab<=(R/2)(a+b)` gives

\[
 Q_{\rm coll}\le\frac{2\gamma K R M^2}{Nw}.
 \tag{12}
\]

These are conditional drifts and brackets. No closure
`E F(p)=F(Ep)` or independence between particles at positive times is used.

## 4. Finite-particle estimates without a transport exponential

Periodic shifts are isometries in (3). Direct expansion gives

\[
 \langle a,A_h a\rangle_h
 =-\frac{w}{2h}\sum_{z,i,d}|v_{id}|
 |a_{z-\operatorname{sgn}(v_{id})e_d,i}-a_{zi}|^2\le0.
 \tag{13}
\]

For nonnegative `f,g` with every component at most `R`,

\[
 \|F(f)-F(g)\|_2\le4KR\|f-g\|_2.
 \tag{14}
\]

Indeed the gradient of `f_i f_j-f_k f_l` has four entries of magnitude at
most `R`, hence norm at most `2R`; multiply by `||nu_r||_2=2` and sum rates.
Convexity of the box justifies the mean-value estimate. Summing over cells
gives the same Lipschitz constant in (3).

### Elementary stochastic energy lemma

Suppose a real Hilbert-space error has form `de=D dt+dM`, with `L,C>=0`,
`<e,D><=L||e||^2` and `d tr<M>/dt<=C`, including after stopping. If
`E0=E||e(0)||^2`, then

\[
 \mathbb E\sup_{t\le T}\|e(t)\|^2
 \le5e^{2LT}(E_0+CT).
 \tag{15}
\]

Proof: the jump energy identity is

`||e_t||^2 <= ||e_0||^2+2L integral_0^t ||e_s||^2 ds+2 Z_t+[M]_t`,

where `Z_t=integral_0^t <e_{s-},dM_s>`. Expectation and Gronwall give
`phi(t):=E||e_t||^2 <= (E0+Ct) exp(2Lt)`. Let
`D_T=(E0+CT) exp(2LT)`. The expected nonmartingale terms in the supremum
bound sum to at most `D_T`. The scalar martingale isometry and Doob's
`L^2` inequality give

\[
 2\mathbb E\sup_{t\le T}|Z_t|
 \le4\left(C\int_0^T\phi(s)ds\right)^{1/2}
 \le4\sqrt{CTD_T}\le4D_T.
\]

Here `E[M]_T=E tr<M>_T<=CT`; all integrability conditions hold for the
finite chain and its stopped version. This proves (15). No bound on
`||A_h||`, and hence no artificial exponential in `sigma/h`, was used.

### Global, fixed-grid estimate

For any grid initial law `p(0)`, any deterministic `u^0` as in (6), and every
finite `T`, put `E0=E||p(0)-u^0||_h^2`. Then

\[
 \boxed{\mathbb E\sup_{t\le T}\|p(t)-u(t)\|_h^2
 \le5e^{8\gamma KM T/w}
 \left\{E_0+\frac{M^2T}{Nw}
     \left(\frac{6\sigma}{h}+\frac{2\gamma KM}{w}\right)\right\}.}
 \tag{16}
\]

Proof: both fields lie componentwise in `[0,M/w]`. Apply (13), (14),
(11), (12), and (15) to (8) minus (6), taking
`L=4 gamma K M/w` and
`C=M^2/(Nw)[6 sigma/h+2 gamma KM/w]`.

This is an unconditional finite-horizon mean-square law of large numbers
for fixed grid and prefactors when the initial mean-square error tends to
zero. It allows arbitrary random initial configurations. Its growing
`w^-1` exponential is explicitly visible and will not be called uniform
under spatial refinement.

### Localized estimate for the unmodified process

Suppose the deterministic solution obeys `max_zi,t<=T u_zi(t)<=B`, and choose
`R>B`, `eta=R-B`. Let

\[
 \tau_R=\inf\{t\ge0:\max_{z,i}p_{zi}(t)\ge R\},\qquad
 D_R=5e^{8\gamma KR T}
 \left\{E_0+\frac{M^2T}{Nw}
 \left(\frac{6\sigma}{h}+2\gamma KR\right)\right\}.
 \tag{17}
\]

This stopping time is only used in the proof; no rates or paths of the
population process are cut off or altered. Then

\[
 \mathbb E\sup_{t\le T}
 \|p(t\wedge\tau_R)-u(t\wedge\tau_R)\|_h^2\le D_R,
 \qquad
 \mathbb P(\tau_R\le T)\le\frac{D_R}{w\eta^2}.
 \tag{18}
\]

For every `r>0`, the **actual**, unstopped process satisfies

\[
 \boxed{\mathbb P\left(\sup_{t\le T}\|p(t)-u(t)\|_h>r\right)
 \le\min\left\{1,\frac{D_R}{\min(r^2,w\eta^2)}\right\},}
 \tag{19}
\]

\[
 \boxed{\mathbb E\sup_{t\le T}\|p(t)-u(t)\|_{1,h}^2
 \le D_R\left(q+\frac{4M^2}{w\eta^2}\right).}
 \tag{20}
\]

If a mean-square `L^2` bound on the full process is needed, a less efficient
but valid one is

\[
 \mathbb E\sup_{t\le T}\|p(t)-u(t)\|_h^2
 \le D_R\left(1+\frac{2M^2}{w^2\eta^2}\right).
 \tag{21}
\]

Proof: before `tau_R`, (14) applies with `R` and the trace rate is bounded
by the `C` in (17). The stopped difference obeys (15). On exiting, some
component differs from the deterministic component by at least `eta`, so
the squared grid norm is at least `w eta^2`, including an exit at time zero.
An overshoot causes no problem: drift and bracket depend on the pre-jump
state, while a larger post-jump value strengthens this lower bound.

If the full error ever exceeds `r`, either there has been no exit and the
stopped error exceeds `r`, or an exit gives stopped error at least
`sqrt(w) eta`; Markov's inequality proves (19). Off the exit event,
`||a||_1,h^2<=q||a||_h^2`. On the exit event both nonnegative fields have
mass `M`, so their `L^1` distance is at most `2M`, proving (20).
Likewise `||p-u||_h^2<=2M^2/w`, proving (21).

For independent initial particle categories with probabilities

\[
 \pi_{zi}=wu^0_{zi}/M,
\]

the multinomial covariance gives exactly

\[
 E_0=\frac{M^2}{Nw}\left(1-\sum_{z,i}\pi_{zi}^2\right)
 \le\frac{M^2}{Nw}.
 \tag{22}
\]

Independence is used only for this optional initial-error formula.

## 5. Continuum kinetic equation and stated lifetime

Let `f^0>=0` belong to `C^2(T^3;R^27)`, with normalized total mass `M>0`.
Put `B0=max_i ||f_i^0||_infinity`. Consider the semilinear kinetic equation

\[
 \partial_t f_i+\sigma v_i\cdot\nabla f_i=\gamma F_i(f),
 \qquad f(0)=f^0.
 \tag{23}
\]

It has a unique nonnegative classical solution at least for every

\[
 0\le T<(\gamma K B_0)^{-1},\qquad
 B_T=\frac{B_0}{1-\gamma K B_0 T},
 \tag{24}
\]

with the right endpoint interpreted as infinity when `gamma=0`. The solution
is `C([0,T];C^2)` and `C^1([0,T];C^1)`, and has components at most `B_T`.
This is a sufficient explicit local lifetime; neither global classical
existence nor an obstruction to it is asserted here.

Proof details: translations along each velocity give a strongly continuous
semigroup on `C^2`; the polynomial collision map is locally Lipschitz there.
The characteristic gain-minus-loss formula preserves nonnegativity. Each
component has total gain at most `K X(t)^2` when
`X(t)=max_i||f_i(t)||_infinity`; dropping the nonnegative losses gives
`X(t)<=B0+gamma K integral_0^t X(s)^2 ds`, whence (24).

For explicit derivative control define
`G_j(t)=max_i,max_{|alpha|=j} ||partial^alpha f_i(t)||_infinity` and
`G_j0=G_j(0)`. Differentiating along characteristics gives

\[
 G_1(t)\le G_{10}e^{4\gamma K B_Tt},\qquad
 G_2(t)\le e^{4\gamma K B_Tt}
 \left[G_{20}+4\gamma KtG_{10}^2e^{8\gamma K B_Tt}\right].
 \tag{25}
\]

The first derivative term has row-sum bound `4KB_T`; each second derivative
has the same linear part plus at most `4K G_1^2`. These bounds prevent a
`C^2` continuation failure before any `T` in (24). The same componentwise
maximum argument applies to (6), so cell-average initialization gives
`0<=u_zi(t)<=B_T` uniformly in `m` on this interval.

Integrating the five conservation laws over the torus preserves `M` and the
four other global moments. Locally, with
`rho=sum_i f_i`, `j=sum_i v_i f_i`,
`Pi_ab=sum_i v_ia v_ib f_i`, and `q_E=sum_i |v_i|^2 v_i f_i`,

\[
 \partial_t\rho+\sigma\nabla\cdot j=0,\quad
 \partial_t j_a+\sigma\sum_b\partial_b\Pi_{ab}=0,\quad
 \partial_t E+\sigma\nabla\cdot q_E=0.
 \tag{26}
\]

In particular neither constant pointwise density nor a local normalized
velocity probability is assumed in the nonlinear collision equation.

## 6. Quantitative spatial continuum comparison

Initialize the grid by cell averages

\[
 u^0_{zi}=\frac1{h^3}\int_{\mathrm{cell}(z)}f_i^0(x)\,dx.
 \tag{27}
\]

This preserves the exact normalized total mass `M`. Let
`G_j^T=sup_{t<=T}G_j(t)` and `L_B=4 gamma K B_T`. Then

\[
 \epsilon_h:=
 e^{L_BT}\left(\frac{h^2G_{20}}8+
              \frac{3\sigma hT}2G_2^T\right),
 \qquad
 d_h:=\epsilon_h+\frac{3h}{2}G_1^T,
 \tag{28}
\]

satisfy

\[
 \sup_{t\le T}\max_{z,i}|u_{zi}(t)-f_i(t,x_z)|\le\epsilon_h,
 \qquad
 \sup_{t\le T}\|I_hu(t)-f(t)\|_{L^2_x(\ell^2_v)}\le\sqrt q\,d_h,
 \tag{29}
\]

and the corresponding `L^1_{x,v}` bound is `q d_h`.

Proof: a one-coordinate Taylor formula gives

\[
 \left|\frac{f_i(x-h\operatorname{sgn}(v_{ia})e_a)-f_i(x)}h
       +\operatorname{sgn}(v_{ia})\partial_a f_i(x)\right|
 \le\frac h2\|\partial_{aa}f_i\|_\infty.
\]

Summing at most three coordinates bounds the residual of sampled (23) in
(6) by `3 sigma h G_2(t)/2`. The upwind semigroup contracts the maximum
norm. The polynomial collision map has maximum-norm Lipschitz constant
`4 K B_T` on this box, by its row-sum derivative bound. Variation of
constants and Gronwall give the first estimate in (29).

For its initial term, one-dimensional symmetric averaging differs from the
midpoint value by at most `h^2||partial_aa f||_infinity/24`. Applying the
three coordinate averaging operators in succession gives
`max|u^0-f^0(x_z)|<=h^2 G20/8`; this proof does not discard mixed derivatives
at uncontrolled Taylor points. Finally every point in the cell is within
coordinate distance `h/2` of its center, yielding `3h G_1^T/2` and (29).

## 7. Ordered and simultaneous limits

Combine (20), (22), and (29), with for example
`B=B_T`, `R=2B_T`, `eta=B_T`. Define `D_R` from (17), using the exact
initial error or its upper bound (22). For the actual particle process,

\[
 \boxed{\mathbb E\sup_{t\le T}
   \|I_hp(t)-f(t)\|_{L^1_{x,v}}^2
 \le2D_R\left(q+\frac{4M^2}{wB_T^2}\right)+2q^2d_h^2.}
 \tag{30}
\]

The `L^2` probability estimate is likewise explicit: for every `r>0`,

\[
 \mathbb P\left(\sup_{t\le T}\|I_hp(t)-f(t)\|_{L^2_x(\ell^2_v)}
                         >r+\sqrt q\,d_h\right)
 \le\min\left\{1,\frac{D_R}{\min(r^2,wB_T^2)}\right\}.
 \tag{31}
\]

For fixed `sigma,gamma,T,K,M,f^0` in the lifetime (24), the constants
`B_T`, `R`, derivative bounds and exponentials are independent of `h,N`.
Equations (17), (22) have `D_R=O(1/(Nwh))` as `h` tends to zero when
`sigma>0`; (28) has `d_h=O(h)`. Since `w=h^3/(2 pi)^3`, a sufficient
simultaneous regime is

\[
 h\longrightarrow0,\qquad N h^7\longrightarrow\infty.
 \tag{32}
\]

It gives uniform-in-time mean-square `L^1` convergence (30), and uniform
`L^2` convergence in probability (31). Equation (21) also gives a sufficient,
less efficient condition `N h^10 -> infinity` for mean-square full `L^2`
convergence. These sufficient exponents are bounds from this proof, not
thresholds or optimality claims. If `sigma=0`, the displayed exact bounds
apply and give a better sufficient power.

An ordered limit needs no coupling prescription: first let `N->infinity`
at each fixed `h` using (16), then refine `h` using (29). The continuum
statement is restricted to the same classical lifetime. Taking `T->infinity`,
letting rates degenerate, refining the velocity set, or scaling `sigma,gamma`
with a new small parameter is not licensed by fixed-prefactor asymptotic
notation. For such a simultaneous limit use the complete expressions
(17), (24), (25), (28), (30), and verify that their terms vanish. In
particular `gamma=delta^-2` may collapse the simple lifetime (24), and its
exponential may be costly; a separate near-equilibrium energy argument can
improve that regime but is not silently assumed here.

## 8. Alternatives, discriminator and remaining scope

The initially available global mass bound `p_zi<=M/w` alone gives (16) and
an ordered limit. It is inadequate for a useful polynomial simultaneous
population requirement because of its `exp(constant/w)` factor. The
localization argument proves (30) for the same full chain and removes that
particular cost; it does not replace local transport by global averaging.

Deterministic straight-line motion with point particles and zero-range
collisions would require an additional encounter mechanism and its own
well-posed scaling argument; this proof does not claim that model. A
synchronous exact lattice streaming/split-collision construction is another
possible model, but would introduce a time-step splitting error. The
continuous-time nearest-neighbor construction above instead has the explicit
vanishing upwind consistency error in (28). Its single-particle local
displacement has drift `sigma v` and covariance rate
`sigma h diag(|v_1|,|v_2|,|v_3|)`, so its spatial randomness vanishes with
the stated mesh limit.

A companion exact-arithmetic discriminator `scripts/spatial_particles_and_nonlinear_kinetic_limit_2026_10_09.py`
independently enumerates collision candidates from four-element species
subsets (no imports from the repository runner), then compares literal count
event sums with the density polynomial/upwind formulas. It checks event
locality, conserved moments, bracket trace normalization and streaming
dissipativity, and tests wrong cell-volume and global-collision-average
mutations. This is author-generated finite algebra evidence and is not an
independent review or a proof of the probabilistic/PDE estimates.

It was run successfully with `PYTHONDONTWRITEBYTECODE=1 python3
scripts/spatial_particles_and_nonlinear_kinetic_limit_2026_10_09.py`; its complete short output is preserved in
`logs/runner-cache/spatial_particles_and_nonlinear_kinetic_limit_2026_10_09.txt`. The test uses 27 cells, 1,304 particles,
some zero species counts, nonuniform rational rates, nonunit total mass and
different physical/normalized cell volumes. It checks 17,010 event types.
The direct hopping bracket trace is exactly `870075/1700416`, and the
collision trace is `879305625/12611135264`; both equal their separately
assembled density formulas. A local mass-transport derivative is nonzero
(`-2835/5216` in cell zero), while all local collision mass derivatives
vanish. The test detects omission of the collision cell-volume factor,
replacement by global-average collisions, removal of transport, and reversal
of its dissipative sign. These figures describe the exercised finite case,
not a general proof or new physical calibration.

The new interface is a supplied spatial population -> supplied nonlinear
fixed-velocity kinetic equation bridge. Coupling it to the existing linear
hydrodynamic result needs a separate amplitude estimate with its own joint
scales. A native excitation map, clock, rate selection, physical observables,
and nonlinear fluid closure remain separate questions.

## 9. Review and formalization scope

Selective independent analytical and finite-algebra review is recorded in the
branch-local `PARTICLE_INDEPENDENT_REVIEW.md`, with exact source identities
and final packaging confirmation. The source retains the original general
mass convention `M`; the separate fluid composition specializes it to mass 1.
No prior note is replaced or granted a stronger status.

The primary runner imports no external input or repository computation. Its
literal jump enumeration and density formulas are separate implementations.
The note proves the probabilistic and PDE estimates; finite execution alone
is not their proof. Lean candidates include the finite generator/bracket
identities and the stopped energy lemma with all integrability and stopping
hypotheses. No Lean verification has been performed.


```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Control a spatial microscopic population approximation to nonlinear kinetics."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Identify a native carrier and test the nonlinear fluid scaling."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Quantitative supplied-model particle and kinetic theorems with explicit lifetime and scaling."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
