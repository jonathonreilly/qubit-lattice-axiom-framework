# Supplied Two-Magnon Sectors: Cycle Translation and Dispersive Bloch Witnesses

**Date:** 2026-10-23
**Type:** bounded_theorem
**Status:** conditional mathematical construction and finite numerical diagnostics; independent audit authority unchanged.
**Primary runner:** `scripts/two_magnon_sector_cycle_and_bloch_witness_2026_10_23.py`
**Cached runner output:** [`logs/runner-cache/two_magnon_sector_cycle_and_bloch_witness_2026_10_23.txt`](../logs/runner-cache/two_magnon_sector_cycle_and_bloch_witness_2026_10_23.txt)

## Object and boundary

Supply a one-particle basis `|x>` and an unordered, distinct-pair basis
`|{x,y}>`. On the finite `L=4` periodic cubic lattice, `N=64`, let
`H1=C^N`, `H2=C^(N(N−1)/2)` and define
`S−|{x,y}>=|x>+|y>`, `S+=(S−)†:H1→H2`.
These are the two displayed sector maps only. No map from `H2` to `H3`,
all-sector SU(2) representation, full tensor-algebra automorphism or physical
particle identification is constructed. Infinite-lattice statements below use
`ell²` of unordered pairs and finite-support lowering identities explicitly.

This positive construction illustrates why the displayed lowering constraint
alone leaves room for pair-sector motion. It does not evade or strengthen the
conditional all-sector theorem in
[SU(2) qubit-QCA rigidity](SU2_EQUIVARIANT_ONE_QUBIT_QCA_TRANSLATION_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-10-21.md).
That theorem assumes a strictly local automorphism, exact unit translations and
global SU(2), which are not supplied by the present sector operators.

## Finite-sector decomposition and corrected phase

For `N≥3`, `S−(S−)†=(N−2)I+J`, with `J` the all-ones matrix: diagonal entries
are `N−1` and off-diagonal entries are one. Its eigenvalues are `2N−2` on
the uniform vector and `N−2` on its orthogonal complement. Thus `S−` is
surjective and

`H2 = im S+ ⊕ ker S−`, with dimensions `N` and `N(N−3)/2`.

For supplied `U1=e^(i phi)I`, the intertwiner is
`U2 S+ = S+ U1 = e^(i phi) S+`, **not** `e^(2i phi) S+`.
The adjoint lowering relation and unitarity permit an arbitrary unitary on
`ker S−` with this fixed scalar on `im S+`. This freedom is only for the
specified `H1/H2` relations. It imposes no constraints involving higher sectors.
At `phi=pi`, the correct and former formulas give `−S+` and `+S+`, a direct
counterexample to the old phase claim. The numerical witnesses retain `phi=0`.
For a monomial pair map fixing singles, the distinct supports of
`S−|{x,y}>` identify the unordered pair and rule out a nontrivial pair permutation;
that restricted observation does not exclude nonmonomial unitaries.

## Alternating cycle and translation operator

Use the six vertices, in order,
`(0,0,0),(1,0,0),(1,1,0),(1,1,1),(0,0,1),(1,−1,0)` and

`psi = (1/sqrt(6)) Σ(i=0,…,5) (−1)^i |{v_i,v_(i+1 mod 6)}> `.

Each vertex occurs twice with opposite coefficients, so its finite-support
lowering sum is zero. The six edge differences are pairwise distinct up to
sign. Two translated edges can therefore coincide only when they have the
same edge type and zero relative translation. It follows that the translated
vectors `psi_x` form an orthonormal family on `Z³`.

Let `V:ell²(Z³)→H2` send `|x>` to `psi_x`, let `T` translate `|x>` to
`|x+e3>`, and put `P=VV†`. Then
`W_g=V T V†+(I−P)` is unitary: the first summand is unitary on `ran V` and
the second is the identity on its orthogonal complement. Translation covariance
of V makes W_g translation invariant. Its orbit satisfies
`W_g^t psi_x=psi_(x+t e3)`. It fixes pairs with separation `|rho|∞≥2`,
since the cycle contains only near pairs. Lowering cancellation holds on the
finite-support vectors on which the formal infinite-lattice lowering map is
used; no bounded all-sector SU(2) operator is inferred from that notation.

The runner independently assembles the finite torus matrix `W_g` and checks
unitarity, both `H1/H2` intertwiners, fixed far pairs, translation invariance,
and four steps of the cycle orbit. “One lattice site per step” describes this
chosen sector orbit, not a physical signal velocity.

## Cubically covariant positive generator and Bloch witness

For the 24 proper signed-permutation rotations `O`, define
`H_O=Σ(R∈O)Σx |pi_R psi_x><pi_R psi_x|`.
Each inner sum is an orthogonal projection, so the infinite-lattice operator
is positive, bounded by 24, and self-adjoint. Permuting rotations/translations
shows its covariance. On the finite torus its range lies in `ker S−`.
Therefore `W_O=exp(i theta H_O)`, `theta=.3`, is unitary and is the identity
on `im S+`; its displayed lowering intertwiner follows. Neither this
exponential nor its finite pair-coordinate hopping generator is asserted to
be a strictly local QCA on the full qubit algebra.

There are 13 near-pair relative-position representatives modulo sign. The
runner assembles their `13×13` Bloch matrix from the rotated cycle amplitudes.
For an exact reconstruction, canonically orient each rotated edge as
`{b,b+rho}` and set `v_R(K)_rho=Σ_edges (-1)^i exp(i K·b)/sqrt(6)`.
Up to the harmless Fourier sign convention,
`H(K)=Σ_R v_R(K)v_R(K)†`. Existing independent exact controls obtained
`tr H(0)^2=340/3` and `tr H(pi/2,0,0)^2=892/9`; distinct second moments
establish that the eigenvalue multiset is not constant. The earlier attempted
comparison at `(pi,0,0)` gave equal moments and remains a preserved failed
discriminant, not supporting evidence. These exact controls were not derived
by importing the author's hopping-table implementation.

The retained numerical fixtures compare the `4³` Bloch grid to all 832
near-pair torus eigenvalues, sample 41 points on `(k,0,0)`, and find a band
width exceeding the unchanged `.1` gate. They also compute forward differences
with `h=1e−5` at 200 seeded random momenta (`seed=7`), separately for each
coordinate. The historical largest sampled absolute eigenphase-derivative
**component** is about `.701` at theta `.3`. This is not a global maximum,
vector-norm speed bound or physical velocity. Ordered eigenvalues and finite
differences alone do not certify differentiability at crossings.

## Evidence and recovery scope

The canonical primary preserves all 19 original numerical predicates and their
thresholds: exact-domain identities are distinguished from floating-point
checks. It uses the existing canonical Counter helper, fails its process when
a predicate fails, and accepts an optional exclusive `--log` file; default
execution writes only standard output. No optimizer or historical search runs.

This extracts only the positive sector argument from PR9831 original
`e294c1dc745dad0c95b4c8688efc6f3f0be03613`, under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C9/`:
`NOTE.md`, `scripts/c9_02_sector.py`, `scripts/c9_common.py` and
`logs/c9_02_sector_run1.txt`. The old phase formula, broad velocity headline,
failed/partial classifier searches and original logs remain recoverable there.
The existing core theorem, C7 correction and their review scopes are unchanged.
No campaign PASS, audit grade, full physical action selection or novelty claim
is imported. Independent affected confirmation belongs to the original reviewer.
