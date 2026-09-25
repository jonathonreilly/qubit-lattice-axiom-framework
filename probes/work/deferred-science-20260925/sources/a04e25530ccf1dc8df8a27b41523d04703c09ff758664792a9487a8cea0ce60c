# From the common rotor readout to microscopic finite-bin records

Root personal conditional derivation, 2026-09-24. This extends the supplied
finite-register target theorem to a particular positive-width trajectory
event and an ordered diagonal approximation. It supplies no quantitative
spin cost, microscopic arrival-time derivative, physical detector or empirical
confirmation. The original compensated Hamiltonian and original formation
instrument are retained, including any specified coherent sign channel.

## 1. Precisely which parent statement is used

At fixed finite graph and fixed positive K,delta,kappa, the pinned
BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET note proves a uniform-in-spin
O(epsilon) approximation of the full microscopic density from P initialization
to its P target. It explicitly allows finite classical event/count registers
when compensation acts trivially on the register and preserves record number.
The LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT note proves strong trace-class
convergence of that spin target to the full rotor target, uniformly on fixed
time intervals, with epsilon^2 S(S+1)=delta/K. The spin target retains the
same KD and bounded strongly converging magnetic/jump terms. Both are
provisional supplied-model dependencies. Their bounds are not uniform as
K,delta, the graph or the observation horizon vary.

The following argument spells out the required registers and time partitions.
It does not infer a trajectory law from unconditioned density convergence
alone. No arbitrary continuously conditioned microscopic-history theorem is
assumed from those parents.

Initially N0=|A| and each formation increases record number N by two.
Hamiltonian and no-event evolution preserve N. Thus both microscopic and
common processes have at most M=floor(|B|/2) events on this finite graph.
The graph and M stay fixed. The alphabet J consists of the original recorded
marks: resolved edge/sign marks or coherent edge marks, as actually chosen.
The two signs of a coherent mark are not separately recorded or dephased.

## 2. Finite deterministic time bins preserve the original instrument

Choose a finite partition 0=t0<t1<...<tm=T*. Use a classical register basis
consisting of all words w of length at most M in pairs (bin index, original
mark). On interval r, replace each channel j_S in the bookkeeping dilation
by j_S tensor V_(r,j), where V_(r,j)|w>=|w,(r,j)> when |w|<M and is zero
at length M. Distinct prefixes have distinct images for a fixed channel,
so each V is a norm-one partial isometry. The register begins empty.
Hamiltonian, compensation, W and T act trivially on it.

The actually reachable subspace satisfies N=N0+2|w|. At |w|=M the physical
formation channel already vanishes because fewer than two empty sites remain.
On this subspace the original loss is unchanged. The register density stays
classical, and tracing it out gives exactly the original unmonitored system
density and its original mark instrument. The word merely stores observed
marks and time bins; it is not an added physical reservoir, reset or law.
No part of the system's postbirth matter coherence is measured by this label.

On each interval the lifted data satisfy the parent's assumptions:

 [W tensor I,j_S tensor V]=-j_S tensor V,
 (j_S tensor V)(P tensor I)=0,
 [C_S tensor I,W tensor I]=0,
 ||j_S tensor V||<=||j_S||.

The canonical cluster rotation remains U_S tensor I. The effective channel
is exactly B_(j,S) tensor V_(r,j), and the effective Hamiltonian is h_S
tensor I. The number of generator channels at a time is the original |J|;
the register is finite for every fixed partition. Thus the parent's density
argument applies separately on every interval. At a switch, target P states
remain in P. Contractivity and a finite triangle inequality propagate the
error through all m intervals, including physical-spin initial approximants.
No estimate uniform as m tends to infinity is asserted.

The common-rotor proof also lifts to this finite register: KD is unchanged,
all remaining factors are uniformly bounded and strongly convergent, and the
same interaction-picture Dyson/finite-rank argument applies. Finite products
of these semigroups therefore converge on each fixed input. Hence at fixed
partition, all recorded word probabilities converge:

  P_micro,S(word belongs to A_partition)
                  -> P_rotor(word belongs to A_partition),       (1)

for every subset of the finite word alphabet. The subset can include any
later marks; reading the first two entries does not forbid later events.
Equation (1) is a bounded register effect evaluated on the converging full
joint density. It does not require bounded microscopic jump intensity.

## 3. Pass from rectangular bins to a positive relative-time window

Let I=[t,t+h], h>0, and b>0 be fixed, with T*>t+h+b. Define A to mean:
the first mark is j at s in I, the next mark is l at s+u with 0<u<=b.
There is no intervening event; all events after the second are unrestricted.
If fewer than two events occur, A is false.

In the common rotor model the full jumps are bounded. Put

 R = kappa ||sum_j B_j* B_j|| <= kappa sum_j ||B_j||^2 < infinity.

Every conditional no-event state has instantaneous total hazard at most R.
Equivalently its next-waiting-time density is bounded by R, directly from
contractivity of the full no-event semigroup and the bounded loss. This also
bounds the first-event time density. No unbounded Hamiltonian derivative or
smoothness of the initial field state is needed.

For a partition of mesh at most eta, let A_eta^- contain the word bins every
realization of which satisfies A, and A_eta^+ contain those with at least one
realization satisfying A. Use the stored word order even when the first two
events have the same bin. Then, for both microscopic and target trajectories,

 A_eta^- subset A subset A_eta^+.

