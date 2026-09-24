# Finite-rate repeated record formation with gauge-preserving motion

Author conditional theorem, 2026-09-22. Personally derived and checked on finite
models by the root; independent reconstruction pending. Quantum dynamics,
formation instruments, energy penalties, a bipartition/background and the
scaling are supplied. This is a finite-graph open-system result. It neither
derives a preferred law from the native axioms nor preserves the earlier
fourth-order photon limit.

## 1. The finite model

Let a finite bipartite graph have site classes A,B. A site has hard-core states
0,+,- with q=diag(0,1,-1) and n=q². Each oriented edge has a fixed finite
integer spin S>=1, E=S_z, U=S_+/sqrt(S(S+1)). For c=+1 set U^[c]=U and for
c=-1 set U^[c]=U†; these symbols are partial shifts, not unitary inverse powers.

Restrict to the supplied Gauss sector
G_x=div E_x+1_A(x)-q_x=0.
On an oriented edge x->y, hopping a charge c from x to vacant y multiplies its
amplitude by U^[-c]. With a_x,c=|0><c|, write the self-adjoint signed hopping

T=-sum_(x->y),c [a_y,c† U^[-c] a_x,c + adjoint].

A birth channel on a wholly vacant edge is
j_e,c=a_x,c† a_y,-c† U^[c].
Use either the two resolved channels j_e,+ and j_e,-, or the single coherent
channel j_e,+ + j_e,-, separately for each edge. The two choices are different
instruments. Other fixed relative phases can be handled by the same algebra,
but the numerical comparisons here use the plus combination.

These operators commute with every G_x. A hop preserves N=sum n_x and
transports the existing charge unchanged; a jump raises N by two. There is
no annihilation or overwrite of an occupied site. Unspecified additional
permanent internal record labels are not silently supplied by this charge
model.

Let M_A=|A| and W=sum_A(1-n_x), the number of vacant A sites. Then

[W,j_e,c]=-j_e,c,   [N,j_e,c]=2j_e,c,
T changes W by exactly one whenever it acts.

Put P=1_(W=0), and Pi_j=1_(W=j). In particular PTP=0 and jP=0. Pair creation
always refills an A vacancy. Boundary spin weights can block some channels;
the proof below does not require all possible birth rates to be positive.

Fix delta,kappa>0 and 0<epsilon<=1. Supply

H_epsilon'=delta W/epsilon² +delta T/epsilon,
L_epsilon,j=sqrt(kappa) j/epsilon.                    (1)

Equivalently Delta=delta epsilon^-2, t=delta epsilon^-1 and
beta=kappa epsilon^-2. The original penalty Hamiltonian Delta N_B+tT differs
from (1) by Delta(N-M_A). Starting with [rho,N]=0, both give identical
number-block-diagonal densities and the same marked jump laws. The formal
theorem for (1) itself allows any initial P density; the identification with
the original Hamiltonian requires this additional number condition.

All spaces and operators in this note are finite. Constants may depend on
the graph, S, delta and kappa. P must be nonzero and the stated initial
density must be supported there. There is no volume-uniform estimate here.

## 2. Effective generator

Define Gamma=kappa sum_j j†j, which commutes with W. On Pi_j, for j>=1, set

D_j=j delta I -i Gamma_j/2.

Its Hermitian real part is the strictly positive scalar j delta, so D_j is
invertible and ||D_j^-1||<=1/(j delta), even if some states cannot decay.
Let

A_1=Pi_1 T P,  T_21=Pi_2 T Pi_1,  B=A_1† D_1^-1 A_1.

A space with no Pi_2 simply omits the associated terms. The proposed
P-space Lindblad operators and Hamiltonian are

H_eff=-(delta²/2)(B+B†),
l_j=sqrt(kappa) delta P j Pi_1 D_1^-1 A_1.             (2)

Thus L_eff X=-i[H_eff,X]+sum_j D[l_j]X, where
D[l]X=l X l†-{l†l,X}/2. Both the effective motion and the birth channels
are finite and can remain nonzero as epsilon tends to zero. Each l_j raises
N by two and acts within P: the A vacancy is only a virtual intermediate.

These familiar non-Hermitian-resolvent formulas alone are not a convergence
proof. The next section includes the recycling terms and the two-hole
coherences required on graphs with more than one A site.

## 3. Complete finite-time error proof

