# Independent check of the specified native collective-pair law

**Scope and result, 2026-09-29.** I independently recover the five-channel Gram, the exact two-particle bands, the failure of the empty state to minimize the full-carrier energy at either proposed pair closing, and the fixed-occupation-readout coherence distinction. The checkerboard result can be strengthened: this product vector is an exact common eigenvector of every local interaction term, not merely a variational test vector. No normalization or domain error was found in the stated calculations. These results concern the supplied Hamiltonian and proposed empty-reference phase; they are not a general finite-`M2` obstruction, a determination of other phases of this Hamiltonian, or a formal review/audit PASS.

The checked author report is frozen as `AUTHOR_REPORT_START.md`, SHA256 `e62c163b75ec61ea92f76eef1869b95a0759d8cf4b0cbd18d8746b05978d70b0`. Later author edits are outside that byte-bound coverage. Pinned main is `e75578f7136401d4bd750131671aed9212c06291`. `SOURCE_BINDINGS.json` records exact source bytes and read coverage. No author Python implementation was imported, executed, or used as proof. The independent implementation is `check_native.py`.

## Carrier and source boundary

The source axioms specify physical cubic sites, a one-site `M2(C)` algebra, local admissibility, and records. They do not supply this tensor-product quantum dynamics, number basis, empty state, occupation measurement, Born probabilities, or a bridge identifying its operators with framework records or gravity. The checked registered primitives do not select this Hamiltonian either.

The landed link-ring and native virtual-pair/eighth-diagonal notes were checked for their actual carrier and operator scope. Their supplied link/edge-role qubits and, in the native perturbative models, anticommuting incident operators are distinct from the present physical-site pair construction. Their bounded finite-geometry/perturbative results are not phase premises here. I did not reconstruct their full spectral or perturbative proofs, the author's broader novelty survey, open-PR results, or large-volume ring simulations.

For the calculation itself, supply one ordinary tensor factor `C²` per physical vertex, operators `b_x=|0><1|`, `n_x=b_x†b_x`, and the empty product vector `Ω`. Different-site operators commute and `b_x²=0`. On the six-site shell around `x`, define

\[
d_i=b_{x+e_i}b_{x-e_i},\quad a_i=b_{x+e_i}-b_{x-e_i},
\qquad Q_{E1}=(d_1-d_2)/\sqrt2,
\quad Q_{E2}=(d_1+d_2-2d_3)/\sqrt6,
\quad Q_{Tij}=a_i a_j/2.
\]

There are no link-role auxiliary factors or oscillator substitutions in this construction. Its interaction is supported on a diameter-two shell. Finite range is established; an elementary nearest-neighbor admissibility law is not derived.

The five local pair states are normalized and mutually orthogonal. Their unnormalized coefficient lists have squared lengths `2,6,4,4,4`. Signed axis permutations send the `a_i` as a vector and permute the `d_i`; `a_i²=-2d_i`. Consequently the five-dimensional span is the cubic `E ⊕ T2` representation. All 24 proper signed permutations were checked on the literal shell pair words. This does not imply continuous rotations, helicity, a physical transverse-traceless identification, or gauge redundancy.

## Independent Gram and band derivation

Write `|x,A>=Q_A(x)†Ω`. An opposite-site pair has a unique center on the infinite lattice and on the stated tori `L≥5`. Its overlap with any orthogonal-axis pair vanishes. An orthogonal-axis pair has exactly two centers; the coefficient signs at those two centers agree. Direct matching therefore gives

\[
\langle 0,A|s,B\rangle=0\quad(A\ne B),
\]

with diagonal coefficient one at `s=0` for each channel, and additional coefficients `1/4` at the four shifts `s=±e_i±e_j` for channel `Tij`. There are no other nonzero coefficients. The independent program compares all 25 channel pairs at all 125 shifts in `[-2,2]^3`: 3,125 exact integer comparisons before normalization, with 17 nonzero coefficients. Matching endpoints from two unit shells forces every displacement coordinate into this box, so this check exhausts the infinite-lattice overlap, rather than sampling a truncation.

