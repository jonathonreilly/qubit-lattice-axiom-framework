---
claim_id: local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/local_compensation_common_field_record_limit_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# A local compensation that gives a common field/record limit

Root conditional construction candidate, September 23, 2026. This changes
the supplied Hamiltonian by the explicit term below. It is not a conclusion
about the unchanged model, a derivation from native axioms, or an assertion
that nature selects this term. The generalized target theorem and this local
construction are provisional pending final independent comparisons. Exact
author controls are complete and bound by LOCAL_CONSTRUCTION_AUTHOR_SEAL.json;
they do not replace the proof or the independent check of this construction.

## 1. Local definition and the additional hypothesis

Take any fixed finite simple bipartite graph G=(A union B,E) with the parent
hard-core records q=0,+1,-1, normalized integer-spin shifts, and physical
Gauss law div E=q-1_A. Let n_a be occupancy and W=sum_(a in A)(1-n_a).
Write F_(a,S) for the *unsigned* sum of legal charge-preserving hops from a
to its empty B neighbors. Then

    T_S=-sum_a(F_(a,S)+F_(a,S)^*).

Each F_a empties A site a. Its adjoint refills that same site. Define the
diagonal local operators, in the physical charge/electric basis,

    D_(a,S)(q,E)=sum_(b~a, q_a!=0, q_b=0)
                         [1-E_e(E_e+k_(a,b,q))/C],
    D_(a,infinity)(q,E)=n_a sum_(b~a)(1-n_b),
    C=S(S+1),

where k=-q_a when a is the lower endpoint of the oriented edge e, and k=+q_a
when it is the upper endpoint. D_(a,S) is exactly the diagonal part of
F_a^*F_a. A forbidden outward spin-boundary hop has zero weight in the
displayed formula, so no boundary path is silently retained.

Let the local occupancy gate be

    Q_a=product_(c in A, c!=a, graph distance(c,a)<=2) n_c,

with the empty product equal to I. Supply the new interaction

    C_S=sum_(a in A) [F_a^*F_a-D_(a,S)+D_(a,infinity)] Q_a. (1)

The microscopic law is changed to

    H_epsilon,S=delta epsilon^(-4)
                          [W+epsilon T_S+epsilon^2 C_S],
    L_(j,epsilon,S)=sqrt(kappa) epsilon^(-1) j_S.          (2)

Thus the extra physical coefficient is delta epsilon^(-2). Equation (1),
including that coefficient, is an additional dynamical assumption. The
construction uses existing local site/link operators, but their particular
combination is not already supplied by the original model.

The bracket in (1) preserves every A occupancy and hence commutes with Q_a
and W. It is self-adjoint and nonnegative: the bracket is F_a^*F_a
plus a nonnegative diagonal operator, since integer E(E+k)>=0 for k=+/-1,
and Q_a is a commuting orthogonal projection. Hops and their reverses preserve
charge, record
number and the Gauss constraint, while the diagonal factors do also. Its
support lies in the radius-two neighborhood of a. It is genuinely local on
bounded-degree graphs; a product over all A sites is not used on a large
graph. The cube happens to have all its A sites within distance two of each
other. With degree z_a,

    ||F_a||<=z_a,  ||D_(a,S)||,||D_(a,infinity)||<=z_a,
    ||C_S||<=sum_a(z_a^2+2z_a),                          (3)

uniformly in S at fixed graph. The bounded compensation target theorem
therefore applies, provided its independent check confirms the derivation.

## 2. Exact removal of the fast off-diagonal motion

On P=1_(W=0), all Q_a equal I. The ranges F_a P for different a have different
vacant A sites and are orthogonal. Consequently, with A_S=Pi_1 T_S P and
M_S=A_S^*A_S,

    M_S=sum_a P F_a^*F_a P,
    P C_S P=M_S+Delta_S,
    Delta_S=sum_a(D_(a,infinity)-D_(a,S))|_P.             (4)

The residual is diagonal, with the exact value

    Delta_S(q,E)=C^(-1) D(q,E),
    D(q,E)=sum_(a in A,b~a,q_b=0) E_e(E_e+k_(a,b,q)).    (5)

