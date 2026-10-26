---
claim_id: block_of_eight_one_mode_sites_carries_a_gapped_dirac_band_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Conditional factorization and differentiable-eigenbranch velocity identities for a supplied eight-mode walk, with separate finite spectral diagnostics; no physical CAR realization or continuous-zone gap theorem."
upstream_dependencies: []
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A downstream physical consumer is not yet known; physical source and qubit implementation bridges remain open."
source_of_blocker_text: review_loop
reachability_to_target: "Formal factorization and eigenbranch identities do not establish physical fermions or a global gap."
conditional_surface_status: "Exact identities under supplied block-mode unitary and differentiable eigenbranch assumptions."
hypothetical_axiom_status: "none adopted; CAR/Fock reading is a supplied mathematical condition"
admitted_observation_status: "none"
claim_type_reason: "Explicit conditional factorization and derivative proofs; finite checks are separately scoped."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: "Conditional algebraic support; downstream consumer not yet known."
next_trace_action: "Prove any proposed physical implementation or continuous-zone bound before promoting those claims."
runner: scripts/block_of_eight_one_mode_sites_carries_a_gapped_dirac_band_2026_10_21.py
---

# Supplied eight-mode walk: factorization and eigenbranch velocity

Claim type: bounded_theorem.
Primary runner: `scripts/block_of_eight_one_mode_sites_carries_a_gapped_dirac_band_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and [candidate-law register](CANDIDATE_LAWS.md) are context only. A one-site M2(C) algebra does not select intersite canonical anticommutation relations (CAR), a Fock representation, or physical local fermion dynamics. No block relay rules or record-source identity are imported from the register.

## Supplied carrier and construction

Supply eight fermionic modes per labelled block with CAR, {a_i,a_j^dagger}=delta_ij and {a_i,a_j}=0, and their Fock representation. The one-particle sector has dimension eight; the full block Fock space has dimension 2^8. Number-preserving Gaussian second quantization of a one-particle unitary acts on its n-particle sector by the nth exterior power and preserves CAR. This is conditional mathematics, not a derivation from the qubit axiom. Locality below is locality in the chosen block modes; a nearest-neighbor qubit circuit has not been constructed.

Assign the eight amplitudes to four two-component blocks L,R,L',R', ordered as copy, chirality, spin. Supply U_L(K)=S_z S_y S_x, where S_i=cos(K_i)I-i sigma_i sin(K_i). The four blocks use U_L(K), U_L(-K), -U_L(K), -U_L(-K). The coin couples L to R and L' to R' with real angle m, and L to R' and L' to R with real angle M. Momentum convention, mode allocation, Pauli soldering, substep order, angles and step readout are supplied; no empirical mass or physical source input is assumed.

## Conditional factorization theorem

In this ordered basis define

    A_i = I tensor Z tensor sigma_i,
    C = exp[-i(m I tensor X tensor I + M X tensor X tensor I)],
    T = Z tensor I tensor I,
    U(K) = T exp(-i K_z A_z) exp(-i K_y A_y) exp(-i K_x A_x) C.

Each A_i is Hermitian and squares to I; C and T are unitary for real angles. Thus the displayed ordered factorization is unitary. The positive and negative chirality blocks of each shift are S_i(K) and S_i(-K); T supplies the negative copy signs. Each S_i gains minus under K_i+pi, so U_L(K+Q)=-U_L(K), Q=pi(1,1,1). Consequently this block form equals the momentum-shifted form as matrices for all real K,m,M, independently of finite eigenvalue sampling.

## Conditional velocity identity

For a normalized differentiable eigenpair U(K)u(K)=exp(-i omega(K))u(K), differentiate the eigenvalue equation and left-multiply by u^dagger U^dagger. Normalization and the eigenvalue equation cancel derivatives of u, giving

    partial_j omega = i u^dagger U^dagger (partial_j U) u.

Differentiating the ordered product cancels T and all shifts later than j. Since partial_j exp(-i K_j A_j)=-i A_j exp(-i K_j A_j), the result is the expectation of A_j in the state after C and the earlier shifts. This is the runner's staged mean step. A simple eigenvalue suffices locally; at degeneracy a chosen differentiable eigenbranch with compatible eigenvector is required. Arbitrary vectors in a degenerate eigenspace need not qualify. No claim that degeneracies occur only on axes is made. This identity does not identify a physical record source.

## Separate finite diagnostics

At m=.05,M=.5 the runner compares spectra at 50 seeded momenta and checks factorization at K=(.3,-.2,.5). Its 25³ grid minimum absolute eigenphase is .05 to the stated tolerance; a mesh minimum is only an upper bound on the continuous-zone infimum, not a global positive lower bound or a continuum Dirac dispersion proof.

The staged mean and tracked finite-difference eigenphase derivative agree within 1e-6 at exactly three momenta: magnitudes .04,.05,.03 along normalized (1,1,0), (1,2,3), (1,.15,.05), respectively. These are numerical illustrations of the conditional identity, not a proof of globally smooth band selection.

## Review record and open bridges

Original PR9841 head 03e4a72ee6ac111db8d9343c676419dcda117bae preserves the earlier overbroad wording. Unsupported candidate-register and unnamed-companion attributions, exact rotation/copy counts, global-gap headline and physical Dirac/source identification are withdrawn. Exact cubic covariance, removal of sublattice copies, matter content, physical masses, a physical CAR realization and a local qubit implementation remain unestablished. No audit standing is assigned.
