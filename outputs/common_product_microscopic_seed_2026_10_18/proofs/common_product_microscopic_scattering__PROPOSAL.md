# Exact microscopic two-port scattering and its remaining packet obligations

New authored bounded derivation requiring a distinct check. For the exact supplied microscopic cell with infinite uniform leads, eliminating its scalar mediator gives a unitary on-shell scattering matrix whose central-band discrepancy from the ideal router is bounded by constants times eta^2 and zeta, without an elapsed-time factor. This is a scattering-column result. It does not yet replace the full-time cell bound in the finite seeded device or establish a new runtime exponent.

ROOT proposed the Robin-channel elimination formula and the possible use of this route to avoid accumulated Duhamel cost. Those suggestions are exposure, not evidence. The signs, channel decomposition, bounds and point-spectrum statements below were reconstructed as new author work. All positive blocks, roles, coefficients, legal programs and reference/input contracts remain supplied premises.

## Exact operator and coordinates

Use the six-qubit cell of `mediated_common_product_program/PROPOSAL.md`, SHA256 `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`, with infinite outward uniform Q_j leads attached to endpoints u and v at radial n=0. The source/emitter ends of the finite composition are removed for this scattering calculation only. Let j=b^2/D0, a_0=2j, a_1=0, eta=b/D0 and zeta=D0/D1. Legal program p has mediator diagonal D=D_p and endpoint potential a=a_p after subtracting ONLY the common physical scalar 2b.

The total-one-head Hilbert space is (C^2 tensor ell^2(N_0)) directsum C_m, with the legal program and any passive reference as additional factors. The exact relative operator is

    h_p=[[K_lead+a(|L,0><L,0|+|R,0><R,0|), B],
         [B*,D]],
    B=-b(|L,0>+|R,0>).

It is bounded and self-adjoint on this one-head space. The full physical generator is 2bI+h_p and remains positive by the source's full positive-qubit decomposition and positive lead blocks. Relative h_p need not be positive. No bounded norm is asserted for an unrestricted infinite many-head sum.

## Boundary elimination and full scattering phase

Set z=exp(ik), E(k)=2j(1-cos k), 0<k<pi. Let psi_n be a two-port generalized column and m its mediator amplitude. The exact endpoint and mediator equations are

    E psi_0=(j+a)psi_0-j psi_1-b m (1,1)^T,
    (D-E)m=b(psi_L,0+psi_R,0).                     (1)

For E!=D, resolve the port projectors P_+=(I+X)/2 and P_-=(I-X)/2. Eliminating m gives the scalar boundary relation in each channel

    E psi_0=j(1+v)psi_0-j psi_1,
    v_+(E)=a/j-2b^2/[j(D-E)],
    v_-(E)=a/j.                                   (2)

With the same radial convention as the ideal router, psi_n=(2pi)^(-1/2)[z^-n I+z^n S_p(k)]f. Substituting one channel psi_n=z^-n+s z^n into (2) gives

    (1-v-z)+s(1-v-z^-1)=0,
    s(v;k)=(1-v-z)/(z^-1-1+v).                    (3)

Thus the exact on-shell port matrix is

    S_p(k)=s(v_+(E(k));k)P_+ + s(v_-(E(k));k)P_-.  (4)

The numerator and denominator of (3) have opposite real parts and the same imaginary part for real v. They therefore have equal magnitudes. The denominator is nonzero in the open band because its imaginary part is -sin k. Each channel has unit modulus and S_p is unitary; it is also symmetric in the two ports. This verifies flux conservation with the identical lead velocities and does not by itself prove completeness or normalization of a generalized spectral transform.

For v=0, (3) gives s=z; for v=2 it gives s=-z. The exact channels are consequently

    enabled p=0:
       v_+=2-2D0/(D0-E)=-2E/(D0-E),
       v_-=2, s_-=-z;
    disabled p=1:
       v_+=-2D0/(D1-E),
       v_-=0, s_-=z.                              (5)

The ideal S_0=zX and S_1=zI have symmetric-channel value z in both programs. Only the symmetric channel differs. The common momentum-dependent phase z is retained, not fitted away. Incoming/outgoing direction follows from E'=2j sin k>0 exactly as in the source ideal router.

