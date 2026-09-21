# Independent polynomial current and four-site classification check

**Results.** The supplied symmetric-tensor construction preserves every
homogeneous product law and has exact product current `J=C grad P`, where P
is the tensor's product expectation. The positive-floor conservative
generators satisfy the hypotheses of the previously sealed conditional
Euler and stationary fluctuation proofs for each fixed finite tensor degree.

The degree-three example has a nonzero direction-independent acoustic pair
at every interior isotropic density when alpha is nonzero, together with
four zero characteristic modes. Its nonlinear currents are not continuously
rotationally covariant, even when evaluated at zero quadrupole. A concrete
rotation counterexample is given below.

The specified four-collinear-site classification contains a symmetric
two-label tensor **and a fully alternating three-label tensor**. The latter
changes microscopic rates but has zero product current. Modulo irrelevant
constants, the proper-cubic-covariant mean-potential space is exactly

    P_i=(u+v rho+w q_i)g_i.

Its all-density nonzero isotropic acoustic family is exactly
`u=0, w=-3v/2, v!=0`. This is a classification for the stated footprint,
central-endpoint antisymmetry and periodic-balance condition, not a
classification of all conservative lattice dynamics.

No primary polynomial, classification, nonlinear, simulation or new growing
product argument was read before sealing. All new calculations and writes
are confined to this directory.

## 1. Arbitrary fixed symmetric tensor degree

Let the seven probabilities be p_0,...,p_6, with sum p_a=1. Let k>=1 be
fixed. For one coordinate direction, S is a symmetric function of k labels.
Write the drive at the edge (x,x+1) as in the supplied specification:

    h_x = sum_{j=0}^{k-1}
      [S(eta_{x-j},...,eta_{x-1},eta_x,eta_{x+2},...,eta_{x+k-j})
       -S(eta_{x-j},...,eta_{x-1},eta_{x+1},eta_{x+2},...,eta_{x+k-j})].

The complete footprint is contained in x-k+1,...,x+k, of size 2k. On a
finite simple torus the stipulated distinct-site condition suffices; for
example a coordinate period at least max(3,2k) suffices. All subsequent
large-N statements hold with k fixed.

### 1.1 Pointwise balance and stationarity

The contexts in each summand exclude both central endpoints. Thus swapping
eta_x and eta_{x+1} sends h_x to -h_x. For both proposed rate choices,

    c_x(eta)-c_x(eta^{x,x+1})=h_x(eta).                  (1)

To sum h along a periodic line, set y=x-j. The jth positive term is S on
y,...,y+k with position j+1 omitted, and the negative term omits position
j. Sum over j after summing over x. Every interior omission cancels, leaving

    sum_x h_x = sum_y [S(eta_y,...,eta_{y+k-1})
                       -S(eta_{y+1},...,eta_{y+k})]=0.  (2)

This is an identity for every configuration. A homogeneous product assigns
equal weight to a configuration and its endpoint swap. Its master-balance
residual, divided by its positive weight, is therefore -sum_x h_x=0.
The same conclusion for products with zero probabilities follows directly
on their invariant support, or by continuity. This proves product
stationarity; detailed balance is not generally implied.

If M_S=max|S|, then |h|<=2k M_S. Hence the positive-part implementation has
rates between its fixed floor and floor+2k M_S, and `K>k M_S` is a sufficient
strictly positive linear-rate choice. A finite collection of direction
tensors has uniform fixed bounds by taking their maximum. No spatial or
cubic covariance of an arbitrary tensor collection is assumed or needed
for (2).

On Z^3 the same fixed bounded finite-range rates give the local process
by thinning Poisson bond clocks at a common ceiling. Backward dependence
paths of length n over a fixed time interval have the usual ordered-clock
factor t^n/n!, with only a fixed number of possible next dependencies at
each step. This excludes infinite finite-time dependence paths and gives
local convergence from expanding tori. Their invariant homogeneous
products then give the corresponding infinite-volume stationary products.

### 1.2 Exact species current and normalization

