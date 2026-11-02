# COMBO — the combined separated-field witness and its exact scope

**PROVEN:** on one specified separated e hierarchy, AF-e together with a
nonzero separated fourth cumulant excludes the literal union
`F1 union F2 union F3` defined below. It also excludes the uniformly
enveloped canonical mixtures in NONFREE55, with the corrected mean term.
**PROVEN counterexamples:** it does not exclude even all finite mixtures
of elementary generalized free fields, or Wick composites of arbitrary
generalized free fields. **PROVEN:** the conjunction is a two-part
criterion; it does not supply ASSEMBLY55's current single continuous
finite-moment N5 witness for that union. A precise replacement and its
conditional assembly proof are in section 5. **OPEN:** its actual
Yang–Mills hypotheses, adoption of the proposed contract, unrestricted
free-net exclusion, full existence and the physical mass gap.

This is a bounded author result under [PROCESS_LIGHT](PROCESS_LIGHT.md).
The comparator definitions and repaired free-side input come from
[WITNESS](WITNESS.md), checked against [its review](REVIEW_WITNESS.md).
The Gaussian cumulant, test geometry and four-source contract come from
[CUMUL](CUMUL.md), checked against [its review](REVIEW_CUMUL.md).
[NONFREE55](NONFREE55.md) is read with its errata and
[CODEX_REVIEW_NONFREE](CODEX_REVIEW_NONFREE.md), particularly R2–R5,
R7, R10 and R16. A review verdict is provenance, not a mathematical
premise. PROVEN below denotes the stated mathematical scope, not audit
or retained status. Balaban and Dimock receive credit for the larger
constructive Yang–Mills program.

## 1. One algebra, one normalization, one reconstruction

**PROVEN as an exact specification; actual YM realization OPEN.** Set

    E_n = ^0 S(R^(4n)),     A_e = direct_sum_(n>=0) E_n,
    e_a(x) = (4a^4)^(-1) sum_(mu!=nu) sum_(p in clover_mu,nu(x))
                                  [1-Re tr(U_p)/N],
    ehat_a = e_a - E_(K,R)e_a,                  Z(a)=1.       (1)

Tests in E_n are Schwartz and flat to every order on all pair-coincidence
planes. Only the products admitted by this separated hierarchy are used.
In particular, the formulas do not adjoin a coincident product e(f)^4.
Use the same Euclidean action, reflection, reality and permutation rules,
and the same actual continuum hierarchy `S=(S_n)` for both conjuncts.
Subtraction in (1) is deterministic at each regulator; it changes no
cumulant of order at least two. The Wilson convention is
`u_i=g_FLOW,i^(-2)=2N/g_std,i^2`, with fixed N>=2.

For definiteness use CUMUL (C2) verbatim: epsilon=1/10000,
`b(t)=exp[-1/(1-t^2)]` on |t|<1 and zero elsewhere,
`rho(x)=product_mu b(x_mu)/(integral b)^4`, and

    c_i=((2i-5)/2,0,0,0),
    f_i(x)=epsilon^-4 rho((x-c_i)/epsilon),
    f_(i,lambda)(x)=lambda^-4 f_i(x/lambda),   i=1,...,4.

All are nonnegative unit-integral smooth tests with disjoint ordered time
supports; reflection exchanges 1 with 4 and 2 with 3. For WITNESS's
AF test choose `f=f4`, `g=f1=theta f4`. This satisfies its support
requirement x0>1. Thus no test-family identification is implicit. With
odd L>=3, lambda_m=L^-m, put

    V_m = lambda_m^8 S_2^T(f_(1,lambda_m),f_(4,lambda_m)),
    AF-e: V_m -> 0 and lambda_m^-eta V_m -> +infinity
                                      for every eta>0.    (2)

Each V_m is nonnegative by reflection positivity and centring. Fix one
integer m_star before the cutoff/volume limit and put lambda_star=L^-m_star.
For the four tests at that scale set

    M_B = S_|B|(tensor_(i in B) f_(i,lambda_star)),
    K4 = sum_(pi partition of {1,2,3,4})
               (-1)^(|pi|-1)(|pi|-1)! product_(B in pi) M_B. (3)

The products in (3) are products of numbers. With zero means this is

    K4 = S4(1,2,3,4) - C12 C34 - C13 C24 - C14 C23,
    Cij=S_2^T(i,j),     B=C23>=0,
    W(S) := [AF-e] AND [K4!=0].                            (4)

W is a logical criterion, not a scalar-valued N5 functional. Seven
centred moment coordinates suffice for K4; without centring use all 15
nonempty-subset coordinates. The pair for AF is (1,4); the optional ratio
`R4=K4/B^2` uses (2,3). Their distinct source weights must be retained.

