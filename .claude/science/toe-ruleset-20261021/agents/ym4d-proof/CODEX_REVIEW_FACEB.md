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

## R5 — Baseline prices check, but the doubled-currency break-even is wrong

**Verdict: CONFIRMED** for the displayed rounded P(k), 151.610 decades, k*=160.380, and k*=42.552 at FACEB.md:505-531. **Verdict: REFUTED** for k* approximately 81.7 at FACEB.md:536-537. **Claim status: CONDITIONAL** on X1, X2, and the frozen reference constants; **PROVEN** for the arithmetic formulas below.

I used rational interval arithmetic, not Decimal or floating point. For x>=1 and t=(x-1)/(x+1), sum the first 80 terms of

    log(x)=2 sum_{j>=0} t^(2j+1)/(2j+1),

and bound the positive remainder by 2 t^161/[161(1-t^2)]. I used log(10)=3 log(2)+log(5/4), and divided positive intervals with outward bounds. This gives the following rigorous intervals (decimal endpoints are rationals):

| quantity | enclosing interval |
|---|---|
| log10(3) | [0.477121254, 0.477121255] |
| DXprime decades | [151.609771637, 151.609771638] |
| epsilon1 decades | [39.173925197, 39.173925198] |
| kstar DXprime | [160.379708394, 160.379708395] |
| kstar epsilon1 | [42.552379043, 42.552379044] |
| kstar doubled currency | [80.939854197, 80.939854198] |
| P(10) | [8.111061330, 8.111061331] |
| P(42) | [38.646821632, 38.646821633] |
| P(160) | [151.247437746, 151.247437747] |
| P(183) | [173.195015463, 173.195015464] |
| P(917/5) | [173.576712467, 173.576712468] |
| P(1778/5) | [337.897272592, 337.897272593] |
| P(356) | [338.278969596, 338.278969597] |

For the baseline C_Omega=1 and omitted C_SR, the exact symbolic formulas are

    D = 152 - log10(307/125),
    k* = (3 + D/log10(3))/2,
    2P(k)=D  =>  k*_double = (3 + D/[2 log10(3)])/2
                           = (k* + 3/2)/2.

Thus the doubled-currency break-even is approximately 80.940, not 81.7. The first violating integer levels are 161 in the original currency and 81 in the doubled currency (given these reference assumptions).

The table is mathematically meaningful as conditional bookkeeping. Without X2 it says nothing about exhausting the programme ceiling: eta, DXprime's bounded quantity, and the particular epsilon_1 have no verified common unit or identification. Without X1 it does not even establish this self-map's constraint. The claims that X1/X2 occur nowhere in the full repository are NOT-VERIFIED under the read limit; their absence from the inspected derivation is explicit. The source identity/value of epsilon_1, C_SR, and C_Omega is also NOT-VERIFIED outside the quoted assumptions.

Keep the constants live: if DXprime=(307/125)10^(-152)/C_Omega and the eta ceiling is 3^(3-2k)/C_SR, then

    k* = [3 + {152-log10(307/125)+log10(C_Omega)-log10(C_SR)}/log10(3)]/2.

The tabulated 160.380 freezes C_Omega=1 and omits log10(C_SR); it is not a fixed programme threshold when either constant is an output. Likewise a change of currency eta proportional to g_0 rather than g_0^2 must transform the entire ceiling and any prefactor, not merely relabel its units. The homogeneity observation at FACEB.md:475-479 is correct as a conditional algebraic statement: decreasing a nonzero eta cancels out of C(k)eta^2<=C_SR eta^2 and cannot repair nonuniform C(k).

## R6 — FB-NOEST is not three identities plus one universally attained inequality

**Verdict: REFUTED** for the claimed inference and the unrestricted factor-8 comparison at FACEB.md:234-255, 405-418, 646-648, 671. **NOT-VERIFIED** for the separate TG-TV/TG-OPT theorems and their admissible competitor class, whose source is outside this review's read budget. **Claim status: GAP** for FB-NOEST as written; **PROVEN** for the distinctions and corrected error estimate below.

