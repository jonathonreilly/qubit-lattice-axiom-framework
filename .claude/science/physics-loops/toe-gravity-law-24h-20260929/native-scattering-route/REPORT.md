# Native two-pair threshold reduction with a gapped closed sector

Author discovery, 2026-09-30. Conditional supplied-model mathematics pending
independent checking. No formal PASS, audit status, Hamiltonian adoption,
condensate, tensor mode, axion selection or actual record instrument follows.

**Result.** The actual N=4 hard-core Hamiltonian admits an orthogonal
configuration-space separation which avoids assigning orthogonality to
overlapping pairs. Configurations without a perfect matching have a uniform
closed-sector gap mu. Their coupling to separated pairs passes through only
1487 connected physical configurations at total momentum zero. The exact
exterior consists of two genuine nine-component bond particles, with the
five known low-energy bands and four high internal components per pair.

This gives an explicit finite-core threshold resolvent. The core Schur matrix
at zero is strictly positive, by a decay and sum-of-squares argument below,
so a decaying zero-energy pole does not obstruct that response. Its entries
are specified by a convergent closed-sector series and finite Brillouin
integrals. They have NOT all been numerically evaluated. A corresponding
15-channel zero-energy variational scattering form is defined and controlled
below. It is genuinely relaxed: an exact original E-pair word forces a
strict reduction from the previously checked bare quartic coefficient.

The construction is for the infinite lattice, fixed N=4, fixed total
momentum K=0 and fixed mu,tau>0. It does not supply finite-energy flux
normalization, asymptotic completeness, a finite-density phase, or a
framework record/readout bridge. The finite torus is not used as a
zero-energy inverse: its pair zero modes would require a separate limiting
prescription. All coordinates in the exact jobs are infinite-lattice ones.

## 1. Actual law, bounded realization and source boundary

Read main at 9d15f404c63ff5b9d877e2bdc06ea8713493ffb4 and selected procedure
7146fe17a76de41badcaca3c3c7cac6d11eb2a00. The supplied Hamiltonian is exactly
that of the frozen native-stability and native-interaction reports, both read
completely, together with the complete independent interaction check. That
check independently reproduces all 675 quartic/number matrix entries; it
explicitly does not identify them with scattering data.

On Z^3 there is one physical M2 factor per site, b_x=|0><1|, n_x=b_x* b_x,
commuting different-site factors and empty Omega. For the eighteen-vector
set G={+/-2e_i, +/-e_i+/-e_j}, let m_x=sum_(d in G)n_(x+d). With the actual
five annihilators

    d_i(x)=b_(x+e_i)b_(x-e_i),
    Q_E1=(d_1-d_2)/sqrt2, Q_E2=(d_1+d_2-2d_3)/sqrt6,
    Q_Tij=(b_(x+e_i)-b_(x-e_i))(b_(x+e_j)-b_(x-e_j))/2,

the law is

    H=mu N-2mu sum P_E-mu sum P_T+V3+W_tau,
    V3=mu sum_x n_x binom(m_x,2),
    W_tau=tau sum_(x,k,A)(Q_A(x+e_k)-Q_A(x))*
                               (Q_A(x+e_k)-Q_A(x)).          (1)

The checked exact positive decomposition is

    H=A+mu D+W_tau,
    D=(1/2)sum_x n_x(m_x-1)(m_x-2),
    A=(2mu/3)sum_x(sum_i d_i)*(sum_i d_i)
       +(mu/4)sum_(x,i<j,a<b)(v_ij^a-v_ij^b)*(v_ij^a-v_ij^b),
    v_ij^(s,t)=st b_(x+s e_i)b_(x+t e_j).                    (2)

