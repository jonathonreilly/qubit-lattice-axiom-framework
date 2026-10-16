# Laboratory calibration and Green normalization

This block reconstructs a published apparatus model and checks its normalization.
It does not fit the scalar theory to the 95 processed torque rows. The pinned
inputs are exposed development material. The source is John G. Lee's 2020
[thesis](https://digital.lib.washington.edu/researchworks/bitstreams/6013936a-da00-42b7-ba0a-4dff0cb05bf8/download),
Chapters 2 and 8, especially printed pages 11–13, 87 and 95. This is standard
Newtonian/Yukawa support mathematics, not a new theory or a claimed new method.

## 1. Start from force, with physical units

Use `G_N` for the coupling in a supplied Newtonian reference calculation, keeping
it distinct from the scalar tensor coefficient `G_T`. Let three equal inner
spheres of mass `m` have centres

`x_j = (r cos(2 pi j/3), r sin(2 pi j/3), 0)`.

Let three equal outer spheres of mass `M` have centres

`y_i = (dx + R cos(phi+2 pi i/3), dy + R sin(phi+2 pi i/3), z)`.

Newton's exterior theorem gives an exact point representation for disjoint
spherically symmetric bodies. Applying it to the actual calibration apparatus
still requires that body model and the treatment of other components. The
torque about the inner centre is

`N(phi) = G_N m M sum_ij (x_j cross y_i)_z / |y_i-x_j|^3`.                (1)

For centred axes `dx=dy=0`, grouping the nine pairs by angle difference gives

`N(phi)=3 G_N m M r R sum_i sin(phi+2 pi i/3)`
`             /[r^2+R^2+z^2-2rR cos(phi+2 pi i/3)]^(3/2)`.             (2)

This is the source's Eq.8.4. It has torque units `kg m^2 s^-2`. At centred axes,
the interaction energy is `U=-G_N m M sum_ij 1/|y_i-x_j|`, and the torque on
the inner pattern equals `+dU/dphi`; the outer pattern feels its opposite.
With radial offset, rotating only the inner pattern differentiates (1); do not
differentiate the outer phase and assume those torques remain opposite about
different centres.

For a real periodic record define `c_n=(1/(2pi)) integral N exp(-in phi) dphi`.
The real harmonic amplitude is `2|c_n|`. A sine coefficient is `-2 Im(c_n)`.
The factor of two must not be lost by mixing complex and real amplitudes.

At `z=0` and `q=r/R<1`, the Legendre expansion of the pair potential gives
the leading third-harmonic amplitude

`A_3 = (135/8) G_N m M r^3/R^4 + O(G_N m M r^5/R^6)`.                 (3)

Indeed the coefficient of `cos(3phi)` in `P_3(cos phi)` is `5/8`; summing
the three outer phases and three inner spheres supplies nine, and differentiating
supplies three. The exact numerical calculation uses (1) or (2), not this
small-radius truncation.

The coefficient `A_3/G_N` inferred from geometry can be compared with the source's
*calculated* nominal `N_cal`. Thus `G_consistency=N_cal/(A_3/G_N)` checks its
input convention. It is not a measurement of G: the target `N_cal` was itself
calculated using a supplied G. The literal printed positive exponent and an
explicitly labeled negative-exponent candidate are both retained. No numerical
input is silently repaired. Centering corrections and single-parameter
sensitivities are compared to the source as diagnostics, with discrepancies
preserved rather than turned into fit parameters or widened uncertainties.

## 2. Normalize the finite-source kernel independently

For `mu>=0`, define the point kernel `g_mu=e^(-mu d)/d` with
`(Delta-mu^2)g_mu=-4pi delta_3`. Its cylindrical expansion is

`g_mu = sum_{n in Z} exp[in(theta-theta')] integral_0^infinity dk`
`       [k/q] J_n(kr) J_n(kr') exp[-q |z-z'|], q=sqrt(k^2+mu^2)`.      (4)

The vertical derivative jump of `exp(-q|z|)/q` is `-2`; angular completeness
contributes `2pi`, and radial completeness gives `delta(r-r')/r`. This fixes
the `-4pi` source and the overall coefficient. In particular, at `r=r'=0`
and positive axial gap `d`, the remaining integral is exactly `exp(-mu d)/d`.

For two disjoint distributions with ordinary mass densities, each cross pair
counted once, the physical reference energy is

`U_mu = -G_N integral rho_A(x) rho_B(y) g_mu(x,y) d^3x d^3y`.           (5)

There is no additional `1/(4pi)` in (5). Such a coefficient belongs to a Green
function normalized to `-delta_3`, not to the kernel in (4). The thesis's printed
Chapter 2 expressions must be reconciled with their source/density convention
before reuse; copying a prefactor is not sufficient. No statement about the
experiment's actual executable normalization follows just from its printed
notation. Equation (2) and the point limit provide separate normalization checks.

## 3. Finite coaxial wedge pattern

Take two patterns of N non-overlapping angular wedges with half-widths beta_A
and beta_B, constant densities rho_A/rho_B, radial supports [a_i,b_i], and
thicknesses t_A,t_B. Put A at `z in [-t_A,0]`, B at `z in [d,d+t_B]`, `d>0`.
They share an axis and their patterns differ by angle phi. Finite thickness,
geometry, uniform density/contrast and common axis are declared model inputs.

The angular integral for `n=N*l`, `l` a positive integer, is

`S_i(n)=2 N sin(n beta_i)/n`; otherwise it vanishes.

Define `R_i(n,k)=integral_{a_i}^{b_i} r J_n(kr) dr`. The coefficient of
`cos(n phi)` in the pair energy is

`U_n = -8 G_N rho_A rho_B sin(n beta_A) sin(n beta_B)/l^2`
`      * integral_0^infinity dk k exp(-q d)`
`        *(1-exp(-q t_A))*(1-exp(-q t_B))*R_A(n,k)*R_B(n,k)/q^3`.       (6)

Two equal positive/negative Fourier orders produce the leading factor two.
The vertical volume integrals produce the two factors `(1-exp(-qt))/q`.
The torque's real harmonic amplitude is `n|U_n|`. At fixed density the energy
has units `G rho_A rho_B length^5`, which are energy units. A removed wedge
uses a signed density contrast; absolute physical source masses and total
variation bounds cannot be replaced by its signed net mass.

This derivation does not make the actual apparatus exactly coaxial. Per-run
positions, tilt, coating offsets, density/metrology, complex phase reductions,
transfer corrections and their covariance remain necessary for a faithful
reference fit. The printed off-axis functions are fitted approximations and
will not be adopted as exact equations.

## 4. Checks and surviving assumptions

The frozen computation plan calls for direct pair force/energy derivatives,
adaptive angular quadrature and converging FFTs, a point-source Green limit,
angular-space/Bessel-space point harmonics, and a complete synthetic finite
wedge volume comparison. A deliberately inserted `1/(4pi)` and a missing
real-amplitude factor provide normalization mutations. Numerical agreement is
a floating diagnostic, not an interval-certified integral or experimental test.

The physical scalar prediction would use `G_T` and a separately derived source
charge, environmental response and calibration response. Treating `G_N=G_T`,
setting calibration leakage to zero, or naming a laboratory background a vacuum
would supply assumptions that this block has not derived. No scalar potential,
initial state, environmental profile or physical absolute scale is selected.
