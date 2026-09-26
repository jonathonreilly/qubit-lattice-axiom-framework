# Ballistic field signals from record formation in a one-dimensional model

Date: 2026-09-22. Status: exact finite sector identities, a second-order
microscopic coefficient, and an exact calculation for a separately declared
reduced transport kernel; independent reconstruction pending. The reduced
kernel's large-volume limit has not been proved for the microscopic Lindblad
model. The calculation is a diagnostic for that missing step, not a no-go
theorem for record formation or a result about three-dimensional photons.

## 1. Exact one-dimensional physical space

Take the supplied hard-core gauge-record model on an even ring of L>=6 sites.
Orient link x from site x to x+1, put A at even sites, and write its electric
bit b_x=E_x+1/2. The selected Gauss sector fixes the record charge uniquely:

    q_x=b_x-b_(x-1)+1_A(x).                              (1)

Allowed charges are 0,+1,-1. Since the link divergence lies between -1 and 1,
an A-minus record is impossible. Every minus record is at B and cannot hop
to either neighboring A site. This is a one-dimensional boundary-of-the-link
space restriction; it is not a general consequence of gauge invariance in
higher dimension. Existing plus records retain their contents while moving.

In the sector with no minus records, set

    eta_x=b_x for x even;       eta_x=1-b_x for x odd.

Equation (1) is equivalent to forbidding adjacent eta=1 excitations. The
Hamiltonian is exactly the constrained spin Hamiltonian

    H=Delta[L/2-sum_x eta_x]
                   -t sum_x P_(x-1) X_x P_(x+1),        (2)

