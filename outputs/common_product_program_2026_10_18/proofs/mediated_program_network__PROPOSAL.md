# A supplied chain of common-product program cells

ROOT author derivation, pending distinct check. This constructs a finite chain of DISJOINT six-qubit cells joined only at their endpoint qubits. It does not replace a processor, identify native dynamics, implement a universal compiler, or assert permanent halt. No scientific program was run.

## Exact premises and geometry

Use the complete cell source739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 and distinct check809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6, both fully read. All of their positivity, coefficient correlation, occupation-frame, selected-coupling and supplied program premises remain. The single-cell attachment source55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a is provisional context; the tensor residual proof below is supplied explicitly and does not rely on a completed review of it.

For N>=1, cell i has heads u_i=(3i-1,0,0),m_i=(3i,0,0),v_i=(3i+1,0,0) and their three program bits one unit above them. Distinct cells share no qubit. Install the cell Hamiltonian H_i of739 with b_i>0,D1_i>D0_i>2b_i,a_i=2b_i²/D0_i. Install additional positive nearest-neighbor bonds K_i=Q_(c_i)(v_i,u_(i+1)), c_i>=0, for i=1,...,N-1. Every missing coupling, including adjacent program-row pairs, is a supplied absence. Each program triple is restricted to000 or111; there is no preparation of those contents here.

The physical Hamiltonian is H_net=sum H_i+sum K_i. It has6N qubits and8N-1 listed positive blocks in the combined mediator-block convention. Every program occupation is conserved, as is total head number. The logical space includes arbitrary endpoint states and all legal program choices, with arbitrary entanglement between cells and passive references. The actual injection J=tensor J_i places every mediator in its vacuum; it is the SAME literal head injection for both programs of each cell.

Let A_i=2b_i I+P0_i a_i Rminus_i and Klog_i=Q_(c_i)(R_i,L_(i+1)), where Rminus is the FULL four-state projector of739, with double-occupation eigenvalue1. Define A_net=sum A_i+sum Klog_i. Its scalar2sum b_i is retained on the entire space. The comparison is exp(-it H_net)J versus J exp(-it A_net), not a product of simultaneous independent gates. Generally the adjacent logical terms do not commute.

## Exact tensor isometry and its norm

For each cell use its auxiliary exact controlled dressed isometry Jd_i. Put epsilon_i=(sqrt(D1_i²+8b_i²)-D1_i)/2, r0_i=sqrt(2)b_i/D0_i, r1_i=sqrt(2)b_i/(D1_i+epsilon_i), alpha_(p,i)=(1+r_(p,i)²)^(-1/2). Then r1_i<r0_i, so alpha_(0,i)<alpha_(1,i). The full exact intertwiner is H_i Jd_i=Jd_i(A_i-epsilon_i P1_i Rplus_i).

The overlap J_i*Jd_i is positive diagonal in the logical vacuum/symmetric/antisymmetric/double basis within each program: eigenvalues1,alpha_(p,i),1,alpha_(p,i). Consequently for Jd=tensor Jd_i,

 kappa_all=||Jd-J||=sqrt(2-2 product_i alpha_(0,i)).       (1)

Indeed (Jd-J)*(Jd-J)=2I-Jd*J-J*Jd, and the smallest eigenvalue of the positive tensor overlap is that product. Entangled inputs do not change this operator-norm identity. Since1-product alpha<=sum(1-alpha) and2(1-alpha_(0,i))<=r0_i²,

 kappa_all<=sqrt(sum_i r0_i²).                           (2)

For a two-cell edge e={i,i+1}, define kappa_e=sqrt(2-2 alpha_(0,i) alpha_(0,i+1))<=sqrt(r0_i²+r0_(i+1)²). These are code distances, not hopping coefficients or observed leakage probabilities.

## Local attachment residual and full evolution

Each endpoint bond exactly preserves the local literal injection: K_e J_e=J_e Klog_e on the full two-cell endpoint/program domain. Its norm and logical norm are2c_e. On that local domain,

 K_e Jd_e-Jd_e Klog_e
 =K_e(Jd_e-J_e)-(Jd_e-J_e)Klog_e,

so its norm is at most4c_e kappa_e. Tensoring the remaining dressed isometries leaves this norm unchanged. This localization avoids charging the whole interaction norm against the whole-chain code distance.

Therefore the full rectangular residual satisfies

 ||H_net Jd-Jd A_net||
 <=sum_i epsilon_i+4sum_e c_e kappa_e.                   (3)

