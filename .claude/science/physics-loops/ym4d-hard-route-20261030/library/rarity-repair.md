# Rarity repair: sparse exclusions and a common denominator
Provenance: OpenAI Codex / GPT-6 (exact serving variant and runtime effort are not exposed; requested effort: max); commit `e2c6b7b0ec7c8b9ceaf6ec071653ef3c7c0c2692`; research text, not an audit, grants no status.

## 1. Scope and exact probability space

**Discharged — source and method.** Paths below are relative to this loop directory. I read GOAL and FINISH's independence, efficiency and rules sections first, then all of `rarity-fresh-c.md` and its `rarity-fresh-c-263afacbd.md` gate, and Sections 1–3 of `rarity-fresh-x.md`, in bounded ranges. The checkout is the requested commit. The workflow file named by the repository entry point is absent; I did not substitute another revision. Only this output is written. Reading, editing and source-identity checks are not mathematical evidence. No numerical experiment, enumeration, external literature, audit or subagent is used. No remembered theorem is an established premise; any suggestion from memory will be marked explicitly.

**Gap — target retained without strengthening.** The targets are the consumer's full-law (RAR^1) and (RAR^ch), below every regular top and under the actual hierarchy mu, including terminal nonregular marks under mu. Nonregular means flux above T_2; the auxiliary label starts at T and is certain above 2T. A bound for a prescribed residual active pattern, or after conditioning on all holes, is a stronger proposed device, not the target. Quiet retains its specified local lift and regular-parent test. I do not change the kernel, thresholds or consumers by introducing a new label rule.

**Discharged — common law and denominator.** On a finite lattice include the auxiliary labels and Haar parents as coordinates. Let nu be fine product Haar followed by the actual, coupling-independent Markov kernels. The Wilson history measure is

    dP_t = Z_t^(-1) exp(-t A(U)) dnu,       t=x_0.

For a fixed regular top use its supplied disintegration, or a nonzero finite top window, in both integrals. A pointwise version at every exact top remains a separate support/disintegration obligation. If D is the exact active set, put W_t(D)=integral_{active=D} exp(-tA) dnu. Then, for prescribed marks M,

    P_t(M active) = [sum_{D containing M} W_t(D)]/[sum_D W_t(D)].       (1.1)

This identity is just a finite partition. It leaves all remote holes and all fine branches in the denominator. There is no requirement to delete M while preserving D minus M. In particular this note does not require (SEP).

**Discharged — why resolving wells needs a uniform mass comparison.** For a fixed-domain density r(v)=integral exp(-S(u,v)) du with two differentiations under the integral justified (for example a compact domain and a C^2 integrand), differentiating numerator and denominator gives

    (-log r)'' = E[S_vv] - Var(S_v).

For r(v)=exp[-t(v-a)^2/2]+exp[-t(v+a)^2/2], direct factorization gives (-log r)''(0)=t-t^2 a^2. Thus branchwise curvature does not control the full mixture. Conditioning on a branch is legitimate, but averaging conditional estimates is useful only if the estimates hold on every branch being averaged, or the exceptional branch masses are paid. This calculation uses no assertion that these two wells are an actual Wilson fibre.

## 2. Hardest test: what a sparse exclusion can and cannot prove

**Discharged — displacement, in a coherent commuting chart.** Let N line logarithms have mean a_H on r deleted lines and mean a_R on the N-r survivors, with q=r/N<1/2. Then

    a_0=(1-q)a_R+q a_H,       a_h=a_R,
    a_h-a_0=q(a_R-a_H).                                      (2.1)

If |a_R-a_H|<=C T, the displacement is at most CqT, not zero. This is a statement about a fixed common logarithm chart. It does not establish such a chart on every hull, nor equate an open bond angle with the gauge-invariant cell flux used by the label.

**Discharged — a crossing is not a mass counterexample.** In the scalar formula choose a_R=s+q d/2 and a_H=a_R-d with d>0. Then a_0=s-q d/2<s<a_h. The construction shows why no deterministic threshold-preservation statement follows from a small displacement. It does not specify lattice plaquettes, a regular top, a conditional reference measure, or an action minimum. Accordingly it is not an admissible counterexample to rarity. The gate's private-face-bond variation realizes a nonzero map displacement; it likewise supplies no non-exponential conditional mass at a parent threshold.

**Implication — an explicit commuting lattice crossing on a specified sparse face geometry.** This strengthens the scalar test without claiming its mass. Take odd L and a face between B(0) and B(L e_1). There are L^3 crossing bonds, one per transverse column; each is read by L of the N=L^4 starting lines of that parent and no other parent's straight segment. Internal block contours read none of these bonds. Take a singleton labelled cell h at a transverse edge of this face, with its prescribed sparse hull. Suppose this hull removes k complete face columns, including that edge column, with 8<=k<L^3/2, and causes no Haar parent. These are explicit geometric admission conditions on the actual hull, not a newly chosen hull; the spanning/pocket convention has not been proved here. They hold for the elementary bounded cubical collar geometry when L is large. Set q=k/L^3.