**PROVEN conditional reconstruction interface.** Require the actual
hierarchy to satisfy S0=1, E1/E2/E3, component reality, and

    |S_n(F)| <= alpha (n!)^beta ||F||_(sn),1,  all n>=1,    (5)

with one triple (s,alpha,beta) and the exact seminorm/test spaces of
[REC_CONT section 1](REC_CONT.md). Its continuation and
[REC_LIB section 18](REC_LIB.md) then reconstruct this same hierarchy on
its OS Hilbert space. A vacuum- and field-preserving equivalence preserves
the ordered Euclidean data, hence all the values in (2)–(4).

For the cumulant this can also be checked directly: continue every
partition term of (3) to the ordered tube. Subtuple gaps are sums of
future-cone gaps; different blocks use disjoint variable slots. Their
boundary products are tensor products, so no undefined coincident
distribution product occurs. The finite sum has polynomial tube growth.
If the reconstructed field is Gaussian, its truncated boundary is zero;
REC_LIB's boundary uniqueness makes this analytic sum zero, including
its matching Euclidean slice. Conversely a Gaussian Euclidean hierarchy
has zero analytic cumulant by uniqueness from that totally real slice.
Thus a nonzero (3) survives the OS quotient. Contacts vanish on E_n.
This invokes the stated local reconstruction library, not an unproved
identification of flowed or auxiliary observables with e.

## 2. Union theorem and canonical mixtures

The class names mean the following, as in WITNESS section 1.

| Class | Exact membership on the named e generators |
|---|---|
| F1 | A Hermitian scalar finite Wick polynomial, with finitely many derivatives, in finitely many canonical free fields of fixed finite masses/spins, in their free vacuum; all coefficients and finite tensor products are allowed. Propagators are finite matrix differential polynomials in mass-shell scalar propagators. |
| F2 | An **elementary** scalar/tensor generalized free hierarchy with an admissible positive tempered spectral measure; its named generators are Gaussian. Wick composites of GFFs are not included by that word. |
| F3 | Any Gaussian/quasi-free state on the named bosonic generators after centring, with arbitrary means and possibly degenerate covariance. |

F2 is contained in F3 at this Gaussian-generator scope. The redundant
name retains the brief's comparison. These are classes of the full
hierarchy with its specified field and vacuum, not just of two-point
functions or of unlabelled Hilbert spaces.

**Theorem U — PROVEN.** For an admissible hierarchy in section 1,

    W(S) implies S not in F1 union F2 union F3.             (6)

Here is the free-side argument, including the analytic part needed from
WITNESS. The heat representation

    G_s(r)=(16 pi^2)^-1 integral_0^infinity
                         t^-2 exp[-r^2/(4t)-s t] dt

gives G0=1/(4 pi^2 r^2). For s=m^2>0 write
`G_s=Y(mr)/(4 pi^2 r^2)`; the radial field equation gives
`z^2 Y''-zY'-z^2Y=0`. The series
`Y=a0+sum_(n>=1)(a_n+b_n log z)z^(2n)` obeys

    b1=a0/2,
    4n(n-1)b_n=b_(n-1),
    4n(n-1)a_n+(4n-2)b_n=a_(n-1), n>=2.

Its two free constants a0,a1 span the two solutions; factorial
denominators give convergence with all finite derivatives on punctured
compact intervals. Finite Wick contraction therefore gives a convergent
integer-power series of finite nonnegative log degree. Scalar covariance
removes angular dependence. After cancellations a nonnull centred F1
field has

    S_2^T(r)=c r^-gamma |log r|^j (1+o(1)),
    gamma integer, j>=0 integer, c>0.                     (7)

If all coefficients vanish the separated analytic kernel is zero.
Reflection positivity at reflected points fixes the positive sign in
(7). Masses may change c and the first surviving exponent: there is no
claim that they are always subleading. Smearing over the fixed separated
supports multiplies the leading coefficient by
`I_gamma=integral f1(x)f4(y)|x-y|^-gamma dxdy>0`, uniformly under dilation.
If gamma>=8, V_m cannot tend to zero. If gamma<=7,
`lambda_m^-1/2 V_m ->0`, contradicting (2). A null field also fails the
lower clause. This proves F1 exclusion, with no classification of all
local fields in a free net.

For F2/F3, use formal variables z1,...,z4 with z_i^2=0. The Gaussian
subset-moment polynomial is

    sum_B M_B z_B = exp(sum_i mu_i z_i + sum_(i<j) Cij z_i z_j).

Expanding its logarithm gives (3): k blocks occur k! times and the log
coefficient is (-1)^(k-1)/k. The logarithm has degree at most two, so
K4=0. This is independent of the covariance, masses, means, degeneracies
and tensor contractions. Equations (2) and (4) thus exclude respectively
F1 and F2/F3, proving (6). The hypotheses need not fail on the same
conjunct for every member of the union. The OS argument in section 1
turns this hierarchy statement into the corresponding reconstructed
named-field statement.

