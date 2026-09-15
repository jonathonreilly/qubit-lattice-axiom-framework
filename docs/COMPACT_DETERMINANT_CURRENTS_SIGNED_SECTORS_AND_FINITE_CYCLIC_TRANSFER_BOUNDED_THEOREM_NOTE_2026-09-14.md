# Compact determinant currents, signed sectors and finite-cyclic transfer

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author proposal; independent scientific review is pending. The actual source
status is conditional-support. No axiom, primitive or established TOE claim
is changed.

This note derives exact current and physical-source identities for a supplied
massive determinant coupled to U(1) or finite-cyclic Villain gauge fields.
An affine integer-Gaussian comparison controls individual sectors without a
volume prefactor. Explicit counterexamples show that signed determinant
currents need not become positive after grouping, and that even the standard
r=1 Wilson paired determinant need not be of positive Fourier type. A separate
fixed-box transfer construction matches a Villain discretization to the
supplied clock Hamiltonian and identifies the remaining fermion/source match.

These results sharpen two actual steps toward an interacting finite-payload
phase. They do not establish that phase, a Hamiltonian photon, a continuum
limit, or the origin of the supplied microscopic law.

**Runner:** [self-contained primary runner](../scripts/compact_determinant_currents_signed_sectors_and_finite_cyclic_transfer_2026_09_14.py).
**Receipt:** [canonical execution cache](../logs/runner-cache/compact_determinant_currents_signed_sectors_and_finite_cyclic_transfer_2026_09_14.txt).
**Review:** [historical author review record](work_history/repo/review_feedback/pr8109-compact-current-evidence/pr8109-REVIEW_HISTORY.md); the [preserved evidence packet](work_history/repo/review_feedback/pr8109-compact-current-evidence/README.md) records its original execution and reading limits.

## Premises and dependency structure

| Input | Use | Status |
|---|---|---|
| Open rectangular cubical box, integer charge and finite massive hopping matrix | Current polynomial, character constraints and source identity | Supplied model data; exact derivations below |
| Standard r=1 Wilson projectors on the full 16-site four-dimensional box | Fourier-sign counterexample with a complete rational remainder | Explicit witness; no empirical mass threshold |
| Integer cell contraction and Poisson summation | Fillability and affine Gaussian-sector bound | Direct proof and checked standard mathematical machinery |
| Fixed finite N and specified clock couplings | Positive transfer and finite-box generator limit | Supplied Hamiltonian, separate from the Wilson determinant |
| Framework admissibility | Context only | Does not select the model or state |

No unmerged sibling is a scientific premise. The current identities support
the source-response obligation; the sign witnesses reject two positivity
shortcuts; the transfer limit fixes a discretization map without importing
any infrared conclusion. All statements are re-established in this note.

## Part I. Exact currents, Gaussian sectors and physical sources

### 1. Domain and conventions

Let a finite open rectangular cubical box in dimension d>=2 have vertex,
positively oriented edge, and plaquette sets V,E,P. Let G=d0: R^V -> R^E
be the forward gradient, C=d1: R^E -> R^P its curl. Thus CG=0. All cells
are internal to this box in this block. Set A=C^*: R^P -> R^E.

There are m fermion components at each site. The matrix D(theta)=M I+K(theta)
has only nearest-neighbor off-diagonal blocks T_xy exp(i theta_xy), with
oppositely oriented phases conjugate; the matrices T_xy are fixed. No relation
between T_xy and T_yx is needed for current conservation or the degree bound.
Take M>2dt and ||T_xy||<=t when positivity and the massive log expansion are
used. Define W(theta)=|det(D(theta)/M)|^2. The norm bound ||K||<=2dt<M
makes W strictly positive. The normalized link measure is Haar probability,
either continuous U(1) or the Nth roots of unity.

The Villain plaquette factor is normalized here as

    V_beta(u)=sqrt(2*pi*beta) sum_n exp[-beta(u+2*pi*n)^2/2]
             =sum_k exp[-k^2/(2*beta)] exp(i*k*u), beta>0.

The equality follows by computing each Fourier coefficient of the periodic
Gaussian and then applying its absolutely convergent Fourier series. The
normalization affects the partition function but not normalized expectations.
It is fixed explicitly to avoid carrying an omitted volume factor. The angle
partition function is Z=int W(theta) product_p V_beta((C theta)_p) dHaar(theta).
The equivalent positive joint law on (theta,n), n in Z^P, is proportional to
W(theta) exp[-beta||C theta+2*pi*n||^2/2] dHaar(theta), with counting measure
on n. Both Haar choices above use probability normalization.

### 2. Finite determinant currents

The determinant is a finite Laurent polynomial in exp(i theta_l). In each
permutation term at most m selected entries traverse one specified directed
edge x->y: its entries use only the m rows at x (and the m columns at y).
At most m entries traverse the reverse edge. Therefore each determinant
exponent j_l lies in [-m,m], and every exponent in W lies in [-2m,2m]. Write

    W(theta)=sum_{j in Z^E, |j_l|<=2m} w_j exp(i<j,theta>).