Choose 0<beta<T with 0<chi(T+beta)<1, possible by continuity between the cutoff endpoints. Set d=T/4 and

    D=d-(d+beta)/k > 0,       v=T+qD/2.

Make the crossing-bond angles equal to v on surviving columns, v-d on all deleted columns except the chosen edge column, and v+beta on that column. All other fine bonds are identity. Choose L large enough that chi(v+beta)<1 and v+beta<2T; continuity at T+beta permits this since the fixed hull has q tending to zero. Each fine plaquette sees either one such angle or a difference of two, so all fine fluxes are <2T. The cell h sees a plaquette of angle v+beta>T against a zero crossing bond outside the face, hence its label has positive weight. Every other cell can have label zero with positive weight. Thus this pattern has positive auxiliary weight on a neighbourhood, not merely at one configuration.

The deleted-column average is v-D. All block contours are identity, including rerouted contours that stay within their blocks. Therefore the two parent fields have just one nonidentity bond, with respective angles

    M_0: v-qD=T-qD/2,       M_h: v=T+qD/2.                (2.1a)

Every incident parent plaquette crosses T. Take all level-1 labels zero, again of positive weight since v<2T. At the next unlabelled step the contour term is a coarse gradient in this commuting chart. A single input bond enters each straight-path average with coefficient at most L/L^4=L^(-3); summing the four sides bounds each level-2 plaquette by 4v/L^3<T_2 for large L. This is the hand path-count proof of regularity of the top; no numerical Fourier calculation is used. All products remain on the small logarithm branch by taking the stipulated small T.

This gives a regular-top crossing whenever the stated singleton-hull geometry is admitted. It still does **not** give a non-rare conditional event under the Wilson history law: fine fields on a whole face were prescribed, and their action and conditional mass were not compared with the full denominator. Indeed the h plaquette alone has action at least 1-cos T>=T^2/4 for T<=1, obtained from the elementary sine bound used in Section 6. Conditioning on all these fine fields would discard precisely that expense. I have not promoted this construction into a full-law counterexample.

**Discharged — the exact margin alternative.** Suppose on a specified supported branch a comparison parent V^0 and the actual retained-line parent V^h have cell fluxes f_0,f_h with |f_h-f_0|<=delta. For any threshold s and 0<=delta<s,

    {f_h>s} subset {f_0>s-delta}.                           (2.2)

This follows from f_0>=f_h-delta. Hence for a sparse set H and disjoint tested patches,

    {all f_h(c)>s, H sparse} subset
    {all f_0(c)>s-delta_c(H), H sparse}.                    (2.3)

No independence is used. Taking delta_c<=eta s with eta<1 replaces the needed threshold by (1-eta)s. It does not bound the probability of that lower-threshold event. The bound CT r/N on bond averages still needs a common-frame, four-side plaquette comparison before it supplies delta_c in (2.3).

**Gap — current crux.** A nonzero displacement is established. A Wilson configuration with the required non-rare *full-law* mass is not established. The outstanding question is whether the lowered-threshold event in (2.3), with all retained-hole fields integrated against their correct weights, has a positive own-level rate. Subsequent sections separate the elementary accounting from that missing Wilson comparison.

## 3. Margin, charging and the genuinely joint alternative

**Discharged — a sharp diagnostic for conditional claims, not a Wilson counterexample.** On [-a,a] give u density proportional to exp(-x u^2/2), with a>delta>0. Set f_0=s-delta/2+u and f_h=f_0+delta. Symmetry gives

    P(f_h>s) >= P(u>=0)=1/2.                               (3.1)

For any nondecreasing label weight chi with chi(s+delta/2)>0, E chi(f_h)>=chi(s+delta/2)/2. Thus a smooth label at a fixed, coupling-independent threshold does not cure a minimum displaced past that threshold. A fixed positive label weight has zero exponential rate: -log chi(s+delta/2)/x tends to zero. This example supplies exactly the missing energetic test, but is not a lattice construction or a refutation of either consumer. In particular choosing a parent value close to T and then conditioning on that very value is not a legitimate test of its rarity.

**Implication — a margin that would suffice, with an explicit gain.** Consider n fixed boxes in one supplied conditional chart, with coordinates u=(u_1,...,u_n), u_i in R^{d_i}, d_i<=d_0. All constants in this paragraph are independent of n,x and the retained data. Suppose the actual action on the *whole numerator domain* satisfies

    A(u)-A(0) >= (a/2) sum_i |u_i|^2,                       (3.2)
    |D_{u_i} R| <= b(x):=sqrt(d_0)(C_0+C_1 x epsilon),
    F=xA+R,       epsilon=exp(-mu d).

