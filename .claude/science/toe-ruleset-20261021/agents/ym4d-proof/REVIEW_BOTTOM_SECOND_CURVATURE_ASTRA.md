# Independent source review: bottom second curvature

**Scoped disposition: BC3/CJ18 is confirmed as a conditional source-specific theorem; BC26 is confirmed under the same named normalized-tree, linear, and current contracts. No material source defect was found.** This review concerns the frozen argument below, its consumed proof interfaces, and its evidence. It is not a verdict on the whole PR or an effective-retained audit decision. Four-dimensional Yang–Mills continuum existence and a positive physical continuum Hamiltonian mass gap remain **OPEN**.

The reviewed source is [BOTTOM_SECOND_CURVATURE_ASTRA.md](BOTTOM_SECOND_CURVATURE_ASTRA.md), SHA-256 `b735eb1d551c9ba80925c0d22830b17ce823735bf7d9ac5d2e19ddabb2ff3ade`. Its [author receipt](checks/bottom_second_curvature_receipt.json), SHA-256 `88d659a2a512fcc57b95dc077836ceb555dbeea177be36cde0abf4f6d0f977b4`, binds twelve artifacts. The source was unchanged throughout this review. The coordinator reports preservation and publication at commit `a63ade893a7f76b9ee1925170545bf7489ad0f18`; this reviewer made no Git, PR, shared-status, or audit mutation.

Claim boundary: `actual_current_surface_status: bounded-support`; `target_claim_type: bounded_theorem`; `trace_class: upstream_support`; `reachability_to_target: partially_closes`; `bare_retained_allowed: false`; `audit_required_before_effective_retained: true`. These describe the source theorem's reach, not an audit assignment.

## 1. Independence, exact contracts, and read coverage

This was a fresh-context reviewer task, requested as `gpt-6-astra/max/fork-none`. This is Codex reviewing Codex work. The runtime backend identity is not independently observable, so the requested label supplies no cross-model or cross-family certification. Before declaring criteria, the reviewer had the coordinator's targeted brief, the full new source and its numerical summaries, the full charged-jet source and review, and the author freeze metadata. The review is source-exposed, not blind. No author or predecessor checker implementation was inspected until all reviewer numerical runs had completed.

The [prospective criteria](checks/review_bottom_curvature_criteria.md), SHA-256 `9ba18d42b79c3a208a8c04b74f3aaca229b9db876e408440e541b724da5f7e79`, preceded reviewer implementation. A separately preserved [supplement declaration](checks/review_bottom_curvature_supplement_criteria.md) followed the first two reviewer runs and preceded its new implementation; it explicitly addressed the first source run's use of a current recovered from the second-order solve. No criterion was relaxed, failed control erased, or source repair made. Finite numerical sample caps in the implementation are diagnostic guards, not candidate universal constants.

The model is CJ1's **u-stripped normalized tree phase** in d=4, SU(N), fixed odd L>=3, ell=L^n, top side T>=3, and kappas in a fixed compact positive interval. Links are integrated in each level's own units and all adjoints use counting inner products. The paired S4-prime contour uses the same permutation at its two endpoints and the divisor `24 L^4`. A common localized first representative is used for every external leg. The hidden domain fixes the top field, quotients only gradients whose gauge parameter vanishes on the top sites, and retains harmonic link modes.

The complete [charged-jet source](CHARGED_STATIONARY_JET_ASTRA.md), SHA-256 `85b91738993f09f7e40a49f4c957c164a684bf499185629a82775229f6437254`, and [its independent review](REVIEW_CHARGED_STATIONARY_JET_ASTRA.md), SHA-256 `f7e02d766c8885dceeeac8d2264784cdc65b85a771ae556efa5935d45236836d`, were read. Their proof content, rather than the word “confirmed,” was checked against the exact uses here. In particular:

