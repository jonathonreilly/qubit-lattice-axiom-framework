# Exact normalized microscopic packets with explicit band derivatives

New authored bridge requiring a distinct check, conditional on the exact microscopic scattering construction `common_product_microscopic_scattering/PROPOSAL.md`, SHA256 `59b59ea3fc51e6ae364716a63ff4b9e001390cba112f48f0b4214c01318865a6`, whose distinct check is pending at assignment. ROOT suggested proving packet normalization from exact Schrödinger evolution and remote-past separation, rather than imposing absence of bound states or proving a global spectral transform. That route is established for the packets below. It does not establish a new finite-seed theorem or runtime bound.

## Packet definition and exact operator

Use the scattering source's bounded total-one-head relative Hamiltonian h_p, with physical generator 2bI+h_p, infinite uniform leads of strength j=b^2/D0, and legal program p. Put eta=b/D0<=1/8, 0<zeta=D0/D1<1/2. Fix the conservative central band [pi/3,2pi/3], where vmin=sqrt(3)j and vmax=2j. Let g in C_c^2((0,pi)) have support in this band and ||g||_2=1. Fix a nonnegative integer ell and a unit legal-program/path/passive-reference input xi. Set G_r=||g^(r)||_1 for r=0,1,2.

Let S_p(k) be the exact source scattering matrix and define Q_p(k)=exp(-ik)S_p(k). In the port symmetric/antisymmetric decomposition, Q_p has symmetric entry q_p and constant antisymmetric entry -1 enabled, +1 disabled. Let R_p(k) be the exact map from a port input to the mediator coordinate,

    R_p(k)=sqrt(2)b/(D_p-E(k)) [1+s_p(k)] <+|,
    E(k)=2j(1-cos k), s_p(k)=exp(ik)q_p(k).

Use controlled direct sums Q,R over legal programs, with identity on passive references. The physical generalized packet, after subtracting only the common scalar, is

    Psi_n(t)=(2pi)^(-1/2) integral [
        exp(i[(ell-n)k-tE(k)])g(k)xi
       +exp(i[(n+ell+1)k-tE(k)])Q(k)g(k)xi] dk,

    Psi_m(t)=(2pi)^(-1/2) integral
                       exp(i[ell k-tE(k)])R(k)g(k)xi dk. (1)

Both integrals use the same g and phase convention. The mediator map changes the path factor to its symmetric amplitude but preserves the legal program and reference. There is no fitted phase. The extra +1 in the outgoing exponent is the exact scattering phase already factored out of Q.

## Explicit derivatives on the fixed band

Write delta=eta^2+zeta. The symmetric Robin parameters are

    v_0=-2E/(D0-E), v_1=-2D0/(D1-E).

Because E<=3j, |E'|<=2j and |E''|<=2j, differentiation gives

    |v_0|<=7eta^2, |v_0'|<=5eta^2, |v_0''|<=6eta^2,
    |v_1|<=3zeta, |v_1'|<=5eta^2 zeta^2,
                                |v_1''|<=6eta^2 zeta^2. (2)

