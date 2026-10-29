# Independent review of the full-colour residual determinant unit

The bounded result is independently confirmed: **the complete residual F² coefficient is zero at each fixed finite depth in the specified infinite-volume/a.e.-Bloch one-loop convention, with volume taken before external momentum tends to zero**. The exact neutral quartic formula is also confirmed. Its uniform weighted estimate is a valid implication from FC19; **FC19 itself remains OPEN**. Neither full Yang–Mills existence nor a positive gap of the physical continuum Hamiltonian is certified.

There was one minor prose finding, now repaired and confirmed in this reviewer context. No remaining material mathematical repair finding was identified within FC1–FC20. This is a source-bound proof-unit review, not a whole-PR review-loop PASS, landing decision, audit verdict, or retained-grade promotion.

## 1. Scope, independence and frozen identities

The reviewed unit is [RESIDUAL_FULL_COLOUR_ASTRA.md](RESIDUAL_FULL_COLOUR_ASTRA.md), including all FC1–FC20 and the evidence claims. Its original 36,936-byte source has SHA-256 `e18ce796044a7f1a1f0a086043e5c072ed7e8b7da9af5097ff34e64526de7944`. The original [author manifest](checks/residual_full_colour_manifest.json), SHA-256 `b9d56d20ad5f123720259f37d66f9e7030f802e013083cda38f3fa7252401bb7`, remains unchanged. It records the 2026-10-29 16:26:42 UTC freeze and author head `63e393bb56f1c51733aabedfca20b65786ee87f3`; the original source is preserved at commit `47a916398fb58231d809695485812faf25c70ce9`.

The repaired 36,980-byte source has SHA-256 `1ce9460989e5491bd491dcc348add15207e63013a0c537cd6c51caa19f0e3dd7`, at commit `4f04b662f4d72d7ef269f6d9693ae9ff6424acf9`. A byte comparison establishes that the entire change is the single FC3 sentence described below. No formula, implementation, output or mathematical premise changed. Both versions are bound by the [source/read manifest](checks/review_residual_full_colour_source_manifest.json), SHA-256 `5ff4aa8f7de932cb58d0c9c723cd27d3c233c55457241beffa5855c9f65abe20`.

Reviewer dispatch was user-selected Astra/max. The visible worker identity is GPT-6 generically; no independent runtime model introspection is claimed. This is a same-family, separate-context review, separated from authorship and with distinct mathematics and implementations. It is not cross-family confirmation. The coordinator owns integration, source repairs and the worktree lock; this reviewer wrote only this report and its named `checks/review_residual_full_colour_*` artifacts. No workers were spawned and no Git, PR or audit state was mutated by this reviewer.

The installed physics-loop and review-loop entrypoints were read. The governing current-main methodology and applicable references were read at the coordinator-fetched revision `ca2bc7ddf64790da96cd43d42017d000fbfe4808`; the local `origin/main` identity was verified. The [falsification contract](checks/review_residual_full_colour_criteria.md) was saved after reading the target and before the independent controls. It specifies normalization, cubic-source, domain/Gram, Ward, exceptional-fibre, consumer/limit-order and uniformity falsifiers. The second lattice implementation has its own [pre-execution criteria](checks/review_residual_full_colour_02_criteria.md).

The actual mathematical dependency chain was read, rather than importing prior confirmation labels: [residual determinant construction](RESIDUAL_DETERMINANT_ASTRA.md) and its [review](REVIEW_RESIDUAL_DETERMINANT_ASTRA.md); [harmonic lattice construction](checks/residual_det_lattice_bridge_working.md) and its [review](REVIEW_RESIDUAL_LATTICE_BRIDGE_ASTRA.md); [actual charged vertices](checks/residual_det_vertices_working.md) and their [review](REVIEW_RESIDUAL_VERTICES_ASTRA.md); [fixed-depth recovery](RECOVERY_UIR_ASTRA.md) and its [review](REVIEW_RECOVERY_UIR_ASTRA.md). Those complete notes/reports were read. The necessary normalized-action, Schur, contour, coupling and producer passages in [FLOW](FLOW.md), [FLOW55](FLOW55.md), [UIR55](UIR55.md), [UIR2_55](UIR2_55.md), [PROOF](PROOF.md) and [BFT34_55](BFT34_55.md) were read in the ranges recorded in the manifest. The [UIR consumer review](CODEX_REVIEW_UIR.md) was also read in full. Broad contextual files were not reviewed in full; hashing their bytes does not expand that coverage.

