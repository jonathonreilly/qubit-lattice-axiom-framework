# Independent reconstruction before author-checker access

The three frozen sources and inherited dependencies are identified in
`PRE_COMPARISON_SOURCES.json`. This is a selective mathematical review of
their supplied representations and operations. No new author checker,
numerical output, log, or twelve-site result was opened in deriving this file.
No native quantum dynamics, phase theorem, or universal obstruction is inferred.

## 1. The operational moment map, with the actual tilted ensemble

Write `|s>` for the two-qubit singlet and
`|t_i>=(sigma_i tensor I)|s>`. These four vectors are orthonormal because the
singlet has zero one-qubit Bloch vector and
`<s|sigma_i sigma_j tensor I|s>=delta_ij`. With an SU(2) representative frame,
the antipodal product vector is `(s + sum_i n_i t_i)/sqrt(2)`, up to an
irrelevant common phase. Consequently, in this basis,

`rho_n = 1/2 [[1,n^T],[n,n n^T]]` and
`rho_a = 1/2 [[1,mu_a^T],[mu_a,M_a]]`.

This is an identity for the stated product interpretation, rather than a
claim that the immutable classical keys are physical qubits. The same formula
can be checked directly from `(I+n.sigma)/2 tensor (I-n.sigma)/2`.

For the quartic color map
`f=(yz(y^2-z^2), zx(z^2-x^2), xy(x^2-y^2))`, direct polynomial substitution
gives `f(Rn)=R f(n)` for every proper signed permutation and `f(-n)=f(n)`.
Each color class is even. The reference density `g0` is constant on each of
the A and B class unions and is invariant under proper cubic rotations.
Thus every class has zero reference first and third moments. Multiplication
by the actual tilt `1+epsilon n.delta`, at fixed direction delta, leaves its
normalizing mass and second moment unchanged and gives

`mu_{a,delta}=epsilon M_a delta`.

This parity step is essential: replacing the actual birth ensemble by its
zero-tilt reference would omit a generally nonzero first moment. Positivity
of the tilt for `|epsilon|<1` preserves each open class support. A linear
functional cannot be constant on an open spherical patch unless its linear
part is zero. Hence the covariance `M-mu mu^T` is positive definite, and the
Schur complement proves that each averaged two-qubit density has rank four.

The stabilizer of A+x contains the proper quarter-turn about x. Its invariant
symmetric matrices are `diag(a,b,b)`, with `a+2b=1`. A proper half-turn about y
maps A+x to A-x and leaves this matrix unchanged. The stabilizer of B111
contains the cyclic coordinate permutation. Its invariant symmetric matrices
are `(1/3-c) I + c 11^T`. The proper rotation
`(x,y,z)->(-y,-x,-z)` maps B111 to B--- and leaves this matrix unchanged.
Proper-cubic transport therefore proves `M_a=M_-a` for all seven opposite
pairs. The fixed-delta tilted first moments agree as well, so

`rho_{a,delta}=rho_{-a,delta}`.

No improper spatial reflection was used. In fact the quartic map is even
under inversion, so replacing this proper-cubic statement by polar covariance
under all 48 transformations would require a different interpretation.

For a stipulated change in the fourteen class probabilities, with the
within-class birth laws and delta held fixed, the density depends only on
`M(p)=sum_a p_a M_a`. It therefore annihilates all seven odd opposite-pair
population changes. The six classical vector population moments have rank
six on this seven-dimensional odd space: three A imbalances and the three
B vector moments; the fourth odd B moment is an additional classical mode.
Since a trace-one real symmetric 3x3 matrix has five affine coordinates, the
thirteen-dimensional population tangent space actually has kernel dimension
at least eight. The even contrast changing total A mass against total B mass
is also invisible because either orbit average of M is I/3. The source need
not assert the kernel is exactly the displayed seven directions.

For independently prepared pairs this equality persists under tensor products
and any input-independent quantum channel or collective measurement. This does
not establish a statement for an arbitrary correlated late-time key ensemble,
for changed within-class distributions, or for several copies of the same
unknown fixed n. The latter preparation contains higher moments and is not
the tensor product of independently averaged pair densities.

At zero tilt, `rho_a <= I_4/2`: the singlet entry is 1/2 and M is positive
with trace one. Under the actual tilt,
`rho_{a,delta} <= (1+|epsilon|) rho_{a,0}`. For uniform fourteen priors, any
POVM consequently has correct-label probability at most
`(1+|epsilon|) tr(I_4)/(2*14)=(1+|epsilon|)/7`. This is an upper bound, not
an asserted optimal success probability.

The independent exact controls use open-class witnesses and finite even
stabilizer orbits. They test the symmetry and density identities, not numerical
values of the continuous spherical moments. In particular they do not replace
the source's continuous ensemble with a discrete one in the theorem.

## 2. A deterministic singlet-cover channel and a coherent filter

Let D have normalized bipartitely oriented singlet-cover columns D_M, and
G=D^dagger D. Every pair of covers has positive overlap. If a trace-preserving
quantum channel maps each orthonormal input `|M>` exactly to the pure output
`|D_M><D_M|`, its Stinespring isometry has the form

`V|M> = |D_M> tensor |e_M>`.

Input orthogonality gives `G_MP <e_M|e_P>=0` for M != P. Positivity of every
off-diagonal overlap forces the environment vectors to be mutually orthogonal.
Tracing that environment erases all input off-diagonals. Thus the unique
channel with these basis-pure outputs is

`Phi(rho)=sum_M rho_MM |D_M><D_M|`.

It is entanglement breaking between this auxiliary input and a reference,
even though each output cover contains internal two-qubit entanglement. The
argument does not assume D is injective. Orthogonal output markers restore an
isometry only by enlarging the specified output resource.

