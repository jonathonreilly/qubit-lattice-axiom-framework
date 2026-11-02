# Independent review of the actual residual-vertex construction

**Disposition: the zero residual F² coefficient is confirmed for the stated paired antiperiodic charged-root calculation, at each fixed depth, with volume taken first and external momentum then sent to zero. The argument uses the actual normalized action and a separately defined auxiliary off-shell function. It does not establish the neutral/full-periodic identification, the depth-uniform tree producer package, or the Yang–Mills existence and physical mass-gap theorem. No mathematical source correction is requested.**

The mathematical source is all 255 lines of `checks/residual_det_vertices_working.md` at `236882cc8e66bfabf606216f5e49ca4cd0a61911`, SHA256 `8a7c87c9b737ee88372eb985189bcd0e25440986868cc8d92062b84f6cb92cd1`. Its complete manifest and `residual_det_04.*` were read and their hashes checked. The coordinator subsequently inserted exactly one dependency-link paragraph; the packaged note has 257 lines/26224 bytes, SHA256 `aa16239e801d371c7242a342b339ed5dfeec8fa75f5dd8a3ac3a128a84989d56`. The complete diff confirms that every mathematical byte is unchanged and all six links resolve. Both versions, complete/partial source coverage, the metadata diff and independent evidence are bound by [the source manifest](checks/review_residual_vertices_source_manifest.json), [packaging check](checks/review_residual_vertices_packaging_check.json) and [freeze receipt](checks/review_residual_vertices_receipt.json).

This is the same independent reviewer context as the preceding completed units, requested as Astra/max in the coordinator dispatch. Visible model identity is GPT-6; no further runtime configuration is introspected. It is same-family scoped review, not cross-family, whole-PR or audit certification. Current-main methodology remains `ca2bc7ddf64790da96cd43d42017d000fbfe4808`. Earlier determinant, harmonic-bridge and mass-gap-target reports remain unchanged. No author/shared source, git/PR state or audit authority was edited by this reviewer.

## Criteria and coverage

[Criteria](checks/review_residual_vertices_criteria.md) were saved after reading the complete mathematical note and before independent computation or reading the author's script. The criteria require actual lattice checks, noncommuting off-shell controls, explicit covariance premises, every trace group and separate singular-centre bounds. The author controls were subsequently read completely; the coordinator's 13/13 replay is not counted as independent mathematical verification.

The previously reviewed normalized finite Phi, actual action dictionary, fixed-depth local tree jets and harmonic bridge supply only their already established scopes. New contextual reads at the vertex freeze are `UIR55.md` 250–297 and 406–420, `UIR2_55.md` 165–235, and `RECOVERY_UIR_ASTRA.md` 154–272. A tool-output truncation inside RECOVERY line 167 was recovered by a separate complete read of 165–173. Inherited ranges and their exact source hashes are recorded separately; no complete review of the large historical PROOF/FLOW/UIR files is claimed. In particular, the old IC/IRL assertions and old discontinuity/cancellation claims in UIR2 are not imported as facts. The new grouping is checked below directly.

| Claim | Disposition |
| --- | --- |
| Local h=1 saddle section and fixed-depth Taylor locality | Confirmed for the germ, with no volume/depth-uniform nonlinear neighborhood asserted. |
| V1: normalized auxiliary zero-residual gauge change | Confirmed off shell for R; no off-shell identification R=Phi is used. |
| V2 and the actual Wilson endpoint row | Confirmed, including the equation-of-motion term and scalar determinant. |
| Tuned path, massive-gradient minimization and V3 | Confirmed; naive interpolation and total differentiation are distinct failed controls. |
| Covariant local frame/high Schur embedding and V5 | Confirmed for the actual Cartan-background/charged-pair vertices, with all frame and embedding derivatives retained. |
| Complete V4/V7 trace groups and half-bubble convention | Confirmed; the numerator cancellation is at the duplicated propagator's own momentum. |
| Antiperiodic Riemann sums, mixed continuity, quadratic-residual logarithm | Confirmed in the stated volume-first order, at fixed depth and uniformly along the compact gauge path. |
| Residual F² coefficient in that root-sector convention | Zero. This is a scoped one-loop conclusion. |
| Neutral/full-periodic/full-colour identification, uniform tree producers, full physical theorem | Remain open. |

