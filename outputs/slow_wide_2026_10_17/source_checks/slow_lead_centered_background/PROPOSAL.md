# Centered recovery removes the resonant derivative cost

Status: root-authored conditional proposal requiring a distinct check. This concerns only the represented nonemitter finite coordinates and complete closed tails. It does not by itself establish a new complete-state or finite-device theorem.

## Sources and exposure

Use the wider domain and literal apparatus of `slow_lead_wide_complete/PROPOSAL.md`, SHA256 `5275860cb241a358d53460e88183879009a9899de7172c7c3b2e75629eb42fba`. That composition is currently under separate review; its exact spectral decomposition is also the previously checked onset interface `slow_lead_complete_onset_frontier/PROPOSAL.md`, SHA256 `c590e093e7a4ca6abc1e147414f5ee5b08e725fa1a881b266fae7271b56e0d46`, check `5f8b8a3b4aea4008c07d9d8e59b53a7c58bf4cb0deead4d7da66be84a2c4a32b`. Wider full8 endpoint source `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3` and check `c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5` supply eta. Wider derivative source `c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a` and check `c74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79` supply L0=4e5 and M=sup||L'||. All were fully read by root; this is new author work, not their reviewers' approval of this new argument. Original source/calibration and physical identification premises remain conditional. No scientific runner or parameter search was performed.

Domain: .0027<j<.003, 0<kappa<=1e-8, 0<g<=1e-6, 0<h<=4e-6, gamma=kappa²/j, d=2j sin h, H=d/gamma>=100, d/g<=.5. On each of the two physical windows, write delta=E-center. Work separately on both Stone lips and record-X sectors, with arbitrary old input and passive references.

## 1. Retain the existing full emitter replacement

The represented background column is -kappa L(E) Tactual(E) Vseed, where Vseed here selects the prepared source-vacuum internal columns. Replace Tactual by the full8 Tref, keeping actual L. The full resolvent comparison still pays at most 2 kappa L0 eta across both windows and both lips. No density-only refinement may replace eta in this step without a new proof.

On a given window the diagonal reference applied to Vseed has one selected vacuum channel with

    Tref_sel(delta)=1/(delta+gamma w(delta)),
    w=exp(iq), delta=-2j cos q,

on the upper lip, and its conjugate on the lower lip. The other prepared vacuum channel is separated by the old-energy gap. The same reference gap bounds used in the onset proof give norm at most6 and derivative at most37 there. The six non-vacuum reference channels are not excited by Vseed. This is a property of the diagonal reference, not a compression of the actual full emitter output or its error.

## 2. Replace only the selected reference scalar by a Lorentzian resolvent

Put Tlor_+(delta)=1/(delta+i gamma), Tlor_-=1/(delta-i gamma), r_delta=sqrt(delta²+gamma²). Since |w-i|<=|q-pi/2|<=|delta|/(2j cos h) and |delta+gamma w|>=.9999 r_delta, a safe bound is

    |Tref_sel-Tlor_+| <= (gamma/j)|delta|/r_delta²,

and likewise on the other lip. Thus replacing these selected factors costs, over both windows and lips,

    Bscalar <= (2 kappa L0/pi)(gamma/j) log(1+H²).       (1)

This is a real-band comparison. No continuation of the actual L or source is used.

## 3. Subtract the center before integration by parts

For each lip and selected channel write L(delta)=Lc+DeltaL(delta), Lc=L(0). On the full closed window ||DeltaL||<=M|delta| and ||DeltaL'||<=M, with all finite and closed coordinates retained. Therefore

    ||(DeltaL Tlor)'|| <= M/r_delta+M|delta|/r_delta².

The two endpoints contribute at most 2M d/r_d. Integrating the displayed derivative gives 2M asinh H+M log(1+H²). Applying real-energy integration by parts, then paying both lips and both windows, bounds the varying part by

    Bvary(t) <= (2 kappa M/(pi t))
       [2d/r_d+2asinh H+log(1+H²)],  t>0.             (2)

