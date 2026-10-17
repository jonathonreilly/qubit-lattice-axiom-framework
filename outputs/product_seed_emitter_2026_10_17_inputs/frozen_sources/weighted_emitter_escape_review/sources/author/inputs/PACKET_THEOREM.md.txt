---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
independent_review: pending
audit_required_before_effective_retained: true
---
# From finite-channel scattering certificates to a persistent wavepacket gate

Provisional mathematical construction, 2026-10-16. This note proves a
conditional implication for the specified half-line Hamiltonian. No concrete
two-body scattering fit, interval certificate or native apparatus is supplied
here. The separate on-shell fitting worker's results were not read or assumed.

The main estimate is

    isometry error <= Delta
      + 2(CA+CB)/sqrt(pi v T) + 3D/[sqrt(2pi) v T],           (1)

for every physical elapsed time t>=2T, with s=t-T. Delta is the certified
reflection-phase mismatch over the entire packet band. D includes the
operator-norm cost of localized and closed-channel columns that need not be
orthogonal. The proof retains the actual asymptotic input energies; it never
commutes the old K through the full interaction.

## 1. Model, target and exact certificate contract

Let the finite internal Hilbert space be old plus source, and let

    iota x = x tensor Omega,
    ||Omega||=1,
    H = h0 tensor I + I tensor B
        + |0><0| tensor V0 + |1><1| tensor V1,
    h0 = 2J I - J sum(n>=0)(|n+1><n|+|n><n+1|), J>0.        (2)

B,V0,V1 are fixed finite selfadjoint matrices. H is a bounded selfadjoint
operator on the half-line one-head Hilbert space. This is the supplied
mathematical model, not a derivation of a full-qubit implementation.

Choose an orthonormal logical basis e_j, j=1,...,m, with

    u_j=iota e_j,       B u_j=b_j u_j,
    Db=diag(b_j).                                           (3)

The old-pair application has m=4 and literal K=2I+Z1 Z2, whose eigenvalues
are 1 and 3. To express (3) as literal old aging plus a common source phase,
one must additionally certify

    B iota = iota(K+bOmega I).                              (4)

Without (4) the theorem still holds, but the aging matrix is the actual Db;
one may not replace it by K. No assertion [H,I tensor K]=0 is made.

Let Q_g be orthogonal internal projections summing to identity and commuting
with B,V0,V1. Each u_j lies in one such block, denoted g(j). Different j may
belong to the same block. All following scattering work is in that block.

Fix a common kinetic-momentum interval

    I=[k0-sigma,k0+sigma] subset (0,pi),
    E(k)=2J(1-cos k),
    0<v<=min_I E'(k),      E2>=max_I |E''(k)|.              (5)

Here v and E2 are certified lower and upper bounds, respectively.
The use of one common kinetic packet is essential to the old-independent
product preparation below. Different total energy bands are allowed:
lambda_j(k)=b_j+E(k).

For each j, the finite scattering certificate must establish all of:

1. **One open channel.** In Q_g(j), u_j is the only B eigenchannel whose
   band [b_l,b_l+4J] contains lambda_j(k), for every k in I. Every other
   channel has a positive uniform closed-channel gap g_j:

       dist(lambda_j(k),[b_l,b_l+4J]) >= g_j > 0.             (6)

   Multiplicity counts: two degenerate open eigenvectors in the same block
   violate this hypothesis. Open channels in decoupled symmetry blocks do
   not matter.
2. **Finite matching.** The unit-incoming stationary solution exists, its
   row-zero convention is fixed, and the finite system specified in section
   2 is invertible on all of I with a checked inverse-norm bound. A grid
   of nonsingular matrices alone is not this certificate.
3. **Target phases.** A desired logical unitary W is diagonal in e_j,
   W e_j=omega_j e_j, with |omega_j|=1. One common phase gamma is supplied.
   Put S=exp(i gamma)W and zeta_j=exp(i gamma)omega_j. Certify

       Delta_j >= sup_(k in I) |r_j(k)-r0(k) zeta_j|,
       r0(k)=-exp(2ik),      Delta=max_j Delta_j.             (7)

   Independent per-column choices of a “global phase” are not allowed.
   This elastic one-open-channel result covers such a diagonal phase gate;
   it does not assert an arbitrary noncommuting logical W.