The Hilbert space here is l2 of unordered four-distinct-site configurations.
On it V3<=12mu. The exact two-particle norm of W_tau is <=24tau: its
symbol below is ell(q) times the collective frame with norm <=2 and ell<=12.
For any positive two-body operator with norm w, its actual hard-core N=4
lift has norm <=6w. To see this without pair bosons, condition the occupation
amplitudes on each residual two-site set. The squared norms of the resulting
two-particle conditional vectors sum to binom(4,2)||psi||^2. Apply the
two-particle bound to each vector and sum. It gives W_tau<=144tau.
Since the attractions in (1) are negative semidefinite, (2) therefore yields

                  0<=H_4<=C I,       C=16mu+144tau.          (3)

This proves a unique bounded selfadjoint realization from finite occupation
support, including its domain; an unproved many-body unbounded-operator
extension is not used. Translation decomposition gives the K=0 fiber on
translation orbits of configurations. A finite set has no nonzero translation
stabilizer. Its orbit basis has ordinary l2 normalization. Positivity and
(3) at K=0 also follow directly by translating any finite orbit vector over
larger cubes and taking its normalized quadratic-form limit. This avoids an
exceptional-fiber inference from an almost-everywhere direct-integral bound.

The native qubit carrier, common number basis, Hamiltonian, couplings, empty
reference and quantum amplitudes are supplied. The actual axiom/primitive
inventory does not select them. No bosonic commutation rule for Q is assumed.

## 2. An orthogonal open/closed configuration split

For an occupation configuration S of four sites, draw its induced G graph.
Let P select configurations with two disjoint G edges, equivalently a perfect
matching. Q=I-P is the orthogonal occupation complement, not the complement
of a nonorthogonal pair frame.

For four vertices without a perfect matching there is either an isolated
vertex, or a three-leaf star. Indeed, pick an edge ab. All other edges meet
a or b. If both a and b have outside neighbors, forbidding disjoint edges
forces the same outside neighbor, giving a triangle and an isolated fourth
vertex. Otherwise all nonisolated edges share one center. On degrees 0,1,2,3
the polynomial (d-1)(d-2)/2 is respectively 1,0,0,1. Hence

                     Q D Q>=Q,       Q H Q>=mu Q.            (4)

Root independently reconstructed this classification and a separate 64-graph
control before reading this route's proof/code. Its selective check covers
(4), not the rest of this report. The author enumeration finds 27 such
graphs: twenty have D=1, six D=2 and one D=4.

Every offdiagonal term in (1) removes a G pair and creates a G pair, with
the possible one-step center shift in W. In a P configuration consisting
of two disconnected G edges, any removable edge is one of those two.
The other remains a G edge. A nonzero hard-core creation therefore leaves
a perfect matching. It follows that QHP has input support only on connected
four-site G configurations admitting a perfect matching. Their translation
classes form the finite physical core C0. Exhaustive connected-set growth
gives 1647 connected four-site shapes, of which **1487** belong to C0.
The growth is exhaustive because a connected finite graph can be built by
adding one neighbor at a time; translation canonicalization only removes
duplicate shapes.

This gap handles breakup and rearrangement collectively. A separated single
particle costs mu, ordinary pair breakup costs 2mu, and possible three-body
binding is not assumed absent. Every discarded N=4 configuration still obeys
the stronger direct compression bound (4). In particular no unknown trimer
threshold is inserted into a denominator.

## 3. Actual orthonormal bond channels and all low-energy pockets

Before taking the collective frame, use these nine orthonormal physical
two-site bond types with integer anchors x:

    axial i:       {x-e_i,x+e_i},                   i=1,2,3;
    diagonal ij,eta:{x,x+e_i+eta e_j},             i<j, eta=+/-1.

Fourier states use V^(-1/2)sum_x exp(iq.x)|type,x> on a torus, and normalized
Brillouin measure dq/(2pi)^3 in the infinite-lattice transform. In this
orthonormal nine-dimensional cell, let P_E be the traceless projector on the
three axial types. For each ij the two diagonal entries of v_ij(q) are

    v_(ij,eta)(q)=-(eta/2)[exp(i eta q_j)+exp(i q_i)].

