# Local electric completions and a field phase after two births

Personal conditional construction, 2026-09-24. The construction below is an
alternative supplied microscopic Hamiltonian within the same hard-core
quantum/Gauss model. It keeps the formation instrument and quantum carriers.
It does not select a new native law or supply an autonomous energy source.
The original compensated model and its energy results remain statements
about their original Hamiltonian.

The question is whether the electric field energy can remain on links when
their endpoints become occupied. The previously checked compensation gives
the electric diagonal D only on currently legal outward-hop links. A local
term that is invisible to its fixed-field fourth-order rotor coefficient
can change this electric diagonal. The resulting family has the same
pre-first limiting field dynamics and a different observable field phase
after an actual two-birth history.

## 1. A uniformly bounded local microscopic addition

Use a fixed finite simple bipartite graph G=(A union B,E), hard-core charges
q=0,+1,-1, normalized integer-spin links S>=1, and the existing Gauss law.
Orient every edge e=(a,b) once; write s_ab=+1 when the A endpoint a is its
lower/oriented source, and -1 otherwise. Let n_a be occupancy. On the full
physical spin space define the diagonal

    D_ext = sum_(a~b) n_a(1-n_b) E_e(E_e-s_ab q_a),
    E2 = sum_e E_e^2,       C=S(S+1),
    R_S = (E2-D_ext)/C.                                  (1)

On P, every A site is occupied, and D_ext restricts to the previously
defined D. This full-space extension is part of the specified construction;
it is not an implicit replacement of C1 by its P restriction.

For fixed 0<=lambda<=1 supply

    C_S^(lambda)=C_S+lambda R_S,
    H_epsilon,S^(lambda)
       =delta epsilon^-4[W+epsilon T_S+epsilon^2 C_S^(lambda)],
    L_(j,epsilon,S)=sqrt(kappa) epsilon^-1 j_S.            (2)

C_S is exactly the original radius-two gated compensation. No jump operator
has been filtered or replaced.

Each summand of R_S is supported on its link and its two endpoint charges.
It is real diagonal, self-adjoint, commutes with W,N and every Gauss operator,
and is uniformly bounded. If the outward hop is inactive, its numerator is
E_e^2. If active, the numerator is s_ab q_a E_e. For |E_e|<=S,

    |R_(e,S)| <= S/(S+1) <=1,      ||R_S||<=|E|.        (3)

The local term need not be positive. The general compensation theorem only
requires bounded self-adjoint penalty-preserving C; it does not require
positivity of every compensation summand. The new family meets that theorem's
uniform bounds. This is a bounded interaction for each finite spin, although
its microscopic coefficient is delta epsilon^-2 as before.

Embed the spin boxes in the rotor physical space and extend R_S by zero
outside. For every finite electric-support vector, R_S tends to zero because
the numerator in (1) is fixed there and C tends to infinity. The uniform
bound (3) extends convergence strongly to the entire space. Norm convergence
is neither needed nor true. This distinction matters for moving inputs with
field proportional to S.

## 2. The complete common rotor target

On P, the original identity C0=M+D/C gives exactly

    P C_S^(lambda) P=M_S+D_lambda/C,
    D_lambda=(1-lambda)D+lambda E2.                       (4)

Take the same joint relation delta/epsilon^2=K C, fixed K,delta,kappa>0.
The entire second-order Hamiltonian is precisely K D_lambda. Both D and E2
are nonnegative diagonal multiplication operators on integer physical fields,
so D_lambda is nonnegative, self-adjoint on its multiplication domain, with
finite-support physical vectors as a core.

In the exact canonical fourth coefficient, changing C changes only

    lambda[A_S* (Pi1 R_S Pi1) A_S
                          -{M_S,P R_S P}/2].            (5)

All factors are uniformly bounded on this fixed graph. R_S tends strongly
to zero, while the bounded hopping products and their adjoints converge
strongly to their rotor counterparts. Thus (5) tends strongly to zero.
The limiting fourth-order Hamiltonian is exactly the original one,

    V=delta H4_infinity^C,
    H4_infinity^C=-2 sum_(overlapping A stars a,c) S_ac* S_ac,
    h_lambda=K D_lambda+V.                              (6)

