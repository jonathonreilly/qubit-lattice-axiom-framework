# Independent check of the full-sphere visibility criterion

2026-10-12. Scoped mathematical/source review by the independent reviewer.
This is not a formal audit, empirical fit, landing authorization, or a review
of the original sphere-threshold theorem.

**Disposition: PASS for the stated conditional continuum criterion and the
exact finite-witness norm bound.** No consequential mathematical or source
defect was found in the complete reviewed note and program. The proposed
candidate's witness expectation remains numerical evidence, including the
independent high-precision replay below. It has not been interval-certified.

## Exact source and scope

The complete sources read were:

- `DIRECT_VISIBILITY_CRITERION.md`, SHA256
  `b7cfa158462874462fea1b91f13b70792899ff473541ea220bde8d2d304d49d3`.
- `direct_visibility_check.py`, SHA256
  `864f2d5cec34c3f36e98da398d6c6df27cb6d21a41d30f095edefe8e8fc15227`.
- Runtime `FREEZE.json`, SHA256
  `e22afbb73bd0f46770610ec2d41fda5e7bdae0907935be98f7a41406e36f1786`.
- Runtime `RESULTS_v1.json`, SHA256
  `b78309cf5b00881e182af21e126924195e660102708e126c113381436377eba9`.

The final declared 300-setting artifact `grid_12_v1.npz` was read and checked,
SHA256 `6311396ee331802bdf67757cd312e9d0f51ecc35a7bbd22f4d93b6769adbcdeb`.
The smaller grid result rows were inspected but their integer products were
not separately replayed. They are unnecessary to certify the fixed final
grid. No original sphere-threshold proof, resource obstruction, composition
packet, observational dataset, or physical source model is promoted by this
review. None is a premise of the argument checked here.

## Necessity, including the infinite-dimensional point

Let the normal state on the separable tensor product be represented by a
density operator and purify it in a separable ancillary space. For projective
binary observables, the vectors `(A(a) tensor I) psi` and
`(I tensor B(b)) psi` have norm one and real inner product equal to the
correlation. For binary POVMs, use the Hermitian contractions and obtain norms
at most one. Assigning the purification ancilla to one side does not change
the correlation. Weak operator measurability suffices: its vector functions
are strongly measurable in a separable Hilbert space. The usual stronger
interpretation of measurable observables also suffices.

For a bounded, strongly measurable vector field u on the probability space
S2, its integral map U from real L2 to the realified Hilbert space satisfies

    sum_n ||U e_n||² = integral ||u(a)||² dmu(a).

One way to justify this without assuming the conclusion is to expand in a
countable orthonormal basis of the target space, apply scalar Parseval to
each coordinate of u, and apply Tonelli to the nonnegative double sum.
Consequently U and W are Hilbert-Schmidt and U*W is trace class with norm
at most one. This does not first assume an absolutely summable Legendre
series. It proves the needed summability from the realization.

With normalized area measure, the addition formula gives eigenvalue
`-V a_l/(2l+1)` on the degree-l harmonic space, whose dimension is `2l+1`.
Continuity of f gives a square-integrable isotropic kernel; the complete
harmonic decomposition is available before trace-class summability is known.
Taking the trace norm therefore gives precisely `V sum_l |a_l| <= 1`.
Neither fair marginals nor finite local dimension were smuggled into this
direction. The harmonic multiplicity and normalized area factors are correct.

## Sufficiency and one state for the whole sphere

Absolute summability and `|P_l(c)| <= 1` make the proposed series uniformly
convergent. Its coefficients agree with f; L2 completeness and continuity
give equality everywhere, rather than merely almost everywhere.

For l >= 1, an explicit supply of the required `2l+1` Clifford generators is

    Gamma_(2j-1) = Z^(tensor(j-1)) tensor X tensor I^(tensor(l-j)),
    Gamma_(2j)   = Z^(tensor(j-1)) tensor Y tensor I^(tensor(l-j)),
    Gamma_(2l+1) = Z^(tensor l),                     j = 1,...,l.

They are traceless Hermitian involutions in dimension `2^l` and anticommute.
The real, normalized degree-l harmonic feature has norm one and pair inner
product P_l. Thus its Clifford combination is also a Hermitian involution.
The maximally entangled identity
`<Phi_d| A tensor B |Phi_d> = Tr(A B^T)/d` fixes the transpose and sign in
the proposed Bob observable. Both signs of a_l are handled correctly.
The separate two-dimensional l=0 construction correctly keeps its marginals
fair. A scalar one-dimensional observable would not do so.

