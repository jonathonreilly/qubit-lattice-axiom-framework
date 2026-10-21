# Finite positive controlled router from endpoint seeds

New authored composition requiring a distinct check. Conditional on the exact supplied positive microscopic cell and equal-diagonal endpoint blocks, a finite, static, one-head device implements a controlled port swap from two endpoint seed positions, with an explicit normalized complete-output bound. Every other head starts vacant. The final comparator has both emitters and the mediator vacant, a common normalized finite radial packet, unchanged legal program contents, and the controlled path operation C=P0 tensor X+P1 tensor I. Arbitrary encoded path/program input and passive-reference entanglement are included.

The standalone launcher, supplied-packet router and corrected fixed-diagonal outer-boundary lemma have recorded distinct checks at the pinned revisions below. The boundary check arrived during this derivation and was fully read and hash-verified before completion. This composition is not independently verified merely because its components were checked. ROOT proposed the proof structure and identified the crucial difference between deleting Laplacian edges and preserving the emitter diagonals. The derivation below checks the interfaces and charges their errors explicitly. It does not inherit an old apparatus/runtime theorem.

## 1. Actual finite Hamiltonian, coordinates and target

Let M>=3 and ell=M-1. Each port r=L,R has logical head sites n=0,...,M, with emitter at n=M and ordinary output sites 0,...,ell. The n=0 sites are the microscopic cell endpoints u,v. Let j=b^2/D0, a=2j, D1>D0>2b, and choose 0<gamma<j. Use the exact six-qubit positive cell H_cell from source 739e99c4 and add, on EACH port,

    sum_(n=0)^(M-2) Q_j(n,n+1) + B_r,
    B_r=Q_gamma(M-1,M)+(j-gamma)n_(M-1)+(2j-gamma)n_M. (1)

The physical generator is H_phys=H_cell+K, where K is precisely the two port sums in (1). All these are positive blocks on full qubit supports, and they conserve head number and legal program sectors. A straight cubic extension of the two source-cell endpoints realizes all added nearest-neighbor supports. All absent extra interactions and coefficient correlations are supplied.

The ideal finite generator h_F has the same port sums, with central enabled Q_j(u,v) or disabled zero replacing H_cell after removing the COMMON scalar 2b. Thus its n=0 diagonals are 2j enabled and j disabled. Every site n>=1 has diagonal 2j, including both emitter-adjacent sites and emitters. The outer hopping is -gamma and all other radial hoppings are -j. Both ||h_F||<=4j and ||K||<=4j on the one-head domain, by absolute row/column sums; for K alone the endpoint diagonal is j. Positivity follows independently from (1) and the ideal central bond.

Let E_seed embed a unit input xi in program/path/reference space by placing its one head at emitter M in the selected path, preparing all other heads vacant, and encoding legal program p as |ppp>. For a basis program/path input this is a product occupation seed; arbitrary input coherence is supplied as logical input, not manufactured by the device or mislabeled a sitewise product. There is exactly one head. Passive references do not interact.

The desired final map will be

    xi -> e^{-i2b t_f} J_out(beta_F tensor C xi),
    C=P0 tensor X+P1 tensor I,                    (2)

where beta_F is a specified common normalized packet on n=0,...,ell. J_out encodes the program, sets both n=M emitters and the mediator vacant, and embeds the head packet and path. Every physical output qubit remains in this vector comparison. No source or mediator is traced away.

## 2. Launch spectrum, cutoff and useful tail notation

Adopt the checked standalone launch amplitudes, using a_src to avoid confusing the cell parameter a:

    E(k)=2j(1-cos k), a_src=2j-gamma^2/j, d_src=gamma^2/j,
    D(k)=a_src^2 cos^2 k+d_src^2 sin^2 k,
    w(k)=2gamma^2 sin^2 k/[pi D(k)],
    u(k)=e^{ik}[d_src sin k-i a_src cos k]/sqrt(D(k)),
    g_+=u sqrt(w), g_-=conjugate(u)sqrt(w).

These satisfy ||g_+||_2=||g_-||_2=1. Choose 0<sigma<sigma'<pi/3 and chi in C_c^2((0,pi)), with 0<=chi<=1, equal to one on |k-pi/2|<=sigma and supported in |k-pi/2|<sigma'. Put

    P=min{1,4gamma^2/[pi a_src^2 tan sigma]},
    p_chi=||chi g_+||_2^2>0,
    g=chi g_+/sqrt(p_chi), G_r=||g^(r)||_1, r=0,1,2,
    vmin=2j cos sigma', vmax=2j.