Different planes and the axial block are disjoint. Thus
||v_ij(q)||^2=S_ij(q)=1+cos q_i cos q_j and the exact pair symbol is

    h2(q)=2mu I_9 +(tau ell(q)-2mu)P_E
                    +(tau ell(q)-mu)sum_(i<j)v_ij(q)v_ij(q)*,
    ell(q)=2sum_i(1-cos q_i).                                (5)

This includes four high internal components, generically at 2mu. At a null
T Gram vector there is no T state; its missing direction joins the high
subspace. No division by S is made at those points. The five non-null bands
are exactly

    epsilon_E=tau ell,
    epsilon_Tij=mu(2-S_ij)+tau ell S_ij.                      (6)

For S in [0,2], the second expression is at least
2min(mu,tau ell). Therefore on the complete nine-component cell

    h2(q)>=a ell(q) I_9,          a=min(tau,mu/6)>0.           (7)

All zero pockets are consequently at q=0. In particular the old pi,pi
pockets at tau=0 are not silently discarded; at positive tau they have
positive energy (16tau at (pi,pi,0) in the corresponding T plane).
Near zero the E mass form is tau|q|^2 and the T form is
(mu/2)(q_i^2+q_j^2)+2tau|q|^2. All are nondegenerate quadratic forms.
The source one-pair continuum outside the G bonds is flat at 2mu.

At K=0 the separated-pair reference has symbol

          h0(q)=h2(q) tensor I+I tensor h2(-q)>=2a ell(q)I.   (8)

Use the exchange-symmetric subspace of two copies of the actual bond space.
This exchange sign comes from the commuting site creators of two separated
clusters; it is a tensor-product channel construction, not a pair-operator
commutator. Ordered coordinates (r,alpha,beta) have the exchange involution
(r,alpha,beta)->(-r,beta,alpha), with the usual normalized orbit basis.
There are 25 ordered products of the five low bands; exchange relates their
momenta and indices. The constant threshold internal space is Sym^2 C^5,
dimension 15, not a claim that all odd-relative or angular channels vanish.
At q=0 the normalized internal vectors are E1,E2 and T12/sqrt2,T13/sqrt2,
T23/sqrt2. That factor sqrt2 is the actual pair Gram.

## 4. Exact finite collision core and the exterior resolvent

Delete from the free two-bond reference every coordinate where the physical
bonds overlap or any G edge joins their endpoints. Call this finite hole I.
Each endpoint is within sup-distance one of its anchor, so a cross G edge
requires ||r||_infty<=4. The exact enumeration finds 3543 ordered hole
indices; nine are fixed under exchange (identical bonds), giving 1776
exchange-symmetric hole coordinates. This auxiliary hole is NOT the physical
core: multiple matchings and overlaps must not be counted as physical states.

Outside I, each four-site configuration has exactly two disconnected G edges
and a unique matching. The normalized symmetric bond basis is therefore
unitarily identified with the physical P exterior. On it the actual
Hamiltonian equals the Dirichlet compression L=chi h0 chi. Actual virtual
couplings and multiple-match interference remain in the physical core.
There is no Q-to-exterior coupling by the argument after (4). Consequently
the literal fiber has the exact block form

             [ A0   B*   C0* ]
    H_4(0) = [ B    DQ   0  ],       DQ>=mu,                 (9)
             [ C0   0    L  ]

on core (1487 dimensions), Q, and separated-pair exterior. Here A0 is a
physical occupation compression, B=QH|core and C0=exterior H|core. The symbol
C0 denotes the coupling in (9), not the earlier set of core configurations.
All columns of B and C0 have finite occupation support. The complete author
core action contains 143672 nonzero mu/tau coefficient pairs, reaches 25645
Q boundary shapes and 8298 exterior boundary shapes, and has maximum
coordinate span seven. These are sparse counts, not a dense matrix inverse.

For real z<0 the exact core resolvent is

    core(H-z)^(-1)core = S(z)^(-1),
    S(z)=A0-z-B*(DQ-z)^(-1)B-C0*(L-z)^(-1)C0.                (10)

