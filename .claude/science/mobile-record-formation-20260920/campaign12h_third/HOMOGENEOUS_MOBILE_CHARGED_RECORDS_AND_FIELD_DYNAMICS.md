# Mobile charged records without a fixed Gauss background

2026-09-22. Author conditional construction and local-limit proof; independent
reconstruction pending. This is a different supplied microscopic model from the
neutral-background model in the first local-field PR. Its target contains mobile
charged matter coupled to compact links. The photon-packet theorem of the neutral
target is **not** imported as a theorem about this interacting target.

The useful change is specific: the same virtual motion that generates electric
energy also transports the actual permanent charged records on the emergent
time scale. A uniform occupation interaction supplies the low-energy sector,
and Gauss's law has no fixed staggered background. Quantum hopping, the local
Hilbert spaces, that occupation interaction, the initial state and the formation
reservoir remain supplied premises. None is derived from the native record law.

## 1. Uniform microscopic model and a legitimate initial sector

Use a d-dimensional cubic torus, d>=2, with every period even and at least six.
Let V be its vertex count, z=2d its degree, M=dV its edge count and N0=V/2.
Orient each stored edge in its positive coordinate direction. Matter at each
vertex has the hard-core basis 0,+,-, with charge q=0,+1,-1 and occupancy n=q^2.
A record keeps its charge content when it moves. There is no record annihilation.

Each edge carries integer spin S>=1. Write C=S(S+1), E=S_z and
U_S=S_+/sqrt(C). The operator U_S has norm one and is zero beyond the spin
endpoints; it is not a cyclic shift. Impose the homogeneous constraint

\[
 G_x=\operatorname{div}E_x-q_x=0.                         \tag{1}
\]

The sum of (1) requires zero total signed charge. Hopping takes a charge q from
an occupied vertex to an adjacent empty vertex, and shifts that link electric
field by the unit required by (1). Let T_S be minus the sum of all such
unit-coefficient weighted hops and their adjoints. Every record moves unchanged.

Define the commuting occupation penalty

\[
 {\cal B}=\frac12\sum_{\langle xy\rangle}(n_x+n_y-1)^2
   =\sum_{\langle xy\rangle}n_xn_y-dN+\frac{dV}{2},
 \qquad H_S=V_0{\cal B}+tT_S.                            \tag{2}
\]

Here V_0,t>0. The displayed identity proves that the spectrum of B is integral:
dV/2 is an integer on these tori. The sum of squares proves nonnegativity.
The kernel requires n_x+n_y=1 on every edge. On a connected bipartite graph this
has exactly two occupation patterns, the two checkerboards, each with N=N0.
Both patterns have the same Hamiltonian energy; choose the A-occupied pattern
as the prepared sector P_A. Charges + and - within A are not fixed by B.

Equation (2) is a uniform repulsive occupied-neighbor interaction plus a
uniform number offset and scalar. Its homogeneous Hamiltonian does not impose
a site-dependent sublattice potential. Selecting one of its two occupation
patterns is still an initial-state choice. This is not the static attractive
record-gas law studied in PR 8626 and is not a derivation of that law's phase.

A bounded-field physical initial family exists on all the stated tori. On A
set q_x=(-1)^{x_1}; on B set q=0. From each positive A site send unit integer
electric current along x to x+e_1 to x+e_1+e_2, whose endpoint has negative
charge. These paths use disjoint oriented edges: their first links have
direction 1 and A tails, their second direction 2 and B tails, and the source
to endpoint maps are injective. Thus div E=q, total charge is zero, and every
E is 0 or 1. This verifies nonemptiness and uniform moments; it does not
establish natural preparation or a ground-state phase.

Formation can use resolved jumps on an oriented edge e=(x,y),

\[
 j_{e,\sigma}=a_{x,\sigma}^{\dagger}
              a_{y,-\sigma}^{\dagger}U_e^\sigma,
 \qquad \sigma=\pm1,                                    \tag{3}
\]

where the hard-core creation matrices act only on an empty site and
U_e^{-1} in this notation means U_e^\dagger, not an inverse. Each jump in (3)
has coefficient sqrt(beta); alternatively one coherent sum has that
coefficient. Both instruments preserve (1), add two records and annihilate
P_A. Their resolved norms are at most one and the coherent norm at most
sqrt(2). The edge loss for either instrument is
2 beta P_vac(1-E_e^2/C), because the two produced matter states are orthogonal.
There is no constant empty-edge clock at finite S. The state space and
Hamiltonian after a birth include all allowed record numbers.

