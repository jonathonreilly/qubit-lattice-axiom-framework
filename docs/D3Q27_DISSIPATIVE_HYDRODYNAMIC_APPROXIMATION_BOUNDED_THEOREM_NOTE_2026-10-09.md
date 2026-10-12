---
claim_id: d3q27_dissipative_hydrodynamic_approximation_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Supplied periodic linear D3Q27 kinetic dynamics with all 288 reversible pair exchanges, fixed positive detailed-balance rates and a fixed positive product Gibbs state. Exact stress and heat responses, including the distinction between cubic and rotationally isotropic constitutive tensors. At the stated supplied isotropic rate, an H4 finite-diffusive-time O(delta) approximation by linear Stokes/heat equations. For arbitrary positive rates, an H5 finite-acoustic-time O(epsilon^2) approximation of projected fields and the first-corrected kinetic distribution by the dissipative macro equation, with explicit preparation and constants. A separate quadratic moment identity is not a nonlinear limit. No native dynamics, rate selection, physical clock, velocity refinement or nonlinear fluid limit is derived."
upstream_dependencies:
  - supplied_finite_velocity_collisions_and_gibbs_equilibration_bounded_theorem_note_2026-10-08
runner: scripts/d3q27_dissipative_hydrodynamic_approximation_2026_10_09.py
---

# D3Q27 dissipative hydrodynamic approximation

**Date:** 2026-10-09

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** `17a95e60d85afc246fc7c163adef8869ab3f4194`.

**Runner:** [exact collision, constitutive and corrector checks](../scripts/d3q27_dissipative_hydrodynamic_approximation_2026_10_09.py).

The supplied collision model has a controlled dissipative macroscopic limit.
With the explicit positive rate choice below, its linear kinetic equation on
diffusive time converges to

\[
 \partial_\tau\rho=\frac4{49}\Delta\rho,\qquad
 \partial_\tau j=\frac{67}{361}\Delta j,\qquad \nabla\!\cdot j=0.
\tag{1}
\]

Theorem 1 gives a uniform finite-time error of order `delta`, with explicit
constants and `H^4` initial data. This is a linear Stokes/heat limit of a fixed
finite-velocity kinetic system. Theorem 2 also gives order `epsilon^2` on
finite acoustic times for a dissipative macro equation, using `H^5` data and
first-order preparation. That sharper error compares the five conserved
fields or the first-corrected kinetic distribution. The full uncorrected
distribution generally retains an order `epsilon` constitutive correction.

The velocities, collisions, rates, equilibrium, continuum streaming and clock
are declared mathematical inputs. The rate making the stress isotropic is a
construction, not a value selected by the framework or an empirical fit.
The conclusions do not identify native lattice excitations with this model.
They advance a supplied kinetic-to-fluid interface relevant to the transport
targets of `lanes/open_science/07_THERMALIZATION_KINETIC_THEORY_OPEN_LANE_2026-06-12.md`
and `lanes/open_science/10_CONTINUUM_HYDRODYNAMICS_OPEN_LANE_2026-06-12.md`.
The physical identification remains a separate obligation.

## 1. Supplied collision operator and exactly five invariants

Let `V={-1,0,1}^3`, with `e(v)=|v|^2`. Include every exchange of two distinct
unordered pair-complexes

\[
 \{i,j\}\longleftrightarrow\{k,l\},\qquad
 v_i+v_j=v_k+v_l,\quad e_i+e_j=e_k+e_l.
\tag{2}
\]

Pairs initially allow repetition. Every nontrivial exchange actually uses four
distinct velocities: a shared velocity would force the other two equal; an
input `(v,v)` would require an output `(v+w,v-w)` with `2|w|^2=0`.
The exhaustive finite construction gives 378 pair-complexes and 288 reversible
exchanges. For an arbitrary orientation let
`nu_r=e_k+e_l-e_i-e_j` and assign the same rate `kappa_r>0` to both directions.
Every rate is fixed independently of the small scaling parameter. The parent
[collision and equilibration note](SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md)
defines the corresponding mass-action model. Only its finite collision contract
is used here; no nonlinear persistence theorem is required in the present proof.

Fix `0<theta<1` and the unit-mass product equilibrium

\[
 M_\theta(v)=\prod_{a=1}^3
 \begin{cases}\theta/2,&v_a=\pm1,\\1-\theta,&v_a=0.\end{cases}
 \qquad W=\operatorname{diag}M_\theta.
\tag{3}
\]

