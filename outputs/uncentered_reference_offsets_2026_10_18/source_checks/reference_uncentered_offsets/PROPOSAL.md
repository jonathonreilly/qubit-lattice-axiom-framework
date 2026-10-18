# Uncentered static reference offsets with a fixed logical loading operation

New bounded author derivation; distinct check required. The result removes the exact mean-zero requirement on the reference offsets in the checked cubic-reference loader, at a factor-two smaller per-site interval. It retains the original P gap and its original free-revival calibration. The complete target reference profile depends on the actual offset mean by an explicit formula; the logical operation does not. No actual coefficient, timed correction or switching is introduced by the proof.

For every static assignment |delta_v|<=lambda/(2N), the same finite full-loader policy given below has complete-vector error less than epsilon/16 and unhalved stabilized complete-channel error less than epsilon/8. The counts, incident cap, finite window and eventual sufficient size/time orders are unchanged. Unknown individual offsets and unknown mean do not enter that policy. This is an extension of a structured supplied Hamiltonian theorem, not a generic frequency-noise, native-preparation or energy-conserving operation claim for the actual unequal free spectrum.

## 1. Exact dependencies and input contract

Research paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. The direct mathematical parent is W/docs/ACTIVE_ENERGY_CUBIC_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md, W=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree, SHA256 8023deeb062288b75065576d89f726d528e077e7b10fac90333b33c61fbff110. ROOT supplied its publication identity PR9746, head8e119e9d45c30498a111e4e36d22f0676fdec4c6; this task makes no new Git/remote claim. The parent was fully read in the immediately preceding coherent task and its unchanged hash refreshed here.

The directly used changed theorem is reference_gap_detuning/PROPOSAL.md SHA256 d2a4ffae8b2f7d2e2fc0aae7c654f78665c400e16d9d8e0dfb7eb4689c380c23, with distinct check reference_gap_detuning_check/REVIEW.md SHA256 11787f41138baea458ff7451424fabedde8b4a5f5fe185f1c30220311f38cf9e. Both were completely read here. The review supports the exact centered and simultaneous weighted/centered interfaces, including their actual-free-energy limitation. It does not check the present uncentered extension.

Section8 of that source uses weighted_cubic_reference/PROPOSAL.md b2f4aaa21de3508c3d51ebf51fc6132a6ad16b8a9a836b3bc1ef9b75973294cb and check8ce18b7cdea55345c292d391154713dff1940ff037e767aff96d47a523ccbb36, completely read in the preceding coherent task. No new independent reconstruction of the unchanged gate, gap, Green function or clock theorem is claimed here. Uniform reference weights are the special case eta=1.

Keep the parent's actual finite four-rail delayed suffix and reference cube. The input is its endpoint head with a=1, arbitrary coherent logical b/Q/P input and arbitrary passive references, blank R and other head sites, and the supplied reference product beta=|+>^N. Old P/passive correlations are retained in Q/passive outputs. All output head, logical, reference and passive systems remain in the comparison. No reference or environment is reset or traced away to state the theorem.

Write NB=sum_v n_Bv and G=n_P+NB, with identities on the other factors. The actual reference occupies the cubic n-by-n-by-n grid, N=n^3, with positive bonds kappa_uv(I-SWAP_uv), each kappa_uv in [eta kappa_max,kappa_max]. Q and R remain freely degenerate. The local non-head blocks use

 H_S=aX_Q+b(Z_Q+Z_P)+c Z_Q Z_P,
 a=lambda/sqrt(2), b=sqrt(5)lambda/4, c=3lambda/4,
 Vloc=g(sigma_P^+ sigma_e^-+sigma_P^- sigma_e^+),
 g=sqrt(2)lambda, s=a+2b+c+g.

Their installed positive-block forms, scalar s and the complete head construction are exactly those of the parent. P's installed occupation remains omega n_P, omega>0. The ONLY occupation change is replacement of each reference block omega n_Bv by the positive block (omega+delta_v)n_Bv. A negative delta is not installed as a separate negative block.

## 2. Algebraic mean removal on the complete physical Hilbert space

Take any real static assignment, define

 mu=(1/N)sum_v delta_v,
 d_v=delta_v-mu,
 D_c=sum_v d_v n_Bv,  sum_v d_v=0.                 (1)

