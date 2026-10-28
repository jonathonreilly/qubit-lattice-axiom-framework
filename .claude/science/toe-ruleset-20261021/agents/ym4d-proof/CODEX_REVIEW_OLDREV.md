# Independent hostile re-review of REVIEW_SQ_S4, REVIEW_BFT_A_S8, and REVIEW_FLOW_S13

## PRE-STATED — 2026-10-28 22:14:22 UTC

Scope: inventory every verdict and ordered fix in the three named reviews; re-derive every refutation and fix against the cited regions of SQ.md, BFT_A.md, and FLOW.md; independently examine at least five CONFIRMED findings in each review. Write only this file. No git commands, snapshots, ledgers, full PROOF.md reads, floating-point numerics, or long jobs.

Prior exposure: before this pre-statement I read SCIENCE_WORKFLOW.md and REVIEW_SQ_S4.md lines 1–180 (including its headline findings). I have not yet examined any target source or performed any derivation. This is a prospective test plan, not a claim of blindness to those review assertions.

Refutation tests:

1. A purported refutation fails if its witness violates the quantified hypotheses, its calculation is wrong, or it targets a stronger statement than the source. A proof gap alone does not refute a theorem.
2. An ordered fix fails as a sufficient repair if the replacement still lacks a hypothesis or proof, breaks a downstream use, hides a conditional constant, or mislabels an incomplete proof PROVEN. Distinguish a justified defect diagnosis from an adequate repair.
3. Reconstruct symbol meanings from current source strings and exact line positions; never transport a constant by name alone. In particular distinguish the two SQ theta thresholds and re-evaluate which minimum binds as epsilon varies.
4. Re-evaluate minima and universal quantifiers using the written dependencies. A historical fixed-value calculation does not establish a claim at a later output parameter.
5. For each cited gate, identify a realizable rejecting input. Flag vacuous, tautological, insensitive, or incompatible conditions. Scripts outside the authorized read set cannot receive implementation verification.
6. Check source-line citations by their strings; report drift and substantive mismatches separately. Do not pretend the current mutable source is the frozen historical revision.

Findings use CONFIRMED / NOT-VERIFIED / REFUTED. Mathematical claims use PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. A CONFIRMED diagnosis does not imply its entire parent theorem is PROVEN. Historical run results, provenance, and unavailable dependencies remain NOT-VERIFIED.

Hit-rate convention, fixed before derivation: report counts for the three reviews separately; use CONFIRMED / (CONFIRMED + REFUTED) for decidable, explicitly listed review atoms, and also give CONFIRMED / all examined atoms so exclusions remain visible. Split composite findings where needed and publish the denominator. Inventory-only confirmations are not counted as examined. No percentage is a scientific completeness score.

Read budget: SCIENCE_WORKFLOW.md is optional file 1; the applicable repository review skill is optional file 2. Other reads are restricted to the three reviews and their three expressly named targets, using bounded ranges. No check-script execution or reading outside that set.

## Findings (appended during review)

### Q1 — S4-14's binding minimum is not established; the requested rename remains absent

**REFUTED** as an unconditional numerical delivery. Attachments: REVIEW_SQ_S4.md:301–326, 604–607; SQ.md:188–190 (`theta_0 := 1/(2C_err)`), 318–319 (DESC minimum), 1609, 1622–1634 (the second theta_0 and C_D).

Use distinct names: theta_SUP = 1/(2C_err(C_D)); theta_REG = min(theta_G, theta_eps); theta_eps = epsilon_*/max(4·2.47N sqrt(kappa_+), 16·32^(1/8) C_0). At the review's N=2, L=3, kappa=1 reference point, theta_eps = epsilon_*/((1336/25)·2^(5/8)). Thus theta_G binds theta_REG **only if** epsilon_* >= ((1336/25)·2^(5/8)) theta_G. There is no such lower bound on epsilon_* in the cited proof. A smaller admissible epsilon_* remains admissible and can reverse the minimum.

Furthermore, DESC retains theta_SUP/C' separately. Its C_D is now max(2(1.011A_0+B_0), C_r), with A_0 proportional to C_T, not the historical input C_D=2 used for 7.6e-9. The review's proposed ceiling theta_G <= 1.46e-13 neither identifies theta_G nor identifies the binding entry of DESC. Consequently eta_flat ≈ 4.2e-36 and t_pr ≈ 1.5e-13 are not established values. The exact corrected deliverable is the full symbolic minimum in SQ.md:318, with both theta names distinguished. Claim status: **CONDITIONAL**, not PROVEN numerical delivery.

There is an additional inequality-direction problem in the ceiling itself: SQ.md:1526 gives `||F_0||_2 <= a theta`, a=2.47 sqrt(2). The review substitutes this upper bound into `beta >= C_q L³ C_1 ||F_0||_2` as if it were equality/a lower bound. That substitution cannot prove a necessary upper bound on the *largest actual* theta_G. One may instead explicitly choose a conservative envelope `beta_bar=A theta+B theta²`, where `A=C_q L³(C_1 a+C_2)` and `B=C_q L³ C_3(a+C_X)²`, and impose beta_bar<=1/16 together with LEV-E. For B>0 its positive cutoff is `1/[8(A+sqrt(A²+B/4))]`. The omitted C_2,C_3 terms and the chosen envelope must be stated before any number is banked.

