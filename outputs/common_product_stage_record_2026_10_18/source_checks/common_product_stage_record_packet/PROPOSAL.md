# Explicit packet envelopes for the staged shared-record network

New bounded author continuation, conditional on the frozen stage-record composition c91300a5, whose distinct check is pending at assignment. This note supplies explicit, deliberately enormous derivative and internal-coordinate bounds, exact packet normalization, and early/late nonstationary tails. It does not construct finite emitters or finite output cuts, infer a resource exponent, or establish a completion herald.

The actual network, positive blocks, one shared record, four external rays and reference planes are exactly those of c91300a5. In particular both cables have34 edges, the common stationary phase is phi=-i exp(57ik), and the physical scalar is c_total=8b+2c_R. All legal program sectors, both record-X sectors and arbitrary passive references are retained. ROOT requested explicit internal recovery rather than an assumed pole-free inverse; the writer margin below is proved from its actual finite recurrences.

## 1. Domain and notation

Fix a compact band K inside |k-pi/2|<=h<=10^-3, eta=b/D0<=1/8, 0<zeta=D0/D1<1/2, j=b^2/D0, E=2j(1-cos k), and z=exp(ik). Use v_min=2j cos(h), v_max=2j. Let

    e=13eta^2+5zeta, w=33h, den=1-ew>0,
    d=34, lambda0=1-3eta^2,
    deltaS=min{2,[2(e+w)+ew]/den}.                (1)

These are sufficient uniform ceilings, not actual reflection amplitudes. Scattering and internal maps below are functions of k; their bounds are uniform on K. Input space is the full four-external-port/program/record fiber. Program and record-X sectors are direct sums, so maxima of sector bounds apply without dimension factors. The passive-reference tensor factor is arbitrary.

All norms denoted by constants are operator norms. A smooth scalar g in C_c^2(K) has ||g||_2=1 and G_r=||g^(r)||_1. No particular launch profile or bandwidth-dependent G_r scaling is silently imported.

## 2. A quantitative writer inverse proved from the graph

For either record-X value x=+/-1, let H_w,int/j be the real symmetric24-by24 one-head writer matrix after removing its common vacancy scalar and deleting external lead hoppings while retaining the port diagonals2. Let E_UF embed its two port values and P=E_UF E_UF*. Its outgoing boundary matrix is

    L_x(k)=H_w,int/j-(E/j)I-zP.                 (2)

For an incoming two-port column f, the exact internal solution is

    V_x(k)f=-2i sin(k)L_x(k)^-1 E_UF f,
    S_w,x(k)=E_UF* V_x(k)-I.                    (3)

The sign follows by substituting psi_1=z psi_0+(z^-1-z)f into the actual -j external hopping equation. The port values are incoming plus outgoing, not outgoing alone.

Here is an explicit inverse bound, not a presumption that no poles exist. For an arbitrary24-vector q, set y=L_x q, p=||Pq|| and Y=||y||. The two port equations, using the invertible orthogonal Hadamard junction, bound the pair of arm attachment values by7p+Y. The coefficient bound7 is conservative: all dimensionless onsite coefficients minus E/j have modulus<=7, and the extra port term has modulus1 (at the ports their combined bound7 still holds). The next inward pair, obtained from the attachment equations, has norm at most7(7p+Y)+p+Y<=50(p+Y).

Each subsequent arm step has nonzero hopping magnitude between1 and sqrt(2), and onsite difference of modulus<=7. For the pair of arm coordinates at a common depth, the recurrence therefore gives

    q_next_norm<=7 q_current_norm+sqrt(2)q_previous_norm+Y.

The source arms each have10 edges and11 heads. Starting with the first two pairs bounded by100(p+Y), repeated use of the still looser11 times the preceding maximum bounds every pair by100*11^10(p+Y). Summing the eleven pair norms and port norm gives

    ||q||<=C_obs(p+Y), C_obs=10^15.             (4)

This also covers phase-cell sites: their diagonal is3, hopping is sqrt(2), and no vanishing divisor occurs. Terminal equations are not needed for this upper bound; their actual onsite values2+x remain in the same bound. It is an inhomogeneous observability estimate for the specified graph, not an assumption of generic invertibility.

The imaginary part of <q,L_x q> is -sin(k)||Pq||^2. Thus sin(k)p^2<=||q||Y. With sin(k)>=1/2, (4) and Young's inequality give

    ||q||<=C_obs sqrt(2||q||Y)+C_obs Y
           <=||q||/2+(C_obs^2+C_obs)Y,
    ||q||<10^31 ||L_x q||.

