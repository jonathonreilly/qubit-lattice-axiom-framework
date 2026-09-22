# Uniform density control with active formation, and its dynamical limits

Date: 2026-09-22. Status: personally derived conditional theorem and finite
controls; independent reconstruction pending. This extends the supplied
hard-core record model. It is not a native-axiom derivation or an infinite
lattice photon theorem. The proof concerns density, not closeness of the
entire field evolution. No new general strong-coupling method is claimed.

## 1. Model and the quantity that formation preserves

Use the finite periodic bipartite cubic graph and local Hilbert spaces of
`HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md`. There are V vertices,
degree 2d, and dV edges. Sites hold zero or one record of content + or -;
each edge has its supplied spin-half electric degree of freedom. Write A,B
for the two equally sized sublattices. All microscopic couplings below are
finite for each member of the model family.

Let b_e move a record from the A endpoint to the vacant B endpoint, with
the appropriate charge-dependent partial electric shift, and write

    T = -sum_e (b_e+b_e^dagger),       H=Delta N_B+t T.

The bare initial state has every A site occupied by a plus record and every
B site vacant. Its field state can be arbitrary in the ice sector, mixed
and entangled with a reference. Initially N=N_0=V/2. H preserves N and
individual existing record contents. The edge-local birth instruments have
jumps J_(e,mu) that create opposite-charge records on two vacant endpoints,
shift the electric field to preserve Gauss, and satisfy

    sum_mu J_(e,mu)^dagger J_(e,mu) = beta P_(e,vac).

Here beta>=0 is uniform. This includes the coherent and charge-resolved
refinements already specified; it does not include arbitrary other jumps
with the same loss if their output action differs from local pair formation.
Define the positive defect count

    K = H_A+N_B,              H_A=sum_(x in A)(1-n_x).

An A-to-B hop raises K by two. A birth on a vacant A-B edge removes one
A hole and adds one B occupant. Consequently

    [K,b_e]=2b_e,       [K,J_(e,mu)]=0,
    [N,b_e]=0,         [N,J_(e,mu)]=2J_(e,mu).            (1)

The birth dissipator D satisfies D^dagger(K)=0 exactly, even though
D^dagger(N)=2 Gamma with Gamma=beta sum_e P_(e,vac). New records do not
directly increase this defect count. They redistribute its A-hole and
B-occupancy contributions. This does not mean that they preserve H.

For number-block-diagonal states, replace H by

    H' = H-Delta(N-N_0)/2 = Delta K/2+tT.                (2)

Both Hamiltonians give exactly the same density evolution: their difference
is scalar in each number block, H preserves blocks, and every jump moves a
block up by two records. Such block diagonality is preserved from the stated
initial condition. This is an algebraic change of energy reference between
number sectors, not a proof that the original physical energy is conserved.

## 2. Exact local effect of birth on hopping coherence

For an edge e=(a,b), a in A and b in B, define the spectator vacancy count

    c_e = sum_(y~a,y!=b)(1-n_y)+sum_(x~b,x!=a)(1-n_x).

It commutes with b_e and obeys 0<=c_e<=4d-2. The exact adjoint identity is

    D^dagger(b_e)=-(beta/2)c_e b_e,
    D^dagger(T)=(beta/2)sum_e c_e(b_e+b_e^dagger).       (3)

To verify it locally, a birth on e has support orthogonal to either end of
its hopping transition. A disjoint birth commutes with b_e and cancels from
the adjoint dissipator. For a birth on an edge f sharing just one endpoint,
J_f^dagger b_e J_f=0: after filling the pair, either the hop is blocked or
the reverse birth cannot remove both records. Exactly one side of the
anticommutator survives, giving -(beta/2)b_e times the vacancy projector at
the other endpoint of f. Summing f gives (3). The reasoning uses the actual
pair-creation maps, and works for both charges and their coherent refinements.

This identity makes the energy exchange explicit. Formation suppresses
hopping coherence even while leaving K unchanged at the instant of a jump.

## 3. A bound independent of the number of sites

Put k(s)=Tr(K rho(s)), x(s)=sqrt[k(s)/V], epsilon=|t|/Delta, and

    C_d=d(4d-2).

Since b_e b_e^dagger <= (1-n_a)n_b, the Schwarz inequality gives

    |Tr(T rho)| <= 2 sum_e sqrt[Tr(b_e b_e^dagger rho)]
                <= 2d sqrt(V k).                       (4)

The last step uses sum_e (1-n_a)n_b <= dK, which follows edgewise from
uv<=(u+v)/2 for commuting binary u,v and the degree bound. Applying the
same inequality to c_e b_e in (3) gives

    |Tr(D^dagger(T) rho)| <= C_d beta sqrt(V k).         (5)