The closed-sector inverse is explicit with a uniform tail for any z<mu:

    (DQ-z)^(-1)=(C-z)^(-1)sum_(n>=0)[(C-DQ)/(C-z)]^n,
    remainder after n=m <= (mu-z)^(-1)
                              [(C-mu)/(C-z)]^(m+1).         (11)

Multiply this bound by ||B||^2 (safely <=C^2) for the self-energy error.
Each coefficient acting on the finite B boundary is a finite sparse word
calculation. Formula (11) supplies an existence/error algorithm, not a
promise that high orders fit the two small jobs' memory budgets.

The exterior threshold inverse is also explicit. For the free reference set

    G0(r)=integral_BZ exp(iq.r) h0(q)^(-1) dq/(2pi)^3.         (12)

Equation (7) and ell(q)>=4|q|^2/pi^2 imply matrix integrability at q=0.
For example its diagonal norm is <=sqrt(3)pi/(16a), using a ball enclosing
the Brillouin cube. No assertion of a continuum 1/r prefactor is needed.
The matrix integrand is L1, hence every entry of G0(r) tends to zero at
infinite separation, by approximation by trigonometric polynomials.

Let GII be the finite compression of G0 to the symmetric hole coordinates.
It is strictly positive: any nonzero finite-support vector has nonzero
Fourier transform on a set of positive measure, and h0(q)>0 almost everywhere.
The Dirichlet identity, first at z<0 and then by the finite limits, gives

    GL(0)=chi [G0-G0 I GII^(-1) I G0] chi.                  (13)

All compact-source entries are finite, and their kernels decay in the
exterior coordinate. This establishes the threshold limit used in (10),
including high bond components and the exact collision hole.
At threshold G0, GL(0) and the full G_H(0) below are kernels/quadratic forms
on compact sources, not bounded inverses on the entire l2 space.

The finite integrals are effectively controllable for computable positive
mu,tau. The omitted ball of radius eta contributes O(eta) with the explicit
bound in (7); outside it the finite matrix symbol is smooth with a computable
derivative bound for ordinary quadrature. For reference each free 81-by-81
coordinate kernel of the resolvent difference at z=-epsilon has operator
norm at most sqrt(epsilon)/(4pi c^(3/2)), c=8a/pi^2, by extending
epsilon/[c|q|^2(c|q|^2+epsilon)] to R^3. For finite source vectors multiply
by their coefficient l1 norms; exchange-projection and finite-matrix norm
factors must also be included. Inverting GII requires its actual certified
lower eigenvalue, not a claim that that conditioning is free.

## 5. The core threshold matrix is invertible: a decaying-pole argument

Define the finite Hermitian matrix

    S0=A0-B*DQ^(-1)B-C0*GL(0)C0.                            (14)

It is positive semidefinite by the Schur forms of H>=0 and their monotone
limits. It is in fact strictly positive for every fixed mu,tau>0. The proof
does not assume a scattering length or extrapolate finite-volume eigenvalues.

Suppose S0 u=0. For epsilon>0 put

    psi_epsilon=(u, -(DQ+epsilon)^(-1)Bu,
                    -(L+epsilon)^(-1)C0u).

These are l2 fiber vectors. If Stilde_epsilon is (14) with both inverse
denominators shifted by +epsilon, direct block multiplication gives

    0<=<psi_epsilon,H psi_epsilon>
      =<u,Stilde_epsilon u>
         -epsilon(||psi_Q||^2+||psi_ext||^2)
      <=<u,Stilde_epsilon u> ->0.                           (15)

The Q part converges in norm by its gap. Every exterior coordinate converges
by (13), to a kernel which tends to zero at large pair separation. The core
is fixed. Thus there is a pointwise limit psi_0 with core u and H psi_0=0,
and it decays whenever one G pair is taken far from the remaining two sites.
For a non-G residual pair this decay instead follows from the l2 Q part.
No exponential offdiagonal Q-resolvent estimate is assumed or needed: an
l2 vector's coefficients tend to zero along distinct escaping orbit indices.
The exterior claim uses only the L1 Fourier-kernel decay just proved.