Suppose a comparison flux obeys f_i(0)<=T/4 and |f_i(u)-f_i(0)|<=L_f |u_i|, and the retained-hole displacement is at most eta T with eta<=1/4. An actual flux above T forces |u_i|>=vT with v=(3/4-eta)/L_f>=1/(2L_f). The same argument applies to any Lipschitz deviation test with a specified positive reference margin; this does not identify it with the consumer's Dev without checking that identification.

Integrate DR along the segment, and use br<=a x r^2/4+b^2/(a x). On the event that all n marks occur,

    F(u)-F(0) >= (a x/4) sum_i |u_i|^2 - n b(x)^2/(a x).

Choose epsilon<=a v T/(8 sqrt(d_0) C_1) when C_1>0, and x>=8 sqrt(d_0) C_0/(a v T). Then b(x)<=a v T x/4 and

    F(u)-F(0) >= (3a v^2/16) n x T^2
                >= g n x T^2,       g:=a v^2/8.             (3.3)

This is a joint gain, not one gain minus the dimension of a growing cluster. It is proved only under the displayed chart, reference-margin and derivative hypotheses. The margin is measured before the possible displacement, so a point arbitrarily close to the original threshold is still paid. S1 does not currently provide these hypotheses uniformly in its retained holes or its site conditioning.

**Implication — charging a displacement without spending a hole twice.** Suppose a label-change comparison loses at most Lambda T sum_c delta_c in the leading action, and delta_c<=C T sum_{h in H} q_{ch}, q_{ch}>=0. Suppose further that each hole has a *reserved* gain b_h x T^2, b_h>=b_*>0, and

    sup_h sum_c q_{ch} <= epsilon_H,
    Lambda C epsilon_H <= b_*/2.                           (3.4)

Changing the order of the two finite sums and multiplying by x bounds the total loss in F by (b_*/2) x T^2 |H|, leaving half of each hole's reserved gain. A quadratic action loss K sum_c delta_c^2/2 can be included if sum_h q_{ch}<=q_*: it is at most (K C^2 q_*/2) T^2 sum_{c,h}q_{ch}. Replace Lambda C in (3.4) by Lambda C+K C^2 q_*/2. These are explicit sufficient constants. A displacement bound for one parent alone gives neither the column sum in (3.4) nor the reserved joint gain. Charging one already-paid hole to arbitrarily many ancestors would invalidate this argument.

**Implication — exhaustive one-step split and exactly where m_* comes from.** Fix n test locations with disjoint full child read boxes B_i, each containing at most N_0 candidate children. There are two cases for each location: every input block is sparse, or some input block contains at least m=m_* distinct labelled children. The sparse case includes *all* near-threshold exits, via (2.2); they cannot be discarded. In the dense case choose m of those children by a fixed ordering; at most

    C_L:=binom(N_0,m)

witness sets need be considered (use C_L=0 if N_0<m). A separate Haar-by-line-loss case disappears only after proving that sparse hulls leave at least half the lines. For cubes of side at most S, one cube intersects at most 2L(S+2)^3 of N=L^4 straight lines: there are at most (S+2)^3 transverse columns and at most 2L possible longitudinal starts in the two read blocks. Thus h such cubes delete a fraction at most 2h(S+2)^3/L^3. This proves the needed half-line bound if that fraction is <1/2 and the actual hull is covered by those cubes. The bounded cube cover, rerouted contours and pocket/spanning-chain rule remain geometric hypotheses; I do not assert that counting core cells alone supplies them.

For a subset D of dense test locations and chosen witness union H_D, the sufficient *mixed* inequality is

    P(all sparse exits at i outside D,
      all children in H_D labelled)
       <= z_k^(n-|D|) p_{k-1}^|H_D|.                       (3.5)

The law here is the original regular-top law, or mu as applicable; unchosen holes remain integrated. Disjoint read boxes give |H_D|=m|D|. Summing witness choices and then D gives the exact bound

    P(all n exits) <= (z_k+C_L p_{k-1}^m)^n.              (3.6)

For n=1 this is a probability bound of the form (4.1). If odds are required, a bound q<=r<1 gives odds<=r/(1-r); for r<=1/2 this costs at most two, which can be absorbed by reducing the exponential rate and increasing x_*. Marginal one-hole estimates do not prove (3.5). Nor does (3.6) prove the multilevel consumer when witnesses at different levels overlap. The common integral comparison in Section 4 is a way of proving such mixed bounds *if its Wilson hypotheses can be established*. Those hypotheses, and bounded reuse across levels, are gaps.

**Discharged — closing the scalar arithmetic once the probabilistic premise exists.** For p_k<=exp(-a_1 x_k)+C_L p_{k-1}^m, p_0<=2exp(-a_1x_0), m>=2 and x_{k-1}>=x_k-b, the induction p_k<=2exp(-a_1x_k) holds whenever

    C_L 2^m exp(a_1 m b) exp[-a_1(m-1)x_*] <= 1.