Each summand is nonnegative on integer fields because k=+1 or -1. Thus D is
a nonnegative diagonal multiplication operator on the full physical rotor
P space. It is self-adjoint on its multiplication domain, and finite-support
physical vectors are a core. Some charge words may leave electric directions
unconfined; essential self-adjointness of a diagonal multiplication operator
does not require a strictly positive confining quadratic form.

Choose K,delta,kappa>0 fixed and

    eta=delta/epsilon^2=K S(S+1).

The second-order Hamiltonian is then *exactly*

    delta epsilon^(-2)(P C_S P-M_S)=K D                 (6)

on the complete physical spin space. Neither a post-formation flat projection
nor a removal of part of the actual output is used. The compensation matches
the spin-weighted off-diagonal matrix, not merely its rotor value; this is
why (6) is diagonal and nonnegative without an additional matrix-valued
unbounded-operator assumption.

## 3. The remaining Hamiltonian and full density limit

Use the generalized canonical coefficient

    H4_S^C=M_S^2-{M_S,P C_S P}/2
               +A_S^*(Pi_1 C_S Pi_1)A_S-Z_S^*Z_S/2.     (7)

All its factors are uniformly bounded in S on this fixed graph. Normalized
spin shifts, their adjoints and the physical-box projections converge strongly
to rotor shifts and the identity. Every fixed finite product converges strongly.
Therefore H4_S^C converges strongly to the bounded self-adjoint H4_infinity^C,
and all effective formation B_(j,S) and their adjoints converge strongly to
the rotor B_j. At rotor order P C_infinity P=M_infinity, so

    H4_infinity^C=A_infinity^* C_(1,infinity) A_infinity
                                      -Z_infinity^*Z_infinity/2. (8)

On the common physical rotor space define

    h=K D+delta H4_infinity^C,
    L rho=-i[h,rho]+kappa sum_j D[B_j]rho.              (9)

The Hamiltonian is self-adjoint on D(D), by bounded perturbation of the
explicit diagonal operator. Its unitary group, plus the bounded jump/loss
operators, defines a trace-preserving completely positive semigroup on trace
class. No high-field moment is required for an initial density to be evolved
by that semigroup, though differentiability or unbounded-energy expectations
would need their own domain hypotheses.

For the spin target, extend H4_S^C and B_(j,S) by zero outside their physical
spin boxes, and use the same K D on the whole rotor space. The boxes reduce
the resulting dynamics, so their restrictions give exactly the target.
In the interaction picture of K D, the remaining Hamiltonian and dissipative
maps are uniformly bounded on trace class and converge strongly there.
For example B_S rho B_S^* converges in trace norm on finite-rank rho by
strong operator convergence, then on all trace class by uniform boundedness.
The Hamiltonian commutator and anticommutator terms follow the same way.

The bounded Dyson series in this common interaction picture converges
absolutely on compact time intervals, uniformly in S. Termwise convergence
first for a fixed trace-class input, then dominated convergence of the series,
gives the full strong trace-class limit, uniformly on every [0,T]. Equivalently
one can use the Duhamel identity with finite-net approximation of the compact
limiting orbit. Trace-norm convergent physical initial approximants are
handled by contractivity. Thus the candidate claim is

    sup_(0<=t<=T)||rho_(target,S)(t)-exp(t L)rho_0||_1 ->0. (10)

The generalized uniform-S O(epsilon) microscopic target theorem then transfers
(10) to the original bare microscopic densities of the *modified law (2)*.
It applies to deterministic P initialization and the complete density after
all allowed formations. Finite event/count registers can be added under the
same bounded selection rules. This is a full trace-one common field/record
description in the stated finite-graph regime, conditional on (1).

## 4. Cube field dynamics and an actual second formation

On the cube A={0,3,5,6}, every other A site is at distance two from a. If
W>=1, either a itself is vacant, so its bracket in (1) is zero, or Q_a has
a zero factor. Hence C_S vanishes on all W>=1 sectors of this cube. In
particular C_(1,S)=0 exactly. The limiting Hamiltonian is especially simple:

    h_cube=K D-(delta/2)Z_infinity^*Z_infinity.          (11)