The first term follows from the exact cell intertwiners and the norm-one FULL projectors P1_i Rplus_i. No one-head reduction, dropping of scalar terms, commutation of adjacent bonds or preservation of the dressed code by attachments is assumed. The latter code generally is not invariant under H_net.

Finite-dimensional rectangular Duhamel gives

 ||exp(-it H_net)J-J exp(-it A_net)||
 <=min(2,2 kappa_all+|t|[sum_i epsilon_i+4sum_e c_e kappa_e]). (4)

Both endpoint replacements Jd to J cost kappa_all. All unitaries are norm one, and both maps in the comparison are isometries; this explains the cap2. Equations(1)-(4) hold for all real t as bounds, though they are useful only on an explicitly chosen finite horizon. They retain every mediator and program output and all logical double-occupation phases. Passive references preserve the bound; the corresponding unhalved trace/channel diamond bound is at most twice(4). Correct individual input marginals alone are not a joint preparation certificate.

## Uniform coefficients and one sufficient bounded-load family

For identical cell coefficients and c_e=z a with any fixed supplied z>=0, let r=sqrt(2)b/D0 and epsilon be the disabled residual. The actual largest incident norm sums are D1+2b on mediators and at most3b+a+2za on endpoints; each endpoint has at most one external bond. Program-bit loads are those of739. The total block norm sum is at most N(D1+4b+2a)+2(N-1)za. These are physical loads, not logical effective strengths.

At the reference time T=pi/a, equation(4), kappa_all<=sqrt(N)r, kappa_e<=sqrt(2)r and epsilon<2b²/D1 imply the uncapped sufficient envelope

 2sqrt(N)r+4sqrt(2) pi z(N-1)r+N pi D0/D1.              (5)

This does NOT assert that the attached logical network performs separate endpoint swaps at T: its prescribed target is the noncommuting evolution of A_net. T merely gives a useful scale relative to each enabled coefficient.

For any incident-load cap Lambda>0 and desired0<eta<=1, define

 L=1+2sqrt(2) pi z,
 R=16pi N/eta,
 D1=Lambda/2, D0=D1/R,
 r=eta/(16 N L), b=rD0/sqrt(2), a=r²D0,
 c_e=z a.                                               (6)

The exact tuning aD0=2b² holds. Since r<=1/16 and R>1, D1>D0>2b. The mediator load is D1+sqrt(2)rD0<Lambda. Endpoint load divided by D0 is3r/sqrt(2)+(1+2z)r². With L>=1 and2z<=L/(sqrt(2)pi), the last two terms are at most1/256+1/(256sqrt(2)pi), while3r/sqrt(2)<=3/(16sqrt(2)); their sum is below1. Thus endpoint loads are belowD0<Lambda. All program-bit loads are also belowLambda. This proves the actual combined-block incident cap including the intercell bonds; no uncharged large detuning is used.

The first two terms of(5) are at most2N L r=eta/8. Its third term is N pi/R=eta/16. Thus the complete norm bound is strictly below3eta/16<eta throughout|t|<=T, with the strictness coming from epsilon<2b²/D1. The sufficient horizon is

 T=pi/a=8192pi² N³ L²/(Lambda eta³).                    (7)

This is an explicit symbolic sufficient family, not an optimum, lower bound, numerical point, benchmark or parameter sweep. It changes supplied coefficients withN,eta,z. In particular endpoint compensation a and external c scale down; exact tuning and coefficient precision remain assumptions. N=1 removes every external bond and the formulas remain valid though deliberately loose.

## Meaning and limits

This is a finite, explicitly geometrical positive chain with a common product mediator preparation and a complete comparison to its specified programmed logical Hamiltonian. It addresses a restricted assembly interface: cells are disjoint and external bonds touch only literal endpoints. A bond to a mediator generally violates the literal injection contract; overlapping cells or shared mediator codes are outside this proof. The logical many-body target may be difficult and is not identified with the old processor or a desired algorithm by this theorem.

The result neither creates Records nor derives native site roles, occupation frames, interactions, omissions or coefficient suppliers. It does not prepare the endpoint/program state, provide a measurement or decoder, establish permanent finite halt, capture, reset or reuse, or transfer the existing emitted-packet apparatus theorem. A finite-time all-output comparison is the claimed conclusion. Any compiler or original-system embedding requires separate explicit proof.

ROOT authored this tensor/local-residual derivation after suggesting the single-cell route to another author. The parent common-product source and distinct check were fully read; the attachment proposal is provisional contextual exposure. No independent check of this network theorem has yet occurred. No scientific computation, symbolic solver, dynamics, sweep, canonical/W/Git/PR/axiom/editable-prompt change was made by this derivation. Only this proposal was written.
