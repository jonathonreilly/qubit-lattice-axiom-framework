# Distinct analytical check of the common literal product program cell

Disposition: conditional support for source `mediated_common_product_program/PROPOSAL.md`, SHA `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`. The full source was read and the changed physical matrices, four-state code, leakage, phase and bounded-load family were reconstructed analytically. No required correction found. This is an isolated supplied six-qubit Hamiltonian theorem, not a native interaction or network replacement result.

## Physical positivity and all number sectors

The full qubit Q_b block has vacuum energy0, one-head matrix [[b,-b],[-b,b]] and double-occupation energy2b. Its spectrum is0,0,2b,2b. Adding the two unconditional compensations gives exactly2b I-b(n_u+n_v). The two Q blocks supply b(n_u+n_v)+2b n_m minus the two exchanges. The programmed mediator term then leaves D n_m; the endpoint projectors add a_u n_u+a_v n_v. Thus equation(4) follows on the entire head Hilbert space in every program sector, with the SAME scalar2b, including vacuum. No head-number scalar has been discarded.

Every term is positive on its declared full support: D0-2b and D1-2b are positive, as are a0 and b. All installed pairs are nearest neighbors at the stated coordinates. The two noninteracting program-row adjacencies are explicitly absent supplied couplings. Each program occupation and total head number commute with the Hamiltonian.

Independently counting occupied sites gives one-head diagonal(a,D,a), two-head diagonal(a+D,2a,a+D), vacuum0 and triple occupation2a+D after removing only2b. Adjacent hard-core exchanges have coefficient-b in both the one- and two-head sectors; no fermionic minus sign is introduced. This reconstructs all eight head columns in each of eight program sectors, not just the legal code. Mixed program patterns have the specified Hamiltonian but are not assigned the legal on/off guarantee.

## Exact four-state low modes and physical preparation

In the enabled setting, the symmetric one-head block is [[a0,-sqrt(2)b],[-sqrt(2)b,D0]]. Its determinant vanishes because a0 D0=2b squared; its low vector is alpha0 S+beta0 M, with ratio beta0/alpha0=sqrt(2)b/D0. The other symmetric energy is D0+a0, and A has energy a0.

For the two-head block on(E,B), subtracting a0 I produces the SAME symmetric matrix. Hence its low vector has the SAME mixing angle and energy a0, and its high energy is D0+2a0. This checks the logical double-occupation column directly. The invariant dressed code therefore realizes a0 Rminus=Q_(a0/2) on all four logical states, including double occupation; it is not ordinary SWAP at the one-head exchange time.

In the disabled setting both symmetric blocks are [[0,-sqrt(2)b],[-sqrt(2)b,D1]]. Their low energy is -epsilon1, their high energy D1+epsilon1, with epsilon1(D1+epsilon1)=2b squared. The low-vector ratio is epsilon1/(sqrt(2)b). Vacuum and A have relative energy0. This realizes -epsilon1 Rplus, with double-occupation eigenvalue1 in Rplus. Both Rminus and Rplus are full four-state projectors. The negative relative low energy is compatible with the positive physical operator because2b remains; epsilon1<b follows from D1>2b.

The actual J_lit tensors an arbitrary two-endpoint state with a vacant mediator in BOTH program settings. It is common even for coherent logical occupations and reference entanglement; it does not require preparation of either dressed low mode. The auxiliary isometries are proof devices. Their norm distance from J_lit is sqrt(2-2alpha_p), because only the symmetric one-head and double-head columns change and their images occupy orthogonal number sectors. The inequality sqrt(2-2/sqrt(1+r squared))<=r follows by the positive scalar inequality (1+x)^(-1/2)>=1-x/2 for x>=0. Thus the code-distance estimate has no extra column-count factor.

## Exact leakage and common-program comparison

Writing S=alpha f-beta h with orthogonal high mode h shows that its difference from the target low-energy evolution is -beta(exp(-it E_high)-exp(-it E_low))h. Its norm is2beta times the absolute sine of half the gap. The double-head column has the same beta and the same gap within each program setting, and its number sector is orthogonal. Vacuum and A are exact. This proves the full operator equalities(10) and(11), rather than only a population-leakage estimate.

Enabled gap is D0+a0 in both occupied sectors; the double-head target phase exp(-ia0 t) is essential. Disabled gap is D1+2epsilon1 in both sectors. Comparing the latter with identity costs the additional exact projector norm2|sin(epsilon1 t/2)|, bounded by epsilon1|t|. Taking the trivial isometry distance cap2 gives(12). This establishes the stated finite-horizon bound and preserves every mediator output. The literal code is not invariant: its symmetric input immediately couples to M. Approximate output vacancy is paid, not asserted exact.