- CJ11 supplies one periodic localized potential lift with coefficient bounds and no mean-subtraction tail. Its primitive and root interpolation use the repaired periodic TU-3, the analytic closed-one-form argument, and NQ-1 for an arbitrary consecutive string of actual Q maps.
- CJ12 gives the actual full-colour cubic in that representative. CJ13–CJ17 distinguish the log current from the right current and retain covariant divergence, the adjoint endpoint funnels, and forced transport. No ordinary co-closed-current replacement enters BC2.
- CJ19 supplies the complete bottom Euler/Bianchi/harmonic source. The sufficient CJ18-to-quartic implication is checked again in Section 5 below.
- The complete corrected [uniform-minimizer source](UNIFORM_SOFT_MINIMIZER_ASTRA.md) was read. US1–US17 concern the normalized tree phase. Its linear Hessian is not substituted for the finite-u spread Hessian.

The actual selected supporting proofs were read in LINEAR_PACKAGE, the session-16 PROOF snapshot, TUNIF, CODEX_REVIEW_TUNIF2, REVIEW55_TUNIF, NQ_DEF, and the unprimed-strip/periodicity repairs in the S13–S15 reviews. NORMS's composite cubic proof, FLOW55's exchange identity and weighted norm/consumer distinction, and UIR55's class J definition were also inspected. These selected reads are not full-document or whole-theory endorsements. The [read manifest](checks/review_bottom_curvature_read_manifest.json) gives exact line coverage and byte hashes, including full-source reads separately from metadata verification.

The installed physics-loop and review-loop skills were reconciled to the fetched current-main revision at review start, `ca2bc7ddf64790da96cd43d42017d000fbfe4808`; stale local main was not used. The owner's later [PROCESS_LIGHT.md](PROCESS_LIGHT.md) decision was read in full before freezing this report. Its explicit allowance for already-running lanes applies here. This research review is not the final consolidated proof deliverable. Root retains combined validation, lock ownership, source integration, publication, and any audit action.

## 2. Source algebra and the high-alias estimate

For the actual stationary coefficient, with `q_j=kappa_j(w2_(j+1)-Q_j w2_j-B_j(a_j))`, the reviewed identity is

    Psi = d_2 w2_0 + B_p(a),
    d_2* Psi = Q_root,0* q_0 - DB_p[a]* f + kappa_0 DB_0[a]* r_0 = S,
    d_3 Psi = d_3 B_p(a) = R,
    harmonic(Psi) = harmonic(B_p(a)).

The three terms of S are indispensable. The upstream coefficient bounds give q_0 of order L^3 ell^-3, the Wilson derivative term of order ell^-3, and the soft derivative term of order ell^-4. Fixed-L contour support absorbs the remaining L-dependent constants. Negative-momentum transpose is the analytic adjoint; complex conjugation at the same momentum would change the source.

BC4–BC6 correctly improve R. On a contractible unit cube, subtract the gradient of the tree-path integral lambda. The remainder c is a fixed local combination of face circulations, hence bounded by f=da. For the exact pure-gauge link `exp(-epsilon lambda_x) exp(epsilon lambda_y)`, the second link logarithm is `-[lambda_x,lambda_y]/2`. Vanishing of every plaquette product therefore gives `B_p(d lambda)=d_2 C(lambda)` and `d_3 B_p(d lambda)=0`. Quadratic polarization leaves terms with one or two c factors, yielding `|R|<=C(|a||f|+|f|^2)`. This argument is a local polynomial identity and works for separate complex external legs. It does not require a componentwise derivative bound on a. Consequently S and R are bounded by C ell^-3 on the joint source tube.

The scalar high-alias estimate BC9 uses the correct counting norm and domain. For complex top momentum k, the projections are biorthogonal and have kernel `ell^-4 exp(i(k+2pi K).(u-v)/ell)`. The selected high part is branchwise. It has a spectral gap of order ell^-2 on the stated slightly enlarged real cube and sufficiently thin fixed imaginary strip.

The small-time argument is adequate without a false global Gaussian pointwise estimate. The half-line equation for `h_t(j)-h_t(j+1)` has nonnegative off-diagonal entries, proving monotonicity. Weighted telescoping and the exact jump-count moment give a derivative l1 bound of order `[(1+t)^-1/2+alpha] exp(C alpha^2 t)`. Set alpha=eta/ell and use the exact twisted image formula. Up to time ell^2, subtraction of the low heat mode costs C/ell; the integral is O(ell). At later times, summing a row first cancels the ell^4 output count against ell^-4 Fourier normalization. The remaining four-dimensional sum of `(1+|K|) exp(-c t |K|^2/ell^2)` is exponentially summable for t/ell^2>=1; its time integral is again O(ell). Both d and d* obey the bound, with only fixed orientation factors. Normal convergence proves holomorphy. This proves a projected derivative Green bound, not a generic inverse estimate at k=0.

