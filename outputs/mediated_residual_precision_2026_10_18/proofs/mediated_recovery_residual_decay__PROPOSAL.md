# Static physical recovery plus an explicit decaying residual

Status: new conditional author derivation requiring a distinct check. Under the unchanged, checked mediated installation, full loaded inverse, physical matching and Hilbert-valued recovery hypotheses, the represented nontraveling map satisfies

    ||N_I(t)|| <= c_R A_s(t)+C_res/|t|, t!=0,
    c_R=1+sqrt(2)gamma_*/a.                            (1)

Here A_s(t) is the ACTUAL represented three-source norm, including both old-input energies and all source-fiber outputs. C_res is an explicit finite constant below. The coefficient c_R is exactly the one in the checked static recovery interface83530c67; the new term can replace its static E_rec allowance. The subtraction is a single all-fiber physical map, identical on both windows and lips. No source waveform, effective preparation, new Hamiltonian or fitted phase is substituted.

For fixed supplied coefficients and fixed background, with eventual rho=sqrt(a lambda), the displayed constant has the sufficient growth

    C_res=O(lambda^(-1/2)+log(1/lambda)).                (2)

The bound therefore retains the checked source exponential while avoiding the unweighted O(lambda^(-1)) contribution from integrating a full inverse-squared envelope. This is a structural estimate, not an evaluated onset or numerical improvement. All complementary terms remain, and the source comparison's calibration allowance is not eliminated.

## 1. Domain and actual represented maps

Retain every corrected-installation and exact mass-tuning condition of loaded5f909e1e/checkf6303bb3, recovery83530c67/check6f1b0755, source73116231/check496164c0 and nontraveling9e4dffc5/checka9738427. In particular:

- The original calibrated background, literal old K and W, shared B and common scalar c_att are unchanged. Port-cap replacement is literal replacement. Positive supplied microscopic blocks, roles, coefficients, geometry and the actual bare product preparation remain premises.
- a=J_m-q>0, b=.185-(J_m+q)>0, gamma_*=max_l gamma_l, n1=n2=2m-1 and n3=m. There are 10m-4 internal mediator heads. No global gap of the assembled apparatus is assumed.
- lambda=lambda_m>0, kappa=sqrt(3jlambda), 0<rho<=min(d_bg,a/2), rho/g<=1/2, lambda<=1e-8 and all original background-domain conditions hold. The exact finite gates eta<1, k_C>0 and zeta<1 must be verified for a chosen finite tuple.
- The actual regularity/matching premises identify the physical lower-minus-upper boundary columns on both CLOSED windows, including endpoints. The checked background lift and its derivative act in the full physical Hilbert norm of the finite background and all closed slow tails.

The windows are I_e=c_att+2j+e+[-rho,rho], e=1,3, and I=I_1 union I_3. The window index e is distinct from the complementary gap b above. On one window set

    D=(E-c_att-2j)I-B, DP=delta P, C=I-P.

P and C are constant within that window. C includes the other prepared energy as well as every other internal channel; |D_C|>=.185. Both lips use their own actual physical roots. Actual background operators need not commute with D or P.

Write S(E) for the PHYSICAL three-source Schur matrix and

    U(E)=S(E)^(-1)V_s, ||V_s||=1,
    Y_s(t)=Q_s exp(-itH)E_H(I)V,
    A_s(t)=||Y_s(t)||.

The coordinate identification of Q_s with the three-source Hilbert space is fixed. U includes the full bare-seed input space, not just the input selected on that window. Its original physical mass congruence and sign gauges remain in the exact matrix.

N_I(t) is the same represented nontraveling contribution as in9e4dffc5: source endpoints, every internal mediator head, the finite background and the closed-tail parts from both windows, embedded into the actual physical space and summed. It excludes the propagating stationary rays and the actual omitted vector E_H(I^c)V. The window-specific open/closed tail classifications need not yield orthogonal contributions. All estimates below sum the two windows by triangle after physical embedding.

## 2. A single static map, rather than window-dependent preparation

Let A_l be the fixed 2n_l-site positive-weight adjacency of mediator l, and let

    R_l(E)=(D tensor I+A_l)^(-1),
    R(E)=direct_sum_l R_l(E),
    R_0=direct_sum_l (I_fiber tensor A_l^(-1)).

