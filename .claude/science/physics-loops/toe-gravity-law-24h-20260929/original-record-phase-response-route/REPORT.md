# Complete marked phase response on the saturated two-hole block

September30,2026. Selected main fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7; selected procedure7146fe17a76de41badcaca3c3c7cac6d11eb2a00. Authored discovery for focused checking, not a formal review or an adopted microscopic limit.

The complete signed feedback has a resonant part that cannot be removed by a bounded normal superoperator coboundary on the full rotor carrier. Nevertheless its complete phase/current tangent has a uniformly bounded physical-time response on a particular source-accessible block, using the EXACT diagnostic dynamics rather than its leading fast Hamiltonian. The block's contribution to the rescaled actual-Omega signed retarded functional vanishes at a fixed sufficiently small positive physical time. This closes one named dense-sector slice; it does not bound arbitrary backgrounds, all holes, or the entire continuously forced remainder.

## 1. Contract, prior and actual law

Keep the supplied compensated hard-core q=0,+/-1 carrier, Gauss law, original normalized spin shifts, original resolved marks OR original unnormalized coherent edge marks, bare Omega, physical clock and coupled scaling epsilon²S(S+1)=delta/K. The instruments are separate; the coherent sign is never measured. All statements about the actual microscopic state use sigma=Y rho_micro Y*, with the exact finite-depth circuit from the checked positive-forcing construction. Its Hamiltonian preserves total record number; each actual original birth increases it by two. Y preserves that number. Delta and kappa are positive.

Use W=sum_A(1-n_a), N=|A|=|B|, Ntot=sum n_x and

    H2=C_S+[F,F*],  G=sum_mu j_mu*j_mu,
    A_mu=[j_mu,F],  d_mu=[F*,j_mu],
    Z_+=[G,F],  Z_-=Z_+*,  R=[Z_-,Z_+],
    T=(i/delta)[C_-,C_+].                              (1)

The exact diagnostic D_epsilon is the COMPLETE W-averaged neutral Hamiltonian and every exact transformed jump J_(mu,r) with r<=0, scaled by kappa epsilon^-2. In particular its same-grade corrections are retained. The actual state sigma is not assumed to evolve under D_epsilon.

The closest prior is the now-checked full signed-feedback report6d883a82, with receipt3f5ef972. It already supplies the exact complete dark formula, its nontrivial cross corner, and the fact that a scalar state phase cannot remove all kicks. The earlier fast-propagation report2f45858d and receiptb3bacbce already supply the full-B,W2 leading invariant sector and its first dressed escape. Neither prior gives the complete exact-D first-event response or the normalizable-packet superoperator obstruction below. The checked global moment37f01ea6/receiptf5590fcc ALREADY gives a small-time dense-sector probability mechanism; its use here is a consumer of that theorem, not a new source-tail theorem. The mean-hole theorem and its check6ba24784 are also inputs at their stated scope.

Main and relevant actual open proposal sources were refreshed before serious derivation, as recorded in PRIOR_REFRESH and SOURCE_IDENTITIES. Required current source bytes agree with the selected main. PR9412 and PR9399 supply no missing uniform phase-response theorem. No external theorem or literature import is needed. The contract and exploratory PRE preceded the complete proof/control; PRE explicitly does not claim blind discovery. During this derivation root supplied the stronger generic first-event estimate in section4. I independently checked its differential argument; this contribution and its exposure are not presented as independent discovery by this author.

## 2. An exact diagnostic first-event block

On a safe even cubic torus, define

    P2=1_(W=2, N_B=N),  K2=Ran P2,
    Pfull=1_(Ntot=2N).                                  (2)

All charge signs and all physical field configurations are allowed. Parity admits this W2 block; on L divisible by4, the earlier actual pair-tiling word supplies an accessible physical vector. Accessibility is not a probability bound. The algebra below does not assert that the microscopic state stays in K2.

