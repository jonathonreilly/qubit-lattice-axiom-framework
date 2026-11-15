# PRE-STATED — hostile review of THETAW.md

UTC pre-statement: 2026-10-28 22:02:07 UTC. Written before reading the target, its checks, or deriving its inequalities.

Scope: independently test the claim that splitting the exponent jobs makes the stated Yang–Mills target satisfiable. Only this deliverable will be written. No git commands, snapshots, audit ledgers, numerical libraries, or long jobs will be used.

Targets and pre-stated refutation criteria:

1. Reconstruct all six jobs from the consuming formulas. A forced equality or a missing coupling invalidates the claimed independent parameter region.
2. Test whether the vertex estimate actually consumes two potential factors and whether BFT-1 supplies their bound. Distinguish a missing hypothesis from a merely renamed one.
3. Derive the curvature and remainder windows; compare the old ceiling with its alleged replacement. An incompatible surviving bound or an unsupported supersession refutes the advertised region.
4. Derive the weighted absorption condition for a row with decay exponent sigma, including constants, endpoints, scale quantifiers, and the role of alpha. A hidden positive floor or missing summability condition refutes the assertion that any positive sigma suffices.
5. Derive the dimension threshold and the exact meaning of zero slack. Separate proven algebra from conditional or argued analytic ceilings.
6. Inspect tw1-A through tw1-D for inputs that predetermine their conclusions, impossible or vacuous checks, stale symbols, and arithmetic or printed-inequality errors. Rebuild load-bearing arithmetic with exact rational/symbolic reasoning only.

Evidence policy: attach findings to current file:line or exact strings; distinguish CONFIRMED, NOT-VERIFIED, and REFUTED review findings from PROVEN, ARGUED, CONDITIONAL, GAP, and OPEN claims. A finite witness or a script PASS does not establish an analytic premise or an all-scale bound. Source limits and uninspected premises will be explicit. The asserted model-family difference is supplied by the assignment; I cannot independently establish the author's model identity.

Read accounting: the required project workflow is discretionary file 1. The project review skill, if read as required by that workflow, is discretionary file 2. Target evidence is restricted to THETAW.md, checks/tw1_*, NORMS.md section N7, and the specified BFT_A.md ranges. No other scientific source will be silently treated as verified.

# Findings (appended during the review)

## F1 — REFUTED: the SPD weakening substitutes a different distance into its hypothesis

Attachments: THETAW.md:356–373, especially :361–363 and :370; BFT_A.md:830–831. Claim status: GAP for the claimed implication; the actual weaker SPD theorem remains OPEN.

The stated hypothesis controls a row born at l after transport to m by L^{-sigma(m-l)} eta^2. The proposed derivation instead assumes that the row at l has size L^{-sigma(k-l)} eta^2. These are different quantified estimates. Setting m=k bounds the transported top image, not the original row at l.

A scalar majorant countermodel makes the failed implication exact: let a_{m,l}=L^{-sigma(m-l)} eta^2 for l<=m<=k. It satisfies the proposed transport estimate with constant 1. Its weighted size at its birth level is omega_l a_{l,l}=L^{theta(k-l)} eta^2, unbounded for every theta>0. Even if transport starts at m=l+1, the weighted size there is L^{theta(k-l-1)-sigma} eta^2 and is still unbounded. More generally omega_m a_{m,l}=L^{theta(k-l)-(theta+sigma)(m-l)} eta^2. Decay in transport distance cannot supply decay in remaining distance to k.

For the DIFFERENT hypothesis |j_l^c|<=C L^{-sigma(k-l)} eta^2, the weighted sup majorant is indeed bounded when theta<=sigma, including equality. If the hypothesis describes only an upper bound, the word "iff" applies to uniform control over the entire bounded class, not to each individual row (a zero row works for every theta). The corresponding unweighted level sum is <=C eta^2/(L^sigma-1), with levels k-l>=1. None of this proves the asserted implication from BFT_A's (m-l)-decay. A further decomposition/transport estimate is needed before the lane can redirect its main effort on this basis. This is a countermodel to the cited inequality implication, not a constructed Yang–Mills remainder.

## F2 — REFUTED: the supposed irreducible 1/4 rough-current deficit is a stale parameter evaluation

Attachments: THETAW.md:375–383; BFT_A.md:990–998. Claim status: PROVEN for the corrected exponent arithmetic, CONDITIONAL on the displayed response target.