The conservative velocities bound E' on the entire support. In particular vmax<2vmin. Every derivative norm is evaluated for the displayed fixed gamma/j and cutoff; no uniform bound as gamma->0 is presumed. The spectral phase of g is fixed by u and positive sqrt(p_chi).

For t>=0 and A>0 define

    T(t,A)=[G_1+(2jt/A)G_0]/sqrt(2pi)
                         *sqrt(A^-2+A^-1).          (3)

Whenever a half-line of Fourier amplitudes has phase-derivative magnitude at least m+A, m=0,1,..., and second derivative at most 2jt, one integration by parts proves its ell^2 norm <=T(t,A). Indeed the m-th integral is bounded by [G_1+2jt G_0/A]/[sqrt(2pi)(m+A)]. Squaring and summing gives (3). All integrals have zero endpoint terms. The bound works for an internal unit vector or its image under C, without dimension factors.

At early time t0>0 the checked launcher estimate uses

    R0=min{1,2j/(pi gamma^2 t0)},
    B_minus=||(chi g_-)'||_1+(2j/vmin)||chi g_-||_1,
    L0=B_minus/sqrt(2pi)*sqrt[(t0vmin)^-2+(t0vmin)^-1],
    delta_launch=sqrt[R0^2+(L0+2sqrt(P))^2].        (4)

Assume delta_launch<1. Its normalized outgoing packet is the positive normalization of O_t0(chi g_+), with the source vacant. Each standalone emitter seed differs from that target by at most 2delta_launch. The same induced norm holds for the two identical launchers and arbitrary program/path/reference input.

## 3. Early finite-device comparison, with the exact source distance

For the early argument embed the finite device in two integer-coordinate port lines n in Z. The standalone launcher on each port has emitter n=M and lead coordinate x=ell-n>=0, hence lead sites n<=ell. It has diagonal 2j, weak hopping -gamma at (ell,M), and uniform hopping -j on the rest of n<=ell. Add to both compared operators a decoupled exterior Dirichlet half-line n>=M+1 (diagonal 2j), merely to use a common space.

Extend h_F to the same space with an additional decoupled Dirichlet half-line n<=-1 on each port. The finite part remains 0<=n<=M. The two extensions differ only at the n=0 region: removing its connection to n=-1, installing the enabled central port bond or disabled boundary diagonal, and retaining the independent negative exterior. Both operators have norm <=4j. Starting from an emitter at M, at least M multiplications are needed to reach n=0. The next multiplication is the first that can detect a changed diagonal or edge. Thus their powers on the seed agree for 0<=m<M+1 in each program sector, and

    e_early=min{2,2 sum_(m=M+1)^infinity (4jt0)^m/m!} (5)

bounds the difference of the normalized evolved seed states. The bound also holds in induced norm over xi. It includes the possibility of negative-coordinate reference-launcher amplitude, which the actual finite state never has. The common infinite exterior is only a proof embedding. No source is duplicated in the physical device.

Define the full-integer incoming Fourier state

    A_n(t)=(2pi)^(-1/2) integral e^{i[(ell-n)k-tE(k)]}g(k)dk.

By Parseval on all integer n, ||A(t)||=1. Reversing x=ell-n converts the normalized standalone outgoing packet exactly into the normalized projection P_(n<=ell)A(t0). The positive sqrt(p_chi) cancels under normalization. The emitter coordinate n=M=ell+1 is outside that projection and is vacant in the reference target. No extra scalar or path-dependent phase is introduced; the translation phase is e^{ik ell}, not e^{ikM}.

For n=ell+1+m, the phase derivative is -(1+m)-t0E'. Equation (3) gives

    ||P_(n>ell)A(t0)|| <= T(t0,1+t0vmin)=:d_right.

Replacing the normalized projection by A(t0) costs at most 2d_right. This follows from the elementary normalized-projection inequality, and remains a valid upper bound even when loose.

Now use the exact normalized ideal-router state on n>=0,

    Psi(t)=F[e^{ik ell}g(k)xi] evolved to time t
          =I_t(e^{ik ell}g)xi+O_t(e^{ik(ell+1)}g)Cxi. (6)

