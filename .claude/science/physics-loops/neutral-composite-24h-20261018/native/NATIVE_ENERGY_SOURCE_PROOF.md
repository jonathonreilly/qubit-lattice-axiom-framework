# Native bond-energy readout of the neutral Q4 mode

Status: conditional-support. Trace: upstream_support to native scalar coupling.
No retained proposal. The Hamiltonian, fixed L=10 slab, anisotropy and units
remain premises. This block adds no interaction.

## Definition and exact conservation check

For H=sum_b h_b=-J sum(ZZ_z+lambda XX_x+lambda YY_y), define the existing
bond-center energy density

 E_q=V^(-1/2) sum_b exp[-i q.center(b)] h_b, V=LR², q_z=0.

This is the particular microscopic density being evaluated. E_q dagger=E_-q.
Bond centers across periodic boundaries are assigned by a consistent unwrapped
local convention; allowed reciprocal momenta make period shifts harmless.
At q=0, E_0=H/sqrt(V), so its transition from any ground state to a different
energy eigenstate is exactly zero. Also

 [H,E_q]=(2sqrt(V))^(-1)sum_(a,b)(f_b-f_a)[h_a,h_b].

Only overlapping perpendicular Pauli bonds contribute. This is an exact
microscopic energy-continuity identity, not a phenomenological field equation.
It provides a zero-momentum sign/normalization check; conservation alone would
not fix the nonzero-momentum coefficient.

Different local density improvements with the same total H can change the
nonzero-q form factor. The bond-center convention is explicit, not a unique
stress-energy or gravitational coupling derived by definition.

## Native marked coefficients

Use the existing whole-column and Q4 pole reductions in
[COLUMN_READOUT_PROOF.md](COLUMN_READOUT_PROOF.md),
[TEN_LAYER_NEUTRAL_BOUND_PROOF.md](TEN_LAYER_NEUTRAL_BOUND_PROOF.md),
[POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md),
and [ISOTROPIC_BOUND_FEATURE_PROOF.md](ISOTROPIC_BOUND_FEATURE_PROOF.md).
The actual reference global ground is provided by
[REFLECTION_GROUND_SECTOR_PROOF.md](REFLECTION_GROUND_SECTOR_PROOF.md).

Insert E_q by differentiating native bond coefficients with their Fourier
marks. For complex modes first differentiate real sine/cosine marks and then
combine. This is an algebraic source calculation, not a new dynamical term.

Write c_x=cos(qx/2), c_y=cos(qy/2). For the fourth-order elementary square,
the four transverse numerator bonds contribute 2c_x+2c_y relative to its
center. The three inverse denominators have total uniform derivative -3.
The fully summed physical-square coefficient has equal vertex weights by
symmetry, each -3/4 of that coefficient. The vertex Fourier sum is 4c_x c_y.
Thus the marked plaquette energy kernel is

 F4(q)=2c_x+2c_y-3c_x c_y.

This equality is for the complete sum of ordered paths, not an assumption of
equal vertex weights in each individual path. The exact rational control
checks all sixteen reference spin patterns and all twenty-four orders.

For the first horizontal winding coefficient, all L transverse numerator
bonds have the same midpoint. Each denominator lies on the two participating
columns; the summed logarithmic derivative -(L-1) divides equally between
them. Hence

 Fx(q)=L-(L-1)c_x, Fy(q)=L-(L-1)c_y.

F4(0)=Fx(0)=Fy(0)=1, consistent with the degree-one homogeneity of all native
energy coefficients under a common rescaling of J.

## Ground rotation fixes the coupling

Let t=Jgamma lambda^L, gamma=binomial(2L-2,L-1)/8^(L-1), and
Delta=L/16. The leading adjacent-column pair energy is JDelta lambda4.
The x-pair's four bad plaquettes lie at offsets (+/-1,+/-1/2) from its
center. Its diagonal energy insertion is therefore
JDelta lambda4 F4(q) cos(qx)c_y. The ground's virtual pair amplitude is
t/(JDelta lambda4). Combining this with the direct winding insertion gives

 A_x(q)=t/sqrt(L)[F4(q)cos(qx)c_y-Fx(q)],
 A_y(q)=t/sqrt(L)[F4(q)c_x cos(qy)-Fy(q)].

The Bloch sum contributes R and the physical normalization R sqrt(L), leaving
1/sqrt(L). Initial and final state mixing give the pair-vacuum diagonal
contrast, not two copies of it. At q=0 the two terms cancel exactly.

A canonical high-wall source connection within N0 has no diagonal part for
real perturbations (it is real antisymmetric). A nontrivial column change
requires at least L physical insertions. Its commutator with the nonconstant
column Hamiltonian begins at lambda^(L+4), too late to change this leading
coefficient. Later flux/shape transformations must transform states and
source together; the displayed formula instead uses the explicit ground
rotation in the original column basis.

Expanding the exact kernels,

 F4(q)=1+(qx²+qy²)/8+O(|q|4),
 F4(q)cos(qx)c_y-Fx(q)=-(L+2)qx²/8+O(|q|4),

and similarly for y. The lower Q4 orientation mode is (A+B)/sqrt(2) for
|q|<<lambda, so its energy-density matrix element is

 A_low(q)=-Jgamma(L+2)/(8sqrt(2L)) lambda^L |q|²
 +O(Jlambda^(L+2)|q|²+Jlambda^(L-2)|q|4)
 +O(JR³lambda^(M-14)).

The second error includes the lower orientation eigenvector's
O(q²/lambda²) change; it cannot be absorbed into the first for every p>1.
Ordinary lambda^L q4 terms are included in the looser displayed q4 error.
Consequently the actual energy-density spectral atom is

 Z_E(q)=J²gamma²(L+2)²/(128L) lambda^(2L)|q|4[1+o(1)].

This is a derived nonzero coupling for nonzero small momentum, with exact
uniform-energy darkness. It is not a constant scalar charge.

## Shrinking momenta and actual-H transfer

All individual native bond terms preserve the full plane characters. Work
in the selected character and exact momentum fibre. Match every local
normal-form transformation on source and states. At q=0 the inelastic vector
vanishes identically because E0 is H/sqrt(V). In the local centered orientation
basis inversion makes the finite-order kernels even in q. Their bounded
spatial displacement moments then give q² factors in higher-order source
corrections; using only an absolute O(lambda^(L+2)) error would be insufficient.
Disconnected scalar ground pieces cancel under the same matched construction.

Choose fixed p>1, R asymptotic lambda^-p through even integers and fixed nonzero
reciprocal label n, q=2pi n/R. The inherited same-fibre orientation gap is
order Jlambda14. A final absolute Hamiltonian remainder JR²lambda^M yields
projector error R²lambda^(M-14). Multiplying the crude energy-source norm
O(JR) gives the displayed JR³lambda^(M-14). For L10 it is smaller than
Jlambda10 q² if M>24+5p. Source remainders can be retained to this same
sufficient fixed order. For example p=5,M=70 satisfies this and the inherited
pole conditions. The relative errors are O(lambda²)+O(q²/lambda²)+o(1).
No fixed-lambda infinite-volume limit or all-orders convergence is claimed.

## Limits and remaining connection

The mode, source and coefficient all belong to the same native Hamiltonian.
The calculation replaces a freely postulated oscillator coupling by a checked
matrix element of a specified native energy density. It does not derive a
universal metric coupling, source/detector apparatus, observed scalar,
longitudinal propagation, common relativistic cone, or initial-state selection
beyond the ground-existence theorem. Energy-density improvement freedom remains
an explicit measurement convention. No observations were fitted or tested;
these are exposed model-development and exact-coefficient controls.