Rebuild the exponent from the norms: if a=||w_l||_own and n=k-l, the F3 size is N=L^{(2+alpha+theta)n}a, while the current coarse size is L^{3n}a. Their ratio is L^{(1-alpha-theta)n}. The adjoint formula at BFT_A:988–990 is a convex interpolation of two neighboring w values times L^{-3l}; at a block-end link it is exactly L^{-3l}w. Multiplying by the fine current conversion L^{3k} therefore gives ||J^c||=||w^c||=L^{(1-alpha-theta)n}N, without an estimate loss. The desired response at :998 is C L^{-alpha n} N. Therefore the improvement needed relative to a plain sup-norm estimate is

    (1-alpha-theta)-(-alpha)=1-theta,

not a universal 1/4+alpha. The exponent 1/4 in the source is evaluated at (alpha,theta)=(1/4,1/2). At that pair the required gain is 1/2. If theta stays 1/2 while alpha tends to zero, the required gain stays 1/2; it does not fall to 1/4.

There is no positive parameter-independent floor: take theta=1-epsilon and alpha=epsilon/2, 0<epsilon<2/3. Then 0<alpha<theta<1 and even theta<=1-alpha holds, while the required gain is epsilon. For example alpha=1/16, theta=7/8 gives image exponent 1/16 and required gain 1/8, below the alleged irreducible 1/4. The infimum is 0, unattained for theta<1. This removes the claimed fixed obstruction; it does not prove the rough-response estimate or control constants as theta tends to 1.

## F3 — REFUTED: the replacement silently restores the known bad level-0 residual weight

Attachments: THETAW.md:569, :587, :615–618; BFT_A.md:524–528 and :398–401. Claim status: GAP in the proposed replacement norm.

The replacement explicitly sets omega_0=1. Its cited consumer explicitly says the residual (R) slot at l=0 must use omega_0=L^{theta k}. At omega_0=1, BFT_A:527 gives a lower bound proportional to L^{alpha(k-1)} minus a k-independent constant, hence divergence for every alpha>0. This is the residual source slot, not the separately normalized plain level-0 current slot (P0); copying a level-0 convention across these slots is a symbol/role collision.

The scale mechanism is elementary: oscillation of fixed coarse amplitude on mesh h=L^{-(k-1)} has Holder quotient proportional to h^{-alpha}; an unweighted residual source allows that fixed amplitude, whereas L^{theta k} in its norm suppresses it by L^{-theta k}. The resulting scale exponent changes from alpha to alpha-theta. This independently explains the endpoint weight in the displayed counterexample; the full inverse construction behind that counterexample has not been re-proved here.

Correction: distinguish omega_0^(R)=L^{theta k} from any omega_0=1 convention for the Wilson/divergence or P0 contribution. At alpha=1/4, theta=1/2, the omitted residual weight is L^{k/2}, not 1. A single indiscriminate omega_0 convention cannot implement the claimed pair.

## F4 — REFUTED: the later window passage retains, rather than removes, the conditional ceiling

Attachments: THETAW.md:188–201, :526–531, :573–574, :681–687; BFT_A.md:396–400, :560–561, :826–834. Claim status: CONDITIONAL for the repaired-slot window; GAP for the claim that it can simply be dropped from the full target.

The source at :826 explicitly supersedes the earlier passage, but :827 explicitly repeats 0<alpha<=theta<=1-alpha and ties it to OPEN conditions W1 and W2. Its sentence "the window is not [dead]" at :833 preserves that window. What is CONFIRMED is narrower: theta<=1-alpha is not among the unconditionally proved linear constraints (:834), and :560–561 calls the repaired-slot use ARGUED. Lack of a proof of a condition does not prove the condition unnecessary for the route that still invokes that slot.

There is also an exact citation/value error: BFT_A:396–397 does not state 1-alpha<=3/4. It states theta<=1-alpha and alpha<=1/2. The 3/4 number appears at :827 only in the example alpha=1/4. With alpha=1/8 the ceiling is 7/8, not 3/4; over alpha>0 its supremum is 1, unattained. The distance 826-396=430 is correct; the characterization of what changed is not.

A region satisfying only 0<alpha<theta<1 is not automatically a region for the repaired rough slot. The example alpha=2/3, theta=3/4 passes the former and violates theta<=1-alpha. Proving a new replacement slot could remove this condition, but that proof is not supplied.

## F5 — REFUTED: R_lin includes sources that violate its own residual cap

Attachments: THETAW.md:265–272, :303–326; BFT_A.md:1549–1552. Claim status: GAP for R_lin as labelled; CONDITIONAL for the corrected residual-source region.