Tensor order is chosen consistently with the physical coordinate identification. The important facts are that A_l^(-1) acts on mediator positions, is the identity on the ENTIRE internal fiber, is independent of E and of the lip, and has norm<=1/a. A_l need not be positive semidefinite; the checked spectral distance from zero supplies this inverse bound.

Let E_s inject only source endpoints into the three joint mediator-endpoint spaces:

    E_s(s0,s1,s2)=((s0,s1),(s1,s2),(s2,0)).

The endpoint injection into each internal chain is implicit. Its two endpoint ranges are orthogonal even when n_l=1, and the three internal paths are disjoint. Consequently

    ||E_s z||^2=||z0||^2+2||z1||^2+2||z2||^2
                  <=2||z||^2.                       (3)

Let E_p inject a port vector only at the right endpoint of the third chain, with norm one, and let Gamma be the block diagonal endpoint coefficient gamma_l. Exact recovery is

    internal(E)=-Gamma R(E)[E_s U(E)+E_p p(E)].      (4)

Define the ONE constant physical lift

    H_stat z=(z, -Gamma R_0 E_s z, 0_background).

Its norm is at most c_R from(1), by triangle and(3). It is not a new physical state preparation or an approximation to H. In particular it is applied to the actual represented Y_s(t), not to a mass-normalized or selected surrogate. It does not contain a port coordinate; the entire actual port-dependent recovery remains in the residual.

The nontraveling boundary column has the exact decomposition

    N_lip(E)=H_stat U(E)+Q_lip(E),                  (5)

where the source component of Q_lip is zero and its other components are

    Q_internal=-Gamma [R(E)-R_0]E_s U(E)
                                      -gamma3 R_3(E)E_p p(E),
    Q_background=L(E)K_p(E)w(E),
    w(E)=t3(D)J2 U(E),
    K_p=(I-S_p G)^(-1), S_p=s3(D),
    p(E)=G_tilde(E)w(E),
    G_tilde=(I-GS_p)^(-1)G=G(I-S_pG)^(-1).          (6)

In the third-chain term E_p denotes its unit endpoint injection. The port is a physical output only inside L; its appearance as an input to R_3 recovers different mediator coordinates. There is no extra output copy of p.

Since H_stat is literally the SAME map on both windows and lips, its combined Stone integral is H_stat Y_s(t). Thus

    N_I(t)=H_stat Y_s(t)+Q_I(t)                     (7)

as physical maps. A replacement by P-dependent static lifts would not justify (7) with the single norm A_s(t). No such replacement is used. The full R_3 in the port term of(6) combines its static and residual pieces exactly; neither is silently dropped.

## 3. Full selected/complementary row derivatives

The checked loaded block inverse and its physical congruence give bounds for the ROW OPERATORS of S^(-1), with their full source forcing domain. Put P_src=I_3 tensor P and C_src=I_3 tensor C, and define

    s=sqrt(1-3lambda/j), R_delta=sqrt(delta^2+lambda^2),
    f=6/[s(1-zeta)], x=b_mix/k_C,
    a_P=f(1+x), a_C=f*x*(1+x),
    A=a_P+a_C=f(1+x)^2, B_c=1/k_C,
    u_delta=A/R_delta+B_c.

Then

    ||P_src S^(-1)||<=a_P/R_delta,
    ||C_src S^(-1)||<=a_C/R_delta+B_c,
    ||S^(-1)||<=u_delta.                            (8)

For example the mass-congruent PP and PC blocks are bounded by f/R_delta and fx/R_delta; summing them gives the first row bound. The CP and CC blocks give the second. The fixed physical masses contract and commute with these output projections; fixed gauges preserve their norms. This proves (8) for arbitrary source forcing, which is essential when differentiating. The unsuppressed complementary B_c term remains.

