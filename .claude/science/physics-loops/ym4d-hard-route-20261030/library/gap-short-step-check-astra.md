# Repo search

The supplied brief reports a lead search of main and PRs 10114, 10133,
10134 and 10141. The target-specific prior note does not exist at the pinned
checkout. The November 8 digest concerns earlier targets, not row 1018;
it cannot certify coverage of this later short-step check. Relevant source
checks and their closeness are as follows.

- Main's operating map and current rules were read at
  `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`. Row 1018 has no additional
  “Repo prior work” source line.
- The digest's nearest mass-gap hit is the older soft-route
  `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` on PR 10114. I fetched that
  head (`f76f6c649cff7dffbab664d8976e680e8f287fe9`) and read those
  lines plus its opening scope. Its claim and displayed operator step
  concern a one-time plaquette-loop positivity comparison, not CHAIN,
  PAR, NAB, or an order-one short
  step. Credit belongs to that earlier repository construction; none
  of its proof is rederived or used as a supplier here.
- Exact target/method searches in the digest and `open-registry.md`
  found no row owning this cross-provider check. Rows 1016 and 1017
  remain outside this work. Row 1022 is the requested earlier check,
  not an authorization to repeat its proof as independent evidence.
- This is a bounded follow-up to the supplied lead search, not a claim
  to have independently searched every file on all five refs. No
  prior complete cross-provider check was supplied or found in these
  searches. No existing research attack was taken over.

Author: OpenAI Codex (GPT-6; exact runtime submodel and effort are not
exposed to this session). Requested lane label: gap-short-step-check-astra.
Source: b67bb4773a051f6f0759ebfff5ddedd23b86fe37. Research check, not an
audit; no status granted. This does not prove a mass gap, validate the full
YM4D chain, or use computation to discharge mathematics. The primary 2D
papers, cited phase theorems, historical numeric logs and full CA-I proofs
are not checked. No source theorem is granted a new standing.

Work plan: read the target and its precise dependencies; check PAR, NAB,
MP, ADD and CHAIN by hand; record all numbered verdicts; only then open
the Claude check and adjudicate every disagreement; finish with one RESULT.

Checkpoint: complete. Own verdicts were written first; the full Claude
check and row 1022 were then read and compared. Both requested SA files
were fetched once at 31a47c543775 into the new empty scratch folder
/tmp/sa-gap-short-step-check-astra.rREhJu. Only this report was changed.

## Own verdicts, recorded before the Claude check

Line numbers below refer to `library/gap-short-step-max.md` at the pinned
commit. The underlying pinned-cell convention is row 1011,
`gap-pinned-cell-gauge-max.md:131–176`.

1. **ADD, lines 87–99: HOLDS AFTER CORRECTION at degenerate M.** Set
   epsilon = 6.1 times 10^(-4), and require M > 0. On epsilon < D <= M,
   CAS gives delta = (1-theta)epsilon; ADD gives theta = 1-delta/M.
   The identity D(2a)=16D(a)-Phi(a) follows by cancelling 16fa^4.
   If the band is empty the implications are vacuous; choose any positive
   delta and theta in (0,1), rather than divide by M=0. One can always
   decrease delta to ensure 0<theta<1. The series at line 99 holds given
   the engine's thermodynamic-limit identification along dyadic cubes.
   The no-seed contradiction at line 101 is conditional on the explicitly
   cited U(1), product and Proposition Delta inputs. Its step count needs
   an integer ceiling; the contradiction itself is valid.

