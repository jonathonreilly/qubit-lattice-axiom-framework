# Root constructive follow-up: a local compensation candidate

Unfrozen exploratory derivation, September 23, approximately 19:20 UTC.
This proposes a change to the supplied microscopic law. It is not derived
from native record axioms, not adopted as a premise, and not yet verified.
The objective is a controlled common ordinary-time field/matter limit with
actual repeated formation, avoiding reliance on a special physical flat band.

For each A site a, let E_a be the normalized-spin outward hopping sum from
occupied a to neighboring empty B sites. It lowers n_a by one. On P,
M_S=Pi_0 T_S Pi_1 T_S Pi_0=sum_a E_a^*E_a. Define its diagonal physical
charge/field part D_a,S and the corresponding unit-weight diagonal D_a,inf
(the number of vacant B neighbors of occupied a).

Consider a local term on the original physical Hilbert space,

    C_a,S = [E_a^*E_a - D_a,S + D_a,inf] Q_a,
    Q_a = product_(c in A, c!=a, dist(c,a)<=2) n_c,
    C_S=sum_a C_a,S.

The occupancy gate commutes with the bracket and W. C_S is gauge invariant,
number preserving and supported on a fixed radius-two neighborhood on
bounded-degree bipartite graphs. It is uniformly bounded in S on a fixed
graph. On P all Q_a=1, and

    C_PP,S=M_S + D_inf-D_S,
    H2_S+C_PP,S=D_inf-D_S
                 = C^-1 sum_(allowed outward edges) E_e(E_e+k_e).

Each integer E(E+k), k=+/-1, is nonnegative. Hence in eta=K S(S+1) scaling
the entire leading target becomes an explicit nonnegative diagonal electric
operator K D(q,E), rather than an eta-divergent matter hopping operator.
This exact spin-weighted compensation is preferable to subtracting only the
unit-rotor M: that alternative leaves a potentially indefinite unbounded
quadratic matrix difference whose essential self-adjointness is unproved.

Candidate microscopic change: add delta epsilon^-2 C_S to the parent
Hamiltonian, equivalently add epsilon^2 C_S inside W+epsilon T. Keep the
formation instrument unchanged. This is an explicitly tuned extra dynamical
term; no inference that the original law already contains it is allowed.

For any bounded block-diagonal C commuting with W, a Schur/orthonormalization
calculation suggests

    H2'=C_P-M,
    H4'=M^2 - (M C_P+C_P M)/2
            + A^* C_(W=1) A - Z^*Z/2.

This coefficient and the uniform microscopic error with the added C must be
derived and independently checked; it is currently a candidate formula.
The effective birth remains B=-P j Pi_1 T P at leading order if the same
block-diagonalization proof applies.

For the cube every pair of A sites is distance two. Thus Q_a kills C on
the W=1 sector, C_Q=0, while C_P tends strongly to M_rotor. The candidate
ordinary limiting Hamiltonian in every P number sector is consequently

    h_N=K D_N(q,E) - (delta/2) Z_N,rotor^* Z_N,rotor,

with the original finite rotor birth jumps. D_N is nonnegative diagonal and
the second term bounded on a fixed graph, giving a straightforward
self-adjoint operator on D(D_N). Finite-support states are a core. Strong
bounded-perturbation convergence should yield the complete trace-class
quantum Markov limit, including actual unselected outputs and both births.

On the initial all-A-plus sector D_4=sum E^2. The cube Z^*Z/2 is
84I+2 sum_faces(W_p+W_p^*), so the proposed field Hamiltonian differs from
the original K sum E^2+60delta-2delta sum_faces only by a scalar -144delta.
Thus the electric/magnetic pre-first behavior may survive this completion.

Why use the radius-two occupancy gate? Without it, C=sum_a E_a^*E_a at
rotor order has A^*C_Q A=Z^*Z/2, because two outward hops from distinct A
sites commute on P and each unordered pair has two orders. Then H4'=0:
naive local cancellation may remove the magnetic term as well. This is a
candidate exact identity to check, and must be preserved if confirmed. The
gate removes the connected virtual contribution at the other A corner of
a square. Disconnected pieces on larger graphs need a separate locality
and coefficient analysis; no general-volume result follows from the cube.

Unclosed obligations: exact generalized Schur coefficients/signs; physical
definition of diagonal extraction and gate on all sectors; boundedness and
gauge covariance; independent controls of pre-field preservation; uniform
microscopic target with C; strong joint limit and event recycling; actual
finite-spin controls; coefficient-tuning tolerance and alternative mechanisms.
A coefficient mismatch of order one could restore a fast operator; departures
of order epsilon^2 might instead add a bounded ordinary term. Neither has
yet been proved. Any result remains conditional on the explicit added law,
with its native selection/physical motivation separate.
