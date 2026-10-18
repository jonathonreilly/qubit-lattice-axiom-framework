# Distinct analytical check of the occupation-sector program chain

Conditional support, with no required correction found, for `common_product_sector_transport/PROPOSAL.md`, SHA256 `a94697cf9dd3c0b62a38b97a3cc64640b7d3eac41d48f625e1595ec7d857dd76`. I read the complete source and independently reconstructed the sector norm, residual, sufficient family and exact path spectrum. The conclusion is a complete-output comparison on the explicitly restricted vacuum-plus-one-head input space, not an arbitrary-occupation network or transport-fidelity theorem.

## Sources and exposure

The exact network premise is `mediated_program_network/PROPOSAL.md`, SHA256 `1d830ee1638794876d2a5062f436be9e32b484fef0c79de095aa54d16c0e5edc`, with check `4e6e229f5cbc92321f72bf71289ed8f911c7663773e3731fa0ab54997f22db77`. Both were read completely for this check and their hashes verified. The unchanged parent cell source `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088` and my earlier full review `809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6` supply the exact four-state intertwiners, scalar and positive-block conventions at their already checked scope.

The present author authored the cell and attachment and checked ROOT's network. I checked the parent cell and attachment and authored their publication syntheses; I did not author this sector sharpening. ROOT suggested the occupation-sector and uniform-path questions, and stated a provisional favorable reading before this check. That exposure and shared ancestry are explicit. My prior review is not counted as fresh independent verification of itself; the new restricted-domain bridge and boundary calculation are reconstructed below.

## Sector invariance and exact distance

Every installed exchange conserves total head number, and the remaining terms are diagonal in head occupations. Each program occupation is separately conserved. The literal and dressed injections preserve head number: the dressed one-head symmetric vector mixes only the endpoint symmetric state and mediator occupation; vacuum is unchanged. Thus the physical vacuum-plus-one-head space and logical H_le1 are invariant under their respective Hamiltonians. This is an actual invariant-domain argument, not a projection applied during evolution.

Fix a legal program string. The one-head space decomposes orthogonally by occupied cell. On each such summand J*Jd has eigenvalues alpha_(p,i) and 1; all other cell factors act on head vacuum with overlap 1. The vacuum summand also has overlap 1. Hence the least overlap on the domain containing every legal program is min_i alpha_(0,i), attained by enabling a minimizing cell and occupying its symmetric endpoint mode. Since the overlap is Hermitian positive,

    (Jd-J)*(Jd-J)=2I-2J*Jd,

which proves exactly kappa_1=sqrt(2-2alpha_min), not merely a bound on individual columns. Orthogonal program sectors give a maximum even for coherent or entangled programs; passive tensor references preserve it. The elementary inequality 2[1-(1+r^2)^(-1/2)]<=r^2 proves kappa_1<=r_max. The full tensor-space product overlap is a different norm and is correctly not used here.

## Residual and full outputs

On H_le1, P1_i Rplus_i is supported only on the symmetric one-head mode in cell i with its disabled program. These supports for distinct i are orthogonal. Vacuum and antisymmetric modes are annihilated. Therefore the norm of their epsilon-weighted sum is exactly epsilon_max, attainable by a disabled symmetric mode of a maximizing cell. There is no sum over cells in this restricted norm. On the larger occupation domain that argument fails, as the source explicitly states.

The external endpoint bonds form a matching: v_i and u_(i+1) never occur in another external bond. On the physical one-head space each bond is c_i[[1,-1],[-1,1]], with eigenvalues 0 and 2c_i; all other endpoint and mediator coordinates are zero blocks. The same holds logically. Consequently both attachment norms are 2c_max, including N=1 with value zero. In particular the diagonal entries from Q_c have not been discarded.

Subtracting Kphys J=J Klog gives the exact dressed residual identity. Jd-J maps into physical H_le1, and Klog preserves logical H_le1, so the restricted norms are applicable to both terms separately. Their sum is bounded by 4c_max kappa_1. Combining with the exact cell defect gives epsilon_max+4c_max kappa_1. No invariance of the dressed code or commutation of adjacent logical terms is assumed.

