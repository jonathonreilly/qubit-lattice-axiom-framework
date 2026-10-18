# Many soft symmetry sectors of the native extended feature

Status: bounded-support. Supplied one-qubit compass Hamiltonian and the
fixed-height-four weak-coupling family of NATIVE_DRESSED_PATCH_PROOF.md.
This counts low-energy heavy levels with multiplicity; it does not derive
a scalar oscillator, fermion statistics, or empirical particle species.

## 1. Statement

Let R be even and comparable to lambda^-1. For an integer patch side
m comparable to lambda^-3/4, there are at least 2^(2m-1) actual odd-parity
heavy eigenvalues, counted with multiplicity, in a window of width
O(Jlambda^(5/2)) above the odd heavy minimum. One can choose one level for
each character of a specified commuting subgroup of exact plane symmetries.
The original neutral bond readout cannot connect different characters.
These may coincide in energy; a large number of distinct frequencies is
not asserted.

## 2. A pure patch trial and its exact symmetry orbit

The previous construction resets a square plus a fixed-width margin to
flat aligned column signs and puts a singleton Dirichlet wave inside it.
The outside reduced vacuum density is mixed. Decompose it into pure states;
one component has the total trial expectation no greater than the average.
Choose that component. This is variational existence, not a physical state
selection. The resulting pure normalized trial v has odd total physical-Z
parity and normal-form energy, relative to the vacuum minimum Eb,

 <v|JB4|v>-Eb <=4J-4Jlambda+CJlambda^(5/2).                 (1)

Use m for the full reset-square side; subtracting a fixed margin does not
change its asymptotic order. Consider m exact plane symmetries in one
transverse direction and m-1 in the other, whose lines intersect this square.
For the native Hamiltonian they are products of X on x-normal planes and
products of Y on y-normal planes. Their mutual intersections contain four
sites, so they commute; they are Hermitian involutions and preserve global
odd Z parity. The equivariant local SW map and B4 commute with them too.

On an aligned column the plane operation reverses its logical sign. On an
occupied column it supplies the native position-dependent phase as well;
this changes the hopping gauge of the singleton wave without changing its
energy. There is no need to drop that phase or hold the outside state fixed.

The resulting subgroup G has 2^(2m-1) distinct patterns within the square.
They have the form s_xy=a_x b_y with one b fixed to remove the redundant
simultaneous sign reversal. Every nonidentity pattern changes at least m
columns. The orbit {gv:g in G} is orthonormal because its inside background
supports are disjoint, regardless of the transformed outside vectors.

## 3. Scalar compression, not an invariant trial space

At order at most four a native interaction word flips at most eight physical
spins. Diagonal filters and resolvents do not add spin flips. Distinct orbit
states differ in at least m background columns, hence at least 4m-2 physical
bits even when their singleton positions differ. For large m this exceeds
eight. Therefore every off-diagonal B4 matrix element between distinct orbit
states vanishes. Exact symmetry makes all diagonal expectations equal.
The compression of JB4 to their span is thus the scalar trial energy.
The span need not be invariant; variational minmax requires only this
compression. Whole-column winding terms at order four obey the same
physical flip count and do not invalidate it.

The inverse SW map preserves orthogonality and symmetry. Its global
remainder has operator norm O(JR²lambda^5)=O(Jlambda³), so the maximum
Rayleigh quotient of the entire transformed span changes by that amount.
There is no multiplication by the exponentially large dimension.

## 4. Counting the actual levels

Apply minmax inside the exact global odd-Z Hilbert space. All aligned N=0
columns have even parity at height four; the vacuum sector is excluded.
Half-column N=2 states also have even parity. The existing wall-relative
bound puts N>=4 above the order-one gap from the heavy cluster. Thus the
low odd spectrum being counted is the singleton two-wall cluster, not a
large collection of vacuum levels. Its lower bound is
Eb+4J-4Jlambda-O(Jlambda³), from the prior theorem. Equation (1) and minmax
give at least |G| levels within O(Jlambda^(5/2)) of the odd minimum.
Replacing Eb by the actual vacuum ground changes only O(Jlambda³).

For the character refinement, the orthogonal orbit carries the regular
representation of G. Its Fourier combinations are nonzero orthonormal
vectors, one per character, all with the same compressed trial expectation.
H commutes with G. Variational minmax in each character's odd sector gives
one actual low heavy level in that character. This does not require those
energies to be different.

## 5. Neutral darkness between the counted sectors

The original C_Q=V^-1/2 sum_r exp[-iQ.(r+ez)] Z_r Z_(r+2ez)
commutes with the exact plane symmetries: each pair overlaps a relevant
transverse plane on two sites or on none. The matched dressed operator
retains this property. Hence its matrix element between distinct G
characters is exactly zero. The same selection rule applies to any
observable commuting with this subgroup.

The count therefore cannot be repackaged as exponentially many visible
scalar modes. It exposes soft symmetry labels of the large feature. Modes
within one fixed character, their dispersion, their coupling to the relaxed
environment, and any connection to ordinary particle statistics remain
separate questions. No extra qubits, interaction, or empirical fit entered
this counting argument.