A target trajectory in A_eta^+ minus A_eta^- has first time within eta of
one of the two endpoints of I, or second-minus-first time within 2 eta of b.
Possible exact endpoint coincidences have target probability zero. Once eta
is sufficiently small compared with the positive margins, the density bounds
and conditioning on the first event give the sufficient estimate

 P_rotor(A_eta^+ minus A_eta^-) <= 8 R eta.             (2)

The first endpoints contribute at most 4R eta; the waiting-time interval at
b contributes at most 4R eta. The first-event distribution integrates to at
most one. Mark restrictions only reduce these upper bounds. One can use a
larger harmless constant at partition endpoints without changing the proof.

Apply (1) at each fixed partition before sending eta to zero. The sandwich
and (2) prove

               P_micro,S(A) -> P_rotor(A)             (3)

at fixed graph,K,delta,kappa,I,b. There is no need for a uniform microscopic
hazard bound, which would be false at the supplied epsilon^-2 jump scaling.
The same sandwich argument applies to these events for arbitrary normalizable
initial rotor fields with trace-norm convergent physical-spin approximants.
It does not imply convergence of time-density derivatives, total variation
of all continuous record laws, or uniform convergence for shrinking b.

## 4. An ordered microscopic realization of the packet contrast

Now conditionally import the sealed two-mark packet and finite-bin arguments.
Use one fixed cubic graph, fixed c,a,kappa,I, and the supplied family
K_g=cg^2/(2a), delta_g=c/(4ag^2). For each fixed g, prepare the normalized
projection of the compact vacuum or one-particle rotor packet into the physical
spin box, in the bare P matter sector. Projection converges in norm as S grows;
the parent theorem does not require replacing this by a dressed initial state.

For each fixed g and b>0, (3) applies with

 epsilon(g,S)^2 S(S+1)=delta_g/K_g=1/(2g^4).

Let g_n tend to zero and b_n>0 obey the sufficient small-bin condition in the
finite-bin packet theorem. That theorem's probabilities satisfy

 [P_rotor,1(g_n;I,b_n)-P_rotor,0(g_n;I,b_n)]
                    /(kappa^2 b_n g_n^2) -> -2 H_I,    (4)

where H_I is its survival-weighted packet-intensity integral. At each n first
hold g_n,b_n fixed, then choose a sufficiently large integer S_n so that for
both preparations the error in (3) is at most

 eta_n kappa^2 b_n g_n^2,          eta_n -> 0.

This is possible by (3); choose S_n still larger if necessary to make
S_n increase and epsilon(g_n,S_n)->0. Therefore the same normalized contrast
limit (4) holds for the actual microscopic recorded event probabilities.
For H_I>0 it is the same negative coincidence contrast, not a positive click.
All physical matter sectors and the unchanged original instrument remain.

This is an existence/ordered-diagonal statement. It provides neither a rate
for S_n nor a finite apparatus or resolution cost. The spin-to-rotor strong
convergence and parent constants are not uniform in g, shrinking bins or
volume. A prescribed simultaneous schedule cannot be substituted. In
particular the vanishing bare microscopic jump at time zero has never been
equated to the target instantaneous rate. A quantitative, feasible model of
source preparation, clocks and detection, and independently selected physical
parameters are still needed before this becomes a prediction for observations.

## 5. A separate finite model tests why the order matters

A five-state supplied penalty model has states P0,Q0,P1,Q1,P2, record numbers
0,0,2,2,4 and penalties 0,1,0,1,0. Take T=-(|Q0><P0|+|Q1><P1|+adjoint),
C=|P0><P0|+|P1><P1|, and j=|P1><Q0|+|P2><Q1|. It satisfies the abstract
parent selection rules, but is explicitly not the physical cube or cubic
rotor model. H2^C=H4^C=0 and its effective original mark is
B=|P1><P0|+|P2><P1|. Thus the target has two successive exponential waits
with rate kappa and then stops.

In either active microscopic block the no-event matrix is

 A_e = -i delta epsilon^-4 [[epsilon^2,-epsilon],[-epsilon,1]]
                         -kappa/(2epsilon^2) diag(0,1).

After each actual event the next block begins in bare P. If lambda_s,lambda_f
are the two eigenvalues, the Q amplitude is

 c_e [exp(lambda_s u)-exp(lambda_f u)],
 c_e=i delta epsilon^-3/(lambda_s-lambda_f).

The waiting density is kappa epsilon^-2 times its squared modulus. Integrating
its three exponential terms gives the exact CDF F_e(u). In particular the
finite-bin event probability is

 [F_e(t+h)-F_e(t)] F_e(b)
         -> [exp(-kappa t)-exp(-kappa(t+h))][1-exp(-kappa b)]

for fixed b>0. However, when b=epsilon^6, the microscopic short-time expansion
gives F_e(b)/(kappa b)~delta^2 epsilon^4/3 ->0, whereas the target ratio tends
to one. The expansion is controlled since b||A_e||=O(epsilon^2). This is a
concrete order-of-limits counterexample in the stated separate model; it is
not a claim that this is the cube's sharp resolution boundary or a universal
obstruction to its controlled diagonal sequence.

The accompanying small control checks these exact selection rules, fixed-bin
and shrinking-bin CDFs, and finite time-grid sandwiches for the two-wait target.
It does not simulate the cubic photon, prove the conditional parent theorem,
or supply a quantitative spin schedule for (4).
