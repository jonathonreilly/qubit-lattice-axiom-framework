# Finite endpoint-seed router: distinct composition check

No required mathematical correction was found in the pinned complete proposal. Its equations (13)–(16) give a valid conditional finite-time, complete-output comparison for the explicitly supplied finite one-head Hamiltonian. The component interfaces, rather than merely their separate estimates, were checked below. The result removes supplied delocalized incoming-packet preparation for this model. It does not derive the supplied microscopic Hamiltonian, coefficients, program/input preparation, or native interpretation of coherent program states, and it does not supply permanent output storage, an old processor replacement, or an optimized runtime.

## Source identities and independence limits

All following paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

Complete new source read and SHA-256 verified:

* `common_product_finite_seed_router/PROPOSAL.md`: `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.

Complete new premise reads and SHA-256 verification in this task:

* `mediated_common_product_program/PROPOSAL.md`: `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.
* `mediated_program_attachment/PROPOSAL.md`: `55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a`.

Previously complete reads/checks in this same checking session, reused after refreshing and matching their hashes:

* `common_product_autonomous_interface/PROPOSAL.md`: `bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5`.
* `common_product_autonomous_interface_check/REVIEW.md`: `90c7926ed7c681286108afe5a9063a9f63f2be690026ff0abc56844214ab67b2`.
* `common_product_endpoint_launch/PROPOSAL.md`: `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`.
* `common_product_endpoint_launch_check/REVIEW.md`: `51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1`.
* `common_product_outer_boundary/PROPOSAL.md`: `af7dfe4193865bb80f9302fcb39f62c7be9ab7693d29b1b53bea8f620f8f2c43`.
* `common_product_outer_boundary_check/REVIEW.md`: `756514da092c820d3e19601565f6d60b174acc2aed26cfcad551e598f0020985`.

I authored the listed launch and outer-boundary checks. Those earlier checks are shared exposure and component evidence, not prior independent verification of this composition. ROOT supplied the proof plan and had read this proposal; the check is therefore neither blind nor model-diverse. I read the proposed formulas before reconstructing the common-space operator difference, Fourier identifications, normalization costs and scaling. No favorable parent assessment was treated as evidence. The workflow and skill snapshots already identified in the endpoint check are reused; no claim of remote-main freshness is made. This is a distinct bounded composition check, not formal audit or retained status.

## 1. Actual operator and early common-space comparison

The added port operator has n=0 diagonal j, ordinary internal diagonal 2j, diagonal 2j at the source-adjacent site and emitter, hopping -j internally and -gamma at the last bond. On the mediator basis vector it vanishes. The ideal central enabled bond raises each n=0 diagonal to 2j and adds hopping -j between ports; in the disabled sector it is absent. The absolute row and column sums of K and h_F are at most 4j. All displayed physical blocks are positive, including the endpoint block on its full two-qubit support. These bounded-operator assertions concern the one-head domain.

For the early reference, the source occupies n=M and its lead occupies all n<=M-1. The weak bond and all coefficients down to and including n=0 match the finite device away from the central modification. On the common integer-coordinate space the reference is completed by a disconnected positive Dirichlet half-line n>=M+1. The finite comparator has that same positive exterior and also a disconnected Dirichlet half-line n<=-1. At n=-1 the latter's diagonal remains 2j, so the only differences from the reference are the removed (0,-1) hopping, the programmed central connection, and (in the disabled branch) the changed n=0 diagonal. There is no distant hidden discrepancy near the seed.

Each multiplication propagates support at most one radial edge. Starting at n=M, h^r reaches n=0 first at r=M. The difference operator annihilates every vector supported strictly at positive n; hence the telescoping power identity shows equality through degree M and first permits a difference at degree M+1. This checks the off-by-one and the changed diagonal explicitly. Both extended norms are <=4j. Taylor expansion therefore bounds the difference by `2 sum_{m>=M+1}(4jt0)^m/m!`, with the isometry-distance cap 2. The argument applies to the whole seed subspace in both conserved program sectors, rather than adding errors for basis inputs.

## 2. Launch target and the two early comparisons

The source column and g_+ phase are the fixed checked ones; there is no phase fit to the intended router output. Since chi=1 on a nonzero interval where w>0, p_chi>0. The source's chi can be chosen C2 within the C1 launch theorem's domain. At fixed positive rho=gamma/j, g is C2 and compactly supported, with finite G_0,G_1,G_2. The stronger support restriction sigma'<pi/3 is valid and ensures vmax<2vmin.

One integration by parts with gap m+A and |phi''|<=2jt yields the site estimate `(G_1+2jt G_0/A)/(sqrt(2pi)(m+A))`. The decreasing-series integral comparison gives the stated T. This estimate is valid for either sign of the phase derivative and uses norm in the full internal/reference space.