2. **CHAIN, lines 109–121: HOLDS with the stated reciprocal multiplicity
   weights.** Here is a direct conditional-covariance check, rather than
   relying on differentiation of the displayed integral. For a plaquette
   in Q let k count its transverse coordinates on fine tiling hyperplanes,
   and b those on the outer boundary of Q. It belongs to 2^(k-b) subcells,
   each with weight 2^(-k); their total is 2^(-b), exactly its Q weight.
   Thus A_Q=sum A_c and N_Q,l=sum_c N_c,l. Given the inner rings, cell
   interiors are independent. Since no cell contains both selected links,
   the conditional cross covariance vanishes, including deterministic
   boundary-only plaquette terms. Total covariance now gives line 117.
   Integration over the inner rings uses the normalized density
   proportional to exp(-sum F_c); this proves line 119's identity. The condition
   excludes a shared plaquette, so there is no mixed direct-action term.
   No boundary reweighting is needed when the convention of row 1011 is
   used consistently. This is an exact identity, not a norm contraction.

3. **PAR Fact 0 and (i)–(iii), lines 154–175: HOLDS for n>=1.** For each
   subset S, divide tau_S by tau_j on P_j when j is in S. Every remaining
   factor is closed there by H2, since the P_i are disjoint. Fact 0 removes
   those factors by changes of the internal variables of container j.
   This proves the subset moment 1 or rho. An equivalent finite Fourier
   calculation gives
   E product(1+eps_i r_i) = ((1+rho)/2)product(1+eps_i)
   + ((1-rho)/2)product(1-eps_i).
   Its all-plus value is 2^(n-1)(1+rho)>0, its all-minus value is
   2^(n-1)(1-rho), and every mixed value is zero. Dividing proves (ii).
   Every proper-block moment in a nontrivial cumulant partition vanishes;
   the one-block term is the full moment. This also covers n=1. Holder
   gives the moment bound, and the pin involution gives r(tau pin)=1/r(pin),
   hence sup|tanh(v/2)|=tanh(sup v/2). Signed beta causes no difficulty:
   all finite-volume weights and normalizers remain positive.
   The bounds concern absolute cost and sup-pin cost; line 179 must not
   be read as a pointwise comparison of signed costs at different pins,
   or as a literal product of unaveraged activities.

These first verdicts were saved before opening row 1022 or the Opus file.

4. **PAR's container geometry, lines 177–181: HOLDS AFTER CORRECTION of
   the geometric shorthand.** Use a dual product cell complex, a closed
   mod-2 dual surface Sigma, and dual paths gamma_i from inside D_i to
   one common terminal segment in the outer collar, avoiding the other
   D_j. Define tau_i on primal links by intersection with Sigma x gamma_i.
   The coboundary is dual to the boundary of this chain. The internal end
   lies in P_i; the outer end is relative to the boundary. Boundary
   plaquettes see an even intersection. Thus H2 holds, and the common
   terminal segment gives identical restrictions on pinned links (H1).
   This requires the stated product geometry and collars; an arbitrary
   collection of containers is not covered just by calling them parallel.
   Line 201 additionally requires four admissible disjoint P_i and a
   common sup-pin class at both scales. Under those hypotheses it holds.

