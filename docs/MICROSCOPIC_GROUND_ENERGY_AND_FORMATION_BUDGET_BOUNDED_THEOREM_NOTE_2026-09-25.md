---
claim_id: microscopic_ground_energy_and_formation_budget_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Conditional fixed-volume full microscopic energy/activity transfer and ground-input energy budget for the supplied compensated formation model; no selected physical vacuum, calibrated heating prediction or reservoir construction."
upstream_dependencies:
  - bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24
  - native_ground_energy_and_original_formation_bounded_theorem_note_2026-09-25
runner: scripts/microscopic_ground_energy_and_formation_budget_2026_09_25.py
---

**Type:** bounded_theorem
**Status:** conditional mathematics with selective independent checks; no retained audit status.

# Microscopic ground energy and the original formation budget

In the supplied compensated model, an energetic ground state cannot remain
a quiet vacuum under the same original formation dynamics. The common-law
energy/activity constraint transfers to the full finite-spin Hamiltonian
under an actual-energy cap. At fixed finite cubic volume and sufficiently
small fixed K/delta, followed by increasing spin resource, every ground-input
density must acquire mean excitation energy 2 delta n by a preparation-dependent
first hitting time whose limsup is at most 5/(16 kappa). These are conditional
statements about that Hamiltonian and instrument. No physical vacuum or
observed heating rate is identified.

The two complete root arguments follow. Part I is the new microscopic transfer;
Part II composes it with exact number balance. The common-law filling trial
and energy/activity inequality imported in Part I are supplied by the native
ground-energy parent in this branch's base. Their separately checked arguments
remain conditional, with no audit promotion. This publication is stacked on
that open review branch rather than silently treating its result as main.

The root personally derived both arguments. Each has a sealed blind PRE and
a released-source POST. Part I's checker reconstructed the microscopic form
comparison, actual-energy control, high/low coherence estimate and spectral
infima. Part II's checker reconstructed the residence and energy-accounting
composition with Part I explicitly imported; it did not independently reprove
Part I. The final released-source publication comparison is a correspondence
review, not an additional blind derivation. Complete exposure histories and
original status wording are preserved in the evidence packet.

The finite-spin correction is an anticommutator, whose sign does not establish
operator order. The comparison controls forms on bounded gated-electric-energy
states; it does not control all occupied-link flux or prove global operator
convergence. A vanishing high-cluster population can retain finite mean energy.
The proof uses a one-sided energy comparison and keeps high/low coherences.
These distinctions are load-bearing, not optional numerical approximations.

Part II bounds total time spent in a low-energy region, including returns.
Its hitting time depends on the prepared ground density. It does not assert
a common laboratory readout time, positive initial power, monotone energy,
temperature, an individual quantum trajectory's energy, or a photon lifetime.
An implementation conserving an additive endpoint energy must account for
the system's gain; a separate interaction-energy or work contribution changes
that ledger. For an unbounded reservoir, the mean-energy statement presupposes
well-defined finite means (or the corresponding nonnegative excitation forms).
The ground-environment example presupposes an attained normal ground state
and actual conservation of the total energy observable; a formal commutator
on an unspecified domain alone is insufficient.

PRE-only stronger conclusions, extra controls and counterexamples retain their
independent provenance. They are not silently folded into the root claims.
In particular, the noncompact flux and rare-high-tail examples constrain
stronger microscopic interpretations, and the independent budget PRE's
time-average and late-time improvements are separate results in its report.


## Part I — transfer to the full microscopic law

### Energy-bounded transfer to the full original compensated generator

Personally derived conditional theorem, 25 September 2026. Separate scoped
PRE and POST are complete; no retained audit status. The primary agent personally
derived the identities, estimates and microscopic transfer below. The
common-law energy/activity inequality used in Section 6 is the explicitly
provisional author36 result; this packet does not independently establish it.
No supplied interaction, energy zero, instrument or preparation is changed.

The question is whether the common-law obstruction to a stationary energetic
minimum survives the actual fast dynamics. Weak energy measures alone cannot
answer this. The additional hypothesis here is an upper bound on the actual
full Hamiltonian mean, not trace closeness, an effective energy bound, or an
assertion that physical preparations meet that bound.

