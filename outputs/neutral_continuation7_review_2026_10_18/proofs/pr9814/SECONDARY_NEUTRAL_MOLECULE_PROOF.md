<!-- Original PR9814 source SHA256 b4f731f7c32d9edbe7ce0e1c3d915c986dc42dba792ae8977fad9e7e773cb4e2. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# A second native neutral molecule from the complete competing manifold

Status: conditional-support. Independent geometry, energy, motion and transfer checks completed; final scoped review recorded separately.
No new interaction. All coefficients refer to H=-J sum(ZZ_z+lambda XX_x+lambda YY_y), fixed L=10, positive plane-character global ground, weak lambda, and growing even transverse periods. These remain model premises, not observationally derived inputs.

## Complete shape competition

Q8 means eight bad column plaquettes. At perimeter sixteen its finite-support, even-column-parity inverse configurations are exactly, modulo translations/D4:

* Two columns separated by (a,b), a>=b>=0, with a>=3 or a=b=2.
* A rod of odd length d>=3 plus a singleton with one intervening vacant site.
* A T tetromino.

The exhaustive argument is short: eight syndrome cells and even row/column degrees allow occupied incidence dimensions only 2x4, 3x4 or 4x4 up to transpose. Perimeter sixteen requires eight adjacent occupied pairs. In 2x4 this forces adjacent rows and exactly one nonunit column gap, giving two columns or the rod family. In 3x4, the degree-four row must be the middle of three consecutive rows, and horizontal adjacency four allows either two separated neighboring-column blocks or the inner/outer pairing of four consecutive columns, giving two columns or T. In 4x4 each occupied row/column pair must be adjacent; saturation from the leftmost pair forces two full 2x2 blocks, giving two columns. Empty gaps remain arbitrary throughout. The [complete incidence check](INDEPENDENT_SECONDARY_GEOMETRY_CHECK.md) spells out the cases; the [D8 completeness check](INDEPENDENT_SECONDARY_ENERGY_CHECK.md) checks the connected graph reduction.

The rod family has unbounded column count. A seven-wide enumeration missed its d>=5 members; that failed finite-box shortcut is preserved. The independent incidence proof uses only eight plaquettes, even row/column degrees and H+V=8 adjacency count. It imposes no bound on empty gaps. On a sufficiently large torus choose empty row/column cuts for the at-most-four occupied syndrome coordinates; the positive-plane quotient identifies flat-line inverse ambiguities. Wrap representatives must be treated in that quotient, not duplicated as separate localized states.

At fixed Q8/perimeter16 all scalar, single-plaquette and nearest-neighbor-plaquette terms are common. The complete distinguishing order-eight operator, divided by JLlambda8, is

 -c [sum straight-three products + sum four-plaquette boxes]
 +h sum four orientations of L-triomino products
 +k sum two diagonal plaquette-pair products,

 c=9/262144, h=5/262144, k=29/1327104.

The primitive simple-loop integral gives c,h. Equal-layer and adjacent-layer touching squares including folds give k=3/65536-254/10616832. Repeated-edge graphs and other folds give only common terms at these fixed invariants. This is a full order-eight reduction, not a rectangle-only ansatz.

Relative to two distant single columns, the distinguishing energy coefficients are:

| shape | coefficient per JLlambda8 |
|---|---:|
| separation (3,0) | -9/32768 |
| separation (3,1) | -9/65536 |
| separation (2,2) | 545/5308416 |
| other allowed two-column separation | 0 |
| every odd rod plus singleton | 9/32768 |
| T tetromino | 683/663552 |

Thus the axial separation-three pairs are the unique shape minimum of this manifold, up to translations and orientation. Define v=9L/32768. The next shape lies Jv lambda8/2 higher. The lower perimeter-twelve and perimeter-fourteen Q8 manifolds are separated at order lambda6, so this is an excited bound family within Q8, not its lowest molecule. Other Q sectors separate at order lambda4. Uniform reductions must use the previously proved local Q-relative normal form; extensive absolute vacuum energies cannot be used as a gap estimate.

## Native motion, without a chosen kinetic term

Nearest whole-column hopping is -Jgamma lambda10, gamma=12155/33554432. It has no matrix element inside the separation-three manifold. At two hops, the separation-four intermediate has gap Jv lambda8, while the separation-(3,1) intermediate has gap Jv lambda8/2. The parallel and transverse translation amplitudes are consequently

 -Jgamma²/v lambda12 and -4Jgamma²/v lambda12.

The transverse factor four includes both orderings and the half-sized energy denominator. Using a guessed common denominator would give the wrong curvature.

Horizontal and vertical pair orientations first communicate after six nearest column moves. Their endpoint matching distance is six. The leading paths remain within Q8/perimeter16; paths visiting other perimeters have larger denominators in weak-coupling power counting and are subleading. Direct multi-column native vertices and higher-order winding corrections are also subleading. Exclude all intermediate returns to the two-orientation model space. Exact rational path sums give the off-diagonal symbol

 -J zeta lambda20 cos³(qx/2) cos³(qy/2),
 zeta=64 gamma6 C/L5,
 C=1046023065421557893414518784/118275147.