**Theorem U-ENV — PROVEN with the stated envelope.** Enlarge F1 by
finite canonical mixtures, or probability mixtures with finite component
mean variance and the common small-distance bound

    0<=C_alpha(r)<=D r^-gamma_alpha |log r|^J,
    0<r<=r0<1,    D,J,r0 independent of alpha.             (8)

Here gamma_alpha is (7)'s leading exponent; null components can be
omitted. For translation-invariant component means mu_alpha, the
connected kernel of the mixture is

    C_mix(r)=integral C_alpha(r) dnu(alpha)
                                  + Var_nu(mu_alpha).    (9)

This is obtained by subtracting the square of the mixed mean from the
mixed raw second moment. It is not generally affine in the state.
Fatou applied to nonnegative reflected pairings and V_m->0 forces
gamma_alpha<=7 almost everywhere. Since lambda_m |x-y|<1 eventually,
(8) bounds their integral by `D' lambda_m^-7 (|log lambda_m|+c0)^J`.
The finite variance in (9) is O(1). Multiplication by lambda_m^(15/2)
makes both vanish, contrary to (2). A finite mixture has common envelope
constants by taking maxima and a smaller r0. Hence AF alone excludes
this enlargement, and adding K4 changes neither its proof nor scope.

## 3. Edge cases: what the union quantifier does and does not cover

**PROVEN — deterministic affine changes.** For fixed a!=0 and b,
`e'=a e+b` gives `V'_m=a^2 V_m` and `K4'=a^4 K4`. This follows by
centering or by adding only a linear term to the formal log. Thus both
conjuncts and the class exclusion are invariant under fixed nonzero
rescaling and deterministic shifts. For a=0 both lower tests fail.
A cutoff-dependent normalization is not permitted in (1). Random means
or amplitudes describe mixtures, not this affine invariance.

**PROVEN — tensor cases at their exact scope.** Finite tensor products
of canonical underlying theories are already F1. A scalar contraction
of any finite canonical tensor polynomial is also F1. Gaussianity of a
tensor family implies the same vanishing cumulant for every four fixed
component tests, including affine linear mixing of components.

If one explicitly changes the named field to a finite bosonic Cartesian
tensor family, choose a fixed test vector h and its reflected test J theta h
for the AF pairing. The finite canonical expansion before smearing is a
uniform angular integer-power/log series on the separated supports.
Integrating each coefficient gives either a zero pairing for all small
lambda, or a first integer-power/log term with positive coefficient by
RP. The same gamma>=8/gamma<=7 contradiction applies to that pairing.
For Gaussian exclusion a single nonzero contracted fourth cumulant is
enough. REC_LIB section 15 uses the invertible Wick conversion
`C=direct_sum_r diag(i,1,1,1)^(tensor r)` and reflection J. Every term
of an n-point cumulant has the same C^(tensor n), preserving zero/nonzero.
No unspecified spinor or abstract representation reconstruction is
asserted. Extending U-ENV to a tensor family requires its common envelope
for the selected contracted pair; scalar (8) is not automatically that
new hypothesis. The YM theorem here continues to use scalar e in (1).

**PROVEN — Gaussian on e, composite underneath.** If the e hierarchy is
Gaussian, K4=0 irrespective of a purported composite realization in a
larger free theory. If that realization is also in F1, AF fails as well.
No theorem saying every nonlinear polynomial must be non-Gaussian is
needed. Conversely, non-Gaussianity of a canonical free composite is
common: it is AF that excludes it. K4 by itself does not do so.

**PROVEN counterexample — finite Gaussian mixtures.** Use WITNESS's
explicit centred GFF q with separated kernel

    Q(r)=integral_0^infinity [s^2/log^2(e+s)] G_s(r) ds.    (10)

Its heat representation gives
`c r^-8/log^2(1/r)<=Q(r)<=C r^-5+C' r^-8/log^2(1/r)` for small r.
For completeness, split the mass integral at r^-1. The low part is
O(r^-5); for the rest use
`integral s^2 G_s(r) ds=192/(pi^2 r^8)` and the logarithmic denominator.
Restricting mass to [r^-2,2r^-2] and heat time to [r^2,2r^2] gives the
lower bound. Positive separated smearing yields AF-e. Its Gaussian OS
hierarchy and the growth required for (5) can be constructed by finite
atomic limits as in the next section; WITNESS also gives an explicit
positive subtracted Fourier covariance. Neither method assumes a
divergent unrenormalized Euclidean spectral integral at coincidence.

Take a random, spacetime-constant amplitude T=1 or 2 with probability
1/2 each, independent of q, and let e=Tq. This is the state
`(S_q+S_(2q))/2` on the very same A_e with fixed normalization. Each
component is an elementary F2/F3 state. With Qij the separated pair values,

    Cij=(5/2)Qij,
    K4=(9/4)(Q12 Q34+Q13 Q24+Q14 Q23)>0.                  (11)