#### 1. Supplied model and exact finite-spin coefficient

Fix a finite simple bipartite graph, all physical matter/field words with
Gauss div E=q-1_A, unsigned hard-core matter, integer spin S>=1 and
C=S(S+1). Orient each link from A to B. Let F_(a,S) be the original outward
sum, W the number of A vacancies, P=1_(W=0), and

    T_S=-sum_a(F_a+F_a*),
    D_a(q,E)=1_(q_a!=0) sum_(b~a,q_b=0) E_ab(E_ab-q_a),
    X_a=D_a/C,
    G_a=product_(c!=a,distance(c,a)<=2) n_c,
    C_S=sum_a (F_a*F_a+X_a) G_a.

D_a here is defined on the FULL charge space; D=sum_a D_a on P. The gate
multiplies the entire bracket, as in the common-law parent. D_a>=0 because
E is integer. On the spin box D_a<=z_a C, z_a=degree(a). The microscopic law is

    H_fast=delta epsilon^-4(W+epsilon T_S+epsilon^2 C_S),
    L_(j,fast)=sqrt(kappa) epsilon^-1 j_S,
    epsilon^2 C=delta/K,                 K,delta,kappa>0 fixed.       (1)

Keep every original resolved sign, or the specified unnormalized coherent
sum of the two signs on one edge. No coherent combination of different edges
or field-only postbirth space is substituted.

Let M_a=PF_a*F_aP, M=sum_a M_a, A=Pi1 T P and Z=Pi2 T Pi1 T P. The bounded
compensation parent gives the canonical fourth-order coefficient

    H4_S=M^2-{M,C0}/2+A*C1 A-Z*Z/2,
    C0=M+D/C,

where C1=Pi1 C_S Pi1. Its exact local expression is

    H4_S=-2 sum_(a<c,distance(a,c)=2) (F_cF_aP)*(F_cF_aP)
          -(1/(2C)) sum_(a,c: c=a or distance(a,c)=2) {M_a,D_c}.    (2)

The second sum is ordered and includes a=c. To prove it, distinct outward
operators commute, including zero for a shared excluded destination. The
two orders for each pair have equal amplitudes, and different pairs of
vacated A sites have orthogonal ranges. Thus Z*Z/2 is twice the sum of all
unordered pair Grams. In the one-hole-a block the a bracket vanishes, all
brackets at overlapping c are gated off, and exactly the distant c brackets
survive. Their F_c*F_c terms cancel the distant part of Z*Z/2. Their X_c
terms give M_a D_c/C: for distant stars all factors commute and the hop
leaves D_c unchanged. These cancel the distant ordered terms of {M,D}/(2C).
The remaining terms are exactly (2). This argument includes spin-boundary
zeros and all returning charges; it is not a rotor-only path identity.

The correction in (2) is an anticommutator. Its negative sign and
nonnegative matrix entries do NOT make it negative in operator order. None
of the following argument uses that invalid inference.

#### 2. Uniform form comparison on states with bounded gated electric mean

Embed the physical spin space isometrically in the full rotor space. Write
F_a^r for the unit rotor outward sum. For a vector psi in the spin box, each
legal outward input edge has spin weight sqrt(1-u),

    u=E(E-q_a)/C in [0,1],     (1-sqrt(1-u))^2<=u.

A rotor hop leaving the box is retained in the comparison; its spin weight
is zero and u=1. Sum the finitely many edge partial shifts and use
Cauchy--Schwarz. On any relevant fixed A-occupancy input block,

    ||(F_a-F_a^r)psi||^2 <= z_a <psi,D_a psi>/C.                   (3)

Define the full nonnegative diagonal D^full=sum_a D_a also on intermediate
hole sectors. Every outward path removes terms from this diagonal: it
empties its A site and fills an empty B site. Its changed electric link is
among the removed terms. Other retained terms are unchanged. Therefore
D^full(output)<=D^full(input) for every basis path. Interference between
paths is not discarded: each output has at most z_a predecessors, and
each input has at most z_a outgoing paths. Hence

    <F_a psi,D^full F_a psi> <= z_a^2 <psi,D^full psi>.             (4)