## 3. The uniform quotient from a nonuniform stationary germ

This is the decisive bridge. The normalized low coefficient has no extra cell count. On the actual source,

    phi(k/ell) Psi_0 = N_0 = d(k/ell) S_0 + d*(k/ell) R_0,
    P_ell = ell^2 phi(k/ell),     N_ell = ell^4 N_0,
    ell^2 Psi_0 = N_ell / P_ell.

BC7 and the extra derivative give N_0=O(ell^-4), so N_ell has a depth-uniform bound on a fixed joint tube. The uniform claim is made for the quotient of this numerator. A numerator that merely vanishes at the real origin need not be divisible.

For fixed n and every real external theta, the finite hidden quadratic form is positive on the rooted gauge complement. A zero-energy hidden field has zero bottom curvature and zero soft residuals; the top-zero condition leaves only the rooted hidden gradients that have already been quotiented. Harmonic links have soft energy and are retained. Near a real fibre, an analytic complement can be chosen using the finite rooted gradient Gram matrix. Changing the first tangent to the localized CJ11 representative is an analytic rooted gauge change on a possibly smaller neighborhood. At second order the explicit solve is for the full hidden CJ7 source at total momentum k, with separate input momenta theta and k-theta; no nonlinear closure of a single Bloch mode is assumed. These facts give the required local holomorphic stationary germ at k=0 for each real theta. No uniform Hessian lower bound or germ radius is used.

The sine coordinate `w_mu=2 ell sin(k_mu/(2 ell))` and its local arcsine inverse have uniform bounds for ell>=3 on a fixed small polydisc. Shrinking the theta strip and choosing the fixed circle radius rho below the original source width keeps both inputs in that original tube, for every point of the integration circle. Thus `F(w,theta)=N_ell(k(w),theta)` is jointly holomorphic and uniformly bounded there.

Write `A(w')=w_2^2+w_3^2+w_4^2`. The BC17 integral divides by `(z^2+A)(z-w_1)` on `|z|=rho`. For `|w_mu|<rho/16`, the denominator has uniform lower bounds and the integral is jointly holomorphic, bounded by `4 sup|F|/rho^2`. For each fixed real theta and sufficiently small w', **both** roots of `z^2+A` lie inside the fixed-n germ. That germ removes both possible poles, including the coalesced double root at the origin. Cauchy's formula identifies the integral with F/P throughout the w_1 disc for these small w'. The holomorphic identity theorem extends `F=P Q` over the connected w' polydisc. Repeated one-variable identity theorems in all components of theta then extend the equality from the real theta set to its connected complex strip. The possibly n-dependent seed radius has disappeared from the estimate. This is a valid fixed-circle division argument; no branch irreducibility assertion is needed.

BC19 controls the remainder of the total-momentum tube. All zeros lie in the small division patch after the imaginary width is reduced by a fixed amount; away from that patch the normalized symbol has a positive lower bound. Direct division and the Cauchy quotient agree on their overlap. Therefore the low curvature is O(ell^-2) uniformly on a fixed smaller joint tube.

At total k=0, the quotient agrees with the actual stationary germ, so its value is exactly the harmonic part of B_p(a), for every opposite-input pair theta,-theta as well as constant inputs. The mean of `d_2 w2_0` is zero. Deleting harmonic modes would contradict this matching, and adding a separate mean correction is unnecessary.

## 4. Reciprocal gluing and the two different density bounds

The finite central/face cover for each of the eight external momentum coordinates, followed by the finite total-momentum folds, is independent of depth. On a change of fold the complete alias set is permuted modulo ell. Individual high and low pieces change, while their sum retains the same physical fine-cell boundary character. On each real overlap away from zero total momentum, both reconstructed sums equal the actual stationary curvature. Holomorphic uniqueness in both independent input variables identifies them on the corresponding connected complex overlap; the removable extension preserves equality at the complex zero set. Face identifications of each input use the actual paired-contour coefficients' periodicity. This addresses both external variables, not just the total momentum.