In particular the displayed `beta >= 4.29e11 theta` is not the consequence of that substitution: the isolated term `C_q L³ C_1 ||F_0||_2` is bounded **above** by the corresponding multiple of theta. Likewise `e=242.9 theta` is an envelope, not an equality for every configuration. A cutoff derived from the envelope in LEV-E (the review's 3.04e-13) is a conservative sufficient choice for that condition, not a demonstrated necessary ceiling on the actual configuration-dependent expression.

**CONFIRMED**: the name collision and the need to rename it. The two definitions remain literally `theta_0` at SQ.md:188 and 1622; no S4 rename is present in these cited regions. The review itself also confuses its item numbers: its opening summary's “form, S4-14” is body S4-15, and its opening “numbers, S4-13” is body S4-14.

### Q2 — S4-6's mandatory R_0 change confuses a bounded stopping factor with a failure

**REFUTED** as a required mathematical correction. Attachments: REVIEW_SQ_S4.md:201–209, M4-2/M4-3, binding fix 8; SQ.md:1498–1506.

Put j=floor(log_2 R)-6 and p_j=2^(j+1). For 64 <= R < 128, j=0, and the empty iteration gives exactly sup <= ||w||_2 <= 128² R^(-2)||w||_2. This is already absorbed by the unspecified constant C in the source's conclusion. R_0=64 is therefore usable; changing it to 128 merely moves this bounded interval to the trivial branch.

For R >= 128 the **actual** stopping factor is R^(4/p_j)=R^(2^(1-j)). On [2^(j+6),2^(j+7)) its supremum is 2^((j+7)2^(1-j)); this decreases for j>=1. Its supremum is **256**, approached as R tends to 256 from below (integer radii: maximum **255**). At R=128 it equals **128**, not 128². The larger envelope R^(256/R) does have maximum 128² on R>=128. The review conflates the factor and its envelope. The proposed replacement e^100 -> 128² is safe but crude; “C_T >= 16384” is a choice of this trivial estimate, not a necessary lower bound on the theorem's optimal constant.

### B1 — S8-7/P8-9 does not yet prove the asymptotic refutation it orders others to bank

**NOT-VERIFIED**: (GE-T) is false. **REFUTED**: the review has supplied a complete refutation or may declare the dependent theorem vacuous on that basis. Attachments: REVIEW_BFT_A_S8.md:221–275, 480–490, 525–548; BFT_A.md:3307–3313, 3580–3592.

The quantifier is one C_GT for every k,T,l,u. One exact value at k=2 only imposes a finite lower bound on C_GT. The review expressly leaves unproved both (i) a uniform bound on the other summand Pi_E u and (ii) absence of cancellation in the higher funnel terms. A ratio for phi_2/phi_1 does not prove any bound on phi_i for i>=3. The source itself labels the no-cancellation argument ARGUED. The review's “essentially proven”, “FALSE outright”, and the replacement ordered in P8-9 cross that boundary without supplying the missing uniform estimates. Correct claim status: **ARGUED**, with these two **GAP** obligations. This does not establish that (GE-T) is true.

### B2 — S8-12/P8-6 drops a hypothesis in its replacement theorem

**REFUTED**. Attachments: REVIEW_BFT_A_S8.md:349–366 and binding P8-6; BFT_A.md:3027–3047 and 3615–3620.

The ordered template `(GE-T)_P => (PW-i)_P => SR_P` omits (PW-ii), although the source's t>=2 interpolation term explicitly uses it. With only PW-i the remainder contributes O(eta²) at each level, so summing gives O(k eta²), not SR's k-uniform bound. The corrected template keeps the other PW-E inputs and reads `(GE-T)_P => (PW-i)_P`; `(PW-i)_P + (PW-ii)_P + SPD + the representative/response hypotheses => SR_P`. Nor does failure of a sufficient hypothesis GE-T logically imply failure of PW-i. The review acknowledges this latter limitation at lines 543–548, contradicting its unconditional vacuity claims elsewhere.

### F1 — S13-13's “arithmetically unachievable” test is a false refutation

**REFUTED**. Attachments: REVIEW_FLOW_S13.md:497–510 and binding fix 7; FLOW.md:4620–4625, 4771–4773, 4803–4815.

O(delta^4) is an upper-order statement with an unspecified coefficient; it is not the error delta^4 and provides no lower bound. At delta=1/50, delta^4=1/6,250,000. An error c delta^4 passes 1e-7 whenever |c|<5/8; c=0 also qualifies. For a concrete exact control, the central derivative of f(x)=x is 1 at every nonzero rational step, and its Richardson combination is also exactly 1. It has error O(delta^4)=0 and passes the quoted tolerance at delta=0.02. The B4 comparison therefore **could have passed**. Field amplification alone supplies no nonzero lower coefficient either. The same logical defect affects the claimed predetermined B3 failure.

The reported B4 residuals support an empirical truncation diagnosis, not pre-run impossibility. B3's absence of a usable scaling sequence is a justified limitation. The ordered text “the FAILs were fixed at pre-registration” must not be applied. The source's separate inference at FLOW.md:4773, “The closed form is therefore exact” from finite-difference scaling, is also invalid as proof; its analytic derivation must carry that conclusion.

### Q3 — S4-3 diagnoses the SU(2) hole correctly but orders an insufficient SU(N) repair

**CONFIRMED** diagnosis; **REFUTED** sufficiency of the ordered `sup ||1-U(p)|| <= 1/4` fix for every N. Attachments: REVIEW_SQ_S4.md:127–156; SQ.md:1388–1390, 1460–1470, 1511–1515.

For SU(2), U(p)=-I gives P=0 and ||1-U(p)||=2, so small P does not imply admissibility. But the proposed repair has its own counterexample: take N=32 and U(p)=exp(i pi/16) I_32. Its determinant is 1, P=0, and

`0 < ||1-U(p)|| = 2 sin(pi/32) < pi/16 < 1/4`.

It can be realized by putting this central matrix on a single link and identity on all other links: adjacent plaquettes are the center element or its inverse. Both P and its source vanish everywhere, including after imposing the proposed 1/4 bound. The comparison `eta <= c_N |P|` still fails. SQ.md:1389's assertion that the principal eigenangles sum to zero has silently replaced “zero modulo 2 pi” by “zero”; here their sum is 2 pi.

A sufficient repair is a genuinely identity-centered SU(N) logarithm sector, for example `eta <= min(1/4,1/N)`. Indeed principal angles then obey |theta_j| <= (pi/2) eta <= pi/(2N), so their sum, an integer multiple of 2 pi, is zero. Writing P_j=i(sin theta_j - mean sin theta), its pairing with theta is sum theta_j sin theta_j >= cos(pi/(2N)) sum theta_j²; Cauchy–Schwarz supplies a finite inverse comparison. This is an independent derivation of the missing sector condition.

This refutes the **repair**, not EPS-T's P-valued conclusion (which is zero on the witness). Also EPS-0a's written hypotheses concern P and S, not Wilson energy; the review's proposed one-line energy discharge is not available for every critical point in that corollary as stated. Add the sector hypothesis to EPS-0a too, or strengthen its energy hypothesis. Minimisers and GAP can discharge a sufficiently small N-dependent sector using their actual Wilson-energy bounds. Claim status until this is done: **GAP**.

### Q4 — S4-16 gives a necessary condition as an equivalence, and loses a square root

**REFUTED** as the single sufficient condition it claims; **CONFIRMED** that constants must be quantified or left conditional. Attachments: REVIEW_SQ_S4.md:356–399, 645–672; SQ.md:145–146, 168–189, 294, 318, 1622–1634.

At N=2,L=3,kappa=1, exact decimal-rational substitution gives

`K/C_D = 39121/500`, `K_top/C_D = 121855493/1500000`,

`A := C_err/C_D² = 13443755175169/937500 + (1744341577691916833/1125000000000) sqrt(2)`.

The rational bounds 1414213/10^6 < sqrt(2) < 1414214/10^6 give **16,532,779 < A < 16,532,781**. This supports the review's rounded coefficient, not its inference. Since t_pr <= theta_SUP, epsilon_1 < t_pr implies

`C_D < (2 A epsilon_1)^(-1/2)`.

It is only necessary: the other entries of DESC, including theta_eps, can still be smaller. The review's literal displayed reciprocal `1/(3.31e7 · 6.7e-40)` is **10^36/22177**, approximately 4.509e31, not 6.7e15. Its **square root** is approximately 6.7e15. The intended rounded necessary bound survives; the written arithmetic and the claimed equivalence do not.

There is an internal numerical contradiction with S4-14 even on the review's own chosen C_T=16384 branch. From c_N>=1, sqrt(2)>7/5 and 2^(5/8)>3/2, SQ's A_0 and G give `C_D > 23073964032/3125 > 7,383,668`, hence **theta_SUP < 6e-22**. Therefore t_pr < 6e-22, not approximately 1.5e-13; tau_flat < 6e-22/53 and eta_flat < `(6e-22)^2/(640·53^4)`. This is a conditional contradiction using the review's own C_T choice, not a claim to have computed the actual Moser constant.

Likewise “only the C_T half is live” is unsupported: epsilon_* has no proved positive numerical lower bound in the cited proof. The user-reported later inadmissibility of epsilon_*=1e-4 is not independently established by these permitted earlier source regions. No historical fixed epsilon value is used as authority here.

### Q5 — The polar-factor diagnosis survives, with a narrower quantifier

**CONFIRMED**: determinant-normalized polar decomposition is not a general SU(2) maximizer; quaternion projection is the right replacement. **REFUTED** if “only on the quaternion line” is read as an iff. Attachments: REVIEW_SQ_S4.md:404–422 and binding fix 6; SQ.md:1701–1709.

For `M=diag(99/100+i/5,1)`, the determinant-normalized polar factor has phase with cos t=10/sqrt(101), sin t=1/sqrt(101). This is the member s=1/10 of `M(s)=diag((1+i s)^2,1)`, which approaches identity as s tends to zero and remains nonstationary for every nonzero sufficiently small s. The objective on diagonal SU(2) matrices at s=1/10 is `(199/100) cos t + (1/5) sin t`. Its derivative at that polar phase is **1/(100 sqrt(101))**, nonzero. The optimal objective squared exceeds the polar objective squared by **1/1,010,000**, exactly. This independently validates the failure mechanism without reproducing any floating-point residual.

Every SU(2) matrix is a unit vector in the real quaternion subspace under the real trace pairing, so Cauchy–Schwarz maximizes the objective by normalizing the orthogonal projection of M onto that subspace. However, M=diag(2,1) is outside that subspace and has polar factor I, which is also its SU(2) maximizer. Correct wording: exactness is guaranteed on the quaternion span and fails for general complex perturbations; it is not exclusive to that span. The historical 3.7e-9, 1.2e-16 and 4.4e-16 outputs remain **NOT-VERIFIED**.

### B3 — Exact reconstruction validates the first two funnel numbers and refutes the claimed tail

**CONFIRMED**: phi_1=-1/54, phi_2=-17/13122 for the unnormalized curl source, and psi=-65/26244 after dividing by 8. **REFUTED**: the asserted higher geometric tail and P8-4's identification of psi with +/-1/54. Attachments: REVIEW_BFT_A_S8.md:246–275, 464–469, 550–568; BFT_A.md:3291–3294, 3307–3309. The path convention is explicitly available at SQ.md:1008–1010 and FLOW.md:4549–4554, 4649–4654.

Independent exact calculation: center nested blocks at 0; let p be the (0,1)-plaquette at z=(1,0,0,0). The four nonzero entries of u=d*delta_p are +1 at (z,0),(z+e_0,1), and -1 at (z+e_1,0),(z,1). For scale n, the straight-average weight of an edge p_mu in output (X,mu) is

`n^(-4) · #{y_mu in [n X_mu-r,n X_mu+r]: 0 <= p_mu-y_mu < n}`,

times the transverse block indicators, r=(n-1)/2. Average the signed path sums from 0 to each of the 81 endpoints in {-1,0,1}^4 over all 24 coordinate orders. The integer incidence totals are -36 at n=1 and -204 at n=3, with denominators 24·81 and 24·81·81 respectively. Thus phi_1=-1/54, phi_2=-17/13122, and their ratio is 17/243.

For every n>=9, the two opposite edges in each orientation have identical longitudinal position and lie in the **same transverse block**. Their straight-average weights cancel exactly for every output link. Therefore `Q_str^(n) u = 0`, and **phi_i=0 for every i>=3**. This is an all-scale support proof, not extrapolation from more depths. Consequently psi_k=-130/6561 for unnormalized u for **every k>=2**, and -65/26244 for u/8. The four symmetric offsets listed in the review give zero; swapping the first two axes or using offset (1,-1,0,0) gives +130/6561.

Corrections: P8-4's `psi=+/-1/54` is the value of **phi_1**, not psi_k. Its corrected psi_k for k>=2 is **+/-130/6561**. The alleged 0.5% tail beyond phi_2 is **zero** for this witness. After retaining only phi_1 the remainder is **17/243 of phi_1**, not the approximately 7.5% obtained by extrapolating a repeated ratio. Retaining two terms leaves **zero**, contradicting the review's blanket “every finite truncation ... leaves a ... remainder” inference from this probe. This does not settle tails for the distinct Green-function field g_0 or the actual Y^p response.

This calculation discharges B1's *second* missing estimate for this particular witness by a different mechanism. The S_E projection/cancellation estimate remains **NOT-VERIFIED** within the authorized source set; the reviewer did not prove it by calling it routine.

### B4 — TE's exact size omits the T=1 case

**REFUTED** as the review's unqualified exact identity. Attachments: REVIEW_BFT_A_S8.md:209–219, 503–505; BFT_A.md:3288, 3474–3477, 3509–3516.

T=1 is included in the setting. There is one coarse root. From `Gamma_E(d lambda)=-lambda+I_chi lambda`, apply lambda=1: d lambda=0, so I_chi 1=1. With one periodized tent this forces chi_X=1 everywhere, hence **||d ev^(l) chi_X||_1=0**, not **8 L^(3(k-l))**. The gauge-transformation identity TE itself remains correct. An 8-times-power size needs a noncollapsed torus and an actual discrete tent summation; a continuum Riemann integral is not that proof. This endpoint does not disprove a GE-T counterexample restricted to larger T.

### B5 — The ordered stand-in transport supplies an identity, not the claimed estimate

**NOT-VERIFIED** quantitative transport; **REFUTED** the claim that P8-3 already supplies a sufficient size estimate. Attachments: REVIEW_BFT_A_S8.md:277–306, 458–463; BFT_A.md:3522–3528.

Granting the displayed local Coulomb equations, product expansion gives `d*d[sum_X chi_X(lambda_X-lambda_X0)]`. Differences of chi cost 1/n or 1/n², but multiply differences or values of the harmonic functions lambda_X-lambda_X0. No bound on those factors is supplied. The identity sum d chi=0 cancels a common function; it does not cancel the remaining products or control their magnitudes. For example, locally harmonic differences A z_1 and 0, with chi_1=z_1²/n² and chi_2=1-chi_1, give a discrete Laplacian proportional to **6 A z_1/n²**, not zero; A is not bounded by partition unity. Thus a quantitative S_E-to-S_C0 bridge still needs input-specific potential estimates. The equation is useful; calling it a completed estimate is not.

### F2 — S13-11 overlooks that Pi-loc is a local Hessian by definition

**REFUTED**: position locality and analyticity require a further cluster-expansion argument or are “not argued at all.” Attachments: REVIEW_FLOW_S13.md:435–449; FLOW.md:1451–1456, 3009–3012, 4595–4596, 4735–4736.

FLOW defines Pi(M)=partial_Z² h(0;M) for **one link**, and Pi_(k+1)=direct_sum_c Pi(Mbar_c(B_k)). The direct sum already forbids off-link matrix elements. The link exponent differs from the maximization defect only by a Z-independent term. Put R=W_0(M)^(-1)M. Expanding the exponential gives a Hessian proportional to `-Re tr(Z² R)`. At diagonal M, for Z=z E_ij-conj(z) E_ji this is `(Re R_ii+Re R_jj)|z|²`; after normalization to Pi(1)=1 its root eigenvalue is `(Re R_ii+Re R_jj)/2`. It is analytic near identity because the stationary equations have invertible W-derivative there; the analytic implicit-function theorem gives analytic W_0. The eigenvalue equals 1 at identity and stays positive on a sufficiently small fixed local neighborhood.

Thus all three Pi-loc clauses follow locally from the displayed construction; no spatial inverse or cluster expansion is involved. The one-line argument in §107 alone mentions only color, but the review had read §30 and missed its direct-sum definition. This removes that particular provisional input after the derivation is made explicit. It does not prove the M-part, T-a3, or the plane-wave/constant-flux exchange.

### F3 — S13-12 confuses lambda-degree with a momentum pole order

**CONFIRMED**: Ntilde_1 and Ntilde_2 have total lambda degrees 12 and 30 and are conservative. **REFUTED**: they imply the specific claimed |K|^(-30) allowance. Attachments: REVIEW_FLOW_S13.md:393–409; FLOW.md:4603–4608, 4750–4763.

Ntilde_2=product_(t=-2..2) lambda(K+tP)^6. At fixed generic nonzero P with only t=0 singular, lambda(K) is of order |K|², so the stated normalized bound permits **|K|^(-12)**. At P=pi e_2 the t=-2,0,2 factors coincide and it permits **|K|^(-36)**. Along joint limits P proportional to K with all shifted momenta nonzero and of order |K|, it permits **|K|^(-60)**. There is no universal exponent 30. At order 1 the analogous generic fixed-P exponent is **8**, and the simultaneous soft exponent is **24**. These describe the weakness of the written normalization, not actual divergences of the proved projector coefficients. The valid repair is to specify which momenta approach zero and which common denominator a downstream estimate needs.

### F4 — S13-16's proposed deletion loses the lower bound needed for its refutation

**CONFIRMED**: the Schur correction is bounded by kappa C(K)² and yields W_n <= C_K/n for sufficiently large n. **REFUTED**: “the FALSE verdict needs only the upper bound,” so the final lower-bound discussion can simply be dropped. Attachments: REVIEW_FLOW_S13.md:451–470 and binding fix 9; FLOW.md:3978–3980, 4277–4283, 4777–4783.

The actual target VC-L is convergence at rate L^(-2n), not a nonzero lower limit. W_n=L^(-2n) also satisfies W_n<=C/n. An upper bound tending to zero cannot refute that target. The missing lower bound matters.

For the **actual S4' maps** it can be supplied from the very estimates §108 displays. Write A_i=Q_str^(L^i)-D h^(i). At fixed K, ||Q_str^(L^i)||<=L^(-i), ||h^(i)||<=H uniformly, and ||D(K)|| is finite. Thus ||A_i||<=1+||D||H=:B_K. The positive noise sum has Y_VV <= kappa^(-1) n B_K² plus the finite fixed-K M-part. Cauchy–Schwarz therefore gives **W_n >= 1/(C_K n+C'_K)**. Combined with the Schur upper bound, **W_n is of order 1/n**, and log W_n=-log n+O_K(1). This really excludes convergence to zero at L^(-2n). Status: **PROVEN from these displayed uniform S4' bounds**. The review should choose its “prove O(n)” option, not its deletion option. Extending this repair to “every covariant map” needs those same uniform bounds and is **NOT-VERIFIED**; covariance alone does not give them.