The source's outgoing lead amplitude is O_t0(chi g_+). Dividing its spectral amplitude by positive sqrt(p_chi) changes only its unnormalized magnitude. Under x=ell-n, its full-integer Fourier continuation becomes exactly A_n(t0), including exp(ik ell) and exp(-it0 E). Zero extension of g to a full Fourier period proves ||A||=1. Consequently the source's normalized lead target is exactly the positively normalized P_(n<=ell)A. Its source coordinate n=M=ell+1 is excluded. Delta_launch<1 ensures that this projection is nonzero through the source theorem; there is no hidden division by zero even if a subsequent tail bound is loose.

For n=ell+1+m the derivative is `-1-m-t0E'`, so the missing right tail is bounded by d_right=T(t0,1+t0vmin). For any unit vector and a nonzero projected part, the distance to its normalized projection is at most twice the discarded norm. Thus the replacement by A costs at most 2d_right. If the bound exceeds one it remains a valid loose distance bound; actual nonzero projection was established separately.

The ideal router's incoming component on n>=0 is exactly the same A_n, not merely a packet with a similar momentum distribution. Its outgoing component has phase `(n+ell+1)k-t0E` from S=exp(ik)C. On negative n=-1-m the A derivative has lower bound ell+1+m-t0vmax; on nonnegative n=m the unwanted outgoing derivative has the same bound. These discrepancies lie on disjoint radial ranges, so their squared norms add, giving sqrt(2)T(t0,A_early), without any assumption about xi and Cxi being orthogonal.

Combining the early power estimate, the launch estimate 2delta_launch, the right-tail projection cost and this disjoint-range comparison gives exactly e0 in (7). The negative-coordinate embedding is then harmless: both endpoints of that comparison are zero at negative n. No negative-coordinate mass or omitted emitter output is silently discarded.

## 3. Fixed-diagonal evolution through the junction

Here the outer-boundary lemma's phase index is L=ell and its emitter coordinate is M=L+1. Its two edges are therefore (ell,ell+1) and (ell+1,ell+2). The source perturbation changes -j to -gamma on the first, changes -j to zero on the second, and leaves all three diagonals at 2j. The finite summand is exactly h_F. The exterior starts at M+1 with diagonal 2j; this requires its additional positive j onsite term and is not the extension by zero.

The local finite block, in source/adjacent-lead order, is precisely `Q_gamma+(2j-gamma)n_s+(j-gamma)n_0`, with one-head matrix [[2j,-gamma],[-gamma,j]] before including the next lead bond, and double-occupation energy 3j. Thus both positivity and the exact source diagonal correlation are preserved. A full Laplacian deletion would not yield this operator and is not used.

The perturbation's three-site matrix has eigenvalues 0 and ±sqrt((j-gamma)^2+j²). Port copies and program/reference identities do not increase this operator norm. At each of its three sites, the exact router phases satisfy incoming gap at least tvmin-1 and outgoing gap at least 2ell-tvmax. Conditions (8) supply the strict margins needed by the checked lemma.

The reproduced twice-IBP expression includes -3g'phi''/(phi')³, -g phi'''/(phi')³, and +3g(phi'')²/(phi')⁴. Bounding |E''| and |E'''| by 2j gives the reproduced H, and integrating the inverse-square envelopes gives exactly B_window. The sqrt(3) factor counts radial sites, each already carrying the full port/program/reference norm. Ordered Duhamel uses the exact Psi(t) on the right and unitarity of the perturbed propagator on the left. Propagating the e0 error adds it once, proving (10). It does not require the actual evolving state to have small boundary amplitudes independently of this bound.

## 4. Final target, normalization and vacancy

At time t_f the incoming phase derivative is ell-n-t_fE'<=-(n+A_late). Hence its complete nonnegative-radial norm is at most d_late. The exact Psi(t_f) has norm one by the unitary router transform, so its outgoing amplitude B has q_out>=1-d_late. Assuming d_late<1 makes normalization legitimate. Replacing B by B/q_out costs at most another d_late, giving 2d_late total.

The discarded outgoing coordinates begin at n=ell+1=M, not at M+1. Their phase derivative is at least 2ell+2+m-t_fvmax. The T estimate bounds that unnormalized tail. Dividing by q_out and using its lower bound yields d_out exactly as written. If d_out<1, the ordinary-site projection is nonzero; its normalized-projection cost is at most 2d_out. The final beta_F is the positive normalization of this same B projection, so the two normalization steps do not introduce a different target phase.

The retained interval is 0<=n<=ell on each port. It excludes both emitters, while the actual source amplitudes stay included in the full vector error. B retains the translation phase exp(ik ell), scattering phase exp(ik), and dispersion exp(-it_fE). It is a single scalar radial packet independent of input xi and program. The path operation C acts on the internal vector. This proves (13) with all four comparison costs present once, not with a partial trace or a separately fitted program-dependent packet.

## 5. Whole-time microscopic replacement

Reading the microscopic cell terms directly gives the scalar 2b from the two compensations even when the head is outside the cell. On an external-head column the cell is in its head vacuum and has precisely that energy. On its one-head subspace the symmetric/mediator matrix is [[a,-sqrt(2)b],[-sqrt(2)b,D]], yielding the enabled low eigenvector with r0=sqrt(2)b/D0 and eigenvalue zero after subtracting 2b. In the disabled sector its low eigenvalue is -epsilon1 and r1=sqrt(2)b/(D1+epsilon1). These are the source quantities used in (14).

