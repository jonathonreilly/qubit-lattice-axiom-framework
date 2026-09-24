---
claim_id: finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated ordered limits; historical numerical tables are author observations, with fresh controls separately identified below."
upstream_dependencies:
  - minimal_axioms
  - finite_rate_repeated_record_formation_bounded_theorem_note_2026-09-24
  - local_finite_rate_formation_and_rotor_limit_bounded_theorem_note_2026-09-24
  - electric_and_magnetic_dynamics_from_record_motion_bounded_theorem_note_2026-09-24
runner: scripts/finite_formation_with_retained_fourth_order_dynamics_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical construction; unaudited.

The complete source argument below is preserved from the frozen submission. Its dated author-status statements and historical execution tables describe that submission, not an independent audit verdict. Quantum laws, enlarged site/link memories, Hamiltonians, instruments, backgrounds and preparations are supplied mathematical model assumptions. They are not new repository axioms or framework primitives. Fresh execution of the canonical runner checks the stated finite controls; finite tests alone do not establish the general proofs or limits.

# Finite-rate formation with retained fourth-order field dynamics

Author conditional theorem, 2026-09-23. Independent reconstruction pending.
The model is the supplied staggered-background hard-core record/link model
of FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md. This is not the different
homogeneous neutral charged-record model of PR 8661.

The first result is a controlled fixed-volume approximation by a generator
that retains fast matter motion, finite fourth-order interactions and finite
formation together. Its target still depends on epsilon. The second result
identifies the field dynamics and first formation law from the initially
vacant-B sector in a joint large-spin limit. Neither result establishes
photon propagation after arbitrary repeated formations.

## 1. Assumptions and the fast target

Fix a finite bipartite graph and the same physical sector
div E+1_A-q=0. Sites have 0,+,-, hard-core hopping T, and coherent-per-edge
or resolved pair-birth channels j. Links are normalized integer spin S>=1,
or unit rotors. Write

W=sum_A(1-n_a),  P=1_(W=0),  Pi_r=1_(W=r),
A=Pi_1 T P,  Z=Pi_2 T Pi_1 A,  M=A†A.

If Pi_2 is absent, set Z=0. The exact selection rules are

Pi_r T Pi_s=0 unless |r-s|=1,
jP=0,  [W,j]=-j,  [N,T]=0,  [N,j]=2j.               (1)

T and all j are bounded at fixed graph, uniformly over these link resources.
In particular ||T||<=number of edges and sum_j||j||²<=2 number of edges.
The W spectrum is a finite subset of the nonnegative integers even for
unit rotors. Assume the chosen physical P space is nonzero.

Fix delta,kappa>0 and supply

H_epsilon=delta epsilon^-4 W+delta epsilon^-3 T,
L_(j,epsilon)=sqrt(kappa) epsilon^-1 j.               (2)

The number-energy offset relating W and N_B has exactly the qualification
in the parent theorem: the H=Delta N_B+tT interpretation requires an
initial number-block-diagonal density. The theorem for (2) itself does not.

Define P-space bounded operators

H_2=-M,
H_4=M²-(1/2)Z†Z,
B_j=-P j Pi_1 T P.                                  (3)

The proposed target generator is

L_(P,epsilon) X
 =-i[delta epsilon^-2 H_2+delta H_4,X]
       +kappa sum_j D[B_j]X.                        (4)

Every B_j raises N by two and returns to P. All terms preserve the supplied
Gauss constraint. The target allows actual repeated formations on P; it
does not project back to the original number sector after a birth.

For every fixed finite T_0 there are epsilon_0,C(T_0)>0 such that, for
0<epsilon<epsilon_0 and every P-supported density rho,

sup_(0<=tau<=T_0)
 ||exp(tau L_epsilon)rho
       -P exp(tau L_(P,epsilon))rho P||_1
 <=C(T_0) epsilon.                                 (5)

Constants depend on graph, delta,kappa,T_0, but can be chosen independently
of integer S. Equation (5) also holds directly for unit rotors. No electric
moment condition is needed in this fixed-volume bounded-generator theorem.
There is no claim that the target (4) has an ordinary epsilon-independent
density limit: the H_2 term is genuinely fast on general later sectors.