Write the full generator as
L_epsilon=epsilon^-2 L_0+epsilon^-1 L_1,
L_0 X=-i delta[W,X]+kappa sum_j D[j]X,
L_1 X=-i delta[T,X].

For a P-supported matrix X define linear maps into the full operator space.
E_0 X is X in the PP block. Put

Y=-delta D_1^-1 A_1,
Y_2=delta² D_2^-1 T_21 D_1^-1 A_1.

The nonzero blocks of E_1 X are
(E_1 X)_(1,0)=Y X,  (E_1 X)_(0,1)=X Y†.
The nonzero blocks of E_2 X are

(E_2 X)_(1,1)=Y X Y†,
(E_2 X)_(2,0)=Y_2 X,  (E_2 X)_(0,2)=X Y_2†.         (3)

No positivity claim is made for this polynomial embedding; all E_i preserve
Hermiticity and have explicitly bounded trace norms.

We check each cancellation, as identities on all P matrices.

* L_0 E_0=0 because W P=0 and jP=0.
* In the (1,0) block, L_0 acts by -iD_1 and L_1 E_0 contributes
  -i delta A_1 X. Their sum vanishes with Y as above. The (0,1) block is
  the adjoint linear identity. Thus L_0 E_1+L_1 E_0=0.
* Put Z=delta² D_1^-1 A_1 X A_1† D_1^-†. In the (1,1) block,
  L_0 Z=-iD_1 Z+i ZD_1†, apart from recycling into P. This is
  i delta²[D_1^-1 A_1 X A_1†-A_1 X A_1†D_1^-†].
  L_1 E_1 gives its negative. In the (2,0) block L_1 E_1 gives
  i delta² T_21 D_1^-1 A_1 X, which is canceled by -iD_2 Y_2 X.
  The (0,2) block is the corresponding adjoint identity.
* The remaining PP block is
  i delta²(BX-XB†)+kappa sum_j P j Z j† P.
  The second term is precisely sum_j l_j X l_j†. Since
  D_1^-1-D_1^-†=i D_1^-† Gamma_1 D_1^-1,
  the first term is -i[H_eff,X]-{sum_j l_j†l_j,X}/2.

These are all possible blocks: T changes W by one; recycling a (1,1) block
lands in PP; recycling a (2,0) or (0,2) block vanishes because jP=0.
Therefore

L_0 E_2+L_1 E_1=E_0 L_eff.                            (4)

Omitting the (2,0)/(0,2) terms would invalidate (4) on a general graph.
The exact four-site path control below explicitly detects their necessity.

Set E_epsilon=E_0+epsilon E_1+epsilon² E_2. The exact residual is

R_epsilon=L_epsilon E_epsilon-E_epsilon L_eff
 =epsilon(L_1 E_2-E_1 L_eff)-epsilon² E_2 L_eff.        (5)

For explicit finite constants one may use
a_1=2||Y||,
a_2=||Y||²+2||Y_2||,
ell=2||H_eff||+2sum_j ||l_j||².
These bound the indicated induced trace norms on Hermitian matrices, and
||L_1||_(1->1)<=2delta||T||. For every density rho=P rho P,
both actual evolutions are CPTP and contract trace norm on Hermitian inputs.
Duhamel applied to (5), with the initial and final embedding defects included,
gives for 0<=tau<=T_0

||exp(tau L_epsilon)rho-E_0 exp(tau L_eff)rho||_1
 <=2(epsilon a_1+epsilon² a_2)
   +T_0[epsilon(2delta||T|| a_2+a_1 ell)
        +epsilon² a_2 ell].                          (6)

In particular this is O(epsilon) on each fixed finite time interval.
No fast excited-state mixing gap, informal factorization or asymptotic
interchange is needed. The initial state is undressed: its initial layer is
included in the O(epsilon) embedding defect. The bound is not asserted to
be sharp.

If A_1=0, the effective process is trivial and the same proof applies.
If some Pi_1 state has zero birth loss, the positive detuning still makes
D_1 invertible. If a Pi_2 sector is absent, take Y_2=0. These cases are part
of the theorem rather than tacit exclusions.

## 4. Marked records, multiple births, and finite capacity

Add a finite classical event-word or count register to both dynamics, and
multiply each jump by the corresponding register transition. A hop acts as
the identity on this register. On the subspace reachable from the chosen
initial number sector, there can be at most floor((|V|-N_initial)/2) births:
each adds two hard-core records and no operation removes records.