Rectangular Duhamel followed by two replacements of Jd by J proves equation (6), for both signs of time. The output is the entire physical head/program space, including mediator leakage. Both maps are isometries, giving cap 2 and the stated unhalved channel-distance bound twice the vector operator bound on this restricted input domain. The scalar C=2sum b_i is the same even on vacuum and is retained. All-enabled programs remove E only when that further invariant program restriction is imposed.

For the optional endpoint graph extension, sum c_xy|psi_x-psi_y|^2<=2d_max||psi||^2 proves the stated one-head norm. The source correctly conditions its use on actual physical/logical copies and exact literal intertwining; it does not infer arbitrary graph geometry from this norm estimate.

## Sufficient family and loads

For identical cells, c=za and T=pi/a, the residual bound becomes 2kappa_1(1+2pi z)+pi epsilon/a. Substitution of kappa_1<=r and epsilon<2b^2/D1 gives (7), with the necessary weak comparison between capped quantities.

For L=1+2pi z, R=16pi/eta, D1=Lambda/2, D0=D1/R and r=eta/(16L), one has a=r^2 D0 and b=rD0/sqrt(2). These satisfy the exact tuning and D1>D0>2b for all Lambda>0, 0<eta<=1 and z>=0. The mediator load is D1+sqrt(2)rD0<Lambda. Endpoint load divided by D0 is 3r/sqrt(2)+(1+2z)r^2. Its terms are bounded by 3/(16sqrt(2)), 1/256 and 1/(256pi), since 2z<L/pi and L>=1. Their sum is below 1. Program loads a and D1-2b also lie below Lambda. This verifies all local caps including external bonds, uniformly in N.

The two error contributions are at most 2rL=eta/8 and strictly less than pi/R=eta/16. Strictness of the resulting uncapped total is valid; no saturated cap is compared strictly. It follows that the error is below 3eta/16 throughout the stated horizon. Direct substitution yields a=Lambda eta^3/(8192pi L^2) and T=8192pi^2 L^2/(Lambda eta^3). Unlike the earlier full-domain family, no N enters these coefficients. The physical counts remain 6N qubits and 7N+(N-1)=8N-1 blocks, on the previously checked disjoint nearest-neighbor coordinates. Size-independent error does not imply size-independent resources or traversal time.

## Path boundary calculation

With every cell enabled and c=a/2, both internal and external logical edges have weight a/2. There are exactly 2N ordered endpoint vertices and 2N-1 consecutive edges. Thus the target after subtraction of C is (a/2)L_path. Every end vertex has degree one and each interior vertex degree two. For N=1 this gives the correct two-by-two internal Q block; no extra end onsite is present.

For M=2N, put theta=pi k/M and f_ell=cos[theta(ell-1/2)]. The interior difference equals 2(1-cos theta)f_ell. At the first endpoint, f_1-f_2=2(1-cos theta)f_1. The right endpoint is equivalent to the ghost relation f_(M+1)=f_M, which holds because sin(M theta)=0. Therefore k=0,...,M-1 gives all M eigenvalues 2(1-cos theta) of L_path. Multiplication by a/2 yields exactly a[1-cos(pi k/(2N))]. The constant mode normalizes by 1/sqrt(M), and the nonconstant modes by sqrt(2/M); their orthogonality supplies a complete basis. These are degree-one, not constant-diagonal-two, boundaries.

Disabling an internal logical edge removes that Q bond and its associated diagonal contributions. It therefore gives the claimed broken-path Laplacian, with external edges intact. Coherent programs give a controlled direct sum with the same C. The nonzero physical disabled residual remains in equation (6). A Laplacian spectrum alone supplies no endpoint arrival fidelity, directionality or read time.

## Disposition and limits

All changed claims are supported within their stated sector and supplied-model premises. Multiple-head inputs, erroneous joint preparation, arbitrary processor encodings, native programs/interactions, absent-coupling protection, compiler claims and transport performance remain outside this result. The theorem compares actual full evolution with the specified noncommuting target; it does not factor a network into isolated gates or establish permanent finite halt.

Only this review was written. No scientific program, symbolic solver, numerical evolution, sweep, source/canonical/W/Git/checkpoint/prompt/model edit or delegation occurred. Hashing was deterministic identity bookkeeping. This selective check assigns neither retained audit status nor publication status.
