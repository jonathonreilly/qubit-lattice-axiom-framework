# Native half-line completion, finite horizons and exact permanence

Working conditional mathematics, personally derived 2026-09-14. No independent
review, native law selection, axiom change or realized Record claim.

## 1. Actual native target and conserved energy

Use the exact reduced-cell nine-pulse sequence in the two 2026-09-07 notes,
fully read at main b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf. Register order is
r,hv,hw,x,f,b0,b1,l0,l1; r=0 factors out. Ready head10, fuel1, labels00 allow
all eight matter/battery columns. With q=n_f, a=1-q, n=n_b1,
K=q(1+Y_x)+1/2+n_b0+2n_b1, p±=(1±Y_x)/2, P±=(1±Z_x)/2.
Accepted S_z=P_z p+ T2+P_z p- send fuel0, head01 and labels01/10;
refusal F=p+n leaves fuel/head/matter/battery and sets label11.
Sum S_z†S_z=I-F and F²=F, so the three-branch map V is an isometry.

The actual pulses are C(p+n,l0), C(p+n,l1), exp[-iπ p+ E_f,b1/2],
exp[-iπ p- X_f/2], C(a,l1), C(aP-,l0), C(aP-,l1),
exp[-iπ a E_head/2], exp[-iπ a]. Here C(P,l)=I+P(X_l-I).
Every pulse globally commutes with K and has support at most three native
qubits. The ready-input restriction of W9=U9...U1 is exactly V. Their native
parent boundaries, carrier tensor interpretation and preparation are supplied.
This analysis reconstructs these matrices rather than replacing the target
with a generic gate or an abstract outcome probability.

## 2. Semibounded clock with an outgoing tail

Let L=9, W0=I, Wn=Un...U1 for n<=L and Wn=WL thereafter. On ℓ²(N0),

    h=2J I-J sum_n (|n+1><n|+|n><n+1|), J>0,
    D=sum_n |n><n| tensor Wn,
    H=I tensor K+D(h tensor I)D†.

The sine transform diagonalizes h with eigenvalue 2J(1-cos k), 0<k<π;
therefore its spectrum is [0,4J]. D is unitary and [D,K]=0, giving a
semibounded autonomous H. On ready input Rψ,

    exp(-itH)(|0> tensor Rψ)
      =sum_n a_n(t)|n> tensor exp(-itK)Wn Rψ,
    a_n=(2/π) integral_0^π sin k sin((n+1)k) exp[-2iJt(1-cos k)] dk
       =exp(-2iJt)i^n[J_n(2Jt)+J_(n+2)(2Jt)]
       =exp(-2iJt)i^n (n+1)/(Jt) J_(n+1)(2Jt).

The last identity is the Bessel recurrence; the integral and its orientation
fix the sign (a1=+iJt+O(t²)). At t=0 use a_n=delta_n0.
No external switching or narrow arrival-time window is used.

Let eta_L(t)=sum_(n<L)|a_n|². For p=1-eta>0 define the normalized completed
clock chi=p^(-1/2)sum_(n>=L)a_n|n>. The actual joint pure output has overlap
sqrt(p) with chi tensor exp(-itK)Vψ, including any reference entanglement.
Their trace distance is exactly 2sqrt(eta); purification gives the same upper
bound on the ready-input channel diamond norm. After discarding the clock,
its orthogonal positions give a convex mixture of prefix channels. The
system-only diamond error from exp(-itK)V is at most 2eta. These are ready
input bounds, not arbitrary initial apparatus channel bounds, and do not
assert measurement or a selected classical outcome.

## 3. Explicit bounds uniform for all later times

Writing C_L=sum_(m=1)^L m²=L(L+1)(2L+1)/6 and using |J_m(x)|<=1,

    eta_L(t)<=min(1,C_L/(Jt)²), t>0.

A stronger elementary oscillatory-integral bound is available. For integer
1<=m<=L and x>=max(2m,144/π²), use
J_m(x)=π^-1 integral_0^π cos(mθ-x sinθ)dθ.
The unique stationary point θ0=arccos(m/x) belongs to [π/3,π/2]. Set
d=2/sqrt(x)<=π/6. On the central interval [θ0-d,θ0+d], absolute integration
costs at most 2d. The derivative φ'=m-x cosθ is monotone on [0,π], and at
each cut has magnitude at least xd/2 because sinθ>=1/2 along the segment
from θ0 to the cut. On either outside interval, integration by parts bounds
|integral exp(iφ)| by 2/min|φ'|<=4/(xd): the endpoint terms plus the total
variation of 1/φ' telescope to that bound. Hence

    |J_m(x)|<=8/(π sqrt(x)),
    eta_L(t)<=32 C_L/[π²(Jt)³]
      whenever Jt>=max(L,72/π²).

Consequently every t>=T0 has system error<=epsilon/2 if

    JT0>=max(L,72/π²,[128 C_L/(π² epsilon)]^(1/3)).