The augmented matrices obey the same W selection rules, and their loss
operators and resolvents are unchanged away from an unreachable register
overflow. Applying (3)--(6) to this enlarged finite space proves convergence
of the joint register/output density, not merely its average count. For a
fixed finite list of event-time thresholds, tag jumps by their time interval
and apply the same argument piecewise. This gives O(epsilon) convergence of
the corresponding marked event CDFs and final quantum output densities.
A total-variation bound on arbitrary full continuous-time path laws is not
being inferred from this finite-register statement.

The finite capacity does not guarantee that every possible birth occurs:
coherent dark states or blocked channels can stop further formation.
Neither a renewal process with independent identical waiting times nor
indefinite production is assumed.

## 5. Complete small models and a second-refill witness

On a star with a single center A and m leaves, total charge is one and
E_(A->leaf)=-q_leaf. For even m, all allowed links in the spin-one physical
sector have unit hopping/formation amplitudes. On a center-vacant state
with N records,

sum_j j†j=2(m-N),  D_1=delta-i kappa(m-N).

For initial center plus and all leaves vacant, the exact initial effective
birth intensity from (2) is

r_m=2m(m-1)kappa delta²/[delta²+kappa²(m-1)²].          (7)

Each edge contributes 2(m-1) orthogonal birth outputs to the squared norm.
For m=2 the only nonabsorbing P state is the initial center state, so the
first event is exponential with rate
r_2=4kappa delta²/(delta²+kappa²).
Its coherent/resolved final states are those in
FINITE_RATE_RENEWED_FORMATION_EXACT_STAR.md. The rate differs from that
note's 4kappa because here beta/Delta=kappa/delta stays finite instead of
tending to zero.

For m=4 the complete physical Hilbert space has dimension 45, with
dim P=29 and dim Pi_1=16. A birth gives three records, leaving vacancies.
Hopping can then empty the same center again, and a second birth gives five
records. At delta=1.3, kappa=0.7 and tau=2 the effective two-event probabilities
from the full 29-state generator are

coherent per edge: 0.7250882880133398,
resolved charge:   0.6623880703002745.

At epsilon=0.025 the actual full 45-state dynamics gives respectively
0.725023700053077 and 0.6623528314098958. Full density trace-norm errors
are 0.0023947628421325563 and 0.0012154613900759981. These numerical values
are model witnesses, not universal rates or experimentally determined numbers.

The same first-event rate r_4=4.654426229508198 holds for both instruments,
but their later event probabilities differ. Therefore matching the
no-event loss or first-event clock does not identify the repeated-formation
law. The choice of formation instrument is a substantive supplied input.

The additional path A0--B1--A2--B3 has a complete nine-state physical spin-one
sector (one of the ten charge-two site words is excluded by the electric
cutoff), with dimensions P=4, Pi_1=4, Pi_2=1. Exact rational checks on all
16 P matrix units verify (4) for each instrument. Removing Y_2 fails this
identity. This tests the additional algebra used to pass from stars to
general finite graphs.

## 5a. Exact later-event law and finite microscopic dark states

The four-leaf star permits a stronger exact check than a positive second-event
probability. In the N=3 sector, write A_3=Pi_1 T P, restricting both sides to
N=3, and M=A_3†A_3 on its 18-dimensional occupied-center subspace.
Its exactly computed spectrum, including multiplicities, is
0(6), 1(3), 2(3), 3(2), 5(3), 6(1).

Starting from the initial center plus, the state immediately after the first
event, with the event mark discarded, is the normalized sum
sigma_3=(1/24)sum_j v_j v_j†, v_j=P_(N=3) j Pi_(N=1,W=1) T g.
The no-event N=1 state has only one bright excited direction. Therefore this
sigma_3 is independent of the first-event time and of Delta,t,beta, at finite
positive microscopic parameters as well as in the limit.

Let w_lambda=tr(P_lambda sigma_3) for M's exact spectral projector P_lambda.
Exact rational projectors give

| instrument | w_0 | w_1 | w_2 | w_3 | w_5 | w_6 |
|---|---:|---:|---:|---:|---:|---:|
| coherent per edge | 4/15 | 0 | 1/3 | 0 | 1/15 | 1/3 |
| resolved charge | 1/3 | 0 | 1/6 | 0 | 1/3 | 1/6 |

