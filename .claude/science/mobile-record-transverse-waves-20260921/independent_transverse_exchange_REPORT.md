# Independent fifteen-state transverse exchange check

Date: 2026-09-21. Derived and sealed without accessing primary transverse,
Maxwell-named, or simulation sources. The only imported mathematics is in
the five allowed sealed independent reports identified below. This is a
conditional classical stochastic model, not an audit or a physical-field
identification.

**Result.** The supplied rates are positive with a fixed floor, preserve
every homogeneous product, and have an exact current potential
gamma E cross B. At orbit-isotropic interior products the full fourteen-field
linearization has a Maxwell-form curl block, four propagating modes and
ten zero-speed modes. The conservative Euler and stationary finite-mode
proofs apply after checking the hypotheses for fifteen labels. The fully
occupied restriction is a separate fourteen-label model with thirteen
independent fields, four propagating modes and nine zero-speed modes.
Uniform births preserve homogeneous products exactly but add order-one
formation noise in the Euler fluctuation limit. Equal occupied-label
products have an explicit integrated-phase propagator. Empty start is
covered by a new, stated boundary extension of the evolving-law energy
argument; it is not justified by a singular entropy inverse.

## 1. Generator, sharp bounds and product balance

The alphabet contains vacancy 0; six A labels with e=+/-coordinate unit
vectors and b=0; and eight B labels with e=0 and b=(sigma_1,sigma_2,sigma_3),
sigma_i=+/-1. In particular |b|=sqrt(3) on B; it has not been normalized
to a unit vector. Both features vanish at vacancy. Gamma is fixed. On a
positive-i edge the supplied symmetric tensor and drive are

\[
 S_i(a,c)={\gamma\over2}[e(a)\times b(c)+e(c)\times b(a)]_i,
\]
\[
 h_i(l,a,c,r)=S_i(l,a)+S_i(a,r)-S_i(l,c)-S_i(c,r).                    \tag{1}
\]

Use either c_i=kappa+max(h_i,0), kappa>0, or c_i=K_0+h_i/2. On cubic
tori N>=4 the four positions are distinct. All unequal endpoint labels,
including two occupied labels, can exchange. The update moves the whole
label without redrawing it.

Each tensor entry is 0 or +/-gamma/2. Hence

\[
 \max|S_i|=|\gamma|/2,\qquad \max|h_i|=2|\gamma|.                   \tag{2}
\]

The second bound follows by summing four entries, and is attained. For
i=3 take central labels A(+e_1), A(-e_1) and both outer labels B(+,+,+):
h_3=2gamma. Thus K_0>|gamma| gives the linear rate interval
[K_0-|gamma|,K_0+|gamma|], while the positive-part interval is
[kappa,kappa+2|gamma|]. These are fixed bounds as N grows. Gamma=0 is a
valid nonpropagating control.

Swapping the central endpoints reverses h, so c(eta)-c(eta^edge)=h(eta).
Along a periodic coordinate line,

\[
 \sum_x h_x=\sum_x[S(x-1,x)+S(x,x+2)
                         -S(x-1,x+1)-S(x+1,x+2)]=0.               \tag{3}
\]

The distance-one and distance-two sums cancel separately by translation.
A homogeneous product gives equal mass to a configuration and an endpoint
swap. Its master-balance residual is therefore minus its mass times (3),
which is zero. Every homogeneous product is invariant, including products
on boundary supports. Detailed balance is not implied. Fixed bounded local
rates also give the usual local graphical construction on Z^3; the finite
torus products pass to invariant infinite-volume products through local
finite-time convergence.

For proper cubic rotations R, both supplied label sets are preserved and
S(Ra,Rc)=R S(a,c). If a directed coordinate is reversed, the positive-edge
representation also reverses (l,a,c,r); its drive changes orientation twice.
The physical rate is covariant under the proper cubic group. An improper
transformation needs an additional declared action on e and b: if both are
treated as polar vectors, their cross product acquires det(R), so ordinary
reflection covariance does not follow from the present specification. No
parity extension is assumed here.

## 2. Complete product currents and entropy