Every positive square row in (2) has finite support on occupation words.
Equation (15) forces each row to annihilate the pointwise limit. In
particular W gives, for every fixed residual pair {y,z},

    (Q_A(x+e_k)psi_0)({y,z})=(Q_A(x)psi_0)({y,z})
                     for all x,k,A.                        (16)

This statement can be written in the translation-zero fiber as simultaneous
translation invariance of the two residual coordinates relative to x.
Sending x away from fixed y,z makes each term vanish by the preceding
decay. Hence every Q_A(x)psi_0 is zero. The original expression (1), not
just the positive rewrite, now gives pointwise

                 (4mu+V3(S)) psi_0(S)=0.                   (17)

Since mu>0, psi_0=0, contradicting its nonzero core u. Therefore S0>0.

This rules out a core-coupled decaying zero-energy resonance/eigenvector in
this fixed K=0 problem. It does not rule out positive-energy resonances,
other total momenta or nondecaying threshold incoming states. It gives the
finite compact-source limit of the full resolvent via (9)-(14).
No numerical lower bound on lambda_min(S0) or on lambda_min(GII) has been
computed. For fixed computable couplings, their proven strict positivity
and the controlled entries give a terminating interval-certification route.
Uniform conditioning as couplings approach zero is not asserted.

## 6. A relaxed threshold interaction, and an exact nonzero virtual correction

For the 15 normalized constant threshold pair channels, let Phi_I be the
actual generalized four-site wavefunction made from products of the normalized
q=0 pair creators. Its amplitude is the sum over actual perfect matchings;
overlapping creators give zero. For identical pair types divide the product
by sqrt2. This is precisely the large-volume normalization of two separated
normalized pairs, not a bosonic identity for overlapping operators.

Each F_I:=H Phi_I has finite relative support: sufficiently separated pairs
each solve the actual zero-energy N=2 equation, and all remaining defects
are in the finite collision neighborhood. The sum-of-squares form of Phi_I
is finite for the same reason. Let G_H(0) be the compact-source threshold
resolvent constructed above. The exact relaxed zero-energy form is

    T0_(IJ)=<Phi_I,H Phi_J>-<F_I,G_H(0)F_J>.                 (18)

Equivalently it is the infimum of the actual H quadratic form after adding
l2 corrections to the prescribed constant incoming profile. To check the
formula, use -(H+epsilon)^(-1)F_J as the correction and pass to zero.
Finiteness of <F,G_H(0)F> makes
epsilon||(H+epsilon)^(-1)F||^2 tend to zero by dominated spectral integration.
The stationary profile Phi-G_H(0)F solves Hpsi=0 pointwise and differs from
Phi by a decaying exterior response. Thus (18) is a finite positive
semidefinite Hermitian threshold interaction form. A finite-energy
retarded/flux-normalized scattering matrix is not being asserted by definition.

The old quartic pulse supplies the first term, not (18). An exact word proves
that the subtraction is nonzero in an actual incoming E channel. Set

    S={(0,0,0),(2,0,0),(4,0,0),(6,0,0)},
    T={(0,0,0),(3,-1,1),(3,1,1),(6,0,0)}.

S has a perfect matching; T has only one G edge and lies in Q. Literal
annihilation/creation gives

                <T,H S>=tau/3.                            (19)

It comes from the center-shifted E projector in W. The matrix element to
the analogous unshifted target is (2mu-6tau)/3, so the shifted word is
chosen to avoid an accidental zero at mu=3tau.

Let C_E=sum_x Q_E1(x)*. The actual generalized vector C_E^2 Omega has
integer matching amplitude F_u(S), with axial edge weights u=(1,-1,0).
This includes the 1/sqrt2 in each E1 creator and the factor two from the
two creation orders. Directly applying H to the above target gives

               (H C_E^2 Omega)(T)=tau/3.                   (20)

