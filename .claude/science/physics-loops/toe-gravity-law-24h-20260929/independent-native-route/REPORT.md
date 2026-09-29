# Exact native collective-pair discriminator

This is conditional discovery, not a review, an audit verdict, or premise adoption. The source sweep uses main `e75578f7136401d4bd750131671aed9212c06291` and the open proposal revisions listed in `SOURCES.json`. The preceding matter-route artifacts are unchanged.

The limited constructive result is five collective two-particle operators on exactly one physical qubit per cubic vertex, carrying the cubic representation `E ⊕ T2`. Their propagation under a supplied attractive quartic law can be solved exactly. This particular law does **not** give a stable linear tensor phase: its dilute bands are flat or quadratic, and a full-carrier checkerboard state has negative energy well before the proposed pair gap closes. The negative-energy witness survives every positive nearest-neighbour density repulsion. It proves failure of the proposed vacuum as a ground state, not dynamical decay of a number-conserving vacuum.

## 1. Actual source boundary and imports

The current axioms supply cubic physical sites, one-site `M2(C)`, a fixed nearest-neighbour conditional distribution rule whose values are unspecified, and permanent records with content-determined readout. They explicitly do not select a Hamiltonian, time metric, basis, Born rule, formation rate or source/action identification. The three registered primitives read for the campaign—scale reference, kinetic isotropy and realized state—do not select the conditional law below. None is used to infer its couplings or ground state.

For this calculation supply:

1. The usual finite tensor product of one `C²` per physical vertex, with commuting factors at different vertices.
2. A common basis, `b_x=|0><1|_x`, `n_x=b_x†b_x`, the empty product vector `Ω`, and Hamiltonian time evolution. The number axis and state are choices; the axiom's algebra privileges neither.
3. The translation- and proper-cubic-covariant Hamiltonian (4) with positive parameters. Its interaction has support on the six neighbours of a center, with diameter two. It is finite range but is not a derivation of an elementary nearest-neighbour admissibility rule.
4. For the readout comparison only, the supplied projective occupation/`Z` readout and its standard quantum probabilities. Actual framework records are not identified with these hypothetical measurements.

There are no link-role qubits, oscillators, canonical field slots, continuum limits, Holstein–Primakoff substitutions, or large-spin approximations in the computation. The sense of *native* established here is carrier-native; law selection and physical readout remain separate.

## 2. Local collective operators

Use an infinite cubic lattice, or a periodic torus of side `L≥5`; the energy witness below uses even `L≥6`. Let

\[
d_i(x)=b_{x+e_i}b_{x-e_i},\qquad
a_i(x)=b_{x+e_i}-b_{x-e_i}.
\tag{1}
\]

Define five operators

\[
Q_{E1}=(d_1-d_2)/\sqrt2,\qquad
Q_{E2}=(d_1+d_2-2d_3)/\sqrt6,
\quad Q_{Tij}=a_i a_j/2\quad(i<j).
\tag{2}
\]

The five vectors `Q_A(x)†Ω` are orthonormal at fixed `x`: the `E` vectors use the three opposite-site pair words, while the `Tij` vector uses the four words with one site on axis `i` and one on axis `j`. Their supports are disjoint between the two sectors and between different `Tij`.

Proper signed permutations act on the `a_i` as a vector, permute the `d_i`, and therefore preserve the two-dimensional traceless diagonal subspace and three-dimensional off-diagonal subspace. Since `a_i²=-2d_i`, these are precisely the two cubic pieces of symmetric traceless quadratic expressions in the `a_i`, up to sector normalizations. Direct permutation matrices on all 15 shell pair words verify covariance under all 24 proper cube rotations. This constructs the restriction of the tensor representation to the cubic group; continuous rotation symmetry, helicity and gauge redundancy do not follow.

## 3. Exact translation overlap and spectrum

For a compatible torus momentum, set

\[
|A,q\rangle=|\Lambda|^{-1/2}
\sum_x e^{iq\cdot x} Q_A(x)^\dagger|\Omega\rangle.
\tag{3}
\]

An opposite-site pair has a unique center for `L≥5`. Thus the `E` overlap is `I2` and distinct centers have zero `E` overlap. An orthogonal-axis pair has two possible centers. For a given `Tij`, the overlap is one at zero displacement and `1/4` at each displacement `±e_i±e_j`; all cross-channel overlaps vanish. Consequently

\[
S(q)=\operatorname{diag}
\left(1,1,1+\cos q_1\cos q_2,
1+\cos q_1\cos q_3,1+\cos q_2\cos q_3\right).
\]

These identities are obtained by enumerating all matching pair words, not by a bosonic commutator replacement. The Laurent overlap has support inside `[-2,2]^3`; the exact enumerator checks the entire support.

Supply the law

\[
H=\mu\sum_x n_x
-g_E\sum_x\sum_{A\in E}Q_A(x)^\dagger Q_A(x)
-g_T\sum_x\sum_{A\in T}Q_A(x)^\dagger Q_A(x),
\qquad \mu,g_E,g_T>0.
\tag{4}
\]