For arbitrary probabilities p_z, including p_0, define

\[
 E=\sum_z p_z e(z),\quad B=\sum_z p_z b(z),\quad
 \Phi_i(p)=\sum_{z,w}p_zp_wS_i(z,w)=\gamma(E\times B)_i.
\]

Orient species current from the left endpoint to the right. Endpoint
interchange removes the swap-symmetric part of the rate. If
bar S_i(a)=sum_z p_z S_i(a,z), the four-site product expectation gives

\[
 J_a^i=2p_a[\bar S_i(a)-\Phi_i]
      =p_a[\partial_{p_a}\Phi_i-2\Phi_i]
      =\gamma p_a[e(a)\times B+E\times b(a)-2E\times B]_i.          \tag{4}
\]

This formula covers all fifteen species and both rate implementations.
The four-site offset count is already present in the factor 2; there is
no additional factor 2. Summing (4) gives zero. In particular
J_0=-2gamma p_0 E cross B, so the total occupied current is
2gamma p_0 E cross B.

For the fourteen independent occupied probabilities, with p_0=1-sum p_a,

\[
 C=\operatorname{diag}(p)-pp^T,\quad
 H=C^{-1}=\operatorname{diag}(1/p_a)+p_0^{-1}11^T,\quad
 J_i=C\nabla_p\Phi_i,\quad A_iC=CA_i^T,\quad A_i=D_pJ_i.            \tag{5}
\]

The last identity follows by differentiating J_i with respect to the
chemical potentials theta_a=log(p_a/p_0): it is the Hessian of Phi_i in
those coordinates. Equivalently H A_i is symmetric. H is positive definite
when all fifteen probabilities are positive. These are the full nonlinear
entropy identities, not just balanced-state identities. The entropy flux
is theta.J_i-Phi_i.

To display every field, put

* rho_A=sum_A p, q_i=p_(A+i)+p_(A-i), r_i=q_i-rho_A/3, sum r_i=0;
* rho_B=sum_B p and M_S=sum_sigma p_sigma product_(i in S)sigma_i,
  for subsets S of {1,2,3}. Thus M_empty=rho_B, M_{i}=B_i, the three
  M_{ij} are pair moments and M_{123} is the triple moment.

Together rho_A,rho_B,E(3),B(3),r(2),M_{ij}(3),M_{123}(1) are fourteen
independent fields. The B coordinates are its complete Walsh expansion;
no B population modes have been discarded. For a one-site observable F,
the exact current vector in physical space is

\[
 J_F=\gamma[\langle F e\rangle\times B
                  +E\times\langle F b\rangle
                  -2\langle F\rangle E\times B].                  \tag{6}
\]

Useful explicit instances, covering the full basis, are

\[
 J_{\rho_A}=\gamma(1-2\rho_A)E\times B,\quad
 J_{\rho_B}=\gamma(1-2\rho_B)E\times B,
\]
\[
 J_{q_i}=\gamma[E_i\,\hat e_i\times B-2q_iE\times B],\quad
 J_{E_i}=\gamma[q_i\,\hat e_i\times B-2E_iE\times B],
\]
\[
 J_{r_i}=J_{q_i}-J_{\rho_A}/3,\quad
 J_{M_S}=\gamma\{E\times(M_{S\triangle\{1\}},M_{S\triangle\{2\}},
                           M_{S\triangle\{3\}})-2M_SE\times B\}.   \tag{7}
\]

Here triangle denotes symmetric difference, and hat e_i is the spatial
coordinate unit vector. These are product currents used in a hydrodynamic
limit. They are not an exact closed first-moment system for a general
inhomogeneous microscopic law.

## 3. All fourteen modes and the precise curl sector

Take p_A=rho_A/6, p_B=rho_B/8, rho_A>0, rho_B>0 and
rho_A+rho_B<1. Then E=B=0, q_i=rho_A/3, and all nonempty B moments are
zero. At this product the only linear
currents are

\[
 \delta J_{E_m}^i={\gamma\rho_A\over3}\epsilon_{imk}\delta B_k,
 \qquad
 \delta J_{B_m}^i=\gamma\rho_B\epsilon_{ijm}\delta E_j.
\]