Gauge covariance D(theta+G chi)=S(chi)^-1 D(theta) S(chi), with site-diagonal
S(chi)=exp(i chi_x), proves W(theta+G chi)=W(theta). Orthogonality of torus
characters then gives

    w_j=0 unless G^*j=0.

For example, multiply the defining Fourier integral by a gauge shift. It
changes by exp(i<G^*j,chi>); a nonzero coefficient requires that character
to be trivial for every real chi. Reality gives w_-j=conjugate(w_j).
If W(-theta)=W(theta), then all w_j are real. Strict pointwise positivity of
W does not imply nonnegative coefficients. The scalar witness below and
the standard Wilson witness in Part II prove failures directly.

The above integer conservation follows from the continuous polynomial before
restriction to roots of unity. Starting only with a finite-cyclic gauge
invariant function would give conservation modulo N instead.

### 3. Exact character-current sums

For any integer closed edge current s define the constrained Gaussian sum

    Z_beta(s)=sum_{k in Z^P: A k=s} exp[-||k||^2/(2*beta)].

The zero sector is positive and finite. Integer homological exactness of a
contractible cubical box makes every closed integer edge current fillable.
Here is the integer cochain contraction used for that assertion. On an
interval with vertices 0,...,L, let (d f)(t)=f(t+1)-f(t), let
(h g)(x)=sum_(0<=t<x) g(t), and let p send a zero-cochain to the constant
f(0), while p is zero on one-cochains. Then dh+hd=I-p and h,p have integer
matrices. On a d-fold product use the graded tensor differential and

    H=h_1 tensor I + p_1 tensor h_2 tensor I
        + ... + p_1 tensor ... tensor p_(d-1) tensor h_d.

With the usual graded tensor signs, dH+Hd=I-p_1 tensor ... tensor p_d;
the intermediate terms telescope. The last product vanishes in positive
cochain degree. This constructs integer matrices H1,H2 and proves
G H1 + H2 C=I on edges. Transposing it, if G^*s=0, then

    s=C^* H2^* s,

so H2^*s is an integer plaquette filling. This proof includes boundary edges;
it is not an assertion of exactness on periodic tori.

Absolute convergence of the Gaussian character series and the finite Fourier
support of W justify termwise integration. Continuous integration yields

    Z_U(1)=sum_j w_j Z_beta(-j).

Finite cyclic averaging instead imposes A k+j=N q and gives exactly

    Z_ZN=sum_j w_j sum_{q in Z^E: G^*q=0} Z_beta(Nq-j).

Indeed G^*(A k+j)=0 and N nonzero imply integer conservation of q. Conversely
each such q makes Nq-j integer closed, hence fillable. These are exact
partition identities with signed or complex summands. They do not define a
positive probability measure on (j,q) for a general paired determinant.

The two useful thresholds have different meanings. If N>2m, then on each
edge with q_l nonzero,

    |Nq_l-j_l| >= (N-2m)|q_l|,

using |q_l|>=1 and |j_l|<=2m. Summing over those edges gives
||Nq-j||^2 >= (N-2m)^2 ||q||^2. If instead N>4m, distinct determinant
exponents in [-2m,2m] cannot alias to the same residue modulo N on any edge.
The latter is an injectivity statement and needs the stronger threshold.

#### Summing the fermion currents does not always restore alias positivity

There is an explicit counterexample within the massive domain above. On one
open square in d=2, take m=1, unit symmetric scalar hopping and M=5>4.
Writing its plaquette holonomy as z=exp(i phi), an exact 4-by-4 determinant is

    det D = M^4-4*M^2+2-z-z^-1 = 527-z-z^-1.

Dropping the harmless positive normalization M^-8, the paired coefficients
are w_0=277731, w_1=w_-1=-1054, and w_2=w_-2=1. Set beta=1, N=7 and
q equal to the square's oriented boundary current. After summing all j, the
canonical q-sector weight is

    S(q)=sum_{r=-2}^2 w_r exp[-(7-r)^2/2]
        =x^25 [1-1054*x^11+277731*x^24-1054*x^39+x^56],
    x=exp(-1/2).

The exact rational interval 60653/100000 < x < 60654/100000 follows from
summing exp(1/2) through degree 20 and bounding the remainder by its first
omitted term divided by 1-1/44. Inserting the lower endpoint in the negative
terms and the upper endpoint in the positive terms makes the bracket still
strictly negative (the runner records the exact rational upper bound).
Thus even the q-marginal of this canonical signed expansion need not be
positive, including N>4m where determinant exponents do not alias each other.
The original angle measure remains strictly positive. This does not rule out
a different positive representation or a phase proof using signed expansions.
The witness uses the stated general hopping family, not the four-spin r=1
Wilson specialization.

### 4. Affine integer Gaussian sectors without a volume prefactor