Only the returned x-axis matching contributes there. This tests the
incoming collective channel, not merely a generic four-site basis state.
For its normalized identical-pair profile Phi_E=C_E^2 Omega/sqrt2,
the source component is tau/(3sqrt2). Since 0<=H<=C, the compact-source
inverse obeys G_H(0)>=1/C in quadratic form. Consequently

    0<=T0_(EE)
      <=104mu+240tau - tau^2/[18(16mu+144tau)]
      <104mu+240tau.                                      (21)

The bare term is twice the independently checked pulse coefficient
52mu+120tau, with the just-declared identical-pair normalization. Thus the
bare quartic interaction is rigorously changed by virtual/relative
relaxation. Equation (21) is a bound and (18) a constructive exact formula;
neither is a claimed numerical evaluation of the relaxed coupling.

A separate literal-state control at mu=tau=1 finds twenty Q output words
from |S>, with ||QH|S>||^2=68/9. Therefore the full-space closed-sector
self-energy diagonal lies in [17/360,68/9], by mu<=DQ<=160.
This last norm is for the literal occupation vector, not silently the
translation-normalized scattering state.

## 7. Evidence, prior work and precise residual

check_matching.py checks all 64 abstract graphs, the 9/113/1647 connected
translation-shape counts, the two exact actual-law witnesses (19)-(20),
twenty literal Hermiticity columns and the closed-output norm. Its final
capture used 0.096 wall seconds, 0.058 CPU seconds and 19.1 MB.
check_channel_geometry.py checks all 64 Gaussian-integer momentum choices
q_i in {0,pi/2,pi,3pi/2} of the full nine-by-nine symbol against literal
two-particle action. It reconstructs every connected physical core column,
including its closed/exterior outputs and the finite free hole. It used
13.763 wall seconds, 13.661 CPU seconds and 34.4 MB. It explicitly reuses
the author's action routine; these are not independent implementations.
Both jobs were priced, single-threaded and far below their memory ceilings.
No complete N=4 torus, dense many-body diagonalization or background worker
was used. Scripts and captures remain in this directory.

The closest inspected repo elimination source is the complete native
third-order star-vertex note (Sept8). It states that its energy-window
resolvent exists “even though the spectra of PH0P and QH0Q overlap at high
energies.” Its actual finite flux carrier, gap, resolvent expansion and
mixed-channel limitation were read; they do not prove this physical-site
N=4 gap or threshold. The complete contact-bound-walker note (Sept24)
explicitly says “Weak binding and threshold states are not classified.”
Its off-spectrum coin resolvent is a different carrier. The exact lattice
Green/heat-kernel note (June7) was also read, including its uniform-asymptotic
qualification. This report proves only the matrix integrability/decay needed
here and does not import its gravitational interpretation or continuum
prefactor. Full source bindings/search scope are in SOURCES.md and
SOURCE_BINDINGS.json. No external-priority claim is made.

The checked density bound and O(nu) ground-density theorem are not premises
of the threshold proof. Neither a pair-breakup gap alone, bare quartic
positivity, nor those many-body density results would justify (14)-(21).

The remaining smaller tasks are to certify numerical conditioning and the
entries/eigenstructure of (18), then prove/normalize the positive-energy
limiting-absorption and flux relation if a finite-energy scattering matrix
is desired. The current proof treats the from-below zero-energy response
and its variational interaction. Positive-energy resonances, scattering
length conventions in anisotropic channels, and uniform coupling limits
need their own statements. They are not silently assumed away.

The author's threshold proof and (18)-(21) await a focused independent
check. This packet freezes them for that check; no further conclusion is
being built on S0 invertibility before it returns.

Much stronger and still open are a controlled finite-density excitation
spectrum, two linear tensor modes, common source/action and an actual record
observable. Inserting those as a “collective phase” would be target-equivalent.
This finite-particle construction neither assumes nor establishes them.
