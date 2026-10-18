# Six-layer four-flux graph: independent focused check

Disposition: PASS for the projected coefficient graph and its upper bound state, conditional on the supplied native sixth-order coefficients and completeness of that coefficient Hamiltonian. This check does not independently rederive all native sixth-order virtual words or transfer the pole to the full microscopic Hamiltonian.

## Exact syndrome kinematics

Label a finite four-defect configuration by bad-plaquette coordinates. Row and column flux constraints require even defect count in every row and column. With exactly four distinct defects this forces corners of an axis-aligned rectangle. For a finite-support column configuration on the infinite plane, the inverse plaquette syndrome has no nonzero finite-support kernel: the column flips fill the rectangle. Total column parity is therefore (-1)^(ab), and the positive-parity sector requires even area. On a torus extra row/column background labels remain; this infinite-plane argument must not be used to discard them or wrapping/folding effects.

An x-edge column-pair flip has syndrome a 2-by-1 rectangle; a y-edge flip has syndrome 1-by-2. XOR of two four-point syndromes stays at four points exactly when they share two corners. For the 2-by-1 move, this requires either an existing width two (move one horizontal boundary by one), or existing height one (move a vertical boundary by two). The y move gives the rotated alternatives. A diagonal shared pair fixes the entire elementary rectangle and cannot produce a new four-defect output. Equal syndrome annihilates the defects and is excluded by P4 projection.

Consequently the component reached from the edge source consists exactly of center (2,2), arms (a,2), a>=3 and (2,b), b>=3, and arms (2n,1), n>=1 and (1,2n), n>=1. The first sites of the latter two arms are A=(2,1), B=(1,2). There is no missing four-defect nonrectangular shape. Other allowed rectangles not satisfying these width/height conditions are immobile under the projected nearest-edge term and not in this source component. Intermediate excursions to zero/eight defects belong to higher-order elimination, not additional edges of the stated lambda^6 graph.

Independent XOR enumeration checked the center, both source endpoints, long-arm first sites, thin-arm next sites, and remote long-arm sites. Each neighboring relative shape receives precisely two physical moves, one from each boundary. At zero COM momentum their amplitudes add, giving -t with t=2 gamma, using normalized translation-orbit states of equal nonwrapping orbit size. At nonzero COM momentum the two phases must be retained; the zero-momentum factor cannot simply be reused.

## Potential

For -b sum_<pq> Pp Pq, four isolated bad plaquettes cost 32b. If e is the number of adjacent bad-bad pairs, the cost is 32b-4be. Generic rectangles with both widths at least two have e=0; a thin allowed rectangle has e=2, giving relative potential -8b. The excluded 1-by-1 rectangle has odd column parity. Thus the proposed four-ray center has onsite zero, two zero-potential arms, and two arms at -v, v=8b. With b=18/8192 and gamma=63/8192, v/t=8/7 exactly. Terms proportional to the single-plaquette sum are constant within P4 and only change the reference energy.

## Spectrum and readout

For a semi-infinite constant arm with hopping -t and onsite d, its endpoint Green function outside its band is

 g_d(E)=[E-d-sign(E-d) sqrt((E-d)^2-4t^2)]/(2t^2).

The center Schur equation is F(E)=E-2t^2 g_0(E)-2t^2 g_-v(E)=0. On either exterior real interval F is strictly increasing, since g'_d<0. Above the top edge 2t, F(2t)=-2t^2 g_-v(2t)<0 and F(infinity)>0. Hence there is exactly one upper bound state. Independent scalar evaluation gives E/t=2.114475316300653 at v/t=8/7. The upper gap is approximately 0.1144753163 t, strictly positive in this coefficient model.

At the lower edge E=-v-2t,

 F(E)/t=2-sqrt((v/t)^2+4v/t).

A lower bound state exists precisely when v/t<2sqrt(2)-2. Equality is a threshold case, not a normalizable isolated eigenvalue. The native value 8/7 exceeds this threshold, so no state lies below the lowest arm band. The two arm bands overlap at this value; there is no intervening spectral gap. Antisymmetric combinations of equal arms are ordinary constant half-lines and add no exterior bound states.

The upper eigenvector has nonzero center amplitude and equal nonzero first-site amplitudes on the two -v arms. Therefore the symmetric edge source A+B has strictly nonzero overlap. This establishes overlap of the projected E-edge source. A statement about the original microscopic C requires its separately derived dressed-source coefficient, including any ground-state mixing and normalization. It is not implied merely by the graph overlap.

The upper isolated eigenvector is rotation-even in the shape graph. Calling it scalar here means this lattice symmetry channel, not a physical scalar field, Lorentz representation, thermodynamic full-H pole, or lifetime assertion.

## Independent artifacts

/tmp/check_fourflux_graph.py and /tmp/neutral_fourflux_graph_independent.json contain the physical-syndrome XOR enumeration and independent Schur root calculation. No shared repository files changed. No formal audit or native all-order claim.
