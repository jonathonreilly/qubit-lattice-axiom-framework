# Outgoing reference concentration with an L2 horizontal-contour estimate

Status: new authored scalar-reference derivation, requiring a distinct check. At fixed kappa=1e-8, hard halfwidth Delta=4e-6 and the declared attached reference phase, define the normalized outgoing packet on the full integer lattice by

    b(t,n)=(1/sqrt(2pi p0)) integral_I F(q) exp(iqn-itE(q))dq,
    F(q)=kappa E'(q) zeta exp(i61q+i172k(q))/(sqrt(2pi)jD(q)),
    I=[pi/2-Delta,pi/2+Delta],
    E(q)=2j(1-cos q), D(q)=E(q)-2j+gamma exp(iq),
    gamma=kappa^2/j, p0=integral_I |F(q)|^2 dq.

Here .0027<j<.003, k(q)=2 arcsin(sqrt(j/J) sin(q/2)), and zeta is the unchanged fixed calibration scalar. Put

    h=kappa^2/(4j^2), v=.0053, s_t=vt-104.

For s_t>=1 the proposed explicit bound is

    ||b(t)||_(n<=0) < Q(t)
       :=2.01 exp(-vth)+.75/sqrt(s_t).                 (A)

Consequently a single sufficient reference onset T=1e15 gives, for every t>=T,

    ||b(t)||_(n<=0)<2.8e-6,
    sum_(n>=1)|b(t,n)|^2 >1-7.84e-12.                (B)

For the unnormalized packet b_I=sqrt(p0)b, its full-lattice squared norm is exactly p0, and its right-ray squared norm exceeds p0(1-7.84e-12)>1-1.100008e-6. This is a concentration result for the scalar reference only. No actual attached runtime or complete transfer theorem is inferred.

## Sources and exposure

Read completely the unchanged wider temporal proposal SHA256 `f407f29620b318e6253a0d75ec9a7a3007be89ff41786f753899d30805eee8cc`, its complete distinct review SHA256 `1182667f9f46a2fd7828558f68be95d9bc742c69bb6cf72617ced810edcc931f`, and the complete narrower temporal route SHA256 `add82a40ddc49a7c7954ea1b087b1b1bf348e8375da072c96b2b2df1b6d2c011`. Only their explicit scalar reference definitions and contour method are reused. Their interacting complex-kernel, localized-column and actual temporal conclusions are not premises here. The scalar estimates needed below are rederived on the changed phase and half-line.

The complete incoming reference source `../record_incoming_alltime/PROPOSAL.md`, SHA256 `1def426f0919789b6a1a8c4048756c3a95a6a2b9ed4b5223c90e0ca321db8bf7`, and my selective review `8ea2e16b8683ecc1eb9c2f92397d372d9ddb55cdc87c780bcd1755677cb76caf` supply the already exposed exact phase and reference normalization. Its full-band scalar extension is not needed for this outgoing contour. The previously read exact reference-measure check `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae` and wider-band source `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2` supply p0>1-1.1e-6. I authored the latter extension and the incoming review; this is new source-exposed author mathematics, not independent verification of itself or that ancestry.

The parent requested a practical scalar onset improvement and specified the phase and output boundary. No desired actual-device conclusion is assumed. Applicable unchanged workflow is reused. No scientific execution, numerical integration, dynamics, parameter sweep, delegation, W/Git, model, prompt, audit or publication change occurred. Only this artifact was written; no editable prompt file changed.

## 1. The shallow scalar strip and the changed phase

The reference phase is Phi(q)=61q+172k(q)+constant: the old 21q carrier plus the attachment's 40q. On the rectangle q=x-iy, x in I, 0<=y<=h, one has h<3.5e-12. The explicit arcsin branch stays analytic. Indeed a=sqrt(j/J)=sqrt(1-C0)<1/3, and both |sin(q/2)| and |cos(q/2)| are below .708 on this tiny rectangle. Thus

    |k'(q)|=|a cos(q/2)/sqrt(1-a^2 sin^2(q/2))|
           <(.708/3)/sqrt(1-.708^2/9)<.25.

The denominator is on the principal square-root branch and bounded away from zero. Hence |Phi'|<61+172/4=104 and

    |exp(iPhi(x-iy))|<=exp(104y).

This is a scalar-only continuation, with no interacting resolvent extended to depth h. The growth has the opposite sign to the incoming lemma and is explicitly paid. Also Im E(x-iy)=-2j sin x sinh y, with 2j sin x>v, so

    |exp(-itE(x-iy))|<=exp(-vty), t>=0.

The complement of the requested output n>=1 is exactly n<=0. Write n=-m, m>=0. The spatial exponential has modulus exp(-my), including m=0 rather than omitting the output-origin coordinate.

## 2. Denominator margins and an L2 bottom bound

Writing gamma=kappa^2/j and A0=2j-gamma, the exact continued denominator is

    D(x-iy)=-A_y cos x+i B_y sin x,
    A_y=2j cosh y-gamma exp(y),
    B_y=gamma exp(y)-2j sinh y.

Since sinh y<=y exp(y) and 2jh=gamma/2,

    B_y>=exp(y)(gamma-2jy)>=gamma exp(y)/2>0.