Embed it by zero on n<0. Assume A_early=ell+1-t0vmax>0. On n<0 the difference A(t0)xi-Psi(t0) is the negative-coordinate tail of A; its phase derivative is at least A_early+m. On n>=0 the difference is minus the outgoing term of (6), with the same derivative lower bound. These occupy disjoint coordinate ranges and each has norm <=T(t0,A_early). Consequently

    ||A(t0)xi-Psi(t0)|| <=sqrt(2)T(t0,A_early).

Combining (4)--(6), the actual finite IDEAL state phi0=e^{-it0 h_F}E_seed,log xi obeys

    ||phi0-Psi(t0)|| <= e0,
    e0=e_early+2delta_launch+2d_right
                              +sqrt(2)T(t0,A_early). (7)

Although auxiliary vectors in the proof used negative n, the two vectors in (7) lie in n>=0, so this is exactly the initial error needed by the outer-boundary lemma. E_seed,log denotes the ideal one-head seed with abstract legal program; the physical encoding is applied later.

## 4. Evolving past the junction while keeping the outer boundary quiet

Assume

    t0vmin>2, t_f>=t0,
    t_f vmin>ell, t_f vmax<2ell-2.                 (8)

The first and last conditions permit the corrected outer-boundary estimate with phase index ell and emitter coordinate M=ell+1. On the infinite ideal router h, define the fixed-diagonal perturbation, on BOTH ports,

    Delta=(j-gamma)Adj(M-1,M)+j Adj(M,M+1),
    Adj(a,b)=|a><b|+|b><a|.

Then h+Delta is exactly h_F direct-summed with exterior Dirichlet half-lines n>=M+1. Its diagonals are unchanged. The exterior's first site has the extra positive j onsite term needed to keep diagonal 2j. This is the hopping-only modification, not deletion of full Laplacian blocks. On the three affected sites the perturbation matrix has off-diagonal entries j-gamma and j, so

    d_hop=||Delta||=sqrt[(j-gamma)^2+j^2].

The norm is not multiplied by the number of ports or programs. The exact fixed-diagonal source decomposition is (1).

For completeness, here is the full quantitative source envelope used. Set

    qi(t)=tvmin-1, qo(t)=2ell-tvmax,
    A_i=G_2+(12j/vmin)G_1+(4j/vmin+48j^2/vmin^2)G_0,
    A_o=G_2+(6jt_f/qo(t_f))G_1
              +(2jt_f/qo(t_f)+12j^2t_f^2/qo(t_f)^2)G_0,
    B_window=(2pi)^(-1/2){
       (A_i/vmin)[1/qi(t0)-1/qi(t_f)]
       +(A_o/vmax)[1/qo(t_f)-1/qo(t0)]},
    e_boundary=sqrt(3)d_hop B_window.              (9)

The twice-integrated amplitude bound is

    H(t,q)=G_2/q^2+6jtG_1/q^3+2jtG_0/q^3+12j^2t^2G_0/q^4.