For `|A,q>=V^{-1/2}Σ_x exp(iq·x)|x,A>`, this implies

\[
S(q)=\operatorname{diag}(1,1,
1+\cos q_1\cos q_2,
1+\cos q_1\cos q_3,
1+\cos q_2\cos q_3).
\]

Define the supplied law, with positive parameters,

\[
H=\mu\sum_x n_x-g_E\sum_{x,A\in E}Q_A(x)^\dagger Q_A(x)
-g_T\sum_{x,A\in T}Q_A(x)^\dagger Q_A(x).
\]

On the exact two-excitation sector, each `Q_A(x)` maps into the one-dimensional vacuum space. Its squared operator is thus exactly `|x,A><x,A|` on that sector. Fourier decomposition and the diagonal Gram give, for every nonzero channel vector,

\[
\epsilon_{E1}=\epsilon_{E2}=2\mu-g_E,
\qquad \epsilon_{Tij}(q)=2\mu-g_T(1+\cos q_i\cos q_j).
\]

The orthogonal complement of the complete pair-channel span has energy `2μ`. A zero Gram entry means the corresponding Fourier vector is zero; it is not an additional eigenstate. This distinction was tested explicitly. The operator `Σ_E Q†Q` is a projector on the local two-particle opposite-pair subspace, but not on the full six-qubit carrier: its full-shell eigenvalue is two.

As a materially separate control, the program builds the actual sparse pair states on a `6³` torus with 216 physical qubits, applies each sector's interaction directly to pair bitstrings, and checks all cross-channel inner products. Eight momenta, in units `π/3`, test 40 channel cases, including four null vectors. Arithmetic is exact in `Q[ζ]/(ζ²−ζ+1)`; no floating-point eigensolver, bosonic commutator, or dense `2^216` representation is used. The torus side exceeds the shell-overlap diameter, so relative shifts in `[-2,2]^3` do not alias. The analytic overlap proof supplies the all-momentum/all-stated-volume conclusion; the 40 cases are controls, not a substitute for it.

At `g_E=2μ`, `g_T=μ`, the nonzero channel vectors have `ε_E=0` and

\[
\epsilon_{Tij}=\mu(1-\cos q_i\cos q_j)
=\tfrac\mu2(q_i^2+q_j^2)+O(|q|^4).
\]

Along the `z` axis the ordered values are `(0,0,0,μ(1−cos q_z),μ(1−cos q_z))`, subject to the null-vector qualification. In particular the formal `E1,T12` transverse-traceless pair is flat on that axis. The proposed dilute modes are flat or quadratic near the common zero-momentum closing, not linear in momentum magnitude. This is a statement about excitations of the supplied empty reference, not a spectrum calculation around an unknown finite-density ground state.

## Full-carrier checkerboard: an exact eigenvector

Let `|F_shell>` fill all six neighbors. For any normalized pair annihilator `Q=Σ_w c_w b_w`, removing word `w` leaves exactly its two sites vacant. A subsequent pair creation can succeed only on the identical word. Thus

\[
Q^\dagger Q|F_{\rm shell}\rangle
=\left(\sum_w|c_w|^2\right)|F_{\rm shell}\rangle
=|F_{\rm shell}\rangle.
\]

The same operator kills an empty shell. This is an operator-action argument on the unrestricted hard-core carrier, not an expectation-only or low-occupation approximation.

On an even periodic lattice `L≥6`, fill exactly one parity sublattice. Half the centers have a full shell and half an empty shell. The checkerboard is therefore a common eigenvector of every individual `Q_A(x)†Q_A(x)` and every `n_x`, with

\[
N=V/2,\qquad \sum_{x,A\in E}Q_A^\dagger Q_A=V,
\qquad \sum_{x,A\in T}Q_A^\dagger Q_A=3V/2
\]

on this vector. Consequently

\[
H|CB\rangle=\tfrac{V}{2}(\mu-2g_E-3g_T)|CB\rangle,
\qquad H|\Omega\rangle=0.
\]