It is proportional to `(theta/[2(1-theta)])^e`, so (2) gives
`M_i M_j=M_k M_l`. Linearizing `f=M(1+h)` about this equilibrium gives

\[
 C=\sum_r\kappa_r M_iM_j\nu_r\nu_r^T,
 \qquad B=W^{-1}C,
 \qquad \partial_t h=-Bh.
\tag{4}
\]

Use the complex weighted inner product
`<g,h>_M=sum_v M_v conjugate(g_v)h_v`. Then `B` is self-adjoint and
nonnegative. Its kernel is exactly

\[
 K=\operatorname{span}\{1,v_x,v_y,v_z,e\}.
\tag{5}
\]

For completeness, a collision invariant `psi` has zero mixed finite difference
on every coordinate rectangle: the exchange
`(x,y,z)+(x',y',z) <-> (x,y',z)+(x',y,z)` is in (2). Applying this in every
coordinate pair makes `psi` a sum of three one-coordinate functions and a
constant. Each function on `{-1,0,1}` is quadratic, so
`psi=a+b·v+sum_a c_a v_a^2`. The exchanges between `(+e_a,-e_a)` and
`(+e_b,-e_b)` force all `c_a` equal. The five functions in (5) are independent
and conserved. Since every coefficient in (4) is positive, equality in its
quadratic form is precisely this invariant condition. Thus `rank B=22`.

Let `P` be the weighted orthogonal projector onto `K`, `Q=I-P`, and

\[
 R=(B|_{K^\perp})^{-1}Q=(B+P)^{-1}-P,
 \quad BR=RB=Q,\quad PR=RP=0,
 \quad b=\|R\|_M=1/\lambda>0.
\tag{6}
\]

Here `lambda` is the least positive eigenvalue of `B`. This is a finite,
explicitly specified constant. At `theta=1/3`, a rational inverse for unit
rates gives the useful bound

\[
 b\leq \frac{b_*}{\kappa_{\min}},\qquad
 b_*:=\operatorname{tr}R_{\kappa=1}
 =\frac{6224911145567}{509693499350}.
\tag{7}
\]

Indeed `B_kappa >= kappa_min B_1` in the weighted quadratic form on
`K^perp`, and the largest eigenvalue of the positive inverse is at most its
trace. No constant is asserted uniform as `theta` approaches 0 or 1 or as a
positive rate approaches zero.

## 2. Streaming, function spaces and the five macroscopic fields

Supply the periodic continuum domain
`T^3=(R/(2 pi Z))^3`, normalized spatial measure, and

\[
 T h(v,x)=v\cdot\nabla_xh(v,x).
\tag{8}
\]

This streaming operator is skew-adjoint. The torus is a supplied domain;
there is no spatial lattice-refinement argument in this note. For a Fourier
series with frequencies `k in Z^3`, define

\[
 \|h\|_{H_M^s}^2=\sum_k(1+|k|^2)^s\|\widehat h(k)\|_M^2,
 \qquad
 \|h\|_{\dot H_M^s}^2=\sum_k|k|^{2s}\|\widehat h(k)\|_M^2.
\tag{9}
\]

Write `||.||=||.||_{L_M^2}`. Constant matrices `P,Q,R` act pointwise. With
`c=sqrt(3)`, their relevant bounds are

\[
 \|P\|,\|Q\|\leq1,\quad \|R\|=b,\quad
 \|Th\|_{\dot H_M^s}\leq c\|h\|_{\dot H_M^{s+1}}.
\tag{10}
\]

For each positive scaling parameter, the Fourier matrices
`-i diag(v·k)-B/epsilon` and `-i diag(v·k)/delta-B/delta^2`
are dissipative in this weighted norm. Their matrix exponentials give unique
contractive kinetic semigroups in every `H_M^s`. Fourier truncation and the
contraction bound justify their extension from smooth data.

For `U=PU`, use the moment coordinates

\[
 \rho=\langle1,U\rangle_M,\quad j_a=\langle v_a,U\rangle_M,
 \quad E=\langle e,U\rangle_M,\quad
 \vartheta=\frac{E-3\theta\rho}{3},\quad
 \beta=\frac{\vartheta}{\theta(1-\theta)}.
\tag{11}
\]

These are supplied linear fluctuation variables. In particular `vartheta` is a
perturbation of the Gibbs variance parameter, not an identified physical
temperature. Direct product moments give