## 1. The local saddle section and its actual action

At the free point, the unminimized fine Hessian completed only in the internal gauge directions is

    Z_int=H_W+M*C^-1 M+D P_int D*.

For a nonzero coarse Bloch momentum K, zero Wilson energy makes the fine field a=D lambda, since every fine alias has nonzero scalar momentum. Exact root covariance MD=d_c ev then makes zero soft energy imply ev lambda=0. The remaining internal fixing forces Delta_int lambda_int=0, and the Dirichlet gap gives a=0. At K=0, a curl-free field is a gradient plus a constant one-form. M sends that constant field to ell times itself, so the soft term removes it. Subtracting the root value from the scalar potential then reduces the remaining case to the same Dirichlet argument. Hence Z_int is positive at every real Bloch point. Its finite-size symbol and the compact Brillouin zone give a fixed-depth gap independent of the number of cells.

The underlying normalized soft-action germ and its fixed-depth local tensors were already identified for the actual phi chain. Completing a local internal Coulomb condition gives a nonsingular fine stationarity equation at the origin. Along the internal gauge orbit, the unminimized action with V fixed is invariant. At a critical point of Q+||Gamma||²/2, surjectivity of Gamma' D_internal forces Gamma=0. Its derivative at the origin is Delta_int, so this applies in the finite-volume implicit-function neighborhood. The stationary point therefore satisfies Q_U=0. The actual combined fine/h Ward identity then gives ev* Q_h=0; ev* is injective, so Q_h=0. This establishes an h=1 representative of the original saddle, not a new tree functional.

At each fixed depth, the gapped inverse and its differentiated local tensors are exponentially summable. Finite-order derivatives of the section are finite trees of such kernels. They have analytic joint Bloch symbols and volume-uniform fixed-depth bounds; they also have the appropriate periodizations. A full nonlinear neighborhood uniform in volume or depth is not needed for these jets and has not been proved. Fine extensions of a coarse gauge transformation differ by an internal gauge transformation; the covariant operators and root frames below remove that internal ambiguity.

The free tree Hessian is analytic and nonnegative, vanishes at zero momentum on the four constant one-forms, and has no linear Hermitian term by positivity at both signs of a small momentum. Thus H_n(P)=O(P²). The actual envelope identity gives rho_1=C_n H_n v, so rho_1=O(P²) at fixed depth. This property concerns the actual local tree section and physical residual, not an external inverse-Laplacian ansatz.

## 2. R is a legitimate auxiliary function; V1 does not extend A5 off the saddle

The harmonic identity A5 from the preceding unit equals the original determinant remainder at the actual fine/h saddle. Here its right side defines R(U,V) off that saddle. The distinction is essential: the previous augmented null-row proof does not hold at arbitrary independent U,rho, and is not used there.

On V=m(U), normalization gives Psi(U,m(U))=0 and vanishing residual first derivative. Differentiating these identities gives the exact Gauss–Newton soft Hessian

    (-M,I)* C^-1 (-M,I),          H_h=G_c=d_c*C^-1d_c.

This statement is about the actual normalized action. An unnormalized contour density would have additional contour-variance terms and would not supply this identity.

Eliminate the massive coarse block C^-1+d_c d_c*. Woodbury gives Q_1=H_W+F_1*F_1, with

    F_1=P_int D*+J R_c^(1/2) d_c*M,
    R_c=(1+d_c*C d_c)^-1,       F_0=D*.

In scalar coordinates (I,L), MD I=0 and MD L=d_c. Thus F_1D is block triangular with diagonal Delta_int and R_c^(1/2)Delta_c. Its determinant is det Delta_int det Delta_c det R_c^(1/2), because the scalar change (I,L) has determinant modulus one. The massive coarse determinant is 1/(det C det R_c). In A5, H_h=G_c cancels its matching factors and the level group cancels det C and the remaining coarse factors. The result is exactly

    R(U,m(U))=Gamma_F1(U)-Gamma_F0(U),
    Gamma_F=1/2 log det(H_W+F*F)-log det(FD).

