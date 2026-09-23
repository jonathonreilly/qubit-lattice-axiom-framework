# A local interaction retaining fields through actual record formation

This publication unit constructs an explicitly changed local Hamiltonian in
the supplied hard-core record and spin-link model. On every fixed finite
simple bipartite graph, its joint limit has ordinary electric and magnetic
dynamics together with the stipulated formation jumps, including recycling
into subsequent record-number sectors. The initial input need not be replaced
by a prepared flat-band state. The construction is conditional and has been
selectively independently reconstructed. It has no formal retained or native
axiom status, and its physical selection remains open.

The original Hamiltonian's post-formation large-spin behavior is a separate
result in the parent PR. Changing its interaction is explicit here. This is
not evidence that the original Hamiltonian already has the new limit.

## What changes

Let W count vacant A sites, let T=-sum_a(F_a+F_a*) be the hopping operator,
and let P mean every A site is occupied. F_a moves a record outward from a
to an empty neighboring B site using the normalized spin shift. The original
dimensionless microscopic Hamiltonian W+epsilon T is changed to

    W+epsilon T+epsilon² C_S,
    C_S=sum_a [F_a*F_a-D_(a,S)+D_(a,infinity)] Q_a.       (1)

D_(a,S) is the diagonal of F_a*F_a, D_(a,infinity) counts its allowed
outward paths, and Q_a requires the other A sites at distance two from a
to be occupied. The added interaction is positive, bounded at fixed graph,
Gauss/record-number/W preserving, and supported within radius two. Its
coefficients are chosen to cancel the unwanted fast return term while
retaining the finite electric correction. That choice is a hypothesis.

On P, with c_S=S(S+1), the exact finite-spin identity is

    C_(0,S)=M_S+D/c_S,    M_S=A_S* A_S,
    D=sum_(legal outward hops) E_e(E_e+k_e) >= 0.         (2)

Consequently eta(C0-M)=K D when eta=K c_S. This exact equality, rather than
strong convergence multiplied by a divergent scale, supplies the common
electric operator. All remaining Hamiltonian/jump coefficients are bounded
and converge strongly. The common interaction-picture proof then yields
trace-norm convergence of the full deterministic density and finite mark/count
registers, uniformly on compact times for each fixed initial trace-class
density with convergent physical embeddings. It is not uniform over all
spin-dependent high-field input states. The independently checked fixed-graph
microscopic target estimate supplies the additional O(epsilon) transfer.

## Why the surviving interaction stays local

In the rotor limit, the fourth-order Hamiltonian reduces to

    H4^C=-2 sum_(a<c sharing a B neighbor) S_ac* S_ac,
    S_ac=F_c F_a P.                                    (3)

Distant, disjoint stars cancel between the one-vacancy compensation and
two-vacancy virtual paths. Neighboring star pairs remain. Each term is bounded
with fixed support; their total norm has an extensive bound on bounded-degree
graphs. This establishes the stated finite-graph locality and does not yet
prove a thermodynamic limit or a volume-uniform microscopic approximation.

Before any birth, all A sites carry positive records. The resulting field
Hamiltonian on every fixed simple bipartite graph is

    K sum_e E_e² - 2delta sum_(simple four-cycles p)(W_p+W_p*)

plus an explicitly computed scalar. The electric and nonconstant magnetic
terms therefore agree with the original initial field dynamics. After birth,
the coupled vacancy-dependent D and local pair operators must be used;
the initial field formula cannot simply be carried unchanged into every
record sector. Square-free graphs have no magnetic four-cycle term here.

On the cube the compensation vanishes on all W>=1 sectors, so C1=0.
The initial fourth-order scalar is -84, with six plaquette coefficients -2.
The original scalar is 60. That scalar difference has no effect within a
fixed-number density block; it is not an autonomous source-energy accounting.

## Actual repeated formation

The formation jumps remain the ones in the supplied model. Exact physical
path algebra on the cube gives, for each normalized actual first mark,
an immediate next loss kappa[8I+W+W*], bounded between 6kappa and 10kappa.
This is an instantaneous statement, not a full exponential waiting law.

Summing every two-mark channel gives

    sum_(j,k) (B_k B_j)* (B_k B_j)
        =384 I+8 sum_(six faces p)(W_p+W_p*).             (4)

Thus the normalizable zero-electric-field input has limiting-target
Pr(N=8 at t)=192 kappa² t²+o(t²). The same coefficient holds for the four
resolved/coherent choices at the two events. For other initial fields its
coefficient lies between 144kappa² and 240kappa². Independent reconstruction
also supplies a specified accessible ordered two-mark isometry for every
initial field. Neither result identifies all later quantum histories across
the instruments. The joint limit precedes the small-time expansion; the
undressed microscopic law jP=0 forbids silently reversing that order.

The cube fills after two births. Its fully occupied target has no hopping,
formation or electric term and stops evolving. There is no indefinite source
of new records in a finite saturated graph and no supplied fuel model.

## Mechanism controls and assumptions that remain open

Removing the occupancy gate from sum F_a*F_a gives a different microscopic
sum of squares with an exactly flat dressed low Hamiltonian. It loses the
desired magnetic dynamics. The source proves that restricted identity to
all orders, not a no-go for every ungated interaction. Adding the finite-spin
diagonal repair changes that exact identity and retains the electric term.

A fixed fractional error in the chosen cancellation leaves a fast non-scalar
term on the physical cube. It fails the explicitly stated criterion of an
ordinary strongly continuous density limit, uniform down to time zero on all
fixed inputs in that block. Selected subspaces, initial layers, changed
topologies and rotating frames are outside that criterion. A detuning
1+nu/eta+o(eta^-1) instead has a well-defined finite extra nu M term. These
facts quantify part of the proposal; they do not establish uniqueness or
naturalness of the tuned coefficients.

Root and independent controls check the canonical compensation expansion,
complete physical small-spin matrices, exact charge/field path identities,
full-target recycling on a separate path graph, and graph families with
different overlap patterns. A new independent irregular disconnected graph
checks the general first-sector cycle count beyond the author's fixtures.
These finite controls support the proofs; their number is not evidence of
independence by itself. Source reuse and post-source additions are explicit.

The principal open question is physical selection of (1), including its
occupancy gate and coefficients. Also open are an autonomous source/resource
model, uniform local dynamics with increasing volume, a spatial field phase,
native-axiom derivation, and empirical identification. Those are not concluded
by this fixed-graph construction.

## Reading and recovery

Read the general expansion in
[the frozen general note](../local_compensation_author/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md)
together with its required
[wording correction](../local_compensation_author/ROOT_GENERAL_TARGET_CORRECTION.md).
Only the two Hamiltonian coefficients are asserted selfadjoint; the original
phrase about every displayed operator was too broad. The independently
acknowledged correction changes no equation or theorem.

Then read the [local construction](../local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md),
the [ungated/tuning analysis](../local_compensation_author/UNGATED_SUM_OF_SQUARES_AND_TUNING.md),
and the [general-graph locality argument](../local_compensation_locality_author/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS.md).
The two independent REPORT/PRE/COMPARISON/FINAL packets are in
`compensation_target_independent` and `local_compensation_independent`.
The root review binds their exact identities and records its read/execution
limits. Immutable pre-comparison bytes and the correction's recovery path
remain included. No raw campaign branch or unrelated evidence is published.