In the exact two-particle sector, `Q_A(x)` maps a pair vector to a multiple of `Ω`, so `Q_A(x)†Q_A(x)` is exactly the outer product of its pair wavefunction. Fourier transformation gives a rank-at-most-five interaction at each `q`. Because the Gram is diagonal, its nonzero channel states have exact energies

\[
\epsilon_{E1}(q)=\epsilon_{E2}(q)=2\mu-g_E,\qquad
\epsilon_{Tij}(q)=2\mu-g_T(1+\cos q_i\cos q_j).
\tag{5}
\]

The orthogonal complement of all such states has energy `2μ`. Whenever `S_A(q)=0`, `|A,q>` is the zero vector, not a physical band with the value obtained by formally extending (5).

At the simultaneous `q=0` closing,

\[
g_E=2\mu,\quad g_T=\mu,
\qquad \epsilon_E=0,\quad
\epsilon_{Tij}=\mu(1-\cos q_i\cos q_j)
=\tfrac\mu2(q_i^2+q_j^2)+O(|q|^4).
\tag{6}
\]

There is no `|q|` dispersion. On the `z` axis the five bands are
`(0,0,0, μ(1−cos q_z), μ(1−cos q_z))` in the order `E1,E2,T12,T13,T23`. Under the formal tensor-component identification, both transverse traceless candidates `E1` and `T12` are flat there; the other three channels remain present. This is a direct exact-spectrum failure of this law, not an application of a harmonic comparator theorem.

A separate direct-action script constructs the actual pair states on 512 physical qubits (`L=8`), applies `12H` at (6), and checks 25 channel/momentum cases using Gaussian integers only. It includes `q` coordinates `0,π/2,π` and two null states. It is an author cross-check of (5), not an independent review.

## 4. Full-carrier energy counterexample

The two-particle computation alone cannot certify `Ω` as the physical low-energy state. On a completely occupied six-site shell,

\[
\left\langle\sum_{A\in E}Q_A^\dagger Q_A\right\rangle=2,
\qquad
\left\langle\sum_{A\in T}Q_A^\dagger Q_A\right\rangle=3.
\tag{7}
\]

Each expectation is the sum of squared coefficients of the normalized pair operators: distinct removed pairs are orthogonal. Literal 64-by-64 matrices on the complete six-qubit Hilbert space also check (7); no low-charge projection is used.

Let `|CB>` occupy every even-parity physical vertex and leave every odd-parity vertex empty on an even torus. Half the centers have a full shell and half an empty shell. Hence exactly

\[
\frac{\langle CB|H|CB\rangle}{|\Lambda|}
=\frac{\mu-2g_E-3g_T}{2},
\qquad \langle\Omega|H|\Omega\rangle=0.
\tag{8}
\]

Thus `2g_E+3g_T≤μ` is a necessary condition for the empty state to be a full-carrier ground state. Either proposed positive-coupling pair closing, `g_E=2μ` or `g_T=μ`, violates this condition already. At the common closing (6), the checkerboard energy is `−3μ|Λ|`. This is a variational upper bound on the ground energy, not a claim that the checkerboard is an eigenstate or the actual ground state.

For example, on the ray `g_E=2g, g_T=g`, the trial state first becomes negative at `g>μ/7`, while the two-particle gap closes only at `g=μ`. The trial-state threshold is not asserted to be a phase-transition location; other states may lower the energy sooner.

Adding arbitrary `W≥0` in

\[
H_W=H+W\sum_{\langle xy\rangle}n_x n_y
\tag{9}
\]

does not alter (8), because a checkerboard has no occupied nearest-neighbour pair. It also does not alter the five pair bands: every pair word in (2) has endpoint separation `2e_i` or `±e_i±e_j`, and is not a nearest-neighbour pair on the stated tori. Thus this density-repulsion repair does not rescue either the dilute spectrum or the proposed vacuum ground state.

Since `[H,Σn]=0`, `Ω` remains an exact stationary state. Equation (8) establishes an energetic obstruction to using it as a full-carrier vacuum, not spontaneous particle creation or decay under (4). Fixing total number to zero evades the energy comparison by excluding all excitations and does not produce the proposed tensor sector as a ground-state excitation theory.

## 5. A concrete fixed-readout obstruction for these operators

At one shell consider normalized vectors

\[
|\psi_\pm\rangle=(d_1^\dagger\pm d_2^\dagger)|\Omega\rangle/\sqrt2.
\tag{10}
\]

Their complete occupation-readout distributions coincide: each gives probability one half to each of the same two pair words. Every deterministic function of that record configuration therefore has the same distribution on the two states. But for `P_E=Σ_{A∈E}Q_A†Q_A`,

\[
\langle\psi_+|P_E|\psi_+\rangle=1/3,
\qquad \langle\psi_-|P_E|\psi_-\rangle=1.
\tag{11}
\]

The first value follows from overlap squared with `(1,1,−2)/√6`; the second state is exactly the first `E` vector. Consequently this particular fixed occupation readout cannot supply the coherent tensor-sector observable, even collectively from the full configuration distribution. A different record-formation instrument, an actual record-content encoding of phase-sensitive outcomes, or a separate observable bridge is needed. The framework does not itself prescribe the hypothetical occupation measurement, so (11) is not a general record no-go and is not a substitution for any original birth-law instrument.