Indeed E[T^2]=5/2, E[T^4]=17/2, and their difference
`E[T^4]-E[T^2]^2=9/4` multiplies the Gaussian pairing sum. All Qij>0
for our tests. Also V_m is (5/2) times q's value, so W holds. Finite
convex combination preserves RP, Euclidean invariance, reality and
the common all-order growth bound. It is an admissible reconstructed
example, not merely a four-variable distribution. Therefore

    W does NOT exclude conv(F1 union F2 union F3).         (12)

It does not refute (6): this mixture is itself neither Gaussian on e
nor a finite canonical composite.

Even fixing the opposite sign does not remove all mixtures. Let T=+1
or -1 equally and e=q+T, so the components are affine Gaussian. For
the unit-integral tests `Cij=Qij+1`, `K4=-2`; the constant covariance
adds only lambda_m^8 to V_m. AF still holds. Deterministic centring of
the total state does not remove this random invariant variable. A
common-centred Gaussian scale mixture has the familiar nonnegative
same-test fourth cumulant, but varying means escape that restriction.
No OS4/unique-vacuum premise is silently imposed to discard these examples.

## 4. A free-composite example and the finite-moment obstruction

**Theorem G — PROVEN.** There is a scalar Wick-composite hierarchy of
two independent GFFs which satisfies W and is a limit, on every E_n,
of F1 hierarchies. This rebuilds and strengthens for this task the
NONFREE55 E3 / CODEX_REVIEW_NONFREE R5 example. It is not an imitation
of the Bianchi/Maxwell tensor numerator withdrawn in NONFREE55 E2.

Put

    h(s)=1/log(e+s),
    H(r)=integral_0^infinity h(s)G_s(r) ds,
    chi=:psi1 psi2:,   psi1,psi2 independent with kernel H. (13)

The colons specify the separated Wick-composite hierarchy; they do not
assert existence of the pointwise product of Euclidean random
distributions. Its construction and actual reconstruction follow below.
Since 0<h<=1, the heat integral gives

    0<H(r)<= integral_0^infinity G_s(r)ds=1/(pi^2 r^4).

Splitting at s=r^-1 gives an upper bound
`C r^-3+C' r^-4/log(1/r)`. Restricting s to [r^-2,2r^-2] and heat time
to [r^2,2r^2] gives a lower bound `c r^-4/log(1/r)`. For sufficiently
small r the r^-3 term is absorbed into the logarithmic term. Thus

    c r^-4/log(1/r) <= H(r) <= C r^-4/log(1/r).             (14)

Independent Wick contraction gives `S2^chi(x,y)=H(x-y)^2`, so (14)
proves both AF clauses after positive separated smearing. At four
distinct points write `A=H12 H34`, `B0=H13 H24`, `C0=H14 H23`.
The raw fourth moment is `(A+B0+C0)^2`; its three disconnected
products are A^2,B0^2,C0^2. Therefore

    K4^chi(x1,x2,x3,x4)=2(AB0+AC0+B0C0)>0.               (15)

Integrate this kernel against the four disjoint nonnegative tests to
obtain K4>0. The formula is a point-kernel identity integrated over
four slots, not a product of separately smeared H covariances. All odd
moments vanish by psi1 -> -psi1. This example is outside F1 by AF and
outside elementary F2/F3 by (15), while remaining a composite in an
underlying generalized free theory.

**PROVEN — construction, growth and approximation.** For an integer
ell>=1, partition [0,ell] into intervals of length 1/ell, choose their
positive right endpoints s_j, and assign weights
`w_j=integral_(I_j) h(s)ds`. Set `H_ell=sum_j w_j G_(s_j)`.
The heat integral shows G_s decreases in s. Consequently

    0<=H_ell(r)<=H(r),  and H_ell(r)->H(r) for every r>0.  (16)

Convergence follows from continuity on each compact mass interval,
vanishing mesh, and the integrable positive mass tail at fixed r.
Each H_ell is the covariance of a finite sum of independent canonical
scalars with coefficients sqrt(w_j). Taking two independent copies
makes `chi_ell=psi1_ell psi2_ell` an F1 field. Its separated n-point
kernel for even n is the square of the Gaussian pairing sum; odd n
give zero. There are ((n-1)!!)^2<=n! terms and each has n edges.
Thus, uniformly in ell, with delta=min_(i<j)|xi-xj|,

    |S_n^chi_ell(X)| <= A^n n! min(delta,1)^(-4n).          (17)