Every vector in ker A_3 is an exact dark state of the full microscopic model:
T vanishes on it, W=0, and all births vanish because the center is occupied.
For every positive eigenvalue lambda, singular-value decomposition of A_3
reduces the no-event microscopic evolution to a damped two-level block with
nonzero coupling t sqrt(lambda), detuning Delta and excited decay beta.
There is no undamped vector in such a block: zero loss would force its
excited component to vanish, and then its nonzero coupling forces the other
component to vanish. Finite-dimensional evolution on those blocks therefore
decays to zero. The initial N=1 bright block also decays for all t,beta>0.

It follows that the eventual probabilities of a second formation are exactly

11/15 for coherent-per-edge formation, and 2/3 for resolved-charge formation,

for every Delta,t,beta>0 in this finite model, not only in the scaling limit.
This does not assert a blockade for other Hamiltonians, instruments or networks.

For the effective model, put
r_0=24kappa delta²/(delta²+9kappa²),
b=2kappa delta²/(delta²+kappa²).
The first event is exponential with rate r_0. Conditional on the first event,
the survival law for the second waiting time is
w_0+sum_(lambda>0) w_lambda exp(-b lambda u).
Hence

P_0(tau)=exp(-r_0 tau),
P_1(tau)=w_0(1-P_0(tau))
 +sum_(lambda>0) w_lambda r_0
   [exp(-r_0 tau)-exp(-b lambda tau)]/(b lambda-r_0),
P_2(tau)=1-P_0(tau)-P_1(tau).                         (8)

At coincident rates the fraction is interpreted continuously as
r_0 tau exp(-r_0 tau). This is a mixture with a dark component, not an
assumed independent identical renewal clock.

repeated_formation_dark_check.py constructs exact rational projectors from
the complete sector and verifies their idempotence, eigenvalues and sum to
the identity. It checks the microscopic dark identities and compares (8)
with all 72 stored effective four-leaf count rows. The maximum numerical
difference is 4.44e-16. This check uses the author's already bound
microscopic-sector builder; it is a separate calculation form, not an
independent author's reconstruction. No failed execution occurred.

## 6. Resource and field limits

In the original Hamiltonian H=Delta N_B+tT,
H/Delta=N_B+epsilon T. On P, N_B=N-M_A. Equation (6) implies

tr(H rho_epsilon(tau))/Delta
 =tr[(N-M_A)rho_eff(tau)]+O(epsilon)

for each fixed finite graph and finite time interval. Starting with all A
occupied and all B vacant, the leading term is twice the expected number
of formation events. Delta=delta epsilon^-2 diverges. A number-energy offset
used in the proof does not supply autonomous fuel or establish a finite
physical energy per event.

This scaling keeps second-order motion t²/Delta=delta finite. The earlier
fourth-order ring scale t^4/Delta³=delta epsilon² instead tends to zero.
Consequently this theorem is not a joint finite-rate-formation/photon
limit. It identifies a well-defined alternative matter/formation regime;
connecting it to the separately checked field-wave regime is an open task.

The supplied A/B penalty and Gauss background also remain present. This
result must not be presented as an extension of the homogeneous, neutral,
repulsion-selected charged-record model without a separate compatibility
argument. Large-volume uniform locality estimates, an autonomous reservoir,
native state/instrument selection, arbitrary record-content transport and
empirical matching are open.

## 7. Evidence and source context

repeated_formation_check.py builds complete constrained tree sectors directly
from site words and exact tree incidence, rather than building the effective
generator first. It checks Gauss shifts, hard-core conditions, charge/number
conservation, W selection rules, loss equality and the sector-energy identity.
The two smaller models have exact SymPy rational tests of all three
embedding identities for every P matrix unit and both instruments.

Full sparse Liouville evolutions are compared with (2) on both stars, for
both instruments, epsilon=0.2,0.1,0.05,0.025 and nine times through two.
All checks passed the first execution. REPEATED_FORMATION_RESULTS.json
contains every basis word, identity result and density/count/energy value;
the execution receipt binds the source and logs. The numerical propagation
does not independently prove (6); the algebra and Duhamel argument do.

The non-Hermitian effective-operator mechanism is standard, for example
[Reiter and Sorensen, arXiv:1112.2806v2](https://arxiv.org/html/1112.2806v2).
The primary source's Sections II and III.1--III.5 were read. No error theorem
is imported from its adiabatic derivation. Equations (3)--(6) give the
finite-dimensional error argument used here, including the two-hole term
and formation recycling. No claim of a new fundamental physics mechanism
is made.