R_lin explicitly includes residual-type sources yet sets theta_w^r=3 with theta<1. C2 in the same target requires theta_w^r<=2+theta whenever that source class is present. These inequalities imply 3<=2+theta<3: the advertised R_lin is empty for its stated class. The distinction is source class, not whether a source arose in a nonlinear calculation: a linear residual forcing already activates the issue.

To see the scale loss, put n=k-1-i and use the source's own/coarse conversion quoted in THETAW:173. The direct residual shift is controlled at size L^{-2n-theta(n+1)}. Multiplying it by the exponent-3 norm gives L^{(1-theta)n-theta}; it cannot be bounded uniformly when theta<1. The data response at BFT_A:1549 instead has size L^{-3n}, which does support exponent 3. Thus the justified data-only exponent is 3; the direct residual-source estimate supplies exponent 2+theta. At theta=1/2 the latter is 5/2 and the formal soft factor is L^{-1/2}, not L^{-1}=1/3 at L=3.

This calculation identifies the missing estimate, not a universal impossibility theorem for every more structured nonlinear row. An upper bound alone does not establish the "and no further" optimality asserted at THETAW:267; a saturating response or lower bound is needed for that ceiling. The full Corollary HX also contains additional BCH rows (:1553–1556), so the strengthened norm must be checked there before the formal rate is promoted.

## F6 — REFUTED: the check record equates an inequality region with its optimal boundary

Attachments: THETAW.md:328–330, :450; checks/tw1_feas.py:100–108; checks/tw1_out.txt:11–18. Claim status: PROVEN for the corrected finite counts.

The script permits 2<tr<=2+theta, not just tr=2+theta. In four dimensions its exponent is 2-tr, which equals -theta only on the cap boundary. Of the 440 points, exactly 55 satisfy that equality and 385 do not. A returned counterexample is

    (alpha,theta,tc,tr,tA)=(1/12,1/6,2,25/12,1),
    exponent=-1/12 != -theta=-1/6.

Independent counting: for theta=j/12, j=2,...,11, there are j-1 alpha choices and j positive residual increments tr-2, yielding sum j(j-1)=440. Exactly one increment per alpha choice saturates the cap, yielding sum(j-1)=55. On that 55-point boundary the exponent range is [-11/12,-1/6], not [-11/12,-1/12]. The latter range correctly describes the larger 440-point inequality region. The data-only count 660=12 sum(j-1) is also correct; only its 55 cap points attain exponent -1.

Execution receipt: extracted only imports, STEP, and function definitions from the original script into memory with Python 3; ran their exact Fraction calculations without the display block or file writes. Counts and the counterexample above were reproduced. The initial launcher name `python` was unavailable (exit 127); the `python3 -B` run exited 0. No floating arithmetic was used by this review.

## F7 — REFUTED: the advertised control sensitivity is not what the controls establish

Attachments: THETAW.md:58–66, :449–475; checks/tw1_criteria.md:36–62; checks/tw1_feas.py:57–109, :140–170. Claim status: PROVEN for the program analysis and mutation results below; NOT-VERIFIED for any analytic premise from these gates.

- **tw1-A:** Its EMPTY result is correct for the encoded system, and it is not a literal always-EMPTY function: the exact same function at d=3 returns four grid witnesses. Algebraically, a common exponent t<=2 gives t+2 min(1,t-1)<=4, which contradicts the strict soft inequality at d=4. This independently proves emptiness without relying on sampling. The script copies the same exponent conditions it claims to check; it does not independently test their derivation from vertices.
- **tw1-B:** A returned exact witness proves satisfiability of the encoded inequalities only. It neither checks SPD/W1, the strengthened inverse, a potential construction, nor m>0. Its finite grid is not a complete decision procedure for the continuous region. Calling it at theta=1/24 returns EMPTY, yet (alpha,theta,tc,tr,tA)=(1/48,1/24,2,49/24,1) satisfies every encoded inequality exactly. Thus the text "EMPTY (no admissible point)" (:113) overstates what enumeration proves. The d=4 default is feasible, so this flaw does not negate its existing witness.
- **tw1-C:** The original returns EMPTY, but it still returns EMPTY with `th_lo_strict=False`, disabling the theta>0 check. Two other contradictions remain: 0<alpha<theta=0; and tr<=2+theta=2 versus tr>2. Consequently this control cannot establish the claimed fact that the explicit theta>0 floor is live. Its emptiness is built into three mutually redundant input restrictions.
- **tw1-D:** EMPTY is algebraically correct: tc<=2 and tA<=1 give tc+2tA<=4<5. Separately, tr<=2+theta<3 and tA<=1 give tr+2tA<5, also contradicting the soft test. In-memory mutations removing either the Wilson predicate or the soft predicate still return EMPTY. D detects some wholesale losses of dimension dependence, but cannot certify each individual exponent count or the curvature ceiling. D' has the same redundancy with tr<=3 and a strict soft inequality.
- **tw1-E/F/G:** E is explicitly reporting only; F prints examples and a prewritten conclusion, and G prints values. None has an assertion or failure verdict. B/B' are also explicitly report-either-way. THETAW:475's claim that E is the one gate that cannot fail is inaccurate. The controls print their outcomes but do not enforce withdrawal via an exception or nonzero exit; a nonzero process result here comes from G's unrelated display defect.