Temporarily treat all seven p_a as independent variables and define the
homogeneous degree-k polynomial

    P(p)=sum_{a_1,...,a_k} S(a_1,...,a_k) product_j p_{a_j}.

For a species a, orient the instantaneous current as
`c_x(1_{eta_x=a}-1_{eta_{x+1}=a})`. Endpoint interchange and (1) imply

    J_a = (1/2) E[h_x(1_{eta_x=a}-1_{eta_{x+1}=a})]
        = E[h_x 1_{eta_x=a}].

Every one of the k window offsets has the same product expectation. If
`s_a=E S(a,X_2,...,X_k)`, independence gives

    J_a = k p_a[s_a-P]
        = p_a[partial_{p_a}P-kP],       a=0,...,6.       (3)

Euler's homogeneous-polynomial identity gives sum_a J_a=0. The factor k
in the window count is already included in partial P: it must not be added
again or omitted from the subtraction in (3).

For six independent occupied probabilities, put p_0=1-rho,
rho=sum_{a=1}^6 p_a, and let P_tilde be P restricted to that simplex.
With C=diag(p)-p p^T,

    J_occupied = C grad P_tilde.                        (4)

Indeed partial_a P_tilde=partial_a P-partial_0 P, and multiplying by C
subtracts sum_{b=0}^6 p_b partial_b P=kP. Equation (4) applies even when
S has nonzero entries containing vacancies. In that general case one must
not replace the density current by k p_0 P without also checking
partial_0 P=0.

### 1.3 Entropy and previously sealed limit hypotheses

For the product entropy s(p)=sum_{a=0}^6 p_a log p_a, let

    lambda_a=log(p_a/p_0),
    H_s=D^2s=diag(1/p_a)+p_0^(-1)11^T=C^(-1).

At every full-support product,

    H_s J_i=grad P_tilde_i,
    H_s DJ_i=(DJ_i)^T H_s.                             (5)

For the second identity, differentiate the first and antisymmetrize its
two free derivative indices. The Hessian of P_tilde cancels; the derivative
of H_s is the fully symmetric third derivative of s and also cancels.
The entropy flux is lambda dot J_i-P_tilde_i. Thus nonlinear entropy
compatibility holds for every fixed symmetric tensor degree, not merely
at an isotropic background.

Here are the actual changes required in the prior proofs:

- The microscopic support and rate ceiling change from a four-site
  context to at most 2k sites and the bounds above. The floor still controls
  every nearest-neighbor transposition, including two unequal occupied
  labels. The canonical sectors remain exactly the seven label counts.
- Uniform product invariance supplies the same reference entropy
  dissipation budget. The canonical sorting/Poincare argument is
  unchanged. Fixed-support sampling without replacement still differs
  from product sampling by O(1/M) on an M-site block, now with constants
  depending on k. Interior-anchor boundary fractions are O(k/ell).
- Replace the old current and potential by (3)-(5). Their derivatives are
  bounded polynomials on the closed simplex. These are precisely the
  linear and constant-term cancellation identities used in the relative
  entropy proof.
- The independent stationary-fluctuation proof uses the symmetric-part
  Dirichlet comparison, the same count-sector Poincare inequality, and
  the bounded fixed-support current. Its conditional-current Taylor
  remainder has variance O(M^(-2)) exactly as before. No endpoint-only
  rate or reversibility condition is needed.

Consequently, for a given C^2 periodic interior solution of
`partial_t p+sum_i partial_i J_i(p)=0`, initial relative entropy o(N^3)
implies the prior Euler relative-entropy and empirical-profile conclusions
on its fixed smooth time interval. This does not prove existence beyond
that assumed interval or through shocks.

Separately, at a fixed stationary full-support product p, with no births,
fixed positive exchange floor, fixed k and fixed Fourier modes K=2pi m,
the previously proved result is

    sup_{t<=T} ||Y_N(K,t)-exp[-i sum_i K_i DJ_i(p)t]Y_N(K,0)||_2 -> 0.

The supremum remains outside L2. Time T, p, k and modes are fixed as N grows.
No nonstationary fluctuation conclusion or new growing-product theorem is
being imported. Neither limit result follows merely from knowing the
product current; the rate and mixing hypotheses above are needed.