Here and below A is a fixed bound, unrelated to the pairing A in (15).
The same estimate holds for the limiting kernel. For a flat test F
and delta<1, project a closest pair onto its coincidence plane. The
displacement has l1 length at most 2delta. All lower Taylor jets
vanish there, and the segment stays within distance one of X. Taylor
order 4n gives

    |F(X)| <= (2delta)^(4n)/(4n)! * 2^(5n/2)
              ||F||_(9n),1 (1+|X|^2)^(-5n/2).            (18)

For delta>=1 use the weighted zeroth derivative. The last weight has
integral at most `Z0^n`, where
`Z0=integral_(R4)(1+|x|^2)^(-5/2)dx<infinity`, because it is bounded
by the product of those n weights. Equations (17)–(18) give the single
uniform bound

    |S_n^chi_ell(F)| <= D^n n! ||F||_(9n),1
                    <= exp(D)(n!)^2 ||F||_(9n),1.         (19)

They also supply an integrable dominating function for each fixed F,
so dominated convergence gives convergence on all E_n, not merely
on the selected four bumps. S1=0 and S0=1 complete (5).

Each approximant has the canonical Wick OS forms. Their positivity
can be seen from the scalar reflected covariance
`integral d^3p/[(2pi)^3 2sqrt(p^2+s)] |integral_(t>0)
exp[-t sqrt(p^2+s)] fhat(t,p)dt|^2`; Gaussian pairing takes its
symmetric tensor-power Gram forms. Restricting to Wick composites
preserves those nonnegative norms. Every admitted OS quadratic form
is a finite combination of separated moments, so its limit remains
nonnegative. E1/E3/reality pass as well. REC_CONT and REC_LIB apply
with the uniform bound (19). This proves the claimed OS construction
using the same reconstruction interface as the union theorem.

One may keep psi1,psi2 and chi jointly. Every mixed word has at most
two Gaussian legs per insertion and at most n edges; at most
`(2n-1)!!<=2^n n!` contractions occur. The same argument gives (19)
with enlarged D for this finite labelled family. Its Gaussian
subhierarchies are the independent GFFs and its composite correlations
are exactly their cross-species Wick products. This supplies the common
free-composite realization, rather than only a guessed e two-point
function.

The identification with the underlying Gaussian space can be made
explicit. On compact ordered positive-time supports, split each chi(x)
into psi1(x) and psi2(x+tau_split v), with v0>0 and smooth displacement
tests supported away from zero; keep both insertions ordered in that
time region. Cross-species self-contractions vanish. All other insertions
are separated; reflected cross terms remain a positive distance apart.
Their Wick kernels therefore converge as tau_split->0, including the
two norms and mixed inner product in the squared norm of the difference
from the chi vector. That difference tends to zero. Apply this to
each insertion of a compact ordered joint test, then use the common
flat-space continuity and ordered-test density from REC_LIB. Every
joint OS vector is thus a limit of psi-only vectors. The joint space
is the Gaussian space generated by psi1,psi2; the chi-cyclic subspace
has the stated Wick-composite realization there.

The same bound also validates the examples in section 3. Replace h by
`s^2/log^2(e+s)` in the atomic construction: its kernel is at most
`192/(pi^2 r^8)`. Gaussian n-point pairings have n/2 edges, so again
at most power 4n in delta. Bounded amplitudes and shifts change only
the constant D and a factorial pairing bound. Hence those examples
have a common triple in (5), including the allowed invariant sector.

**Corollary G-FIN — PROVEN, with a limited quantifier.** There cannot
be a continuous function w of finitely many separated moments which
vanishes on all F1 states and is nonzero for **every** state satisfying
W. Indeed chi_ell is F1, all its chosen moment coordinates converge
to those of chi, and continuity forces `w(chi)=lim w(chi_ell)=0`, while
chi satisfies W. This includes any proposed continuous finite-moment
encoding of the conjunction for the whole union. Multiplying K4 by
an AF indicator instead gives a discontinuous, infinite-coordinate
object at this example.

This does **not** prove that every OS hierarchy is in the finite-moment
closure of F1, does not settle NONFREE55's general NG1-prime conjecture,
and does not rule out a different finite-moment witness using additional
YM-specific information. It proves that W alone cannot furnish the
unchanged universal N5 contract. The example also proves that exclusion
of all GFF composites by W is false, not just unproved.

## 5. Exact N5-COMBO replacement and N1F assembly

**PROVEN interface diagnosis.** K4 is a continuous finite-moment
polynomial vanishing on F2/F3, but it need not vanish on F1: CUMUL's
free Maxwell composite already has a positive K4 at these tests.
AF is an asymptotic property of countably many two-point coordinates.
Neither a pair of these objects nor their logical AND meets the current
[ASSEMBLY55 N5](ASSEMBLY55.md) requirement of one finite-moment
functional null on the entire named free class. G-FIN rules out a
universal conversion of this criterion into such a functional.