For the prior target W=exp(i theta)exp(i theta X1 X2), one can choose a
common K,W eigenbasis. Whether the actual B and interactions provide the
required source-vacuum eigenvectors and reducing blocks remains a concrete
certificate, not a consequence of the target's algebra.

## 2. A finite matching certificate supplies the regularity needed

Work in a block of internal dimension d_j, with fixed orthonormal B
eigenvectors u_j and v_l for the other channels. Set

    s_jl(k)=(2J+b_l-lambda_j(k))/J,
    q_jl(k)=(s_jl-sign(s_jl)sqrt(s_jl^2-4))/2.               (8)

By (6), q is real, nonzero and |q|<1. A sufficient common bound is

    a_j=2+g_j/J,
    kappa_j=(a_j-sqrt(a_j^2-4))/2 < 1,
    |q_jl|<=kappa_j,
    |q'_jl|<=Q1_j:=2 kappa_j^2/(1-kappa_j^2).               (9)

The derivative follows by differentiating q+q^(-1)=s:
q'=2 sin(k) q^2/(1-q^2). In particular
|(q^(-1))'|<=2/(1-kappa_j^2). Branch signs cannot change on I without
violating the gap. The B eigenvectors themselves are k-independent.

Write the unnormalized unit-incoming eigenfunction as

    phi_j(k,0)=x0_j(k),       phi_j(k,1)=x1_j(k),
    phi_j(k,n)=(exp(-ikn)+r_j(k)exp(ikn))u_j
                + sum_l alpha_jl(k) q_jl(k)^(n-2) v_l,
                                    n>=2.                 (10)

The unknown vector z_j=(x0_j,x1_j,r_j,alpha_j) has dimension 3d_j. Define
D_a=2J I+B+V_a-lambda_j I on the selected block. The matching equations
are exactly

    D_0 x0 - J x1 = 0,
    -J x0 + D_1 x1 - J r exp(2ik)u_j - J sum_l alpha_l v_l
        = J exp(-2ik)u_j,
    -J x1 + J r exp(ik)u_j + J sum_l q_l^(-1) alpha_l v_l
        = -J exp(-ik)u_j.                                  (11)

The last line is the n=2 equation after inserting the bulk recurrence;
equivalently it matches the exterior solution extrapolated to site 1.
All n>=3 equations are then automatic. Thus the finite system
M_j(k)z_j(k)=d_j(k) is the actual half-line eigenfunction condition.

Suppose a certificate supplies

    inf_I sigma_min(M_j(k)) >= nu_j>0.                     (12)

Since all entries are C1, this proves C1 solutions. The right-hand side
of (11) has norm sqrt(2)J and derivative norm sqrt(5)J. A sufficient
derivative bound for the matrix is

    LM_j=J sqrt[9+4/(1-kappa_j^2)^2],
    ||M'_j||<=LM_j.                                        (13)

To check (13), split the input vector into (x0,x1), r and alpha. Their
derivative images have norms at most 2J, sqrt(5)J and
2J/(1-kappa_j^2), respectively, times the corresponding input norm.
Cauchy–Schwarz over these three groups gives (13).

Consequently one may use

    X0_j=sqrt(2)J/nu_j,
    X1_j=[sqrt(5)J+LM_j X0_j]/nu_j,
    sup_I ||z_j||<=X0_j,    sup_I ||z'_j||<=X1_j.           (14)

Sharper directly certified bounds are welcome. With no closed channels,
delete the alpha terms, take LM_j=3J, and delete closed-tail terms below.

Selfadjointness supplies |r_j(k)|=1, rather than a fitted normalization.
For a stationary solution the current
2J Im<phi(n),phi(n+1)> is independent of n. The absent n=-1 bond makes
it zero at the entrance. At n>=2, orthogonality of B eigenchannels and
real q make every closed-channel current zero. The open-channel current
is 2J sin(k)(|r_j|^2-1), proving the claim. Thus

    Lj:=X1_j  is a sufficient bound on sup_I |r'_j|.         (15)