The half-error allocation leaves room for finite-clock approximation below.
For L=9, C_L=285. The asymptotic expansion at fixed L further gives, with
φ=2Jt-π/4,

    eta_L(t)=[E_L cos²φ+O_L sin²φ]/[π(Jt)³]+O((Jt)^-4),
    E_L=sum_even_m m², O_L=sum_odd_m m².

For L=9, E_L=120 and O_L=165. Both are positive, so this particular clock's
unfinished probability is of order t^-3 at late times. This is not a lower
bound on all possible apparatuses. The all-time sufficient bound above does
not depend on replacing the Bessel functions by their asymptotic expansion.
The Bessel integral and expansion are standard identities, checked against
NIST DLMF §§10.9,10.17; the split estimate is given explicitly here.

## 4. Positive qubit extension and resource accounting

For clock qubits with a_n=|0><1|_n and number n_n, use the bond operator

    J[n_n+n_(n+1)-a†_(n+1)a_n tensor U_(n+1)
                       -a†_n a_(n+1) tensor U†_(n+1)],

where U_(n+1)=I after the Lth gate. Add J n0. Each bond is positive: on
00 it vanishes; on11 it is 2J; on the one-excitation block its matrix is a
unitarily gauged J[[I,-I],[-I,I]], with eigenvalues0 and2J. Thus its norm is
2J and it has support on at most five qubits. Tail terms have two-site clock
support. The sum restricted to the one-hot sector equals the displayed h
under D. On the Hilbert direct sum of finite-excitation sectors, each fixed-number
sector is bounded: bond positivity and the bound of each bond by
2J(n_n+n_(n+1)) give 0<=H_clock<=4J N_clock, including the boundary term.
Thus every fixed-number restriction extends to a bounded selfadjoint operator,
and their orthogonal direct sum defines a nonnegative selfadjoint extension.
Only the one-hot sector is used by the operation theorem. K is bounded here
and commutes with every term. No assumption about a thermal infinite-density
representation is needed or asserted.

For a finite M-site truncation, add J n_(M-1) also, giving the same constant
2J diagonal at both ends. The sum is a full finite-qubit Hamiltonian without
a global one-hot projector. It preserves clock number and K; its operation
is asserted only in the prepared one-hot sector. The full finite clock term
has norm at most 2J(M-1)+2J=2JM; on the one-hot sector it is at most4J.

The infinite version supplies an infinite blank clock tail and static gate
couplings near its entrance. The finite version uses M clock plus nine
native qubits. Neither construction supplies a strict nearest-neighbor
physical embedding of the five-site entrance terms, homogeneous native
roles, a preparation mechanism, renewal or a thermodynamic cost theorem.
An infinite ready tail is a changed resource budget, not a free improvement.
The free energy K remains in the output and both K and total H are conserved.

## 5. Finite apparatus through a stated horizon

Embed the M-site clock in the half-line and compare its evolved |0> vector
with the infinite one. Put A=(h-2JI)/(2J); both infinite and finite A have
norm<=1. Degree k<M polynomials applied to |0> coincide in the embedding,
since a path needs at least M edges to see the first removed site. The
Jacobi-Anger/Chebyshev series and ||T_k(A)||<=1 give

    epsilon_M(T):=sup_(0<=t<=T)||a_infinite(t)-a_M(t)||
       <=4 sum_(k>=M)|J_k(2JT)|_uniform_bound
       <=4 exp[-mu M+2JT sinh(mu)]/[1-exp(-mu)], mu>0.

The first tail is understood at each t; Bessel absolute values themselves
are not asserted monotone in t. The second uniform bound follows directly
by shifting the generating-function contour:
|J_k(x)|<=exp[-mu k+x sinh(mu)], x>=0.
The common phase exp(-2iJt) cancels. D and exp(-itK) preserve vector norms;
therefore the result holds uniformly for arbitrary ready input/reference.
Triangle inequality and partial trace give, for T0<=t<=T,

    ||Phi_M(t)-Phi_target(t)||_diamond <=2eta_L(t)+2epsilon_M(T).

For 0<epsilon<1, T>=T0 and M>=L+1, a sufficient choice is

    M>= [2JT sinh(mu)+log(16/[(1-exp(-mu))epsilon])]/mu.

Combined with section3 this guarantees error<=epsilon throughout the stated
interval. At mu=1 the clock length grows at most linearly with JT with
coefficient2sinh(1), plus a logarithmic accuracy term. The bound is sufficient,
not a minimal apparatus cost. A finite-dimensional autonomous apparatus
still recurs. No infinite retention statement is made for fixed finite M.

## 6. Exact permanence boundary for semibounded continuous unitary dynamics

