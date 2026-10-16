# M12 independent trajectory/readout/inverse check

Scope: focused numerical and source correspondence for the supplied action, by `/root/inertial_response_check`. Root remains author. This is not a formal audit, empirical action selection, a high-precision trajectory calculation, or an integrated-main check. I wrote only this assigned directory. No parent implementation or results were read before my source, protocol commitments and independent results were frozen.

## Independent derivation and freeze chronology

I first read the complete supplied future-confinement action note and original `SYNTHETIC_PROTOCOL_v1.json`. `PRECHECK_v1.md` gives the independent derivation: original Einstein equations in tau=Hv*t_E, the physical Jordan clock dt_J=sqrt(C)dt_E, analytic F,H,rho and derivative readouts, general FLRW inverse with pressure and spatial curvature, and candidate parameter recovery. `independent_inverse_v1.py` implements this derivation without importing author code. `PRECOMPUTE_FREEZE_v1.json` was recorded before execution (SHA256 `785a1d366ae6381d3ad037ba1e712c882b266a5154009a234afc02da121d085a`).

All twelve fixed cases ran once with empty stderr. `RESULT_FREEZE_v1.json` (SHA256 `aa7c370235f358517af191a02b3116b1b80538c1485cd993ba9881513efe4b5b`) froze source, precheck, results, summary and logs before any author output was opened. Author original results and precision diagnosis were then copied into `author_results_v1/`; only after parent supplied canonical exposure did I freeze and read the complete canonical helper, primary and note. This report is written after that comparison; it is not relabeled as a pre-exposure report.

The implementation integrates u,v,r with binary64 DOP853, where v=du/d(Hv*t_E) and r=rho_E/(Q Hv²). The parent independently integrates physical velocity, Einstein density, scale factor and Jordan time in Einstein proper time. These distinct state/clock implementations agree after unit conversion. The no-one-half action convention gives the matter force -alpha_B*r/(2K), the scalar friction -3hv and h'=-K v²-r/2. All 17 epochs are fixed, with calibration at indices 0 and 6 and residuals at 7 through 16. Parameters are not retuned on later times. The original 5e-7 parameter and 1e-8 residual tolerances are retained.

For clarity, my pre-exposure symbol D denotes the Jordan coefficient multiplying -(partial F)²/2. The author's D denotes kinetic stress. The conversion is

    D_author = D_independent * Fdot²,
    omega_author = F * D_independent,
    c_author = b_independent,
    Fc_author = Finf_independent.

With this conversion, the independently derived general inverse and both canonical metric equations agree, including curvature and pressure signs. My implementation accepts supplied pressure and curvature arguments; numerical histories are the original flat dust cases. Generic pressure/curvature validity is an algebraic source check, not a second observed or curved-trajectory sample.

## Original fixed-case results and preserved failures

Every mode uses the same independent binary64 trajectory. The three prospective modes differ only in arithmetic at the readout/inverse stage:

| Mode | Parameter tolerance | Maximum relative parameter error | Maximum later relative D,V residual |
| --- | --- | ---: | ---: |
| Binary64 source assembly/inverse | 11 of 12 cases pass; case 9 fails | 4.804360541399433e-6 | 1.8304278093239645e-9 |
| Lift rounded physical readouts to 50 digits | 11 of 12 cases pass; case 9 fails | 6.083588374789427e-6 | 2.3190330227367786e-9 |
| Assemble readouts at 50 digits from saved double states | All 12 pass | 2.8158809234001164e-41 | 1.1564508992950427e-44 |

In both failing modes case 9's nu recovery exceeds 5e-7. It remains a failure. All later residuals pass their fixed 1e-8 threshold, illustrating that small fitted residuals need not imply accurate recovered parameters. Maximum local direct-action D-coefficient identity error is 3.698743533675497e-10 in binary64 and 4.675049038508363e-10 after lifting rounded inputs. It falls to 2.295755211145431e-45 with source-assembled 50-digit inputs. The maximum subtraction cancellation ratio is about 3.5043496554e6.

These tiny source-assembled residuals test internal algebra at states of a supplied model. They do not certify integration error, give a high-precision orbit, or supply precision for physical F,H and their derivatives. Every generated readout uses the original action and parameters on the source side. Reconstructing them downstream is an implementation and inverse-identity control; it is not independent evidence for that action. The precision-lift failure explicitly demonstrates that merely using more digits cannot recover information lost in rounded physical inputs. I did not increase precision in the trajectory or modify the time interval to avoid that failure.

## Comparison to original author outputs

