# Finite-time attachment to a common-product program cell

Claim type: bounded_theorem. Conditional mathematical result with a distinct analytical check and separate publication integration. It proves a finite-time, full-output comparison for a supplied common-product program cell with an added bounded interaction that exactly preserves its literal input code. The attachment need not commute with the enabled logical exchange. An endpoint exchange provides a positive nearest-neighbor example. A specified mediator exchange fails the intertwining hypothesis; no claim of dynamical failure is drawn from that fact.

The direct mathematical parent is the [common-product program cell note](COMMON_PRODUCT_PROGRAM_CELL_BOUNDED_THEOREM_NOTE_2026-10-18.md). The new argument and distinct check are [the attachment proof](../outputs/common_product_program_2026_10_18/proofs/mediated_program_attachment__PROPOSAL.md) and [its analytical review](../outputs/common_product_program_2026_10_18/proofs/mediated_program_attachment_check__REVIEW.md). Neither an arbitrary network theorem nor a native physical interaction law is supplied.

## Physical cell and exact attachment domain

The parent cell has head qubits at u=(-1,0,0), m=(0,0,0), v=(1,0,0), and three program qubits immediately above them. Its two legal programs are the physical product states |000> and |111>. The common literal isometry J inserts a vacant mediator and the selected legal program while leaving all four endpoint occupation states arbitrary. The preparation is the same literal endpoint/vacancy map in both programs; dressed eigenstates are proof devices, not required initial states.

Write X_h,uv=(X_u X_v+Y_u Y_v)/2 and n_u=(I-Z_u)/2. The positive head block is Q_b(u,v)=b(n_u+n_v-X_h,uv), with double-occupation energy 2b and norm 2b. For b>0 and D1>D0>2b, set a0=2b²/D0. The supplied six-qubit Hamiltonian is

    H = Q_b(u,m)+Q_b(m,v)+b(I-n_u)+b(I-n_v)
        +[(D0-2b)P0(c_m)+(D1-2b)P1(c_m)] n_m
        +a0 P0(c_u)n_u+a0 P0(c_v)n_v.

All displayed blocks are positive. On legal program p, this is exactly 2b I plus the head Hamiltonian with endpoint onsite a0 for p=0 and zero for p=1, mediator onsite D_p, and both exchanges -b. The scalar 2b is common to both programs, vacuum, and all endpoint occupations.

On the logical endpoint space define the full four-state projectors

    R_minus=(n_L+n_R-X_h,LR)/2,
    R_plus =(n_L+n_R+X_h,LR)/2.

Both have eigenvalue one on double occupation. The desired isolated logical generator, including its physical scalar, is

    A=2b I+P0 tensor a0 R_minus.

Tensor J with the identity on any added neighbor degrees of freedom. Let K be bounded and self-adjoint on the physical space. The attachment contract is the exact operator identity

    KJ=J K_log                                             (1)

for a bounded self-adjoint K_log on the entire logical domain, including both legal programs, all endpoint occupations and all permitted neighbor states. It implies K_log=J* KJ, ||K_log||<=||K||, and that range(J) reduces K. Agreement of compressed matrix elements alone is insufficient: the off-code block (I-JJ*)KJ must vanish.

No commutation of K_log with A is required. The comparison throughout this note is

    exp[-it(H+K)]J  versus  J exp[-it(A+K_log)].             (2)

Every physical output is retained. Passive references may be tensored onto these maps without changing the bounds. An actively coupled degree of freedom must instead belong to the domain on which (1) is checked.

## General ordered propagator bound

The following identity applies to any bounded self-adjoint H, A and K satisfying (1). Define

    E(s)=exp(-isH)J-J exp(-isA),   D=HJ-JA,
    U_K(s)=exp[-is(H+K)],         V_K(s)=exp[-is(A+K_log)].

The exact difference F(t) in (2) satisfies, for t>=0,

    F(t)=-i integral_0^t U_K(t-s) D V_K(s) ds.

Differentiate Y(s)=U_K(t-s)E(s)exp(isA)V_K(s). The physical H terms cancel, while

    d/ds [exp(isA)V_K(s)]=-i exp(isA)K_log V_K(s).

No logical operator has been commuted through A. Integrating with Y(0)=0 gives the exact ordered identity

    F(t)=E(t)exp(itA)V_K(t)
       -i integral_0^t U_K(t-s)K E(s)exp(isA)V_K(s) ds
       +i integral_0^t U_K(t-s)E(s)exp(isA)K_log V_K(s) ds. (3)

Consequently, if ||E(s)||<=delta(s),

    ||F(t)|| <= delta(t)
        +(||K||+||K_log||) integral_0^t delta(s) ds
      <= delta_bar(T)[1+2T||K||],     0<=t<=T.            (4)

The bound can be capped at 2 because both maps are isometries. The same proof for -H,-A,-K gives the negative-time statement with a two-sided isolated envelope. The two insertions in (3) are distinct; this argument does not give a factor 1+T||K||. No spectral gap of H+K is assumed.

For the parent cell, a valid isolated envelope is

    delta(s)=max{2 beta0 |sin[(D0+a0)s/2]|,
       min(2,2 beta1+2|sin(epsilon1 s/2)|)},

with the parameters below. This estimate is finite-time and can be weak when T||K|| is large.

## Dressed-code bound for this cell

Set

    epsilon1=4b²/[sqrt(D1²+8b²)+D1],
    r0=sqrt(2)b/D0,                 r1=sqrt(2)b/(D1+epsilon1),
    alpha_p=(1+r_p²)^(-1/2),       beta_p=r_p alpha_p.