The embedding of the abstract program basis into000/111 has orthogonal conserved images, so the joint error is the maximum of the two program errors. The scalar exp(-i2bt) is genuinely common across programs and logical occupations. Coherent program superpositions consequently retain their correct phase. Such a mathematical embedding does not prepare three equal program bits or establish their native Record interpretation; the proposal explicitly retains those premises. Passive references preserve the operator norm, and the unhalved output trace/channel diamond bound2 times that norm is valid for the two isometries. No postselection or renormalization is used.

## Finite horizon, block loads and scaling

Since beta0<sqrt(2)b/D0 and beta1<sqrt(2)b/D1, the sufficient inequalities(13) imply the claimed horizon error for 0<eta<2. Their separate D0>2b condition remains necessary to the specified positive construction. Enabled error is uniformly bounded for all real times; disabled identity is only controlled over the stated horizon. Its Rplus phase is not a removable common scalar.

The seven-block convention is explicit: two Q blocks, two unconditional one-site compensations, one combined mediator/program block and two endpoint/program blocks. Their norm sum is D1+4b+2a0. The incident sums are3b+a0 at u,v, D1+2b at m, a0 at the endpoint program bits and D1-2b at the mediator program bit. Because a0<b and D1>2b, the mediator incident sum dominates. Splitting the mediator block into two separately counted projectors changes the incident-norm bookkeeping; the proposal does not conceal that convention. No direct u-v interaction is installed.

For the proposed symbolic family R=8pi/eta,D1=Lambda/2,D0=D1/R,b=D0 eta/(8sqrt(2)), one obtains a0=2b squared/D0=D0 eta squared/64. For 0<eta<=1, D1>D0>2b and D1+2b<Lambda. Enabled error is below eta/4. At T_gate=pi/a0, the disabled residual is below pi D0/D1=eta/8, while its mixing term is below eta/(4R). Their sum is below eta/2. All bounds hold throughout the absolute-time interval, not only at the endpoint. Substitution gives exactly T_gate=1024pi squared/(Lambda eta cubed). Thus the claimed sufficient bounded-strength scaling closes analytically, with no hidden large incident load.

This family changes supplied coefficients with eta; it does not guarantee robustness to their independent errors or supply those coefficients from a native law. At fixed effective strength increasing D0 also increases b, as stated. There is no free speed/precision gain or optimality claim. The full positive-Q operation has a -1 double-occupation phase at the one-head swap time and is correctly distinguished from ordinary SWAP.

## Exact sources, exposure and limits

Reviewed target739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 in full. Refreshed contextual source `mediated_program_cell/PROPOSAL.md`0e665329d8034e1bf2dfbbd4cfd918fc7f95451060906562d56fe04e5ff5928d and its full recorded check160fcc32d0936a9f090c62a2fab9dfb649ae800353c956df1e101945fdf3a115. The earlier construction uses DIFFERENT program-dependent dressed codes and different program vacuum phases. Its symbolic-program evidence was neither run nor reused as validation of the present Hamiltonian. Only the full Q convention, coordinate patch and supplied-law boundaries are contextual premises; all new matrices and estimates were reconstructed above. No original apparatus performance theorem or axiom claim is imported.

ROOT proposed the common-product algebra and the bounded-load ratio route; the resources worker authored this source. I did not author it. I have extensive shared mediator/positive-block and complete-output ancestry, but the present full-sector calculation is a distinct analytical check of this isolated model. Design exposure and same-model ancestry are explicit, not blind replication.

The result removes a PARTICULAR program-dependent dressed-head preparation premise by proving an approximate common literal endpoint/vacancy interface. It does not produce exact code invariance, permanent disabled identity, a preparation procedure, a decoder, native roles/coefficients/projectors, network interoperability or an apparatus replacement. Interacting neighbors can alter the low modes and gaps; only an exactly independent environment may tensor its own evolution onto both sides without new work. Full-joint initial preparation errors may be added by contractivity, but correct marginals alone are insufficient. Existing campaign certificates remain unchanged.

Only this review was written. No scientific or symbolic program, eigensolver, numerical dynamics, sweep, source/W/Git/PR/checkpoint/prompt/model edit or delegation occurred. Hashing was source identity bookkeeping. No retained status or publication is assigned.
