# Distinct conditional test: published GW170817 waveform dispersion

This is a primary-literature comparison in a specified waveform response
class. It is separate from the failed frozen three-band extraction,
which remains failed and supplies no measured bound. No new likelihood,
posterior, significance, or exclusion probability is computed here.

## Primary result and exact comparison

[Abbott et al., *Tests of General Relativity with GW170817*, DCC
P1800059-v9](https://dcc.ligo.org/LIGO-P1800059-v9/public), section III.A,
uses a Bayesian waveform-phasing test of

\[
 E^2=p^2c^2+\mathcal A p^\alpha c^\alpha.
\]

For `alpha=0`, `mathcal A>0`, the paper identifies
`mathcal A=m_g^2 c^4` and reports the graviton-mass upper-bound value
`9.51e-22 eV/c^2`. The paragraph is visually verified on page 10 of
the exact downloaded DCC v9 PDF. It does not restate a coverage level
beside that number, and this note does not infer a new coverage level
or a tail probability from the value alone.

The campaign's selected inverse-length pole is
`mu=6.42760036943869e-12 m^-1`. Its rest energy is

\[
 m c^2=\hbar c\mu=1.2683389725004337\times10^{-18}\ {\rm eV},
\]

which is `1333.69` times the reported waveform-bound mass scale.
The reported value corresponds to
`mu=4.819411911064732e-15 m^-1`, or a reduced-Compton/Yukawa length
`1/mu=2.074941960665641e14 m`. Here the static inverse length is
`m c/hbar`; replacing it by `m c/h` would introduce an erroneous
factor `2 pi`.

This comparison is applicable only if the selected pole carries the
observed radiative mode and the emitted signal belongs to the
published binary-neutron-star waveform class with the stipulated
propagation modification. A massive spectral component that is not
the observed mode is a different problem. An arbitrary positive
continuum, coherent mode mixture, modified source generation, or
different detector coupling is not constrained merely by copying this
one-parameter mass value.

The original paper's dispersion parameter `mathcal A` has energy-squared
units at `alpha=0`; it is **not** the earlier three-band coefficient
`A_t= D c mu^2/(8 pi^2)` with units `s Hz^2`.

## Relation to the phase and to the timing contrast

In the convention `t(f)=(1/(2 pi)) dPsi/df`, the small-mass extra delay
`Delta t=A_t/f^2` corresponds to

\[
 \delta\Psi(f)=-\frac{2\pi A_t}{f}
 =-\frac{Dc\mu^2}{4\pi f},
\]

up to terms degenerate with constant phase and time. A waveform
likelihood can therefore use the relative phase over a frequency
range, with coalescence time and phase as nuisance parameters. It
does not need to identify an estimated coalescence time with a
particular Fourier-mode arrival. The cosmological propagation-distance
factor and redshift conventions must be restored for the exact
published test; the displayed `D` is the campaign's linear-distance
approximation.

For a future explicit reconstruction, a usual stationary-Gaussian
frequency-domain likelihood would have the form

\[
 \log L=-\frac12\sum_I
 \langle d_I-h_I(\theta,\mu),d_I-h_I(\theta,\mu)\rangle_I+
 \text{constant},
\]

\[
 \langle a,b\rangle_I=4\operatorname{Re}\int
 \frac{a^*(f)b(f)}{S_I(f)}df,
\]

with source waveform, detector response, calibration, and glitch
treatment specified, and all required nuisance priors supplied.
This is a statement of the inputs needed for a reconstruction, not
an assertion that the complete original run configuration has been
recovered.

## Released data are not the dispersion likelihood

The same DCC release supplies a README, example notebook, and two
posterior archives for PhenomPNRT and SEOBNRT. The README and notebook
explicitly describe these as posterior samples from tests of the PN
coefficients in the **binary dynamics**. The notebook enumerates the
PN tests from `-1PN` through `3.5PN`; it does not identify a separate
massive-graviton/modified-dispersion posterior or likelihood file.

The primary paper's propagation paragraph does not provide a full run
configuration, all nuisance priors, or the separate dispersion samples.
Those were not located in this release. Consequently:

* The reported mass-bound value is usable as a published conditional
  result, with its response class stated.
* The released PN posterior must not be relabeled as a propagation
  posterior. Even an algebraically similar `f^-1` phase term requires
  a correct parameter mapping, Jacobian/prior treatment, distance
  dependence, and nuisance correlations before reuse.
* A posterior is itself not a raw likelihood; a reported upper bound
  cannot determine a Bayes factor or the likelihood of the campaign
  pole.

The paper discusses high-spin and tidal priors and two neutron-star
waveform models in its dynamics section, but the short dispersion
paragraph does not separately enumerate all its analysis settings.
This note does not silently identify those settings with the v3 raw
strain extraction, the older glitch-subtracted release, or an exact
new likelihood.

## Concrete next input

The higher-value next input is the actual modified-dispersion posterior
with its prior and run configuration, if available, or a separately
frozen phase-coherent likelihood using specified primary strain,
noise, calibration and source waveform inputs. Neither route requires
manufacturing individually significant peaks in three narrow bands.

Before treating this as a constraint on a proposed physical model, its
source and detector couplings must identify the observed waveform with
the selected pole and justify the waveform-generation assumptions.
For the finite scalar-bath construction alone, that identification has
not been established.

Raw files are retained under runtime
`gravity_measurements/waveform/dispersion_primary/`: `main.pdf`, its
text extraction and rendered page, the DCC landing HTML, README,
notebook, conversion script (not executed), `manifest.json`, and
`pole_comparison.json`. The exact primary PDF SHA256 is
`d86fc8bc15abdac47b75960218aefd247f7adeddc00237e9c329b492962584b7`.
