# Integrable outer-boundary error for the exact supplied-packet router

New bounded author derivation requiring a distinct check. ROOT suggested twice integrating the incoming/outgoing packet integrals by parts and then integrating the resulting outer-contact amplitudes in Duhamel. ROOT subsequently identified that deleting full Laplacian edges changes diagonals and does not match an equal-diagonal weak emitter, and suggested the fixed-diagonal variant proved below. These are design exposure, not independent verification. Both perturbations are controlled during an explicitly separated time window, but they describe different Hamiltonians. The result does not establish launch from an outer site, or a complete product-seed router.

## Exact premise and window

Use the exact ideal one-head router h, unitary transform F, dispersion E(k)=2j(1-cos k), and S(k)=exp(ik)C from `common_product_autonomous_interface/PROPOSAL.md`, SHA256 `bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5`. Here j>0, C=P0 tensor X+P1 tensor I is a constant unitary involution on the legal program/path space and acts trivially on a passive reference. Its recorded distinct check, read previously in full, is `common_product_autonomous_interface_check/REVIEW.md`, SHA256 `90c7926ed7c681286108afe5a9063a9f63f2be690026ff0abc56844214ab67b2`. I authored that prior check; it is a premise qualification, not independent evidence for this new lemma. No microscopic cell estimate is added in the present result.

Let L be an integer, g in C_c^2((0,pi)) with ||g||_2=1, and xi any unit vector in the legal program/path/passive-reference space. Choose a compact interval [k_-,k_+] containing the support, inside (0,pi), and set

    vmin = min_[k_-,k_+] E'(k)>0,
    vmax = max_[k_-,k_+] E'(k)>0,
    G_r = ||g^(r)||_L1(0,pi), r=0,1,2.

Suppose 0<t0<=tf, t0 vmin>2, and tf vmax<2L-2. These conditions imply L>=2. Put f_L(k)=exp(ikL)g(k)xi. The exact normalized ideal state is

    psi(t)=exp(-ith)F f_L=I_t f_L+O_t S f_L.

At each n its full program/path/reference amplitude is

    psi_n(t)=(2pi)^(-1/2) integral g(k) {
       exp(i[(L-n)k-tE(k)]) xi
       +exp(i[(n+L+1)k-tE(k)]) Cxi } dk.       (1)

The extra +1 in the outgoing phase comes from S, and is essential. For every n>=L-1, including n=L-1,L,L+1,L+2, define uniform lower derivative bounds

    q_i(t)=t vmin-1>1,
    q_o(t)=2L-t vmax>2.

Indeed the incoming phase derivative (L-n)-tE' is negative and has magnitude at least q_i. The outgoing derivative n+L+1-tE' is positive and at least q_o. Neither claim uses a stationary-phase approximation. The time labels here refer to this exact ideal state and do not themselves identify a physical preparation procedure.

## Two integrations by parts

