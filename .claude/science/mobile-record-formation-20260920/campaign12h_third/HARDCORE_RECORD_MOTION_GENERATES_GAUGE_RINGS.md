# Gauge rings from permanent record motion with exact occupancy exclusion

Date: 2026-09-22. Status: personally derived conditional finite-volume
construction; independent reconstruction pending. This is an effective-model
bridge, not a native derivation from the minimal axioms or a photon-phase
theorem. The companion runner checks the stated coefficients and finite live
formation model; its receipt records the actual result.

## 1. Question, established machinery, and supplied structure

The preceding construction supplied a plaquette field Hamiltonian. The earlier
`VIRTUAL_MULTIPLE_OCCUPANCY_SOURCE_FOR_RECORD_CIRCULATION.md` obtained one
circulation coefficient by allowing virtual double occupancy. Here double
occupancy is absent from the Hilbert space. Vacant sites instead permit
permanent, same-content records to exchange positions through ordinary
nearest-neighbor gauge-covariant hopping.

Obtaining gauge plaquettes from auxiliary matter motion is established
strong-coupling machinery. Zohar, Cirac and Reznik's
[loop method, arXiv:1303.5040v3](https://arxiv.org/pdf/1303.5040v3), section VI.A,
uses pinned auxiliary fermion species and initially unitary link operators.
Gonzalez-Cuadra, Zohar and Cirac's
[Abelian-Higgs construction, arXiv:1702.05492](https://arxiv.org/pdf/1702.05492),
section 3.5.1, uses a finite on-site occupancy penalty. Neither that general
idea nor a new gauge principle is claimed here. The present calculation keeps
the link exactly spin half and excludes multiple occupancy at every stage;
its diagonal cancellation uses the ice Gauss sector explicitly. Coefficients
are derived below, not imported from those different auxiliary models.

Supply a finite d-dimensional periodic cubic lattice with all side lengths
even and at least six. Write V for its number of vertices and A,B for its
checkerboard sublattices. Each vertex has states |0>, |+>, |- >, with at most
one record. In the closed sector considered first there are V/2 identical
bosonic records, all with unchanged charge/content +1. Each oriented link has
E=+-1/2 and unit-amplitude raising/lowering operators U,U-dagger. Supply

    H_0 = Delta sum_(x in B) n_x,       Delta>0,
    H = H_0 + t T,
    T = -sum_(e:x->y,q) (a_(y,q)^dagger a_(x,q) U_e^(-q) + h.c.).

For q=+1, U^(-q) means the lowering operator; for q=-1 it means raising.
These are partial shifts, not invertible group elements. The spin-half
boundary is enforced exactly. In the fixed-plus sector the minus terms vanish.
Also supply the static compensating background n_x^0=1_A(x), and impose

    G_x = div_x E + n_x^0 - q_x = 0.

Every hop commutes with every G_x and with total record number. At t=0 the
low subspace P has one plus record at every A site, no B records, and div E=0.
Its field space is precisely the finite spin-half ice space, including all
its components. An oriented hop always has a vacant destination; no doubled
site is virtual or real. The records are indistinguishable within this
content class. Adding separately readable identity tags changes the effective
action to a joint field/record-permutation action and needs a separate model.

The link qubits, quantum amplitude rule, bosonic statistics, background
charge, energy penalty, checkerboard preparation and continuous Hamiltonian
time are supplied. The penalty and background select a spatial period-two
pattern; this is not the original homogeneous microscopic law. The argument
does not derive the field tensor factors from one possibility qubit per
original site. In particular, it must not be reported as native closure.

## 2. Complete coefficients through fourth order

Let Q=I-P and D=Q H_0^(-1) Q. In the specified fixed-number sector H_0>=Delta
on Q. PTP=0, and odd numbers of hops cannot restore the checkerboard record
occupation. With coefficients defined without their powers of t,

    H_2 = -P T D T P,
    F_4 = -P T D T D T D T P,
    K_2 = P T D^2 T P,
    H_4 = F_4 - (K_2 H_2 + H_2 K_2)/2.                 (1)

The last term matters. To see its origin, expand the energy-dependent Schur
operator near E=O(t^2):

    E u = (t^2 H_2 + t^4 F_4)u - t^2 E K_2 u + O(t^6).

Symmetric normalization of the metric I+t^2 K_2 gives (1). Merely evaluating
the Schur operator at zero energy omits this normalization contribution.

On an ice basis state c, precisely d of the 2d incident fields at each A
vertex permit an outgoing plus record. At each B vertex precisely d incoming
edges are eligible. Thus the graph of initially allowed A->B hops is
d-regular on all V vertices and has

    M = d V/2

edges, independent of c. A two-hop P return must undo the first hop: the
original A vacancy is the only available A destination. Consequently

    H_2 = -(M/Delta) I_P,          K_2=(M/Delta^2) I_P.  (2)

For a four-hop path that stays in Q at its three intermediate stages, the
numbers of records on B are necessarily 1,2,1. Its denominators are therefore
Delta,2Delta,Delta. The first two hops use two initially eligible edges with
disjoint endpoints. There are

    N_disjoint = choose(M,2) - V choose(d,2)

unordered choices. Undoing these two moves gives four time orderings per
choice and hence F_4(c,c)=-2 N_disjoint/Delta^3. Adding the folded term in (1)
leaves

    H_4(c,c) = [M^2 - 2 N_disjoint]/Delta^3
             = [V d(2d-1)/2]/Delta^3.                    (3)

This is a constant, not a flippability potential. A non-diagonal return must
exchange the two identical records: the two departure and two arrival edges
form a simple four-cycle. On the stated torus these are exactly elementary
plaquettes. Spin-half eligibility requires its oriented loop field to be
flippable. Each directed loop has four allowed time orderings and gives

    H_4(c^p,c) = -2/Delta^3.                             (4)

There are no other four-hop P returns. In particular,

    H_eff = [-M t^2/Delta + V d(2d-1)t^4/(2Delta^3)] I_P
            - J sum_p (W_p+W_p^dagger) + O_V(t^6/Delta^5),
    J = 2 t^4/Delta^3.                                  (5)

The remainder is for a fixed finite lattice near t/Delta=0, not a
volume-uniform linked-cluster estimate. One bond term in T has norm at most
one, so ||T||<=dV. For |t| ||T||<Delta/2, the low spectral cluster is isolated
from the others by at least Delta-2|t| ||T||. Its spectral projector and the
canonical normalized low-space Hamiltonian are analytic in t/Delta. The
unitary (-1)^(N_B) changes t to -t and is the identity on P, so this canonical
effective Hamiltonian is even in t. These finite-matrix facts justify the
stated sixth-order remainder after (1)-(4); no thermodynamic convergence
radius is inferred.

A torus with side length two has parallel-edge two-cycles. Side length four
also has winding four-cycles along an axis. Formula (5), with *only* ordinary
plaquettes, excludes both cases. The generic graph formula instead includes
every allowed shortest four-cycle when there are no two-cycles.

## 3. A complete single-square control and the statistics premise

Orient all four edges around one square and supply the boundary/background
offset (1,0,1,0). In the two-record zero-Gauss sector there are seven states:
two low field words with records at 0,2; four one-excursion states of energy
Delta; and one opposite-checkerboard state of energy 2Delta. Their exact
hopping graph gives

    H_2 = -(2/Delta) I,
    F_4 = -(2/Delta^3) [[1,1],[1,1]],
    H_4 =  (2/Delta^3) [[1,-1],[-1,1]].

The symmetric and antisymmetric low energies begin respectively
`-2t^2/Delta+O(t^6/Delta^5)` and
`-2t^2/Delta+4t^4/Delta^3+O(t^6/Delta^5)`.
Both low field words are flippable, so the constant on this restricted
doublet can resemble an RK projector. Equation (3) shows why it must not be
promoted to a lattice flippability potential.

For comparison, one trapped record on the same square gives a five-state
sector, H_2=-I/Delta and H_4=-X/Delta^3. This check distinguishes a one-record
loop from the two-record exchange actually used in (5). Replacing the two
identical bosons by identical fermions reverses the off-diagonal fourth-order
sign, yielding `2[[1,1],[1,1]]/Delta^3` in the same ordering. Permanence alone
does not select the required exchange statistics.

## 4. New records can form during a virtual vacancy

Now allow the already specified gauge-preserving pair formation at every
vacant edge. The coherent or charge-resolved versions have the same loss
operator

    Gamma = beta sum_e P_(both endpoints vacant),       beta>0.

Every birth creates two opposite-charge records, preserves Gauss, and leaves
pre-existing record contents unchanged. Hopping preserves number and births
only increase it. Initially Gamma P=0 because no two B sites are neighbors.
After one allowed A->B hop there is one A vacancy. Exactly 2d-1 of its B
neighbors remain vacant, so Gamma on the first-excursion space is
beta(2d-1) I. Eliminating that space in the no-birth conditional Hamiltonian
therefore gives the leading probability-loss rate

    R_birth = M beta(2d-1) t^2 /
              [Delta^2 + (beta(2d-1)/2)^2] I_P.           (6)

This is the leading second-order coefficient, with Delta and beta held
fixed as t becomes small. It does not claim that the full finite-time
survival is exactly exponential or that later births follow this same rate.
The first-birth calculation needs the no-event loss only and is independent
of how the same loss is refined into retained birth outcomes.

For beta<<Delta the ratio of (6) to J scales as
`M(2d-1) beta Delta/(2t^2)`. Raising Delta at fixed t makes the ring slower
faster than it suppresses births. That parameter path is unfavorable, but
is not an impossibility result for record formation and field dynamics.

There is a different controlled finite-volume scaling. Hold J and beta fixed
and choose

    t = (J Delta^3/2)^(1/4),             Delta -> infinity.

Then t/Delta=(J/(2Delta))^(1/4) tends to zero, the desired ring coefficient
stays J, the sixth-order Hamiltonian remainder scales as O_V(Delta^(-1/2)),
and the leading birth rate is

    M(2d-1) beta sqrt[J/(2Delta)].                       (7)

Both microscopic scales grow in this construction. It does not keep a fixed
upper bound on the microscopic energy or hopping strength. The divergent
second-order term in (5) is a scalar inside P and has no effect on its density
dynamics. The background and preparation costs remain supplied.

## 5. A finite-time control that does not assume the effective birth equation

The positive scaling conclusion can be supported without mistaking (6) for
an exact generator. Let v=|t| ||T||<Delta/2, and let P' be the isolated low
spectral projector of the closed, fixed-number Hamiltonian. The Sylvester
equation for QP' gives

    ||P'-P|| = ||Q P'|| <= v/(Delta-v).

Indeed QH_0Q has spectrum at least Delta, while H restricted to P' has
spectrum at most v; its off-block equation has right side of norm at most v.
The integral solution of that Sylvester equation yields the displayed bound.
The two projectors have the same rank. Splitting a state initially in P into
P' and its complement thus gives, uniformly in time,

    ||Q exp(-iH s) psi|| <= q_* := min(1,2v/(Delta-v)).   (8)

Let g=||Gamma||<=beta dV. Gamma annihilates P and preserves the original
fixed-number sector. The no-first-birth vector is
`psi_c(s)=exp[-i(H-iGamma/2)s]psi`; its propagator is a contraction. Duhamel
against the closed vector gives

    ||psi_c(s)-exp(-iHs)psi|| <= g q_* s/2,
    ||Q psi_c(s)|| <= q_*(1+g s/2).

The exact first-birth probability consequently obeys

    Pr(first birth by T)
       = integral_0^T <psi_c(s),Gamma psi_c(s)> ds
       <= g q_*^2 T (1+gT/2)^2,                         (9)

with the trivial upper bound one understood. Mixtures and a reference system
obey the same bound by purification; all displayed operator estimates tensor
with the identity on that reference. Subsequent evolution after a first birth
does not change the equality for its probability.

For completeness, compare the *full* state with and without formation, not
only its no-birth probability. On a pure closed state with Q-norm at most
q_*, the dissipator has trace norm at most `g(q_*+q_*^2)`: its positive jump
part has trace at most g q_*^2 and its anticommutator part has trace norm at
most g q_*. CPTP contraction and Duhamel give

    ||rho_live(T)-rho_closed(T)||_1
        <= g T (q_*+q_*^2).                             (10)

Here the Hamiltonian and formation law may be extended in the stated way to
the higher-number sectors; the closed reference trajectory never enters
them. Thus (9)-(10) do not assume a sink reset, a removal of created records,
or a return from a higher-number sector.

At fixed V,J,beta,T in the scaling above, (9) tends to zero as
O_V,beta,T(Delta^(-1/2)) and (10) as O_V,beta,T(Delta^(-1/4)). Combining (10)
with the finite analytic closed effective Hamiltonian and dressing gives the
spin-half ring unitary on every fixed finite time interval, after ignoring
the scalar phase in (5). This is an approximation theorem for a family of
supplied finite models. It is not a claim of one finite model surviving
indefinitely, uniformity in V, or commuting the long-time and large-Delta
limits.

The seven-state square has a particularly transparent exact no-birth check.
The four energy-Delta states have loss beta; the other three have zero loss.
Put a=Delta-i beta/2. The reflection-odd block has low eigenvalue

    E_odd=-2t^2/a+4t^4/a^3+O(t^6),

and the even block has

    E_even=-2t^2/a+[4/a^3-4/(a^2 Delta)]t^4+O(t^6).

Their splitting gives the stated ring scale as beta/Delta tends to zero.
The runner constructs actual charge-preserving birth maps on the full square
sector, checks Gamma exactly, and evaluates the exact seven-dimensional
no-event propagator with beta=1 and fixed J=1. After a birth all four sites
are occupied, so there is at most one birth in this particular square model.

## 6. What has and has not been connected

This supplies a finite-model path from nearest-neighbor motion of permanent
records through vacancies to a nontrivial magnetic ring Hamiltonian, with
single occupancy enforced exactly and new record formation left active. It
also gives the scale cost of keeping that formation rare over a selected
field-evolution interval. The statement concerns quantum motion of the
specified content classes; it does not recover quantum amplitudes from a
classical random walk.

The generated Hamiltonian is the pure kinetic spin-half ring model. An RK
flippability potential, the preceding preparation controls, a large-scale
deconfined photon regime, Lorentz symmetry, the observed matter spectrum and
gravity have not been derived. Coexisting preparation apparatus on this
checkerboard is another obligation: the low configuration itself has no
adjacent vacant sites available to host a fresh pair readout. Extra prepared
apparatus cannot be silently identified with those occupied/background sites.

The neutral background, selected pattern, enlarged vertex/link space,
statistics and scalable microscopic energies are explicit premise costs.
Future work should test whether some can be implemented by the record law
and existing site algebra, and whether the large-volume dynamics have the
required infrared physics. The result is a concrete conditional bridge for
that work, not evidence that a theory of everything has been established.
