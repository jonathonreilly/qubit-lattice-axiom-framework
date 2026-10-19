# Distinct analytical check of the supplied-packet static router

Disposition: conditional support for the complete proposal at SHA256 `bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5`. No required mathematical correction found. The result is a finite-time, full-output controlled-router comparison for a supplied common incoming packet, conditional on the specified positive cell and legal one-head domain. It does not prove product-seed launch, a compiler, permanent capture, or an old processor replacement.

## Sources and qualification

Read the complete target and both complete source proposals. Verified identities by SHA256 bookkeeping:

* `common_product_autonomous_interface/PROPOSAL.md`: `bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5`.
* `mediated_common_product_program/PROPOSAL.md`: `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.
* `mediated_program_attachment/PROPOSAL.md`: `55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a`.
* Complete prior cell check: `809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6`.
* Complete prior attachment check: `48940d210811f4599c16677edde54b6e3b1be8d6715b7a14aa29e5c4b3b440ce`.

Those prior checks qualify the source premises at their recorded scope. They are not fresh independent audits here. The new scattering transform, normalized interface, one-head infinite extension, finite cut and associated error sums were reconstructed below. ROOT supplied the boundary scattering design and had a provisionally favorable reading; neither was treated as a verdict. This checker did not author the target. Same-model lineage and supplied design exposure prevent describing this as blind or model-independent replication.

## Boundary and complete spectral transform

For a port-involution eigenvector with eigenvalue sigma, write the boundary coefficient as q=1-sigma: q=0 for the symmetric channel or disabled sector, and q=2 for the enabled antisymmetric channel. The boundary equation is E psi_0=j(1+q)psi_0-j psi_1. With psi_n=z^{-n}+s z^n, E/j=2-z-z^{-1}, substitution gives s=z when q=0 and s=-z when q=2. Recombining enabled channels yields S=zX; disabled channels yield S=zI. No reflected phase is omitted. The enabled boundary diagonal is 2j and disabled diagonal j, as required by the graph definition.

The sigma=+1 and -1 generalized waves are respectively sqrt(2/pi) exp(ik/2) cos((n+1/2)k) and -i sqrt(2/pi) exp(ik/2) sin((n+1/2)k). Integrating products on (0,pi) gives delta_nm for each real normalized family. Completeness can be seen independently by extending a function evenly (cosine) or oddly (sine) to (-pi,pi): the full half-integer Fourier family exp(i(l+1/2)k), l integer, is complete because it is the integer Fourier basis multiplied by exp(ik/2). Grouping paired positive/negative frequencies recovers precisely each parity family. Thus there is no missing endpoint eigenstate or bound-state summand.

Multiplication of the input function by exp(ik/2), and by the constant -i where needed, is unitary. The integral maps in the proposal are therefore unitary analysis transforms onto ell^2, even though the kernel is written without a complex conjugate. Resolving the finite-dimensional involution gives the full two-port unitary F_p. The recurrence at n>=1 and the verified boundary equation show h_p F_p=F_p E, initially on smooth compactly supported inputs. Boundedness extends this identity to all inputs. The spectrum has supremum 4j and no negative component. Independently, both graph Laplacians have maximum degree two and norm at most 4j; positivity is termwise. These arguments agree.

For exp(-itE), the incoming exponent -kn-tE has stationary position n=-tE'(k), while the outgoing exponent kn-tE has position n=tE'(k). Since E'=2j sin k>0, the prepared incoming component is on nonnegative n at negative time label and the outgoing component at positive label. This verifies the signs and the elapsed interval 2tau, without laboratory backward evolution.

## Tail estimate and normalized common-packet map

For I_tau and O_-tau the absolute phase derivative is n+tau E'(k)>=n+tau v_*. Integration by parts has zero boundary term because the C1 data vanish near 0 and pi. The Hilbert-valued integral obeys

    ||amplitude_n|| <= (2pi)^(-1/2) [||f'||_1/(n+A)
                       + 2j tau ||f||_1/(n+A)^2], A=tau v_*.

Since tau/(n+A)<=1/v_*, this is at most B(f)/(sqrt(2pi)(n+A)). Squaring and summing, the decreasing positive summand has sum at most A^-2+integral_0^infinity (x+A)^-2 dx=A^-2+A^-1. This proves both tail bounds with the displayed constants. The Bochner integral triangle inequality uses the reference Hilbert norm directly and introduces no dimension factor.

Let x_-=exp(+i tau h)Ff and x_+=exp(-i tau h)Ff. Both have norm one and exp(-i2tau h)x_-=x_+. Their differences from I_-tau f and O_tau Sf are, respectively, O_-tau Sf and I_tau f. If these errors are d_- and d_+ below one, the candidate norms are positive. For any y within d of unit x, ||y/||y||-x||<=|1-||y||||+||y-x||<=2d. Two such replacements and exact unitary transport give 2D_tau(Sf)+2D_tau(f). The normalization cost is neither missing nor double-counted.

For f=g xi, the incoming unnormalized map is the same scalar radial vector times xi, and the outgoing map is the scalar vector from exp(ik)g times Cxi. The involution C is unitary for coherent legal programs and paths, so their normalization factors are independent of xi and any passive reference. This turns the vector argument into a uniform induced isometry-norm statement. For general spectral/internal entanglement, the separate vector comparison remains valid but no common radial factor follows; the proposal states that restriction correctly. The derivative estimate for exp(ik)g follows from ||g'+ig||_1<=||g'||_1+||g||_1.

The common exp(ik) phase is momentum dependent and must remain in the outgoing packet. It cannot be replaced by a global scalar. The scalar physical phase exp(-i4b tau) is a separate issue and is retained correctly.

## Physical attachment, scalar and resources

On the total-one-head physical space the lead Laplacian acts on the endpoint-plus-lead subspace and annihilates the mediator basis vector. It is bounded by 4j. It acts on no program coordinate and maps a vacant mediator to a vacant mediator on the whole allowed logical input domain, so KJ=JK_log exactly. Checking compression alone would have been insufficient, but the actual supports establish the stronger column identity.

The isolated cell acts as 2b on a state whose head lies entirely in a lead: both endpoint compensation projectors contribute b, while cell occupations and hops vanish. On cell-head states the same scalar follows from the source expansion. Thus the direct-sum extension has one common scalar 2b, rather than a head-location-dependent energy shift. The extended dressed map fixes all external lead basis vectors and changes only the endpoint symmetric column to alpha_p S+beta_p M. Its image remains orthonormal and its norm distance from J remains max sqrt(2-2alpha_p). The disabled residual is -epsilon1 on the dressed symmetric endpoint mode and zero on the other logical modes; its norm is epsilon1.

The rectangular dressed residual is K(J_d-J)-(J_d-J)K_log minus the dressed disabled residual. Its norm is at most 8j kappa+epsilon1. Duhamel over duration T and replacing the initial and final injections cost T(8j kappa+epsilon1)+2kappa. This proves (5) without dressed-subspace invariance. Combining with the normalized packet isometry comparison proves (6), preserving mediator output and legal programs. Passive-reference extensions preserve each norm. The usual two-isometry channel estimate gives unhalved trace/diamond distance at most twice the vector/operator bound; a separate trivial channel cap could tighten it but is not needed for validity.

All infinite operators used here are bounded on the specified one-head space. The physical cell is a bounded finite-site perturbation plus a scalar, and the lead Laplacian is bounded there. Finite lead extensions converge strongly with uniform bounds, so the alternative finite-first construction is legitimate. No bounded unrestricted many-head Hamiltonian is inferred from the infinite sum of local terms.

At T=s/j, epsilon1<2b^2/D1 and j=b^2/D0 give T epsilon1<2s D0/D1; the stated weak capped envelope is valid even when the cap saturates. At fixed dimensionless j tau, the packet bound depends on j tau and the band interval, while kappa can be reduced through b/D0 and the residual through D0/D1. The claimed existence limit is consistent, although it supplies no fixed speed at bounded load.

Each full Q_j lead block is positive, has norm 2j and is nearest neighbor at the stated coordinates. Adding one such bond to each endpoint changes its incident sum to 3b+a+2j. Mediator/program loads retain the source values; an interior lead site has two bonds and sum 4j. A non-endpoint outer end has one bond and sum 2j. For N=0 there is no added lead bond, so the displayed endpoint load remains a conservative upper bound rather than an exact count for that degenerate cut. The maximum given is still sufficient. No physical endpoint-to-endpoint bond is silently installed: it belongs only to the effective comparator.

## Finite cut and target normalization

The operator difference h-h_N is first detectable at site N: deleting the edge (N,N+1) changes the diagonal at N, as well as its outward hop. A vector initially supported at n<=R needs at least N-R multiplications to reach N; the next multiplication can distinguish the operators. Induction therefore proves equality of powers for m<N-R+1, including R=N where only m=0 is promised. This verifies the potentially delicate diagonal contribution and the stated d, in both program sectors.

Both bounded norms are <=4j, so the remaining Taylor terms have difference at most 2 sum_{m>=d}(4jT)^m/m! on a normalized supported input. Writing m=d+l and using (d+l)!>=d! l! gives the exponential majorant. The isometry cap 2 is valid after embedding the finite space. The series converges to zero with d at fixed T; it does not claim long-time uniformity.

For a normalized packet with tail delta, its projected norm is sqrt(1-delta^2), and replacing it by the normalized projection costs at most delta+1-sqrt(1-delta^2)<=2delta. Apply this once at the input, transport unitarily, add the cut error and the infinite packet comparison, and add the same finite-lead cell residual. This yields exactly (8), with one input-tail cost, one cut cost, one wavepacket cost and one cell cost. The embedded physical outputs retain every coordinate. Replacing the infinite target by its normalized finite projection adds at most 2delta_out,N, with no postselection of the actual output. For fixed packet and T the ell^2 tails vanish; first increasing R, then N, achieves the three geometric budgets. The physical attachment estimate is uniform in N.

## Boundaries and result

Counterexample checks against an omitted reflection phase, wrong incoming sign, missing spectral bound mode, deleted-cut diagonal, location-dependent compensation scalar, and improper many-head boundedness found no failure in the stated theorem. The normalized incoming packet is supplied and generally delocalized. The mathematical program superpositions are allowed inputs, not a derived Record-preparation mechanism. Exact coefficients, legal program contents, local roles, vacant mediator, absent extra interactions and passive references remain premises. Finite recurrence precludes inferring permanent output storage from this single-time comparison.

Only this review was created. No scientific executable, symbolic solver, simulation, sweep, source edit, Git/canonical/PR/checkpoint/editable-prompt/model change or further delegation was performed. The initial broad path inventory was truncated and was not used as evidence of coverage; exact named sources were subsequently read in full. No formal audit or retained status is assigned.