\[
 U=\rho+\frac{j\cdot v}{\theta}+\beta(e-3\theta),
 \qquad
 \|U\|_M^2=|\rho|^2+\frac{|j|^2}{\theta}
       +\frac{|E-3\theta\rho|^2}{3\theta(1-\theta)}.
\tag{12}
\]

The last equality also specifies exactly the field norm in Theorem 2.
The identities `P(v_a v_b)=delta_ab e/3` and
`P(e v_a)=(1+2 theta)v_a` show that `U_t+PTU=0` is

\[
 \rho_t+\nabla\!\cdot j=0,\quad
 j_t+\tfrac13\nabla E=0,\quad
 E_t+(1+2\theta)\nabla\!\cdot j=0.
\tag{13}
\]

Its sound speed squared is `(1+2 theta)/3`, hence `5/9` at `theta=1/3`.
This energy-conserving acoustic system includes an entropy mode; it is not an
isothermal identification of pressure with density.

## 3. Complete first constitutive correction

Define the symmetric trace-free strain and the three microscopic heat sources

\[
 D(j)=\frac{\nabla j+(\nabla j)^T}{2}
              -\frac{\nabla\!\cdot j}{3}I,\qquad
 H_a(v)=v_a(e-1-2\theta),\quad \phi_D(v)=v^TDv.
\tag{14}
\]

Here the convention for `nabla j` is `(nabla j)_ab=partial_a j_b`;
symmetrization removes any convention issue. Both `phi_D` and `H_a` lie in
`K^perp`. Projection of the streaming source gives the exact identity

\[
 QTU=\frac1\theta\phi_{D(j)}+\sum_aH_a\partial_a\beta.
\tag{15}
\]

For arbitrary positive rates, put `w=-RTU`. Its mass-flux correction is zero,
and its stress `Sigma_ab=<v_a v_b,w>_M` is symmetric and trace-free. Its
energy-flux correction is `q_a=<e v_a,w>_M=<H_a,w>_M`. The complete formula is

\[
 \begin{aligned}
 \operatorname{tr}(F\Sigma)
 &=-\theta^{-1}\langle\phi_F,R\phi_{D(j)}\rangle_M
   -\sum_a\langle\phi_F,RH_a\rangle_M\partial_a\beta,\\
 q_a&=-\theta^{-1}\langle H_a,R\phi_{D(j)}\rangle_M
      -\sum_b\langle H_a,RH_b\rangle_M\partial_b\beta
 \end{aligned}
\tag{16}
\]

for every real symmetric trace-free `F`. These equations also cover rates that
break inversion symmetry, when mixed stress/heat coefficients may be present.
The eight-source response matrix is symmetric nonnegative because `R` is.
There is no independent bulk-stress response: `e` is an exact invariant and
`<e,w>_M=0`.

If the rates are invariant under all signed coordinate permutations, mixed
stress/heat terms vanish by parity. The heat response is `chi delta_ab`, and
the stress form on real symmetric trace-free tensors `D,F` has precisely two
coefficients:

\[
 \langle\phi_D,R\phi_F\rangle_M
 =2\mu_D\operatorname{tr}(D_{\rm diag}F_{\rm diag})
  +2\mu_O\operatorname{tr}(D_{\rm off}F_{\rm off}),
 \qquad \langle H_a,RH_b\rangle_M=\chi\delta_{ab}.
\tag{17}
\]

For complex fields the constitutive map extends complex-linearly, and the
associated energy form uses complex conjugation in its first tensor argument.

To see completeness, coordinate sign changes kill diagonal/off-diagonal
cross terms and cross terms between distinct off-diagonal pairs. Permutations
equate the three remaining off-diagonal coefficients. A permutation-invariant
form on diagonal tensors is a combination of `sum_a D_aa F_aa` and
`tr D tr F`; the latter vanishes on the trace-free plane. The representatives
`diag(1/2,-1/2,0)` and `F_xy=F_yx=1/2` both have squared trace norm `1/2`.
Thus their responses determine all five stress components, with the factors
in (17). The positive coefficients are

\[
 \mu_D=\langle(v_x^2-v_y^2)/2,R((v_x^2-v_y^2)/2)\rangle_M,
 \quad \mu_O=\langle v_xv_y,R(v_xv_y)\rangle_M,
 \quad \chi=\langle H_x,RH_x\rangle_M.
\tag{18}
\]

Consequently

\[
 \Sigma=-\frac2\theta[\mu_DD_{\rm diag}(j)+\mu_OD_{\rm off}(j)],
 \qquad q=-\chi\nabla\beta.
\tag{19}
\]

The dissipative macro equation