## 2. Complete second and fourth orders

Within N=N0, B is simply the occupied-neighbor bond count. One outward hop
from A to B leaves z-1 occupied neighbors at its destination, so its gap is

\[
 \Delta=(z-1)V_0,\qquad \epsilon=t/\Delta,\qquad h=t^2/\Delta.
                                                               \tag{4}
\]

For stored edge e let a(e) be its A endpoint and let sigma_e=+1 when the
stored tail is A and -1 otherwise. On P_A its outward squared amplitude is

\[
 F_e=1-\frac{E_e^2-\sigma_e q_{a(e)}E_e}{C}.                \tag{5}
\]

All F_e are nonnegative, including their zero-amplitude cutoff states.
The only two-hop low endpoints are returns on the same edge. Gauss gives

\[
 \sum_e\sigma_e q_{a(e)}E_e
   =\sum_{a\in A}q_a\operatorname{div}E_a
   =\sum_{a\in A}q_a^2=N_0.
\]

Consequently the exact second-order block is

\[
 H_2=-h\sum_eF_e
    =-h(M+N_0/C)I+(h/C)\sum_eE_e^2.                      \tag{6}
\]

No fixed background is used in this cancellation. A positive electric energy
is generated by hopping even though no bare sum E^2 occurs in (2).

For an unordered pair of distinct initial edges e=(a,b), f=(c,d), oriented
here A to B, separate pairs that share an endpoint from disjoint pairs. For a
disjoint pair put r(e,f)=1_{c~b}+1_{a~d}, which is 0,1 or 2. The two outward
hops have intermediate energy 2 Delta-r V_0: each vacated cross neighbor
removes one occupied bond. Four time orderings give their diagonal unfolded
fourth-order contribution. Folded orthonormalization gives (sum F_e)^2.
In units t^4/Delta^3 the resulting canonical fourth-order block is

\[
 \begin{split}
 D_{4,S}={}&\sum_eF_e^2+
      2\sum_{\mathrm{meet}\ e<f}F_eF_f
      -\frac{2}{2z-3}\sum_{\mathrm{disjoint},r=1}F_eF_f\\
     &-\frac{2}{z-2}\sum_{\mathrm{disjoint},r=2}F_eF_f
      -\gamma_d\sum_p(R_{p,S}+R_{p,S}^{\dagger}),\\
 \gamma_d={}&\frac{2(z-1)}{z-2}
            =\frac{2d-1}{d-1}.                          \tag{7}
 \end{split}
\]

To check the diagonal coefficients, each disjoint pair has folded coefficient
2 and unfolded coefficient -4 Delta/(2 Delta-r V_0). Their difference is
zero for r=0, -2/(2z-3) for r=1 and -2/(z-2) for r=2. Meeting outward hops
are excluded by hard-core occupancy, leaving their folded coefficient 2.
The remaining nonconstant interactions in (7) are local: r>0 relates the two
edges by a cross nearest-neighbor bond.

For a cyclic plaquette a,b,c,d with a,c in A, R_{p,S} moves charge q_a along
a->b->c and charge q_c along c->d->a. It swaps the two A records and shifts
the four links by the transported charges, using the four spin shifts and
the corresponding charge projectors. In cyclic edge orientation its increments
are (-q_a,-q_a,-q_c,-q_c); stored-orientation signs must be included.
Four allowed leg orderings have denominators

\[
 \Delta,\quad 2(z-2)V_0,\quad \Delta.
\]

Thus their coefficient is -4 Delta/[2(z-2)V_0]=-\gamma_d, proving the
last term in (7). The reverse route is R_{p,S}^\dagger. Equal charges give
opposite field circulations for the two routes. For opposite charges both
routes reach the same *joint matter-field* state; their amplitudes add.
They must not be counted as two distinct final states or reduced by a half.
Neither route changes the content carried by an individual record.

There are no further four-hop low endpoints: the occupied pattern must be
restored, and a connected four-hop return on this bipartite simple graph is
an edge backtrack or a plaquette exchange. Periods >=6 exclude extra winding
four-cycles. Disconnected excursions are already included in the folded
count. Returning into the other full checkerboard would require at least
N0 hops, and N0>=18.

For unit rotor shifts, F_e tends to 1. The relevant unordered counts are

\[
 \begin{split}
 \#\mathrm{meet}&=Vz(z-1)/2,\\
 \#r_2&=M(d-1),\\
 \#r_1&=M[(z-1)^2-2(d-1)].
 \end{split}
\]