Conservation with the stated orientation therefore yields

\[
 \partial_t\delta E={\gamma\rho_A\over3}\nabla\times\delta B,
 \qquad
 \partial_t\delta B=-\gamma\rho_B\nabla\times\delta E.             \tag{8}
\]

Both signs matter. The other eight basis fields have zero linear current.
For nonzero Fourier vector k, write C_k v=k cross v. The directional
current matrix on the E,B block is

\[
 A_{EB}(k)=\begin{pmatrix}0&-aC_k\\bC_k&0\end{pmatrix},\quad
 a={\gamma\rho_A\over3},\quad b=\gamma\rho_B,
 \quad c^2=ab={\gamma^2\rho_A\rho_B\over3}.                        \tag{9}
\]

Since -C_k^2=|k|^2P_T, its full fourteen-field characteristic polynomial is

\[
 \lambda^{10}(\lambda^2-c^2|k|^2)^2.                              \tag{10}
\]

For gamma!=0 there are two modes at +c|k| and two at -c|k|. The ten
zero-speed modes are the two longitudinal vector components and all eight
spectator fields listed above. The current matrix is entropy-symmetric
in a positive metric, so these zero modes are semisimple. At k=0 every
mode is zero speed. If gamma=0, all fourteen speeds vanish. Vanishing
orbit densities leave the interior theorem and require the appropriate
smaller support; a formal singular-metric continuation is not a theorem.

Equation (8) is a transverse Maxwell-form linear sector after constant
field rescaling. It also leaves div E and div B unchanged, rather than
forcing them to vanish. A source-free Gauss constraint would be an
additional initial restriction. Nonlinear currents (7) still couple
the other moments, and the finite lattice has only its stipulated cubic
geometry. Neither a closed nonlinear Maxwell theory nor continuous
rotational or Lorentz symmetry of the full microscopic process follows.

The equilibrium one-site vector covariances are

\[
 C_{EE}=\rho_A I_3/3,\quad C_{BB}=\rho_B I_3,\quad C_{EB}=0.        \tag{11}
\]

The factor rho_B, rather than rho_B/3, comes from the supplied unnormalized
cube-corner labels. It fixes both the speed and formation-noise factors.

## 4. Why the conservative limit proofs apply

Each needed hypothesis of the allowed finite-alphabet proofs is verified:
the state set is finite; the rates have a fixed positive floor on every
unequal-label adjacent swap and a fixed ceiling; their support is four
sites; homogeneous products are invariant by (3); the current is the
polynomial (4); and (5) gives the nonlinear entropy compatibility.

In the relative-entropy proof, replace the reference uniform seven-state
product by the uniform fifteen-state product. The entropy budget is
V log15. Canonical sectors are the fifteen label counts, and nearest-neighbor
transpositions still connect all arrangements of a fixed multiset.
The Hamiltonian-path sorting proof gives the same conservative bound
M^2 15^M for a block of M sites. Fixed-footprint canonical sampling,
marginal Dirichlet contraction, translated-block overlap bounds and the
quadratic multinomial exponential estimate are unchanged apart from fixed
alphabet constants. The constant and linear cancellations use (5).
Thus, for a given C^2 periodic solution of

\[
 p_t+\sum_i\partial_iJ_i(p)=0
\]

with all fifteen probabilities bounded below on a fixed [0,T], initial
relative entropy o(N^3) remains o(N^3), uniformly on that interval.
Empirical weak profiles converge as in the sealed Euler proof. Adding
per-label macroscopic uniform births beta gives source beta p_0 1 and
the same theorem, with budget V(log15+beta T), as in that proof. No global
smooth-solution or post-shock assertion is included.

For stationary homogeneous full-support products and no births, define
the fourteen-component occupied-indicator Fourier field, on the macroscopic
generator N L_N, by

\[
 Y_N(k,t)=V^{-1/2}\sum_xe^{-ik\cdot x/N}[\xi_x(t)-p],
 \qquad k=2\pi m,\quad m\in\mathbb Z^3\text{ fixed}.
\]

