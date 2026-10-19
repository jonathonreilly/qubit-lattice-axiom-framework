# Neutral resonance contrast with the fast background retained

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_realaxis_contrast.py](../scripts/native_realaxis_contrast.py)

The original scalar diagnostic can show a depletion rather than an extra
positive peak when its neutral composite channel is included. A nonzero
outgoing residue therefore does not by itself establish a visible positive
particle line. This block derives a broadened-response comparison in a
specified coefficient model and preserves the background that the earlier
pole-component envelope excluded.

## Exact source Schur identity

Set Jz=1. Keep the native leading source -sqrt(2)lambda d, fast resolvent R,
slow punctured-host matrix h, and the previously derived crossvertices V.
Attach the slow arm's endpoint resolvent g_s through its native -1 vertex:

    h_s=h+h_A g_s h_A^T/(1-g_s h_AA),  b=V^T R d,
    G_C=2lambda Rdd+2lambda² b^T(I-lambda h_s V^T R V)^-1 h_s b.

This identity is exact for the specified model. For physical broadening
eta=beta lambda^4, beta>0, the fast and slow imaginary energies are
beta lambda^3 and beta lambda². Genuine upper-half-plane resolvents give a
nonnegative total spectral response -Im G_C/pi. The correction term alone
need not be positive.

Define G_C^0 by replacing h_s with h, keeping the fast sector and source.
This arm-deleted comparison is a mathematical diagnostic, not a native
operation or an independently available experiment. Its signed difference
isolates interference associated with the chosen channel within the model.

## A controlled leading-model comparison

For the leading nearest-neighbor fast model, the confined arm has hopping
-2 and slope f_fast=lambda^3/16. Its exact Bessel ratio and interior
oscillatory asymptotic give a bounded nonzero endpoint Green function for
each fixed beta>0. The fast contractions then approach

    V^T R d -> -(1,2)/2.

For the slow nearest-neighbor arm put f=lambda²/8, sigma=h_AA(-2),
a=sigma/(1+sigma), and u=(1,2)/sqrt(2). In the window

    e=-2+alpha1 f^(2/3)+f(2+Re a)+lambda²(x+i beta),

uniformly on compact real x intervals,

    (G_C-G_C^0)/lambda² -> B+R0/[x+i(beta-Im a/8)],
    B=-(u^T h A)^2/(1+sigma),
    R0=(u^T h A)^2/[8(1+sigma)^2].

The regular term B is essential. An initial numerical comparison omitted
it; the discrepancy led to the corrected derivation. The squares are
bilinear, not absolute squares.

Checked quadrature gives R0=-0.03036208824-0.03638513790i and
B=0.24029040084+0.14213670689i. The pole part at x=0 contributes
Re R0/[pi(beta-Im a/8)], which is negative for these numerical coefficients.
This is a depletion against the positive full spectrum. It is not a
negative probability or a rigorously interval-certified sign claim.

## Why background resolution is still an obstacle

In this leading fast model the arm Green function is

    g_f=-J_(2-z/f_fast)(4/f_fast)/(2 J_(1-z/f_fast)(4/f_fast)).

Its phase ripple has damping exp(-16pi beta) and physical energy spacing
asymptotic to lambda^4/8. At fixed beta the leading fast background is
O(lambda), while the arm comparison is O(lambda²). A fixed-width smoothing
on the mode's lifetime scale does not automatically remove the fast ripple.
The underlying [Bessel recurrence](https://dlmf.nist.gov/10.6) and
[Debye expansions](https://dlmf.nist.gov/10.19) are standard prior art.

The native K2 correction changes the accumulated fast phase substantially;
the leading model's phase cannot be transferred to the complete native
spectrum. Separate numerical controls retain the corrected native fast
K2 dispersion, contacts and arm hopping, plus leading slow host/tension,
crossvertices and source. They check total positivity and signed contrast.
They omit slow K4, K3 contacts and higher source coefficients. These controls
are not a complete microscopic response theorem.

The root derivation (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9768/REAL_AXIS_CONTRAST_PROOF.md`)
and focused Schur/Bessel checks state these boundaries. Broadening,
comparison channel and observable remain analysis choices. No empirical
calibration or independent observation test is used; detector identification,
full native signal visibility and cosmological mediation remain open.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.