In particular the scalar normalization is -log det(FD), not half of that term. R(U,m(U)) need not vanish off shell. The independent dense control has HD nonzero and obtains both the exact V1 ratio and a nonzero off-shell face. It does not assume the null-row identity it is testing.

## 3. Nielsen derivative and the nonflat Wilson row

At fixed background U, let Q_t=H_W+F_t*F_t and B_t=F_tD. Differentiating the two finite determinant logs gives

    partial_t Gamma=Tr(Q_t^-1 F_t* dotF_t)-Tr(B_t^-1 dotF_t D).

The first coefficient 1/2 cancels against the two equal real transpose terms from F_t*F_t. Since Q_t D=T_E+F_t*B_t, where T_E=H_WD, cyclicity gives

    partial_t Gamma=-Tr(Q_t^-1 T_E B_t^-1 dotF_t).

This is an exact identity for noncommuting matrices. It does not set HD to zero away from Wilson stationarity, and it does not modify the later 1/2 bubble coefficient.

For right coordinates U_l exp(a_l), the actual gauge generator is D_U lambda=Ad(U_l^-1)lambda_x-lambda_y. BCH to first order in a gives its derivative

    delta_a X_lambda=1/2[Ad(U_l^-1)lambda_x+lambda_y,a_l].

Differentiating gauge invariance and using the invariant trace inner product yields

    (H_W D_U lambda)_l=-1/2[E_l,Ad(U_l^-1)lambda_x+lambda_y].

This is a finite-range lattice endpoint row. It is not the assertion H_WD=0 at every background, nor merely a continuum shorthand. An opposite consistent generator convention changes the matched signs together.

The independent exact check differentiates the actual Wilson plaquette trace at four rational, noncommuting SU(2) links, with all twelve right-coordinate components and twelve site-gauge components. The background gradient is nonzero. The complete Hessian times D equals this endpoint row exactly. Dropping the row, dropping an endpoint, or changing its half coefficient fails. Separately, direct determinant-polynomial differentiation of a dense off-shell family confirms V2 and rejects omission of the scalar normalization. These checks are independent of the author's small example.

## 4. Why the tuned path gives the correct partial cancellation

Let alpha=ell² and r=ell⁴-1=alpha²-1. At K=0 the harmonic extension of the root constant is the constant scalar. Therefore, for b=J*Delta I,

    h=Delta_int^-1 b*=-1_int,          ||h||²=r.

The root part of F_tD in harmonic coordinates is u b Delta_int^-1 y+(uS+vR_c^(1/2)Delta_c)eta, where y=Delta_int xi. Using S=alpha|K|²+O(K⁴), Delta_c=|K|²+O(K⁴) and R_c=1+O(K²), its leading energy is

    ||y||²+|u h*y+a |K|² eta|²,       a=alpha u+v.

Exact rank-one minimization gives y_min=-u a |K|² eta h/(1+u²r) and energy a²|K|⁴|eta|²/(1+u²r). The curve v=sqrt(1+ru²)-alpha u has a²=1+ru². It is nonnegative on 0<=u<=1, since its numerator after rationalization is 1-u²; a>=1. Its rational parametrization has denominator at least 2. Both give a regular compact path from F_0 to F_1. The scalar root symbol b_t=uS+vR_c^(1/2)Delta_c is positive away from zero, and its inverse has a simple pole with constants uniform along that path at fixed depth.

At fixed fluctuation, the leading partial dotF on the minimizing gauge field is

    [dot a-dot u u r a/(1+u²r)] |K|² eta.

The derivative of a²=1+u²r makes this exactly zero. The minimizing field must be held fixed in this particular path derivative, as V2 requires. Differentiating F_t E_t in t instead would add F_t dotE_t and gives a different, nonzero result. Conversely, when taking a subsequent background derivative of k_t=dotf_t E_t, the background derivative of E_t must be included. The source makes both distinctions correctly.

