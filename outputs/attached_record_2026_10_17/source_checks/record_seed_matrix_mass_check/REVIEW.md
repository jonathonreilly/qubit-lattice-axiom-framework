# Full seed matrix-mass interface: selective check

Final disposition: conditional support on corrected PROPOSAL.md SHA256e1abe3233bfe4b0e3d5e623240df9df9e80a35f7f3d081ab3e41944f06c6dd5d. The primary theorem, alternative full-reference formulation, resolvent integral and sector recombination are supported with their stated actual-device hypotheses. No outstanding correction requested.

Verified the exact full diff from preserved PROPOSAL_v1.md SHA25632c21d95854971a33220cd3fb42912f513325deddab08cd7896b70b8142f147b: the final paragraph now requires local reference absolute continuity including endpoints, the sector paragraph distinguishes pointwise squared-norm equality from the operator upper bound, and a correction acknowledgment preserves the counterexample below. No other mathematical content changed. These edits resolve the initial review finding without changing any bound.

Resolved initial finding: the alternative full-reference-measure formulation had omitted the necessary local reference regularity hypothesis; the original scalar-density formulation was already correct.

Counterexample to the alternative without that condition: take the actual seed measure M to be I_O times a unit atom outside I and M_ref to be I_O times a unit atom inside I. Both can be spectral measures of bounded scalar Hamiltonians on the four-dimensional seed space. The actual measure is absolutely continuous on I with zero density; both absolutely continuous densities on I vanish. Then tau=0 and eta=0 in the written alternative, yet actual omitted amplitude is1. The corrected reference regularity hypothesis excludes this example. No defect is found in the first formulation, whose reference is explicitly a scalar density integrated against the P_r.

## Source and scope

Read COMPLETE ../record_seed_matrix_mass/PROPOSAL.md at verified SHA25632c21d95854971a33220cd3fb42912f513325deddab08cd7896b70b8142f147b. This is a self-contained mathematical interface; no other packet's status is used to establish its identities. Previously read local instructions and scientific proof discipline are reused.

The proposal is root-authored and exposed before this check. I am a distinct checker of this proposal. I authored the earlier scalar return-resolvent proposal and checked the complete all-time herald interface; those are related exposed context, not independent validation of this new full matrix normalization step. Neither a scalar return-amplitude bound nor a local record-gate scattering estimate is imported as its actual-device premise.

No attached-device regularity, inverse margin, mass normalization, common-window fit or reference tail is independently supplied here. No numerical/scientific execution, solver, sweep, delegation, W/Git/prompt/model/checkpoint edit, audit or publication occurred. Only source reading/hashing and this report were performed. No editable prompt file changed.

## Matrix measure and physical-energy windows

For the isometry V, M(B)=V*E_H(B)V is positive and countably additive with exact M(R)=I_O. Its values need not be projections or commute with K. In particular its off-diagonal old-energy blocks cannot be set to zero merely because the chosen physical windows are disjoint.

On the stated absolutely continuous closed windows, the density convention is D=-Im F/pi, matching the retarded resolvent(z-H)^-1. Let A_ref=sum_r p_r P_r. The full matrix comparison integrates to

    ||M(I)-A_ref||<=sum_r eta_r=eta.

Both matrices are self-adjoint, so this norm estimate implies M(I)>=A_ref-eta I. Since the mutually orthogonal P_r sum to I and p_r>=p_min, A_ref>=p_min I. Therefore

    0<=I-M(I)<= (1-p_min+eta)I.

The upper bound is valid even if p_min-eta is negative; its useful version caps the outside operator norm by1. For Q=E_H(R\I),

    ||QV||²=||(QV)*QV||=||V*QV||=||M(R\I)||.

The square root, not the mass, is consequently the correct omitted-state amplitude. This treats arbitrary old superpositions and passive references because it is a full operator norm. No additional column factor is needed once this matrix comparison has been proved; separate diagonal expectations alone do not give it with the stated eta.