## 2. The specified degree-three example

Write n(a)=1_{a!=0}, f_i(a)=v_a dot e_i, and q_i(a)=f_i(a)^2. For product
means, rho=<n>, q_i=<q_i(a)>, and g_i=<f_i>. The given potential is

    P_i=alpha[(2rho^2-3rho q_i)g_i+3g_i^3].             (6)

An explicit symmetric tensor is

    S_i=alpha[2 Sym(n tensor n tensor f_i)
                -3 Sym(n tensor q_i tensor f_i)
                +3 f_i tensor f_i tensor f_i],         (7)

where Sym averages over all slot permutations. Every entry involving a
vacancy vanishes. Classifying the remaining slots as axial +, axial -,
or transverse gives S_i/alpha in
`{0,+/-1/3,+/-2/3,+/-2,+/-10/3}`. Its exact supremum is therefore
(10/3)|alpha|, so |h|<=20|alpha|.
The six-site string (+i,-i,+i,-i,+i,-i), with its middle pair as the edge,
attains h=-20alpha; endpoint interchange supplies the opposite value.
Thus this is also the sharp drive bound. `K>10|alpha|` ensures a positive
linear floor, and the positive-part ceiling is floor+20|alpha|.

The tensor and rates are covariant under all 48 joint signed-coordinate
transformations. Under a direction reversal the positive-edge
representation reverses the footprint; the symmetric tensor transforms
with the direction sign and the endpoint difference supplies the other
sign. This is cubic covariance, not an action of arbitrary rotations on
the finite label alphabet.

### 2.1 Exact nonlinear currents

For a fixed direction i, define

    R_i=alpha(4rho-3q_i)g_i,
    Q_i=-3alpha rho g_i,
    V_i=alpha(2rho^2-3rho q_i+9g_i^2),
    D_i=R_i-3P_i.

These are respectively the formal rho, q_i and g_i derivatives of P_i,
and the indicated difference. Since partial_0 P_i=0, (3) gives

    J_a^i=p_a[D_i+Q_i q_i(a)+V_i f_i(a)]  (a occupied),
    J_0^i=-3p_0P_i,
    J_rho^i=3(1-rho)P_i,                               (8)
    J_{q_j}^i=q_j D_i+delta_ij(Q_i q_i+V_i g_i),
    J_{g_j}^i=g_j D_i+delta_ij(Q_i g_i+V_i q_i).

Let the two independent diagonal quadrupoles be
`z_j=q_j-rho/3`, with sum_j z_j=0. Evaluating (8) at q_i=rho/3 for all i,
while keeping the vector g arbitrary within the physical domain, gives

    J_rho^i=3alpha(1-rho)(rho^2 g_i+3g_i^3),            (9)

    J_{g_j}^i=(alpha rho^3/3)delta_ij
                +3alpha[rho(1-rho)g_i-3g_i^3]g_j,     (10)

    J_{z_j}^i=3alpha(3delta_ij-1)g_i^3.                (11)

The coefficient +3g_i^3 in (6) cancels the diagonal g_i^2 term in (10).
It does not cancel the cubic population current, the cubic quadrupole
current, or the quartic anisotropic term in the vector current.

Equations (9)-(11) are evaluations of the full six-field product fluxes.
They are not an assertion that z=0 is a closed nonlinear evolution
manifold. For example, a smooth profile with constant rho, z=0 and
g=(g_1(X_1),0,0) produces quadrupole fluxes
`(J_z1^1,J_z2^1,J_z3^1)=(6,-3,-3)alpha g_1^3`.
When partial_1 g_1^3 is nonzero, the Euler equation immediately generates
nonzero quadrupoles. The underlying six-state vector alphabet has only
diagonal second moments; no five-component continuously rotating
quadrupole representation has been added.

### 2.2 Complete isotropic linear spectrum