Substitution proves this directly. It establishes no premise of (3.5).

## 4. Fixed boxes: product denominator and both entropy corrections

**Implication — exact integral lemma with additive constants.** Fix outside data sigma on a compatible fibre. Let n be the number of paid boxes, each of bounded geometry. Suppose the entire marked numerator is covered by at most s_0^n coordinate pieces, each of dimension at most d_0 n and contained in [-R,R]^{d_0 n} in the sense that every actual coordinate is in [-R,R], R>=1. Its reference density (including whatever label weights and constraint Jacobians have not been put in F) is at most J_+^n. Suppose every piece satisfies

    F(u) >= F_ref + g n x T^2 - b_0 n.                    (4.1)

In the *same* full conditional denominator suppose there is an injective chart

    Phi_sigma : product_{i=1}^n [-r_0,r_0]^{e_i}
                              --> the same top/exterior fibre,
    1<=e_i<=d_0,

with density at least J_-^n>0 and a single reference value F_ref, and on

    D_x:=Phi_sigma(product_i [-x^(-1/2),x^(-1/2)]^{e_i})

one has F<=F_ref+n(A_0+A_1 sqrt(x)). Require x>=max(1,r_0^(-2)). These are hypotheses on one jointly admissible chart, not an assertion that separate hard fibres form a product. All denominator labels, constraints and Haar coordinates must be the actual ones.

The common denominator is explicitly

    Z_sigma >= integral_{D_x} exp(-F) dm
       >= exp[-F_ref-n(A_0+A_1 sqrt(x))]
          J_-^n (2/sqrt(x))^(sum_i e_i).                  (4.2)

The numerator is at most s_0^n J_+^n (2R)^{d_0 n} exp[-F_ref-g n x T^2+b_0 n]. Since sum_i e_i<=d_0n, division yields

    log P_sigma(all marks)
       <= n[-g xT^2 + K_0+A_1 sqrt(x)+(d_0/2)log x],     (4.3)
    K_0:=b_0+A_0+log s_0+max(0,log(J_+/J_-))
                                    +d_0 log(2R).

Take b_0,A_0,A_1>=0, s_0>=1. From log x=integral_1^x du/u<=2sqrt(x) for x>=1, put K_1=A_1+d_0. For

    x>=max{1,r_0^(-2),4K_0/(gT^2),[4K_1/(gT^2)]^2},

the last two costs in (4.3) total at most g xT^2/2. Therefore the probability is at most exp[-(g/2)n xT^2]. There is no n log n term. The former uncharged C times cluster dimension is replaced by a fixed cost per paid box, absorbed by that box's gain. Growing n never changes x_*.

**Discharged — fixed-range overlap costs only a fixed fraction at one level.** If the chosen boxes overlap, suppose their intersection graph has degree at most D_0, independent of volume and x. Order the boxes and assign each the first colour unused by its already-coloured neighbours. At most D_0 colours are forbidden, so D_0+1 suffice. One colour contains at least n/(D_0+1) requested marks and has disjoint boxes. The event that all n marks occur is contained in the event for that colour. A proved disjoint-box bound with rate a therefore gives rate a/(D_0+1) per original mark. For nonidentical rates select the colour with largest sum of rates. This selection depends only on prescribed marks, not on the fields. It removes the need to grow one box around a connected cluster; it does not construct the common conditional chart. In particular a chart whose free dimension grows with the OS collar d_x proportional to log x is not a fixed-box chart and does not satisfy the hypotheses used here.

**Implication — denominator oscillation from first derivatives, no marginal convexity assertion.** On the displayed joint chart suppose A has upper Hessian C_A I, DR has each coordinate bounded by C_0+C_1x epsilon, and 0 is an interior minimum of F=xA+R. Taylor's formula and x DA(0)=-DR(0) give

    F(h)-F(0) <= (C_A x/2)|h|^2
                       +2(C_0+C_1x epsilon)|h|_1.

On D_x this is at most n[d_0 C_A/2+2d_0 C_0/sqrt(x)+2d_0 C_1 epsilon sqrt(x)]. Thus (4.2) may use A_0=d_0 C_A/2+2d_0 C_0 and A_1=2d_0 C_1 epsilon for x>=1. If the centre is stationary for A instead, omit the factor two in the remainder term. This is a written fixed-box repair of the entropy calculation. It does not construct the chart, its reference minimum or its positive density. For different label branches these comparisons must share F_ref and must include their branch measures; an upper RANK bound supplies no J_-.

**Discharged — repair of S3(a), by normalized integration.** Let H include retained patterns and their field data, with their actual common disintegration. Write Z(H) for their unmarked inner mass and Z_E(H) for the marked mass in that same space. If Z_E(H)<=z^n Z(H) for almost every H, then

    [integral Z_E(H) dnu(H)]/[integral Z(H) dnu(H)]<=z^n.   (4.4)

