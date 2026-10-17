# Incoming reference on the physical output half-line for every nonnegative time

Status: new authored scalar-reference lemma, requiring an independent check. With the actual nominal converter/reference phase and the frozen attachment phase, the normalized hard-band incoming reference packet has

    sup_(t>=0) ||b_in,I(t)||_(ell2(n>=0)) < .00105.       (1)

The hard band remains I=pi/2+[-4e-6,4e-6], kappa=1e-8 and the output origin remains the final gate output o. No positive onset or negative-time theorem is substituted. This proves a reference incoming-wave bound, NOT that the actual attached spectral incoming coefficient equals that reference or has small discrepancy from it. Those matrix-coefficient and spectral-synthesis obligations remain explicit.

## Sources, exposure and scope

Read the complete autonomous_record_herald_route/PROPOSAL.md, SHA256653e37a16d328af0f02f38ae08c18a41716cd69236a39d60fb59e0fe0d4469b7. Its warning that a physical incoming-frequency term must be charged separately is the question addressed here. Use the previously completely read converter publication f8480df631730d3e4e9fadb07b73486a1e02aec650511f7eae859ae2dabbe311, exact free-reference check1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae, and wider-band source d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2 for the unchanged nominal j, reference normalization and tail. The frozen attachment fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457 supplies the extra transmitted phase -i exp(40iq), including the eighteen-edge cable.

I authored the attachment and earlier reference/temporal reviews. This is a new exposed author derivation, not independent review of that ancestry. Root identified the incoming-frequency gap and requested all-time control; it did not supply the contour/completion bound below. Applicable unchanged instructions/workflow are reused. No scientific execution, solver, sweep, delegation, W/Git/model/prompt/checkpoint edit or publication occurred. Only source reading/hash bookkeeping and this sole deliverable were performed.

## 1. Exact coefficient and metric

Write E(q)=2j(1-cos q), gamma=kappa squared/j and

    D(q)=E(q)-2j+gamma exp(iq),
    Dbar(q)=E(q)-2j+gamma exp(-iq).

On the real interval, Dbar is the conjugate of D. The old common phase is rho_n(q)=zeta exp(172ik(q)), since rho_g=-zeta exp(92ik) and rho_n=-exp(80ik)rho_g. Here zeta is the fixed unit-modulus canonical calibration scalar, common to all old columns. The nominal reference outgoing coefficient AFTER the added attachment phase is

    F_out(q)=(-i exp(40iq)) Fref(q)
            =kappa E'(q) zeta exp(i61q+i172k(q))
                          /[sqrt(2pi)j D(q)].          (2)

Thus the physical incoming REFERENCE frequency is represented by

    b_in,I(t,n)=(1/sqrt(2pi p0)) integral_I
                  conjugate(F_out(q)) exp(-iqn-itE(q))dq,
    n>=0, p0=integral_I |F_out| squared dq.           (3)

Any fixed unimodular old-column multiplier leaves this scalar norm unchanged. Equation(3) specifies the conjugation and propagation sign; replacing its phase by its modulus would lose the result. The physical scalar exp(-it c_att) and old aging are unitary factors and remain in the full comparison, although they do not change this scalar norm. No input-dependent phase adjustment is made.

For clarity, the following proof is for EXACTLY (3). An actual attached incoming coefficient must be identified by the real two-lip spectral jump and coherently compared with conjugate(F_out), including its old/parity multiplier and record half-difference. The statement is not obtained by declaring an outgoing resolvent coefficient to be the whole spectral density.

## 2. An auxiliary full-band extension, not a source-domain extension

Define the SAME explicit scalar functions for 0<q<pi, using

    k(q)=2 arcsin(a sin(q/2)), a=sqrt(1-C0)=sqrt(j/J).

This agrees with the nominal branch because cos k=C0+(1-C0)cos q and k is near k0 at q=pi/2. This extends a scalar reference formula only. It does not extend any interacting source calibration, matching inverse or actual coefficient outside its certified band. On this full real interval k is real, so all phase factors in(2) have unit modulus. The exact free-emitter spectral measure therefore gives

    integral_(0,pi) |F_out(q)| squared dq=1,
    integral_((0,pi) outside I) |F_out(q)| squared dq=1-p0<1.1e-6. (4)

The last inequality is the checked fixed-width reference tail, not an attached actual-seed mass statement.

Define the unnormalized auxiliary incoming packet b_full by replacing I in(3) by (0,pi) and omitting p0. Fourier Plancherel and half-line restriction imply, for every real t,

    ||b_in,I(t)|| <=[||b_full(t)||+sqrt(1-p0)]/sqrt(p0). (5)

The hard cutoff is therefore retained exactly via a charged tail. This does not assert its discontinuous truncated coefficient is analytic or silently replace the physical band by an uncut wavepacket.

## 3. Pole-free lower rectangle with the actual phase

Use the fixed scalar rectangle 0<=Re z<=pi, -1<=Im z<=0. No interacting kernel is continued onto it. For z=x-iy with0<=y<=1,

    Dbar(z)=-j exp(iz)-(j-gamma)exp(-iz).

Since0<gamma<j, its first term has magnitude j exp(y), strictly larger than (j-gamma)exp(-y); hence Dbar has no zeros on the closed rectangle. This also handles the corners without an unproved limiting prescription.

