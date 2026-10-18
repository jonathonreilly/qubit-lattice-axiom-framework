# A uniform observation interval for the finite seeded router

New authored bounded derivation requiring a distinct check, conditional on the provisional complete composition in `common_product_finite_seed_router/PROPOSAL.md`, SHA256 `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`. That complete source was read and its identity verified. Its composition remains under distinct review; this extension does not independently validate its launch, attachment or finite-device premises. ROOT suggested considering endpoint-controlled observation intervals. The monotonicity and uniform existence arguments below are new author work, not an independent check of that suggestion.

The same finite static Hamiltonian and same seed admit a nonzero relative-width observation interval with a uniform complete-output error, provided the displayed quantitative margins hold. The outgoing common packet and the physical scalar phase remain time dependent. This is not a stationary output, capture/reset, permanent halt, or an old processor theorem.

## Fixed device, source quantities and window assumptions

Keep the source's fixed physical Hamiltonian H_phys, seed isometry E_seed, one-head domain, legal encoded programs, passive references, j=b^2/D0, 0<gamma<j, M>=3 and ell=M-1. All positive blocks, absent interactions, coefficient relations and preparation premises remain exactly as in the source. In particular the actual outer block is the equal-diagonal B_r, not full Laplacian deletion. The controlled path operation is C=P0 tensor X+P1 tensor I.

Keep one fixed spectral cutoff and one fixed normalized g=chi g_+/sqrt(p_chi) from that source. Set G_r=||g^(r)||_1, r=0,1,2, and vmin=2j cos sigma', vmax=2j, with sigma'<pi/3. Nothing in the proof varies g or the Hamiltonian with the observation time. Define the source tail function

    T(t,A)=[G1+(2jt/A)G0]/sqrt(2pi)
                         *sqrt(A^-2+A^-1), A>0.

Choose the same early comparison time t0 and its fixed error e0 from source equation (7), including e_early, delta_launch, d_right and A_early=ell+1-t0 vmax. Assume its hypotheses delta_launch<1, A_early>0 and t0 vmin>2. Select endpoints satisfying

    t0<=tminus<tplus,
    tminus vmin>ell,
    tplus vmax<2ell-2.                            (1)

For t in this interval, define

    A_late(t)=t vmin-ell,
    A_out(t)=2ell+2-t vmax,
    d_late(t)=T(t,A_late(t)),
    N_out(t)=T(t,A_out(t)).

Set the uniform allowances

    d_L=T(tminus,tminus vmin-ell),
    n_O=T(tplus,2ell+2-tplus vmax),
    d_O=n_O/(1-d_L).                              (2)

Require d_L<1 and d_O<1. These strict conditions ensure that every normalized packet used below exists throughout the interval.

## Endpoint bounds established separately

For positive A, F(A)=sqrt(A^-2+A^-1) is strictly decreasing. The late gap A_late(t) increases, while

    d/dt [t/(t vmin-ell)] = -ell/(t vmin-ell)^2<0.

Both nonnegative factors in T(t,A_late(t)) therefore decrease. Thus d_late(t)<=d_L on the whole interval. This argument uses the gap's form; T is not assumed decreasing in t for arbitrary A(t).

The outgoing gap A_out(t) decreases, and

    d/dt [t/(2ell+2-t vmax)]
                      = (2ell+2)/(2ell+2-t vmax)^2>0.

Both factors in N_out(t) increase, hence N_out(t)<=n_O. The source normalized outgoing-tail allowance is d_out(t)=N_out(t)/(1-d_late(t)). Its numerator and denominator both increase, so monotonicity of the quotient does NOT follow. Instead the independent bounds give

    d_out(t)<=n_O/(1-d_L)=d_O.                    (3)

For the boundary allowance use qi(t)=t vmin-1 and qo(t)=2ell-t vmax. Let A_i be the source's fixed nonnegative constant and define

    A_o(t)=G2+(6jt/qo(t))G1
                   +(2jt/qo(t)+12j^2t^2/qo(t)^2)G0,
    B_boundary(t)=(2pi)^(-1/2){
        (A_i/vmin)[1/qi(t0)-1/qi(t)]
        +(A_o(t)/vmax)[1/qo(t)-1/qo(t0)] }.

Here A_i=G2+(12j/vmin)G1+(4j/vmin+48j^2/vmin^2)G0. Over t>=t0 in the allowed pre-return range, the first bracket is nonnegative and increasing. The second bracket is nonnegative and increasing. Also t/qo(t) increases, with derivative 2ell/qo(t)^2, so A_o(t) is nonnegative and increasing. The product in the second term consequently increases. This proves B_boundary(t)<=B_boundary(tplus), without substituting endpoint values into a difference of uncontrolled signs. With d_hop=sqrt((j-gamma)^2+j^2), define

    e_B=sqrt(3)d_hop B_boundary(tplus).           (4)

The physical cell allowance is capped but nondecreasing in t, since kappa, j and epsilon1 are nonnegative. Thus its uniform bound is

    e_C=min{2,2kappa+tplus(8j kappa+epsilon1)}.     (5)

The early error e0 is fixed at t0 and is not re-evaluated at each observation time. In particular the factorial early comparison uses t0, not tplus.

## Uniform normalized target and full-output bound

For each t in [tminus,tplus], define the scalar outgoing amplitudes

    B_n(t)=(2pi)^(-1/2) integral_0^pi
                  exp(i[(n+ell+1)k-tE(k)])g(k) dk,
    beta_F(t)=P_(0<=n<=ell)B_packet(t)
                        /||P_(0<=n<=ell)B_packet(t)||. (6)

Here B_packet(t) is the sequence of amplitudes B_n(t), distinct from the scalar boundary integral B_boundary(t).

