# Local volume dynamics with commuting electric terms and finite-rate birth

Root analytic candidate, 2026-09-23, before independent reconstruction.
This extends the explicitly compensated **limiting target**, not the original
Hamiltonian and not the microscopic approximation uniformly in volume.
Physical selection of the compensation and of the formation instrument is
still supplied. A dynamics limit is not a phase theorem or emergent relativity.

## 1. Algebra and finite-volume target

Fix the nearest-neighbor bipartite graph Z^d, d>=2, with degree z=2d. Regard
vertices and links as cells of its incidence graph. At each A vertex the
effective P-space has charges +1,-1; at each B vertex it has 0,+1,-1. Each
oriented link is a rotor l²(Z), with integer E and unit translation U. For a
finite cell set X use B(H_X), with the usual normal embeddings into larger
finite tensor Hilbert spaces. Take the norm completion of this local net as
the quasi-local observable algebra. Normal local matrix algebras are used;
no unjustified norm density of finite sums of product operators is required.

The previously constructed compensated target on a finite induced bipartite
graph G has, on its P space,

    h_G = K D_G - 2delta sum_(a<c sharing a B neighbor) S_ac* S_ac,
    S_ac=F_c F_a P,
    D_G=sum_(e=(a,b), a in A) (1-n_b) E_e(E_e+k_e(q_a)),        (1)

where k_e=-q_a if the chosen orientation is a to b, and +q_a otherwise.
Its resolved jump is L_(e,sigma)=sqrt(kappa) P j_(e,sigma) F_a P; use the
stipulated coherent sum instead if that is the selected instrument. The
compositions in (1) are local operators on the effective A/B tensor spaces:
one can use an auxiliary vacant A state to define F, then compress the local
composition. No infinite product of P projectors occurs in these definitions.

The diagonal summands D_e are nonnegative selfadjoint multiplication
operators because E(E+/-1)>=0 for integers. They strongly commute. A finite
sum D_G is selfadjoint on its maximal multiplication domain with finite
electric support as a core. All other terms are bounded. Each pair term has
norm at most 2|delta| z^4. Each resolved jump has norm at most
sqrt(kappa)(z-1); the coherent sum has norm at most twice this. The finite
Hamiltonian is selfadjoint on D(D_G). The associated density semigroup is
the mild Hamiltonian evolution with a bounded Lindblad perturbation. It is
normal, completely positive, trace preserving and strongly continuous on
trace class. General densities need not be in the generator domain.

Let T_t^G denote its unital completely positive Heisenberg dual, extended
as the identity on cells outside G. For any fixed bounded local observable
A_X and compact time interval, the following is proposed:

    T_t^G(A_X) -> T_t(A_X) in operator norm as G increases to Z^d,
    uniformly for 0<=t<=T.                                      (2)

The limit is independent of regular induced-box exhaustion or bounded local
boundary changes confined to a fixed boundary layer. It extends by contraction
to the quasi-local algebra as a unital completely positive semigroup. The
statement is norm convergence in **volume**, not norm continuity in time.

For a locally normal initial state omega, omega composed with T_t stays
locally normal, and t -> omega(T_t(A_X)) is continuous. Local Gauss constraints
are preserved. No global density matrix, finite global particle count or
first global birth time is asserted on the infinite lattice.

## 2. Remove the electric terms without growing an unlimited light cone

For a finite graph put alpha_t^G(A)=exp(it K D_G) A exp(-it K D_G).
If A is supported in X, then only D_e whose support meets X contributes.
All other factors commute with A and with those retained factors. Therefore

    alpha_t^G(A_X) is supported in X^(2),
    ||alpha_t^G(A_X)||=||A_X||.                                (3)

The radius is in the incidence metric. This support bound holds for every
t and every electric-field value, without a bound on the norm of D_e.
For G containing that neighborhood the expression is independent of G.
Mutual strong commutation is essential: one must not iterate neighborhoods
as though the electric factors could spread each other's support.

Conjugating each bounded Hamiltonian term and jump by alpha_t^G gives a
time-dependent local Lindblad generator in the interaction picture. Original
pair supports have incidence diameter at most8 and jump supports at most4.
The dressed diameters are at most12 and8 respectively. Their norms do not
change. Let ell_Z^G(t) be one dressed pair commutator or one dressed edge's
dissipator, grouping its actual sign channels. Uniformly in G and t,

    ||ell_Z^G(t)||_cb <= ell_0,
    ell_0=4|delta| z^4+8kappa(z-1)^2.                         (4)

There is a finite bound on the number Zeta of such indexed terms overlapping
any one term, depending only on d. A crude bound can count at most z² terms
per A anchor and all anchors within incidence distance16. The dressed support
has at most a dimension-dependent number of cells. In particular all constants
are independent of rotor cutoffs, G, and the unbounded size of K D_G.

The coefficients are strongly continuous, with strongly continuous adjoints.
They need not be norm-continuous. Thus one cannot simply invoke a theorem
requiring norm-continuous local generators without treating this distinction.

## 3. A bounded-locality estimate with the needed continuity topology

