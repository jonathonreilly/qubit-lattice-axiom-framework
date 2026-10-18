# A native plaquette interaction between large column features

Status: conditional fixed-order derivation. The original one-qubit directional Hamiltonian generates a four-column interaction and favors the previously chosen positive-parity band in a fixed finite tube at sufficiently small transverse coupling. No new microscopic interaction, extra site qubit or parity constraint is added. This does not select a cosmological state or establish the isotropic three-dimensional ground phase.

Replay: [native_column_plaquette_selection.py](../scripts/native_column_plaquette_selection.py).

The starting Hamiltonian is supplied, with strong ferromagnetic Jz and Jx=lambda jx, Jy=lambda jy, where jx and jy are fixed nonzero couplings as lambda tends to zero. The numerical cases use Jx=Jy=Jperp. If either transverse coupling vanishes, the plaquette term vanishes; a ratio that itself tends to zero needs a separate order comparison. Longitudinal columns have length L>=5. At zero transverse coupling every column is uniformly up or down; its sign is a logical coordinate of L physical sites. We now retain ALL aligned column configurations, rather than imposing positive four-column parity. This extends [the column tunneling calculation](NATIVE_LARGE_COLUMN_DYNAMICS_NOTE_2026-10-18.md). The neutral packet results in [the local normal-form note](NATIVE_LOCAL_NORMAL_FORM_NOTE_2026-10-18.md) remain conditional on their own prepared state and geometry.

## Four native bonds produce the interaction

Take one elementary transverse square with X edges01,23 and Y edges02,13. Apply each edge once, in every ordering. The final physical spin configuration returns to its initial value. The Pauli phases retain the product P_square=Zbar0 Zbar1 Zbar2 Zbar3 of the four aligned column signs.

For an interior longitudinal slice, flipping one physical spin costs4Jz. For an end slice of an open column it costs2Jz. Exact summation of all24 signed paths with the three native energy denominators gives

bulk slice: -Jx^2 Jy^2 P_square/(128 Jz^3),
end slice: -Jx^2 Jy^2 P_square/(16 Jz^3).

All16 initial sign assignments give these coefficients. The sign is not chosen to favor the sector: it follows from the Y phases and resolvent denominators.

For L>=5 a fourth-order process cannot reverse an entire column. With four distinct square edges each column is touched twice, so return to the aligned manifold requires those two flips at the same longitudinal site. Connectivity forces all four edges onto the same slice. Thus mixed-slice loops do not add another plaquette coefficient. At second order only repeating the same edge at the same slice returns to the aligned manifold. Both the second-order energy and normalization matrices are scalar; the fourth-order folded subtraction cannot change the plaquette coefficient.

Summing slices gives the generated interaction

H_eff^(4) = scalar - K_L sum_square P_square,
K_L = (L+14) Jx^2 Jy^2/(128 Jz^3) for open columns,
K_L = L Jx^2 Jy^2/(128 Jz^3) for periodic columns.

This is a coefficient at fixed perturbative order. Extensivity in L is not a uniform convergence theorem. Use nonduplicated transverse edges and elementary squares; thin periodic geometries with identified duplicate bonds need separate counting.

An independent exact computation includes every two-step intermediate state and the canonical folded term for an open2x2xL tube, L5..8, all16 colors. It reproduces the parity splitting 2K_L. It does not merely replay the24-loop subset. The color-independent fourth-order energies are kept in the computation, not discarded before comparing parity sectors.

## What assumption is reduced

For the open2x2 tube the aligned manifold has16 states. P_square=+1 has eight and P_square=-1 has eight. Their fourth-order energy separation is2K_L>0. Off-diagonal complete-column tunneling first occurs at order L. Therefore for each fixed finite L>=5 and sufficiently small nonzero transverse ratio, the positive-parity part lies below the negative-parity part within the continued aligned band. The other unperturbed sectors have a nonzero wall gap, so finite-dimensional perturbation theory supplies a sufficiently small interval where the low-energy band descends from the aligned manifold.