Thus no outgoing resonance pole is crossed on the chosen strip. Also exp(h)<1.000001 and gamma/(2j)<7e-12 give A_y>.999 A0. In particular the stronger-than-needed A_y>A0/2 holds. At the bottom, therefore,

    |D(x-ih)|^2 >= (1/4)[A0^2 cos^2 x+gamma^2 sin^2 x]
                 =(1/4)|D(x)|^2.

The numerator obeys |E'(x-ih)|^2/|E'(x)|^2=1+sinh^2 h/sin^2 x<1.000001, while the squared phase growth exp(208h)<1.000001. Thus pointwise on I,

    |F(x-ih)|^2 <4(1.000001)^2 |F(x)|^2,
    ||F(.-ih)||_L2(I) <2.000002 sqrt(p0).            (C)

This comparison retains the narrow resonance's actual L2 mass. It does not multiply its peak by the entire cutoff width.

Deform the finite hard-band Fourier integral to the horizontal segment at depth h and both vertical sides. For its horizontal contribution to n=-m, write it as exp(-mh) times the m-th Fourier coefficient of

    g_t(x)=1_I(x) F(x-ih) exp(-itE(x-ih))/sqrt(p0).

Fourier isometry on an enclosing 2pi period and exp(-mh)<=1 give

    ||bottom||_(n<=0) <=||g_t||_L2
        <2.000002 exp(-vth)<2.01 exp(-vth).          (D)

The phase growth is already paid in (C); no additional exp(104h) is omitted or needed in (D). This is the improvement over the earlier per-coordinate peak bound followed by a geometric sum. It eliminates the old large bottom prefactor without changing h or crossing the pole.

## 3. Both cutoff sides

At x=pi/2±Delta, |D(x-iy)|>=A_y sin Delta>.0053 Delta. The last inequality follows directly from A_y>2j-gamma exp(h), j>.0027 and sin Delta/Delta>1-Delta^2/6; it does not use the weaker A_y>.999A0 alone as an unexplained bound. Also |E'|/j<=2 cosh h. Including 1/sqrt(p0), the entire coefficient F/sqrt(p0), with its phase growth removed, has magnitude less than

    170 kappa/Delta.

For example sqrt(2pi)>2, p0>1-1.1e-6 and cosh h<1.000001 give a prefactor below 190 from the denominator .0053 alone; to obtain 170 retain sqrt(2pi)>2.5, giving a prefactor below 152. This makes the numerical margin explicit.

Paying both vertical sides, including the outer Fourier factor 1/sqrt(2pi)>0 but less than 1/2.5, bounds each n=-m contribution by

    (340/2.5)(kappa/Delta) integral_0^h exp(-(s_t+m)y)dy
       <=136 kappa/[Delta(s_t+m)].

For s_t>=1 the decreasing-function estimate gives

    sum_(m>=0)(s_t+m)^(-2)<=s_t^(-2)+s_t^(-1)<=2/s_t.

Consequently the two sides together have half-line norm less than

    136 sqrt(2) kappa/(Delta sqrt(s_t))
       <300 kappa/(Delta sqrt(s_t))=.75/sqrt(s_t).  (E)

The phases of both sides are not presumed to cancel. Combining (D) and (E) by triangle inequality proves (A). The hard cutoff is retained exactly: no discarded side or unstated analytic cutoff appears.

## 4. One explicit onset and concentration

Take the single sufficient choice T=1e15, without a parameter sweep or optimality claim. Since j<.003,

    h>1/(3.6e11), vTh>14,
    s_T=5.3e12-104>(2.3e6)^2.

An elementary exponential witness is e>8/3, (8/3)^5>130 and (8/3)^4>50. Hence e^14>130^2*50=845000. At every t>=T both terms of Q decrease, and

    Q(t)<2.01/845000+.75/(2.3e6)<2.8e-6.

Full-lattice Fourier isometry gives ||b(t)||^2=1, independently of time. Orthogonal coordinate restriction then yields (B). For the unnormalized packet its exact total norm squared is p0, so

    ||b_I(t)||_(n>=1)^2
       >p0(1-7.84e-12)
       >(1-1.1e-6)(1-7.84e-12)
       >1-1.100008e-6.

If a unit-norm right-ray comparison vector is desired, its positive normalization changes the already restricted normalized packet by 1-sqrt(1-q_left^2)<=q_left^2<7.84e-12. Its distance from the original full-lattice packet still includes the left-tail amplitude; that normalization cost must not replace it.

## Scope and remaining check

The scalar reference has the same q dependence for each literal old-energy column, apart from unitary old aging and fixed W multipliers. Physical energy is b_j+E(q), so exp(-itb_j) factors on each ideal diagonal column; the declared common scalar also has unit modulus. These do not change its concentration. Orthogonal ideal old/parity fibers and passive references preserve this scalar bound without a sqrt(2) loss. This statement is about the ideal reference, not arbitrary actual cross-window error vectors.

The earlier wide temporal result's T=1e17 was a sufficient onset for a complete unattached apparatus bound, including localized columns. The present T=1e15 is solely a sufficient reference concentration onset, and does not improve that full-device theorem or certify an attached runtime. Relative to the earlier scalar contour method, the improvement is the bottom prefactor from order 1e6 to 2.01 at the same pole-free depth. Actual attached spectral synthesis, incoming coefficient comparison, local/closed record outputs, omitted actual mass and any finite truncation remain separate obligations. An independent check should focus on the shifted-coefficient Fourier isometry, denominator comparison (C), n=0 inclusion, changed phase104 and both cutoff sides.