This is multiplication and integration of a nonnegative inequality, not label independence. If changing a label also changes constraints, the augmented space must be used to supply this common disintegration; it cannot be inferred by matching formal delta symbols.

If one instead has only product-odds bounds, the correct pattern sum is (1+p)^N<=exp(Np), from log(1+p)<=p. The exact condition for (1+p)^N<=2 is N log(1+p)<=log 2; Np<=log 2 is a sufficient condition. Neither size restriction is supplied in S3(a). On fixed boxes with N<=N_0 n the cost is at most exp(N_0 p n), another per-mark cost in (4.3). Remote unmarked boxes must stay in (4.4), not in this absolute sum. This repairs the arithmetic without silently allowing volume-dependent constants.

## 5. Exact S1 statements still needed, including label changes

**Gap — conditional chart and minimum statement (C-S1).** For the chosen fixed box P, regular parents on its read enlargement, and every compatible retained-hole/exterior datum sigma that is actually exposed, construct the disintegration of the augmented history on P. Supply a class reference U_sigma, a fixed-size free-coordinate chart and its jointly admissible products on disjoint boxes. The following are the required quantitative assertions, not conclusions of the word "class":

1. The reference lies in the same top/exterior fibre and in the interior of its denominator support; its new labels have positive weights there. The complete pulled-back measure has the lower density J_- of (4.2), on a cube of radius r_0 independent of x, volume, depth and sigma. The corresponding numerator cover has the bounds s_0,d_0,R,J_+ in Section 4, or a relative integral substitute with those same per-mark costs.
2. The free chart is a single specified logarithm/gauge branch on the entire segments used in (3.2) and (4.2). The reference is an actual stationary conditional minimum, and its consumer deviation from Lift_b is at most eps_q T/2 in the square-root Dev norm. For the flux-margin argument its comparison flux is at most T/4. These are different tests; whichever is used must be verified in the actual frame.
3. For F_sigma=-log of the *actual conditional inner density*, identify the leading action and prove the lower comparison (3.2) on each class numerator piece, the derivative bound on R, and the upper Hessian bound on A on the denominator chart. For pieces outside that chart prove (4.1) directly, including S2's partial child integral and any S3 tower/sector branches. Calling the field class on the unfrozen bonds supplies none of these comparisons at their holes.

Together these precise assertions would yield S1's integral estimate by Sections 3–4. They are not supplied in the pinned source. In particular, the local OS formula at mapped 636–660 defines a particular Omega and needs clearance for the outer measure to be independent of the varied parent. Its inner estimates use a gas with a rarity input. Arbitrary conditioning on S1's lower site data is not that construction. A useful admission test is measurability: if the exposed lower fields and labels already determine the tested parent's full read support, its event has conditional probability zero or one. It cannot then satisfy a uniform strictly positive exponential penalty on the event-one data. This is a conditional-probability identity, not a claim that the specified sparse example has such data. The proof must either exclude that exposure or keep those data integrated and compare their mass.

**Implication — the needed multiplier theorem in a form that actually proves the loss.** Work in one fixed parent coordinate chart: w+Delta is coordinate addition, and lambda is dual to those coordinates. For a fixed all-zero local map M_0 and the same exterior, let U(w) be a continuously differentiable path of admitted *global fibre minima*, M_0(U(w))=w, with

    DA(U(w))=DM_0(U(w))^* lambda(w),
    |lambda(w)|_infinity<=Lambda T,
    |lambda(w+t Delta)-lambda(w)|_infinity
                                    <=K t |Delta|_infinity.

Differentiating m(w)=A(U(w)) along w+t Delta gives m'(t)=<lambda(w+t Delta),Delta>. Integration proves

    |m(w+Delta)-m(w)|
       <=Lambda T |Delta|_1+(K/2)|Delta|_infinity |Delta|_1.   (5.1)

This proves the asserted minimum comparison from a specifically stated theorem; an inverse fibre Hessian is not that theorem. No uniqueness outside the supplied minimum path is inferred. The source `c0-loc.md` (9.1),(9.7) obtains a multiplier bound only with smooth class chains, actual stationarity, local curvature and a supported unit-row lift; its admission boundary excludes rough rerouted constraints. It does not supply this path across the changing label fibres, nor the conversion to the constants Lambda,K required here.

**Gap — signed label-change comparison (L-S1).** For each labelled numerator field U with n paid marks, one needs a same-exterior representative U^nat in an admitted M_0 fibre, M_0(U^nat)=w+Delta, such that a *signed marked excess* is retained. A sufficient explicit statement is

    A(U) >= m(w+Delta)+g_0 n T^2-L_fill,
    L_fill+Lambda T |Delta|_1
           +(K/2)|Delta|_infinity |Delta|_1
                                     <=(g_0/2)n T^2.        (5.2)