The original definitions were executed and the C/D mutations were made only in memory. Results: A(d=4)=0 witnesses, A(d=3)=4; C original=0 and C without its explicit floor=0; D original=0, D without Wilson=0, D without soft=0. A finite negative search is not a substitute for the algebraic certificates just supplied.

## F8 — REFUTED: the stated universal sigma witness fails at sigma=1 and above

Attachments: THETAW.md:364–373. Claim status: PROVEN for a corrected witness under the DIFFERENT top-distance hypothesis isolated in F1.

The proposed choice alpha=sigma/2, theta=sigma is inadmissible for sigma>=1 because theta<1 is strict. In particular, at the original sigma=1 it sets theta=1, where C_P diverges. If the conditional repaired-slot ceiling theta<=1-alpha is retained, this proposed choice also fails for sigma>2/3. "Sigma>2/3 only widens the room" may describe the available region, but not that particular point.

A valid universal choice is

    theta=min(sigma/2,1/2), alpha=theta/2.

For every sigma>0 it satisfies 0<alpha<theta<1, theta<sigma, and even theta<=1-alpha. It also avoids a weighted-sum endpoint if one is required. This corrects the witness only; it does not repair the m-l to k-l implication in F1. Under the original choice the constants are not finite "for every sigma>0": sigma=1 is already a counterexample.

## F9 — REFUTED: the "one provably empty slot" promotes a power-count upper bound to a lower bound

Attachments: THETAW.md:275–279, :344–347, :533–536; BFT_A.md:538–543 and the correction at :814–817. Claim status: CONDITIONAL for emptiness under the additional remainder power-count premise; GAP for unconditional impossibility of the actual rows.

The later correction says explicitly that the purported two-sided size is only an upper bound, that no lower bound on the remainder rows exists, and that the nonlinear-side obstruction is ARGUED. THETAW quotes that correction at :276–278 but still calls the slot empty for every pair, and later "provably empty."

Re-derivation separates the two sides. For the unrestricted current class, choose aligned constant-mode currents at every level with coarse size c. If theta+alpha-1<=0, their maximum F3 weighted size is <=|c|, while the top residual is (k-1)c/kappa. Hence a uniform linear estimate fails, including equality. This is a genuine obstruction for the full F3 class. On the remainder side, an estimate |j_l^c|<=C eta^2 gives only

    ||j_l||_F3 <= C L^{(theta+alpha-1)(k-l)} eta^2.

When theta+alpha-1>0 this upper bound grows; that is not a lower bound on an actual row. Rows with extra decay, or zero rows, satisfy the same premise and can still be bounded. Thus the displayed estimates do not close a uniform linear-plus-remainder argument, but they do not prove that every actual remainder family fails. The assertion that exactly one source slot is the sole obstruction is also unsupported while the full strengthened inverse and potential inputs remain unchecked.

## F10 — NOT-VERIFIED: the stronger residual norm is not delivered by the cited full inverse theorem

Attachments: THETAW.md:172, :265–272, :322–340, :489–497, :567–568, :615–618; BFT_A.md:1548–1557. Claim status: GAP for the full strengthened estimate; CONDITIONAL for the direct-shift calculation.

The cited source distinguishes r_i(x)=r_i(y)+sigma_i, a data response y, and additional soft BCH rows controlled by Theorem XB. Its conclusion is a Sigma norm with the old residual exponent. THETAW admits it has not checked all these rows (:339–340), but simultaneously lists the whole region as PROVEN (:489) and supplies it to BFT-5. The estimate for the direct shift sigma_i is not the estimate for every part of x.

There is an endpoint issue if the Sigma output of HX is retained. Write delta=theta_w^r-2 and n=k-i. Up to fixed powers of L, the strengthened direct-shift Sigma estimate is

    sum_{n=1}^k L^{-(theta-delta)n} ||s||_R/kappa_-.

