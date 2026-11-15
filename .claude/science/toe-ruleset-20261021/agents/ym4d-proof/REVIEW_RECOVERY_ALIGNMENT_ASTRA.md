# Independent review of the frozen alignment continuation

Completed bounded review with same-context confirmation of the narrow dependency repair. Frozen science revision: `962f97c259d8c241df632a07e27f498f4ad33b09`. Reviewed continuation SHA256: `c58b51c8d19a87f473e0ecc86d582919ff7962417357db7b7c65eb83f2073fb4`. Methodology read at current-main revision `ca2bc7ddf64790da96cd43d42017d000fbfe4808` through `git show`; no checkout or reset. This is an independent bounded mathematical review, not an audit verdict, a whole-PR disposition, or a proof of continuum existence or physical mass gap. The user's overall target includes existence and physical mass gap; neither is supplied by this unit.

## Scope and pre-stated criteria

The exact criteria were saved before new mathematical computations in `checks/review_alignment_criteria.md`. The scope is the entire frozen `RECOVERY_ALIGNMENT_ASTRA.md`, with actual source definitions/proofs needed for its periodization, P1/P2, AC(log), restricted source norm, chart transfer, and explicitly open NC/weighted/background interface. Every uniform conclusion below rests on a displayed argument, not a finite checker. No fitted empirical target, external numerical benchmark, physical parameter, or new primitive is used. Dispatch requested Astra/max; exact runtime/model provenance is not independently observable from this worker.

## Independent derivations

### 1. Universal-cover filling and periodization

Use positive links, `Df(e)=f(head e)-f(tail e)`, and the corresponding oriented cellular boundary. Let `E=DM-I+S1 B`. The stated commuting identities give `ED=D(MD)-D+S1 BD=-DS0R+S1 DR=0`. Thus each row z of E has zero cellular divergence. For an output link b based at p, choose the fixed coordinate-ordered path gamma(p,x) on the infinite lattice. Fill the closed loop `gamma(p,tail e)+e-gamma(p,head e)` by interchanging the last edge successively past the coordinate segments. At most `|tail e-p|_1` elementary plaquettes are used, with signed multiplicity. Weighted summation over e gives a 2-chain F_b with boundary z: the path terms at each vertex cancel by zero divergence. The first-moment row bound makes both the edge and plaquette sums absolutely convergent. Exponential decay survives with any smaller positive exponent because the filling has only a linear loss.

For column bounds, write output roots in the L-periodic residue classes. For a fixed residue and input edge/plaquette type, translation identifies its column mass with a subset of the absolute row first-moment sum. Summing at most `d L^d` classes gives the displayed column bound. The factor is allowed to depend on fixed d,L, never on depth or volume.

Only now periodize every kernel by summing all image copies. Absolute convergence permits exchanging image sums and the finitely supported incidence operators; it also gives the row/column bounds by the triangle inequality. Composition commutes with image summation by the same rearrangement and translation covariance. No image path is first replaced by a shortest torus path. Therefore this argument includes side lengths below the kernel range and paths with repeated/wrapping edges. It supplies neither a new continuum limit nor interchange of any thermodynamic/RG limits.

The affine reproduction identity is load-bearing: `sum_Y a(y,Y)(y-Y)=0` makes M annihilate a constant 1-form on the universal cover; image periodization retains this exact harmonic cancellation. A shortest representative can change the winding integral even when endpoint restriction/interpolation still works. Roots satisfy `RM=0`, `RS0=I`. At the top, the field direction is `x_k=0`. Iterating the identity with `w_(m+1)=S1^T w_m` gives PER4 with the negative initial plain slot, positive residual slots, and negative curvature slots; the top pairing vanishes. This is a representation identity for every finite k, including k=1, rather than a source-domain inverse theorem.

### 2. Cubic interpolation and compatible gauge norms