Subtracting the actual B_p(a) gives a closed, periodic holomorphic family g bounded by C ell^-2. Two independent contour shifts yield a product exponential envelope in the two input-to-output distances. Finite-T sampling is exact periodization of the common Bloch coefficients, identified with the real-fibre stationary solution and its retained harmonic value. Thus this conclusion is not extrapolated from one numerical cell.

The row and anchored-column estimates are distinct. Summing both top inputs at fixed fine output leaves C ell^-2. Summing the fine output and the other input at fixed top input includes ell^4 fine sites per top cell and gives C ell^2. The diameter weight is controlled by a fixed loss of the exponential rate. No row/column norm identity or supremum over factorized signs replaces an absolute tensor sum.

## 5. Conditional full-colour quartic consequence

The repaired periodic TU-3 applies to g with total momentum as the twisted variable and theta retained as a holomorphic parameter. Closure and the zero harmonic value were proved above. Its bottom primitive has amplitude C ell^-1. Forward propagation with the actual Q maps uses the any-consecutive-level NQ-1 estimate. The residual contribution is `L^m L^-2(s+m)=L^-2s L^-m`, a geometric sum. The top defect is an analytic closed one-form; the two-axis argument gives zero value at total momentum zero. The local root interpolation corrects it to top zero without a harmonic tail. This supplies one admissible second representative with the claimed product envelopes at every level.

The quartic identity is the completed stationary value

    T4 = R4 + (1/2)||D_h w2+Z||^2 + <Da,DZ[a]w2>.

The bottom square has four inverse powers of ell and one ell^4 output count. Soft squares have q_j^2/kappa_j and yield a summable L^-2s after counting. Soft R4 terms contain a first residual and have at least that summable power; bottom R4 occurs once. The bottom U term has powers ell^-2, ell^-1, ell^-1 and count ell^4. Soft U terms have powers L^-3s, L^-s, L^-s and count L^4s, leaving L^-s. Polarization before taking absolute sums supplies all colour/order coefficients and their weighted tensor norm. These estimates apply to the completed expression, including cubic exchange, rather than to separately O(n)-bounded pieces.

BC26 therefore follows under the named contracts. With the existing quadratic and cubic inputs it supplies the bounded-jet interface used by UIR55's class J. It does not prove jet convergence, the finite-part increment, a uniform nonlinear neighborhood, finite-u density estimates, or determinant root/harmonic Gram cancellation. The separate determinant factors remain separate. The constant noncommuting field is a retained harmonic-curvature control; the centered paired mean BCH2 cancels and is not evidence of marginal growth.

## 6. Independent diagnostics and reproduction

The first reviewer program was written without author or predecessor helper imports. It uses centered cell coordinates, a directly assembled rooted gauge completion, LU solves, labelled signed path words, and analytic negative-momentum transpose. Its L=3 cell has 81 sites, 324 links, 486 plaquettes, 7,776 paired contours, and 80 rooted scalar gauge directions; kappa=.83 and the external data differ from the author's fixtures. This is a new implementation of the same finite Bloch system, not a different theorem or physical-volume limit. SU(2) tests use the st coefficient, twice the polarized coefficient.

| Reviewer run | Result | Main discriminating evidence |
|---|---:|---|
| [Scalar output](checks/review_bottom_curvature_scalar_01_out.json) | 26/26 | Odd ell=3,5,9,15; complex bulk/face twists; incidence/FFT normalization; high-branch nonperiodicity; conjugation and origin-only controls |
| [Actual source output](checks/review_bottom_curvature_source_01_out.json) | 61/61 | Both null sheets; exact Euler/Bianchi/Hodge/gauge equations; opposite and constant harmonic values; both input faces; Cauchy reconstruction; missing-term mutations |
| [Declared supplement output](checks/review_bottom_curvature_supplement_01_out.json) | 38/38 | Top current from the cubic on three linear lifts before any w2 solve; genuinely complex theta on both null sheets; independent-current Cauchy test; exact integer cube algebra |