This derivation uses exact selfadjoint matrices. Approximate non-Hermitian
matching data require their own residual-to-exact-solution certificate.

## 3. Localized corrections, including the entire source output

Define c_j(k,n) by subtracting the open wave at **all** sites:

    c_j(k,n)=phi_j(k,n)-(exp(-ikn)+r_j(k)exp(ikn))u_j,
    C_j(k)=(c_j(k,n))_(n>=0).                               (16)

C_j lies in l2(N0) tensor Q_g(j). It includes both finite interaction
amplitudes at n=0,1 and all closed-channel tails. It is not a traced-out
or ignored source component. The matching certificate gives the following
explicit sufficient Hilbert-space C1 bounds:

    C0_j = sqrt[2(X0_j+2)^2+X0_j^2/(1-kappa_j^2)],

    C1_j = sqrt[(2X1_j)^2+(2X1_j+2)^2]
         + X1_j/sqrt(1-kappa_j^2)
         + X0_j Q1_j sqrt[(1+kappa_j^2)/(1-kappa_j^2)^3],

    sup_I ||C_j(k)||<=C0_j,
    sup_I ||C'_j(k)||<=C1_j.                               (17)

For the first two coordinates, use |r|=1, |r'|<=X1 and the derivatives
of exp(+-ik). For the tail, orthonormality of v_l gives
sum_(m>=0)|q_l|^(2m)=1/(1-q_l^2). Differentiating the tail produces
alpha'_l q_l^m plus alpha_l m q_l^(m-1)q'_l; use

    sum_(m>=1) m^2 kappa^(2m-2)=(1+kappa^2)/(1-kappa^2)^3.

These uniformly convergent square sums also justify differentiating in
the l2 norm, not only coordinatewise. No bound-state completeness claim
is needed. When a gap closes or nu_j approaches zero, these bounds may
become arbitrarily costly; a successful central fit does not bound them.

## 4. Packet constants and nonorthogonal columns

Choose f in W^(1,1)_0(I), ||f||_2=1, and write F0=||f||_1,
F1=||f'||_1. One explicit choice is the parabolic packet

    f(k)=sqrt(15)/(4sqrt(sigma)) [1-((k-k0)/sigma)^2]
               on I, and zero outside,
    F0=sqrt(15sigma)/3,     F1=sqrt(15)/(2sqrt(sigma)).       (18)

The interval is inside (0,pi), so v>0. The central choice k0=pi/2,
sigma<=pi/6 permits v=sqrt(3)J and E2<=2J.

Use the finite constants

    CA=F1+(E2/v)F0,
    CB=max_j [F1+(Lj+E2/v)F0],
    Dj=F1 C0_j+F0 C1_j+(E2/v)F0 C0_j,
    D=max_g sqrt(sum_(j:g(j)=g) Dj^2).                      (19)

The universally safe alternative is D=sqrt(sum_j Dj^2). The grouped
version uses only the exactly reducing Q_g. Within a group the error
columns are not assumed orthogonal. In particular D<=sqrt(m)max_j Dj,
but replacing D by max_j Dj without an additional orthogonality certificate
is unjustified.

Define vectors and column maps, with all clock sums over n>=0,

    a_s(n)=1/sqrt(2pi) integral_I f(k)exp(-ikn-iE(k)s) dk,
    b_s^j(n)=1/sqrt(2pi) integral_I f(k)r_j(k)exp(ikn-iE(k)s) dk,
    ell_j(s)=1/sqrt(2pi) integral_I f(k)C_j(k)exp(-iE(k)s) dk,
    Gamma_s e_j=(a_s+b_s^j) tensor u_j + ell_j(s).           (20)

For u>0 with vu>=1, integration by parts and the square-sum bound
sum_(n>=0)(n+vu)^(-2)<=2/(vu) give

    ||a_u|| <= CA/sqrt(pi v u),
    max_j ||b_-u^j|| <= CB/sqrt(pi v u).                    (21)

The endpoint terms vanish because f does. The phase derivative of
kn+E(k)u is at least n+vu, and its second derivative is bounded by E2 u.

