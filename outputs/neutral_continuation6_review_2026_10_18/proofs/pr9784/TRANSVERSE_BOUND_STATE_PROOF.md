<!-- Original PR9784 source SHA256 2d634de40b9e119ea6785fb5d9dd935205898749b675f454d279e5bff76069d6. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Native transverse band-edge composite (root)

Status: bounded-support. Supplied anisotropic one-qubit Hamiltonian, uniform reference, compact layer-even four-wall sector, first-order coefficient K1. No new interaction. The earlier complete configuration classification says each state is two columns reversed over the same interval. At interval length one, arbitrary transverse separation is allowed; at length at least two, nonadjacent columns are frozen at K1. Their zero eigenvalues do not affect the following negative isolated state.

## Full first-order graph at general momentum

Write a=cos(Qx/2), b=cos(Qy/2), c=cos(Qz/2). The length-one host is Z² without the origin, with inversion-even pair wavefunctions, hopping -2a along x and -2b along y. Unit-norm orientation roots are |x>=(|ex>+|-ex>)/sqrt2 and |y>=(|ey>+|-ey>)/sqrt2. The adjacent-column interval rays ell>=2 attach to these roots with hopping -2c for x and +2c for y; those signs follow from XX and YY on equal spins. On opposite spins both transverse single-spin exchanges are negative. These are physical pair COM phases, not chosen dispersions.

Direct Bloch sums of physical bit configurations on an8x8x10 torus check representative host and interval edges at(0,pi,0) and(pi/2,pi/2,2pi/10). This uses640-qubit configurations, not diagonalization of a2^640 matrix. No additional qubits or interpolated interaction are present.

## Exact isolated mode

At a=c=1,b=0, host rows decouple. The inversion-related y=+/-1 rows and the y interval ray form one three-lead T junction. Each lead has hopping magnitude2; alternating signs gauge away the positive y-ray hopping. The y=0 punctured row plus the x interval ray is a full chain. Other rows are chains, and nonadjacent long intervals are frozen. Thus all components outside the T bound pair have spectrum within[-4,4].

For the negative T eigenvector, the root amplitude is v0=1/2 and the three lead magnitudes are v0 r^n, n>=1, r=1/sqrt2. The y interval lead has an extra(-1)^n. Normalization is v0²[1+3r²/(1-r²)]=1. The root and tail equations give

 E0=-3sqrt2,

strictly below-4. The unique negative state is isolated from the complete K1 continuum, not just a selected finite-box level. There is a positive bipartite partner; it is not part of this lower-state claim. Physical leading energy is8Jz-3sqrt2 Jz lambda.

Changing b perturbs K1 by operator norm at most4|b|. Therefore8|b|<3sqrt2-4 is a sufficient isolated-branch neighborhood. Analytic perturbation gives a single real eigenbranch and projector there. The b-sign gauge makes its energy even in b.

## Derived readout and its first nonzero overlap

Use the original distance-two Fourier readout divided by sqrt(number of physical sites), with bond-center phase. A pair of single flips costs8Jz. First-order ground dressing and its actual readout difference give

 q_C(Q)=-lambda cos(Qz)[a|x>-b|y>]+O(lambda²).

The physical bit Bloch control checks this normalized coefficient directly, including cos(Qz). At the anchor the bound state lies in the y T component and the source lies in the disconnected x chain: the leading overlap is zero.

Set a=c=1 and perturb b. The root y amplitude is1/2+O(b²). The y=0 component is a full chain, with Green kernel at E0

 G_nm=-r^|n-m|/sqrt2.

Choose its integer coordinate so the original host x root lies at n=1 and the x interval ray occupies n<=0. The native perturbation drive on n>=1 is -4b v0 r^n. Summing its geometric convolution gives the x-root amplitude4b v0+O(b³)=2b+O(b³). The original source therefore has

 <psi_b,q_C>/lambda=-3b/2+O(b³),
 |<psi_b,q_C>|²=(9/4)lambda² b²+O(lambda² b4)+O(lambda³)

for fixed small nonzero b in the coefficient/source expansion. This is a positive isolated-eigenstate source weight at leading order, unlike a complex resonance residue. It is not an experimental line area or a full-H spectral assertion. If b shrinks with lambda, omitted source terms can compete and must be retained; no uniform joint scaling is asserted.

## Dispersion: explicitly a saddle

The first energy correction from b is computable without a fit. The first-order drive also enters the free y=2 row with f_n=-2v0 r^|n|. The two disconnected Green sums are

 S++=sum_(n,m>=1) r^(n+m+|n-m|)=3,
 Sabs=sum_(n,m in Z) r^(|n|+|m|+|n-m|)=13.

Consequently E2=-(16v0² S+++4v0² Sabs)/sqrt2=-25/sqrt2, and

 E(b)=-3sqrt2-(25/sqrt2)b²+O(b4).

Hellmann-Feynman splits the three equal lead energies into two horizontal and one interval contributions: dE/da=-2sqrt2, dE/dc=-sqrt2. With delta_y=Qy-pi, the coefficient band locally is

 E(Q)=-3sqrt2+(sqrt2/4)Qx²-(25/(4sqrt2))delta_y²+(sqrt2/8)Qz²+O(|Q-(0,pi,0)|4).

The transverse y curvature is negative. This is a momentum-dependent neutral bound composite, not a positive isotropic relativistic scalar. Its internal scale at the anchor is a few sites; a large-feature limit would require a separate binding-threshold analysis. Native higher orders, ground preparation, the full microscopic band and physical/cosmological identification remain open. All finite-grid controls are exposed model development, with no empirical calibration or independent observation test.