It is uniformly summable for delta<theta. At the advertised delta=theta it becomes k||s||_R/kappa_-, not a uniform geometric sum. Thus the pointwise/sup estimate can permit theta_w^r<=2+theta, whereas this Sigma estimate needs theta_w^r<2+theta. One cannot switch between those norms silently. For example theta=1/2, delta=1/4 gives the formal ratio A=L^{-1/4}; choosing delta=theta gives A=L^{-1/2} but loses this Sigma-bound argument.

This is not a finding that all possible strengthened sup-norm proofs fail. It identifies the exact missing choice and proof: specify the residual aggregation, re-establish the inverse on it for every admitted source row, and then apply the vertex count. Until then the formal parameter witness is not a verified feasible norm pair.

## F11 — CONFIRMED (conditional algebra): the curvature/residual split has real content, with sharply limited scope

Attachments: THETAW.md:149–180, :241–288, :396–437; NORMS.md:644–675. Claim status: PROVEN for the algebra below, CONDITIONAL on the supplied decay estimates and caps.

Let c=theta_w^c, r=theta_w^r, a=theta_A and n=k-j. Multiplication of a volume factor L^{dn}, one curvature/residual factor L^{-cn} or L^{-rn}, and two potential factors L^{-an} gives exponents d-c-2a and d-r-2a. The Wilson vertex occurs at one scale, so boundedness requires c+2a>=d. For soft vertices, the geometric series sum_{n=1}^k L^{(d-r-2a)n} is uniformly bounded exactly when r+2a>d; equality produces k terms of size 1. The additional fixed factor L^r in NORMS:651 does not affect that criterion.

At d=4, c<=2 and a<=1 force c=2 and a=1 if c+2a>=4. Then r>2 is necessary for this geometric majorant. A common exponent c=r<=2 cannot work. Separate exponents can: c=2, a=1, r=5/2, theta=1/2, alpha=1/4 is an exact witness for the reduced inequalities (including alpha<=theta<=1-alpha). No algebra in these vertices forces c=r=theta. The shared letter was not itself a mathematical equality. However r is coupled to the source class and source weight (F5/F10), and a depends on the gauge/potential construction. "Different variables cannot clash" is false as a general inference and fails for the labelled R_lin.

The dimension calculation is equally exact for these capped inequalities: c+2a<=4, so d>=5 is impossible; at d=2,3,4 the displayed witness with c=2,a=1,r=5/2 works in this formal nonlinear-cap system. Wilson slack at (c,a)=(2,1) is 4-d, hence 2,1,0,-1,-2 for d=2,...,6. Zero slack at d=4 depends on the asserted c<=2 cap (ARGUED in THETAW) as well as a<=1. This review does not prove either upstream optimality theorem by re-labelling its source status.

Two qualifications in the target are wrong or incomplete:

- At fixed theta the soft condition is d<4+theta, not d<=4 as a real-d inequality (THETAW:415). For integer d and 0<theta<1 the feasibility cutoff is indeed d<=4.
- Positive Wilson slack at d=4 does not automatically buy d=5 (THETAW:425–427). Taking c=9/4 and a=1 gives slack 1/4 at d=4 but still deficit 3/4 at d=5. Reaching d=5 needs at least one whole power of Wilson slack and an adequate soft exponent. In the full cap r<=2+theta<3, the soft obstruction at d=5 persists even if the curvature cap is removed.

The script also keeps its data-only cap fixed at 3 in its dimension sweep (tw1_feas.py:132–133), whereas the claimed general-dimensional supply is d-1. The binary d=2,3,4 versus d>=5 conclusion under the Wilson cap survives; the simulated data regions are not the general-dimensional delivered-data regions.

## F12 — CONFIRMED / NOT-VERIFIED by job: what the six symbols actually consume

Attachments: THETAW.md:85–116, :241–288; NORMS.md:644–657; BFT_A.md:398–400, :518–561, :990–998, :1548–1557. Claim status: CONDITIONAL for transferring these jobs to the complete BFT target.

