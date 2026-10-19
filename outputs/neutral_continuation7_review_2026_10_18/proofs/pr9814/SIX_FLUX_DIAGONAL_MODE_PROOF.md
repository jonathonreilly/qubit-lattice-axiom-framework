<!-- Original PR9814 source SHA256 ec66d09cdba85212de8a2b14532c6206a322988161e64a815d9e90d3dec0e66d. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# A native staggered neutral diagonal-pair mode

Status: conditional-support. Trace: upstream_support. No retained proposal.

Use the existing H=-J sum(ZZ_z+lambda XX_x+lambda YY_y), fixed L=10,
even transverse R sufficiently large, and lambda tending to zero. No extra
interaction or degree of freedom. Geometry, anisotropy and physical units
remain premises. The exact all-positive-plane global-ground existence is
[REFLECTION_GROUND_SECTOR_PROOF.md](REFLECTION_GROUND_SECTOR_PROOF.md).
The global low-energy Q-relative local normal form and fixed-p polynomial
embedding are [ISOTROPIC_BOUND_FEATURE_PROOF.md](ISOTROPIC_BOUND_FEATURE_PROOF.md)
and [POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md).
Native winding, sixth-order perimeter, and twelfth-order detour are as derived
in [EIGHT_FLUX_BOUND_CLUSTER_PROOF.md](EIGHT_FLUX_BOUND_CLUSTER_PROOF.md).

Set Delta=L/16, a=25L/18432, b=3L/8192,
gamma=12155/33554432, d=1076510135/10567230160896.
The diagonal energy above a flat configuration is
J Delta Q lambda4/4+J(2a Q+2b perimeter)lambda6+O(lambda8).
The offdiagonal nearest-column flip is
-J[gamma lambda10+d lambda12 sum_(two adjacent plaquettes)P
+u lambda12]E_edge+O(lambda14), with scalar u not needed below.
We do not silently set u to zero.

## 1. The six-defect minimum is a two-column neutral feature

A finite Q6 syndrome has even occupancy in each row and column. As an edge
set on the row/column bipartite incidence graph it is a six-cycle. It uses
three rows and three columns, with a permutation matrix removed from their
3 by 3 array. At most two horizontal and two vertical occupied adjacencies
are possible: one row omits the middle column, and similarly for columns.
Thus perimeter>=24-2(4)=16. Equality requires consecutive rows and columns.
Inversion to column flips gives two diagonal pairs and four L trimers.
The former have even column parity; the latter odd. In the positive-plane
sector the minima are exactly
A_r={r,r+ex+ey}, B_r={r+ex,r+ey}.
Both have common center r+(1/2,1/2). Nonminimal Q6 states are separated by
at least 4Jb lambda6. Q4/Q8 sectors differ in energy by order Jlambda4.
Flat row/column identifications are included in the fixed-character orbit
basis. These local patterns are distinct for sufficiently large R.

The leading rest energy is (3/2)JDelta lambda4+J(12a+32b)lambda6+O(lambda8).
It is not a measured mass. Q6 is an approximate normal-form charge, not a
new exact conservation postulate.

## 2. Native paths select internal orientation and momentum

Two winding hops with a Q6 intermediate have order lambda14 but can return
to a minimum only at the original pair: they are onsite selfenergy. For a
Q4/Q8 intermediate m let q_m and p_m denote its defect number and perimeter:

 D4=(6-q_m)Delta/4, D6=2a(6-q_m)+2b(16-p_m).

Each path contributes Jgamma²/D4 at order lambda16 and
J[-gamma²D6/D4²+gamma d(m1+m2)/D4] at order lambda18,
where m_j is the adjacent-plaquette sign sum before hop j. This convention
uses E_initial-E_intermediate, so a Q4 denominator is positive.

Every displaced pair has one Q4 and one Q8 route; their order16 translations
cancel. Same-center orientation change has four Q4 routes and gives
+Jt16 lambda16, t16=8gamma²/Delta. The lower combination is A-B.
At order18 the displaced amplitudes are

 A_move=-48gamma² b/Delta²+8gamma d/Delta=4.13308411037e-7,
 B_move=-32gamma² b/Delta²=-3.936691639339074e-8.

A_move translates a fixed orientation by one axial unit; B_move changes
orientation and translates its center by one axial unit. The scalar u
cancels from these displaced amplitudes with the order16 denominator sum.
It does contribute to a momentum-independent order18 orientation splitting,
which is not reported as derived here. The detour is essential: dropping it
would give the wrong sign of A_move and hence the wrong preferred momentum.