The mediator amplitude with this incoming convention is explicitly

    m_p(k;f)=(2pi)^(-1/2) b/(D-E)
                  (1,1)(I+S_p(k))f
             =(2pi)^(-1/2) sqrt(2)b/(D-E)
                     [1+s(v_+;k)] f_+,             (6)

where f_+=<+|f>. Antisymmetric input has zero mediator amplitude. Equation (3) also yields

    1+s=(z^-1-z)/(z^-1-1+v).

This supplies the amplitude and its phase, not only a mediator population estimate.

## Uniform central-band scattering discrepancy

Take the fixed conservative band |k-pi/2|<=pi/6, namely k in [pi/3,2pi/3], used by the finite-source cutoff construction. Then j<=E<=3j. To make the uniform denominators explicit impose eta<=1/8 and 0<zeta<1/2, a subdomain already allowed by the incident-cap construction. In particular D0>=64j and D1>D0, so there is no elimination pole anywhere in this band.

Subtracting z from (3), without discarding the momentum phase, gives

    s(v;k)-z=-v(1+z)/(z^-1-1+v).

Since the denominator's modulus is at least sin k and |1+z|/sin k=1/sin(k/2)<=2 on the band,

    |s(v;k)-z|<=2|v|.                             (7)

Equations (5),(7) give the exact useful bounds

    ||S_0(k)-zX||<=12eta^2/(1-3eta^2)<=13eta^2,
    ||S_1(k)-zI||<=4zeta/(1-3eta^2 zeta)<=5zeta.    (8)

For example 12/(1-3/64)=768/61<13, while 4/(1-3/128)=512/125<5. The controlled legal-program matrix therefore satisfies

    ||S(k)-zC||<=max{13eta^2,5zeta}
                       <=13eta^2+5zeta,            (9)

uniformly on this band, with arbitrary passive-reference tensor factors. This estimate has no elapsed time. For normalized band-supported spectral data, it bounds the L2 norm of the difference of outgoing spectral columns by the same constant, since multiplication by S-zC has that essential-supremum norm. Interpreting those spectral columns as complete physical normalized outputs requires the additional packet work below.

By |1+s|<=2, (6) also gives

    |m_p(k;f)|<= (2pi)^(-1/2)
          [2sqrt(2)eta/(1-3eta^2)] |f_+|.          (10)

For the disabled branch the smaller ratio b/D1 can be retained, but (10) is a valid common bound. The generalized mediator coefficient is of order eta, rather than eta^2. It cannot simply be omitted when turning (9) into a full-output claim. A wavepacket mediator amplitude is an oscillatory integral of (6); time separation may suppress it, but that suppression is not proved here.

## Actual point spectrum: it is not absent

There is an exact decoupled antisymmetric channel, a half-line with boundary v=2 in the enabled sector and v=0 in the disabled sector. The known half-integer sine/cosine representations from the ideal-router source give continuous spectrum [0,4j] and no square-summable eigenvector in that channel.

The symmetric channel consists of a half-line operator A_sym=K_half+a|0><0| coupled with coefficient -sqrt(2)b to the mediator D. A_sym is positive and has norm <=4j: its endpoint diagonal is 3j enabled or j disabled, and its absolute row sums are at most 4j. Its spectral interval and absence of point spectrum also follow from the same v=2 or v=0 half-integer representations before attaching the mediator.

For E>4j, the scalar Schur equation is

    F(E)=D-E+2b^2 <0|(E-A_sym)^-1|0>=0.

F is strictly decreasing because F'(E)=-1-2b^2<0|(E-A_sym)^-2|0><0. It is positive for 4j<E<=D, positive at D, and tends to minus infinity. Thus there is exactly one symmetric bound eigenvalue above D in each legal program. The high mediator mode is a genuine omitted spectral channel, not an algebraic approximation to a propagating column.

At negative energy the quadratic-form Schur complement at zero classifies negative directions because D>0. In the enabled sector A_sym-2b^2|0><0|/D0=K_half>=0, so the full relative operator has no negative eigenvalue. In the disabled sector the complement is K_half-2b^2|0><0|/D1, a rank-one attractive perturbation, hence it has at most one negative direction. It has at least one: for normalized geometric x_n=sqrt(1-r^2)r^n, 0<r<1,

    <x|K_half|x>=j(1-r)^2,
    |x_0|^2=1-r^2.

