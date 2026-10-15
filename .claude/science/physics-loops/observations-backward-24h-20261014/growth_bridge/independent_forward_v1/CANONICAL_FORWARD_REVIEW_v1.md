# Focused canonical forward-source correspondence, version 1

This report covers the consolidated forward implementation and candidate assessment at the exact snapshot below. Root remains the scientific author. It is a focused source/computational check, not formal audit, integrated landing approval or empirical validation. The original independent derivation, six numerical integrations, original failures and FORWARD_REVIEW_v1.md remain unchanged.

## Source and scope

I froze and read the complete canonical helper `scalar_growth_lensing_inverse.py` (SHA256 `5561f381fd2fd82ae1a979dcd8d79f275f8b4a500f3fbbc607c8a82ad63efecf`), complete primary runner (`9b229daa53db4d896709f4741b4499d59e2440b191d5305143196ea6ff4a0fae`) and complete canonical note (`28b28d2a9da9c7682bc225f8b97e122bac638059cf88c5f4986876b2d20df9a7`). Copies and original path identities are in `canonical_source_v1/` and `CANONICAL_SOURCE_SNAPSHOT_v1.json`. The scientific disposition here concerns the full `source_model`, `inverse_rows`, `forward_controls`, `candidate_domain` and `assess_candidate`, their interactions, and the note's forward/background scope. Other inverse/classification proofs were read as context; this report does not replace the separate math review. External-source/observation claims were not independently re-read from primary publications in this task.

The previous working forward source was `f72a91a02850a149bd0d002aadac6647039838cbb1c85e6b8b26a551fddad8fa`; its protocol remains `1a3e541a71573b43b6c7ffc26d8a61680cc75d4f8fa96403f31937cc62edc088`. The copied background source was the previously reviewed M12 helper `1bf2d30207b99cea8508a612a739ed8b82dc7d6860920e101fb4e1374eccd9be`. These identities are not relabelled as current canonical sources.

## Unchanged equations and proper source closure

Exact AST comparisons establish that canonical `source_model` is the previously checked function, and canonical `inverse_rows` is the previously checked observable-only inverse. The nested `background`, `perturb_read` and `ode` functions are also exact AST copies. The complete old-to-new `forward_controls` delta is retained in `CANONICAL_FORWARD_DELTA_v1.patch`. Its changes are protocol injection, a local call to copied `source_model`, extraction of later assessments into the gated helper, one per-case sampled-domain control, and return/packaging structure. The numerical equations, initial data, sampling, integrator settings and tolerances did not change.

The direct root source no longer reads an unmerged M12 helper. It differentiates the supplied radial action locally with SymPy, and uses the same Einstein-to-Jordan clock, scale, density and F-derivative conversions previously checked independently. In particular the implicit continuity denominator, minus sign in q'/(1-q), and J=[I+3(Phi-Phi0)]/W0 normalization are intact. No new ODE run was needed or performed.

The primary reads the fixed protocol and imports only the consolidated scientific helper plus standard numerical libraries. It hashes the primary and four declared paths, then writes the configured result and summary. The helper performs no scientific file read. The action-copy provenance is an honest source history, not a runtime transitive dependency. Full repository dependency/index/cache validation remains outside this scoped source check.

Inverse truth separation is unchanged. The inverse receives q,P,What,J from three calibration epochs; source beta,B,C are used afterward for recovery diagnostics. Every returned candidate is preserved. The remaining three fixed epochs test it. The six previously computed histories remain synthetic reduced-model controls, not independent empirical tests.

## Candidate gates that are correct

The added sampled-domain check requires finite real beta,B,C,q,J; strict 1/4<beta<1/3, positive B, 0<q<beta and J+C>0. Exact rationals are kept through comparison, including beta=1/3-10^-20. No float conversion collapses that admissible point onto the excluded upper boundary. `assess_candidate` calls the gate before evaluating Z, so q=beta is refused without pole evaluation, even if unused P/What keys are absent.

`canonical_source_check_v1.py` was frozen before execution. It checks AST correspondence, the exact near-boundary point, both exact boundary exclusions, nonfinite B/C, zero q, negative density, empty rows, a singular q=beta case, and regular exact residuals. It additionally reapplies only candidate gates and later residual evaluation to all six already frozen working histories. This is data reuse without ODE recomputation. All 28 focused checks passed; every actual candidate passes the sampled gates and all later residuals and decisions are numerically identical to the old working results.

This passes a limited set of checks, and does not erase the additional material finding below.

## Material finding: nonfinite readout can be falsely admitted

The snapshot's gate does not check P or What, and the residual acceptance does not explicitly reject nonfinite residuals. Set beta=.29, B=.2, C=2, q=.1 and What=1. Take two rows J=0,1, with P0=B*C/Z_beta(q) and P1=+infinity. Calling `assess_candidate` on indices [0,1] returns:

    relative_residuals = [0.0, NaN]
    sampled_domain_passed = True
    within_fixed_threshold = True

Python's max([0.0, NaN]) is 0.0. Thus a nonfinite later lensing value can pass the generic helper instead of being refused. The exact copied source, independently written reproducer, pre-execution freeze and actual JSON-safe result are preserved as `nonfinite_readout_witness_v1.py`, `NONFINITE_WITNESS_SOURCE_FREEZE_v1.json` and `NONFINITE_READOUT_WITNESS_v1.json`. The witness is post-source-exposure, not a blind derivation. No original test or tolerance was weakened.

The six finite trajectories are unaffected. The positive-q theorem is not refuted because its supplied finite physical histories exclude this input. However a generic assessment routine intended to reject invalid/nonfinite inputs should not announce admission here. I promptly reported the exact witness to root. A finite-positive P/What input gate and explicit finite residual acceptance can close the defect; this version does not presume a repair. Any repaired source requires its own narrow confirmation.

## Prose and surviving limitations

The note now correctly calls the continuity control an absolute normalized error despite the historical protocol key containing “relative.” It separately calls later algebraic residuals relative. It identifies order-unity contrasts as linear mode normalization, and it says sampled gates do not certify unsampled times. Its 60-control claim explicitly refers to the old working forward run; this report does not substitute the current combined suite count for that history.

The full homogeneous radial backgrounds and explicitly supplied r=q closure remain separate. Exact linear dust conservation is retained inside that reduced response; no full-action perturbation evolution, finite-mass approximation bound, scalar homogeneous-state selection, nonlinear perturbation validity, actual observation operator, covariance or likelihood is supplied by these controls. Extra inverse arithmetic precision acts on rounded synthetic inputs. Neither the current equations nor the independent source agreement establish new observed precision.

The canonical cache/results were stale at dispatch and are deliberately not bound as current here. A fresh source-bound run and source/product identity confirmation will be a separate final step. Apart from the nonfinite-readout admission defect, this scoped review found no changed forward equation or incorrect source consolidation. The earlier reports, both serialized-output failures and the new material finding remain preserved without relabelling.