Use the exact decomposition

    F_c F_a-F_c^r F_a^r=(F_c-F_c^r)F_a+F_c^r(F_a-F_a^r).

The first argument F_a psi remains in the spin box, so (3)--(4) apply.
Uniform bounds ||F_a||,||F_a^r||<=z_a then bound the difference of every
pair-Gram expectation by a graph-dependent constant times
sqrt(<D>/C) for normalized P vectors.

For the remaining correction use D_c^2<=z_c C D_c on the spin box:

    |<psi,{M_a,D_c}psi>|/C
      <=2 ||M_a psi|| ||D_c psi||/C
      <=2 z_a^2 sqrt(z_c <D_c>/C).                               (5)

Thus there is a finite graph-dependent constant A_G, independent of S,
for which, writing h_S=KD+delta H4_S and h=KD+delta H4_r,

    |<h_S>-<h>| <= delta A_G sqrt(<D>/C).                        (6)

Here h and h_S are evaluated on the same embedded spin vector. For a
normal density the identical bound follows by its spectral decomposition
and Cauchy--Schwarz over its weights. Only the first moment of D is used.
The parent gives a uniform bound ||H4_S||<=M_G; the rotor H4 is bounded too.
For fixed K>0, any uniform upper bound on <h_S> therefore bounds <D>.
No coercivity of D in every electric direction is required.

Let e_S=inf spectrum(h_S on the physical spin P space) and e_*=inf spectrum h
on the full physical rotor P space. Then

    e_S -> e_*.                                                   (7)

For the upper bound take a finite-electric-support normalized rotor vector
with Rayleigh quotient arbitrarily close to e_*. Finite support is a form
core for KD plus bounded H4; for large S it is inside the spin box, and (6)
applies. For the lower bound use spin minimizing states: the preceding
upper bound and uniform M_G bound their <D>, so (6) bounds e_S below by
e_*-o(1). No rotor eigenvector, compact resolvent, or minimum in any
continuous cycle-angle fiber is assumed. This proves convergence of
infima, not global operator-norm convergence or all energy moments.

#### 3. Original formation intensities on the same energy-controlled states

The leading target mark is B_(j,S)=P j_S F_a P. With T=-sum(F+F*), the
parent convention B_j=-Pj Pi1 T P gives precisely this plus sign. The
initial scratch allowed an irrelevant minus sign in this amplitude; the
positive comparison here fixes the actual convention.

For a selected creation edge b, the preceding outward hop must use a
different vacant neighbour. The electric field on b therefore has not
changed. For every integer e and q,sigma in {+1,-1},

    e(e+sigma) <= 2e(e-q)+2.                                    (8)

For q=sigma=+1 the residual is (e-1)(e-2)>=0; for q=sigma=-1 it is
(e+1)(e+2)>=0. For q=-sigma the residual is e(e-q)+2>=0.
This is an all-integer proof, including boundary values.

Use

    j_S F_a-j_r F_a^r=(j_S-j_r)F_a+j_r(F_a-F_a^r).

The first argument is again in the spin box. The creation-weight analogue
of (3), (8), and the same bounded path/predecessor multiplicities give

    ||(B_(j,S)-B_(j,r))psi|| <= b_G sqrt((<D>+1)/C).               (9)

For example the square of the first term is bounded by
2 z_a^2(<D>+1)/C; the second is bounded by z_a<D>/C. No reverse hop or
creation path has been projected away. The coherent instrument is a fixed
sum of two such maps, so it has the same order with a finite changed
constant. Uniform boundedness of B_j and a finite sum over the complete
instrument then yield

    |Tr Gamma_S rho-Tr Gamma_r rho|
       <= kappa B_G sqrt((Tr D rho+1)/C),
    Gamma_S=kappa sum_j B_(j,S)*B_(j,S).                         (10)