The square finite matrix is therefore invertible, uniformly on K, with

    B=10^31, ||L_x^-1||<=B.                    (5)

This proves a (very loose) margin and rules out hidden local homogeneous solutions at these energies. It does not assert absence of other bound states.

Since ||L_x'||<=3 and ||L_x''||<=3, inverse differentiation gives

    ||(L_x^-1)'||<=3B^2,
    ||(L_x^-1)''||<=18B^3+3B^2.

Using the derivatives of -2i sin(k) in(3), uniformly over both record sectors,

    ||V_w||<=a0=2B,
    ||V_w'||<=a1=8B^2,
    ||S_w'||<=w1=8B^2,
    ||S_w''||<=w2=56B^3.                        (6)

The exact scattering norm is1. The two physical writers sharing R use a direct sum in head path of these same sector maps; (6) bounds their complete48-head map with no extra factor2. The record is not copied. Constants here are deliberately not useful performance estimates, but they are finite explicit bounds established without an absent-pole assumption.

## 3. Core scattering and mediator derivatives

Use the exact core boundary matrix

    V=2I-alpha(I+R_p)-beta(I+S_p),
    alpha=D0/(D0-E), beta=D0/(D1-E).

For convenient parameter dependence set

    a_1=2eta^2/lambda0^2,
    a_2=2eta^2/lambda0^2+8eta^4/lambda0^3,
    b_1=2eta^2 zeta^2/(1-3eta^2 zeta)^2,
    b_2=2eta^2 zeta^2/(1-3eta^2 zeta)^2
                        +8eta^4 zeta^3/(1-3eta^2 zeta)^3,
    v1=2(a_1+b_1), v2=2(a_2+b_2),
    l1=1+v1, l2=1+v2.

Directly differentiating alpha,beta gives their first/second derivative ceilings a_1,a_2,b_1,b_2, because |E'|,|E''|<=2j and D0-E>=D0 lambda0. Let L_c=z^-1 I-I+V. Its inverse norm is at most1/sin(k)<=2, and S_c=-I+(z^-1-z)L_c^-1. Consequently safe explicit bounds are

    ||S_c||=1,
    ||S_c'||<=c1=4+8l1,
    ||S_c''||<=c2=4+16l1+32l1^2+8l2.            (7)

These constants were derived here; no two-port or four-port cancellation constants are imported. They remain finite for the prescribed eta,zeta domain.

Let N be the four-endpoint/four-edge unoriented incidence matrix, ||N||=2. The complete four-mediator map for core incoming data is M_c=b(D-E)^-1 N^T(I+S_c). With d0=D0-3j>0,

    ||M_c||<=m0=4b/d0,
    ||M_c'||<=m1=8jb/d0^2+2b c1/d0.             (8)

The core endpoint map I+S_c has norm<=2 and derivative norm<=c1. All four mediators are included at once.

## 4. Derivatives of exact feedback and full scattering

Retain the frozen block names S_c=[[A,B_c],[C,D]] and S_w=[[a,b_w],[c_w,d_w]], with the external grouping(I,F). The cable factor P_c=z^d I has derivative norms d and d^2. Let

    K=(I-a P_c D P_c)^-1,
    k0=1/den,
    f1=w1 e+w c1+2dwe,
    f2=w2 e+w c2+2w1 c1+4d(w1 e+w c1)+4d^2we,
    k1=k0^2 f1,
    k2=2k0^3 f1^2+k0^2 f2.                     (9)

The product rule and inverse derivative identities prove ||K^(r)||<=k_r for r=0,1,2. In particular the same small-reflection den margin that makes the stationary composition valid is retained in its derivatives; it is not replaced by an unexplained inverse constant.

For a full external incoming column f=(f_I,f_F), write the internal outgoing coefficient maps as

    U=K[a P_c C, b_w],
    W=[C,0]+D P_c U.                            (10)

Thus U is the writer's outgoing cable amplitude and W is the core's outgoing cable amplitude. Row concatenation is bounded by the sum of the two block bounds (a safe overestimate). Define

    l_0=w,
    l_1=w1+wd+w c1,
    l_2=w2+wd^2+w c2+2dw1+2w1 c1+2wd c1,
    u0=k0(w+1),
    u1=k1(w+1)+k0(l_1+w1),
    u2=k2(w+1)+2k1(l_1+w1)+k0(l_2+w2),
    v0=1+e u0,
    v1c=c1+(c1+ed)u0+e u1,
    v2c=c2+(c2+2dc1+ed^2)u0+2(c1+ed)u1+e u2.

