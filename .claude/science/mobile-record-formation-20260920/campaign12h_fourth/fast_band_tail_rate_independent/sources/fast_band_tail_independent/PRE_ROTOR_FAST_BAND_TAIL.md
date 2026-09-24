# Independent PRE: the rotor cube fast-band tail

For the stated rotor N=6, total-charge-four, W=1 physical Gauss sector, and
fixed delta,kappa>0, the answer is

    lim_(tau->infinity) ||exp[tau(-i delta G1-kappa Gamma1/2)] r|| = 0

for every normalizable physical r. There is nevertheless a stationary dark
vector in the zero-phase Fourier fiber. It is not a normalizable state of the
physical integer-flux space. In fact the physical semigroup has operator norm
one at every finite tau>=0, so the strong limit is not an operator-norm limit.

The proof uses an exact finite Laurent-matrix certificate, then a measure and
semigroup argument. It does not replace a physical flux state by one fiber.
This PRE was reconstructed without reading any root tail packet, external
personal tail plan, current campaign CHECKPOINT, or other agents' current work.
No author comparison, publication, audit verdict, or claim about a fixed
positive physical time is made.

## 1. Supplied operator and its complete physical sector

The cube has A={0,3,5,6}, B={1,2,4,7}. Edges are oriented A to B:

    (01,02,04,31,32,37,51,54,57,62,64,67).

Each vertex has charge q_v in {0,+1,-1}; div E=q-1_A; every rotor link field is
an arbitrary integer. The sector has six occupied sites and total charge four,
so it has five plus charges and one minus charge. W=1 means precisely one A
vacancy. Since there are two vacancies in total, there is also one B vacancy.
There are 4*4*6=96 allowed matter words at W=1. No physical charge word is
excluded. The complete N=6 matter-label space used to compute the two products
in G1 has dimensions (36,96,36) at W=(0,1,2), hence 168 labels in total.

Let F=sum_a F_a be the unsigned outward transport. On an edge (a,b), F moves
q_a=+1 or -1 from occupied a to empty b and shifts E_ab by -q_a. The original
resolved j_(ab,sigma) fills two empty endpoints with charges sigma,-sigma and
shifts E_ab by sigma. The coherent edge mark is the original sum of the two
resolved marks. All rotor shift amplitudes are one. The operator under study is

    G1=Pi1(FF* - F*F)Pi1,
    Gamma1=Pi1 sum_j j*j Pi1,
    A1=-i delta G1-kappa Gamma1/2,       V(tau)=exp(tau A1).

The two products in G1 use W=0 and W=2 intermediate words, respectively. They
are not replaced by the low-band Hamiltonian, and their signs are not changed.
Both G1 and Gamma1 are bounded, with G1 self-adjoint and Gamma1 nonnegative.
For example ||F||<=12 gives ||G1||<=288. The semigroup is therefore defined by
a bounded-operator power series and is contractive:

    d/dtau ||V(tau)r||^2 = -kappa <V(tau)r,Gamma1 V(tau)r> <= 0.

There is at most one edge connecting the two vacancies. If they are adjacent,
the two resolved signs each have j*j=1 on that physical word; if they are not
adjacent, every mark vanishes. The two resolved ranges on a fixed edge have
different endpoint charges, so their cross j_+*j_- is exactly zero. Consequently
both original instruments give exactly

    Gamma1=2 P_bright,

where bright means adjacent vacancies. On the cube each A vertex has exactly
one nonadjacent B vertex, its opposite. The dark space of charge labels has
4*6=24 labels; the bright space has 72. This equality is an operator statement
on the physical flux space, not a declaration that all states in ker Gamma1
remain dark under G1.

The prior fast-band note is an allowed, separately provisional compact-time
premise. It identifies these operators in a particular microscopic limit.
The present semigroup theorem takes the stated rotor operators as its problem
and does not need to assume that microscopic theorem in order to prove their
long-tau behavior. Any subsequent use for its microscopic energy curve remains
conditional on that separate compact-time identification.

## 2. Exact Gauss coordinates and Fourier representation

Use the following spanning tree, in the same A-to-B orientation:

    (01,02,04,31,51,62,37).

The five chords, in their fixed order, are

    (32,54,57,64,67).

For each allowed matter word q, solve the tree incidence equation
`div E0(q)=q-1_A`, with all chord fields set to zero. Leaf elimination gives a
unique integral solution because the total right-hand side is zero. Let c_l
be the fundamental cycle whose l-th chord field is one and whose other chord
fields vanish. Every physical field has the unique form

    E=E0(q)+sum_(l=1)^5 z_l c_l,           z in Z^5.

Indeed subtracting the right-hand side leaves a divergence-free tree-supported
flow, which vanishes by leaf elimination. Thus the physical W=1 Hilbert space
is unitarily identified with

    l2(Z^5) tensor C^96.