The mixed-state extension again uses a weighted Cauchy--Schwarz inequality.
Equality of the resolved and coherent losses is not needed to establish
this transfer; both original choices are retained separately in the proof.

#### 4. Actual full energy controls high-cluster contamination

Use the exact canonical cluster rotation U from the bounded compensation
parent. All its estimates are uniform in S on this fixed graph. In rotated
coordinates the Hamiltonian commutes with W exactly, with low block

    P U*H_fast U P=h_S+R_S,       ||R_S||<=c_G delta epsilon^2.    (11)

Every other block is at least delta/(2 epsilon^4) for small epsilon.
The low block has a uniform lower bound -c0, since D>=0 and H4_S is
uniformly bounded. The cluster unitary respects Gauss and N, since those
commute with both the exact spectral projections and W.

Let rho_S be ANY normal microscopic spin density, including coherences
between W or N sectors. Suppose its actual mean satisfies E_S=Tr H_fast rho_S
<=Ecap, with Ecap fixed independently of S. Set r=U*rho_SU, p=Tr P r,
w=1-p and sigma=P r P/p, which is defined for all sufficiently large S.
Exact block diagonalization, not an omission of coherences, gives

    E_S >= -c0(1-w)+delta w/(2 epsilon^4),
    w=O_(Ecap,G,K,delta)(epsilon^4).                            (12)

The high block is nonnegative. From (11),

    Tr h_S sigma <= (E_S+O(delta epsilon^2))/p
                  <= E_S+O_(Ecap)(epsilon^2).                  (13)

The second step uses both the uniform lower energy bound and the upper
cap; w=O(epsilon^4). In particular Tr D sigma is uniformly bounded.
Equations (6) and C^-1/2=epsilon sqrt(K/delta) imply

    Tr h sigma <= E_S+O_(Ecap,G,K,delta)(epsilon).                (14)

This is an upper comparison for the low-state energy. The full mean need
not converge to that energy: a tiny high-cluster population may retain a
finite positive contribution. The one-sided bound is exactly what is
needed below.

#### 5. Full fast intensity, with the high/low cross terms retained

The parent first rotation coefficient gives, as a map from the entire P
spin space into the full space,

    epsilon^-1 U*j_SU P=B_(j,S)+O_G(epsilon).                   (15)

On the complement its norm is O_G(epsilon^-1). To bound general density
coherences, use Hilbert--Schmidt amplitudes with r^(1/2):

    X_j=sqrt(kappa) epsilon^-1 U*j_SU P r^(1/2),
    Y_j=sqrt(kappa) epsilon^-1 U*j_SU (1-P) r^(1/2).

The complete full intensity is sum_j ||X_j+Y_j||_HS^2. Equation (15)
bounds sum||X_j||^2 uniformly and gives

    sum||X_j||^2=p Tr Gamma_S sigma+O(epsilon).

Equation (12) bounds sum||Y_j||^2 by O(epsilon^-2 w)=O(epsilon^2).
Cauchy--Schwarz in the direct sum of channel Hilbert--Schmidt spaces
bounds the total cross term by O(epsilon). It is NOT set to zero. Thus

    Tr Gamma_fast rho_S=Tr Gamma_r sigma+O_(Ecap)(epsilon),
    Gamma_fast=kappa epsilon^-2 sum_j j_S*j_S.                 (16)

The replacement p->1 costs O(epsilon^4), and (10) costs O(epsilon).
All constants here are for the fixed graph and fixed positive K,delta,kappa.
They are not uniform in g, volume, time, or a chosen laboratory calibration.
No energy-variance bound or inference from weak-measure convergence is used.

Also the full microscopic spectral infimum obeys

    inf spectrum H_fast -> e_*.                                (17)

The high blocks diverge positively while the low infimum differs from e_S
by O(delta epsilon^2); combine (7) and (11). This does not assert convergence
of every spectral edge or every preparation's supported energy law.

#### 6. Conditional stationarity consequence for the cubic model