### F5 — S13-20 misses a logarithm-branch hypothesis in the exact S4' claim

**REFUTED** as literally quantified over every Cartan lift satisfying D'; **CONFIRMED** locally in the identity-centered lift. Attachments: REVIEW_FLOW_S13.md:227–246; FLOW.md:4560–4568, 4637–4641, with its contour-average definition at 4553 and 4649–4654.

The inference `||exp(delta H)-1||<1 => |h_j delta|<pi/3` is false: delta=2 pi, H=i diag(1,-1) gives identity on the left. D' controls a group element, not a chosen lifted real line sum.

A whole-map witness at L=3: set all fine links to identity, represent one direction-0 link from (2,1,1,1) to (3,1,1,1) by a_b=2 pi with H=i diag(1,-1), and all other a's by zero. Every group link and every composite is identity, so D' holds at every level and the nonlinear S4' output is identity. For the coarse direction-0 link from block {0,1,2}^4 to its neighbor, this fine link lies on the straight paths and on no within-block funnel. Exactly three of the 81 starting sites' straight paths contain it; averaging over coordinate orders does not change that. Hence its Q_root coefficient is **1/27**, and exp((Q_root a)H)=exp((2 pi/27)H), which is not identity. The exact statement needs a compatible small lift with every contour logarithm equal to its unwrapped Cartan line sum. This preserves the perturbative plane-wave results near a=0; it refutes the review's unqualified all-domain confirmation.

### Q6 — S4-7 overlooks a small but exact combinatorial error

**REFUTED**: every face in the stated spanning-tree gauge has at most two non-tree edges. Attachment: SQ.md:1422–1425; REVIEW_SQ_S4.md:211–231 confirms the lemma's proof without noticing this.

The z=1 face of the named cube has edges 001–101, 101–111, 011–111, and 001–011. None is among the seven tree edges listed in the source. Its holonomy has **four**, not at most two, non-tree factors. The Bianchi-defect proof is repairable: use at most four factors, each within 2 epsilon of identity, then the first-order oriented edge sum still cancels. Only the uncomputed C_B changes. This is not a counterexample to the O(epsilon²) Bianchi statement.

## Independent positive checks (the confirmations sampled)

These are derivations of the specified atoms, not endorsements of every dependency of an entire lane theorem.

### SQ confirmations

1. **S4-5, exponent conversion — CONFIRMED; CONDITIONAL on EPS-T.** SQ.md:1511–1515, 1611, 1625–1627: `n^(3-4/q)(32 n^4)^(1/q)n^(-3)=32^(1/q)`; the conclusion similarly gives `32^(1/q)n^(-2)`. Reflection multiplies the P norm by 4 and the S norm by 16^(1/q). At R=n/2 its source-smallness factor is `2^(-3+8/q)/16 <= 1` for q>4. There is no exponent loss in this arrow; Q3 prevents treating this as a complete proof of the upstream theorem.
2. **S4-7, NREFL and SOB — CONFIRMED.** SQ.md:1401–1415: each crossing face has inverse copies of the same tangent transport, hence holonomy 1 and zero Wilson derivative; the 16 images preserve the remaining norms. SQ.md:1445–1456: applying the four-direction discrete Holder inequality to |f|³ gives `(1/4)·6·2=3`, hence C_S=3. Reflecting to 3Q multiplies squared sums by at most 81, and the path gap gives `C_SP <= C_S(9+9 S_max/S_min) <=27 C_S=81`. The WB support radius follows from composing at most two nearest-neighbor operators; its flat cancellation plus a local tree gauge gives an O(eta) coefficient. Its exact crude counts were not multiplied into a Moser constant.
3. **S4-8, TPL/N1/N2 — CONFIRMED.** SQ.md:402–406, 1528–1549: T_n is the convolution of two n-site indicators, so its maximum is n and total n²; sums over translates by n are n. Two in-plane and two transverse factors give row sum n², column sum at most n^(-2), and entries at most n^(-2). Thus the l² Schur norm is <=1; `||Tv||_2² <= ||Tv||_infty ||Tv||_1 <= n^(-4)||v||_1²`. This proves both norm facts independently of q5.
4. **S4-9, STOKES-avg collection — CONFIRMED as an implication of the displayed local error bounds.** SQ.md:1537–1543: 2mx<=m²+x² gives `4(m²+1.011mx) <=6.022(m²+x²)<6.1(m²+x²)`; `(a+b)²<=2a²+2b²` and 2.03²<4.2 give the other coefficient. Finally `4.044x+C_S' x²<=4.094x<4.1x` when C_S'x<=0.05.
5. **S4-10, LEV-E — CONFIRMED as the stated induction.** SQ.md:1552–1563: counting R_q overlaps by 6·3^4=486 is a safe upper bound. With the preceding norm facts, old errors cost a geometric sum <=1/8 and the current error costs at most C_S'' c_R E_(j-1). Thus `sqrt(E_j)<=e+(9/2)C_S''c_R e²<=e+5C_S''c_R e²<=2e`. No product in the depth is introduced.
6. **S4-11, LOC-T — CONFIRMED as localized transport.** SQ.md:1078–1094, 1571–1582: an incoming funnel differs from the current link only by local residual/spread terms; four incoming links times the adjoint difference factor 2 gives 8. Straight weights total at most L^(-3). The accumulated distance is bounded by `3L^(l+1)+2L^(l+2)<=L^(l+3)` exactly when `(L-3)(L+1)>=0`. The top-current factor is 1.01·1.65=1.6665<1.67, giving the stated C_0.
7. **S4-12, the main CARL geometric mechanism — CONFIRMED; explicit threshold NOT-VERIFIED.** SQ.md:1584–1598: multiply the ancestor count `5^4 L^(4(j+2)-4M)` by the transported column weight L^(-2j), sum j<=M-2, and apply Cauchy–Schwarz over at most 6·7^4 L^(4M) plaquettes. The L^M powers cancel and give `(9/8)5^4·49 sqrt(6)L^4`. The residual series has ratio q_transport L²<=2/3; the quadratic-error series has ratio L^(-4). This proves existence of depth-independent constants. The source does not evaluate C_2,C_3 into the claimed theta_G value.
8. **S4-13, GARSIA and the norm-sum consequence — CONFIRMED.** SQ.md:1600–1613: `S_M^p<=p sum a_m S_m^(p-1)`; conditioning first on F_m is valid because F_M is contained in F_m and a_m is F_m-measurable. Induction gives p! beta^p and summing the exponential series gives `(1-lambda beta)^(-1)`. Summing at most four links per site yields the safe **sum** bound 32n^4(C_0 theta n^(-3))^q. An average over the actual free-boundary links is not literally an average over four links at every site; the sum bound is the one used downstream.
9. **S4-20, absence of CVX-K from these arguments — CONFIRMED.** SQ.md:1620–1639 uses EPS-0a and EPS-0b-avg; 1675–1685 uses flow, GAP, LU-ap and the gauge-functional Hessian. The kernel-energy convexity condition at 1695–1697 occurs in neither argument. This is a dependency check, not a certification of GAP or the imported Hessian estimate.