The sealed stationary argument applies with canonical Poincare bound
2M^2 15^M. Its forward/reversed stationary martingale estimate still gives
(2t/N)||F||_{-1,S}^2; conditional centering and block overlaps bound this
inverse form by C M^3 15^M. The conditional current mean differs from
J(q) by O(1/M); after removing its constant and linear parts its normalized
spatial remainder has squared norm O(1/M). Exact Fourier filters handle
the O(ell/N) averaging error. Exchange jump brackets are O(1/N).
Consequently

\[
 \sup_{t\le T}\|Y_N(k,t)-e^{-itA(k,p)}Y_N(k,0)\|_2\longrightarrow0,  \tag{12}
\]

where the supremum is outside the L2 norm. For example the prior error
bound with sqrt(M^3 7^M/N) replaced by sqrt(M^3 15^M/N) tends to zero
using ell^3<=log N/(2 log15). Finitely many fixed modes and times converge
jointly to their Gaussian transported initial fields; conjugated two-time
covariance is e^{-i(t-s)A(k,p)}C(p). Nonconjugated covariance pairs opposite
modes. The zero mode is exactly conserved and may be included separately.

This supplies microscopic long-wavelength covariance content to (8), not
merely a formal flux spectrum. For example, at the orbit-isotropic product
and k!=0,

\[
 \lim E[Y_E(k,t)Y_E(k,0)^*]
     ={\rho_A\over3}[P_L+\cos(c|k|t)P_T].                          \tag{13}
\]

The analogous B factor is rho_B. The longitudinal covariance is retained;
it has not been discarded to manufacture a transverse result. The theorem
fixes p, parameters, floor, T and the mode list before N grows. It does
not give finite-wave-number damping, a growing-time limit or a maximal
path-space fluctuation theorem.

## 5. Exactly full occupancy is a separate fourteen-label model

When vacancy is absent, the actual generator remains an exchange process
on fourteen occupied labels. Products with all fourteen probabilities
positive are full-support products for this restricted model. Exchange
does not stop, and the same balance proof and rate floor hold. Choose one
occupied label a_* as reference and thirteen independent probabilities q.
Now use

\[
 C_{13}=\operatorname{diag}(q)-qq^T,\qquad
 H_{13}=\operatorname{diag}(1/q_a)+p_{a_*}^{-1}11^T.                 \tag{14}
\]

These are nonsingular in the fourteen-label interior. Restrict Phi to
p_(a*)=1-sum q. Its chemical derivatives again give the species currents,
and H_13 D_qJ is symmetric. Canonical sectors have fourteen counts and
the finite-block bound is M^2 14^M. Thus the conservative entropy and
stationary fluctuation theorems follow directly on this model without
inverting the singular fifteen-state vacancy metric.

At orbit-isotropic full products rho_B=1-rho_A, 0<rho_A<1, the actual
constraint delta rho_A+delta rho_B=0 removes one spectator. There are
thirteen independent fields, and their polynomial is

\[
 \lambda^9[\lambda^2-\gamma^2\rho_A(1-\rho_A)|k|^2/3]^2.           \tag{15}
\]

The four propagating modes and nine zero modes are semisimple. A redundant
fourteen-indicator description has covariance rank thirteen; its total
population fluctuation is identically zero, not an additional random mode.
For equal occupied-label probabilities 1/14, rho_A=3/7, rho_B=4/7 and
c=2|gamma|/7. Uniform births do nothing on this exactly full restriction,
and their noise is zero.

## 6. Uniform formation and the surviving finite-mode theorem

Add microscopic rate beta/N for each of the fourteen labels at vacancy,
so the macroscopic generator is N L_N+beta B_N. For any homogeneous
initial product, including boundary products, the exact finite-N trajectory is

\[
 p_0(t)=p_0(0)e^{-14\beta t},\qquad
 p_a(t)=p_a(0)+{p_0(0)\over14}(1-e^{-14\beta t}).                    \tag{16}
\]