On K2, F=0, j_mu=0, C_S=0 and H2=FF*. The gates in C_S do not conceal a residual field term: at a hole its bracket vanishes; at a filled A site all its B destinations are occupied, so both outgoing diagonal terms and F_a*F_a vanish. H2 preserves W,Ntot and hence K2. Inward F* can fill either of two A holes from six B neighbors. Its subsequent outward F can fill the unique B vacancy from at most six A sites. Each path has amplitude at most one. The same reversed count applies to rows. Therefore

    0<=H2|K2<=72 I.                                     (3)

Every exact J_mu=Yj_muY* increases Ntot by two. An input in K2 has Ntot=2N-2, so its output, if nonzero, has EVERY site occupied. Consequently on K2 every exact W-grade except r=-2 vanishes. The neutral H'_diag preserves K2. On Pfull, the original hopping, compensation and jumps vanish; W=0, and Y preserves Pfull. Thus the fully occupied target is inert under the exact diagnostic dynamics.

It follows that D_epsilon restricted to K2 and its target is exactly a first-original-event absorbing quantum instrument with

    H_epsilon=H'_diag|K2,
    ell_(epsilon,mu)=epsilon^-1 J_(mu,-2)|K2,
    L_(epsilon,mu)=sqrt(kappa) ell_(epsilon,mu).         (4)

All exact same-grade terms are inside H_epsilon and ell_epsilon. No magnitude bound or leading approximation to H_epsilon is used in the response theorem. A constant 2delta epsilon^-4 on K2 may be subtracted without changing it. The only event is the original mu and its original append; there is no newly observed grade label.

The leading jump is d_mu=-j_mu F* on this input. After F* there is one A hole and one B vacancy. Its total bare loss is at most two, with equality for an eligible rotor edge. Hence, as quadratic forms on K2,

    Q_d=sum_mu d_mu*d_mu=F G F*<=2FF*<=144 I.            (5)

This estimate keeps coherent paths and is not a sum of diagonal path probabilities. The Schur bound(3) was a separate bound on the complete positive operator.

There is also a VOLUME/SPIN-uniform stack Taylor remainder

    ||(ell_(epsilon,mu)-d_mu)_mu||<=c epsilon.            (6)

To see this, each transformed original local jump has a fixed circuit cone, and its second Taylor remainder has norm at most c0 epsilon² uniformly in spin and volume. Grade averaging preserves its cone, local Ntot increment+2 and grade-2. Restricted to K2, it must see BOTH holes inside that cone; otherwise local nonnegative W cannot decrease by two. Let p_mu project onto that condition. The remainder equals its product with p_mu. On any two-hole occupation word, only a bounded number b of original-mark cones can contain both holes, independent of their separation and volume. Thus sum p_mu<=bI. Squaring the stack estimate gives b c0² epsilon² after dividing by epsilon. No orthogonality of coherent sign paths is inserted. In particular ||ell_epsilon||<=12+c epsilon, uniformly. This is a sector estimate, not a global small-unitary assertion.

## 3. The COMPLETE feedback, not a compressed substitute

The checked dark identity is

 Pdark T(O)Pdark=i kappa²/(2delta) sum_mu Pdark{
      A_mu*[U_mu(O),M_mu]A_mu-d_mu*[U_mu(O),M_mu]d_mu}Pdark
              +i kappa²/(4delta)Pdark[R,O]Pdark.         (7)

M_mu is the diagonal bare-loss value pulled back along the actual original mark. It uses no inverse jump amplitude and preserves both coherent output-sign sectors. On K2, A_mu=0. The d output is fully occupied; undoing that one mark leaves exactly one A hole and one neighboring B vacancy. Therefore the required M_mu has a local extension on the target with

    0<=M_mu<=2,
    P2 R P2=-C_d,  C_d=sum_mu d_mu*M_mu d_mu.             (8)

In contrast to a general dark input, R also preserves K2: it preserves W and Ntot, and these two values force N_B=N. Thus R P2=P2 R P2. The troublesome test cross corner in the general formula really vanishes HERE. This is a consequence of the exact total-count block, not an assumption that arbitrary dark test corners vanish. For any bounded joint test, with all original appends,

 P2 T(O)P2= -i kappa²/(2delta) sum_mu d_mu*[U_mu(O),M_mu]d_mu
                  -i kappa²/(4delta)[C_d,P2 O P2].      (9)