**ARGUED recommendation; PROVEN conditional closure.** The following
is the exact proposed replacement, without editing ASSEMBLY55 or
[PANEL_P1](PANEL_P1.md):

> **N5-COMBO.** On the same normalized A_e and the same sequence as
> H_reg, H_RP and H_Euc, use (i) a fixed four-test polynomial K4 with
> convergent defining coordinates and liminf_j |K4_j|>=c4>0, and
> (ii) the fixed countable test family V_m with convergent coordinates.
> There are specified finite positive bounds l_m,h_m, independent of
> cutoff and volume, such that for each fixed m>=m0, eventually in j,
> l_m<=V_(m,j)<=h_m, with h_m->0 and lambda_m^-eta l_m->infinity
> for every eta>0. The named comparator is exactly F1 union F2 union
> F3, optionally enlarged only by the U-ENV canonical mixtures.
> The same reconstruction identifies all these separated values;
> its full hypotheses remain part of H_reg/ALG/REC.

The tail index may depend on m; l_m,h_m,m0,c4 and m_star are fixed
before extracting the final limit. Uniform convergence in m is not
required. E-TS below supplies a stronger uniform regulator statement.
For canonical exclusion alone the eta=1/2 clause suffices, but retaining
all eta makes the contract exactly the requested AF-e.

**Proof of N1F-COMBO.** Use one convergent determining hierarchy, with
uniform extension to every test here. Fixed finite RP, reality,
permutation and Euclidean-symmetry identities pass as in N1F; (5) and
REC supply the actual reconstructed field. Polynomial continuity passes
the fixed positive K4 margin. For each fixed m, take j->infinity in
its two-point inequalities. These now hold for all countably many m
in the same state. Only then take m->infinity, obtaining (2). Apply
Theorem U, or U-ENV for its stated enlargement. No interchange of
limits or new subsequence for individual cumulant terms is used.
In particular a moving-scale assertion with m=m_j would not be this
contract. The passage is by individual closed inequalities followed by
a comparator theorem, not by claiming non-freeness is closed.

The optional display R4 is continuous only where B>0 and passes to a
limit with a uniform margin B_j>=b>0. It is not a replacement for (3):
there is no continuous nonconstant scale-invariant extension at the
zero field. Scaling any fixed moment tuple to zero proves that fact.
K4 alone needs no denominator estimate for elementary Gaussian
exclusion. Adoption of N5-COMBO and the precise OWN-free target remains
**OPEN as a contract decision**; this deliverable does not make it.

## 6. Combined Yang–Mills obligations and shared inputs

All actual YM inputs in this section are **OPEN**. The implication from
them is **PROVEN**. No coordinator estimate is repaired or strengthened
by this lane. Use the flat Wilson law throughout; a sphere version needs
its own maps, quantifiers and diagonal construction.

| Named input | Required statement and sharing |
|---|---|
| E-ALG = C-ALG | The very same centred clover (1), E_n, source maps, E(4) action and actual all-order (5), normalization, reality, RP and permutations. Apply REC_LIB/REC_CONT once. Neither conjunct uses flowed e, time-zero B or auxiliary soft noise. |
| E-SEQ + C-SEQ/MOM | One (K_j,R_j), a_j=L^-K_j->0, R_j->infinity, converging for the determining hierarchy, every AF pair and the seven fixed cumulant coordinates (15 with means). Uniform seminorm estimates extend dense-test convergence to the exact bumps. Weak convergence of random variables alone is not moment convergence; a probability-law route additionally needs uniform integrability. |
| E-TR = C-TR | One fixed nonzero admissible g_ref and the same actual chain couplings: `0<U_-(m)<=u_(K-m)<=U_+(m)`, `U_±=g_ref^-2+beta_± m log L ± R_F`, beta_->0. No fitted or independently retuned four-point coupling. |
| E-TS | On the AF pair (1,4), for all m>=m0, K>=m+d0 and admissible R, `c_- u_(K-m)^(-kappa')<=V_m^(K,R)<=C_+ u_(K-m)^(-kappa)`, with fixed `0<kappa<=kappa'<infinity` and constants uniform in K,R. |
| C-4MATCH | A relative lower matching estimate for the **connected**, normalized four-source derivative, on the same law and tests, as in (20) below. This is the additional dynamical lower estimate. |
| C-2MATCH/UP and C-ORIGINAL | Bounds/convergence for all six pair terms and every original-law normalization, terminal, background and large-field contribution. For the optional ratio supply the separate positive denominator match on (2,3). Source upper bounds never replace C-4MATCH. |

E-TS and E-TR give the proposed bounds
`l_m=c_- U_+(m)^(-kappa')`, `h_m=C_+ U_-(m)^(-kappa)`.
Since U_± grow linearly in m, h_m->0 and every positive exponential
L^(eta m) beats U_+(m)^kappa'. This proves AF in the specified limit order.

