# PRE-STATED

UTC: 2026-10-28 21:50:40 UTC

Independent hostile review of FACEB.md. This section was written before reading the target or deriving its claims. Prior exposure: the owner's prompt supplies the claimed witness, constants, propositions, suspected normalization problem, and price formula. Model-family independence from the author has not been independently established here; the independent derivation is what this report can document.

## Targets and advance refutation criteria

1. FB-CLASS: reconstruct admissibility of u=(1/8)d*delta_p under every stated constraint; refute the claimed class theorem if a necessary constraint fails, the uniform quantifiers do not match, or the exact oscillation fails the asserted 2.4768e-3 lower bound.
2. FB-NOEST: reconstruct every equality and inequality and both attainment directions. An unproved equality, a conflation of scalar potential and projected gradient, or a nonuniform sharpness factor refutes the corresponding conclusion.
3. FB-LOCAL: compute each block contribution at one common normalization. A ratio unequal to 243/260, an unstated scale restriction, or an asymptotic term presented as a finite-scale identity refutes the stated scope.
4. FB-BOOT: determine exactly what follows from the absolute row-sum bound, including whether cancellation rules out all lower bounds or only a proposed local bound. A missing source-norm comparison or a sign claim stronger than the algebra supports is a refutation target.
5. Price: verify P(k) and the stated break-even using rational bounds for logarithms, with no floating-point numerical evaluation. Distinguish a conditional bookkeeping comparison from an identified physical constraint; inspect X2 explicitly.
6. Negative-claim reframing: compare the original quantifiers, admissible family, and conclusion with the positive version; a weaker positive assertion cannot validate a stronger no-go.
7. For every gate inspected: ask whether it could fail or whether its outcomes are exhaustive, exclusive, and capable of deciding the advertised question. Check symbol identity, frozen-constant assumptions, and source-citation scope.

## Operating boundary

No git commands or .git access. Only this report may be written. Source reads are restricted to FACEB.md; checks/fb1_criteria.md, fb1_bianchi.py, fb1_out.txt; the permitted YSUP.md and TENTQ.md regions; and two procedural files: docs/ai_methodology/SCIENCE_WORKFLOW.md and docs/ai_methodology/skills/no-go-discipline/SKILL.md. PROOF.md and other uninspected source claims will remain NOT-VERIFIED rather than being inferred from labels. All arithmetic checks use plain Python integers and fractions; no supplied numerical script will be executed if it violates that rule. Findings will be appended as they are established.

Review verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. No retained or audit status is conferred by this review.

# Findings

## R1 — FB-BOOT loses a contraction lower bound; kernel signs are not the only missing input

**Verdict: REFUTED** for the assertion that the decomposition gives no lower bound at all (FACEB.md:298-315, 673, strings `give no positive lower bound at all` and `missing half is only G_e`). **Claim status: PROVEN** for the following corrected algebra; **OPEN** for the actual response.

Write y_p=Phi_k(Y^p), a_p=Phi_k(g_p^natural), z_p=Phi_k(Z_p''), and y=a+z+Gy, with ||G||_(infinity->infinity)<=1/2. Put F=||a+z||_infinity and M=||y||_infinity. The forward and reverse triangle inequalities give

    F=||(I-G)y|| <= (3/2)M,
    M <= F+(1/2)M,
    (2/3)F <= M <= 2F.

Thus, with A=||a||_infinity and B=||z||_infinity,

    M >= (2/3) max(A-B,0),       M <= 2(A+B).

No sign hypothesis on G is needed. If B<A, some response has a positive lower bound; a uniform-in-p upper demand can be refuted by such a supremum witness. FACEB inserts its rough upper bound for M into a pointwise reverse triangle inequality and mistakes that failed estimate for nonexistence of lower estimates. The omitted lower bound is sharp: one scalar equation with G=-1/2, z=0 gives y=(2/3)a. G=+1/2 gives y=2a and saturates the upper bound.

There need not be a lower bound at each prescribed p: take a=(1,1), z=(0,0), G=((0,-1/2),(0,1/2)), y=(0,2). Both row sums of absolute values are 1/2 and y=a+Gy exactly. This preserves the narrower pointwise limitation while refuting the unrestricted `nothing below` conclusion. Also, to infer the upper bound for M, FACEB's A must be a supremum in p (or proved p-independent); line 296 defines only a single |Phi_k(g_0^natural)|.

Positivity of G alone is insufficient: a=(1), z=(-1), G=(0), y=(0) obeys G>=0 and cancels the forcing exactly. Even with z=0, a=(1,-1), G=((0,1/2),(0,1/2)), y=(0,-2) has G>=0 and a vanishing first response. Sign coherence of two terms in one witness is not sign coherence across all source indices q, and does not control Z''. Consequently the alleged single cheap missing condition is not established. M<=2(A+B) is an O(C_0) statement if A+B=O(C_0), not the asserted Theta(C_0) statement at line 298.

This algebra concerns a fixed linear funnel coordinate with a bounded response family. Transferring it to coarse-cell oscillation, a chosen representative, and a k-uniform lower bound on A-B remains a separate obligation.