For `r=sqrt(3)-2`, the inverse coefficients `c_j=sqrt(3) r^|j|` solve the cubic collocation convolution; their absolute sum is 3. The centered nonnegative B3 translates partition unity. Tensor interpolation hence has Lebesgue bound `A0=3^d`. Differentiating with `B3'=B2(.+1/2)-B2(.-1/2)` gives `A1=6*3^(d-1)`. Two derivatives give `12*3^(d-1)` on a repeated coordinate and `36*3^(d-2)` on distinct coordinates; these agree in d=4. Consequently `d*A2` bounds the l-infinity spatial Lipschitz constant of the gradient. On any cyclic grid the collocation eigenvalue is `(4+2 cos t)/6 >=1/3`, also for one or two coarse sites when entries merge. These bounds do not grow with period. Nested cardinal cubic spaces give compatible interpolation across levels.

On a fixed axial path the integral of an affine 1-form is a quadratic scalar polynomial in its endpoints. Cubic interpolation reproduces that polynomial, so M kills its constant and affine jets. If the own mesh is h, subtract the affine jet of the coarse-unit field; discrete telescoping yields a remainder bounded by `h^(2+alpha) D^(2+alpha)` times its derivative Holder modulus. Long tails use `2*||gradient||_infinity` in addition to the unit-range seminorm. This proves the stated `m_(2+alpha)`-moment estimate with `C_D=2 L^-(2+alpha) m_(2+alpha)` and `C_D'=C_D(1+C_C+2*8^alpha)`. It does not supply regularity for a different, merely compact kernel without a compatible interpolation proof.

The Campanato-to-pointwise constant used at this step was checked in the actual BFT_A section 8.4 proof. In d=4 a nested dyadic box doubles its side and multiplies its cardinality by 16, so the difference of its two means is bounded by four times the larger-box L2 oscillation. The geometric telescope for each endpoint costs `4*2^alpha/(2^alpha-1)`. Put both comparable endpoint boxes inside a box four times wider; each mean comparison then costs 16, giving `32*4^alpha`. Since the dyadic side is below twice the point separation, `C_C=2^alpha[8*2^alpha/(2^alpha-1)+32*4^alpha]` suffices for separations at most 1/8. Larger separations cost `2*8^alpha ||H||_infinity`. The lifted boxes have side at most one, so the same count works on the stated tori, including a unit coarse torus.

For detail amplitude `M rho^(2+alpha)`, differentiate the level reconstruction zero, one and two times and sum geometric series. Supremum, gradient supremum, and gradient Holder contributions are bounded respectively by the three displayed constants

`A0/(1-L^-(2+alpha))`,
`A1 L^(2+alpha)/(L^(1+alpha)-1)`,
`L^(2+alpha) [d A2/(1-L^-alpha)+2 A1/(1-L^-(1+alpha))]`.

Their SUM bounds the norm defined as a sum. A maximum of them would require an additional factor. The Holder estimate at distance t splits details at rho=t: use the second derivative below the coarse side and twice the first derivative above it. It holds for `0<theta<=1`; the limiting theta=1 estimate is finite since alpha>0. The continuation correctly retains the prior sum-of-constants repair.

### 3. P2 slot powers and sufficient exponent window

Write `h_l=L^-(k-l)`, `H_m=h_(m+1)`, d=4, and `pi=h_l^-3 |w_l|`. Transposed S1 propagation costs `L^(3(m-l))`, whereas S0 costs `L^(4(m-l))`. For S1, the image cardinal step interpolant has derivative total variation at most 3 in its active coordinate; the other coordinates cost 3 each. Thus constants depend on fixed d,L and the kernel, not k,T.

After S1 propagation the own coefficient is at most `C h_m^3 pi`. In PER4 its curvature coarse density is at most `C h_m pi`. An inverse box estimate costs at most `h_m^-alpha`, and the positive-level Y weight costs `h_m^-theta`. Hence the output is `C h_m^(1-alpha-theta) pi`; G0 instead costs `C h0^(1-alpha) pi`. Its residual slot at m has price `C L^theta H_m^(1-theta) pi`. Its plain slot costs pi at level zero and `h_l^-theta pi` at positive l. These calculations use the actual COFUN source prices, not a renamed norm. G0 is charged both separately and inside Y, as its definition requires.