**What is an identity.** With Q_X(S)=sum_l <d(ev chi_X),S_l>, one obtains

    sum_X Q_X(S) Phi_X
      = sum_l <sum_X Phi_X d(ev chi_X),S_l>
      = sum_l <d(ev sum_X Phi_X chi_X),S_l>.

This re-derives TQ-INT (TENTQ.md:263-268, 355-361). FACEB step 1 uses D(S)(c_X), whereas TQ-INT uses Q_X(S); the identification between the root charge and the tent-weighted charge is imported, not proved in the inspected text. The original COF-res identity therefore remains NOT-VERIFIED here, rather than being accepted from its status label.

**What is an inequality.** TENT-TV explicitly invokes the triangle inequality (TENTQ.md:283-287). Going from the exact pairing to TQ-osc also requires

    |sum_l <F_l,S_l>| <= sum_l |<F_l,S_l>|
                         <= sum_l ||F_l||_1 ||S_l||_infinity,

followed by the norm conversion and the bound of a sum of corner deviations by a multiple of oscillation. These can be packaged as one corollary but remain different opportunities for strictness. FACEB step 4 is a decay upper bound plus an asserted dominance conclusion, not a third identity. In particular its core Theta(C_0) is precisely the response lower bound that section 4.3 leaves OPEN.

**Attainment has quantifiers.** A one-corner Phi and c=0 give Psi=Phi_X chi_X; the triangle inequality in the global TENT-TV bound is then equality. For arbitrary unconstrained slot fields, choosing S_l proportional to sign(F_l), with one nonzero slot, attains the dual norm ||F_l||_1. These facts establish possible saturation in a large source class. They do not say that the nonlinear physical source has that sign pattern, or even that this pattern is admissible after all row constraints.

Conversely, a nonzero co-exact source slot S_l=delta W has <d(ev Psi),S_l>=<dd(ev Psi),W>=0 for every Psi while its source norm is positive. It can be supported on one interior plaquette of a coarse cell. Thus a nonzero oscillation can coexist with zero residue. No finite universal ratio, in particular 8, compares the upper bound to the actual object for all such sources. FACEB itself recognizes this null subspace at lines 355-357. A worst-case operator-norm sharpness claim needs explicit suprema and an admissible joint extremizer; it is not a pointwise lower bound and has not been established for the actual source here.

**The claimed multiplicative asymptotic lacks a charge hypothesis.** Write a=Phi_(X_p). If all other corner values have magnitude <=C C_0 n^(-2), the exact identity gives only

    | |T_p(S)| - n^2 |Q_(X_p) a| | <= C C_0 sum_(X!=X_p) |Q_X|.

Converting this to FACEB's (1+O(n^(-2))) requires control of

    C_0 sum_(X!=X_p)|Q_X| / |Q_(X_p) a|.

No such bound is supplied. A neutral charge vector (Q_core,Q_1,Q_2)=(0,1,-1), with potential (a,n^(-2),0), has residue 1 while the claimed leading product is zero. Neutrality does not exclude it. Such a charge pair can be realized in the unconstrained chain-source model by a unit path between two non-core corner roots: the pairing with d chi_X telescopes to their root indicator differences. This is a counterexample to the claimed deduction from those algebraic/decay premises, not a claim to have constructed a nonlinear Yang-Mills row.

**The lower-bound domain is missing.** FACEB describes the remaining freedom as a level-0 extension of prescribed root values (lines 408-414), then imports a bound for `every admissible competitor`. Prescribed root values alone do not imply ||d mu||_1>=n^3 osc at l=0: an extension supported only at one root, with value a, has ||d mu||_1=8|a| on a large 4D torus, whereas the claimed lower bound is n^3|a| (729|a| when n=9). A block-average constraint could exclude this extension. It must be stated and matched before using TG-TV. I do not assert that this extension satisfies the uninspected TG-TV hypotheses.

Therefore FB-NOEST does not establish that all estimator improvements for the actual source/response are impossible. The much narrower class obstruction in R2 survives independently: fixed exact witness values cannot be reduced by sharpening an upper estimate on that same witness.

