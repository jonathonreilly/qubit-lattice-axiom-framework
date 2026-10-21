# Exact and conditional core arguments for the supplied corner model

This is live supporting mathematics. The model, flux sector, number conservation, gauge-dressed rotation action and coordinate units are supplied. Representation reconstruction and sampled spectra must be distinguished from the following algebraic implications. None identifies a physical particle or constructs a native one-qubit dynamics.

## Affine action and representations

Write a dressed rotation as a signed permutation with sign
`(-1)^(lambda_R.v + tau_R(c))`. Its action on a Bloch state gives
`k -> R k + pi s_R`. The finite GF(2) equations fix the signs. The axis half-turn fixed-point equations restrict each component to the quarter-grid modulo `2pi`; enumeration of that grid is therefore complete for the fixed-point question. It is not a band-minimum search. In the supplied flux sector the common fixed points are `k*=(pi/2)(1,-1,1)` and `-k*`.

Conditional on the exhibited binary-octahedral representation
`E1/2 + E5/2 + 2 G3/2`, every commuting Hermitian operator has scalar action on each irreducible factor and arbitrary Hermitian action only on its multiplicity space. Since these irreducible dimensions are even, all levels at the fixed points are even. The numerical character reconstruction and six random commuting Hamiltonians test this specific representation; random Hamiltonians do not prove the universal implication, which is Schur's lemma.

In the folded two-valley space, inversion exchanges the two inequivalent doublet sectors through the A2 character. If the Hamiltonian also commutes with that inversion, their spectra coincide. G3/2 factors already have dimension four. Thus levels of this specified folded symmetry class have multiplicity divisible by four. A directly A2-weighted staggered seed may split these quartets. Its normalization requires a nonzero projection. A finite quartet split alone is not the Clifford kinetic/mass relation needed for a leading Dirac dispersion. The separately scoped parent Dirac-pair construction supplies such a projected relation for its own explicitly chosen matrices; it is not inferred from this runner's arbitrary background split.

## Isotropic tensors and supplied actions

An invariant symmetric matrix under independent coordinate sign flips is diagonal. Invariance under all coordinate permutations equates its diagonal entries. Thus in four dimensions the full signed-permutation group leaves one symmetric rank-two tensor. With only spatial permutations and time reversal it leaves two, the time component and the common spatial component. The primary computes the complete Reynolds image of all ten basis symmetric matrices with integer arithmetic.

For an isolated spinorial doublet at an octahedrally fixed momentum, the linear vector coupling is proportional to `q.sigma`. A nonzero coefficient is an additional condition; symmetry also permits zero. The full supplied analytic family has higher-order terms. The primary's angular spreads at three radii are finite evidence for the displayed quadratic relative anisotropy, not a uniform remainder estimate for all parameters.

A common physical speed does not follow from the tensor count alone. It requires the supplied common four-dimensional symmetry/action, isotropic coordinate normalization, and the relevant spin/gauge kinetic assumptions. Spatial cubic symmetry by itself permits different speeds for different supplied fields.

## Link reflection and flat modes

Each corner `{a,b}` at `v` has exactly two link neighbours, `{−a,b}` at `v+a` and `{a,−b}` at `v+b`. The diagonal of `H_link^2` is two. Its only off-diagonal two-step endpoint is `{−a,−b}` at `v+a+b`; the two paths enclose a pi-flux link plaquette and cancel. Therefore `H_link(k)^2=2I` for every momentum, not only torus samples. Its trace is zero, so `R=H_link/sqrt(2)` has six positive eigenvalues.

Let `P2` be the four-dimensional eigenvalue-two projector of the supplied onsite hopping. Then `U=I-2P2` is a reflection with positive-space dimension eight. The positive spaces of R and U intersect in dimension at least `6+8-12=2`; their intersection gives exact eigenvalue-one states of `W=RU` at every momentum. Generic numerical samples find dimension two; the lower bound is the universal dimension argument.

The exact coefficient helper constructs the onsite matrix from signed integer edges, takes the exact kernel of `H_on-2I`, and forms its orthogonal projector algebraically. It evaluates each link Fourier monomial at k* using powers of i and differentiates the monomial analytically. For an exact kernel basis N of `W(k*)-I`, with Gram matrix G=N†N, its first-order phase matrix is

`M(q)=G^(-1) N† [-i U H_link(k*)† (sum_j q_j d_j H_link) U / 2] N`.

No rounded derivative or fitted rational coefficient enters. The coefficient certificate verifies

`M(q)^3=(|q|^2/3)M(q)`, `tr M=0`, and `tr M^2=4|q|^2/3`.

For real nonzero q, M is self-adjoint in the Gram inner product. Its possible eigenvalues are zero and `±|q|/sqrt(3)`; the traces force multiplicities two each. This is a first-order statement. The finite-q spectrum has higher-order corrections. The six-state node is not a four-component Dirac particle.