For the localized component, integration by parts in the Hilbert-space
integral, using phase E(k)s, gives for s!=0

    ||ell_j(s)|| <= Dj/[sqrt(2pi) v |s|],
    ||L_s|| <= D/[sqrt(2pi) v |s|],
    L_s e_j=ell_j(s).                                      (22)

Here the derivative of 1/E' contributes E2/v inside Dj. The factor
outside is 1/(v|s|), not 1/sqrt(v|s|). The second inequality follows from
the Hilbert–Schmidt bound within each column group and orthogonality
between distinct Q_g output groups.

In contrast, the open outgoing map e_j -> b_s^j tensor u_j has exactly
orthogonal columns because the u_j are orthonormal. Its operator norm is
max_j||b_s^j||. These different treatments are intentional.

## 5. Exact normalized packet dynamics without commuting K

Put

    Psi_s=Gamma_s exp(-is Db).                             (23)

Every column is an integral of the stationary eigenfunction phi_j(k)
at its actual energy E(k)+b_j. The open-wave synthesis maps are bounded
Fourier restrictions. The localized synthesis is bounded by the Bochner
integral estimate with C0_j. Energies are bounded on I. Therefore Psi_s
is norm differentiable and satisfies i d_s Psi_s=H Psi_s strongly.
Bounded selfadjoint evolution gives

    Psi_s=exp[-i(s-r)H]Psi_r.                              (24)

On the full integer line, Parseval gives ||a_-T||=1. Its negative-site
part tends to zero by the same nonstationary phase estimate, with n=-m.
Thus its half-line norm A_T tends to one. Equations (21)–(22) show
Gamma_-T minus the map e_j -> a_-T tensor u_j tends to zero in operator
norm. Hence

    ||Gamma_-T^* Gamma_-T-I|| -> 0.

The Gram matrix Psi_s^*Psi_s is constant by (24). Conjugating the last
display by exp(iT Db) does not change its distance to identity. It follows
that

    Psi_s^*Psi_s=Gamma_s^*Gamma_s=I  for every real s.       (25)

This proves the required normalized isometries without claiming continuum
completeness or absence of bound states.

Most importantly, (23)–(24) give the exact column identity

    exp[-i(T+s)H] Gamma_-T
       = Gamma_s exp[-i(T+s)Db].                           (26)

This is an incoming-channel intertwining identity. It is not the generally
false factorization of exp(-itH) into exp(-itB) times an interaction
propagator with unchanged coefficients. No commutator of K with V0,V1
has been set to zero.

## 6. Common preparation and complete-output theorem

Choose T with vT>=1 and define

    delta_in(T)=CB/sqrt(pi v T)+D/[sqrt(2pi) v T].           (27)

Assume delta_in(T)<=1/4 and CA/sqrt(pi v T)<=1/4. Let

    A_T=||a_-T||,       chi=a_-T/A_T,
    V_ready x=chi tensor iota x.                          (28)

These are common clock/source preparations, independent of the old input.
For any unit old vector, (25) and reverse triangle inequality give
|A_T-1|<=delta_in(T), so A_T>=3/4. Consequently

    ||V_ready-Gamma_-T|| <= 2 delta_in(T).                 (29)

For the common outgoing clock, use the free reflection r0=-exp(2ik):

    b_s^0(n)=1/sqrt(2pi) integral_I f(k)r0(k)exp(ikn-iE(k)s) dk,
    beta_s=b_s^0/||b_s^0||.                               (30)

The free half-line solution a_s+b_s^0 has norm exactly one by the same
past-limit normalization proof, or by the elementary sine transform.
Hence | ||b_s^0||-1 |<=||a_s||; for s>=T it has norm at least 3/4.
Normalization in (28) and (30) is positive real. The entire Fourier and
free reflection phase is retained in beta_s.

By Parseval on the full integer line, followed by half-line restriction,

    ||b_s^j-zeta_j b_s^0|| <= Delta_j.                     (31)

The corresponding output columns lie in orthogonal u_j channels. Therefore
their aggregate operator error is bounded by Delta, with no sqrt(m) factor.
Combining (20)–(22), (30) and (31) gives

    ||Gamma_s - [x -> beta_s tensor iota Sx]||
       <= 2CA/sqrt(pi v s)+D/[sqrt(2pi) v s]+Delta,
                                                        s>=T. (32)