The following lemma holds for any real matrix A with integer entries and a
nonempty integer affine sector. Set L=ker(A) intersect Z^P and X=ker(A).
Rationality of A supplies a rational basis for X; clearing denominators shows
L spans X and is a full lattice there. Choose any integer k_* with A k_*=s.
Let y be its orthogonal projection to X-perp and x=k_*-y. Then y is the unique
minimum-norm real solution of A y=s, and

    Z_beta(s)=exp[-||y||^2/(2*beta)] Theta_L(x),
    Theta_L(x)=sum_{l in L} exp[-||l+x||^2/(2*beta)].

Poisson summation in X, with dual lattice L^vee defined by <p,l> in Z, gives

    Theta_L(x)=(2*pi*beta)^(dim X/2)/covol(L)
               sum_{p in L^vee} exp[-2*pi^2*beta*||p||^2]
                                  exp(2*pi*i<p,x>).

The sign of the last phase is immaterial by p->-p. Pairing p and -p and
using cos<=1 shows Theta_L(x)<=Theta_L(0). In dimension zero both sides are
1. Hence the exact volume-uniform sector comparison is

    Z_beta(s)/Z_beta(0) <= exp[-||y||^2/(2*beta)].

A complementary lower bound uses the integer filling directly:

    Z_beta(s)/Z_beta(0)
      =exp[-||k_*||^2/(2*beta)] E_L exp[-<l,k_*>/beta]
      >=exp[-||k_*||^2/(2*beta)],

where E_L is the centered lattice Gaussian on L. Its symmetry makes the last
expectation an average of cosh, at least one. Both bounds hold for every
integer filling; the upper bound uses the smaller minimum real norm.

For the internal box, ||A||^2=||C||^2<=4d. To prove this, extend edge fields
by zero to the infinite cubical lattice. Internal curl is a restriction of
full curl; the Fourier symbol is exterior multiplication by
q_mu=exp(i k_mu)-1, whose squared norm is at most sum_mu |q_mu|^2<=4d.
Thus ||s||^2=||Ay||^2<=4d||y||^2, and

    Z_beta(s)/Z_beta(0)<=exp[-||s||^2/(8*d*beta)].

For N>2m the termwise cyclic bound is consequently

    Z_beta(Nq-j)/Z_beta(0)
      <=exp[-(N-2m)^2 ||q||^2/(8*d*beta)].

This is a bound on a positive Gaussian sector, before summation over signed
w_j. It neither normalizes the determinant-coupled q sum nor proves a charged
phase. A comparison relative to the same fermion current's q=0 term instead
has the explicit filling cost

    Z_beta(Nq-j)/Z_beta(-j)
      <=exp[(||k_j||^2-||y_(Nq-j)||^2)/(2*beta)], A k_j=-j.

A large, spread-out fermion current can make this estimate weak. Suppressing
that dependence requires a local current expansion or another argument.

### 5. Positive density bound for the pure cyclic gauge model

Only in this paragraph set W=1. Then q has the actual positive law
p(q)=Z_beta(Nq)/sum_r Z_beta(Nr), over integer closed currents. Put
b=N^2/(8*d*beta). Since the denominator contains Z_beta(0), for 0<s<b,

    E exp(s||q||^2) <= theta(b-s)^|E|,
    theta(a)=sum_{n in Z} exp(-a n^2).

Jensen with s=b/2 gives, for |E|>0,

    E||q||^2/|E| <= (2/b) log theta(b/2)
                  <= 4 exp(-b/2)/[b(1-exp(-3*b/2))].

The final inequality uses n^2>=1+3(n-1) for n>=1 and log(1+u)<=u.
Occupied-edge density is no greater than this second-moment density. This
positive pure-gauge density estimate does not establish the requisite
small-momentum current response. The determinant-coupled signed expansion has no corresponding
probability statement from these steps alone.

### 6. Why a global absolute Fourier bound is insufficient

For q0=2dt/M<1, the convergent trace-log expansion gives
L(theta)=log W(theta)=L0+sum_{j!=0} ell_j exp(i<j,theta>). Every length-n
closed walk has |j|_1<=n. On a nearest-neighbor bipartite box nonzero currents
first occur at n=4. For a>=0 with q0 exp(a)<1, counting rooted walks yields

    sum_{j!=0} |ell_j| exp(a|j|_1)
      <= B_a := 2*m*|V| sum_{n>=4} (q0 exp(a))^n/n.