### BFT confirmations

1. **S8-3, DF — CONFIRMED as algebra from the displayed covariance/projection identities.** BFT_A.md:3466–3477: expand `Y_l=Q^(0->l)Y_0-sum Qr`, add the zero top term using Y_k=0, and take d*. The three divergences are D(j), `-D(j)+I_chi^T D(j)`, and `-I_chi^T D(j)`, hence cancel. A zero-total coarse function is a divergence: route its value at each vertex along a spanning tree to a base vertex. Duality with a sign current gives the l¹ norm. No numerical identity supplies the missing S_E construction.
2. **S8-4, PW-cc exponent and constant bookkeeping — CONFIRMED; CONDITIONAL on the displayed YH and weighted-data estimates.** BFT_A.md:3484–3498: each dual straight transport costs L^(-3) in sup norm and at most L in l¹ norm. The residual factor is `L^(-3(l-m-1)) L^(k-1-m) L^(-2k)=L^(2m+2-k-3l)`. Summing gives at most `L^(-k-l)/(1-L^(-2)) <= L^(k-3l)/(L²-1)`. At 1471, m'=m_*'/3 is fixed; at 2389 the geometric sum over Z^4 factors into four copies of `(1+e^(-m'))/(1-e^(-m'))`. Torus distances can be represented by distinct nearest Z^4 points, so this is uniform in T. This does not re-prove all of YH or N2-exp'.
3. **S8-5, RF identity — CONFIRMED.** BFT_A.md:3503–3507: expand the product using Qd=d ev; the terms combine into `Q^(0->l)=Q_str^(0->l)-d sum ev h_i Q_str^(0->i)`. Applying `d*d f=8f-sum_neighbors f` gives RF with exactly the source's signs. The identity alone proves neither convergence to a nonzero spike nor the size of the residual terms.
4. **S8-6, TE transformation identity — CONFIRMED.** BFT_A.md:3510–3512: substitute `Lambda(x+d mu)=Lambda(x)-mu+I_chi mu` into the projection. The two bare mu terms cancel, leaving `d ev I_chi mu`. For mu=a delta_root this is a d ev chi_X. Its norm needs the separate endpoint qualification B4.
5. **S8-10, RC projection and sign — CONFIRMED.** BFT_A.md:3537–3547: Pi_E annihilates gauge directions in G_0 and sigma(Pi_E x) is such a direction. Therefore applying Pi_E to Pi_sharp x returns Pi_E x; applying Pi_sharp twice returns Pi_sharp x. Its kernel is G_0 and its range intersects G_0 trivially. Pairing the added **plus** Xi sigma with S gives **plus** n²<D(S),sigma>. A bound on the difference of two responses is not a lower bound on either separately; the review correctly demands that extra qualification.
6. **S8-11, PW-E bootstrap — CONFIRMED as a conditional implication, not vacuity.** BFT_A.md:3554–3578: a coarse cell has 4L^(4(k-l)) links, each own value is L^(-(k-l)) times its coarse value, so an n^(-2) coarse bound contributes `4 L^(k-3l)`. The finite-system inequality M<=A+M/2 gives M<=2A. A c^4-fold cover's l¹ norm divides by c^4 upon descent, cancelling the c^4 translated sources. GE-T, weighted EP-rec and the response/decomposition inputs remain hypotheses; failure to prove GE-T does not make this implication empty.
7. **S8-14, verdict arithmetic on the printed table — CONFIRMED, execution NOT-VERIFIED.** BFT_A.md:3660–3670: 0.2303/0.0287=329/41, above 4; 0.2303>2·0.0822=0.1644. The F6 inequality 0>0.5·0.2303 is false. A large ratio of two near-zero values cannot pass the second F3 size clause unless the reference threshold also collapses.

### FLOW confirmations

1. **S13-5, root-sector decoupling — CONFIRMED.** FLOW.md:4665–4673: diagonal conjugation multiplies E_ij by its character t_i/t_j. Equivariance forces every matrix element between unequal characters to vanish. A real-linear map's conjugate-root mixing also vanishes because that character is different. The neutral Cartan subspace is separate; this does not prove its determinant contribution is harmless.
2. **S13-8, the Lagrange repair — CONFIRMED.** FLOW.md:4671–4683 and 3009–3012: stationarity of `sum Re(e^(-i phi_k)m_k)` under sum phi=0 forces Im r_k to be independent of k. Thus `avg N-avg Nbar=2i(Im r_i-Im r_j)=0`. Substitution into the displayed derivative formula gives exactly the missing covariance coefficient 1. This proof does not use the review's toy floating-point optimizer. The S4' half follows from `g(z)(1-e^(-z))=z`; its first-order expansion uses f(z)=1-z/2+O(z²), g(z)=1+z/2+O(z²), yielding the stated covariance term.
3. **S13-6, SLICE-U(a) — CONFIRMED.** FLOW.md:4693–4698: expanding `(Q_m-D_(m+1)h_m)(Q^m-D_m h^m)` produces two opposite `D_(m+1)h_m D_m h^m` terms; the remainder is `Q_m Q^m-D_(m+1)(ev h^m+h_m Q^m)`. Multiplication by P_n kills D_n. Differentiating the finite gauge-covariance identity gives TD=D' ev at every background in the map's domain, as explicitly stated at 3738. No Cartan restriction is needed for this algebra.
4. **S13-7, U=1 versus expansion about U=1 — CONFIRMED.** FLOW.md:4709–4718: differentiating P(U)D(U)=0 gives P_1D_0=-P_0D_1. The positive term P_1(1-P_0)C_0(1-P_0)P_1 is a coefficient with **two** derivatives, not the value at epsilon=0. It equals P_0D_1G D_1^*P_0. Its growth does not refute the flat projected identity. The separate PROOF.md input-map interpretation was not checked.
5. **S13-20, local oddness and plane-wave form factor — CONFIRMED on the small lift; F5 limits the exact global claim.** FLOW.md:4642–4656: uniqueness makes the maximizer diagonal; conjugation sends a to -a and phi to -phi, eliminating its quadratic term. Averaging the transverse phase gives a geometric sum `sin(Lp/2)/sin(p/2)`, the within-block path average vanishes by the symmetric first-coordinate average, and telescoping gives `sin(L^m p/2)/sin(p/2)`. The bound |sin x|<=|x| and |sin(P/2)|>=|P|/pi gives rho_i<=(pi/2)L^(-i).
6. **S13-21 and S13-23(b), the local norm/Cauchy mechanism — CONFIRMED with its local domain.** FLOW.md:4699–4708, 4741–4748: a finite analytic matrix perturbation vanishing at zero is O(eta); finite incidence bounds its operator norm. `L^(-1)+C eta<=L^(-1) exp(LC eta)`. Multiplying levels costs `exp(LC R sum rho_i)`, with `sum rho_i<=pi/(2(L-1))`. Holomorphic extension of the adjoint is Q(conj epsilon)^*, so Cauchy's coefficient bound is valid and gives L^(-i) or L^(-2i). Constants must be chosen on one neighborhood where the local Hessians stay invertible, as supplied in F2.
7. **S13-23(c), P-poles — CONFIRMED on sectors avoiding zero.** FLOW.md:4749–4758: expand `(Delta_0+E)^(-1)=Delta_0^(-1)-Delta_0^(-1)E Delta_0^(-1)+...` to order r. There are at most r+1 inverse factors and each momentum shift is at most rP. Multiplication by N_r clears them. At first order the three projector derivatives have denominators lambda(K), lambda(K+P), or their product. This re-derives the specified two-factor normalization, independently of B4's finite differences.

### F6 — S13-3's “Schur formula slip” assumes two local C(K)'s are the same

**REFUTED** as a demonstrated mathematical error. Attachments: REVIEW_FLOW_S13.md:168–171 and binding fix 9; FLOW.md:4280–4283 versus 4781–4782.

The earlier tag says only that Y_VT is bounded and calls the total Schur subtraction C(K). It does **not** define that C(K) as a bound on |Y_VT|. The later proof explicitly defines its own C(K) by |Y_VT|<=C(K). Both formulas are valid with **C_tag(K)=kappa C_cross(K)²**. Reusing one letter without a definition is poor notation, but it is not evidence that factors were dropped. The ordered replacement is a permissible clarification if accompanied by that definition; it is not a proven correction to a false bound. This is a symbol-collision false alarm made by the reviewer itself.

One additional exact reporting correction, attached to REVIEW_FLOW_S13.md:89 and the S13-8 sentence “Im r_k agree to 1e-10”: the printed values (-1.78160e-4, -1.78231e-4, -1.78145e-4) have spread **8.6e-8**, not <=1e-10. **REFUTED** as printed arithmetic; the exact Lagrange proof above is unaffected. No optimizer was re-run.

## Verdict inventory and ordered-fix disposition

Original vocabulary is quoted faithfully below, including NARROWED, WRONG and CONFIRMED-WITH-FIX. Our verdict column uses only the owner's three review statuses. Repeated summary-table claims are mapped to their finding IDs rather than counted again. Split rows distinguish mathematics, execution evidence, and sufficiency of a proposed fix. “CONFIRMED” on an algebraic implication means the implication with its stated inputs, not independent establishment of those inputs.

### REVIEW_SQ_S4 inventory

