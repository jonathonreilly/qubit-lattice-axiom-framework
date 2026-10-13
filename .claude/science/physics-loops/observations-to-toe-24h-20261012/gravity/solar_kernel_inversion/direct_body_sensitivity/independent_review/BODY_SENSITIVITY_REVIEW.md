# Focused independent finite-body sensitivity review

No material mathematical or numerical correction was identified in the
current source. The equilibrium sensitivity, conditional Hessian response,
polytropic energy and radial identity, leading exchange/radiation channels,
and LLR mapping agree with independent derivations and calculations.
This conclusion is limited to the supplied weak-body EFT and observation
roles. It is not a formal audit, retained promotion, empirical acceptance,
compact-star result, or complete binary-radiation prediction.

## Source coverage and execution history

All 31 files in the delivered block were snapshotted exactly before review.
I read the full protocol, mathematical note, fixtures, current runner,
observation inputs, ledger, results/scope note, certificate, trace gate,
discovery/freeze metadata, both executions, and the complete one-line
contraction correction. The v1 source was read through its byte-exact diff
against the fully read v2 source; both complete snapshots were verified.
The complete result was parsed and all relevant numerical classes consumed.
No author file was edited and no author runner/helper was imported or run.

The note is SHA-256
`db13193ebc99b457ccf08444ba57d878a1e8281c20d38c3e7f055569d72d7b3d`.
The current runner is
`c6a6b277d499ebefb231ad54e330752341ea198de64b216041a7eccf78e1553c`;
the failed v1 runner is
`b6c1a5b041bcc6248a09c22aa3f47d2a5921be3a22ef4050780c4211a2c5ed57`.
The successful result is
`733c8a71984314bae266210a26894cd374f7a130155b8e64dd65c900c63011c8`.
All final sources and recovery snapshots are enumerated in the disposition
map and bound by the final receipt.

The first author execution failed in the scalar quadrupole contraction:
the subscripts specified two direction vectors but only one was passed.
Its source, stderr, empty stdout, exit status, and absent result are preserved.
The recorded diff adds precisely the missing second direction operand.
The second freeze differs only in that runner line; all other declared
input hashes match. The v2 execution succeeded with 2,818 recorded checks.
No tolerance, physical formula, fixture, or observation was changed to make
that run pass. I verified the full diff, chronology, and frozen/result hashes.

## Independent computation and numerical coverage

The independent runner completed its first execution in about 1.58 seconds.
All **4,095 checks passed**, with empty stderr. The exact executed reviewer
source and logs are preserved. It used different numerical routes:

- Boundary-value collocation with unknown first zero, rather than the
  author's Lane-Emden initial-value shooting, for all four polytropes.
- Composite Simpson integration with two grids, rather than adaptive
  quadrature, for mass/energy and the 48 radial controls.
- Exact scaling of fixed-baryon/EOS equilibria to check all 12 base bodies,
  72 shifted states, 36 finite-difference triples, and all body charges.
- Fourier derivatives of moments formed from the two actual source
  trajectories, followed by a 14-point spherical rule and transverse
  polarization components, to check all 18 binaries and 576 angular rows.
- Independent symbolic identities and exact rational LLR arithmetic.

All 2,818 author check records were parsed, their flags checked, and their
names checked for uniqueness. Numerical coverage did not rely on those
flags alone. The independent shape quantities differ from the author values
by at most about 3.13e-11 relatively; radial quantities by 3.75e-10.
The Fourier/sphere route agrees within 1.31e-8 relatively for nonzero
channels; its worst case is a small dipole formed by subtracting nearly
equal source charges. The independently recomputed channel sums agree
within 1.66e-13 relatively. These are observed comparison errors, not
rigorous truncation bounds or a certification of all future configurations.

The four n=1.0,1.5,2.0,2.5 shapes satisfy the expected finite-radius behavior,
and n=1 agrees with its analytic root and mass normalization. All frozen
radial trial numerators and denominators are positive. Their interpretation
as examples is kept separate from the general pulsation-energy proof.
The synthetic size and adiabatic ratios agree with the source. The mass-ratio
times radius/separation cubed estimate is below 1.26e-7 for these fixtures;
this is only a small-parameter check, not a calculation of tidal dynamics.

## Mathematical findings and scope

The physical-frame coefficient G_J=G_*A^2(1+a) requires converting both
energy and separation. The source does that consistently. The envelope
identity correctly differentiates equilibrium energy at fixed conserved
matter quantities and proper nongravitational parameters. It yields
s=-U_G/(M_Jc^2), not minus total binding energy divided by mass. The
polytropic distinction is a factor p=3/(3-n), and the controls reject
using total binding as a substitute.