Use the checked actual derivative ceiling ||S'||<=S1 from9e4dffc5. For explicit evaluation define

    r_*=min(a-rho,b), Gamma2=sum_l gamma_l^2,
    tau=gamma3^2/b,
    theta3=(1-rho^2/a^2)^(-m)-1,
    t_P=sqrt(Z2)*kappa*(1+theta3), t_b=max(t_P,tau),
    t_1=s_1=gamma3^2/r_*^2,
    nu=gamma3^2/[a(a-rho)], sigma=max(nu*rho,tau),
    e_rho=a0+b0*rho, G_b=1/j+e_rho, k=1/(1-eta),
    a0=8e-18, b0=46000/.0053+290/g,
    G1=196000000+16622/g,
    K1=k^2*(s_1*G_b+sigma*G1),
    Gt0=k*G_b, Gt1=k^2*G1+Gt0^2*s_1,
    S1=1+Gamma2/r_*^2+2*t_b*t_1*Gt0+t_b^2*Gt1.     (9)

Here b_mix=kappa(1+theta3)e_tilde*tau and e_tilde=e_rho/[(1-eta0)(1-eta)] retain their exact loaded definitions. The background derivative in(9) comes from physical matching, not differentiation of e_rho. The ordered identities are

    K_p'=K_p(S_p'G+S_pG')K_p,
    G_tilde'=(I-GS_p)^(-1)G'(I-S_pG)^(-1)
                                      +G_tilde S_p' G_tilde.

The internal identity R_l'=-R_l^2 gives the full-fiber t_1,s_1 ceilings and the source self-energy contribution in S1. These are already checked at the indicated scope. Nothing here bounds an actual derivative by differentiating an error envelope.

Differentiate the exact physical inverse, with V_s constant:

    U'=-S^(-1)S'U.

Using the ROW bounds(8), rather than substituting a selected column for the full inverse, gives

    ||P_src U||<=a_P/R_delta,
    ||C_src U||<=a_C/R_delta+B_c,
    ||P_src U'||<=S1*(a_P/R_delta)*u_delta,
    ||C_src U'||<=S1*(a_C/R_delta+B_c)*u_delta.     (10)

Equations(8)--(10) include complementary output and wrong-window prepared input on each lip. No complementary jump is asserted to vanish. They also hold with identity on any passive reference.

## 4. Ordered background and port residual, without losing t_P

The physical t3(D) preserves P,C, although G and K_p need not. Its selected norm is at most t_P, including sqrt(Z2); its complementary norm is at most tau. Put

    D_w=t_P*a_P+tau*a_C, e_w=tau*B_c,
    w_bar(delta)=D_w/R_delta+e_w.

Applying(10) before the loaded background yields

    ||w||<=w_bar,
    ||w'||<=t_1*u_delta+S1*w_bar*u_delta.          (11)

For the derivative, t3'J2U costs t_1||U||. The other term is bounded by t_P||P_src U'||+tau||C_src U'||, which is exactly the second term of(11). This preserves the small selected hopping and the small cross-row coefficient. Replacing t_P by max(t_P,tau) before this step would discard the improvement. The actual order remains L K_p t3 J2 and G_tilde t3 J2.

The background lift has the checked Hilbert operator bounds

    L0=14000,
    L1=1.00068*(7.29e16+3.31e7/g)+30,
    ||L||<=L0, ||L'||<=L1.

These include all finite background coordinates and complete closed tails. The combined background plus third-port internal recovery in(6), viewed as a map acting on w, has bounds

    H_p0=L0*k+gamma3*Gt0/r_*,
    H_p1=L1*k+L0*K1
                    +gamma3*(Gt0/r_*^2+Gt1/r_*).   (12)

Indeed differentiate L K_p and -gamma3 R_3 E_p G_tilde in their physical orders. The R_3 derivative is paid at 1/r_*^2 on ALL fibers. Consequently this part of Q_lip and its derivative are bounded by

    H_p0*w_bar,
    H_p1*w_bar+H_p0*[t_1*u_delta+S1*w_bar*u_delta]. (13)

No static background map common to the windows is presumed. Its entire actual response is in (13), including the port, complementary loading and the closed tails. No source pulse is used to estimate a background resolvent column.

## 5. Source-driven internal residual and its energy weight

Let d_P,d_C,e_P,e_C be the uniform constants

    d_P=1/[a(a-rho)], e_P=1/(a-rho)^2,
    d_C=1/a+1/b,       e_C=1/b^2.                  (14)

Exact internal resolvent identities imply

    ||(R_l-R_{0,l})P||<=d_P*|delta|,
    ||R_l' P||<=e_P,
    ||(R_l-R_{0,l})C||<=d_C,
    ||R_l' C||<=e_C.                              (15)