Hegerfeldt's 1998 theorem is a load-bearing external result; its needed
interval version has a short direct proof. Let H be selfadjoint and bounded
below, 0<=A<=I bounded, and ψ_t=exp(-itH)ψ. After a constant energy shift,
H>=0. For each vector φ,
Fφ(z)=<φ,A^(1/2) exp(-izH)ψ> is analytic in the lower half-plane and
continuous on its real boundary. If <ψ_t,Aψ_t>=0 on an open time interval,
A^(1/2)ψ_t=0 there, so Fφ vanishes there. Schwarz reflection through that
zero real boundary interval extends Fφ analytically, and the identity theorem
makes it identically zero. Thus the positive expectation vanishes for all
times. For a normal mixed state, decompose it into positive-weight pure
states; positivity forces every contributing component to obey the same
conclusion. No finite-dimensional recurrence assumption is required.

Take A=I-P for a fixed completed/persistent pointer projector. If its
probability becomes exactly one throughout an interval of later times under
the same closed semibounded H, it was one initially. A ready state outside
P cannot reach an exactly invariant completed subspace in finite continuous
time. This excludes deterministic exact permanent capture in that supplied
representation, including an infinite apparatus with a normal initial state.
It does not say the finite error bound of section3 is impossible.

For an exact isometry-channel version, use a maximally entangled ready input
and a reference. If the reduced channel equals V on an open interval, its
Choi state is the fixed pure |Omega_V><Omega_V|. Apply the theorem to
A=(I-|Omega_V><Omega_V|) tensor I_apparatus: the initial reduced channel
would already have to equal V. If the target is exp(-itK)V instead, a valid
interaction-picture reduction requires [H,K]=0 and H-K semibounded. Both
hold for the constructed native fixture (K bounded and commuting); those
conditions are not presumed for arbitrary open systems.

This theorem is about a single unitary trajectory and exact interval
probabilities. It does NOT rule out a random formation time with unbounded
support and permanent records on each conditionally updated trajectory;
then the ensemble completion probability is below one at every finite time.
It also does not transfer automatically to a nonnormal infinite thermal
representation with a two-sided Liouvillian, a discrete-time law, a moving
projector, time-dependent switching, conditional collapse, a dissipative
semigroup, or merely asymptotic/approximate locking. A full-line reversible
shift can send a stroboscopic ready state into a future-invariant half-line
subspace; integer times are not an open continuous interval.

## 7. Explicit irreversible comparison and its price

A supplied time-homogeneous GKSL clock on j=0,...,L with jumps
L_j=sqrt(gamma)|j+1><j| tensor U_(j+1), j<L, and free Hamiltonian K has an
absorbing completed clock state. In the commuting gauge, its block-diagonal
ready solution is a truncated Poisson process: for j<L,
p_j(t)=exp(-gamma t)(gamma t)^j/j!, while p_L=1-sum_(j<L)p_j.
The system channel differs from the freely evolved coherent target
exp(-itK)V by at most2sum_(j<L)p_j.
The completion time has the Erlang(L,gamma) law and is almost surely finite,
with no finite deterministic maximum. These statements are obtained directly
from the triangular master equation, not from the closed half-line clock.

If realized sign/refusal labels are desired in that supplied jump model,
split the LAST jump by the complete orthogonal label projectors P_z:
L_(L-1,z)=sqrt(gamma)|L><L-1| tensor P_z U_L, including label00 for a full
operator definition. Sum_z P_z=I and [P_z,K]=0 retain the same survival law
and conserve the modeled K observable. Final reduced output is the DEPHASED
native instrument exp(-itK)[sum_z P_z V rho V†P_z]exp(itK),
not the coherent isometry channel.
Each chosen unraveling trajectory keeps its sampled final label thereafter.
The last statement depends on an explicitly supplied trajectory/readout law.
A Lindblad semigroup by itself does not select a unique unraveling or derive
a single ontological Record. Complete positivity, rates, Markov reservoir,
input readiness and any Born interpretation remain supplied. The existing
2026-09-07 autonomous-head note already uses an open irreversible law; this
comparison does not claim to invent that route or close its reservoir gap.

## 8. Axiom-facing conclusion and next obligations

The current minimal axioms require permanent one-per-site Records. They do
not identify a Record with a fixed projector in a closed positive-energy
continuous-time Hilbert evolution, nor supply H, time/rates, the clock carrier
or a unitary formation law. Therefore section6 is a conditional bridge
incompatibility, NOT evidence requiring an axiom update. The construction
in sections1-5 closes a finite observation-window defect for an approximate
coherent native operation at a stated infinite apparatus cost, and gives a
finite horizon cost. It does not derive permanent classical formation.

Next load-bearing tests: derive a formation/readout bridge selected by the
native law; compile entrance interactions into strict physical locality;
determine whether a permanent Record is an invariant observable, a conditioned
history append, a superselection sector or an additional postulated law;
and price preparation/renewal. An axiom update would require showing that
all authorized representations of the actual axioms fail a demanded physical
prediction. This note does not establish that much stronger proposition.