The gains use the full target block of O. They are not discarded because the input is dark. Equation(9) gives a completely bounded global-sector estimate, including arbitrary passive references and contractive original appends,

    ||T|K2||_(1->1,complete)<=432 kappa²/delta.           (10)

Indeed ||Q_d||<=144, ||C_d||<=288; the two commutator gains cost at most4||Q_d|| and the Hamiltonian costs2||C_d|| with the prefactors in(9). This already sums all original marks over the entire torus. It is not a per-volume local bound.

In the rotor, M_mu d_mu=2d_mu exactly. The entire marked gain phase in(9) is then zero, even on a general full target test. The complete Schrödinger feedback is

    T*(rho)= i kappa²/(2delta)[Q_d,rho], rho=P2 rho P2.  (11)

It is a contact-loss Hamiltonian correction. Equation(11) will obstruct a bounded cochain; the finite-spin proof above does not silently replace its M by2.

## 4. A time-uniform common first-event estimate

Here is an elementary general lemma, independently verified after root disclosed its stronger bound. Let L be a bounded stacked map from an initial space to the direct sum of original target spaces, let M be diagonal in the original mark with self-adjoint blocks and ||M||<=m, put Q=L*L and C=L*ML. For an arbitrary self-adjoint H define

    H_lambda=H-kappa lambda C/2,
    event map sqrt(kappa) exp(-i lambda M)L.             (12)

The target is inert after this event. The loss Q is independent of lambda. Let S_lambda solve the no-event equation with generator

    -iH+i kappa lambda C/2-kappa Q/2.

Its complete terminal-plus-first-event isometry at time t is

 V_lambda^t psi = S_lambda(t)psi
       direct-sum sqrt(kappa){exp(-i lambda M)L S_lambda(s)psi :0<=s<=t}. (13)

The direct integral is a mathematical common dilation, not an added observed output. Dephasing the original event/time environment and applying the original mark appends, bins or final readouts are CP contractions. It is enough to bound(13), including a tensor identity on any reference.

Set u=S_lambda psi and z=partial_lambda u. Loss balance gives kappa integral||Lu||²<=||psi||². Since C=L*ML,

 d||z||²/ds=-kappa||Lz||²+kappa Re i<Lz,MLu>
             <=-kappa||Lz||²/2+kappa||MLu||²/2.

For ||psi||=1 put a=||z(t)||², b=kappa integral||Lz||² and c=kappa integral||MLu||². Then a+b/2<=c/2 and c<=m². Differentiating(13) gives

 ||partial_lambda V_lambda^t psi||²
     =a+kappa integral||Lz-iMLu||²
     <=a+2b+2c<=4m².                                   (14)

Consequently, uniformly in t>=0, H, dimension, volume and any reference,

 ||V_lambda^t-V_0^t||<=2m|lambda|,
 ||Phi_lambda^t-Phi_0^t||_diamond<=4m|lambda|.            (15)

For bounded finite-spin H all derivatives are ordinary bounded-operator derivatives. If H is self-adjoint unbounded, bounded L,C and its strongly continuous unitary group suffice via mild equations and their energy identity; no field-domain truncation deletes a generator. Only the bounded finite-spin case is needed for exact D here. Uniformity in t does not assume eventual absorption: the terminal branch is retained in(13).

Apply this lemma with L=ell_epsilon, the exact H_epsilon from(4), and the actual M from(8), so m=2. Define C_epsilon=sum ell* M ell. This is a genuine exact-loss comparison family. Its derivative multiplied by kappa/(2delta) equals(9) with d replaced by ell_epsilon. Using(6), the difference from the COMPLETE T in(9) has complete norm at most C epsilon. Thus for the diagnostic D, any finite physical t,

 ||integral_0^t Phi_D^(t-s) (epsilon² T*) Phi_D^s ds||_diamond
         <=4 kappa epsilon²/delta+C epsilon³ t.         (16)