| Review atom | Original verdict / order | Re-review verdict | Source attachment and disposition |
|---|---|---|---|
| SQ-1a | S4-1 CONFIRMED byte count | CONFIRMED | SQ.md:1295–1369 is 7853 bytes, independently counted from that range. No temporal conclusion follows. |
| SQ-1b | S4-1 CONFIRMED self-report; NOT-VERIFIED file times | NOT-VERIFIED | SQ.md:1297,1370 supply declarations, not independently recoverable edit order. Logs and historical filesystem evidence not read. |
| SQ-2 | S4-2 all sixteen fixes faithfully applied | NOT-VERIFIED | Current tags at SQ.md:827,912,1019,1028,1057,1075,1115,1134,1137,1164,1166,1193,1207,1217,1236,1253,1275,1287 cover the named IDs; fidelity to unread REVIEW_SQ_S3 is not certified. |
| SQ-3a | S4-3 missing smallness hypothesis | CONFIRMED | SQ.md:1388–1390,1467–1470; SU(2) central witness, Q3. |
| SQ-3b | S4-3 binding 1/4 repair; harmless at every use | REFUTED | Q3: SU(32) passes this repair; EPS-0a lacks the Wilson-energy premise used to discharge it. |
| SQ-4 | S4-4 NARROWED, order “PROVEN ... modulo bookkeeping”; keep counted | REFUTED | SQ.md:1458–1506 has an unresolved sector/proof issue; appending “modulo” does not make it PROVEN. Use GAP/CONDITIONAL until repaired. Uncomputed constants alone would not invalidate an existence proof. |
| SQ-5 | S4-5 CONFIRMED averaged-to-pointwise architecture | CONFIRMED | Exponent and reflection calculation above; implication conditional on EPS-T. |
| SQ-6 | S4-6 CONFIRMED-WITH-FIX, R_0=128, C_T>=16384 | REFUTED | Q2; 64 is usable, actual stopping supremum 256 for R>=128, not 16384. |
| SQ-7a | S4-7 NREFL CONFIRMED | CONFIRMED | SQ.md:1401–1415; crossing-face cancellation and 16 images. |
| SQ-7b | S4-7 BIA proof CONFIRMED | REFUTED | Q6 refutes its at-most-two-factor assertion; the O(epsilon²) theorem survives a four-factor repair. |
| SQ-7c | S4-7 WB CONFIRMED | CONFIRMED | SQ.md:1431–1443; nearest-neighbor support and flat cancellation imply a local O(eta) error. Numerical locality certification remains excluded. |
| SQ-7d | S4-7 SOB CONFIRMED, C_S=3,C_SP=81 | CONFIRMED | SQ.md:1445–1456; constants re-derived above. |
| SQ-8 | S4-8 TPL/N1/N2 CONFIRMED | CONFIRMED | SQ.md:402–406,1528–1549; exact tensor-kernel argument above. |
| SQ-9 | S4-9 STOKES-avg CONFIRMED | CONFIRMED | SQ.md:1537–1543; local-error collection independently checked. |
| SQ-10 | S4-10 LEV-E CONFIRMED | CONFIRMED | SQ.md:1552–1563; nonmultiplicative induction above. |
| SQ-11 | S4-11 LOC-T CONFIRMED | CONFIRMED | SQ.md:1078–1094,1571–1582; local cancellation and distance sum. |
| SQ-12 | S4-12 CARL mechanism CONFIRMED | CONFIRMED | SQ.md:1584–1598; geometric existence bound, not a fully evaluated theta_G. |
| SQ-13 | S4-13 GARSIA/EPS-0b-avg CONFIRMED | CONFIRMED | SQ.md:1600–1613; conditional moment proof and the safe link-sum bound. The downstream EPS-0 conclusion still inherits Q3. |
| SQ-14a | S4-14 theta_0 collision; binding rename | CONFIRMED | SQ.md:188 and 1622 remain distinct definitions under the same name. Rename has not occurred. |
| SQ-14b | S4-14 numerical thresholds and binding entry | REFUTED | Q1/Q4: no binding minimum or approximate eta_flat/t_pr delivered. The envelope substitution also changes an inequality's direction. |
| SQ-15a | S4-15 min-form and c_pr unchanged | CONFIRMED | SQ.md:294–319: c_pr=1/(640·53²)=1/1797760 and t_pr=C' tau_flat are exact algebra. |
| SQ-15b | S4-15 all HW/RLARGE clauses match | NOT-VERIFIED | External consumers were not read; no current consumer status or full theorem delivery certified. |
| SQ-16a | S4-16 constants unresolved; order quantify or condition | CONFIRMED | SQ.md:1459,1624,1634 leaves C_T uncomputed. A complete threshold calculation or explicit conditional delivery is necessary. |
| SQ-16b | S4-16 single iff C_D<=6.7e15 / only C_T live | REFUTED | Q4: necessary bound only, missing square root, epsilon_* and all other minima remain live. |
| SQ-17a | S4-17 polar factor can fail; quaternion repair | CONFIRMED | SQ.md:1703–1709; exact near-identity witness and projection proof in Q5. |
| SQ-17b | S4-17 “only on the quaternion line” | REFUTED | Q5: diag(2,1) is a non-quaternion counterexample to necessity. |
| SQ-17c | S4-17 recorded residuals/PASSes and reversal of S3 | NOT-VERIFIED | SQ.md:1701–1709 reports them; scripts, output and S3 review not read. |
| SQ-18a | S4-18 face-start d-intertwining with SQ's Q_2 is false | CONFIRMED | SQ.md:402–406,1717–1722. On a finite patch take only a_2(x)=x_1 x_2. The face-start coarse curl is L²[LX_2+(L-1)/2]: the transverse x_1 average shifts by L, while the longitudinal line has mean LX_2+(L-1)/2. The tent/Stokes average of da=x_2 is L²[LX_2+L-1], since its in-plane tent mean is LX_2+L-1. Their difference is L²(L-1)/2, nonzero. Embed the patch in a larger torus if needed. The correct all-starts averaged-lines operator telescopes around each square. |
| SQ-18b | S4-18 error in criterion, not merely script; no pre-registered valid test | NOT-VERIFIED | Criterion/script contents and chronology are outside the read set. The mathematical distinction is verified; the attribution is not. |
| SQ-19a | S4-19 side-3 locality test is blind; recommend side>=9 | CONFIRMED | REVIEW_SQ_S4.md:450–464 quotes the side. On that domain every periodic coordinate distance<=1, so all N_1,N_2,N_3 are global. Side>=9 permits an outside-support control; no rerun performed here. |
| SQ-19b | S4-19 W1/W2/R1/T1/G1 execution and process clean | NOT-VERIFIED | SQ.md:1711–1724 is only a report; implementation/lock evidence not read. |
| SQ-20 | S4-20 CVX-K not needed | CONFIRMED | SQ.md:1620–1639,1675–1697; dependency inspection above. |
| SQ-21 | S4-21 LU-ex CONFIRMED-WITH-FIX; sector/epsilon_U/import disclosures | NOT-VERIFIED | SQ.md:1646–1685: flow compactness yields a critical subsequence without Lojasiewicz, and open/closed continuation is valid if GAP and the stated Hessian bound hold. Imported reflection/Hessian inputs and numerical epsilon_U were not independently established. Sector discharge must use Q3's corrected condition. |
| SQ-22 | S4-22 withdraw BFT requirements (1),(3),(4) | NOT-VERIFIED | SQ.md:1244–1256 still contains the request. Withdrawal is conditional on an actually repaired EPS-T/EPS-0 chain; do not bank closure from the present labels. Item (5), Holder estimates and uniqueness remain separate. |
| SQ-M1 | M4-1 order §15.6 -> §15.5 | CONFIRMED | SQ.md:1277 points to §15.6; the q4b section is §15.5 at 1700. This correction remains unapplied. |
| SQ-M5 | M4-5 add level-0 smallness threshold | CONFIRMED | SQ.md:1115–1117,1622: add 1.6 sqrt(N kappa_+) theta_REG<tau_0, plus Q3's sector threshold; do not justify it by a historical numeric comparison. |
| SQ-M6 | M4-6 say “conservatively” for link count | CONFIRMED | SQ.md:1611–1613 counts at most 16n^4 links. The sum estimate is safe; exact equality for actual free-boundary links is not asserted here. |
| SQ-M8 | M4-8 hypothesis fix does not trigger reopening | NOT-VERIFIED | SQ.md:1748–1749; the original one-line fix is insufficient (Q3), so retaining all old statuses cannot be certified. |

M4-2/M4-3 are covered by SQ-6; M4-4 by SQ-14a; M4-7 by SQ-5. Binding fixes 1–10 at REVIEW_SQ_S4.md:595–624 map respectively to SQ-3, SQ-16, SQ-14, SQ-22, SQ-18, SQ-17, SQ-4, SQ-6, the M rows, and SQ-19a. The “FOR OTHER FILES” orders require the same corrected minima and conditional statuses; their target files were not edited or read. The summary's EPS-T/EPS-0/REG-min/PRICE-iii/DESC-epsilon/CLS-min labels inherit Q3/Q4; LU-ex/GS/LU-ap/GAP inherit SQ-21. The old 14/1/2 tally is **NOT-VERIFIED**, not a retained count.

### REVIEW_BFT_A_S8 inventory