For a positive-level curvature input, `pi_A <= C eta |G_l^c| <= C eta h_l^theta N_Y`. Summing all input levels below m costs at most `h_m^theta/(1-L^-theta)`. It leaves a decaying `h_m^(1-alpha)` factor. The unweighted G0 input instead leaves `h_m^(1-alpha-theta)`. Thus `alpha+theta<=1` is sufficient, including equality because the output Y is a maximum, not a sum over m. Above this window this particular upper-bound argument loses uniformity; that is not a necessity theorem or a counterexample to P2 itself.

The exact even gauge correction has own size `O(h_l^2 eta^2)`. Its curvature-source row therefore has size `h_l^4 eta^2 G_l^c`, and `pi_B=O(h_l eta^2 G_l^c)`. It gains ONE h relative to the principal pi term, not two. The continuation's correction is essential. Plain-source correction gains `h_l^2 eta^2` relative to its original current currency.

Scalar point charges from G,j have own size `h_l^4 eta G_l^c` and `h_l^4 eta pi_j`. S0 completion followed by the current price gives `h_m^(1-theta)` times the input coarse strength. A residual s has own size at most `L^-theta H^(2+theta) R`; its principal scalar charge is at most `L^-theta H^(4+sigma+theta) eta R`. Dividing by the scalar input volume and summing the surviving `H^(sigma+theta)` is geometric. The local residual divergence row is at most `L^-theta H^(3+theta) eta R`. It costs `L^(3-theta) H^theta eta R` in the fine pi currency and `L^-theta H^theta eta R` in the coarse one; each output sees only its adjacent residual levels. All omitted factors are fixed stencil/color constants, not depth-dependent constants.

### 4. AC(log): midpoint cancellation, independent coarse field, and residual sum

For the exact logarithmic gauge generator put `A_l=-[y_l,mu_bar_l]` and `R_l=-(1/2) Phi(ad_y_l) D mu_l`, where `Phi(z)=z coth(z/2)-2` is analytic and even, beginning with `z^2/6`. The small analytic ball is fixed before k,T vary. Color number N is fixed; no smallness radius uniform in N is certified here. The gauge norm supplies the supremum, gradient supremum and POINTWISE theta-Holder gradient at every level, and root compatibility; it does not supply second derivatives.

For a directed positive edge b let `m_b=tail b+e_i/2`. On one centered paired contour, sum each oriented axial segment exactly. For fine direction i and coordinate j the first moment is

`-L delta_(j,nu) z_i + delta_(i,nu) [L z_j + (L^2/2) delta_(j,nu)]`.

The zeroth moment is `L delta_(i,nu)`. Averaging offsets with mean zero gives `sum beta_b^i (m_b-m_c)=0` for every i, with `m_c=(L/2)e_nu`. Reverse-path signs must be attached to the canonical positive edge midpoint. Neither lower-left endpoints nor an uncentered offset set satisfy this cancellation.

Keeping the next-level background independent gives the exact identity

`r_l(A)=-[r_l(y),mu_bar_(l+1)]-sum_b beta_b [y_l(b),mu_bar_l(b)-mu_bar_(l+1)]`.

Replacing `y_(l+1)` by `B y_l` without the mismatch term changes this identity. At the top the root gauge vanishes, so `A_k=0` even for independent top data.

Discrete telescoping on the fixed lifted contour support gives

`mu_bar_l(b)-mu_bar_(l+1)=h g . (m_b-m_c)+E_b`,
`|E_b|<=C H^(1+theta) ||mu||_(1,theta)`.

Here g is one fine forward gradient at the root. Endpoint averaging gives the edge midpoint; coarse endpoints are the two roots. The remainder uses only the pointwise Holder continuity of that gradient; for distances beyond one coarse unit the gradient supremum handles the fixed-L tail. Write `a_i=y_l^c(i)` and subtract `a_i(root)`. The constant coefficient times the affine term cancels orientation by orientation. Since `osc a_i<=C H eta`, the remaining own-unit products have sizes `C h H^(1+theta) eta M` and `C h H^2 eta M`. Both are at most `C H^(2+theta) eta M` for H<=1 and theta<=1. The mismatch contributes the same bound because `|r_l(y)|<=eta H^(2+sigma)` and sigma>=theta.

