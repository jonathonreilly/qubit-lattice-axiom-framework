# M14 canonical mathematical source correspondence, version 1

This report binds the canonical source snapshot taken at 2026-10-15T14:59:51Z. It is a focused mathematical source comparison, not a formal audit, publication approval, new blind derivation, aggregate execution or independent ODE validation. Root remains scientific author. The earlier independent equations and working-source reports remain unchanged.

## Complete read scope and identity

I completely read the 24,914-byte canonical note, SHA256 `326ad86376122e55c9ff2804d91b7ec95e7e5fa7b43e349a0b834257f0fd810f`, and all six canonical Python sources:

| Source | SHA256 |
| --- | --- |
| scalar_dynamical_momentum_inverse_check.py | cea1f8f345aa64adf0c2a903b25133418e0389c06b48691e50b553a5d7e341b4 |
| scalar_dynamical_forward.py | b7ece5a9ea1e48334c1ee9301b4ca3b5e59f7246f6837ec5b9e0c2b47e64f005 |
| scalar_dynamical_geometry.py | e88694b30d4e9557ebf9272423556f4c6f01c63f3b569556a99395c1a3b4b834 |
| scalar_dynamical_extensions.py | 935f99266dc7b93ea90589c60a5c35e71accec69bac4592dd11a333d19798f14 |
| scalar_dynamical_domains.py | 17136ce5e6296b569e1786836004c1564f6f80d229e828d29c12c02b090facbf |
| scalar_dynamical_covariance.py | 060d282e64eb8ead9ebd55614cdda8bc4dd2db33bb51ee2ef56fcca9083cf9f6 |

I also completely read the frozen forward protocol, N1–N8 scope checklist, summary output and launch_check's complete covariance derivation, identity receipt and pre-exposure freeze. The latter derivation is SHA256 `f2150ce1e33898c3790b73ce4ccdf8a07ce79029745750289c2065d38b19157b`; its identity is `b35b5096bcc47c25b6c7741d8605b8c5237b2c3d4f5213beefccae457058a6a0`. I did not rerun its 39 pre-exposure or 16 correspondence controls. These are another checker's evidence, not my blind derivation or count.

All original canonical source bytes match the supplied author freeze. Frozen RESULTS_v1 and SUMMARY_v1 source hash fields bind these exact sources and report 81 passing author controls, zero failures and zero empirical tests. I checked these bindings and counts, not the entire numerical product independently. RESULTS_v1 was parsed for those fields; all per-epoch numerical rows remain the forward checker's responsibility. The summary was read completely. The mathematical/source read of the forward helper is not a new numerical evolution.

The exact paths, byte counts and product identities are in CANONICAL_EXPOSURE_FREEZE_v1.json and CANONICAL_PRODUCT_BINDING_v1.json. Root has announced later targeted changes; this version deliberately binds the preserved earlier snapshot. A later supplement must cover changed bytes.

## 1. Equations, maps and three-row inverse

Sections 1–3 retain the correct supplied-action and metric conventions. The density contrast is now explicitly the Einstein proper rest-frame number contrast. Real calibrated mode components and common real physical coefficients are also explicit. These close the two domain clarifications in my working report.

Equations (2)–(7) agree with the independent pre-exposure derivation. They retain both scalar initial perturbations, the rho b^2 term associated with number contrast, and the matter lapse source. The direct geometry helper constructs the first-order Christoffel, Ricci and mixed Einstein tensors from the stated metric rather than importing the forward solver's expressions. Its mixed 00, 0i and spatial-pressure targets have the correct signs; its box expansion matches the independently expanded density-divergence calculation. In particular delta G^0_i=-2 partial_i(phi_dot+Hphi) combines with scalar and dust momenta to give the sign in the canonical first-order system.

The symbolic constraint calculation in the forward helper and spatial-trace calculation in the extension helper use the same complete flow as the independently proved C_dot=-3HC and trace identities. They do not impose a quasistatic particular solution. The undivided constraint avoids a spurious singular divisor 2Qp^2-s^2.