Let H_c denote the entire checked centered physical loader with reference offsets d_v, P gap omega, and all original head and local blocks. Let H_delta be the actual entire uncentered loader. Exactly,

 H_delta=H_c+mu NB=(H_c-mu n_P)+mu G.               (2)

Every term of H_c commutes with G. The grid swaps conserve NB; the corner exchange conserves n_P+NB; H_S is diagonal on P and acts arbitrarily only on degenerate Q; the physical delayed-suffix data blocks are diagonal on P; head-only terms and all occupations commute. Also [G,n_P]=0. Therefore on the FULL finite Hilbert space, not just the symmetric reference sector or a one-head expectation,

 exp(-it H_delta)=exp(-it mu G)exp[-it(H_c-mu n_P)]. (3)

The auxiliary H_c-mu n_P is used only as a bounded self-adjoint comparison generator. No claim that a negative term is installed, or that this comparison generator has an independently verified positive-block cap, is necessary. The actual positive device remains H_delta. The centered device H_c meets the separately checked hypotheses below.

Ordinary Duhamel, using ||n_P||=1, gives the complete induced bound

 ||exp[-it(H_c-mu n_P)]-exp(-it H_c)||<=|mu|t,
                                                       t>=0. (4)

This bound is independent of the number of reference sites. The potentially extensive collective rotation in (3) is kept EXACTLY, including its phase; it is not replaced by the identity. Treating mu NB by its norm N|mu| would lose this distinction.

Let E_in be the parent's input isometry. Suppose at a time t the centered theorem supplies the normalized complete target

 V_c(t)xi=Phi(t) E_out U_f xi tensor beta_omega(t),
 Phi(t)=exp[-i(C_head+s)t] i^L exp(-i pi/4),
 U_f=I_a X_R C_P^(b) SWAP_QP,
 beta_omega(t)=exp(-it omega NB)|+>^N,
 ||exp(-itH_c)E_in-V_c(t)||<=e_c(t).                (5)

E_out embeds the head at the prescribed external endpoint and all other heads in their vacancy states. U_f is the parent's fixed operation on the supplied blank-R input; its phase convention is unchanged. Applying exp(-it mu G) to this target gives EXACTLY

 Phi(t) E_out [exp(-it mu n_P)U_f xi]
                       tensor beta_(omega+mu)(t).  (6)

This equation makes no commutation assumption between n_P and U_f; the P rotation is AFTER the whole U_f. Since ||exp(-it mu n_P)-I||<=|mu|t, comparison with the new normalized target

 V_delta(t)xi=Phi(t) E_out U_f xi
                       tensor beta_(omega+mu)(t),
 beta_(omega+mu)(t)=
       (exp[-it(omega+mu)n]|+>)^N                  (7)

yields

 ||exp(-itH_delta)E_in-V_delta(t)||
                   <=e_c(t)+2|mu|t.               (8)

All tensor identities and bounds are stable under arbitrary passive references. Equation(8) pays both the changed dynamics in (4) and the residual P phase in (6). Neither is silently canceled. No exact SWAP theorem for the shifted gap omega+mu is assumed. In particular omega tau, not (omega+mu)tau, remains the calibrated revival below.

Equation(7) defines the output in advance as a function of the actual supplier assignment. It is not an arbitrary best-fit apparatus state. The common reference is independent of the logical input, retains its full collective phase, and generally differs from the product freely evolved with every individual omega+delta_v. The centered ferromagnetic comparison controls the remaining differences. A fixed supplier-independent complete apparatus target is NOT asserted.

## 3. Explicit independent interval and unchanged full-loader policy

Fix Lambda>omega>0, M=Lambda-omega, 0<epsilon<=1 and 0<eta<=1. Put C_P=(sqrt(5)+3)/2+2sqrt(2). Choose exactly the checked simultaneous policy

 n=ceil[(8192 pi^2/epsilon^2)^(1/3)], N=n^3,
 kappa_max=M/32, Delta_w=eta kappa_max/(3n^2),
 L=ceil max{16,(8192/epsilon)^2}, J_budget=M/64,
 lambda_max=min{omega/2, M/(4C_P), Delta_w/16,
                 epsilon eta kappa_max/(524288 n),
                 4J_budget/(L+1)},
 m=ceil[omega/(2lambda_max)], lambda=omega/(2m),
 alpha=lambda/2, tau=pi/lambda,
 J_c=lambda(L+1)/4, C_head=4J_c,
 w=min{epsilon/[128(omega+9lambda/4)],
               epsilon/(1024lambda),epsilon/(64lambda L)}.  (9)

