# Finite-time attachment stability of the common literal program cell

New bounded author derivation requiring a distinct check. Under an EXACT literal-code intertwining condition on the added physical interaction, the common-product cell739e99c4 admits explicit full-output finite-time bounds even when the attachment does not commute with the enabled logical exchange. Two bounds are proved below: a general isolated-propagator estimate with factor1+2T||K||, and a cell-specific dressed-isometry estimate. A factor1+T||K|| is not presumed.

ROOT proposed both the perturbative question and, subsequently, the controlled dressed-isometry route. These suggestions are design exposure, not independent checks. The common-product source is itself under distinct review; its algebra is the explicit provisional premise here. No complete network or processor replacement theorem is asserted.

## 1. Exact spaces, scalar and attachment contract

Let J denote the common literal injection of739e99c4, including the two legal program sectors |000>,|111>, arbitrary endpoint states and a vacant mediator. Tensor J with identity on any added logical neighbor and passive reference. Let H be the physical six-site cell Hamiltonian (identity on the neighbors), and

 A=2b I+P0 tensor a0 R_-,
 a0=2b²/D0, D1>D0>2b,
 R_-=(n_L+n_R-X_h,LR)/2.

A includes the actual scalar2b on BOTH programs, vacuum and all endpoint occupations. Thus J exp(-itA) is the literal enabled-Q/disabled-identity comparator. The ideal program projectors refer to the two abstract legal programs. No phase is dropped.

Add a bounded self-adjoint physical operator K. Require

                 KJ=J K_log                              (1)

for a bounded self-adjoint logical operator K_log on the FULL encoded input domain, including programs and all allowed neighbor/reference degrees of freedom. Since J is an isometry, K_log=J* KJ and ||K_log||<=||K||. Self-adjointness and(1) make range(J) reducing for K; equivalently there is no off-code column from K on that domain. This is stronger than small leakage, agreement of matrix elements or conservation of total head number. It is an exact attachment hypothesis to be checked from physical terms.

No commutation [A,K_log]=0 is required. The desired physical comparison is exp[-it(H+K)]J versus J exp[-it(A+K_log)], including every physical output. Passive-reference extension preserves all bounds. If K acts on what had been called a reference, that degree is now part of the logical attachment and(1) must hold on its whole domain; no unspecified interaction with a passive reference is allowed.

## 2. General propagator transfer, derived in physical order

This section applies to any bounded self-adjoint H,A,K satisfying(1), not just the cell. Define

 E(s)=exp(-isH)J-J exp(-isA), D=HJ-JA,
 U_K(s)=exp[-is(H+K)], V_K(s)=exp[-is(A+K_log)].

Then E(0)=0 and E'=-iHE-iD exp(-isA). The full difference is the exact rectangular Duhamel integral

 F(t)=U_K(t)J-JV_K(t)
     =-i integral_0^t U_K(t-s)D V_K(s) ds.             (2)

For t>=0 differentiate the physical ordered product

 Y(s)=U_K(t-s) E(s) exp(isA) V_K(s).

Cancellation of the H terms, without commuting K_log through A, gives

 Y'(s)= iU_K(t-s)K E(s)exp(isA)V_K(s)
        -iU_K(t-s)D V_K(s)
        -iU_K(t-s)E(s)exp(isA)K_log V_K(s).

Since Y(0)=0, Y(t)=E(t)exp(itA)V_K(t), integration yields

 F(t)=E(t)exp(itA)V_K(t)
       -i integral_0^t U_K(t-s)K E(s)exp(isA)V_K(s) ds
       +i integral_0^t U_K(t-s)E(s)exp(isA)K_log V_K(s) ds.
                                                               (3)

Every external factor is unitary and the last term has the displayed noncommuting order. Therefore if ||E(s)||<=delta(s),

 ||F(t)||<=delta(t)+(||K||+||K_log||) integral_0^t delta(s) ds
          <=delta_bar(T)[1+2T||K||], 0<=t<=T,        (4)

where delta_bar(T) bounds delta on the interval. For negative times apply the same argument to -H,-A,-K, giving the same result with |t| and a two-sided isolated envelope. A trivial cap2 can always be added because both maps are isometries.