## R7 — Gate audit: a normalization-breaking mutation passes A1-A6, including the designed failure

**Verdict: REFUTED** for the claimed normalization/admissibility corroboration and the strong independence language at FACEB.md:573-575 and checks/fb1_criteria.md:21-23, 30. **CONFIRMED** for the limited cochain identities and the recorded integer A1-A6 outcomes. **Claim status: PROVEN** for the explicit blind spot; **NOT-VERIFIED** for using these checks to decide any funnel, response, or estimator no-go.

I executed only the first 161 lines' integer definitions of fb1_bianchi.py in memory, then called its core with the stated seed. I did not run its Decimal section or write a test file. The unmodified core reproduced A1-A5 acceptance and the designed-control counts (6,25,7). I then replaced every plaquette-incidence coefficient c by 2c and repeated the same clean and one-sign-flip tests:

| incidence | A1-A5 criteria satisfied | A6 control fires | nonzero witness values | corrupted A1/A2/A3 counts |
|---|---|---|---|---|
| D1 | all five | yes | {-1,+1} | 6 / 25 / 7 |
| 2 D1 | all five | yes | {-2,+2} | 6 / 25 / 7 |

The second incidence violates the registered unit-coefficient plaquette convention and, after the claimed 1/8 normalization, violates the C_0=1 profile at distance 1: 1/4>1/8. Yet every integer gate clause, including its designed-failure control, accepts it. This is not an error alleged in the unchanged script's coefficients; it is an executed counterexample to the gate's power to certify the imported normalization. A4 prints support/values at script lines 149-150 and 182, but its acceptance expression at line 183 checks only three booleans. It does not assert support=4, coefficients={-1,+1}, the location relative to the block root, or any profile inequality.

| gate | what it can decide | unresolved or dependent part |
|---|---|---|
| A1 | can detect d1 d0 != 0 on sampled inputs; local symbolic cancellation proves the correctly defined identity | not orientation/scale fidelity to an external convention; finite sampling is not the universal proof |
| A2 | can detect a defect in the transpose-application routine or a nonzero d1 d0 pairing | algebraically <d0 phi,d1^T W>=<d1 d0 phi,W>; the same incidence defines both sides, so it is not independent evidence for the incidence normalization |
| A3 | checks that the selected co-boundary is orthogonal to tested gradients | translation to site 0 is harmless for cochain algebra but cannot validate the witness's root placement for h_0 |
| A4 | excludes a zero witness and a non-co-closed witness | does not enforce the numerical support values or admissibility used by FB-CLASS |
| A5 | proves a generic pairing need not vanish | says nothing about the funnel or physical source class |
| A6 | detects the chosen single-entry sign corruption | does not detect coherent scale errors, whole-row orientation reversals, or a wrong source/response identification |
| A7 | can reject insufficient numerical agreement between two precisions | a coherently wrong formula, coefficient, constant identity, or currency gives the same answer at both precisions and passes |

The A7 source (fb1_bianchi.py:212-243) compares two evaluations of the same formula with the same constants. It cannot adjudicate X2 or catch the separate 81.7 error, which is not one of its rows. Decimal logarithms are rounded transcendental evaluations, not exact rational arithmetic; the `exact decimal` description at FACEB.md:502, 566 and script:209 is inaccurate. This review instead used the rigorous rational intervals in R5. The recorded 50-versus-100-digit discrepancy itself was not independently reproduced and remains NOT-VERIFIED.

The strongest honest gate conclusion is: the supplied integer implementation passes several consistency checks and one local corruption control. That is useful, but cannot confer the claimed proposition statuses. This is precisely the `could this check have failed in the way that matters?` distinction.

## R8 — The no-go reuses d and delta at different form degrees

**Verdict: REFUTED** for the deduction at FACEB.md:355-385, 365-370, 722-724 that the tested orthogonality exhausts the source/response derivative or gauge routes. **Claim status: PROVEN** for the type distinction and counterexamples; **OPEN** for whether any such route improves the full response.

