# M14 affected-source supplement, version 2

The complete v1 mathematical review remains unchanged. This supplement covers only the full source deltas frozen at 2026-10-15T15:07:54Z, after the v1 report was saved. No aggregate, ODE, empirical analysis, formal audit or publication check was run.

## New source identities

| Changed source | SHA256 |
| --- | --- |
| SCALAR_DYNAMICAL_MOMENTUM_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md | 2133ec1786855f768c261f243f77c1fcc114001c4b583d1115fdec4defb6dd30 |
| scalar_dynamical_covariance.py | 091fb733a5529c3b5ea0e7f05814c00fb5a2835c31a8096619dd3170cade9d20 |
| scalar_dynamical_extensions.py | d74ae0ecf222446ae939b19d7e78b63cf7fda454c2a3fef3138037f7706d7a3a |
| scalar_dynamical_momentum_inverse_check.py | cb233af6423d3dae7f35f2bc079df2b62c4720d599472326ff191026a645a8d0 |

The domains, forward and geometry helpers have exactly the v1 hashes. CANONICAL_AFFECTED_FREEZE_v2.json lists all source identities. Complete unified diffs and copies of every changed source are preserved. I read every changed line and its full affected functions; unchanged arguments use the complete v1 review.

## Note-only clarification

The canonical note now writes (C_SS)' and (C_VV)' in (17)–(18), explicitly distinguishing total auto-power derivatives from the earlier single-leg notation. It also says five independent rows suffice and makes no minimum-data claim. These are faithful clarifications of the reviewed proof, with no change to the covariance identity or its domains.

## Covariance controls and unchanged inverse

The functions lift_row and inverse are AST-identical to v1. The production equation, rational/PSD gates, rank check, both monomial tests and coefficient domains are unchanged.

The control changes isolate each nonlinear monomial identity separately. For each chosen bad lifted vector, the control alters only the auto-power derivative so the same row matrix has that vector as its exact linear solution. A missing square or product compatibility test therefore cannot hide behind a different inconsistent condition. This corresponds to the two separate negative probes already checked in my v1 canonical pass.

The negative-PSD control now uses C_SS=C_VV=1 and C_SV=2, with all derivative moments recomputed from the common dynamical coefficients. Its 2-by-2 principal determinant is -3. I checked separately that the otherwise assembled five-row matrix remains invertible, determinant -7/1920, and recovers the correct physical lifted coefficient vector when the covariance-admission gate is omitted from the algebra. Calling the unchanged copied inverse rejects this input specifically with the positive-semidefinite error. Thus this fixture now isolates covariance admission instead of relying on an unrelated monomial failure. It is an intentionally impossible covariance, not a failed physical candidate.

## Potential extraction and exact event

The numerical per-epoch arithmetic formerly inside potential_diagnostics is moved into potential_readout. Its beta-to-k branch, s parameter, omega, relative potential, exponential-u conversion, C and basis functions are unchanged by inspection of the full diff. The diagnostic still carries no achieved measurement precision or generic physical-domain certification. The full forward and potential numerical outputs remain assigned to the independent forward checker; I did not recompute them.

The new software control uses k=1/6 and exp(2alpha u)=2. Direct algebra gives

    beta=5/16, s_m=14, q=5/44, f=29, C=30/29,
    u=2 log(2)/sqrt(5),
    U0=3/2+21/841, U1=15u^2/(2*841).

At the supplied E=13/10, x=3/50, R=2/5 and aJ=1, the target is vpot*C/2 with omega=(44/5-3)/2. These values agree with the new expected constants and normalization. My separate affected-source probe evaluates the copied potential_readout on this event: the largest absolute difference from the exact expressions converted to floats is 8.9e-16, below the stated 1e-13 software tolerance. This is post-exposure correspondence, not an independently measured scale or an error enclosure for the ill-conditioned two-epoch fit.

The primary change adds this decoder control to the background group. It does not alter the scientific run protocol, read inputs or the inverse. The additional independent monomial fixture also changes the author control count. A fresh exact-source execution is needed to bind the new aggregate count; the v1 81-control receipt must not be relabeled as covering these new bytes.

## Result and limits

Seven targeted affected-source checks passed: four AST comparisons, the exact-backed decoder event, the otherwise-valid negative-PSD lift and its specific rejection. They are recorded in CANONICAL_DELTA_RESULTS_v2.json. No substantive mathematical discrepancy was found in the affected scope. All original proof, setup/failure history, v1 source copies and reports remain preserved.

This supplement plus the complete v1 report covers the mathematical source changes listed here. It does not bind a future metadata/whitespace/source change, a fresh runner cache or a staged delivery tree, and it is not a formal approval.