The original author `RESULTS_v1.json` is SHA256 `b8a3721a16dae081bf16aa342451aa85d3dc5bfa0b0fe7408031f131a884f822`; `PRECISION_DIAGNOSIS_v1.json` is `cf4f5f7dd99b9a079244c203aacbb5370a1da7be53a47e7afc2948a4b4b1d515`. `result_correspondence_v1.py` compares all 12 cases and all 204 states/readouts, without executing author functions. Exact case definitions match. The largest differences after unit conversion are 5.55e-16 in u, 2.22e-15 in dimensionless velocity and 1.11e-16 in dimensionless Einstein density. Relative physical readout differences are at most 2.44e-15. The cancellation-sensitive derived kinetic stress differs by up to 4.03e-10 relative, and q by up to 5.35e-11. Those differences are preserved rather than asserted to be exact numeric agreement.

The original author run has 90 passing controls and one failing case-9 parameter check; its nu error is 2.6967536211064402e-6. At 50 digits, lifting its stored rounded inputs still gives a failing 2.550157293603847e-6 maximum error, while reassembling source readouts passes. My independently generated floating errors differ, but all twelve per-case pass/fail classifications agree in the corresponding binary64, lifted-50 and source-assembled-50 modes. The independent implementation does not claim to reproduce the author's 80-digit run or all 91 original symbolic/domain controls. The comparison confirms the same conditioning mechanism, not bitwise equality between different arithmetic expression trees and integrated state parameterizations.

`RESULT_CORRESPONDENCE_v1.json` retains all per-case errors and cross-implementation differences. No original output or failed control was replaced. The original literal source and results remain unchanged in their snapshots.

## Complete canonical source correspondence

I read the complete canonical helper `scalar_cosmological_inverse.py` (SHA256 `435d7b03a8038a8bf2eddef1122e7123953d046071df2136f23f359412f27bd7`), primary `scalar_cosmological_inverse_check.py` (`df487184eb73a347b1c5c6aacc641d49ea482cac75e2494dac15dcd6d07923ca`) and canonical note (`e4025969133e49394328cf628dc2797d041cd643ba7785953f5bc495fbdef53a`). The helper implements the same original Einstein equations, clock factors, conformal density normalization and inverse after the notation conversion above. Its source-model derivatives are symbolic; my implementation writes the analytic derivatives directly. The source uses no older unpublished helper import. The primary declares the note, helper and original protocol, reads that protocol, and writes RESULTS and SUMMARY. No raw observations or likelihood are acquired by this run.

The candidate relation is D_independent=b/(F-Finf), b=(1-3a)/(2a). Both implementations infer the affine reciprocal relation at the two fixed epochs, choose the k branch inside 0<k<1/3, reconstruct Q0, and solve the two potential basis coefficients for Hv and nu. The canonical code checks positive F, kinetic stress, nonzero Fdot, distinct epoch values, the c range, positive boundary, potential rank and positive coefficients. Its later residual calculation has an equivalent normalization to mine up to the explicit max scale; their values are not asserted identical. The original protocol's epochs and tolerances are unchanged.

The canonical 50-digit assembly reconstructs rho_E and a_E from its saved rounded Jordan rows, then recomputes physical readouts and derivatives from the original action. That step must be described as algebraic reassembly at saved numerical states. It does not promote the original density/trajectory to an accurately measured state. The helper retains an explicit rounded-input case-9 failure control. The primary's uncertainty statement and original-failure record make the distinction explicit.

I checked the new curved manufactured metric readout directly: with F=2, Fdot=1, Fddot=0, H=.5, Hdot=-.25, curvature=.5 and zero matter, the source equations give D=3.5, V=4.25 and q=1/17. This confirms the added control's target; no author aggregate was rerun here. The source's transverse positivity and invariance expressions agree with the supplied diagonal kinetic metric and potential. The exact background equality requires zero transverse velocities; deriving x=y=0 uses equality on an interval plus the transverse equations. Two fitted epochs alone do not establish that condition. The note makes this distinction and keeps the action class, state choice, tensor endpoint map, measured functions and their uncertainties conditional.

I read all note sections for numerical/assumption scope. The supplied continuous input functions, field-chart domain, relative-normalization ambiguity, precision warning and lack of empirical action selection are stated. I did not freshly verify the linked gravitational-wave or distance papers, nor perform an independent general transport-theorem review; documentary review belongs to the separate scoped checker. No cached canonical execution was available for this report, so current-cache/output identity is not claimed here.

## Narrow open prose finding at these bytes

Section 6 says the kinetic-stress subtraction has maximum cancellation ratio 2.962906e6. The frozen precision diagnosis shows that number for case 9, while case 11 reaches 3.5043496545456173e6, consistent with my independent maximum. I notified root to qualify the former as case 9 or report the twelve-case maximum. This is an interpretation/counting correction, not a formula discrepancy and not a reason to rerun the unchanged scientific controls. The source-bound correction and final execution, if supplied, require a separate affected supplement; this historical report will not be overwritten.

The complete local evidence identity is in `NUMERICAL_IDENTITY_v1.json`. No fit to observations, initial-state principle, action derivation, rigorous numerical enclosure or retained-grade conclusion follows from this check.