The r_2 pairs are the two opposite edge pairs per plaquette. Counting one
cross bond and the outgoing choices at its endpoints gives M(z-1)^2
cross incidences; r_2 pairs are counted twice, yielding the r_1 formula.
Hence the diagonal unit-shift limit is the scalar

\[
 c_d V=\frac{8d^2(d-1)}{4d-3}V.                          \tag{8}
\]

The rotor R_p is a unitary permutation of joint charge-electric basis states
in the Gauss sector. Its inverse is the reverse exchange. Equation (7) then
has unit-link limit c_d V I-gamma_d sum_p(R_p+R_p^\dagger).

## 3. A local limit with actual mobile charged records

Fix K,J>0. Choose integer S increasing to infinity and set

\[
 \epsilon_S^2 C=\frac{J}{\gamma_d K},\quad
 \Delta_S=\frac{\gamma_d K^2 C^2}{J},\quad
 V_{0,S}=\frac{\Delta_S}{z-1},\quad
 t_S=\epsilon_S\Delta_S,\quad
 \beta_S=\beta_0\epsilon_S^{3d},\qquad \beta_0\ge0.       \tag{9}
\]

Then h_S=KC and gamma_d t_S^4/Delta_S^3=J. The target on the chosen
occupation checkerboard and integer rotor fields is

\[
 H_{\rm mc}=K\sum_eE_e^2-J\sum_p(R_p+R_p^\dagger),
 \qquad \operatorname{div}E_x=q_x,\quad
 n_A=1,\ n_B=0.                                        \tag{10}
\]

The A charges are dynamical in (10). In particular, this target is not the
pure gauge Hamiltonian obtained by dropping the record swaps.

Take any physical density rho_S on P_A and |E_e|<=S, allowing arbitrary
charge-field entanglement, with

\[
 \sup_{S,V,e}\operatorname{Tr}\rho_S(1+E_e^2)^2\le B_*<\infty.
                                                               \tag{11}
\]

There is a gauge- and number-preserving finite-depth local circuit Y_S,
with depth and range independent of S,V, for which the preparation
rho_micro(0)=Y_S^\dagger rho_S Y_S has the following property. For every
bounded local observable O_X of link fields and retained record contents,
compress it to the microscopic spin intervals and extend its matter action
in a fixed bounded manner off P_A. For fixed T and X,

\[
 \sup_{0\le\tau\le T}
 |\operatorname{Tr}[O_X\rho_{\rm micro}(\tau)]
    -\operatorname{Tr}[O_Xe^{-i\tau H_{\rm mc}}
                         \rho_S e^{i\tau H_{\rm mc}}]|
 \le C_{X,T,K,J,\beta_0,d,B_*}\|O_X\|
       [\epsilon_S+C^{-1}(1+\log C)^d].                 \tag{12}
\]

The constant is independent of S,V and the density within (11).
For sufficiently large S the bracket is O(1/S). The target starts in the
same embedded rho_S; convergence of an arbitrary S-dependent state family
is not asserted. The circuit is a supplied preparation, not an autonomous
thermalization theorem. Births remain enabled at each finite S if beta_0>0,
but (12) has no positive limiting birth density.

Here is a proof including the changed locality and excited-sector scale.

### 3.1 Commuting penalty inverse and the finite local circuit

The previous normal-form construction used an onsite integer penalty.
B in (2) instead has overlapping commuting bond terms. This difference
cannot be ignored, but a bounded support expansion suffices.

If A_Z is supported on Z, in e^{i theta B} A_Z e^{-i theta B} all penalty
terms with support disjoint from Z commute through and cancel. The remaining
terms touch Z and lie in its one-neighbor halo. All penalty terms commute,
so terms that touch that halo but not Z do not produce a second expansion.
Conjugation preserves norm for all real theta. B has integral spectrum;
therefore the maps

\[
 {\cal D}(A)=\frac1{2\pi}\int_0^{2\pi}
       e^{i\theta B}Ae^{-i\theta B}d\theta,\qquad
 {\cal I}(A)=\frac1{2\pi}\int_0^{2\pi}
       i(\theta-\pi)e^{i\theta B}Ae^{-i\theta B}d\theta
                                                               \tag{13}
\]