For any scalar C2 amplitude a vanishing together with its first derivative near the integration endpoints, and C3 real phase phi with lambda=phi' nonzero, two integrations by parts bound the integral by the L1 norm of

    ( ((a/lambda)')/lambda )'
      = a''/lambda^2 -3a' lambda'/lambda^3
        -a lambda''/lambda^3 +3a(lambda')^2/lambda^4.   (2)

The overall factors of i have modulus one. In the present application a=g, lambda'=-tE'' and lambda''=-tE'''. The exact derivatives are E''=2j cos k and E'''=-2j sin k, so both have absolute value at most 2j. Thus a uniform explicit bound is

    H(t,q)=G2/q^2 + 6jt G1/q^3
                    +2jt G0/q^3 +12j^2 t^2 G0/q^4.   (3)

All derivatives in (2) are included; in particular the E''' term and the squared E'' term are not discarded. C_c^2 regularity gives zero endpoint terms at both integrations. Applying (3) to each term of (1), using ||xi||=||Cxi||=1, yields simultaneously at every n>=L-1

    ||psi_n(t)|| <= M(t)
       :=[H(t,q_i(t))+H(t,q_o(t))]/sqrt(2pi).          (4)

The norm on the left is over all ports, legal programs and references at that radial index. No sum over reference dimension, program sectors, or ports appears. Interference between the two terms is bounded by a triangle inequality, without claiming that either summand is normalized.

## Explicit integrable envelopes

Write qi0=t0 vmin-1, qif=tf vmin-1, qo0=2L-t0 vmax and qof=2L-tf vmax. Since q_i>1, t/q_i=(1+1/q_i)/vmin<=2/vmin. Consequently

    A_i=G2 +(12j/vmin)G1
              +(4j/vmin)G0 +(48j^2/vmin^2)G0,
    H(t,q_i(t)) <= A_i/q_i(t)^2.                     (5)

In particular q_i>=t vmin/2 implies the explicit O(t^-2) envelope 4A_i/(t^2 vmin^2). For the outgoing term, t<=tf and q_o>=qof>2 give

    A_o=G2 +(6jtf/qof)G1
              +(2jtf/qof)G0 +(12j^2 tf^2/qof^2)G0,
    H(t,q_o(t)) <= A_o/q_o(t)^2.                     (6)

This is an O((2L-t vmax)^-2) envelope with its window-dependent constant fully displayed. It is not a uniform statement as the window approaches return; the factors tf/qof must be paid.

Direct integration therefore gives

    integral_t0^tf M(t) dt <= B_window,

    B_window=(2pi)^(-1/2) {
      (A_i/vmin)(1/qi0-1/qif)
      +(A_o/vmax)(1/qof-1/qo0) }.                    (7)

Both differences are nonnegative, and both vanish when tf=t0. The formula uses only finite positive denominators under the stated window assumptions. One may instead integrate the smaller exact envelope (3); (7) is a sufficient closed bound, not an optimization. The outgoing time dependence does not automatically become negligible merely because L is large if tf grows too close to 2L/vmax.

## Weakened outer edge, deleted cut edge and exact norms

For each port let B_(a,b)=(|a>-|b>)(<a|-<b|) be the radial edge Laplacian, with norm 2. Let 0<gamma<j, set w=j-gamma, and choose a boundary index M>=L. Replace the edge (M-1,M) of weight j by weight gamma and delete the entire edge (M,M+1), including its diagonals. Leave all other ideal edges unchanged, including the programmed routing edge at n=0. The operator on the infinite comparison space is

    h_tilde=h+Delta,
    Delta= -w sum_ports B_(M-1,M) -j sum_ports B_(M,M+1).  (8)

Identity on legal programs and reference is understood. This is the direct sum of the actual finite router through n=M and the decoupled exterior leads starting at n=M+1. The latter retain their edges to n=M+2 and beyond. It is not the extension by a zero exterior Hamiltonian; the direct-sum extension is chosen so that the difference is exactly the two stated edges. All retained edge weights are positive, and h_tilde is bounded positive with norm at most 4j by the weighted degree bound. Each full qubit edge block Q_gamma or Q_j is positive on its entire support; the present norm calculation is on the total-one-head restriction.

The initial illustrative edge choice is M=L. For a source whose local lead coordinate x=0 is adjacent to an emitter at router coordinate M, the reversal is x=M-1-n. Its translated incoming spectral factor is exp(ik(M-1)), so the present phase index is L=M-1, equivalently M=L+1. The contact/cut positions are then (L,L+1) and (L+1,L+2). Equation (4) includes all three required sites. This coordinate conversion was supplied by ROOT; no source-launch result is imported or proved here. The phase index L and emitter coordinate M must not be silently identified. Moreover, this geometric conversion alone does not identify the full Laplacian variant (8) with an equal-diagonal weak emitter: their onsite terms differ. The fixed-diagonal variant below is the applicable Hamiltonian for that specified source block.

On the three radial coordinates (M-1,M,M+1), -Delta has matrix

    [[w,-w,0],[-w,w+j,-j],[0,-j,j]].

Its eigenvalues are 0 and w+j +/- sqrt(w^2-wj+j^2), as follows from its characteristic polynomial lambda[lambda^2-2(w+j)lambda+3wj]. Hence

    ||Delta||=d_edge:=w+j+sqrt(w^2-wj+j^2)<=3j.       (9)

The two ports form orthogonal copies, not a norm sum; program and passive-reference tensor factors preserve this value. If P_3 projects onto these three radial sites in both ports, Delta=Delta P_3. Therefore (4) implies

    ||Delta psi(t)|| <= d_edge ||P_3 psi(t)||
                     <=sqrt(3) d_edge M(t).           (10)

This retains the actual combined perturbation norm. A separate edgewise triangle estimate is valid but unnecessary. No smallness assumption on j-gamma was used, so the bound includes arbitrarily weak positive gamma.

## Integrated Duhamel comparison and limitation

For s=tf-t0, bounded-operator Duhamel in physical order gives

    exp(-is h_tilde)psi(t0)-psi(tf)
       = -i integral_t0^tf exp[-i(tf-t)h_tilde]
                                    Delta psi(t) dt.

All vectors psi(t) on the right follow the EXACT ideal evolution; no estimate of the perturbed contact amplitudes is assumed. Equations (7),(10) give the complete normalized-state comparison

    ||exp(-is h_tilde)psi(t0)-psi(tf)||
       <=min{2, sqrt(3) d_edge B_window}.             (11)

The proof and its constants are uniform over xi, including coherent legal programs, port superpositions and arbitrary passive reference entanglement. Thus (11) is an induced isometry-norm comparison for the map xi -> psi(t0), with the corresponding isometry targets at tf. A common scalar added equally to the two Hamiltonians changes neither the error nor this proof, provided its physical phase is retained in fixed-phase target vectors.

To apply the lemma to an actual finite-device state phi at t0, embed it in the finite direct summand of h_tilde and supply an independently justified initial error epsilon0=||phi-psi(t0)||. Unitarity gives

    ||exp(-is h_tilde)phi-psi(tf)||
       <=min{2, epsilon0+sqrt(3) d_edge B_window}

for normalized phi. The initial ideal packet may have exterior support; (11) does not silently truncate or prepare it. The comparison with a genuinely finite phi must pay epsilon0, including that tail and any launch mismatch. Nothing in the lemma bounds epsilon0 from a one-site seed or proves autonomous emission. It also gives no later-time capture, permanent halt, or microscopic mediated-cell replacement by itself.

## Fixed-diagonal weak-emitter variant

Set M=L+1 and w=j-gamma, with the same 0<gamma<j and exact packet/window assumptions. Define adjacency A_(a,b)=|a><b|+|b><a| and the different perturbation

    Delta_hop = w sum_ports A_(M-1,M)
                  +j sum_ports A_(M,M+1),
    h_fixed=h+Delta_hop.                              (12)

The ideal off-diagonal hopping on each edge is -j. Thus (12) changes the first hopping to -gamma and the second to zero, while leaving every onsite diagonal unchanged. Since M=L+1>=3, all three affected sites are away from the router endpoint and have original diagonal 2j in both program sectors. The decoupled finite and exterior pieces therefore both retain diagonal 2j on their respective outer endpoints. This differs from (8), which lowers the affected diagonals by w, w+j and j.

For completeness the fixed-diagonal finite Hamiltonian has the positive decomposition, with both port sums understood,

    h_fixed,finite = routing_endpoint_bond
       +sum_(n=0)^(M-2) Q_j(n,n+1)
       +Q_gamma(M-1,M)
       +(j-gamma)n_(M-1)+(2j-gamma)n_M.              (13)

Here routing_endpoint_bond is j(|L,0>-|R,0>)(<L,0|-<R,0|) in the enabled program and zero in the disabled program; the head-occupation symbol n_a in (13) means the one-head onsite projector at site a. The Q blocks are full positive qubit blocks before restricting to one head. All coefficients in (13) are positive. At M-1, the inward Q_j contributes diagonal j, Q_gamma contributes gamma, and the onsite term adds j-gamma, totaling 2j. At M, Q_gamma contributes gamma and the onsite term adds 2j-gamma, again totaling 2j. Their off-diagonal entry is exactly -gamma. Thus the endpoint block is the specified equal-diagonal weak-source block, rather than the lower-diagonal block obtained by simply weakening a Laplacian edge.

The decoupled exterior on each port is

    h_fixed,ext = sum_(n=M+1)^infinity Q_j(n,n+1)
                     +j n_(M+1).                    (14)

Its first Q_j contributes diagonal j at M+1 and the extra onsite j restores the required 2j. Subsequent exterior diagonals are already 2j. There is no hopping from M to M+1. Equations (13),(14) therefore establish the exact direct-sum identity with (12), including every changed boundary diagonal. Positivity follows from the displayed blocks, on the finite device and on the bounded one-head exterior.

Boundedness can also be checked directly: every diagonal equals that of h, at most 2j, while the absolute off-diagonal row sum is at most 2j, and is reduced at the two modified edges. The symmetric matrix has absolute row and column sums at most 4j, hence operator norm at most 4j by the Schur bound. This argument is valid for the infinite one-head operator and uniformly for finite cuts. It makes no claim that the unrestricted infinite many-head sum is bounded.

On (M-1,M,M+1) the perturbation itself has matrix

    [[0,w,0],[w,0,j],[0,j,0]].

Its characteristic polynomial is lambda[lambda^2-(w^2+j^2)], so its exact norm is

    d_hop=||Delta_hop||=sqrt(w^2+j^2)<=sqrt(2)j.      (15)

Again the port copies are orthogonal direct summands and passive references do not enlarge this norm. This perturbation is not positive, but the resulting h_fixed is positive by (13),(14); positivity of a perturbation is not required by Duhamel. With P_3 on these same three radial sites, Delta_hop=Delta_hop P_3. Equations (4),(7) give

    ||Delta_hop psi(t)||<=sqrt(3)d_hop M(t),
    ||exp[-i(tf-t0)h_fixed]psi(t0)-psi(tf)||
          <=min{2,sqrt(3)d_hop B_window}.             (16)

For a normalized state phi in the actual finite direct summand and independently certified epsilon0=||phi-psi(t0)||, the right side becomes min{2,epsilon0+sqrt(3)d_hop B_window}. The derivation is the same ordered Duhamel identity as (11), with Delta_hop in place of Delta; it is uniform in coherent program/path/reference inputs and includes all exterior coordinates in the comparison. It does not certify epsilon0 or establish source emission.

The old Laplacian-deletion formula (11) remains a valid result for its own explicitly different Hamiltonian. It cannot be used as the equal-diagonal emitter comparison merely by relabeling coordinates. Formula (16), with (13),(14), is the new appropriate variant for the specified fixed-diagonal contact. The local source block match is exact; no external source-launch theorem, packet coefficient formula or broader product-seed composition is asserted here.

## Provenance and check obligations

The target source and its recorded check were fully read for the preceding distinct router check and are reused at the exact identities above. The preceding proposal is preserved unchanged as `PROPOSAL_v1.md`, SHA256 `e4649afe46ad1e704cba35a4bfc24013522cebc3de2278b01396085c37e3e396`. ROOT identified the diagonal mismatch and suggested (12); I reconstructed the diagonal bookkeeping, positive decomposition, norm and residual comparison as new author work. The original tail proof and Laplacian-variant formulas are unchanged. This is a new authored argument, not another independent review. Its decisive new obligations are the twice-IBP coefficient 3 terms, all dispersion derivatives, the uniform three-site phase margins, integrated constants, both combined perturbation norms, the fixed-diagonal positive decomposition, and the Duhamel direction with an exact ideal comparator. A distinct checker should reconstruct those steps and verify that no launch theorem or zero-exterior extension is inferred.

Only this proposal and its preserved first version were written. No scientific program, symbolic solver, simulation, parameter sweep, upstream source edit, Git/canonical/PR/checkpoint/editable-prompt/model change or delegation occurred. Source hashing and preservation copying are identity bookkeeping. No audit or retained status is assigned.