The exchange generator annihilates every product on this curve, while
uniform independent births give its derivative; uniqueness of the finite
forward equation proves (16). No commutation of generator semigroups is
assumed. This is not a product-preservation statement for spatially varying
initial marginals or for a different neighbor-dependent formation rule.

For fixed full-support initial products, let C(t)=diag(p(t))-p(t)p(t)^T,
A_i(t)=D J_i(p(t)), R=-beta 11^T and

\[
 D_k(t)=-i\sum_i k_iA_i(t)+R.
\]

The correct joint finite-mode, finite-time limit is the fourteen-field
Gaussian diffusion

\[
 dY_k=D_k(t)Y_k\,dt+\sqrt{\beta p_0(t)}\,dW_k,                     \tag{17}
\]

with the initial Fourier Gaussian of covariance C(0), independent of the
new Gaussian noise. Its conventions are

\[
 E[dW_kdW_l^*]=I_{14}{\bf1}_{m=n}\,dt,\quad
 E[dW_kdW_l^T]=I_{14}{\bf1}_{m=-n}\,dt,
 \quad W_{-k}=\overline{W_k}.                                    \tag{18}
\]

The zero mode is real and has no exchange part. Birth noise is beta p_0
times the identity in occupied species coordinates. It is not the covariance
of a fixed number of categorical draws: the number of formation events
also fluctuates. The total-density noise variance is 14beta p_0.

Here is the nonstationary load-bearing check of applicability. The formal
weighted adjoint has row sum partial_t log mu_t; the Markov reversal is
the adjoint minus that score. Its births reverse to a->0 at
beta p_0(t)/p_a(t), with score -14beta at vacancy and beta p_0/p_a at
occupied a. Therefore the stationary forward/reversed martingale shortcut
must not be copied unmodified. Instead the allowed growing proof solves

\[
 (\partial_t+G_N)u_t=-F_t,\quad u_b=0,
\]

and uses the **actual** evolving law mu_t in

\[
 {d\over dt}E_{\mu_t}|u_t|^2
    =2\Re E_{\mu_t}[\bar u_t(\partial_t+G_N)u_t]
       +E_{\mu_t}\Gamma_{G_N}(u_t).
\]

The additive-functional squared norm is exactly
||u_a||^2+integral E Gamma=2 Re integral <u,F>. The exchange floor gives
E Gamma>=2N delta E_0. If |<F,h>|<=a_t sqrt(E_0(h)), it follows that

\[
 E\left|\int_a^bF_t(\eta_t)dt\right|^2
       \le {2\over N\delta}\int_a^b a_t^2dt.                      \tag{19}
\]

At each time the exact law (16) is product, and its conditional law given
block counts is uniform over arrangements. The canonical centering and
Poincare bound 2M^2 15^M give a_t^2<=C M^3 15^M for the fast current
residual. The slow residual and Fourier filters use the same one-time
product bounds as before, uniformly along the curve. This proves the
nonstationary current replacement for the actual context rates.

Each exchange martingale vanishes on this scale. A birth at x changes
species a's Fourier field by e^{-ik.x/N}/sqrt(V), giving the exact bracket

\[
 d\langle M^b_{N,a}(k),\overline{M^b_{N,c}(l)}\rangle_t
   =\delta_{ac}{\beta\over V}\sum_xe^{-i(k-l)\cdot x/N}
                                   {\bf1}_{\eta_x=0}\,dt.         \tag{20}
\]

Under the exact product, its normalized spatial fluctuation has variance
O(1/V), and its integrated deviation vanishes without a temporal mixing
assumption. Jumps are O(V^{-1/2}); the elementary compensated-exponential
argument in the sealed report yields the finite-dimensional Gaussian
martingale limit and independence from the initial field. These facts prove
(17), rather than assuming a noise closure.

If Phi_k(t,s) solves partial_t Phi=D_k(t)Phi, then the precise prelimit
L2 statement is approximation by

\[
 Z_N(k,t)=\Phi_k(t,0)Y_N(k,0)
                  +\int_0^t\Phi_k(t,s)\,dM_N^b(k,s),
 \quad \sup_{t\le T}\|Y_N(k,t)-Z_N(k,t)\|_2\longrightarrow0.       \tag{21}
\]