| Job | Independent reconstruction and coupling | Review verdict |
|---|---|---|
| J1, c | Curvature contributes one decay factor to the differentiated cubic leg; Wilson requires c+2a>=4. With c<=2 and a<=1 this pins c=2. It need not equal r or theta. | CONFIRMED for the displayed vertex count; NOT-VERIFIED for the nonlinear supplier and optimal ceiling. |
| J2, r | The residual supplies the differentiated soft leg; summing levels requires r+2a>4. The direct source shift is tied to theta, not merely to the input data exponent. | CONFIRMED for the strict window r>2 at a=1; REFUTED for R_lin's source-class claim (F5). |
| J3, theta | This weights allowed forcing rather than displacement. The plain source's level-0 images have sum bounded by sum_{n>=1}L^{-theta n}=1/(L^theta-1), finite for theta>0. The displayed divergence-form reduction in BFT_A:536 consumes summability of L^{-(1-theta)q}, giving theta<1 for that estimate. | CONFIRMED as the window consumed by these bounds; it is not a proof that every possible endpoint method fails. |
| J4, alpha | A lattice-scale oscillation has Holder cost L^{alpha n}; residual source decay contributes L^{-theta n}. Their product imposes alpha<=theta. A freely chosen positive alpha can be arbitrarily small in this inequality system. | CONFIRMED for this coupling and absence of a positive floor in the inspected algebra; NOT-VERIFIED for all uninspected consumers. Strict alpha<theta is a safe chosen window, not a necessity proved by the alpha>theta counterexample. |
| J5, m | This is a spatial exponential rate, not a power of L per scale. HX's inspected heading is explicitly m=0; THETAW admits the positive-rate family is not analysed (:663). | NOT-VERIFIED for faithful splitting of norm, tree, and polymer rates. A proof only at m=0 supplies neither a positive-rate theorem nor a contradiction with one. |
| J6, a | Cubic expansion of a squared field strength gives <dX,B_2(X,X)>; expansion of a squared soft residual gives <r(X),B_2(X,X)>. Polarization produces a differentiated leg and TWO undifferentiated potential legs in each such trilinear term. Their two decay factors are exactly the 2a in N7. | CONFIRMED that the displayed route needs two potential estimates; NOT-VERIFIED that every term of N1-15 has the claimed form or that the original BFT-1 omits every way of supplying them. |

The J6 consumption is not spurious. A curvature bound alone cannot control a gauge potential: in a commuting subgroup, A=d lambda has dA=0 with arbitrarily variable nonzero A, and compatible gauge changes preserve zero soft residuals. A chosen-gauge estimate or a norm that already includes it is needed. The inspected BFT_A:1555–1556 bounds the soft coefficient by p_L^2(2|x-bar|+3 delta_x), then by 7 p_L^2 L^{-(k-l)} eta. This directly exposes an undifferentiated-potential input and supports the consumption mechanism independently of N7's label.

The cap a<=1 can be re-derived for an interpolated gauge with fixed nonzero endpoint difference: a path of M=L^n fine links joining two fixed coarse values with difference Delta has max link difference >=|Delta|/M. A uniform bound C L^{-a n}|Delta| with a>1 contradicts this as n grows. Its application requires that those endpoint data cannot be gauged away in the admissible class. Axial integration of curvature over length L^n supplies a bound C L^{-(c-1)n}, while the interpolated boundary term supplies C L^{-n}; their sum gives the usable exponent min(c-1,1). This is a bound one may choose, not in itself an optimality proof or a requirement that every weaker recorded exponent equal that minimum. At c=2 the usable value is 1.

Direct verification limits matter here: the original REVIEW_S22 BFT statement and NORMS's N1-11/N1-15 proofs are outside the permitted reads after the two required procedure files. Therefore the exact omission claim at THETAW:99–105 and the verbatim "twice in every cubic vertex" inventory remain NOT-VERIFIED, even though the need for the two potential factors in the displayed route is independently reconstructed. No PROVEN-HERE label was substituted for those missing reads.

## F13 — NOT-VERIFIED: the new potential clause changes the bounded object unless its gauge scope is specified

Attachments: THETAW.md:99–105, :576–586, :593–610. Claim status: GAP in the replacement as a statement about globally bounded actual potentials; CONDITIONAL counterexample below.

The norm paragraph concerns displacements X relative to Z^lift and the vertex discussion concerns lifted variations zeta_j^c Y. The new BFT-1c instead says that there is a gauge representative with own-unit potentials <=C_0 L^{-(k-j)} epsilon, under data assumptions that bound only plaquette curvature. These are not automatically the same object.

