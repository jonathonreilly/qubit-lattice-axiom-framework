# Joint equal-time gauge and matter state in the simultaneous limit

Personal derivation, 2026-09-16. **Provisional author theorem proposal.**
Dependencies: Block01 plaquette concentration, Block02 uniform energy and
oscillator-defect estimate, and Block03 gauge characteristic function.
All remain provisional pending independent review. The model is exactly
Block02's supplied quadratic paired Wilson/compact-rotor Hamiltonian, with
no additional unscaled onsite charge interaction.

## 1. Statement

Let g->0 and L->infinity jointly along any sequence. At each finite g,L use
the normalized trace over the entire ground space in N_+=N_-=L^3 and exact
integer Gauss law. For real fixed local link and plaquette smears w=(u,v),
write

    W_(g,L)(w)=exp(i[P(u)+Z(v)]),                         (1)

with the rescaled weighted fields P,Z of Block02. For fixed finite-path
gauge-neutral matter polynomials use the explicit dressing in section3.
Every finite word in these bounded physical observables has a limit.
The limit is the product of:

- the centered free transverse gauge-field Gaussian state specified by
  Block03, with covariance quadratic form
  `kappa(w)=u.Omega_infty.u+v.Omega_(p,infty).v`;
- the filled-negative-band Slater state omega_F of the free paired Wilson
  one-particle matrix (including the supplied band parameters b,zeta).

More explicitly, for any finite list w_1,...,w_n and any fixed neutral
finite CAR polynomial B, dressed by j_L,

    lim rho[W(w_1)...W(w_n) j_L(B)]
       =exp[(i/2)sum_(j<k) sigma(w_j,w_k)]
           exp[-kappa(sum_j w_j)/4] omega_F(B),          (2)
    sigma((u,v),(u',v'))=(Su).v'-(Su').v.                (3)

The local form S in (3) has no ambiguity in sufficiently large boxes.
Interleaved words have the same limit after commuting fields past matter
and preserving the original CAR order. Finite choices of dressing paths
or roots give the same limit for neutral polynomials. No assertion concerns
paths or smears whose lengths grow with L or 1/g.

This is a joint **equal-time, weak-microscopic-coupling** limit. It neither
proves a fixed-g Coulomb/Weyl phase nor supplies real-time convergence,
finite-clock realization, law selection, or an axiomatic TOE.

## 2. Exact transport and the limiting Weyl product

Put beta_w=g W_E^(1/2)u. The first-order transport equation gives exactly

    [W(w)psi](theta)=exp[i phi_w(theta)] psi(theta+beta_w),
    phi_w(theta)=int_0^1 Z(v)(theta+s beta_w) ds.         (4)

This is an identity on the full rotor/Fock space and restricts to physical
states. The multiplication part is real, so its exponential has modulus
one. It can be verified by differentiating in the time parameter in (1).

For fixed local u,v, Taylor's formula for sine gives uniformly in theta,L

    phi_w(theta)=Z(v)(theta)
                    +(1/2)(Su).diag(cos theta_p).v+r_w(theta),
    ||r_w||_infty<=C_w g.                               (5)

For example the second-order remainder is bounded by
`(g/6)sum_p sqrt(b_p)|v_p|[(C W_E^(1/2)u)_p]^2`.
Only fixed finitely many plaquettes contribute.