Then (5.1) gives A(U)-m(w)>=(g_0/2)nT^2. The label/coarea part must also obey Section 4's density comparison, or its direct integrated counterpart. Merely constructing a class fill gives neither the first inequality of (5.2) nor a positive marked excess. Even A(U)>=A(U^nat)>=m(w+Delta), without that excess, proves only a lower bound with a *negative* loss against m(w); it does not price the mark.

For the sparse displacement, (3.4) is a sufficient summed bound for the linear and quadratic terms in (5.2), provided the joint reserved hole energy exists. The common chart, the signed fill/excess and the summed influence estimate are separate missing statements. They are not replaced by declaring the hole exterior or by an upper parent-window volume bound.

**Gap — remaining coverage of S2–S4.** No argument here asserts that a fibre lift estimate bounds every child in a fibre, that the descent length is independent of a cluster's diameter, or that a sector-changing competitor with the same parents exists. S3(c)'s use of PER would require globally class copies with controlled seam energy and a value increment uniform in the actual retained holes. Mapped MD 666–680 supplies its decomposition only after excluding insufficient regular crossings, using rarity. It is not the pointwise arbitrary-hole input used in S3(c). The full-law comparison of those branches, the mixed bound (3.5), and the terminal base under mu remain unpaid. This is why the conditional repairs above do not constitute repaired S1–S4.

## 6. RANK: corrected differential and a proved local replacement

**Discharged — the logarithm estimate with constants.** Identify su(2) with imaginary quaternions: v^2=-|v|^2, so the even and odd terms of the exponential series give exp(v)=cos|v|+(sin|v|/|v|)v. Differentiating in the radial direction gives eigenvalue one for the trivialized exponential derivative. On the transverse plane at v=theta n, multiplication by exp(-v) makes that derivative (sin theta/theta) times a rotation through angle theta. Its inverse is

    Dlog=theta cot(theta) I +/- theta J,       J^2=-I.

Consequently ||Dlog-I||=sqrt((theta cot(theta)-1)^2+theta^2)>=theta. The asserted 1/4 bound at theta=1/2 is false.

For 0<=theta<=1/2, integrate cos s>=1-s^2/2 to get sin theta>=theta-theta^3/6. Also

    sin theta-theta cos theta=integral_0^theta s sin s ds
                                           <=theta^3/3.

Here sin s<=s follows by integrating cos s<=1; cos s>=1-s^2/2 follows by integrating sin s<=s. Therefore

    0<=1-theta cot theta<=8theta^2/23,
    ||Dlog-I||<=theta+8theta^2/23<=2theta.                  (6.1)

The transverse exponential derivative differs from the identity by at most theta+theta^2/6<=2theta, using |exp(theta J)-I|=2sin(theta/2)<=theta and |sin theta/theta-1|<=theta^2/6. Thus also

    ||dexp_xi-I||<=2|xi|,       |xi|<=1/2.                 (6.2)

These formulas include the dexp factor omitted when the varied bond is written exp(xi)g_0.

**Implication — local row volume bound, with its entire support hypothesis visible.** Suppose on the whole convex ball |xi|<=1/64 a row really has the coherent formula

    Phi(xi)=N^(-1) sum_x log ell_x(xi),
    ell_x(xi)=A_x exp(xi)g_0 B_x

for its s varying lines, the others constant. Suppose every read logarithm has angle <=1/64 there, and ||Ad(A_x)-R||<=1/32 for a *single fixed* rotation R. Equations (6.1)–(6.2), with the product rule, give

    ||D Phi-(s/N)R|| <= (s/N)[(33/32)^3-1] < s/(8N),

because 33^3-32^3=3169<4096=32^3/8. Integrating along the segment from xi to eta proves

    |Phi(xi)-Phi(eta)| >= (7s/(8N)) |xi-eta|.             (6.3)

Thus Phi is injective on the entire ball and its Jacobian is at least (7s/(8N))^3. This proof would not work with derivative control on a disconnected set K alone.

In exponential coordinates normalized Haar density is (sin r/r)^2/(2pi^2): parameterizing a unit quaternion as (cos r,n sin r) gives metric dr^2+sin^2 r dn^2, hence angular area 4pi sin^2 r, and integral_0^pi sin^2 r dr=pi/2. Left multiplication is orthogonal in these four real coordinates, so this normalized volume is Haar. On r<=1/2 its coordinate density lies between (23/24)^2/(2pi^2) and 1/(2pi^2). Change of variables in (6.3) therefore bounds the measure of the preimage of any group ball B_epsilon(W) by

    (24/23)^2 (8N/(7s))^3 Haar(B_epsilon)
                               <=4(N/s)^3 h(epsilon).      (6.4)