Pure deterministic transport of the initial field is false when beta p_0
is positive. Its omitted noise has covariance
integral Phi(t,u)[beta p_0(u)I]Phi(t,u)^*du. All fields, including those
with zero spatial speed, must be kept.

The normalization is independently fixed by

\[
 \dot C=D_k C+C D_k^*+\beta p_0I_{14},\qquad
 \lim E[Y_N(k,t)Y_N(k,s)^*]=\Phi_k(t,s)C(s),\quad t\ge s.           \tag{22}
\]

Indeed the exchange terms cancel by A_iC=CA_i^T, while
dot C=beta p_0[I-1p^T-p1^T] and R C+C R^T=-beta p_0(1p^T+p1^T).
The covariance limit follows from (21) and martingale isometry, not just
an unproved uniform-integrability inference from convergence in law.

## 7. Every growing mode, and equal-per-label explicit propagation

If the initial product is orbit-isotropic, it remains so, with

\[
 \rho_A(t)=\rho_A(0)+{3\over7}[p_0(0)-p_0(t)],\quad
 \rho_B(t)=\rho_B(0)+{4\over7}[p_0(0)-p_0(t)].                      \tag{23}
\]

The Maxwell block now has a(t)=gamma rho_A(t)/3, b(t)=gamma rho_B(t)
and zero direct reaction drift on E,B. The orbit fluctuations satisfy
delta rho_A'=-6beta delta rho, delta rho_B'=-8beta delta rho. Thus total
density has drift -14beta, and d=4rho_A-3rho_B has zero reaction drift.
The A quadrupoles, B pair/triple moments and both longitudinal vector
components have zero drift on this leading scale, but receive formation
noise. In the fourteen-dimensional field basis the noise is exactly
beta p_0 T T^T, where T maps occupied indicators to the listed observables.
In particular,

\[
 Q_E=2\beta p_0 I_3,\quad Q_B=8\beta p_0 I_3,\quad Q_{EB}=0,
\]
\[
 Q_\rho=14\beta p_0,\quad Q_d=168\beta p_0,\quad Q_{\rho,d}=0,
 \quad Q_r=2\beta p_0(I_3-11^T/3),
\]
\[
 Q_{M_{12},M_{13},M_{23},M_{123}}=8\beta p_0 I_4.                  \tag{24}
\]

Cross covariances between these groups vanish. The r block has its
sum-zero constraint. This displays every mode and its noise. In particular,
births do not preserve a zero longitudinal-field constraint.

For unequal initial orbit proportions the two Maxwell matrices at distinct
times generally do not commute: the E block of their commutator contains
[a(t)b(s)-a(s)b(t)]C_k^2. An explicit clock phase is not generally valid.
The full Phi in (21) is then time ordered.

For **equal occupied-label probabilities** p_a=rho/14, however,
rho_A=3rho/7, rho_B=4rho/7 for all times. This includes the fully uniform
fifteen-label product at rho=14/15, but does not mean all fifteen probabilities
remain equal as births proceed. Put Z=(E,mathcal B), mathcal B=B/2. Then

\[
 dE=i v_c(t)C_k\mathcal B\,dt+dM_E,\qquad
 d\mathcal B=-i v_c(t)C_k E\,dt+dM_{\mathcal B},
 \quad v_c(t)={2\gamma\rho(t)\over7},
\]
\[
 Q_Z(t)=2\beta p_0(t)I_6,\qquad C_Z(t)={\rho(t)\over7}I_6.          \tag{25}
\]

All deterministic Maxwell matrices are scalar multiples of one fixed
matrix, so they commute. For k!=0 define the signed phase

\[
 \Omega_k(t,s)={2\gamma|k|\over7}\int_s^t\rho(u)du
 ={2\gamma|k|\over7}\left[(t-s)
       -{p_0(0)\over14\beta}(e^{-14\beta s}-e^{-14\beta t})\right]  \tag{26}
\]

for beta>0. At beta=0 the integral is rho(0)(t-s). With
L=P_L+cos(Omega)P_T, the deterministic propagator on these six fields is