Thus `2g_E+3g_T≤μ` is a necessary condition for the empty state to be a ground state of the unrestricted carrier. Either positive-coupling pair closing violates it. At the common closing the checkerboard energy is `−3μV`; on the ray `g_E=2g,g_T=g`, it is already negative for `g>μ/7`, while the pair gap closes at `g=μ`. Neither the threshold `μ/7` nor the checkerboard is asserted to locate the actual phase transition or actual ground state. An exact excited-state eigenvector can still provide a strict variational upper bound on ground energy.

The independent local 64-state action and global `6³` action both verify these statements. For `μ=1,g_E=2,g_T=1`, the global checkerboard has `N=108`, sector sums `216,324`, and energy `−648`. As an additional control the completely filled state has `N=216`, sector sums `432,648`, and energy `−1296`; it too is a common eigenvector. No exhaustive many-body diagonalization was attempted or needed.

Every nearest-neighbor bond contains at most one occupied checkerboard site. Adding `Σ_<xy> W_xy n_x n_y` therefore leaves its action and energy unchanged, even for arbitrary nonnegative bond coefficients. The homogeneous repair in the author report is included. Every pair word in the five channel states also has separation `2e_i` or `±e_i±e_j`, never nearest-neighbor on these tori, so that penalty leaves the five pair bands unchanged. It can change the energies of other two-particle states; the `2μ` complement statement above refers to the unmodified Hamiltonian.

Number is conserved, and the vacuum remains an exact stationary eigenstate. The result is an energetic obstruction to selecting it as a full-carrier ground state, not spontaneous decay or particle production. Restricting to total number zero removes the energy comparison by excluding the proposed excitations as well. All-volume statements use the explicitly supplied finite-torus family; no thermodynamic phase construction is claimed.

## Coherence and the specified readout

The normalized vectors `ψ±=(d_1†±d_2†)Ω/√2` have the same complete occupation distribution: probability `1/2` on each of two identical pair words. On the three-dimensional opposite-pair subspace,

\[
P_E=\sum_{A\in E}Q_A^\dagger Q_A
=I-|u\rangle\langle u|,\quad u=(1,1,1)/\sqrt3,
\]

and hence `⟨ψ+|P_E|ψ+⟩=1/3`, `⟨ψ−|P_E|ψ−⟩=1`. These fractions and the equality of readout distributions were independently checked using literal qubit operators. Any fixed state-independent classical postprocessing of that single-time occupation record has the same distribution on both states and cannot determine this observable on all states. The conclusion extends from deterministic to randomized postprocessing, since applying the same stochastic map preserves equal input distributions.

It does not forbid phase-sensitive instruments, another basis, an intervening known quantum evolution, or temporal readout protocols. Nor does it identify the hypothetical occupation measurements with the framework's actual permanent records. The landed fixed-`Z` coherence argument has the same type of limitation; the new witness is reconstructed for these particular operators.

## Evidence and remaining limits

The computation was priced as 64 local basis vectors, 24 cube rotations, a few thousand overlap comparisons, and sparse two-particle operations on 216 sites: below 200 MB and one minute expected, with no many-body diagonalization. Actual completed run: 6.892 seconds, single-thread environment, all exact assertions satisfied. Deadline and stop sentinel were checked before computation; no stop request was present. Outputs are `results.json` and `results.txt`. Reproduction from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-native-check/check_native.py
```

The author report's opening should be read narrowly as failure of the proposed empty-reference tensor phase. A claim excluding every stable linear tensor phase of this Hamiltonian, or of general native `M2` laws, is not established. Its detailed concluding limits already preserve other ground states, finite-density phases, other interactions and other record protocols. The statement that the checkerboard calculation does not claim eigenvector status is conservative, but can be strengthened by the exact action above. No additional error was found in the specified Gram, bands, energy, or readout formulas.

New many-particle stabilizers, changed interactions or different vacua require a separate calculation. Exhibiting a cubic five-component collective carrier does not close the missing continuum symmetry, tensor-only mode content, observable, source/action, or gravitational identity bridges. `MANIFEST.json` binds this check's evidence; it confers no formal review status.