| Review atom | Original verdict / order | Re-review verdict | Source attachment and disposition |
|---|---|---|---|
| BFT-1a | S8-1 provenance CONFIRMED-WITH-FIX | NOT-VERIFIED | BFT_A.md:3273–3285,3647–3653: old hashes/logs unavailable within scope. |
| BFT-1b | S8-1 unchanged birth time implies every edit was an append | REFUTED | REVIEW_BFT_A_S8.md:23 and BFT_A.md:3647–3653. Replacing an interior character preserves birth time and can preserve byte length; appending afterward also preserves both recorded prefix-length checkpoints. The implication is invalid even if the historical edit order happened to be correct. |
| BFT-2 | S8-2 eight prior fixes faithful | NOT-VERIFIED | BFT_A.md:3373–3441 contains P7-1..P7-8; faithfulness to unread S7 and its source proofs not certified. |
| BFT-3 | S8-3 DF CONFIRMED | CONFIRMED | BFT_A.md:3465–3477; algebraic implication re-derived above. |
| BFT-4 | S8-4 PW-cc CONFIRMED, uniform k,T | CONFIRMED | BFT_A.md:3481–3498; exponents and fixed-parameter uniformity conditional on the named YH/data estimates. P8-2's explicit dependence/no-current clarification is valid. |
| BFT-5a | S8-5 RF exact CONFIRMED | CONFIRMED | BFT_A.md:3503–3507; operator identity re-derived. |
| BFT-5b | S8-5 RF implies nonzero limiting Y^p spike | NOT-VERIFIED | RF also contains neighbor and residual terms. Their required bounds for actual Y^p are not supplied by the identity. |
| BFT-6a | S8-6 TE identity CONFIRMED | CONFIRMED | BFT_A.md:3510–3512; gauge substitution. |
| BFT-6b | S8-6 size exactly 8L^(3(k-l)) | REFUTED | B4: T=1 gives zero. |
| BFT-6c | S8-6 no positive proof depends on TE size/FS | CONFIRMED | BFT_A.md:3465–3578 separates the algebraic results and conditional PW-E from the size/refutation claims. |
| BFT-7a | S8-7 withdraw psi_u=level-0 spike | CONFIRMED | BFT_A.md:3291–3294,3582–3585 defines a path functional and a divergence functional, respectively; B3's exact curl example has d*u=0 but psi nonzero. |
| BFT-7b | S8-7 exact first two coefficients and psi_2 | CONFIRMED | B3 re-derived them with Fractions and finite incidence counts. |
| BFT-7c | S8-7 GE-T false | NOT-VERIFIED | B1/B3: the infinite funnel tail is now resolved for this witness; the S_E projection/no-cancellation estimate is not. |
| BFT-7d | S8-7/P8-9 refutation is already proved | REFUTED | B1: finite-depth evidence and two explicitly unproved estimates were promoted to a theorem. |
| BFT-7e | geometric higher tail / every finite truncation leaves remainder | REFUTED | B3: the exhibited compact curl has phi_i=0 for i>=3. No such conclusion for the distinct Green field follows from it. |
| BFT-7f | the gradient test certifies the funnel functional | REFUTED | REVIEW_BFT_A_S8.md:244–245,385–386: h(d lambda)=mean(lambda)-lambda(root) cannot determine h on co-closed inputs; see B6 below. The independently rebuilt coefficients in B3 do survive. |
| BFT-8 | S8-8/P8-3 transport estimate supplied, sound | REFUTED | B5: partition unity provides no bound on harmonic-potential differences. The transport itself remains NOT-VERIFIED. |
| BFT-9a | S8-9 spike threshold exponent | CONFIRMED | BFT_A.md:3532–3535: if a fixed positive spike exists, 8 abs(sp)<=C_P L^(k-3l) fails for l>k/3+constant. Conditional arithmetic only. |
| BFT-9b | P8-4 exact psi values +/-1/54 | REFUTED | B3: those are phi_1; psi_k for k>=2 is +/-130/6561 on the stated unnormalized sources. |
| BFT-9c | S8-9 six-decimal zero cannot certify 1e-10 | CONFIRMED | BFT_A.md:3530,3662 distinguishes “exact” from “to print precision”; a displayed zero only bounds rounding error by about 5e-7. One nonzero offset still rejects universal vanishing. |
| BFT-10a | S8-10 RC projection and response sign | CONFIRMED | BFT_A.md:3537–3547; algebra above. |
| BFT-10b | P8-7 response difference does not bound f^E itself | CONFIRMED | BFT_A.md:3548–3552,3601: f_sharp-f_E large does not identify which response is large. A bound on f_sharp is missing. |
| BFT-10c | P8-7 C0# data are not a Pi_E test; “not yet a slice” wording | CONFIRMED | BFT_A.md:3664–3670,3684 explicitly uses S_C0 and says S_E was not computed; RC gives an algebraic slice, with configuration compatibility still OPEN. |
| BFT-11 | S8-11 PW-E implication and ARGUED-input label | CONFIRMED | BFT_A.md:3459–3462,3554–3578; conditional bootstrap above. External “no quiet downstream use” survey is not certified. |
| BFT-12 | S8-12/P8-6 SR vacuous; replacement template | REFUTED | B2: GE-T failure does not imply PW-i failure; PW-i alone does not imply SR. |
| BFT-13a | S8-13 no factor-k closure or remainder bound | CONFIRMED | BFT_A.md:3615–3620,3724–3728 explicitly retains these obligations. |
| BFT-13b | S8-13 PW-ii fails in S_E by same mechanism | NOT-VERIFIED | BFT_A.md:3619–3620 relies on the same unproved Y^p spike transfer. |
| BFT-14 | S8-14 printed F3/F6 verdict arithmetic | CONFIRMED | BFT_A.md:3660–3670; rational inequalities above. Criteria chronology and execution remain unverified. |
| BFT-15 | S8-15/P8-5 three undisclosed F6 YES lines | NOT-VERIFIED | Those are in unread output. If recovered, report them with their true criterion scope; the present source contains only the decisive-offset result. |
| BFT-16a | S8-16 E4 cannot certify the norm bound | CONFIRMED | BFT_A.md:3499,3663: each random pairing is a lower bound on a supremum, so small samples cannot establish its uniform upper bound. They are informational only. |
| BFT-16b | S8-16/P8-6 three planned j versus one | NOT-VERIFIED | Requires unread criteria and script. |
| BFT-17 | S8-17 reproduction NOT-VERIFIED | NOT-VERIFIED | No floating-point run or script/path audit performed here. |
| BFT-18 | S8-18 downstream rate survey CONFIRMED | NOT-VERIFIED | BFT_A.md:3622–3640 reports outside consumers, whose units, selectable scales and thresholds were not re-read. The ceiling m_Y<=log(2)/4160 follows, but does not certify the survey. |

P8-1: **NOT-VERIFIED** as a criterion/script deviation; source BFT_A.md:3479 does report (k,T)=(3,1). P8-2: **CONFIRMED** as a local clarification, via BFT-4. P8-3: inadequate, BFT-8. P8-4: split BFT-9b/9c; its exact source-functional zeros do not by themselves prove zeros for the distinct S_C0 Green-function field. P8-5: unverified, BFT-15. P8-6: its central template/vacuity order is refuted (BFT-12); the scope/remainder cautions are valid (BFT-13a/16a); script-count attribution is unverified (BFT-16b). P8-7: the three qualifications are justified (BFT-10b/10c). P8-8: carry the weighted EP-rec hypothesis as requested (BFT-11). P8-9: withdraw the mistaken functional identification (BFT-7a), retain the exact coefficients (BFT-7b), but do not promote the refutation (BFT-7c/7d); the cosmetic `N_b -> N_B` at BFT_A.md:3403 is **CONFIRMED** by its preceding definition. No mathematical status follows from an “essentially proven” label. The review's final five-candidate tally is only a list of conditional/algebraic candidates here.

### REVIEW_FLOW_S13 inventory

| Review atom | Original verdict / order | Re-review verdict | Source attachment and disposition |
|---|---|---|---|
| FLOW-1a | S13-1 session complete; count reconciliation | CONFIRMED | FLOW.md:4826–4842 dispositions X1–X6; 19/21 plus 9/10 is 28/31. This confirms internal arithmetic, not actual run counts. |
| FLOW-1b | S13-1 2.92 -> 2.89; orphan smoke numbers | NOT-VERIFIED | FLOW.md:4721–4722,4730 contains 2.92 and the smoke values. The claimed 2.8916 source output and missing-artifact history were not inspected. Drop unsupported values or recover the actual record; do not recreate evidence from the review's memory. |
| FLOW-2 | S13-2 provenance clean, reconstruction unavailable | NOT-VERIFIED | FLOW.md:4541,4785–4798 reports dates/hashes; no historical hash reconstruction or outside scratchpad search was done. Saving replacement scripts is sensible; hashes and pair counts alone cannot reconstruct their bytes. |
| FLOW-3a | S13-3 all nine earlier fixes faithful | NOT-VERIFIED | Current RFL12-fix tags exist in cited regions; full faithfulness requires the excluded S12 review. |
| FLOW-3b | S13-3 Schur formula “drops kappa and square” | REFUTED | F6: C_tag and C_cross have not been defined identically. Rename/define them instead of asserting a dropped factor. |
| FLOW-4a | S13-4 Cartan restriction matches target, cite it | CONFIRMED | FLOW.md:3835 defines the constant-flux target; 4470–4483 leaves the plane-wave/constant-flux exchange T-c OPEN. This is useful local progress with an explicit remaining bridge. |
| FLOW-4b | S13-4 neutral Cartan sector carries no universal content | NOT-VERIFIED | FLOW.md:1968–1974 asserts this scope; its complete determinant/logarithmic-coefficient argument was not rebuilt here. Do not infer it from root decoupling alone. |
| FLOW-5 | S13-5 root-sector diagonalisation | CONFIRMED | FLOW.md:4665–4673; torus-character argument above. |
| FLOW-6 | S13-6 general-background SLICE-U(a), ordered citation | CONFIRMED | FLOW.md:3738,4693–4698; differentiation of covariance and cancellation above. |
| FLOW-7 | S13-7 no failure of flat decomposition | CONFIRMED | FLOW.md:4709–4718; derivative coefficient is not the value at U=1. PROOF.md citation remains unverified. |
| FLOW-8a | S13-8 missing Lagrange step and ordered repair | CONFIRMED | FLOW.md:3009–3012,4679–4683; exact algebra above. |
| FLOW-8b | S13-8 numerical Im r agreement <=1e-10 | REFUTED | Printed spread is 8.6e-8, F6. Exact covariance theorem unaffected. |
| FLOW-9 | S13-9 WRONG §30(C3), change to §37 | CONFIRMED | FLOW.md:4645 points to §30; conjugation (C3) is at 1923 in §37. It remains uncorrected. |
| FLOW-10a | S13-10 carry scope/hypotheses into heading and tally | CONFIRMED | FLOW.md:4733–4736,4831,4847–4850 inconsistently displays its own hypothesis. Make the derivation/scope explicit; F2 discharges the particular local Hessian premise. |
| FLOW-10b | binding fix 3 puts P-poles under Pi-loc too | REFUTED | FLOW.md:4749–4758 never uses Pi. The review itself calls P-poles unconditional at lines 627 and 683. Separate its label from VC-T1. |
| FLOW-11 | S13-11 Pi-loc locality/analyticity unargued | REFUTED | F2: direct-sum local Hessian and analytic maximizer give these clauses. |
| FLOW-12a | S13-12 normalization degree 12/30 is conservative | CONFIRMED | FLOW.md:4603–4608; degree=2(r+1)(2r+1). A sharper denominator must be derived for its specified entries, not inferred from test data. |
| FLOW-12b | S13-12 permits abs(K)^(-30) | REFUTED | F3: generic fixed-P power 12 at r=2; commensurate P=pi power 36; simultaneous-soft power 60. |
| FLOW-13a | S13-13 historical FAIL/PASS reports honest | NOT-VERIFIED | FLOW.md:4800–4815 reports them candidly; artifacts/implementation not read. |
| FLOW-13b | S13-13 ordered “predetermined FAIL” diagnosis | REFUTED | F1: O(delta^4) has no positive lower coefficient. |
| FLOW-13c | S13-13 B4 scaling supports truncation; B3 scaling untested | CONFIRMED | On the review's printed B4 numbers, ratios are 1220000/121 and 440/3. B3's smaller values sit at the stated floor. This is conditional arithmetic/diagnostic evidence, not exactness or a reproduced run. |
| FLOW-14 | S13-14 0.5 -> 0.6 unlogged relaxation | NOT-VERIFIED | FLOW.md:4622 has 0.5; the later 0.6 criterion and log omission require excluded files. If true it is a 20% relaxation and both quoted ratios still pass 0.5. |
| FLOW-15 | S13-15 probe is thin and not proof-bearing | CONFIRMED | FLOW.md:4793,4820–4822: (3,3,1,1) and K_1!=0 gives six sectors with lambda in {3,6}; one depth ratio cannot establish a rate. The analytic bound above supplies the proof mechanism. |
| FLOW-16a | S13-16 Schur upper bound | CONFIRMED | FLOW.md:4777–4782; subtract at most kappa C_cross² and require positive denominator for the large-n estimate. |
| FLOW-16b | S13-16 only upper bound needed; delete lower-bound sentence | REFUTED | F4: fast convergence is not excluded by O(1/n). Supply Y_VV=O(n), as derived here for S4', and retain the resulting lower bound. |
| FLOW-17 | S13-17 actual 1.03 GB breach | NOT-VERIFIED | FLOW.md:4791 discloses it; actual RSS/log/process compliance not independently inspected. The reported decimal 1.03 GB exceeds a decimal 1 GB ceiling if those are the governing units. |
| FLOW-18 | S13-18 P_n result extends to each level k | CONFIRMED | FLOW.md:4737–4740,4749–4758: the finite-dimensional sector formula is level-independent once expressed in that level's coordinates. Keep the avoiding-zero hypothesis. |
| FLOW-19 | S13-19 f16 reproducibility NOT-VERIFIED | NOT-VERIFIED | No f16 execution or script read; no reproducibility PASS claimed. |
| FLOW-20a | S13-20 oddness/second-order form factor | CONFIRMED | FLOW.md:4642–4656; identity-neighborhood proof above. |
| FLOW-20b | S13-20 exact S4' identity on all of D' | REFUTED | F5: identity links with a wrapped Cartan lift give Q_root a=2pi/27 on the selected coarse link. |
| FLOW-21 | S13-21 SLICE-U(b),(c) | CONFIRMED | FLOW.md:4699–4708; local analytic construction and finite-incidence norm estimate, with a sufficiently small local domain. |
| FLOW-22 | S13-22 move forward reference out of proof | CONFIRMED | FLOW.md:4717–4718 refers to §107, whose proof uses §106(a),(c), not (d). No circularity; relocation is editorial. |
| FLOW-23 | S13-23 coefficient expansion/P-poles/conditional convergence | CONFIRMED | FLOW.md:4737–4763; jets of order<=2, geometric product bound and inverse-series algebra re-derived above. Global exact-lift wording and optimized infrared bounds are separate. |

