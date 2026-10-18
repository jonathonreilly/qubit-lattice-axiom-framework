# Native charged-pair collision operator

Status: conditional-support. Trace: upstream_support. Proposal allowed: false.
The Hamiltonian and fixed height L=10 remain conditional premises. All data here
are exposed model development. No observation is fitted or independently tested.
This derives an interaction operator from existing bonds; it does not add one.

## Scope and prior inputs

Use the unchanged periodic column Hamiltonian and the globally positive-plane
ground existence from this campaign. The charged column has hopping
-J gamma lambda^10, gamma=12155/33554432. The complete Q8/perimeter16 shape
classification and order-eight energies are in
[SECONDARY_NEUTRAL_MOLECULE_PROOF.md](SECONDARY_NEUTRAL_MOLECULE_PROOF.md).
The local fixed-defect normal forms and connected vacuum subtraction are in
[POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md).

Work in the even relative channel at total transverse momentum zero. It is
convenient first to write the operator on ordered relative coordinates r; the
physical identical-column states are its r->-r even subspace. No fermionic
statistics or physical cross-section convention is inferred from this notation.
Subtract the energy of two far charged columns and their kinetic band bottom.

## Complete order-ten diagonal interaction

A connected diagonal insertion graph contributing to the interaction of two
columns must depend on both background signs. At an affected endpoint the
Y-degree is odd, and diagonal return makes the X-degree odd also. At separation
(3,2), a connected ten-edge Euler tour visiting both endpoints splits into two
paths of length at least five. Equality forces two monotone shortest paths.
Enumerating their distinct multigraphs gives exactly six simple ten-cycles,
two touching six-plus-four cycles and one dumbbell of two squares joined by
a doubled edge. Twelve path-pair descriptions represent only nine graphs;
counting descriptions would overcount.

Every simple cycle lies in one longitudinal layer. For touching cycles, their
layers differ by 0 or +/-1. For the dumbbell both bridge occurrences occupy the
same layer; that layer differs by at most one from each square. Fixing the first
square at zero gives nine layer assignments, including second-square height
+/-2. Other layer separations have exactly disconnected folded energy zero.
The height-ten circle causes no alias of these assignments.

The primitive-cycle formula from [PRIMITIVE_LOOP_INTERACTION_PROOF.md](PRIMITIVE_LOOP_INTERACTION_PROOF.md)
gives the six simple contributions: one -143/33554432, four +55/33554432,
one -35/33554432. A connected Rayleigh recurrence including all proper energy
folds gives each touching graph the layer sum 331/226492416. The dumbbell sum
is -75101/97844723712. Its two labeled identical bridge insertions require a
factor 1/2!, applied to the complete coefficient including folds.

`neutral_order10_pair_control.py` computes the full rational recurrence;
independent Feshbach expansion agrees in every tested layer assignment.
A reversed endpoint changes the sign of each relevant graph, so the two-column
contrast E_AB-E_A-E_B+E_0 is four times its reference coefficient. Summing the
first layer gives L. Thus

    V_(3,2) = JL lambda^10 * 333355/24461180928 + O(J lambda^12).

At (4,1), the only shortest closed graph with the required endpoint turns is
the 4-by-1 rectangle. At (4,0), the graph needs a transverse excursion to make
both endpoints turns: the two unit-width 4-by-1 rectangles are the only
minimal graphs. Hence

    V_(4,1) = -143 JL lambda^10/8388608 + O(J lambda^12),
    V_(4,0) = -143 JL lambda^10/4194304 + O(J lambda^12).

All further allowed separations need more than ten insertions for a connected
sign-dependent graph. This is a diagonal coefficient statement; native
height-ten winding enters at the same order as offdiagonal hopping and is
included separately below. It is not permissible to discard winding.

## The native continuum channel

Other Q sectors differ at order lambda^4, and other Q8 perimeters at order
lambda^6. Within perimeter16, axis-three and (3,1) pairs lie below the far
continuum at order lambda^8; (2,2), the infinite odd-rod family and T shapes
lie above it at that order. Their gaps are uniform in the classified shapes.
After eliminating these channels, the remaining relative domain is

    D = Z^2 \ F,
    F = {r: |rx|+|ry| <= 4} \ {(4,0),(-4,0),(0,4),(0,-4)}.