Let E(s)=Tr(H' rho(s)). Initially E(0)=0, and Hamiltonian evolution does not
change E. Equations (2), (4), and (5) therefore imply

    Delta x(s)^2/2 <= E(s)/V+2d|t|x(s),
    E(s)/V <= |t| C_d beta integral_0^s x(u) du.         (6)

For any T_0>=0 let X=max_(0<=s<=T_0)x(s), attained by continuity in finite
dimension. Evaluate (6) at a maximizing time and use integral x<=T_0 X.
If X>0, divide by X; if X=0 the result is immediate. Thus, for every s>=0,

    k(s)/V <= epsilon^2 [4d+2C_d beta s]^2.              (7)

The trivial bound k/V<=1 can also be used. No small global norm condition
such as |t| ||T||<Delta/2 appears. The same constants work for every volume.
The estimate permits both quantum motion and active formation for the entire
interval, with no occupation monitoring, sink, removal, or reset assumption.

Write B(s) for the number of birth events. Since N=N_0+2B on each number
trajectory, N>=N_0 on its support. Hence H_A<=K/2, and

    Gamma <= 2d beta H_A <= d beta K.

Integration of the exact counting intensity Tr(Gamma rho) yields

    E[B(T_0)]/V <= d beta epsilon^2 [16d^2 T_0
                       +8d C_d beta T_0^2
                       +(4/3) C_d^2 beta^2 T_0^3].      (8)

The expectation notation in (8) is distinct from the energy E(s) above.
In particular, the increase of the mean permanent-record density is twice
the left side. For beta=0 there are no births and (7) is uniform for all time.
For beta>0 this is a finite-time estimate, not a stationary density bound.

Holding the ring scale J=2t^4/Delta^3 fixed gives

    epsilon^2=sqrt[J/(2Delta)].

Thus both defect density and additional-record density tend to zero at each
fixed time, uniformly in V. The explicit bound also gives vanishing added
record density on intervals T_0=o(epsilon^(-2/3)) at fixed positive beta,J.
This longer interval is a statement about density only. Its constants are
conservative; no optimal time scale is claimed.

The statement is uniform over finite volumes and controls spatial averages.
Pointwise local bounds require the corresponding translation symmetry or
another control on spatial concentration. A global average is not silently
promoted to a bound at every selected site or to existence of a particular
infinite-volume state. No infinite-volume limit theorem is needed for (7)-(8).

## 4. Why this does not yet control the large-system field evolution

An exact three-site control exposes a separate scale. Take an A center and
two B leaves, two identical plus records, outward edge fields E_1,E_2, and
external Gauss offsets (1,1/2,1/2). The entire fixed-charge physical sector
has three states:

    (matter; edge bits) = (1,1,0;0,1), (1,0,1;1,0),
                         (0,1,1;0,0).

The first two have one B record; the intermediate state has two. Relative
to the low pair, its energy is Delta. Ordinary hops connect each low state
to that intermediate state with matrix element -t. The low effective matrix
at second order is

    -(t^2/Delta) [[1,1],[1,1]].                         (9)

The exact spectrum consists of zero and
(Delta+-sqrt(Delta^2+8t^2))/2. This is exchange of an extra record between
B sites through a temporarily vacant A site, with single occupancy exact
at every step. In the fixed-J scaling its exchange scale

    h_defect=t^2/Delta=sqrt(J Delta/2)

grows while the characteristic creation-density scale beta epsilon^2 shrinks.
Their product is beta J/2. This comparison alone does not establish any
finite limiting field disturbance: the star is not a solved many-body
transport or scattering model. It does show why small mean density, by
itself, supplies no uniform bound on the accumulated field action of moving
defects. The relevant propagation and field disturbance must be calculated.

General local Schrieffer-Wolff and prethermalization results were inspected
as possible tools: [Bravyi, DiVincenzo and Loss, arXiv:1105.0675](https://arxiv.org/html/1105.0675),
sections 4.3-4.4, and [Abanin et al., arXiv:1509.05386v3](https://arxiv.org/html/1509.05386v3),
sections 2.2 and 3. Their locality constructions motivate a separate dressed
preparation analysis. No theorem from those papers is used to replace the
open-system estimates above or to assert bare-state field convergence. A
volume-uniform local ring-dynamics theorem with the stipulated live birth
law remains an open obligation here.

## 5. The formation apparatus has an energy cost

The original energy H, unlike K, is changed by pair formation. Already
D^dagger(Delta N_B)=Delta Gamma. Moreover, the coherence term (3) contributes
to D^dagger(H). The algebraic subtraction in (2) cannot remove that physical
energy exchange from an apparatus ledger.

For the exact four-site square from the preceding note, start in a normalized
low eigenstate of the closed two-record block, with energy E_low. Every
birth ends in a fully occupied four-record state of energy 2Delta; hopping
then vanishes. If R=Tr(Gamma rho)>0, the exact instantaneous relation is

    Tr(D^dagger(H) rho) = (2Delta-E_low) R.              (10)

For the low symmetric eigenstate and fixed J, E_low/Delta tends to zero;
the energy supplied per birth is asymptotic to 2Delta. The finite birth
rate becomes smaller, but the energy of a rare event grows. This is an
exact finite apparatus requirement, not a no-go theorem for an energy-aware
formation law. A frequency-selective reservoir, a bounded-energy fuel model,
or a change of the prescribed birth instrument would be different physical
models and need their own analysis. The earlier rest-record count ledger
does not by itself account for this interacting energy.

## 6. Verification and remaining claims

The companion `record_density_and_fast_defect_check.py` checks (1) and (3)
on complete 18-, 108-, and 324-dimensional local tensor products, for three
birth refinements. Sparse matrices use exact integer entries. It enumerates
the complete three-state Gauss sector for (9) and checks its characteristic
polynomial symbolically. It also evolves the full nine-state square including
both record-number sectors and checks (7)-(8), positivity, trace, and (10).
Those finite checks support algebra and implementation; they do not substitute
for the proof of the volume-uniform estimate.

The construction still supplies the enlarged local spaces, quantum law,
bosonic statistics, checkerboard energy penalty, background, preparation,
and apparatus. The density theorem removes a global-volume restriction for
one observable class. It neither proves nor refutes a photon phase, Lorentz
symmetry, indefinite coexistence, or the underlying theory of everything.