**Conditional wavepacket theorem.** Under (2)–(19), (27)–(28), for every
physical elapsed t>=2T and s=t-T,

    ||exp(-itH)V_ready
       - [x -> beta_s tensor iota S exp(-itDb)x]||
       <= 2 delta_in(T)+2CA/sqrt(pi v s)
                      +D/[sqrt(2pi) v s]+Delta
       <= Delta+2(CA+CB)/sqrt(pi v T)+3D/[sqrt(2pi) v T].    (33)

Proof: propagate (29) under the same H, use (26), then use (32).
Multiplication on the input by exp(-itDb) preserves operator norm. All
source and clock components remain in the comparison. This proves (1).

When (4) holds and e_j is the K,W eigenbasis, the comparator is exactly

    x -> exp(i gamma) exp(-it bOmega)
          beta_(t-T) tensor iota exp(-itK)W x.             (34)

Thus the old generator ages for the full physical time t, and both the
common fitted phase and source-vacuum dynamical scalar remain explicit.
Transient old/source mixing is included in L_s, not prohibited.

Tensoring any passive reference leaves (33) unchanged. For every normal
old/reference density, the unhalved trace-norm distance of the complete
old/source/clock/reference outputs is at most twice the right side of (33),
capped at 2. This follows by inserting the two isometries into the density
and splitting their difference into two terms. No partial trace is used.

An explicit sufficient choice for an escape contribution <=epsilon_e,
0<epsilon_e<=1, with fixed f and certificates, is

    T >= max{1/v,
       16(CA+CB)^2/(pi v epsilon_e^2),
       6D/[sqrt(2pi) v epsilon_e],
       64 CB^2/(pi v),
       8D/[sqrt(2pi) v]}.                                 (35)

The last two terms ensure delta_in<=1/4; the second term also ensures
CA/sqrt(pi v T)<=epsilon_e/4. The two travel-time terms in (1) then sum
to at most epsilon_e. If D=0, its two time constraints are zero.

## 7. Bound states and the actual prepared input

The exact packets are orthogonal to every normal bound eigenvector of H.
Indeed Gamma_-T converges weakly to zero: for each fixed clock coordinate,
the incoming phase -kn+E(k)T is nonstationary for all sufficiently large T;
the reflected and localized parts tend to zero in norm. Bounded norms then
extend this to every l2 test vector. The same holds columnwise for Psi_-T.
For a bound eigenvector v with energy lambda, (24) says the magnitude of
<v,Psi_-T e_j> is independent of T, so it must be zero. No completeness
assertion about the complementary spectrum is used.

Let Ppp be the point-spectral projection of the infinite half-line H.
The physically prepared input can have nonzero bound-state amplitude, but

    ||Ppp V_ready|| <= 2 delta_in(T).                      (36)

It remains bounded by the same number at every elapsed time because Ppp
commutes with exp(-itH). This residual is already included in (29) and
(33); it must not be silently removed or counted as a new independent
error. Other physical-input components outside the exact packet family
are likewise covered by (29). For a finite chain its entire spectrum is
point spectrum; (36) is a statement about the infinite apparatus only.

## 8. What an on-shell fit does and does not certify

Suppose the separate fit certifies at k0, using the same common gamma,

    |r_j(k0)/r0(k0)-zeta_j|<=delta0_j.                     (37)

With the interval regularity certificate (15), one may choose the certified
band-mismatch bound

    Delta = max_j [delta0_j+(Lj+2)sigma].                  (38)

Here 2 is |r0'|. Equation (38), the gap (6), the inverse bound (12), and
the actual input-energy identity (3)/(4) are separate requirements. A
central fit alone proves none of the three others. In particular it does
not bound the long-lived localized packet near a matching resonance.

Shrinking sigma can reduce the variation term while increasing F1 and the
required travel time. A positive certified upper bound delta0_j leaves
that term in the guaranteed accuracy; it is not itself a theorem that the
physical optimum has a nonzero error floor. Arbitrary accuracy for a fixed
Hamiltonian would require, for example, an exact central phase match and
fixed positive gap/inverse certificates on a neighborhood of k0. Under
those additional certificates, narrowing the packet and increasing T does
give arbitrary accuracy. No such concrete exact-fit certificate, or
uniform family of fitted hardware, is supplied in this note.