There are 37 excluded sites. This excludes both attractive and repulsive
shifted channels: it does not claim the lower molecules disappeared.
The two ways to move one endpoint give hopping t=2 gamma at center momentum
zero. In units J lambda^10 the leading operator is

    K = t(4 - adjacency_D) + U.

The only nonzero U, including rotations/reflections, are

    U40/t = -8/17,   U41/t = -4/17,   U32/t = 30305/161109.

There are twenty potential sites. The constant 4t fixes the far continuum
threshold at zero. Nearest-column winding is the entire leading offdiagonal
operator in this channel. A winding move to a rod or removed pair shape leaves
this channel and first returns at order lambda^12, owing to its lambda^8 gap.
No arbitrary boundary potential or contact coupling has been supplied.

## Positivity and threshold behavior

Let K_D=t(4-adjacency_D). Its form is t times the sum of internal edge
differences squared plus t times the missing-neighbor count at each boundary
site. Those counts are one at40, one at41 and two at32. The negative U uses
at most 8/17 of that boundary term, while U32 is positive. Therefore

    K >= (9/17) K_D >= 0.

There is no negative-energy bound state in THIS far-channel leading operator;
this does not exclude the lower native molecules already integrated out.
There is also no nonzero bounded zero-energy solution. Multiply such a
solution by a cutoff whose transition is logarithmic over a large annulus.
The localization error is bounded by its squared sup norm times the cutoff
Dirichlet energy, which tends to zero in two dimensions. Coercivity forces
every fixed edge difference and boundary value to vanish. D is connected and
has absorbing boundary, so the solution is zero. Logarithmically growing
zero-energy scattering solutions are not excluded.

With Fourier measure d²k/(2pi)², the full-plane symbol is
 t(4-2cos kx-2cos ky)=t|k|²+O(|k|^4).
The finite-support outgoing free resolvent has common singular part
 -(log(t/E)+i pi)/(4pi t).