For example v_0'=-2D0 E'/(D0-E)^2 and v_0''=-2D0[E''/(D0-E)^2+2(E')^2/(D0-E)^3]. The disabled derivatives have the same bracket multiplied by D0 instead of D_p, giving the displayed extra powers of zeta. The denominator margins 1-3eta^2>=61/64 and 1-3eta^2zeta>=125/128 establish the constants in (2) directly. In particular, uniformly in both programs,

    |v|<=7delta, |v'|<=5delta, |v''|<=6delta,
    |v|<=2, |v'|<=1, |v''|<=1.                    (3)

Put z=exp(ik), W=1-z+vz and F=(1+z)/W. The exact formula q=1-vF follows from the source Robin ratio. Its denominator has |W|>=sin k>=sqrt(3)/2>1/2. Also |W'|<=4 and |W''|<=6, by differentiating W=z(v-1)+1 and using (3). Thus

    |F|<=4,
    |F'|<=2+32=34,
    |F''|<=2+32+48+512=594<600.

The four terms in the last bound are respectively N''/W, -2N'W'/W^2, -NW''/W^2 and 2N(W')^2/W^3, with N=1+z. It follows that

    ||Q||=1,
    ||Q'||<=260delta,
    ||Q''||<=4600delta,
    ||Q-C||<=d_S:=max{13eta^2,5zeta}.              (4)

Indeed q'=-v'F-vF' gives 20+238=258 times delta, and q'' gives 24+340+4200=4564 times delta. The last inequality is the sharper source scattering estimate, unchanged by exp(-ik). These constants are conservative but independent of j, ell, time and reference dimension. They do not become singular as eta or zeta decreases.

For the outgoing amplitude a(k)=Q(k)g(k)xi, define sufficient derivative L1 bounds

    H0=G0,
    H1=G1+260delta G0,
    H2=G2+520delta G1+4600delta G0.                (5)

The product rule and ||xi||=1 prove these without diagonalizing the reference state. Controlled direct sums require a maximum of program bounds, not their sum.

The mediator coefficient obeys

    ||R||<=3eta, ||R'||<=420eta.                   (6)

For the first bound use |1+s|<=2 and b/(D-E)<=eta/(1-3eta^2), giving 2sqrt(2)eta/(1-3eta^2)<3eta. For the derivative, |s'|<=1+260delta, b/(D-E)<2eta, and |d[b/(D-E)]/dk|<=3eta^3. Hence

    ||R'||<=sqrt(2)[6eta^3+2eta(1+260delta)]
            <=(4+780delta)eta<420eta,

since delta<33/64. Thus for the mediator integrand,

    J0=3eta G0,
    J1=3eta G1+420eta G0                          (7)

bound its L1 norm and first-derivative L1 norm. Equation (6) is a coefficient estimate, not yet a finite-time mediator output estimate.

## Exact strong evolution and normalization without completeness

The two lead integral maps are restrictions of full-integer Fourier analysis of a function on (0,pi), extended by zero to a 2pi interval. They are contractions from spectral L2 to radial ell^2. Multiplication by Q is unitary pointwise. The mediator integral is a bounded L1 functional with coefficient R bounded on the compact band. Therefore (1) defines a Hilbert-space vector for every real t.

Differentiation in t is legitimate in lead ell^2 because multiplication by E is bounded on the support and the Fourier maps are bounded; the same holds for the mediator integral by dominated differentiation. Applying the bounded h to (1), the bulk recurrence and exact endpoint/mediator equations of the scattering source give i dPsi/dt=hPsi, including the n=0 and mediator coordinates. Thus Psi(t)=exp[-i(t-s)h]Psi(s) strongly for any s,t, and its norm is constant. This argument requires no orthogonality or completeness assumption for generalized columns.

For clarity define the following scalar envelope for a vector amplitude with L1 bounds A0,A1:

    T_(A0,A1)(t,q)=[A1+(2j|t|/q)A0]/sqrt(2pi)
                                  *sqrt(q^-2+q^-1), q>0. (8)

If a half-line of phase derivatives has magnitude at least n+q and |phi''|<=2j|t|, one integration by parts and sum_(n>=0)(n+q)^-2<=q^-2+q^-1 give (8). For a single mediator integral with phase derivative magnitude at least q, the bound is

    M(t,q)=[J1/q+2j|t|J0/q^2]/sqrt(2pi).          (9)

At t=-tau, tau>0, the full-integer incoming Fourier vector has norm one by Parseval. Its missing n<0 tail has derivative gap ell+1+tau vmin, so its norm is bounded by T_(G0,G1)(-tau,ell+1+tau vmin), which tends to zero. The outgoing half-line has the same gap, with amplitude bounds H0,H1, so its norm also tends to zero. The mediator gap is ell+tau vmin, so (9) tends to zero as tau tends to infinity. The ratio tau/(ell+1+tau vmin) stays bounded; (8) decays at least as tau^-1/2 and (9) as tau^-1 for fixed parameters.

It follows that ||Psi(-tau)|| tends to one. Constancy of the exact Schrödinger norm therefore proves

    ||Psi(t)||=1 for every real t.                 (10)

The construction is linear in xi, and the argument applies to every input vector by homogeneity. Polarization then proves that xi -> Psi(t) is an isometry, including coherent legal programs, paths and arbitrary passive references. The physical packet is exp(-i2bt)Psi(t); its phase is retained.

This proof normalizes this particular incoming packet family. It does not assert that the family spans the whole physical Hilbert space, that the Hamiltonian lacks bound states, or that an arbitrary seed has zero bound-state component. Those claims are unnecessary for (10). The source's high-energy and disabled below-band states remain present.

## Quantitative early and late packet comparisons

For t>=0 with ell-tvmax>0, let A_full(t) be the normalized full-integer incoming Fourier vector with phase (ell-n)k-tE, embedded with zero mediator. Compare it with Psi(t), extended by zero to n<0. The discrepancies on negative n, nonnegative n and mediator are orthogonal coordinate sectors. Consequently

    ||A_full(t)xi-Psi(t)||
      <=sqrt{ T_(G0,G1)(t,ell+1-tvmax)^2
             +T_(H0,H1)(t,ell+1-tvmax)^2
             +M(t,ell-tvmax)^2 }.                (11)

At nonnegative n the incoming terms cancel exactly, leaving the microscopic outgoing term. The stronger mediator gap condition in (11) is explicit; the earlier ideal comparison's ell+1-tvmax>0 alone is not silently reused for that coordinate.

For late t with A_late=tvmin-ell>0, the incoming lead term has norm at most T_(G0,G1)(t,A_late), and the mediator at most M(t,A_late). Compare the outgoing term with the common ideal outgoing sequence

    B_n(t)=(2pi)^(-1/2) integral
                         exp(i[(n+ell+1)k-tE])g(k) dk,

times Cxi. By full-line Fourier contraction and ||Q-C||<=d_S, their half-line norm difference is at most d_S. Hence a sufficient full physical discrepancy from this unnormalized common outgoing comparator is

    d_packet(t)=T_(G0,G1)(t,A_late)+d_S+M(t,A_late).

If d_packet(t)<1, its norm q_B obeys q_B>=1-d_packet(t)>0 by (10). Positive normalization of that common outgoing vector costs at most a second d_packet(t). To truncate the target to ordinary sites n<=ell and exclude emitter locations M=ell+1, its discarded unnormalized outgoing norm is bounded by

    N_out(t)=T_(G0,G1)(t,2ell+2-tvmax)

when the latter gap is positive. If N_out(t)/(1-d_packet(t))<1, the normalized truncated common target is well defined and the total packet-to-target bound is

    2d_packet(t)+2N_out(t)/(1-d_packet(t)).          (12)

The target excludes the mediator and both emitter coordinates. Their actual amplitudes remain in the error. This is a comparison for the exact normalized microscopic packet, not yet for an evolved finite emitter seed. Formula (12) intentionally uses a sufficient sum rather than assuming outgoing distortions or mediator terms are orthogonal within an unnormalized target.

## Microscopic outer-contact envelope

Let t0>0, t0 vmin>2 and tf>=t0 with tf vmax<2ell-2. The fixed-diagonal contact/cut perturbation at emitter coordinate M=ell+1 acts only on the three radial coordinates ell,ell+1,ell+2 in each port. It is

    Delta=(j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2),
    d_hop=||Delta||=sqrt((j-gamma)^2+j^2),

with port sums understood, and zero on the mediator. The microscopic central cell is untouched. At those sites the incoming and outgoing phase derivative gaps are at least qi(t)=tvmin-1 and qo(t)=2ell-tvmax. With a vector amplitude having L1 derivative bounds A0,A1,A2, two integrations by parts give

    H_A(t,q)=A2/q^2+6jt A1/q^3
                         +2jt A0/q^3+12j^2t^2 A0/q^4. (13)

For the microscopic packet the incoming amplitude uses G0,G1,G2 and the outgoing amplitude uses H0,H1,H2 from (5). All derivatives of Q are therefore paid; the ideal g-only outer envelope cannot simply be reused. The lead vector at any affected radial site obeys

    ||Psi_n(t)||<= [H_G(t,qi(t))+H_H(t,qo(t))]/sqrt(2pi).

Define the explicit integrable coefficients

    A_i=G2+(12j/vmin)G1+(4j/vmin+48j^2/vmin^2)G0,
    A_o=H2+(6jtf/qo(tf))H1
                    +(2jtf/qo(tf)+12j^2tf^2/qo(tf)^2)H0.

The integrated residual is bounded by

    integral_t0^tf ||Delta Psi(t)|| dt <= E_outer,

    E_outer=sqrt(3)d_hop/sqrt(2pi) {
       (A_i/vmin)[1/qi(t0)-1/qi(tf)]
       +(A_o/vmax)[1/qo(tf)-1/qo(t0)] }.           (14)

The proof uses t/qi<=2/vmin, t<=tf, qo(t)>=qo(tf), and the elementary inverse-square integrals. The sqrt(3) counts radial sites, each already containing all internal/reference components. Delta has no mediator column, so (14) needs no additional mediator contribution. The exact microscopic evolution on the right is essential.

Ordered Duhamel then bounds exp[-i(tf-t0)(h+Delta)]Psi(t0)-Psi(tf) by E_outer, with a trivial cap 2 because (10) normalized both compared vectors. This is an auxiliary packet comparison. Psi(t0) generally has exterior components; a finite physical initial state still requires its own full-vector match. The common physical scalar cancels in the norm while remaining in the target phase.

## Remaining finite-seed obligations and scope

The new packet normalization avoids a global completeness gate but does not erase point-spectrum weight in a real seed. To obtain a finite operation, an explicit early comparison must connect the actual finite evolved emitter seed to Psi(t0), paying the difference of the exact source launch packet, the three terms in (11), source/output normalizations and all exterior tails. A full-vector match pays any point-spectrum component omitted by this packet family. Such matching is not proved by merely declaring the seed to be incoming.

The unchanged positive fixed-diagonal finite outer block must be identified with h+Delta including its exterior generator; (14) then provides a candidate residual bound. A later proof must combine that initial error, (14) and (12), check simultaneous parameter choices and physical incident loads, and derive any resource scaling separately. No new finite-seed theorem, observation-window resource exponent, permanent halt, stationary output, capture/reset or old processor replacement is asserted here.

The exact scattering source59b59ea3 is reused unchanged, conditionally at its stated scope. Its microscopic cell739e99, ideal scattering conventionbcc47793 and finite geometry3a195efc were previously fully read in this coherent work. ROOT suggested the packet-specific normalization approach and requested derivative bounds. I authored the scattering source and related boundary/window proposals, so this is author continuation with explicit exposure, not independent verification. A distinct checker should reconstruct the strong evolution argument, remote-past norm limit, Q/R derivative constants, phase margins and full-output comparisons.

Only this proposal was created. No scientific executable, numerical simulation, symbolic solver, sweep, upstream source edit, W/Git/canonical/publication/checkpoint/editable-prompt/model change or delegation occurred. No retained status or formal audit is assigned.
