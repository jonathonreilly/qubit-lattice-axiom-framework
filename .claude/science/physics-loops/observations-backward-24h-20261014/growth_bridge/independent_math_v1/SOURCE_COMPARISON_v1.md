# Post-exposure source correspondence v1

This is a separately labeled source check after the independent proof, interval extension, continuity extension and 43 independent exact controls were frozen. Root remains author. No formal audit, raw observation access, external literature check, Git/status/cache operation, source edit or author aggregate execution occurred.

## Exact complete read scope

I read all 172 lines / 8,708 bytes of the frozen author `WORKING_v1.md` (SHA256 `7540ac4431c3b2a1ff553edf52eb7c30f86522ded8e16804cdf4d99aa7e04fe6`) and all 188 lines / 10,160 bytes of `growth_inverse_v1.py` (SHA256 `1e12edf8106f43a97a9636d7d8f7fc46c351f6773bd8d2b46fef54851b72a894`). Exact copies are preserved as AUTHOR_WORKING_v1.md and AUTHOR_growth_inverse_v1.py. No v2 note/code was read. I did not open the synthetic protocol, author aggregate results, claimed repository search evidence, literature sources, or observational summaries, so those are not independently verified here.

## Mathematical correspondence

The metric signs, force factor two, slip quotient and the Weyl source agree with the independent proof, within the stated frozen-coefficient linear response model. The two-scale affine inverse of 1/r in 1/K² is algebraically correct, conditional on a common positive coupling and nonnegative single effective mass at that epoch. It does not derive this response model or eliminate the homogeneous scalar mode; the working note and code explicitly preserve that limitation.

The author's B is rho0/(3H0² Fc), equal to 1/v in my proof; it is not my dimensionful B=rho0/(3H0²). With that notation translated, G1 is precisely the difference of delta=I+d multiplied by the candidate chart and the lensing relation. Taking endpoint differences eliminates d without choosing it. Reconstructing d after fixing the candidate is a conditional inference, not a state-selection law.

The three-epoch coefficients in G2 follow by eliminating B between the two G1 differences (the possible overall sign of the polynomial is irrelevant). The cleared polynomial has degree at most two. Poles, positive B and all candidate-domain inequalities must be retained; an identically zero polynomial gives no finite-candidate conclusion. The code retains multiple admissible roots and does not claim a fourth epoch always singles one out. My exact interval family demonstrates why that qualification is substantive. The derivative-free integrated inverse and my four-parameter lift are consistent parameterizations, with the latter requiring w=u d.

G3 is the same conditional tensor-ratio inverse as my independent extension. It requires a physically calibrated F ratio, distinct-q sensitivity, a nonzero denominator and the candidate domain. Equal-q endpoint pairs give no shape information. The note correctly leaves endpoint/generation calibration, absolute normalization and complete background/action membership open.

The code's exact metric, coupling-chart, integrated-identity and tensor formulas correspond to the note. Source reading is not independent verification of the unrun aggregate counts or its protocol-selected synthetic cases. Binary64 roots remain a diagnostic with an explicitly separate tolerance. No empirical significance follows from any of these synthetic controls.

The v1 note still uses R=delta' with a stated neglected potential term. The independent CONTINUITY_EXTENSION_v1.md supplies the requested exact linear-dust kinematic replacement and its extra potential/calibration requirements; it is not falsely attributed to these v1 bytes.

## Concrete implementation finding F1: missing positive-q gate

`integrated_inverse` requires positive P,R and beta greater than every supplied q, but does not enforce q>0. `tensor_inverse` likewise does not enforce q_i,q_j>0. The canonical candidate requires 0<q<beta and F/Fc>1. The missing lower gate admits points outside that physical chart.

A focused post-exposure execution of only these frozen functions, not main or the aggregate, used:

| I | R | q | P |
|---|---|---|---|
| 0 | 1 | -1/10 | 27/26 |
| 1/4 | 1 | -39/400 | 5365/4136 |
| 1/2 | 1 | -19/200 | 1599/1028 |

The inverse returns beta=2/7 and B=1, and the associated tensor ratio also returns beta=2/7, even though every q is negative and each reconstructed F/Fc is below one. The result is preserved in POST_EXPOSURE_DOMAIN_WITNESS_v1.json, with a standalone reproducible witness script. This does not invalidate G1–G3; it requires explicit finite positive q input gates and negative/zero-q rejection controls in the source implementing the physical admission set. Root has been notified. This v1 report does not assert a repair before inspecting repaired bytes.

## Remaining boundaries

The working note's historical/prior-art and exposed empirical statements were not checked here. The supplied light/single-pole field model, growing real coherent sector, common calibration and physical H/mode map remain premises. The finite-epoch inverse supplies an admission set, not guaranteed identification, full action membership, a derived physical discrepancy budget or an observational fit. Later exact-source changes require their own scoped comparison.