The sixteen endpoint weights are C times the product of two binomial-(3) rows; all have the same negative Hamiltonian sign. This coefficient is an exact finite path sum, not fitted. No lower-order folded orientation term exists because no lower-order path connects the orientations.

At q=0 the lower combination is even under exchanging orientations and has splitting 2Jzeta lambda20. For |q|<<lambda4 the actual lower branch has isotropic increment

 (5/2) Jgamma²/v lambda12 |q|²,

with local errors O(Jlambda14 q² + Jlambda4 |q|4). The second error is the avoided-crossing expansion: the diagonal orientation anisotropy is order lambda12 q² whereas their mixing is lambda20. The scalar statement is transverse square-lattice A1, not three-dimensional Lorentz invariance.

## Physical source and transfer obligations

Define D^alpha_r=product_z sigma^alpha_(r,z), and S^alpha_q=(sqrt(2)R)^-1 sum_r [exp(-iq.(r+3ex/2))D^alpha_r D^alpha_(r+3ex)+exp(-iq.(r+3ey/2))D^alpha_r D^alpha_(r+3ey)]. Use S_q=(S^X_q+S^Y_q)/2. At q=0 subtract its exact ground expectation to define the connected source; neutral charge does not make it orthogonal to the ground. Its column-space projection creates the even orientation combination with unit amplitude. For L=10 each separated-column pair reverses 4L transverse YY (or XX) virtual bonds. Matched ultraviolet dressing therefore gives the q=0 pole weight

 1-Llambda²/4+O(lambda4).

At generic |q|<<lambda4, the fixed symmetric source has an additional orientation-overlap error O(|q|4/lambda16); it cannot be silently included in O(lambda4) for all p>4. For p>=5 it is at most that size on the first momentum grid.

Shape admixtures begin in amplitude lambda² and change this source residue only at order lambda4. The operator is a readout, not an extra interaction. Its norm is O(R). No claim is made that it equals a laboratory detector or cosmological scalar.

Use the established finite-order local normal form to any final remainder O(JR²lambdaM), after all shape-gap denominators. For R of order lambda^-p, p>4, the common resolved infrared branch requires M>12+4p. The source projector tail across the orientation gap lambda20 is O(R³lambda^(M-20)); M>24+3p makes it smaller than the retained lambda4 source error. For example p=5,M=70 suffices. The finite-pattern charge Gram controls the normalized local source expansion. Exact positive-plane global-ground existence is inherited from the checked reflection proof, not assumed sector selection.

## Derived overlap with a physical two-constituent source

For generic relative momentum k with 2k not reciprocal zero, define

 O_k=[R^-2 sum_(r!=s) exp(ik.(r-s)) D^X_r D^X_s]/sqrt(1-2/R²).

This is the fixed physical pair operator used previously, not a fitted effective scalar coupling. Its projection has unit flat-state norm. At total momentum zero, the secondary molecule's native nearest-column hopping produces tails at relative displacement (4,0) with amplitude 2gamma lambda²/v from the horizontal component, and at (3,+/-1) with amplitude 4gamma lambda²/v. The vertical component gives rotated tails. The latter denominators are v/2, so they cannot be omitted. Separation-two states are only order lambda4 in amplitude because their perimeter gap is order lambda6.

The resulting connected pole form factor is

 sqrt(2)/[R sqrt(1-2/R²)] times
 { (1-Llambda²/8)[cos(3kx)+cos(3ky)]
 +lambda²[(2gamma/v)(cos(4kx)+cos(4ky))
 +(4gamma/v)(cos(3kx+ky)+cos(3kx-ky)+cos(kx+3ky)+cos(kx-3ky))] }
 +O(lambda4/R).

The first correction is matched ultraviolet dressing; the additional momentum structure comes from the same native interaction and virtual shape motion. Norm corrections to the molecule start at lambda4. This is a spectral form factor, not an on-shell scattering amplitude or a matter-coupling identification. At special self-inverse k the pair normalization changes and this displayed generic formula is not applicable.

Finite-order charge-locality bounds the relative-support l1 norm of these corrections independently of R. Nonlocal torus paths enter only beyond any chosen fixed perturbative order. For the O(R²)-norm pair operator, the final orientation-gap projector tail is O(R4lambda^(M-20)); M>24+5p makes it smaller than lambda4/R. The example p=5,M=70 still suffices. Ground expectation subtraction removes the neutral elastic contribution.

This block has no independent observation test. It derives another model excitation and a physical operator overlap, not a universal charge, emission rate, fermion, common relativistic metric, or TOE. The exact squared-energy comparisons remain active.

**Deferred terminal interpretation (packet pending):** the previously stated common-metric obstruction remains an inspectable scientific continuation, not an active promoted conclusion.
