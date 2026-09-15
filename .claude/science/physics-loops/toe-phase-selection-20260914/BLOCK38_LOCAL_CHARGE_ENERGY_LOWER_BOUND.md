# Block 38 — local temporal averaging gives an external-charge energy floor

Personal affirmative proof proposal,2026-09-15; independent review pending.
Same supplied finite-clock Villain model as PR8140/8144 and Blocks36-37.
Fixed finite N>=2,beta>0; integer charge profiles are interpreted mod N.

Let w(k)>0 be the one-link temporal Villain weight on Z_N, m=min w,M=max w,
and set delta=(m/M)^6, r=1-delta. Positive Fourier coefficients imply that w
is nonconstant at finite beta and N>=2, hence0<delta<1 and0<r<1. The exponent6
is the maximum spatial vertex degree in the cubic spatial lattice.

## 1. Conditional averaging at charged vertices

For finite spatial configurations a,b, the kernel of the charge-projected
convolution is, up to its common normalization,

 C_rho(a,b)=average_eta exp[-2pi i<rho,eta>/N]
                       product_e w(a_e-b_e+(d0 eta)_e).             (1)

Let v have rho_v nonzero mod N. Condition on all eta except eta_v. Its
conditional probability has N positive weights, each a product of d_v<=6
terms between m and M. Consequently each probability is at least
(m/M)^(d_v)/N>=delta/N. Write this conditional distribution as delta times
the uniform law plus(1-delta) times another probability law. The nontrivial
charge character averages to0 under the uniform component, so its conditional
absolute expectation is at most r. This is a strict finite-clock mixing
estimate, not a Gaussian approximation.

For a set A of charged vertices with no adjacent pair, their conditional
eta variables are independent after all other eta are fixed: no edge joins
two variables in A. The same estimate multiplies. Integrating the remaining
variables and dropping their phases in absolute value gives pointwise

 |C_rho(a,b)|<=r^|A| C_0(a,b).                          (2)

This does not say C_rho itself has nonnegative entries. It is an absolute
kernel bound against the neutral projected kernel.

## 2. Transfer operator and infinite reconstructed sector

Spatial V commutes with local gauge transformations. Put
T_rho=V^(1/2) C_rho V^(1/2)=P_rho T, where P_rho is the orthogonal gauge-charge
projection and T commutes with it. The neutral projected T_0 has an entrywise
positive kernel and its norm is the full Perron eigenvalue lambda0: the unique
positive Perron vector is gauge invariant. Equation(2) therefore implies

 ||T_rho||<=r^|A| lambda0.                              (3)

Indeed |T_rho x|<=r^|A| T_0|x|, and the L2 norm gives(3). On the rho sector,
T_rho agrees with T. Thus0<=tau|rho<=r^|A|I. This form bound passes through
all finite history Gram limits, yielding the full history-sector estimate

 H|rho>=|A|[-log(1-(m/M)^6)] I.                         (4)

Only the finite history representation reconstructed earlier is identified;
other infinite-volume representations are not covered. The estimate does
not depend on the spatial box. Boundary degrees below6 only improve delta.

For s charged vertices, the bipartition supplies an independent subset of
size at least ceil(s/2). A separated nonadjacent test-charge pair has an
independent subset of size2; an adjacent pair is covered by size1. Charge
aliases rho=0 mod N are excluded from the charged count and retain the neutral
vacuum at energy0. N=1 has no nontrivial charge sector and needs no bound.

## 3. Physical scope and compatibility

Combining with the static/full-history threshold equality gives a strictly
positive lower bound for each nonzero external charge profile. Under the
additional source curvature assumptions, the existing Coulomb-form upper
bound remains valid. This brackets an external-charge energy; it gives neither
an exact interaction force nor a propagating charged-particle mass.

The lower bound can be extremely small at weak lattice coupling and tends to0
in parameter limits; no continuum-uniform mass claim is made. It applies to
nonzero local Gauss charge. Neutral transverse field excitations belong to the
rho=0 sector, where this bound is0, so it does not assert a neutral photon gap.
The model still conserves each external charge profile and supplies no matter
hopping term. No axiom change, general no-go or physical-law selection follows.

## Decisive checks

Compare the explicit temporal group sum with independent electric-Fourier
charge blocks, test pointwise absolute domination and sector operator norms,
and enumerate the actual single-vertex conditional distributions. Include
nonadjacent pairs, multiple charges, neutral aliases and the trivial harmonic
as a control. Small matrices cannot certify the cofinal passage in(4).

Executed evidence:12charged/alias cases on N=2,3,4;29conditional single-vertex
distributions. Explicit gauge-projected kernels agree with independent Fourier
charge blocks; pointwise domination and spectral bounds pass. Neutral aliases
and the excluded trivial harmonic behave as required. The public follow-up
packages this result with the history construction; all science remains an
author proposal awaiting independent review.