The dressed map fixes every external-head basis vector and changes only the cell endpoint symmetric direction. Its distance from the literal map on the extended total-one-head space remains kappa. K acts only on endpoint/lead heads and their occupations and leaves mediator vacancy invariant, proving KJ=JK_log on this entire logical domain. K also preserves total head number, so restriction to one head loses no evolution column here. Its combined norm, rather than the sum of all local block norms, is <=4j.

The dressed residual is `K(J_d-J)-(J_d-J)K_log-J_d P1 epsilon1 R_+`, of norm at most 8j kappa+epsilon1. Rectangular Duhamel plus the two literal/dressed endpoint replacements gives 2kappa+t_f(8j kappa+epsilon1). This reconstruction checks that the entire physical duration t_f is charged, including launch. No isolated-cell permanence or commutation with the ideal routing bond is required. The residual includes mediator output, and the final scalar exp(-i2bt_f) is necessary. Adding this uniform map error to the ideal composition proves (15); arbitrary passive references preserve each operator norm. The usual two-isometry trace/channel bound supplies min{2,2e_total}.

## 6. Ordered existence and finite resources

At fixed rho and cutoff, w,u,g and all derivative norms are independent of overall j. R0 is controlled by rho²u0, while L0 and d_right decay as u0=jt0 grows. The nonvanishing spectral contribution tends to 2sqrt(P) within delta_launch and is made small first through rho. The constants can deteriorate with rho; the stated order allows u0 to be chosen only afterward and does not assume uniform derivative bounds.

After multiplying B_window by d_hop<=sqrt(2)j, its incoming part is bounded by a fixed constant divided by u0(vmin/j)-1. It is therefore controlled by the same early choice uniformly over later t_f. Since vmin/j>1 and vmax/j=2, a constant alpha exists strictly between 1/(vmin/j) and 1. With t_f=alpha ell/j, A_late and A_out grow linearly in ell and jt_f divided by either gap remains bounded. Their T estimates tend to zero; d_out's denominator tends to one. The early gap grows while jt0=u0 is fixed. The early factorial remainder tends to zero with degree ell+2 at fixed argument 4u0.

For the outgoing boundary term, qo(t_f)=(2-2alpha)ell and jt_f/qo(t_f) is bounded. Its coefficient A_o is therefore bounded at fixed rho, cutoff and alpha, and d_hop times its integrated inverse-square term is O(1/ell). All strict window and normalization conditions hold eventually. This proves simultaneous arbitrary ideal accuracy, not merely separately small incompatible terms.

With s=jt_f fixed after these choices, kappa<=sqrt(2)eta and epsilon1/j<2zeta give (16). Reducing eta,zeta subsequently changes j and both physical times while leaving u0,s,rho,ell and every ideal error unchanged. Thus the physical replacement can be made small without undoing the ideal choices.

For the proposed cap scaling, D1=Lambda/2, D0=zeta Lambda/2, b=eta zeta Lambda/2, j=eta²zeta Lambda/2. The largest mediator load is Lambda(1/2+eta zeta)<9Lambda/16. The endpoint load is Lambda zeta(3eta+4eta²)/2<7Lambda/64 in the stated domain. The other displayed loads, including 5j and 3j, are also strictly below Lambda. D1>D0>2b follows from zeta<1/2 and eta<=1/8. There is no fixed-time claim at this cap; t_f=s/j is finite for each positive parameter choice but may be very large.

The cell has three heads and three program qubits. Each port adds sites 1,...,M, hence 6+2M qubits. Each port adds M-1 ordinary bonds plus one combined B block, hence 7+2M positive blocks under the cell's combined mediator-projector convention. Full block norms are 2j for Q_j and 3j for B. Each central endpoint receives an additional 2j incident bond norm, giving 3b+a+2j=3b+4j. An emitter-adjacent site receives 2j+3j=5j, and an emitter 3j. M>=3 separates these categories. Straight outward extensions of the specified cell endpoints provide the claimed nearest-neighbor added supports; no effective u-v bond is mistakenly counted as physically installed.

## Scope and verification record

The mathematical outcome is a finite static conditional construction from literal endpoint positions with all other heads vacant, admitting a complete normalized output estimate at a selected observation time and a finite local incident-load cap. Arbitrary coherent encoded input is supplied; only basis program/path inputs are sitewise occupation products. Exact interactions, role assignments, occupation frame, coefficient correlations, absent extra couplings and legal program contents remain premises. Their derivation from a native physical law or their realization as lawful Records remains a separate identification problem, not an algebraic defect repaired by this proof. Finite recurrence and lack of capture remain explicit limitations.

Only this report was written. No scientific executable, simulation, symbolic solver, broad sweep, source edit, Git/PR/canonical/checkpoint/editable-prompt change, model override, delegation or other-chat message was used. Source hashing and directory creation were bookkeeping. The report assigns no retained or formal audit status.