## 2. Neutral coefficients and the stationary quartic value

For commuting fields the plaquette phase is linear in the links. Two neutral quantum derivatives of the normalized Wilson action therefore give `d₂* diag[N⁻¹ Σ_j h_Aj h_Bj cos(f_j)] d₂`. This immediately proves the off-shell identity `H_W d=0`, but its second background derivative is nonzero. At the free point the gauge-completed inverse is `λ(q)⁻¹ I` off the harmonic kernel. The trace of a single plaquette curl against this inverse has density `(1−1/V_f)/2`: symmetry gives equal contributions from the four difference components and their sum is one at every nonzero momentum.

Combining the minus one-half in the cosine vertex, the one-half vector log determinant, and `Σ_A h_Aj h_Ak=Nδ_jk−1` gives exactly

`β_neutral[W^perp]=−(N−1)(1−1/V_f)/4`.

The Wilson normalization is essential: its quadratic background action is `Σ f_j²/(2N)`. No neutral ghost term cancels this within the fine Wilson group, because the neutral scalar Laplacian is background independent. Thus FC1 is a genuine nonzero finite coefficient. Its infinite-volume value is `−(N−1)/4`, with no claim that the level-n neutral finite part has that same value.

For the soft term, put `M_j=e^(i barθ_j) E e^(i z_j)` and `E z_j=0`. Direct expansion gives `|M_j|=1−μ₂j/2+μ₄j/24+O(6)` and `arg M_j=barθ_j−μ₃j/6+O(5)`. Expanding `|M_j|[1−cos(b_j−arg M_j)]` gives all three FC2 quartic terms, with coefficients `+1/6`, `−1/4`, `−1/24`. The fourth central moment cancels at this order; the variance term does not. Multiplication by `κ/N` is required by the actual normalized density.

The SU(N) maximization constraint cannot simply be ignored at all orders. Its cubic common trace-phase correction is orthogonal to the traceless first-order residual, so it does not change the degree-four value. Equivalently, the actual constrained maximum and the polar expression differ first at degree six, as can also be checked directly through the Lagrange multiplier. The exact SU(3) control makes that cubic center correction nonzero and checks its trace constraint, stationarity and quartic cancellation.

There is no cubic exchange in this restricted quartic calculation. Every cubic action tensor involving two Cartan inputs and an arbitrary internal colour is a commutator tensor; the two Cartan matrices commute. This includes a charged internal direction, not just a third neutral direction. Thus the second-order stationary displacement sourced by two neutral external fields vanishes on the fixed gauge slice. At degree four the unknown cubic displacement pairs with the quadratic stationarity equation and drops out. The remaining value is precisely the Wilson quartic plus the sum of the FC2 quartics evaluated on the **actual linear stationary chain**, proving FC18. The general charged cubic exchange terms remain present outside this restriction.

## 3. Scalar domains, harmonic vectors and gauge completion

The finite-dimensional domains in FC3–FC9 are consistent when all scalar constants and all four neutral harmonic one-forms per colour are tracked.

Let `Δ=d*d`, with root and interior injections `J,I`. Eliminating the positive interior block gives `Δ L_har=J S`, `L_har 1_c=1_f`, and `ker S=span(1_c)`. On mean-zero coarse scalars, the **column `Δ L_har`** has Gram `S²`. Its range projector is consequently `J P_cperp J*`; its orthogonal complement is

`Q_per=P_int+J P_c0 J*`.