The local-pair formula is the existing checked source, not a new derivation
in this note. On the cube it reduces to H4=-Z*Z/2. The first effective maps
B_j=-PjPi1TP are unchanged, because the compensation enters at epsilon^2
and does not alter U'(0).

Since V and all jumps are bounded at fixed graph, h_lambda is self-adjoint
on D(D_lambda) and generates, together with the bounded Lindblad terms, a
trace-preserving completely positive trace-class semigroup. To transfer
the spin targets, extend their bounded fourth-order coefficients and jumps
by zero outside the physical spin boxes and retain the common K D_lambda
on the full rotor space. The boxes reduce this dynamics. In the interaction
picture of K D_lambda, the remaining superoperators are uniformly bounded
and converge strongly on trace class. Their bounded Dyson series then gives,
for every trace-norm convergent sequence of physical initial densities,

    sup_(0<=t<=T)||rho_target,S(t)-exp(t L_lambda)rho_0||_1 ->0,
    L_lambda rho=-i[h_lambda,rho]+kappa sum_j D[B_j]rho. (7)

This proof uses finite-rank approximation and dominated convergence of the
Dyson series; no energy-moment bound on rho_0 is silently required. The
general compensation theorem supplies the uniform-S O(epsilon) microscopic
density error for (2), including its stated finite count/mark registers.
Combining it with (7) gives the fixed-graph common density limit through
all permitted formations. It does not transfer unbounded microscopic energy
moments or assert convergence of arbitrary continuously conditioned histories.

## 3. Identical pre-first limiting field behavior

On the all-A-positive, B-vacant sector, the Gauss equation says div E=0.
The linear term in D is minus sum_(a in A) div E_a. Hence D=E2 on this
entire normalizable field sector, and (4) is independent of lambda there.
Equation (6) and the jump operators are independent of lambda as well.
Therefore every family member has the same limiting pre-first Hamiltonian,
the same no-event generator on this sector, and the same first-mark maps.
This is exact agreement of the limiting preparation and first-event law.
It is not an assertion of identical finite-S microscopic Hamiltonians.

The subsequent h_lambda need not agree. In particular, on a completely
occupied graph all outward hops vanish. Thus D=0 and H4=0 there, but

    h_lambda|_(full occupancy)=K lambda E2.             (8)

At lambda=0 that sector is frozen. At lambda>0 its field superpositions can
acquire nontrivial phases even though no further formation is possible.
This is electric field evolution; (8) does not supply a magnetic propagation
term on a completely filled lattice or establish a photon phase.

For lambda>0 on any fixed graph, D_lambda>=lambda E2 also implies compact
resolvent: there are finitely many charge words and finitely many integer
field vectors with E2 below any fixed bound, and V is bounded. This is a
finite-graph spectral statement. It implies neither an infinite-volume gap
nor relaxation of the open-system dynamics. In contrast, on a cyclic graph
the lambda=0 fully occupied sector has infinitely many circulation states
with zero Hamiltonian. No compactness conclusion is transferred to it.

## 4. An accessible two-birth interference witness

Use the cube and the normalizable face-circulation Omega_n specified in the
high-flux note, with any integer n. Keep the original resolved instrument.
Consider the ordered marks (01,+ at0), then (67,+ at6). Directly applying
their actual B operators gives

    B_(67,+) B_(01,+) Omega_n = |a_n>+|b_n>,
    ||B_(67,+) B_(01,+) Omega_n||^2=2.                 (9)

Both outputs have all A charges plus, B1 and B7 minus, and B2 and B4 plus.
For a_n the old records take 0->2 and 6->4; for b_n they take 0->4 and
6->2. Relative to the initial field their nonzero shifts are

| output | shifted oriented links | E2 |
|---|---|---|
| a_n | E01 +=1, E02 -=1, E46 +=1, E67 +=1 | 4n^2+4n+4 |
| b_n | E01 +=1, E04 -=1, E26 +=1, E67 +=1 | 4n^2+2n+4 |