This is a direct integration identity rather than an assumed Volterra or Gronwall estimate. It needs neither a spectral gap for H+K nor a commutation condition with A. The price is that two distinct insertions of K occur in(3); no factor1+T||K|| is inferred by deleting one. The statement remains finite-time and can be poor when T||K|| is large.

For the cell, the already derived isolated bound can be used as

 delta(s)=max{2beta0|sin[(D0+a0)s/2]|,
       min(2,2beta1+2|sin(epsilon1 s/2)|)},

or by any larger valid two-sided envelope. It is not necessary to select the maximum leakage times for different programs or replace sine by its maximum unless a simpler sufficient bound is wanted.

## 3. Cell-specific dressed-isometry bound

The controlled dressed injection J_d maps logical symmetric one-head and double-head states in program p to alpha_p S+beta_p M and alpha_p E+beta_p B, respectively, leaving vacuum and antisymmetric one-head unchanged. In the source notation

 r0=sqrt(2)b/D0,
 epsilon1=4b²/[sqrt(D1²+8b²)+D1],
 r1=sqrt(2)b/(D1+epsilon1),
 alpha_p=(1+r_p²)^(-1/2), beta_p=r_p alpha_p.

Its exact physical intertwiner and distance are

 H J_d=J_d A_d,
 A_d=A-P1 tensor epsilon1 R_+,
 R_+=(n_L+n_R+X_h,LR)/2,
 kappa_code=||J_d-J||=max_p sqrt(2-2alpha_p).        (5)

The symbol kappa_code is a code distance, not any previous source hopping. R_+ is a FULL four-state projector including double occupation. The scalar2b occurs in A_d exactly as in A. The injections and identities tensor with neighbor/reference identity.

Using(1),

 KJ_d-J_dK_log=K(J_d-J)-(J_d-J)K_log,
 ||KJ_d-J_dK_log||<=(||K||+||K_log||)kappa_code.    (6)

Thus the rectangular Hamiltonian residual against the desired logical generator is

 (H+K)J_d-J_d(A+K_log)
   =KJ_d-J_dK_log-J_d(P1 tensor epsilon1 R_+).

Its norm is at most2||K||kappa_code+epsilon1. Rectangular Duhamel then gives a linear-in-time bound without any commutation assumption between K_log and either logical projector. Adding the two endpoint replacements J_d to J yields

 ||exp[-it(H+K)]J-J exp[-it(A+K_log)]||
 <=min{2, 2kappa_code+|t|(2||K||kappa_code+epsilon1)}. (7)

This remains valid even if an allowed K_log mixes the two legal program sectors; the residual projector has norm one. For attachments conserving the program, the separate enabled branch has no epsilon1 term and the disabled branch may use its own smaller kappa_code,p. Such refinement requires that extra commutation, not merely(1).

Equation(7) is usually more useful than multiplying a bound containing epsilon1*T by1+2T||K||. It does not mean the actual attached state stays in the dressed subspace; that subspace may cease to be invariant. Its residual is explicitly paid. Equations(4),(7) bound the SAME full comparison and may be combined by a minimum. The sharper isolated2beta_p bounds are not relabeled as2kappa_code: the latter is the distance used by this proof and is slightly larger.

## 4. A concrete nearest-neighbor positive attachment

Add one physical head qubit w at(-2,0,0), nearest neighbor to u=(-1,0,0), with arbitrary occupation and reference entanglement. Use the literal extended injection J_ext=J tensor I_w and physical positive exchange

                  K=Q_c(u,w), c>=0.

This is the same full positive head block with double-occupation energy2c. It acts on no mediator or program coordinate, so direct action on every occupation basis column gives

          K J_ext=J_ext Q_c(L,w), ||K||=2c.        (8)

It can exchange an endpoint head with the new neighbor while the mediator stays vacant. It does NOT have to commute with Q_(a0/2)(L,R); for positive nonzero couplings the shared endpoint generally makes their commutator nonzero. Conditions(1) and self-adjointness, rather than that commutation, justify(4),(7).

A positive endpoint onsite q n_u similarly interwines with q n_L, and positive q n_w with itself. Sums of such terms obey(1), with their actual combined norm or the safe sum of block norms. Endpoints, neighbor and mediator may all be occupied during actual evolution; the bound is on the full encoded four-state endpoint domain tensored with the full neighbor qubit, not a one-head-only approximation. The original source proof included all endpoint head numbers, so this tensor extension loses no two-head input column.