The physical-frame map, fixed-comoving-mode derivative, Jordan Euler/continuity and normalized momentum row (12) match the independently checked working derivation. The proof and source correctly retain q=2Qb^2, the factor of two in T=2bX, and x/y=q. The determinant transformation (13), state-completion proof and distinctions between available and observed rank are valid.

The three-row helper refuses nonfinite/nonrational inputs, zero supplied P, rank loss, nonpositive R, zero y and nonpositive q. This is the generic canonical-scalar domain; the optional revised-family inequality q<beta is a separate condition. At b=0, the q>0 derivation cannot divide by b. At a scalar turning point s=0 with b!=0, x=y=0 and q is instantaneously unidentified. The canonical note states both cases and does not interpret sampled saved-epoch success as uniform interval identification.

## 2. Covariance time legs and five-row lift

I had already independently derived the statistical time-leg distinction before this canonical review. The new five-row lift, however, was first seen after root and launch_check developed it. My check of that lift is therefore an explicitly post-exposure proof/source comparison. I read launch_check's independent derivation completely and checked its interaction with my independently derived equations.

From the exact momentum and Jordan Euler equations, V=H_J v_J satisfies V'=hV-(S+T)/2. The field identity in (16), S'-yV'=aS+cV, follows without dividing by y. Multiplication by (S-yV)* and taking a real expectation gives (17), with y treated as a coefficient at that epoch. No y' term belongs in that multiplication: it is not a derivative of a variance with a time-varying coefficient.

Let A=C_SS, B=C_SV and C=C_VV. In launch_check's independently derived chart, alpha=1+(x-y)/2 and gamma=JR+hy. Its lift is

    (alpha,y,y^2,gamma-alpha*y,gamma*y).

The canonical chart is

    (x,y,y^2,JR-xy/2,JRy).

The two residuals are identically equal under this affine/polynomial change of coordinates. I checked that identity symbolically in the separately labeled targeted source controls. Thus the change of basis introduces no missing factor, sign or time-leg term.

The canonical helper builds the exact row in (18). It requires finite rational h,J and data, J>0, exactly five rows, positive-semidefinite equal-time two-field covariance, full row rank, both monomial identities, R>0, nonzero y and q>0. In particular neither monomial condition is omitted. An arbitrary linear five-vector is not silently interpreted as a physical coupling. The note correctly limits the converse to these eliminated covariance equations; full background/scalar dynamics and the measurement supplier remain separate.

Substituting the full moment dynamics into the row gives (19). The transformation from (C_SS,C_SV,C_VV,C_ST,C_VT) has determinant exactly 1/8. Positive-definite three-field covariance matrices contain an open set, and the projection to those five moments has full dimension. The allowed linear state triples and rho>0 constraint completion therefore establish available rank. They do not establish a realized cosmological ensemble or useful conditioning. Bounded finite ensembles can realize the covariance construction after amplitude scaling, with free scalar velocity data still retained.

I applied the copied canonical inverse to launch_check's distinct positive-definite witness Sigma=t t^T+I/7, with five t=(r,1,w) choices from its proof. In the canonical row basis the determinant is 8/7, and the inverse recovers the supplied R,x,y,q exactly. I also checked exact refusal of zero y, zero/negative q, zero/negative R, nonpositive J, nonfinite moments/background, rank loss and separate violations of each monomial identity. These are targeted post-exposure API checks, not an aggregate rerun or empirical experiment.

One notation suggestion was sent to root: use (C_SS)' and (C_VV)' for total auto-power derivatives in (17)–(18), because the preceding C_SW' notation explicitly denotes a single time leg. The surrounding proof already says total derivatives, so this is clarity rather than a mathematical factor defect. Root accepted a future wording repair. Five independent rows are a sufficient construction; no minimum-row theorem is proved or needed.

## 3. Error, candidate and transverse domains