This derives a conditional energetic reason for the positive sector. It does not turn that sector into an exact kinematic constraint, fix a vacuum superposition, or supply a uniform size-dependent interval. Boundary conditions, Hamiltonian, anisotropy and the low-energy preparation still matter.

Full native calculations, with no parity chosen between the two competing sectors, compare their eight-state low bands for L5,6 at lambda=Jperp/Jz=.1,.2. All retained eigenvectors have residuals below6e-13. The mean-band splitting divided by lambda^4 approaches2K_L/Jperp^4, and the positive sector is lower in these tests. The finite data are exposed model-development checks, not observational evidence or a general ground-state certificate.

## Deriving the original composite readout

For the existing longitudinal next-neighbor observable C=sum_(column,j) Z_(column,j) Z_(column,j+2), use H+sC only as a source derivative at s=0; this is not a new physical interaction in the candidate. At slice j let n1(j) count its nearest longitudinal neighbors and n2(j) its distance-two neighbors. A flipped spin in the virtual plaquette loop costs

d_j(s)=2 n1(j) Jz - 2 s n2(j).

The loop coefficient is K_j(s)=Jx^2 Jy^2/[2 d_j(s)^3]. Differentiating -K_j(s)P_square yields -6 n2(j) K_j(0)/d_j(0) times P_square. For an open column L>=5, n1 is1 at the ends and2 inside, while n2 is1 on the first two and last two sites and2 elsewhere. Thus

C_eff = scalar - [3(L+13) Jx^2 Jy^2/(128 Jz^4)] sum_square P_square + higher orders.

The parameter-dependent canonical transformation also generates a connection commutator. It cannot alter this order-four coefficient because the aligned-band operators through order two are scalar and the first-order projected generator vanishes; the trace over the continued band is independent of that connection exactly. The finite native test measures the band-averaged original C directly from the eigenvectors, with no fitted readout parameter. For the single-square2x2 tube, its positive-minus-negative difference is predicted to be -3(L+13)lambda^4/64 for equal transverse couplings.

This is a derived readout coupling to the emergent plaquette energy. At this order that readout commutes with the generated plaquette Hamiltonian. It supplies an elastic density response, not by itself an inelastic scalar pole. The smaller inherited tunneling and a wider transverse array must be included to test dynamics.

## General arrays and remaining degeneracy

In a transverse rectangular array, the leading condition is P_square=+1 on each square. Its solutions are z_(x,y)=a_x b_y. There are2^(Nx+Ny-1) such sign assignments for an open rectangle; periodic compatible rectangles obey the same parameter count. Thus this interaction derives a constraint on large features but leaves a subsystem degeneracy. It is a commuting plaquette energy, not a derived gauge redundancy, toric code or relativistic scalar.

The previously derived pair-column tunneling scale is of order Jperp^L/(2Jz)^(L-1) for open columns. At fixed L>4 it is parametrically smaller than the order-four plaquette scale as lambda tends to zero. How the inherited tunneling acts among or outside the plaquette minima, and whether a neutral readout sees a propagating low-energy composite in a wider transverse grid, are the next questions. Neither a scalar coupling nor matter identification is supplied by naming this effective interaction.

## Prior-art boundary and evidence

Virtual-loop generation of plaquette interactions in compass/Kitaev systems is established methodology; see [Compass and Kitaev models](https://arxiv.org/abs/1303.5922) and [A Tale of Two Quantum Compass Models](https://arxiv.org/abs/2206.15199). Those models and their gauge/topological interpretations are not automatically this cubic-column model. Here the claim is the explicitly checked coefficient and its conditional consequence for the current reconstruction, not invention of plaquette emergence.

Exact source calculations, finite native spectra and independent checks are model development. No empirical calibration or independent observation test has been performed. A three-dimensional continuum, isotropy, physical scales, cosmological state, universal matter coupling and measured-gravity bridge remain open.