5. **MP, lines 429–441: HOLDS.** Write the exterior density as
   Z^(-1) exp(A_rest) product Z_i. Under tau_S it acquires product_S r_i,
   while O acquires (-1)^|S|. Expanding product(1-r_i) therefore produces
   2^n E[O]. Expanding product(1+r_i) without O produces 2^n. This proves
   both normalization and the exact reweighted identity, then the bound
   follows from |O| and the pin involution used in PAR. No independence
   under the reweighted law is claimed or needed.

   Primary-source comparison: G. Mack and V. B. Petkova, *Sufficient
   Condition for Confinement of Static Quarks by a Vortex Condensation
   Mechanism*, Ann. Phys. 125 (1980), 117–134,
   [paper](https://www-library.desy.de/preparch/desy/postpr/1978/desy78-069.pdf).
   I inspected the scanned formulas and figures on pp. 120–121, 126–130.
   Their (2.12) omits boundary plaquettes from the interior action;
   (2.16) and (2.18) give the reweighted expectation and its normalization;
   (2.19) is the bound; (2.20)–(2.21) identify its SU(2) factor with
   tanh(xi/2). Dividing their character by chi(1)=2 matches this note's
   normalized trace. Boundary-only action factors cancel in r_i when the
   twist is closed there. The attribution and normalization are correct.
   A confinement application still needs admissible container families
   and uniform cost bounds as the loop grows. Thus F441's consumer is
   this conditional Wilson-loop criterion, not a proved spectral gap for
   an entire centre-odd sector or the full L3 of section 2.1. Neither
   this comparison nor the loop bound supplies a centre-even gap.

6. **FLOW, lines 219–229: HOLDS.** On the compact interior manifold a
   smooth flow has Haar Jacobian satisfying d log J_s/ds=div V at tau_s.
   The pullback of exp(A)dU is exp(integral Psi_V) exp(A)dU. Differentiating
   its logarithm gives exactly the negative mean derivative and negative
   variance in line 225; Jensen has the displayed direction. Equality in
   the Hessian bound is equivalent to Var(Psi_V)=0. Boundary rotations
   must be fixed, as stated, and the field must be smooth.
   **The minimum assertion at line 231: HOLDS AFTER CORRECTION of grade.**
   The identities prove an upper bound for every flow and characterize
   equality; attainment still uses the explicitly unreconstructed
   weighted Poisson solvability argument. Replace the summaries at lines
   453 and 497 by “the flow bound is proved; attainment is ARGUED via
   weighted elliptic solvability.” No attainment theorem is proved here.

7. **PROJ (i)–(iii), lines 235–243: HOLDS.** Gauge differentiation gives
   sum_out N=sum_in Ad(U)^(-1)N. Taking its scalar product with n_z
   yields div j(z)=-sum_in D_l n dot N_l. Summation by parts gives
   X((d lambda)n)=sum_l lambda_head D_l n dot N_l, with the sign printed.
   This is pointwise and does not differentiate the field dependence of n.
   **PROJ (iv): HOLDS AFTER CORRECTION.** Require smooth fields, theta
   zero on pinned links, and div V_theta=0 for every theta being tested.
   Then E X=0 and integration by parts gives -E[V X]=E X^2. Testing
   gradients whose potentials vanish at pinned sites proves equivalence
   to div j=0 at free sites. For a boundary-moving field, the cost is
   H+Var(Psi), not simply E X^2 (FLOW); line 241 must state this internal
   restriction. Algebraic current conservation need not imply Dn=0.

8. **FR+, lines 249–255: HOLDS in four dimensions.** Along each
   plaquette, telescope v_x-Ad(U_p)v_x. Squaring the four edge terms
   gives |s_p cross v_x|^2 <= sum_edges |D_l v|^2. Summing counts each
   link at most six times, and minimizing the left side over the
   direction of v_x proves the stated multiplication-form inequality.
   A zero v_x contributes zero. This uses no statistical assumption.

9. **SPLIT, lines 257–267: HOLDS for the abelian part.** Multiplying
   the phase substitutions adds their boundary angles and affects each
   P_i only by its own phase, so the ratio identity is exact. Applying
   -log E exp(-sum v_i) <= E sum v_i proves Jensen's bound. The h/n
   conclusion is conditional on the uniform quadratic bound stated there.
   **The SU(2) defect at line 269: FAILS.** Let n=i, u=j and let the
   rest of a twice-crossed plaquette be v=k, in unit-quaternion notation.
   Then Re[(exp(theta i) j exp(-theta i))k]=-sin(2theta), whereas
   Re(jk)=0. There is a nonzero linear action change -2 beta theta.
   The defect is not universally beta theta^2 |u_perp|^2. Even after
   symmetrizing theta, its quadratic coefficient depends on v and has
   no fixed sign: for u=j and v=j the trace change is 1-cos(2theta),
   while v=-j gives cos(2theta)-1. Commutation with u suffices to preserve the holonomy;
   preservation of its trace is weaker (take v=1). Replace line 269 by:
   “Noncentral cut substitutions generally change the action; commuting
   tangential transports suffice for exact preservation. No universal
   positive quadratic defect, or necessity of reducibility for preserving
   one configuration's action value, is proved.”

10. **The exclusive reducibility claim at line 275: FAILS.** It is
    stronger than PROJ and contradicts the open exclusion acknowledged
    at line 273. A hand example: on an odd cubic torus take constant
    links U_1=i, U_2=j, U_3=k, U_4=1. All plaquette holonomies are central,
    hence every force N_l=0 and every projected current is conserved.
    Yet the odd-period holonomies i and j have no common fixed adjoint
    vector, so there is no global covariantly constant unit frame.
    Replace “each exists exactly ... only” by the sufficient commuting
    case and the still-open force-orthogonality alternative. This does
    not construct a useful typical-field flow or a short step.

11. **NAB (i), lines 308–315: HOLDS AFTER CORRECTION of the common-mean
    hypothesis.** Write m_p=E x_p and S_l=sum_{q containing l} E x_q.
    Direct integration by parts gives E X_l^2=beta S_l and
    E[(c dot y_p)X_l]=-m_p. Colour averaging then gives the exact bound
    E|y_p|^2 >= 3m_p^2/(beta S_l) when S_l>0. On a cubic torus,
    S_l=6 xbar, so this is xbar/(2 beta). The case xbar=0 is immediate.
    The line 315 equality S_l=6 xbar does not follow from constant beta
    and side lengths merely at least three: translations do not exchange
    differently oriented plaquettes on a rectangular torus. State “cubic
    torus” (or explicitly assume a common plaquette mean) for the printed
    formula. On a general rectangular torus the weaker universally
    available bound is m_p^2/(2 beta), using S_l<=6. This is a missing
    hypothesis in the printed proof, not a numerical refutation of its
    stronger rectangular-torus conclusion.

12. **NAB (ii), lines 311 and 316: HOLDS, with the means specified.** The
    two chosen outward links share exactly the one (1,3)-plaquette on
    every torus with periods at least three. Each link lies in six
    plaquettes. Thus |DD'A|<=beta, |DX|<=6 beta and
    E X^4=-3E[X^2 DX]<=18 beta E X^2<=108 beta^2.
    Cauchy–Schwarz gives E[X^2 X'^2]<=108 beta^2 and hence
    E(XX'+DD'A)^2<=2(108+1)beta^2=218 beta^2.
    Twice integrating by parts gives E[f(XX'+DD'A)]=E[DD'f], with plus
    sign. Colour averaging kills the linear terms. For c=e_1,c'=e_2,
    only i=3 contributes to sum_i (c cross e_i) cross (c' cross e_i),
    and it contributes e_3=c cross c'. Rotation covariance proves the
    identity for orthonormal pairs; bilinearity and antisymmetry give it
    for all c,c'. Therefore the displayed bracket and the
    factor 3 from E f^2=E|y_p cross y_p'|^2/3 are correct.
    For the numerical lower bound it suffices that both m_p,m_p'>=3/4:
    E[x_p x_p']>=m_p+m_p'-1>=1/2, while
    |E[y_p dot y_p']|<=sqrt(E|y_p|^2 E|y_p'|^2)<=1/2.
    The bracket is at least 1/3, giving 1/(654 beta^2). No common-mean
    assumption is needed for this repaired local version of (ii).

13. **NAB (iii), lines 312 and 317: HOLDS AFTER CORRECTION at zero.**
    Give the ratio e_2/tr M the value zero when tr M=0; as printed,
    “for every configuration” includes the flat field and contains 0/0.
    If T=tr M>0 and a>=b>=c>=0 are its eigenvalues, then
    T(b+c)-e_2=b^2+bc+c^2>=0. Also e_2=sum_{p<p'}|y_p cross y_p'|^2.
    Hence lambda_x=b+c>=e_2/T>=|y_p cross y_p'|^2/6.
    Combining (ii) gives 1/(3924 beta^2), and FR's incidence bound gives
    |sites|/(23544 beta^2). These constants are correct in d=4 under
    the explicit local-mean condition in item 12 (in particular on the
    intended cubic torus with xbar>=3/4). No run was used.

14. **NAB's claimed extensions and the P4 test cells: FAILS.** First
    overstatement: line 319(d), “dimension free ... every lattice”. The
    proof uses both six plaquettes at a link and six based at a site.
    In dimension d>=4 these counts are q=2(d-1), m=d(d-1)/2; the same
    proof gives score constant 6q^2+2, site denominator
    3(6q^2+2)m, and frame denominator 3(6q^2+2)mq. At d=5 these are
    386, 11580 and 92640, not 218, 3924 and 23544.
    Lines 340, 399, 402 and 405 must not import NAB verbatim into a
    matter model or frozen slices. Frozen spatial links violate its
    all-links-free hypothesis: the (1,2) plaquette has y_p=0, so the
    selected cross product is identically zero. A matter action adds
    a matter score to X and destroys the displayed six-plaquette bound.
    What survives is that the method has dimension-dependent variants
    for pure Wilson theories, not all the stated model identifications.
    This matters to the claim that *every* proved piece passes those
    barrier tests. No selective short step is thereby established.

15. **DICH, lines 281–285: HOLDS.** Before the exit step there are at
    most floor((r_1-r_0)/delta) drop steps and floor(E_max/eps)
    energy-increase steps. Assign a step satisfying both to either type.
    One final step suffices to force exit. This proves the printed real
    upper bound, with the understood integer time, even if either ratio
    is an integer. The proof's count should say “before the exit step”.

16. **ENG, lines 323–332: HOLDS AFTER CORRECTION of domains.** Require
    c_1,c_2>0 and Rbar(l)>0 (or define the Rbar=0 case separately).
    Multiply FL by the nonnegative c_2 Rbar and insert it into DEC to
    get the asserted minimum. The intended nonnegative responses then
    force compatible constants; one may choose c_1 c_2<=1.
    Line 323 must use NA=lambda_x/6, or allow NA in [0,6], since bare
    lambda_x is not bounded by one. The implication proves neither FL
    nor DEC and gives no monotonicity of NA.

17. **The 2D Z_2 test, lines 414–420: HOLDS for beta>=0.** Expanding
    product_p(cosh beta)(1+t U_p) leaves only the empty surface and
    the full disc under internal-link Haar integration. Thus its
    dependence on W is 1+W t^A. In the two-disc decomposition the
    factors (1+r_i) remove exactly those two disc factors; only
    1+W_1W_2 t^A_0 remains. Summing the four signs proves the two
    displayed moments. For signed beta use absolute values in the
    final sup inequality; this test implicitly uses ferromagnetic beta.

The named-lemma verdicts above were also saved before opening the Opus
file; the following heuristic judgments were saved before it as well.

18. **The map in section 3.4: HOLDS; the physical reading stays
    conditional.** Algebra gives
    2 artanh(tanh(s/2)^4)=log((cosh s+1/cosh s)/2), s=kappa r.
    This makes the large-r term kappa r-log 4 explicit. For kappa=1,
    0<tanh(r/2)^4<tanh(r/2) at finite r>0, so the map strictly contracts.
    A hand check of the three illustrations uses
    C(s)=sum_{j=0}^6 s^(2j)/(2j)! and
    0<cosh s-C(s)<(s^14/14!)/(1-1/60), for 0<s<=2.
    This brackets cosh(6/5), cosh(8/5), cosh(2) respectively between
    1.81065 and 1.81066, 2.57746 and 2.57747, 3.76219 and 3.76220.
    For q=(c+1/c)/2 use log q=2 sum_{j>=0} z^(2j+1)/(2j+1),
    z=(q-1)/(q+1); truncation after j=6 has remainder at most
    2 z^15/[15(1-z^2)]. Rational substitution gives respectively
    0.166<f<0.168, 0.393<f<0.395, 0.699<f<0.701. These hand bounds
    verify the quoted scale and contraction/expansion signs, with no run.
    The series bound, classical-to-quantum comparison and thin-vortex
    lower bound at hostile pins in line 203 remain unproved.

19. **Sections 3.3–3.5, 4.5, 5.3, 5.5–5.6 and 6.2: HOLDS AFTER
    CORRECTION of what their conclusions claim.** Product splitting
    (line 127) follows from the factorized pinned law and the block
    diagonal covariance. Frozen-slice identification (line 195) follows
    by inserting spatial links equal to 1; the separate long-range-order
    theorem remains a cited input. The primary 2D results and recalled
    U(1), finite-group and Higgs phase results were not re-proved here.
    They do not become unconditional counterexamples in this check.
    The last column of the barrier table suggests ways to discriminate
    models; it does not prove those five properties are logically
    necessary for *every* possible proof. In particular a product test
    requires attention to all factors, not a theorem that perfection of
    the Lie algebra is a necessary confinement condition.
    Lines 273–276 do not exclude force-orthogonal frames, as line 273
    itself admits. Replace “route (ii) FAILS” by “these estimates do not
    establish a curl bound or a selective step; the general route stays
    open.” Line 274's order-one interpretation supplies no constructed
    blocked law. The random-walk and energy/entropy descriptions in
    lines 299–304 are heuristics, not a counterexample to an exact
    quantified dichotomy. The model tests involving NAB require item 14's
    corrections. Lines 424–426 are conditional proposals, not reductions
    to a weaker established obligation. Their open labels are appropriate.

20. **Sections 6.1 and 8, including numbered 8.2(1)–(5): HOLDS AFTER
    CORRECTION of the summaries.** I did not rerun or validate the
    historical numeric logs at lines 367–387; they are excluded from all
    mathematical verdicts here. “No sign or count error” at line 387
    should say “the reported run did not detect one”. For 8.2(1), retain
    the corrected domains of ADD and PAR and the exact CHAIN identity.
    For (2), retain the cited-input qualifiers and distinguish heuristic
    selection rules from necessity. For (3), apply items 6–10 above:
    the flow minimum is not fully proved in this text, and the SU(2)
    defect and reducibility claims fail. For (4), use corrected NAB and
    ENG; no selective conclusion follows. For (5), withdraw the verbatim
    P4 model-transfer claim. The statements that O1, O2 and (W) remain
    open, and that no mass gap follows, survive. Sections 8.3–8.8 and
    line 497 must inherit these same corrections, with no source edit
    made by this checker.

Own-verdict freeze: all mathematical verdicts above were written before
reading the Claude check. This cross-provider comparison checks the same
source; another provider alone is not mathematical independence. The
separate paths here are total covariance for CHAIN, finite sign Fourier
algebra for PAR/MP, raw score identities and eigenvalue inequalities for
NAB, and explicit quaternion tests of the SU(2) claims.

## Comparison with the Claude check, read after the verdict freeze

Now read in full: `gap-short-step-check-opus.md:1–292`, and FINISH row
1022. The author is Claude Opus 5.5 max; its source pin is 54b9ac6aa.
The following gives every substantive difference found, including a
correction to my own geometric restriction. O denotes the Opus check's
line numbers; F denotes the Fable source's line numbers.

| Point | Adjudication with the exact line |
|---|---|
| CHAIN, O149–156 versus F115–119 | **Agreement: both checks are right.** Fine multiplicities add to coarse weights. There is no missing surface-action correction. The direct total-covariance argument in item 2 confirms the identity on the original weighted cells. |
| PAR geometry, O60–68, O285 versus my item 4 | **Opus is right; my sufficient construction was unnecessarily restrictive.** For the four-square tiling, paths may cross other subcontainers. H2 asks for zero coboundary there, not zero link signs. In a flat product, assign -1 to transverse links crossed by each dual path. Mixed plaquettes have equal paired signs; transverse plaquettes have odd parity only at the two path ends. Put one end inside its own D_i and the other at the common dual exit outside D. This proves H1/H2 without avoiding D_j. Delete the avoidance requirement for the fourfold application. F177's literal avoidance wording is not always possible, but the lemma and F201 survive. |
| SPLIT, O177–186 and O283 versus F269 | **The algebra in O180 correctly detects the linear term; its “ARGUED size” disposition is too weak for the printed universal sentence.** My explicit j,k plaquette refutes that sentence. O179 proves invariance for *all W* iff commutation; that is correct but is a stronger quantifier than preservation of one configuration's trace. The replacement must state this uniform-action quantifier or only sufficiency. Neither a bare ARGUED mark nor a claim about only reducible configurations repairs F269 as written. |
| NAB's common mean, O104–126 and O280 | **Agreement on the required correction; Opus is right about the broken equality.** My local-mean version of (ii) is slightly broader than its cubic repair. O280 additionally says translation-invariant laws are of the symmetric kind; that inference is wrong without hypercubic invariance or common means. Translation invariance alone does not exchange plaquette orientations. |
| NAB model transfer, O128–134 versus F319, F340, F399, F402, F405 | **Opus is wrong at O134 about frozen slices.** The all-links-free hypothesis fails there; the selected spatial plaquette has zero imaginary part. Dimension-dependent proofs exist in d>=4, but unchanged constants do not follow in d=5. O129 recognizes changed constants, which is compatible with item 14; it does not repair the source's “verbatim” table or its matter-model use. These are concrete scope failures, beyond an ARGUED size. |
| Route (ii), O227–228, O273, O281 | **Agreement that F275 overstates necessity; disagreement about calling the general route a failure.** My odd-torus central-plaquette example refutes necessity for conserved projected currents. O227 correctly notes that generic aligned choices may have nonzero divergence. That supplies a further obligation, not their exclusion. O228's “FAILS ... rests on the unexcluded aligned frame” cannot establish failure; the route remains open. |
| Heuristics, O219–225 and O230–240 | **Opus is right only at the expressly heuristic level.** No lower bound for the hostile-pin vortex free-energy *difference*, covariance cancellation bound, or typical-frame theorem is supplied. O220's asserted boundary-layer mechanism and distant-pin cure are not established by its dimensional estimates. They should be proposals, as my items 18–19 keep them. We agree with O234 that the table gives candidate distinguishing properties, not necessary ones. |
| Fixed-point wording, O204 versus F203 | **The three illustrated values agree, but the literal threshold sentence needs correction.** My hand bounds give f(0.4)<0.395<0.4; by continuity f(r)<r also for some r>0.4. Thus “expands above 0.40” is false if read as an exact threshold. Replace it with “contracts at 0.3 and 0.4 and expands at 0.5; the crossing lies between 0.4 and 0.5.” Opus's “right to two digits” is acceptable only as an explicitly approximate statement, not an inequality. This sharpens my item 18 after the comparison. |
| MP source and independence, O244–250, O292 | **Agreement on the identity and normalization; two source claims need correction.** Scanned (2.22) is the partition-function/thin-vortex-insertion identity, not the oddness identity O247 assigns to it. Pin-involution oddness follows directly from (1.6). The note and paper use the same centre substitution and Fourier method, expressly credited by F152/F431. Different authors do not make these two independent derivations under the repository's different-path rule. This does not impair the mathematical identity or its attribution to Mack and Petkova. |

Other distinctions do not change conclusions. O145 correctly permits a
negative theta if the band is empty; positive theta in my item 1 is an
optional convenient choice, not an extra demand of ADD. My explicit M>0
convention only avoids division by zero in a vacuous edge case. O167
agrees that FLOW's minimum is conditional on the unreconstructed Poisson
step. O172 agrees on PROJ's boundary restriction. O123 treats the zero
matrix separately; my ratio convention makes that repair explicit. O197's
lambda_x/4 is a sharper valid normalization than my lambda_x/6; both
repair ENG's [0,1] phrase. DICH and FR+ agree. No difference in label
“ADVANCE” versus “HOLDS” is taken as a mathematical disagreement.

The Opus report excludes the target's test table and filter corrections
from its coverage (O288). My failures there are additional coverage;
O134 nevertheless makes the frozen-slice assertion explicitly. Its final
“no WRONG anywhere” therefore does not apply to this complete line-by-line
check. No audit standing is inferred from either report.

## Source coverage and remaining limits

The source file has the same Git blob at this pin and the Opus check's
pin 54b9ac6aa: `e0830dbb6078c7d43fa723f472f4ddc693215644`. The disagreement
is therefore about the same text, not a later edit. I read all 497 source
lines, the referenced finite-cell definitions and FR argument, the CAS
statement and Proposition Delta's use, and the engine's definitions.
This checks their use here; it does not re-certify the engine's inputs.

After comparison I read C8 and C9 in `gap-invent-selective-max.md:128–130,
243–248`. Under C8's explicit ordering hypothesis, gamma_l uses only
preceding links, so the coefficient of the l-th Haar vector field is
independent of U_l and its contribution to div V is zero. That conditional
example in PROJ is valid. C9 and its claimed length scale remain heuristic;
no typical-frame or blocked-law claim is discharged by them.

The Sussman–Alpoge index was consulted before source excerpts: README's
usage rules; targeted searches in the chunk files, `obligations.md`, and
`ca-4.12-4.19/`; neighbouring rows at chunk-24:7–15 and chunk-29:69–78;
obligations at 1319 and 1495–1500. The exact short-step, vortex-container,
Mack–Petkova, cross-cell covariance and non-abelian-content terms produced
no matching target entry. This is a search result, not an absence theorem.
The “Neumann” hits concern scalar block estimates or Neumann series,
not the pinned Neumann-data covariance in CHAIN, and were not imported.

The cited outline source reads were 25976–25983 (Theorem 7.1's small-
coupling and witness-depth assumptions) and 31860–31882 (scalar-sector
scope and the explicit separation of a mass gap). These passages do not
supply the short step being checked. The complete CA-I file was fetched
as requested but no proof from it is used or claimed checked. Credit:
**Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text**, at commit `31a47c543775`. Their mathematics is not claimed
as this lane's contribution. Balaban's papers were not imported.

The Mack–Petkova PDF was fetched once into the separate new directory
`/tmp/sa-gap-short-step-mp.GNSRmi`. `pdftotext` was unavailable; PyMuPDF
rendered the relevant pages, and I inspected the images. Image rendering,
file hashing and source searches are bookkeeping, not proof steps. No
simulation, numerical proof, machine enumeration or formal proof checker
was run. The short rational bounds in item 18 are displayed hand
inequalities, not a machine certificate.

No target source, FINISH row, registry, ledger or audit record was edited.
The sole deliverable is this local file, on branch
`codex/gap-short-step-check-astra`; it is not committed or pushed.
The root proof targets (W), CAS, O1/DEC and O2/SER/SPR remain open.

RESULT: Cross-provider research check of row 1018 completed on b67bb4773: PAR, MP and CHAIN hold; ADD holds with its vacuous-domain convention; NAB's d=4 constants hold after the common-mean and zero-ratio corrections; FLOW/PROJ/FR+/DICH/ENG survive with the stated scopes. SPLIT's universal SU(2) defect fails at line 269, the exclusive reducibility claim fails at line 275, and NAB's frozen-slice/matter and verbatim dimension transfers fail. All differences with row 1022 are recorded, including the accepted Opus correction to path avoidance. No short step, mass gap, audit status or closure of (W) is claimed.