All external atoms and singular components are included by the exact complementary projection. Unitary evolution preserves its norm since Q commutes with H, and a subsequent record projection is a contraction. One must use the common union of PHYSICAL energy windows before recombination; relabeling a distinct kinetic interval for each logical column would not define this single spectral projection. No commutation of H with K or factoring old aging through H enters the argument.

## Resolvent comparison and reference tails

The imaginary-part map is contractive in operator norm: ||(X-X*)/(2i)||<=||X||. Thus, whenever the reference has the required boundary density, the L1 difference of densities is at most1/pi times the L1 norm of the resolvent difference. This controls real and imaginary logical off-diagonals through the full matrix norm; positivity of individual diagonal densities is insufficient.

For the exact seed-space Schur inverses, the identity

    D_e^-1-D_ref^-1=D_e^-1(D_ref-D_e)D_ref^-1

has the correct noncommuting matrix order. It follows by expanding the two terms, with no reordering of the middle perturbation. The stated inverse bounds and perturbation norm imply

    ||D_e^-1-D_ref^-1||
      <=kappa² C C_ref (a+b|delta|)/(delta²+gamma²).

The finite symmetric integrals are2arctan(d/gamma)/gamma and log(1+d²/gamma²), respectively. Multiplication by1/pi gives exactly the proposed eta_r bound. There is no record-basis factor1/2 here: this is a full seed density difference, distinct from the scalar record-flip return amplitude.

An application must identify F and F_ref with these exact inverse blocks, or with common isometric compressions of them so the norm comparison remains valid. An unrelated full inverse estimate alone does not identify the actual seed measure. The norms must hold for all relevant logical/fiber coordinates on the same physical-energy window. The proposal correctly leaves these as missing physical obligations.

The other reference channels cannot silently be dropped on I_r. For a full diagonal reference with nonzero other-channel densities, use triangle inequality to pay their integrated operator norm in eta_r, or retain the entire reference matrix measure. The latter formulation is valid with the reference regularity correction identified above: if M_ref(I)=integral_I D_ref, ||M_ref(R\I)||<=tau and the integrated matrix-density difference is<=eta, then

    M(R\I)<=M_ref(R\I)+eta I<=(tau+eta)I.

If instead M_ref has a positive singular component N_ref on I, the same lower comparison contains a subtraction of N_ref and gives only the safe upper bound tau+eta+||N_ref||. This is the precise extra term needed, not a reason to assume the reference singular part disappears. The actual measure's own positive local singular mass would not worsen this omitted-mass lower-comparison argument, but any use of a purely absolutely continuous packet representation must still account for it separately; the proposal's stronger actual regularity premise avoids that ambiguity.

## Record sectors and amplitude aggregation

With exact conserved-X sectors and normalized sector embeddings V_+,V_-, the delivered record0 seed is their coherent direct sum divided bysqrt(2). For each common unit logical/reference input u, the full omitted vector before record projection has squared norm

    (||Q_+V_+u||²+||Q_-V_-u||²)/2.

Orthogonality of the two record-X fibers, not cancellation of their errors, proves this equality. Taking the supremum gives an upper bound by the average of the sector operator-norm squares. It need not equal that average of suprema if the maximizing logical inputs differ. The proposal's final inequality uses the valid upper bound and therefore gives

    epsilon_sp<=min{1,sqrt((tau_++eta_++tau_-+eta_-)/2)}.

The tau/eta terms must come from valid sector mass estimates, including the corrected reference condition. Projecting onto record1 then contracts the entire omitted vector and cannot increase the bound. The two sector amplitudes may interfere after projection, but no favorable interference is assumed. Passive-reference tensoring preserves the full map norms and this orthogonal-sector argument.

The result supplies a conditional route from actual full seed matrix density comparison to the omitted-state amplitude required by the all-time interface. It establishes neither the density comparison nor a successful attachment. The narrow reference regularity repair and final-source verification are complete. The mathematical interface is supported without additional theorem constants or numerical work.