\[
 U_t+PTU=\varepsilon PTRTU,\qquad PU=U
\tag{20}
\]

therefore has, for cubic rates, the complete component form

\[
 \begin{aligned}
 \rho_t+\nabla\!\cdot j&=0,\\
 j_t+\tfrac13\nabla E
  &=\frac{2\varepsilon}{\theta}\nabla\!\cdot
       [\mu_DD_{\rm diag}(j)+\mu_OD_{\rm off}(j)],\\
 E_t+(1+2\theta)\nabla\!\cdot j
  &=\frac{\varepsilon\chi}{3\theta(1-\theta)}
       \Delta(E-3\theta\rho).
 \end{aligned}
\tag{21}
\]

For general rates the fluxes in (16) replace (19). In every case

\[
 \tfrac12\frac d{dt}\|U\|^2
   =-\varepsilon\langle TU,RTU\rangle_{L_M^2}\leq0.
\tag{22}
\]

For cubic rates the integrand is
`(2/theta^2)[mu_D |D_diag|^2+mu_O |D_off|^2]+chi |grad beta|^2`.
The same contraction holds in each Sobolev norm. Cubic symmetry alone does
not make the stress rotationally isotropic; that requires `mu_D=mu_O`.

## 4. Exact responses of the nine-rate family

Now fix `theta=1/3`. Among the 288 reactions distinguish the nine exchanges

\[
 \{w+e_a,w-e_a\}\longleftrightarrow
 \{w+e_b,w-e_b\},\qquad a<b,\quad w_a=w_b=0,
\tag{23}
\]

where the remaining coordinate of `w` is `-1,0,1`. Give these reactions rate
`alpha>0`, all others rate 1. This rule has full signed-permutation symmetry.
It preserves all five invariants and detailed balance.

The stress pairs
`Phi_D=(d,d v_z^2)`, `d=(v_x^2-v_y^2)/2`, and
`Phi_O=(o,o v_z^2)`, `o=v_x v_y`, have the same Gram matrix

\[
 S=\Phi^TW\Phi=\begin{pmatrix}1/9&1/27\\1/27&1/27\end{pmatrix}.
\tag{24}
\]

Their invariant collision blocks `B Phi=Phi D` are

\[
 D_D=\begin{pmatrix}4(\alpha+1)/9&-5/18\\2/3-\alpha/3&\alpha/9+35/18\end{pmatrix},
 \qquad
 D_O=\begin{pmatrix}16/9&-2/9\\1/18&5/2\end{pmatrix}.
\tag{25}
\]

Equivalently their weighted dissipation matrices are

\[
 H_D=S D_D=
 \begin{pmatrix}(\alpha+2)/27&(\alpha+10)/243\\
 (\alpha+10)/243&(\alpha+15)/243\end{pmatrix},\qquad
 H_O=\begin{pmatrix}97/486&11/162\\11/162&41/486\end{pmatrix}.
\tag{26}
\]

The heat pair `Phi_H=(H_x,J_x)`, with
`H_x=v_x(e-5/3)` and `J_x=v_x(v_y^2 v_z^2-1/9)`, has

\[
 S_H=\begin{pmatrix}4/27&4/81\\4/81&8/243\end{pmatrix},\quad
 D_H=\begin{pmatrix}79/54&-2/9\\5/9&5/2\end{pmatrix},\quad
 H_H=S_HD_H=\begin{pmatrix}178/729&22/243\\22/243&52/729\end{pmatrix}.
\tag{27}
\]

Here `B Phi_H=Phi_H D_H`, independent of `alpha`. These are identities in all
27 velocity entries, not closed-subspace assumptions. One direct reproduction
method is to apply to each column `phi` the flux derivative

\[
 (B\phi)_i\mathrel{+}=\frac{\kappa M_iM_j}{M_i}
   (\phi_i+\phi_j-\phi_k-\phi_l),
\tag{28}
\]

with the corresponding plus sign at `j` and minus signs at `k,l`, divided
by their respective weights. Enumerating the 288 reactions evaluates the
left side exactly. Both sides of each block identity are affine in `alpha`;
the runner verifies their two coefficients at `alpha=0,1`, all coordinate
permutations, and both direct-flux and matrix implementations. Using zero
only to certify an affine coefficient does not apply a positive-rate theorem
at zero. Thus these finite identities hold for every `alpha`, and the inverse
statements below use `alpha>0`.

If `s` is the first column of a Gram matrix, the response of its first source
is `s^T H^{-1}s`. In particular