\[
 U_M(t,s)=\begin{pmatrix}
 L&i\sin(\Omega)C_k/|k|\\
 -i\sin(\Omega)C_k/|k|&L
 \end{pmatrix}.                                                   \tag{27}
\]

It is unitary in these matched covariance coordinates. The actual limit
still includes the stochastic convolution with (25). Its two-time covariance is

\[
 E[Z_k(t)Z_k(s)^*]={\rho(s)\over7}U_M(t,s).                         \tag{28}
\]

For example E-E covariance is rho(s)/7 times
[P_L+cos(Omega_k(t,s))P_T]. It is not a stationary cosine at a fitted
constant speed. The other eight fields retain the reaction and noise just
listed, and have not been integrated out to obtain (28).

## 8. Empty initial state and order of limits

Starting completely empty, the exact product law is still (16), now
p_0(t)=e^{-14beta t}, p_a(t)=(1-e^{-14beta t})/14. For beta>0 it is
interior for every t>0, but not at t=0. The interior entropy theorem alone
does not license substituting p_a(0)=0 into H.

The growing fluctuation argument has a stronger property. Its operative
energy identity (19) uses the finite forward equation and the backward
terminal equation, **not** division by mu_t or the score. It is valid even
if the law initially has zero probabilities. Given block counts, any product
on a boundary support is still uniform over arrangements in each sector
with positive probability. The canonical sorting bound is independent of
those probabilities. The residual current is conditionally centered on
each such sector. The polynomial Taylor and multinomial fourth-moment
bounds, current variance bound and Fourier-filter estimate are uniform
on the closed simplex. At the all-vacant support the residual is zero.
Thus the proof of (19)-(21) extends directly to the empty endpoint; it
never evaluates the reverse death rate beta p_0/p_a there.

An equivalent explicit limit order is to fix delta>0, apply the interior
growing theorem on [delta,T] with N tending to infinity, then let delta
decrease to zero. On [0,delta], exact product independence and bounded
finite-range currents give a uniform L2 bound on every centered Fourier
current field and on A(t)Y_N(t). Their integrated replacement discrepancy
is at most C delta uniformly in N. Initial covariance C(delta)=O(delta),
and the birth-martingale bracket on that interval is O(delta). These facts
close the small-time interval without any uniform inverse-density bound.
Both routes give the same finite-mode limit (17) with Y_k(0)=0.

The coefficients A(p(t)), R and beta p_0(t) are continuous at t=0, so the
limiting linear Gaussian diffusion starting from zero is well defined.
All empty-start randomness comes from formation noise. At the time when
p_0=1/2, for example, the exact one-time covariance of the fourteen-species
Fourier field has trace 27/56. A deterministic transport law from its
identically zero initial field would predict zero and is decisively false.
For the equal-label Maxwell block, the early integrated phase is
Omega_k(t,0)=2gamma beta |k|t^2+O(t^3); the noise has already begun at
order t. Longitudinal fields are also generated.

This theorem fixes beta, gamma, the floor, the finite horizon and finitely
many integer modes before N grows. It asserts finite-dimensional joint
laws and the L2 approximation (21), with the supremum outside the norm.
It does not assert an infinite-dimensional path limit, uniform growing
time or wave-number bounds, or interchange N->infinity with a fixed
microscopic formation rate. A fixed microscopic rate would become N beta
on this clock and is a different limit. With beta=0, empty start stays
empty. With exactly full occupancy, births are absent and Section 5 is
the proper conservative theorem.

## 9. Independent controls and retained development failures

The checker was written independently and imports no primary implementation.
It enumerates the 15^4=50,625 local words to verify sharp tensor/drive
bounds, endpoint antisymmetry, and complete directional four-cycle balance.
The 24 proper cubic actions are checked on all 225 label pairs at tensor
level, which suffices for the transformed four-site drive. A biased product
with nonzero E cross B checks every species current in all three directions
and both rate implementations by integer-weight enumeration. Generic
chemical-current and entropy identities are additionally tested exactly.