Now take the even degree-six cubic torus L>=6, n=L^3/2. Import ONLY the
following explicitly provisional author36 common-law inequality, including
its author35 half-filling trial dependency: at fixed L and sufficiently
small K/delta, every normal finite-energy rotor density obeys

    Tr Gamma_r sigma >= (16/5)kappa n
           -(4kappa/(5delta))(Tr h sigma-e_*).                 (18)

Its proof, constants and thresholds are separate source-bound obligations;
root37's new work is the full microscopic transfer (2)--(17). Root read the
distinct independent36 PRE before finalizing this packet; that PRE uses a
different affine operator bound and is not silently substituted for (18).
Its stronger numerical constants are not claimed here.

Combining (14), (16), and (18) gives, uniformly over actual full-energy
capped microscopic families,

    Tr Gamma_fast rho_S >= (16/5)kappa n
         -(4kappa/(5delta))(Tr H_fast rho_S-e_*)-O_(Ecap)(epsilon).
                                                                    (19)

This is a bound for the FULL original compensated finite-spin generator.
The resource limit is taken at fixed positive K,delta,kappa, AFTER selecting
a fixed small K/delta permitted by (18). It is not an arbitrary joint limit.
Finite-spin ground states exist; by (17) their intensities have liminf at
least (16/5)kappa n. They cannot be stationary for sufficiently large S.

For the full law [N,H_fast]=0 and [N,L_j]=2L_j, with N bounded on the fixed
graph. Consequently every stationary microscopic density has Gamma_fast
mean zero. Applying (19) on any subsequence with bounded upper mean energy
proves for ANY stationary family

    liminf_(S->infinity) Tr H_fast rho_(stationary,S)
         >= e_*+4delta n.                                      (20)

If the liminf is finite below this value, it admits such an energy-capped
subsequence, a contradiction. A positive infinite liminf already satisfies
the inequality. There is a uniform lower energy bound, so a negative infinite
liminf is impossible. In conjunction with (17), this separates asymptotic
stationary energies from the actual microscopic ground energy. Darkness
alone at a single instant still need not imply stationarity.

#### 7. Controls, failed attempt, and physical boundary

primitive_spin_energy_controls.py constructs complete Gauss spaces on four-
and eight-cycles directly from all allowed charge words and integer cycle
flows. Six full-space cases test (2), the exact second-order term, both full
original losses, every outward path's D monotonicity, and spin-boundary paths.
At S=1 all operations in those coefficient checks are exactly representable
binary rational arithmetic, and both coefficient residuals are zero. The
larger-spin fourth-order maximum residual is 1.066e-14; these floating rows
are not interval enclosures. The eight-cycle includes four ordered distant
A pairs, so its test does not collapse all compensation gates to one case.

Four separate four-cycle rows use K=100,delta=kappa=1 and S=1,2,4,8. Exact
matrix diagonalization and canonical low-cluster rotation test the mechanism
behind (11), (15)--(17), not the cubic inequality (18). The ground energies
are approximately -3.98009,-4.00663,-4.01598,-4.01888; original intensities
approach eight. The embedded rotor means stay near -4.019999. Low-block
remainder/epsilon^2 is 10.74 through 14.15. Numerical eigenvector residual
reaches 6.77e-8 at S=8; no asymptotic theorem rests on numerical extrapolation.

The initial all-A-plus, zero-field bare P word has fast intensity zero but
actual mean energy 4KC=800,2400,8000,28800 in those four rows. It violates
the uniform energy cap. This is a direct control of why trace closeness to
P alone cannot replace (12), consistent with the earlier high-tail findings.
The proof does not claim energy-bounded preparation of an actual lab input.

Attempt01 stopped at an overly strict floating equality between resolved
and coherent losses in the S=2 four-cycle. Its measured difference in the
completed diagnostic is 2.220446049250313e-16. Source, stderr and failed
receipt are preserved. Attempt02 retains exact equality for S=1 and records
an explicit floating residual with tolerance for other spins; it also makes
sparse diagonal float types explicit to remove a SciPy future warning.
It completed in 0.452311916 seconds, exit zero, empty stderr. Every result
row and the complete code were personally read. The separate four-integer-
quadratic checks corroborate (8); its all-integer proof is given above.