The negative rank-one term dominates as r approaches 1 from below. Choosing the mediator component to minimize the quadratic form gives a negative trial value for the full operator. Its essential spectrum remains [0,4j] under this finite-rank coupling, so there is exactly one negative-energy bound eigenvalue in the disabled relative sector. This does not contradict positivity of 2bI+h_p.

An explicit out-of-band eigenvalue equation, useful for subsequent weights, follows from a decaying tail x_n=x_0 r^n, |r|<1 and real r:

    E/j=2-r-r^-1,
    (D-E)[1-r^-1-a/j]+2b^2/j=0.                  (11)

Positive r corresponds to E<0, negative r to E>4j. E=D cannot be an eigenvalue: its mediator equation forces x_0=0, then a decaying tail must vanish and the endpoint equation forces the mediator to vanish as well. Interior-band and threshold eigenvectors are also excluded by the constant-coefficient recurrence: oscillatory solutions, or threshold constant/linear solutions, are not square summable unless the tail vanishes, which forces the entire column to vanish. These observations do not constitute a full spectral-transform completeness proof or compute the bound-state weights of a finite emitter seed.

## What a finite-seed replacement would still need

The proposed improvement is real at the on-shell matrix level, but the following obligations are not discharged by (9):

1. Construct exact physical packet solutions from the lead and mediator columns, with their normalization and the coherent program/reference map established. A unitary on-shell S alone does not prove a unitary transform onto the full Hilbert space. A full spectral method must include the point spectrum just identified and justify completeness of its continuous representation.
2. Alternatively, ROOT suggested a packet-specific route: build smooth compact-band solutions of the exact Schrödinger equation, prove their norm from incoming/outgoing separation as time tends to minus infinity, and match them directly to the literal finite seeded state. If that matching pays the full vector error, it can also pay any omitted bound-state component without a separate global completeness theorem. This is an unproved proposed route here, not a requirement that bound states be absent.
3. Rebuild the actual launch-to-microscopic-packet comparison, retaining the exact source spectral phase, radial translation and normalization. The original ideal packet and its launch interface cannot simply be substituted without checking the changed columns and mediator component.
4. Control unwanted finite-time lead pieces and mediator amplitude in the complete output norm, with explicit derivative bounds or another justified mechanism. The order-eta generalized mediator coefficient in (10) is not automatically an order-eta^2 output error.
5. Match the same fixed-diagonal outer emitter/cut perturbation and pay its finite-window boundary residual for the microscopic packet, including its changed energy dependence. Any finite-device bound-state contribution or early mismatch must remain in the full state error. Point-spectrum weight is not assumed zero because the incoming continuum matrix is favorable.
6. Establish the final normalized common packet and vacancy comparator. S differs from zC, so branch-dependent packet distortions must be charged as a full coherent error, not hidden by tracing the radial degree away. Keep the physical scalar exp(-i2bt), all emitter/mediator coordinates and the whole-time seed preparation contract.
7. Only then insert a uniform complete-output estimate into a simultaneous bounded-load resource construction. Equation (9) alone supplies no new finite-router duration exponent, stationary output, permanent halt, capture/reset or old processor replacement.

Thus the existence of bound states is a concrete obligation for an initial-state comparison, not a blanket obstruction to packet-specific scattering constructions. Their absence is neither true here nor necessary if all omitted components are quantitatively paid.

## Sources, exposure and limits

The microscopic cell739e99 above and `common_product_finite_seed_router/PROPOSAL.md`, SHA256 `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`, were previously fully read and recently hash-refreshed. The ideal scattering conventions and half-integer channel bases are from `common_product_autonomous_interface/PROPOSAL.md`, SHA256 `bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5`, previously fully read and distinctly checked in this session at review90c7926e. Their exact scopes are reused; no new audit of those sources is claimed. This scattering geometry removes the source ends and is not itself the finite Hamiltonian of the composition.

ROOT supplied the candidate Robin formula and later suggested the packet-specific normalization route; both exposures are explicit. I previously checked the ideal router and authored related boundary/window/scaling extensions. The present elimination, bounds and bound-state analysis are authored work requiring a distinct check, not an independent review. No practical advantage or new runtime is claimed.

Only this proposal was created. No scientific executable, simulation, symbolic solver, sweep, upstream source edit, W/Git/canonical/publication/checkpoint/editable-prompt/model change or delegation occurred. No formal audit or retained status is assigned.
