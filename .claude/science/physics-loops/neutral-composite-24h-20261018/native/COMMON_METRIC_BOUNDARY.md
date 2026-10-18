# Native branch curvatures do not yet supply a common relativistic metric

Status: bounded-support; negative_route_pruning for simultaneous common-metric
identification of these branches in the stated weak-coupling regime. No
observational exclusion or all-regime impossibility claim.

The positive construction has produced several actual microscopic excitation
branches. This note tests a necessary compatibility condition before identifying
them with matter/scalars of a single relativistic vacuum. It does not impose
that condition as a selector that changes the Hamiltonian.

## Derived inputs, one native Hamiltonian and one coordinate system

Fix L=10, J>0 and the same weak lambda for every branch. The table uses the
excitation energy omega above the same chosen positive-plane global ground,
and D_i defined by omega_i(q_i+k)-omega_i(q_i)=D_i |k|²+smaller terms.

| Branch | Momentum minimum | Leading rest energy | Leading D_i |
|---|---|---|---|
| charged column | (0,0) | JDelta lambda4 | Jgamma lambda10 |
| neutral Q4 | (0,0) | JDelta lambda4 | Jkappa lambda12/2 |
| neutral Q8 | (0,0) | 2JDelta lambda4 | 5Jgamma² lambda14/(2D) |
| neutral Q6 | (pi,pi) | 3JDelta lambda4/2 | JK6 lambda18 |

Here Delta=5/8, gamma=12155/33554432, D=15/512,
v=90/32768, kappa=4gamma²/v,
and K6=8gamma d/Delta-16gamma²b/Delta²>0 with
b=15/4096 and d=1076510135/10567230160896.
The load-bearing derivations are
[CHARGED_COLUMN_POLE_PROOF.md](CHARGED_COLUMN_POLE_PROOF.md),
[POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md),
[ISOTROPIC_BOUND_FEATURE_PROOF.md](ISOTROPIC_BOUND_FEATURE_PROOF.md), and
[SIX_FLUX_DIAGONAL_MODE_PROOF.md](SIX_FLUX_DIAGONAL_MODE_PROOF.md).
All limits have fixed p with R asymptotic lambda^-p, sufficiently high final
reduction order, and resolved reciprocal-grid displacements. For all four at
once use p>4 so Q8's k<<lambda4 condition holds. Charged/Q4 alone already
suffices for incompatibility with p>1. This does not compare an uncontrolled
finite-grid derivative with a continuum derivative.

## Necessary test

Define the squared-energy increment coefficient C_i=2 omega_i(q_i)D_i.
Indeed omega_i(q_i+k)²-omega_i(q_i)²=2omega_i(q_i)D_i |k|²+O(D_i²|k|4)
with the inherited errors. For a common relativistic dispersion
omega_i²=m_i²+c²|k|²+o(|k|²), all C_i must agree, independent of masses.
This is only a necessary test. No branch has been shown relativistic over a
finite energy range merely because its rest-point Taylor expansion can be
written this way. C_i are not microscopic front velocities.

The actual derived leading coefficients are

 C_ch=2Delta gamma J²lambda14,
 C_4=Delta kappa J²lambda16,
 C_8=10Delta gamma² J²lambda18/D,
 C_6=3Delta K6 J²lambda22.

Their ratios to the charged branch are

 C_4/C_ch=[kappa/(2gamma)]lambda²[1+o(1)],
 C_8/C_ch=[5gamma/D]lambda4[1+o(1)],
 C_6/C_ch=[3K6/(2gamma)]lambda8[1+o(1)].

Every prefactor is finite and positive. All three ratios tend to zero,
rather than one. The displayed remainder estimates allow the comparison on
a common sequence of actual grids; choose p=5 and final M sufficiently large
(for example M=70, larger than the requirements of all four blocks).
Thus these four branches cannot simultaneously have the common relativistic
rest-point dispersion in this weak-coupling regime. Rest-energy hierarchy
alone does not repair this kinetic mismatch.

## Reparameterizations do not remove the test

A common time rescaling multiplies all omega by the same factor and a common
length rescaling multiplies all reciprocal-coordinate coefficients by the
same factor. C_i themselves are dimensionful and transform; their ratios
are invariant. J rescaling cancels from the ratios, including a common
lambda-dependent change of units. Multiplying or canonically normalizing a
source changes residues, not pole positions. A momentum shift to the Q6
minimum changes the expansion origin, not the slope. Species-dependent clocks
or length standards would abandon the proposed common metric and are not a
derivation. A common momentum-dependent change of coordinates likewise has
one common Jacobian at the corresponding envelope momenta; assigning distinct
Jacobians to different species/minima is an additional embedding assumption.

## Relation to current repository work and scope

PR9718 was refreshed at head 965c6f3dbd6d2023d4227886143e78a80861a1e6. Its
body reports conditional curvature-constraint closure requiring a common
matter cone, while supplying the matter systems. That report motivates this
compatibility test but is not a proof input here: the necessary dispersion
condition above follows directly from the displayed common-metric ansatz.
No closure theorem or graviton kernel from that PR is imported as native.

This prunes identifying all the present native branches with a common
relativistic vacuum by normalization alone. Ordinary composite quasiparticles
in a medium can have different effective inertial masses; that is not a
contradiction. There is no claim that every neutral excitation must represent
an observed elementary scalar, nor that Lorentz symmetry cannot emerge in a
different phase or scaling regime of the Hamiltonian. No observed speeds,
units, masses or fitted parameters were used. In particular this is not an
experimental falsification without a physical identification map.

Next constructive targets are an actual collective critical regime with a
shared dispersion, a derivation of how only a suitable subset becomes physical
matter, or a native mechanism equalizing kinetics. Adding independent speed
coefficients to force equality would supply the missing connection.


## Height choice and the newly derived secondary molecule

For every fixed even L>=10 in the same strong-column construction, write
Delta_L=L/16, gamma_L=binom(2L-2,L-1)/8^(L-1), and v_L=9L/32768.
The charged-column and Q4 lower-pole leading rest energies are both
JDelta_L lambda4, while their quadratic momentum coefficients are
Jgamma_L lambdaL and 2Jgamma_L²/v_L lambda^(2L-8). Thus their squared-energy
curvature ratio is

 C_Q4/C_charged=(2gamma_L/v_L)lambda^(L-8)[1+o(1)].

It vanishes at every fixed even L>=10. This is a fixed-height conclusion;
no uniform growing-L continuation is presumed. Equalizing the powers would
suggest L=8, but at that height the native endpoint attraction/hopping ratio
is v_8/(2gamma_8)=96/143<1. The particular lower endpoint bound mode therefore
does not exist by this mechanism there. Picking height eight does not repair
this family by retaining its bound-mode formula outside its binding regime.
This does not exclude another mode or phase at height eight.

There is a further mismatch entirely within the now checked L10 neutral
families. The secondary axis-three molecule has rest energy 2JDelta lambda4
and curvature (5/2)Jgamma²/v lambda12, while the Q4 mode has rest energy
JDelta lambda4 and curvature 2Jgamma²/v lambda12. Hence

 C_secondary/C_Q4 -> 5/2.

Even their equal lambda powers do not give a common relativistic slope.
Common units or source normalization leave this ratio unchanged. These remain
conditional model identification tests, not a claim that ordinary bound states
in a medium must obey vacuum relativistic dispersion. The missing mechanism
is a common physical kinetic structure, not another freely chosen scalar
normalization.