\[
 \det H_D=\frac{8\alpha^2+133\alpha+170}{59049},\quad
 s^T\operatorname{adj}(H_D)s=\frac{4\alpha+31}{59049},
\]
\[
 \boxed{\mu_D(\alpha)=\frac{4\alpha+31}{8\alpha^2+133\alpha+170},\quad
 \mu_O=\frac{67}{1083},\quad\chi=\frac{40}{441}.}
\tag{29}
\]

Equations (17) and (29) are the full traceless stress and heat responses, not
just two selected stress entries. For unit rates, `mu_D=35/311` differs from
`mu_O`. Equality holds at the unique positive root

\[
 \alpha_* =\frac{-4579+3\sqrt{7614177}}{1072},\qquad
 536\alpha_*^2+4579\alpha_*-22183=0,
 \quad 1<\alpha_*<4.
\tag{30}
\]

The quadratic has negative constant term and positive leading coefficient,
so exactly one root is positive. Its values at 1 and 4 have opposite signs.
All rates at `alpha_*` are therefore at least 1, so (7) gives `b<=b_*`.
At this supplied rate the constitutive differential operator is rotationally
isotropic, with

\[
 \nu=\mu_O/\theta=\frac{67}{361},\qquad
 \Sigma=-2\nu D(j),\qquad q=-\frac{20}{147}\nabla(E-\rho)
                =-\frac{20}{49}\nabla\vartheta,
\tag{31}
\]
\[
 \begin{aligned}
 \rho_t+\nabla\!\cdot j&=0,\\
 j_t+\tfrac13\nabla E
  &=\varepsilon\nu(\Delta j+\tfrac13\nabla\nabla\!\cdot j),\\
 E_t+\tfrac53\nabla\!\cdot j
  &=\varepsilon\tfrac{20}{147}\Delta(E-\rho).
 \end{aligned}
\tag{32}
\]

The energy convention is `e=|v|^2`, not `|v|^2/2`; (31) uses that convention
throughout. The statement concerns the linear constitutive tensors, not
rotational invariance of the full discrete-velocity collision operator or of
all higher moments. Multiplying all supplied rates rescales the responses;
no physical viscosity or clock normalization has been obtained.

## 5. Theorem 1: a diffusive-time linear Stokes/heat limit

Use `theta=1/3`, `alpha=alpha_*`, and let

\[
 D_\rho=\frac4{49},\qquad \nu=\frac{67}{361},\qquad d=\nu=\max(D_\rho,\nu),
 \qquad a=cb+D_\rho\sqrt{6/5},\quad c=\sqrt3.
\tag{33}
\]

Choose real or complex periodic `rho_0,j_0` with `div j_0=0`, and set

\[
 U_0=\rho_0\frac{5-3e}{2}+3j_0\cdot v\ \in H_M^4.
\tag{34}
\]

Let `U(tau)=rho(tau)(5-3e)/2+3j(tau)·v`, where `rho,j` solve (1) with these
initial data. This subspace has `E=0`; nonzero constant density and momentum
means are allowed. The theorem does not require arbitrary initial acoustic
data to converge to (1). For each `0<delta<=1`, let

\[
 \partial_\tau h^\delta+\delta^{-1}Th^\delta
          +\delta^{-2}Bh^\delta=0,\qquad h^\delta(0)=U_0.
\tag{35}
\]

For `N_s=||U_0||_{dot H_M^s}` and every fixed `L<infinity`,

\[
 \boxed{
 \sup_{0\leq\tau\leq L}\|h^\delta(\tau)-U(\tau)\|
 \leq \delta\{2aN_1+L a(d+bc^2)N_3\}
       +\delta^2\{2bcaN_2+L bca dN_4\}.}
\tag{36}
\]

The constants are independent of `delta`. Replacing `b` by `b_*` gives fully
specified finite upper bounds. The estimate proves uniform strong `L_M^2`
convergence on every bounded interval of diffusive time. It also controls
the five projected moments. It is not a claim of an error uniform for
unbounded `L` or for arbitrary unsuppressed acoustic initial data.

**Proof.** The two heat semigroups in (1) contract every Sobolev norm and
preserve `div j=0`. On this subspace (12) is

\[
 \|U\|_M^2=\tfrac52|\rho|^2+3|j|^2,
 \quad PTU=0,\quad
 \|U_\tau\|_{\dot H_M^s}\leq d N_{s+2}.
\tag{37}
\]

Define the explicit macroscopic and kinetic correctors