It follows by differentiating ((g/phi')'/phi')', retaining the coefficients -3g'phi''/(phi')^3, -g phi'''/(phi')^3, and +3g(phi'')^2/(phi')^4. The exact packet (6) has derivative gaps qi,qo at all three affected sites; |E''|,|E'''|<=2j. Thus each radial vector is bounded by [H(t,qi)+H(t,qo)]/sqrt(2pi). Integrating the displayed envelopes gives B_window. Multiplying by sqrt(3)d_hop bounds ||Delta Psi(t)|| integrated over time. These are the corrected source's constants, reproduced to expose every denominator used in the composition.

Ordered Duhamel with the EXACT ideal comparator Psi(t) yields

    ||e^{-i(t_f-t0)(h+Delta)}phi0-Psi(t_f)||
                                      <= e0+e_boundary. (10)

The left evolved state remains in the finite summand and equals e^{-it_f h_F}E_seed,log xi. Neither perturbed boundary amplitudes nor negligible repeated returns are assumed; their possible effect over this window is paid by the exact residual integral. Reference atom absence is not transferred to the finite graph.

## 5. Final finite normalized packet and complete ideal error

Let A_late=t_f vmin-ell>0. The incoming term of (6) has phase derivative of magnitude at least n+A_late for n>=0. Define

    d_late=T(t_f,A_late),
    B_n=(2pi)^(-1/2) integral e^{i[(n+ell+1)k-t_fE(k)]}g(k)dk,
    q_out=||B||_(n>=0).

Assume d_late<1. Since Psi(t_f) has unit norm and differs from B tensor Cxi by at most d_late, q_out>=1-d_late>0. Its positively normalized infinite outgoing target differs from Psi(t_f) by at most 2d_late.

To leave both emitters vacant, truncate the target to ordinary sites 0<=n<=ell, not through n=M. For n=ell+1+m, the outgoing phase derivative is at least

    A_out+m, A_out=2ell+2-t_f vmax>0.

Hence its discarded unnormalized norm is <=T(t_f,A_out), and the discarded norm of B/q_out is at most

    d_out=T(t_f,A_out)/(1-d_late).                  (11)

Assume d_out<1. Define the final scalar radial packet by

    beta_F=P_(0<=n<=ell)B / ||P_(0<=n<=ell)B||.      (12)

The denominator is positive; it fixes a single common phase for both programs and paths. The normalized-projection cost is at most 2d_out. Combining (7),(10)--(12) proves the full ideal map bound

    ||e^{-it_f h_F}E_seed,log xi
                 -J_out,log(beta_F tensor Cxi)||
       <= e_ideal:=min{2,e0+e_boundary+2d_late+2d_out}. (13)

This target has both emitter coordinates exactly vacant, while the actual residuals remain charged in the norm. The common translation factor e^{ik ell}, scattering factor e^{ik}, and full dispersion e^{-it_fE} are all present in B. There is no fitted branch phase or suppressed elapsed time.

## 6. Physical cell replacement for the WHOLE elapsed time

The added finite port operator K in (1) acts on no mediator or program site and satisfies exact literal-code intertwining KJ=JK_log on the entire allowed one-head input domain, including both emitters. Its norm is <=4j. If the head is outside the cell, the cell's two compensations still contribute the same scalar 2b; there is no location-dependent removal of that scalar.

Let

    epsilon1=4b^2/[sqrt(D1^2+8b^2)+D1],
    r0=sqrt(2)b/D0, r1=sqrt(2)b/(D1+epsilon1),
    kappa=max_p sqrt[2-2/sqrt(1+r_p^2)].

The common dressed-residual attachment theorem therefore gives

    e_cell=min{2,2kappa+t_f(8j kappa+epsilon1)}.      (14)

This is applied for total time t_f starting at the literal emitter seed, not just t_f-t0 or a nominal isolated gate time. Its full-domain comparison includes all actual mediator output. The dressed injection is a proof device, never a preparation requirement.

Finally, uniformly over normalized xi and arbitrary passive references,

    ||e^{-it_f H_phys}E_seed xi
             -e^{-i2b t_f}J_out(beta_F tensor Cxi)||
        <= e_total:=min{2,e_cell+e0+e_boundary+2d_late+2d_out}. (15)

This is an induced isometry-norm bound. The unhalved channel/trace-distance bound is at most min{2,2e_total}. Positive target normalization does not renormalize the actual output, and all physical coordinates are retained. Exact legal program contents are conserved. Their coherence is part of the mathematical input contract, not a native Record claim.

## 7. Existence of simultaneous choices, including a finite local load cap

The error terms can be made arbitrarily small in a consistent order. This is a sufficient analytical existence argument, not a selected numerical point, optimized scaling or practical runtime certificate.

First fix 0<sigma<sigma'<pi/3 and a C2 cutoff. Choose rho=gamma/j>0 sufficiently small that the fixed spectral-tail contribution in 2delta_launch is small. Then all g, G_r, B_minus and p_chi depend only on rho and the cutoff, not on the overall j scale. Hold them fixed thereafter.

Choose u0=jt0 sufficiently large. This reduces R0, L0, d_right and the incoming contribution d_hop times B_window to any required small allowance. The last assertion follows directly from (9): after multiplying by d_hop<=sqrt(2)j, the incoming part is bounded by a fixed constant times 1/(u0(vmin/j)-1), independently of later t_f. No derivative norm is assumed independent of rho.

Choose a constant alpha satisfying

    1/(vmin/j)<alpha<2/(vmax/j)=1,

which is possible because vmax<2vmin. Then take the integer ell sufficiently large, set M=ell+1 and t_f=alpha ell/j. With u0 fixed, conditions (8), A_early>0 and t_f>=t0 all hold for sufficiently large ell. The factorial series (5) tends to zero because its argument 4u0 is fixed while M+1=ell+2 grows. The early gap tail tends to zero. Both late gaps A_late and A_out grow linearly in ell, while jt_f/A is bounded, so d_late and d_out tend to zero. In (9), jt_f/qo(t_f) stays bounded; the outgoing boundary allowance is O(1/ell). Thus e_ideal can be made arbitrarily small by these ordered choices.

Only after fixing these dimensionless choices, let s=jt_f=alpha ell. Choose eta=b/D0 and zeta=D0/D1 small. Since kappa<=sqrt(2)eta and epsilon1/j<2zeta,

    e_cell <= min{2,(2+8s)sqrt(2)eta+2s zeta}.       (16)

This can be made small independently of the already fixed dimensionless ideal error. Changing eta,zeta rescales j, t0 and t_f consistently, with gamma=rho j; it does not hold physical time fixed while weakening the cell.

For any supplied incident load cap Lambda>0, one explicit safe scale choice is D1=Lambda/2, D0=zeta D1, b=eta D0 with 0<eta<=1/8 and 0<zeta<1/2, subsequently made smaller as needed for (16). Then j=eta^2 zeta Lambda/2, a=2j, and D1>D0>2b. The largest possible displayed loads are

    D1+2b at mediator,
    3b+a+2j=3b+4j at cell endpoints,
    a at endpoint program sites, D1-2b at mediator program site,
    4j at ordinary lead interiors, 5j at emitter-adjacent sites,
    3j at emitters.

All are strictly below Lambda for that conservative eta,zeta domain. The 5j/3j counts use each B_r as ONE positive block; the smaller separate-summand convention is not silently substituted. Physical times become finite but can grow greatly because j becomes small.

## 8. Finite resource count and scope

There are 3 cell head qubits, 3 program qubits, and M added head qubits on each port: 6+2M total qubits. Under the source's combined mediator-projector convention the isolated cell has 7 positive blocks. Each port adds M-1 ordinary Q_j blocks and one B_r, hence 7+2M combined positive blocks in all. The outer block has norm 3j on its full qubit support; ordinary lead blocks have norm 2j. M>=3 keeps emitter-adjacent and cell-endpoint load categories distinct. M>=2 would already suffice for the raw construction/count, but the stated proof window requires the stricter chosen size.

The finite time t_f is an observation time, not an internal stopping mechanism. A closed finite device has recurrences and may later reabsorb or reflect its head. There is no permanent halt, stable classical output, capture/reset, old processor replacement, arbitrary network compiler or derived native supplier. The target is a coherent encoded path operation with one head and a common radial packet; no multi-head computation theorem is asserted. Exact positive blocks, site roles, coefficient correlations, legal program contents and initial encoded input with all other heads vacant remain supplied assumptions.

## 9. Provenance and remaining check obligations

Sources and their SHA-256 identities:

* common_product_autonomous_interface/PROPOSAL.md: bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5; distinct review common_product_autonomous_interface_check/REVIEW.md: 90c7926ed7c681286108afe5a9063a9f63f2be690026ff0abc56844214ab67b2.
* common_product_endpoint_launch/PROPOSAL.md: fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4; distinct review common_product_endpoint_launch_check/REVIEW.md: 51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1.
* common_product_outer_boundary/PROPOSAL.md: af7dfe4193865bb80f9302fcb39f62c7be9ab7693d29b1b53bea8f620f8f2c43; distinct review common_product_outer_boundary_check/REVIEW.md: 756514da092c820d3e19601565f6d60b174acc2aed26cfcad551e598f0020985. The fixed-diagonal variant is used; the earlier e4649afe Laplacian-deletion revision is NOT the equal-diagonal emitter model. The new review supports the boundary lemma at its stated scope, not this composition.
* Underlying cell and attachment, previously fully read: mediated_common_product_program/PROPOSAL.md SHA739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 and mediated_program_attachment/PROPOSAL.md SHA55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a. Their prior checks are recorded in the supplied-packet router review; no new audit of them is claimed here.

The new proof obligations for a distinct composition check are: the common-space early comparison and first unequal power; exact source reversal ell=M-1; normalization of the full-integer Fourier state and both early tails; fixed-diagonal boundary matching; final exclusion of both emitter sites; uniform coherent program/path/reference errors; whole-time cell attachment; and simultaneous dimensionless/physical scaling under the stated local load convention. No summary or favorable parent reading substitutes for those checks.

Only common_product_finite_seed_router/PROPOSAL.md was created. No scientific executable, numerical simulation, symbolic solver, sweep, canonical/W/Git/PR/checkpoint/editable-prompt/model change or delegation occurred. No retained status is assigned.