The first four-record sector has q=1_A and divergence-free fields. Summing
the linear electric terms in (5) gives zero, so D_4=sum_e E_e^2. Exact cube
path enumeration gives

    Z_(4,infinity)^*Z_(4,infinity)/2
             =84I+2 sum_(six faces p)(W_p+W_p^*).

Thus before formation, (11) is

    K sum E^2-2delta sum_faces(W_p+W_p^*)-84delta I.     (12)

The original pre-first cube field Hamiltonian has the scalar +60delta
instead; their difference is the irrelevant scalar -144delta. The generated
electric and magnetic dynamics on that first sector are therefore retained.
After formation, (11) and the rotor jumps provide the common evolving
matter/field density rather than assuming the first-sector field Hamiltonian
continues unchanged.

The jumps B_j are unchanged at leading order. On the initial all-A-plus
sector their total rotor loss is 48 kappa I. Following any specified first
cube mark, the checked immediate next-rate operator is

    kappa[8I+W_square+W_square^*]

on the normalized first output, for both specified first instruments. Its
expectation is between 6 kappa and 10 kappa for every normalizable initial
field. For the initial zero-field state the expectation is 8 kappa. Direct
composition of all first and second marks therefore predicts the small-time
limit in the modified model

    Pr(N=8 at t)=192 kappa^2 t^2+o(t^2).                (13)

The coefficient is half the total two-jump intensity
48 kappa times 8 kappa. It does not require differentiating an unbounded
Hamiltonian on the zero-field state: the bounded jump source integrands are
continuous in trace norm at time zero, and their ordered double integral
has the displayed coefficient. The exact direct path sum in
local_compensation_check.py gives total two-jump norm squared 384 for all
four combinations of resolved/coherent first and second instruments. The
separate exact Laurent-path mechanism_check.py checks the displayed normalized
next-rate polynomial for all 24 resolved and all 12 coherent first marks.
More generally the leading coefficient lies between 144 and 240 times
kappa^2 for a fixed normalizable initial field. This supplies an actual
positive second-formation witness; it is not just a nonzero formal jump
operator on an inaccessible state. The eight-record target then freezes
because every site is occupied.

## 5. Why the naive compensation is insufficient

The occupancy gate in (1) matters. At rotor order, omitting it gives
C_infinity=sum_a F_a^*F_a. On P, two outward hops from distinct A sites
commute: if they use the same empty B destination both orders vanish by
hard-core exclusion; otherwise their local operators commute. Different
pairs of vacated A sites have orthogonal ranges. Counting the two possible
orders yields

    A^* C_1 A=Z^*Z/2.

Then (8) vanishes. That simple cancellation removes the fourth-order magnetic
effect as well as the unwanted second-order motion. The gated construction
is intended to avoid this cancellation on interacting radius-two stars.
For the cube C_1=0 proves the distinction exactly. On a general graph,
equation (8) is the explicit definition; an unchanged plaquette formula on
larger graphs has not been proved in this packet.

The result is a constructive conditional completion of a specific supplied
model. Its coupling choice, physical origin, stability under coefficient
errors, finite-resource interpretation, growing-volume limit, native-law
selection and comparison with observations remain separate questions. The
proof neither adopts a new axiom nor claims a TOE. The point-spectrum and
local-escape results for the original Hamiltonian remain valid for that
different law.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** the specified graph, sector, input, observable and order of limits.
- **N2 — Alternatives:** other models, initial states, instruments and resource scalings remain possible.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not new repository axioms.
- **N4 — Dependencies:** companion results retain their hypotheses; no retained grade is imported.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate the argument; floating computations are not interval enclosures.
- **N6 — Resolution:** density convergence, energy convergence, initial power, finite time and volume limits are distinct statements.
- **N7 — Remaining work:** native selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** no audit verdict or retained-grade promotion is applied.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied model.
- [bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.
- [local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8841, frozen head `fed8422aaaaff35c4da1ae613d6e889a989613b4`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/local_compensation_common_field_record_limit_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