The source gives q_out(t)=||B_packet(t)||_(n>=0)>=1-d_late(t)>=1-d_L>0. The normalized discarded tail is at most d_O<1. More explicitly,

    ||P_(0<=n<=ell)B_packet(t)||
        >=(1-d_L)sqrt(1-d_O^2)>0.                    (7)

Thus the positive normalization in (6) is uniformly defined. It retains a common phase across paths and programs, including the translation exp(ik ell), scattering exp(ik), and dispersive phase exp(-itE(k)). The finite sequence is continuous in t and its denominator is bounded away from zero, so beta_F(t) is a continuous moving target; no phase fitting or discontinuous choice is needed.

At each t the provisional composition applies, and the independently established endpoint bounds give the single uniform statement

    sup_(tminus<=t<=tplus) sup_(||xi||=1)
      ||exp(-itH_phys)E_seed xi
          -exp(-i2bt)J_out(beta_F(t) tensor Cxi)||
       <= E_window,

    E_window=min{2,e_C+e0+e_B+2d_L+2d_O}.           (8)

The second supremum permits arbitrary coherent legal program/path inputs and passive-reference entanglement. Constants are dimension independent. The target has both emitters and mediator vacant and unchanged encoded legal programs, exactly as in the source; actual residual occupation is paid in the full vector norm. No actual output is normalized, projected or traced away. The unhalved channel distance is uniformly at most min{2,2E_window} for the corresponding time-indexed isometries. The actual Hamiltonian never switches at t0, tminus or tplus; t0 is a proof decomposition time and the other two specify an observation interval.

## Ordered existence with a fixed nonzero relative width

Let cmin=vmin/j=2cos sigma' and cmax=vmax/j=2. Since sigma'<pi/3, cmin>1 and cmax<2cmin. Choose once and hold fixed

    1/cmin<alphaMinus<alphaPlus<2/cmax.

First choose the same cutoff and rho=gamma/j sufficiently small for the source spectral-tail allowance, then hold rho and all derivative norms fixed. Next choose u0=jt0 sufficiently large to reduce the source launch remainder, right tail and incoming part of the boundary residual. These choices use the same ordered existence argument as the provisional composition; no derivative norm is assumed uniform as rho tends to zero.

Now increase the integer ell and set

    tminus=alphaMinus ell/j,
    tplus=alphaPlus ell/j.                           (9)

For all sufficiently large ell, (1) holds with strict margins: tminus vmin-ell=(alphaMinus cmin-1)ell, and 2ell-tplus vmax=(2-alphaPlus cmax)ell. The early source errors depending on ell tend to zero exactly as in the composition, with u0 fixed. The factorial order is ell+2 with fixed argument 4u0, and the early gap grows linearly.

At tminus, jtminus/A_late is constant and A_late grows linearly, so d_L=O(ell^-1/2). At tplus, jtplus/A_out is bounded and A_out grows linearly, so n_O=O(ell^-1/2); hence d_O tends to zero and its strict normalization condition eventually holds. For the boundary integral, A_o(tplus) stays bounded because jtplus/qo(tplus) is constant. Multiplication by d_hop=O(j) cancels the 1/j factor in each velocity denominator. The outgoing part is O(ell^-1). The incoming part is bounded by a constant times 1/(u0 cmin-1), already made small by the earlier choice of u0. These constants can depend on the fixed rho and cutoff. Thus the entire ideal error is uniformly small over the interval, not merely at one time.

After fixing these dimensionless choices, choose eta=b/D0 and zeta=D0/D1 small enough using the largest duration splus=jtplus=alphaPlus ell:

    e_C<=min{2,(2+8splus)sqrt(2)eta+2splus zeta}.

For any supplied incident-load cap Lambda>0, take the source's safe scale D1=Lambda/2, D0=zeta D1, b=eta D0 with eta<=1/8, zeta<1/2. The source's positive-block counts and load maxima are unchanged; this extension adds no sites or interactions. The whole interval rescales with j=eta^2 zeta Lambda/2 and gamma=rho j. Both endpoints remain finite for every fixed positive choice, although their physical magnitudes may be large.

The width and relative width are exactly

    tplus-tminus=(alphaPlus-alphaMinus)ell/j>0,
    (tplus-tminus)/tminus
                    =(alphaPlus-alphaMinus)/alphaMinus>0. (10)

They do not collapse when ell increases or when the overall bounded-load scale is reduced. This establishes a uniform relative-width observation window for arbitrarily small certified error under the ordered supplied-parameter existence construction. It does not assert an efficient runtime or an optimized width. Narrowing the spectral support or changing rho requires recalculating its derivative constants before using this argument.

## Scope and provenance

The complete composition at hash 3a195efc is the single scientific premise for this extension and remains provisional pending its own distinct check. Its underlying component hashes and physical premises are preserved by reference at that exact revision. This author previously checked the supplied-packet router and authored the outer-boundary lemma; that ancestry is exposure, not independent recertification of the composition or this extension. ROOT suggested the uniform-window question, but the separate monotonicity arguments and the mixed-endpoint normalization bound were derived here.

The observation is a coherent, time-dependent packet factor times Cxi, with the exact physical scalar exp(-i2bt). No time-independent spatial output, all-late behavior, stable classical Record, capture, reset, permanent halt, arbitrary processor or native supplier follows. A finite closed device can later return its head. Uncertain observation time without retaining its corresponding packet/phase description is a different operational question from the uniform time-indexed theorem proved here.

Only this proposal was created. No scientific executable, simulation, sweep, source modification, Git/canonical/publication/checkpoint/editable-prompt/model change or delegation occurred. Hashing was source-identity bookkeeping. No retained status or independent audit is assigned.
