**Focused independent check — initial-phase elimination and two-chirp operator**

The cumulative-count map, exact state-annihilating contrasts, count-error propagation and restricted chirped inverse are mathematically consistent in their declared models. The initial-phase v2 source correctly repairs the combined operator/count-error qualification found in v1. The chirped v2 source correctly points to that repaired result. A further scope issue remains in the source version bound below: covariance alone does not justify calling the optimized contrast unbiased. That finding and an exact probability-model counterexample are preserved here for the author's announced wording correction.

This is a focused independent mathematical check, not a formal audit, landing review, retained-status decision or physical scalar test. I read the complete initial-phase v1 and v2 notes, the complete chirped v1 and v2 notes, and the full chirped v1-to-v2 diff. The only chirped revision is its dependency pointer. I did not read, import or rerun the author's control programs. My new program uses its own exact rational row reduction, inverse, null space, projector, sample covariance and phase-history implementation. No observation product was opened.

| Source or evidence | SHA-256 |
| --- | --- |
| `INITIAL_PHASE_ELIMINATION_v1.md` | `af50288fa56e9a6e18f01bbf12956ec85d1a33f64b39182e470cec159e9e93ff` |
| `INITIAL_PHASE_ELIMINATION_v2.md` | `e1966dbf396ff12892818b4dafd585e8ff3473c96b421d89d7a100c6f16ec856` |
| `CHIRPED_COHERENT_PHASE_OPERATOR_v1.md` | `fbccc83584029ff10d5fccb234f85341190973f44159ffc06c111e1a0e370dbf` |
| `CHIRPED_COHERENT_PHASE_OPERATOR_v2.md` | `f37d259802a6277ca2b97b86e5280b5f603b28328878a552b0cad572f66d7a7a` |
| `independent_initial_phase_chirp_v1.py` | `f60366b98fd9d91856c226ee1a6020b29e37c236525ed0870a4827eb28bebdd8` |
| `INITIAL_PHASE_CHIRP_INDEPENDENT_RESULTS_v1.json` | `e36a9d092ad84793e10305b5445b014e2ba02c5438ef939e62ef3e7f2c237082` |
| `UNBIASEDNESS_COUNTEREXAMPLE_v1.json` | `66739cca4883067bda19febb679e9b37a946cdd6a97854b6b7e4192cbe25c31e` |

Each note version is preserved as an exact `*_SNAPSHOT.md` in this directory. The earlier plasma report, `REVIEW_FINITE_COUNT_PLASMA_v2.md`, remains unchanged at SHA-256 `9290eee04f5e237ffdf6b16df1c85b408b0c7ed4bee12d2982eb677b40a9b553`.

**Initial-phase identity, converse and estimator scope**

In fixed phase units, telescoping measured increments gives `q_i=q_0+c_i`. Applying the first inverse row proves `G=r+W q_0`. If `h^T W=0`, the contrast is independent of the initial phase. Conversely, for real nonzero row `u=h^T W`, shifting every endpoint phase by `u^T` preserves all increments while changing the contrast by `||u||^2`. Applying each known inverse `B_i^-1` supplies corresponding latent histories. This proves the stated converse in the unrestricted linear-state class; it does not establish that the shifted histories satisfy extra physical constraints. Rank-nullity gives the dimension and the constant-operator special case.

Appending the supplied nuisance columns `H` is algebraically correct. The projection formula follows without a fitted initial phase: for any feasible contrast, `h^T P s=1`, so Cauchy-Schwarz gives `||h|| >= 1/||P s||`; equality gives `h=P s/(s^T P s)`. If `s` lies in the nuisance span, all allowed contrasts remove it. This is a statement about the declared signature and nuisance model, not a physical indistinguishability theorem or justification for deleting actual nuisance processes.

The deterministic error bound is valid even with nonzero bias. However, the source's phrase “minimum-variance unbiased contrast” needs an additional error-mean premise. Consider three endpoints with nuisance column `(1,1,1)`, signature `(0,1,2)` and contrast `(-1/2,0,1/2)`. Let `epsilon=(3/7)s+xi`, where the three components of `xi` are independent symmetric signs. Its covariance is exactly the identity, while the contrast bias is `3/7`. The normalized contrast and minimum-norm calculation remain correct. A statistical unbiasedness statement additionally requires zero-mean remaining errors, or correctly removed known means, including any count errors used in that estimator. The author has accepted this qualification; confirmation of the corrected source belongs in a separate source-bound addendum.

For count errors I independently formed every cumulative endpoint error and then applied the contrast. Interchanging sums yields exactly `b_k=sum_{i>=k} h_i v_i`. Direct variance over correlated rational samples agrees with `b^T Sigma b`. The deterministic componentwise bound is attained by errors with signs matching the corresponding coefficients. Even independent increments do not make cumulative endpoints independent: for four scalar endpoints the covariance is `min(i,j)`; contrast `(0,-1,0,1)` has variance 2, while discarding those off-diagonal covariances gives 4. Also, the pure count-derived endpoint covariance has a zero initial row and can be singular. The positive-definite `C` optimization in the note is therefore a separate conditional case, not an automatically available covariance model.

**Operator uncertainty: repaired joint bound and remaining domain**

The affine-family construction is exact when every allowed inverse-row family is actually of the specified affine form. Annulment of all coefficient columns removes the initial-phase contribution for every parameter in that family. This is a sufficient construction; it does not justify truncating a nonlinear physical inverse.

