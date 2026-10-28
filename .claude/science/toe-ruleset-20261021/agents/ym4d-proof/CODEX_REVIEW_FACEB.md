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

## R2 — The four-link witness is admissible in the two-condition class; its decimal certificate is rounded the wrong way

**Verdict: CONFIRMED** for co-closedness and the stated profile-only admissibility, and for the exact coefficient under the explicit centered axial convention reconstructed below. **Verdict: REFUTED** for the exact decimal equality at FACEB.md:264; **NOT-VERIFIED** for identifying this two-condition class with the entire actual-response admissibility class (FACEB.md:259-284, 672). **Claim status: PROVEN** for the explicit construction below; **CONDITIONAL** for transfer to any additional, uninspected lane hypotheses.

Set the root c_X=0 and the plaquette anchor p=(1,0,0,0). Before division by 8, the oriented boundary has the following nonzero links:

| link base b | direction | coefficient |
|---|---:|---:|
| (1,0,0,0) | 0 | +1 |
| (2,0,0,0) | 1 | +1 |
| (1,1,0,0) | 0 | -1 |
| (1,0,0,0) | 1 | -1 |

At each of the four vertices, incoming and outgoing boundary coefficients cancel. Thus delta u=0. For every scalar mu, <d mu,u> is the telescoping circulation around this plaquette and is zero. At the plaquette itself du=4/8=1/2, so u is nonzero and not closed. All four link bases have infinity distance 0 or 1 from the anchor p; |u|=1/8 <= (1+|b-p|_infinity)^(-3), with equality at the distance-1 bases. This checks the C_0=1 profile under the link-base distance convention (also valid for distance to the plaquette support); that metric convention must remain explicit. The same scalar construction embeds along any fixed unit Lie-algebra direction at the stated trivial background. It does not prove an elliptic-slice constraint, a response equation, a minimizing-representative condition, or any additional block constraint.

I independently reconstructed the standard centered model: h averages the oriented integral from 0 to t over t in {-1,0,1}^4 and all 24 coordinate orders. At scale n_i=3^i, Q_n averages the n-step straight integral over offsets in [-(n-1)/2,(n-1)/2]^4, with weight n^(-4). This has Q_n d=d A_n and sends a constant 1-form to n times itself, as required by YSUP.md:159-168. No supplied funnel code was executed or read. For a unit link at b in direction mu, its contribution to Q_n at z is

    n^(-4) 1_{|b_j-n z_j| <= r for j != mu}
      * max(0, min(n-1,b_mu-n z_mu+r)-max(0,b_mu-n z_mu-r)+1),
    r=(n-1)/2.

Enumerating only 81 endpoints and 24 coordinate orders gives these exact h Q_n coefficients for the four links above, in the same order:

| n | edge 1 | edge 2 | edge 3 | edge 4 |
|---|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 1/54 |
| 3 | 10/2187 | 1/4374 | 10/2187 | 10/6561 |

Consequently phi_1=-1/54 and phi_2=1/4374-10/6561=-17/13122 before normalization. For every n_i>=9, both transverse members of each oppositely signed pair lie inside the same centered averaging block, with identical longitudinal multiplicities; hence Q_(n_i)u=0 identically. This is a proof of termination, rather than inference from checking phi_3, phi_4, phi_5. Dividing by 8 yields

    Phi_k(u)=(-1/54-17/13122)/8=-65/26244,     k>=2.

For a coarse torus with at least three sites per direction, choose the cell with c_X and its adjacent roots. The witness lies in the centered c_X block, and the other roots' disjoint block funnels see no support, so their values are zero. Its cell oscillation is therefore 65/26244. This supplies a counterexample sequence to a k-uniform class bound. A theorem for every coarse cell or every torus size would need extra quantifiers: in particular a one-site coarse torus has zero oscillation. Such a universal lower claim is unnecessary for the no-go.

The numerical correction is exact:

    0.0024768 - 65/26244 = 89/2050312500 > 0.

Use (65/26244)n^2, or the downward-rounded 0.0024767 n^2, as this witness's rigorous certificate. The class supremum might exceed the witness value; this arithmetic refutes the displayed equality and this witness's certificate for the rounded lower bound, not the abstract possibility of a larger supremum.

Scope warning: FACEB's source anchor for the class is expressly the `g_0 clause` (line 276), while TENTQ.md:381-390 asks about a named representative Y_* and explicitly distinguishes the tested compact source from a response. The construction proves that profile+co-closedness alone cannot imply (TENT-osc) in the reconstructed model. It cannot establish actual-response admissibility from that clause. Source-level equality of the reconstructed block conventions with the complete uninspected RG definition remains NOT-VERIFIED; the exact arithmetic agreement is not a substitute for that identification.

## R3 — 243/260 is correct; the normalization erratum is real; `any fix must change h_0` is too strong

**Verdict: CONFIRMED** for FACEB.md:440-441, 610-622; **REFUTED** for the unrestricted `Any fix must change h_0` at FACEB.md:454-455. **Claim status: PROVEN** for the ratio and witness localization; **OPEN** for actual-response localization and the space of possible repairs.

Using one common normalization throughout,

    (-1/54)/(-130/6561) = (-1/432)/(-65/26244) = 243/260.

Thus the first term contributes exactly 1215/13 percent, whose two-decimal rounding is 93.46 percent. The second term has the same sign and fraction 17/260. This figure is free of the neighboring normalization mixture. YSUP.md:249 does mix unnormalized phi_1, phi_2 with normalized psi_u; its mixed ratio is 486/65, not a physical fraction of the total. Correct the total there to -130/6561, or divide both terms by 8.

The inference about all fixes changes quantifiers. The exact fractions are those of one witness. An actual response may have additional restrictions or cancellation without changing h_0, as FACEB itself admits at lines 639-645. Even within the broad two-condition class, v_k=n^(-2)u is admissible with the same upper profile constant C_0=1 and has n^2 osc(Phi_k(v_k))=65/26244. This does not repair the universal class bound (u still defeats it), but it shows why a class counterexample does not force an h_0 redesign for an identified response family. Higher-level cancellations for other inputs are likewise not decided by the two same-sign witness terms. The valid conclusion is that improving only large-i upper estimates cannot remove this fixed witness's nonzero i=0 contribution while its exact funnel remains unchanged.

## R4 — `dimensionless` has been promoted to `k-independent`

**Verdict: REFUTED** at FACEB.md:139-145, 669 (strings `carries no k at all` and `k-free dimensionless number`). **Claim status: PROVEN** for the counterexample; the actual response's k dependence is **OPEN**.

The very identity quoted at FACEB.md:144 and YSUP.md:167 is Phi_k(d delta_c)(c)=3^(-4k)-1. Its values -80/81 and -6560/6561 at k=1,2 differ by -80/6561. Units do not depend on k, but a dimensionless value can. This is a dependency error, not a change in the meaning of n: n=3^k is consistently identified. The stronger profile-class example v_k=n^(-2)u in R3 shows directly that the allowed k-dependent input family may supply the missing smallness. Neither unit conversion nor an upper profile hypothesis supplies a lower bound on that family.