Finite-rank elimination of the obstacle and U therefore gives the ordered
relative monopole amplitude

    T(E;k',k) = 4pi t/[log(t/E)+4pi B+i pi+o(1)]

as on-shell k,k' tend to zero, with the outgoing convention
T=V+V(E+i0-H)^(-1)V. In particular the leading coefficient is 4pi t.
The logarithmic threshold law is standard two-dimensional scattering
structure, not a novelty claim. The model-specific derivation here is D,U
and their native coefficient, followed by the threshold-exception exclusion.
For discrete resolvent context see
[Komech, Kopylova and Vainberg](https://www.mat.univie.ac.at/~komech/articles/KKV07.pdf).
The normalization is not a symmetrized boson rate or a measured cross section.

## A derived dimensionless scattering scale

An exact finite-integral definition avoids fitting a contact coupling. Put
t=1 temporarily. On S=F union support(U), define W^-1 to be zero on F and
1/(U/t) on the twenty potential sites. For epsilon>0 the free positive Green
matrix is G_epsilon=(epsilon+4-adjacency)^(-1) restricted to S. Then the
Euclidean zero-external-momentum amplitude is

    T(-t epsilon;0,0)/t = 1^T [W^-1+G_epsilon]^-1 1.

The hard obstacle is the infinite positive onsite-potential limit, not an
additional native interaction. It represents the removed gapped shapes.
Writing G_epsilon=log(1/epsilon)11^T/(4pi)+C+o(1), the exact matrix entries are

    C_rs = log(32)/(4pi) - a(r-s),
    a(x,y) = integral_0^pi [1-cos(kx) exp(-|y| eta(k))]
                         /[pi sqrt(delta(k)(4+delta(k)))] dk,
    delta(k)=4 sin²(k/2), eta(k)=2 asinh(sin(k/2)).

The finite constant B is defined by the augmented system

    (W^-1+C)v = B 1,       1^T v=1.

The zero-resonance exclusion ensures the corresponding scattering solution
is unique. This formulation does not require W^-1+C alone to be invertible.
The numeric control uses stable endpoint subtraction, checks a(1,0)=1/4
and a(1,1)=1/pi, and compares this system with six finite-epsilon inversions.
It obtains

    B approximately -0.150856109238,
    epsilon_* = exp(4pi B) approximately 0.150211079390.

These decimals are numerical evaluations of the specified coefficient-model
integrals, not interval-certified digits or observed constants. The energy
scale in this limiting channel is J lambda^10 t epsilon_*. The externally
chosen J,lambda and lattice units have not themselves been derived.

## Microscopic transfer and its limit

At any fixed finite transverse torus larger than the support above, the
existing local normal forms, followed by the shape-gap elimination, give a
matched block after common scalar subtraction:

    H_eff/(J lambda^10) = K_R + B_lambda,R,
    ||B_lambda,R|| <= C lambda² + C R² lambda^(M-10).

Here the first C is volume independent in the fixed-Q sector: connected local
terms minus their vacuum value must meet a bad plaquette, and Q=8 is fixed.
A local winding changes the shape only near those defects. The lambda^8 shape
gap makes its eliminated mixing O(lambda²) and its feedback O(lambda^12).
All retained degrees are even by the transverse checkerboard transformation;
height ten makes that transformation trivial on the unperturbed column space.
These facts justify the next degree twelve rather than an assumed lambda11.
The arbitrary fixed-order remainder M includes the prior reductions' losses;
M can be chosen before taking the polynomial-volume limit. Exact N/plane
embedding and matched state preparation remain part of this comparison.

Duhamel bounds evolution error at scaled time tau by
 |tau|[C lambda²+C R² lambda^(M-10)], plus initial embedding error.
This transfers fixed-time collision dynamics and permits growing times
 o(lambda^-2), with adequate M. For example R~lambda^(-2/3) and
 tau~lambda^-1 give errors O(lambda)+O(lambda^(M-37/3)), apart from matching
errors O(lambda²). This is an evolution bound, NOT by itself an extracted
on-shell scattering amplitude or a boundary-return estimate.

The logarithmic T above is a theorem of the leading coefficient operator.
A fixed-lambda microscopic infinite-time S-matrix, full inelastic channels,
physical detector normalization, and uniform extraction of arbitrarily small
energies remain open. First-grid energies on R~lambda^-p with p>1 cannot be
transferred using only this O(lambda²) scaled remainder. No universal gravity,
common relativistic cone, or empirical scalar identification follows here.

## Controlled finite collision in the microscopic model

The preceding limitation can be partly overcome by specifying a collision
experiment in the matched Hilbert space rather than taking an unjustified
fixed-lambda infinite-time limit. The construction below uses no physical
interaction beyond H. Packet preparation and the dressed readout are explicitly
specified operations; they are not claimed to be cosmological initial states
or a laboratory detector that has already been built.

First work in the limiting coefficient model. Extend K from D to the full
relative lattice by a decoupled core energy kappa>8t on F. Its difference V
from K0 is bounded and supported on a fixed finite set of sites and bonds.
This extension changes neither scattering in D nor the hard-obstacle condition.
Take an inversion-even, radial smooth Fourier packet

    f_k(p)=k^-1 phi(p/k),   support(phi) subset {1<|u|<3/2},

normalized in the lattice Fourier measure. For small k it is supported inside
the Brillouin zone. Near the finite interaction support, nonstationary phase
in u gives, for every fixed N,

    ||V exp(-i s K0) f_k|| <= C_N k (1+k² |s|)^(-N).

The phase gradient on the annulus is bounded below after division by k²;
fixed spatial offsets in V do not change this estimate for |s|k² large.
Cook's tail beyond T is therefore at most
 C_N k^-1 (Tk²)^(1-N).
The same estimate holds for the outgoing packet S f_k: its scaled Fourier
profile has uniformly bounded fixed-order derivatives. To see this, use the
finite-support resolvent matrix. Its only threshold singularity is the rank-one
logarithm; the complementary finite matrix has no threshold kernel by the
bounded-resonance argument. After p=ku, energy derivatives of the logarithm
are accompanied by k², and angular derivatives of the finite-support plane
waves have additional k factors. The smooth energy-shell density stays bounded
in two dimensions. Thus the outgoing profile remains in a fixed annulus with
uniform scaled Sobolev bounds. This does not assume smoothness of a generic
unknown microscopic S-matrix.

More explicitly, the derivative assertion does not differentiate a scalar
o(1). For each of the finitely many Green-function displacements, split the
Fourier integral near the quadratic minimum from its smooth complement. The
analytic Morse coordinate near that minimum makes the denominator radial;
angular integration of the analytic numerator gives a power series in the
radial energy. Integrating its first finitely many terms gives the logarithm,
a regular matrix, and an O(E log E) remainder with the same bound under any
fixed number of E d/dE derivatives. Boundary values retain the specified
imaginary constant. The smooth complement is differentiable to every needed
fixed order because its denominator stays away from zero.

Let e be the all-ones vector on the finite support and Q its orthogonal
complement. Put A=W^-1+C at zero energy. Q A Q is invertible on Q. Otherwise
there is nonzero v with e^T v=0 and A v=b e. The function
 psi(r)=b-sum_s C(r-s)v_s
is bounded at infinity (the logarithmic terms cancel), vanishes on the core,
and satisfies K psi=0 on D with U psi=v on potential sites. If it vanished
identically, its extension and lattice equation would force v=0, a
contradiction. Thus it would be precisely the bounded zero solution already
excluded. This proves the required regular-complement condition, rather than
assuming it from the scalar T limit.

Schur inversion with this regular complement leaves the one denominator
 log(1/E)/(4pi)+B+i/4+O(E log E).
Its inverse and every fixed scaled energy derivative are bounded; the other
blocks are bounded as well. Substituting E=k² rho, with rho in a compact
positive interval, gives uniform rho-derivative bounds. The energy-shell
formula for S contains delta(omega(p')-omega(p)); after p=ku its k^-2 factor
cancels the momentum-measure k² factor. The scaled shell is smooth and stays
away from zero, so the outgoing scaled profile has the claimed uniform
finite-order derivatives. This establishes the two-sided Cook estimate.

Choose T=k^-3 and N=5. The two-sided finite collision operator

    S_T = exp(i T K0) exp(-2i T K_extended) exp(i T K0)

then satisfies ||(S_T-S)f_k||=O(k³). The decoupled core component of the
incoming packet is included in this bound, rather than silently projected away.

Now put k=lambda^(1/4), take an even torus R asymptotic to lambda^-1, and
periodize the incoming packet. A finite-range single-particle propagation bound
makes finite/infinite-volume differences negligible: R/T tends to infinity,
while initial periodization tails are arbitrarily small powers of kR because
phi is smooth. Free and interacting hopping ranges and norms are fixed in
these scaled units. This is a relative-coordinate bound; it is not a claim
about the microscopic Lieb-Robinson velocity at the much longer physical time.
The microscopic comparison instead uses the already derived block bound.

Prepare the dressed native state corresponding to exp(i T K0)f_k in the
zero-center-momentum, inversion-even pair channel. Evolve for physical time
 2T/(J lambda^10), and compare with the matched outgoing free-channel readout.
Consistent removal of the common scalar phase is understood. Duhamel and the
normal-form embedding give

    error <= C lambda^(5/4) + C lambda^(M-51/4)
             + O(lambda^(3/4)) + periodization tails,

where the first two terms are microscopic evolution errors, the third is the
finite collision/Cook tail, and M is chosen, for example, >=20. Any preparation
or readout error must be added; the displayed statement is for matched dressed
states and operators. Bare product preparation is not substituted for them.

Finally, the low-energy angular density is dE/(4pi t) times dtheta/(2pi).
On the normalized angular monopole, the leading scattering eigenvalue is

    s0(E) = 1-i T(E)/(2t)
          = [L(E)-i pi]/[L(E)+i pi] + o(1/log(t/E)),
    L(E)=log(t/E)+4pi B.

The radial packet is in this monopole to leading order; lattice angular
corrections vanish as k->0. Therefore

    ||(S-I)f_k|| ~ 2pi/log(1/k²)
                ~ 4pi/log(1/lambda).

All displayed evolution errors are smaller than this signal. This gives a
nonzero, controlled asymptotic finite-collision signal for the dressed physical
two-column channel, with the same one-qubit Hamiltonian. The inversion-even
packet fixes normalization without guessing a factor from distinguishable
particle cross sections. The order of limits and growing observation time are
part of the result. It remains different from a fixed-lambda infinite-time
microscopic scattering theorem, a full many-body effective field theory, a
fermionic matter sector, a relativistic scalar, or an empirical force law.

## Finite-k diagnostic (not a threshold certification)

The sparse propagation control `neutral_pair_collision_packet.py` uses K/t,
k=.25,.20,.15 and torus sizes192,256,512 with time k^-3. Norm conservation
errors stay below3e-12. The difference from the leading threshold phase is
1.128,.851,.507, and initial core weights are .055,.029,.0093. These are
not yet the asymptotic regime; the numbers do not validate a small threshold
error at these k. The decreasing discrepancy is only a finite coefficient-model
diagnostic. The analytic limit, not an extrapolation from these three points,
supports the finite-collision theorem. No full microscopic spin evolution was
numerically simulated by this control.