If this is a bound on a single global representative of the actual connection on the torus, flat holonomy supplies a counterexample. Embed a commuting diagonal subgroup in SU(N), take level-k side T, and take a constant link exp(i phi H/T) in one direction, with H=diag(1,-1,0,...), 0<phi<pi. Every plaquette is identity, but the cycle holonomy exp(i phi H) is nontrivial. A compatible fine lift has links exp(i phi H/(T L^{k-j})). Periodic gauges preserve cycle holonomy up to conjugacy. If all these fine-link logarithms were <=C_0 L^{-(k-j)} epsilon, the sum along the T L^{k-j}-link cycle would bound its group distance from identity by C_0 T epsilon. The fixed nontrivial holonomy violates this for sufficiently small positive epsilon, while the data still have curvature 0<=epsilon.

A displacement bound relative to a lift retaining the holonomy, or separate gauges on contractible blocks with controlled transition data, avoids that counterexample. The clause must specify which is meant, and the consumed vertex must use the same object and gauge. Calling J6 "missing" and inserting a bound on a different object is not a faithful repair.

## F14 — CONFIRMED with limits: the abort and false bracket; REFUTED exact-only and citation claims

Attachments: THETAW.md:177–178, :441–475; checks/tw1_feas.py:197–202; checks/tw1_out.txt:54–55; checks/tw1_err.txt:1–7. Claim status: PROVEN for the symbolic corrections; NOT-VERIFIED for the uninspected tw1b rerun and external reuse.

The saved log shows G prints only the data-only 1/3 value, and the traceback identifies the subsequent Fraction construction at :202. That line evaluates 3**(1/2) for the first fractional case before trying to use it as a Fraction denominator. Python's fractional power leaves rational arithmetic; the resulting denominator is not Rational. Thus the claim of no floating point anywhere in the whole original script is false, although the feasibility predicates before G do use exact Fractions. This review did not execute that display line.

The quoted bracket is false exactly as disclosed. For A=3^{-1/2}, the correct ordering is

    A=3^{-1/2} > 3^{-1}=1/3 > 3^{-3/2},
    or, as a bracket, 1 > A > 1/3.

The boundary identity tr=2 => A=1 is independently correct, but the quoted boundary row at THETAW:177–178 was never reached in the original tw1-G log. It must not be represented as observed output of that aborted check.

A string search within all permitted target/check files found the false bracket only in THETAW's disclosure at :467. The files named tw1b_display.py and tw1b_out.txt do NOT match the permitted tw1_* glob and were not opened. Their exit-0 claim and possible quotation in any other lane file remain NOT-VERIFIED. No search of snapshots, ledgers, PROOF.md, or the wider lane was performed.

One further endpoint attribution error: checks/tw1_criteria.md:53 and THETAW.md:413 associate the theta>0 floor with C_P. But C_P(0)=L/(e log L) is finite. The theta=0 obstruction in the displayed estimates is the geometric level sum 1/(L^theta-1), not C_P.

## Evidence boundaries and citation audit

The two discretionary files were docs/ai_methodology/SCIENCE_WORKFLOW.md and docs/ai_methodology/skills/review-loop/SKILL.md, required by the project entry point. The user's narrower no-git, single-write, and read-budget instructions controlled over broader procedure references; no further skill references, registry files, or audit material were opened. No agents were spawned. The review is local mathematical/source review, not an audit-status operation.

Target and check files were read in bounded ranges. BFT_A was read only in short ranges around the six authorized locations (including the immediately adjacent BL-5 statement, RBA2 correction, and rough-image formulas needed to interpret them). NORMS's scientific evidence used here is section N7. Operational disclosure: the initial locator grep for N7 also returned isolated mentions of N7 from other NORMS sections; no surrounding sections were opened and those incidental lines are not used as proof.

Current anchor checks locate the cited formulas at NORMS:644–657; the earlier window at BFT_A:396–400; its actual conditional replacement at :826–834; SPD's transport distance at :830–831; the rough-image exponent at :991; and HX's split at :1549–1557. These citations match their current text. The 3/4 attribution to :396–397 is a misquotation, not an observed line-number drift. The original G boundary-output citation is also invalid as a run receipt (F14).

PROOF.md was not opened. All claimed PROOF line correspondences, including :30–34, :6236–6239, and :6326, remain NOT-VERIFIED; none is silently certified by the N7 algebra. REVIEW_S22, RTARGET, SF, NBG_B, and the other cited scientific sources were likewise not opened. The exact original BFT inventory, the asserted endpoint alpha=theta status, and the tw1b rerun are therefore not independently verified. This limit does not weaken the direct contradictions identified inside THETAW and its permitted sources.

## Summary table