High physical transverse aliases have F_t=O(K), while the low fixing has order K. Their coupling to a low mode is consequently O(K²), and their minimizing amplitude is O(K²); they do not change the leading gauge calculation. A transverse low vector has zero degree-one divergence. The gradient computation above removes the remaining longitudinal degree-one contribution. Therefore the actual low embedding satisfies dotF_t E_t=J k_t with k_t(K)=O(K²). The longitudinal low one-form principal coefficient is ell^-2, since ||D L eta||²=ell²|K|²|eta|² to leading order; the transverse coefficient is the same Wilson coefficient. This establishes the four-component simple-pole low block throughout the path.

For comparison, straight interpolation has coefficient 25/21 at ell=3,t=1/2, and its partial cancellation fails. This failure remains part of the source and independent controls. The actual-contour numerical implementation confirms the tuned result on both prescribed rays and at three interior path parameters. It also evaluates nonzero flat Cartan connections with the correct transported link derivative and a covariant real cell frame. The largest recorded partial-dotF norm is about 5.16e-6 at |K| or |A|=.04; at .01 it is at most 8.07e-8. The wrong total derivative divided by .01 is about .13855. These samples support the construction; the general fixed-depth result follows from the preceding algebra and locality, not from numerical extrapolation.

## 5. Covariant massive elimination and the actual Ward premise

Each right-chart fine fluctuation transforms at its link endpoint. Parallel transport it from that endpoint to the chosen coarse root, then use a fixed orthonormal basis of the cell components. The full frame is orthogonal in the adjoint inner product with determinant modulus one. Its low columns at the trivial background are the four normalized constant one-forms. Every component in a given cell now transforms by the same root adjoint action. Thus fixed low/high projections commute with the allowed background transformations. The frame depends on background, and its derivatives remain in every transformed operator.

For every path parameter, the free high compression is positive at K=0. At K nonzero, H_Wa=0 implies a=D lambda and B_t lambda=0 implies a=0; hence Q_t is positive. Compactness of momentum and the path parameter supplies a common fixed-depth high gap. Analytic continuation in a smaller complex strip and differentiated resolvent identities then give exponential locality of the high inverse, Schur embedding and their finite jets. The same reasoning applies to the square-root profile: 1+d_c*C d_c has spectrum in a fixed-depth compact positive interval starting at 1. This is a gapped functional calculus, not a hidden massless inverse.

The alias frame used for the free calculation and the covariant cell frame require care. One cannot justify arbitrary moving-frame differentiation merely by saying their difference is O(K). More explicitly, align their low coordinates at zero. The alias Schur embedding obeys Q E_alias=U_alias,low q_alias, with q_alias=O(K²). Its violation of the fixed-cell high stationary equation is therefore O(K³), because the high projection of U_alias,low is O(K). Inverting the fixed-cell high block corrects it by O(K³). Up to an analytic low-coordinate factor equal to the identity at zero, the two embeddings consequently have the same leading k_t zero. This verifies the source's claim that the actual embedding absorbs the frame change; no frame derivative was dropped.

The actual normalized Psi and its Hessians, Wilson Hessian, M and C are covariant under simultaneous background gauge changes in these charts. This covariance is compatible with the nonzero off-shell row H_WD: changing the background and fluctuation frame is different from setting a gauge-orbit tangent in an off-shell Hessian. Unique normalized minima and the local tree section preserve covariance up to the internal transformation removed at the roots. Harmonic L, Delta_int^-1, B_t, its root Schur block b_t, Q_t, q_t and rectangular k_t consequently transform in their respective root frames. This provides the Ward premise for these actual operators.

For a local operator K(A) between such root fields, its first background vertex has an analytic joint symbol. The infinitesimal Cartan background Ward identity is

    sum_mu d_mu(p) K_mu^(1)(k+p,k)
      =R(lambda)K_0(k)-K_0(k+p)R(lambda),

with the appropriate input/output actions. The free operators are colour scalar on the charged pair. If K_0(k)=O(k²), set k=0 and p=s e_nu in this analytic identity. The right side is O(s²), so the coefficient of s on the left forces K_nu^(1)(0,0)=0. Analyticity then gives a bound by C(|k|+|k+p|). This works for rectangular k_t as well as square q_t and b_t.