In (15), R_{0,l} is the block A_l^(-1) on EVERY internal fiber, not the actual complementary resolvent at a window center. The first comparison uses the selected identity R_l(delta)-A_l^(-1)=-delta R_l(delta)A_l^(-1). The complementary comparison uses the actual gap b and the triangle bound; complementary D is not small. P and C are fixed within each window, so their derivatives vanish. The source endpoint injection E_s commutes with these fiber projections.

For M_s=-Gamma(R-R_0)E_s U, equations(3),(10),(15) give

    ||M_s|| <= sqrt(2)gamma_* * {
       d_P*|delta|*a_P/R_delta
                       +d_C*(a_C/R_delta+B_c)},       (16)

    ||M_s'|| <= sqrt(2)gamma_* * {
       e_P*a_P/R_delta
       +d_P*|delta|*S1*(a_P/R_delta)*u_delta
       +e_C*(a_C/R_delta+B_c)
       +d_C*S1*(a_C/R_delta+B_c)*u_delta}.             (17)

Every term is from the product rule on the exact physical map. In particular the selected inverse-derivative term retains |delta|/R_delta^2, rather than 1/R_delta^2. The complementary inverse-derivative term has a_C/R_delta^2 AND the B_c/R_delta term. The former is small only through the checked cross coupling; the latter is not dropped. This is a row-wise norm estimate, not an assumed cancellation of the two lips or of a small scalar envelope.

## 6. Explicit residual constant and hard-edge Stone estimate

Define the positive exact integrals

    R_e=sqrt(rho^2+lambda^2),
    J_R=2asinh(rho/lambda)=int 1/R_delta,
    J_R2=2atan(rho/lambda)/lambda=int 1/R_delta^2,
    J_x=2(R_e-lambda)=int |delta|/R_delta,
    J_log=log(1+rho^2/lambda^2)=int |delta|/R_delta^2,

where every integral is over [-rho,rho]. Put

    w_e=D_w/R_e+e_w,
    I_w=D_w*J_R+2rho*e_w,
    I_wprime=t_1*(A*J_R+2rho*B_c)
       +S1*[D_w*A*J_R2+(D_w*B_c+e_w*A)*J_R
                                           +2rho*e_w*B_c].   (18)

These bound ||w|| at each hard edge, int||w|| and int||w'||, respectively. They result by integrating(11), not by differentiating w_bar.

For the source-driven internal residual define

    M_e=sqrt(2)gamma_* * {
          d_P*rho*a_P/R_e+d_C*(a_C/R_e+B_c)},

    I_Mprime=sqrt(2)gamma_* * {
       e_P*a_P*J_R
       +d_P*S1*a_P*(A*J_log+B_c*J_x)
       +e_C*(a_C*J_R+2rho*B_c)
       +d_C*S1*[a_C*A*J_R2+(a_C*B_c+B_c*A)*J_R
                                                  +2rho*B_c^2] }.
                                                               (19)

Equation(16) bounds both endpoint norms by M_e; direct integration of(17) gives I_Mprime. Now set

    Q_e=M_e+H_p0*w_e,
    I_Qprime=I_Mprime+H_p1*I_w+H_p0*I_wprime,
    C_res=(2/pi)*(2*Q_e+I_Qprime).                 (20)

All constants are nonnegative and finite at any fixed admissible finite tuple. Their dependence on the actual gap, g, inverse margins and length is explicit through(8)--(20) and the inherited loaded quantities. A numerical evaluation is not part of this proposal.

For one lip on one window, Q_lip is absolutely continuous as an operator from the fixed prepared input space to the physical output Hilbert space. The finite maps are differentiable there; L and its closed-tail lift are differentiable in their full Hilbert norm. The energy-independent embeddings of each window's closed channels into the physical tails are used before adding windows. Thus Bochner integration by parts gives

    ||int_(I_e) exp(-itE)Q_lip(E)dE||
                        <=(2*Q_e+I_Qprime)/|t|.   (21)

Both hard endpoints are retained and paid; no vanishing boundary value is assumed. Stone has two lips with factor 1/(2pi) and two windows; bounding them separately gives 2/pi. This proves ||Q_I(t)||<=C_res/|t| and then(1) by(7). No cross-window orthogonality, entrywise imaginary-part rule or same-lip adjoint substitution is used.