## 6. Exact prior-source disposition

The route was selected after a main/open-proposal source sweep; exact-source checks continued through packaging. `SOURCES.json` binds the actual text used; hashes supply identity, not review coverage.

- **PR9363, photon-triplet and finite-slot notes:** the proofs assume local analytic positive harmonic kernels, specified tensor/photon carriers, and particular constraints. Their stated open scope includes nonharmonic phases, other composites and one-qubit-per-site realizations. The present quartic physical-site model is outside that harmonic calculation. Its failure is established by (3)–(8), not inferred from it.
- **Spin-half link-ring note, September 3:** exact ring algebra on supplied link-role qubits, small-width/finite-volume results, and an explicit fixed-`Z` coherence obstruction. No exclusion of collective modes on the physical-site qubits is inferred. Equation (11) is the corresponding witness calculated for the new operators, not a new general readout principle.
- **Compact-U1 Gauss note, September 3:** supplied link/rotor and fermionic carriers, integer-flux/Gauss-law construction and conditional Maxwell germ. It does not choose the physical-site law (4).
- **Native virtual-pair and eighth-diagonal notes, September 8:** actual full supplied edge-role qubits and anticommuting incident operators, a perturbative ring term and eighth-order diagonal patterns. They do not establish a full phase or an oscillator-free physical-site tensor mode. They were read as positive finite-carrier mechanisms and cannot be replaced by bare commuting `X` operators or a claimed RK equality.
- **New main composite-network studies:** the exact spin/comparator sign relation uses a four-dimensional composite local site (two qubits) and its projected sectors. The other new notes' charge-two band touchings are topological charges, not a spatial spin-two particle claim. The sign-identity source was read; the full topology studies were not independently rederived and are not exclusion premises here.
- **New main ring studies:** the `24³` energy-only moment bound is conditional on the model and measured quantities, while the fresh projection-window study shows susceptibility/curvature movement with projection time. These are live finite-volume evidence, not a settled thermodynamic tensor or photon phase. They do not match the carrier or law (4). No long ring simulation was run here.
- **Open PR9285:** its moving-record three-state classical law has low-density susceptibility bounds and conditional high-density long-range order. Static order does not provide the coherent Hamiltonian or tensor readout of (4).
- **Open PR9287:** the full argument fixes a walker placement's zero-transfer band momentum and constrains finite trigonometric hop stencils. Its interaction claim retains explicit regular-scattering/channel conditions. It is not a theorem about the quartic collective carrier here.
- **Older gravity-sign/emergent-diffeomorphism note:** its healthy tensor sign is conditional on the emergent gauge/diffeomorphism and source identification; neither follows from exhibiting the five operators (2).

The two-particle bound-neighbour source was also inspected: its supplied two-coin-walker and strong-binding law is different from (4). Targeted searches included both orders of collective/two-particle/bound-pair with tensor/spin-two/quadrupole, as well as nematic and pair-projector terms. No exact match was located in the inspected main/open-proposal surfaces. This is a bounded source search, not an exhaustive novelty claim.

## 7. What remains open, at what strength

The strongest conclusion is restricted to (4), its positive couplings, the proposed empty ground state, and the optional repair (9). It does not exclude non-number-conserving dynamics, differently shaped collective operators, genuine finite-density phases, other interactions, different record formation or another ground state of this same Hamiltonian.

A precise smaller next lemma would construct a finite-range, cubic-symmetric positive operator `V` that vanishes on the entire zero-, one- and two-particle sectors, then prove `H+V≥0` on every finite torus at (6). Such a lemma would repair the many-particle ground-energy defect while preserving the exactly established pair bands. It would require a new supplied interaction and does **not** repair the flat/quadratic dispersion; a nearest-neighbour two-body density penalty demonstrably cannot do the job. No existence or positivity result for such `V` is claimed here.

The stronger desired lemma—some native finite-qubit phase with two linear tensor modes, no unwanted gapless partners, actual record-readable tensor observables, a common source/action and the necessary gravitational identities—is essentially the original missing gravity target, not a useful assumption discharged by this construction. In particular, it must not be inserted under the name “collective tensor phase.” The present result supplies an exact discriminator and an explicit elementary collective carrier; it does not close that target.

## 8. Reproduction and evidence limits

Run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-native-route/collective_pair_exact.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-native-route/finite_torus_pair_action.py
```

Actual outputs are saved in the same directory. The first reported `PASS=5 FAIL=0` for the complete Laurent Gram, cubic covariance, full-shell operators, readout pair and product-state witness; the second reported `PASS=25 FAIL=0` for exact direct action and norms. `collective_pair_exact.json` and `finite_torus_pair_action.json` preserve the values. The analytic argument supplies the all-volume claims; a finite computation alone does not. No thermodynamic phase, continuum limit, observable bridge or independent review was run or claimed. `ARTIFACT_HASHES.json` identifies the handoff files.