For the fourth matching, set `d=N^2-1` and use CUMUL (C14)'s exact
smooth coefficients, not its point-evaluation value:

    A4=d A_sm/pi^8,   A2=d B_sm/pi^4,
    A_sm=16 integral product_i[f_i(x_i)d^4xi]
          sum_(cycles 1234,1243,1324)
              tr product_(edges ij) Gtilde(x_i-x_j),
    B_sm=12 integral f2(x)f3(y)|x-y|^-8 dxdy,
    Gtilde(z)=Lambda^2(I-2zz^T/|z|^2)/|z|^4.

CUMUL's support calculation gives `3/2<A_sm<5/3`, `11<B_sm<13`, hence
A4,A2>0. These are named local library inputs, including its verified
Wilson/clover normalization. Require, with k=K-m,

    P_(K,R)(m)=lambda_m^16 K4_(K,R)(m),
    |P_(K,R)(m)-A4 u_k^-4|
       <= A4 u_k^-4 [r4(m)+h4(K-m)+v4(R/lambda_m)],        (20)

with nonnegative errors tending to zero in their own arguments, uniformly
on the common trajectory. This is C-4MATCH; all disconnected subtractions
are already included. A direct fixed-scale bound
`liminf_j |K4_j|>0` would suffice for the minimal combined criterion,
but (20) is CUMUL's named structured producer.

Choose m_star large enough and then fixed depth/volume thresholds to make
the bracket <=1/2. On a tail of the common sequence,

    K4_j >= lambda_star^-16 A4/[2 U_+(m_star)^4] = c4>0.  (21)

No convergence of u_k itself is needed. The analogous A2 bound for
`Q_(K,R)=lambda_m^8 C23` supplies
`B_j>=lambda_star^-8 A2/[2U_+(m_star)^2]>0` and, if wanted,
`R4_j>=2A4/(9A2^2)>1/[507(N^2-1)]`. This optional denominator work
is not an additional logical requirement for K4!=0. All six pair
coordinates still require the ordinary moment/convergence control.

**PROVEN conditional production comparison; actual estimates OPEN.**
WITNESS's sufficient PL-1L_Sigma is
`|sum_i(D_i-Lambda_i)|<=C u_k^(-2-theta2)`, theta2>0, retaining the
terminal covariance. With FLOW-pw, K-dec and LGF it produces E-TS with
kappa=kappa'=2. The stronger per-slice PL-1L is sufficient, not needed
as an extra independent conjunct once E-TS is supplied.

For four insertions CUMUL instead names

    G_run=sum_l mathcal K_l/u_l,
    P_run=16d lambda^16 sum_(three cycles)
                     Tr(W_c1 G_run W_c2 G_run W_c3 G_run W_c4 G_run),
    PL-4C: |P_(K,R)-P_run|<=C4 u_k^(-4-theta4), theta4>0. (22)

The W_i here are the fixed quadratic clover-source weights, not the
logical criterion W. Together with
`|P_run-A4u_k^-4|<=C_AF,4 u_k^-5+A4u_k^-4[h4+v4]`, (22) implies
(20), absorbing the relative powers into r4(m) by U_-(m). Four-factor
telescoping of separated kernels of size O(u_k^-1) and errors
O(u_k^-2) gives the O(u_k^-5) reference error; its uniform kernel
hypotheses must actually hold. Orthogonality of conditional-expectation
increments is a second-cumulant identity and does not split a fourth
cumulant into unmixed slices. Mixed conditional covariance/mean terms
must remain in the connected source derivative.

To identify the shared source estimates S precisely, write
`S_src(J)=log E_(K,R) exp(sum_i J_i O_a(f_i))` for the normalized source
functional, distinct from the Schwinger hierarchy S_n. Its derivatives
of order two and four are the two cumulants. The shared analytic
package is SRC-poly/SRC-kappa(+LF), its genuine source domains,
original-law denominators, singleton terms and all-order extension/
growth estimates. This notation does not assert that there is a landed
theorem called S with all these properties. ASSEMBLY55 N9/N10 retains
the corresponding unresolved applications. Two-source upper control
or a fixed source radius alone gives no connected fourth lower match.

Both routes use the same coupling-one free curvature slices and
[LGF](LGF.md)'s scalar/free lattice Green library, through the order-two
curvature bound consumed in WITNESS: `G^F=d_lat Delta_1^-1 d_lat*` and error
`O(r^-5)+O(T^-4)`, with T=R/a and 1<=r<=T/4. The two-point route
squares that kernel; the four-point route uses its four-cycle products.
The same FLOW-pw and K-dec inputs control replacement of slice couplings
by u_k. LGF supplies neither PL-1L nor PL-4C for the interacting law.
Here d_lat is the discrete exterior derivative, unrelated to the colour
count d=N^2-1.