The extra root-mean term is necessary. Removing it makes the candidate completed ghost lose its constant left kernel. In fact the omitted row contributes `1_c*J*Δ`; the remaining naive row has `1_f*F_naive d=−1_c*J*Δ`, generally nonzero. A calculation retaining the same mean-zero left domain after deleting this term is not a valid quotient.

**Resolved finding.** The original FC3 prose, at line 70, called `S²` the Gram of the harmonic lift itself. Literally `L_har*L_har` is a different matrix, and `L_har*Δ L_har=S`. The displayed formula already used the correct gauge-fixing column. The coordinator changed only the sentence to “The gauge-fixing column Delta_f L_har on that parameter space has Gram (S|1_c-perp)^2.” I confirmed the exact replacement in this same context. The [finding record](checks/review_residual_full_colour_findings.json) binds the old/new hashes and the [coordinator repair record](checks/full_proof_residual_full_colour_gram_fix.json), whose SHA-256 is `71ab2638e044c35b63846de773494e73f5ce4d442db6ae9481db944efc203baf`.

The scalar determinant factor can be derived without assuming a pseudodeterminant congruence rule. Delete one root row and column. Interior Schur elimination gives the fine cofactor as `det A` times the corresponding cofactor of `S`. Since the constant kernel is simple, the pseudodeterminants are the cofactors times `V_f` and `V_c`, respectively. Their ratio is `V_f/V_c=ell⁴`, proving FC4. This is an orthogonal constant-mode prescription, not a site-pinned Green function.

For FC5, covariance gives `M d=d_c ev`, and `R_c^(1/2)1_c=1_c`. In harmonic scalar columns the completed ghost is block triangular with upper-right zero and lower diagonal block `R_c^(1/2)Δ_c`; its lower-left root-mean row must remain. Direct multiplication shows that both its left and right kernels, in the original counting spaces, are the same constants as those of `Δ_f`. The same cofactor argument, with `R_c` preserving constants, gives FC6, including `ell⁴` and the constant eigenvalue one of `R_c`. No moving-kernel derivative is needed here.

Harmonic one-forms require another normalization. Adding a constant commuting fine form `a` and `L^j a` to every level preserves each Wilson curvature and multiplies every contour average by the corresponding common phase. The normalized soft energy is unchanged for arbitrary commuting background and residual in the chart. The joint harmonic kernel is therefore fixed; its h-component is zero. Counting norms give the transfer between normalized constant vectors as `ell⁻¹` from fine to coarse and `ell` in the opposite parametrization. Their graph Gram factors are `1+ell⁻²` and `1+ell²`, each raised to `h=4(N−1)`.

For a positive block operator, elimination of an invertible block embeds the Schur kernel as `z ↦ (−A⁻¹Bz,z)`. Regularizing this fixed kernel by a small positive eigenvalue gives FC7 with its graph Gram determinant. The gauge harmonic shear is orthogonal to constant one-forms and introduces no extra harmonic Gram. Applying this identity in both orders, together with the scalar cofactor factors, yields FC8 and the residual constant in FC9:

`R_per(U,m(U))=Γ_Fbar1(U)−Γ_d*(U)−h log ell`.

The difference of the two Γ terms is independent of the gauge row because `H_W d=0` off shell, on the common fixed scalar and harmonic quotients. One may verify this by decomposing link space into transverse and gradient parts and eliminating the gradient block; the determinant of `F d` cancels the entire gauge completion. The harmonic ratio contributes `−h log ell`, not zero. It is constant in **both** U and ρ and has no Taylor coefficient. Its per-coarse-site density tends to zero, but that limit is not used to justify discarding a derivative-dependent term.

## 4. Complete neutral residual and the periodic defect

Neutral first background/residual vertices vanish at the origin, so every second log-determinant variation is a tadpole with the **actual full second vertex**. The four weights in FC10 are `+1/2, −1, +1/2, −1/2`; the neutral `Δ_c` vertex happens to be zero. Massive determinants produced by elimination remain in this statement. The general mixed formula has bubble coefficient `−w`, or `−1/2` in an epsilon-squared trace-log expansion; the bubble vanishes here because its two first vertices vanish, not because its normalization was changed.

