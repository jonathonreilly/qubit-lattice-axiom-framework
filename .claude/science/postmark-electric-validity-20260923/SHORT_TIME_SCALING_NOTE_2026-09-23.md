---
claim_id: postmark_electric_short_time_scaling_2026_09_23
claim_type: bounded_theorem
claim_scope: "For the supplied integer-spin one-vacancy Jacobi matrices M_S on I_S=[-5S,5S-4], the zero-extended operators M_S converge strongly to M_infinity=2I+U+U* on l2(Z) and have norm at most 4. Therefore, with C=S(S+1), the exact generator G_S=M_S^2-CM_S obeys e^{-i(tau/C)G_S}|0> -> e^{i tau M_infinity}|0> for every fixed real tau. The bounded vacancy projector has limiting expectation 1/3+(2/3)J_0(2 sqrt(3) tau). This is a shrinking-time theorem only; it makes no assertion at a fixed nonzero laboratory time."
upstream_dependencies:
  - PR #8831 supplied one-vacancy model and Jacobi entries
runner: .claude/science/postmark-electric-validity-20260923/scaled_time_limit_probe.py
---

# Exact short-time scaling limit of the post-mark vacancy observable

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result up front

For the supplied exact finite-spin generator, the actual vacancy expectation has a strong limit at the shrinking time `t=tau/C`, equal to `1/3+(2/3)J_0(2 sqrt(3) tau)`. The fixed-laboratory-time limit remains open.

## Claim

For integer spin S in the supplied one-vacancy sector, let C=S(S+1), let M_S=-H_{2,S} be the finite symmetric tridiagonal matrix on I_S=[-5S,5S-4], and let G_S=M_S^2-CM_S. Embed its path basis into l2(Z) by zero extension. Then, for each fixed real tau,

    exp[-i (tau/C) G_S] |0>  ->  exp[i tau M_infinity] |0>

strongly as S tends to infinity, where

    M_infinity = 2 I + U + U*,       U|n> = |n+1>.

For the supplied observable O=1[n mod 3=0],

    lim_{S->infinity} <O>_{t=tau/C}
      = 1/3 + (2/3) J_0(2 sqrt(3) tau),

where J_0 is the order-zero Bessel function.

This result is conditional on the #8831 finite-spin model and its output sector. The time is tau/C, so the theorem does not answer the predeclared comparison at fixed laboratory times 1/4, 1/2, and 1.

## Proof

Write a_n=(M_S)_{n,n} and b_n=(M_S)_{n,n+1}. On any fixed finite set of path coordinates, the exact residue polynomials in [FINITE_SPIN_JACOBI_COEFFICIENTS.json](FINITE_SPIN_JACOBI_COEFFICIENTS.json) give a_n -> 2 and b_n -> 1 because each fixed electric-flux numerator is independent of S while C grows. Thus M_S converges entrywise on finitely supported vectors to M_infinity.

The spin-link factors have the form sqrt(1-m(m+a)/C), with integer m and a in {-1,1}. For every allowed link, 0 <= m(m+a) <= C, so each factor lies in [0,1]. A diagonal entry of M_S is the sum of two return contributions and lies in [0,2]; an off-diagonal entry lies in [0,1]. Every absolute row sum is therefore at most 4, including boundary rows with missing outward edges. Since M_S is symmetric, ||M_S|| <= 4. Also ||M_infinity|| <= 4.

Let Mtilde_S be the zero-extended finite matrix on l2(Z). The finite-support convergence and the uniform norm bound imply Mtilde_S -> M_infinity strongly. Set A_S=G_S/C=Mtilde_S^2/C-Mtilde_S on the embedded finite sector and zero on its orthogonal complement. Since ||Mtilde_S^2/C|| <= 16/C, A_S -> -M_infinity strongly and sup_S ||A_S|| < infinity. Polynomial approximation to the exponential on a common compact spectral interval then gives exp(-i tau A_S)|0> -> exp(i tau M_infinity)|0> for each fixed tau.