The output version of this formula includes terminal states and all original event records. It is the derivative of the common instrument, or the ordinary extended-register Duhamel formula; its trace-norm bound is independent of a register cap. The first term follows by differentiating(15) at zero and setting lambda=epsilon² kappa/(2delta). The second term is the separately integrated d-versus-ell error. Equation(16) does not equate the finite kicked generator at this lambda with D+epsilon²T. Its derivative is what is controlled. Higher powers of lambda are not assigned to the actual microscopic law.

This pays the complete tangent by a single total event activity, not by an inverse fast gap at each visit. It controls arbitrary initial quantum states and references INSIDE K2, including any supplied positive injection integrated against its mass. It does not claim that actual continuous microscopic forcing is such an injection, or that sigma follows D. The unrestricted source/cross-sector problem remains separate.

## 5. A genuine actual-Omega retarded slice

The old global theorem gives, for each theta>0 and actual original count Rmarks,

    E exp(2theta Rmarks(s))<=exp[Ctheta N(s+epsilon²)].  (17)

Since Y preserves Ntot=N+2Rmarks, K2 requires Rmarks=(N-2)/2 even after dressing. For T<=theta/(4Ctheta) and epsilon²<=theta/(4Ctheta), uniformly s<=T,

    Tr(P2 sigma(s))<=exp(2theta-theta N/2).              (18)

The checked dressed mean-hole estimate supplies independently

    Tr(P2 sigma(s))<=C_T epsilon² N.                    (19)

For N<4 log(1/epsilon)/theta use(19); for larger N use(18). Thus

    sup_(safe L,S,s<=T) Tr(P2 sigma(s))
                    <=C_T epsilon²[1+log(1/epsilon)].  (20)

Only the count-moment and mean-hole premises are used. No local-island tail or probability conditional on a selected hole is inferred. The local circuit's spatial coloring does not affect this global count argument. This repeats the old small-time mechanism on the EXACT Y frame by count invariance; it is not a new proof of a local source law.

Let O_s be any bounded neutral exact-D backward joint test, or any bounded neutral measurable family, ||O_s||<=1, with the original monitored labels and passive reference retained. Then(10),(20) imply the actual-state estimate

 |epsilon^-2 integral_0^T epsilon² Tr[sigma(s) P2 T(O_s)P2] ds|
                <=C_T epsilon²[1+log(1/epsilon)] ->0.   (21)

There is no support-radius cost in(21);(10) summed the whole marked operator before taking the expectation. In particular the potentially very large backward cone has not been replaced by a finite cone with an unjustified error.

The displayed quantity is an algebraic BLOCK CONTRIBUTION, not an experiment which measures P2 or prepares sigma conditionally. For the actual Omega state, total record count is block diagonal, including the original classical history, because H,Y preserve it and each original mark raises it by two on both density legs. Neutrality of T(O_s) then makes the W,Ntot blocks legitimate expectation summands. At W2,Ntot=2N-2 the B occupation is forced to be saturated, so there is no discarded coherent alternative B mask inside that block. Equation(21) can also simply be read as the displayed compressed scalar functional without making any claim about other summands. It supplies no smallness for a block with many unsaturated B sites, nor a complete bound on the remaining higher corrector terms.

## 6. A bounded-coboundary obstruction for the complete rotor tangent

This is an all-state algebraic obstruction, not a bare-Omega counterexample. Fix L divisible by4, L>=8, and retain the entire physical Gauss/charge/field carrier. On K2 the rotor fast generator is

    B2*(rho)=-i delta[H,rho], H=FF*,
    T*(rho)=i alpha[Q,rho], Q=FGF*, alpha=kappa²/(2delta). (22)

Suppose a bounded normal superoperator S, with bounded trace-class predual, solved [B2,S]=T on the neutral algebra. Its dual would satisfy T*=S*B2*-B2*S*. S is allowed to leave K2, to be nonlocal, and to mix quantum components. The following contradiction is therefore stronger than failure of a scalar rephasing. It does not exclude unbounded correctors on a restricted source norm.