The even correction satisfies `|R_l|<=C h^3 eta^2 M`; applying B and subtracting the independent next-level correction gives `|r_l(R)|<=C H^3 eta^2 M<=C H^(2+theta) eta^2 M`. At the top the latter correction is zero. All these are local stencil estimates valid even when a finite torus identifies some variables.

For the field part, the discrete product identity writes the gradient of A^c as bounded shifted a times the gauge gradient plus bounded shifted mu times the gradient of a. On a box of side r, the oscillation of each undifferentiated bounded factor is at most `C r` times its Lipschitz constant. This proves the required Campanato-alpha product bound directly, using theta>=alpha for the differentiated gauge. No Campanato-to-pointwise conversion and no C2(mu) estimate are needed. For an arbitrary mesh-h array F, direct finite differences and box averages give `||F||_(C1alpha)<=C h^-(1+alpha)||F^c||_infinity`; applied to R^c=O(h^2 eta^2 M), this gives `C h^(1-alpha) eta^2 M`.

The residual coarse density is `r_l(K')/H=O(H^(1+theta) eta M)`. The sharp residual weight cancels this power. The C1alpha inverse bound instead gives `C H^(theta-alpha) eta M`. Thus for the actual residual sum,

`N_res(K') <= C eta M sum_(q=1)^(k-1) L^(-(theta-alpha)q) <= C eta M/(L^(theta-alpha)-1)`.

The sum is empty for k=1. The strict theta>alpha, rather than theta>=alpha, is necessary for THIS geometric argument; at equality its bound is k-1. The separate M-gradient residual factor is weaker for H<=1. This independently establishes the continuation's local AC(log) implication under its fixed global background, compatibility, exact contour, and norm assumptions. It does not identify a covariant sharp output norm.

### 5. Restricted source domain and logarithmic chart

At fixed k,T the representation map is linear between finite-dimensional spaces. Its R0 class sets `G_l=0` for l>=1 and includes every plain current. It is therefore onto; a bounded minimizing sequence of slots has a convergent subsequence in that finite-dimensional slot norm, and the closed fiber attains the infimum. This proves that N0 is a finite-dimensional quotient norm. The mere existence of an R0 representation imposes no restriction on a finite source. There is no uniform assertion `N0<=C N`, since the full representation infimum N allows additional positive-level G slots.

For any R0 representation, the sum of positive-level plain currents is bounded by `P_c/(L^theta-1)`, and the residual R(theta) price is exactly `L^-theta` times the R price. Together with the unchanged G0/P0 terms this gives `N^(theta)<=C_N N0`, where `C_N=max(1,(L^theta-1)^-1)` is sufficient. The existing projected K(theta) estimate then gives the displayed response factor `2 G (1+C_projection eta) C_N N0`. This is conditional on that matched projected inverse and its source/data mapping; the review does not recertify the inverse theorem globally.

For the chart, J maps left tangents w to logarithmic tangents v: `v=Jw`. Pairing therefore fixes the directions `f=J^-T S`, `S=J^T f`; gauge coordinates satisfy `Xi_Z=-J^-1 K`. Actual source slots in the read BGT definition pair G with the transported curl and s with the derivative of the same local logarithmic root residual. Consequently, writing `E_G=d_Z J^-1-d` and `delta_l=D rho_l-r_l`, the identity is

`G_flat=G`, `s_flat=s`,
`j_flat=J^-T j+E_G^T G+sum_l delta_l^T s_l`.

This is an identity of representations before taking infima. It preserves G_l=0 at positive levels, so it is valid for both the full and restricted quotient norms separately. It does not exchange those infima.

The finite curl stencil has coefficient error O(h eta). Multiplying a G coefficient of own size h^2 G^c gives current currency `C eta G^c`. The residual stencil has coefficient error O(H eta). For `|s_l|<=L^-theta H^(2+theta) R`, the output Pc costs are `C L^3 eta R` at mesh h=H/L and `C L^-theta eta R` at mesh H. At most the two adjacent residual slots feed an output level. This is the source of the L-dependent constant in the claimed `1+C eta` norm equivalence. The P0 price is no larger. The inverse local chart has the same estimates, and the plain-current multiplier is `I+O(h eta)`.