The fourteen-field matrix is assembled from the species-space Hessian of
the pair potential and an independently constructed full field basis.
Its polynomial, curl signs, extra modes and covariance factors are checked
symbolically. Full occupancy is recomputed using thirteen probabilities
and the affine reference-label Hessian. At equal full labels the covariance
minor has determinant 14^(-14)>0, verifying that this calculation never
uses a singular vacancy metric. Symbolic checks also retain the formation
reaction, all vector-noise factors, the equal-label rescaling, and a
noncommuting unequal-orbit control.

A complete fifteen-state four-cycle generator has 50,625 configurations
and 391,500 transition-array entries, with exchange acceleration 4 and
beta=1/3. Exact integer arithmetic checks the product forward equation,
the evolving-measure energy identity and birth covariance on equal and
biased interior products, the empty product and full occupancy. For one
species count in the equal interior case, the incorrect stationary energy
-E[u G u] is -1/14, whereas the actual count bracket is 2/3. At empty
start that count bracket is 4/3; it is not zero because u initially
vanishes. A complete configuration/current Fourier comparison checks the
negative-exponential sign on all six E,B features. These finite controls
support the load-bearing identities; the three-dimensional limit rests
on the proofs above.

Three checker executions are retained. Attempts 1 and 2 stopped on SymPy structural
equality tests for unexpanded exact zeros: first the isotropic gradient,
then equivalent factored entries in the full-occupancy matrix. Each failure
has its original script, raw traceback and exact diagnostic expansion.
The repair only normalizes polynomial differences before equality; no
target, premise or formula was altered. Attempt 3 completed all 23 exact
finite/symbolic control groups. Its full log is byte-identical to
`RESULTS.json`. `ATTEMPTS.json` binds each execution to its script hash.
There were no numerical stochastic simulations and no discarded failures.
A separate dependency-bookkeeping command stopped on a mistyped expected
axiom hash. `BOOKKEEPING_FAILURE.json` retains the failure, corrected identity
and unchanged source; the corrected comparison verified all dependencies.

The rejected shortcuts are explicit: omitting the ten static modes;
normalizing the B corners without changing the model; importing a singular
fifteen-state entropy inverse at full occupancy; ignoring the evolving-law
score; dropping formation noise; treating unequal-orbit drift matrices as
commuting; or obtaining empty start by a bare interior-theorem substitution.
Each is replaced by a displayed calculation or a checked proof step.

Reproduce from this directory using

    OPENBLAS_NUM_THREADS=1 python3 independent_check.py

Versions are recorded in the raw output. The only mathematical dependency
reports have these SHA-256 identities:

| Report | SHA-256 |
|---|---|
| context exchange | `277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713` |
| context Euler | `60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3` |
| stationary fluctuations | `772046745ac814c32adcd8f36e3c8415ddf4a3a4b37435e8992441c6c8d5be68` |
| growing fluctuations | `168ae65623d124f2aa10a0c215c75e8767950f7fb1c50fc5a3fc287f1667b1dc` |
| polynomial flux | `94d8ffa8681f9fbc605bd6ff196c495d6725e3c92fdd9013cee1b840577776e8` |

Their seals/checkers and the unchanged minimal-axiom memo are identified
in `DEPENDENCIES.json`; all new artifacts are bound by `PRE_SOURCE_SEAL.json`.

## 10. Boundary with the framework and physical interpretation

The local swaps preserve supplied labels and the at-most-one-record
occupancy condition, and respect proper cubic geometry. The fourteen
distinguishable occupied labels, their e/b features, the tensor, positive
floor, clock and uniform formation rule are additional supplied structure.
No qubit readout or compatibility with every minimal axiom has been derived.
Uniform formation is not the axiom's specified neighbor-dependent odds.

“Maxwell-form” here names the proved linear curl equations and their stated
long-wavelength stochastic sector. It does not supply physical electric or
magnetic observables, charges, zero Gauss constraints, gauge dynamics,
physical units, a physical light speed, Lorentz invariance, quantum theory
or a TOE conclusion. Conversely, this conditional positive construction is
not a no-go about such identifications. No source, Git, PR, audit or model
mutation was performed outside the assigned independent directory.