Binding fixes 1–11 at REVIEW_FLOW_S13.md:636–675 are all dispositioned: (1) FLOW-1b; (2) FLOW-8a; (3) FLOW-10a/10b/11; (4) FLOW-4a/4b; (5) FLOW-6; (6) FLOW-12a/12b; (7) FLOW-13b/13c, with the worse quoted B3 eigenvalue unverified against raw output; (8) FLOW-14; (9) FLOW-9/3b/16b/22, including adding the existing §108 result to Outcomes; (10) FLOW-2; (11) FLOW-15/17. The proposed larger/small-momentum/SU(3) probe is a sensible future discrimination test, not work executed here. The claimed 75 and strict 70 are arithmetic tallies built on an unread earlier 70/66 and incompletely qualified statements, hence **NOT-VERIFIED** as mathematical status counts. T-a1-M, T-a3, T-b and T-c remain OPEN in the read source; the corrected local results do not close them.

### B6 — A gradient-only test cannot identify a funnel on the co-closed counterexample

**REFUTED** as a sufficient certification argument. Attachments: REVIEW_BFT_A_S8.md:244–245 and 385–386 (`So the code's funnel is the object ...`); the target input is defined at BFT_A.md:3307–3313.

Let u=d*delta_p and replace the tested functional by `h_tilde(v)=h(v)+alpha <u,v>` at the tested root. For every lambda, `<u,d lambda>=<delta_p,dd lambda>=0`. Thus h_tilde passes **every** gradient identity `h(d lambda)=mean(lambda)-lambda(root)` exactly, for every alpha. But `h_tilde(u)-h(u)=alpha ||u||²`, nonzero for alpha!=0. The advertised check is blind precisely to the co-closed input used for the refutation. This does not refute the coefficients: B3 derives them from the full signed-path definition instead. A decisive test must also probe the complementary input space, or verify every path coefficient.

## Systemic audit: symbols, quantifiers, and discriminating checks

### Symbol register and stale quantifiers

| Object | Current source anchors | Consequence |
|---|---|---|
| theta_SUP versus theta_REG | SQ.md:188 versus 1622; both enter 318–319/1633 | The unexecuted rename is necessary; neither a shared spelling nor an upper ceiling identifies the active minimum. |
| C_D | SQ.md:145–146 versus output formula 1634 | A calculation at historical input C_D=2 cannot be reused after C_D depends on C_T. |
| C_1 | SQ.md:190 (SUP-price value 160), 1487 (Moser constant), 1587 (CARL coefficient) | These are different constants. Q1 uses the CARL value only; Q4 uses SUP-price's full formula. No cross-comparison by name is accepted. |
| q_transport versus q_source | SQ.md:1096–1099 versus 1459/1621 | The contraction ratio is <1; the integrability exponent is >4 and then chosen as 8. The summation and moment bounds use different objects. |
| phi_i, Phi_l, psi_u, sp_l | BFT_A.md:3291–3294,3307–3309 | A single funnel term, a partial sum, the top funnel, and a representative's divergence are not interchangeable. B3 repairs both a symbol mistake and an unsupported asymptotic extrapolation. |
| C_tag(K) versus C_cross(K) | FLOW.md:4283 versus 4781–4782 | The former may bound the whole Schur subtraction; the latter bounds a cross entry. F6's definition C_tag=kappa C_cross² reconciles them. |
| Pi(M) versus P_n(U) | FLOW.md:1452–1456 versus 4602–4605/4749 | Pi is the local maximizer Hessian; P is the transverse projector. P-poles does not acquire a Pi-loc hypothesis from its neighbor. |
| lambda-degree versus momentum power | FLOW.md:4603–4608 | Each soft lambda contributes two momentum powers. Which shifted factors vanish depends on the path to the infrared limit. |

The comparison `epsilon_1<t_pr` remains a **CONDITIONAL** consumer test, not a numerical delivery. Neither epsilon_* nor the Moser constant has the evaluated bound needed to close all its minima in the permitted source. BFT's k-uniform refutation cannot be certified by k=2 alone, and its T>=1 exact-size claim must include the collapsed T=1 torus. FLOW's local analytic expansion must not silently quantify over wrapped Cartan lifts. A 1/n upper bound does not exclude the much faster L^(-2n) rate.

### Could the cited check fail for the right reason?

All implementation and execution verdicts below are **NOT-VERIFIED**: the scripts and raw outputs are outside the read budget. This is a design audit of the gates as stated in the permitted text, with algebraic witnesses where possible. A printed PASS never substitutes for a proof.

| Check family and source | Discrimination audit |
|---|---|
| SQ q4b P0 and K1–K6; REVIEW_SQ_S4.md:404–422, SQ.md:1700–1709 | P0 can fail: Q5 supplies a nonstationary polar output. Objective-value accuracy is second order in stationarity error and therefore K3 passing cannot establish P0. The individual K1/K2/K4/K5/K6 implementations and their independence are not specified sufficiently in these ranges; their PASS labels remain NOT-VERIFIED. |
| SQ review R1/R2/R3; REVIEW_SQ_S4.md:20–29 | R1 is replaced here by exact Q5. R2 can match all historical constant examples while missing a changed input/minimum; Q1/Q4 expose that failure. R3's byte arithmetic can fail and its 7853-byte equality survives; it cannot prove chronology or absence of in-place edits. |
| SQ q5 T1/T2/T2b; SQ.md:1711–1722 | T1 can reject wrong tent weights or composition. T2 separates face-start and all-starts maps: SQ-18a's a_2=x_1 x_2 is an exact rejecting input. Equal mass and constant-field checks cannot distinguish them. T2b is expressly post hoc; it does not retroactively alter T2's criterion. |
| SQ q5 W1/W2/W3/B1; REVIEW_SQ_S4.md:450–464 | W1 tests flat cancellation; W2 can detect covariance errors if its operator is independently constructed. W3/B1 at side 3 cannot test support outside N_2/N_3 because there are no such sites. Their global ratios can still fail, but do not decide locality. The literal BIA tree count fails Q6. |
| SQ q5 R1/G1; SQ.md:1714–1716 | R1 can reject a reflection that creates crossing curvature or changes norms. G1 can reject an incorrect finite-tree inequality on sampled adapted data; finitely many random cases do not establish the universal moment theorem. Its analytic proof is separately reconstructed above. |
| SQ failure modes S4-F1..F5; SQ.md:1363–1368 | F1 is addressed by the local WB cancellation, F2 by exact template sums, F3 by LEV-E's additive induction, F4 by the local funnel identity. Side-3 data cannot decide F1/F4 locality. F5 concerns the separate coercivity route; CVX-K's nonuse does not prove that coercivity claim. |
| BFT E1 / BA8-F1,F5; BFT_A.md:3353–3363 | An independently evaluated DF/RF residual can reject a wrong sign or transport. E1 explicitly replaces Gamma_E by the exact algebra it uses, so its passing cannot certify construction or bounds of the actual S_E projector. B6 gives a whole invisible family for the gradient-only h test. |
| BFT E2 / BA8-F3,F6; REVIEW_BFT_A_S8.md:391–409 | F3 has both a ratio and a size clause: zero/near-zero spikes cannot win by ratio alone at the quoted nonzero reference threshold. F6 must be evaluated at that F3 offset. The printed decisive numbers reject F6; symmetric-offset print-floor ratios are not another theorem. Finite-k spikes do not settle k-uniformity. |
| BFT E3 / BA8-F4; BFT_A.md:3530–3531 and REVIEW_BFT_A_S8.md:295–308 | One adequately resolved nonzero offset rejects universal cancellation. Six-decimal zeros cannot certify a 1e-10 all-offset condition. Exact zeros of psi for a curl source cannot certify zeros of epsilon=phi_1(y) for a different Green-function representative. |
| BFT E4 / BA8-F2; BFT_A.md:3364–3368,3499 | A random pairing gives a lower bound on a supremum, so a large sample could refute a specified upper bound. Small samples cannot certify it. The proof, not E4, must carry PW-cc. |
| BFT BA8-F7 / MR; BFT_A.md:3348–3358,3622–3640 | This comparison is meaningful only with a fixed rate unit, allowed scale choices, and a proved consumer requirement. Those outside consumers are not re-read here. A quoted upper ceiling on m_Y cannot alone decide every requirement. |
| FLOW f16 A1 / S13-F1; FLOW.md:4612–4617 | Exact-map, off-diagonal, oddness, and cubic-ratio tests can reject distinct errors. Small-lift samples cannot test the wrapped-lift quantifier; F5 passes D' while falsifying the all-lift formula. A cubic ratio also needs a nonzero resolved denominator. |
| FLOW f16 A2/A3 / S13-F2; FLOW.md:4614–4617 | Comparing independently computed nonlinear-map derivatives to the closed formula can reject incorrect root weights. The proposed weight=1 negative control can distinguish them on the chosen nontrivial field; it is not guaranteed to reject at zero field. Covariance identities alone cannot certify all matrix entries, and the two-half-scale ratio needs a resolved difference. Implementation independence remains NOT-VERIFIED. |
| FLOW f16 B1 / S13-F3; FLOW.md:4620–4622 | Product-composition and projection identities can reject an independently implemented recursion. If the compared side is merely defined from that same identity the check is circular; script inspection would be needed to exclude this. Either way it does not test convergence or the longitudinal Schur lower bound. |
| FLOW f16 B2 / S13-F4; FLOW.md:4622–4623,4820–4822 | The specified ratios can pass or fail on a chosen nonzero pair of coefficients. One depth ratio at lambda>=3 has no sensitivity to small momentum, all depths, or SU(3) Part-B behavior. The alleged 0.5-to-0.6 relaxation is unverified from excluded criteria; both printed ratios pass the original gate. |
| FLOW f16 B3/B4 / S13-F5,F6; FLOW.md:4623–4625,4803–4815 | Both could pass: F1's exact linear Richardson control disproves predetermined failure. B4's printed scaling supports a truncation diagnosis only. B3 lacks that scaling evidence. A post-hoc smaller step is a new test, not a replacement pre-registration. An analytic P-poles derivation, not observed residual decay, establishes the identity. |
| FLOW reviewer toy maximizer; REVIEW_FLOW_S13.md:89–90,257–296 | Testing Im r_i equality can reject nonstationarity; its printed spread already fails the claimed 1e-10 agreement. The exact Lagrange derivation, not that optimizer output, repairs the proof. |

