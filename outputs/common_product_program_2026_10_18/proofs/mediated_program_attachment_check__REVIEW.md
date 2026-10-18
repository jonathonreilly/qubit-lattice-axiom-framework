# Distinct check of finite-time common-product cell attachment

Disposition: conditional support for the complete corrected source `mediated_program_attachment/PROPOSAL.md`, SHA256 `55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a`. No further mathematical correction is required. The result is a bounded-operator finite-time comparison under exact full-domain attachment intertwining. It does not supply that condition for arbitrary contacts or overlapping networks.

## Revision and premise identities

The preserved `PROPOSAL_v1.md` has SHA256 `65355be5c834e18db22da52ae67e67b406cc81c40527071ae5b12920c9235cbb`. The complete diff is one change in equation (9): the comparison between the two capped minima is now weak rather than strict. ROOT requested this correction; the author applied it. Although epsilon1 < 2 b^2/D1 strictly, both minima can equal 2. The corrected comparison is valid, including that saturated case. No constant, physical premise or other proof changed.

The unchanged isolated-cell premise is `mediated_common_product_program/PROPOSAL.md`, SHA256 `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`, with my prior full distinct check `mediated_common_product_program_check/REVIEW.md`, SHA256 `809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6`. These identities were refreshed. The earlier check is reused only for the exact four-state Hamiltonian, injection, eigenvectors, scalar and positive-block conventions. It is not independent evidence for this new attachment theorem. Statements in the proposal that its parent check was pending describe author-time provenance; that dependency is now supported at these exact identities.

## Ordered propagator identity

Let B=A+K_log and U(t)=exp[-it(H+K)]. On the entire specified logical Hilbert space, KJ=JK_log eliminates the attachment part of the rectangular generator defect, leaving D=HJ-JA. Hence differentiation of U(t-s)J exp(-isB) gives i U(t-s)D exp(-isB); integrating gives F(t)=-i integral U(t-s)D exp(-isB) ds with the sign in equation (2).

For E(s)=exp(-isH)J-J exp(-isA), direct differentiation gives E'=-iHE-iD exp(-isA). Independently differentiating Y(s)=U(t-s)E(s)exp(isA)exp(-isB), the H terms cancel on the physical left, while

    d/ds [exp(isA)exp(-isB)]
      = -i exp(isA) K_log exp(-isB).

This last equality cancels A only against itself. It does not move K_log through A. The surviving terms are +i U K E exp(isA)V, -i U D V, and -i U E exp(isA)K_log V. The endpoints are Y(0)=0 and Y(t)=E(t)exp(itA)V(t). Solving the integrated identity for F gives exactly equation (3), including the signs and order of both insertions.

Unitary invariance therefore yields delta(t)+(||K||+||K_log||) integral delta(s) ds. Compression K_log=J* KJ implies ||K_log||<=||K||, giving 1+2T||K||. Dropping either insertion would not be justified. The same calculation for the three negated generators proves the stated negative-time version. Bounded self-adjoint generators make these derivatives and integrals legitimate without unbounded-domain qualifications. The cap 2 follows from the difference of two isometries. At t=0 the exact difference vanishes, even if a chosen loose envelope does not.

## Exact attachment domain and dressed residual

The hypothesis is stronger than matching J* KJ: the off-code block (I-JJ*)KJ must vanish. Because K is self-adjoint, its adjoint block vanishes too, so range(J) reduces K. Full neighbor and legal-program domains are essential; checking only a selected one-head column would not suffice. No implication that range(J) reduces H is made.

The isolated source supplies HJ_d=J_d A_d with A_d=A-P1 epsilon1 R_plus. R_plus is a norm-one projector on the complete four-state endpoint space: its eigenvalues on vacuum, symmetric, antisymmetric and double occupation are 0,1,0,1. Thus the disabled double-occupation residual is included. The common scalar 2b occurs in both A and A_d.