Then ||U^(r)||<=u_r, and W has bounds v0,v1c,v2c. The names v1c,v2c distinguish these from the core boundary-parameter derivative bounds v1,v2 above.

The exact external outputs are

    out_I=[A,0]+B_c P_c U,
    out_F=c_w P_c W+[0,d_w].

The sum of the two output-row norm bounds gives

    s1=c1+(c1+d)u0+u1
                         +w1+(w1+d)v0+v1c,
    s2=c2+(c2+2dc1+d^2)u0+2(c1+d)u1+u2
                  +w2+(w2+2dw1+d^2)v0+2(w1+d)v1c+v2c,
    ||S'||<=s1, ||S''||<=s2, ||S||=1.            (11)

Every derivative in the repeated-reflection inverse and both cables is paid. The estimates are full-fiber bounds and cover F incidence as well as I incidence. Extracting only the common phase phi=-iz^57 gives

    Q=phi^-1 S, ||Q||=1,
    ||Q'||<=q1=s1+57,
    ||Q''||<=q2=s2+114s1+57^2,
    ||Q-R_ideal||<=deltaS,
    R_ideal=[[0,C_p X_R],[C_p X_R,0]].           (12)

In particular the writer's O(h) scattering defect remains in deltaS; it is not recast as an eta^2 defect.

## 5. All finite head-coordinate maps

There are122 finite head vertices:8 core heads,48 writer heads,66 interior cable heads. The two cables have68 edges, not68 new head sites. The four external ray origins are included in these122 vertices (two core I and two writer F ports); the strict internal space has118 heads. Record/program labels are fibers, not additional head positions.

The following redundant finite-vertex map T_all bounds all122 coordinates including those four origins. Restriction gives the strict internal map T. Define the core incoming-map ceilings

    n0=1+u0, n1=d u0+u1,

and the writer incoming-map ceilings

    r0=1+v0, r1=d v0+v1c.

Core endpoint and mediator bounds are respectively

    E0=2n0, E1=c1 n0+2n1,
    M0=m0 n0, M1=m1 n0+m0 n1.

The complete48-head writer map has

    W0=a0 r0, W1=a1 r0+a0 r1.

At cable coordinate l=1,...,33, the exact path-vector amplitude is z^l W+z^(d-l)U. Bounding all sites of both cables conservatively gives

    C0=sqrt(66)(v0+u0),
    C1=sqrt(66)[d(v0+u0)+v1c+u1].

The common energy normalization factor1/sqrt(2pi) is not included in these coefficient maps. Summing orthogonal coordinate-group norm ceilings (rather than trying to optimize their square sum) proves

    ||T_all||,||T||<=t0=E0+M0+W0+C0,
    ||T_all'||,||T'||<=t1=E1+M1+W1+C1.           (13)

No mediator, cable, arm, terminal, junction or record sector is omitted. No internal coefficient is called a population. The constants can be huge even where scattering error is small.

## 6. Exact normalized packet and explicit tails

For any unit external/fiber input xi, any real translation ell, and g as above, define external and strict internal coordinates by

    Psi_n(t)=(2pi)^(-1/2) integral exp(iell k-itE)g(k)
                                  [z^-n I+z^n S(k)]xi dk, n>=0,
    Psi_int(t)=(2pi)^(-1/2) integral exp(iell k-itE)T(k)g(k)xi dk.

External origins are counted here only in Psi_n, not in Psi_int. The actual physical solution is exp(-ic_total t)Psi(t). Exact lead, core, writer, terminal and cable equations prove strong relative Schrödinger evolution. Fourier synthesis bounds the lead maps; (13) bounds the finite internal integral. Bounded E and smooth compact support justify differentiation under the integral.

As t tends to minus infinity, incoming half-line components approach the norm-one full-integer incoming Fourier state. Outgoing half-line components vanish by nonstationary phase, and the finite internal coordinates vanish by the estimate below. Conservation of norm therefore proves ||Psi(t)||=||xi|| at all times. Linearity and polarization give an isometry including arbitrary passive references. This constructs one normalized scattering-packet family, without proving global completeness or setting any seed bound-state component to zero.

For amplitude bounds A0,A1 and q>0 define

    Tail_A(t,q)=[A1+(2j|t|/q)A0]/sqrt(2pi)
                                     *sqrt(q^-2+q^-1).

The same single integration-by-parts and integer-tail sum as in the checked packet sources applies on K. For outgoing amplitude Qg use

    H0=G0, H1=G1+q1 G0, H2=G2+2q1 G1+q2 G0.   (14)