\[
 m=-3D_\rho v\cdot\nabla\rho\in K,\qquad
 w=-RTU+m,\qquad z=-RTw\in K^\perp.
\tag{38}
\]

No inverse of the acoustic streaming operator is needed here. First,
`TU+Bw=PTU=0`. Second,

\[
 U_\tau+PTw=U_\tau-PTRTU+PTm=0.
\tag{39}
\]

To check every component of (39), `PTRTU` has moment coordinates
`(0, nu Delta j, -(20/147)Delta rho)` by (32). The moment coordinates of
`PTm` are `(-D_rho Delta rho,0,-(5/3)D_rho Delta rho)`.
Those of `U_tau` are `(D_rho Delta rho,nu Delta j,0)`.
The identity is exactly `(5/3)D_rho=20/147`. Thus
`U_tau+Tw+Bz=0` as a full 27-component identity, since `Bz=-QTw`.

For `H_app=U+delta w+delta^2 z`, direct substitution into (35) now gives

\[
 (\partial_\tau+T/\delta+B/\delta^2)H_{\rm app}
       =\delta(w_\tau+Tz)+\delta^2z_\tau.
\tag{40}
\]

This is an exact residual, without discarded asymptotic terms. From (37),
`||rho||_{dot H^s}<=sqrt(2/5)N_s` and
`||m||_{dot H_M^s}<=D_rho sqrt(6/5)N_{s+1}`. Consequently

\[
 \begin{aligned}
 \|w\|&\leq aN_1,&\quad \|z\|&\leq bcaN_2,\\
 \|w_\tau+Tz\|&\leq a(d+bc^2)N_3,&
 \|z_\tau\|&\leq bca dN_4.
 \end{aligned}
\tag{41}
\]

All these bounds hold uniformly in time. More explicitly
`||w_tau||<=a d N_3` and `||Tz||<=bc^2 a N_3`;
`z_tau=-RT w_tau` accounts for the fourth derivative. `H^4` data give the
corrector regularity needed for (40) in `L_M^2`: `w` is continuous in `H^3`,
`z` in `H^2`, `w_tau` in `H^1`, and `z_tau` in `L^2`.
Fourier truncation gives the identity first for smooth data and passage to
the limit in these norms.

The kinetic semigroup is contractive. Its difference from `H_app` at zero
is `-delta w(0)-delta^2 z(0)`. Duhamel's formula, (40), and (41) bound that
difference by the initial correctors plus the integrated residual. Adding
`||H_app-U||<=delta||w||+delta^2||z||` proves (36). The factors 2 in (36)
account separately for initial and final correctors. This completes the proof.

Theorem 1 supplies a dissipative linear fluid limit on times of order
`1/delta` in the associated acoustic scale. It does not establish a nonlinear
Navier–Stokes equation, positivity of a nonlinear distribution, or any limit
in which the velocity set is refined.

## 6. Theorem 2: order epsilon squared on finite acoustic times

This theorem applies to **every** fixed `theta in (0,1)` and every set of
fixed positive rates in (2), without cubic symmetry. Let `U_0=PU_0 in H_M^5`
and let `U=U^epsilon` solve (20) with `U(0)=U_0`, for `0<epsilon<=1`.
Its Fourier generator on `K` is
`-iP diag(v·k)P-epsilon P diag(v·k)R diag(v·k)P`, so it is contractive in
every Sobolev norm. Set

\[
 w=-RTU,\qquad
 z=-R(w_t+QTw)=R^2TU_t+RQTRTU.
\tag{42}
\]

Let `h^epsilon` be the exact solution

\[
 h_t^\varepsilon+Th^\varepsilon+B h^\varepsilon/\varepsilon=0,
 \qquad h^\varepsilon(0)=U_0-\varepsilon RTU_0.
\tag{43}
\]

This is explicit first-order preparation, and its five initial moments equal
those of `U_0`. No second corrector is required in the initial datum.
Put `N_s=||U_0||_{dot H_M^s}` and define

\[
 \begin{aligned}
 Z_\varepsilon&=2b^2c^2N_2+\varepsilon b^3c^3N_3,\\
 Y_\varepsilon&=4b^2c^3N_3+4\varepsilon b^3c^4N_4
                      +\varepsilon^2b^4c^5N_5.
 \end{aligned}
\tag{44}
\]

For any fixed `L<infinity`,

