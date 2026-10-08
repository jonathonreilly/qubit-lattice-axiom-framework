---
claim_id: supplied_ferromagnet_order_and_low_temperature_normalization_bounded_theorem_note_2026-10-08
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied nearest-neighbor Pauli ferromagnet H_J=J sum sigma_x dot sigma_y on Z^3 with J<0, the exact basis/coupling/time dictionary to the published Lean-covered spin-half Heisenberg model gives convergent infinite-volume dynamics and, at every sufficiently large inverse temperature, a translation-invariant KMS state with Pauli magnetization at least 1/4. The finite bond, one-magnon and Gaussian-moment identities are proved locally. Later Bloch-law coefficients are separate consequences conditional on the named companion-paper asymptotic, not covered by the imported Lean theorem."
upstream_dependencies: []
runner: scripts/supplied_ferromagnet_order_and_low_temperature_normalization_2026_10_08.py
---

# Order and normalization in a supplied Pauli ferromagnet

**Date:** 2026-10-08. **Claim type:** bounded_theorem.
**Current status:** conditional-support for an explicitly supplied Hamiltonian.

The phase question for one supplied corner now has a precise mathematical
answer: for every fixed J<0, at all sufficiently large inverse temperatures
there exists a translation-invariant equilibrium state with expectation of
the standard Pauli Z at least 1/4. This uses the exact published Lean-covered
spontaneous-magnetization theorem as accepted external support and proves
its model dictionary here. A repeated external formal-verification campaign
is not a prerequisite for this application.