The diagonal unitary V|n>=omega^n|n>, omega=exp(2 pi i/3), satisfies O=(I+V+V*)/3. Under the Fourier transform, M_infinity has multiplier 2+2 cos(k). The expectation <exp(i tau M_infinity)0, V exp(i tau M_infinity)0> is the normalized integral of exp(i tau [m(k-2 pi/3)-m(k)]), with m(k)=2+2 cos(k). The phase difference is a sinusoid of amplitude 2 sqrt(3), so this integral is J_0(2 sqrt(3) tau). Substituting into the projector identity proves the formula.

## Exact reduction of the fixed-time wall

For each finite S, M_S commutes with G_S=M_S^2-CM_S, so the exact evolution factors as

    exp(-it G_S)|0> = exp(it C M_S) eta_S(t),
    eta_S(t) = exp(-it M_S^2)|0>.

The same strong convergence and uniform bound used above imply eta_S(t) -> exp(-it M_infinity^2)|0> strongly for each fixed t. Thus the exact-side fixed-time problem reduces to the long-time action of exp(i T M_S) on a convergent initial profile, with T=Ct growing like S^2. The finite path interval has length O(S), so the fixed-tau theorem cannot control this regime; the spin-dependent boundary and coefficients enter before T reaches its fixed-time value. This factorization identifies the remaining evolution but gives no limit or discrepancy. The rotor comparison still additionally requires the unbounded D term and its selected self-adjoint realization.

## Exact local curvature and the wall

The exact generator has three nonzero diagonals beyond its main diagonal:

    (G_S)_(n,n)   = a_n^2 + b_(n-1)^2 + b_n^2 - C a_n,
    (G_S)_(n,n+1) = b_n (a_n+a_(n+1)-C),
    (G_S)_(n,n+2) = b_n b_(n+1).

For V_(n,n)=omega^n, this gives

    [G_S,V]_(n,n+1) = (omega-1) omega^n b_n(a_n+a_(n+1)-C),
    [G_S,V]_(n,n+2) = (omega^2-1) omega^n b_n b_(n+1),

with conjugate entries below the diagonal. If z_S(t)=<exp(-itG_S)0,V exp(-itG_S)0>, then z'_S(t)=i<[G_S,V]>_t. Since a_0,a_1 ->2 and b_0 ->1, the (0,1) entry divided by C has magnitude tending to |omega-1|=sqrt(3). Also ||[G_S,V]|| <=2||G_S|| <=32+8C by ||M_S||<=4. Hence ||[G_S,V]|| is Theta(C), and this direct continuity estimate cannot be uniform in spin.

Because G_S=M_S^2-CM_S has bandwidth two, it connects n=0 only to n=0, +/-1, and +/-2. Every nonzero off-diagonal destination is outside the class-zero projector. Direct differentiation at t=0 gives

    p_S''(0) = -2 sum_{n in {-2,-1,1,2}} |(G_S)_{n,0}|^2.

The nearest-neighbour entries are b_n(a_n+a_{n+1}-C); the next-neighbour entries are b_n b_{n+1}. Since a_n ->2 and b_n ->1 at each fixed n, it follows that

    p_S''(0)/C^2 -> -4.

This curvature calculation and the Bessel scaling curve show why ordinary fixed-derivative or continuity estimates are not uniform in S. They do not imply that p_S(t) has, or lacks, a limit when t is held fixed: tau=Ct then diverges, outside the theorem's fixed-tau regime.

## Scope and open obligations

The limit keeps tau fixed while the physical time shrinks like 1/C. It does not control the finite-spin boundary over fixed laboratory times, macroscopic electric tails, the candidate Friedrichs evolution, fourth-order corrections to the post-mark Hamiltonian, or the actual fixed-time vacancy expectation. No framework axiom or primitive is used to derive the supplied Hamiltonian, spin-link representation, or first-mark output. No axiom change follows.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: conditional on the supplied six-site Hamiltonian, integer-spin link representation, and actual first-mark output
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "For fixed laboratory times, prove a long-tau uniform limit with spin-dependent boundary and coefficient control, or certify a bounded-observable discrepancy; the present theorem only holds at t=tau/C."
```

The downstream consumer is [open PR #8831](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8831). This theorem makes no claim about the framework's four axioms, any other sector, or a volume limit.

## Verification

The adjacent `scaled_time_limit_probe.py` checks the spectral convergence numerically on a finite spin sequence and compares it with the derived Bessel curve. The proof uses the exact Jacobi entries and uniform operator bound above; the diagnostic is not used as proof.
