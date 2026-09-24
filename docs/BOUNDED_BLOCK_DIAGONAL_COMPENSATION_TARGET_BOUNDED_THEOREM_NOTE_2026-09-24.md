---
claim_id: bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/bounded_block_diagonal_compensation_target_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# Effective target with a bounded penalty-preserving compensation

Root conditional theorem candidate, September 23, 2026. This generalizes the
checked parent target theorem to an explicitly changed microscopic law.
The added interaction is a supplied hypothesis, not a derivation from the
record axioms. Selective independent reconstruction is pending.

## Statement and canonical convention

Use the parent's fixed finite graph, physical Hilbert space, integer-spectrum
penalty W, P=1_(W=0), Pi_r=1_(W=r), bounded self-adjoint T with only
|r-s|=1 blocks, and bounded formation channels j obeying jP=0 and [W,j]=-j.
The bounds are uniform in the link resource S. Let C_S be another bounded
self-adjoint physical operator such that

    [C_S,W]=0,   sup_S ||C_S||<infinity.

It also preserves N and Gauss in the record applications below. Its coefficient
and form are new premises. Supply the microscopic Hamiltonian

    H_epsilon,S=delta epsilon^(-4)(W+epsilon T_S+epsilon^2 C_S),
    L_(j,epsilon,S)=sqrt(kappa) epsilon^(-1) j_S.        (1)

Let A=Pi_1 T P, M=A^*A, Z=Pi_2 T Pi_1 A, C_0=P C P and
C_1=Pi_1 C Pi_1. Define on P

    H2^C=C_0-M,
    H4^C=M^2-(M C_0+C_0 M)/2+A^* C_1 A-Z^*Z/2,
    B_j=-P j Pi_1 T P.                                 (2)

The candidate effective generator is

    L_P^C rho=-i[delta epsilon^(-2)H2^C+delta H4^C,rho]
                    +kappa sum_j D[B_j]rho.             (3)

For each fixed T0, the full microscopic density from any P-supported density
differs from the embedded (3) by at most O(epsilon) in trace norm, uniformly
on [0,T0]. Constants depend on the fixed graph, delta,kappa,T0 and the uniform
T,j,C bounds, but not on S. The statement also applies to bounded unit-rotor
versions. It does not assume that (3) already has a resource-independent limit.

The canonical convention is the parent's positive-overlap all-cluster block
rotation. The anticommutator in (2) depends on respecting that convention;
a nonorthonormal Schur complement by itself gives a different fourth-order
matrix, similar to (2) but not the desired Hermitian operator.

## Analytic cluster rotation and coefficient derivation

Put h(epsilon)=W+epsilon T+epsilon^2 C. The finitely many integer W clusters
remain separated for uniformly small epsilon, by the resolvent Neumann series
and the uniform bounds on T,C. Their Riesz projections Q_r(epsilon) are
analytic and differ from Pi_r by O(epsilon). The same polar construction

    S(epsilon)=sum_r Q_r(epsilon)Pi_r,
    U(epsilon)=S(epsilon)[S(epsilon)^*S(epsilon)]^(-1/2)

is unitary, is I+O(epsilon), and makes U^*hU commute with W exactly.
All inverse square roots use a norm-convergent series near the identity.

Xi=(-1)^W satisfies Xi T Xi=-T and Xi C Xi=C. Hence
h(-epsilon)=Xi h(epsilon)Xi, and the constructed diagonal blocks are even
analytic functions. Consequently

    delta epsilon^(-4) U^*hU
         =delta epsilon^(-4)W+O(epsilon^(-2))           (4)

globally, while its P block has a remainder O(epsilon^2) after the two
coefficients in (2). Uniformity is dimension independent at fixed graph.

For an explicit coefficient calculation, write the low cluster as the graph
of X:P->Q, Q=I-P. Its invariance equation is

    epsilon A+(W_Q+epsilon T_QQ+epsilon^2 C_Q)X
          =X(epsilon^2 C_0+epsilon A^*X).               (5)

There is no off-diagonal C block, and PTP=0. Set
X=epsilon X1+epsilon^2 X2+epsilon^3 X3+... and R=W_Q^(-1).
The first coefficients are

    X1=-A,   X2=Z/2,
    A^*X3=M^2-M C_0+A^* C_1 A-Z^*Z/2.                 (6)