## 2. Exact bounded block rotation, with its hypotheses

Here is a direct construction; no dissipative excited-population inverse
or assumed fast mixing gap is used. Put h(epsilon)=W+epsilon T and
P_r=1_(W=r). For small |epsilon|, circles of radius less than 1/2 around
the distinct integers separate its spectral clusters. Let Q_r(epsilon)
be their Riesz projections. Contour resolvent Neumann series, using
bounded T and the unit separation of the W spectrum, show that these
projections are analytic and Q_r(epsilon)=P_r+O(epsilon), with constants
independent of Hilbert-space dimension or S at fixed graph.

Let

S(epsilon)=sum_r Q_r(epsilon) P_r,
U(epsilon)=S(epsilon)[S(epsilon)†S(epsilon)]^-1/2.

For real sufficiently small epsilon this is a unitary, is I+O(epsilon),
and maps each P_r to Q_r(epsilon). Indeed S†S is block diagonal with
block P_r Q_r P_r, positive and close to identity. The inverse square
root is given by its norm-convergent power series. Orthogonal cluster
ranges show UU†=U†U=I. Therefore U†hU commutes with W exactly.

This construction diagonalizes all W clusters, not merely P versus its
complement. That distinction is needed below: otherwise an O(epsilon^-3)
hopping term could remain in the complementary block.

The parity operator Xi=(-1)^W obeys Xi T Xi=-T. The contour construction
gives U(-epsilon)=Xi U(epsilon) Xi. Since U†hU commutes with W, Xi acts as
a scalar on each block, so U†hU is an even analytic function of epsilon.
Consequently the exact transformed Hamiltonian has the global bound

H_tilde=delta epsilon^-4 W+O(epsilon^-2),             (6)

and on P it equals delta epsilon^-2 H_2+delta H_4+O(epsilon²).

To check the coefficients, write the low spectral space as the graph of
a map X:P->Q, Q=I-P, and let R=(W|_Q)^-1. Its invariance equation is

epsilon A+(W_Q+epsilon QTQ)X=epsilon X A†X.

With X=epsilon X_1+epsilon²X_2+epsilon³X_3+...,

X_1=-A,  X_2=(1/2)Z,
A†X_3=M²-(1/2)Z†Z.

These identities use A in W=1 and Z in W=2; W=3 terms in X_3 are
annihilated by A†. The graph's effective matrix epsilon A†X consequently
has coefficients -M and M²-Z†Z/2. Converting from graph coordinates to
the canonical isometry multiplies by (I+X†X)^(1/2) on the left and its
inverse on the right. The only possible fourth-order change is
[ M/2,-M ]=0. This proves (3) for the above positive-overlap block unitary.

The first derivative satisfies U'(0)P=-A. Hence, for the exact transformed
jump j_tilde=U†jU,

j_tilde P=epsilon B_j+O(epsilon²),  B_j=P B_j P.      (7)

All analytic and norm bounds here are uniform in S because only finitely
many integer W clusters, bounded T,j and fixed contour separations enter.
For unit rotors the same bounded functional calculus and operator-norm
series apply to the infinite-dimensional physical sector.

