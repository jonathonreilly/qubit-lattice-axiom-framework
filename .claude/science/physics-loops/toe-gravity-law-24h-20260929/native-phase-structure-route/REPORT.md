# Spatial reflection and an explicit pair-field critical response

Author discovery report, 2026-09-30. Actual current-surface status:
**conditional-support** for a supplied quantum Hamiltonian and its explicitly
declared source probe. No formal review, audit, source integration or
retained-grade status is asserted. The positive-density ODLRO target remains
open. A failed reflection method is not absence of a phase.

## 1. Exact target, source and scope

The target is genuine pair off-diagonal long-range order at fixed positive,
sufficiently small chemical potential nu, on the original full occupation
carrier. One precise criterion is a volume-extensive eigenvalue of its
physical pair correlation matrix along a stated thermodynamic ground-state
family. Explicit-field polarization, a few-particle wave, or an infrared
estimate that leaves no extensive lower bound does not meet this target.

The only load-bearing science source is main
`30a9461ee19a49b99fa6628fe942f08e504e8903`,
`docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md`.
The selected procedure is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`.
All earlier route reports remain unchanged. In particular, no new
defect/coherence lemma from `native-dilute-phase-route` is a premise here,
even though a focused independent check became available during this pass.
The N4 threshold form and pulse quartic are not used.

There are two concrete outcomes. First, the actual spatial thermal
reflection form has a negative high-temperature derivative for every
mu,tau>0 and any nu. The obstruction covers all reflections that map each
site algebra to its geometrically reflected site through on-site
*-isomorphisms, not only one attempted square decomposition. Block or
nonlocal reflection maps are outside that statement. Second, an explicit
uniform pair field at nu=0 has rigorous, volume-uniform source bounds which
imply thermodynamic energy -Theta(eta^(4/3)), particle density
Theta(eta^(2/3)), and pair polarization Theta(eta^(1/3)). This supplies
critical source behavior, not spontaneous order at positive density.

## 2. Unchanged physical operators and landed inputs

On every cubic torus L>=5, V=L^3, use one actual two-dimensional tensor
factor per site, b_x=|0><1|, n_x=b_x^dagger b_x and N=sum_x n_x. Operators
at distinct sites commute. The law, state space and quantum expectation
rule are supplied; they are not selected by M2 alone.

Let G={+/-2e_i,+/-e_i+/-e_j:i<j}, m_x=sum_(d in G)n_(x+d), and

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=s t b_(x+s e_i)b_(x+t e_j),
    Q_E1=(d_1-d_2)/sqrt(2),
    Q_E2=(d_1+d_2-2d_3)/sqrt(6),
    Q_Tij=(1/2)sum_(s,t)v_ij^(s,t).

With P_E and P_T the corresponding sums of Q^dagger Q, the actual model is

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)+V3+W,
    V3=mu sum_x n_x binom(m_x,2),
    W=tau sum_(x,k,A)[Q_A(x+e_k)-Q_A(x)]^dagger
                         [Q_A(x+e_k)-Q_A(x)],
    Hnu=H0-nu N.                                          (1)

No collective component, signed plane word or shared-center contribution
is discarded. The landed theorem proves on the entire carrier

    H0>=0, H0>=c N(N-2)/V,
    c=min(tau,mu/12)/99090432,                            (2)

and its finite-torus kernel is the vacuum plus five uniform pair waves.
For K=i sum_x(Q_E1(x)^dagger-Q_E1(x)) and the exact normalized state
psi(u)=exp(-iuK)Omega, it also proves

    <H0>_u/V<=A u^4,
    |<N>_u/V-2u^2|<=B u^4,
    A=10199347200(182mu+240tau), B=3870720.               (3)

These are all-volume operator/variational inputs, not a truncated coherent
state or an independent-boson law.

## 3. A negative spatial reflection form from the actual V3 term

Take an even cubic torus L>=12 and the bond reflection
theta(x1,x2,x3)=(1-x1,x2,x3), with the left half containing the normal
coordinates 0,-1,-2. Let Theta be its antilinear occupation-basis
conjugation: Theta(b_x)=b_(theta x), Theta(n_x)=n_(theta x). This is a
spatial reflection. Positivity of exp(-beta Hnu) as a Hilbert-space
operator is a different statement and is insufficient for the form below.

Let tr be the normalized full occupation trace, and define

    R_beta(F)=tr[F Theta(F) exp(-beta Hnu)]/
                                      tr[exp(-beta Hnu)]

for an operator F in the left algebra. Spatial reflection positivity
requires R_beta(F) to be a nonnegative real number for every such F.
For tr F=0 the two halves factor at beta=0, so R_0(F)=0 and

    R'_0(F)=-tr[F Theta(F)Hnu].                           (4)

This elementary derivative is a necessary condition for RP in any
right-neighborhood of beta=0. No external phase theorem is needed for it.

Put a=(-1,0,0), b=(-2,0,0), theta(a)=(2,0,0), theta(b)=(3,0,0),
q_x=n_x-1/2, and F=q_a+q_b. The normalized trace tr(q_x^2)=1/4.
The two-site cross-density coefficient matrix, written in q variables,
is exactly

                  theta(a)  theta(b)
              a      0        mu/2
              b     mu/2       0 .                       (5)

Here is the full-term check, rather than a presumed favorable split.

* The off-diagonal pair {a,theta(b)} has normal separation four. Exactly
  one triple of V3 contains it: {(-1,0,0),(1,0,0),(3,0,0)}. Tracing its
  middle occupation gives (mu/2)n_a n_(theta b), whose q_a q_(theta b)
  coefficient is mu/2. The other off-diagonal pair similarly comes from
  {(-2,0,0),(0,0,0),(2,0,0)}. No period aliases enter at L>=12.
* The two diagonal pairs have odd normal separations three and five. All
  three sites of a V3 triple have the same parity of x1+x2+x3 on an even
  torus. Thus neither diagonal pair occurs in V3.
* The diagonal part of every on-center Q^dagger Q is a physical G-edge
  occupation projector, with separation at most two. An off-diagonal
  pair product either has four unmatched endpoints and zero two-site
  partial trace, or shares one endpoint and leaves a two-site hopping
  term of separation at most two. Thus neither the attractions nor the
  on-center pieces of W contribute to (5).
* In a cross term of W, the two pair centers differ by one unit. Their
  endpoints have opposite lattice parity, so the annihilation/creation
  pairs have no shared endpoint. Their two-site partial trace is zero.
  The chemical-potential and onsite number terms have no two-site cross
  component.

These statements also show that the full three-by-three Pauli cross
blocks on (a,theta(a)) and (b,theta(b)) vanish, not only their density
entries. In standard Pauli coordinates with n=(1-Z)/2, each nonzero
off-diagonal block in (5) is precisely (mu/8) Z tensor Z.

Substituting (5) into (4) gives the explicit witness

    R'_0(q_a+q_b)=-mu/16<0.                              (6)

Finite-dimensional analyticity implies R_beta(F)<0 for all sufficiently
small positive beta, for each stated finite torus and parameter choice.
No volume-uniform beta interval is claimed from this derivative alone.
The result holds for arbitrary nu and every tau>0. It is independent of a
choice of decomposition of Hnu into reflection squares.

The sparse local check reconstructs every contributing literal pair
projector product, using P_E,ij=delta_ij-1/3 and the actual signed plane
Gram. On L=12,14,16 it obtains exactly the two mu/8 Pauli entries and
zeros for all other tested cross Pauli entries, including all tau terms.
The analytic support/parity argument gives every even L>=12; the three
finite checks are controls, not extrapolation.

## 4. On-site twists cannot repair this bond-reflection family

Number-preserving phase twists leave q_x fixed, so (6) applies directly.
A larger precise class can be excluded without assuming that Theta leaves
Hnu invariant. Suppose Theta is an antilinear, unital, *-preserving
involution exchanging halves, and maps the algebra of each site x
isomorphically onto that of theta(x). It can rotate the three traceless
Hermitian Pauli directions at each site; these rotations are invertible.

Use the six-dimensional left test space of Pauli operators at a and b.
At beta=0 its reflection form vanishes. The derivative matrix has two
zero diagonal three-by-three blocks, because all Pauli cross coefficients
at the corresponding mirrored pairs vanish. At least one off-diagonal
block is nonzero: the rank-one mu/8 density coupling survives the
invertible on-site Pauli map.

If RP held for all small beta, this derivative matrix would have to be
Hermitian positive semidefinite. A positive semidefinite matrix with a
zero diagonal block has zero corresponding off-diagonal block, by its
two-by-two principal minors (or Cauchy-Schwarz). This is a contradiction.
If the derivative matrix is not Hermitian, positivity already fails by
polarization. Thus no reflection in this on-site class gives RP on a
neighborhood of beta=0. The ordinary spin-flip reflection is included;
one must not silently substitute it for occupation conjugation and then
reuse the sign of (6).

This conclusion does not cover a reflection that maps a one-site operator
to an entangled block operator, a different carrier/interaction, a
conditioned site-plane construction, or an inequality proved only in a
special low-temperature state. It does not rule out an infrared bound by
another method or a phase in the unchanged model. A two-site blocking
that only permutes/rephases physical sites remains in the excluded class;
a genuinely nonlocal block map needs new analysis.

## 5. The zero-density endpoint also fails the standard RP test

There is a separate, low-temperature check using only the exact landed
kernel. At nu=0 the beta->infinity Gibbs density matrix is the normalized
projection onto its six-dimensional ground space. Translation invariance
and total particle number in that space give

    <n_a>=rho_L=5/(3V).

Every two-particle ground wave has support only on physical G edges.
Because a and theta(a) have odd separation three, their joint occupation
vanishes on the entire kernel. For the left observable F=n_a-rho_L,

    <F Theta(F)>_(beta=infinity)=-rho_L^2<0.              (7)

It follows by finite-volume Gibbs convergence that the standard reflection
form also fails at all sufficiently large beta on each such torus at
nu=0. This is not a claim about every intermediate beta.

For 0<nu<3c/V, (2) shows that every N>=3 sector lies above the five N2
zero waves after subtracting nu N: relative to their energy -2nu,
the lower bound is (N-2)(cN/V-nu)>0. The N=0 and N=1 sectors also lie
above them. The ground density matrix is then the normalized five-state
projection, rho_L=2/V, and the same witness is -4/V^2.
That chemical-potential window shrinks with volume. It does not address
a fixed positive thermodynamic density, and cannot be used as a no-phase
argument there.

## 6. A distinct constructive method: response to an actual pair field

Introduce an explicitly supplied diagnostic field, not a replacement law,

    S=sum_x[Q_E1(x)^dagger+Q_E1(x)],
    H(eta)=H0-eta S, eta>0.                              (8)

All five components and all hard-core interactions remain in H0. The field
selects one E component solely as a probe; it does not show that a zero-field
ground state selects this channel. For a ground state define
e_L(eta)=E0(H(eta))/V, rho=<N>/V and m=<S>/V.

First, an elementary full-carrier source bound is

    |m|<=s sqrt(rho), s=2sqrt(2).                        (9)

Indeed |<Q_E1(x)>|^2<=<Q_E1(x)^dagger Q_E1(x)>
<=<d_1^dagger d_1+d_2^dagger d_2>. Each pair occupation is at most half
the sum of its two endpoint occupations. Summing x gives an upper bound
2<N> on sum_x |<Q_E1(x)>|^2, and Cauchy-Schwarz on the sum over x proves
(9). This proof uses the actual pair operators and applies to mixed states.

For the exact landed unitary trial psi(u), the new source expectation
satisfies

    <S>_u/V>=2u-Du^3, u>=0,
    D=1935360.                                           (10)

To prove it, set B_E=sum_x Q_E1(x), so K=i(B_E^dagger-B_E) and
S=B_E^dagger+B_E. The uniform E Gram is exactly
<Omega|B_E B_E^dagger|Omega>=V. Thus
i<K S-S K>_Omega=2V, fixing the sign and derivative 2.
The number phase exp(i pi N/2) changes both K and S to their negatives,
so the source expectation along this trajectory is odd in u.

Each local S_x has four-site support and norm <3. Using the actual
connected-commutator counting of the landed source, the third derivative
has norm bound

    ||ad_K^3 S||<=24^3*4*7*10*3 V=6D V.

Integral Taylor remainder proves (10) for the exact normalized state,
with no assumption V u^2<<1. In particular, m(u)>=u for
0<=u<=D^(-1/2). Combining this with (3), take

    eta_* =4A D^(-3/2),
    u=(eta/(4A))^(1/3),
    d=3/[4(4A)^(1/3)].

For 0<eta<=eta_*, every volume obeys

    e_L(eta)<=A u^4-eta u=-d eta^(4/3).                 (11)

This is an exact variational upper bound on the original many-particle
carrier with an explicit external source. It is not the N4 pulse quartic
reinterpreted as a scattering coefficient.

For a ground state, positivity H0>=0 and (11) imply m>=d eta^(1/3).
Equation (9) then gives rho>=d^2 eta^(2/3)/8. In the other direction,
coercivity and the vacuum energy upper bound zero give

    c(rho^2-2rho/V)<=s eta sqrt(rho),
    rho<=4/V+(2s eta/c)^(2/3).                           (12)

For the last implication, either rho<4/V or the quadratic expression
on the left is at least c rho^2/2. No assumption about a definite-N
ground state is made; the source does not conserve N, and Jensen in (2)
is the valid mixed-sector step.

There is also a finite-volume lower energy bound,

    e_L(eta)>=-3 eta^(4/3)/(2c)^(1/3)-2c/V^2.            (13)

Use c(rho^2-2rho/V)>=(c/2)rho^2-2c/V^2, (9), and minimize
(c/2)t^4-s eta t over t=sqrt(rho)>=0. The constants follow from
s^(4/3)=4; they do not contain a fitted critical exponent.

The bounded finite-range source interaction has the same elementary
open/periodic boundary comparison as the landed Hamiltonian, so the
thermodynamic energy density e(eta) exists. For all accumulation values
of rho and m at fixed eta, direct passage to the sharper uncompleted
coercivity inequality yields

    -3 eta^(4/3)/(4c)^(1/3)<=e(eta)<=-d eta^(4/3),
    (d^2/8) eta^(2/3)<=rho<=2 c^(-2/3)eta^(2/3),
    d eta^(1/3)<=m<=4 c^(-1/3)eta^(1/3).                 (14)

These are two-sided scaling bounds, not an exact leading coefficient,
uniqueness or differentiability theorem. Volume is taken large at each
fixed eta before eta decreases. At finite volume the zero-mode degeneracy
can give a different very-small-field crossover; the explicit 1/V terms
in (12) and (13) retain it.

The energy is even in eta by the number phase. Equation (14) gives zero
first derivative at eta=0 but -e(eta)/eta^2 tending to infinity. Likewise
m/eta>=d eta^(-2/3). The zero-density endpoint therefore has a singular
pair-field response, while its polarization tends to zero as the source
is removed. None of this is spontaneous finite-density order.

There is an exact normal-side calibration as well. For nu=-delta<0,
H0+delta N has the unique vacuum ground state. S Omega is the uniform E1
pair with squared norm V and exact energy 2delta. Finite-dimensional
second-order perturbation theory therefore gives on every finite torus

    E0(H0+delta N-eta S)/V=-eta^2/(2delta)+O_V(eta^4),
    (d/deta)(<S>/V)|_(eta=0)=1/delta.                    (14a)

The odd powers vanish by the same number phase. The displayed Taylor
coefficient is exact, but no volume-uniform analytic radius or remainder
is inferred from finite-dimensional perturbation theory. The uniform
critical-field bounds (14) were obtained by a different variational
argument, precisely to avoid that interchange of limits.

### Uniform extension over the actual five-component pair space

The same argument has a post-contract extension which keeps every
collective channel explicit. Put
R=(Q_E1,Q_E2,Q_T12/sqrt(2),Q_T13/sqrt(2),Q_T23/sqrt(2)), choose any
complex z with sum_A|z_A|^2=1, and use R_z=sum_A z_A R_A,
S_z=sum_x(R_z^dagger+R_z), K_z=i sum_x(R_z^dagger-R_z).
The exact uniform Gram is V I_5, so K_z Omega has norm squared V and
H0 K_z Omega=0 for every z. This is a consequence of the landed kernel
and its normalization, not an SO(3) identification.

Each local R_z has support in the six unit neighbors. The norm bound
||R_z||<=sqrt(14) follows from ||Q_A||<=2 and the three T/sqrt(2)
weights. Thus each S_z,x and K_z,x has norm <8, and each site belongs to
six supports. Connected-commutator counting now uses a factor 96s per
step and adds at most five sites. Safe uniform constants are

    A_*=96^4*25*30*35*40*(182mu+240tau)/24,
    D_*=96^3*6*11*16*8/6.                                (14b)

They give energy <=A_* u^4 and source >=2u-D_*u^3 on the exact unitary
trajectory. The source-density bound can be taken as |<S_z>|/V<=6sqrt(rho):
sum_(x,A)<R_A^dagger R_A> is bounded by the number of physical G edges,
which is at most9<N>. The first comparison follows from the orthogonal
axial doublet and the normalized plane constant vector; every plane edge
occurs at two centers with weight1/2. Applying Cauchy-Schwarz to R_z and
then to the spatial sum proves the stated bound.

Consequently the same energy/density/polarization exponents in (14) hold
uniformly over z, with A,D,s replaced by A_*,D_*,6 and
0<eta<=4A_*D_*^(-3/2). Explicitly put
d_*=3/[4(4A_*)^(1/3)]; then the thermodynamic bounds include

    -(3/4)*6^(4/3)*(4c)^(-1/3)eta^(4/3)
                    <=e_z(eta)<=-d_*eta^(4/3),
    (d_*^2/36)eta^(2/3)<=rho_z<=(6/c)^(2/3)eta^(2/3),
    d_*eta^(1/3)<=m_z<=6^(4/3)c^(-1/3)eta^(1/3).         (14c)

Uniform bounds on these powers do not make the leading coefficients
equal, select a polarization, or identify E and T as a continuum tensor.

## 7. What is still required at fixed positive density

For the actual positive-density model consider

    Hnu(eta)=H0-nu N-eta S,
    e_nu(eta)=lim_(V->infinity) E0(Hnu(eta))/V.

The same basic inequalities bound every accumulation density by
c rho^2<=nu rho+s eta sqrt(rho). Consequently any source-removal
accumulation at fixed nu has rho<=nu/c and |m|<=s sqrt(nu/c).
They give no positive lower bound on m as eta->0 at fixed nu.

The needed source-defined spontaneous E1 polarization would be

    liminf_(eta->0+) liminf_(V->infinity) <S>/V>0.        (15)

A verified nonzero value would imply an extensive physical pair
correlation eigenvalue by <B_E^dagger B_E>>=|<B_E>|^2: the normalized
uniform E1 test vector gives lambda_max>=m^2 V/4. This is a
**stronger, channel-selecting** sufficient target for general pair ODLRO:
the latter might occur in a different channel or mode. It cannot be
deduced from the eta^(1/3) endpoint response by interchanging eta and nu.
Proving a cusp of e_nu(eta) at eta=0 is the same source-order obligation
in energy language, not a new small compatibility lemma.

An infrared approach has a similarly concrete missing ingredient. With
R=(Q_E1,Q_E2,Q_T12/sqrt(2),Q_T13/sqrt(2),Q_T23/sqrt(2)), the actual energy
identity supplies total pair weight at least
V rho[1/2-nu/(2mu)] in a zero-field Hnu ground state. To force extensive
zero-momentum weight, one must bound its *normal-ordered* nonzero-momentum
depletion below that total. A density-independent spin infrared bound
whose momentum integral is a positive O(1) constant cannot do that in the
dilute limit, where the total weight is O(rho). Replacing the physical
correlator by a canonical-boson covariance would be an unproved change of
carrier.

For example, a genuinely verified estimate of the form

    tr Gamma(k)<=C min(sqrt(nu/ell(k)),nu^2/ell(k)^2),
    ell(k)=4sum_j sin^2(k_j/2), k!=0,                     (16)

with a constant independent of volume and small nu, would be a strong new
mechanism: its three-dimensional normalized sum is O(nu^(3/2)), whereas
the landed density lower bound is a positive constant times nu.
This would leave extensive zero-mode weight for sufficiently small nu.
Equation (16) is an explicitly unproved sufficient lemma, not a result,
an imported Bogoliubov formula, or an asserted necessary condition for
ODLRO. The crossover ell~nu gives the power by direct shell integration;
the uniform finite-volume small-mode sum has the same bound. Other
phase proofs need not establish this particular shape.

The new RP obstruction explains why a direct spatial reflection argument
on the declared on-site class cannot supply such a bound. It does not
prove (16) false. A different reflection representation, a direct
many-body variational comparison, or another correlation method remains
open. Simply stating that the nonzero-mode sum is smaller than the total
by a fixed fraction is essentially the chosen zero-mode-condensation
target via its sum rule; it must not be advertised as a nearly finished
reduction.

Even a pair ODLRO theorem would not establish two linear tensor modes.
The microscopic continuous number symmetry is U(1), the spatial symmetry
here is cubic, and no SO(3) identification, excitation dispersion, record
readout or common-action gravity source is supplied by this report.

## 8. Prior arguments, hypotheses and concrete verification

The current-main classical vacancy infrared note was read at its actual
kernel-split/Gaussian-domination statements: it proves a bound only when
its crossing kernel is positive and has an explicit positive stiffness.
It is a different, classical content law, not the quantum operator (1).
The native weak-electric density note was read in full; its useful
variational/entropy argument explicitly does not transfer RP or a mean
density bound to a perturbed phase theorem. The staggered temporal RP
note was read selectively for its declared transfer/Gram and one-/two-step
scope. Its fermionic temporal construction is not a spatial RP theorem
for this model. No result from those comparisons is a proof premise.

The primary Jaffe–Janssens paper was read in sections V.1–V.4 and VI.1–VI.2.
It uses actual crossing couplings to characterize spin RP and relates
changed reflections to algebra automorphisms; its conventional spin
reflection differs from occupation conjugation. The derivative criterion
used here is independently proved in (4). Its theorem is not an imported
phase conclusion. [Primary paper](https://arxiv.org/abs/1506.04197).
The Dyson–Lieb–Simon quantum-spin phase paper was located bibliographically
but its full required hypotheses were not read or invoked. No named
literature theorem substitutes for the failed hypothesis of (6).

`check_reflection.py` imports no earlier route implementation. It expands
the literal creation-pair/annihilation-pair products, including all signed
plane coefficients, and takes their exact normalized two-site Pauli
projections. Four unmatched endpoints give zero partial trace; one shared
endpoint gives its actual n factor and a hopping operator; equal pairs
give n n. These are exact trace operations, not an effective Hamiltonian.
All 153 triples per contributing center are included.

For each L=12,14,16, 74 contributing centers produce 66,156 local projector
products. The expected two mu/8 Pauli entries and every tested zero agree
exactly over rational arithmetic, including imaginary Pauli components.
The final run took 1.442 wall seconds, 1.441 CPU seconds and 17,219,584 bytes
peak RSS on this macOS runtime, with threads1. No full-carrier thermal
diagonalization or scan was performed. The proof of the field response
is analytic; the runner only checks its integer Taylor constants.

The exact next action is a focused independent check of the whole-H
two-site trace, on-site-reflection extension and the source Taylor/Jensen
bounds, before extensive reuse. The strongest remaining phase obligations
are (15), (16), or another actual extensive pair-eigenvalue mechanism.
None is claimed complete. No PR, source/audit mutation or campaign stop
follows from this route-local method limitation.