Restriction to a smaller measurable K only lowers this one-row numerator. For several private bonds, a product follows if, after fixing all nonprivate bonds, each row's entire relevant preimage is covered by at most J such charts, independently of the other private coordinates. Privacy then makes each row-window event a function of its own coordinate alone. Drop 1_K, integrate this product of row indicators against product Haar, and apply (6.4) to each factor, with 4J replacing 4. This is a proved analytic implication, not a global sheet-count theorem. Merely bounding the sections of 1_K does not justify multiplication: on [0,1]^2 the set |u-v|<epsilon has each section of length at most 2epsilon but area 2epsilon-epsilon^2, not at most 4epsilon^2 for small epsilon. Thus the chart coverage must control the complete row preimages, not just K-sections depending on the other private bonds.

**Gap — what RANK still needs beyond its repaired constant.** The actual block link uses relative loops and a reference path. That path's derivative must either vanish for the chosen private variable or be included in D Phi. RANK needs the above common-chart bounds on every relevant sheet and a uniform sheet count. Nearness of open paths to each other and smallness of exp(mean principal log) do not supply them: exp((pi-delta)tau) and exp(-(pi-delta)tau) are close in SU(2) but their principal logs cancel at zero. Neither (JW) nor S1's lower denominator density is established by (6.4). The smaller WRONG differential claim is corrected; the global admission problem is explicitly left open.

## 7. A strictly smaller inequality at which this attempt stops

**Unchecked — fixed test, with every reduction specified.** Fix the geometric constants and an admitted odd L once. Work at depth exactly two, on one fixed torus whose side is Q L^2 in fine units. Choose the even integer Q larger than 100 times the sum of 1 and all the brick, lift and hull read widths in Theta, so no read patch used here wraps. There is no volume or depth limit in this test. Fix one fine cell h near a block face and one level-1 plaquette c incident to that face's parent, as in Section 2. Use the actual kernel, including its hull convention; do not replace it by a chosen cube hull. Fix the following event E_h in the augmented two-step history:

- Exactly h is labelled at level 0; all fine plaquette fluxes are <2T. Every parent is non-Haar and both the all-lines and retained-line maps are on their coherent small relative-log branches.
- At level 1 every plaquette has flux <2T, and every outgoing label is zero.
- For this one plaquette c,

      f_c(M_0 U)<=T<T_c^h:=f_c(M_h U)<9T/8.

  In addition, its containing test cell is non-quiet by the consumer's actual predicate. This last clause avoids using an unproved lift identification to identify a flux event with Dev. Under the stated lift bound flux(Lift)<=T/4 and eps_q<=1/4, it is automatic: the reverse triangle inequality gives a plaquette deviation >3T/4.

All other fields are integrated even in this restricted numerator. In the denominator impose **none** of these label, class or mark restrictions.

For definiteness, restrict top centres to the following one-parameter family, rather than every regular field. Let W_* be the level-2 field of the admitted face construction (2.1a), taking L large enough that its flux is <=T_2/4. Fix one top bond b_* and the same commuting generator tau. Set W(w)(b_*)=exp(w tau)W_*(b_*), leave all other top bonds unchanged, and let 0<=w<=T_2/4. A plaquette contains b_* at most once, so its angle changes by at most w. Thus W(w) has flux <=T_2/2. Use the fixed positive window radius epsilon=T/100 and

    B_w={dist(V_2(b),W(w)(b))<epsilon for every top bond b}.

Multiplying four links and applying the triangle inequality shows every top in B_w has flux <=T_2/2+4epsilon<T_2. These are regular-top mixtures. The test can equally be posed with any fixed admissible sparse core in place of the singleton; the singleton is the present narrowed choice. If the literal singleton hull fails the geometric admission in Section 2, that admission must first be settled; it is not justified by a row calculation. Empty numerator windows below are harmless and are omitted.

**Gap — one scalar variational inequality (SP).** With the coupling-independent two-step base measure nu of Section 1, define

    a_all(w)=ess inf_{B_w} A(U),
    a_exit(w)=ess inf_{B_w intersect E_h} A(U),

and take the infimum only over windows with nu(B_w intersect E_h)>0. The essential infima use the restrictions of the *same* nu; this avoids counting isolated zero-mass configurations as minima. The next proposed task is the single inequality

    Delta_sp := inf_w [a_exit(w)-a_all(w)] > 0.             (SP)

If the entire indexed numerator is empty, there is no sparse crossing in this test and (SP) is vacuous; it must not be reported as an energetic result. The face construction gives a positive-weight geometric crossing when admitted, but I have not used it as a comparison of these infima. The actual non-quiet predicate and all required hull admission conditions are retained in E_h.

**Discharged — why (SP) is smaller and uses the correct denominator.** For any nonzero finite restricted base measure eta, let a=ess inf A. For every delta>0 the set A<a+delta has positive eta-mass b_delta. Hence

    b_delta exp[-t(a+delta)]
       <= integral exp(-tA) d eta <= eta(total) exp(-ta).