This is a basis relabeling of actual Gauss words; there is no finite flux cutoff
and no quotient identifying different physical electric fields. The complete
intermediate N=6 space likewise uses l2(Z^5) tensor C^168.

Choose Fourier convention `rhat(theta)=sum_z exp(i theta.z) r(z)` with normalized
Haar measure on T^5. A link transition changes z_l by its electric shift if the
link is chord l, and changes no cycle coordinate if it is a tree edge. Hence
its fiber matrix entry is exp(i theta_l times shift), or one on a tree edge.
This follows directly from the updated charge word and uniqueness of the tree
reference flow. The control checks this Gauss-coordinate intertwining exactly
for every legal outward move of every one of the 168 N=6 charge labels.
Adjoints then have the conjugate entries.

Consequently G1 is a 96 by 96 Hermitian Laurent-polynomial matrix G(theta),
Gamma1 is the constant matrix 2 P_bright, and the physical semigroup is the
direct integral

    Fourier V(tau) Fourier^-1
      = multiplication by exp[tau A(theta)],
    A(theta)=-i delta G(theta)-kappa P_bright.

The equality follows term by term from the bounded exponential power series.
All fiber matrices are continuous in theta. Their exponentials are contractions
for every real theta, tau>=0, and positive delta,kappa.

## 3. The decisive exact rank certificate

Define the bright-from-dark block

    K(theta)=P_bright G(theta) P_dark : C^24 -> C^72.

It is sufficient to prove that K(theta) is injective for almost every theta.
No full classification of all exceptional fibers is needed.

The independent engine constructs all charge words by lexicographically ordered
six-site occupied subsets, then by the position of their one negative charge.
W=1 labels retain that order. The dark W=1 columns are

    30,31,32,33,34,35,
    42,43,44,45,46,47,
    54,55,56,57,58,59,
    72,73,74,75,76,77.

Choose the 24 bright W=1 rows 0,1,...,23. The resulting square minor at the
chord phases

    (exp(i theta_32),exp(i theta_54),exp(i theta_57),exp(i theta_64),exp(i theta_67))
      =(1,1,1,1,i)

has exact determinant

    -222208 = -2^10 * 7 * 31 != 0.

`EXACT_FIBER_RESULTS_01.json` contains all 576 Gaussian-integer entries of this
minor, its row/column identities, tree/cycle data, exact determinant, and the
complete code-generated certificate. `exact_fiber_control.py` builds F and the
original j matrices from the local definitions using exact SymPy integers and
i, independently of the earlier floating exploratory rank scan. It forms
FF*-F*F on the complete 168-label sector before compressing to W=1. It checks
both original instruments' Gamma matrices and all resolved-range cross terms.

An independent modular Gaussian-integer calculation sends i to 2 in F_5,
which is valid because 2^2=-1 mod 5. Direct modular elimination of K's transpose
finds 24 independent columns and selects the above minor. Its determinant is
2 mod 5. Thus the nonzero determinant assertion does not rest on a numerical
rank tolerance or on small singular values. Exact complex and modular routes
agree. The control does not import any author or earlier campaign builder.

Let p(theta) be this minor's Laurent determinant for general phases. It is not
the zero Laurent polynomial, since its value at the specified point is nonzero.
Its zero set on T^5 has Haar measure zero. For completeness, multiply by a
monomial to obtain a polynomial and induct on the number of torus variables.
As a polynomial in the last variable it has finitely many coefficient
polynomials; at least one is nonzero. Outside the zero set of that coefficient,
which has measure zero by induction, the last-variable polynomial is nonzero
and has finitely many roots. Fubini then proves the assertion. This argument
also applies to complex coefficients. It is not an inference that a single
numerical fiber is representative.

Therefore, outside a measure-zero exceptional set,

    rank K(theta)=24.

The chosen minor may vanish at points where another minor remains invertible;
we do not claim to classify its zero set as exactly the set of dark fibers.

## 4. From almost-everywhere fiber damping to every physical state

Fix a theta where K(theta) is injective. Dissipativity implies that every
eigenvalue of A(theta) has nonpositive real part. Suppose A(theta)v=lambda v
with Re lambda=0 and v nonzero. Taking the real part of the inner product gives

    0=Re <v,A(theta)v> = -kappa ||P_bright v||^2.

Since kappa>0, v lies in the dark space. Projecting the eigenvalue equation to
the bright space then gives

    0=-i delta K(theta)v.

Since delta>0 and K(theta) is injective, v=0, a contradiction. Thus every
eigenvalue has strictly negative real part for almost every theta. Each such
fiber is finite dimensional, so its exponential tends to zero as tau tends
to infinity. Possible Jordan blocks only introduce polynomial factors against
strictly decaying exponentials. No theta-uniform spectral gap is asserted.

For any normalizable physical r, rhat is in L2(T^5;C^96). Almost everywhere,

    ||exp[tau A(theta)] rhat(theta)||^2 -> 0.