The incremental cost is therefore four-source connected matching,
including leading source-image factor one, background/coarse covariance
and running-coupling identification, all terminal terms, four-insertion
large-field sums, disconnected cancellations and the required moment
extension. Common ALG/SEQ/TR/all-order OS work is shared once; it is
not a second reconstruction. If the AF pair estimate is only proved for
(1,4), it cannot be reused without proof for (2,3) or the other pairs.
The fixed source radius, finite-coupling remainder and original-law
coercivity/tails remain named coordinator inputs at their supplied scopes.
None is asserted here to produce the needed four-source derivative.

## 7. Strength relative to T_OS and final status

| Claim | Status and boundary |
|---|---|
| Literal F1 union elementary F2 union F3 exclusion | **PROVEN** by U on the same reconstructed named-field hierarchy. |
| NONFREE55's repaired T_NF: F1 plus finite/ENV canonical mixtures | **PROVEN implication** from W, already from AF, using (9). The additional K4 removes the elementary Gaussian AF counterexample. |
| Every finite mixture of classes in the union | **PROVEN false** for W; (11) and the random-shift example pass it. |
| Every GFF-composite realization | **PROVEN false** for W; (13)–(19) supply a common-algebra OS example with positive K4. |
| Arbitrary canonical mixtures without ENV; arbitrary infinite Wick series or unmarked free-net embeddings | **OPEN as exclusion targets**; the union proof gives no such theorem. No polynomial-classification result recalled from memory is used. |
| A single finite-moment N5 witness inferred universally from W | **PROVEN impossible at that quantifier**, by G-FIN. A different YM-specific finite-moment witness remains **OPEN**. |
| N5-COMBO and N1F-COMBO conditional assembly | **PROVEN implication**; their acceptance as the intended target contract is **OPEN**. |
| Actual YM E-ALG/SEQ/TR/TS, C-4MATCH and original-law bounds | **OPEN**. The coefficients and conditional algebra do not prove them. |
| Existence of the full intended YM observable theory, clustering, unique vacuum, nontrivial scattering or a physical mass gap | **OPEN**; none follows from these two local/UV tests. |

**ARGUED recommendation.** ASSEMBLY55 N0 leaves the meaning of “free”
to an explicit OWN-free contract. If it means the finite canonical
assignments and ENV mixtures recommended in NONFREE55, this conjunction
supplies that comparator theorem and an additional elementary Gaussian
exclusion. If it means all mixtures, all GFF composites, or equivalence
of arbitrary unmarked local nets, the conjunction does not meet it.
Field-preserving data cannot be promoted to a classification after
forgetting the field. The scalar e sector is also not automatically the
full family of YM gauge-invariant observables.

A positive AF lower clause excludes the zero/constant-only e sector;
it does not prohibit all other senses of trivial dynamics. The explicit
free-composite and mixed examples demonstrate that limitation without
claiming any property of the unknown YM limit. In particular the expanded
existence-and-mass-gap goal in HANDOFF remains separate and open.

## 8. Provenance and verification

The method credits are Isserlis/Wick for Gaussian contraction,
Osterwalder/Schrader and Glaser for the reconstruction program, and
Balaban/Dimock for the constructive YM program. The primary
[Duetsch–Rehren paper, section 2.1, pp. 7–8](https://arxiv.org/pdf/math-ph/0209035)
was inspected for generalized-free and composite-field terminology.
No literature assertion supplies a proof step here. The GFF product
example is credited locally to NONFREE55 E3 and its repaired review;
the growth and finite-atomic closure argument is printed in section 4.
No memory-only [m] claim bears weight.

The [criteria](checks/combo_criteria.md) precede implementation of the
finite exact checks. [All 18 checks passed](checks/combo_results.json),
including four controls detecting incorrect formulas. The
[resource receipt](checks/combo_run.json) records nice 20, one thread per
numerical library, an exclusive lock, load1 2.1211, free memory 51% and
combined peak RSS 41,500,672 bytes. These finite formal identities do
not verify asymptotic estimates or the actual Yang–Mills inputs.

**Fresh hostile review: LAND, with no binding fixes.** The
[separate-context review](checks/combo_review.md) independently re-derived
the arguments, including the joint-space construction, growth/atomic
limit, limited finite-moment obstruction and conditional assembly.
This is same-family Codex review, not a cross-family review or audit
grade. Its accepted scope retains every OPEN YM and target-contract
obligation above. Only this provenance section changed afterward.

[Source identities](checks/combo_sources.json),
[final verification](checks/combo_verification.json) and
[COMBO_LOG](COMBO_LOG.md) record the reviewed/final hashes, checks and
unchanged scientific text. All 3,505 pre-existing files are preserved;
only the authorized new COMBO outputs were written. No commits, axiom,
audit or ledger edits were made.