First construct a legitimate physical fiber. For every finite charge word with total Gauss charge N, choose an integer reference link flow solving its Gauss equation. Every other physical field differs by an integer circulation in the cycle lattice of the finite connected torus graph. This lattice is free of rank d=|edges|-|vertices|+1=2L³+1. In these coordinates the rotor space is a finite charge-word space tensored with ell²(Z^d). Each actual hop or birth is a charge-word partial permutation times an integer cycle translation. Fourier transform gives continuous finite Laurent matrices H(theta),Q(theta). No electric field coordinate is discarded.

At theta=0, all translations have value one. On K2, fix the actual Nminus=(N-2)/2 charge count. For each unordered pair of A holes, use the normalized equal superposition of ALL allowed +/- assignments to its occupied sites with this count. Each two-hop path permutes the assignments bijectively, so these equal-weight vectors form a reducing subspace of H(0),Q(0). Self-adjointness promotes invariance to reduction. This finite subspace is an exact charge-symmetric fiber, not a replacement pair-boson model. Its dimension is D=N(N-1)/2.

Here are its literal rows. For an input hole pair {h,u}, choose one filled-in hole h, one b adjacent to h, then an occupied A site c adjacent to b, c!=u. The final holes are {u,c}. H contributes one for each such inward/outward path. Q contributes two exactly when u is also adjacent to b. Sum both choices of filled-in hole. In particular H_diagonal=12 and ||H-12I||<=60. Elementary endpoint counting gives

    Tr Q=60N,
    Tr Q(H-12I)=432N>0.                                (23)

For the first formula each b has fifteen unordered neighboring hole pairs, each with diagonal weight4. For the second, fix b and ordered distinct u,c among its six A neighbors. The number of common B neighbors of u,c sums to6*1+24*2=54: six ordered opposite pairs and twenty-four ordered perpendicular pairs. The original second hole h can be any of the other four A neighbors of b. The Q factor is2. Thus each b contributes2*4*54=432. This counts the COMPLETE off-diagonal covariance, including path multiplicities; diagonal subtraction removes the twelve return paths. On safe L>=8 there are no extra aliases. The additional control identities Tr(H-12I)²=54N(N-2) and Tr Q²=912N are corroboration, not necessary premises of the obstruction.

Choose an eigenbasis of H which also diagonalizes Q inside each degenerate H eigenspace, and put q_n=<n|Q|n>. Formula(23) implies that these diagonal values are not all equal. More quantitatively, their range is at least

    Delta_q >=432N/(60D)=72/[5(N-1)].                    (24)

Indeed subtract any q between their extremal values in the trace covariance and use Tr(H-12I)=0 and ||H-12I||<=60. Pick n,m with this difference and X=|n><m|. It is a Liouville eigenvector with lambda=-i delta(E_n-E_m). The spectral-frequency projection of T*X onto its lambda eigenspace is exactly

    i alpha(q_n-q_m)X.                                 (25)

Other Q matrix elements with this same frequency would require an equal H eigenvalue on the changed leg, and vanish by the within-degeneracy diagonalization. This is a resonant component; finite matrices already show why a commutator cannot remove it.

A single zero-angle fiber is NOT a normalizable physical state, so it alone would not prove the claimed obstruction. Complete that step as follows. Choose a smooth normalized scalar packet f_w(theta) supported within distance w of zero. Let psi_n=f_w tensor v_n and psi_m=f_w tensor v_m in the physical Fourier representation, and X_w=|psi_n><psi_m|. These are legitimate physical vectors/coherences, with finite electric moments of every fixed order; those moments grow as w shrinks and no uniform field-moment claim is made. They have trace norm one. Since the fixed-torus Laurent matrices are Lipschitz,

    ||(B2*-lambda)X_w||_1<=c_L w.                       (26)