The relevant earlier repo discussion is
`DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md`
at `ed04ee2736b5bddb4e9064966505e3c3dfe003de`. Its scope states:
“No ground state, phase, excitation or physical identification of any coupling
is claimed. The sign and size of `J`, `K`, `D` are free.” This note addresses
the equilibrium-order part for the supplied J<0 isotropic corner only.
The complete model is redeclared below; the earlier classification is provenance,
not an assumed scientific lemma.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: dynamics_clause_covariant_nearest_neighbour_two_qubit_generators_heisenberg_under_possibility_covariance_three_couplings_under_full_soldering_bounded_theorem_note_2026-09-24
target_blocker_text: "No ground state, phase, excitation or physical identification of any coupling is claimed. The sign and size of J, K, D are free."
source_of_blocker_text: null
blocker_source_section: "What this does not do, third item"
blocker_source_revision: "ed04ee2736b5bddb4e9064966505e3c3dfe003de"
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Supplied isotropic ferromagnetic Hamiltonian and quantum equilibrium interpretation"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "An explicit model theorem using a matched external mathematical import"
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Review this bridge; consider its basis, KMS scaling and finite identities for Lean verification during later audit."
```

## Model, imported statement and provenance

At every x in Z^3 put M_2(C), with standard Pauli matrices
X=[[0,1],[1,0]], Y=[[0,-i],[i,0]], Z=diag(1,-1).
The observable algebra is the norm completion of the union of finite tensor
matrix algebras, with the usual identity embeddings. For a finite set Lambda,
let E(Lambda) contain each unordered nearest-neighbor bond once and set

    H_J,Lambda = J sum_{ {x,y} in E(Lambda) } sum_{a=1}^3 sigma_x^a sigma_y^a,
    J<0, kappa=-4J>0.

Finite dynamics is alpha_J,Lambda,t(A)=exp(i t H_J,Lambda) A exp(-i t H_J,Lambda).
Inverse temperature beta is in these Hamiltonian/clock units, with hbar=k_B=1.
States are positive normalized continuous complex-linear functionals on the
quasilocal algebra. Translation invariance means invariance under all lattice
translations. A beta-KMS state for alpha is a state for which, for every A,B,
a bounded continuous function F on 0<=Im z<=beta, analytic in its interior,
obeys F(t)=omega(A alpha_t(B)) and
F(t+i beta)=omega(alpha_t(B) A). These are mathematical supplied objects;
no preparation, temperature calibration, probability readout or dynamics
selection follows from the four framework axioms or their primitives.

All external links below are pinned to OpenAI/math revision
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

| Mathematical input | Exact support and role |
|---|---|
| Low-temperature order and norm convergence of dynamics | Accepted published Lean-covered theorem [OAI.Heisenberg.spontaneous_magnetization](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MathematicalPhysics/Heisenberg/Main.lean), selected by [Heisenberg.json](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Heisenberg.json). |
| Definitions matched by that theorem | [Comparator statement and full definitions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Heisenberg.lean). The comparator's `sorry` is a challenge slot; the selected production module contains the proof. |
| Scope of formal coverage | [Family271 scope](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/271.md): spontaneous magnetization/KMS and dynamics convergence; not the later Bloch coefficients or spherical law. |
| Later asymptotic, used only in the separately conditional consequence below | [First lattice correction](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/first-lattice-correction-bloch-law.pdf). Its many-body expansion is an explicit paper premise for that consequence. |

The selected formal theorem uses natural dimension d>=3 and integer ell>=1,
with spin S=ell/2. Its Hamiltonian has unit ferromagnetic coupling,
H_0=-sum_{ {x,y} } S_x dot S_y. It establishes DynamicsConverges and some
beta_0>0 such that each beta_ext>=beta_0 has a translation-invariant beta_ext-KMS
state omega_ext with real expectation omega_ext(S_z(0))>=ell/8=S/4.
The comparator permits only `propext`, `Quot.sound` and `Classical.choice`.
This note accepts that published mathematical result; it does not claim a new
local Lean/comparator run or a local audit of its transitive proof library.

## Theorem 1: exact basis, coupling and KMS dictionary

For the model above, the infinite-volume dynamics exists as the norm limit of
finite-box dynamics. There is beta_c(J)>0 such that every beta>=beta_c(J)
admits a translation-invariant beta-KMS state omega_J with

    omega_J(Z_0) real and omega_J(Z_0)>=1/4.

Proof. Specialize the external theorem to d=3, ell=1. Its local matrix units
represent each finite tensor matrix algebra faithfully, with its usual
operator norm; their norm closure is therefore the same quasilocal algebra
up to the canonical isometric star isomorphism. Its magnetic levels
are k-ell/2, ordered k=0,1, so its one-site matrices are

    S_x=X/2, S_y=-Y/2, S_z=-Z/2.

Let u=X. Direct matrix multiplication gives u S_a u*=sigma_a/2 for each a.
For a finite support Lambda, tensor conjugation by u on each site defines
a unital isometric star automorphism Phi_Lambda. These maps agree under the
identity embeddings, so extend continuously to a star automorphism Phi of
the quasilocal algebra. This constructs the map on local algebras and their
completion; it does not posit an infinite tensor-product unitary in a chosen
reference Hilbert space. Phi commutes with every lattice translation.

Each unordered bond occurs once in both conventions. Thus

    Phi(H_0,Lambda)=-1/4 sum_{ {x,y} in E(Lambda) } sigma_x dot sigma_y,
    H_J,Lambda=kappa Phi(H_0,Lambda), kappa=-4J>0.

Functional calculus or the norm-convergent exponential series gives
alpha_J,Lambda,t=Phi alpha_0,Lambda,kappa*t Phi^{-1}. Since Phi is isometric,
the imported dynamics convergence gives
alpha_J,t=Phi alpha_0,kappa*t Phi^{-1} on the completed observable algebra.

Take beta_c(J)=beta_0/kappa and beta>=beta_c(J). Apply the external theorem at
beta_ext=kappa beta to obtain omega_ext. Define omega_J=omega_ext composed
with Phi^{-1}; positivity, normalization and translation invariance follow.
For A'=Phi^{-1}(A), B'=Phi^{-1}(B), let F_ext be its beta_ext-KMS function.
Then F_J(z)=F_ext(kappa z) maps the closed beta strip to the closed beta_ext
strip and has the needed boundedness, continuity and analyticity. Its lower
and upper boundary identities are exactly the beta-KMS identities for alpha_J.
Finally Phi(S_z)=Z/2 and the imported lower bound is 1/8. Consequently
omega_J(Z)=2 omega_ext(S_z)>=1/4, with zero imaginary part. QED.

This is an existence statement for an infinite-volume ordered KMS state.
It gives no numerical critical temperature, uniqueness, dynamical
thermalization or preparation protocol. A finite-volume zero-field Gibbs
state has zero one-site magnetization by spin-flip symmetry; this does not
contradict the infinite-volume existence statement. Other signs of J and
compass/Moriya terms are separate models. These scope statements do not assert
that those models lack ordered phases.

## Theorem 2: excitation normalization and exact Gaussian coefficient

In the one-down-spin sector of the periodic cubic Pauli model, measured from
the all-up energy, the Hamiltonian is -2J times the graph Laplacian. Hence on
the infinite lattice its one-magnon dispersion is

    epsilon(k)=-4J sum_{a=1}^3(1-cos k_a)
              =D |k|^2 - (D/12) sum_a k_a^4 + O(|k|^6), D=-2J=kappa/2.

Proof. A bond containing the flipped site has diagonal Pauli-dot entry -1
instead of +1 and off-diagonal exchange entry 2. A bond not containing it
has unchanged diagonal entry +1. Subtracting the all-up energy gives diagonal
-2J times the degree and off-diagonal 2J on each incident edge. This is
-2J times the graph Laplacian. Fourier characters diagonalize translations,
giving the displayed expression; Taylor's cosine series gives its expansion.
The runner separately assembles this sector from the full 4x4 bond operator
on a 3x3x3 periodic graph and compares every entry to the graph Laplacian.
No full 2^27 matrix or finite-size inference about the thermal phase is used.

For a>0 the normalized one-dimensional Gaussian fourth moment is 3/(4a^2),
by integration by parts twice. Integrating the first-order term
(a/12) sum_i k_i^4 exp(-a |k|^2) gives 3/(16a) times the leading Gaussian
integral. We integrate this polynomial-weighted Gaussian, not an exponential
with a positive quartic tail. This is an exact Gaussian-moment
calculation; passing from this spin-wave expression to the interacting
many-body thermal magnetization is not established by that calculation. QED.

## Separately conditional Bloch-law consequence

Assume additionally the nearest-neighbor many-body asymptotic stated in the
October5 lattice-correction paper, including its thermodynamic-pressure and
positive-field-to-zero limits. Let m_sigma be twice that paper's spin-half
magnetization, after the basis identification above, rather than the zero
magnetization of a finite zero-field Gibbs state. Its normalization becomes

    1-m_sigma(beta)
      = zeta(3/2)/(4*pi^(3/2)) * (beta*(-2J))^(-3/2)
      + 3*zeta(5/2)/(64*pi^(3/2)) * (beta*(-2J))^(-5/2)
      + o(beta^(-5/2)).

The order is thermodynamic volume first, external positive field to zero
second, and beta to infinity last, with fixed J<0. Since Z=2S_z, the same field
term obeys -h_sigma sum Z=-h_S sum S_z with h_S=2h_sigma. The exact bond and
Gaussian calculations above check the conversion and coefficients; they do
not independently prove this paper's many-body remainder. Theorem1 does not
depend on this extra asymptotic premise. The production Lean scope listed
above does not include these later coefficients; no broader certification is
claimed from the family title.

## Reproduction, review and Lean audit targets

Primary runner: [exact checks](../scripts/supplied_ferromagnet_order_and_low_temperature_normalization_2026_10_08.py).
Paired output: [content-pinned cache](../logs/runner-cache/supplied_ferromagnet_order_and_low_temperature_normalization_2026_10_08.txt).
The runner uses Python and SymPy, reads no scientific input files, and checks
the basis orientation, bond coefficient, all finite commutator entries,
one-spin-flip operator, dispersion and Gaussian moment. Those checks do not
claim to execute an infinite-volume KMS state. The infinite conclusion uses
the accepted external theorem and the written dictionary proof.

The local bridge is new source work in this packet; global mathematical
novelty is not asserted. Independent source review is recorded in its branch
pack. No formal audit or retained status is assigned by this author note.

For later audit, prioritize Lean proofs of the one-site matrix/basis identities,
the consistent local-algebra automorphism, positive time/KMS-strip rescaling,
and application of `OAI.Heisenberg.spontaneous_magnetization` at d=3,ell=1.
The integer sector identity and rational Taylor coefficients are additional
small candidates. Any actual formalization should pin its toolchain, exact
theorem type, dependency revision, permitted axioms and compiler output.
Our new proof need not wait for that formalization before review or further
mathematical development.
