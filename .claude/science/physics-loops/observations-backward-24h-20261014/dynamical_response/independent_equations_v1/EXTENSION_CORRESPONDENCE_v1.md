# Post-exposure check of the domain helper and statistical input extension

This supplement follows the independently frozen equation derivation and the complete two-note working-source report. It is a focused mathematical source check, not a new independent derivation of the author's source, empirical verification, numerical-forward review or formal audit. Root remains author. No author aggregate was rerun.

## Exact complete read scope

I copied and completely read the following immutable versions:

- `domains_v1.py`: SHA256 `f871a82cc8420a60dff830849376595eb8ff71fc8cc7246b7d159954244aa7d7`, 6,285 bytes.
- `DOMAINS_RESULT_v1.json`: SHA256 `a0f86b9398a91f8303129cbaabb0240f5733060fc15e2deb0da185d6428d221e`, 2,064 bytes.
- `STATISTICAL_INPUT_v1.md`: SHA256 `79604dea5cd68201d2216a7f085f64c496daec0821bace3da6fe2d1c85312c86`, 2,417 bytes.

The result receipt reports 23 passing author controls, including a single aggregate control covering all 512 rational corners. I inspected the implementation and receipt but did not invoke `checks()` or rerun the 512-corner sweep. A separate small probe imports only the copied helper, calls its envelope API once, and checks three independently assembled covariance identities/witnesses. All writes remain in this independent directory, with Python bytecode disabled.

## Exact-decimal API and coefficient envelope

`rational` deliberately accepts finite real values representable through the stated exact-rational/decimal convention. Booleans, nonfinite numbers, complex values and unsupported symbolic irrationals are refused. In particular conversion through the supplied decimal representation is an input convention; it does not upgrade rounded physical data or a floating ODE solution to exact measurements. The three-row constructor checks dimensions, nonzero supplied P and exact matrix rank. `inverse` additionally requires R>0, y!=0 and q=x/y>0. Those gates match the conditional canonical action chart.

The envelope implementation agrees with the reviewed proof. Its d includes both individual product errors and their cross term, uses the induced infinity norm of the inverse, and requires eta<1. The state and ratio formulas have the correct denominator orientation. Negative input envelopes are refused. Broad matrix error, possible turning crossings and unresolved positive coefficients return an inconclusive result rather than a physical rejection. Zero-error inputs recover exact coefficient values.

The 512-corner check is a useful exact control. It is not the proof that every interior point obeys the bound: that proof is the norm inequality, which was checked separately. The API does not implement any observationally achieved uncertainty, prior or likelihood.

## Narrow label finding: coefficients versus full observable chart

The helper currently calls a positive R/q result `positive chart certified`. The formulas certify the reconstructed coefficient chart conditional on already valid normalized inputs. They do not independently certify every denominator used to define those inputs.

A concrete exact witness is preserved in `EXTENSION_PROBE_RESULT_v1.json`:

    Phat=(1/1000000,1,2), rhat=(0,1,-1),
    zhat=(R,x,y)=(1,1/10,1/5),
    Mhat_i=R-Phat_i*x/2-Phat_i*rhat_i*y/2,
    eP=(1/500000,0,0), er=eM=(0,0,0).

The helper returns certified=True, eta=12/3999997, state_error=12/3999985 and q_error=18/799985. Nevertheless the allowed first P interval includes zero. In the original normalized readout, that zero may make r undefined even though the coefficient matrix can remain invertible.

This does not refute the coefficient perturbation theorem, which presumes valid true normalized readouts. It is a scope/label issue. I sent root the witness and suggested the narrower wording `positive coefficients certified`, with observable-chart admission left explicit. If a full observable-chart certificate is intended, separate margins and physical input denominators must be supplied. Merely bounding fitted coefficients cannot establish those missing physical conditions. This report preserves the original source and finding, regardless of subsequent wording repair.

## Statistical covariance equations

The undivided mode equation is

    D(S'+S)+R W+(D/2)(x S+y T)=0.

The coefficients D,x,y,R are common background quantities for each declared row. Under the stated finite-covariance and derivative/expectation interchange premise, taking the real covariance with W gives

    C_WW R+(D/2)C_SW x+(D/2)C_TW y
      =-D(C_S'W+C_SW).

No Gaussian assumption is needed. The same real coefficient vector must apply to all rows, and the resulting covariance-row matrix must have sufficient rank. The existence of three shells or three summary numbers does not itself give rank. A broad wave-number window cannot replace the K-dependent D by its value at the center without a separate approximation.

For C_WW>0 and C_SW!=0, the definitions P=-D C_SW/C_WW, r=C_TW/C_SW and M=-D(C_S'W+C_SW)/C_WW reduce the equation to the prior normalized form. Euler covariance implies

    gW=C_W'W/C_WW=(ln C_WW)'/2,
    r=2 E^2 a^3(gW+2+h)/(3P)-1.

The factors and signs match the independent Jordan Euler convention. Since D'=D,

    P'=P[1+(C_S'W+C_SW')/C_SW-2gW],
    M=P'+P(2gW-eta), eta=C_SW'/C_SW.

The author explicitly retains eta rather than replacing it with gW. That is necessary with general preparations. A deterministic relation W'=gW W in every realization suffices for the replacement but is not inferred merely from an auto-power growth rate.

Two exact local covariance witnesses make the input distinction concrete. Let xi,zeta be independent centered real amplitudes of unit variance. Set W=xi, W'=zeta and S=xi+zeta. Then gW=0 but eta=1. This alone disproves an unconditional eta=gW identity.

For a separate diagonal/time-leg witness keep the same S,W at one epoch. In case A choose S'=2xi+3zeta and W'=zeta. In case B choose S'=3xi+3zeta and W'=0. In both cases C_SW=1, the total derivative (C_SW)'=3 and (C_WW)'=0, but C_S'W is respectively 2 and 3. Thus equal-time covariance and its total derivative do not identify its first time leg. These are algebraic covariance examples, not a claim that two complete cosmological solutions share every observation and background coefficient. The note's narrower input-obligation claim is what they test.

This extension therefore correctly distinguishes a coherent individual-mode identity from a ratio of survey summaries. It does not assert that the additional time-leg information is impossible to measure or model. Lensing projection, velocity bias and stochasticity, unequal-time inference, finite windows and shared calibration remain supplied physical inference obligations.

## Outcome and limits

No equation, norm-bound, covariance-time-leg or exact-rational implementation discrepancy was found in the read sources. The one certificate-label scope issue above was sent to root with an exact API witness. The three symbolic/covariance probes passed. The source helper's reported 23 controls remain author evidence, not newly executed independent results. No data, full code aggregate, ODE, statistical coverage claim or formal verdict is included in this supplement.