| Finding | Review verdict | Claim status after review | Consequence |
|---|---|---|---|
| F1: transport distance replaced by distance to top | REFUTED | GAP; weaker SPD remains OPEN | Do not redirect the lane on the purported sigma>0 sufficiency proof. |
| F2: fixed 1/4 rough deficit | REFUTED | Corrected arithmetic PROVEN | The deficit is 1-theta; its infimum is 0, not 1/4. |
| F3: omega_0=1 in the residual slot | REFUTED | GAP | The replacement reinstates a source weight explicitly rejected by its consumer. |
| F4: conditional ceiling allegedly removed | REFUTED | CONDITIONAL window retained | BFT_A:827 retains theta<=1-alpha; 3/4 is only the alpha=1/4 example. |
| F5: R_lin contains residual sources with r=3 | REFUTED | GAP | Its own C2 makes that labelled region empty for theta<1. |
| F6: all 440 points have exponent -theta | REFUTED | Corrected counts PROVEN | Only 55 do; 385 are strict below-cap points. |
| F7: controls certify the claimed sensitivity | REFUTED | Program behavior PROVEN; analytic premises NOT-VERIFIED | C and D survive deletion of the individual checks they are said to validate; finite grids cannot certify continuous emptiness. |
| F8: alpha=sigma/2, theta=sigma works for every sigma>0 | REFUTED | Corrected witness PROVEN under the different top-distance hypothesis | Use theta=min(sigma/2,1/2), alpha=theta/2. |
| F9: actual F3 remainders provably exclude every pair | REFUTED | CONDITIONAL / GAP | The nonlinear-side obstruction is an upper-bound power count, explicitly downgraded upstream. |
| F10: full strengthened inverse, including endpoint | NOT-VERIFIED | GAP | Sup and Sigma aggregation differ; the Sigma direct-shift endpoint loses a factor k. |
| F11: reduced algebra and integer dimension cutoff | CONFIRMED | CONDITIONAL on supplied caps/decays | Formal feasibility at d=2,3,4 and emptiness at d>=5; zero Wilson slack at d=4 under c<=2,a<=1. |
| F12: two potential factors in the displayed cubic route | CONFIRMED | CONDITIONAL | J6 is a real input, but the exact original omission/all-vertex inventory is NOT-VERIFIED. |
| F13: replacement potential object and gauge scope | NOT-VERIFIED | GAP | A global actual-potential reading fails on flat torus holonomy; a displacement/local reading must be stated. |
| F14: abort and false bracket | CONFIRMED | Symbolic correction PROVEN | Exact-only claim and original boundary-output receipt are REFUTED; tw1b/external reuse NOT-VERIFIED. |

Overall review verdict: the advertised R_lin, SPD reduction, fixed rough deficit, and several check interpretations are **REFUTED** as stated. Satisfiability of the complete repaired target is **NOT-VERIFIED**, not proved impossible. The smaller exponent system has a **CONFIRMED** formal witness, with **CONDITIONAL** analytic applicability.

## Short stdout summary

Verdicts: REFUTED the advertised R_lin, SPD reduction, fixed deficit, and check interpretations; CONFIRMED reduced inequality feasibility; NOT-VERIFIED full-target satisfiability, strengthened inverse, original missing-clause inventory, and weakened SPD theorem.

Numeric/exponent corrections: fixed rough deficit 1/4 -> 1-theta (infimum 0; at theta=1/2 it is 1/2); universal ceiling 3/4 -> 1-alpha (7/8 at alpha=1/8); residual-source r=3 -> supplied direct-shift exponent 2+theta (5/2 at theta=1/2), with formal A=L^{-theta} rather than 1/3 there; residual omega_0=1 -> L^{theta k}; 440 points with exponent -theta -> 55, with 385 counterexamples; cap-boundary exponent range [-11/12,-1/12] -> [-11/12,-1/6]; grid EMPTY at theta=1/24 -> witness (alpha,tc,tr,tA)=(1/48,2,49/24,1); universal theta=sigma -> theta=min(sigma/2,1/2), alpha=theta/2 (original fails at sigma>=1, and above 2/3 if the conditional ceiling is kept); Sigma endpoint r<=2+theta -> r<2+theta for that geometric-sum estimate (endpoint gives k); "any positive slack permits d=5" -> at least one full Wilson power plus the soft condition; false bracket -> 1>A=3^{-1/2}>1/3; theta=0 does not make C_P diverge, since C_P(0)=L/(e log L).

Most dangerous unverified point: whether decay L^{-sigma(m-l)} of transported smooth parts, for any sigma>0, actually yields a k-uniform repaired source/inverse estimate. The file's supposed proof replaces m-l by k-l and cannot answer that question.
