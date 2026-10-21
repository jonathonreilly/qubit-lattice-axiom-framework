# Supporting mathematical source

Scope of this supporting source: exact constructive identities retain their stated mathematical validity. Any terminal exclusion developed below is preserved as deferred science, pending its required promotion packet; it is not promoted by this extract or used to strengthen the active canonical claim.

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_COLUMN_STAR_CHECK.md`, SHA256 `e1d6d663e533e74086b119ea9d9638257723a5da8faccd0b3cfe3218368b3ab4`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Conditional four-defect rectangle-star check

The star secular equation, zero-offset residues, threshold and L6 ratio check. The geometry describes the source-connected component at first order in pair flips on an infinite transverse lattice, or its large-grid limit. It is not literally the whole finite periodic four-defect graph. No repository files were changed.

## Rectangle geometry and diagonal cost

In the plaquette-defect description, a local physical nearest-neighbor X pair toggles the four corners of a2x1 or1x2 rectangle. A four-defect configuration that obeys even defect number in each row/column is a rectangle, subject to finite-torus identifications. Even total column-flip parity on an even periodic transverse grid retains even-area rectangles.

To stay in the four-defect sector, the toggled domino corner set must overlap exactly two existing corners. This is possible only for rectangles with a side of length1 or2. Starting from the2x1 and1x2 sources, the connected graph has:

- two A arms:2x1,4x1,6x1,... and1x2,1x4,1x6,...;
- hub2x2;
- two B arms:2x3,2x4,2x5,... and3x2,4x2,5x2,... .

At zero center-of-mass momentum the two equivalent endpoint moves add, giving hopping magnitude2t. Its sign can be gauged on this bipartite tree; keep the same convention for the source. Rectangles with both side lengths>=3 are present in the full sector but frozen at this first order and disconnected from the stated source component. Finite periodic grids eventually fold or join arms and may introduce orbit-normalization/alias effects, so the literal half-line graph needs the large-grid limit.

For -K6 sum_(nearest plaquettes) Pp Pq, four isolated defects break16 neighbor bonds, costing32K6. If one rectangle side has length1 (and the other at least2), there are two adjacent defect pairs; each shared pair removes two broken bonds, giving12 broken bonds and cost24K6. The2x2 hub and B arms therefore have32K6, whereas the A arms have24K6. This verifies the stated offset delta=8K6/t after subtracting the common24K6 and measuring energies in t. The K4 four-defect mass is common to these states.

## Secular equation and residues

Combine the two A arms into their symmetric channel and likewise the two B arms. Each resulting half-line has hopping2 and couples to the hub by2sqrt(2). The hub and B channel have diagonal delta; the A channel diagonal0. The surface resolvent for hopping2 is

g2(z)=(z-sqrt(z²-16))/8,

with g~1/z and the appropriate real branch outside[-4,4]. The hub equation is

F(E)=E-delta-8g2(E)-8g2(E-delta)=0.

Antisymmetric arm combinations are free half-lines and supply no bound eigenstates. For an isolated root, the hub probability is

Z_h=[1-8g2'(E)-8g2'(E-delta)]^(-1).

The normalized symmetric two-A-end source has weight8g2(E)² Z_h. At delta0, E=16g2(E), giving E=±8/sqrt(3), g2(E)²=1/12 and g2'(E)=-1/8. Thus Z_h=1/3 and the source weight is2/9 at either pole. Multiplying by the supplied original-source norm squared2 gives4/9 at either pole. This normalization does not derive the original physical observable/source amplitude; it uses the stated source identification.

## Threshold and complete bound roots for delta>=0

Below the lowest band, F'(E)>1 because each real g2' is negative. At E=-infinity, F is negative. At the lower edge E=-4,

F(-4)=4-sqrt((4+delta)²-16).

Hence a lower root exists exactly for delta<4sqrt(2)-4. At equality the solution reaches the edge and is not a normalizable ordinary bound state; for larger delta there is no lower root.

Above the highest band E=delta+4, F=-8g2(delta+4)<0 and F tends positive infinity, again strictly increasing. Therefore exactly one upper bound root always exists at finite delta>=0. If delta>8 the two essential bands separate, but there is no extra root in their gap: F at the lower gap endpoint4 is negative, F at the upper endpoint delta-4 is also negative, and F is increasing there. Within a propagating band the nonzero hub couplings prevent an isolated radial bound root; the decoupled antisymmetric free arms have none either.

For L6 the supplied K6 coefficient is3*68/8192=51/2048 in the common energy prefactor, while t has coefficient1/32. Thus K6/t=51/64 and delta=51/8=6.375. This is above the lower disappearance threshold, so only the upper star bound mode remains. The zero-delta residues must not be reused at this nonzero offset; use the derivative formula above.

## Perturbative and physical scope

The common order-six single-P renormalization shifts the four-defect mass and remains needed for an absolute excitation energy. A proof that the displayed K6 neighbor term exhausts every relevant order-six diagonal interaction is also necessary: other same-order terms could change A/B offsets, hub energy or additional couplings. At L6, pair-flip tunneling and K6 occur at the same transverse order, so retaining both is essential and omitting another same-order term would alter the leading star operator.

Higher-order terms can connect the first-order-frozen rectangles, enlarge the source component or couple other defect sectors. Boundness in this candidate component does not prove stability in the full effective theory or exact native Hamiltonian. The even-parity, prepared-state, source normalization and infinite transverse-grid limits all remain premises until separately derived. No physical scalar, detector interaction, cosmological bridge or empirical spectral claim follows from this calculation.

## Follow-up: momentum dispersion and L6 readout normalization

The momentum geometry checks using rectangle centers. Increasing a thin A rectangle's long side by2 moves its center by±1, so its two-end hopping is2cos(q_long). Increasing a width-two B rectangle's length by1 moves its center by±1/2, giving2cos(q_long/2). A2x1 endpoint joins the2x2 hub by a y extension, hence coupling a_y, while its arm hopping is b_x. The1x2 endpoint has coupling a_x and hopping b_y. The2x3 and3x2 B arms have coupling and hopping a_y and a_x respectively. Thus the proposed equation is

E-delta=a_y² g_(b_x)(E)+a_x² g_(b_y)(E)
       +a_y² g_(a_y)(E-delta)+a_x² g_(a_x)(E-delta),

a_i=2cos(q_i/2), b_i=2cos(q_i),

where g_h satisfies g_h=1/(E-h²g_h), with the decaying physical branch outside its band. A sign of h away from the origin can be gauged; the surface function depends on h². The equation applies to the source-connected infinite star, subject to the earlier finite-torus and omitted-interaction qualifications.

Write p=q_x² near q0. Then partial_p a_x²=-1 and partial_p b_x²=-4. From the quadratic surface equation,

partial_(h²) g_h=g_h³/(1-h²g_h²),
partial_E g_h=-g_h²/(1-h²g_h²).

Implicit differentiation of the hub equation therefore gives exactly

partial_p E=Z[-16g_A³/(1-4g_A²)-g_A-g_B-4g_B³/(1-4g_B²)],

with Z=[1-8g2'(E)-8g2'(E-delta)]^-1, g_A=g2(E), g_B=g2(E-delta). The y coefficient is identical by square symmetry. This is the coefficient of q_x², not the second derivative with respect to q_x (which is twice it).

Independent root finding at delta=51/8 gives

E_upper=10.45335101527882,
Z_hub=.19198867106999534,
16g_A² Z_hub=.0303796635305607,
coefficient of q_x²=q_y²=-.2635576323011551.

The upper mode is therefore a local band maximum at zero momentum in this effective component. Its negative curvature is not evidence for a relativistic positive kinetic term. At q0 it lies only .0783510153 above the highest host edge delta+4, so finite-momentum isolation should not be extrapolated without checking the moving continuum.

Taking the separately supplied native original-C amplitude coefficient -(63/20)t/Jz as INPUT, the corresponding weight coefficient is

(.0303796635305607)*(63/20)²=.3014422113819885.

Thus the physical dimensionless C weight is .3014422113819885*(t/Jz)² at this order; writing weight/t²=.301442... presumes Jz=1 energy units. I checked this multiplication and the star residue, not the independent native derivation of the63/20 coefficient. Bare differentiation and ground/source dressing must be included consistently before treating that amplitude as established. No new interaction is introduced by this readout calculation.