The exact kernels retain exp[-it(c_att+2j+e)] and all original signs and physical mass factors. Unit scalar phases are discarded only inside estimates. The source mass was never normalized away, and no different reference phase was selected. Record/parity sectors combine with their original normalized input weights; the full operator estimates remain valid on arbitrary coherent old inputs and passive references.

## 7. Source exponential, comparison with the old recovery, and scaling

The independently checked source theorem73116231 gives

    A_s(t)<=min{1,F_Z(lambda t)+S_s}
           <=C_s exp(-lambda t/2)+S_s,
    C_s=9/sqrt(Z0), t>=0.                          (22)

Use exactly its physical F_Z and S_s, including selected source comparison, complementary SOURCE output, wrong-window INPUT, reference finite-band error and reference-only truncation. No actual mediated moment or exact mediated scalar pulse is asserted. Combining(1) with(22) gives

    ||N_I(t)||<=c_R*C_s exp(-lambda t/2)
                              +c_R*S_s+C_res/t, t>0. (23)

For a desired represented-nontraveling allowance epsilon>c_R*S_s, set d=epsilon-c_R*S_s. The explicit sufficient LOCAL criterion

    t>=max{(2/lambda)*max(0,log(2*c_R*C_s/d)),
                                      2*C_res/d}     (24)

then makes (23) at most epsilon. It is not an arrival, normalized output, finite-cut or full runtime criterion. If epsilon<=c_R*S_s, this certificate does not establish the target; it does not prove a physical residue or an impossibility.

The checked old recovery bounds the SAME N_I by c_R A_s+E_rec, so the safe combined interface is

    ||N_I(t)||<=c_R*A_s(t)+min{E_rec,C_res/|t|}.     (25)

One may also take the minimum of the whole right side with the independently checked full-nontraveling C_decay/|t| from9e4dffc5. These are alternatives for the same represented contribution, not extra additive error charges. C_res and C_decay are decay constants; neither is the unrelated positive-block scalar shift C_phase. For a shifted implementation the known global phase and window shift must still be supplied.

For the asymptotic claim(2), fix one exact supplier solution, a>0, original j and fixed background g,h. Take the checked family rho=min(d_bg,a/2,sqrt(a lambda)); for sufficiently large m its last branch applies and the inverse margins stay bounded away from zero. Then

    a_P,A,B_c,S1,H_p0,H_p1,t_1=O(1),
    a_C=O(sqrt(lambda)*(a0+b0*rho)),
    t_P,D_w=O(sqrt(lambda)), e_w=O(1),
    J_R,J_log=O(log(1/lambda)),
    J_R2=O(1/lambda), J_x=O(rho).

The direct complementary e_w and B_c need not be small. Nevertheless I_w=O(sqrt(lambda)log(1/lambda)), while

    I_wprime=O(lambda^(-1/2)+log(1/lambda)),
    I_Mprime=O(lambda^(-1/2)+log(1/lambda)),
    Q_e=O(1).

The only unweighted J_R2 factors in(18)--(19) carry D_w or a_C; neither has been replaced by an O(1) coefficient. The selected static-residual term instead carries J_log. This proves(2). In particular, for any fixed scaled time xi>0 at t=xi/lambda,

    C_res/t=O((sqrt(lambda)+lambda log(1/lambda))/xi)
                    ->0.                           (26)

The calibration floor a0 is retained in every constant and in the limiting S_s certificate. It does not become a nonvanishing a0 log(1/lambda) error in(26). The c_R S_s allowance remains and need not vanish. No asymptotic statement here is uniform if g, the mediator gap or an inverse margin changes with m. At a fixed physical t, (2) alone gives no useful small residual as lambda tends to zero.

The large checked L1 can still dominate a finite constant through H_p1 I_w. There is no assertion that (25) is smaller than the old bound at every finite tuple or at any previously published point. No numerical substitution, parameter search, improved device count or performance comparison has been made.

## 8. Limits, unsuccessful shortcuts and required check