For all finite coordinates use J0=t0 G0, J1=t0 G1+t1 G0. If the internal phase ell k-tE has derivative magnitude at least q, then

    ||Psi_int(t)||<=Internal(t,q)
          =[J1/q+2j|t|J0/q^2]/sqrt(2pi).        (15)

The same bound controls the full122-coordinate finite-vertex restriction if desired, by using T_all. Boundary terms vanish because g is compactly supported. Equation(15) covers early t>=0 with q=ell-tv_max>0, late t with q=tv_min-ell>0, and remote past with q=ell+|t|v_min>0 when ell>=0. No denominator is assumed positive outside its stated regime.

For ell>=0, positive early time with ell-tv_max>0, compare Psi to the full-integer incoming Fourier vector on the external rays (zero strict internal coordinates). Its missing negative-coordinate tail has bound Tail_G(t,ell+1-tv_max). The outgoing term has phase -i exp(i[n+ell+57]k-itE)Qg and bound Tail_H(t,ell+57-tv_max). Therefore a safe full-vector early match is

    ||Psi(t)-A_full(t)||
       <=Tail_G(t,ell+1-tv_max)
          +Tail_H(t,ell+57-tv_max)
          +Internal(t,ell-tv_max).              (16)

This is only a comparator estimate, not a proof that an actual finite emitter seed prepares A_full.

At late t with tv_min>ell, take xi supported on the I rays. Let O_ideal be the external F outgoing vector formed with common scalar sequence

    B_n(t)=(-i)/sqrt(2pi) integral
                    exp(i[n+ell+57]k-itE)g(k)dk, n>=0,

and fiber action C_p X_R. Set every other output coordinate to zero. Parseval and (12) bound the complete outgoing spectral distortion by deltaS, while incoming and internal pieces give

    ||Psi(t)-O_ideal(t)||<=D(t),
    D(t)=Tail_G(t,tv_min-ell)+deltaS
                              +Internal(t,tv_min-ell). (17)

If D(t)<1, exact packet normalization implies ||O_ideal||>=1-D(t)>0. Positive normalization beta=B/||B|| gives

    ||Psi(t)-J_F(beta(t) tensor C_p X_R xi)||<=min{2,2D(t)}.

Record|0> becomes the common record|1> in this comparator; arbitrary record input receives X. The phase -i, shift57 and physical exp(-ic_total t) remain fixed. Wrong outgoing I components and all actual internal/record amplitudes are included in the error. For any fixed supplied parameters and smooth g with deltaS<1, the tails tend to zero at late times; this is a conditional infinite-ray packet statement, not finite-source or all-time completion.

## 7. Remaining finite-source and completion obligations

A finite I-emitter/F-cut construction must still choose its actual positive cap/source blocks and diagonal conventions; prove a complete early seed-to-packet comparison with the new core/writer strength and distance; account for all localized spectral components through that comparison; integrate actual finite-edge perturbations using (14) or sharper derivatives; and prove final positive normalization and vacancy of every apparatus coordinate throughout a stated window. The enormous fixed writer margin here proves finiteness only and is not an optimized runtime/resource certificate. No old central-band constants or finite-device exponent are transferred.

The shared record can already rotate during an internal terminal visit and can toggle again after a return. Even a later finite-window record-output theorem would not prove an all-time heralded completion implication, stationary output, irreversible latch, capture/reset or permanent halt. Native Record identification, blank initialization/readout and the local interaction/coefficient supplier remain additional physical premises.

## 8. Sources and exposure

Primary composition: common_product_stage_record_core/PROPOSAL.md, c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729, authored/full-read in the immediately preceding task and conditional pending its distinct check. The complete actual writer sources93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56 and reviewc5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a, and core60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182/review8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d were fully read and hash-verified at that task. Their identities and scopes are unchanged. No old interacting closed-channel or runtime theorem is imported.

ROOT requested this derivative/internal-tail interface. This author previously authored the composition and several launch/packet-interface notes. The writer observability bound, derivative chain and full internal inventory above are newly authored, source-exposed work requiring a distinct check. Particular obligations for that check are the recurrence constants, outgoing boundary sign, all inverse/product derivatives, doubled-versus-shared record accounting, strict internal/lead-origin partition, source translation and phase57, normalization and all positivity conditions on tail denominators.

Only common_product_stage_record_packet/PROPOSAL.md was created. No scientific executable, numerical solver/simulation, sweep, source/W/Git/publication/checkpoint/editable-prompt/model change or delegation occurred. No retained status or independent acceptance is assigned.