At p_a=rho/6, g=0 and q_i=rho/3. Hold alpha fixed when differentiating.
For a real spatial direction nu, set D_nu=diag(nu_1,nu_2,nu_3). In the six
variables (delta q,delta g), the complete directional Jacobian is

    A(nu) = [[0, alpha rho^2(1-rho) 11^T D_nu],
             [alpha rho^2 D_nu 11^T, 0]].              (12)

Its characteristic polynomial and spectrum are

    det(lambda I-A)=lambda^4
        [lambda^2-3alpha^2 rho^4(1-rho)|nu|^2],         (13)

    +/- |alpha|rho^2 sqrt(3(1-rho)) |nu|, 0,0,0,0.     (14)

For alpha!=0, 0<rho<1 and nu!=0 it has rank two and a four-dimensional
semisimple kernel. The zero modes are the two sum-zero q perturbations
and the two vector perturbations transverse to nu. The propagating
population/vector equations are

    partial_t delta rho+3alpha rho^2(1-rho) div delta g=0,
    partial_t delta g+alpha rho^2 grad delta rho=0.      (15)

The sound-speed square is `3alpha^2 rho^4(1-rho)`. The full spectrum is
direction independent at every fixed interior rho. Speed nevertheless
depends on density. If alpha=0, rho=0, or nu=0 all eigenvalues are zero.
At rho=1 the formal unconstrained six-variable matrix can be nonzero
nilpotent; its restriction to the fixed-full-occupancy tangent
delta rho=0 is zero. Interior diagonalizability is not extended to that
boundary.

### 2.3 Rotational scope and exact counterexample

The propagating linear population/vector subsystem (15) has ordinary
continuous rotational covariance. This and the isotropic spectrum do not
establish continuous covariance of the full nonlinear color-state family.
For (9), the vector `(g_1^3,g_2^3,g_3^3)` is not a rotational vector under
general rotations.

An exact counterexample stays inside the full-support physical domain.
Take alpha=1, rho=1/2, q_i=1/6 and g=(1/12,0,0). Rotate g by 45 degrees
about the third axis, leaving q_i=rho/3. Both the original and rotated
probability vectors are strictly positive. If R denotes that rotation,

    J_rho(Rg)-R J_rho(g)
       =(-sqrt(2)/1536,-sqrt(2)/1536,0) != 0.           (16)

Hence even the zero-quadrupole evaluation of the nonlinear density flux
fails continuous rotational covariance. In (10) the first two terms are
rotationally covariant, but `-9alpha g_i^3 g_j` is not. The failures start
at cubic order in g for population/quadrupole currents and quartic order
for the vector current. These formal orders are useful local information;
they are not an exact finite-amplitude rotational theorem or a closed
four-field hydrodynamics.

## 3. Complete four-collinear-site drive classification

This section uses only the following assumptions for a function of four
labels:

    h(l,a,b,r)=-h(l,b,a,r),
    sum_x h(eta_{x-1},eta_x,eta_{x+1},eta_{x+2})=0
                                      on every periodic string.        (17)

The rates still use (1). No special content geometry is needed until
Section 4.

### 3.1 Periodic zero sum is a three-site coboundary

Use the directed full de Bruijn graph whose vertices are triples (l,a,b)
and whose edges are quadruples (l,a,b,r), directed from (l,a,b) to
(a,b,r). The graph is strongly connected. Every directed closed walk is
a periodic string, and (17) says that the sum of h around it is zero.
If only strings of length at least four are used to impose distinct
footprint positions, repeat any shorter closed walk sufficiently many
times; its sum is still forced to vanish.

Fix a base vertex. The sum of h along a directed path from it to a vertex
is independent of the path: append one common return path to the base
and use the zero closed-walk sums. Its negative defines G, with

    h(l,a,b,r)=G(l,a,b)-G(a,b,r).                       (18)

G is unique up to a constant. Conversely every such coboundary has zero
periodic sum. Thus no unproved cohomology assumption is being inserted
into the classification.

### 3.2 Endpoint antisymmetry fixes the form of G

Apply (17) to (18):

    G(l,a,b)+G(l,b,a)=G(a,b,r)+G(b,a,r).                (19)