For the mixed neutral vertex, a fine neutral gauge shift changes U and its coarse mean together while leaving ρ and the neutral quantum coordinates unchanged. After the local stationary section is composed, the corresponding Ward identity is an identity for the actual vertex before inserting the massless propagator. Its fixed-depth analytic symbol obeys `Σ_mu d_mu(P) O_A_mu,rho(K;P,−P)=0`. Approaching zero along each coordinate direction gives a zero constant term in every component. Thus it is `O_n(|P|)` uniformly in K. The repeated-residual vertex is bounded at this fixed depth. No discontinuous external transverse projector has been extracted and renamed an analytic coefficient.

The local free inverse has a simple acoustic pole and a fixed-depth high gap. The root-mean correction is supported at the single coarse K=0 fibre, is independent of U and ρ, and changes only a bounded high compression after the harmonic kernel is removed. Its differentiated trace-density correction is therefore `O_n(T⁻⁴)` times the bounded second vertex. For the other fibres, `T⁻⁴ Σ_(K≠0) λ(K)⁻¹` is bounded in four dimensions. Inserting the bounded first background map and `ρ₁=C_n H_n(P)v=O_n(P²)` gives FC12, hence FC13. This proves a zero **complete residual** coefficient while leaving the nonzero individual neutral finite parts intact.

The charged finite-periodic statement has a different domain: it is explicitly a fixed-free-complement Taylor regulator, not a nonlinear pseudodeterminant through a changing stabilizer. At a nonexceptional momentum fibre, all the actual Schur, gauge and ghost identities are ordinary invertible finite matrix identities. Differentiating them through two external insertions is legitimate there. Local stationary inverses and massive blocks are bounded at each fixed n; the reviewed charged vertices provide the requisite actual numerators, not only formal covariance.

At an exceptional fibre the inverse relation is `G O=O G=1−P₀`. In the finite expression obtained by the eliminations and two derivatives, telescope each use of an inverse identity. Every discrepancy contains a Fourier kernel projector. The same block argument treats terms introduced by inserting a fixed free-complement compression or comparing the kernel graph factors. This does not assert that either omitted domain term vanishes separately.

There are only two external insertions. After phase averaging the nonzero ordered transfers are `(P,−P)`, `(−P,P)`, or a net-zero second vertex. A projector insertion anchors the loop momentum, so all remaining inverse factors in that word occur at `0,P,−P`, modulo the fixed alias identification. Unmatched `(+P,+P)` terms do not contribute to the phase-averaged density. In particular there is no free momentum summation left that could put another inverse a distance `1/T` from zero. Zero acoustic eigenvectors are set to zero; retained high blocks stay bounded. Other inverse factors are bounded by `C_n(1+|P|⁻²)` for fixed nonzero P. The finite number of factors therefore gives exactly the FC15 form

`C_n T⁻⁴ (1+|P|⁻²)^(m_n)`.

This is a support and inverse-norm proof. It does not rely on finite rank alone, give a useful joint n/P bound, or justify sending P to zero first. The independent charged covariant-Laplacian control demonstrates that the fixed-complement defect can actually be nonzero: it has epsilon-squared coefficient `−1/2`, whereas the true moving pseudodeterminant is constant. Its density is `−1/162` on the actual 3⁴ torus. This makes omission of projector/Gram terms detectable rather than tautologically assuming them absent.

The nonexceptional charged grouped terms have separate-centre exponents `(1,2),(2,1),(2,0)` for the mixed response and at worst `(2,2)` for repeated residuals. At fixed nonzero P each centre has exponent below four. Periodic deleted-centre and antiperiodic meshes satisfy the same dyadic shell bound `C r^(4−s)` for exponent `s<4`. Away from small balls the symbols are identical and ordinary Riemann sums converge. These two facts prove convergence to the same integral, including for admissible `P_T→P`; FC15 accounts for the remaining exceptional fibres.