For two square covers, G has entries 1 on the diagonal and 1/2 off diagonal.
The incoherent output of an equal input superposition differs from the
normalized coherent sum by trace distance 1/4. More generally the difference
for two positive-overlap normalized vectors with overlap g is `(1-g)/2`.

The success operator `aD` is physical exactly when `|a|^2 G <= I`, so its
largest scalar normalization is `|a|^2=1/lambda_max(G)`. A failure operator
`sqrt(I-G/lambda_max)` completes an instrument with an orthogonal outcome
flag. The success probability on coefficient vector c is
`c^dagger G c/lambda_max`. It is undefined to condition on success when this
quantity vanishes; in particular vectors in ker(D) give probability zero.
Each basis input succeeds with `1/lambda_max`, while a top eigenvector succeeds
with probability one. Multiple success Kraus operators proportional to D
replace `|a|^2` by the sum of their squared coefficients.

An even cubic torus tiles into P=N^3/4 disjoint xy plaquettes. Choosing the two
coverings on each tile gives an actual principal Gram matrix
`[[1,1/2],[1/2,1]] tensor ... tensor [[1,1/2],[1/2,1]]`.
Its largest eigenvalue is `(3/2)^P`, so the full Gram has at least this largest
eigenvalue and this scalar filter has basis success at most `(2/3)^P`.
This does not bound a direct preparation of one chosen coherent state, or all
possible alternative target families or approximate operations.

## 3. Signed immutable-record fibers and the physical Gram metric

For K distinct antipodal key pairs, each full geometric matching has
`2^K K!` marked assignments. Weight an assignment by the product of the signs
of its records on the black sublattice. These signed, normalized fibers define
an orthogonal isometry U_-. Either one-step four-record plaquette rotation
exchanges the black/white roles of two pairs, so it preserves the sign and
bijects the complete fibers. The two senses each contribute half the supplied
flip amplitude. This proves the same geometric QDM intertwining as in the
orthogonal-fiber construction, now for the signed fiber.

For one key, an orthonormal SU(2) frame (u,v) obeys
`u tensor v-v tensor u=sqrt(2)|s>`. Expanding the K antisymmetrizations and
summing the K! assignments gives `V U_-|M>=sqrt(K!) D_M`. With arbitrary
representative phases, the product of the K frame determinants is a common
phase independent of the matching because each fixed record occurs once.
The claim is not a globally continuous choice of a Bloch-sphere spinor phase.

In computational spin coordinates a cover column has 2^K entries of magnitude
`2^(-K/2)`, with sign `(-1)^(number of black down spins)`. Overlaying two
matchings yields disjoint alternating loops, including doubled common edges.
There are two compatible spin assignments per loop and equal signs in both
columns. Thus `G_MP=2^(number of overlay loops-K)>0`.

If an ordinary Hermitian Hphys satisfies `Hphys D=D Hqdm` with Hermitian
Hqdm, then necessarily `[G,Hqdm]=0`. When G is invertible this condition is
also sufficient for the generally nonlocal operator
`D Hqdm G^-1 D^dagger`. For any Hermitian W, its compressed coefficient matrix
`G^-1 D^dagger W D` is self-adjoint in the G metric; it need not be symmetric
in ordinary coefficient coordinates. No arbitrary-graph independence of all
cover columns follows from the small examples.

The square Gram commutes with the supplied two-state QDM at all v,t; the
six-site ladder imposes v=t/2; the cube imposes two independent conditions
and permits only v=t=0 in that two-parameter QDM. These are conditions on the
specified Hamiltonian, not on the existence of all Hermitian operators.

## 4. Finite local-operator controls and their boundary

For a vertex star containing its possible nearest-neighbor partners, the
maximum-total-spin projector annihilates every singlet cover: the singlet
between the center and its partner is antisymmetric under that pair exchange,
whereas the fully symmetric star subspace is symmetric. Summing these positive
projectors gives a finite frustration-free parent, but this inclusion alone
does not identify its full ground space or give a volume-uniform gap.

The independent checker constructs exact integer singlet columns and physical
spin permutations in fixed magnetization sectors. With Dint unnormalized,
the leakage inner products are obtained from the small exact rational matrix

`(W_i Dint)^T(W_j Dint) - (Dint^T W_i Dint)^T
 (Dint^T Dint)^-1 (Dint^T W_j Dint)`.

Dividing the trace by 2^K gives squared Hilbert-Schmidt norms over normalized
cover columns. This implementation independently tests the asserted square,
six-site ladder, open cube, eight-site ladder and twelve-site patch values.
It is not a full Hilbert-space diagonalization of the twelve-site model.

On the cube, the positive parent has nineteen ground vectors, comprising ten
singlets and three spin-one multiplets, whereas the cover span has dimension
nine. The nearest-neighbor and plaquette-ring operators each leak from that
span, but the combination W_ring-2 W_NN cancels that leakage on this cube.
The corresponding cancellation on the six-site ladder uses coefficient -1.
The eight- and twelve-site residuals therefore matter: a cancellation on one
finite graph is not a graph-independent local realization theorem.

The square singlet-edge readout is 3/4 in the coherent equal-cover state, 5/8
in the equal incoherent mixture, and 1/2 as a classical matching occupation.
Those are three different specified observables/preparations. Finally,
uniformly averaging antipodal product pairs gives singlet weight 1/2 and three
triplet weights 1/6; it does not produce the pure singlet. This last observation
does not prevent a separately supplied entangling channel or filter.

The contextual papers are not used as theorem imports in this reconstruction.
No claim about their thermodynamic results is independently proved here.