The common quantity is independent of both l and r and is symmetric in
a,b. Call it 2S(a,b). Define

    G_S(x,y,z)=S(x,y)+S(y,z)-S(x,z).

Then G-G_S is antisymmetric under interchange of its first two slots
and under interchange of its last two slots, by (19). Those adjacent
transpositions generate the permutation group, so it is a fully
alternating three-label tensor A. Therefore the complete decomposition is

    G(x,y,z)=S(x,y)+S(y,z)-S(x,z)+A(x,y,z),             (20)

    h(l,a,b,r)=S(l,a)+S(a,r)-S(l,b)-S(b,r)
                          +A(l,a,b)-A(a,b,r).         (21)

Here S is symmetric and A is fully alternating. Conversely (21) obeys
both parts of (17). A is unique. The only ambiguity in S is addition
of one constant to every entry, which changes G by that constant and
leaves h unchanged.

For seven labels, S has 28 parameters, A has 35, and the h-space has
dimension `28+35-1=62`. Omitting A would miss 35 independent drives.
This is not merely a harmless alternative representation of the same
microscopic S-drive.

### 3.3 Product currents and the alternating sector

Because a cyclic permutation of three slots preserves an alternating
tensor's sign,

    A(l,a,b)-A(a,b,r)=A(a,b,l)-A(a,b,r).

Under a homogeneous product, l and r are independent identical samples.
Thus this expression has conditional mean zero given the endpoints a,b.
The alternating sector contributes exactly zero to every mean species
current. This remains true for the nonlinear positive-part rate: by (1)
the mean current only uses h/2, so additivity of currents does not require
additivity of the rates themselves.

Let

    P_i(p)=sum_{a,b} S_i(a,b)p_a p_b.

The complete product current of (21) is therefore

    J_a^i=2p_a[(S_i p)_a-P_i],                         (22)

for all seven labels, or `J_occupied^i=C grad P_tilde_i`. The alternating
sector can alter activity and other microscopic properties despite being
invisible to this product flux.

## 4. Proper-cubic covariance and the mean-potential space

Proper cubic rotations are the 24 signed coordinate permutations with
determinant +1, acting jointly on space and labels. When a positive edge
is sent to a negative coordinate direction its positive-coordinate
representation reverses the word (l,a,b,r). Directly from (21),

    h_S(r,b,a,l)=-h_S(l,a,b,r),
    h_A(r,b,a,l)=+h_A(l,a,b,r).                         (23)

Consequently the symmetric tensors transform as a vector indexed by the
edge direction, modulo their constant gauge. Normalize S_i(0,0)=0 to
remove that gauge. Then their mean potential P_i is exactly a vector
covariant. The alternating tensor collection instead transforms with the
unoriented axis index, without the direction sign. It cannot add a new
mean potential because its product current vanishes.

### 4.1 Complete quadratic vector-covariant space

On the simplex, P_i is a polynomial of degree at most two in the six
variables q_1,q_2,q_3,g_1,g_2,g_3. Its constant term can be set to zero.
Consider the subgroup of proper rotations that flips any two coordinate
signs. For a vector component i, the only allowed degree-at-most-two
monomials are

    g_i,  q_1 g_i, q_2 g_i, q_3 g_i,  g_j g_k
                          ({i,j,k}={1,2,3}).

A 90-degree rotation about axis i fixes the component i, interchanges
q_j,q_k, and changes g_j g_k to its negative. Thus the coefficient of
g_j g_k is zero and the two transverse q coefficients agree. Proper
rotations permuting axes then identify the coefficients between the
three components. The exact space is therefore

    P_i=(u+v rho+w q_i)g_i,             u,v,w real.      (24)

All three polynomials are attained by symmetric tensors:

    S_i(a,b)=(u/2)[f_i(a)+f_i(b)]
       +(v/2)[n(a)f_i(b)+f_i(a)n(b)]
       +(w/2)[q_i(a)f_i(b)+f_i(a)q_i(b)].              (25)