We use the finite-range bounded-Lindbladian locality argument of
[Barthel–Kliesch, arXiv:1111.4210v2, sections II–III,V and Appendix B](https://arxiv.org/abs/1111.4210v2).
For norm-continuous bounded local terms with range a and overlap Zeta, it
gives local-probe bounds proportional to exp(e Zeta ell_0 |t-s|-dist/a).
Its proof uses contractive completely positive propagators and paths of
overlapping term supports. The constants do not involve the local Hilbert
dimension. The related theorem of
[Nachtergaele–Vershynina–Zagrebnov, arXiv:1103.1122v2, Assumption1 and Theorems2–3](https://arxiv.org/abs/1103.1122v2)
explicitly assumes norm-continuous finite-volume generators. That assumption
is not asserted for the present interaction picture. The following approximation
supplies the extension actually needed here.

On each fixed finite volume, strongly continuous bounded h_Z(t),L_Z(t) and
their adjoints give a trace-norm-continuous map t -> ell_Z(t)_*(rho) for every
trace-class rho. First prove it for rank-one rho using strong convergence on
its two vectors; then use uniform operator bounds and finite-rank density.
The sum over the finite volume has a uniform-in-time bounded trace-class
operator norm. Its Picard series therefore defines a unique propagator on
trace class. All time integrals here are trace-class integrals of continuous
vectors, not assumed Bochner integrals of B(H)-norm-continuous coefficients.

Approximate time by a finite mesh and freeze each local Hamiltonian/jump at
the left endpoint. The resulting finite product of bounded constant GKLS
propagators is CPTP. It converges in trace norm on each fixed initial density,
uniformly on compact time intervals. Indeed the exact trajectory is a compact
set of trace-class vectors; strong pointwise convergence of the sampled
generators is uniform on this compact set by a finite-net argument and their
common bound. Duhamel/Gronwall then bounds the evolution error by the integral
of that vanishing discrepancy. The same applies to any subsystem generator.

For each time mesh, apply the bounded finite-range support-path proof on
the finitely many constant intervals; its integral recursion has the same
range, overlap and norm bound for every mesh. All arguments take place on
normal local maps, and their spatial amplifications have the cb bounds (4).
The proof uses commutation of disjoint maps and contractivity, both valid on
the full finite tensor B(H), including infinite-dimensional factors. A further
norm-continuous interpolation of the sampled GKLS generators can also be used:
convex interpolation retains support, complete dissipativity and the same
norm bound. Thus piecewise sampling introduces no new continuity premise.

Taking mesh size to zero gives ultraweak convergence of the dual propagators.
Every operator-norm locality bound survives this limit by testing all
trace-class functionals (equivalently weak-star lower semicontinuity of norm).
The same passage applies to comparisons of two finite volumes. This proves
the required dimension-independent locality estimates for the actual strongly
continuous rotor coefficients. It does not upgrade their time dependence
to norm continuity.

More explicitly, for a bounded normal local map Q_Y with Q_Y(I)=0,
the support-path recursion yields, with constants depending on the fixed
support and interaction overlap,

    ||Q_Y V^G(s,t)(A_X)||
       <= C_(X,Y) ||Q_Y||_cb ||A_X||
                          exp(v|t-s|-dist(X,Y)/a),             (5)

where a can be12 and v=e Zeta ell_0. For Y equal to one term's support,
the prefactor can be bounded by a constant times |X|, independent of its
position and G. V^G is the interaction-picture Heisenberg propagator.
Ordinary commutators are special cases. The trivial bound by
||Q_Y||_cb ||A_X|| is available as well. Constants are intentionally coarse;
no quantitative microscopic propagation speed is inferred.

## 4. Boundary comparison and the volume limit

Fix X and two volumes whose boundaries lie far away. The terminal observable
alpha_t^G(A_X) equals the same bounded local expression in both volumes once
they contain X^(2). In the interaction picture, their dressed generators
coincide throughout the common interior. Differences occur only in a boundary
layer of fixed thickness: incomplete stars and pairs are local, and the extra
electric conjugation adds only the neighborhood in (3). Each difference is
a sum of local maps annihilating I with bounded cb norm. It need not itself
be a positive generator; both propagators in Duhamel remain CPTP.

Apply Duhamel to the two bounded interaction-picture propagators. On the
left use contractivity; on each boundary source use (5). Cubic geometry
has only C_d(n+1)^(d-1) indexed supports in its nth distance shell about a
fixed cell. Summing first over X and then over boundary shells gives

 ||T_t^G(A_X)-T_t^H(A_X)||
    <= C_X ||A_X|| exp(vT)
          sum_(n>=floor(r/a)) (n+1)^(d-1) exp(-n),            (6)

for 0<=t<=T. Here r is the distance from X to the nearer boundary minus a
fixed geometric buffer. The buffer accounts for original star truncation
and (3). Constants and buffer depend on d and fixed coefficients, not the
volumes, time mesh, fields, or states. The shell sum tends to zero exponentially
up to a polynomial factor. The mesh argument of section3 makes (6) valid
before the volume limit; it is not a formal interchange of two unproved limits.

The actual induced-graph target and a truncation retaining only complete
infinite-graph stars/pairs may differ near the boundary. Both obey (4), agree
in the interior, and satisfy the same comparison. Thus (2) refers to the
target actually derived on finite graphs, not only to an unrelated boundary
Hamiltonian. More general boundary additions are allowed only when their
support/range and local cb density have uniform bounds. Arbitrarily strong
or nonlocal boundary driving is not covered.

Equation (6) proves a norm-Cauchy limit uniformly on compact times for every
local A. Uniform contraction extends it to the quasi-local algebra. Unitality
and complete positivity survive pointwise norm limits at each finite matrix
amplification. The semigroup law follows from the finite-volume law: for
A local, insert T_s(A) between T_t^G T_s^G(A) and T_t T_s(A), use contraction,
then approximate T_s(A) in norm by local observables. No assumption of norm
time continuity is needed for this argument.

## 5. States, Gauss constraints, and the time-continuity boundary

For fixed X the estimate (6) is uniform over its observable unit ball. If
omega is locally normal, omega composed with T_t^G restricted to B(H_X) is
a normal functional: the finite-volume map is normal and omega is normal
on that finite region. Those restrictions converge in functional norm by
(6). The normal functionals are norm closed, so the limiting state is locally
normal. Its expectation of every local observable is time-continuous because
the corresponding finite-volume expectation is, and convergence is uniform
on compact times. This is the physically used statewise continuity assertion.

The local Gauss operator is G_x=div E_x+1_A(x)-q_x. Its zero spectral projector
is bounded and local. Every hop path and birth shifts charge/field together;
D_e is diagonal and all gates commute with G_x. Consequently each local term
strongly commutes with the Gauss spectral projectors, which are fixed by
every finite-volume Heisenberg semigroup and by its limit. A locally normal
state satisfying each Gauss constraint therefore keeps that constraint.

Norm time continuity on all bounded local rotor observables is false in
general. Even in the initial all-A-plus sector, take a plaquette translation
W and a normalizable electric basis vector with circulation n around that
plaquette and zero elsewhere. The diagonal energy is 4K n². Translation
changes it by K(8n+4). At t_n=pi/[K(8n+4)] the matrix element of
alpha_(t_n)(W)-W has magnitude2 although t_n->0. These are gauge-compatible
electric words and W is gauge invariant. The free dynamics is not norm
continuous on W. Adding the uniformly bounded local terms changes its local
evolution by at most C_W t on a fixed short interval, using the same shell
sum/contractivity bound, so it cannot repair this norm-continuity countercontrol.
There is no contradiction with continuous expectations in each fixed normal
state; the maximizing electric vector changes with n.

The construction does not give a norm-continuous C*-dynamical semigroup on
the whole stated algebra. A smaller regular algebra or a locally normal
representation is needed if that additional property is desired. It also
does not require a uniform initial electric-energy bound for bounded local
expectations or their volume convergence. Energy moments and derivatives
of unbounded observables are separate obligations.

## 6. A local formation diagnostic on the infinite lattice

The initial all-A-plus, B-empty, zero-electric-field product state is locally
normal and satisfies Gauss. A resolved first mark on edge(a,b) has z-1
orthogonal outward destinations distinct from b. Hence its Gram on this
initial sector is (z-1)I. Opposite signs have distinct final charge words;
the coherent edge jump has Gram2(z-1)I. The initial rate of a monitored edge
is therefore 2kappa(z-1) in either convention. A fixed finite set of local
detectors can be included by finite classical mark/count registers; their
additional bounded local GKLS terms preserve the locality proof. No finite
total event rate for the entire infinite lattice is claimed.

In particular let n_b be occupation of one B site. It commutes with D, and
its generator image is bounded and local. Initially the Hamiltonian does
not change its expectation. Birth at b itself contributes 2kappa z(z-1),
and transfer of the old A record to b contributes the same amount. Thus

    d/dt omega_0(T_t(n_b)) at t=0+ =4kappa z(z-1).             (7)

This is a local initial derivative, not a late-time density equation. For
the cubic lattice z=6 it is120kappa; the total record-density derivative per
vertex is60kappa, since the A sites stay occupied and B is half the lattice.
The time evolution thereafter couples formation, transport and fields.
Saturation, stationarity, phases and an unlimited finite-resource record
supply do not follow from (7).

## 7. Required controls and remaining scope

Decisive controls should check the finite support and overlap counts after
electric dressing, the Gauss-compatible norm-continuity example, and the
local first-formation counting including coherent channels. A small numerical
volume study could corroborate (6), but cannot prove its unbounded-field or
infinite-volume assertion. Its proof is the topology-aware bounded-locality
argument above, conditional on the already checked finite-graph target.

The earlier spin-half local normal-form theorem used a prepared code and a
birth rate tending to zero. It is a different result and is not imported
as a fixed-rate rotor theorem here. The present claim takes the compensated
target first, then its spatial limit. The fixed-graph microscopic error
has not been made uniform in volume; no exchange of microscopic, large-spin
and spatial limits is licensed. There is no derived Coulomb/ordered phase,
photon dispersion, Lorentz symmetry, reservoir or native theory of everything.