For clarity, the epsilon^3 equation is

    W_Q X3=-T_QQ X2-C_Q X1+X1 C_0+X1 A^*X1.

Left multiplication by A^*R, with A at W=1 and Z at W=2, gives (6).
The nonorthonormal graph-coordinate matrix is

    h_graph=epsilon^2 C_0+epsilon A^*X.

Its second coefficient is C_0-M and its fourth coefficient is the last
line of (6). The canonical isometry multiplies this graph matrix on the
left by (I+X^*X)^(1/2) and on the right by its inverse. Since
(I+X^*X)^(1/2)=I+epsilon^2 M/2+O(epsilon^3), the additional fourth-order
term is [M,C_0-M]/2=[M,C_0]/2. This converts -M C_0 precisely to
-(M C_0+C_0 M)/2, proving (2). Both Hamiltonian coefficients H2^C and H4^C are self-adjoint.

The first derivative of U is unchanged because C enters at epsilon^2:
U'(0)P=-A. Therefore

    U^* j U P=epsilon B_j+O(epsilon^2),   P B_j P=B_j.  (7)

The leading effective formation operator is unchanged. This statement does
not assert that the fourth-order Hamiltonian or its subsequent waiting law
is unchanged by C.

## Uniform density approximation with the large dissipator

The parent residual proof applies with the new coefficient (2), for the
following explicit reasons. Let G_epsilon be the exactly rotated full
generator, E0 the P-matrix embedding, and

    R_epsilon=G_epsilon E0-E0 L_P^C.

Use Off X=QXP+PXQ and Diag X=PXP+QXQ. Equation (7), the exact Hamiltonian
block diagonalization and the P-block O(epsilon^2) Hamiltonian remainder give

    ||Off R_epsilon||_(1->1)=O(epsilon^(-1)),
    ||Diag R_epsilon||_(1->1)=O(epsilon).                (8)

In particular the QP loss term epsilon^(-2)Q j_tilde^*j_tilde P is generally
O(epsilon^(-1)); it has not been discarded. The P recycling/loss agree with
the B_j dissipator to O(epsilon), and Q recycling starts at O(epsilon^2).

Let A0 X=-i delta[W,X]. On Off matrices its inverse is bounded, using
R=W_Q^(-1) on the Q side. Define the Hermiticity-preserving correction

    K_epsilon=-epsilon^4 A0^(-1)Off R_epsilon,
    E_epsilon=E0+K_epsilon.

Then ||K_epsilon||=O(epsilon^3), and its exact residual is

    G_epsilon E_epsilon-E_epsilon L_P^C
       =Diag R_epsilon
        +(G_epsilon-epsilon^(-4)A0)K_epsilon
        -K_epsilon L_P^C.                              (9)

Both remaining generator norms are O(epsilon^(-2)): (4) controls the full
rotated Hamiltonian, the full dissipator has that order, and C_0,H2^C,H4^C
are uniformly bounded. Thus (9) is O(epsilon) in induced trace norm.

Duhamel between the full and target CPTP semigroups bounds the error on
Hermitian densities by the O(epsilon^3) endpoint correction plus T0 times
this residual. Transforming the original and final states by U=I+O(epsilon)
adds O(epsilon), establishing the claim. Positivity of the correction map
is not assumed. For each fixed epsilon all generators here are bounded,
including on the rotor trace class, so the no-jump/jump expansion supplies
the semigroups and their contractivity.

Finite classical event/count registers inherit this argument when C acts
trivially on the register and has the stated record-number conservation.
No claim about arbitrary continuously conditioned microscopic histories is
added. The added C is an explicit Hamiltonian assumption throughout.


## Clarified adjoint scope

Only the Hamiltonian coefficients H2^C and H4^C are asserted self-adjoint. The raw graph fourth coefficient need not be self-adjoint when [M,C0] is nonzero, and the formation maps need not be self-adjoint. This incorporates the submission’s ROOT_GENERAL_TARGET_CORRECTION.


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
- [finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24](FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8841, frozen head `fed8422aaaaff35c4da1ae613d6e889a989613b4`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/bounded_block_diagonal_compensation_target_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