The first term uses sum_a p_a=1. These currents are the earlier
axis-balanced family under `v=2EA, w=2EB`, but the preceding argument
classifies the whole specified mean-potential space rather than assuming
that parameterization is exhaustive.

There is also a nonzero proper-cubic microscopic alternating witness:

    A_i(a,b,c)=det[v_a,v_b,v_c], independent of i.       (26)

It is invariant under proper rotations; (23) handles orientation reversal.
For (l,a,b,r)=(+e1,+e2,+e3,0), its drive is 1. It cannot be represented
by a symmetric pair drive because the alternating part in (20) is unique.
It has zero product current at every p. Under spatial/content inversion
the drive becomes -1, so the positive-part rates with floor 1 change from
2 to 1. This proper-cubic witness is not covariant under improper
transformations. Requiring all 48 cubic transformations would remove
this particular chiral witness; proper and full cubic symmetry must not
be conflated.

### 4.2 All-density directional isotropy in (24)

For clarity the exact nonlinear species current from (24) is

    U_i=u+v rho+w q_i,       Z_i=u+2v rho+2w q_i,
    J_a^i=p_a[U_i f_i(a)+(v+w q_i(a)-Z_i)g_i].          (27)

At p_a=rho/6, define

    a_*=u+rho(v+2w/3),
    beta=(rho/3)[v-u-2rho(v+w/3)],
    gamma=v rho/3,
    Z=u+2rho(v+w/3),       Q=(1-rho)Z^2.

In (delta q,delta g), the full directional matrix is

    [[0, (a_* I+beta 11^T)D_nu],
     [D_nu(a_* I+gamma 11^T), 0]].                    (28)

The three squared characteristic speeds are the eigenvalues of

    diag(nu_i^2)[a_*^2 I+b_*11^T],
    b_*=a_*(beta+gamma)+3beta gamma,
    a_*^2+3b_*=Q.                                    (29)

The identities `a_*+3beta=(1-rho)Z` and `a_*+3gamma=Z` prove the last
equality and Q>=0. In a unit axis direction the squared speeds are
`(2a_*^2+Q)/3,0,0`; in a unit body-diagonal direction they are
`a_*^2/3,a_*^2/3,Q/3`.

Any nonzero pair present with the same speed in every direction must
appear in both lists. Equality with a_*^2/3 would force a_*^2+Q=0,
which gives zero speed. Equality with Q/3 requires a_*=0. Conversely,
when a_*=0 and v!=0, (28) has exactly one nonzero isotropic pair and
four semisimple zero modes, with

    c(rho)^2=v^2 rho^2(1-rho)/3.                       (30)

Thus at a fixed interior rho the condition is a_*(rho)=0 and v!=0.
For fixed coefficients to satisfy it at every 0<rho<1, the affine
polynomial a_*(rho) must vanish identically. The exact answer is

    u=0,       w=-3v/2,       v!=0.                    (31)

Invisible alternating terms and swap-symmetric changes of rate cannot
alter this product-current conclusion. They do not cease to matter to
every other microscopic observable.

## 5. Independent exact controls and unsuccessful routes

`python3 independent_check.py > RUN.log 2>&1` completed **33 grouped
checks, zero failures**. RESULTS.json and the complete RUN.log are
byte-identical. The checker was written without importing an earlier
checker or primary code. All algebra, enumeration and finite-field rank
calculations are exact; seeded strings are supplementary examples, not
the proof of arbitrary-period balance.

- At degrees k=1,...,5, nontrivial symmetric tensors satisfy pointwise
  balance and endpoint antisymmetry on 100 seeded strings each. Exact
  product summation checks all seven currents and the factor k against
  (3) at a full-support nonuniform product.
- For the cubic tensor, all 343 entries, all 48 signed-coordinate
  transformations, and all 117,649 six-site strings are used to check
  tensor normalization/covariance, the sharp drive bound, and the exact
  currents for both rate implementations. At alpha=1, K=11 or floor=1,
  the rate ranges are [1,21]. Symbolic six-field differentiation verifies
  (8)-(14); (16) is an exact algebraic counterexample.