An axial comparison transport across a coarse box of side r has at most C r/h links with each log O(h eta); hence its deviation from identity is `C eta r` (with a fixed exponential factor in the complex continuation). Ordinary versus transported Campanato seminorms therefore differ by at most `C eta ||G^c||_infinity`, since r^(1-alpha)<=1. This needs the specified short local paths; it says nothing about arbitrary winding transports or a merely curvature-small background. The independent top background is bounded by its neighboring fine potential and top mismatch, with a fixed L-dependent constant absorbed into the same small-ball choice.

### 6. Local analytic residual dependency

The read NA-alg source defines the actual SU(N) maximizer W0 by `Pi_su(e^-X M)=0`. At M=I,X=0, the derivative in X is minus the identity on su(N). The real analytic implicit-function theorem gives one fixed analytic ball for this finite local word. Its complex extension is the extension of this real-analytic local solution, not an arbitrary global SU(N) polar projection. A finite set of stencil types gives a uniform local radius independent of k,T; identifying repeated variables on a wrapping torus only restricts that finite word. For fixed N the local branch is also the maximizing branch after shrinking the ball if needed: at M=I the unique maximizer is I, compactness separates points outside a fixed identity neighborhood, and the local stationary solution is unique inside it. This does not recertify every displayed numerical threshold of NA-alg for arbitrary N.

For the required centered quadratic jet, write each contour logarithm `Y_t=A+Q_t+O(a^3)`, where A is the common constant-field linear part and the averaged signed area is zero, so `average Q_t=0`. Then `M=I+A+(1/2)A^2+O(a^3)`. Substitution in the stationarity equation with `X=A+X2` gives `Pi_su(-X2)+O(a^3)=0`, hence X2=0. Spatial variation introduces one extra mesh power; terms of order at least three have at least three own-field powers on the fixed analytic ball. This derives the local residual sizes needed in P2 without using an incorrect exact central-phase formula for a general SU(N) maximizer.

There was a stale historical proof-body defect in frozen BFT_A BA5, already acknowledged in its RBA1-fix note but not reconciled in the proof body: a general SU(N) maximizer is not obtained from the U(N) polar factor by a uniform scalar phase. If the positive polar factor has unequal eigenvalues and the determinant phase is nonzero, that phase correction leaves a non-scalar anti-Hermitian part, violating stationarity. The actual stationarity proof above and in PROOF NA-alg supplies the quadratic conclusion used here. This is not a refutation of the frozen continuation, which uses the actual analytic W0 residual; it identifies the exact old proof text that cannot be adopted. The earlier RBA1-fix acknowledgement was read after the coordinator pointed it out, so this review records reconciliation of a known issue, not priority for its discovery.

## Explicitly unclosed obligations

NC(log) remains a generic-field map from flat sharp to the stated covariant sharp norm. AC(log) only treats compatible gauge-generated fields and cannot replace that map. A proposed local polarized estimate must be proved for the actual W0 residual to all orders, with independent next-level data, transported gradients, and the full summed residual term; a finite BCH2 expansion cannot supply that proof. The reported local source equivalence does not by itself give NC.

Weighted image/filling, weighted AC/NC/source transfer, preservation of the specified weights and allowed exponential losses, the matched flat sharp right inverse, reference projections, HD/FW dictionaries, and the globally small background required by the contraction remain conditional interfaces. In particular, global log-potential smallness is not implied by local curvature smallness. This review establishes no global critical background, continuum/non-free SU(N) measure on R4, OS0–OS3 package, order of continuum/thermodynamic limits, or positive physical mass gap. No registry/status promotion or audit-system authority is exercised.

## Coverage ledger, exact runs, and frozen receipt

### Same-context repair confirmation

The coordinator replaced the BA5 proof body and clarified its historical note. The final repaired `BFT_A.md` SHA256 is `553d56f46ea457aa1b6a97c2a53f435739d3fadb6c9af0cf89676f41a7266902`. I read the complete two-hunk diff, the replacement in section 3.5, and the historical note in context. The earlier repaired hash `d8429af529a4c36b23887a35a1db0600eadad07076c0567dd587e11cd279072b` had the same corrected proof body; the final change only fixes the old note's overly strong "only scalar P" wording. Zero determinant phase permits a nonscalar positive polar factor, as the final text now says.