The scalar counting-row norm divided by ell ranges from .230346 to .338898 in those samples. At the first source run's two null points, the low numerator is at most `1.07e-17` while low curvature is about .041–.043. Removing Wilson DB, soft DB, or Bianchi terms gives discrepancies from `5.41e-6` through `8.34e-5`; substituting a conjugate adjoint also fails. At zero total momentum, the nonzero-opposite and constant cases retain harmonic B_p of .04136924 and .06000000, respectively, while the mean of g is at most `7.67e-19`. The three 40-node Cauchy tests agree to `3.90e-15` or better.

The first run reconstructed q from w2, which could make part of a source check self-confirming. The declared supplement removes that limitation for its decisive null test: it evaluates the cubic cyclically on a(theta), b(k-theta), and each of four independent top test lifts at -k, then constructs the Euler numerator before solving w2. The resulting top current agrees with the w2-derived one to `2.80e-15`; on both complex-null sheets with complex theta its low numerator is at most `2.39e-18`. Its 32-node Cauchy value agrees with direct low curvature to `5.42e-15`. It reuses only the reviewer's own cell/path helpers, so it is an independent current derivation, not a second independent geometry implementation. Eight exact integer cube cases have zero BCH-gradient, pure-gradient Bianchi, and polarization errors; a nonzero mixed a*f contribution detects omission of that term.

All 125 reviewer predicates passed on their first execution. No threshold or implementation was changed after a failed run, and there were no failed numerical controls. These counts are correlated diagnostics, not 125 proofs. Tests use ordinary floating point except the finite integer cube identities; they are not interval certification, arbitrary-depth numerical coverage, or a proof for all SU(N). The analytic argument supplies the all-depth, all-volume, and finite-colour-constant statements.

Only after those runs were complete were both author programs read and rerun. Their [76-predicate scalar reproduction](checks/review_bottom_curvature_author01_reproduced_out.json) and [61-predicate source reproduction](checks/review_bottom_curvature_author02_reproduced_out.json) match every original JSON field exactly except the declared `elapsed_seconds`. Both exits are zero and both stderr files empty. This establishes reproducibility, not independent evidence. All reviewer stdout/stderr, sources, criteria, commands, exits, and the supplemental chronology are retained in the [attempt ledger](checks/review_bottom_curvature_attempts.json) and bound by the [review receipt](checks/review_bottom_curvature_receipt.json).

## 7. Literature boundary and remaining obligations

The primary-source comparison was checked at the sections actually used. [Abadias–De Leon-Contreras, Lemma 2.6 and proof](https://link.springer.com/article/10.1007/s00028-022-00851-1) provides unweighted l1 difference estimates on the integer lattice. The neighboring remark warns against global Gaussian pointwise control. It does not provide the complex-character finite-cell estimate; BC10–BC14 prove that extension here.

[Dowker, arXiv1207.2096v2, equations (13)–(15)](https://arxiv.org/pdf/1207.2096v2) treats a real phase twist and matches images to normalized Fourier modes. The complex twist follows in this source from absolute normal convergence via jump-count exponential moments, with four-dimensional tensor products. No complex-source theorem is imported from Dowker.

[Michta–Slade, definitions (1.1)–(1.3), Lemma 2.1 and proof (2.3)–(2.5)](https://alea.impa.br/articles/v19/19-38.pdf) concerns the scalar infinite-lattice resolvent, with d>2q required in the massless case. Its Laplacian symbol is `1-d^-1 sum cos k_mu`; the present phi is 2d times that symbol. The heat-time rescaling is consistent. No asymptotic theorem, Appendix B estimate, complex finite-cell bound, or stationary-source divisibility result from that paper is consumed.

Balaban and Dimock are credited for the constructive lattice-gauge and renormalization-group methods motivating this research program. No fresh theorem from Dimock, Balaban, BGM, or Dybalski–Stottmeister–Tanimoto is imported in this review. The author's explicitly limited historical screening is not enlarged into a whole-paper certification.

No source repair is requested for this frozen unit. A later consumer must still keep the normalized-tree/finite-u distinction, the complete determinant domains, and the difference between bounded jets and convergence. The next unresolved scientific obligations include the finite-part increment and its convergence, nonlinear control on a depth-uniform complex neighborhood, the continuum construction, and a positive physical continuum spectral gap. None is settled or ruled out by this review.