- The 343-dimensional triple-potential space is constrained by (19).
  The integer constraint matrix has rank at least 280, computed exactly
  modulo the prime 1009. An explicit 63-dimensional rational kernel
  consisting of the 28 symmetric and 35 alternating basis tensors proves
  rank at most 280. Thus this combination establishes the exact rational
  rank, not just a rank guess from one prime. The resulting h-image has
  rank 62; the one constant gauge is checked directly.
- Proper-cubic covariance imposes rank at least 81 on the 84 symmetric
  tensor coefficients for three directions. The three explicit rational
  tensors in (25) lie in its kernel and are independent, so the exact
  remaining dimension is three. The determinant witness (26) is checked
  against all local words and all proper cubic rotations, and its actual
  positive-part product currents are exactly zero.

One checker-development failure is preserved. SymPy's characteristic
polynomial used a new formal symbol named z without the `real` assumption,
whereas the comparison target used a different symbol named z with that
assumption. Their printed names agreed, but their symbolic identities did
not. Explicit substitution of the polynomial generator into the requested
symbol made the exact difference zero. The failed log, completed-check
prefix, source hash and diagnosis are in ATTEMPT_1*; the corrected full
run is the one counted above. A separate source-hash bookkeeping attempt
used the parent of a relative `Path('.')` instead of its resolved absolute
path and found no sibling file; it was corrected before sealing. It read
no unintended source and changed no scientific calculation. This is
recorded in EXECUTION_NOTES.md.

Two tempting mathematical routes fail and have not been used:

1. Dropping the alternating part of a four-site coboundary is false;
   (26) is a nonzero counterexample even with proper cubic covariance.
2. Inferring nonlinear rotational covariance from the all-direction
   balanced spectrum is false; (16) gives an explicit defect, and (11)
   shows that zero quadrupole does not generically persist spatially.

## 6. Scope, dependencies and seal

All three requested targets are resolved under their displayed premises.
The tensor degree, local alphabet, rate coefficients and positive floor
are fixed; the torus has distinct footprint sites. The Euler conclusion is
conditional on the given smooth interior solution and initial small
relative entropy. The fluctuation conclusion requires a stationary
full-support product and fixed finite times/modes. There is no exact
microscopic-wave theorem, no growth fluctuation result, and no extension
to a vanishing floor or increasing interaction range.

The four-site classification assumes periodic zero sum for that
collinear drive and antisymmetry under swapping the central endpoints.
It does not classify larger footprints, cancellations between different
spatial directions, processes preserving only a smaller product family,
nonproduct invariant laws, or all conservative generators. The cubic
tensor construction has a six-site footprint and lies outside the
quadratic four-site potential class. No universal impossibility or
physics/TOE conclusion is drawn.

The unchanged independent dependencies are:

| Relative sibling source | SHA-256 |
|---|---|
| independent_context_euler/REPORT.md | 60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3 |
| independent_context_euler/PRE_SOURCE_SEAL.json | 48dda0ccb30539906dd6274bbf8736258727077c0018bb89c604f491164a1fa9 |
| independent_axis_balanced_context/REPORT.md | b9cedcafccb48dfcd2503e5f00569a547288d4dcef0fb7dfca832565aec8f7cf |
| independent_axis_balanced_context/PRE_SOURCE_SEAL.json | 8519e354a43ed16b9c176aa3e7e4672e6b3e6e1101e83af040555323aa3390a2 |
| independent_context_fluctuations/REPORT.md | 772046745ac814c32adcd8f36e3c8415ddf4a3a4b37435e8992441c6c8d5be68 |
| independent_context_fluctuations/PRE_SOURCE_SEAL.json | c729b0f85e0350b834380909001ef62f0db0378fdf114b108f5feef7f6e0e8d1 |

The first two reports were read completely where used in this task. The
fluctuation proof was just independently completed and its unchanged
argument is reused. No external literature, new primary source or simulation
outcome was imported. PRE_SOURCE_SEAL.json records the dependency and new
artifact identities. This is a bounded mathematical check, not an audit,
publication approval or retained-status verdict.