The three-row error formula is unchanged. AST comparison confirms that rational, vector3, system, inverse and norm_inf are identical to the previously checked helper, and that error_envelope differs only in its terminal positive-coefficients labels. The docstring and note now explicitly leave normalized observable admission separate. The original exact P-crossing witness is implemented as a control and continues to return a positive coefficient certificate without pretending to certify the denominator. The prior finding is properly closed in this source version.

The norm proof covers the interior of the allowed input box; the 512 author corners are illustrative controls rather than its justification. Equation (20) is explicitly limited to the three-row coefficient inverse. No unproved uncertainty theorem is extended to the nonlinear monomial tests of the five-row lift. Exact identities are not noisy-data rejection thresholds.

The relative-F condition, background kinetic relation and potential normalization in (21) match the independent Jordan-time equations and their N conversion. The extension helper independently differentiates the relevant Einstein expressions and obtains the same identities. Absolute F remains tied to the unknown dust normalization. The numerical potential function is diagnostic, not an unguarded claim of empirical scale selection; full forward/potential numerical validation belongs to the separate checker.

The revised-family section explicitly supplies the whole radial/transverse kinetic metric, matter coupling and potential. Its geometric q, Fc/F relation, two-epoch determinant, branch inversion and gamma/nu potential solve agree with the already checked M12 family and working extension. Positive beta/kappa/q and independent potential-basis conditions remain necessary. Two calibrated epochs cannot establish an interval identity or choose a fundamental action. The canonical primary checks the frozen numerical cases' saved-epoch domains; it does not claim a generic interval certificate.

Arbitrary transverse linear modes decouple about the stated radial background because the mixed kinetic and potential/matter derivatives vanish as stated. Their free initial data are not set to zero. The note preserves the distinctions from nonlinear backreaction, nonradial backgrounds and stability inferred solely from a potential Hessian.

## 4. Source and evidence correspondence limits

The primary imports all five helpers and declares their exact bytes, the canonical note, fixed protocol and scope checklist. Its reported product source identities match the frozen copies. The products distinguish exact rational controls, double-precision trajectories, conditioning diagnostics and zero empirical tests. No raw observations, ancestral numerical results or external likelihood are loaded by this primary.

The canonical note's literature/admission paragraphs were read as part of the full note, but their external PDFs were not independently reopened here. That work belongs to the observation/source checker. I do not claim independent validation of those citations or of the current survey pipeline. Likewise I read the forward code for mathematical correspondence but did not rerun its ODE, its 301-time constraint diagnostic or the other checker's Radau calculation. The note correctly preserves those separate scopes, sampled turning signs and potential-conditioning limitations.

The N1–N8 checklist describes a positive conditional construction, not an exhausted search or universal no-go. Its live observation and full-history routes are consistent with the mathematics. This source check does not ratify a formal status or certify an integrated-main/review packet.

## 5. Targeted checks and preserved checker issue

The original independent count remains 30 exact checks. The later working-source count remains 14. This canonical pass adds 22 targeted post-exposure algebra/API/AST checks; all pass. They are recorded separately in CANONICAL_TARGETED_RESULTS_v2.json.

The first targeted script reported 21 passing refusal/identity checks, but its zero-y fixture used Python zero inputs in an expression that introduced a float. The copied exact-decimal helper therefore refused the fixture at a monomial test, rather than the intended turning-point gate. I preserved that script/result and recorded the test weakness. Version 2 converts all synthetic parameters to exact rationals before constructing moments, asserts the correct zero-y rejection message and adds a zero-q case. It passes 22/22. This is a checker-fixture correction, not an author-source or mathematical defect, and it is not hidden by the passing aggregate count.

Within the complete frozen note and mathematical source scope, no substantive equation or implementation discrepancy remains. The one notation improvement and already repaired certificate-label distinction are separately recorded. Any later source changes require a narrow supplement; no result here should be attributed to bytes outside the stated freeze.
