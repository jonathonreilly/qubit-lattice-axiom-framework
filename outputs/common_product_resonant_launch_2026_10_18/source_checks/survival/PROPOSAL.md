# A uniform resonance approximation for standalone emitter survival

New bounded author derivation requiring a distinct check. For the exact standalone positive endpoint launcher, the survival amplitude is uniformly approximated by a phase-fixed exponential with an explicit O(rho^2) remainder. This is one sharper source-residual envelope, not a pure exponential decay theorem or a new finite-router resource certificate. The band-edge remainder is retained. The frozen microscopic finite composition452231 is not modified.

ROOT proposed the rational z-plane resonance route. The rational identity is verified below, but the useful bound instead comes from an exact energy-coordinate density and total-variation comparison with a normalized Cauchy measure. No physical density is replaced without paying its full L1 error.

## 1. Operator and checked premises

Use exactly the standalone launcher of sourcefb72f4ed: emitter s, lead n>=0, positive source block

    B=Q_gamma(s,0)+(2j-gamma)n_s+(j-gamma)n_0,

and uniform positive Q_j lead bonds. Here j>0, 0<gamma<j, rho=gamma/j, and Q includes its full double-occupation diagonal. On the one-head space every diagonal is2j, source hopping is-gamma, and later hoppings are-j. The physical seed is |s>, with all other heads vacant. The one-head generator is bounded and self-adjoint; no unrestricted infinite-many-head norm is assumed.

Adopt the checked complete emitter spectral measure used in fb72f4ed. It has mass one and no atoms or omitted singular mass for this operator. With A=2-rho^2 and d=rho^2,

    E(k)=2j(1-cos k),
    w(k)=2rho^2 sin^2(k)/[pi(A^2 cos^2(k)+d^2 sin^2(k))],
    a_s(t)=<s|exp(-itH_gamma)|s>
          =integral_0^pi w(k)exp(-itE(k))dk.       (1)

The full seeded vector and directed-packet normalization remain those of the launch source. This note changes only its scalar residual allowance R_t. Absence of atoms here is an adopted property of the standalone launcher; it is not transferred to the microscopic router or any finite graph.

## 2. Exact rational identity, with its domain retained

The phase-preserving source amplitude from derivative378086 is

    F(k)=g_+(k)=-i c rho exp(ik)/[A cot(k)-i d],
    c=sqrt(2/pi), 0<k<pi.

For z=exp(ik), cot(k)=i(z^2+1)/(z^2-1), so

    A cot(k)-i d
      =2i[1+(1-rho^2)z^2]/(z^2-1),
    F(z)=-(c rho/2) z(z^2-1)/[1+(1-rho^2)z^2].   (2)

This verifies ROOT's proposed factor and sign exactly. The rational continuation has poles +/-i/sqrt(1-rho^2), strictly outside the unit circle. Equation(2) retains the source complex phase, not only |F|.

Its physical Fourier integral still runs only over the upper half-circle. Also exp(-itE)=exp(-i2jt)exp[ijt(z+z^-1)] has an essential singularity at zero for t!=0. A fixed compact C2 cutoff is not an analytic function on a contour. Consequently closing the full circle and retaining only these rational poles does not follow from(2). No such contour manipulation is used below.

## 3. Exact energy density and normalized comparison

Put

    r=1-rho^2>0, lambda=rho^2/(2sqrt(r)), x=cos k.

The transformation k in(0,pi) to x in(-1,1) is one-to-one with reversed orientation. Since A^2-d^2=4r and |dk|=dx/sqrt(1-x^2), equation(1) becomes

    a_s(t)=exp(-i2jt) integral_R f_rho(x)exp(i2jtx)dx,
    f_rho(x)= [sqrt(1-x^2)/sqrt(r)] 1_(|x|<1) L_lambda(x),
    L_lambda(x)=lambda/[pi(x^2+lambda^2)].        (3)

Both f_rho and L_lambda are nonnegative probability densities. Mass one of f_rho is the checked spectral normalization, not a Lorentzian approximation; mass one of L_lambda follows from its arctangent integral. The factor and support in f_rho keep both exact band edges. In particular no second half of the k-circle is being inserted.

Write q_rho(x)=sqrt(1-x^2)/sqrt(r) on |x|<1 and zero elsewhere. Since integral(f_rho-L_lambda)=0,

    ||f_rho-L_lambda||_1
        =2 integral (q_rho-1)_+ L_lambda dx
        <=2(1/sqrt(r)-1).                       (4)

Indeed q_rho<=1/sqrt(r) everywhere; its positive excess is confined to |x|<rho. The negative part includes both the diminished edge density and the whole Cauchy mass outside[-1,1]. Equality of the two masses pays those contributions without dropping them.

For 0<rho<=1/2, sqrt(r)>=sqrt(3)/2, and

    2(1/sqrt(r)-1)
       =2rho^2/[sqrt(r)(1+sqrt(r))]
       <=(4/3)rho^2.                            (5)

For the final inequality the denominator is at least3/2: at sqrt(r)>=sqrt(3)/2 its value is at least3/4+sqrt(3)/2>3/2. This is a uniform numerical constant, not asymptotic notation.

## 4. Uniform all-time amplitude estimate

The normalized Cauchy characteristic function is

    integral_R L_lambda(x)exp(isx)dx=exp(-lambda|s|).