Subtracting the literal intertwiner gives exactly

    KJ_d-J_dK_log = K(J_d-J)-(J_d-J)K_log.

Consequently the rectangular defect relative to B has norm at most (||K||+||K_log||) kappa_code+epsilon1. Rectangular Duhamel costs |t| times that norm. Replacing J by J_d at the initial and target ends costs kappa_code twice, proving equation (7). No invariance of the dressed space under H+K is assumed. This argument remains valid if K_log mixes legal programs; conservation of a program sector is needed only for the optional branchwise improvement.

The norm of J_d-J is the maximum, not the sum, of sqrt(2-2alpha_p): the changed symmetric and double-occupation columns have orthogonal number sectors, and legal programs have orthogonal images. The parent four-state calculation covers this norm. The inequality kappa_code<=r0 follows from r1<r0 and (1+r^2)^(-1/2)>=1-r^2/2. No sharper isolated leakage constant is substituted for this different code distance.

## Physical example and hypothesis failure

For K=Q_c(u,w), w=(-2,0,0), the block acts exclusively on the literal endpoint factor and added neighbor. The mediator and program factors of J_ext are untouched. Its action is therefore exactly J_ext Q_c(L,w) on every endpoint/neighbor occupation, including double occupation and arbitrary entanglement. The full qubit block has norm 2c, is positive, and is nearest neighbor at the stated coordinates. Its noncommutation with the enabled L-R exchange causes no gap in either proof. The seventh physical qubit and added incident norm 2c at u and w must be paid; the source does so explicitly.

For Q_c(m,w'), the displayed vacuum-endpoint, occupied-neighbor column acquires a mediator-occupied component of coefficient -c. It cannot lie in range(J_ext); hence no K_log satisfies the required intertwining for that contact. This is an explicit failure of this theorem's hypothesis, not a claim that the attached dynamics necessarily fail or a universal restriction on mediator contacts. In particular n_m annihilates the literal code and satisfies the condition with zero logical operator, as the source observes.

## Horizon, target and scope

At |t|=pi/a0 and ||K||<=chi a0, equation (7) gives 2 kappa_code(1+pi chi)+pi epsilon1/a0 before capping. Substituting epsilon1<2b^2/D1 and a0=2b^2/D0 gives the corrected weak capped inequality (9), and kappa_code<=sqrt(2)b/D0 gives (10). For c=z a0, the full block norm gives chi=2z, not z. At fixed c while a0 decreases this dimensionless ratio grows, so no uniform overhead follows. The proposal correctly avoids an operating-point or optimality claim.

The target is exp[-it(A+K_log)], retaining the common 2b phase and any scalar in the attachment. It cannot generally be factored into the isolated gate and neighbor evolution. The time pi/a0 is only a comparison scale. Arbitrary passive-reference tensor extensions preserve operator norms; an actively coupled degree of freedom must instead be included in the domain on which intertwining is proved. The estimate retains every physical output and incurs no postselection or normalization cost.

The supplied positive physical cell, vacancy preparation, legal replicated program states, coefficient/role calibration and absent interactions remain premises. This theorem does not derive native program storage, an arbitrary network compiler, repeated monitoring, permanent finite storage, or a processor replacement. No previous apparatus runtime or performance result is imported.

## Exposure and verification limits

I read the complete corrected proposal and the complete revision diff, reconstructed the new ordered identity and dressed residual analytically, and reused the unchanged isolated-cell check at its exact scope. ROOT supplied the attachment question and dressed-residual design to the author; that exposure was known to me. I previously checked the parent cell and authored its publication synthesis, and share substantial mediator/positive-block ancestry. I did not author this attachment source. This is a distinct check of the new bridge, not fresh independent recertification of my own parent review.

Only this review was written. No scientific program, symbolic solver, dynamics calculation, numerical sweep, source/W/Git/PR/checkpoint/prompt/model edit or delegation occurred. Hashing and textual diff were identity bookkeeping. No audit or retained status is assigned.