The subtraction is separately defined on each lip/window; no equality of Lc on different windows or sectors is assumed. This removes the L0/gamma term from the former product-derivative bound. The derivative M remains an independently supplied obligation; a value bound alone is insufficient.

For the constant part, the full-line Fourier integrals of Tlor are -2pi i exp(-gamma t) for the upper lip and zero for the lower lip when t>0. These follow by closing the rational integrand in the lower half-plane. For each lip the removed two tails |delta|>=d have oscillatory integral norm at most 4/(dt): integration by parts pays two endpoints <=2/d and integral derivative <=2/d. The integrals are understood as symmetric improper limits, whose boundary terms at infinity vanish for t>0. Consequently the constant parts, on both windows, are bounded by

    Bcenter(t) <= 2 kappa L0 exp(-gamma t)
                         +8 kappa L0/(pi d t).        (3)

The full-line calculation extends only the explicitly introduced rational comparator, not actual L, physical spectral coefficients or the actual Hamiltonian's energy band.

## 4. Complementary prepared reference columns

On each window these columns have Tref norm<=6 and derivative<=37. Direct integration by parts, retaining both endpoints, gives 12L0+2d(6M+37L0) inside the per-window bound. Adding both windows and lips therefore costs at most

    Bwrong(t) <= (2 kappa/(pi t))
                         [12L0+12dM+74dL0].          (4)

This safe sum does not assume orthogonality of the two input error ranges. The reference channel's actual window phase is kept. Parity blocks and the orthogonal record-X preparation combine without another factor. The selected and complementary reference channels exhaust the prepared source-vacuum input after the full8 replacement error has already been paid.

## 5. Conditional background envelope and one fixed evaluation

Adding all these terms gives the proposed sharper background bound

    B_I(t) <= 2 kappa L0 eta+Bscalar+Bvary(t)
                                      +Bcenter(t)+Bwrong(t). (5)

It is an alternative to the earlier IBP bound; take their minimum where both hold. This charges no new omitted state, and makes no statement about emitter or traveling terms.

At the single already proposed wide candidate kappa=1e-8, h=4e-6, g=5e-8 and t>=T=1e15, use the checked-domain enclosures M<6.49e17, eta<5.3e-6, gamma/j<1.4e-11, d>2.15e-8, d<2.4e-8, asinh H<15, log(1+H²)<28, pi>3.14, gamma T>100/3. Then:

* Bvary < (2e-23/3.14)*(6.49e17)*60 <.000249.
* Replacement <4.24e-8.
* Bscalar <(2*.004/3.14)*1.4e-11*28 <1.1e-12.
* Bcenter <.008*2^-33 +.032/(3.14*2.15e7) <4.9e-10.
* Bwrong <(2e-23/3.14)*[4.8e6+12*(2.4e-8)*(6.49e17)+74*(2.4e-8)*4e5] <1.3e-12.

The bracket in (2) is strictly below60. These relaxed bounds give B_I(t)<.000250 uniformly for t>=T, replacing the proposed wider composition's .000607 background allowance. This is a sufficient bound on the same conditional apparatus, not an observed error or new operating-point search. It does not yet combine any pending sharper seed-mass result.

## Review obligations and limits

A distinct checker should verify the full8 replacement/selected-reference split, lip and window factors, the scalar-to-Lorentzian comparison, the improper Fourier and tail bounds, and the complementary prepared channels. In particular, an improved prepared spectral-density estimate cannot be silently used for the earlier full resolvent replacement. The construction preserves every nonemitter finite/closed output and passive references. Actual omitted state, full emitter, incoming/outgoing errors, target normalization and finite cut remain separate. Exact supplied coefficients/seed, old aging/common phase, physical time/Record identification, finite-window versus permanent halt, and reset/reuse qualifications remain unchanged. No publication or retained-status claim is made.