For completeness, at s>0 integrate the rational function times exp(isz) over the upper semicircle, retaining its simple pole i lambda. The arc vanishes: for radius R>2lambda the rational factor is O(R^-2), the arc length is pi R, and |exp(isz)|<=1 there. The residue gives exp(-lambda s). At s<0 use conjugation, and at s=0 use mass one. This energy-plane contour has no time essential singularity at its finite origin and does not act on a nonanalytic cutoff.

Combining this identity with(3)--(5), using the bounded test function exp(i2jtx), proves

    |a_s(t)-exp(-i2jt)exp[-j rho^2 |t|/sqrt(1-rho^2)]|
        <=2[(1-rho^2)^(-1/2)-1]
        <=(4/3)rho^2,
    0<rho<=1/2, j>0, all real t.                (6)

The physical phase exp(-i2jt) is fixed by the exact diagonal. It is not fitted after comparing moduli. At t=0 the exact difference is zero; the uniform ceiling need not be sharp. Equation(6) is an amplitude estimate, not a survival-probability approximation. Squaring an amplitude bound is permitted for a probability upper bound but does not give equality of probability laws.

Together with the previously checked variation bound, the useful replacement residual is, for t>0,

    R_res(t)=min{1, 2/(pi j rho^2 t),
       exp[-j rho^2 t/sqrt(1-rho^2)]
         +2[(1-rho^2)^(-1/2)-1]}.               (7)

Thus |a_s(t)|<=R_res(t). Taking the minimum preserves the old all-late algebraic decay while gaining a resonant-time envelope. The estimate with an additive O(rho^2) remainder does not assert pure exponential behavior or discard the eventual band-edge contribution.

An explicit tolerance corollary is: for 0<tau<1, if

    0<rho<=1/2, rho^2<=3tau/8,
    t>=sqrt(1-rho^2)/(j rho^2) log(2/tau),

then R_res(t)<=tau. This is a sufficient scalar source-vacancy time, not a complete directed-launch time: the incoming lead remainder and normalized target still have to be paid separately.

## 5. Complete-output use and limits

For exactly the fixed cutoff chi, raw incoming coefficient B_minus, tail probability ceiling P and lead allowance L_t of fb72f4ed, define only the changed scalar combination

    delta_res(t)=sqrt[R_res(t)^2+(L_t+2sqrt(P))^2].

The same exact decomposition a_s(t)|s>+O_t g_++I_t g_- and orthogonality of source/lead sectors give the unchanged comparator W_t=O_t(chi g_+):

    ||exp(-itH_gamma)|s>-W_t||<=delta_res(t).

Whenever delta_res(t)<1, W_t is nonzero and its positive normalization beta_t=W_t/||W_t|| satisfies

    ||exp(-itH_gamma)|s>-|0_s>beta_t||
        <=min{2,2delta_res(t)}.                  (8)

This is a legitimate substitution into the standalone launch theorem; it neither analytically continues chi nor changes its normalization or exact target phase. Two identical disjoint launchers preserve the same isometry bound for arbitrary supplied path/program/passive-reference input, with no additional branch factor. All source and lead output coordinates remain in the error. Any separately supplied common scalar is retained on the target as in the source theorem.

The new estimate controls survival only. It supplies no new incoming or outgoing spatial tail envelope, no stronger finite-boundary residual, and no improved finite-router epsilon exponent. In the currently frozen composition, the lead tails and integrated outer residual also constrain the early time and distance; reducing only R_t does not prove a new simultaneous family. This note does not alter452231 or its descendants.

Failed shortcut retained: poles outside the unit circle do not license a whole-circle physical transform, neglecting the essential singularity, or analytic continuation of the fixed C2 cutoff. The successful limited route instead compares exact normalized real-energy measures and explicitly pays their difference. It does not compute a sharp long-time band-edge asymptotic, prove the remainder optimal, or rule out a sharper future tail argument.

The physical interaction law, exact source compensation, absent couplings, one-head seed preparation and occupation basis remain supplied. No native law, old literal processor result, physical stopping/capture/reset, finite permanent halt, precision tolerance or practical resource claim is inferred.

## 6. Sources, exposure and work record

Complete reads and source identities for this task:

- next_resonance_route/ROOT_PROPOSAL.md: f20c4df3a7c6bd593be38b905ea90f97150eb194a5501327683f3eb1150ad026. This is an unchecked design suggestion, not an adopted theorem.
- common_product_endpoint_launch/PROPOSAL.md: fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4. Adopt its exact standalone measure/decomposition and already checked normalization at their stated scopes.
- common_product_launch_derivative_bounds/PROPOSAL.md: 378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8. Adopt its exact complex-amplitude cancellation and fixed-cutoff conventions; do not use a new derivative estimate here.

ROOT suggested exploitation of the rational resonance. The author reconstructed(2), derived the exact density(3), normalized comparison(4)--(5), and uniform envelope(6)--(8). This is source-exposed author work, not an independent check. A distinct reviewer should verify the density Jacobian and constants, complete mass-one premise, full real-line normalization comparison, physical phase, all-time characteristic-function identity, rho-domain and unchanged complete-output normalization.

Only common_product_resonance_tail/PROPOSAL.md was created. No scientific executable, symbolic solver, numerical integration, simulation, sweep, source/W/Git/checkpoint/editable-prompt/model change or delegation occurred. No retained status or independent acceptance is assigned.