This use of k=0 is an analytic-symbol argument for the local operators before their massless inverses, not an insertion of an excluded zero mode into a finite determinant. The finite antiperiodic Ward identities and local periodization, or equivalently the infinite-lattice local covariance identity, justify the analytic continuation from the momentum meshes. A free double zero without the covariance premise would not suffice: adding a bounded constant first background vertex to a local analytic operator would preserve its free symbol and violate the Ward identity. The actual covariance construction above rules out that counterexample.

All these assertions are for Cartan external backgrounds and the stated charged pair. Those gauge transformations commute with the antiperiodic holonomy and preserve the quantum domain. Generic non-Cartan backgrounds mix root sectors and have not been inferred from this calculation.

## 6. Complete Nielsen grouping and its momentum assignments

Use a fixed covariant cell frame. The exact fine inverse has the decomposition

    Q_t^-1=E_t q_t^-1 E_t*+H_t,

where H_t is the high inverse extended to the full fine space and is local. Since dotF_t=J dotf_t and harmonic scalar elimination gives B_t^-1 J=L b_t^-1, cyclicity in V2 yields exactly

    -Tr[b_t^-1 k_t q_t^-1 e_t(E)]
    -Tr[b_t^-1 h_t(E)],

with e_t(E)=E_t* T_E L and h_t(E)=dotf_t H_t T_E L. Both coefficients are local and linear in E. Background derivatives of the endpoint transports, L, high inverse, tree section and frame are contained in these expressions. They do not create unlisted massless propagators.

Write k'=k+p. There are exactly four mixed E/background groups from the first trace and two from the second. Their separate-centre bounds are as follows; bounded local matrices and fixed-depth constants are suppressed, not propagator factors.