## 9. Explicit finite-support product readiness

The incoming packet is the same scalar vector for every old/source column,
so a finite-support truncation remains an independent product preparation.
For n>2JT, integration by parts in -kn+E(k)T gives

    |a_-T(n)| <= [F1/(n-2JT)+2JT F0/(n-2JT)^2]/sqrt(2pi).

For d=N-2JT>=max(1,2JT), its tail therefore obeys

    ||1_(n>=N) a_-T|| <= (F1+F0)/sqrt(pi d).                (39)

For 0<eta_p<=1/2, take

    N=ceil[2JT+max{1,2JT,16(F1+F0)^2/(pi eta_p^2)}],
    chi_N=1_(0<=n<N)a_-T / ||1_(0<=n<N)a_-T||.             (40)

The discarded norm is <=eta_p/4. Since A_T>=3/4, normalizing the
orthogonal truncation costs at most 2 times the discarded norm divided
by A_T, hence ||chi_N-chi||<=eta_p. Its retained norm is at least 5/8.
The infinite-clock bound (33) increases by at most eta_p, uniformly for
all t>=2T; the bound-state amplitude (36) also increases by at most eta_p.

Formula (40) specifies finitely many one-dimensional integrals. It does
not assert exact finite-machine emission or a native preparation algorithm.
A separately certified preparation-isometry error eta_a adds at most eta_a
to every displayed vector bound. The complete source remains Omega at
preparation and in the comparator; actual source excitation is included
in the output error.

## 10. Finite clock through an explicit horizon, without a K commutator

Let M>=max(N,2), retain sites 0,...,M-1, and use the compression H_M of H:
the scalar clock diagonal stays 2J at both endpoints. In a positive clock
bond representation this entails the usual added J n_(M-1) term. No other
full-qubit positivity or locality statement is inferred here.

Let bmin,bmax bound the spectrum of B and set

    Vmax=max(||V0||,||V1||),
    c=(bmin+bmax+4J)/2,
    rho=2J+(bmax-bmin)/2+Vmax.                              (41)

The perturbations at clock0 and clock1 have disjoint clock support, so
their sum has norm Vmax. Both H and H_M have spectrum inside
[bmin-Vmax,bmax+4J+Vmax]. Thus (H-cI)/rho and (H_M-cI)/rho are
selfadjoint contractions. This estimate uses the **full internal B and
interactions**, not an invalid factorization through old K.

An input supported on clock0,...,N-1 cannot reach the first omitted site M
in fewer than d_M=M-N+1 hops. Internal matrices and diagonal shifts do not
move clock support. Therefore degree k<d_M polynomials in these contractions
agree on the input after embedding the finite clock in the half-line.
The Chebyshev expansion of the exponential and the Bessel generating
function contour |z|=exp(mu) give, for mu>0,

    ||exp(-itH)V_N - embed exp(-itH_M)V_N||
      <=4 sum_(k>=d_M)|J_k(rho t)|
      <=4 exp[-mu d_M+rho t sinh(mu)]/[1-exp(-mu)], t>=0,   (42)

where V_N x=chi_N tensor iota x. The expansion contributes a factor 2,
and the difference of two contraction images contributes the other factor
2. The contour bound is |J_k(x)|<=exp[-mu k+x sinh(mu)] for x>=0.
This argument applies directly to the complete input isometry and any
passive reference. It does not assume old K is conserved.

For an observation horizon Tobs>=2T and tolerance zeta>0, it suffices that

    M>=max(N,2),
    M-N+1 >= [rho Tobs sinh(mu)
                +log(4/((1-exp(-mu))zeta))]/mu.            (43)

Then for every 2T<=t<=Tobs, the embedded finite output has isometry error
at most the uniform right side of (33) plus eta_p+eta_a+zeta. The complete
trace bound is twice this number, capped at 2. The common target is the
half-line beta_(t-T) with the scalar and aging in (34), or the actual Db
comparator when (4) has not been certified. This is an explicitly embedded
distance; it does not say a finite device contains the omitted output sites.
A fixed finite M is covered only through its stated horizon.

