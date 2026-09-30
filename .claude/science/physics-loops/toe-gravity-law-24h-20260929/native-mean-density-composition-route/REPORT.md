# Mean-density energy, grand potential and the dilute onset slope

Author composition of source-bound checked inputs; new focused checking is
required before downstream use. No formal review, audit, retained status,
canonical fixed-N upper, condensate or phase statement is attached. The
actual supplied qubit Hamiltonian and its parameters remain unchanged.

For the definitions below, put

 t=min_(||z||=1)<z tensor z,T0 z tensor z> >0,       c=t/8.

The composition proves a thermodynamic MEAN-constrained energy e(rho) near
zero density and a thermodynamic grand potential g(nu), with

 e(rho)=(t/8)rho^2+o(rho^2),
 g(nu)=-(2/t)nu^2+o(nu^2),       nu down0.                       (1)

Every thermodynamic accumulation value of the mean density of a finite-
volume ground state of H0-nu N obeys, uniformly over the ground-state choice,

                      rho_gr(nu)=(4/t)nu+o(nu).                 (2)

The order is volume first, then rho or nu down to zero. No joint finite-size
rate is asserted. Equation(2) is a ratio/onset slope; it does not assert a
second derivative of g, a unique ground density at each positive nu, or a
compressibility function. The coefficient is the coherent minimum of the
FULL15 threshold form, not its smallest eigenvalue on arbitrary Sym^2 C5.
Its occurrence in the lower is proved through the finite-mode density-matrix
identity, not by assuming the many-body state is coherent.

## 1. Actual law, definitions and precise reused inputs

The carrier is one actual qubit per site of the cubic torus with V=L^3,
L>=5. Distinct-site operators commute; b_x=|0><1| and n_x=b_x^*b_x.
With graph offsets +/-2e_i and +/-e_i+/-e_j, set m_x=sum_(y~x)n_y and

 d_i(x)=b_(x+e_i)b_(x-e_i),
 v_ij^(s,t)(x)=s t b_(x+s e_i)b_(x+t e_j),
 Q_E1=(d1-d2)/sqrt2, Q_E2=(d1+d2-2d3)/sqrt6,
 Q_Tij=(1/2)sum_(s,t) v_ij^(s,t),

 H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)
          +mu sum_x n_x binom(m_x,2)
          +tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|^2,
 N=sum_x n_x,       mu,tau>0.                                   (3)

Here P_E and P_T are the corresponding sums of Q_A^*Q_A. These are the
supplied operators, not independently canonical pair fields. The unchanged
landed theorem gives H0>=0, H0 Omega=0 and the ALL-density bound

 H0>=c0 N(N-2)/V,       c0=min(tau,mu/12)/99090432>0.              (4)

In particular every density matrix Gamma satisfies

 Tr(Gamma H0)/V>=c0[rho^2-2rho/V],
                         rho=Tr(Gamma N)/V.                     (5)

This is not merely a dilute estimate. The original local grouping H0=sum h_x
has norm ||h_x||<=h_*=182mu+240tau and support inside x+[-2,2]^3 (at most
25 actual sites). Finite range and this bounded local norm will be used
only for the thermodynamic boundary comparison in section2.

Define, allowing ALL density matrices,

 e_L(rho)=min_{Gamma>=0,Tr Gamma=1,Tr(Gamma N)=rho V}
                                      Tr(Gamma H0)/V,
 g_L(nu)=V^-1 min spec(H0-nu N).                                 (6)

Thus e_L is a mean-number variational function. At noninteger rho V it can
use number mixtures, and it is not the exact-N sector energy. The finite
minimum exists. Since H0 commutes with N, dephasing in number leaves both
constraints and energy unchanged; e_L is the convex hull of the finitely
many sector ground energies. It is continuous and convex on[0,1], with

 e_L(0)=0,       0<=e_L(rho)<=h_*rho,
 g_L(nu)=min_(0<=rho<=1)[e_L(rho)-nu rho].                        (7)

The upper line uses the vacuum/fully occupied mixture. It does not claim
the actual fully occupied energy equals h_*.

Two source-bound scientific inputs supply the dilute coefficient:

* The checked actual-cell residual and particle-tail lower prove the uniform
  full-carrier lower liminf t/8, at volume then density order, for arbitrary
  states of that mean density. Their exact sources are976cfb69 and2e4d9f8b,
  with complete focused receipts3fbe2af3 and124091e9. All finite-cell, odd-
  sector, tail and fragmentation obligations are included there.