| Differentiated factor | Massless factors before numerator cancellation | Actual numerator/cancellation | Remaining bound |
| --- | --- | --- | --- |
| k_t | abs(k)^-2 abs(k')^-2 | V5 supplies abs(k)+abs(k') | (1,2)+(2,1) |
| q_t^-1 | b^-1(k) q^-1(k) q^-1(k') | k_t(k)=O(k²) cancels one of the two k poles; q_A supplies abs(k)+abs(k') | (1,2)+(2,1) |
| b_t^-1 | b^-1(k) b^-1(k') q^-1(k') | k_t(k')=O(k'²) cancels one of the two k' poles; b_A supplies abs(k)+abs(k') | (1,2)+(2,1) |
| e_t | b^-1(k) q^-1(k) | k_t(k)=O(k²); e_A,E is local | (2,0) |
| b_t^-1 in the high trace | b^-1(k) b^-1(k') | b_A has degree one; h_E is local | (1,2)+(2,1) |
| h_t in the high trace | b^-1(k) | h_A,E is local | (2,0) |

Here (a,b) denotes |k|^-a|k+p|^-b. In the two three-propagator cases the free k zero is at precisely the duplicated momentum, as obtained by following the cyclic matrix products. Moving that numerator to the other centre would leave a nonintegrable fourth power at the wrong centre; that operation is not used.

## 7. Complete residual groups, one-point terms and external maps

Define R_0(U)=R(U,m(U)) and R_rho(U,rho)=R(U,m(U)e^rho)-R_0(U). Only on the actual saddle is their sum identified with the original Delta_n. At fixed U the four rho-dependent determinants have weights

    L_harm: +1/2;    Delta_c: -1;    G_c: +1/2;    H_h: -1/2.

The other four determinants in expanded A5 depend only on U and cancel from R_rho. H_loc inside L_harm is the complete actual unminimized soft Hessian, and H_h is its actual orbit Hessian. No h-minimization inverse has been silently omitted: the h determinant is explicitly retained.

For each weighted log determinant, the full mixed derivative is Tr(G O_A,rho)-Tr(G O_A G O_rho); the full repeated residual derivative is Tr(G O_rho,rho)-Tr(G O_rho G O_rho). If O=O_0+epsilon O_1+epsilon² O_2, the coefficient instead reads Tr(G O_2)-1/2 Tr(G O_1 G O_1). The outer determinant weight must still be applied. Independent direct determinant-polynomial differentiation confirms this convention and rejects the missing-half formula.

Eliminate massive bands with their log determinants retained. For L_harm the low simple-pole bound is the preceding harmonic result; for Delta_c, G_c and H_h the free scalar low symbols are quadratic and positive away from zero. Their A vertices obey the actual Ward lemma. Rho and mixed A,rho vertices are bounded local kernels, without requiring a false derivative improvement from the residual amplitude itself. Hence every mixed bubble has (1,2)+(2,1), every mixed tadpole has (2,0), every repeated-rho bubble has at worst (2,2), and every repeated-rho tadpole has (2,0). The massive determinant parts are analytic.

The free one-point coefficients vanish on the paired real root plane. The Wilson row is a commutator insertion. Also, for anti-Hermitian X,Y,Z,

    Re tr(XYZ)=1/2 Re tr(X[Y,Z]).

It follows directly by conjugating and reversing the trace. Thus cubic real-trace tensors of the actual action are commutator tensors; eliminating intermediate variables at cubic order contracts them with colour-scalar quadratic inverses. The first frame, M, C and square-root-profile derivatives have the same adjoint structure. On the free antiperiodic pair, all spatial operators are colour scalar and the commutator colour trace is zero. This relies on the paired real domain and the specified scalar -1 twist. It is not a claim about a single complex root with an unmatched phase regulator.

Consequently c_E(1)=0 and (R_rho)_rho(1,0)=0. The actual saddle equation gives E_W=-Psi_U and, at first order, E_W,1=M*C^-1 rho_1. The complete second derivative of R_0 along the saddle is therefore 2<Dc_E[U_1],E_W,1>; the term c_E(1)E_W,2 vanishes. Since R_rho(U,0)=0 identically, its complete second derivative is

    2(R_rho)_U,rho[U_1,rho_1]
      +(R_rho)_rho,rho[rho_1,rho_1].

There is no omitted contribution from second derivatives of the external tree/residual maps. These disappear because the corresponding one-point coefficients have actually been shown to vanish, not because their external fields are small.

## 8. The finite regulator, volume passage and continuity

The common regulator is the paired real antiperiodic charged-root space for every fine/coarse/ghost matrix, with periodic external Cartan momenta. Fine and coarse twists correspond around the same cycles. All finite determinants and the path use ordinary invertible matrices in that sector. Exact finite gauge covariance is preserved; this is not a hard continuum momentum cutoff being assumed covariant. No pseudodeterminant or root pin is substituted.

At fixed depth, the local jets and massive inverses have volume-uniform exponential bounds. On an antiperiodic momentum mesh the nearest distance to a singular centre is comparable to T^-1. A periodic external shift preserves that mesh. Counting sites in dyadic annuli yields, for s<4,

    T^-4 sum_{|k|<r} |k|^-s <= C_s r^(4-s).

For r below the first mesh point the sum is empty; otherwise each shell has at most C(T r_shell)^4 points and the geometric shell sum gives the stated bound. The same estimate applies around -p. This verifies uniform integrability, including the moving centres, rather than appealing only to homogeneous total degree.

For example, with x=|k|^-1 and y=|k+p|^-1,

    x y² <= (x³+2y³)/3,

because x³+2y³-3xy²=(x-y)²(x+2y)>=0. The other mixed term is symmetric. Thus all mixed groups are controlled by translated cubic or quadratic singularities, with uniformly small integrals/sums on small balls. Away from these balls the analytic periodized symbols converge normally. It follows that the finite per-site sums converge to the common Brillouin-zone integrals and that the integrated mixed response is continuous at p=0. The constants are uniform along the compact path at each fixed depth, so its parameter integral also commutes with this controlled limit.

A fixed continuum p is understood through admissible periodic external momenta tending to it, with volume taken first. The uniform local bounds make the choice of approximants immaterial. The antiperiodic shift then keeps both singular centres off every finite quantum mesh.

For a (2,2) bubble at fixed nonzero p, balls around 0 and -p contribute bounded amounts; outer shells from scale |p| to a fixed radius contribute at most C(1+log(1/|p|)). This is the claimed logarithmic bound. Only after taking the volume limit is p sent to zero. With each actual rho_1=O(p²), division by the transverse Wilson p² normalization leaves O(p²(1+log(1/|p|))), which tends to zero. No uniform-in-depth constant or reversed order of these limits has been invoked.

## 9. Ward pairing and the precise zero coefficient

Pull the Nielsen coefficient back to the coarse residual by the local map C^-1 M, and compose with the actual local tree section. Its background response is covariant under the allowed coarse Cartan gauge transformations and its value at the trivial field is zero. The same is true of the one-residual coefficient of R_rho. Their first responses Y_N(p),Y_rho(p) therefore annihilate the coarse pure-gauge direction d_c(p). This statement includes the tree-section response and the local root-frame derivatives.

The preceding separate-pole argument proves their continuity at zero. In Y(p)d_c(p)=0, set p=s e_mu, divide by s, and take the limit. Every column of Y(0) is zero. Thus Y_N(p) and Y_rho(p) tend to zero. Pairing either response with rho_1=O(p²) and dividing by the Wilson p² density gives a vanishing mixed contribution. The repeated residual contribution vanishes by the logarithmic bound above.

For the Cartan plane wave and phase-averaged transverse normalization used in UIR55 250–259, this proves the residual coefficient is zero for the paired charged-root sector in the specified order of limits, at each n>=1. It is a statement about the coefficient after those limits; it is not a uniform finite-momentum estimate as n tends to infinity. The value zero has no n-dependence, but the local constants and neighborhoods used to prove it can depend on n.

This conclusion is not the old scalar-model cancellation or the old IC/IRL matching assumption relabeled. The present route uses the actual local soft Hessian at rho=0, its actual covariant vertices, an exact finite normalized gauge-change identity with the Wilson row retained, and a complete six-group/four-determinant pole ledger. The potentially super-marginal terms in the h-minimized Phi organization are handled by changing to this exact saddle representation and retaining all its factors. The older observation that an individual longitudinal term can be nonzero is not contradicted or discarded.

## 10. Independent evidence and remaining boundary

[Actual lattice implementation](checks/review_residual_vertices_01.py), [complete stdout](checks/review_residual_vertices_01_out.json) and [stderr](checks/review_residual_vertices_01_err.txt): **162/162**, empty stderr. The code enumerates all 24 orderings and all 81 cell sites, transports every oriented right-link insertion on the actual contours, builds Wilson curl rows independently, and constructs a covariant orthonormal cell frame. It checks MD=d_c ev, H_WD=0 on the nonzero flat Cartan backgrounds, the internal gap and the tuned Schur/partial-dotF behavior. It retains both the straight-path and wrong-total-derivative controls. Numerical evidence is confined to those samples; the operator/domain/limit claims use the proofs above.

[Exact independent implementation](checks/review_residual_vertices_02.py), [complete stdout](checks/review_residual_vertices_02_out.json) and [stderr](checks/review_residual_vertices_02_err.txt): **30/30**, empty stderr. Besides the actual nonflat SU(2) Wilson Hessian, it checks noncommuting V1/V2 ratios, nonzero off-shell effects, scalar-normalization and half-bubble controls, the rational tuned curve, the separate-centre domination identity and residual logarithm suppression. The full raw output is retained, including an unsimplified exact row-norm expression; it is not evidence of an additional estimate. No author helper was imported. No failed unexpected predicate was discarded; the designed wrong-formula routes all reject.

The source's 13 exact author controls were inspected completely and are consistent with their stated algebra-only scope. They do not themselves prove the Ward or regulator passage; those steps were reconstructed independently here.

No mathematical correction is required to the frozen unit. The six-link packaging paragraph is confirmed as a single metadata insertion with all links resolving, without extending the prior bridge review to this unit by citation alone.

The conclusion must retain its domain. A common antiperiodic regulator can be chosen for a given charged pair, but that does not supply a common full-colour periodic prescription or identify every neutral zero-mode/Gram factor. Generic non-Cartan background variations mix sectors. The neutral/full-periodic comparison therefore remains an explicit bridge for any consumer requiring the original full theory. Even after that bridge, the common weighted tree bounds H1/H2/H3, the remaining nonlinear/flow inputs, existence/reconstruction and the actual uniform physical infrared estimate are separate obligations. The auxiliary high/internal gaps used here are not a Hamiltonian mass gap. This report certifies no whole-PR PASS, audit verdict or completion of the user's full Yang–Mills goal.
