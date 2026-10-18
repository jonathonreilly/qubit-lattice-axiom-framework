# Fixed-height polynomial-box embedding and source check

Disposition: PASS for the proposed first N0 embedding and remainder/source power counting, with the explicit hypotheses below. This is not a completed proof of the subsequent dispersive normal form or global-ground selection.

Read TEN_LAYER_NEUTRAL_BOUND_PROOF.md and INDEPENDENT_LOCAL_NORMALFORM.md. The latter gives an actual fixed finite product of local unitaries, individually N-preserving finite-range retained coefficients, and a volume-uniform interaction-norm remainder. Constants may depend on fixed order and L=10, but not transverse R. Here write the chosen final absolute remainder as O(lambda^M R^2), regardless of whether the construction labels it order M or M-1.

## First embedding is genuinely volume-controlled

Encode each complete height-ten column by a reference spin s=Z_0 and nine independent bond-wall bits; the tenth periodic bond bit is fixed by their even-parity constraint. This is an exact on-column unitary coordinate identification. Full-column spin flip is logical X, and logical Z can be Z_0. The ancillary wall labels are untouched by these logical Pauli operators. Since height is fixed, completing the support of a local term to whole columns only enlarges its support by a fixed factor.

For each Hermitian local retained term d_X individually commuting with N, restrict it to no walls on the columns meeting its support and extend that logical operator by identity on the wall labels. Call this extension d_X^0. On input with no walls in those columns, N preservation forbids output walls: the term acts identically to its N0 restriction. Hence

 d_X-d_X^0=B_X(d_X-d_X^0)B_X,

where B_X projects onto at least one wall on the completed support. This sandwich, not merely agreement of diagonal expectations, is the key fact. It follows also on the left by Hermiticity. Since B_X is bounded by the sum of wall projectors there, summing local interaction norms gives the form inequality

 |<psi,(D-D_ext^0)psi>| <= C lambda <psi,N psi>.

D_ext^0 commutes with all wall labels and is an exact copy of D|N0 on the logical spins. After a common scalar subtraction, its operator norm is at most C lambda^4 R^2; there are no nonconstant lower-order N0 terms. Periodic columns have minimal nonzero N=2. Thus the retained full Hamiltonian separates the entire N0 band from N>0 by

 4-O(lambda)-O(lambda^4 R^2)

in units J. This is positive uniformly eventually for R~lambda^-p with p<2. Including the global remainder O(lambda^M R^2) preserves the separation and identifies the exact microscopic low band by a spectral projector. No assumption about a particular logical ground state enters this argument.

The norm bound and the sandwich require individually N-preserving retained local terms. A decomposition whose sum alone commutes with N should first be averaged termwise with the local N action. The inherited construction already permits this.

## Second bad-plaquette reduction

After division by lambda^4, the leading operator is a constant plus a positive multiple of the local integer Qbad. The same finite-order local averaging works because its plaquette projectors commute. Retained terms can be made individually Qbad-preserving and plane-symmetry invariant.

For a bounded-support term, enlarge the tested plaquette neighborhood by a fixed collar. On a configuration with no bad plaquette in this neighborhood, a finite-support Qbad-preserving transition cannot create defects or enact a nontrivial flat row/column flip once R exceeds its support. The flat local configurations are related by the plane flips. Consequently the term, after subtraction of its common flat scalar, is sandwiched by the projector for a nearby bad plaquette. The same form estimate bounds its restriction to fixed Qbad by C Qbad, independent of volume. In particular the Qbad=4 sector has bounded retained-coefficient norms. This requires the enlarged neighborhood and fixed support; it is not true merely from plane invariance without Qbad preservation.

There can be additional quasi-local tails from the exact finite product; retain finite-order terms and put those tails in the arbitrarily high-order global remainder. Whole-row processes of length comparable to R are not finite-order retained local terms. This reasoning avoids assuming a selected global plane character.

The subsequent thin/nonthin and endpoint reductions require their own explicit bounded-degree/local-kernel estimates. The previous argument supports them but does not replace them. In particular it does not by itself prove that all uncomputed momentum-dependent coefficients preserve the displayed positive curvature.

## Source and gap bookkeeping

The normalized microscopic Fourier C has global norm O(R) at fixed L. In a specified positive plane fibre, Qbad=0 is one dimensional. A normalized sum of fixed-range defect-creating patterns applied to that vacuum has O(1) norm: distinct widely separated translates have distinct syndromes and are orthogonal, while coincidences have bounded multiplicity. Plane-orbit normalization does not change this statement. The same finite-pattern Gram argument applies to every retained source coefficient, after the matched unitary transformations and ground-mixing subtraction. Thus a source remainder O(lambda^11) with a volume-independent coefficient is plausible and justified by this structure once its first nonzero order lambda^10 is established; replacing it by a crude global norm at that order would lose the desired estimate.

The leading order and coefficient must be computed in the same retained gauge as the state. Inherited direct winding plus ground mixing supplies beta_L, not the bare winding derivative alone. Centering removes the vacuum scalar. Neither locality alone nor a projector norm estimate establishes this cancellation; it remains the inherited matched-source calculation.

Assume the target branch has a proved gap c lambda^14 within its fixed exact momentum and plane-character fibre (including orientation splitting when necessary). A global Hamiltonian remainder O(lambda^40 R^2) gives projector/eigenvector error O(lambda^26 R^2). Multiplying by ||C||=O(R) gives source error O(lambda^26 R^3). At p=21/20 this is lambda^(457/20)=lambda^22.85, hence o(lambda^10). Ground-projector errors, whose gap within this fibre is of order lambda^4, are smaller. Constants can be large at order 40, but fixed, so this is an asymptotic conclusion.

The lambda^14 denominator is not a gap from all neighboring momentum states. Momentum spacings can be of order lambda^12/R^2 and smaller than lambda^14 when p>1. Exact translation symmetry permits comparison in each momentum fibre and the Fourier source selects that fibre. This qualification is essential. Also q=2pi/R is indeed o(lambda) for p>1.

## Remaining state and claim limits

The argument isolates N0 and supports a specified plane-sector ground and source. It does not prove this character is the actual global ground uniformly along polynomial R. Exponentially high row-tunneling orders cannot be selected by a fixed-order remainder estimate. It also does not turn an O(lambda^14) eigenvalue error into a resolved curvature: to compare neighboring q energies one must control momentum dependence or make the exact remainder smaller than the dispersion signal, while bounding the retained higher-order coefficients separately.

No repository files changed. This is a focused embedding/source check, not a full microscopic dispersion or scattering theorem.