* The actual compact-correction upper report0c4ef9ac, independently checked
  before this composition, supplies exact finite-torus states

   psi_L(u)=exp(u^2 X_chi) exp[u(C_z^*-C_z)] Omega,
   C_z^*=sum_(x,A) z_A R_A(x)^*,
   R=(Q_E1,Q_E2,Q_T12/sqrt2,Q_T13/sqrt2,Q_T23/sqrt2),

  with compact physical four-site chi chosen before L and u. For every
  sufficiently large L and all real u,

   |Tr(H0 psi_L)/V-(t_chi/2)u^4|<=D_chi |u|^6,
   |Tr(N psi_L)/V-2u^2|<=B_chi u^4.                             (8)

  Expectation notation in(8) abbreviates the pure-state density matrix.
  The constants are finite and independent of L for fixed chi. For every
  epsilon>0 a finite chi exists with t<=t_chi<=t+epsilon, choosing a unit z
  attaining the compact-sphere minimum. The half factor comes from the
  actual incoming Phi=C_z^2 Omega/sqrt2 and physical orbit normalization.
  Neither an l2 threshold minimizer nor a global torus orbit isometry is
  presumed. The full unitary remainders, not truncated vectors, give(8).

The bounded finite Hermitian T0 and its strict positivity are the actual
physical K0,N4 threshold inputs. Source identities and precise roles are in
SOURCE_BINDINGS.json. The present author previously authored parts of the
lower and independently checked the older upper; this composition is not
an independent review of either.

## 2. Thermodynamic limits actually used

First prove the grand limit rather than assume it. Fix a bounded chemical-
potential interval |nu|<=nu_max. Tile a large torus by J=floor(L/ell)^3
complete cubes of side ell and a remainder. Replace H0-nu N by the sum of
J independent periodic ell-cube copies and zero on the remainder. Only
terms meeting block faces or the remainder change. A term centered farther
than two sites from a face is unchanged. The number of changed centers is
at most C[L^3/ell+ell L^2], and every changed local term has uniformly bounded
norm. Onsite chemical terms cost at most nu_max times the remainder volume.
Therefore the operator difference has norm at most

 C(h_*+nu_max)[L^3/ell+ell L^2].

The artificial periodic copies are used ONLY in this bounded-norm
thermodynamic comparison, not as physical lower cells in a dilute proof.
Their minimum energy adds because their Hilbert tensor factors are disjoint.
The variational principle gives a two-sided bound. Since |g_ell|<=h_*+nu_max
and Jell^3/L^3 differs from one by O(ell/L),

 sup_(|nu|<=nu_max)|g_L(nu)-g_ell(nu)|
             <=C(h_*+nu_max)[ell^-1+ell/L].                      (9)

For every fixed ell send L to infinity, then let ell grow. This makes g_L
uniformly Cauchy on the chosen interval. Hence a finite limit g(nu) exists
for every real nu, uniformly on compact nu intervals. It is concave and
1-Lipschitz because each g_L has those properties. The proof uses no
hypothesis on ground-state uniqueness or spatial order.

The mean-constrained limit near zero follows by elementary convex duality.
Nonnegativity, convexity and e_L(0)=0 imply e_L is nondecreasing. For
0<=rho<=1/2, its supporting slopes can be chosen in[0,2h_*]: every right
slope below1/2 is bounded by the secant to1, at most h_* /(1-rho).
The finite convex hull in(7) consequently has the exact representation

 e_L(rho)=sup_(0<=nu<=2h_*)[g_L(nu)+nu rho],       0<=rho<=1/2.

Uniform convergence in(9) implies uniform convergence of e_L on this
interval to

 e(rho)=sup_(0<=nu<=2h_*)[g(nu)+nu rho].                          (10)

This proves the claimed MEAN-constrained thermodynamic limit, not the
existence of an exact-N thermodynamic limit. The argument would extend to
any compact density interval below one with a larger bounded slope interval,
but that extension is unnecessary here. From(5), e(rho)>=c0 rho^2.

No thermodynamic rate in(9) is divided by a vanishing rho^2 or nu^2 at fixed
volume. Volume convergence occurs first throughout the dilute conclusions.

## 3. An upper at exactly the prescribed mean density

The old unitary trial's parameter density need not be monotone. Continuity
alone suffices. Fix epsilon, z and compact chi before all limits. Let
r_L(u)=<N>_(psi_L(u))/V. For a sufficiently small prescribed rho>0,

 r_L(0)=0,       r_L(sqrt rho)>=2rho-B_chi rho^2>=rho.

The intermediate value theorem supplies u_L in[0,sqrt rho] with
r_L(u_L)=rho exactly. Set s_L=u_L^2. Equation(8) then gives, uniformly in L,

 |s_L-rho/2|<=B_chi rho^2/2,
 e_L(rho)<= (t_chi/8)rho^2+C_chi rho^3.                          (11)

For example the energy error follows from s_L<=rho and
|s_L^2-rho^2/4|<=3B_chi rho^3/4. No fixed particle-number projection is used;
the exact state still has its actual sector distribution. For fixed chi,
let L tend to infinity, then rho down to zero, and only then improve its
threshold accuracy. This proves

 limsup_(rho down0)e(rho)/rho^2<=t/8.