The exchange example uses seven physical qubits, one extra positive nearest-neighbor two-qubit block and supplied coefficient c. It adds incident norm2c at u,w. The original combined-block cell norm/load counts remain those of739e99c4; an imposed load cap must now pay this increment at u rather than silently reuse the isolated count. Geometry alone does not mandate or forbid other couplings; all absent interactions remain supplied. No neighbor initialization is required by the mathematical map beyond a supplied state on its full domain, but its role/occupation frame and any physical preparation remain external premises.

A sharp violation is K=Q_c(m,w'), c>0, with a new neighbor w'=(0,0,1). In the legal input column with u=v=m=0,w'=1, hopping creates -c times the state m=1,w'=0. This lies outside range(J_ext), whereas J_ext K_log can never have a mediator-occupied column. Thus(1) fails for every logical K_log. This theorem gives no bound for that contact. It is not a claim that every mediator-supported operator is forbidden: for example q n_m annihilates the literal code and satisfies(1) with K_log=0. The exact invariant-domain test, not the coordinate label alone, is decisive.

## 5. Gate-time overhead for attachment strength proportional to a0

Suppose a permitted attachment has ||K||<=chi a0 for a supplied constant chi>=0. At the enabled isolated exchange time T_gate=pi/a0, equation(7) becomes

 error<=min{2, 2kappa_code(1+pi chi)+pi epsilon1/a0}
       <min{2, 2kappa_code(1+pi chi)+pi D0/D1}.     (9)

The last inequality uses epsilon1<2b²/D1 and a0=2b²/D0. Since r1<r0, kappa_code<=r0=sqrt(2)b/D0. The resulting fully explicit sufficient envelope is

       2sqrt(2)(b/D0)(1+pi chi)+pi D0/D1.         (10)

For the exchange example c=z a0 with z>=0, ||K||=2z a0, hence chi=2z and the factor is1+2pi z. This is a finite overhead at fixed z. It does not certify that the attached ideal operation at T_gate is a standalone endpoint exchange: its target is exp[-it(A+K_log)], which generally differs from a product of an exchange and independent neighbor dynamics. The time name only supplies a natural comparison scale.

For comparison the generic result(4) gives factor1+2pi chi multiplying the isolated horizon envelope; both are valid but distinct estimates. At fixed c not shrinking with a0, chi=2c/a0 grows as a0 decreases, so a uniform small overhead does not follow. Nor may a bounded-strength scaling ignore the added incident load. No new parameter point, coefficient optimization or operating certificate is selected here.

## 6. Physical scope, provenance and required check

The model still assumes the exact candidate H, common literal product injection, positive programmable roles/coefficients, three equal program contents and correct occupation basis. The actual scalar2b remains in A+K_log; if an attachment itself contains scalar terms they remain in K_log as well. Nontrivial neighbor/old dynamics are not removed by a fitted phase. Coherent legal program superpositions are covered mathematically, without claiming their interpretation as native permanent Records.

This is a sufficient stability theorem for explicitly intertwining bounded attachments. It is neither arbitrary strong-attachment protection nor a network compiler. One can apply the general identity to a larger isolated comparison only after supplying its own full-domain isolated error and an exact common injection. Individual cell estimates do not establish those premises for overlapping networks. Approximate intertwining, extra mediator exchange, erroneous initialization, native Record creation, capture/reset and permanent finite storage require separate proofs.

Primary source: mediated_common_product_program/PROPOSAL.md SHA739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088. I authored that source, whose independent check is pending at task assignment. This proposal does not claim that parent accepted reading equals a distinct check. ROOT proposed the attachment question and then the dressed residual route; both were verified here as author mathematics with exposure. The general ordered identity(3), exact attachment domain(8) and full dressed residual(6)--(10) require a distinct check before integration. The previous program cell/check remain context at their scopes, not a check of this attachment result.

Only this proposal was written. No scientific program, symbolic solver, simulation, numerical sweep, new performance point, canonical/W/Git/PR/checkpoint/prompt/model change or delegation occurred. No publication or retained status is assigned.
