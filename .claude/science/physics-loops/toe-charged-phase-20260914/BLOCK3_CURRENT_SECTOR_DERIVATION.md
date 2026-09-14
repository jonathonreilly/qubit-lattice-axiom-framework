# Exact determinant currents, cyclic aliases, and Gaussian sector comparison

Personal exploratory derivation, 2026-09-14. Author proposal; independent
review pending. This is a supplied Euclidean lattice model, not an axiom-derived
Hamiltonian or a proof of its charged massless phase.

## 1. Domain and conventions

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
It is fixed explicitly to avoid carrying an omitted volume factor.

## 2. Finite determinant currents

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
W does not imply nonnegative coefficients. The block2 explicit Wilson r=2
flux witness rules out that inference for the full permitted model family.

The above integer conservation follows from the continuous polynomial before
restriction to roots of unity. Starting only with a finite-cyclic gauge
invariant function would give conservation modulo N instead.

## 3. Exact character-current sums

For any integer closed edge current s define the constrained Gaussian sum

    Z_beta(s)=sum_{k in Z^P: A k=s} exp[-||k||^2/(2*beta)].

The zero sector is positive and finite. Integer homological exactness of a
contractible cubical box makes every closed integer edge current fillable.
A constructive proof is obtained by transposing the integer cochain homotopy
identity G H1 + H2 C=I on edges: if G^*s=0, then

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

### Summing the fermion currents does not always restore alias positivity

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

## 4. Affine integer Gaussian sectors without a volume prefactor

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

## 5. A genuine positive result for the pure cyclic gauge model

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
small-momentum current response, just as the block2 magnetic density estimate
does not do so. The determinant-coupled signed expansion has no corresponding
probability statement from these steps alone.

## 6. Why a global absolute Fourier bound is insufficient

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

## 7. Physical Villain source, before any positivity claim

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

## 8. Exact remaining target

Construct a positive, source-compatible representation or a controlled local
signed expansion for this determinant-coupled compact/finite-cyclic model.
It must bound the response to the original physical source uniformly in box
size and in its small-momentum limit, treating both magnetic defects and cyclic
aliases, with supplied massive-matter conditions explicit. A partition-only
identity, small occupied-defect density, and the pointwise positivity of W do
not discharge that target. No new framework axiom is warranted by this gap.