For every tau the same quantity is bounded by ||rhat(theta)||^2, by contractivity.
That dominating function is integrable. Dominated convergence and Plancherel
therefore yield

    ||V(tau)r||^2
      = integral_T5 ||exp[tau A(theta)] rhat(theta)||^2 dtheta -> 0.

This proves the requested assertion for every normalizable physical state in
the whole specified sector, not only for finite-support birth vectors. In
particular there is no nonzero normalizable physical state whose norm survives
at infinite fast time. Possible dark eigenvectors in exceptional fibers cannot
produce an L2 state supported on their measure-zero set.

## 5. The zero fiber survives, and why that does not invalidate the theorem

The all-zero Fourier phase has a genuine finite-matrix dark vector. Let v0 be
the equal sum of the 24 dark charge labels, with coefficient one on every label
listed in Section 3 and zero on the other 72. Exact local-matrix multiplication
gives

    Gamma(0) v0=0,       G(0) v0=0,       ||v0||^2=24.

The exact control also finds that K(0) has rank 23 and a one-dimensional kernel,
spanned by this vector. Thus exp[tau A(0)]v0=v0 for every tau. The output JSON
lists all its actual charge words, not merely its dimension or norm.

At a structural level, in FF*-F*F the two-hop histories that move both vacancies
on disjoint edges cancel between the two orderings. The remaining off-diagonal
terms move one vacancy at a time. Starting from opposite holes, moving exactly
one hole gives adjacent holes. The diagonal inward and outward counts are both
three. Hence the dark-to-dark block vanishes; at zero phase the bright
amplitudes of the equal dark sum cancel as checked exactly. The zero-phase
vector is a useful obstruction to the failed strategy of proving strict
damping separately at every fiber.

A state supported only at theta=0 is a delta distribution in Fourier space,
not an element of L2(T^5). Its inverse transform has constant cycle amplitudes
and infinite l2 norm. It is therefore not a surviving normalizable physical
state. A finite packet sharply concentrated near zero is normalizable but
still decays in norm by Section 4.

The zero-fiber vector also establishes the absence of operator-norm decay.
For a fixed finite tau, theta-continuity implies that
`||exp[tau A(theta)]v0/||v0||||` is arbitrarily close to one on a sufficiently
small neighborhood of zero, a set of positive Haar measure. A normalized L2
wave packet supported there has norm after time tau arbitrarily close to one.
Thus

    ||V(tau)||=1       for every finite tau>=0,
    V(tau)r ->0       for every fixed physical r in l2.

There is no contradiction: the wave packet used to approach the operator norm
can depend on tau. This also excludes a common state-independent decay bound
g(tau)->0 multiplying ||r||. No individual decay rate, power-law tail, complete
exceptional-set classification, or classification of finite-spin long-time
behavior is claimed.

## 6. Sequential-limit scope and provenance

The question has fixed positive delta and kappa. At delta=0, the physical dark
subspace does not couple to the bright space and gives surviving normalizable
states. At kappa=0 the entire evolution is unitary. These excluded degenerate
parameters are genuine counterexamples to omitting positivity, and are not
limits over which the asserted long-time convergence is uniform.

If the separately provisional compact-time theorem identifying the actual birth
curve `f_i(tau)=||V(tau)R_i||^2/b_i` is accepted, its finite-support physical R_i
is covered and f_i(tau)->0. This is a sequential statement: first the rotor/
compact joint limit at bounded tau, then tau->infinity for the resulting
semigroup. It supplies no bound uniform in unbounded tau for the finite-epsilon
model. In particular tau=t/epsilon^2 for fixed positive physical t is outside
what has been proved. The argument also does not exchange the finite-spin and
long-tau limits. No heat, work, bath, reservoir, or microscopic fixed-time
energy claim follows here.

The principal allowed compact-time source is bound to SHA256
`f71515321246fd2900b1ca801eb12e816b0a7ab2a1d8f820ae75bb87e28df02a`.
The original compensation/original-mark source identities, current repository
instructions, and pinned planning AGENTS are in SOURCE_BINDINGS.json with exact
snapshots. Current workflow and planning bytes agree with those already read
for the coherent task. No current tail-author packet or peer material was read.
The code is new; inherited model/reasoning were retained; no subagent was used.

The initial numerical scan is retained, including its rank-23 zero-phase row.
The next phase produced rank 24 and was then replaced by the exact Gaussian/
modular proof certificate for the load-bearing rank claim. There were no failed
executions, discarded physical cases, relaxed tolerances, or modified sources.
The scan alone would not establish the theorem. The exact certificate, physical
Gauss decomposition, measure-zero argument, and dominated-convergence step are
all necessary parts of this PRE packet. Its integrity seal validates provenance;
it is not an audit or independent proof of the separately provisional
microscopic compact-time theorem.