This conditional result tests an exact missing step in the observation
bridge: whether a suggested energetic vacuum would stay stationary under
the same microscopic formation law. It does not identify that minimum with
the observed vacuum, derive a native preparation, set physical units, supply
a reservoir, predict detector lifetimes, or rule out driven nonequilibrium
states or constrained sectors. All actual matter and original formation
outputs are retained. The assumptions remain supplied, the common-law
inequality remains a labelled dependency, and no new axiom, empirical
confirmation, broad framework no-go or TOE completion follows.

## Part II — residence and actual energy supply

### Actual ground-state heating and the required energy source

Personally derived conditional consequence, 25 September 2026. This composes
the separately checked root37 microscopic theorem in Part I
with the existing exact number balance. It is NOT an independent proof of
root37. No new interaction, bath, axiom, or physical identification is adopted.

The proposed physical identification being tested is that an energetic
minimum of the supplied full matter/field Hamiltonian is a persistent vacuum
under that SAME original formation law. The test uses the actual microscopic
Hamiltonian mean above its own minimum, rather than a selected-jump mean,
an effective energy proxy, or a field-only postbirth approximation.

#### 1. Exact premises and the provisional imported estimate

Use the full original compensated spin model on an even degree-six cubic
torus of side L>=6. Set n=L^3/2. Keep K, delta, kappa positive, at a fixed
K/delta sufficiently small for the explicitly imported common-law bound.
Then let S tend to infinity with

    C=S(S+1),  epsilon^2 C=delta/K,
    H_S=delta epsilon^-4(W+epsilon T_S+epsilon^2 C_S),
    L_(j,S)=sqrt(kappa) epsilon^-1 j_S.

The entire compensation bracket remains vacancy gated. All physical charges,
electric fields, and resolved signs or the specified unnormalized coherent
instrument are retained. Denote Gamma_S=sum_j L_(j,S)*L_(j,S) and

    E0_S=min spectrum H_S,
    e_*=inf spectrum h_rotor.

Finite-spin physical spaces are finite dimensional. Root37 provisionally
establishes E0_S->e_* and, for every fixed upper energy cap Ecap, a remainder
r_S(Ecap)>=0 tending to zero such that EVERY microscopic density with
Tr H_S rho<=Ecap obeys

    Tr Gamma_S rho >= (16/5) kappa n
          -(4 kappa/(5 delta))(Tr H_S rho-e_*)-r_S(Ecap).     (1)

Its uniformity over energy-capped states is essential. Fixed-time weak
convergence of energy distributions would not supply (1). The common-law
energy/activity estimate and its half-filling trial are upstream dependencies,
not independent conclusions of this note. The order of limits is fixed L,
fixed small K/delta, then spin resource. No volume-uniform threshold is assumed.

On the full charge space the original operators satisfy exactly

    [N,H_S]=0,  [N,L_(j,S)]=2 L_(j,S),
    d Tr N rho(t)/dt=2 Tr Gamma_S rho(t).                    (2)

Total Gauss charge is sum_x q_x=n, and n_x=|q_x| for the hard-core local
charges. Hence N>=n. Occupancy gives N<=2n. These bounds hold outside P
as well. Because n is even on these tori, the upper bound is compatible
with the total-charge parity; the proof needs only the upper bound.
Integrating (2), for every initial microscopic density and every T>=0,

    integral_0^T Tr Gamma_S rho(t) dt
       =(Tr N rho(T)-Tr N rho(0))/2
       <=(2n-Tr N rho(0))/2 <=n/2.                         (3)

Equation (3) is exact at each S for the full original dynamics, including
all quantum coherences. It is not a count-rate approximation.

#### 2. Total residence time near the actual microscopic minimum

Fix alpha with 0<alpha<4, and define the excitation-energy region along an
arbitrary actual trajectory by

    A_(S,alpha)={t>=0: Tr H_S rho(t)-E0_S <= alpha delta n}.

Since E0_S->e_*, all states in this region have a common upper energy cap
for sufficiently large S, for example Ecap=e_*+(alpha+1)delta n. Put

    eta_S=r_S(Ecap)+(4 kappa/(5 delta)) |E0_S-e_*|,
    gamma_(S,alpha)=(4 kappa n/5)(4-alpha)-eta_S.             (4)