Only then may P tend to zero. The mixed bounds are uniformly integrable at merging centres: for example `x y² ≤ (x³+2y³)/3`, and the exponent-three singularities are integrable. The actual grouped Ward identity kills the resulting continuous constant coefficient. Repeated residuals have at most logarithmic growth, which the two external `O(P²)` factors suppress after division by the Wilson P² density. These are the actual bounds established in the [charged vertex source](checks/residual_det_vertices_working.md), reconstructed with its full local/gauge pairing; a generic EOM-proportional functional would not suffice.

## 5. Consumer equality, depth and the conditional producer

The consumer comparison is substantive. [FLOW, Def F-g](FLOW.md) defines the coupling through the infinite-volume Hessian. [UIR55 §5 and late erratum E-2](UIR55.md) explicitly retain the finite neutral sector and state the split fibrewise for almost every level momentum. The normalized joint Hessian and its ghost/Gram factors in the predecessors agree with that split on those nonexceptional fibres. The preceding estimates prove convergence of the actual grouped coefficient to precisely that integral. Thus FC16 concerns the original stated **Gaussian one-loop** consumer, rather than a coefficient of a newly substituted finite-torus functional.

A Cartan background decomposes the quantum fields into the neutral block and real root pairs. A regular Cartan external direction avoids accidental zero root charges; after removing the regulators, global Ad invariance fixes the full colour Hessian to the invariant quadratic form. The finite sum of zero root-pair residual coefficients and FC13 therefore gives `Rho_n^full=0` for every fixed n≥1. This reasoning does not assume that simultaneous root-pair antiperiodicity defines a full SU(N) bundle. It also does not identify a nonlinear finite-torus stabilizer integral with this Taylor coefficient, or prove the SF-infinity polymer comparison.

For any two fixed depths in the claimed range, their extracted residual coefficients differ by zero. No depth-uniform constant or interchange of n with either limit is needed for this arithmetic conclusion. Subtracting the corrected TEL identities then gives FC17 with the displayed sign of `a^perp(J_n)−a^perp(J_j)`. At depth zero the unblocked residual, if included in the increment convention, is identically zero. The finite-part differences may still grow; their uniform boundedness or sufficiently small linear increment bound is not supplied by the residual cancellation.

FC19 is an explicit sufficient hypothesis about the **actual linear** curvature, spread and residual responses. It is not a restatement of the full nonlinear quartic conclusion. Given its weighted row and column bounds, polarize each FC18 product. Anchor one external leg and use its column bound; use row bounds for the other three. The diameter weight is bounded by the product of the four weights to the common interaction location. One level therefore costs at most a fixed multiplicity times `A⁴ L^(4s) theta^(4s)`. Summing levels proves FC20, with `1/[1−(L theta)⁴]` and the fixed fourth-derivative, colour, contour and geometric factors absorbed into C. The strict condition `theta<1/L` is essential to this absolute-value proof.

Neither the engineering expectation `theta=L⁻²` nor the actual FC19 constants have been proved. The envelope identity `r_j=κ⁻¹ H_(j+1) a_(j+1)` and the fixed plaquette Stokes representation of each contour spread are exact starting points. They narrow the neutral task to linear transfer estimates; they do not supply them. The full charged producer still has exchange terms. [BFT34_55](BFT34_55.md)'s H1/H2/H3, together with the corrected same-link envelope term and a verified smaller rate, would supply broader weighted jets through the [recovery transfer](RECOVERY_UIR_ASTRA.md). Its uniform complex domain, source inverse and locality hypotheses remain separate unproved inputs here.