The strongest newly exposed blind gate is B6: even exact success on every gradient input leaves the entire co-closed component of the asserted funnel undetermined. The strongest false gate diagnosis is S13-13: a big-O upper bound was used as if it were a positive lower bound.

### Citation and scope audit

Located source statements by strings and checked the displayed current ranges. Key target anchors (SQ theta definitions and §§15.1–15.5; BFT §§36–40; FLOW §§103–110) still contain the cited subject matter. Confirmed specific mistakes: SQ.md:1277's §15.6 points to §15.5; FLOW.md:4645's §30(C3) points to §37(C3); REVIEW_SQ_S4's opening S4 item labels drift relative to its own body. These are specific mismatches, not a claim of uniform line drift.

The reviews' PROOF.md references (including FLOW's cited 6600–6660/6633/6637ff) are **NOT-VERIFIED**: checking them would exceed the two optional-file budget. The same applies to logs, criteria, scripts, previous reviews, BFT_B, LINEAR_PACKAGE, HW/RLARGE, and audit ledgers. No assertion about their current content, historical reproducibility, or applied downstream status is certified here. Only this deliverable was written; no target repair, git command, floating-point run, or external scientific-status update was performed.

## Summary table and hit rates

Counts below are the **unique split rows in the three verdict-inventory tables**, not the old reviews' theorem tallies. A repeated fix inherits its linked row and is not counted twice; standalone excluded-artifact checks mentioned in the mapping paragraphs are not additional counted atoms. This makes the denominator reproducible and avoids rewarding repeated headline claims. Each CONFIRMED row states the exact scope checked; conditional algebra is not counted as proof of its hypotheses.

| Review | CONFIRMED | REFUTED | NOT-VERIFIED | Total listed atoms | Hit rate among decided atoms | Confirmed / all listed atoms |
|---|---:|---:|---:|---:|---:|---:|
| REVIEW_SQ_S4 | 22 | 7 | 9 | 38 | 22/29 = **75.9%** | 22/38 = 57.9% |
| REVIEW_BFT_A_S8 | 16 | 8 | 9 | 33 | 16/24 = **66.7%** | 16/33 = 48.5% |
| REVIEW_FLOW_S13 | 17 | 8 | 8 | 33 | 17/25 = **68.0%** | 17/33 = 51.5% |
| Total | 55 | 23 | 26 | 104 | 55/78 = **70.5%** | 55/104 = 52.9% |

Coverage: every S4-1..S4-22, M4-1..M4-8 and SQ binding order 1..10 is dispositioned; every S8-1..S8-18 and P8-1..P8-9 is dispositioned; every S13-1..S13-23 and FLOW binding order 1..11 is dispositioned. The positive-check section independently derives nine SQ groups, seven BFT groups, and seven FLOW groups, exceeding five sampled confirmations per review. Historical script execution, provenance and outside dependencies receive NOT-VERIFIED rather than a guessed verdict. Exact-arithmetic recount found no missing main numbered item or duplicate inventory ID.

| Refuted number or numerical conclusion | Corrected result | Derivation / finding |
|---|---|---|
| SQ theta_G ceiling 1.46e-13 and tau_R ceiling 2.75e-15 used to identify a binding entry; eta_flat approximately 4.2e-36, t_pr approximately 1.5e-13 | No evaluated binding minimum. theta_REG=min(theta_G,epsilon_*/[(1336/25)2^(5/8)]), and DESC also retains theta_SUP. On the review's own C_T=16384 choice, t_pr<6e-22, tau_flat<6e-22/53, eta_flat<(6e-22)^2/(640·53^4). | Q1/Q4. The beta>=4.29e11 theta substitution is invalid; e=242.9 theta and LEV-E's 3.04e-13 describe a conservative envelope/choice. A conservative CARL envelope cutoff is 1/[8(A+sqrt(A²+B/4))], with the other conditions retained. |
| SQ's 1/4 neighborhood is sufficient for every SU(N) | It fails at N=32. A sufficient replacement is eta<=min(1/4,1/N), or an explicitly identity-centered SU(N) logarithm sector. | Q3: central element has eta=2sin(pi/32)<1/4 but P=0. |
| SQ requires R_0=128 instead of 64; stopping factor identified with 128² | R_0=64 works after absorbing its finite interval. For R>=128 the actual factor has supremum 256 (integer maximum 255), and equals 128 at R=128. The larger envelope has maximum 16384. | Q2: exact dyadic exponent. No necessary optimal C_T>=16384 follows. |
| SQ cube faces have at most two non-tree edges | Four in the listed tree gauge. | Q6: explicit z=1 face. |
| SQ 1/(3.31e7·6.7e-40)=6.7e15; this condition is iff | The reciprocal is 10^36/22177, approximately 4.509e31. Its square root is approximately 6.7e15; the corrected necessary condition is C_D<(2A epsilon_1)^(-1/2), with 16,532,779<A<16,532,781. | Q4: exact rational substitution and rational square-root enclosure. It remains insufficient to close the full minimum. |
| BFT psi=+/-1/54 | That is phi_1. For the stated unnormalized source and k>=2, psi=+/-130/6561; normalized negative witness gives -65/26244. | B3: integer path sums -36 and -204. |
| BFT 0.5% tail, approximately 7.5% remainder, every finite truncation nonzero | After phi_1 the exact remainder is (17/243)phi_1; after phi_2 it is zero for this witness, at every greater depth. | B3: opposite-edge cancellation gives Q_str^(n)u=0 for n>=9. This does not settle the different Y^p input. |
| BFT exact tent norm 8L^(3(k-l)) for the whole stated setting | Zero at T=1. | B4: the sole periodized partition function is identically 1. Larger T needs its own discrete sum. |
| FLOW Im r agreement <=1e-10 | Printed spread is 8.6e-8. | F6: subtract the printed extrema; exact stationarity theorem survives. |
| FLOW normalized bound allows a universal abs(K)^(-30) | At r=2: powers 12 for fixed generic P, 36 at P=pi e_2, 60 in a joint soft limit. At r=1: generic power 8, joint soft power 24. | F3: each soft lambda is quadratic in momentum. These are bound allowances, not actual poles. |
| FLOW delta=0.02 and O(delta^4) force failure against 1e-7 | delta^4=1/6,250,000, but c delta^4 passes for abs(c)<5/8, including c=0. | F1: exact linear Richardson control. B4's printed coefficient is 7625, giving the empirical requirement delta^4<1/76,250,000,000, not a pre-run impossibility theorem. |
| FLOW D' implies every abs(h_j delta)<pi/3 | Wrapped delta=2pi can have identity group element. The explicit identity-link witness has Q_root a=2pi/27 while its nonlinear output is identity. | F5: three out of 81 contour starts cross the chosen link; coefficient 1/27. |

Other rejected conclusions: the proposed SQ repair does not license retaining all old statuses; BFT's GE-T-to-SR template drops PW-ii, its transport proof lacks potential estimates, and its gradient gate cannot certify a co-closed funnel; FLOW's Pi-loc criticism misses the direct-sum Hessian, its P-poles label imports an unused hypothesis, and its W_n refutation needs the supplied lower bound. The apparent Schur-factor error is a symbol-definition ambiguity, not a demonstrated dropped factor.

**Single most dangerous unverified item:** the k-uniform bound/no-cancellation estimate for the **actual S_E projection of the compact curl witness**, BFT_A.md:3307–3313 and REVIEW_BFT_A_S8.md:258–264. Resolving the funnel tail does not resolve that projection. The old review used the claimed GE-T refutation to call PW/SR vacuous, despite also admitting that PW-i for the actual Y^p response was not refuted. Until the projection estimate and the distinct response bridge are proved, that downstream exclusion remains **ARGUED/GAP**, not PROVEN. No verdict here declares GE-T true.

Completion: 2026-10-28 UTC. This report is the deliverable; source-side fixes and downstream audit actions are outside this assignment.

Final verification: plain-Python exact arithmetic independently reproduced phi_1=-1/54, phi_2=-17/13122 and phi_3=0; checked the face/all-starts witness (9 versus 18 at L=3), C_err's symbolic coefficients and rational enclosure, the conditional C_D/t_pr bounds, the reciprocal, and the stationarity spread. The inventory recount is 104 unique rows: 55 CONFIRMED, 23 REFUTED, 26 NOT-VERIFIED. These checks validate the stated local derivations and report arithmetic only; they do not turn excluded dependencies or historical runs into PASSes.