The product W(w)W(w') translates by beta_w+beta_w'. Its exact phase
difference from W(w+w') is

    phi_w(theta)+phi_w'(theta+beta_w)-phi_(w+w')(theta)
      =sigma(w,w')/2
        +(1/2)sum_p [(Su)_p v'_p-(Su')_p v_p]
                                      (cos theta_p-1)
        +r_(w,w')(theta),
    ||r_(w,w')||_infty<=C_(w,w') g.                     (6)

The sign in (6) is positive. It agrees with the limiting commutator
`[P(u)+Z(v),P(u')+Z(v')]=-i sigma(w,w')`.

By Block01, `||(cos theta_p-1)||_rho<=sqrt(2B0)g`.
After translating the angles by g W_E^(1/2)sum_j u_j for a fixed list of
smears, the same norm is bounded by Cg, by the Lipschitz estimate in
Block03. Together with |exp(ix)-1|<=|x| this proves

    ||W(w)W(w')-exp[i sigma(w,w')/2]W(w+w')||_rho<=Cg.   (7)

The norm here is `||X||_rho^2=rho(X^*X)`. In deriving (7), the phase
defect in (6) must be evaluated after the translation from W(w+w'); the
translated estimate supplies exactly that step.

The same inequality holds when applied to any fixed finite word of field
unitaries and bounded dressed CAR operators on the right, with a constant
depending on that word. Indeed, field unitaries add only a fixed total
angle translation and a unit-modulus multiplication phase. Dressed CAR
operators are bounded matter-valued multiplication functions, commute with
scalar angle functions, and retain the same operator norm after translation.
Thus every scalar phase defect still reduces to a translated ground-state
cosine defect multiplied by a bounded matrix. Finite sums of words follow
by the triangle inequality.

Repeated use of (7) and Block03 yields all pure-gauge word expectations in
(2). More importantly, the word-excited version makes the Weyl relations
valid on the full cyclic space of any limiting joint state, not merely
in its expectation on one vector.

## 3. Physical neutral matter and an auxiliary full CAR extension

Fix an origin0 and, for every site x of Z^3, a finite oriented integer path
p_x from0 to x. Set p_0=0 and choose p_(e_i) to be the single positive link
in direction i. Any fixed finite set of these paths embeds in all
sufficiently large periodic boxes without identification of distinct sites.
Use q_+=1, q_-=-1 and define

    a_(x,s)=U(p_x)^(q_s) c_(x,s).                        (8)

Orbital indices are implicit and are not mixed by the dressing. Rotor
multiplication commutes with all CAR operators, so (8) obeys the exact CAR.
It gives a norm-preserving *-homomorphism j_L on each fixed finite CAR
algebra, as an algebra of operators on the ambient rotor/Fock space.

For D=tail-minus-head, Dp_x=delta_0-delta_x. Under the Gauss transformation
generated by G_y=(DE)_y-Q_y, U(p_x) transforms with phase
exp[i(alpha_0-alpha_x)], while c_(x,s) transforms with exp(i q_s alpha_x).
Therefore a_(x,s) carries charge q_s at the root and no charge elsewhere.
Every polynomial of total gauge charge zero maps to a physical bounded
operator preserving Gauss law. Nonneutral elements of the auxiliary CAR
algebra do not preserve it and are not being presented as physical charged
observables.

The finite-rank physical ground density matrix defines a positive state
on the ambient Hilbert space as well. Composing it with the full finite CAR
homomorphism gives a normalized positive functional. Its nonneutral
expectations vanish because all charge remains at the root and the ground
space obeys Gauss law. Its separate species-number symmetries also follow
from fixed N_+,N_-. This positive auxiliary extension is useful below;
the final physical statement (2) is restricted to neutral observables.

## 4. Path independence and emergent matter translation invariance

Two finite paths with the same endpoints differ by an integer closed chain
in Z^3. Such a chain is a finite integer sum of elementary plaquette
boundaries: commute coordinate steps, cancel backtracking, and fill the
remaining coordinate rectangles. For any fixed resulting loop,

    ||U_loop-1||_rho
       <=sum_p |n_p| ||U_p-1||_rho
       <=sqrt(2B0)g sum_p |n_p|.                        (9)

Integer multiplicities and signs are covered by telescoping powers of a
unitary. Multiplying by a bounded CAR monomial does not spoil this estimate,
because the scalar loop multiplication commutes with it. Equation (9)
therefore compares any two fixed path systems for a neutral polynomial.

When the root changes, insert a common connector from the old root to the
new one. Its phase cancels from every monomial of total charge zero, and
the remaining differences are again finite loops. Translate a rooted
polynomial by a fixed lattice vector. The actual finite-volume rho is
translation invariant. Comparing the translated root/path system with the
original one using (9) shows that every limiting neutral CAR expectation
is translation invariant. Nonneutral expectations are zero throughout, so
the auxiliary full CAR limit is translation invariant too. The rooted
finite-g auxiliary state itself is not assumed to be translation invariant.

State compactness can be made elementary here: choose a countable dense
set of local CAR polynomials and use a diagonal subsequence of their bounded
expectations. Positivity and the norm bound pass to the limit, producing
a state omega on the infinite CAR algebra.

## 5. Its free energy density is minimal

Let h_loc be the free paired matter energy in one cell: its onsite term
and the three forward nearest-neighbor Hermitian hopping terms. With the
path convention just specified, j_L(h_loc) is exactly the physical matter
energy density at the root, including its gauge link phases. In particular

    j_L(c_0^* T_i c_(e_i))=c_0^* T_i U_i c_(e_i)

for the plus species, and the conjugate expression holds for the minus.
Translation invariance of the actual ground trace and Block02 give

    omega(h_loc)=lim rho(calH_m)/V
       =lim E_m,L/V=:e_m,free.                          (10)

The last limit is the Brillouin-zone integral of the negative eigenvalues
of the free symbol. Those eigenvalues are continuous functions of momentum,
even at the Weyl points, so ordinary Riemann sums suffice. No gap estimate
or finite-volume eigenvector limit is used in (10).

## 6. Isolated Weyl points do not allow a different covariance

Write h(k)=h_+(k) direct-sum h_-(k) on the four matter orbitals per site.
For any translation-invariant CAR state its one-particle covariance C is
a positive contraction on l2(Z^3) tensor C^4. This follows directly from
the CAR: for every finitely supported f,

    0<=omega(a(f)^*a(f))<=||f||_2^2.                   (11)

The covariance commutes with translations. Fourier transformation therefore
represents it as multiplication by a measurable matrix C(k) satisfying
0<=C(k)<=I almost everywhere. Equivalently, the positive Fourier measure of
its matrix coefficients is dominated by the identity Lebesgue measure by
(11), so it has a bounded density. In particular no occupation measure
concentrated at an isolated momentum is permitted.

Let P_-(k),P_+(k) be the negative and positive spectral projections of h(k)
away from its zeros. The free energy-density excess is

    omega(h_loc)-e_m,free
      =int_(BZ) tr |h(k)| [P_+ C(k) P_+
                         +P_- (I-C(k)) P_-] dk/(2pi)^3.  (12)

Both terms in square brackets are positive. For0<zeta<1 the plus symbol
vanishes only at (b,0,+/-arccos zeta), modulo the Brillouin torus; the minus
symbol has the corresponding conjugate pair. Possible coincidences of
these points do not change their measure-zero property. Thus |h(k)| is
strictly positive off a finite set.

By (10), (12) is zero. Consequently P_+ C P_+=0 and
P_- (I-C) P_-=0 almost everywhere off that set. Positivity of C and I-C
also eliminates their off-diagonal blocks. It follows that

    C(k)=P_-(k) almost everywhere.                     (13)

This reasoning does not assert uniqueness of a finite-box matter ground
state. At an exact zero mode, different occupations can have the same
energy. It uses the bounded covariance and measure-zero zero set only
after taking the translation-invariant infinite-volume state limit.

## 7. Projection covariance determines the full pure Slater state

Equation (13) fixes more than the two-point function. In the GNS
representation of omega, if f belongs to the positive spectral subspace,

    a(f) Omega_state=0;

if f belongs to the negative spectral subspace, then

    a(f)^* Omega_state=0.                              (14)

These statements follow from the corresponding zero nonnegative excitation
occupations. They apply to l2 vectors as well as finite-support vectors
because the CAR operators are continuous in that norm.

Choose orthonormal bases of the two spectral subspaces. The particle
annihilators in the positive subspace and the hole annihilators in the
negative subspace annihilate the same vector and satisfy the CAR. Reorder
any finite polynomial by those relations. Its expectation is the vacuum
contraction value, hence the filled-band Slater value. Approximate arbitrary
test vectors in the spectral subspaces by finite basis sums to obtain all
local polynomial expectations. This identifies omega uniquely as omega_F.

It also proves purity without assuming it. In any convex decomposition of
omega, each nonnegative excitation occupation in (14) must still be zero
in each component. The same CAR reordering then identifies every component
with omega_F. There is no nontrivial decomposition.

The projection hypothesis is essential. Equal nonprojection two-point
covariances can have different four-point functions; the auxiliary fixture
preserves such an example. The proof has obtained an exact projection in
the limiting state, rather than inferring a Slater state from unspecified
two-point data.

## 8. Gauge and matter commute in the limit

For each dressed generator in (8),

    [P(u),a_(x,s)]
       =g q_s <W_E^(1/2)u,p_x> a_(x,s),
    [Z(v),a_(x,s)]=0.

Exponentiating this exact eigenoperator commutator yields

    W(w)a_(x,s)W(w)^*
       =exp[i g q_s <W_E^(1/2)u,p_x>] a_(x,s).          (15)

Thus `||[W(w),j_L(B)]||<=C_(w,B)g` for any fixed local CAR polynomial,
including the nonneutral auxiliary elements. This is an operator-norm
bound, independent of the state. Norm approximation extends the limiting
commutation property to the full CAR algebra.

## 9. Positivity of the joint limit and factorization

For any chosen finite set of real local field probes, take the countable
additive group generated by them and a countable norm-dense set of local
CAR polynomials. A diagonal subsequence gives all bounded word
expectations. For every finite word polynomial X, rho(X^*X)>=0. Hence the
limiting functional is positive. The CAR relations hold exactly. Their
operator-norm bounds pass to the cyclic representation, since at finite
volume `rho(X^*j(B)^*j(B)X)<=||B||^2 rho(X^*X)`.

Each W has norm one and W(-w)=W(w)^*. The word-excited estimate in section2
makes the Weyl product relations valid throughout the limiting cyclic
representation. The norm estimate (15) makes its field algebra commute
with the represented CAR algebra. This constructs a positive joint state
sigma on commuting bounded algebras. No presumed tensor factorization is
used in this construction. Arbitrary selected finite real probes can be
handled by choosing their own countable additive group; a separability
assumption on the entire abstract Weyl algebra is unnecessary.

Its CAR marginal is the pure state omega_F of sections5--7. If G is a
positive bounded element of the commuting gauge algebra, then

    B -> sigma(G B)

is a positive functional on CAR and lies between zero and
||G|| omega_F. A positive functional dominated by a multiple of a pure
state must be a scalar multiple of that state: subtract the normalized
functional from that multiple, and any failure to be proportional would
give a nontrivial convex decomposition of omega_F. Therefore

    sigma(G B)=sigma(G) omega_F(B).                     (16)

Extend linearly from positive G to every bounded gauge element. Block03
and section2 determine the gauge marginal. This proves (2) for every
subsequential limit. Since the value is unique and all finite-word
expectations are bounded, the original full sequence converges.

## 10. Checks and limits of the result

The new Weyl-product fixture uses exact finite rotor matrices and checks
the positive phase sign both on a ground vector and after a field/charge
excitation. A reversed sign retains an order-one discrepancy while the
correct discrepancy decreases with g; its bounds are specified by the
Taylor/translated-defect argument, not fitted to the output. The Fourier
boundary mass is recorded and negligible for those auxiliary vectors.

A separate free two-band fixture keeps two different exact finite-volume
zero-mode ground occupations at half filling. Their full covariance
operator difference has norm one, while their fixed-site difference is
the number of zero momenta divided by volume. This discriminates local
state convergence from a false global operator-norm or finite-box
uniqueness assertion. Another fixture gives equal nonprojection covariance
with different four-point functions, testing the necessity of section7's
projection premise. These computations are author checks; the general
proof is the argument above.

The observable domain is local and equal-time. Growing Wilson loops,
macroscopic probes, charged fields without a finite neutral dressing,
real-time propagation, nonzero-temperature states, and fixed-positive-g
infrared behavior are outside this theorem. The supplied model's fields
and coefficients remain inputs. This conditional bridge removes a prior
order-of-limits restriction without selecting those inputs from axioms.