Taking logarithms, dividing by -t and then sending t to infinity and delta to zero proves the limit a. Applied to the two restrictions above, this gives

    lim_{t->infinity} -t^(-1) log P_t(E_h | B_w)
                                      =a_exit(w)-a_all(w).  (7.1)

Consequently the repaired S1–S4 proposal, if valid at all sufficiently large couplings as printed, with a positive uniform one-mark rate and the bounded-step relation x_1=t+O(1), would imply (SP), indeed Delta_sp>=a_mark T^2 for some a_mark>0. The regular-top bound passes to B_w by integrating against the *Wilson* top marginal, not by pretending it is Haar. E_h is a subset of a single actual non-quiet event, so the full numerator bound applies. This large-coupling test is for that uniformly stated proposal; an assertion on one fixed terminal window alone does not justify the limit in (7.1).

Unlike the original item, (SP) has one fixed volume, two steps, one mark, one sparse core, no rough intermediate fields above 2T, no unbounded exteriors, and only a one-parameter set of top windows. It asks only for positive separation of two essential action infima. It asks for no finite-coupling fluctuation estimate, no uniform relative entropy, no product over marks, no tower accounting and no terminal mu estimate. Even its numerator fixes one special label branch; the denominator retains *all* branches. It is therefore a necessary subproblem of the proposed full-law repair, not (SEP) and not uniform rarity after conditioning on H. Positivity in (SP) cannot control omitted marked branches or supply their fluctuation factors. For a purely logical check already at one window, take three unit-mass atoms: an unmarked atom of action 0, the restricted marked event E consisting of one atom of action 1, and another marked atom of action 0 outside E. The restricted essential gap is 1, whereas the full marked probability is (1+exp(-t))/(2+exp(-t))>=1/2. This is a finite-measure separation of implications, not a Wilson counterexample.

**Unchecked — expectation and failure mode.** I expect (SP) to be true on this narrowed class, after the stated large-L choices. The reason is that the hole requires fine flux at least T, while the intended stationary lift of a regular top has a strict flux margin below T; removing a fixed number of face columns changes a normalized constraint by a fraction of order L^(-3). This suggests that a local signed repair could recover a fixed part of the hole/exit cost while paying the mean correction. That is a heuristic based on the displayed scales, not a remembered theorem or a proved estimate. The reason for caution is precise: a minimum in the excluded-line fibre can differ from the all-lines minimum. Without (5.2), small movement of the constraint need not leave a positive *difference* after subtracting the complete denominator's action. Neither absolute rough-cell energy nor class Hessian positivity decides this difference.

**Gap — disposition.** I have no admitted configuration with a proved non-exponential full-law conditional mass, and no proof of (SP) with its actual constraint measure. I therefore cannot supply the requested full S1–S4 proof. The usable repairs are the margin/charging algebra, the joint alternative conditional on (3.5), the common fixed-box denominator with explicit constants, normalized hole summation and the local Dlog/RANK correction. Their Wilson admission and signed-excess inputs remain gaps. The next decisive calculation is (SP), rather than another cluster counting argument.

## 8. Source boundary and recovery checkpoint

**Discharged — read boundary.** In addition to the three required full/ranged sources, supporting reads were confined to these allowed passages: mapped Text 3.1 (376–402), density and coordinates through the kernel (562–624), local OS and the relevant MD construction (636–688); QB 15–31 for quiet and the local lift; RD 325–371 for the stated exclusion geometry and its still-unrebuilt deformation step; `one-window.md` 41–103 for the one-link comparison and its scope; `c0-loc.md` 186–210, 910–934, 995–1071 and 1185–1266 for relative loops, stationarity, multipliers and admission; upper-chain interface statements around 176–190, particularly the two rarity clauses at 182–183. Bounded location searches in those files were not treated as proof. Some tool outputs were truncated; required full-source text and decisive passages were retrieved again in smaller ranges. Numerical claims printed in those sources were not used to discharge anything.

**Discharged — firewall and edits.** No forbidden independent-side file or gate, excluded library file, strategy/history-budget/compute-inventory gate, outside proof account or external literature was opened. References to such material inside allowed files were not followed. No source theorem is granted status by its author's label. No editable prompt, source argument or other repository file was changed; only `library/rarity-repair.md` was written. No commit, push, PR, post, audit or subagent was made.

**Gap — current checkpoint at the pinned source.** Open: literal sparse-hull/chart admission; the essential-action gap (SP); C-S1's actual conditional chart and positive common measure; L-S1's signed excess and multiplier path; mixed joint payment and multilevel reuse; the separate terminal mu base. Failed routes retained: zero influence of excluded lines; a fixed smooth cutoff as an exponential price; one Euclidean ball on an arbitrary cluster; (1+p)^N<=2 without any size control; deriving a positive excess from a minimum-continuity loss; and extending branch curvature to the full mixture. The narrowed next decision is whether (SP) has strictly positive separation on its nonempty supports. No other queue item has been taken.

STOPPED