## Constant-spectrum algebra lemma

Assume differentiable normal generators F_j(k) near k*, with constant distinct eigenvalues, locally constant multiplicities and differentiable orthogonal spectral projectors. Each generator commutes with the supplied translations and gauge-dressed point-group action. Assume the spinorial irreps E1/2 and E5/2 each occur with multiplicity one at k*. Let D be an exactly two-dimensional isolated level of a Hermitian Hamiltonian or unitary step in the generated algebra.

Schur's lemma makes every generator scalar on D, so D is contained in one full eigenspace E of each generator. Write `F=sum_a lambda_a P_a(k)`. Differentiating `P_a^2=P_a` gives `P_a dP_a P_a=0`. Differentiating `P_a P_b=0` for a≠b and compressing by P_b gives `P_b dP_a P_b=0`. Therefore `P_E dF P_E=0` and hence `P_D dF P_D=0`.

At k*, the product rule gives `P_D d(FG) P_D = f_D P_D dG P_D + g_D P_D dF P_D`. This extends to every finite sum and product. The first-order compression vanishes. Isolation makes it the first-order spectral shift of that level. This proves the stated zero derivative under these premises, not a claim about arbitrary nonnormal matrices or repeated irreps.

Multifold nodes can mix inequivalent factors at the same eigenvalue and evade the isolated-doublet conclusion. Momentum-dependent generator spectra, nonsymmetric factors with a symmetric product, and different little groups also lie outside the premises. The primary's finite reflection-product tests explicitly require actual unitarity and at least one isolated doublet with exactly two selected phases.

## Weyl-automaton group-speed bound

Use nearest-neighbour distance per tick, `x_i=k_i/sqrt(3)`, and
`d=cos x cos y cos z - sin x sin y sin z`, with eigenphases `±acos d`.
At a differentiable point, `|grad_k omega|^2=(sum_i d_i^2)/(3(1-d^2))`, where d_i differentiates with respect to x_i.

Put `A_i=cos^2 x_i`, `B_i=sin^2 x_i`, `p=prod_i cos x_i sin x_i`, and `D0=prod A_i+prod B_i`. Direct expansion gives
`d^2=D0-2p` and `sum_i d_i^2=1-D0+6p`.
The six mixed products in `1-D0` are nonnegative and have geometric mean `|p|`; their sum is at least `6|p|`. Consequently `sum_i d_i^2 <= (3/2)(1-d^2)` and `|grad_k omega|<=1/sqrt(2)`. Equality occurs at `x=(3pi/4,-pi/4,5pi/4)`.

For one component, regard d as `A cos x_i-B sin x_i`. Then `d^2+d_i^2=A^2+B^2<=1`, so `|d_i|/sqrt(3(1-d^2))<=1/sqrt(3)`. These inequalities apply where the gradient exists and bound limiting directional speeds. The small-k expansion gives speed `1/sqrt(3)` and an allowed cubic product term, hence linear relative anisotropy for this T_d-symmetric dispersion. They do not assert full octahedral symmetry of that automaton.

## Conditional eigenphase-counting argument

Suppose a continuous finite- or summable-range unitary Bloch step has a genuine global quasienergy gap at E', commutes with translations and the specified anticommuting dressed axis-half-turn lifts, and has an exactly twofold isolated nonsingular linearly split untilted doublet at k* at E. The nonsingular linear cone condition means one branch is below E in every nonzero sufficiently small direction. The half-turn symmetries force zero tilt here.

Count eigenphases n(k) in the arc from E' to E. Away from the E-level set this integer is locally constant. At each of the eight common half-turn-fixed cube points its value is even whenever E is absent, because all eigenvalues there have even multiplicity. Immediately around k*, the count is odd: the other levels contribute an even number and precisely one of the two cone branches is below E. Thus the E-level set separates k* from any cube point at which E is absent. If the E-level set is finite, the punctured three-torus is connected, and all eight cube points must be in it.

This is a conditional parity argument. Finite grids do not establish its global-gap or finite-level-set premises. The corrected primary reports only its sampled eigenphase distances and empty histogram arcs. No exhaustive species census or global absence of a gap is inferred from those samples. The complete conditional argument remains inspectable even where terminal exclusion promotion requires further review discipline.

## Winding boundary

For smooth maps on the three-torus, winding is additive under products. Constant onsite factors, diagonal shifts and the stated reflection factors have zero three-dimensional winding, giving zero for their word class. Under the imported Floquet theorem's actual hypotheses this constrains net charge. Zero net charge permits balanced Weyl nodes, including isotropic nodes. It does not exclude all common-speed steps or all finite-range symmetric constructions. Broader winding-based exclusions and absent phase-two assertions remain historical proposals, not premises of this note.