The Hessian formula and signs are correct on the explicitly assumed smooth
stable constrained subspace with an inverse after symmetry modes are removed.
Positive radial pulsation energy does not establish that full Hessian
hypothesis on arbitrary nonradial directions. The note correctly separates
these assertions. Its mass denominator is exact inside a Newtonian energy
wrapper, not an all-orders relativistic resummation or scalarization proof.

The hydrostatic virial and enthalpy identities yield the stated potential
and internal energies. Fixed baryon mass/EOS produces the stated density,
radius and energy powers of G. The radial equation follows from the actual
mass-shell perturbation, and the stated boundary domain removes the
integration-by-parts term. For the supplied constant Gamma>4/3 the
numerator is positive for any nonzero admissible radial displacement.
No nonradial, nonlinear, relativistic, or arbitrary-EOS theorem follows.

The matched body covectors and K^-1 inner products produce the correct
exchange coefficient and barycentric dipole/quadrupole weights. Attraction
is separately assumed for a given pair. Tensor flux requires conserved
total matter plus interaction stress; particle kinetic stress alone would
be wrong. The actual G12 is used for the orbit and for the explicitly
defined same-orbit GR normalization.

Dipole and quadrupole interference vanishes by angular parity. The separate
leading powers and their channel ratio are correct, including the factor
5/96 in the general ratio and 5/24 in its leading sensitivity form. Equal
sensitivities remove the leading dipole, but equal nonzero sensitivities
do not recover the zero-sensitivity common coupling. This is a real
boundary on inheritance of the earlier radiation result.

The note's warning about order counting is necessary and sufficient here:
when a leading dipole is present, its next correction contributes at the
same formal c^-5 order as the displayed quadrupoles. That term was not
computed. Consequently the summed channels cannot be used as a complete
power through that order or as a precise pulsar/binary-period prediction.
The code and results retain this limitation; no circular synthetic fixture
is presented as an actual observed binary.

## Historical LLR source and readout

I checked the existing external primary PDF identity and viewed its pages
2 and 3, including Eqs. 3 and 5. The [Williams–Turyshev–Boggs paper](https://arxiv.org/pdf/gr-qc/0411113v2)
uses Earth minus Moon for both the self-energy coefficient and total EP
summary. The latter already includes the published solar-radiation-pressure
correction. Its SEP and eta summaries reuse that LLR fit together with a
laboratory composition result; they are not independent additional LLR
observations. The source correctly avoids importing the derived Cassini
beta estimate. No raw normal points, laboratory primary likelihood, or
ephemeris covariance were inspected by this reviewer.

The geophysical coefficient -4.45e-10 is a supplied body-model value,
not an output of these synthetic polytropes. The force derivation gives
Delta=-8.90e-10 f to the stated order, with the correct sign. The solar
sensitivity enters only at discarded products of weak sensitivities.
The four signed residuals and exact working intervals reproduce all output
rows: [0,3/11125] for one reported uncertainty and [0,1/2500] for two.
Those intersections are descriptive and not confidence levels.

The earlier interval was independently traced to the already reviewed
tensor/scalar note, hash
`fac07945fb9d7ab1341a3b93c6a2c67637764fe30345848a34a41846833deda3`.
Its exposed VLBA rectangle maps to the same 0<=f<=1/2500. This block
neither refits that interval nor treats the current LLR data as a blind
holdout. No prior repository theorem status is promoted by this check.

Allowing d_comp leaves a rank-one observation for two unknowns. Every f
can match the summary mean by shifting that nuisance. Universality and no
other macroscopic force are therefore substantive model premises, not
conclusions of the LLR agreement. In particular, the earlier charge EFT
does not establish macroscopic charge retention, neutrality, or absence of
electromagnetic forces. The note states that boundary explicitly.

## Failures, preservation, and final disposition

The original author contraction failure is preserved, not concealed by
the successful v2 result. The ledger also records an initial primary-fetch
certificate error and its ordinary-TLS curl resolution; it does not claim
an unavailable raw stderr artifact. This review created no new primary-PDF
copy in the source tree. A targeted reviewer lookup initially named a
nonexistent upstream observation JSON; the actual note and results/scope
file were then used to verify the unchanged interval. One combined source
display was truncated at the runner entrypoint; that entrypoint was reread
completely. No independent numerical execution failed.

There is no unresolved material correction from this focused review. The
source's pending-review wording is historical metadata left unchanged by
the reviewer. The exact 31-file disposition map, independent calculations,
full derivation, primary-source boundaries, and hashes are preserved here.
Parent remains the scientific author; assumptions about matter microphysics,
matching, realistic bodies, cosmological boundary conditions, and full
observational likelihoods remain open.