The weighted Fourier l1 norm is a Banach algebra (triangle inequality for
|j+j'|_1). Exponentiating the absolutely convergent log series therefore gives

    sum_j |w_j| exp(a|j|_1) <= exp(L0+B_a).

On the other hand w_0=integral W>=exp(integral L)=exp(L0) by Jensen. Their
ratio is at most exp(B_a), an extensive bound. Applying this globally in the
signed sector sum loses uniform thermodynamic control. This is an identified
limitation of that estimate, not a proof that all signed local expansions fail.

### 7. Physical Villain source, before any positivity claim

The physical real plaquette field is F=C theta+2*pi*n in the joint Villain
measure, with n in Z^P. A real source h couples to F, not to the dual character
k. Completing the one-dimensional Gaussian Fourier transform gives

    sqrt(2*pi*beta) sum_n exp[-beta(u+2*pi*n)^2/2+h(u+2*pi*n)]
      =exp[h^2/(2*beta)] sum_k exp[-k^2/(2*beta)]
                            exp(i*k*u-i*k*h/beta).

Consequently the exact moment-generating function in either group is

    E exp(<h,F>) = exp[||h||^2/(2*beta)] T(h)/T(0),
    T(h)=sum_(j,k satisfying the group constraint)
             w_j exp[-||k||^2/(2*beta)] exp[-i<k,h>/beta].

All derivatives exist: finite Fourier support and Gaussian character tails
justify them. In the even model T is real and even; the original positive
integral makes T(h)>0 for all real h. This does not make its individual
Fourier coefficients nonnegative. Writing the normalized signed expectation
only as an algebraic notation gives

    Cov(F)=beta^-1 I-beta^-2 Cov_signed(k).

For the pure continuous model k lies in ker(A); the character weights there
are an actual lattice Gaussian. Completing the square and the theta maximum
proved above show its MGF is at most exp[beta||P_ker(A) h||^2/2]. Thus

    beta^-1 P_range(C) <= Cov(F) <= beta^-1 I      (pure U(1)).

The upper inequality uses the genuine nonnegative covariance of k; it cannot
be imported to the determinant-coupled signed sum. The lower inequality
alone still does not give the directional zero needed for an infrared
non-summability proof: the magnetic sectors can contribute in ker(A).

For finite cyclic gauge even the pure dual k constraint is A k in N Z^E,
a full-rank sublattice containing N Z^P. Its theta maximum only gives the
trivial physical bound 0<=Cov(F)<=beta^-1 I. An intermediate massless phase
requires sharper simultaneous control of the magnetic and cyclic responses.

### 8. Exact remaining target

Construct a positive, source-compatible representation or a controlled local
signed expansion for this determinant-coupled compact/finite-cyclic model.
It must bound the response to the original physical source uniformly in box
size and in its small-momentum limit, treating both magnetic defects and cyclic
aliases, with supplied massive-matter conditions explicit. A partition-only
identity, small occupied-defect density, and the pointwise positivity of W do
not discharge that target. No new framework axiom is warranted by this gap.

## Part II. Standard r=1 Wilson sign certificate

Take the full open box {0,1}^4, all 32 nearest-neighbor links, four spin
components per vertex, and Wilson r=t0=1. For positive direction mu the
hopping block is -P_mu,- exp(i theta_l), for negative direction it is
-P_mu,+ exp(-i theta_l), with P_mu,+/-=(I+/-gamma_mu)/2. The four Hermitian
Euclidean gamma matrices are

    gamma_1,2,3 = sigma_1 tensor sigma_1,2,3,
    gamma_4 = sigma_2 tensor I.

Set D=M I+K, W=|det(I+K/M)|^2, M>8. This meets the absolute
hopping domain M>2dt in Part I. Write w_j(M) for the Fourier coefficient of W at the
integer edge current j.

### 1. The simple cycle and its exact spin trace

Starting at (1,1,0,1), traverse the direction word

    (-1,-4,+3,-2,-3,+1,+2,+3,+4,-3).

All ten visited vertices before closure are distinct and belong to {0,1}^4.
Let j put unit oriented flow on this cycle and zero on the other edges.
Then G^*j=0 and ||j||_1=10. There is no proper nonempty closed subcurrent
made from a subset of its oriented edges: each cycle vertex has exactly one
incoming and one outgoing selected edge, so following any selected edge
forces the whole cycle.

For a signed direction a put P_a=(I-sign(a)*gamma_|a|)/2. Direct exact
Clifford multiplication along the displayed word gives

    tr P_cycle=1/32,
    det(z I-P_cycle)=z^2(z^2-z/32+1/1024).

The runner checks the trace by both explicit matrices with exact rational
complex entries and a separate bit-mask Clifford-algebra multiplication.
The characteristic polynomial and cycle closure are additional checks.
The Clifford trace functional used here sends the identity to four and every
nonempty ordered gamma monomial to zero: conjugate an even-length monomial
by a gamma contained in it, or an odd-length monomial by one absent from it.
The sign reverses and trace invariance gives zero.

### 2. Leading Fourier coefficient, including the fermion-loop sign

Expand W in lambda=1/M. A degree-r term contains exactly r hopping factors
across the two determinants. Its net edge current has l1 norm at most r.
Therefore the j coefficient is zero through degree 9.

At degree 10, attaining ||j||_1=10 leaves no reversed or off-cycle hop and
no cancellation between determinants. Gauge invariance requires each
nonconstant determinant cycle to be an integer closed subcurrent of j.
The simple-cycle property forces all ten hops into one determinant cycle
in one of the two factors. Equivalently, in

    log det(I+lambda K)=sum_{n>=1} (-1)^(n+1)
                                      lambda^n tr(K^n)/n,

the selected oriented loop has ten possible roots. Their factor ten cancels
1/n. The sign is negative at even n=10, while the ten minus signs in the
Wilson hoppings multiply to positive. Thus its coefficient in one log
determinant is -tr P_cycle=-1/32. Products of shorter closed currents cannot
supply j at the same degree, so exponentiation does not alter that leading
coefficient. The adjoint determinant contributes the reversed adjoint loop,
with the same real trace: gamma_5 conjugates every P_a to P_-a. Hence

    w_j(M)=-1/(16 M^10)+higher powers of M^-1.

This is a full-box coefficient statement: the other 22 links are present,
but cannot enter that minimum-degree Fourier coefficient.

### 3. A full-polynomial remainder certificate

The full matrix has dimension Dsize=64. Each axial hopping operator is a
compression of -[P_mu,- U_mu+P_mu,+ U_mu^*], whose norm is one because the
spin projectors are orthogonal and U_mu is unitary. Consequently ||K||<=4
uniformly in all link phases. A principal minor of order r has determinant
at most 4^r in absolute value, so the coefficient of lambda^r in either
determinant is bounded by binom(64,r)4^r. Multiplication and Vandermonde's
identity give the pointwise bound binom(128,r)4^r for the degree-r coefficient
of W. Its individual Fourier coefficient obeys the same bound by integration.
Thus

    |w_j(M)+1/(16 M^10)|
      <= sum_{r=11}^{128} binom(128,r)(4/M)^r
      <= binom(128,11)(4/M)^11 / (1-39/M),    M>39.

The final ratio bound is exact: for r>=11 the next/previous summand ratio
is 4(128-r)/[(r+1)M]<=39/M. With the explicit, deliberately conservative
choice M=2^100, dividing the remainder by the leading magnitude gives

    16 binom(128,11)4^11/(M-39) < 1.

Every quantity in this last inequality is an integer or rational number.
The bound is strictly below one for every real
M>39+16*binom(128,11)*4^11. Therefore Re w_j(M)<0 for this concrete full
r=1 Wilson model. It is not
of positive Fourier type. No numerical subtraction of M^-10 terms is used
in the full-box certificate. A positive-type function on the link torus has
nonnegative Fourier coefficients: integrate its positive quadratic kernel
W(theta-phi) against a character and its conjugate. The negative coefficient
therefore contradicts that property. The very large mass is an existence witness;
no useful physical threshold, sharp mass range, or empirical parameter is
claimed.

### 4. Scope and independent check limit

The cycle-only graph is also checked separately: its transfer product gives
an exact determinant as the product of det(I-lambda^10 z P_cycle) and the
reverse-loop factor. Direct full 40-by-40 determinants at several phases
agree with that formula. This challenges the loop sign and normalization
through a separate determinant calculation. The full-box remainder proof is
analytic and rational; the cycle-only numerical test does not replace it.

This result closes only the previously untested r=1 positive-Fourier-type
hypothesis. Pointwise W>0 persists, the physical Villain measure is positive,
and neither a signed local expansion nor another positive representation is
ruled out. In particular it does not establish that any charged Coulomb phase
fails, and it creates no contradiction with the framework axioms.

## Part III. Matched finite-cyclic transfer

### 1. Exact one-link temporal transfer

Fix N>=2 and X^N=I on C^N, with X the angle-translation operator. Write

    theta(x)=sum_{q in Z} x^(q^2),  0<x<1,
    Q_x=theta(x)^-1 sum_{q in Z} x^(q^2) X^q.

This is exactly the normalized convolution transfer of a Villain temporal
plaquette on Z_N when

    beta_tau=N^2/(2*pi^2) log(1/x).

Indeed the angle difference r has weight sum_n x^((r+nN)^2); summing over
r mod N gives theta(x). The normalization makes Q_x 1=1. Its eigenvalues
are strictly positive by the Fourier transform of a periodized Gaussian,
and are at most one because it is an average of unitary translations.
Thus Q_x is positive definite and a contraction for every fixed N and x.

Set x=delta*t with t>0 and delta*t<1. If H0=2-X-X^*, then

    Q_(delta*t)=I-delta*t H0+O(delta^2),
    -delta^-1 log Q_(delta*t) -> t H0

in operator norm, for fixed N. In fact the error estimates can be independent
of N. Let R(x)=2 sum_{q>=2} x^(q^2)<=2*x^4/(1-x^5). Since ||H0||<=4,

    ||Q_x-(I-x H0)|| <=8*x^2+(4*x+2)R(x).

This follows by writing Q_x-I=[-x H0+(R_op-R I)]/(1+2x+R), with
||R_op||<=R, then adding x H0. The scalar logarithm is uniformly Lipschitz
on a fixed interval containing the spectra for small x, and
||exp(-x H0)-(I-x H0)||<=8*x^2*exp(4x), giving the stated generator limit.

This is a logarithmic temporal coupling at fixed N:

    beta_tau=N^2/(2*pi^2) log[1/(delta*t)].

By contrast, beta_tau=b/delta with fixed b>0 gives
x=exp[-2*pi^2*b/(N^2*delta)]. Then ||Q_x-I||=O(x), x/delta->0, and
-delta^-1 log Q_x->0. That conventional rotor scaling freezes the electric
motion when N is fixed. It is not the same order of limits as first taking
N to infinity.

### 2. A spatial Villain factor that yields the Wilson plaquette potential

For any plaquette angle phi define the positive normalized multiplier

    B_y(phi)=[1+2 sum_{q>=1} y^(q^2) cos(q phi)]/theta(y),
    y=exp[-1/(2*beta_s)].

The numerator is the Villain Fourier series. It is positive by its real
Gaussian representation and at most theta(y), so 0<B_y<=1. Uniformly in phi,

    B_y(phi)=1-2*y*(1-cos phi)+O(y^2).

Choose y=delta*K/2, K>0. Then

    beta_s=1/[2 log(2/(delta*K))],
    -delta^-1 log B_(delta*K/2)(phi) -> K(1-cos phi)

uniformly in phi. The same remainder estimate as for Q applies after
replacing H0 by the scalar 2(1-cos phi). This is inverse-logarithmic spatial
coupling. beta_s proportional to delta would instead give a spatial
interaction that vanishes faster than delta.

For fixed N,t,K the two matched scalings satisfy

    beta_tau*beta_s -> N^2/(4*pi^2).

This limiting product is a scaling identity, not a critical-coupling relation.
The t/K ratio remains in the subleading logarithms and in the Hamiltonian.

### 3. Matched finite-box Hamiltonian and Gauss projection

On a fixed finite spatial cell complex, allow link-dependent t_l>0 and
plaquette-dependent K_p>0. Let Q_delta be the tensor product of the temporal
Q_(delta*t_l), and let B_delta multiply by the product over plaquettes of
B_(delta*K_p/2)(phi_p). Form the positive symmetric transfer

    T_delta=B_delta^(1/2) Q_delta B_delta^(1/2).

Each factor is gauge invariant for Z_N: the link translations commute with
vertex gauge translations, and plaquette angles are unchanged. For fixed
finite volume, multiplying the norm expansions gives

    T_delta=I-delta H_g+O(delta^2),
    H_g=sum_l t_l(2-X_l-X_l^*) + sum_p K_p(1-Re W_p).

Therefore T_delta^(floor(T/delta))->exp(-T H_g) in operator norm for fixed
T>=0, as does -delta^-1 log T_delta->H_g. The same limits hold after
restriction to any invariant Gauss sector. The O(delta^2) constant from this
simple product proof depends on the finite box; no uniform thermodynamic
statement is inferred from it.

A supplied finite-dimensional gauge-invariant Hermitian matter Hamiltonian
H_m can be included by the positive sandwich

    T_delta,m=exp(-delta H_m/2) T_delta exp(-delta H_m/2).

It has generator H_g+H_m on the fixed finite box. A harmless scalar energy
shift can make each matter exponential contractive if desired. This uses the
specified operator H_m; it does not show that its coherent-state determinant
is the nearest-neighbor Euclidean Wilson matrix defined in Part II.

In particular exp(-delta h(theta)) for a spatial hopping matrix generally
has an infinite Fourier series in the link phases, even on a finite graph.
For example, take minus the scalar adjacency matrix on a four-cycle with
unit hopping and flux z. The diagonal exponential is a sum of closed walks
with nonnegative coefficients. Its z^n coefficient is at least
delta^(4n)/(4n)! for every positive integer n, from n clockwise traversals.
Thus there is no universal finite Fourier-degree bound for that exponential.
The finite-degree determinant-current bound from the nearest-neighbor D
cannot simply be transferred to that exact exponential. A bond-split transfer
can restore bounded phase degrees per factor, but its source map, multiplicity
and limiting error must be derived for that discretization.

### 4. Why the isotropic massive bound does not cover this limit automatically

Take the usual supplied r=1 free Wilson discretization with temporal spacing
delta and fixed spatial spacing a in three spatial dimensions. Its diagonal
M_delta=m0+1/delta+3/a and forward/backward hopping norms are 1/a_mu each.
The absolute rooted-walk majorant for these hopping norms has ratio

    q_count(delta)=(2/delta+6/a)/(m0+1/delta+3/a) ->2.

It therefore leaves its q_count<1 domain for every fixed physical m0. This
is a limitation of that particular absolute path estimate, not a proof of
singularity of the Wilson operator. For r=1 the orthogonal spin projectors
in opposite temporal directions can improve the operator norm: each axial
hopping operator has norm at most 1/a_mu, hence

    ||K||/M_delta <= (1/delta+3/a)/(m0+1/delta+3/a)<1, m0>0.

For open boundaries this follows by compression from unitary covariant shifts;
for periodic boundaries it follows directly from the orthogonal projectors.
The improved ratio still tends to one. It establishes invertibility/log-series
convergence at each delta, but does not supply the volume- and delta-uniform
curl-curvature majorant needed for an infrared application. Its proof counted individual paths
in absolute value, so inserting the smaller operator norm in that path count
would be invalid.

The operator also has a coercivity proof independent of the walk expansion.
Writing U_mu for the unitary covariant forward shift and P_mu,+/- for the
orthogonal spin projectors,

    Re D = m0 I + sum_mu [I-(U_mu+U_mu^*)/2]/a_mu >=m0 I.

The anti-Hermitian spin-derivative contribution cancels in Re D. Compression
preserves this inequality for open boundaries. Therefore the minimum singular
value is at least m0 and ||D^-1||<=1/m0, uniformly in delta, volume and gauge
field. This does not by itself provide the needed gauge-curl curvature bound:
trace multiplicities, gauge derivatives and physical spacetime weights still
have to be controlled.

A plausible next attack is to resum long temporal runs before expanding in
spatial hopping. It must preserve the physical field/source normalization,
fermion boundary conditions and finite-cyclic Gauss projection. No such
resummation or uniform interacting phase theorem is claimed here.

### 5. Prior art and model matching

Pásztor and Pesznyák, *Gauge field digitization in the Hamiltonian limit*,
arXiv:2609.07886v2 (9 September 2026). Their section II derives logarithmic
temporal scaling for the Wilson action; the spatial Wilson coupling scales
linearly in the time step. Their numerical work concerns pure gauge models
in 2+1 dimensions. It is not an interacting 3+1-dimensional phase theorem.
The logarithmic finite-group mechanism therefore has explicit prior art.
The additional content here is the direct Villain normalization, its pairing
with the specified clock Hamiltonian, and the checked separation
from the massive determinant/current proof domain. These are model-matching
steps, not a claim to discover the general finite-group scaling principle.

Primary source: https://arxiv.org/abs/2609.07886v2 . The fetched v2 PDF has
SHA256 5a64a9eec53ae6b24b0677ac6cc857e0d09023c9914c7fea02974840891ca835.

## Evidence and falsifiers

The input-free primary runs three substantive families. The first compares
symbolic scalar determinants, direct angle integrals, character sums, affine
integer Gaussian sums and the physical-source identity, and tests integer
contractions in dimensions two through four. The second compares direct
Villain kernels with their spectra, tests fixed-box transfer generators,
preserves exponentially small freezing effects with high-precision log1p,
and distinguishes Wilson path and operator norm bounds. The third checks the
r=1 sign witness by Clifford algebra, explicit spin matrices, exhaustive cycle
subcurrents, a rational full-polynomial remainder, and separate 40-by-40 cycle
determinants. These are author checks, not three independent reviews.

The general proofs are the displayed mathematical arguments. Finite angle
sums and sampled momenta alone do not prove their quantified domains. The
r=1 full-box Fourier sign uses the rational remainder, not the cycle-only
floating-point test. Its large mass is a conservative existence certificate.
The finite checks report floating-point tolerances and the actual evaluated
parameters in the source and cache; they are not interval-certified Gaussian
integrals. Explicit perturbations of the mathematical code are retained in
the review packet as falsifier checks.

## No-Go Discipline Gate

### N1 — Actual alternative routes

| Route | Status | Actual outcome |
|---|---|---|
| Exact determinant-current and character representation | ATTEMPTED, positive in scope | Conserved bounded Fourier currents and exact U(1)/Z_N constraints |
| Affine integer-Gaussian sector comparison | ATTEMPTED, positive in scope | No-volume-prefactor upper/lower bounds and a pure-gauge density result |
| Restore a probability by summing the matter current first | ATTEMPTED, inference refuted | Explicit massive scalar square has a negative canonical q weight |
| Restrict the positivity argument to standard r=1 Wilson hopping | ATTEMPTED, inference refuted | A simple ten-edge loop and full-box remainder give a negative Fourier coefficient |
| Couple a physical source before dualizing | ATTEMPTED, positive identity | Exact generating function exposes the needed signed response |
| Match the finite-N Villain transfer to the clock Hamiltonian | ATTEMPTED, positive on fixed boxes | Temporal/spatial scaling and Gauss-sector generator limit |
| Replace the failed path bound by Wilson operator coercivity | ATTEMPTED, partial | Uniform inverse bound; curl-curvature and time-resummed phase bounds remain open |

### N2 — Relations among remaining conditions

The compact response and phase question form one coupled obligation I. A
matched charged transfer/source limit is H. Native law selection and physical
identification are P. Their independence is not proved.

| Pair | First closes second? | Second closes first? | Independence proved? |
|---|---|---|---|
| I, H | unresolved | unresolved | unresolved |
| I, P | unresolved | unresolved | unresolved |
| H, P | unresolved | unresolved | unresolved |

The two positivity counterexamples are statements in different explicitly
specified model families. They are not counted as two independent reasons
that a charged phase cannot exist.

### N3 — Hidden-condition scan

Integer charge, open-box exactness, the finite determinant rather than an
exact temporal exponential, mass ranges, N thresholds and the Villain
normalization are explicit. Evenness is stated where signed covariances are
used. Pure-gauge density is not promoted to matter-coupled probability.
Fixed-box transfer limits do not supply uniform thermodynamic limits.
The r=1 coefficient is controlled by a full finite-polynomial remainder.
The word 'canonical' describes a specific Fourier grouping or execution
receipt, never an additional physical premise. No native law is silently
selected by calling its dynamics supplied.

### N4 — Source and residual matching

| Source or earlier obligation | Exact use here | Closure claimed |
|---|---|---|
| NIST DLMF 20.13.4, periodized Gaussian | Standard normalization comparator; the full lattice formula is displayed | Mathematical identity only |
| Frohlich-Spencer IHES/P/81/40 pp. 26-30, 38, 47-51 | Examined current separation and positive-type source steps | No charged-model theorem imported |
| Pasztor-Pesznyak arXiv:2609.07886v2 section II, equations 15-17 | Prior art for finite-group logarithmic temporal Wilson scaling | General mechanism credited; Villain normalization is derived here |
| Campaign PR #8108, compact response and r=1 positivity left open | Motivation for the new current/source derivation and sign witness | r=1 positivity shortcut rejected; the compact phase remains open |
| Campaign PR #8106, supplied finite-clock Hamiltonian | Target operator for the fixed-box gauge transfer | Gauge operator matched; nearest-neighbor Euclidean matter determinant not identified |
| MINIMAL_AXIOMS_2026-06-29.md, admissibility scope | Framework context, no scientific theorem premise | No native model selection or axiom contradiction claimed |

### N5 — Resolution and rhetoric

The primary includes per_element, per_site, per_mode, per_block and
lattice_wide scope lines. Lattice-wide means the analytic general sector
bounds, not an established interacting phase. A negative Fourier coefficient
and a negative grouped alias weight reject named positive representations;
they do not reject all representations, all couplings or all charged models.
The fixed-N freezing statement concerns the specified wrong time scaling.

### N6 — Partial closure and live routes

A local signed-current expansion, a different positive source representation,
or direct infrared renormalization could supply the response bound. Temporal
Wilson resummation may exploit the uniform coercivity without the failed
absolute path count. A direct Hamiltonian phase argument can avoid a chosen
Euclidean correspondence. Each requires its own hypotheses and evidence.
A restricted finite mass range is also a live possibility; the r=1 witness
rules out an unrestricted sufficiently-heavy-mass positive-type theorem,
not positivity in every narrower range. No axiom update is requested.

### N7 — Hostile steelman

A reviewer should reject interpreting the sign witness as a fermion sign
problem in the original paired measure: that measure is positive. The
obstruction concerns its Fourier-current representation. A reviewer should
also reject turning the fixed-box transfer limit into a uniform phase
identification. Both distinctions are kept explicit. The large-mass witness
is enough to disprove universal positive type, but does not locate a useful
physical mass threshold or determine which phase occurs.

### N8 — Cross-cycle distinction

The preceding massive covariance result did not establish the exact cyclic
current/source sum, the grouped alias sign, the r=1 Fourier coefficient or
the fixed-N transfer scaling. The present note re-establishes its own inputs
and does not reuse the earlier noncompact result as a compact phase premise.
The unresolved infrared response is the same retained open obligation,
not a newly discovered independent wall.

Gate disposition: author scope review of exact supplied-model implications
and narrowly stated inference counterexamples. Independent review is pending.

## Source trace and review boundary

- [NIST, periodized Gaussians and theta functions](https://dlmf.nist.gov/20.13): normalization reference.
- [Frohlich and Spencer, IHES/P/81/40](https://omeka.ihes.fr/files/original/c59d65f61f9b1aba2d8eb6f4c01ceb88.pdf): examined pure-gauge current and source machinery; no charged theorem imported.
- [Pasztor and Pesznyak, arXiv:2609.07886v2](https://arxiv.org/abs/2609.07886v2): prior finite-group Wilson transfer scaling; its 2+1-dimensional numerical results are not phase evidence for this note.

All model definitions, proofs and live code are in the primary pair. No
editable prompt or workflow file changes. No audit verdict, effective status,
main merge or axiom/primitive edit is part of this author proposal.

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A controlled interacting charged gauge phase on a supplied finite-payload carrier, with matched physical sources and Hamiltonian observables."
source_of_blocker_text: "frontier_question"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Independently review the exact current, sign and transfer claims; construct the actual compact infrared response or a matched direct Hamiltonian proof."
conditional_surface_status: "Supplied massive determinant and Villain models; exact current/source identities, sign counterexamples, and fixed-box finite-cyclic transfer limits, with phase and native identification open."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Direct conditional mathematical implications and explicit counterexamples to named positivity shortcuts; no phase conclusion or audit authority."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
