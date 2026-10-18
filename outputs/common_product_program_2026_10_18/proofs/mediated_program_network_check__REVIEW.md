# Distinct analytical check of the disjoint-cell program chain

Conditional support, with no required correction found, for `mediated_program_network/PROPOSAL.md` SHA256 `1d830ee1638794876d2a5062f436be9e32b484fef0c79de095aa54d16c0e5edc`. I read the complete source and reconstructed its tensor norm, local residual, full evolution estimate, physical layout/load counts and explicit sufficient family. No numerical program or parameter sweep was used.

## Exact premises and exposure

The single-cell source739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 is my author work. Its distinct check809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6 was read in full for this task. Both identities and the network source identity were verified from the actual files. I also authored the provisional attachment55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a. That argument is contextual exposure, not an independently checked premise needed by the network proof.

ROOT authored this network construction after suggesting the original single-cell and attachment routes. I did not author the network. This is a distinct reconstruction of its new assembly and scaling steps, with shared model/source exposure explicitly disclosed; it is not blind validation or rechecking my own single-cell theorem independently. The accepted exact single-cell intertwiners, positive block conventions and supplied-law restrictions are reused at their stated scope.

## Tensor overlap on the full domain

In the logical vacuum/symmetric/antisymmetric/double basis for each legal program p, J_i*Jd_i has eigenvalues1,alpha_(p,i),1,alpha_(p,i). This is a positive Hermitian overlap, not merely a lower bound on individual column fidelity. Since r1_i<r0_i, its least eigenvalue is alpha_(0,i). Tensoring the overlaps therefore gives a positive operator with least eigenvalue product_i alpha_(0,i). Both tensor maps are isometries, so

 (Jd-J)*(Jd-J)=2I-2 tensor_i(J_i*Jd_i).

The claimed exact kappa_all=sqrt(2-2 product alpha0) follows. All minimum eigenvectors are in the allowed domain, so this is an equality rather than an unattained upper envelope. Coherent programs, entangled endpoint states and passive references do not invalidate the operator identity.

For numbers alpha in[0,1], 1-product alpha<=sum(1-alpha); also2(1-alpha0_i)<=r0_i squared. This proves kappa_all<=sqrt(sum r0_i squared). Restricting exactly the same argument to the two cells touched by an edge proves kappa_e<=sqrt(r0_i squared+r0_(i+1) squared). No factor counting input basis columns or all other cells is missing.

## Local physical residual and all outputs

Each external bond Q_c(v_i,u_(i+1)) acts only on literal endpoints. On the entire two-cell logical/program domain it interwines with Q_c(R_i,L_(i+1)), including its double-occupation diagonal2c. It has norm2c on both physical and logical spaces. Subtracting this exact literal intertwiner from the dressed one gives

 K_e Jd_e-Jd_e Klog_e
 =K_e(Jd_e-J_e)-(Jd_e-J_e)Klog_e,

and hence norm<=4c_e kappa_e. Tensoring the remaining dressed isometries preserves that norm. This proves localization to the two incident cells even though their logical evolution generally does not commute with neighboring terms. It does not assume the dressed network subspace is invariant.

For the cell terms, the exact residual is minus epsilon_i times the full logical projector P1_i Rplus_i, followed by Jd. Its norm is epsilon_i, with double occupation included. Summing the cell and edge residuals by triangle proves equation(3). The common scalar2sum b_i occurs on both sides and cancels from the residual legitimately; it is not dropped from the target evolution.

Rectangular Duhamel for H_net Jd-Jd A_net gives |t| times that residual bound. Replacing each endpoint isometry Jd by J costs kappa_all twice, proving equation(4). The cap2 is valid because both complete comparison maps are isometries. This proof needs no use of the generic attachment lemma, no Gronwall iteration and no commutation of logical terms. It applies for positive and negative times on the full tensor endpoint space, all legal programs and references, including head-number sectors reached when endpoints exchange heads with neighboring cells.

Every mediator and program output remains in the comparison. The trace/channel bound twice the isometry norm is valid; it does not imply correctness from input marginals alone or an exact mediator reset.

