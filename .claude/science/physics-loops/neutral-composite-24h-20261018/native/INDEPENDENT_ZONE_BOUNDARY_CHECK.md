# Conditional zone-boundary band check

The half-line bound-state formulas and exact reflection selection check. The supplied finite projection source was inspected but its JSON was not yet present when first read; I have not replayed the expensive band extraction. Consequently the numerical K2 coefficients themselves are inputs to the half-line conclusions below, not independently derived all-length coefficients in this report.

## Odd-edge chain

With hopping t=1/4, bulk b=-1/2 and boundary diagonal+1/2, the boundary defect is v=1. The standard half-line recurrence yields r=t/v=1/4, energy b+v+t²/v=9/16, and normalized boundary probability Z=1-r²=15/16. It lies above the host band [-1,0] by 9/16 in the K2 coefficient units. For original leading source -2lambda E1, the corresponding leading weight is 4lambda² Z=15lambda²/4. The source normalization and sign are conditional on the root's native dressing; the minus sign has no effect on this squared weight.

## Even-edge chain plus d2

For a host of bulk diagonal -1/2 and hopping1/4, attach a side state of energy-2 to its endpoint with coupling-sqrt(2). A bound solution with host ratio r obeys E+2=2g00(E) and g00=r/t=4r. Hence r=(E+2)/8. Substitution into E+1/2=(r+r^-1)/4 gives

31E²+76E-36=0,
E=(-38±16sqrt(10))/31.

BOTH roots are admissible, not artifacts of squaring: their ratios (E+2)/8 have absolute value below1. Numerically the upper root is approximately .406 and the lower approximately -2.858, lying above and below [-1,0], respectively. Further dark sites at flat energy-2 are separate at this order under the supplied decoupling premise; the two side-host roots are not the entire dark-sector spectrum. Higher-order couplings can lift that flat degeneracy.

## Exact longitudinal reflection

Take R:j→-j with origin at a rung, and the explicit centered interval phase exp[iq(start+(ell-1)/2)]. Reflection sends the interval center to its negative. At q=pi the ratio is exp[-2pi i(start+(ell-1)/2)]=(-1)^(ell-1). Therefore E_ell has reflection parity(-1)^(ell-1), and all allowed even-length diagonal vectors have parity-1. This is independent of finite terminal-fold normalization; excluded terminal vectors remain absent.

The centered uniform-column O_pi=sum_j(-1)^j sum_a Z_(a,j-1)Z_(a,j+1) is reflection even. In a reflection-positive ground state it accesses only reflection-positive excited states. The even-edge/dark branch is therefore invisible to this readout exactly, as long as the full model and state retain the symmetry. This selection is not merely a K2 matrix-element zero. If the ground reflection character differs, the final character must be changed accordingly; a nonsymmetric state or differently phased/odd source need not obey the stated restriction.

The sign and source conclusions refer to a fixed lattice reflection center. Translating the reflection origin can alter the parity labeling at q=pi; transform the source and ground conventions together rather than mixing centers.

## Exact reason odd canonical orders vanish

There is also a direct all-order finite-band symmetry explanation for the observed K1=K3=0. Let Q be the product, over all rungs, of physical Z_(0,1) Z_(1,0). Each transverse X or Y bond intersects this checkerboard pair once, so Q flips the sign of the transverse perturbation and preserves the longitudinal unperturbed Hamiltonian. Thus Q H(lambda) Q=H(-lambda).

On the complete scalar E8 q=pi basis, Q gives (-1)^ell on an edge interval, because every native transverse edge anticommutes with its local factor. On a diagonal interval it gives+1. Consequently R=-Q throughout this chosen E8 space. A symmetry-equivariant canonical effective Hamiltonian commutes with R and transforms under Q by lambda→-lambda. Combining these facts makes it even in lambda: every odd coefficient vanishes, not just K1 and K3. This is a finite-band analytic/equivariant statement and does not prove an infinite-volume convergence radius. It assumes the same complete symmetry sector used in the explicit-basis proof.

## What remains conditional

The half-line K2 matrix elements and source dressing require an all-length local derivation or controlled extraction; testing finite matrices alone does not establish them everywhere. The odd-edge bound level has a gap within its leading effective reflection-positive host, but this is not automatically a stable native eigenstate separated from all sectors or multi-feature continua. Higher even orders shift energies and vertices. A volume-uniform band isolation, a full spectral gap at fixed coupling and physical detector/cosmological identification have not been derived here.

The exact reflection rule removes this particular even/dark readout, not the full neutral mode program. The q=pi odd branch is a lattice-zone-boundary feature, not evidence for a long-wavelength relativistic scalar. No observational claim is supported by these conditional spectra.