| Claim | Independent disposition | Essential boundary |
|---|---|---|
| FC1 | Confirmed | Nonzero neutral Wilson finite coefficient in the stated normalization |
| FC2 | Confirmed | Actual normalized neutral fourth-order expansion; SU(N) constraint handled |
| FC3 | Confirmed after prose repair | Mean-zero coarse gauge parameters; root-mean projector retained |
| FC4 | Confirmed | Scalar `ell⁴` Gram factor in counting norms |
| FC5 | Confirmed | `Fbar_1 d` shares the fixed constant left/right kernels of `d* d` |
| FC6 | Confirmed | Completed ghost pseudodeterminant on those domains |
| FC7 | Confirmed | Fixed-kernel positive block operator and graph Gram |
| FC8 | Confirmed | Complete neutral determinant/ghost/harmonic weights |
| FC9 | Confirmed | Exact neutral gauge cancellation plus constant `−4(N−1)log ell` |
| FC10 | Confirmed | Complete residual determinant weights; neutral ghost vertex zero |
| FC11 | Confirmed | First neutral vertices vanish; actual full second vertices retained |
| FC12 | Confirmed | Fixed n; uniform periodic single-pole tadpole estimate |
| FC13 | Confirmed | Complete neutral residual coefficient, not individual finite parts |
| FC14 | Confirmed | Fixed-free-complement Taylor inverse relation `I−P₀` |
| FC15 | Confirmed | All exceptional words vanish at fixed n,P≠0 as T→∞ |
| FC16 | Confirmed | Original infinite-volume/a.e.-Bloch one-loop coefficient; volume first |
| FC17 | Confirmed as reduction | The finite-part increment bound remains OPEN |
| FC18 | Confirmed | Exact neutral stationary quartic, no cubic exchange in this restriction |
| FC19 | OPEN | Actual uniform weighted linear producer is not established |
| FC20 | Conditional implication confirmed | Requires precisely FC19 and `theta<1/L` |

## 6. Independent evidence, preserved limits and literature reuse

Both independent programs were implemented without importing predecessor or author helpers and ran once. Their complete outputs and empty stderr files are preserved.

| Independent evidence | Result | What it tests |
|---|---|---|
| [Program 01](checks/review_residual_full_colour_01.py), [output](checks/review_residual_full_colour_01_out.json), [stderr](checks/review_residual_full_colour_01_err.txt) | 30/30 | Exact actual 3⁴ inverse/projector and pure-gauge defect; 6⁴ neutral curl trace; SU(3), SU(5) normalization; all 1,944 local S4′ contours for a nontrivial SU(3) quartic and constrained center; arbitrary internal SU(3) colours in the cubic source |
| [Program 02](checks/review_residual_full_colour_02.py), [output](checks/review_residual_full_colour_02_out.json), [stderr](checks/review_residual_full_colour_02_err.txt) | 35/35 | Full 6⁴-to-2⁴ periodic d=4 S4′ geometry, 124,416 contours, scalar/ghost/harmonic domains at three actual nonflat background amplitudes, and actual normalized stationary-chain quartic |

Program 01 obtains the charged pure-gauge tadpole `7/3` and bubble `−17/6`, hence the nonzero complement defect `−1/2`. It rejects the wrong bubble weight and a missing seagull. The neutral Wilson results are exactly `−1295/2592` for SU(3) and `−1295/1296` for SU(5). Its local SU(3) normalized quartic is `−53410418/127035441`; every FC2 quartic group is nonzero, so omitting any group is detected.

Program 02 builds `M` and `C` from actual contour phase averages, not from matrices manufactured to satisfy covariance. It verifies `Qd=d_c ev`, the root-mean projector, both constant ghost kernels and the `ell⁴=81` factor. The largest displayed completed-ghost log-determinant discrepancy is `9.1×10⁻13`. Its stationary solve has relative residual `3.3×10⁻15`. FC18 gives `−0.013592293460292048`; direct evaluation of the exact SU(2) normalized action with Richardson extrapolation differs by `1.9×10⁻8`, and adding an arbitrary cubic displacement differs by `4.4×10⁻8`, within the predeclared tolerance. The polar-variance contribution is nonzero. Exact simultaneous harmonic shifts preserve the action at nonzero residual.

These controls are finite falsifiers/support, not an all-depth or continuum theorem. Program 02 uses T=2, whereas the recovery periodization theorem is stated for T≥3; the former tests the finite operators and normalization, not that theorem's thermodynamic assertion. Its floating-point solve is not an interval certificate. The exact local SU(3) polynomial contour control is not itself periodic. The analytic arguments above establish the general statements.