Pin the symbols to their actual maps:

    d0: vertices -> links,        delta1=d0^T: links -> vertices,
    d1: links -> plaquettes,      delta2=d1^T: plaquettes -> links.

fb1_bianchi.py:54-65 defines d0 and d1. Its line 129 uses delta2 to construct the link witness; line 145 uses delta1 to test its divergence. What d1 d0=0 actually proves is

    <d0 phi, delta2 W>=0,       delta1 delta2 W=0.

The root source D(S) in FACEB.md:377 is instead a sum of pulled-back delta1 S_l, hence a scalar. It does not belong to the co-exact-link subspace im(delta2) merely because it is called a divergence. A single source link S from a to b gives delta1 S=delta_b-delta_a, and <Phi,delta1 S>=Phi(b)-Phi(a), which need not vanish. Thus `D(S) is entirely inside the second` at line 367 conflates different degrees. The relevant cancellation requires S_l=delta2 W_l, not just the tautology that its scalar divergence is a divergence.

On the response leg, differentiating a 1-form means d1 Y. The identity Phi_k d0=A-ev concerns inserting an exact 1-form; it is not a formula for recovering Phi_k Y from d1 Y. In fact d1 u!=0, so curvature differentiation does see the witness. Orthogonality to im(d0) is not proof that an arbitrary scalar funnel functional annihilates all gauge additions. From FACEB's own quoted identity,

    Phi_k(u+d0 mu)-Phi_k(u)=A mu-ev mu,

which is generally nonzero regardless of delta1 u=0. The total source pairing may compensate this change; checking that is the separate, uninspected TG-PRICE theorem, not a consequence of the witness's being co-exact. Therefore `there is nothing for a gauge to act on` at line 724 is an invalid second proof of that theorem.

Finally, `annihilates exactly the exact part` omits harmonic 1-forms on a periodic torus. A nonzero constant 1-form is d1-closed but not the gradient of a periodic scalar, since its integral around a winding cycle is nonzero. This does not alter the local witness calculation; it refutes the stated exhaustive kernel description.

## R9 — The positive reframing retreats from its quantified headline and never repairs it

**Verdict: REFUTED** for the positive headline as a conclusion of the presented evidence (FACEB.md:632-648) and for its downstream reuse at 683-689, 699-707, 732-746. **CONFIRMED** that lines 639-645 disclose a real limitation. **Claim status: GAP** for the broad no-go; **PROVEN** only for the explicitly constructed profile-class obstruction under the stated model.

The headline says `Every k-uniform bound on T_p must come from the D(S) leg`. That universally excludes an actual-response property making Phi_k small. The next paragraph acknowledges exactly that unclosed possibility and switches to `a no-go about available routes`. These are different claims. The retreat is visible, rather than hidden, but the headline and several outcome/dispatch statements retain the stronger quantifier. FB-CLASS only says the two named inequalities do not imply a uniform bound for every field satisfying them. It cannot show that `no such property is currently available` in all lane hypotheses, and it cannot identify the only possible future repair.

An honest positive equivalent is: for every k>=2 there exists a co-closed C_0=1 profile field on the specified nondegenerate torus and a cell for which n^2 osc(Phi_k v)=(65/26244)3^(2k). Equivalently, for every finite C there is a k and such a v/cell violating that C. That statement retains the same class and quantifiers as the scoped negative claim. It does not mention the actual response or forbid response-specific cancellation.

The five named routes are not five independently exhausted mechanism families: FACEB.md:336-338 itself says three reuse one identity and a fourth is its homotopy. R6 and R8 identify unproved transitions in their purported closure. Under docs/ai_methodology/skills/no-go-discipline/SKILL.md N1, merely naming five routes cannot certify the five-family requirement. N4/N5 require matching the residual and resolution: a class witness and a single scalar funnel coordinate are not a lower bound for the physical response or total f_0. N7's actionable counter-route is already present: prove a structural restriction or cancellation for the actual named Y_* (or bound its total forcing as in R1), and test its coarse-cell oscillation. This remains unclosed.

