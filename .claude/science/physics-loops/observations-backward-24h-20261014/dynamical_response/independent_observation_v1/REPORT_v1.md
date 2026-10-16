# M14 primary-source and observational-input check

The current M14 wording keeps the observational obligation explicit. No measurement-admission correction is required in the three source versions reviewed here. The exact mode and covariance identities remain conditional tools: the inspected ACT/BOSS products do not already supply their required same-time, same-mode velocity, slip and time-derivative inputs. This is a bounded conclusion about the inspected papers and recorded products, not an absence claim about all existing or future observations. It does not certify the author’s perturbation equations, numerical evolution, novelty or a formal audit outcome.

I froze independent source conclusions in `INDEPENDENT_ADMISSION_FREEZE_v1.json` before reading the author’s `WORKING_v1.md`, `EXTENSION_v1.md` and subsequently created `STATISTICAL_INPUT_v1.md`. The three earlier primary PDFs still match their frozen identities. No raw maps, catalogues, chains, covariance arrays, new observations, fits or author ODE runs were acquired or executed.

## What the published statistics supply

[ACT DR6+BOSS, 2405.12795v2](https://arxiv.org/pdf/2405.12795v2), Eqs. 1–7 and 14–19, defines projected angular spectra with redshift kernels, cross-sample reweighting, a fitted beta and a magnification correction. Its reported E_G is a ratio of estimated spectra with a ratio likelihood, not an observed ratio of individual complex Fourier coefficients. The two broad samples and their finite angular bins do not constitute a continuous mode history. Earlier recorded covariance, calibration, bandpower-window and public-product limits still apply; I made no new numerical-release search.

[The precision estimator, 2401.12971v2](https://arxiv.org/pdf/2401.12971v2), Eq. 8, first relates a lensing–galaxy cross spectrum to a velocity–galaxy cross spectrum. Replacing the latter by beta times galaxy auto power uses its linear bias and velocity-transfer assumptions. Eqs. 14–20 then project into angular spectra. Its RSD summaries are conditional inference products; they are not direct measurements of every realization’s W, a continuous C_WW, or a separate cross-spectrum time derivative. A ratio weighted by the galaxy field is not automatically the same as a ratio weighted by W when deterministic transfer, absence of velocity bias and stochasticity assumptions are relaxed.

The [1210.0439v2 ideal-observable discussion](https://arxiv.org/pdf/1210.0439v2) remains useful for conventions and ideal input obligations, rather than supplying new measured histories. Preserve the frozen normalization dictionary: its P2 equals twice standard ACT E_G. The standard Sigma convention has GR value one; the older paper’s corresponding lensing amplitude has GR value two. Names alone do not define the normalization.

For the author’s explicit metric slots, the ACT spatial potential is minus the author’s Phi, so its lensing combination maps to S=Psi+Phi. With physical Jordan quantities, c=1 and the stated positive growing-velocity convention, the ideal definition maps to P=−a^3 K^2 S/(3H0^2 W). This dictionary does not elevate the observed spectrum ratio into that ideal coefficient ratio. In particular, the author’s exact continuity equation gives W=delta_J′−3Phi′. Identifying W with f delta_J requires an additional regime, gauge/transfer argument or explicit correction. It is not automatic when moving from the sources’ RSD approximation to full nonquasistatic dynamics. The two published papers also print different theta signs; retain the operational convention and positive GR normalization rather than copying an isolated symbol.

## Statistical derivative and weighting requirements

For a common physical background, fixed comoving Fourier label, fixed differentiable ensemble and C_AB=Re E[A B*], multiplying an exact linear field identity by W* and averaging is legitimate. It does not require Gaussianity or a single initial scalar mode. Every term must use the same weighting and covariance convention. Thus the author’s normalized P, r and M may be formed from C_SW, C_TW, C_WW and C_S′W on their stated nonzero-denominator domain. Products of unrelated published ratio estimates have no such automatic guarantee.

The product rule is

    d_N C_SW = C_(S′)W + C_S(W′).

The required C_(S′)W is the first time-leg derivative of Re E[S(N1,k) W*(N2,k)], evaluated at N1=N2. A derivative of the diagonal only gives the sum. The other leg is not determined in general by C_WW′ or by a scalar RSD growth summary. A real deterministic transfer W′=gW W would supply C_S(W′)=gW C_SW, but that is an added premise. The weaker equality of those covariances is sufficient; deterministic transfer is one example, not a necessary condition.

A simple information check makes the distinction explicit. Let X,Y be independent unit-variance real variables, W=cos(theta)X+sin(theta)Y, V=−sin(theta)X+cos(theta)Y and S=cW+V, with constant nonzero c. Then C_WW=1, C_SW=c and C_SS=c^2+1 at every time, while C_(S′)W=−theta′ and C_S(W′)=theta′. All equal-time covariances stay fixed while the two time-leg derivatives vary. This is an algebraic illustration of the missing statistical information, not a proposed cosmological solution or an extra numerical experiment.

At fixed comoving k, K=k/a and D=a^3K^2/(3H0^2) obey D′=D for N=ln a_J. Substitution gives the author’s exact expression

    M = P′ + P(2gW−eta),
    gW = (ln C_WW)′/2,  eta = C_S(W′)/C_SW.

Accordingly, `STATISTICAL_INPUT_v1.md` correctly treats eta=gW as additional information. Its cross-correlated Euler equation also legitimately obtains the covariance-weighted slip from gW, P and the calibrated background; this does not make gW an already observed ACT/BOSS time series.

The source-admission obligations are therefore specific:

| Input | Additional obligation beyond the inspected published E_G summaries |
|---|---|
| C_SW and C_WW | A physical velocity inference, common tracer weighting and consistent noise/bias treatment; a justified conversion from the measured projected spectra. |
| C_TW or its Euler replacement | A slip-sensitive cross statistic, or calibrated H,h and a continuous velocity-power derivative with the Euler premises verified. |
| C_(S′)W | Separate time-leg information, a directly modelled derivative-sensitive cross observable, or an explicit justified closure for C_S(W′). |
| Three independent rows | Common epoch/background and measured covariance-weighted rank, with uncertainty; differing wave numbers alone do not prove rank. |
| Error envelopes | Joint covariance, calibration, windows and differentiation/closure errors. Published marginal E_G intervals are not these envelopes. |

A projected measurement also averages over time. Unknown R(N), x(N), y(N) and the geometrical factors must remain inside the redshift-window prediction unless their extraction is justified. Putting only K-dependent D inside a broad-scale operator does not remove this time-window obligation. Neither an effective redshift nor a bin midpoint makes the exact pointwise inverse an exact survey estimator.

## Frame and comparator scope

[Rondeau and Li, 1709.07087v1](https://arxiv.org/pdf/1709.07087v1), §§IV–V, uses g_J=A_paper g_E; therefore A_paper=A_author^2. Its invariant Weyl combination, conformal time and correctly defined redshift support consistent observable predictions. Individual density perturbations/power spectra need not be frame invariant. Its v_k=q_k/rho transformation does not by itself establish invariance of the author’s H-normalized W. The observed clock satisfies 1+z=a_J0/a_J, rather than a_E0/a_E. Its ISW expression, Eq. 154, identifies a possible projected sensitivity to potential time variation, but supplies no measured unprojected C_(S′)W likelihood. The paper’s scope is classical and conformal; quantum/disformal conclusions are not imported.

Direct substitution of the author’s metric definitions gives Psi_J=phi_E+bX, Phi_J=phi_E−bX and invariant S=2phi_E. Primes in the conformal paper denote conformal-time derivatives, whereas the author uses N_J, so d/dN_J=(a_J H_J)^−1 d/deta. The stated a_J, H_J, density and velocity definitions keep that conversion explicit. This check does not establish a sign error in the earlier vacuum note, whose potential labels require their own metric-slot dictionary.

[Assisted coupled quintessence, 1407.2156v1](https://arxiv.org/pdf/1407.2156v1), §II and §VI, is a comparator with canonical fields and constant coupling coefficients. Eqs. 77–81 retain linear scalar time derivatives and metric/dust terms; Eq. 82 then explicitly adopts a small-scale limit. Its Einstein-frame equal-potential relation cannot be copied into an observed Jordan slip. It does not supply the curved-metric/variable-coupling derivation or observational histories. I have not certified every printed coefficient or adopted its small-scale approximation.

## Reviewed author versions and limits

The complete author notes read were WORKING `637fdbfbead8d4566bf0e99e046a26cae28123b73f88f60d4e768ee5584cdff1`, EXTENSION `1e1dadc5a38f5b6ac0a2e2fd778d360d1246f49c668cd054c88ca53705a3dc57`, and STATISTICAL_INPUT `79604dea5cd68201d2216a7f085f64c496daec0821bace3da6fe2d1c85312c86`. All preserve supplied-model, rank, free-preparation and observational-calibration conditions. The statistical source addresses the exact cross-spectrum issue without claiming that current E_G releases deliver its inputs. The error envelope expressly requires justified measurement errors; it does not derive them.

Exact versions, PDF/text/render hashes, full page lists, inherited read scope and source snapshots are bound in `READ_SCOPE_v1.json` and `IDENTITY_RECEIPT_v1.json`. Only the relevant sections were read; unexamined appendices and all survey numerical arrays remain uncertified. Full downloaded papers/text/renders remain local source material and must be excluded from any publication packet. One tool-call quoting error occurred before execution and was recovered; no scientific test was run or failed. All writes stayed within this independent-review folder, with no Git, external-message or formal-audit action.