Choose any grid weights in their stated positive interval and ANY static real reference offsets in the independent box

                    |delta_v|<=lambda/(2N).       (10)

There is no sum constraint, correlation constraint between weights and offsets, or need to know the individual coefficients or mean when selecting (9). Deterministic adversarial cochoices are included; statistical independence is unnecessary. From (1),(10),

 |mu|<=lambda/(2N), |d_v|<=lambda/N, sum_v d_v=0.   (11)

Thus H_c satisfies precisely the checked simultaneous centered hypotheses with the SAME omega, lambda and geometry. In particular its centered theorem provides e_c(t)<7epsilon/128 throughout [tau-w,tau+w]. Its inverse, gap, star and late-suffix arguments need no new transfer by analogy: they are applied to this actual centered comparison assignment. The full interval lies in 0<t<2pi/lambda, as certified by (9).

On this entire interval the added error in (8) obeys

 2|mu|t<=lambda t/N<2pi/N
 <=epsilon^2/(4096pi)<epsilon/128.                 (12)

The last strict inequality holds for 0<epsilon<=1 since epsilon<32pi. Consequently the new complete theorem is

 sup_[tau-w,tau+w] ||exp(-itH_delta)E_in-V_delta(t)||
                         <epsilon/16.             (13)

The unhalved stabilized complete-channel error is <epsilon/8. For mixed logical/passive inputs this follows by purification and contraction, or the isometry inequality ||V rho V*−W rho W*||_1<=2||V−W||. All apparatus outputs are retained. Since the ideal target has external endpoint occupancy AND R=1, the actual probability of that event is

                 >1−(epsilon/16)^2.              (14)

No normalized conditional guarantee for an arbitrarily rare event is inferred. There is no current-record all-time identity supplied by this bound. The target is a fixed logical U_f at every time in the chosen window, with the explicit time-dependent scalar and common reference profile (7). It is not the aged logical contract exp(-it omega n_P)U_f. At the center the non-revived mean contribution is still paid by (12), rather than declared absent.

For an input-independent classical distribution of observation time supported in this window, convexity gives the same complete trace/diamond allowance against the common mixed reference target integral |beta_(omega+mu)(t)><beta_(omega+mu)(t)| dnu(t), fixed endpoint and U_f. The scalar Phi cancels in density matrices. This statement does not cover coherent time control or input-correlated time/supplier selection. The pure-vector statement retains Phi exactly.

## 4. Positivity, full-support cap, counts and orders

Actual occupations are strictly positive:

 omega+delta_v>=omega-lambda/(2N)
                  >=omega(1-1/(4N))>0.            (15)

The formal centered comparison has |d_v|<=lambda/N, so its positive occupations and cap were checked independently; no actual implementation of the mean decomposition is needed. The actual offsets are smaller than that existing cap allowance. In particular lambda<=M/(4C_P), C_P>4 imply |delta_v|<M/8. Charging the actual full-support norms, safe inherited ceilings are

 P<=omega+M/4+M/8, Q<M/4, R<=M/4,
 each head<=(5+sqrt(2))M/64,
 noncorner reference<=omega+M/2,
 corner reference<omega+9M/16<Lambda.              (16)

The weighted bonds are charged by kappa_max, not by their compressed values. No installed block, site, edge or scalar repair is added or removed. The actual counts remain

 qubits: 4L+N+7,
 positive blocks: 8L+N+40+3n^2(n−1).               (17)

The reference grid bonds remain nearest-neighbor, with negative-coordinate cube disjoint from the suffix and head geometry. The full supplied device retains the parent's range<=9 and degree<=8; the whole loader is not being reclassified as nearest-neighbor.