N2/N3/N6: two summands at different roots are not thereby independent obstructions, and neither the quoted `sigma` size nor the absence of cancellation with the remaining response has been established here. X1/X2 and the precise source/representative constraints are explicit unresolved premises, not evidence of impossibility. N8's cross-cycle/ledger search was not performed because the owner's read boundary forbids it. No formal no-go packet acceptance or retained status is asserted; the user authorized only this scoped review, not ledger edits, commits, or an audit workflow.

The original ARTEFACT/SHARP-AND-FATAL decision table (FACEB.md:62-68) is capable of expressing an inconclusive result, so it is not intrinsically vacuous. Its application is the problem: SHARP-AND-FATAL requires an input satisfying the lane's hypotheses, while lines 685-689 substitute the enlarged two-condition class and concede that actual sharpness is OPEN. For the actual-response target, the honest outcome is NOT-VERIFIED / OPEN; for the explicitly defined larger class, the corrected counterexample is available.

## R10 — Concrete citation drift and conditional-status mismatch

**Verdict: REFUTED** for the following source locations and the blanket labeling claim; **NOT-VERIFIED** for references outside the allowed files/regions. **Claim status: GAP** for those provenance links, independent of mathematical corrections above.

| FACEB location | claim/citation | observed current source |
|---|---|---|
| 117-118 | Theorem TQ-INT at TENTQ.md:253-259 | those lines discuss the prior NEUT-box/GT-ell conclusion; the matching heading is 261 and the statement/proof is 263-268 |
| 21 | Corollary TQ-osc at TENTQ.md:277 | line 277 is a quantifier in Lemma TENT-TV; the corollary is at 289-292 |
| 582-584 | every claim using a funnel value is conditional on the source files and labeled so | FB-CLASS at 273 and 672 is expressly `UNCONDITIONAL`; fb1_criteria.md:39-42 makes the same conditionality promise |

FACEB's later TQ-INT references at 240 and 353 use the current matching range. The earlier copies are stale. YSUP.md:249 still contains the normalization mixture FACEB reports. The allowed YSUP normalization and TENTQ named-item anchors match their relevant strings. PROOF.md:6205-6240 at FACEB.md:348 was not inspected, because the two permitted extra files were consumed by the mandatory workflow and selected skill. Its accuracy is NOT-VERIFIED; I do not invent a drift amount. The same limitation applies to BFT_A/B, TGAUGE_PRICE, REVIEW_SF_S7, RLARGE and other external source claims.

No status label or cached acceptance substituted for a derivation in this review. The reconstructed witness arithmetic can support a new precise class theorem, but cannot retroactively make FACEB's unperformed source checks unconditional.

## R11 — Two inherited TENT statements also require missing qualifications

**Verdict: REFUTED** under the stated own-unit lattice derivative and ordinary scalar oscillation conventions; **claim status: GAP** for the unqualified source statements. These are secondary findings about the cited reduction, not a refutation of the correctly scoped witness no-go.

1. **Missing level-step factor.** TENTQ.md:277-287 states the pointwise factor bound |delta_mu(z)|<=15/(8n) for all 0<=l<=k. At l=k, ev samples adjacent coarse roots; choose corner values 0 and 1 along that edge. The tent interpolation takes those endpoint values, so the difference equals 1. The asserted bound is 15/(8n), equal to 5/24 at k=2, n=9. The Lipschitz derivation instead uses a step L^l/n, giving |delta_mu|<=15 L^l/(8n), optionally capped at 1 for the monotone tent. This identifies the scale dependence missing from the source's own proof sentence `the coarse step is 1/n`. It does not by itself invalidate the separately derived global total-variation bound or add a new power of n to the correct source norm conversion.

2. **Zero does not imply oscillation equals maximum absolute value.** TENTQ.md:301-306 asserts osc(Phi)=max|Phi| whenever the corner set contains a zero. With the standard osc=max(Phi)-min(Phi), values {-a,0,+a} have osc=2a and max|Phi|=a. The equality requires all values to have one sign (or a corresponding explicit extremum condition). Merely containing zero gives max|Phi|<=osc<=2 max|Phi|. The R2 witness has one nonzero signed corner and zeros, so its equality and exact coefficient remain valid. This source error matters when extrapolating that equality to arbitrary responses.