On the two countable local direct sums, the vector formed from matching
sectors with amplitudes `sqrt(V |a_l|)` and the optional product sector has
norm one. It is an ordinary vector state and hence normal. Block-diagonal
bounded observables suppress every cross-sector matrix element. They are
projective; their setting dependence is strongly continuous because each
finite block is continuous and the squared vector tail controls the infinite
sum uniformly. This supplies a single state and observable family for all
settings, not a separate realization for each finite table. No finite entropy,
energy, dimensional economy, or dynamical source claim follows.

## An independent polynomial and explicit quantum control

The reviewer chose

    f(c) = P0(c)/4 + P1(c) - P2(c)/4.

Its absolute coefficient sum is exactly `3/2`, so the asserted threshold is
`V = 2/3`. A GL3 polar grid with seven equally spaced azimuths integrates all
products of harmonics through degree two exactly. In exact arithmetic the
weighted kernel has eigenvalues `1/4` once, `1/3` three times, `-1/20` five
times, and zero twelve times. The trace norm is therefore exactly `3/2`.
The discrete sign operator built from the degree-0, degree-1 and negative
degree-2 harmonic projectors has norm one. At V = 7/10 its candidate witness
value is exactly `21/20`, supplying an analytically known finite failure.

The separate implementation constructs the degree-two feature explicitly
from x, y, z, uses Pauli tensor matrices, builds the full pure sector state
and directly evaluates the tensor-product observables. At V = 1/2 and 2/3,
the local dimension is ten and all marginals are zero. Maximum correlation
errors were `1.67e-16` and `2.22e-16`; the maximum projectivity error was
`4.44e-16`. The polynomial spectrum error was `1.67e-16`. This tests signed
sectors, the l=0 sector, the uncorrelated remainder, multiplicities and the
transpose convention independently of the author's candidate implementation.

## Finite witness certification and numerical candidate replay

For arbitrary binary quantum correlations, the weighted factor matrices have
Frobenius norms at most one. Nuclear-norm duality gives the claimed bound for
every fixed real contraction S. It requires neither isotropy nor fair
marginals. The source uses G rather than C = -V G to choose the witness; the
absolute value in the bound makes this overall sign immaterial.

The reviewer recomputed every entry needed for the final integer Gram bound
using scalar Python integer inner products and triangular traversal, without
importing the author program or using its object-matrix multiplication. With
the stored integer matrix J and denominator r:

    max_i sum_j |(J^T J)_ij| = 100000001528224292312,
    r = 10000000077,
    r² = 100000001540000005929.

The spectral-radius bound by the maximum absolute row sum proves
`||J/r||_op <= 1` exactly. Probability numerators are positive integers and
sum exactly to the recorded denominator `1000000000000`. The certified
object uses these exact rational probabilities and their exact square roots;
the floating `witness_coefficients` array is a convenient approximation,
not a second independent exact certificate for literal rounded coefficients.
Any apparatus implementation still needs to account for coefficient and
experimental uncertainties.

A different 65-digit calculation generated the analytic GL12 roots, grouped
the fixed integer coefficients by azimuth difference, and evaluated the
candidate via `tanh(atanh(2 asin(c)/pi)+k*c)`. It gave

    B(1)    = 1.105789006518142748876929880391362369454700284354078375337894941,
    B(.95)  = 1.0504995561922356114330833863717942509819652701363744565710001939,
    B(cos)  = 0.99999999165835983220977586247588222398921979583713507095225891456.

The first differs from the independent floating replay by `3.33e-15`.
This is a numerical consistency check with a large apparent excess at .95,
not an interval proof of that excess. The source correctly keeps that limit
explicit. Passing at .9 does not prove quantum membership or determine the
continuum critical visibility. No real experiment has been evaluated here.

## Reproduction and remaining obligations

Run the adjacent `independent_visibility_check.py` using `/usr/local/bin/python3`.
It imports no author helper, writes only its assigned runtime review directory,
and checks the reviewed source hashes before accepting results. The completed
run used Python 3.12.8, NumPy 2.4.1 and mpmath 1.3.0 and exited zero.
`CHECKS_v1.json` in the runtime review directory preserves the actual results
and exact sources. Its output is not overwriteable by the runner.

The theorem is conditional on the stated ordinary tensor-product quantum
model and measurable separable normal realization. This review does not
establish the conditioned candidate's entire Legendre tail, its exact
critical visibility, any empirical exclusion, physical resource adequacy,
novelty, or a connection to a theory of everything. Future changes to the
reviewed statement, premises or code require checking the affected source.