For clarity, the fixed-point proof is quantitatively valid in the declared Hilbert–Schmidt norm: the projection Pi_su has norm one and `|Pi_su(Z H2)|<=||H2||_op |Z|`. Rearrange the stationarity equation as `R'=Pi_su R3+Q(R')`. On `|R'|<=2|R3|`, its Lipschitz constant is at most `C(|H2|+|R3|+|R'|)`, which is below 1/2 after one fixed smallness choice. The map then takes that ball into itself. The resulting `W=e^mean(Y)e^R'` has logarithm inside NA-alg's `|X|<=3y` uniqueness ball and is its actual maximizing branch. This proves `|R'|<=c_pol y^3` and hence `X0=mean(Y)+O(y^3)`. It supplies an unspecified finite constant, no numerical c_pol and no global projection formula. It adds no depth/volume dependence. This confirms the narrow repair without extending coverage to unread parts of BFT_A or changing the frozen continuation's conclusions.

The exact counterexample control uses `z=(1+i/1000)/(1-i/1000)` and `M=(2I+diag(z,z^2,z^-3))/3`. Its determinant has nonzero imaginary part `47999984000/27000081000081000027`, and its three squared singular values are distinct exact rationals. The input logarithm has squared Hilbert–Schmidt norm at most `7/125000 < 1/400`, inside the cited y<=1/20 ball. If the scalar-phase polar formula were used, its stationarity residual would be a nonzero traceless part of `sin(Phi/3) diag(sigma_i)`. No numerical optimization or fitted parameter enters this witness.

### Exact source coverage

`checks/review_alignment_source_inventory.json` binds every frozen source to its SHA256 and Git blob and gives exact read ranges. The entire continuation, entire ALIGN3_55, and all five frozen `recovery_align_*` artifacts were read. Every hash in the author's source/output receipt agrees with the independently inspected frozen Git object. That agreement attests identity, not full-document coverage.

| Source | Fully read spans at the frozen revision |
|---|---|
| CODEX_REVIEW_ALIGN2.md | 1–94, 130–328 |
| ALIGN2_55.md | 97–268, 398–573 |
| COFUN_CC.md | 113–143 |
| BGT55.md | 42–136, 317–409 |
| ALIGN55.md | 204–243 |
| KFACTOR_OFF55.md | 68–130 |
| LINEAR_PACKAGE.md | 49–115 |
| BFT_A.md | 18–47, 120–185, 355–380, 432–510, 540–585, 626–646; plus the final changed proof and note in the working tree |
| BFT_B.md | 1586–1632, 2015–2109 |
| DICT55.md | 132–170, 216–257, 368–479 |
| PROOF.md | 1938–1966, 3328–3363, 5647–5658 |

All other spans are unreviewed for this receipt, even if a search returned a matching line. A truncated read was not counted as full; relevant uncertain spans were reread before inclusion. In particular I do not attest whole-file correctness of BFT_A/BFT_B/PROOF, the original inverse theorem, HD/FW's entire dependency chain, or the whole PR.

`checks/review_alignment_methodology_inventory.json` binds the current-main methodology and installed skill reads separately. The entire pinned AGENTS, SCIENCE_WORKFLOW, physics-loop and review-loop skills, freshness check, claim-status reference, primitive registry check, minimal-axiom memo, registry JSON, proof-search governance, no-go skill, and five review references were read. The conformance reference was additionally read through line 440; later landing sections are outside this unit's operations. Both installed skills were read but the consistent pinned current-main set controls. No registry primitive is invoked to supply gauge dynamics, an action, a continuum measure, or a mass scale. No premise-source grant is inferred from a skill summary.

### Runs and controls

`checks/review_alignment_exact.py` is a new implementation. Its image kernels use exact Q(sqrt(3)) geometric sums, including winding-index first moments; its S1 uses integrated quadratic B-spline basis functions. It neither imports the author's matrix solver nor imposes harmonic cancellation. All identities held for L=3,5 and coarse counts 1,2,3,5,9. The merged-path controls had nonzero harmonic errors; at L=3, counts 3,5,9 their first values were -8/9, 40/99 and 8/153. The proof, not these finite values, supports arbitrary-period bounds.

The contour checker integrates entire oriented segments and verifies the stronger single-contour moment formula before averaging. All directions/orders at d=2,4 and L=3,5,7 passed, and uncentered controls failed the required transverse moment. Exact su(2)-bracket AC1 checks included a wrapping periodic top-root-zero instance and an independent-coarse-background local algebra instance; corrupting the coarse sign was detected. The latter uses a constant gauge shift as an algebraic test, so it is not claimed to be a global root-zero gauge hierarchy. The mathematical proof separately imposes the actual root compatibility. There were 4,620 direct own-unit exponent identities, geometric sums through k=20, the equality alpha+theta=1 case, the strict theta-alpha summation control, both neighboring source-chart prices, and the single h power in the Phi-G correction. Finite exponent checks are bookkeeping evidence, not an infimum norm theorem.

The frozen author checker was reproduced once from its exact Git bytes. Its stdout is byte-identical to the frozen 942-byte output, with exit zero and empty stderr. `checks/review_alignment_controls.py` saved five independent mutated copies and their complete outputs:

| Deliberate corruption | Actual exit | Detected failure |
|---|---:|---|
| Remove image harmonic subtraction | 1 | Nonzero row sum of M |
| Replace S1 row sum 1/L by 1 | 1 | Completion identity |
| Use lower-corner edge locations instead of midpoint | 1 | Contour first moment |
| Reverse coarse commutator sign | 1 | Cubic AC scaling |
| Use uncentered offset set | 1 | Contour first moment |
| Independent reviewer: replace S1 growth 3(m-l) by scalar growth 4(m-l) | 1 | Propagated own-unit exponent |

All six failures are preserved as actual nonzero exits with their AssertionError tracebacks. They are expected negative controls, not failed positive tests. The control driver's own run exited zero with empty stderr. There was no unexpected mathematical checker failure and no discarded/revised positive test run. One wrong source path caused a Git read failure; its exact diagnostic and successful path correction are recorded in `checks/review_alignment_operational_failures.txt`. No unchanged successful scientific run was repeated to change metadata.

These are raw reviewer evidence captures, not runner-cache envelopes or audit verdicts. Author/control timings are recorded in the control JSON (original reproduction approximately 0.85 seconds); the first independent runner's wall time was not instrumented. One scientific review iteration and one narrow repair with a historical-wording follow-up were completed in this same reviewer context. Full pipelines: zero in this bounded worker. Git commits/pushes, integration retries, audit/status writes and PR actions: zero. The combined candidate gate and any landing/audit packaging are coordinator responsibilities and are not asserted here.

### Disposition and receipt boundary

The displayed conditional finite-lattice implications are confirmed within their exact geometry, norms, exponent window and fixed small analytic ball. One known historical proof-body inconsistency was reconciled and the affected fix was independently confirmed; the old note's zero-phase exception was corrected in the same pass. No other consequential defect in the scoped continuation remains from this review. Missing global/weighted/NC inputs remain explicit open inputs, with no assertion that they are independent, impossible, or exhaustive. This is positive local mathematical support and open-obligation bookkeeping, not an N-gate or audit-packet PASS. No five-route exhaustion or global impossibility claim is made.

Accepting this unit's mathematical support does not certify the full R2 assembly, the PR, an R4 Yang–Mills existence theorem, OS0–OS3, non-freeness, or physical mass gap. The strongest immediately named missing local bridge remains the generic-field NC(log) estimate in the actual covariant sharp norm, alongside the unverified upstream inverse/background and weighted interfaces. None is replaced by a target-equivalent assumption represented as closure. No new claim IDs are proposed for independent audit by this worker.

The frozen receipt is `checks/review_alignment_receipt.json`. It binds this final report, every retained reviewer artifact, frozen source identities/coverage, and the exact final repaired BFT_A hash. The receipt excludes itself to avoid a self-hash cycle. Receipt/report hashes are supplied in the coordinator handoff; neither is an audit authority.

