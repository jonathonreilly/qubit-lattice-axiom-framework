# Local gauge cooling with fresh permanent records

Status: personally derived conditional finite-volume theorem, awaiting
independent reconstruction. The local cooling operator is established prior
work; the argument below checks global attraction under explicit premises.
This is not an axiom-native state-preparation rule or a photon-phase proof.

## 1. Model and relation to existing work

Fix a finite set C of spin-half link configurations in one connected component
of a gauge-preserving plaquette-flip graph. A component fixes the Gauss charges
and any fluxes preserved by these flips. Let D=|C| and

    u = D^(-1/2) sum_(c in C) |c>.

For each plaquette p, orient every flippable pair a->b so that the field changes
by the same nonzero vector z_p, independent of the spectator links. Distinct
pairs for a fixed p have disjoint support in the configuration basis. Define

    s_ab=(|a>+|b>)/sqrt(2),  d_ab=(|a>-|b>)/sqrt(2),
    P_p^- = sum_pairs |d_ab><d_ab|,
    P_p^+ = sum_pairs |s_ab><s_ab|,
    L_p = sum_pairs |s_ab><d_ab|.

On nonflippable configurations these three operators vanish. Thus
L_p^dag L_p=P_p^-, L_p L_p^dag=P_p^+, L_p^2=0, and L_p u=0.
If W_p maps a to b, X_p=W_p+W_p^dag, and Z_e=2E_e on one link raised by W_p,
then P_p^-=(X_p^2-X_p)/2 and L_p=-Z_e P_p^-.
This equals the cooling jump c_p=Z_e(1-X_p)X_p/2 in Weimer et al.,
"A Rydberg Quantum Simulator", arXiv:0907.1657v2, Eq. (12).
Their paper describes the equal-weight target and demonstrates cooling in a
small numerical system. The jump and its physical purpose are not new here.

Consider only the specified generator

    G(rho)=-i[H,rho]+sum_p gamma_p D[L_p](rho),
    H=sum_p h_p P_p^-,  gamma_p>0, h_p real,
    D[L](rho)=L rho L^dag-{L^dag L,rho}/2.

There are no additional arbitrary jumps or diagonal Hamiltonians. The h_p may
be inhomogeneous and need not be proportional to gamma_p. If h_p>=0, H is a
Rokhsar-Kivelson Hamiltonian and u is a frustration-free ground state. The
attraction theorem does not require h_p>=0. Flips remain within C; it does not
assert communication between disconnected components, including frozen ones.

## 2. Conditional finite-volume attraction theorem

**Claim.** Under the model in Section 1, every initial density matrix supported
on span(C) converges to |u><u|. For each fixed finite model the convergence is
exponential, with model-dependent constants. The expected total number of
cooling jumps is finite. No lower bound on the decay rate uniform in volume,
efficient preparation time, or thermodynamic phase follows from this claim.

The proof uses the fixed displacement of a plaquette flip. Connectivity and a
unique common dark vector alone would not suffice; Section 5 gives a control.

### 2.1 Positive loss operator

Write K=sum_p gamma_p P_p^- and R=K/2+iH. Since the flip graph is connected,

    <v,Kv> = (1/2) sum_p gamma_p sum_(a,b in p) |v_a-v_b|^2

vanishes exactly on span(u). Therefore K is strictly positive on u-perp.
Both R u=0 and R^dag u=0. In particular |u><u| is stationary.

### 2.2 A separating auxiliary diagonal observable

Enumerate the links l=0,...,m-1 and set

    F(c)=sum_l 3^l E_l(c),  F=sum_c F(c)|c><c|.

The E_l take values +/-1/2. The values F(c) are distinct for distinct link
configurations: the largest differing power exceeds the sum of all smaller
powers. This F is an auxiliary proof device, not an extra physical term or a
preferred direction in the dynamics. For a p-pair a->b,

    F(b)-F(a)=Delta_p=sum_l 3^l z_(p,l),

which is constant across its spectator backgrounds. Set v(t)=exp(tF)u for real
t. The two amplitudes in each pair give the exact identity

    P_p^- v(t) = -tanh(t Delta_p/2) L_p^dag v(t).                 (1)

This includes all nonflippable configurations, where both sides vanish.

### 2.3 Exclusion of an invariant subspace orthogonal to the target