\[
 \boxed{\sup_{0\leq t\leq L}\|Ph^\varepsilon-U\|
        \leq\varepsilon^2(Z_\varepsilon+L Y_\varepsilon),}
\tag{45}
\]
\[
 \boxed{\sup_{0\leq t\leq L}\|h^\varepsilon-(U+\varepsilon w)\|
        \leq\varepsilon^2(2Z_\varepsilon+L Y_\varepsilon).}
\tag{46}
\]

Replacing every explicit `epsilon` inside (44) by 1 gives constants uniform
over `(0,1]`. An additional initial error of norm at most `epsilon^2 I_0`
adds `epsilon^2 I_0` to both bounds. If instead one uses the fully specified
second-order preparation `U_0+epsilon w(0)+epsilon^2 z(0)`, the initial
`Z_epsilon` term is removed from each bound. Preparation in (43) is sufficient
for this proof; necessity for the projected-field estimate is not claimed.

**Proof.** Write `A_epsilon=-PT+epsilon PTRT` on `K`. Sobolev contraction and
(10) give

\[
 \begin{aligned}
 \|U_t\|_{\dot H_M^s}
 &\leq c N_{s+1}+\varepsilon c^2bN_{s+2},\\
 \|U_{tt}\|_{\dot H_M^s}
 &\leq c^2N_{s+2}+2\varepsilon c^3bN_{s+3}
                         +\varepsilon^2c^4b^2N_{s+4}.
 \end{aligned}
\tag{47}
\]

The second inequality bounds both orderings in the cross term of
`A_epsilon^2`; it does not assume the streaming and collision matrices
commute. The norms on the right can also be read as the corresponding
time-dependent norms of `U`, bounded by their initial values.

Because `Bw=-QTU`, inserting `U+epsilon w` into the full kinetic operator gives

\[
 (\partial_t+T+B/\varepsilon)(U+\varepsilon w)
       =\varepsilon(w_t+QTw).
\tag{48}
\]

The macro part cancels exactly by (20). `w_t+QTw` lies in `K^perp`, so
`Bz=-(w_t+QTw)`. Therefore, for `H_app=U+epsilon w+epsilon^2 z`,

\[
 (\partial_t+T+B/\varepsilon)H_{\rm app}
       =\varepsilon^2(z_t+Tz).
\tag{49}
\]

The first formula in (42), without commuting `R` past `T`, gives

\[
 \|z\|\leq b^2c\|U_t\|_{\dot H_M^1}+b^2c^2N_2
                 \leq Z_\varepsilon,
\]
\[
 \begin{aligned}
 \|z_t+Tz\|
 &\leq b^2c\|U_{tt}\|_{\dot H_M^1}
       +2b^2c^2\|U_t\|_{\dot H_M^2}+b^2c^3N_3\\
 &\leq Y_\varepsilon.
 \end{aligned}
\tag{50}
\]

In the second bound, the two middle contributions are respectively
`RQTRTU_t` and `TR^2TU_t`; their orderings are retained. This verifies all
constants in (44). With `H^5` initial data, `U_t` is continuous in `H^3`,
`U_tt` in `H^1`, `z` in `H^2`, and `z_t+Tz` in `L^2`. Thus (49) is a
valid strong `L^2` residual, also obtainable by Fourier truncation.

At zero, `h^epsilon-H_app=-epsilon^2 z(0)`. Contraction and Duhamel yield
`||h^epsilon-H_app||<=epsilon^2(Z_epsilon+tY_epsilon)`. Since `Pw=Pz=0`,
projection gives (45). Adding `epsilon^2||z||` gives (46). The statements
about extra initial error and second-order preparation follow from the same
contraction bound. This proves the theorem for all Fourier modes together;
the finite Fourier runner check is a certificate of the cancellation, not a
substitute for this Sobolev argument.

The distinction in (46) is necessary for the stated comparison: whenever
`RTU_0` is nonzero, its prepared datum already has
`||h^epsilon(0)-U_0||=epsilon||RTU_0||`, giving an exact order `epsilon` initial distance from the
**uncorrected full distribution** for this class of data.
This explicit observation makes no exclusion claim about other initial-layer
formulations or other kinetic models. The linear fluctuation equation also
places no positivity requirement on `h`; a nonlinear nonnegative population
approximation is a different theorem.

## 7. An exact next nonlinear moment test

The linear theorems leave a concrete nonlinear closure question. At
`theta=1/3` take the slow local fluctuation

\[
 U=\rho A+3j\cdot v,\qquad A=(5-3e)/2,\qquad
 \eta=E-\tfrac53\rho=-\tfrac53\rho.
\tag{51}
\]