## Independent combinatorial certificate for the funnel fractions

This supplements the explicit enumeration in R2 with a short hand derivation; it is not a quotation of the prior rationals. Let W(z,mu) be the coefficient of a link in the centered 81-endpoint, 24-order axial average. For a positive link out of the origin, the mu step precedes all m other nonzero endpoint directions. Summing their choices gives

    W(0,mu) = (1/81) sum_(m=0)^3 binom(3,m) 2^m/(m+1) = 10/81.

For the positive direction-1 link out of (1,0,0,0), direction 0 must precede direction 1, and both precede any of the m active remaining directions:

    W((1,0,0,0),1)
      = (1/81) sum_(m=0)^2 binom(2,m) 2^m/[(m+1)(m+2)] = 1/54.

The reflected negative-direction links have the opposite W coefficient. Of the unnormalized plaquette's links, h_0 sees only the negative direction-1 link at (1,0,0,0), hence phi_1=-1/54.

After Q_3, the direction-0 pair cancels. The remaining direction-1 links are

    ((1,0,0,0),1): +2/81,    ((1,-1,0,0),1): +1/81,
    ((0,0,0,0),1): -2/81,    ((0,-1,0,0),1): -1/81.

Applying W therefore gives

    phi_2=(2-1)/(81*54)+(-2+1)*10/(81*81)
         =(1/54-10/81)/81=-17/13122.

For n_i>=9 the two transverse members of each boundary pair occupy the same averaging block and have identical longitudinal multiplicity, so every Q_(n_i)u link is zero. This proves the all-k termination under these explicit conventions. Plain Python Fraction arithmetic separately checked both binomial sums, the four-link profile and divergence, and every displayed fraction. No numerical linear solve, quadrature, or array library was used.

# Summary table

All lane file references above are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. Review verdicts apply only to the exact claim in the row; they are not audit statuses.

| target | review verdict | claim status after review | decisive result |
|---|---|---|---|
| FB-CLASS: explicit profile+co-closed witness | CONFIRMED under the explicit centered/link-base model | PROVEN for that construction | four boundary links; exact funnel -65/26244 for k>=2; nonzero oscillation on a specified nondegenerate cell |
| FB-CLASS: equality to -0.0024768 and that witness's rounded lower certificate | REFUTED | GAP until coefficient corrected | magnitude is 65/26244; rounding overshoot is 89/2050312500 |
| FB-CLASS: full actual-response admissibility / exact source convention match | NOT-VERIFIED | OPEN | g_0 is not automatically the named response Y_*; complete slice, profile metric and blocking constraints not inspected |
| FB-NOEST | REFUTED as written | GAP | strict pairing inequalities, missing charge comparison, and an unverified competitor domain; no universal pointwise factor 8 |
| FB-LOCAL: 243/260 and common normalization | CONFIRMED | PROVEN for the witness | both normalized and unnormalized ratios equal 243/260; YSUP:249 really mixes them |
| FB-LOCAL: every fix must change h_0 | REFUTED as a general implication | GAP | actual-response restrictions/cancellations remain possible without changing h_0 |
| FB-BOOT: no lower bound / only kernel signs missing | REFUTED | GAP | (2/3)||a+z||<=M<=2||a+z||; G>=0 alone does not control Z'' or source signs |
| Actual (TENT-osc) / actual sharpness | NOT-VERIFIED | OPEN | no lower or upper oscillation statement for the named physical response was proved here |
| Baseline price arithmetic | CONFIRMED | CONDITIONAL on X1/X2 and constants | D in [151.609771637,151.609771638]; k* in [160.379708394,160.379708395] |
| Doubled-currency break-even 81.7 | REFUTED | PROVEN correction | k* in [80.939854197,80.939854198] |
| Price as a programme-ceiling comparison without X2 | NOT-VERIFIED | GAP | mathematically evaluable numbers, no verified exchange rate |
| `dimensionless` implies `k-free` | REFUTED | GAP | the cited exact test already changes from -80/81 to -6560/6561 |
| A1-A6 supplied integer outcomes | CONFIRMED | PROVEN for executed checks only | reproduced the clean criteria and control counts (6,25,7) |
| Gate certification of normalization/admissibility | REFUTED | GAP | the mutation D1->2D1 passes A1-A6, including the control |
| Derivative/source-leg type identification | REFUTED | GAP | im(delta2) consists of link fields; D(S) is a scalar in a pulled-back im(delta1) |
| Broad positive reframing / fatality conclusion | REFUTED as an inference | GAP | it abandons an unclosed response-specific route while retaining a universal headline |
| Older TQ-INT/TQ-osc citations | REFUTED | GAP | correct anchors are TENTQ:263-268 and 289-292, respectively |
| PROOF.md and other out-of-scope citations | NOT-VERIFIED | OPEN for this review | not read; no fabricated line-drift finding |
| TENT-TV pointwise step and generic osc=max assertion | REFUTED as stated | GAP | use step L^l/n; a zero alone gives max|Phi|<=osc<=2max|Phi| |