No earlier offsite term was omitted. A direct change of four entire columns
requires at least twenty physical V insertions. Below that, relevant native
N0 flips are adjacent two-column windings. Two hops through Q6 stay onsite.
Three nearest-edge hops toggle checkerboard column parity oddly and cannot
connect two diagonal pairs. Four hops with three small lambda6 denominators
start at order22. Higher diagonal corrections enter the non-Q6 denominators
only after the displayed order18. These are finite-order statements.

The lower orientation band therefore has momentum-dependent part
2J(A_move-B_move)lambda18(cos qx+cos qy)+O(Jlambda20), with weighted local
remainder bounds. Its minimum is q*=(pi,pi). About this minimum,

 E_-(q*+k)-E_-(q*)=J K6 lambda18 |k|²
 +O(Jlambda20 |k|²+Jlambda18 |k|4+J R²lambda^M),
 K6=A_move-B_move=8gamma d/Delta-16gamma²b/Delta²>0.

Reflection and translation symmetry remove odd powers of k. The orientation
gap is 2Jt16 lambda16[1+O(lambda²)]. The omitted common energy and splitting
corrections do not affect the leading resolved-grid increment. This is a
staggered mode; a uniform q0 scalar is not inferred.

## 3. Exact-H interpretation and limits

Apply the inherited local N and Q normal forms, then finite-order elimination
of nonminimal Q6 shapes (gap lambda6), then the two-orientation reduction.
At every retained order the connected paths have bounded displacement moments;
therefore momentum-dependent errors carry |k|² after subtracting q* energy.
Local four-column native terms beginning at order20 are within the stated
remainder. Global Q-relative positivity separates these low levels from wall
sectors even when the entire N0 bandwidth overlaps high states.

For each fixed p>0, R asymptotic lambda^-p through even integers, choose final
absolute remainder exponent M>18+4p (and source condition below). Then actual
microscopic same-momentum-fibre levels resolve the positive increment at
fixed nonzero reciprocal-grid displacements k=2pi n/R. This is an actual
finite-volume spectral branch above one actual global ground, not just a
truncated coefficient eigenvalue. It is not fixed-lambda infinite-volume
control, an all-orders convergent series or a uniqueness theorem for all
microscopic ground sectors.

## 4. Physical readout and point-group qualification

Let D^X_r=product_z X_(r,z) and D^Y_r=product_z Y_(r,z), and define
P^alpha_q=(sqrt(2)R)^-1 sum_r exp[-iq.(r+(1/2,1/2))]
[D^alpha_r D^alpha_(r+ex+ey)-D^alpha_(r+ex)D^alpha_(r+ey)].
The neutral observable S_q=(P^X_q+P^Y_q)/2 adds no Hamiltonian term.
In N0 at L10, D^Y_r=-D^X_r, so pair products agree and S_q creates the
normalized antisymmetric diagonal pair at leading order. At q* its phase
is real and S is Hermitian. It preserves the exact full-plane characters.

Under integer-site-centered spatial C4 with spin rotation about z by pi/2,
the two diagonal orientations exchange and the Bloch center shifts by an
odd lattice unit. At q* these two minus signs cancel; P^X and P^Y exchange.
Their average is invariant. Axial spatial mirrors similarly have the
orientation/Bloch cancellation. Thus S_q* is scalar under the transverse
little point group, while at q0 the antisymmetric pattern is not scalar.
This is not a 3D Lorentz scalar or a uniform cosmological field.

Each diagonal X pair reverses 4L external YY bonds; each Y pair reverses
4L external XX bonds. The matched-source amplitude correction is
-2(4L)(lambda/8)²=-Llambda²/8. Shape admixture starts at lambda4 and its
normalization at lambda8; non-Q6 mixing starts later. Both source components
therefore have the same first correction. The pole weight of S_q* is

 |<B_-|S_q*|ground>|²=1-Llambda²/4+O(lambda4)=1-5lambda²/2+O(lambda4).

Finite-pattern translated Gram bounds control the connected inelastic source
without area growth. The final crude source norm O(R) times projector error
R²lambda^(M-16) is negligible through lambda4 if M>20+3p. Together with
M>18+4p this provides a sufficient fixed-p joint-limit condition. Source and
states must be transformed together; no product-vacuum fidelity is assumed.

The native Hamiltonian fixes this mode and its readout residue. The physical
observable is explicitly specified and extended over two ten-qubit columns.
An actual experimental detector for it, universal coupling to other features,
statistics, Lorentz invariance, geometry selection and observed scale matching
are unproved. No empirical data enter these exposed development calculations.