At fixed eta,omega,M>0, n=Theta(epsilon^(−2/3)), N,L=Theta(epsilon^(−2)). The gap restriction in (9) scales as eta M epsilon^(4/3), the local restriction as eta M epsilon^(5/3), and the clock-cap restriction as M epsilon^2. The clock eventually dominates. Revival rounding changes lambda by less than a factor two. Thus the unchanged sufficient full size and time are Theta(epsilon^(−2)) and Theta(M^(−1)epsilon^(−2)); the allowed independent per-site offset ceiling lambda/(2N) is Theta(M epsilon^4). This eventual statement is not uniform as eta approaches zero, and the constants are enormous.

For comparison, direct full-norm Duhamel on an arbitrary uncentered box |delta|<=d only gives ||sum delta_v n_v||<=Nd and hence a sufficient d=O(epsilon/(NT))=O(M epsilon^5) for an O(epsilon) addition on this horizon. The present factor-one-over-epsilon improvement compares sufficient certificates, with a supplier-dependent reference output in the new certificate. It is neither a necessary tolerance nor an optimality statement. In particular it does not claim the same improvement while requiring the original fixed beta_omega target.

## 5. Why the remaining qualifications are essential

An uncontrolled mean really does produce the collective symmetric term mu NB. It cannot be discarded as a scalar on |+>^N or on the full symmetric reference space. The failed inference would be to apply the centered proof directly to uncentered coefficients and retain its exact projected generator. The successful route instead factors the conserved charge and pays two nonextensive P effects. Its only smallness requirement on the mean is already implied by (10). This is not removal of all frequency precision or of calibration of P's omega and the original lambda revival.

The complete target reference depends only on the assignment mean, not on the logical input or its passive correlations. If the supplier assignment is unknown, the theorem gives a uniform family of such complete targets; it does not supply knowledge of the actual mean. If assignments are classically randomized independently of the logical input, the corresponding common reference mixture is allowed after averaging (13). A logically correlated assignment is outside this preparation contract. The theorem does not replace the target by tracing away a troublesome reference, nor assert closeness to any fixed supplier-independent pure reference.

Nominal H_E=omega G still commutes with every installed term, and so does the total static Hamiltonian with itself. The actual free occupation operator is H_E+sum delta_v n_Bv and is generally NOT conserved: grid swaps fail for unequal delta_u,delta_v, and the P-corner exchange fails already for a nonzero uniform mean. Even all delta_v=mu gives a nonzero free-energy exchange mismatch with P. No claim of conservation of the actual unequal free energy is recovered by (3). Q and R remain freely degenerate; undeclared active H_PE is not included.

All product reference coherence, endpoint head/logical supply, blank record and apparatus, exact positive matrix forms, absence of additional interactions, weight lower bound, P frequency and clock calibration remain premises. The construction has no autonomous preparation/cooling, output capture, reset, reference reuse or permanent halt. No output-ray or no-revival theorem is imported. The full Hamiltonian continues evolving after the finite window.

## 6. Exposure, work record and decisive next check

ROOT proposed investigating mean removal by splitting off the conserved total charge, and independently suggested an auxiliary shifted-P-gap comparison while this derivation was in progress. I used the charge-factor route (2) so that neither an auxiliary changed positive-device cap nor a changed revival hypothesis is required. I independently derived (3)–(12), including the necessary second P-phase error, and applied the exact checked centered source only to its actual admissible assignment d_v. I authored the centered source and several inherited interfaces, and synthesized the tolerance manuscript; this is source-exposed shared-lineage author work, not an independent check of them or a retained audit.

A distinct check should prioritize: full physical [H_c,G]=0 despite the noncommuting SWAP operation; order of n_P after U_f in (6); use of ordinary Duhamel on the full auxiliary self-adjoint generator without a positivity claim; both |mu|t contributions; the centered interval (11); the nonextensive budget (12); and the distinction between a fixed logical U_f and a supplier-dependent complete reference output. The result is a candidate conditional extension until that check, despite accepted dependencies.

Only this PROPOSAL.md was written. Work consisted of analytical derivation, complete necessary source/review reading and deterministic file/hash bookkeeping. No scientific solver, simulation, external search, delegation, Git/canonical/checkpoint/axiom/editable-prompt/model change, historical source edit or publication was performed. No editable prompt changed.