Then eta_S->0 and gamma_(S,alpha)>0 eventually. Applying (1) to each
state in A_(S,alpha) gives Tr Gamma_S rho(t)>=gamma_(S,alpha).
Outside the region, Gamma_S remains nonnegative. Integrating this
pointwise inequality and using (3) proves

    |A_(S,alpha) intersect [0,T]|
       <=(2n-Tr N rho(0))/(2 gamma_(S,alpha)),              (5)

where |.| is Lebesgue time measure. Letting T increase gives the SAME bound
on total residence time over the entire infinite future, including any
number of returns. All functions are continuous at finite S; there is no
measurability or domain issue. No assumption that energy is monotone is used.

In particular, uniformly over arbitrary initial-state families,

    limsup_(S->infinity) |A_(S,alpha)|
       <= 5/[8 kappa (4-alpha)].                          (6)

The sharper numerator in (5) uses the actual initial expected N. The
uniform-time conclusion comes from an exact balance plus a state-uniform
inequality. We have not extrapolated a fixed-time approximation to infinity.
There is still no quantitative resource threshold: r_S is an asymptotic
remainder with fixed-graph constants from root37.

#### 3. A full mean-energy gain from any ground-state input

Now take ANY initial density supported on the ground eigenspace of H_S,
including mixtures of number sectors and coherences inside a degeneracy.
Its initial mean is exactly E0_S. Define the first hitting time

    T_(S,alpha)=inf{t>=0: Tr H_S rho(t)-E0_S >= alpha delta n}.

Before this time the trajectory is in A_(S,alpha). If the time were infinite,
(5) would be contradicted. Thus it is finite for sufficiently large S and

    T_(S,alpha) <= (2n-Tr N rho(0))/(2 gamma_(S,alpha)),
    limsup_(S->infinity) T_(S,alpha)
       <= 5/[8 kappa (4-alpha)].                          (7)

Continuity implies that the full system mean energy gain at the first
hitting time is alpha delta n. For the useful concrete choice alpha=2,

    full mean-energy gain = 2 delta n,
    limsup first hitting time <= 5/(16 kappa).             (8)

These statements concern the actual H_S and actual rho(t), not a rotor
proxy or a postselected output. Every ground input is covered, so no
nondegeneracy assumption or explicit many-body ground vector is needed.
This does NOT assert a positive instantaneous energy derivative at t=0:
successive jumps may initially move within a degenerate ground space.
It also does not give a monotone energy curve, a final equilibrium, an
individual trajectory's energy measurement, or a temperature.

The n in (8) is the number of A sites in a fixed finite graph. It is not
yet a measured volume. The supplied delta and kappa are not calibrated
joules and seconds. A physical interpretation of a persistent energetic
vacuum must confront (7) after those identifications and finite-resource
errors are justified; the present statement alone is not an experimental
exclusion or an observed heating prediction.

#### 4. What an energy-conserving implementation would have to supply

The positive difference in (8) is a system internal-energy gain for the
supplied Hamiltonian. The generator itself does not specify a reservoir
ledger, so calling it heat, work, absorbed light, or energy created from
nothing would add an unsupported interpretation.

A precise compatibility test can nevertheless be made. Suppose a proposed
implementation has an additional semibounded Hamiltonian H_R, and the
initial and readout energies are the additive H_S+H_R, with no omitted
interaction energy or externally supplied work between those endpoints.
If its total evolution conserves that additive total energy, then

    Delta <H_R> = -Delta <H_S>.                            (9)

Consequently an implementation reproducing (8) must provide at least
2 delta n of reservoir/other-system excitation energy above its lower bound
by that time. Interaction energy or externally supplied work could instead
account for it, but must then be included in the ledger. No implementation
has been constructed by writing (9).

In particular a system ground input and an environment also supported on
its ground subspace cannot reproduce (8) through an exactly energy-conserving
channel for H_S+H_R. Indeed

    H_S-E0_S >=0,  H_R-E0_R >=0.