## 11. Distinct finite algebra check: column errors can align

The companion `column_norm_check.py` uses exact two-dimensional matrices:

    K=diag(1,3),       P=ones(2,2)/2,
    z=3/5+4i/5,       U=I+(z-1)P.

U and I are both isometries, but their error E=U-I satisfies

    E*E=(2/5)ones(2,2),
    max_j ||E e_j||^2=2/5,    ||E||^2=4/5.

Thus orthogonal actual and comparator columns do not make their error
columns orthogonal. The sum-of-column-squares operator bound is sharp in
this example. Also [K,P]!=0. This exact check resolves the specific risk
of replacing D by a maximum merely because the incident old states are
orthogonal. It is not a scattering fit or a certificate for (6), (12) or
(37). The full output and execution/source identities are in
`check_stdout.txt` and `CHECK_EXECUTION.json`. The calculation uses SymPy
exact arithmetic, dimension 2, a 10 CPU-second and 30 wall-second cap.

## 12. Provenance, status and next certificates

The one-channel prior context is the frozen boundary-reflection
`CANDIDATE_V2.md`, SHA256
`694484853b731991d97f11f5d9a3a012ff30b9badb7fe57a7c57f6fee7e2fd36`,
and `FINITE_READINESS_ADDENDUM.md`, SHA256
`ce01691b49abf924d2fc610cf2dd6c71c565c0c21df6f1bc39960ecb2c546a2f`.
Their methods supply context, not the new multi-channel certificates.
The present proof rederives the needed normalization and tail estimates,
adds closed-channel/interaction-site decay, and uses (26) to replace the
old global commutation argument. Standard tools used with their hypotheses
shown are Fourier Parseval, integration by parts, bounded selfadjoint
evolution, finite matrix inversion, and the explicit Chebyshev/Bessel
expansion. No framework primitive or observed physical value is used as a
hidden premise. The supplied Hamiltonian and preparations are conditional
model assumptions; no new framework axiom is proposed.

Scope of prior search: a local textual search in the current correlation
worktree docs for nearby combinations of scattering, wavepacket and
closed-channel terms returned no matches. It was not a complete repo or
literature search; no novelty claim follows. The explicit task prohibited
Git and network calls. The procedural snapshot was the already identified
science workflow at SHA256
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`.

This is a new author derivation, separate from the earlier source-exposed
reviewer role. It has not received independent mathematical review. The
finite algebra check is an author check of a distinct load-bearing risk;
it does not independently certify the whole theorem. The result supplies
a conditional analytic bridge for a future scattering certificate. It does
not promote the independently pursued numerical fit or establish native
hardware, reset/reuse, a selected Record, energy-resource pricing, arbitrary
noise robustness or any actual uniform fit family.

The remaining concrete obligations for use on a fitted device are:

1. Freeze the actual B,V0,V1 and source-vacuum embedding, prove exact
   selfadjointness and reducing symmetries, and verify (3). Verify (4)
   before using literal K plus one source scalar in the comparator.
2. Certify exactly one propagating eigenchannel in each relevant block
   throughout a common kinetic interval, with explicit positive gaps (6).
3. Build the actual matching matrices (11), certify nu_j>0 over that
   interval, and obtain explicit constants (14)–(19). Near-zero matching
   singular values are a resource cost, not a negligible fit detail.
4. Certify the actual reflection convention and target phases with one
   common gamma, preserving the nonzero residuals. Supply (7) directly or
   a valid combination of (15) and (37). A finite central fit alone is
   insufficient; exact or uniform accuracy remains unestablished unless
   separately certified.
5. Choose a single f,T and finite preparation specification from the
   resulting constants. If the apparatus is finite, certify its actual
   compression/endpoint term and choose its horizon from (41)–(43).
6. Independently check this bridge before substantial downstream reliance.
   Separately establish any strict two-body full-qubit realization,
   invariant one-head subspace, native readiness or physical interpretation.

The next decision is quantitative: insert genuine interval certificates,
compute Delta and the constants, and compare the resulting accuracy and
resource bound with the actual target. No existing fit is declared to have
met these obligations.