The use of a unitary block rotation is established perturbation machinery;
see the primary source [Bravyi, DiVincenzo and Loss,
arXiv:1105.0675](https://arxiv.org/abs/1105.0675). The source abstract was
consulted for context. No dynamical error theorem from that work is
imported: the construction and residual proof needed here are given explicitly.

## 3. The large off-block dissipator cannot simply be discarded

Let G_epsilon be the exact generator after conjugation by U. Let E_0 embed
P matrices in the full space, and define its discrepancy from (4),

R_epsilon=G_epsilon E_0-E_0 L_(P,epsilon).

For a full matrix X write
Off X=QXP+PXQ and Diag X=PXP+QXQ. Equations (6)--(7) imply, as induced
trace-norm bounds on these linear maps,

||Off R_epsilon||=O(epsilon^-1),
||Diag R_epsilon||=O(epsilon).                       (8)

In detail, the Hamiltonian is exactly W-block diagonal; its P-block
truncation error is O(epsilon²). Jump recycling inside PP has leading
kappa B_j X B_j† and O(epsilon) remainder. Its QQ part is O(epsilon²),
since Q j_tilde P=O(epsilon²). The PP loss is
kappa B_j†B_j+O(epsilon). However the QP loss contains
epsilon^-2 Q j_tilde†j_tilde P=O(epsilon^-1).
This is the leading off-block source in (8). Dropping it without a
correction would not prove a small generator residual.

Put A_0 X=-i delta[W,X]. On Off matrices this has a bounded inverse:
in QP it maps Y to (i/delta)R Y, and in PQ it maps Y to
(-i/delta)Y R. Define the Hermiticity-preserving correction map

C_epsilon=-epsilon^4 A_0^-1 Off R_epsilon,
E_epsilon=E_0+C_epsilon.                            (9)

It has norm O(epsilon³). There is no claim that E_epsilon is positive.
Its exact residual is

G_epsilon E_epsilon-E_epsilon L_(P,epsilon)
 =Diag R_epsilon
   +(G_epsilon-epsilon^-4 A_0)C_epsilon
   -C_epsilon L_(P,epsilon).                        (10)

Both ||G_epsilon-epsilon^-4 A_0|| and ||L_(P,epsilon)|| are O(epsilon^-2).
The jump contribution to the first norm is also O(epsilon^-2);
the exact block rotation removed the potentially worse Hamiltonian term.
Thus (8)--(10) give an O(epsilon) induced trace-norm residual.

Duhamel between the two CPTP evolutions contracts trace norm on Hermitian
inputs. The initial and final embedding defects are O(epsilon³), so it
bounds their difference in the transformed picture by
2||C_epsilon||+T_0 O(epsilon). Finally U=I+O(epsilon) changes the original
undressed initial density and the final density by O(epsilon), uniformly
over all density matrices. This proves (5).

All generators for a fixed epsilon are bounded also on the rotor trace
class; the norm-convergent no-jump/jump expansion supplies their CPTP
semigroups. There is no unbounded E² term in this part of the proof.
The large-spin electric term below arises only after a further restricted
joint limit.

A finite classical count or event-label register can be added exactly as
in the parent theorem. Hamiltonians act trivially on it and jump channels
perform the register transitions, with no reachable overflow. The same
bounded selection rules and proof apply. Thus (5) includes fixed finite
lists of count observations and first-event marked CDFs. It does not alone
give total variation of arbitrary continuously marked quantum histories.

## 4. What happens before the first formation on a cubic graph

Now specialize to a periodic cubic graph with every coordinate period even
and at least six, and initially all A sites plus, all B sites vacant. These
are the checked field-coefficient source's hypotheses; shorter wrapping
cycles are not silently included. Write P_v for that entire field sector. Total charge
is |A|, and the supplied Gauss equation gives div E=0 there. This sector
is invariant under both number-preserving target Hamiltonian terms until
a formation occurs.

Let C=S(S+1), let m be the number of edges, and choose

epsilon² C=delta/K,  J=2delta,  K>0.                 (11)

The exact second-order calculation in
ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION_BOUNDED_THEOREM_NOTE_2026-09-24.md gives on P_v

H_2=-m I+(1/C)sum_e E_e².                            (12)

It follows directly by summing the single-hop-and-return link weights:
the linear electric terms sum to zero by Gauss. After subtracting the
irrelevant scalar -delta m epsilon^-2, the second-order Hamiltonian in
(4) is exactly K sum E². The earlier fourth-order calculation gives,
strongly on finite electric-support vectors,

H_4 -> c_G I-2sum_p(U_p+U_p†),                       (13)

where c_G=d|V|(4d-1) on the stated cubic graph. The finite-spin H_4
operators are bounded uniformly in S at fixed graph. Thus the field
Hamiltonian before the first event tends to

H_field=K sum E²-J sum_p(U_p+U_p†),                  (14)

up to a scalar. These are the already checked field coefficients, used
here with a different, finite-effective-formation schedule. The quoted
source's microscopic theorem with decreasing beta is not being applied
outside its assumptions; (5) is the new fixed-volume approximation
that supplies this schedule.

For unit rotors, B_j=-PjTP restricted to P_v moves an existing plus record
from a to one neighboring empty B site, then creates a pair on a different
incident edge. Distinct old-record destinations are orthogonal for each
fixed birth channel. Coherent charge outputs are orthogonal at the
filled A center. Every legal unit-rotor shift has norm one. Therefore

sum_j B_j†B_j |_(P_v)=r/kappa I,
r=2kappa sum_(a in A) z_a(z_a-1).                    (15)

This identity is for the initially vacant-B sector. It is not a claim that
later formation rates depend only on occupations. On a regular cubic graph
z_a=2d, and r is proportional to volume, as expected for the first event
anywhere in a finite system.

For a rotor density sigma in P_v, the limiting density on the branch with
no formation by tau is consequently

sigma_no(tau)=exp(-r tau)
     exp(-i tau H_field) sigma exp(i tau H_field).   (16)

The first event has an exponential waiting time with rate r, while the
conditional field evolves under the generated electric-plus-magnetic
Hamiltonian. Its marked first-event CDF is

Pr(first event by T, mark j)
 =integral_0^T kappa exp(-r tau)
   tr[B_j exp(-i tau H_field) sigma
                exp(i tau H_field) B_j†] d tau.    (17)

Marks refer to the specified instruments; coherent and resolved marks
are different operational records even though their total r agrees.

## 5. Why the joint first-event limit is controlled

In (11), epsilon(S)->0. The error in (5), including the finite-register
version, is uniform in S and hence tends to zero. It remains to compare
the target's no-event field branch with (16).

Embed finite-spin fields in the integer-rotor space as in the locality
addendum. All finite products of normalized shifts and their adjoints
converge strongly, uniformly bounded. Thus H_(4,S) and the restricted
birth operators B_(j,S), including their adjoints, converge strongly.
The second-order field Hamiltonian after its scalar subtraction is
exactly the compression of the common K sum E².

One can extend each finite-spin problem to the full rotor space with that
same unbounded diagonal electric Hamiltonian and bounded H_(4,S) and
birth-loss perturbations. The finite electric box remains reducing for
the finite-spin dynamics. In the interaction picture of K sum E²,
bounded-perturbation Dyson series and strong convergence give convergence
of the no-event semigroups on trace class, uniformly on each fixed finite
time interval. The same argument follows first on finite-rank finite-
electric-support inputs and then on any trace-class density by contraction.
There is no need to assume a uniform electric moment for this qualitative
fixed-volume strong limit.

The restricted losses tend strongly to the scalar in (15). Products
B_(j,S) rho_S B_(j,S)† converge in trace norm when rho_S converges and the
operators converge strongly with adjoints. Boundedness and finite time
therefore give convergence of the integrals in (17). Together with the
finite-register version of (5), this proves the first-event time/mark
probability statement for the microscopic dynamics.

This argument proves the pre-event quantum field density and integrated
first-event probabilities. It does not prove that the quantum output after
that event follows the unchanged field Hamiltonian. The full post-event
approximation available here is the epsilon-dependent generator (4).
The new matter sectors can have a nontrivial fast H_2 term.

## 6. Scientific status and checks

The fourth-order Hamiltonian and the formation terms coexist in (4).
The reason the earlier balanced formation theorem lost its field scale
was its different choice of Delta,t; that loss is not forced by the
algebra of refilling alone. Here both delta H_4 and the kappa birth
generator remain finite, while fast matter motion is explicitly retained.

fast_matter_formation_check.py compares canonical spectral block rotations
with (3), and propagates both the full microscopic generator and (4) on
the four-leaf star, the two-A path, and genuine cyclic Gauss sectors at
spin one and two. The cyclic controls test nonconstant electric fields,
nonzero fourth-order loop terms and the first-formation loss operator.
Numerical coefficient/error scaling is corroboration; equations (6)--(10)
supply the convergence proof. Complete results and failure history are
bound by the author seal.

The four models supply 72 complete density comparisons; the largest observed
trace error divided by epsilon is 3.611. The canonical fourth-order coefficient
controls separately test the Hamiltonian formula through exact spectral
cluster rotations. Their initial default eigensolver produced a 3.22e-13
polar-unitarity error against the declared 2e-13 target on the spin-one
cycle. That attempt is preserved. Switching to the divide-and-conquer
Hermitian solver passed the unchanged threshold and all coefficient checks.

A second runner, first_formation_field_check.py, assembles the complete
microscopic two-record sector on the cycle directly from its six matter
words and electric circulation. It compares the no-event density with the
rotor prediction at S=2,4,8,16,32 and five times through 0.5, with
K=1,J=2.6,kappa=0.7 and first-event rate 5.6. At S=32 and time 0.5,
the microscopic no-event probability is 0.0625611458 versus the limiting
0.0608100626; the unnormalized density trace error is 0.00900084.
The finite rotor cutoff is checked against twice that cutoff, with a state
norm difference below 1.78e-14. These are floating controls, not interval
certificates or a three-dimensional evolution.

The first version rejected an eigenvector condition number 16.5 against
its declared cutoff 10. The complete attempt is preserved. Unitary complex
Schur propagation removes that eigenbasis-inversion issue. A further
preserved diagnostic replaced a subtractive rank-two distance formula,
which produced a spurious roughly 6e-8 time-zero error, with its stable
orthogonal-component identity. The target's omitted electric tail remains
included. No physical parameter, target or convergence claim was changed.

The prepared field-wave results can be used on the conditional pre-event
branch at fixed box under their own assumptions. This is not a persistent
photon phase with repeatedly created charged matter. The first-event rate
is extensive, so a global no-event statement is especially restrictive
at large volume. No volume-uniform microscopic bound is claimed here.

The site/link Hilbert spaces, quantum dynamics, background, initial state,
instruments and resource scaling remain supplied. The original energy
cost per added pair grows with Delta; there is no autonomous fuel
construction. Dynamics after repeated births, a controlled macroscopic
matter/field regime, native selection of these laws and empirical matching
remain open.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the model, graph, sector, preparation, observables and order of limits explicitly specified above.
- **N2 — Alternatives:** other instruments, Hamiltonians, states and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probabilistic structures are model assumptions; the native axioms do not select them.
- **N4 — Dependencies:** named companion arguments are used within their stated scope; no audit grade is inherited.
- **N5 — Evidence:** exact finite algebra and numerical stability controls corroborate the displayed proofs. Floating spectra and propagations are not interval enclosures. Historical tables are not independently certified by their presence here.
- **N6 — Resolution:** fixed-volume, uniform-volume and ordered-limit statements keep their distinct hypotheses; no exchange of limits is inferred.
- **N7 — Remaining work:** native selection, physical implementation, energy supply, preparation and empirical identification remain separate obligations except for explicitly proved model-specific results.
- **N8 — Authority:** this source applies no audit verdict, retained grade or assembly decision.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary only; it does not derive the supplied model.
- [finite_rate_repeated_record_formation_bounded_theorem_note_2026-09-24](FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.
- [local_finite_rate_formation_and_rotor_limit_bounded_theorem_note_2026-09-24](LOCAL_FINITE_RATE_FORMATION_AND_ROTOR_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.
- [electric_and_magnetic_dynamics_from_record_motion_bounded_theorem_note_2026-09-24](ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.

Finite-dimensional linear algebra, operator calculus and the explicit inequalities above are mathematical tools. Referenced literature is attribution or context unless its actual assumptions and use are stated in the argument.

## Source and verification

Source PR #8672, frozen head `fe6dc2c5ef061fa1e0051063d49178f23b872c13`. The primary review session uses no subagents; no separate fix reviewer or formal audit is claimed. Original auxiliary packets, failed attempts and historical seals remain recoverable on the original PR branch. The combined receipt records each original path disposition.

```bash
python3 scripts/finite_formation_with_retained_fourth_order_dynamics_2026_09_24.py
```

The canonical wrapper executes the selected scientific controls in a fresh temporary directory, retains their generated result JSON in its stdout, and ends with TOTAL. It does not execute historical sealing or approval instructions.