are local with one extra halo, have norms <=1 and <=pi/2, respectively,
and satisfy [B,I(A)]=A-D(A). The integral for a nonzero integer spectral
difference k equals 1/k. I maps Hermitian A to an anti-Hermitian operator.
For the dimensionless penalty B/(z-1), use (z-1)I. These statements and
their constants do not depend on the electric Hilbert dimension.

Construct the circuit order by order up to n=3d+6. At order r decompose the
residual coefficient into finite-range local Hermitian terms with fixed
occupation matrix decompositions; remove each nonzero B grade using (13).
Color overlapping supports with finitely many colors and apply the order-r
anti-Hermitian generators as gates exp(epsilon^r S_{r,Z}) color by color.
Their linear effect removes that order's off-diagonal coefficient. Products
of those gates first change higher orders. Freeze the lower coefficients
before continuing, so the final finite circuit has the declared Taylor
normal form through order n.

Every application of (13) adds only a bounded halo. At fixed n the support,
number of colors and circuit depth are thus bounded independently of V,S.
Local terms are finite sums of fixed-length words in spin shifts and finite
matter matrices with scalar denominators from B grades. Grade projectors
depend on finitely many occupations; they do not require an S-dependent
decomposition by every electric eigenvalue.

Conjugating each original local term by the exact finite circuit reaches
only its finite circuit cone. Taylor's integral remainder there has norm
bounded by a constant times epsilon^{n+1}, because all generator and hop
norms are uniformly bounded. B terms have uniformly bounded local norm.
Summing by supports gives the *exact* form

\[
 Y_SH_SY_S^\dagger=V_{0,S}B+D_S+{\cal R}_S,\quad
 [D_S,B]=0,\quad
 \|D_S\|_{\rm loc}\le C t_S,\quad
 \|{\cal R}_S\|_{\rm loc}\le C\Delta_S\epsilon_S^{n+1}.
                                                               \tag{14}
\]

The local interaction norm here sums the norms of terms meeting a site,
with the fixed finite-range support weights absorbed into C. No bound on
the global operator norm uniform in volume is asserted.

All Hamiltonian terms preserve Gauss and N; (13) and the gates preserve them too.
The parity (-1)^{N_B} maps t to -t while fixing B and P_A. Choose the structural
decomposition and gates with their corresponding order parity. Odd code
coefficients vanish. No coefficient of degree <=n can map the full A pattern
to the full B pattern: it contains at most n hopping factors, whereas that
change needs N0 factors. Indeed n=3d+6<N0 on every allowed torus. Thus D_S
preserves P_A through its displayed finite order.

The transformed formation operators b_j=Y_S j Y_S^\dagger have finite
support and uniformly bounded norm. Since jP_A=0 and Y_S is perturbatively
the identity on each local support,

\[
 \|b_jP_A\|\le C\epsilon_S.                             \tag{15}
\]

This is an operator estimate on all correlated physical code states.

### 3.2 The full excited sector is faster than in the preceding model

A hop between an occupied source x and empty neighbor y has B grade

\[
 \sum_{v\sim y,\ v\ne x}n_v-
 \sum_{v\sim x,\ v\ne y}n_v.
\]

This can vanish on an excited occupation pattern. Accordingly the first
normal-form coefficient D_1 need not vanish off the code and has scale t.
The older excited-sector speed h=t^2/Delta is not a valid bound here.

Remove V_0 B by its exact interaction picture. By the commuting-halo
argument above, each remainder, normal-form interaction and jump retains
uniformly bounded range and norm under this transformation, even though
V_0 diverges. Finite-range Hamiltonian/GKSL commutator iteration therefore
gives an exponential spatial bound with speed

\[
 v\le C(t_S+\beta_S+\delta_S),\qquad
 \delta_S=\Delta_S\epsilon_S^{n+1},\qquad
 t_S=O(\epsilon_S^{-3}).                               \tag{16}
\]

An observable acquires only the same fixed halo under the removed penalty.
This reasoning uses time-uniform interaction bounds, so rapid penalty
phases do not increase the speed.

Compare the exact dressed evolution to the code Hamiltonian P_A D_S P_A.
In the Duhamel source, a bounded remainder term contributes O(delta_S).
For a code density, the full dissipator of b_j, including its anticommutator,
has trace-norm bound C epsilon_S: the jump term is O(epsilon_S^2), but
b_j^\dagger b_j P_A is only guaranteed O(epsilon_S). Multiplying by beta_S
is essential. Far from X use the bounded full superoperator norm and the
spatial propagation bound. Splitting the sums at a radius
C(vT+|log epsilon_S|+1) gives