Suppose a nonzero W contained in u-perp were invariant under R and every L_p.
Let P_W project onto W, R_W=P_W R|W, and L_(p,W)=P_W L_p|W. Invariance implies

    P_W R^dag = R_W^dag P_W,
    P_W L_p^dag = L_(p,W)^dag P_W.

With f(t)=P_W v(t), equation (1) therefore gives

    [R_W^dag + sum_p (gamma_p/2-i h_p)
         tanh(t Delta_p/2) L_(p,W)^dag] f(t) = 0.               (2)

At t=0 the matrix in brackets is invertible: its Hermitian part is
P_W K|W/2>0. By continuity it stays invertible on some real interval around
zero. Hence f(t)=0 on that interval. Analyticity implies P_W F^n u=0 for all
n>=0. Since F has D distinct eigenvalues and u has a nonzero component on
each configuration, the D vectors u,Fu,...,F^(D-1)u span the full space by
the Vandermonde determinant. Thus W=0, a contradiction.

The exponentially large coefficients of F do not set a physical rate. This
argument is qualitative and does not supply a useful gap estimate.

### 2.4 From invariant subspaces to convergence

For completeness, the required finite-dimensional semigroup argument is as
follows. Let P0=|u><u|, Q=I-P0. Relative to P0 plus Q, R is block diagonal and
each L_p has blocks [[0,a_p],[0,B_p]]. The Q block sigma=Q rho Q evolves by
the autonomous completely positive, trace-nonincreasing semigroup

    A(sigma)=-R_Q sigma-sigma R_Q^dag
             +sum_p gamma_p B_p sigma B_p^dag,
    d Tr(sigma)/dt=-sum_p gamma_p Tr(a_p sigma a_p^dag).

If its trace did not tend to zero for some positive initial sigma, finite-
dimensional Cesaro averages would have a nonzero positive stationary limit
sigma_*. Stationarity and zero leakage imply a_p range(sigma_*)=0 for all p.
For a vector orthogonal to range(sigma_*), the diagonal stationary equation
then implies B_p range(sigma_*) is contained in range(sigma_*). The off-block
stationary equation implies R_Q range(sigma_*) is contained there as well.
Thus range(sigma_*) would be a nonzero W of the forbidden kind in Section 2.3.

It follows that exp(tA) tends to zero on every positive matrix, hence on every
matrix by linear span. All eigenvalues of A have strictly negative real part.
Finite-dimensional Jordan bounds give Tr(Q rho(t))<=C exp(-g t) for some
model-dependent C,g>0, uniformly over initial density matrices. Positivity
and the pure-state trace-distance bound give

    ||rho(t)-P0||_1 <= 2 sqrt(Tr(Q rho(t)))
                     <= 2 sqrt(C) exp(-g t/2).

The logic agrees with the invariant-subspace approach of Kraus et al.,
arXiv:0803.1463, Theorem 2. We supplied the argument because our exclusion
uses both the jumps and R, and because uniqueness of a dark vector alone is
not an adequate substitute.

### 2.5 Finite expected record production

In the usual resolved quantum-jump instrument the total instantaneous cooling
intensity is Tr(K rho(t)). Since K annihilates u,

    E[N_jump] = integral_0^infinity Tr(K rho(t)) dt
              <= ||K|| C/g < infinity.

Consequently N_jump is finite almost surely in that supplied instrument. If
each jump creates two permanent records, its expected total output is twice
this value. This does not give a deterministic finite storage bound. A fixed
finite arena without fresh capacity can exhaust its slots on some histories;
the ideal model assumes adequate fresh resources and export capacity.

## 3. Fresh-record implementation and its supplied resources

For one p, a fuel/spent ancillary degree of freedom has coupling

    C_p=L_p tensor |spent><fuel|+L_p^dag tensor |fuel><spent|.

Because L_p is a partial isometry from the orthogonal minus to plus subspace,
C_p^3=C_p. Starting with fuel, exp(-i theta C_p) gives data Kraus operators

    A0=I+(cos(theta)-1)P_p^-,   A1=-i sin(theta)L_p.