## Physical geometry, positivity and counts

For neighboring indices, v_i has x-coordinate3i+1 and u_(i+1) has3i+2, so the added bond has cubic distance one. No cell qubits overlap. The program row is displaced by one unit in y and shares no head coordinate. All internal supports retain the single-cell nearest-neighbor geometry. Geometrically adjacent but uninstalled program couplings are an explicit supplied absence, not an inferred property of a homogeneous law.

There are6N qubits,7N internal positive blocks in the combined mediator-block convention and N-1 additional positive Q blocks, giving8N-1. Conservation of program occupations and total head number follows termwise. The two legal values in each program triple and their preparation remain external assumptions; mixed triples have physical dynamics but are not in the promised interface domain.

Each endpoint has at most one external bond, of norm2za, so its incident sum is at most3b+a+2za. The mediator sum remains D1+2b. Program-bit sums remain a or D1-2b. The full sum bound N(D1+4b+2a)+2(N-1)za is consistent with those block norms. Splitting the combined mediator block into separately counted projectors would require different load bookkeeping; the declared convention is explicit and positive.

## Uniform coefficients and sufficient family

For c_e=za and T=pi/a, substitute kappa_all<=sqrt(N)r, kappa_e<=sqrt(2)r and epsilon<2b squared/D1, with a=2b squared/D0. This gives exactly

 2sqrt(N)r+4sqrt(2)pi z(N-1)r+N pi D0/D1.

The ideal evolution remains exp(-it A_net), not a product of isolated swaps. The possible logical noncommutation is not removed by naming T an exchange scale.

For equation(6), a=r squared D0 and b=rD0/sqrt(2) satisfy the required exact correlation. With0<eta<=1,N>=1,L>=1, r<=1/16; R=16pi N/eta>1. Thus D1>D0>2b. The mediator load is below Lambda because D1=Lambda/2 and sqrt(2)rD0<Lambda/2.

For endpoints, dividing the actual incident sum by D0 gives3r/sqrt(2)+(1+2z)r squared. The first is at most3/(16sqrt(2)). The other contributions are at most1/256 and1/(256sqrt(2)pi), since2z< L/(sqrt(2)pi), r squared<=1/(256L squared), and L>=1. Their sum is below1, proving endpoint load<D0<Lambda for every z>=0, not just small z. All program loads are likewise below Lambda.

The first two error terms are bounded by2NLr=eta/8, since sqrt(N)<=N and N-1<=N. The residual term is strictly below Npi/R=eta/16. Hence the complete error is strictly below3eta/16<eta throughout |t|<=T. Strictness is valid here because epsilon<2b squared/D1 with N>=1; there is no incorrect strict comparison between two saturated capped expressions.

Finally D0=Lambda eta/(32pi N) and r squared=eta squared/(256N squared L squared), so a=Lambda eta cubed/(8192pi N cubed L squared). Therefore T=8192pi squared N cubed L squared/(Lambda eta cubed), as claimed. N=1 removes all external bonds and remains admissible; the z-dependent family is then only a loose parameterization, not a claimed necessity. No optimal scaling or fixed-coefficient-in-N assertion follows.

## Limits and disposition

This proves a conditional finite-chain all-output comparison for disjoint cells with exact endpoint-only bonds, and an explicit bounded-incident-load family. It is a restricted network result that goes beyond the isolated-cell statement; it is not a compiler for an arbitrary graph, overlapping-cell compatibility, an old-processor replacement or an algorithmic correctness theorem. The prescribed logical many-body target may itself have nontrivial dynamics.

Exact roles, omitted couplings, block shapes, correlated coefficients, occupation frame, program/endpoint preparation and their physical interpretation remain supplied. Native Record formation, arbitrary faults or strong contacts, mediator exchange, capture/reset/reuse and finite permanent halt are not established. All finite-time and phase qualifications are preserved.

Only this review was written. No scientific or symbolic program, numerical calculation run, dynamics, sweep, source/W/Git/PR/checkpoint/prompt/model change or delegation occurred. No retained-audit or publication status is assigned.