\[
 C_{X,T}\|O_X\|
 [\delta_S(1+vT+|\log\epsilon_S|)^d
   +\beta_S\epsilon_S(1+vT+|\log\epsilon_S|)^d
   +\epsilon_S].                                      \tag{17}
\]

The last term is the local observable change under Y_S. The tails can be
made of the same or smaller order by increasing the logarithmic coefficient.
For n=3d+6, the remainder term in (17) is O(epsilon_S^3).
For beta_S=beta_0 epsilon_S^{3d}, the birth term is O(epsilon_S).
The logarithm is dominated by the nonzero t_S scale at fixed positive T;
at T=0 the source integral is zero. Thus (17) is O(epsilon_S), uniformly
in volume, without conditioning on a no-birth history.

This conservative schedule is more restrictive than the preceding
epsilon^{2d} formation law because (16) retains order-t excited motion.
A sharper estimate or a positive limiting formation rate remains open.

### 3.3 The code and rotor comparison with unbounded electric fields

The code term of order two is exactly (6). Set its electric coefficient
to K using (9) and subtract its scalar -hM-KN0. Odd orders vanish;
sixth and higher coefficients have local strength
O(Delta epsilon^6)=O(J epsilon^2).

At fourth order retain the *actual* coefficient of the chosen finite
circuit, denoted D_{4,S}^{circ}. A canonical effective block can differ
from it by a within-code change of basis because (6) is not scalar at
finite S. The coefficient remains a fixed sum of matter matrices and
spin-shift words with S-independent coefficients. In the unit-shift limit
the second-order dimensionless coefficient is -M I: the 1/C electric
correction vanishes before the physical scaling is applied to that
coefficient. The first-order code block is zero. Hence the first
non-scalar fourth-order block is invariant under an analytic near-identity
within-code change, and (7)-(8) imply

\[
 D_{4,\infty}^{circ}
    =c_d V I-\gamma_d\sum_p(R_p+R_p^\dagger).            \tag{18}
\]

No equality of all finite-S canonical and circuit fourth orders is assumed.

Extend the finite-S shift to zero outside its interval in ell^2(Z). Extend
the second-order code term by the exact K sum E^2. The resulting code
Hamiltonian agrees with its microscopic finite-S restriction and, after
the two scalar subtractions, is

\[
 K\sum E^2+(J/\gamma_d)(D_{4,S}^{circ}-c_d V I)
       +{\cal E}_{\ge6,S},\qquad
 \|{\cal E}_{\ge6,S}\|_{\rm loc}\le C J\epsilon_S^2.       \tag{19}
\]

All interactions other than the onsite electric term are bounded,
finite-range and uniformly controlled in S. They can include charge
projectors and permutations, which have norm at most one and commute with
electric weight operators.

The elementary shift bound, including endpoints and exterior states, is

\[
 \|(U_S-U)(1+E^2)^{-1}\|\le 2/C.                        \tag{20}
\]

For an interior m use the explicit square root and
|m(m+1)|<=2(1+m^2); outside the interval the reciprocal weight is O(1/C).
Adjoints obey a similar fixed constant. Fixed-length shifted products
are handled by telescoping, since a bounded shift changes 1+E^2 by a
bounded multiplicative factor. Equation (20), Cauchy-Schwarz and (11)
give an O(1/C) trace-norm source for every local word difference in
D_{4,S}^{circ}-D_{4,infty}^{circ}. This is a state-weighted estimate:
uniform operator-norm shift convergence is false.

For w_e=(1+E_e^2)^2, each R_p either leaves E_e fixed or shifts it by one
conditional on a charge projector. The adjacent-value ratios are at most
9 in either direction. Charge permutations are unitary and do not alter
w_e. The same weighted commutator estimate as for a pure plaquette shift
therefore gives the sufficient inequality

\[
 |\partial_\tau\operatorname{Tr}\rho_{\rm mc}(\tau)w_e|
 \le 24J(d-1)\operatorname{Tr}\rho_{\rm mc}(\tau)w_e.      \tag{21}
\]

It follows first for capped weights min(w_e,L), whose adjacent ratios obey
the same estimate, and then by monotone convergence. The initial moment
bound propagates as B_* exp[24J(d-1)T].

In finite volume K sum E^2 is self-adjoint and its magnetic perturbation is
bounded. Removing the onsite electric term leaves strongly continuous
bounded finite-range interactions. Vector Dyson series converge by factorial
bounds; the usual commutator iteration then gives spatial propagation with
speed C J, without requiring operator-norm continuity of the onsite
conjugation or finite local dimension. The same holds for (19).