The nominal C0>.9 gives a<1/3. Since cosh(1/2)<1.2, |a sin(z/2)|<.4 throughout the rectangle. The principal arcsin is analytic there. Its imaginary part has the sign of the imaginary part of its argument: writing arcsin(v)=alpha+i beta, with |alpha|<pi/2, gives Im v=cos(alpha)sinh(beta). For this rectangle Im[a sin(z/2)]=-a cos(x/2)sinh(y/2)<=0. Thus Im k(z)<=0, and

    |exp(-i172k(z))|=exp(172 Im k(z))<=1.

The other actual phase contributes |exp(-i61z)|=exp(-61y). Moreover Im E(x-iy)=-2j sin(x)sinh(y)<=0. Therefore |exp(-itE(z))|<=1 for EVERY t>=0, including t=0. This favorable sign is what supplies all-time control. No replacement s_t=vt-64 or later onset is used.

Including the two Fourier factors, the analytic incoming integrand has prefactor kappa conjugate(zeta)/(2pi j), times

    [E'(z)/Dbar(z)] exp[-i(n+61)z-i172k(z)-itE(z)].

Contour deformation of the finite scalar integral bounds each lattice amplitude by the bottom plus BOTH vertical sides. All functions are analytic on a neighborhood of the closed rectangle; no half-plane asymptotic argument is needed.

## 4. Explicit bottom and two-side bounds

On the bottom y=1,

    |Dbar| >=j(exp(1)-exp(-1))=2j sinh(1),
    |E'|<=2j cosh(1), so |E'/Dbar|<=coth(1)<2.

The horizontal length is pi. Its amplitude contribution is at most

    (kappa/j) exp[-(n+61)].

Its complete half-line norm is therefore at most (kappa/j)exp(-61)/sqrt(1-exp(-2)).

At x=0 the denominator is -2j cosh(y)+gamma exp(-y), whose modulus is >=2j-gamma>j. At x=pi it has the opposite sign and the same modulus. E'(z) has modulus2j sinh(y) at either vertical edge. The two vertical sides together thus have amplitude at most

    (2kappa/(pi j)) integral_0^1 sinh(y) exp[-(n+61)y]dy
      <= (2kappa/(pi j))/[(n+61) squared-1].          (6)

The last integral was extended to infinity using a positive integrand, with n+61>1. The time multiplier has modulus one at those sides because E is real there; the phase-k multiplier remains at most one. No time oscillation or early-time cancellation was assumed.

Since (n+61) squared-1 >=(n+60) squared,

    sum_(n>=0) 1/[(n+61) squared-1] squared
       <=60^-4+1/(3*60 cubed)=7/4320000<1/750 squared.

Minkowski's inequality therefore gives the all-time explicit bound

    ||b_full(t)|| <=(kappa/j)exp(-61)/sqrt(1-exp(-2))
                         +2kappa/(750 pi j), t>=0.    (7)

At kappa=1e-8 and j>.0027, pi>3, the side term is <3.3e-9. The bottom is <1e-22 using exp(1)>2 and sqrt(1-exp(-2))>1/2. Hence ||b_full(t)||<4e-9 for all t>=0. These are elementary analytical inequalities; no numerical integration or dynamics was executed.

Finally sqrt(1.1e-6)<.001049 and1/sqrt(1-1.1e-6)<1.000001. Substitution in(5) proves

    ||b_in,I(t)|| <(.001049+4e-9)*1.000001<.00105,
    every t>=0.

This is a conservative cutoff-tail dominated bound. For the unnormalized hard-band reference used in a subnormalized herald target, the same bound holds without the p0 division, and is slightly smaller. The proof neither claims sharpness nor infers a native probability from this scalar reference.

## 5. Actual coefficient interface and remaining limitations

If the actual incoming matrix coefficient differs in L2(operator norm) from the required reference conjugate by epsilon_in, Fourier Plancherel and half-line contraction bound the ACTUAL incoming contribution by epsilon_in plus the appropriate reference bound above, after correct old/reference and record-sector aggregation. The possibly O(1) full-line norm of the reference does not defeat this estimate: only its outgoing-side incoming-frequency restriction was estimated by the analytic argument. Plancherel alone would give no .00105 conclusion for the reference term.

Conversely, arbitrary phase removal, a complex conjugation on the wrong factor, a different physical reference plane, or input-dependent source phases would change(3) and must be checked anew. The exact carrier61 came from21+40; the172k factor was retained and shown favorable rather than replaced by an adverse absolute derivative allowance. If another reference is chosen with the exact terminal phase -exp(iq) instead of the checked gate comparator -i exp(22iq), its extra phase must be carried explicitly and its corresponding contour estimate redone.

The remaining actual-device tasks are the two-lip incoming/outgoing coefficient identity, their coherent common-W comparison and L2 residual, actual omitted seed spectral amplitude, and the complete record-1 local/closed-tail bounds. The existing all-time conditional herald interface can then charge this incoming contribution as an additional same-ray term. It must not combine incoming and outgoing errors on the same ray by orthogonal quadrature without a separate orthogonality proof. No actual all-time herald theorem, success lower bound, normalized early-time correctness, new time window or finite-device all-time transfer is asserted here.