# Numerical corrections and their scope

| refuted statement | correction |
|---|---|
| `65/26244 = 0.0024768` exactly | 65/26244 is strictly smaller by 89/2050312500; use the exact fraction or downward bound 0.0024767 |
| doubled-currency `k* approximately 81.7` | 80.939854197 < k* < 80.939854198; approximately 80.940 |
| at most `8` between the bound and every actual source pairing | no finite universal pointwise factor; nonzero co-exact sources can give zero pairing; a separately scoped operator-norm comparison remains unverified |
| the bootstrap gives `nothing below` | M >= (2/3)||a+z|| >= (2/3)max(A-B,0), with A and B supremum norms |
| TENT-TV's all-level pointwise factor `15/(8n)` | 15 L^l/(8n), optionally capped at 1; at l=k,n=9 the stated 5/24 cannot bound the endpoint difference 1 |
| `osc=max|Phi|` from a zero alone | max|Phi|<=osc<=2max|Phi|; equality needs an additional sign/extremum condition |

The checked numbers **243/260**, **93.46%**, **151.610**, **160.380**, **42.552**, and the baseline P(k) rows require no arithmetic correction. The mixed YSUP ratio **486/65** is numerically correct for mismatched normalizations and physically inappropriate as a fractional contribution; use a common normalization to obtain **243/260**.

**Single most dangerous unverified item:** whether the actual named response, with its full representative/slice constraints and total forcing g^natural+Z'', has a k-uniform nonzero *coarse-cell oscillation* after the bootstrap. Neither the compact source witness, a profile upper bound, two same-sign witness terms, nor positivity of G establishes that identification. Until it is resolved, exporting the class counterexample as a refutation of actual (TENT-osc), or treating the response route as closed, is unsupported.

Completion UTC: 2026-10-28 22:05:49 UTC. Only this deliverable was created/appended; no git commands, no .git access, no source edits, no external ledger reads, and no non-rational numerical job were used.

# Stdout summary

REFUTED: FB-BOOT's no-lower-bound/sign-only claim; FB-NOEST's universal sharpness inference; the broad reframed no-go; k-free-from-units; gate normalization certification. CONFIRMED: the explicit profile-class witness under stated conventions, 243/260, baseline price arithmetic. NOT-VERIFIED: actual-response admissibility and (TENT-osc), external source identities.
Corrections: 0.0024768 -> exact 65/26244 (safe lower decimal 0.0024767); 81.7 -> 80.939854197...; universal factor 8 -> no finite pointwise ratio; no bootstrap lower bound -> M>=(2/3)max(A-B,0); 15/(8n) -> 15 L^l/(8n); zero-implies-osc=max -> max<=osc<=2max.
Most dangerous unverified: the actual constrained response's coarse-cell oscillation after g^natural, Z'' and bootstrap cancellation.