Here `E=0`; the last equality holds only on this slow subspace. Direct finite
moments are

\[
 \langle e v_i^2\rangle_M=\frac59,\qquad
 \langle e^2v_i^2\rangle_M=\frac{29}{27},\qquad
 \langle v_i^2(e-5/3)^2\rangle_M=\frac4{27}.
\tag{52}
\]

Since `A=-(3/2)(e-5/3)`, parity and (52) give the exact polynomial identity

\[
 \left\langle(e-5/3)v_i\,\frac{U^2}{2}\right\rangle_M
       =-\frac23\rho j_i=\frac25\eta j_i.
\tag{53}
\]

The fourth moments `E[v_i^4]=1/3`, `E[v_i^2v_j^2]=1/9` for `i!=j` also give

\[
 \left\langle\left(v_iv_j-\frac{\delta_{ij}}3e\right)
                     \frac{U^2}{2}\right\rangle_M
       =j_i j_j-\frac{|j|^2}{3}\delta_{ij}.
\tag{54}
\]

Every density-squared and density/momentum or momentum/momentum coefficient
not displayed in these two identities vanishes as specified by parity and
trace removal; the runner checks all coefficients, not selected field values.
The expressions `U^2/2` arise as the quadratic term in a local exponential
equilibrium expansion. Adding a `K`-valued second-order coordinate correction
does not change (53) or (54), whose test functions lie in `K^perp`.

If a nonlinear solvability calculation uses this slow variable `eta` and
these quadratic equilibrium fluxes, its normalized entropy advection term has
coefficient `2/5`, while the momentum convection coefficient in (54) is 1.
That conditional comparison identifies an exact next test for a proposed
nonlinear fluid closure. It does not prove a nonlinear hydrodynamic limit,
identify physical entropy, or rule out other moment choices, scalings, velocity
sets or physical dynamics. The rate adjustment in (30) does not change these
equilibrium moment identities.

## 8. Evidence, remaining interfaces and later formal work

The runner uses the Python standard library and no input file, network,
empirical data or mutable cache. Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/d3q27_dissipative_hydrodynamic_approximation_2026_10_09.py
```

It declares `AUDIT_TIMEOUT_SEC = 180` for the repository's runner-cache
envelope. Its exact checks cover two exhaustive reaction enumerations,
conservation, balance, the full rank/inverse certificate, all 48 cubic
symmetries, the all-rate block identities, all stress/heat components, complete
linear fluxes, polynomial corrector cancellations, slow-field solvability,
and the quadratic moment witness. Omitting a real axial reaction, reversing
the dissipative macro sign, and replacing the density diffusivity by the
energy-flux coefficient are distinct failing controls. A supplementary
floating-point matrix-exponential calculation distinguishes order-two
projected/corrected errors from an order-one uncorrected error on a specified
Fourier mode. It supplies neither a rigorous floating-point enclosure nor an
all-mode proof; those roles are separated from the analytic estimates above.

The earlier collision investigation independently checked full constrained
Poisson solves at four rational rates. Those checks support finite algebra at
those rates; they do not by themselves prove the all-rate identities or either
PDE estimate. Selective independent derivations in this branch packet examine
the corrector arguments and finite moments. Author checks, selective review
and a later retained-status audit are distinct evidence classes. No external
proof rebuild or Lean prerequisite is used to license these proposed proofs.

For a native kinetic/hydrodynamic derivation, the next interface must specify
the actual microscopic dynamics, its excitation observables, conserved
quantities, time scale and local collision/streaming approximation error. It
must explain the stress tensor and rate normalization or predict their
departure from (30). The original Lane 7 language about an additive scalar
Record readout is a target description; this note does not adopt that extra
structure as an axiom. Nonlinear amplitude estimates, boundary layers,
large-time uniformity and any velocity-refinement limit are separate
mathematical obligations, not consequences of (36) or (45).

Concrete later Lean/formal targets are: the 288-reaction finite enumeration
and invariant kernel; weighted projection and inverse identities; the three
two-dimensional blocks and isotropy polynomial; the eight-source constitutive
map; the two exact corrector residuals; Fourier semigroup contraction and
the stated Sobolev/Duhamel bounds. Formalization would strengthen proof
checking of the declared model. It would not identify that model with the
framework's native physical dynamics.


```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Control the approximation from finite-velocity collisions to dissipative macroscopic transport."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Test the actual native collision/streaming interface and derive a nonlinear limit with its exact thermal moments."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Linear kinetic limits and constitutive identities under explicit supplied-model conditions."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