Subtracting only a selected, window-dependent A_l^(-1)P map would not give the common H_stat Y_s(t) term in(7). Treating all of U' by the unweighted u_delta^2 ceiling and all t3 by max(t_P,tau) would reintroduce a J_R2 coefficient of order one. Those are losses or gaps in those estimates, not obstructions to physical escape. The proof above avoids them through a fixed physical lift and full selected/complementary row bounds; it does not presume a better actual cancellation.

The exact background ordering, physical sqrt(Z2) in t_P, complementary B_c term, both lips, both windows, hard-edge terms and complete closed-tail output all remain. No selected output is mistaken for a full inverse domain. In-band spectral identification is imported only at its checked fixed-tuple scope. Actual outside spectral mass, including any atoms, is not part of N_I and is not charged here; a complete composition must add it once globally. Propagating rays, exact common-output normalization, finite receiver cuts and readout interfaces remain separate.

This is one author proof proposal with explicit constants. Before downstream use a distinct check should reconstruct (5)--(7), the full-row derivative estimate(10), the physical ordered forcing estimate(11), all terms of(19), and the factor 2/pi in(20). It should also verify that the static lift is identical on both windows and that the closed-tail derivative is used in its actual Hilbert space. Existing ancestor checks do not supply that check of the present argument. No retained status, native supplier, arbitrary-fault tolerance, autonomous capture, reset/reuse or permanent finite storage claim is made.

## 9. Exact source exposure

The six recovery/source-time/nontraveling argument and review files below were read completely for this task. The unchanged full loaded inverse was previously authored/read in this lane; its exact physical-kernel, port-order, full-block and asymptotic passages were refreshed here. Regularity is reused at its exact checked scope through the fully read source-time and nontraveling arguments, rather than claimed as newly re-audited. All listed bytes and hashes were checked. Paths are relative to the renewal directory.

| Source | Bytes | SHA256 |
|---|---:|---|
| `mediated_apparatus_recovery/PROPOSAL.md` | 15232 | `83530c67a650ae309fa920c0d149388080bb47178fd2b9f2a4cba88512be6333` |
| `mediated_apparatus_recovery_check/REVIEW.md` | 4889 | `6f1b07555cd71a9e4208041c5249e892cf4b7f41ea25c92ed47c5b22b974a79f` |
| `mediated_source_time_composition/PROPOSAL.md` | 22918 | `73116231ff9d68e030b86def616eb69c088d72647005049279d82b5d0ab4137e` |
| `mediated_source_time_composition_check/REVIEW.md` | 6294 | `496164c0b8fff7dcd6bdb5f2037ba07c7954bd1720f2c6f881030a6b47fd7ebb` |
| `mediated_nontraveling_time_decay/PROPOSAL.md` | 14233 | `9e4dffc592cb259b58090b64016807f8f34024c2d07050467d30bc2042d71404` |
| `mediated_nontraveling_time_decay_check/REVIEW.md` | 5990 | `a973842794e10806684ebddbbe89a0f1cf1f1cb6a0eb04c56bfc3b5f27c47240` |
| `mediated_loaded_inverse_interface/PROPOSAL.md` | 26824 | `5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22` |
| `mediated_loaded_inverse_interface_check/REVIEW.md` | 10993 | `f6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3` |
| `mediated_seed_regularity/PROPOSAL.md` | 10238 | `f8153ddb6a86a58e04e9d69a1ef98d13feefe8f0171ba3cbb3e98cf35ae4522b` |
| `mediated_seed_regularity_check/REVIEW.md` | 11101 | `9d837417cc295e6d96fcaf1c8db5aad508d618f90cd57bcb9d560bb70640ea6d` |

I authored the loaded interface, source-time composition and some background ancestors, and have substantial source exposure. Root proposed the fixed all-fiber subtraction as a hypothesis and explicitly warned about complements, background forcing and different window maps. Those suggestions were not evidence. The new row-wise differentiated recovery and formulas(10)--(26) are the present reconstruction and require a distinct check. This is not a blind review of another author.

The lane-builder guidance was used only for premise, evidence and scope discipline. Current supplied task constraints govern the single-file author deliverable. No instruction, prompt or physical axiom was changed. No numerical scientific execution, solver, dynamics, quadrature, point evaluation, sweep or delegation occurred. Only this PROPOSAL.md was written; no W/Git/PR/publication/checkpoint/model changes occurred.