Choosing cos(theta)=exp(-gamma_p dt/2) gives exactly exp(dt gamma_p D[L_p])
after tracing the ancilla. Replacing spent by a fixed neutral permanent pair
changes the record number by two in A1. The coherent coupling conserves
N_record+2P_fuel. Its inverse exists and reuse of the same spent ancilla can
undo the cooling; the construction requires a fresh incoming ancilla for
each application, with outputs carried away. All old record contents remain
unchanged by the ideal interface. Local spin-half gauge neutrality of L_p
is inherited from the plaquette flip; any extra charged ancilla transport
would need its own checked Gauss-compatible routing.
The displayed conserved count accounts for fuel and record rest resources.
It does not establish conservation of an arbitrary additional interacting
field Hamiltonian during a collision; that energy balance remains open.

Combining the individual channels and exp(-iH dt) in a Trotter limit gives
the specified generator. At finite step the composition is a discretization,
not asserted to equal the full simultaneous semigroup. A fresh moving stream,
its initialization, controls, storage, and timing remain supplied. The earlier
autonomous single-carrier construction can implement a chosen finite gate
approximately under its own assumptions; it does not by itself establish an
autonomous many-carrier realization of this entire generator.

The conditional jump intensity is gamma_p <P_p^->, which depends on the field.
This is not the earlier field-independent classical occupation clock. The
outgoing records carry preparation information. The relative phase selected
by L_p is part of the engineered coupling, not derived from record permanence.

## 4. What this would add to the campaign

Previous ring constructions preserved or read out a supplied coherent state.
This model instead prepares the equal-positive-amplitude state from any
ordinary basis configuration in a chosen finite flip component. That is a
state-preparation bridge with explicit entropy export. The target is an RK
state. It does not establish a Maxwell photon, relativistic dynamics, an
infinite-volume Coulomb phase, a unique choice of law, or a native compiler
from one M2 site and the minimal record axioms. The repo's finite-volume RK
and phase-bridge notes remain the separate sources for their own claims.

## 5. Completed bounded controls

The companion runner passed its first complete execution. Its full results,
stdout, stderr, command and source identity are preserved alongside this note.

1. Exact local partial-isometry, separating-vector identity, fuel-dilation
   algebra, and channel composition Phi_a Phi_b=Phi_(ab), including signs.
2. Fixed displacement, distinct separating F, Gauss charges, and a spanning
   tree checked on the periodic 2x2x2 zero-flux component of 864 states. This
   is a traversal of that component, not a census of the entire Gauss sector.
   All 24 plaquette operators have 144 disjoint pairs there. Open one-square,
   two-square and cube controls have largest components of 2, 3 and 9 states.
3. Integral complex Liouvillian matrices for those three open components
   have exact nullity one, certified by a full-rank minor modulo 65537 and
   an exact target nullvector. Inhomogeneous gamma_p=p+1 and signed
   h_p=(-1)^p(p+2) are used. Numerical exponentials preserve trace/positivity
   and approach the target; their floating-point decay gaps are approximately
   0.5000, 0.4886 and 0.8677. Reward Poisson equations give expected total
   jumps from the selected basis state of 0.5, 1 and 3.22058 respectively.
   These numbers have no asserted volume-scaling significance.
4. A connected four-state graph where inconsistent matching orientations
   violate the fixed-displacement premise and create a mixed stationary trap:
   L1 pumps pairs (1->2),(3->4), L2 pumps (2->3),(4->1), each difference to sum.
   The common dark kernel is the uniform vector, but a two-dimensional
   orthogonal invariant subspace survives. Its normalized projector is a
   stationary density of purity 1/2, with H=0 or H=sum Pminus. Constant flip
   displacements would force F1=F3 and F2=F4, preventing a separating F.
   All these statements are checked exactly. This prevents using connectivity
   alone as a proof.

No control is a replacement for independent reconstruction of Section 2.

## Sources actually consulted

- Weimer et al., arXiv:0907.1657v2, abstract/introduction, gauge-theory section
  including Eq. (12), and the associated finite-system cooling description:
  https://arxiv.org/pdf/0907.1657 . The entire paper was not independently audited.
- Kraus et al., arXiv:0803.1463, Section III through Theorem 2 and its proof:
  https://arxiv.org/pdf/0803.1463 . Their sufficient criterion is context, not an
  imported assertion that our concrete operators satisfy it.
- Main dee2310d375f37a0ca4c8641e9a12aa7fabb8577: the full Sept. 3 spin-half
  cubic-ice RK/phase-bridge bounded note and the full Sept. 4 pure-model bounded
  note, as pinned in CLASSICAL_RECORD_GAUGE_AND_CUTOFF_SOURCE_CONTEXT.json.