There is also a preserved reviewer defect: an **unexecuted comment** in Program 01 assigns `1/(4λ(P)²)` to a four-insertion projector word. The correct nonresonant value is `1/(8λ(P)²)`, and that four-leg word is outside FC15's two-leg calculation. No predicate or output used it. The executed source was not silently rewritten. The [control notes](checks/review_residual_full_colour_control_notes.md) derive the correction and also disclose that Program 02 did not execute a separate missing-root-mean ghost-determinant mutation; its Q_per mutation was executed and the ghost-domain failure is proved above.

Both author implementations, criteria, saved outputs and stderr files were read completely. Their advertised 34/34 and 25/25 counts match their saved evidence. They were **not rerun by this reviewer**, since the coordinator handles that reproduction. Their finite graph and exceptional-word examples do not themselves prove consumer equality; the source arguments and independent reconstruction supply that part.

The requested [primary-literature ledger](checks/review_residual_full_colour_literature.md) records a block-by-block applicability check, direct arXiv/publisher URLs, exact theorem/equation hypotheses and explicit non-import boundaries. The source manifest records document hashes, versions and selected page coverage. No complete third-party paper is proposed for commit: the six downloaded PDFs are **local-only inputs with no verified republication license**. Failed retrievals and access HTML are preserved as metadata, not treated as theorem reads.

The useful uniform-estimate candidates are the constrained gauge/Green estimates in [Dimock's covariant axial-gauge work](https://arxiv.org/abs/1410.2798v3) and [multiscale QED work](https://arxiv.org/abs/1712.10029v3). Applying them still requires a d=4, integrated-link, finite-κ soft-chain comparison. The identity `Q_S4′=Q_str−d_c alpha`, already in [FLOW §89](FLOW.md), helps align curvature variables; equal printed powers of L in different dimensions do not establish equal normalization. The other inspected papers supply perturbative Ward/matching context or possible covariance infrastructure, not an unproved replacement for FC19. The Bałaban originals remained bibliographic leads where full text was unavailable. No search absence is used as a priority claim, proof obstruction or route-exhaustion claim.

The accepted data are the supplied SU(N), Wilson action, normalized φ, S4′ contours and winding, κ>0, counting norms and prescribed perturbative coupling convention. The current primitive registry and actual registered source grants were read; none supplies the determinant, uniform-producer, source/history/action, OS or physical spectral-gap conclusions. No new axiom, primitive, empirical number or unexplained physical identification is adopted.

The remaining proof obligations are explicit: actual FC19 or another uniform producer; the full charged cubic/quartic estimates; nonlinear small/large-field flow and the relevant polymer comparisons; source/history/action matching; continuum OS existence/reconstruction; nontriviality and the physical Hamiltonian gap. Fixed-depth auxiliary inverse gaps are not physical mass gaps. No global no-go or exhausted-route verdict follows from any of the rejected shortcuts in this review.

## 7. Final evidence binding

One review pass and one coordinator-owned prose repair were followed by affected confirmation in the original reviewer context. There were two independent executions, no author rerun, no pipeline run, no reviewer commit, and no audit operation. All frozen author input hashes still match; only the exactly identified target sentence differs from the original manifest.

The [final receipt](checks/review_residual_full_colour_receipt.json) binds this report, the source/read manifest, findings, all independent criteria/scripts/stdout/stderr, the literature analysis and retrieval metadata. It separately marks the PDF inputs as local-only. It is a bounded-review evidence receipt, not the coordinator's whole-PR/canonical landing receipt.

Final source disposition: **FC1–FC18 confirmed within the domains and limit order stated above; FC19 OPEN; FC20 confirmed as an implication from FC19.** The full existence and physical continuum mass-gap target remains OPEN. Changed mathematical sources or consumed premises require affected re-review; unchanged source hashes permit reuse of this bounded confirmation.