where P=|0><0| and X has unit off-diagonal elements. The quantum-link/PXP
connection is established machinery, not claimed as new here; see
[Desaules et al., arXiv:2301.07717v3, section 2](https://arxiv.org/html/2301.07717v3).
Equation (2) is the direct specialization with this note's record and bit
conventions. Adding irreversible pair births goes beyond that closed PXP
subspace and needs its own bookkeeping.

In the full live physical space, only the A constraint is imposed. Each A
pair (b_(A-1),b_A) can be 00,10,11, independently, so the dimension is 3^(L/2).
A new minus at B fixes b_(B-1)=1 and b_B=0. The A constraints also fix
b_(B-2)=1 and b_(B+1)=0. Equivalently it creates a locked eta pattern 0,1,1,0.
The adjacent two A-plus records are immobile as well. No Hamiltonian term
can connect across this fixed cluster.

For a nonempty fixed set of minus positions, let g_i be the cyclic distances
between consecutive minus records in B-site spacings. Each g_i>=2. The closed
Hamiltonian factorizes exactly into open PXP intervals of lengths 2g_i-4,
with fixed zero eta boundaries. Its sector dimension is

    product_i F_(2g_i-2),                               (3)

where F_0=0,F_1=1. The diagonal penalty is
`Delta[L/2-sum_(free links) eta_x]`. Pair births can create new cuts, but
cannot remove the old ones. The runner checks all physical words through
L=14, their exact hopping transitions, penalties and dimension factors.
This is an exact description of this one-dimensional model's fragmentation,
not a claim that analogous fixed cuts occur in the cubic model.

## 2. The first created pair has a mobile field boundary

Fix one minus record at a B site r. In the lowest N_B sector after one birth,
all A sites are occupied by plus records, and there is exactly one plus and
one minus on B. There are m-1 such states, where m=L/2. Label them |n>,
1<=n<=m-1, by the clockwise separation of the B-plus record from r in B-site
spacings. Between the minus and plus, exactly 2n links have b=0; all other
links have b=1. Relative to the all-one ice field, the total electric-field
deficit is therefore 2n.

The bare energy is 2Delta in the original N_B model. It is Delta under the
homogeneous field-star model. In fact in this entire fixed-minus sector the
two Hamiltonians differ by the scalar Delta: A-minus records are impossible,
so R=N_B-1. Their record and field dynamics agree exactly.

The two A records adjacent to the fixed minus cannot leave. Each of the
other m-2 A records has one eligible virtual departure. Every intermediate
state reached by one hop has energy Delta above this low sector. A two-hop
return either reverses that departure or exchanges the mobile B-plus record
with its neighbor through an A vacancy. Consequently

    H_eff = E_bare I -h[(m-2)I+A_(path,m-1)]
                         +O_L(t^4/Delta^3),
    h=t^2/Delta,                                       (4)

where the path adjacency has unit entries between consecutive n. Both the
diagonal and off-diagonal coefficients are complete second-order results.
The error is at fixed L. Exact full-sector matrices for L=6,8,10,12,14
give dimensions 3,8,21,55,144 and reproduce (4); finite spectra corroborate
the fourth-order error for the first three rings.

Start instead in the all-one ice field before any birth. Its leading dressed
low-state correction is `-(t/Delta)QT|ice>`. At a fixed odd birth edge r, the
only contributing first excursion moves the A record immediately to its
right into the next B site. The birth then fills that A vacancy and puts a
minus at r. Thus the leading transformed birth operator creates |r,n=1>
with amplitude epsilon=t/Delta. Its leading rate is beta epsilon^2 per B
anchor. The source coefficient is checked directly as `-J_r T|ice>`, apart
from its common denominator and t, separately from the target-sector hopping
calculation. It refers to a dressed low state, not an assumed stationary bare
checkerboard after a sudden quench.

This is where perturbative microscopic matching stops in this note. Using
(4) on distances growing with hT requires additional control. The following
calculation takes the leading transport and source terms as a stipulated
reduced model and proves statements only about that model.

## 3. Exact quantum-walk transport in the reduced model

On the half-line n=1,2,..., take H_walk=-h A_path, initial state |1>, and
theta=h s. The sine transform, or odd reflection of the line propagator,
gives the exact amplitudes

    psi_n(s)=i^(n-1)[J_(n-1)(2theta)+J_(n+1)(2theta)]
            =i^(n-1)(n/theta) J_n(2theta).              (5)

The theta=0 value is understood by continuity. The recurrence used here is
the ordinary Bessel recurrence in [DLMF 10.6](https://dlmf.nist.gov/10.6).
Ballistic continuous-time quantum-walk limits are established mathematics;
the following short derivation checks the coefficient for this boundary
initial state rather than importing a different initial-state law.

Embed |1> as the normalized odd line state
`(|1>-|-1>)/sqrt(2)`. For the unit-hopping line Hamiltonian, the Heisenberg
position is exactly X(theta)=X+theta V, where V commutes with H and has
Fourier multiplier 2 sin k, up to an irrelevant overall sign. The initial
Fourier probability density is sin^2(k)/pi on [-pi,pi]. The operators
X/theta+V converge in strong resolvent sense to V: on a finite-support core
their difference tends to zero, and the bounded resolvent identity extends
the convergence. Also ||[X/theta+V]psi|| is uniformly bounded for theta>=1.
That second-moment bound makes absolute first moments uniformly integrable.
Odd reflection identifies the half-line separation with absolute line
position. Hence

    lim_(s->infinity) <n(s)>/(h s)
       =(1/pi) integral_(-pi)^pi 2|sin k| sin^2(k) dk
       =16/(3pi).                                     (6)

This argument is for the specified finite-support initial state and uniform
half-line hopping, without a boundary potential. The operator norm of the
position current is at most 2h, giving the useful all-time bound

    <n(s)> <= 1+2h s.                                  (7)

The runner checks (5) against complete finite matrix exponentials, checks
normalization with two Bessel cutoffs, and evaluates (6) up to theta=2000.
It finds <n>/theta=1.6976527661, approaching 16/(3pi)=1.6976527263.

## 4. Density and field susceptibility separate in this reduced kernel

For a finite ring, define a reduced vacuum |Omega> with all b=1, and a
one-pair block for each of its m anchors. Its Hamiltonian in each block is
the path Hamiltonian (4) after scalar removal. Supply jumps

    L_r=sqrt(beta) epsilon |r,1><Omega|.                (8)

These equations specify a trace-preserving finite one-birth model. They
contain a whole-vacuum projector and are not claimed to be a native local
generator. They also give the first derivative at beta=0 of any smooth
extension that adds further beta-proportional birth channels only after the
first birth: those channels cannot contribute at first order.

Let F_L=L^(-1)sum_e(1/2-E_e), and let R_L count additional records divided by
L. In vacuum both are zero. In |r,n> they are respectively 2n/L and 2/L.
The exact linear susceptibilities of (8), at beta=0, are

    d_beta <R_L(T)>|_0 = epsilon^2 T,
    d_beta <F_L(T)>|_0 = epsilon^2 integral_0^T <n(s)>_path ds.  (9)

First take L to infinity at fixed h,T. The finite path tends to the half-line;
its expansion in paths controls boundary errors, while (7) controls the
integral. Then hold J=2h epsilon^2 fixed and let epsilon approach zero.
Equations (6)-(7) and dominated convergence give

    lim_(epsilon->0) lim_(L->infinity) d_beta <R_L(T)>|_0 =0,
    lim_(epsilon->0) lim_(L->infinity) d_beta <F_L(T)>|_0
                                        =4JT^2/(3pi).   (10)

For each fixed L, however, n<=m-1; the field derivative in (9) is at most
epsilon^2 T(m-1) and tends to zero. Reversing the two limits thus gives zero.
The order-of-limits distinction is exact for the reduced kernel. There is
no nonzero local magnetic plaquette Hamiltonian in an infinite 1D chain;
J here labels the same microscopic scale combination as in the cubic route,
not a claim that this one-dimensional model contains photons or plaquettes.

At J=T=1, the numerical field susceptibility is 0.4244143671 for epsilon=.025,
while the exact limit is 4/(3pi)=0.4244131816. The additional-record density
susceptibility is only .000625. These are derivatives at zero beta; multiplying
them by an arbitrary finite beta is not a controlled many-birth prediction.

## 5. What this resolves and what it does not

The exact microscopic sector calculation identifies an immobile new minus
record, a moving plus boundary, and its t^2/Delta transport coefficient. The
specified reduced model demonstrates quantitatively how a vanishing source
density and an increasing propagation speed can leave a finite field
response. The same small number of records can delimit a large field region.
It gives a concrete target for the missing large-volume open-dynamics check.

It does not prove that (10) is the microscopic limit. That would require
uniform control of the dressed initial state, Hamiltonian corrections, birth
operators and observables, followed by the volume and beta-derivative limits.
Bare sudden preparation can add other propagating excitations and must be
analyzed separately. At nonzero beta, further cuts and interacting domains
must be included. The one-dimensional pinned-minus mechanism does not extend
unchanged to three dimensions, where A-minus states can be allowed.

Possible positive routes remain: a prepared dressed state, a formation rate
that scales with the transport limit, or a different microscopic interaction
that controls disturbance propagation. None is excluded by this diagnostic.
The general question of a uniform local field limit stays open; the earlier
finite-volume approximation and uniform mean-density theorems retain their
separate stated meanings.