The initial total excitation mean is zero. Conservation and positivity force
both excitation means to remain zero. Equivalently, a unitary commuting with
H_S+H_R leaves the total ground subspace invariant. Such a channel preserves
the system ground subspace, contradicting (7)-(8).

This is a test of a ZERO-EXCITATION environment with the stated endpoint
energy accounting. Passivity alone is not sufficient: a finite-temperature
passive reservoir has energy that can heat a ground-state system. A prepared
excited reservoir, externally driven apparatus, stored interaction energy,
or another justified state-selection mechanism is not excluded. None is
introduced as a new primitive here.

#### 5. Verification and claim boundary

This is an analytic composition. No new numerical experiment is claimed.
Its separate scoped PRE and POST are described in the publication overview. Source identities bind the existing exact number
balance and the root37 candidate. The algebra is displayed so that the
state-uniform remainder, capacity factor two, ground-energy reference, and
order of quantifiers can be reconstructed separately. The root37 microscopic
controls do not numerically establish (6)-(8) on cubic tori.

N1: the tested route is an energetic ground-state vacuum under the unchanged
original birth-only generator. Other physical preparations remain open.
N2: (1) is an explicit provisional import, not a second independent proof.
N3: fixed graph, positive couplings, small K/delta, charge background and
finite spin before the resource limit are load-bearing.
N4: the resource remainder is uniform on a chosen energy cap, not on volume,
couplings or every physical laboratory scaling.
N5: total occupation time is bounded; a pointwise relaxation or monotone
heating law is not inferred.
N6: actual microscopic mean energy gain is distinguished from heat/work and
from a selected detector mark's energy distribution.
N7: driven preparations, constrained sectors, dark stationary states and
reservoir energy remain live alternatives. The main already contains
unsaturated stationary states and homogeneous number balance; neither is
claimed as new here.
N8: physical scale, preparation, readout identification and error calibration
remain open. No observed fit, whole-framework no-go, retained audit verdict,
new axiom, or TOE completion follows.

## Verification and physical boundary

The primary runner freshly reuses the exact root microscopic-control source
in a temporary directory and preserves its complete stdout, stderr and JSON
artifact. The exact S=1 coefficient controls and floating cycle diagnostics
test the transfer mechanism. They do not numerically prove the small-K/delta
cubic inequality or the analytic residence theorem. The initial floating
equality failure, its narrow recorded repair, all earlier evidence and the
separate checker scopes remain available. Fresh source reuse creates no new
independence; floating diagnostics are not certified interval enclosures.

Limits are fixed graph, fixed positive K,delta,kappa with small K/delta selected
under the common-law parent, then increasing spin resource. The remainder is
uniform on each fixed actual-energy cap. No numerical resource threshold,
uniform volume limit or physical scale calibration is asserted. All original
matter states, formation signs and spin-boundary paths remain in the law.

The implication for the observation bridge is specific: a proposed persistent
energetic vacuum needs a justified preparation, state-selection mechanism and
energy supply or accounting. Those are not supplied by naming the ground
state. Driven or constrained preparations and other justified implementations
remain open. These statements do not compare a predicted number with data,
exclude the whole framework, add an axiom, construct a reservoir or complete
a theory of everything.

## Imports

- [bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional parent within its stated scope.
- [local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional parent within its stated scope.
- [local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional parent within its stated scope.
- [formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24](FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional parent within its stated scope.
- [native_ground_energy_and_original_formation_bounded_theorem_note_2026-09-25](NATIVE_GROUND_ENERGY_AND_ORIGINAL_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-25.md): conditional parent within its stated scope.

## Reproduction and evidence

Run `python3 scripts/microscopic_ground_energy_and_formation_budget_2026_09_25.py` from the repository root. Complete fresh results are
under `outputs/microscopic_energy_budget_20260925/`. Original arguments, failed attempts, independent reports,
source bindings and final correspondence are in [the evidence directory](../.claude/science/physics-loops/mobile-record-microscopic-energy-budget-20260925/).