These are two distinct physical flux basis states with the same charges.
Let W_square translate b_n to a_n by the divergence-free unit circulation
on 0-2-6-4. It is a bounded physical rotor Wilson operator, independent of n.
For psi_n=(a_n+b_n)/sqrt(2), (8) gives the exact terminal expectation

    <W_square+W_square*>_tau = cos(2K lambda n tau).    (10)

An added scalar or number-only energy offset cancels from this phase because
both components have the same number and charge word. Thus the difference
between family members is observable in their stipulated dynamics, not just
an energy-origin convention.

Equation (9) is also an actual short-time accessibility witness. Strong
continuity of the bounded-jump integrands gives, for precisely these ordered
marks completed by small t,

    probability = kappa^2 t^2+o(t^2),
    normalized conditional terminal state -> |psi_n><psi_n|. (11)

The factor is the ordered time-simplex area t^2/2 times the squared norm2.
At full occupancy there are no additional births. After a further fixed
waiting time tau, the conditional Wilson expectation tends to (10) as
t decreases to zero. The event itself does not have positive probability
at time zero; for sufficiently small positive t it approximates this
experiment with the probability in (11). No intermediate energy projection
or preparation filter has been inserted. The displayed resolved marks are
one of the original instruments, not a coherent-instrument assertion.

## 5. System-energy consequences and scope of selection

The selected first mark (01,+) has the same two paths as before. Their
E2 values are 4n^2+4n+2 and 4n^2+2n+2; the original D values are 0 and2n^2.
It follows directly that its normalized output satisfies

    <D_lambda>=(1+3lambda)n^2+3lambda n+2lambda,
    Var(D_lambda)=[(1-lambda)n^2-lambda n]^2.           (12)

The checked H4 coefficients on these two input words coincide, so their
covariance with D_lambda is zero. Using the sealed high-flux author H4 moments (their full independent
comparison is pending at this seal), the corresponding Hamiltonian statements are

    <h_lambda>_after-<h_lambda>_before
       =K[-3(1-lambda)n^2+3lambda n+2lambda]+64delta,
    Var(h_lambda)_after
       =K^2[(1-lambda)n^2-lambda n]^2+392delta^2.       (13)

The all-mark rotor E2 drift at Omega_n is 96kappa. Each of the 48 signed
paths shifts two distinct links by one; the two birth signs cancel their
linear energy contribution, while the old-hop linear contributions sum to
zero by the initial Gauss divergence. Every path adds the constant two.
Together with the checked D and H4 balances this yields, for either
instrument,

    d<h_lambda>/dt at0
       =kappa[-96(1-lambda)K n^2+96lambda K+3216delta]. (14)

At lambda=1 link energy persists through filling, the selected electric
variance grows as n^2, and the all-mark initial system-energy drift is the
positive constant kappa(96K+3216delta). At lambda=0 the earlier n^4 variance
and negative high-flux drift are recovered. These different conditional
models satisfy the same stated pre-first limiting field and birth data.
The construction supplies an explicit family and a discriminator; it
does not infer that nature chooses lambda=1 or any other value.

All energy formulas are for the target system Hamiltonian. Neither positive
nor negative drift identifies heat, accounts for a physical drive, or gives
a finite autonomous fuel model. The microscopic Hamiltonian has changed by
the stated term (2), and its unbounded energy moments need separate analysis.
No all-time heating law, growing-volume microscopic limit, native selection,
continuum field equation, or observed-particle claim follows here.

The exact author control reconstructs both ordered outputs and compares them
with the earlier independently written birth-path implementation at its pinned
hash. It checks seven positive/negative/zero n values, four lambda values,
the full terminal H4 action, the divergence-free Wilson shift, and the sharp
local bound in (3) at six spins. The proofs are (1)-(11), not extrapolation
from those cases. Fresh independent reconstruction and final comparison
standing are recorded separately; author computation is not independent review.