The restriction of B2* to these inputs is unitary evolution in K2. Comparing H(theta),Q(theta) to their constant theta=0 matrices by Duhamel bounds the difference of the frequency-modulated integrals by c_L(u+u²)w. The frozen finite-matrix integral has, by its contractive time-average frequency projection and(25), norm at least alpha Delta_q u. Consequently

 ||integral_0^u exp(-lambda t) exp(t B2*) T*X_w dt||_1
                     >=alpha Delta_q u-c_L(u+u²)w.     (27)

This comparison applies separately to both theta legs of the rank-one density kernel, so it does not identify different nonnormalizable fibers or GNS vectors.

If the bounded cochain existed, differentiating exp(-lambda t)exp(tB2*)S*X_w and using its equation would instead give the upper bound

    2||S*||+u||S*|| ||(B2*-lambda)X_w||_1.              (28)

The full finite-torus B2* semigroup is trace-norm contractive; no assumption that S* preserves K2 is needed. Choosing w=u^-3 contradicts(27),(28) as u tends to infinity. At fixed torus the rotor B2 generator is bounded, so this integration by parts has no unbounded-generator domain gap. One may take real and imaginary Hermitian parts of the coherence witness if desired. Its role is an operator identity test, not a proposed probability preparation.

There is thus no bounded normal full-carrier superoperator cochain for the complete tangent, already on one safe finite rotor torus. No finite-spin impossibility is deduced by exchanging this packet limit with S tending to infinity. Nor does this result refute the actual-Omega physical-time response: the diagnostic original escape, omitted by B2 but retained in section4, is precisely what can pay the susceptibility.

## 7. Control, alternatives and terminal missing quantity

The one new control streamed255 relative two-hole rows on L8,N256 from literal two-hop endpoint operations. It checked reverse-row Hermiticity and diagonal paths, then obtained exactly

    TrQ=15360, TrQ(H-12I)=110592,
    Tr(H-12I)²=3511296, TrQ²=233472.

Maximum H row sum was72; maximum Q row sum40 (the proof only requires144). No eigenvalues or dense full carrier were computed. Frozen pre-execution expectations matched on the first run. Scientific-section runtime was3.885723 CPU seconds,3.892827 wall seconds, peak19,218,432 bytes, with four thread settings1. Imports precede that timing; it is not an invented whole-child figure. CPU cap30seconds, internal90second wall and120MiB checks, and campaign deadline/STOP guards were active. No failed execution or rerun occurred. The control proves neither the physical fiber embedding nor the packet/response theorem; those are the analytic arguments above.

The distinct mathematical families are: a resonant superoperator cohomology test, a common first-event passive-response estimate, and consumption of an already checked actual global source tail. The first fails for a concrete complete-tangent reason. The second succeeds on the exact two-hole saturated diagnostic block without a fast gap and even without a time cost. The third turns its bounded global signed coefficient into the actual small-time retarded slice(21). The former crude sqrt(t) Duhamel estimate was superseded by the stronger root-proposed differential calculation; no result relies on that abandoned price.

To extend this to the full consumer one needs a bound for the COMPLETE phase/current and cross-corner response in the ACTUAL continuously forced environment, where multiple original events and unsaturated B sites remain. In the general dark identity both a_mu and d_mu occur, R need not preserve darkness, and the phase Hamiltonian is not tied solely to a single terminating exact-loss map. The first-event proof cannot simply be iterated: total events may be extensive, later coherent source blocks are not independent, and ell-versus-d errors would also need their actual weighted summation. A concrete sufficient replacement would be a common-dilation derivative estimate in a local actual-source norm whose squared cost is controlled by a spatially summable integrated ORIGINAL activity, together with the explicit R dark/bright-corner contribution. The existing local negative budget does not supply that backward norm. This is a response estimate stronger than the current local source moments, not a newly proved auxiliary theorem or a full-limit conclusion disguised as one.

No all-state uniform susceptibility for arbitrary backgrounds, original output convergence, microscopic field UI, axiom adoption, new observed label, modified preparation or scientific no-go follows. The fixed physical interval in(21) is epsilon-independent but explicitly small; the normalizable rotor packets in section6 are not actual-Omega conditional states. These limits remain separate.