The separately checked lower has exactly that mean-density/volume order
and applies to every e_L-minimizing state. Its energy-ceiling alternative
causes no gap: the upper(11) supplies a fixed O(rho^2) ceiling for small rho,
and states above such a ceiling already satisfy the lower comparison.
It follows that

                         e(rho)=c rho^2+o(rho^2).                (12)

This matching statement concerns the precisely defined convex mean-number
problem(6). It does not assert equality of a canonical fixed-N quantity.

## 4. Confinement of grand minimizers before the dilute optimization

For any finite-volume ground state Gamma_nu,L of H0-nu N with nu>0,
comparison with the vacuum gives g_L(nu)<=0. Combining with(5) yields

                 rho_nu,L <= nu/c0+2/V.                         (13)

This ALL-density step excludes a remote positive-density minimizer from
invalidating the dilute optimization. A lower known only near rho=0 would
not justify(13). For fixed sufficiently small nu, all thermodynamic density
accumulation values lie in[0,nu/c0], a subset of[0,1/2].

For clarity, take any sequence of finite-volume grand ground states and a
subsequence on which rho_nu,L converges to r. Such a subsequence exists by
boundedness. Uniform mean-energy convergence in(10) gives

 g(nu)=e(r)-nu r.

At finite volume the ground state attains e_L at its own mean; otherwise
a state of the same mean with lower H0 energy would lower H0-nu N. Uniform
convergence and continuity justify passing the moving mean to r. Conversely
for any fixed small density s, variational comparison gives

                        g(nu)<=e(s)-nu s.                       (14)

Given delta in(0,c), equation(12) bounds e(r) between(c-delta)r^2 and
(c+delta)r^2 for every sufficiently small r. Confinement(13) puts every
minimizing accumulation r in that range when nu is small. Minimizing the
lower quadratic over all r>=0, and testing(14) at
s=nu/[2(c+delta)], gives

 -nu^2/[4(c-delta)] <= g(nu) <= -nu^2/[4(c+delta)].                (15)

Now send nu down to zero and then delta down to zero. This proves the grand
asymptotic in(1). It also recovers directly the older variational upper
coefficient -2/t, now matched by a full-carrier lower. For nu<0, H0>=0
makes the finite-volume vacuum the unique ground state and g(nu)=0. At
nu=0, the coercivity or exact kernel makes all thermodynamic ground-density
accumulation values zero.

## 5. Ground-density slope from concave secants

No differentiability of g is needed. For any finite-volume ground state at
nu, using it as a trial at nu+h and nu-h gives, for0<h<nu,

 [g_L(nu-h)-g_L(nu)]/h <=rho_nu,L
                      <=[g_L(nu)-g_L(nu+h)]/h.                 (16)

The signs follow from the actual perturbation -nu N. Equation(16) is valid
for every density matrix supported on the ground eigenspace, including
mixtures of degenerate particle sectors. Let L grow and take any density
accumulation value rho_gr(nu); convergence of g_L preserves both bounds.
Set h=theta nu with fixed0<theta<1 and use g(nu)=-kappa nu^2+o(nu^2),
kappa=2/t. Then

 kappa(2-theta)+o(1) <=rho_gr(nu)/nu
                                  <=kappa(2+theta)+o(1).

First send nu down to zero, then theta down to zero. The bounds do not depend
on the choice of ground state or accumulation subsequence, proving(2).
Equivalently all concave supergradient densities -partial g(nu) have that
same leading ratio wherever they are considered. No derivative of those
densities or second derivative of g follows.

The corresponding internal H0 energy per volume in such grand ground-state
accumulations is g(nu)+nu rho_gr(nu)=(2/t)nu^2+o(nu^2). This is a consequence
of the exact identity H0=(H0-nu N)+nu N and the proven density ratio; it does
not identify the state, its polarization, correlations or excitations.

## 6. Scope and evidence

The upper used an exact finite-torus unitary and compact physical threshold
corrections. The lower used the actual full-carrier boundary, centered-
residual and total-particle-tail arguments; fragmentation was priced through
a finite5-mode identity. All-density coercivity then supplied the missing
confinement for grand optimization. No pair-boson substitution or assumed
condensate entered any of these steps.

This composition makes no exact-N upper claim, no canonical thermodynamic
existence assertion, no ODLRO or spontaneous-symmetry-breaking conclusion,
no selected tensor direction, and no physical record/common-source or
framework-Hamiltonian selection. mu,tau and the quantum state/expectation
rule remain supplied. No new T0 matrix entries or numerical error constants
were computed. Every new step here is analytic; no runner was executed.

CONTRACT.md was frozen before this complete proof. SOURCE_BINDINGS.json
binds the actual main/provisional sources and focused receipts, including
the author's prior role in the lower and prior independent role on the upper.
Root's separate canonical block-transfer candidate was not opened during
this composition and supplies no premise. This file requires a fresh focused
check before inclusion in any coherent milestone or downstream theorem.