The parent four-state calculation gives an auxiliary isometry J_d. In each program it replaces the symmetric one-head state S by alpha_p S+beta_p |010>, and the double-endpoint state |101> by alpha_p |101>+beta_p (|110>+|011>)/sqrt(2). Vacuum and the antisymmetric one-head state are unchanged. It obeys

    HJ_d=J_d A_d,   A_d=A-P1 tensor epsilon1 R_plus,
    kappa_code=||J_d-J||=max_p sqrt(2-2alpha_p).          (5)

Here kappa_code denotes code distance, not a source hopping. Because the changed number sectors and program images are orthogonal, there is no sum over four input columns in (5).

The exact literal attachment condition implies

    KJ_d-J_d K_log=K(J_d-J)-(J_d-J)K_log.

Thus the rectangular defect against A+K_log has norm at most

    (||K||+||K_log||)kappa_code+epsilon1.

Duhamel's formula, followed by the two endpoint replacements of J_d with J, proves

    ||F(t)|| <= min{2,
        2kappa_code+|t|(2||K||kappa_code+epsilon1)}.      (6)

This estimate does not assert that the dressed space remains invariant after attachment. Its failure of invariance is paid through the residual. It remains valid when an allowed K_log mixes the two legal programs. A branchwise refinement omitting epsilon1 on the enabled branch requires the additional condition that the attachment conserve that program sector.

Equations (4) and (6) bound the same comparison and may be combined by a minimum. The sharper isolated sine leakage constants are not interchangeable with the code distance used in (6).

## Positive endpoint attachment and a failed hypothesis

Add a head qubit w=(-2,0,0), allow its full occupation space, and take K=Q_c(u,w) with c>=0. Since this block acts on neither mediator nor program coordinates,

    K(J tensor I_w)=(J tensor I_w)Q_c(L,w),
    ||K||=2c.                                          (7)

This verifies (1) on every endpoint/neighbor input, including double occupation and reference entanglement. The shared endpoint means Q_c(L,w) generally does not commute with the enabled L-R exchange; equations (3) and (6) explicitly allow that situation. Positive endpoint and neighbor onsite terms also satisfy (1), as do sums satisfying the same full-domain identity.

The example adds one qubit and one positive nearest-neighbor two-qubit block. It adds incident norm 2c at u and w, which must be included in any load cap. The parent cell's combined-block convention has seven blocks, with incident loads 3b+a0 at u,v and D1+2b at m; those isolated numbers cannot be used unchanged after attachment. Absent couplings and supplied local roles remain physical premises.

For contrast take K=Q_c(m,w') with c>0 and w'=(0,0,1). On the literal input with u=v=m=0 and w'=1, the hopping creates a mediator-occupied component with coefficient -c. It lies outside range(J tensor I_w'), so no logical K_log can satisfy (1) for this contact. This only excludes application of the present sufficient theorem. It proves neither actual computational failure nor a general ban on mediator-supported terms: q n_m annihilates the literal code and satisfies (1) with K_log=0.

## Finite-horizon overhead and the actual target

Suppose an allowed attachment satisfies ||K||<=chi a0. At the isolated comparison time T_gate=pi/a0, equation (6) gives

    error <= min{2,2kappa_code(1+pi chi)+pi epsilon1/a0}
          <= min{2,2kappa_code(1+pi chi)+pi D0/D1}.     (8)

The last comparison is weak even though epsilon1<2b²/D1: the cap can make both minima equal to 2. Since r1<r0 and kappa_code<=r0, an explicit sufficient uncapped envelope is

    2sqrt(2)(b/D0)(1+pi chi)+pi D0/D1.                 (9)

For the endpoint example c=z a0, chi=2z and the factor in (9) is 1+2pi z. This is a finite overhead at fixed z. At fixed c while a0 decreases, chi grows; neither uniform small overhead nor an unchanged incident cap follows. The generic propagator bound instead gives factor 1+2pi chi multiplying the isolated horizon envelope. No new operating point or optimized coefficient family is selected here.

The target at this time remains exp[-it(A+K_log)]. It generally is not a standalone endpoint exchange followed by independent neighbor evolution. The scalar 2b, any scalar in K_log, coherent program phases and the full double-occupation action remain present. The word gate in T_gate specifies a comparison scale, not a factorization or a new attached gate guarantee.

## Premises, evidence and limits

This result assumes the supplied Hamiltonian, exact coefficients and roles, common literal vacancy injection, legal replicated program content, and an independently verified attachment identity (1). It does not construct native Records or their preparation, supply a network compiler, cover approximate intertwining without additional error terms, or establish capture/reset, repeated monitoring or permanent finite storage. Overlapping-cell estimates cannot be composed without a full common domain and its own isolated comparison. No pending mediator-source, finite-mass or apparatus performance result enters this note.

The exact primary identities are:

- Attachment proof: `55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a`.
- Distinct attachment review: `48940d210811f4599c16677edde54b6e3b1be8d6715b7a14aa29e5c4b3b440ce`.
- Isolated-cell proof, reused through the direct parent: `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.
- Isolated-cell review: `809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6`.

The [superseded attachment revision](../outputs/common_product_program_2026_10_18/history/attachment_PROPOSAL_v1.md), SHA256 `65355be5c834e18db22da52ae67e67b406cc81c40527071ae5b12920c9235cbb`, is non-premise history. At ROOT's request the author changed only the capped strict comparison to a weak comparison; the review verified the complete diff.

ROOT proposed the attachment question and dressed-residual route. The resources worker authored the proof. The distinct reviewer had checked the isolated parent and has shared positive-block ancestry; the new ordered identity, full-domain examples and residual were reconstructed explicitly. This synthesis is by that reviewer and is not an additional independent mathematical check. The separate ROOT publication integration is recorded in the evidence packet. No scientific program, new numerical result, audit or retained-status claim is supplied; publication copy and link evidence are separate mechanical work.
