---
claim_id: one_qubit_tick_update_covariance_limits_bounded_theorem_note_2026-10-21
claim_type: open_gate
claim_scope: "Supplied single-particle polynomial and ordered-block diagnostics, with explicit pointwise mixing counterexamples. General dynamics classification and physical mass identification are not claimed; the original negative theorem is deferred with exact recovery."
runner: scripts/one_qubit_tick_update_covariance_limits_2026_10_21.py
---

# Supplied convolution walks: ordered-block and point-phase diagnostics

Claim type: open_gate.
Primary runner: `scripts/one_qubit_tick_update_covariance_limits_2026_10_21.py`.

The filename and claim identifier are historical handles. The mathematical carrier is l2(Z^3) tensor C^2: a linear translation-invariant single-particle convolution model, with a separately supplied spin-1/2 rotation action. This is not a derived tensor-product many-body qubit dynamics, framework admissibility law or record process. A finite stencil {0,+-e_i} is used for the polynomial ansatz below; the split-step products reach a different stencil. No axiom or candidate-law clause supplies these choices.

## Supplied polynomial diagnostic

Choose complex a,b,c and the expression

    A(k) = (a+2b sum_i cos(k_i)) I - 2i c sum_i sin(k_i) sigma_i.

Half the trace of A†A is |a+2b sum cos(k_i)|^2+4|c|^2 sum sin^2(k_i). Writing q_i=cos(k_i), its mixed q_x q_y coefficient is 8|b|^2 and its q_x^2 coefficient is 4|b|^2-4|c|^2. These are algebraic expansion identities for this supplied expression. This salvage does not promote them to a classification of allowed dynamics or conclude a universal stationary-update result. The runner expands the coefficients symbolically and tests covariance of one seeded complex instance at 20 momenta for the 24 proper cubic rotations.

## Forward and reverse factor orders

Let S_i(k)=cos(k_i) I-i sin(k_i) sigma_i, UL=S_z S_y S_x and UR=S_x S_y S_z. Both expand at the origin as I-i sum_i k_i sigma_i+O(|k|^2). Their origin velocity determinants have the same sign; reverse ordering is not an opposite-chirality construction.

The half-traces are c_x c_y c_z+s_x s_y s_z for UL and c_x c_y c_z-s_x s_y s_z for UR. A z quarter-turn produces order z,x,y after rotating the spin axes. Cyclicity of trace makes its trace equal to that of reverse order x,y,z, and SU(2) then gives the same unordered eigenvalue pair. The matrices are generally different. The runner checks that distinction at a generic nondegenerate point. Across its fixed 20 seeded momenta, the original comparison gives 12 spectral symmetries and 4 operator symmetries among the 24 rotations. Those finite comparisons are identified as diagnostics, not an exhaustive dynamical classification.

## Exact point identities for a supplied mixing

Form D(k)=diag(UL,UR), beta=tau_x tensor I, and W(k,theta)=D(k) exp(-i theta beta). At k=0, the minimum absolute principal eigenphase is |theta| for |theta|<=pi. This is a pointwise distance, not a neighborhood mass gap.

On k=(t,0,0), UL=UR=exp(-it sigma_x). The block generator I tensor sigma_x commutes with beta, so the eigenphases are +-t+-theta modulo 2pi. At t=theta there is an exact zero phase. This counterexample directly tests the earlier inference from the origin alone.

At k_d=(pi/2)(1,1,1), UL=I and UR=-I. Thus D=tau_z tensor I anticommutes with beta, W^2=I and Tr(W)=0. The eigenvalues remain +1 and -1 (twice each) for every theta. This is an exact point result; a cone or physical-particle identification is not inferred.

An onsite scalar phase exp(-i delta) multiplies these corner eigenvalues by exp(-i delta). For delta not an integer multiple of pi the corner has no zero phase. It remains translation invariant and momentum diagonal. This is a pointwise counterexample to the earlier universal momentum-mixing prescription; it is not a global-gap construction or a physical mass theorem. The runner uses theta=.1 and delta=.23 for numerical controls.

## Deferred original theorem and recovery

Original PR9838 head `a5457b49c85b3393aef3e86e57678088a394aa67` preserves the full original note, runner and cache at these same paths. Its nearest-neighbor commutant/normalization proof is deferred separately from this salvage. The original independent reviewer found the narrow convolution-model proof mathematically sound, but its negative-claim submission packet lacked the required route-family evidence. The original proof is not declared false, silently discarded or repackaged as a newly approved theorem. The original branch remains a recovery handle for that unlanded content. The corrected source here does not assert the original broad dynamics or mass prescriptions.

## No-Go Discipline Gate

This is a limitation record for the deferred original negative claim, not a packet PASS for it. The current open_gate surface retains supplied algebra and explicit counterexamples only.

- N1: one actual commutant/normalization mechanism was checked in the original review. Five distinct attempted or prior-ruled-out route families are not evidenced. Different implementations are not additional families. The original negative-claim packet remains incomplete; its theorem is deferred rather than declared false.
- N2: no independent wall count is asserted. Linear carrier, translation invariance, stencil and rotation action are joint model conditions.
- N3: those supplied conditions and the unproved physical realization are now explicit. A qubit label does not derive this convolution model.
- N4: no candidate-law or prior theorem is used as a matched exclusion witness in the salvage.
- N5: polynomial coefficients, one-site carrier declarations, sampled momenta, 2x2/4x4 blocks and unexecuted lattice-wide physical interpretations are separated in runner output. Point identities are not neighborhood or global mass-gap statements.
- N6: this correction adopts no new axiom. Alternative carriers, actions, stencils and nonlinear updates are outside the deferred theorem's domain, not failed routes.
- N7: the exact axis zero defeats the origin-only gap inference; the scalar phase defeats the pointwise momentum-mixing necessity assertion. Neither is claimed to refute the independently checked narrow nearest-neighbor proof.
- N8: the original reviewer inspected relevant premise/statement sections of earlier cell-classification and staggered-block notes. They are context only, not retained authority or an exhaustion certificate here. No new cross-cycle closure claim is made.

## Scope and open obligations

Momentum conventions, spin action, factor order, mixing beta, phase branch, complex test coefficients, seed 0 and finite momentum samples are supplied. General perturbation classes, global gaps, physical statistics and a many-body framework realization remain unproved. Source-only review and runner diagnostics do not assign retained or audit status.