My independent remainder witness uses nine endpoints `t_i=i/8`, rows `W_0=(1,t,t^2)` and `W_1=(t^3,t^4,t^5)`, and a sixth finite-difference contrast. It annihilates both coefficient matrices. Adding the omitted term `lambda^2(t^6,0,0)` gives nonzero leakage with zero counts. At `lambda=1/2`, a specified initial phase gives leakage 1; doubling it gives 2. Each row is realized as the first inverse row of an explicit invertible matrix. Thus the witness is internally consistent, while not purporting to be a radio-link realization. A bounded parameter interval alone cannot control remainder times an unrestricted initial phase.

V1's joint-error wording did not specify which count coefficients to use when its operator bound uses observed cumulative counts. The repaired v2 identity is

    h r_0(c_obs) - h r_lambda(c_true)
      = h[r_0(c_obs)-r_lambda(c_obs)] + b(lambda)^T eta.

The first term uses observed counts, while the second uses true-family coefficients or a justified uniform bound on them. My exact counterexample has equal endpoint inverse rows `(1+lambda,0,0)`, contrast `(-1,1)`, nominal parameter 0, true parameter 1, true increment `(1,0,0)` and error `(-1,0,0)`. The observed increment and data-based operator bound vanish. The nominal count bound is 1 but the actual error is 2; the true-family bound is 2. V2 explicitly preserves this example and repairs the formula. I tested its exact decomposition and the conservative affine-family joint bound at 41 rational parameter values, with an arbitrarily large initial phase that cancels exactly.

The remaining mathematical bound uses a fixed dual norm pair and triangle/Hölder inequalities. It does not estimate the allowable chirp family, count error, clock errors or physical residuals. In particular, rank two for each known chirp history does not by itself produce one contrast robust to every uncertain history: the nuisance shapes can change with that history. A real robust family still needs a physical supplier.

**Chirped phase operator and physical normalization**

The declared station-time phase derivatives are consistent with the fixed reference factors. The geometric term is `k[Phi(s+G)-Phi(s)]/(kF)`, whose linear coefficient is `f(s)/F`. Its remainder is bounded by `sup|f'| G^2/(2F)` on the full connecting segment. I checked this with exact quadratic frequency chirps, signed displacements and the coherent ratios retained through normalization.

Starting separately from coherent uplink phase transfer and the downlink plasma contribution gives

    [k U/f_u + D/(k f_u)]/(kF)
       = U/(F^2 s) + D/[(kF)^2 s].

Thus the proposed fixed-unit matrix `B=[s,diag(1/s)a,diag(1/s)b]` follows within the stated separable local-frequency/common-ray eikonal class. It does not require instantaneous carrier division of measured counts. The distinction repaired in the earlier plasma note remains intact.

For the inverse I compared direct exact inversion with the proposed row, not two copies of the same formula. Multiplying `B` by `diag(s)` gives `[s^2,a,b]`; the first-column replacement determinant gives `det B=det A0*D_s/(s_X^2 s_K)`. The independent Leibniz determinant and inverse agree. Substituting the reference definitions simplifies

    D_s=(f_K^2-f_X^2)/(F_K^2-F_X^2),

under the stated invertible-`A0` reference choice. Equal positive uplink frequencies therefore make this matrix singular; downlink diversity is separately needed. Distinct frequencies alone provide no uniform conditioning margin near equality. Any uniform physical error budget must bound the inverse over its actual uncertainty family.

The inverse row always lies in the span of `(w01,w02,0)` and `(0,0,w03)`, with endpoint coefficients `s_X/D_s` and `s_K/D_s`. These channel vectors are independent under the stated positive/nondegenerate conditions. Their coefficient ratio is `s_K/s_X`, proving rank one for constant relative chirp and rank two when two sampled relative chirps differ. The consequent contrast count is correct for known nonsingular endpoint operators. For a common chirp, constant channel weights give `sG`, not `G`; the note correctly preserves that target difference.

The independent program exercised two coherent-ratio families, one using the sourced Cassini ratios but wholly synthetic carrier histories. A nine-endpoint example has `rank(W)=2`, seven initial-phase-free contrasts, and `rank([W H])=4` after two specified synthetic nuisance columns. These are exact constructed results, not fitted data or evidence of actual mission simultaneity.

The program exited 0 with 1,281 correlated exact checks and zero failed checks. That computational result does not erase the separate unbiasedness wording finding, which required an additional counterexample after the first run. The JSON records per-family coverage, numerical witnesses and limitations. The chirped v2 dependency-only change was fully read and confirmed after the run; none of its mathematical formulas changed, so the same controls apply without a rerun.

**Physical conditions that remain supplied**

The chirped construction assumes two coherent uplink phases with known station-clock derivatives, fixed turnaround ratios, shared nominal emission/bounce/reception maps, common retarded plasma paths and proper-length measures, and frequency factors separable into an uplink frequency times a shared achromatic map. The local frequency used in the plasma law must be consistent with those clock and medium frames. These are substantive conditions, not consequences of a common archive date or of the revised scalar action.

`G` is the chosen common nondispersive displacement in that model. It is not identified with gravity, and the separately included plasma phase must not be counted again as part of that displacement. Ray changes, shifted plasma evaluation, nonstationary-medium effects, higher-order dispersion, electronics errors and the geometric Taylor remainder remain in the residual with as-yet-unsupplied physical bounds. The note explicitly retains these obligations. The exposed X/X data do not supply the two additional coherent band phases needed by this operator.

Initial receiver phase is eliminated only for the demonstrated contrasts in the supplied model. Scalar initial state/history, action and potential, absolute scales, physical environment and candidate-consistent trajectory remain open. All new files were confined to this independent evidence directory. No author source, earlier review, raw measurement, campaign state, branch, commit or scientific status was changed.