Use the target density in Duhamel, (20)-(21) near the observation cone, and
the bounded interaction norm with the spatial estimate outside it. Splitting
at distance C(JT+log C+1) yields local code-to-target error

\[
 C_{X,T}\|O_X\|
       [\epsilon_S^2+C^{-1}(1+\log C)^d].               \tag{22}
\]

The first term comes from the higher-order bounded remainder. Combining
(17) and (22) proves (12), conditional on the supplied model and prepared
state, with the changed commuting-penalty circuit explicitly established
above. The analytical proof still needs an independent reconstruction;
the finite controls below are not a substitute for it.

## 4. Exact controls, failures and their scope

homogeneous_charged_records_check.py independently constructs the full
physical charge-zero two-record basis on a square at S=1,2,3. To retain
the bulk coordination cost, its square penalty has z-2 fixed external
occupied A neighbors at each B site. This *guarded square* is a denominator
and coefficient control; it is not an isolated periodic square instance of
the many-volume theorem. The extra term is (z-2)N_B. An isolated C4 would
have a second checkerboard after just two hops and would be an invalid
gapped control for (7).

At (S,z)=(1,4),(2,4),(1,6),(2,6),(3,6), the complete physical dimensions
are 24,48,24,48,72 and code dimensions 4,8,4,8,12. Every matrix element of
the exact normalized second and fourth effective blocks agrees with
(5)-(7). For S=1,z=6, Delta=5 and the middle square gap is 8; gamma=5/2.
The normalized second block is -4I, and the fourth block has diagonal
11 and swapped-state off-diagonal -5. At z=4 the corresponding diagonal
is 10 and off-diagonal -6. The two directions coincide for opposite charges.

The same runner constructs literal 6^2 and 6^3 cubic geometry, the bounded
initial fields above, all unordered edge pairs and the occupied-neighbor
energies after two disjoint hops. The meet/r1/r2 counts are respectively
216/504/72 and 3240/13608/1296. The unit-shift constants are 1152/5 and
3456. It enumerates every ordering of four exchange legs, finding exactly
four valid paths in each direction, with the stated three denominators.
Both equal- and opposite-charge controls are included where available.
The displayed initial fields happen to give F_e=1 on every edge; genuine
nonunit weights are checked by the complete higher-spin square matrices.

homogeneous_occupancy_penalty_check.py checks all 65,536 occupations of a
4x4 torus. It verifies the integral nonnegative penalty, exactly two zero
patterns and the one-halo hop-grade formula. Of 16,384 allowed hops on a
selected directed edge, 5,120 have grade zero. Ground-pattern hops have
grade three. This is a direct check of the order-t excited motion that
forces the changed speed in (16); period four is an auxiliary occupation
algebra control, not an added case of the period>=6 theorem.

The first charged-record runner passed its guarded-square calculations
and then failed while constructing the cubic edge index: a missing
coordinate-axis loop left a variable unbound. The exact failed source,
stdout, traceback and receipt are preserved under
homogeneous_charged_source_history/initial_edge_index_failure. Adding that
axis loop was the only repair. The full second execution passed; no
scientific expectation or asserted coefficient was changed. The occupation
runner passed on its first execution. Full outputs and execution receipts
are retained. No large-volume dynamics simulation is represented here.

## 5. What remains open

This construction connects permanent record motion to a local interacting
charge-field Hamiltonian on one common finite-time scale, with no fixed
Gauss background and no explicitly staggered Hamiltonian coefficient.
It supplies the repulsive occupation interaction and selects a prepared
checkerboard sector; it does not derive that sector from the repository's
static record probability law.

The phase and excitations of (10) are open. Charge motion may favor an
ordered or screened phase; the neutral pure-gauge photon-packet result
does not settle that question. There is no established Coulomb phase,
physical mass spectrum, observed coupling, chiral fermion sector, gravity,
Lorentz-invariant interacting continuum limit or TOE conclusion here.
No independent theorem currently identifies newly formed microscopic
records with a finite-density continuum matter field.

The live-formation schedule in (9), diverging microscopic energies, growing
link memory, native compilation of spin shifts and preparation gates, and
autonomous selection of the physical state are material costs and open
obligations. The result should be assessed as a conditional construction
whose new local-limit proof and interacting target both warrant further
checks.
